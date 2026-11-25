/* Çocuk Köşesi — "Malazgirt 1071" sıra tabanlı strateji oyunu (8-12 yaş).
   Sultan Alparslan'ın ordusunu yönetirsin: 3 bölüm (Öncü çarpışması, Hilal taktiği, Meydan savaşı).
   Birlikler yenilince "geri çekilir"; kan ve şiddet ayrıntısı yoktur. Bölüm aralarında tarih ve din bilgisi verilir.
   cocuk.html ve cocuk-oyun.js'teki sayfa, esc, toast, bitti, konfeti, karis yardımcılarını kullanır. */
(function () {
'use strict';
if (!window.BUYUK_OYUN) return;
var css = document.createElement('style');
css.textContent = [
 '.mz-hik{background:linear-gradient(160deg,#1d3557,#2a6f6f 60%,#c9a227);color:#fff;border-radius:24px;padding:18px 16px;margin:6px 0 12px}',
 '.mz-hik h2{margin:0 0 6px;color:#ffe08a;font-size:22px}.mz-hik p{margin:0 0 8px;font-size:16.5px;line-height:1.55}.mz-hik .ay{background:rgba(255,255,255,.14);border-radius:14px;padding:8px 12px;font-size:15px}',
 '.mz-bol{display:grid;gap:10px}.mz-bol .btn{justify-content:flex-start;text-align:left;padding:12px 14px;font-size:17px}.mz-bol .btn small{display:block;font-weight:500;color:var(--muted);font-size:13.5px}.mz-bol .btn[disabled]{opacity:.45}',
 '.mz-ust{display:flex;align-items:center;gap:8px;margin:4px 0 8px;font-weight:800}.mz-ust .h{flex:1;font-size:15px}.mz-ust .t{background:var(--sunS);border-radius:999px;padding:3px 10px;font-size:13px}',
 '.mz-alan{position:relative;display:grid;gap:3px;padding:6px;border-radius:20px;background:linear-gradient(#8fbf6a,#6fa24f);box-shadow:inset 0 0 0 3px #5b8a3e;touch-action:manipulation;user-select:none}',
 '.mz-k{aspect-ratio:1;border-radius:8px;background:rgba(255,255,255,.10);position:relative;border:0;padding:0;cursor:pointer}',
 '.mz-k.tepe{background:rgba(120,85,40,.35)}.mz-k.tepe:after{content:"⛰";position:absolute;right:2px;bottom:0;font-size:11px;opacity:.7}',
 '.mz-k.kaya{background:rgba(60,60,60,.35);cursor:default}.mz-k.kaya:after{content:"🪨";position:absolute;inset:0;display:grid;place-items:center;font-size:20px}',
 '.mz-k.git{background:rgba(255,255,255,.55);box-shadow:inset 0 0 0 2px #fff}.mz-k.hed{background:rgba(239,71,111,.45);box-shadow:inset 0 0 0 2px #ef476f}',
 '.mz-b{position:absolute;inset:6%;border-radius:50%;display:grid;place-items:center;font-size:clamp(16px,5.4vw,26px);transition:transform .25s,opacity .4s;box-shadow:0 3px 0 rgba(0,0,0,.25)}',
 '.mz-b.biz{background:radial-gradient(circle at 35% 30%,#3ba57e,#1f6f52);border:2px solid #ffe08a}.mz-b.dus{background:radial-gradient(circle at 35% 30%,#9b6fd1,#5a3591);border:2px solid #e5d2ff}',
 '.mz-b.kom{border-width:3px}.mz-b.sec{transform:scale(1.12);box-shadow:0 0 0 3px #fff,0 3px 0 rgba(0,0,0,.25)}.mz-b.bitti{filter:grayscale(.7);opacity:.75}',
 '.mz-b i{position:absolute;left:8%;right:8%;bottom:-5px;height:5px;border-radius:3px;background:rgba(0,0,0,.35);overflow:hidden}.mz-b i b{display:block;height:100%;background:#ffe08a}',
 '.mz-b.dus i b{background:#ff8fab}.mz-b.vur{animation:mzVur .4s}.mz-b.git2{opacity:0;transform:scale(.4)}',
 '@keyframes mzVur{0%,100%{transform:none}25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}',
 '.mz-ok{position:absolute;font-size:18px;pointer-events:none;transition:all .35s linear;z-index:3}',
 '.mz-sayi{position:absolute;font-weight:800;color:#fff;text-shadow:0 1px 2px #000;font-size:15px;pointer-events:none;animation:mzSayi .9s forwards;z-index:4}',
 '@keyframes mzSayi{to{transform:translateY(-22px);opacity:0}}',
 '.mz-log{min-height:44px;font-size:14.5px;margin:8px 2px;color:var(--ink)}',
 '.mz-alt{display:flex;gap:8px}.mz-alt .btn{flex:1}',
 '.mz-bilgi{display:flex;gap:10px;align-items:center;background:var(--card);border:2px solid var(--line);border-radius:16px;padding:8px 12px;margin-top:8px;font-size:14px}.mz-bilgi b{font-size:15px}'
].join('\n');
document.head.appendChild(css);

var TUR = {
  okcu:   { e: '🏹', ad: 'Atlı okçu', can: 6, guc: 2, hiz: 3, menzil: 3, not: 'Uzaktan ok atar, hızlıdır.' },
  suvari: { e: '🐎', ad: 'Süvari', can: 8, guc: 3, hiz: 3, menzil: 1, not: 'Hamle yapıp saldırırsa +1 güç.' },
  piyade: { e: '🛡️', ad: 'Mızraklı', can: 10, guc: 2, hiz: 2, menzil: 1, not: 'Dayanıklıdır, yavaştır.' },
  kom:    { e: '🌙', ad: 'Sultan Alparslan', can: 12, guc: 3, hiz: 2, menzil: 1, not: 'Komutan. Yanındaki birliklere +1 güç verir. Yenilirse bölüm kaybedilir.' },
  bpiy:   { e: '🛡️', ad: 'Bizans piyadesi', can: 9, guc: 2, hiz: 2, menzil: 1 },
  bsuv:   { e: '🐎', ad: 'Bizans ağır süvarisi', can: 10, guc: 3, hiz: 2, menzil: 1 },
  bok:    { e: '🏹', ad: 'Bizans okçusu', can: 5, guc: 2, hiz: 2, menzil: 3 },
  bkom:   { e: '👑', ad: 'İmparator Romanos Diogenes', can: 14, guc: 3, hiz: 1, menzil: 1 }
};
var S = 7, R = 9; /* sütun, satır */
var BOL = [
  { ad: '1. Öncü çarpışması', alt: 'Bizans öncü birliklerini geri püskürt', hedef: 'Bütün Bizans birliklerini geri çekilmeye zorla.',
    once: ['Yıl 1071. Bizans İmparatoru Romanos Diogenes çok büyük bir orduyla Anadolu’ya geldi. Sultan Alparslan’ın askeri ondan çok azdı.', 'İlk iş, öncü birlikleri karşılamak. Okçularını uzakta tut, mızraklıları öne sür!'],
    biz: [['okcu', 1, 7], ['okcu', 5, 7], ['piyade', 3, 6], ['kom', 3, 8]], dus: [['bpiy', 2, 1], ['bpiy', 4, 1], ['bok', 3, 0], ['bsuv', 1, 2]],
    tepe: [[0, 4], [6, 4], [3, 4]], kaya: [[1, 5], [5, 5]] },
  { ad: '2. Hilal taktiği', alt: 'Geri çekiliyormuş gibi yap, yanlardan kuşat', hedef: 'Düşman ortaya çekilince yanlardaki pusu birlikleri çıkar. Bütün düşmanı geri çekilmeye zorla.',
    once: ['Alparslan ordusunu hilal (yarım ay) gibi dizdi. Ortadaki birlikler geri çekiliyormuş gibi yaptı; Bizans ordusu peşlerinden koştu.', 'Düşman ortaya gelince iki yanda saklanan Türk süvarileri çıkıp onları kuşattı. Ortadaki birliklerinle düşmanı çek: 3. turda pusu birliklerin gelecek!'],
    biz: [['piyade', 3, 4], ['okcu', 2, 6], ['okcu', 4, 6], ['kom', 3, 8]], pusu: [['suvari', 0, 2], ['suvari', 6, 2], ['okcu', 0, 5], ['okcu', 6, 5]],
    dus: [['bpiy', 2, 1], ['bpiy', 3, 1], ['bpiy', 4, 1], ['bsuv', 1, 0], ['bsuv', 5, 0], ['bok', 3, 0]],
    tepe: [[0, 3], [6, 3]], kaya: [] },
  { ad: '3. Meydan savaşı', alt: 'İmparatoru esir al', hedef: 'İmparator Romanos Diogenes’in (👑) gücünü bitir; o teslim olunca zafer kazanılır.',
    once: ['26 Ağustos 1071, cuma günü. Alparslan cuma namazını kıldı, ordusuyla birlikte dua etti. Beyaz elbiseler giydi ve “Şehit düşersem bu elbise kefenim olsun” dedi.', 'Şimdi son hamle: İmparatorun etrafındaki muhafızları aş ve onu teslim olmaya zorla!'],
    biz: [['suvari', 1, 6], ['suvari', 5, 6], ['okcu', 2, 7], ['okcu', 4, 7], ['piyade', 3, 6], ['kom', 3, 8]],
    dus: [['bkom', 3, 0], ['bpiy', 2, 1], ['bpiy', 4, 1], ['bsuv', 1, 2], ['bsuv', 5, 2], ['bok', 3, 1]],
    tepe: [[3, 4], [0, 5], [6, 5]], kaya: [[2, 3], [4, 3]] }
];
var SONRA = [
  'Öncü birlikler geri çekildi. Malazgirt Ovası’nda büyük karşılaşmanın vakti yaklaşıyor.',
  'Hilal taktiği işe yaradı! Bizans ordusu dağıldı. Bu taktik, Türk savaş tarihinin en ünlü taktiklerinden biridir.',
  'Zafer! İmparator esir alındı. Sultan Alparslan ona hükümdarlara yakışır biçimde davrandı, sonra onu hediyelerle serbest bıraktı. Kur’an’ın öğrettiği merhamet ve adaletin örneğiydi. Bu zaferle Anadolu’nun kapıları Müslüman Türklere açıldı.'
];
var SORU = [
  { q: 'Malazgirt Savaşı hangi yıl yapıldı?', c: ['1071', '1453', '1923', '1299'], d: '1071' },
  { q: 'Alparslan savaştan önce hangi namazı kıldı?', c: ['Cuma namazı', 'Bayram namazı', 'Teravih', 'Cenaze namazı'], d: 'Cuma namazı' },
  { q: 'Alparslan esir aldığı imparatora nasıl davrandı?', c: ['Ona iyi davranıp serbest bıraktı', 'Zindana attı', 'Ceza verdi', 'Sürgüne gönderdi'], d: 'Ona iyi davranıp serbest bıraktı' }
];

var O = null; /* oyun durumu */
function anahtar(x, y) { return x + ',' + y; }
var ZOR = [0.6, 1.0, 1.2];
function birlik(t, x, y, taraf) { var T = TUR[t], c = taraf === 'dus' ? Math.max(3, Math.round(T.can * ZOR[O.i])) : T.can; return { t: t, x: x, y: y, taraf: taraf, can: c, max: c, hareket: false, saldiri: false, id: Math.random().toString(36).slice(2) }; }
function bul(x, y) { for (var i = 0; i < O.b.length; i++) { var b = O.b[i]; if (b.can > 0 && b.x === x && b.y === y) return b; } return null; }
function mesafe(a, b) { return Math.abs(a.x - b.x) + Math.abs(a.y - b.y); }
function engel(x, y) { return x < 0 || y < 0 || x >= S || y >= R || O.kaya[anahtar(x, y)]; }
function ulasilir(b) { /* BFS: hız kadar adım, birliklerin içinden geçilmez */
  var hiz = TUR[b.t].hiz, gor = {}, q = [[b.x, b.y, 0]], sonuc = []; gor[anahtar(b.x, b.y)] = 1;
  while (q.length) { var c = q.shift(); [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(function (d) {
    var nx = c[0] + d[0], ny = c[1] + d[1], k = anahtar(nx, ny); if (gor[k] || engel(nx, ny) || bul(nx, ny) || c[2] + 1 > hiz) return;
    gor[k] = 1; sonuc.push([nx, ny]); q.push([nx, ny, c[2] + 1]); }); }
  return sonuc; }
function hedefler(b) { return O.b.filter(function (x) { return x.can > 0 && x.taraf !== b.taraf && mesafe(x, b) <= TUR[b.t].menzil; }); }
function guc(a, h) { var g = TUR[a.t].guc;
  if (a.taraf === 'biz' && a.t !== 'kom' && O.b.some(function (k) { return k.can > 0 && k.t === 'kom' && mesafe(k, a) === 1; })) g++;
  if (a.t === 'suvari' && a.hareket) g++;
  if (TUR[a.t].menzil > 1 && mesafe(a, h) === 1) g = Math.max(1, g - 1); /* okçu yakında zayıf */
  if (O.tepe[anahtar(h.x, h.y)]) g = Math.max(1, g - 1); /* tepedeki birlik korunur */
  return g + (Math.random() < .3 ? 1 : 0); }

function bolumSec() {
  var ac = (function () { try { return JSON.parse(localStorage.getItem('cocuk.malazgirt') || '1'); } catch (e) { return 1; } })();
  sayfa('Malazgirt 1071', '<div class="mz-hik"><h2>⚔️ Malazgirt 1071</h2><p>Sultan Alparslan’ın ordusunu sen yönetiyorsun! Birliklerini akıllıca yerleştir, Bizans ordusunu yen ve Anadolu’nun kapılarını aç.</p>' +
    '<div class="ay">“Nice az topluluk, Allah’ın izniyle çok topluluğa galip gelmiştir. Allah sabredenlerle beraberdir.” <b>(Bakara, 249)</b></div></div>' +
    '<div class="mz-bol">' + BOL.map(function (b, i) { return '<button class="btn" data-b="' + i + '"' + (i + 1 > ac ? ' disabled' : '') + '><span>' + (i + 1 > ac ? '🔒 ' : '') + '<b>' + b.ad + '</b><small>' + b.alt + '</small></span></button>'; }).join('') + '</div>' +
    '<div class="akil"><b>Nasıl oynanır?</b><ul><li>Kendi birliğine dokun: gidebileceği yerler beyaz, saldırabileceği düşmanlar kırmızı yanar.</li><li>Her birlik turda bir kez yürür ve bir kez saldırır. Bitince “Turu bitir”e dokun.</li><li>🏹 okçular uzaktan vurur, 🐎 süvari koşarak saldırınca güçlenir, 🌙 Sultan yanındakileri güçlendirir. ⛰ tepedeki birlik daha az zarar görür.</li></ul></div>', '#oyun');
  [].forEach.call(document.querySelectorAll('[data-b]'), function (b) { b.onclick = function () { location.hash = 'oyun/malazgirt-' + b.dataset.b; }; });
}
function onHikaye(i) {
  var B = BOL[i];
  sayfa(B.ad, '<div class="mz-hik"><h2>' + B.ad + '</h2>' + B.once.map(function (p) { return '<p>' + esc(p) + '</p>'; }).join('') + '<div class="ay">🎯 ' + esc(B.hedef) + '</div></div><button class="btn pri" id="mzBas" style="width:100%">⚔️ Savaşa başla</button>', '#oyun/malazgirt');
  document.getElementById('mzBas').onclick = function () { kur(i); };
}
function kur(i) {
  var B = BOL[i]; O = { i: i, b: [], tur: 1, sec: null, kilit: false, tepe: {}, kaya: {}, pusu: (B.pusu || []).slice() };
  B.tepe.forEach(function (t) { O.tepe[anahtar(t[0], t[1])] = 1; }); B.kaya.forEach(function (t) { O.kaya[anahtar(t[0], t[1])] = 1; });
  B.biz.forEach(function (u) { O.b.push(birlik(u[0], u[1], u[2], 'biz')); }); B.dus.forEach(function (u) { O.b.push(birlik(u[0], u[1], u[2], 'dus')); });
  sayfa(B.ad, '<div class="mz-ust"><span class="h">🎯 ' + B.alt + '</span><span class="t" id="mzTur"></span></div><div class="mz-alan" id="mzA" style="grid-template-columns:repeat(' + S + ',1fr)"></div>' +
    '<div class="mz-log" id="mzLog">Bir birliğine dokun.</div><div class="mz-alt"><button class="btn pri" id="mzBit">Turu bitir ⏭</button><button class="btn" id="mzYeni">↻</button></div><div id="mzBil"></div>', '#oyun/malazgirt');
  document.getElementById('mzBit').onclick = function () { if (!O.kilit) dusmanTuru(); };
  document.getElementById('mzYeni').onclick = function () { if (confirm('Bölüm baştan başlasın mı?')) kur(i); };
  ciz(); log('Tur 1 · ' + B.hedef);
}
function log(t) { var l = document.getElementById('mzLog'); if (l) l.textContent = t; }
function ciz() {
  var A = document.getElementById('mzA'); if (!A) return; var git = {}, hed = {}, s = O.sec;
  if (s && !s.hareket) ulasilir(s).forEach(function (c) { git[anahtar(c[0], c[1])] = 1; });
  if (s && !s.saldiri) hedefler(s).forEach(function (h) { hed[anahtar(h.x, h.y)] = 1; });
  var h = '';
  for (var y = 0; y < R; y++) for (var x = 0; x < S; x++) {
    var k = anahtar(x, y), b = bul(x, y), cl = 'mz-k' + (O.tepe[k] ? ' tepe' : '') + (O.kaya[k] ? ' kaya' : '') + (git[k] ? ' git' : '') + (hed[k] ? ' hed' : '');
    h += '<button class="' + cl + '" data-x="' + x + '" data-y="' + y + '" aria-label="kare">' + (b ? '<span class="mz-b ' + b.taraf + (b.t === 'kom' || b.t === 'bkom' ? ' kom' : '') + (b === s ? ' sec' : '') + (b.taraf === 'biz' && b.hareket && b.saldiri ? ' bitti' : '') + '" data-id="' + b.id + '">' + TUR[b.t].e + '<i><b style="width:' + Math.round(b.can / b.max * 100) + '%"></b></i></span>' : '') + '</button>';
  }
  A.innerHTML = h; document.getElementById('mzTur').textContent = 'Tur ' + O.tur;
  [].forEach.call(A.querySelectorAll('.mz-k'), function (c) { c.onclick = function () { dokun(+c.dataset.x, +c.dataset.y); }; });
  var bi = document.getElementById('mzBil'); if (bi) { var g = s || null; bi.innerHTML = g ? '<div class="mz-bilgi"><span style="font-size:26px">' + TUR[g.t].e + '</span><span><b>' + TUR[g.t].ad + '</b> · güç ' + TUR[g.t].guc + ' · can ' + g.can + '/' + g.max + '<br>' + (TUR[g.t].not || '') + '</span></div>' : ''; }
}
function konum(b) { var A = document.getElementById('mzA'), e = A && A.querySelector('[data-id="' + b.id + '"]'); if (!e) return null; var r = e.getBoundingClientRect(), a = A.getBoundingClientRect(); return { x: r.left - a.left + r.width / 2, y: r.top - a.top + r.height / 2, el: e }; }
function vur(a, h, bitince) {
  var A = document.getElementById('mzA'), p1 = konum(a), p2 = konum(h), g = guc(a, h);
  var son = function () { h.can = Math.max(0, h.can - g); var p = konum(h);
    if (p) { p.el.classList.add('vur'); var n = document.createElement('div'); n.className = 'mz-sayi'; n.textContent = '−' + g; n.style.left = (p.x - 8) + 'px'; n.style.top = (p.y - 20) + 'px'; A.appendChild(n); setTimeout(function () { n.remove(); }, 900); }
    setTimeout(function () { if (h.can <= 0) { var q = konum(h); if (q) q.el.classList.add('git2'); }
      setTimeout(function () { ciz(); bitince && bitince(g); }, h.can <= 0 ? 380 : 120); }, 280); };
  if (TUR[a.t].menzil > 1 && p1 && p2 && A) { var o = document.createElement('div'); o.className = 'mz-ok'; o.textContent = '➶'; o.style.left = p1.x + 'px'; o.style.top = p1.y + 'px'; A.appendChild(o);
    requestAnimationFrame(function () { o.style.left = p2.x + 'px'; o.style.top = p2.y + 'px'; }); setTimeout(function () { o.remove(); son(); }, 360); }
  else son();
}
function dokun(x, y) {
  if (O.kilit) return; var b = bul(x, y), s = O.sec;
  if (b && b.taraf === 'biz') { O.sec = b === s ? null : b; ciz(); if (O.sec) log(TUR[b.t].ad + (b.hareket && b.saldiri ? ' bu tur işini bitirdi.' : ' seçildi.')); return; }
  if (!s) { if (b) log(TUR[b.t].ad + ' · can ' + b.can + '/' + b.max); return; }
  if (b && b.taraf === 'dus') {
    if (s.saldiri || mesafe(s, b) > TUR[s.t].menzil) { log('Bu düşman menzil dışında.'); return; }
    O.kilit = true; s.saldiri = true; s.hareket = true;
    vur(s, b, function (g) { log(TUR[s.t].ad + ' saldırdı (−' + g + ').' + (b.can <= 0 ? ' ' + TUR[b.t].ad + ' geri çekildi!' : '')); O.kilit = false; kontrol(); });
    return; }
  if (!b && !s.hareket && ulasilir(s).some(function (c) { return c[0] === x && c[1] === y; })) {
    s.x = x; s.y = y; s.hareket = true; if (!hedefler(s).length) s.saldiri = true; ciz();
    log(hedefler(s).length ? 'Şimdi kırmızı yanan düşmana saldırabilirsin.' : TUR[s.t].ad + ' yerini aldı.'); }
}
function kontrol() {
  var dus = O.b.filter(function (b) { return b.taraf === 'dus' && b.can > 0; }), kom = O.b.filter(function (b) { return b.t === 'kom' && b.can > 0; });
  if (O.i === 2 && !O.b.some(function (b) { return b.t === 'bkom' && b.can > 0; })) return zafer();
  if (!dus.length && !O.pusuDus) return zafer();
  if (!kom.length) return yenilgi('Sultan geri çekilmek zorunda kaldı.');
  return false;
}
function dusmanTuru() {
  O.kilit = true; O.sec = null; ciz(); log('Bizans ordusu hamle yapıyor…');
  var D = O.b.filter(function (b) { return b.taraf === 'dus' && b.can > 0; }), i = 0;
  (function sira() {
    if (i >= D.length || !document.getElementById('mzA')) return turBasi();
    var d = D[i++]; if (d.can <= 0) return sira();
    var biz = O.b.filter(function (b) { return b.taraf === 'biz' && b.can > 0; }); if (!biz.length) return turBasi();
    var hedef = biz.sort(function (a, b) { return (mesafe(a, d) - mesafe(b, d)) || (a.can - b.can); })[0];
    if (d.t === 'bkom' && mesafe(hedef, d) > 2) { /* imparator yerinden ayrılmaz */ return setTimeout(sira, 60); }
    if (mesafe(hedef, d) > TUR[d.t].menzil) {
      var en = null, em = 1e9; ulasilir(d).forEach(function (c) { var m = Math.abs(c[0] - hedef.x) + Math.abs(c[1] - hedef.y); if (TUR[d.t].menzil > 1 && m < 2) m = 5; if (m < em) { em = m; en = c; } });
      if (en && em < mesafe(hedef, d)) { d.x = en[0]; d.y = en[1]; ciz(); } }
    var hs = hedefler(d); if (hs.length) { var h = hs.sort(function (a, b) { return a.can - b.can; })[0];
      setTimeout(function () { vur(d, h, function () { if (kontrol()) return; setTimeout(sira, 220); }); }, 260); }
    else setTimeout(sira, 220);
  })();
}
function turBasi() {
  if (kontrol()) return; O.tur++;
  O.b.forEach(function (b) { if (b.taraf === 'biz') { b.hareket = false; b.saldiri = false; } });
  if (O.pusu.length && O.tur >= 3) { O.pusu.forEach(function (u) { var x = u[1], y = u[2]; if (bul(x, y)) { y = Math.min(R - 1, y + 1); } if (!bul(x, y) && !engel(x, y)) O.b.push(birlik(u[0], x, y, 'biz')); }); O.pusu = [];
    toast('🌙 Pusu birlikleri yanlardan çıktı! Hilal kapandı.'); }
  O.kilit = false; ciz(); log('Tur ' + O.tur + ' · Sıra sende.');
}
function zafer() {
  O.kilit = true; var i = O.i; try { var a = JSON.parse(localStorage.getItem('cocuk.malazgirt') || '1'); if (i + 2 > a) localStorage.setItem('cocuk.malazgirt', JSON.stringify(Math.min(3, i + 2))); } catch (e) {}
  var y = bitti('g:malazgirt-' + i, i === 2 ? 3 : 2); konfeti();
  setTimeout(function () {
    var s = SORU[i], sec = karis(s.c);
    sayfa('Zafer!', '<div class="mz-hik"><h2>🏆 ' + (i === 2 ? 'Malazgirt Zaferi!' : 'Bölüm kazanıldı!') + '</h2><p>' + esc(SONRA[i]) + '</p>' + (y ? '<div class="ay">⭐ ' + (i === 2 ? 3 : 2) + ' yıldız kazandın!</div>' : '') + '</div>' +
      '<div class="card"><div class="q" style="font-weight:800;margin-bottom:8px">🎓 Bilgi sorusu: ' + esc(s.q) + '</div><div class="mz-bol" id="mzS">' + sec.map(function (c) { return '<button class="btn" data-c="' + esc(c) + '">' + esc(c) + '</button>'; }).join('') + '</div></div>' +
      '<div class="mz-alt">' + (i < 2 ? '<button class="btn pri" id="mzSon">Sonraki bölüm ›</button>' : '<button class="btn pri" id="mzBas2">Bölümlere dön</button>') + '</div>', '#oyun/malazgirt');
    [].forEach.call(document.querySelectorAll('#mzS [data-c]'), function (b) { b.onclick = function () { var ok = b.dataset.c === s.d; b.classList.add(ok ? 'ok' : 'bad'); toast(ok ? 'Doğru! Mâşallah 🌟' : 'Doğrusu: ' + s.d); [].forEach.call(document.querySelectorAll('#mzS [data-c]'), function (x) { x.disabled = true; if (x.dataset.c === s.d) x.classList.add('ok'); }); }; });
    var n = document.getElementById('mzSon'); if (n) n.onclick = function () { location.hash = 'oyun/malazgirt-' + (i + 1); };
    var g = document.getElementById('mzBas2'); if (g) g.onclick = function () { location.hash = 'oyun/malazgirt'; };
  }, 900);
}
function yenilgi(neden) {
  O.kilit = true;
  setTimeout(function () { sayfa('Tekrar dene', '<div class="mz-hik"><h2>Bu sefer olmadı</h2><p>' + esc(neden) + ' Sabırlı ol ve taktiğini değiştir: okçularını geride tut, Sultan’ı koru, tepeleri kullan.</p><div class="ay">“Ey iman edenler! Sabredin, sabırda yarışın.” <b>(Âl-i İmrân, 200)</b></div></div><button class="btn pri" id="mzTek" style="width:100%">↻ Yeniden dene</button>', '#oyun/malazgirt');
    document.getElementById('mzTek').onclick = function () { kur(O.i); }; }, 700);
}

var BO = window.BUYUK_OYUN;
BO.tiles.push(['malazgirt', '⚔️', 'Malazgirt 1071', 'Alparslan’ın ordusunu yönet, hilal taktiğiyle zafer kazan', '#1d3557', '8-12 yaş']);
BO.calis.malazgirt = bolumSec;
[0, 1, 2].forEach(function (i) { BO.calis['malazgirt-' + i] = function () { onHikaye(i); }; });
})();
