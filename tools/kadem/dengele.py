# Kadem içerik aracı. Kullanım: python3 tools/kadem/dengele.py
import json,glob,re,random,collections,sys
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','konu')
def sabit(q):
    c=q['c']
    if all(re.match(r'^(Yalnız|I|II|III|IV)\b',x) for x in c): return True
    if all(re.match(r'^[\d.,: ]+',x) for x in c): return True
    if re.search(r'sıralan|yer(lerinin)? değiştir|sırasıyla',q['s']): return True
    return False
for f in sys.argv[1:] or sorted(glob.glob(R+'/*.json')):
    d=json.load(open(f)); Q=d['sorular']
    cnt=collections.Counter(q['d'] for q in Q if sabit(q))
    rnd=random.Random(d['id'])
    for q in Q:
        if sabit(q): continue
        m=min(cnt[i] for i in range(5)); adaylar=[i for i in range(5) if cnt[i]==m]
        t=rnd.choice(adaylar); s=q['d']
        if t!=s:
            for k in ('c','ac'): q[k][s],q[k][t]=q[k][t],q[k][s]
            q['d']=t
        cnt[t]+=1
    json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
    print(f.split('/')[-1],dict(sorted(collections.Counter('ABCDE'[q['d']] for q in Q).items())))
