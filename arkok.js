/* Arapça kelime için sözlükte aranacak biçimler: bağlaç/harf-i cer önekleri, zamir ve çekim sonekleri,
   muzâri önekleri (ي ت ن أ), ة/ت ve ء/ئ/ؤ değişimleri. tools/dil (aday üretimi) ile aynı kurallar. */
(function(){
var PR=['وال','فال','بال','كال','لل','ال','وب','ول','فب','فل','وك','فك','وس','فس','و','ف','ب','ل','ك','س'];
var SF=['تموها','تموه','تما','هما','كما','تم','تن','هم','هن','ها','كم','كن','نا','ني','ون','ين','ات','ان','وا','ه','ك','ي','ت','ن','ة','ا'];
var OZ={'ابا':'اب','ابي':'اب','ابو':'اب','اخا':'اخ','اخي':'اخ','اخو':'اخ','ذي':'ذو','ذا':'ذو','فا':'فو'};
function sw(a,b){return a.slice(0,b.length)===b}function ew(a,b){return b.length<=a.length&&a.slice(a.length-b.length)===b}
function oz(s){return OZ[s.replace(/[أإآ]/g,'ا')]}
window.arAday=function(n){var out=[],seen={};function add(x){if(x&&x.length>=2&&!seen[x]){seen[x]=1;out.push(x)}}
 var bases=[n];PR.forEach(function(p){if(sw(n,p)&&n.length-p.length>=2){var r=n.slice(p.length);bases.push(r);if(sw(r,'ال')&&r.length>4)bases.push(r.slice(2))}});
 bases.forEach(function(b){add(b);if(!sw(b,'ال'))add('ال'+b)});
 var stems=[];bases.forEach(function(b){var t=sw(b,'ال')&&b.length>4?b.slice(2):b;stems.push(t);var lv=[t];
  for(var k=0;k<2;k++){var nx=[];lv.forEach(function(u){SF.forEach(function(s){if(ew(u,s)&&u.length-s.length>=2){var st=u.slice(0,u.length-s.length);nx.push(st);
    if(ew(st,'ت'))stems.push(st.slice(0,-1)+'ة');var z=st.slice(-1);if(z==='ئ'||z==='ؤ')stems.push(st.slice(0,-1)+'ء');if(ew(st,'ا')&&st.length>=3)stems.push(st.slice(0,-1)+'ى')}})});
   stems=stems.concat(nx);lv=nx}});
 var v=[];stems.forEach(function(s){v.push(s);
  if(s.length>=4&&'يتناأإ'.indexOf(s[0])>=0){v.push(s.slice(1));if(sw(s.slice(1),'ست')&&s.length>=6)v.push('ا'+s.slice(1))}
  if(s.length===3&&'يتنأ'.indexOf(s[0])>=0){var r=s.slice(1);v.push(r+'ى',r+'ا',r[0]+'ا'+r[1],r+r[1])}
  if(s.length===2)v.push(s+'ى',s+'ا',s+'ي',s[0]+'ا'+s[1])});
 v.forEach(function(s){add(s);add('ال'+s);add(s+'ة');var o=oz(s);if(o)add(o)});
 var o0=oz(n);if(o0){out.unshift(o0)}return out};
})();
