/* Çevrimdışı çalışma. Sürüm değişince eski önbellek silinir. */
const V = 'ing-v5.3';
/* Yazı tipleri Google'dan geliyor. Same-origin şartı bunları önbelleğe almıyordu,
   uçak modunda sayfa sistem fontuna düşüyordu. Bu iki kaynak da önbelleklenir. */
const FONT_HOSTS = /^https:\/\/fonts\.(googleapis|gstatic)\.com$/;
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
  const origin = new URL(e.request.url).origin;
  const isFont = FONT_HOSTS.test(origin);

  // Yazı tipleri değişmez: varsa önbellekten ver, yoksa indir ve sakla.
  if (isFont) {
    e.respondWith(
      caches.match(e.request).then(hit => hit || fetch(e.request).then(r => {
        if (r.ok || r.type === 'opaque') {
          const copy = r.clone();
          e.waitUntil(caches.open(V).then(c => c.put(e.request, copy)));
        }
        return r;
      }).catch(() => new Response('', { status: 504 })))
    );
    return;
  }

  // Ağ önce: açıkken hep güncel sürümü al; ağ yoksa önbellekten ver.
  e.respondWith(
    fetch(e.request)
      .then(r => {
        if (r.ok && origin === location.origin) {
          const copy = r.clone();
          /* waitUntil: SW erken kapanırsa put düşmesin */
          e.waitUntil(caches.open(V).then(c => c.put(e.request, copy)));
        }
        return r;
      })
      .catch(() => caches.match(e.request).then(hit => hit || caches.match('./index.html')))
  );
});
