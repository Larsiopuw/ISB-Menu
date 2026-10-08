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
import time
import threading
import shutil
sys.coinit_flags = 0  # Media thumbnail completion must not depend on a GUI STA pump.
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
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
        self.browser = BrowserMedia()

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
        browser_sources = self.browser.sources()
        if key.startswith('yt:'):
            self.refresh()
            sources = [{'id': k, 'name': app_name(s.source_app_user_model_id),
                        'playing': s.get_playback_info().playback_status == Status.PLAYING}
                       for k, s in self.sessions.items()] + browser_sources
            result = self.browser.state(key, sources)
            for identity, cover in self.covers.values():
                if identity[0] == result['title']:
                    result['coverId'] = cover['id']
                    result['cover'] = cover['data'] if cover['id'] != known_cover else ''
                    break
            return result
        key, session = self.selected(key)
        sources = [{'id': k, 'name': app_name(s.source_app_user_model_id),
                    'playing': s.get_playback_info().playback_status == Status.PLAYING}
                   for k, s in self.sessions.items()] + browser_sources
        if session is None:
            if browser_sources:
                return self.browser.state(browser_sources[0]['id'], sources)
            return {'available': False, 'sources': sources, 'message': 'Kein Windows-Medienplayer aktiv.'}
        properties = await session.try_get_media_properties_async()
        if app_name(session.source_app_user_model_id) in ('Opera', 'Chrome', 'Edge', 'Firefox'):
            browser_key = self.browser.match(properties.title)
            if browser_key:
                result = self.browser.state(browser_key, sources)
                try:
                    cover = await asyncio.wait_for(self.cover(session, properties), timeout=2)
                    result['coverId'] = cover['id']
                    result['cover'] = cover['data'] if cover['id'] != known_cover else ''
                except asyncio.TimeoutError:
                    pass
                return result
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
        seek_min = max(0, timeline.min_seek_time.total_seconds())
        seek_max = max(0, timeline.max_seek_time.total_seconds())
        # Chromium uses a negative end timestamp for an unbounded livestream.
        live = duration < 0
        playing = info.playback_status == Status.PLAYING
        if playing:
            import datetime
            elapsed = (datetime.datetime.now(datetime.timezone.utc) - timeline.last_updated_time).total_seconds()
            position = min(duration, position + max(0, elapsed)) if duration > 0 else position
        return {'available': True, 'selected': key, 'source': app_name(session.source_app_user_model_id),
                'title': properties.title or 'Ohne Titel', 'artist': properties.artist or '',
                'playing': playing, 'position': max(0, position), 'duration': max(0, duration),
                'live': live, 'seekMin': seek_min, 'seekMax': seek_max,
                'volume': volume, 'sources': sources,
                'coverId': cover['id'], 'cover': cover['data'] if cover['id'] != known_cover else '',
                'controls': {'toggle': bool(controls.is_play_pause_toggle_enabled),
                             'next': bool(controls.is_next_enabled), 'previous': bool(controls.is_previous_enabled),
                             'seek': bool(controls.is_playback_position_enabled and seek_max > seek_min),
                             'volume': bool(volume_sessions), 'mute': False}}

    async def command(self, data):
        if str(data.get('source', '')).startswith('yt:'):
            return await self.browser.command(data)
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


class BrowserMedia:
    """Authenticated snapshots and acknowledged commands for YouTube-only tabs."""
    def __init__(self):
        self.tabs = {}
        self.pending = {}
        self.counter = 0
        self.lock = threading.Lock()

    def sources(self):
        with self.lock:
            current = time.monotonic()
            self.tabs = {k: v for k, v in self.tabs.items() if current-v['updated'] < 5}
            return [{'id': key, 'name': 'YouTube' if len(self.tabs)==1 else 'YouTube '+str(i+1),
                     'playing': value['state']['playing']} for i, (key, value) in enumerate(self.tabs.items())]

    def exchange(self, data):
        tab = data.get('tab')
        if type(tab) is not int or tab < 0:
            raise ValueError('Ungültiger Player.')
        key = 'yt:'+str(tab)
        state = data.get('state')
        with self.lock:
            for ack in data.get('acknowledgements', [])[:8]:
                item = self.pending.get(ack.get('id'))
                if item and item['source']==key:
                    item['result'] = {'ok': ack.get('ok') is True, 'error': str(ack.get('error','Aktion nicht angenommen.'))[:160]}
            if state is None:
                self.tabs.pop(key, None)
            elif isinstance(state, dict):
                safe = {'title': str(state.get('title','YouTube'))[:240], 'artist': str(state.get('artist',''))[:160],
                        'playing': state.get('playing') is True, 'muted': state.get('muted') is True,
                        'live': state.get('live') is True}
                for field in ('position', 'duration', 'seekMin', 'seekMax', 'volume', 'liveStartedAt'):
                    value = state.get(field, 0)
                    if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                        raise ValueError('Ungültige Player-Daten.')
                    safe[field] = value
                safe['volume'] = min(1, safe['volume'])
                safe['controls'] = {'toggle': True, 'mute': True, 'volume': True, 'previous': False, 'next': False,
                                    'seek': safe['seekMax'] > safe['seekMin']}
                self.tabs[key] = {'state': safe, 'updated': time.monotonic()}
            commands = []
            for item in self.pending.values():
                if item['source']==key and not item.get('sent'):
                    item['sent'] = True
                    commands.append({k: item[k] for k in ('id','command','value')})
            return {'commands': commands}

    def match(self, title):
        with self.lock:
            for key, item in self.tabs.items():
                if time.monotonic()-item['updated'] < 5 and item['state']['title']==title:
                    return key
        return None

    def state(self, key, sources):
        with self.lock:
            item = self.tabs.get(key)
            if not item or time.monotonic()-item['updated'] >= 5:
                raise ValueError('YouTube-Verbindung unterbrochen. YouTube-Tab neu laden.')
            state = dict(item['state'])
            age = time.monotonic()-item['updated']
        if state['playing']:
            state['position'] += age
            if state['live']:
                state['seekMax'] += age
            else:
                state['position'] = min(state['duration'], state['position'])
        return dict(state, available=True, selected=key, source='YouTube', sources=sources, coverId='', cover='', browser=True)

    async def command(self, data):
        source = str(data.get('source',''))
        state = self.state(source, [])
        command = data.get('command')
        if not state['controls'].get(command):
            raise ValueError('YouTube unterstützt diese Aktion aktuell nicht.')
        value = data.get('value')
        if command in ('seek','volume'):
            if type(value) not in (int,float) or not math.isfinite(value):
                raise ValueError('Ungültiger Wert.')
            value = max(state['seekMin'], min(state['seekMax'], value)) if command=='seek' else max(0,min(1,value))
        if command=='mute' and type(value) is not bool:
            raise ValueError('Ungültige Stummschaltung.')
        with self.lock:
            self.counter += 1
            item = {'id': self.counter, 'source': source, 'command': command, 'value': value}
            self.pending[item['id']] = item
        try:
            deadline = time.monotonic()+3
            while time.monotonic() < deadline:
                with self.lock:
                    result = item.get('result')
                if result is not None:
                    if not result['ok']:
                        raise ValueError(result['error'])
                    return {'ok': True}
                await asyncio.sleep(.03)
            raise ValueError('YouTube antwortet nicht. Bitte den YouTube-Tab neu laden.')
        finally:
            with self.lock:
                self.pending.pop(item['id'], None)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--client-workspace', type=Path)
    parser.add_argument('--prepare-browser', action='store_true')
    args = parser.parse_args()
    browser_home = Path(os.environ.get('LOCALAPPDATA', str(Path.home()))) / 'ISBMenu'
    browser_home.mkdir(parents=True, exist_ok=True)
    browser_config = browser_home / 'youtube-connection.json'
    if browser_config.is_file():
        browser_token = json.loads(browser_config.read_text(encoding='utf-8'))['token']
    else:
        browser_token = secrets.token_urlsafe(32)
        browser_config.write_text(json.dumps({'token': browser_token}), encoding='utf-8')
    if args.prepare_browser:
        template = Path(__file__).resolve().parent / 'ISB-YouTube'
        target = browser_home / 'ISB-YouTube'
        shutil.copytree(template, target, dirs_exist_ok=True)
        (target/'connection.js').write_text('const ISB_CONNECTION = '+json.dumps({'token': browser_token})+';\n// -- by Larsiopuw\n', encoding='utf-8')
        return
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

        def browser_authorized(self):
            origin = self.headers.get('Origin', '')
            return (not origin or origin.startswith('chrome-extension://')) and hmac.compare_digest(
                self.headers.get('Authorization',''), 'Bearer '+browser_token)

        def do_GET(self):
            if not self.authorized():
                return self.respond(403, {'ok': False, 'error': 'Nicht autorisiert.'})
            url = urlsplit(self.path)
            if url.path != '/state':
                return self.respond(404, {'ok': False})
            try:
                selected = parse_qs(url.query).get('source', [''])[0]
                known_cover = parse_qs(url.query).get('cover', [''])[0]
                self.respond(200, asyncio.run_coroutine_threadsafe(media.state(selected, known_cover), loop).result(timeout=8))
            except Exception as error:
                self.respond(503, {'ok': False, 'error': str(error)[:160]})

        def do_POST(self):
            if self.path == '/browser/exchange':
                if not self.browser_authorized():
                    return self.respond(403, {'ok': False, 'error': 'Nicht autorisiert.'})
                try:
                    length = int(self.headers.get('Content-Length', '0'))
                    if not 0 < length <= 8192:
                        raise ValueError('Ungültige Anfrage.')
                    data = json.loads(self.rfile.read(length))
                    if not isinstance(data, dict):
                        raise ValueError('Ungültige Anfrage.')
                    return self.respond(200, media.browser.exchange(data))
                except Exception as error:
                    return self.respond(400, {'ok': False, 'error': str(error)[:160]})
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
                self.respond(200, asyncio.run_coroutine_threadsafe(media.command(data), loop).result(timeout=8))
            except Exception as error:
                self.respond(400, {'ok': False, 'error': str(error)[:160]})

    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    threading.Thread(target=loop.run_forever, daemon=True).start()
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
        loop.call_soon_threadsafe(loop.stop)


if __name__ == '__main__':
    main()
# -- by Larsiopuw
