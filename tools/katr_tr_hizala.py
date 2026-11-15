import json,re
def norm(s):
    s=re.sub(r'[ً-ْٰـ]','',s); s=re.sub('[أإآ]','ا',s); s=s.replace('ة','ه').replace('ى','ي')
    return re.findall(r'[ء-ي]+',s)
S=json.load(open('data/kitap/serhkatr.json')); K=json.load(open('data/kitap/katr.json'))
segs=[]
for b in S['bolumler']:
    for t,p,tr in zip(b['pt'],b['p'],b['tr']):
        if t=='m' and tr: segs.append((set(norm(p)),norm(p),tr))
kp=[(bi,pi,norm(p)) for bi,b in enumerate(K['bolumler']) for pi,p in enumerate(b['p'])]
def big(w): return set(zip(w,w[1:]))
assign={}
for si,(ws,wl,tr) in enumerate(segs):
    sb=big(wl); best=None;bs=0
    for bi,pi,w in kp:
        kb=big(w)
        if not kb or not sb: continue
        sc=len(sb&kb)/len(sb)
        if sc>bs: bs=sc;best=(bi,pi)
    if bs>=0.35: assign.setdefault(best,[]).append(tr)
cov=0
for bi,b in enumerate(K['bolumler']):
    b['tr']=['']*len(b['p'])
    for pi in range(len(b['p'])):
        if (bi,pi) in assign: b['tr'][pi]=' '.join(dict.fromkeys(assign[(bi,pi)])); cov+=1
json.dump(K,open('data/kitap/katr.json','w'),ensure_ascii=False,separators=(',',':'))
print('kapsanan',cov,'/',len(kp),'seg atanan',sum(len(v) for v in assign.values()),'/',len(segs))
for bi,b in enumerate(K['bolumler']):
    for pi,p in enumerate(b['p']):
        if not b['tr'][pi]: print(f'{bi}.{pi}|{p}')
EL={
'0.2':'İsim iki çeşittir:',
'0.3':'1) Mu‘reb: kendisine giren âmiller sebebiyle sonu değişendir; زيد gibi.',
'0.5':'Fiil ise üç kısımdır:',
'0.6':'1) Mâzî: sâkin te’nîs tâsıyla tanınır. Binâsı fetha üzeredir (ضرب); vâv-ı cemâatle dammeli (ضربوا), mütehharrik merfû zamirle sâkin olur (ضربتُ). En doğru görüşe göre نعم، بئس، عسى ve ليس de mâzîdendir.',
'0.7':'2) Emir: talebe delâlet edip muhâtaba yâsını kabul etmesiyle tanınır. Binâsı sükûn üzeredir (اضربْ); mu‘tel olan sonunun hazfı üzere (اغزُ، اخشَ، ارمِ), قوما gibiler —',
'0.8':'— ve قوموا، قومي ise nûnun hazfı üzere mebnîdir. Temîm lehçesinde هلمّ, en doğru görüşe göre هاتِ ve تعالَ de emirdendir.',
'0.12':'Fasıl: İ‘râbın çeşitleri dörttür.',
'0.19':'“Bir kavmin mızrağını sıktığımda, boğumlarını kırardım; ya da (mızrak) doğrulana kadar.” (أو burada “illâ” mânâsındadır.)',
'0.21':'إنْ، إذ ما، أيّ، أين، أنّى، أيّان، متى، مهما، من، ما، حيثما iki fiili cezmeder: إن يشأ يذهبْكم، من يعملْ سوءًا يُجزَ به، ما ننسخْ من آيةٍ أو —',
'0.22':'— ننسِها نأتِ بخيرٍ منها.',
'0.23':'Birincisine şart, ikincisine cevap ve ceza denir. Cevap edata doğrudan gelmeye elverişli değilse fâ alır (وإن يمسسك بخير فهو على كل شيء قدير) ya da müfâcee إذا’sı alır (وإن تصبهم سيئة بما قدّمت أيديهم إذا هم يقنطون).',
'0.24':'Fasıl: İsim iki çeşittir.',
'2.3':'“Teselli bul; yeryüzünde hiçbir şey bâkî değildir; Allah’ın takdirinden koruyacak bir sığınak da yoktur.” (lâ, leyse gibi amel etmiştir.)',
'2.8':'Üçüncü çeşit: kalbî fiiller olan ظنّ، رأى، حسب، درى، خال، زعم، وجد، علم. Bunlar (mübtedâ ile haberi) iki mef‘ûl olarak nasbeder; şöyle:',
'2.9':'“Allah’ı her şeyden büyük gördüm (bildim).”',
'2.10':'Sona geçerlerse ilgâ (amelsiz bırakma) tercih edilir;',
'2.11':'“Kavim ardımda, sandım” gibi; araya girerlerse ilgâ ile amel eşittir; şöyle:',
'2.12':'“Recez şiirlerinde alçaklık ve zayıflık olduğunu sandım.”',
'5.0':'زيدًا ضربتُه، ضربتُ أخاه veya مررتُ به gibi ifadelerde Zeyd’i mübtedâ olarak merfû okumak câizdir, o zaman sonraki cümle haberdir; ya da hazfı vâcib olan ضربتُ، أهنتُ، جاوزتُ takdiriyle mansûb okumak câizdir, o zaman sonraki cümlenin i‘râbta yeri yoktur. (Devamında nasbın tercih edildiği, vâcib olduğu, ref‘in vâcib olduğu ve ikisinin eşit olduğu yerler sayılır.)',
'6.1':'“Dostlar bana cefâ etti, ben ise onlara cefâ etmedim.” (İkinci âmil amel ettirilmiş, birinciye yalnız merfû zamir verilmiştir.)',
'6.2':'Şu söz ise bu bâbdan değildir:',
'6.3':'“Bana az bir mal yeterdi, (fazlasını) istemedim.”',
'6.4':'çünkü (tenâzu‘ sayılırsa) mânâ bozulur.',
'7.8':'“Seni anınca beni bir titreme alır.” (Sebep bildiren isim, şartı eksik olduğu için lâm ile mecrûr gelmiştir.)',
'7.9':'“Geldim; o ise uyumak için elbiselerini çıkarmıştı.”',
'8.1':'“Meyye’nin ıssız kalmış bir harabesi var.” (Hâl, sâhibi nekre olduğu için öne geçmiştir.)',
'8.3':'Şâirin şu sözü de (tekîd için gelen temyîzdir):',
'8.4':'“…din olarak yaratılmışların dinlerinin en hayırlısındandır.”',
'8.5':'Şu da ondandır:',
'8.6':'“Onların aygırı ne kötü aygırdır!”',
'8.7':'— Sîbeveyh buna muhaliftir.',
'8.8':'İllâ ile istisnâ edilen, tam ve müsbet sözden ise mansûbdur: فشربوا منه إلا قليلًا منهم. Müsbetlik yoksa muttasıl istisnâda bedel tercih edilir: ما فعلوه إلا قليلٌ منهم.',
'8.9':'Munkatı‘ istisnâda Temîmoğullarına göre nasb tercih edilir, Hicazlılara göre vâcibdir: ما لهم به من علمٍ إلا اتّباعَ الظنّ. Müstesnâ öne geçerse ikisinde de nasb olur; şâirin şu sözü gibi:',
'8.10':'“Benim Âl-i Muhammed’den başka taraftarım, hak mezhepten başka mezhebim yoktur.”',
'8.11':'Söz tam değilse âmillere göre i‘râb alır: وما أمرُنا إلا واحدةٌ; buna müferrağ denir. غير ve سوى ile de istisnâ edilir; bunlar sonrakini cerreder ve illâdan sonraki ismin i‘râbını alır. خلا، عدا ve حاشا nasb veya cer eder; ما خلا، ما عدا، ليس ve لا يكون ise yalnız nasbeder.',
'10.2':'“Dikkat edin, kişinin kendine zulmetmesi apaçıktır.” (Masdar muzâf olarak amel etmiştir.)',
'10.3':'Tenvînli masdarın amel etmesi daha kıyâsîdir: أو إطعامٌ في يومٍ ذي مسغبةٍ (يتيمًا). El-’li olarak amel etmesi şâzdır: “İlâhına kötülük eden kimseye verilen rızka şaştım”, “Bindiğin şeyin sırtından nasıl sakınılır?”',
'11.3':'Tekîd ya lafzîdir; şöyle:',
'11.4':'“Kardeşine (sarıl), kardeşine! Kardeşi olmayan kimse…”',
'11.5':'Ve şöyle:',
'11.6':'“Arkadan gelenler sana yetişti, yetişti; dur, dur!”',
'11.7':'Ve şöyle:',
'11.8':'“Hayır, hayır! Büseyne’nin sevgisini açığa vurmam; o…”',
'11.10':'“Keşke bütün bir yılın sayısı Receb olsaydı!” (Nekreye tekîd nâdirdir.)',
'11.12':'“Ben Bişr el-Bekrî’yi (yerde) bırakanın oğluyum.” (بشر atf-ı beyândır, bedel olamaz.)',
'11.13':'Ve şâirin şu sözü:',
'11.14':'“Ey iki kardeşimiz Abdüşems ve Nevfel!”',
'13.0':'İsmin munsarif olmasına engel olan sebepler dokuzdur; şu beyit bunları toplar:',
'13.1':'“Vezin, terkîb, ucme, ta‘rîf, adl, vasf, cem‘, (elif-nûn) ziyâdesi ve te’nîs.”',
}
K=json.load(open('data/kitap/katr.json')); m=0
for bi,b in enumerate(K['bolumler']):
    for pi in range(len(b['p'])):
        k=f'{bi}.{pi}'
        if k in EL and not b['tr'][pi]: b['tr'][pi]=EL[k]; m+=1
json.dump(K,open('data/kitap/katr.json','w'),ensure_ascii=False,separators=(',',':'))
print('elle',m, 'kalan',[f'{bi}.{pi}' for bi,b in enumerate(K['bolumler']) for pi in range(len(b['p'])) if not b['tr'][pi]])
