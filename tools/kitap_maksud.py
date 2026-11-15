import json
exec(open('tools/kitap_bina.py').read().split("kitap('bina'")[0])
kitap('maksud','المقصود في التصريف',[
 ('مقدمة','Maksûd’a giriş: tasrîf ve masdar',[
  'Maksûd, Binâ’dan sonra okunur ve sarfın kurallarını <b>gerekçeleriyle</b> verir. Müellifi olarak İmâm-ı Âzam Ebû Hanîfe gösterilir; bu nisbet tartışmalıdır.',
  'Kitabın ana fikri: kelimelerin aslı <b>masdar</b>dır; mâzî, muzâri, emir, ism-i fâil, ism-i mef‘ûl… hep masdardan türer (Basra mektebinin görüşü). Kûfeliler ise aslın fiil olduğunu söyler.',
  'Sülâsî mücerredin masdarları <b>semâî</b>dir (duyularak öğrenilir): <span lang="ar">نَصْرٌ، ضَرْبٌ، عِلْمٌ، دُخُولٌ، كِتَابَةٌ</span>. Mezîd ve rubâînin masdarları ise <b>kıyâsî</b>dir (kalıba göre yapılır): <span lang="ar">إِكْرَامٌ، تَعْلِيمٌ، مُقَاتَلَةٌ، اِسْتِخْرَاجٌ، دَحْرَجَةٌ</span>.'],
  [('ذَهَبَ ذَهَابًا','semâî masdar'),('جَلَسَ جُلُوسًا','semâî masdar'),('أَكْرَمَ إِكْرَامًا','kıyâsî masdar'),('اِنْطَلَقَ اِنْطِلَاقًا','kıyâsî masdar')]),
 ('اشتقاق الأمثلة','Kalıpların türetilme sırası',[
  'Medrese usulünde kalıplar şu sırayla türetilir: <b>masdar → mâzî → muzâri → emir ve nehiy → ism-i fâil → ism-i mef‘ûl → ism-i zaman ve mekân → ism-i âlet → ism-i tafdîl</b>.',
  '<b>Muzâri</b>, mâzînin başına muzâri harflerinden (<span lang="ar">أَنَيْتُ</span>) birini getirip fâ’ü’l-fiili sâkin yapmakla kurulur: <span lang="ar">نَصَرَ ← يَنْصُرُ</span>. Muzâri harfi rubâî ve if‘âl, tef‘îl, mufâale bâblarında dammeli (<span lang="ar">يُكْرِمُ، يُعَلِّمُ، يُقَاتِلُ، يُدَحْرِجُ</span>), diğerlerinde fethalıdır.',
  '<b>Emr-i hâzır</b>, muhâtab muzârinin başındaki harf atılıp sonu cezmedilerek yapılır; ilk harf sâkin kalırsa hemze-i vasl getirilir: <span lang="ar">تَنْصُرُ ← نْصُرْ ← اُنْصُرْ</span>. Hemze, ayn’ül-fiil dammeli ise dammeli, değilse kesreli olur (<span lang="ar">اِضْرِبْ، اِفْتَحْ</span>). If‘âl bâbında hemze-i kat‘ geri döner: <span lang="ar">أَكْرِمْ</span>.'],
  [('تَضْرِبُ ← اِضْرِبْ','emir yapımı'),('تَعْلَمُ ← اِعْلَمْ','emir yapımı'),('تُكْرِمُ ← أَكْرِمْ','if‘âlde hemze-i kat‘')]),
 ('اسم الفاعل والمفعول','İsm-i fâil ve ism-i mef‘ûl',[
  'Sülâsî mücerredde ism-i fâil <span lang="ar">فَاعِلٌ</span> (<span lang="ar">نَاصِرٌ</span>), ism-i mef‘ûl <span lang="ar">مَفْعُولٌ</span> (<span lang="ar">مَنْصُورٌ</span>) kalıbındadır.',
  'Mezîd ve rubâîde ikisi de <b>muzârinin harfini mîm-i mazmûme</b> ile değiştirerek yapılır; ism-i fâilde sondan bir önceki harf kesreli, ism-i mef‘ûlde fethalıdır: <span lang="ar">يُكْرِمُ ← مُكْرِمٌ / مُكْرَمٌ</span>, <span lang="ar">يَسْتَخْرِجُ ← مُسْتَخْرِجٌ / مُسْتَخْرَجٌ</span>, <span lang="ar">يُدَحْرِجُ ← مُدَحْرِجٌ / مُدَحْرَجٌ</span>.',
  'Lâzım fiilin ism-i mef‘ûlü ancak harf-i cer ile yapılır: <span lang="ar">مَذْهُوبٌ بِهِ</span>, <span lang="ar">مَغْضُوبٌ عَلَيْهِمْ</span> (Fâtiha).'],
  [('عَالِمٌ / مَعْلُومٌ','sülâsî'),('مُعَلِّمٌ / مُعَلَّمٌ','tef‘îl'),('مُجْتَهِدٌ','ifti‘âl ism-i fâil'),('مُنْطَلَقٌ','infi‘âl — ism-i mekân/masdar-ı mîmî olarak')]),
 ('الزمان والمكان والآلة','İsm-i zaman-mekân, ism-i âlet, masdar-ı mîmî',[
  'Sülâsîde ism-i zaman ve mekân, muzârinin ayn’ül-fiili kesreli ise <span lang="ar">مَفْعِلٌ</span> (<span lang="ar">مَجْلِسٌ</span> oturulan yer), fethalı veya dammeli ise <span lang="ar">مَفْعَلٌ</span>dır (<span lang="ar">مَكْتَبٌ، مَذْهَبٌ</span>). Bazı kelimeler kural dışı kesreyle gelir: <span lang="ar">مَسْجِدٌ، مَشْرِقٌ، مَغْرِبٌ</span>.',
  'Mezîdde ism-i zaman-mekân ve masdar-ı mîmî, ism-i mef‘ûl kalıbındadır: <span lang="ar">مُجْتَمَعٌ</span> (toplanma yeri), <span lang="ar">مُنْقَلَبٌ</span> (dönüş yeri).',
  'İsm-i âlet yalnız sülâsîden üç kalıpla yapılır: <span lang="ar">مِفْعَلٌ</span> (<span lang="ar">مِبْرَدٌ</span> eğe), <span lang="ar">مِفْعَلَةٌ</span> (<span lang="ar">مِكْنَسَةٌ</span> süpürge), <span lang="ar">مِفْعَالٌ</span> (<span lang="ar">مِفْتَاحٌ</span> anahtar).'],
  [('مَطْبَخٌ','mutfak — مَفْعَلٌ'),('مَنْزِلٌ','konak — مَفْعِلٌ'),('مِنْشَارٌ','testere — مِفْعَالٌ'),('مُسْتَشْفًى','hastane — istif‘âl ism-i mekânı')]),
 ('الإعلال: الأجوف','İ‘lâl (1): ecvef',[
  'İ‘lâl, harf-i illetin (و، ي) değiştirilmesi, düşürülmesi veya sâkin yapılmasıdır. Ecvef fiillerin temel kuralı: <b>harekeli vâv veya yâ, öncesi fethalı ise elife kalbolunur</b>: <span lang="ar">قَوَلَ ← قَالَ</span>, <span lang="ar">بَيَعَ ← بَاعَ</span>, <span lang="ar">خَوِفَ ← خَافَ</span>.',
  'Muzâride illet harfinin harekesi önündeki sâkin sahîh harfe nakledilir: <span lang="ar">يَقْوُلُ ← يَقُولُ</span>, <span lang="ar">يَبْيِعُ ← يَبِيعُ</span>, <span lang="ar">يَخْوَفُ ← يَخَافُ</span>.',
  'Cezm ve emirde iki sâkin bir araya gelince illet harfi düşer: <span lang="ar">لَمْ يَقُلْ، قُلْ، لَمْ يَبِعْ، بِعْ، خَفْ</span>. Mütehharrik zamirle mâzîde de düşer: <span lang="ar">قُلْتُ، بِعْتُ، خِفْتُ</span> (nasara bâbında fâ dammeli, diğerlerinde kesreli).'],
  [('قَالَ يَقُولُ قُلْ','ecvef-i vâvî'),('بَاعَ يَبِيعُ بِعْ','ecvef-i yâî'),('نَامَ يَنَامُ نَمْ','ecvef, alime bâbı'),('قَائِلٌ / مَقُولٌ','ism-i fâil ve mef‘ûl')]),
 ('الإعلال: الناقص والمثال','İ‘lâl (2): nâkıs ve misâl',[
  '<b>Nâkıs</b>: Sondaki vâv/yâ öncesi fethalı ise elife döner: <span lang="ar">دَعَوَ ← دَعَا</span>, <span lang="ar">رَمَيَ ← رَمَى</span>. Muzâride merfûda damme ağır geldiği için takdir edilir (<span lang="ar">يَدْعُو، يَرْمِي، يَخْشَى</span>); cezmde illet harfi düşer: <span lang="ar">لَمْ يَدْعُ، لَمْ يَرْمِ، لَمْ يَخْشَ</span>; emirde de: <span lang="ar">اُدْعُ، اِرْمِ، اِخْشَ</span>.',
  'Vâv-ı cemâat gelince illet harfi düşer: <span lang="ar">دَعَوْا، رَمَوْا، خَشُوا</span>; <span lang="ar">يَدْعُونَ، يَرْمُونَ</span>.',
  '<b>Misâl-i vâvî</b>: Muzârinin ayn’ül-fiili kesreli ise vâv muzâride düşer: <span lang="ar">وَعَدَ يَعِدُ عِدْ</span>, <span lang="ar">وَصَلَ يَصِلُ صِلْ</span>; masdarda da düşüp sonuna tâ gelebilir: <span lang="ar">عِدَةٌ، صِلَةٌ</span>. Ayn’ül-fiil fethalı ise genelde kalır: <span lang="ar">وَجِلَ يَوْجَلُ</span>.'],
  [('دَعَا يَدْعُو اُدْعُ','nâkıs-ı vâvî'),('رَمَى يَرْمِي اِرْمِ','nâkıs-ı yâî'),('وَهَبَ يَهَبُ هَبْ','misâl (ayn fethalı ama halk harfi sebebiyle)'),('وَقَى يَقِي قِ','lefîf-i mefrûk — emir tek harf!')]),
 ('المهموز والمضاعف','Mehmûz ve muzâafın hükümleri',[
  '<b>Mehmûz</b>: İki hemze bir kelimede yan yana gelip ikincisi sâkin olursa, ikinci hemze öncekinin harekesine uygun med harfine döner: <span lang="ar">أَأْمَنَ ← آمَنَ</span>, <span lang="ar">أُؤْمِنُ ← أُومِنُ</span>, <span lang="ar">إِئْمَانٌ ← إِيمَانٌ</span>.',
  'Üç fiilin emrinde hemze ile birlikte hemze-i vasl da düşer: <span lang="ar">أَخَذَ ← خُذْ</span>, <span lang="ar">أَكَلَ ← كُلْ</span>, <span lang="ar">أَمَرَ ← مُرْ</span>. <span lang="ar">سَأَلَ</span> fiilinin emri hem <span lang="ar">اِسْأَلْ</span> hem <span lang="ar">سَلْ</span> olur.',
  '<b>Muzâaf</b>: idgâm kuralları Binâ’daki gibidir; ism-i fâil <span lang="ar">مَادٌّ</span> (aslı <span lang="ar">مَادِدٌ</span>), ism-i mef‘ûl <span lang="ar">مَمْدُودٌ</span> olur.'],
  [('آمَنَ يُؤْمِنُ إِيمَانًا','mehmûzü’l-fâ, if‘âl'),('خُذْ، كُلْ، مُرْ','kısaltılmış emirler'),('ضَالٌّ','muzâaf ism-i fâil (aslı ضَالِلٌ)')]),
],[
 (0,'Basra mektebine göre kelimelerin aslı nedir?',['Masdar','Mâzî fiil','Muzâri fiil','Emir'],'Basralılar masdarın asıl olduğunu, fiillerin ondan türediğini söyler.'),
 (0,'Hangi masdar semâîdir?',['ذَهَابٌ','إِكْرَامٌ','تَعْلِيمٌ','اِسْتِخْرَاجٌ'],'Sülâsî mücerredin masdarları semâîdir.'),
 (1,'Hangi fiilin muzâri harfi dammelidir?',['أَكْرَمَ','نَصَرَ','اِنْطَلَقَ','تَعَلَّمَ'],'Rubâî ve if‘âl, tef‘îl, mufâalede muzâri harfi dammelidir: يُكْرِمُ.'),
 (1,'ضَرَبَ fiilinin emr-i hâzırı nasıldır?',['اِضْرِبْ','اُضْرُبْ','أَضْرِبْ','ضَرِّبْ'],'Ayn’ül-fiil kesreli olduğu için hemze-i vasl kesreli.'),
 (2,'اِسْتَخْرَجَ fiilinin ism-i mef‘ûlü hangisidir?',['مُسْتَخْرَجٌ','مُسْتَخْرِجٌ','مَسْتَخْرُوجٌ','اِسْتِخْرَاجٌ'],'Mîm-i mazmûme + sondan bir önceki fetha.'),
 (2,'Lâzım fiilden ism-i mef‘ûl nasıl yapılır?',['Harf-i cer ile (مَغْضُوبٌ عَلَيْهِمْ)','Yapılamaz','مُفْعَلٌ kalıbıyla','Masdarla'],'غَضِبَ lâzımdır; mef‘ûlü cer harfiyle gelir.'),
 (3,'مِفْتَاحٌ hangi kalıptadır?',['İsm-i âlet (مِفْعَالٌ)','İsm-i mekân','İsm-i tafdîl','Masdar-ı mîmî'],'Anahtar: açma âleti.'),
 (3,'جَلَسَ يَجْلِسُ fiilinin ism-i mekânı hangisidir?',['مَجْلِسٌ','مَجْلَسٌ','مُجْلَسٌ','مِجْلَسٌ'],'Muzâride ayn kesreli: مَفْعِلٌ.'),
 (4,'قَالَ fiilinin aslı nedir?',['قَوَلَ','قَيَلَ','قَالَلَ','قَأَلَ'],'Harekeli vâv, öncesi fethalı → elif.'),
 (4,'خَافَ fiilinin mütekellim mâzîsi (أنا) hangisidir?',['خِفْتُ','خُفْتُ','خَافْتُ','خَوِفْتُ'],'Alime bâbından ecvef: fâ kesreli olur.'),
 (5,'لَمْ يَدْعُ ifadesinde vâv neden düşmüştür?',['Cezm alâmeti olarak harf-i illet hazfedildi','Vâv-ı cemâat geldiği için','İdgâm sebebiyle','Kural dışı'],'Sonu mu‘tel muzârinin cezmi illet harfinin hazfıyladır.'),
 (5,'وَعَدَ fiilinin emri hangisidir?',['عِدْ','اِوْعِدْ','وَعِدْ','اُعْدُ'],'Misâl-i vâvîde vâv muzâride ve emirde düşer.'),
 (6,'أَخَذَ fiilinin emri hangisidir?',['خُذْ','اُؤْخُذْ','أُخُذْ','اِيخَذْ'],'خُذْ، كُلْ، مُرْ kısaltılmış emirlerdir.'),
 (6,'إِيمَانٌ kelimesinin aslı nedir?',['إِئْمَانٌ','أَيْمَانٌ','إِيمَنٌ','أُؤْمَانٌ'],'İkinci hemze sâkin, öncesi kesreli → yâ.'),
])
