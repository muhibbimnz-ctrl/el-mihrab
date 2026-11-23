# Akaid ve Kelâm — araştırmaya dayalı yenileme (TDV İA "Kelâm" ve ilgili maddeler; İbn Haldun, Mukaddime’deki mütekaddimîn–müteahhirîn ayrımı;
# kelâmın felsefîleşme süreci üzerine çalışmalar (Gazzâlî–Râzî); Îcî, el-Mevâkıf düzeni; Nesefî, el-Akāid’de bilginin kaynakları; Taşköprizâde ve Saçaklızâde’nin âdâb literatürü)
from z_ortak import P, T, B, M

EK = {
 'Ebû Mansûr el-Mâtürîdî': ('Kitâbü’t-Tevhîd’e bilgi teorisiyle başlar: bilgi duyular (ıyân), haber ve akıl yürütme (nazar) ile elde edilir. Aklın iyi ve kötüyü kısmen bilebileceğini, Allah’ın fiillerinin hikmetli olduğunu ve tekvin sıfatını savunması Mâtürîdî kelâmını Eş‘arîlikten ayırır. Te’vîlâtü’l-Kur’ân ile Sünnî kelâmî tefsirin de kurucusudur.', 'Ona nispet edilen Şerhu’l-Fıkhi’l-ekber’in Ebü’l-Leys es-Semerkandî’ye ait olduğu kabul edilir.'),
 'Ebü’l-Hasan el-Eş‘arî': ('Kırk yaşına kadar Mu‘tezilî Ebû Ali el-Cübbâî’nin talebesi iken, Basra camiinde Mu‘tezile’den ayrıldığını ilan etti. Kelâm yöntemini Ehl-i sünnet akāidini savunmak için kullanması, kelâmı Sünnî dünyada meşru kıldı. Makālâtü’l-İslâmiyyîn mezhepler tarihinin, el-Lüma‘ ise Eş‘arî kelâmının temel metnidir.', 'el-İbâne an usûli’d-diyâne’nin farklı nüshaları ve Eş‘arî’nin son görüşünü yansıtıp yansıtmadığı tartışmalıdır.'),
 'İmam Gazzâlî': ('el-Munkız’da anlattığı şüphe ve arayış dönemi, onu kelâmın sınırlarını sorgulamaya götürdü. Tehâfütü’l-felâsife’de filozofların yirmi meselesini eleştirdi, ancak mantığı (Mi‘yârü’l-ilm, el-Kıstâsü’l-müstakîm) Sünnî ilimlere taşıdı. İbn Haldun’a göre kelâmda “müteahhirîn” yolu onunla başlar.', ''),
 'Fahreddîn er-Râzî': ('Kelâm ile felsefeyi aynı problemler etrafında buluşturan, bu yüzden “felsefî kelâm”ın gerçek kurucusu sayılan âlimdir. el-Muhassal ve el-Metâlibü’l-âliye’de İbn Sînâ’nın kavramlarıyla tartışır; Esâsü’t-takdîs’te akıl ile naklin çatıştığı durumlarda “kānûn-ı küllî”yi formüle etti.', ''),
 'Sa‘düddîn et-Teftâzânî': ('Şerhu’l-Akāid’i, Ömer en-Nesefî’nin Mâtürîdî metnini çoğu yerde Eş‘arî bakışla şerh eder; bu yüzden iki ekolün buluştuğu medrese metni oldu. Şerhu’l-Makāsıd, müteahhirîn kelâmının en kapsamlı eserlerindendir.', 'Mâtürîdî mi Eş‘arî mi olduğu tartışılmıştır; eserlerinde iki ekolün görüşlerini birlikte değerlendirir.'),
 'Adudüddîn el-Îcî': ('el-Mevâkıf, kelâmı altı “mevkıf”a ayırır: bilgi ve nazar, umûr-ı âmme (varlık, yokluk, vücûb, imkân), arazlar, cevherler, ilâhiyyât ve sem‘iyyât. Bu düzen müteahhirîn kelâmının standart planı oldu; Seyyid Şerîf’in şerhiyle Osmanlı medreselerinin en ileri kelâm kitabıydı.', ''),
}

KISILER = [
 P('Ma‘bed el-Cühenî', 'معبد الجهني', '80/699', 'ilk', 'Kaderiyye', 'Basralı; kader meselesinde insanın fiillerini Allah’ın ezelî takdirinden bağımsız gören ilk kişilerdendir. Görüşlerine İbn Ömer’in sert tepkisi Müslim’in ilk hadisinde (Cibrîl hadisinin rivayet sebebi) anlatılır. Haccâc döneminde öldürüldü.'),
 P('Hasan b. Muhammed b. el-Hanefiyye', 'الحسن بن محمد بن الحنفية', '100/718 civarı', 'ilk', 'ircâ', 'Hz. Ali’nin torunu; siyasî ihtilaflarda hüküm vermeyip meseleyi Allah’a bırakmayı (ircâ) savunan risâlesi, Mürcie düşüncesinin bilinen en eski metnidir.', ['Kitâbü’l-İrcâ']),
 P('Gaylân ed-Dımaşkī', 'غيلان الدمشقي', '105/723 sonrası', 'ilk', 'Kaderiyye', 'Şamlı kelâmcı; insanın kendi fiillerinin yaratıcısı olduğu ve imamın Kureyşli olmasının gerekmediği görüşleriyle tanınır. Hişâm b. Abdülmelik döneminde idam edildi.'),
 P('Ca‘d b. Dirhem', 'الجعد بن درهم', '124/742', 'ilk', 'Cehmiyye öncüsü', 'Kur’an’ın mahlûk olduğunu ve sıfatların reddini ilk savunanlardan sayılır; görüşleri talebesi Cehm b. Safvân ile yayıldı. Emevî valisi Hâlid el-Kasrî tarafından idam edildi.'),
 P('Amr b. Ubeyd', 'عمرو بن عبيد', '144/761', 'mutezile', 'Mu‘tezile', 'Basralı zâhid; Vâsıl b. Atâ ile birlikte Mu‘tezile’nin kurucusu sayılır. Zühdü ve dürüstlüğüyle Abbâsî halifesi Mansûr’un bile saygısını kazandı. Kader ve büyük günah konularında Mu‘tezile’nin ilk görüşlerini temsil eder.'),
 P('Nazzâm', 'إبراهيم بن سيار النظام', '231/845', 'mutezile', 'Mu‘tezile', 'Basra Mu‘tezilesi’nin özgün düşünürü; Câhız’ın hocasıdır. Cüz’-i lâ yetecezzâ’yı reddetmesi, “tafra” ve “kümûn” nazariyeleri ve Kur’an’ın i‘câzını “sarfe” ile açıklaması meşhurdur. İcmâ ve haber-i vâhid konusundaki tenkitleri usûlde tartışma doğurdu.'),
 P('Bişr el-Merîsî', 'بشر المريسي', '218/833', 'mutezile', 'Mürcie-Cehmiyye', 'Bağdatlı kelâmcı ve fakih; Ebû Yûsuf’tan fıkıh okudu. İmanı tasdikten ibaret görmesi ve Kur’an’ın mahlûk olduğunu savunmasıyla mihne sürecinin fikrî arka planında yer aldı. Dârimî’nin er-Red ale’l-Merîsî’si ona reddiyedir.'),
 P('Ebû Ali el-Cübbâî', 'أبو علي الجبائي', '303/916', 'mutezile', 'Mu‘tezile', 'Basra Mu‘tezilesi’nin reisi ve Eş‘arî’nin hocasıdır. Mu‘tezilî kelâmı sistemleştirdi; Eş‘arî’nin ondan ayrılmasına sebep olduğu nakledilen “üç kardeş” tartışması meşhurdur. Tefsiri kaybolmuş, görüşleri Kādî Abdülcebbâr’ın eserlerinde korunmuştur.'),
 P('Ebû Hâşim el-Cübbâî', 'أبو هاشم الجبائي', '321/933', 'mutezile', 'Mu‘tezile', 'Ebû Ali’nin oğlu; “ahvâl” nazariyesiyle sıfat tartışmasına yeni bir boyut getirdi. Behşemiyye kolunun kurucusudur ve Kādî Abdülcebbâr bu çizgidedir.'),
 P('Osman b. Saîd ed-Dârimî', 'عثمان بن سعيد الدارمي', '280/894', 'ilk', 'Ehl-i hadis', 'Herat’ta yaşayan muhaddis; Ahmed b. Hanbel ve İbn Maîn’in talebesidir. er-Red ale’l-Cehmiyye ve Nakzu’d-Dârimî ale’l-Merîsî, sıfatları te’vilsiz kabul eden Ehl-i hadis akidesinin erken temel metinlerindendir.', ['er-Red ale’l-Cehmiyye', 'en-Nakz ale’l-Merîsî']),
 P('İbn Huzeyme (akide)', 'ابن خزيمة', '311/924', 'ilk', 'Ehl-i hadis', 'Nîşâburlu büyük muhaddis. Kitâbü’t-Tevhîd ve isbâtü sıfâti’r-Rab’da sıfat âyet ve hadislerini senetleriyle toplayıp te’vile karşı çıkar; Selefî akide literatürünün klasiklerindendir.', ['Kitâbü’t-Tevhîd']),
 P('Hakîm es-Semerkandî', 'الحكيم السمرقندي', '342/953', 'kurucu', 'Mâtürîdî', 'Semerkant kadısı; Mâtürîdî’nin çağdaşı ve onun çevresindendir. es-Sevâdü’l-a‘zam, Sâmânî emîrinin isteğiyle Ehl-i sünnet akidesini altmış iki madde hâlinde açıklayan, erken dönemde Farsçaya da çevrilen bir halk akidesidir.', ['es-Sevâdü’l-a‘zam']),
 P('Ebû İshâk el-İsferâyînî', 'أبو إسحاق الإسفراييني', '418/1027', 'mutekaddimin', 'Eş‘arî', 'Nîşâbur’da ders veren Eş‘arî kelâmcı ve Şâfiî usûlcü; Bâkıllânî ve İbn Fûrek ile birlikte Eş‘arîliğin ikinci kuşağını oluşturur. Mütevâtir haberin bilgi değeri ve icmâ konusundaki görüşleri kelâm ve usûlde etkilidir.'),
 P('Ebû Şekûr es-Sâlimî', 'أبو شكور السالمي', 'V/XI. yy', 'mutekaddimin', 'Mâtürîdî', 'Mâverâünnehirli Hanefî-Mâtürîdî kelâmcı. et-Temhîd fî beyâni’t-tevhîd, Mâtürîdî akāidini halka yönelik ve mezhepleri reddeden bir üslupla anlatır; Pezdevî ve Nesefî’den önceki dönemin önemli kaynaklarındandır.', ['et-Temhîd fî beyâni’t-tevhîd']),
 P('Nasîrüddîn-i Tûsî', 'نصير الدين الطوسي', '672/1274', 'mutaahhirin', 'İmâmiyye, felsefe', 'Merâga rasathanesinin kurucusu filozof, astronom ve İmâmî kelâmcıdır. Tecrîdü’l-i‘tikād, kelâmı felsefî kavramlarla en yoğun biçimde ifade eden metinlerdendir; Sünnî âlimlerin de (Kuşçu, Devvânî) şerh ettiği bu eser, iki geleneğin kesiştiği yerdir. Râzî’nin Muhassal’ını Telhîsü’l-Muhassal’da eleştirdi.', ['Tecrîdü’l-i‘tikād', 'Telhîsü’l-Muhassal', 'Şerhu’l-İşârât']),
 P('Ebü’l-Berekât en-Nesefî (akide)', 'أبو البركات النسفي', '710/1310', 'mutaahhirin', 'Mâtürîdî', 'Hanefî fakih ve müfessir. Umdetü’l-akāid ve kendi şerhi el-İ‘timâd, Mâtürîdî akāidinin özlü metinlerindendir; Medârik tefsiri ve Kenz de onundur.', ['Umdetü’l-akāid', 'el-İ‘timâd fi’l-i‘tikād']),
 P('Kemâleddîn İbn Ebû Şerîf', 'كمال الدين ابن أبي شريف', '906/1500', 'mutaahhirin', 'Eş‘arî', 'Kudüslü Şâfiî âlim; İbnü’l-Hümâm’ın talebesidir. Hocasının el-Müsâyere’sini el-Müsâmere adıyla şerh ederek Mâtürîdî-Eş‘arî karşılaştırmasının önemli bir metnini ortaya koydu.', ['el-Müsâmere şerhu’l-Müsâyere']),
 P('Celâleddîn ed-Devvânî', 'جلال الدين الدواني', '908/1502', 'mutaahhirin', 'Eş‘arî, felsefî kelâm', 'Şirazlı filozof-kelâmcı. Şerhu’l-Akāidi’l-Adudiyye ile Tecrîd şerhine yazdığı “kadîm” ve “cedîd” hâşiyeler, Sadreddîn ed-Deştekî ile tartışmaları (Tabakātü’l-Celâliyye ve’s-Sadriyye) Osmanlı medreselerinde uzun süre okundu.', ['Şerhu’l-Akāidi’l-Adudiyye', 'Hâşiye-i kadîme ve cedîde (Tecrîd)', 'Ahlâk-ı Celâlî']),
 P('Ali Kuşçu', 'علي القوشجي', '879/1474', 'osmanli', 'kelâm, astronomi', 'Semerkant rasathanesinde Uluğ Bey’in yanında yetişen astronom ve kelâmcı; Fâtih döneminde İstanbul’a geldi. Tecrîd’e yazdığı Şerh-i cedîd, Osmanlı ve İran medreselerinde felsefî kelâmın ana metinlerinden oldu; Ayasofya’da ders verdi.', ['Şerhu Tecrîdi’l-i‘tikād (Şerh-i cedîd)', 'Risâle fi’l-hey’e']),
 P('Hızır Bey', 'خضر بك', '863/1459', 'osmanli', 'Osmanlı', 'Fâtih’in İstanbul’daki ilk kadısı. Kasîde-i Nûniyye, Ehl-i sünnet akāidini 105 beyitte özetleyen manzumedir; oğlu Sinan Paşa ve talebesi Hayâlî’nin şerhleriyle çok okunmuştur.', ['el-Kasîdetü’n-Nûniyye']),
 P('Hocazâde Muslihuddîn', 'خواجه زاده', '893/1488', 'osmanli', 'Osmanlı', 'Bursalı Osmanlı âlimi; Fâtih’in isteğiyle Alâeddîn et-Tûsî ile birlikte Gazzâlî ile filozoflar arasında hakemlik eden Tehâfüt’ünü yazdı ve bu yarışmayı kazandı. Eser, Osmanlı’da kelâm-felsefe ilişkisinin simgesi olmuştur.', ['Tehâfütü’l-felâsife', 'Şerhu’l-Mevâkıf hâşiyesi']),
 P('Saçaklızâde Mehmed Efendi', 'ساجقلي زاده', '1145/1732', 'osmanli', 'Osmanlı, âdâb', 'Maraşlı Osmanlı âlimi. Takrîrü’l-kavânîn ve el-Velediyye adlı eserleri âdâb-ı bahs ve münazara ilminin Osmanlı medreselerinde en çok okunan metinleri oldu; Tertîbü’l-ulûm ise ilimlerin tasnifi ve okuma sırasına dair değerli bir rehberdir.', ['Takrîrü’l-kavânîn', 'Risâletü’l-Velediyye', 'Tertîbü’l-ulûm']),
 P('Dâvûd-i Karsî', 'داود القارصي', '1169/1756', 'osmanli', 'Osmanlı', 'Karslı Osmanlı müderrisi; mantık, nahiv, kelâm ve akāid alanlarında yazdığı şerhlerle medreselerde iz bıraktı. Kasîde-i Nûniyye ve Emâlî şerhleri akāid öğretiminde kullanıldı.', ['Şerhu’l-Kasîdeti’n-Nûniyye', 'Şerhu Bed’i’l-emâlî']),
 P('Filibeli Ahmed Hilmi', 'شهبندرزاده أحمد حلمي', '1914', 'modern', 'Yeni kelâm', 'Osmanlı’nın son dönem düşünürü (Şehbenderzâde). Huzur-ı Akl u Fende Maddiyyûn Meslek-i Dalâleti’nde materyalizme karşı İslâm inancını modern felsefî tartışmalarla savunarak yeni ilm-i kelâm arayışının öncülerinden oldu.', ['Huzur-ı Akl u Fende Maddiyyûn Meslek-i Dalâleti', 'İslâm Tarihi']),
 P('Muhammed Zâhid el-Kevserî (akide)', 'محمد زاهد الكوثري', '1952', 'modern', 'Mâtürîdî', 'Düzceli Osmanlı âlimi, son şeyhülislâm vekili; Kahire’de yaşadı. Mâtürîdî-Hanefî çizgiyi savunan tahkik ve ta‘lîkleriyle (Beyhakī’nin el-Esmâ ve’s-sıfât’ı, İşârâtü’l-merâm neşri gibi) modern dönemde Sünnî kelâmın önemli savunucularındandır.', ['Makālâtü’l-Kevserî', 'Te’nîbü’l-Hatîb']),
 P('Bekir Topaloğlu', 'بكر طوبال أوغلو', '2019', 'modern', 'Türk kelâm akademisyeni', 'Türkiye’de akademik kelâm çalışmalarının kurucu kuşağındandır. Mâtürîdî’nin Kitâbü’t-Tevhîd’ini tahkik edip (M. Aruçi ile) Türkçeye çevirdi; Kelâm İlmi: Giriş ve Allah’ın Varlığı (İsbât-ı Vâcib) eserleri ders kitabı olarak okutuldu. TDV İslâm Ansiklopedisi’nin kelâm maddelerinin önemli kısmını yazdı.', ['Kelâm İlmi: Giriş', 'Allah’ın Varlığı (İsbât-ı Vâcib)', 'Kitâbü’t-Tevhîd tercümesi']),
]

TASNIF = dict(
 tasnif=[
  dict(g='Konu tasnifi: kelâm kitaplarının bölüm düzeni', d='Kelâm kitaplarının iskeleti zamanla değişti; mütekaddimîn bilgi bahsinden sonra doğrudan âlemin hudûsuna geçerken müteahhirîn varlığın genel hükümleriyle (umûr-ı âmme) başlar.', items=[
   dict(ad='İlâhiyyât', ar='الإلهيات', d='Allah’ın varlığı, birliği, sıfatları ve fiilleri; halk-ı ef‘âl, kader ve rü’yet meseleleri.', ornek=['İsbât-ı vâcib', 'Sıfât-ı zâtiyye ve subûtiyye', 'Tekvin', 'Kesb']),
   dict(ad='Nübüvvât', ar='النبوات', d='Peygamberliğin imkânı ve ispatı, mu‘cize, peygamberlerin sıfatları (sıdk, emanet, ismet, fetânet, tebliğ).', ornek=['Mu‘cize ve kerâmet', 'İsmet', 'Hz. Muhammed’in nübüvvetinin delilleri']),
   dict(ad='Sem‘iyyât', ar='السمعيات', d='Ancak nakille bilinebilen konular: kabir, kıyamet, haşir, mîzan, sırat, şefaat, cennet ve cehennem.', ornek=['Âhiret hâlleri', 'Melek, cin, ruh']),
   dict(ad='İmâmet', ar='الإمامة', d='Sünnîlerde fıkhî bir mesele olduğu kabul edildiği hâlde Şîa ile tartışma sebebiyle kelâm kitaplarının sonuna eklendi.', ornek=['Hilâfetin şartları', 'Hulefâ-i Râşidîn’in fazileti']),
   dict(ad='Mütekaddimîn düzeni', ar='ترتيب المتقدمين', d='Bilgi ve nazar → âlemin hudûsu → Sâni‘in varlığı → sıfatlar → fiiller → nübüvvet → sem‘iyyât → imâmet.', ornek=['Mâtürîdî, Kitâbü’t-Tevhîd', 'Bâkıllânî, et-Temhîd', 'Cüveynî, el-İrşâd']),
   dict(ad='Müteahhirîn düzeni (el-Mevâkıf)', ar='ترتيب المتأخرين', d='Altı mevkıf: mukaddimât (bilgi-nazar), umûr-ı âmme (vücûd, vücûb, imkân, illiyet), a‘râz, cevâhir, ilâhiyyât, sem‘iyyât.', ornek=['Îcî, el-Mevâkıf', 'Teftâzânî, el-Makāsıd', 'Tûsî, Tecrîdü’l-i‘tikād'])]),
  dict(g='Akîde metinleri (mütûn)', d='Ezberlenip şerh edilen özlü inanç metinleri.', items=[
   dict(ad='el-Fıkhu’l-ekber', ar='الفقه الأكبر', d='Ebû Hanîfe’ye nispet edilen, Hammâd b. Ebû Hanîfe rivayetiyle gelen kısa akide metni.', ornek=['Şerhleri: Aliyyü’l-Kārî, Minehu’r-ravzi’l-ezher; Ebü’l-Müntehâ el-Mağnisâvî']),
   dict(ad='el-Akīdetü’t-Tahâviyye', ar='العقيدة الطحاوية', d='Ebû Hanîfe ve iki talebesinin akidesini anlatan, bütün Sünnî ekollerin benimsediği metin.', ornek=['Şerhler: Gaznevî, Ekmelüddîn el-Bâbertî, İbn Ebi’l-İz']),
   dict(ad='el-Akāidü’n-Nesefiyye', ar='العقائد النسفية', d='Ömer en-Nesefî’nin Mâtürîdî akidesini özetleyen metni; medresenin ana akide metni.', ornek=['Teftâzânî, Şerhu’l-Akāid']),
   dict(ad='Bed’ü’l-emâlî (Kasîde-i Lâmiyye)', ar='بدء الأمالي', d='Sirâceddîn el-Ûşî’nin 66 beyitlik Mâtürîdî akide manzumesi.', ornek=['Şerhleri: Aliyyü’l-Kārî, Dâvûd-i Karsî']),
   dict(ad='el-Kasîdetü’n-Nûniyye', ar='القصيدة النونية', d='Hızır Bey’in Osmanlı’da çok okunan akide manzumesi.', ornek=['Hayâlî, Şerhu’n-Nûniyye']),
   dict(ad='el-Akāidü’l-Adudiyye', ar='العقائد العضدية', d='Îcî’nin Eş‘arî akāidini özetleyen kısa metni.', ornek=['Devvânî, Şerhu’l-Akāidi’l-Adudiyye']),
   dict(ad='Ümmü’l-berâhîn (es-Senûsiyye)', ar='أم البراهين', d='Senûsî’nin hükm-i aklî ve sıfatlar tasnifi üzerine kurulu, Kuzey Afrika’da çok yaygın Eş‘arî metni.', ornek=['Şerhleri: Senûsî, Bâcûrî']),
   dict(ad='Cevheretü’t-tevhîd', ar='جوهرة التوحيد', d='Lekānî’nin 144 beyitlik Eş‘arî manzumesi; Ezher’in temel akide metni.', ornek=['Bâcûrî, Tuhfetü’l-mürîd'])]),
  dict(g='Kapsamlı kelâm eserleri', d='Kelâmın bütün meselelerini delilleriyle işleyen büyük eserler.', items=[
   dict(ad='Mütekaddimîn dönemi', ar='كتب المتقدمين', d='Cevher-araz fiziği ve hudûs delili üzerine kurulu sistemler.', ornek=['Mâtürîdî, Kitâbü’t-Tevhîd', 'Bâkıllânî, et-Temhîd', 'Kādî Abdülcebbâr, el-Muğnî', 'Ebü’l-Muîn en-Nesefî, Tebsıratü’l-edille', 'Cüveynî, el-İrşâd ve eş-Şâmil']),
   dict(ad='Geçiş dönemi', ar='مرحلة الانتقال', d='Mantığın kelâma girişi ve felsefeye eleştiri.', ornek=['Gazzâlî, el-İktisâd fi’l-i‘tikād', 'Gazzâlî, Tehâfütü’l-felâsife', 'Şehristânî, Nihâyetü’l-ikdâm']),
   dict(ad='Müteahhirîn dönemi', ar='كتب المتأخرين', d='Felsefî kavramlarla örülmüş sistemler.', ornek=['Râzî, el-Muhassal ve el-Metâlibü’l-âliye', 'Âmidî, Ebkârü’l-efkâr', 'Beyzâvî, Tavâliu’l-envâr', 'Îcî, el-Mevâkıf', 'Teftâzânî, el-Makāsıd']),
   dict(ad='Mâtürîdî büyük eserleri', ar='كتب الماتريدية', d='Mâtürîdî ekolünün kapsamlı kaynakları.', ornek=['Ebü’l-Yüsr el-Pezdevî, Usûlü’d-dîn', 'Nûreddîn es-Sâbûnî, el-Bidâye', 'İbnü’l-Hümâm, el-Müsâyere'])]),
  dict(g='Şerh ve hâşiye literatürü', d='Medresede asıl öğrenilen kelâm, metinler üzerine yazılan şerh-hâşiye halkalarında yaşadı.', items=[
   dict(ad='Şerhu’l-Akāid halkası', ar='حلقة شرح العقائد', d='Teftâzânî’nin şerhi ve üzerine yazılan hâşiyeler.', ornek=['Hayâlî, Kestelî, İsâmüddîn, Ramazan Efendi hâşiyeleri']),
   dict(ad='Şerhu’l-Mevâkıf halkası', ar='حلقة شرح المواقف', d='Seyyid Şerîf’in şerhi ve hâşiyeleri; en ileri kelâm dersi.', ornek=['Hasan Çelebi, Siyâlkûtî hâşiyeleri']),
   dict(ad='Tecrîd halkası', ar='حلقة التجريد', d='Tûsî’nin metni, Kuşçu’nun şerhi ve Devvânî-Deştekî hâşiyeleri.', ornek=['Şerh-i cedîd', 'Hâşiye-i kadîme ve cedîde']),
   dict(ad='Fıkh-ı ekber ve Tahâviyye şerhleri', ar='شروح الفقه الأكبر والطحاوية', d='Hanefî-Mâtürîdî akide öğretiminin halkası.', ornek=['Aliyyü’l-Kārî', 'Beyâzîzâde, İşârâtü’l-merâm'])]),
  dict(g='Tartışma ve mukayese literatürü', d='Ekoller arası farklar ve felsefe ile tartışmalar.', items=[
   dict(ad='Mâtürîdî–Eş‘arî ihtilâfı risâleleri', ar='رسائل الخلاف بين الأشاعرة والماتريدية', d='İki Sünnî ekol arasındaki farkları (sayıları 12-50 arasında verilir) sayan eserler.', ornek=['Kemalpaşazâde, Risâle fi’l-ihtilâf', 'Ebû Uzbe, er-Ravzatü’l-behiyye', 'Şeyhzâde, Nazmü’l-ferâid']),
   dict(ad='Tehâfüt literatürü', ar='التهافت', d='Kelâmcılarla filozoflar arasındaki tartışma eserleri.', ornek=['Gazzâlî, Tehâfütü’l-felâsife', 'İbn Rüşd, Tehâfütü’t-Tehâfüt', 'Hocazâde ve Alâeddîn et-Tûsî, Tehâfüt']),
   dict(ad='Reddiyeler', ar='الردود', d='Belli bir fırka veya görüşe cevap eserleri.', ornek=['Dârimî, er-Red ale’l-Cehmiyye', 'Bâkıllânî, Nakzu’l-Kur’ân']),
   dict(ad='Makālât ve fırak', ar='المقالات والفرق', d='Mezheplerin görüşlerini kaydeden eserler (ayrıntısı İslâm Mezhepleri Tarihi bölümündedir).', ornek=['Eş‘arî, Makālât', 'Bağdâdî, el-Fark', 'Şehristânî, el-Milel'])]),
  dict(g='Rivayet temelli akîde literatürü', d='Ehl-i hadis çizgisinin âyet, hadis ve selef sözlerini senetleriyle toplayan eserleri.', items=[
   dict(ad='Kitâbü’s-Sünne', ar='كتب السنة', d='Akide konularındaki rivayetleri toplayan eserler.', ornek=['Abdullah b. Ahmed, es-Sünne', 'Hallâl, es-Sünne', 'Lâlekâî, Şerhu usûli i‘tikādi ehli’s-sünne']),
   dict(ad='Kitâbü’t-Tevhîd ve’s-sıfât', ar='كتب التوحيد والصفات', d='Sıfat nasslarını derleyen eserler.', ornek=['İbn Huzeyme, Kitâbü’t-Tevhîd', 'Beyhakī, el-Esmâ ve’s-sıfât']),
   dict(ad='Kitâbü’l-Îmân', ar='كتب الإيمان', d='İmanın tanımı ve artıp eksilmesi tartışması.', ornek=['Ebû Ubeyd, Kitâbü’l-Îmân', 'İbn Teymiyye, Kitâbü’l-Îmân'])]),
  dict(g='Telif üslubuna göre', d='Kelâm bilgisinin farklı okuyuculara göre aldığı biçimler.', items=[
   dict(ad='Nazarî-istidlâlî kelâm', ar='الكلام الاستدلالي', d='Delil ve itiraz-cevap düzeniyle yazılmış ilmî eserler.', ornek=['Mevâkıf', 'Makāsıd']),
   dict(ad='Manzum akāid', ar='العقائد المنظومة', d='Ezber kolaylığı için şiir hâlinde akide.', ornek=['Bed’ü’l-emâlî', 'Nûniyye', 'Cevhere']),
   dict(ad='İlmihal ve halk akāidi', ar='العقائد الشعبية', d='Halka hitap eden sade akide kitapları.', ornek=['Hakîm es-Semerkandî, es-Sevâdü’l-a‘zam', 'Birgivî, Vasiyetnâme', 'Osmanlı Türkçesi akāid risâleleri']),
   dict(ad='Yeni ilm-i kelâm', ar='علم الكلام الجديد', d='Materyalizm, pozitivizm ve modern bilim karşısında inancı savunan eserler.', ornek=['Abduh, Risâletü’t-tevhîd', 'İzmirli, Yeni İlm-i Kelâm', 'Filibeli Ahmed Hilmi, Huzur-ı Akl u Fen'])])],
 tabakat=[
  dict(b='Sıfatların tasnifi: Mâtürîdî ve Eş‘arî', d='Allah’ın sıfatlarının kelâm kitaplarındaki tasnifi; iki ekolün farkı tekvin sıfatındadır.', items=[
   dict(ad='Sıfât-ı nefsiyye', d='Zâtı ifade eden: vücûd.', ornek='—'),
   dict(ad='Sıfât-ı selbiyye (tenzîhiyye)', d='Allah’a yakışmayanı nefyeden: kıdem, bekā, muhâlefetün li’l-havâdis, kıyâm bi-nefsihî, vahdâniyyet.', ornek='—'),
   dict(ad='Sıfât-ı subûtiyye (me‘ânî)', d='Zâta ilave, ezelî sıfatlar: hayat, ilim, irade, kudret, sem‘, basar, kelâm; Mâtürîdîlere göre ayrıca tekvin.', ornek='Eş‘arîlerde yedi, Mâtürîdîlerde sekiz'),
   dict(ad='Sıfât-ı haberiyye', d='Nasslarda geçen yed, vech, istivâ gibi ifadeler; selef tefvîz, halef te’vil yolunu tuttu.', ornek='—'),
   dict(ad='Sıfât-ı fi‘liyye', d='Yaratma, rızık verme, diriltme gibi fiiller; Mâtürîdîlere göre tekvin sıfatına döner ve ezelîdir, Eş‘arîlere göre hâdistir.', ornek='—')]),
  dict(b='Mütekaddimîn ve müteahhirîn (İbn Haldun)', d='İbn Haldun’un Mukaddime’de yaptığı ve kelâm tarihinde en yaygın kabul gören dönemlendirme; dönüm noktası Gazzâlî’dir.', items=[
   dict(ad='Mütekaddimîn yolu', d='Cevher-araz ve cüz’-i lâ yetecezzâ fiziği; “delilin bâtıl olması medlûlün bâtıl olmasını gerektirir” ilkesi; mantığa mesafe.', ornek='Bâkıllânî, Cüveynî (ilk dönemi)'),
   dict(ad='Geçiş: Gazzâlî', d='Mantığın Sünnî ilimlere girişi, filozofların tenkidi, delilin butlanı ilkesinin terki.', ornek='el-Mustasfâ mukaddimesi, Tehâfüt'),
   dict(ad='Müteahhirîn yolu', d='Kelâm ve felsefe problemlerinin iç içe geçmesi, umûr-ı âmme bahsi, İbn Sînâcı kavramlar.', ornek='Râzî, Âmidî, Beyzâvî, Îcî, Teftâzânî'),
   dict(ad='Eleştiri', d='İbn Haldun bu karışmanın talebeyi zorladığını söyler; modern araştırmalar dönüşümü kelâmın “tümel bir metafiziğe” dönüşmesi olarak yorumlar.', ornek='—')]),
  dict(b='Kelâm ekollerinin kuşakları (Sünnî kelâm)', d='Ekollerin kurucudan şârihlere kadar başlıca halkaları.', items=[
   dict(ad='Mâtürîdiyye', d='Mâtürîdî → Hakîm es-Semerkandî → Ebü’l-Yüsr el-Pezdevî → Ebü’l-Muîn en-Nesefî → Ömer en-Nesefî → Nûreddîn es-Sâbûnî → İbnü’l-Hümâm → Beyâzîzâde.', ornek='—'),
   dict(ad='Eş‘ariyye (mütekaddimîn)', d='Eş‘arî → Bâhilî, İbn Mücâhid → Bâkıllânî, İbn Fûrek, İsferâyînî → Bağdâdî → Cüveynî.', ornek='İbn Asâkir, Tebyîn’deki tabakalar'),
   dict(ad='Eş‘ariyye (müteahhirîn)', d='Gazzâlî → Şehristânî → Râzî → Âmidî → Beyzâvî → Îcî → Teftâzânî ve Cürcânî → Devvânî → Senûsî ve Lekānî.', ornek='—')])],
 agac=[
  dict(b='el-Mevâkıf ve şerh-hâşiye halkası', kok=dict(name='el-Mevâkıf fî ilmi’l-kelâm — Adudüddîn el-Îcî (ö. 756/1355)', children=[
   dict(name='Şerhu’l-Mevâkıf — Seyyid Şerîf el-Cürcânî (ö. 816/1413)', children=[
    dict(name='Hâşiye — Hasan Çelebi el-Fenârî (ö. 886/1481)'),
    dict(name='Hâşiye — Abdülhakîm es-Siyâlkûtî (ö. 1067/1657)'),
    dict(name='Hâşiye — Hocazâde, Molla Lütfî ve diğer Osmanlı müderrisleri')]),
   dict(name='Şerh — Şemseddîn el-Kirmânî')])),
  dict(b='Tecrîdü’l-i‘tikād halkası', kok=dict(name='Tecrîdü’l-i‘tikād — Nasîrüddîn-i Tûsî (ö. 672/1274)', children=[
   dict(name='Keşfü’l-murâd — Allâme el-Hillî (ö. 726/1325): İmâmî şerh'),
   dict(name='Teşyîdü’l-kavâid (Şerh-i kadîm) — Şemseddîn el-İsfahânî (ö. 749/1348)', children=[dict(name='Hâşiye — Seyyid Şerîf el-Cürcânî (Hâşiye-i Tecrîd)')]),
   dict(name='Şerh-i cedîd — Ali Kuşçu (ö. 879/1474)', children=[
    dict(name='Hâşiye-i kadîme ve cedîde — Celâleddîn ed-Devvânî (ö. 908/1502)'),
    dict(name='Hâşiyeler — Sadreddîn ed-Deştekî ve Gıyâseddîn Mansûr (Celâlî–Sadrî tartışması)')])])),
  dict(b='el-Fıkhu’l-ekber şerhleri', kok=dict(name='el-Fıkhu’l-ekber — Ebû Hanîfe’ye nispet edilen metin (Hammâd rivayeti)', children=[
   dict(name='Şerh — Ebü’l-Leys es-Semerkandî’ye nispet edilen (Mâtürîdî’ye de nispet edilmiştir)'),
   dict(name='Şerhu’l-Fıkhi’l-ekber — Ebü’l-Müntehâ el-Mağnisâvî (ö. 1000/1592 civarı)'),
   dict(name='Minehu’r-ravzi’l-ezher — Aliyyü’l-Kārî (ö. 1014/1606)'),
   dict(name='İşârâtü’l-merâm min ibârâti’l-İmâm — Beyâzîzâde Ahmed Efendi (ö. 1098/1687): Ebû Hanîfe’nin beş risâlesini birlikte şerh eder')]))],
)

TERIM = [
 dict(g='Varlık ve âlem (dakīku’l-kelâm)', items=[
  T('الجوهر الفرد', 'Cevher-i ferd', 'Bölünemeyen en küçük parça (cüz’-i lâ yetecezzâ); mütekaddimîn kelâm fiziğinin temeli.'),
  T('العرض', 'Araz', 'Cevherde bulunan, kendi başına var olamayan nitelik; iki anda bekā etmez.'),
  T('الحدوث', 'Hudûs', 'Sonradan var olma; âlemin hâdis oluşu Allah’ın varlığının temel delilidir.'),
  T('القدم', 'Kıdem', 'Başlangıcı olmama; yalnız Allah’a ve sıfatlarına aittir.'),
  T('الأمور العامة', 'Umûr-ı âmme', 'Vücûd, vücûb, imkân, birlik-çokluk, illet-ma‘lûl gibi bütün varlıklara ait genel hükümler.'),
  T('واجب الوجود', 'Vâcibü’l-vücûd', 'Varlığı zorunlu olan; Allah.'),
  T('ممكن الوجود', 'Mümkinü’l-vücûd', 'Varlığı ve yokluğu eşit olan; âlem.'),
  T('التسلسل والدور', 'Teselsül ve devir', 'Sonsuz sebepler zinciri ve kısır döngü; ikisi de muhal kabul edilir.')]),
 dict(g='Sıfatlar ve fiiller', items=[
  T('التكوين', 'Tekvin', 'Mâtürîdîlere göre yaratma, rızık verme gibi fiillerin kaynağı olan ezelî sıfat.'),
  T('الكلام النفسي', 'Kelâm-ı nefsî', 'Allah’ın zâtıyla kâim, harf ve sesten münezzeh ezelî kelâm sıfatı.'),
  T('الكسب', 'Kesb', 'Eş‘arîlere göre kulun, Allah’ın yarattığı fiile kudretiyle sahip olması.'),
  T('الإرادة الجزئية', 'İrâde-i cüz’iyye', 'Kulun fiillerde tercih gücü; Mâtürîdî sorumluluk anlayışının merkezi.'),
  T('الحسن والقبح', 'Hüsün ve kubuh', 'İyilik ve kötülüğün akılla bilinip bilinemeyeceği tartışması.'),
  T('التفويض والتأويل', 'Tefvîz ve te’vil', 'Haberî sıfatların anlamını Allah’a bırakma ve uygun bir anlamla yorumlama.'),
  T('الرؤية', 'Rü’yetullah', 'Mü’minlerin âhirette Allah’ı görmesi; Ehl-i sünnet kabul, Mu‘tezile red eder.')]),
 dict(g='Nübüvvet ve sem‘iyyât', items=[
  T('المعجزة', 'Mu‘cize', 'Peygamberlik iddiasındaki kişinin elinde, meydan okuma ile birlikte görülen olağanüstü hâl.'),
  T('الإرهاص', 'İrhâs', 'Peygamberlikten önce görülen olağanüstü hâller.'),
  T('الكرامة', 'Kerâmet', 'Velînin elinde görülen olağanüstü hâl.'),
  T('العصمة', 'İsmet', 'Peygamberlerin günahtan korunmuşluğu.'),
  T('الشفاعة', 'Şefaat', 'Âhirette peygamber ve salihlerin Allah’ın izniyle aracılığı.'),
  T('السمعيات', 'Sem‘iyyât', 'Yalnız nakille bilinebilen inanç konuları.')]),
]

DONEMLER = [dict(ad=t['ad'], aralik=t.get('aralik', ''), d=t['d']) for t in []]  # eski dönemler korunur

OLAY = [
 dict(t='80/699', kim='Ma‘bed el-Cühenî', ne='Kader tartışmasının ilk açık savunucusu.', neden='Kaderiyye’nin doğuşu; İbn Ömer’in tepkisi Cibrîl hadisinin rivayet sebebidir.'),
 dict(t='218/833', kim='Halife Me’mûn', ne='Mihne başladı: Kur’an’ın mahlûk olduğunu kabul etme dayatması.', neden='Mu‘tezile devlet desteği kazandı; Ahmed b. Hanbel direnişin simgesi oldu.'),
 dict(t='234/848', kim='Halife Mütevekkil', ne='Mihneye son verildi.', neden='Ehl-i hadis yeniden güç kazandı.'),
 dict(t='300/912 civarı', kim='Ebü’l-Hasan el-Eş‘arî', ne='Mu‘tezile’den ayrıldığını Basra’da ilan etti.', neden='Sünnî kelâmın Irak kolu doğdu.'),
 dict(t='333/944', kim='Ebû Mansûr el-Mâtürîdî', ne='Semerkant’ta vefat etti; Kitâbü’t-Tevhîd.', neden='Sünnî kelâmın Mâverâünnehir kolu kuruldu.'),
 dict(t='488/1095', kim='Gazzâlî', ne='Tehâfütü’l-felâsife yazıldı (yaklaşık bu yıllar).', neden='Kelâm ile felsefe tartışması yeni bir evreye girdi.'),
 dict(t='580/1184 civarı', kim='İbn Rüşd', ne='Tehâfütü’t-Tehâfüt.', neden='Gazzâlî’ye filozof cevabı.'),
 dict(t='672/1274', kim='Nasîrüddîn-i Tûsî', ne='Tecrîdü’l-i‘tikād.', neden='Felsefî kelâmın Sünnî-Şiî ortak ders metni.'),
 dict(t='756/1355', kim='Adudüddîn el-Îcî', ne='el-Mevâkıf.', neden='Müteahhirîn kelâmının standart planı.'),
 dict(t='880/1475 civarı', kim='Fâtih Sultan Mehmed', ne='Hocazâde ile Alâeddîn et-Tûsî’ye Tehâfüt yazdırdı.', neden='Osmanlı’da kelâm-felsefe tartışması kurumsallaştı.'),
 dict(t='1339/1921', kim='İzmirli İsmâil Hakkı', ne='Yeni İlm-i Kelâm.', neden='Modern sorulara cevap arayan kelâm projesi.'),
]

METIN = [
 M('Nesefî: Bilginin kaynakları', 'el-Akāidü’n-Nesefiyye’nin girişindeki bu ilke, kelâmın bilgi teorisinin özeti sayılır.', 'وأسباب العلم للخلق ثلاثة: الحواس السليمة، والخبر الصادق، والعقل', 'النسفي، العقائد النسفية'),
 M('Nesefî: Âlemin hudûsu', 'Akāid metninin âlem tanımı; kelâmın hudûs delilinin çıkış noktası.', 'والعالم بجميع أجزائه محدث، إذ هو أعيان وأعراض', 'النسفي، العقائد النسفية'),
]

KUT = [
 B('Kelâm tarihi', 'İslâm Düşüncesinin Teşekkül Devri', 'The Formative Period of Islamic Thought', 'W. Montgomery Watt (trc. E. R. Fığlalı)', '1973', 'İlk dönem kelâm tartışmalarının tarihî bağlamı.'),
 B('Kelâm tarihi', 'Kelâm Tarihi', 'تاريخ علم الكلام', 'Şerafeddin Gölcük – Süleyman Toprak', 'XX. yy', 'Türkiye’de kelâm tarihinin ders kitabı.'),
 B('Kelâm tarihi', 'İslâm Düşünce Atlası', 'أطلس الفكر الإسلامي', 'İbrahim Halil Üçer (ed.)', '2023', 'Klasik, yenilenme, muhasebe ve arayışlar dönemlerine göre kelâm ve diğer ilimler.'),
 B('Akide metni', 'el-Akīdetü’t-Tahâviyye', 'العقيدة الطحاوية', 'Ebû Ca‘fer et-Tahâvî', '321/933', 'Bütün Sünnî ekollerce kabul gören akide metni.'),
 B('Akide metni', 'Bed’ü’l-emâlî', 'بدء الأمالي', 'Sirâceddîn el-Ûşî', '575/1179', 'Mâtürîdî akide manzumesi.'),
 B('Akide metni', 'Ümmü’l-berâhîn', 'أم البراهين', 'Muhammed b. Yûsuf es-Senûsî', '895/1490', 'Eş‘arî akide metni.'),
 B('Akide metni', 'Cevheretü’t-tevhîd', 'جوهرة التوحيد', 'İbrâhîm el-Lekānî', '1041/1631', 'Ezher’in akide manzumesi.'),
 B('Akide metni', 'el-Kasîdetü’n-Nûniyye', 'القصيدة النونية', 'Hızır Bey', '863/1459', 'Osmanlı akide manzumesi.'),
 B('Kapsamlı eser', 'Tebsıratü’l-edille', 'تبصرة الأدلة', 'Ebü’l-Muîn en-Nesefî', '508/1115', 'Mâtürîdî kelâmının en kapsamlı klasiği.'),
 B('Kapsamlı eser', 'el-İrşâd', 'الإرشاد', 'İmâmü’l-Haremeyn el-Cüveynî', '478/1085', 'Mütekaddimîn Eş‘arî kelâmının ders kitabı.'),
 B('Kapsamlı eser', 'el-Muhassal', 'محصل أفكار المتقدمين والمتأخرين', 'Fahreddîn er-Râzî', '606/1210', 'Felsefî kelâmın kurucu metni.'),
 B('Kapsamlı eser', 'Tavâliu’l-envâr', 'طوالع الأنوار', 'Kādî Beyzâvî', '685/1286', 'Yoğun müteahhirîn metni; İsfahânî şerhiyle okunur.'),
 B('Kapsamlı eser', 'el-Müsâyere', 'المسايرة', 'Kemâleddîn İbnü’l-Hümâm', '861/1457', 'Mâtürîdî ve Eş‘arî görüşleri karşılaştıran eser.'),
 B('Şerh', 'Şerhu’l-Mevâkıf', 'شرح المواقف', 'Seyyid Şerîf el-Cürcânî', '816/1413', 'Osmanlı’nın en ileri kelâm kitabı.'),
 B('Şerh', 'Şerhu Tecrîdi’l-i‘tikād', 'شرح تجريد الاعتقاد', 'Ali Kuşçu', '879/1474', 'Felsefî kelâmın Osmanlı’daki ana metinlerinden.'),
 B('Şerh', 'Minehu’r-ravzi’l-ezher fî şerhi’l-Fıkhi’l-ekber', 'منح الروض الأزهر', 'Aliyyü’l-Kārî', '1014/1606', 'Fıkh-ı ekber’in en yaygın şerhi.'),
 B('Mukayese', 'er-Ravzatü’l-behiyye', 'الروضة البهية', 'Ebû Uzbe', '1172/1759', 'Eş‘arî–Mâtürîdî farkları.'),
 B('Mukayese', 'Nazmü’l-ferâid ve cem‘u’l-fevâid', 'نظم الفرائد', 'Şeyhzâde Abdurrahîm', '1133/1721 civarı', 'İki Sünnî ekol arasındaki kırk küsur meselenin incelemesi.'),
 B('Felsefe tartışması', 'Tehâfütü’l-felâsife', 'تهافت الفلاسفة', 'Gazzâlî', '505/1111', 'Filozofların yirmi meselesinin eleştirisi.'),
 B('Felsefe tartışması', 'Tehâfütü’t-Tehâfüt', 'تهافت التهافت', 'İbn Rüşd', '595/1198', 'Gazzâlî’ye cevap.'),
 B('Felsefe tartışması', 'Tehâfütü’l-felâsife', 'تهافت الفلاسفة', 'Hocazâde Muslihuddîn', '893/1488', 'Fâtih’in isteğiyle yazılan hakem eser.'),
 B('Rivayet temelli', 'Şerhu usûli i‘tikādi ehli’s-sünne', 'شرح أصول اعتقاد أهل السنة', 'Lâlekâî', '418/1027', 'Selef akidesine dair rivayet derlemesi.'),
 B('Rivayet temelli', 'el-Esmâ ve’s-sıfât', 'الأسماء والصفات', 'Beyhakī', '458/1066', 'Sıfat nasslarının Eş‘arî bakışla derlemesi.'),
 B('Modern', 'Risâletü’t-tevhîd', 'رسالة التوحيد', 'Muhammed Abduh', '1905', 'Modern dönemin kısa akide klasiği.'),
 B('Modern Türkçe', 'Kelâm İlmi: Giriş', 'مدخل إلى علم الكلام', 'Bekir Topaloğlu', 'XX. yy', 'Türkiye’de kelâmın ders kitabı.'),
 B('Modern Türkçe', 'İslâm İnançları', 'العقائد الإسلامية', 'İlyas Çelebi (ed.)', 'XXI. yy', 'İlahiyat fakültelerinin güncel akaid ders kitabı.'),
]

# ───────────────────────── USÛL-İ KELÂM ─────────────────────────
USUL = dict(
 AD='Usûl-i Kelâm',
 KISA='Kelâmın yöntemi: bilginin kaynakları, delil türleri, akıl ile naklin ilişkisi, istidlâl yolları ve münazara âdâbı; ayrıca itikadî ekollerin yöntem farkları.',
 DONEM={
  'ilk': 'Cedel ve ilk yöntem tartışmaları (II–III/VIII–IX. yy)',
  'kurulus': 'Sünnî kelâm yönteminin kuruluşu (IV–V/X–XI. yy)',
  'mantik': 'Mantığın kelâma girişi ve felsefî yöntem (V–VIII/XI–XIV. yy)',
  'adab': 'Âdâb-ı bahs ve Osmanlı yöntem literatürü (VIII–XIII/XIV–XIX. yy)',
  'modern': 'Modern dönem (XX. yy–)'},
 DONEM_ATA={'İbn Küllâb': 'ilk', 'Ebû Nasr el-İyâzî': 'kurulus', 'Abdülkāhir el-Bağdâdî': 'kurulus', 'Şehristânî': 'mantik', 'Taşköprizâde Ahmed Efendi': 'adab', 'Ebû Uzbe': 'adab'},
 KISILER=[
  P('Ebû Mansûr el-Mâtürîdî (usûl)', 'أبو منصور الماتريدي', '333/944', 'kurulus', 'Mâtürîdî', 'Kitâbü’t-Tevhîd’in girişinde bilginin üç yolunu (duyular/ıyân, haber, nazar) ve taklidin bilgi değeri olmadığını temellendirir. Akıl ve vahyi birbirini tamamlayan iki kaynak olarak görmesi, Mâtürîdî yönteminin ayırt edici özelliğidir.', ['Kitâbü’t-Tevhîd (bilgi bahsi)']),
  P('Kādî Ebû Bekir el-Bâkıllânî (usûl)', 'أبو بكر الباقلاني', '403/1013', 'kurulus', 'Eş‘arî', 'et-Temhîd ve el-İnsâf’ın giriş bölümlerinde bilginin tanımı, kısımları ve nazarın şartlarını sistemleştirdi. “Delilin bâtıl olması medlûlün bâtıl olmasını gerektirir” ilkesi ona nispet edilir; bu ilke mütekaddimîn kelâmının yöntem özelliği sayılmıştır.', ['et-Temhîd', 'el-İnsâf', 'et-Takrîb ve’l-irşâd']),
  P('Kādî Abdülcebbâr (yöntem)', 'القاضي عبد الجبار', '415/1025', 'kurulus', 'Mu‘tezile', 'el-Muğnî’nin “en-Nazar ve’l-maârif” cildinde Mu‘tezile’nin bilgi teorisini ve “mükellefin ilk vâcibi nazardır” görüşünü ayrıntılı işledi. Aklın, şer‘den önce de iyi ve kötüyü bilebileceğini savunur.', ['el-Muğnî (XII. cilt: en-Nazar ve’l-maârif)', 'Şerhu’l-Usûli’l-hamse']),
  P('İmâmü’l-Haremeyn el-Cüveynî (cedel)', 'إمام الحرمين الجويني', '478/1085', 'kurulus', 'Eş‘arî', 'el-Kâfiye fi’l-cedel’de münazara ve cedel ilminin kurallarını sistemleştirdi. el-İrşâd’da delilleri aklî ve sem‘î olarak ayırıp kelâm meselelerini delil türlerine göre sınıflandırdı; son dönem eseri en-Nizâmiyye’de selefin tefvîz yoluna yakınlaştı.', ['el-Kâfiye fi’l-cedel', 'el-İrşâd', 'el-Akīdetü’n-Nizâmiyye']),
  P('İmam Gazzâlî (yöntem)', 'أبو حامد الغزالي', '505/1111', 'mantik', 'Eş‘arî', 'Mi‘yârü’l-ilm, Mihakkü’n-nazar ve el-Kıstâsü’l-müstakîm ile Aristo mantığını Sünnî ilimlerin yöntemi hâline getirdi. Kānûnü’t-te’vîl’de akıl ile naklin çatıştığı durumlar için ilkeler koydu.', ['Mi‘yârü’l-ilm', 'Mihakkü’n-nazar', 'el-Kıstâsü’l-müstakîm', 'Kānûnü’t-te’vîl']),
  P('İbn Rüşd (yöntem)', 'ابن رشد', '595/1198', 'mantik', 'felsefe', 'Kurtubalı filozof, fakih ve kadı. Faslü’l-makāl’de felsefe ile şeriatın uyumunu savunup insanları burhan, cedel ve hitabet ehli olarak üçe ayırdı; el-Keşf an menâhici’l-edille’de kelâmcıların delillerini eleştirdi.', ['Faslü’l-makāl', 'el-Keşf an menâhici’l-edille', 'Tehâfütü’t-Tehâfüt']),
  P('Fahreddîn er-Râzî (kānûn-ı küllî)', 'فخر الدين الرازي', '606/1210', 'mantik', 'Eş‘arî', 'Esâsü’t-takdîs’te akıl ile naklin çatıştığı durumlar için “kānûn-ı küllî”yi formüle etti: akıl naklin temeli olduğundan, kesin aklî delil karşısında nakil te’vil edilir veya anlamı Allah’a bırakılır. Bu ilke sonraki tartışmaların merkezinde yer aldı.', ['Esâsü’t-takdîs', 'el-Muhassal', 'el-Metâlibü’l-âliye']),
  P('İbn Teymiyye (akıl-nakil)', 'ابن تيمية', '728/1328', 'mantik', 'Ehl-i hadis/Selefî', 'Der’ü teâruzi’l-akl ve’n-nakl’de Râzî’nin kānûn-ı küllîsini eleştirerek sahih nakil ile sarih aklın çatışamayacağını savundu. er-Red ale’l-mantıkıyyîn’de Aristo mantığını tenkit etti.', ['Der’ü teâruzi’l-akl ve’n-nakl', 'er-Red ale’l-mantıkıyyîn']),
  P('Şemseddîn es-Semerkandî', 'شمس الدين السمرقندي', 'VII/XIII. yy sonu', 'adab', 'kelâmcı, mantıkçı', 'Semerkantlı kelâmcı, mantıkçı ve matematikçi. er-Risâle fî âdâbi’l-bahs ile münazara ilmini cedelden ayırıp mantıkî temelde müstakil bir disiplin olarak kurdu; eser Osmanlı medreselerinde şerhleriyle okutuldu. es-Sahâifü’l-ilâhiyye kelâm eseridir.', ['Risâle fî âdâbi’l-bahs', 'es-Sahâifü’l-ilâhiyye', 'Kıstâsü’l-efkâr']),
  P('Adudüddîn el-Îcî (âdâb)', 'عضد الدين الإيجي', '756/1355', 'adab', 'Eş‘arî', 'el-Mevâkıf’ın birinci mevkıfında bilgi ve nazar konusunu müteahhirîn düzeniyle işledi. er-Risâletü’l-Adudiyye fî âdâbi’l-bahs, kısa münazara metni olarak çok sayıda şerhe konu oldu.', ['el-Mevâkıf (I. mevkıf)', 'Risâle fî âdâbi’l-bahs (Adudiyye)']),
  P('İsmâil Gelenbevî (âdâb)', 'إسماعيل الكلنبوي', '1205/1791', 'adab', 'Osmanlı', 'Mantık, kelâm ve matematikte Osmanlı’nın son büyük müderrislerindendir. Risâletü’l-âdâb, münazara ilminin Osmanlı medreselerinde en çok okunan metinlerinden oldu; el-Burhân fî ilmi’l-mîzân mantık kitabı da yaygındır.', ['Risâletü’l-âdâb', 'el-Burhân', 'Hâşiye ale’l-Celâl']),
  P('İzmirli İsmâil Hakkı', 'إزميرلي إسماعيل حقي', '1946', 'modern', 'Yeni ilm-i kelâm', 'Osmanlı-Cumhuriyet geçiş döneminin âlimi. Yeni İlm-i Kelâm’da kelâmın yöntemini modern felsefe ve bilimin sorularına göre yenilemeyi önerdi; İslâm’da Felsefe Cereyanları ve Muhassal-ı Kelâm ve Hikmet de onundur.', ['Yeni İlm-i Kelâm', 'Muhassal-ı Kelâm ve Hikmet']),
 ],
 TASNIF=dict(
  tesekkul=[
   dict(ad='Kur’an’ın istidlâl üslubu', aralik='I/VII. yy', d='Kur’an, Allah’ın varlık ve birliğini, öldükten sonra dirilişi aklî delillerle (temânu‘, ilk yaratılış, nizam) anlatır; kelâm yönteminin ilk kaynağı bu üsluptur.', eserler=['Enbiyâ 21/22 (temânu‘)', 'Yâsîn 36/78-79 (ilk yaratılış)']),
   dict(ad='Cedel ve ilk tartışmalar', aralik='II–III/VIII–IX. yy', d='Kader, iman ve sıfat tartışmalarında karşı tarafı ilzam etmeye dayalı cedel yöntemi gelişti; Mu‘tezile aklın önceliğini ve “ilk vâcib nazardır” ilkesini öne çıkardı.', eserler=['Mu‘tezile’nin usûl-i hamse risâleleri', 'İbn Küllâb’ın eserleri (kayıp)']),
   dict(ad='Sünnî yöntemin kuruluşu', aralik='IV/X. yy', d='Mâtürîdî bilginin üç yolunu, Eş‘arî ve talebeleri nazarın meşruiyetini temellendirdi; Eş‘arî’nin İstihsânü’l-havz’ı kelâmla uğraşmayı savunur.', eserler=['Mâtürîdî, Kitâbü’t-Tevhîd', 'Eş‘arî, İstihsânü’l-havz fî ilmi’l-kelâm']),
   dict(ad='Mütekaddimîn mukaddimeleri', aralik='V/XI. yy', d='Bâkıllânî, Bağdâdî ve Cüveynî kelâm kitaplarını bilgi ve nazar bahisleriyle açtı; cevher-araz fiziği yöntemin parçası oldu.', eserler=['Bâkıllânî, et-Temhîd', 'Bağdâdî, Usûlü’d-dîn', 'Cüveynî, el-İrşâd ve el-Kâfiye fi’l-cedel']),
   dict(ad='Mantığın girişi', aralik='V–VI/XI–XII. yy', d='Gazzâlî mantığı “bütün ilimlerin mukaddimesi” sayarak Sünnî ilimlere taşıdı; delilin butlanı ilkesi terk edildi.', eserler=['Gazzâlî, Mi‘yârü’l-ilm ve Mihakkü’n-nazar']),
   dict(ad='Akıl-nakil teorisi', aralik='VI–VIII/XII–XIV. yy', d='Râzî’nin kānûn-ı küllîsi, İbn Rüşd’ün uzlaştırma teorisi ve İbn Teymiyye’nin eleştirisi akıl-nakil ilişkisinin üç büyük modelini oluşturdu.', eserler=['Râzî, Esâsü’t-takdîs', 'İbn Rüşd, Faslü’l-makāl', 'İbn Teymiyye, Der’ü teâruz']),
   dict(ad='Âdâb-ı bahs', aralik='VII–XII/XIII–XVIII. yy', d='Semerkandî münazarayı mantık temelli müstakil bir ilim yaptı; Îcî’nin Adudiyye’si, Taşköprizâde, Saçaklızâde ve Gelenbevî’nin eserleriyle medrese müfredatına girdi.', eserler=['Semerkandî, Âdâbü’l-bahs', 'Îcî, Adudiyye', 'Taşköprizâde, Şerhu’l-Adudiyye', 'Saçaklızâde, Takrîrü’l-kavânîn ve el-Velediyye', 'Gelenbevî, Risâletü’l-âdâb']),
   dict(ad='Modern dönem', aralik='XX. yy – günümüz', d='Yeni ilm-i kelâm projeleri, din felsefesi ile kesişim ve yöntem tartışmaları.', eserler=['İzmirli, Yeni İlm-i Kelâm', 'Topaloğlu, Kelâm İlmi: Giriş'])],
  tasnif=[
   dict(g='Bilginin kaynakları (esbâbü’l-ilm)', d='Nesefî’nin Akāid’inde özetlenen ve Sünnî kelâmda yerleşen tasnif.', items=[
    dict(ad='Havâss-ı selîme', ar='الحواس السليمة', d='Sağlam beş duyu; duyulur âlem hakkında kesin bilgi verir.', ornek=['İşitme, görme, koklama, tatma, dokunma']),
    dict(ad='Haber-i sâdık', ar='الخبر الصادق', d='Doğru haber: mütevâtir haber ile peygamber haberi; ikisi de kesin bilgi verir.', ornek=['Mütevâtir haber', 'Resul haberi (mu‘cize ile teyit edilmiş)']),
    dict(ad='Akıl', ar='العقل', d='Bedîhî (zorunlu) ve istidlâlî (nazarî) bilgi kaynağı.', ornek=['“Bütün parçadan büyüktür” (bedîhî)', 'Âlemin hâdis oluşu (istidlâlî)']),
    dict(ad='İlham', ar='الإلهام', d='Ehl-i sünnete göre ilham, sahibini bağlasa da başkası için bilgi kaynağı değildir.', ornek=['Nesefî’nin “ilham, Ehl-i hak katında bilgi sebebi değildir” ifadesi'])]),
   dict(g='Delil türleri', d='Kelâm kitaplarının delil tasnifi.', items=[
    dict(ad='Aklî delil', ar='الدليل العقلي', d='Tamamen akıl öncüllerinden oluşan delil.', ornek=['Hudûs delili']),
    dict(ad='Naklî (sem‘î) delil', ar='الدليل النقلي', d='Kitap ve sünnete dayanan delil; sem‘iyyât konularında esastır.', ornek=['Âhiret hâlleri']),
    dict(ad='Mürekkep delil', ar='الدليل المركب', d='Akıl ve nakil öncüllerinin birlikte kullanıldığı delil.', ornek=['—']),
    dict(ad='Kat‘î ve zannî delil', ar='القطعي والظني', d='Akāidde kesin bilgi aranır; âhâd haber tek başına akide ispatında tartışmalıdır.', ornek=['—'])]),
   dict(g='İstidlâl yolları ve meşhur deliller', d='Kelâmcıların başlıca akıl yürütme kalıpları.', items=[
    dict(ad='Hudûs delili', ar='دليل الحدوث', d='Âlem araz taşır, arazlar hâdistir, hâdisten ayrılmayan da hâdistir; hâdisin de bir muhdisi vardır.', ornek=['Mütekaddimîn’in temel delili']),
    dict(ad='İmkân (vücûb) delili', ar='دليل الإمكان', d='Mümkün varlıklar zincirinin varlığı zorunlu bir varlığa dayanması gerekir; İbn Sînâ’dan alınıp müteahhirîn kelâmında yaygınlaştı.', ornek=['—']),
    dict(ad='Temânu‘ delili', ar='دليل التمانع', d='İki ilah olsaydı iradeleri çatışır, âlem düzen bulmazdı (Enbiyâ 21/22).', ornek=['—']),
    dict(ad='Nizam ve inâyet delili', ar='دليل النظام والعناية', d='Âlemdeki düzen ve amaçlılık bir hikmet sahibine delildir.', ornek=['—']),
    dict(ad='Kıyâsü’l-ğāib ale’ş-şâhid', ar='قياس الغائب على الشاهد', d='Görülenden görülmeyene akıl yürütme; sınırları tartışılmıştır.', ornek=['—']),
    dict(ad='Sebr ve taksîm, ilzâm', ar='السبر والتقسيم والإلزام', d='İhtimalleri sayıp eleme ve hasmı kendi önermesiyle bağlama.', ornek=['—'])]),
   dict(g='Hükm-i aklî', d='Akla göre bir şeyin üç durumu; özellikle Senûsî ve Eş‘arî metinlerinin giriş konusu.', items=[
    dict(ad='Vâcib', ar='الواجب', d='Yokluğu düşünülemeyen.', ornek=['Allah’ın varlığı']),
    dict(ad='Câiz (mümkin)', ar='الجائز', d='Varlığı ve yokluğu düşünülebilen.', ornek=['Âlemin varlığı']),
    dict(ad='Müstahîl', ar='المستحيل', d='Varlığı düşünülemeyen.', ornek=['Ortak ilah'])]),
   dict(g='Akıl-nakil ilişkisi modelleri', d='Akıl ile naklin çatıştığı görüldüğünde ne yapılacağına dair başlıca yaklaşımlar.', items=[
    dict(ad='Mu‘tezile: aklın önceliği', ar='تقديم العقل', d='Akıl şer‘den önce iyi ve kötüyü bilir; nakil aklın bildiğini teyit eder.', ornek=['Kādî Abdülcebbâr']),
    dict(ad='Mâtürîdî denge', ar='التوازن الماتريدي', d='Akıl ve vahiy birbirini tamamlar; akıl Allah’ı bilmeyi gerektirir, hükümler vahiyle kesinleşir.', ornek=['Mâtürîdî', 'Ebü’l-Muîn en-Nesefî']),
    dict(ad='Eş‘arî kānûn-ı küllî', ar='القانون الكلي', d='Kesin aklî delil karşısında nakil te’vil edilir veya tefvîz yapılır.', ornek=['Râzî, Esâsü’t-takdîs']),
    dict(ad='Uzlaştırma (filozof yaklaşımı)', ar='التوفيق', d='Hakikat hakikate zıt olmaz; zâhir burhana aykırıysa te’vil edilir.', ornek=['İbn Rüşd, Faslü’l-makāl']),
    dict(ad='Sahih nakil – sarih akıl uyumu', ar='موافقة صحيح المنقول لصريح المعقول', d='Gerçek bir çatışma olamaz; çatışma görünüyorsa ya nakil sahih değil ya akıl sarih değildir.', ornek=['İbn Teymiyye, Der’ü teâruz'])]),
   dict(g='Âdâb-ı bahs (münazara) kavramları', d='Tartışmada iki tarafın görev ve hamlelerini düzenleyen ilim.', items=[
    dict(ad='Müddeî ve sâil', ar='المدعي والسائل', d='İddiada bulunan (mu‘allil) ile ona itiraz eden.', ornek=['—']),
    dict(ad='Men‘ (mukāyese)', ar='المنع', d='Delilin bir öncülünü kabul etmeme.', ornek=['—']),
    dict(ad='Nakz', ar='النقض', d='Delilin, hükmün bulunmadığı bir yerde de bulunduğunu göstererek bozulması.', ornek=['—']),
    dict(ad='Muâraza', ar='المعارضة', d='Karşı iddiayı başka bir delille ispat etme.', ornek=['—']),
    dict(ad='Tahrîr-i mahall-i nizâ‘', ar='تحرير محل النزاع', d='Tartışılan noktayı netleştirme; münazaranın ilk adımı.', ornek=['—'])])],
  ekoller=[
   dict(ad='Mu‘tezilî yöntem', ar='منهج المعتزلة', aralik='II–VI/VIII–XII. yy', d='Aklın önceliği, hüsün-kubhun aklîliği, müteşâbihlerin akla göre te’vili.', temsilci=['Ebü’l-Hüzeyl', 'Nazzâm', 'Cübbâîler', 'Kādî Abdülcebbâr']),
   dict(ad='Mâtürîdî yöntem', ar='منهج الماتريدية', aralik='IV/X. yy –', d='Akıl ve vahyin dengesi, hikmet merkezli fiil anlayışı, bilginin üç yolu.', temsilci=['Mâtürîdî', 'Ebü’l-Muîn en-Nesefî', 'Ömer en-Nesefî']),
   dict(ad='Mütekaddimîn Eş‘arî yöntemi', ar='منهج المتقدمين', aralik='IV–V/X–XI. yy', d='Cevher-araz fiziği, hudûs delili, delilin butlanı ilkesi.', temsilci=['Eş‘arî', 'Bâkıllânî', 'Cüveynî']),
   dict(ad='Müteahhirîn (felsefî) yöntem', ar='منهج المتأخرين', aralik='V/XI. yy –', d='Mantık ve felsefe kavramlarıyla iç içe kelâm; imkân delili, umûr-ı âmme.', temsilci=['Gazzâlî', 'Râzî', 'Âmidî', 'Îcî', 'Teftâzânî']),
   dict(ad='Eserî (Ehl-i hadis) yöntem', ar='المنهج الأثري', aralik='II/VIII. yy –', d='Akide konularında nassları esas alma, kelâm cedeline mesafe, sıfatlarda te’vilin reddi.', temsilci=['Ahmed b. Hanbel', 'Dârimî', 'İbn Huzeyme', 'İbn Teymiyye'])],
  tabakat=[
   dict(b='Münazaranın aşamaları (âdâb-ı bahs)', d='Osmanlı âdâb metinlerinde (Adudiyye, Velediyye, Gelenbevî) yer alan tartışma düzeni.', items=[
    dict(ad='1. Tahrîr-i mahall-i nizâ‘', d='Tartışılan meselenin ve terimlerin netleştirilmesi.', ornek='—'),
    dict(ad='2. İddia ve delil (ta‘lîl)', d='Müddeînin iddiasını delille ortaya koyması.', ornek='—'),
    dict(ad='3. İtiraz: men‘, nakz veya muâraza', d='Sâilin delile yönelik üç itiraz yolu.', ornek='—'),
    dict(ad='4. Cevap ve ilzâm', d='Müddeînin itirazı gidermesi; sonuçta ya ilzâm ya ifhâm (susturma) gerçekleşir.', ornek='—')])],
  agac=[dict(b='Âdâb-ı bahs literatürü', kok=dict(name='er-Risâle fî âdâbi’l-bahs — Şemseddîn es-Semerkandî (VII/XIII. yy)', children=[
   dict(name='Şerh — Kutbüddîn el-Kîlânî; Mes‘ûd er-Rûmî (Osmanlı’da okunan şerhler)'),
   dict(name='er-Risâletü’l-Adudiyye — Adudüddîn el-Îcî (ö. 756/1355)', children=[
    dict(name='Şerh — Taşköprizâde Ahmed Efendi (ö. 968/1561)'),
    dict(name='Şerh — Hanefî et-Tebrîzî')]),
   dict(name='Takrîrü’l-kavânîn ve Risâletü’l-Velediyye — Saçaklızâde (ö. 1145/1732)', children=[dict(name='Velediyye şerhleri (Osmanlı medreselerinin münazara dersi)')]),
   dict(name='Risâletü’l-âdâb — İsmâil Gelenbevî (ö. 1205/1791)')]))]),
 TERIM=[dict(g='Bilgi ve yöntem', items=[
  T('النظر', 'Nazar', 'Bilinenlerden bilinmeyene ulaşmak için akıl yürütme.'),
  T('الضروري والنظري', 'Zarûrî ve nazarî bilgi', 'Akıl yürütmeye ihtiyaç duymayan ve duyan bilgi.'),
  T('التقليد', 'Taklit', 'Delilini bilmeden başkasının görüşünü kabul; akāidde tartışılmıştır.'),
  T('أول الواجبات', 'Evvelü’l-vâcibât', 'Mükellefin ilk vazifesi: nazar mı, marifet mi, ikrar mı tartışması.'),
  T('بطلان الدليل يستلزم بطلان المدلول', 'Delilin butlanı ilkesi', 'Mütekaddimîn’e nispet edilen, delil bâtılsa iddianın da bâtıl olacağı ilkesi.'),
  T('القانون الكلي', 'Kānûn-ı küllî', 'Râzî’nin akıl-nakil çatışmasına dair kuralı.'),
  T('آداب البحث والمناظرة', 'Âdâbü’l-bahs ve’l-münâzara', 'Tartışma usulü ilmi.'),
  T('المنع والنقض والمعارضة', 'Men‘, nakz, muâraza', 'Münazarada delile itirazın üç yolu.'),
  T('الإلزام والإفحام', 'İlzâm ve ifhâm', 'Hasmı kendi önermesiyle bağlama ve susturma.')])],
 OLAY=[
  dict(t='300/912 civarı', kim='Ebü’l-Hasan el-Eş‘arî', ne='İstihsânü’l-havz fî ilmi’l-kelâm.', neden='Kelâmla uğraşmanın meşruiyeti savunuldu.'),
  dict(t='403/1013', kim='Bâkıllânî', ne='et-Temhîd’in bilgi ve nazar mukaddimesi.', neden='Sünnî kelâmın yöntem bahisleri sistemleşti.'),
  dict(t='478/1085', kim='Cüveynî', ne='el-Kâfiye fi’l-cedel.', neden='Cedel ilminin kelâmcı sistemi.'),
  dict(t='505/1111', kim='Gazzâlî', ne='Mi‘yârü’l-ilm ve Mihakkü’n-nazar.', neden='Mantık Sünnî ilimlerin yöntemi oldu.'),
  dict(t='595/1198', kim='İbn Rüşd', ne='Faslü’l-makāl ve el-Keşf an menâhici’l-edille.', neden='Felsefe–şeriat ilişkisinin filozofça teorisi.'),
  dict(t='606/1210', kim='Fahreddîn er-Râzî', ne='Esâsü’t-takdîs: kānûn-ı küllî.', neden='Akıl-nakil teorisinin Eş‘arî formülü.'),
  dict(t='728/1328', kim='İbn Teymiyye', ne='Der’ü teâruzi’l-akl ve’n-nakl.', neden='Kānûn-ı küllîye kapsamlı itiraz.'),
  dict(t='1145/1732', kim='Saçaklızâde', ne='Takrîrü’l-kavânîn ve el-Velediyye.', neden='Osmanlı medreselerinin münazara metinleri.')],
 METIN=[
  M('Eş‘arî: Kelâmla uğraşmanın meşruiyeti', 'İstihsânü’l-havz’ın girişi: bazı kimselerin kelâmı bid‘at saydığını, oysa Kur’an’ın aklî delillerle dolu olduğunu söyler.', 'إن طائفة من الناس جعلوا الجهل رأس مالهم، وثقل عليهم النظر والبحث عن الدين، ومالوا إلى التخفيف والتقليد', 'الأشعري، استحسان الخوض في علم الكلام')],
 KUT=[
  B('Yöntem', 'Kitâbü’t-Tevhîd', 'كتاب التوحيد', 'Ebû Mansûr el-Mâtürîdî', '333/944', 'Bilgi teorisiyle açılan Mâtürîdî kelâmının kurucu eseri; Topaloğlu–Aruçi tahkiki ve tercümesi.'),
  B('Yöntem', 'İstihsânü’l-havz fî ilmi’l-kelâm', 'استحسان الخوض في علم الكلام', 'Ebü’l-Hasan el-Eş‘arî', '324/936', 'Kelâmın meşruiyetine dair kısa risâle.'),
  B('Yöntem', 'el-Kâfiye fi’l-cedel', 'الكافية في الجدل', 'İmâmü’l-Haremeyn el-Cüveynî', '478/1085', 'Cedel ilminin kelâmcı sistemi.'),
  B('Yöntem', 'Mi‘yârü’l-ilm', 'معيار العلم', 'Gazzâlî', '505/1111', 'Mantığın Sünnî ilimlere taşındığı eser.'),
  B('Yöntem', 'Esâsü’t-takdîs', 'أساس التقديس', 'Fahreddîn er-Râzî', '606/1210', 'Kānûn-ı küllî ve haberî sıfatların te’vili.'),
  B('Yöntem', 'Faslü’l-makāl', 'فصل المقال', 'İbn Rüşd', '595/1198', 'Felsefe ile şeriatın ilişkisi.'),
  B('Yöntem', 'el-Keşf an menâhici’l-edille', 'الكشف عن مناهج الأدلة', 'İbn Rüşd', '595/1198', 'Kelâmcıların delillerinin eleştirisi.'),
  B('Yöntem', 'Der’ü teâruzi’l-akl ve’n-nakl', 'درء تعارض العقل والنقل', 'İbn Teymiyye', '728/1328', 'Akıl-nakil ilişkisine Selefî yaklaşım.'),
  B('Âdâb', 'er-Risâle fî âdâbi’l-bahs', 'رسالة في آداب البحث', 'Şemseddîn es-Semerkandî', 'VII/XIII. yy', 'Münazara ilminin kurucu metni.'),
  B('Âdâb', 'er-Risâletü’l-Adudiyye', 'الرسالة العضدية', 'Adudüddîn el-Îcî', '756/1355', 'Kısa münazara metni.'),
  B('Âdâb', 'Takrîrü’l-kavânîn', 'تقرير القوانين', 'Saçaklızâde Mehmed Efendi', '1145/1732', 'Âdâb ilminin kapsamlı Osmanlı eseri.'),
  B('Âdâb', 'Risâletü’l-Velediyye', 'الرسالة الولدية', 'Saçaklızâde Mehmed Efendi', '1145/1732', 'Osmanlı medreselerinin münazara ders kitabı.'),
  B('Âdâb', 'Risâletü’l-âdâb', 'رسالة الآداب', 'İsmâil Gelenbevî', '1205/1791', 'Geç Osmanlı münazara metni.'),
  B('İlimlerin tasnifi', 'Miftâhu’s-saâde', 'مفتاح السعادة', 'Taşköprizâde Ahmed Efendi', '968/1561', 'İlimlerin tasnifi ve kelâmın ilimler arasındaki yeri.'),
  B('İlimlerin tasnifi', 'Tertîbü’l-ulûm', 'ترتيب العلوم', 'Saçaklızâde Mehmed Efendi', '1145/1732', 'Medrese ilimlerinin okuma sırası.'),
  B('Modern', 'Yeni İlm-i Kelâm', 'علم الكلام الجديد', 'İzmirli İsmâil Hakkı', '1946', 'Kelâmın yönteminin yenilenmesi önerisi.')],
)
USUL['DONEMLER'] = [dict(ad=t['ad'], aralik=t['aralik'], d=t['d']) for t in USUL['TASNIF']['tesekkul']]
del DONEMLER
