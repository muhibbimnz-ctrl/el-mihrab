# Romanlarda sözlük kapsamı ölçümü (exec /tmp/sz/cand.py yerine tools/dil/ar_aday.py kullanın)
import json,re,collections,os
exec(open('/tmp/sz/cand.py').read())
os.chdir('/home/claude/el-mihrab')
H=re.compile('[ً-ْٰـ]')
def norm(w):return H.sub('',re.sub('[«»،.؟!:؛()\\-"]','',w))
def hz(w):return re.sub('[إأآٱ]','ا',w).replace('ى','ي').replace('ي','ی').replace('ك','ک').replace('ة','ه')
import sys
S=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'data/roman/sozluk_ar.json'))
O={}
for k,v in S.items():
    n=norm(k);O.setdefault(n,v);O.setdefault('~'+hz(n),v)
def bul(n,G):
    if n in G:return 1
    for x in cand(n):
        if x in G or '~'+hz(x) in G:return 1
    return 0
L=[k for k in json.load(open('data/roman/liste.json')) if k['dil']=='ar']
tot=fnd=0;miss=collections.Counter()
for k in L:
    b=json.load(open('data/roman/%s.json'%k['id']));G=dict(O)
    for kk,v in (b.get('sozluk') or {}).items():
        n=norm(kk);G[n]=v;G.setdefault('~'+hz(n),v)
    for bo in b['bolumler']:
        for c in bo['c']:
            for p in c[0].split():
                n=norm(p)
                if not n or not re.search('[ء-ي]',n):continue
                tot+=1
                if bul(n,G):fnd+=1
                else:miss[n]+=1
print('kapsam %%%.2f eksik tekil %d'%(100*fnd/tot,len(miss)))
json.dump(miss.most_common(),open('/tmp/sz/miss2.json','w'),ensure_ascii=False)
