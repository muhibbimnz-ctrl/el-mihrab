# Kadem içerik aracı. Kullanım: python3 tools/kadem/harita.py
# Haritası olan her sınavda, ünite listelerini o sınava bağlı hazır konulardan günceller.
import json,glob,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
for f in sorted(glob.glob(R+'/*.json')):
    if f.endswith('sinavlar.json'): continue
    m=json.load(open(f))
    if 'harita' not in m: continue
    K={}
    for r in m.get('konular',[]):
        d=json.load(open(R+'/konu/'+r['ref']+'.json')); K.setdefault(d['ders'],[]).append(d)
    for ders in m['harita']['dersler']:
        if ders['ad'] in K:
            eski={u.get('konu'):u.get('oncelik',2) for u in ders['uniteler']}
            ders['uniteler']=[{'ad':d['ad'],'oncelik':d.get('oncelik',eski.get(d['id'],3)),'konu':d['id']} for d in K[ders['ad']]]
    json.dump(m,open(f,'w',newline='\n'),ensure_ascii=False,indent=1)
    print(os.path.basename(f),{k:len(v) for k,v in K.items()})
