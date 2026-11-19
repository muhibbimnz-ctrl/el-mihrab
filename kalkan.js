/* el-Mihrâb kalkanı — her sayfada ilk yüklenen küçük koruma betiği.
   1) İnternet isteği sonsuza kadar beklemez (25 sn sonra bırakılır).
   2) Gizli sekme / dolu hafıza yüzünden localStorage çalışmazsa sayfa çökmez (geçici hafıza kullanılır).
   3) Sayfa açılırken bozulursa (boş ekran) "Onar" düğmesi çıkar; bozuk önbellek temizlenir, veriler korunur.
   4) Adrese ?onar yazılırsa aynı onarım kendiliğinden yapılır.
   5) Tarayıcıdan, indirilen Kur'an ve ders verisini silmemesi istenir.
   Bu dosya hiçbir koşulda hata fırlatmamalıdır; her şey try içindedir. */
(function(){
  'use strict';
  var W=window;

  /* 2) localStorage yedeği */
  try{var k='__mh';W.localStorage.setItem(k,'1');W.localStorage.removeItem(k)}catch(e){
    try{
      var M={};var mem={getItem:function(x){return Object.prototype.hasOwnProperty.call(M,x)?M[x]:null},
        setItem:function(x,v){M[x]=String(v)},removeItem:function(x){delete M[x]},clear:function(){M={}},
        key:function(i){return Object.keys(M)[i]||null},get length(){return Object.keys(M).length}};
      Object.defineProperty(W,'localStorage',{value:mem,configurable:true});
    }catch(x){}
  }

  /* 1) Zaman aşımı olan fetch */
  try{
    var F=W.fetch;
    if(F&&typeof AbortController==='function'){
      W.fetch=function(u,o){
        o=o||{};
        if(o.signal)return F.call(this,u,o);
        var c=new AbortController(),t=setTimeout(function(){try{c.abort()}catch(e){}},25000);
        var o2={};for(var p in o)o2[p]=o[p];o2.signal=c.signal;
        return F.call(this,u,o2).then(function(r){clearTimeout(t);return r},function(e){clearTimeout(t);throw e});
      };
    }
  }catch(e){}

  /* 3–4) Onarım */
  function onar(){
    var isler=[];
    try{if(navigator.serviceWorker&&navigator.serviceWorker.getRegistrations)
      isler.push(navigator.serviceWorker.getRegistrations().then(function(rs){return Promise.all(rs.map(function(r){return r.unregister()}))}))}catch(e){}
    try{if(W.caches)isler.push(caches.keys().then(function(ks){
      /* Uygulama kabuğu silinir; indirilmiş Kur'an/ders verisi (mihrab-data-*) korunur */
      return Promise.all(ks.filter(function(x){return x.indexOf('mihrab-v')===0}).map(function(x){return caches.delete(x)}))}))}catch(e){}
    var git=function(){try{var u=location.pathname+location.hash;location.replace(u)}catch(e){location.reload()}};
    Promise.all(isler).then(git,git);setTimeout(git,4000);
  }
  W.mihrabOnar=onar;
  try{if(/[?&]onar\b/.test(location.search)){onar();return}}catch(e){}

  var hatalar=0,ilk=Date.now();
  function kaydet(m){try{hatalar++;W.localStorage.setItem('mihrab.sonhata',JSON.stringify({t:new Date().toISOString(),s:location.pathname,m:String(m).slice(0,300)}))}catch(e){}}
  W.addEventListener('error',function(e){
    try{if(e&&e.target&&e.target!==W&&e.target.tagName)return; /* resim/ses yüklenemedi: önemsiz */
      kaydet((e&&e.message)||'hata')}catch(x){}
  },true);
  W.addEventListener('unhandledrejection',function(e){try{var r=e&&e.reason;
    if(r&&(r.name==='AbortError'))return; kaydet((r&&r.message)||r||'promise')}catch(x){}});

  function bosMu(){
    try{var b=document.body;if(!b)return true;
      var t=(b.innerText||'').replace(/\s+/g,'');return t.length<40}catch(e){return false}
  }
  function bar(){
    try{if(document.getElementById('mhOnar'))return;
      var d=document.createElement('div');d.id='mhOnar';d.setAttribute('role','alert');
      d.style.cssText='position:fixed;left:12px;right:12px;bottom:16px;z-index:2147483647;background:#1f2937;color:#fff;padding:14px 16px;border-radius:14px;font:15px/1.4 system-ui,sans-serif;box-shadow:0 6px 24px rgba(0,0,0,.3);display:flex;gap:10px;align-items:center;flex-wrap:wrap';
      d.innerHTML='<span style="flex:1;min-width:180px">Sayfa düzgün açılmadı. Onarmak indirdiğiniz verileri silmez.</span>';
      var a=document.createElement('button');a.textContent='Onar';a.style.cssText='background:#10b981;color:#fff;border:0;border-radius:10px;padding:9px 18px;font:600 15px system-ui,sans-serif';
      a.onclick=onar;
      var y=document.createElement('button');y.textContent='Yenile';y.style.cssText='background:transparent;color:#fff;border:1px solid #6b7280;border-radius:10px;padding:8px 14px;font:15px system-ui,sans-serif';
      y.onclick=function(){location.reload()};
      d.appendChild(a);d.appendChild(y);document.body.appendChild(d);
    }catch(e){}
  }
  /* Açılıştan birkaç saniye sonra ekran boşsa ve hata olduysa (ya da tamamen boşsa) onarım öner */
  W.addEventListener('load',function(){
    setTimeout(function(){try{if(bosMu()&&(hatalar>0||Date.now()-ilk>6000))bar()}catch(e){}},5000);
  });

  /* 5) Kalıcı depolama isteği (Android Chrome genelde sessizce kabul eder) */
  try{if(navigator.storage&&navigator.storage.persist&&!W.localStorage.getItem('mihrab.persist')){
    navigator.storage.persisted().then(function(p){if(p)return true;return navigator.storage.persist()})
      .then(function(){try{W.localStorage.setItem('mihrab.persist','1')}catch(e){}},function(){});
  }}catch(e){}

  /* 8) Bilgisayar ekranı: telefona göre 760 px'lik dar sütunla yazılmış sayfalar geniş ekranda genişler, kartlar çoğalır */
  try{
    var gs=document.createElement('style');
    gs.textContent='@media (min-width:1100px){html.genis main{max-width:1060px!important}'+
      'html.genis body.mdLanding #modes{grid-template-columns:repeat(4,1fr)!important}'+
      'html.genis .tiles{grid-template-columns:repeat(3,1fr)!important}}';
    (document.head||document.documentElement).appendChild(gs);
    var gk=function(){try{var m=document.querySelector('main');if(m&&getComputedStyle(m).maxWidth==='760px')document.documentElement.classList.add('genis')}catch(e){}};
    if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',gk);else gk();
  }catch(e){}

  /* 9) Geri tuşu (adresi değişmeden ekran değiştiren sayfalar): ekran değişince geçmişe bir adım yazılır;
        telefonun geri tuşuna basılınca sayfanın kendi "‹ … / ← Geri" düğmesine basılır, sayfadan çıkılmaz */
  try{if(/\/(almanca|fransizca|ispanyolca|siyer|fikih|hadis)(\.html)?$/.test(location.pathname)){
    var derin=0,ici=false;
    var ozet=function(){var m=document.querySelector('main')||document.body;return m?(m.innerText||'').slice(0,300):''};
    var yer=function(){return location.pathname+location.search};
    var gorunur=function(x){var r=x.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(x).visibility!=='hidden'};
    var geriBul=function(){var L=[].slice.call(document.querySelectorAll('button,a,[role=button]')).filter(gorunur),i,t;
      for(i=0;i<L.length;i++){t=(L[i].innerText||'').trim();if(/^(‹|←)/.test(t)&&!/Önceki|el-Mihr/i.test(t))return L[i]}
      for(i=0;i<L.length;i++){if(L[i].matches('[aria-pressed="true"],[aria-selected="true"],.on,.sec,.aktif')&&L[i].closest('nav,header,.sekme,.tabs,.sek,[role=tablist]'))return L[i]}
      return null};
    document.addEventListener('click',function(e){try{if(ici)return;var a=e.target.closest&&e.target.closest('a');
      if(a&&a.getAttribute('href')&&!/^#/.test(a.getAttribute('href')))return;if(e.target.closest&&e.target.closest('input,select,textarea'))return;
      var once=ozet(),y=yer();setTimeout(function(){try{if(yer()!==y||ozet()===once)return;derin++;history.pushState({mhg:derin},'',location.href)}catch(x){}},400)}catch(x){}},true);
    W.addEventListener('popstate',function(){try{if(derin<=0)return;derin--;var b=geriBul();if(!b)return;
      if(b.tagName==='A'&&!b.onclick&&b.getAttribute('href')&&!/^#/.test(b.getAttribute('href')))return;
      ici=true;b.click();setTimeout(function(){ici=false},600)}catch(x){ici=false}});
  }}catch(e){}

  /* 7) Uygulamanın bir bölümünü açan kişi, ana sayfaya dönünce tanıtım sayfasına yönlendirilmez */
  try{if(!/\/(index(\.html)?)?$/.test(location.pathname)&&!/tanitim/.test(location.pathname))W.localStorage.setItem('mihrab.tanitim','1')}catch(e){}

  /* 6) Sayfadan çıkınca sesli okuma durur (Android'de başka sayfaya geçince ses devam edebiliyordu) */
  try{W.addEventListener('pagehide',function(){try{if(W.speechSynthesis)W.speechSynthesis.cancel()}catch(e){}})}catch(e){}
})();
