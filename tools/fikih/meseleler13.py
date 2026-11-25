# Fıkıh Dirâsesi — on üçüncü kısım: daha önce yalnız data/fikih/meseleler.json'da bulunan, betik kaynağı olmayan 41 mesele.
# yap.py json'u betiklerden yeniden kurduğu için bunlar silinmesin diye buraya aktarıldı (25 Kasım 2026).
import json
M=json.loads(r'''[
{
"id": "nifas",
"yol": [
"Tahâret",
"Gusül ve hayız"
],
"baslik": "Lohusalığın (nifâs) en uzun süresi",
"ar": "أكثر النفاس",
"hanefi": "Nifâsın en azı için sınır yoktur; en çoğu kırk gündür. Kırk günü aşan kan özür kanıdır (istihâza).",
"mez": {
"maliki": [
"Altmış gün",
"En çok altmış gündür (meşhur); en azının sınırı yoktur."
],
"safii": [
"Altmış gün",
"Çoğunlukla kırk gün, en çok altmış gündür."
],
"hanbeli": [
"Kırk gün",
"En çok kırk gündür; bundan sonra kan devam ederse istihâzadır."
]
},
"sebep": "Bu konuda sahih ve açık bir nas yoktur; Ümmü Seleme’nin “Lohusalar kırk gün otururdu” rivayeti ile kadınların âdetine dair tümevarım (istikrâ) farklı değerlendirilmiştir.",
"delil": [
[
"hadis",
"“Lohusalar Resûlullah zamanında kırk gün otururdu”",
"hadis.html#ara=%D9%83%D8%A7%D9%86%D8%AA%20%D8%A7%D9%84%D9%86%D9%81%D8%B3%D8%A7%D8%A1%20%D8%AA%D8%AC%D9%84%D8%B3%20%D8%B9%D9%84%D9%89%20%D8%B9%D9%87%D8%AF%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87&kap=tisa",
"Ebû Dâvûd, Tirmizî — Ümmü Seleme."
]
],
"usul": "Nas bulunmayan yerde örf ve tümevarım delil kabul edilir; Hanefî ve Hanbelîler rivayeti, diğerleri tümevarımı esas almıştır.",
"metin": [
[
"kuduri",
4,
"وأكثره أربعون يوما"
],
[
"bidaye",
15,
"النفاس"
]
],
"_ibare": [
"kuduri",
4,
"وأقل النفاس لا حد له وأكثره أربعون يوما وما زاد على ذلك فهو استحاضة وإذا تجاوز الدم الأربعين وقد كانت هذه المرأة ولدت قبل ذلك ولها عادة في النفاس ردت إلى أيام عادتها وإن لم لها عادة فابتدأ نفاسها أربعون يوما ومن ولدت ولدين في بطن واحد",
"وأكثره أربعون يوما"
]
},
{
"id": "kedisuru",
"yol": [
"Tahâret",
"Sular ve necasetler"
],
"baslik": "Kedi artığı (sü’r) temiz midir?",
"ar": "سؤر الهرة",
"hanefi": "Kedinin artığı temizdir ama mekruhtur (tenzîhen); başka su varken onunla abdest almamak evlâdır. Tavuk gibi pisliğe dokunan hayvanların artığı da böyledir.",
"mez": {
"maliki": [
"Temiz",
"Kedi artığı temizdir, kerâhet yoktur; ağzında necaset görülmüşse o başka."
],
"safii": [
"Temiz",
"Kedi artığı temiz ve temizleyicidir."
],
"hanbeli": [
"Temiz",
"Kedi ve ondan küçük hayvanların artığı temizdir."
]
},
"sebep": "Kedi artığının temiz olduğunda ittifak vardır. Hanefîler, kedinin necasetten sakınmaması ve etinin yenmemesi sebebiyle kerâhete hükmetmiştir; diğerleri hadisin açık ifadesini esas almıştır.",
"delil": [
[
"hadis",
"“O necis değildir; o etrafınızda dolaşanlardandır”",
"hadis.html#ara=%D8%A5%D9%86%D9%87%D8%A7%20%D9%84%D9%8A%D8%B3%D8%AA%20%D8%A8%D9%86%D8%AC%D8%B3%20%D8%A5%D9%86%D9%87%D8%A7%20%D9%85%D9%86%20%D8%A7%D9%84%D8%B7%D9%88%D8%A7%D9%81%D9%8A%D9%86&kap=tisa",
"Ebû Dâvûd, Tirmizî, Nesâî — Ebû Katâde."
]
],
"usul": "Hadisle sabit temizlik hükmü, etinin yenmemesinden doğan kıyasla tamamen kaldırılmaz; iki delil “kerâhet-i tenzîhiyye” ile uzlaştırılır.",
"metin": [
[
"kuduri",
1,
"وسؤر الهرة"
],
[
"bidaye",
7,
"سؤر"
]
],
"_ibare": [
"kuduri",
1,
"وسؤر الآدمي وما يؤكل لحمه طاهر وسؤر الكلب والخنزير وسباع البهائم نجس وسؤر الهرة والدجاجة المخلاة وسباع الطير وما يسكن في البيوت مثل الحية والفأرة مكروه",
"وسؤر الهرة"
]
},
{
"id": "debag",
"yol": [
"Tahâret",
"Sular ve necasetler"
],
"baslik": "Ölü hayvan derisi tabaklanınca temizlenir mi?",
"ar": "طهارة جلد الميتة بالدباغ",
"hanefi": "Domuz ve insan derisi dışında her deri tabaklanınca temizlenir; üzerinde namaz kılınabilir, ondan su kabı yapılabilir.",
"mez": {
"maliki": [
"Temizlenmez (meşhur)",
"Tabaklanmış ölü derisi hakikaten temiz olmaz; ancak kuru şeylerde ve suda kullanılmasına izin verilir."
],
"safii": [
"Temizlenir",
"Köpek ve domuz ile bunlardan doğanların derisi hariç her deri tabaklanınca temizlenir."
],
"hanbeli": [
"Temizlenmez (mezhep)",
"Ölü derisi tabaklanmakla temizlenmez; bir rivayette eti yenen hayvanın derisi temizlenir."
]
},
"sebep": "“Hangi deri tabaklanırsa temizlenir” hadisi ile “Ölü hayvanın derisinden ve sinirinden faydalanmayın” (Abdullah b. Ükeym) hadisinin nasıl telif edileceği ihtilafın kaynağıdır.",
"delil": [
[
"hadis",
"“Hangi deri tabaklanırsa temizlenmiş olur”",
"hadis.html#ara=%D8%A3%D9%8A%D9%85%D8%A7%20%D8%A5%D9%87%D8%A7%D8%A8%20%D8%AF%D8%A8%D8%BA%20%D9%81%D9%82%D8%AF%20%D8%B7%D9%87%D8%B1&kap=tisa",
"Müslim, Tirmizî — İbn Abbâs."
],
[
"hadis",
"“Ölünün derisinden ve sinirinden faydalanmayın”",
"hadis.html#ara=%D9%84%D8%A7%20%D8%AA%D9%86%D8%AA%D9%81%D8%B9%D9%88%D8%A7%20%D9%85%D9%86%20%D8%A7%D9%84%D9%85%D9%8A%D8%AA%D8%A9%20%D8%A8%D8%A5%D9%87%D8%A7%D8%A8%20%D9%88%D9%84%D8%A7%20%D8%B9%D8%B5%D8%A8&kap=tisa",
"Ebû Dâvûd, Tirmizî — Abdullah b. Ükeym."
]
],
"usul": "Hanefî ve Şâfiîlere göre ‘ihâb’ tabaklanmamış deri demektir; nehiy tabaklanmamışa, ruhsat tabaklanmışa hamledilir.",
"metin": [
[
"kuduri",
1,
"دبغ"
],
[
"bidaye",
26,
"الدباغ"
]
],
"_ibare": [
"kuduri",
1,
"وكل إهاب دبغ فقد ظهر وجازت الصلاة فيه والوضوء منه إلا جلد الخنزير والآدمي",
"دبغ"
]
},
{
"id": "mustamel",
"yol": [
"Tahâret",
"Sular ve necasetler"
],
"baslik": "Kullanılmış su (mâ-i müsta‘mel)",
"ar": "الماء المستعمل",
"hanefi": "Abdest veya gusülde kullanılan su temizdir ama temizleyici değildir; onunla tekrar abdest alınmaz (fetva İmam Muhammed’in görüşüdür).",
"mez": {
"maliki": [
"Temiz ve temizleyici",
"Kullanılmış su temizleyicidir; ancak başka su varken onunla abdest almak mekruhtur."
],
"safii": [
"Temiz, temizleyici değil",
"Farz taharette kullanılan az su temiz olup temizleyici değildir (yeni mezhep)."
],
"hanbeli": [
"Temiz, temizleyici değil",
"Hadesi gidermede kullanılan az su temizdir, temizleyici değildir (mezhep)."
]
},
"sebep": "Suyun kullanılmakla vasfını yitirip yitirmediği, sahâbenin abdest suyunu teberrüken kullanması ve “Durgun suda cünüpken yıkanmayın” hadisinin neye delalet ettiği tartışılmıştır.",
"delil": [
[
"hadis",
"“Biriniz cünüpken durgun suda yıkanmasın”",
"hadis.html#ara=%D9%84%D8%A7%20%D9%8A%D8%BA%D8%AA%D8%B3%D9%84%20%D8%A3%D8%AD%D8%AF%D9%83%D9%85%20%D9%81%D9%8A%20%D8%A7%D9%84%D9%85%D8%A7%D8%A1%20%D8%A7%D9%84%D8%AF%D8%A7%D8%A6%D9%85%20%D9%88%D9%87%D9%88%20%D8%AC%D9%86%D8%A8&kap=tisa",
"Müslim — Ebû Hüreyre."
]
],
"usul": "Nehyin illeti suyun temizleyiciliğini yitirmesidir diyenler kullanılmış suyu temizleyici saymamış; illeti kirlenme sayanlar saymıştır.",
"metin": [
[
"kuduri",
1,
"الماء المستعمل"
],
[
"bidaye",
6,
"الماء المستعمل"
]
],
"_ibare": [
"kuduri",
1,
"والماء المستعمل لا يجوز استعماله في طهارة الأحداث",
"الماء المستعمل"
]
},
{
"id": "mayiile",
"yol": [
"Tahâret",
"Sular ve necasetler"
],
"baslik": "Necaseti sudan başka sıvılarla temizlemek",
"ar": "إزالة النجاسة بغير الماء",
"hanefi": "Ebû Hanîfe ve Ebû Yûsuf’a göre necaset su ile olduğu gibi sirke, gül suyu gibi akıcı ve temizleyici her temiz sıvı ile de giderilebilir.",
"mez": {
"maliki": [
"Ancak su ile",
"Necaset ancak mutlak su ile giderilir."
],
"safii": [
"Ancak su ile",
"Necasetin giderilmesinde su şarttır; istincâda taş istisnadır."
],
"hanbeli": [
"Ancak su ile (mezhep)",
"Necaset ancak temizleyici su ile giderilir; bir rivayette her sıvı ile giderilebilir."
]
},
"sebep": "Maksadın necaseti gidermek mi, yoksa suya mahsus bir taabbüdî hüküm mü olduğu ihtilafın esasıdır.",
"delil": [
[
"ayet",
"Müddessir 74:4",
"./#74-4",
"“Elbiseni temizle.” Âyet temizlemeyi mutlak emretmiştir; Hanefîler bunu delil getirir."
],
[
"hadis",
"Hayız kanını kazıyıp su ile yıkama hadisi",
"hadis.html#ara=%D8%AA%D8%AD%D8%AA%D9%87%20%D8%AB%D9%85%20%D8%AA%D9%82%D8%B1%D8%B5%D9%87%20%D8%A8%D8%A7%D9%84%D9%85%D8%A7%D8%A1&kap=tisa",
"Buhârî, Müslim — Esmâ."
]
],
"usul": "Hanefîler hadisteki ‘su’yu örnek, maksadı necasetin giderilmesi sayar; cumhur ise naslarda geçen suyu taabbüdî kabul eder.",
"metin": [
[
"kuduri",
5,
"ويجوز تطهير النجاسة بالماء"
],
[
"bidaye",
28,
""
]
],
"_ibare": [
"kuduri",
5,
"ويجوز تطهير النجاسة بالماء وبكل مائع طاهر يمكن إزالتها به كالخل وماء الورد",
"ويجوز تطهير النجاسة بالماء"
]
},
{
"id": "kabeici",
"yol": [
"Namaz",
"Vakitler ve şartlar"
],
"baslik": "Kâbe’nin içinde namaz kılmak",
"ar": "الصلاة في الكعبة",
"hanefi": "Kâbe’nin içinde farz da nafile de kılınabilir; kişi hangi yöne dönerse dönsün kıbleye dönmüş olur.",
"mez": {
"maliki": [
"Nafile caiz, farz değil",
"Farz namaz Kâbe içinde kılınmaz; kılınırsa vakit içinde iade edilir. Nafile caizdir."
],
"safii": [
"Caiz",
"Önünde Kâbe’nin bir kısmı bulunmak şartıyla farz ve nafile caizdir."
],
"hanbeli": [
"Nafile caiz, farz değil",
"Farz namaz Kâbe içinde ve damı üzerinde sahih değildir; nafile sahihtir."
]
},
"sebep": "Resûlullah’ın Kâbe içinde namaz kıldığı Bilâl’in rivayetiyle sabittir; ancak bu namazın nafile olması, farzda “Kâbe’nin tamamına yönelme” şartının aranıp aranmayacağını tartışmaya açmıştır.",
"delil": [
[
"hadis",
"Bilâl: Resûlullah Kâbe’nin içinde namaz kıldı",
"hadis.html#ara=%D8%B5%D9%84%D9%89%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87%20%D9%81%D9%8A%20%D8%A7%D9%84%D9%83%D8%B9%D8%A8%D8%A9&kap=tisa",
"Buhârî, Müslim — İbn Ömer."
],
[
"ayet",
"Bakara 2:144",
"./#2-144",
"“Yüzünü Mescid-i Harâm tarafına çevir.”"
]
],
"usul": "Nafile ile farz arasında ayırım yapmayan Hanefî ve Şâfiîler, nafilede sahih olanın farzda da sahih olduğu kaidesini esas alır.",
"metin": [
[
"kuduri",
25,
"الصلاة في الكعبة جائزة فرضها ونفلها"
],
[
"bidaye",
41,
"الكعبة"
]
],
"_ibare": [
"kuduri",
25,
"الصلاة في الكعبة جائزة فرضها ونفلها فإن صلى الإمام بجماعة فجعل بعضهم ظهره الإمام جاز ومن جعل منهم ظهره إلى وجه الإمام لم تجز صلاته",
"الصلاة في الكعبة جائزة فرضها ونفلها"
]
},
{
"id": "tarikussalat",
"yol": [
"Namaz",
"Vakitler ve şartlar"
],
"baslik": "Namazı tembellikle terk edenin hükmü",
"ar": "حكم تارك الصلاة كسلا",
"hanefi": "Namazın farz olduğunu inkâr etmeden tembellikle terk eden kâfir olmaz; fâsıktır. Tövbe edip namaza başlayıncaya kadar hapsedilir ve ta‘zîr olunur.",
"mez": {
"maliki": [
"Had olarak öldürülür",
"Kâfir olmaz; tövbeye çağrılır, kılmazsa had olarak öldürülür."
],
"safii": [
"Had olarak öldürülür",
"Kâfir olmaz; tövbeye çağrılır, kılmazsa had olarak öldürülür, Müslüman olarak defnedilir."
],
"hanbeli": [
"Kâfir olur (mezhep)",
"Tövbeye çağrılıp kılmazsa küfrü sebebiyle öldürülür; bir rivayette had olarak öldürülür."
]
},
"sebep": "“Kişi ile küfür arasında namazı terk etmek vardır” hadisinin hakikat mi yoksa tehdit (küfr-i amelî) mi olduğu; ayrıca “Müslüman kişinin kanı ancak üç şeyden biriyle helal olur” hadisinde namazı terkin sayılmaması tartışmanın temelidir.",
"delil": [
[
"hadis",
"“Kişi ile şirk ve küfür arasında namazı terk etmek vardır”",
"hadis.html#ara=%D8%A8%D9%8A%D9%86%20%D8%A7%D9%84%D8%B1%D8%AC%D9%84%20%D9%88%D8%A8%D9%8A%D9%86%20%D8%A7%D9%84%D8%B4%D8%B1%D9%83%20%D9%88%D8%A7%D9%84%D9%83%D9%81%D8%B1%20%D8%AA%D8%B1%D9%83%20%D8%A7%D9%84%D8%B5%D9%84%D8%A7%D8%A9&kap=tisa",
"Müslim — Câbir."
],
[
"hadis",
"“Müslümanın kanı ancak üç şeyden biriyle helal olur”",
"hadis.html#ara=%D9%84%D8%A7%20%D9%8A%D8%AD%D9%84%20%D8%AF%D9%85%20%D8%A7%D9%85%D8%B1%D8%A6%20%D9%85%D8%B3%D9%84%D9%85%20%D8%A5%D9%84%D8%A7%20%D8%A8%D8%A5%D8%AD%D8%AF%D9%89%20%D8%AB%D9%84%D8%A7%D8%AB&kap=tisa",
"Buhârî, Müslim — İbn Mes‘ûd."
]
],
"usul": "Hanefîler kanı helal kılan sebeplerin nasla sınırlandığını, sınırlanmış sayının kıyasla artırılamayacağını söyler.",
"metin": [
[
"bidaye",
31,
"تارك الصلاة"
]
]
},
{
"id": "selamsayi",
"yol": [
"Namaz",
"Namazın kılınışı"
],
"baslik": "Namazdan çıkarken kaç selam verilir?",
"ar": "عدد التسليم",
"hanefi": "Biri sağa, biri sola olmak üzere iki selam verilir; ikisi de vâciptir.",
"mez": {
"maliki": [
"Tek selam",
"İmam ve tek başına kılan, yüzü önde başlayıp sağa çevirerek tek selam verir; cemaat ayrıca imamın selamını alır."
],
"safii": [
"İki selam",
"Birincisi farz, ikincisi sünnettir."
],
"hanbeli": [
"İki selam",
"Farz namazda iki selam da rükündür (mezhep)."
]
},
"sebep": "Resûlullah’ın sağa ve sola iki selam verdiği İbn Mes‘ûd’dan, tek selam verdiği ise Âişe’den rivayet edilmiştir; Medine ehlinin ameli tek selam yönündedir.",
"delil": [
[
"hadis",
"“Sağına ve soluna, yanağının beyazı görülecek şekilde selam verirdi”",
"hadis.html#ara=%D9%83%D8%A7%D9%86%20%D9%8A%D8%B3%D9%84%D9%85%20%D8%B9%D9%86%20%D9%8A%D9%85%D9%8A%D9%86%D9%87%20%D9%88%D8%B9%D9%86%20%D9%8A%D8%B3%D8%A7%D8%B1%D9%87&kap=tisa",
"Müslim, Ebû Dâvûd — İbn Mes‘ûd."
],
[
"hadis",
"Âişe: “Tek bir selam verirdi”",
"hadis.html#ara=%D9%83%D8%A7%D9%86%20%D9%8A%D8%B3%D9%84%D9%85%20%D8%AA%D8%B3%D9%84%D9%8A%D9%85%D8%A9%20%D9%88%D8%A7%D8%AD%D8%AF%D8%A9&kap=tisa",
"Tirmizî, İbn Mâce."
]
],
"usul": "Mâlikîler Medine ehlinin amelini haber-i vâhide tercih eder; diğerleri sayıca çok ve sahih rivayeti esas alır.",
"metin": [
[
"kuduri",
9,
""
],
[
"bidaye",
50,
"التسليم"
]
]
},
{
"id": "farsca",
"yol": [
"Namaz",
"Namazın kılınışı"
],
"baslik": "Namazda Kur’an’ı Arapçadan başka dille okumak",
"ar": "القراءة بالفارسية",
"hanefi": "Ebû Hanîfe önce Arapçayı bilenin de Farsça okumasıyla namazın sahih olacağını söylemiş, sonra bu görüşünden dönmüştür. Fetvaya göre Arapça okuyabilenin namazı başka dille okumakla sahih olmaz; okuyamayan ise meali okur.",
"mez": {
"maliki": [
"Caiz değil",
"Kur’an ancak Arapça okunur; okuyamayan zikir ve tesbih eder."
],
"safii": [
"Caiz değil",
"Fâtiha’yı Arapça okuyamayan onu öğrenir; öğrenemezse başka âyet veya zikir okur, tercüme okumaz."
],
"hanbeli": [
"Caiz değil",
"Tercüme Kur’an değildir; okuyamayan tesbih ve tahmid eder."
]
},
"sebep": "Kur’an’ın lafız ve mânâdan mı, yoksa yalnız mânâdan mı ibaret olduğu; “Bu, önceki kitaplarda da vardır” (A‘lâ 87:18) âyetinin mânânın başka dilde de Kur’an sayılmasına delil olup olmadığı tartışılmıştır.",
"delil": [
[
"ayet",
"Yûsuf 12:2",
"./#12-2",
"“Biz onu Arapça bir Kur’an olarak indirdik.”"
],
[
"ayet",
"A‘lâ 87:18",
"./#87-18",
"“Bu, önceki sahifelerde de vardır.”"
]
],
"usul": "Ebû Hanîfe’nin dönüşü, Kur’an’ın hem lafız hem mânâ olduğu görüşünün mezhepte esas alınmasını sağlamıştır; Kudûrî ve Hidâye bu dönüşü nakleder.",
"metin": [
[
"kuduri",
9,
""
],
[
"bidaye",
52,
""
]
]
},
{
"id": "imamevla",
"yol": [
"Namaz",
"Vitir, cemaat ve secdeler"
],
"baslik": "İmamete en lâyık kimdir?",
"ar": "الأولى بالإمامة",
"hanefi": "İmamete en lâyık olan, namazın hükümlerini (sünneti) en iyi bilendir; sonra Kur’an’ı en iyi okuyan, sonra en takvalı, sonra en yaşlı gelir.",
"mez": {
"maliki": [
"En fakih",
"Önce fıkhı en iyi bilen, sonra hadisi bilen, sonra en iyi okuyan."
],
"safii": [
"En fakih",
"Namazın fıkhını bilen, Kur’an’ı daha iyi okuyandan önce gelir."
],
"hanbeli": [
"En iyi okuyan",
"Kur’an’ı en iyi okuyan (akra’) önce gelir, sonra en fakih."
]
},
"sebep": "Hadis “Kavme Allah’ın kitabını en iyi okuyanı imam olur” der. Bir kısım âlimler sahâbe döneminde en iyi okuyanın aynı zamanda en fakih olduğunu, namazda fıkha daha çok ihtiyaç duyulduğunu söylemiştir.",
"delil": [
[
"hadis",
"“Kavme Allah’ın kitabını en iyi okuyanı imam olur”",
"hadis.html#ara=%D9%8A%D8%A4%D9%85%20%D8%A7%D9%84%D9%82%D9%88%D9%85%20%D8%A3%D9%82%D8%B1%D8%A4%D9%87%D9%85%20%D9%84%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%84%D9%87&kap=tisa",
"Müslim — Ebû Mes‘ûd el-Ensârî."
],
[
"hadis",
"“Ebû Bekir’e söyleyin, insanlara namaz kıldırsın”",
"hadis.html#ara=%D9%85%D8%B1%D9%88%D8%A7%20%D8%A3%D8%A8%D8%A7%20%D8%A8%D9%83%D8%B1%20%D9%81%D9%84%D9%8A%D8%B5%D9%84%20%D8%A8%D8%A7%D9%84%D9%86%D8%A7%D8%B3&kap=tisa",
"Buhârî, Müslim."
]
],
"usul": "Nassın zahiri ile illeti (namazda gereken bilginin fıkıh olması) arasında tercih yapılmıştır.",
"metin": [
[
"kuduri",
9,
"بالإمامة"
],
[
"bidaye",
55,
"بالإمامة"
]
],
"_ibare": [
"kuduri",
9,
"وأولى الناس بالإمامة أعلمهم",
"بالإمامة"
]
},
{
"id": "cocukimam",
"yol": [
"Namaz",
"Vitir, cemaat ve secdeler"
],
"baslik": "Ergenlik çağına girmemiş çocuğun imamlığı",
"ar": "إمامة الصبي",
"hanefi": "Erginlik çağına girmemiş çocuğun yetişkinlere imamlığı farzda da nafilede de (muhtar görüşe göre) caiz değildir.",
"mez": {
"maliki": [
"Farzda caiz değil",
"Çocuğun farz namazda imamlığı sahih değildir; nafilede kerâhetle caizdir."
],
"safii": [
"Caiz",
"Mümeyyiz çocuğun farzda da nafilede de imamlığı sahihtir; ergin olanın imamlığı evlâdır."
],
"hanbeli": [
"Farzda caiz değil",
"Çocuk farzda yetişkine imam olamaz; nafilede olabilir."
]
},
"sebep": "Amr b. Seleme’nin yedi-sekiz yaşında kavmine imamlık yapması hadisi bir yanda, çocuğun namazının nafile sayılıp farz kılanın nafile kılana uyamaması öte yandadır.",
"delil": [
[
"hadis",
"Amr b. Seleme altı-yedi yaşında kavmine imam oldu",
"hadis.html#ara=%D8%B9%D9%85%D8%B1%D9%88%20%D8%A8%D9%86%20%D8%B3%D9%84%D9%85%D8%A9%20%D9%88%D8%A3%D9%86%D8%A7%20%D8%A7%D8%A8%D9%86%20%D8%B3%D8%AA%20%D8%A3%D9%88%20%D8%B3%D8%A8%D8%B9%20%D8%B3%D9%86%D9%8A%D9%86&kap=tisa",
"Buhârî."
]
],
"usul": "Hanefîler, imamın namazının cemaatinkini “tazammun ettiği” (kapsadığı) ilkesine dayanır; çocuğun nafilesi yetişkinin farzını kapsayamaz.",
"metin": [
[
"kuduri",
9,
"ولا يجوز للرجال أن يقتدوا بامرأة أو صبي"
],
[
"bidaye",
56,
""
]
],
"_ibare": [
"kuduri",
9,
"ولا يجوز للرجال أن يقتدوا بامرأة أو صبي",
"ولا يجوز للرجال أن يقتدوا بامرأة أو صبي"
]
},
{
"id": "farznafile",
"yol": [
"Namaz",
"Vitir, cemaat ve secdeler"
],
"baslik": "Farz kılanın nafile kılana uyması",
"ar": "اقتداء المفترض بالمتنفل",
"hanefi": "Farz kılan, nafile kılan imama uyamaz; nafile kılanın farz kılana uyması ise caizdir.",
"mez": {
"maliki": [
"Caiz değil",
"İmamla cemaatin niyeti aynı olmalıdır."
],
"safii": [
"Caiz",
"Farz kılan nafile kılana, öğleyi kılan ikindiyi kılana uyabilir."
],
"hanbeli": [
"Caiz değil (mezhep)",
"Caiz değildir; bir rivayette caizdir."
]
},
"sebep": "Muâz b. Cebel’in Resûlullah’la yatsıyı kıldıktan sonra kavmine aynı namazı kıldırması hadisi ile “İmam ancak kendisine uyulsun diye kılınmıştır; ona muhalefet etmeyin” hadisinin genel anlamı karşı karşıyadır.",
"delil": [
[
"hadis",
"Muâz’ın Resûlullah’la kıldıktan sonra kavmine imam olması",
"hadis.html#ara=%D9%83%D8%A7%D9%86%20%D9%85%D8%B9%D8%A7%D8%B0%20%D9%8A%D8%B5%D9%84%D9%8A%20%D9%85%D8%B9%20%D8%A7%D9%84%D9%86%D8%A8%D9%8A%20%D8%AB%D9%85%20%D9%8A%D8%A3%D8%AA%D9%8A%20%D9%82%D9%88%D9%85%D9%87&kap=tisa",
"Buhârî, Müslim — Câbir."
],
[
"hadis",
"“İmam kendisine uyulsun diye kılınmıştır, ona muhalefet etmeyin”",
"hadis.html#ara=%D8%A5%D9%86%D9%85%D8%A7%20%D8%AC%D8%B9%D9%84%20%D8%A7%D9%84%D8%A5%D9%85%D8%A7%D9%85%20%D9%84%D9%8A%D8%A4%D8%AA%D9%85%20%D8%A8%D9%87%20%D9%81%D9%84%D8%A7%20%D8%AA%D8%AE%D8%AA%D9%84%D9%81%D9%88%D8%A7%20%D8%B9%D9%84%D9%8A%D9%87&kap=tisa",
"Buhârî, Müslim."
]
],
"usul": "Hanefîler Muâz hadisini, onun Resûlullah’la nafile niyetiyle kıldığı ihtimaline veya hükmün başlangıç dönemine hamletmiştir.",
"metin": [
[
"kuduri",
9,
"المفترض"
],
[
"bidaye",
56,
""
]
],
"_ibare": [
"kuduri",
9,
"لي الذي يركع ويسجد خلف الموميء ولا يصلي المفترض خلف المتنقل ولا من يصلي فرضا خلف من يصلي فرضا آخر ويصلي المتنقل خلف المفترض",
"المفترض"
]
},
{
"id": "sabahsunnet",
"yol": [
"Namaz",
"Vitir, cemaat ve secdeler"
],
"baslik": "Kamet getirildikten sonra sabahın sünnetini kılmak",
"ar": "ركعتا الفجر بعد الإقامة",
"hanefi": "İmam sabah namazına başlamışken gelen kişi, bir rekâta (veya son oturuşa) yetişebileceğini umarsa sünneti cemaatten ayrı bir yerde kılar, sonra imama uyar; yetişemeyeceğinden korkarsa sünneti bırakır.",
"mez": {
"maliki": [
"Mescid dışında",
"Rekâtı kaçırmayacaksa sünneti mescidin dışında kılar; mescidin içinde kılmaz."
],
"safii": [
"Kılınmaz",
"Kamet getirildikten sonra hiçbir nafile kılınmaz; doğrudan cemaate katılır."
],
"hanbeli": [
"Kılınmaz",
"Kamet getirilince nafile kılınmaz; başlamışsa hafifçe tamamlar."
]
},
"sebep": "“Kamet getirilince farzdan başka namaz yoktur” hadisinin mutlak olup olmadığı ile sabah sünnetinin diğer sünnetlerden kuvvetli olması karşı karşıyadır. İbn Mes‘ûd’un mescidin kapısında sünneti kılıp sonra cemaate katıldığı rivayet edilir.",
"delil": [
[
"hadis",
"“Kamet getirildiğinde farzdan başka namaz yoktur”",
"hadis.html#ara=%D8%A5%D8%B0%D8%A7%20%D8%A3%D9%82%D9%8A%D9%85%D8%AA%20%D8%A7%D9%84%D8%B5%D9%84%D8%A7%D8%A9%20%D9%81%D9%84%D8%A7%20%D8%B5%D9%84%D8%A7%D8%A9%20%D8%A5%D9%84%D8%A7%20%D8%A7%D9%84%D9%85%D9%83%D8%AA%D9%88%D8%A8%D8%A9&kap=tisa",
"Müslim — Ebû Hüreyre."
],
[
"hadis",
"“Sabahın iki rekât sünneti dünyadan ve içindekilerden hayırlıdır”",
"hadis.html#ara=%D8%B1%D9%83%D8%B9%D8%AA%D8%A7%20%D8%A7%D9%84%D9%81%D8%AC%D8%B1%20%D8%AE%D9%8A%D8%B1%20%D9%85%D9%86%20%D8%A7%D9%84%D8%AF%D9%86%D9%8A%D8%A7%20%D9%88%D9%85%D8%A7%20%D9%81%D9%8A%D9%87%D8%A7&kap=tisa",
"Müslim — Âişe."
]
],
"usul": "Hanefîler hadisi cemaatle aynı safta, imama muhalefet görüntüsü veren nafileye hamletmiş; ayrı yerde kılınanı nehyin dışında saymıştır.",
"metin": [
[
"kuduri",
12,
""
],
[
"bidaye",
83,
"ركعتي الفجر"
]
]
},
{
"id": "cenazeel",
"yol": [
"Namaz",
"Cenaze"
],
"baslik": "Cenaze namazında elleri kaldırmak",
"ar": "رفع اليدين في تكبيرات الجنازة",
"hanefi": "Eller yalnız ilk tekbirde kaldırılır; diğer üç tekbirde kaldırılmaz.",
"mez": {
"maliki": [
"Yalnız ilkinde (meşhur)",
"Yalnız ilk tekbirde kaldırılır."
],
"safii": [
"Her tekbirde",
"Dört tekbirin hepsinde eller kaldırılır."
],
"hanbeli": [
"Her tekbirde",
"Her tekbirde kaldırılır."
]
},
"sebep": "Bu konuda Resûlullah’tan sahih bir merfû rivayet yoktur. İbn Ömer’in her tekbirde ellerini kaldırdığı rivayet edilir; Hanefîler ise ilk tekbirin iftitah tekbiri olduğunu, diğerlerinin rükû tekbirleri gibi olduğunu söyler.",
"delil": [
[
"hadis",
"İbn Ömer cenazede her tekbirde ellerini kaldırırdı",
"hadis.html#ara=%D9%83%D8%A7%D9%86%20%D8%A7%D8%A8%D9%86%20%D8%B9%D9%85%D8%B1%20%D9%8A%D8%B1%D9%81%D8%B9%20%D9%8A%D8%AF%D9%8A%D9%87%20%D9%81%D9%8A%20%D9%83%D9%84%20%D8%AA%D9%83%D8%A8%D9%8A%D8%B1%D8%A9%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%84%D8%AC%D9%86%D8%A7%D8%B2%D8%A9&kap=tisa",
"Buhârî (ta‘lîk)."
]
],
"usul": "Sahâbî fiilinin delil olup olmadığı ve cenaze tekbirlerinin rekâtlara kıyas edilip edilmeyeceği tartışılmıştır.",
"metin": [
[
"kuduri",
23,
""
],
[
"bidaye",
99,
""
]
]
},
{
"id": "ramazansefer",
"yol": [
"Oruç",
"Oruç"
],
"baslik": "Ramazanda oruca başladıktan sonra yolculuğa çıkmak",
"ar": "الفطر لمن سافر في أثناء النهار",
"hanefi": "Oruçlu olarak sabahlayan sonra gündüz yolculuğa çıkan kişi o günün orucunu bozamaz; bozarsa kaza gerekir, kefaret gerekmez.",
"mez": {
"maliki": [
"Bozamaz",
"Bozarsa kaza gerekir; kefaret konusunda ihtilaf vardır."
],
"safii": [
"Bozamaz",
"Mukimken başlanan oruç tamamlanır."
],
"hanbeli": [
"Bozabilir",
"Yolculuğa çıktıktan sonra o günün orucunu bozabilir."
]
},
"sebep": "Resûlullah’ın Mekke fethi yılında Kedîd’e varınca orucunu açması, yolculuk başladıktan sonra iftara delil sayılmış; diğerleri o günün mukimken başlandığını, hazar hükmünün galip geldiğini söylemiştir.",
"delil": [
[
"hadis",
"Resûlullah Kedîd’e varınca orucunu açtı",
"hadis.html#ara=%D8%AE%D8%B1%D8%AC%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87%20%D8%B9%D8%A7%D9%85%20%D8%A7%D9%84%D9%81%D8%AA%D8%AD%20%D9%81%D8%B5%D8%A7%D9%85%20%D8%AD%D8%AA%D9%89%20%D8%A8%D9%84%D8%BA%20%D8%A7%D9%84%D9%83%D8%AF%D9%8A%D8%AF%20%D8%AB%D9%85%20%D8%A3%D9%81%D8%B7%D8%B1&kap=tisa",
"Buhârî, Müslim — İbn Abbâs."
],
[
"ayet",
"Bakara 2:184",
"./#2-184",
"“Sizden kim hasta veya yolcu olursa…”"
]
],
"usul": "İbadet hazar ile sefer arasında karışınca hazar tarafı (ihtiyat) tercih edilir — Hanefî, Mâlikî ve Şâfiîlerin yaklaşımı budur.",
"metin": [
[
"kuduri",
37,
""
],
[
"bidaye",
129,
""
]
]
},
{
"id": "hamileoruc",
"yol": [
"Oruç",
"Oruç"
],
"baslik": "Hamile ve emzikli kadının oruç tutmaması",
"ar": "فطر الحامل والمرضع",
"hanefi": "Kendisine veya çocuğuna zarar gelmesinden korkan hamile ve emzikli kadın oruç tutmaz; sonra yalnız kaza eder, fidye gerekmez.",
"mez": {
"maliki": [
"Hamile kaza; emzikli kaza+fidye",
"Hamile hasta hükmündedir, yalnız kaza eder; emzikli çocuğu için yerse kaza ile birlikte fidye verir."
],
"safii": [
"Çocuk için ise kaza+fidye",
"Kendisi için korkarsa yalnız kaza; çocuğu için korkarsa kaza ile birlikte her gün için bir müd fidye."
],
"hanbeli": [
"Çocuk için ise kaza+fidye",
"Çocuğu için korkarsa kaza eder ve çocuğun nafakasını veren fidyeyi verir."
]
},
"sebep": "Hamile ve emzikli kadının hastaya mı, yoksa “oruca güç yetirebilenler fidye verir” âyetinde kastedilenlere mi benzetileceği ihtilafın sebebidir. İbn Abbâs ve İbn Ömer’den fidye görüşü rivayet edilmiştir.",
"delil": [
[
"hadis",
"“Allah yolcudan orucu ve namazın yarısını, hamile ve emzikliden orucu kaldırdı”",
"hadis.html#ara=%D8%A5%D9%86%20%D8%A7%D9%84%D9%84%D9%87%20%D9%88%D8%B6%D8%B9%20%D8%B9%D9%86%20%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D9%81%D8%B1%20%D8%A7%D9%84%D8%B5%D9%88%D9%85%20%D9%88%D8%B4%D8%B7%D8%B1%20%D8%A7%D9%84%D8%B5%D9%84%D8%A7%D8%A9%20%D9%88%D8%B9%D9%86%20%D8%A7%D9%84%D8%AD%D8%A7%D9%85%D9%84%20%D9%88%D8%A7%D9%84%D9%85%D8%B1%D8%B6%D8%B9&kap=tisa",
"Ebû Dâvûd, Tirmizî — Enes b. Mâlik el-Ka‘bî."
],
[
"ayet",
"Bakara 2:184",
"./#2-184",
"“Oruca güç yetirebilenler bir yoksul doyumu fidye verir.”"
]
],
"usul": "Hanefîler hadiste hamile ve emzikliyi yolcuyla birlikte zikredilmesini, yolcu gibi yalnız kaza ile yükümlü olduklarına delil sayar.",
"metin": [
[
"kuduri",
37,
"الحامل"
],
[
"bidaye",
128,
"الحامل"
]
],
"_ibare": [
"kuduri",
37,
"والحامل والمريض إذا خافتا على ولديهما أفطرتا وقضتا ولا فدية عليهما",
"الحامل"
]
},
{
"id": "kefarettertip",
"yol": [
"Oruç",
"Oruç"
],
"baslik": "Oruç kefaretinde sıra (tertip)",
"ar": "الترتيب في كفارة الفطر",
"hanefi": "Kefaret sıralıdır: önce köle azadı, buna gücü yetmeyen iki ay peş peşe oruç, buna da gücü yetmeyen altmış fakiri doyurur.",
"mez": {
"maliki": [
"Muhayyer",
"Üçü arasında muhayyerdir; en faziletlisi altmış fakiri doyurmaktır."
],
"safii": [
"Sıralı",
"Köle, sonra iki ay oruç, sonra altmış fakir."
],
"hanbeli": [
"Sıralı (mezhep)",
"Sıralıdır; bir rivayette muhayyerdir."
]
},
"sebep": "Ramazanda eşiyle ilişki kuran bedeviye Resûlullah’ın kefareti sırayla sorması tertibe; Muvatta’daki “Bir köle azat etsin veya oruç tutsun veya yedirsin” rivayeti muhayyerliğe delil sayılmıştır.",
"delil": [
[
"hadis",
"Ramazanda eşiyle ilişki kuran adam hadisi",
"hadis.html#ara=%D9%87%D9%84%20%D8%AA%D8%AC%D8%AF%20%D8%B1%D9%82%D8%A8%D8%A9%20%D8%AA%D8%B9%D8%AA%D9%82%D9%87%D8%A7&kap=tisa",
"Buhârî, Müslim — Ebû Hüreyre."
]
],
"usul": "Hadisin bir rivayetindeki “fe” (sıra) ve diğerindeki “ev” (seçenek) lafızlarından hangisinin tercih edileceği tartışılmıştır.",
"metin": [
[
"kuduri",
37,
"الكفارة"
],
[
"bidaye",
126,
""
]
],
"_ibare": [
"kuduri",
37,
"ومن جامع عامدا في أحد السبيلين أو أكل أو شرب ما يتغذى به أو يتداوى به فعليه القضاء والكفارة مثل كفارة الظهار ومن جامع فيما دون الفرج فأنزل فعليه القضاء ولا",
"الكفارة"
]
},
{
"id": "kadinkefaret",
"yol": [
"Oruç",
"Oruç"
],
"baslik": "Ramazanda ilişkiden dolayı kadına kefaret gerekir mi?",
"ar": "كفارة المرأة في الجماع",
"hanefi": "Kadın rızasıyla ilişkiye girmişse o da kaza ile birlikte ayrıca kefaret öder; zorlanmışsa yalnız kaza eder.",
"mez": {
"maliki": [
"Gerekir",
"Rızasıyla ise kendisine de kefaret gerekir; zorlanmışsa kefaretini koca öder."
],
"safii": [
"Gerekmez (esah)",
"Kefaret yalnız erkeğe gerekir; kadına yalnız kaza düşer."
],
"hanbeli": [
"Gerekir",
"Rızasıyla ise kadına da kefaret gerekir (mezhep)."
]
},
"sebep": "Resûlullah’ın hadiste yalnız erkeğe kefaret emredip kadından söz etmemesi; buna karşılık kadının orucunu kasten bozan bir mükellef olması ihtilafın sebebidir.",
"delil": [
[
"hadis",
"Ramazanda eşiyle ilişki kuran adam hadisi",
"hadis.html#ara=%D9%88%D9%82%D8%B9%D8%AA%20%D8%B9%D9%84%D9%89%20%D8%A7%D9%85%D8%B1%D8%A3%D8%AA%D9%8A%20%D9%88%D8%A3%D9%86%D8%A7%20%D8%B5%D8%A7%D8%A6%D9%85&kap=tisa",
"Buhârî, Müslim — Ebû Hüreyre."
]
],
"usul": "Hanefîler kefaretin illetini “Ramazan orucunu kasten tam bozmak” sayar; bu illet kadında da bulunduğundan hüküm ona da geçer.",
"metin": [
[
"kuduri",
37,
"الكفارة"
],
[
"bidaye",
126,
""
]
]
},
{
"id": "alacakzekat",
"yol": [
"Zekât",
"Zekât ve fıtır"
],
"baslik": "Alacağın (deyn) zekâtı",
"ar": "زكاة الدين",
"hanefi": "Borçlunun ikrar ettiği veya ispat edilebilen kuvvetli alacak tahsil edilince, geçen yılların zekâtı da verilir. Tahsil edilene kadar ödeme gerekmez.",
"mez": {
"maliki": [
"Tahsilde bir yıllık",
"Alacak tahsil edilince, kaç yıl geçmiş olursa olsun, yalnız bir yılın zekâtı verilir."
],
"safii": [
"Her yıl vâcip",
"Ödeme gücü olan borçludaki alacağın zekâtı her yıl vâciptir; tahsil edince ödenir."
],
"hanbeli": [
"Tahsilde geçmiş yıllar",
"Tahsil edilince geçmiş yılların zekâtı verilir."
]
},
"sebep": "Alacağın elde olmaması mülkiyeti eksik kılar mı, yoksa sahibi istediğinde alabileceğinden mevcut mal sayılır mı? Bu konuda Hz. Osman ve Hz. Ali’den farklı rivayetler vardır.",
"delil": [
[
"hadis",
"Hz. Ali: “Alacak doğru ise, tahsil edince geçmiş yılların zekâtını verir”",
"hadis.html#ara=%D9%81%D9%8A%20%D8%A7%D9%84%D8%AF%D9%8A%D9%86%20%D8%A7%D9%84%D8%B8%D9%86%D9%88%D9%86%20%D8%A5%D9%86%20%D9%83%D8%A7%D9%86%20%D8%B5%D8%A7%D8%AF%D9%82%D8%A7%20%D9%81%D9%84%D9%8A%D8%B2%D9%83%D9%87%20%D8%A5%D8%B0%D8%A7%20%D9%82%D8%A8%D8%B6%D9%87%20%D9%84%D9%85%D8%A7%20%D9%85%D8%B6%D9%89&kap=tisa",
"Abdürrezzâk, İbn Ebî Şeybe."
]
],
"usul": "Mülkiyetin varlığı ile malın elde bulunmaması (yed) şartı arasındaki dengeye göre hüküm kurulmuştur.",
"metin": [
[
"kuduri",
26,
""
],
[
"bidaye",
106,
""
]
]
},
{
"id": "tacil",
"yol": [
"Zekât",
"Zekât ve fıtır"
],
"baslik": "Zekâtı yıl dolmadan önce vermek",
"ar": "تعجيل الزكاة",
"hanefi": "Nisaba malik olan kişi zekâtını yıl dolmadan, hatta birkaç yıllığını peşin verebilir.",
"mez": {
"maliki": [
"Caiz değil",
"Yıl dolmadan verilen zekât geçerli olmaz; ancak bir ay kadar kısa bir süre önce verilmesi affedilir."
],
"safii": [
"Bir yıllık caiz",
"Nisaba malik olduktan sonra bir yıllık zekât peşin verilebilir."
],
"hanbeli": [
"İki yıla kadar",
"İki yıllık zekât peşin verilebilir."
]
},
"sebep": "Resûlullah’ın Abbâs’tan iki yıllık zekâtı peşin alması rivayeti ile namazın vaktinden önce kılınamaması gibi ibadetin vaktine bağlı olması arasındaki kıyas tartışılmıştır.",
"delil": [
[
"hadis",
"Abbâs zekâtını vaktinden önce vermek için izin istedi, Resûlullah izin verdi",
"hadis.html#ara=%D8%B3%D8%A3%D9%84%20%D8%A7%D9%84%D8%B9%D8%A8%D8%A7%D8%B3%20%D8%A7%D9%84%D9%86%D8%A8%D9%8A%20%D9%81%D9%8A%20%D8%AA%D8%B9%D8%AC%D9%8A%D9%84%20%D8%B5%D8%AF%D9%82%D8%AA%D9%87%20%D9%82%D8%A8%D9%84%20%D8%A3%D9%86%20%D8%AA%D8%AD%D9%84&kap=tisa",
"Ebû Dâvûd, Tirmizî — Ali."
]
],
"usul": "Hanefîlere göre zekâtın vücûb sebebi nisaba malik olmaktır, yıl dolması ise edânın vaktidir; sebep bulunduktan sonra edâ öne alınabilir.",
"metin": [
[
"kuduri",
26,
""
],
[
"bidaye",
113,
""
]
]
},
{
"id": "zimmizekat",
"yol": [
"Zekât",
"Zekât ve fıtır"
],
"baslik": "Gayrimüslime zekât ve fıtır sadakası vermek",
"ar": "دفع الزكاة إلى الذمي",
"hanefi": "Zekât zimmîye verilmez; fıtır sadakası, kefaret ve adak ise Ebû Hanîfe ve Muhammed’e göre zimmî fakire verilebilir (Müslüman fakire vermek evlâdır).",
"mez": {
"maliki": [
"Hiçbiri verilmez",
"Zekât da fıtır sadakası da Müslüman fakire verilir."
],
"safii": [
"Hiçbiri verilmez",
"Farz sadakalar gayrimüslime verilmez."
],
"hanbeli": [
"Hiçbiri verilmez",
"Zekât ve fıtır gayrimüslime verilmez; kalbi İslam’a ısındırılacaklar (müellefe) istisnadır."
]
},
"sebep": "Muâz hadisindeki “zenginlerinden alınır, fakirlerine verilir” ifadesi zekâtı Müslümanlara tahsis eder. Fıtır sadakası ve kefaretlerde böyle bir tahsis bulunmadığından Hanefîler genel “fakir” ifadesini esas almıştır.",
"delil": [
[
"hadis",
"“Zenginlerinden alınıp fakirlerine verilir”",
"hadis.html#ara=%D8%AA%D8%A4%D8%AE%D8%B0%20%D9%85%D9%86%20%D8%A3%D8%BA%D9%86%D9%8A%D8%A7%D8%A6%D9%87%D9%85%20%D9%81%D8%AA%D8%B1%D8%AF%20%D8%B9%D9%84%D9%89%20%D9%81%D9%82%D8%B1%D8%A7%D8%A6%D9%87%D9%85&kap=tisa",
"Buhârî, Müslim — İbn Abbâs."
],
[
"ayet",
"Mümtehine 60:8",
"./#60-8",
"“Din konusunda sizinle savaşmayanlara iyilik etmenizi Allah yasaklamaz.”"
]
],
"usul": "Hadisle tahsis edilen yalnız zekâttır; tahsis edilmeyenler âyetin umumu üzerinde kalır.",
"metin": [
[
"kuduri",
35,
"ولا يجوز أن يدفع الزكاة إلى ذمي"
],
[
"bidaye",
115,
""
]
],
"_ibare": [
"kuduri",
35,
"ولا يجوز أن يدفع الزكاة إلى ذمي",
"ولا يجوز أن يدفع الزكاة إلى ذمي"
]
},
{
"id": "kiracioşur",
"yol": [
"Zekât",
"Zekât ve fıtır"
],
"baslik": "Kiraya verilen tarlanın öşrü kime aittir?",
"ar": "عشر الأرض المستأجرة",
"hanefi": "Ebû Hanîfe’ye göre öşür tarla sahibine aittir, çünkü kira ürünün karşılığıdır. İmâmeyn’e göre ekini alan kiracıya aittir.",
"mez": {
"maliki": [
"Kiracıya",
"Öşür ekin sahibine (kiracıya) aittir."
],
"safii": [
"Kiracıya",
"Öşür ürünün zekâtıdır; ürün kimin ise ona aittir."
],
"hanbeli": [
"Kiracıya",
"Öşür ekin sahibinindir; tarla sahibine kira bedelinin zekâtı düşer."
]
},
"sebep": "Öşrün toprağın vergisi mi (mev’ûnetü’l-arz), yoksa ürünün zekâtı mı olduğu ihtilafın temelidir.",
"delil": [
[
"hadis",
"“Yağmurun suladığında onda bir vardır”",
"hadis.html#ara=%D9%81%D9%8A%D9%85%D8%A7%20%D8%B3%D9%82%D8%AA%20%D8%A7%D9%84%D8%B3%D9%85%D8%A7%D8%A1%20%D8%A7%D9%84%D8%B9%D8%B4%D8%B1&kap=tisa",
"Buhârî — İbn Ömer."
]
],
"usul": "Ebû Hanîfe öşrü haraç gibi toprağa bağlı bir yük saymış, diğerleri ürünün zekâtı kabul etmiştir.",
"metin": [
[
"kuduri",
34,
""
],
[
"bidaye",
105,
""
]
]
},
{
"id": "kudum",
"yol": [
"Hac",
"Hac"
],
"baslik": "Kudüm (varış) tavafının hükmü",
"ar": "حكم طواف القدوم",
"hanefi": "Mekke dışından gelen ifrad veya kıran haccı yapan için kudüm tavafı sünnettir; terk eden için bir şey gerekmez.",
"mez": {
"maliki": [
"Vâcip",
"Terk eden kurban (dem) keser."
],
"safii": [
"Sünnet",
"Terkinde bir şey gerekmez."
],
"hanbeli": [
"Sünnet",
"Terkinde bir şey gerekmez."
]
},
"sebep": "Resûlullah’ın Mekke’ye girer girmez tavaf etmesi fiilinin vücûb mu, sünnet mi ifade ettiği tartışılmıştır.",
"delil": [
[
"hadis",
"Resûlullah Mekke’ye gelince ilk iş abdest alıp tavaf etti",
"hadis.html#ara=%D8%A3%D9%88%D9%84%20%D8%B4%D9%8A%D8%A1%20%D8%A8%D8%AF%D8%A3%20%D8%A8%D9%87%20%D8%AD%D9%8A%D9%86%20%D9%82%D8%AF%D9%85%20%D8%A3%D9%86%D9%87%20%D8%AA%D9%88%D8%B6%D8%A3%20%D8%AB%D9%85%20%D8%B7%D8%A7%D9%81&kap=tisa",
"Buhârî, Müslim — Âişe."
]
],
"usul": "Fiil-i nebevî, emir ile desteklenmedikçe vücûb ifade etmez — Hanefî, Şâfiî ve Hanbelîlerin kaidesi.",
"metin": [
[
"kuduri",
39,
""
],
[
"bidaye",
139,
""
]
]
},
{
"id": "ihramkadin",
"yol": [
"Hac",
"Hac"
],
"baslik": "İhramlı kadının yüzünü örtmesi ve eldiven giymesi",
"ar": "نقاب المحرمة وقفازها",
"hanefi": "İhramlı kadın yüzüne değecek şekilde peçe takmaz; yüzüne değmeyecek şekilde örtü sarkıtabilir. Eldiven giymesi caizdir.",
"mez": {
"maliki": [
"Eldiven giyemez",
"Yüzüne peçe takmaz, eldiven giymez; giyerse fidye gerekir."
],
"safii": [
"Eldiven giyemez (esah)",
"Peçe ve eldiven yasaktır; yabancı erkeklerden yüzünü değmeyecek şekilde örter."
],
"hanbeli": [
"Eldiven giyemez",
"Peçe ve eldiven yasaktır."
]
},
"sebep": "“İhramlı kadın peçe takmaz, eldiven giymez” cümlesinin Resûlullah’ın sözü mü yoksa İbn Ömer’in sözü mü (müdrec) olduğu tartışılmıştır.",
"delil": [
[
"hadis",
"“İhramlı kadın peçe takmaz, eldiven giymez”",
"hadis.html#ara=%D9%84%D8%A7%20%D8%AA%D9%86%D8%AA%D9%82%D8%A8%20%D8%A7%D9%84%D9%85%D8%B1%D8%A3%D8%A9%20%D8%A7%D9%84%D9%85%D8%AD%D8%B1%D9%85%D8%A9%20%D9%88%D9%84%D8%A7%20%D8%AA%D9%84%D8%A8%D8%B3%20%D8%A7%D9%84%D9%82%D9%81%D8%A7%D8%B2%D9%8A%D9%86&kap=tisa",
"Buhârî — İbn Ömer."
]
],
"usul": "Hanefîler eldiven kısmını İbn Ömer’in fetvası sayar; kadının ihramı yüzündedir, elleri ise ihram yasağı kapsamında değildir.",
"metin": [
[
"kuduri",
39,
""
],
[
"bidaye",
137,
""
]
]
},
{
"id": "tiraş",
"yol": [
"Hac",
"Hac"
],
"baslik": "Tıraşta başın ne kadarı yeterlidir?",
"ar": "مقدار الحلق والتقصير",
"hanefi": "Başın en az dörtte birini tıraş etmek veya saçların uçlarından parmak ucu kadar kısaltmak yeterlidir; tamamını tıraş etmek sünnettir.",
"mez": {
"maliki": [
"Tamamı",
"Başın tamamı tıraş edilir veya bütün saçlardan kısaltılır."
],
"safii": [
"Üç kıl",
"En az üç kıl tıraş etmek veya kısaltmak yeterlidir."
],
"hanbeli": [
"Tamamı",
"Başın tamamı tıraş edilir veya bütün saçlardan kısaltılır."
]
},
"sebep": "Âyetteki “başlarınızı tıraş etmiş olarak” ifadesinin tamamı mı, bir kısmı mı ifade ettiği; abdestteki baş meshi tartışmasına paralel bir ihtilaftır.",
"delil": [
[
"ayet",
"Fetih 48:27",
"./#48-27",
"“Başlarınızı tıraş etmiş ve saçlarınızı kısaltmış olarak…”"
]
],
"usul": "Hanefîler başın dörtte birini, baş meshinde olduğu gibi “tamamın yerine geçen kısım” saymıştır.",
"metin": [
[
"kuduri",
39,
""
],
[
"bidaye",
147,
""
]
]
},
{
"id": "minagece",
"yol": [
"Hac",
"Hac"
],
"baslik": "Teşrik gecelerinde Mina’da kalmak",
"ar": "المبيت بمنى",
"hanefi": "Teşrik gecelerini Mina’da geçirmek sünnettir; terk eden kötü yapmış olur ama bir şey gerekmez.",
"mez": {
"maliki": [
"Vâcip",
"Terk eden kurban keser."
],
"safii": [
"Vâcip (esah)",
"Terk edilen her gece için ceza gerekir."
],
"hanbeli": [
"Vâcip",
"Terk edene dem gerekir."
]
},
"sebep": "Resûlullah’ın Abbâs’a, hacılara su dağıtmak için Mekke’de kalma izni vermesi, Mina’da gecelemenin vâcip olduğuna (izin istisnaya delalet ettiği için) veya sünnet olduğuna delil sayılmıştır.",
"delil": [
[
"hadis",
"Abbâs, su dağıtmak için Mina gecelerinde Mekke’de kalmak üzere izin istedi",
"hadis.html#ara=%D8%A7%D8%B3%D8%AA%D8%A3%D8%B0%D9%86%20%D8%A7%D9%84%D8%B9%D8%A8%D8%A7%D8%B3%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87%20%D8%A3%D9%86%20%D9%8A%D8%A8%D9%8A%D8%AA%20%D8%A8%D9%85%D9%83%D8%A9%20%D9%84%D9%8A%D8%A7%D9%84%D9%8A%20%D9%85%D9%86%D9%89&kap=tisa",
"Buhârî, Müslim — İbn Ömer."
]
],
"usul": "Hanefîler gecelemenin taş atmaya hazırlık (vesile) olduğunu, maksadın kendisi olmadığını söyler.",
"metin": [
[
"kuduri",
39,
""
],
[
"bidaye",
144,
""
]
]
},
{
"id": "mekketemettu",
"yol": [
"Hac",
"Hac"
],
"baslik": "Mekkelinin temettu ve kıran yapması",
"ar": "تمتع المكي وقرانه",
"hanefi": "Mekkeliler ve mîkatın içinde oturanlar için temettu ve kıran yoktur; yalnız ifrad yaparlar. Yaparlarsa ceza kurbanı gerekir.",
"mez": {
"maliki": [
"Caiz, kurban yok",
"Yapabilirler; temettu kurbanı gerekmez."
],
"safii": [
"Caiz, kurban yok",
"Yapabilirler; ancak kurban gerekmez."
],
"hanbeli": [
"Caiz, kurban yok",
"Yapabilirler; kurban gerekmez."
]
},
"sebep": "“Bu, ailesi Mescid-i Harâm’da oturmayanlar içindir” cümlesindeki işaretin (zâlike) temettu hakkına mı, yoksa kurban yükümlülüğüne mi döndüğü ihtilafın sebebidir.",
"delil": [
[
"ayet",
"Bakara 2:196",
"./#2-196",
"“Bu, ailesi Mescid-i Harâm’da oturmayanlar içindir.”"
]
],
"usul": "Hanefîler işaret ismini “temettu”ya döndürür; temettu kolaylığı uzaktan gelenler içindir.",
"metin": [
[
"kuduri",
41,
"وليس لأهل مكة تمتع ولا قران"
],
[
"bidaye",
138,
""
]
],
"_ibare": [
"kuduri",
41,
"وليس لأهل مكة تمتع ولا قران وإنما لهم الإفراد خاصة",
"وليس لأهل مكة تمتع ولا قران"
]
},
{
"id": "cenin",
"yol": [
"Kurban ve av",
"Yiyecekler"
],
"baslik": "Kesilen hayvanın karnından ölü çıkan yavru",
"ar": "ذكاة الجنين",
"hanefi": "Ebû Hanîfe’ye göre annesi kesildikten sonra karnından ölü çıkan yavru yenmez. İmâmeyn’e göre yaratılışı tamamlanmışsa yenir.",
"mez": {
"maliki": [
"Tüylenmişse yenir",
"Yaratılışı tamamlanıp tüyü bitmişse yenir."
],
"safii": [
"Yenir",
"Annesinin kesilmesi onun kesilmesi sayılır."
],
"hanbeli": [
"Yenir",
"Annesinin kesilmesi onun kesilmesi sayılır."
]
},
"sebep": "“Ceninin kesimi annesinin kesimidir” hadisi; bu cümlenin “annesinin kesimi yeterlidir” mi, yoksa “annesinin kesimi gibi kesilir” mi anlamına geldiği tartışılmıştır.",
"delil": [
[
"hadis",
"“Ceninin kesimi annesinin kesimidir”",
"hadis.html#ara=%D8%B0%D9%83%D8%A7%D8%A9%20%D8%A7%D9%84%D8%AC%D9%86%D9%8A%D9%86%20%D8%B0%D9%83%D8%A7%D8%A9%20%D8%A3%D9%85%D9%87&kap=tisa",
"Ebû Dâvûd, Tirmizî — Ebû Saîd."
]
],
"usul": "Ebû Hanîfe hadisi teşbih (benzetme) anlamında okumuş, cenini ayrı bir canlı sayıp ayrıca kesilmesini şart koşmuştur.",
"metin": [
[
"kuduri",
104,
"جنينا ميتا لم يؤكل"
],
[
"bidaye",
185,
""
]
],
"_ibare": [
"kuduri",
104,
"ومن نحر ناقة أو ذبح بقرة أو شاة فوجد في بطنها جنينا ميتا لم يؤكل أشعر أو لم يشعر",
"جنينا ميتا لم يؤكل"
]
},
{
"id": "nafakamiktar",
"yol": [
"Nikâh ve talâk",
"Nikâh"
],
"baslik": "Eşin nafakası neye göre belirlenir?",
"ar": "تقدير نفقة الزوجة",
"hanefi": "Fetvaya göre nafaka karı-kocanın ikisinin hâline göre belirlenir: ikisi zenginse zengin nafakası, ikisi fakirse fakir nafakası, biri zengin biri fakirse orta nafaka.",
"mez": {
"maliki": [
"İkisinin hâli ve örf",
"Kocanın gücü, kadının hâli ve yerin örfü dikkate alınır."
],
"safii": [
"Kocanın hâli",
"Kocanın hâline göre: zengine günde iki müd, ortaya bir buçuk, fakire bir müd."
],
"hanbeli": [
"İkisinin hâli",
"İkisinin hâline göre hâkim belirler."
]
},
"sebep": "“Varlıklı olan nafakayı varlığına göre versin” âyeti kocanın hâline, “Çocuğuna ve sana yetecek kadarını örfe göre al” hadisi kadının ihtiyacına bakmayı gösterir; iki delil birleştirilmiştir.",
"delil": [
[
"ayet",
"Talâk 65:7",
"./#65-7",
"“Varlıklı olan, varlığına göre nafaka versin.”"
],
[
"hadis",
"“Sana ve çocuğuna yetecek kadarını örfe göre al”",
"hadis.html#ara=%D8%AE%D8%B0%D9%8A%20%D9%85%D8%A7%20%D9%8A%D9%83%D9%81%D9%8A%D9%83%20%D9%88%D9%88%D9%84%D8%AF%D9%83%20%D8%A8%D8%A7%D9%84%D9%85%D8%B9%D8%B1%D9%88%D9%81&kap=tisa",
"Buhârî, Müslim — Âişe (Hind)."
]
],
"usul": "Âyet ile hadisin birlikte uygulanması (cem‘) Hanefî fetvasının dayanağıdır.",
"metin": [
[
"kuduri",
89,
""
],
[
"bidaye",
231,
""
]
]
},
{
"id": "zinahurmet",
"yol": [
"Nikâh ve talâk",
"Nikâh"
],
"baslik": "Zina ile evlilik hısımlığı (hurmet-i musâhere) doğar mı?",
"ar": "حرمة المصاهرة بالزنا",
"hanefi": "Zina da nikâh gibi hurmet-i musâhere doğurur: zina edilen kadının annesi ve kızı o erkeğe, erkeğin babası ve oğlu o kadına haram olur.",
"mez": {
"maliki": [
"Doğurmaz (Muvatta’)",
"Haram, helali haram kılmaz."
],
"safii": [
"Doğurmaz",
"Haram ilişki helal olan nikâh hısımlığını doğurmaz."
],
"hanbeli": [
"Doğurur",
"Zina hurmet-i musâhere doğurur."
]
},
"sebep": "Âyetteki “nikâh” kelimesinin akit mi yoksa cinsel birleşme mi olduğu ve “Haram helali haram kılmaz” rivayetinin sıhhati tartışılmıştır.",
"delil": [
[
"ayet",
"Nisâ 4:22",
"./#4-22",
"“Babalarınızın nikâhladığı kadınlarla evlenmeyin.”"
],
[
"hadis",
"“Haram helali haram kılmaz”",
"hadis.html#ara=%D9%84%D8%A7%20%D9%8A%D8%AD%D8%B1%D9%85%20%D8%A7%D9%84%D8%AD%D8%B1%D8%A7%D9%85%20%D8%A7%D9%84%D8%AD%D9%84%D8%A7%D9%84&kap=tisa",
"İbn Mâce, Dârekutnî — İbn Ömer."
]
],
"usul": "Hanefîler “nikâh”ın hakiki anlamının cinsel birleşme olduğunu, akdin mecaz olduğunu kabul eder; hurmet, cüz’iyyet (çocuk doğabilmesi) illetine bağlanmıştır.",
"metin": [
[
"kuduri",
80,
""
],
[
"bidaye",
218,
""
]
]
},
{
"id": "kizkardes",
"yol": [
"Nikâh ve talâk",
"Talâk, iddet ve rada‘"
],
"baslik": "Boşadığı eşin iddeti içinde onun kız kardeşiyle evlenmek",
"ar": "نكاح أخت المعتدة",
"hanefi": "Boşanma ric‘î de olsa bâin de olsa, iddet bitmeden kadının kız kardeşiyle veya beşinci bir kadınla evlenilemez.",
"mez": {
"maliki": [
"Bâinde caiz",
"Bâin talakta iddet içinde kız kardeşiyle evlenebilir."
],
"safii": [
"Bâinde caiz",
"Bâin talakta nikâh bağı kalmadığından evlenebilir."
],
"hanbeli": [
"Caiz değil",
"İddet bitmeden kız kardeşiyle evlenemez."
]
},
"sebep": "İddetin nikâhın bazı hükümlerinin devamı mı (nafaka, evden çıkmama), yoksa nikâhın tamamen sona ermesinin ardından gelen bir bekleme mi olduğu ihtilafın esasıdır.",
"delil": [
[
"ayet",
"Nisâ 4:23",
"./#4-23",
"“…ve iki kız kardeşi bir arada (nikâhınızda) tutmanız (haram kılındı).”"
]
],
"usul": "Hanefîler iddet süresince nikâhın bazı hükümleri sürdüğünden “iki kız kardeşi birleştirme” yasağının kapsamına girdiğini söyler.",
"metin": [
[
"kuduri",
80,
""
],
[
"bidaye",
220,
""
]
]
},
{
"id": "ihdad",
"yol": [
"Nikâh ve talâk",
"Talâk, iddet ve rada‘"
],
"baslik": "Bâin talakla boşanan kadının yas tutması (ihdâd)",
"ar": "إحداد المبتوتة",
"hanefi": "Kocası ölen kadın gibi bâin talakla boşanan kadın da iddeti boyunca süs, koku ve kına gibi şeylerden kaçınarak yas tutar.",
"mez": {
"maliki": [
"Gerekmez",
"İhdâd yalnız kocası ölen kadına vâciptir."
],
"safii": [
"Gerekmez (müstehab)",
"Kocası ölene vâcip, bâin boşanana müstehabdır."
],
"hanbeli": [
"Gerekmez (mezhep)",
"Vâcip değildir; bir rivayette vâciptir."
]
},
"sebep": "Hadis ihdâdı açıkça kocası ölen kadın için emretmiştir. Hanefîler bunu nikâh nimetinin kaybına üzüntüyü göstermek olarak illetlendirmiş ve bâin boşanana da uygulamıştır.",
"delil": [
[
"hadis",
"“Allah’a ve ahiret gününe inanan bir kadının… koca dışında üç günden fazla yas tutması helal değildir”",
"hadis.html#ara=%D9%84%D8%A7%20%D9%8A%D8%AD%D9%84%20%D9%84%D8%A7%D9%85%D8%B1%D8%A3%D8%A9%20%D8%AA%D8%A4%D9%85%D9%86%20%D8%A8%D8%A7%D9%84%D9%84%D9%87%20%D9%88%D8%A7%D9%84%D9%8A%D9%88%D9%85%20%D8%A7%D9%84%D8%A2%D8%AE%D8%B1%20%D8%A3%D9%86%20%D8%AA%D8%AD%D8%AF&kap=tisa",
"Buhârî, Müslim — Ümmü Habîbe."
]
],
"usul": "İllete dayalı kıyas ile hükmün nasta geçen yere hasredilmesi arasındaki tercihtir.",
"metin": [
[
"kuduri",
88,
""
],
[
"bidaye",
269,
""
]
]
},
{
"id": "ine",
"yol": [
"Muâmelât",
"Alışveriş ve akitler"
],
"baslik": "Îne satışı (vadeli satıp peşin ucuza geri almak)",
"ar": "بيع العينة",
"hanefi": "Vadeli sattığı malı, bedelini almadan önce satıcıdan daha ucuza peşin geri almak fâsittir (faize vesile olduğu için).",
"mez": {
"maliki": [
"Bâtıl",
"Faize vesile olduğu için yasaktır (sedd-i zerâi)."
],
"safii": [
"Sahih (mekruh)",
"Akit şeklen sahihtir; niyet akdi bozmaz."
],
"hanbeli": [
"Bâtıl",
"Haramdır; ikinci akit bâtıldır."
]
},
"sebep": "Zeyd b. Erkam’ın böyle bir satış yaptığını duyan Hz. Âişe’nin sert tepkisi ile “Allah alışverişi helal kıldı” âyetinin umumu karşı karşıyadır; ayrıca akitlerde niyetin ve sonucun dikkate alınıp alınmaması tartışılmıştır.",
"delil": [
[
"hadis",
"“Îne ile alışveriş ettiğinizde… Allah üzerinize zillet musallat eder”",
"hadis.html#ara=%D8%A5%D8%B0%D8%A7%20%D8%AA%D8%A8%D8%A7%D9%8A%D8%B9%D8%AA%D9%85%20%D8%A8%D8%A7%D9%84%D8%B9%D9%8A%D9%86%D8%A9&kap=tisa",
"Ebû Dâvûd — İbn Ömer."
],
[
"ayet",
"Bakara 2:275",
"./#2-275",
"“Allah alışverişi helal, faizi haram kıldı.”"
]
],
"usul": "Mâlikî ve Hanbelîler sedd-i zerâi‘ ilkesini, Şâfiîler akdin zahirini esas alır; Hanefîler bedeli ödenmemiş malın daha ucuza geri alınmasını faiz şüphesi sebebiyle fâsit sayar.",
"metin": [
[
"kuduri",
50,
""
],
[
"bidaye",
282,
"العينة"
]
]
},
{
"id": "musakat",
"yol": [
"Muâmelât",
"Kira, rehin ve hibe"
],
"baslik": "Bağ ve bahçe ortakçılığı (müsâkât)",
"ar": "المساقاة",
"hanefi": "Ebû Hanîfe’ye göre bağ-bahçeyi ürünün bir kısmı karşılığında bakıma vermek caiz değildir. İmâmeyn’e göre caizdir; fetva İmâmeyn’in görüşüyledir.",
"mez": {
"maliki": [
"Caiz",
"Hurma ve diğer meyve ağaçlarında caizdir."
],
"safii": [
"Caiz",
"Hurma ve asmada caizdir."
],
"hanbeli": [
"Caiz",
"Meyvesi yenen bütün ağaçlarda caizdir."
]
},
"sebep": "Hayber halkıyla ürünün yarısı karşılığında anlaşma yapılması bir yanda, ücretin bilinmemesi (garar) ve hasılın bir kısmıyla kiralama (kafîz-i tahhân) yasağı öte yandadır.",
"delil": [
[
"hadis",
"Hayber halkıyla çıkan ürünün yarısı karşılığında anlaşıldı",
"hadis.html#ara=%D8%B9%D8%A7%D9%85%D9%84%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87%20%D8%A3%D9%87%D9%84%20%D8%AE%D9%8A%D8%A8%D8%B1%20%D8%A8%D8%B4%D8%B7%D8%B1%20%D9%85%D8%A7%20%D9%8A%D8%AE%D8%B1%D8%AC%20%D9%85%D9%86%D9%87%D8%A7&kap=tisa",
"Buhârî, Müslim — İbn Ömer."
]
],
"usul": "Ebû Hanîfe Hayber muamelesini haraç-ı mukâseme saymış; İmâmeyn ise onu ortakçılığa delil kabul etmiştir. İnsanların ihtiyacı (teâmül) fetvayı İmâmeyn’e çekmiştir.",
"metin": [
[
"kuduri",
79,
""
],
[
"bidaye",
330,
""
]
]
},
{
"id": "hibekabz",
"yol": [
"Muâmelât",
"Kira, rehin ve hibe"
],
"baslik": "Teslim (kabz) olmadan hibe tamam olur mu?",
"ar": "القبض في الهبة",
"hanefi": "Hibe akitle kurulur ama teslim alınmadıkça mülkiyet geçmez; bağışlayan teslimden önce vazgeçebilir veya ölürse hibe düşer.",
"mez": {
"maliki": [
"Akitle bağlayıcı",
"Hibe akitle bağlayıcıdır; teslim tamamlayıcı şarttır, bağışlanan teslimi isteyebilir."
],
"safii": [
"Kabzla tamam olur",
"Teslimden önce mülkiyet geçmez."
],
"hanbeli": [
"Kabzla tamam olur (mezhep)",
"Ölçülüp tartılanlarda kabz şarttır; bir rivayette her şeyde."
]
},
"sebep": "Hz. Ebû Bekir’in Âişe’ye bağışladığı hurmaları teslim almadığı için “Bugün o vârislerin malıdır” demesi kabz şartına; “Akitlerinizi yerine getirin” âyeti akdin bağlayıcılığına delil gösterilir.",
"delil": [
[
"hadis",
"Ebû Bekir: “Onu teslim almış olsaydın senin olurdu; bugün vârislerin malıdır”",
"hadis.html#ara=%D9%84%D9%88%20%D9%83%D9%86%D8%AA%20%D8%AC%D8%AF%D8%AF%D8%AA%D9%8A%D9%87%20%D9%88%D8%A7%D8%AD%D8%AA%D8%B2%D8%AA%D9%8A%D9%87%20%D9%83%D8%A7%D9%86%20%D9%84%D9%83%20%D9%88%D8%A5%D9%86%D9%85%D8%A7%20%D9%87%D9%88%20%D8%A7%D9%84%D9%8A%D9%88%D9%85%20%D9%85%D8%A7%D9%84%20%D9%88%D8%A7%D8%B1%D8%AB&kap=tisa",
"Muvatta’ — Âişe."
],
[
"ayet",
"Mâide 5:1",
"./#5-1",
"“Akitlerinizi yerine getirin.”"
]
],
"usul": "Teberru akitlerinin (karşılıksız bağış) mülkiyeti ancak kabzla geçirmesi, bağışlayana zarar gelmemesi için konmuştur.",
"metin": [
[
"kuduri",
67,
"الهبة"
],
[
"bidaye",
370,
""
]
],
"_ibare": [
"kuduri",
67,
"الهبة: تصح بالإيجاب والقبول وتتم القبض فإذا قبض الموهوب له في المجلس بغير أمر الواهب جاز",
"الهبة"
]
},
{
"id": "tealim",
"yol": [
"Muâmelât",
"Kira, rehin ve hibe"
],
"baslik": "Kur’an öğretmek, ezan ve imamlık için ücret almak",
"ar": "الاستئجار على الطاعات",
"hanefi": "Mezhebin asıl görüşüne göre ibadetler için ücret almak caiz değildir. Sonraki Hanefî âlimler, din eğitimi ve şiarları kaybolmasın diye Kur’an öğretmek, imamlık ve ezan için ücret almayı caiz görmüş; fetva buna göredir.",
"mez": {
"maliki": [
"Caiz",
"Kur’an öğretmek ve ezan için ücret caizdir."
],
"safii": [
"Caiz",
"Kur’an öğretmek için ücret caizdir; farz-ı ayn ibadetler için caiz değildir."
],
"hanbeli": [
"Caiz değil (mezhep)",
"Ücret caiz değildir; beytülmalden maaş veya ücretsiz bağış alınabilir."
]
},
"sebep": "Resûlullah’ın Kur’an öğretmeyi mehir kılması ve “Ücret almaya en lâyık olduğunuz şey Allah’ın kitabıdır” hadisi bir yanda; Osman b. Ebi’l-Âs’a “Ezanına ücret almayan bir müezzin edin” demesi öte yandadır.",
"delil": [
[
"hadis",
"“Ücret almaya en lâyık olduğunuz şey Allah’ın kitabıdır”",
"hadis.html#ara=%D8%A5%D9%86%20%D8%A3%D8%AD%D9%82%20%D9%85%D8%A7%20%D8%A3%D8%AE%D8%B0%D8%AA%D9%85%20%D8%B9%D9%84%D9%8A%D9%87%20%D8%A3%D8%AC%D8%B1%D8%A7%20%D9%83%D8%AA%D8%A7%D8%A8%20%D8%A7%D9%84%D9%84%D9%87&kap=tisa",
"Buhârî — İbn Abbâs."
],
[
"hadis",
"“Ezanına ücret almayan bir müezzin edin”",
"hadis.html#ara=%D9%88%D8%A7%D8%AA%D8%AE%D8%B0%20%D9%85%D8%A4%D8%B0%D9%86%D8%A7%20%D9%84%D8%A7%20%D9%8A%D8%A3%D8%AE%D8%B0%20%D8%B9%D9%84%D9%89%20%D8%A3%D8%B0%D8%A7%D9%86%D9%87%20%D8%A3%D8%AC%D8%B1%D8%A7&kap=tisa",
"Ebû Dâvûd, Tirmizî — Osman b. Ebi’l-Âs."
]
],
"usul": "Müteahhirîn Hanefîlerin fetvası, zamanın değişmesiyle hükmün değişmesi (zaruret ve maslahat) ilkesine dayanır.",
"metin": [
[
"kuduri",
59,
"ولا يجوز الاستئجار على الأذان"
],
[
"bidaye",
324,
""
]
],
"_ibare": [
"kuduri",
59,
"والحجام ولا يجوز أخذ عسب التيس ولا يجوز الاستئجار على الأذان والإقامة والحج والغناء والنوح",
"ولا يجوز الاستئجار على الأذان"
]
},
{
"id": "varisikrar",
"yol": [
"Muâmelât",
"Gasb, emanet ve hacr"
],
"baslik": "Ölüm hastalığında mirasçıya borç ikrarı",
"ar": "إقرار المريض لوارثه",
"hanefi": "Ölüm hastalığındaki kişinin bir mirasçısına borçlu olduğunu ikrar etmesi, diğer mirasçılar onaylamadıkça geçerli değildir.",
"mez": {
"maliki": [
"Töhmet yoksa geçerli",
"İkrarda kayırma şüphesi yoksa geçerlidir."
],
"safii": [
"Geçerli (esah)",
"Hasta kişinin ikrarı mirasçıya da geçerlidir; insan bu hâlde doğru söyler."
],
"hanbeli": [
"Geçerli değil",
"Diğer mirasçılar onaylamadıkça geçersizdir."
]
},
"sebep": "İkrarın mirasçılar arasında kayırma (vasiyete benzer) olma şüphesi ile ölüm hâlinde insanın doğruyu söyleme ihtimalinin yüksekliği arasında tercih yapılmıştır.",
"delil": [
[
"hadis",
"“Mirasçıya vasiyet yoktur”",
"hadis.html#ara=%D9%84%D8%A7%20%D9%88%D8%B5%D9%8A%D8%A9%20%D9%84%D9%88%D8%A7%D8%B1%D8%AB&kap=tisa",
"Ebû Dâvûd, Tirmizî — Ebû Ümâme."
]
],
"usul": "Hanefîler mirasçıya ikrarı, vasiyetin hilesi olabileceği için vasiyete kıyas etmiştir.",
"metin": [
[
"kuduri",
58,
"لوارثه"
],
[
"bidaye",
428,
""
]
],
"_ibare": [
"kuduri",
58,
"عليه ديون في صحته جاز إقراره وكان المقر له أولى من الورثة وإقرار المريض لوارثه باطل إلا أن يصدقه فيه بقية الورثة",
"لوارثه"
]
},
{
"id": "tagrib",
"yol": [
"Cinâyât ve hadler",
"Kısas ve hadler"
],
"baslik": "Bekâr zâniye sopa ile birlikte sürgün",
"ar": "التغريب مع الجلد",
"hanefi": "Had yalnız yüz değnektir; sürgün (tağrîb) haddin parçası değildir. Devlet başkanı maslahat görürse ta‘zîr olarak sürgün edebilir.",
"mez": {
"maliki": [
"Erkeğe sürgün",
"Erkek bir yıl sürgün edilir; kadın fitne endişesiyle sürgün edilmez."
],
"safii": [
"Sürgün hadde dahil",
"Erkek ve kadın bir yıl sürgün edilir; kadın mahremiyle gider."
],
"hanbeli": [
"Sürgün hadde dahil",
"Bir yıl sürgün haddin parçasıdır."
]
},
"sebep": "“Bekâr bekârla zina ederse yüz değnek ve bir yıl sürgün” hadisi ile âyette yalnız yüz değneğin zikredilmesi karşı karşıyadır.",
"delil": [
[
"ayet",
"Nûr 24:2",
"./#24-2",
"“Zina eden kadın ve erkeğin her birine yüz değnek vurun.”"
],
[
"hadis",
"“Bekâr bekârla: yüz değnek ve bir yıl sürgün”",
"hadis.html#ara=%D8%A7%D9%84%D8%A8%D9%83%D8%B1%20%D8%A8%D8%A7%D9%84%D8%A8%D9%83%D8%B1%20%D8%AC%D9%84%D8%AF%20%D9%85%D8%A7%D8%A6%D8%A9%20%D9%88%D9%86%D9%81%D9%8A%20%D8%B3%D9%86%D8%A9&kap=tisa",
"Müslim — Ubâde b. Sâmit."
]
],
"usul": "Hanefîlere göre âyetteki hükme haber-i vâhidle ilave yapmak nesih hükmündedir; bu yüzden sürgün hadde dahil edilmez, siyaset (ta‘zîr) sayılır.",
"metin": [
[
"kuduri",
99,
"ولا يجمع في البكر بين الجلد والنفي"
],
[
"bidaye",
411,
""
]
],
"_ibare": [
"kuduri",
99,
"ولا يجمع في المحصن بين الجلد والرجم ولا يجمع في البكر بين الجلد والنفي إلا أن يرى الإمام ذلك مصلحة فيغربه على قدر ما يراهوإذا زنى المريض وحده الرجم رجم وإن كان حده الجلد لم يجلد حتى يبرأ",
"ولا يجمع في البكر بين الجلد والنفي"
]
},
{
"id": "murtedkadin",
"yol": [
"Cinâyât ve hadler",
"Kısas ve hadler"
],
"baslik": "Dinden dönen kadının hükmü",
"ar": "حكم المرتدة",
"hanefi": "Dinden dönen kadın öldürülmez; İslam’a dönünceye kadar hapsedilir.",
"mez": {
"maliki": [
"Öldürülür",
"Tövbeye çağrılır, dönmezse erkek gibi öldürülür."
],
"safii": [
"Öldürülür",
"Tövbeye çağrılır, dönmezse öldürülür."
],
"hanbeli": [
"Öldürülür",
"Tövbeye çağrılır, dönmezse öldürülür."
]
},
"sebep": "“Dinini değiştireni öldürün” hadisinin umumu ile Resûlullah’ın savaşta kadınların öldürülmesini yasaklaması karşı karşıyadır.",
"delil": [
[
"hadis",
"“Dinini değiştireni öldürün”",
"hadis.html#ara=%D9%85%D9%86%20%D8%A8%D8%AF%D9%84%20%D8%AF%D9%8A%D9%86%D9%87%20%D9%81%D8%A7%D9%82%D8%AA%D9%84%D9%88%D9%87&kap=tisa",
"Buhârî — İbn Abbâs."
],
[
"hadis",
"Resûlullah savaşta kadınların öldürülmesini yasakladı",
"hadis.html#ara=%D9%86%D9%87%D9%89%20%D8%B1%D8%B3%D9%88%D9%84%20%D8%A7%D9%84%D9%84%D9%87%20%D8%B9%D9%86%20%D9%82%D8%AA%D9%84%20%D8%A7%D9%84%D9%86%D8%B3%D8%A7%D8%A1%20%D9%88%D8%A7%D9%84%D8%B5%D8%A8%D9%8A%D8%A7%D9%86&kap=tisa",
"Buhârî, Müslim — İbn Ömer."
]
],
"usul": "Hanefîler irtidat cezasını, savaşan küfre (hırâbe) bağlar; kadın savaşan kimselerden olmadığından asıl küfür hâlindeki gibi öldürülmez.",
"metin": [
[
"kuduri",
113,
"فأما المرأة إذا ارتدت فلا تقتل"
]
],
"_ibare": [
"kuduri",
113,
"فأما المرأة إذا ارتدت فلا تقتل ولكن تحبس حتى تسلم",
"فأما المرأة إذا ارتدت فلا تقتل"
]
},
{
"id": "sirkatekrar",
"yol": [
"Cinâyât ve hadler",
"Kısas ve hadler"
],
"baslik": "Hırsızlığı tekrarlayanın cezası",
"ar": "تكرار السرقة",
"hanefi": "İlk hırsızlıkta sağ el, ikincide sol ayak kesilir; üçüncüde artık kesilmez, tövbe edinceye kadar hapsedilir ve ta‘zîr olunur.",
"mez": {
"maliki": [
"Dört uzva kadar",
"Üçüncüde sol el, dördüncüde sağ ayak kesilir; sonra hapsedilir."
],
"safii": [
"Dört uzva kadar",
"Üçüncüde sol el, dördüncüde sağ ayak; sonra ta‘zîr."
],
"hanbeli": [
"İki uzva kadar",
"Hanefîler gibi; üçüncüde hapsedilir (mezhep)."
]
},
"sebep": "Dört uzvun kesilmesini bildiren rivayetlerin sıhhati ile Hz. Ali’nin “Ne yiyeceği eli ne yürüyeceği ayağı kalmasın, bundan Allah’tan hayâ ederim” sözü karşı karşıyadır.",
"delil": [
[
"hadis",
"Hz. Ali: “Ne eli ne ayağı kalsın diye kesmekten Allah’tan hayâ ederim”",
"hadis.html#ara=%D8%A5%D9%86%D9%8A%20%D9%84%D8%A3%D8%B3%D8%AA%D8%AD%D9%8A%D9%8A%20%D8%A7%D9%84%D9%84%D9%87%20%D8%A3%D9%86%20%D9%84%D8%A7%20%D8%A3%D8%AF%D8%B9%20%D9%84%D9%87%20%D9%8A%D8%AF%D8%A7%20%D9%8A%D8%A3%D9%83%D9%84%20%D8%A8%D9%87%D8%A7&kap=tisa",
"Beyhakî, Abdürrezzâk."
],
[
"ayet",
"Mâide 5:38",
"./#5-38",
"“Hırsız erkek ve hırsız kadının ellerini kesin.”"
]
],
"usul": "Hadler şüpheyle düşer; zayıf rivayetlerle helak edici bir ceza kurulmaz — Hanefî ve Hanbelî yaklaşımı.",
"metin": [
[
"kuduri",
102,
""
],
[
"bidaye",
416,
""
]
]
},
{
"id": "unutyemin",
"yol": [
"Yeminler",
"Yemin"
],
"baslik": "Unutarak veya zorla yemini bozmak",
"ar": "الحنث ناسيا أو مكرها",
"hanefi": "Yeminini unutarak veya zorlanarak bozan kişiye kefaret gerekir; çünkü hüküm yemin edilen fiilin gerçekleşmesine bağlıdır.",
"mez": {
"maliki": [
"Gerekir",
"Unutarak bozan da yemini bozmuş sayılır."
],
"safii": [
"Gerekmez (esah)",
"Unutan ve zorlanan yemini bozmuş sayılmaz."
],
"hanbeli": [
"Ayrıma göre",
"Allah adına yeminde unutana kefaret gerekmez; talak ve ıtakta yemin bozulur (mezhep)."
]
},
"sebep": "“Ümmetimden hata, unutma ve zorlama kaldırıldı” hadisinin günahı mı yoksa dünyevi hükmü (kefareti) de mi kaldırdığı ihtilafın sebebidir.",
"delil": [
[
"hadis",
"“Ümmetimden hata, unutma ve zorlandıkları şey kaldırıldı”",
"hadis.html#ara=%D8%A5%D9%86%20%D8%A7%D9%84%D9%84%D9%87%20%D9%88%D8%B6%D8%B9%20%D8%B9%D9%86%20%D8%A3%D9%85%D8%AA%D9%8A%20%D8%A7%D9%84%D8%AE%D8%B7%D8%A3%20%D9%88%D8%A7%D9%84%D9%86%D8%B3%D9%8A%D8%A7%D9%86%20%D9%88%D9%85%D8%A7%20%D8%A7%D8%B3%D8%AA%D9%83%D8%B1%D9%87%D9%88%D8%A7%20%D8%B9%D9%84%D9%8A%D9%87&kap=tisa",
"İbn Mâce — İbn Abbâs."
]
],
"usul": "Hanefîler hadisi uhrevî hükme (günaha) hamleder; dünyevi hükümler fiilin varlığına bağlanır.",
"metin": [
[
"kuduri",
106,
""
],
[
"bidaye",
174,
""
]
]
}
]''')
