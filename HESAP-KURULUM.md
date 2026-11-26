# Google (Gmail) ile giriş: kurulum

Kod hazır (`hesap.js`, `hesap-ayar.js`, `firestore.rules`). Bütün sayfalara eklendi. `hesap-ayar.js` içindeki `HESAP_AYAR` boş (`null`) kaldıkça giriş düğmesi görünmez, site eskisi gibi çalışır.

## Nasıl çalışır
- Ana sayfada üst çubukta (Ayarlar düğmesinin solunda) ve Kadem'in üst çubuğunda kişi simgesi çıkar. Dokununca "Google ile giriş yap / kayıt ol" penceresi açılır.
- İlk giriş kayıttır: Firestore'da `kullanicilar/{uid}` belgesi açılır (ad, e-posta, kayıt tarihi, son giriş).
- Tarayıcıdaki ilerleme (Kadem, Medrese, sözlük, zikir, okuma yeri, ayarlar) anahtar anahtar hesaba yazılır. Sayfadan çıkarken ve açıkken 2 dakikada bir eşitlenir.
- Kural: son değişen kazanır. Bir cihazın bu hesapla ilk eşitlemesinde ise iki tarafta da olan kayıtta dolu olan kazanır, üzerine yazılan sürüm cihazda `hesap.yedek` içinde saklanır. Böylece yeni telefonun boş kaydı eski ilerlemeyi silmez.
- Hesaba gitmeyenler: `kadem.anahtar` (Kadem şifre anahtarı; yeni cihazda şifre bir kez daha girilir), hata kayıtları, Firebase'in kendi kayıtları.
- Aynı kod el-mihrab.com (Cloudflare Pages), muhibbimnz-ctrl.github.io/el-mihrab ve Android uygulamasında (TWA) çalışır; hepsi aynı hesabı kullanır.

## Firebase'de yapılacaklar (bir kez)
1. https://console.firebase.google.com → **Proje ekle** → ad: `el-mihrab` (Google Analytics gerekmez).
2. **Authentication** → Başlayın → **Sign-in method** → **Google** → Etkinleştir → destek e-postasını seç → Kaydet.
3. Authentication → **Settings** → **Yetkili alan adları** → şunları ekle:
   `el-mihrab.com`, `www.el-mihrab.com`, `el-mihrab.pages.dev`, `muhibbimnz-ctrl.github.io`
4. **Firestore Database** → Veritabanı oluştur → konum `eur3 (Europe)` → **üretim modu**. Sonra **Kurallar** sekmesine `firestore.rules` dosyasının içeriğini yapıştır → Yayınla.
5. **Proje ayarları** (dişli) → Genel → Uygulamalarınız → **Web (</>)** → takma ad `el-mihrab-web` → Kaydet. Çıkan `firebaseConfig` içindeki `apiKey`, `authDomain`, `projectId`, `appId` değerlerini `hesap-ayar.js` dosyasına yaz.
6. `hesap-ayar.js?v=1` ve `hesap.js?v=1` sürümlerini bütün sayfalarda ve `sw.js` içinde bir artır, `sw.js` sürümünü artır, `python3 tools/kontrol.py`, commit, push.

Not: Bu değerler gizli değildir; erişimi `firestore.rules` sınırlar (herkes yalnız kendi belgesini görür).

## Yayından sonra
- Google Play'de uygulamanın **Veri güvenliği** formu güncellenmeli: ad, e-posta (hesap yönetimi için, isteğe bağlı), uygulama etkinliği (ilerleme). Silme isteği: gizlilik sayfasındaki iletişim.
- `gizlilik.html` hesap bölümüyle güncellendi (25 Kasım 2026).

---

# Kadem üyeliği (ücretli erişim, iyzico)

Kod hazır: `kadem.html` (giriş ekranı), `yonetim.html` (üye paneli), `firestore.rules`, `hesap-ayar.js` içindeki `KADEM_SATIS`.
Firebase ayarı (yukarıdaki 1-6) yapılmadan hiçbiri görünmez; Kadem eskisi gibi şifreyle açılır.

## Nasıl çalışır
- Kişi Kadem’de **Google ile giriş yapar**, sonra **Kartla satın al** düğmesiyle iyzico ödeme sayfasına gider. Ödeme formunda e-posta olarak Gmail adresini yazar.
- Ödeme sana iyzico’dan bildirilir. **yonetim.html** sayfasına girip o Gmail’i yazarsın (1 yıl) → üyelik açılır.
- Kişi Kadem’i açtığında (ya da “Üyeliğimi kontrol et”e bastığında) anahtar Firestore’dan gelir, bütün içerik açılır. Süre dolunca cihazdaki anahtar silinir.
- Eski şifreyle girenler etkilenmez (“Şifrem var” bölümü duruyor).
- **Google Play uygulamasında satın alma düğmesi gösterilmez.** Play, uygulama içinde satılan dijital içerik için kendi ödeme sistemini zorunlu tutar. Uygulamada yalnız Google ile giriş vardır; web’den satın alan kişi uygulamada da aynı hesapla girer.

## Bir kez yapılacaklar
1. Firebase kurulumu (yukarıdaki 1-6).
2. Firestore → **Kurallar**: güncel `firestore.rules` içeriğini yapıştır → Yayınla.
3. Firestore → **Veri** → koleksiyon başlat: `yoneticiler` → belge kimliği: kendi Gmail adresin (küçük harfle) → bir alan ekle (ör. `ad`: adın) → Kaydet.
4. Siteden `yonetim.html` sayfasını aç → Google ile gir → **Kadem anahtarı** bölümüne Kadem şifresini bir kez yaz → Anahtarı kaydet.
5. iyzico → **Linkle Ödeme Al** (bireysel) başvurusu → onaydan sonra 250 TL’lik bir ürün linki oluştur (ürün adı: “el-Mihrâb Kadem – 1 yıllık erişim”; açıklamaya “Ödeme formuna Google ile giriş yaptığınız Gmail adresinizi yazın” notunu ekle).
6. `hesap-ayar.js` → `KADEM_SATIS.odemeLinki` alanına linki, `iletisim` alanına (isteğe bağlı) bir iletişim adresi yaz; sürümleri artır, kontrol, commit, push.

## Satış ve iade metinleri
Satış sayfasına (gizlilik.html’e bölüm olarak) kısa “Satış ve iade koşulları” ile “KVKK aydınlatma” metni eklenmeli: dijital içerik ödeme onayıyla hemen açıldığı için cayma hakkının nasıl işleyeceği, toplanan veri (Gmail adresi, üyelik süresi) ve silme talebi.
