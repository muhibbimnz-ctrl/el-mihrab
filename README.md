# el-Mihrâb — Kur'ân-ı Kerîm ve Tefsîri

Kur'an metni, meâller, tefsir, i'râb, belâgat, kıraat, nüzûl ve garîb kitapları tek sayfada.

Adres: https://muhibbimnz-ctrl.github.io/el-mihrab/

لَا تَنْسَوْنِي مِنْ صَالِحِ دُعَائِكُمْ — Beni hayır dualarınızda unutmayın.

## Namaz ve Kur'an menüsü (25 Kasım 2026)
- Menü `index.html` içindeki `#namaz` ekranıdır: arama, vakit satırı, kaldığın yer ve gruplu simge ızgarası. Öğeler `NMG` (grup, simge, ad, arama kelimeleri), simgeler `NI`, tıklama davranışı `NA` içinde.
- Yeni sayfalar ortak `arac.css` ve `arac.js` kullanır: `kible.html`, `kaza.html`, `ozel.html`, `hatim.html`, `haber.html`, `soru.html`, `cami.html`. `./#namaz` menüyü, `./#okuma` mushafı açar.
- Telefonda saklananlar: `mihrab.kaza`, `mihrab.hatim`, `mihrab.ozel` (hesaba gönderilmez), `mihrab.soru`.
- **Haber eklemek:** `data/haber.json` içindeki `haberler` listesine en üste bir kayıt ekleyin (`tarih`, `etiket`, `baslik`, `ozet`, `kaynak`, `link`) ve `guncelleme` tarihini değiştirin. Sayfa her açılışta önce internetten okur; sürüm artırmak gerekmez. Özet kendi cümlelerimizle yazılır.
- Soru-Cevap, `data/fikih/meseleler.json` ve `adim.json` üzerinde telefonda arama yapar; `fikih.html`'deki `HV` değişirse `soru.html`'deki `?v=` de aynı yapılmalı.
- **Haberler kendiliğinden güncellenir:** `.github/workflows/haber.yml` her sabah 07:00'de (Türkiye) `tools/haber_guncelle.py`'yi çalıştırır. Betik Google Haberler aramalarından (Diyanet, cami/hutbe, kandil/hac, Gazze/Kudüs/Aksa, Müslümanlar/İslamofobi, Doğu Türkistan/Arakan/Keşmir, İİT) son 2 günün haberlerini alır; en çok 8 yenisini başlık + kaynak + bağlantı olarak ekler (`"oto": true`), listeyi 60 haberde tutar. Elle eklenen haberler korunur. Aramaları değiştirmek için betikteki `ARAMALAR` listesi düzenlenir. Elle çalıştırmak: GitHub > Actions > "Haberleri güncelle" > Run workflow.
- **Fetva asistanı (`soru.html`):** Soru önce telefonda meselelerde aranır; en yakın meseleler `functions/api/fetva.js`'ye (Cloudflare Pages Function) gönderilir ve Cloudflare Workers AI modeli yalnız bu meselelere dayanarak cevap yazar. Çalışması için Cloudflare panelinde Pages projesi > Settings > Bindings > Add > **Workers AI**, değişken adı **AI** eklenmelidir (ücretsiz günlük kota yeter). Bağlantı yoksa asistan cevabı meselelerden kendisi kurar.
- **İlmihal:** Namaz ve Kur'an menüsündeki İlmihal, `fikih.html?ilmihal` açar: yalnız adım adım uygulamalar ve ibadet babları (Tahâret, Namaz, Oruç, Zekât, Hac, Kurban). `&bab=Hac` gibi tek bab da açılabilir.
- **Hac ve Umre (`hac.html`):** Umre, hac, ihram, Medine ve dualar; fotoğraflar Wikimedia Commons'tan `Special:FilePath` ile gelir (yüklenmezse gizlenir).
- **Mushaf:** Alt çubuk (Hız = otomatik kaydırma, Tefsir, sayfa, Git, Ayarlar), âyete dokununca Dinle/Tefsir/Meâl/Kopyala, Allah lafzı renkli. Ayarlar: `okSz`, `okLh`, `okZemin`, `okMedine`.
