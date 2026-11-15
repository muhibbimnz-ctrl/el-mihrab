# Kelime çözümleme verisi (Medrese · Kelime kartı)

Bu klasördeki `1.json … 114.json`, `roots.json` ve `babs.json` dosyaları
**Quranic Arabic Corpus Morphology v0.4** (Kais Dukes, Leeds Üniversitesi —
http://corpus.quran.com) verisinden üretilmiştir. Kullanılan nüsha, düzeltmeler içeren
`mustafa0x/quran-morphology` çatalıdır. Kaynak veri **GNU GPL** lisanslıdır; bu türetilmiş
veri de aynı lisansla dağıtılır.

Üretim: `python3 tools/morph_build.py quran-morphology.txt`

- `{sûre}.json` — `a[âyet][kelime][parça] = [metin, tür, etiketler]`; `sm` = imlâî yazımda
  ayrı yazılan يا/ها belirteçlerinin kelime eşlemesi.
- `roots.json` — kök → sözlük şekli → geçtiği yerler (`sûre:âyet:kelime`).
- `babs.json` — sülâsî mücerred fiillerin bâbı `[bâb no, kesin mi, masdar]`; korpustaki mâzî ve
  muzâri harekelerinden otomatik çıkarılmıştır.
- `onay.json` — **ehil onaylı i'râb**. Anahtar `sûre:âyet:kelime`; değer
  `{"ar": "Arapça i'râb", "tr": "Türkçe açıklama", "by": "Onaylayan"}`.
  Burada bulunan kelimelerde kart otomatik metin yerine bunu gösterir ve "Onaylı" damgası basar.

Türkçe medrese terimleri, i'râb cümleleri ve Emsile çekim tabloları `kelime.js` içinde kural
ile üretilir ve onaylanana kadar **taslak** sayılır.
