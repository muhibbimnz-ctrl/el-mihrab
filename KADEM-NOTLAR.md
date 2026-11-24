# Kadem — Devam Notları

Diyanet personeli için sınav hazırlık bölümü. Her çalışma oturumunun sonunda bu dosya güncellenir.
Yeni bir sohbete başlarken: "el-mihrab deposundaki KADEM-NOTLAR.md dosyasını oku, kaldığımız yerden devam edelim" demen yeterli.

## Yapı
- Sayfa: `kadem.html` (ana sayfadaki "Kadem" kutucuğu buraya açılır)
- Sınav listesi: `data/kadem/sinavlar.json`
- Her sınavın içeriği: `data/kadem/<id>.json` (id: mbsts, dhbt, muftu, uzman, gys, mevzuat)
- Çevrimdışı: `sw.js` içinde kabuğa eklendi; `data/kadem/` önce ağdan, yoksa telefondaki kopyadan gelir

### `data/kadem/<id>.json` biçimi
```json
{"konular":[
  {"id":"k1","ad":"Konu adı","ders":"Fıkıh",
   "anlatim":["paragraf", {"b":"Ara başlık"}, {"not":"Önemli not"}],
   "sorular":[{"s":"Soru kökü","c":["A","B","C","D","E"],"d":0,"a":"Açıklama","kay":"Kaynak"}]}
]}
```
`d` doğru şıkkın sırasıdır (0 = A). Dosyası olmayan sınav "Hazırlanıyor" olarak görünür.

### Sayfanın yaptıkları
- Sınav listesi → sınav sayfası (konular, deneme sınavı, yanlışlarım) → konu anlatımı → konu testi
- Deneme: sınavın bütün sorularından karışık en çok 60 soru
- Yanlış yapılan sorular telefonda saklanır (`localStorage`, anahtar `kadem.v1`) ve doğru yapılınca listeden düşer

## Oturum günlüğü

### 1. oturum — 24 Kasım 2026
- Bölümün adı "Kadem" olarak seçildi.
- İskelet kuruldu: kutucuk, `kadem.html`, sınav listesi, test motoru. Henüz konu ve soru yok.
- Sınavlar: DİB-MBSTS (60 soru · 90 dk · ÖSYM), DHBT, Müftü Yardımcılığı, Din İşleri Uzmanlığı, Görevde Yükselme, Mevzuat.

### Sıradaki iş
- Kullanıcı kitaplarını yükleyecek; hangi sınavla başlanacağını seçecek.
- O sınavın güncel konu dağılımı resmî kaynaktan (ÖSYM kılavuzu / Diyanet duyurusu) doğrulanacak.
- Konu konu anlatım ve sorular `data/kadem/<id>.json` dosyasına yazılacak.
- Açık konu: bölüm ücretli mi olacak? Uygulamada şu an ödeme sistemi yok.
