// YDS okuma metinlerini ekler: node tools/yds/metin_ekle.js tools/yds/yeni/<alan>.json [...]
// Her dosya bir dizi metin içerir. Denetim: kimlik tekrarı, alan geçerli mi, ar/tr paragraf sayısı eşit mi,
// soruların 4 şıkkı ve geçerli cevabı var mı. Hata varsa hiçbir şey yazılmaz.
const fs = require('fs'), path = require('path');
const kok = path.join(__dirname, '..', '..'), dosya = path.join(kok, 'data', 'modern', 'modern.json');
const M = JSON.parse(fs.readFileSync(dosya, 'utf8'));
const alanlar = new Set(M.alanlar.map(a => a[0])), idler = new Set(M.metinler.map(m => m.id));
const hatalar = [], yeni = [];
for (const f of process.argv.slice(2)) {
  for (const m of JSON.parse(fs.readFileSync(f, 'utf8'))) {
    const h = s => hatalar.push(`${path.basename(f)} / ${m.id}: ${s}`);
    if (!m.id || idler.has(m.id)) h('kimlik yok ya da zaten var');
    if (!alanlar.has(m.alan)) h('alan geçersiz');
    for (const k of ['baslik', 'ar_baslik', 'konu', 'seviye']) if (!m[k]) h(k + ' eksik');
    if (!Array.isArray(m.ar) || !Array.isArray(m.tr) || m.ar.length !== m.tr.length || m.ar.length < 3) h('ar/tr paragrafları eşit değil');
    if (!Array.isArray(m.sozluk) || m.sozluk.length < 6 || m.sozluk.some(x => !x[0] || !x[1])) h('sözlük eksik');
    if (!Array.isArray(m.sorular) || m.sorular.length < 3) h('soru az');
    (m.sorular || []).forEach((q, i) => { if (!q.s || !Array.isArray(q.k) || q.k.length !== 4 || !(q.d >= 0 && q.d < 4)) h('soru ' + (i + 1) + ' bozuk'); if (q.a === undefined) q.a = ''; });
    idler.add(m.id); yeni.push(m);
  }
}
if (hatalar.length) { console.error(hatalar.join('\n')); process.exit(1); }
M.metinler.push(...yeni);
fs.writeFileSync(dosya, JSON.stringify(M));
const by = {}; M.metinler.forEach(m => by[m.alan] = (by[m.alan] || 0) + 1);
const w = yeni.map(m => m.ar.join(' ').split(/\s+/).length);
console.log(`${yeni.length} metin eklendi (ortalama ${Math.round(w.reduce((a, b) => a + b, 0) / (w.length || 1))} kelime). Alan başına:`, JSON.stringify(by));
