import json
exec(open('tools/kitap_bina.py').read().split("kitap('bina'")[0])
kitap('avamil','العوامل',[
 ('العامل والمعمول','Âmil, ma‘mûl ve i‘râb',[
  'Avâmil, nahve giriş kitabıdır. Temel fikri şudur: kelimenin sonundaki değişiklik (i‘râb) kendiliğinden olmaz; onu bir <b>âmil</b> yapar. Âmilin etkilediği kelimeye <b>ma‘mûl</b>, ortaya çıkan harekeye <b>i‘râb alâmeti</b> denir.',
  '<span lang="ar">فِي الدَّارِ</span> örneğinde <span lang="ar">فِي</span> âmil, <span lang="ar">الدَّارِ</span> ma‘mûl, kesre i‘râb alâmetidir.',
  'Âmiller <b>lafzî</b> (söylenen bir kelime: harf, fiil veya isim) ve <b>ma‘nevî</b> (söylenmeyen, anlamdan doğan) olmak üzere ikiye ayrılır. Lafzî âmillerin bir kısmı <b>semâî</b> (Araplardan duyulduğu gibi ezberlenir), bir kısmı <b>kıyâsî</b>dir (bir kurala bağlıdır).',
  'Bu ders notunda Avâmil geleneğinin (Cürcânî’nin <i>Mie Âmil</i>’i ve İmâm Birgivî’nin <i>Avâmil-i cedîd</i>’i) tasnifi esas alınmıştır; sayılar nüshalara göre küçük farklar gösterir.'],
  [('فِي الدَّارِ','âmil: فِي — ma‘mûl: الدَّارِ (mecrûr)'),('لَمْ يَذْهَبْ','âmil: لَمْ — ma‘mûl: يَذْهَبْ (meczûm)')]),
 ('حروف الجر','Yalnız ismi cerreden harfler (hurûf-ı cârra)',[
  'Bu harfler yalnızca isme girer ve onu cerreder: <span lang="ar">بِ، مِنْ، إِلَى، عَنْ، عَلَى، فِي، كَـ، لِـ، رُبَّ، حَتَّى، مُنْذُ، مُذْ، خَلَا، عَدَا، حَاشَا</span> ve yemin harfleri <span lang="ar">وَ، تَـ</span>.',
  'Mânâlarından bazıları: <span lang="ar">مِنْ</span> başlangıç, <span lang="ar">إِلَى</span> son nokta, <span lang="ar">عَنْ</span> uzaklaşma, <span lang="ar">عَلَى</span> üstünlük, <span lang="ar">فِي</span> zarfiyet, <span lang="ar">بِـ</span> ilsâk ve istiâne (vasıta), <span lang="ar">لِـ</span> mülk ve ihtisas, <span lang="ar">كَـ</span> teşbîh.'],
  [('بِسْمِ اللَّهِ','بِ — istiâne/teberrük'),('مِنَ الْمَسْجِدِ الْحَرَامِ إِلَى الْمَسْجِدِ الْأَقْصَى','مِنْ başlangıç, إِلَى son'),('وَاللَّهِ','yemin vâvı')]),
 ('الحروف المشبهة بالفعل','İsmi nasb, haberi ref‘ eden harfler',[
  '<span lang="ar">إِنَّ، أَنَّ، كَأَنَّ، لَكِنَّ، لَيْتَ، لَعَلَّ</span>: isim cümlesinin başına girer, mübtedâyı isimleri olarak nasbeder, haberi ref‘ eder. Fiile benzedikleri (fethalı bina, üç ve fazla harf, mânâ) için <b>hurûf-ı müşebbehe bi’l-fiil</b> denir.',
  'Mânâları: إِنَّ ve أَنَّ tekîd, كَأَنَّ teşbîh, لَكِنَّ istidrâk, لَيْتَ temennî, لَعَلَّ tereccî. Başlarına kâffe <span lang="ar">مَا</span> gelince amelden düşerler: <span lang="ar">إِنَّمَا اللَّهُ إِلَهٌ وَاحِدٌ</span>.',
  'Lâ-yı nâfiye li’l-cins (<span lang="ar">لَا إِلَهَ إِلَّا اللَّهُ</span>) de bunlar gibi amel eder.'],
  [('إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ','اللَّهَ: ism-i inne (mansûb), غَفُورٌ: haber (merfû)'),('لَعَلَّكُمْ تَتَّقُونَ','كُمْ: ismi (mahallen mansûb), cümle: haber')]),
 ('ما ولا المشبهتان بليس','Leyse’ye benzeyen mâ ve lâ',[
  'Hicaz lehçesinde nâfiye <span lang="ar">مَا</span> ve (şartlarıyla) <span lang="ar">لَا</span>, leyse gibi ismi ref‘, haberi nasbeder: <span lang="ar">مَا هَذَا بَشَرًا</span> (Yûsuf 31). Haberin önüne <span lang="ar">إِلَّا</span> gelirse veya haber öne geçerse amel bâtıl olur: <span lang="ar">وَمَا مُحَمَّدٌ إِلَّا رَسُولٌ</span>.'],
  [('مَا هَذَا بَشَرًا','هَذَا: ismi (mahallen merfû), بَشَرًا: haberi (mansûb)')]),
 ('نواصب المضارع وجوازمه','Muzâriyi nasbeden ve cezmeden harfler',[
  '<b>Nevâsıb</b>: <span lang="ar">أَنْ، لَنْ، كَيْ، إِذَنْ</span>. Bunlar muzâriyi nasbeder: <span lang="ar">لَنْ تَنَالُوا الْبِرَّ</span>. Ayrıca أَنْ, lâm-ı ta‘lîl, lâm-ı cuhûd, حَتَّى, أَوْ, sebebiyye fâsı ve maiyye vâvından sonra gizli olarak amel eder.',
  '<b>Tek fiili cezmedenler</b>: <span lang="ar">لَمْ، لَمَّا</span>, emir lâmı (<span lang="ar">لِيُنْفِقْ</span>), nehiy lâsı (<span lang="ar">لَا تَحْزَنْ</span>).',
  '<b>İki fiili cezmedenler (şart edatları)</b>: harf olan <span lang="ar">إِنْ</span> ve isim olanlar <span lang="ar">مَنْ، مَا، مَهْمَا، أَيٌّ، مَتَى، أَيْنَ، أَنَّى، حَيْثُمَا، إِذْمَا</span>: <span lang="ar">إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ</span>.'],
  [('لَنْ تَنَالُوا الْبِرَّ','لَنْ: nâsıb — nûnun hazfı'),('لَمْ يَلِدْ وَلَمْ يُولَدْ','لَمْ: câzim — sükûn'),('مَنْ يَعْمَلْ سُوءًا يُجْزَ بِهِ','مَنْ: iki fiili cezmeder')]),
 ('حروف النداء والاستثناء','Nidâ harfleri ve istisnâ',[
  'Nidâ harfleri (<span lang="ar">يَا، أَيَا، هَيَا، أَيْ، أَ</span>) münâdâyı mahallen veya lafzen nasbeder: muzâf münâdâ mansûb (<span lang="ar">يَا عَبْدَ اللَّهِ</span>), müfred alem damme üzere mebnî (<span lang="ar">يَا مُوسَى، يَا نُوحُ</span>).',
  'Tam ve müsbet sözde <span lang="ar">إِلَّا</span> müstesnâyı nasbeder: <span lang="ar">فَسَجَدُوا إِلَّا إِبْلِيسَ</span>.'],
  [('يَا أَيُّهَا النَّاسُ','أَيُّ: münâdâ (mebnî)'),('رَبَّنَا آتِنَا','رَبَّ: muzâf münâdâ, nidâ harfi hazfedilmiş')]),
 ('الأفعال العاملة','Âmil fiiller',[
  '<b>Bütün fiiller</b> fâili ref‘ eder; müteaddî fiiller ayrıca mef‘ûlü nasbeder. Bu, kıyâsî bir ameldir.',
  '<b>Ef‘âl-i nâkısa</b> (<span lang="ar">كَانَ، صَارَ، أَصْبَحَ، أَمْسَى، أَضْحَى، ظَلَّ، بَاتَ، لَيْسَ، مَا زَالَ، مَا بَرِحَ، مَا فَتِئَ، مَا انْفَكَّ، مَا دَامَ</span>): ismi ref‘, haberi nasbeder: <span lang="ar">وَكَانَ اللَّهُ غَفُورًا رَحِيمًا</span>.',
  '<b>Ef‘âl-i mukâraba</b> (<span lang="ar">كَادَ، أَوْشَكَ، كَرَبَ</span>), reca (<span lang="ar">عَسَى</span>) ve şürû‘ (<span lang="ar">طَفِقَ، جَعَلَ، أَخَذَ</span>): ismi ref‘ eder, haberi muzâri cümlesidir: <span lang="ar">يَكَادُ الْبَرْقُ يَخْطَفُ أَبْصَارَهُمْ</span>.',
  '<b>Ef‘âl-i medh ve zemm</b> (<span lang="ar">نِعْمَ، بِئْسَ، سَاءَ، حَبَّذَا</span>): fâili ref‘ eder: <span lang="ar">نِعْمَ الْعَبْدُ</span>. <b>Ef‘âl-i kulûb</b> (<span lang="ar">ظَنَّ، حَسِبَ، خَالَ، زَعَمَ، عَلِمَ، رَأَى، وَجَدَ</span>): iki mef‘ûlü nasbeder: <span lang="ar">وَإِنَّا لَنَظُنُّكَ مِنَ الْكَاذِبِينَ</span>.'],
  [('كَانَ اللَّهُ عَلِيمًا','اللَّهُ: ism-i kâne, عَلِيمًا: haberi'),('عَسَى رَبُّكُمْ أَنْ يَرْحَمَكُمْ','عَسَى: reca fiili'),('بِئْسَ الْمَصِيرُ','الْمَصِيرُ: bi’se’nin fâili')]),
 ('الأسماء العاملة','Âmil isimler',[
  '<b>Esmâ-i şart</b> iki fiili cezmeder (bkz. önceki bâb). <b>Esmâ-i ef‘âl</b> (fiil isimleri) fiil gibi amel eder: <span lang="ar">هَيْهَاتَ</span> (uzaklaştı), <span lang="ar">صَهْ</span> (sus), <span lang="ar">رُوَيْدَ زَيْدًا</span> (Zeyd’e mühlet ver), <span lang="ar">عَلَيْكُمْ أَنْفُسَكُمْ</span> (kendinize bakın).',
  '<b>Fiilden türeyen isimler</b> fiilleri gibi amel eder: ism-i fâil (<span lang="ar">بَاسِطٌ ذِرَاعَيْهِ</span>), ism-i mef‘ûl (nâib-i fâili ref‘ eder), sıfat-ı müşebbehe (<span lang="ar">حَسَنٌ وَجْهُهُ</span>), masdar (<span lang="ar">وَلَوْلَا دَفْعُ اللَّهِ النَّاسَ</span>) ve ism-i tafdîl.',
  '<b>Muzâf</b> muzâf ileyhi cerreder (<span lang="ar">كِتَابُ اللَّهِ</span>). <b>Mübhem isimler</b> (sayılar, ölçüler, كَمْ) temyîzi nasbeder: <span lang="ar">أَحَدَ عَشَرَ كَوْكَبًا</span>, <span lang="ar">كَمْ كِتَابًا قَرَأْتَ؟</span>'],
  [('رَبِّ الْعَالَمِينَ','muzâf: رَبِّ — muzâf ileyh: الْعَالَمِينَ (mecrûr)'),('أَرْبَعِينَ لَيْلَةً','sayı temyîzi nasbeder (Bakara 51)')]),
 ('العوامل المعنوية','Ma‘nevî âmiller',[
  'Söylenmeyen, anlamdan doğan iki âmil vardır:',
  '<b>1. İbtidâ</b>: mübtedâyı ref‘ eden âmil, ismin lafzî âmillerden sıyrılarak cümlenin başında bulunmasıdır: <span lang="ar">اللَّهُ الصَّمَدُ</span> — <span lang="ar">اللَّهُ</span> ibtidâ ile merfûdur.',
  '<b>2. Muzârinin ref‘i</b>: muzâri fiili ref‘ eden âmil, nâsıb ve câzimden sıyrılmış olmasıdır (Basra görüşü: isim yerinde bulunması): <span lang="ar">يَعْلَمُ مَا فِي السَّمَاوَاتِ</span>.',
  'Avâmil’i bitiren öğrenci her kelimeye “bunu ne ref‘ etti/nasbetti/cerretti?” diye sorar. Kur’an i‘râbı modülündeki <b>Avâmil notları</b> ve <b>İ‘râb oyunu</b> bu soruyu sordurmak için hazırlandı.'],
  [('اللَّهُ الصَّمَدُ','mübtedâ: ibtidâ ile merfû'),('يَعْلَمُ','muzâri: nâsıb ve câzimden tecerrüd ile merfû')]),
],[
 (0,'Kelimenin sonundaki i‘râbı meydana getiren şeye ne denir?',['Âmil','Ma‘mûl','Alâmet','Tâbi'],'Âmil etkiler, ma‘mûl etkilenir, alâmet görünen harekedir.'),
 (0,'Âmiller ilk olarak hangi iki kısma ayrılır?',['Lafzî ve ma‘nevî','İsim ve fiil','Harf ve fiil','Mu‘reb ve mebnî'],'Lafzî: söylenen; ma‘nevî: söylenmeyen.'),
 (1,'Aşağıdakilerden hangisi yalnız ismi cerreden harflerdendir?',['عَنْ','لَنْ','لَمْ','إِنَّ'],'عَنْ cer harfidir.'),
 (2,'إِنَّ ve kardeşlerinin ameli nedir?',['İsmi nasb, haberi ref‘','İsmi ref‘, haberi nasb','İkisini de nasb','Muzâriyi nasb'],'Hurûf-ı müşebbehe bi’l-fiil.'),
 (2,'إِنَّمَا ifadesinde إِنَّ niçin amel etmez?',['Kâffe mâ bitiştiği için','Haberi öne geçtiği için','Fiile girdiği için','Nekreye girdiği için'],'مَا kâffe, amelden alıkoyar.'),
 (3,'مَا هَذَا بَشَرًا cümlesinde بَشَرًا niçin mansûbdur?',['Leyse gibi amel eden mânın haberi olduğu için','Hâl olduğu için','Mef‘ûlün bih olduğu için','Temyîz olduğu için'],'Hicaz lehçesinde mâ leyse gibi amel eder.'),
 (4,'Hangisi muzâriyi NASBEDER?',['كَيْ','لَمَّا','لَا (nehiy)','مَهْمَا'],'Nevâsıb: أن، لن، كي، إذن.'),
 (4,'إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ cümlesinde يَنْصُرْكُمْ neden meczûmdur?',['Şartın cevabı olduğu için','Nehiy olduğu için','لَمْ geldiği için','Emir olduğu için'],'إِنْ iki fiili cezmeder: şart ve cevap.'),
 (5,'يَا عَبْدَ اللَّهِ münâdâsı niçin mansûbdur?',['Muzâf olduğu için','Müfred alem olduğu için','Nekre-i maksûde olduğu için','Mebnî olduğu için'],'Muzâf münâdâ mansûbdur.'),
 (6,'كَادَ fiilinin haberi genellikle nedir?',['Muzâri cümlesi','Mansûb müfred isim','Câr-mecrûr','Mâzî fiil'],'يَكَادُ الْبَرْقُ يَخْطَفُ أَبْصَارَهُمْ.'),
 (6,'Ef‘âl-i kulûb kaç mef‘ûl nasbeder?',['İki','Bir','Üç','Hiç'],'ظننت زيدًا قائمًا.'),
 (7,'صَهْ kelimesi nedir?',['İsm-i fiil (sus)','Harf','Mâzî fiil','Masdar'],'Esmâ-i ef‘âl fiil gibi amel eder.'),
 (7,'Muzâf, muzâf ileyhe ne yapar?',['Cerreder','Nasbeder','Ref‘ eder','Cezmeder'],'كِتَابُ اللَّهِ.'),
 (8,'Mübtedâyı ref‘ eden âmil nedir?',['İbtidâ (ma‘nevî âmil)','Haber','Fiil','إِنَّ'],'Lafzî âmillerden sıyrılma: ibtidâ.'),
])
