# Yeni konu dosyalarını ölçütlere göre denetler.
#   python3 tools/kadem/kontrol_konu.py tefsir-5 tefsir-6 …   (ad vermezsen bütün yeni konular)
import json,os,re,sys,glob
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','konu')
tum={}
for f in glob.glob(R+'/*.json'):
    for q in json.load(open(f)).get('sorular',[]): tum.setdefault(q['id'],[]).append(os.path.basename(f)[:-5])
adlar=sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(R+'/*.json') if not os.path.basename(f).startswith('eski-'))
hata=0
for a in adlar:
    d=json.load(open(f'{R}/{a}.json'));S=d['sorular'];A=d['anlatim'];m=[]
    n=len(json.dumps(A,ensure_ascii=False))
    say=lambda k:sum(1 for b in A if isinstance(b,dict) and k in b)
    if n<9000:m.append(f'anlatım {n} karakter')
    for k,en in (('merak',2),('sinav',2),('tablo',2),('akil',2),('b',3)):
        if say(k)<en:m.append(f'{k} {say(k)}<{en}')
    if len(d.get('ozet',[]))<10:m.append('özet az')
    if len(d.get('kartlar',[]))<12:m.append('kart az')
    if len(S)<14:m.append(f'soru {len(S)}')
    z=[q['z'] for q in S]
    if z.count(1)>2:m.append('kolay fazla')
    if z.count(3)<0.4*len(S):m.append(f'zor az ({z.count(3)})')
    if sum(1 for q in S if re.search(r'(^|\n)\s*I\.',q['s']))<2:m.append('I-II-III az')
    for q in S:
        if len(q['c'])!=5 or len(q.get('ac',[]))!=5 or not 0<=q['d']<=4:m.append(q['id']+' şık/ac/d')
        if any(re.search(r'\b[A-E]\s*(şıkkı|seçeneği|\))',x) for x in q['ac']):m.append(q['id']+' ac içinde harf')
        if len(tum.get(q['id'],[]))>1:m.append(q['id']+' tekrar: '+','.join(tum[q['id']]))
    print(('✓ ' if not m else '✗ ')+a,f'{n} kar., {len(S)} soru (zor {z.count(3)})','; '.join(m))
    hata+=bool(m)
sys.exit(1 if hata else 0)
