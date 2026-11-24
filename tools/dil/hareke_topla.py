# Harekeli kaynaklardan biçim haritası -> /tmp/hr/map.pkl (sonra hareke_oto.py, sonra hareke_kur.py /tmp/hr/oto.json)
import json,re,os,collections,glob
os.chdir('/home/claude/el-mihrab')
HAR='ً-ْ'
TOK=re.compile('[ء-ْٰٱۡ]+')
def uth(w):  # Osmanlı/uthmani işaretlerini sadeleştir
    w=w.replace('ٱ','ا').replace('ۡ','ْ').replace('ٰ','ا')
    return re.sub('[ؐ-ؚۖ-ۭـ]','',w)
def ciplak(w):return re.sub('[إأآٱ]','ا',re.sub('['+HAR+']','',w)).replace('ى','ي')
C=collections.defaultdict(collections.Counter);LEM=collections.defaultdict(collections.Counter)
def ekle(w,D=C,k=1):
    w=uth(w)
    if len(re.findall('['+HAR+']',w))<1:return
    c=ciplak(w)
    if len(c)<2:return
    D[c][w]+=k
# 1) Kur'an lemmaları (sözlük biçimi)
R=json.load(open('data/morph/roots.json'))
for r,L in R.items():
    for lem,locs in L.items():ekle(lem,LEM,len(locs) if isinstance(locs,list) else 1)
# 2) Kur'an morfoloji: LEM: etiketleri ve tam kelimeler
for f in glob.glob('data/morph/[0-9]*.json'):
    d=json.load(open(f))
    for a in d['a']:
        for w in a:
            ekle(''.join(s[0] for s in w))
            for s in w:
                m=re.search('LEM:([^|]+)',s[2])
                if m:ekle(m.group(1),LEM)
# 3) harekeli ders ve kitap metinleri
fs=['veri/arapca.js']+glob.glob('data/kitap/*.json')+glob.glob('data/modern/*.json')+glob.glob('data/yds/*.json')+glob.glob('data/cocuk/*.json')+glob.glob('data/hadis/erbain.json')+['data/zikir.json']
for f in fs:
    try:t=open(f,encoding='utf-8').read()
    except:continue
    for w in TOK.findall(t):ekle(w)
pickle=__import__('pickle');pickle.dump((dict(C),dict(LEM)),open('/tmp/hr/map.pkl','wb'))
print('form',len(C),'lemma',len(LEM))
