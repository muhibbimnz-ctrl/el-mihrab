# OpenITI'den asıl metin romanlar/edebî eserler -> data/roman/<id>.json (uzun biçim), liste.json'a ekler
import re,json,os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','hadis'));from openiti import clean
Z='Corcî Zeydân (ö. 1914) · asıl metin';ZG='Corcî Zeydân romanları — asıl metin'
KG='Klasik Arap edebiyatı — asıl metin'
KB=[
('z_endulus','1331JurjiZaydan.FathAndalus','فتح الأندلس','Fethu’l-Endelüs — Endülüs’ün fethi','B2',Z,ZG),
('z_nasir','1331JurjiZaydan.CabdRahmanNasir','عبد الرحمن الناصر','Abdurrahmân en-Nâsır — Kurtuba’nın altın çağı','B2',Z,ZG),
('z_kurays','1331JurjiZaydan.CadhraQuraysh','عذراء قريش','Azrâu Kureyş — Kureyşli kız (Hz. Osman dönemi)','B2',Z,ZG),
('z_kerbela','1331JurjiZaydan.GhadatKarbala','غادة كربلاء','Ğâdetü Kerbelâ — Kerbelâ’nın kızı','B2',Z,ZG),
('z_haccac','1331JurjiZaydan.HajjajIbnYusuf','الحجاج بن يوسف','Haccâc b. Yûsuf','B2',Z,ZG),
('z_ebumuslim','1331JurjiZaydan.AbuMuslimKhurasani','أبو مسلم الخراساني','Ebû Müslim el-Horasânî — Abbâsî ihtilâli','B2',Z,ZG),
('z_abbase','1331JurjiZaydan.CabbasaUkhtRashid','العباسة أخت الرشيد','el-Abbâse — Hârûnürreşîd’in kız kardeşi','B2',Z,ZG),
('z_emin','1331JurjiZaydan.AminWaMamun','الأمين والمأمون','Emîn ve Me’mûn — iki kardeşin savaşı','B2',Z,ZG),
('z_fergane','1331JurjiZaydan.CarusFarghana','عروس فرغانة','Arûsu Fergâne — Fergâne gelini','B2',Z,ZG),
('z_tolun','1331JurjiZaydan.AhmadIbnTulun','أحمد بن طولون','Ahmed b. Tolun — Mısır’da Tolunoğulları','B2',Z,ZG),
('z_kayrevan','1331JurjiZaydan.FatatQayruwan','فتاة القيروان','Fetâtü’l-Kayrevân — Kayrevanlı kız','B2',Z,ZG),
('z_gassan','1331JurjiZaydan.FatatGhassan','فتاة غسان','Fetâtu Ğassân — Gassanlı kız (fetihler)','B2',Z,ZG),
('z_armanusa','1331JurjiZaydan.ArmanusaMisriyya','أرمانوسة المصرية','Armânûsa — Mısır’ın fethi','B2',Z,ZG),
('z_ramazan','1331JurjiZaydan.Ramadan','١٧ رمضان','17 Ramazan — Hz. Ali’nin şehadeti','B2',Z,ZG),
('z_mutemehdi','1331JurjiZaydan.AsirMutamahdi','أسير المتمهدي','Mehdî’nin esiri — Sudan','B2',Z,ZG),
('z_memluk','1331JurjiZaydan.MamlukSharid','المملوك الشارد','Kaçak Memlûk','B2',Z,ZG),
('z_istibdad','1331JurjiZaydan.IstibdadMamalik','استبداد المماليك','Memlûklerin istibdadı','B2',Z,ZG),
('z_cihad','1331JurjiZaydan.JihadMuhibbin','جهاد المحبين','Cihâdü’l-Muhibbîn — âşıkların mücadelesi','B2',Z,ZG),
('z_inkilab','1331JurjiZaydan.InqilabCuthmani','الانقلاب العثماني','Osmanlı inkılâbı (1908)','B2',Z,ZG),
('menfaluti','1342MustafaLutfiManfaluti.Cabarat','العبرات','el-Abarât — Gözyaşları (hikâyeler)','B2','Mustafa Lutfî el-Menfelûtî (ö. 1924) · asıl metin',KG),
('itibar','0584IbnMunqidhShayzari.Ictibar','كتاب الاعتبار','Kitâbü’l-İ‘tibâr — Haçlılar devrinde bir şövalyenin hatıraları','C1','Üsâme b. Munkız (ö. 584) · asıl metin',KG),
('cubeyr','0614IbnJubayr.Rihla','رحلة ابن جبير','İbn Cübeyr Seyahatnamesi','C1','İbn Cübeyr (ö. 614) · asıl metin',KG),
('buhala','0255Jahiz.Bukhala','كتاب البخلاء','Kitâbü’l-Buhalâ — Cimriler','C1','Câhiz (ö. 255) · asıl metin',KG),
('hemedani','0398BadicZamanHamadhani.Maqamat','مقامات بديع الزمان','Makāmât — Bedîüzzamân el-Hemedânî','C2','Bedîüzzamân el-Hemedânî (ö. 398) · asıl metin',KG),
('hariri','0516IbnCaliHariri.Maqamat','مقامات الحريري','Makāmât — Harîrî','C2','Harîrî (ö. 516) · asıl metin',KG),
]
RLM='‏'
def bol(raw,zeydan):
    body=raw.split('#META#Header#End#')[-1];S=[];cur=None;cp=None
    for line in body.splitlines():
        if not line.strip(): continue
        if line.startswith('### '):
            m=re.match(r'^###\s*(\|+)\s*(.*)',line);lv=len(m.group(1)) if m else 1;t=clean(m.group(2) if m else line[4:]).strip('[] ')
            if not t: continue
            if lv<=2 or cur is None: cur=[t[:90],[]];S.append(cur)
            else: cur[1].append('— '+t+' —')
            cp=None;continue
        if line.startswith('# '):
            raw_t=line[2:];t=clean(raw_t)
            if not t or re.fullmatch(r'PageV\d+P\d+',raw_t.strip()): continue
            if zeydan and raw_t.lstrip().startswith('|'):
                cur=[t.strip(),[]];S.append(cur);cp=None;continue
            if zeydan and raw_t.rstrip().endswith(RLM) and len(t)<60: continue
            if cur is None: cur=['مقدمة',[]];S.append(cur)
            cur[1].append(t);cp=len(cur[1])-1
        elif line.startswith('~~') and cur and cp is not None:
            t=clean(line[2:])
            if t: cur[1][cp]+=' '+t
    S=[[t,p] for t,p in S if p and sum(len(x) for x in p)>200]
    # klasik metinde satır kırılmış kısa paragrafları birleştir
    out=[]
    for t,P in S:
        Q=[]
        for p in P:
            if Q and not zeydan and len(Q[-1])<350 and not Q[-1].startswith('—') and not p.startswith('—') and not re.search(r'[.!؟:»]$',Q[-1]): Q[-1]+=' '+p
            else: Q.append(p)
        # uzun bölümleri parçala
        buf=[];n=1;top=sum(len(x) for x in Q)
        if top<=14000: out.append([t,Q]);continue
        for p in Q:
            buf.append(p)
            if sum(len(x) for x in buf)>9000: out.append([f'{t} ({n})',buf]);buf=[];n+=1
        if buf: out.append([f'{t} ({n})',buf])
    return out
L=json.load(open('data/roman/liste.json',encoding='utf-8'));ids={k[0] for k in KB};L=[x for x in L if x['id'] not in ids]
for id,pre,ar,tr,sv,yz,gr in KB:
    raw=open(f'/tmp/oiti/rom/{pre}.txt',encoding='utf-8').read();B=bol(raw,pre.startswith('1331') or pre.startswith('1342'))
    if not B: print('BOŞ',id);continue
    d=dict(id=id,dil='ar',seviye=sv,baslik=ar,tr_baslik=tr,yazar=yz,not_='',uzun=1,
      bolumler=[dict(b=t,tr_b='',c=[[p,''] for p in P]) for t,P in B],sozluk={})
    d['not']='Asıl Arapça metin (OpenITI külliyatı, CC BY-NC-SA 4.0). Bilmediğin kelimeye dokun: anlamı geniş sözlükten gelir.';del d['not_']
    json.dump(d,open(f'data/roman/{id}.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    L.append(dict(id=id,dil='ar',seviye=sv,baslik=ar,tr_baslik=tr,yazar=yz,bolum=len(B),uzun=1,grup=gr))
    print(id,len(B),sum(len(p) for _,P in B for p in P)//1000,'k')
json.dump(L,open('data/roman/liste.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
