# Sade metin biçiminden deneme JSON'u üretir ve denetler.
#   python3 tools/kadem/deneme_yaz.py kaynak.txt N "açıklama"
# Biçim: "@Ders" satırı; her soru: "z | kök ( // = yeni satır)", 5 adet "- şık || şık açıklaması", "= doğru harf (A-E)", "> genel açıklama", "~ kaynak"
import json,sys,re,os,collections
src,n,acik=sys.argv[1],int(sys.argv[2]),sys.argv[3]
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
    out.append({'id':f'md{n}-{i:02d}','ders':q['ders'],'z':q['z'],'s':q['s'],'c':q['c'],'d':q['d'],'a':q['a'],'ac':q['ac'],'kay':q.get('kay','')})
z=collections.Counter(q['z'] for q in out)
d={'id':f'mbsts-{n}','ad':f'{n}. Deneme','aciklama':f'{acik} · 60 soru · {z[1]} kolay, {z[2]} orta, {z[3]} zor','sorular':out}
sira=[(k,len(list(g))) for k,g in __import__('itertools').groupby(q['ders'] for q in out)]
hedef=[('Kur’an Bilgisi',7),('Tefsir',7),('Akaid ve Kelam',7),('Fıkıh ve İlmihal',20),('Hadis',7),('Siyer ve İslam Tarihi',7),('Mezhepler Tarihi',3),('Dinler Tarihi',2)]
m=[]
if sira!=hedef:m.append(f'dağılım {sira}')
if z[1]>6:m.append('kolay fazla')
if z[3]<24:m.append(f'zor az {z[3]}')
if sum(1 for q in out if re.search(r'(^|\n)I\.',q['s']))<8:m.append('I-II-III az')
for q in out:
    if len(q['c'])!=5:m.append(q['id']+' şık')
    if any(len(a)<15 for i,a in enumerate(q['ac']) if i!=q['d']):m.append(q['id']+' kısa ac')
    if any(re.search(r'\b[A-E]\s*(şıkkı|seçeneği|\))',a) for a in q['ac']+[q['a']]):m.append(q['id']+' harf')
json.dump(d,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','deneme',f'mbsts-{n}.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(f'mbsts-{n}:',len(out),'soru',dict(z),'; '.join(m) or '✓')
