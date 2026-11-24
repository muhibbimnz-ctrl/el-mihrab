# Kadem — Devam Notları

Diyanet personeli için sınav hazırlık bölümü. Her çalışma oturumunun sonunda bu dosya güncellenir.
Yeni bir sohbete başlarken: "el-mihrab deposundaki KADEM-NOTLAR.md dosyasını oku, kaldığımız yerden devam edelim" demen yeterli.

## Yapı
- Sayfa: `kadem.html` (ana sayfadaki "Kadem" kutucuğu buraya açılır)
- Sınav listesi: `data/kadem/sinavlar.json`
- Her sınavın içeriği: `data/kadem/<id>.json` — id'ler `sinavlar.json` içinde (dhbt, aday, mbsts, kbys, kurumici, ihtisas, vaizlik, ilcemuftu, muftuyrd, egitimgorevlisi, gys, murakip, diyk, diu, mufettis, yurtdisi, musavir, mevzuat, arapca)
- `sinavlar.json`'da her sınavın `grup`, `yapi` (resmî biçim/konu maddeleri) ve `kaynak` (resmî duyuru linki) alanları var; sınav sayfasında "Sınav hakkında" olarak görünür
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

### 2. oturum — 24 Kasım 2026
- Diyanet'teki sınavlar resmî kaynaklardan (ÖSYM, Diyanet İK, Dış İlişkiler, Diyanet Akademisi, mevzuat.gov.tr) tarandı.
- 19 sınav/ders, 7 grupta listelendi: Giriş (DHBT, aday din görevlisi sözlüsü) · Kariyer (MBSTS, kariyer basamakları, kurum içi unvan geçişi) · İhtisas ve vaizlik (yüksek ihtisas kursiyer seçimi, vaizliğe giriş) · Müftülük ve yönetim (ilçe müftülüğü, il müftü yardımcılığı, eğitim görevliliği, görevde yükselme, murakıplık) · Merkez (DİYK uzman yrd., Diyanet işleri uzman yrd., müfettiş yrd.) · Yurt dışı (uzun süreli din görevlisi, müşavirlik/ataşelik) · Ortak (mevzuat, Arapça).
- Her sınava resmî biçim, konu/puan dağılımı ve kaynak linki eklendi.
- İl müftülüğü sınavla değil, atama ile gelinen bir görev; ayrı sınavı yok.
- Bilgiler Kasım 2026 itibarıyla; her içerik yazımından önce o sınavın en güncel duyurusu yeniden kontrol edilmeli.

### Sıradaki iş
- Kullanıcı kitaplarını yükleyecek; hangi sınavla başlanacağını seçecek. Öneri: önce MBSTS (en geniş kitle, puanı kariyer ve yurt dışında da kullanılıyor), sonra ilçe müftülüğü / müftü yardımcılığı / kariyer basamakları (konuları ortak), ardından DHBT.
- O sınavın güncel konu dağılımı resmî kaynaktan (ÖSYM kılavuzu / Diyanet duyurusu) doğrulanacak.
- Konu konu anlatım ve sorular `data/kadem/<id>.json` dosyasına yazılacak.
- Açık konu: bölüm ücretli mi olacak? Uygulamada şu an ödeme sistemi yok.
