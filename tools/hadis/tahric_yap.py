# Otomatik tahrîc: 32 kitaptaki rivayetlerin metin (matn) benzerliğinden ortak rivayetleri bulur.
# Girdi: data/hadis/ara/*.json  Çıktı: data/hadis/tahric/<kitap>.json = {ref: [[kitap, ref, yüzde], ...]}
import json,glob,os,re,zlib,numpy as np,time
t0=time.time()
K=json.load(open('data/hadis/kutub.json',encoding='utf-8'));kits=[b['k'] for b in K]
PR=re.compile(r'(صلي الله عليه وسلم|صلى الله عليه وسلم|رسول الله|النبي)')
DOC=[];SH=[];DI=[]
for bi,k in enumerate(kits):
    for r in json.load(open(f'data/hadis/ara/{k}.json',encoding='utf-8')):
        t=r[1];m=PR.search(t);w=(t[m.end():] if m else t).split()
        if not m: w=w[len(w)*2//5:]
        w=[x for x in w if x not in ('صلي','صلى','الله','عليه','وسلم','قال','قالت','يقول','ان','عن','في','من','و')][:45]
        if len(w)<6: continue
        di=len(DOC);DOC.append((bi,r[0]))
        hs={zlib.crc32((' '.join(w[i:i+3])).encode()) for i in range(len(w)-2)}
        SH.extend(hs);DI.extend([di]*len(hs))
print('belge',len(DOC),'shingle',len(SH),round(time.time()-t0))
SH=np.array(SH,dtype=np.uint32);DI=np.array(DI,dtype=np.int32)
nsh=np.bincount(DI,minlength=len(DOC)).astype(np.float32)
o=np.argsort(SH,kind='stable');SH=SH[o];DI=DI[o]
b=np.flatnonzero(np.diff(SH))+1;st=np.r_[0,b];en=np.r_[b,len(SH)];sz=en-st
sec=(sz>=2)&(sz<=40);st=st[sec];en=en[sec];print('grup',len(st),round(time.time()-t0))
N=len(DOC);pairs=[]
buf=[]
for s,e in zip(st,en):
    d=DI[s:e];
    if len(d)==2: buf.append(int(d[0])*N+int(d[1]) if d[0]<d[1] else int(d[1])*N+int(d[0]));continue
    d=np.sort(d);i,j=np.triu_indices(len(d),1);buf.extend((d[i].astype(np.int64)*N+d[j]).tolist())
    if len(buf)>20_000_000: pairs.append(np.array(buf,dtype=np.int64));buf=[]
pairs.append(np.array(buf,dtype=np.int64));P=np.concatenate(pairs);del pairs,buf
print('çift',len(P),round(time.time()-t0))
u,c=np.unique(P,return_counts=True);del P
a=(u//N).astype(np.int64);bb=(u%N).astype(np.int64)
sc=c/np.minimum(nsh[a],nsh[bb]);keep=(c>=3)&(sc>=0.3)
a=a[keep];bb=bb[keep];sc=sc[keep];print('bağ',len(a),round(time.time()-t0))
L={}
for x,y,s in zip(a.tolist(),bb.tolist(),sc.tolist()):
    p=min(100,int(round(s*100)))
    L.setdefault(x,[]).append((p,y));L.setdefault(y,[]).append((p,x))
os.makedirs('data/hadis/tahric',exist_ok=True);out={k:{} for k in kits}
for d,ls in L.items():
    bi,ref=DOC[d];ls.sort(reverse=True)
    # her kitaptan en iyi 3, toplam 12
    say={};sec=[]
    for p,y in ls:
        by=DOC[y][0]
        if say.get(by,0)>=3: continue
        say[by]=say.get(by,0)+1;sec.append([kits[by],DOC[y][1],p])
        if len(sec)>=12: break
    out[kits[bi]][json.dumps(ref,ensure_ascii=False,separators=(',',':'))]=sec
top=0
for k,v in out.items():
    json.dump(v,open(f'data/hadis/tahric/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    top+=os.path.getsize(f'data/hadis/tahric/{k}.json')
print('kitap dosyaları',top//1024//1024,'MB',round(time.time()-t0),'sn')
