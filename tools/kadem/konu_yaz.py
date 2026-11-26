# Sade metinden konu JSON'u üretir:  python3 tools/kadem/konu_yaz.py kaynak.txt [kaynak2.txt …]
# Biçim (her satır bir öğe):
#   #id | ad | ders | sınav1,sınav2 | öncelik      (ilk satır)
#   P paragraf · B başlık · M merak · S sınavda · A aklında kalsın · N not · K kontrol
#   AY meal || kaynak · HD hadis || kaynak · MD madde || kaynak
#   T hücre | hücre | hücre   (art arda T satırları bir tablo; boş "T" tabloyu bitirir)
#   O özet maddesi · C ön || arka
#   Q z | soru kökü ( // = yeni satır ) · "- şık || şık açıklaması" ×5 · "= harf" · "> açıklama" · "~ kaynak"
#   Soru id'leri: dosyadaki "@on" satırıyla verilen önek + sıra (ör. "@on ar1" → ar1-01 …)
import json,sys,os,re
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','konu')
for src in sys.argv[1:]:
    L=[l.rstrip('\n') for l in open(src,encoding='utf-8')]
    h=[x.strip() for x in L[0][1:].split('|')]
    d={'id':h[0],'ad':h[1],'ders':h[2],'sinavlar':[s.strip() for s in h[3].split(',')],'oncelik':int(h[4]),'anlatim':[],'ozet':[],'kartlar':[],'sorular':[]}
    on=h[0].replace('-','');tab=None;q=None
    def bit():
        global tab
        if tab: d['anlatim'].append({'tablo':tab}); tab=None
    for ln in L[1:]:
        if not ln.strip(): continue
        k,_,v=ln.partition(' ');v=v.strip()
        if k!='T': bit()
        if k=='@on': on=v
        elif k=='P': d['anlatim'].append(v)
        elif k in ('B','M','S','A','N','K'): d['anlatim'].append({{'B':'b','M':'merak','S':'sinav','A':'akil','N':'not','K':'kontrol'}[k]:v})
        elif k in ('AY','HD','MD'):
            m,_,kay=v.partition(' || '); d['anlatim'].append({{'AY':'ayet','HD':'hadis','MD':'madde'}[k]:m.strip(),'kay':kay.strip()})
        elif k=='T':
            if not v: bit()
            else: tab=(tab or [])+[[c.strip() for c in v.split(' | ')]]
        elif k=='O': d['ozet'].append(v)
        elif k=='C': o,_,a=v.partition(' || '); d['kartlar'].append({'o':o.strip(),'a':a.strip()})
        elif k=='Q':
            z,_,s=v.partition(' | '); q={'id':f"{on}-{len(d['sorular'])+1:02d}",'z':int(z),'s':s.replace(' // ','\n'),'c':[],'ac':[]}; d['sorular'].append(q)
        elif k=='-': o,_,a=v.partition(' || '); q['c'].append(o.strip()); q['ac'].append(a.strip())
        elif k=='=': q['d']='ABCDE'.index(v)
        elif k=='>': q['a']=v
        elif k=='~': q['kay']=v
        else: raise SystemExit(f'{src}: anlaşılmadı: {ln[:70]}')
    bit()
    for q in d['sorular']:
        assert len(q['c'])==5 and 'd' in q and 'a' in q,(src,q['id'])
        q.setdefault('kay','')
        q={k:q[k] for k in ('id','z','s','c','d','a','ac','kay')}
    d['sorular']=[{k:q[k] for k in ('id','z','s','c','d','a','ac','kay')} for q in d['sorular']]
    json.dump(d,open(f"{R}/{d['id']}.json",'w',newline='\n'),ensure_ascii=False,indent=1)
    print(d['id'],len(d['anlatim']),'öğe',len(d['sorular']),'soru',len(d['kartlar']),'kart')
