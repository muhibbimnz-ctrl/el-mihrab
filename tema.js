/* el-Mihrâb ortak görünüm seçimi (tema.css ile birlikte). <head> içinde, stillerden sonra eşzamanlı yüklenmeli.
   localStorage "mihrab.tema": 'a' Gece Mavisi (varsayılan) · 'b' Sabah Ferahlığı · '0' klasik (sayfaların eski görünümü).
   Kadem'in eski anahtarı "kadem.tema" da eşitlenir ('' = klasik).
   Tema.al() · Tema.ayarla(t) · Tema.secici() (HTML) · Tema.bagla(kok) · Tema.altMenu(aktif) */
(function(){
 var K='mihrab.tema',KK='kadem.tema';
 function al(){var t=null;try{t=localStorage.getItem(K);if(t==null){t=localStorage.getItem(KK);if(t==='')t='0'}}catch(x){}
  return t==='a'||t==='b'||t==='0'?t:'a'}
 function renk(t){var m=document.querySelector('meta[name="theme-color"]');if(!m)return;if(!m.dataset.ilk)m.dataset.ilk=m.content;
  m.content=t==='a'?'#1E2A4A':t==='b'?'#F6FAF9':m.dataset.ilk}
 function uygula(t){t=t||al();var h=document.documentElement;if(t==='a'||t==='b')h.dataset.tema=t;else delete h.dataset.tema;renk(t);
  var b=document.querySelectorAll('[data-tema-sec]');for(var i=0;i<b.length;i++)b[i].classList.toggle('on',b[i].getAttribute('data-tema-sec')===t)}
 function ayarla(t){try{localStorage.setItem(K,t);localStorage.setItem(KK,t==='0'?'':t)}catch(x){}uygula(t);
  try{dispatchEvent(new CustomEvent('tema',{detail:t}))}catch(x){}}
 function secici(klasik){var t=al(),L=[['a','Gece Mavisi','linear-gradient(160deg,#1E2A4A,#2E3F73 60%,#F2994A)'],['b','Sabah Ferahlığı','linear-gradient(135deg,#fff,#14B8A6 55%,#FDE68A)']];
  if(klasik!==false)L.push(['0','Klasik','linear-gradient(135deg,#f3ead4,#0e5a43)']);
  return'<div class="t-temasec">'+L.map(function(x){return'<button type="button" data-tema-sec="'+x[0]+'"'+(t===x[0]?' class="on"':'')+'><i style="background:'+x[2]+'"></i>'+x[1]+'</button>'}).join('')+'</div>'}
 function bagla(kok){var b=(kok||document).querySelectorAll('[data-tema-sec]');for(var i=0;i<b.length;i++)b[i].onclick=function(){ayarla(this.getAttribute('data-tema-sec'))}}
 function altMenu(aktif){if(document.querySelector('.t-alt'))return;
  var L=[['ana','index.html','Ana sayfa','⌂'],['namaz','index.html#namaz','Kur’an','۞'],['medrese','medrese.html','Medrese','✎'],['kadem','kadem.html','Kadem','◆']];
  var n=document.createElement('nav');n.className='t-alt';n.setAttribute('aria-label','Ana menü');
  n.innerHTML=L.map(function(x){return'<a href="'+x[1]+'"'+(x[0]===aktif?' class="on" aria-current="page"':'')+'><i>'+x[3]+'</i>'+x[2]+'</a>'}).join('')+
   '<button type="button" id="t-gorunum" aria-label="Görünümü değiştir"><i>◐</i>Görünüm</button>';
  document.body.appendChild(n);document.body.classList.add('t-altli');
  document.getElementById('t-gorunum').onclick=function(){var t=al();ayarla(t==='a'?'b':t==='b'?'0':'a')}}
 addEventListener('storage',function(e){if(e.key===K||e.key===KK)uygula()});
 window.Tema={al:al,ayarla:ayarla,uygula:uygula,secici:secici,bagla:bagla,altMenu:altMenu};
 uygula();
})();
