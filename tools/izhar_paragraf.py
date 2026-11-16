import re,json
src=open('tools/kitap_birgivi_avamil.py').read()
ns={'re':re}; exec(src[src.index('def temiz'):src.index('def g(')],ns); temiz=ns['temiz']
L=[]
for l in open('tools/kaynak/izhar_ar_ham.txt'):
    l=l.strip()
    if l.startswith('###') or not l or re.fullmatch(r'[\s»«\-|"().0-9٠-٩]*',l) or l in ('اِظهار','﷽','اظهار'): continue
    l=re.sub(r'\s+\d{2,3}\s*$','',l); l=re.sub(r'^\d{2,3}\s+(?=\D)','',l)
    l=re.sub(r'(?<=[ء-ْٰ])\.(?=[ء-ي])','',l)
    l=l.replace('»','').replace('«','')
    L.append(l)
P=[];cur=''
for l in L:
    start_new = bool(re.match(r'^(نَحْوُ|نَحْوَ|\d+\s*[–-]|\([أ-ي]\)|اَلْبَابُ|اَلنَّوْعُ|فَصْلٌ|تَنْبِيهٌ|فَائِدَةٌ)',l))
    if cur and (start_new or re.search(r'[.:؟!]\s*$',cur)):
        P.append(cur);cur=l
    else: cur=(cur+' '+l).strip()
if cur: P.append(cur)
def parens(x):
    # eşleşmeyen ')' için 'اَيْ' öncesine '('
    out=x
    while out.count(')')>out.count('('):
        idx=out.find(')')
        # o ')' öncesi son açıklayıcı kelime
        seg=out[:idx]
        m=list(re.finditer(r'(اَيْ|اَىْ|أَيْ|اَيِ|اَىِ|اَعْن۪ي|اَعْنِي)',seg))
        if not m: break
        k=m[-1].start(); 
        if '(' in seg[k:]: break
        out=out[:k]+'('+out[k:]
        if out.count(')')<=out.count('('): break
    return out
P=[temiz(parens(p)) for p in P]
P=[p for p in P if len(p)>2]
Q=[]
for p in P:
    if Q and (re.match(r'^(نَحْوُ|نَحْوَ|وَنَحْوُ)',p) or len(Q[-1])<45): Q[-1]=Q[-1]+' '+p
    else: Q.append(p)
P=Q
json.dump(P,open('/tmp/izh_P.json','w'),ensure_ascii=False)
print(len(P))
