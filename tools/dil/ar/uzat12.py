# Arapça Hikâye Programı 1. haftası (1–6. günler): her güne yeni okuma cümleleri ve diyalog satırları ekler (18+ cümle, 12 replik).
# python3 tools/dil/ar/uzat12.py   (tekrar çalıştırılırsa aynı cümleleri ikinci kez eklemez)
import json, os, subprocess, sys
R = lambda ar, tr: [ar, tr]
E = {}

E[0] = ([
 R('فِي الْغُرْفَةِ فَتَحَ يُوسُفُ النَّافِذَةَ، فَدَخَلَ هَوَاءٌ بَارِدٌ يَحْمِلُ رَائِحَةَ الْيَاسَمِينِ.', 'Odada Yusuf pencereyi açtı; yasemin kokusu taşıyan serin bir hava içeri girdi.'),
 R('كَانَتِ الْمَدِينَةُ تَحْتَهُ كَبَحْرٍ مِنَ الْأَضْوَاءِ الصَّغِيرَةِ الَّتِي لَا تَنْتَهِي.', 'Şehir aşağıda, bitmek bilmeyen küçük ışıklardan bir deniz gibiydi.'),
 R('اتَّصَلَ بِأُمِّهِ وَقَالَ لَهَا: «وَصَلْتُ يَا أُمِّي، وَكُلُّ شَيْءٍ عَلَى مَا يُرَامُ.»', 'Annesini aradı ve ona dedi: “Vardım anneciğim, her şey yolunda.”'),
 R('سَأَلَتْهُ أُمُّهُ: «هَلْ أَكَلْتَ شَيْئًا؟» فَتَذَكَّرَ أَنَّهُ لَمْ يَأْكُلْ مُنْذُ الصَّبَاحِ.', 'Annesi ona “Bir şey yedin mi?” diye sordu; o da sabahtan beri yemek yemediğini hatırladı.'),
 R('نَزَلَ إِلَى مَطْعَمٍ صَغِيرٍ بِجَانِبِ الْفُنْدُقِ، وَطَلَبَ صَحْنًا مِنَ الْحُمُّصِ وَرَغِيفًا سَاخِنًا.', 'Otelin yanındaki küçük bir lokantaya indi ve bir tabak humus ile sıcak bir pide istedi.'),
 R('كَانَ صَاحِبُ الْمَطْعَمِ شَابًّا مَرِحًا، فَلَمَّا عَرَفَ أَنَّهُ تُرْكِيٌّ رَحَّبَ بِهِ تَرْحِيبًا حَارًّا.', 'Lokantanın sahibi neşeli bir gençti; onun Türk olduğunu öğrenince onu sıcacık karşıladı.'),
 R('قَالَ الشَّابُّ: «أَصْبَحَتِ الْمُسَلْسَلَاتُ التُّرْكِيَّةُ مَشْهُورَةً هُنَا، فَلَسْتَ غَرِيبًا عَنَّا!»', 'Genç dedi: “Türk dizileri burada meşhur oldu; yani bize hiç yabancı değilsin!”'),
 R('وَقَبْلَ أَنْ يَنَامَ كَتَبَ فِي دَفْتَرِهِ أَوَّلَ جُمْلَةٍ فِي رِحْلَتِهِ: «مَا زِلْتُ فِي الْبِدَايَةِ، لَكِنَّ الطَّرِيقَ جَمِيلٌ.»', 'Uyumadan önce defterine yolculuğunun ilk cümlesini yazdı: “Henüz başlangıçtayım, ama yol güzel.”'),
 R('ثُمَّ أَطْفَأَ النُّورَ، وَظَلَّ يَسْمَعُ أَصْوَاتَ الْمَدِينَةِ حَتَّى غَلَبَهُ النَّوْمُ.', 'Sonra ışığı söndürdü ve uyku onu yenene kadar şehrin seslerini dinleyip durdu.')],
 [['يُوسُفُ', 'وَمَاذَا كُنْتَ تَفْعَلُ فِي الْمَغْرِبِ؟', 'Peki Fas’ta ne yapıyordun?'],
  ['السَّائِقُ', 'كُنْتُ أَعْمَلُ هُنَاكَ مُهَنْدِسًا خَمْسَ سَنَوَاتٍ، ثُمَّ رَجَعْتُ إِلَى بَلَدِي.', 'Orada beş yıl mühendis olarak çalıştım, sonra memleketime döndüm.'],
  ['يُوسُفُ', 'مُهَنْدِسٌ؟ فَلِمَاذَا صِرْتَ سَائِقًا؟', 'Mühendis mi? Peki neden şoför oldun?'],
  ['السَّائِقُ', 'لِأَنِّي أُحِبُّ الْكَلَامَ مَعَ النَّاسِ، وَكَانَ الْمَكْتَبُ صَامِتًا جِدًّا!', 'Çünkü insanlarla konuşmayı severim; ofis de çok sessizdi!'],
  ['يُوسُفُ', 'إِذَنْ سَأَتَعَلَّمُ مِنْكَ اللَّهْجَةَ فِي الطَّرِيقِ!', 'O zaman yolda lehçeyi senden öğreneceğim!']])

E[1] = ([
 R('فِي الْمَسَاءِ طَرَقَ يُوسُفُ بَابَ جَارَتِهِ، وَفِي يَدِهِ عُلْبَةٌ مِنَ الْحَلْقُومِ التُّرْكِيِّ.', 'Akşam Yusuf komşusunun kapısını çaldı; elinde bir kutu Türk lokumu vardı.'),
 R('فَتَحَ لَهُ الْبَابَ أَبُو أَحْمَدَ، وَهُوَ رَجُلٌ طَوِيلٌ ذُو شَارِبٍ أَبْيَضَ، يَعْمَلُ مُعَلِّمًا لِلتَّارِيخِ.', 'Kapıyı ona Ebû Ahmed açtı; beyaz bıyıklı, uzun boylu bir adamdı ve tarih öğretmeni olarak çalışıyordu.'),
 R('كَانَ الْبَيْتُ مُمْتَلِئًا بِرَائِحَةِ اللَّحْمِ وَاللَّبَنِ وَالسَّمْنِ.', 'Ev et, yoğurt ve sade yağ kokusuyla doluydu.'),
 R('وَضَعَتْ أُمُّ أَحْمَدَ عَلَى الْمَائِدَةِ صَحْنًا كَبِيرًا مِنَ الْمَنْسَفِ، وَقَالَتْ: «كُلْ بِيَدِكَ الْيُمْنَى كَمَا يَأْكُلُ أَهْلُ الْبَادِيَةِ.»', 'Ümmü Ahmed sofraya büyük bir tabak mansaf koydu ve dedi: “Bedeviler gibi sağ elinle ye.”'),
 R('حَاوَلَ يُوسُفُ أَنْ يَصْنَعَ كُرَةً مِنَ الْأَرُزِّ وَاللَّحْمِ، لَكِنَّ الْأَرُزَّ سَقَطَ عَلَى قَمِيصِهِ.', 'Yusuf pirinç ve etten bir top yapmaya çalıştı, ama pirinç gömleğine döküldü.'),
 R('ضَحِكَ الْجَمِيعُ، وَقَالَ أَبُو أَحْمَدَ: «لَا بَأْسَ، إِنَّ الْمَنْسَفَ يَحْتَاجُ إِلَى تَدْرِيبٍ طَوِيلٍ!»', 'Herkes güldü; Ebû Ahmed dedi: “Zararı yok, mansaf uzun bir alıştırma ister!”'),
 R('ثُمَّ حَدَّثَهُ عَنْ تَارِيخِ عَمَّانَ، وَقَالَ إِنَّ اسْمَهَا كَانَ «فِيلَادِلْفِيَا» فِي الْعَهْدَيْنِ الْيُونَانِيِّ وَالرُّومَانِيِّ.', 'Sonra ona Amman’ın tarihini anlattı ve Yunan ve Roma dönemlerinde adının “Philadelphia” olduğunu söyledi.'),
 R('وَلَمَّا عَادَ إِلَى شَقَّتِهِ وَجَدَ لُولُو تَنْتَظِرُهُ عِنْدَ الْبَابِ، كَأَنَّهَا تَسْأَلُهُ: «أَيْنَ نَصِيبِي؟»', 'Dairesine döndüğünde Lulu’yu kapıda onu beklerken buldu; sanki “Benim payım nerede?” diye soruyordu.'),
 R('أَعْطَاهَا قِطْعَةً صَغِيرَةً مِنَ اللَّحْمِ، وَقَالَ: «لَيْتَ كُلَّ أَيَّامِي مِثْلُ هَذَا الْيَوْمِ!»', 'Ona küçük bir parça et verdi ve dedi: “Keşke bütün günlerim bu gün gibi olsa!”')],
 [['يُوسُفُ', 'الْمَنْسَفُ؟ سَمِعْتُ عَنْهُ كَثِيرًا، لَكِنِّي لَمْ أَذُقْهُ.', 'Mansaf mı? Çok duydum ama hiç tatmadım.'],
  ['أُمُّ أَحْمَدَ', 'إِنَّهُ لَحْمٌ مَطْبُوخٌ بِلَبَنٍ مُجَفَّفٍ نُسَمِّيهِ «الْجَمِيدَ».', 'O, “cemîd” dediğimiz kurutulmuş yoğurtla pişirilmiş ettir.'],
  ['يُوسُفُ', 'وَمَاذَا أُحْضِرُ مَعِي؟ فِي بِلَادِنَا لَا يَذْهَبُ الضَّيْفُ بِيَدٍ فَارِغَةٍ.', 'Yanımda ne getireyim? Bizim memlekette misafir eli boş gitmez.'],
  ['أُمُّ أَحْمَدَ', 'لَا تُحْضِرْ شَيْئًا، يَكْفِي أَنْ تَأْتِيَ جَائِعًا!', 'Hiçbir şey getirme; aç gelmen yeter!'],
  ['يُوسُفُ', 'إِذَنْ لَنْ آكُلَ شَيْئًا حَتَّى الْمَسَاءِ!', 'O zaman akşama kadar hiçbir şey yemeyeceğim!']])

E[2] = ([
 R('كَانَتْ مَكْتَبَةُ الْمَعْهَدِ صَغِيرَةً، لَكِنَّ رُفُوفَهَا مَلِيئَةٌ بِكُتُبِ اللُّغَةِ وَالْأَدَبِ.', 'Enstitünün kütüphanesi küçüktü, ama rafları dil ve edebiyat kitaplarıyla doluydu.'),
 R('جَاءَتْ أَمِينَةُ وَجَلَسَتْ أَمَامَهُ، وَفَتَحَتْ دِيوَانَ ابْنِ زَيْدُونَ.', 'Emine geldi, karşısına oturdu ve İbn Zeydûn’un divanını açtı.'),
 R('سَأَلَهَا يُوسُفُ: «لِمَاذَا اخْتَرْتِ الشِّعْرَ الْأَنْدَلُسِيَّ بِالذَّاتِ؟»', 'Yusuf ona sordu: “Neden özellikle Endülüs şiirini seçtin?”'),
 R('قَالَتْ: «لِأَنَّ جَدِّي كَانَ يَقُولُ إِنَّ الْبُوسْنَةَ وَالْأَنْدَلُسَ تَشْتَرِكَانِ فِي الْحَنِينِ.»', 'Dedi ki: “Çünkü dedem, Bosna ile Endülüs’ün hasrette ortak olduğunu söylerdi.”'),
 R('لَمْ يَفْهَمْ يُوسُفُ قَصْدَهَا، فَشَرَحَتْ لَهُ أَنَّ كِلْتَيْهِمَا أَرْضٌ عَاشَ فِيهَا الْمُسْلِمُونَ قُرُونًا عَلَى أَطْرَافِ أُورُوبَّا.', 'Yusuf ne demek istediğini anlamadı; o da ona, ikisinin de Müslümanların Avrupa’nın kenarında asırlarca yaşadığı topraklar olduğunu açıkladı.'),
 R('ثُمَّ قَرَأَتْ لَهُ بَيْتًا بِصَوْتٍ خَافِتٍ، فَأَحَسَّ أَنَّ لِلشِّعْرِ مُوسِيقَى لَا تُتَرْجَمُ.', 'Sonra ona alçak sesle bir beyit okudu; Yusuf şiirin tercüme edilemeyen bir musikisi olduğunu hissetti.'),
 R('قَرَّرَ يُوسُفُ أَنْ يَحْفَظَ كُلَّ أُسْبُوعٍ بَيْتَيْنِ مِنَ الشِّعْرِ كَيْ تَقْوَى ذَاكِرَتُهُ.', 'Yusuf hafızası güçlensin diye her hafta iki beyit ezberlemeye karar verdi.'),
 R('وَفِي الْمَسَاءِ وَصَلَتْهُ رِسَالَةٌ مِنَ الْأُسْتَاذِ خَالِدٍ فِيهَا قَائِمَةٌ بِعَشَرَةِ كُتُبٍ.', 'Akşam Hâlid Hoca’dan içinde on kitaplık bir liste bulunan bir mesaj geldi.'),
 R('كَانَ أَوَّلُ الْكُتُبِ «كَلِيلَةَ وَدِمْنَةَ»، فَقَالَ يُوسُفُ فِي نَفْسِهِ: «يَجِبُ أَنْ أَجِدَ هَذَا الْكِتَابَ.»', 'Kitapların ilki “Kelîle ve Dimne” idi; Yusuf içinden “Bu kitabı bulmalıyım” dedi.')],
 [['أَمِينَةُ', 'يَا أُسْتَاذُ، هَلْ نَسْتَطِيعُ أَنْ نَقْرَأَ هَذِهِ الْكُتُبَ دُونَ قَامُوسٍ؟', 'Hocam, bu kitapları sözlüksüz okuyabilir miyiz?'],
  ['الْأُسْتَاذُ خَالِدٌ', 'لَا أُرِيدُ أَنْ تَفْتَحُوا الْقَامُوسَ عِنْدَ كُلِّ كَلِمَةٍ.', 'Her kelimede sözlüğü açmanızı istemiyorum.'],
  ['يُوسُفُ', 'فَمَاذَا نَفْعَلُ إِذَا لَمْ نَفْهَمْ كَلِمَةً؟', 'Peki bir kelimeyi anlamazsak ne yapalım?'],
  ['الْأُسْتَاذُ خَالِدٌ', 'اقْرَؤُوا الْجُمْلَةَ كُلَّهَا أَوَّلًا، فَالسِّيَاقُ يَشْرَحُ أَكْثَرَ مِمَّا تَظُنُّونَ.', 'Önce cümlenin tamamını okuyun; bağlam sandığınızdan fazlasını açıklar.'],
  ['أَمِينَةُ', 'حَسَنًا، سَنُحَاوِلُ أَنْ نَصْبِرَ عَلَى الْكَلِمَاتِ الصَّعْبَةِ.', 'Peki, zor kelimelere sabretmeye çalışacağız.']])

E[3] = ([
 R('فِي الْمَسَاءِ جَلَسَ يُوسُفُ عَلَى الشُّرْفَةِ وَفَتَحَ الْكِتَابَ الْقَدِيمَ بِعِنَايَةٍ.', 'Akşam Yusuf balkonda oturdu ve eski kitabı özenle açtı.'),
 R('كَانَتْ أَوْرَاقُهُ صَفْرَاءَ، وَعَلَى الصَّفْحَةِ الْأُولَى اسْمٌ مَكْتُوبٌ بِخَطٍّ جَمِيلٍ.', 'Sayfaları sararmıştı; ilk sayfada güzel bir hatla yazılmış bir isim vardı.'),
 R('قَرَأَ فِي الْمُقَدِّمَةِ أَنَّ ابْنَ الْمُقَفَّعِ نَقَلَ هَذَا الْكِتَابَ إِلَى الْعَرَبِيَّةِ مِنَ الْفَهْلَوِيَّةِ، أَيِ الْفَارِسِيَّةِ الْقَدِيمَةِ.', 'Mukaddimede İbnü’l-Mukaffa‘ın bu kitabı Pehleviceden, yani eski Farsçadan Arapçaya aktardığını okudu.'),
 R('وَعَرَفَ أَيْضًا أَنَّ أَصْلَ الْكِتَابِ هِنْدِيٌّ، وَأَنَّ حِكَايَاتِهِ تُرْوَى عَلَى أَلْسِنَةِ الْحَيَوَانَاتِ.', 'Kitabın aslının Hint olduğunu ve hikâyelerinin hayvanların dilinden anlatıldığını da öğrendi.'),
 R('لَمْ يَفْهَمْ كُلَّ الْكَلِمَاتِ، لَكِنَّهُ لَمْ يَفْتَحِ الْقَامُوسَ، وَتَذَكَّرَ نَصِيحَةَ أُسْتَاذِهِ.', 'Bütün kelimeleri anlamadı, ama sözlüğü açmadı; hocasının öğüdünü hatırladı.'),
 R('وَفِي الصَّفْحَةِ الْأَخِيرَةِ وَجَدَ وَرَقَةً صَغِيرَةً مَطْوِيَّةً بَيْنَ الْغِلَافِ وَالْأَوْرَاقِ.', 'Son sayfada kapakla sayfalar arasında katlanmış küçük bir kâğıt buldu.'),
 R('كَانَ فِيهَا سَطْرٌ وَاحِدٌ: «مَنْ قَرَأَ هَذَا الْكِتَابَ فَلْيَدْعُ لِصَاحِبِهِ الْأَوَّلِ.»', 'Üzerinde tek bir satır vardı: “Bu kitabı okuyan, ilk sahibine dua etsin.”'),
 R('تَعَجَّبَ يُوسُفُ: مَنْ كَانَ صَاحِبُ هَذَا الْكِتَابِ؟ وَكَيْفَ وَصَلَ إِلَى دُكَّانِ أَبِي سَلِيمٍ؟', 'Yusuf şaşırdı: Bu kitabın sahibi kimdi? Ebû Selîm’in dükkânına nasıl ulaşmıştı?'),
 R('وَضَعَ الْوَرَقَةَ فِي جَيْبِهِ، وَقَالَ فِي نَفْسِهِ: «لَا بُدَّ أَنْ أَسْأَلَ أَبَا سَلِيمٍ عَنْهَا فِي أَقْرَبِ فُرْصَةٍ.»', 'Kâğıdı cebine koydu ve içinden dedi: “İlk fırsatta Ebû Selîm’e bunu mutlaka sormalıyım.”')],
 [['يُوسُفُ', 'سَنَعُودُ إِنْ شَاءَ اللَّهُ. أَيْنَ أَجِدُ مَحَلًّا لِلْقَهْوَةِ؟', 'İnşallah tekrar geliriz. Bir kahveciyi nerede bulurum?'],
  ['الْبَائِعُ', 'امْشِ إِلَى آخِرِ الشَّارِعِ، وَلَا تَدْخُلِ الزُّقَاقَ الضَّيِّقَ.', 'Sokağın sonuna kadar yürü ve dar ara sokağa girme.'],
  ['أَمِينَةُ', 'لِمَاذَا؟ هَلْ هُوَ خَطِيرٌ؟', 'Neden? Tehlikeli mi?'],
  ['الْبَائِعُ', 'لَا، لَكِنَّ فِيهِ عِطْرًا وَبَخُورًا، وَلَنْ تَخْرُجَا مِنْهُ قَبْلَ سَاعَةٍ!', 'Hayır, ama orada parfüm ve buhur var; bir saatten önce oradan çıkamazsınız!'],
  ['يُوسُفُ', 'إِذَنْ لِنَدْخُلْهُ فِي الْمَرَّةِ الْقَادِمَةِ، فَالْيَوْمَ لَمْ يَبْقَ مَعِي مَالٌ.', 'O zaman bir dahaki sefere girelim; bugün yanımda para kalmadı.']])

E[4] = ([
 R('فِي تِلْكَ اللَّيْلَةِ دَعَتْ أُمُّ أَحْمَدَ الْجِيرَانَ إِلَى شُرْبِ الشَّايِ فِي سَاحَةِ الْبَيْتِ.', 'O gece Ümmü Ahmed komşuları evin avlusunda çay içmeye davet etti.'),
 R('جَلَسَ الْكِبَارُ عَلَى الْكَرَاسِيِّ، وَجَلَسَ الْأَطْفَالُ عَلَى الْأَرْضِ حَوْلَ لُولُو.', 'Büyükler sandalyelere, çocuklar Lulu’nun etrafında yere oturdu.'),
 R('كَانَتِ الْقِطَّةُ تَأْكُلُ بِهُدُوءٍ، كَأَنَّهَا لَمْ تَكُنْ فِي خَطَرٍ قَبْلَ سَاعَةٍ.', 'Kedi sakin sakin yiyordu; sanki bir saat önce tehlikede değilmiş gibi.'),
 R('قَالَ أَبُو أَحْمَدَ: «الْأَطْفَالُ يَبْحَثُونَ، وَالْجِيرَانُ يُسَاعِدُونَ، وَيُوسُفُ يَصْعَدُ: هَذَا هُوَ الْحَيُّ!»', 'Ebû Ahmed dedi: “Çocuklar arar, komşular yardım eder, Yusuf tırmanır: işte mahalle budur!”'),
 R('سَأَلَ الْأَطْفَالُ يُوسُفَ: «هَلْ تَلْعَبُونَ فِي تُرْكِيَا كَمَا نَلْعَبُ هُنَا؟»', 'Çocuklar Yusuf’a sordu: “Türkiye’de siz de bizim burada oynadığımız gibi oynar mısınız?”'),
 R('فَحَدَّثَهُمْ عَنْ أَلْعَابِ طُفُولَتِهِ فِي أَزِقَّةِ إِسْطَنْبُولَ، وَعَنْ جَدَّتِهِ الَّتِي كَانَتْ تُطْعِمُ قِطَطَ الشَّارِعِ.', 'O da onlara İstanbul’un ara sokaklarındaki çocukluk oyunlarını ve sokak kedilerini besleyen ninesini anlattı.'),
 R('قَالَتْ سَلْمَى: «إِذَا كَانَتْ جَدَّتُكَ تُحِبُّ الْقِطَطَ، فَلْتَأْتِ إِلَى عَمَّانَ!»', 'Selma dedi: “Ninen kedileri seviyorsa Amman’a gelsin!”'),
 R('ضَحِكَ الْجَمِيعُ، وَوَعَدَهُمْ يُوسُفُ أَنْ يُرِيَهُمْ صُوَرَ قِطَطِ إِسْطَنْبُولَ فِي الْغَدِ.', 'Herkes güldü; Yusuf da ertesi gün onlara İstanbul kedilerinin fotoğraflarını göstereceğine söz verdi.'),
 R('وَقَبْلَ أَنْ يَنْصَرِفَ الْجِيرَانُ قَالَتْ أُمُّ أَحْمَدَ لِلْأَطْفَالِ: «لَا تَتْرُكُوا لُولُو تَصْعَدُ الشَّجَرَةَ بَعْدَ الْيَوْمِ!»', 'Komşular dağılmadan önce Ümmü Ahmed çocuklara dedi: “Bundan sonra Lulu’nun ağaca çıkmasına izin vermeyin!”')],
 [['يُوسُفُ', 'شُكْرًا يَا سَلْمَى. هَلْ تَشْرَبُونَ الشَّايَ بِالنَّعْنَاعِ أَمْ بِالْمَرْيَمِيَّةِ؟', 'Teşekkürler Selma. Çayı nane ile mi içersiniz, adaçayı ile mi?'],
  ['أَحْمَدُ', 'أُمِّي تَضَعُ الْمَرْيَمِيَّةَ دَائِمًا، وَأَبِي يَضَعُ سُكَّرًا كَثِيرًا.', 'Annem hep adaçayı koyar, babam da çok şeker koyar.'],
  ['سَلْمَى', 'وَأَنْتُمْ فِي تُرْكِيَا، أَلَا تَشْرَبُونَ الشَّايَ فِي كُؤُوسٍ صَغِيرَةٍ؟', 'Siz Türkiye’de çayı küçük bardaklarda içmez misiniz?'],
  ['يُوسُفُ', 'بَلَى، وَنَشْرَبُهُ طُولَ النَّهَارِ: فِي الْبَيْتِ وَالْعَمَلِ وَالسُّوقِ.', 'Elbette; hem de bütün gün içeriz: evde, işte ve çarşıda.'],
  ['أَحْمَدُ', 'إِذَنْ أَنْتُمْ تَشْرَبُونَ الشَّايَ مِثْلَ أَبِي تَمَامًا!', 'O zaman siz de çayı tıpkı babam gibi içiyorsunuz!']])

E[5] = ([
 R('فِي صَبَاحِ الْيَوْمِ التَّالِي ذَهَبَ يُوسُفُ إِلَى مَكْتَبِ الْبَرِيدِ مُسْرِعًا قَبْلَ الدَّرْسِ.', 'Ertesi sabah Yusuf dersten önce aceleyle postaneye gitti.'),
 R('سَأَلَهُ الْمُوَظَّفُ مُبْتَسِمًا: «رِسَالَةٌ بِالْبَرِيدِ الْعَادِيِّ؟ قَلِيلٌ مَنْ يَكْتُبُ الرَّسَائِلَ الْيَوْمَ!»', 'Memur gülümseyerek sordu: “Normal postayla mektup mu? Bugün mektup yazan pek az!”'),
 R('قَالَ يُوسُفُ: «أُمِّي تُحِبُّ أَنْ تَقْرَأَ الرِّسَالَةَ وَهِيَ تُمْسِكُهَا بِيَدَيْهَا.»', 'Yusuf dedi: “Annem mektubu elleriyle tutarak okumayı sever.”'),
 R('أَلْصَقَ الْمُوَظَّفُ طَابَعًا عَلَيْهِ صُورَةُ الْبَتْرَاءِ، وَقَالَ: «سَتَصِلُ بَعْدَ أُسْبُوعَيْنِ تَقْرِيبًا.»', 'Memur üzerinde Petra resmi olan bir pul yapıştırdı ve dedi: “Yaklaşık iki hafta sonra ulaşır.”'),
 R('خَرَجَ يُوسُفُ مِنَ الْمَكْتَبِ خَفِيفًا، كَأَنَّهُ أَرْسَلَ جُزْءًا مِنْ قَلْبِهِ.', 'Yusuf postaneden hafiflemiş olarak çıktı; sanki kalbinin bir parçasını göndermişti.'),
 R('وَفِي الطَّرِيقِ إِلَى الْمَعْهَدِ رَأَى أَمِينَةَ وَاقِفَةً عِنْدَ بَائِعِ الْكَعْكِ، فَمَشَيَا مَعًا مُتَحَدِّثَيْنِ.', 'Enstitü yolunda Emine’yi simitçinin yanında dururken gördü; birlikte konuşarak yürüdüler.'),
 R('أَخْبَرَهَا عَنِ الْوَرَقَةِ الَّتِي وَجَدَهَا فِي «كَلِيلَةَ وَدِمْنَةَ»، فَقَرَأَتْهَا مُتَأَمِّلَةً.', 'Ona “Kelîle ve Dimne”de bulduğu kâğıttan bahsetti; Emine onu dikkatle düşünerek okudu.'),
 R('قَالَتْ: «هَذَا خَطٌّ قَدِيمٌ؛ رُبَّمَا كَانَ صَاحِبُ الْكِتَابِ عَالِمًا أَوْ مُعَلِّمًا.»', 'Dedi ki: “Bu eski bir yazı; belki kitabın sahibi bir âlim ya da öğretmendi.”'),
 R('اتَّفَقَا عَلَى أَنْ يَزُورَا أَبَا سَلِيمٍ مَعًا، لِيَسْأَلَاهُ عَنْ سِرِّ هَذِهِ الْوَرَقَةِ.', 'Bu kâğıdın sırrını sormak için Ebû Selîm’i birlikte ziyaret etmeye karar verdiler.')],
 [['أَمِينَةُ', 'وَأَيَّ بَيْتٍ سَتَخْتَارُ؟', 'Peki hangi beyti seçeceksin?'],
  ['يُوسُفُ', 'رُبَّمَا: «أَعَزُّ مَكَانٍ فِي الدُّنَى سَرْجُ سَابِحٍ ... وَخَيْرُ جَلِيسٍ فِي الزَّمَانِ كِتَابُ».', 'Belki şunu: “Dünyada en aziz yer, hızlı koşan bir atın eyeridir; zamanın en hayırlı dostu da kitaptır.”'],
  ['أَمِينَةُ', 'اخْتِيَارٌ جَمِيلٌ، وَسَتَفْرَحُ بِهِ أُمُّكَ وَهِيَ تَقْرَؤُهُ.', 'Güzel bir seçim; annen onu okurken sevinecek.'],
  ['يُوسُفُ', 'سَأَشْرَحُهُ لَهَا بِالتُّرْكِيَّةِ فِي آخِرِ الرِّسَالَةِ حَتَّى لَا يَضِيعَ مَعْنَاهُ.', 'Anlamı kaybolmasın diye mektubun sonunda ona Türkçe açıklayacağım.']])

kok = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
vf = os.path.join(kok, 'veri', 'arapca.js')
s = open(vf, encoding='utf-8').read()
bas = s.index('var D=['); son = s.index('\n];', bas)
D = json.loads(subprocess.check_output(['node', '-e', "const fs=require('fs');const o={};new Function('o',fs.readFileSync(process.argv[1],'utf8')+';o.D=D')(o);process.stdout.write(JSON.stringify(o.D))", vf]))
degisti = False
for i, (rd, dia) in E.items():
    d = D[i]
    if rd[0][0] in [r[0] for r in d['read']]: continue
    d['read'] += rd; d['dia'] += dia; degisti = True
if degisti:
    yeni = 'var D=[\n' + ',\n\n'.join(json.dumps(g, ensure_ascii=False, separators=(',', ':')) for g in D)
    s = s[:bas] + yeni + s[son:]
    open(vf, 'w', encoding='utf-8').write(s)
    sys.path.insert(0, os.path.join(kok, 'tools'))
    from dil_veri import damga
    print('damga', damga('arapca'))
print('uzatıldı:' if degisti else 'zaten uzatılmış:', [(i, len(D[i]['read']), len(D[i]['dia'])) for i in E])
