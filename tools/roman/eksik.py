# Kullanım: python3 tools/roman/eksik.py <id>  -> sözlükte olmayan kelimeleri listeler
import sys,re,glob,importlib.util
id=sys.argv[1]
H=re.compile(r'[ً-ْٰـ]')
sp=importlib.util.spec_from_file_location('m',f'tools/roman/{id}.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
dil=m.KITAP['dil']
def norm(w):
    if dil=='en':
        w=w.lower().strip("'\".,!?;:");return w[:-2] if w.endswith("'s") else w
    return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))
B=[]
ps=sorted(glob.glob(f'tools/roman/{id}_[0-9]*.py'))
if ps:
    for f in ps:
        sp=importlib.util.spec_from_file_location('p',f);q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q);B+=q.B
else:B=m.B
DIL={'ar':['sindbad','hamama','hayy'],'fa':['tuti','sohrab','mantik'],'en':['prince','crusoe','carol']}
G={l.split('=',1)[0].strip() for x in DIL[dil] for l in open(f'tools/roman/{x}_sozluk.txt',encoding='utf-8') if '=' in l}
eks=[]
for _,_,ss in B:
    for a,_ in ss:
        for w in (re.findall(r"[A-Za-z']+",a) if dil=='en' else a.split()):
            n=norm(w)
            if n and n not in G and n not in eks:eks.append(n)
print(len(eks));print(' '.join(eks))
