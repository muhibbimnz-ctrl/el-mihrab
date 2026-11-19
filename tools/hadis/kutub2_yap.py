# hadith-json (AhmedBaset) kaynaklı ek kitaplar -> data/hadis/kutub.json'a eklenir. Girdi: /tmp/hj sparse checkout.
import json,glob,os
ROOT='/tmp/hj/db/by_chapter/'
TR={
'ahmed':{'1':'Müsnedü Ebî Bekr es-Sıddîk','2':'Müsnedü Ömer b. el-Hattâb','3':'Sakîfe hadisi','4':'Müsnedü Osmân b. Affân','5':'Müsnedü Alî b. Ebî Tâlib','6':'Müsnedü Talha b. Ubeydillâh','7':'Müsnedü’z-Zübeyr b. el-Avvâm','31':'Ebû Rimse hadisi'},
'darimi':{'introduction':'Mukaddime','1':'Tahâret','2':'Salât','3':'Zekât','4':'Savm','5':'Menâsik','6':'Edâhî','7':'Sayd','8':'Et‘ime','9':'Eşribe','10':'Rüya','11':'Nikâh','12':'Talâk','13':'Hudûd','14':'Nüzûr ve eymân','15':'Diyât','16':'Cihâd','17':'Siyer','18':'Büyû‘','19':'İsti’zân','20':'Rikâk','21':'Ferâiz','22':'Vesâyâ','23':'Fezâilü’l-Kur’ân'},
'riyad_assalihin':{'introduction':'Mukaddimât (Çeşitli bablar)','1':'Edeb','2':'Yemek âdâbı','3':'Libâs','4':'Uyku, yatma ve oturma âdâbı','5':'Selâm','6':'Hasta ziyareti ve cenaze','7':'Yolculuk âdâbı','8':'Fezâil','9':'İ‘tikâf','10':'Hac','11':'Cihâd','12':'İlim','13':'Hamd ve şükür','14':'Salavât','15':'Zikir','16':'Dua','17':'Yasaklanan şeyler','18':'Çeşitli kıymetli hadisler','19':'İstiğfâr'},
'bulugh_almaram':{'1':'Tahâret','2':'Salât','3':'Cenâiz','4':'Zekât','5':'Sıyâm','6':'Hac','7':'Büyû‘','8':'Nikâh','9':'Cinâyât (Kısas)','10':'Hudûd','11':'Cihâd','12':'Et‘ime','13':'Eymân ve nüzûr','14':'Kazâ (Yargı)','15':'Itk','16':'Câmi‘ (Edeb, zühd, zikir)'},
'aladab_almufrad':{'1':'Anne baba','2':'Sıla-i rahim','3':'Mevlâlar','4':'Kız çocuklarına bakmak','5':'Çocuklara bakmak','6':'Komşular','7':'Cömertlik ve yetimler','8':'Çocuk ölümü','9':'Efendilik (hizmetçilere davranış)','10':'Gözetim','11':'Güzel davranış','12':'İnsanlara güler yüz','13':'İstişare','14':'Güzel ahlak','15':'Lanetleme','16':'Övgü','17':'Ziyaret','18':'Yaşlılar','19':'Çocuklar','20':'Merhamet','21':'Toplumsal davranış','22':'Küsmek','23':'Nasihat','24':'Ayıplamak','25':'Binada israf','26':'Şefkat','27':'Dünya işleri','28':'Zulüm','29':'Hasta ziyareti','30':'Genel davranışlar','31':'Dua','32':'Misafir ve infak','33':'Sözler','34':'İsimler','35':'Künyeler','36':'Şiir','37':'Kelimeler','38':'Sonuçlar','39':'Uğursuzluk','40':'Aksırma ve esneme','41':'İşaretler','42':'Selâm','43':'İzin isteme','44':'Ehl-i kitap','45':'Mektuplar','46':'Meclisler','47':'İnsanlarla münasebet','48':'Oturma ve uzanma','49':'Sabah ve akşam','50':'Uyku ve gece','51':'Hayvanlar','52':'Kaylûle (öğle uykusu)','53':'Sünnet olmak','54':'Bahis ve oyunlar','55':'Tanışmak','56':'Haddini aşmak ve sertlik','57':'Öfke'},
'shamail_muhammadiyah':{'1':'Hz. Peygamber’in mübarek görünüşü','2':'Mühr-i nübüvvet','3':'Mübarek saçları','4':'Saçlarını taraması','5':'Ak saçları','6':'Boya kullanması','7':'Sürmesi','8':'Giyimi','8b':'Geçimi','9':'Mestleri','10':'Ayakkabıları','11':'Mübarek yüzüğü','12':'Yüzüğü sağ elde takması','13':'Kılıcı','14':'Zırhı','15':'Miğferi','16':'Sarığı','17':'İzârı','18':'Yürüyüşü','19':'Başörtüsü (kınâ‘)','20':'Oturuşu','21':'Yastığı','22':'Yastıktan başka şeye dayanması','23':'Yemek yeyişi','24':'Ekmeği','25':'Katıkları','26':'Yemekte abdesti','27':'Yemekten önce ve sonra duası','28':'Kabı','29':'Yediği meyveler','30':'İçtikleri','31':'İçişi','32':'Güzel koku kullanması','33':'Konuşması','34':'Gülmesi','35':'Şakalaşması','36':'Şiir hakkındaki sözleri','37':'Gece sohbeti','38':'Ümmü Zer‘ hadisi','39':'Uykusu','40':'İbadeti','41':'Kuşluk namazı','42':'Evde nafile kılması','43':'Orucu','44':'Kur’an okuyuşu','45':'Ağlaması','46':'Yatağı','47':'Tevâzuu','48':'Ahlak ve âdetleri','49':'Hayâsı','50':'Hacâmat','51':'İsimleri','52':'Yaşayışı','53':'Mübarek yaşı','54':'Vefatı','55':'Mirası','56':'Rüyada görülmesi'},
'mishkat_almasabih':{'1':'Îmân','2':'İlim','3':'Tahâret','4':'Salât','5':'Cenâiz','6':'Zekât','7':'Savm','8':'Fezâilü’l-Kur’ân','9':'De‘avât','10':'Menâsik','11':'Büyû‘','12':'Ferâiz ve vesâyâ','13':'Nikâh','14':'Itk','15':'Eymân ve nüzûr','16':'Kısas','17':'Hudûd','18':'İmâre ve kazâ','19':'Cihâd','20':'Sayd ve zebâih','21':'Et‘ime','22':'Libâs','23':'Tıb ve rukye','24':'Rüya'},
}
KB=[('ahmed','the_9_books','Müsned-i Ahmed (ilk müsnedler)','مسند أحمد','Ahmed b. Hanbel (v. 241)','Kütüb-i tis‘a'),
('darimi','the_9_books','Sünen-i Dârimî','سنن الدارمي','Abdullah ed-Dârimî (v. 255)','Kütüb-i tis‘a'),
('riyad_assalihin','other_books','Riyâzü’s-Sâlihîn','رياض الصالحين','İmam Nevevî (v. 676)','Derlemeler'),
('bulugh_almaram','other_books','Bulûğu’l-Merâm','بلوغ المرام','İbn Hacer el-Askalânî (v. 852)','Derlemeler'),
('mishkat_almasabih','other_books','Mişkâtü’l-Mesâbîh','مشكاة المصابيح','Hatîb et-Tebrîzî (v. 741)','Derlemeler'),
('aladab_almufrad','other_books','el-Edebü’l-Müfred','الأدب المفرد','İmam Buhârî (v. 256)','Ahlak ve şemâil'),
('shamail_muhammadiyah','other_books','Şemâil-i Muhammediyye','الشمائل المحمدية','İmam Tirmizî (v. 279)','Ahlak ve şemâil')]
def sira(x):
    return (-1,0) if x=='introduction' else (int(''.join(c for c in x if c.isdigit())), x)
K=json.load(open('data/hadis/kutub.json',encoding='utf-8'))
K=[b for b in K if b.get('src')!='hj']
for k,g,ad,ar,mu,gr in KB:
    secs=[];tot=0
    for f in sorted(glob.glob(ROOT+g+'/'+k+'/*.json'),key=lambda f:sira(os.path.basename(f)[:-5])):
        sid=os.path.basename(f)[:-5];d=json.load(open(f));n=len(d['hadiths'])
        if n==0 or sid not in TR[k]: 
            if n: print('adsız',k,sid)
            continue
        tot+=n;secs.append([sid,TR[k][sid],n])
    K.append(dict(k=k,src='hj',g=g,ad=ad,ar=ar,muellif=mu,grup=gr,tr=False,adet=tot,b=secs));print(k,len(secs),tot)
json.dump(K,open('data/hadis/kutub.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
