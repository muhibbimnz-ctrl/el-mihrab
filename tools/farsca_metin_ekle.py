# tools/fa_metinler*.py içindeki Farsça okuma metinlerini farsca.html'deki Günlük Hayat (T) / Akademik (A) / İslami İlimler (I)
# programlarına ders olarak ekler. Tekrar çalıştırılabilir.
import json,re,glob,importlib.util,random
F=[]
def _z(x):
    # '+' yarım boşluk (ZWNJ) yazımı
    if isinstance(x,str): return x.replace('+','\u200c')
    if isinstance(x,(list,tuple)): return type(x)(_z(i) for i in x)
    return x
for p in sorted(glob.glob('tools/fa_metinler*.py')):
    sp=importlib.util.spec_from_file_location('m',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);F+=_z(m.M)
out={'T':[],'A':[],'I':[]}
for x in F:
    prog,cat,fa_b,tr_b,sv,P,V,Qs=x
    allfa=[s for par in P for s,_ in par]
    VV=[[w,t,next((s for s in allfa if w in s),''),''] for w,t in V]
    mq=[]
    for i,(s,k,a) in enumerate(Qs):
        R=random.Random(fa_b+str(i));kk=k[1:];R.shuffle(kk);d=R.randrange(len(k));kk.insert(d,k[0]);mq.append([s,kk,d,a])
    out[prog].append({'c':cat,'en':fa_b,'tr':tr_b,'v':VV,'p':[[[s,t] for s,t in par] for par in P],'mq':mq,'sv':sv})
js='/*FA-METIN*/'+''.join(f'{k}.push.apply({k},{json.dumps(v,ensure_ascii=False,separators=(",",":"))});' for k,v in out.items())+'/*/FA-METIN*/\n'
import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from dil_veri import blok_yaz
blok_yaz('farsca','FA-METIN',js)
print({k:len(v) for k,v in out.items()})
