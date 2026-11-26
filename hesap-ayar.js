/* el-Mihrâb · Hesap ayarı (Firebase). Bu bilgiler gizli değildir; güvenlik Firestore kurallarıyla sağlanır (firestore.rules).
   Kurulum: HESAP-KURULUM.md. Değerler girilene kadar giriş düğmesi görünmez ve site eskisi gibi çalışır. */
window.HESAP_AYAR = {
  apiKey: "AIzaSyAGotRPSKBlgUZOB4YoNDZ6Aio9c3YdlBo",
  /* el-mihrab.com’da giriş kendi alan adımızdan geçer (functions/__/auth); diğer adreslerde Firebase’in alan adı kullanılır. */
  authDomain: /^(www\.)?el-mihrab\.com$/.test(location.hostname) ? location.hostname : "el-mihrab.firebaseapp.com",
  projectId: "el-mihrab",
  appId: "1:917596621684:web:f0f24afdb1816df01afa21"
};
/* Örnek:
window.HESAP_AYAR = {
  apiKey: "AIza…",
  /* el-mihrab.com’da giriş kendi alan adımızdan geçer (functions/__/auth); diğer adreslerde Firebase’in alan adı kullanılır. */
  authDomain: /^(www\.)?el-mihrab\.com$/.test(location.hostname) ? location.hostname : "el-mihrab.firebaseapp.com",
  projectId: "el-mihrab",
  appId: "1:…:web:…"
};
*/

/* Kadem satışı. odemeLinki: iyzico panelinde oluşturulan 250 TL'lik "Linkle Ödeme" adresi.
   Boş kaldıkça satın alma düğmesi görünmez; Google ile giriş ve eski şifreyle giriş çalışmaya devam eder.
   Satın alma düğmesi Android uygulamasında (Google Play) gösterilmez: Play, dijital içeriği yalnız kendi ödeme sistemiyle sattırır. */
window.KADEM_SATIS = {
  fiyat: '250 TL',
  sure: '1 yıl',
  odemeLinki: '',
  iletisim: ''
};
