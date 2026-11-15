import json
old=json.load(open('data/kitap/avamil.json'))
B=[]
def b(ar,tr_b,pairs): B.append({'b':ar,'tr_b':tr_b,'p':[x[0] for x in pairs],'tr':[x[1] for x in pairs]})
b('خُطْبَةُ الْكِتَابِ','Kitabın girişi',[
('الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى مُحَمَّدٍ وَآلِهِ وَصَحْبِهِ أَجْمَعِينَ. أَمَّا بَعْدُ:','Hamd âlemlerin Rabbi Allah’a; salât ve selâm Muhammed’e, âline ve bütün ashâbına olsun. Bundan sonra:'),
('فَإِنَّ الْعَوَامِلَ فِي النَّحْوِ - عَلَى مَا أَلَّفَهُ الشَّيْخُ الْإِمَامُ عَبْدُ الْقَاهِرِ بْنُ عَبْدِ الرَّحْمَنِ الْجُرْجَانِيُّ رَحْمَةُ اللَّهِ تَعَالَى عَلَيْهِ - مِائَةُ عَامِلٍ.','Şeyh İmam Abdülkâhir b. Abdirrahman el-Cürcânî’nin (Allah’ın rahmeti üzerine olsun) telif ettiğine göre nahivde âmiller yüz âmildir.'),
('وَهِيَ تَنْقَسِمُ إِلَى قِسْمَيْنِ: لَفْظِيَّةٍ، وَمَعْنَوِيَّةٍ. فَاللَّفْظِيَّةُ مِنْهَا تَنْقَسِمُ إِلَى قِسْمَيْنِ: سَمَاعِيَّةٍ، وَقِيَاسِيَّةٍ.','Bunlar iki kısma ayrılır: lafzî ve ma‘nevî. Lafzî olanlar da iki kısma ayrılır: semâî ve kıyâsî.'),
('فَالسَّمَاعِيَّةُ مِنْهَا أَحَدٌ وَتِسْعُونَ عَامِلًا، وَالْقِيَاسِيَّةُ مِنْهَا سَبْعَةُ عَوَامِلَ، وَالْمَعْنَوِيَّةُ مِنْهَا عَدَدَانِ؛ فَالْجُمْلَةُ مِائَةُ عَامِلٍ.','Semâî olanlar doksan bir âmil, kıyâsî olanlar yedi âmil, ma‘nevî olanlar iki tanedir; toplam yüz âmil eder.'),
('وَالسَّمَاعِيَّةُ مِنْهَا تَتَنَوَّعُ عَلَى ثَلَاثَةَ عَشَرَ نَوْعًا.','Semâî âmiller on üç çeşide ayrılır.')])
b('النَّوْعُ الْأَوَّلُ: حُرُوفٌ تَجُرُّ الِاسْمَ فَقَطْ','1. çeşit: Yalnız ismi cerreden harfler',[
('النَّوْعُ الْأَوَّلُ: حُرُوفٌ تَجُرُّ الِاسْمَ فَقَطْ، وَهِيَ سَبْعَةَ عَشَرَ حَرْفًا:','Birinci çeşit: Yalnız ismi cerreden harflerdir; on yedi harftir:'),
('الْأَوَّلُ: الْبَاءُ؛ لِلْإِلْصَاقِ، نَحْوُ: بِهِ دَاءٌ، وَمَرَرْتُ بِزَيْدٍ.','Birincisi: bâ. İlsâk (bitiştirme) içindir: “Onda bir hastalık var”, “Zeyd’in yanından geçtim.”'),
('وَلِلتَّعْدِيَةِ، نَحْوُ: ذَهَبْتُ بِزَيْدٍ.','Ta‘diye (geçişli kılma) için: “Zeyd’i götürdüm.”'),
('وَلِلِاسْتِعَانَةِ، نَحْوُ: كَتَبْتُ بِالْقَلَمِ.','İstiâne (vasıta) için: “Kalemle yazdım.”'),
('وَلِلْمُصَاحَبَةِ، نَحْوُ: دَخَلْتُ عَلَيْهِ بِثِيَابِ السَّفَرِ.','Musâhabe (beraberlik) için: “Yanına yolculuk elbisesiyle girdim.”'),
('وَلِلْمُقَابَلَةِ، نَحْوُ: بِعْتُ هَذَا بِهَذَا.','Mukâbele (karşılık) için: “Bunu buna karşılık sattım.”'),
('وَلِلزِّيَادَةِ، نَحْوُ قَوْلِهِ تَعَالَى: ﴿وَلَا تُلْقُوا بِأَيْدِيكُمْ إِلَى التَّهْلُكَةِ﴾، ﴿وَكَفَى بِاللَّهِ شَهِيدًا﴾.','Zâid olarak: “Kendinizi kendi ellerinizle tehlikeye atmayın” ve “Şahit olarak Allah yeter” âyetlerindeki gibi.'),
('وَلِلظَّرْفِيَّةِ، نَحْوُ: صَلَّيْتُ بِالْمَسْجِدِ.','Zarfiyet (içinde olma) için: “Mescidde namaz kıldım.”'),
('وَلِلْقَسَمِ، نَحْوُ: بِاللَّهِ لَأَفْعَلَنَّ كَذَا.','Yemin için: “Allah’a yemin ederim ki şunu mutlaka yapacağım.”'),
('وَالثَّانِي: مِنْ؛ لِابْتِدَاءِ الْغَايَةِ، نَحْوُ: سِرْتُ مِنَ الْبَصْرَةِ إِلَى الْكُوفَةِ.','İkincisi: min. Başlangıç noktası için: “Basra’dan Kûfe’ye yürüdüm.”'),
('وَلِلتَّبْعِيضِ، نَحْوُ: أَخَذْتُ مِنَ الْمَالِ.','Teb‘îz (bir kısmını) için: “Maldan aldım.”'),
('وَلِلتَّبْيِينِ، نَحْوُ قَوْلِهِ تَعَالَى: ﴿فَاجْتَنِبُوا الرِّجْسَ مِنَ الْأَوْثَانِ﴾.','Tebyîn (açıklama) için: “Putlardan ibaret olan pislikten kaçının.”'),
('وَلِلزِّيَادَةِ، نَحْوُ: مَا جَاءَنِي مِنْ أَحَدٍ.','Zâid olarak: “Bana hiç kimse gelmedi.”'),
('وَالثَّالِثُ: إِلَى؛ لِانْتِهَاءِ الْغَايَةِ، نَحْوُ: سِرْتُ مِنَ الْبَصْرَةِ إِلَى الْكُوفَةِ.','Üçüncüsü: ilâ. Bitiş noktası için: “Basra’dan Kûfe’ye yürüdüm.”'),
('وَبِمَعْنَى «مَعَ»، نَحْوُ قَوْلِهِ تَعَالَى: ﴿فَاغْسِلُوا وُجُوهَكُمْ وَأَيْدِيَكُمْ إِلَى الْمَرَافِقِ﴾.','“Me‘a” (ile) mânâsına: “Yüzlerinizi ve dirseklerinizle birlikte ellerinizi yıkayın.”'),
('وَالرَّابِعُ: فِي؛ لِلظَّرْفِيَّةِ، نَحْوُ: الْمَالُ فِي الْكِيسِ، وَنَظَرْتُ فِي الْكِتَابِ.','Dördüncüsü: fî. Zarfiyet için: “Mal keseninin içinde”, “Kitaba baktım.”'),
('وَبِمَعْنَى «عَلَى»، نَحْوُ قَوْلِهِ تَعَالَى: ﴿وَلَأُصَلِّبَنَّكُمْ فِي جُذُوعِ النَّخْلِ﴾.','“Alâ” (üzerine) mânâsına: “Sizi hurma dallarına asacağım.”'),
('وَالْخَامِسُ: حَتَّى؛ لِانْتِهَاءِ الْغَايَةِ، نَحْوُ: أَكَلْتُ السَّمَكَةَ حَتَّى رَأْسِهَا.','Beşincisi: hattâ. Bitiş noktası için: “Balığı başına kadar yedim.”'),
('وَالسَّادِسُ: اللَّامُ؛ لِلتَّمْلِيكِ، نَحْوُ: الْمَالُ لِزَيْدٍ.','Altıncısı: lâm. Temlîk (sahiplik) için: “Mal Zeyd’indir.”'),
('وَلِلتَّخْصِيصِ، نَحْوُ: الْجُلُّ لِلْفَرَسِ.','Tahsîs için: “Çul atındır (ata mahsustur).”'),
('وَلِلْقَسَمِ، نَحْوُ: لِلَّهِ لَا يُؤَخَّرُ الْأَجَلُ.','Yemin için: “Allah’a yemin olsun, ecel ertelenmez.”'),
('وَلِلزِّيَادَةِ، كَقَوْلِهِ تَعَالَى: ﴿رَدِفَ لَكُمْ بَعْضُ الَّذِي تَسْتَعْجِلُونَ﴾، «وَلَا أَبَا لَكُمْ».','Zâid olarak: “Acele ettiğiniz şeyin bir kısmı arkanıza gelmiş olabilir” âyetinde ve “lâ ebâ leküm” sözünde olduğu gibi.'),
('وَالسَّابِعُ: رُبَّ؛ لِلتَّقْلِيلِ، نَحْوُ: رُبَّ رَجُلٍ جَوَادٍ لَقِيتُهُ، وَرُبَّ رَجُلٍ أَبُوهُ عَالِمٌ لَقِيتُهُ، وَرُبَّ رَجُلٍ حَسَنٍ أَبُوهُ لَقِيتُهُ.','Yedincisi: rubbe. Taklîl (azlık) içindir: “Nice cömert adama rastladım”, “Babası âlim olan nice adama rastladım”, “Babası güzel nice adama rastladım.”'),
('وَالثَّامِنُ: عَلَى؛ وَهِيَ لِلِاسْتِعْلَاءِ، نَحْوُ: زَيْدٌ عَلَى السَّطْحِ، وَعَلَيْهِ دَيْنٌ.','Sekizincisi: alâ. İsti‘lâ (üstünlük) içindir: “Zeyd damın üstünde”, “Onun üzerinde borç var.”'),
('وَقَدْ يَكُونُ فِعْلًا، نَحْوُ قَوْلِهِ تَعَالَى: ﴿إِنَّ فِرْعَوْنَ عَلَا فِي الْأَرْضِ﴾.','Bazen fiil olur: “Firavun yeryüzünde büyüklendi.”'),
('وَالتَّاسِعُ: عَنْ؛ لِلْبُعْدِ وَالْمُجَاوَزَةِ، نَحْوُ: رَمَيْتُ السَّهْمَ عَنِ الْقَوْسِ.','Dokuzuncusu: an. Uzaklık ve geçip gitme içindir: “Oku yaydan attım.”'),
('وَالْعَاشِرُ: الْكَافُ؛ لِلتَّشْبِيهِ، نَحْوُ: زَيْدٌ كَالْأَسَدِ، وَالَّذِي كَزَيْدٍ أَخُوكَ.','Onuncusu: kâf. Teşbîh içindir: “Zeyd aslan gibidir”, “Zeyd gibi olan senin kardeşindir.”'),
('وَالْحَادِيَ عَشَرَ: مُذْ، وَالثَّانِيَ عَشَرَ: مُنْذُ؛ وَهُمَا لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ الْمَاضِي، نَحْوُ: مَا رَأَيْتُهُ مُذْ يَوْمِ الْجُمُعَةِ، وَمُنْذُ يَوْمِ السَّبْتِ.','On birincisi muz, on ikincisi munzü. Bunlar geçmiş zamanda başlangıç içindir: “Onu cuma gününden beri görmedim”, “cumartesi gününden beri.”'),
('وَالثَّالِثَ عَشَرَ: الْوَاوُ لِلْقَسَمِ، نَحْوُ: وَاللَّهِ لَأَفْعَلَنَّ كَذَا. وَالرَّابِعَ عَشَرَ: التَّاءُ كَذَلِكَ، نَحْوُ: تَاللَّهِ لَأَفْعَلَنَّ كَذَا.','On üçüncüsü: yemin vâvı: “Vallahi şunu mutlaka yapacağım.” On dördüncüsü: tâ da öyledir: “Tallahi şunu mutlaka yapacağım.”'),
('وَالْخَامِسَ عَشَرَ: حَاشَا؛ لِلتَّنْزِيهِ، نَحْوُ: سَاءَ الْقَوْمُ حَاشَا زَيْدٍ.','On beşincisi: hâşâ. Tenzîh içindir: “Kavim kötü davrandı, Zeyd hariç (onu tenzih ederim).”'),
('وَالسَّادِسَ عَشَرَ: عَدَا، وَالسَّابِعَ عَشَرَ: خَلَا؛ وَهُمَا لِلِاسْتِثْنَاءِ، نَحْوُ: جَاءَنِي الْقَوْمُ عَدَا زَيْدٍ، وَخَلَا زَيْدٍ.','On altıncısı adâ, on yedincisi halâ. Bunlar istisnâ içindir: “Kavim bana geldi, Zeyd hariç.”')])
b('النَّوْعُ الثَّانِي: الْحُرُوفُ الْمُشَبَّهَةُ بِالْفِعْلِ','2. çeşit: Fiile benzeyen harfler (ismi nasb, haberi ref‘)',[
('النَّوْعُ الثَّانِي: حُرُوفٌ تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ، وَهِيَ سِتَّةُ أَحْرُفٍ:','İkinci çeşit: İsmi nasb, haberi ref‘ eden harflerdir; altı harftir:'),
('إِنَّ وَأَنَّ لِلتَّحْقِيقِ، نَحْوُ: إِنَّ زَيْدًا قَائِمٌ، وَبَلَغَنِي أَنَّكَ عَالِمٌ.','İnne ve enne tahkîk (kesinlik) içindir: “Şüphesiz Zeyd ayaktadır”, “Senin âlim olduğun bana ulaştı.”'),
('وَكَأَنَّ لِلتَّشْبِيهِ، نَحْوُ: كَأَنَّ زَيْدًا الْأَسَدُ.','Keenne teşbîh içindir: “Zeyd sanki aslandır.”'),
('وَلَكِنَّ لِلِاسْتِدْرَاكِ، نَحْوُ: جَاءَنِي زَيْدٌ لَكِنَّ عَمْرًا لَمْ يَجِئْ.','Lâkinne istidrâk içindir: “Zeyd bana geldi, ama Amr gelmedi.”'),
('وَلَيْتَ لِلتَّمَنِّي، نَحْوُ: لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا فَأُخْبِرَهُ بِمَا فَعَلَ الْمَشِيبُ.','Leyte temennî içindir: “Keşke gençlik bir gün geri dönse de ona ihtiyarlığın yaptıklarını haber versem.”'),
('وَلَعَلَّ لِلتَّرَجِّي، نَحْوُ: لَعَلَّ زَيْدًا حَاضِرٌ.','Lealle tereccî (umma) içindir: “Umulur ki Zeyd hazırdır.”')])
b('النَّوْعُ الثَّالِثُ: مَا وَلَا الْمُشَبَّهَتَانِ بِلَيْسَ','3. çeşit: Leyse’ye benzeyen mâ ve lâ',[
('النَّوْعُ الثَّالِثُ: حَرْفَانِ تَرْفَعَانِ الِاسْمَ وَتَنْصِبَانِ الْخَبَرَ، وَهُمَا: مَا وَلَا الْمُشَبَّهَتَانِ بِلَيْسَ.','Üçüncü çeşit: İsmi ref‘, haberi nasbeden iki harftir: leyse’ye benzeyen mâ ve lâ.'),
('فَمَا لِنَفْيِ الْحَالِ، نَحْوُ: مَا زَيْدٌ مُنْطَلِقًا.','Mâ, şimdiki zamanı olumsuzlamak içindir: “Zeyd gitmekte değildir.”'),
('وَلَا لِنَفْيِ الِاسْتِقْبَالِ، نَحْوُ: لَا رَجُلٌ مُنْطَلِقًا.','Lâ, geleceği olumsuzlamak içindir: “Hiçbir adam gidecek değildir.”')])
b('النَّوْعُ الرَّابِعُ: حُرُوفٌ تَنْصِبُ الِاسْمَ الْمُفْرَدَ','4. çeşit: Yalnız tek ismi nasbeden harfler',[
('النَّوْعُ الرَّابِعُ: حُرُوفٌ تَنْصِبُ الِاسْمَ فَقَطْ، وَهِيَ سَبْعَةُ أَحْرُفٍ:','Dördüncü çeşit: Yalnız ismi nasbeden harflerdir; yedi harftir:'),
('الْوَاوُ بِمَعْنَى «مَعَ»، نَحْوُ: اسْتَوَى الْمَاءُ وَالْخَشَبَةَ.','“Me‘a” mânâsındaki vâv: “Su tahta ile beraber yükseldi.”'),
('وَإِلَّا لِلِاسْتِثْنَاءِ، نَحْوُ: جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا، وَمَا جَاءَنِي الْقَوْمُ إِلَّا حِمَارًا.','İllâ istisnâ içindir: “Kavim bana geldi, Zeyd hariç”, “Kavim bana gelmedi, bir eşek hariç.”'),
('وَيَا، وَأَيَا، وَهَيَا؛ لِنِدَاءِ الْبَعِيدِ، نَحْوُ: يَا عَبْدَ اللَّهِ، وَيَا خَيْرًا مِنْ زَيْدٍ، وَيَا رَجُلًا خُذْ بِيَدِي، وَأَيَا عَبْدَ اللَّهِ، وَهَيَا عَبْدَ اللَّهِ.','Yâ, eyâ ve heyâ uzaktakine nidâ içindir: “Ey Abdullah”, “Ey Zeyd’den hayırlı olan”, “Ey (herhangi bir) adam, elimden tut”, “Eyâ Abdallah”, “Heyâ Abdallah.”'),
('وَأَيْ وَالْهَمْزَةُ لِنِدَاءِ الْقَرِيبِ، نَحْوُ: أَيْ عَبْدَ اللَّهِ، وَأَعَبْدَ اللَّهِ؛ لَكِنَّ الْهَمْزَةَ لِنِدَاءِ الْأَقْرَبِ.','Ey ve hemze yakındakine nidâ içindir: “Ey Abdallah”, “E-Abdallah”; ancak hemze en yakındakine nidâ içindir.')])
b('النَّوْعُ الْخَامِسُ: حُرُوفٌ تَنْصِبُ الْفِعْلَ الْمُضَارِعَ','5. çeşit: Muzâriyi nasbeden harfler',[
('النَّوْعُ الْخَامِسُ: حُرُوفٌ تَنْصِبُ الْفِعْلَ الْمُضَارِعَ، وَهِيَ أَرْبَعَةُ أَحْرُفٍ:','Beşinci çeşit: Muzâri fiili nasbeden harflerdir; dört harftir:'),
('أَنْ لِلِاسْتِقْبَالِ، نَحْوُ: أُرِيدُ أَنْ أَخْرُجَ.','En, istikbâl içindir: “Çıkmak istiyorum.”'),
('وَلَنْ لِتَأْكِيدِ نَفْيِ الِاسْتِقْبَالِ، نَحْوُ قَوْلِهِ تَعَالَى: ﴿فَلَنْ أَبْرَحَ الْأَرْضَ حَتَّى يَأْذَنَ لِي أَبِي﴾.','Len, geleceğe dair olumsuzluğu pekiştirmek içindir: “Babam bana izin verinceye kadar bu yerden asla ayrılmayacağım.”'),
('وَكَيْ لِلتَّعْلِيلِ، نَحْوُ: جِئْتُكَ كَيْ تُعْطِيَنِي حَقِّي.','Key, ta‘lîl (sebep) içindir: “Hakkımı vermen için sana geldim.”'),
('وَإِذَنْ وَهِيَ جَوَابٌ لِقَوْلِ الْقَائِلِ وَجَزَاءٌ لِفِعْلِ الْفَاعِلِ، نَحْوُ قَوْلِكَ: إِذَنْ أُكْرِمَكَ؛ لِمَنْ قَالَ: أَنَا آتِيكَ.','İzen; söyleyenin sözüne cevap ve yapanın işine karşılıktır: “Sana geleceğim” diyene “O hâlde sana ikram ederim” demen gibi.')])
b('النَّوْعُ السَّادِسُ: حُرُوفٌ تَجْزِمُ الْفِعْلَ الْمُضَارِعَ','6. çeşit: Muzâriyi cezmeden harfler',[
('النَّوْعُ السَّادِسُ: حُرُوفٌ تَجْزِمُ الْفِعْلَ الْمُضَارِعَ، وَهِيَ خَمْسَةُ أَحْرُفٍ:','Altıncı çeşit: Muzâri fiili cezmeden harflerdir; beş harftir:'),
('إِنْ لِلشَّرْطِ وَالْجَزَاءِ، نَحْوُ: إِنْ تَأْتِنِي أُكْرِمْكَ.','İn, şart ve cezâ içindir: “Bana gelirsen sana ikram ederim.”'),
('وَلَمْ لِنَفْيِ الْمَاضِي بَعْدَ نَقْلِهِ مِنَ الْمُسْتَقْبَلِ إِلَى الْمَاضِي، نَحْوُ: لَمْ يَخْرُجْ زَيْدٌ.','Lem, muzâriyi gelecekten geçmişe naklettikten sonra geçmişi olumsuzlamak içindir: “Zeyd çıkmadı.”'),
('وَلَمَّا لِنَفْيِ الْمَاضِي أَيْضًا، وَفِيهِ تَوَقُّعٌ وَانْتِظَارٌ، نَحْوُ: لَمَّا يَخْرُجِ الْأَمِيرُ.','Lemmâ da geçmişi olumsuzlamak içindir; ancak onda beklenti vardır: “Emîr henüz çıkmadı (ama çıkması bekleniyor).”'),
('وَلَا لِلنَّهْيِ، نَحْوُ: لَا تَفْعَلْ.','Lâ, nehiy içindir: “Yapma.”'),
('وَاللَّامُ لِلْأَمْرِ، نَحْوُ: لِيَفْعَلْ زَيْدٌ.','Lâm, emir içindir: “Zeyd yapsın.”')])
b('النَّوْعُ السَّابِعُ: أَسْمَاءٌ تَجْزِمُ الْأَفْعَالَ','7. çeşit: Fiilleri cezmeden isimler (şart isimleri)',[
('النَّوْعُ السَّابِعُ: أَسْمَاءٌ تَجْزِمُ الْفِعْلَ الْمُضَارِعَ عَلَى مَعْنَى «إِنْ»، وَهِيَ تِسْعَةُ أَسْمَاءٍ:','Yedinci çeşit: “İn” mânâsıyla muzâri fiili cezmeden isimlerdir; dokuz isimdir:'),
('مَنْ، نَحْوُ: مَنْ تَضْرِبْ أَضْرِبْ.','Men: “Kime vurursan ona vururum.”'),
('وَأَيٌّ، نَحْوُ: أَيَّهُمْ تَضْرِبْ أَضْرِبْ.','Eyyün: “Onlardan hangisine vurursan ona vururum.”'),
('وَمَا، نَحْوُ: مَا تَصْنَعْ أَصْنَعْ.','Mâ: “Ne yaparsan onu yaparım.”'),
('وَمَتَى، نَحْوُ: مَتَى تُكْرِمْنِي أُكْرِمْكَ.','Metâ: “Bana ne zaman ikram edersen sana ikram ederim.”'),
('وَمَهْمَا، نَحْوُ: مَهْمَا تَفْعَلْ أَفْعَلْ.','Mehmâ: “Her ne yaparsan yaparım.”'),
('وَأَيْنَ، نَحْوُ: أَيْنَ تَكُنْ أَكُنْ.','Eyne: “Nerede olursan olurum.”'),
('وَحَيْثُمَا، نَحْوُ: حَيْثُمَا تَجْلِسْ أَجْلِسْ.','Haysümâ: “Nereye oturursan otururum.”'),
('وَإِذْمَا، نَحْوُ: إِذْمَا تَفْعَلْ أَفْعَلْ.','İzmâ: “Ne zaman yaparsan yaparım.”'),
('وَأَنَّى، نَحْوُ: أَنَّى تَفْعَلْ أَفْعَلْ.','Ennâ: “Nerede/nasıl yaparsan yaparım.”')])
b('النَّوْعُ الثَّامِنُ: أَسْمَاءٌ تَنْصِبُ عَلَى التَّمْيِيزِ','8. çeşit: Temyîz olarak nasbeden isimler',[
('النَّوْعُ الثَّامِنُ: أَسْمَاءٌ تَنْصِبُ أَسْمَاءً نَكِرَاتٍ عَلَى التَّمْيِيزِ، وَهِيَ أَرْبَعَةُ أَسْمَاءٍ:','Sekizinci çeşit: Nekre isimleri temyîz olarak nasbeden isimlerdir; dört isimdir:'),
('الْأَوَّلُ: عَشَرَ إِذَا رُكِّبَتْ مَعَ أَحَدٍ إِلَى تِسْعَةٍ، نَحْوُ: عِنْدِي أَحَدَ عَشَرَ رَجُلًا.','Birincisi: Bir’den dokuz’a kadar sayılarla birleşik olduğunda “aşera”: “Yanımda on bir adam var.”'),
('وَالثَّانِي: كَمْ لِلِاسْتِفْهَامِ، نَحْوُ: كَمْ رَجُلًا عِنْدَكَ؟','İkincisi: soru için kem: “Yanında kaç adam var?”'),
('وَالثَّالِثُ: كَأَيِّنْ، نَحْوُ: كَأَيِّنْ رَجُلًا عِنْدِي.','Üçüncüsü: keeyyin: “Yanımda nice adam var.”'),
('وَالرَّابِعُ: كَذَا، وَهِيَ كِنَايَةٌ عَنِ الْعَدَدِ، نَحْوُ: عِنْدِي كَذَا دِرْهَمًا.','Dördüncüsü: kezâ; sayıdan kinayedir: “Yanımda şu kadar dirhem var.”')])
b('النَّوْعُ التَّاسِعُ: أَسْمَاءُ الْأَفْعَالِ','9. çeşit: Fiil isimleri',[
('النَّوْعُ التَّاسِعُ: كَلِمَاتٌ تُسَمَّى أَسْمَاءَ الْأَفْعَالِ، بَعْضُهَا يَرْفَعُ وَبَعْضُهَا يَنْصِبُ، وَهِيَ تِسْعُ كَلِمَاتٍ.','Dokuzuncu çeşit: “Esmâ-i ef‘âl” (fiil isimleri) denilen kelimelerdir; bir kısmı ref‘, bir kısmı nasbeder; dokuz kelimedir.'),
('النَّاصِبَةُ مِنْهَا سِتُّ كَلِمَاتٍ: رُوَيْدَ، نَحْوُ: رُوَيْدَ زَيْدًا، أَيْ: أَمْهِلْهُ.','Nasbedenler altı kelimedir. Ruveyde: “Ruveyde Zeyden” yani ona mühlet ver.'),
('وَبَلْهَ، نَحْوُ: بَلْهَ زَيْدًا، أَيْ: دَعْهُ.','Belhe: “Belhe Zeyden” yani onu bırak.'),
('وَدُونَكَ، نَحْوُ: دُونَكَ زَيْدًا، أَيْ: خُذْهُ.','Dûneke: “Dûneke Zeyden” yani onu al.'),
('وَعَلَيْكَ، نَحْوُ: عَلَيْكَ زَيْدًا، أَيْ: الْزَمْهُ.','Aleyke: “Aleyke Zeyden” yani ona sarıl, ondan ayrılma.'),
('وَهَا، نَحْوُ: هَا زَيْدًا، أَيْ: خُذْهُ.','Hâ: “Hâ Zeyden” yani onu al.'),
('وَحَيَّهَلَ، نَحْوُ: حَيَّهَلَ الثَّرِيدَ، أَيْ: ائْتِهِ.','Hayyehele: “Hayyehele’s-serîde” yani tirite gel.'),
('وَالرَّافِعَةُ مِنْهَا ثَلَاثُ كَلِمَاتٍ: هَيْهَاتَ، نَحْوُ: هَيْهَاتَ زَيْدٌ، أَيْ: بَعُدَ.','Ref‘ edenler üç kelimedir. Heyhâte: “Heyhâte Zeydün” yani uzaklaştı.'),
('وَسَرْعَانَ، نَحْوُ: سَرْعَانَ ذَا إِهَالَةً، أَيْ: سَرُعَ.','Ser‘âne: “Ser‘âne zâ ihâleten” yani çabuk oldu.'),
('وَشَتَّانَ، نَحْوُ: شَتَّانَ زَيْدٌ وَعَمْرٌو، أَيِ: افْتَرَقَا.','Şettâne: “Şettâne Zeydün ve Amrun” yani ikisi birbirinden ayrıldı (arada çok fark var).')])
b('النَّوْعُ الْعَاشِرُ: الْأَفْعَالُ النَّاقِصَةُ','10. çeşit: Nâkıs fiiller',[
('النَّوْعُ الْعَاشِرُ: الْأَفْعَالُ النَّاقِصَةُ تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ، وَهِيَ ثَلَاثَةَ عَشَرَ فِعْلًا:','Onuncu çeşit: Nâkıs fiiller ismi ref‘, haberi nasbeder; on üç fiildir:'),
('كَانَ، نَحْوُ: كَانَ زَيْدٌ قَائِمًا. وَتَكُونُ تَامَّةً، نَحْوُ: كَانَ زَيْدٌ، أَيْ: وُجِدَ زَيْدٌ. وَزَائِدَةً، نَحْوُ: إِنَّ مِنْ أَفْضَلِهِمْ كَانَ زَيْدًا. وَمُضْمَرًا فِيهَا ضَمِيرُ الشَّأْنِ، نَحْوُ: كَانَ زَيْدٌ قَائِمٌ.','Kâne: “Zeyd ayakta idi.” Tâmme olur: “Kâne Zeydün” yani Zeyd var oldu. Zâide olur: “Onların en faziletlisi Zeyd’dir.” İçinde zamîr-i şe’n gizli olarak da gelir: “Kâne Zeydün kâimun.”'),
('وَصَارَ لِلِانْتِقَالِ، نَحْوُ: صَارَ زَيْدٌ غَنِيًّا. وَتَكُونُ تَامَّةً، نَحْوُ: صَارَ زَيْدٌ إِلَى عَمْرٍو، أَيْ: ذَهَبَ إِلَيْهِ.','Sâra intikâl (bir hâlden diğerine geçme) içindir: “Zeyd zengin oldu.” Tâmme olur: “Zeyd Amr’a gitti.”'),
('وَأَصْبَحَ، نَحْوُ: أَصْبَحَ زَيْدٌ فَقِيرًا. وَتَكُونُ تَامَّةً، نَحْوُ: أَصْبَحَ زَيْدٌ، أَيْ: دَخَلَ فِي وَقْتِ الصَّبَاحِ. وَبِمَعْنَى صَارَ، نَحْوُ: أَصْبَحَ زَيْدٌ غَنِيًّا.','Asbaha: “Zeyd sabahleyin fakirdi.” Tâmme olur: “Asbaha Zeydün” yani sabah vaktine girdi. Sâra mânâsına da gelir: “Zeyd zengin oldu.”'),
('وَأَمْسَى مِثْلُ أَصْبَحَ أَيْضًا، نَحْوُ: أَمْسَى زَيْدٌ فَقِيرًا.','Emsâ da asbaha gibidir: “Zeyd akşamleyin fakirdi.”'),
('وَأَضْحَى مِثْلُ أَصْبَحَ، نَحْوُ: أَضْحَى زَيْدٌ آكِلًا.','Adhâ da asbaha gibidir: “Zeyd kuşluk vakti yiyordu.”'),
('وَظَلَّ مِثْلُ أَصْبَحَ أَيْضًا، نَحْوُ: ظَلَّ زَيْدٌ قَائِمًا. وَتَكُونُ بِمَعْنَى صَارَ، نَحْوُ: ظَلَّ زَيْدٌ فَقِيرًا.','Zalle da asbaha gibidir: “Zeyd gün boyu ayakta kaldı.” Sâra mânâsına da gelir: “Zeyd fakir oldu.”'),
('وَبَاتَ مِثْلُ أَصْبَحَ أَيْضًا، نَحْوُ: بَاتَ زَيْدٌ قَائِمًا. وَتَكُونُ بِمَعْنَى صَارَ، نَحْوُ: بَاتَ زَيْدٌ فَقِيرًا.','Bâte da asbaha gibidir: “Zeyd geceyi ayakta geçirdi.” Sâra mânâsına da gelir: “Zeyd fakir oldu.”'),
('وَمَا زَالَ، نَحْوُ: مَا زَالَ زَيْدٌ كَرِيمًا.','Mâ zâle: “Zeyd hâlâ cömerttir.”'),
('وَمَا بَرِحَ، وَمَا فَتِئَ، وَمَا انْفَكَّ؛ بِمَعْنَى مَا زَالَ.','Mâ berihe, mâ fetie ve mâ’nfekke de mâ zâle mânâsındadır (hâlâ … devam etti).'),
('وَمَا دَامَ، نَحْوُ: اجْلِسْ مَا دَامَ زَيْدٌ جَالِسًا.','Mâ dâme: “Zeyd oturduğu sürece otur.”'),
('وَلَيْسَ لِنَفْيِ الْحَالِ، نَحْوُ: لَيْسَ زَيْدٌ قَائِمًا.','Leyse, şimdiki zamanı olumsuzlamak içindir: “Zeyd ayakta değildir.”')])
b('النَّوْعُ الْحَادِيَ عَشَرَ: أَفْعَالُ الْمُقَارَبَةِ','11. çeşit: Mukârebe fiilleri',[
('النَّوْعُ الْحَادِيَ عَشَرَ: أَفْعَالٌ تُسَمَّى أَفْعَالَ الْمُقَارَبَةِ، تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ، وَهِيَ أَرْبَعَةُ أَفْعَالٍ:','On birinci çeşit: Ef‘âl-i mukârebe denilen fiillerdir; ismi ref‘, haberi nasbeder; dört fiildir:'),
('عَسَى، نَحْوُ: عَسَى زَيْدٌ أَنْ يَخْرُجَ. وَتَكُونُ تَامَّةً، نَحْوُ: عَسَى أَنْ يَخْرُجَ زَيْدٌ.','Asâ: “Umulur ki Zeyd çıkar.” Tâmme de olur: “Zeyd’in çıkması umulur.”'),
('وَكَادَ، نَحْوُ: كَادَ زَيْدٌ يَخْرُجُ.','Kâde: “Zeyd neredeyse çıkacaktı.”'),
('وَكَرَبَ، نَحْوُ: كَرَبَ زَيْدٌ يَخْرُجُ.','Kerebe: “Zeyd çıkmaya yaklaştı.”'),
('وَأَوْشَكَ، نَحْوُ: أَوْشَكَ زَيْدٌ أَنْ يَخْرُجَ، وَأَوْشَكَ أَنْ يَخْرُجَ زَيْدٌ، وَأَوْشَكَ زَيْدٌ يَخْرُجُ.','Evşeke: “Zeyd çıkmak üzere”, “Zeyd’in çıkması yakın”, “Zeyd çıkmak üzere.”')])
b('النَّوْعُ الثَّانِيَ عَشَرَ: أَفْعَالُ الْمَدْحِ وَالذَّمِّ','12. çeşit: Övme ve yerme fiilleri',[
('النَّوْعُ الثَّانِيَ عَشَرَ: أَفْعَالُ الْمَدْحِ وَالذَّمِّ تَرْفَعُ الِاسْمَ الْجِنْسَ الْمُعَرَّفَ بِاللَّامِ، وَهِيَ أَرْبَعَةُ أَفْعَالٍ:','On ikinci çeşit: Övme ve yerme fiilleri, lâm ile ma‘rife yapılmış cins ismini ref‘ eder; dört fiildir:'),
('نِعْمَ، نَحْوُ: نِعْمَ الرَّجُلُ زَيْدٌ.','Ni‘me: “Zeyd ne güzel adamdır.”'),
('وَبِئْسَ، نَحْوُ: بِئْسَ الرَّجُلُ زَيْدٌ.','Bi’se: “Zeyd ne kötü adamdır.”'),
('وَحَبَّذَا، نَحْوُ: حَبَّذَا الرَّجُلُ زَيْدٌ.','Habbezâ: “Zeyd ne hoş adamdır.”'),
('وَسَاءَ، نَحْوُ: سَاءَ الرَّجُلُ زَيْدٌ.','Sâe: “Zeyd ne kötü adamdır.”')])
b('النَّوْعُ الثَّالِثَ عَشَرَ: أَفْعَالُ الشَّكِّ وَالْيَقِينِ','13. çeşit: Şek ve yakîn fiilleri (kalbî fiiller)',[
('النَّوْعُ الثَّالِثَ عَشَرَ: أَفْعَالُ الشَّكِّ وَالْيَقِينِ، تَدْخُلُ عَلَى اسْمَيْنِ ثَانِيهِمَا عِبَارَةٌ عَنِ الْأَوَّلِ وَتَنْصِبُهُمَا جَمِيعًا، وَهِيَ سَبْعَةُ أَفْعَالٍ:','On üçüncü çeşit: Şek ve yakîn fiilleri; ikincisi birinciyi anlatan iki isme girer ve ikisini birlikte nasbeder; yedi fiildir:'),
('ظَنَنْتُ، نَحْوُ: ظَنَنْتُ زَيْدًا كَرِيمًا. وَإِذَا كَانَ بِمَعْنَى اتَّهَمْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ، نَحْوُ: ظَنَنْتُ زَيْدًا، أَيِ: اتَّهَمْتُهُ.','Zanentü: “Zeyd’i cömert sandım.” “İtham ettim” mânâsına olursa ikinci mef‘ûlü gerektirmez: “Zeyd’den şüphelendim.”'),
('وَحَسِبْتُ، نَحْوُ: حَسِبْتُ أَخَاكَ كَرِيمًا.','Hasibtü: “Kardeşini cömert sandım.”'),
('وَخِلْتُ، نَحْوُ: خِلْتُ زَيْدًا عَاقِلًا.','Hiltü: “Zeyd’i akıllı sandım.”'),
('وَعَلِمْتُ، نَحْوُ: عَلِمْتُ زَيْدًا فَاضِلًا. وَإِذَا كَانَ بِمَعْنَى عَرَفْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ، نَحْوُ: عَلِمْتُ زَيْدًا، أَيْ: عَرَفْتُهُ.','Alimtü: “Zeyd’in faziletli olduğunu bildim.” “Tanıdım” mânâsına olursa ikinci mef‘ûlü gerektirmez: “Zeyd’i tanıdım.”'),
('وَرَأَيْتُ، نَحْوُ: رَأَيْتُ زَيْدًا قَائِمًا. وَإِذَا كَانَ بِمَعْنَى أَبْصَرْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ، نَحْوُ: رَأَيْتُ زَيْدًا، أَيْ: أَبْصَرْتُهُ.','Raeytü: “Zeyd’in ayakta olduğunu gördüm (bildim).” “Gözle gördüm” mânâsına olursa ikinci mef‘ûlü gerektirmez: “Zeyd’i gördüm.”'),
('وَوَجَدْتُ، نَحْوُ: وَجَدْتُ زَيْدًا جَوَادًا. وَإِذَا كَانَ بِمَعْنَى أَصَبْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ، نَحْوُ: وَجَدْتُ الضَّالَّةَ، أَيْ: أَصَبْتُهَا.','Vecedtü: “Zeyd’i cömert buldum.” “Ele geçirdim” mânâsına olursa ikinci mef‘ûlü gerektirmez: “Kayıp hayvanı buldum.”'),
('وَزَعَمْتُ، نَحْوُ: زَعَمْتُ زَيْدًا فَاضِلًا. وَإِذَا كَانَ بِمَعْنَى قُلْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ، نَحْوُ قَوْلِهِ تَعَالَى: ﴿زَعَمَ الَّذِينَ كَفَرُوا أَنْ لَنْ يُبْعَثُوا﴾.','Zeamtü: “Zeyd’i faziletli zannettim.” “Dedim” mânâsına olursa ikinci mef‘ûlü gerektirmez: “Kâfirler asla diriltilmeyeceklerini iddia ettiler.”')])
b('الْعَوَامِلُ الْقِيَاسِيَّةُ','Kıyâsî âmiller (7)',[
('وَالْقِيَاسِيَّةُ مِنْهَا سَبْعَةُ عَوَامِلَ:','Kıyâsî âmiller yedidir:'),
('الْفِعْلُ عَلَى الْإِطْلَاقِ، نَحْوُ: ضَرَبَ زَيْدٌ عَمْرًا.','1. Mutlak olarak fiil: “Zeyd Amr’ı dövdü.”'),
('وَالْمَصْدَرُ، نَحْوُ: أَعْجَبَنِي ضَرْبُ زَيْدٍ عَمْرًا.','2. Masdar: “Zeyd’in Amr’ı dövmesi hoşuma gitti.”'),
('وَاسْمُ الْفَاعِلِ، نَحْوُ: زَيْدٌ ضَارِبٌ غُلَامُهُ عَمْرًا.','3. İsm-i fâil: “Zeyd’in kölesi Amr’ı dövmektedir.”'),
('وَاسْمُ الْمَفْعُولِ، نَحْوُ: زَيْدٌ مُعْطًى غُلَامُهُ دِرْهَمًا.','4. İsm-i mef‘ûl: “Zeyd’in kölesine bir dirhem verilmektedir.”'),
('وَالصِّفَةُ الْمُشَبَّهَةُ، نَحْوُ: جَاءَنِي رَجُلٌ حَسَنٌ وَجْهُهُ.','5. Sıfat-ı müşebbehe: “Bana yüzü güzel bir adam geldi.”'),
('وَكُلُّ اسْمٍ أُضِيفَ إِلَى اسْمٍ آخَرَ، نَحْوُ: غُلَامُ زَيْدٍ، وَخَاتَمُ فِضَّةٍ.','6. Başka bir isme muzâf olan her isim: “Zeyd’in kölesi”, “gümüş yüzük.”'),
('وَكُلُّ اسْمٍ اسْتَغْنَى عَنِ الْإِضَافَةِ، نَحْوُ: عِنْدِي رَاقُودٌ خَلًّا، وَمَنَوَانِ سَمْنًا، وَعِشْرُونَ دِرْهَمًا، وَمِلْؤُهُ عَسَلًا.','7. İzâfetten müstağni olan (tamamlanmış) her isim: “Yanımda bir küp sirke, iki batman yağ, yirmi dirhem ve onun dolusu bal var.”')])
b('الْعَوَامِلُ الْمَعْنَوِيَّةُ','Ma‘nevî âmiller (2)',[
('وَالْمَعْنَوِيَّةُ مِنْهَا عَدَدَانِ:','Ma‘nevî âmiller ikidir:'),
('الْعَامِلُ فِي الْمُبْتَدَإِ وَالْخَبَرِ، وَهُوَ كَوْنُهُ مُبْتَدَأً وَخَبَرًا، نَحْوُ: زَيْدٌ مُنْطَلِقٌ.','1. Mübtedâ ve haberdeki âmil: onların mübtedâ ve haber olmalarıdır (ibtidâ): “Zeyd gitmektedir.”'),
('وَالْعَامِلُ فِي الْفِعْلِ الْمُضَارِعِ، وَهُوَ وُقُوعُهُ مَوْقِعَ الِاسْمِ، نَحْوُ: زَيْدٌ يَضْرِبُ؛ وَيَضْرِبُ زَيْدٌ فِي مَوْقِعِ: زَيْدٌ ضَارِبٌ.','2. Muzâri fiildeki âmil: onun ismin yerinde bulunmasıdır: “Zeyd döver” — buradaki “yadribu”, “Zeyd dövücüdür” sözündeki isim yerindedir.')])
Q=[
 (0,'Cürcânî’ye göre âmillerin toplam sayısı kaçtır?',['Yüz','Altmış','Doksan bir','On üç'],'مِائَةُ عَامِلٍ: 91 semâî + 7 kıyâsî + 2 ma‘nevî.'),
 (0,'Semâî âmiller kaç çeşide ayrılır?',['On üç','Yedi','İki','Dokuz'],'تَتَنَوَّعُ عَلَى ثَلَاثَةَ عَشَرَ نَوْعًا.'),
 (1,'كَتَبْتُ بِالْقَلَمِ cümlesinde bâ hangi mânâdadır?',['İstiâne (vasıta)','İlsâk','Musâhabe','Kasem'],'وَلِلِاسْتِعَانَةِ، نَحْوُ: كَتَبْتُ بِالْقَلَمِ.'),
 (1,'أَخَذْتُ مِنَ الْمَالِ cümlesinde min hangi mânâdadır?',['Teb‘îz','İbtidâ-i gâye','Tebyîn','Zâid'],'وَلِلتَّبْعِيضِ.'),
 (1,'رُبَّ hangi mânâ içindir?',['Taklîl','Teşbîh','İsti‘lâ','Tenzîh'],'رُبَّ لِلتَّقْلِيلِ.'),
 (1,'مُذْ ve مُنْذُ ne bildirir?',['Geçmiş zamanda başlangıç','Mekânda bitiş','Teşbîh','Yemin'],'لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ الْمَاضِي.'),
 (2,'لَكِنَّ hangi mânâ içindir?',['İstidrâk','Teşbîh','Temennî','Tereccî'],'وَلَكِنَّ لِلِاسْتِدْرَاكِ.'),
 (3,'Leyse’ye benzeyen mâ neyi olumsuzlar?',['Şimdiki zamanı (hâl)','Geleceği','Geçmişi','Emri'],'فَمَا لِنَفْيِ الْحَالِ.'),
 (4,'اسْتَوَى الْمَاءُ وَالْخَشَبَةَ cümlesinde vâv ne mânâdadır?',['“Me‘a” (ile beraber)','Atf','Kasem','Hâl'],'الْوَاوُ بِمَعْنَى «مَعَ».'),
 (4,'Hemze ile nidâ kime yapılır?',['En yakındakine','Uzaktakine','Ortadakine','Ölüye'],'لَكِنَّ الْهَمْزَةَ لِنِدَاءِ الْأَقْرَبِ.'),
 (5,'لَنْ hangi mânâyı ifade eder?',['Gelecekteki olumsuzluğun te’kîdi','Geçmişin olumsuzlanması','Nehiy','Şart'],'وَلَنْ لِتَأْكِيدِ نَفْيِ الِاسْتِقْبَالِ.'),
 (6,'لَمَّا ile لَمْ arasındaki fark nedir?',['لَمَّا’da beklenti (tevakku‘) vardır','لَمَّا geleceği olumsuzlar','لَمْ nasbeder','Fark yoktur'],'وَفِيهِ تَوَقُّعٌ وَانْتِظَارٌ.'),
 (7,'Fiilleri cezmeden isimler kaç tanedir?',['Dokuz','Beş','Dört','On yedi'],'وَهِيَ تِسْعَةُ أَسْمَاءٍ.'),
 (8,'كَمْ رَجُلًا عِنْدَكَ cümlesinde رَجُلًا nedir?',['Temyîz','Hâl','Mef‘ûlün bih','Bedel'],'أَسْمَاءٌ تَنْصِبُ … عَلَى التَّمْيِيزِ.'),
 (9,'هَيْهَاتَ hangi fiil mânâsındadır?',['بَعُدَ (uzaklaştı)','خُذْ (al)','دَعْ (bırak)','اِلْزَمْ (sarıl)'],'هَيْهَاتَ زَيْدٌ، أَيْ: بَعُدَ.'),
 (9,'Aşağıdakilerden hangisi nasbeden fiil isimlerindendir?',['رُوَيْدَ','شَتَّانَ','سَرْعَانَ','هَيْهَاتَ'],'Nasbedenler: رويد، بله، دونك، عليك، ها، حيهل.'),
 (10,'كَانَ زَيْدٌ “Zeyd var oldu” mânâsında kâne nasıl kullanılmıştır?',['Tâmme','Nâkısa','Zâide','Şe’n zamirli'],'وَتَكُونُ تَامَّةً، نَحْوُ: كَانَ زَيْدٌ، أَيْ: وُجِدَ زَيْدٌ.'),
 (10,'Nâkıs fiiller kaç tanedir?',['On üç','Dört','Yedi','Altı'],'وَهِيَ ثَلَاثَةَ عَشَرَ فِعْلًا.'),
 (11,'Aşağıdakilerden hangisi mukârebe fiillerindendir?',['كَرَبَ','ظَلَّ','حَبَّذَا','خِلْتُ'],'عَسَى، كَادَ، كَرَبَ، أَوْشَكَ.'),
 (12,'نِعْمَ fiili neyi ref‘ eder?',['Lâm ile ma‘rife olmuş cins ismini','Herhangi bir nekreyi','Muzâri fiili','Zamir dışında hiçbir şeyi'],'تَرْفَعُ الِاسْمَ الْجِنْسَ الْمُعَرَّفَ بِاللَّامِ.'),
 (13,'رَأَيْتُ “gözle gördüm” mânâsında ise ne olur?',['İkinci mef‘ûlü gerektirmez','Üç mef‘ûl alır','Hiç mef‘ûl almaz','Haberi ref‘ eder'],'وَإِذَا كَانَ بِمَعْنَى أَبْصَرْتُ لَمْ يَقْتَضِ الْمَفْعُولَ الثَّانِيَ.'),
 (14,'Kıyâsî âmiller kaç tanedir?',['Yedi','İki','On üç','Dokuz'],'وَالْقِيَاسِيَّةُ مِنْهَا سَبْعَةُ عَوَامِلَ.'),
 (14,'غُلَامُ زَيْدٍ terkibinde âmil hangisidir?',['Muzâf olan isim','Ma‘nevî âmil','Gizli bir cer harfi','Fiil'],'وَكُلُّ اسْمٍ أُضِيفَ إِلَى اسْمٍ آخَرَ.'),
 (15,'Muzâri fiili ref‘ eden ma‘nevî âmil nedir?',['İsmin yerinde bulunması','Başındaki muzâri harfi','Mübtedâ olması','Gizli إنّ'],'وَهُوَ وُقُوعُهُ مَوْقِعَ الِاسْمِ.'),
]
d={'id':'avamil','baslik':'العوامل المائة — عبد القاهر الجرجاني','kaynak':'Avâmil-i Cürcânî (Mie Âmil); harekeli nüsha','tr_kaynak':'Türkçe tercüme: el-Mihrâb','bolumler':B,'sorular':[{'b':b_,'s':s,'k':k,'d':0,'a':a} for b_,s,k,a in Q]}
json.dump(d,open('data/kitap/avamil.json','w'),ensure_ascii=False,indent=0)
print(len(B),sum(len(x['p']) for x in B),len(Q))
