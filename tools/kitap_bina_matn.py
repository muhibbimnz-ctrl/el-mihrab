import json
L=[l.strip() for l in open('tools/bina_matn.txt') if l.strip()]
L[48]=L[48]+' '+L.pop(49)
TR=[
'Bil ki tasrîf bâbları otuz beştir; bunlardan altısı sülâsî mücerred içindir.',
'Birinci bâb: fe‘ale yef‘ulü; misali nasara yansuru. Alâmeti, ayn’ül-fiilin mâzîde fethalı, muzâride dammeli olmasıdır. Binâsı çoğunlukla ta‘diye (geçişlilik) içindir, bazen lâzım olur. Müteaddî örneği: “Zeyd Amr’a yardım etti”; lâzım örneği: “Zeyd çıktı.”',
'Müteaddî, fâilin fiilinin mef‘ûlün bihe geçtiği fiildir; lâzım ise fâilin fiilinin mef‘ûlün bihe geçmeyip kendisinde kaldığı fiildir.',
'İkinci bâb: fe‘ale yef‘ilü; misali daraba yadribu. Alâmeti, ayn’ül-fiilin mâzîde fethalı, muzâride (gâbir) kesreli olmasıdır. Binâsı yine çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd Amr’ı dövdü”; lâzım: “Zeyd oturdu.”',
'Üçüncü bâb: fe‘ale yef‘alü; misali fetaha yeftahu. Alâmeti, ayn’ül-fiilin mâzîde ve muzâride fethalı olmasıdır; şartı ayn’ül-fiilin veya lâm’ül-fiilin boğaz harflerinden olmasıdır. Boğaz harfleri altıdır: hâ, hı, ayn, gayn, he ve hemze. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd kapıyı açtı”; lâzım: “Zeyd gitti.”',
'Dördüncü bâb: fe‘ile yef‘alü; misali alime ya‘lemu. Alâmeti, ayn’ül-fiilin mâzîde kesreli, muzâride fethalı olmasıdır. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd meseleyi bildi”; lâzım: “Zeyd korktu.”',
'Beşinci bâb: fe‘ule yef‘ulü; misali hasune yahsunu. Alâmeti, ayn’ül-fiilin mâzîde ve muzâride dammeli olmasıdır. Binâsı ancak lâzım olur: “Zeyd güzel oldu.”',
'Altıncı bâb: fe‘ile yef‘ilü; misali hasibe yahsibu. Alâmeti, ayn’ül-fiilin mâzîde ve muzâride kesreli olmasıdır. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd Amr’ı faziletli sandı”; lâzım: “Zeyd nimetlendi (refaha erdi).”',
'Bunlardan on ikisi sülâsîden fazla olanlar (sülâsî mezîd) içindir ve üç nevidir. Birinci nevi, sülâsîye bir harf ziyade edilendir; üç bâbdır.',
'Birinci bâb: ef‘ale yuf‘ilu if‘âlen; misali ekrame yukrimu ikrâmen. Alâmeti, mâzîsinin başına hemze ziyadesiyle dört harf olmasıdır. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd Amr’a ikram etti”; lâzım: “Adam sabahladı.”',
'İkinci bâb: fe‘‘ale yufe‘‘ilu tef‘îlen; misali ferraha yuferrihu tefrîhan. Alâmeti, mâzîsinin, fâ ile ayn arasına ayn’ül-fiil cinsinden bir harf ziyadesiyle dört harf olmasıdır. Binâsı çoğunlukla teksîr (çokluk) içindir: bazen fiilde olur — “Zeyd Kâbe’yi çokça tavaf etti”; bazen fâilde — “Develer (birbiri ardınca) öldü”; bazen mef‘ûlde — “Zeyd kapıları (bir bir) kapadı.”',
'Üçüncü bâb: fâ‘ale yufâ‘ilu mufâ‘aleten ve fi‘âlen ve fî‘âlen; misali kâtele yukâtilu mukâteleten ve kitâlen ve kîtâlen. Alâmeti, mâzîsinin fâ ile ayn arasına elif ziyadesiyle dört harf olmasıdır. Binâsı çoğunlukla iki kişi arasında müşâreket (karşılıklılık) içindir, bazen tek kişi için olur. Müşâreket: “Zeyd Amr ile savaştı”; tek kişi: “Allah onları kahretsin.”',
'İkinci nevi, sülâsî mücerrede iki harf ziyade edilendir; beş bâbdır.',
'Birinci bâb: infe‘ale yenfe‘ilu infi‘âlen; misali inkesera yenkesiru inkisâran. Alâmeti, mâzîsinin başına hemze ve nûn ziyadesiyle beş harf olmasıdır. Binâsı mutâvaat içindir. Mutâvaatın mânâsı, müteaddî fiilin taalluku sebebiyle bir şeyin eserinin meydana gelmesidir: “Camı kırdım, o cam kırıldı.” Camın kırılması, müteaddî fiil olan kırmanın taalluku ile meydana gelen bir eserdir.',
'İkinci bâb: ifte‘ale yefte‘ilu ifti‘âlen; misali ictema‘a yectemi‘u ictimâ‘an. Alâmeti, mâzîsinin başına hemze, fâ ile ayn arasına tâ ziyadesiyle beş harf olmasıdır. Binâsı yine mutâvaat içindir: “Develeri topladım, o develer toplandı.”',
'Üçüncü bâb: if‘alle yef‘allu if‘ilâlen; misali ihmerra yahmerru ihmirâran. Alâmeti, mâzîsinin başına hemze, sonuna lâm’ül-fiil cinsinden bir harf ziyadesiyle beş harf olmasıdır. Binâsı lâzımın mübalağası içindir; çünkü Zeyd’de biraz kırmızılık olduğunda “hamira Zeydun”, çok kırmızılık olduğunda “ihmerra Zeydun” denir. Renkler ve ayıplar içindir de denmiştir; renk örneği: “Zeyd kızardı”, ayıp örneği: “Zeyd’in bir gözü kör oldu.”',
'Dördüncü bâb: tefe‘‘ale yetefe‘‘alu tefe‘‘ulen; misali tekelleme yetekellemu tekellumen. Alâmeti, mâzîsinin başına tâ, fâ ile ayn arasına ayn’ül-fiil cinsinden bir harf ziyadesiyle beş harf olmasıdır. Binâsı tekellüf içindir. Tekellüfün mânâsı, istenen şeyi azar azar elde etmektir: “İlmi mesele mesele öğrendim.”',
'Beşinci bâb: tefâ‘ale yetefâ‘alu tefâ‘ulen; misali tebâ‘ade yetebâ‘adu tebâ‘uden. Alâmeti, mâzîsinin başına tâ, fâ ile ayn arasına elif ziyadesiyle beş harf olmasıdır. Binâsı iki veya daha fazla kişi arasında müşâreket içindir. İki kişi arasında: “Zeyd ile Amr birbirinden uzaklaştı”; daha fazlası arasında: “Kavim barıştı.”',
'Üçüncü nevi, sülâsîye üç harf ziyade edilendir; dört bâbdır.',
'Birinci bâb: istef‘ale yestef‘ilu istif‘âlen; misali istahrace yestahricu istihrâcen. Alâmeti, mâzîsinin başına hemze, sîn ve tâ ziyadesiyle altı harf olmasıdır. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd malı çıkardı”; lâzım: “Çamur taşlaştı.” Fiili talep içindir de denmiştir: “Allah’tan mağfiret dilerim.”',
'İkinci bâb: if‘aw‘ale yef‘aw‘ilu if‘î‘âlen; misali i‘şewşebe ya‘şewşibu i‘şîşâben. Alâmeti, mâzîsinin başına hemze, ayn ile lâm arasına ayn’ül-fiil cinsinden bir harf ve vâv ziyadesiyle altı harf olmasıdır. Binâsı lâzımın mübalağası içindir; çünkü yeryüzünde biraz ot bitince “aşuba’l-arzu”, yeryüzünün otu çoğalınca “i‘şewşebe’l-arzu” denir.',
'Üçüncü bâb: if‘awwale yef‘awwilu if‘ivvâlen; misali iclewweze yeclewwizu iclivvâzen. Alâmeti, mâzîsinin başına hemze, ayn ile lâm arasına iki vâv ziyadesiyle altı harf olmasıdır. Binâsı yine lâzımın mübalağası içindir; çünkü develer biraz hızlı yürüyünce “celeze’l-ibilu”, çok hızlı yürüyünce “iclewweze’l-ibilu” denir.',
'Dördüncü bâb: if‘âlle yef‘âllu if‘îlâlen; misali ihmârra yahmârru ihmîrâran. Alâmeti, mâzîsinin başına hemze, ayn ile lâm arasına elif, sonuna lâm’ül-fiil cinsinden bir harf ziyadesiyle altı harf olmasıdır. Binâsı yine lâzımın mübalağası içindir; ancak bu bâb if‘ilâl bâbından daha beliğdir: biraz kırmızılık için “hamira”, mübalağalı kırmızılık için “ihmerra”, daha da mübalağalı kırmızılık için “ihmârra” denir.',
'Bir bâb da rubâî mücerred içindir: fa‘lele yufa‘lilu fa‘leleten ve fi‘lâlen; misali dahrace yudahricu dahraceten ve dihrâcen. Alâmeti, mâzîsinin dört harf olması ve bütün harflerinin aslî olmasıdır. Binâsı çoğunlukla ta‘diye içindir, bazen lâzım olur. Müteaddî: “Zeyd taşı yuvarladı”; lâzım: “Zeyd (eğilip) başını öne indirdi.”',
'Altı bâb da dahrace’nin mülhakı içindir; bu altısına “rubâîye mülhak” denir.',
'Bunların birincisi: fev‘ale yufev‘ilu fev‘aleten ve fî‘âlen; misali havkale yuhavkilu havkaleten ve hîkâlen. Alâmeti, mâzîsinin fâ ile ayn arasına vâv ziyadesiyle dört harf olmasıdır. Binâsı yalnız lâzım içindir: “Zeyd ihtiyarlayıp zayıfladı.”',
'İkinci bâb: fey‘ale yufey‘ilu fey‘aleten ve fî‘âlen; misali baytara yubaytiru baytaraten ve bîtâran. Alâmeti, mâzîsinin fâ ile ayn arasına yâ ziyadesiyle dört harf olmasıdır. Binâsı yalnız ta‘diye içindir: “Zeyd kalemi yardı.”',
'Üçüncü bâb: fa‘vele yufa‘vilu fa‘veleten ve fi‘vâlen; misali cehvere yucehviru cehvereten ve cihvâran. Alâmeti, mâzîsinin ayn ile lâm arasına vâv ziyadesiyle dört harf olmasıdır. Binâsı yine yalnız ta‘diye içindir: “Zeyd Kur’ân’ı yüksek sesle okudu.”',
'Dördüncü bâb: fa‘yele yufa‘yilu fa‘yeleten ve fi‘yâlen; misali ‘asyera yu‘asyiru ‘asyeraten ve ‘isyâran. Alâmeti, mâzîsinin ayn ile lâm arasına yâ ziyadesiyle dört harf olmasıdır. Binâsı yalnız lâzım içindir: “Zeyd (toz kaldırdı / tökezledi).”',
'Beşinci bâb: fa‘lele yufa‘lilu fa‘leleten ve fi‘lâlen; misali celbebe yucelbibu celbebeten ve cilbâben. Alâmeti, mâzîsinin sonuna lâm’ül-fiil cinsinden bir harf ziyadesiyle dört harf olmasıdır. Binâsı ta‘diye içindir: “Zeyd Amr’a cilbâb giydirdi.”',
'Altıncı bâb: fa‘lâ yufa‘lî fa‘leyeten ve fi‘lâen; misali selkâ yuselkî selkayeten ve silkâen. Alâmeti, mâzîsinin sonuna yâ ziyadesiyle dört harf olmasıdır. Binâsı ta‘diye içindir: “Zeyd’i sırtüstü yatırdım.” Bu altısına “rubâîye mülhak” denir; ilhâkın mânâsı iki masdarın, yani mülhak ile mülhakun bihin masdarlarının bir (aynı vezinde) olmasıdır.',
'Üç bâb da rubâî mücerredden fazla olanlar içindir ve iki nevidir. Birinci nevi, rubâîye bir harf ziyade edilendir; tek bâbdır: tefa‘lele yetefa‘lelu tefa‘lulen; misali tedahrace yetedahracu tedahrucen. Alâmeti, mâzîsinin başına tâ ziyadesiyle beş harf olmasıdır. Binâsı mutâvaat içindir: “Taşı yuvarladım, o taş yuvarlandı.”',
'İkinci nevi, rubâîye iki harf ziyade edilendir; iki bâbdır. Birinci bâb: if‘anlele yef‘anlilu if‘inlâlen; misali ihrancema yahrancimu ihrincâmen. Alâmeti, mâzîsinin başına hemze, ayn ile birinci lâm arasına nûn ziyadesiyle altı harf olmasıdır. Binâsı yine mutâvaat içindir: “Develeri bir araya topladım, o develer toplandı.”',
'İkinci bâb: if‘alelle yef‘alillu if‘illâlen; misali ikşa‘arra yakşa‘irru ikşi‘râran. Alâmeti, mâzîsinin başına hemze, sonuna ikinci lâm’ül-fiil cinsinden bir harf ziyadesiyle altı harf olmasıdır. Binâsı lâzımın mübalağası içindir; çünkü adamın derisinin tüyleri biraz ürperince “kaş‘ara cildu’r-racul”, çok ürperince “ikşa‘arra cildu’r-racul” denir.',
'Beş bâb da tedahrace’nin mülhakı içindir. Birinci bâb: tefa‘lele yetefa‘lelu tefa‘lulen; misali tecelbebe yetecelbebu tecelbuben. Alâmeti, mâzîsinin başına tâ, sonuna lâm’ül-fiil cinsinden bir harf ziyadesiyle beş harf olmasıdır. Binâsı mutâvaat içindir: “Zeyd’e cilbâb giydirdim, o da giyindi.”',
'İkinci bâb: tefev‘ale yetefev‘alu tefev‘ulen; misali tecevrebe yetecevrebu tecevruben. Alâmeti, mâzîsinin başına tâ, fâ ile ayn arasına vâv ziyadesiyle beş harf olmasıdır. Binâsı yine mutâvaat içindir: “Ona çorap giydirdim, o da çorap giydi.”',
'Üçüncü bâb: tefey‘ale yetefey‘alu tefey‘ulen; misali teşeytane yeteşeytanu teşeytunen. Alâmeti, mâzîsinin başına tâ, fâ ile ayn arasına yâ ziyadesiyle beş harf olmasıdır. Binâsı yalnız lâzım içindir: “Zeyd şeytanlaştı.”',
'Dördüncü bâb: tefa‘vele yetefa‘velu tefa‘vulen; misali terahveke yeterahveku terahvuken. Alâmeti, mâzîsinin başına tâ, ayn ile lâm arasına vâv ziyadesiyle beş harf olmasıdır. Binâsı yalnız lâzım içindir: “Zeyd salınarak yürüdü.”',
'Beşinci bâb: tefa‘lâ yetefa‘lâ tefa‘liyen; misali teselkâ yeteselkâ teselkiyen. Alâmeti, mâzîsinin başına tâ, sonuna yâ ziyadesiyle beş harf olmasıdır. Binâsı lâzım içindir: “Zeyd sırtüstü düştü.”',
'Bil ki bu mülhaklarda ilhâkın hakikati tâ dışındaki ziyade iledir. Mesela tecelbebe’de ilhâk ancak bânın tekrarıyladır; tâ ise tedahrace’de olduğu gibi mutâvaat mânâsı için girmiştir. Çünkü ilhâk kelimenin başında olmaz, ortasında veya sonunda olur; Şerhu’l-Mufassal’da açıkça böyle denmiştir.',
'İki bâb da ihrancema’nın mülhakı içindir. Birinci bâb: if‘anlele yef‘anlilu if‘inlâlen; misali ik‘ansesa yak‘ansisu ik‘insâsen. Alâmeti, mâzîsinin başına hemze, ayn ile lâm arasına nûn ve sonuna lâm’ül-fiil cinsinden bir harf ziyadesiyle altı harf olmasıdır. Binâsı lâzımın mübalağası içindir; çünkü adamın göğsü biraz çıkıp sırtı içeri girince “ka‘ise’r-racul”, bu çok olunca “ik‘ansesa’r-racul” denir.',
'İkinci bâb: if‘anlâ yef‘anlî if‘inlâen; misali islenkâ yeslenkî islinkâen. Alâmeti, mâzîsinin başına hemze, ayn ile lâm arasına nûn ve sonuna yâ ziyadesiyle altı harf olmasıdır. Binâsı mutâvaat içindir: “Onu sırtüstü yatırdım, o da sırtüstü düştü.”',
'Sonra bil ki bu bâblarda toplanan fiil ya sülâsî mücerred sâlimdir (kerume), ya sülâsî mücerred gayr-i sâlimdir (va‘ade), ya rubâî mücerred sâlimdir (dahrace), ya rubâî mücerred gayr-i sâlimdir (vesvese), ya sülâsî mezîd sâlimdir (ekrame), ya sülâsî mezîd gayr-i sâlimdir (ev‘ade), ya rubâî mezîd sâlimdir (tedahrace), ya da rubâî mezîd gayr-i sâlimdir (tevesvese). Bu kısımlara “sekiz kısım” denir.',
'Sonra bil ki her fiil ya sahihtir: fâ, ayn ve lâmının karşılığında illet harflerinden —vâv, yâ ve elif— biri, hemze ve tad‘îf (aynı harfin tekrarı) bulunmayan fiildir; nasara gibi.',
'Ya misâldir: fâ’ü’l-fiilinin karşılığında illet harfi bulunan fiildir; va‘ade ve yesera gibi.',
'Ya ecvefdir: ayn’ül-fiilinin karşılığında illet harfi bulunan fiildir; kâle ve kâle (ölçtü) gibi.',
'Ya nâkıstır: lâm’ül-fiilinin karşılığında illet harfi bulunan fiildir; gazâ ve ramâ gibi.',
'Ya lefîftir: içinde iki illet harfi bulunan fiildir; iki kısımdır. Birincisi lefîf-i makrûndur: ayn ve lâmının karşılığında bu harflerden ikisi bulunan fiildir; tavâ ve kaviye gibi. İkincisi lefîf-i mefrûktur: fâ ve lâmının karşılığında bu harflerden ikisi bulunan fiildir; vakâ yakî gibi.',
'Ya muzâ‘aftır: ayn’ül-fiili ile lâm’ül-fiili aynı cinsten olan fiildir; medde gibi — aslı medede idi; birinci dâlin harekesi hazfedildi, sonra ikinci dâle idgâm edildi. İdgâm, iki mütecânis harften birini diğerine katmaktır; üç nevidir. Birinci nevi vâcibtir: iki mütecânis harfin ikisi de harekeli olur ya da birincisi sâkin, ikincisi harekeli olur; medde yemuddu gibi. İkinci nevi câizdir: iki mütecânis harften birincisi harekeli, ikincisi ârızî bir sükûnla sâkin olur; dâlin (üç) harekesiyle “lem yemudde/yemuddu/yemuddi” gibi — aslı lem yemdud idi; birinci dâlin harekesi mîme nakledildi, iki sâkin bir araya geldi, sonra ikinci dâl, sükûnu ârızî olduğu için ya damme ya fetha ya da kesre ile harekelendi. Üçüncü nevi mümteni‘dir: iki mütecânis harften birincisi harekeli, ikincisi aslî bir sükûnla sâkin olur; medadtu ve medadne gibi.',
'Ya mehmûzdur: aslî harflerinden biri hemze olan fiildir; ehaze, se’ele ve kara’e gibi. Hemze fâ’ü’l-fiilin karşılığında ise mehmûzü’l-fâ, ayn’ül-fiilin karşılığında ise mehmûzü’l-ayn, lâm’ül-fiilin karşılığında ise mehmûzü’l-lâm denir. Bu kısımlara “yedi kısım” denir; şu beyit onları toplar:',
'“Sahih, misâl, muzâ‘af, lefîf, nâkıs, mehmûz ve ecvef.” (Farsça beyit: “sahîh’est, misâl’est…”)',
'Tamam oldu.',
]
assert len(TR)==len(L),(len(TR),len(L))
def B(b,tr_b,a,z): return {'b':b,'tr_b':tr_b,'p':L[a:z],'tr':TR[a:z]}
bol=[B('الثلاثي المجرد','Sülâsî mücerred — altı bâb',0,8),
     B('الثلاثي المزيد فيه','Sülâsî mezîd — on iki bâb',8,23),
     B('الرباعي المجرد وملحقاته','Rubâî mücerred ve ona mülhak altı bâb',23,31),
     B('الرباعي المزيد فيه وملحقاته','Rubâî mezîd ve mülhakları',31,42),
     B('الأقسام الثمانية والأقسام السبعة','Sekiz kısım ve yedi kısım (sahih, misâl, ecvef, nâkıs, lefîf, muzâ‘af, mehmûz)',42,len(L))]
old=json.load(open('data/kitap/bina.json'))
sor=[]
for q in old['sorular']:
    q=dict(q); q['b']=min(q.get('b',0),len(bol)-1); sor.append(q)
ek=[('Binâ’ya göre tasrîf bâbları kaç tanedir?',['35','6','12','25'],0,'خمسة وثلاثون بابا'),
('Fetaha yeftahu bâbının şartı nedir?',['Ayn veya lâm’ül-fiilin boğaz harfi olması','Fâ’ü’l-fiilin illet harfi olması','Mâzînin dört harfli olması','Lâzım olması'],0,'بشرط أن يكون عين فعله أو لامه حرفا من حروف الحلق'),
('Hasune yahsunu bâbının binâsı nedir?',['Yalnız lâzım','Çoğunlukla müteaddî','Mutâvaat','Müşâreket'],0,'لا يكون إلا لازما'),
('İnfi‘âl bâbının binâsı nedir?',['Mutâvaat','Teksîr','Tekellüf','Talep'],0,'وبناؤه للمطاوعة'),
('Tefa‘‘ul bâbının binâsı nedir?',['Tekellüf','Müşâreket','Mutâvaat','Ta‘diye'],0,'وبناؤه للتكلف'),
('“İhmârra” hangi bâbdandır ve neyi bildirir?',['İf‘îlâl — lâzımda daha ileri mübalağa','İf‘ilâl — renk','İstif‘âl — talep','İfti‘âl — mutâvaat'],0,'هذا الباب أبلغ من باب الافعلال'),
('Binâ’ya göre ilhâkın mânâsı nedir?',['İki masdarın (vezince) bir olması','İki harfin idgâmı','Fiilin müteaddî olması','Hemze ziyadesi'],0,'معنى الإلحاق اتحاد المصدرين'),
('Medadtu’da idgâm neden mümteni‘dir?',['İkinci harf aslî sükûnla sâkin olduğu için','Birinci harf sâkin olduğu için','İki harf de harekeli olduğu için','Hemze bulunduğu için'],0,'والثاني ساكنا بسكون أصلي'),
('Vakâ yakî hangi kısımdandır?',['Lefîf-i mefrûk','Lefîf-i makrûn','Ecvef','Mehmûz'],0,'في مقابلة فائه ولامه حرفان من هذه الحروف'),
('Kâtele yukâtilu bâbının asıl binâsı nedir?',['İki kişi arasında müşâreket','Teksîr','Mutâvaat','Talep'],0,'وبناؤه للمشاركة بين الاثنين غالبا')]
bmap=[0,0,0,1,1,1,2,3,4,1]
for (s,k,d,a),b in zip(ek,bmap): sor.append({'b':b,'s':s,'k':k,'d':d,'a':a})
json.dump({'id':'bina','baslik':'كتاب البناء في الصرف','kaynak':'Mecmûatü’s-sarf — matn','bolumler':bol,'sorular':sor},open('data/kitap/bina.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(bol),len(sor))
