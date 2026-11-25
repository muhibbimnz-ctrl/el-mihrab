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
