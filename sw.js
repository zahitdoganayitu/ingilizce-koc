/* Çevrimdışı çalışma. Sürüm değişince eski önbellek silinir. */
const V = 'ing-v4.2';
const FILES = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png', './apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== V).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  // Ağ önce: açıkken hep güncel sürümü al; ağ yoksa önbellekten ver.
  e.respondWith(
    fetch(e.request)
      .then(r => {
        if (r.ok && new URL(e.request.url).origin === location.origin) {
          const copy = r.clone();
          caches.open(V).then(c => c.put(e.request, copy));
        }
        return r;
      })
      .catch(() => caches.match(e.request).then(hit => hit || caches.match('./index.html')))
  );
});
