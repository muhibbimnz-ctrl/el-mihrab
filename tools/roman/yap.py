# tools/roman/<id>.py + <id>_sozluk.txt -> data/roman/<id>.json ve data/roman/liste.json
import json,re,importlib.util,sys
H=re.compile(r'[ً-ْٰـ]')
def norm(w,dil):
    if dil=='en':
        w=w.lower().strip("'\".,!?;:");return w[:-2] if w.endswith("'s") else w
    return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))
liste=[]
for id in ['sindbad','hamama','hayy','tuti','sohrab','mantik','prince','crusoe','carol']:
    sp=importlib.util.spec_from_file_location('m',f'tools/roman/{id}.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    K=dict(m.KITAP);dil=K['dil']
    G={}
    for ln in open(f'tools/roman/{id}_sozluk.txt',encoding='utf-8'):
        if '=' in ln:k,v=ln.rstrip('\n').split('=',1);G[k.strip()]=v.strip()
    eks=[]
    for _,_,ss in m.B:
        for a,_ in ss:
            for w in (re.findall(r"[A-Za-z']+",a) if dil=='en' else a.split()):
                n=norm(w,dil)
                if n and n not in G and n not in eks:eks.append(n)
    assert not eks,(id,eks)
    K['bolumler']=[{'b':b,'tr_b':tb,'c':[[a,t] for a,t in ss]} for b,tb,ss in m.B];K['sozluk']=G
    json.dump(K,open(f'data/roman/{id}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    liste.append({k:K[k] for k in ['id','dil','seviye','baslik','tr_baslik','yazar']}|{'bolum':len(m.B)})
    print(id,len(m.B),'bölüm',len(G),'kelime')
json.dump(liste,open('data/roman/liste.json','w',encoding='utf-8'),ensure_ascii=False)
