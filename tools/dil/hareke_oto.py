import pickle,json,re,os,collections
os.chdir('/home/claude/el-mihrab')
C,LEM=pickle.load(open('/tmp/hr/map.pkl','rb'))
S=json.load(open('data/roman/sozluk_ar.json'))
HAR='ً-ْ'
def ciplak(w):return re.sub('[إأآٱ]','ا',re.sub('['+HAR+']','',w)).replace('ى','ي')
VERB=re.compile(r"^[^,;(]*?(d[ıiuü]|t[ıiuü])(\b|$)",re.I)
def fiil_mi(m):
    g=re.split('[,;(]',m)[0].strip().lower()
    return bool(re.search('(dı|di|du|dü|tı|ti|tu|tü)$',g))
def bas(w,fiil):
    w=w.rstrip('ْ')
    if fiil and w.endswith('َ'):return w
    while w and w[-1] in 'ًٌٍَُِْ':w=w[:-1]
    return w
def harf_ok(v,c):  # harekeli biçimin harfleri anahtarla uyuşsun (hemze yazımı dahil)
    return ciplak(v)==c
out={};kay=collections.Counter()
for k,m in S.items():
    if re.search('['+HAR+']',k):continue
    c=ciplak(k);f=fiil_mi(m);adaylar=[]
    for src,D,w in (('lem',LEM,3),('metin',C,1)):
        for v,n in D.get(c,{}).items():adaylar.append((v,n*w,src))
    if not adaylar:continue
    def puan(x):
        v,n,src=x;son=v.rstrip('ْ')[-1:]
        ok=(son=='َ')==f if src=='lem' else True
        if src=='metin' and f and son!='َ':ok=False
        if src=='metin' and not f and son=='َ' and len(c)==3:ok=False
        return (ok,n)
    adaylar.sort(key=puan,reverse=True);v,n,src=adaylar[0]
    # hemze/elif yazımı anahtarla aynı olsun
    h=bas(v,f)
    if re.sub('['+HAR+']','',h).replace('ى','ي')!=k.replace('ى','ي'):
        # harfleri anahtardan al, harekeleri aktar (harf sayısı eşitse)
        pass
    hs=re.findall('([^'+HAR+'])(['+HAR+']*)',h)
    if len(hs)!=len(k):continue
    hs[0]=(hs[0][0],hs[0][1].replace('\u0651',''))
    h=''.join(k[i]+hs[i][1] for i in range(len(k)))
    if not re.search('['+HAR+']',h):continue
    out[k]=h;kay[src]+=1
json.dump(out,open('/tmp/hr/oto.json','w'),ensure_ascii=False)
print(len(out),kay)
import random;random.seed(5)
for k in random.sample(list(out),40):print(k,'→',out[k],'|',S[k][:40])
