/* el-Mihrâb · Okuma alanı (PDF kitaplığı + okuyucu: kalem, fosforlu, altını çizme, not, yer imi, içindekiler, arama)
   Kitaplar ve notlar yalnız bu cihazda (IndexedDB) saklanır; hiçbir yere gönderilmez.
   Kullanım: Kitaplik.goster(kapsayici, {ilim:'tefsir', ad:'Tefsir', defter:function(kayit){...}}) */
(function(){
'use strict';
var DB='mihrab-kitaplik',ST='kitap',NT='not',PDFJS='vendor/pdfjs/',SVGNS='http://www.w3.org/2000/svg';
function e(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function ac(){return new Promise(function(ok,no){var r=indexedDB.open(DB,2);r.onupgradeneeded=function(){var d=r.result;if(!d.objectStoreNames.contains(ST)){var s=d.createObjectStore(ST,{keyPath:'id'});s.createIndex('ilim','ilim')}if(!d.objectStoreNames.contains(NT))d.createObjectStore(NT,{keyPath:'id'})};r.onsuccess=function(){ok(r.result)};r.onerror=function(){no(r.error)};r.onblocked=function(){no(new Error('Kitaplık başka sekmede açık; o sekmeyi kapatıp tekrar dene'))}})}
var dbP=null;function db(){if(!dbP)dbP=ac().catch(function(x){dbP=null;throw x});return dbP}
function is(st,mod,f){return db().then(function(d){return new Promise(function(ok,no){var t=d.transaction(st,mod),r=f(t.objectStore(st));t.oncomplete=function(){ok(r&&r.result)};t.onerror=t.onabort=function(){no(t.error||new Error('Kayıt hatası'))}})})}
function hepsi(){return is(ST,'readonly',function(s){return s.getAll()})}
function al(id){return is(ST,'readonly',function(s){return s.get(id)})}
function koy(k){return is(ST,'readwrite',function(s){return s.put(k)})}
function sil(id){return is(ST,'readwrite',function(s){return s.delete(id)}).then(function(){return is(NT,'readwrite',function(s){return s.delete(id)})})}
function notAl(id){return is(NT,'readonly',function(s){return s.get(id)}).then(function(n){n=n||{id:id};n.s=n.s||{};n.n=n.n||{};n.y=n.y||[];return n})}
function notKoy(n){return is(NT,'readwrite',function(s){return s.put(n)})}
function boyut(b){return b>1048576?(b/1048576).toFixed(1)+' MB':Math.max(1,Math.round(b/1024))+' KB'}
function tost(t){var x=document.getElementById('toast');if(!x){x=document.createElement('div');x.id='toast';document.body.appendChild(x)}x.textContent=t;x.classList.add('on');x.style.zIndex=99;clearTimeout(tost.t);tost.t=setTimeout(function(){x.classList.remove('on')},2400)}
var pdfjsP=null;
function pdfjs(){if(!pdfjsP)pdfjsP=import('./'+PDFJS+'pdf.min.js').then(function(m){m.GlobalWorkerOptions.workerSrc=new URL(PDFJS+'pdf.worker.min.js',location.href).href;return m}).catch(function(x){pdfjsP=null;throw new Error('PDF okuyucu yüklenemedi (internet bağlantısını kontrol edip bir kez daha dene)')});return pdfjsP}
function ayar(){var K=new URL(PDFJS,location.href).href;return{cMapUrl:K+'cmaps/',cMapPacked:true,standardFontDataUrl:K+'standard_fonts/',wasmUrl:K+'wasm/',iccUrl:K+'iccs/',useWasm:true,isEvalSupported:false,stopAtErrors:false}}
function veriBlob(k){return k.blob||k.veri}
/* PDF açıcı: dosyayı parça parça okur (büyük kitaplar belleği doldurmaz); olmazsa tümünü okur. Şifreli PDF'te şifre sorar. */
function belgeAc(P,blob,sifreSor){
 function kur(o){var lt=P.getDocument(o),iptal=false;lt.onPassword=function(cb,neden){sifreSor(neden===P.PasswordResponses.INCORRECT_PASSWORD).then(function(s){if(s==null){iptal=true;lt.destroy()}else cb(s)})};return lt.promise.catch(function(x){if(iptal){var y=new Error('Şifre girilmedi');y.iptal=1;throw y}throw x})}
 var ilk=Math.min(blob.size,262144);
 return blob.slice(0,ilk).arrayBuffer().then(function(b0){
  if(ilk>=blob.size){var o=ayar();o.data=new Uint8Array(b0);return kur(o)}
  var tr=new P.PDFDataRangeTransport(blob.size,new Uint8Array(b0));
  tr.requestDataRange=function(a,z){blob.slice(a,z).arrayBuffer().then(function(b){tr.onDataRange(a,new Uint8Array(b))}).catch(function(x){console.warn('parça okunamadı',x)})};
  var o=ayar();o.range=tr;o.rangeChunkSize=262144;o.disableAutoFetch=true;o.disableStream=true;return kur(o)
 }).catch(function(x){if(x&&(x.iptal||x.name==='PasswordException'))throw x;console.warn('parçalı açılamadı, tümü deneniyor',x);
  return blob.arrayBuffer().then(function(b){var o=ayar();o.data=new Uint8Array(b);return kur(o)})})}
function yoket(d){try{if(!d)return;if(d.destroy)d.destroy();else if(d.loadingTask)d.loadingTask.destroy()}catch(x){}}
function hataMetni(x){var m=(x&&(x.message||x.name))||'';if(/Invalid PDF|InvalidPDF/i.test(m))return'Dosya bozuk ya da tam inmemiş görünüyor.';if(/Password|Şifre/i.test(m))return'Şifre girilmedi.';if(/Missing PDF|MissingPDF/i.test(m))return'Dosya boş görünüyor.';if(/memory|Array buffer allocation/i.test(m))return'Telefonun belleği yetmedi; uygulamayı kapatıp yeniden açmayı dene.';return m||'Bilinmeyen hata'}

var CSS=
'.kt-up{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:4px 0 14px}.kt-up label{background:var(--acc,#3d2a5c);color:#fff;border-radius:14px;padding:11px 16px;font-weight:700;cursor:pointer}.kt-up input{display:none}.kt-up small{color:var(--muted)}'+
'.kt-sw{display:flex;gap:6px;margin:0 0 10px}.kt-sw button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:20px;padding:5px 12px;font:inherit;font-size:14px}.kt-sw button.on{background:var(--acc,#3d2a5c);color:#fff;border-color:transparent}'+
'.kt-l{display:grid;gap:10px}@media(min-width:700px){.kt-l{grid-template-columns:1fr 1fr}}.kt-k{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:10px 12px}.kt-k .kp{width:48px;height:66px;flex:none;border-radius:4px 7px 7px 4px;background:linear-gradient(135deg,#5b3d2a,#8a6243);color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;overflow:hidden;box-shadow:2px 2px 6px rgba(0,0,0,.25);cursor:pointer}.kt-k .kp img{width:100%;height:100%;object-fit:cover}'+
'.kt-yd button,.kt-up label.ikinci{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:14px;padding:9px 14px;font:inherit;font-weight:600;cursor:pointer}.kt-yd{margin-top:-6px}'+
'.kt-k .ki{flex:1;min-width:0;cursor:pointer}.kt-k .ki b{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.kt-k .ki small{color:var(--muted);font-size:13px;display:block}.kt-k .bar{height:5px;background:var(--line);border-radius:3px;margin-top:6px;overflow:hidden}.kt-k .bar i{display:block;height:100%;background:#a0703f}'+
'.kt-k button{border:0;background:none;color:var(--muted);font-size:19px;padding:6px;cursor:pointer}.kt-bos{color:var(--muted);text-align:center;padding:26px 10px;border:1.5px dashed var(--line);border-radius:16px}'+
'#kt-o{position:fixed;inset:0;z-index:50;background:#2e2925;display:flex;flex-direction:column;font:15px/1.4 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#f3ece2;-webkit-tap-highlight-color:transparent}'+
'#kt-o button{font:inherit;color:inherit;cursor:pointer}'+
'#kt-b,#kt-a{position:absolute;left:0;right:0;z-index:3;background:rgba(28,24,21,.95);backdrop-filter:blur(6px);transition:transform .25s}'+
'#kt-b{top:0;display:flex;align-items:center;gap:3px;padding:calc(6px + env(safe-area-inset-top,0px)) 6px 6px}#kt-b.gz{transform:translateY(-110%)}'+
'#kt-b button{border:0;background:transparent;border-radius:10px;min-width:38px;height:38px;font-size:18px;padding:0 6px}#kt-b button:active,#kt-b button.on{background:rgba(255,255,255,.14)}#kt-b b{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:15px;font-weight:600;padding:0 4px}'+
'#kt-a{bottom:0;padding:6px 10px calc(8px + env(safe-area-inset-bottom,0px))}#kt-a.gz{transform:translateY(110%)}'+
'.kt-ar{display:none;gap:4px;align-items:center;overflow-x:auto;padding:2px 0 8px;scrollbar-width:none}.kt-ar.ac{display:flex}.kt-ar button{flex:none;border:0;background:rgba(255,255,255,.08);border-radius:12px;min-width:44px;height:42px;font-size:19px;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1}.kt-ar button small{font-size:9.5px;opacity:.8;margin-top:2px}.kt-ar button.on{background:#f3ece2;color:#2a221c}.kt-ar .ay{width:1px;height:28px;background:rgba(255,255,255,.2);margin:0 4px;flex:none}'+
'.kt-ar .rk{min-width:30px;width:30px;height:30px;border-radius:50%;border:2px solid transparent}.kt-ar .rk.on{border-color:#fff;box-shadow:0 0 0 2px #2a221c inset}'+
'.kt-sl{display:flex;align-items:center;gap:10px}.kt-sl input{flex:1;accent-color:#d9b27c}.kt-sl span{font:600 14px system-ui;min-width:84px;text-align:center;cursor:pointer;background:rgba(255,255,255,.08);border-radius:10px;padding:6px 4px}'+
'#kt-s{flex:1;overflow:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;touch-action:pan-x pan-y}#kt-s.ciz{touch-action:none}'+
'#kt-in{padding:58px 8px 78px;transform-origin:0 0;margin:0 auto}'+
'#kt-o.sayfali #kt-s{scroll-snap-type:x mandatory;overflow:auto}#kt-o.sayfali #kt-in{display:flex;align-items:flex-start;padding:0;margin:0;width:max-content;min-height:100%}#kt-o.sayfali #kt-in .sy{flex:none;scroll-snap-align:center;scroll-snap-stop:always}'+
'#kt-in .sy{margin:0 auto 12px;position:relative;background:var(--kg,#f6eedc);box-shadow:0 1px 3px rgba(0,0,0,.4),0 6px 18px rgba(0,0,0,.25);border-radius:2px}'+
'#kt-in .sy canvas{display:block;position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:multiply}'+
'#kt-in .sy svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;overflow:visible}#kt-in .sy svg .nt{pointer-events:auto;cursor:pointer}'+
'#kt-in .sy .pn{position:absolute;left:0;right:0;top:50%;text-align:center;color:rgba(80,60,40,.35);font:600 15px system-ui}'+
'#kt-in .sy .yi{position:absolute;top:-4px;right:18px;width:18px;height:30px;background:#b3322b;clip-path:polygon(0 0,100% 0,100% 100%,50% 75%,0 100%);display:none}#kt-in .sy.yer .yi{display:block}'+
'#kt-o.kagit{--kg:#f6eedc}#kt-o.sepya{--kg:#e9d6b0}#kt-o.beyaz{--kg:#fff}#kt-o.beyaz #kt-in .sy canvas{mix-blend-mode:normal}'+
'#kt-o.gece{background:#121110;--kg:#1d1b18}#kt-o.gece #kt-in .sy canvas{mix-blend-mode:normal;filter:invert(.88) hue-rotate(180deg) sepia(.15)}#kt-o.gece #kt-in .sy svg .fs{mix-blend-mode:screen}'+
'#kt-in .sy svg .fs{mix-blend-mode:multiply}'+
'#kt-y{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;text-align:center;padding:24px;z-index:2}#kt-y button,.kt-btn{border:0;background:#d9b27c;color:#2a221c;border-radius:12px;padding:10px 16px;font-weight:700}'+
'.kt-sh{position:absolute;inset:0;z-index:6;background:rgba(0,0,0,.45);display:flex;align-items:flex-end;justify-content:center}.kt-shi{background:#f8f2e7;color:#2a221c;width:100%;max-width:640px;max-height:82vh;overflow:auto;border-radius:20px 20px 0 0;padding:14px 16px calc(16px + env(safe-area-inset-bottom,0px));box-shadow:0 -8px 30px rgba(0,0,0,.3)}'+
'.kt-shi h3{margin:2px 0 10px;font-size:17px}.kt-shi textarea,.kt-shi input[type=text],.kt-shi input[type=password],.kt-shi input[type=search]{width:100%;box-sizing:border-box;border:1px solid #d8c8ae;border-radius:12px;padding:10px;font:16px/1.5 system-ui;background:#fffdf8;color:#2a221c}.kt-shi textarea{min-height:120px}'+
'.kt-shi .bt{display:flex;gap:8px;justify-content:flex-end;margin-top:10px;flex-wrap:wrap}.kt-shi .bt button{border:0;border-radius:12px;padding:10px 16px;font-weight:700;background:#e9dcc6;color:#2a221c}.kt-shi .bt button.a{background:#5b3d2a;color:#fff}.kt-shi .bt button.s{background:#f3d6d2;color:#8b1e16;margin-right:auto}'+
'.kt-tb{display:flex;gap:4px;margin-bottom:10px;overflow-x:auto}.kt-tb button{border:0;background:#ece1cd;color:#2a221c;border-radius:20px;padding:7px 12px;font-weight:600;white-space:nowrap}.kt-tb button.on{background:#5b3d2a;color:#fff}'+
'.kt-li{display:flex;gap:10px;align-items:flex-start;padding:9px 4px;border-bottom:1px solid #e6d9c2;cursor:pointer}.kt-li:last-child{border:0}.kt-li i{font-style:normal;min-width:52px;color:#8a6243;font-weight:700;font-size:13px}.kt-li span{flex:1;white-space:pre-wrap;word-break:break-word}.kt-li mark{background:#f6dd7a}'+
'.kt-ic{list-style:none;margin:0;padding:0}.kt-ic ul{list-style:none;margin:0;padding-left:16px}.kt-ic li>div{display:flex;justify-content:space-between;gap:8px;padding:8px 4px;border-bottom:1px solid #e6d9c2;cursor:pointer}.kt-ic li>div small{color:#8a6243}'+
'.kt-tm{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:14px}.kt-tm button{border:2px solid transparent;border-radius:12px;height:64px;font-weight:700}.kt-tm button.on{border-color:#5b3d2a}'+
'.kt-zm{display:flex;gap:8px;align-items:center;margin-bottom:12px}.kt-zm button{flex:1;border:0;background:#ece1cd;color:#2a221c;border-radius:12px;height:44px;font-weight:700;font-size:16px}.kt-zm span{min-width:60px;text-align:center;font-weight:700}'+
'body:has(#kt-o) #toast{bottom:150px!important;z-index:99}body:has(#kt-o) #toast:not(.on){opacity:0;pointer-events:none}.kt-sc{display:flex;align-items:center;justify-content:space-between;padding:8px 2px;border-top:1px solid #e6d9c2}.kt-bos2{color:#8a7a66;text-align:center;padding:18px}';
function stil(){if(document.getElementById('kt-css'))return;var s=document.createElement('style');s.id='kt-css';s.textContent=CSS;document.head.appendChild(s)}

/* ---------- Yedekleme: kitaplar + notlar + okuma defteri tek dosyada ---------- */
var MAGIC='MIHRABK1';
function lsHepsi(){var o={};try{for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(/^ihtisas\./.test(k))o[k]=localStorage.getItem(k)}}catch(x){}return o}
function notlarHepsi(){return is(NT,'readonly',function(s){return s.getAll()})}
function modal(h){var w=document.createElement('div');w.style.cssText='position:fixed;inset:0;z-index:60';w.innerHTML='<div class="kt-sh"><div class="kt-shi">'+h+'</div></div>';document.body.appendChild(w);var r={q:function(x){return w.querySelector(x)},kapa:function(){w.remove()}};w.firstChild.addEventListener('click',function(ev){if(ev.target===w.firstChild)r.kapa()});return r}
function dosyaVer(blob,ad,m){var f;try{f=new File([blob],ad,{type:blob.type||'application/octet-stream'})}catch(x){}
 var pay=f&&navigator.canShare&&navigator.canShare({files:[f]});
 m.q('.kt-ys').innerHTML='<p>✅ Yedek hazır: <b>'+e(ad)+'</b> ('+boyut(blob.size)+')</p><div class="bt">'+(pay?'<button class="a" data-pay>📤 Drive’a / başka yere kaydet</button>':'')+'<button class="'+(pay?'':'a')+'" data-ind>⬇ İndir</button></div><p style="color:#8a7a66;font-size:13px">Bu dosyayı Google Drive’a ya da bilgisayarına koy. Yeni telefonda “Yedekten geri yükle” ile seçmen yeterli.</p>';
 var ind=m.q('[data-ind]');ind.onclick=function(){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=ad;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},60000)};
 var pb=m.q('[data-pay]');if(pb)pb.onclick=function(){navigator.share({files:[f],title:ad}).catch(function(x){if(x&&x.name!=='AbortError')tost('Paylaşılamadı; “İndir”i dene')})}}
function yedekle(kitaplarla){var m=modal('<h3>💾 Kitaplığı yedekle</h3><div class="kt-ys"><p>Hazırlanıyor…</p></div><div class="bt"><button data-x>Kapat</button></div>');m.q('[data-x]').onclick=m.kapa;
 return Promise.all([hepsi(),notlarHepsi()]).then(function(r){var K=r[0],N=r[1],parcalar=[],meta=[];
  K.forEach(function(k){var b=kitaplarla?veriBlob(k):null,c={};for(var q in k)if(q!=='blob'&&q!=='veri')c[q]=k[q];c.boy=b?b.size:0;meta.push(c);if(b)parcalar.push(b)});
  var bas=new TextEncoder().encode(JSON.stringify({v:1,tarih:Date.now(),kitaplarla:!!kitaplarla,kitaplar:meta,notlar:N,ls:lsHepsi()})),uz=new Uint8Array(4);new DataView(uz.buffer).setUint32(0,bas.length,true);
  var blob=new Blob([MAGIC,uz,bas].concat(parcalar),{type:'application/octet-stream'}),t=new Date().toISOString().slice(0,10);
  dosyaVer(blob,'el-mihrab-kitaplik-'+(kitaplarla?'':'notlar-')+t+'.mihrab',m)}).catch(function(x){m.q('.kt-ys').innerHTML='<p>Yedek hazırlanamadı: '+e(hataMetni(x))+'</p>'})}
function geriYukle(f,bitti){var m=modal('<h3>♻️ Yedekten geri yükle</h3><div class="kt-ys"><p>Okunuyor…</p></div><div class="bt"><button data-x>Kapat</button></div>');m.q('[data-x]').onclick=m.kapa;var Y=m.q('.kt-ys');
 f.slice(0,12).arrayBuffer().then(function(b){if(new TextDecoder().decode(new Uint8Array(b,0,8))!==MAGIC)throw new Error('Bu dosya el-Mihrâb kitaplık yedeği değil');var L=new DataView(b).getUint32(8,true);return f.slice(12,12+L).text().then(function(t){return{h:JSON.parse(t),off:12+L}})})
 .then(function(r){var h=r.h,off=r.off,i=0,eklenen=0;return hepsi().then(function(Mevcut){var var_={};Mevcut.forEach(function(k){var_[k.id]=k});
  return h.kitaplar.reduce(function(pr,k){return pr.then(function(){var bas=off;off+=k.boy||0;i++;Y.innerHTML='<p>Kitap '+i+' / '+h.kitaplar.length+': '+e(k.ad)+'</p>';var eski=var_[k.id];
    if(!k.boy){if(eski){eski.sayfa=Math.max(eski.sayfa||1,k.sayfa||1);return koy(eski)}return}
    if(eski&&veriBlob(eski)&&(eski.son||0)>=(k.son||0))return;
    return f.slice(bas,bas+k.boy).arrayBuffer().then(function(a){var y={};for(var q in k)if(q!=='boy')y[q]=k[q];y.blob=new Blob([a],{type:'application/pdf'});eklenen++;return koy(y)})})},Promise.resolve())
  .then(function(){return(h.notlar||[]).reduce(function(pr,n){return pr.then(function(){return is(NT,'readonly',function(s){return s.get(n.id)}).then(function(e2){if(!e2)return notKoy(n);var t=e2;['s','n'].forEach(function(z){t[z]=t[z]||{};for(var p in n[z]||{}){var A=t[z][p]||[],ks={};A.forEach(function(x){ks[JSON.stringify(x)]=1});(n[z][p]||[]).forEach(function(x){if(!ks[JSON.stringify(x)])A.push(x)});t[z][p]=A}});t.y=(t.y||[]).concat((n.y||[]).filter(function(x){return(t.y||[]).indexOf(x)<0})).sort(function(a,b){return a-b});return notKoy(t)})})},Promise.resolve())})
  .then(function(){var ls=h.ls||{};for(var k in ls){try{var yeni=JSON.parse(ls[k]),eskiS=localStorage.getItem(k);if(!eskiS){localStorage.setItem(k,ls[k]);continue}var es=JSON.parse(eskiS);
    if(k==='ihtisas.defter.v1'){for(var il in yeni){var A=es[il]||[],ks={};A.forEach(function(x){ks[JSON.stringify(x)]=1});yeni[il].forEach(function(x){if(!ks[JSON.stringify(x)])A.push(x)});A.sort(function(a,b){return a.t<b.t?-1:a.t>b.t?1:0});es[il]=A}}
    else if(es&&typeof es==='object'&&!Array.isArray(es)){for(var q in yeni)if(!(q in es))es[q]=yeni[q]}
    localStorage.setItem(k,JSON.stringify(es))}catch(x){}}
   Y.innerHTML='<p>✅ Geri yükleme tamam. '+eklenen+' kitap eklendi; notlar, yer imleri ve okuma defteri birleştirildi.</p>';if(bitti)bitti()})})})
 .catch(function(x){Y.innerHTML='<p>Geri yüklenemedi: '+e(hataMetni(x))+'</p>'})}

/* ---------- Kitaplık listesi ---------- */
function goster(ic,o){stil();var tum=false;
 ic.innerHTML='<p class="lead">Kendi kitabını PDF olarak yükle, burada kâğıt renginde, geniş ekranda oku. Kalemle altını çiz, fosforlu kalemle işaretle, sayfaya not düş. Kitaplar ve notlar yalnız bu cihazda saklanır; kaldığın sayfa hatırlanır. Okurken 📒 ile okuduğun sayfalar okuma defterine eklenir.</p>'+
 '<div class="kt-up"><label>📄 PDF yükle<input type="file" accept="application/pdf,.pdf,application/octet-stream,*/*" multiple></label><small id="kt-yer"></small></div><div class="kt-up kt-yd"><button type="button" data-yd>💾 Yedekle</button><label class="ikinci">♻️ Yedekten geri yükle<input type="file" data-gy></label></div><div class="kt-sw"><button class="on" data-t="0">'+e(o.ad)+'</button><button data-t="1">Bütün kitaplarım</button></div><div class="kt-l"></div>';
 var L=ic.querySelector('.kt-l'),inp=ic.querySelector('.kt-up input[type=file]:not([data-gy])');
 ic.querySelector('[data-yd]').onclick=function(){var m=modal('<h3>💾 Kitaplığı yedekle</h3><p>Ne yedeklensin?</p><div class="bt" style="flex-direction:column;align-items:stretch"><button class="a" data-t="1">📚 Kitaplar + notlar + okuma defteri (tam yedek, büyük dosya)</button><button data-t="0">📝 Yalnız notlar, yer imleri ve okuma defteri (küçük dosya)</button><button data-x>Vazgeç</button></div>');m.q('[data-x]').onclick=m.kapa;[].forEach.call([m.q('[data-t="1"]'),m.q('[data-t="0"]')],function(b){b.onclick=function(){m.kapa();yedekle(b.dataset.t==='1')}})};
 var gy=ic.querySelector('[data-gy]');gy.onchange=function(){var f=gy.files&&gy.files[0];gy.value='';if(f){if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(function(){});geriYukle(f,ciz)}};
 function yer(){if(navigator.storage&&navigator.storage.estimate)navigator.storage.estimate().then(function(s){var y=ic.querySelector('#kt-yer');if(y&&s.quota)y.textContent='Kullanılan: '+boyut(s.usage||0)+' · boş yer: '+boyut(Math.max(0,s.quota-(s.usage||0)))}).catch(function(){})}
 function ciz(){hepsi().then(function(K){K=K.filter(function(k){return tum||k.ilim===o.ilim}).sort(function(a,b){return(b.son||b.eklendi)-(a.son||a.eklendi)});
  L.innerHTML=K.length?K.map(function(k){var p=k.toplam?Math.round(100*(k.sayfa||1)/k.toplam):0;return'<div class="kt-k" data-id="'+e(k.id)+'"><div class="kp">'+(k.kapak?'<img alt="" src="'+e(k.kapak)+'">':'📖')+'</div><div class="ki"><b>'+e(k.ad)+'</b><small>'+(k.toplam?'Sayfa '+(k.sayfa||1)+' / '+k.toplam+' · ':'')+boyut(k.boyut)+(tum&&k.ilimAd?' · '+e(k.ilimAd):'')+'</small><div class="bar"><i style="width:'+p+'%"></i></div></div><button data-ad aria-label="Adını değiştir">✎</button><button data-sil aria-label="Sil">🗑</button></div>'}).join(''):'<div class="kt-bos">Henüz kitap yok.<br>“PDF yükle” ile ilk kitabını ekle.</div>';
  [].forEach.call(L.querySelectorAll('.kt-k'),function(d){var id=d.dataset.id;
   d.querySelector('.ki').onclick=d.querySelector('.kp').onclick=function(){oku(id,o,ciz)};
   d.querySelector('[data-sil]').onclick=function(){if(confirm('Bu kitap ve üzerindeki notlar cihazdan silinsin mi?'))sil(id).then(function(){tost('Silindi');ciz();yer()})};
   d.querySelector('[data-ad]').onclick=function(){al(id).then(function(k){var a=prompt('Kitabın adı',k.ad);if(a&&a.trim()){k.ad=a.trim();koy(k).then(ciz)}})}});yer()}).catch(function(x){L.innerHTML='<div class="kt-bos">Kitaplık açılamadı: '+e(hataMetni(x))+'<br><small>Gizli sekmede kitaplık çalışmaz.</small></div>'})}
 [].forEach.call(ic.querySelectorAll('.kt-sw button'),function(b){b.onclick=function(){tum=b.dataset.t==='1';[].forEach.call(ic.querySelectorAll('.kt-sw button'),function(x){x.classList.toggle('on',x===b)});ciz()}});
 inp.onchange=function(){var F=[].slice.call(inp.files||[]);inp.value='';if(!F.length)return;
  if(navigator.storage&&navigator.storage.persist)navigator.storage.persist().catch(function(){});
  var sira=Promise.resolve();F.forEach(function(f){sira=sira.then(function(){return ekle(f,o).catch(function(x){console.error(x);tost(f.name+': '+(x&&x.name==='QuotaExceededError'?'yer yetmiyor':hataMetni(x)))})}).then(ciz)});sira.then(yer)};
 ciz()}

function ekle(f,o){tost('Yükleniyor: '+f.name);
 return f.slice(0,1024).arrayBuffer().then(function(b){var s='';var u=new Uint8Array(b);for(var i=0;i<u.length;i++)s+=String.fromCharCode(u[i]);
  if(s.indexOf('%PDF')<0)throw new Error('Bu dosya PDF değil');
  return f.size<=400*1048576?f.arrayBuffer().then(function(a){return new Blob([a],{type:'application/pdf'})}):f}).then(function(blob){
  var k={id:'k'+Date.now().toString(36)+Math.random().toString(36).slice(2,6),ilim:o.ilim,ilimAd:o.ad,ad:f.name.replace(/\.pdf$/i,'').replace(/[_]+/g,' ').trim()||'Adsız kitap',boyut:f.size,eklendi:Date.now(),sayfa:1,blob:blob};
  return koy(k).then(function(){return pdfjs().then(function(P){return belgeAc(P,blob,function(){return Promise.resolve(null)})}).then(function(d){k.toplam=d.numPages;
   return d.getMetadata().catch(function(){return{}}).then(function(m){var t=m&&m.info&&m.info.Title;if(t&&t.trim().length>2&&!/^(untitled|microsoft|document|adsız|about:|http)/i.test(t.trim()))k.ad=t.trim();return d.getPage(1)}).then(function(p){var v=p.getViewport({scale:1}),s=140/v.width,vv=p.getViewport({scale:s}),c=document.createElement('canvas');c.width=Math.ceil(vv.width);c.height=Math.ceil(vv.height);var x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);return p.render({canvasContext:x,viewport:vv}).promise.then(function(){k.kapak=c.toDataURL('image/jpeg',.72)})}).then(function(){yoket(d)},function(x){yoket(d);throw x})}).catch(function(x){console.warn('kapak/sayfa',x);if(x&&x.iptal)k.sifreli=1}).then(function(){return koy(k)}).then(function(){tost('Eklendi: '+k.ad)})})})}

/* ---------- Okurken sözlük ---------- */
var SZ={},HR=/[ً-ْٰـ]/g;
function szYukle(d){if(!SZ[d])SZ[d]=fetch('data/roman/sozluk_'+d+'.json').then(function(r){if(!r.ok)throw 0;return r.json()}).catch(function(){delete SZ[d];return{}});return SZ[d]}
function szNorm(w,d){if(d==='en'){w=w.toLowerCase().trim().replace(/^['".,!?;:]+|['".,!?;:]+$/g,'');return /'s$/.test(w)?w.slice(0,-2):w}w=w.replace(/[«»،.؟!:؛()\-"]/g,'').replace(HR,'').trim();if(d==='ar')w=w.replace(/[إأآٱ]/g,'ا').replace(/ى/g,'ي').replace(/ی/g,'ي').replace(/ک/g,'ك');if(d==='fa')w=w.replace(/ي/g,'ی').replace(/ك/g,'ک').replace(/ى/g,'ی');return w}
function szKok(n,d){var c=[n];if(d==='ar'){['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك','س'].forEach(function(p){if(n.indexOf(p)===0&&n.length-p.length>=3){var r=n.slice(p.length);c.push(r,'ال'+r)}});var t=n.replace(/^(وال|بال|فال|ال|و|ف|ب)/,'');['هما','هم','هن','ها','كم','نا','ني','ه','ك','ي','ون','ين','ات','ان','ة'].forEach(function(s){if(t.length-s.length>=3&&t.slice(-s.length)===s)c.push(t.slice(0,-s.length),'ال'+t.slice(0,-s.length))});c.push(n.replace(/ة$/,'ه'),n.replace(/ه$/,'ة'))}
 else if(d==='fa'){var P=/^(نمی‌|نمی|می‌|می|ب|ن)/,S=/‌?(هایی|های|ها|ترین|تر|گان|ان|ای|اش|ام|ات|یم|ید|ند|ی|ش|م)$/;c.push(n.replace(P,''),n.replace(S,''),n.replace(P,'').replace(S,''),n.replace(/‌/g,''));if(/گان$/.test(n))c.push(n.slice(0,-3)+'ه')}
 else c.push(n.replace(/ies$/,'y'),n.replace(/ied$/,'y'),n.replace(/(ing|ed|es|s|ly|er|est)$/,''),n.replace(/ing$/,'e'),n.replace(/ed$/,'e'),n.replace(/([b-df-hj-np-tv-z])\1(ing|ed|er|est)$/,'$1'),n.replace(/ily$/,'y'),n.replace(/(ness|ment|ful|less)$/,''));return c}
function szDiller(w){if(/[A-Za-z]/.test(w))return['en'];if(/[پچژگ]|[یک]/.test(w))return['fa','ar'];return['ar','fa']}
function szAra(w){w=(w||'').normalize('NFKC').trim();if(!w)return Promise.resolve(null);var D=szDiller(w),ters=w.split('').reverse().join('');
 return D.reduce(function(pr,d){return pr.then(function(r){if(r)return r;return szYukle(d).then(function(G){var adaylar=[w,ters];for(var i=0;i<adaylar.length;i++){var K=szKok(szNorm(adaylar[i],d),d);for(var j=0;j<K.length;j++)if(K[j]&&G[K[j]])return{w:adaylar[i],k:K[j],m:G[K[j]],d:d}}return null})})},Promise.resolve(null))}

/* ---------- Okuyucu ---------- */
var AY='ihtisas.okuyucu.v2';
function ayarA(){try{return JSON.parse(localStorage.getItem(AY))||{}}catch(x){return{}}}
function ayarY(a){try{localStorage.setItem(AY,JSON.stringify(a))}catch(x){}}
var ARAC=[['el','✋','Kaydır'],['sz','📖','Sözlük'],['k','✏️','Kalem'],['f','🖍️','Fosforlu'],['c','〰️','Altını çiz'],['n','📝','Not'],['s','🧽','Silgi']];
var RENK={k:['#1f3f8f','#b3261e','#1d7a43','#222222','#7b3fa0'],f:['#ffd84a','#8fe08a','#7cc8ff','#ff9ec2','#ffb56b'],c:['#b3261e','#1f3f8f','#1d7a43','#222222','#c07a00']};
var KAL={k:3,f:18,c:3.2};

function oku(id,o,kapaninca){stil();var A=ayarA();A.duzen=A.duzen||'dikey';A.tema=A.tema||'kagit';A.zoom=A.zoom||1;A.renk=A.renk||{};
 var ov=document.createElement('div');ov.id='kt-o';ov.className=A.tema+(A.duzen!=='dikey'?' sayfali':'');
 ov.innerHTML='<div id="kt-b"><button data-k title="Kapat">✕</button><b>…</b><button data-pn title="İçindekiler, notlar, arama">☰</button><button data-yi title="Yer imi">🔖</button><button data-ar title="Kalem ve notlar">🖊️</button><button data-gr title="Görünüm">Aa</button><button data-d title="Okuma defterine ekle">📒</button></div>'+
 '<div id="kt-s"><div id="kt-in"></div></div>'+
 '<div id="kt-a"><div class="kt-ar"></div><div class="kt-sl"><input type="range" min="1" value="1"><span>1 / 1</span></div></div><div id="kt-y">Kitap açılıyor…</div>';
 document.body.appendChild(ov);ov.querySelector('.kt-sl input').style.direction=A.duzen==='rtl'?'rtl':'';var eskiOv=document.body.style.overflow;document.body.style.overflow='hidden';
 var $=function(q){return ov.querySelector(q)};
 var S=$('#kt-s'),IN=$('#kt-in'),bar=$('#kt-b'),alt=$('#kt-a'),AR=$('.kt-ar'),rng=$('.kt-sl input'),gs=$('.kt-sl span'),Y=$('#kt-y');
 var K,doc,P,n=0,oran=[],ciz={},su=1,bas=1,enCok=1,io,kayT,notT,bitti=false,mod='el',N=null,geriY=[],wl=null,anaW=0;
 history.pushState({kt:1},'');
 function kapat(geri){if(bitti)return;bitti=true;var kp=Promise.all([kaydet(),notKaydet(true)]);if(io)io.disconnect();for(var q in ciz)birak(+q);yoket(doc);
  if(document.fullscreenElement&&document.exitFullscreen)document.exitFullscreen().catch(function(){});if(wl){wl.release().catch(function(){});wl=null}
  ov.remove();document.body.style.overflow=eskiOv;removeEventListener('popstate',pop);removeEventListener('resize',rs);removeEventListener('keydown',tus);document.removeEventListener('visibilitychange',gor);
  if(!geri&&history.state&&history.state.kt)history.back();kp.then(function(){if(kapaninca)kapaninca()})}
 function pop(){var s=ov.querySelectorAll('.kt-sh');if(s.length){s[s.length-1].remove();history.pushState({kt:1},'');return}kapat(true)}addEventListener('popstate',pop);
 function kaydet(){if(!K)return Promise.resolve();K.sayfa=su;K.son=Date.now();return koy(K).catch(function(){})}
 function notKaydet(hemen){clearTimeout(notT);if(!N||!N.kirli)return Promise.resolve();if(!hemen){notT=setTimeout(function(){notKaydet(true)},700);return Promise.resolve()}N.kirli=0;var c={id:N.id,s:N.s,n:N.n,y:N.y};return notKoy(c).catch(function(x){console.warn(x);tost('Not kaydedilemedi')})}
 function kirlet(){N.kirli=1;notKaydet()}
 function uyanik(){if(navigator.wakeLock&&!wl&&document.visibilityState==='visible')navigator.wakeLock.request('screen').then(function(w){wl=w;w.addEventListener('release',function(){wl=null})}).catch(function(){})}
 function gor(){if(document.visibilityState==='visible')uyanik();else{kaydet();notKaydet(true)}}document.addEventListener('visibilitychange',gor);uyanik();
 function gizle(g){bar.classList.toggle('gz',g);alt.classList.toggle('gz',g)}
 $('[data-k]').onclick=function(){kapat()};
 $('[data-ar]').onclick=function(){var a=!AR.classList.contains('ac');AR.classList.toggle('ac',a);this.classList.toggle('on',a);if(!a)modSec('el');else aracCiz()};
 $('[data-gr]').onclick=gorunum;
 $('[data-pn]').onclick=function(){panel('ic')};
 $('[data-yi]').onclick=function(){if(!N)return;var i=N.y.indexOf(su);if(i>-1){N.y.splice(i,1);tost('Yer imi kaldırıldı')}else{N.y.push(su);N.y.sort(function(a,b){return a-b});tost('Sayfa '+su+' yer imlerine eklendi')}kirlet();yerImiCiz()};
 $('[data-d]').onclick=function(){if(!o.defter){tost('Okuma defteri yok');return}var s=Math.max(1,enCok-bas+1);
  var sh=pencere('<h3>📒 Okuma defterine ekle</h3><p style="margin:0 0 8px">“'+e(K.ad)+'” · sayfa '+bas+'–'+enCok+'</p><label>Kaç sayfa okudun?<input type="text" inputmode="numeric" value="'+s+'"></label><div class="bt"><button data-x>Vazgeç</button><button class="a" data-t>Ekle</button></div>');
  sh.q('[data-x]').onclick=sh.kapa;sh.q('[data-t]').onclick=function(){var x=parseInt(sh.q('input').value,10);if(!x){tost('Sayı yaz');return}o.defter({k:K.ad,s:x,n:'s. '+bas+'–'+enCok});tost('Deftere eklendi: '+x+' sayfa');bas=su;enCok=su;sh.kapa()}};
 gs.onclick=function(){var sh=pencere('<h3>Sayfaya git</h3><input type="text" inputmode="numeric" placeholder="1 – '+n+'" value="'+su+'"><div class="bt"><button data-x>Vazgeç</button><button class="a" data-t>Git</button></div>');var i=sh.q('input');i.select();sh.q('[data-x]').onclick=sh.kapa;sh.q('[data-t]').onclick=i.onkeydown=function(ev){if(ev.type==='keydown'&&ev.key!=='Enter')return;var x=parseInt(i.value,10);if(x>=1&&x<=n){git(x);sh.kapa()}}};
 rng.oninput=function(){gs.textContent=rng.value+' / '+n};rng.onchange=function(){git(+rng.value)};
 function pencere(h){var b=document.createElement('div');b.className='kt-sh';b.innerHTML='<div class="kt-shi">'+h+'</div>';ov.appendChild(b);var r={el:b.firstChild,q:function(s){return b.querySelector(s)},kapa:function(){b.remove()}};b.addEventListener('click',function(ev){if(ev.target===b)r.kapa()});return r}
 function sinif(){ov.className=A.tema+(sayfali()?' sayfali':'');rng.style.direction=A.duzen==='rtl'?'rtl':''}
 function sayfali(){return A.duzen==='rtl'||A.duzen==='ltr'}
 function temaUygula(t){A.tema=t;sinif();ayarY(A)}
 function duzenUygula(dz){var p=su;A.duzen=dz;ayarY(A);sinif();IN.dir=dz==='rtl'?'rtl':'ltr';S.scrollLeft=0;S.scrollTop=0;yerlestir();gozlem();git(p);yeniden()}
 function gozlem(){if(io)io.disconnect();io=new IntersectionObserver(function(G){G.forEach(function(g){if(g.isIntersecting)sayfaCiz(+g.target.dataset.p)})},{root:S,rootMargin:sayfali()?'0px 150%':'120% 0px'});[].forEach.call(IN.children,function(x){io.observe(x)})}
 function gorunum(){var T=[['kagit','Kâğıt','#f6eedc','#2a221c'],['sepya','Sepya','#e9d6b0','#3b2a17'],['gece','Gece','#1d1b18','#e8dfd2'],['beyaz','Beyaz','#ffffff','#111']];
  var sh=pencere('<h3>Görünüm</h3><div class="kt-tm">'+T.map(function(t){return'<button data-t="'+t[0]+'" style="background:'+t[2]+';color:'+t[3]+'" class="'+(A.tema===t[0]?'on':'')+'">'+t[1]+'</button>'}).join('')+'</div>'+
  '<h3 style="font-size:15px;margin:4px 0 8px">Sayfa düzeni</h3><div class="kt-tb kt-dz">'+[['dikey','↕ Aşağı kaydır'],['rtl','← Sağdan sola (Arapça kitap)'],['ltr','→ Soldan sağa']].map(function(x){return'<button data-dz="'+x[0]+'" class="'+(A.duzen===x[0]?'on':'')+'">'+x[1]+'</button>'}).join('')+'</div>'+
  '<div class="kt-zm"><button data-z="-">A−</button><span>%'+Math.round(A.zoom*100)+'</span><button data-z="+">A+</button><button data-z="1">Sığdır</button></div>'+
  '<div class="kt-sc"><span>Tam ekran</span><button class="kt-btn" data-f>⛶ Aç/kapat</button></div><p style="color:#8a7a66;font-size:13px;margin:8px 0 0">İki parmakla da yakınlaştırıp uzaklaştırabilirsin. Kitap açıkken ekran kararmaz.</p>');
  [].forEach.call(sh.el.querySelectorAll('[data-t]'),function(b){b.onclick=function(){temaUygula(b.dataset.t);[].forEach.call(sh.el.querySelectorAll('[data-t]'),function(x){x.classList.toggle('on',x===b)})}});
  [].forEach.call(sh.el.querySelectorAll('[data-dz]'),function(b){b.onclick=function(){duzenUygula(b.dataset.dz);[].forEach.call(sh.el.querySelectorAll('[data-dz]'),function(x){x.classList.toggle('on',x===b)})}});
  [].forEach.call(sh.el.querySelectorAll('[data-z]'),function(b){b.onclick=function(){var z=b.dataset.z==='1'?1:b.dataset.z==='+'?A.zoom*1.2:A.zoom/1.2;yakinlas(z);sh.q('.kt-zm span').textContent='%'+Math.round(A.zoom*100)}});
  sh.q('[data-f]').onclick=function(){if(document.fullscreenElement)document.exitFullscreen();else if(ov.requestFullscreen)ov.requestFullscreen().catch(function(){tost('Tam ekran desteklenmiyor')});else tost('Tam ekran desteklenmiyor')}}
 function aracCiz(){var h=ARAC.map(function(a){return'<button data-m="'+a[0]+'" class="'+(mod===a[0]?'on':'')+'">'+a[1]+'<small>'+a[2]+'</small></button>'}).join('')+'<button data-u>↶<small>Geri al</small></button>';
  if(RENK[mod]){h+='<span class="ay"></span>'+RENK[mod].map(function(r){return'<button class="rk'+((A.renk[mod]||RENK[mod][0])===r?' on':'')+'" data-r="'+r+'" style="background:'+r+'"></button>'}).join('')}
  AR.innerHTML=h;
  [].forEach.call(AR.querySelectorAll('[data-m]'),function(b){b.onclick=function(){modSec(b.dataset.m)}});
  [].forEach.call(AR.querySelectorAll('[data-r]'),function(b){b.onclick=function(){A.renk[mod]=b.dataset.r;ayarY(A);aracCiz()}});
  AR.querySelector('[data-u]').onclick=geriAl}
 function modSec(m){mod=m;S.classList.toggle('ciz',m!=='el'&&m!=='sz');aracCiz();if(m!=='el'){var ip={sz:'Anlamını görmek istediğin kelimeye dokun (metinli PDF’lerde). Kaydır modunda kelimeye basılı tutmak da olur.',k:'Kalemle sayfaya yaz. Kaydırmak için iki parmak kullan.',f:'Fosforlu kalem: satırın üstünden geç (düz geçersen dümdüz olur).',c:'Altını çizmek istediğin satırın altından parmağını kaydır.',n:'Not düşmek istediğin yere dokun.',s:'Silmek istediğin çizginin üstünden geç.'}[m];if(ip)tost(ip)}}
 function gen(){return Math.round(Math.min(S.clientWidth-16,1000)*A.zoom)}
 function yerlestir(){var pd=IN.children;if(sayfali()){var vw=S.clientWidth,vh=S.clientHeight;IN.style.width='';for(var j=0;j<n;j++){var ww=Math.round(Math.min(vw-16,(vh-16)/oran[j])*A.zoom),hh=Math.round(ww*oran[j]);pd[j].style.width=ww+'px';pd[j].style.height=hh+'px';pd[j].style.margin=Math.max(8,(vh-hh)/2)+'px '+Math.max(8,(vw-ww)/2)+'px'}return}var w=gen();IN.style.width=Math.max(w+16,S.clientWidth)+'px';for(var i=0;i<n;i++){pd[i].style.margin='';pd[i].style.width=w+'px';pd[i].style.height=Math.round(w*oran[i])+'px'}}
 function odak(mx,my){var cy=S.scrollTop+my,p=sayfaBul(cy),d=IN.children[p-1];return{p:p,fy:(cy-d.offsetTop)/d.offsetHeight,fx:(S.scrollLeft+mx-d.offsetLeft)/d.offsetWidth,mx:mx,my:my}}
 function odakla(f){var d=IN.children[f.p-1];S.scrollTop=d.offsetTop+f.fy*d.offsetHeight-f.my;S.scrollLeft=d.offsetLeft+f.fx*d.offsetWidth-f.mx}
 function yakinlas(z,f){z=Math.max(.5,Math.min(4,z));if(Math.abs(z-A.zoom)<.001)return;if(sayfali()){var p0=su;A.zoom=+z.toFixed(3);ayarY(A);yerlestir();git(p0);yeniden();return}f=f||odak(S.clientWidth/2,S.clientHeight/2);A.zoom=+z.toFixed(3);ayarY(A);yerlestir();odakla(f);yeniden()}
 function yeniden(){for(var q in ciz)birak(+q);clearTimeout(yeniden.t);yeniden.t=setTimeout(function(){for(var q=Math.max(1,su-1);q<=Math.min(n,su+2);q++)sayfaCiz(q)},40)}
 function rs(){clearTimeout(rs.t);rs.t=setTimeout(function(){if(!n||S.clientWidth===anaW)return;anaW=S.clientWidth;if(sayfali()){var p0=su;yerlestir();git(p0);yeniden();return}var f=odak(0,0);yerlestir();odakla(f);yeniden()},200)}addEventListener('resize',rs);
 function sayfaBul(y){var pd=IN.children,lo=0,hi=n-1;while(lo<hi){var md=(lo+hi+1)>>1;if(pd[md].offsetTop<=y)lo=md;else hi=md-1}return lo+1}
 function git(p){var d=IN.children[p-1];if(d){if(sayfali()){var R=S.getBoundingClientRect(),r=d.getBoundingClientRect();S.scrollLeft+=r.left+r.width/2-(R.left+R.width/2);S.scrollTop=Math.max(0,d.offsetTop-8)}else S.scrollTop=d.offsetTop-58}su=p;guncel()}
 function simdiki(){if(!sayfali())return sayfaBul(S.scrollTop+S.clientHeight/3);var R=S.getBoundingClientRect(),cx=R.left+R.width/2,pd=IN.children,b=Math.max(0,su-1);for(var k=0;k<n;k++){var c=[b+k,b-k];for(var z=0;z<2;z++){var i=c[z];if(i<0||i>=n)continue;var r=pd[i].getBoundingClientRect(),ml=parseFloat(pd[i].style.marginLeft)||0;if(r.left-ml<=cx&&r.right+ml>=cx)return i+1}}return su}
 function guncel(){rng.value=su;gs.textContent=su+' / '+n;if(su>enCok)enCok=su;if(su<bas)bas=su;clearTimeout(kayT);kayT=setTimeout(kaydet,800)}
 S.addEventListener('scroll',function(){var p=simdiki();if(p!==su){su=p;guncel()}for(var q in ciz)if(Math.abs(q-su)>5)birak(+q)},{passive:true});
 function tus(ev){if(ov.querySelector('.kt-sh')||/INPUT|TEXTAREA/.test(ev.target.tagName))return;var k=ev.key;
  if(k==='Escape')kapat();else if(k==='PageDown'||k===' '){S.scrollTop+=S.clientHeight*.9;ev.preventDefault()}else if(k==='PageUp'){S.scrollTop-=S.clientHeight*.9;ev.preventDefault()}
  else if(k==='ArrowRight'||k==='ArrowLeft'){if(A.zoom<=1.01||sayfali()){var ileri=(k==='ArrowRight')!==(A.duzen==='rtl');git(Math.max(1,Math.min(n,su+(ileri?1:-1))));ev.preventDefault()}}else if(k==='+'||k==='=')yakinlas(A.zoom*1.2);else if(k==='-')yakinlas(A.zoom/1.2)}addEventListener('keydown',tus);
 function sayfaCiz(p){if(ciz[p]||!doc||bitti)return;var d=IN.children[p-1];if(!d)return;var tok={iptal:false,cancel:function(){this.iptal=true;if(this.g)try{this.g.cancel()}catch(x){}}};ciz[p]=tok;
  doc.getPage(p).then(function(pg){if(tok.iptal)return;var w=d.clientWidth,v1=pg.getViewport({scale:1}),r=v1.height/v1.width;
   if(Math.abs(r-oran[p-1])>.005){var eskiTop=S.scrollTop,ust=d.offsetTop<S.scrollTop,fark=Math.round(w*r)-Math.round(w*oran[p-1]);oran[p-1]=r;d.style.height=Math.round(w*r)+'px';if(ust)S.scrollTop=eskiTop+fark;svgBoyut(p)}
   var dpr=Math.min(window.devicePixelRatio||1,2.5),sc=w/v1.width*dpr,azami=Math.sqrt(9e6/(v1.width*v1.height));if(sc>azami)sc=azami;
   var v=pg.getViewport({scale:sc}),c=document.createElement('canvas');c.width=Math.floor(v.width);c.height=Math.floor(v.height);
   tok.g=pg.render({canvasContext:c.getContext('2d',{alpha:false}),viewport:v,background:'#ffffff'});
   return tok.g.promise.then(function(){if(tok.iptal){c.width=c.height=0;return}var pn=d.querySelector('.pn');if(pn)pn.style.display='none';var e2=d.querySelector('canvas');if(e2){e2.width=e2.height=0;e2.remove()}d.insertBefore(c,d.firstChild)})}).catch(function(x){if(x&&x.name!=='RenderingCancelledException'){console.warn('sayfa',p,x);delete ciz[p];var pn=d.querySelector('.pn');if(pn)pn.textContent=p+' · bu sayfa çizilemedi'}})}
 function birak(p){var t=ciz[p];if(!t)return;t.cancel();delete ciz[p];var d=IN.children[p-1];if(d){var c=d.querySelector('canvas');if(c){c.width=c.height=0;c.remove()}var pn=d.querySelector('.pn');if(pn)pn.style.display=''}}
 function svgAl(p){var d=IN.children[p-1];return d&&d.querySelector('svg')}
 function svgBoyut(p){var s=svgAl(p);if(s)s.setAttribute('viewBox','0 0 1000 '+Math.round(1000*oran[p-1]))}
 function yolD(st){var d=st.d,h='M'+d[0]+' '+d[1];if(d.length===2)h+='l0.1 0';for(var i=2;i<d.length;i+=2)h+='L'+d[i]+' '+d[i+1];return h}
 function cizgiEl(st){var y=document.createElementNS(SVGNS,'path');y.setAttribute('d',yolD(st));y.setAttribute('fill','none');y.setAttribute('stroke',st.r);y.setAttribute('stroke-width',st.w);y.setAttribute('stroke-linecap',st.t==='f'?'butt':'round');y.setAttribute('stroke-linejoin','round');if(st.t==='f'){y.setAttribute('stroke-opacity','.42');y.setAttribute('class','fs')}return y}
 function notEl(nt,i,p){var g=document.createElementNS(SVGNS,'g');g.setAttribute('class','nt');g.setAttribute('transform','translate('+nt.x+' '+nt.y+')');g.innerHTML='<circle r="30" fill="#f2c14e" stroke="#8a5a12" stroke-width="2.5"/><text y="10" text-anchor="middle" font-size="30">📝</text>';g.addEventListener('pointerdown',function(ev){ev.stopPropagation()});g.addEventListener('click',function(ev){ev.stopPropagation();notAc(p,i)});return g}
 function sayfaNotCiz(p){var s=svgAl(p);if(!s||!N)return;s.innerHTML='';(N.s[p]||[]).forEach(function(st){s.appendChild(cizgiEl(st))});(N.n[p]||[]).forEach(function(nt,i){s.appendChild(notEl(nt,i,p))})}
 function yerImiCiz(){if(!N)return;[].forEach.call(IN.children,function(d,i){d.classList.toggle('yer',N.y.indexOf(i+1)>-1)})}
 function geriAl(){var g=geriY.pop();if(!g){tost('Geri alınacak bir şey yok');return}if(g.t==='s'){var L=N.s[g.p]||(N.s[g.p]=[]);if(g.op==='ekle'){var i=L.indexOf(g.o);if(i>-1)L.splice(i,1)}else L.push(g.o)}else if(g.t==='n'){var M=N.n[g.p]||(N.n[g.p]=[]);if(g.op==='ekle'){var j=M.indexOf(g.o);if(j>-1)M.splice(j,1)}else if(g.op==='sil')M.push(g.o);else if(g.op==='duz')g.o.m=g.eski}kirlet();sayfaNotCiz(g.p)}
 function notAc(p,i,yeni){var nt=yeni||N.n[p][i];
  var sh=pencere('<h3>📝 Not · sayfa '+p+'</h3><textarea placeholder="Notunu yaz…">'+e(nt.m||'')+'</textarea>'+(nt.z?'<small style="color:#8a7a66">'+new Date(nt.z).toLocaleString('tr-TR')+'</small>':'')+'<div class="bt">'+(yeni?'':'<button class="s" data-s>Sil</button>')+'<button data-x>Vazgeç</button><button class="a" data-t>Kaydet</button></div>');
  var ta=sh.q('textarea');setTimeout(function(){ta.focus()},50);
  sh.q('[data-x]').onclick=sh.kapa;
  if(!yeni)sh.q('[data-s]').onclick=function(){var M=N.n[p];M.splice(M.indexOf(nt),1);geriY.push({t:'n',op:'sil',p:p,o:nt});kirlet();sayfaNotCiz(p);sh.kapa();tost('Not silindi')};
  sh.q('[data-t]').onclick=function(){var m=ta.value.trim();if(!m){sh.kapa();return}if(yeni){nt.m=m;nt.z=Date.now();(N.n[p]=N.n[p]||[]).push(nt);geriY.push({t:'n',op:'ekle',p:p,o:nt})}else{geriY.push({t:'n',op:'duz',p:p,o:nt,eski:nt.m});nt.m=m;nt.z=Date.now()}kirlet();sayfaNotCiz(p);sh.kapa();tost('Not kaydedildi')}}
 function kelimeAl(p,cx,cy){var d=IN.children[p-1];return doc.getPage(p).then(function(pg){var v=pg.getViewport({scale:1}),r=d.getBoundingClientRect(),pt=v.convertToPdfPoint((cx-r.left)/r.width*v.width,(cy-r.top)/r.height*v.height);
  return pg.getTextContent().then(function(tc){var I=[];tc.items.forEach(function(it){if(!it.str)return;var t=it.transform,h=it.height||Math.abs(t[3])||10;if(!(it.width>0))return;I.push({s:it.str.normalize('NFKC'),x:t[4],y:t[5],w:it.width,h:h,dir:it.dir})});
   var en=-1,eb=1e9;I.forEach(function(o,k){if(!o.s.trim())return;var dx=pt[0]<o.x?o.x-pt[0]:pt[0]>o.x+o.w?pt[0]-o.x-o.w:0,dy=pt[1]<o.y-o.h*.3?o.y-o.h*.3-pt[1]:pt[1]>o.y+o.h*1.05?pt[1]-o.y-o.h*1.05:0,u=dx*dx+dy*dy*4;if(u<eb){eb=u;en=k}});
   if(en<0||eb>900)return null;var o=I[en],hrf=/[\p{L}\p{M}‌'’]/u,ar=/[؀-ۿ]/.test(o.s);
   /* aynı satırdaki parçalar (soldan sağa sıralı) */
   var L=I.filter(function(q){return Math.abs(q.y-o.y)<o.h*.5}).sort(function(a,b){return a.x-b.x}),k=L.indexOf(o);
   function harfmi(q){return q.s.length>0&&[].every.call(q.s,function(c){return hrf.test(c)})}
   function bitisik(a,b){return b.x-(a.x+a.w)<Math.max(a.h,b.h)*.18}
   if(harfmi(o)&&o.s.length<=3){var i0=k,i1=k;while(i0>0&&harfmi(L[i0-1])&&bitisik(L[i0-1],L[i0]))i0--;while(i1<L.length-1&&harfmi(L[i1+1])&&bitisik(L[i1],L[i1+1]))i1++;var P=L.slice(i0,i1+1);if(ar)P.reverse();var w=P.map(function(q){return q.s}).join('');if(w.length>1)return w}
   var s2=o.s,fr=Math.max(0,Math.min(.999,(pt[0]-o.x)/o.w)),rtl=o.dir==='rtl'||ar,i=Math.floor((rtl?1-fr:fr)*s2.length);if(i>=s2.length)i=s2.length-1;
   while(i>0&&!hrf.test(s2[i]))i--;var a2=i,b2=i;while(a2>0&&hrf.test(s2[a2-1]))a2--;while(b2<s2.length-1&&hrf.test(s2[b2+1]))b2++;return s2.slice(a2,b2+1).replace(/['’]+$/,'')||null})})}
 function sozlukAc(kelime,bos){var sh=pencere('<h3>📖 Sözlük</h3><input type="search" dir="auto" style="font-size:22px;font-family:Amiri,serif" value="'+e(kelime||'')+'" placeholder="Kelime yaz…"><div class="kt-szs" style="margin:10px 2px;font-size:17px;min-height:48px"></div><div class="bt"><button data-ac>Sözlükte aç</button><button class="a" data-x>Kapat</button></div>');
  var i=sh.q('input'),R2=sh.q('.kt-szs'),son=null;sh.q('[data-x]').onclick=sh.kapa;
  function bak(){var w=i.value.trim();if(!w){R2.innerHTML=bos?'<span style="color:#8a7a66">'+bos+'</span>':'';return}R2.innerHTML='<span style="color:#8a7a66">Bakılıyor…</span>';szAra(w).then(function(r){son=r;if(i.value.trim()!==w)return;R2.innerHTML=r?'<div dir="auto" style="font:700 22px Amiri,serif">'+e(r.k)+'</div><div>'+e(r.m)+'</div><small style="color:#8a7a66">'+({ar:'Arapça',fa:'Farsça',en:'İngilizce'})[r.d]+' sözlük</small>':'<span style="color:#8a7a66">Sözlükte bulunamadı. Kelimeyi düzeltip tekrar dene ya da “Sözlükte aç” ile ara.</span>'})}
  i.oninput=function(){clearTimeout(bak.t);bak.t=setTimeout(bak,300)};bak();if(!kelime)setTimeout(function(){i.focus()},60);
  sh.q('[data-ac]').onclick=function(){var w=i.value.trim(),d=son?son.d:szDiller(w)[0];kaydet();notKaydet(true);location.href='sozluk.html?dil='+d+'&q='+encodeURIComponent(w)}}
 function kelimeyeBak(p,cx,cy){if(!doc)return;kelimeAl(p,cx,cy).then(function(w){if(w)sozlukAc(w);else sozlukAc('','Bu noktada okunabilir metin yok (taranmış sayfa olabilir). Kelimeyi kendin yazarak arayabilirsin.')}).catch(function(){sozlukAc('','Metin okunamadı; kelimeyi yazarak arayabilirsin.')})}
 var PT={},st=null,iki=null,dokT=0,hareket=false,uzunT=0,uzunOldu=false;
 function nokta(ev,d){var r=d.getBoundingClientRect(),k=1000/r.width;return[Math.round((ev.clientX-r.left)*k*10)/10,Math.round((ev.clientY-r.top)*k*10)/10]}
 function ikiBasla(){var a=Object.keys(PT).map(function(k){return PT[k]});if(a.length<2)return;var mx=(a[0].x+a[1].x)/2,my=(a[0].y+a[1].y)/2,R=S.getBoundingClientRect();iki={d0:Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y)||1,mx:mx,my:my,z0:A.zoom,f:odak(mx-R.left,my-R.top),s:1,sx:S.scrollLeft,sy:S.scrollTop,ox:mx-R.left+S.scrollLeft,oy:my-R.top+S.scrollTop,dx:0,dy:0}}
 S.addEventListener('pointerdown',function(ev){PT[ev.pointerId]={x:ev.clientX,y:ev.clientY,t:ev.pointerType};hareket=false;
  if(Object.keys(PT).length===2&&ev.pointerType==='touch'){if(st)iptalCizgi();ikiBasla();return}
  var d=ev.target.closest&&ev.target.closest('.sy');uzunOldu=false;clearTimeout(uzunT);if(!d||!N)return;var kalem=ev.pointerType==='pen',m=mod==='el'&&kalem?'k':mod;
  if(m==='el'){var cx0=ev.clientX,cy0=ev.clientY,pp=+d.dataset.p;uzunT=setTimeout(function(){if(!hareket&&Object.keys(PT).length===1){uzunOldu=true;if(navigator.vibrate)navigator.vibrate(15);kelimeyeBak(pp,cx0,cy0)}},550);return}
  if(m==='sz'){st={t:'sz',p:+d.dataset.p,x:ev.clientX,y:ev.clientY};return}
  var p=+d.dataset.p;ev.preventDefault();
  if(m==='n'){st={t:'n',p:p,d:d,a:nokta(ev,d)};return}
  try{S.setPointerCapture(ev.pointerId)}catch(x){}
  var pt=nokta(ev,d);
  if(m==='s'){st={t:'s',p:p,d:d,id:ev.pointerId};silNokta(p,pt);return}
  st={t:m,r:A.renk[m]||RENK[m][0],w:KAL[m],d:pt.slice(),p:p,el:null,dv:d,id:ev.pointerId};st.el=cizgiEl(st);svgAl(p).appendChild(st.el)},{passive:false});
 S.addEventListener('pointermove',function(ev){var q=PT[ev.pointerId];if(!q)return;if(Math.abs(ev.clientX-q.x)+Math.abs(ev.clientY-q.y)>6){hareket=true;clearTimeout(uzunT)}q.x=ev.clientX;q.y=ev.clientY;
  if(iki){var a=Object.keys(PT).map(function(k){return PT[k]});if(a.length<2)return;var dd=Math.hypot(a[0].x-a[1].x,a[0].y-a[1].y),s=Math.max(.5/iki.z0,Math.min(4/iki.z0,dd/iki.d0)),mx=(a[0].x+a[1].x)/2,my=(a[0].y+a[1].y)/2;iki.s=s;iki.dx=mx-iki.mx;iki.dy=my-iki.my;
   IN.style.transformOrigin=iki.ox+'px '+iki.oy+'px';IN.style.transform='translate('+iki.dx+'px,'+iki.dy+'px) scale('+s+')';return}
  if(!st||st.t==='sz'||st.id!==ev.pointerId)return;var evs=ev.getCoalescedEvents?ev.getCoalescedEvents():[ev];if(!evs.length)evs=[ev];
  if(st.t==='s'){evs.forEach(function(x){silNokta(st.p,nokta(x,st.d))});return}
  evs.forEach(function(x){var pt=nokta(x,st.dv),L=st.d,lx=L[L.length-2],ly=L[L.length-1];if(Math.abs(pt[0]-lx)+Math.abs(pt[1]-ly)<1.5)return;if(st.t==='c'){st.d=[L[0],L[1],pt[0],pt[1]]}else{L.push(pt[0],pt[1])}});
  if(st.t==='c'){var L2=st.d;if(L2.length===4&&Math.abs(L2[3]-L2[1])<Math.abs(L2[2]-L2[0])*.25)L2[3]=L2[1]}
  st.el.setAttribute('d',yolD(st))});
 function iptalCizgi(){if(st&&st.el)st.el.remove();st=null}
 function bitir(ev){var q=PT[ev.pointerId];delete PT[ev.pointerId];clearTimeout(uzunT);if(uzunOldu){uzunOldu=false;dokT=Date.now();return}
  if(iki){if(Object.keys(PT).length<2){var I=iki;iki=null;IN.style.transform='';IN.style.transformOrigin='';var R=S.getBoundingClientRect();
    if(Math.abs(I.s-1)>.03){var f=I.f;f.mx=I.mx-R.left+I.dx;f.my=I.my-R.top+I.dy;yakinlas(I.z0*I.s,f)}else{S.scrollLeft=I.sx-I.dx;S.scrollTop=I.sy-I.dy}}
   dokT=Date.now();PT={};return}
  if(!st){if(ev.type==='pointerup'&&q&&!hareket&&mod==='el'&&Date.now()-dokT>350&&!(ev.target.closest&&ev.target.closest('.nt'))){dokT=Date.now();var R3=S.getBoundingClientRect(),fx=(ev.clientX-R3.left)/R3.width;
   if(sayfali()&&(fx<.28||fx>.72)){var ileri=A.duzen==='rtl'?fx<.5:fx>.5;git(Math.max(1,Math.min(n,su+(ileri?1:-1))))}else gizle(!bar.classList.contains('gz'))}return}
  if(st.t!=='n'&&st.id!==ev.pointerId)return;
  var s2=st;st=null;
  if(s2.t==='sz'){if(ev.type==='pointerup'&&!hareket)kelimeyeBak(s2.p,s2.x,s2.y);return}
  if(s2.t==='n'){if(ev.type==='pointerup'&&!hareket)notAc(s2.p,-1,{x:Math.round(s2.a[0]),y:Math.round(s2.a[1])});return}
  if(s2.t==='s')return;
  if(ev.type==='pointercancel'){if(s2.el)s2.el.remove();return}
  var L=s2.d;if(s2.t==='f'&&L.length>4){var y0=1e9,y1=-1e9;for(var i=1;i<L.length;i+=2){y0=Math.min(y0,L[i]);y1=Math.max(y1,L[i])}var x0=L[0],x1=L[L.length-2];if(y1-y0<26&&Math.abs(x1-x0)>30){var ym=(y0+y1)/2;s2.d=[Math.min(x0,x1),ym,Math.max(x0,x1),ym]}}
  if(s2.t==='k'&&L.length>8){var z=[L[0],L[1]];for(var j=2;j<L.length-2;j+=2){if(Math.hypot(L[j]-z[z.length-2],L[j+1]-z[z.length-1])>=2.2)z.push(L[j],L[j+1])}z.push(L[L.length-2],L[L.length-1]);s2.d=z}
  s2.d=s2.d.map(function(v){return Math.round(v*10)/10});
  var kay={t:s2.t,r:s2.r,w:s2.w,d:s2.d};(N.s[s2.p]=N.s[s2.p]||[]).push(kay);geriY.push({t:'s',op:'ekle',p:s2.p,o:kay});kirlet();sayfaNotCiz(s2.p)}
 S.addEventListener('pointerup',bitir);S.addEventListener('pointercancel',bitir);
 S.addEventListener('contextmenu',function(ev){ev.preventDefault()});
 function silNokta(p,pt){var L=N.s[p];if(!L||!L.length)return;for(var i=L.length-1;i>=0;i--){var s=L[i],d=s.d,es=s.w/2+14,vur=false;
   for(var j=0;j<d.length&&!vur;j+=2){var x1=d[j],y1=d[j+1],x2=d[j+2]!==undefined?d[j+2]:x1,y2=d[j+3]!==undefined?d[j+3]:y1,dx=x2-x1,dy=y2-y1,l=dx*dx+dy*dy,t=l?Math.max(0,Math.min(1,((pt[0]-x1)*dx+(pt[1]-y1)*dy)/l)):0;if(Math.hypot(pt[0]-(x1+t*dx),pt[1]-(y1+t*dy))<es)vur=true}
   if(vur){L.splice(i,1);geriY.push({t:'s',op:'sil',p:p,o:s});kirlet();sayfaNotCiz(p)}}}
 var icindekiler=null,araSon={q:'',r:[]};
 function panel(sek){var sh=pencere('<div class="kt-tb"><button data-t="ic">İçindekiler</button><button data-t="nt">Notlar ve çizimler</button><button data-t="yi">Yer imleri</button><button data-t="ar">Ara</button></div><div class="kt-pi"></div>');
  var PI=sh.q('.kt-pi');function sec(t){[].forEach.call(sh.el.querySelectorAll('.kt-tb button'),function(b){b.classList.toggle('on',b.dataset.t===t)});({ic:icG,nt:ntG,yi:yiG,ar:arG})[t]()}
  [].forEach.call(sh.el.querySelectorAll('.kt-tb button'),function(b){b.onclick=function(){sec(b.dataset.t)}});
  function gitK(p){sh.kapa();git(p)}
  function icG(){if(!doc){PI.innerHTML='';return}if(icindekiler===null){PI.innerHTML='<div class="kt-bos2">Yükleniyor…</div>';doc.getOutline().then(function(O){return O?cozum(O):[]}).then(function(O){icindekiler=O;icG()}).catch(function(){icindekiler=[];icG()});return}
   if(!icindekiler.length){PI.innerHTML='<div class="kt-bos2">Bu PDF’te içindekiler bilgisi yok.<br>Alttaki sayfa numarasına dokunarak istediğin sayfaya gidebilir, önemli yerlere 🔖 yer imi koyabilirsin.</div>';return}
   function ag(L){return'<ul class="kt-ic">'+L.map(function(x){return'<li><div data-p="'+(x.p||'')+'"><span>'+e(x.t)+'</span><small>'+(x.p||'')+'</small></div>'+(x.c&&x.c.length?ag(x.c):'')+'</li>'}).join('')+'</ul>'}
   PI.innerHTML=ag(icindekiler);[].forEach.call(PI.querySelectorAll('[data-p]'),function(d){d.onclick=function(){if(+d.dataset.p)gitK(+d.dataset.p)}})}
  function ntG(){var h='',say=0;for(var p=1;p<=n;p++){var M=N.n[p]||[],S2=N.s[p]||[];if(!M.length&&!S2.length)continue;M.forEach(function(x){say++;h+='<div class="kt-li" data-p="'+p+'"><i>s. '+p+'</i><span>📝 '+e(x.m)+'</span></div>'});if(S2.length){say++;var c={k:0,f:0,c:0};S2.forEach(function(x){c[x.t]++});h+='<div class="kt-li" data-p="'+p+'"><i>s. '+p+'</i><span>'+[c.f?'🖍️ '+c.f+' fosforlu':'',c.c?'〰️ '+c.c+' altı çizili':'',c.k?'✏️ '+c.k+' kalem':''].filter(Boolean).join(' · ')+'</span></div>'}}
   PI.innerHTML=(say?h+'<div class="bt"><button class="a" data-x>⬇ Notları dışa aktar (.txt)</button></div>':'<div class="kt-bos2">Henüz not ya da çizim yok.<br>🖊️ düğmesinden kalemi seçip sayfaya yazabilirsin.</div>');
   [].forEach.call(PI.querySelectorAll('[data-p]'),function(d){d.onclick=function(){gitK(+d.dataset.p)}});var x=PI.querySelector('[data-x]');if(x)x.onclick=disaAktar}
  function yiG(){PI.innerHTML=N.y.length?N.y.map(function(p){return'<div class="kt-li" data-p="'+p+'"><i>🔖</i><span>Sayfa '+p+'</span></div>'}).join(''):'<div class="kt-bos2">Yer imi yok. Okurken üstteki 🔖 düğmesi o sayfayı buraya ekler.</div>';[].forEach.call(PI.querySelectorAll('[data-p]'),function(d){d.onclick=function(){gitK(+d.dataset.p)}})}
  function arG(){PI.innerHTML='<input type="search" placeholder="Kitapta ara, Enter’a bas (metinli PDF’lerde)…" value="'+e(araSon.q)+'"><div class="kt-ard" style="margin-top:8px"></div>';var i=PI.querySelector('input'),R=PI.querySelector('.kt-ard');
   function goster2(){R.innerHTML=araSon.r.length?araSon.r.map(function(x){return'<div class="kt-li" data-p="'+x.p+'"><i>s. '+x.p+'</i><span>'+x.h+'</span></div>'}).join(''):(araSon.q?'<div class="kt-bos2">Sonuç yok. (Taranmış/resim PDF’lerde metin araması yapılamaz.)</div>':'');[].forEach.call(R.querySelectorAll('[data-p]'),function(d){d.onclick=function(){gitK(+d.dataset.p)}})}
   goster2();i.onkeydown=function(ev){if(ev.key==='Enter'){ev.preventDefault();ara(i.value,R,goster2)}};setTimeout(function(){i.focus()},50)}
  sec(sek)}
 function nz(s){return String(s).toLocaleLowerCase('tr').replace(/[ً-ٰٟـ]/g,'').replace(/[أإآٱ]/g,'ا').replace(/ى/g,'ي').replace(/\s+/g,' ')}
 var araSay=0;function ara(q,R,bitince){q=q.trim();araSon={q:q,r:[]};if(q.length<2||!doc){bitince();return}var nq=nz(q),my=++araSay,p=1;R.innerHTML='<div class="kt-bos2">Aranıyor… <span>0</span>/'+n+'</div>';
  (function dongu(){if(my!==araSay||bitti)return;if(p>n||araSon.r.length>=300){bitince();return}var pp=p++;doc.getPage(pp).then(function(pg){return pg.getTextContent()}).then(function(tc){var t=tc.items.map(function(x){return x.str}).join(' '),nt=nz(t),i=nt.indexOf(nq);if(i>-1){var a=Math.max(0,i-40);araSon.r.push({p:pp,h:e(nt.slice(a,i))+'<mark>'+e(nt.substr(i,nq.length))+'</mark>'+e(nt.slice(i+nq.length,i+nq.length+60))})}var sp=R.querySelector('span');if(sp)sp.textContent=pp}).catch(function(){}).then(function(){if(pp%8===0)setTimeout(dongu,0);else dongu()})})()}
 function cozum(O){return Promise.all(O.map(function(x){var dp=typeof x.dest==='string'?doc.getDestination(x.dest):Promise.resolve(x.dest);return dp.then(function(d){return d&&d[0]!=null?(typeof d[0]==='number'?d[0]+1:doc.getPageIndex(d[0]).then(function(i){return i+1})):null}).catch(function(){return null}).then(function(p){return(x.items&&x.items.length?cozum(x.items):Promise.resolve([])).then(function(c){return{t:x.title,p:p,c:c}})})}))}
 function disaAktar(){var L=['“'+K.ad+'” — notlarım ve işaretlerim','('+new Date().toLocaleDateString('tr-TR')+', el-Mihrâb okuma alanı)',''];for(var p=1;p<=n;p++){var M=N.n[p]||[],S2=N.s[p]||[];if(!M.length&&!S2.length&&N.y.indexOf(p)<0)continue;L.push('— Sayfa '+p+(N.y.indexOf(p)>-1?' 🔖':'')+(S2.length?' · '+S2.length+' çizim/işaret':''));M.forEach(function(x){L.push('   • '+x.m.replace(/\n/g,'\n     '))});L.push('')}
  var b=new Blob([L.join('\n')],{type:'text/plain;charset=utf-8'}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=K.ad.replace(/[\\\/:*?"<>|]+/g,' ').slice(0,80)+' - notlar.txt';document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},1500)}
 function sifreSor(yanlis){return new Promise(function(ok){var sh=pencere('<h3>🔒 Şifreli PDF</h3><p style="margin:0 0 8px">'+(yanlis?'Şifre yanlış, tekrar dene.':'Bu kitap şifreyle korunuyor. Şifresini yaz:')+'</p><input type="password" autocomplete="off"><div class="bt"><button data-x>Vazgeç</button><button class="a" data-t>Aç</button></div>');var i=sh.q('input');setTimeout(function(){i.focus()},50);sh.q('[data-x]').onclick=function(){sh.kapa();ok(null)};sh.q('[data-t]').onclick=function(){sh.kapa();ok(i.value)};i.onkeydown=function(ev){if(ev.key==='Enter'){sh.kapa();ok(i.value)}}})}
 Promise.all([al(id),notAl(id),pdfjs()]).then(function(r){var k=r[0];if(!k)throw new Error('Kitap bulunamadı');K=k;N=r[1];P=r[2];bar.querySelector('b').textContent=k.ad;var b=veriBlob(k);if(!b)throw new Error('Kitabın dosyası bulunamadı; silip yeniden yükle');
  Y.textContent='Kitap açılıyor… ('+boyut(k.boyut||b.size)+')';return belgeAc(P,b,sifreSor)}).then(function(d){if(bitti){yoket(d);return}doc=d;n=d.numPages;rng.max=n;
  return d.getPage(1).then(function(p){var v=p.getViewport({scale:1}),r=v.height/v.width;for(var i=0;i<n;i++)oran.push(r);
   var h='';for(i=1;i<=n;i++)h+='<div class="sy" data-p="'+i+'"><span class="pn">'+i+'</span><svg xmlns="'+SVGNS+'" viewBox="0 0 1000 '+Math.round(1000*r)+'" preserveAspectRatio="none"></svg><span class="yi"></span></div>';IN.innerHTML=h;IN.dir=A.duzen==='rtl'?'rtl':'ltr';Y.remove();anaW=S.clientWidth;yerlestir();
   for(i=1;i<=n;i++)if((N.s[i]&&N.s[i].length)||(N.n[i]&&N.n[i].length))sayfaNotCiz(i);yerImiCiz();
   if(K.toplam!==n)K.toplam=n;
   gozlem();
   var bp=Math.min(Math.max(1,K.sayfa||1),n);bas=bp;enCok=bp;git(bp);if(bp>1)tost('Kaldığın yer: sayfa '+bp);setTimeout(function(){if(!bitti&&!AR.classList.contains('ac'))gizle(true)},2500)})})
 .catch(function(x){console.error(x);if(bitti)return;if(x&&x.iptal){kapat();return}
  Y.innerHTML='<div style="font-size:40px">📕</div><b>Bu PDF okuyucuda açılamadı.</b><small style="opacity:.8;max-width:420px">'+e(hataMetni(x))+'</small><div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center"><button data-tt>Tekrar dene</button><button data-dis>Telefonun PDF uygulamasında aç</button><button data-gg>Geri</button></div>';
  Y.querySelector('[data-gg]').onclick=function(){kapat()};Y.querySelector('[data-tt]').onclick=function(){kapat();setTimeout(function(){oku(id,o,kapaninca)},300)};
  Y.querySelector('[data-dis]').onclick=function(){var b=K&&veriBlob(K);if(!b)return;var u=URL.createObjectURL(b.type==='application/pdf'?b:new Blob([b],{type:'application/pdf'})),a=document.createElement('a');a.href=u;a.target='_blank';a.rel='noopener';if(/Android|iPhone|iPad/i.test(navigator.userAgent))a.download=(K.ad||'kitap')+'.pdf';document.body.appendChild(a);a.click();setTimeout(function(){a.remove()},1000)}})}

window.Kitaplik={goster:goster,oku:oku};
})();
