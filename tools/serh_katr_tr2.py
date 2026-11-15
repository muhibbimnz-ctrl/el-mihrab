import json
TR={
'31.0':'Mübtedâ ve haberin hükmünü değiştirenler (nevâsih) üç çeşittir. Birincisi: كان، أمسى، أصبح، أضحى، ظلّ، بات، صار، ليس، ما زال، ما فتئ، ما انفكّ، ما برح، ما دام. Bunlar mübtedâyı kendi isimleri olarak ref‘, haberi kendi haberleri olarak nasbeder: وكان ربُّك قديرًا.',
'32.1':'Haber, fiil ile ismi arasına girebilir: فليس سواءً عالمٌ وجهول.',
'32.3':'Haber (fiilin) önüne de geçebilir; ancak دام ve ليس’in haberi geçemez.',
'32.5':'İlk beşi (كان، أمسى، أصبح، أضحى، ظلّ) “sâra” (oldu) mânâsına gelmekle hususîdir.',
'32.8':'Kâne, araya zâid olarak girebilmekle hususîdir: ما كان أحسنَ زيدًا.',
'32.10':'Meczûm muzârisinin nûnu, ardından sâkin bir harf veya muttasıl nasb zamiri gelmezse vasl hâlinde hazfedilebilir (لم يكُ).',
'32.12':'Kâne tek başına hazfedilip yerine mâ getirilebilir (أمّا أنت ذا نفرٍ); ismiyle birlikte de hazfedilebilir: إنْ خيرًا فخيرٌ، التمسْ ولو خاتمًا من حديد.',
'33.0':'Hicazlılara göre nâfiye mâ, leyse gibi amel eder; şartları: isim öne geçmiş olmalı, mâdan sonra zâid in gelmemeli, haberin ma‘mûlü (zarf ve câr-mecrûr hariç) öne geçmemeli ve haber illâ ile gelmemeli: ما هذا بشرًا.',
'34.0':'Nâfiye lâ da şiirde, iki ma‘mûlü nekre olmak şartıyla leyse gibi amel eder: “Teselli bul; yeryüzünde hiçbir şey bâkî değildir ve Allah’ın takdirinden koruyacak hiçbir sığınak yoktur.”',
'35.0':'Lâte de leyse gibi amel eder, ancak yalnız “hîn” (vakit) kelimelerinde; iki cüzü birlikte zikredilmez, çoğunlukla merfûu hazfedilir: ولاتَ حينَ مناصٍ.',
'36.0':'İkinci çeşit: إنّ ve أنّ tekîd, لكنّ istidrâk, كأنّ teşbîh veya zan, ليت temennî, لعلّ tereccî, işfâk veya ta‘lîl içindir. Bunlar mübtedâyı kendi isimleri olarak nasb, haberi kendi haberleri olarak ref‘ eder.',
'36.2':'Ancak başlarına harf olan mâ bitişirse amel etmezler: إنّما اللهُ إلهٌ واحدٌ; leyte bundan müstesnâdır, onda iki vecih câizdir.',
'36.5':'Muhaffef (şeddesiz) kesreli in de böyledir (iki vecih câizdir).',
'36.7':'Muhaffef lâkin ise amel etmez.',
'36.9':'Muhaffef en amel eder; zarûret dışında ismi olan zamîr-i şe’nin hazfı ve haberinin cümle olması vâcibdir; haber, duâ olmayan mutasarrıf bir fiille başlarsa قد, tenfîs (سـ/سوف), nefy veya لو ile ayrılır.',
'36.12':'Muhaffef keenne de amel eder; ismi az zikredilir; fiil ondan لم veya قد ile ayrılır.',
'36.15':'Bunların haberi, zarf veya mecrûr olmadıkça isimlerinin önüne geçemez: إنّ في ذلك لعبرةً، إنّ لدينا أنكالًا. (Paragrafın devamı müellifin şerhidir.)',
'36.16':'İnne şu yerlerde kesreli okunur: ibtidâda (إنّا أنزلناه في ليلة القدر), kasemden sonra (حم والكتاب المبين إنّا أنزلناه), kavlden sonra (قال إنّي عبد الله) ve haberinde lâm bulunduğunda (والله يعلم إنّك لرسوله).',
'36.18':'Kesreli inne’nin sona kalan haberine, ismine, araya giren haber ma‘mûlüne veya fasl zamirine lâm girebilir; muhaffef in amelsiz bırakılır ve mânâ belli olmazsa lâm vâcibdir.',
'37.0':'Lâ-yı nâfiye li’l-cins de inne gibi amel eder; ancak ameli kendisine bitişik nekrelere mahsustur: لا صاحبَ علمٍ ممقوتٌ، لا عشرين درهمًا عندي. İsmi muzâf veya muzâfa benzer değilse لا رجلَ ve لا رجالَ’de fetha üzere, لا مسلماتِ’te fetha veya kesre üzere, لا رجلَيْنِ ve لا مسلمِينَ’de yâ üzere mebnî olur.',
'37.3':'لا حولَ ولا قوةَ gibi bir ifadede birinciyi fethalı okursun; ikincide fetha, nasb ve ref‘ câizdir. لا رجلَ ظريفٌ’teki sıfat da böyledir; birinci merfû okunursa (ikincide) nasb imkânsızdır. Lâ tekrarlanmazsa, sıfat ayrılırsa veya müfred değilse fetha câiz değildir.',
'38.0':'Üçüncü çeşit: kalbî fiiller olan ظنّ، رأى، حسب، درى، خال، زعم، وجد، علم. Bunlar mübtedâ ile haberi iki mef‘ûl olarak nasbeder: رأيتُ اللهَ أكبرَ كلِّ شيء. Sona geçince ilgâ (amelsiz bırakma) tercih edilir (القوم في أثري ظننتُ); araya girince ilgâ ile amel eşittir. Başlarına nâfiye mâ, lâ, in, ibtidâ lâmı, kasem veya istifhâm gelirse lafızda amelleri vâciben bâtıl olur; buna ta‘lîk denir: لنعلمَ أيُّ الحزبين أحصى.',
'39.0':'Fâil merfûdur: قام زيدٌ، مات عمرٌو. Âmili ondan sonra gelmez; fiile tesniye ve cem‘ alâmeti eklenmez: “قام رجلٌ” denildiği gibi “قام رجلان، رجالٌ، نساءٌ” denir; “يتعاقبون فيكم ملائكة” ve “أوَمُخرجيَّ هم” şâzdır. Fâil müennes ise fiile te’nîs alâmeti gelir: قامت هندٌ، طلعت الشمسُ. Zâhir mecâzî müenneste (قد جاءتكم موعظة / قد جاءكم بيّنة), araya fasıl giren hakîkî müenneste (حضر القاضيَ امرأةٌ), ni‘me–bi’se bâbındaki bitişikte (نعمت المرأةُ هندٌ) ve cemide (قالت الأعراب) iki vecih câizdir; iki sâlim cem‘ ise tekilleri gibidir: قام الزيدون، قامت الهندات. Nesirde “ما قامت إلا هندٌ” denmez, çünkü fâil hazfedilmiş müzekkerdir. Fâil (hazfedilmez; yalnız) أو إطعامٌ في يوم ذي مسغبة يتيمًا، قُضي الأمرُ، أسمِعْ بهم وأبصِرْ gibi yerlerde hazfedilir.',
'39.5':'Asıl olan, fâilin âmilinden hemen sonra gelmesidir. Bazen câizen sonra gelir (ولقد جاء آلَ فرعونَ النذرُ), bazen vâciben (وإذ ابتلى إبراهيمَ ربُّه، ضربني زيدٌ). Bazen mef‘ûlün sonra gelmesi vâcib olur: ضربتُ زيدًا، ما أحسنَ زيدًا، ضرب موسى عيسى; أرضعت الصغرى الكبرى ise böyle değildir. Mef‘ûl âmilinin önüne câizen (فريقًا هدى) veya vâciben (أيًّا ما تدعوا) geçebilir. Fiil ni‘me veya bi’se olursa fâil ya cins el-’iyle ma‘rifedir (نعم العبدُ), ya onu taşıyana muzâftır (ولنعم دارُ المتقين), ya da mahsûsa uygun bir temyîzle açıklanan gizli zamirdir (بئس للظالمين بدلًا).',
'40.0':'Nâib-i fâil: Fâil hazfedilir ve bütün hükümlerinde mef‘ûlün bih onun yerini tutar; yoksa muhtas ve mutasarrıf zarf, mecrûr veya masdar yerini tutar. Fiilin ilk harfi her hâlde dammelenir; تُعُلِّمَ’de ikinci, اُنطُلِقَ’de üçüncü harf de ona katılır. Sondan bir önceki harf muzâride fethalı, mâzîde kesreli olur. قال ve باع gibilerde halis kesre (قِيل), damme işmâmlı kesre ve halis damme câizdir.',
'41.0':'İştiğâl: “زيدًا ضربتُه”, “ضربتُ أخاه” veya “مررتُ به” gibi yerlerde Zeyd mübtedâ olarak merfû olabilir, o zaman sonraki cümle haberdir; veya hazfı vâcib olan ضربتُ، أهنتُ، جاوزتُ takdiriyle mansûb olabilir, o zaman sonraki cümlenin i‘râbtan mahalli yoktur. Talep bulunduğunda nasb tercih edilir (زيدًا اضربْه; والسارقُ والسارقةُ فاقطعوا… ayeti te’vil edilir), tenâsüp için (والأنعامَ خلقها لكم) ve fiil ağır bastığında (أبشرًا منا واحدًا نتّبعه، ما زيدًا رأيتُه). Şart ve tahdîd edatlarından sonra nasb vâcibdir (إنْ زيدًا لقيتَه فأكرمْه، هلّا زيدًا أكرمتَه). Müfâcee إذا’sından sonra ref‘ vâcibdir (خرجتُ فإذا زيدٌ يضربه عمرٌو). Denk durumlarda ikisi eşittir (زيدٌ قام أبوه وعمرٌو أكرمتُه). وكلُّ شيءٍ فعلوه في الزبر ve أزيدٌ ذُهب به bu bâbdan değildir.',
'42.0':'Tenâzu‘: ضربني وضربتُ زيدًا gibi yerlerde birinci âmili amel ettirmek câizdir — Kûfeliler bunu tercih eder, o zaman ikinciye ihtiyaç duyduğu her şey zamir olarak verilir; ikinciyi amel ettirmek de câizdir — Basralılar bunu tercih eder, o zaman birinciye yalnız merfûu zamir olarak verilir: جفوني ولم أجفُ الأخلّاءَ. “كفاني ولم أطلب قليلٌ من المال” ise mânâ bozulacağı için bu bâbdan değildir.',
'43.0':'Mef‘ûl mansûbdur.',
'43.2':'Beş tanedir.',
'44.0':'Mef‘ûlün bih: fâilin fiilinin üzerine vâki olduğu isimdir: ضربتُ زيدًا.',
'45.0':'Münâdâ da ondandır.',
'45.2':'Münâdâ ancak şu hâllerde mansûb olur: muzâf ise (يا عبدَ الله), muzâfa benzer ise (يا حسنًا وجهُه، يا طالعًا جبلًا، يا رفيقًا بالعباد) veya nekre-i gayr-i maksûde ise — âmânın “يا رجلًا خذْ بيدي” sözü gibi.',
'45.4':'Müfred ma‘rife münâdâ, merfû olduğu alâmet üzere mebnî olur: يا زيدُ، يا زيدان، يا زيدون، ve belli biri için يا رجلُ.',
'45.6':'Fasıl: “يا غلام” (mütekellim yâsına muzâf) üç harekeyle, fethalı veya sâkin yâ ile ve elif ile söylenir.',
'45.9':'يا أبتِ، يا أمّتِ، يا ابنَ أمَّ/أمِّ، يا ابنَ عمَّ/عمِّ fetha ve kesre ile söylenir; ilk ikisine elif veya yâ eklemek çirkin, son ikisine eklemek zayıftır.',
'45.12':'Fasıl: Mebnî münâdânın na‘tı, tekîdi, atf-ı beyânı ve el-’li nesakı müfred ise veya el-’li olarak muzâf ise lafzına veya mahalline göre; el-’siz muzâf ise mahalline göre i‘râb alır. Eyyü’nün na‘tı lafzına uyar. El-’siz bedel ve nesak ise bağımsız münâdâ gibidir.',
'46.2':'يا زيدُ زيدَ اليعملات gibi bir ifadede ikisini de fethalı okuyabilir veya birinciyi dammeli okuyabilirsin.',
'47.0':'Fasıl: Ma‘rife münâdâda terhîm câizdir; terhîm, hafifletmek için sonunu hazfetmektir. Tâ’lı olanlarda mutlak olarak (يا طلحَ، يا ثُبَ); diğerlerinde ise mebnî, alem ve üç harften uzun olmak şartıyla: يا جعفُ / يا جعفَ.',
'47.2':'سلمان، منصور، مسكين gibilerden iki harf, معدي كرب gibilerden ikinci kelime hazfedilir.',
'47.5':'Fasıl: İstiğâse eden “يا لَلّهِ لِلمسلمين” der; müstegâsün bihin lâmı fethalıdır; ancak yâ tekrarlanmayan ma‘tûfun lâmı böyle değildir. يا زيدا لعمرٍو da denir.',
'49.0':'Nüdbe yapan “وا زيدا، وا أميرَ المؤمنينا، وا رأسا” der; vakfda hâ eklemen câizdir (وا زيداه).',
'50.0':'Mef‘ûl-i mutlak: lafzından (ضربتُ ضربًا) veya mânâsından (قعدتُ جلوسًا) bir âmilin üzerine yöneldiği fazla masdardır. Başka şeyler onun yerini tutabilir: ضربتُه سوطًا، فاجلدوهم ثمانين جلدةً، فلا تميلوا كلَّ الميل، ولو تقوّل علينا بعضَ الأقاويل. وكلا منها رغدًا bundan değildir.',
'51.0':'Mef‘ûlün leh: vakit ve fâilde kendisine ortak olan bir fiilin sebebini bildiren masdardır: قمتُ إجلالًا لك. Bir şartı eksikse ta‘lîl harfiyle mecrûr olur: خلق لكم، “Seni anınca beni bir titreme alır”, “Uyumak için elbiselerini çıkarmışken geldim.”',
'52.0':'Mef‘ûlün fîh: âmilin “fî” mânâsıyla yöneldiği zaman ismi (صمتُ يومَ الخميس، حينًا، أسبوعًا) veya mübhem mekân ismidir: altı yön (önü, üstü, sağı ve zıtları), عند ve لدى gibileri, ölçüler (fersah gibi) ve âmilinin masdarından yapılan (قعدتُ مقعدَ زيدٍ).',
'53.0':'Mef‘ûlün maah: beraberliği açıkça bildirmek için getirilen ve kendisinden önce bir fiil veya fiilin harflerini ve mânâsını taşıyan bir kelime bulunan vâvdan sonra gelen fazla isimdir: سرتُ والنيلَ، أنا سائرٌ والنيلَ.',
'54.1':'Bazen nasb vâcib olur: لا تنهَ عن القبيح وإتيانَه; en doğru görüşe göre قمتُ وزيدًا ve مررتُ بك وزيدًا da böyledir. كن أنت وزيدًا كالأخ’de nasb tercih edilir; قام زيدٌ وعمرٌو’da (nasb) zayıftır.',
'55.0':'Hâl: “nasıl?” sorusunun cevabında yer alan fazla vasıftır: ضربتُ اللصَّ مكتوفًا.',
'55.2':'Şartı nekre olmasıdır.',
'55.4':'Sâhibinin şartı ma‘rife olması, tahsis veya umum ifade etmesi ya da (hâlden) sonra gelmesidir: خشّعًا أبصارُهم يخرجون، في أربعة أيامٍ سواءً للسائلين، وما أهلكنا من قريةٍ إلا لها منذرون، لميّةَ موحشًا طللُ.',
'56.2':'Temyîz en çok ölçülerden sonra (جريبٌ نخلًا، صاعٌ تمرًا، منوانِ عسلًا) ve sayılardan sonra gelir (أحدَ عشرَ كوكبًا، تسعٌ وتسعون نعجةً); istifhâmî kem’in temyîzi de böyledir (كم عبدًا ملكتَ؟). Haberî kem’in temyîzi ise mecrûrdur: yüz ve üstünün temyîzi gibi müfred veya on ve altının temyîzi gibi cemi olur. Harfle mecrûr istifhâmî kem’in temyîzinde cer ve nasb câizdir. Temyîz, nisbeti açıklayıcı olabilir: muhavvel (اشتعل الرأسُ شيبًا، وفجّرنا الأرضَ عيونًا، أنا أكثرُ منك مالًا) veya muhavvel olmayan (امتلأ الإناءُ ماءً). Hâl ve temyîz bazen tekîd için gelir: ولا تعثَوا في الأرض مفسدين; “dinlerin en hayırlısı din olarak” ve “bi’se’l-fahlu fahluhum fahlen” da böyledir — Sîbeveyh buna muhaliftir.',
'58.0':'Müstesnâ: tam ve müsbet sözde إلّا ile müstesnâ mansûbdur: فشربوا منه إلّا قليلًا منهم. Müsbet olmazsa muttasılda bedel tercih edilir (ما فعلوه إلّا قليلٌ منهم); munkatı‘da Temîmoğullarına göre nasb tercih edilir, Hicazlılara göre vâcibdir (ما لهم به من علم إلّا اتّباعَ الظنّ). Müstesnâ öne geçerse ikisinde de nasb olur: “Ahmed’in âlinden başka taraftarım yok…” Söz tam değilse (müstesnâ minh zikredilmemişse) âmillere göre i‘râb alır: وما أمرُنا إلّا واحدةٌ; buna müferrağ denir.',
'59.0':'غير ve سوى ile de istisnâ yapılır; bunlar sonraki ismi cerreder, kendileri ise إلّا’dan sonraki ismin i‘râbını alır. خلا، عدا ve حاشا ile istisnâ yapılır; bunlar nasb veya cer eder. ما خلا، ما عدا، ليس ve لا يكون ise yalnız nasbeder.',
}
d=json.load(open('data/kitap/serhkatr.json'))
n=0
for i,b in enumerate(d['bolumler']):
    if 'tr' not in b: b['tr']=['']*len(b['p'])
    for j in range(len(b['p'])):
        k=f'{i}.{j}'
        if k in TR: b['tr'][j]=TR[k]; n+=1
json.dump(d,open('data/kitap/serhkatr.json','w'),ensure_ascii=False,separators=(',',':'))
print(n)
