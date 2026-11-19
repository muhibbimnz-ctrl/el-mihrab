# Hadis Dirâsesi verisini üretir: data/hadis/erbain.json ve data/hadis/bais.json
import json,re,glob,os,importlib.util,sys
D=os.path.dirname(os.path.abspath(__file__))
def yukle(p):
    sp=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
R=yukle(os.path.join(D,'rical.py')).R
H=[]
for p in sorted(glob.glob(os.path.join(D,'erbain*.py'))): H+=yukle(p).H
H.sort(key=lambda x:x['n'])
B=yukle(os.path.join(D,'bais.py')).N
anah={}
for n,k,al,*_ in B:
    for x in [k]+al: anah[x]=n
txt=json.dumps(H,ensure_ascii=False)
eks=[]
for r in set(re.findall(r'\{r:([a-z0-9_]+)\|',txt))|{i for h in H for i in h.get('sened',[])}:
    if r not in R: eks.append('râvî:'+r)
for t in set(re.findall(r'\{t:([a-z0-9_]+)\|',txt+json.dumps(R,ensure_ascii=False)))|{d[0] for h in H for d in h.get('derece',[])}:
    if t not in anah: eks.append('terim:'+t)
assert not eks,eks
os.makedirs('data/hadis',exist_ok=True)
E={'kitap':'İmam Nevevî, el-Erbaûn (Kırk Hadis)','kisaAd':'Kırk Hadis',
 'aciklama':'Her hadisin altında şerh, i‘râb, belâgat, garîb, meâl, vürûd sebebi, tahrîc, sened ve fıkıh panelleri vardır. Altı çizili râvî ve usûl terimlerine dokunun.',
 'yakinda':'' if len(H)>=42 else f'Şu an {len(H)} hadis hazır; kalan hadisler eklenmeye devam ediyor (toplam 42).',
 'h':H,'rical':{k:dict(ad=v[0],ar=v[1],v=v[2],**{'not':v[3]}) for k,v in R.items()}}
json.dump(E,open('data/hadis/erbain.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
BB={'kitap':'İbn Kesîr, İhtisâru Ulûmi’l-Hadîs (el-Bâis el-Hasîs)',
 'aciklama':'İbnü’s-Salâh’ın Mukaddime’sindeki 65 nev‘i İbn Kesîr’in tertibiyle özetler. Arapça tanımlar klasik usûl kaynaklarındaki tanımlardır; Türkçe açıklamalar el-Mihrâb’ın özetidir (Ahmed Şâkir’in şerh notları alınmamıştır).',
 'nev':[dict(n=n,k=k,al=al,ar=ar,tr=tr,tanim=ta,ozet=oz,ornek=orn) for n,k,al,ar,tr,ta,oz,orn in B]}
json.dump(BB,open('data/hadis/bais.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(H),'hadis,',len(R),'râvî,',len(B),'nev')
