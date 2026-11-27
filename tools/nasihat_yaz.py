# data/nasihat.json üretir: günün nasihati (açılış ekranı) ve Nasihatler kitabı (nasihat.html).
# Her kayıt: b başlık, n âyet/hadis meali (sade Türkçe), k kaynak, s kısa açıklama. Sıra = gün sırası.
import json,os
N=[
("Niyet","Ameller ancak niyetlere göredir; herkese niyet ettiği şey vardır.","Buhârî, Bed’ü’l-vahy 1; Müslim, İmâre 155","Güne başlarken yaptığın işleri Allah rızasına bağla. Aynı iş, niyetle ibadete dönüşür."),
("Salavat","Kim bana bir salavat getirirse Allah da ona on rahmet eder.","Müslim, Salât 70","Bir salavat az bir sözdür ama karşılığı büyüktür. Dilini gün boyu salavatla meşgul et."),
("İlk hesap","Kıyamet günü kulun ilk hesaba çekileceği ameli namazdır; o düzgün çıkarsa diğer amelleri de düzgün çıkar.","Tirmizî, Salât 188; Nesâî, Salât 9","Namaz, diğer amellerin terazisidir. Vaktini, abdestini ve huşûunu koru."),
("Beş vakit","Kapınızın önünden bir nehir aksa ve her gün beş defa yıkansanız üzerinizde kir kalır mı? Beş vakit namaz da böyledir; Allah onlarla günahları siler.","Buhârî, Mevâkît 6; Müslim, Mesâcid 283","Her namaz bir arınmadır. Bir vakti kaçırmak, o temizlikten mahrum kalmaktır."),
("Az ama devamlı","Allah katında amellerin en sevimlisi, az da olsa devamlı olanıdır.","Buhârî, Rikak 18; Müslim, Müsâfirîn 218","Büyük ama kısa süren hevesler yerine küçük ve sürekli bir vird edin: birkaç âyet, birkaç tesbih."),
("Kur’an","Sizin en hayırlınız Kur’an’ı öğrenen ve öğretendir.","Buhârî, Fezâilü’l-Kur’ân 21","Bugün Kur’an’dan bir şey öğren ya da bildiğini birine öğret; ikisi de hayırdır."),
("Faydasızı bırakmak","Kişinin kendisini ilgilendirmeyen şeyleri bırakması, Müslümanlığının güzelliğindendir.","Tirmizî, Zühd 11; İbn Mâce, Fiten 12","Vaktini ve dilini sana fayda vermeyen işlerden koru; ömür sermayedir."),
("Kardeşini sevmek","Sizden biri kendisi için istediğini kardeşi için de istemedikçe (kâmil) iman etmiş olmaz.","Buhârî, Îmân 7; Müslim, Îmân 71","Kendine dilediğin hayrı kardeşine de dile; kıskançlığın ilacı duadır."),
("Dil","Allah’a ve âhiret gününe iman eden ya hayır söylesin ya da sussun.","Buhârî, Edeb 31; Müslim, Îmân 74","Konuşmadan önce düşün: Bu söz hayır mı? Değilse susmak da bir ibadettir."),
("Öfke","Güçlü kimse güreşte yenen değil, öfkelendiğinde kendine hâkim olandır.","Buhârî, Edeb 76; Müslim, Birr 107","Öfkelendiğinde sus, abdest al, yerini değiştir. Kendine hâkim olmak en büyük güçtür."),
("Kolaylaştırmak","Kolaylaştırın, zorlaştırmayın; müjdeleyin, nefret ettirmeyin.","Buhârî, İlim 11; Müslim, Cihâd 8","Dini anlatırken ve insanlarla muamelede yumuşak ol; sertlik kapıları kapatır."),
("Takva ve güzel ahlak","Nerede olursan ol Allah’tan kork. Kötülüğün ardından bir iyilik yap ki onu silsin. İnsanlara güzel ahlakla davran.","Tirmizî, Birr 55","Hatanın ardından hemen bir iyilik yap: bir sadaka, bir tövbe, bir güzel söz."),
("Sağlık ve vakit","İki nimet vardır ki insanların çoğu onlarda aldanmıştır: sağlık ve boş vakit.","Buhârî, Rikak 1","Sağlıklıyken ve vaktin varken hayrı erteleme; ikisi de bir gün elden gider."),
("Tebessüm","Kardeşinin yüzüne gülümsemen senin için bir sadakadır.","Tirmizî, Birr 36","Sadaka yalnız para değildir. Güler yüz, güzel söz ve yol göstermek de sadakadır."),
("Temizlik","Temizlik imanın yarısıdır.","Müslim, Tahâret 1","Bedenini, elbiseni, evini ve kalbini temiz tut; namaz temizlikle başlar."),
("Yolcu gibi","Dünyada bir garip ya da bir yolcu gibi ol.","Buhârî, Rikak 3","Yolcu yükünü hafif tutar ve varacağı yeri unutmaz. Dünyayı ahiretin yolu bil."),
("Elinden ve dilinden","Müslüman, Müslümanların elinden ve dilinden emin olduğu kimsedir.","Buhârî, Îmân 4; Müslim, Îmân 64","Bugün kimse senin elinden ve dilinden incinmesin; ibadetin güzelliği ahlakta görünür."),
("Kalbe bakar","Allah sizin dış görünüşünüze ve mallarınıza bakmaz; kalplerinize ve amellerinize bakar.","Müslim, Birr 34","Görünüşü değil kalbi düzeltmeye çalış; Allah’ın nazar ettiği yer orasıdır."),
("Secde","Kulun Rabbine en yakın olduğu an secde hâlidir; secdede duayı çoğaltın.","Müslim, Salât 215","Secdeyi aceleye getirme; derdini, şükrünü ve dileğini orada Rabbine aç."),
("Merhamet","Merhamet etmeyene merhamet olunmaz.","Buhârî, Edeb 18; Müslim, Fezâil 65","Çocuğa, yaşlıya, hayvana ve hataya düşene merhametle bak; rahmet merhamete iner."),
("Dua","Dua ibadetin ta kendisidir.","Tirmizî, Daavât 1; Ebû Dâvûd, Vitir 23","Duayı yalnız sıkıntıda değil her an et; dua kulluğun ifadesidir."),
("Hayâ","Hayâ imandandır.","Buhârî, Îmân 3; Müslim, Îmân 57","Hayâ insanı kötülükten alıkoyan bir perdedir; onu yırtacak söz ve bakıştan sakın."),
("Güzel ahlak","Müminlerin iman bakımından en olgunu, ahlakı en güzel olanıdır.","Ebû Dâvûd, Sünnet 15; Tirmizî, Radâ 11","İmanın ölçüsü ahlakta görünür. Evde, işte ve yolda aynı güzel insan ol."),
("Namaz alıkoyar","Namazı dosdoğru kıl. Şüphesiz namaz hayâsızlıktan ve kötülükten alıkoyar.","Ankebût, 29/45","Namaz kıldığın hâlde kötülükten uzaklaşamıyorsan namazının huşûuna bak."),
("Kalplerin huzuru","Bilin ki kalpler ancak Allah’ı anmakla huzura kavuşur.","Ra‘d, 13/28","Daralan kalbin ilacı zikirdir. Namazın ardından tesbihatı bırakma."),
("Sabır ve namaz","Sabır ve namazla Allah’tan yardım isteyin.","Bakara, 2/45","Sıkıntıda önce namaza dur; Peygamberimiz bir iş onu üzdüğünde namaza koşardı."),
("Zorlukla kolaylık","Şüphesiz zorlukla beraber bir kolaylık vardır. Evet, zorlukla beraber bir kolaylık vardır.","İnşirâh, 94/5-6","Hiçbir darlık kalıcı değildir; ümidini kesme, çabanı bırakma."),
("Anne baba","Rabbin, yalnız kendisine ibadet etmenizi ve anne babaya iyilik etmenizi emretti.","İsrâ, 17/23","Bugün anne babanı ara, onlara dua et; hayatta değillerse onlar için Kur’an oku."),
("Cemaat","Cemaatle kılınan namaz, tek başına kılınandan yirmi yedi derece daha faziletlidir.","Buhârî, Ezân 30; Müslim, Mesâcid 249","Fırsat buldukça camiye git; cemaat hem sevabı hem kardeşliği artırır."),
("Kardeşe yardım","Kul, kardeşinin yardımında olduğu sürece Allah da onun yardımındadır.","Müslim, Zikir 38","Bir kardeşinin işini kolaylaştır; Allah da senin işini kolaylaştırır."),
("En sevimli amel","Allah’a en sevimli amel, vaktinde kılınan namaz; sonra anne babaya iyilik; sonra Allah yolunda gayrettir.","Buhârî, Mevâkît 5; Müslim, Îmân 137","Namazı vaktin başında kılmaya gayret et; ertelemek çoğu zaman kaçırmaya götürür."),
]
# Büyüklerin sözleri: (kim, başlık, söz, kaynak, kısa açıklama). Kaynağı kesin olmayanlarda "nispet edilir" yazılır.
S=[
("Hz. Ömer","Kendini hesaba çek","Hesaba çekilmeden önce kendinizi hesaba çekin; tartılmadan önce amellerinizi tartın.","Tirmizî, Kıyâmet 25","Her akşam günün muhasebesini yap: neyi iyi yaptın, neyi düzeltmelisin."),
("Hz. Ali","İnsanın değeri","Her insanın değeri, iyi yaptığı iştedir.","Nehcü’l-belâğa, Hikem 81","İşini güzel yap; insanın kıymeti makamında değil, emeğinin güzelliğindedir."),
("Hasan-ı Basrî","Günler","Ey Âdemoğlu! Sen ancak günlerden ibaretsin; bir gün gittiğinde senden bir parça da gitmiş olur.","Ebû Nuaym, Hilyetü’l-evliyâ","Bugün ömrünün bir parçasıdır; onu boşa harcama."),
("Hasan-ı Basrî","Üç gün","Dünya üç gündür: dün geçti, yarına belki yetişmezsin; senin olan bugündür.","Hasan-ı Basrî’ye nispet edilir","Tövbeyi ve hayrı yarına bırakma; elindeki tek gün bugündür."),
("Fudayl b. İyâz","İhlas","İnsanlar için ameli terk etmek riyadır; insanlar için amel etmek şirktir. İhlas, Allah’ın seni bu ikisinden korumasıdır.","Kuşeyrî, er-Risâle, İhlâs bâbı","Görülmek için yapma, görülürüm diye de bırakma; yalnız Allah için yap."),
("Süfyân-ı Sevrî","Niyet","Niyetimden daha zor tedavi ettiğim bir şey olmadı; çünkü o bana karşı dönüp durur.","Süfyân-ı Sevrî’ye nispet edilir","Niyet bir kere düzeltilip bırakılmaz; her işte yeniden tazelenir."),
("Abdullah b. Mübârek","Niyetin gücü","Nice küçük amel vardır ki niyet onu büyütür; nice büyük amel vardır ki niyet onu küçültür.","İbn Receb, Câmiu’l-ulûm ve’l-hikem","Küçük bir iyiliği hafife alma; güzel niyetle büyür."),
("Abdullah b. Mübârek","Edep","Çok ilimden ziyade, az bir edebe daha çok muhtacız.","Abdullah b. Mübârek’e nispet edilir","İlim edeple güzelleşir; edepsiz ilim sahibini de başkasını da yorar."),
("İmam Ebû Hanîfe","Fıkıh","Fıkıh, kişinin lehine ve aleyhine olanı bilmesidir.","Sadrüşşerîa, et-Tavzîh","Dinini öğrenmek, neyin sana fayda neyin zarar verdiğini bilmektir."),
("İmam Mâlik","Ümmetin ıslahı","Bu ümmetin sonu, ancak evvelini ıslah eden şeyle ıslah olur.","Kādî Iyâz, eş-Şifâ","İlk neslin yolu Kitap ve sünnetti; düzelmek isteyen oraya döner."),
("İmam Mâlik","İlim nurdur","İlim çok rivayet etmek değildir; ilim, Allah’ın kalbe koyduğu bir nurdur.","İmam Mâlik’e nispet edilir","Bilgiyi yığmak yetmez; onu kalbe indiren takva ve amel olur."),
("İmam Şâfiî","Hafıza","Vekî‘a hafızamın zayıflığını şikâyet ettim; bana günahları bırakmamı öğütledi ve dedi ki: İlim bir nurdur, Allah’ın nuru günahkâra verilmez.","İmam Şâfiî, Dîvân","Ders aklında kalmıyorsa önce kalbini temizle; günah ilmin önünde perdedir."),
("İmam Şâfiî","Görüş ve hakikat","Görüşüm doğrudur ama yanlış olabilir; bana muhalif olanın görüşü yanlıştır ama doğru olabilir.","İmam Şâfiî’ye nispet edilir","Tartışırken kendi görüşüne de karşındakine de insafla bak."),
("İmam Ahmed b. Hanbel","Ömür boyu ilim","Hokkadan kabre kadar.","İbnü’l-Cevzî, Menâkıbü’l-İmâm Ahmed","İlim öğrenmenin yaşı yoktur; kalem ancak kabirde bırakılır."),
("Cüneyd-i Bağdâdî","Kitap ve sünnet","Bu ilmimiz Kitap ve sünnetle bağlıdır. Kur’an’ı ezberlemeyen ve hadis yazmayana bu işte uyulmaz.","Kuşeyrî, er-Risâle","Tasavvuf, şeriatın dışında değil, onun özünde bir yoldur."),
("Bâyezîd-i Bistâmî","Kerametin ölçüsü","Havada bağdaş kurup oturan birini görseniz bile, emir ve yasaklara nasıl uyduğuna bakmadıkça ona aldanmayın.","Kuşeyrî, er-Risâle","Ölçü harikalar değil, dosdoğru bir kulluktur."),
("Sehl b. Abdullah et-Tüsterî","Yolun esasları","Yolumuzun esasları yedidir: Kitaba sarılmak, sünnete uymak, helal yemek, eziyet etmemek, günahlardan sakınmak, tövbe ve hakları ödemek.","Sülemî, Tabakātü’s-sûfiyye","Bu yedi esası günlük hayatında bir bir yokla."),
("Râbia el-Adeviyye","Allah için","Allah’ım, sana cehennem korkusundan ibadet ediyorsam beni onda yak; cennet umudundan ediyorsam beni ondan mahrum et. Yalnız senin için ediyorsam, cemalini benden esirgeme.","Ferîdüddîn Attâr, Tezkiretü’l-evliyâ","Kulluğun en yükseği, karşılık beklemeden sevgiyle yapılanıdır."),
("İmam Gazâlî","İlim ve amel","Amelsiz ilim delilik, ilimsiz amel boşunadır.","Gazâlî, Eyyühe’l-veled","Öğrendiğinle amel et; amel ettikçe Allah bilmediğini de öğretir."),
("İmam Gazâlî","Kendini bilmek","Kendini bilmek, Rabbini bilmenin anahtarıdır.","Gazâlî, Kîmyâ-yı Saâdet","Nefsini, zaafını ve muhtaçlığını tanıyan, Rabbinin kudretini ve rahmetini tanır."),
("İbn Atâullah el-İskenderî","Amelin ruhu","Ameller dikilmiş suretlerdir; onların ruhu, içlerindeki ihlas sırrıdır.","İbn Atâullah, el-Hikem, 10","İbadetin şekli kadar içini de gözet; ruhsuz suret ayakta durmaz."),
("İbn Atâullah el-İskenderî","Duanın gecikmesi","İstediğinin gecikmesi seni ümitsizliğe düşürmesin; Allah sana senin seçtiğin vakitte değil, kendi seçtiği vakitte icabet etmeyi tekeffül etmiştir.","İbn Atâullah, el-Hikem, 6","Duana cevap gecikirse bil ki en hayırlı vakit hazırlanıyor."),
("İbn Atâullah el-İskenderî","Rızık ve kulluk","Senin için garanti edilen rızık için çabalayıp senden istenen kullukta gevşek davranman, basiretinin bulandığının işaretidir.","İbn Atâullah, el-Hikem, 5","Rızkı Allah üstlendi; sen üzerine düşen kulluğa bak."),
("Mevlânâ Celâleddîn-i Rûmî","Ney","Dinle, bu ney nasıl şikâyet ediyor, ayrılıkları nasıl anlatıyor.","Mesnevî, I/1","İnsan da aslından ayrı düşmüş bir ney gibidir; onun iniltisi Rabbine özlemdir."),
("Mevlânâ Celâleddîn-i Rûmî","Kur’an’ın bendesi","Yaşadıkça ben Kur’an’ın kölesiyim; ben Muhammed Muhtâr’ın yolunun toprağıyım.","Mevlânâ, Rubâiyyât","Mevlânâ’nın yolu Kur’an ve sünnetin yoludur; onu bundan ayırmak ona haksızlıktır."),
("Ahmed Yesevî","Gönül incitmemek","Sünnettir: kâfir de olsa incitme; gönlü katı, gönül incitenden Hak bîzardır.","Ahmed Yesevî, Dîvân-ı Hikmet","Sözün sertliği gönülleri kırar; dili tatlı olan gönülleri kazanır."),
("Yunus Emre","Gönül","Bir kez gönül yıktın ise, bu kıldığın namaz değil; yetmiş iki millet dahi elin yüzün yumaz değil.","Yunus Emre, Dîvân","Namaz gönül kırmanın kefareti değildir; kul hakkını gözet."),
("Yunus Emre","Tanış olalım","Gelin tanış olalım, işi kolay kılalım; sevelim sevilelim, dünya kimseye kalmaz.","Yunus Emre, Dîvân","Küskünlüğü uzatma; dünya kısa, sevgi kalıcıdır."),
("Yunus Emre","İlim","İlim ilim bilmektir, ilim kendin bilmektir; sen kendini bilmezsin, ya nice okumaktır.","Yunus Emre, Dîvân","Okuduğun kitap seni sana tanıtmıyorsa eksik okuyorsun."),
("Yunus Emre","Mal da yalan","Mal sahibi mülk sahibi, hani bunun ilk sahibi? Mal da yalan mülk de yalan, var biraz da sen oyalan.","Yunus Emre, Dîvân","Elindekiler emanettir; onlara gönül bağlama."),
("Hacı Bayram-ı Velî","Kendini bilmek","Bilmek istersen seni, can içre ara canı; geç canından bulasın, sen seni bilesin seni.","Hacı Bayram-ı Velî, İlâhî","Kendini bulmak, nefsin isteklerini aşmakla olur."),
("Hacı Bektâş-ı Velî","Üç emanet","Eline, diline, beline sahip ol.","Hacı Bektâş-ı Velî’ye nispet edilir","Harama uzanmayan el, yalan söylemeyen dil, iffetli bir hayat: edebin özü budur."),
("Bahâeddîn Nakşibend","El işte, gönül Hak’ta","Dest be kâr, dil be yâr: el işte, gönül Allah’ta.","Nakşibendî büyüklerine nispet edilir","Çalışırken de zikretmek mümkündür; kalp Allah’la, el helal kazançla meşgul olsun."),
("Ebu’l-Hasan Harakānî","Kapıya gelen","Bu kapıya gelene ekmeğini verin, imanını sormayın; Allah katında can bulan, Ebu’l-Hasan’ın sofrasında ekmeği elbette bulur.","Ebu’l-Hasan Harakānî’ye nispet edilir","İyilik yaparken insanları ayırma; ikram, gönülleri açar."),
("Şeyh Sa‘dî-i Şîrâzî","İnsanlar bir bedendir","İnsanoğulları birbirinin uzuvlarıdır, çünkü yaratılışta bir cevherdendirler. Zaman bir uzvu ağrıttı mı, öbür uzuvlara da huzur kalmaz.","Sa‘dî, Gülistan, I","Kardeşinin derdini kendi derdin bil; ümmet tek bir beden gibidir."),
]
# İLİM VE OKUMAK: (kim — boşsa âyet/hadis, başlık, metin, kaynak, kısa açıklama). Günlük sırada ağırlık bunlardadır.
IL=[
("","Oku","Yaratan Rabbinin adıyla oku! O, insanı bir kan pıhtısından yarattı. Oku! Rabbin en cömert olandır; kalemle öğreten O’dur, insana bilmediğini öğretti.","Alak, 96/1-5","İlk inen emir “oku”dur. Bugün bir sayfa da olsa ilim için oku."),
("","Bilen ve bilmeyen","Hiç bilenlerle bilmeyenler bir olur mu?","Zümer, 39/9","Bilgi insanı yükseltir; cehaleti kader sanma, öğrenmeye başla."),
("","İlmimi artır","Rabbim, ilmimi artır.","Tâhâ, 20/114","Allah, Peygamberine bile ilmin artmasını istemeyi öğretti. Bu duayı dilinden düşürme."),
("","Derecelerle yükseltir","Allah içinizden iman edenleri ve kendilerine ilim verilenleri derecelerle yükseltir.","Mücâdele, 58/11","İman ve ilim bir araya gelince insanı yükselten iki kanat olur."),
("","Âlimlerin haşyeti","Kulları içinde Allah’tan ancak âlimler hakkıyla korkar.","Fâtır, 35/28","Gerçek ilim insanı kibre değil, Allah’a saygıya ve tevazua götürür."),
("","Kaleme yemin","Nûn. Kaleme ve yazdıklarına andolsun.","Kalem, 68/1","Allah’ın kaleme yemin etmesi yazının ve ilmin değerini gösterir. Not alarak oku."),
("","Bilenlere sorun","Bilmiyorsanız bilenlere sorun.","Nahl, 16/43","Bilmediğini sormak ayıp değil, ilmin kapısıdır."),
("","Hikmet","Kime hikmet verilmişse, ona pek çok hayır verilmiştir.","Bakara, 2/269","Hikmet, bilgiyi yerli yerinde kullanmaktır; onu Allah’tan iste."),
("","Düşünenler","Göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardınca gelişinde akıl sahipleri için deliller vardır.","Âl-i İmrân, 3/190","Kâinat da okunacak bir kitaptır; tefekkür ederek bak."),
("","Beyanı öğretti","Rahmân, Kur’an’ı öğretti; insanı yarattı, ona beyanı öğretti.","Rahmân, 55/1-4","Konuşma ve anlatma gücü bir emanettir; onu ilimle süsle."),
("","İsimleri öğretti","Allah Âdem’e bütün isimleri öğretti.","Bakara, 2/31","İnsanı meleklerden üstün kılan ilk şey öğrenme kabiliyetidir."),
("","Ancak âlimler anlar","Bu misalleri insanlara veriyoruz; onları ancak bilenler anlar.","Ankebût, 29/43","Kur’an’ın derinliği okuyup düşündükçe açılır."),
("","Bilmediğin şey","Hakkında bilgin olmayan şeyin ardına düşme.","İsrâ, 17/36","Duyduğunu araştırmadan söyleme ve uygulama; önce öğren."),
("","Her bilenin üstünde","Her bilenin üstünde daha iyi bilen biri vardır.","Yûsuf, 12/76","Ne kadar öğrenirsen öğren, öğrenci kalmayı bırakma."),
("","Mûsâ ve Hızır","Sana öğretilen doğru bilgiden bana da öğretmen için sana uyabilir miyim?","Kehf, 18/66","Bir peygamber bile ilim için yola çıktı ve hocasına edeple sordu."),
("","Düşünmezler mi","Kur’an’ı hiç düşünmüyorlar mı?","Muhammed, 47/24","Okumak yetmez; ayetler üzerinde durup düşünmek de istenir."),
("","Mübarek kitap","Bu, âyetlerini düşünsünler ve akıl sahipleri öğüt alsınlar diye sana indirdiğimiz mübarek bir kitaptır.","Sâd, 38/29","Her gün birkaç âyeti meali ve tefsiriyle düşünerek oku."),
("","İlim farzdır","İlim öğrenmek her Müslümana farzdır.","İbn Mâce, Mukaddime 17","Dinini, işini ve sorumluluklarını bilmek her Müslümanın görevidir."),
("","Cennete yol","Kim ilim öğrenmek için bir yola girerse, Allah ona cennete giden yolu kolaylaştırır.","Müslim, Zikir 38","Derse giden her adım, kitaba açılan her sayfa cennete bir adımdır."),
("","Dinde anlayış","Allah kimin hayrını dilerse onu dinde derin anlayış sahibi kılar.","Buhârî, İlim 13; Müslim, Zekât 98","İlme yönelmek, Allah’ın senin için hayır dilediğinin işaretidir."),
("","Kesilmeyen amel","İnsan ölünce ameli kesilir; ancak üç şey müstesna: sadaka-i câriye, faydalanılan ilim ve kendisine dua eden hayırlı evlat.","Müslim, Vasıyyet 14","Öğrettiğin ilim, sen gittikten sonra da sevap yazdırmaya devam eder."),
("","Peygamberlerin vârisleri","Âlimler peygamberlerin vârisleridir. Peygamberler miras olarak altın ve gümüş bırakmadılar; ilim bıraktılar. Onu alan büyük bir pay almıştır.","Ebû Dâvûd, İlim 1; Tirmizî, İlim 19","Gerçek miras ilimdir; ondan payını almak için okumaya devam et."),
("","Ay ve yıldızlar","Âlimin âbide üstünlüğü, dolunayın diğer yıldızlara üstünlüğü gibidir.","Ebû Dâvûd, İlim 1; Tirmizî, İlim 19","İbadet kendine, ilim başkalarına da ışık olur."),
("","Allah yolunda","İlim talebi için evinden çıkan kimse, dönünceye kadar Allah yolundadır.","Tirmizî, İlim 2","Ders yolculuğu bir ibadet yolculuğudur; niyetini öyle kur."),
("","Faydasız ilim","Allah’ım, fayda vermeyen ilimden sana sığınırım.","Müslim, Zikir 73","İlmin değeri faydasıyla ölçülür; seni Allah’a yaklaştırmayan bilgiden sakın."),
("","Faydalı ilim duası","Allah’ım, bana öğrettiklerinle beni faydalandır, bana fayda verecek olanı öğret ve ilmimi artır.","Tirmizî, Daavât 128; İbn Mâce, Mukaddime 23","Derse başlarken bu duayı oku."),
("","Hikmet müminin yitiğidir","Hikmetli söz müminin yitiğidir; onu nerede bulursa almaya en layık olan odur.","Tirmizî, İlim 19","Faydalı bilgiyi kimden gelirse gelsin al; ölçün Kitap ve sünnet olsun."),
("","Bir âyet de olsa","Benden bir âyet de olsa tebliğ edin.","Buhârî, Enbiyâ 50","Öğrendiğini paylaş; ilim öğretildikçe çoğalır."),
("","Yüzü ağarsın","Benden bir söz işitip ezberleyen ve onu duyduğu gibi başkasına ulaştıranın Allah yüzünü ağartsın.","Tirmizî, İlim 7; Ebû Dâvûd, İlim 10","Duyduğunu doğru aktarmak da ilmin emanetidir."),
("","Gıpta","Yalnız iki kişiye gıpta edilir: Allah’ın mal verip hak yolunda harcattığı kişiye ve Allah’ın hikmet verip onunla hükmeden ve onu öğreten kişiye.","Buhârî, İlim 15","Kıskanacaksan ilim öğretenin hâline gıpta et."),
("","Hayra vesile","Hayra vesile olan, onu yapan gibidir.","Tirmizî, İlim 14","Birine kitap hediye et, bir derse götür; onun öğrendiğinden sana da sevap var."),
("","Kur’an şefaatçidir","Kur’an okuyun; çünkü o kıyamet günü okuyanlarına şefaatçi olarak gelecektir.","Müslim, Müsâfirîn 252","Her gün Kur’an’dan bir miktar oku; az da olsa devam ettir."),
("","Zorlanarak okuyan","Kur’an’ı güzel okuyan, değerli meleklerle beraberdir. Zorlanarak, kekeleyerek okuyana ise iki sevap vardır.","Buhârî, Tefsîr (Abese) 1; Müslim, Müsâfirîn 244","Zorlanıyorsan bırakma; zorlanmanın da ayrı bir sevabı var."),
("","Her harfe on sevap","Kim Allah’ın kitabından bir harf okursa ona bir iyilik vardır; her iyilik on misliyledir.","Tirmizî, Fezâilü’l-Kur’ân 16","Okuduğun her harf hesaba yazılır; okumayı küçümseme."),
("","İlim meclisi","Bir topluluk Allah’ın evlerinden birinde toplanıp Allah’ın kitabını okur ve aralarında müzakere ederse, üzerlerine sekînet iner, rahmet onları kaplar.","Müslim, Zikir 38","Bir ders halkasına katıl; birlikte okumanın bereketi büyüktür."),
("","Âlim ve öğrenci","Dünya ve içindekiler değersizdir; ancak Allah’ın zikri, ona yaklaştıranlar, âlim ve ilim öğrenen müstesna.","Tirmizî, Zühd 14; İbn Mâce, Zühd 3","Ya öğreten ya öğrenen ol; ikisi de değerlidir."),
("","İlmi gizlemek","Kendisine bildiği bir ilim sorulup da onu gizleyene kıyamet günü ateşten bir gem vurulur.","Ebû Dâvûd, İlim 9; Tirmizî, İlim 3","Bildiğini, ihtiyacı olana cömertçe öğret."),
("","Önce ilim","Söz ve amelden önce ilim gelir.","Buhârî, İlim 10 (bab başlığı)","Bir işe başlamadan önce onun bilgisini edin."),
("Hz. Ali","İlim maldan hayırlıdır","İlim maldan hayırlıdır: ilim seni korur, malı ise sen korursun. Mal harcadıkça azalır, ilim harcadıkça artar.","Nehcü’l-belâğa, Hikem 147","Paranı biriktirdiğin gibi ilmini de biriktir; o seni korur."),
("Hz. Ali","Üç kısım insan","İnsanlar üç kısımdır: Rabbânî âlim, kurtuluş yolundaki öğrenci ve her sesin peşine takılan başıboşlar.","Nehcü’l-belâğa, Hikem 147","Âlim olamıyorsan bile öğrenci ol; başıboş kalma."),
("Hz. Ömer","Öğrenin","İlim öğrenin; ilim için vakar ve sükûneti de öğrenin. Öğrendiğiniz kimselere karşı alçak gönüllü olun.","Hz. Ömer’e nispet edilir","İlim edeple ve hocaya saygıyla öğrenilir."),
("Muâz b. Cebel","İlmin hâlleri","İlim öğrenin; Allah için öğrenmek haşyettir, talep etmek ibadettir, müzakeresi tesbihtir, araştırması cihattır, bilmeyene öğretmek sadakadır.","İbn Abdilber, Câmiu beyâni’l-ilm","İlimle geçen her an bir ibadettir."),
("Ebü’d-Derdâ","Beşincisi olma","Ya âlim ol, ya öğrenci, ya dinleyici ya da onları seven; beşincisi olma, helâk olursun.","İbn Abdilber, Câmiu beyâni’l-ilm","İlimle bağını hiç koparma; en azından ilim ehlini sev."),
("İbn Abbâs","Gecenin bir saati","Gecenin bir saatinde ilim müzakere etmek, bütün geceyi ibadetle geçirmekten bana daha sevimlidir.","Dârimî, Mukaddime","Akşamları bir saati ilme ayır."),
("Hasan-ı Basrî","İki ilim","İlim ikidir: dilde kalan ilim, Allah’ın insana karşı delilidir; kalbe inen ilim ise faydalı ilimdir.","Dârimî, Mukaddime","Öğrendiğini kalbine indir; sadece dilde kalmasın."),
("İmam Ebû Hanîfe","Âlimlerin hayatı","Âlimlerin hayat hikâyeleri bana fıkıh meselelerinin çoğundan daha sevimlidir; çünkü onlar o âlimlerin edebidir.","İbn Abdilber, Câmiu beyâni’l-ilm","Büyüklerin hayatını oku; edep onların yaşayışından öğrenilir."),
("İmam Ebû Yûsuf","Bütününü ver","İlim, sen ona bütününü vermedikçe sana bir parçasını bile vermez.","İmam Ebû Yûsuf’a nispet edilir","İlim gönül vermeyi ister; dağınık çaba az ürün verir."),
("İmam Mâlik","İlme gidilir","İlim ziyaret edilir, kendisi ziyarete gitmez.","İmam Mâlik’e nispet edilir","Bilgi ayağına gelmez; kitabı aç, derse git, hocayı ara."),
("İmam Şâfiî","Altı şart","Kardeşim, ilmi ancak altı şeyle elde edersin: zekâ, istek, gayret, azık, hocanın yanında bulunmak ve uzun zaman.","İmam Şâfiî, Dîvân","Sabırsızlanma; ilim uzun soluklu bir yolculuktur."),
("İmam Şâfiî","Kur’an’ı öğrenen","Kur’an’ı öğrenenin kıymeti büyür; hadis yazanın delili güçlenir; ilmini korumayanı ilmi korumaz.","Beyhakî, Menâkıbü’ş-Şâfiî","Öğrendiğini tekrar ederek ve amel ederek koru."),
("İmam Ahmed b. Hanbel","Ekmekten çok","İnsanlar ilme, yemeye ve içmeye muhtaç olduklarından daha çok muhtaçtır; çünkü yemek günde bir iki kez gerekir, ilim ise her nefeste.","İbnü’l-Kayyim, Medâricü’s-sâlikîn","Bedenini doyurduğun gibi aklını ve kalbini de besle."),
("Abdullah b. Mübârek","Ne zamana kadar","Kendisine ne zamana kadar ilim yazacağı sorulunca: Belki kurtuluşum henüz yazmadığım bir kelimededir, dedi.","Abdullah b. Mübârek’e nispet edilir","Öğrenmeye “yeter” deme; faydalı bir söz hayatını değiştirebilir."),
("Süfyân-ı Sevrî","En faziletli amel","Niyeti düzgün olursa, ilim talebinden daha faziletli bir amel bilmiyorum.","Süfyân-ı Sevrî’ye nispet edilir","İlmi Allah rızası için öğrendiğinde en büyük ibadetlerden olur."),
("İmam Gazâlî","Ağaç ve meyve","İlim ağaca, amel meyveye benzer; meyvesiz ağaç işe yaramaz.","İmam Gazâlî’ye nispet edilir","Okuduğundan bugün bir şeyi hayatına geçir."),
("Burhâneddîn ez-Zernûcî","İlme saygı","Talebe ancak ilme, ilim ehline ve kitaba saygı göstermekle ilme ulaşır ve ondan faydalanır.","Zernûcî, Ta‘lîmü’l-müteallim, IV. fasıl","Kitabı yere koyma, hocanı incitme; saygı ilmin kapısını açar."),
("Burhâneddîn ez-Zernûcî","Tekrar","Talebe dünkü dersi, ondan önceki dersleri belli bir düzen içinde tekrar etmelidir; tekrar edilmeyen ilim unutulur.","Zernûcî, Ta‘lîmü’l-müteallim","Yeni bir şeye geçmeden önce dünkü dersini bir kez daha oku."),
("Yunus Emre","Okumaktan maksat","Okumaktan mâni ne, kişi Hakk’ı bilmektir; çün okudun bilmezsin, ha bir kuru emektir.","Yunus Emre, Dîvân","Okumanın gayesi Allah’ı tanımaktır; kuru bilgi yorgunluktan ibarettir."),
("Şeyh Sa‘dî-i Şîrâzî","Amelsiz âlim","Amelsiz âlim, meyvesiz ağaç gibidir.","Sa‘dî, Gülistan, VIII","Bildiğini yaşamak, bilgini meyveye durdurur."),
]
o=[]
H=[{'b':b,'n':n,'k':k,'s':s,'t':'h'} for b,n,k,s in N]
Z=[{'b':b,'n':n,'k':k,'s':s,'t':'s','kim':kim} for kim,b,n,k,s in S]
# gün sırası: her üç günün ikisi ilim ve okuma, biri diğer nasihatler (âyet-hadis ve büyüklerin sözleri dönüşümlü)
D=[]
for i in range(max(len(H),len(Z))):
    if i<len(H): D.append(H[i])
    if i<len(Z): D.append(Z[i])
# eski listedeki ilimle ilgili olanlar da "İlim ve okumak" bölümüne girer
ILM={('','Kur’an'),('İmam Mâlik','İlim nurdur'),('İmam Şâfiî','Hafıza'),('İmam Ahmed b. Hanbel','Ömür boyu ilim'),('Cüneyd-i Bağdâdî','Kitap ve sünnet'),('İmam Gazâlî','İlim ve amel'),('İmam Gazâlî','Kendini bilmek'),('Yunus Emre','İlim'),('Abdullah b. Mübârek','Edep'),('İmam Ebû Hanîfe','Fıkıh')}
for x in D:
    if (x.get('kim',''),x['b']) in ILM: x['il']=1
I=[{'b':b,'n':n,'k':k,'s':s,'t':('s' if kim else 'h'),'il':1,**({'kim':kim} if kim else {})} for kim,b,n,k,s in IL]
while I or D:
    for _ in range(2):
        if I: o.append(I.pop(0))
    if D: o.append(D.pop(0))
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','nasihat.json')
json.dump({'ad':'Nasihatler','aciklama':'Âyetler, hadisler ve büyük âlimlerle tasavvuf büyüklerinin sözleri; her gün biri. Açılış ekranında günün nasihati buradan gelir.','n':o},open(p,'w'),ensure_ascii=False,indent=0)
print(len(o),'nasihat')
