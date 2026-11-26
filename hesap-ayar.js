/* el-Mihrâb · Hesap ayarı (Firebase). Bu bilgiler gizli değildir; güvenlik Firestore kurallarıyla sağlanır (firestore.rules).
   Kurulum: HESAP-KURULUM.md. Değerler girilene kadar giriş düğmesi görünmez ve site eskisi gibi çalışır. */
window.HESAP_AYAR = {
  apiKey: "AIzaSyAGotRPSKBlgUZOB4YoNDZ6Aio9c3YdlBo",
  /* el-mihrab.com’da giriş kendi alan adımızdan geçer (functions/__/auth; Google Cloud’da yönlendirme adresi kayıtlı). Diğer adreslerde Firebase’in alan adı. */
  authDomain: /^(www\.)?el-mihrab\.com$/.test(location.hostname) ? location.hostname : "el-mihrab.firebaseapp.com",
  projectId: "el-mihrab",
  appId: "1:917596621684:web:f0f24afdb1816df01afa21"
};

/* Kadem satışı. odemeLinki: iyzico panelinde oluşturulan 250 TL'lik "Linkle Ödeme" adresi.
   Boş kaldıkça satın alma düğmesi görünmez; Google ile giriş ve eski şifreyle giriş çalışmaya devam eder.
   Satın alma düğmesi Android uygulamasında (Google Play) gösterilmez: Play, dijital içeriği yalnız kendi ödeme sistemiyle sattırır. */
/* Üyelik paketleri. "link": iyzico'da her paket için oluşturulan ödeme linki; boşsa satın alma butonu görünmez.
   Paketin Firestore karşılığı: uyeler/{eposta}.paketler içinde id ("mbsts", "yds", "max"). */
window.KADEM_SATIS = {
  sure: '1 yıl',
  paketler: [
    { id: 'mbsts', ad: 'Pro · MBSTS', fiyat: '300 TL', kapsam: 'DİB-MBSTS: bütün konu anlatımları, kartlar, testler ve tam denemeler', link: '' },
    { id: 'yds', ad: 'Pro · YDS Arapça', fiyat: '300 TL', kapsam: 'YDS Arapça: 12 tam deneme, konu konu sorular, kelime kartları ve okuma metinleri', link: '' },
    { id: 'max', ad: 'Max', fiyat: '500 TL', kapsam: 'Kadem’deki bütün sınavlar (MBSTS, DHBT, ihtisas, murakıplık, yurt dışı ve diğerleri) ile YDS Arapça', link: '' }
  ],
  iletisim: ''
};
