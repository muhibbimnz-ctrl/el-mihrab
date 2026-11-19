/* el-Mihrâb service worker
   - Uygulama kabuğu: önce ağ, yoksa saklanan kopya
   - Kur'an, meal, tefsir, kıraat servisleri ve yazı tipleri: önce ağ, internet yoksa daha önce okunan kopya */
const V='mihrab-v92', DATA='mihrab-data-v1';
const SHELL=['./','./index.html','./medrese.html','./elifba.html','./medrese.js','./kelime.js','./kalkan.js','./hadis.html','./hadis-arama.js','./fikih.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
const API=['api.alquran.cloud','api.quran.com','api.qurancdn.com','api.quranpedia.net','quranenc.com','api.aladhan.com'];
const FONT=['fonts.googleapis.com','fonts.gstatic.com','api2.quranpedia.net','static.qurancdn.com','verses.quran.foundation'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(SHELL)).then(()=>self.skipWaiting()))});
async function budama(){try{const c=await caches.open(DATA),ks=await c.keys();const api=ks.filter(k=>API.includes(new URL(k.url).hostname));
  if(api.length>1500)await Promise.all(api.slice(0,api.length-1200).map(k=>c.delete(k)))}catch(e){}}
self.addEventListener('activate',e=>{budama();e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x.startsWith('mihrab-v')&&x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
function timeout(p,ms){return Promise.race([p,new Promise((_,r)=>setTimeout(()=>r(new Error('timeout')),ms))])}
self.addEventListener('fetch',e=>{
  const req=e.request;if(req.method!=='GET')return;
  const u=new URL(req.url);
  if((u.origin===location.origin||u.hostname==='el-mihrab.pages.dev')&&u.pathname.includes('/data/q/')){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok)c.put(req,n.clone()).catch(()=>{});return n}))));return}
  /* Medrese verisi (kitaplar, YDS, kelime çözümlemesi): önce saklanan kopya, arkada güncelle */
  /* Dil sayfalarının ders verisi (veri/*.js?v=özet): adres özetle değiştiği için önce telefondaki kopya; yenisi gelince eskisi silinir */
  if(u.origin===location.origin&&u.pathname.includes('/veri/')&&u.pathname.endsWith('.js')){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok){c.put(req,n.clone()).catch(()=>{});c.keys().then(ks=>ks.forEach(k=>{const x=new URL(k.url);if(x.pathname===u.pathname&&x.search!==u.search)c.delete(k)}))}return n}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>{if(r)return r;throw new Error('offline')})))));return}
  /* Hadis ve usûl verisi (büyük, nadiren değişen dosyalar): önce telefondaki kopya, arkada tekrar indirme yok; ?v= değişince yenisi alınır */
  if(u.origin===location.origin&&/\/data\/(hadis|usul|fikih)\//.test(u.pathname)){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok){c.put(req,n.clone()).catch(()=>{});c.keys().then(ks=>ks.forEach(k=>{const x=new URL(k.url);if(x.pathname===u.pathname&&x.search!==u.search)c.delete(k)}))}return n}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>{if(r)return r;throw new Error('offline')})))));return}
  if(u.origin===location.origin&&u.pathname.endsWith('/data/videolar.json')){
    e.respondWith(timeout(fetch(req,{cache:'no-cache'}),3500).then(n=>{if(n.ok){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n}).catch(()=>caches.match(req)));return}
  if(u.origin===location.origin&&u.pathname.includes('/data/')){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>{const f=fetch(req).then(n=>{if(n.ok)c.put(req,n.clone()).catch(()=>{});return n}).catch(()=>r);return r||f})));return}
  if(u.origin===location.origin){
    e.respondWith(timeout(fetch(req,{cache:'no-cache'}),3500).then(r=>{const c=r.clone();caches.open(V).then(x=>x.put(req,c).catch(()=>{}));return r}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>r||caches.match('./index.html'))));return}
  if(FONT.includes(u.hostname)){
    e.respondWith(caches.match(req).then(r=>r||timeout(fetch(req),5000).then(n=>{if(n.ok||n.type==='opaque'){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n})));return}
  if(API.includes(u.hostname)){
    e.respondWith(timeout(fetch(req),9000).then(n=>{if(n.ok){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n}).catch(err=>caches.match(req).then(r=>{if(r)return r;throw err})));return}
});
