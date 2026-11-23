# Farsça Hikâye Programı 1–2. haftaları uzatır: her güne yeni okuma cümleleri ve diyalog satırları ekler.
# python3 tools/dil/fa/uzat12.py   (tekrar çalıştırılırsa aynı cümleleri ikinci kez eklemez)
import json, os, re, subprocess
R = lambda fa, tr: [fa, tr]
E = {}
E[0] = ([
 R('خانهٔ خانم شیرازی در محله‌ای قدیمی نزدیک بازار بود و کوچه‌هایش آن‌قدر باریک بود که تاکسی نمی‌توانست وارد شود.', 'Şirazi Hanım’ın evi çarşıya yakın eski bir mahalledeydi; sokakları öyle dardı ki taksi içeri giremiyordu.'),
 R('کرم چمدان سنگینش را روی سنگفرش کوچه می‌کشید و صدای چرخ‌هایش در سکوت ظهر می‌پیچید.', 'Kerem ağır bavulunu sokağın kaldırım taşları üzerinde sürüklüyordu; tekerleklerinin sesi öğle sessizliğinde yankılanıyordu.'),
 R('پیرمردی که جلوی مغازه‌اش نشسته بود، از جا برخاست و بی‌آنکه چیزی بپرسد، دستهٔ چمدان را گرفت.', 'Dükkânının önünde oturan yaşlı bir adam yerinden kalktı ve hiçbir şey sormadan bavulun sapını tuttu.'),
 R('گفت: «مهمان خانم شیرازی هستید؟ دیروز گفت که دانشجویی از ترکیه می‌آید.»', 'Dedi ki: “Şirazi Hanım’ın misafiri misiniz? Dün Türkiye’den bir öğrencinin geleceğini söyledi.”'),
 R('کرم تعجب کرد که خبر آمدنش پیش از خودش به محله رسیده است.', 'Kerem, geleceği haberinin kendisinden önce mahalleye ulaşmış olmasına şaştı.'),
 R('در چوبی خانه نقش‌های کهنه‌ای داشت و دو کوبه، یکی سنگین و یکی سبک، بر آن آویزان بود.', 'Evin ahşap kapısında eski oymalar vardı ve üzerinde biri ağır, biri hafif iki tokmak asılıydı.'),
 R('پیرمرد توضیح داد که در قدیم مردها کوبهٔ سنگین را می‌زدند و زن‌ها کوبهٔ سبک را، تا اهل خانه بدانند چه کسی باید در را باز کند.', 'Yaşlı adam, eskiden erkeklerin ağır, kadınların hafif tokmağı çaldığını, böylece ev halkının kapıyı kimin açması gerektiğini bileceğini anlattı.'),
 R('کرم با احتیاط کوبهٔ سنگین را زد و چند لحظه بعد صدای پایی از حیاط شنیده شد.', 'Kerem dikkatle ağır tokmağı çaldı; birkaç saniye sonra avludan ayak sesleri duyuldu.'),
 R('زنی میان‌سال با چادری گل‌دار در را گشود و با لبخندی گرم گفت: «خوش آمدی پسرم، خسته نباشی!»', 'Çiçekli çarşaflı orta yaşlı bir kadın kapıyı açtı ve sıcak bir gülümsemeyle dedi: “Hoş geldin oğlum, yorulmamışsındır inşallah!”'),
 R('کرم پاسخ داد: «سلامت باشید»؛ جمله‌ای که در کلاس زبان یاد گرفته بود و حالا نخستین بار به کار می‌برد.', 'Kerem “Sağ olun” diye cevap verdi; bu, dil kursunda öğrendiği ve şimdi ilk kez kullandığı bir cümleydi.'),
 R('آن شب، پیش از خواب، در دفترش نوشت: «امروز فهمیدم که فارسی را نه از کتاب، بلکه از مردم باید آموخت.»', 'O gece uyumadan önce defterine yazdı: “Bugün anladım ki Farsçayı kitaptan değil, insanlardan öğrenmek gerekir.”')],
 [['پیرمرد', 'خوش آمدید! بگذارید کمکتان کنم؛ این چمدان خیلی سنگین است.', 'Hoş geldiniz! Bırakın size yardım edeyim; bu bavul çok ağır.'],
  ['کرم', 'خیلی ممنون، زحمت نکشید. خودم می‌توانم.', 'Çok teşekkürler, zahmet etmeyin. Kendim yapabilirim.'],
  ['پیرمرد', 'زحمتی نیست. شما مهمان محلهٔ ما هستید.', 'Zahmet değil. Siz mahallemizin misafirisiniz.'],
  ['کرم', 'شما از کجا می‌دانید که من به این خانه می‌آیم؟', 'Bu eve geleceğimi nereden biliyorsunuz?'],
  ['پیرمرد', 'در این کوچه هیچ خبری پنهان نمی‌ماند، پسرم!', 'Bu sokakta hiçbir haber gizli kalmaz, oğlum!'],
  ['کرم', 'پس باید مواظب باشم که کار بدی نکنم!', 'O zaman kötü bir şey yapmamaya dikkat etmeliyim!']])
E[1] = ([
 R('فردای آن روز کرم زود بیدار شد و دید که خانم شیرازی در حیاط به گلدان‌ها آب می‌دهد.', 'Ertesi gün Kerem erkenden uyandı ve Şirazi Hanım’ın avluda saksılara su verdiğini gördü.'),
 R('دور حوض گلدان‌های شمعدانی سرخ چیده شده بود و آب حوض از نور صبح می‌درخشید.', 'Havuzun çevresine kırmızı sardunya saksıları dizilmişti ve havuzun suyu sabah ışığıyla parlıyordu.'),
 R('خانم شیرازی گفت که این خانه بیش از صد سال پیش ساخته شده و پدربزرگش آن را از تاجری خریده است.', 'Şirazi Hanım bu evin yüz yıldan önce yapıldığını ve dedesinin onu bir tüccardan satın aldığını söyledi.'),
 R('اتاق‌های خانه دور حیاط ساخته شده بودند و پنجره‌های رنگی آنها نور را به رنگ‌های سرخ و سبز و آبی بر فرش می‌انداختند.', 'Evin odaları avlunun etrafına yapılmıştı ve renkli pencereleri ışığı halının üzerine kırmızı, yeşil ve mavi renklerle düşürüyordu.'),
 R('به این پنجره‌ها «اُرُسی» می‌گفتند و کرم یاد پنجره‌های چوبی خانه‌های قدیمی صفرانبولو افتاد.', 'Bu pencerelere “orsi” deniyordu; Kerem Safranbolu’nun eski evlerinin ahşap pencerelerini hatırladı.'),
 R('در گوشهٔ حیاط زیرزمینی بود که خانم شیرازی آن را «سرداب» می‌نامید.', 'Avlunun köşesinde Şirazi Hanım’ın “serdab” dediği bir bodrum vardı.'),
 R('او توضیح داد که در تابستان‌های داغ، پیش از کولر، خانواده ظهرها در سرداب استراحت می‌کرد، چون همیشه خنک بود.', 'Sıcak yazlarda, klimadan önce, ailenin serinliğinden dolayı öğlenleri serdabda dinlendiğini anlattı.'),
 R('کرم پرسید که آیا هنوز هم کسی آنجا می‌خوابد؛ خانم شیرازی خندید و گفت: «حالا فقط شیشه‌های ترشی و مربا آنجا می‌خوابند!»', 'Kerem hâlâ orada uyuyan biri olup olmadığını sordu; Şirazi Hanım güldü ve dedi: “Şimdi orada sadece turşu ve reçel kavanozları uyuyor!”'),
 R('بعد از صبحانه، کرم به مادرش زنگ زد و تصویری از حوض و درخت نارنج را برایش فرستاد.', 'Kahvaltıdan sonra Kerem annesini aradı ve havuzun ve turunç ağacının bir fotoğrafını ona gönderdi.'),
 R('مادرش گفت: «انگار خانهٔ مادربزرگت است؛ فقط حوضش بزرگ‌تر است.»', 'Annesi dedi: “Sanki ninenin evi; sadece havuzu daha büyük.”')],
 [['کرم', 'خانم شیرازی، این پنجره‌های رنگی را چه می‌نامند؟', 'Şirazi Hanım, bu renkli pencerelere ne deniyor?'],
  ['خانم شیرازی', 'اُرُسی. شیشه‌هایش را استادکاران قدیم یکی‌یکی بریده‌اند.', 'Orsi. Camlarını eski ustalar tek tek kesmişler.'],
  ['کرم', 'در ترکیه هم خانه‌هایی با پنجره‌های چوبی زیبا داریم.', 'Türkiye’de de güzel ahşap pencereli evlerimiz var.'],
  ['خانم شیرازی', 'باید عکسشان را به من نشان بدهی.', 'Fotoğraflarını bana göstermelisin.'],
  ['کرم', 'حتماً. امشب بعد از شام نشانتان می‌دهم.', 'Elbette. Bu akşam yemekten sonra gösteririm.'],
  ['خانم شیرازی', 'پس شام را زودتر آماده می‌کنم!', 'O zaman akşam yemeğini daha erken hazırlarım!']])
E[2] = ([
 R('ساختمان دانشکدهٔ ادبیات بنایی آجری با راهروهای بلند و پنجره‌های بزرگ بود.', 'Edebiyat fakültesinin binası uzun koridorlu ve büyük pencereli tuğla bir yapıydı.'),
 R('روی دیوار راهرو، عکس‌های سیاه و سفید استادان قدیمی دانشکده آویخته بودند.', 'Koridorun duvarına fakültenin eski hocalarının siyah beyaz fotoğrafları asılmıştı.'),
 R('در کلاس، استاد کاظمی اول از هر دانشجو خواست که خود را به فارسی معرفی کند.', 'Sınıfta Kâzımî Hoca önce her öğrenciden kendini Farsça tanıtmasını istedi.'),
 R('دانشجوی چینی، که نامش لی بود، گفت که سال‌ها رباعیات خیام را به چینی خوانده است.', 'Adı Li olan Çinli öğrenci, yıllarca Hayyam’ın rubailerini Çince okuduğunu söyledi.'),
 R('دختری از لبنان گفت که مادربزرگش اصفهانی بوده و او می‌خواهد زبان مادربزرگش را بیاموزد.', 'Lübnanlı bir kız, ninesinin İsfahanlı olduğunu ve ninesinin dilini öğrenmek istediğini söyledi.'),
 R('وقتی نوبت به کرم رسید، دستش کمی می‌لرزید، اما جمله‌هایش را بی‌اشتباه گفت.', 'Sıra Kerem’e geldiğinde eli biraz titriyordu, ama cümlelerini hatasız söyledi.'),
 R('گفت که در قونیه بزرگ شده و از کودکی صدای نی را در کنار آرامگاه مولانا شنیده است.', 'Konya’da büyüdüğünü ve çocukluğundan beri Mevlânâ’nın türbesinin yanında ney sesini duyduğunu söyledi.'),
 R('استاد لبخند زد و گفت: «پس تو از شهری آمده‌ای که شاعر بزرگ ما در آن آرمیده است.»', 'Hoca gülümsedi ve dedi: “Demek büyük şairimizin yattığı şehirden geldin.”'),
 R('پس از کلاس، نسرین کرم را به کتابخانهٔ دانشکده برد و نشان داد که چطور کارت عضویت بگیرد.', 'Dersten sonra Nesrin Kerem’i fakülte kütüphanesine götürdü ve nasıl üyelik kartı alacağını gösterdi.'),
 R('کتابدار پیر عینکش را بالا زد و گفت: «کتاب را می‌توانی دو هفته نگه داری، ولی دیوان حافظ را هیچ‌کس پس نمی‌آورد!»', 'Yaşlı kütüphaneci gözlüğünü kaldırdı ve dedi: “Kitabı iki hafta tutabilirsin; ama Hafız divanını kimse geri getirmez!”')],
 [['کتابدار', 'کارت دانشجویی‌ات را بده تا کارت کتابخانه برایت صادر کنم.', 'Öğrenci kartını ver de sana kütüphane kartı çıkarayım.'],
  ['کرم', 'بفرمایید. چند کتاب می‌توانم امانت بگیرم؟', 'Buyurun. Kaç kitap ödünç alabilirim?'],
  ['کتابدار', 'سه کتاب، برای دو هفته. اگر دیر بیاوری، جریمه می‌شوی.', 'Üç kitap, iki haftalığına. Geç getirirsen ceza ödersin.'],
  ['کرم', 'جریمه‌اش چقدر است؟', 'Cezası ne kadar?'],
  ['کتابدار', 'برای هر روز کمی پول؛ اما بدتر از آن، اخم من است!', 'Her gün için biraz para; ama ondan beteri benim kaş çatmam!'],
  ['نسرین', 'نگران نباش، آقای رضایی فقط شوخی می‌کند.', 'Merak etme, Rızâî Bey sadece şaka yapıyor.']])
E[3] = ([
 R('بازار وکیل را کریم‌خان زند در قرن دوازدهم هجری ساخته است؛ همان کسی که شیراز را پایتخت کرد.', 'Vekil Çarşısı’nı hicrî on ikinci yüzyılda Kerim Han Zend yaptırmıştır; Şiraz’ı başkent yapan kişi o’dur.'),
 R('نسرین گفت که کریم‌خان خود را «شاه» نمی‌نامید، بلکه «وکیل‌الرعایا» یعنی وکیل مردم می‌خواند.', 'Nesrin, Kerim Han’ın kendisine “şah” demediğini, “Vekîlü’r-reâyâ” yani halkın vekili dediğini anlattı.'),
 R('به همین دلیل بازار و مسجد و حمام آن دوره نام «وکیل» را دارند.', 'Bu yüzden o döneme ait çarşı, cami ve hamam “Vekil” adını taşır.'),
 R('در راسته‌های بازار، هر صنفی جای خود را داشت: مسگرها، فرش‌فروش‌ها، عطارها و پارچه‌فروش‌ها.', 'Çarşının sokaklarında her esnafın kendi yeri vardı: bakırcılar, halıcılar, aktarlar ve kumaşçılar.'),
 R('صدای چکش مسگرها در زیر سقف‌های گنبدی می‌پیچید و بوی زعفران و دارچین از دکان عطاری بیرون می‌آمد.', 'Bakırcıların çekiç sesi kubbeli tavanların altında yankılanıyor, aktar dükkânından safran ve tarçın kokusu yayılıyordu.'),
 R('کرم برای خودش کمی زعفران خرید، چون مادرش گفته بود که زعفران ایران بهترین زعفران دنیاست.', 'Kerem kendisi için biraz safran aldı, çünkü annesi İran safranının dünyanın en iyisi olduğunu söylemişti.'),
 R('عطار پیر با ترازوی کوچکی زعفران را وزن کرد و در کاغذی سفید پیچید.', 'Yaşlı aktar safranı küçük bir teraziyle tarttı ve beyaz bir kâğıda sardı.'),
 R('سپس گفت: «زعفران را با کمی شکر بکوب و در آب گرم دم کن؛ رنگ و بویش دوچندان می‌شود.»', 'Sonra dedi: “Safranı biraz şekerle döv ve ılık suda demle; rengi ve kokusu iki katına çıkar.”'),
 R('در پایان روز، کیسه‌های کرم پر بود و جیبش خالی؛ اما احساس می‌کرد که بیشتر از آنچه خرج کرده، چیز آموخته است.', 'Günün sonunda Kerem’in torbaları dolu, cebi boştu; ama harcadığından daha fazlasını öğrendiğini hissediyordu.')],
 [['عطار', 'زعفران برای غذا می‌خواهید یا برای دارو؟', 'Safranı yemek için mi istiyorsunuz, ilaç için mi?'],
  ['کرم', 'برای غذا. مادرم می‌خواهد شله‌زرد بپزد.', 'Yemek için. Annem zerde pişirmek istiyor.'],
  ['عطار', 'شله‌زرد؟ پس شما هم شله‌زرد دارید!', 'Zerde mi? Demek sizde de zerde var!'],
  ['کرم', 'بله، در ترکیه به آن «زرده» می‌گوییم و در عروسی‌ها می‌پزیم.', 'Evet, Türkiye’de ona “zerde” deriz ve düğünlerde pişiririz.'],
  ['عطار', 'می‌بینید؟ غذاهای ما هم مثل زبان‌هایمان خویشاوندند.', 'Görüyor musunuz? Yemeklerimiz de dillerimiz gibi akrabadır.'],
  ['نسرین', 'آقای عطار، یک مثقال هم برای من بکشید، لطفاً.', 'Aktar bey, bir miskal de bana tartın lütfen.']])
E[4] = ([
 R('آرامگاه حافظ در دورهٔ کریم‌خان زند بنا شد و بعدها در قرن چهاردهم هجری شمسی، معماری فرانسوی به نام آندره گدار آن را بازسازی کرد.', 'Hafız’ın türbesi Kerim Han Zend döneminde yapıldı; sonra hicrî şemsî on dördüncü yüzyılda André Godard adlı bir Fransız mimar onu yeniden inşa etti.'),
 R('ستون‌های سنگی بلند ایوان و کاشی‌های فیروزه‌ای گنبد، آرامگاه را به جایی آرام و باشکوه بدل کرده بود.', 'Eyvanın yüksek taş sütunları ve kubbenin firuze çinileri türbeyi huzurlu ve görkemli bir yere dönüştürmüştü.'),
 R('روی سنگ قبر، غزلی از حافظ با خطی زیبا کنده شده بود.', 'Mezar taşının üstüne Hafız’ın bir gazeli güzel bir hatla oyulmuştu.'),
 R('نسرین گفت که بسیاری از ایرانیان در هر خانه دیوان حافظ و قرآن را کنار هم نگه می‌دارند.', 'Nesrin, birçok İranlının her evde Hafız divanını ve Kur’an’ı yan yana tuttuğunu söyledi.'),
 R('کرم پرسید چرا حافظ را «لسان‌الغیب» می‌نامند.', 'Kerem Hafız’a neden “Lisânü’l-gayb” dendiğini sordu.'),
 R('نسرین پاسخ داد: «چون مردم باور دارند که شعرش از رازهای دل خبر می‌دهد؛ گویی از غیب سخن می‌گوید.»', 'Nesrin cevap verdi: “Çünkü insanlar onun şiirinin gönlün sırlarından haber verdiğine inanır; sanki gaybdan konuşuyor.”'),
 R('همچنین گفت که خود حافظ قرآن را با چهارده روایت از بر داشت، و نامش هم از همین است.', 'Ayrıca Hafız’ın Kur’an’ı on dört rivayetle ezbere bildiğini ve adının da buradan geldiğini söyledi.'),
 R('کرم در دل گفت: «پس او هم مانند ما حافظ قرآن بود، نه فقط شاعر.»', 'Kerem içinden dedi: “Demek o da bizim gibi Kur’an hafızıydı, sadece şair değil.”'),
 R('وقتی هوا تاریک شد، چراغ‌های باغ روشن شدند و یک گروه موسیقی سنتی در گوشه‌ای شروع به نواختن کرد.', 'Hava kararınca bahçenin lambaları yandı ve bir köşede geleneksel bir müzik grubu çalmaya başladı.'),
 R('کرم و نسرین تا دیروقت ماندند و به صدای تار و آواز گوش دادند.', 'Kerem ve Nesrin geç saate kadar kalıp tar ve şarkı sesini dinlediler.')],
 [['کرم', 'حافظ واقعاً همهٔ قرآن را حفظ بود؟', 'Hafız gerçekten bütün Kur’an’ı ezbere biliyor muydu?'],
  ['نسرین', 'خودش در شعری می‌گوید که قرآن را با چهارده روایت می‌خواند.', 'Kendisi bir şiirinde Kur’an’ı on dört rivayetle okuduğunu söyler.'],
  ['کرم', 'پس شعرش هم باید پر از اشاره به قرآن باشد.', 'O zaman şiiri de Kur’an’a işaretlerle dolu olmalı.'],
  ['نسرین', 'دقیقاً. بعضی از استادان کتاب‌هایی فقط دربارهٔ همین موضوع نوشته‌اند.', 'Kesinlikle. Bazı hocalar sadece bu konu hakkında kitaplar yazmış.'],
  ['کرم', 'این می‌تواند موضوع خوبی برای پایان‌نامه باشد!', 'Bu iyi bir tez konusu olabilir!'],
  ['نسرین', 'اول زبانت را قوی کن، بعد به پایان‌نامه فکر کن!', 'Önce dilini güçlendir, sonra tezi düşün!']])
E[5] = ([
 R('باغ ارم امروز باغ گیاه‌شناسی دانشگاه شیراز است و گیاهانی از سراسر ایران در آن کاشته‌اند.', 'Eram Bahçesi bugün Şiraz Üniversitesi’nin botanik bahçesidir ve içine İran’ın her yerinden bitkiler dikilmiştir.'),
 R('در میان باغ، کاخی قاجاری با کاشی‌های رنگارنگ و نقش‌هایی از داستان‌های شاهنامه قرار دارد.', 'Bahçenin ortasında renkli çinileri ve Şehnâme hikâyelerinden resimleri olan bir Kaçar köşkü bulunur.'),
 R('استاد کاظمی گفت که نام «ارم» از قرآن آمده است: «إِرَمَ ذَاتِ الْعِمَادِ»، شهری با ستون‌های بلند.', 'Kâzımî Hoca, “İrem” adının Kur’an’dan geldiğini söyledi: “İrem zâti’l-imâd”, yüksek sütunlu bir şehir.'),
 R('سپس افزود که شاعران فارسی «باغ ارم» را نماد بهشت زمینی دانسته‌اند.', 'Sonra Fars şairlerinin “İrem bağı”nı yeryüzü cennetinin sembolü saydıklarını ekledi.'),
 R('بعد از خواندن جمله‌ها، دانشجویان دور هم نشستند و هر کس غذایی از کشور خود آورده بود.', 'Cümleler okunduktan sonra öğrenciler bir araya oturdu; her biri kendi ülkesinden bir yemek getirmişti.'),
 R('لی پیراشکی چینی آورده بود، دختر لبنانی تبوله، و کرم باقلوایی که در بازار پیدا کرده بود.', 'Li Çin mantısı getirmişti, Lübnanlı kız tabule, Kerem de çarşıda bulduğu baklavayı.'),
 R('استاد گفت: «این سفره خودش یک کلاس زبان است؛ هر غذا داستانی دارد.»', 'Hoca dedi: “Bu sofra başlı başına bir dil dersidir; her yemeğin bir hikâyesi vardır.”'),
 R('آن شب هر کس به نوبت دربارهٔ غذای خود به فارسی سخن گفت، و کرم دید که همه با چه شوقی گوش می‌دهند.', 'O gece herkes sırayla kendi yemeği hakkında Farsça konuştu; Kerem herkesin ne büyük bir hevesle dinlediğini gördü.')],
 [['لی', 'کرم، این شیرینی را چطور درست می‌کنند؟', 'Kerem, bu tatlıyı nasıl yapıyorlar?'],
  ['کرم', 'لایه‌های نازک خمیر را روی هم می‌چینند و میانشان پسته می‌ریزند.', 'İnce hamur katlarını üst üste dizip aralarına fıstık serperler.'],
  ['لی', 'چند لایه دارد؟', 'Kaç katı var?'],
  ['کرم', 'گاهی چهل لایه! مادربزرگم می‌گفت هر لایه یک دعاست.', 'Bazen kırk kat! Ninem her katın bir dua olduğunu söylerdi.'],
  ['استاد کاظمی', 'چه جملهٔ زیبایی! این را در دفترت بنویس.', 'Ne güzel bir cümle! Bunu defterine yaz.'],
  ['کرم', 'چشم استاد، امشب حتماً می‌نویسم.', 'Baş üstüne hocam, bu gece mutlaka yazarım.']])
E[7] = ([
 R('نان سنگک را روی ریگ‌های داغ می‌پزند و نامش از همین «سنگ» گرفته شده است.', 'Sengek ekmeğini kızgın çakıl taşları üzerinde pişirirler ve adı da bu “seng” (taş) kelimesinden gelir.'),
 R('گاهی ریگی کوچک به نان می‌چسبد و مردم پیش از خوردن آن را با دقت جدا می‌کنند.', 'Bazen küçük bir çakıl ekmeğe yapışır ve insanlar yemeden önce onu dikkatle ayırır.'),
 R('پسر کوچک، که نامش آرش بود، گفت که هر روز پیش از مدرسه نان می‌خرد.', 'Adı Âreş olan küçük oğlan, her gün okuldan önce ekmek aldığını söyledi.'),
 R('او پرسید: «در ترکیه هم صف نانوایی این‌قدر طولانی است؟»', 'Sordu: “Türkiye’de de fırın kuyruğu bu kadar uzun mu?”'),
 R('کرم گفت که در ماه رمضان، پیش از افطار، صف نان پیده از این هم طولانی‌تر می‌شود.', 'Kerem, ramazanda iftardan önce pide kuyruğunun bundan da uzun olduğunu söyledi.'),
 R('آرش با تعجب گفت: «پس شما هم نان را مثل ما دوست دارید!»', 'Âreş şaşırarak dedi: “Demek siz de ekmeği bizim gibi seviyorsunuz!”'),
 R('در راه بازگشت، کرم تکه‌ای از نان داغ را کند و خورد؛ طعمش با هیچ نانی که پیش‌تر خورده بود قابل مقایسه نبود.', 'Dönüş yolunda Kerem sıcak ekmekten bir parça koparıp yedi; tadı daha önce yediği hiçbir ekmekle kıyaslanamazdı.'),
 R('خانم شیرازی با دیدن نان نیمه‌خورده خندید و گفت: «هیچ‌کس نان سنگک را سالم به خانه نمی‌رساند!»', 'Şirazi Hanım yarısı yenmiş ekmeği görünce güldü ve dedi: “Hiç kimse sengeği eve bütün getiremez!”'),
 R('سر سفرهٔ صبحانه، پنیر و گردو و سبزی خوردن کنار نان چیده شد و چای تازه‌دم در استکان‌ها ریخت.', 'Kahvaltı sofrasında ekmeğin yanına peynir, ceviz ve yeşillik dizildi; taze demlenmiş çay ince belli bardaklara döküldü.')],
 [['آرش', 'شما هر روز نان می‌خرید یا فقط امروز؟', 'Her gün ekmek mi alıyorsunuz, yoksa sadece bugün mü?'],
  ['کرم', 'امروز نوبت من است. فردا نوبت خانم شیرازی است.', 'Bugün sıra bende. Yarın Şirazi Hanım’da.'],
  ['آرش', 'من هر روز می‌خرم. پدرم می‌گوید نان خریدن مرد را صبور می‌کند!', 'Ben her gün alıyorum. Babam ekmek almanın adamı sabırlı yaptığını söylüyor!'],
  ['کرم', 'پدرت راست می‌گوید؛ این صف واقعاً صبر می‌خواهد.', 'Baban doğru söylüyor; bu kuyruk gerçekten sabır istiyor.'],
  ['آرش', 'فردا هم بیایید تا با هم در صف بایستیم.', 'Yarın da gelin de kuyrukta birlikte duralım.'],
  ['کرم', 'قول می‌دهم، اگر خواب نمانم!', 'Söz veriyorum, uyuya kalmazsam!']])
E[8] = ([
 R('تخت جمشید را داریوش بزرگ بنا کرد و پادشاهان پس از او آن را گسترش دادند.', 'Persepolis’i Büyük Dârâ (Darius) kurdu ve ondan sonraki krallar onu genişletti.'),
 R('در نوروز، نمایندگان سرزمین‌های گوناگون با هدیه‌هایشان از پله‌ها بالا می‌رفتند تا به حضور شاه برسند.', 'Nevruzda çeşitli ülkelerin temsilcileri hediyeleriyle şahın huzuruna çıkmak için merdivenlerden yukarı çıkarlardı.'),
 R('استاد کاظمی گفت که پله‌ها را کوتاه ساخته‌اند تا مهمانان با آرامش و وقار بالا روند.', 'Kâzımî Hoca, misafirler huzur ve vakarla çıksın diye basamakların alçak yapıldığını söyledi.'),
 R('سپس نقش شیری را نشان داد که با گاوی می‌جنگد و گفت که آن را نماد آمدن بهار دانسته‌اند.', 'Sonra bir boğayla dövüşen bir arslan kabartmasını gösterdi ve onun baharın gelişinin sembolü sayıldığını söyledi.'),
 R('اسکندر مقدونی این کاخ‌ها را در آتش سوزاند و آنچه امروز می‌بینیم، تنها ویرانه‌ای از شکوه گذشته است.', 'Makedonyalı İskender bu sarayları yaktı; bugün gördüğümüz, geçmiş ihtişamın sadece bir harabesidir.'),
 R('کرم به یاد بیتی از خیام افتاد که از کاخ‌هایی می‌گوید که روزی شاهان در آنها بودند و اکنون فاخته بر بامشان می‌خواند.', 'Kerem, bir zamanlar şahların bulunduğu ve şimdi damlarında kumruların öttüğü saraylardan söz eden Hayyam’ın bir beytini hatırladı.'),
 R('نسرین گفت: «همهٔ شاعران ما از ویرانه‌ها درس گرفته‌اند؛ ناپایداری دنیا یکی از موضوع‌های اصلی شعر فارسی است.»', 'Nesrin dedi: “Bütün şairlerimiz harabelerden ders almıştır; dünyanın geçiciliği Fars şiirinin temel konularından biridir.”'),
 R('در راه برگشت، اتوبوس در کنار جاده ایستاد و همه از چشمه‌ای آب خنک نوشیدند.', 'Dönüş yolunda otobüs yol kenarında durdu ve herkes bir pınardan serin su içti.')],
 [['استاد کاظمی', 'کرم، در ترکیه هم ویرانه‌هایی مثل اینجا دارید؟', 'Kerem, Türkiye’de de burası gibi harabeleriniz var mı?'],
  ['کرم', 'بله، مثلاً افسس و نمرود‌داغ. مجسمه‌های بزرگ نمرود را دیده‌اید؟', 'Evet, mesela Efes ve Nemrut Dağı. Nemrut’un büyük heykellerini gördünüz mü?'],
  ['استاد کاظمی', 'فقط در عکس. شنیده‌ام که آنها هم به شاهان ایرانی ربط دارند.', 'Sadece fotoğrafta. Onların da İran şahlarıyla bağlantılı olduğunu duydum.'],
  ['کرم', 'بله، پادشاه کماگنه خود را از نسل داریوش می‌دانست.', 'Evet, Kommagene kralı kendini Dârâ’nın soyundan sayardı.'],
  ['نسرین', 'پس تاریخ ما بیش از آنچه فکر می‌کردیم به هم گره خورده است.', 'Demek tarihimiz sandığımızdan daha çok birbirine bağlanmış.'],
  ['استاد کاظمی', 'درست است. زبان، تاریخ و شعر مرز نمی‌شناسند.', 'Doğru. Dil, tarih ve şiir sınır tanımaz.']])
E[9] = ([
 R('در آن سه روز، خانم شیرازی هر صبح جوشانده‌ای از گل گاوزبان و لیمو عمانی برای کرم دم می‌کرد.', 'O üç gün boyunca Şirazi Hanım her sabah Kerem için hodan çiçeği ve kuru limonla bir kaynatma hazırladı.'),
 R('می‌گفت: «طب سنتی ما می‌گوید که سرماخوردگی از سردی است و باید غذای گرم خورد.»', 'Diyordu ki: “Bizim geleneksel tıbbımız soğuk algınlığının soğukluktan olduğunu ve sıcak yemek yemek gerektiğini söyler.”'),
 R('کرم به یاد آورد که مادربزرگش هم در قونیه همین را می‌گفت و برایش سوپ عدس می‌پخت.', 'Kerem, ninesinin de Konya’da aynı şeyi söylediğini ve ona mercimek çorbası pişirdiğini hatırladı.'),
 R('نسرین با یک سبد میوه و جزوه‌های درس به عیادتش آمد.', 'Nesrin bir sepet meyve ve ders notlarıyla onu ziyarete geldi.'),
 R('گفت: «استاد سلام رساند و گفت که درس‌ها را از دست ندهی.»', 'Dedi: “Hoca selam gönderdi ve dersleri kaçırmamanı söyledi.”'),
 R('کرم در بستر، جزوه‌ها را خواند و برای اولین بار یک شعر کوتاه فارسی از حفظ کرد.', 'Kerem yatağında notları okudu ve ilk kez kısa bir Farsça şiiri ezberledi.'),
 R('بیماری به او فرصت داد که در سکوت بیشتر بخواند و بیندیشد.', 'Hastalık ona sessizlik içinde daha çok okuma ve düşünme fırsatı verdi.'),
 R('روز چهارم که به کلاس رفت، استاد گفت: «پس بیماری هم برایت معلم خوبی بوده است!»', 'Dördüncü gün derse gittiğinde hoca dedi: “Demek hastalık da senin için iyi bir öğretmen olmuş!”')],
 [['نسرین', 'حالت بهتر است؟ صدایت هنوز گرفته است.', 'Daha iyi misin? Sesin hâlâ kısık.'],
  ['کرم', 'بهترم، ولی هنوز کمی سرفه دارم.', 'Daha iyiyim, ama hâlâ biraz öksürüğüm var.'],
  ['نسرین', 'این میوه‌ها را بخور؛ پر از ویتامین است.', 'Bu meyveleri ye; vitamin dolu.'],
  ['کرم', 'دستت درد نکند. زحمت کشیدی.', 'Elin dert görmesin. Zahmet ettin.'],
  ['نسرین', 'خواهش می‌کنم. زود خوب شو؛ کلاس بدون تو ساکت است!', 'Rica ederim. Çabuk iyileş; sınıf sensiz sessiz!'],
  ['کرم', 'پس‌فردا حتماً می‌آیم، ان‌شاءالله.', 'Öbür gün mutlaka gelirim, inşallah.']])
E[10] = ([
 R('کتاب‌فروش پیر گفت که پنجاه سال است در همین دکان کار می‌کند و پدرش نیز پیش از او همین‌جا کتاب می‌فروخت.', 'Yaşlı kitapçı elli yıldır bu dükkânda çalıştığını ve babasının da ondan önce burada kitap sattığını söyledi.'),
 R('او از روزهایی حرف زد که شاعران و نویسندگان مشهور شیراز در همین دکان دور هم جمع می‌شدند.', 'Şiraz’ın ünlü şair ve yazarlarının bu dükkânda bir araya geldiği günlerden söz etti.'),
 R('سپس از قفسه‌ای بالا یک چاپ سنگی کهنه از گلستان پایین آورد و ورق‌هایش را با احتیاط گشود.', 'Sonra yüksek bir raftan Gülistan’ın eski bir taş baskısını indirdi ve yapraklarını dikkatle açtı.'),
 R('خط نستعلیق آن چنان زیبا بود که کرم مدتی فقط به شکل حرف‌ها نگاه کرد.', 'Nestalik hattı öyle güzeldi ki Kerem bir süre yalnızca harflerin şekline baktı.'),
 R('کتاب‌فروش گفت: «در چاپ سنگی، خوشنویس متن را بر سنگ می‌نوشت و هر صفحه یک اثر هنری بود.»', 'Kitapçı dedi: “Taş baskıda hattat metni taşa yazardı ve her sayfa bir sanat eseriydi.”'),
 R('کرم گفت که در استانبول هم کتاب‌های چاپ سنگی عثمانی را در بازار صحافان دیده است.', 'Kerem İstanbul’da da Sahaflar Çarşısı’nda Osmanlı taş baskı kitaplarını gördüğünü söyledi.'),
 R('پیرمرد چشمانش برق زد: «صحافان! همیشه آرزو داشتم آنجا را ببینم.»', 'Yaşlı adamın gözleri parladı: “Sahaflar! Hep orayı görmeyi arzu etmiştim.”'),
 R('کرم قول داد که روزی از آنجا کتابی برایش بفرستد، و پیرمرد گفت: «پس ما دوست شدیم؛ دوستیِ کتاب‌ها از همه پایدارتر است.»', 'Kerem bir gün oradan ona bir kitap göndereceğine söz verdi; yaşlı adam dedi: “O hâlde dost olduk; kitapların dostluğu en kalıcı olanıdır.”')],
 [['کتاب‌فروش', 'این چاپ سنگی گلستان را ببین. صد سال پیش در بمبئی چاپ شده.', 'Gülistan’ın şu taş baskısına bak. Yüz yıl önce Bombay’da basılmış.'],
  ['کرم', 'بمبئی؟ مگر در هند هم کتاب فارسی چاپ می‌شد؟', 'Bombay mı? Hindistan’da da Farsça kitap mı basılırdı?'],
  ['کتاب‌فروش', 'بله، بسیاری از بهترین چاپ‌های فارسی در هند انجام شده است.', 'Evet, en iyi Farsça baskıların çoğu Hindistan’da yapılmıştır.'],
  ['کرم', 'چه جالب! فارسی واقعاً زبانی جهانی بوده است.', 'Ne ilginç! Farsça gerçekten evrensel bir dil olmuş.'],
  ['کتاب‌فروش', 'از استانبول تا دهلی، اهل قلم به فارسی می‌نوشتند.', 'İstanbul’dan Delhi’ye kalem ehli Farsça yazardı.'],
  ['کرم', 'و حالا من از قونیه آمده‌ام تا همان راه را ادامه دهم.', 'Ve şimdi ben aynı yolu sürdürmek için Konya’dan geldim.']])
E[11] = ([
 R('مادربزرگ خانواده گفت که در قدیم، شب یلدا را «شب چله» هم می‌نامیدند، چون آغاز چهل روز سرمای سخت زمستان است.', 'Ailenin ninesi, eskiden Yeldâ gecesine “çille gecesi” de dendiğini, çünkü kışın sert soğuğunun kırk gününün başlangıcı olduğunu söyledi.'),
 R('کرم با شگفتی گفت که در ترکیه هم «چله» داریم و مادرش همیشه می‌گفت که در چلهٔ بزرگ باید خود را گرم نگه داشت.', 'Kerem hayretle Türkiye’de de “zemheri/çille” olduğunu ve annesinin büyük çillede insanın kendini sıcak tutması gerektiğini hep söylediğini anlattı.'),
 R('پدربزرگ گفت: «می‌بینی؟ ما فقط همسایه نیستیم؛ تقویم و آیین‌هایمان هم یکی است.»', 'Dede dedi: “Görüyor musun? Biz sadece komşu değiliz; takvimimiz ve âdetlerimiz de birdir.”'),
 R('سپس شاهنامه را گشود و داستان کودکی رستم را با آوازی آرام خواند.', 'Sonra Şehnâme’yi açtı ve Rüstem’in çocukluğunun hikâyesini yavaş bir ezgiyle okudu.'),
 R('بچه‌ها گرد او نشسته بودند و هر بار که نام رخش، اسب رستم، می‌آمد، فریاد شادی می‌کشیدند.', 'Çocuklar etrafına oturmuştu; Rüstem’in atı Rahş’ın adı her geçtiğinde sevinçle bağırıyorlardı.'),
 R('کرم دانست که شاهنامه برای ایرانیان فقط کتاب نیست؛ بخشی از خاطرهٔ خانوادگی است.', 'Kerem, Şehnâme’nin İranlılar için yalnızca bir kitap değil, aile hafızasının bir parçası olduğunu anladı.'),
 R('نزدیک نیمه‌شب، خانم شیرازی هندوانه را برید و گفت که هر کس شب یلدا هندوانه بخورد، در تابستان گرما نمی‌بیند.', 'Gece yarısına doğru Şirazi Hanım karpuzu kesti ve Yeldâ gecesi karpuz yiyenin yazın sıcaktan etkilenmeyeceğini söyledi.'),
 R('کرم خندید: «پس من امشب دو برش می‌خورم، چون تابستان قونیه خیلی داغ است!»', 'Kerem güldü: “O zaman bu gece iki dilim yiyeceğim, çünkü Konya’nın yazı çok sıcak!”')],
 [['مادربزرگ', 'پسرم، در ترکیه شب‌های زمستان چه می‌کنید؟', 'Oğlum, Türkiye’de kış gecelerinde ne yaparsınız?'],
  ['کرم', 'در روستاها مردم دور هم جمع می‌شوند، قصه می‌گویند و تخمه می‌شکنند.', 'Köylerde insanlar bir araya gelir, masal anlatır ve çekirdek çitlerler.'],
  ['مادربزرگ', 'درست مثل ما! قصه‌های شما هم دیو و پری دارد؟', 'Tıpkı bizim gibi! Sizin masallarınızda da dev ve peri var mı?'],
  ['کرم', 'بله، و قهرمانی به نام کلوغلان که شبیه قهرمانان شما است.', 'Evet, sizin kahramanlarınıza benzeyen Keloğlan adında bir kahraman var.'],
  ['پدربزرگ', 'پس دفعهٔ بعد تو برای ما قصه بگو!', 'O zaman bir dahaki sefere sen bize masal anlat!'],
  ['کرم', 'به شرطی که شما هم باز شاهنامه بخوانید.', 'Siz de yine Şehnâme okursanız.']])
E[12] = ([
 R('در ادامهٔ نامه نوشت: «مادر جان، اینجا هر روز چیزی تازه یاد می‌گیرم؛ گاهی از استاد و گاهی از نانوای سر کوچه.»', 'Mektubun devamında yazdı: “Anneciğim, burada her gün yeni bir şey öğreniyorum; bazen hocadan, bazen sokağın başındaki fırıncıdan.”'),
 R('«دیروز پسرکی به نام آرش به من یاد داد که نان داغ را چطور بگیرم که دستم نسوزد.»', '“Dün Âreş adında küçük bir oğlan bana sıcak ekmeği elim yanmadan nasıl tutacağımı öğretti.”'),
 R('«پدربزرگ خانواده در شب یلدا برایم فال حافظ گرفت و گفت سفرم مبارک است.»', '“Yeldâ gecesi ailenin dedesi bana Hafız falı baktı ve yolculuğumun mübarek olduğunu söyledi.”'),
 R('«گاهی دلم برای صدای اذان مسجد محله‌مان و برای چای عصرهای تو تنگ می‌شود.»', '“Bazen mahallemizin camisinin ezan sesini ve senin ikindi çaylarını özlüyorum.”'),
 R('«اما وقتی به حرم شاه‌چراغ می‌روم و صدای قرآن را می‌شنوم، احساس می‌کنم که در خانهٔ خودم هستم.»', '“Ama Şâhçerâğ türbesine gidip Kur’an sesini duyduğumda kendimi evimde gibi hissediyorum.”'),
 R('«برایم دعا کن که درسم را خوب تمام کنم و با دست پر برگردم؛ نه با چمدانی پر، بلکه با دلی پر.»', '“Derslerimi iyi bitirip eli dolu dönmem için bana dua et; dolu bir bavulla değil, dolu bir gönülle.”'),
 R('پستچی پیر در ادارهٔ پست، نامه را وزن کرد و تمبری با تصویر گل سرخ بر آن چسباند.', 'Postanede yaşlı postacı mektubu tarttı ve üzerine kırmızı gül resimli bir pul yapıştırdı.'),
 R('کرم هنگام بیرون آمدن از اداره احساس کرد که بخشی از دلش را همراه نامه به قونیه فرستاده است.', 'Kerem postaneden çıkarken gönlünün bir parçasını mektupla birlikte Konya’ya gönderdiğini hissetti.')],
 [['پستچی', 'این نامه به کجا می‌رود؟', 'Bu mektup nereye gidiyor?'],
  ['کرم', 'به ترکیه، شهر قونیه.', 'Türkiye’ye, Konya şehrine.'],
  ['پستچی', 'قونیه! سال‌ها پیش آرزو داشتم به زیارت مولانا بروم.', 'Konya! Yıllar önce Mevlânâ’yı ziyaret etmeyi arzu ederdim.'],
  ['کرم', 'اگر روزی آمدید، مهمان ما باشید؛ خانهٔ ما نزدیک آرامگاه است.', 'Bir gün gelirseniz misafirimiz olun; evimiz türbeye yakın.'],
  ['پستچی', 'خدا از دهانت بشنود! نامه‌ات ده روزه می‌رسد.', 'Ağzından Allah işitsin! Mektubun on günde ulaşır.'],
  ['کرم', 'متشکرم. ان‌شاءالله به سلامت برسد.', 'Teşekkür ederim. İnşallah sağ salim ulaşır.']])

kok = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
vf = os.path.join(kok, 'veri', 'farsca.js')
s = open(vf, encoding='utf-8').read()
bas = s.index('var D=['); son = s.index('\n];', bas)
D = json.loads(subprocess.check_output(['node', '-e', "const fs=require('fs');const o={};new Function('o',fs.readFileSync(process.argv[1],'utf8')+';o.D=D')(o);process.stdout.write(JSON.stringify(o.D))", vf]))
for i, (rd, dia) in E.items():
    d = D[i]
    if rd[0][0] in [r[0] for r in d['read']]: continue
    d['read'] += rd; d['dia'] += dia
yeni = 'var D=[\n' + ',\n\n'.join(json.dumps(g, ensure_ascii=False, separators=(',', ':')) for g in D)
s = s[:bas] + yeni + s[son:]
open(vf, 'w', encoding='utf-8').write(s)
print('uzatıldı:', [(i, len(D[i]['read']), len(D[i]['dia'])) for i in E])
