# Sözlük kelimelerini köklerine ayırır -> data/roman/kok_ar.json {kök: [kelime,...]} (aynı kökten kelimeler için)
import re,json,collections
exec(open('tools/dil/beyit_esle.py').read().split("ES={};kul")[0])
def jsnorm(w):return re.sub('[إأآٱ]','ا',H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))).replace('ى','ي').strip()
M=collections.defaultdict(list)
for k in S:
    w=sk(k)
    if ' ' in w or len(w)<3: continue
    r=kokbul(w)
    if r: M[jsnorm(r)].append(k)
M={r:v for r,v in M.items() if len(v)>=2}
json.dump(M,open('data/roman/kok_ar.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(M),'kök',sum(len(v) for v in M.values()),'kelime')
