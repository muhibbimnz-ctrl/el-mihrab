# Kadem içerik aracı. Kullanım: python3 tools/kadem/harita.py
import json,glob
import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
m=json.load(open(R+'/mbsts.json'))
K={}
for r in m['konular']:
    d=json.load(open(R+'/konu/'+r['ref']+'.json')); K.setdefault(d['ders'],[]).append(d)
ONC={'fikih-1':3,'fikih-2':3,'fikih-3':3,'fikih-4':3,'fikih-5':2,'fikih-6':3,'fikih-7':3,'fikih-8':3,'fikih-9':2,'fikih-10':3}
for ders in m['harita']['dersler']:
    if ders['ad'] in K:
        eski={u.get('konu'):u.get('oncelik',2) for u in ders['uniteler']}
        ders['uniteler']=[{'ad':d['ad'],'oncelik':d.get('oncelik',ONC.get(d['id'],eski.get(d['id'],3))),'konu':d['id']} for d in K[ders['ad']]]
json.dump(m,open(R+'/mbsts.json','w'),ensure_ascii=False,indent=1)
print({k:len(v) for k,v in K.items()})
