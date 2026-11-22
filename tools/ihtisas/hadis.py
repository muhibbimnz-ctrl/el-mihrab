# İhtisas — Hadis ve Hadis Usûlü
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
HK = ('hadis.html', 'Hadis Dirâsesi kütüphanesinde oku')
ALAN = dict(
 id='hadis', ad='Hadis ve Hadis Usûlü', ar='عِلْمُ الْحَدِيث', renk='#8a6a2c',
 kisa='Peygamberimizin söz, fiil ve onaylarını; rivayet ve dirâyet yönüyle inceleme ilmi.',
 giris=[
  'Hadis ilmi iki kanattan oluşur: Rivâyetü’l-hadîs, hadislerin metinlerini senetleriyle nakleder; dirâyetü’l-hadîs (hadis usûlü) ise bu rivayetlerin sahih olup olmadığını, râvîlerin durumunu ve metnin anlaşılma kurallarını inceler.',
  'Hadis öğrencisi önce kısa derlemelerle hadis dilini ve ahlâkını tanır, sonra usûlün temel terimlerini öğrenir, ardından Kütüb-i Sitte ve şerhleriyle derinleşir. Ricâl (râvîler) ve ilel (gizli kusurlar) ilmi ise mütehassısın alanıdır.',
  'Bu yoldaki kitapların büyük kısmı el-Mihrâb’ın Hadis Dirâsesi kütüphanesinde Arapça ve Türkçe olarak okunabilir.'],
 basamaklar=[
  dict(ad='Hadisle tanışma', alt='Başlangıç', ac='Kısa ve seçme hadis derlemeleri: hadis dilini, ahlâk ve ibadet hadislerini tanımak.',
   kitaplar=[
    K('el-Erbaûn (Kırk Hadis)', 'الأربعون النووية', 'İmam Nevevî', '676/1277', 'derleme', 'Dinin temel kurallarını özetleyen 42 hadis; ezberlenir.', ['İbn Recep, Câmiu’l-ulûm ve’l-hikem', 'İbn Dakîkul‘îd, Şerhu’l-Erbaîn'], ('hadis.html#k=erbain', 'Hadis Dirâsesi’nde Kırk Hadis')),
    K('Riyâzü’s-sâlihîn', 'رياض الصالحين', 'İmam Nevevî', '676/1277', 'derleme', 'Ahlâk ve âdâb hadislerini konulara göre toplar; her bâbın başında âyetler.', ['İbn Allân, Delîlü’l-fâlihîn'], HK),
    K('Bulûğu’l-merâm', 'بلوغ المرام من أدلة الأحكام', 'İbn Hacer el-Askalânî', '852/1449', 'ahkâm derlemesi', 'Fıkıh bâblarına göre ahkâm hadisleri; her hadisin kaynağı ve derecesi verilir.', ['San‘ânî, Sübülü’s-selâm'], HK)]),
  dict(ad='Usûle giriş', alt='Başlangıç', ac='Sahih, hasen, zayıf; muttasıl, mürsel; cerh ve ta‘dîl gibi temel kavramlar.',
   kitaplar=[
    K('el-Manzûmetü’l-Beykûniyye', 'المنظومة البيقونية', 'Ömer el-Beykûnî', '1080/1669 civarı', 'manzum metin', '34 beyitte hadis usûlünün temel terimleri; ezberlenir.'),
    K('Nuhbetü’l-fiker ve Nüzhetü’n-nazar', 'نخبة الفكر ونزهة النظر', 'İbn Hacer el-Askalânî', '852/1449', 'metin ve şerh', 'Usûlün en çok okunan özlü metni ve müellifin kendi şerhi.', app=('hadis.html', 'Usûl kütüphanesinde Nuhbe ve Nüzhe')),
    K('Hadis Usûlü (Türkçe)', '—', 'Talat Koçyiğit', '—', 'Türkçe ders kitabı', 'Türkçe usûl terminolojisini oturtan klasik ders kitabı.')]),
  dict(ad='Temel kaynaklar: Kütüb-i Sitte ve Muvatta', alt='Orta', ac='Hadisin asıl kaynakları. Önce Buhârî ve Müslim, sonra Sünenler.',
   kitaplar=[
    K('el-Muvatta’', 'الموطأ', 'İmam Mâlik', '179/795', 'musannef', 'Medine amelini yansıtan, fıkıh bâblarına göre ilk büyük derleme.', app=HK),
    K('el-Câmiu’s-sahîh (Sahîh-i Buhârî)', 'صحيح البخاري', 'İmam Buhârî', '256/870', 'câmi‘', 'Kur’an’dan sonra en sahih kitap kabul edilir; bâb başlıkları ayrı bir fıkıh hazinesidir.', ['İbn Hacer, Fethu’l-bârî', 'Aynî, Umdetü’l-kârî', 'Kastallânî, İrşâdü’s-sârî'], HK),
    K('Sahîh-i Müslim', 'صحيح مسلم', 'İmam Müslim', '261/875', 'câmi‘', 'Rivayetleri tek yerde toplayan düzeniyle hadis karşılaştırmasına çok uygun.', ['Nevevî, el-Minhâc'], HK),
    K('Sünen-i Ebû Dâvûd', 'سنن أبي داود', 'Ebû Dâvûd es-Sicistânî', '275/889', 'sünen', 'Ahkâm hadislerinin temel kaynağı.', ['Hattâbî, Meâlimü’s-sünen'], HK),
    K('Câmiu’t-Tirmizî', 'جامع الترمذي', 'İmam Tirmizî', '279/892', 'câmi‘', 'Her hadisin derecesini ve fakihlerin görüşlerini bildirir; usûl öğrencisi için ders kitabı gibidir.', app=HK),
    K('Sünen-i Nesâî', 'سنن النسائي', 'İmam Nesâî', '303/915', 'sünen', 'Râvî tenkidinde titizliğiyle bilinir.', app=HK),
    K('Sünen-i İbn Mâce', 'سنن ابن ماجه', 'İbn Mâce', '273/887', 'sünen', 'Kütüb-i Sitte’nin altıncısı; zevâid hadisleri için önemli.', app=HK)]),
  dict(ad='Şerhler', alt='İleri', ac='Hadisin anlaşılması: dil, fıkıh, usûl ve tarih bilgisiyle açıklama.',
   kitaplar=[
    K('Fethu’l-bârî', 'فتح الباري بشرح صحيح البخاري', 'İbn Hacer el-Askalânî', '852/1449', 'şerh', 'Buhârî’nin en büyük şerhi; hadis ilminin ansiklopedisi.', app=('hadis.html', 'Usûl kütüphanesinde mukaddimesi: Hedyü’s-sârî')),
    K('Umdetü’l-kârî', 'عمدة القاري', 'Bedreddîn el-Aynî', '855/1451', 'şerh', 'Hanefî bakışla Buhârî şerhi; dil ve i‘rab tahlilleri zengin.'),
    K('el-Minhâc', 'المنهاج شرح صحيح مسلم', 'İmam Nevevî', '676/1277', 'şerh', 'Müslim’in en çok okunan şerhi; fıkhî hükümleri ve dil meselelerini dengeli işler.')]),
  dict(ad='İleri usûl, ricâl ve ilel', alt='Mütehassıs', ac='Bir hadisin sıhhatine kendin karar verebilmek için gereken ilimler.',
   kitaplar=[
    K('Ulûmü’l-hadîs (Mukaddime)', 'معرفة أنواع علوم الحديث', 'İbnü’s-Salâh', '643/1245', 'usûl', 'Usûlü 65 nev‘ hâlinde sistemleştiren ve sonraki bütün kitapların dayandığı eser.', ['Irâkî, Elfiyye ve şerhi', 'Sehâvî, Fethu’l-muğîs', 'Süyûtî, Tedrîbü’r-râvî'], ('hadis.html', 'Usûl kütüphanesinde oku')),
    K('Tedrîbü’r-râvî', 'تدريب الراوي', 'Celâleddîn es-Süyûtî', '911/1505', 'şerh', 'Nevevî’nin Takrîb’ine geniş şerh; usûlün başvuru kitabı.', app=('hadis.html', 'Usûl kütüphanesinde oku')),
    K('Takrîbü’t-tehzîb', 'تقريب التهذيب', 'İbn Hacer el-Askalânî', '852/1449', 'ricâl', 'Kütüb-i Sitte râvîlerinin her birine tek kelimelik hüküm veren el kitabı.', app=('hadis.html', 'Senette râvîye dokunarak')),
    K('Tehzîbü’l-kemâl', 'تهذيب الكمال في أسماء الرجال', 'Cemâleddîn el-Mizzî', '742/1341', 'ricâl', 'Râvî biyografilerinin büyük kaynağı.'),
    K('Mîzânü’l-i‘tidâl', 'ميزان الاعتدال', 'Şemseddîn ez-Zehebî', '748/1348', 'ricâl', 'Hakkında tenkit bulunan râvîlerin listesi ve değerlendirmesi.')]),
 ],
 sahsiyetler=[
  dict(ad='Ebû Hüreyre', ar='أبو هريرة', v='58/678', k='En çok hadis rivayet eden sahâbî.'),
  dict(ad='Hz. Âişe', ar='عائشة أم المؤمنين', v='58/678', k='Hadis ve fıkıhta sahâbenin önde gelen âlimi.'),
  dict(ad='İbn Şihâb ez-Zührî', ar='ابن شهاب الزهري', v='124/742', k='Hadislerin resmî tedvininin öncüsü.'),
  dict(ad='İmam Mâlik', ar='مالك بن أنس', v='179/795', k='el-Muvatta’.'),
  dict(ad='Ahmed b. Hanbel', ar='أحمد بن حنبل', v='241/855', k='el-Müsned.'),
  dict(ad='İmam Buhârî', ar='البخاري', v='256/870', k='Sahîh’in müellifi.'),
  dict(ad='İmam Müslim', ar='مسلم بن الحجاج', v='261/875', k='Sahîh’in müellifi.'),
  dict(ad='İbnü’s-Salâh', ar='ابن الصلاح', v='643/1245', k='Usûlün sistemleştiricisi.'),
  dict(ad='İmam Nevevî', ar='النووي', v='676/1277', k='Kırk Hadis, Riyâzü’s-sâlihîn, el-Minhâc.'),
  dict(ad='Zehebî', ar='الذهبي', v='748/1348', k='Ricâl ve tarih.'),
  dict(ad='İbn Hacer el-Askalânî', ar='ابن حجر العسقلاني', v='852/1449', k='Fethu’l-bârî, Nuhbe, Takrîb.')],
 terimler=[
  dict(ar='الإسناد', tr='İsnad / sened', d='Hadisi nakleden râvîler zinciri.'),
  dict(ar='المتن', tr='Metin', d='Senedin sonunda gelen asıl söz.'),
  dict(ar='الصحيح', tr='Sahih', d='Adil ve zabıt râvîlerin muttasıl senetle, şâz ve illetsiz naklettiği hadis.'),
  dict(ar='الحسن', tr='Hasen', d='Sahihin şartlarını taşıyıp râvîlerinden birinin zabtı biraz hafif olan hadis.'),
  dict(ar='الضعيف', tr='Zayıf', d='Sahih ve hasenin şartlarından birini taşımayan hadis.'),
  dict(ar='المرسل', tr='Mürsel', d='Tâbiînin sahâbîyi atlayarak doğrudan Peygamberimizden naklettiği hadis.'),
  dict(ar='المتواتر', tr='Mütevâtir', d='Yalan üzerinde birleşmeleri imkânsız kalabalıkların naklettiği haber.'),
  dict(ar='الآحاد', tr='Âhâd', d='Tevâtür derecesine ulaşmayan haber.'),
  dict(ar='الجرح والتعديل', tr='Cerh ve ta‘dîl', d='Râvîlerin güvenilirliğini değerlendirme ilmi.'),
  dict(ar='العلة', tr='İllet', d='Hadisin sıhhatini zedeleyen gizli kusur.'),
  dict(ar='الشاذ', tr='Şâz', d='Güvenilir râvînin daha güvenilir olana aykırı rivayeti.'),
  dict(ar='الموضوع', tr='Mevzû', d='Uydurma hadis.')],
 nasil=[
  'Kırk Hadis’i ezberle; her hadisin bir şerhini oku. Hadis dili kulağına yerleşsin.',
  'Beykûniyye ve Nuhbe ile terimleri öğrenmeden Kütüb-i Sitte’de derecelendirme yapmaya çalışma.',
  'Buhârî’yi bâb başlıklarına dikkat ederek oku; İmam Buhârî’nin fıkhı başlıklardadır.',
  'Bir hadisin bütün rivayetlerini (Buhârî, Müslim, Sünenler) yan yana koy; lafız farklarını ve ek bilgileri not et.',
  'Zayıf hadisle amel konusunda âlimlerin şartlarını öğren; hüküm vermeyi mütehassısa bırak.'],
)
