# Arapça sözlüğü genişletir: ar_ek_lugat.txt + 2 + 3 + ar_ek_isim.txt (elle yazılmış) + ar_hasat.json (uygulamadaki ders/metin sözlüklerinden toplanmış)
import json,re
H=re.compile('[ً-ٰٟـ]')
def n(w):return H.sub('',w).replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ٱ','ا').replace('ى','ي').strip()
p='data/roman/sozluk_ar.json';S=json.load(open(p));var={n(k) for k in S};ek=0
for ln in [l for f in ('tools/dil/ar_ek_lugat.txt','tools/dil/ar_ek_lugat2.txt','tools/dil/ar_ek_lugat3.txt','tools/dil/ar_ek_lugat4.txt','tools/dil/ar_ek_isim.txt') for l in open(f,encoding='utf-8')]:
    if ln.startswith('#') or '=' not in ln: continue
    k,v=ln.rstrip('\n').split('=',1);k=k.strip()
    if n(k) not in var: S[k]=v.strip();var.add(n(k));ek+=1
for k,v in json.load(open('tools/dil/ar_hasat.json')).items():
    if n(k) in var or len(v)>70 or len(n(k).split())>3 or len(n(k))<2: continue
    S[k]=v;var.add(n(k));ek+=1
json.dump(S,open(p,'w'),ensure_ascii=False,separators=(',',':'));print('eklendi',ek,'toplam',len(S))
