# İhtisas — Akaid ve Kelâm. Ekoller tarafsızca tanıtılır; tercih yapılmaz.
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
ALAN = dict(
 id='akaid', ad='Akaid ve Kelâm', ar='عِلْمُ الْعَقِيدَة وَالْكَلَام', renk='#3d2a5c',
 kisa='İman esaslarını delilleriyle ortaya koyma ve savunma ilmi.',
 giris=[
  'Akaid, iman edilmesi gereken esasları; kelâm ise bu esasları aklî ve naklî delillerle açıklayan ve itirazlara cevap veren ilmi ifade eder. Allah’ın varlığı ve sıfatları, nübüvvet, âhiret ve kader gibi konuları işler.',
  'Ehl-i sünnet içinde üç ana çizgi vardır: Mâtürîdîlik (Ebû Mansûr el-Mâtürîdî; Hanefîler arasında yaygın), Eş‘arîlik (Ebü’l-Hasen el-Eş‘arî; Şâfiî ve Mâlikîler arasında yaygın) ve Selefî/Eserî çizgi (Ahmed b. Hanbel’in yolu). Bu ekoller temel iman esaslarında birleşir; ihtilaflar çoğunlukla sıfatların yorumu, iman-amel ilişkisi ve kader gibi ayrıntılardadır.',
  'Bu bölüm ekollerden birini savunmaz; her ekolü kendi temel metinleriyle tanıtır. Kendi geleneğini (Türkiye’de çoğunlukla Mâtürîdî) önce sağlam öğrenmek, sonra diğerlerini kendi kaynaklarından okumak en sağlıklı yoldur.'],
 basamaklar=[
  dict(ad='Temel metinler', alt='Başlangıç', ac='Kısa, ezberlenebilir ve bütün Ehl-i sünnetin kabul ettiği iman metinleri.',
   kitaplar=[
    K('el-Fıkhü’l-ekber', 'الفقه الأكبر', 'İmam Ebû Hanîfe’ye nispet edilir', '150/767', 'metin', 'Akaidin en eski metinlerinden; iman esaslarını kısa maddelerle verir. Nispeti tartışılsa da Hanefî geleneğinin temel metnidir.', ['Aliyyülkārî, Minehu’r-ravzi’l-ezher']),
    K('el-Akîdetü’t-Tahâviyye', 'العقيدة الطحاوية', 'Ebû Ca‘fer et-Tahâvî', '321/933', 'metin', 'Ebû Hanîfe ve öğrencilerinin akidesini özetler; üç ekolün de saygı duyduğu ortak metin.', ['İbn Ebi’l-İzz, Şerhu’t-Tahâviyye (Selefî çizgide)', 'Gaznevî, Şerhu’t-Tahâviyye (Mâtürîdî çizgide)']),
    K('Bed’ü’l-emâlî (Kasîde-i Emâlî)', 'بدء الأمالي', 'Sirâceddîn Ali b. Osman el-Ûşî', '575/1179', 'manzum metin', 'Mâtürîdî akidesini 66 beyitte veren, ezberlenen kaside.', ['Aliyyülkārî, Dav’ü’l-meâlî'])]),
  dict(ad='Medrese metni', alt='Orta', ac='Akaidi kelâm yöntemiyle, tanım ve delillerle öğreten klasik ders kitapları.',
   kitaplar=[
    K('el-Akâidü’n-Nesefiyye', 'العقائد النسفية', 'Necmeddîn Ömer en-Nesefî', '537/1142', 'metin', 'Mâtürîdî akidesinin özlü metni; medresede ezberlenir.', ['Teftâzânî, Şerhu’l-Akâid', 'Hayâlî, Hâşiye ale’ş-Şerh', 'Kestelî, Hâşiye']),
    K('Şerhu’l-Akâid', 'شرح العقائد النسفية', 'Sa‘düddîn et-Teftâzânî', '792/1390', 'şerh', 'Nesefî metnini kelâmî delillerle açan, Osmanlı medresesinin akaid ders kitabı.', ['Hayâlî (ö. 875/1470), Hâşiye']),
    K('Cevheretü’t-tevhîd', 'جوهرة التوحيد', 'İbrâhîm el-Lekānî', '1041/1631', 'manzum metin', 'Eş‘arî akidesinin en çok okunan manzum metni.', ['Bâcûrî, Tuhfetü’l-mürîd']),
    K('el-Akîdetü’l-Vâsıtiyye', 'العقيدة الواسطية', 'İbn Teymiyye', '728/1328', 'metin', 'Selefî çizginin en yaygın akide metni.')]),
  dict(ad='Ekollerin kurucu eserleri', alt='İleri', ac='Her ekolü kurucusunun ve ilk büyük temsilcisinin kitabından tanımak.',
   kitaplar=[
    K('Kitâbü’t-Tevhîd', 'كتاب التوحيد', 'Ebû Mansûr el-Mâtürîdî', '333/944', 'kurucu eser', 'Mâtürîdî kelâmının ana kaynağı; bilgi teorisiyle başlar.'),
    K('Tebsıratü’l-edille', 'تبصرة الأدلة', 'Ebü’l-Muîn en-Nesefî', '508/1115', 'sistematik eser', 'Mâtürîdî kelâmının en kapsamlı sistematik sunumu.'),
    K('el-İbâne ve el-Luma‘', 'الإبانة واللمع', 'Ebü’l-Hasen el-Eş‘arî', '324/935', 'kurucu eser', 'Eş‘arî’nin görüşlerini yansıtan iki temel risâlesi.'),
    K('el-İrşâd', 'الإرشاد إلى قواطع الأدلة', 'İmâmü’l-Harameyn el-Cüveynî', '478/1085', 'sistematik eser', 'Eş‘arî kelâmının klasik dönem el kitabı.'),
    K('el-İktisâd fi’l-i‘tikâd', 'الاقتصاد في الاعتقاد', 'Gazzâlî', '505/1111', 'orta hacimli eser', 'İtidalli bir dille yazılmış, okunması kolay kelâm kitabı.')]),
  dict(ad='Müteahhirîn kelâmı', alt='Mütehassıs', ac='Kelâmın felsefeyle karşılaştığı, en ayrıntılı tartışmaların yapıldığı büyük şerhler.',
   kitaplar=[
    K('Şerhu’l-Mevâkıf', 'شرح المواقف', 'Seyyid Şerîf el-Cürcânî (metin: Adudüddîn el-Îcî)', '816/1413 · 756/1355', 'şerh', 'Kelâmın ansiklopedisi; Osmanlı medresesinde ileri seviyede okunurdu.'),
    K('Şerhu’l-Makâsıd', 'شرح المقاصد', 'Sa‘düddîn et-Teftâzânî', '792/1390', 'metin ve şerh', 'Teftâzânî’nin kendi metnine yazdığı büyük kelâm şerhi.'),
    K('el-Müsâyere', 'المسايرة', 'Kemâleddîn İbnü’l-Hümâm', '861/1457', 'mukayeseli eser', 'Mâtürîdî ve Eş‘arî görüşlerini karşılaştırarak veren önemli eser.', ['İbn Ebû Şerîf, el-Müsâmere'])]),
 ],
 sahsiyetler=[
  dict(ad='Ebû Hanîfe', ar='أبو حنيفة', v='150/767', k='Akaide dair risâleler ona nispet edilir.'),
  dict(ad='Ahmed b. Hanbel', ar='أحمد بن حنبل', v='241/855', k='Eserî/Selefî çizginin imamı.'),
  dict(ad='Tahâvî', ar='الطحاوي', v='321/933', k='Akîdetü’t-Tahâviyye.'),
  dict(ad='Ebü’l-Hasen el-Eş‘arî', ar='أبو الحسن الأشعري', v='324/935', k='Eş‘arîliğin kurucusu.'),
  dict(ad='Ebû Mansûr el-Mâtürîdî', ar='أبو منصور الماتريدي', v='333/944', k='Mâtürîdîliğin kurucusu.'),
  dict(ad='Bâkıllânî', ar='الباقلاني', v='403/1013', k='Eş‘arî kelâmının sistemleştiricisi.'),
  dict(ad='Cüveynî', ar='الجويني', v='478/1085', k='İmâmü’l-Harameyn; Gazzâlî’nin hocası.'),
  dict(ad='Ebü’l-Muîn en-Nesefî', ar='أبو المعين النسفي', v='508/1115', k='Tebsıratü’l-edille.'),
  dict(ad='Gazzâlî', ar='الغزالي', v='505/1111', k='Hüccetü’l-İslâm.'),
  dict(ad='Fahreddîn er-Râzî', ar='فخر الدين الرازي', v='606/1210', k='Müteahhirîn kelâmının öncüsü.'),
  dict(ad='İbn Teymiyye', ar='ابن تيمية', v='728/1328', k='Selefî çizginin büyük temsilcisi.'),
  dict(ad='Teftâzânî', ar='التفتازاني', v='792/1390', k='Şerhu’l-Akâid, Şerhu’l-Makâsıd.')],
 terimler=[
  dict(ar='التوحيد', tr='Tevhîd', d='Allah’ın zatında, sıfatlarında ve fiillerinde bir olduğuna inanmak.'),
  dict(ar='الصفات الذاتية', tr='Zâtî sıfatlar', d='Vücûd, kıdem, bekā, muhâlefetün li’l-havâdis, kıyâm bi-nefsihî, vahdâniyyet.'),
  dict(ar='الصفات الثبوتية', tr='Sübûtî sıfatlar', d='Hayat, ilim, irade, kudret, semi‘, basar, kelâm ve (Mâtürîdîlere göre) tekvîn.'),
  dict(ar='التكوين', tr='Tekvîn', d='Mâtürîdîlerin ayrı bir ezelî sıfat kabul ettiği “yaratma” sıfatı; Eş‘arîler bunu kudretin taalluku sayar.'),
  dict(ar='الكسب', tr='Kesb', d='Kulun fiillerinde iradesiyle yöneldiği ve sorumlu tutulduğu pay.'),
  dict(ar='القضاء والقدر', tr='Kazâ ve kader', d='Allah’ın olacak şeyleri ezelde bilip takdir etmesi ve zamanı gelince yaratması.'),
  dict(ar='الإيمان', tr='İman', d='Kalbin tasdiki; Hanefî-Mâtürîdîlere göre amel imanın parçası değildir, kemâlindendir.'),
  dict(ar='النبوة', tr='Nübüvvet', d='Allah’ın insanlara vahiy ulaştırmak için peygamber seçmesi.'),
  dict(ar='المعجزة', tr='Mucize', d='Peygamberin davasını doğrulayan olağanüstü olay.'),
  dict(ar='العصمة', tr='İsmet', d='Peygamberlerin günahtan korunmuş olması.'),
  dict(ar='الرؤية', tr='Rü’yetullah', d='Müminlerin âhirette Allah’ı görmesi meselesi.'),
  dict(ar='التأويل والتفويض', tr='Te’vîl ve tefvîz', d='Haberî sıfatları uygun bir anlamla yorumlamak ya da anlamını Allah’a bırakmak.')],
 nasil=[
  'Önce kendi geleneğinin temel metnini (Tahâviyye veya Nesefî Akaidi) bir şerhle iyice öğren.',
  'Ekoller arası farkları büyütmeden öğren: Temel iman esaslarında birlik olduğunu, ihtilafın ayrıntılarda olduğunu unutma.',
  'Her ekolü kendi kaynağından oku; bir ekolü rakibinin kitabından öğrenmek yanlış anlamaya yol açar.',
  'Kelâmın ileri konularına (Mevâkıf, Makâsıd) mantık ve felsefe terimlerini öğrenmeden girme.',
  'Tekfir ve sert hükümlerden uzak dur; büyük âlimlerin ihtiyatlı üslubunu örnek al.'],
)
