# Çocuk Köşesi — Abdest, namaz (Hanefî), sûreler ve dualar, oyun verileri.
ABDEST = [
 # ikon, başlık, açıklama
 ('🫧','Niyet ve besmele','“Niyet ettim Allah rızası için abdest almaya” deriz. Sonra “Eûzü billâhi mine’ş-şeytâni’r-racîm, Bismillâhirrahmânirrahîm” deriz. Kolları dirseklerin üstüne kadar sıvarız.'),
 ('🤲','Elleri yıkamak','Ellerimizi bileklere kadar üç kez yıkarız. Parmaklarımızın arasını da ovalarız. Yüzük varsa oynatırız.'),
 ('💧','Ağza su vermek','Sağ elimizle ağzımıza üç kez su alır, her seferinde çalkalayıp dökeriz.'),
 ('👃','Burna su vermek','Sağ elimizle burnumuza üç kez su çekeriz, sol elimizle sümkürerek temizleriz.'),
 ('🙂','Yüzü yıkamak (farz)','Yüzümüzü alnın üstündeki saç bitiminden çene altına kadar, bir kulak yumuşağından öbürüne kadar üç kez yıkarız.'),
 ('💪','Sağ kolu yıkamak (farz)','Sağ kolumuzu parmak uçlarından dirseklerle birlikte üç kez yıkarız.'),
 ('💪','Sol kolu yıkamak (farz)','Sol kolumuzu da aynı şekilde dirseklerle birlikte üç kez yıkarız.'),
 ('🖐️','Başı meshetmek (farz)','Ellerimizi ıslatıp başımızın en az dörtte birini sıvazlarız. Buna mesh denir.'),
 ('👂','Kulakları ve boynu meshetmek','Serçe parmaklarımızla kulaklarımızın içini, başparmaklarımızla arkasını meshederiz. Sonra ellerimizin dış yüzüyle boynumuzu meshederiz.'),
 ('🦶','Sağ ayağı yıkamak (farz)','Sağ ayağımızı topuklarla birlikte üç kez yıkarız. Sol elimizin serçe parmağıyla parmak aralarını temizleriz.'),
 ('🦶','Sol ayağı yıkamak (farz)','Sol ayağımızı da topuklarla birlikte üç kez yıkarız.'),
 ('☝️','Kelime-i şehâdet','Abdestten sonra kıbleye dönüp Kelime-i şehâdet getiririz: “Eşhedü en lâ ilâhe illallâh ve eşhedü enne Muhammeden abdühû ve rasûlüh.”'),
]

# Namaz adımları — iki rekâtlı sabah namazının sünneti örneğiyle. poz: çizim anahtarı. o: okunan dualar (DUALAR id)
NAMAZ = [
 dict(poz='kiyam0', b='Niyet', a='Kıbleye döner, ayaklarımızın arası dört parmak açık dururuz. Kalbimizle niyet ederiz: “Niyet ettim Allah rızası için bugünkü sabah namazının sünnetini kılmaya.”', o=[]),
 dict(poz='tekbir', b='İftitah tekbiri', a='Erkekler ellerini kulak hizasına, kızlar omuz hizasına kaldırır. Avuç içleri kıbleye bakar. “Allâhu ekber” deriz. Artık namaza başladık; konuşmayız, etrafa bakmayız.', o=[]),
 dict(poz='kiyam', b='Kıyam', a='Erkekler sağ elini sol elinin üstüne koyarak göbeğinin altına bağlar; kızlar göğüslerinin üstüne koyar. Gözlerimiz secde yerine bakar. Sırasıyla Sübhâneke, Eûzü-Besmele, Fâtiha ve bir sûre okuruz.', o=['subhaneke','euzu','s1','s112']),
 dict(poz='ruku', b='Rükû', a='“Allâhu ekber” diyerek eğiliriz. Ellerimizle dizlerimizi tutar, sırtımızı düz tutarız. Üç kez “Sübhâne rabbiye’l-azîm” (Yüce Rabbim, seni noksan sıfatlardan tenzih ederim) deriz.', o=['ruku']),
 dict(poz='kavme', b='Doğrulma (kavme)', a='“Semi‘allâhü limen hamideh” (Allah kendisine hamd edeni işitir) diyerek doğruluruz. Tam doğrulunca “Rabbenâ leke’l-hamd” (Rabbimiz, hamd sana mahsustur) deriz.', o=['kavme']),
 dict(poz='secde', b='Secde', a='“Allâhu ekber” diyerek önce dizlerimizi, sonra ellerimizi, sonra burnumuzu ve alnımızı yere koyarız. Ellerimiz kulak hizasında, parmaklar kıbleye doğru. Üç kez “Sübhâne rabbiye’l-a‘lâ” (Yüce Rabbim, seni noksan sıfatlardan tenzih ederim) deriz.', o=['secde']),
 dict(poz='celse', b='Celse (iki secde arası)', a='“Allâhu ekber” diyerek doğrulur, dizlerimizin üstüne otururuz. Ellerimiz uyluklarımızın üstündedir. Bir “Sübhânallah” diyecek kadar bekleriz.', o=[]),
 dict(poz='secde', b='İkinci secde', a='“Allâhu ekber” diyerek tekrar secdeye gideriz ve yine üç kez “Sübhâne rabbiye’l-a‘lâ” deriz. Böylece birinci rekât bitti.', o=['secde']),
 dict(poz='kiyam', b='İkinci rekât', a='“Allâhu ekber” diyerek ayağa kalkarız. Ellerimizi bağlar, Besmele, Fâtiha ve bir sûre okuruz. Sonra yine rükû, doğrulma ve iki secde yaparız.', o=['s1','s108']),
 dict(poz='kade', b='Ka‘de (oturuş)', a='İkinci secdeden sonra otururuz. Ettehiyyâtü, Allâhümme salli, Allâhümme bârik ve Rabbenâ dualarını okuruz. “Eşhedü en lâ ilâhe illallâh” derken sağ elimizin şehâdet parmağını kaldırırız.', o=['tahiyyat','salli','barik','rabbena','rabbenagfirli']),
 dict(poz='selam1', b='Sağa selam', a='Başımızı sağa çevirip omzumuza bakarak “Esselâmü aleyküm ve rahmetullâh” deriz.', o=[]),
 dict(poz='selam2', b='Sola selam', a='Başımızı sola çevirip yine “Esselâmü aleyküm ve rahmetullâh” deriz. Namazımız bitti! Ellerimizi açıp dua ederiz. Tesbihat yapabiliriz: 33 Sübhânallah, 33 Elhamdülillah, 33 Allâhu ekber.', o=[]),
]

VAKIT = [
 ('🌄','Sabah','2 sünnet + 2 farz'),
 ('☀️','Öğle','4 sünnet + 4 farz + 2 sünnet'),
 ('🌤️','İkindi','4 sünnet + 4 farz'),
 ('🌇','Akşam','3 farz + 2 sünnet'),
 ('🌙','Yatsı','4 sünnet + 4 farz + 2 sünnet + 3 vitir'),
]

# Sûreler: Kur'an verisinden yüklenir (data/q). [sûre no, ad, kısa anlam]
SURELER = [
 (1,'Fâtiha','Açılış sûresi; her rekâtta okunur. Allah’a hamd eder, doğru yolu isteriz.'),
 (105,'Fîl','Kâbe’yi yıkmaya gelen fil ordusunu Allah’ın küçük kuşlarla durdurması.'),
 (106,'Kureyş','Mekkelilere verilen güven ve bolluk nimeti için Kâbe’nin Rabbine ibadet.'),
 (107,'Mâûn','Yetimi itmemek, yoksulu doyurmak, namazı gösteriş için kılmamak.'),
 (108,'Kevser','Kur’an’ın en kısa sûresi; Allah’ın Peygamberimize verdiği bol nimet.'),
 (109,'Kâfirûn','Herkesin dini kendisinedir; biz yalnız Allah’a ibadet ederiz.'),
 (110,'Nasr','Allah’ın yardımı ve fetih gelince Allah’ı övmek ve af dilemek.'),
 (111,'Tebbet','Peygamberimize düşmanlık eden Ebû Leheb’in sonu.'),
 (112,'İhlâs','Allah birdir, doğurmamış ve doğmamıştır; O’nun dengi yoktur.'),
 (113,'Felak','Her türlü kötülükten sabahın Rabbine sığınmak.'),
 (114,'Nâs','İnsanların kalbine vesvese veren şeytandan Allah’a sığınmak.'),
]

# Dualar. ay: âyet sesi (sûre, ilk âyet, son âyet) varsa Afâsî kaydı çalar; yoksa cihazın sesli okuması kullanılır.
DUALAR = [
 dict(id='besmele', ad='Besmele', ar='بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ', ok='Bismillâhirrahmânirrahîm.', tr='Rahmân ve Rahîm olan Allah’ın adıyla.', ay=(1,1,1)),
 dict(id='euzu', ad='Eûzü - Besmele', ar='اَعُوذُ بِاللّٰهِ مِنَ الشَّيْطَانِ الرَّجِيمِ بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ', ok='Eûzü billâhi mine’ş-şeytâni’r-racîm. Bismillâhirrahmânirrahîm.', tr='Kovulmuş şeytandan Allah’a sığınırım. Rahmân ve Rahîm olan Allah’ın adıyla.'),
 dict(id='tevhid', ad='Kelime-i Tevhid', ar='لَا اِلٰهَ اِلَّا اللّٰهُ مُحَمَّدٌ رَسُولُ اللّٰهِ', ok='Lâ ilâhe illallâh, Muhammedün rasûlullâh.', tr='Allah’tan başka ilah yoktur, Muhammed Allah’ın elçisidir.'),
 dict(id='sehadet', ad='Kelime-i Şehâdet', ar='اَشْهَدُ اَنْ لَا اِلٰهَ اِلَّا اللّٰهُ وَاَشْهَدُ اَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ', ok='Eşhedü en lâ ilâhe illallâh ve eşhedü enne Muhammeden abdühû ve rasûlüh.', tr='Allah’tan başka ilah olmadığına şahitlik ederim. Muhammed’in O’nun kulu ve elçisi olduğuna da şahitlik ederim.'),
 dict(id='subhaneke', ad='Sübhâneke', ar='سُبْحَانَكَ اللّٰهُمَّ وَبِحَمْدِكَ وَتَبَارَكَ اسْمُكَ وَتَعَالٰى جَدُّكَ وَلَا اِلٰهَ غَيْرُكَ', ok='Sübhâneke’llâhümme ve bi-hamdik, ve tebârakesmük, ve teâlâ ceddük, ve lâ ilâhe ğayrük.', tr='Allah’ım! Seni her türlü eksiklikten uzak tutar, sana hamd ederim. Senin adın mübarektir, şanın yücedir. Senden başka ilah yoktur.'),
 dict(id='ruku', ad='Rükû tesbihi', ar='سُبْحَانَ رَبِّيَ الْعَظِيمِ', ok='Sübhâne rabbiye’l-azîm.', tr='Yüce Rabbimi her türlü eksiklikten uzak tutarım.'),
 dict(id='kavme', ad='Rükûdan doğrulurken', ar='سَمِعَ اللّٰهُ لِمَنْ حَمِدَهُ رَبَّنَا لَكَ الْحَمْدُ', ok='Semi‘allâhü limen hamideh. Rabbenâ leke’l-hamd.', tr='Allah kendisine hamd edeni işitir. Rabbimiz, hamd sana mahsustur.'),
 dict(id='secde', ad='Secde tesbihi', ar='سُبْحَانَ رَبِّيَ الْاَعْلٰى', ok='Sübhâne rabbiye’l-a‘lâ.', tr='En yüce Rabbimi her türlü eksiklikten uzak tutarım.'),
 dict(id='tahiyyat', ad='Ettehiyyâtü', ar='اَلتَّحِيَّاتُ لِلّٰهِ وَالصَّلَوَاتُ وَالطَّيِّبَاتُ اَلسَّلَامُ عَلَيْكَ اَيُّهَا النَّبِيُّ وَرَحْمَةُ اللّٰهِ وَبَرَكَاتُهُ اَلسَّلَامُ عَلَيْنَا وَعَلٰى عِبَادِ اللّٰهِ الصَّالِحِينَ اَشْهَدُ اَنْ لَا اِلٰهَ اِلَّا اللّٰهُ وَاَشْهَدُ اَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ', ok='Ettehiyyâtü lillâhi ve’s-salavâtü ve’t-tayyibât. Esselâmü aleyke eyyühe’n-nebiyyü ve rahmetullâhi ve berakâtüh. Esselâmü aleynâ ve alâ ibâdillâhi’s-sâlihîn. Eşhedü en lâ ilâhe illallâh ve eşhedü enne Muhammeden abdühû ve rasûlüh.', tr='Bütün selamlar, dualar ve güzel sözler Allah’a mahsustur. Ey Peygamber! Allah’ın selamı, rahmeti ve bereketi senin üzerine olsun. Selam bizim ve Allah’ın iyi kullarının üzerine olsun. Allah’tan başka ilah olmadığına, Muhammed’in O’nun kulu ve elçisi olduğuna şahitlik ederim.'),
 dict(id='salli', ad='Allâhümme Salli', ar='اَللّٰهُمَّ صَلِّ عَلٰى مُحَمَّدٍ وَعَلٰى اٰلِ مُحَمَّدٍ كَمَا صَلَّيْتَ عَلٰى اِبْرٰهِيمَ وَعَلٰى اٰلِ اِبْرٰهِيمَ اِنَّكَ حَمِيدٌ مَجِيدٌ', ok='Allâhümme salli alâ Muhammedin ve alâ âli Muhammed. Kemâ salleyte alâ İbrâhîme ve alâ âli İbrâhîm. İnneke hamîdün mecîd.', tr='Allah’ım! Hz. İbrâhim’e ve ailesine rahmet ettiğin gibi, Hz. Muhammed’e ve ailesine de rahmet et. Şüphesiz sen övülmeye lâyıksın, şanı yücesin.'),
 dict(id='barik', ad='Allâhümme Bârik', ar='اَللّٰهُمَّ بَارِكْ عَلٰى مُحَمَّدٍ وَعَلٰى اٰلِ مُحَمَّدٍ كَمَا بَارَكْتَ عَلٰى اِبْرٰهِيمَ وَعَلٰى اٰلِ اِبْرٰهِيمَ اِنَّكَ حَمِيدٌ مَجِيدٌ', ok='Allâhümme bârik alâ Muhammedin ve alâ âli Muhammed. Kemâ bârekte alâ İbrâhîme ve alâ âli İbrâhîm. İnneke hamîdün mecîd.', tr='Allah’ım! Hz. İbrâhim’e ve ailesine bereket verdiğin gibi, Hz. Muhammed’e ve ailesine de bereket ver. Şüphesiz sen övülmeye lâyıksın, şanı yücesin.'),
 dict(id='rabbena', ad='Rabbenâ Âtinâ', ar='رَبَّنَا اٰتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْاٰخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ', ok='Rabbenâ âtinâ fi’d-dünyâ haseneten ve fi’l-âhireti haseneten ve kınâ azâbe’n-nâr.', tr='Rabbimiz! Bize dünyada da iyilik ver, âhirette de iyilik ver. Bizi cehennem azabından koru.', ay=(2,201,201)),
 dict(id='rabbenagfirli', ad='Rabbenağfirlî', ar='رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ', ok='Rabbenağfirlî ve li-vâlideyye ve li’l-mü’minîne yevme yekûmü’l-hisâb.', tr='Rabbimiz! Hesap gününde beni, annemi, babamı ve bütün müminleri bağışla.', ay=(14,41,41)),
 dict(id='kunut1', ad='Kunut Duası 1', ar='اَللّٰهُمَّ اِنَّا نَسْتَعِينُكَ وَنَسْتَغْفِرُكَ وَنَسْتَهْدِيكَ وَنُؤْمِنُ بِكَ وَنَتُوبُ اِلَيْكَ وَنَتَوَكَّلُ عَلَيْكَ وَنُثْنِي عَلَيْكَ الْخَيْرَ كُلَّهُ نَشْكُرُكَ وَلَا نَكْفُرُكَ وَنَخْلَعُ وَنَتْرُكُ مَنْ يَفْجُرُكَ', ok='Allâhümme innâ nesteînüke ve nestağfirüke ve nestehdîk. Ve nü’minü bike ve netûbü ileyk. Ve netevekkelü aleyk. Ve nüsnî aleyke’l-hayra küllehû neşkürük. Ve lâ nekfürük. Ve nahleu ve netrükü men yefcürük.', tr='Allah’ım! Senden yardım ister, bağışlanmamızı diler, doğru yola iletilmeyi isteriz. Sana inanır, sana tövbe eder, sana güveniriz. Bütün iyilikleri sana yakıştırır, seni överiz. Sana şükreder, nankörlük etmeyiz. Sana karşı geleni bırakırız.'),
 dict(id='kunut2', ad='Kunut Duası 2', ar='اَللّٰهُمَّ اِيَّاكَ نَعْبُدُ وَلَكَ نُصَلِّي وَنَسْجُدُ وَاِلَيْكَ نَسْعٰى وَنَحْفِدُ نَرْجُو رَحْمَتَكَ وَنَخْشٰى عَذَابَكَ اِنَّ عَذَابَكَ بِالْكُفَّارِ مُلْحِقٌ', ok='Allâhümme iyyâke na‘büdü ve leke nüsallî ve nescüd. Ve ileyke nes‘â ve nahfid. Nercû rahmeteke ve nahşâ azâbek. İnne azâbeke bi’l-küffâri mülhık.', tr='Allah’ım! Yalnız sana ibadet eder, senin için namaz kılar ve secde ederiz. Sana koşar, sana yöneliriz. Rahmetini umar, azabından korkarız. Senin azabın inkâr edenlere ulaşır.'),
 dict(id='amentu', ad='Âmentü', ar='اٰمَنْتُ بِاللّٰهِ وَمَلٰئِكَتِهِ وَكُتُبِهِ وَرُسُلِهِ وَالْيَوْمِ الْاٰخِرِ وَبِالْقَدَرِ خَيْرِهِ وَشَرِّهِ مِنَ اللّٰهِ تَعَالٰى وَالْبَعْثُ بَعْدَ الْمَوْتِ حَقٌّ اَشْهَدُ اَنْ لَا اِلٰهَ اِلَّا اللّٰهُ وَاَشْهَدُ اَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ', ok='Âmentü billâhi ve melâiketihî ve kütübihî ve rusülihî ve’l-yevmi’l-âhiri ve bi’l-kaderi hayrihî ve şerrihî mina’llâhi teâlâ ve’l-ba‘sü ba‘de’l-mevti hakkun. Eşhedü en lâ ilâhe illallâh ve eşhedü enne Muhammeden abdühû ve rasûlüh.', tr='Allah’a, meleklerine, kitaplarına, peygamberlerine, âhiret gününe, kadere, hayrın ve şerrin Allah’tan olduğuna inandım. Öldükten sonra dirilmek haktır. Allah’tan başka ilah olmadığına, Muhammed’in O’nun kulu ve elçisi olduğuna şahitlik ederim.'),
 dict(id='kursi', ad='Âyetü’l-Kürsî', ar=None, ok='Allâhü lâ ilâhe illâ hüve’l-hayyü’l-kayyûm. Lâ te’huzühû sinetün ve lâ nevm. Lehû mâ fi’s-semâvâti ve mâ fi’l-ard. Men zellezî yeşfeu indehû illâ bi-iznih. Ya‘lemü mâ beyne eydîhim ve mâ halfehüm. Ve lâ yuhîtûne bi-şey’in min ilmihî illâ bimâ şâ’. Vesia kürsiyyühü’s-semâvâti ve’l-ard. Ve lâ yeûdühû hıfzuhümâ. Ve hüve’l-aliyyü’l-azîm.', tr='Allah’tan başka ilah yoktur. O diridir, her şeyi ayakta tutandır. Onu ne uyuklama ne uyku tutar. Göklerde ve yerde ne varsa O’nundur. O’nun izni olmadan kim şefaat edebilir? O, insanların önlerindekini ve arkalarındakini bilir. Onlar O’nun bildirdiğinin dışında hiçbir şeyi kavrayamaz. Kürsüsü gökleri ve yeri kaplar. Onları korumak O’na ağır gelmez. O yücedir, büyüktür.', ay=(2,255,255)),
 dict(id='yunusdua', ad='Hz. Yûnus’un Duası', ar='لَا اِلٰهَ اِلَّا اَنْتَ سُبْحَانَكَ اِنِّي كُنْتُ مِنَ الظَّالِمِينَ', ok='Lâ ilâhe illâ ente sübhâneke innî küntü mine’z-zâlimîn.', tr='Senden başka ilah yoktur. Seni her türlü eksiklikten uzak tutarım. Ben kendime yazık edenlerden oldum.'),
 dict(id='yemek', ad='Yemek Duası', ar='اَلْحَمْدُ لِلّٰهِ الَّذِي اَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مِنَ الْمُسْلِمِينَ', ok='Elhamdülillâhillezî et‘amenâ ve sekânâ ve cealenâ mine’l-müslimîn.', tr='Bizi yediren, içiren ve Müslümanlardan kılan Allah’a hamd olsun.'),
 dict(id='uyku', ad='Uyku Duası', ar='اَللّٰهُمَّ بِاسْمِكَ اَمُوتُ وَاَحْيَا', ok='Allâhümme bismike emûtü ve ahyâ.', tr='Allah’ım! Senin adınla ölür (uyur) ve dirilirim (uyanırım).'),
 dict(id='ilim', ad='İlim Duası', ar='رَبِّ زِدْنِي عِلْمًا', ok='Rabbi zidnî ilmâ.', tr='Rabbim! İlmimi artır.'),
]
# Hz. Yûnus’un duası Enbiyâ 87’nin bir parçasıdır; âyetin tamamı daha uzun olduğu için sesli okuma cihazdan yapılır.

DOGRU_YANLIS = [
 ('Yemeğe başlarken “Bismillah” deriz.', 1),
 ('Büyükler konuşurken sözlerini keseriz.', 0),
 ('Kardeşine gülümsemek sadakadır.', 1),
 ('Arkadaşımızın eşyasını izinsiz alabiliriz.', 0),
 ('Kapıyı çalıp izin istedikten sonra odaya gireriz.', 1),
 ('Suyu boşa akıtmak israftır.', 1),
 ('Hayvanlara taş atmak eğlencelidir.', 0),
 ('Selamı önce veren daha çok sevap kazanır.', 1),
 ('Yalan söylemek bazen iyidir, kimse anlamazsa sorun yok.', 0),
 ('Komşumuz hastaysa onu ziyaret ederiz.', 1),
 ('Öfkelenince oturur, gerekirse abdest alırız.', 1),
 ('Emanet aldığımız kitabı kirletip geri vermeyiz, saklarız.', 0),
 ('Yaşlı birine otobüste yer veririz.', 1),
 ('Yemeği beğenmezsek bağırarak ayıplarız.', 0),
 ('Bize iyilik edene teşekkür ederiz.', 1),
 ('Çöpümüzü parka atabiliriz, nasılsa biri toplar.', 0),
 ('Sağ elimizle ve önümüzden yeriz.', 1),
 ('Küs kaldığımız arkadaşımızla üç günden fazla konuşmamalıyız.', 0),
 ('Anne-babamıza “of” bile demeyiz.', 1),
 ('Dua sadece Arapça yapılabilir.', 0),
]

HAFIZA = [
 ('🕌','Namaz'),('🌅','Oruç'),('🎁','Zekât'),('🕋','Hac'),('📖','Kur’an'),('✨','Melek'),('💧','Abdest'),('🤲','Dua'),
 ('🌙','Ramazan'),('📢','Ezan'),('🌹','Peygamber'),('🧭','Kıble'),
]
