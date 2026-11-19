# data/hadis/kutub.json: hadith-api (fawazahmed0) kitap listesi + Türkçe bölüm adları
# Kaynak: /tmp/ha/info.json (git sparse checkout ile alınır)
import json,sys,os,importlib.util
D=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location('k',os.path.join(D,'kutub_adlari.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
info=json.load(open(sys.argv[1] if len(sys.argv)>1 else '/tmp/ha/info.json'))
ED=json.load(open(os.path.join(os.path.dirname(sys.argv[1]) if len(sys.argv)>1 else '/tmp/ha','editions.json')))
KB=[('bukhari','Sahîh-i Buhârî','صحيح البخاري','İmam Buhârî (v. 256)','Kütüb-i sitte'),
('muslim','Sahîh-i Müslim','صحيح مسلم','İmam Müslim (v. 261)','Kütüb-i sitte'),
('abudawud','Sünen-i Ebû Dâvûd','سنن أبي داود','Ebû Dâvûd es-Sicistânî (v. 275)','Kütüb-i sitte'),
('tirmidhi','Câmiu’t-Tirmizî','جامع الترمذي','İmam Tirmizî (v. 279)','Kütüb-i sitte'),
('nasai','Sünen-i Nesâî','سنن النسائي','İmam Nesâî (v. 303)','Kütüb-i sitte'),
('ibnmajah','Sünen-i İbn Mâce','سنن ابن ماجه','İbn Mâce (v. 273)','Kütüb-i sitte'),
('malik','el-Muvatta’','الموطأ','İmam Mâlik (v. 179)','Diğer'),
('qudsi','Kırk Hadîs-i Kudsî','الأربعون القدسية','Derleme','Kırk hadis'),
('dehlawi','Dihlevî’nin Kırk Hadisi','الأربعون للدهلوي','Şah Veliyyullah Dihlevî (v. 1176)','Kırk hadis')]
out=[]
for k,ad,ar,mu,gr in KB:
    md=info[k]['metadata'];sd=md['section_details'];names=m.K[k]
    secs=[]
    for s,v in md['sections'].items():
        s=int(s)
        if s not in names: continue
        d=sd[str(s)];f,l=d['hadithnumber_first'],d['hadithnumber_last']
        if not f: continue
        secs.append([s,names[s],int(f),int(l)])
    langs=[c['language'] for c in ED[k]['collection']]
    out.append(dict(k=k,ad=ad,ar=ar,muellif=mu,grup=gr,tr='Turkish' in langs,adet=len(info[k]['hadiths']),b=secs))
    print(k,len(secs),'tr' if 'Turkish' in langs else '-')
json.dump(out,open('data/hadis/kutub.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
