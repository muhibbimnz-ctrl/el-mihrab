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
("Abdullah b. Mübârek","Edep","Çok ilimden çok, biraz edebe muhtacız.","Abdullah b. Mübârek’e nispet edilir","İlim edeple güzelleşir; edepsiz ilim sahibini de başkasını da yorar."),
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
o=[]
H=[{'b':b,'n':n,'k':k,'s':s,'t':'h'} for b,n,k,s in N]
Z=[{'b':b,'n':n,'k':k,'s':s,'t':'s','kim':kim} for kim,b,n,k,s in S]
# gün sırası: âyet-hadis ile büyüklerin sözleri dönüşümlü
for i in range(max(len(H),len(Z))):
    if i<len(H): o.append(H[i])
    if i<len(Z): o.append(Z[i])
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','nasihat.json')
json.dump({'ad':'Nasihatler','aciklama':'Âyetler, hadisler ve büyük âlimlerle tasavvuf büyüklerinin sözleri; her gün biri. Açılış ekranında günün nasihati buradan gelir.','n':o},open(p,'w'),ensure_ascii=False,indent=0)
print(len(o),'nasihat')
