# data/fikih/meseleler.json: mesele kartları + Arapça metin bağlantıları (kitap bölüm indeksi)
import json,os,re,importlib.util
D=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('m',os.path.join(D,'meseleler.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
sp2=importlib.util.spec_from_file_location('m2',os.path.join(D,'meseleler2.py'));m2=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(m2)
HR=re.compile(r'[ً-ٰٟـ]')
def an(t):return re.sub('[أإآ]','ا',HR.sub('',t)).replace('ى','ي').replace('ة','ه')
K={}
out=[]
for x in m.M+m2.M:
    mt=[]
    for k,ifade in x['metin']:
        if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
        S=K[k];g=an(ifade);bul=None
        KB={'Tahâret':'الطهار','Namaz':'الصلا','Oruç':'الصوم','Zekât':'الزكا','Hac':'الحج','Kurban ve av':'الاضحي','Nikâh ve talâk':'النكاح','Muâmelât':'البيوع','Ferâiz':'الفرائض'}
        if k=='bidaye': KB['Kurban ve av']='الضحايا'
        if 'سرق' in g: KB['Muâmelât']='السرق'
        if g in ('الطلاق','الخلع','الرضاع','الثلاث'): KB['Nikâh ve talâk']='الطلاق' if g!='الرضاع' else 'الرضاع'
        kb=an(KB[x['yol'][0]])
        bas=next((i for i,(t,_) in enumerate(S) if kb in an(t)),None)
        if bas is None: bas=next((i for i,(t,tx) in enumerate(S) if kb in an(tx[:400])),0)
        if x['yol'][0]=='Tahâret': bas=0
        son=next((i for i in range(bas+1,len(S)) if 'كتاب' in an(S[i][0]) and kb not in an(S[i][0])),len(S))
        if x['yol'][0]=='Tahâret': son=next((i for i,(t,_) in enumerate(S) if i>0 and 'كتاب الصلا' in an(t)),len(S))
        if son-bas<3: son=min(len(S),bas+60)
        R=list(range(bas,son))
        for i in R:
            if g in an(S[i][0]): bul=i;break
        if bul is None:
            for i in R:
                if g in an(S[i][1]): bul=i;break
        if bul is None and x['yol'][0]!='Tahâret':
            bul=next((i for i,(t,_) in enumerate(S) if g in an(t)),None)
        if bul is None: bul=bas
        tam=g in an(S[bul][0]+' '+S[bul][1])
        mt.append([k,bul,ifade if tam else ''])
        if not tam: print('yaklaşık',x['id'],k,ifade,'->',S[bul][0][:40])
    y=dict(x);y['metin']=mt;out.append(y)
json.dump(out,open('data/fikih/meseleler.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'mesele')
