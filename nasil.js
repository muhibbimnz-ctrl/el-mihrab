/* el-Mihrâb — "Nasıl çalışılır?" tanıtımı.
   Her bölüm sayfası <script src="nasil.js?v=1" data-b="hadis"></script> ile yükler.
   Bölüme ilk girişte hikâye biçiminde (dokun: ileri/geri, kendiliğinden ilerler) tanıtım açılır;
   sonra üstteki "Nasıl?" düğmesiyle yeniden izlenir. Görüldü bilgisi: localStorage "mihrab.nasil.<bölüm>".
   window.Nasil.ac('<bölüm>') ile başka yerden de açılabilir. */
(function () {
'use strict';
var N = {
 app: { ad: 'el-Mihrâb', renk: '#0e5a43', s: [
  ['🕌', 'Kur’an ve tefsir bir arada', 'Mushafı sayfa sayfa oku, âyete dokunup tefsirini, i‘râbını ve meâlini aç; dilediğin kâriden dinle.'],
  ['📿', 'Namaz ve Kur’an menüsü', 'Ezan vakti, kıble, kaza takibi, hatim, tesbihat, ilmihal ve fetva asistanı tek yerde.'],
  ['📚', 'Dirâseler', 'Hadis, Fıkıh, Akaid, Ahlak ve Siyer dirâseleri: her biri kendi planıyla, adım adım.'],
  ['🗣️', 'Diller', 'Arapça, Farsça ve İngilizce: 6 aylık sesli programlar, romanlar ve sözlükler.'],
  ['🎯', 'Kadem', 'Diyanet sınavlarına hazırlık: konu anlatımı, açıklamalı sorular ve ÖSYM biçiminde denemeler.'],
  ['', 'Her bölümde kısa bir rehber', 'Bir bölüme ilk girdiğinde nasıl çalışılacağı bir kez gösterilir. Yeniden bakmak için sayfanın üstündeki “Nasıl çalışılır” düğmesini kullan.']] },
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
  ['⏱️', 'Az ve düzenli', 'Her gün kısa bir ders, ertesi gün dünkünün tekrarı. Medrese usûlünde esas, az ve düzenli ilerlemektir.']] },
 elifba: { ad: 'Kur’an Öğren', renk: '#0e5a43', s: [
  ['🔤', 'Dersler sırayla', 'Harflerden başla, dersleri sırayla bitir.'],
  ['🔊', 'Dinle', 'Harfin adını ve okunuşunu dinle; “Hepsini dinle” ile dersin tamamını çal.'],
  ['🗣️', 'Sen de oku', 'Duyduğunu yüksek sesle tekrar et; tekrar modunu açarak alıştır.'],
  ['✅', 'Okunuşu işaretle', 'Doğru okuduğunda işaretle, yanlışsa “Yeniden dene”.']] },
 roman: { ad: 'Roman Okuma', renk: '#4b3a7a', s: [
  ['📕', 'Seviyene göre seç', 'Romanlar seviyeye göre sıralı; zorlanmadan okuyabileceğin bir romanla başla.'],
  ['📖', 'Paragraf paragraf', 'Önce kendin oku, sonra “Türkçesi”ni açıp karşılaştır.'],
  ['📒', 'Kelime defteri', 'Bilmediğin kelimeyi defterine ekle; öğrenince “Öğrendim” de.'],
  ['⏱️', 'Her gün bir bölüm', 'Kısa ama düzenli okumak, dili en kalıcı geliştiren yoldur.']] },
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
 '.nsl-k{position:fixed;inset:0;z-index:99999;display:flex;flex-direction:column;background:#f7f3ea;color:#1f1c17;font-family:"Source Sans 3",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;opacity:0;transition:opacity .2s ease}',
 '.nsl-k.on{opacity:1}',
 '.nsl-u{display:flex;align-items:center;justify-content:space-between;padding:calc(env(safe-area-inset-top,0px) + 14px) 22px 0;font-size:12.5px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--nr,#0e5a43)}',
 '.nsl-u button{border:0;background:none;color:#6f665a;font:600 14px inherit;letter-spacing:0;text-transform:none;padding:8px 0 8px 12px;cursor:pointer}',
 '.nsl-c{display:flex;gap:6px;padding:12px 22px 0}.nsl-c i{flex:1;height:2px;background:#ddd3c1}.nsl-c i.on{background:var(--nr,#0e5a43)}',
 '.nsl-g{flex:1;display:flex;flex-direction:column;justify-content:center;padding:24px 30px 10px;max-width:560px;width:100%;margin:0 auto;box-sizing:border-box;transition:opacity .18s ease}',
 '.nsl-g.gec{opacity:0}',
 '.nsl-g .no{font-family:Georgia,"Times New Roman",serif;font-size:15px;color:#8a7f6e;margin-bottom:14px;font-variant-numeric:tabular-nums}',
 '.nsl-g .no b{color:var(--nr,#0e5a43);font-size:15px}',
 '.nsl-g h2{font-family:Georgia,"Times New Roman",serif;font-weight:700;font-size:30px;line-height:1.2;margin:0 0 14px;color:#1f1c17}',
 '.nsl-g p{font-size:18px;line-height:1.6;margin:0;color:#4a4237}',
 '.nsl-g .cz{width:44px;height:3px;background:var(--nr,#0e5a43);margin:0 0 22px}',
 '.nsl-g video{width:min(80vw,330px);max-height:60vh;border-radius:14px;background:#000;align-self:center}',
 '.nsl-a{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 22px calc(env(safe-area-inset-bottom,0px) + 22px);max-width:560px;width:100%;margin:0 auto;box-sizing:border-box}',
 '.nsl-a button{border:0;cursor:pointer;font:600 16px inherit;border-radius:12px;padding:14px 22px}',
 '.nsl-a .ger{background:none;color:#6f665a;padding-left:0}.nsl-a .ger[disabled]{visibility:hidden}',
 '.nsl-a .ile{background:var(--nr,#0e5a43);color:#fff;min-width:150px}',
 '@media (prefers-color-scheme:dark){.nsl-k{background:#141816;color:#ece6d8}.nsl-g h2{color:#ece6d8}.nsl-g p{color:#c8c0ae}.nsl-c i{background:#2c3430}.nsl-u button,.nsl-a .ger{color:#a59c8a}}',
 '.nsl-b{display:inline-flex;align-items:center;gap:6px;border:1px solid currentColor;background:transparent;color:inherit;border-radius:8px;padding:4px 10px;font:600 12.5px system-ui,sans-serif;cursor:pointer;opacity:.8;white-space:nowrap;line-height:1.2}',
 '.nsl-b svg{width:13px;height:13px}',
 '.nsl-b.nsl-i{flex:none!important;width:30px!important;height:30px!important;min-width:30px!important;padding:0!important;justify-content:center;border-radius:50%!important;margin:0 2px 0 6px!important;opacity:.8;font-size:0!important;line-height:0!important}.nsl-b.nsl-i svg{width:17px!important;height:17px!important;flex:none}',
 '.nsl-y{position:fixed;top:calc(env(safe-area-inset-top,0px) + 70px);right:10px;z-index:9990;background:#fff;color:#2a2a2a;border-color:#d9d2c4;opacity:.95;box-shadow:0 1px 3px rgba(0,0,0,.12)}'
].join('\n');
document.head.appendChild(css);
function gorulduMu(b) { try { return !!localStorage.getItem('mihrab.nasil.' + b); } catch (e) { return true; } }
function gorulduYap(b) { try { localStorage.setItem('mihrab.nasil.' + b, '1'); } catch (e) {} }
var acik = null;
function ac(b, bitince) {
  var D = N[b]; if (!D || acik) return; gorulduYap(b);
  var S = D.s.slice(); if (D.video) S.unshift(['video', D.ad, '']);
  var k = document.createElement('div'); k.className = 'nsl-k'; k.style.setProperty('--nr', D.renk); k.setAttribute('role', 'dialog'); k.setAttribute('aria-label', 'Nasıl çalışılır: ' + D.ad);
  k.innerHTML = '<div class="nsl-u"><span>' + D.ad + ' · Nasıl çalışılır</span><button data-x>Kapat</button></div><div class="nsl-c">' + S.map(function () { return '<i></i>'; }).join('') + '</div><div class="nsl-g"></div><div class="nsl-a"><button class="ger" data-g="-1">‹ Geri</button><button class="ile" data-g="1"></button></div>';
  document.body.appendChild(k); acik = k; var ovf = document.documentElement.style.overflow; document.documentElement.style.overflow = 'hidden';
  requestAnimationFrame(function () { k.classList.add('on'); });
  var i = -1, G = k.querySelector('.nsl-g'), C = k.querySelectorAll('.nsl-c i'), GER = k.querySelector('.ger'), ILE = k.querySelector('.ile'), ger = 0;
  function kapat() { document.removeEventListener('keydown', tus); var v = G.querySelector('video'); if (v) try { v.pause(); } catch (e) {} k.classList.remove('on'); setTimeout(function () { try { k.remove(); } catch (e) {} }, 200); acik = null; document.documentElement.style.overflow = ovf; if (bitince) try { bitince(); } catch (e) {} }
  function ciz() { var s = S[i];
    for (var x = 0; x < C.length; x++) C[x].className = x <= i ? 'on' : '';
    if (s[0] === 'video') G.innerHTML = '<video src="' + D.video + '" autoplay muted playsinline controls preload="metadata"></video>';
    else G.innerHTML = '<div class="no"><b>' + (i + 1) + '</b> / ' + S.length + '</div><div class="cz"></div><h2>' + s[1] + '</h2><p>' + s[2] + '</p>';
    var v = G.querySelector('video'); if (v) { v.onerror = function () { if (S[i] && S[i][0] === 'video') git(1); }; try { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); } catch (e) {} }
    GER.disabled = i === 0; ILE.textContent = i === S.length - 1 ? 'Başla' : 'İleri';
    G.classList.remove('gec'); }
  function git(d) { var n = i + d; if (n >= S.length) return kapat(); if (n < 0) return; var v = G.querySelector('video'); if (v) try { v.pause(); } catch (e) {}
    i = n; if (ger) clearTimeout(ger); G.classList.add('gec'); ger = setTimeout(ciz, i === 0 && !G.innerHTML ? 0 : 160); }
  function tus(e) { if (e.key === 'Escape') kapat(); else if (e.key === 'ArrowRight' || e.key === 'Enter') git(1); else if (e.key === 'ArrowLeft') git(-1); }
  k.addEventListener('click', function (e) { if (e.target.closest('[data-x]')) return kapat(); var g = e.target.closest('[data-g]'); if (g) git(+g.getAttribute('data-g')); });
  document.addEventListener('keydown', tus);
  i = 0; ciz();
}
function dugme(b) {
  var SV = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="8" cy="8" r="6.5"/><path d="M6.3 6.2a1.8 1.8 0 1 1 2.5 1.7c-.5.2-.8.6-.8 1.1M8 11.2v.1" stroke-linecap="round"/></svg>';
  var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'nsl-b'; btn.title = 'Nasıl çalışılır'; btn.setAttribute('aria-label', 'Nasıl çalışılır');
  btn.onclick = function (e) { e.preventDefault(); e.stopPropagation(); ac(b); };
  var ust = document.querySelector('#hd .top');
  if (ust) { btn.innerHTML = SV + 'Nasıl çalışılır'; var son = ust.lastElementChild;
    if (son && son.tagName === 'SPAN' && !son.textContent.trim()) { son.replaceWith(btn); btn.style.marginLeft = 'auto'; }
    else { var h = ust.querySelector('h1'); if (h && h.nextSibling) ust.insertBefore(btn, h.nextSibling); else ust.appendChild(btn); btn.style.margin = '0 6px'; }
    return btn; }
  /* Diğer sayfalar: üst çubuğun içine yalnız küçük bir “?” simgesi (yazı ve düğmelerin üstüne binmez) */
  btn.innerHTML = SV; btn.classList.add('nsl-i');
  var bar = null, A = document.querySelectorAll('#top, header, .top, .bar, .ust, nav');
  for (var x = 0; x < A.length; x++) { var r = A[x].getBoundingClientRect(), st = getComputedStyle(A[x]);
    if (r.top < 12 && r.height > 30 && r.height < 130 && r.width > innerWidth * .8 && (st.position === 'fixed' || st.position === 'sticky' || r.top >= 0) && st.display !== 'none') { bar = A[x]; break; } }
  if (bar) { var sag = bar.querySelector('.sag'); if (sag) sag.insertBefore(btn, sag.firstChild); else { bar.appendChild(btn); } }
  else { btn.classList.add('nsl-y'); document.body.appendChild(btn); }
  return btn;
}
/* Sayfa tamamen yüklenip boşa çıkınca aç; açılış sırasında takılma olmasın */
function bosta(f) { var go = function () { (window.requestIdleCallback || function (c) { setTimeout(c, 300); })(function () { setTimeout(f, 250); }, { timeout: 1500 }); };
  if (document.readyState === 'complete') go(); else addEventListener('load', go, { once: true }); }
window.Nasil = { ac: ac, gorulduMu: gorulduMu, gorulduYap: gorulduYap, bosta: bosta, N: N };
if (B && N[B]) {
  var bas = function () { bosta(function () { try { if (!document.querySelector('.nsl-b')) dugme(B); } catch (e) {} if (!gorulduMu(B)) ac(B); }); };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bas); else bas();
}
})();
