# tools/kaynak/metin/*.txt dosyalarındaki okuma metinlerini data/modern/modern.json'a ekler (idempotent)
import json,glob,random
M='data/modern/modern.json'; m=json.load(open(M))
YENI={'hukuk':['Hukuk ve siyaset','القانون والسياسة'],'medya':['Medya ve iletişim','الإعلام والاتصال'],'sanat':['Sanat ve spor','الفن والرياضة']}
yeni=[]
for f in sorted(glob.glob('tools/kaynak/metin/*.txt')):
  cur=None
  for ln in open(f,encoding='utf-8'):
    ln=ln.rstrip('\n')
    if not ln.strip(): continue
    if ln[0]=='@':
      i,alan,sv,tr,ar=[x.strip() for x in ln[1:].split('|')]
      cur={'id':i,'baslik':tr,'ar_baslik':ar,'konu':YENI[alan][0],'seviye':sv,'ar':[],'tr':[],'sozluk':[],'sorular':[],'alan':alan}; yeni.append(cur); continue
    t,_,rest=ln.partition('|')
    if t=='A': cur['ar'].append(rest.strip())
    elif t=='R': cur['tr'].append(rest.strip())
    elif t=='S': cur['sozluk']=[[y.strip() for y in x.split('=')] for x in rest.split(';')]
    elif t=='Q':
      p=[x.strip() for x in rest.split('|')]; assert len(p)==6 and len(set(p[1:5]))==4,(cur['id'],rest[:40])
      R=random.Random(cur['id']+str(len(cur['sorular']))); k=p[2:5]; R.shuffle(k); d=R.randrange(4); k.insert(d,p[1])
      cur['sorular'].append({'s':p[0],'k':k,'d':d,'a':p[5]})
    else: raise SystemExit('bilinmeyen: '+ln[:40])
for x in yeni: assert len(x['ar'])==len(x['tr'])>=2 and len(x['sorular'])==3 and all(len(s)==2 for s in x['sozluk']),x['id']
ids={x['id'] for x in yeni}
m['metinler']=[x for x in m['metinler'] if x['id'] not in ids]+yeni
for a,(tr,ar) in YENI.items():
  if any(x['alan']==a for x in yeni) and not any(z[0]==a for z in m['alanlar']): m['alanlar'].append([a,tr,ar])
json.dump(m,open(M,'w'),ensure_ascii=False,separators=(',',':'))
print(len(m['metinler']),[z[0] for z in m['alanlar']])
