# tools/roman/<id>.py + <id>_sozluk.txt -> data/roman/<id>.json ve data/roman/liste.json
import json,re,importlib.util,sys
H=re.compile(r'[ً-ْٰـ]')
def norm(w,dil):
    if dil=='en':
        w=w.lower().strip("'\".,!?;:");return w[:-2] if w.endswith("'s") else w
    return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))
liste=[]
sys.path.insert(0,'tools/roman');import kitaplar
DIL=kitaplar.DIL()
for id in [i for l in [kitaplar.SIRA] for i in l if any(i in v for v in DIL.values())]:
    sp=importlib.util.spec_from_file_location('m',f'tools/roman/{id}.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    import glob,os
    _p=sorted(glob.glob(f'tools/roman/{id}_[0-9]*.py'),key=lambda x:int(re.findall(r'_(\d+)\.py$',x)[0]))
    if _p and id!='sindbad':
        m.B=[]
        for f in _p:
            sp=importlib.util.spec_from_file_location('p',f);q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q);m.B+=q.B
    K=dict(m.KITAP);dil=K['dil']
    G={}
    # aynı dildeki diğer romanların sözlükleri ortak yedek olarak kullanılır; kitabın kendi sözlüğü önceliklidir
    for _id in DIL[dil]:
        if not __import__('os').path.exists(f'tools/roman/{_id}_sozluk.txt'):continue
        if _id==id:continue
        for ln in open(f'tools/roman/{_id}_sozluk.txt',encoding='utf-8'):
            if '=' in ln:k,v=ln.rstrip('\n').split('=',1);G.setdefault(k.strip(),v.strip())
    _O={}
    for ln in open(f'tools/roman/{id}_sozluk.txt',encoding='utf-8'):
        if '=' in ln:k,v=ln.rstrip('\n').split('=',1);_O[k.strip()]=v.strip()
    G.update(_O)
    eks=[]
    for _,_,ss in m.B:
        for a,_ in ss:
            for w in (re.findall(r"[A-Za-z']+",a) if dil=='en' else a.split()):
                n=norm(w,dil)
                if n and n not in G and n not in eks:eks.append(n)
    assert not eks,(id,eks)
    K['bolumler']=[{'b':b,'tr_b':tb,'c':[[a,t] for a,t in ss]} for b,tb,ss in m.B];K['sozluk']=G
    json.dump(K,open(f'data/roman/{id}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    if id not in getattr(kitaplar,'GIZLI',[]):
        liste.append({k:K[k] for k in ['id','dil','seviye','baslik','tr_baslik','yazar']}|{'bolum':len(m.B)})
    print(id,len(m.B),'bölüm',len(G),'kelime')
import uzun as _U
for _i in getattr(kitaplar,'UZUN',[]):
    _e=_U.kur(_i)
    if _e:liste.insert(0,_e)
json.dump(liste,open('data/roman/liste.json','w',encoding='utf-8'),ensure_ascii=False)
