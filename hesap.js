/* el-Mihrâb · Hesap: Google (Gmail) ile giriş / kayıt ve ilerlemenin hesapta saklanması.
   - Altyapı: Firebase Authentication (Google) + Cloud Firestore. Ayarlar hesap-ayar.js içinde; ayar yoksa bu dosya hiçbir şey yapmaz.
   - İlk giriş = kayıt: kullanicilar/{uid} belgesi oluşturulur (ad, e-posta, kayıt tarihi).
   - Eşitleme: tarayıcıda (localStorage) tutulan ilerleme (Kadem, Medrese, sözlük, zikir, okuma yeri…) anahtar anahtar,
     son değişen kazanır kuralıyla hesaba yazılır ve başka cihazda geri yüklenir.
   - Hesaba GİTMEYENLER: Kadem şifre anahtarı (kadem.anahtar), özel hâller kaydı (mihrab.ozel), hata kayıtları, Firebase'in kendi kayıtları.
   Sayfaya eklemek: <script src="hesap-ayar.js"></script><script src="hesap.js" defer></script>
   Düğme: ana sayfada üst çubukta kendiliğinden çıkar; başka sayfada <span data-hesap></span> konan yere yerleşir. */
(function(){
'use strict';
var A = window.HESAP_AYAR;
if (!A || !A.apiKey || !A.projectId) return;            // kurulum yapılmadıysa sessiz kal
var CDN = 'https://www.gstatic.com/firebasejs/10.12.2/';
var HARIC = /^(kadem\.anahtar|hesap\.|firebase:|mihrab\.sonhata|mihrab\.persist|mihrab\.ozel|__)/;     // mihrab.ozel: kadın özel hâller kaydı yalnız telefonda kalır
var SINIR = 900000;                                      // Firestore belge sınırı 1 MB; pay bırakılır
var LS; try { LS = window.localStorage; LS.getItem('x') } catch (e) { return }
function J(k, d) { try { var v = LS.getItem(k); return v ? JSON.parse(v) : d } catch (e) { return d } }
function Y(k, v) { try { LS.setItem(k, JSON.stringify(v)) } catch (e) {} }
function ozet(s) { var h = 2166136261; for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619) } return (h >>> 0).toString(36) + ':' + s.length }

/* Yerel değişiklikleri işaretle: her anahtarın son değiştiği an (hesap.zaman) */
function yerel() {
  var son = J('hesap.son', {}), z = J('hesap.zaman', {}), o = {}, now = Date.now(), k, i;
  for (i = 0; i < LS.length; i++) { k = LS.key(i); if (k && !HARIC.test(k)) o[k] = LS.getItem(k) }
  for (k in o) { var h = ozet(o[k]); if (son[k] !== h) { son[k] = h; z[k] = now } }
  for (k in son) if (!(k in o)) { delete son[k]; z[k] = now }          // silinen anahtar: silinme anı tutulur
  Y('hesap.son', son); Y('hesap.zaman', z);
  return { o: o, z: z };
}

var F = null, U = null, durum = 'bekliyor', sonEsit = J('hesap.sonEsit', 0), degisti = false;
function yukle() {
  if (F) return F;
  F = Promise.all(['firebase-app.js', 'firebase-auth.js', 'firebase-firestore.js'].map(function (f) { return import(CDN + f) }))
    .then(function (m) {
      var app = m[0].initializeApp(A), auth = m[1].getAuth(app), db = m[2].getFirestore(app);
      auth.languageCode = 'tr';
      return { app: m[0], au: m[1], fs: m[2], auth: auth, db: db };
    });
  F.catch(function () { F = null });
  return F;
}

/* Eşitleme: buluttaki ile yereli birleştir, sonucu iki tarafa yaz */
var esitleniyor = null;
function esitle(neden) {
  if (!U) return Promise.resolve();
  if (esitleniyor) return esitleniyor;
  esitleniyor = yukle().then(function (f) {
    var ref = f.fs.doc(f.db, 'kullanicilar', U.uid);
    return f.fs.getDoc(ref).then(function (s) {
      var bulut = s.exists() ? s.data() : null, b = { d: {}, z: {} };
      try { if (bulut && bulut.veri) b = JSON.parse(bulut.veri) } catch (e) {}
      var L = yerel(), son = J('hesap.son', {}), uygulanan = 0, k;
      var anahtar = {}; for (k in L.z) anahtar[k] = 1; for (k in b.z) anahtar[k] = 1;
      var d = {}, z = {}, ilkKez = J('hesap.esitUid', null) !== U.uid, yedek = J('hesap.yedek', {});
      for (k in anahtar) {
        if (HARIC.test(k)) continue;
        var lt = L.z[k] || 0, bt = b.z[k] || 0, bulutta = k in b.d, yerelde = k in L.o;
        /* Bu cihazın bu hesapla ilk eşitlemesi: zamana değil içeriğe bak; iki tarafta da varsa dolu olan kazanır */
        var bulutKazanir = ilkKez && bulutta ? (b.d[k] != null && (!yerelde || b.d[k].length > L.o[k].length)) : bt > lt;
        if (ilkKez && bulutta && !bulutKazanir) lt = Math.max(lt, bt + 1);
        if (bulutKazanir) {                                      // buluttaki → cihaza yaz
          var v = b.d[k];
          if (yerelde && L.o[k] !== v) yedek[k] = L.o[k];
          try { if (v == null) LS.removeItem(k); else LS.setItem(k, v) } catch (e) { continue }
          if (v == null) delete son[k]; else son[k] = ozet(v);
          L.z[k] = bt; uygulanan++;
          d[k] = v == null ? null : v; z[k] = Math.max(bt, 1);
        } else {
          d[k] = k in L.o ? L.o[k] : null; z[k] = lt; L.z[k] = lt;
        }
      }
      Y('hesap.son', son); Y('hesap.zaman', L.z); try { LS.setItem('hesap.yedek', JSON.stringify(yedek)) } catch (e) {}
      /* Büyük kayıtlar belgeyi şişirmesin: en büyükten başlayarak dışarıda bırak (cihazda kalır) */
      var metin = JSON.stringify({ d: d, z: z }), disari = [];
      if (metin.length > SINIR) {
        Object.keys(d).filter(function (x) { return d[x] }).sort(function (x, y) { return d[y].length - d[x].length })
          .some(function (x) { disari.push(x); delete d[x]; delete z[x]; metin = JSON.stringify({ d: d, z: z }); return metin.length <= SINIR });
      }
      var kayit = {
        veri: metin, ad: U.displayName || '', eposta: U.email || '', foto: U.photoURL || '',
        sonGiris: f.fs.serverTimestamp(), cihaz: (navigator.userAgent || '').slice(0, 160)
      };
      if (!bulut) kayit.kayitTarihi = f.fs.serverTimestamp();
      return f.fs.setDoc(ref, kayit, { merge: true }).then(function () {
        sonEsit = Date.now(); Y('hesap.sonEsit', sonEsit); Y('hesap.esitUid', U.uid); degisti = false; durum = 'tamam'; ciz();
        if (uygulanan && neden === 'acilis' && !sessionStorage.getItem('hesap.yenilendi')) {
          sessionStorage.setItem('hesap.yenilendi', '1');
          bildir('İlerlemen hesabından yüklendi'); setTimeout(function () { location.reload() }, 900);
        } else if (uygulanan) bildir('İlerlemen hesabından yüklendi');
        if (disari.length) console.warn('Hesap: çok büyük olduğu için eşitlenmeyen kayıtlar', disari);
      });
    });
  }).catch(function (e) { durum = 'hata'; ciz(); console.warn('Hesap eşitleme', e) })
    .then(function () { esitleniyor = null });
  return esitleniyor;
}

function giris() {
  return yukle().then(function (f) {
    var p = new f.au.GoogleAuthProvider(); p.setCustomParameters({ prompt: 'select_account' });
    return f.au.signInWithPopup(f.auth, p).catch(function (e) {
      if (e && /popup-blocked|operation-not-supported|popup-closed-by-browser/.test(e.code || '')) return f.au.signInWithRedirect(f.auth, p);
      throw e;
    });
  }).catch(function (e) {
    if (e && /popup-closed-by-user|cancelled-popup-request/.test(e.code || '')) return;
    bildir('Giriş yapılamadı' + (e && e.code === 'auth/unauthorized-domain' ? ': bu adres Firebase’de yetkili değil' : ''));
    console.warn('Hesap giriş', e);
  });
}
function cikis() {
  return esitle('cikis').then(yukle).then(function (f) { return f.au.signOut(f.auth) }).then(function () {
    try { LS.removeItem('hesap.uid') } catch (e) {} bildir('Çıkış yapıldı. İlerlemen bu cihazda da duruyor.');
  });
}

/* Görünüm */
var css = '.hs-b{width:38px;height:38px;border-radius:50%;border:0;background:transparent;padding:0;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;color:inherit;flex:none}' +
  '.hs-b img{width:28px;height:28px;border-radius:50%;display:block}.hs-b svg{width:24px;height:24px}' +
  '.hs-ov{position:fixed;inset:0;background:rgba(10,16,32,.62);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);z-index:9999;display:flex;align-items:center;justify-content:center;padding:18px;animation:hsF .2s ease}' +
  '@keyframes hsF{from{opacity:0}to{opacity:1}}@keyframes hsY{from{transform:translateY(14px);opacity:0}to{transform:none;opacity:1}}' +
  '.hs-k{position:relative;background:#FBF7EE;color:#1d2430;border-radius:22px;max-width:390px;width:100%;padding:0 0 18px;font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;box-shadow:0 24px 60px rgba(0,0,0,.35);text-align:center;overflow:hidden;animation:hsY .25s ease}' +
  '.hs-bas{background:linear-gradient(160deg,#2B3D6E,#17224A);color:#F4E6C6;padding:26px 22px 22px;position:relative}' +
  '.hs-bas:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:14px;background:#FBF7EE;border-radius:22px 22px 0 0}' +
  '.hs-lg{width:62px;height:62px;border-radius:16px;display:block;margin:0 auto 10px;box-shadow:0 6px 18px rgba(0,0,0,.3);border:2px solid rgba(244,230,198,.5)}' +
  '.hs-bas h3{margin:0;font:600 23px/1.25 Georgia,"Times New Roman",serif;color:#F4E6C6;letter-spacing:.2px}.hs-bas p{margin:6px 0 0;font-size:13.5px;color:rgba(244,230,198,.85)}' +
  '.hs-ic{padding:6px 22px 0}.hs-ic p{margin:8px 0;color:#4a4f58}.hs-k small{color:#7a7466;font-size:12.5px}.hs-k small a{color:#2B3D6E}' +
  '.hs-fy{list-style:none;margin:10px 0 6px;padding:0;text-align:left;display:grid;gap:8px}.hs-fy li{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:#2f3540;line-height:1.45}' +
  '.hs-fy i{flex:none;width:22px;height:22px;border-radius:50%;background:#E8E2D2;color:#2B3D6E;font:700 12px/22px system-ui;font-style:normal;text-align:center}' +
  '.hs-k img.f{width:72px;height:72px;border-radius:50%;border:3px solid rgba(244,230,198,.7);display:block;margin:0 auto 10px}' +
  '.hs-g{display:flex;align-items:center;justify-content:center;gap:12px;width:100%;margin:16px 0 8px;padding:13px 14px;border:1px solid #d9d3c4;border-radius:14px;background:#fff;color:#1f1f1f;font:600 15.5px system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;cursor:pointer;box-shadow:0 2px 6px rgba(0,0,0,.08);transition:box-shadow .15s,transform .15s}' +
  '.hs-g:hover{box-shadow:0 4px 14px rgba(0,0,0,.14)}.hs-g:active{transform:scale(.985)}.hs-g:disabled{opacity:.6}' +
  '.hs-s{display:block;width:100%;margin:8px 0;padding:12px;border:0;border-radius:14px;background:#2B3D6E;color:#F4E6C6;font:600 15px system-ui,-apple-system,"Segoe UI",sans-serif;cursor:pointer}.hs-s.ik{background:transparent;color:#5b5f68;font-weight:500;margin-top:2px}' +
  '.hs-kp{position:absolute;top:10px;right:12px;z-index:2;width:32px;height:32px;border:0;border-radius:50%;background:rgba(244,230,198,.14);color:#F4E6C6;font:20px/32px system-ui;cursor:pointer}' +
  '@media (prefers-color-scheme:dark){.uyg .hs-k{background:#141B2E;color:#E9E4D8}.uyg .hs-bas:after{background:#141B2E}.uyg .hs-ic p,.uyg .hs-fy li{color:#cfd3dc}.uyg .hs-fy i{background:#24304F;color:#F4E6C6}}' +
  '.hs-t{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:#1f2a24;color:#fff;padding:9px 16px;border-radius:20px;font:14px system-ui,sans-serif;z-index:10000;box-shadow:0 6px 18px #0004}';
var G = '<svg viewBox="0 0 48 48" width="20" height="20"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>';
var KISI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg>';
function e(s) { return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] }) }
function bildir(m) { var t = document.createElement('div'); t.className = 'hs-t'; t.textContent = m; document.body.appendChild(t); setTimeout(function () { t.remove() }, 3200) }
var dugmeler = [];
function ciz() {
  dugmeler.forEach(function (b) {
    b.innerHTML = U && U.photoURL ? '<img src="' + e(U.photoURL) + '" alt="" referrerpolicy="no-referrer">' : KISI;
    b.title = U ? (U.displayName || U.email) + ' · hesabım' : 'Google ile giriş / kayıt';
  });
  var k = document.querySelector('.hs-k'); if (k) pencere(true);
}
function zaman(t) { if (!t) return 'henüz yok'; var s = Math.round((Date.now() - t) / 1000); return s < 60 ? 'az önce' : s < 3600 ? Math.round(s / 60) + ' dk önce' : new Date(t).toLocaleString('tr-TR') }
function pencere(yenile) {
  var ov = document.querySelector('.hs-ov');
  if (!ov) { if (yenile) return; ov = document.createElement('div'); ov.className = 'hs-ov'; ov.onclick = function (x) { if (x.target === ov) ov.remove() }; document.body.appendChild(ov) }
  var ilk = pencere.ilk; pencere.ilk = false;
  ov.innerHTML = '<div class="hs-k"><button class="hs-kp" data-x="kap" aria-label="Kapat">×</button>' + (U ?
    '<div class="hs-bas">' + (U.photoURL ? '<img class="f" src="' + e(U.photoURL) + '" alt="" referrerpolicy="no-referrer">' : '<img class="hs-lg" src="icon-192.png" alt="">') +
    '<h3>' + e(U.displayName || 'Hesabım') + '</h3><p>' + e(U.email) + '</p></div>' +
    '<div class="hs-ic"><p><small>İlerlemen bu hesapta saklanıyor. Son eşitleme: ' + zaman(sonEsit) + (durum === 'hata' ? ' · <b style="color:#9e2a2b">son deneme başarısız</b>' : '') + '</small></p>' +
    '<button class="hs-s" data-x="es">Şimdi eşitle</button><button class="hs-s ik" data-x="cik">Çıkış yap</button></div>'
    :
    '<div class="hs-bas"><img class="hs-lg" src="icon-192.png" alt=""><h3>' + (ilk ? 'el-Mihrâb’a hoş geldin' : 'el-Mihrâb hesabı') + '</h3><p>İlim, ibadet ve huzur için bir yol arkadaşı</p></div>' +
    '<div class="hs-ic"><ul class="hs-fy"><li><i>✓</i><span>Kur’an, medrese, sözlük ve Kadem ilerlemen kaybolmaz</span></li>' +
    '<li><i>✓</i><span>Telefonda, bilgisayarda ve uygulamada kaldığın yerden devam edersin</span></li>' +
    '<li><i>✓</i><span>Şifre gerekmez; Gmail hesabınla tek dokunuşta girersin</span></li></ul>' +
    '<button class="hs-g" data-x="gir">' + G + 'Google ile devam et</button><button class="hs-s ik" data-x="kap">' + (ilk ? 'Girişsiz devam et' : 'Şimdi değil') + '</button>' +
    '<p><small>Yalnız adın, e-posta adresin ve ilerleme kayıtların saklanır. <a href="gizlilik.html">Gizlilik</a></small></p></div>') + '</div>';
  ov.querySelectorAll('[data-x]').forEach(function (b) {
    b.onclick = function () {
      var x = b.dataset.x;
      if (x === 'kap') ov.remove();
      else if (x === 'gir') { b.disabled = true; giris().then(function () { b.disabled = false }) }
      else if (x === 'es') { b.textContent = 'Eşitleniyor…'; esitle('el').then(function () { bildir(durum === 'hata' ? 'Eşitlenemedi; internet bağlantını kontrol et' : 'Eşitlendi') }) }
      else if (x === 'cik') { ov.remove(); cikis() }
    };
  });
}
function dugme() { var b = document.createElement('button'); b.type = 'button'; b.className = 'hs-b'; b.onclick = function () { pencere() }; dugmeler.push(b); return b }

function kur() {
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  var yer = document.querySelectorAll('[data-hesap]');
  if (yer.length) yer.forEach(function (y) { y.appendChild(dugme()) });
  else { var ay = document.getElementById('setB'); if (ay && ay.parentNode) ay.parentNode.insertBefore(dugme(), ay) }
  ciz();
  var giris_yapilmis = !!J('hesap.uid', null);
  /* Firebase yalnız düğmesi olan sayfada ya da daha önce giriş yapılmışsa yüklenir (sayfa hızı için) */
  if (!dugmeler.length && !giris_yapilmis && !document.documentElement.hasAttribute('data-hesap-yukle')) return;
  var ilk = true;
  var karsila = !!document.getElementById('home') && !J('hesap.uid', null) && !J('hesap.karsilandi', 0);
  if (karsila) setTimeout(function () { if (!U && !document.querySelector('.hs-ov')) { Y('hesap.karsilandi', Date.now()); pencere.ilk = true; pencere() } }, 2200);
  yukle().then(function (f) {
    f.au.getRedirectResult(f.auth).catch(function () {});
    f.au.onAuthStateChanged(f.auth, function (u) {
      var onceki = U; U = u || null;
      if (U) { Y('hesap.uid', U.uid); esitle(ilk ? 'acilis' : 'giris').then(function () { if (!onceki && !ilk) bildir('Hoş geldin, ' + (U.displayName || U.email)) }) }
      else try { LS.removeItem('hesap.uid') } catch (e) {}
      ilk = false; ciz(); bildirOturum();
    });
  }).catch(function (x) { console.warn('Hesap yüklenemedi', x) });
  /* Değişiklik olunca: sayfadan çıkarken ve en geç 2 dakikada bir eşitle */
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden' && U) esitle('cikis-sayfa') });
  setInterval(function () { if (U && document.visibilityState === 'visible') { var L = yerel(), d = false; for (var k in L.z) if ((L.z[k] || 0) > sonEsit) { d = true; break } if (d) esitle('aralik') } }, 120000);
}
/* Kadem üyeliği için: Firebase'e erişim ve oturum değişikliği bildirimi (kadem.html, yonetim.html) */
var dinleyen = [];
function bildirOturum() { dinleyen.forEach(function (f) { try { f(U) } catch (e) {} }) }
window.Hesap = { ac: function () { pencere() }, esitle: function () { return esitle('el') }, kullanici: function () { return U },
  hazir: function () { return !!A }, firebase: function () { return A ? yukle() : Promise.reject('ayar') },
  dinle: function (f) { dinleyen.push(f); if (U) f(U) } };
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', kur); else kur();
})();
