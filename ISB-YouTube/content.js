/* YouTube-only media adapter; no account data or browsing history is collected. */
(() => {
  let acknowledgements = [];
  let running = false;
  const audibleVolumes = new WeakMap();
  const finite = value => Number.isFinite(value) ? value : 0;
  function snapshot(video) {
    if (video.volume > 0) audibleVolumes.set(video, video.volume);
    const liveBadge = document.querySelector('.ytp-live-badge');
    const live = video.duration === Infinity || Boolean(liveBadge && liveBadge.getClientRects().length);
    const range = video.seekable;
    const seekMin = range.length ? range.start(range.length - 1) : 0;
    const seekMax = range.length ? range.end(range.length - 1) : 0;
    const startMeta = document.querySelector('meta[itemprop="startDate"]');
    const parsedStart = startMeta ? Date.parse(startMeta.content) / 1000 : 0;
    return {
      title: document.querySelector('h1.ytd-watch-metadata')?.textContent?.trim() || document.title.replace(/ - YouTube$/, ''),
      artist: document.querySelector('#owner #channel-name')?.textContent?.trim() || 'YouTube',
      playing: !video.paused && !video.ended,
      position: finite(video.currentTime), duration: live ? 0 : finite(video.duration),
      seekMin: finite(seekMin), seekMax: finite(seekMax),
      live, liveStartedAt: Number.isFinite(parsedStart) && parsedStart > 0 && parsedStart < Date.now()/1000 ? parsedStart : 0,
      muted: video.muted || video.volume === 0, volume: video.volume,
      controls: {toggle: true, seek: seekMax > seekMin, volume: true, mute: true, next: false, previous: false}
    };
  }
  async function execute(video, item) {
    switch (item.command) {
      case 'toggle': if (video.paused) await video.play(); else video.pause(); break;
      case 'mute':
        video.muted = Boolean(item.value);
        if (!video.muted && video.volume === 0) video.volume = audibleVolumes.get(video) || .5;
        break;
      case 'volume': video.volume = Math.max(0, Math.min(1, item.value)); if (item.value > 0) video.muted = false; break;
      case 'seek': {
        const ranges = video.seekable;
        if (!ranges.length) throw new Error('Dieser Stream bietet aktuell kein Rückspulfenster.');
        const first = ranges.start(ranges.length-1), last = ranges.end(ranges.length-1);
        video.currentTime = Math.max(first, Math.min(last - .05, item.value)); break;
      }
      default: throw new Error('Aktion nicht verfügbar.');
    }
  }
  async function tick() {
    if (running) return;
    running = true;
    try {
      const video = document.querySelector('video.html5-main-video');
      const result = await chrome.runtime.sendMessage({type: 'isb-media', state: video ? snapshot(video) : null, acknowledgements});
      acknowledgements = [];
      for (const item of result?.commands || []) {
        try {
          if (!video) throw new Error('YouTube-Player nicht mehr verfügbar.');
          await execute(video, item);
          acknowledgements.push({id: item.id, ok: true});
        } catch (error) { acknowledgements.push({id: item.id, ok: false, error: String(error.message).slice(0,160)}); }
      }
    } catch (_) { /* Bridge reconnects on the next tick. */ }
    finally { running = false; }
  }
  setInterval(tick, 300);
  tick();
})();
// -- by Larsiopuw
