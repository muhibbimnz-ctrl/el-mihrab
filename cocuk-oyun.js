/* Çocuk Köşesi — büyük oyunlar: Harf Balonları (4-6), İyilik Yolculuğu (6-8), Peygamberler Treni (8-9).
   cocuk.html içindeki sayfa, karis, esc, toast, konfeti, bitti, gun, seslendir, durdur yardımcılarını kullanır. */
(function () {
'use strict';
var css = document.createElement('style');
css.textContent = [
 '.yas{position:absolute;left:12px;top:12px;background:rgba(255,255,255,.92);color:#2b2a33;border-radius:999px;padding:1px 10px;font-weight:800;font-size:13px}',
 '.bgh{font-weight:800;color:var(--muted);margin:4px 4px 10px;font-size:15px}',
 /* balonlar */
 '.hb-ust{display:flex;align-items:center;gap:12px;background:var(--card);border:2px solid var(--line);border-radius:22px;padding:10px 14px;margin:6px 0 10px}',
 '.hb-hedef{font-family:"Noto Naskh Arabic","Amiri",serif;font-size:64px;line-height:1;width:84px;height:84px;display:grid;place-items:center;background:var(--sunS);border-radius:20px;flex:none}',
 '.hb-ust b{display:block;font-size:22px}.hb-ust small{color:var(--muted)}',
 '.hb-alan{position:relative;height:58vh;min-height:360px;border-radius:24px;overflow:hidden;background:linear-gradient(#bfe6ff,#eaf8ff 70%,#d8f5d0);border:2px solid var(--line);touch-action:manipulation}',
 '.hb-b{position:absolute;bottom:-120px;width:78px;height:94px;border:0;padding:0;background:none;cursor:pointer;animation:hbYuk linear forwards}',
 '.hb-b span{display:grid;place-items:center;width:78px;height:86px;border-radius:50% 50% 46% 46%;color:#fff;font-family:"Noto Naskh Arabic","Amiri",serif;font-size:40px;box-shadow:inset -8px -10px 0 rgba(0,0,0,.12)}',
 '.hb-b:after{content:"";position:absolute;left:38px;top:84px;width:2px;height:26px;background:rgba(0,0,0,.25)}',
 '.hb-b.pat span{animation:hbPat .25s forwards}.hb-b.yan{animation-play-state:paused}.hb-b.yan span{animation:sallan .3s}',
 '@keyframes hbYuk{to{transform:translateY(calc(-58vh - 240px))}}@keyframes hbPat{to{transform:scale(1.6);opacity:0}}',
 '.hb-bar{height:12px;background:var(--line);border-radius:8px;overflow:hidden;margin:10px 0}.hb-bar i{display:block;height:100%;background:var(--pri);transition:width .3s}',
 '.sev{display:grid;grid-template-columns:1fr 1fr;gap:10px}.sev .btn{flex-direction:column;padding:14px}.sev .ar{font-size:26px;line-height:1.4}',
 /* yolculuk */
 '.yol2{display:flex;align-items:center;justify-content:space-between;background:var(--card);border:2px solid var(--line);border-radius:22px;padding:10px 8px;margin:6px 0 12px;position:relative}',
 '.yol2 .d{font-size:28px;opacity:.45;text-align:center;flex:1;position:relative}.yol2 .d.on{opacity:1}.yol2 .d.ok:after{content:"✓";position:absolute;right:2px;top:-6px;font-size:15px;color:var(--ok);font-weight:800}',
 '.yol2 .ben{position:absolute;top:-16px;font-size:26px;transition:left .6s}',
 '.sah{font-size:72px;text-align:center;line-height:1.1;margin:4px 0}',
 '.sec{display:grid;gap:10px}.sec .btn{text-align:left;justify-content:flex-start;font-size:17px;padding:14px}.sec .btn.ok{background:var(--okS);border-color:var(--ok)}.sec .btn.bad{background:var(--badS);border-color:var(--bad)}',
 '.kalp{font-size:22px;text-align:center;letter-spacing:2px}',
 /* tren */
 '.tren{display:flex;flex-direction:row-reverse;gap:4px;overflow-x:auto;padding:8px 4px 12px;background:var(--card);border:2px solid var(--line);border-radius:22px;margin:6px 0 12px;min-height:92px;align-items:flex-end}',
 '.tren .v{flex:none;min-width:74px;height:62px;border-radius:12px 12px 6px 6px;background:var(--sky);color:#fff;font-weight:800;font-size:13px;display:grid;place-items:center;text-align:center;padding:2px 4px;position:relative;line-height:1.15}',
 '.tren .v:after{content:"● ●";position:absolute;bottom:-12px;left:0;right:0;text-align:center;color:#444;font-size:14px;letter-spacing:14px}',
 '.tren .lok{font-size:52px;flex:none;line-height:1}',
 '.es{display:grid;grid-template-columns:1fr 1.5fr;gap:8px}.es .btn{font-size:15px;line-height:1.3;padding:10px;text-align:left;justify-content:flex-start;min-height:56px}',
 '.es .btn.sec1{background:var(--sunS);border-color:var(--sun)}.es .btn.bitti{background:var(--okS);border-color:var(--ok);opacity:.6}.es .btn.bad{animation:sallan .3s;border-color:var(--bad)}'
].join('');
document.head.appendChild(css);

function son(kutu, puan, tum, anahtar, tekrar, metin) {
  var y = puan >= tum ? 3 : puan >= tum * .6 ? 2 : puan ? 1 : 0;
  kutu.innerHTML = '<div class="card" style="text-align:center"><div class="score">' + puan + ' / ' + tum + '</div><div class="stars">' + '⭐'.repeat(y) + '☆'.repeat(3 - y) + '</div><p>' + esc(metin || (y === 3 ? 'Mâşallah! Harika oynadın.' : y === 2 ? 'Çok güzel! Bir daha oynarsan tam puan alırsın.' : 'Güzel başlangıç! Tekrar dene, yaparsın.')) + '</p><div class="row" style="justify-content:center"><button class="btn pri" id="tkr">🔁 Yeniden oyna</button><a class="btn" href="#oyunlar">🎮 Oyunlar</a></div></div>';
  document.getElementById('tkr').onclick = tekrar;
  if (y === 3) { if (bitti(anahtar + ':' + gun(), 3)) toast('3 yıldız kazandın ⭐⭐⭐'); else konfeti(); }
}
function soyle(t) { try { seslendir([{ t: t }]); } catch (e) {} }

/* ───────── 1) HARF BALONLARI (4-6 yaş) ───────── */
var HARF = [['ا','Elif'],['ب','Be'],['ت','Te'],['ث','Se'],['ج','Cim'],['ح','Ha'],['خ','Hı'],['د','Dal'],['ذ','Zel'],['ر','Ra'],['ز','Ze'],['س','Sin'],['ش','Şın'],['ص','Sad'],['ض','Dad'],['ط','Tı'],['ظ','Zı'],['ع','Ayn'],['غ','Ğayn'],['ف','Fe'],['ق','Kaf'],['ك','Kef'],['ل','Lam'],['م','Mim'],['ن','Nun'],['و','Vav'],['ه','He'],['ي','Ye']];
var SEV = [
 { ad: '1. Seviye', a: 'ا ب ت ث ج ح خ', h: HARF.slice(0, 7), hiz: 7.5 },
 { ad: '2. Seviye', a: 'د ذ ر ز س ش ص', h: HARF.slice(7, 14), hiz: 7 },
 { ad: '3. Seviye', a: 'ض ط ظ ع غ ف ق', h: HARF.slice(14, 21), hiz: 6.5 },
 { ad: '4. Seviye', a: 'ك ل م ن و ه ي', h: HARF.slice(21), hiz: 6 },
 { ad: 'Benzer harfler', a: 'ب ت ث · ج ح خ · س ش', h: [HARF[1], HARF[2], HARF[3], HARF[4], HARF[5], HARF[6], HARF[11], HARF[12]], hiz: 6 },
 { ad: 'Hepsi karışık', a: '28 harf', h: HARF, hiz: 5.5 }];
var RENK = ['#ef476f', '#3a86ff', '#ffb703', '#8338ec', '#06d6a0', '#fb8500', '#e76f51'];

function balonlar() {
  sayfa('Harf Balonları', '<h1>🎈 Harf Balonları</h1><p class="lead">Ekrandaki harfi taşıyan balonları patlat! Yanlış balona dokunursan balon sallanır. <b>4-6 yaş</b> için; harfleri tanımayı ve ayırt etmeyi öğretir.</p><div class="sev">' +
    SEV.map(function (s, i) { return '<button class="btn" data-s="' + i + '"><b>' + s.ad + '</b><span class="ar">' + esc(s.a) + '</span>' + (S.ok['o:balon:' + i] ? '<small>⭐ tamamlandı</small>' : '') + '</button>'; }).join('') + '</div>', '#oyunlar');
  [].forEach.call(document.querySelectorAll('[data-s]'), function (b) { b.onclick = function () { location.hash = 'oyun/balon-' + b.dataset.s; }; });
}
function balonOyna(si) {
  var sv = SEV[si], hedefler = karis(sv.h).slice(0, 3), hi = 0, vurdu = 0, hata = 0, GEREK = 5, saat = null;
  sayfa('Harf Balonları', '<div class="hb-ust"><div class="hb-hedef" id="hh"></div><div style="flex:1"><b id="hn"></b><small id="hs"></small><div class="hb-bar"><i id="hp" style="width:0"></i></div></div><button class="btn" id="hd" aria-label="Dinle">🔊</button></div><div class="hb-alan" id="ha"></div>', '#oyun/balon');
  var alan = document.getElementById('ha');
  function hedef() { var h = hedefler[hi]; document.getElementById('hh').textContent = h[0]; document.getElementById('hn').textContent = h[1] + ' harfini yakala!'; document.getElementById('hs').textContent = 'Harf ' + (hi + 1) + ' / ' + hedefler.length + ' · ' + vurdu + ' / ' + GEREK; document.getElementById('hp').style.width = (100 * vurdu / GEREK) + '%'; }
  document.getElementById('hd').onclick = function () { soyle(hedefler[hi][1] + ' harfini yakala'); };
  function uret() {
    if (!document.body.contains(alan)) { clearInterval(saat); return; }
    var h = hedefler[hi], harf = Math.random() < .42 ? h : sv.h[Math.floor(Math.random() * sv.h.length)];
    var b = document.createElement('button'); b.className = 'hb-b'; b.setAttribute('aria-label', harf[1]);
    b.style.left = (4 + Math.random() * 74) + '%'; b.style.animationDuration = (sv.hiz + Math.random() * 1.5) + 's';
    b.innerHTML = '<span style="background:' + RENK[Math.floor(Math.random() * RENK.length)] + '">' + harf[0] + '</span>';
    b.onclick = function () {
      if (b.classList.contains('pat')) return;
      if (harf[0] === hedefler[hi][0]) {
        b.classList.add('pat'); vurdu++; setTimeout(function () { b.remove(); }, 260);
        if (vurdu >= GEREK) {
          hi++; vurdu = 0;
          if (hi >= hedefler.length) { clearInterval(saat); alan.innerHTML = ''; var k = document.createElement('div'); alan.parentNode.appendChild(k); alan.remove(); document.querySelector('.hb-ust').remove();
            var puan = Math.max(0, 10 - hata); son(k, puan, 10, 'o:balon:' + si, function () { balonOyna(si); }, hata ? 'Bitti! ' + hata + ' yanlış balona dokundun.' : 'Hiç hata yapmadın, mâşallah!'); if (puan >= 8) S.ok['o:balon:' + si] = 1, kaydet(); return; }
          toast('Aferin! Şimdi yeni harf: ' + hedefler[hi][1]); soyle(hedefler[hi][1] + ' harfini yakala');
        }
        hedef();
      } else { hata++; b.classList.add('yan'); setTimeout(function () { b.classList.remove('yan'); }, 350); toast('Bu ' + harf[1] + '. Biz ' + hedefler[hi][1] + ' arıyoruz.'); }
    };
    b.addEventListener('animationend', function (ev) { if (ev.animationName === 'hbYuk') b.remove(); });
    alan.appendChild(b);
  }
  hedef(); soyle(hedefler[0][1] + ' harfini yakala'); uret(); saat = setInterval(uret, 950);
}

/* ───────── 2) İYİLİK YOLCULUĞU (6-8 yaş) ───────── */
var DURAK = [
 { e: '🏠', ad: 'Ev', s: [
  { r: '🧒🍽️', q: 'Sofraya oturdun, yemekler çok güzel kokuyor. Ne yaparsın?', c: [['“Bismillâh” der, sağ elimle ve önümden yerim.', 1], ['Hemen en büyük parçayı kaparım.', 0], ['Önce tabletimi açar, sonra yerim.', 0]], n: 'Peygamberimiz bir çocuğa şöyle öğretti: “Allah’ın adını an, sağ elinle ye, önünden ye.”', k: 'Buhârî, Et‘ime, 2' },
  { r: '👵🛋️', q: 'Annen yorgun, sana “Odanı toplar mısın?” dedi. Ne dersin?', c: [['“Tamam anneciğim” der, hemen toplarım.', 1], ['“Öf, şimdi olmaz!” derim.', 0], ['Duymamış gibi yaparım.', 0]], n: 'Allah, anne babaya “öf” bile denmemesini, onlara güzel söz söylenmesini emreder.', k: 'İsrâ 17/23' },
  { r: '🍞🗑️', q: 'Tabağında yemek kaldı ama doydun. Ne yaparsın?', c: [['Bir dahaki sefere az alırım, kalanı israf etmem.', 1], ['Hepsini çöpe atarım.', 0], ['Yere döker oynarım.', 0]], n: 'Kur’an der ki: “Yiyiniz, içiniz fakat israf etmeyiniz.”', k: 'A‘râf 7/31' }]},
 { e: '🏫', ad: 'Okul', s: [
  { r: '✏️😢', q: 'Sınıf arkadaşın kalemini evde unutmuş, üzgün. Ne yaparsın?', c: [['Kendi kalemlerimden birini ona veririm.', 1], ['“Kendi suçun” deyip gülerim.', 0], ['Görmezden gelirim.', 0]], n: 'Peygamberimiz: “Sizden biri kendisi için istediğini kardeşi için de istemedikçe gerçek iman etmiş olmaz.”', k: 'Buhârî, Îmân, 7' },
  { r: '🏺💥', q: 'Teneffüste yanlışlıkla bir vazoyu kırdın. Kimse görmedi. Ne yaparsın?', c: [['Öğretmenime doğruyu söylerim.', 1], ['Başkası kırdı derim.', 0], ['Saklanırım.', 0]], n: 'Peygamberimiz: “Doğruluk iyiliğe, iyilik de cennete götürür.”', k: 'Buhârî, Edeb, 69' },
  { r: '📖👧', q: 'Arkadaşın Fâtiha’yı ezberleyemiyor. Sen biliyorsun. Ne yaparsın?', c: [['Ona yavaş yavaş birlikte tekrar ettiririm.', 1], ['“Sen hiç öğrenemezsin” derim.', 0], ['Ona söylemem, sadece ben bileyim.', 0]], n: 'Peygamberimiz: “Sizin en hayırlınız Kur’an’ı öğrenen ve öğretendir.”', k: 'Buhârî, Fezâilü’l-Kur’ân, 21' }]},
 { e: '🌳', ad: 'Park', s: [
  { r: '🐱💧', q: 'Parkta susamış bir kedi gördün. Ne yaparsın?', c: [['Bir kaba su koyup içmesini beklerim.', 1], ['Ona taş atarım.', 0], ['Kuyruğunu çekerim.', 0]], n: 'Peygamberimiz: “Yeryüzündekilere merhamet edin ki göktekiler de size merhamet etsin.”', k: 'Tirmizî, Birr, 16' },
  { r: '🧸👦', q: 'Küçük bir çocuk salıncağa binmek istiyor ama sıra hep sende. Ne yaparsın?', c: [['Sırayı ona veririm, birlikte sırayla bineriz.', 1], ['Hiç inmem.', 0], ['Onu iterim.', 0]], n: 'Peygamberimiz: “Küçüklerimize merhamet etmeyen, büyüklerimize saygı göstermeyen bizden değildir.”', k: 'Tirmizî, Birr, 15' },
  { r: '🪨🚶', q: 'Yolun ortasında insanların takılabileceği büyük bir taş var. Ne yaparsın?', c: [['Taşı kenara kaldırırım.', 1], ['Üstünden atlar, geçerim.', 0], ['Başkası kaldırsın derim.', 0]], n: 'Peygamberimiz: “Yolda insanlara eziyet veren şeyi kaldırmak sadakadır.”', k: 'Buhârî, Mezâlim, 24' }]},
 { e: '🛒', ad: 'Pazar', s: [
  { r: '🪙🍎', q: 'Manav sana fazla para üstü verdi. Ne yaparsın?', c: [['Fazlasını geri veririm.', 1], ['Sessizce cebime koyarım.', 0], ['Şeker alırım.', 0]], n: 'Peygamberimiz: “Bizi aldatan bizden değildir.” Başkasının hakkı ona geri verilir.', k: 'Müslim, Îmân, 164' },
  { r: '👴🛍️', q: 'Yaşlı bir dede ağır torbalarını taşıyamıyor. Ne yaparsın?', c: [['“Yardım edebilir miyim?” deyip taşırım.', 1], ['Gülüp geçerim.', 0], ['Acelem var deyip koşarım.', 0]], n: 'Peygamberimiz büyüklere saygıyı imanın gereği saydı.', k: 'Tirmizî, Birr, 15' },
  { r: '😊👋', q: 'Pazarda tanıdık bir teyzeyle karşılaştın. Ne yaparsın?', c: [['Gülümser, “Selâmün aleyküm” derim.', 1], ['Başımı çevirip geçerim.', 0], ['Ona dil çıkarırım.', 0]], n: 'Peygamberimiz: “Kardeşine gülümsemen sadakadır.” Bir hadiste de “Selamı aranızda yayın” buyurdu.', k: 'Tirmizî, Birr, 36; Müslim, Îmân, 93' }]},
 { e: '🏡', ad: 'Komşu', s: [
  { r: '🍲🚪', q: 'Annen güzel bir çorba pişirdi. Komşunuz hasta. Ne yaparsınız?', c: [['Bir tas çorba götürürüz.', 1], ['Hepsini kendimiz yeriz.', 0], ['Kapılarını çalıp kaçarız.', 0]], n: 'Peygamberimiz: “Komşusu açken tok yatan kişi (olgun) mümin değildir.”', k: 'Buhârî, el-Edebü’l-müfred, 112' },
  { r: '⚽🪟', q: 'Topun komşunun bahçesine düştü. Ne yaparsın?', c: [['Kapıyı çalıp izin isterim.', 1], ['Çitten atlayıp girerim.', 0], ['Bahçedeki çiçekleri ezerek ararım.', 0]], n: 'Kur’an, başkasının evine izin alıp selam vermeden girilmemesini öğretir.', k: 'Nûr 24/27' },
  { r: '🎁🧒', q: 'Komşunun çocuğuyla küstünüz. Ne yaparsın?', c: [['Ona küçük bir hediye verip barışırım.', 1], ['Hiç konuşmam.', 0], ['Herkese onu kötülerim.', 0]], n: 'Peygamberimiz: “Hediyeleşin ki birbirinizi sevesiniz.”', k: 'Buhârî, el-Edebü’l-müfred, 594' }]},
 { e: '🕌', ad: 'Cami', s: [
  { r: '🧼💧', q: 'Camiye namaza gideceksin. Önce ne yaparsın?', c: [['Abdest alır, temiz giyinirim.', 1], ['Çamurlu ayakkabıyla girerim.', 0], ['Hiç hazırlanmadan koşarım.', 0]], n: 'Peygamberimiz: “Temizlik imanın yarısıdır.”', k: 'Müslim, Tahâret, 1' },
  { r: '🤫🕌', q: 'Camide insanlar namaz kılıyor. Ne yaparsın?', c: [['Sessizce saf tutar, ben de kılarım.', 1], ['Koşup bağırırım.', 0], ['Önlerinden geçip oynarım.', 0]], n: 'Müslüman, elinden ve dilinden insanların emin olduğu kimsedir; camide başkalarını rahatsız etmez.', k: 'Buhârî, Îmân, 4' },
  { r: '👞👟', q: 'Cami çıkışında ayakkabılar karışmış. Ne yaparsın?', c: [['Kendiminkini bulur, dağınık olanları düzeltirim.', 1], ['Ayakkabıları tekmelerim.', 0], ['Beğendiğim ayakkabıyı giyerim.', 0]], n: 'Peygamberimiz: “Kolaylaştırın, zorlaştırmayın.” Başkasının işini kolaylaştırmak da iyiliktir.', k: 'Buhârî, İlim, 11' }]}];

function yolculuk() {
  var plan = DURAK.map(function (d) { return { d: d, s: d.s[Math.floor(Math.random() * d.s.length)] }; }), i = 0, puan = 0, ilk = true;
  sayfa('İyilik Yolculuğu', '<h1>🧭 İyilik Yolculuğu</h1><p class="lead"><b>6-8 yaş</b> · Evden camiye giden yolda her durakta bir seçim var. Doğru davranışı seç, iyilik yıldızlarını topla!</p><div class="yol2" id="yl">' +
    plan.map(function (p, j) { return '<div class="d" data-j="' + j + '">' + p.d.e + '</div>'; }).join('') + '<span class="ben" id="ben">🧒</span></div><div id="yk"></div>', '#oyunlar');
  function ciz() {
    [].forEach.call(document.querySelectorAll('#yl .d'), function (x, j) { x.classList.toggle('on', j <= i); x.classList.toggle('ok', j < i); });
    var ben = document.getElementById('ben'), d = document.querySelectorAll('#yl .d')[Math.min(i, plan.length - 1)];
    if (ben && d) ben.style.left = (d.offsetLeft + d.offsetWidth / 2 - 13) + 'px';
    var kt = document.getElementById('yk'); if (!kt) return;
    if (i >= plan.length) { son(kt, puan, plan.length, 'o:yolculuk', yolculuk, puan === plan.length ? 'Camiye vardın ve her durakta iyiliği seçtin. Mâşallah!' : 'Camiye vardın! Bazı duraklarda tekrar düşündün; bu da güzel.'); return; }
    var p = plan[i], s = p.s; ilk = true;
    kt.innerHTML = '<div class="card"><small style="color:var(--muted)">' + (i + 1) + '. durak: ' + p.d.ad + '</small><div class="sah">' + s.r + '</div><div class="q">' + esc(s.q) + '</div><button class="mini" id="yd">🔊 Dinle</button><div class="sec" style="margin-top:10px">' +
      karis(s.c).map(function (c) { return '<button class="btn" data-v="' + c[1] + '">' + esc(c[0]) + '</button>'; }).join('') + '</div><div id="yn"></div></div><div class="kalp">' + '⭐'.repeat(puan) + '</div>';
    document.getElementById('yd').onclick = function () { soyle(s.q + ' ' + s.c.map(function (c) { return c[0]; }).join(' Ya da: ')); };
    [].forEach.call(kt.querySelectorAll('[data-v]'), function (b) { b.onclick = function () {
      if (b.disabled) return;
      if (+b.dataset.v) {
        if (ilk) puan++;
        b.classList.add('ok'); [].forEach.call(kt.querySelectorAll('[data-v]'), function (x) { x.disabled = true; });
        document.getElementById('yn').innerHTML = '<div class="hadis" style="margin-top:12px">💚 ' + esc(s.n) + '<i>' + esc(s.k) + '</i></div><button class="btn pri" id="yi" style="width:100%">' + (i < plan.length - 1 ? 'Sonraki durağa yürü 👣' : 'Camiye var 🕌') + '</button>';
        document.getElementById('yi').onclick = function () { i++; ciz(); window.scrollTo(0, 0); };
      } else { ilk = false; b.classList.add('bad'); b.disabled = true; toast('Bunu bir daha düşün. Hangisi Allah’ın sevdiği davranış?'); }
    }; });
  }
  ciz();
}

/* ───────── 3) PEYGAMBERLER TRENİ (8-9 yaş) ───────── */
var PEY = [
 ['Hz. Âdem', 'İlk insan ve ilk peygamber; Allah ona bütün isimleri öğretti.', 'Bakara 2/31'],
 ['Hz. Nûh', 'Allah’ın emriyle büyük bir gemi yaptı; tufandan inananlar kurtuldu.', 'Hûd 11/37-44'],
 ['Hz. Hûd', 'Güçlü binalar yapan Âd kavmine gönderildi.', 'Hûd 11/50'],
 ['Hz. Sâlih', 'Semûd kavmine mucize olarak bir dişi deve gösterildi.', 'Hûd 11/61-64'],
 ['Hz. İbrâhîm', 'Putları kırdığı için ateşe atıldı; ateş onu yakmadı, serin oldu.', 'Enbiyâ 21/68-69'],
 ['Hz. İsmâil', 'Babası İbrâhîm ile birlikte Kâbe’nin temellerini yükseltti.', 'Bakara 2/127'],
 ['Hz. Yûsuf', 'Kardeşleri onu kuyuya attı; sonra Mısır’da hazinelerin başına geçti.', 'Yûsuf 12/15, 55'],
 ['Hz. Eyyûb', 'Ağır hastalığa sabrettiği için sabrın örneği oldu.', 'Sâd 38/41-44'],
 ['Hz. Mûsâ', 'Asası yılana dönüştü; deniz ikiye ayrıldı. Ona Tevrat verildi.', 'Tâhâ 20/20; Şuarâ 26/63'],
 ['Hz. Dâvûd', 'Allah ona demiri yumuşattı, zırh yaptı. Ona Zebur verildi.', 'Sebe 34/10-11'],
 ['Hz. Süleymân', 'Karıncanın sözünü anladı; rüzgâr onun emrine verildi.', 'Neml 27/18-19'],
 ['Hz. Yûnus', 'Balığın karnında “Senden başka ilah yok” diye dua etti.', 'Enbiyâ 21/87'],
 ['Hz. Zekeriyyâ', 'Yaşlılığında oğlu Yahyâ ile müjdelendi.', 'Meryem 19/7'],
 ['Hz. Îsâ', 'Beşikteyken konuştu. Ona İncil verildi.', 'Meryem 19/29-30'],
 ['Hz. Muhammed ﷺ', 'Son peygamberdir; ona Kur’ân-ı Kerîm indirildi.', 'Ahzâb 33/40']];
var SIRA = ['Hz. Âdem', 'Hz. Nûh', 'Hz. İbrâhîm', 'Hz. Yûsuf', 'Hz. Mûsâ', 'Hz. Dâvûd', 'Hz. Îsâ', 'Hz. Muhammed ﷺ'];

function tren() {
  sayfa('Peygamberler Treni', '<h1>🚂 Peygamberler Treni</h1><p class="lead"><b>8-9 yaş</b> · İki istasyon var: önce her peygamberi kıssasıyla eşleştir, sonra treni peygamberlerin geliş sırasına göre diz.</p><div class="list"><button class="it" id="t1"><span class="e">🔗</span><span class="tx"><b>1. İstasyon: Kıssa eşleştirme</b><small>6 peygamber, 6 kıssa</small></span><span class="ok">' + (S.ok['o:tren1:' + gun()] ? '⭐' : '') + '</span></button><button class="it" id="t2"><span class="e">🚃</span><span class="tx"><b>2. İstasyon: Treni sırala</b><small>8 vagonu doğru sırayla tak</small></span><span class="ok">' + (S.ok['o:tren2:' + gun()] ? '⭐' : '') + '</span></button></div><div class="akil" style="margin-top:14px"><b>Bilgi:</b> Kur’an’da adı geçen 25 peygamber vardır. Hepsine iman ederiz ve aralarında ayrım yapmayız (Bakara 2/285).</div>', '#oyunlar');
  document.getElementById('t1').onclick = function () { location.hash = 'oyun/tren-es'; }; document.getElementById('t2').onclick = function () { location.hash = 'oyun/tren-sira'; };
}
function eslestir() {
  var L = karis(PEY).slice(0, 6), sol = karis(L), sag = karis(L), secili = null, bulunan = 0, hata = 0;
  sayfa('Peygamberler Treni', '<h1>🔗 Kıssa Eşleştirme</h1><p class="lead">Önce soldan bir peygamber seç, sonra sağdan onun kıssasına dokun.</p><div class="es" id="es">' +
    sol.map(function (p, j) { return '<button class="btn" data-p="' + esc(p[0]) + '">' + esc(p[0]) + '</button><button class="btn" data-k="' + esc(sag[j][0]) + '">' + esc(sag[j][1]) + '</button>'; }).join('') + '</div><div id="ek"></div>', '#oyun/tren');
  [].forEach.call(document.querySelectorAll('[data-p]'), function (b) { b.onclick = function () { if (b.classList.contains('bitti')) return; [].forEach.call(document.querySelectorAll('[data-p]'), function (x) { x.classList.remove('sec1'); }); b.classList.add('sec1'); secili = b; }; });
  [].forEach.call(document.querySelectorAll('[data-k]'), function (b) { b.onclick = function () {
    if (b.classList.contains('bitti')) return;
    if (!secili) { toast('Önce soldan bir peygamber seç.'); return; }
    if (b.dataset.k === secili.dataset.p) {
      var p = PEY.filter(function (x) { return x[0] === b.dataset.k; })[0];
      b.classList.add('bitti'); secili.classList.add('bitti'); secili.classList.remove('sec1'); secili = null; bulunan++; toast('Doğru! ' + p[0] + ' · ' + p[2]);
      if (bulunan === L.length) setTimeout(function () { son(document.getElementById('ek'), Math.max(0, 6 - hata), 6, 'o:tren1', eslestir, hata ? 'Hepsini eşleştirdin! ' + hata + ' kez yanıldın.' : 'Hiç yanılmadan hepsini eşleştirdin!'); document.getElementById('ek').scrollIntoView({ behavior: 'smooth' }); }, 500);
    } else { hata++; b.classList.remove('bad'); void b.offsetWidth; b.classList.add('bad'); toast('Bu kıssa ' + secili.dataset.p + '’a ait değil.'); }
  }; });
}
function sirala() {
  var sira = 0, hata = 0;
  sayfa('Peygamberler Treni', '<h1>🚃 Treni Sırala</h1><p class="lead">Lokomotiften başlayarak peygamberleri geliş sırasına göre vagonlara bindir. Sıradaki vagon: <b id="sn">1</b></p><div class="tren" id="tr"><span class="lok">🚂</span></div><div class="ord" id="ord">' +
    karis(SIRA.map(function (a, j) { return { a: a, j: j }; })).map(function (o) { return '<button class="btn" data-j="' + o.j + '">' + esc(o.a) + '</button>'; }).join('') + '</div><div id="sk"></div>', '#oyun/tren');
  var RK = ['#3a86ff', '#ef476f', '#ffb703', '#8338ec', '#06d6a0', '#fb8500', '#2a9d8f', '#1f8a70'];
  [].forEach.call(document.querySelectorAll('#ord button'), function (b) { b.onclick = function () {
    if (b.classList.contains('done')) return;
    if (+b.dataset.j === sira) {
      b.classList.add('done'); var v = document.createElement('div'); v.className = 'v'; v.style.background = RK[sira]; v.textContent = SIRA[sira].replace('Hz. ', ''); document.getElementById('tr').appendChild(v); v.scrollIntoView({ inline: 'end', block: 'nearest' });
      sira++; document.getElementById('sn').textContent = sira + 1;
      if (sira === SIRA.length) { document.getElementById('sn').textContent = 'tamam'; toast('Tren hazır! Çuf çuf 🚂'); son(document.getElementById('sk'), Math.max(0, 8 - hata), 8, 'o:tren2', sirala, 'Âdem’den Peygamberimize kadar treni dizdin!'); }
    } else { hata++; b.classList.remove('bad'); void b.offsetWidth; b.classList.add('bad'); toast('Bu peygamber daha ' + (+b.dataset.j < sira ? 'önce' : 'sonra') + ' geldi.'); }
  }; });
}

window.BUYUK_OYUN = {
 tiles: [
  ['balon', '🎈', 'Harf Balonları', 'Elif-Bâ harflerini patlat', '#fb5607', '4-6 yaş'],
  ['yolculuk', '🧭', 'İyilik Yolculuğu', 'Evden camiye iyilik seç', '#2a9d8f', '6-8 yaş'],
  ['tren', '🚂', 'Peygamberler Treni', 'Kıssaları eşleştir, treni diz', '#3a0ca3', '8-9 yaş']],
 calis: { balon: balonlar, yolculuk: yolculuk, tren: tren, 'tren-es': eslestir, 'tren-sira': sirala },
 ac: function (k) { var m = /^balon-(\d)$/.exec(k || ''); if (m && SEV[+m[1]]) { balonOyna(+m[1]); return true; } if (this.calis[k]) { this.calis[k](); return true; } return false; }
};
})();
