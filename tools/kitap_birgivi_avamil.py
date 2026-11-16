import json,re
L=open('/tmp/avb_lines.txt').read().split('\n')
FIX={0:'اَلْحَمْدُ لِلّٰهِ رَبِّ الْعَالَمِينَ وَالصَّلَوةُ وَالسَّلاَمُ',18:'اَلْاَوَّلُ: اَلْبَاءُ. نَحْوُ: آمَنْتُ بِاللّٰهِ.',20:'وَالثّاَلِثُ: إِلَى. نَحْوُ: تُبْتُ اِلَى اللّٰهِ تَعَالَى.',21:'وَالرَّابِعُ: عَنْ. نَحْوُ: كُفِفْتُ عَنِ الْحَرَامِ.',
23:'وَالسَّادِسُ: اَللاَّمُ. نَحْوُ: اَنَا عَبْدٌ لِلّٰهِ تَعَالَى.',29:'وَالثّاَنِي عَشَرَ: تاَءُ الْقَسَمِ. نَحْوُ: تَاللّٰهِ لَاَفْعَلَنَّ الْفَرَائِضَ.',33:'وَالسَّادِسَ عَشَرَ: خَلاَ. نَحْوُ: هَلَكَ الْعَالِمُونَ خَلاَ الْعَامِلِ بِعِلْمِهِ.',
37:'وَالْعِشْرُونَ: لَعَلَّ فِي لُغَةِ عُقَيْلٍ. نَحْوُ: لَعَلَّ اللّٰهِ تَعَالَى يَغْفِرُ ذُنُوبِي.',39:'اَلْاَوَّلُ: إِنَّ. نَحْوُ: اِنَّ اللّٰهَ تَعَالَى عَالِمُ كُلِّ شَيْءٍ.',40:'وَالثّاَنِي: أَنَّ. نَحْوُ: اَعْتَقِدُ اَنَّ اللّٰهَ تَعَالَى قَادِرٌ عَلَى كُلِّ شَيْءٍ.',
55:'اَلْاَوَّلُ: اَنْ. نَحْوُ: اُحِبُّ اَنْ اُطِيعَ اللّٰهَ تَعَالَى.',56:'وَالثّاَنِي: لَنْ. نَحْوُ: لَنْ يَغْفِرَ اللّٰهُ تَعَالَى لِلْكَافِرِينَ.',57:'وَالثّاَلِثُ: كَيْ. نَحْوُ: اُحِبُّ طُولَ الْعُمْرِ كَيْ اُحَصِّلَ الْعِلْمَ.',58:'وَالرَّابِعُ: اِذَنْ. نَحْوُ قَوْلِكَ: اِذَنْ تَدْخُلَ الْجَنَّةَ، لِمَنْ قَالَ: اُطِيعُ اللّٰهَ تَعَالَى.',
61:'اَلْاُولَى: لَمْ. نَحْوُ قَوْلِهِ تَعَالَى: لَمْ يَلِدْ وَلَمْ يُولَدْ.',62:'وَالثّاَنِيَةُ: لَمَّا. نَحْوُ: لَمَّا يَنْفَعْ عُمْرِي.',68:'وَالسَّابِعَةُ: مَا. نَحْوُ: مَا تَفْعَلْ مِنْ خَيْرٍ تَجِدْهُ عِنْدَ اللّٰهِ تَعَالَى.',76:'وَالْخَامِسَةَ عَشَرَ: اِذَامَا. نَحْوُ: اِذَامَا تَعْمَلْ بِعِلْمِكَ تَكُنْ خَيْرَ النَّاسِ.',
79:'اَلْاَوَّلُ: اَلْفِعْلُ مُطْلَقاً. فَكُلُّ فِعْلٍ يَرْفَعُ وَيَنْصِبُ.',94:'نَحْوُ: اَلْعِبَادَةُ حَسَنٌ ثَوَابُهَا. وَالْمَعْصِيَةُ قَبِيحٌ عَذَابُهَا.',97:'وَالسَّادِسُ: اَلْمَصْدَرُ. فَهُوَ اَيْضاً يَعْمَلُ عَمَلَ فِعْلِهِ.',99:'وَالسَّابِعُ: اَلْاِسْمُ الْمُضَافُ. فَهُوَ يَعْمَلُ الْجَرَّ.',101:'وَالثّاَمِنُ: اَلْاِسْمُ الْمُبْهَمُ التَّامُّ. فَهُوَ يَعْمَلُ النَّصْبَ.',102:'نَحْوُ: اَلتَّرَاوِيحُ عِشْرُونَ رَكْعَةً.',
108:'اَلْاَوَّلُ: رَافِعُ الْمُبْتَدَإِ وَالْخَبَرِ. نَحْوُ: مُحَمَّدٌ رَسُولُ اللّٰهِ.',109:'وَالثّاَنِي: رَافِعُ الْفِعْلِ الْمُضَارِعِ. نَحْوُ: يَرْحَمُ اللّٰهُ تَعَالَى التَّائِبَ.',110:'اَلْبَابُ الثّاَنِي فِي الْمَعْمُولِ',
113:'وَهُوَ عَلَى ضَرْبَيْنِ: مَعْمُولٌ بِالْاَصَالَةِ، وَمَعْمُولٌ بِالتَّبَعِيَّةِ؛ اَيْ اِعْرَابُهُ يَكُونُ مِثْلَ اِعْرَابِ مَتْبُوعِهِ.',122:'وَالثّاَلِثُ وَالرَّابِعُ: اَلْمُبْتَدَأُ وَالْخَبَرُ. نَحْوُ: مُحَمَّدٌ خَاتَمُ الْاَنْبِيَاءِ عَلَيْهِمُ الصَّلَوةُ وَالسَّلاَمُ.',
126:'وَالسَّابِعُ: خَبَرُ لاَ لِنَفْيِ الْجِنْسِ. نَحْوُ: لاَ عَمَلَ مُرَاءٍ مَقْبُولٌ.',127:'وَالثّاَمِنُ: اِسْمُ مَا وَلاَ الْمُشَبَّهَتَيْنِ بِلَيْسَ. نَحْوُ: مَا التَّكَبُّرُ لاَئِقاً لِلْعَالِمِ وَلاَ حَسَدٌ حَلاَلاً.',
134:'وَالرَّابِعُ: اَلْمَفْعُولُ لَهُ. نَحْوُ: اِعْمَلْ طَلَباً لِمَرْضَاةِ اللّٰهِ تَعَالَى.',139:'وَالتَّاسِعُ: خَبَرُ بَابِ كَانَ. نَحْوُ: كَانَ الْمَلاَئِكَةُ عِبَادَ اللّٰهِ تَعَالَى.',141:'وَالْحَادِيَ عَشَرَ: اِسْمُ لاَ لِنَفْيِ الْجِنْسِ. نَحْوُ: لاَ طَاعَةَ مُغْتَابٍ مَقْبُولَةٌ.',145:'نَحْوُ: اُحِبُّ اَنْ يُغْفَرَ ذُنُوبِي.',
156:'وَالْفَاءُ. نَحْوُ: تَجِبُ تَكْبِيرَةُ الْاِفْتِتَاحِ فَالْقِيَامُ.',158:'وَحَتَّى. نَحْوُ: مَاتَ النَّاسُ حَتَّى الْاَنْبِيَاءُ عَلَيْهِمُ الصَّلَوةُ وَالسَّلاَمُ.',159:'وَاَوْ. نَحْوُ: صَلِّ الضُّحَى اَرْبَعاً اَوْ ثَمَانِياً.',160:'وَاِمَّا. نَحْوُ: اِعْمَلْ اِمَّا وَاجِباً وَاِمَّا مُسْتَحَبّاً.',161:'وَاَمْ. نَحْوُ: أَرِضَاءَ اللّٰهِ تَعَالَى تَطْلُبُ اَمْ سَخَطَهُ؟',162:'وَلاَ. نَحْوُ: اِعْمَلْ صَالِحاً لاَ سَيِّئاً.',163:'وَبَلْ. نَحْوُ: اُطْلُبْ حَلاَلاً بَلْ طَيِّباً.',164:'وَلَكِنْ. نَحْوُ: لاَ يَحِلُّ رِيَاءٌ لَكِنْ اِخْلاَصٌ.',
174:'وَهُوَ اِمَّا حَرَكَةٌ اَوْ حَرْفٌ اَوْ حَذْفٌ.',184:'فَالْجُمْلَةُ عَشَرَةٌ. وَاَنْوَاعُ الْمُعْرَبِ بِالْقِيَاسِ اِلَى مَا اُعْطِيَ لَهَا مِنْ هٰذِهِ الْعَشَرَةِ تِسْعَةٌ.',
190:'وَالْاَوَّلُ اِمَّا تَامُّ الْاِعْرَابِ، وَهُوَ اَنْ يَكُونَ رَفْعُهُ بِالضَّمَّةِ وَنَصْبُهُ بِالْفَتْحَةِ وَجَرُّهُ بِالْكَسْرَةِ.',193:'نَحْوُ: جَاءَنَا الرَّسُولُ وَصَدَّقْنَا الرَّسُولَ وَآمَنَّا بِالرَّسُولِ عَلَيْهِ السَّلاَمُ.',199:'نَحْوُ: جَاءَنَا اَحْمَدُ وَصَدَّقْنَا اَحْمَدَ وَآمَنَّا بِاَحْمَدَ عَلَيْهِ السَّلاَمُ.',
213:'الْمُذَكَّرِ السَّالِمُ وَ"اُولُو" وَ"عِشْرُونَ" وَاَخَوَاتُهَا.',219:'بِالْاِثْنَيْنِ كِلَيْهِمَا.',230:'نَحْوُ: اَلْاَوْلِيَاءُ وَالْعُلَمَاءُ يَشْفَعَانِ يَوْمَ الْقِيَامَةِ،'}
for k,v in FIX.items(): L[k]=v
def temiz(x):
    x=re.sub(r'(?<=[\u0628-\u064A])ا([\u064E])',lambda m:m.group(1)+'ا',x)
    x=re.sub(r'اْل(?=[\u0621-\u064A])','الْ',x)
    x=re.sub(r'(?<=[\u0621-\u064A])([\u064A\u0648])([\u064E-\u0650])(?=[\u0621-\u064A])',lambda m:m.group(2)+m.group(1) if False else m.group(0),x)
    x=x.replace('تُسَمَّي','تُسَمَّى').replace('عَلٰي','عَلَى').replace('عَلَي','عَلَى').replace('اِلَي','اِلَى').replace('تَعَالَي','تَعَالَى').replace('تَعَالٰي','تَعَالَى')
    x=x.replace('\u06EA','\u0650').replace('\u06EB','')
    x=re.sub(r'(?<=[\u0628-\u064A])(\u0651)ا(\u064E)',r'\1\2ا',x)
    x=re.sub(r'(?<=[\u0628-\u064A])ي(\u0650)(?=[\s.،:]|$)',r'\1ي',x)
    x=re.sub(r'(?<=[\u0628-\u064A])و(\u064F)',r'\1و',x)
    x=x.replace('اَْلَا','اَلْاَ').replace('اَْل','اَلْ').replace('بِاْ لَا','بِالْاَ').replace('بِاْ ','بِالْ').replace('اْلَا','الْاَ').replace('الاْيِ','الْاِي').replace('اْلَ','الَ')
    x=re.sub(r'(?<=[\u064E\u0651])ي(?=[\s.،:!؟,)\]]|$)','ى',x)
    x=re.sub(r'([\u0650])\1+',r'\1',x)
    return re.sub(r'\s+',' ',x).strip()
def g(a,b): return temiz(' '.join(L[i].strip() for i in range(a,b+1) if L[i].strip() and not re.fullmatch(r'[\s|\-"]*',L[i]) and i not in (111,151,112,123,175,176,178,179,181,182,192,194,198,202,208)))
# (bölüm başlığı, [ (aralık, Türkçe) ... ])
B=[
('Mukaddime','مقدمة',[((0,1),'Âlemlerin Rabbi Allah’a hamd, Muhammed’e ve bütün âline salât ve selâm olsun.'),
 ((2,2),'Bundan sonra bil ki i‘râbı öğrenmek isteyen her talebenin yüz şeyi bilmesi gerekir:'),
 ((3,5),'Bunların altmışına âmil, otuzuna ma‘mûl, onuna amel ve i‘râb denir.'),
 ((6,9),'Allah’ın izniyle bu üçünü sana kısaca üç bâbta açıklıyorum: Birinci bâb âmil, ikinci bâb ma‘mûl, üçüncü bâb i‘râb hakkındadır.')]),
('Âmil: cer harfleri','العامل: حروف الجر',[((10,14),'Birinci bâb: Âmil. Âmil iki türlüdür: lafzî ve ma‘nevî. Lafzî âmil ikiye ayrılır: semâî ve kıyâsî. Semâî âmiller kırk dokuzdur ve beş nevidir.'),
 ((15,17),'Birinci nevi: Yalnız bir ismi cerreden harfler. Bunlara cer harfleri ve izâfet harfleri denir; yirmi tanedir:'),
 ((18,18),'1. Bâ: “Allah’a iman ettim.”'),((19,19),'2. Min: “Her günahtan tövbe ettim.”'),((20,20),'3. İlâ: “Allah’a tövbe ettim.”'),((21,21),'4. ‘An: “Harama karşı engellendim (ondan alıkonuldum).”'),
 ((22,22),'5. ‘Alâ: “Tövbe her günahkâra vâcibdir.”'),((23,23),'6. Lâm: “Ben Allah’ın kuluyum.”'),((24,24),'7. Fî: “İtaatkâr cennettedir.”'),((25,25),'8. Kâf: “O’nun benzeri hiçbir şey yoktur.” (Şûrâ 11)'),
 ((26,26),'9. Hattâ: “Ölüme kadar Allah’a ibadet ederim.”'),((27,27),'10. Rubbe: “Nice Kur’an okuyan vardır ki Kur’an ona lânet eder.”'),((28,28),'11. Kasem vâvı: “Vallahi büyük günahları işlemem.”'),
 ((29,29),'12. Kasem tâsı: “Tallahi farzları mutlaka yaparım.”'),((30,30),'13. Hâşâ: “Âlim müstesnâ insanlar helak oldu.”'),((31,31),'14. Muz: “Bulûğ gününden beri işlediğim her günahtan tövbe ettim.”'),
 ((32,32),'15. Munzu: “Namaz bulûğ gününden itibaren farzdır.”'),((33,33),'16. Halâ: “İlmiyle amel eden müstesnâ âlimler helak oldu.”'),((34,34),'17. ‘Adâ: “İhlâslı olan müstesnâ amel edenler helak oldu.”'),
 ((35,35),'18. Levlâ: “Ey Allah’ın rahmeti, sen olmasaydın insanlar helak olurdu!”'),((36,36),'19. Keyme: “Niçin isyan ettin?”'),((37,37),'20. Ukayl lehçesinde le‘alle: “Umulur ki Allah günahlarımı bağışlar.”')]),
('İnne ve kardeşleri; mâ ve lâ','إنّ وأخواتها، ما ولا',[((38,38),'İkinci nevi: İsmi nasbedip haberi ref‘ eden harfler; sekiz tanedir:'),
 ((39,39),'1. İnne: “Şüphesiz Allah her şeyi bilendir.”'),((40,40),'2. Enne: “Allah’ın her şeye kâdir olduğuna inanırım.”'),((41,41),'3. Keenne: “Haram sanki ateştir.”'),
 ((42,42),'4. Lâkinne: “Câhil kurtuluşa ermedi, fakat âlim kurtuluşa erendir.”'),((43,43),'5. Leyte: “Keşke ilim herkese nasip olsa.”'),((44,44),'6. Le‘alle: “Umulur ki Allah günahımı bağışlayandır.”'),
 ((45,45),'Bu altısına fiile benzeyen harfler (hurûf-ı müşebbehe bi’l-fi‘l) denir.'),((46,47),'7. Munkatı‘ istisnâdaki illâ: “Günah cennetten uzaklaştırır; ama taat ona yaklaştırır.”'),
 ((48,49),'8. Cinsi nefyeden lâ: “Kötülük yapan hiç kimse kurtulmaz.”'),
 ((50,52),'Üçüncü nevi: İsmi ref‘, haberi nasbeden iki harf: leyse’ye benzeyen mâ ve lâ. “Allah bir mekânda yerleşmiş değildir; hiçbir şey de Allah’a benzer değildir.”')]),
('Muzâriyi nasb ve cezmedenler','نواصب المضارع وجوازمه',[((53,54),'Dördüncü nevi: Muzâri fiili nasbeden harfler; dört tanedir:'),
 ((55,55),'1. En: “Allah’a itaat etmeyi severim.”'),((56,56),'2. Len: “Allah kâfirleri asla bağışlamaz.”'),((57,57),'3. Key: “İlim tahsil edeyim diye uzun ömrü severim.”'),
 ((58,58),'4. İzen: “Allah’a itaat ederim” diyene “O hâlde cennete girersin” demen gibi.'),
 ((59,60),'Beşinci nevi: Muzâri fiili cezmeden kelimeler; on beş tanedir:'),
 ((61,61),'1. Lem: “Doğurmadı ve doğurulmadı.” (İhlâs 3)'),((62,62),'2. Lemmâ: “Ömrüm (henüz) fayda vermedi.”'),((63,63),'3. Emir lâmı: “Salih amel işlesin.”'),((64,64),'4. Nehiy lâsı: “Günah işleme.”'),
 ((65,65),'Bu dördü tek bir fiili cezmeder.'),((66,66),'5. İn: “Tövbe edersen günahların bağışlanır.”'),((67,67),'6. Mehmâ: “Ne yaparsan ondan sorulursun.”'),
 ((68,68),'7. Mâ: “Hayırdan ne yaparsan onu Allah katında bulursun.”'),((69,69),'8. Men: “Kim salih amel işlerse kurtulur.”'),((70,70),'9. Eyne: “Nerede olursanız ölüm sizi bulur.”'),
 ((71,71),'10. Metâ: “Ne zaman haset edersen helak olursun.”'),((72,72),'11. Ennâ: “Nerede günah işlersen Allah seni bilir.”'),((73,73),'12. Eyy: “Hangi âlim kibirlenirse Allah ona gazap eder.”'),
 ((74,74),'13. Haysümâ: “Nerede yaparsan yaptığın yazılır.”'),((75,75),'14. İzmâ: “Ne zaman tövbe edersen tövben kabul edilir.”'),((76,76),'15. İzâmâ: “Ne zaman ilminle amel edersen insanların en hayırlısı olursun.”'),
 ((77,77),'Bu on biri, şart ve ceza diye adlandırılan iki fiili cezmeder.')]),
('Kıyâsî ve ma‘nevî âmiller','العوامل القياسية والمعنوية',[((78,80),'Kıyâsî âmiller dokuzdur. 1. Mutlak olarak fiil: Her fiil ref‘ ve nasb eder: “Allah her şeyi yarattı; Kur’an (parça parça) indi.”'),
 ((81,81),'Her fiilin mutlaka bir merfûu bulunur.'),((82,83),'Fiil merfûu ile söz tamamlanırsa ona tam fiil denir: “Allah bildi.”'),
 ((84,85),'Merfûu ile tamamlanmayıp mansûb bir habere ihtiyaç duyarsa nâkıs fiil denir: “Allah bilen ve hikmet sahibidir”; “İsyankâr azaba müstehak oldu.”'),
 ((86,88),'“Günahkâr Allah’tan uzak olmaya devam etti”; “Ruh bedende kaldıkça tövbe kabul edilir”; “Allah cisim değildir.”'),
 ((89,90),'2. İsm-i fâil: ma‘lûm fiilinin amelini yapar: “Her hasetçinin hasedi amelini yakar.”'),((91,92),'3. İsm-i mef‘ûl: meçhul fiilinin amelini yapar: “Her tövbe edenin tövbesi kabul olunur.”'),
 ((93,94),'4. Sıfat-ı müşebbehe: fiilinin amelini yapar: “İbadetin sevabı güzeldir, günahın azabı çirkindir.”'),((95,96),'5. İsm-i tafdîl: fiilinin amelini yapar: “Hilmin kendisinde, âlimdekinden daha güzel olduğu hiçbir adam yoktur.”'),
 ((97,98),'6. Masdar: o da fiilinin amelini yapar: “Allah, kulunun bir fakire bir dirhem vermesini sever.”'),((99,100),'7. Muzâf isim: cer amel eder: “Allah’a ibadet hayırdır.”'),
 ((101,102),'8. Tam mübhem isim: nasb amel eder: “Teravih yirmi rekâttır.”'),
 ((103,106),'9. Fiil mânâsı: kendisinden fiil mânâsı anlaşılan her lafız: “Günahkâr Allah’tan ne uzak!”, “Günahı bırak!”; “Dünyada rahatlık yoktur”; “Âlimin ahlâkının Muhammedî olması gerekir.”'),
 ((107,109),'Ma‘nevî âmil ikidir: 1. Mübtedâ ve haberi ref‘ eden (ibtidâ): “Muhammed Allah’ın resulüdür.” 2. Muzâri fiili ref‘ eden: “Allah tövbe edene merhamet eder.”')]),
('Ma‘mûl: aslen ma‘mûl olanlar','المعمول بالأصالة',[((110,113),'İkinci bâb: Ma‘mûl. İki türlüdür: aslen ma‘mûl ve tâbi olarak ma‘mûl; ikincisinin i‘râbı metbûunun i‘râbı gibidir.'),
 ((114,118),'Birinci türün dört nevi vardır: merfû, mansûb, isme mahsus mecrûr ve fiile mahsus meczûm.'),
 ((119,121),'Merfû dokuzdur: 1. Fâil: “Allah tövbe edene merhamet etti.” 2. Nâib-i fâil: “Tövbe edene merhamet edildi.”'),
 ((122,122),'3–4. Mübtedâ ve haber: “Muhammed (a.s.) peygamberlerin sonuncusudur.”'),((124,125),'5. Kâne ve kardeşlerinin ismi: “Allah bilen ve hikmet sahibidir.” 6. İnne bâbının haberi: “Öldükten sonra dirilme haktır.”'),
 ((126,127),'7. Cins nefyeden lânın haberi: “Riyakârın ameli makbul değildir.” 8. Leyse’ye benzeyen mâ ve lânın ismi: “Kibir âlime yakışır değildir; haset de helal değildir.”'),
 ((128,129),'9. Nâsıb ve câzimlerden boş olan muzâri fiil: “Allah tevazuu sever.”'),
 ((130,133),'Mansûb on üçtür: 1. Mef‘ûl-i mutlak: “Halis bir tövbe ile tövbe ettim.” 2. Mef‘ûlün bih: “Allah’a ibadet ederim.” 3. Mef‘ûlün fîh: “Ramazan ayını oruçla geçir.”'),
 ((134,135),'4. Mef‘ûlün leh: “Allah’ın rızasını isteyerek amel et.” 5. Mef‘ûlün maah: “Mal yok olur, amelinle birlikte (sen) kalırsın.”'),
 ((136,138),'6. Hâl: “Allah’a korkarak ve umarak ibadet ederim.” 7. Temyîz: “Âlim ibadetçe güzelleşti.” 8. Müstesnâ: “Kâfir müstesnâ insanlar cennete girer.”'),
 ((139,141),'9. Kâne bâbının haberi: “Melekler Allah’ın kullarıydı.” 10. İnne bâbının ismi: “Şüphesiz (kabirdeki) sorgu haktır.” 11. Cins nefyeden lânın ismi: “Gıybet edenin hiçbir taati makbul değildir.”'),
 ((142,143),'12. Leyse’ye benzeyen mâ ve lânın haberi: “Gıybet helal değildir, laf taşımak da câiz değildir.”'),((144,145),'13. Nâsıblardan biri giren muzâri: “Günahlarımın bağışlanmasını severim.”'),
 ((146,148),'Mecrûr ikidir: 1. Cer harfiyle mecrûr: “İhlâsla amel et.” 2. İzâfetle mecrûr: “Kulun günahı kalbini karartır.”'),
 ((149,150),'Meczûm birdir: Câzimlerden biri giren muzâri fiil: “İhlâslı olursan amelin kabul olunur.”')]),
('Tâbiler','التوابع',[((151,153),'İkinci tür (tâbi olarak ma‘mûl) beştir: 1. Sıfat: “Yüce Allah’a ibadet ederim.”'),
 ((154,155),'2. On harften biriyle atıf: Vâv: “Allah’a ve Resûl’e itaat ederim.”'),((156,157),'Fâ: “İftitah tekbiri, ardından kıyam vâcibdir.” Sümme: “Önce ilim, sonra amel gerekir.”'),
 ((158,158),'Hattâ: “İnsanlar öldü, peygamberler (a.s.) bile.”'),((159,160),'Ev: “Kuşluk namazını dört veya sekiz rekât kıl.” İmmâ: “Ya vâcib ya müstehap bir amel işle.”'),
 ((161,161),'Em: “Allah’ın rızasını mı istiyorsun, yoksa gazabını mı?”'),((162,164),'Lâ: “Salih amel işle, kötü değil.” Bel: “Helal iste, hatta temiz olanı.” Lâkin: “Riya helal değildir; ama ihlâs (helaldir).”'),
 ((165,166),'3. Tekid: “İhlâsı iste, ihlâsı!”; “Günahların hepsini bırak.”'),
 ((167,170),'4. Bedel: “Rabbine, âlemlerin ilâhına ibadet et”; “İnsanlardan Allah’a isyan edene buğzet”; “Allah’ın hakkını gözet.”'),
 ((171,172),'5. Atf-ı beyân: “Peygamberimiz Muhammed’e (a.s.) iman ettik.”')]),
('İ‘râb','الإعراب',[((173,174),'Üçüncü bâb: İ‘râb. İ‘râb ya hareke, ya harf ya da hazf ile olur.'),
 ((177,177),'Hareke üçtür: damme, fetha ve kesre.'),((180,180),'Harf dörttür: vâv, yâ, elif ve nûn.'),
 ((183,183),'Hazf üçtür ve fiile mahsustur: harekenin hazfı, son harfin hazfı ve nûnun hazfı.'),
 ((184,189),'Toplamı ondur. Mu‘rebin bu ondan kendisine verilene göre nevileri dokuzdur; çünkü i‘râb ya yalnız hareke ya yalnız harf ile olur (ikisi isme mahsustur), ya hareke ile birlikte hazf ya harf ile birlikte hazf ile olur (ikisi fiile mahsustur).'),
 ((190,195),'Birincisi (yalnız hareke) ya tam i‘râbdır: ref‘i damme, nasbı fetha, cerri kesre ile; bu, munsarif müfred ve munsarif cem‘-i teksîrdir: “Resul bize geldi, Resul’ü tasdik ettik, Resul’e iman ettik”; “Gökten kitaplar indi…”'),
 ((196,199),'Ya da nâkıs i‘râbdır; iki kısımdır: Ref‘i damme, nasb ve cerri fetha ile olan: gayr-i munsarif: “Ahmed (a.s.) bize geldi…”'),
 ((200,203),'Ref‘i damme, nasb ve cerri kesre ile olan: cem‘-i müennes sâlim: “Bize mucizeler geldi, mucizeleri tasdik ettik, mucizelere iman ettik.”'),
 ((204,210),'İkincisi (yalnız harf) ya tam i‘râbdır: ref‘i vâv, nasbı elif, cerri yâ ile; bu, mütekellim yâsı dışındakine muzâf, müfred ve mükebber esmâ-i sittedir: ebûhu, ehûhu, hamûhâ, henûhu, fûhu, zû mâl. “Ebü’l-Kâsım (a.s.) bize geldi…”'),
 ((211,215),'Ya da nâkıs i‘râbdır: Ref‘i vâv, nasb ve cerri yâ ile olan: cem‘-i müzekker sâlim, ülû, ‘işrûn ve kardeşleri: “Peygamberler bize geldi…”'),
 ((216,219),'Ref‘i elif, nasb ve cerri yâ ile olan: tesniye, isnân ve zamire muzâf kilâ: “İkisi, yani Kitap ve Sünnet bize geldi; ikisine de uyduk, ikisiyle de amel ettik.”'),
 ((220,223),'Üçüncüsü (hareke ile birlikte hazf) yalnız tam i‘râb olur; iki kısımdır: Ref‘i damme, nasbı fetha, cezmi harekenin hazfıyla olan: sonuna zamir bitişmemiş, son harfi sahih muzâri: “Şefaat olunmayı ve mahrum bırakılmamayı sever.”'),
 ((224,226),'Ref‘i damme, nasbı fetha, cezmi son harfin hazfıyla olan: sonuna zamir bitişmemiş, son harfi illet harfi olan muzâri: “Allah’tan bizi affetmesini ve ateşe atmamasını dileriz.”'),
 ((227,231),'Dördüncüsü (harf ile birlikte hazf) yalnız nâkıs i‘râb olur: sonuna nûn dışında bir zamir bitişen muzâri: ref‘i nûn ile, nasb ve cezmi nûnun hazfıyla: “Veliler ve âlimler kıyamet günü şefaat ederler; bize şefaat etmelerini ve bizden yüz çevirmemelerini umarız.”'),
 ((232,233),'Sonra i‘râb lafızda görünürse lafzî denir; zikredilen örneklerde olduğu gibi.'),((234,235),'Lafızda görünmeyip sonunda takdir edilirse takdîrî denir: “Ben isyankârım (el-‘âsî).”'),
 ((236,237),'Ne görünür ne de sonunda takdir edilirse mahallî denir: “Hayrın ancak kendi tarafından geldiği Zât’a (men) tevekkül ettik.”')]),
]
K={'id':'birgivi','baslik':'Avâmil (İmam Birgivî)','kaynak':'İmam Birgivî Mehmed Efendi (ö. 981/1573)','bolumler':[],'sorular':[]}
for tr_b,b,pars in B:
    p=[g(*r) for r,_ in pars]; t=[x for _,x in pars]
    K['bolumler'].append({'b':b,'tr_b':tr_b,'p':p,'tr':t})
def S(b,s,k,a=''): K['sorular'].append({'b':b,'s':s,'k':k,'d':0,'a':a})
S(0,'Avâmil’e göre i‘râbı öğrenmek isteyen kaç şeyi bilmelidir?',['Yüz','Altmış','Otuz','On'],'60 âmil, 30 ma‘mûl, 10 i‘râb.')
S(0,'Âmillerin sayısı kaçtır?',['Altmış','Yüz','Kırk dokuz','Dokuz'])
S(1,'Semâî âmiller kaç tanedir?',['Kırk dokuz','Altmış','Yirmi','On beş'])
S(1,'Cer harfleri kaç tanedir?',['Yirmi','Sekiz','On beş','Dört'])
S(1,'Hangisi cer harfi değildir?',['لَنْ','رُبَّ','حَتَّى','مُذْ'])
S(2,'İsmi nasbedip haberi ref‘ eden harfler kaç tanedir?',['Sekiz','Altı','Dört','İki'])
S(2,'Fiile benzeyen harfler (müşebbehe bi’l-fi‘l) hangisidir?',['إِنَّ وأخواتها','حروف الجر','ما ولا','لم ولما'])
S(2,'Leyse’ye benzeyen iki harf hangileridir?',['مَا ve لَا','إِنَّ ve أَنَّ','لَمْ ve لَمَّا','أَنْ ve لَنْ'])
S(3,'Muzâriyi nasbeden harfler hangileridir?',['أَنْ، لَنْ، كَيْ، إِذَنْ','لَمْ، لَمَّا، لَا، لِ','إِنْ، مَا، مَنْ، مَهْمَا','إِنَّ، أَنَّ، كَأَنَّ، لَيْتَ'])
S(3,'Muzâriyi cezmeden kelimeler kaç tanedir?',['On beş','On bir','Dört','Yirmi'])
S(3,'İki fiili (şart ve ceza) cezmedenler kaç tanedir?',['On bir','Dört','On beş','Dokuz'])
S(4,'Kıyâsî âmiller kaç tanedir?',['Dokuz','İki','Kırk dokuz','On üç'])
S(4,'Merfûu ile tamamlanmayıp mansûb habere muhtaç fiile ne denir?',['Nâkıs fiil','Tam fiil','Meçhul fiil','Muzâri'])
S(4,'Ma‘nevî âmiller kaç tanedir?',['İki','Dokuz','Bir','Dört'])
S(5,'Merfû ma‘mûller kaç tanedir?',['Dokuz','On üç','İki','Beş'])
S(5,'Mansûb ma‘mûller kaç tanedir?',['On üç','Dokuz','İki','Bir'])
S(5,'“اُعْبُدُ اللّٰهَ خَائِفاً” örneğindeki “خَائِفاً” nedir?',['Hâl','Temyîz','Mef‘ûl-i mutlak','Müstesnâ'])
S(6,'Tâbiler kaç tanedir?',['Beş','Dört','On','Üç'])
S(6,'Atıf harfleri kaç tanedir?',['On','Beş','Yirmi','Sekiz'])
S(7,'Hazf ile i‘râb hangi kelime türüne mahsustur?',['Fiile','İsme','Harfe','Hepsine'])
S(7,'Ref‘i damme, nasb ve cerri fetha ile olan hangisidir?',['Gayr-i munsarif','Cem‘-i müennes sâlim','Esmâ-i sitte','Tesniye'])
S(7,'Lafızda görünmeyip sonda takdir edilen i‘râba ne denir?',['Takdîrî','Lafzî','Mahallî','Tam'])
json.dump(K,open('/home/claude/el-mihrab/data/kitap/birgivi.json','w'),ensure_ascii=False,separators=(',',':'))
print(sum(len(b['p']) for b in K['bolumler']),'paragraf', len(K['sorular']),'soru')
