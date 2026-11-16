import json
K='tools/kaynak/'
P=json.load(open(K+'izhar_ar_paragraf.json'))
T={}
for i in range(1,7): T.update(json.load(open(K+f'izhar_tr_{i}.json')))
ATLA={282}
D=[(0,'Mukaddime: kelime ve isim','المقدمة: الكلمة والاسم'),(10,'Âmilin tarifi ve kısımları','تعريف العامل وأقسامه'),
(23,'Cer harfleri','حروف الجر'),(41,'Cer harflerinin müteallakı','متعلق حروف الجر'),(50,'İnne ve kardeşleri','إنّ وأخواتها'),
(53,'Leyse’ye benzeyen mâ ve lâ','ما ولا المشبهتان بليس'),(59,'Cinsi nefyeden lâ','لا النافية للجنس'),(63,'Nidâ harfleri','حروف النداء'),
(69,'Muzâriyi nasbeden harfler','نواصب المضارع'),(75,'Muzâriyi cezmeden harfler','جوازم المضارع'),(97,'Kâne ve kardeşleri','كان وأخواتها'),
(103,'Mukârebe fiilleri','أفعال المقاربة'),(108,'Medih ve zem fiilleri','أفعال المدح والذم'),(120,'Kalp fiilleri','أفعال القلوب'),
(132,'Kıyâsî âmiller: fiil','العوامل القياسية: الفعل'),(140,'İsm-i fâil','اسم الفاعل'),(147,'İsm-i mef‘ûl ve sıfat-ı müşebbehe','اسم المفعول والصفة المشبهة'),
(154,'İsm-i tafdîl','اسم التفضيل'),(160,'Masdar','المصدر'),(174,'Muzâf isim','الاسم المضاف'),(176,'Tam isim (mübhem isim)','الاسم التام'),
(181,'İsm-i fiil','اسم الفعل'),(191,'Mânevî âmiller','العوامل المعنوية'),(202,'Ma‘mûl: müfred','المعمول: المفرد'),(209,'Muzâri ve mâzînin ma‘mûl oluşu','المضارع والماضي معمولين'),
(221,'Cümle ve kısımları','الجملة وأقسامها'),(225,'Cümlenin i‘râbı','إعراب الجملة'),(238,'Mahalli olan ve olmayan cümle','الجمل التي لها محل والتي لا محل لها'),
(258,'Merfûlar: fâil ve nâib-i fâil','المرفوعات: الفاعل ونائبه'),(279,'Bâriz zamirler ve açık fâil','الضمير البارز والفاعل الظاهر'),
(292,'Te’nîs ve cemi','التأنيث والجمع'),(307,'Mübtedâ ve haber','المبتدأ والخبر'),(313,'Habere fâ girmesi; diğer merfûlar','دخول الفاء في الخبر وبقية المرفوعات'),
(322,'Mansûbat: mef‘ûller','المنصوبات: المفاعيل'),(329,'Mef‘ûlün leh ve me‘ah','المفعول له والمفعول معه'),(334,'Hâl','الحال'),(342,'Temyiz','التمييز'),
(343,'Müstesnâ','المستثنى'),(355,'Diğer mansûblar','بقية المنصوبات'),(360,'Mecrûrlar ve izâfet','المجرورات والإضافة'),(370,'Meczûm; cezâya fâ girmesi','المجزوم ودخول الفاء في الجزاء'),
(378,'Tâbiler: sıfat','التوابع: الصفة'),(381,'Ma‘rife ve nekre','المعرفة والنكرة'),(404,'Atıf ve tekid','العطف والتأكيد'),(413,'Bedel ve atf-ı beyân','البدل وعطف البيان'),
(418,'İ‘râbın tarifi ve taksimleri','الإعراب وتقسيماته'),(441,'Munsarif ve gayr-i munsarif','المنصرف وغير المنصرف'),(457,'Takdîrî i‘râb','الإعراب التقديري'),
(487,'Mahallî i‘râb ve mebnî','الإعراب المحلي والمبني')]
S=[s for s,_,_ in D]+[len(P)]
bol=[]
for k,(s,tr,ar) in enumerate(D):
  idx=[i for i in range(s,S[k+1]) if i not in ATLA]
  bol.append({'b':ar,'tr_b':f'{k+1}. Ders: {tr}','p':[P[i] for i in idx],'tr':[T[str(i)] for i in idx]})
Q=[
(0,'İzhâr’a göre kelime kaç kısımdır?',['Üç: isim, fiil, harf','İki: isim ve fiil','Dört','Beş'],'İsim, fiil ve harf.'),
(1,'Âmil nedir?',['Kelimenin sonunun belli bir i‘râb almasını gerektiren şey','Kelimenin kökü','Cümlenin öznesi','Bir harekenin adı'],'Bir aracı vasıtasıyla i‘râbı gerektiren şey.'),
(2,'Cer harfleri kaç tanedir?',['Yirmi','On','Otuz','On iki'],'Bâ ile başlayan yirmi harf.'),
(2,'“Rubbe” hangi mânâ içindir?',['Taklîl (azlık)','Teşbih','Kasem','İstisnâ'],'Rubbe azlık bildirir.'),
(3,'Cer harflerinin mutlaka neyi olmalıdır?',['Müteallakı','Haberi','Temyizi','Hâli'],'Fiil, fiile benzeyen veya fiil mânâsı.'),
(4,'İnne ve kardeşleri ismini ve haberini nasıl etkiler?',['İsmini nasb, haberini ref‘ eder','İsmini ref‘, haberini nasb eder','İkisini de nasb eder','İkisini de cerr eder'],'İsmi mansûb, haberi merfû olur.'),
(6,'Cinsi nefyeden lânın haberi hangi i‘râbdadır?',['Merfû','Mansûb','Mecrûr','Meczûm'],'Lânın haberi merfûdur.'),
(8,'Hangisi muzâriyi nasbeden harflerdendir?',['Len','Lem','Lemmâ','Emir lâmı'],'En, len, key, izen nâsıbtır.'),
(9,'“Lem” muzâriye ne yapar?',['Cezmeder ve mânâsını mâzîye çevirir','Nasbeder','Ref‘ eder','İstikbâle çevirir'],'Lem câzimdir, mâzî nefyi verir.'),
(10,'Kâne ve kardeşleri haberini nasıl etkiler?',['Nasbeder','Ref‘ eder','Cerr eder','Etkilemez'],'İsmi merfû, haberi mansûb.'),
(11,'Kâde, ‘asâ gibi fiillere ne denir?',['Mukârebe fiilleri','Kalp fiilleri','Medih fiilleri','Nâsıb fiiller'],'Yaklaşma, ümit ve başlama fiilleri.'),
(12,'“Ni‘me” ve “bi’se” hangi fiillerdendir?',['Medih ve zem','Kalp','Mukârebe','Nâkıs'],'Övme ve yerme fiilleri.'),
(13,'Kalp fiilleri kaç mef‘ûle nasb verir?',['İki','Bir','Üç','Hiç'],'Mübtedâ ve haberin aslı olan iki mef‘ûl.'),
(15,'İsm-i fâilin amel etmesi için şartlardan biri hangisidir?',['Hâl veya istikbâl mânâsında olması','Mâzî olması','Ma‘rife olması','Cemi olması'],'Hâl/istikbâl ve dayanak şartı.'),
(17,'İsm-i tafdîl açık bir ismi ref‘ eder mi?',['Genellikle hayır; yalnız Kuhl meselesinde','Her zaman eder','Asla etmez, istisnasız','Yalnız cemi olunca'],'Kuhl meselesi müstesnâdır.'),
(21,'“Heyhâte” hangi kelime türüdür?',['İsm-i fiil','Harf','Mâzî fiil','Masdar'],'Mâzî mânâsında ism-i fiil.'),
(22,'Mânevî âmiller kaçtır (bu metne göre)?',['İki: ibtidâ ve muzâriyi ref‘ eden âmil','Bir','Üç','Beş'],'İbtidâ ve nâsıb/câzimden boş olma.'),
(25,'Fiil cümlesi neden oluşur?',['Fiil ve fâilden','Mübtedâ ve haberden','Harf ve isimden','İki isimden'],'Fiil ile fâili.'),
(26,'Lafzı kastedilen cümlenin i‘râbı var mıdır?',['Evet, müfred hükmündedir','Hayır, asla','Yalnız mecrûr olur','Yalnız şiirde'],'Müfred tevilinde olduğu için i‘râbı vardır.'),
(28,'Fâil ile nâib-i fâilin farkı nedir?',['Fâil ma‘lûm, nâib meçhul fiile isnâd edilir','Fâil mansûbdur','Nâib her zaman önce gelir','Fark yoktur'],'Meçhulde nâib-i fâil gelir.'),
(28,'“İdrib” fiilinin fâili nasıldır?',['Vâcib gizli zamir','Açık isim','Bâriz zamir','Fâilsiz'],'Tekil müzekker muhâtab emirde vücûben müstetir.'),
(30,'Hakiki müennes nedir?',['Karşılığında erkeği olan canlı','Tâ ile biten her kelime','Güneş gibi kelimeler','Her cemi'],'İmrae, nâka gibi.'),
(31,'Mübtedânın haberi cümle olursa ne gerekir?',['Mübtedâya dönen bir âid','Fâ harfi','Kad harfi','Tenvin'],'Şe’n zamiri dışında âid gerekir.'),
(32,'“Emmâ”dan sonra gelen mübtedânın haberine ne girer?',['Fâ','Lâm','Vâv','Bâ'],'Emmâ Zeydun fe-munṭalikun.'),
(33,'“Darabtu darben” cümlesinde “darben” nedir?',['Mef‘ûl-i mutlak','Mef‘ûlün bih','Hâl','Temyiz'],'Fiilin kendi masdarı.'),
(34,'“Ci’tu ve Zeyden”de Zeyden nedir?',['Mef‘ûlün me‘ah','Ma‘tûf','Mef‘ûlün bih','Hâl'],'Eşlik bildiren vâvdan sonra.'),
(35,'Hâlin şartı nedir?',['Nekre olması','Ma‘rife olması','Cemi olması','Mecrûr olması'],'Hâl nekre olur.'),
(36,'“Tâbe Zeydun nefsen”de nefsen nedir?',['Temyiz','Hâl','Mef‘ûlün bih','Bedel'],'Belirsizliği kaldıran temyiz.'),
(37,'“Câenî’l-kavmu illâ Zeyden”de Zeyden niçin mansûbdur?',['Müspet ve tam sözde illâ’dan sonra geldiği için','Hâl olduğu için','Bedel olduğu için','Mef‘ûl olduğu için'],'Nasbı vâcib müstesnâ.'),
(39,'“Ves’eli’l-karyete” âyetinde hazfedilen nedir?',['Muzâf (ehl)','Muzâfun ileyh','Fiil','Harf'],'Yani karye halkına sor.'),
(40,'Cezâ isim cümlesi olursa başına ne gelir?',['Fâ','Lâm','Sîn','Kad'],'İn darabte fe-ente madrûbun.'),
(41,'Nekre bir cümle ile vasfedilince cümlede ne bulunmalı?',['Mevsufa dönen zamir','Fâ','Tenvin','Lâm'],'Câenî raculun kâme ebûhu.'),
(42,'Ma‘rife kaç nevidir?',['Altı','Dört','Beş','Yedi'],'Zamir, alem, işaret, mevsûl, lâmlı, muzâf.'),
(43,'Bitişik merfû zamire atıf yapılırsa ne gerekir?',['Ayrı zamirle tekid','Cer harfinin tekrarı','Fâ','Hiçbir şey'],'Darabtu ene ve Zeydun.'),
(44,'“Sulibe Zeydun sevbuhû”da sevbuhû hangi bedeldir?',['Bedel-i iştimâl','Bedel-i küll','Bedel-i ba‘z','Bedel-i galat'],'Küll-cüz dışı bir ilgi.'),
(45,'İ‘râb zât bakımından kaç kısımdır?',['Üç: hareke, harf, hazf','İki','Dört','On'],'Toplam on alâmet.'),
(46,'Gayr-i munsarif lâm alırsa ne olur?',['Kesre alır (munsarif olur)','Tenvin alır','Mebnî olur','Değişmez'],'Merartu bi’l-Ahmeri.'),
(47,'“El-‘asâ” kelimesinin i‘râbı nasıldır?',['Üç hâlde de takdîrî','Lafzî','Mahallî','Mebnî'],'Sonu elif olan isim.'),
(48,'“Lâ havle ve lâ kuvvete” gibi ifadelerde kaç vecih câizdir?',['Beş','İki','Üç','Dört'],'Beş vecih sayılır.')]
sor=[{'b':b,'s':s,'k':k,'d':0,'a':a} for b,s,k,a in Q]
out={'id':'izhar','baslik':'İzhâru’l-Esrâr','kaynak':'İmam Birgivî (ö. 981/1573), İzhâru’l-esrâr fi’n-nahv. Metin; Türkçe açıklama ve sorular el-Mihrâb için hazırlanmıştır.','bolumler':bol,'sorular':sor}
json.dump(out,open('data/kitap/izhar.json','w'),ensure_ascii=False)
print(len(bol),sum(len(b['p']) for b in bol),len(sor))
