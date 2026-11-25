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
ARALIK={'kuduri':{'Tahâret':(1,6),'Namaz':(6,26),'Zekât':(26,37),'Oruç':(37,39),'Hac':(39,46),'Muâmelât':(46,80),'Nikâh ve talâk':(80,90),'Cinâyât ve hadler':(95,104),'Kurban ve av':(104,106),'Yeminler':(106,107),'Ferâiz':(116,119),'Dava ve şahitlik':(107,111),'Siyer ve cihad':(113,115)},
 'bidaye':{'Tahâret':(0,31),'Namaz':(31,101),'Zekât':(101,121),'Oruç':(121,134),'Hac':(134,167),'Yeminler':(167,179),'Kurban ve av':(179,197),'Nikâh ve talâk':(197,270),'Muâmelât':(270,375),'Ferâiz':(375,394),'Cinâyât ve hadler':(401,422),'Dava ve şahitlik':(422,432),'Siyer ve cihad':(150,167)},
 'ihtiyar':{'Tahâret':(4,139),'Namaz':(4,139),'Zekât':(139,172),'Oruç':(172,189),'Hac':(189,298),'Muâmelât':(298,550),'Nikâh ve talâk':(550,695),'Cinâyât ve hadler':(771,815),'Kurban ve av':(897,919),'Ferâiz':(994,1069)}}
DUR=set('في من على الى إلى عن ما به او أو و ثم لا ان أن هل حكم وقت قدر'.split())
def kok(w):
    w=an(w)
    for p in ('وال','بال','فال','لل','ال'):
        if w.startswith(p) and len(w)-len(p)>=3: return w[len(p):]
    return w
import math
PAR={}
def paragraflar(k,S):
    if k in PAR: return PAR[k]
    L=[];df={}
    for i,(t,tx) in enumerate(S):
        for p in tx.split('\n\n'):
            p2=p.replace('**','').strip();q=an(p2)
            if len(q)<40: continue
            W=set(kok(w) for w in re.findall(r'[ء-ي]+',q))
            L.append((i,p2,W))
            for w in W: df[w]=df.get(w,0)+1
    PAR[k]=(L,df);return PAR[k]
def esles(t,W):
    if t in W: return True
    return any(w.startswith(t) and len(w)-len(t)<=2 for w in W if len(w)>=len(t))
def ibare(k,S,rng,baslik,ifade):
    L,df=paragraflar(k,S);N=len(L)
    T=[kok(w) for w in baslik if an(w) not in DUR and len(kok(w))>=3]
    T=list(dict.fromkeys(T))
    if not T: return None
    idf={t:math.log((N+1)/(1+sum(v for w,v in df.items() if w==t or (w.startswith(t) and len(w)-len(t)<=2)))) for t in T}
    nadir=max(T,key=lambda t:idf[t]);gerek=min(2,len(T))
    rs=set(rng);en=(0,None,None)
    for i,p,W in L:
        if i not in rs: continue
        M=[t for t in T if esles(t,W)]
        if len(M)<gerek or nadir not in M: continue
        s=sum(idf[t] for t in M)-len(p)/4000
        if s>en[0]: en=(s,i,p)
    if en[1] is None: return None
    p=en[2]
    if len(p)>480:
        q=an(p);poz=[q.find(t) for t in T if t in q];ilk=min(poz) if poz else 0
        bas=max(0,ilk-160);son=min(len(p),bas+460)
        while bas>0 and p[bas]!=' ':bas-=1
        while son<len(p) and p[son]!=' ':son+=1
        p=('… ' if bas>0 else '')+p[bas:son].strip()+(' …' if son<len(p) else '')
    return en[1],p
import importlib.util as _iu
_sp=_iu.spec_from_file_location('ib',os.path.join(D,'ibare.py'));_ib=_iu.module_from_spec(_sp);_sp.loader.exec_module(_ib);IBX=_ib.IB
out=[]
assert len({x['id'] for x in TUM})==len(TUM),'yinelenen id'
YENI={'Talâk ve rada‘':'Talâk, iddet ve rada‘','Talâk ve iddet':'Talâk, iddet ve rada‘','Alışveriş ve cezalar':'Alışveriş ve akitler'}
for x in TUM:
    x['yol']=[x['yol'][0],YENI.get(x['yol'][1],x['yol'][1])]
    if x['id']=='sirkat': x['yol']=['Cinâyât ve hadler','Kısas ve hadler']
ALT=[('Tahâret',['Abdest','Abdesti bozan şeyler','Mest üzerine mesh','Gusül ve hayız','Sular ve necasetler','Teyemmüm']),
('Namaz',['Vakitler ve şartlar','Ezan ve kamet','Namazın kılınışı','Vitir, cemaat ve secdeler','Yolcu, cuma ve bayram','Kaza ve hasta namazı','İstiskâ ve küsûf','Cenaze']),
('Oruç',['Oruç']),('Zekât',['Zekât ve fıtır']),('Hac',['Hac']),('Kurban ve av',['Kurban','Yiyecekler']),
('Nikâh ve talâk',['Nikâh','Talâk, iddet ve rada‘']),('Muâmelât',['Alışveriş ve akitler','Selem ve istisnâ','Şirket ve mudârebe','Kira, rehin ve hibe','Borç ve para','Vekâlet, kefâlet ve sulh','Gasb, emanet ve hacr']),
('Cinâyât ve hadler',['Kısas ve hadler']),('Dava ve şahitlik',['Dava ve şahitlik']),('Siyer ve cihad',['Cihad ve barış']),('Yeminler',['Yemin']),('Ferâiz',['Miras'])]
SB=[a for a,_ in ALT];SA={a:l for a,l in ALT}
for x in TUM:
    assert x['yol'][1] in SA[x['yol'][0]],x['yol']
TUM=sorted(enumerate(TUM),key=lambda p:(SB.index(p[1]['yol'][0]),SA[p[1]['yol'][0]].index(p[1]['yol'][1]),p[0]))
TUM=[x for _,x in TUM]
for x in TUM:
    mt=[]
    for _mt in x['metin']:
        if len(_mt)==3:  # meseleler13: çözülmüş [kitap, bölüm, ifade] olduğu gibi korunur
            K.setdefault(_mt[0],json.load(open(f'data/fikih/{_mt[0]}.json',encoding='utf-8'))['s']);mt.append(list(_mt));continue
        k,ifade=_mt
        if isinstance(ifade,int):
            if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
            mt.append([k,ifade,'']);continue
        if k not in K: K[k]=json.load(open(f'data/fikih/{k}.json',encoding='utf-8'))['s']
        S=K[k];g=an(ifade);bul=None
        KB={'Tahâret':'الطهار','Namaz':'الصلا','Oruç':'الصوم','Zekât':'الزكا','Hac':'الحج','Kurban ve av':'الاضحي','Nikâh ve talâk':'النكاح','Muâmelât':'البيوع','Ferâiz':'الفرائض','Cinâyât ve hadler':'الجنايات','Yeminler':'الأيمان','Dava ve şahitlik':'الشهادات','Siyer ve cihad':'السير'}
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
    yeni=[]
    for k,i,q in mt:
        S=K[k]
        rng=range(*ARALIK[k][x['yol'][0]]) if k in ARALIK and x['yol'][0] in ARALIK[k] else range(len(S))
        yeni.append([k,i,q])
    y=dict(x);y['metin']=yeni
    if '_ibare' in y: y['ibare']=y.pop('_ibare')  # meseleler13: hazır ibare korunur
    ph=IBX.get(x['id'])
    if ph:
        S=K.setdefault('kuduri',json.load(open('data/fikih/kuduri.json',encoding='utf-8'))['s'])
        rng=range(*ARALIK['kuduri'][x['yol'][0]]) if x['yol'][0] in ARALIK['kuduri'] else range(len(S))
        bul=None
        for ii in rng:
            for p in S[ii][1].split('\n\n'):
                if an(ph) in an(p): bul=(ii,p.replace('**','').strip());break
            if bul:break
        if bul:
            ii,p=bul;q=an(p);j=q.find(an(ph))
            if len(p)>380:
                bas=max(0,j-120);son=min(len(p),bas+360)
                while bas>0 and p[bas]!=' ':bas-=1
                while son<len(p) and p[son]!=' ':son+=1
                p=('… ' if bas>0 else '')+p[bas:son].strip()+(' …' if son<len(p) else '')
            y['ibare']=['kuduri',ii,p,ph]
        else: print('ibare bulunamadı',x['id'])
    out.append(y)
json.dump(out,open('data/fikih/meseleler.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
AY={}
for x in out:
    for d in x['delil']:
        if d[0]=='ayet':
            k=d[2].split('#')[1]
            if [x['id'],x['baslik']] not in AY.setdefault(k,[]): AY[k].append([x['id'],x['baslik']])
json.dump(AY,open('data/fikih/ayet.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'mesele,',len(AY),'âyet')
