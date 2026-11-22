# İhtisas — Fıkıh ve Fıkıh Usûlü (Hanefî ders geleneği esas; diğer mezheplerin temel metinleri ayrıca)
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
FK = ('fikih.html', 'Fıkıh Dirâsesi’nde Kudûrî ibareleriyle')
ALAN = dict(
 id='fikih', ad='Fıkıh', ar='عِلْمُ الْفِقْه', renk='#5b4a7a',
 kisa='Amelî hükümleri tafsilî delilleriyle bilme ilmi ve bu hükümlerin çıkarılma yöntemi.',
 giris=[
  'Fıkıh, mükellefin fiillerine dair şer‘î hükümleri, Kur’an, Sünnet, icmâ ve kıyas gibi delillerden çıkararak bilme ilmidir. Fıkıh usûlü ise bu hükümlerin hangi yöntemle çıkarıldığını inceler: emir ve nehyin delâleti, âm-hâs, nesh, kıyasın şartları gibi.',
  'Türkiye’deki medrese geleneği Hanefî mezhebine dayanır. Bu yüzden aşağıdaki yol Hanefî ders zincirini esas alır: ilmihal ve muhtasarlarla başlayıp Kudûrî, Mülteka, Hidâye ve büyük şerhlere uzanır. Diğer üç mezhebin temel metinleri ayrı bir basamakta tanıtılır.',
  'Fıkıh usûlü ayrı bir ihtisas alanı olarak verilmiştir; ancak furû‘ (hükümler) ile paralel okunmalıdır: Kudûrî’yi okurken Menâr’a başlamak en iyisidir.'],
 basamaklar=[
  dict(ad='İlmihal ve ilk metinler', alt='Başlangıç', ac='İbadetlerin ve günlük hayatın hükümlerini sade bir dille öğrenmek.',
   kitaplar=[
    K('Büyük İslâm İlmihali', '—', 'Ömer Nasuhi Bilmen', '1391/1971', 'Türkçe ilmihal', 'Hanefî fıkhını Türkçe ve sistemli veren en yaygın ilmihal.'),
    K('Nûru’l-îzâh', 'نور الإيضاح ونجاة الأرواح', 'Hasan eş-Şürünbülâlî', '1069/1659', 'metin', 'Tahâret, namaz, oruç gibi ibadetleri özlü anlatan ilk Arapça fıkıh metni.', ['Şürünbülâlî, Merâki’l-felâh', 'Tahtâvî, Hâşiye alâ Merâki’l-felâh']),
    K('Muhtasarü’l-Kudûrî', 'مختصر القدوري', 'Ebü’l-Hüseyn el-Kudûrî', '428/1037', 'metin', 'Hanefî fıkhının bütün bâblarını kapsayan temel muhtasar; “el-Kitâb” diye anılır.', ['Meydânî, el-Lübâb', 'Merğînânî, Hidâye (Kudûrî ve Câmiu’s-sağîr üzerine)'], FK)]),
  dict(ad='Orta seviye metinler', alt='Orta', ac='Mezhep içi görüş farklarını ve fetvâya esas görüşleri öğrenmek.',
   kitaplar=[
    K('el-Muhtâr ve el-İhtiyâr', 'المختار للفتوى والاختيار لتعليل المختار', 'Abdullah b. Mahmûd el-Mevsılî', '683/1284', 'metin ve şerh', 'Metni fetvâya esas görüşleri, şerhi delilleri verir; Hanefî “mütûn-ı erbaa”dan.'),
    K('Kenzü’d-dekâik', 'كنز الدقائق', 'Ebü’l-Berekât en-Nesefî', '710/1310', 'metin', 'Çok özlü ve yoğun metin; mütûn-ı erbaadan.', ['Zeylaî, Tebyînü’l-hakâik', 'İbn Nüceym, el-Bahrü’r-râik']),
    K('Mülteka’l-ebhur', 'ملتقى الأبحر', 'İbrâhîm el-Halebî', '956/1549', 'metin', 'Dört muteber metni birleştiren Osmanlı’nın en çok okunan fıkıh kitabı.', ['Şeyhîzâde, Mecmau’l-enhur', 'Haskefî, ed-Dürrü’l-müntekâ']),
    K('Dürerü’l-hükkâm', 'درر الحكام شرح غرر الأحكام', 'Molla Hüsrev', '885/1480', 'metin ve şerh', 'Osmanlı kadılarının başvuru kitabı.')]),
  dict(ad='İleri: Hidâye ve şerhleri', alt='İleri', ac='Hükümleri delilleri ve mezhep imamlarının görüşleriyle birlikte okumak.',
   kitaplar=[
    K('el-Hidâye', 'الهداية شرح بداية المبتدي', 'Burhâneddîn el-Merğînânî', '593/1197', 'şerh', 'Hanefî fıkhının ders kitabı; her hükmü naklî ve aklî deliliyle verir.', ['İbnü’l-Hümâm, Fethu’l-kadîr', 'Bâbertî, el-İnâye', 'Aynî, el-Binâye', 'Zeylaî, Nasbü’r-râye (hadislerinin tahrici)']),
    K('Reddü’l-muhtâr (İbn Âbidîn Hâşiyesi)', 'رد المحتار على الدر المختار', 'İbn Âbidîn', '1252/1836', 'hâşiye', 'Hanefî fetvâ birikiminin son büyük derlemesi; müftünün el kitabı.')]),
  dict(ad='Kaynak eserler', alt='Mütehassıs', ac='Mezhebin kuruluş metinleri ve büyük istidlâl kitapları.',
   kitaplar=[
    K('el-Mebsût', 'المبسوط', 'Şemsü’l-eimme es-Serahsî', '483/1090', 'şerh', 'İmam Muhammed’in kitaplarına dayanan, hükümleri gerekçeleriyle tartışan büyük eser.'),
    K('Bedâiu’s-sanâi‘', 'بدائع الصنائع في ترتيب الشرائع', 'Alâeddîn el-Kâsânî', '587/1191', 'sistematik eser', 'Fıkhı mantıklı bir tertiple ve gerekçeleriyle sunan eşsiz kitap.'),
    K('Bidâyetü’l-müctehid', 'بداية المجتهد ونهاية المقتصد', 'İbn Rüşd (el-Hafîd)', '595/1198', 'mukayeseli fıkıh', 'Mezhepler arası ihtilafların sebeplerini gösterir; ihtilaf ilmine giriş.')]),
  dict(ad='Diğer mezheplerin temel metinleri', alt='Mukayese', ac='Diğer mezhepleri kendi kaynaklarından tanımak için birer temel metin.',
   kitaplar=[
    K('Minhâcü’t-tâlibîn (Şâfiî)', 'منهاج الطالبين', 'İmam Nevevî', '676/1277', 'metin', 'Şâfiî mezhebinin en muteber metni.', ['Remlî, Nihâyetü’l-muhtâc', 'İbn Hacer el-Heytemî, Tuhfetü’l-muhtâc']),
    K('er-Risâle (Mâlikî)', 'الرسالة', 'İbn Ebû Zeyd el-Kayrevânî', '386/996', 'metin', 'Mâlikî mezhebinin ilk okunan metni.'),
    K('el-Umde ve el-Muğnî (Hanbelî)', 'عمدة الفقه والمغني', 'İbn Kudâme', '620/1223', 'metin ve büyük eser', 'Hanbelî mezhebinin başlangıç metni ve mukayeseli büyük kaynağı.')]),
 ],
 sahsiyetler=[
  dict(ad='Ebû Hanîfe', ar='أبو حنيفة النعمان', v='150/767', k='Hanefî mezhebinin imamı.'),
  dict(ad='İmam Mâlik', ar='مالك بن أنس', v='179/795', k='Mâlikî mezhebinin imamı.'),
  dict(ad='İmam Ebû Yûsuf', ar='أبو يوسف', v='182/798', k='Ebû Hanîfe’nin öğrencisi; ilk başkadı.'),
  dict(ad='İmam Muhammed', ar='محمد بن الحسن الشيباني', v='189/805', k='Hanefî mezhebinin temel kitaplarını (Zâhirü’r-rivâye) yazan imam.'),
  dict(ad='İmam Şâfiî', ar='الشافعي', v='204/820', k='Şâfiî mezhebinin imamı; usûlün kurucusu.'),
  dict(ad='Ahmed b. Hanbel', ar='أحمد بن حنبل', v='241/855', k='Hanbelî mezhebinin imamı.'),
  dict(ad='Serahsî', ar='السرخسي', v='483/1090', k='el-Mebsût.'),
  dict(ad='Kâsânî', ar='الكاساني', v='587/1191', k='Bedâiu’s-sanâi‘.'),
  dict(ad='Merğînânî', ar='المرغيناني', v='593/1197', k='el-Hidâye.'),
  dict(ad='Molla Hüsrev', ar='ملا خسرو', v='885/1480', k='Osmanlı şeyhülislâmı; Dürer ve Mir’ât.'),
  dict(ad='İbn Âbidîn', ar='ابن عابدين', v='1252/1836', k='Reddü’l-muhtâr.')],
 terimler=[
  dict(ar='الفرض', tr='Farz', d='Kesin delille yapılması istenen fiil.'),
  dict(ar='الواجب', tr='Vâcip', d='Hanefîlerde zannî delille sabit, yapılması gereken fiil.'),
  dict(ar='السنة', tr='Sünnet', d='Peygamberimizin devamlı ya da çoğunlukla yaptığı fiil.'),
  dict(ar='المندوب', tr='Mendup', d='Yapılması sevap olan, terki günah olmayan fiil.'),
  dict(ar='المباح', tr='Mübah', d='Yapılıp yapılmaması serbest bırakılan fiil.'),
  dict(ar='المكروه', tr='Mekruh', d='Yapılmaması daha iyi olan fiil (tahrîmen ve tenzîhen).'),
  dict(ar='الحرام', tr='Haram', d='Kesin delille yasaklanan fiil.'),
  dict(ar='الإجماع', tr='İcmâ', d='Bir dönemdeki müctehidlerin bir hüküm üzerinde birleşmesi.'),
  dict(ar='القياس', tr='Kıyas', d='Hakkında nas bulunmayan meseleyi ortak illet sebebiyle nasla sabit hükme bağlamak.'),
  dict(ar='الاستحسان', tr='İstihsân', d='Daha kuvvetli bir delil sebebiyle kıyasın gereğinden ayrılmak.'),
  dict(ar='العرف', tr='Örf', d='Toplumda yerleşmiş ve dine aykırı olmayan uygulama.'),
  dict(ar='ظاهر الرواية', tr='Zâhirü’r-rivâye', d='İmam Muhammed’in altı kitabında yer alan, Hanefî mezhebinin asıl görüşleri.')],
 nasil=[
  'İbadetleri önce ilmihalden öğren; Arapça metne Nûru’l-îzâh ile geç.',
  'Kudûrî’yi baştan sona bir kez oku; her bâbın ana kavramlarını bir deftere çıkar.',
  'Furû‘ okurken paralelinde usûl oku (Fıkıh Usûlü alanına bak): Menâr’da öğrendiğin kuralın Kudûrî’de nasıl işlediğini gör.',
  'Hidâye’yi okurken Nasbü’r-râye ile hadislerin kaynağına bak.',
  'Fetvâ vermek ayrı bir uzmanlıktır; kitaptan okuduğun hükmü günlük bir meseleye uygulamadan önce bir âlime danış.'],
)
