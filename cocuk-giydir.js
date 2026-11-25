/* Çocuk Köşesi — "Namaza Hazırlan" giydirme oyunu (kız ve erkek).
   Çocuk kıyafet seçer, "Hazırım" der; namaz örtüsü (Hanefî) kurallarına göre geri bildirim alır.
   cocuk.html ve cocuk-oyun.js'teki sayfa, esc, toast, bitti, konfeti yardımcılarını kullanır. */
(function () {
'use strict';
if (!window.BUYUK_OYUN) return;
var css = document.createElement('style');
css.textContent = [
 '.gy-sec{display:grid;grid-template-columns:1fr 1fr;gap:12px}.gy-sec .btn{flex-direction:column;padding:18px 10px;font-size:20px}.gy-sec .btn span{font-size:54px;line-height:1}',
 '.gy{display:grid;grid-template-columns:minmax(0,1fr);gap:10px}',
 '.gy-ayna{background:linear-gradient(#e9f5ff,#fff7e8);border:2px solid var(--line);border-radius:24px;display:grid;place-items:center;padding:6px}.gy-ayna svg{width:min(62vw,250px);height:auto;display:block}',
 '.gy-k{font-weight:800;color:var(--muted);font-size:14px;margin:4px 2px 4px}',
 '.gy-r{display:flex;gap:8px;overflow-x:auto;padding:2px 2px 6px}.gy-r .btn{flex:none;padding:8px 12px;font-size:15px}.gy-r .btn.on{background:var(--priS);border-color:var(--pri);color:var(--pri)}',
 '.gy-renk{display:flex;gap:8px;margin:2px 2px 6px}.gy-renk button{width:30px;height:30px;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 2px var(--line);cursor:pointer}.gy-renk button.on{box-shadow:0 0 0 3px var(--ink)}',
 '.gy-sonuc{border-radius:20px;padding:12px 14px;margin:8px 0;font-size:16px}.gy-sonuc.ok{background:var(--okS)}.gy-sonuc.no{background:var(--sunS)}.gy-sonuc ul{margin:6px 0 0;padding-left:20px}',
 '@media(min-width:620px){.gy{grid-template-columns:260px 1fr;align-items:start}}'
].join('\n');
document.head.appendChild(css);

var TEN = '#f1c7a5', TEN2 = '#e2ad88';
var RENK = ['#1f8a70', '#3a86ff', '#ef476f', '#8338ec', '#f4a261', '#ffffff', '#264653'];
var PARCA = {
  kiz: {
    bas: [['yok', 'Açık saç'], ['ortu', 'Başörtüsü'], ['toka', 'Saç tokası']],
    ust: [['atlet', 'Kolsuz bluz'], ['kisa', 'Kısa kollu'], ['uzun', 'Uzun kollu'], ['tunik', 'Uzun tunik']],
    alt: [['sort', 'Şort'], ['kisaetek', 'Kısa etek'], ['etek', 'Uzun etek'], ['pantolon', 'Pantolon']]
  },
  erkek: {
    bas: [['yok', 'Başı açık'], ['takke', 'Takke'], ['sapka', 'Şapka']],
    ust: [['atlet', 'Atlet'], ['kisa', 'Tişört'], ['uzun', 'Gömlek'], ['entari', 'Uzun entari']],
    alt: [['sort', 'Kısa şort'], ['bermuda', 'Diz altı şort'], ['pantolon', 'Pantolon'], ['salvar', 'Şalvar']]
  }
};
function koyu(c) { return c === '#ffffff' ? '#d9d9d9' : 'rgba(0,0,0,.18)'; }

function ciz(c, k) {
  var s = '', U = k.ustR, A = k.altR, B = k.basR, kz = c === 'kiz';
  /* bacaklar ve ayaklar */
  s += '<rect x="96" y="198" width="20" height="92" rx="9" fill="' + TEN + '"/><rect x="124" y="198" width="20" height="92" rx="9" fill="' + TEN + '"/>';
  s += '<ellipse cx="104" cy="294" rx="15" ry="7" fill="#6d4c41"/><ellipse cx="136" cy="294" rx="15" ry="7" fill="#6d4c41"/>';
  /* alt giysi */
  if (k.alt === 'sort') s += '<path d="M90 194h60v34h-26l-4-14-4 14H90z" fill="' + A + '" stroke="' + koyu(A) + '"/>';
  if (k.alt === 'kisaetek') s += '<path d="M92 194h56l14 38H78z" fill="' + A + '" stroke="' + koyu(A) + '"/>';
  if (k.alt === 'bermuda') s += '<path d="M90 194h60v62h-26l-4-40-4 40H90z" fill="' + A + '" stroke="' + koyu(A) + '"/>';
  if (k.alt === 'etek') s += '<path d="M92 194h56l24 94H68z" fill="' + A + '" stroke="' + koyu(A) + '"/><path d="M84 270h72" stroke="' + koyu(A) + '" stroke-width="3"/>';
  if (k.alt === 'pantolon') s += '<path d="M90 194h60l-4 94h-22l-4-70-4 70H94z" fill="' + A + '" stroke="' + koyu(A) + '"/>';
  if (k.alt === 'salvar') s += '<path d="M88 194h64l4 70q-6 22-30 22l-6-60-6 60q-24 0-30-22z" fill="' + A + '" stroke="' + koyu(A) + '"/><path d="M90 280h22M128 280h22" stroke="' + koyu(A) + '" stroke-width="4"/>';
  /* kollar (ten) */
  s += '<rect x="64" y="112" width="20" height="88" rx="10" fill="' + TEN + '"/><rect x="156" y="112" width="20" height="88" rx="10" fill="' + TEN + '"/>';
  s += '<circle cx="74" cy="204" r="9" fill="' + TEN + '"/><circle cx="166" cy="204" r="9" fill="' + TEN + '"/>';
  /* alt atlet (her zaman) */
  s += '<path d="M86 110h68l2 90H84z" fill="#fdfdfd" stroke="#ddd"/>';
  /* üst giysi */
  var govde = function (alt) { return '<path d="M84 108h72l' + (alt > 210 ? '10 ' + (alt - 108) + 'H74' : '2 ' + (alt - 108) + 'H82') + 'z" fill="' + U + '" stroke="' + koyu(U) + '"/>'; };
  if (k.ust === 'atlet') s += '<path d="M90 108h12q18 14 36 0h12l4 92H86z" fill="' + U + '" stroke="' + koyu(U) + '"/>';
  if (k.ust === 'kisa') s += govde(202) + '<rect x="60" y="108" width="28" height="36" rx="10" fill="' + U + '" stroke="' + koyu(U) + '"/><rect x="152" y="108" width="28" height="36" rx="10" fill="' + U + '" stroke="' + koyu(U) + '"/>';
  if (k.ust === 'uzun' || k.ust === 'tunik' || k.ust === 'entari') {
    var boy = k.ust === 'uzun' ? 204 : k.ust === 'tunik' ? 250 : 288;
    s += govde(boy) + '<rect x="60" y="108" width="28" height="94" rx="11" fill="' + U + '" stroke="' + koyu(U) + '"/><rect x="152" y="108" width="28" height="94" rx="11" fill="' + U + '" stroke="' + koyu(U) + '"/>';
    if (k.ust === 'uzun' && !kz) s += '<path d="M120 112v88" stroke="' + koyu(U) + '" stroke-width="2"/><circle cx="120" cy="130" r="2" fill="' + koyu(U) + '"/><circle cx="120" cy="155" r="2" fill="' + koyu(U) + '"/><circle cx="120" cy="180" r="2" fill="' + koyu(U) + '"/>';
    if (k.ust === 'entari') s += '<path d="M120 110v30" stroke="' + koyu(U) + '" stroke-width="3"/>';
  }
  /* boyun */
  s += '<rect x="111" y="96" width="18" height="16" fill="' + TEN2 + '"/>';
  /* baş */
  var yuz = function (cx, cy) { return '<circle cx="' + (cx - 10) + '" cy="' + (cy - 2) + '" r="3.4" fill="#2b2a33"/><circle cx="' + (cx + 10) + '" cy="' + (cy - 2) + '" r="3.4" fill="#2b2a33"/><path d="M' + (cx - 9) + ' ' + (cy + 11) + 'q9 8 18 0" fill="none" stroke="#b5534b" stroke-width="3" stroke-linecap="round"/><circle cx="' + (cx - 17) + '" cy="' + (cy + 7) + '" r="4" fill="#f4a4a4" opacity=".55"/><circle cx="' + (cx + 17) + '" cy="' + (cy + 7) + '" r="4" fill="#f4a4a4" opacity=".55"/>'; };
  if (kz && k.bas === 'ortu') {
    s += '<path d="M76 74a44 44 0 0 1 88 0v14q4 30-12 52H88q-16-22-12-52z" fill="' + B + '" stroke="' + koyu(B) + '"/>';
    s += '<ellipse cx="120" cy="76" rx="25" ry="29" fill="' + TEN + '"/>' + yuz(120, 76);
    s += '<path d="M95 66q25-18 50 0" fill="none" stroke="' + koyu(B) + '" stroke-width="2"/>';
  } else {
    if (kz) s += '<path d="M84 64q-6 60 6 82h60q12-22 6-82z" fill="#6d3f1f"/>';
    s += '<circle cx="120" cy="70" r="34" fill="' + TEN + '"/>';
    s += kz ? '<path d="M86 66q4-34 34-34t34 34q-18-16-34-14-16-2-34 14z" fill="#6d3f1f"/>' : '<path d="M86 62q2-30 34-30t34 30q-14-10-34-10t-34 10z" fill="#4a2c17"/>';
    s += yuz(120, 74);
    if (kz && k.bas === 'toka') s += '<path d="M142 44l12-6 4 10-12 4z" fill="' + B + '" stroke="' + koyu(B) + '"/>';
    if (!kz && k.bas === 'takke') s += '<path d="M88 52a32 22 0 0 1 64 0z" fill="' + B + '" stroke="' + koyu(B) + '"/><path d="M92 48h56" stroke="' + koyu(B) + '" stroke-dasharray="3 3"/>';
    if (!kz && k.bas === 'sapka') s += '<path d="M88 54a32 26 0 0 1 64 0z" fill="' + B + '"/><path d="M146 54h26q0 6-10 6h-16z" fill="' + B + '" stroke="' + koyu(B) + '"/>';
  }
  return '<svg viewBox="40 20 160 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Giydirilen çocuk">' + s + '</svg>';
}

function kontrol(c, k) {
  var e = [], bonus = [];
  if (c === 'kiz') {
    if (k.bas !== 'ortu') e.push('Saçların görünüyor. Namazda başörtüsüyle saç ve boyun örtülür.');
    if (k.ust === 'atlet' || k.ust === 'kisa') e.push('Kolların açık kaldı. Kollar bileklere kadar örtülür; eller açık olabilir.');
    if (k.alt === 'sort' || k.alt === 'kisaetek') e.push('Bacakların görünüyor. Uzun etek ya da pantolon giymelisin.');
    if (k.alt === 'pantolon' && k.ust !== 'tunik') bonus.push('Pantolonun üstüne uzun tunik giyersen daha güzel olur.');
  } else {
    var uzunAlt = k.alt === 'pantolon' || k.alt === 'salvar' || k.ust === 'entari';
    if (!uzunAlt) e.push(k.alt === 'bermuda' ? 'Şort dizini tam örtmüyor. Erkekler göbekten dizin altına kadar örtünür; diz de örtülür.' : 'Bacakların açık. Erkekler göbekten dizin altına kadar örtünür.');
    if (k.ust === 'atlet') bonus.push('Atletle de namaz olur ama Allah’ın huzuruna gömlek ya da tişörtle çıkmak daha edepli.');
    if (k.bas !== 'takke') bonus.push('Takke takmak Peygamberimizin âdetiydi; istersen tak.');
    if (k.bas === 'sapka') bonus.push('Şapka siperliği secdede alnı engelleyebilir; namazda çıkarmak daha iyi.');
  }
  return { e: e, b: bonus };
}

function sec() {
  sayfa('Namaza Hazırlan', '<h1>🧕 Namaza Hazırlan</h1><p class="lead">Çocuğu namaz için giydir, sonra “Hazırım!”a dokun. Doğru giydirirsen yıldız kazanırsın.</p>' +
    '<div class="gy-sec"><button class="btn" data-c="kiz"><span>👧</span>Kız çocuk</button><button class="btn" data-c="erkek"><span>👦</span>Erkek çocuk</button></div>' +
    '<div class="akil"><b>Biliyor musun?</b><ul><li>Kızlar namazda yüzleri, elleri ve ayakları dışında bütün bedenlerini örter.</li><li>Erkekler göbekleri ile dizleri arasını örter; diz de buna dâhildir.</li><li>Temiz ve güzel giyinmek Allah’ın huzuruna çıkmanın edebidir.</li></ul></div>', '#oyun');
  [].forEach.call(document.querySelectorAll('[data-c]'), function (b) { b.onclick = function () { location.hash = 'oyun/giydir-' + b.dataset.c; }; });
}

function oyna(c) {
  var P = PARCA[c], k = { bas: 'yok', ust: 'atlet', alt: 'sort', basR: c === 'kiz' ? RENK[3] : '#ffffff', ustR: RENK[1], altR: RENK[6] };
  var ad = c === 'kiz' ? 'Kız çocuk' : 'Erkek çocuk';
  sayfa('Namaza Hazırlan', '<h1>' + (c === 'kiz' ? '👧' : '👦') + ' ' + ad + '</h1><div class="gy"><div class="gy-ayna" id="ay"></div><div id="sc"></div></div><div id="sn"></div>' +
    '<div style="display:flex;gap:10px;margin-top:10px"><button class="btn pri" id="hz" style="flex:1">🕌 Hazırım!</button><button class="btn" id="dg">' + (c === 'kiz' ? '👦 Erkek' : '👧 Kız') + '</button></div>', '#oyun/giydir');
  var grup = [['bas', c === 'kiz' ? 'Baş' : 'Baş', 'basR'], ['ust', 'Üst', 'ustR'], ['alt', 'Alt', 'altR']];
  function yaz() {
    document.getElementById('ay').innerHTML = ciz(c, k);
    document.getElementById('sc').innerHTML = grup.map(function (g) {
      return '<div class="gy-k">' + g[1] + '</div><div class="gy-r">' + P[g[0]].map(function (p) { return '<button class="btn' + (k[g[0]] === p[0] ? ' on' : '') + '" data-g="' + g[0] + '" data-v="' + p[0] + '">' + esc(p[1]) + '</button>'; }).join('') + '</div>' +
        '<div class="gy-renk">' + RENK.map(function (r) { return '<button style="background:' + r + '" class="' + (k[g[2]] === r ? 'on' : '') + '" data-r="' + g[2] + '" data-v="' + r + '" aria-label="renk"></button>'; }).join('') + '</div>';
    }).join('');
    [].forEach.call(document.querySelectorAll('#sc [data-g]'), function (b) { b.onclick = function () { k[b.dataset.g] = b.dataset.v; document.getElementById('sn').innerHTML = ''; yaz(); }; });
    [].forEach.call(document.querySelectorAll('#sc [data-r]'), function (b) { b.onclick = function () { k[b.dataset.r] = b.dataset.v; yaz(); }; });
  }
  yaz();
  document.getElementById('dg').onclick = function () { location.hash = 'oyun/giydir-' + (c === 'kiz' ? 'erkek' : 'kiz'); };
  document.getElementById('hz').onclick = function () {
    var r = kontrol(c, k), sn = document.getElementById('sn');
    if (!r.e.length) {
      sn.innerHTML = '<div class="gy-sonuc ok"><b>Mâşallah, namaza hazırsın! 🌟</b>' + (r.b.length ? '<ul>' + r.b.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') + '</div>';
      if (bitti('g:giydir-' + c, 2)) toast('2 yıldız kazandın ⭐⭐'); else konfeti();
    } else {
      sn.innerHTML = '<div class="gy-sonuc no"><b>Biraz daha düzeltelim:</b><ul>' + r.e.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul></div>';
    }
    sn.scrollIntoView({ behavior: 'smooth', block: 'center' });
  };
}

var BO = window.BUYUK_OYUN;
BO.tiles.push(['giydir', '🧕', 'Namaza Hazırlan', 'Kız ve erkek çocuğu namaz için giydir', '#c0587e', '5-9 yaş']);
BO.calis.giydir = sec;
BO.calis['giydir-kiz'] = function () { oyna('kiz'); };
BO.calis['giydir-erkek'] = function () { oyna('erkek'); };
})();
