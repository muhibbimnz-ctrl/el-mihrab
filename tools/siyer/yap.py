# data/siyer/olaylar.json, yerler.json, ayet.json üretir ve hadis/fıkıh bağlantılarını denetler
import json,os,re,importlib.util
from urllib.parse import quote
D=os.path.dirname(os.path.abspath(__file__));R=os.path.dirname(os.path.dirname(D))
sp=importlib.util.spec_from_file_location('o',os.path.join(D,'olaylar.py'));o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o)
MS={x['id'] for x in json.load(open(os.path.join(R,'data/fikih/meseleler.json')))}
K=json.load(open(os.path.join(R,'data/hadis/kutub.json')))
def an(t):
    t=re.sub('[ً-ٰـۖ-ۭ‌-‏]','',t);t=re.sub('[أإآٱ]','ا',t).replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return re.sub(r'\s+',' ',re.sub('[^ء-ي\\s]',' ',t)).strip()
C={};S=['bukhari','muslim','abudawud','tirmidhi','nasai','ibnmajah']
def kit(kap):
    if kap=='sitte':return S
    if kap=='tisa':return S+['malik','ahmed','darimi']
    if kap.startswith('k:'):return [kap[2:]]
    return [b['k'] for b in K]
GL={'umre':'Kâbe’yi ziyaret ibadeti; yılın her zamanı yapılabilir.','ihram':'Hac veya umreye niyet edip bazı mubahları kendine yasaklamak.','münafık':'Müslüman görünüp içten inanmayan kimse.','ganimet':'Savaşta düşmandan alınan mal.','müttefik':'Antlaşmayla birbirine bağlı taraf.','Ensar':'Medineli Müslümanlar; “yardımcılar.”','Muhacir':'Mekke’den Medine’ye göç eden Müslümanlar.','hutbe':'Topluluğa yapılan dinî konuşma.','menâsik':'Haccın yapılış adımları.','fidye':'Kurtulmak için ödenen bedel.','sancak':'Ordunun bayrağı.','kuşatma':'Bir yeri dört bir yandan sarıp çevirme.','müstahkem':'Sağlam, tahkim edilmiş.','tövbe':'Günahtan pişman olup Allah’a dönmek.','ashab':'Peygamber’in arkadaşları, sahâbîler.','sahâbî':'Peygamber’i görüp ona iman eden ve Müslüman olarak ölen kişi.','gazve':'Peygamber’in bizzat katıldığı sefer.','himaye':'Koruma, sahip çıkma.','kervan':'Yük taşıyan deve kafilesi.','tebliğ':'Dini insanlara ulaştırma.','kıble':'Namazda yönelinen yön, Kâbe.','cahiliye':'İslam’dan önceki bilgisizlik ve putperestlik dönemi.','vakf':'Bir malı hayır için kalıcı olarak ayırmak.','ribâ':'Faiz.','esir':'Savaşta yakalanan kişi.','şehit':'Allah yolunda öldürülen.','putperest':'Putlara tapan.','teselli':'Acısını hafifletme, avutma.','dedikodu':'Arkadan konuşma, söylenti.','müjde':'Sevindirici haber.','risalet':'Peygamberlik görevi.','dua':'Allah’a yalvarma.','istişare':'Danışma, fikir alışverişi.','antlaşma':'Taraflar arasında yapılan söz ve sözleşme.','vadi':'İki dağ arasındaki çukur arazi.','nübüvvet':'Peygamberlik.','fetih':'Bir yerin İslam hâkimiyetine girmesi; zafer.','sebat':'Kararlılıkla yerinde durmak.','pusu':'Düşmanı gizlenerek beklemek.','bahane':'Asıl sebebi gizlemek için ileri sürülen sebep.','vasiyet':'Ölmeden önce yapılan son tavsiye.','hâmi':'Koruyucu.'}
def glosla(p,kul):
    for w,a in GL.items():
        if w in kul:continue
        m=re.search(r'(?<![\w{|])('+re.escape(w)+r')',p,flags=re.I)
        if m and '{' not in p[max(0,m.start()-40):m.start()].split('}')[-1]:
            p=p[:m.start()]+'{'+m.group(1)+'|'+a+'}'+p[m.end():];kul.add(w)
    return p
out=[];AY={};hata=0
for x in o.O:
    assert x['yer'] in o.YER,x['yer']
    for f in x['fikih']:
        if f not in MS: print('fıkıh yok',x['id'],f);hata+=1
    hd=[]
    for et,q,kap,ac in x['hadis']:
        W=an(q).split(' ');n=0
        for k in kit(kap):
            fp=os.path.join(R,f'data/hadis/ara/{k}.json')
            if not os.path.exists(fp):continue
            if k not in C:C[k]=json.load(open(fp))
            n+=sum(1 for r in C[k] if all(w in r[1] for w in W))
        if n==0 or n>80: print('hadis',x['id'],et,q,kap,n);hata+=1
        hd.append([et,'hadis.html#ara='+quote(q)+'&kap='+kap,ac])
    y=dict(x);y['hadis']=hd;y['ayet']=[[a,'./#'+r,n] for a,r,n in x['ayet']];kul=set();y['metin']=[glosla(p,kul) for p in x['metin'].strip().split('\n')]
    out.append(y)
    for a,r,n in x['ayet']: AY.setdefault(r,[]).append([x['id'],x['baslik']])
json.dump(out,open(os.path.join(R,'data/siyer/olaylar.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
json.dump({k:list(v) for k,v in o.YER.items()},open(os.path.join(R,'data/siyer/yerler.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
json.dump(AY,open(os.path.join(R,'data/siyer/ayet.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'bölüm,',len(AY),'âyet, sorunlu',hata)
