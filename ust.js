/* el-Mihrâb ortak üst alan: selam, sıradaki namaz vakti, kaldığın âyet. Kadem dışındaki sayfalara eklenir.
   Vakitler ana sayfanın kaydettiği verilerden okunur (localStorage mihrab.loc, mihrab.pt2); kaldığın âyet beyan2.last.
   Renk: Sabah Ferahlığı seçiliyse turkuaz, diğer durumlarda Gece Mavisi. */
(function(){
 if(window.__mhUst)return;window.__mhUst=1;
 var SN="Fâtiha|Bakara|Âl-i İmrân|Nisâ|Mâide|En'âm|A'râf|Enfâl|Tevbe|Yûnus|Hûd|Yûsuf|Ra'd|İbrâhîm|Hicr|Nahl|İsrâ|Kehf|Meryem|Tâhâ|Enbiyâ|Hac|Mü'minûn|Nûr|Furkân|Şuarâ|Neml|Kasas|Ankebût|Rûm|Lokmân|Secde|Ahzâb|Sebe'|Fâtır|Yâsîn|Sâffât|Sâd|Zümer|Mü'min (Gâfir)|Fussılet|Şûrâ|Zuhruf|Duhân|Câsiye|Ahkâf|Muhammed|Fetih|Hucurât|Kâf|Zâriyât|Tûr|Necm|Kamer|Rahmân|Vâkıa|Hadîd|Mücâdele|Haşr|Mümtehine|Saf|Cum'a|Münâfikûn|Teğâbün|Talâk|Tahrîm|Mülk|Kalem|Hâkka|Meâric|Nûh|Cin|Müzzemmil|Müddessir|Kıyâme|İnsân|Mürselât|Nebe'|Nâziât|Abese|Tekvîr|İnfitâr|Mutaffifîn|İnşikâk|Bürûc|Târık|A'lâ|Gâşiye|Fecr|Beled|Şems|Leyl|Duhâ|İnşirâh|Tîn|Alak|Kadr|Beyyine|Zilzâl|Âdiyât|Kâria|Tekâsür|Asr|Hümeze|Fîl|Kureyş|Mâûn|Kevser|Kâfirûn|Nasr|Tebbet|İhlâs|Felak|Nâs".split('|'),PN=[['Fajr','İmsak'],['Sunrise','Güneş'],['Dhuhr','Öğle'],['Asr','İkindi'],['Maghrib','Akşam'],['Isha','Yatsı']];
 function g(k){try{var v=localStorage.getItem(k);return v?JSON.parse(v):null}catch(e){return null}}
 function tema(){var t=null;try{t=localStorage.getItem('mihrab.tema')||localStorage.getItem('kadem.tema')}catch(e){}return t}
 function dk(v){var a=String(v||'').slice(0,5).split(':');return a.length<2?NaN:+a[0]*60+(+a[1])}
 function vakit(){var loc=g('mihrab.loc'),st=g('mihrab.pt2');if(!loc||!st)return null;
  var d=new Date(),gun=function(x){var A=st[loc.k+'|'+x.getFullYear()+'-'+(x.getMonth()+1)];return A&&A[x.getDate()-1]},t=gun(d);if(!t)return null;
  var simdi=d.getHours()*60+d.getMinutes();
  for(var i=0;i<PN.length;i++){var m=dk(t[PN[i][0]]);if(m>simdi)return{ad:PN[i][1],s:String(t[PN[i][0]]).slice(0,5),kal:m-simdi}}
  var y=new Date(d.getTime()+864e5),ty=gun(y)||t,m0=dk(ty.Fajr);return{ad:'İmsak',s:String(ty.Fajr).slice(0,5),kal:1440-simdi+m0}}
 function sure(n){var s=Math.floor(n/60),d=n%60;return(s?s+' sa ':'')+d+' dk kaldı'}
 var css='.mh-ust{background:linear-gradient(160deg,#1E2A4A,#2E3F73);color:#fff;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:calc(14px + env(safe-area-inset-top,0px)) 18px 16px;border-radius:0 0 24px 24px}'+
  '.mh-ust.b{background:linear-gradient(135deg,#14B8A6,#0EA5E9)}.mh-ust .mh-in{max-width:760px;margin:0 auto}'+
  '.mh-ust .mh-sel{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#FFB547}.mh-ust.b .mh-sel{color:#fff;opacity:.9}'+
  '.mh-ust .mh-ad{display:block;color:#fff;text-decoration:none;font-size:26px;font-weight:800;letter-spacing:-.02em;margin:2px 0 12px}'+
  '.mh-ust .mh-arb{float:right;font-family:Amiri,serif;font-size:26px;line-height:1.2;opacity:.9;margin-top:-2px}'+
  '#home .hm-logo{display:none}'+
  '.mh-ust .mh-oz{display:grid;grid-template-columns:1fr 1fr;gap:8px}'+
  '.mh-ust .mh-oz a{display:block;background:rgba(255,255,255,.13);border-radius:14px;padding:9px 12px;color:#fff;text-decoration:none;min-width:0}.mh-ust.b .mh-oz a{background:rgba(255,255,255,.22)}'+
  '.mh-ust .mh-oz b{display:block;font-size:17px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.mh-ust .mh-oz small{display:block;font-size:11.5px;opacity:.85;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}';
 function ciz(el){var h=new Date().getHours(),v=vakit(),l=g('beyan2.last')||{s:1,a:1},s=Math.min(114,Math.max(1,+l.s||1)),a=+l.a||1;
  el.className='mh-ust'+(tema()==='b'?' b':'');
  el.innerHTML='<div class="mh-in"><span class="mh-arb" lang="ar">المِحْرَاب</span><div class="mh-sel">'+(h<5?'Hayırlı geceler':h<11?'Hayırlı sabahlar':h<17?'Hayırlı günler':h<22?'Hayırlı akşamlar':'Hayırlı geceler')+'</div>'+
   '<a class="mh-ad" href="index.html">el-Mihrâb</a><div class="mh-oz">'+
   '<a href="index.html#namaz"><b>'+(v?v.ad+' '+v.s:'Ezan vakti')+'</b><small>'+(v?sure(v.kal):'Konum seçmek için dokun')+'</small></a>'+
   '<a href="index.html#'+s+'-'+a+'"><b>'+SN[s-1]+' '+a+'</b><small>Kaldığın âyet · '+s+':'+a+'</small></a></div></div>'}
 function kur(){if(document.querySelector('.mh-ust'))return;
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  var el=document.createElement('header'),yer=document.querySelector('#home .hm');
  if(yer){el.style.margin='-26px -18px 0';el.style.alignSelf='stretch';yer.insertBefore(el,yer.firstChild)}else document.body.insertBefore(el,document.body.firstChild);
  ciz(el);setInterval(function(){ciz(el)},30000);
  addEventListener('storage',function(){ciz(el)});addEventListener('focus',function(){ciz(el)})}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',kur);else kur();
})();
