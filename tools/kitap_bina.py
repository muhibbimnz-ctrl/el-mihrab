import json
def kitap(id, baslik, bolumler, sorular):
    d={'id':id,'baslik':baslik,'tur':'ders','kaynak':'el-Mihrâb ders notu','bolumler':[{'b':b,'tr_b':t,'n':n,'ornek':o} for b,t,n,o in bolumler],
       'sorular':[{'b':b,'s':s,'k':k,'d':0,'a':a} for b,s,k,a in sorular]}
    json.dump(d,open(f'data/kitap/{id}.json','w'),ensure_ascii=False,indent=0); print(id,len(bolumler),len(sorular))

kitap('bina','البناء — بناء الأفعال',[
 ('مدخل','Binâ’ya giriş: fiilin binâsı',[
  'Binâ, Emsile’den sonra okunan ikinci sarf kitabıdır. Emsile’de bir fiilin <b>nasıl çekildiğini</b> ezberledik; Binâ fiilin <b>nasıl kurulduğunu</b> (binâsını) öğretir: kaç harfli olduğu, harflerinin asıl mı zâid mi olduğu, hangi bâbdan geldiği ve harflerinin sağlam mı illetli mi olduğu.',
  'Fiilin harfleri <span lang="ar">ف ع ل</span> ile tartılır: birinci asıl harfe <b>fâ’ü’l-fiil</b>, ikinciye <b>ayn’ül-fiil</b>, üçüncüye <b>lâm’ül-fiil</b> denir. <span lang="ar">نَصَرَ</span> kelimesinde ن fâ’ü’l-fiil, ص ayn’ül-fiil, ر lâm’ül-fiildir.',
  'Fiil asıl harflerinin sayısına göre <b>sülâsî</b> (üç harfli) veya <b>rubâî</b> (dört harfli) olur; asıl harflerinin üzerine harf eklenmemişse <b>mücerred</b>, eklenmişse <b>mezîd</b> adını alır. Bu kitap geleneğinde tasrîf bâbları otuz beş sayılır; bunların altısı sülâsî mücerred içindir.'],
  [('نَصَرَ','sülâsî mücerred (3 asıl harf)'),('أَكْرَمَ','sülâsî mezîd (bir harf ziyâdeli)'),('دَحْرَجَ','rubâî mücerred (4 asıl harf)'),('تَدَحْرَجَ','rubâî mezîd')]),
 ('الثلاثي المجرد','Sülâsî mücerredin altı bâbı ve alâmetleri',[
  'Sülâsî mücerred fiilin bâbı, ayn’ül-fiilin mâzîdeki ve muzârideki harekesine bakılarak bilinir:',
  '<b>1. Nasara</b> (<span lang="ar">فَعَلَ يَفْعُلُ</span>): mâzîde fetha, muzâride damme. <b>2. Daraba</b> (<span lang="ar">فَعَلَ يَفْعِلُ</span>): fetha / kesre. <b>3. Fetaha</b> (<span lang="ar">فَعَلَ يَفْعَلُ</span>): fetha / fetha — şartı, ayn’ül-fiil veya lâm’ül-fiilin halk harflerinden (<span lang="ar">ء ه ع ح غ خ</span>) biri olmasıdır. <b>4. Alime</b> (<span lang="ar">فَعِلَ يَفْعَلُ</span>): kesre / fetha. <b>5. Hasibe</b> (<span lang="ar">فَعِلَ يَفْعِلُ</span>): kesre / kesre — az kullanılır. <b>6. Kerume</b> (<span lang="ar">فَعُلَ يَفْعُلُ</span>): damme / damme — tabiat ve kalıcı vasıf bildirir, daima lâzımdır.',
  'Kur’an’daki fiillerin bâbını “Bâb bul” oyununda ve Kur’an i‘râbı modülündeki kelime kartında görebilirsiniz.'],
  [('نَصَرَ يَنْصُرُ','1. bâb'),('ضَرَبَ يَضْرِبُ','2. bâb'),('فَتَحَ يَفْتَحُ','3. bâb (ح halk harfi)'),('عَلِمَ يَعْلَمُ','4. bâb'),('حَسِبَ يَحْسِبُ','5. bâb'),('كَرُمَ يَكْرُمُ','6. bâb (tabiat)')]),
 ('المزيد بحرف','Bir harf ziyâdeli sülâsî mezîd',[
  '<b>İf‘âl</b> (<span lang="ar">أَفْعَلَ يُفْعِلُ إِفْعَالًا</span>): başa hemze eklenir. Çoğunlukla ta‘diye (geçişli yapma) içindir: <span lang="ar">خَرَجَ</span> çıktı → <span lang="ar">أَخْرَجَ</span> çıkardı. Ayrıca bir şeyi o sıfatta bulma (<span lang="ar">أَحْمَدْتُهُ</span> onu övülmeye lâyık buldum), bir vakte girme (<span lang="ar">أَصْبَحَ</span> sabaha girdi) gibi mânâlar verir.',
  '<b>Tef‘îl</b> (<span lang="ar">فَعَّلَ يُفَعِّلُ تَفْعِيلًا</span>): ayn’ül-fiil şeddelenir. Teksîr (çokluk) ve ta‘diye içindir: <span lang="ar">قَطَعَ</span> kesti → <span lang="ar">قَطَّعَ</span> paramparça etti; <span lang="ar">فَرِحَ</span> sevindi → <span lang="ar">فَرَّحَ</span> sevindirdi. Nisbet de bildirir: <span lang="ar">كَذَّبَهُ</span> onu yalanlamakla nitelendi.',
  '<b>Mufâale</b> (<span lang="ar">فَاعَلَ يُفَاعِلُ مُفَاعَلَةً</span>): fâ’dan sonra elif eklenir. Müşâreke (karşılıklılık) içindir: <span lang="ar">ضَارَبَ زَيْدٌ عَمْرًا</span> Zeyd Amr’la dövüştü.'],
  [('أَكْرَمَ يُكْرِمُ إِكْرَامًا','if‘âl — ikram etti'),('عَلَّمَ يُعَلِّمُ تَعْلِيمًا','tef‘îl — öğretti'),('قَاتَلَ يُقَاتِلُ مُقَاتَلَةً','mufâale — savaştı')]),
 ('المزيد بحرفين','İki harf ziyâdeli sülâsî mezîd',[
  '<b>İnfi‘âl</b> (<span lang="ar">اِنْفَعَلَ يَنْفَعِلُ اِنْفِعَالًا</span>): mutâvaat (etkiyi kabul) içindir: <span lang="ar">كَسَرْتُهُ فَانْكَسَرَ</span> onu kırdım, kırıldı. Daima lâzımdır.',
  '<b>İfti‘âl</b> (<span lang="ar">اِفْتَعَلَ يَفْتَعِلُ اِفْتِعَالًا</span>): mutâvaat ve kendi için yapma: <span lang="ar">جَمَعْتُهُ فَاجْتَمَعَ</span>. Fâ’ü’l-fiil <span lang="ar">ص ض ط ظ</span> ise bâbın tâ’sı ط’ye (<span lang="ar">اِصْطَبَرَ</span>), <span lang="ar">د ذ ز</span> ise د’ye (<span lang="ar">اِزْدَجَرَ</span>) döner; vâv ise tâya çevrilip idgâm edilir (<span lang="ar">اِتَّصَلَ</span>).',
  '<b>İf‘ilâl</b> (<span lang="ar">اِفْعَلَّ يَفْعَلُّ اِفْعِلَالًا</span>): renk ve ayıplarda mübalağa: <span lang="ar">اِحْمَرَّ</span> kızardı, <span lang="ar">اِعْوَرَّ</span> şaşı oldu.',
  '<b>Tefa‘‘ul</b> (<span lang="ar">تَفَعَّلَ يَتَفَعَّلُ تَفَعُّلًا</span>): tef‘îlin mutâvaatı ve tekellüf: <span lang="ar">عَلَّمْتُهُ فَتَعَلَّمَ</span>; <span lang="ar">تَشَجَّعَ</span> cesur görünmeye çalıştı.',
  '<b>Tefâ‘ul</b> (<span lang="ar">تَفَاعَلَ يَتَفَاعَلُ تَفَاعُلًا</span>): ikiden fazla taraf arasında müşâreke ve gibi görünme: <span lang="ar">تَضَارَبُوا</span> birbirlerini dövdüler; <span lang="ar">تَمَارَضَ</span> hasta numarası yaptı.'],
  [('اِنْقَطَعَ','infi‘âl — kesildi'),('اِجْتَمَعَ','ifti‘âl — toplandı'),('اِصْفَرَّ','if‘ilâl — sarardı'),('تَكَلَّمَ','tefa‘‘ul — konuştu'),('تَعَاوَنَ','tefâ‘ul — yardımlaştı')]),
 ('المزيد بثلاثة أحرف','Üç harf ziyâdeli sülâsî mezîd',[
  '<b>İstif‘âl</b> (<span lang="ar">اِسْتَفْعَلَ يَسْتَفْعِلُ اِسْتِفْعَالًا</span>): talep (<span lang="ar">اِسْتَغْفَرَ</span> mağfiret diledi), bir şeyi o vasıfta bulma (<span lang="ar">اِسْتَعْظَمَهُ</span> onu büyük gördü) ve dönüşme (<span lang="ar">اِسْتَحْجَرَ الطِّينُ</span> çamur taşlaştı).',
  '<b>İf‘îlâl</b> (<span lang="ar">اِفْعَالَّ</span>): if‘ilâlden daha kuvvetli mübalağa: <span lang="ar">اِحْمَارَّ</span>. <b>İf‘îvvâl</b> (<span lang="ar">اِفْعَوَّلَ</span>): <span lang="ar">اِجْلَوَّذَ</span> hızlı gitti. <b>İf‘î‘âl</b> (<span lang="ar">اِفْعَوْعَلَ</span>): <span lang="ar">اِعْشَوْشَبَتِ الْأَرْضُ</span> yer çok otlandı.'],
  [('اِسْتَخْرَجَ يَسْتَخْرِجُ اِسْتِخْرَاجًا','istif‘âl — çıkarmaya çalıştı, çıkardı'),('اِخْضَوْضَرَ','if‘î‘âl — yemyeşil oldu')]),
 ('الرباعي','Rubâî mücerred, mülhak ve mezîd',[
  '<b>Rubâî mücerred</b>in tek bâbı vardır: <span lang="ar">فَعْلَلَ يُفَعْلِلُ فَعْلَلَةً</span> (<span lang="ar">دَحْرَجَ</span> yuvarladı, <span lang="ar">زَلْزَلَ</span> sarstı).',
  '<b>Mülhak bi’r-rubâî:</b> sülâsî bir köke bir harf eklenerek rubâî kalıbına sokulan fiillerdir; aynen rubâî gibi çekilir: <span lang="ar">جَلْبَبَ</span> (cilbâb giydirdi), <span lang="ar">حَوْقَلَ</span>, <span lang="ar">بَيْطَرَ</span>.',
  '<b>Rubâî mezîd</b>: <span lang="ar">تَفَعْلَلَ</span> (<span lang="ar">تَدَحْرَجَ</span> yuvarlandı — mutâvaat), <span lang="ar">اِفْعَنْلَلَ</span> (<span lang="ar">اِحْرَنْجَمَ</span> toplandı), <span lang="ar">اِفْعَلَلَّ</span> (<span lang="ar">اِقْشَعَرَّ</span> tüyleri ürperdi; <span lang="ar">اِطْمَأَنَّ</span> mutmain oldu).'],
  [('زَلْزَلَ يُزَلْزِلُ زَلْزَلَةً','rubâî mücerred'),('تَزَلْزَلَ','tefa‘lül — sarsıldı'),('اِطْمَأَنَّ يَطْمَئِنُّ اِطْمِئْنَانًا','if‘illâl')]),
 ('اللازم والمتعدي','Lâzım ve müteaddî',[
  '<b>Lâzım</b> fiil fâiliyle yetinir, mef‘ûle geçmez: <span lang="ar">جَلَسَ زَيْدٌ</span>. <b>Müteaddî</b> fiil fâilini geçip mef‘ûlün bih alır: <span lang="ar">ضَرَبَ زَيْدٌ عَمْرًا</span>.',
  'Lâzım fiil üç yolla müteaddî yapılır: if‘âl bâbına nakil (<span lang="ar">أَذْهَبَهُ</span>), tef‘îl bâbına nakil (<span lang="ar">فَرَّحَهُ</span>) ve harf-i cer ile (<span lang="ar">ذَهَبَ بِهِ</span> onu götürdü).'],
  [('خَرَجَ ← أَخْرَجَ','lâzım → müteaddî (if‘âl)'),('نَزَلَ ← نَزَّلَ','lâzım → müteaddî (tef‘îl)'),('ذَهَبَ ← ذَهَبَ بِ','harf-i cer ile')]),
 ('أقسام الفعل السبعة','Fiilin yedi kısmı (heft aksâm)',[
  'Medresede şu meşhur beyitle ezberlenir: <span lang="ar">صَحِيحٌ اسْت وَمِثَال اسْت وَمُضَاعَف ✦ لَفِيف وَنَاقِص وَمَهْمُوز وَأَجْوَف</span> (Farsça).',
  '<b>Sahîh</b>: harflerinde harf-i illet (و، ي، ا), hemze ve tekrar olmayan: <span lang="ar">نَصَرَ</span>. <b>Mehmûz</b>: harflerinden biri hemze: fâ’da <span lang="ar">أَخَذَ</span>, ayn’da <span lang="ar">سَأَلَ</span>, lâm’da <span lang="ar">قَرَأَ</span>. <b>Muzâaf</b>: ayn ve lâm’ı aynı harf: <span lang="ar">مَدَّ</span> (aslı <span lang="ar">مَدَدَ</span>).',
  '<b>Misâl</b>: fâ’sı illetli: vâvî <span lang="ar">وَعَدَ</span>, yâî <span lang="ar">يَسَرَ</span>. <b>Ecvef</b>: ayn’ı illetli: vâvî <span lang="ar">قَالَ</span> (aslı <span lang="ar">قَوَلَ</span>), yâî <span lang="ar">بَاعَ</span> (aslı <span lang="ar">بَيَعَ</span>). <b>Nâkıs</b>: lâm’ı illetli: vâvî <span lang="ar">دَعَا</span>, yâî <span lang="ar">رَمَى</span>. <b>Lefîf</b>: iki harfi illetli; illet harfleri ayrıksa <b>mefrûk</b> (<span lang="ar">وَقَى</span>), bitişikse <b>makrûn</b> (<span lang="ar">طَوَى</span>).'],
  [('كَتَبَ','sahîh'),('أَمَرَ','mehmûzü’l-fâ'),('شَدَّ','muzâaf'),('وَصَلَ','misâl-i vâvî'),('خَافَ','ecvef-i vâvî'),('مَشَى','nâkıs-ı yâî'),('وَفَى','lefîf-i mefrûk'),('رَوَى','lefîf-i makrûn')]),
 ('الإدغام','İdgâm',[
  'İdgâm, iki benzer harften birincisini sâkin yapıp ikincisine katmaktır; şedde ile yazılır. Muzâaf fiillerde üç hâl vardır:',
  '<b>Vâcib</b>: iki harf de harekeli ise: <span lang="ar">مَدَدَ ← مَدَّ</span>, <span lang="ar">يَمْدُدُ ← يَمُدُّ</span> (ilk harfin harekesi önceki sâkine nakledilir). <b>Câiz</b>: ikinci harf cezm veya emir sebebiyle sâkinse: <span lang="ar">لَمْ يَمْدُدْ</span> veya <span lang="ar">لَمْ يَمُدَّ</span>; <span lang="ar">اُمْدُدْ</span> veya <span lang="ar">مُدَّ</span>. <b>Mümteni‘</b>: ikinci harf mütehharrik bir zamir sebebiyle aslen sâkin olursa: <span lang="ar">مَدَدْتُ، مَدَدْنَا، يَمْدُدْنَ</span>.'],
  [('رَدَّ يَرُدُّ','idgâm vâcib'),('لَمْ يَرْدُدْ / لَمْ يَرُدَّ','idgâm câiz'),('رَدَدْتُ','idgâm mümteni‘')]),
],[
 (0,'نَصَرَ fiilinde ص harfine ne denir?',['Ayn’ül-fiil','Fâ’ü’l-fiil','Lâm’ül-fiil','Harf-i zâid'],'ف ع ل vezninde ikinci harf ayn’ül-fiildir.'),
 (1,'فَعَلَ يَفْعَلُ (Fetaha) bâbının şartı nedir?',['Ayn veya lâm’ül-fiilin halk harfi olması','Fiilin lâzım olması','Fâ’nın vâv olması','Fiilin rubâî olması'],'فتح يفتح: ح halk harfidir.'),
 (1,'Kerume bâbındaki fiiller genellikle neyi bildirir?',['Tabiat ve kalıcı vasıf','Karşılıklılık','Talep','Renk ve ayıp'],'كَرُمَ، حَسُنَ، شَرُفَ: kalıcı vasıflar; daima lâzımdır.'),
 (2,'أَخْرَجَ hangi bâbdandır?',['İf‘âl','Tef‘îl','Mufâale','İfti‘âl'],'أَفْعَلَ يُفْعِلُ إِفْعَالًا.'),
 (2,'Mufâale bâbının asıl mânâsı nedir?',['Müşâreke (karşılıklılık)','Mutâvaat','Talep','Teksîr'],'ضَارَبَ، قَاتَلَ.'),
 (3,'كَسَرْتُهُ فَانْكَسَرَ örneğindeki اِنْكَسَرَ hangi mânâyı verir?',['Mutâvaat','Talep','Tekellüf','Müşâreke'],'İnfi‘âl bâbı mutâvaat içindir ve lâzımdır.'),
 (3,'اِصْطَبَرَ kelimesinde bâbın tâ’sı neden ط olmuştur?',['Fâ’ü’l-fiil ص olduğu için','Kök tâ ile bittiği için','Muzâaf olduğu için','Kural dışı (semâî) olduğu için'],'İfti‘âlde fâ’ü’l-fiil ص ض ط ظ ise tâ, ط’ye döner.'),
 (3,'اِحْمَرَّ hangi bâbdandır?',['İf‘ilâl','İfti‘âl','İnfi‘âl','İstif‘âl'],'Renk ve ayıplarda: اِفْعَلَّ.'),
 (4,'اِسْتَغْفَرَ fiilinde istif‘âl bâbı hangi mânâyı verir?',['Talep','Mutâvaat','Müşâreke','Renk'],'Mağfiret talep etti.'),
 (5,'Rubâî mücerredin kalıbı hangisidir?',['فَعْلَلَ','تَفَعَّلَ','اِفْعَلَّ','فَاعَلَ'],'دَحْرَجَ، زَلْزَلَ.'),
 (6,'Lâzım fiili müteaddî yapan yollardan hangisi DEĞİLDİR?',['İnfi‘âl bâbına nakil','If‘âl bâbına nakil','Tef‘îl bâbına nakil','Harf-i cer'],'İnfi‘âl mutâvaat içindir ve lâzım yapar.'),
 (7,'قَالَ fiili yedi kısımdan hangisidir?',['Ecvef-i vâvî','Nâkıs-ı vâvî','Misâl-i vâvî','Lefîf'],'Aslı قَوَلَ; ayn’ül-fiil vâvdır.'),
 (7,'وَقَى fiili hangi kısımdandır?',['Lefîf-i mefrûk','Lefîf-i makrûn','Misâl','Nâkıs'],'Fâ’ ve lâm illetli, aralarında sahîh harf var: mefrûk.'),
 (8,'مَدَدْتُ kelimesinde idgâmın hükmü nedir?',['Mümteni‘','Vâcib','Câiz','Hepsi olabilir'],'İkinci harf mütehharrik zamir sebebiyle sâkin: idgâm yapılamaz.'),
])
