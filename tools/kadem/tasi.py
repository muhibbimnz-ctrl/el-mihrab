# Köprü (eski-*) dosyalarındaki soruları yeni konulara taşır; boşalan köprü dosyasını (json+enc) siler.
#   python3 tools/kadem/tasi.py tefsir-5:t2-01,t2-06 tefsir-6:t1-11 …
import json,os,sys,glob
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','konu')
yaz=lambda f,d:open(f,'w',encoding='utf-8',newline='\n').write(json.dumps(d,ensure_ascii=False,indent=1)+'\n')
eski={f:json.load(open(f)) for f in glob.glob(R+'/eski-*.json')}
for arg in sys.argv[1:]:
    hedef,ids=arg.split(':');ids=ids.split(',');hf=f'{R}/{hedef}.json';H=json.load(open(hf))
    var={q['id'] for q in H['sorular']}
    for i in ids:
        for f,E in eski.items():
            q=next((q for q in E['sorular'] if q['id']==i),None)
            if q:
                E['sorular'].remove(q)
                if i not in var:H['sorular'].append(q)
                break
        else: print('bulunamadı',i)
    yaz(hf,H)
for f,E in eski.items():
    if E['sorular']: yaz(f,E)
    else:
        os.remove(f)
        if os.path.exists(f[:-5]+'.enc'):os.remove(f[:-5]+'.enc')
        print('silindi',os.path.basename(f))
