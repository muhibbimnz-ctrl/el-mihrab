# Ahlak Dirâsesi verisi: tools/ahlak/konular*.py → data/ahlak/konular.json (+ hadis arama ve âyet denetimi)
import json,os,re,glob,importlib.util
from urllib.parse import quote
D=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(os.path.dirname(D))
TUM=[]
for f in sorted(glob.glob(os.path.join(D,'konular*.py'))):
    sp=importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);TUM+=m.K
assert len({x['id'] for x in TUM})==len(TUM)
SIRA=['Kalbin amelleri','Kalbin ve dilin hastalıkları','Kul hakları','Edepler ve gündelik hayat']
TUM=[x for _,x in sorted(enumerate(TUM),key=lambda p:(SIRA.index(p[1]['grup']),p[0]))]
K=json.load(open(os.path.join(R,'data/hadis/kutub.json')))
def an(t):
    t=re.sub('[ً-ٰـۖ-ۭ‌-‏]','',t);t=re.sub('[أإآٱ]','ا',t).replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return re.sub(r'\s+',' ',re.sub('[^ء-ي\\s]',' ',t)).strip()
C={};S=['bukhari','muslim','abudawud','tirmidhi','nasai','ibnmajah']
def kit(kap):
    if kap=='sitte':return S
    if kap=='tisa':return S+['malik','ahmed','darimi']
    if kap.startswith('k:'):return [kap[2:]]
    return [b['k'] for b in K]
hata=0;out=[];AY={}
for x in TUM:
    y=dict(x);hd=[]
    for et,q,kap,an_ in x['hadis']:
        W=an(q).split(' ');n=0
        for k in kit(kap):
            fp=os.path.join(R,f'data/hadis/ara/{k}.json')
            if not os.path.exists(fp):continue
            if k not in C:C[k]=json.load(open(fp))
            n+=sum(1 for r in C[k] if all(w in r[1] for w in W))
        if n==0 or n>80: print('hadis',x['id'],et,q,kap,n);hata+=1
        hd.append([et,'hadis.html#ara='+quote(q)+'&kap='+kap,an_])
    y['hadis']=hd;y['ayet']=[[a,'./#'+r,m] for a,r,m in x['ayet']]
    for a,r,m in x['ayet']: AY.setdefault(r,[]).append([x['id'],x['baslik']])
    out.append(y)
json.dump(out,open(os.path.join(R,'data/ahlak/konular.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
json.dump(AY,open(os.path.join(R,'data/ahlak/ayet.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'konu,',len(AY),'âyet, sorunlu',hata)
