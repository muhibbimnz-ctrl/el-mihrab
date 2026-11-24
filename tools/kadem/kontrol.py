# Kadem içerik aracı. Kullanım: python3 tools/kadem/kontrol.py
import json,glob,os,collections,re,sys
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
ids=set();toplam=0
for f in sorted(glob.glob(R+'/konu/*.json')):
    d=json.load(open(f))
    for q in d['sorular']:
        assert len(q['c'])==5 and len(q['ac'])==5 and 0<=q['d']<5 and q['z'] in (1,2,3),(f,q['id'])
        assert q['id'] not in ids,q['id']; ids.add(q['id'])
    c=collections.Counter('ABCDE'[q['d']] for q in d['sorular'])
    toplam+=len(d['sorular'])
    print(os.path.basename(f),d['ders'],len(d['sorular']),dict(sorted(c.items())))
# mbsts konular = all konu files with mbsts
m=json.load(open(R+'/mbsts.json'))
sira=['Kur’an Bilgisi','Tefsir','Akaid ve Kelam','Fıkıh ve İlmihal','Hadis','Siyer ve İslam Tarihi','Mezhepler Tarihi','Dinler Tarihi']
K=[]
for f in sorted(glob.glob(R+'/konu/*.json'),key=lambda f:(f.split('/')[-1].split('-')[0],int(re.findall(r'(\d+)',f)[-1]))):
    d=json.load(open(f))
    if 'mbsts' in d.get('sinavlar',[]): K.append((sira.index(d['ders']),d['id']))
K.sort(key=lambda x:x[0])
m['konular']=[{'ref':i} for _,i in K]
json.dump(m,open(R+'/mbsts.json','w'),ensure_ascii=False,indent=1)
print('toplam soru',toplam,'konu',len(K))
