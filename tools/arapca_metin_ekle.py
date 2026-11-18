# data/modern/modern.json'daki okuma metinlerini (makaleleri) Modern Arapça sayfasının
# Günlük Hayat / Akademik / İslami İlimler programlarına ders olarak ekler. Tekrar çalıştırılabilir.
import json,re
m=json.load(open('data/modern/modern.json'))
H=re.compile(r'[ً-ْٰـ]')
# alan -> (program, kategori)
ALAN={'bilim':('A',0),'tarih':('A',1),'edebiyat':('A',2),'egitim':('A',3),'medya':('A',4),'cevre':('A',5),'saglik':('A',6),'ekonomi':('A',7),'hukuk':('A',7),'sanat':('T',7)}
OZEL={'Uzaktan çalışma':('T',6),'Trafik güvenliği':('T',5),'Sosyal medya ve gençler':('T',8),'Dijital bağımlılık':('T',8),'Değişen aile yapısı':('T',11),'Yaşlılar ve yalnızlık':('T',11),'Gönüllülük':('T',11),'Göç ve kentleşme':('T',7),'Tüketim kültürü':('T',2),'Bir haber metni: uluslararası konferans':('T',10),
 'Ramazan’da sağlıklı beslenme':('I',2),'Ramazan ve dayanışma':('I',2),'Zekât':('I',2),'Cuma günü':('I',2),'Hac yolculuğu':('I',2),'Vakıf medeniyeti':('I',5),'Kudüs ve Mescid-i Aksâ':('I',5),'Caminin toplumdaki yeri':('I',5),'Hadis ilmi':('I',1),'Hafızlık geleneği':('I',0),
 'Gıda israfı':('T',3),'Çocuk beslenmesi':('T',3),'Su içmenin önemi':('T',4),'Uykunun önemi':('T',4),'Arılar ve hayat':('T',9),'Ormanlar':('T',9),
 'Akıl ve iman':('I',3),'Hicret':('I',4),'Komşuluk hakkı':('I',6),'Muallakât':('I',7),'Makame türü':('I',7),'Kur’an’ın cem edilmesi':('I',0),'İslam tarihinde kadın âlimler':('I',5),
 'Câhız ve Arap nesri':('C2',1),'Tavku’l-Hamâme':('C2',1),'Modern Arap romanı':('C2',2),'Necîb Mahfûz':('C2',2),'Arapça dünyada':('C2',3),'Yapay zekânın sınırları':('C2',4),'İbn Haldûn':('C2',4),
 'Basın özgürlüğü':('C2',5),'Yalan haberle mücadele':('C2',5),'Vakıf medeniyeti':('C2',6),'Makam müziği':('C2',6),'Yargı bağımsızlığı':('C2',7),'Anayasa nedir?':('C2',7)}
def bol(s,isar):
    p=re.split(r'(?<=[.!?؟])\s+',s.strip()); return [x for x in p if x.strip()]
out={'T':[],'A':[],'I':[],'C2':[]}
for x in m['metinler']:
    hedef=OZEL.get(x['baslik']) or ALAN.get(x['alan'])
    if not hedef: continue
    P=[]
    for a,t in zip(x['ar'],x['tr']):
        sa,st=bol(a,1),bol(t,0)
        P.append([[u,v] for u,v in zip(sa,st)] if len(sa)==len(st) else [[a,t]])
    cumle=[s for par in x['ar'] for s in bol(par,1)]
    V=[]
    for w,tr in x['sozluk']:
        k=H.sub('',w).replace('…','').replace('بـ','').strip().split()[0] if w.strip() else w
        ex=next((s for s in cumle if k and k in H.sub('',s)),'')
        V.append([w,tr,ex,''])
    L={'c':hedef[1],'en':x['ar_baslik'],'tr':x['baslik'],'v':V,'p':P,'mq':[[q['s'],q['k'],q['d'],q.get('a','')] for q in x['sorular']],'sv':x.get('seviye','')}
    out[hedef[0]].append(L)
js='/*YDS-METIN*/'+''.join(f'{k}.push.apply({k},{json.dumps(v,ensure_ascii=False,separators=(",",":"))});' for k,v in out.items())+'/*/YDS-METIN*/\n'
f='arapca.html'; s=open(f,encoding='utf-8').read()
s=re.sub(r'/\*YDS-METIN\*/.*?/\*/YDS-METIN\*/\n','',s,flags=re.S)
assert s.count('\nvar COL={')==1; s=s.replace('\nvar COL={','\n'+js+'var COL={',1)
open(f,'w',encoding='utf-8').write(s)
print({k:len(v) for k,v in out.items()})
