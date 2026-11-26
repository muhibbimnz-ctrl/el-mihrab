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
 function sure(n){var s=Math.floor(n/60),d=n%60;return(s?s+' sa ':'')+d+' dk'}
 var css='.mh-ust{background:linear-gradient(160deg,#2B3D6E,#3D5494);color:#fff;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;padding:14px 18px 16px;border-radius:0 0 26px 26px}'+
  '.mh-ust.b{background:linear-gradient(135deg,#2CC4B4,#38B2F0)}.mh-ust .mh-in{max-width:760px;margin:0 auto}'+
  '.mh-ust .mh-sel{font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#FFB547}.mh-ust.b .mh-sel{color:#fff;opacity:.9}'+
  '.mh-ust .mh-arb{float:right;font-family:"Reem Kufi","Aref Ruqaa",Amiri,serif;font-weight:700;font-size:38px;line-height:1;color:#F5C76B;text-shadow:0 2px 10px rgba(0,0,0,.25);margin-top:-2px;letter-spacing:1px}.mh-ust.b .mh-arb{color:#FFF6D6}'+
  '.mh-ust .mh-ad{display:block;color:#fff;text-decoration:none;font-size:30px;font-weight:800;letter-spacing:-.02em;margin:2px 0 12px;font-size:28px}'+
  '.mh-ust .mh-ad{display:flex!important;align-items:center;gap:10px}.mh-ust .mh-lg{width:34px;height:34px;border-radius:9px;box-shadow:0 2px 8px rgba(0,0,0,.25);flex:none}'+
  '.mh-ust .mh-alt{font-size:14px;opacity:.85;margin-bottom:18px}'+
  '.mh-ust .mh-oz{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}'+
  '.mh-ust .mh-oz a{display:block;background:rgba(255,255,255,.14);border-radius:16px;padding:9px 6px;color:#fff;text-decoration:none;text-align:center;min-width:0}.mh-ust.b .mh-oz a{background:rgba(255,255,255,.24)}'+
  '.mh-ust .mh-oz b{display:block;font-size:18px;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.mh-ust .mh-oz small{display:block;font-size:11.5px;opacity:.85;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'+
  '#home .hm-logo{display:none}'+
  '#home{overflow:hidden!important;display:flex!important;flex-direction:column}#home.hide{display:none!important}'+
  '#home .hm{flex:1;min-height:0;width:100%;max-width:520px;margin:0 auto;padding:0 14px 10px;gap:10px;align-items:stretch;box-sizing:border-box}'+
  '#home .hmgrid{flex:1;min-height:0;width:auto;margin:0;gap:10px;grid-template-rows:1fr 1fr auto}'+
  '#home .hmgrid .tile{aspect-ratio:auto!important;min-height:0!important;height:auto!important;padding:8px 6px!important}'+
  '#home .hmgrid .tile svg{width:46px!important;height:36px!important}#home .hmgrid .tile b{font-size:16px!important}#home .hm-sub{font-size:11.5px}'+
  '#home #hKadem{padding:10px!important;flex-direction:row;gap:10px!important}#home #hKadem svg{flex:none}'+
  '#home .hm-links{flex:none;text-align:center;font-size:13px;margin:0}'+
  '@media(max-height:620px){#home{overflow-y:auto!important}#home .hmgrid{grid-template-rows:auto}#home .hmgrid .tile{min-height:120px!important}}'+
  'body:has(#home:not(.hide)) .top{background:#2B3D6E;border-bottom:0;box-shadow:none}'+
  'body:has(#home:not(.hide)) .top .ib,body:has(#home:not(.hide)) .top .brand b{color:#fff}body:has(#home:not(.hide)) .top .brand small{color:#C9D2EC}'+
  'body:has(#home:not(.hide)) .top .sbtn,body:has(#home:not(.hide)) .top .jump{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.25);color:#fff}'+
  'body:has(#home:not(.hide)) .top .sbtn .ar{color:#FFB547}';
 function kadem(){var k=0;try{var o=JSON.parse(localStorage.getItem('kadem.v1')||'{}');for(var x in o)if(/^p\./.test(x))k++}catch(e){}return k}
 function ciz(el){var h=new Date().getHours(),v=vakit(),l=g('beyan2.last')||{s:1,a:1},s=Math.min(114,Math.max(1,+l.s||1)),a=+l.a||1;
  el.className='mh-ust'+(tema()==='b'?' b':'');
  el.innerHTML='<div class="mh-in"><span class="mh-arb" lang="ar">المِحْرَاب</span><div class="mh-sel">'+(h<5?'Hayırlı geceler':h<11?'Hayırlı sabahlar':h<17?'Hayırlı günler':h<22?'Hayırlı akşamlar':'Hayırlı geceler')+'</div>'+
   '<a class="mh-ad" href="index.html"><img class="mh-lg" src="icon-192.png" alt="" width="34" height="34">El-Mihrâb</a><div class="mh-oz">'+
   '<a href="index.html#namaz"><b>'+(v?v.s:'—')+'</b><small>'+(v?v.ad+' · '+sure(v.kal):'Ezan vakti')+'</small></a>'+
   '<a href="index.html#'+s+'-'+a+'"><b>'+s+':'+a+'</b><small>'+SN[s-1]+'</small></a>'+
   '<a href="kadem.html"><b>'+kadem()+'</b><small>Kadem konusu</small></a></div></div>'}
 function kur(){if(document.querySelector('.mh-ust'))return;
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  var el=document.createElement('header'),yer=document.querySelector('#home .hm');
  if(yer){el.style.margin='0 -14px';el.style.alignSelf='stretch';el.style.flex='none';yer.insertBefore(el,yer.firstChild)}else document.body.insertBefore(el,document.body.firstChild);
  ciz(el);setInterval(function(){ciz(el)},30000);
  addEventListener('storage',function(){ciz(el)});addEventListener('focus',function(){ciz(el)})}
 if(document.readyState!=='loading'||document.querySelector('#home .hm'))kur();else document.addEventListener('DOMContentLoaded',kur);
})();
