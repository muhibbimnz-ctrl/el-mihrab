# İhtisas — Belâgat (Nahiv-Sarf temeliyle). Kitap merkezli okuma yolu.
# Kitap: (ad, arapça ad, müellif, vefat "hicrî/milâdî", tür, ne için okunur, [şerh/hâşiye zinciri], uygulama bağlantısı (adres, etiket) ya da None)
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
MED = lambda k, e: ('medrese.html#/kitap/' + k, 'Medrese’de oku: ' + e)
ALAN = dict(
 id='belagat', ad='Belâgat, Nahiv ve Sarf', ar='عِلْمُ الْبَلَاغَة', renk='#8a3b12',
 kisa='Sözü yerinde, gereği kadar ve etkili söyleme ilmi: meânî, beyân, bedî‘.',
 giris=[
  'Belâgat, Arapçanın üç “âlet ilmi”nin taçıdır: Sarf kelimenin yapısını, nahiv cümlenin dizilişini öğretir; belâgat ise o cümlenin neden öyle kurulduğunu ve muhataba nasıl tesir ettiğini sorar. Bu yüzden Kur’an’ın i‘câzını anlamanın da anahtarıdır.',
  'Klasik belâgat üç ilme ayrılır: Meânî (sözün duruma uygunluğu: takdim-tehir, hasr, fasl-vasl, îcâz-ıtnâb), Beyân (bir anlamı farklı açıklık dereceleriyle anlatma: teşbih, mecaz, istiâre, kinâye) ve Bedî‘ (sözü güzelleştiren sanatlar: cinas, tıbâk, mukabele, tevriye).',
  'Medrese geleneğinde belâgat, nahiv ve sarftan sonra okunurdu. Sekkâkî’nin Miftâh’ı, Kazvînî’nin Telhîs’i ve Teftâzânî’nin iki şerhi (Muhtasar ve Mutavvel) bu geleneğin omurgasıdır. Aşağıdaki yol, bu sırayı bugünün öğrencisine göre basamaklandırır.'],
 basamaklar=[
  dict(ad='Temel: Sarf ve Nahiv', alt='Belâgattan önce', ac='Belâgat, sağlam bir nahiv ve sarf bilgisinin üstüne kurulur. Bu basamağın kitaplarının çoğu el-Mihrâb Medrese bölümünde metniyle birlikte var.',
   kitaplar=[
    K('Emsile ve Binâ', 'الأمثلة والبناء', 'Müellifi meçhul (medrese metinleri)', '—', 'metin', 'Fiil kalıplarını ve çekimi ezberletir; sarfın ilk adımı.', app=MED('bina', 'Binâ')),
    K('Maksûd', 'المقصود', 'Ebû Hanîfe’ye nispet edilir (kesin değil)', '—', 'metin', 'Bâblar, mastarlar ve türemiş isimler; Binâ’nın devamı.', app=MED('maksud', 'Maksûd')),
    K('İzzî', 'العزي في التصريف', 'İzzeddîn ez-Zencânî', '655/1257 civarı', 'metin', 'Sarfı ilmî bir düzenle toplar; medrese sarfının son kitabı.', ['Teftâzânî, Şerhu’l-İzzî'], MED('izzi', 'İzzî')),
    K('Avâmil', 'العوامل', 'İmam Birgivî', '981/1573', 'metin', 'Nahvin “âmil-ma‘mûl” mantığını yüz âmil üzerinden öğretir.', ['Cürcânî’nin Avâmil’i ayrı bir eserdir'], MED('birgivi', 'Avâmil')),
    K('İzhâr', 'إظهار الأسرار', 'İmam Birgivî', '981/1573', 'metin', 'Avâmil’in açılımı; i‘rabın ayrıntıları.', ['Adalı Mustafa, Şerhu’l-İzhâr'], MED('izhar', 'İzhâr')),
    K('Kâfiye', 'الكافية', 'İbnü’l-Hâcib', '646/1249', 'metin', 'Nahvi tanımlarla ve kısa kurallarla toplayan özlü metin.', ['Câmî, el-Fevâidü’z-Ziyâiyye (Molla Câmî)', 'Radî el-Esterâbâdî, Şerhu’l-Kâfiye']),
    K('Molla Câmî', 'الفوائد الضيائية', 'Abdurrahmân-ı Câmî', '898/1492', 'şerh', 'Kâfiye şerhi; medresede nahvin zirvesi, mantıklı akıl yürütmeyi öğretir.'),
    K('Katru’n-nedâ ve Şerhi', 'قطر الندى وبل الصدى', 'İbn Hişâm el-Ensârî', '761/1360', 'metin ve şerh', 'Arap dünyasında en çok okunan orta seviye nahiv kitabı; şâhitleri zengin.', app=MED('katr', 'Katru’n-nedâ')),
    K('Elfiyye ve İbn Akîl Şerhi', 'ألفية ابن مالك وشرح ابن عقيل', 'İbn Mâlik / İbn Akîl', '672/1274 · 769/1367', 'manzum metin ve şerh', 'Bin beyitlik nahiv manzumesi; ezberlenir, İbn Akîl şerhiyle okunur.'),
    K('Muğni’l-lebîb', 'مغني اللبيب عن كتب الأعاريب', 'İbn Hişâm el-Ensârî', '761/1360', 'ileri', 'Edatların ve cümle türlerinin ansiklopedisi; belâgata en yakın nahiv kitabı.')]),
  dict(ad='Giriş: Belâgata ilk adım', alt='Başlangıç', ac='Terimleri tanımak ve bol örnekle sanatları görmek için sade, modern anlatımlı kitaplar.',
   kitaplar=[
    K('el-Belâgatü’l-vâzıha', 'البلاغة الواضحة', 'Ali el-Cârim ve Mustafa Emîn', '1937 baskısı', 'modern ders kitabı', 'Her konu örnek, açıklama, kural ve alıştırma sırasıyla; kendi kendine çalışmaya en uygun giriş.'),
    K('Cevâhirü’l-belâga', 'جواهر البلاغة', 'Ahmed el-Hâşimî', '1362/1943', 'modern ders kitabı', 'Meânî, beyân ve bedî‘in bütün konularını klasik tasnife sadık, anlaşılır bir dille toplar.'),
    K('Belâgat (Arap Edebiyatında Edebî Sanatlar)', '—', 'Nusrettin Bolelli', '—', 'Türkçe ders kitabı', 'İlahiyat fakültelerinde okutulan Türkçe giriş; terimlerin Türkçe karşılıklarını oturtur.')]),
  dict(ad='Medrese metni: Telhîs ve Muhtasar', alt='Orta', ac='Klasik belâgat eğitiminin çekirdeği. Telhîs’in ibareleri ezberlenir, Muhtasar ile şerh edilerek okunur.',
   kitaplar=[
    K('Telhîsü’l-Miftâh', 'تلخيص المفتاح', 'Hatîb el-Kazvînî', '739/1338', 'metin', 'Sekkâkî’nin Miftâh’ının üçüncü kısmını özetler; belâgatın “matn”ı, tanımları ezberlenir.', ['Teftâzânî, Muhtasaru’l-Meânî', 'Teftâzânî, el-Mutavvel', 'Bahâüddîn es-Sübkî, Arûsü’l-efrâh']),
    K('Muhtasaru’l-Meânî', 'مختصر المعاني', 'Sa‘düddîn et-Teftâzânî', '792/1390', 'şerh', 'Telhîs’in orta hacimli şerhi; medresede asıl ders kitabı. Her ibarenin gerekçesini gösterir.', ['Dessûkî, Hâşiye ale’l-Muhtasar']),
    K('el-Îzâh fî ulûmi’l-belâga', 'الإيضاح في علوم البلاغة', 'Hatîb el-Kazvînî', '739/1338', 'metin', 'Kazvînî’nin Telhîs’i kendi eliyle genişlettiği hâli; örnekleri çoğaltır.')]),
  dict(ad='İleri: Mutavvel ve hâşiyeleri', alt='İleri', ac='Meselelerin derinliğine inildiği, tartışmaların ve itirazların görüldüğü basamak.',
   kitaplar=[
    K('el-Mutavvel', 'المطول', 'Sa‘düddîn et-Teftâzânî', '792/1390', 'şerh', 'Telhîs’in büyük şerhi; belâgatı mantık ve kelâmla birlikte işler. Osmanlı medresesinde ileri ders.', ['Seyyid Şerîf Cürcânî, Hâşiye ale’l-Mutavvel', 'Hasan Çelebi (Fenârî), Hâşiye ale’l-Mutavvel']),
    K('Miftâhu’l-ulûm (3. kısım)', 'مفتاح العلوم', 'Sirâceddîn es-Sekkâkî', '626/1229', 'kaynak metin', 'Belâgatı meânî-beyân-bedî‘ şeklinde sistemleştiren kitap; sonraki bütün metinler buna dayanır.', ['Kazvînî, Telhîsü’l-Miftâh', 'Seyyid Şerîf Cürcânî, Şerhu’l-Miftâh']),
    K('Arûsü’l-efrâh', 'عروس الأفراح في شرح تلخيص المفتاح', 'Bahâüddîn es-Sübkî', '773/1372', 'şerh', 'Telhîs’e Şâfiî-Arap çevresinden geniş bir şerh; Teftâzânî’ye alternatif bakış.')]),
  dict(ad='Kurucu eserler', alt='Kaynaklara dönüş', ac='Belâgatın sistemleşmeden önceki canlı hâli. Burada kurallar değil, kuralların doğduğu düşünce okunur.',
   kitaplar=[
    K('Delâilü’l-i‘câz', 'دلائل الإعجاز', 'Abdülkâhir el-Cürcânî', '471/1078', 'kurucu eser', 'Nazm nazariyesi: anlam, kelimelerin tek tek değil, nahiv ilişkileri içindeki dizilişinden doğar. Meânî ilminin kaynağı.'),
    K('Esrârü’l-belâga', 'أسرار البلاغة', 'Abdülkâhir el-Cürcânî', '471/1078', 'kurucu eser', 'Teşbih, temsil ve istiâre üzerine derin bir inceleme; beyân ilminin kaynağı.'),
    K('el-Beyân ve’t-tebyîn', 'البيان والتبيين', 'Câhız', '255/869', 'kurucu eser', 'Hitabet, fesâhat ve beyân üzerine ilk büyük eser; Arap düzyazısının şaheseri.'),
    K('Kitâbü’l-Bedî‘', 'كتاب البديع', 'İbnü’l-Mu‘tez', '296/908', 'kurucu eser', 'Bedî‘ sanatlarını ilk kez bir kitapta toplar.'),
    K('Kitâbü’s-Sınâ‘ateyn', 'كتاب الصناعتين', 'Ebû Hilâl el-Askerî', '395/1005', 'kurucu eser', 'Nazım ve nesir sanatı; sanatları bol şâhitle tanıtır.'),
    K('Sırrü’l-fesâha', 'سر الفصاحة', 'İbn Sinân el-Hafâcî', '466/1074', 'kurucu eser', 'Fesâhatın şartlarını ses ve kelime düzeyinde inceler.')]),
  dict(ad='Kur’an belâgatı ve i‘câz', alt='Uygulama', ac='Belâgat bilgisinin asıl uygulandığı alan: Kur’an’ın i‘câzı ve âyetlerin belâgat tahlili.',
   kitaplar=[
    K('el-Keşşâf', 'الكشاف عن حقائق التنزيل', 'Zemahşerî', '538/1144', 'tefsir', 'Belâgat tefsirinin zirvesi; âyetlerdeki meânî ve beyân inceliklerini gösterir. İtizâlî görüşlerine dikkatle okunur.', ['İbnü’l-Münîr, el-İntisâf (itiraz)', 'Tîbî, Fütûhu’l-gayb (hâşiye)'], ('index.html?dirase=kuran', 'Kur’an Dirâsesi’nde Belâgat sekmesi')),
    K('İ‘câzü’l-Kur’ân', 'إعجاز القرآن', 'Bâkıllânî', '403/1013', 'i‘câz', 'Kur’an’ın şiir ve nesirden farkını karşılaştırmalı gösterir.'),
    K('Beyânü i‘câzi’l-Kur’ân', 'بيان إعجاز القرآن', 'Hattâbî', '388/998', 'risâle', 'İ‘câzı kelimelerin seçimi ve diziliş uyumunda arayan kısa ve etkili risâle.'),
    K('İ‘râbü’l-Kur’ân ve Beyânüh', 'إعراب القرآن وبيانه', 'Muhyiddîn Dervîş', '1402/1982', 'modern tahlil', 'Her âyetin i‘rabını ve belâgatını birlikte veren pratik kaynak.', app=('index.html?dirase=kuran', 'Kur’an Dirâsesi’nde İ‘râb ve Belâgat'))]),
  dict(ad='Osmanlı belâgat geleneği', alt='Bizim gelenek', ac='Osmanlı âlimlerinin hâşiyeleri ve Türkçe belâgat kitapları.',
   kitaplar=[
    K('Hâşiye ale’l-Mutavvel', 'حاشية على المطول', 'Hasan Çelebi (Fenârî)', '886/1481', 'hâşiye', 'Osmanlı medresesinde Mutavvel’in en çok okunan hâşiyesi.'),
    K('Belâgat-ı Osmâniyye', 'بلاغت عثمانيه', 'Ahmed Cevdet Paşa', '1312/1895', 'Türkçe ders kitabı', 'Klasik belâgatı Osmanlı Türkçesine uygulayan ders kitabı.')]),
 ],
 nasil=[
  'Sırayı atlama: Nahiv ve sarf oturmadan Telhîs’e başlamak, kuralları ezberleyip anlamamaya yol açar.',
  'Telhîs’in tanımlarını ezberle, Muhtasar’ı bir hocadan ya da şerhiyle satır satır oku.',
  'Her sanatı öğrendikten sonra Kur’an’da, hadiste ve şiirde en az üç örneğini kendin bul.',
  'Kurucu eserleri (Cürcânî, Câhız) en son değil, Muhtasar’la birlikte paralel okumak anlayışı derinleştirir.',
  'Bir tefsirin belâgat notlarını (Keşşâf, Ebüssuûd) bir sûre boyunca takip et; teori uygulamaya döner.'],
)
