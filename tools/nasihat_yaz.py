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
o=[{'b':b,'n':n,'k':k,'s':s} for b,n,k,s in N]
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','nasihat.json')
json.dump({'ad':'Nasihatler','aciklama':'Her gün bir âyet ya da hadis ve kısa bir nasihat. Açılış ekranında günün nasihati buradan gelir.','n':o},open(p,'w'),ensure_ascii=False,indent=0)
print(len(o),'nasihat')
