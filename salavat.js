/* el-Mihrâb açılış ekranı: Peygamber Efendimize salavat ve günün nasihati.
   Uygulama her açıldığında bir kez gösterilir (oturum başına; sayfa içi geçişlerde ve adresle doğrudan bir bölüm açılınca çıkmaz).
   Günün nasihati data/nasihat.json'dan gün sırasına göre seçilir; aynı liste "Nasihatler" kitabında (nasihat.html) okunur.
   window.gunNasihati(liste) → bugünkü kaydın sırası (nasihat.html de kullanır). */
(function(){
 function gunSira(n){var d=new Date();return Math.floor((Date.UTC(d.getFullYear(),d.getMonth(),d.getDate()))/864e5)%n}
 window.gunNasihati=function(L){return L&&L.length?gunSira(L.length):0};
 if(!document.getElementById('home'))return;
 try{if(location.hash||sessionStorage.getItem('mihrab.salavat'))return;
  var r=document.referrer;if(r&&r.indexOf(location.origin)===0)return;
  sessionStorage.setItem('mihrab.salavat','1')}catch(e){return}
 window.__salavatAcik=1;
 function esc(s){return String(s||'').replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 var css='#slv{position:fixed;inset:0;z-index:2147483000;background:radial-gradient(120% 80% at 50% 0%,#17322B 0%,#0D1B18 62%);color:#EFE6D2;display:flex;flex-direction:column;align-items:center;overflow-y:auto;-webkit-overflow-scrolling:touch;opacity:0;transition:opacity .35s ease;font-family:"Source Sans 3",system-ui,-apple-system,"Segoe UI",sans-serif}'+
  '#slv.ac{opacity:1}#slv.kapan{opacity:0;pointer-events:none}'+
  '#slv .ic{width:100%;max-width:460px;padding:calc(34px + env(safe-area-inset-top,0px)) 26px calc(26px + env(safe-area-inset-bottom,0px));box-sizing:border-box;display:flex;flex-direction:column;min-height:100%}'+
  '#slv .ust{flex:1;display:flex;flex-direction:column;justify-content:center;text-align:center;padding:10px 0 6px}'+
  '#slv .cer{width:150px;height:14px;margin:0 auto 22px;opacity:.75}'+
  '#slv .slv-ar{font-family:"Amiri Quran",Amiri,"Scheherazade New",serif;direction:rtl;font-size:31px;line-height:1.95;color:#D9B868;margin:0 0 18px}'+
  '#slv h1{font-family:"Cormorant Garamond","Source Serif 4",Georgia,serif;font-weight:700;font-size:27px;line-height:1.2;margin:0 0 12px;color:#F4ECDA;letter-spacing:.2px}'+
  '#slv .slv-m{background:none;border:0;padding:0;box-shadow:none;font-family:"Source Serif 4",Georgia,serif;font-size:15px;line-height:1.6;color:rgba(239,230,210,.78);margin:0 auto;max-width:360px}#slv .slv-m small{display:block;margin-top:6px;font-family:"Source Sans 3",system-ui,sans-serif;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:rgba(217,184,104,.8)}'+
  '#slv .dg{-webkit-appearance:none;appearance:none;box-shadow:none;display:block;width:100%;margin:26px 0 0;padding:15px 16px;border:1px solid rgba(217,184,104,.55);border-radius:14px;background:rgba(217,184,104,.12);color:#F4ECDA;font:600 16.5px "Source Sans 3",system-ui,sans-serif;letter-spacing:.2px;cursor:pointer;transition:background .2s}#slv .dg:active{background:rgba(217,184,104,.24)}'+
  '#slv .nas{margin-top:26px;padding:18px 18px 16px;border-radius:16px;background:rgba(244,236,218,.06);border:1px solid rgba(244,236,218,.1);text-align:left}'+
  '#slv .nas .et{font-size:11.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#D9B868;margin:0 0 8px}'+
  '#slv .nas h2{font-family:"Cormorant Garamond","Source Serif 4",Georgia,serif;font-size:21px;font-weight:700;margin:0 0 8px;color:#F4ECDA}'+
  '#slv .nas blockquote{margin:0;font-family:"Source Serif 4",Georgia,serif;font-size:16px;line-height:1.6;color:#EFE6D2}'+
  '#slv .nas .kay{font-size:12.5px;color:rgba(239,230,210,.6);margin:6px 0 10px}'+
  '#slv .nas p{margin:0;font-size:14.5px;line-height:1.55;color:rgba(239,230,210,.82)}'+
  '#slv .alt{display:flex;justify-content:space-between;align-items:center;margin-top:14px;font-size:13.5px}#slv .alt a{color:#D9B868;text-decoration:none;font-weight:600}#slv .alt button{border:0;background:none;color:rgba(239,230,210,.6);font:inherit;cursor:pointer;padding:6px 0}'+
  '@media(min-height:760px){#slv .slv-ar{font-size:34px}}';
 var CER='<svg class="cer" viewBox="0 0 150 14" fill="none" stroke="#D9B868" stroke-width="1"><path d="M0 7h58M92 7h58"/><path d="M75 1l6 6-6 6-6-6z"/><circle cx="63" cy="7" r="1.6" fill="#D9B868" stroke="none"/><circle cx="87" cy="7" r="1.6" fill="#D9B868" stroke="none"/></svg>';
 function kur(){
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  var d=document.createElement('div');d.id='slv';d.setAttribute('role','dialog');d.setAttribute('aria-label','Salavat');
  d.innerHTML='<div class="ic"><div class="ust">'+CER+
   '<div class="slv-ar" lang="ar">اللّٰهُمَّ صَلِّ عَلٰى<br>سَيِّدِنَا مُحَمَّدٍ<br>وَعَلٰى آلِهِ وَصَحْبِهِ وَسَلِّمْ</div>'+
   '<h1>Peygamber Efendimize salavat getirelim</h1>'+
   '<div class="slv-m">Allah ve melekleri Peygamber’e salât ederler. Ey iman edenler! Siz de ona salât edin, içtenlikle selâm verin.<small>Ahzâb, 33/56</small></div>'+
   '<button class="dg" type="button">Sallallâhu aleyhi ve sellem</button></div>'+
   '<div class="nas" id="slvN" hidden></div>'+
   '<div class="alt"><a href="nasihat.html">Nasihatler kitabı ›</a><button type="button" data-k>Geç</button></div></div>';
  document.body.appendChild(d);requestAnimationFrame(function(){d.classList.add('ac')});
  function kapa(){d.classList.add('kapan');window.__salavatAcik=0;setTimeout(function(){d.remove()},380)}
  d.querySelector('.dg').onclick=kapa;d.querySelector('[data-k]').onclick=kapa;
  addEventListener('keydown',function k(e){if(e.key==='Escape'){kapa();removeEventListener('keydown',k)}});
  fetch('data/nasihat.json').then(function(r){return r.json()}).then(function(j){var L=j.n||[];if(!L.length)return;var x=L[gunSira(L.length)],N=document.getElementById('slvN');if(!N)return;
   N.innerHTML='<div class="et">Günün nasihati</div><h2>'+esc(x.b)+'</h2><blockquote>“'+esc(x.n)+'”</blockquote><div class="kay">'+esc(x.k)+'</div><p>'+esc(x.s)+'</p>';N.hidden=false}).catch(function(){});
 }
 if(document.body)kur();else document.addEventListener('DOMContentLoaded',kur);
})();
