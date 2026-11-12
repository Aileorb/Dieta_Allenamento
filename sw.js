const CACHE = 'ilmiopiano-v61';
const FILES = ["index.html", "manifest.webmanifest", "icons/muscolo5-180.png", "icons/muscolo5-192.png", "icons/muscolo5-512.png", "promemoria-spesa.ics"];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {cache: 'reload'})))).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;
  const fresh = req.mode === 'navigate' || /\.(html|webmanifest|png)$/.test(url.pathname) || url.pathname.endsWith('/');
  e.respondWith(caches.open(CACHE).then(async c => {
    if (fresh) {
      // pagina, manifest e icone: prima la rete, così aggiornamenti e icona nuova arrivano subito
      const key = req.mode === 'navigate' ? 'index.html' : req;
      try { const r = await fetch(req, {cache: 'no-cache'}); if (r && r.ok) { c.put(key, r.clone()); return r; } } catch (err) {}
      return (await c.match(key, {ignoreSearch: true})) || Response.error();
    }
    const hit = await c.match(req, {ignoreSearch: true});
    const net = fetch(req).then(r => { if (r && r.ok) c.put(req, r.clone()); return r; }).catch(() => null);
    if (hit) { e.waitUntil(net); return hit; }
    return (await net) || Response.error();
  }));
});
