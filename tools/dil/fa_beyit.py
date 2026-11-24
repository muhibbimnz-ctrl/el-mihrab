# Farsça sözlüğe şâhid beyit: klasik şairlerden (Gencûr metinlerinden derlenmiş "Persian Poems Corpus", github.com/amnghd/Persian_poems_corpus, normalized/*.txt)
# Kullanım: python3 tools/dil/fa_beyit.py /yol/Persian_poems_corpus/normalized  -> data/roman/beyit_fa.json
# Çıktı: {"b":[[mısra1 ... mısra2, şâir, türkçe],...], "w":{kelime_norm: no | [no,no]}}; Türkçeler tools/dil/beyit_fa_tr.txt (md5ilk8=Türkçe)
import json,re,sys,os,hashlib,collections
D=sys.argv[1] if len(sys.argv)>1 else '/home/claude/pp/normalized'
SAIR=[('hafez','Hâfız'),('saadi','Sa‘dî'),('moulavi','Mevlânâ'),('ferdousi','Firdevsî'),('khayyam','Hayyâm'),('roodaki','Rûdekî'),('attar','Attâr'),('sanaee','Senâî'),('jami','Câmî')]
H=re.compile('[ً-ٰٟـ]')
def nfa(w):return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w)).replace('ي','ی').replace('ك','ک').replace('‌','').strip()
def duzen(m):  # ayrık ekleri yarım boşlukla bağla (gösterim için)
    m=re.sub(r'(^| )(ن?می) (?=\S)',lambda x:x.group(1)+x.group(2)+'‌',m)
    m=re.sub(r' (هایی|های|ها)(?= |$)',r'‌\1',m)
    return re.sub(r'\s+',' ',m).strip()
TR={}
p='tools/dil/beyit_fa_tr.txt'
if os.path.exists(p):
    for ln in open(p,encoding='utf-8'):
        if '=' in ln and not ln.startswith('#'): a,b=ln.rstrip('\n').split('=',1);TR[a.strip()]=b.strip()
def hid(v):return hashlib.md5(v.encode()).hexdigest()[:8]
SIKI={'moulavi','ferdousi','attar','jami','sanaee','hafez','saadi','khayyam','roodaki'}  # gazellerde mısra sırası kayabildiği için yalnız kafiyeli çiftler
B=[];IDX=collections.defaultdict(list)
KOTU=re.compile(r'(^| )(کیر|قحبه|جنده|گایید|گاید|بگای|لواط|غلامباره|کون ?ده|خایه|فرج|شاشید|ریدن|رید|گوز)')
for rank,(f,ad) in enumerate(SAIR):
    fp=os.path.join(D,f+'_norm.txt')
    if not os.path.exists(fp): continue
    blok=[]
    def bitir():
        # mısraları eşleştir: ya iki mısra kafiyeli (mesnevî), ya ikinci mısra şiirin redif/kafiyesiyle biter (gazel)
        son=lambda m:nfa(m.replace(' ',''))[-2:]
        say=collections.Counter(son(m) for m in blok);ust=say.most_common(1)[0][0] if say else ''
        i=0
        while i<len(blok)-1:
            a0,b0=blok[i],blok[i+1]
            if not (son(a0)==son(b0) or (f not in SIKI and say[son(b0)]>=4 and son(b0)==ust and son(a0)!=ust)): i+=1;continue
            if a0.startswith('که ') or (f=='hafez' and nfa(a0.replace(' ',''))[-3:]!=nfa(b0.replace(' ',''))[-3:]): i+=1;continue
            i+=2
            a,b=duzen(a0),duzen(b0)
            if not(8<=len(a)<=48 and 8<=len(b)<=48): continue
            v=a+' ... '+b
            if KOTU.search(v): continue
            bi=len(B);B.append([v,ad,rank])
            for t in set(re.findall(r'[\u0600-\u06FF\u200c]+',v)):
                n=nfa(t)
                if len(n)>=2: IDX[n].append(bi)
    for ln in open(fp,encoding='utf-8'):
        ln=ln.strip()
        if not ln or not re.search(r'[؀-ۿ]',ln):
            bitir();blok=[];continue
        blok.append(ln)
    bitir()
print(len(B),'beyit')
S=json.load(open('data/roman/sozluk_fa.json'))
SN={nfa(k) for k in S}
ZC={}
def zor(b):
    if b in ZC: return ZC[b]
    T=[nfa(t) for t in re.findall(r'[؀-ۿ‌]+',B[b][0])]
    ZC[b]=1-sum(1 for t in T if t in SN or len(t)<=2)/max(1,len(T));return ZC[b]
TRB={i for i,x in enumerate(B) if hid(x[0]) in TR}
kul=collections.Counter();OUT=[];OI={};W={}
for k in S:
    n=nfa(k)
    if n in W or len(n)<2 or ' ' in n: continue
    c=IDX.get(n)
    if not c: continue
    if len(c)>3000: c=c[::len(c)//3000+1]
    def puan(b):
        x=B[b];return (-400 if b in TRB else 0)+x[2]*9+zor(b)*80+abs(len(x[0])-52)*0.4+kul[b]*30
    c=sorted(set(c),key=puan)
    sec=[c[0]]
    for b in c[1:6]:
        if B[b][1]!=B[sec[0]][1] and (zor(b)<0.45 or b in TRB): sec.append(b);break
    L=[]
    for b in sec:
        kul[b]+=1
        if b not in OI: OI[b]=len(OUT);OUT.append([B[b][0],B[b][1],TR.get(hid(B[b][0]),'')])
        L.append(OI[b])
    W[n]=L[0] if len(L)==1 else L
json.dump({'b':OUT,'w':W},open('data/roman/beyit_fa.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(S),'kelime,',len(W),'beyitli,',len(OUT),'beyit,',sum(1 for x in OUT if x[2]),'Türkçeli',collections.Counter(x[1] for x in OUT).most_common())
