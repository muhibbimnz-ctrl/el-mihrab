import json
TR={
'60.0':'İsim ya ortak bir harfle cerrolunur —من، إلى، عن، على، في، lâm ve bâ (kasem için ve başka mânâlarda)— ya da zâhir isme mahsus bir harfle: ربّ، مذ، منذ، kâf, حتى, kasem vâvı ve kasem tâsı.',
'62.0':'Ya da izâfetle cerrolunur: lâm mânâsıyla (غلامُ زيدٍ), min mânâsıyla (خاتمُ حديدٍ) veya fî mânâsıyla (مكرُ الليلِ); buna ma‘nevî izâfet denir, çünkü ta‘rîf veya tahsis içindir. Vasfın ma‘mûlüne izâfeti de vardır (بالغَ الكعبةِ، معمورُ الدارِ، حسنُ الوجهِ); buna lafzî izâfet denir, çünkü yalnız hafifletmek içindir.',
'62.3':'İzâfet; tenvîn, i‘râb harfinden sonra gelen nûn ve el- ile hiçbir şekilde bir arada bulunmaz; ancak الضاربا زيدٍ، الضاربو زيدٍ، الضاربُ الرجلِ، الضاربُ رأسِ الجاني، الرجلُ الضاربُ غلامِه gibi (lafzî izâfet) örneklerinde el- bulunabilir.',
'63.0':'Fiilinin amelini yapan yedi şey vardır: (1) İsm-i fiil: هيهات (uzak oldu), صه (sus), وي (hayret!) gibi. İsm-i fiil hazfedilmez, ma‘mûlünden sonra gelmez (كتابَ الله عليكم te’vil edilir), zamiri açık görünmez; talep bildirenin cevabında muzâri meczûm olur (مكانَكِ تُحمَدي أو تستريحي), mansûb olmaz.',
'65.0':'(2) Masdar: ضرب ve إكرام gibi; yerine أن veya ما ile birlikte fiil konulabilirse amel eder. Amel etmesi için tasgîr edilmemiş, zamir olmamış, (tek seferlik) sınırlanmamış, amelden önce sıfatlanmamış, hazfedilmemiş, ma‘mûlünden ayrılmamış ve ondan sonra gelmemiş olmalıdır. Muzâf olarak amel etmesi daha çoktur (ولولا دفعُ اللهِ الناسَ), tenvînli olarak daha kıyâsîdir (أو إطعامٌ في يومٍ ذي مسغبةٍ يتيمًا), el-’li olarak şâzdır.',
'66.0':'(3) İsm-i fâil: ضارب، مكرم gibi. El-’li ise mutlak olarak amel eder; el-’siz ise iki şartla: hâl veya istikbâl bildirmesi ve nefy, istifhâm, haber verilen (mübtedâ) veya mevsûfa dayanması. وباسطٌ ذراعيه hikâye-i hâl üzere açıklanır (Kisâî buna muhaliftir). (4) Mübalağa sîgası: fâil’den çokça فعّال، فعول، مفعال’e, azca فعيل veya فَعِل’e çevrilen kalıplardır: أمّا العسلَ فأنا شرّابٌ.',
'68.0':'(5) İsm-i mef‘ûl: مضروب، مكرَم gibi; fiilinin amelini yapar ve (şartlarda) ism-i fâil gibidir.',
'69.0':'(6) Tek mef‘ûllü müteaddî ism-i fâile benzetilen sıfat-ı müşebbehe: tafdîl dışında, sübût ifade etmek için yapılmış sıfattır (حسن، ظريف، طاهر، ضامر). Ma‘mûlü öne geçmez ve yabancı (sıfatın sahibine bağlı olmayan) olmaz. Ma‘mûlü fâil veya bedel olarak merfû, temyîz veya mef‘ûlün bihe benzetme olarak mansûb (ma‘rifede ikincisi taayyün eder) ve izâfetle mecrûr olur.',
'69.4':'(7) İsm-i tafdîl: ortaklık ve fazlalık bildiren sıfattır (أكرم). من ile ve nekreye muzâf olarak kullanılınca tekil ve müzekker kalır; el- ile kullanılınca (mevsûfuna) uyar; ma‘rifeye muzâf olunca iki vecih câizdir. Hiçbir şekilde mef‘ûl nasbetmez; çoğunlukla zâhir ismi de ref‘ etmez — “kuhl meselesi” bundan müstesnâdır.',
'71.0':'Tâbiler: Kendinden öncekine i‘râbında tâbi olanlar beştir.',
'72.1':'(1) Na‘t: metbûunun lafzından farklı olan, müştak veya müştak ile te’vil edilen tâbidir.',
'72.3':'Faydası tahsis, tavzîh, medih, zem, terahhum veya tekîddir.',
'72.5':'Na‘t, i‘râbın bir vechinde ve ma‘rifelik–nekrelikte men‘ûtuna uyar. Gizli bir zamiri ref‘ ediyorsa müzekkerlik–müenneslikte ve tekil–tesniye–cemide de uyar; aksi hâlde fiil gibidir. En güzeli جاءني رجلٌ قعودٌ غلمانُه, sonra قاعدٌ, sonra قاعدون’dur.',
'72.9':'Mevsûfu gerçekte veya iddiada belli olan sıfatı (tâbilikten) kesmek câizdir: هو takdiriyle ref‘, أعني، أمدح، أذمّ veya أرحم takdiriyle nasb.',
'73.0':'(2) Tekîd: ya lafzîdir — “أخاك أخاك؛ kardeşi olmayan kimse…”, “أتاك أتاك اللاحقون، احبسِ احبسِ”, “لا لا أبوح بحبّ بثنة” gibi; دكًّا دكًّا ve صفًّا صفًّا bundan değildir—',
'73.3':'—ya da ma‘nevîdir: نفس ve عين iledir; ikisi birlikte gelirse عين sonra gelir; tekil olmayanla أفعُل vezninde cemilenir (أنفُسهم، أعيُنهم). Kendisi veya âmili itibarıyla cüzlere ayrılabiliyorsa tesniye dışındakiler için كلّ; yerine tekil konulabiliyor ve isnad edilen mânâ bir ise tesniye için كلا ve كلتا ile yapılır. Bunlar tekîd edilenin zamirine muzâf olur. أجمع، جمعاء ve cemileri ise muzâf olmadan gelir.',
'73.6':'Na‘tların aksine tekîd lafızları birbirine atfedilmez ve nekreye tâbi olmaz; “يا ليت عدّةَ حولٍ كلِّه رجب” nâdirdir.',
'74.2':'(3) Atf-ı beyân: metbûuna (ma‘rifelik, nekrelik vb.) uyar.',
'74.4':'أقسم بالله أبو حفصٍ عمرُ ve هذا خاتمٌ حديدٌ gibi.',
'74.6':'Birincinin yerine konulması imkânsız değilse bedel-i küll mine’l-küll olarak i‘râb edilebilir; “أنا ابنُ التاركِ البكريِّ بشرٍ” ve “أيا أخوينا عبدَ شمسٍ ونوفلا” sözlerinde ise (bedel olamaz, atf-ı beyândır).',
'75.0':'(4) Atf-ı nesak: vâv iledir;',
'75.2':'vâv mutlak cem‘ (birleştirme) içindir.',
'75.4':'Fâ tertip ve ta‘kîb (hemen ardından) içindir.',
'75.6':'Sümme tertip ve terâhî (aralıklı ardından) içindir.',
'75.8':'Hattâ gâye ve tedrîc içindir,',
'75.10':'tertip için değildir.',
'75.12':'Ev, iki veya daha çok şeyden biri içindir; talepten sonra tahyîr veya ibâha, haberden sonra şek veya teşkîk ifade eder.',
'75.15':'Em, eşit iki şeyden birinin başına giren hemzeden sonra tayin talebi içindir.',
'75.17':'Hükümdeki hatayı düzeltmek için: müsbetten sonra lâ, nefyden sonra lâkin ve bel; hükmü sonrakine çevirmek için müsbetten sonra bel.',
'75.19':'(5) Bedel: hükümde vasıtasız kastedilen tâbidir; altı çeşittir: küll (مفازًا حدائقَ), ba‘z (مَن استطاع), iştimâl (قتالٍ فيه); idrâb, galat ve nisyân: تصدّقتُ بدرهمٍ دينارٍ — birinci ve ikinci kastedildiyse idrâb, ikinci kastedilip dil sürçtüyse galat, birinci kastedilip sonra hata anlaşıldıysa nisyân.',
'77.0':'Sayı: Üçten dokuza kadar sayılar müzekkerle müennes, müennesle müzekker olarak daima gelir: سبعَ ليالٍ وثمانيةَ أيامٍ. On da birleşik değilse böyledir. Üçten aşağısı ve فاعل vezni (ثالث، رابع) daima kıyâs üzeredir (uyar). فاعل vezni ya tekil kullanılır, ya türediği sayıya veya kendinden aşağısına muzâf olur, ya da kendinden aşağısını nasbeder.',
'78.0':'Gayr-i munsarif: ismi tenvînden men eden sebepler dokuzdur; şu beyitte toplanmıştır: vezn, terkîb, ucme, ta‘rîf, adl, vasf, cem‘, (elif-nûn) ziyâdesi, te’nîs — أحمد، أحمر، بعلبك، إبراهيم، عمر، أُخَر، أُحاد ve dörde kadar مَوحَد، مساجد، دنانير، سلمان، سكران، فاطمة، طلحة، زينب، سلمى، صحراء gibi. Te’nîs elifi ve tekillerde benzeri olmayan cem‘ tek başlarına engel olur; diğerlerinin her biri vasıf veya alemiyyetle birlikte bulunmalıdır. Terkîb, te’nîs ve ucmede alemiyyet taayyün eder. Ucmenin şartı, Acem dilinde alem olması ve üç harften fazla olmasıdır; vasfın şartı asıl olması ve tâ kabul etmemesidir; bu yüzden عريان، أرمل، صفوان ve “katı” mânâsında أرنب munsariftir. هند gibilerde iki vecih câizdir; زينب، سقر ve بلخ’te değildir. Temîm’e göre عمر gibi olanlar: râ ile bitmeyen حذام bâbı (سفار müstesna), merfû ve belli gün için أمس — bazıları ikisinde şart koşmaz — ve herkese göre belli bir vakit için zarf olan سحر.',
'88.0':'Taaccüb: iki sîgası vardır. Birincisi ما أفعلَ زيدًا; i‘râbı: ما “büyük bir şey” mânâsında mübtedâ, أفعل mâzî fiil ve fâili mâya râci zamir, زيدًا mef‘ûlün bih, cümle de mânın haberidir. İkincisi أفعِلْ به; mânâsı ما أفعلَه’dir; aslı “şöyle sahibi oldu” mânâsında أفعلَ’dir (أغدّ البعيرُ: deve guddeli oldu); lafız değiştirilmiş ve lafzı düzeltmek için fâile bâ eklenmiştir; bu yüzden burada lâzımdır, كفى’nın fâilinde ise değildir. Taaccüb fiilleri ve ism-i tafdîl ancak üç harfli, müsbet, dereceli, tam, ma‘lûm ve ism-i fâili أفعل vezninde olmayan fiilden yapılır.',
'89.0':'Vakf: En fasih olan, رحمة gibilerde hâ ile, مسلمات’ta tâ ile durmaktır.',
'89.2':'قاضٍ gibilerde ref‘ ve cer hâlinde (yâyı) hazfederek, القاضي gibilerde ise bu iki hâlde yâyı ispat ederek durulur.',
'89.4':'Bunlarda bazen aksi yapılır.',
'89.6':'قاضيًا ve القاضيَ’nin nasb hâlinde ise yalnız yâ ile durulur.',
'89.8':'إذًا، لنسفعًا ve رأيتُ زيدًا’da elif ile durulur,',
'89.10':'yazıldıkları gibi.',
'89.12':'Elif, cemâat vâvından sonra yazılır (قالوا), aslî vâvdan sonra yazılmaz (زيد يدعو). Elif üç harfi aşarsa (استدعى، المصطفى) veya aslı yâ ise (رمى، الفتى) yâ şeklinde, diğerlerinde elif şeklinde yazılır (قفا، العصا). Fiildeki elifin aslı tâ ile (رميتُ، عفوتُ), isimdeki ise tesniye ile (عصوان، فتيان) anlaşılır.',
'90.0':'Fasıl: Kesre ve damme ile اسم، است، ابن، ابنم، ابنة، امرؤ، امرأة ve bunların tesniyeleri, اثنان، اثنتان, الغلام (el-’in hemzesi) ve kasemdeki ايمن الله’ın hemzesi vasl hemzesidir: başta söylenir, vaslda düşer. Dört harften fazla mâzînin (استخرج), emrinin ve masdarının; üç harfli fiilin emrinin hemzesi de böyledir: اُقتل، اُغزُ، اُغزي dammeli; اِضرب، اِمشوا، اِذهب ve diğerleri kesrelidir.',
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
miss=[f'{i}.{j}' for i,b in enumerate(d['bolumler']) for j,t in enumerate(b['pt']) if t=='m' and not b['tr'][j]]
print('eksik',miss)
