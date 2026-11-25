/* Çocuk Köşesi · Arapça ve İngilizce (5–12 yaş). İçerik: data/cocuk/dil.json (tools/cocuk/dil_veri.py üretir).
   Yollar: #ar, #en (ünite listesi) · #ar/<ünite> (kartlar) · #ar/<ünite>/dinle · #ar/<ünite>/eslestir · #ar/<ünite>/yaz
   cocuk.html’deki ortak işlevleri kullanır: sayfa, esc, bitti, S, toast, durdur, karis, $. */
(function(){
 var D=null,yuk=null,SEV=[[1,'5–7 yaş','Minikler','🧸'],[2,'8–10 yaş','Çocuklar','🎈'],[3,'11–12 yaş','Büyükler','🚀']];
 var css='.dk-sev{display:flex;gap:8px;margin:0 0 14px}.dk-sev button{flex:1;border:2px solid var(--line);background:var(--card);border-radius:16px;padding:10px 4px;font-weight:700;font-size:14px;font-family:inherit;color:var(--ink);cursor:pointer}.dk-sev button.on{border-color:var(--pri);background:var(--priS)}'+
  '.dk-kart{background:var(--card);border:2px solid var(--line);border-radius:28px;padding:22px 16px;text-align:center;margin:8px 0 12px;box-shadow:0 8px 22px -14px rgba(0,0,0,.35)}'+
  '.dk-kart .em{font-size:84px;line-height:1.1}.dk-kart .yb{font-size:44px;font-weight:800;margin:10px 0 2px;line-height:1.3;word-break:break-word}.dk-kart .yb[dir=rtl]{font-family:Amiri,"Noto Naskh Arabic",serif;font-size:52px;font-weight:700}'+
  '.dk-kart .yb.ornek{font-size:30px;color:var(--pri)}.dk-kart .yb.ornek[dir=rtl]{font-size:38px}.dk-kart .okn{display:block;text-align:center;font-size:18px;color:var(--pri);font-weight:700}.dk-kart .tr{font-size:22px;margin-top:6px}.dk-kart.cumle .yb{font-size:30px}.dk-kart.cumle .yb[dir=rtl]{font-size:36px}'+
  '.dk-nok{display:flex;justify-content:center;gap:5px;flex-wrap:wrap;margin:6px 0 12px}.dk-nok i{width:9px;height:9px;border-radius:50%;background:var(--line)}.dk-nok i.on{background:var(--pri)}'+
  '.dk-dug{display:grid;grid-template-columns:1fr 1.4fr 1fr;gap:8px}.dk-dug .btn{min-height:54px;font-size:17px}'+
  '.dk-akt{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:14px 0}.dk-akt button{border:0;border-radius:20px;padding:14px 10px;color:#fff;font-weight:800;font-size:16px;font-family:inherit;cursor:pointer;min-height:84px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}.dk-akt button span{font-size:30px}'+
  '.dk-sec{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}.dk-sec button{border:3px solid var(--line);background:var(--card);border-radius:22px;padding:12px 6px;min-height:96px;cursor:pointer;font-size:52px;color:var(--ink)}'+
  '.dk-sec button.yazi{font-size:19px;font-weight:700;min-height:72px}.dk-sec button.yazi[dir=rtl]{font-family:Amiri,serif;font-size:28px}.dk-sec button.dogru{border-color:var(--ok);background:var(--okS)}.dk-sec button.yanlis{border-color:var(--bad);background:var(--badS)}'+
  '.dk-ust{display:flex;justify-content:space-between;align-items:center;font-weight:800;color:var(--muted);margin:6px 2px}.dk-bar{height:10px;border-radius:6px;background:var(--line);overflow:hidden;margin-bottom:10px}.dk-bar i{display:block;height:100%;background:var(--pri);transition:width .3s}'+
  '.dk-buyuk{display:block;width:100%;margin:12px auto;font-size:22px;min-height:64px}'+
  '.dk-es{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}.dk-es button{aspect-ratio:1;border:0;border-radius:18px;background:var(--pri);color:#fff;font-size:30px;cursor:pointer;padding:4px;transition:transform .15s}'+
  '.dk-es button.ac{background:var(--card);color:var(--ink);border:3px solid var(--line)}.dk-es button.ac.yazi{font-size:16px;font-weight:800}.dk-es button.ac.yazi[dir=rtl]{font-family:Amiri,serif;font-size:22px}.dk-es button.tamam{border-color:var(--ok);background:var(--okS);visibility:visible}'+
  '.dk-yaz{font-size:46px;font-weight:800;letter-spacing:6px;margin:14px 0;text-align:center}.dk-yaz u{color:var(--pri);text-decoration:none;border-bottom:4px solid var(--pri);padding:0 6px}';
 function stil(){if(document.getElementById('dk-stil'))return;var s=document.createElement('style');s.id='dk-stil';s.textContent=css;document.head.appendChild(s)}
 function yukle(){if(D)return Promise.resolve(D);if(yuk)return yuk;
  yuk=fetch('data/cocuk/dil.json?v=2').then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(j){D=j;return j}).catch(function(e){yuk=null;throw e});return yuk}
 /* ——— Ses: telefonun okuma motoru; dil sesi yoksa uyarır, kilitlenmeye karşı bekçi süresi var ——— */
 var uyardi={};
 function sesBul(dil){var l=dil.slice(0,2),V=[];try{V=speechSynthesis.getVoices()||[]}catch(e){}
  for(var i=0;i<V.length;i++){var x=(V[i].lang||'').toLowerCase().replace('_','-');if(x.indexOf(dil.toLowerCase())===0)return V[i]}
  for(i=0;i<V.length;i++)if((V[i].lang||'').toLowerCase().indexOf(l)===0)return V[i];return null}
 function soyle(metin,dil,yavas,bitince){try{durdur()}catch(e){}
  if(!window.speechSynthesis||!window.SpeechSynthesisUtterance){if(!uyardi.yok){uyardi.yok=1;toast('Bu cihazda sesli okuma yok; okunuşu yazıdan takip et.')}bitince&&bitince();return}
  var L=[].concat(metin),i=0,bitti=false;
  function son(){if(bitti)return;bitti=true;bitince&&bitince()}
  function sira(){if(i>=L.length)return son();var u=new SpeechSynthesisUtterance(L[i++]),v=sesBul(dil);u.lang=dil;if(v)u.voice=v;
   else if(!uyardi[dil]){uyardi[dil]=1;toast(dil.indexOf('ar')===0?'Arapça ses bulunamadı; telefon ayarlarından Arapça metin okuma sesini indirebilirsin.':'İngilizce ses bulunamadı; telefon ayarlarından indirebilirsin.')}
   u.rate=yavas?.65:(dil.indexOf('ar')===0?.8:.85);u.pitch=1.05;
   var bekci=setTimeout(sira,Math.max(2500,String(u.text).length*180));
   u.onend=u.onerror=function(){clearTimeout(bekci);setTimeout(sira,200)};
   try{speechSynthesis.speak(u)}catch(e){clearTimeout(bekci);son()}}
  try{speechSynthesis.cancel()}catch(e){}setTimeout(sira,60)}
 function kartSes(L,k){var d=D[L].dil;if(k.length>4)return soyle([k[4],k[5]],d,true);soyle(k[1],d,false)}
 function sev(){var s=0;try{s=+localStorage.getItem('cocuk.dilSev')||0}catch(e){}return s||null}
 function sevYaz(s){try{localStorage.setItem('cocuk.dilSev',s)}catch(e){}}
 function yildiz(L,u,akt){return S.ok['dil.'+L+'.'+u+'.'+akt]?'⭐':''}
 function uniteBul(L,id){return D[L].uniteler.filter(function(u){return u.id===id})[0]}

 /* ——— Ünite listesi ——— */
 function liste(L){var X=D[L],s=sev(),h='<h1>'+(L==='ar'?'🕌 ':'🌍 ')+esc(X.ad)+'</h1><p class="lead">Yaşını seç; sana uygun dersler önce gelsin. Her derste kartları dinle, sonra oyunlarla yıldız topla.</p>'+
   '<div class="dk-sev">'+SEV.map(function(x){return'<button data-sev="'+x[0]+'"'+(s===x[0]?' class="on"':'')+'>'+x[3]+' '+x[1]+'</button>'}).join('')+'</div><div class="list">';
  var U=X.uniteler.map(function(u,i){u._i=i;return u});U.sort(function(a,b){return(s?(a.sev===s?0:1)-(b.sev===s?0:1):0)||a.sev-b.sev||a._i-b._i});var son=null;
  U.forEach(function(u){var g=SEV[u.sev-1];if(g[0]!==son){h+='<div class="grp">'+g[3]+' '+g[2]+' · '+g[1]+'</div>';son=g[0]}
   var y=['ogren','dinle','eslestir','yaz'].filter(function(a){return S.ok['dil.'+L+'.'+u.id+'.'+a]}).length;
   h+='<button class="it" data-h="'+L+'/'+u.id+'"><span class="e"'+(L==='ar'&&u.harf?' style="font-family:Amiri,serif;font-size:34px"':'')+'>'+esc(u.e)+'</span><span class="tx"><b>'+esc(u.ad)+'</b><small>'+u.k.length+' kelime</small></span><span class="ok">'+(y?'⭐'.repeat(Math.min(y,3)):'')+'</span></button>'});
  sayfa(X.ad,h+'</div><footer>Anne-babalar için: Sesler telefonun metin okuma motoruyla çalınır. Ses gelmiyorsa telefon ayarlarından '+(L==='ar'?'Arapça':'İngilizce')+' metin okuma sesini indirin. Okunuşlar Türkçe harflerle yaklaşık olarak yazılmıştır.</footer>','#');
  [].forEach.call(document.querySelectorAll('[data-sev]'),function(b){b.onclick=function(){sevYaz(+b.dataset.sev);liste(L)}});
  [].forEach.call(document.querySelectorAll('[data-h]'),function(b){b.onclick=function(){location.hash=b.dataset.h}})}

 /* ——— Ünite sayfası: etkinlik seçimi ——— */
 function unite(L,u){var A=[['ogren','📖','Kartları öğren','#1f8a70'],['dinle','👂','Dinle ve bul','#3a86ff'],['eslestir','🧩','Eşleştir','#ef476f']];
  if(L==='en'&&u.sev>=2&&!/cumle/.test(u.id))A.push(['yaz','✍️','Harfi tamamla','#fb8500']);
  if(L==='ar'&&u.sev>=2)A.push(['yaz','✍️','Doğru yazılış','#fb8500']);
  sayfa(u.ad,'<h1>'+esc(u.e)+' '+esc(u.ad)+'</h1><p class="lead">'+SEV[u.sev-1][1]+' · '+u.k.length+' kelime. Önce kartları dinle, sonra oyunları oyna; her oyunda en az %75 doğru yaparsan yıldız kazanırsın.</p>'+
   '<div class="dk-akt">'+A.map(function(a){return'<button style="background:'+a[3]+'" data-h="'+L+'/'+u.id+'/'+a[0]+'"><span>'+a[1]+'</span>'+a[2]+' '+yildiz(L,u.id,a[0])+'</button>'}).join('')+'</div>'+
   '<div class="list">'+u.k.map(function(k,i){return'<button class="it" data-i="'+i+'"><span class="e">'+k[0]+'</span><span class="tx"><b'+(D[L].yon==='rtl'?' dir="rtl" style="font-family:Amiri,serif;font-size:24px;text-align:right"':'')+'>'+esc(k[1])+'</b><small>'+esc(k[3])+' · '+esc(k[2])+'</small></span><span class="ok">🔊</span></button>'}).join('')+'</div>','#'+L);
  [].forEach.call(document.querySelectorAll('[data-h]'),function(b){b.onclick=function(){location.hash=b.dataset.h}});
  [].forEach.call(document.querySelectorAll('[data-i]'),function(b){b.onclick=function(){kartSes(L,u.k[+b.dataset.i])}})}

 /* ——— Kartlar ——— */
 function ogren(L,u){var i=0,K=u.k,rtl=D[L].yon==='rtl',gor={};
  function ciz(){var k=K[i];gor[i]=1;
   $('#m').innerHTML='<div class="dk-ust"><span>'+esc(u.ad)+'</span><span>'+(i+1)+' / '+K.length+'</span></div>'+
    '<div class="dk-kart'+(/cumle/.test(u.id)?' cumle':'')+'"><div class="em">'+k[0]+'</div><div class="yb"'+(rtl?' dir="rtl" lang="ar"':' lang="en"')+'>'+esc(k[1])+'</div>'+(k.length>4?'<div class="yb ornek"'+(rtl?' dir="rtl" lang="ar"':' lang="en"')+'>'+esc(k[5])+'</div>':'')+'<div class="okn">'+esc(k[3])+'</div><div class="tr">'+esc(k[2])+'</div></div>'+
    '<div class="dk-nok">'+K.map(function(x,j){return'<i'+(j===i?' class="on"':'')+'></i>'}).join('')+'</div>'+
    '<div class="dk-dug"><button class="btn" id="dkO"'+(i?'':' disabled')+'>‹</button><button class="btn pri" id="dkS">🔊 Dinle</button><button class="btn" id="dkN">'+(i+1<K.length?'›':'✓')+'</button></div>'+
    '<button class="btn" id="dkY" style="width:100%;margin-top:8px">🐢 Yavaş dinle</button>';
   $('#dkS').onclick=function(){kartSes(L,k)};$('#dkY').onclick=function(){soyle(k.length>4?[k[4],k[5]]:k[1],D[L].dil,true)};
   $('#dkO').onclick=function(){if(i){i--;ciz()}};
   $('#dkN').onclick=function(){if(i+1<K.length){i++;ciz()}else{if(Object.keys(gor).length>=K.length&&bitti('dil.'+L+'.'+u.id+'.ogren',1))toast('Bütün kartları gördün! ⭐');location.hash=L+'/'+u.id}};
   kartSes(L,k)}
  sayfa(u.ad,'','#'+L+'/'+u.id);ciz()}

 /* ——— Dinle ve bul ——— */
 function dinle(L,u){var K=u.k,N=Math.min(8,K.length),Q=karis(K).slice(0,N),i=0,dogru=0,metin=/cumle|selam/.test(u.id)||u.sev===3;
  function ciz(){if(i>=N)return sonuc();var k=Q[i],sec=karis([k].concat(karis(K.filter(function(x){return x!==k})).slice(0,3))),ilk=true;
   $('#m').innerHTML='<div class="dk-ust"><span>👂 Dinle ve bul</span><span>'+(i+1)+' / '+N+'</span></div><div class="dk-bar"><i style="width:'+(100*i/N)+'%"></i></div>'+
    '<button class="btn pri dk-buyuk" id="dkC">🔊 Tekrar dinle</button><p class="lead" style="text-align:center">Duyduğun '+(metin?'sözün anlamını':'şeyi')+' bul!</p>'+
    '<div class="dk-sec">'+sec.map(function(x,j){return'<button data-j="'+j+'"'+(metin?' class="yazi"':'')+'>'+(metin?x[0]+' '+esc(x[2]):x[0])+'</button>'}).join('')+'</div>';
   $('#dkC').onclick=function(){kartSes(L,k)};kartSes(L,k);
   [].forEach.call(document.querySelectorAll('[data-j]'),function(b){b.onclick=function(){var x=sec[+b.dataset.j];
     if(x===k){b.classList.add('dogru');if(ilk)dogru++;try{navigator.vibrate&&navigator.vibrate(20)}catch(e){}
      [].forEach.call(document.querySelectorAll('[data-j]'),function(c){c.disabled=true});setTimeout(function(){i++;ciz()},900)}
     else{b.classList.add('yanlis');ilk=false;b.disabled=true;toast(x[2]+' değil, bir daha dinle!')}}})}
  function sonuc(){sonucGoster(L,u,'dinle',dogru,N,function(){dinle(L,u)})}
  sayfa('Dinle ve bul','','#'+L+'/'+u.id);ciz()}

 /* ——— Eşleştirme (hafıza) ——— */
 function eslestir(L,u){var P=karis(u.k).slice(0,6),C=[];
  P.forEach(function(k,j){C.push({j:j,t:'e',v:k[0]});C.push({j:j,t:'y',v:k[1]})});C=karis(C);
  sayfa('Eşleştir','<div class="dk-ust"><span>🧩 Resmi ve kelimeyi eşleştir</span><span id="dkH">0 hamle</span></div><div class="dk-es">'+C.map(function(c,n){return'<button data-n="'+n+'">❓</button>'}).join('')+'</div>','#'+L+'/'+u.id);
  eslestirBagla(L,u,P,C)}
 function eslestirBagla(L,u,P,C){/* sayfa() içeriği yeniden yazdığı için olayları yeniden bağla */
  var acik=[],bulunan=0,hamle=0,kilit=false,rtl=D[L].yon==='rtl';
  [].forEach.call(document.querySelectorAll('.dk-es button'),function(b){b.onclick=function(){if(kilit||b.classList.contains('ac'))return;var c=C[+b.dataset.n];
    b.classList.add('ac');if(c.t==='y'){b.classList.add('yazi');if(rtl)b.setAttribute('dir','rtl');kartSes(L,P[c.j])}b.textContent=c.v;acik.push(b);
    if(acik.length<2)return;hamle++;var h=document.getElementById('dkH');if(h)h.textContent=hamle+' hamle';var a=C[+acik[0].dataset.n],z=C[+acik[1].dataset.n];
    if(a.j===z.j&&a.t!==z.t){acik.forEach(function(x){x.classList.add('tamam')});acik=[];bulunan++;
     if(bulunan===P.length)setTimeout(function(){var puan=hamle<=P.length+4?P.length:Math.max(0,P.length-(hamle-P.length-4));sonucGoster(L,u,'eslestir',puan,P.length,function(){eslestir(L,u)},hamle)},700)}
    else{kilit=true;setTimeout(function(){acik.forEach(function(x){x.classList.remove('ac','yazi');x.removeAttribute('dir');x.textContent='❓'});acik=[];kilit=false},900)}}})}

 /* ——— Yazma: İngilizce eksik harf · Arapça doğru yazılış ——— */
 function yaz(L,u){var K=u.k.filter(function(k){return L==='ar'||/^[a-z]{3,}$/i.test(k[1])}),N=Math.min(8,K.length),Q=karis(K).slice(0,N),i=0,dogru=0;
  if(!N)return unite(L,u);
  function ciz(){if(i>=N)return sonucGoster(L,u,'yaz',dogru,N,function(){yaz(L,u)});var k=Q[i],ilk=true,sec,soru;
   if(L==='en'){var w=k[1],p=1+Math.floor(Math.random()*(w.length-1)),h=w[p].toLowerCase(),harf='abcdefghijklmnoprstuvwy'.split('').filter(function(x){return x!==h});
     sec=karis([h].concat(karis(harf).slice(0,3)));soru='<div class="dk-yaz" lang="en">'+esc(w.slice(0,p))+'<u>?</u>'+esc(w.slice(p+1))+'</div>';
     k._c=h}
   else{var y=karis(K.filter(function(x){return x!==k})).slice(0,3).map(function(x){return x[1]});sec=karis([k[1]].concat(y));soru='';k._c=k[1]}
   $('#m').innerHTML='<div class="dk-ust"><span>✍️ '+(L==='en'?'Eksik harfi bul':'Doğru yazılışı seç')+'</span><span>'+(i+1)+' / '+N+'</span></div><div class="dk-bar"><i style="width:'+(100*i/N)+'%"></i></div>'+
    '<div class="dk-kart" style="padding:14px"><div class="em" style="font-size:64px">'+k[0]+'</div><div class="tr">'+esc(k[2])+'</div><div class="okn">'+esc(k[3])+'</div></div>'+soru+
    '<div class="dk-sec">'+sec.map(function(x,j){return'<button class="yazi" data-j="'+j+'"'+(L==='ar'?' dir="rtl"':'')+' style="'+(L==='en'?'font-size:34px':'')+'">'+esc(x)+'</button>'}).join('')+'</div>';
   [].forEach.call(document.querySelectorAll('[data-j]'),function(b){b.onclick=function(){var x=sec[+b.dataset.j];
     if(x===k._c){b.classList.add('dogru');if(ilk)dogru++;kartSes(L,k);[].forEach.call(document.querySelectorAll('[data-j]'),function(c){c.disabled=true});setTimeout(function(){i++;ciz()},1100)}
     else{b.classList.add('yanlis');b.disabled=true;ilk=false}}})}
  sayfa('Yazma','','#'+L+'/'+u.id);ciz()}

 function sonucGoster(L,u,akt,d,n,tekrar,hamle){var oran=n?d/n:0,yeni=false;
  if(oran>=.75)yeni=bitti('dil.'+L+'.'+u.id+'.'+akt,1);
  $('#m').innerHTML='<div class="dk-kart"><div class="em">'+(oran>=.75?'🏆':oran>=.5?'👍':'💪')+'</div><div class="yb" style="font-size:34px">'+(hamle?hamle+' hamlede bitirdin!':d+' / '+n+' doğru')+'</div>'+
   '<div class="tr">'+(oran>=.75?(yeni?'Bir yıldız kazandın! ⭐':'Harikasın, mâşallah!'):oran>=.5?'Güzel! Bir daha denersen yıldızı alırsın.':'Kartları bir daha dinleyip tekrar dene.')+'</div></div>'+
   '<button class="btn pri dk-buyuk" id="dkT">🔁 Tekrar oyna</button><button class="btn dk-buyuk" id="dkG">‹ Derse dön</button>';
  $('#dkT').onclick=tekrar;$('#dkG').onclick=function(){location.hash=L+'/'+u.id}}

 window.DilKosesi=function(p){stil();var L=p[0];
  if(!D){$('#m').innerHTML='<div class="card"><p>Yükleniyor…</p></div>';
   return yukle().then(function(){window.DilKosesi(p)},function(){$('#m').innerHTML='<div class="card"><p>Dersler yüklenemedi. İnternet bağlantını kontrol et.</p><button class="btn pri" onclick="location.reload()">Yenile</button></div>'})}
  var u=p[1]&&uniteBul(L,p[1]);if(!u)return liste(L);
  if(p[2]==='ogren')return ogren(L,u);if(p[2]==='dinle')return dinle(L,u);if(p[2]==='eslestir')return eslestir(L,u);if(p[2]==='yaz')return yaz(L,u);
  unite(L,u)};
})();
