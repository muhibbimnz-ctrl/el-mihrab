// YDS deneme sınavı ekler: node tools/yds/deneme_ekle.js tools/yds/deneme/dXX.json
// Dosya: { dn, metinler:[modern metin kimlikleri], sorular:[{tip,q,k(5 şık),d,a,p?}], pasajlar:{anahtar:metin} }
// Okuma (paragraf) soruları data/modern/modern.json'daki metinlerin kendi sorularından üretilir (deneme başına 30).
const fs = require('fs'), path = require('path');
const kok = path.join(__dirname, '..', '..');
const bd = path.join(kok, 'data', 'yds', 'banka.json'), md = path.join(kok, 'data', 'modern', 'modern.json');
const B = JSON.parse(fs.readFileSync(bd, 'utf8')), M = JSON.parse(fs.readFileSync(md, 'utf8'));
const S = { kelime: 8, gramer: 8, cloze: 5, tamamlama: 7, ceviri: 8, diyalog: 4, yakin: 4, bosluk: 3, bozan: 3 };
const hata = [];
for (const f of process.argv.slice(2)) {
  const D = JSON.parse(fs.readFileSync(f, 'utf8')), dn = D.dn;
  if (B.sorular.some(q => q.dn === dn)) { hata.push(`deneme ${dn} zaten var`); continue; }
  const say = {}, yeni = [];
  for (const [k, v] of Object.entries(D.pasajlar || {})) { if (B.pasajlar[k]) hata.push('pasaj zaten var: ' + k); B.pasajlar[k] = v; }
  D.sorular.forEach(q => {
    say[q.tip] = (say[q.tip] || 0) + 1;
    const id = `d${dn}_${q.tip}${say[q.tip]}`;
    if (!S[q.tip]) hata.push(id + ': tip geçersiz');
    if (!Array.isArray(q.k) || q.k.length !== 5 || new Set(q.k).size !== 5) hata.push(id + ': 5 farklı şık olmalı');
    if (!(q.d >= 0 && q.d < 5)) hata.push(id + ': cevap geçersiz');
    if (q.p && !B.pasajlar[q.p]) hata.push(id + ': pasaj yok ' + q.p);
    yeni.push({ id, tip: q.tip, q: q.q, k: q.k, d: q.d, a: q.a || '', ...(q.p ? { p: q.p } : {}), dn });
  });
  for (const [t, n] of Object.entries(S)) if ((say[t] || 0) !== n) hata.push(`deneme ${dn}: ${t} ${say[t] || 0}/${n}`);
  let pn = 0;
  for (const id of D.metinler) {
    const m = M.metinler.find(x => x.id === id); if (!m) { hata.push('metin yok: ' + id); continue; }
    const pk = 'm_' + id; if (!B.pasajlar[pk]) B.pasajlar[pk] = m.ar.join(' ');
    for (const s of m.sorular) { if (pn >= 30) break; pn++; yeni.push({ id: `d${dn}_paragraf${pn}`, tip: 'paragraf', q: s.s, k: s.k, d: s.d, a: s.a || '', p: pk, dn }); }
  }
  if (pn !== 30) hata.push(`deneme ${dn}: okuma sorusu ${pn}/30`);
  B.sorular.push(...yeni);
  console.log(`deneme ${dn}: ${yeni.length} soru hazır`);
}
if (hata.length) { console.error(hata.join('\n')); process.exit(1); }
fs.writeFileSync(bd, JSON.stringify(B));
console.log('denemeler:', [...new Set(B.sorular.map(q => q.dn || 1))].join(','), '| toplam soru', B.sorular.length);
