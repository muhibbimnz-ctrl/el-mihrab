# Siyer Dirâsesi — sahne (hikâye) bölümleri. Metinler el-Mihrâb için özgün olarak yazılmıştır.
# {kelime|anlam} : zor kelime açıklaması. yer: harita noktası id. ayet: [(etiket,'sure-ayet',not)]
# hadis: [(etiket, arama ifadesi, kapsam, not)]  fikih: [mesele id]  kisi: [(ad, tanıtım)]  ders: [cümle]
O=[
dict(id='dogum',donem='Mekke dönemi',tarih='Fil yılı · M. 571',yer='mekke',baslik='Fil yılı ve doğum',ar='المولد النبوي',
metin='''Mekke, Kâbe’nin etrafında kurulmuş, ekin bitmeyen bir {vadi|iki dağ arasındaki çukur arazi} şehriydi. Yemen valisi Ebrehe, Kâbe’yi yıkıp insanları kendi yaptırdığı kiliseye çevirmek için fillerle yola çıktı. Mekkeliler dağlara çekildi. Kureyş’in ileri geleni Abdülmuttalib, Ebrehe’nin elindeki develerini istedi ve “Ben develerin sahibiyim, Beyt’in de bir sahibi var, onu O korur” dedi.
Ordu Mekke’ye yaklaşınca fil yürümedi; gökten gelen kuş sürüleri orduyu dağıttı. Kur’an bu olayı Fîl suresinde anlatır. Araplar o yılı “Fil yılı” diye andı.
Aynı yıl, Rebîülevvel ayında Abdülmuttalib’in oğlu Abdullah ile Âmine’nin oğlu dünyaya geldi. Babası o doğmadan vefat etmişti. Dedesi onu Kâbe’ye götürdü ve ona Muhammed adını verdi. Âdet olduğu üzere süt annesi Halîme ile çöle, Benî Sa‘d yurduna gönderildi; orada temiz hava ve {fasih|düzgün ve açık} Arapça içinde büyüdü.
Altı yaşında annesini, sekiz yaşında dedesini kaybetti; amcası Ebû Tâlib onu yanına aldı. Gençliğinde çobanlık ve ticaret yaptı, doğruluğundan dolayı Mekkeliler ona “el-Emîn” (güvenilir) dedi.''',
ayet=[('Fîl 105:1-5','105-1','Fil ordusunun helâki.'),('Duhâ 93:6','93-6','“O seni yetim bulup barındırmadı mı?”')],
hadis=[('Benî Sa‘d’da göğsünün yarılması','شق صدره','sitte','Müslim, Enes’ten.'),('Çobanlık','رعي الغنم','sitte','“Allah’ın gönderdiği her peygamber koyun gütmüştür” (Buhârî).')],
fikih=[],kisi=[('Abdülmuttalib','Dedesi, Kureyş’in ileri geleni.'),('Âmine','Annesi.'),('Halîme es-Sa‘diyye','Süt annesi.'),('Ebû Tâlib','Amcası ve hâmisi.')],
ders=['Allah, Beyt’ini ve elçisini sebepler tükendiği yerde korur.','Yetimlik, Peygamber’in hayatında şefkatin kaynağı oldu.','“Emîn” sıfatı, risaletten önce kazanılmış bir güvendi.']),

dict(id='vahiy',donem='Mekke dönemi',tarih='M. 610 · 40 yaşında',yer='mekke',baslik='Hira’da ilk vahiy',ar='بدء الوحي',
metin='''Kırk yaşına yaklaşırken yalnızlık ona sevimli geldi. Mekke’nin yakınındaki Nur dağında, Hira mağarasında günlerce kalır, {tefekkür|derin düşünme} ve ibadetle meşgul olurdu.
Ramazan ayında bir gece melek Cebrâil geldi ve “Oku!” dedi. “Ben okuma bilmem” cevabını verdi. Melek onu üç defa sıkıp bıraktı, sonra Alak suresinin ilk âyetlerini okudu: “Yaratan Rabbinin adıyla oku…”
Titreyerek evine döndü ve “Beni örtün, beni örtün” dedi. Eşi Hz. Hatice onu teselli etti: “Allah seni asla utandırmaz; sen akrabanı gözetirsin, düşküne yardım edersin, misafiri ağırlarsın.” Sonra onu amcasının oğlu, Tevrat ve İncil’i bilen Varaka b. Nevfel’e götürdü. Varaka, gelenin Mûsâ’ya gelen {Nâmûs|vahiy meleği} olduğunu söyledi.
Bir süre vahiy kesildi (fetret). Sonra Müddessir suresinin ilk âyetleri indi: “Ey örtüye bürünen! Kalk ve uyar.” Böylece davet başladı.''',
ayet=[('Alak 96:1-5','96-1','İlk inen âyetler.'),('Müddessir 74:1-5','74-1','Davet emri.'),('Kadr 97:1','97-1','Kur’an’ın Kadir gecesinde inmesi.')],
hadis=[('Vahyin başlangıcı','اول ما بدي به رسول الله','sitte','Buhârî’nin ilk hadislerinden, Hz. Âişe’den.'),('“Beni örtün”','زملوني','sitte','Buhârî, Müslim.')],
fikih=[],kisi=[('Hz. Hatice','İlk iman eden; Peygamber’in eşi.'),('Varaka b. Nevfel','Hatice’nin amcasının oğlu; ehl-i kitap âlimi.'),('Cebrâil','Vahiy meleği.')],
ders=['Vahiy “oku” emriyle başladı: ilim, bu dinin ilk kapısıdır.','Hz. Hatice’nin teselli cümleleri, güzel ahlakın Allah katındaki değerini gösterir.','Zor anlarda bilgili ve güvenilir insanlara danışmak sünnettir.']),

dict(id='davet',donem='Mekke dönemi',tarih='M. 613',yer='mekke',baslik='Safâ tepesinde açık davet',ar='الجهر بالدعوة',
metin='''Üç yıl kadar davet gizli yürüdü. İlk Müslümanlar Hz. Hatice, Hz. Ebû Bekir, Hz. Ali ve Zeyd b. Hârise idi. Ebû Bekir’in davetiyle Osman, Zübeyr, Abdurrahman b. Avf, Sa‘d b. Ebî Vakkâs ve Talha da iman etti.
Sonra “En yakın akrabanı uyar” âyeti indi. Peygamber Safâ tepesine çıkıp Kureyş’e seslendi: “Şu dağın ardında bir atlı birliği size saldırmak üzere desem bana inanır mısınız?” “Evet, senden yalan duymadık” dediler. “Ben, önünüzdeki çetin bir azaba karşı sizi uyarıyorum” dedi.
Amcası Ebû Leheb öfkeyle karşı çıktı; bunun üzerine Tebbet suresi indi. Bundan sonra {işkence|eziyet, zulüm} başladı: Bilâl kızgın kumlara yatırıldı, Yâsir ailesi işkence gördü; Sümeyye İslam’ın ilk şehidi oldu. Müslümanlar Erkam b. Ebi’l-Erkam’ın evinde toplanıp Kur’an öğreniyordu.''',
ayet=[('Şuarâ 26:214','26-214','“En yakın akrabanı uyar.”'),('Tebbet 111:1','111-1','Ebû Leheb hakkında.'),('Hicr 15:94','15-94','“Emrolunduğun şeyi açıkça bildir.”')],
hadis=[('Safâ tepesindeki çağrı','صعد النبي صلي الله عليه وسلم علي الصفا','sitte','Buhârî, İbn Abbâs’tan.')],
fikih=[],kisi=[('Hz. Ebû Bekir','İlk iman eden hür erkek.'),('Hz. Ali','İlk iman eden çocuk.'),('Bilâl-i Habeşî','İşkenceye “Ehad, Ehad” diye direnen sahâbî.'),('Sümeyye','İlk kadın şehit.')],
ders=['Davet en yakından başlar.','Güvenilirlik, tebliğin en büyük sermayesidir.','İman uğruna çekilen eziyet boşa gitmez.']),

dict(id='habesistan',donem='Mekke dönemi',tarih='M. 615',yer='habesistan',baslik='Habeşistan’a hicret',ar='الهجرة إلى الحبشة',
metin='''Eziyet artınca Peygamber, korunmasız Müslümanlara “Habeşistan’da kimseye zulmedilmeyen bir {hükümdar|kral} var” dedi. Önce on beş kadar kişi, sonra seksenden fazla Müslüman denizi geçerek Habeşistan’a gitti. Aralarında Hz. Osman ile eşi Rukıyye, Ca‘fer b. Ebî Tâlib de vardı.
Kureyş peşlerinden Amr b. el-Âs’ı hediyelerle gönderdi. Necâşî Müslümanları dinlemek istedi. Ca‘fer ayağa kalktı; cahiliyede putlara taptıklarını, akrabalık bağlarını kopardıklarını, Allah’ın onlara doğru sözlü bir peygamber gönderdiğini anlattı ve Meryem suresinden okudu.
Necâşî ağladı, “Bu ve Îsâ’nın getirdiği aynı kandilden çıkmıştır” dedi ve Müslümanları teslim etmedi. Yıllar sonra Necâşî vefat edince Peygamber Medine’de onun için gıyabî cenaze namazı kıldırdı.''',
ayet=[('Meryem 19:16-36','19-16','Ca‘fer’in Necâşî’ye okuduğu âyetler.'),('Zümer 39:10','39-10','“Allah’ın arzı geniştir.”')],
hadis=[('Necâşî’nin cenazesi','نعي النجاشي','sitte','Buhârî, Müslim.')],
fikih=['gaib'],kisi=[('Ca‘fer b. Ebî Tâlib','Muhacirlerin sözcüsü.'),('Necâşî (Ashame)','Habeş hükümdarı.'),('Hz. Osman ve Rukıyye','İlk muhacirlerden.')],
ders=['Dinini yaşayamayan, yaşayabileceği yere hicret eder.','Hakkı açık ve doğru anlatmak gönülleri yumuşatır.','Adaletli yönetici, dini farklı da olsa takdir edilir.']),

dict(id='taif',donem='Mekke dönemi',tarih='M. 619 · Hüzün yılı',yer='taif',baslik='Hüzün yılı ve Tâif',ar='عام الحزن والطائف',
metin='''Nübüvvetin onuncu yılında önce amcası Ebû Tâlib, kısa süre sonra Hz. Hatice vefat etti. Bu yıl “Hüzün yılı” diye anıldı. Ebû Tâlib’in himayesi kalkınca Mekke’de eziyet arttı.
Peygamber, Zeyd b. Hârise ile birlikte Tâif’e gitti, Sakîf kabilesini İslam’a çağırdı. Onlar alay ettiler, çocukları ve {ayak takımını|halkın kaba kısmını} peşine takıp taşlattılar; ayakları kanadı.
Bir bahçeye sığındı ve Rabbine o meşhur duayı etti: gücünün azlığını, çaresizliğini Allah’a arz etti ve “Sen bana gazap etmedikten sonra hiçbir şeye aldırmam” dedi. Dağlar meleği gelip “İstersen şu iki dağı üzerlerine kapatayım” dedi. O, “Hayır, umarım Allah onların neslinden yalnız O’na kulluk eden insanlar çıkarır” cevabını verdi.''',
ayet=[('Ahkâf 46:29','46-29','Dönüşte cinlerin Kur’an dinlemesi.')],
hadis=[('Dağlar meleği','ملك الجبال','sitte','Buhârî, Müslim (Hz. Âişe).')],
fikih=[],kisi=[('Zeyd b. Hârise','Peygamber’in azatlısı ve evlatlığı.'),('Addâs','Tâif’te üzüm getiren Ninovalı köle; iman etti.')],
ders=['Merhamet, intikam imkânı varken bile beddua etmemektir.','Sıkıntı anında Allah’a sığınmak peygamber yoludur.']),

dict(id='isra',donem='Mekke dönemi',tarih='M. 621 civarı',yer='mekke',baslik='İsrâ ve Mi‘râc',ar='الإسراء والمعراج',
metin='''Hüzünlü günlerin ardından bir gece Peygamber, Mescid-i Harâm’dan Mescid-i Aksâ’ya götürüldü (İsrâ), oradan göklere yükseltildi (Mi‘râc). Mescid-i Aksâ’da peygamberlere imam oldu.
Mi‘râcda beş vakit namaz farz kılındı. Önce elli vakit emredilmiş, Hz. Mûsâ’nın tavsiyesiyle Peygamber birkaç kez hafifletilmesini istemiş ve beş vakte indirilmişti; sevabı ise elli vakit olarak bırakıldı. Bakara suresinin son âyetleri de bu gecenin {hediyesi|ikramı} sayılır.
Sabah Mekkelilere anlattığında alay edenler oldu. Ebû Bekir ise “O söylediyse doğrudur” dedi ve “es-Sıddîk” lakabını aldı.''',
ayet=[('İsrâ 17:1','17-1','Gece yolculuğu.'),('Necm 53:13-18','53-13','Sidretü’l-müntehâ.'),('Bakara 2:285-286','2-285','Mi‘râcda verilen son âyetler.')],
hadis=[('Mi‘râc hadisi ve beş vakit','فرض الله علي امتي خمسين صلاه','sitte','Buhârî, Müslim.')],
fikih=['ikindi'],kisi=[('Hz. Ebû Bekir es-Sıddîk','Tereddütsüz tasdik etti.'),('Hz. Mûsâ','Namazın hafifletilmesini tavsiye etti.')],
ders=['Namaz, Mi‘râcda doğrudan farz kılınan ibadettir: müminin mi‘râcıdır.','Teslimiyet, akla sığmayanı da Allah’ın kudretine havale etmektir.']),

dict(id='akabe',donem='Mekke dönemi',tarih='M. 621–622',yer='mekke',baslik='Akabe biatleri',ar='بيعة العقبة',
metin='''Hac mevsimlerinde Peygamber kabileleri dolaşıp İslam’ı anlatıyordu. Yesrib’den (Medine) gelen Hazrecli altı kişi onu dinledi ve iman etti. Ertesi yıl on iki kişi Mina’daki Akabe’de {biat|bağlılık sözü} etti: Allah’a ortak koşmamak, hırsızlık ve zina etmemek, çocuklarını öldürmemek, iftira etmemek.
Peygamber onlarla Mus‘ab b. Umeyr’i öğretmen olarak gönderdi. Mus‘ab’ın gayretiyle Medine’de İslam hızla yayıldı.
Bir yıl sonra yetmiş üç erkek ve iki kadın, gece gizlice Akabe’de buluştu. Peygamber’i ailelerini korudukları gibi koruyacaklarına söz verdiler. Böylece hicretin yolu açıldı.''',
ayet=[('Mümtehine 60:12','60-12','Biat maddelerine benzeyen kadınların biatı.')],
hadis=[('Akabe biatı (Ubâde)','بايعوني علي ان لا تشركوا بالله شيئا','sitte','Buhârî, Müslim.')],
fikih=[],kisi=[('Mus‘ab b. Umeyr','İlk “İslam öğretmeni.”'),('Es‘ad b. Zürâre','Medine’de ilk cumayı kıldıran.'),('Ubâde b. Sâmit','Akabe biatına katılanlardan.')],
ders=['Bir şehir, samimi bir öğretmenle değişebilir.','Söz ve biat, Müslüman toplumun temelidir.']),

dict(id='hicret',donem='Medine dönemi',tarih='H. 1 · M. 622',yer='medine',baslik='Hicret',ar='الهجرة',
metin='''Müslümanlar küçük gruplar hâlinde Medine’ye göçmeye başladı. Kureyş, Dâru’n-Nedve’de toplanıp Peygamber’i öldürmeye karar verdi. O gece Hz. Ali Peygamber’in yatağına yattı; Peygamber evinden çıktı ve Ebû Bekir ile birlikte Sevr mağarasına gizlendi.
Takipçiler mağaranın ağzına kadar geldi. Ebû Bekir endişelenince Peygamber “Üzülme, Allah bizimle” dedi. Üç gün sonra {kılavuz|yol gösterici} Abdullah b. Uraykıt ile sahil yolundan Medine’ye yöneldiler. Yolda Sürâka peşlerine düştü; atının ayakları kuma battı ve geri döndü.
Kubâ’da birkaç gün kalıp ilk mescidi kurdular. Medine’ye girişte halk sevinçle karşıladı. Peygamber’in devesi Ebû Eyyûb el-Ensârî’nin evinin önünde çöktü; orada Mescid-i Nebevî yapıldı. Muhacirler ile Ensar kardeş ilan edildi. Hz. Ömer döneminde hicret, İslam takviminin başlangıcı kabul edildi.''',
ayet=[('Tevbe 9:40','9-40','Mağaradaki “Üzülme, Allah bizimle.”'),('Enfâl 8:30','8-30','Dâru’n-Nedve tuzağı.'),('Tevbe 9:108','9-108','Takva üzerine kurulan mescit (Kubâ).')],
hadis=[('Mağarada','ما ظنك باثنين الله ثالثهما','sitte','“Üçüncüsü Allah olan iki kişi hakkında ne düşünürsün?” (Buhârî, Müslim).'),('Hicret yolculuğu','سراقه','sitte','Buhârî.')],
fikih=['cumasayi'],kisi=[('Hz. Ali','Peygamber’in yatağına yattı, emanetleri sahiplerine verdi.'),('Esmâ bnt. Ebî Bekir','Mağaraya yiyecek taşıdı; “Zâtü’n-nitâkayn.”'),('Sürâka b. Mâlik','Takip edip geri dönen; sonra Müslüman oldu.'),('Ebû Eyyûb el-Ensârî','Peygamber’i evinde misafir etti.')],
ders=['Tedbir almak tevekküle aykırı değildir.','Kardeşlik (muâhât), yeni bir toplumun ilk binasıdır.','Mescit, toplum hayatının merkezidir.']),

dict(id='kible',donem='Medine dönemi',tarih='H. 2 · M. 624',yer='medine',baslik='Kıblenin Kâbe’ye çevrilmesi ve orucun farz oluşu',ar='تحويل القبلة',
metin='''Medine’de on altı veya on yedi ay Kudüs’e (Beytü’l-Makdis) doğru namaz kılındı. Peygamber, kıblenin Kâbe olmasını arzu eder, yüzünü göğe çevirirdi.
Hicretin ikinci yılında Bakara suresinin âyetleri indi: “Yüzünü Mescid-i Harâm tarafına çevir.” Bir mescitte ikindi kılan cemaate haber ulaşınca namazın içinde Kâbe’ye döndüler; o mescide “Kıbleteyn” (iki kıbleli) dendi. Münafıklar ve bazı Yahudiler bunu dedikodu konusu yaptı; Kur’an “Doğu da batı da Allah’ındır” diye cevap verdi.
Aynı yıl Ramazan orucu ve fıtır sadakası farz kılındı; zekâtın oranları da bu yıllarda açıklandı.''',
ayet=[('Bakara 2:144','2-144','Kıblenin çevrilmesi.'),('Bakara 2:142','2-142','Beyinsizlerin itirazı.'),('Bakara 2:183-185','2-183','Orucun farz kılınması.')],
hadis=[('Kıble değişince namazda dönmeleri','وقد امر ان يستقبل الكعبه','sitte','Buhârî, Müslim (İbn Ömer).')],
fikih=['kible','niyetvakti','hilal','fitir'],kisi=[('Berâ b. Âzib','Kıble olayını rivayet eden sahâbî.')],
ders=['Teslimiyet: Emir gelince namazın içinde bile yön değiştirmek.','Kıble, ümmetin kimliğidir.']),

dict(id='bedir',donem='Medine dönemi',tarih='17 Ramazan H. 2 · M. 624',yer='bedir',baslik='Bedir',ar='غزوة بدر',
metin='''Ebû Süfyân’ın idaresindeki büyük Kureyş kervanı Şam’dan dönüyordu. Müslümanlar kervanı yakalamak için çıktı; kervan sahil yoluna saparak kurtuldu, fakat Mekke’den bin kişilik bir ordu yola çıktı.
Peygamber ashabına danıştı. Muhacirlerden Mikdâd “Biz sana Mûsâ’nın kavmi gibi ‘Sen ve Rabbin gidin savaşın’ demeyiz” dedi. Ensar adına Sa‘d b. Muâz “Bizi denize götürsen seninle dalarız” dedi. Üç yüz on küsur Müslüman, Ramazanın on yedinci günü Bedir kuyuları başında bin kişilik orduyla karşılaştı.
Peygamber gece sabaha kadar dua etti: “Allah’ım, bu topluluk helâk olursa yeryüzünde sana ibadet edecek kimse kalmaz.” Allah melekler ve yağmurla destekledi. Ebû Cehil başta olmak üzere Kureyş’in ileri gelenleri öldü. Esirlere iyi davranıldı; okuma yazma bilenlerin fidyesi on Medineli çocuğa yazı öğretmek oldu.''',
ayet=[('Enfâl 8:9','8-9','Meleklerle yardım.'),('Âl-i İmrân 3:123','3-123','“Siz zayıf iken Allah size Bedir’de yardım etti.”'),('Enfâl 8:41','8-41','Ganimetin beşte biri.')],
hadis=[('Bedir gecesi dua','اللهم ان تهلك هذه العصابه','sitte','Müslim (Ömer).'),('Bedir ehli','لعل الله اطلع علي اهل بدر','sitte','Buhârî, Müslim.')],
fikih=[],kisi=[('Sa‘d b. Muâz','Ensarın sözcüsü.'),('Mikdâd b. Amr','Muhacirlerin sözcüsü.'),('Ebû Cehil','Kureyş ordusunun komutanı.')],
ders=['İstişare, liderin ilk işidir.','Zafer sayıyla değil, ihlas ve duayladır.','Esire iyilik ve ilme değer, Bedir’in ahlakıdır.']),

dict(id='uhud',donem='Medine dönemi',tarih='Şevval H. 3 · M. 625',yer='uhud',baslik='Uhud',ar='غزوة أحد',
metin='''Bedir’in intikamını almak isteyen Kureyş, üç bin kişilik bir orduyla Medine’ye geldi. Peygamber şehirde savunmayı düşünüyordu; gençlerin ısrarıyla Uhud dağının eteğine çıkıldı. Münafık Abdullah b. Übey üç yüz kişiyle yoldan döndü; yedi yüz kişi kaldı.
Peygamber Ayneyn tepesine elli okçu yerleştirdi ve “Bizi kuşların kaptığını görseniz bile yerinizden ayrılmayın” dedi. Savaşın başında Müslümanlar üstündü. Okçuların çoğu ganimet için tepeden inince Hâlid b. Velîd arkadan dolaştı.
Saflar dağıldı, Peygamber yaralandı, dişi kırıldı. Hz. Hamza başta olmak üzere yetmiş sahâbî şehit oldu. Şehitler yıkanmadan, kanlı elbiseleriyle defnedildi. Kur’an bu yenilgiyi itaatsizliğin ve dünyalık sevgisinin bir {imtihanı|sınaması} olarak anlattı.''',
ayet=[('Âl-i İmrân 3:121-122','3-121','Savaş düzeni.'),('Âl-i İmrân 3:152','3-152','Okçuların emri çiğnemesi.'),('Âl-i İmrân 3:169','3-169','“Allah yolunda öldürülenleri ölü sanma.”')],
hadis=[('Okçular','لا تبرحوا','sitte','Buhârî (Berâ).'),('Şehitlerin defni','ولم يصل عليهم','sitte','Buhârî (Câbir).')],
fikih=['sehit'],kisi=[('Hz. Hamza','Seyyidü’ş-şühedâ.'),('Mus‘ab b. Umeyr','Sancaktar, şehit.'),('Nesîbe (Ümmü Umâre)','Peygamber’i korumak için savaştı.'),('Hâlid b. Velîd','O gün Kureyş süvarilerinin komutanı.')],
ders=['Emre itaat, zaferin şartıdır.','Yenilgi de bir terbiye ve arınmadır.','Şehitler ölü değildir.']),

dict(id='hendek',donem='Medine dönemi',tarih='Şevval H. 5 · M. 627',yer='hendek',baslik='Hendek (Ahzâb)',ar='غزوة الخندق',
metin='''Kureyş, Gatafân ve diğer kabileler on bin kişilik bir {ittifak|birleşik ordu} kurup Medine’ye yürüdü. Selmân-ı Fârisî’nin önerisiyle Medine’nin açık kuzey tarafına hendek kazıldı. Peygamber de ashabıyla toprak taşıdı; açlıktan karınlarına taş bağladılar.
Kuşatma yaklaşık bir ay sürdü. Medine’deki Benî Kurayza Yahudileri antlaşmayı bozdu; Müslümanlar iki ateş arasında kaldı. Kur’an o günü “gözlerin kaydığı, yüreklerin gırtlaklara dayandığı” gün diye anlatır.
Bir gün savaş yüzünden ikindi ve diğer namazlar vaktinde kılınamadı; Peygamber onları sırasıyla kaza etti. Sonunda soğuk bir rüzgâr düşman ordusunun çadırlarını söktü ve kuşatma dağıldı. Peygamber “Artık biz onlara gideriz, onlar bize gelemez” dedi.''',
ayet=[('Ahzâb 33:9-11','33-9','Rüzgâr ve görünmez ordular.'),('Ahzâb 33:21','33-21','“Sizin için Resûlullah’ta güzel bir örnek vardır.”')],
hadis=[('Hendek günü kaza edilen namazlar','يوم الخندق','sitte','Buhârî, Müslim.'),('“Artık biz onlara gideriz”','نغزوهم ولا يغزوننا','sitte','Buhârî.')],
fikih=['kazatertip','kerahet'],kisi=[('Selmân-ı Fârisî','Hendek fikrini veren sahâbî.'),('Nuaym b. Mes‘ûd','Düşman saflarına ayrılık düşüren yeni Müslüman.')],
ders=['Fikir nereden gelirse alınır: Hendek bir Fars savaş tekniğiydi.','Lider, zahmeti ashabıyla paylaşır.','Kaçırılan namaz sırasıyla kaza edilir.']),

dict(id='hudeybiye',donem='Medine dönemi',tarih='Zilkade H. 6 · M. 628',yer='hudeybiye',baslik='Hudeybiye Antlaşması',ar='صلح الحديبية',
metin='''Peygamber bir rüya üzerine umre niyetiyle yaklaşık bin dört yüz sahâbîyle yola çıktı; kurbanlıkları da yanlarındaydı. Kureyş onları Mekke’ye sokmadı. Müslümanlar Hudeybiye’de durdu.
Elçi olarak gönderilen Hz. Osman’ın öldürüldüğü haberi yayılınca sahâbe bir ağacın altında ölümüne biat etti (Rıdvân biatı). Sonra Kureyş’in elçisi Süheyl b. Amr ile antlaşma yapıldı: on yıl savaş olmayacak, Müslümanlar o yıl dönüp ertesi yıl umre yapacaklardı. Bazı maddeler sahâbeye ağır geldi.
Peygamber kurbanını kesip tıraş oldu; sahâbe de onu görünce aynısını yaptı ve ihramdan çıktılar. Dönüş yolunda Fetih suresi indi ve antlaşmayı “apaçık bir fetih” diye müjdeledi. Barış ortamında iki yılda Müslümanların sayısı önceki yıllardan fazla arttı.''',
ayet=[('Fetih 48:1','48-1','“Sana apaçık bir fetih verdik.”'),('Fetih 48:18','48-18','Ağacın altındaki biat.'),('Bakara 2:196','2-196','Engellenenin (ihsar) hükmü.')],
hadis=[('Hudeybiye antlaşması','صلح الحديبيه','sitte','Buhârî, Şurût bölümü.'),('Ümmü Seleme’nin tavsiyesi','اخرج ثم لا تكلم احدا','sitte','Buhârî.')],
fikih=['ihsar','ihram','bedel'],kisi=[('Hz. Osman','Mekke’ye elçi.'),('Süheyl b. Amr','Kureyş’in antlaşma elçisi.'),('Ümmü Seleme','Peygamber’e kurbanını kesmesini tavsiye eden eşi.')],
ders=['Sabır ve barış, zaferin kapısı olabilir.','Lider örnek olunca söz gerekmez: Ümmü Seleme’nin tavsiyesi.','Kadının görüşü istişarede değerlidir.']),

dict(id='hayber',donem='Medine dönemi',tarih='Muharrem H. 7 · M. 628',yer='hayber',baslik='Hayber',ar='غزوة خيبر',
metin='''Hendek’te düşmanları kışkırtan Benî Nadîr’in sığındığı Hayber, Medine’nin kuzeyinde, kaleleri ve hurmalıklarıyla müstahkem bir yerdi. Hudeybiye’den döndükten kısa süre sonra Müslümanlar Hayber’e yürüdü.
Kaleler birer birer fethedildi. Peygamber “Yarın sancağı, Allah ve Resûlü’nün sevdiği ve onların da onu sevdiği birine vereceğim” dedi ve sancağı Hz. Ali’ye verdi. Kamus kalesi onun eliyle açıldı.
Hayber arazisi, mahsulün yarısı karşılığında Yahudilere bırakıldı (müsâkât ve müzâraa). Hz. Ömer’in buradan payına düşen değerli araziyi “aslını alıkoy, gelirini tasadduk et” tavsiyesiyle vakfetmesi, İslam’daki vakıf geleneğinin ilk örneklerindendir. Ehlî eşek eti bu gazvede yasaklandı, at etine izin verildi. Habeşistan muhacirleri de Ca‘fer ile bu günlerde döndü.''',
ayet=[('Fetih 48:20','48-20','“Allah size alacağınız birçok ganimet vaat etti.”')],
hadis=[('Sancak Ali’ye','لاعطين الرايه غدا','sitte','Buhârî, Müslim.'),('Ömer’in vakfı','حبست اصلها وتصدقت بها','sitte','Buhârî, Müslim.'),('Ehlî eşek ve at','واذن في لحوم الخيل','sitte','Buhârî, Müslim.')],
fikih=['vakif','at'],kisi=[('Hz. Ali','Sancaktar, Hayber fatihi.'),('Hz. Ömer','Hayber’deki arazisini vakfetti.'),('Ca‘fer b. Ebî Tâlib','Habeşistan’dan bu günlerde döndü.')],
ders=['Vakıf, hayrın sürekli kılınmasıdır.','Yenilen topluma adaletle muamele.']),

dict(id='fetih',donem='Medine dönemi',tarih='Ramazan H. 8 · M. 630',yer='mekke',baslik='Mekke’nin fethi',ar='فتح مكة',
metin='''Kureyş’in müttefikleri, Müslümanların müttefiki Huzâa’ya saldırarak Hudeybiye antlaşmasını bozdu. Peygamber on bin kişilik bir orduyla Ramazanda yola çıktı; yolda oruçlarını bozdular.
Ordu Mekke’ye neredeyse savaşsız girdi. Ebû Süfyân Müslüman oldu; “Ebû Süfyân’ın evine giren, evinin kapısını kapatan, Mescid-i Harâm’a giren güvendedir” denildi. Peygamber Kâbe’deki üç yüz altmış putu elindeki çubukla devirirken “Hak geldi, bâtıl yok oldu” âyetini okuyordu.
Yıllarca kendisine eziyet eden Mekkelilere “Size bugün bir kınama yok; gidin, serbestsiniz” dedi. Bilâl Kâbe’nin üzerine çıkıp ezan okudu. Peygamber Mekke’de on dokuz gün kaldı ve namazları kısaltarak kıldı.''',
ayet=[('Nasr 110:1-3','110-1','“Allah’ın yardımı ve fetih gelince…”'),('İsrâ 17:81','17-81','“Hak geldi, bâtıl yok oldu.”'),('Yûsuf 12:92','12-92','“Bugün size kınama yok.”')],
hadis=[('Putların yıkılması','جاء الحق وزهق الباطل','sitte','Buhârî, Müslim.'),('Yolda oruç','الكديد','sitte','Fetih yolunda Kedîd’de oruç bozuldu (Buhârî).'),('On dokuz gün kısaltma','تسعه عشر','k:bukhari','Buhârî (İbn Abbâs).')],
fikih=['yolcuoruc','ikamet','kasr'],kisi=[('Ebû Süfyân','Kureyş’in lideri; fetih öncesi Müslüman oldu.'),('Bilâl','Kâbe’nin üzerinde ezan okudu.'),('Hâlid b. Velîd','Ordunun bir kolunun komutanı.')],
ders=['Affetmek, güç elde iken yapılır.','Tevhid, Kâbe’nin putlardan temizlenmesiyle tamamlandı.']),

dict(id='huneyn',donem='Medine dönemi',tarih='Şevval H. 8 · M. 630',yer='huneyn',baslik='Huneyn ve Tâif',ar='غزوة حنين',
metin='''Fetihten hemen sonra Hevâzin ve Sakîf kabileleri büyük bir ordu topladı. On iki bin kişilik İslam ordusu kalabalığına güvendi; bazıları “Bugün azlıktan yenilmeyiz” dedi.
Huneyn vadisinde sabahın karanlığında pusuya düştüler; ordu dağıldı. Peygamber beyaz katırının üzerinde sebat etti ve “Ben peygamberim, yalan değil; ben Abdülmuttalib’in oğluyum” diye seslendi. Amcası Abbâs’ın gür sesiyle ashap toplandı ve zafer kazanıldı.
Ganimetler dağıtılırken yeni Müslümanlara bol pay verildi; Ensar üzülünce Peygamber onlara “İnsanlar koyun ve develerle dönerken siz Resûlullah ile dönmeye razı olmaz mısınız?” dedi; Ensar ağlayarak razı oldu.''',
ayet=[('Tevbe 9:25-26','9-25','“Çokluğunuz sizi böbürlendirmişti.”')],
hadis=[('“Ben peygamberim, yalan değil”','انا النبي لا كذب','sitte','Buhârî, Müslim.'),('Ensara hitap','ترضون ان يذهب الناس بالشاه والبعير','sitte','Buhârî, Müslim.')],
fikih=['siniflar'],kisi=[('Abbâs b. Abdülmuttalib','Gür sesiyle ashabı topladı.'),('Mâlik b. Avf','Hevâzin’in komutanı; sonra Müslüman oldu.')],
ders=['Sayıya güvenmek bozgunun sebebidir.','Kalpleri İslam’a ısındırmak (müellefe-i kulûb) da bir siyasettir.']),

dict(id='tebuk',donem='Medine dönemi',tarih='Recep H. 9 · M. 630',yer='tebuk',baslik='Tebük',ar='غزوة تبوك',
metin='''Bizans’ın kuzeyde ordu topladığı haberi geldi. Mevsim çok sıcak, yol uzun, hurmalar olgunlaşmıştı. Peygamber bu sefere açıkça çağırdı; otuz bin kişilik ordu “zorluk ordusu” (ceyşü’l-usre) diye anıldı. Hz. Osman orduyu donatmak için büyük bir bağış yaptı, Hz. Ebû Bekir bütün malını getirdi.
Ordu Tebük’e ulaştı, Bizans karşısına çıkmadı. Peygamber yirmi gün kadar orada kalıp namazları kısalttı; yolculukta öğle ile ikindiyi, akşam ile yatsıyı birleştirdi. Bölge kabileleriyle antlaşmalar yapıldı.
Münafıkların bahaneleri Tevbe suresinde açığa çıkarıldı. Özürsüz geride kalan üç samimi sahâbî (Kâ‘b b. Mâlik ve iki arkadaşı) elli gün boyunca toplumdan uzak tutuldu; sonra tövbeleri kabul edildi.''',
ayet=[('Tevbe 9:38-41','9-38','Sefere çağrı.'),('Tevbe 9:117-118','9-117','Geride kalan üç kişinin tövbesi.')],
hadis=[('Kâ‘b b. Mâlik’in kıssası','كعب بن مالك','k:bukhari','Buhârî, Meğâzî.'),('Tebük’te cem‘','غزوه تبوك','k:muslim','Müslim (Muâz).')],
fikih=['cem','kasr','ikamet'],kisi=[('Kâ‘b b. Mâlik','Doğruyu söyleyip tövbesi kabul edilen sahâbî.'),('Hz. Osman','Orduyu donattı.'),('Ebû Hayseme','Sonradan yetişen sahâbî.')],
ders=['Doğruluk, insanı zor anda bile kurtarır.','Malı Allah yolunda vermek imanın ölçüsüdür.']),

dict(id='veda',donem='Medine dönemi',tarih='Zilhicce H. 10 · M. 632',yer='arafat',baslik='Vedâ haccı',ar='حجة الوداع',
metin='''Hicretin onuncu yılında Peygamber hac için yola çıktığını duyurdu; yüz bini aşkın Müslüman toplandı. Bu, onun yaptığı tek hac oldu ve “Menâsikinizi benden alın” dedi.
Arefe günü Arafat’ta devesinin üzerinde meşhur hutbesini okudu: Canların, malların ve namusların dokunulmaz olduğunu; cahiliye kan davalarının ve ribânın kaldırıldığını; kadınlar hakkında Allah’tan korkmayı; Allah’ın kitabına sarılmayı tavsiye etti. “Tebliğ ettim mi?” diye sordu; “Evet” dediler. “Allah’ım şahit ol” dedi.
O gün “Bugün dininizi kemale erdirdim” âyeti indi. Peygamber haccını tamamlayıp Medine’ye döndü.''',
ayet=[('Mâide 5:3','5-3','“Bugün dininizi kemale erdirdim.”'),('Bakara 2:198-199','2-198','Arafat ve Müzdelife.'),('Bakara 2:278-279','2-278','Ribânın kaldırılması.')],
hadis=[('Câbir’in uzun hac hadisi','فاجاز رسول الله صلي الله عليه وسلم حتي اتي عرفه','k:muslim','Müslim (Câbir).'),('“Kanlarınız, mallarınız”','فان دماءكم واموالكم','sitte','Buhârî, Müslim.'),('“Menâsikinizi benden alın”','لتاخذوا مناسككم','sitte','Müslim.')],
fikih=['kiran','hactertip','arafatgunes','muzdelife','say'],kisi=[('Câbir b. Abdullah','Haccı en ayrıntılı anlatan sahâbî.')],
ders=['İnsan hakları hutbesi: can, mal ve namus dokunulmazdır.','Ribâ ve kan davası, cahiliyenin kaldırılan mirasıdır.']),

dict(id='vefat',donem='Medine dönemi',tarih='Rebîülevvel H. 11 · M. 632',yer='medine',baslik='Vefat',ar='الوفاة النبوية',
metin='''Vedâ haccından birkaç ay sonra Peygamber hastalandı. Hastalığı ağırlaşınca Hz. Âişe’nin odasında kalmak için izin istedi. Namazları kıldırmak için Ebû Bekir’i görevlendirdi.
Son günlerinde sık sık “Namaza dikkat edin, elinizin altındakilere (hizmetçilere) iyi davranın” diye tavsiye ediyordu. Son sözleri “Er-Refîku’l-a‘lâ” (en yüce dost) oldu.
Haber yayılınca Hz. Ömer bunu kabul edemedi. Hz. Ebû Bekir gelip halka hitap etti: “Kim Muhammed’e tapıyorsa bilsin ki Muhammed ölmüştür. Kim Allah’a ibadet ediyorsa bilsin ki Allah diridir, ölmez.” Ardından “Muhammed ancak bir peygamberdir…” âyetini okudu. Ashap bu âyeti sanki o gün ilk defa duyuyormuş gibi oldu. Peygamber vefat ettiği odaya defnedildi.''',
ayet=[('Âl-i İmrân 3:144','3-144','“Muhammed ancak bir peygamberdir.”'),('Zümer 39:30','39-30','“Sen de öleceksin, onlar da ölecekler.”')],
hadis=[('Ebû Bekir’in hitabı','من كان يعبد محمدا','sitte','Buhârî.'),('Son tavsiye','الصلاه وما ملكت ايمانكم','tisa','Ebû Dâvûd, İbn Mâce.'),('“Refîk-ı a‘lâ”','الرفيق الاعلي','sitte','Buhârî, Müslim.')],
fikih=['cenazefatiha','cenazemescit'],kisi=[('Hz. Âişe','Peygamber onun odasında vefat etti.'),('Hz. Ebû Bekir','İlk halife.'),('Hz. Fâtıma','Peygamber’in vefatından sonra en önce ona kavuşacağı müjdelenen kızı.')],
ders=['Peygamber’in son tavsiyesi: namaz ve zayıfların hakkı.','Allah’a kulluk, kişiye bağlı değildir; Allah diridir, ölmez.']),
]
YER={'mekke':('Mekke',21.42,39.83),'medine':('Medine',24.47,39.61),'taif':('Tâif',21.27,40.42),'bedir':('Bedir',23.78,38.79),'uhud':('Uhud',24.62,39.62),'hendek':('Hendek',24.32,39.75),
'hudeybiye':('Hudeybiye',21.55,39.55),'hayber':('Hayber',25.70,39.29),'huneyn':('Huneyn',21.60,40.15),'tebuk':('Tebük',28.38,36.57),'arafat':('Arafat',21.35,39.98),'habesistan':('Habeşistan (Aksum)',14.13,38.72)}
