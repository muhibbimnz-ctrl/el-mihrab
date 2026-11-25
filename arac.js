/* el-Mihrâb araç sayfaları için ortak yardımcılar. <head> içinde yüklenir (tema ilk boyamadan önce uygulanır). */
(function(){try{var s=JSON.parse(localStorage.getItem('beyan2.set')||'{}'),t=s.theme;
  if(t==='gece'||(!t&&matchMedia('(prefers-color-scheme: dark)').matches))document.documentElement.setAttribute('data-theme','gece')}catch(e){}})();
var $=function(q,e){return (e||document).querySelector(q)},$$=function(q,e){return Array.prototype.slice.call((e||document).querySelectorAll(q))};
var LS={get:function(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}},set:function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function toast(m){var t=$('#toast');if(!t){t=document.createElement('div');t.id='toast';t.className='toast';document.body.appendChild(t)}t.textContent=m;t.classList.add('on');clearTimeout(toast.t);toast.t=setTimeout(function(){t.classList.remove('on')},2600)}
function bugun(d){d=d||new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
function trTarih(s,o){var d=typeof s==='string'?new Date(s.length<=10?s+'T12:00':s):s;return d.toLocaleDateString('tr-TR',o||{day:'numeric',month:'long',year:'numeric'})}
/* Geri: uygulamanın içinden gelindiyse geri git, değilse Namaz ve Kur'an menüsünü aç */
document.addEventListener('DOMContentLoaded',function(){var g=$('a.geri');if(!g)return;
  g.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>';
  g.setAttribute('href','./#namaz');g.setAttribute('aria-label','Geri');
  g.onclick=function(e){try{if(document.referrer&&new URL(document.referrer).origin===location.origin&&history.length>1){e.preventDefault();history.back()}}catch(x){}}});
/* Konum: ezan vakti ile aynı kayıt (mihrab.loc) */
function konumAl(ok,hata){if(!navigator.geolocation){hata&&hata();return}
  navigator.geolocation.getCurrentPosition(function(p){var l={k:'g'+p.coords.latitude.toFixed(2)+','+p.coords.longitude.toFixed(2),lat:+p.coords.latitude.toFixed(4),lng:+p.coords.longitude.toFixed(4),name:'Konumunuz'};
    if(!LS.get('mihrab.loc',null)){LS.set('mihrab.loc',l);LS.set('mihrab.pt2',{})}ok(l)},function(){hata&&hata()},{enableHighAccuracy:true,timeout:15000,maximumAge:300000})}
