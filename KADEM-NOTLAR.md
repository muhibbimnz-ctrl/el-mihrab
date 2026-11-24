# Kadem — Devam Notları

Diyanet personeli için sınav hazırlık bölümü. Her çalışma oturumunun sonunda bu dosya güncellenir.
Yeni bir sohbete başlarken: "el-mihrab deposundaki KADEM-NOTLAR.md dosyasını oku, kaldığımız yerden devam edelim" demen yeterli.

## Yapı
- Sayfa: `kadem.html` (ana sayfadaki "Kadem" kutucuğu buraya açılır)
- Sınav listesi: `data/kadem/sinavlar.json`
- Her sınavın içeriği: `data/kadem/<id>.json` — id'ler `sinavlar.json` içinde (dhbt, aday, mbsts, kbys, kurumici, ihtisas, vaizlik, ilcemuftu, muftuyrd, egitimgorevlisi, gys, murakip, diyk, diu, mufettis, yurtdisi, musavir, mevzuat, arapca)
- `sinavlar.json`'da her sınavın `grup`, `yapi` (resmî biçim/konu maddeleri) ve `kaynak` (resmî duyuru linki) alanları var; sınav sayfasında "Sınav hakkında" olarak görünür
- Çevrimdışı: `sw.js` içinde kabuğa eklendi; `data/kadem/` önce ağdan, yoksa telefondaki kopyadan gelir

### `data/kadem/<id>.json` biçimi (3. oturumda genişletildi)
```json
{"deneme":{"soru":60,"dakika":90,"yanlisGoturur":false},
 "harita":{"kaynak":"…","dersler":[{"ad":"Hadis","soru":7,"uniteler":[{"ad":"…","oncelik":3,"konu":"hadis-1"}]}]},
 "konular":[{"ref":"hadis-1"}]}
```
- Konular ortak dosyalarda durur: `data/kadem/konu/<konu>.json`. Bir sınav onları `{"ref":"…"}` ile çağırır; aynı konu MBSTS, DHBT, kariyer sınavlarında tekrar yazılmadan kullanılır.
- Konu dosyası:
```json
{"id":"hadis-1","ad":"…","ders":"Hadis","sinavlar":["mbsts","dhbt"],
 "anlatim":["paragraf",{"b":"Ara başlık"},{"not":"…"},{"ayet":"meal","kay":"Nahl, 16/44"},{"hadis":"metin","kay":"Buhârî, İlim, 39"},
            {"tablo":[["başlık","başlık"],["hücre","hücre"]]},{"kontrol":"Hoca kontrolü bekleyen bilgi"}],
 "ozet":["madde"],"kartlar":[{"o":"ön yüz","a":"arka yüz"}],
 "sorular":[{"id":"h1-01","z":1,"s":"kök","c":["A","B","C","D","E"],"d":2,"a":"genel açıklama","ac":["A neden…","B neden…","…"],"kay":"kaynak"}]}
```
- `d` doğru şık (0 = A), `z` zorluk (1 kolay, 2 orta, 3 zor), `ac` her şıkkın neden doğru/yanlış olduğu, `id` kalıcı soru anahtarı (yanlış defteri buna bağlı; değiştirme).
- Konunun `ders` adı haritadaki ders adıyla birebir aynı olmalı (deneme, soruları ders ağırlığına göre bu adla seçer). Kesme işareti olarak ’ kullanılıyor: “Kur’an Bilgisi”.
- Dosyası olmayan sınav "Hazırlanıyor" olarak görünür.

### Sayfanın yaptıkları
- Sınav sayfası: deneme, bugünkü tekrar, yanlış defteri, konu haritası, derslere göre konular
- Konu: sekmeler Anlatım · Özet · Kartlar · Test. Ayet/hadis kutuları kaynağıyla, tablolar, ⚑ "Kontrol bekliyor" kutuları
- Konu testi kolaydan zora sıralı; her cevaptan sonra doğru cevap, seçilen şıkkın neden yanlış olduğu, bütün şıkların açıklaması ve kaynak
- Deneme (ÖSYM biçimi): süre sayacı, soru haritası, işaretleme, cevap değiştirme/silme, süre dolunca otomatik bitiş, sayfa kapansa da kaldığı yerden devam. Sorular haritadaki ders ağırlıklarıyla seçilir; hazır ders azsa deneme kısalır, süre orantılı (1,5 dk/soru)
- Sonuç: doğru/yanlış/boş, ham puan veya net (yanlisGoturur), ders ders başarı çubukları, soruları açıklamalı inceleme, son 20 deneme geçmişi
- Yanlış defteri + aralıklı tekrar: yanlış soru 1-3-7-15-30 gün arayla sorulur; beşinde de doğruysa defterden düşer, yanlışsa baştan başlar
- Telefonda saklananlar (`localStorage` "kadem.v1"): `p.<sınav>.<konu>` yüzde, `d.<sınav>` defter, `dn.<sınav>` deneme geçmişi, `a.<sınav>` yarım deneme. Eski `y.<sınav>` listesi otomatik taşınır

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



### 3. oturum — 24 Kasım 2026 (MBSTS başlangıcı)
- **Resmî kapsam doğrulandı.** ÖSYM DİB-MBSTS kılavuzu (2024): 60 soru, 90 dk, beş seçenekli; yanlış doğruyu götürmez, ham puan = doğru sayısı, standart puan 20-100. Dağılım: Fıkıh ve İlmihal 20 · Kur’an Bilgisi 7 · Tefsir 7 · Akaid ve Kelam 7 · Hadis 7 · Siyer ve İslam Tarihi 7 · Mezhepler Tarihi 3 · Dinler Tarihi 2. 29 Mart 2026 sınavı (kullanıcının "2026 MBTS.pdf" dosyası) bu dağılımla birebir uyuşuyor: 1-7 Kur’an, 8-14 Tefsir, 15-21 Kelam, 22-41 Fıkıh, 42-48 Hadis, 49-55 Siyer-İT, 56-58 Mezhepler, 59-60 Dinler.
- **MBSTS’de mevzuat yok.** Mevzuat; kariyer basamakları, ilçe müftülüğü, müftü yardımcılığı gibi sınavlar için ayrıca hazırlanacak.
- **MBSTS ≠ DHBT.** DHBT: KPSS’nin parçası, 40 soru/60 dk (DHBT-1 20 ortak: inanç, ibadet, Kur’an bilgisi, siyer, ahlak; DHBT-2 20, öğrenim düzeyine göre: tefsir, fıkıh, hadis, kelam, İT, dinler-mezhepler, hitabet). ÖSYM DHBT için ders başına soru sayısı yayımlamıyor. KPSS’de 4 yanlış 1 doğruyu götürür. Alanlar büyük ölçüde ortak olduğu için konular `data/kadem/konu/` altında ortak yazılıyor; DHBT’ye özgü üniteler (İslam ahlakı, din hizmetleri/hitabet) ayrıca eklenecek.
- Konu haritası (37 ünite, 8 ders) `data/kadem/mbsts.json` → `harita` içinde; uygulamada "Konu haritası" sayfası. **Kullanıcı onayı bekliyor.**
- Örnek ünite: **Hadis** (3 konu, 59 soru, 61 kart, özetler, ayet/hadis kaynakları). Konu seçimi 2017-2020 ve 2026 sınavlarındaki ~35 hadis sorusunun dökümüne göre yapıldı: eser türleri (müsned, sünen, câmi’, müstahrec, müstedrek, zevâid, etrâf) ~7; zayıf hadis türleri ~6; hadis tarihi (yazım, tedvin, rihle, Zührî/Goldziher) ~6; râvi/cerh-ta’dil ~5; râvi sayısı ~3; sahih-hasen-merfû/mevkûf/muhtelif ~3; tahammül yolları ~2; sünnetin konumu ~3.
- kadem.html yeniden yazıldı (yukarıdaki "Sayfanın yaptıkları"). Chrome ile uçtan uca denendi: konu, özet, kart, test, defter, tekrar, deneme (yenileme sonrası devam), sonuç, inceleme.
- `sw.js` sürümü artırılmadı (main ile çakışmasın diye); kadem.html önbellekten açılıp arkada yenilendiği için ikinci açılışta güncellenir. main’e birleştirirken sürüm artırılabilir.

### Hoca kontrolü bekleyenler (Hadis ünitesi)
- hadis-1: muksirûn rivayet sayıları (anlatımda ⚑ ile işaretli).
- hadis-2: maklûb örneğinin Müslim’deki yeri (⚑).
- hadis-3: Hz. Ebû Bekir’in 500 hadisi yaktığı rivayeti — anlatıma alınıp alınmayacağı (⚑, soruda kullanılmadı).
- Bütün hadis numaraları bab numarasıyla verildi (ör. Buhârî, İlim, 39). Bab/numara sistemi baskıya göre değişebileceği için kaynak satırlarının genel kontrolü iyi olur.
- Ayet mealleri kendi cümlelerimizle, Diyanet mealine yakın yazıldı.

## Kitap envanteri (kullanıcının "mbstttt" klasörü, 25 PDF)
Tür: KA = konu anlatımı, SB = soru bankası, D = deneme, ÇS = çıkmış soru, N = not/özet. Kalite: ★ zayıf · ★★ orta · ★★★ iyi.

| Dosya | Tür | Kapsam | Kalite / not |
|---|---|---|---|
| Tüm Yıllar MBSTS.pdf (ve Tum-Yillar-MBSTS_… aynısı) | ÇS | 2017, 2018, 2019, 2020 MBSTS (taranmış, 50 sf) | ★★★ En değerli kaynak: konu ağırlığı ve soru tarzı. Cevap anahtarı var |
| 2026 MBTS .pdf | ÇS | 29 Mart 2026 MBSTS, 60 soru, her sayfada cevap (taranmış) | ★★★ Güncel dağılımın kanıtı |
| mtsb.pdf | KA+SB+D | Diyanet-Sen 2017 "Konu Anlatımlı MBSTS Soru Bankası", 572 sf, 7 alan + 3 deneme | ★★★ MBSTS’ye en uygun kitap; yer yer tanım hataları var (ör. meşhur hadis "en az iki râvi" diye yanlış) |
| MBSTS TEFSİR TARİHİ ve USULÜ – Salih Köklü (22 sf) | ÇS/SB | Tefsir; çıkmış MBSTS sorularından derleme | ★★★ |
| MBSTS İSLAM TARİHİ – Salih Köklü (15 sf) | ÇS/SB | Siyer-İT | ★★★ |
| MBSTS İSLAM MEZHEPLERİ TARİHİ – Salih Köklü (7 sf) | ÇS/SB | Mezhepler | ★★★ |
| MBSTS TECVİT – Salih Köklü (4 sf) | ÇS/SB | Tecvid | ★★★ |
| MBSTS & DHBT KİTABI (GENCO) (iki kopya, metinleri aynı) | KA (kodlamalı) | Tecvid, tefsir usulü, fıkıh (ibadet, aile), hadis usulü, akaid, kelam, siyer, mezhepler, dinler; 217 sf | ★★ Kodlamalı özet; kaynak gösterilmemiş |
| mbsts özet bilgiler şabettin Akyol.pdf | N (el yazısı, taranmış) | Tefsir, akaid… özet şemalar | ★★ OCR zor; yalnız kontrol amaçlı |
| mbsts- dhbt özel notlar.pdf | N (soru-cevap) | Siyer ağırlıklı karışık bilgiler, 36 sf | ★★ |
| DHBT DKAB MBSTS notlar.pdf (Çoban) | N (madde madde) | Akaid, kelam, karışık | ★ Hatalı maddeler var (ör. "Reca" ↔ ric’at); doğrulamadan kullanılmamalı |
| DHBT 1-2 KONU ANLATIMLI ÇÖZÜMLÜ SORU BANKASI (İhtiyaç, 2014) | KA+SB | DHBT bütün alanlar, 680 sf | ★★ Eski (dört seçenekli dönemden kalma kısımlar var) |
| DHBT 1-2 TÜM KONULAR SORU BANKASI(1) / DHbt-Soru-Bankasi (aynı dosya) | N (soru-cevap) | DHBT bütün alanlar, 149 sf | ★ Klasik soru-cevap; ÖSYM tarzı değil |
| rauf şara dhbt 1 soru bankası 2025 (347 sf, taranmış) | SB (çözümlü) | DHBT-1: ibadet, inanç, Kur’an, siyer, ahlak | ★★★ Güncel, çözümlü, ÖSYM tarzı |
| rauf şara dhbt 2 soru 2025 (348 sf, taranmış) | SB (çözümlü) | DHBT-2: tefsir, hadis, fıkıh, kelam, İT… | ★★★ |
| Rauf şara soru bankası .pdf (392 sf, taranmış) | SB (çözümlü) | Kur’an ilimleri ağırlıklı | ★★ |
| muhkem dhbt 2 önlisans-lisans soru bankası 2020 (ZOR DENEMELER… dosyası bunun aynısı) | SB | DHBT-2 lisans/önlisans | ★★ |
| muhkem dhbt 2 ortaöğretim soru bankası 2020 | SB | DHBT-2 ortaöğretim | ★★ |
| DHBT ÇÖZÜMLÜ 5 DENEME (Yönerge, taranmış) | D | DHBT-1/2, 5 deneme | ★★ |
| Mûtenâ Akademi DHBT 2. Deneme / Özel DHBT Deneme (Harun Sancı) | D | DHBT 1-2 | ★★ |

Kullanım ilkesi: kitaplardan yalnızca bilgi alınır; metin ve sorular kendi cümlelerimizle yazılır. Çıkmış sorular konu ağırlığını ve soru tarzını belirlemek için kullanılır, aynen kopyalanmaz. Taranmış kitaplar Tesseract (tur) ile okunuyor.

## Sıradaki iş
1. Kullanıcı konu haritasını ve Hadis ünitesini onaylayacak (ve ⚑ işaretli yerleri kontrol edecek).
2. Onaydan sonra aynı kalıpla sırasıyla: Fıkıh (20 soru, 14 ünite) → Kur’an Bilgisi → Tefsir → Akaid-Kelam → Siyer-İT → Mezhepler → Dinler.
3. Her ders bitince denemeler büyür; bütün dersler hazır olunca 60 soruluk tam deneme kendiliğinden oluşur. Sonra ayrı deneme havuzu (konu testlerinde olmayan sorular) eklenebilir.
4. DHBT: `dhbt.json` açılıp ortak konular `ref` ile bağlanacak; DHBT-1’e özgü İslam ahlakı ve hitabet üniteleri yazılacak; deneme 40 soru/60 dk, yanlisGoturur: true.
5. Açık konu: bölüm bir süre ücretsiz; ödeme sistemi yok.
