# Sade metin biçiminden deneme JSON'u üretir ve denetler.
#   python3 tools/kadem/deneme_yaz.py kaynak.txt N "açıklama" [sınav=mbsts]
#   Ders sırası ve soru sayıları sınavın haritasından okunur (sınavın sıra listesi: harita.dersler).
# Biçim: "@Ders" satırı; her soru: "z | kök ( // = yeni satır)", 5 adet "- şık || şık açıklaması", "= doğru harf (A-E)", "> genel açıklama", "~ kaynak"
import json,sys,re,os,collections
src,n,acik=sys.argv[1],int(sys.argv[2]),sys.argv[3]
sid=sys.argv[4] if len(sys.argv)>4 else 'mbsts'
RK=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
H=json.load(open(f'{RK}/{sid}.json'))
hedef=[(x['ad'],x['soru']) for x in H['harita']['dersler']]
if sid=='mbsts':hedef=[('Kur’an Bilgisi',7),('Tefsir',7),('Akaid ve Kelam',7),('Fıkıh ve İlmihal',20),('Hadis',7),('Siyer ve İslam Tarihi',7),('Mezhepler Tarihi',3),('Dinler Tarihi',2)]
N=sum(k for _,k in hedef);on={'mbsts':'md','dhbt':'dh','mevzuat':'mz'}.get(sid,sid[:2])
S=[];ders=None;q=None
for ln in open(src,encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln.strip():continue
    if ln.startswith('@'):ders=ln[1:].strip();continue
    m=re.match(r'^([123])\s*\|\s*(.*)$',ln)
    if m:
        q={'ders':ders,'z':int(m.group(1)),'s':m.group(2).replace(' // ','\n'),'c':[],'ac':[]};S.append(q);continue
    if ln.startswith('- '):o,a=ln[2:].split(' || ');q['c'].append(o.strip());q['ac'].append(a.strip());continue
    if ln.startswith('= '):q['d']='ABCDE'.index(ln[2:].strip());continue
    if ln.startswith('> '):q['a']=ln[2:].strip();continue
    if ln.startswith('~ '):q['kay']=ln[2:].strip();continue
    raise SystemExit('anlaşılmadı: '+ln[:60])
out=[]
for i,q in enumerate(S,1):
    out.append({'id':f'{on}{n}-{i:02d}','ders':q['ders'],'z':q['z'],'s':q['s'],'c':q['c'],'d':q['d'],'a':q['a'],'ac':q['ac'],'kay':q.get('kay','')})
z=collections.Counter(q['z'] for q in out)
d={'id':f'{sid}-{n}','ad':f'{n}. Deneme','aciklama':f'{acik} · {N} soru · {z[1]} kolay, {z[2]} orta, {z[3]} zor','sorular':out}
sira=[(k,len(list(g))) for k,g in __import__('itertools').groupby(q['ders'] for q in out)]
m=[]
if sira!=hedef:m.append(f'dağılım {sira}')
if z[1]>N*0.1:m.append('kolay fazla')
if z[3]<N*0.4:m.append(f'zor az {z[3]}')
if sum(1 for q in out if re.search(r'(^|\n)I\.',q['s']))<N*0.13:m.append('I-II-III az')
for q in out:
    if len(q['c'])!=5:m.append(q['id']+' şık')
    if any(len(a)<15 for i,a in enumerate(q['ac']) if i!=q['d']):m.append(q['id']+' kısa ac')
    if any(re.search(r'\b[A-E]\s*(şıkkı|seçeneği|\))',a) for a in q['ac']+[q['a']]):m.append(q['id']+' harf')
json.dump(d,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','deneme',f'{sid}-{n}.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(f'{sid}-{n}:',len(out),'soru',dict(z),'; '.join(m) or '✓')
sys.exit(1 if m else 0)
