# Kadem içerik aracı. Kullanım: python3 tools/kadem/kontrol.py
# Bütün konu ve deneme dosyalarını doğrular; her sınav dosyasının "konular" ve "denemeler" listesini yeniden kurar.
# Bir konu, "sinavlar" alanında adı geçen her sınava bağlanır. Sıralama: haritadaki ders sırası, sonra dosya numarası.
import json,glob,os,collections,re
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
SIRA=['Kur’an Bilgisi','Tefsir','Akaid ve Kelam','Fıkıh ve İlmihal','Hadis','Siyer ve İslam Tarihi','İslam Ahlakı','Mezhepler Tarihi','Dinler Tarihi','Din Hizmetleri ve Hitabet','Mevzuat']
ids=set();toplam=0;KONU={}
def soru_kontrol(f,q):
    global toplam
    assert len(q['c'])==5 and len(q['ac'])==5 and 0<=q['d']<5 and q['z'] in (1,2,3),(f,q['id'])
    assert q['id'] not in ids,('tekrar id',q['id']); ids.add(q['id']); toplam+=1
for f in sorted(glob.glob(R+'/konu/*.json')):
    d=json.load(open(f));KONU[d['id']]=d
    for q in d['sorular']: soru_kontrol(f,q)
    c=collections.Counter('ABCDE'[q['d']] for q in d['sorular'])
    print(os.path.basename(f),d['ders'],len(d['sorular']),dict(sorted(c.items())))
DEN={}
for f in sorted(glob.glob(R+'/deneme/*.json')):
    d=json.load(open(f));DEN[d['id']]=d
    for q in d['sorular']: soru_kontrol(f,q)
    c=collections.Counter(q['ders'] for q in d['sorular'])
    print(os.path.basename(f),len(d['sorular']),dict(c))
def no(i): m=re.findall(r'(\d+)$',i); return int(m[0]) if m else 0
for f in sorted(glob.glob(R+'/*.json')):
    sid=os.path.basename(f)[:-5]
    if sid=='sinavlar': continue
    m=json.load(open(f))
    sira=[x['ad'] for x in m.get('harita',{}).get('dersler',[])] or SIRA
    def anahtar(k): d=KONU[k]; return (sira.index(d['ders']) if d['ders'] in sira else 99, k.split('-')[0], no(k))
    K=sorted([k for k,d in KONU.items() if sid in d.get('sinavlar',[])],key=anahtar)
    m['konular']=[{'ref':k} for k in K]
    Dn=sorted([k for k in DEN if k.startswith(sid+'-')],key=no)
    if Dn:
        m['denemeler']=[{'ref':k} for k in Dn]
        dersler={x['ad']:x['soru'] for x in m.get('harita',{}).get('dersler',[])}
        for k in Dn:
            c=collections.Counter(q['ders'] for q in DEN[k]['sorular'])
            for ders in c: assert not dersler or ders in dersler,(k,'harita dışı ders',ders)
            if dersler and c!=collections.Counter(dersler): print('  UYARI',k,'dağılım haritadan farklı',dict(c))
    elif 'denemeler' in m: del m['denemeler']
    json.dump(m,open(f,'w',newline='\n'),ensure_ascii=False,indent=1)
    print(sid,'konu',len(K),'deneme',len(Dn))
print('toplam soru',toplam)
