// Bộ nhớ đệm: giao diện lấy mạng trước (để cập nhật nhanh), dữ liệu & giọng mẫu lấy bộ nhớ trước (dùng được khi mất mạng)
const C='luyennoi-v2';
self.addEventListener('install',e=>{ e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','app.js','pitch.js','lib/speech-sdk.min.js','data/hsk.json','data/dlg.json','manifest.json','icon.svg']))); self.skipWaiting(); });
self.addEventListener('activate',e=>{ e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch',e=>{ const u=new URL(e.request.url); if(e.request.method!=='GET'||u.origin!==location.origin) return;
  const heavy=/\/(audio|data|lib)\//.test(u.pathname);
  e.respondWith(heavy? caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{ if(res.ok){ const cl=res.clone(); caches.open(C).then(c=>c.put(e.request,cl)); } return res; }))
    : fetch(e.request).then(res=>{ if(res.ok){ const cl=res.clone(); caches.open(C).then(c=>c.put(e.request,cl)); } return res; }).catch(()=>caches.match(e.request))); });
