# Uzun siyer kitabı: tools/siyer/kitap/NN.txt → data/siyer/kitap.json
# Bölüm dosyası: ilk satır "# Başlık | tarih | yer-id | olay-id(isteğe bağlı)", ardından her satır bir paragraf.
import json,os,re,glob,importlib.util
D=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(os.path.dirname(D))
sp=importlib.util.spec_from_file_location('sy',os.path.join(D,'yap.py'))
src=open(os.path.join(D,'yap.py'),encoding='utf-8').read()
ns={'re':re};exec(src[src.index('GL={'):src.index('out=[];AY={}')],ns)
glosla=ns['glosla']
sp2=importlib.util.spec_from_file_location('o',os.path.join(D,'olaylar.py'));o=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(o)
OL={x['id'] for x in o.O}
plan=[]
for satir in open(os.path.join(D,'kitap','plan.txt'),encoding='utf-8'):
    if satir.startswith('#') or ':' not in satir: continue
    don,lst=satir.split(':',1)
    for p in lst.split('·'):
        p=p.strip();n,b=p.split(' ',1);plan.append([int(n),b.strip(),don.strip()])
B=[];top=0
for f in sorted(glob.glob(os.path.join(D,'kitap','[0-9][0-9]*.txt'))):
    t=open(f,encoding='utf-8').read().strip().split('\n')
    h=[x.strip() for x in t[0].lstrip('#').split('|')]
    assert len(h)>=3,f
    yer=h[2];olay=h[3] if len(h)>3 else ''
    assert yer in o.YER,(f,yer)
    assert not olay or olay in OL,(f,olay)
    kul=set();par=[glosla(p.strip(),kul) for p in t[1:] if p.strip()]
    k=len(re.sub(r'\{([^|{}]+)\|[^{}]+\}',r'\1',' '.join(par)).split());top+=k
    n=os.path.basename(f)[:-4]
    B.append(dict(n=n,baslik=h[0],tarih=h[1],yer=yer,olay=olay,metin=par,kelime=k))
yazili={int(re.match(r'\d+',b['n']).group()) for b in B}
for p in plan: p.append(p[0] in yazili)
json.dump(dict(bolum=B,plan=plan,kelime=top,sayfa=round(top/250)),open(os.path.join(R,'data/siyer/kitap.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(B),'bölüm,',top,'kelime ≈',round(top/250),'sayfa; plan',len(plan))
