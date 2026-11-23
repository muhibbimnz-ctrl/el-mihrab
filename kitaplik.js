/* el-Mihrâb · Okuma alanı (PDF kitaplığı + tam ekran okuyucu)
   Kitaplar yalnız bu cihazda (IndexedDB) saklanır; hiçbir yere gönderilmez.
   Kullanım: Kitaplik.goster(kapsayici, {ilim:'tefsir', ad:'Tefsir', defter:function(kayit){...}}) */
(function(){
'use strict';
var DB='mihrab-kitaplik',ST='kitap',PDFJS='vendor/pdfjs/';
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function ac(){return new Promise(function(ok,no){var r=indexedDB.open(DB,1);r.onupgradeneeded=function(){var s=r.result.createObjectStore(ST,{keyPath:'id'});s.createIndex('ilim','ilim')};r.onsuccess=function(){ok(r.result)};r.onerror=function(){no(r.error)}})}
function is(mod,f){return ac().then(function(d){return new Promise(function(ok,no){var t=d.transaction(ST,mod),s=t.objectStore(ST),r=f(s);t.oncomplete=function(){ok(r&&r.result)};t.onerror=t.onabort=function(){no(t.error)}})})}
function hepsi(){return is('readonly',function(s){return s.getAll()})}
function al(id){return is('readonly',function(s){return s.get(id)})}
function koy(k){return is('readwrite',function(s){return s.put(k)})}
function sil(id){return is('readwrite',function(s){return s.delete(id)})}
function boyut(b){return b>1048576?(b/1048576).toFixed(1)+' MB':Math.max(1,Math.round(b/1024))+' KB'}
function tost(t){var x=document.getElementById('toast');if(x){x.textContent=t;x.classList.add('on');clearTimeout(tost.t);tost.t=setTimeout(function(){x.classList.remove('on')},2200)}else alert(t)}
var pdfjsP=null;
function pdfjs(){if(!pdfjsP)pdfjsP=import('./'+PDFJS+'pdf.min.js').then(function(m){m.GlobalWorkerOptions.workerSrc=PDFJS+'pdf.worker.min.js';return m});return pdfjsP}

var CSS='.kt-up{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:4px 0 14px}.kt-up label{background:var(--acc,#3d2a5c);color:#fff;border-radius:14px;padding:11px 16px;font-weight:700;cursor:pointer}.kt-up input{display:none}.kt-up small{color:var(--muted)}'+
'.kt-sw{display:flex;gap:6px;margin:0 0 10px}.kt-sw button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:20px;padding:5px 12px;font:inherit;font-size:14px}.kt-sw button.on{background:var(--acc,#3d2a5c);color:#fff;border-color:transparent}'+
'.kt-l{display:grid;gap:10px}.kt-k{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:10px 12px}.kt-k .kp{width:46px;height:62px;flex:none;border-radius:6px;background:linear-gradient(135deg,#3d2a5c,#7a5aa8);color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;overflow:hidden}.kt-k .kp img{width:100%;height:100%;object-fit:cover}'+
'.kt-k .ki{flex:1;min-width:0;cursor:pointer}.kt-k .ki b{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.kt-k .ki small{color:var(--muted);font-size:13px}.kt-k .bar{height:5px;background:var(--line);border-radius:3px;margin-top:6px;overflow:hidden}.kt-k .bar i{display:block;height:100%;background:#7a5aa8}'+
'.kt-k button{border:0;background:none;color:var(--muted);font-size:20px;padding:6px;cursor:pointer}.kt-bos{color:var(--muted);text-align:center;padding:26px 10px;border:1.5px dashed var(--line);border-radius:16px}'+
'#kt-o{position:fixed;inset:0;z-index:50;background:#3a3a3e;display:flex;flex-direction:column}#kt-o.gece{background:#0d0d10}#kt-o.gece canvas{filter:invert(.92) hue-rotate(180deg)}#kt-o.sepya canvas{filter:sepia(.35) brightness(.97)}'+
'#kt-b{display:flex;align-items:center;gap:4px;padding:calc(6px + env(safe-area-inset-top,0px)) 6px 6px;background:rgba(20,18,26,.94);color:#fff;transition:transform .25s;position:absolute;left:0;right:0;top:0;z-index:2}#kt-b.gz{transform:translateY(-110%)}'+
'#kt-b button{border:0;background:rgba(255,255,255,.1);color:#fff;border-radius:10px;min-width:38px;height:38px;font:600 15px system-ui;cursor:pointer;padding:0 8px}#kt-b b{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:15px;padding:0 4px}'+
'#kt-a{position:absolute;left:0;right:0;bottom:0;z-index:2;display:flex;align-items:center;gap:8px;padding:6px 10px calc(8px + env(safe-area-inset-bottom,0px));background:rgba(20,18,26,.94);color:#fff;transition:transform .25s}#kt-a.gz{transform:translateY(110%)}#kt-a input{flex:1;accent-color:#b99be0}#kt-a span{font:600 14px system-ui;min-width:78px;text-align:center;cursor:pointer}'+
'#kt-s{flex:1;overflow:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;padding:54px 0 64px}#kt-s .sy{margin:0 auto 10px;background:#fff;position:relative;box-shadow:0 2px 10px rgba(0,0,0,.35)}#kt-s .sy canvas{display:block;width:100%;height:100%}#kt-s .sy i{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#999;font:14px system-ui}'+
'#kt-y{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font:16px system-ui;text-align:center;padding:20px}';
function stil(){if(document.getElementById('kt-css'))return;var s=document.createElement('style');s.id='kt-css';s.textContent=CSS;document.head.appendChild(s)}

/* ---------- Kitaplık listesi ---------- */
function goster(ic,o){stil();var tum=false;
 ic.innerHTML='<p class="lead">Kendi kitabını PDF olarak yükle, burada geniş ekranda oku. Kitaplar yalnız bu cihazda saklanır, internete gönderilmez; kaldığın sayfa hatırlanır. Okurken 📒 düğmesiyle okuduğun sayfalar okuma defterine eklenir.</p>'+
 '<div class="kt-up"><label>📄 PDF yükle<input type="file" accept="application/pdf,.pdf" multiple></label><small id="kt-yer"></small></div><div class="kt-sw"><button class="on" data-t="0">'+e(o.ad)+'</button><button data-t="1">Bütün kitaplarım</button></div><div class="kt-l"></div>';
 var L=ic.querySelector('.kt-l'),inp=ic.querySelector('input[type=file]');
 function yer(){if(navigator.storage&&navigator.storage.estimate)navigator.storage.estimate().then(function(s){var y=ic.querySelector('#kt-yer');if(y&&s.quota)y.textContent='Kullanılan: '+boyut(s.usage||0)+' · boş yer: '+boyut(Math.max(0,s.quota-(s.usage||0)))})}
 function ciz(){hepsi().then(function(K){K=K.filter(function(k){return tum||k.ilim===o.ilim}).sort(function(a,b){return(b.son||b.eklendi)-(a.son||a.eklendi)});
  L.innerHTML=K.length?K.map(function(k){var p=k.toplam?Math.round(100*(k.sayfa||1)/k.toplam):0;return'<div class="kt-k" data-id="'+e(k.id)+'"><div class="kp">'+(k.kapak?'<img alt="" src="'+e(k.kapak)+'">':'📖')+'</div><div class="ki"><b>'+e(k.ad)+'</b><small>'+(k.toplam?'Sayfa '+(k.sayfa||1)+' / '+k.toplam+' · ':'')+boyut(k.boyut)+(tum&&k.ilimAd?' · '+e(k.ilimAd):'')+'</small><div class="bar"><i style="width:'+p+'%"></i></div></div><button data-ad aria-label="Adını değiştir">✎</button><button data-sil aria-label="Sil">🗑</button></div>'}).join(''):'<div class="kt-bos">Henüz kitap yok.<br>“PDF yükle” ile ilk kitabını ekle.</div>';
  [].forEach.call(L.querySelectorAll('.kt-k'),function(d){var id=d.dataset.id;
   d.querySelector('.ki').onclick=function(){oku(id,o,ciz)};d.querySelector('.kp').onclick=function(){oku(id,o,ciz)};
   d.querySelector('[data-sil]').onclick=function(){if(confirm('Bu kitap cihazdan silinsin mi?'))sil(id).then(function(){tost('Silindi');ciz();yer()})};
   d.querySelector('[data-ad]').onclick=function(){al(id).then(function(k){var a=prompt('Kitabın adı',k.ad);if(a&&a.trim()){k.ad=a.trim();koy(k).then(ciz)}})}});yer()}).catch(function(){L.innerHTML='<div class="kt-bos">Bu tarayıcıda kitaplık açılamadı (gizli sekme olabilir).</div>'})}
 [].forEach.call(ic.querySelectorAll('.kt-sw button'),function(b){b.onclick=function(){tum=b.dataset.t==='1';[].forEach.call(ic.querySelectorAll('.kt-sw button'),function(x){x.classList.toggle('on',x===b)});ciz()}});
 inp.onchange=function(){var F=[].slice.call(inp.files||[]);inp.value='';if(!F.length)return;
  if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(function(){});
  var sira=Promise.resolve();F.forEach(function(f){sira=sira.then(function(){return ekle(f,o)})});sira.then(function(){ciz()}).catch(function(x){console.error(x);tost('Yüklenemedi: yer yetmiyor olabilir');ciz()})};
 ciz()}

function ekle(f,o){if(!/pdf$/i.test(f.type)&&!/\.pdf$/i.test(f.name)){tost(f.name+' PDF değil');return Promise.resolve()}
 tost('Yükleniyor: '+f.name);
 var k={id:'k'+Date.now().toString(36)+Math.random().toString(36).slice(2,6),ilim:o.ilim,ilimAd:o.ad,ad:f.name.replace(/\.pdf$/i,'').replace(/[_]+/g,' '),boyut:f.size,eklendi:Date.now(),sayfa:1,veri:f};
 /* önce ham dosyayı kaydet, sonra sayfa sayısı ve kapak resmi (olmazsa da kitap kalır) */
 return koy(k).then(function(){return pdfjs().then(function(P){return f.arrayBuffer().then(function(b){return P.getDocument(ayar(P,b)).promise}).then(function(d){k.toplam=d.numPages;return d.getMetadata().catch(function(){return{}}).then(function(m){var t=m&&m.info&&m.info.Title;if(t&&t.trim().length>2&&!/^(untitled|microsoft|document)/i.test(t))k.ad=t.trim();return d.getPage(1)}).then(function(p){var v=p.getViewport({scale:1}),s=120/v.width,vv=p.getViewport({scale:s}),c=document.createElement('canvas');c.width=vv.width;c.height=vv.height;return p.render({canvasContext:c.getContext('2d'),viewport:vv}).promise.then(function(){k.kapak=c.toDataURL('image/jpeg',.7);yoket(d)})})})}).catch(function(x){console.warn('kapak/sayfa',x)}).then(function(){return koy(k)}).then(function(){tost('Eklendi: '+k.ad)})})}
function yoket(d){try{if(!d)return;if(d.destroy)d.destroy();else if(d.loadingTask)d.loadingTask.destroy()}catch(x){}}
function ayar(P,b){return{data:b,cMapUrl:PDFJS+'cmaps/',cMapPacked:true,standardFontDataUrl:PDFJS+'standard_fonts/',wasmUrl:PDFJS+'wasm/',iccUrl:PDFJS+'iccs/',isEvalSupported:false}}

/* ---------- Okuyucu ---------- */
var AY='ihtisas.okuyucu.v1';
function ayarA(){try{return JSON.parse(localStorage.getItem(AY))||{}}catch(x){return{}}}
function ayarY(a){try{localStorage.setItem(AY,JSON.stringify(a))}catch(x){}}
function oku(id,o,kapaninca){stil();var A=ayarA(),zoom=A.zoom||1,renk=A.renk||'';
 var ov=document.createElement('div');ov.id='kt-o';if(renk)ov.className=renk;
 ov.innerHTML='<div id="kt-b"><button data-k title="Kapat">✕</button><b>…</b><button data-z="-" title="Küçült">A−</button><button data-z="+" title="Büyüt">A+</button><button data-r title="Gece / sepya">◐</button><button data-f title="Tam ekran">⛶</button><button data-d title="Okuma defterine ekle">📒</button></div><div id="kt-s"></div><div id="kt-a"><input type="range" min="1" value="1"><span>1 / 1</span></div><div id="kt-y">Kitap açılıyor…</div>';
 document.body.appendChild(ov);var eskiOv=document.body.style.overflow;document.body.style.overflow='hidden';
 var S=ov.querySelector('#kt-s'),bar=ov.querySelector('#kt-b'),alt=ov.querySelector('#kt-a'),rng=alt.querySelector('input'),gs=alt.querySelector('span'),Y=ov.querySelector('#kt-y');
 var K,doc,n=0,oran=[],ciz={},su=1,bas=1,enCok=1,io,kayT,bitti=false;
 history.pushState({kt:1},'');
 function kapat(geri){if(bitti)return;bitti=true;var kp=kaydet();if(io)io.disconnect();yoket(doc);if(document.fullscreenElement&&document.exitFullscreen)document.exitFullscreen().catch(function(){});ov.remove();document.body.style.overflow=eskiOv;removeEventListener('popstate',pop);removeEventListener('resize',rs);if(!geri&&history.state&&history.state.kt)history.back();kp.then(function(){if(kapaninca)kapaninca()})}
 function pop(){kapat(true)}addEventListener('popstate',pop);
 function kaydet(){if(!K)return Promise.resolve();K.sayfa=su;K.son=Date.now();return koy(K).catch(function(){})}
 function gizle(g){bar.classList.toggle('gz',g);alt.classList.toggle('gz',g)}
 var dokT=0;S.addEventListener('click',function(ev){if(Date.now()-dokT<350)return;dokT=Date.now();gizle(!bar.classList.contains('gz'))});
 ov.querySelector('[data-k]').onclick=function(){kapat()};
 ov.querySelector('[data-r]').onclick=function(){renk=renk===''?'gece':renk==='gece'?'sepya':'';ov.className=renk;A.renk=renk;ayarY(A);tost(renk==='gece'?'Gece modu':renk==='sepya'?'Sepya':'Normal')};
 ov.querySelector('[data-f]').onclick=function(){if(document.fullscreenElement)document.exitFullscreen();else if(ov.requestFullscreen)ov.requestFullscreen().catch(function(){tost('Tam ekran desteklenmiyor')})};
 [].forEach.call(ov.querySelectorAll('[data-z]'),function(b){b.onclick=function(){var z=b.dataset.z==='+'?Math.min(3,zoom+.2):Math.max(.5,zoom-.2);if(z!==zoom){zoom=+z.toFixed(2);A.zoom=zoom;ayarY(A);boyutla(su)}}});
 ov.querySelector('[data-d]').onclick=function(){if(!o.defter){tost('Okuma defteri yok');return}var s=Math.max(1,enCok-bas+1),r=prompt('Okuma defterine eklensin:\n“'+K.ad+'” · sayfa '+bas+'–'+enCok+'\nKaç sayfa okudun?',s);if(r===null)return;var x=parseInt(r,10);if(!x){tost('Sayı yaz');return}o.defter({k:K.ad,s:x,n:'s. '+bas+'–'+enCok});tost('Deftere eklendi: '+x+' sayfa');bas=su;enCok=su};
 gs.onclick=function(){var r=prompt('Kaçıncı sayfaya gidilsin? (1–'+n+')',su);var x=parseInt(r,10);if(x>=1&&x<=n)git(x)};
 rng.oninput=function(){gs.textContent=rng.value+' / '+n};rng.onchange=function(){git(+rng.value)};
 function gen(){return Math.min(S.clientWidth-16,1400)*zoom}
 function boyutla(hedef){var w=gen(),pd=S.children;for(var i=0;i<n;i++){var d=pd[i];d.style.width=w+'px';d.style.height=Math.round(w*oran[i])+'px';if(ciz[i+1]){ciz[i+1].cancel&&ciz[i+1].cancel();delete ciz[i+1];var c=d.querySelector('canvas');if(c)c.remove()}}git(hedef,true);setTimeout(function(){for(var q=Math.max(1,su-1);q<=Math.min(n,su+3);q++)sayfaCiz(q)},60)}
 function git(p,sessiz){var d=S.children[p-1];if(d)S.scrollTop=d.offsetTop-54;su=p;guncel()}
 function guncel(){rng.value=su;gs.textContent=su+' / '+n;if(su>enCok)enCok=su;clearTimeout(kayT);kayT=setTimeout(kaydet,800)}
 function rs(){clearTimeout(rs.t);rs.t=setTimeout(function(){boyutla(su)},250)}addEventListener('resize',rs);
 function sayfaCiz(p){if(ciz[p]||!doc)return;var d=S.children[p-1];if(!d)return;var tok={iptal:false,cancel:function(){this.iptal=true;if(this.g)this.g.cancel()}};ciz[p]=tok;
  doc.getPage(p).then(function(pg){if(tok.iptal)return;var w=d.clientWidth,v1=pg.getViewport({scale:1}),dpr=Math.min(window.devicePixelRatio||1,2),sc=w/v1.width*dpr,v=pg.getViewport({scale:sc});
   if(Math.abs(v1.height/v1.width-oran[p-1])>.01){oran[p-1]=v1.height/v1.width;d.style.height=Math.round(w*oran[p-1])+'px'}
   var c=document.createElement('canvas');c.width=Math.floor(v.width);c.height=Math.floor(v.height);tok.g=pg.render({canvasContext:c.getContext('2d'),viewport:v});
   return tok.g.promise.then(function(){if(tok.iptal)return;var i=d.querySelector('i');if(i)i.remove();var e2=d.querySelector('canvas');if(e2)e2.remove();d.appendChild(c)})}).catch(function(x){if(x&&x.name!=='RenderingCancelledException')console.warn(x)})}
 function birak(p){var t=ciz[p];if(!t)return;t.cancel();delete ciz[p];var d=S.children[p-1];if(d){var c=d.querySelector('canvas');if(c)c.remove()}}
 S.addEventListener('scroll',function(){var m=S.scrollTop+S.clientHeight/3,pd=S.children,lo=0,hi=n-1;while(lo<hi){var md=(lo+hi+1)>>1;if(pd[md].offsetTop<=m)lo=md;else hi=md-1}var p=lo+1;if(p!==su){su=p;guncel()}
  for(var q in ciz)if(Math.abs(q-su)>6)birak(+q)},{passive:true});
 al(id).then(function(k){if(!k)throw new Error('yok');K=k;bar.querySelector('b').textContent=k.ad;var veri=k.veri;return(veri.arrayBuffer?veri.arrayBuffer():new Response(veri).arrayBuffer())}).then(function(b){return pdfjs().then(function(P){return P.getDocument(ayar(P,b)).promise})}).then(function(d){if(bitti){yoket(d);return}doc=d;n=d.numPages;rng.max=n;
  return d.getPage(1).then(function(p){var v=p.getViewport({scale:1}),r=v.height/v.width;for(var i=0;i<n;i++)oran.push(r);
   var w=gen(),h='';for(i=1;i<=n;i++)h+='<div class="sy" data-p="'+i+'" style="width:'+w+'px;height:'+Math.round(w*r)+'px"><i>'+i+'</i></div>';S.innerHTML=h;Y.remove();
   if(!K.toplam||K.toplam!==n){K.toplam=n}
   io=new IntersectionObserver(function(G){G.forEach(function(g){if(g.isIntersecting)sayfaCiz(+g.target.dataset.p)})},{root:S,rootMargin:'150% 0px'});[].forEach.call(S.children,function(x){io.observe(x)});
   var bp=Math.min(Math.max(1,K.sayfa||1),n);bas=bp;enCok=bp;git(bp);if(bp>1)tost('Kaldığın yer: sayfa '+bp);setTimeout(function(){gizle(true)},2500)})}).catch(function(x){console.error(x);Y.innerHTML='Bu PDF açılamadı.<br><small>'+e(x&&x.message||'')+'</small><br><br><button onclick="this.closest(\'#kt-o\').querySelector(\'[data-k]\').click()">Geri</button>'})}

window.Kitaplik={goster:goster,oku:oku};
})();
