# Ek OpenITI fıkıh/usûl kitapları -> data/fikih/<k>.json (+ büyükler için data/fikih/<k>/<n>.json parçaları), liste.json'a ekler
import re,json,os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','hadis'));from openiti import clean
H='Hanefî';HU='Usûl-i fıkıh'
KB=[
('fikhekber','0150AbuHanifa.FiqhAkbar','el-Fıkhu’l-Ekber','الفقه الأكبر','Ebû Hanîfe (v. 150) · İmam-ı Âzam’ın risâleleri'),
('fikhebsat','0150AbuHanifa.FiqhAbsat','el-Fıkhu’l-Ebsat','الفقه الأبسط','Ebû Hanîfe (Ebû Mutî‘ rivâyeti) · İmam-ı Âzam’ın risâleleri'),
('vasiyye','0150AbuHanifa.Wasiyya','el-Vasiyye','الوصية','Ebû Hanîfe (v. 150) · İmam-ı Âzam’ın risâleleri'),
('nurizah','1069IbnCammarShurunbulali.NurIdah','Nûru’l-Îzâh','نور الإيضاح ونجاة الأرواح','Şürünbülâlî (v. 1069) · '+H),
('meraki','1069IbnCammarShurunbulali.MaraqiFalahSharhNurIdah','Merâki’l-Felâh','مراقي الفلاح شرح نور الإيضاح','Şürünbülâlî (v. 1069) · '+H),
('lubab','1298IbnTalibDimashqiMaydani.LubabFiSharhKitab','el-Lübâb fî Şerhi’l-Kitâb','اللباب في شرح الكتاب','Meydânî (v. 1298) · '+H),
('tuhfe','0540IbnAhmadCalaDinSamarqandi.TuhfatFuqaha','Tuhfetü’l-Fukahâ','تحفة الفقهاء','Alâeddîn es-Semerkandî (v. 540) · '+H),
('bedai','0587IbnMascudCalaDinKasani.BadaicSanaic','Bedâiu’s-Sanâi‘','بدائع الصنائع في ترتيب الشرائع','Kâsânî (v. 587) · '+H),
('mebsut','0483IbnAhmadSarakhsi.Mabsut','el-Mebsût','المبسوط','Serahsî (v. 483) · '+H),
('tebyin','0743FakhrDinZaylaci.TabyinHaqaiq','Tebyînü’l-Hakâik','تبيين الحقائق شرح كنز الدقائق','Zeylaî (v. 743) · '+H),
('durer','0885IbnFaramurzMullaKhusraw.DurarHukkam','Dürerü’l-Hükkâm','درر الحكام شرح غرر الأحكام','Molla Hüsrev (v. 885) · '+H),
('durrmuhtar','1088IbnCaliHaskafi.DurrMukhtar','ed-Dürrü’l-Muhtâr','الدر المختار شرح تنوير الأبصار','Haskefî (v. 1088) · '+H),
('reddulmuhtar','1252IbnCabidinDimashqi.RaddMukhtar','Reddü’l-Muhtâr (İbn Âbidîn Hâşiyesi)','رد المحتار على الدر المختار','İbn Âbidîn (v. 1252) · '+H),
('ihtilaf','0370IbnCaliJassas.MukhtasarIkhtilafCulama','Muhtasaru İhtilâfi’l-Ulemâ','مختصر اختلاف العلماء','Cessâs (v. 370) · Mukayeseli (Hanefî)'),
('mecelle','1300Anonymous.MajallatAhkam','Mecelle-i Ahkâm-ı Adliyye','مجلة الأحكام العدلية','Ahmed Cevdet Paşa heyeti (1293) · '+H),
('halil','0767KhalilIbnIshaq.MukhtasarKhalil','Muhtasaru Halîl','مختصر خليل','Halîl b. İshâk (v. 776) · Mâlikî'),
('muhezzeb','0476AbuIshaqShirazi.MuhadhdhabFiFiqh','el-Mühezzeb','المهذب في فقه الإمام الشافعي','Ebû İshâk eş-Şîrâzî (v. 476) · Şâfiî'),
('hiraki','0334IbnHusaynKhiraqi.MukhtasarMinMasailIbnHanbal','Muhtasaru’l-Hırakî','مختصر الخرقي','Hırakî (v. 334) · Hanbelî'),
('kerhi','0340AbuHasanKarkhi.Usul','Usûlü’l-Kerhî','أصول الكرخي','Kerhî (v. 340) · '+HU+' (Hanefî)'),
('sasi','0344NizamDinShashi.Usul','Usûlü’ş-Şâşî','أصول الشاشي','Nizâmeddîn eş-Şâşî · '+HU+' (Hanefî)'),
('fusul','0370IbnCaliJassas.FusulFiUsul','el-Fusûl fi’l-Usûl','الفصول في الأصول','Cessâs (v. 370) · '+HU+' (Hanefî)'),
('takvim','0430AbuZaydDabusi.Taqwim','Takvîmü’l-Edille','تقويم الأدلة','Debûsî (v. 430) · '+HU+' (Hanefî)'),
('tesis','0430AbuZaydDabusi.TasisNazar','Te’sîsü’n-Nazar','تأسيس النظر','Debûsî (v. 430) · '+HU+' (Hanefî)'),
('pezdevi','0482IbnMuhammadBazdawi.KanzWusul','Usûlü’l-Pezdevî (Kenzü’l-Vüsûl)','كنز الوصول إلى معرفة الأصول','Pezdevî (v. 482) · '+HU+' (Hanefî)'),
('serahsiusul','0483IbnAhmadSarakhsi.Usul','Usûlü’s-Serahsî','أصول السرخسي','Serahsî (v. 483) · '+HU+' (Hanefî)'),
('menar','0710IbnAhmadHafizDinNasafi.ManarAnwar','Menârü’l-Envâr','منار الأنوار','Nesefî (v. 710) · '+HU+' (Hanefî)'),
('telvih','0792IbnCumarTaftazani.TalwihCalaTawdih','et-Telvîh ale’t-Tavzîh','التلويح على التوضيح','Teftâzânî (v. 792) · '+HU+' (Hanefî)'),
('esbah','0970IbnIbrahimIbnNujaymMisri.AshbahWaNazair','el-Eşbâh ve’n-Nezâir','الأشباه والنظائر','İbn Nüceym (v. 970) · Kavâid (Hanefî)'),
('risalesafii','0204Shafici.Risala','er-Risâle','الرسالة','İmam Şâfiî (v. 204) · '+HU+' (Mütekellimîn)'),
('burhan','0478ImamHaramaynJuwayni.BurhanFiUsulFiqh','el-Burhân','البرهان في أصول الفقه','Cüveynî (v. 478) · '+HU+' (Mütekellimîn)'),
('mustasfa','0505Ghazali.Mustasfa','el-Mustasfâ','المستصفى','Gazzâlî (v. 505) · '+HU+' (Mütekellimîn)'),
('mahsul','0606FakhrDinRazi.Mahsul','el-Mahsûl','المحصول','Fahreddîn er-Râzî (v. 606) · '+HU+' (Mütekellimîn)'),
('ihkam','0631SayfDinAmidi.IhkamFiUsulAhkam','el-İhkâm fî Usûli’l-Ahkâm','الإحكام في أصول الأحكام','Âmidî (v. 631) · '+HU+' (Mütekellimîn)'),
('minhacvusul','0685NasirDinBaydawi.MatnMinhajWusul','Minhâcü’l-Vüsûl','منهاج الوصول إلى علم الأصول','Beyzâvî (v. 685) · '+HU+' (Mütekellimîn)'),
('furuk','0684ShihabDinQarafi.Furuq','el-Furûk','الفروق','Karâfî (v. 684) · Kavâid (Mâlikî)'),
('muvafakat','0790IbnMusaGharnatiShatibi.Muwafaqat','el-Muvâfakât','الموافقات','Şâtıbî (v. 790) · Makâsıd (Mâlikî)'),
]
CH=600_000  # parça başına karakter
L=json.load(open('data/fikih/liste.json',encoding='utf-8'));L=[x for x in L if x['k'] not in {k for k,*_ in KB}]
for k,pre,ad,ar,mu in KB:
    raw=open(f'/tmp/oiti/f_{pre}.txt',encoding='utf-8').read().split('#META#Header#End#')[-1]
    S=[];cur=None;cp=None
    for line in raw.splitlines():
        if line.startswith('### '):
            m=re.match(r'^###\s*(\|+)\s*(.*)',line);lv=len(m.group(1)) if m else 1;t=clean(m.group(2) if m else line[4:])
            if not t: continue
            if lv<=2 or cur is None: cur=[t[:120],[]];S.append(cur)
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
    M=[]
    for t,x in S:
        if M and len(x)<120: M[-1][1]+='\n\n**'+t+'**\n\n'+x
        else: M.append([t,x])
    P=[]
    for t,x in M:
        if len(x)<=15000: P.append([t,x]);continue
        buf=[];n=1
        for p in x.split('\n\n'):
            buf.append(p)
            if sum(len(q) for q in buf)>8000: P.append([f'{t} ({n})','\n\n'.join(buf)]);buf=[];n+=1
        if buf: P.append([f'{t} ({n})','\n\n'.join(buf)])
    M=P;top=sum(len(x) for _,x in M)
    if not M: print('BOŞ',k);continue
    if top<=1_000_000:
        json.dump({'s':M},open(f'data/fikih/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    else:
        os.makedirs(f'data/fikih/{k}',exist_ok=True);idx=[];parca=[];c=0;boy=0
        for t,x in M:
            if boy+len(x)>CH and parca:
                json.dump({'t':parca},open(f'data/fikih/{k}/{c}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'));c+=1;parca=[];boy=0
            idx.append([t,'',c,len(parca)]);parca.append(x);boy+=len(x)
        json.dump({'t':parca},open(f'data/fikih/{k}/{c}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
        json.dump({'s':idx,'c':c+1},open(f'data/fikih/{k}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    L.append(dict(k=k,ad=ad,ar=ar,muellif=mu,bolum=len(M)));print(k,len(M),top//1000,'k')
json.dump(L,open('data/fikih/liste.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
