# Abduh er-Râcihî, et-Tatbîku'n-Nahvî — kitabın konu sırası ve yöntemi (kural → tam i'râblı örnek → Kur'an alıştırması).
# Kitabın metni telifli olduğu için alınmamıştır; Arapça kural cümleleri, örnekler, Türkçe açıklama ve sorular el-Mihrâb için yazılmıştır.
import json,re
L=json.load(open('tools/tatbik_dersler.json',encoding='utf-8'))
KURAL=["الْكَلَامُ هُوَ اللَّفْظُ الْمُفِيدُ فَائِدَةً تَامَّةً، وَالْكَلِمَةُ ثَلَاثَةُ أَقْسَامٍ: اسْمٌ وَفِعْلٌ وَحَرْفٌ.",
"الْمُعْرَبُ مَا يَتَغَيَّرُ آخِرُهُ بِتَغَيُّرِ الْعَوَامِلِ الدَّاخِلَةِ عَلَيْهِ، وَالْمَبْنِيُّ مَا يَلْزَمُ آخِرُهُ حَالَةً وَاحِدَةً.",
"الْمُبْتَدَأُ اسْمٌ مَرْفُوعٌ يُبْتَدَأُ بِهِ الْكَلَامُ، وَالْخَبَرُ مَا تَتِمُّ بِهِ الْفَائِدَةُ مَعَ الْمُبْتَدَإِ، وَهُوَ مَرْفُوعٌ.",
"كَانَ وَأَخَوَاتُهَا أَفْعَالٌ نَاقِصَةٌ تَدْخُلُ عَلَى الْمُبْتَدَإِ وَالْخَبَرِ، فَتَرْفَعُ الْمُبْتَدَأَ وَيُسَمَّى اسْمَهَا، وَتَنْصِبُ الْخَبَرَ وَيُسَمَّى خَبَرَهَا.",
"إِنَّ وَأَخَوَاتُهَا حُرُوفٌ تَدْخُلُ عَلَى الْمُبْتَدَإِ وَالْخَبَرِ، فَتَنْصِبُ الْمُبْتَدَأَ وَيُسَمَّى اسْمَهَا، وَتَرْفَعُ الْخَبَرَ وَيُسَمَّى خَبَرَهَا.",
"الْفَاعِلُ اسْمٌ مَرْفُوعٌ يَأْتِي بَعْدَ فِعْلٍ مَبْنِيٍّ لِلْمَعْلُومِ، وَيَدُلُّ عَلَى مَنْ فَعَلَ الْفِعْلَ."]
tag=lambda s:re.sub(r'<[^>]+>','',s)
B=[];Q=[]
for i,l in enumerate(L):
    p=[l.get('k') or KURAL[i]];tr=[' '.join(tag(x) for x in l['x'])]
    for e in l['e']:
        p.append(e['s']+'. — '+' ؛ '.join(w[0]+': '+w[1] for w in e['w'])+'.')
        tr.append('“'+e['tr']+'” — '+' '.join('«'+w[0]+'»: '+w[2] for w in e['w']))
    B.append({'b':l['a'],'tr_b':l['t'],'p':p,'tr':tr})
    for q in l['q']:
        w=re.search(r'<i>(.*?)</i>',q['s']).group(1);ay=tag(q['s'])
        k=[q['o'][q['a']]]+[o for j,o in enumerate(q['o']) if j!=q['a']]
        Q.append({'b':i,'w':w,'s':'“'+ay+'” ('+q['ref']+') — «'+w+'» kelimesinin i‘râbı nedir?','k':k,'d':0,'a':tag(q['x'])})
out={'id':'tatbik','baslik':'et-Tatbîku’n-Nahvî','kaynak':'Dr. Abduh er-Râcihî (1937–2010), et-Tatbîku’n-Nahvî. Kitabın konu sırası ve yöntemi izlenmiştir; kitabın metni telifli olduğu için alınmamıştır. Arapça kural cümleleri, örnekler, tam i‘râblar, Türkçe açıklamalar ve Kur’an alıştırmaları el-Mihrâb için hazırlanmıştır. Toplam 21 bâb.','bolumler':B,'sorular':Q}
json.dump(out,open('data/kitap/tatbik.json','w'),ensure_ascii=False)
print(len(B),sum(len(b['p']) for b in B),len(Q))
