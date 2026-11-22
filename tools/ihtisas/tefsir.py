# İhtisas — Tefsir ve Kur'an İlimleri
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
KD = ('index.html?dirase=kuran', 'Kur’an Dirâsesi’nde Tefsir sekmesi')
ALAN = dict(
 id='tefsir', ad='Tefsir ve Kur’an İlimleri', ar='عِلْمُ التَّفْسِير', renk='#1f5b6e',
 kisa='Kur’an’ın anlamını; dil, rivayet, nüzûl ve usûl bilgisiyle ortaya koyma ilmi.',
 giris=[
  'Tefsir, Kur’an âyetlerinin anlamını ve maksadını insan gücü ölçüsünde açıklama ilmidir. Müfessir; Arap dili ve belâgatını, kıraatleri, nüzûl sebeplerini, nâsih-mensûhu, hadisleri ve fıkıh usûlünü bilmek zorundadır. Bu bilgilerin toplamına “Ulûmü’l-Kur’ân” denir.',
  'Tefsirler iki ana yolda yazılmıştır: Rivâyet tefsiri, âyetleri başka âyetler, hadisler, sahâbe ve tâbiûn sözleriyle açıklar (Taberî, İbn Kesîr). Dirâyet tefsiri ise dil, belâgat, akıl ve içtihada daha geniş yer verir (Zemahşerî, Râzî, Beyzâvî). Bu ikisi birbirinin rakibi değil, tamamlayıcısıdır.',
  'Aşağıdaki yol önce usûle ve kısa bir tefsire, sonra medresede okunan orta hacimli tefsirlere, en sonda da büyük kaynak tefsirlere götürür.'],
 basamaklar=[
  dict(ad='Usûle giriş', alt='Başlangıç', ac='Tefsire başlamadan önce Kur’an’ın nasıl indiği, toplandığı ve nasıl anlaşılacağı.',
   kitaplar=[
    K('Mukaddime fî usûli’t-tefsîr', 'مقدمة في أصول التفسير', 'İbn Teymiyye', '728/1328', 'risâle', 'Tefsirde rivayetin yeri, ihtilafın türleri ve isrâiliyyât üzerine kısa ve öğretici bir risâle.'),
    K('Menâhilü’l-irfân', 'مناهل العرفان في علوم القرآن', 'Muhammed Abdülazîm ez-Zürkânî', '1367/1948', 'modern ders kitabı', 'Vahiy, cem‘, yedi harf, nesh, muhkem-müteşâbih gibi konuları açık bir dille toplar.'),
    K('el-Burhân fî ulûmi’l-Kur’ân', 'البرهان في علوم القرآن', 'Bedreddîn ez-Zerkeşî', '794/1392', 'klasik usûl', 'Kur’an ilimlerini 47 başlıkta toplayan ilk büyük derleme.'),
    K('el-İtkân fî ulûmi’l-Kur’ân', 'الإتقان في علوم القرآن', 'Celâleddîn es-Süyûtî', '911/1505', 'klasik usûl', 'Ulûmü’l-Kur’ân’ın başvuru kitabı; 80 nev‘ ile alanın en kapsamlı eseri.')]),
  dict(ad='İlk tefsir', alt='Kısa tefsir', ac='Kur’an’ı baştan sona kısa bir tefsirle okumak; her âyette asgari anlamı kavramak.',
   kitaplar=[
    K('Tefsîrü’l-Celâleyn', 'تفسير الجلالين', 'Celâleddîn el-Mahallî ve Celâleddîn es-Süyûtî', '864/1459 · 911/1505', 'kısa tefsir', 'Medresede ilk okunan tefsir; âyeti kısa açıklamalarla, metne çok yakın açar.', ['Sâvî, Hâşiye ale’l-Celâleyn', 'Cemel, el-Fütûhâtü’l-ilâhiyye'], KD),
    K('et-Tefsîrü’l-müyesser', 'التفسير الميسر', 'Bir heyet (Medine, Mücemma‘)', 'çağdaş', 'kısa tefsir', 'Sade Arapçayla yazılmış güvenilir çağdaş özet tefsir; Arapça okuma alıştırması için de uygun.', app=KD)]),
  dict(ad='Medrese tefsirleri', alt='Orta', ac='Osmanlı medresesinde asıl okunan, dil ve akaid meselelerini birlikte işleyen tefsirler.',
   kitaplar=[
    K('Envârü’t-tenzîl ve esrârü’t-te’vîl', 'أنوار التنزيل وأسرار التأويل', 'Kâdî Beyzâvî', '685/1286 (691 de denir)', 'dirâyet tefsiri', 'Keşşâf’ın belâgat birikimini Ehl-i sünnet çizgisinde özetler; Osmanlı medresesinin tefsir ders kitabı.', ['Şeyhzâde, Hâşiye ale’l-Beyzâvî', 'Şihâbeddîn el-Hafâcî, İnâyetü’l-kâdî', 'Konevî, Hâşiye']),
    K('Medârikü’t-tenzîl', 'مدارك التنزيل وحقائق التأويل', 'Ebü’l-Berekât en-Nesefî', '710/1310', 'dirâyet tefsiri', 'Hanefî-Mâtürîdî bakışla yazılmış özlü ve dengeli bir tefsir.'),
    K('Meâlimü’t-tenzîl', 'معالم التنزيل', 'Begavî', '516/1122', 'rivâyet tefsiri', 'Rivayetleri ayıklayarak veren, sade ve güvenilir orta hacimli tefsir.'),
    K('Tefsîrü’l-Kur’âni’l-azîm', 'تفسير القرآن العظيم', 'İbn Kesîr', '774/1373', 'rivâyet tefsiri', 'Âyeti âyetle, sonra hadisle açıklar; hadislerin senedini değerlendirir.', app=KD)]),
  dict(ad='Büyük kaynak tefsirler', alt='İleri', ac='Bir âyet üzerinde derinleşmek için başvurulan büyük tefsirler.',
   kitaplar=[
    K('Câmiu’l-beyân', 'جامع البيان عن تأويل آي القرآن', 'İbn Cerîr et-Taberî', '310/923', 'rivâyet tefsiri', 'Tefsirlerin anası; sahâbe ve tâbiûn görüşlerini senetleriyle toplar ve tercih yapar.', app=KD),
    K('el-Keşşâf', 'الكشاف', 'Zemahşerî', '538/1144', 'dil ve belâgat tefsiri', 'Âyetlerin belâgat inceliklerinde rakipsiz; itizâlî yorumları dikkatle ayırt edilerek okunur.', ['İbnü’l-Münîr, el-İntisâf', 'Tîbî, Fütûhu’l-gayb']),
    K('Mefâtîhu’l-gayb (et-Tefsîrü’l-kebîr)', 'مفاتيح الغيب', 'Fahreddîn er-Râzî', '606/1210', 'dirâyet tefsiri', 'Kelâm, felsefe ve dil meselelerini âyetlerle birlikte tartışan ansiklopedik tefsir.', app=KD),
    K('el-Câmi‘ li-ahkâmi’l-Kur’ân', 'الجامع لأحكام القرآن', 'Kurtubî', '671/1273', 'ahkâm tefsiri', 'Âyetlerin fıkhî hükümlerini mezheplerin görüşleriyle birlikte işler.', app=KD),
    K('İrşâdü’l-akli’s-selîm', 'إرشاد العقل السليم', 'Ebüssuûd Efendi', '982/1574', 'dirâyet tefsiri', 'Osmanlı’nın en meşhur tefsiri; belâgat incelikleriyle tanınır.'),
    K('Rûhu’l-meânî', 'روح المعاني', 'Âlûsî', '1270/1854', 'dirâyet tefsiri', 'Önceki tefsirlerin birikimini toplayan geniş tefsir; işârî yorumlara da yer verir.', app=KD)]),
  dict(ad='Modern ve Türkçe tefsirler', alt='Günümüz', ac='Çağımızın sorularına da cevap arayan tefsirler.',
   kitaplar=[
    K('Hak Dini Kur’an Dili', '—', 'Elmalılı Muhammed Hamdi Yazır', '1361/1942', 'Türkçe tefsir', 'Cumhuriyet döneminin en kapsamlı Türkçe tefsiri; dil ve belâgat tahlilleri güçlüdür.', app=KD),
    K('et-Tahrîr ve’t-tenvîr', 'التحرير والتنوير', 'Muhammed Tâhir İbn Âşûr', '1393/1973', 'dil ve makâsıd tefsiri', 'Belâgat ve makâsıd bakışını birleştiren çağdaş büyük tefsir.', app=KD),
    K('Kur’an Yolu', '—', 'Hayreddin Karaman ve heyet (Diyanet)', 'çağdaş', 'Türkçe tefsir', 'Anlaşılır Türkçeyle yazılmış, klasik kaynaklara dayanan beş ciltlik tefsir.')]),
 ],
 sahsiyetler=[
  dict(ad='İbn Abbâs', ar='عبد الله بن عباس', v='68/687', k='Tercümânü’l-Kur’ân; sahâbe tefsirinin önderi.'),
  dict(ad='Mücâhid b. Cebr', ar='مجاهد بن جبر', v='104/722', k='İbn Abbâs’ın öğrencisi; Mekke tefsir okulu.'),
  dict(ad='Taberî', ar='ابن جرير الطبري', v='310/923', k='Rivâyet tefsirinin imamı.'),
  dict(ad='Zemahşerî', ar='الزمخشري', v='538/1144', k='Belâgat tefsirinin zirvesi (el-Keşşâf).'),
  dict(ad='Fahreddîn er-Râzî', ar='فخر الدين الرازي', v='606/1210', k='Kelâmî tefsirin büyük temsilcisi.'),
  dict(ad='Kurtubî', ar='القرطبي', v='671/1273', k='Ahkâm tefsiri.'),
  dict(ad='Beyzâvî', ar='البيضاوي', v='685/1286', k='Medrese tefsir ders kitabının müellifi.'),
  dict(ad='İbn Kesîr', ar='ابن كثير', v='774/1373', k='Hadis merkezli rivâyet tefsiri.'),
  dict(ad='Süyûtî', ar='السيوطي', v='911/1505', k='el-İtkân; Celâleyn’in ikinci müellifi.'),
  dict(ad='Ebüssuûd Efendi', ar='أبو السعود', v='982/1574', k='Osmanlı şeyhülislâmı ve müfessiri.'),
  dict(ad='Elmalılı Hamdi Yazır', ar='—', v='1361/1942', k='Hak Dini Kur’an Dili.')],
 terimler=[
  dict(ar='التفسير بالمأثور', tr='Rivâyet tefsiri', d='Âyeti âyet, hadis, sahâbe ve tâbiûn sözleriyle açıklama.'),
  dict(ar='التفسير بالرأي', tr='Dirâyet tefsiri', d='Dil, usûl ve ilmî birikime dayanan içtihatla açıklama.'),
  dict(ar='أسباب النزول', tr='Esbâb-ı nüzûl', d='Âyetlerin inmesine vesile olan olaylar ve sorular.'),
  dict(ar='الناسخ والمنسوخ', tr='Nâsih-mensûh', d='Bir hükmün sonra gelen başka bir hükümle kaldırılması meselesi.'),
  dict(ar='المحكم والمتشابه', tr='Muhkem-müteşâbih', d='Anlamı açık olan ve birden çok anlama ihtimali bulunan âyetler.'),
  dict(ar='المكي والمدني', tr='Mekkî-Medenî', d='Hicretten önce ve sonra inen âyet ve sûreler.'),
  dict(ar='القراءات', tr='Kıraat', d='Kur’an’ın sahih senetle gelen farklı okunuş yolları.'),
  dict(ar='الإسرائيليات', tr='İsrâiliyyât', d='Ehl-i kitap kaynaklarından tefsire giren haberler.'),
  dict(ar='الإعجاز', tr='İ‘câz', d='Kur’an’ın benzerinin getirilemeyişi.'),
  dict(ar='المناسبة', tr='Münâsebet', d='Âyetler ve sûreler arasındaki anlam bağı.'),
  dict(ar='غريب القرآن', tr='Garîbü’l-Kur’ân', d='Kur’an’daki az bilinen kelimelerin açıklaması.'),
  dict(ar='الوجوه والنظائر', tr='Vücûh ve nezâir', d='Bir kelimenin Kur’an’daki farklı anlamları ve benzer kullanımları.')],
 nasil=[
  'Önce usûl: Bir usûl kitabını (Zürkânî ya da İtkân’dan seçmeler) okumadan büyük tefsirlere girme.',
  'Kur’an’ı Celâleyn ya da Müyesser ile en az bir kez baştan sona oku; büyük tefsirler sonra anlam kazanır.',
  'Bir sûreyi seç; aynı âyeti Taberî, Zemahşerî, Râzî ve İbn Kesîr’de karşılaştırarak oku. Farklılıkların sebebini not et.',
  'Beyzâvî’yi Şeyhzâde hâşiyesiyle okumak, medrese usulünü en iyi öğreten yoldur.',
  'İsrâiliyyât ve zayıf rivayetlerde ihtiyatlı ol; İbn Kesîr’in değerlendirmelerine dikkat et.'],
)
