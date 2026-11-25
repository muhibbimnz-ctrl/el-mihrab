/* el-Mihrâb service worker
   - Uygulama kabuğu: önce telefondaki kopya (hemen açılır), arkada yenisi indirilir
   - Kur'an, meal, tefsir, kıraat servisleri: önce ağ (8 sn), olmazsa daha önce okunan kopya, o da yoksa bir kez daha dener */
const V='mihrab-v227', DATA='mihrab-data-v1';
/* Cloudflare Pages "x.html" adresini "x"e yönlendirir. Yönlendirilmiş cevap telefona olduğu gibi saklanırsa
   internetsiz açılışta tarayıcı onu reddeder; bu yüzden temiz bir kopyası saklanır ve iki adres de denenir. */
function temiz(r){return r&&r.redirected?new Response(r.body,{status:r.status,statusText:r.statusText,headers:r.headers}):r}
function esler(url){const u=new URL(url),p=u.pathname,o=u.origin;
  if(p.endsWith('/'))return[o+p+'index.html'];if(p.endsWith('/index.html'))return[o+p.slice(0,-10)];
  if(p.endsWith('.html'))return[o+p.slice(0,-5)];if(!/\.[a-z0-9]+$/i.test(p))return[o+p+'.html'];return[]}
async function sakla(c,key,r){const t=temiz(r);const ks=[key];if(r.redirected&&r.url)ks.push(r.url);
  await Promise.all(ks.map(k=>c.put(k,t.clone()).catch(()=>{})))}
const SHELL=['./','./index.html','./hesap.js?v=2','./hesap-ayar.js?v=1','./medrese.html','./elifba.html','./ihtisas.html','./kadem.html','./cocuk.html','./cocuk-oyun.js','./cocuk-giydir.js?v=1','./data/cocuk/icerik.json?v=2','./medrese.js','./kelime.js','./kalkan.js','./hadis.html','./hadis-arama.js','./fikih.html','./siyer.html','./ahlak.html','./zikir.html','./delail.html','./kible.html','./kaza.html','./ozel.html','./hatim.html','./haber.html','./soru.html','./cami.html','./arac.css?v=1','./arac.js?v=1','./data/delail.json?v=1','./akaid.html','./sozluk.html','./kitaplik.js','./data/zikir.json','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
const API=['api.alquran.cloud','api.quran.com','api.qurancdn.com','api.quranpedia.net','quranenc.com','api.aladhan.com'];
const FONT=['fonts.googleapis.com','fonts.gstatic.com','api2.quranpedia.net','static.qurancdn.com','verses.quran.foundation'];
/* Kurulum: tek bir dosya inmezse bütün kurulum bozulmasın diye dosyalar tek tek saklanır */
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>Promise.all(SHELL.map(x=>fetch(x,{cache:'no-cache'}).then(r=>{if(r.ok)return sakla(c,new URL(x,location).href,r)}).catch(()=>{})))).then(()=>self.skipWaiting()))});
/* Önbellek şişmesin: servis cevapları en çok 1500, yazı tipleri en çok 300 kayıt (en eskiler silinir) */
async function budama(){try{const c=await caches.open(DATA),ks=await c.keys();const api=ks.filter(k=>API.includes(new URL(k.url).hostname));
  if(api.length>1500)await Promise.all(api.slice(0,api.length-1200).map(k=>c.delete(k)));
  const fo=ks.filter(k=>FONT.includes(new URL(k.url).hostname));if(fo.length>300)await Promise.all(fo.slice(0,fo.length-250).map(k=>c.delete(k)))}catch(e){}}
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
  if(u.origin===location.origin&&/\/data\/(hadis|usul|fikih|siyer|ahlak)\//.test(u.pathname)){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>r||fetch(req).then(n=>{if(n.ok){c.put(req,n.clone()).catch(()=>{});c.keys().then(ks=>ks.forEach(k=>{const x=new URL(k.url);if(x.pathname===u.pathname&&x.search!==u.search)c.delete(k)}))}return n}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>{if(r)return r;throw new Error('offline')})))));return}
  /* Sık güncellenen veriler (ihtisas, romanlar, hutbe, vaaz, canlı yayın, haberler): önce ağ (5 sn), olmazsa telefondaki kopya */
  if(u.origin===location.origin&&(/\/data\/(ihtisas|roman|kadem)\//.test(u.pathname)||/\/data\/(hutbe|vaaz|canli|haber)\.json$/.test(u.pathname))){
    e.respondWith(timeout(fetch(req,{cache:'no-cache'}),5000).then(n=>{if(n.ok){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n}).catch(()=>caches.match(req,{ignoreSearch:true}).then(r=>{if(r)return r;throw new Error('offline')})));return}
  if(u.origin===location.origin&&u.pathname.endsWith('/data/videolar.json')){
    e.respondWith(timeout(fetch(req,{cache:'no-cache'}),3500).then(n=>{if(n.ok){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n}).catch(()=>caches.match(req)));return}
  if(u.origin===location.origin&&u.pathname.includes('/data/')){
    e.respondWith(caches.open(DATA).then(c=>c.match(req).then(r=>{const f=fetch(req).then(n=>{if(n.ok)c.put(req,n.clone()).catch(()=>{});return n}).catch(()=>r);return r||f})));return}
  /* Uygulama kabuğu (sayfalar, betikler): telefonda kopyası varsa hemen o açılır, yenisi arkada indirilir (bir sonraki açılışta görünür).
     Kopya yoksa ağ beklenir; yavaş ağda başka sayfa (index.html) verilmez. index.html yedeği yalnız sayfa açılışında ve ağ tamamen yoksa. */
  if(u.origin===location.origin){
    e.respondWith(kabuk(e,req));return}
  if(FONT.includes(u.hostname)){
    e.respondWith(caches.match(req).then(r=>r||timeout(fetch(req),20000).then(n=>{if(n.ok||n.type==='opaque'){const c=n.clone();caches.open(DATA).then(x=>x.put(req,c).catch(()=>{}))}return n})));return}
  /* Dış servisler: 8 sn içinde cevap yoksa ya da sunucu hatası verirse telefondaki kopya; kopya yoksa bir kez daha denenir */
  if(API.includes(u.hostname)){
    e.respondWith(api(req));return}
});
async function kabuk(e,req){
  const c=await caches.open(V),gez=req.mode==='navigate';
  let r=await c.match(req)||(gez?await c.match(req,{ignoreSearch:true}):null);
  if(!r&&gez)for(const k of esler(req.url)){r=await c.match(k,{ignoreSearch:true});if(r)break}
  r=temiz(r);
  const f=timeout(fetch(req,{cache:'no-cache'}),r?30000:45000).then(n=>{if(n.ok)sakla(c,req.url,n.clone());return n});
  if(r){e.waitUntil(f.catch(()=>{}));return r}
  try{return await f}catch(err){
    const y=await caches.match(req,{ignoreSearch:true})||(gez?await c.match(new URL('./index.html',location).href)||await c.match(new URL('./',location).href):null);
    if(y)return temiz(y);throw err}
}
async function api(req){
  const c=await caches.open(DATA),kaydet=n=>{if(n.ok)c.put(req,n.clone()).catch(()=>{});return n};
  const dene=ms=>timeout(fetch(req),ms).then(n=>{if(n.status>=500)throw new Error('sunucu '+n.status);return kaydet(n)});
  try{return await dene(8000)}catch(e){}
  const r=await c.match(req);if(r)return r;
  return dene(12000);
}
