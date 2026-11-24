# Sözlük kelimeleri için uygulamadaki romanlardan örnek cümle (aslı + Türkçesi + kitap) -> data/roman/ornek_<dil>.json
# Çıktı: {"k":[kitap başlığı,...], "s":[[cümle, türkçe, kitap_no],...], "w":{kelime_norm: cümle_no}}
import json,re,glob,collections
H=re.compile('[ً-ٰٟـ]')
def nar(w):return re.sub('[إأآٱ]','ا',H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))).replace('ى','ي').strip()
def nfa(w):return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w)).replace('ي','ی').replace('ك','ک').replace('‌','').strip()
def nen(w):
    w=w.lower().strip().strip('\'".,!?;:')
    return w[:-2] if w.endswith("'s") else w
NORM={'ar':nar,'fa':nfa,'en':nen}
PRE_AR=['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك']
def varyant(t,d):
    o={t}
    if d=='ar':
        for p in PRE_AR:
            if t.startswith(p) and len(t)-len(p)>=2:
                r=t[len(p):];o.add(r)
                if not r.startswith('ال'): o.add('ال'+r)
        for s in ['ها','هم','ه','ك','كم','نا','هما','هن']:
            for x in list(o):
                if x.endswith(s) and len(x)-len(s)>=3: o.add(x[:-len(s)])
    elif d=='fa':
        for s in ['هایی','های','ها','ی','ان','را']:
            if t.endswith(s) and len(t)-len(s)>=2: o.add(t[:-len(s)])
        for p in ['نمی','می','ب']:
            if t.startswith(p) and len(t)-len(p)>=2: o.add(t[len(p):])
    else:
        for s,r in [('ies','y'),('es',''),('s',''),('ed',''),('ed','e'),('ing',''),('ing','e'),('ly','')]:
            if t.endswith(s) and len(t)-len(s)>=3: o.add(t[:-len(s)]+r)
    return o
for d in ['ar','fa','en']:
    S=json.load(open(f'data/roman/sozluk_{d}.json'))
    K=[];KI={};SN=[];IDX=collections.defaultdict(list)
    for f in sorted(glob.glob('data/roman/*.json')):
        try: b=json.load(open(f))
        except Exception: continue
        if not isinstance(b,dict) or b.get('dil')!=d or 'bolumler' not in b: continue
        ki=len(K);K.append(b.get('tr_baslik') or b.get('baslik'))
        for bl in b['bolumler']:
            for c in bl.get('c',[]):
                if not isinstance(c,list) or len(c)<2 or not c[1]: continue
                o,t=c[0].strip(),c[1].strip()
                if not (18<=len(o)<=150) or len(t)>230: continue
                si=len(SN);SN.append([o,t,ki])
                for tok in set(re.findall(r"[A-Za-z']+" if d=='en' else r'[؀-ۿ‌]+',o)):
                    n=NORM[d](tok)
                    if len(n)<2: continue
                    for v in varyant(n,d): IDX[v].append(si)
    kul=collections.Counter();W={};SE={}
    def puan(si,n):
        o=SN[si][0];ex=any(NORM[d](t)==n for t in re.findall(r"[A-Za-z']+" if d=='en' else r'[؀-ۿ‌]+',o))
        return (0 if ex else 40)+abs(len(o)-60)*0.4+kul[si]*25+kul[('k',SN[si][2])]*0.002
    for k in S:
        n=NORM[d](k)
        if n in W or len(n)<2 or ' ' in n: continue
        c=IDX.get(n)
        if not c: continue
        c=list(dict.fromkeys(c))[:400]
        si=min(c,key=lambda s:puan(s,n))
        kul[si]+=1;kul[('k',SN[si][2])]+=1
        if si not in SE: SE[si]=len(SE)
        W[n]=SE[si]
    out=[None]*len(SE)
    for si,j in SE.items(): out[j]=SN[si]
    json.dump({'k':K,'s':out,'w':W},open(f'data/roman/ornek_{d}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    print(d,len(S),'kelime,',len(W),'örnekli,',len(out),'cümle,',len(K),'kitap')
