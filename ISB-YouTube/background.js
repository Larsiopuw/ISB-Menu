importScripts('connection.js');
chrome.runtime.onMessage.addListener((message, sender, reply) => {
  if (message.type !== 'isb-media' || !sender.tab || !/^https:\/\/(www\.|m\.)?youtube\.com\//.test(sender.url || '')) return;
  if (!ISB_CONNECTION.token) { reply({commands: []}); return; }
  fetch('http://127.0.0.1:8766/browser/exchange', {
    method: 'POST', headers: {'Content-Type': 'application/json', Authorization: 'Bearer ' + ISB_CONNECTION.token},
    body: JSON.stringify({tab: sender.tab.id, state: message.state, acknowledgements: message.acknowledgements || []}),
    signal: AbortSignal.timeout(3000)
  }).then(response => response.ok ? response.json() : {commands: []})
    .then(reply).catch(() => reply({commands: []}));
  return true;
});
// -- by Larsiopuw
