# Siyer Dirâsesi — Sahâbe kartları ve Kureyş şeceresi → data/siyer/sahabe.json
import json,os,re
from urllib.parse import quote
D=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(os.path.dirname(D))
AS='Aşere-i mübeşşere';EB='Ehl-i beyt ve akrabalar';MH='Muhâcirler';EN='Ensar';SN='Sonra katılanlar'
def s(id,ad,ar,grup,lakap,nesep,hayat,ozet,bolum,hadis): return dict(id=id,ad=ad,ar=ar,grup=grup,lakap=lakap,nesep=nesep,hayat=hayat,ozet=ozet,bolum=bolum,hadis=hadis)
S=[
s('ebubekir','Ebû Bekir es-Sıddîk','أبو بكر الصديق',AS,'es-Sıddîk, Atîk','Abdullah b. Osman (Ebû Kuhâfe) b. Âmir b. Amr b. Ka‘b b. Sa‘d b. Teym b. Mürre — Peygamber’le Mürre’de birleşir.','d. Fil yılından ~2 yıl sonra · ö. 13/634, Medine',
 ['Hür erkeklerden ilk Müslüman olandır. Davetinin ilk yıllarında Osman, Zübeyr, Talha, Abdurrahman b. Avf ve Sa‘d b. Ebî Vakkās onun vasıtasıyla İslam’a girdi. Malını işkence gören köleleri, Bilâl ve Âmir b. Füheyre gibi, satın alıp azat etmeye harcadı.','Hicrette Peygamber’in yol arkadaşıydı; Sevr mağarasında “İki kişinin üçüncüsü Allah ise onlar hakkında ne düşünürsün?” sözü ona söylendi. İsrâ haberini hiç tereddütsüz tasdik ettiği için “Sıddîk” lakabını aldı. Peygamber’in hastalığında namazları o kıldırdı; vefattan sonra ilk halife seçildi ve iki yıl üç ay hilafetinde ridde savaşlarını yürüttü, Kur’an’ı bir mushafta topladı.'],
 [12,21,26,27,59,63,65],[('“İki kişinin üçüncüsü Allah ise”','ما ظنك باثنين الله ثالثهما','sitte'),('“Bir dost edinseydim”','لو كنت متخذا خليلا','sitte')]),
s('omer','Ömer b. el-Hattâb','عمر بن الخطاب',AS,'el-Fârûk','Ömer b. el-Hattâb b. Nüfeyl b. Abdüluzzâ … b. Adî b. Ka‘b — Peygamber’le Ka‘b’da birleşir.','d. ~584 · ö. 23/644, Medine (şehit)',
 ['Nübüvvetin altıncı yılında, kız kardeşi Fâtıma ile eniştesi Saîd b. Zeyd’in evinde Tâhâ sûresini duyarak Müslüman oldu. Onun İslam’a girişiyle Müslümanlar Kâbe’de açıkça namaz kılmaya başladı; hakkı bâtıldan ayırdığı için “Fârûk” diye anıldı.','Ezan, esirler, hicab gibi konularda görüşü vahiyle teyit edildi. Ebû Bekir’den sonra halife oldu; on yıllık hilafetinde Şam, Irak, İran ve Mısır fethedildi, hicrî takvim, divan ve kadılık teşkilatı kuruldu. Sabah namazında Ebû Lü’lü’e tarafından yaralanarak şehit oldu ve Peygamber’in yanına defnedildi.'],
 [17,31,46,65],[('“Şeytan seni bir yolda görse”','ما لقيك الشيطان سالكا فجا','sitte')]),
s('osman','Osman b. Affân','عثمان بن عفان',AS,'Zinnûreyn','Osman b. Affân b. Ebi’l-Âs b. Ümeyye b. Abdüşems b. Abdümenâf — Peygamber’le Abdümenâf’ta birleşir.','d. ~576 · ö. 35/656, Medine (şehit)',
 ['Ebû Bekir’in davetiyle ilk Müslümanlar arasına katıldı. Peygamber’in kızı Rukıyye ile evlendi ve onunla birlikte Habeşistan’a hicret etti; Rukıyye’nin vefatından sonra Ümmü Gülsüm’le evlendiği için “iki nur sahibi” (Zinnûreyn) denildi.','Cömertliğiyle tanınır: Rûme kuyusunu satın alıp Müslümanlara vakfetti, Tebük ordusunun büyük kısmını donattı. Hudeybiye’de Peygamber’in elçisi olarak Mekke’ye gitti; onun öldürüldüğü haberi üzerine Rıdvân biatı yapıldı. Üçüncü halife olarak Kur’an’ı tek mushafta çoğaltıp şehirlere gönderdi; evinde kuşatılarak Kur’an okurken şehit edildi.'],
 [12,16,46,57],[('“Meleklerin hayâ ettiği adam”','الا استحي من رجل تستحي منه الملايكه','sitte')]),
s('ali','Ali b. Ebî Tâlib','علي بن أبي طالب',AS,'Ebu’l-Hasan, Haydar','Ali b. Ebî Tâlib (Abdümenâf) b. Abdülmuttalib b. Hâşim — Peygamber’in amcasının oğlu.','d. ~600, Mekke · ö. 40/661, Kûfe (şehit)',
 ['Peygamber’in evinde büyüdü ve on yaşlarında, çocuklardan ilk Müslüman olan oldu. Hicret gecesi Peygamber’in yatağında yattı, emanetleri sahiplerine teslim edip sonra Medine’ye geldi. Fâtıma ile evlendi; Hasan ve Hüseyin onlardandır.','Bedir, Uhud ve Hendek’te öne çıktı; Hayber’de sancak ona verildi ve kale onun eliyle fethedildi. Tebük seferinde Peygamber onu Medine’de bıraktı ve “Benim yanımda Hârûn’un Mûsâ yanındaki yeri gibi olmaya razı değil misin?” buyurdu. Dördüncü halife oldu; Kûfe’de sabah namazına giderken bir Hâricî tarafından yaralanıp şehit oldu.'],
 [12,26,34,43,48,56],[('“Hârûn’un Mûsâ yanındaki yeri”','بمنزله هارون من موسي','sitte')]),
s('talha','Talha b. Ubeydullah','طلحة بن عبيد الله',AS,'Talhatü’l-hayr','Talha b. Ubeydullah b. Osman b. Amr b. Ka‘b b. Sa‘d b. Teym — Ebû Bekir’in kabilesinden.','ö. 36/656, Cemel',
 ['Ebû Bekir’in davetiyle ilk Müslümanlardan oldu. Uhud’da Peygamber’i eliyle korudu; o gün aldığı oklarla eli çolak kaldı. Peygamber o gün onun için “(Cenneti) hak etti” buyurdu; Ebû Bekir de Uhud gününü anınca “O gün tamamen Talha’nın günüdür” derdi.','Cömertliği sebebiyle “Talhatü’l-hayr” ve “Talhatü’l-feyyâz” diye anıldı. Cemel savaşında şehit oldu.'],
 [12,38],[('“Talha hak etti”','اوجب طلحه','tisa')]),
s('zubeyr','Zübeyr b. el-Avvâm','الزبير بن العوام',AS,'Havâriyyü’r-Resûl','Zübeyr b. el-Avvâm b. Huveylid b. Esed b. Abdüluzzâ b. Kusay — annesi Safiyye bint Abdülmuttalib, Peygamber’in halasıdır.','ö. 36/656, Vâdi’s-Sibâ‘',
 ['Gençken Müslüman oldu; amcası onu hasıra sarıp dumanla işkence etse de dininden dönmedi. Allah yolunda ilk kılıç çeken o oldu. Her iki Habeşistan hicretine katıldı.','Hendek’te düşmanın haberini getirmek için gönüllü olunca Peygamber “Her peygamberin bir havârisi vardır; benim havârim Zübeyr’dir” buyurdu. Mekke fethinde ordunun bir kanadını komuta etti. Cemel’den ayrılırken yolda öldürüldü.'],
 [12,16,43,53],[('“Benim havârim Zübeyr”','وحواري الزبير','sitte')]),
s('abdurrahman','Abdurrahman b. Avf','عبد الرحمن بن عوف',AS,'','Abdurrahman b. Avf b. Abdi Avf b. Abd b. el-Hâris b. Zühre b. Kilâb — Peygamber’in annesinin kabilesi Zühre’den.','ö. 32/652, Medine',
 ['Ebû Bekir’in davetiyle Müslüman oldu, iki hicrete de katıldı. Medine’de Sa‘d b. Rebî‘ ile kardeş yapıldı; Sa‘d malının yarısını ona teklif edince “Allah malını ve aileni sana mübarek kılsın; bana çarşının yolunu gösterin” dedi ve ticaretle zengin oldu.','Servetini Allah yolunda harcadı; Tebük’e büyük yardımda bulundu, vefatında Bedir ehline ve ümmehâtü’l-mü’minîne vasiyetlerde bulundu. Ömer’in belirlediği şûrâ heyetinde Osman’ın halifeliğini o yönetti.'],
 [12,16,30,57],[('“Bana çarşının yolunu gösterin”','دلوني علي السوق','sitte')]),
s('sad','Sa‘d b. Ebî Vakkās','سعد بن أبي وقاص',AS,'','Sa‘d b. Mâlik (Ebû Vakkās) b. Üheyb b. Abdümenâf b. Zühre b. Kilâb — Peygamber’in dayıları Zühre’den.','ö. 55/675, Akīk',
 ['On yedi yaşında Müslüman oldu. Annesi, dininden dönmedikçe yemeyip içmeyeceğine yemin edince Sa‘d “Yüz canın olsa da birer birer çıksa dinimi bırakmam” dedi; bu olay üzerine Lokmân sûresindeki anne babaya itaatin sınırını belirleyen âyet indi.','Allah yolunda ilk ok atan odur. Uhud’da Peygamber ona okları uzatarak “At, anam babam sana feda olsun” dedi. Ömer döneminde Kādisiye’de İran ordusunu yendi ve Kûfe’yi kurdu. Duasının kabul olduğu bilinirdi.'],
 [12,38],[('“At, anam babam sana feda olsun”','فداك ابي وامي','sitte')]),
s('said','Saîd b. Zeyd','سعيد بن زيد',AS,'','Saîd b. Zeyd b. Amr b. Nüfeyl … b. Adî — Ömer’in amcasının oğlu ve eniştesi.','ö. 51/671, Akīk',
 ['Babası Zeyd b. Amr, cahiliye döneminde putlara tapmayan, İbrâhim’in dinini arayan bir hanîfti. Saîd ve eşi Fâtıma bint el-Hattâb ilk Müslümanlardandı; Ömer onların evinde Kur’an’ı dinleyerek Müslüman oldu.','Bedir sırasında Peygamber’in verdiği bir görevle Şam yolunda olduğu için savaşa katılamadı; ama ganimetten pay verildi. Diğer bütün savaşlarda bulundu.'],
 [12,17],[('Cennetle müjdelenen on kişi','ابو بكر في الجنه وعمر في الجنه','tisa')]),
s('ebuubeyde','Ebû Ubeyde b. el-Cerrâh','أبو عبيدة بن الجراح',AS,'Emînü’l-ümme','Âmir b. Abdullah b. el-Cerrâh … b. el-Hâris b. Fihr — Peygamber’le Fihr’de birleşir.','ö. 18/639, Amvâs vebası',
 ['Ebû Bekir’in davetiyle ilk Müslümanlardan oldu, Habeşistan’a hicret etti. Uhud’da Peygamber’in yanağına batan miğfer halkalarını dişleriyle çıkarırken ön dişleri kırıldı.','Necrân heyetiyle gönderilecek güvenilir birini istediklerinde Peygamber “Size gerçekten güvenilir birini göndereceğim” dedi ve onu gönderdi: “Her ümmetin bir emini vardır; bu ümmetin emini Ebû Ubeyde’dir.” Ömer döneminde Şam ordularının başkomutanı oldu; Amvâs vebasında askerlerini bırakmayıp orada vefat etti.'],
 [12,16,38,58],[('“Bu ümmetin emini”','امين هذه الامه','sitte')]),
s('hamza','Hamza b. Abdülmuttalib','حمزة بن عبد المطلب',EB,'Esedullah, Seyyidü’ş-şühedâ','Hamza b. Abdülmuttalib b. Hâşim — Peygamber’in amcası ve süt kardeşi.','ö. 3/625, Uhud (şehit)',
 ['Ebû Cehil’in Peygamber’e hakaret ettiğini duyunca avdan dönüşte onun başına yayıyla vurdu ve “Ben de onun dinindeyim” diyerek Müslüman oldu. Onun ve ardından Ömer’in Müslüman olması Müslümanlara güç verdi.','Bedir’de öne çıkan mübârizlerdendi. Uhud’da Vahşî’nin attığı mızrakla şehit oldu; Hind’in onun cesedine yaptıkları Peygamber’i derinden yaraladı. “Şehitlerin efendisi” diye anılır.'],
 [17,34,38,39],[('“Şehitlerin efendisi”','سيد الشهداء','tisa')]),
s('abbas','Abbâs b. Abdülmuttalib','العباس بن عبد المطلب',EB,'','Abbâs b. Abdülmuttalib b. Hâşim — Peygamber’in amcası.','ö. 32/653, Medine',
 ['Henüz Müslüman olmadığı hâlde İkinci Akabe’de yeğeninin yanında bulundu ve Ensar’dan onu koruyacaklarına dair söz istedi. Bedir’de Kureyş saflarında esir düştü ve fidye vererek kurtuldu.','Mekke fethinden önce Müslüman olup Medine’ye hicret etti. Huneyn’de güçlü sesiyle dağılan Müslümanları geri çağırdı. Ömer döneminde kuraklıkta onunla yağmur duasına çıkıldı: “Allah’ım, Peygamberimizin amcasını vesile ediyoruz.”'],
 [24,35,52,54],[('Abbâs ile yağmur duası','كنا نتوسل اليك بنبينا','sitte')]),
s('cafer','Ca‘fer b. Ebî Tâlib','جعفر بن أبي طالب',EB,'et-Tayyâr, Ebu’l-mesâkîn','Ca‘fer b. Ebî Tâlib b. Abdülmuttalib — Ali’nin ağabeyi.','ö. 8/629, Mûte (şehit)',
 ['Habeşistan muhâcirlerinin sözcüsüydü. Necâşî’nin huzurunda cahiliyeyi ve İslam’ı anlatan konuşmasını yaptı, Meryem sûresini okudu; Necâşî ağladı ve Müslümanları Kureyş’e teslim etmedi.','Hayber’in fethi günü Habeşistan’dan döndü; Peygamber “Hangisine daha çok sevineceğimi bilmiyorum, Hayber’in fethine mi, Ca‘fer’in gelişine mi?” dedi ve ona “Yaratılışta da ahlakta da bana benzedin” buyurdu. Mûte’de sancağı taşırken iki kolu kesilerek şehit oldu; cennette iki kanatla uçtuğu müjdelendiği için “Tayyâr” denildi.'],
 [16,48,50],[('“Yaratılışta ve ahlakta bana benzedin”','اشبهت خلقي وخلقي','sitte')]),
s('hatice','Hatice bint Huveylid','خديجة بنت خويلد',EB,'Ümmü’l-mü’minîn, et-Tâhire','Hatice bint Huveylid b. Esed b. Abdüluzzâ b. Kusay — Zübeyr’in halası.','ö. nübüvvetin 10. yılı (619), Mekke',
 ['Mekke’nin saygın bir tüccarıydı. Peygamber’in dürüstlüğünü görünce ona evlenme teklif etti. İlk vahiy geldiğinde onu “Allah seni asla utandırmaz; sen akrabayı gözetir, düşkünün yükünü taşırsın…” diyerek teselli etti ve ilk iman eden oldu.','Bütün servetini davete harcadı; boykot yıllarında Şi‘b’de Peygamber’le birlikte kaldı. İbrâhim dışındaki bütün çocukları ondandır. Vefat ettiği yıl, Ebû Tâlib’in de vefatıyla “Hüzün yılı” oldu. Cebrâil ona Rabbinden selam getirdi ve cennette bir köşkle müjdeledi.'],
 [9,11,18,19,70],[('“Kadınlarının en hayırlısı Hatice”','خير نسايها خديجه','sitte'),('İnciden köşkle müjde','من قصب لا صخب','sitte')]),
s('aise','Âişe bint Ebî Bekir','عائشة بنت أبي بكر',EB,'Ümmü’l-mü’minîn, es-Sıddîka','Âişe bint Ebî Bekir — Teym kabilesinden.','ö. 58/678, Medine',
 ['Ebû Bekir’in kızıdır; hicretten sonra Peygamber’in evine geldi. İfk hadisesinde iftiraya uğradı ve Nûr sûresinin âyetleriyle temize çıkarıldı.','Sahâbenin en fakihlerinden biriydi; büyük sahâbîler bile ona danışırdı. Binlerce hadis rivayet etti ve Peygamber’in ev hayatına dair bilgilerin çoğu ondan gelir. Peygamber son hastalığında onun odasında kaldı ve orada vefat etti.'],
 [41,63,64,70],[('Âişe’nin üstünlüğü','فضل عايشه علي النساء','sitte')]),
s('fatima','Fâtıma bint Muhammed','فاطمة بنت محمد',EB,'ez-Zehrâ','Fâtıma bint Muhammed b. Abdullah — annesi Hatice.','ö. 11/632, Medine',
 ['Peygamber’in en küçük kızıdır. Mekke’de babasının çektiği eziyetlere şahit oldu; Kâbe’de sırtına deve işkembesi konduğunda onu temizleyen oydu. Ali ile evlendi; Hasan, Hüseyin, Zeyneb ve Ümmü Gülsüm onlardandır.','Peygamber “Fâtıma benden bir parçadır; onu üzen beni üzer” buyurdu. Son hastalığında ona ehlinden ilk kavuşacak kişinin kendisi olduğunu söyledi; Fâtıma babasından yaklaşık altı ay sonra vefat etti.'],
 [63,71],[('“Fâtıma benden bir parçadır”','فاطمه بضعه مني','sitte')]),
s('bilal','Bilâl b. Rebâh','بلال بن رباح',MH,'Müezzinü’r-Resûl','Habeş asıllı; annesi Hamâme. Ümeyye b. Halef’in kölesiydi.','ö. 20/641 civarı, Dımaşk',
 ['Mekke’nin kızgın kumlarında göğsüne taş konarak işkence edilirken “Ehad, ehad” (Allah birdir) demekten vazgeçmedi. Ebû Bekir onu satın alıp azat etti.','Medine’de İslam’ın ilk müezzini oldu; Mekke fethinde Kâbe’nin üstüne çıkıp ezan okudu. Peygamber, cennette önünde onun ayak seslerini duyduğunu söylemişti. Peygamber’in vefatından sonra ezan okumakta zorlandı ve Şam’a gidip cihada katıldı.'],
 [15,31,34,53],[('Cennetteki ayak sesleri','دف نعليك','sitte')]),
s('ammar','Ammâr b. Yâsir','عمار بن ياسر',MH,'','Ammâr b. Yâsir — babası Yâsir Yemenli, annesi Sümeyye; Mahzûmoğullarının himayesindeydi.','ö. 37/657, Sıffîn',
 ['Annesi Sümeyye İslam’ın ilk şehididir; babası Yâsir de işkenceyle öldü. Peygamber yanlarından geçerken “Sabredin ey Yâsir ailesi, sizin buluşma yeriniz cennettir” derdi. Ammâr işkence altında söylediği sözden dolayı üzülünce “Kalbin nasıl?” diye soruldu ve Nahl 16:106 ile teselli edildi.','Mescid-i Nebevî inşa edilirken iki kerpiç taşıdığında Peygamber “Seni bâğî bir topluluk öldürecek” buyurdu. Sıffîn’de Ali’nin saflarında savaşırken doksan yaşlarında şehit oldu.'],
 [15,29],[('“Seni bâğî bir topluluk öldürecek”','تقتلك الفيه الباغيه','tisa')]),
s('musab','Mus‘ab b. Umeyr','مصعب بن عمير',MH,'Mus‘abü’l-hayr','Mus‘ab b. Umeyr b. Hâşim … b. Abdüddâr b. Kusay.','ö. 3/625, Uhud (şehit)',
 ['Mekke’nin en bakımlı, en güzel giyinen genciydi. Müslüman olunca ailesi onu hapsetti; o her şeyini bırakıp Habeşistan’a, sonra Medine’ye gitti.','Birinci Akabe’den sonra Medine’ye ilk muallim olarak gönderildi; onun vesilesiyle Üseyd b. Hudayr ve Sa‘d b. Muâz Müslüman oldu ve kısa sürede Ensar’ın hemen her evine İslam girdi. Uhud’da sancağı taşırken şehit oldu; kefen olarak tek bir hırkası vardı, başı örtülünce ayakları açılıyordu.'],
 [16,23,38],[('Uhud’da şehit oluşu','مصعب بن عمير قتل يوم احد','sitte')]),
s('sadmuaz','Sa‘d b. Muâz','سعد بن معاذ',EN,'','Evs kabilesinin Abdüleşhel kolunun reisi.','ö. 5/627, Medine',
 ['Mus‘ab b. Umeyr’in daveti ile Müslüman oldu ve aynı gün kabilesine “Allah’a ve Resûlü’ne iman etmedikçe sizinle konuşmam haramdır” dedi; akşama kadar bütün Abdüleşhel Müslüman oldu.','Bedir öncesi Ensar adına “Denize dalsan seninle dalarız” diyerek Peygamber’i sevindirdi. Hendek’te aldığı ok yarası ağırlaştı; Benî Kurayza hakkında hakem oldu. Vefat ettiğinde Peygamber “Sa‘d’ın ölümüyle Rahmân’ın arşı titredi” buyurdu.'],
 [23,33,34,43,44],[('“Arş titredi”','اهتز العرش لموت سعد','sitte')]),
s('ebueyyub','Ebû Eyyûb el-Ensârî','أبو أيوب الأنصاري',EN,'Mihmândâr-ı Nebî','Hâlid b. Zeyd — Hazrec’in Neccâroğulları kolundan.','ö. 52/672, İstanbul kuşatması',
 ['İkinci Akabe biatına katıldı. Hicrette Peygamber’in devesi onun evinin önüne çöktü; Mescid ve odalar yapılıncaya kadar Peygamber onun evinde misafir kaldı. Ebû Eyyûb, Peygamber’in üstünde yürümemek için üst katta saygıyla oturur, yemeğin artığında onun parmak izlerini arardı.','Bütün savaşlara katıldı. İleri yaşına rağmen İstanbul seferine çıktı, orada hastalanıp vefat etti ve vasiyeti üzerine surlara yakın bir yere defnedildi.'],
 [24,28,29],[('Peygamber’in onun evine inmesi','حتي نزل علي ابي ايوب','sitte')]),
s('muaz','Muâz b. Cebel','معاذ بن جبل',EN,'','Muâz b. Cebel — Hazrec’in Seleme kolundan.','ö. 18/639, Amvâs vebası',
 ['On sekiz yaşında İkinci Akabe’de biat etti. Peygamber onu “Ümmetimin helali ve haramı en iyi bileni” olarak övdü.','Yemen’e vali ve muallim olarak gönderilirken Peygamber ona nasıl hükmedeceğini sordu ve onu uğurlamak için bir süre yanında yürüdü; ona “Ehl-i kitaptan bir kavme gidiyorsun” diyerek davetin sırasını öğretti. Şam’da Amvâs vebasında vefat etti.'],
 [24,58],[('Helal ve haramı en iyi bilen','اعلمهم بالحلال والحرام معاذ','tisa'),('Yemen’e gönderilmesi','انك تاتي قوما من اهل الكتاب','sitte')]),
s('ebuhureyre','Ebû Hüreyre','أبو هريرة',SN,'','Abdurrahman b. Sahr (meşhur görüş) — Yemen’in Devs kabilesinden.','ö. 57-59/677-679, Medine',
 ['Hayber yılında Medine’ye gelip Müslüman oldu ve dört yıl kadar Peygamber’den hiç ayrılmadı; Suffe ehlindendi, açlıktan bayıldığı günler oldu.','En çok hadis rivayet eden sahâbîdir. Unutkanlıktan şikâyet edince Peygamber “Ridânı yay” dedi ve ona dua etti; ondan sonra duyduğunu unutmadığını söylerdi. Annesinin Müslüman olması için yaptırdığı dua da kabul edilmiştir.'],
 [48],[('“Ridânı yay”','ابسط رداءك','sitte')]),
s('ibnmesud','Abdullah b. Mes‘ûd','عبد الله بن مسعود',MH,'','Abdullah b. Mes‘ûd — Hüzeyl kabilesinden; Zühreoğullarının müttefiki.','ö. 32/652-653, Medine',
 ['Mekke’de çobanlık yaparken Müslüman oldu. Kâbe’nin yanında Rahmân sûresini yüksek sesle okuyan ilk kişidir; bu yüzden dövüldü.','Peygamber’in ayakkabı ve misvakını taşıyan hizmetçisiydi. “Kur’an’ı indiği gibi taze okumak isteyen İbn Ümmi Abd’in kıraatiyle okusun” buyruldu. Bedir’de Ebû Cehil’in işini bitiren odur. Ömer onu Kûfe’ye muallim gönderdi; Hanefî fıkhının temelinde onun ilmi vardır.'],
 [12,13,16,34],[('“Kur’an’ı taze okumak isteyen”','ان يقرا القران غضا','tisa')]),
s('selman','Selmân-ı Fârisî','سلمان الفارسي',SN,'Selmânü’l-hayr','İsfahan yakınlarından Mecûsî bir ailenin oğlu.','ö. 35/656 civarı, Medâin',
 ['Hakikati aramak için evinden kaçtı; Şam, Musul, Nusaybin ve Ammûriye’de rahiplerin yanında kaldı. Son rahip ona Arabistan’da çıkacak peygamberin alametlerini haber verdi. Köle olarak Medine’ye getirildi ve alametleri görünce Müslüman oldu; Peygamber’in yardımıyla azat edildi.','Hendek savaşında Medine’nin etrafına hendek kazılmasını önerdi. Peygamber “İman Süreyyâ’da olsaydı bunlardan bazı adamlar ona ulaşırdı” buyururken elini Selmân’ın omzuna koydu.'],
 [42,43],[('“İman Süreyyâ’da olsaydı”','لناله رجال من هولاء','sitte')]),
s('halid','Hâlid b. el-Velîd','خالد بن الوليد',SN,'Seyfullah','Hâlid b. el-Velîd b. el-Mugîre — Mahzûm kabilesinden.','ö. 21/642, Humus',
 ['Uhud’da Müslümanların arkasından dolaşan Kureyş süvarilerinin komutanıydı. Hudeybiye’den sonra Amr b. el-Âs ile birlikte Medine’ye gelip Müslüman oldu.','Mûte’de üç komutan şehit olunca sancağı aldı ve orduyu kurtardı; Peygamber onu “Allah’ın kılıçlarından bir kılıç” diye andı. Ebû Bekir ve Ömer dönemlerinde Irak ve Şam fetihlerinde, özellikle Yermük’te büyük zaferler kazandı. Yatağında ölürken vücudunda yarasız yer kalmadığını söyledi.'],
 [38,50,53],[('“Allah’ın kılıçlarından bir kılıç”','سيف من سيوف الله','sitte')]),
s('zeyd','Zeyd b. Hârise','زيد بن حارثة',MH,'Hibbü Resûlillâh','Zeyd b. Hârise — Kelb kabilesinden; çocukken esir düşüp köle olarak satıldı.','ö. 8/629, Mûte (şehit)',
 ['Hatice’nin Peygamber’e hediye ettiği köleydi. Babası onu almaya geldiğinde Peygamber’in yanında kalmayı tercih etti; Peygamber onu azat edip evlat edindi. Kur’an’da adı geçen tek sahâbîdir (Ahzâb 33:37).','İlk Müslümanlardandır; Tâif yolculuğunda Peygamber’in yanındaydı. Mûte ordusunun ilk komutanı olarak şehit oldu. Peygamber oğlu Üsâme’yi komutan atadığında itiraz edenlere “Babası da emirliğe layıktı” buyurdu.'],
 [12,20,50],[('“Emirliğe layıktı”','ان كان لخليقا للاماره','sitte')]),
]
# Kureyş şeceresi: [ad, not, sahabe-id veya '', çocuklar]
SEC=['Fihr (Kureyş)','Kureyş’in atası',None,[
 ['Lüey','',None,[['Ka‘b','',None,[
   ['Mürre','',None,[
     ['Kilâb','',None,[
       ['Kusay','Kâbe hizmetlerini toplayan',None,[
         ['Abdümenâf','',None,[
           ['Hâşim','',None,[['Abdülmuttalib','Zemzem’i yeniden kazan',None,[
              ['Abdullah','',None,[['Hz. Muhammed ﷺ','Resûlullah',None,[['Fâtıma','Ali ile evlendi','fatima',[]]]]]],
              ['Ebû Tâlib','',None,[['Ali','','ali',[]],['Ca‘fer','','cafer',[]]]],
              ['Hamza','','hamza',[]],['Abbâs','','abbas',[]],['Safiyye','Zübeyr’in annesi',None,[]]]]]],
           ['Abdüşems','',None,[['Ümeyye','',None,[['Ebu’l-Âs','',None,[['Affân','',None,[['Osman','','osman',[]]]]]]]]]]]],
         ['Abdüluzzâ','',None,[['Esed','',None,[['Huveylid','',None,[['Hatice','Peygamber’in eşi','hatice',[]],['Avvâm','',None,[['Zübeyr','','zubeyr',[]]]]]]]]]],
         ['Abdüddâr','',None,[['…','',None,[['Mus‘ab b. Umeyr','','musab',[]]]]]]]],
       ['Zühre','Peygamber’in annesi Âmine’nin kabilesi',None,[['Abdurrahman b. Avf','','abdurrahman',[]],['Sa‘d b. Ebî Vakkās','','sad',[]]]]]],
     ['Teym','',None,[['Ebû Bekir','','ebubekir',[['Âişe','','aise',[]]]],['Talha','','talha',[]]]],
     ['Mahzûm (Yakaza)','',None,[['Hâlid b. el-Velîd','','halid',[]]]]]],
   ['Adî','',None,[['Ömer','','omer',[]],['Saîd b. Zeyd','','said',[]]]]]]]],
 ['el-Hâris b. Fihr','',None,[['Ebû Ubeyde','','ebuubeyde',[]]]]]]
def an(t):
    t=re.sub('[ً-ٰـ]','',t);t=re.sub('[أإآٱ]','ا',t).replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي');return t
SS=['bukhari','muslim','abudawud','tirmidhi','nasai','ibnmajah'];C={}
def say(q,kap):
    W=an(q).split(' ');n=0
    for k in (SS if kap=='sitte' else SS+['malik','ahmed','darimi']):
        fp=os.path.join(R,f'data/hadis/ara/{k}.json')
        if not os.path.exists(fp):continue
        if k not in C:C[k]=json.load(open(fp))
        n+=sum(1 for r in C[k] if all(w in r[1] for w in W))
    return n
kt=json.load(open(os.path.join(R,'data/siyer/kitap.json')));NB={int(b['n']):b['baslik'] for b in kt['bolum']}
hata=0;ids={x['id'] for x in S}
for x in S:
    for b in x['bolum']: assert b in NB,(x['id'],b)
    x['bolum']=[[b,NB[b]] for b in x['bolum']]
    h=[]
    for et,q,kap in x['hadis']:
        n=say(q,kap)
        if n==0 or n>80: print('hadis',x['id'],q,n);hata+=1
        h.append([et,'hadis.html#ara='+quote(q)+'&kap='+kap])
    x['hadis']=h
def gez(d):
    if d[2]: assert d[2] in ids,d[2]
    for c in d[3]: gez(c)
gez(SEC)
json.dump(dict(sahabe=S,secere=SEC),open(os.path.join(R,'data/siyer/sahabe.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(S),'sahâbî, sorunlu',hata)
