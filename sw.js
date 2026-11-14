/* el-Mihrâb service worker
   - Uygulama kabuğu: önce ağ, yoksa saklanan kopya
   - Kur'an, meal, tefsir, kıraat servisleri ve yazı tipleri: önce ağ, internet yoksa daha önce okunan kopya */
const V='mihrab-v20', DATA='mihrab-data-v1';
const SHELL=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
const API=['api.alquran.cloud','api.quran.com','api.qurancdn.com','api.quranpedia.net','quranenc.com','api.aladhan.com'];
const FONT=['fonts.googleapis.com','fonts.gstatic.com','api2.quranpedia.net','static.qurancdn.com','verses.quran.foundation'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith('mihrab-v')&&x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
function timeout(p,ms){return Promise.race([p,new Promise((_,r)=>setTimeout(()=>r(new Error('timeout')),ms))])}
self.addEventListener('fetch',e=>{
  const req=e.request;if(req.method!=='GET')return;
  const u=new URL(req.url);
  if((u.origin===location.origin||u.hostname==='el-mihrab.pages.dev')&&u.pathname.includes('/data/')){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok)c.put(req,n.clone());return n}))));return}
  if(u.origin===location.origin){
    e.respondWith(timeout(fetch(req),6000).then(r=>{const c=r.clone();caches.open(V).then(x=>x.put(req,c));return r}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))));return}
  if(FONT.includes(u.hostname)){
    e.respondWith(caches.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok||n.type==='opaque'){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c))}return n})));return}
  if(API.includes(u.hostname)){
    e.respondWith(timeout(fetch(req),9000).then(n=>{if(n.ok){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c))}return n}).catch(err=>caches.match(req).then(r=>{if(r)return r;throw err})));return}
});
