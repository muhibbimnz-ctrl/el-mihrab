// Roman okumada "kitap sözlüğünde yok" kelimeler için dil başına ortak sözlük:
// bütün romanların sözlükleri + veri/<dil>.js derslerindeki kelime listeleri → data/roman/sozluk_<dil>.json
// Kullanım: node tools/roman/ortak_sozluk.js
const fs=require('fs'),path=require('path'),R=path.join(__dirname,'..','..');
const H=/[ً-ْٰـ]/g;
const norm=(w,d)=>{if(d==='en'){w=w.toLowerCase().replace(/^['".,!?;:]+|['".,!?;:]+$/g,'');return /'s$/.test(w)?w.slice(0,-2):w}return w.replace(/[«»،.؟!:؛()\-"]/g,'').replace(H,'').trim()};
const S={ar:{},fa:{},en:{}};
for(const f of fs.readdirSync(path.join(R,'data/roman'))){if(!/^[a-z]+\.json$/.test(f)||f==='liste.json')continue;
  const K=JSON.parse(fs.readFileSync(path.join(R,'data/roman',f),'utf8'));if(!S[K.dil])continue;
  for(const [k,v] of Object.entries(K.sozluk||{}))if(!(k in S[K.dil]))S[K.dil][k]=v}
// Ders verilerindeki ve diğer bölümlerdeki kelime çiftleri: [kelime (≤3 sözcük), Türkçe anlam]
const AR=/[؀-ۿ]/,LAT=/^[A-Za-z][A-Za-z '\-]*$/;
const iyi=(w,m,d)=>typeof w==='string'&&typeof m==='string'&&w.length<40&&m.length>0&&m.length<90&&w.trim().split(/\s+/).length<=3&&!AR.test(m)&&(d==='en'?LAT.test(w.trim()):AR.test(w))&&!/[.!?؟]$/.test(w.trim());
const gez=(o,d,acc=[])=>{if(Array.isArray(o)){if(o.length>=2&&iyi(o[0],o[1],d))acc.push([o[0],o[1]]);else o.forEach(x=>gez(x,d,acc))}
  else if(o&&typeof o==='object')for(const v of Object.values(o))gez(v,d,acc);return acc};
const ekle=(d,ps)=>{let n0=Object.keys(S[d]).length;for(const [w,m] of ps)for(const p of w.split(/\s*[–\/،,]\s*/)){const n=norm(p,d);if(n&&!(n in S[d]))S[d][n]=m.trim()}return Object.keys(S[d]).length-n0};
const ders={ar:'arapca',fa:'farsca',en:'ingilizce'};
for(const [d,f] of Object.entries(ders)){const p=path.join(R,'veri',f+'.js');if(!fs.existsSync(p))continue;
  let src=fs.readFileSync(p,'utf8');const names=[...src.matchAll(/(?:^|\n)\s*(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=/g)].map(m=>m[1]);
  let env;try{env=new Function('window',src+';return {'+names.map(n=>n+':typeof '+n+'!=="undefined"?'+n+':null').join(',')+'}')({})}catch(e){console.log('atlandı',f,e.message);continue}
  console.log(f,'+',ekle(d,gez(env,d)))}
const J=f=>{try{return JSON.parse(fs.readFileSync(path.join(R,f),'utf8'))}catch(e){return null}};
const dosya=(dir,re)=>fs.existsSync(path.join(R,dir))?fs.readdirSync(path.join(R,dir)).filter(x=>re.test(x)).map(x=>dir+'/'+x):[];
for(const f of ['data/modern/modern.json',...dosya('tools/yds/yeni',/\.json$/),...dosya('tools/yds/deneme',/\.json$/),...dosya('tools/dil/ar',/\.json$/),'data/hadis/erbain.json']){const o=J(f);if(o)console.log(f,'+',ekle('ar',gez(o,'ar')))}
for(const f of dosya('tools/dil/fa',/\.json$/)){const o=J(f);if(o)console.log(f,'+',ekle('fa',gez(o,'fa')))}
// Elle hazırlanan temel kelime listeleri: tools/roman/sozluk/<dil>_*.txt (kelime=anlam)
for(const f of dosya('tools/roman/sozluk',/\.txt$/)){const d=f.split('/').pop().slice(0,2);if(!S[d])continue;
  const ps=fs.readFileSync(path.join(R,f),'utf8').split('\n').filter(l=>l.includes('=')).map(l=>{const i=l.indexOf('=');return [l.slice(0,i).trim().replace(/_/g,'‌'),l.slice(i+1).trim()]});
  let n0=Object.keys(S[d]).length;for(const [w,m] of ps){const n=norm(w,d);if(n&&!(n in S[d]))S[d][n]=m}console.log(f,'+',Object.keys(S[d]).length-n0)}
for(const d in S){fs.writeFileSync(path.join(R,'data/roman','sozluk_'+d+'.json'),JSON.stringify(S[d]));console.log(d,Object.keys(S[d]).length)}
