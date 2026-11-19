# Arama dizini: data/hadis/ara/<kitap>.json = [[ref, araplNorm, turkceNorm], ...]
import json,re,glob,os
HR=re.compile(r'[ً-ٰٟـۖ-ۭ‌-‏]')
def an(t):
    t=HR.sub('',t or '');t=re.sub('[أإآٱ]','ا',t).replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return re.sub(r'\s+',' ',re.sub(r'[^ء-ي\s]',' ',t)).strip()
TRM=str.maketrans('çşğıöüâîûÇŞĞIİÖÜÂÎÛ','csgiouaiucsgiiouaiu')
def tn(t):
    t=(t or '').translate(TRM).lower()
    return re.sub(r'\s+',' ',re.sub(r'[^a-z0-9\s]',' ',t)).strip()
KES=re.compile(r'(NEVEV[İI] ŞERH|DAVUDOĞLU|AÇIKLAMA|HAD[İI]S[İI]N FIKIH|BAZI HÜKÜMLER|Tekrar[ıi]?\s*:|Diğer [Tt]ahric|BURAYA TIKLA)')
os.makedirs('data/hadis/ara',exist_ok=True)
K=json.load(open('data/hadis/kutub.json',encoding='utf-8'));top=0
for b in K:
    k=b['k'];src=b.get('src','fa');R=[]
    if src=='fa':
        A=json.load(open(f'/tmp/ha/editions/ara-{k}1.min.json'))['hadiths']
        T={}
        if b['tr'] and os.path.exists(f'/tmp/ha/editions/tur-{k}.min.json'):
            for h in json.load(open(f'/tmp/ha/editions/tur-{k}.min.json'))['hadiths']:
                t=h['text'];m=KES.search(t);T[h['hadithnumber']]=tn((t[:m.start()] if m else t)[:1500])
        for h in A:
            n=h['hadithnumber']
            if h['text'].strip(): R.append([n,an(h['text']),T.get(n,'')])
    elif src=='hj':
        for f in glob.glob(f"/tmp/hj/db/by_chapter/{b['g']}/{k}/*.json"):
            sid=os.path.basename(f)[:-5]
            if sid not in [s[0] for s in b['b']]: continue
            for h in json.load(open(f))['hadiths']:
                R.append([[sid,h.get('idInBook') or h.get('id')],an(h.get('arabic','')),''])
    else:
        for s in b['b']:
            D=json.load(open(f"data/hadis/{k}/{s[0]}.json",encoding='utf-8'));H=D['h'] if isinstance(D,dict) else D
            for x in H: R.append([[s[0],x[0]],an(x[1]),''])
    if src!='fa':
        for r in R: r.pop() if r[2]=='' else None
    json.dump(R,open(f'data/hadis/ara/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    sz=os.path.getsize(f'data/hadis/ara/{k}.json');top+=sz;print(k,len(R),sz//1024,'KB')
print('toplam',top//1024//1024,'MB')
