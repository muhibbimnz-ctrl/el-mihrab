// Dil sayfasının Hikâye Programı'na (D) bir hafta ekler ve HTML'deki ?v= damgasını tazeler.
// node tools/dil/gun_ekle.js farsca tools/dil/fa/hafta02.json
// Hafta dosyası: hikâye günlerinin dizisi ({title, read, dia, vocab, gram, say}); sona tekrar günü ({rev:1}) eklenir.
// Hafta 9'dan itibaren programda metin günü de vardır: dizide {txt:1} yazılırsa o da eklenir.
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const [ad, dosya] = process.argv.slice(2);
const kok = path.join(__dirname, '..', '..'), vf = path.join(kok, 'veri', ad + '.js'), hf = path.join(kok, ad + '.html');
const gunler = JSON.parse(fs.readFileSync(dosya, 'utf8'));
const hata = [];
gunler.forEach((g, i) => {
  if (g.rev || g.txt) return;
  for (const k of ['title', 'read', 'dia', 'vocab', 'gram', 'say']) if (!g[k] || (Array.isArray(g[k]) && !g[k].length)) hata.push(`gün ${i + 1}: ${k} eksik`);
  (g.read || []).forEach((r, j) => { if (r.length !== 2 || !r[0] || !r[1]) hata.push(`gün ${i + 1} okuma ${j + 1} bozuk`); });
  (g.dia || []).forEach((r, j) => { if (r.length !== 3 || r.some(x => !x)) hata.push(`gün ${i + 1} diyalog ${j + 1} bozuk`); });
  (g.vocab || []).forEach((r, j) => { if (r.length < 3 || !r[0] || !r[1] || !r[2]) hata.push(`gün ${i + 1} kelime ${j + 1} bozuk`); });
});
if (hata.length) { console.error(hata.join('\n')); process.exit(1); }
let s = fs.readFileSync(vf, 'utf8');
const bas = s.indexOf('var D=['), son = s.indexOf('\n];', bas);
if (bas < 0 || son < 0) { console.error('D dizisi bulunamadı'); process.exit(1); }
const ek = gunler.concat([{ rev: 1 }]).map(g => JSON.stringify(g)).join(',\n\n');
s = s.slice(0, son) + ',\n\n' + ek + s.slice(son);
fs.writeFileSync(vf, s);
// Kontrol: dosya çalışıyor mu, kaç gün oldu?
const o = {}; new Function('o', s + ';o.D=D')(o);
// Sürüm damgası (tools/dil_veri.py ile aynı: sha1'in ilk 10 hanesi)
const oz = crypto.createHash('sha1').update(fs.readFileSync(vf)).digest('hex').slice(0, 10);
let h = fs.readFileSync(hf, 'utf8');
const re = new RegExp('<script src="veri/' + ad + '\\.js(\\?v=[0-9a-f]*)?"></script>');
if (!re.test(h)) { console.error('HTML damgası bulunamadı'); process.exit(1); }
h = h.replace(re, '<script src="veri/' + ad + '.js?v=' + oz + '"></script>'); fs.writeFileSync(hf, h);
console.log(`${ad}: ${gunler.length} gün + tekrar eklendi; program şimdi ${o.D.length} gün; damga ${oz}`);
