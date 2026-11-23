# C2 seviyesinde yeni akademik metinler → data/modern/modern.json (metinler). Tekrar çalıştırılırsa aynı id'yi günceller.
# Sonra: python3 tools/arapca_metin_ekle.py  (C1/C2 metinler C1–C2 programına, c2kat kategorisine girer)
import json, os
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'data', 'modern', 'modern.json')
X = []
def m(id, alan, c2kat, baslik, ar_baslik, ar, tr, sozluk, sorular):
    assert len(ar) == len(tr)
    X.append({'id': id, 'alan': alan, 'c2kat': c2kat, 'baslik': baslik, 'ar_baslik': ar_baslik, 'konu': baslik, 'seviye': 'C2',
              'ar': ar, 'tr': tr, 'sozluk': [list(s) for s in sozluk],
              'sorular': [{'s': s, 'k': k, 'd': d, 'a': a} for s, k, d, a in sorular]})

m('icaz-nazariyeleri', 'edebiyat', 0, 'İ‘câzü’l-Kur’ân nazariyeleri', 'نظريات إعجاز القرآن بين الصرفة والنظم',
['لم يكن سؤال الإعجاز سؤالا لاهوتيا خالصا، بل كان في جوهره سؤالا نقديا عن طبيعة البيان: ما الذي يجعل نصا ما متعاليا على قدرة البلغاء، مع أنه مؤلف من الحروف نفسها التي ينظمون بها كلامهم؟',
 'وأول جواب لافت جاء من المعتزلي إبراهيم النظام، الذي ذهب إلى القول بالصرفة، أي أن الله صرف العرب عن معارضة القرآن وسلبهم القدرة عليها، ولولا ذلك لاستطاعوا أن يأتوا بمثله. وقد بدا هذا القول لكثير من العلماء انتقاصا من النص نفسه، إذ يجعل الإعجاز في المنع لا في الممنوع منه.',
 'ثم جاء الخطابي والرماني والباقلاني فنقلوا مركز الثقل إلى النص ذاته، فتحدثوا عن حسن التأليف والتئام الكلم وصحة المعاني، وإن ظلت عباراتهم أقرب إلى الوصف منها إلى التفسير. فالباقلاني مثلا يكثر من الموازنة بين القرآن وشعر امرئ القيس ليبين التفاوت، ولكنه لا يقدم معيارا يمكن اطراده.',
 'وكان عبد القاهر الجرجاني هو من حول الملاحظة الذوقية إلى نظرية متماسكة، حين رد الفصاحة إلى النظم، والنظم إلى توخي معاني النحو فيما بين الكلم. فالمزية عنده ليست في اللفظة المفردة ولا في المعنى المجرد، وإنما في العلاقات التي تنشأ بين الكلمات بحسب مواقعها من التقديم والتأخير والذكر والحذف والتعريف والتنكير.',
 'وقد ظل هذا الإطار مهيمنا قرونا، حتى ظهر في العصر الحديث ما يسمى الإعجاز العلمي، الذي يبحث في الآيات عن إشارات إلى حقائق الكون. ويرى منتقدو هذا الاتجاه أنه يعرض النص لتقلبات النظريات العلمية، ويخرج بالإعجاز من حقل البيان الذي تحدى به القرآن العرب ابتداء.',
 'ومهما يكن من أمر، فإن الجدل حول الإعجاز كان من أخصب ما أنتجته الثقافة العربية، إذ تولدت منه علوم البلاغة الثلاثة، وتشكلت في ظله أدق المفاهيم النقدية التي لا يزال الدرس اللساني المعاصر يعود إليها.'],
['İ‘câz sorusu salt teolojik bir soru değildi; özünde beyânın mahiyetine dair eleştirel bir soruydu: Bir metni, belîğlerin sözlerini dizdikleri harflerin aynısından oluştuğu hâlde, onların gücünü aşan bir mertebeye ne çıkarır?',
 'Dikkat çekici ilk cevap Mu‘tezilî İbrâhim en-Nazzâm’dan geldi; o, sarfe görüşünü benimsedi: Allah Arapları Kur’an’a karşılık vermekten çevirmiş ve bu gücü onlardan almıştır; öyle olmasaydı benzerini getirebilirlerdi. Bu görüş birçok âlime metnin kendisini küçümsemek gibi göründü; çünkü i‘câzı engellenen şeyde değil, engellemede görüyordu.',
 'Sonra Hattâbî, Rummânî ve Bâkıllânî ağırlık merkezini metnin kendisine taşıdılar; telifin güzelliğinden, kelimelerin uyumundan ve manaların sıhhatinden söz ettiler; ama ifadeleri açıklamadan çok tasvire yakın kaldı. Mesela Bâkıllânî aradaki farkı göstermek için Kur’an ile İmruülkays’ın şiirini sık sık karşılaştırır; fakat genelleştirilebilecek bir ölçüt ortaya koymaz.',
 'Zevkî gözlemi tutarlı bir teoriye dönüştüren Abdülkâhir el-Cürcânî oldu: Fesahati nazma, nazmı da kelimeler arasında nahiv manalarını gözetmeye bağladı. Ona göre meziyet ne tek kelimede ne de soyut manadadır; takdim-tehir, zikir-hazf, tarif-tenkir gibi konumlarına göre kelimeler arasında doğan ilişkilerdedir.',
 'Bu çerçeve yüzyıllarca hâkim kaldı; ta ki modern çağda âyetlerde kâinatın hakikatlerine işaretler arayan “ilmî i‘câz” ortaya çıkana dek. Bu yaklaşımı eleştirenler, onun metni bilimsel teorilerin dalgalanmalarına maruz bıraktığını ve i‘câzı, Kur’an’ın Arapları başlangıçta meydan okuduğu beyân alanının dışına çıkardığını düşünür.',
 'Her ne olursa olsun, i‘câz tartışması Arap kültürünün ürettiği en verimli tartışmalardan biri oldu; çünkü üç belâgat ilmi ondan doğdu ve çağdaş dilbilimin hâlâ başvurduğu en ince eleştirel kavramlar onun gölgesinde şekillendi.'],
[('الإعجاز', 'i‘câz; benzerini getirmekten aciz bırakma'), ('متعاليا على', '…i aşan'), ('الصرفة', 'sarfe (Allah’ın muarazadan alıkoyması)'), ('معارضة', 'muâraza, karşılık verme'), ('انتقاصا من', '…i küçümseme'),
 ('مركز الثقل', 'ağırlık merkezi'), ('التئام', 'uyum, kaynaşma'), ('اطراده', 'genelleştirilmesi, kural olarak işlemesi'), ('توخي', 'gözetme'), ('مهيمنا', 'hâkim'), ('تقلبات', 'dalgalanmalar'), ('أخصب', 'en verimli')],
[('Nazzâm’ın sarfe görüşüne göre i‘câz nerededir?', ['Allah’ın Arapları muârazadan alıkoymasında', 'Kur’an’ın kelimelerinin seçiminde', 'Kur’an’daki bilimsel işaretlerde', 'Kur’an’ın ses ahenginde'], 0, 'صرف العرب عن معارضة القرآن وسلبهم القدرة عليها'),
 ('Metne göre Bâkıllânî’nin eksiği nedir?', ['Şiiri hiç bilmemesi', 'Genelleştirilebilir bir ölçüt koymaması', 'Sarfeyi savunması', 'İlmî i‘câzı reddetmesi'], 1, 'لا يقدم معيارا يمكن اطراده'),
 ('Cürcânî’ye göre meziyet nerededir?', ['Kelimeler arasındaki nahvî ilişkilerde', 'Tek tek kelimelerde', 'Soyut manalarda', 'Seci ve kafiyede'], 0, 'في العلاقات التي تنشأ بين الكلمات'),
 ('İlmî i‘câza yöneltilen eleştiri hangisidir?', ['Metni bilimsel teorilerin değişkenliğine maruz bırakması', 'Belâgati fazla önemsemesi', 'Hadisleri dışlaması', 'Şiire dayanması'], 0, 'يعرض النص لتقلبات النظريات العلمية')])

m('taha-husein', 'edebiyat', 2, 'Tâhâ Hüseyin ve “el-Eyyâm”', 'طه حسين و«الأيام»: السيرة الذاتية بوصفها نقدا للذات والمجتمع',
['حين نشر طه حسين الجزء الأول من «الأيام» مسلسلا في مجلة الهلال أواخر العشرينيات، لم يكن القارئ العربي قد ألف أن يتحدث كاتب عن طفولته بهذا القدر من الصراحة، ولا أن يتحدث عن نفسه بضمير الغائب كأنه يروي حكاية رجل آخر.',
 'وهذا الاختيار السردي ليس حيلة أسلوبية فحسب، بل هو موقف معرفي؛ فالكاتب يقف من الصبي الضرير الذي كانه مسافة تسمح له بالتأمل والسخرية والإشفاق في آن واحد. فهو لا يستدر عطف القارئ، بل يدعوه إلى أن يرى معه كيف تتشكل الذات في مواجهة العجز والجهل والعادات المتحجرة.',
 'وتنتقل السيرة من قرية في صعيد مصر إلى أروقة الأزهر، فترسم صورة نقدية لطرق التعليم القائمة على الحفظ والتكرار، وللشيوخ الذين يحفظون المتون ولا يحسنون فهمها. ويرى بعض الدارسين أن هذه الصفحات كانت تصفية حساب مع مؤسسة لفظته، بينما يرى آخرون أنها شهادة صادقة على مرحلة انتقالية كان فيها التعليم الديني يواجه أسئلة الحداثة.',
 'أما اللغة فهي من أنقى ما كتب في النثر العربي الحديث: جمل طويلة متوازنة، يغلب عليها الإيقاع الصوتي الذي اكتسبه الكاتب من حفظ القرآن ومن اعتماده على السماع بدل القراءة. ولذلك قيل إن نثر طه حسين يكتب للأذن قبل العين.',
 'غير أن مكانة «الأيام» لا تنفصل عن الجدل الذي أثاره صاحبها في كتابه «في الشعر الجاهلي» سنة ١٩٢٦، حين شكك في صحة كثير من الشعر المنسوب إلى ما قبل الإسلام. فقد جعلته تلك المعركة رمزا لمنهج الشك الديكارتي في الدرس الأدبي، كما جعلته هدفا لردود عنيفة من الرافعي ومحمود شاكر وغيرهما.',
 'وسواء اتفق القارئ مع آراء طه حسين أو خالفها، فإن «الأيام» تبقى نصا مؤسسا لفن السيرة الذاتية في الأدب العربي، ونموذجا لكيفية تحويل التجربة الفردية إلى سؤال ثقافي عام.'],
['Tâhâ Hüseyin “el-Eyyâm”ın ilk cildini 1920’lerin sonunda el-Hilâl dergisinde tefrika ettiğinde Arap okuru, bir yazarın çocukluğundan bu ölçüde açık konuşmasına da, kendinden başka bir adamın hikâyesini anlatır gibi üçüncü şahıs zamiriyle bahsetmesine de alışık değildi.',
 'Bu anlatı tercihi yalnızca bir üslup hilesi değil, bilgiye dair bir tavırdır; yazar, bir zamanlar olduğu âmâ çocuğa karşı ona aynı anda hem tefekkürle, hem ironiyle, hem şefkatle bakmasını sağlayan bir mesafede durur. Okurun acımasını dilenmez; onu, benliğin acizlik, cehalet ve katılaşmış âdetler karşısında nasıl şekillendiğini kendisiyle birlikte görmeye çağırır.',
 'Otobiyografi Yukarı Mısır’daki bir köyden Ezher’in revaklarına geçer ve ezber ile tekrara dayanan öğretim usullerinin, metinleri ezberleyip iyi anlayamayan şeyhlerin eleştirel bir tablosunu çizer. Bazı araştırmacılar bu sayfaların yazarı dışlayan bir kurumla hesaplaşma olduğunu düşünürken, diğerleri bunları dinî eğitimin modernitenin sorularıyla yüzleştiği bir geçiş döneminin samimi bir tanıklığı sayar.',
 'Dili ise modern Arap nesrinde yazılmış en saf dillerden biridir: Kur’an’ı ezberlemesinden ve okumak yerine işitmeye dayanmasından edindiği ses ritminin hâkim olduğu, uzun ve dengeli cümleler. Bu yüzden Tâhâ Hüseyin’in nesrinin gözden önce kulak için yazıldığı söylenmiştir.',
 'Ne var ki “el-Eyyâm”ın yeri, yazarının 1926’da “Fi’ş-şi‘ri’l-câhilî” kitabında İslam öncesine nispet edilen şiirin büyük kısmının sıhhatinden şüphe ederek yol açtığı tartışmadan ayrı düşünülemez. O kavga onu edebî araştırmada Kartezyen şüphe metodunun sembolü yaptığı gibi, Râfiî, Mahmud Şâkir ve başkalarının sert reddiyelerinin de hedefi yaptı.',
 'Okur Tâhâ Hüseyin’in görüşlerine katılsın ya da katılmasın, “el-Eyyâm” Arap edebiyatında otobiyografi sanatının kurucu metni ve bireysel tecrübenin genel bir kültürel soruya nasıl dönüştürüleceğinin örneği olarak kalır.'],
[('مسلسلا', 'tefrika hâlinde'), ('ألف', 'alıştı'), ('ضمير الغائب', 'üçüncü şahıs zamiri'), ('حيلة أسلوبية', 'üslup hilesi'), ('الضرير', 'âmâ'), ('يستدر عطف', 'acıma dilenmek'),
 ('المتحجرة', 'katılaşmış'), ('أروقة', 'revaklar'), ('تصفية حساب', 'hesaplaşma'), ('لفظته', 'onu dışladı'), ('شكك في', '…den şüphe etti'), ('نصا مؤسسا', 'kurucu metin')],
[('Yazar kendinden neden üçüncü şahısla söz eder?', ['Çocukluğuna tefekkür, ironi ve şefkatle bakabileceği bir mesafe kurmak için', 'Gerçek kimliğini gizlemek için', 'Dergi editörü öyle istediği için', 'Arapçada birinci şahıs kullanılmadığı için'], 0, 'مسافة تسمح له بالتأمل والسخرية والإشفاق'),
 ('Metne göre Ezher sayfaları hakkındaki iki görüş nedir?', ['Hesaplaşma ve samimi tanıklık', 'Mizah ve trajedi', 'Tarih ve kurgu', 'Övgü ve şükran'], 0, 'تصفية حساب… شهادة صادقة'),
 ('Tâhâ Hüseyin’in nesrinin “kulak için” yazıldığı söylenmesinin sebebi nedir?', ['Ezber ve işitmeye dayanmasından gelen ses ritmi', 'Radyo için yazması', 'Şiir biçiminde yazması', 'Kısa cümleler kullanması'], 0, 'الإيقاع الصوتي'),
 ('“Fi’ş-şi‘ri’l-câhilî” hangi tartışmaya yol açtı?', ['Câhiliye şiirinin sıhhati', 'Kadın eğitimi', 'Ezher’in kapatılması', 'Arap harflerinin değiştirilmesi'], 0, 'شكك في صحة كثير من الشعر')])

m('serbest-siir', 'edebiyat', 2, 'Modern Arap şiirinde serbest şiir', 'قصيدة التفعيلة: ثورة على عمود الشعر أم امتداد له؟',
['ظل عمود الشعر العربي، بوزنه الخليلي وقافيته الموحدة، قرابة خمسة عشر قرنا الإطار الذي لا يكاد يخرج عنه شاعر، حتى عد الخروج عليه خروجا على الشعر نفسه.',
 'وفي سنة ١٩٤٧ نشرت نازك الملائكة قصيدتها «الكوليرا»، ونشر بدر شاكر السياب ديوانه «أزهار ذابلة» وفيه قصيدة «هل كان حبا؟»، فدار جدل طويل حول أيهما السابق. والأهم من الأسبقية أن كليهما اتخذ التفعيلة الواحدة وحدة للإيقاع بدل البيت ذي الشطرين، فصار السطر يطول ويقصر بحسب الدفقة الشعورية.',
 'وقد حرصت نازك في كتابها «قضايا الشعر المعاصر» على أن تؤصل للشكل الجديد من داخل العروض الخليلي، فبينت أن الشعر الحر لا يلغي الوزن بل يحرر عدد التفعيلات، وأنه ينبغي أن يقتصر على البحور الصافية كالكامل والرمل والمتقارب. غير أن الأجيال التالية تجاوزت قيودها، ثم جاءت قصيدة النثر فأسقطت الوزن كليا.',
 'ولم يكن التحول شكليا فحسب؛ فقد حملت قصيدة التفعيلة معها لغة يومية وصورا مستمدة من المدينة والمنفى والأسطورة، كما في توظيف السياب لأسطورة تموز رمزا للموت والانبعاث في «أنشودة المطر».',
 'واختلف النقاد في تقويم هذه الحركة: فمنهم من رآها ثورة ضرورية حررت الشعر من الرتابة والزخرفة اللفظية، ومنهم من عدها قطيعة مع الذاكرة الإيقاعية للأمة، فتحت الباب لنصوص ضعيفة تتستر بالحداثة.',
 'والأرجح أن التجربة لا تقاس بالشكل وحده، بل بقدرة الشاعر على أن يجعل الإيقاع الجديد ضرورة يقتضيها المعنى، لا زيا يلبسه ليبدو معاصرا.'],
['Halîl’in vezni ve tek kafiyesiyle Arap şiirinin “amûdu” yaklaşık on beş yüzyıl boyunca hemen hiçbir şairin dışına çıkmadığı çerçeve olarak kaldı; öyle ki ondan çıkmak şiirin kendisinden çıkmak sayıldı.',
 '1947’de Nâzik el-Melâike “el-Kolera” şiirini, Bedr Şâkir es-Seyyâb ise içinde “Hel kâne hubben?” şiirinin bulunduğu “Ezhâr Zâbile” divanını yayımladı ve hangisinin önce geldiği uzun süre tartışıldı. Öncelikten daha önemlisi, ikisinin de ritim birimi olarak iki mısralı beyit yerine tek tef‘îleyi esas alması ve dizenin duygu akışına göre uzayıp kısalması oldu.',
 'Nâzik “Kadâyâ’ş-şi‘ri’l-mu‘âsır” kitabında yeni biçimi Halîl aruzunun içinden temellendirmeye özen gösterdi; serbest şiirin vezni kaldırmadığını, yalnızca tef‘îlelerin sayısını serbest bıraktığını ve kâmil, remel, mütekârib gibi saf bahirlerle sınırlı kalması gerektiğini açıkladı. Ancak sonraki kuşaklar onun kayıtlarını aştı; ardından gelen mensur şiir ise vezni tamamen düşürdü.',
 'Dönüşüm yalnızca biçimsel değildi; tef‘île şiiri, Seyyâb’ın “Ünşûdetü’l-matar”da Temmûz efsanesini ölüm ve diriliş sembolü olarak kullanmasında olduğu gibi, gündelik bir dili ve şehirden, sürgünden, mitostan devşirilmiş imgeleri de beraberinde getirdi.',
 'Eleştirmenler bu hareketi değerlendirmede ayrıldı: Kimi onu şiiri tekdüzelikten ve lafzî süsten kurtaran zorunlu bir devrim olarak gördü, kimi de milletin ritmik hafızasıyla bir kopuş sayıp modernliğin arkasına saklanan zayıf metinlere kapı açtığını düşündü.',
 'Daha doğrusu, tecrübenin yalnız biçimle ölçülmemesi; şairin yeni ritmi, çağdaş görünmek için giydiği bir kıyafet değil, mananın gerektirdiği bir zorunluluk hâline getirebilmesiyle ölçülmesidir.'],
[('عمود الشعر', 'şiirin amûdu, klasik kaside kuralları'), ('التفعيلة', 'tef‘île, aruz cüzü'), ('الشطرين', 'iki mısra'), ('الدفقة الشعورية', 'duygu akışı'), ('تؤصل', 'temellendirmek'), ('البحور الصافية', 'saf (tek tef‘îleli) bahirler'),
 ('قصيدة النثر', 'mensur şiir'), ('الانبعاث', 'diriliş'), ('الرتابة', 'tekdüzelik'), ('قطيعة', 'kopuş'), ('تتستر', 'gizlenir, perdelenir'), ('زيا', 'kıyafet')],
[('Serbest şiirde ritim birimi nedir?', ['Tek tef‘île', 'İki mısralı beyit', 'Kafiye', 'Hece sayısı'], 0, 'اتخذ التفعيلة الواحدة وحدة للإيقاع'),
 ('Nâzik el-Melâike serbest şiiri hangi bahirlerle sınırlamak istedi?', ['Saf bahirler (kâmil, remel, mütekârib)', 'Bütün bahirler', 'Yalnız tavîl', 'Hiçbir bahir'], 0, 'البحور الصافية'),
 ('Seyyâb Temmûz efsanesini neyin sembolü olarak kullandı?', ['Ölüm ve diriliş', 'Savaş ve barış', 'Aşk ve ayrılık', 'Zenginlik'], 0, 'رمزا للموت والانبعاث'),
 ('Yazarın vardığı sonuç nedir?', ['Yeni ritim mananın gerektirdiği bir zorunluluk olmalıdır', 'Klasik vezne dönülmelidir', 'Mensur şiir en üstün biçimdir', 'Biçim önemsizdir'], 0, 'ضرورة يقتضيها المعنى')])

m('siyasi-soylem', 'medya', 5, 'Siyasî söylem ve örtmece', 'لغة الخطاب السياسي: حين تخفي الكلمات أكثر مما تكشف',
['لا تقتصر وظيفة اللغة السياسية على نقل المعلومات، بل تمتد إلى تشكيل إدراك المتلقي للوقائع قبل أن يحكم عليها. ولذلك يعنى محللو الخطاب بالألفاظ التي تختار بعناية لتخفيف وقع الحقيقة أو تضخيمها.',
 'ومن أشهر هذه الأدوات التلطيف، وهو استبدال لفظ محايد أو ناعم بلفظ صادم: فيقال «إعادة هيكلة» بدل تسريح العمال، و«أضرار جانبية» بدل قتل المدنيين، و«تحريك الأسعار» بدل رفعها. فالمتلقي يتلقى الخبر نفسه، لكن وقعه العاطفي يخفت إلى حد قد يحول دون الاعتراض.',
 'وفي المقابل يلجأ الخطاب التعبوي إلى المبالغة والاستقطاب، فيقسم العالم إلى «نحن» و«هم»، ويصف الخصم بألفاظ تنزع عنه صفته الإنسانية. وتكشف الدراسات أن الجمهور الذي يتعرض لهذا النوع من الخطاب مدة طويلة يصبح أقل قدرة على تقبل الحلول الوسط.',
 'كما يعتمد الخطاب السياسي على البناء للمجهول لإخفاء الفاعل؛ فجملة «اتخذت إجراءات أدت إلى خسائر» لا تخبرنا من اتخذها ولا من يتحمل تبعتها. وهذه الظاهرة النحوية البسيطة قد تكون في السياق السياسي وسيلة فعالة للتنصل من المسؤولية.',
 'ولا يعني هذا أن كل تلطيف خداع؛ فاللغة الدبلوماسية تحتاج إلى قدر من اللين يتيح للأطراف المتنازعة أن تتراجع دون أن تفقد ماء وجهها. والحد الفاصل بين الدبلوماسية والتضليل هو مدى بقاء الحقيقة قابلة للاستخلاص من وراء العبارة.',
 'ومن هنا تبرز أهمية التربية الإعلامية التي تعلم القارئ أن يسأل: من الفاعل؟ ما اللفظ البديل الممكن؟ ولمصلحة من صيغت العبارة بهذه الطريقة؟'],
['Siyasî dilin işlevi bilgi aktarmakla sınırlı kalmaz; alıcının olaylar hakkında hüküm vermeden önce onları nasıl algılayacağını biçimlendirmeye kadar uzanır. Bu yüzden söylem analistleri, gerçeğin etkisini hafifletmek ya da büyütmek için özenle seçilen kelimelerle ilgilenir.',
 'Bu araçların en meşhuru örtmecedir; yani sarsıcı bir kelimenin yerine nötr ya da yumuşak bir kelime koymak: İşçi çıkarmak yerine “yeniden yapılanma”, sivilleri öldürmek yerine “yan hasar”, fiyatları yükseltmek yerine “fiyat hareketlendirme” denir. Alıcı aynı haberi alır; ama duygusal etkisi itiraza engel olacak ölçüde söner.',
 'Buna karşılık seferberlik söylemi abartıya ve kutuplaştırmaya başvurur; dünyayı “biz” ve “onlar” diye ikiye böler, rakibi insanî vasfından soyan kelimelerle niteler. Araştırmalar, bu tür söyleme uzun süre maruz kalan kitlenin orta yol çözümleri kabul etmeye daha az yatkın hâle geldiğini gösteriyor.',
 'Siyasî söylem faili gizlemek için edilgen yapıya da dayanır; “Kayıplara yol açan tedbirler alındı” cümlesi bize onları kimin aldığını da, sorumluluğu kimin taşıdığını da söylemez. Bu basit dil bilgisi olgusu, siyasî bağlamda sorumluluktan sıyrılmanın etkili bir aracı olabilir.',
 'Bu, her örtmecenin bir aldatma olduğu anlamına gelmez; diplomatik dil, çatışan tarafların itibarını kaybetmeden geri adım atabilmesine imkân veren bir ölçüde yumuşaklığa ihtiyaç duyar. Diplomasi ile yanıltma arasındaki sınır, gerçeğin ifadenin arkasından hâlâ çıkarılabilir kalıp kalmadığıdır.',
 'İşte bu noktada okura şunları sormayı öğreten medya okuryazarlığının önemi ortaya çıkar: Fail kim? Yerine hangi kelime kullanılabilirdi? İfade kimin yararına bu şekilde kurulmuş?'],
[('المتلقي', 'alıcı, muhatap'), ('وقع', 'etki'), ('التلطيف', 'örtmece, hüsn-i ta‘bîr'), ('تسريح العمال', 'işçi çıkarma'), ('أضرار جانبية', 'yan hasar'), ('يخفت', 'söner, zayıflar'),
 ('التعبوي', 'seferberlik amaçlı, mobilize edici'), ('الاستقطاب', 'kutuplaşma'), ('البناء للمجهول', 'edilgen yapı'), ('التنصل من', '…den sıyrılma'), ('ماء وجهها', 'itibarı, yüzü'), ('التضليل', 'yanıltma, dezenformasyon')],
[('“أضرار جانبية” ifadesi neyin örneğidir?', ['Örtmece', 'Kutuplaştırma', 'Abartı', 'İstiare'], 0, 'التلطيف'),
 ('Edilgen yapı siyasî söylemde ne işe yarar?', ['Faili ve sorumluyu gizlemeye', 'Cümleyi kısaltmaya', 'Duyguyu artırmaya', 'Rakibi övmeye'], 0, 'لإخفاء الفاعل'),
 ('Metne göre diplomasi ile yanıltma arasındaki sınır nedir?', ['Gerçeğin ifadenin arkasından hâlâ çıkarılabilir olması', 'Kelimelerin uzunluğu', 'Konuşanın makamı', 'Edilgen yapının kullanılmaması'], 0, 'مدى بقاء الحقيقة قابلة للاستخلاص'),
 ('Kutuplaştırıcı söyleme uzun süre maruz kalan kitle hakkında ne söyleniyor?', ['Orta yol çözümleri kabul etmeye daha az yatkın olur', 'Siyasetten uzaklaşır', 'Daha çok okur', 'Daha hoşgörülü olur'], 0, 'أقل قدرة على تقبل الحلول الوسط')])

d = json.load(open(K, encoding='utf-8'))
ids = {x['id'] for x in X}
d['metinler'] = [x for x in d['metinler'] if x.get('id') not in ids] + X
json.dump(d, open(K, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(X), 'C2 metin yazıldı')
