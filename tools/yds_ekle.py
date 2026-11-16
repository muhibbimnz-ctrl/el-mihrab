import json
from collections import Counter
def Q(s,k,d): return {'s':s,'k':k,'d':d,'a':''}
def T(id,alan,b,ab,sv,ar,tr,soz,sor):
    assert len(ar)==len(tr),(id,len(ar),len(tr))
    return dict(id=id,alan=alan,baslik=b,ar_baslik=ab,konu=b,seviye=sv,ar=ar,tr=tr,sozluk=soz,sorular=sor)
def ekle(Y):
    p='data/modern/modern.json'; M=json.load(open(p)); ids={m['id'] for m in M['metinler']}
    for y in Y:
        assert y['id'] not in ids, y['id']
        M['metinler'].append(y); ids.add(y['id'])
    json.dump(M,open(p,'w'),ensure_ascii=False,indent=0)
    print(len(M['metinler']),sorted(Counter(m['alan'] for m in M['metinler']).items()))
