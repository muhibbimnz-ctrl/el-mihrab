import json
TR={
'1.0':'Kelime, müfred (tek) bir sözdür.',
'1.3':'Kelime isim, fiil ve harftir.',
'2.0':'İsim; el- takısı (الرجل), tenvîn (رجلٌ) ve hakkında haber verilebilmesi (ضربتُ’deki tâ gibi) ile tanınır.',
'2.2':'İsim iki çeşittir: Mu‘reb, kendisine giren âmiller sebebiyle sonu değişendir (زيد gibi). Mebnî bunun aksidir: هؤلاء kesrede sabit kalır; Hicazlılara göre حذام ve أمس de öyledir; أحد عشر ve benzerleri fethada; muzâf ileyhi hazfedilip mânâsı niyet edildiğinde قبل ve بعد ve benzerleri dammede; من ve كم sükûnda sabit kalır. Sükûn, binânın aslıdır.',
'4.0':'Fiil üç kısımdır. Mâzî: sâkin te’nîs tâsıyla tanınır; binâsı fetha üzeredir (ضرب); vâv-ı cemâatle damme (ضربوا), mütehharrik merfû zamirle sükûn (ضربتُ) olur. En doğru görüşe göre نعم، بئس، عسى ve ليس de mâzîdendir. Emir: talebe delâlet etmesi ve muhâtaba yâsını kabul etmesiyle tanınır; binâsı sükûn üzeredir (اضربْ); mu‘tel ise sonunun hazfı üzere (اغزُ، اخشَ، ارمِ), قوما، قوموا، قومي gibilerde nûnun hazfı üzere mebnîdir. Temîm lehçesinde هلمّ, en doğru görüşe göre هاتِ ve تعالَ de emirdendir. Muzâri: لم ile tanınır, başında “نأيت” harflerinden biri bulunur (نقوم، أقوم، يقوم، تقوم). Mâzîsi dört harfli ise başı dammeli (يدحرج، يكرم), değilse fethalıdır (يضرب، يجتمع، يستخرج). Nûn-ı nisve ile sonu sâkin olur (يتربّصن، إلا أن يعفون); lafzen veya takdîren doğrudan bitişen nûn-ı tekîd ile fethalı olur (لينبذنّ).',
'4.1':'Bunların dışında muzâri mu‘rebdir: يقومُ زيدٌ، ولا تتّبعانِّ، لتُبلَوُنّ، فإمّا تَرَيِنّ، ولا يصدُّنّك.',
'8.0':'Harf, isim ve fiil alâmetlerinden hiçbirini kabul etmemesiyle tanınır: هل، بل gibi. En doğru görüşe göre مهما ve إذ ما harf değildir; masdariyye mâ ile rabıt lemmâ ise harftir.',
'8.4':'Bütün harfler mebnîdir.',
'9.1':'Kelâm, faydalı (mânâ ifade eden) lafızdır.',
'9.3':'En az iki isimden (زيد قائم) veya bir fiil ile bir isimden (قام زيد) meydana gelir.',
'10.0':'Fasıl: İ‘râbın çeşitleri dörttür: ref‘ ve nasb isimde ve fiilde olur (زيدٌ يقومُ، إنّ زيدًا لن يقومَ); cer yalnız isimde (بزيدٍ), cezm yalnız fiilde (لم يقمْ) olur. Ref‘ damme, nasb fetha, cer kesre, cezm harekenin hazfı ile olur.',
'11.0':'Ancak esmâ-i sitte —أبوه، أخوه، حموها، هنوه، فوه ve ذو مال— vâv ile merfû, elif ile mansûb, yâ ile mecrûr olur.',
'11.3':'هَن kelimesini غَد gibi (harekelerle) kullanmak daha fasihtir.',
'12.0':'Tesniye (الزيدان) elif ile, cem‘-i müzekker sâlim (الزيدون) vâv ile merfû olur; ikisi de yâ ile mecrûr ve mansûb olur. كلا ve كلتا zamire muzâf olunca tesniye gibidir; اثنان ve اثنتان (birleşik de olsa) da öyledir. أولو، عشرون ve kardeşleri، عالمون، أهلون، وابلون، أرضون، سنون ve benzerleri، بنون، عليّون cem‘ gibi i‘râb olunur.',
'12.4':'أولات ile zâid bir elif ve tâ ile cemilenen (ve bunlardan isim olarak verilen) kelimeler kesre ile mansûb olur: خلق الله السمواتِ، اصطفى البناتِ.',
'12.6':'Munsarif olmayan isim fetha ile mecrûr olur (بأفضلَ منه); ancak el- ile (بالأفضلِ) veya muzâf olunca (بأفضلِكم) kesre ile mecrûr olur.',
'14.0':'Emsile-i hamse — تفعلان ve تفعلون (yâ ve tâ ile) ile تفعلين — nûnun sübûtu ile merfû, hazfıyla meczûm ve mansûb olur: فإن لم تفعلوا ولن تفعلوا.',
'15.1':'Sonu mu‘tel muzâri fiil, sonunun hazfıyla meczûm olur: لم يغزُ، لم يخشَ، لم يرمِ.',
'15.3':'Fasıl: غلامي ve الفتى gibi kelimelerde bütün harekeler takdîr olunur; ikincisine maksûr denir. القاضي gibilerde damme ve kesre takdîr olunur; ona menkûs denir. يخشى’da damme ve fetha, يدعو ve يقضي’de yalnız damme takdîr olunur. إنّ القاضيَ لن يقضيَ ولن يدعوَ’da fetha görünür.',
'16.0':'Fasıl: Muzâri, nâsıb ve câzimden boş olunca merfû olur: يقومُ زيدٌ.',
'17.0':'Muzâri لن ile mansûb olur: لن نبرحَ.',
'17.2':'Masdariyye كي ile de mansûb olur: لكيلا تأسوا.',
'17.4':'Başta gelen, gelecek bildiren ve (fiile) bitişik ya da araya yalnız kasem girmiş إذن ile de mansûb olur: إذن أكرمَك، إذن والله نرميَهم بحرب.',
'17.6':'Masdariyye أن ile de mansûb olur: açık olarak (أن يغفرَ لي) — ancak ilim bildiren bir fiilden sonra gelmemelidir (علم أن سيكون منكم مرضى); zan fiilinden sonra gelirse iki vecih câizdir (وحسبوا أن لا تكون فتنة). Câizen gizli olarak: halis bir isimden sonra gelen atf harfinden sonra (ولبس عباءة وتقرَّ عيني) ve lâmdan sonra (لتبيّنَ للناس); لئلا يعلم ve لئلا يكون gibi yerlerde ise yalnız açık gelir; وما كان الله ليعذّبَهم gibi yerlerde yalnız gizli olur. Gelecek bildiren حتى’dan sonra (حتى يرجعَ إلينا موسى), “ilâ” mânâsındaki أو’dan sonra (أو أُدركَ المنى) ve “illâ” mânâsındaki أو’dan sonra da vâciben gizlidir. Ayrıca halis nefy veya fiille yapılan talepten sonra gelen sebebiyye fâsı ve maiyye vâvından sonra: لا يُقضى عليهم فيموتوا، ويعلمَ الصابرين، ولا تطغوا فيه فيحلَّ، لا تأكل السمك وتشربَ اللبن.',
'17.15':'Talepten sonra fâ düşer ve ceza kastedilirse muzâri meczûm olur: قل تعالوا أتلُ. Nehiyden sonra cezmin şartı, onun yerine “in lâ” konulabilmesidir: لا تدنُ من الأسد تسلمْ (yaklaşmazsan kurtulursun); يأكلْك denmez. Muzâri ayrıca لم (لم يلدْ ولم يولدْ), لمّا (لمّا يقضِ) ve talep lâmı ile talep lâsı ile meczûm olur (لينفقْ، ليقضِ، لا تشركْ، لا تؤاخذْنا). إنْ، إذ ما، أين، أنّى، أيّان، متى، مهما، من، ما، حيثما iki fiili cezmeder: إن يشأ يذهبْكم، من يعملْ سوءًا يُجزَ به، ما ننسخْ من آية أو ننسِها نأتِ بخير منها. Birincisine şart, ikincisine cevap ve ceza denir. Cevap edata doğrudan gelmeye elverişli değilse fâ alır (وإن يمسسك بخير فهو على كل شيء قدير) veya müfâcee إذا’sı alır (وإن تصبهم سيئة… إذا هم يقنطون).',
'21.0':'Fasıl: İsim iki çeşittir. Nekre: var olan (رجل) veya varsayılan (شمس) bir cinste yaygın olandır. Ma‘rife altıdır: Birincisi zamir; mütekellim, muhâtab veya gâibe delâlet edendir. Zamir ya gizlidir —أقوم ve نقوم’da vâciben, زيد يقوم’da câizen takdîr edilen gibi— ya da açıktır; açık zamir ya muttasıldır (قمتُ’nin tâsı, أكرمك’in kâfı, غلامه’nin hâsı) ya munfasıl (أنا، هو، إيّاي). Bitişik gelmesi mümkünken ayrık getirilmez; ancak سلنيه’deki hâda (zayıf olarak) ve ظننتكه ile كنته’de (tercihen) ayrık gelebilir.',
'24.0':'Sonra alem gelir: ya şahıs alemidir (زيد) ya cins alemi (أسامة: aslan). Ya isimdir (verdiğimiz örnekler gibi), ya lakap (زين العابدين، قُفّة), ya künye (أبو عمرو، أم كلثوم). Lakap isimden sonra gelir; mutlak olarak ona tâbi olur, ikisi de müfred ise izâfetle mecrûr da olabilir: سعيدُ كرزٍ.',
'25.0':'Sonra ism-i işâret gelir: müzekker için ذا; müennes için ذي، ذه، تي، ته، تا; tesniye için ref‘de elifle, cer ve nasbda yâ ile ذان ve تان; her ikisinin cemi için أولاء. Uzaktaki için lâmsız veya lâmlı kâf ile kullanılır; ancak tesniyede mutlak olarak, cemide onu medli okuyanların lehçesinde ve başına tenbîh hâsı gelenlerde lâm getirilmez.',
'26.0':'Sonra ism-i mevsûl gelir: الذي، التي; ref‘de elifle, cer ve nasbda yâ ile اللذان، اللتان; müzekker cemi için her hâlde yâ ile الذين ve الألى; müennes cemi için اللائي، اللاتي. Hepsinin mânâsında من، ما، أيّ; tafdîl dışındaki sarih vasıfta el- (الضارب، المضروب); Tayy lehçesinde ذو; istifhâm مَن ve مَا’sından sonra ذا. El-’in sılası vasıftır; diğerlerinin sılası ya mevsûle uygun bir zamir (âid) taşıyan haber cümlesidir —bu zamir hazfedilebilir: أيّهم أشدّ، وما عملت أيديهم، فاقض ما أنت قاض، ويشرب مما تشربون— ya da hazfedilmiş استقرّ’ya müteallak tam zarf veya câr-mecrûrdur.',
'27.2':'Sonra edatlı isim gelir; edat Halîl ve Sîbeveyh’e göre (yalnız lâm değil) أل’dir — Ahfeş buna muhaliftir. Ahd için olur (في زجاجة؛ الزجاجة، جاء القاضي), cins için (أهلك الناسَ الدينارُ والدرهمُ، وجعلنا من الماء كلَّ شيء حي), cinsin fertlerini kuşatmak için (وخُلق الإنسان ضعيفًا) veya sıfatlarını kuşatmak için (زيد الرجلُ: Zeyd tam adamdır).',
'28.3':'Lâmı mîme çevirmek (am-) Himyer lehçesidir.',
'28.5':'Bunlardan birine muzâf olan isim de ma‘rifedir ve derecesi muzâf ileyhine göredir; ancak zamire muzâf olan alem derecesindedir.',
'30.0':'Mübtedâ ve haber merfûdur: اللهُ ربُّنا، محمدٌ نبيُّنا.',
'30.2':'Mübtedâ umum veya tahsis bildirirse nekre olabilir: ما رجلٌ في الدار، أإلهٌ مع الله، ولعبدٌ مؤمنٌ خيرٌ من مشرك، خمسُ صلواتٍ كتبهنّ الله.',
'30.4':'Haber, bir râbıtı olan cümle olabilir: زيدٌ أبوه قائم، ولباسُ التقوى ذلك خير، الحاقةُ ما الحاقة، زيدٌ نعم الرجل; قل هو الله أحد gibi yerlerde râbıt gerekmez.',
'30.7':'Zaman ismi zata haber yapılmaz; “الليلة الهلال” gibi sözler te’vil edilir.',
'30.9':'İstifhâm veya nefye dayanan vasfın merfûu haberin yerini tutar: أقاطنٌ قومُ سلمى، ما مضروبٌ العمران.',
'30.11':'Haber birden çok olabilir: وهو الغفور الودود.',
'30.13':'Haber öne geçebilir: في الدار زيدٌ، أين زيدٌ.',
'30.15':'Mübtedâ da haber de hazfedilebilir: سلامٌ قومٌ منكرون — yani “selâm size; siz tanınmayan kimselersiniz.”',
'30.17':'Haberin hazfı şu yerlerde vâcibdir: لولا’nın ve sarih kasemin cevabından önce, haber olması imkânsız hâlden önce ve sarih beraberlik vâvından sonra: لولا أنتم لكنّا مؤمنين، لعمرُك لأفعلنّ، ضربي زيدًا قائمًا، كلُّ رجلٍ وضيعتُه.',
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
