# "Tarih · Dinler · Mezhepler" kutusu — alan modülü şeması

Her alan tek dosyadır: `tools/ihtisas/t_<id>.py`. yap.py bu dosyadan `ALAN` sözlüğünü olduğu gibi alır.
İçerik Türkçe, doğru ve tarafsız olmalı; vefat tarihleri `'H/M'` ('310/923'), modern kişilerde miladi.
Nispeti tartışmalı eser varsa notta belirt. Tez/makale/DergiPark'a atıf YOK. Kaynak cümlesi kopyalama; kendi cümlenle yaz.

```python
from z_ortak import P, T, B, K, M   # P(ad,ar,v,donem,alan,bio,eserler=(),notu='',ekol='')  T(ar,tr,d)  B(c,tr,ar,mu,v,d)  K(ad,ar,mu,v,tur,neden,zincir=(),app=None)  M(b,ne,ar,ref)
ALAN = dict(
 id='<id>', ad='Alan adı', ar='Arapça ad', renk='#xxxxxx', kisa='1 cümle',
 giris=['3 paragraf: ilmin tanımı, konusu, önemi, bu bölümün yolu'],
 basamaklar=[dict(ad='Basamak', alt='Başlangıç|Orta|İleri|…', ac='1 cümle', kitaplar=[K(...), ...]), ...],  # 5-6 basamak, toplam 28+ kitap (klasik + modern Türkçe temel eserler)
 nasil=['8-10 çalışma tavsiyesi'],
 sahsiyetDonem={'anahtar': 'Dönem başlığı', ...},
 sahsiyetler=[P(...), ...],          # 45+ kişi; bio 3-5 cümle; eserler listesi; notu = nispet/yanlış bilinenler
 terimler=[dict(g='Grup', items=[T(...), ...]), ...],   # 60+ terim, 6-8 grup
 tarih=dict(donemler=[dict(ad='', aralik='', d='2-3 cümle')], olaylar=[dict(t='', kim='', ne='', neden='')]),  # 6-8 dönem, 30+ olay, kronolojik
 metinler=[M(...), ...],             # 8+ gerçek kısa klasik metin parçası (Arapça, emin olmadığını yazma)
 kutuphane=[B(...), ...],            # 50+ eser; c = kategori adı (ör. 'Klasik kaynak', 'Modern Türkçe', 'Ansiklopedi/Başvuru')
 tasnif=dict(
   tesekkul=[dict(ad, aralik, d, eserler=[...])],                 # ilmin teşekkül evreleri 7-9
   tasnif=[dict(g, d, items=[dict(ad, ar, d, ornek=[...])])],   # eser türleri / sınıflandırmalar, 25+ öğe
   ekoller=[dict(ad, ar, aralik, d, temsilci=[...])],             # 8+
   tabakat=dict(b, d, items=[dict(ad, d, ornek='')]),             # ilmin sıralama/sınıflama ölçütü
   agac=dict(b, kok=dict(name, children=[...]))),                 # bir eser silsilesi ağacı
 program=[dict(ad='Hazırlık|Başlangıç|Orta|İleri|İhtisas', sure='6 ay', hedef='', onsart=[...], oku=[dict(k='kitap', n='nasıl')], ezber=[...], uygulama=[...], olcut=[...])],  # 5 seviye
 alistirma=[dict(b='başlık', s='soru', k='kaynaklar', i='ipucu', c='cevap 3-5 cümle')],   # 6+
)
```
Bitince: `cd tools/ihtisas && python3 -c "import t_<id>"` hatasız olmalı.

## Yenileme katmanı (Tefsir, Fıkıh, Hadis, Akaid)
Dört ana alan eski hattan (tefsir.py + z_*.py + z_tas_*.py) üretildikten sonra `i_<alan>.py` modülü `i_ortak.uygula()` ile üzerine uygulanır (yap.py içinde otomatik).
Tanımlanabilen adlar: `DONEM, DONEM_ATA, EKOL_ATA, EK, KISILER, TASNIF(tesekkul/tasnif/ekoller/tabakat=[...]/agac=[...]), TERIM, DONEMLER, OLAY, METIN, KUT` ve aynı anahtarlarla `USUL` (+ `AD, KISA, KONU`).
`tabakat` ve `agac` artık liste olabilir; ihtisas.html birden çok sıralama ve eser ağacını gösterir. Usûl sekmesi tasnif, metinler, kütüphane ve dönemli şahsiyetleri destekler.
Belâgat bu katmana dahil değildir (dokunulmaz). Duman testi: `python3 tools/ihtisas/test_ui.py` (sunucusuz).
