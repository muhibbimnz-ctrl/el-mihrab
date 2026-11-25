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
- Sabit tam denemeler (5. oturum): `data/kadem/deneme/<sınav>-<n>.json` → `{"id":"mbsts-1","ad":"1. Deneme","aciklama":"…","sorular":[{"id":"md1-01","ders":"Tefsir",…}]}`. Sorular konu testlerinde yoktur; her sorunun `ders` alanı haritadaki ders adıyla aynı olmalı. `kontrol.py` dosya adının önekine (`mbsts-`) bakarak sınavın `denemeler` listesini kendisi kurar ve dağılım haritadan farklıysa uyarır.
- Konu dosyasındaki `sinavlar` listesi, konunun hangi sınavlarda görüneceğini belirler; `kontrol.py` her sınav dosyasının `konular` listesini buna göre yeniden kurar (elle düzenlemeye gerek yok).
- Anlatımda yeni öğe: `{"madde":"metin","kay":"633 sayılı Kanun, md. 1"}` (mevzuat maddesi kutusu).
- `d` doğru şık (0 = A), `z` zorluk (1 kolay, 2 orta, 3 zor), `ac` her şıkkın neden doğru/yanlış olduğu, `id` kalıcı soru anahtarı (yanlış defteri buna bağlı; değiştirme).
- Konunun `ders` adı haritadaki ders adıyla birebir aynı olmalı (deneme, soruları ders ağırlığına göre bu adla seçer). Kesme işareti olarak ’ kullanılıyor: “Kur’an Bilgisi”.
- Dosyası olmayan sınav "Hazırlanıyor" olarak görünür.

### Sayfanın yaptıkları
- Görünüm (5. oturumda yenilendi): kâğıt rengi zemin, serif başlıklar, ince çizgiler, künye tablosu, optik form gibi yuvarlak şıklar; her sınavın kendi rengi yalnız vurgu rengi olarak kullanılıyor. Karanlık tema var.
- Sınav sayfası: künye (kimler girer, biçim, puanlama, hazır içerik, ilerleme), Denemeler, bugünkü tekrar, yanlış defteri, çalışma programı, konu haritası, derslere göre konular
- Denemeler sayfası: sabit tam denemeler (son sonuçla), her seferinde yeni karma deneme (konu havuzundan resmî ağırlıkla), ders denemeleri (tek dersten 20 soru, süreli), deneme geçmişi. Aynı anda tek yarım deneme tutulur; yenisine başlarken sorulur.
- Çalışma programı (`pl.<sınav>`): 4/6/8/12 hafta seçilir; konular dersler iç içe geçecek şekilde günlere dağılır, haftada 5 konu günü + 1 deneme günü (sırayla sabit denemeler, sonra karma) + 1 dinlenme; sık çıkan (★★★) konular sonda tekrar edilir; bugünkü gün işaretlenir, testi çözülen konu üstü çizili görünür.
- Konu: sekmeler Anlatım · Özet · Kartlar · Test. Ayet/hadis kutuları kaynağıyla, tablolar, ⚑ "Kontrol bekliyor" kutuları
- Konu testi kolaydan zora sıralı; her cevaptan sonra doğru cevap, seçilen şıkkın neden yanlış olduğu, bütün şıkların açıklaması ve kaynak
- Deneme (ÖSYM biçimi): süre sayacı, soru haritası, işaretleme, cevap değiştirme/silme, süre dolunca otomatik bitiş, sayfa kapansa da kaldığı yerden devam. Sorular haritadaki ders ağırlıklarıyla seçilir; hazır ders azsa deneme kısalır, süre orantılı (1,5 dk/soru)
- Sonuç: doğru/yanlış/boş, ham puan veya net (yanlisGoturur), aynı denemenin önceki sonucu, ders ders başarı çubukları, zayıf derslere öneri, soruları açıklamalı inceleme; geçmişteki her deneme `&t=sonuc&r=<zaman>` ile açılır (son 30 deneme saklanır)
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

### 4. oturum — 24 Kasım 2026 (MBSTS içeriği tamamlandı)
- Kullanıcı onay beklenmeden bütün MBSTS’nin hazırlanmasını istedi. Hadis ünitesindeki üç ⚑ kontrol notu araştırılıp kapatıldı (muksirûn sayıları not olarak kaldı; maklûb rivayeti Müslim, Zekât, 91 / no. 1031 olarak doğrulandı; Hz. Ebû Bekir’in 500 hadis rivayeti zayıf olarak işaretlendi). Şu anda içerikte açık ⚑ yok.
- MBSTS’nin 8 dersi de hazır: **23 konu, 297 soru**, her konuda anlatım (tablolar, ayet/hadis kutuları), özet, tekrar kartları ve kolaydan zora açıklamalı test.
- 60 soruluk, 90 dakikalık tam deneme artık resmî dağılımla (7-7-7-20-7-7-3-2) kendiliğinden oluşuyor; Chrome’da baştan sona denendi.
- Doğru şıkların A–E arasında dengeli dağılması için `dengele.py` mantığı kullanıldı (sıralı şıklı sorulara dokunulmaz).

### 5. oturum — 24-25 Kasım 2026 (görünüm, denemeler, DHBT, mevzuat)
- **Görünüm yenilendi** (kullanıcı “şablon hoş durmadı, yapay zekâ yapmış gibi durmasın” dedi): renkli yuvarlak kartlar yerine kâğıt zemin, serif başlıklar, ince çizgili tablolar, optik form şıkları; üst çubuk sade.
- **Deneme sistemi genişletildi:** sabit tam denemeler, karma deneme, ders denemeleri, deneme geçmişi, sonuç karşılaştırma; çalışma programı sayfası eklendi.
- **MBSTS derinleştirildi:** Fıkıh 125 → 202, Mezhepler 8 → 22 (mezhep-2), Dinler 8 → 22 (dinler-2), diğer derslere 3-5’er soru; **5 tam deneme (300 soru)** yazıldı.
- **DHBT:** `dhbt.json` açıldı (40 soru, 60 dk, 4 yanlış 1 doğru). ÖSYM ders başına sayı vermediği için ağırlıklar kullanıcının klasöründeki yayınevi denemelerinden (Yönerge 5 Deneme – OCR, Mûtenâ Akademi 1. ve 2. deneme) soru sırası sayılarak çıkarıldı: DHBT-1 ≈ inanç 3, ibadet 5, Kur’an-tecvid 6, siyer 4, ahlak 2; DHBT-2 ≈ tefsir 3, fıkıh-usul 4, hadis 3, kelam 3, İslam tarihi 2, mezhepler 1, dinler 2, din hizmetleri-hitabet 1-2. Harita lisans düzeyine göredir. Yeni konular: ahlak-1 (İslam Ahlakı), hitabet-1 (Din Hizmetleri ve Hitabet).
- **Mevzuat ünitesi:** mevzuat-1 (633 sayılı Kanun; 04.06.2025 konsolide metne göre: Başkan 5 yıl/2 dönem, en fazla 5 başkan yardımcısı, DİYK 16 üye/5 yıl, Mushaf Kurulu başkan+12, yurt dışı 3+1 yıl, 40 müşavir/40 Başkanlık müftüsü, md. 10/A, 25, 34, 35), mevzuat-2 (657 DMK: ilkeler, ödevler, haklar, yasaklar, adaylık, izinler, disiplin, görevden uzaklaştırma), mevzuat-3 (Kariyer Basamakları Yönetmeliği: basamaklar, 6/4/8 yıl şartları, sözlü puanlar 30-30-30-10 ve 70-20-10, başarı 70, itiraz 7/15 gün, duyuru 15/30 gün; yurt dışı seçimde son 3 yılın en yüksek MBSTS’si).
- Doğrulama: Chrome (headless) ile sabit deneme başlat-cevapla-bitir-incele, karma DHBT denemesi, çalışma programı, konu testi, karanlık tema denendi; konsol hatası yok.

### Hoca kontrolü bekleyenler (5. oturum)
- mevzuat-1: DİYK üyelerinin seçim usulü (12 üyenin Aday Tespit Kurulunun belirlediği adaylar arasından seçilmesi) — 633/5 ve 20’nin güncel metniyle bir kez daha karşılaştırılmalı.
- mevzuat-2: 657 md. 102 (iznin devri), md. 104 (mazeret izni ayrıntıları) — güncel metinle kontrol.
- mevzuat-3: yurt dışı mülakat puan kalemleri (yalnız ikisi doğrulandı: mevzuat 15, hizmet alanı bilgisi 15).
- Deneme 3, soru md3-35 (Hukûk-ı Âile Kararnâmesi – gaip kocanın durumu) ve md4-40 (Hanefî’de fetva sıralaması) — ifade ayrıntıları.

### 6. oturum — 25 Kasım 2026 (yayın, şifre, sade ana sayfa, 6-10. denemeler)
- **Yayın:** kadem dalı main’e alındı (sw v170). Bundan sonra her iş hem `kadem` hem `main`’e gönderiliyor.
- **ŞİFRE (önemli):** Kadem içeriği şifreli. `data/kadem/**/*.json` artık git’e girmez (.gitignore); yayına yalnız `*.enc` dosyaları gider. Şifre depoda YOK; kullanıcıda. Çalışmaya başlarken:
  `KADEM_SIFRE='…' python3 tools/kadem/sifre.py ac` → düz .json dosyaları oluşur; iş bitince sırayla dengele → kontrol → harita → `KADEM_SIFRE='…' python3 tools/kadem/sifre.py kapat` → commit.
  Biçim: AES-256-GCM, anahtar PBKDF2-SHA256 (250.000 tur, tuz `data/kadem/anahtar.json`). Tarayıcı şifreyi bir kez sorar, türetilen anahtarı cihazda `kadem.anahtar` olarak saklar. Şifre değişirse `anahtar.json` silinip yeni şifreyle `kapat` çalıştırılır; eski cihazlar otomatik olarak giriş ekranına döner.
  Not: Şifreden önceki commit’lerde içerik düz metin olarak git geçmişinde duruyor (depo herkese açık).
- **Sınav ana sayfası sadeleşti:** konu listesi yerine “Bugünün işi” kartı (programdan ya da sıradaki çalışılmamış konu), 4 karo (Denemeler, Tekrar, Yanlış defteri, Program), ders kartları (sınavdaki soru sayısı, konu/soru sayısı, ilerleme), zayıf konular (yanlış defterinden), çalışma araçları. Konular ders sayfasında (`&ds=<ders>`): ders denemesi, dersin özeti, dersin kartları. Yeni: **Son tekrar kitapçığı** (`&t=ozet[&ds=]`, bütün özetler, yazdırılabilir), **Karışık kartlar** (`&t=kartlar[&ds=]`). Sınav bilgisi katlanır kutuda.
- **MBSTS 6-10. denemeler (300 soru):** son yılların ÖSYM tarzında (uzun paragraf kökü, olay senaryosu, I-II-III öncüllü, eşleştirme, “bu parçada sözü edilen…”). Kullanıcının klasöründeki “2026 MBTS.pdf” (60 soruluk görüntü PDF) OCR ile yalnız tarz ve konu dağılımı için incelendi; ilk taslakta birebir benzeyen sorular çıkınca tamamı farklı örnek ve öncüllerle yeniden yazıldı. Kural aynı: çıkmış soru alınmaz, tarz alınır.
- Toplam: 32 konu, 521 konu sorusu + 600 deneme sorusu = **1121 soru**; MBSTS’de 10 tam deneme.

### 7. oturum — 25 Kasım 2026 (MBSTS’yi konu listesine göre yeniden kurma: Kur’an Bilgisi bitti)
- **Kullanıcının yeni hedefi:** MBSTS’den en az 80 alınabilecek, başka kaynak gerektirmeyen içerik. Her ders, kullanıcının verdiği konu listesine göre (aşağıda “Yeniden yapılanma planı”) **her konu ayrı dosya**, ders kitabı derinliğinde. Şimdilik yalnız MBSTS; DHBT bekliyor. Sıra: Kur’an Bilgisi → Tefsir → Kelam → Siyer-İT → Hadis → Mezhepler → Dinler → Fıkıh.
- **Her konu dosyasında olması gerekenler:** her alt başlık bir merak sorusu (`{"merak":…}`) ya da olayla açılır; bilgi sebep-sonuç içinde anlatılır, listeler tabloyla özetlenir; karıştırılan kavramlar karşılaştırma tablosuyla verilir; ayet/hadis kaynaklı; `{"sinav":…}` (“Sınavda nasıl sorulur?”, ÖSYM tuzakları) ve `{"akil":…}` (“Aklında kalsın”) kutuları; özet 10-20 madde; en az 12 kart; en az 12 soru (paragraf, senaryo, I-II-III, eşleştirme; her şıkka ayrı açıklama, şık açıklamalarında harf geçmez çünkü dengele şıkları karıştırır). Emin olunmayan bilgi `{"kontrol":…}`. Fıkıh Hanefî. Çıkmış soru birebir alınmaz.
- **Kur’an Bilgisi tamamlandı: 13 konu (kuran-1 … kuran-13), 196 soru, 196 kart.** Eski kuran-1 (vahiy-tarih-yapı) ve kuran-2 (tecvid) bölündü; eski 32 sorunun id’leri korunarak yeni konulara taşındı (k1-xx → kuran-1,3,4,5,6,7,8; k2-xx → kuran-11,12,13). 2026 sınavına neredeyse birebir benzeyen 6 soru (k1-04, k1-05, k1-06, k1-08, k2-04, k2-05) aynı id ile farklı örneklerle yeniden yazıldı. Yeni soru id’leri `kb<konu>-<n>`.
- Kaynak: mtsb.pdf Kur’an Bilgisi bölümü (sf. 9-50; metin katmanında “a/d” harfleri düşüyor ama okunuyor), GENCO, Köklü Tecvit (2018-2024 çıkmış tecvid soruları), 2026 MBTS ve Tüm Yıllar MBSTS (OCR). mtsb Kur’an bölümünde “Kur’an’ı anlama ve meal bilgisi” de var → kuran-5 (sure kimlikleri) ve kuran-6 (kısa surelerde kelime anlamları, sure içerikleri) içine alındı.
- **Görünüm:** Kadem ana sayfası sadeleşti: üstte iki büyük kart (MBSTS, DHBT; ilerleme çubuğu, “Kaldığın yer” – son açılan konu `son.<sınav>` ile hatırlanır), diğer 17 sınav katlanır “Diğer sınavlar” listesinde (yalnız ad + biçim; açılışta yüklenmez, ana sayfa hızlandı). Sınav sayfasında karolar ve kart ızgarası kaldırıldı: Bugünün işi → numaralı ders listesi (ilerleme çizgili) → tek satır araç bağlantıları (Denemeler, Tekrar, Yanlış defteri, Program, Özet kitapçığı, Kartlar, Konu haritası). Konu anlatımına yeni bloklar: `merak`, `sinav`, `akil`.
- **Windows’ta çalışma (bu oturumda bilgisayarda yapıldı):** Python 3.12 (`%LOCALAPPDATA%\Programs\Python\Python312\python.exe`, `pip install cryptography pymupdf`), Tesseract 5.4 (`C:\Program Files\Tesseract-OCR`, Türkçe model `%USERPROFILE%\tessdata\tur.traineddata` → `--tessdata-dir`). Araçları **`PYTHONUTF8=1`** ile çalıştır (yoksa Türkçe JSON cp1254 ile okunur). Araçlar artık JSON’u LF ile yazıyor ve `sifre.py` iv’yi `/` ayraçlı yolla hesaplıyor; böylece değişmeyen dosyaların .enc’i Windows’ta da değişmez.
- Tarayıcı denemesi (uygulama içi tarayıcı; Chrome eklentisi bağlı değildi): giriş, ana sayfa, MBSTS sayfası, Kur’an Bilgisi ders sayfası (13 konu), kuran-8 anlatımı (merak/sınav/aklında kalsın kutuları, tablolar), kuran-11 testi (yanlış cevap açıklaması, şık açıklamaları) — sorun yok.

### Yeniden yapılanma planı (mevcut dosya → yeni konular)
Kullanıcının konu listesindeki her satır ayrı dosya olacak. Bir ders yazılırken eski dosyaların soruları id’leri korunarak ilgili yeni konuya taşınır, eski dosya yeni numarayla üzerine yazılır.
| Ders | Hedef | Eski dosyalar → yeni konular |
|---|---|---|
| Kur’an Bilgisi | 13 | ✅ bitti |
| Tefsir | 9 | tefsir-1 (ulûm, usul) → tefsir-1…4; tefsir-2 (tarih, ekoller) → tefsir-5…8; tefsir-9 (seçme sure ve ayetler) yeni |
| Akaid ve Kelam | 12 | kelam-1 → kelam-1…10; kelam-2 (ekoller) → kelam-11; kelam-12 (felsefe, yeni ilm-i kelam, deizm-ateizm) yeni |
| Siyer ve İslam Tarihi | 16 | siyer-1 → siyer-1…7; siyer-2 → siyer-8…16 (Endülüs-Mısır, Türk-İslam, Haçlı-Moğol, Osmanlı kurumları, medeniyet büyük ölçüde yeni) |
| Hadis | 10 | hadis-1 → hadis-1, 2, 6; hadis-2 → hadis-3, 4, 5; hadis-3 → hadis-7, 8, 9; hadis-10 (yorum ilkeleri, seçme hadisler) yeni |
| Mezhepler Tarihi | 10 | mezhep-2 → mezhep-1, 2, 4, 6, 8; mezhep-1 → mezhep-3, 10; mezhep-5 (Mu’tezile), 7 (fıkhî mezhepler), 9 (Alevîlik-Bektaşîlik) yeni |
| Dinler Tarihi | 10 | dinler-2 → dinler-1, 2, 6, 10; dinler-1 → dinler-3, 4, 5, 7, 8, 9 |
| Fıkıh ve İlmihal | 22 | fikih-1 → 1; fikih-2 → 2, 3, 4; fikih-3 → 6, 7; fikih-4 → 8, 9, 10; fikih-5 → 11; fikih-6 → 12; fikih-7 → 13, 14; fikih-8 → 14, 15; fikih-9 → 16, 17, 18; fikih-10 → 19, 20, 21, 22; fikih-5 (kaideler-makāsıd) yeni. **Dikkat:** fikih-N numaraları anlam değiştiriyor; Fıkıh tek seferde yazılmalı (önce bütün eski soruları bir yere dök). |

### 8. oturum — 25-26 Kasım 2026 (bütün dersler paralel yazılıyor; ara kayıt)
- Kullanıcı “teker teker değil, bütün dersleri aynı anda yaz; sorular zor olsun; hızlı ol” dedi. 11 alt ajan paralel çalıştırıldı (Tefsir, Kelam 1-6, Kelam 7-12, Siyer 1-7, Siyer 8-16, Hadis, Mezhepler, Dinler, Fıkıh 1-11, Fıkıh 12-22, Kur’an Bilgisi zorlaştırma). Ortak talimat ve denetim betiği: oturum scratchpad’indeki `BRIEF.md` ve `kontrol_konu.js` (yeni ölçüt: anlatım ≥15.000 karakter, her ara başlık merak ile açılır ve akil ile biter, ≥3 sinav kutusu, ≥3 tablo, ≥14 soru, en fazla 2 kolay, en az %40 zor, ≥2 I-II-III sorusu, şık açıklamasında harf yok, id tekrarı yok).
- Ajanlar 5 saatlik kullanım sınırına iki kez takıldı. Kullanıcı ara commit istedi; bu commit **yarım durumdadır**.
- **Yazılmış yeni konular (69):** kuran-1…13 (1-11 zorlaştırıldı; 12, 13 zorlaştırma yarım), tefsir-1…4, kelam-1…4, 7…11, siyer-1…4, 8…13, hadis-1…6 (hadis-6 yarım: 7 soru), mezhep-1…6, dinler-1…7, fikih-1…4, 12…15.
- **Henüz yazılmayanlar:** tefsir-5…9; kelam-5, 6, 12; siyer-5, 6, 7, 14, 15, 16; hadis-7…10 (+hadis-6 tamamlanacak); mezhep-7…10; dinler-8…10; fikih-5…11, 16…22.
- **Köprü dosyaları (geçici):** Yazılmamış konuların eski içeriği kaybolmasın diye eski dosyalar `eski-<eski id>.json` olarak geri kondu (ör. eski-fikih-5 = eski oruç konusu); içlerinde yalnız henüz yeni dosyalara taşınmamış sorular var (id tekrarı yok). Ad: “… (önceki anlatım; yeni konular hazırlanıyor)”. **Bir dersin bütün yeni konuları yazılınca o dersin eski-* dosyalarındaki kalan sorular yeni konulara taşınmalı ve eski-* dosyaları SİLİNMELİ** (köprüdeki her soru id’si bir yeni dosyada olmalı). Eski dosyaların tam yedeği ajanların kullandığı scratchpad’de (`eski_konu/`); scratchpad silinirse eski içerik git geçmişindeki .enc dosyalarından `sifre.py ac` ile geri alınabilir (commit 83daa29).
- **Sonraki iş:** (1) kalan konuları yaz (yukarıdaki liste; aynı talimat), köprüleri kaldır; (2) kullanıcının isteği: MBSTS’ye **10 yeni tam deneme (mbsts-11…20)**, zor ağırlıklı, ÖSYM tarzı; talimat `DENEME-BRIEF.md`, denetim `kontrol_deneme.js` (60 soru resmî sıra 7-7-7-20-7-7-3-2, id md<N>-01…60, en fazla 6 kolay, en az 24 zor, ≥8 I-II-III, ≥25 uzun kök, doğru şıklar dengeli, her şık açıklaması ≥25 karakter); (3) sonra DHBT (İslam Ahlakı, Din Hizmetleri-Hitabet genişletme, DHBT denemeleri). Öncelik MBSTS.
- Müfredat kontrolü: ÖSYM MBSTS kılavuzunda bu 8 ders dışında ders yok; 2026 sınavı aynı dağılımla yapıldı.


### 9. oturum — 25 Kasım 2026 (claude.ai sohbetinden; MBSTS konuları bitti)
- Kullanıcı Claude Code yerine sohbetten çalışmayı istedi (sınır tasarrufu): alt ajan yok, ders ders yazıp her dersten sonra commit.
- **MBSTS’nin 102 konusunun hepsi yazıldı**: tefsir-5…9, kelam-5, 6, 12, siyer-5, 6, 7, 14, 15, 16, hadis-7…10 (hadis-6 tamamlandı), mezhep-7…10, dinler-8…10, fikih-5…11, 16…22; kuran-13 zorlaştırma bitti. **Bütün eski-* köprü dosyaları silindi**; eski soruların hepsi id’leri korunarak yeni konulara taşındı (`tools/kadem/tasi.py`).
- Yeni konuların anlatımı 6.500–12.000 karakter (önceki 15.000 hedefinden kısa); her konuda ≥14 soru, ≥%40 zor, ≥2 I-II-III, ≥12 kart, ≥10 özet. Yeni soru id’leri: tefsir tf5-…, kelam kl5-/kl6-/kl12-, siyer sy5-…, hadis hd7-…, mezhep mz7-…, dinler dn8-…, fıkıh fq5-… .
- Yeni araçlar: `tools/kadem/kontrol_konu.py` (konu ölçütleri; Mezhepler/Dinler için anlatım alt sınırı 7000, diğerleri 6500), `tools/kadem/tasi.py` (köprü sorularını taşır, boşalan köprüyü siler).
- Görünüm: sınav sayfasında her ders açılır kutu (details); konular doğrudan dersin altında listelenir, son çalışılan ders açık gelir. Araç düğmeleri ve ders sayfası düğmeleri eşit ızgara.
- Denetim: yerelde `python3 -m http.server` + Playwright/Chrome ile telefon boyutunda ekran görüntüsü alındı.
- DHBT’ye özgü ahlak-1, hitabet-1 ve mevzuat-1…3 eski biçimde (yeni ölçütleri karşılamıyor).


### 10. oturum — 25 Kasım 2026 (gece)
- MBSTS zor denemeleri 11–20 yazıldı (her biri 60 soru, ≥24 zor). Araç: `tools/kadem/deneme_yaz.py kaynak.txt N "açıklama" [sınav]` — ders dağılımını sınavın haritasından okur; DHBT için `dhbt` (40 soru).
- DHBT 1. deneme yazıldı (`data/kadem/deneme/dhbt-1`). Sıradaki: DHBT 2–5, mevzuat denemeleri (30 soru).
- ahlak-1, hitabet-1, mevzuat-1…3 yeni ölçütlere taşındı (`tools/kadem/konu_ek.py` ile kutu/özet/kart/soru eklenir). Artık bütün konular `kontrol_konu.py`’den geçiyor.
- Arayüz “adım adım yol” olarak yenilendi: her konu 4 adım (Oku → Özet → Kartlar → Test). Anlatım başlıklara göre bölüm bölüm gösterilir (`&g=oku&b=N`, `b=hepsi` tek sayfa). Adım ilerlemesi `ad.<sınav>.<konu>` anahtarında, son okunan bölüm `bl.<sınav>.<konu>`’da. Sınav sayfası: genel ilerleme çubuğu, “Sıradaki adım” kartı, yol haritası (4 nokta), 3 ana araç + “Diğer araçlar”. Test bitince “Sıradaki konu” düğmesi.

### KALDIĞIM YER (7. oturum sonu — artık geçerli değil, 8. oturuma bak)
- **Sıradaki ders: TEFSİR** (tefsir-1 … tefsir-9). Önce mtsb.pdf Tefsir bölümü (sf. 51-116), Köklü “Tefsir Tarihi ve Usulü” (çıkmış sorular) ve GENCO tefsir kısmı okunacak. Eski tefsir-1 ve tefsir-2 sorularının id’leri korunacak; çıkmış soruya çok benzeyenler aynı id ile yeniden yazılacak.
- Kur’an Bilgisi’nde açık ⚑ kontrol kutuları: kuran-1 (fetret süresi), kuran-2 (Mekkî-Medenî sayıları; leylî-firâşî örnekleri), kuran-3 (Kureyş okuryazar sayısı), kuran-4 (Osman nüshaları sayısı/kâriler, Topkapı-Taşkent mushafları, basma mushaf tarihleri), kuran-5 (diğer ayet sayımları; mufassal sınırları; Türkiye’de hizb), kuran-9 (TİEM 73 tarihi; Diyanet meal heyetleri; Batı tercümelerinin yılları), kuran-11 (gunne süresi), kuran-12 (uzatma miktarları).

## İçerik durumu (25 Kasım 2026, 5. oturum sonu)
Toplam: **32 konu, 521 konu sorusu + 300 deneme sorusu = 821 açıklamalı soru.**

| Ders (MBSTS / DHBT soru) | Konu dosyaları | Soru |
|---|---|---|
| Kur’an Bilgisi (7 / 6) | kuran-1 … kuran-13 (7. oturumda yeniden kuruldu) | 196 |
| Tefsir (7 / 3) | tefsir-1, tefsir-2 | 33 |
| Akaid ve Kelam (7 / 6) | kelam-1, kelam-2 | 33 |
| Fıkıh ve İlmihal (20 / 9) | fikih-1 … fikih-10 (her birinde “Sık sorulan ek bilgiler” tablosu) | 202 |
| Hadis (7 / 3) | hadis-1, hadis-2, hadis-3 | 59 |
| Siyer ve İslam Tarihi (7 / 6) | siyer-1, siyer-2 | 34 |
| Mezhepler Tarihi (3 / 1) | mezhep-1 (Şîa, gulât, modern), mezhep-2 (milel-nihal, Hâricîler, Mürcie, Cebriyye-Kaderiyye, Ehl-i sünnet, tarikatlar) | 22 |
| Dinler Tarihi (2 / 2) | dinler-1 (büyük dinler), dinler-2 (din bilimleri, teoriler, eski Türk, Çin-Japon, Yahudi-Hristiyan ibadeti, yeni hareketler) | 22 |
| İslam Ahlakı (– / 2) | ahlak-1 | 20 |
| Din Hizmetleri ve Hitabet (– / 2) | hitabet-1 | 18 |
| Mevzuat | mevzuat-1 (633), mevzuat-2 (657), mevzuat-3 (Diyanet yönetmelikleri) | 46 |

**Denemeler:** MBSTS’de 5 sabit tam deneme (`data/kadem/deneme/mbsts-1…5.json`, her biri 60 soru, 7-7-7-20-7-7-3-2) + sınırsız karma deneme + her ders için ders denemesi. DHBT ve Mevzuat’ta karma ve ders denemeleri var; sabit deneme henüz yok.

**Sınavlara bağlanan konular:** mbsts 25 konu · dhbt 27 · kbys, ilcemuftu, muftuyrd, egitimgorevlisi 28 (bütün dinî konular + mevzuat) · ihtisas, vaizlik 25 · aday 11, kurumici 14 (temel ilmihal, siyer, tecvid, ahlak, hitabet) · gys, murakip, yurtdisi 4 (mevzuat + hitabet) · mevzuat 3. Bu sınavların denemesi yok (sözlü ya da biçimi belirsiz); yalnız konu çalışması ve testler.

Fıkıh hükümleri Hanefî mezhebine göredir; mezhep farkları ayrıca belirtilmiştir.

## Araçlar (`tools/kadem/`)
- `kontrol.py`: bütün konu ve deneme dosyalarını doğrular; her sınav dosyasının `konular` (konu dosyasındaki `sinavlar` alanına göre) ve `denemeler` (dosya adı önekine göre) listesini yeniden kurar · `dengele.py [dosya…]`: doğru şıkları A–E arasında dengeler (deneme dosyaları için yolu açıkça ver: `dengele.py data/kadem/deneme/*.json`) · `harita.py`: haritası olan her sınavda ünite listelerini hazır konulardan günceller (sırayla çalıştır: dengele → kontrol → harita).
Yeni içerik eklenince yapılacak kontroller: her sorunun 5 şıkkı ve 5 şık açıklaması (`ac`) olmalı, `d` 0-4, `z` 1-3, `id` benzersiz; doğru şıklar A–E arasında dengeli; yeni konu `mbsts.json` → `konular` listesine `{"ref":"…"}` olarak ve haritadaki ilgili derse `"konu":"…"` ile eklenmeli; konunun `ders` adı haritadaki adla birebir aynı olmalı.

## Sıradaki iş
0. Şifreli düzenle ilgili yukarıdaki iş akışına uy (önce `sifre.py ac`).
1. **DHBT sabit denemeleri:** `data/kadem/deneme/dhbt-1…5.json` (40 soru; DHBT-1 20 + DHBT-2 20, haritadaki dağılım). DHBT-1’e özgü kolay-orta ilmihal soruları ağırlıkta olmalı. Ön lisans ve ortaöğretim için ayrı harita düşünülebilir.
2. **Mevzuat:** sabit deneme (30 soru); “Hoca kontrolü bekleyenler” maddelerinin güncel metinle kontrolü; Atama ve Yer Değiştirme Yönetmeliği (hizmet bölgeleri, ortak nitelik), Görevde Yükselme Yönetmeliği, Din Hizmetleri Yönetmeliği/Cami Hizmetleri ve Kur’an Kursları yönetmelikleri için mevzuat-4.
3. **Kariyer / müftülük sınavları:** konular bağlandı; Arapça (sözlüde 30 puan) için ayrı ünite ve sözlü sınav hazırlık kartları (Kur’an kıraat-anlam-tefsir sorusu örnekleri).
4. **MBSTS:** Hadis dışındaki derslerde konu sorusu 32-34; her derse bir tur daha (hedef 50). Anlatımları ders kitabı düzeyine çıkarmak (özellikle Tefsir, Kelam, Siyer).
5. Yayın: kadem dalındaki iş main’e birleştirilince `sw.js` sürümü artırılmalı (kadem.html kabukta). Deneme klasörü `data/kadem/` altında olduğu için önbellek kuralı değişmeden çalışır.
6. Açık konu: bölüm bir süre ücretsiz; ödeme sistemi yok.
