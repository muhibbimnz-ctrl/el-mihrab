# OpenITI hadis kitaplarını data/hadis/<id>/<n>.json parçalarına böler, kutub.json'a ekler. Girdi: /tmp/oiti
import sys,os,json,glob,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import openiti
KB=[('hemmam','0132HammamIbnMunabbih.Sahifa','Sahîfetü Hemmâm b. Münebbih','صحيفة همام بن منبه','Hemmâm b. Münebbih (v. 132)','Müsnedler'),
('ibnmubarek','0181IbnMubarak.Musnad','Müsned-i İbnü’l-Mübârek','مسند ابن المبارك','Abdullah b. el-Mübârek (v. 181)','Müsnedler'),
('safii','0204Shafici.Musnad','Müsned-i Şâfiî','مسند الشافعي','İmam Şâfiî (v. 204)','Müsnedler'),
('humeydi','0219IbnZubayrHumaydi.Musnad','Müsned-i Humeydî','مسند الحميدي','Humeydî (v. 219)','Müsnedler'),
('ibnrahuye','0238IbnRahawayh.Musnad','Müsned-i İshâk b. Râhûye','مسند إسحاق بن راهويه','İshâk b. Râhûye (v. 238)','Müsnedler'),
('ibnhuzeyme','0311IbnKhuzaymaNaysaburi.Sahih','Sahîh-i İbn Huzeyme','صحيح ابن خزيمة','İbn Huzeyme (v. 311)','Sahihler'),
('mustedrek','0405HakimNaysaburi.Mustadrak','el-Müstedrek ale’s-Sahîhayn','المستدرك على الصحيحين','Hâkim en-Nîsâbûrî (v. 405)','Sahihler'),
('safiisunen','0204Shafici.SunanMathura','es-Sünenü’l-Me’sûre','السنن المأثورة','İmam Şâfiî (v. 204)','Sünenler'),
('saidmansur','0227IbnMansurKhurasani.Sunan','Sünen-i Saîd b. Mansûr','سنن سعيد بن منصور','Saîd b. Mansûr (v. 227)','Sünenler'),
('darekutni','0385Daraqutni.Sunan','Sünen-i Dârekutnî','سنن الدارقطني','Dârekutnî (v. 385)','Sünenler'),
('beyhaki','0458Bayhaqi.SunanKubra','es-Sünenü’l-Kübrâ','السنن الكبرى للبيهقي','Beyhakî (v. 458)','Sünenler'),
('ibnebiseybe','0235IbnAbiShayba.Musannaf','el-Musannef','مصنف ابن أبي شيبة','İbn Ebî Şeybe (v. 235)','Musannefler'),
('taberanikebir','0360Tabarani.MucjamKabir','el-Mu‘cemü’l-Kebîr','المعجم الكبير للطبراني','Taberânî (v. 360)','Mu‘cemler'),
('taberanisagir','0360Tabarani.MucjamSaghir','el-Mu‘cemü’s-Sağîr','المعجم الصغير للطبراني','Taberânî (v. 360)','Mu‘cemler')]
K=json.load(open('data/hadis/kutub.json',encoding='utf-8'));ids={x[0] for x in KB};K=[b for b in K if b['k'] not in ids]
N=200
for k,pre,ad,ar,mu,gr in KB:
    f=[x for x in glob.glob(f'/tmp/oiti/*/data/*/{pre}/{pre}*') if not x.endswith('.yml')][0]
    H=openiti.parse(open(f,encoding='utf-8').read());os.makedirs(f'data/hadis/{k}',exist_ok=True)
    for x in glob.glob(f'data/hadis/{k}/*.json'): os.remove(x)
    secs=[]
    for i in range(0,len(H),N):
        p=H[i:i+N];n=i//N+1;C=[];h=[]
        for x in p:
            if not C or C[-1]!=x['ch']: C.append(x['ch'])
            h.append([x['p'],x['t'],len(C)-1])
        json.dump({'c':C,'h':h},open(f'data/hadis/{k}/{n}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
        bas=(p[0]['ch'] or '').strip()[:60]
        secs.append([str(n),f'{p[0]["p"]}–{p[-1]["p"]}'+(f' · {bas}' if bas else ''),len(p),p[0]['p'],p[-1]['p']])
    K.append(dict(k=k,src='yerel',ad=ad,ar=ar,muellif=mu,grup=gr,tr=False,adet=len(H),b=secs,kaynak='OpenITI külliyatı (CC BY-NC-SA 4.0), Arapça; numaralar baskı numarasıdır'))
    print(k,len(H),len(secs))
json.dump(K,open('data/hadis/kutub.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
# Takrîbü't-Tehzîb: râvî biyografileri (sened paneli için)
f=glob.glob('/tmp/oiti/*/data/*/0852IbnHajarCasqalani.TaqribTahdhib/*-ara1')[0]
T=openiti.parse(open(f,encoding='utf-8').read())
json.dump([[x['p'],x['t']] for x in T],open('data/hadis/takrib.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print('takrib',len(T))
