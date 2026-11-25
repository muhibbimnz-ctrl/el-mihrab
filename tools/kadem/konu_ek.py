# Eski biçimdeki bir konuyu yeni ölçütlere taşımak için ek içerik işler.
#   python3 tools/kadem/konu_ek.py ek.txt
# Biçim:
#   #konu ahlak-1          (dosya; sonraki satırlar bu konuya)
#   +merak metin | +sinav metin | +akil metin   (anlatıma kutu ekler; dağıtarak yerleştirir)
#   +ozet metin             +kart soru || cevap         +z soru-id 3   (zorluk günceller)
#   +duz soru-id sıra metin (bir şık açıklamasını değiştirir; sıra 0-4)
#   sorular: deneme_yaz.py ile aynı biçim (z | kök, - şık || açıklama, = harf, > açıklama, ~ kaynak)
import json,os,re,sys
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem','konu')
def isle(ad,satirlar):
    p=f'{R}/{ad}.json';d=json.load(open(p));A=d['anlatim'];kutu=[];yeni=[];q=None
    on=re.match(r'([a-z]+\d*)-',d['sorular'][0]['id']).group(1);n=len(d['sorular'])
    for s in satirlar:
        if s.startswith('+merak ')or s.startswith('+sinav ')or s.startswith('+akil '):
            k,m=s[1:].split(' ',1);kutu.append({k:m})
        elif s.startswith('+ozet '):d['ozet'].append(s[6:])
        elif s.startswith('+kart '):o,a=s[6:].split(' || ');d['kartlar'].append({'o':o,'a':a})
        elif s.startswith('+z '):_,i,z=s.split();[x.update(z=int(z)) for x in d['sorular'] if x['id']==i]
        elif s.startswith('+duz '):
            _,i,k,m=s.split(' ',3);[x['ac'].__setitem__(int(k),m) for x in d['sorular'] if x['id']==i]
        elif re.match(r'^[123] \| ',s):
            z,k=s.split(' | ',1);n+=1;q={'id':f'{on}-{n:02d}','z':int(z),'s':k.replace(' // ','\n'),'c':[],'ac':[]};yeni.append(q)
        elif s.startswith('- '):c,a=s[2:].split(' || ');q['c'].append(c);q['ac'].append(a)
        elif s.startswith('= '):q['d']='ABCDE'.index(s[2])
        elif s.startswith('> '):q['a']=s[2:]
        elif s.startswith('~ '):q['kay']=s[2:]
    # kutuları anlatıma eşit aralıklarla dağıt (başlık öncesine)
    bas=[i for i,b in enumerate(A) if isinstance(b,dict) and 'b' in b] or [len(A)]
    for j,k in enumerate(kutu):
        hedef=bas[min(len(bas)-1,(j+1)*len(bas)//(len(kutu)+1))]
        A.insert(hedef+j,k)
    d['sorular']+=yeni
    json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(ad,'+',len(kutu),'kutu,',len(yeni),'soru')
akt=None;buf=[]
for s in open(sys.argv[1],encoding='utf-8').read().split('\n'):
    if s.startswith('#konu '):
        if akt:isle(akt,buf)
        akt=s.split()[1];buf=[]
    elif s.strip():buf.append(s)
if akt:isle(akt,buf)
