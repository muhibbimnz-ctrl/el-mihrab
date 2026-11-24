# Lisânü'l-Arab (OpenITI, 0725AH/data/0711IbnManzurIfriqi/...Shamela0001687-ara1.mARkdown) -> kök maddeleri, şâhid beyitler ve şâirleri: /tmp/lisan_beyit.json
# Çıktı: [[kök, [[beyit, şâir_tr], ...]], ...]  (şâir bilinmiyorsa "")
import re,json,sys
H=re.compile('[ً-ٰٟـ]')
src=sys.argv[1] if len(sys.argv)>1 else '/tmp/oiti/lisan.txt'
# Beytin hemen önündeki "قال/أنشد ل..." ifadesinden şâir adı (Türkçe yazımıyla)
SAIR={'امرؤ القيس':'İmruülkays','الأعشى':'A‘şâ','أعشى باهلة':'A‘şâ Bâhile','ذو الرمة':'Zürrumme','رؤبة':'Ru’be','رؤبة بن العجاج':'Ru’be','الكميت':'Kümeyt','جرير':'Cerîr',
 'أبو ذؤيب':'Ebû Züeyb el-Hüzelî','أبو ذؤيب الهذلي':'Ebû Züeyb el-Hüzelî','الراعي':'Râî en-Nümeyrî','العجاج':'Accâc','الفرزدق':'Ferezdak','النابغة':'Nâbiga','النابغة الذبياني':'Nâbiga ez-Zübyânî',
 'الأخطل':'Ahtal','ابن مقبل':'İbn Mukbil','تميم بن مقبل':'İbn Mukbil','الطرماح':'Tırimmâh','زهير':'Züheyr b. Ebû Sülmâ','زهير بن أبو سلمى':'Züheyr b. Ebû Sülmâ','ابن أحمر':'İbn Ahmer','عمرو بن أحمر':'İbn Ahmer','ابن أحمر الباهلي':'İbn Ahmer',
 'طرفة':'Tarafe','طرفة بن العبد':'Tarafe','الشماخ':'Şemmâh','ساعدة بن جؤية':'Sâide b. Cüeyye','ساعدة بن جؤية الهذلي':'Sâide b. Cüeyye','ساعدة':'Sâide b. Cüeyye','ساعدة الهذلي':'Sâide b. Cüeyye',
 'كثير':'Küseyyir','كثير عزة':'Küseyyir','القطامي':'Kutâmî','عنترة':'Antere','الجعدي':'Nâbiga el-Ca‘dî','النابغة الجعدي':'Nâbiga el-Ca‘dî','أوس بن حجر':'Evs b. Hacer','أوس':'Evs b. Hacer',
 'أبو النجم':'Ebü’n-Necm el-İclî','عدي بن زيد':'Adî b. Zeyd','عدي بن زيد العبادي':'Adî b. Zeyd','الحطيئة':'Hutay’a','حميد بن ثور':'Humeyd b. Sevr','حميد بن ثور الهلالي':'Humeyd b. Sevr',
 'بشر بن أبو خازم':'Bişr b. Ebû Hâzim','حسان':'Hassân b. Sâbit','حسان بن ثابت':'Hassân b. Sâbit','أبو دواد':'Ebû Duâd el-İyâdî','أبو دواد الإيادي':'Ebû Duâd el-İyâdî','صخر الغي':'Sahru’l-Gayy',
 'المتنخل الهذلي':'Mütenahhil el-Hüzelî','المتنخل':'Mütenahhil el-Hüzelî','طفيل':'Tufeyl el-Ganevî','طفيل الغنوي':'Tufeyl el-Ganevî','تأبط شرا':'Teebbata Şerran','كعب بن زهير':'Ka‘b b. Züheyr',
 'المرار':'Merrâr el-Fak‘asî','المرار الفقعسي':'Merrâr el-Fak‘asî','ابن هرمة':'İbn Herme','أبو زبيد':'Ebû Zübeyd et-Tâî','أبو زبيد الطائي':'Ebû Zübeyd et-Tâî','أبو خراش':'Ebû Hırâş el-Hüzelî','أبو خراش الهذلي':'Ebû Hırâş el-Hüzelî',
 'أبو وجزة':'Ebû Vecze es-Sa‘dî','أبو وجزة السعدي':'Ebû Vecze es-Sa‘dî','النمر بن تولب':'Nemir b. Tevleb','الأسود بن يعفر':'Esved b. Ya‘fur','أبو كبير':'Ebû Kebîr el-Hüzelî','أبو كبير الهذلي':'Ebû Kebîr el-Hüzelî',
 'البعيث':'Beîs','عبيد بن الأبرص':'Abîd b. el-Ebras','أمية بن أبو الصلت':'Ümeyye b. Ebi’s-Salt','جميل':'Cemîl-i Buseyne','قيس بن الخطيم':'Kays b. el-Hatîm','ابن ميادة':'İbn Meyyâde','ابن الرقاع':'Adî b. er-Rikâ‘','عدي بن الرقاع':'Adî b. er-Rikâ‘',
 'مهلهل':'Mühelhil','الحرث بن حلزة':'Hâris b. Hillize','ابن حلزة':'Hâris b. Hillize','نصيب':'Nusayb','علقمة':'Alkame el-Fahl','علقمة بن عبدة':'Alkame el-Fahl','المثقب العبدي':'Müsakkıb el-Abdî',
 'عمرو بن كلثوم':'Amr b. Külsûm','عمرو بن معديكرب':'Amr b. Ma‘dîkerib','الأفوه':'Efveh el-Evdî','الأفوه الأودي':'Efveh el-Evdî','المخبل':'Muhabbel es-Sa‘dî','المخبل السعدي':'Muhabbel es-Sa‘dî','قيس بن ذريح':'Kays b. Zerîh',
 'الأحوص':'Ahvas','عمر بن أبو ربيعة':'Ömer b. Ebû Rebîa','سلامة بن جندل':'Selâme b. Cendel','المتلمس':'Mütelemmis','دريد بن الصمة':'Düreyd b. es-Simme','الشنفرى':'Şenfera','عروة بن الورد':'Urve b. el-Verd',
 'معن بن أوس':'Ma‘n b. Evs','حاتم':'Hâtim et-Tâî','جران العود':'Cirânü’l-Avd','عامر بن الطفيل':'Âmir b. et-Tufeyl','لبيد':'Lebîd','عباس بن مرداس':'Abbâs b. Mirdâs','العباس بن مرداس':'Abbâs b. Mirdâs',
 'متمم بن نويرة':'Mütemmim b. Nüveyre','متمم':'Mütemmim b. Nüveyre','الأغلب العجلي':'Ağleb el-İclî','الأغلب':'Ağleb el-İclî','عمران بن حطان':'İmrân b. Hıttân','ابن قيس الرقيات':'İbn Kays er-Rukayyât','ابن الرقيات':'İbn Kays er-Rukayyât',
 'ذو الإصبع العدواني':'Zü’l-İsba‘ el-Advânî','أبو قيس بن الأسلت':'Ebû Kays b. el-Eslet','الخنساء':'Hansâ','مالك بن نويرة':'Mâlik b. Nüveyre','كعب بن مالك':'Ka‘b b. Mâlik','كعب بن مالك الأنصاري':'Ka‘b b. Mâlik',
 'عبيد':'Abîd b. el-Ebras','الشماخ بن ضرار':'Şemmâh','مزرد':'Müzerrid','هدبة بن خشرم':'Hüdbe b. Haşrem','أبو حية النميري':'Ebû Hayye en-Nümeyrî','مزاحم العقيلي':'Müzâhim el-Ukaylî','مزاحم':'Müzâhim el-Ukaylî',
 'أبو صخر الهذلي':'Ebû Sahr el-Hüzelî','أمية بن أبو عائذ الهذلي':'Ümeyye b. Ebû Âiz el-Hüzelî','أمية بن أبو عائذ':'Ümeyye b. Ebû Âiz el-Hüzelî','عبدة بن الطبيب':'Abde b. et-Tabîb','خفاف بن ندبة':'Hufâf b. Nüdbe',
 'المسيب بن علس':'Müseyyeb b. Alas','عمرو بن قميئة':'Amr b. Kamîe','السليك بن السلكة':'Süleyk b. es-Sülake','زيد الخيل':'Zeydü’l-Hayl','الممزق العبدي':'Mümezzak el-Abdî','حميد الأرقط':'Humeyd el-Erkat',
 'أبو محمد الفقعسي':'Ebû Muhammed el-Fak‘asî','عروة':'Urve b. el-Verd','سويد بن أبو كاهل':'Süveyd b. Ebû Kâhil','الحسين بن مطير':'Hüseyn b. Mutayr','أبو نخيلة':'Ebû Nuhayle','دكين':'Dükeyn er-Râcîz','هميان بن قحافة':'Hemyân b. Kuhâfe',
 'جندل بن المثنى':'Cendel b. el-Müsennâ','القتال الكلابي':'Kattâl el-Kilâbî','العجير السلولي':'Uceyr es-Selûlî','الزفيان':'Zefeyân','مسكين الدارمي':'Miskîn ed-Dârimî','زياد الأعجم':'Ziyâd el-A‘cem','أحيحة':'Uhayha b. el-Culâh',
 'قعنب بن أم صاحب':'Ka‘neb b. Ümmü Sâhib','عمرو بن شأس':'Amr b. Şe’s','دريد':'Düreyd b. es-Simme','الأعشى ميمون':'A‘şâ'}
def sair(t):
    t=H.sub('',t).strip()
    m=re.search(r'(?:قال|وقال|أنشد|وأنشد|كقول|لقول|وقول|قول)\s+((?:ابن بري|ابن الأعرابي|ثعلب|الجوهري)\s+)?(ل)?([^:؛،.]{2,40}?)\s*(?:يصف[^:]*)?[:؛]?\s*$',t)
    if not m: return ''
    a=m.group(3).strip()
    if m.group(2) and 'ل'+a in SAIR: a='ل'+a  # "لبيد" -> ل + بيد
    a=re.sub(r'^إمرؤ|^امرئ|^إمرئ','امرؤ',a);a=re.sub(r'\bأبي\b','أبو',a);a=re.sub(r'^ذي\b','ذو',a)
    if a not in SAIR and a.startswith('ل') and a[1:] in SAIR: a=a[1:]
    return SAIR.get(a,'')
R=[];cur=None;prev='';son=''
for line in open(src,encoding='utf-8'):
    line=line.rstrip('\n')
    m=re.match(r'^### \$\s*([^:،\s]+)\s*:',line)
    if m:
        cur=[m.group(1).strip(),[]];R.append(cur);prev='';son='';continue
    if line.startswith('### '): cur=None;continue
    if cur is None: continue
    if not (line.startswith('# ') and ' ... ' in line):
        prev=line[2:] if line[:2] in('# ','~~') else line
        continue
    v=re.sub(r'«\d+»|PageV\d+P\d+|ms\d+','',line[2:]).strip()
    a,_,b=v.partition(' ... ')
    a=a.strip(' ،,;؛');b=b.strip(' ،,;؛.')
    s=sair(re.sub(r'«\d+»|PageV\d+P\d+|ms\d+','',prev)) if prev else son;son=s;prev=''
    if len(a)<12 or len(b)<12 or len(a)>70 or len(b)>70 or ' ... ' in b or re.search(r'[A-Za-z0-9]',v): continue
    cur[1].append([a+' ... '+b,s])
R=[r for r in R if r[1]]
json.dump(R,open('/tmp/lisan_beyit.json','w'),ensure_ascii=False)
print(len(R),'kök',sum(len(r[1]) for r in R),'beyit',sum(1 for r in R for x in r[1] if x[1]),'şâirli')
