const CACHE = 'ilmiopiano-v68';
const FILES = ["./", "manifest.webmanifest", "icons/muscolo5-180.png", "icons/muscolo5-192.png", "icons/muscolo5-512.png", "promemoria-spesa.ics"];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {cache: 'reload'})))).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin || url.pathname.includes('/api/')) return;
  const fresh = req.mode === 'navigate' || /\.(html|webmanifest|png)$/.test(url.pathname) || url.pathname.endsWith('/');
  e.respondWith(caches.open(CACHE).then(async c => {
    if (fresh) {
      // pagina, manifest e icone: prima la rete, così aggiornamenti e icona nuova arrivano subito
      const key = req.mode === 'navigate' ? './' : req;
      try { const r = await fetch(req, {cache: 'no-cache'}); if (r && r.ok) { c.put(key, r.clone()); return r; } } catch (err) {}
      return (await c.match(key, {ignoreSearch: true})) || Response.error();
    }
    const hit = await c.match(req, {ignoreSearch: true});
    const net = fetch(req).then(r => { if (r && r.ok) c.put(req, r.clone()); return r; }).catch(() => null);
    if (hit) { e.waitUntil(net); return hit; }
    return (await net) || Response.error();
  }));
});

// notifiche di fine recupero mandate dal Worker (vedi worker/index.js)
self.addEventListener('push', e => {
  let d = {}; try { d = e.data ? e.data.json() : {}; } catch (err) { d = {body: e.data ? e.data.text() : ''}; }
  e.waitUntil(self.registration.showNotification(d.title || 'Di&T', {body: d.body || '', tag: d.tag || 'recupero', renotify: true, icon: 'icons/muscolo5-192.png', badge: 'icons/muscolo5-192.png', data: {id: d.id || '', at: d.at || Date.now()}}));
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(self.clients.matchAll({type: 'window', includeUncontrolled: true}).then(list => {
    const c = list.find(x => 'focus' in x);
    if (c) { c.postMessage({t: 'push-open'}); return c.focus(); }
    return self.clients.openWindow('./');
  }));
});
