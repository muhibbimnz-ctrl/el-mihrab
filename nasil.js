/* el-Mihrâb — "Nasıl çalışılır?" tanıtımı.
   Her bölüm sayfası <script src="nasil.js?v=1" data-b="hadis"></script> ile yükler.
   Bölüme ilk girişte hikâye biçiminde (dokun: ileri/geri, kendiliğinden ilerler) tanıtım açılır;
   sonra üstteki "Nasıl?" düğmesiyle yeniden izlenir. Görüldü bilgisi: localStorage "mihrab.nasil.<bölüm>".
   window.Nasil.ac('<bölüm>') ile başka yerden de açılabilir. */
(function () {
'use strict';
var N = {
 app: { ad: 'el-Mihrâb’a hoş geldin', renk: '#0e5a43', s: [
  ['🕌', 'Kur’an ve tefsir bir arada', 'Mushafı sayfa sayfa oku, âyete dokunup tefsirini, i‘râbını ve meâlini aç; dilediğin kâriden dinle.'],
  ['📿', 'Namaz ve Kur’an menüsü', 'Ezan vakti, kıble, kaza takibi, hatim, tesbihat, ilmihal ve fetva asistanı tek yerde.'],
  ['📚', 'Dirâseler', 'Hadis, Fıkıh, Akaid, Ahlak ve Siyer dirâseleri: her biri kendi planıyla, adım adım.'],
  ['🗣️', 'Diller', 'Arapça, Farsça ve İngilizce: 6 aylık sesli programlar, romanlar ve sözlükler.'],
  ['🎯', 'Kadem', 'Diyanet sınavlarına hazırlık: konu anlatımı, açıklamalı sorular ve ÖSYM biçiminde denemeler.'],
  ['✨', 'Her bölümde bir rehber', 'Bir bölüme ilk girdiğinde nasıl çalışılacağını gösteririz. Tekrar izlemek için üstteki “Nasıl?” düğmesine dokun.']] },
 kuran: { ad: 'Kur’an Dirâsesi', renk: '#0e5a43', s: [
  ['📖', 'Sûreni seç', 'Sûre listesinden ya da kaldığın yerden başla. Âyetler Arapçası ve seçtiğin meâllerle alt alta gelir.'],
  ['👆', 'Âyete dokun', 'Tefsir, i‘râb, belâgat, kıraat, nüzul ve meâller sekmelerinde o âyetin bütün ilmine ulaş.'],
  ['🎧', 'Dinle ve takip et', 'Kâriyi seç, oynat: okunan âyet işaretlenir, sayfa kendiliğinden ilerler.'],
  ['⚙️', 'Kendine göre ayarla', 'Hat, yazı boyutu, tecvid renkleri, okunuş ve meâller Ayarlar’da. Günde birkaç âyeti tefsiriyle okumak yeter.']] },
 hadis: { ad: 'Hadis Dirâsesi', renk: '#7a4a1e', s: [
  ['📚', 'Kitabını seç', 'Buhârî, Müslim, Riyâzu’s-Sâlihîn ve diğer kitaplar; her biri bölüm bölüm.'],
  ['📝', 'Hadisi anlayarak oku', 'Arapça metin, Türkçesi ve açıklamaları birlikte. Kısa bir bölümle başla, her gün biraz ilerle.'],
  ['🎧', 'Dinle', 'Hadisleri sesli dinleyebilir, metinde aradığını “Ara” ile bulabilirsin.'],
  ['🔁', 'Uygula ve tekrar et', 'Her gün okuduğun bir hadisi hayatına geçirmeye niyet et; ertesi gün onu tekrar ederek başla.']] },
 fikih: { ad: 'Fıkıh Dirâsesi', renk: '#1d4e6e', s: [
  ['⚖️', 'Mesele mesele', 'Her mesele önce Hanefî hükmüyle, sonra diğer üç mezhebin görüşüyle verilir.'],
  ['📜', 'Delilleriyle', 'Âyet ve hadis delilleri meseleye bağlı; dokunup kaynağında açabilirsin.'],
  ['🧭', 'Adım adım ilmihal', 'Abdest, gusül, namaz gibi ibadetler sırayla, açıklamalı adımlarla.'],
  ['❓', 'Takıldığında sor', 'Fetva asistanı sorunu meselelerden cevaplar. Bir babı baştan sona bitirerek ilerlemek en verimlisidir.']] },
 akaid: { ad: 'Akaid Dirâsesi', renk: '#4b3a7a', s: [
  ['🧱', 'Madde madde', 'Akaid metni maddeler hâlinde: önce “Metin”, sonra “Hakkında” açıklaması.'],
  ['🧠', 'Ezber modu', 'Kısa metinleri ezber moduyla tekrar et; sorularla kendini yokla.'],
  ['✅', 'Okudum', 'Bitirdiğin maddeyi “Okudum” ile işaretle, ilerlemen kaydedilir.'],
  ['🎧', 'Dinle', 'Metni dinleyerek tekrar etmek akılda kalmasını kolaylaştırır.']] },
 ahlak: { ad: 'Ahlak Dirâsesi', renk: '#8a3b4b', s: [
  ['🌱', 'Konu konu', 'Her konu âyet ve hadislerle anlatılır; bir oturumda bir konu yeter.'],
  ['🪞', 'Muhasebe', 'Gün sonunda kendini “İyi / Eksik” diye değerlendir; nefis muhasebesi düzenli olunca işe yarar.'],
  ['✅', 'Okudum', 'Okuduğun konuyu işaretle, sıradaki konuya geç.'],
  ['🎧', 'Dinle', 'Konuları dinleyerek de takip edebilirsin.']] },
 siyer: { ad: 'Siyer Dirâsesi', renk: '#6b5a2c', s: [
  ['🗓️', '72 günlük plan', '“72 günlük planı başlat” de; her gün “Bugünün dersi” seni bekler.'],
  ['🗺️', 'Harita ve kişiler', 'Olayları haritada gör, sahâbîleri ve Kureyş şeceresini incele.'],
  ['🔗', 'Hadis ve fıkıh bağlantıları', 'Her olayın ilgili hadislerine ve fıkhî sonuçlarına geç.'],
  ['✅', 'Okudum', 'Dersi bitirince işaretle; plan seni kaldığın yerden devam ettirir.']] },
 arapca: { ad: 'Arapça Dersi', renk: '#0e5a43', s: [
  ['🗓️', 'Her gün bir ders', '6 aylık program günlere bölünmüş. “Kaldığım yerden devam et” ile o günün dersini aç.'],
  ['🎧', 'Önce dinle', 'Metni sesli dinle, sonra kendin oku. Harekeleri gizleyip okumayı dene.'],
  ['🔤', 'Kelimeler', 'Bilmediğin kelimenin “Anlamını göster”; yeni kelimeleri sesli tekrar et.'],
  ['✍️', 'Alıştırmalar', 'Soruları çöz, “Kontrol et” ile cevabını gör. Bitince “Sonraki gün”e geç; her gün 20-30 dakika yeter.']] },
 farsca: { ad: 'Farsça Dersi', renk: '#1d4e6e', s: [
  ['🗓️', 'Her gün bir ders', '6 aylık program günlere bölünmüş. “Kaldığım yerden devam et” ile başla.'],
  ['🎧', 'Dinle ve oku', 'Metni dinle; gerekirse “Okunuşu göster” ve “Türkçeyi göster”i aç.'],
  ['🔤', 'Kelimeler', '“Anlamını göster” ile kelimeleri öğren, sesli tekrar et.'],
  ['✍️', 'Alıştırmalar', 'Soruları çöz, “Kontrol et” ile doğrula, sonra “Sonraki gün”. Podcast’leri de dinlemeyi unutma.']] },
 ingilizce: { ad: 'İngilizce Dersi', renk: '#7a4a1e', s: [
  ['🗓️', 'Her gün bir ders', '6 aylık program günlere bölünmüş. “Kaldığım yerden devam et” ile o günün dersini aç.'],
  ['🎧', 'Dinle ve tekrar et', 'Metni sesli dinle, cümleleri yüksek sesle tekrar et.'],
  ['🔤', 'Kelimeler', 'Bilmediğin kelimede “Anlamını göster”; kelimeleri cümle içinde öğren.'],
  ['✍️', 'Alıştırmalar', 'Doğru-yanlış ve diğer soruları çöz, “Kontrol et”, sonra “Sonraki gün”.']] },
 medrese: { ad: 'Medrese', renk: '#6b5a2c', s: [
  ['🏛️', 'Medrese usûlü', 'Emsile, Binâ ve Avâmil sırasıyla okunur; biri bitmeden ötekine geçilmez.'],
  ['🧠', 'Ezberle', 'Emsile çekimlerini ve kuralları yüksek sesle tekrar ederek ezberle.'],
  ['🔍', 'Kur’an i‘râbı', 'Öğrendiğin kuralları Kur’an âyetlerinin i‘râbında uygula.'],
  ['⏱️', 'Az ve düzenli', 'Her gün kısa bir ders, ertesi gün dünkünün tekrarı: medrese usûlünün sırrı budur.']] },
 elifba: { ad: 'Kur’an Öğren', renk: '#0e5a43', s: [
  ['🔤', 'Dersler sırayla', 'Harflerden başla, dersleri sırayla bitir.'],
  ['🔊', 'Dinle', 'Harfin adını ve okunuşunu dinle; “Hepsini dinle” ile dersin tamamını çal.'],
  ['🗣️', 'Sen de oku', 'Duyduğunu yüksek sesle tekrar et; tekrar modunu açarak alıştır.'],
  ['✅', 'Okunuşu işaretle', 'Doğru okuduğunda işaretle, yanlışsa “Yeniden dene”.']] },
 roman: { ad: 'Roman Okuma', renk: '#4b3a7a', s: [
  ['📕', 'Seviyene göre seç', 'Romanlar seviyeye göre sıralı; zorlanmadan okuyabileceğin bir romanla başla.'],
  ['📖', 'Paragraf paragraf', 'Önce kendin oku, sonra “Türkçesi”ni açıp karşılaştır.'],
  ['📒', 'Kelime defteri', 'Bilmediğin kelimeyi defterine ekle; öğrenince “Öğrendim” de.'],
  ['⏱️', 'Her gün bir bölüm', 'Kısa ama düzenli okumak dili en hızlı geliştiren yoldur.']] },
 sozluk: { ad: 'Sözlük', renk: '#1d4e6e', s: [
  ['🔎', 'Ara', 'Kelimeyi yaz; Arapça, Farsça veya İngilizce karşılıkları ve örnekleri gelir.'],
  ['➕', 'Defterine ekle', 'Öğrenmek istediğin kelimeyi “＋” ile ekle.'],
  ['❓', 'Sözlük hakkında', 'Üstteki “?” düğmesi sözlükte neler olduğunu anlatır.']] },
 ihtisas: { ad: 'İhtisas', renk: '#6b5a2c', s: [
  ['🎓', 'Alanını seç', 'Tefsir, hadis, fıkıh ve diğer alanlarda okunacak kitaplar sıralı.'],
  ['📚', 'Kitap kitap', 'Listedeki kitapları sırayla oku; bitirdiğini işaretle.'],
  ['📈', 'İlerlemeni gör', 'Her alanın ilerleme çubuğu kaç kitap okuduğunu gösterir.']] },
 kadem: { ad: 'Kadem', renk: '#1d2b4f', video: 'img/kadem-tanitim.mp4', s: [
  ['🎯', 'Sınavını seç', 'MBSTS, DHBT ve diğer Diyanet sınavları. Ana sayfadaki büyük karttan sınavına gir.'],
  ['📅', 'Bugünün işi', 'Her gün sıradaki konu karşına gelir: Oku → Özet → Kartlar → Test.'],
  ['✅', 'Açıklamalı test', 'Her sorudan sonra doğru cevabı ve her şıkkın neden doğru ya da yanlış olduğunu gör.'],
  ['⏱️', 'Denemeler', 'ÖSYM biçiminde süreli denemeler; sonuçta ders ders başarını gör.'],
  ['📒', 'Yanlış defteri ve tekrar', 'Yanlışların deftere düşer; “Tekrar” ile unutmadan pekiştir.']] }
};
var ME = document.currentScript, B = ME && ME.getAttribute('data-b');
var css = document.createElement('style');
css.textContent = [
 '.nsl-k{position:fixed;inset:0;z-index:99999;color:#fff;display:flex;flex-direction:column;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--nr,#0e5a43);background:radial-gradient(900px 700px at 85% -10%,rgba(255,255,255,.18),transparent 60%),radial-gradient(800px 700px at -10% 110%,rgba(0,0,0,.35),transparent 60%),var(--nr,#0e5a43);animation:nslA .25s ease;user-select:none;-webkit-user-select:none}',
 '@keyframes nslA{from{opacity:0}to{opacity:1}}',
 '.nsl-c{display:flex;gap:4px;padding:calc(env(safe-area-inset-top,0px) + 12px) 12px 0}.nsl-c i{flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.3);overflow:hidden}.nsl-c i b{display:block;height:100%;width:0;background:#fff}',
 '.nsl-u{display:flex;align-items:center;justify-content:space-between;padding:12px 16px 0;font-size:14px;font-weight:700;opacity:.92}.nsl-u button{border:0;background:rgba(255,255,255,.16);color:#fff;border-radius:999px;padding:7px 14px;font:600 14px inherit;cursor:pointer}',
 '.nsl-g{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:20px 30px;position:relative}',
 '.nsl-g .ik{font-size:84px;line-height:1;margin-bottom:22px;animation:nslZ .35s ease}@keyframes nslZ{from{transform:scale(.7);opacity:0}to{transform:none;opacity:1}}',
 '.nsl-g h2{font-size:30px;line-height:1.15;margin:0 0 14px;font-weight:800;max-width:520px}.nsl-g p{font-size:18px;line-height:1.55;margin:0;max-width:480px;opacity:.92}',
 '.nsl-g video{width:min(78vw,340px);max-height:62vh;border-radius:22px;box-shadow:0 20px 50px rgba(0,0,0,.45);background:#000}',
 '.nsl-a{padding:0 20px calc(env(safe-area-inset-bottom,0px) + 22px);display:flex;justify-content:center;gap:10px}.nsl-a button{border:0;border-radius:999px;padding:14px 28px;font:700 17px inherit;cursor:pointer;background:#fff;color:#1b1b1b;min-width:200px}.nsl-a .nsl-n{font-size:13px;opacity:.7;align-self:center}',
 '.nsl-dk{position:absolute;top:0;bottom:0;width:32%;z-index:1}.nsl-dk.s{left:0}.nsl-dk.r{right:0}',
 '.nsl-b{display:inline-flex;align-items:center;gap:5px;border:1px solid currentColor;background:transparent;color:inherit;border-radius:999px;padding:4px 10px;font:600 12.5px system-ui,sans-serif;cursor:pointer;opacity:.85;white-space:nowrap;line-height:1.2}',
 '.nsl-y{position:fixed;top:calc(env(safe-area-inset-top,0px) + 8px);right:8px;z-index:9990;background:rgba(0,0,0,.55);color:#fff;border-color:transparent;backdrop-filter:blur(4px)}'
].join('\n');
document.head.appendChild(css);
function gorulduMu(b) { try { return !!localStorage.getItem('mihrab.nasil.' + b); } catch (e) { return true; } }
function gorulduYap(b) { try { localStorage.setItem('mihrab.nasil.' + b, '1'); } catch (e) {} }
var acik = null;
function ac(b, bitince) {
  var D = N[b]; if (!D || acik) return; gorulduYap(b);
  var S = D.s.slice(); if (D.video) S.unshift(['video', D.ad, 'Kısa tanıtım']);
  var k = document.createElement('div'); k.className = 'nsl-k'; k.style.setProperty('--nr', D.renk); k.setAttribute('role', 'dialog'); k.setAttribute('aria-label', 'Nasıl çalışılır: ' + D.ad);
  k.innerHTML = '<div class="nsl-c">' + S.map(function () { return '<i><b></b></i>'; }).join('') + '</div><div class="nsl-u"><span>' + D.ad + ' · Nasıl çalışılır?</span><button data-x>Geç</button></div><div class="nsl-g"></div><div class="nsl-a"></div>';
  document.body.appendChild(k); acik = k; var ovf = document.documentElement.style.overflow; document.documentElement.style.overflow = 'hidden';
  var i = 0, t0 = 0, raf = 0, dur = false, SURE = 5200, G = k.querySelector('.nsl-g'), A = k.querySelector('.nsl-a'), C = k.querySelectorAll('.nsl-c b');
  function kapat() { cancelAnimationFrame(raf); document.removeEventListener('keydown', tus); try { k.remove(); } catch (e) {} acik = null; document.documentElement.style.overflow = ovf; if (bitince) try { bitince(); } catch (e) {} }
  function goster(j) {
    i = Math.max(0, Math.min(S.length - 1, j)); var s = S[i]; t0 = performance.now(); dur = false;
    for (var x = 0; x < C.length; x++) C[x].style.width = x < i ? '100%' : '0';
    if (s[0] === 'video') {
      G.innerHTML = '<video src="' + D.video + '" autoplay muted playsinline preload="auto"></video>';
      var v = G.querySelector('video'); v.onended = function () { goster(i + 1); }; v.onerror = function () { goster(i + 1); };
      v.ontimeupdate = function () { if (v.duration) C[i].style.width = (v.currentTime / v.duration * 100) + '%'; };
      try { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } catch (e) {}
    } else G.innerHTML = '<div class="ik">' + s[0] + '</div><h2>' + s[1] + '</h2><p>' + s[2] + '</p>';
    G.insertAdjacentHTML('beforeend', '<div class="nsl-dk s" data-g="-1"></div><div class="nsl-dk r" data-g="1"></div>');
    A.innerHTML = i === S.length - 1 ? '<button data-x>Başla</button>' : '<span class="nsl-n">Dokun: ileri · sol kenar: geri</span>';
  }
  function dongu(t) { var s = S[i]; if (s[0] !== 'video' && !dur) { var o = (t - t0) / SURE; C[i].style.width = Math.min(100, o * 100) + '%'; if (o >= 1) { if (i < S.length - 1) goster(i + 1); else dur = true; } } raf = requestAnimationFrame(dongu); }
  function tus(e) { if (e.key === 'Escape') kapat(); else if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') goster(i + (e.key === 'ArrowRight' ? 1 : -1)); }
  k.addEventListener('click', function (e) { var x = e.target.closest('[data-x]'); if (x) return kapat(); var g = e.target.closest('[data-g]');
    if (g) { var n = i + (+g.getAttribute('data-g')); if (n >= S.length) return; goster(n); } });
  document.addEventListener('keydown', tus);
  goster(0); raf = requestAnimationFrame(dongu);
}
function dugme(b) {
  var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'nsl-b'; btn.innerHTML = '▶ Nasıl?'; btn.title = 'Nasıl çalışılır?';
  btn.onclick = function (e) { e.preventDefault(); e.stopPropagation(); ac(b); };
  var ust = document.querySelector('#hd .top');
  if (ust) { var son = ust.lastElementChild; if (son && son.tagName === 'SPAN' && !son.textContent.trim()) { son.replaceWith(btn); btn.style.marginLeft = 'auto'; }
    else { var h = ust.querySelector('h1'); if (h && h.nextSibling) ust.insertBefore(btn, h.nextSibling); else ust.appendChild(btn); btn.style.margin = '0 6px'; } }
  else { btn.classList.add('nsl-y'); document.body.appendChild(btn); }
  return btn;
}
window.Nasil = { ac: ac, gorulduMu: gorulduMu, N: N };
if (B && N[B]) {
  var bas = function () { try { dugme(B); if (!gorulduMu(B)) setTimeout(function () { ac(B); }, 450); } catch (e) {} };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bas); else bas();
}
})();
