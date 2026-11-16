# YDS denemelerini üretir: tools/kaynak/yds/dN.txt (yazılı sorular) + okuma metinlerinden paragraf soruları
import json,os,hashlib,re,random
B='data/yds/banka.json'; d=json.load(open(B)); m=json.load(open('data/modern/modern.json'))
d['sorular']=[q for q in d['sorular'] if q.get('dn',1)==1]
for q in d['sorular']: q['dn']=1
d['pasajlar']={k:v for k,v in d['pasajlar'].items() if not re.match(r'd\d+_|m_',k)}
TIP={'K':'kelime','G':'gramer','T':'tamamlama','C':'ceviri','D':'diyalog','Y':'yakin'}
ROM=['I','II','III','IV','V']
def yer(i,n=5): return int(hashlib.md5(i.encode()).hexdigest(),16)%n
alan={}
for x in m['metinler']: alan.setdefault(x['alan'],[]).append(x)
AL=[a[0] for a in m['alanlar'] if a[0] in alan][:9]
rapor=[]
for N in range(2,11):
  f=f'tools/kaynak/yds/d{N}.txt'; say={}; out=[]; pc=0; cl=0
  R=random.Random(1000+N); POS=[0,1,2,3,4]*10; R.shuffle(POS); P4=[0,1,2,3]*8; R.shuffle(P4)
  if os.path.exists(f):
    for ln in open(f,encoding='utf-8'):
      ln=ln.rstrip('\n')
      if not ln.strip(): continue
      p=[x.strip() for x in ln.split('|')]; t=p[0]
      def ekle(tip,q,dogru,yan,a,pas=None):
        say[tip]=say.get(tip,0)+1; i=f'd{N}_{tip}{say[tip]}'
        assert len(yan)==4 and len(set(yan+[dogru]))==5,(N,ln[:60])
        say['_n']=say.get('_n',0)+1; pos=POS[(say['_n']-1)%len(POS)]; k=yan[:]; k.insert(pos,dogru)
        o={'id':i,'tip':tip,'q':q,'k':k,'d':pos,'a':a,'dn':N}
        if pas: o['p']=pas
        out.append(o)
      if t in TIP:
        assert len(p)==8,(N,len(p),ln[:60]); ekle(TIP[t],p[1].replace(' // ','\n'),p[2],p[3:7],p[7])
      elif t=='P': pc+=1; cl=0; d['pasajlar'][f'd{N}_c{pc}']=p[1]
      elif t=='L':
        assert len(p)==7,(N,ln[:60]); cl+=1; ekle('cloze',f'({cl}) numaralı boşluk',p[1],p[2:6],p[6],f'd{N}_c{pc}')
      elif t=='B':
        assert len(p)==8 and '----' in p[1],(N,ln[:60]); k=f'd{N}_b{say.get("bosluk",0)+1}'; d['pasajlar'][k]=p[1]
        ekle('bosluk','Parçada boş bırakılan yere hangi cümle gelmelidir?',p[2],p[3:7],p[7],k)
      elif t=='Z':
        assert len(p)==4 and p[2] in ROM and all(f'({r})' in p[1] for r in ROM),(N,ln[:60])
        say['bozan']=say.get('bozan',0)+1; i=f'd{N}_bozan{say["bozan"]}'; d['pasajlar'][f'd{N}_z{say["bozan"]}']=p[1]
        out.append({'id':i,'tip':'bozan','q':'Hangi cümle anlam bütünlüğünü bozar?','k':ROM,'d':ROM.index(p[2]),'a':p[3],'p':f'd{N}_z{say["bozan"]}','dn':N})
      else: raise SystemExit(f'bilinmeyen satır d{N}: {ln[:50]}')
  if not out: continue
  # okuma: her alandan (N-2). metin + bir ek metin
  ms=[alan[a][N-2] for a in AL if len(alan[a])>N-2]
  ek=alan[AL[(N-2)%len(AL)]]
  if len(ek)>9: ms.append(ek[9])
  pn=0
  for x in ms:
    pk='m_'+x['id']; d['pasajlar'][pk]=' '.join(x['ar'])
    for q in x['sorular'][:3]:
      pn+=1; kk=q['k'][:]; dg=kk.pop(q['d']); R.shuffle(kk); np_=P4[(pn-1)%len(P4)]%(len(kk)+1); kk.insert(np_,dg)
      out.append({'id':f'd{N}_paragraf{pn}','tip':'paragraf','q':q['s'],'k':kk,'d':np_,'a':q.get('a',''),'p':pk,'dn':N})
  d['sorular']+=out; say.pop('_n',None); rapor.append((N,len(out),dict(say),pn))
ids=[q['id'] for q in d['sorular']]; assert len(ids)==len(set(ids))
for q in d['sorular']: assert 0<=q['d']<len(q['k']) and (not q.get('p') or q['p'] in d['pasajlar']),q['id']
json.dump(d,open(B,'w'),ensure_ascii=False,separators=(',',':'))
print(len(d['sorular']),rapor)
