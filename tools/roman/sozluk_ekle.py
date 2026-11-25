# Yeni sözlük maddelerini mevcut data/roman/sozluk_<dil>.json'a yalnız EKLER (var olanı silmez),
# Arapça/Farsça maddeleri şâhid beyitlere bağlar (en çok 4 beyit, Türkçesi olan öne).
# Not: tools/roman/ortak_sozluk.js sözlüğü baştan kurar ve bugün Arapçayı ~12.700'e düşürür; onun yerine bunu kullan.
# Kullanım: python3 tools/roman/sozluk_ekle.py tools/roman/sozluk/ar_15.txt [başka .txt ...]
import json,re,sys,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
P=re.compile(r'[«»،.؟!:؛()\-"\[\]]'); HR=re.compile(r'[ً-ٰٟـ]')
def nr(w): return re.sub('[إأآٱ]','ا',P.sub('',HR.sub('',w or ''))).replace('ى','ي').strip()
def nf(w): return P.sub('',HR.sub('',w or '')).replace('ي','ی').replace('ك','ک').replace('‌','').strip()
def adar(n):
    c=[n]
    for p in ['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك','س']:
        if n.startswith(p) and len(n)-len(p)>=3: r=n[len(p):]; c+=[r,'ال'+r]
    t=re.sub(r'^(وال|بال|فال|ال|و|ف|ب)','',n)
    for s in ['هما','هم','هن','ها','كم','نا','ني','ه','ك','ي','ون','ين','ات','ان','ة','ا']:
        if len(t)-len(s)>=3 and t.endswith(s): c+=[t[:-len(s)],'ال'+t[:-len(s)]]
    return c
def adfa(n):
    c=[n]
    for r in [r'(هایی|های|ها|ان|ی)$',r'^(نمی|می|ب)']:
        x=re.sub(r,'',n)
        if x!=n and len(x)>=2: c.append(x)
    return c
def anahtar(w,d):
    if d=='en':
        w=w.lower().strip("'\".,!?;:"); return w[:-2] if w.endswith("'s") else w
    return HR.sub('',w.replace('_','‌')).strip()
for f in sys.argv[1:]:
    d=os.path.basename(f)[:2]
    sp=os.path.join(R,'data/roman/sozluk_'+d+'.json'); S=json.load(open(sp,encoding='utf-8'))
    yeni=[]
    for l in open(f,encoding='utf-8'):
        if '=' not in l or l.startswith('#'): continue
        k,v=l.rstrip('\n').split('=',1); k=anahtar(k,d); v=v.strip()
        if k and v and k not in S: S[k]=v; yeni.append(k)
    json.dump(S,open(sp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    bag=0
    if d in ('ar','fa'):
        bp=os.path.join(R,'data/roman/beyit_'+d+'.json'); B=json.load(open(bp,encoding='utf-8')); W=B['w']
        N=nr if d=='ar' else nf; AD=adar if d=='ar' else adfa; ti=2 if d=='ar' else 2
        RX=r'[ء-ي]+' if d=='ar' else r'[ء-ی‌]+'
        idx={}
        for i,x in enumerate(B['b']):
            for t in set(re.findall(RX,N(x[0]))):
                for a in AD(N(t)): idx.setdefault(a,set()).add(i)
        for k in yeni:
            nk=N(k)
            if nk in W: continue
            L=sorted(idx.get(nk,()),key=lambda i:(0 if len(B['b'][i])>ti and B['b'][i][ti] else 1,i))[:4]
            if L: W[nk]=L if len(L)>1 else L[0]; bag+=1
        json.dump(B,open(bp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    print(f,'+',len(yeni),'madde;',bag,'şâhid bağı; toplam',len(S))
