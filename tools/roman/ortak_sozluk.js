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
const ders={ar:'arapca',fa:'farsca',en:'ingilizce'};
for(const [d,f] of Object.entries(ders)){const p=path.join(R,'veri',f+'.js');if(!fs.existsSync(p))continue;
  let src=fs.readFileSync(p,'utf8');const names=[...src.matchAll(/(?:^|\n)\s*(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=/g)].map(m=>m[1]);
  let env;try{env=new Function('window',src+';return {'+names.map(n=>n+':typeof '+n+'!=="undefined"?'+n+':null').join(',')+'}')({})}catch(e){console.log('atlandı',f,e.message);continue}
  const gez=o=>{if(Array.isArray(o)){if(o.length>=2&&typeof o[0]==='string'&&typeof o[1]==='string'&&o[0].length<40&&o[1].length<80&&o[0].split(/\s+/).length<=3&&!/[A-Za-z]/.test(d==='en'?'':o[0]))return [o];return o.flatMap(gez)}
    if(o&&typeof o==='object')return Object.entries(o).flatMap(([k,v])=>/^(vocab|voc|kelime|words)$/.test(k)&&Array.isArray(v)?v.filter(x=>Array.isArray(x)&&typeof x[0]==='string'&&typeof x[1]==='string'):gez(v));return []};
  for(const [w,m] of Object.values(env).flatMap(gez)){for(const p of w.split(/\s*[–\-\/،,]\s*/)){const n=norm(p,d);if(n&&n.split(' ').length===1&&!(n in S[d]))S[d][n]=m}}}
for(const d in S){fs.writeFileSync(path.join(R,'data/roman','sozluk_'+d+'.json'),JSON.stringify(S[d]));console.log(d,Object.keys(S[d]).length)}
