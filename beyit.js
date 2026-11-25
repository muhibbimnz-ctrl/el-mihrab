// Şâhid beyit: Arapça (Lisânü'l-Arab) ve Farsça (klasik şairler) — kelimenin geçtiği beyit, şâiri ve Türkçesi.
// Kaynaklar beyit başına değil, sözlük sayfasının altında topluca verilir.
var BY=(function(){
 var D={},P={},HR=/[ً-ٰٟـ]/g;
 function nr(w){return (w||'').replace(/[«»،.؟!:؛()\-"\[\]]/g,'').replace(HR,'').replace(/[إأآٱ]/g,'ا').replace(/ى/g,'ي').trim()}
 function nf(w){return (w||'').replace(/[«»،.؟!:؛()\-"\[\]]/g,'').replace(HR,'').replace(/ي/g,'ی').replace(/ك/g,'ک').replace(/‌/g,'').trim()}
 function yukle(d){d=d||'ar';if(D[d])return Promise.resolve(D[d]);if(P[d])return P[d];
  P[d]=fetch('data/roman/beyit_'+d+'.json?v=8').then(function(r){return r.json()}).then(function(x){return D[d]=x}).catch(function(){P[d]=null;return null});return P[d]}
 function adaylar(n,d){var c=[n];if(d==='fa'){[/(هایی|های|ها|ان|ی)$/,/^(نمی|می|ب)/].forEach(function(re){var r=n.replace(re,'');if(r!==n&&r.length>=2)c.push(r)});return c}
  ['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك','س'].forEach(function(p){if(n.indexOf(p)===0&&n.length-p.length>=3){var r=n.slice(p.length);c.push(r,'ال'+r)}});
  var t=n.replace(/^(وال|بال|فال|ال|و|ف|ب)/,'');['هما','هم','هن','ها','كم','نا','ني','ه','ك','ي','ون','ين','ات','ان','ة','ا'].forEach(function(s){if(t.length-s.length>=3&&t.slice(-s.length)===s)c.push(t.slice(0,-s.length),'ال'+t.slice(0,-s.length))});return c}
 function hepsi(w,d){d=d||'ar';var X=D[d];if(!X)return [];var c=adaylar(d==='fa'?nf(w):nr(w),d);for(var i=0;i<c.length;i++){var x=X.w[c[i]];if(x!=null)return (typeof x==='number'?[x]:x).map(function(j){return X.b[j]})}return []}
 function bul(w,d){return hepsi(w,d)[0]||null}
 function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function kok3(r){return nr(r).replace(/ء/g,'').split('')}
 function vurgu(m,w,kok,d){
  if(d==='fa'){var n=nf(w),V=adaylar(n,'fa');return esc(m).replace(/[؀-ۿ‌]+/g,function(t){var u=nf(t),ok=V.indexOf(u)>=0||adaylar(u,'fa').indexOf(n)>=0;return ok?'<b>'+t+'</b>':t})}
  var n=nr(w),K=kok3(kok||'');return esc(m).replace(/[ء-يً-ٟ]+/g,function(t){var u=nr(t),ok=false;
   if(u===n||u.replace(/^(وال|بال|فال|كال|لل|ال|و|ف|ب|ل|ك)/,'')===n.replace(/^(ال)/,''))ok=true;
   else if(K.length>=3){var j=0;for(var i=0;i<u.length&&j<K.length;i++)if(u[i]===K[j]||(K[j]==='ا'&&/[اوي]/.test(u[i]))||(/[وي]/.test(K[j])&&/[اوي]/.test(u[i])))j++;ok=j===K.length&&u.length<=K.length+5}
   return ok?'<b>'+t+'</b>':t})}
 // b: ar -> [beyit, kök, türkçe, şâir?]  fa -> [beyit, şâir, türkçe]
 function html(b,w,koyu,d){if(!b)return '';d=d||'ar';var p=b[0].split(' ... '),sa=d==='fa'?b[1]:(b[3]||''),tr=b[2],kok=d==='fa'?'':b[1];
  return '<div class="sahid '+d+(koyu?' koyu':'')+'"><div class="sb" lang="'+d+'" dir="rtl"><span>'+vurgu(p[0],w,kok,d)+'</span><span>'+vurgu(p[1]||'',w,kok,d)+'</span></div>'+
   (sa?'<div class="sa">— '+esc(sa)+'</div>':'')+(tr?'<div class="st">'+esc(tr)+'</div>':'')+'</div>'}
 var CSS='.sahid{direction:ltr;font-family:system-ui,sans-serif;position:relative;margin:10px 0 4px;padding:14px 14px 10px;border-radius:14px;background:#fbf4e3;border:1px solid #e3d2a6;box-shadow:inset 0 0 0 4px #fbf4e3,inset 0 0 0 5px #e9d9ad}'+
  '.sahid .sb{font-family:Amiri,"Noto Naskh Arabic",serif;font-size:20px;line-height:1.8;color:#22303a}.sahid.fa .sb{font-family:"Noto Nastaliq Urdu",Vazirmatn,serif;font-size:18px;line-height:2.25}'+
  '.sahid .sb span{display:block;text-align:right}.sahid .sb span+span{text-align:left;padding-inline-start:12%}.sahid .sb b{color:#a3341a;font-weight:700}'+
  '.sahid .sa{font:600 12.5px system-ui,sans-serif;color:#8a6d2b;text-align:left;margin-top:2px;letter-spacing:.2px}'+
  '.sahid .st{font-size:15px;line-height:1.55;color:#3a3226;font-style:italic;margin-top:8px;padding-top:8px;border-top:1px dashed #dcc89a;text-align:center}'+
  '.sahid.koyu{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.2);box-shadow:none}.sahid.koyu .sb{color:#fff}.sahid.koyu .sb b{color:#f3d98b}.sahid.koyu .st{color:#e9e1f5;border-color:rgba(255,255,255,.2)}.sahid.koyu .sa{color:#f3d98b}'+
  '@media(prefers-color-scheme:dark){.sahid{background:#24211b;border-color:#4a4130;box-shadow:inset 0 0 0 4px #24211b,inset 0 0 0 5px #4a4130}.sahid .sb{color:#f1e8d4}.sahid .sb b{color:#f0c46a}.sahid .st{color:#d9cfb9;border-color:#4a4130}.sahid .sa{color:#d1b06a}}';
 try{var st=document.createElement('style');st.textContent=CSS;document.head.appendChild(st)}catch(e){}
 return {yukle:yukle,bul:bul,hepsi:hepsi,html:html,esc:esc}
})();
