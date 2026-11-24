// Şâhid beyit: Lisânü'l-Arab'dan kelimenin geçtiği beyit + Türkçesi (sözlük ve romanlar)
var BY=(function(){
 var D=null,P=null,HR=/[ً-ٰٟـ]/g;
 function nr(w){return (w||'').replace(/[«»،.؟!:؛()\-"\[\]]/g,'').replace(HR,'').replace(/[إأآٱ]/g,'ا').replace(/ى/g,'ي').trim()}
 function yukle(){if(D)return Promise.resolve(D);if(P)return P;P=fetch('data/roman/beyit_ar.json?v=4').then(function(r){return r.json()}).then(function(d){return D=d}).catch(function(){P=null;return null});return P}
 function adaylar(n){var c=[n];['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك','س'].forEach(function(p){if(n.indexOf(p)===0&&n.length-p.length>=3){var r=n.slice(p.length);c.push(r,'ال'+r)}});
  var t=n.replace(/^(وال|بال|فال|ال|و|ف|ب)/,'');['هما','هم','هن','ها','كم','نا','ني','ه','ك','ي','ون','ين','ات','ان','ة','ا'].forEach(function(s){if(t.length-s.length>=3&&t.slice(-s.length)===s)c.push(t.slice(0,-s.length),'ال'+t.slice(0,-s.length))});return c}
 function bul(w){if(!D)return null;var c=adaylar(nr(w));for(var i=0;i<c.length;i++){var x=D.w[c[i]];if(x!=null)return D.b[x]}return null}
 function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function kok3(r){return nr(r).replace(/ء/g,'').split('')}
 function vurgu(m,w,kok){var n=nr(w),K=kok3(kok);return esc(m).replace(/[ء-يً-ٟ]+/g,function(t){var u=nr(t),ok=false;
   if(u===n||u.replace(/^(وال|بال|فال|كال|لل|ال|و|ف|ب|ل|ك)/,'')===n.replace(/^(ال)/,''))ok=true;
   else if(K.length>=3){var j=0;for(var i=0;i<u.length&&j<K.length;i++)if(u[i]===K[j]||(K[j]==='ا'&&/[اوي]/.test(u[i]))||(/[وي]/.test(K[j])&&/[اوي]/.test(u[i])))j++;ok=j===K.length&&u.length<=K.length+5}
   return ok?'<b>'+t+'</b>':t})}
 function html(b,w,koyu){if(!b)return '';var p=b[0].split(' ... ');
  return '<div class="sahid'+(koyu?' koyu':'')+'"><div class="sb" lang="ar" dir="rtl"><span>'+vurgu(p[0],w,b[1])+'</span><span>'+vurgu(p[1]||'',w,b[1])+'</span></div>'+
   (b[2]?'<div class="st">'+esc(b[2])+'</div>':'')+'<div class="sk">Şâhid · Lisânü’l-Arab, “'+esc(b[1])+'” maddesi</div></div>'}
 var CSS='.sahid{margin:8px 0 2px;padding:10px 12px;border-radius:12px;background:#f6edda;border:1px solid #e1cf9f;border-inline-start:4px solid #b98a2e}'+
  '.sahid .sb{font-family:Amiri,"Noto Naskh Arabic",serif;font-size:19px;line-height:1.75;color:#2b1d45}'+
  '.sahid .sb span{display:block;text-align:right}.sahid .sb span+span{text-align:left;padding-inline-start:14%}.sahid .sb b{color:#9a2f12}'+
  '.sahid .st{font-size:14.5px;line-height:1.5;color:#3d3528;font-style:italic;margin-top:6px;text-align:center}.sahid .sk{font-size:11.5px;color:#8a7a5c;margin-top:5px;text-align:center}'+
  '.sahid.koyu{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.18);border-inline-start-color:#f3d98b}.sahid.koyu .sb{color:#fff}.sahid.koyu .sb b{color:#f3d98b}.sahid.koyu .st{color:#e9e1f5}.sahid.koyu .sk{color:#bfb3d6}'+
  '@media(prefers-color-scheme:dark){.sahid{background:#2a2433;border-color:#4a3e5c}.sahid .sb{color:#efe6ff}.sahid .sb b{color:#f3d98b}.sahid .st{color:#d9cfe9}.sahid .sk{color:#a598bd}}';
 try{var st=document.createElement('style');st.textContent=CSS;document.head.appendChild(st)}catch(e){}
 return {yukle:yukle,bul:bul,html:html}
})();
