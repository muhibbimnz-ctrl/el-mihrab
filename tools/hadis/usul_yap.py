# OpenITI usûl kitaplarını başlıklara göre bölümlere ayırır -> data/usul/<id>.json, data/usul/liste.json
import re,json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));from openiti import clean
KB=[('marife','0405HakimNaysaburi.MacrifatCulumHadith','Ma‘rifetü Ulûmi’l-Hadîs','معرفة علوم الحديث','Hâkim en-Nîsâbûrî (v. 405)'),
('kifaye','0463KhatibBaghdadi.KifayaFiCilmRiwaya','el-Kifâye fî İlmi’r-Rivâye','الكفاية في علم الرواية','Hatîb el-Bağdâdî (v. 463)'),
('cami','0463KhatibBaghdadi.JamicLiAkhlaqRawiWaAdabSamic','el-Câmi‘ li-Ahlâki’r-Râvî ve Âdâbi’s-Sâmi‘','الجامع لأخلاق الراوي وآداب السامع','Hatîb el-Bağdâdî (v. 463)'),
('mukaddime','0643IbnSalahShahrazuri.MuqaddimatCulumHadith','Mukaddimetü İbni’s-Salâh','مقدمة ابن الصلاح','İbnü’s-Salâh (v. 643)'),
('mukiza','0748Dhahabi.MuqizaFiCilmMustalahHadith','el-Mûkıza','الموقظة في علم مصطلح الحديث','Zehebî (v. 748)'),
('elfiyeiraki','0806IbnHusaynZaynDinCiraqi.AlfiyyatTabsira','Elfiyyetü’l-Irâkî (et-Tabsıra ve’t-Tezkira)','ألفية العراقي','Zeynüddîn el-Irâkî (v. 806)'),
('nuhbe','0852IbnHajarCasqalani.NukhbatFikar','Nuhbetü’l-Fiker','نخبة الفكر','İbn Hacer (v. 852)'),
('nuzhe','0852IbnHajarCasqalani.NuzhatNazar','Nüzhetü’n-Nazar','نزهة النظر','İbn Hacer (v. 852)'),
('hedyussari','0852IbnHajarCasqalani.MuqaddimatFathBari','Hedyü’s-Sârî (Fethu’l-Bârî mukaddimesi)','هدي الساري','İbn Hacer (v. 852)'),
('fethulmugis','0902Sakhawi.FathMughith','Fethu’l-Muğîs','فتح المغيث','Sehâvî (v. 902)'),
('tedrib','0911Suyuti.TadribRawi','Tedrîbü’r-Râvî','تدريب الراوي','Süyûtî (v. 911)'),
('elfiyesuyuti','0911Suyuti.AlfiyyaFiCilmHadith','Elfiyyetü’s-Süyûtî','ألفية السيوطي','Süyûtî (v. 911)')]
yollar={}
for ln in open('/tmp/oiti/usul_sec.txt'):
    b,f=ln.split();yollar[f.split('/')[2]]='/tmp/oiti/'+b+'/'+f
yollar['0748Dhahabi.MuqizaFiCilmMustalahHadith']='/tmp/oiti/0750AH/data/0748Dhahabi/0748Dhahabi.MuqizaFiCilmMustalahHadith/0748Dhahabi.MuqizaFiCilmMustalahHadith.Shamela0008195-ara1'
os.makedirs('data/usul',exist_ok=True);L=[]
for k,pre,ad,ar,mu in KB:
    raw=open(yollar[pre],encoding='utf-8').read().split('#META#Header#End#')[-1]
    S=[];cur=None;cp=None
    for line in raw.splitlines():
        if line.startswith('### '):
            m=re.match(r'^###\s*(\|+)\s*(.*)',line);lv=len(m.group(1)) if m else 1;t=clean(m.group(2) if m else line[4:])
            if not t: continue
            if lv<=2 or cur is None: cur=[t,[]];S.append(cur)
            else: cur[1].append('**'+t+'**')
            cp=None
        elif line.startswith('# '):
            t=clean(line[2:])
            if t and cur is None: cur=['مقدمة',[]];S.append(cur)
            if t: cur[1].append(t);cp=len(cur[1])-1
        elif line.startswith('~~') and cur and cp is not None:
            t=clean(line[2:])
            if t: cur[1][cp]+=' '+t
    S=[[t,'\n\n'.join(p)] for t,p in S if p]
    # çok küçük bölümleri öncekine kat
    M=[]
    for t,x in S:
        if M and len(x)<120: M[-1][1]+='\n\n**'+t+'**\n\n'+x
        else: M.append([t,x])
    P=[]
    for t,x in M:
        if len(x)<=15000: P.append([t,x]);continue
        par=x.split('\n\n');buf=[];n=1
        for p in par:
            buf.append(p)
            if sum(len(q) for q in buf)>8000: P.append([t+(f' ({n})' if True else ''),'\n\n'.join(buf)]);buf=[];n+=1
        if buf: P.append([t+f' ({n})','\n\n'.join(buf)])
    M=P
    json.dump({'s':M},open(f'data/usul/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    L.append(dict(k=k,ad=ad,ar=ar,muellif=mu,bolum=len(M)));print(k,len(M),sum(len(x) for _,x in M)//1000,'k')
json.dump(L,open('data/usul/liste.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
