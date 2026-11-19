# data/fikih/meseleler.json: mesele kartları + Arapça metin bağlantıları (kitap bölüm indeksi)
import json,os,re,importlib.util
D=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('m',os.path.join(D,'meseleler.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
HR=re.compile(r'[ً-ٰٟـ]')
def an(t):return re.sub('[أإآ]','ا',HR.sub('',t)).replace('ى','ي').replace('ة','ه')
K={}
out=[]
for x in m.M:
    mt=[]
    for k,ifade in x['metin']:
        if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
        S=K[k];g=an(ifade);bul=None
        son=next((i for i,(t,_) in enumerate(S) if i>0 and 'كتاب الصلا' in an(t)),len(S));S=S[:son]
        # önce başlıkta, sonra metinde Tahâret kısmı içinde ara
        for i,(t,tx) in enumerate(S):
            if g in an(t): bul=i;break
        if bul is None:
            for i,(t,tx) in enumerate(S):
                if g in an(tx): bul=i;break
        mt.append([k,bul if bul is not None else 0,ifade])
        if bul is None: print('bulunamadı',x['id'],k,ifade)
    y=dict(x);y['metin']=mt;out.append(y)
json.dump(out,open('data/fikih/meseleler.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'mesele')
