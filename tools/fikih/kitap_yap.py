# OpenITI usûl kitaplarını başlıklara göre bölümlere ayırır -> data/fikih/<id>.json, data/fikih/liste.json
import re,json,os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','hadis'));from openiti import clean
KB=[('kuduri','0428AbuHusaynQuduri.Mukhtasar','Muhtasarü’l-Kudûrî','مختصر القدوري','Kudûrî (v. 428) · Hanefî'),
('hidaye','0593BurhanDinFarghaniMarghinani.HidayaFiSharhBidaya','el-Hidâye','الهداية في شرح بداية المبتدي','Merğînânî (v. 593) · Hanefî'),
('ihtiyar','0683IbnMahmudMajdDinMawsili.IkhtiyarLiTaclil','el-İhtiyâr li-Ta‘lîli’l-Muhtâr','الاختيار لتعليل المختار','Mevsılî (v. 683) · Hanefî'),
('kenz','0710IbnAhmadHafizDinNasafi.KanzDaqaiq','Kenzü’d-Dekâik','كنز الدقائق','Nesefî (v. 710) · Hanefî'),
('bidaye','0595IbnRushdHafid.BidayatMujtahid','Bidâyetü’l-Müctehid','بداية المجتهد ونهاية المقتصد','İbn Rüşd (v. 595) · Mukayeseli (Mâlikî)'),
('risale','0386IbnAbiZaydQayrawani.Risala','er-Risâle','الرسالة','İbn Ebî Zeyd el-Kayrevânî (v. 386) · Mâlikî'),
('minhac','0676Nawawi.MinhajTalibin','Minhâcü’t-Tâlibîn','منهاج الطالبين','Nevevî (v. 676) · Şâfiî'),
('umde','0620IbnQudamaMaqdisi.CumdatFiqh','Umdetü’l-Fıkh','عمدة الفقه','İbn Kudâme (v. 620) · Hanbelî')]
yollar={}
for ln in open('/tmp/oiti/fikih_sec.txt'):
    if len(ln.split())<2: continue
    b,f=ln.split();yollar[f.split('/')[2]]='/tmp/oiti/'+b+'/'+f
_x='/tmp/oiti/0750AH/data/0748Dhahabi/0748Dhahabi.MuqizaFiCilmMustalahHadith/0748Dhahabi.MuqizaFiCilmMustalahHadith.Shamela0008195-ara1'
os.makedirs('data/fikih',exist_ok=True);L=[]
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
    json.dump({'s':M},open(f'data/fikih/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    L.append(dict(k=k,ad=ad,ar=ar,muellif=mu,bolum=len(M)));print(k,len(M),sum(len(x) for _,x in M)//1000,'k')
json.dump(L,open('data/fikih/liste.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
