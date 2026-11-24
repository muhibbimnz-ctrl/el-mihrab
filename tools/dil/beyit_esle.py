# Sözlük kelimelerini Lisânü'l-Arab şâhid beyitleriyle eşleştirir -> tools/dil/beyit_es.json {kelime_norm: beyit_id}, tools/dil/beyitler.json [beyit,kök]
import re,json,collections
H=re.compile('[ً-ٰٟـ]')
def n(w):return re.sub('[إأآٱؤئء]','ء',H.sub('',w)).replace('ى','ي').replace('ة','ه')
def sk(w):  # sözlük anahtarı normu (sozluk.html ile uyumlu olması gerekmez; eşleştirme için)
    return n(w).strip()
ZAYIF=set('اويء')
def guclu(r):return [c for c in n(r) if c not in ZAYIF]
def uyar(r,w):
    g=guclu(r);i=0
    for c in w:
        if i<len(g) and c==g[i]: i+=1
    return i==len(g) and len(g)>=2
PR=['وال','فال','بال','كال','لل','ال','و','ف','ب','ل','ك']
def kokler(t):
    out={t}
    for p in PR:
        if t.startswith(p) and len(t)-len(p)>=2: out.add(t[len(p):])
    return out
R=json.load(open('/tmp/lisan_beyit.json'))
B=[];I=collections.defaultdict(list)
for kok,vs in R:
    for v in vs:
        bid=len(B);B.append([v,kok])
        for tok in set(re.findall(r'[ء-ي]+',n(v))):
            for t in kokler(tok): I[t].append(bid)
KB=collections.defaultdict(list)
for i,(v,k) in enumerate(B): KB[n(k)].append(i)
ON='امتنيسء';ICI='اويتن'
SONL={'','ه','ات','ان','ون','ين','ا','ي','ت','وا','نا','ها','هم','هن','ك','كم','يه','يات','تم','تن','اء','ى','وه','اه','ته','تها','ني','ان','يين','اني','انه','ونه'}
def eslestir(r,w):
    # r kökünün harflerini w içinde konumlarıyla bul; ek harfleri yerinde mi?
    best=None
    def go(ri,wi,pos):
        nonlocal best
        if ri==len(r):
            pre=w[:pos[0]];suf=w[pos[-1]+1:];ic=[w[k] for k in range(pos[0],pos[-1]+1) if k not in pos]
            if len(pre)<=3 and all(c in ON for c in pre) and len(ic)<=2 and all(c in ICI for c in ic) and suf in SONL:
                sc=-(len(pre)+len(ic)+len(suf))-1.1*sum(1 for k,q in zip(pos,r) if w[k]!=q)
                if best is None or sc>best: best=sc
            return
        c=r[ri]
        # tekrar eden son harf (şedde): شدد -> اشتد
        if ri>0 and c==r[ri-1] and pos: go(ri+1,wi,pos)
        for k in range(wi,len(w)):
            if w[k]==c or (c in 'اويء' and w[k] in 'اويء'):
                go(ri+1,k+1,pos+[k])
            if k-wi>3: break
    go(0,0,[])
    return best
KOKS=[r for r in KB if len(r)>=3]
def kokbul(w0):
    W=[w0]
    for p in ['وال','فال','بال','كال','لل','ال','و','ف','ب','ل','ك','س']:
        if w0.startswith(p) and len(w0)-len(p)>=3: W.append(w0[len(p):])
    best=None
    for w,r in ((w,r) for w in W for r in KOKS):
        if r[0] not in w and r[0] not in 'اويء': continue
        sc=eslestir(r,w)
        if sc is None: continue
        sc=(sc-(0.5 if w!=w0 and w0.startswith('ال') is False else 0),sum(c not in 'اويء' for c in r),len(KB[r]))
        if best is None or sc>best[0]: best=(sc,r)
    return best[1] if best else None
S=json.load(open('data/roman/sozluk_ar.json'))
SN=set()
for k in S: SN.add(n(k).replace('ال','',1) if n(k).startswith('ال') else n(k))
ZC={}
def zor(b):
    if b in ZC: return ZC[b]
    T=re.findall(r'[\u0621-\u064A]+',n(B[b][0]));bil=0
    for t in T:
        if any(x in SN or x.replace('ال','',1) in SN for x in kokler(t)): bil+=1
    ZC[b]=1-bil/max(1,len(T));return ZC[b]
import hashlib,os
TRH=set()
if os.path.exists('tools/dil/beyit_tr.txt'):
    for ln in open('tools/dil/beyit_tr.txt',encoding='utf-8'):
        if '=' in ln and not ln.startswith('#'): TRH.add(ln.split('=',1)[0].strip())
TRB={i for i,(v,k) in enumerate(B) if hashlib.md5(v.encode()).hexdigest()[:8] in TRH}
ES={};kul=collections.Counter()
for k in S:
    w=sk(k)
    if ' ' in w or len(w)<3: continue
    c=[b for b in I.get(w,[]) if uyar(B[b][1],w)]
    if not c:  # aynı kökten türemiş bir kelime geçen beyit
        r=kokbul(w)
        if r: c=[b for b in KB.get(r,[]) if any(uyar(r,t) for t in re.findall(r'[\u0621-\u064A]+',n(B[b][0])))]
    if not c: continue
    c.sort(key=lambda b:((0 if b in TRB else kul[b]*40)+abs(len(B[b][0])-60)*0.5+70*zor(b)-(300 if b in TRB else 0)))
    ES[w]=c[0];kul[c[0]]+=1
print(len(S),'kelime,',len(ES),'beyitli,',len(set(ES.values())),'farklı beyit')
json.dump(ES,open('/tmp/beyit_es.json','w'),ensure_ascii=False)
import hashlib
def hid(v):return hashlib.md5(v.encode()).hexdigest()[:8]
TR={}
import os
if os.path.exists('tools/dil/beyit_tr.txt'):
    for ln in open('tools/dil/beyit_tr.txt',encoding='utf-8'):
        if '=' in ln and not ln.startswith('#'): a,b=ln.rstrip('\n').split('=',1);TR[a.strip()]=b.strip()
def jsnorm(w):return re.sub('[إأآٱ]','ا',H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))).replace('ى','ي').strip()
OB=[];OI={};W={}
for k in S:
    w=sk(k)
    if w not in ES: continue
    b=ES[w];v,kok=B[b]
    if b not in OI: OI[b]=len(OB);OB.append([v,kok,TR.get(hid(v),'')])
    W[jsnorm(k)]=OI[b]
json.dump({'b':OB,'w':W},open('data/roman/beyit_ar.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print('çıktı',len(OB),'beyit,',sum(1 for x in OB if x[2]),'tercümeli')
json.dump(B,open('/tmp/beyitler.json','w'),ensure_ascii=False)
