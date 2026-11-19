# data/fikih/meseleler.json: mesele kartları + Arapça metin bağlantıları (kitap bölüm indeksi)
import json,os,re,importlib.util
D=os.path.dirname(os.path.abspath(__file__))
import glob
TUM=[]
for f in sorted(glob.glob(os.path.join(D,'meseleler*.py')),key=lambda f:(len(f),f)):
    sp=importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f);mm=importlib.util.module_from_spec(sp);sp.loader.exec_module(mm);TUM+=mm.M
HR=re.compile(r'[ً-ٰٟـ]')
def an(t):return re.sub('[أإآ]','ا',HR.sub('',t)).replace('ى','ي').replace('ة','ه')
K={}
out=[]
assert len({x['id'] for x in TUM})==len(TUM),'yinelenen id'
YENI={'Talâk ve rada‘':'Talâk, iddet ve rada‘','Talâk ve iddet':'Talâk, iddet ve rada‘','Alışveriş ve cezalar':'Alışveriş ve akitler'}
for x in TUM:
    x['yol']=[x['yol'][0],YENI.get(x['yol'][1],x['yol'][1])]
    if x['id']=='sirkat': x['yol']=['Cinâyât ve hadler','Kısas ve hadler']
ALT=[('Tahâret',['Abdest','Abdesti bozan şeyler','Mest üzerine mesh','Gusül ve hayız','Sular ve necasetler','Teyemmüm']),
('Namaz',['Vakitler ve şartlar','Namazın kılınışı','Vitir, cemaat ve secdeler','Yolcu, cuma ve bayram','Kaza ve hasta namazı','Cenaze']),
('Oruç',['Oruç']),('Zekât',['Zekât ve fıtır']),('Hac',['Hac']),('Kurban ve av',['Kurban','Yiyecekler']),
('Nikâh ve talâk',['Nikâh','Talâk, iddet ve rada‘']),('Muâmelât',['Alışveriş ve akitler','Selem ve istisnâ','Şirket ve mudârebe','Kira, rehin ve hibe','Borç ve para']),
('Cinâyât ve hadler',['Kısas ve hadler']),('Yeminler',['Yemin']),('Ferâiz',['Miras'])]
SB=[a for a,_ in ALT];SA={a:l for a,l in ALT}
for x in TUM:
    assert x['yol'][1] in SA[x['yol'][0]],x['yol']
TUM=sorted(enumerate(TUM),key=lambda p:(SB.index(p[1]['yol'][0]),SA[p[1]['yol'][0]].index(p[1]['yol'][1]),p[0]))
TUM=[x for _,x in TUM]
for x in TUM:
    mt=[]
    for k,ifade in x['metin']:
        if isinstance(ifade,int):
            if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
            mt.append([k,ifade,'']);continue
        if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
        S=K[k];g=an(ifade);bul=None
        KB={'Tahâret':'الطهار','Namaz':'الصلا','Oruç':'الصوم','Zekât':'الزكا','Hac':'الحج','Kurban ve av':'الاضحي','Nikâh ve talâk':'النكاح','Muâmelât':'البيوع','Ferâiz':'الفرائض','Cinâyât ve hadler':'الجنايات','Yeminler':'الأيمان'}
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
        if bul is None and x['yol'][0]!='Tahâret':
            bul=next((i for i,(t,_) in enumerate(S) if g in an(t)),None)
        if bul is None:
            for i in R:
                if g in an(S[i][1]): bul=i;break
        if bul is None and x['yol'][0]!='Tahâret':
            bul=next((i for i,(t,tx) in enumerate(S) if g in an(tx)),None)
        if bul is None: bul=bas
        tam=g in an(S[bul][0]+' '+S[bul][1])
        mt.append([k,bul,ifade if tam else ''])
        if not tam: print('yaklaşık',x['id'],k,ifade,'->',S[bul][0][:40])
    y=dict(x);y['metin']=mt;out.append(y)
json.dump(out,open('data/fikih/meseleler.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
AY={}
for x in out:
    for d in x['delil']:
        if d[0]=='ayet':
            k=d[2].split('#')[1]
            if [x['id'],x['baslik']] not in AY.setdefault(k,[]): AY[k].append([x['id'],x['baslik']])
json.dump(AY,open('data/fikih/ayet.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'mesele,',len(AY),'âyet')
