"""Local Windows media transport and per-application audio bridge for ISB Menu."""
import argparse
import asyncio
import base64
import hashlib
import hmac
import json
import math
import os
from pathlib import Path
import secrets
import sys
sys.coinit_flags = 0  # Media thumbnail completion must not depend on a GUI STA pump.
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit, parse_qs

if not getattr(sys, 'frozen', False):
    candidate = Path(__file__).resolve().parent.parent / 'work/media-deps'
    if candidate.is_dir():
        sys.path.insert(0, str(candidate))

from winrt.windows.media.control import (
    GlobalSystemMediaTransportControlsSessionManager as Manager,
    GlobalSystemMediaTransportControlsSessionPlaybackStatus as Status,
)
from pycaw.pycaw import AudioUtilities
from winrt.windows.storage.streams import DataReader


def app_name(source):
    for word in ('spotify', 'opera', 'msedge', 'chrome', 'firefox', 'vlc'):
        if word in source.lower():
            return {'msedge': 'Edge', 'vlc': 'VLC'}.get(word, word.title())
    return source.split('!')[-1].removesuffix('.exe')[:60]


def audio_sessions(source):
    name = app_name(source).lower()
    expected = {'edge': 'msedge', 'spotify': 'spotify', 'opera': 'opera',
                'chrome': 'chrome', 'firefox': 'firefox', 'vlc': 'vlc'}.get(name)
    if expected is None:
        return []
    found = []
    for session in AudioUtilities.GetAllSessions():
        try:
            if session.Process and session.Process.name().lower() == expected + '.exe':
                found.append(session.SimpleAudioVolume)
        except Exception:
            continue
    return found


class Media:
    def __init__(self, manager):
        self.manager = manager
        self.sessions = {}
        self.covers = {}

    def refresh(self):
        self.sessions = {}
        counts = {}
        for session in list(self.manager.get_sessions())[:16]:
            source = session.source_app_user_model_id
            ordinal = counts.get(source, 0)
            counts[source] = ordinal + 1
            key = hashlib.sha256((source + '#' + str(ordinal)).encode()).hexdigest()[:16]
            self.sessions[key] = session
        return self.sessions

    def selected(self, key):
        self.refresh()
        if key:
            if key not in self.sessions:
                raise ValueError('Der ausgewählte Player ist nicht mehr verfügbar.')
            return key, self.sessions[key]
        current = self.manager.get_current_session()
        for key, session in self.sessions.items():
            if session == current:
                return key, session
        for key, session in self.sessions.items():
            if session.get_playback_info().playback_status == Status.PLAYING:
                return key, session
        return next(iter(self.sessions.items()), ('', None))

    async def cover(self, session, properties):
        source = session.source_app_user_model_id
        identity = (properties.title, properties.artist, properties.album_title)
        previous = self.covers.get(source)
        if previous and previous[0] == identity:
            return previous[1]
        result = {'id': '', 'data': ''}
        try:
            if properties.thumbnail:
                stream = await properties.thumbnail.open_read_async()
                try:
                    size = stream.size
                    if 0 < size <= 1_000_000:
                        reader = DataReader(stream.get_input_stream_at(0))
                        try:
                            loaded = await reader.load_async(size)
                            data = bytearray(loaded)
                            reader.read_bytes(data)
                            if data[:8] == b'\x89PNG\r\n\x1a\n' or data[:2] == b'\xff\xd8':
                                result = {'id': hashlib.sha256(data).hexdigest()[:24], 'data': base64.b64encode(data).decode('ascii')}
                        finally:
                            reader.close()
                finally:
                    stream.close()
        except Exception:
            pass
        self.covers[source] = (identity, result)
        if len(self.covers) > 16:
            self.covers.pop(next(iter(self.covers)))
        return result

    async def state(self, key='', known_cover=''):
        key, session = self.selected(key)
        sources = [{'id': k, 'name': app_name(s.source_app_user_model_id),
                    'playing': s.get_playback_info().playback_status == Status.PLAYING}
                   for k, s in self.sessions.items()]
        if session is None:
            return {'available': False, 'sources': sources, 'message': 'Kein Windows-Medienplayer aktiv.'}
        properties = await session.try_get_media_properties_async()
        try:
            cover = await asyncio.wait_for(self.cover(session, properties), timeout=2)
        except asyncio.TimeoutError:
            cover = {'id': '', 'data': ''}
        info = session.get_playback_info()
        timeline = session.get_timeline_properties()
        controls = info.controls
        volume_sessions = audio_sessions(session.source_app_user_model_id)
        volume = volume_sessions[0].GetMasterVolume() if volume_sessions else None
        position = timeline.position.total_seconds()
        duration = timeline.end_time.total_seconds()
        playing = info.playback_status == Status.PLAYING
        if playing:
            import datetime
            elapsed = (datetime.datetime.now(datetime.timezone.utc) - timeline.last_updated_time).total_seconds()
            position = min(duration, position + max(0, elapsed)) if duration > 0 else position
        return {'available': True, 'selected': key, 'source': app_name(session.source_app_user_model_id),
                'title': properties.title or 'Ohne Titel', 'artist': properties.artist or '',
                'playing': playing, 'position': max(0, position), 'duration': max(0, duration),
                'volume': volume, 'sources': sources,
                'coverId': cover['id'], 'cover': cover['data'] if cover['id'] != known_cover else '',
                'controls': {'toggle': bool(controls.is_play_pause_toggle_enabled),
                             'next': bool(controls.is_next_enabled), 'previous': bool(controls.is_previous_enabled),
                             'seek': bool(controls.is_playback_position_enabled), 'volume': bool(volume_sessions)}}

    async def command(self, data):
        key, session = self.selected(str(data.get('source', '')))
        if session is None:
            raise ValueError('Kein Player verfügbar.')
        command = data.get('command')
        controls = session.get_playback_info().controls
        capabilities = {'toggle': controls.is_play_pause_toggle_enabled,
                        'next': controls.is_next_enabled, 'previous': controls.is_previous_enabled,
                        'seek': controls.is_playback_position_enabled}
        if command in capabilities and not capabilities[command]:
            raise ValueError('Dieser Player unterstützt diese Aktion nicht.')
        if command == 'toggle':
            ok = await session.try_toggle_play_pause_async()
        elif command == 'next':
            ok = await session.try_skip_next_async()
        elif command == 'previous':
            ok = await session.try_skip_previous_async()
        elif command == 'seek':
            value = float(data.get('value', 0))
            timeline = session.get_timeline_properties()
            if not math.isfinite(value):
                raise ValueError('Ungültige Position.')
            value = max(timeline.min_seek_time.total_seconds(), min(value, timeline.max_seek_time.total_seconds()))
            ok = await session.try_change_playback_position_async(int(value * 10_000_000))
        elif command == 'volume':
            value = float(data.get('value', 0))
            if not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError('Ungültige Lautstärke.')
            targets = audio_sessions(session.source_app_user_model_id)
            if not targets:
                raise ValueError('App-Lautstärke ist derzeit nicht verfügbar.')
            for target in targets:
                target.SetMasterVolume(value, None)
            ok = True
        else:
            raise ValueError('Unbekannte Aktion.')
        if not ok:
            raise ValueError('Der Player hat die Aktion nicht angenommen.')
        return {'ok': True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--client-workspace', type=Path)
    args = parser.parse_args()
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    media = Media(loop.run_until_complete(Manager.request_async()))
    token = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_):
            pass

        def respond(self, status, value):
            body = json.dumps(value, ensure_ascii=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def authorized(self):
            # Browser origins are denied. Only the configured local client is accepted.
            return not self.headers.get('Origin') and hmac.compare_digest(self.headers.get('Authorization', ''), 'Bearer ' + token)

        def do_GET(self):
            if not self.authorized():
                return self.respond(403, {'ok': False, 'error': 'Nicht autorisiert.'})
            url = urlsplit(self.path)
            if url.path != '/state':
                return self.respond(404, {'ok': False})
            try:
                selected = parse_qs(url.query).get('source', [''])[0]
                known_cover = parse_qs(url.query).get('cover', [''])[0]
                self.respond(200, loop.run_until_complete(media.state(selected, known_cover)))
            except Exception as error:
                self.respond(503, {'ok': False, 'error': str(error)[:160]})

        def do_POST(self):
            if not self.authorized():
                return self.respond(403, {'ok': False, 'error': 'Nicht autorisiert.'})
            if self.path != '/command':
                return self.respond(404, {'ok': False})
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 4096:
                    raise ValueError('Ungültige Anfrage.')
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise ValueError('Ungültige Anfrage.')
                self.respond(200, loop.run_until_complete(media.command(data)))
            except Exception as error:
                self.respond(400, {'ok': False, 'error': str(error)[:160]})

    server = HTTPServer(('127.0.0.1', args.port), Handler)
    server.timeout = .5
    default = Path(os.environ.get('LOCALAPPDATA', '')) / 'Real/workspace'
    workspace = args.client_workspace or (default if default.is_dir() else Path.home() / 'ISBMenu')
    workspace.mkdir(parents=True, exist_ok=True)
    config = workspace / 'ISBMenu-media-bridge.json'
    config.write_text(json.dumps({'port': args.port, 'token': token}), encoding='utf-8')
    try:
        server.serve_forever(poll_interval=.5)
    finally:
        server.server_close()
        loop.close()


if __name__ == '__main__':
    main()
# -- by Larsiopuw
