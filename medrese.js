/* el-Mihrâb · MEDRESE — klasik Arapça (sarf · nahiv · Kur'an i'râbı)
   Bütün içerik "taslak → onaylı" kuralına tâbidir: ehil onayı olmayan her şey "taslak" damgalıdır. */
'use strict';
const $ = (s, r) => (r || document).querySelector(s), $$ = (s, r) => [...(r || document).querySelectorAll(s)];
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const LS = { get(k, d){ try{ const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v) }catch(e){ return d } }, set(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)) }catch(e){ try{ localStorage.removeItem('medrese.ydsD'); localStorage.setItem(k, JSON.stringify(v)) }catch(x){} } }, del(k){ try{ localStorage.removeItem(k) }catch(e){} } };
/* Sağlam veri yükleme: zaman aşımı, yeniden deneme, biçim denetimi */
function getJSON(url, ok, opt){ const bir = n => { const c = typeof AbortController === 'function' ? new AbortController() : null, t = setTimeout(() => c && c.abort(), 15000); return fetch(url, Object.assign({ signal: c ? c.signal : undefined }, opt || {})).then(r => { if(!r.ok) throw new Error('HTTP ' + r.status); return r.json() }).then(j => { clearTimeout(t); if(!j || typeof j !== 'object' || (ok && !ok(j))) throw new Error('Bozuk veri: ' + url); return j }).catch(e => { clearTimeout(t); if(n > 0) return new Promise(r => setTimeout(r, 600)).then(() => bir(n - 1)); throw e }) }; return bir(2) }
function toast(m){ const t = $('#toast'); t.textContent = m; t.classList.add('show'); clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove('show'), 2600) }
function SN(){ return S_TR }
const shuffle = a => { a = a.slice(); for(let i = a.length - 1; i > 0; i--){ const j = Math.random() * (i + 1) | 0; [a[i], a[j]] = [a[j], a[i]] } return a };
const pick = a => a[Math.random() * a.length | 0];
const today = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 6e4) / 864e5);
const REPO = 'https://github.com/muhibbimnz-ctrl/el-mihrab/issues/new';
const bugLink = (id, txt) => `${REPO}?title=${encodeURIComponent('Medrese hata bildirimi: ' + id)}&body=${encodeURIComponent((txt || '') + '\n\nHata nedir, doğrusu ne olmalı?\n')}&labels=medrese`;

/* ======================================================================
   KİTAPLAR (müfredat) — tanıtım bilgileri de taslaktır
   ====================================================================== */
const BOOKS = [
  { id: 'emsile', ad: 'Emsile', ar: 'الأمثلة', yol: 'sarf', sira: 1, durum: 'hazir',
    tanitim: {
      muellif: 'Müellifi kesin olarak bilinmiyor. Osmanlı medreselerinde sarfa ilk adım olarak okutulan, kısa ve ezberlenmek üzere hazırlanmış bir metindir.',
      amac: 'Tek bir kökten (نصر) fiil ve fiilden türeyen isimlerin bütün kalıplarını göstermek: mâzî, muzâri, menfî, meçhûl, cahd, nehiy, emir, nûn-ı tekîd; ism-i fâil, ism-i mef‘ûl, zaman-mekân, âlet ve tafdîl isimleri. Öğrenci bu kalıpları bir kez ezberleyince her sâlim fiili kendisi çekebilir.',
      yontem: 'Önce “Emsile-i muhtelife” sesli ve ritmik tekrarla ezberlenir. Sonra “Emsile-i muttaride” bölüm bölüm, her sîga Türkçesiyle okunur. Her bölümden sonra kökü değiştirip (ضرب، فتح، علم…) aynı kalıbı kendiniz çekin; alıştırmalar ve aralıklı tekrar unutmayı önler.'
    } },
  { id: 'bina', ad: 'Binâ', ar: 'البناء', yol: 'sarf', sira: 2, durum: 'hazir',
    tanitim: { muellif: 'Müellifi kesin olarak bilinmiyor; Emsile’den sonra okutulur.', amac: 'Otuz beş tasrîf bâbını (6 sülâsî mücerred, 12 sülâsî mezîd, rubâî ve mülhakları) alâmeti ve binâsıyla vermek; sonra fiilin sekiz ve yedi kısmını (sahih, misâl, ecvef, nâkıs, lefîf, muzâ‘af, mehmûz) tanıtmak.', yontem: 'Tam matn, Mecmûatü’s-sarf nüshasından. Her paragrafa dokununca Türkçesi açılır; her bâbın vezin ve misalini Emsile’de çekimleyin.' } },
  { id: 'maksud', ad: 'Maksûd', ar: 'المقصود', yol: 'sarf', sira: 3, durum: 'hazir',
    tanitim: { muellif: 'İmâm-ı Âzam Ebû Hanîfe’ye nisbet edilir; bu nisbet tartışmalıdır.', amac: 'Sarf kurallarını, özellikle mezîd bâbları ve i‘lâl kaidelerini sistemli biçimde vermek.', yontem: 'Tam matn, Mecmûatü’s-sarf nüshasından. Her paragrafa dokununca Türkçesi açılır; masdar–mâzî–muzâri–emir–fâil–mef‘ûl türetimini Emsile çekimleriyle karşılaştırın.' } },
  { id: 'izzi', ad: 'İzzî', ar: 'التصريف العزي', yol: 'sarf', sira: 4, durum: 'hazir',
    tanitim: { muellif: 'İzzeddîn Abdülvehhâb b. İbrâhîm ez-Zencânî (7./13. yy).', amac: 'Tasrîf ilmini (kelimenin kalıptan kalıba çevrilmesi) özlü ve ileri seviyede vermek.', yontem: 'Tam matn, Mecmûatü’s-sarf nüshasından. Her paragrafa dokununca Türkçesi açılır; i‘lâl kaidelerini Kur’an i‘râbı modülündeki kelimelerde uygulayın.' } },
  { id: 'avamil', ad: 'Avâmil-i Cürcânî', ar: 'العوامل المائة', yol: 'nahiv', sira: 1, durum: 'hazir',
    tanitim: { muellif: 'İmam Abdülkâhir el-Cürcânî (ö. 471/1078) — “el-Avâmilü’l-mie” (Avâmil-i atîk). Belâgatta “Delâilü’l-i‘câz” ve “Esrârü’l-belâga”nın da müellifidir.', amac: 'Kelimelerin sonunu değiştiren yüz âmili (91 semâî, 7 kıyâsî, 2 ma‘nevî) on üç çeşit hâlinde, her birini örnekle tanıtmak. Nahvin “bunu ne ref‘ etti, ne nasbetti?” sorusuna buradan başlanır.', yontem: 'Her âmili örneğiyle birlikte ezberleyin. Cümleye dokununca Türkçesi açılır. Bâb sonundaki sorularla pekiştirin; i‘râbı Kur’an i‘râbı modülünde ve İ‘râb oyununda uygulayın.' } },
  { id: 'birgivi', ad: 'Avâmil (Birgivî)', ar: 'العوامل للبركوي', yol: 'nahiv', sira: 2, durum: 'hazir',
    tanitim: { muellif: 'İmam Birgivî Mehmed Efendi (ö. 981/1573), Balıkesir/Birgi. Osmanlı medreselerinde “Avâmil-i cedîd” diye okutulmuştur; şerhi aynı müellifin İzhâr’ıdır.', amac: 'İ‘râbı öğrenmek için gereken yüz şeyi —60 âmil, 30 ma‘mûl, 10 i‘râb— üç bâbta, her kuralı ahlâkî örnek cümlelerle vermek.', yontem: 'Harekeli Arapça metni okuyun, Türkçesi için paragrafa dokunun. Her bölümün sonunda o bâbtan sorular var; Emsile ve Binâ’dan sonra, İzhâr’dan önce okunur.' } },
  { id: 'izhar', ad: 'İzhâr', ar: 'إظهار الأسرار', yol: 'nahiv', sira: 2.5, durum: 'hazir',
    tanitim: { muellif: 'İmam Birgivî Mehmed Efendi (ö. 981/1573) — “İzhâru’l-esrâr fi’n-nahv”, kendi Avâmil’inin şerhi gibidir; Osmanlı medreselerinde Avâmil’den sonra okutulmuştur.', amac: 'Âmil, ma‘mûl ve i‘râbı Avâmil’den daha ayrıntılı, şartları ve istisnâlarıyla vermek: cer harfleri, nevâsih, kıyâsî âmiller, merfûât, mansûbât, tâbiler, takdîrî/mahallî i‘râb ve mebnîler.', yontem: '49 derse bölündü. Harekeli metni okuyun, Türkçe açıklama için paragrafa dokunun; her dersin sonunda o dersin sorusu var. Birgivî Avâmil’inden sonra okuyun.' } },
  { id: 'kavaid', ad: 'Kavâidü’l-i‘râb', ar: 'قواعد الإعراب', yol: 'nahiv', sira: 3.5, durum: 'hazir',
    tanitim: { muellif: 'İbn Hişâm el-Ensârî (ö. 761/1360) — “el-İ‘râb ‘an Kavâ‘idi’l-i‘râb”; Muğni’l-lebîb’in özü sayılan küçük bir risâle. Medreselerde İzhâr’dan sonra okutulmuştur.', amac: 'Cümlenin i‘râbını öğretmek: hangi cümlenin mahalli vardır, hangisinin yoktur; câr-mecrûrun müteallakı; i‘râb yaparken sık geçen edatlar ve dikkat edilecek ifadeler.', yontem: 'Şimdilik Mukaddime ve 1. Bâb (cümle ve hükümleri, dört mesele) hazır; diğer bâblar eklenecek. Harekeli metni okuyun, Türkçe açıklama için paragrafa dokunun; sonunda sorular var.' } },
  { id: 'zuruf', ad: 'Zurûf', ar: 'الظروف', yol: 'nahiv', sira: 3, durum: 'hazir',
    tanitim: { muellif: 'Molla Yûnus el-Erkutînî’nin risâlesi; Arapçaya Muhammed Şîrîn el-Bitlîsî aktarmış ve faydalar ekleyerek şerh gibi genişletmiştir. Doğu medreselerinde Avâmil’den sonra okutulur.', amac: 'Zarfın kısımlarını (hakikî–mecâzî, zaman–mekân, mübhem–muayyen), taallukunu, lağv ve müstekarr zarfı; sonunda nahvin tarifini ve i‘râbın kısımlarını vermek.', yontem: 'Harekeli metni okuyun, Türkçesi için paragrafa dokunun; bölüm sonlarındaki sorularla pekiştirin.' } },
  { id: 'ajurrumiyye', ad: 'Âcurrûmiyye', ar: 'الآجرومية', yol: 'nahiv', sira: 4, durum: 'hazir',
    tanitim: { muellif: 'İbn Âcurrûm es-Sanhâcî (ö. 723/1323), Fas. “Tuhfetü’s-seniyye” bu matnin şerhidir.', amac: 'Nahvin bütün temel bâblarını (i‘râb, alâmetler, merfûlar, mansûblar, mecrûrlar) en kısa yoldan vermek. Asırlardır nahve başlangıç metni olarak ezberlenir.', yontem: 'Her bâbı önce Arapça okuyun, sonra Türkçesine bakın; tanımları ezberleyin. Bâb sonundaki sorularla pekiştirin ve öğrendiğiniz i‘râbı Kur’an modülünde deneyin. Not: Tuhfetü’s-seniyye şerhi (M. Muhyiddîn Abdülhamîd, ö. 1972) telif kapsamında olduğu için uygulamaya matn ve bizim Türkçe açıklamamız konuldu.' } },
  { id: 'katr', ad: 'Katru’n-nedâ', ar: 'قطر الندى', yol: 'arsiv', sira: 3, durum: 'hazir',
    tanitim: { muellif: 'İbn Hişâm el-Ensârî (ö. 761/1360).', amac: 'Nahvin bütün bâblarını kısa ve yoğun bir matnle, şâhidleriyle vermek. Âcurrûmiyye’den sonra okunur.', yontem: 'Matni bâb bâb okuyun; her bâbın Türkçe özeti başta verilmiştir. Ardından aynı bâbı Şerhu Katri’n-nedâ’da müellifin kendi açıklamasıyla okuyun.' } },
  { id: 'serhkatr', ad: 'Şerhu Katri’n-nedâ', ar: 'شرح قطر الندى', yol: 'nahiv', sira: 4, durum: 'hazir',
    tanitim: { muellif: 'İbn Hişâm el-Ensârî (ö. 761/1360) — kendi matni Katru’n-nedâ’yı şerh etmiştir.', amac: 'Matnin her cümlesini (ص) açıp şâhidleriyle (âyet, hadis, şiir) şerh etmek (ش); orta-ileri seviyede nahvin temel şerhidir.', yontem: 'Altın çizgili kısımlar matndir, diğerleri şerh. Önce matn cümlesini, sonra müellifin açıklamasını okuyun; her bâbın sonunda Katru’n-nedâ alıştırmalarını çözün.' } },
  { id: 'kuran', ad: 'Kur’an i‘râbı', ar: 'إعراب القرآن', yol: 'kuran', sira: 1, durum: 'hazir',
    tanitim: { muellif: 'Kelime verisi: Quranic Arabic Corpus (Leeds Üniversitesi, corpus.quran.com, GNU GPL).', amac: 'Kur’ân-ı Kerîm’in her kelimesine dokununca sarf (kök, bâb, sîga) ve nahiv (i‘râb) çözümlemesini görmek; Emsile ve Avâmil’de öğrenileni Kur’an üzerinde uygulamak.', yontem: 'Bir sûre açın, kelimeye dokunun. Üstteki anahtarla Sarf ve Nahiv arasında geçin.' } },
  { id: 'yds', ad: 'YDS Arapça', ar: 'اختبار اللغة', yol: 'yds', sira: 1, durum: 'hazir',
    tanitim: { muellif: '—', amac: 'Kelime, dilbilgisi, cümle tamamlama, çeviri ve paragraf soruları; deneme sınavı.', yontem: 'Günlük kısa setler ve aralıklı tekrar.' } },
  { id: 'modern', ad: 'Modern Arapça', ar: 'العربية المعاصرة', yol: 'modern', sira: 1, durum: 'hazir',
    tanitim: { muellif: '—', amac: 'Günlük kelime, temel diyalog ve okuma.', yontem: 'Sesli dinleme ve tekrar.' } }
];
const YOL = { sarf: ['Sarf yolu', 'الصرف'], nahiv: ['Nahiv yolu', 'النحو'], kuran: ['Kur’an', 'القرآن'], yds: ['YDS', 'YDS'], modern: ['Modern Arapça', 'المعاصرة'] };

/* ======================================================================
   EMSİLE MOTORU — sâlim sülâsî mücerred kökten bütün kalıplar
   ====================================================================== */
const F = 'َ', Ki = 'ِ', D = 'ُ', S = 'ْ', SH = 'ّ', AN = 'ً', UN = 'ٌ';
const VV = { a: F, i: Ki, u: D };
const SIGA = [null,
  ['Müfred müzekker gâib', 'هُوَ', 'O (bir erkek)', 3, 1], ['Tesniye müzekker gâib', 'هُمَا', 'O ikisi (iki erkek)', 3, 1], ['Cem‘-i müzekker gâib', 'هُمْ', 'Onlar (erkekler)', 3, 3],
  ['Müfred müennes gâibe', 'هِيَ', 'O (bir kadın)', 3, 1], ['Tesniye müennes gâibe', 'هُمَا', 'O ikisi (iki kadın)', 3, 1], ['Cem‘-i müennes gâibe', 'هُنَّ', 'Onlar (kadınlar)', 3, 3],
  ['Müfred müzekker muhâtab', 'أَنْتَ', 'Sen (bir erkek)', 2, 1], ['Tesniye müzekker muhâtab', 'أَنْتُمَا', 'Siz ikiniz (iki erkek)', 2, 3], ['Cem‘-i müzekker muhâtab', 'أَنْتُمْ', 'Siz (erkekler)', 2, 3],
  ['Müfred müennes muhâtaba', 'أَنْتِ', 'Sen (bir kadın)', 2, 1], ['Tesniye müennes muhâtaba', 'أَنْتُمَا', 'Siz ikiniz (iki kadın)', 2, 3], ['Cem‘-i müennes muhâtaba', 'أَنْتُنَّ', 'Siz (kadınlar)', 2, 3],
  ['Nefs-i mütekellim vahdehû', 'أَنَا', 'Ben', 1, 1], ['Nefs-i mütekellim ma‘a’l-gayr', 'نَحْنُ', 'Biz', 1, 3]];
const ALL = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], HAZIR = [7,8,9,10,11,12];
const BAB = [null,
  { ad: 'Nasara', ar: 'نَصَرَ يَنْصُرُ', p: 'a', i: 'u' }, { ad: 'Daraba', ar: 'ضَرَبَ يَضْرِبُ', p: 'a', i: 'i' }, { ad: 'Fetaha', ar: 'فَتَحَ يَفْتَحُ', p: 'a', i: 'a' },
  { ad: 'Alime', ar: 'عَلِمَ يَعْلَمُ', p: 'i', i: 'a' }, { ad: 'Hasibe', ar: 'حَسِبَ يَحْسِبُ', p: 'i', i: 'i' }, { ad: 'Kerume', ar: 'كَرُمَ يَكْرُمُ', p: 'u', i: 'u' }];
/* model fiiller ve Türkçe karşılıkları (s: ma‘lûm kök, ps: meçhûl kök, aor: geniş zaman eki türü) */
const MODEL = {
  'نصر': { bab: 1, masdar: 'نَصْرًا', tr: { s: 'yardım et', ps: 'yardım edil', aor: 'A' }, mana: 'yardım etmek' },
  'ضرب': { bab: 2, masdar: 'ضَرْبًا', tr: { s: 'vur', ps: 'vurul', aor: 'I' }, mana: 'vurmak' },
  'فتح': { bab: 3, masdar: 'فَتْحًا', tr: { s: 'aç', ps: 'açıl', aor: 'A' }, mana: 'açmak' },
  'علم': { bab: 4, masdar: 'عِلْمًا', tr: { s: 'bil', ps: 'bilin', aor: 'I' }, mana: 'bilmek' },
  'حسب': { bab: 5, masdar: 'حِسْبَانًا', tr: { s: 'san', ps: 'sanıl', aor: 'I' }, mana: 'sanmak, zannetmek' },
  'كرم': { bab: 6, masdar: 'كَرَامَةً', tr: { s: 'kerîm ol', ps: null, aor: 'I' }, mana: 'kerîm (cömert, şerefli) olmak', lazim: true }
};
const MAZI = [null, F, F+'ا', D+'وا', F+'تْ', F+'تَا', S+'نَ', S+'تَ', S+'تُمَا', S+'تُمْ', S+'تِ', S+'تُمَا', S+'تُنَّ', S+'تُ', S+'نَا'];
const PRE = [null, 'ي','ي','ي','ت','ت','ي','ت','ت','ت','ت','ت','ت','أ','ن'];
const MERFU = [null, D, F+'انِ', D+'ونَ', D, F+'انِ', S+'نَ', D, F+'انِ', D+'ونَ', Ki+'ينَ', F+'انِ', S+'نَ', D, D];
const MANSUB = [null, F, F+'ا', D+'وا', F, F+'ا', S+'نَ', F, F+'ا', D+'وا', Ki+'ي', F+'ا', S+'نَ', F, F];
const MECZUM = [null, S, F+'ا', D+'وا', S, F+'ا', S+'نَ', S, F+'ا', D+'وا', Ki+'ي', F+'ا', S+'نَ', S, S];
const SAKILE = [null, F+'نَّ', F+'انِّ', D+'نَّ', F+'نَّ', F+'انِّ', S+'نَانِّ', F+'نَّ', F+'انِّ', D+'نَّ', Ki+'نَّ', F+'انِّ', S+'نَانِّ', F+'نَّ', F+'نَّ'];
const HAFIFE = { 1: F+'نْ', 3: D+'نْ', 4: F+'نْ', 7: F+'نْ', 9: D+'نْ', 10: Ki+'نْ', 13: F+'نْ', 14: F+'نْ' };
function join(stem, suf){ const last = stem.slice(-1); if(suf[0] === S && suf[1] === last && (last === 'ن' || last === 'ت')) return stem + SH + suf.slice(2); return stem + suf }

/* ---- Türkçe fiil çekimi (ünlü uyumu, ünsüz yumuşaması) ---- */
const TV = 'aeıioöuüâîû';
function lastV(s){ for(let i = s.length - 1; i >= 0; i--){ const c = s[i]; if(TV.includes(c)) return { 'â':'a', 'î':'i', 'û':'u' }[c] || c } return 'e' }
const I4 = v => ({ a:'ı', ı:'ı', e:'i', i:'i', o:'u', u:'u', ö:'ü', ü:'ü' }[v]);
const A2 = v => 'aıou'.includes(v) ? 'a' : 'e';
function tsuf(stem, tmpl){
  let cur = stem;
  for(const ch of tmpl){
    let add = ch;
    if(ch === 'I') add = I4(lastV(cur)); else if(ch === 'A') add = A2(lastV(cur));
    else if(ch === 'D') add = 'çfhkpsşt'.includes(cur.slice(-1)) ? 't' : 'd';
    if(TV.includes(add)){
      if(/(^|\s)et$/.test(cur)) cur = cur.slice(0, -1) + 'd';
      else if(/(cak|cek)$/.test(cur)) cur = cur.slice(0, -1) + 'ğ';
      if(TV.includes(cur.slice(-1)) && (ch === 'I' || ch === 'A')) cur += 'y';
    }
    cur += add;
  }
  return cur;
}
const PAST_P = { '1-1': 'm', '1-3': 'k', '2-1': 'n', '2-3': 'nIz', '3-1': '', '3-3': 'lAr' };
const PRES_P = { '1-1': 'Im', '1-3': 'Iz', '2-1': 'sIn', '2-3': 'sInIz', '3-1': '', '3-3': 'lAr' };
function aor(st, type){ return tsuf(st, (st.includes(' ') ? st.split(' ').pop() : st).length > 3 ? 'Ir' : type === 'I' ? 'Ir' : 'Ar') }
function trVerb(m, kind, si, pass){
  const st = pass ? m.ps : m.s; if(!st) return '';
  const [, , gl, per, num] = SIGA[si] || [], key = per + '-' + num;
  const neg = { '1-1': 'mAm', '1-3': 'mAyIz', '2-1': 'mAzsIn', '2-3': 'mAzsInIz', '3-1': 'mAz', '3-3': 'mAzlAr' };
  let v;
  switch(kind){
    case 'past': v = tsuf(st, 'DI' + PAST_P[key]); break;
    case 'pastNeg': v = tsuf(st, 'mAdI' + PAST_P[key]); break;
    case 'aor': v = tsuf(aor(pass ? m.ps : m.s, pass ? 'I' : m.aor), PRES_P[key].replace(/^I/, 'I')); break;
    case 'aorNeg': v = tsuf(st, neg[key]); break;
    case 'futNeg': v = 'asla ' + tsuf(st, 'mAyAcAk' + PRES_P[key]); break;
    case 'fut': v = 'mutlaka ' + tsuf(st, 'AcAk' + PRES_P[key]); break;
    case 'emrG': v = per === 1 ? tsuf(st, num === 1 ? 'AyIm' : 'AlIm') : per === 2 ? (num === 1 ? st : tsuf(st, 'In')) : tsuf(st, num === 1 ? 'sIn' : 'sInlAr'); break;
    case 'nehy': v = per === 1 ? tsuf(st, num === 1 ? 'mAyAyIm' : 'mAyAlIm') : per === 2 ? tsuf(st, num === 1 ? 'mA' : 'mAyIn') : tsuf(st, num === 1 ? 'mAsIn' : 'mAsInlAr'); break;
    case 'emr': v = num === 1 ? st : tsuf(st, 'In'); break;
    case 'emrT': v = 'mutlaka ' + (num === 1 ? st : tsuf(st, 'In')); break;
  }
  return `${gl} ${v}`;
}

/* ---- Emsile-i muttaride bölümleri ---- */
function emsile(root, bab, opt){
  opt = opt || {};
  const [a, b, c] = [...root], B = BAB[bab], pv = VV[B.p], iv = VV[B.i];
  const mz = a+F+b+pv+c, mzM = a+D+b+Ki+c, mu = a+S+b+iv+c, muM = a+S+b+F+c;
  const muz = (si, suf, pass, pre) => (pre || '') + PRE[si] + (pass ? D : F) + join(pass ? muM : mu, suf[si]);
  const hz = (B.i === 'u' ? 'اُ' : 'اِ') + a+S+b+iv+c;
  const EMR = [null, , , , , , , S, F+'ا', D+'وا', Ki+'ي', F+'ا', S+'نَ'];
  const EMR_SK = [null, , , , , , , F+'نَّ', F+'انِّ', D+'نَّ', Ki+'نَّ', F+'انِّ', S+'نَانِّ'];
  const zm = (B.i === 'i' ? 'مَ'+a+S+b+Ki+c : 'مَ'+a+S+b+F+c);
  const M = MODEL[root], lazim = M && M.lazim;
  const sec = [];
  const add = (key, tr, ar, kip, mood, sigas, fn, trk, pass) => { if(pass && lazim) return; sec.push({ key, tr, ar, kip, mood, rows: sigas.map(si => ({ si, f: fn(si), t: M ? trVerb(M.tr, trk, si, pass) : '' })) }) };
  add('mazi', 'Fiil-i mâzî müsbet ma‘lûm', 'الفعل الماضي المثبت المعلوم', 'mâzî', 'mebnî', ALL, si => join(mz, MAZI[si]), 'past');
  add('maziN', 'Fiil-i mâzî menfî ma‘lûm', 'الفعل الماضي المنفي المعلوم', 'mâzî menfî', 'mebnî', ALL, si => 'مَا ' + join(mz, MAZI[si]), 'pastNeg');
  add('maziM', 'Fiil-i mâzî müsbet meçhûl', 'الفعل الماضي المثبت المجهول', 'mâzî meçhûl', 'mebnî', ALL, si => join(mzM, MAZI[si]), 'past', true);
  add('maziMN', 'Fiil-i mâzî menfî meçhûl', 'الفعل الماضي المنفي المجهول', 'mâzî menfî meçhûl', 'mebnî', ALL, si => 'مَا ' + join(mzM, MAZI[si]), 'pastNeg', true);
  add('muz', 'Fiil-i muzâri‘ müsbet ma‘lûm', 'الفعل المضارع المثبت المعلوم', 'muzâri‘', 'merfû', ALL, si => muz(si, MERFU), 'aor');
  add('muzN', 'Fiil-i muzâri‘ menfî ma‘lûm', 'الفعل المضارع المنفي المعلوم', 'muzâri‘ menfî', 'merfû', ALL, si => muz(si, MERFU, false, 'لَا '), 'aorNeg');
  add('muzM', 'Fiil-i muzâri‘ müsbet meçhûl', 'الفعل المضارع المثبت المجهول', 'muzâri‘ meçhûl', 'merfû', ALL, si => muz(si, MERFU, true), 'aor', true);
  add('muzMN', 'Fiil-i muzâri‘ menfî meçhûl', 'الفعل المضارع المنفي المجهول', 'muzâri‘ menfî meçhûl', 'merfû', ALL, si => muz(si, MERFU, true, 'لَا '), 'aorNeg', true);
  add('lan', 'Nefy-i istikbâl bi-len (te’kîd-i nefy) ma‘lûm', 'نفي المستقبل بـ«لن» المعلوم', 'lenli muzâri‘', 'mansûb', ALL, si => muz(si, MANSUB, false, 'لَنْ '), 'futNeg');
  add('lanM', 'Nefy-i istikbâl bi-len meçhûl', 'نفي المستقبل بـ«لن» المجهول', 'lenli muzâri‘ meçhûl', 'mansûb', ALL, si => muz(si, MANSUB, true, 'لَنْ '), 'futNeg', true);
  add('lam', 'Cahd (nefy-i mâzî bi-lem) ma‘lûm', 'الجحد المطلق بـ«لم» المعلوم', 'cahd', 'meczûm', ALL, si => muz(si, MECZUM, false, 'لَمْ '), 'pastNeg');
  add('lamM', 'Cahd meçhûl', 'الجحد المطلق بـ«لم» المجهول', 'cahd meçhûl', 'meczûm', ALL, si => muz(si, MECZUM, true, 'لَمْ '), 'pastNeg', true);
  add('emrG', 'Emr-i gâib ve mütekellim ma‘lûm', 'الأمر الغائب والمتكلم المعلوم', 'emr-i gâib', 'meczûm', [1,2,3,4,5,6,13,14], si => muz(si, MECZUM, false, 'لِ'), 'emrG');
  add('emrGM', 'Emr-i meçhûl', 'الأمر المجهول', 'emr-i meçhûl', 'meczûm', ALL, si => muz(si, MECZUM, true, 'لِ'), 'emrG', true);
  add('nehy', 'Nehy ma‘lûm', 'النهي المعلوم', 'nehiy', 'meczûm', ALL, si => muz(si, MECZUM, false, 'لَا '), 'nehy');
  add('nehyM', 'Nehy meçhûl', 'النهي المجهول', 'nehiy meçhûl', 'meczûm', ALL, si => muz(si, MECZUM, true, 'لَا '), 'nehy', true);
  add('emr', 'Emr-i hâzır', 'الأمر الحاضر', 'emr-i hâzır', 'mebnî', HAZIR, si => join(hz, EMR[si]), 'emr');
  add('tekS', 'Muzâri‘ bi-nûni’t-te’kîdi’s-sakîle', 'المضارع المؤكد بالنون الثقيلة', 'nûn-ı tekîd-i sakîle', 'mebnî', ALL, si => 'لَ' + PRE[si] + F + mu + SAKILE[si], 'fut');
  add('tekH', 'Muzâri‘ bi-nûni’t-te’kîdi’l-hafîfe', 'المضارع المؤكد بالنون الخفيفة', 'nûn-ı tekîd-i hafîfe', 'mebnî', [1,3,4,7,9,10,13,14], si => 'لَ' + PRE[si] + F + mu + HAFIFE[si], 'fut');
  add('emrT', 'Emr-i hâzır bi-nûni’t-te’kîdi’s-sakîle', 'الأمر المؤكد بالنون الثقيلة', 'emr-i hâzır tekîdli', 'mebnî', HAZIR, si => hz + EMR_SK[si], 'emrT');
  // isimler
  const nf = M ? tsuf(M.tr.s, 'An') : '', nm = M && M.tr.ps ? tsuf(M.tr.ps, 'An') : '';
  const isim = (key, tr, ar, kip, forms, gl, note) => sec.push({ key, tr, ar, kip, isim: true, note, rows: forms.map((f, i) => ({ f, lbl: gl[i], t: '' })) });
  const G6 = ['Müfred müzekker', 'Tesniye müzekker', 'Cem‘-i müzekker sâlim', 'Müfred müennes', 'Tesniye müennes', 'Cem‘-i müennes sâlim'];
  const fa = a+F+'ا'+b+Ki+c, mf = 'مَ'+a+S+b+D+'و'+c;
  const six = st => [st+UN, st+F+'انِ', st+D+'ونَ', st+F+'ةٌ', st+F+'تَانِ', st+F+'اتٌ'];
  isim('fail', 'İsm-i fâil', 'اسم الفاعل', 'ism-i fâil', six(fa), G6, (bab === 4 || bab === 6 ? 'Bu bâbda vasıf çoğunlukla sıfat-ı müşebbehe ile gelir (كَرِيمٌ gibi). ' : '') + (nf ? `Mânâ: “${nf}”.` : ''));
  if(!lazim) isim('meful', 'İsm-i mef‘ûl', 'اسم المفعول', 'ism-i mef‘ûl', six(mf), G6, nm ? `Mânâ: “${nm}”.` : '');
  isim('zaman', 'İsm-i zaman ve mekân', 'اسم الزمان والمكان', 'ism-i zaman-mekân', [zm+UN, zm+F+'انِ', 'مَ'+a+F+'ا'+b+Ki+c+D], ['Müfred', 'Tesniye', 'Cem‘ (mekesser)'], `Kalıp: ${B.i === 'i' ? 'مَفْعِلٌ (muzâri‘de ayn’ül-fiil kesreli olduğu için)' : 'مَفْعَلٌ'}.` + (M ? ` Mânâ: “${tsuf(M.tr.s, 'mA')} yeri / zamanı”.` : ''));
  const al1 = 'مِ'+a+S+b+F+c, al3 = 'مِ'+a+S+b+F+'ا'+c;
  isim('alet', 'İsm-i âlet', 'اسم الآلة', 'ism-i âlet', [al1+UN, al1+F+'انِ', al1+F+'ةٌ', al1+F+'تَانِ', al3+UN, al3+F+'انِ', 'مَ'+a+F+'ا'+b+Ki+c+D, 'مَ'+a+F+'ا'+b+Ki+'ي'+c+D], ['مِفْعَلٌ — müfred', 'tesniye', 'مِفْعَلَةٌ — müfred', 'tesniye', 'مِفْعَالٌ — müfred', 'tesniye', 'Cem‘ (مَفَاعِلُ)', 'Cem‘ (مَفَاعِيلُ)'], M ? `Mânâ: “${tsuf(M.tr.s, 'mA')} âleti”.` : '');
  const tf = 'أَ'+a+S+b+F+c, tfF = a+D+b+S+c+F+'ى';
  isim('tafdil', 'İsm-i tafdîl', 'اسم التفضيل', 'ism-i tafdîl', [tf+D, tf+F+'انِ', tf+D+'ونَ', 'أَ'+a+F+'ا'+b+Ki+c+D, tfF, a+D+b+S+c+F+'يَانِ', a+D+b+S+c+F+'يَاتٌ', a+D+b+F+c+UN], ['Müfred müzekker', 'Tesniye müzekker', 'Cem‘-i müzekker sâlim', 'Cem‘-i mükesser', 'Müfred müennes', 'Tesniye müennes', 'Cem‘-i müennes sâlim', 'Cem‘-i mükesser'], M ? `Mânâ: “en çok ${nf}”.` : '');
  isim('teaccub', 'Fiil-i teaccüb', 'فعلا التعجب', 'fiil-i teaccüb', ['مَا أَ'+a+S+b+F+c+F+'هُ', 'أَ'+a+S+b+Ki+c+S+' بِهِ'], ['مَا أَفْعَلَهُ', 'أَفْعِلْ بِهِ'], M ? `Mânâ: “Ne kadar çok ${tsuf(M.tr.s, 'DI')}!” — hayret bildirir.` : '');
  return sec;
}
/* Emsile-i muhtelife: bölümlerin ilk sîgalarından tek satır */
function muhtelife(root, bab, sec){
  const g = k => { const s = sec.find(x => x.key === k); return s ? s.rows[0].f : null };
  const M = MODEL[root], masdar = M ? M.masdar : '';
  const seq = [['mazi', 'mâzî'], ['muz', 'muzâri‘'], masdar && ['_m', 'masdar', masdar], ['fail', 'ism-i fâil', 'فَهُوَ ' + g('fail')], ['meful', 'ism-i mef‘ûl', g('meful') && 'وَذَاكَ ' + g('meful')],
    ['lam', 'cahd'], ['lamM', 'cahd meçhûl'], ['muzN', 'muzâri‘ menfî'], ['muzMN', 'muzâri‘ menfî meçhûl'], ['maziN', 'mâzî menfî'], ['maziMN', 'mâzî menfî meçhûl'],
    ['lan', 'nefy-i istikbâl'], ['lanM', 'nefy-i istikbâl meçhûl'], ['emr', 'emr-i hâzır'], ['emrGM', 'emr-i meçhûl'], ['nehy', 'nehiy'], ['nehyM', 'nehiy meçhûl'],
    ['zaman', 'ism-i zaman-mekân'], ['alet', 'ism-i âlet'], ['tafdil', 'ism-i tafdîl'], ['teaccub', 'fiil-i teaccüb']].filter(Boolean);
  return seq.map(([k, ad, ov]) => { let f = ov || g(k); if(k === 'nehy' && f){ const s = sec.find(x => x.key === 'nehy'); f = s.rows.find(r => r.si === 7).f } if(k === 'emrGM' && f){ const s = sec.find(x => x.key === 'emrGM'); f = s.rows.find(r => r.si === 1).f } return f ? { k, ad, f } : null }).filter(Boolean);
}

/* ======================================================================
   ARALIKLI TEKRAR (SM-2 benzeri) — LS 'medrese.srs'
   ====================================================================== */
const SRS = {
  all(){ return LS.get('medrese.srs', {}) },
  save(o){ LS.set('medrese.srs', o) },
  grade(id, ok, tag){
    const o = SRS.all(), r = o[id] || { n: 0, ef: 2.5, iv: 0, due: today(), ok: 0, bad: 0, tag };
    r.tag = tag; r.last = ok ? 1 : 0; r.seen = today();
    if(ok){ r.ok++; r.n++; r.iv = r.n === 1 ? 1 : r.n === 2 ? 3 : Math.round(r.iv * r.ef); r.ef = Math.min(2.8, r.ef + 0.1) }
    else { r.bad++; r.n = 0; r.iv = 0; r.ef = Math.max(1.3, r.ef - 0.2) }
    r.due = today() + r.iv; o[id] = r; SRS.save(o);
  },
  due(){ const o = SRS.all(), t = today(); return Object.keys(o).filter(k => o[k].due <= t) },
  wrong(){ const o = SRS.all(); return Object.keys(o).filter(k => o[k].last === 0) }
};

/* ======================================================================
   SORU ÜRETİMİ — kimlikten yeniden kurulur: tip|kök|bâb|bölüm|sîga
   ====================================================================== */
const HV = { a: 'fethalı', i: 'kesreli', u: 'dammeli' };
const TAGS = { siga: 'Sîga tespiti', kip: 'Kip ve zaman', cekim: 'Çekim (doğru kalıbı bulma)', bab: 'Bâb tespiti', turkce: 'Mânâ (Türkçesi)' };
const MODEL_ROOTS = Object.keys(MODEL);
function secOf(root, bab, key){ return emsile(root, bab).find(s => s.key === key) }
function makeQ(id){
  const [tip, root, bab0, key, si0] = id.split('|'), bab = +bab0, si = +si0;
  if(tip === 'kitap' || tip === 'yds' || tip === 'mo' || tip === 'mk') return extQ(id);
  if(tip === 'bab'){
    const sec = emsile(root, bab), f = sec[0].rows[0].f + '  ' + sec.find(s => s.key === 'muz').rows[0].f;
    return { id, tag: 'bab', soru: 'Bu fiil hangi bâbdandır?', kelime: f, secenek: [1,2,3,4,5,6].map(n => ({ v: n, t: `${BAB[n].ad} <span lang="ar">${BAB[n].ar}</span>` })), dogru: bab,
      aciklama: `Mâzîde ayn’ül-fiil ${HV[BAB[bab].p]}, muzâride ${HV[BAB[bab].i]}: ${BAB[bab].ad} bâbı (${BAB[bab].ar}).` };
  }
  const S = secOf(root, bab, key); if(!S) return null;
  const row = S.rows.find(r => r.si === si) || S.rows[0];
  if(tip === 'siga'){
    const opts = shuffle([si, ...shuffle(S.rows.map(r => r.si).filter(x => x !== si && S.rows.find(r => r.si === x).f !== row.f)).slice(0, 3)]);
    return { id, tag: 'siga', soru: 'Bu kelimenin sîgası hangisidir?', kelime: row.f, alt: S.tr, secenek: opts.map(x => ({ v: x, t: `${SIGA[x][0]} <span lang="ar">(${SIGA[x][1]})</span>` })), dogru: si,
      aciklama: `${row.f}: ${S.tr}, ${SIGA[si][0]} (${SIGA[si][1]}).` + (row.t ? ` Türkçesi: “${row.t}”.` : '') + (S.rows.filter(r => r.f === row.f).length > 1 ? ' Not: Bu kalıp başka bir sîgayla aynı yazılır; bağlamdan ayırt edilir.' : '') };
  }
  if(tip === 'kip'){
    const all = emsile(root, bab).filter(s => !s.isim), others = shuffle(all.filter(s => s.key !== key && !s.rows.some(r => r.f === row.f))).slice(0, 3);
    const opts = shuffle([S, ...others]);
    return { id, tag: 'kip', soru: 'Bu kelime hangi kiptir?', kelime: row.f, secenek: opts.map(s => ({ v: s.key, t: `${s.tr} <span lang="ar">${s.ar}</span>` })), dogru: key,
      aciklama: `${row.f}: ${S.tr} (${S.ar}), ${SIGA[si][0]}. İ‘râb/binâ: ${S.mood}.` };
  }
  if(tip === 'cekim'){
    const opts = shuffle([row, ...shuffle(S.rows.filter(r => r.f !== row.f)).slice(0, 3)]);
    return { id, tag: 'cekim', soru: `${secOf(root, bab, 'mazi').rows[0].f} fiilinin <b>${S.tr}</b> kipinde <b>${SIGA[si][0]}</b> (${SIGA[si][1]}) sîgası hangisidir?`, secenek: opts.map(r => ({ v: r.f, t: `<span lang="ar" class="ar2">${r.f}</span>` })), dogru: row.f,
      aciklama: `Doğrusu ${row.f}.` + (row.t ? ` “${row.t}”.` : '') };
  }
  if(tip === 'turkce' && row.t){
    const opts = shuffle([row, ...shuffle(S.rows.filter(r => r.t && r.t !== row.t)).slice(0, 3)]);
    return { id, tag: 'turkce', soru: 'Bu kelimenin Türkçesi hangisidir?', kelime: row.f, secenek: opts.map(r => ({ v: r.t, t: esc(r.t) })), dogru: row.t, aciklama: `${row.f}: “${row.t}” (${S.tr}).` };
  }
  return null;
}
function newIds(n, scope){
  const ids = [], keys = ['mazi','muz','maziM','muzM','lan','lam','emr','nehy','emrG','tekS','maziN','muzN'];
  for(let k = 0; k < n * 3 && ids.length < n; k++){
    const root = scope && scope.root || pick(MODEL_ROOTS), bab = scope && scope.bab || MODEL[root].bab;
    const key = scope && scope.key || pick(keys), S = secOf(root, bab, key); if(!S) continue;
    const si = pick(S.rows).si, tip = pick(['siga', 'siga', 'kip', 'cekim', 'turkce']);
    const id = [tip, root, bab, key, si].join('|');
    if(!ids.includes(id) && makeQ(id)) ids.push(id);
  }
  return ids;
}

/* ======================================================================
   ARAYÜZ
   ====================================================================== */
const V = $('#v');
const bar = (title, back) => `<div class="mh"><button class="ib" onclick="${back ? `go('${back}')` : `location.href='index.html'`}" aria-label="Geri">‹</button><b>${title}</b><span class="sp"></span><a class="chip" href="#/tekrar" title="Bugünün tekrarı">Tekrar <i>${SRS.due().length}</i></a></div>`;
function go(h){ location.hash = h }
function hataEkrani(e){ try{ console.warn(e) }catch(x){} try{ V.innerHTML = bar('Bir sorun oluştu', '/') + '<div class="wrap"><div class="empty"><p><b>Bu sayfa açılırken bir sorun oluştu.</b></p><p class="lead">İlerlemeniz kayıtlı, kaybolmadı. Sayfayı yenileyin ya da ana sayfaya dönün.</p><p><button class="btn pri" id="hyen">Yenile</button> <a class="btn" href="#/">Ana sayfa</a></p></div></div>'; const y = $('#hyen'); if(y) y.onclick = () => location.reload() }catch(x){} }
function guvenliRoute(){ try{ const r = route(); if(r && typeof r.catch === 'function') r.catch(hataEkrani) }catch(e){ hataEkrani(e) } }
addEventListener('hashchange', guvenliRoute);
addEventListener('unhandledrejection', e => { try{ e.preventDefault(); console.warn(e.reason) }catch(x){} });
/* ---- ders videosu (mini oynatıcı) ---- */
const KLASIK = ['emsile', 'bina', 'maksud', 'izzi', 'avamil', 'birgivi', 'izhar', 'zuruf', 'kavaid', 'ajurrumiyye', 'katr', 'serhkatr'];
let VDATA = null, VP = { key: null, open: false, big: false };
const VIDKEY = h => { if(h[0] === 'emsile') return 'emsile'; if((h[0] === 'kitap' || h[0] === 'oku') && KLASIK.includes(h[1])) return h[1]; return null };
const DERS_LISTE = { izhar: 'PLUFT_YZ2pHv71kszU0PdBBsNcE9HrTj7P', zuruf: 'PLUFT_YZ2pHv6OSE_5zcdx0q4iDIdrEExP', birgivi: 'PLUFT_YZ2pHv7tvTbDhX8Nzs4jf72z-XaB', emsile: 'PLUFT_YZ2pHv5pjh2ZMt7BJ-1beuXGKOth', bina: 'PLUFT_YZ2pHv51Rn2jzRzJ1iPMrRcyUl9C', maksud: 'PLUFT_YZ2pHv7TVNi9bD9yrYVqTpBLqkbw', izzi: 'PLUFT_YZ2pHv6MpTMupA0fxtPL0XY8Slgs', avamil: 'PLUFT_YZ2pHv5jiqfMYytJAcKkgSFx_CH5', katr: 'PLUFT_YZ2pHv7MZgzym0gi8qazfVeaEBHA', serhkatr: 'PLUFT_YZ2pHv7MZgzym0gi8qazfVeaEBHA' };
async function vidListe(k){ if(DERS_LISTE[k]) return { liste: DERS_LISTE[k] }; try{ VDATA = VDATA || await fetch('data/videolar.json', { cache: 'no-cache' }).then(r => r.json()) }catch(e){ VDATA = {} } const d = (VDATA.dersler || {})[k]; return d && (d.liste || d.video) ? d : null }
function vidKur(h){
  const k = VIDKEY(h); let btn = $('#vpBtn'), box = $('#vp');
  if(!btn){ document.body.insertAdjacentHTML('beforeend', `<button id="vpBtn" aria-label="Ders videosu"><span>▶</span> Ders</button><div id="vp" class="hide"><div class="vph"><b>Ders videosu</b><button data-a="buyut" aria-label="Büyüt/küçült">⤢</button><button data-a="kapat" aria-label="Kapat">✕</button></div><div class="vpb"></div></div>`); btn = $('#vpBtn'); box = $('#vp');
    btn.onclick = () => VP.open ? vidKapat() : vidAc();
    box.querySelector('[data-a=kapat]').onclick = vidKapat;
    box.querySelector('[data-a=buyut]').onclick = () => { VP.big = !VP.big; box.classList.toggle('big', VP.big) }; }
  if(!k) document.body.classList.remove('vpVar');
  if(!k){ btn.classList.add('hide'); vidKapat(); VP.key = null; return }
  if(VP.key !== k){ vidKapat(); VP.key = k; btn.classList.add('hide'); document.body.classList.remove('vpVar'); vidListe(k).then(d => { if(VP.key === k && d){ btn.classList.remove('hide'); document.body.classList.add('vpVar') } }) }
  else if(!btn.dataset.yok) { vidListe(k).then(d => { if(d){ btn.classList.remove('hide'); document.body.classList.add('vpVar') } }) }
}
async function vidAc(){
  const box = $('#vp'), b = box.querySelector('.vpb'), d = await vidListe(VP.key);
  VP.open = true; $('#vpBtn').classList.add('on'); $('#vpBtn').innerHTML = '<span>■</span> Kapat'; box.classList.remove('hide');
  const src = d ? (d.liste ? `https://www.youtube-nocookie.com/embed/videoseries?list=${encodeURIComponent(d.liste)}&rel=0&playsinline=1&origin=${encodeURIComponent(location.origin)}` : `https://www.youtube-nocookie.com/embed/${encodeURIComponent(d.video)}?rel=0&playsinline=1&origin=${encodeURIComponent(location.origin)}`) : '';
  b.innerHTML = src ? `<iframe src="${src}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin" title="Ders videosu"></iframe>` : '<p class="vpe">Bu dersin video listesi yakında eklenecek.</p>';
}
function vidKapat(){ const box = $('#vp'); if(!box) return; VP.open = false; box.classList.add('hide'); box.querySelector('.vpb').innerHTML = ''; const b = $('#vpBtn'); b.classList.remove('on'); b.innerHTML = '<span>▶</span> Ders' }

function route(){
  sesDur();
  if(window.Kelime) Kelime.close(); const sh = $('#sh'); if(sh) sh.classList.add('hide');
  const h = (location.hash || '#/').slice(2).split('/').map(decodeURIComponent);
  scrollTo(0, 0);
  const [p0, p1, p2, p3, p4] = h;
  vidKur(h);
  if(!p0) return home();
  if(p0 === 'kitap') return kitap(p1);
  if(p0 === 'emsile') return p1 === 'alistirma' ? alistirma({ scope: 'emsile' }) : emsileOku();
  if(p0 === 'tekrar') return YUK.then(() => alistirma({ scope: 'tekrar' }));
  if(p0 === 'yanlislar') return YUK.then(yanlislar);
  if(p0 === 'rapor') return YUK.then(rapor);
  if(p0 === 'oyun' && p1 === 'vezin') return vezinOyunu();
  if(p0 === 'oyun') return babOyunu(p1 === 'hizli');
  if(p0 === 'yol') return yolSayfa(p1);
  if(p0 === 'oyunlar') return oyunlar();
  if(p0 === 'oku') return p2 === 'alistirma' ? kitapAlistirma(p1) : kitapOku(p1, p2);
  if(p0 === 'yds') return yds(p1, p2);
  if(p0 === 'modern') return modern(p1, p2);
  if(p0 === 'gunluk') return gunluk();
  if(p0 === 'irab') return irabOyunu();
  if(p0 === 'harita') return harita();
  if(p0 === 'kuran') return p1 ? kuranSure(+p1, +p2 || 0, p3 ? +p3 : null) : kuranListe();
  home();
}

/* ---- ana ekran ---- */
function home(){
  const due = SRS.due().length, wr = SRS.wrong().length;
  V.innerHTML = bar('Medrese') + `<div class="wrap">
   <div class="hero"><div class="hero-ar" lang="ar">المَدْرَسَة</div><p>Medrese usûlüyle sarf ve nahiv: <b>oku, anla, unutma.</b></p>
    <div class="hero-b"><a class="btn pri" href="#/tekrar">Bugünün tekrarı <i>${due}</i></a><a class="btn" href="#/yanlislar">Yanlışlarım <i>${wr}</i></a><a class="btn" href="#/rapor">Zayıf konularım</a><a class="btn" href="#/harita">Öğrenme haritam</a></div></div>
   <div class="boxes">
    <a class="bigbox b-sarf" href="#/yol/sarf"><span lang="ar">الصَّرْف</span><b>Sarf</b><small>Emsile · Binâ · Maksûd · İzzî</small></a>
    <a class="bigbox b-nahiv" href="#/yol/nahiv"><span lang="ar">النَّحْو</span><b>Nahiv</b><small>Avâmil · Âcurrûmiyye · Katru’n-nedâ</small></a>
    <a class="bigbox b-kuran" href="#/kitap/kuran"><span lang="ar">إِعْرَابُ الْقُرْآنِ</span><b>Kur’an i‘râbı</b><small>Her kelimeye dokun: sarf ve nahiv</small></a>
    <a class="bigbox b-yds" href="#/yds"><span lang="ar">اِخْتِبَار</span><b>YDS Arapça</b><small>Deneme · okuma metinleri · kelime</small></a>
    <a class="bigbox b-mod" href="arapca.html?medrese=1"><span lang="ar">المُعَاصِرَة</span><b>Modern Arapça</b><small>Sesli Arapça dersleri · hikâyeler</small></a>
    <a class="bigbox b-oyun" href="#/oyunlar"><span lang="ar">أَلْعَاب</span><b>Oyunlar</b><small>Günün sorusu · İ‘râb · Bâb bul</small></a>
   </div>
   <p class="foot">Hata görürseniz her ekrandaki <i>Hata bildir</i> bağlantısını kullanın.<br><a href="#" onclick="$('#src').classList.remove('hide');return false">Kaynaklar ve lisans</a></p></div>`;
}
function yolSayfa(y){
  const rozet = LS.get('medrese.rozet', {}), B = BOOKS.filter(b => b.yol === y).sort((a, b) => a.sira - b.sira);
  V.innerHTML = bar(YOL[y] ? YOL[y][0] : 'Medrese', '/') + `<div class="wrap"><div class="hero"><div class="hero-ar" lang="ar">${YOL[y][1]}</div><p>Kitaplar medresedeki okunuş sırasıyla.</p></div>
   <div class="ylist">${B.map((b, i) => `<a class="yk" href="#/kitap/${b.id}"><i>${i + 1}</i><span lang="ar">${b.ar}</span><b>${b.ad}</b><small>${rozet[b.id] ? '✦ bitirildi' : b.durum === 'hazir' ? 'açık' : 'yakında'}</small></a>`).join('')}</div></div>`;
}
function oyunlar(){
  V.innerHTML = bar('Oyunlar', '/') + `<div class="wrap"><div class="games">
   <button onclick="go('/gunluk')"><b>Günün sorusu</b><span>☀</span><small>Herkes aynı soruyu çözer</small></button>
   <button onclick="go('/irab')"><b>İ‘râb oyunu</b><span lang="ar">رفع؟ نصب؟</span><small>Kur’an âyetleriyle</small></button>
   <button onclick="go('/oyun')"><b>Bâb bul</b><span lang="ar">نَصَرَ؟ ضَرَبَ؟</span><small>Kur’an fiillerinden</small></button>
   <button onclick="go('/oyun/vezin')"><b>Vezin bul</b><span lang="ar">فَاعِل؟ مَفْعُول؟</span><small>En iyi: ${LS.get('medrese.vezinBest', 0)}/10</small></button>
   <button onclick="go('/oyun/hizli')"><b>Hızlı tur</b><span>60 saniye</span><small>En iyi: ${LS.get('medrese.babBest', 0)}</small></button></div></div>`;
}
/* ---- Vezin bul oyunu ---- */
const VEZIN = 'كاتِب فاعِل|شاكِر فاعِل|مَكْتُوب مَفْعُول|مَنْصُور مَفْعُول|رَحِيم فَعِيل|عَلِيم فَعِيل|غَفّار فَعّال|صَبّار فَعّال|مِفْتاح مِفْعال|مِحْراب مِفْعال|مَسْجِد مَفْعِل|مَنْزِل مَفْعِل|مَذْهَب مَفْعَل|مَكْتَب مَفْعَل|مِنْبَر مِفْعَل|أَكْبَر أَفْعَل|أَعْلَم أَفْعَل|كُبْرَى فُعْلَى|حُسْنَى فُعْلَى|رَحْمان فَعْلان|عَطْشان فَعْلان|إِسْلام إِفْعال|إِكْرام إِفْعال|تَعْلِيم تَفْعِيل|تَسْبِيح تَفْعِيل|مُجاهَدَة مُفاعَلَة|مُشاوَرَة مُفاعَلَة|اِنْقِلاب اِنْفِعال|اِنْكِسار اِنْفِعال|اِجْتِماع اِفْتِعال|اِخْتِلاف اِفْتِعال|تَكَبُّر تَفَعُّل|تَعَلُّم تَفَعُّل|تَعاوُن تَفاعُل|تَباعُد تَفاعُل|اِسْتِغْفار اِسْتِفْعال|اِسْتِخْراج اِسْتِفْعال|مُؤْمِن مُفْعِل|مُرْسِل مُفْعِل|مُعَلِّم مُفَعِّل|مُسَبِّح مُفَعِّل|مُسْتَغْفِر مُسْتَفْعِل|مُسْتَخْرِج مُسْتَفْعِل|مُجْتَهِد مُفْتَعِل|مُخْتَلِف مُفْتَعِل|كِتابَة فِعالَة|تِجارَة فِعالَة|مَساجِد مَفاعِل|مَنازِل مَفاعِل|عُلَماء فُعَلاء|شُعَراء فُعَلاء|مُكْرَم مُفْعَل|مُنْزَل مُفْعَل|مُكَرَّم مُفَعَّل|مُعَلَّم مُفَعَّل|مُقاتِل مُفاعِل|مُجاهِد مُفاعِل|مُتَكَلِّم مُتَفَعِّل|مُتَعَلِّم مُتَفَعِّل'.split('|').map(s => s.split(' '));
function vezinOyunu(){
  const tum = [...new Set(VEZIN.map(x => x[1]))];
  const sorular = shuffle(VEZIN).slice(0, 10); let i = 0, dogru = 0;
  const ciz = () => {
    if(i >= sorular.length){ const best = Math.max(LS.get('medrese.vezinBest', 0), dogru); LS.set('medrese.vezinBest', best);
      V.innerHTML = bar('Vezin bul', '/oyunlar') + `<div class="wrap" style="text-align:center"><h1>${dogru} / ${sorular.length}</h1><p class="lead">En iyi skorun: ${best}/10</p><p><button class="btn pri big" onclick="go('/oyun/vezin');route()">Yeniden oyna</button> <a class="btn big" href="#/oyunlar">Oyunlar</a></p></div>`; return }
    const [k, v] = sorular[i]; const sec = shuffle([v, ...shuffle(tum.filter(x => x !== v)).slice(0, 3)]);
    V.innerHTML = bar('Vezin bul', '/oyunlar') + `<div class="wrap" style="text-align:center"><p class="lead">${i + 1} / ${sorular.length} · Doğru: ${dogru}</p><p class="lead">Bu kelime hangi vezindedir?</p><div lang="ar" style="font-size:52px;margin:18px 0">${k}</div><div class="vzs" style="display:grid;grid-template-columns:1fr 1fr;gap:10px">${sec.map(s => `<button class="btn big" lang="ar" style="font-size:26px" data-s="${s}">${s}</button>`).join('')}</div><p id="vzm" class="lead" style="min-height:2em"></p></div>`;
    V.querySelectorAll('[data-s]').forEach(b => b.onclick = () => { const ok = b.dataset.s === v; if(ok) dogru++;
      V.querySelectorAll('[data-s]').forEach(x => { x.disabled = true; if(x.dataset.s === v) x.classList.add('pri') });
      V.querySelector('#vzm').innerHTML = ok ? '✓ Doğru' : `✗ Doğrusu: <span lang="ar">${v}</span>`;
      setTimeout(() => { i++; ciz() }, ok ? 700 : 1500) });
  };
  ciz();
}
/* ---- kitap tanıtım ekranı ---- */
function kitap(id){
  const b = BOOKS.find(x => x.id === id); if(!b) return home();
  const T = b.tanitim, hedef = b.durum !== 'hazir' ? null : id === 'emsile' ? '/emsile' : id === 'kuran' ? '/kuran' : id === 'yds' ? '/yds' : id === 'modern' ? '/modern' : '/oku/' + id;
  const seen = LS.get('medrese.tanitim', {});
  V.innerHTML = bar(b.ad, ['sarf','nahiv'].includes(b.yol) ? '/yol/' + b.yol : '/') + `<div class="wrap"><div class="intro"><div class="intro-ar" lang="ar">${b.ar}</div><h1>${b.ad}</h1><div class="yolt">${YOL[b.yol][0]}</div>
    <dl><dt>Müellif ve dönem</dt><dd>${T.muellif}</dd><dt>Bu kitaptan maksat</dt><dd>${T.amac}</dd><dt>Nasıl çalışılır</dt><dd>${T.yontem}</dd></dl>
    ${hedef ? `<a class="btn pri big" href="#${hedef}">${seen[id] ? 'Devam et' : 'Başla'} ›</a>${id === 'emsile' ? ' <a class="btn big" href="#/emsile/alistirma">Alıştırma</a>' : KITAPLAR.includes(id) ? ` <a class="btn big" href="#/oku/${id}/alistirma">Alıştırma</a>` : ''}` : '<p class="soon">Bu kitap hazırlanıyor. Matn, Türkçe açıklama ve alıştırmalar Emsile ile aynı kalıpta eklenecek.</p>'}</div></div>`;
  seen[id] = 1; LS.set('medrese.tanitim', seen);
}

/* ---- Emsile okuma ---- */
let EM = LS.get('medrese.emsile', { root: 'نصر', bab: 1, tr: true, gizle: '' });
function emsileOku(){
  const { root, bab } = EM, sec = emsile(root, bab), mh = muhtelife(root, bab, sec), M = MODEL[root];
  const okundu = LS.get('medrese.okundu', {});
  const opts = MODEL_ROOTS.map(r => `<button class="${r === root ? 'on' : ''}" data-root="${r}"><span lang="ar">${emsile(r, MODEL[r].bab)[0].rows[0].f}</span><small>${BAB[MODEL[r].bab].ad}</small></button>`).join('');
  const row = (s, r, i) => `<div class="er" data-s="${s.key}" data-i="${i}"><div class="ef" lang="ar">${r.f}</div><div class="el">${r.lbl || SIGA[r.si][0] + ' <span lang="ar">' + SIGA[r.si][1] + '</span>'}</div>${EM.tr && r.t ? `<div class="et">${esc(r.t)}</div>` : ''}</div>`;
  V.innerHTML = bar('Emsile', '/kitap/emsile') + `<div class="wrap">
   <div class="roots">${opts}<button data-root="_" class="${M ? '' : 'on'}"><span>+</span><small>Başka kök</small></button></div>
   ${M ? `<p class="mana">${BAB[bab].ad} bâbı · <span lang="ar">${BAB[bab].ar}</span> · Mânâ: <b>${M.mana}</b></p>` : `<p class="mana">Kök <b lang="ar">${[...root].join(' ')}</b> · ${BAB[bab].ad} bâbı. Türkçe satırlar yalnızca model fiillerde gösterilir.</p>`}
   <div class="tools"><label><input type="checkbox" id="trT" ${EM.tr ? 'checked' : ''}> Türkçesi (satır altı)</label>
     <span class="seg"><button data-g="" class="${!EM.gizle ? 'on' : ''}">Oku</button><button data-g="ar" class="${EM.gizle === 'ar' ? 'on' : ''}">Arapçayı gizle</button><button data-g="tr" class="${EM.gizle === 'tr' ? 'on' : ''}">Türkçeyi gizle</button></span>
     ${'speechSynthesis' in window ? '<button class="btn sm" id="sesli">▶ Sesli oku (muhtelife)</button>' : ''}</div>
   <section class="emh"><h2>Emsile-i muhtelife <span lang="ar">الأمثلة المختلفة</span></h2>
    <div class="mtl ${EM.gizle ? 'gz-' + EM.gizle : ''}">${mh.map((x, i) => `<span class="mw" data-mi="${i}"><b lang="ar">${x.f}</b><i>${x.ad}</i></span>`).join('')}</div>
    </section>
   <h2>Emsile-i muttaride <span lang="ar">الأمثلة المطّردة</span></h2>
   <div class="toc">${sec.map(s => `<a href="#" data-to="${s.key}" class="${okundu[root + s.key] ? 'done' : ''}">${s.tr}</a>`).join('')}</div>
   ${sec.map(s => `<section class="sec ${EM.gizle ? 'gz-' + EM.gizle : ''}" id="s-${s.key}"><h3>${s.tr}<span lang="ar">${s.ar}</span></h3>
     ${s.note ? `<p class="snote">${s.note}</p>` : ''}<div class="rows">${s.rows.map((r, i) => row(s, r, i)).join('')}</div>
     <div class="sf"><button class="btn sm ${okundu[root + s.key] ? 'on' : ''}" data-oku="${s.key}">${okundu[root + s.key] ? '✓ Okundu' : 'Okudum'}</button> <a class="btn sm" href="#" data-ex="${s.key}">Bu bölümden alıştırma</a> <a class="lnk" target="_blank" rel="noopener" href="${bugLink('emsile ' + root + ' ' + s.key, s.tr)}">Hata bildir</a></div></section>`).join('')}
   <div class="end"><a class="btn pri big" href="#/emsile/alistirma">Karışık alıştırma ›</a></div></div>`;
  $$('[data-root]').forEach(b => b.onclick = () => { if(b.dataset.root === '_') return kokSor(); EM.root = b.dataset.root; EM.bab = MODEL[EM.root].bab; LS.set('medrese.emsile', EM); emsileOku() });
  $('#trT').onchange = e => { EM.tr = e.target.checked; LS.set('medrese.emsile', EM); emsileOku() };
  $$('[data-g]').forEach(b => b.onclick = () => { EM.gizle = b.dataset.g; LS.set('medrese.emsile', EM); emsileOku() });
  $$('[data-to]').forEach(a => a.onclick = e => { e.preventDefault(); $('#s-' + a.dataset.to).scrollIntoView({ behavior: 'smooth' }) });
  $$('[data-oku]').forEach(b => b.onclick = () => { const o = LS.get('medrese.okundu', {}), k = root + b.dataset.oku; if(o[k]) delete o[k]; else o[k] = 1; LS.set('medrese.okundu', o); b.classList.toggle('on'); b.textContent = o[k] ? '✓ Okundu' : 'Okudum'; rozetKontrol() });
  $$('[data-ex]').forEach(a => a.onclick = e => { e.preventDefault(); alistirma({ scope: 'emsile', root, bab, key: a.dataset.ex }) });
  $$('.er').forEach(el => el.onclick = () => { if(EM.gizle){ el.classList.toggle('show'); return } const s = sec.find(x => x.key === el.dataset.s); formKart(root, bab, s, s.rows[+el.dataset.i]) });
  $$('.mw').forEach(el => el.onclick = () => { if(EM.gizle){ el.classList.toggle('show'); return } const x = mh[+el.dataset.mi], s = sec.find(y => y.key === x.k); if(s) formKart(root, bab, s, s.rows.find(r => r.f === x.f.replace(/^(فَهُوَ|وَذَاكَ) /, '')) || s.rows[0]) });
  const sb = $('#sesli'); if(sb) sb.onclick = () => seslendir(mh.map(x => x.f).join('، '), sb);
}
const SES = { btn: null, lbl: '' };
function sesDur(){ try{ speechSynthesis.cancel() }catch(e){} if(SES.btn){ SES.btn.innerHTML = SES.lbl; SES.btn.classList.remove('caliyor') } SES.btn = null }
function seslendir(t, btn){
  if(!('speechSynthesis' in window)){ toast('Sesli okuma desteklenmiyor'); return }
  if(btn && SES.btn === btn){ sesDur(); return }
  sesDur();
  const v = speechSynthesis.getVoices().find(v => v.lang && v.lang.startsWith('ar')); if(!v) toast('Cihazınızda Arapça ses bulunamadı');
  const parca = []; String(t).split(/(?<=[.؟!،؛:])\s+|\n+/).forEach(s => { s = s.trim(); if(!s) return; while(s.length > 220){ let k = s.lastIndexOf(' ', 220); if(k < 80) k = 220; parca.push(s.slice(0, k)); s = s.slice(k).trim() } if(s) parca.push(s) });
  if(btn){ SES.btn = btn; SES.lbl = btn.innerHTML; btn.innerHTML = '■ Durdur'; btn.classList.add('caliyor') }
  parca.forEach((s, i) => { const u = new SpeechSynthesisUtterance(s); u.lang = 'ar-SA'; u.rate = 0.85; if(v) u.voice = v; if(i === parca.length - 1) u.onend = () => { if(SES.btn === btn) sesDur() }; speechSynthesis.speak(u) });
}
function kokSor(){
  const r = prompt('Sâlim (harf-i illet, hemze ve tekrarlı harf içermeyen) üç harfli bir kök yazın, örn: كتب', 'كتب'); if(!r) return;
  const k = r.replace(/[^ء-ي]/g, ''); if(k.length !== 3 || /[وياأإآءؤئى]/.test(k) || k[1] === k[2]) return toast('Şimdilik yalnızca sâlim üç harfli kökler çekilebiliyor');
  const b = +prompt('Bâb numarası (1 Nasara · 2 Daraba · 3 Fetaha · 4 Alime · 5 Hasibe · 6 Kerume)', String(BABS[k] ? BABS[k][0] : 1)); if(!(b >= 1 && b <= 6)) return;
  EM.root = k; EM.bab = b; LS.set('medrese.emsile', EM); emsileOku();
  if(BABS[k] && BABS[k][0] !== b) toast(`Not: Kur’an’da bu kök ${BAB[BABS[k][0]].ad} bâbından geçiyor`);
}

/* ---- Emsile kelime kartı ---- */
function formKart(root, bab, s, r){
  const M = MODEL[root], mood = s.isim ? '' : (s.mood === 'merfû' && (r.si === 6 || r.si === 12)) ? 'mebnî ale’s-sükûn (nûn-ı nisve)' : s.mood === 'merfû' && [2,3,5,8,9,10,11].includes(r.si) ? 'merfû — alâmeti nûnun sübûtu (ef‘âl-i hamse)' : (s.mood === 'mansûb' || s.mood === 'meczûm') && [2,3,5,8,9,10,11].includes(r.si) ? `${s.mood} — alâmeti nûnun hazfı (ef‘âl-i hamse)` : s.key.startsWith('tek') || s.key === 'emrT' ? 'mebnî ale’l-feth (nûn-ı tekîd)' : s.mood === 'mebnî' && s.key.startsWith('mazi') ? 'mebnî' : s.mood;
  const kur = BABS_READY && ROOTS ? (ROOTS[root] ? Object.values(ROOTS[root]).reduce((n, v) => n + v.length, 0) : 0) : null;
  sheet(`<div class="fk"><div class="fkw" lang="ar">${r.f}</div>
   <table class="kwt"><tr><th>Kip</th><td>${s.tr} <span class="kar" lang="ar">${s.ar}</span></td></tr>
   ${r.si ? `<tr><th>Sîga</th><td>${SIGA[r.si][0]} <span class="kar" lang="ar">(${SIGA[r.si][1]})</span></td></tr>` : `<tr><th>Şekil</th><td>${r.lbl}</td></tr>`}
   <tr><th>Kök</th><td><b class="kar" lang="ar">${[...root].join(' ')}</b> · Sahîh (sâlim)</td></tr>
   <tr><th>Bâb</th><td>Sülâsî mücerred · <b>${BAB[bab].ad}</b> <span class="kar" lang="ar">${BAB[bab].ar}</span></td></tr>
   ${mood ? `<tr><th>İ‘râb / binâ</th><td>${mood}</td></tr>` : ''}
   ${r.t ? `<tr><th>Türkçesi</th><td>${esc(r.t)}</td></tr>` : ''}</table>
   ${s.note ? `<p class="knote">${s.note}</p>` : ''}
   <div class="kwf">${kur ? `<button class="pill" onclick="kuranKok('${root}')">Kur’an’da bu kök (${kur} yer) ›</button>` : ''}<a class="pill" target="_blank" rel="noopener" href="${bugLink('emsile ' + root + ' ' + s.key + ' ' + (r.si || r.lbl), r.f)}">Hata bildir</a></div>
   </div>`);
}
function sheet(html){
  let o = $('#sh'); if(!o){ o = document.createElement('div'); o.id = 'sh'; o.className = 'kwov'; o.innerHTML = '<div class="kws"><div class="kwh"><span class="kwref"></span><button class="kwx kwc" aria-label="Kapat">✕</button></div><div class="shb"></div></div>'; document.body.appendChild(o);
    o.addEventListener('click', e => { if(e.target === o || e.target.closest('.kwc')) o.classList.add('hide') }) }
  $('.shb', o).innerHTML = html; o.classList.remove('hide');
}
function kuranKok(root){
  const R = ROOTS[root]; if(!R) return;
  const refs = Object.entries(R).sort((a, b) => b[1].length - a[1].length);
  $('#sh .shb').innerHTML = `<p class="knote"><b class="kar" lang="ar">${[...root].join(' ')}</b> kökü Kur’an’da:</p>` + refs.map(([l, rs]) => `<details class="kkd"><summary><span lang="ar">${esc(l)}</span> <small>${rs.length}</small></summary><div class="kref">${rs.map(x => { const [s, a, w] = x.split(':'); return `<button onclick="$('#sh').classList.add('hide');go('/kuran/${s}/${a}/${w - 1}')">${s}:${a}</button>` }).join('')}</div></details>`).join('');
}
function rozetKontrol(){
  const o = LS.get('medrese.okundu', {}), keys = emsile('نصر', 1).map(s => s.key), hepsi = keys.every(k => o['نصر' + k]);
  const s = SRS.all(), em = Object.keys(s).filter(k => !k.startsWith('bab|')), ok = em.reduce((n, k) => n + s[k].ok, 0), bad = em.reduce((n, k) => n + s[k].bad, 0);
  const rz = LS.get('medrese.rozet', {});
  if(hepsi && ok >= 40 && ok / (ok + bad) >= 0.8 && !rz.emsile){ rz.emsile = Date.now(); LS.set('medrese.rozet', rz); sheet(`<div class="rozet"><div class="rz-i">✦</div><h2>Emsile’yi bitirdin</h2><p>Bütün bölümleri okudun ve alıştırmalarda %${Math.round(ok / (ok + bad) * 100)} başarıya ulaştın. Sıradaki kitap: <b>Binâ</b>.</p></div>`) }
}

/* ---- alıştırma ---- */
function alistirma(opt){
  let ids;
  if(opt.scope === 'tekrar'){ ids = shuffle(SRS.due()).slice(0, 15); if(!ids.length){ V.innerHTML = bar('Bugünün tekrarı', '/') + `<div class="wrap"><div class="empty"><b>Bugün tekrar edilecek soru yok.</b><p>Yeni sorular çözdükçe, unutmaya başlayacağınız gün tekrar buraya gelirler.</p><a class="btn pri" href="#/emsile/alistirma">Yeni alıştırma</a></div></div>`; return } }
  else if(opt.ids) ids = opt.ids;
  else if(opt.scope === 'yanlis') ids = shuffle(SRS.wrong()).slice(0, 15);
  else ids = newIds(10, opt.key ? { root: opt.root, bab: opt.bab, key: opt.key } : null);
  let i = 0, dogru = 0;
  const title = opt.title || (opt.scope === 'tekrar' ? 'Bugünün tekrarı' : opt.scope === 'yanlis' ? 'Yanlışlarım' : 'Emsile alıştırması');
  const next = () => {
    if(i >= ids.length){ V.innerHTML = bar(title, '/') + `<div class="wrap"><div class="empty"><div class="score">${dogru} / ${ids.length}</div><p>${dogru === ids.length ? 'Mükemmel.' : 'Yanlışlar “Yanlışlarım” listesine ve tekrar takvimine eklendi.'}</p><a class="btn pri" href="#/emsile/alistirma" onclick="setTimeout(route)">Yeni set</a> <a class="btn" href="#/">Medrese</a></div></div>`; rozetKontrol(); return }
    const q = makeQ(ids[i]); if(!q){ i++; return next() }
    V.innerHTML = bar(title, '/') + `<div class="wrap"><div class="prog"><i style="width:${i / ids.length * 100}%"></i></div><div class="q"><div class="qn">${i + 1} / ${ids.length} · ${TAGS[q.tag]}</div>
      ${q.kelime ? `<div class="qw" lang="ar">${q.kelime}</div>` : ''}<div class="qs">${q.soru}</div>
      <div class="opts">${q.secenek.map((o, k) => `<button data-k="${k}">${o.t}</button>`).join('')}</div><div class="qa"></div></div></div>`;
    $$('.opts button').forEach(b => b.onclick = () => {
      if($('.opts').classList.contains('done')) return; $('.opts').classList.add('done');
      const o = q.secenek[+b.dataset.k], ok = o.v === q.dogru; if(ok) dogru++;
      b.classList.add(ok ? 'ok' : 'bad'); if(!ok) $$('.opts button').forEach((x, k) => { if(q.secenek[k].v === q.dogru) x.classList.add('ok') });
      SRS.grade(q.id, ok, q.tag);
      $('.qa').innerHTML = `<p class="${ok ? 'okt' : 'badt'}">${ok ? 'Doğru.' : 'Yanlış.'} ${q.aciklama}</p><div class="qf"><button class="btn pri" id="nx">Devam ›</button><a class="lnk" target="_blank" rel="noopener" href="${bugLink(q.id, q.soru.replace(/<[^>]+>/g, '') + ' ' + (q.kelime || ''))}">Hata bildir</a></div>`;
      $('#nx').onclick = () => { i++; next() }; $('#nx').focus();
    });
  };
  next();
}
function yanlislar(){
  const w = SRS.wrong();
  V.innerHTML = bar('Yanlışlarım', '/') + `<div class="wrap">${w.length ? `<p class="lead">${w.length} soruyu en son yanlış cevapladınız. Doğru cevapladıkça listeden çıkar.</p><a class="btn pri" href="#" id="yb">Yanlışlarımı çöz ›</a>
    <ul class="wl">${w.map(id => { const q = makeQ(id); return q ? `<li><b lang="ar">${q.kelime || ''}</b> ${q.soru.replace(/<[^>]+>/g, '')} <small>${TAGS[q.tag]}</small></li>` : '' }).join('')}</ul>` : '<div class="empty"><b>Yanlışınız yok.</b><p>Alıştırma çözdükçe yanlış cevapladıklarınız burada toplanır.</p></div>'}</div>`;
  const yb = $('#yb'); if(yb) yb.onclick = e => { e.preventDefault(); alistirma({ scope: 'yanlis' }) };
}
function rapor(){
  const o = SRS.all(), by = {}, bySiga = {}, byKip = {};
  for(const [id, r] of Object.entries(o)){
    const [tip, , , key, si] = id.split('|');
    const acc = (m, k) => { m[k] = m[k] || { ok: 0, bad: 0 }; m[k].ok += r.ok; m[k].bad += r.bad };
    acc(by, r.tag || tip); if(['siga','kip','cekim','turkce'].includes(tip)){ acc(bySiga, si); acc(byKip, key) }
  }
  const S0 = emsile('نصر', 1);
  const tagAd = k => TAGS[k] || (k.startsWith('kitap:') ? (BOOKS.find(b => b.id === k.slice(6)) || { ad: k }).ad : k.startsWith('yds:') ? 'YDS · ' + (YDS_TIP[k.slice(4)] || [k])[0] : k === 'mo' ? 'Modern Arapça okuma' : k === 'mk' ? 'Kelime kartları' : k);
  const line = (ad, x) => { const n = x.ok + x.bad, p = n ? Math.round(x.bad / n * 100) : 0; return `<div class="rr"><span>${ad}</span><span class="rb"><i style="width:${p}%" class="${p >= 40 ? 'hi' : p >= 20 ? 'md' : ''}"></i></span><b>%${p}</b><small>${n} cevap</small></div>` };
  const zayif = Object.entries(bySiga).concat(Object.entries(byKip).map(([k, v]) => ['k' + k, v])).filter(([, x]) => x.ok + x.bad >= 3).map(([k, x]) => [k, x.bad / (x.ok + x.bad), x]).filter(x => x[1] >= 0.3).sort((a, b) => b[1] - a[1]).slice(0, 3);
  const ad = k => k[0] === 'k' ? (S0.find(s => s.key === k.slice(1)) || { tr: k }).tr : SIGA[+k] ? SIGA[+k][0] + ' sîgası' : k;
  V.innerHTML = bar('Zayıf konularım', '/') + `<div class="wrap">${Object.keys(o).length ? `
   ${zayif.length ? `<div class="warn"><b>Öncelikli çalışılacaklar:</b><ul>${zayif.map(([k, p]) => `<li>${ad(k)} — %${Math.round(p * 100)} hata</li>`).join('')}</ul></div>` : '<div class="okbox">Belirgin bir zayıf konu yok. Böyle devam.</div>'}
   <h2>Soru türüne göre hata oranı</h2>${Object.entries(by).map(([k, x]) => line(tagAd(k), x)).join('')}
   <h2>Sîgaya göre</h2>${Object.entries(bySiga).sort((a, b) => a[0] - b[0]).map(([k, x]) => line(SIGA[+k] ? SIGA[+k][0] : k, x)).join('')}
   <h2>Kipe göre</h2>${Object.entries(byKip).map(([k, x]) => line((S0.find(s => s.key === k) || { tr: k }).tr, x)).join('')}`
   : '<div class="empty"><b>Henüz veri yok.</b><p>Birkaç alıştırma çözünce hangi sîga ve kiplerde zorlandığınız burada görünür.</p></div>'}</div>`;
}

/* ---- Bâb bul oyunu (Kur'an'dan sâlim fiiller) ---- */
let BABS = {}, BABS_READY = false, ROOTS = null;
fetch('data/morph/babs.json').then(r => r.json()).then(j => { BABS = j; BABS_READY = true }).catch(() => {});
fetch('data/morph/roots.json').then(r => r.json()).then(j => { ROOTS = j }).catch(() => {});
function babHavuz(){ return Object.keys(BABS).filter(k => BABS[k][1] && k.length === 3 && !/[ويأإآءؤئى]/.test(k) && k[1] !== k[2]) }
function babOyunu(hizli){
  if(!BABS_READY){ V.innerHTML = bar('Bâb bul', '/') + '<div class="wrap"><p class="lead">Yükleniyor…</p></div>'; setTimeout(() => babOyunu(hizli), 400); return }
  const havuz = babHavuz(); let puan = 0, seri = 0, sayi = 0, bitis = hizli ? Date.now() + 60000 : 0, tm;
  const tur = () => {
    if(hizli && Date.now() >= bitis) return son();
    const root = pick(havuz), bab = BABS[root][0], id = ['bab', root, bab, 'mazi', 1].join('|'), q = makeQ(id);
    const refs = ROOTS && ROOTS[root] ? Object.values(ROOTS[root]).reduce((n, v) => n + v.length, 0) : 0;
    V.innerHTML = bar(hizli ? 'Hızlı tur' : 'Bâb bul', '/') + `<div class="wrap"><div class="gbar"><span>Puan <b>${puan}</b></span><span>Seri <b>${seri}</b></span>${hizli ? '<span>Süre <b id="sure">60</b></span>' : `<span>${sayi} soru</span>`}</div>
      <div class="q"><div class="qw big" lang="ar">${q.kelime}</div><p class="qs">${q.soru} <small>(Kur’an’da ${refs} yerde geçen kök)</small></p><div class="opts g6">${q.secenek.map((o, k) => `<button data-k="${k}">${o.t}</button>`).join('')}</div><div class="qa"></div></div></div>`;
    $$('.opts button').forEach(b => b.onclick = () => {
      if($('.opts').classList.contains('done')) return; $('.opts').classList.add('done'); sayi++;
      const ok = q.secenek[+b.dataset.k].v === q.dogru; b.classList.add(ok ? 'ok' : 'bad');
      if(ok){ seri++; puan += 10 + Math.min(seri, 10) } else { seri = 0; $$('.opts button').forEach((x, k) => { if(q.secenek[k].v === q.dogru) x.classList.add('ok') }) }
      SRS.grade(id, ok, 'bab');
      if(hizli && ok) return setTimeout(tur, 250);
      $('.qa').innerHTML = `<p class="${ok ? 'okt' : 'badt'}">${q.aciklama}</p><div class="qf"><button class="btn pri" id="nx">Sonraki ›</button> <button class="btn" onclick="go('/kuran');setTimeout(()=>kuranKokAc('${root}'),300)">Kur’an’da gör</button></div>`;
      $('#nx').onclick = tur; $('#nx').focus();
    });
  };
  const son = () => { clearInterval(tm); const best = LS.get('medrese.babBest', 0); if(puan > best) LS.set('medrese.babBest', puan);
    V.innerHTML = bar('Hızlı tur', '/') + `<div class="wrap"><div class="empty"><div class="score">${puan}</div><p>${sayi} fiil · ${puan > best ? 'Yeni rekor!' : 'En iyi: ' + best}</p><a class="btn pri" href="#" onclick="babOyunu(true);return false">Tekrar oyna</a> <a class="btn" href="#/">Medrese</a></div></div>` };
  if(hizli) tm = setInterval(() => { const s = $('#sure'); if(!s) return clearInterval(tm); const k = Math.max(0, Math.ceil((bitis - Date.now()) / 1000)); if(s) s.textContent = k; if(k <= 0){ clearInterval(tm); son() } }, 250);
  tur();
}
function kuranKokAc(root){ if(!ROOTS || !ROOTS[root]) return; sheet('<div></div>'); kuranKok(root) }

/* ---- Kur'an i'râb modülü ---- */
const QCACHE = {};
const qText = s => QCACHE[s] || (QCACHE[s] = fetch(`data/q/quran-uthmani/${s}.json`).then(r => { if(!r.ok) throw 0; return r.json() }));
function kuranListe(){
  const last = LS.get('medrese.kuranSon', null);
  V.innerHTML = bar('Kur’an i‘râbı', '/kitap/kuran') + `<div class="wrap">${last ? `<a class="btn pri" href="#/kuran/${last.s}/${last.a}">Devam et · ${S_TR[last.s - 1]} ${last.s}:${last.a} ›</a>` : ''}
   <input class="srch" id="sq" placeholder="Sûre ara (ad veya numara)"><div class="slist">${S_TR.map((n, i) => `<a href="#/kuran/${i + 1}" data-n="${(i + 1) + ' ' + n.toLocaleLowerCase('tr')}"><i>${i + 1}</i><b>${n}</b><span lang="ar">${S_AR[i]}</span><small>${S_CNT[i]} âyet</small></a>`).join('')}</div></div>`;
  $('#sq').oninput = e => { const q = e.target.value.toLocaleLowerCase('tr').trim(); $$('.slist a').forEach(a => a.style.display = !q || a.dataset.n.includes(q) ? '' : 'none') };
}
async function kuranSure(s, focus, w){
  const mode = () => LS.get('mihrab.kwMode', 'sarf');
  V.innerHTML = bar(`${s}. ${S_TR[s - 1]}`, '/kuran') + `<div class="wrap"><p class="lead">Yükleniyor…</p></div>`;
  let d; try{ d = await qText(s) }catch(e){ V.querySelector('.lead').textContent = 'Sûre yüklenemedi; internet bağlantınızı kontrol edin.'; return }
  const strip = (n, t) => { if(n !== 1 || s === 1 || s === 9) return t; const x = t.split(' '); return x.slice(4).join(' ') };
  const toAr = n => String(n).replace(/\d/g, c => '٠١٢٣٤٥٦٧٨٩'[c]);
  V.innerHTML = bar(`${s}. ${S_TR[s - 1]}`, '/kuran') + `<div class="wrap">
   <div class="qmode"><span>Kelimeye dokununca:</span><span class="seg"><button data-m="sarf">Sarf <i lang="ar">صرف</i></button><button data-m="nahiv">Nahiv <i lang="ar">نحو</i></button></span></div>
   <div class="qsh"><div lang="ar">سُورَةُ ${S_AR[s - 1]}</div>${s !== 1 && s !== 9 ? '<div class="qb" lang="ar">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</div>' : ''}</div>
   ${d.a.map(a => `<div class="ay" id="a${a.n}" data-a="${a.n}"><div class="ar-t" lang="ar">${Kelime.wrap(strip(a.n, a.t))} <span class="num">${toAr(a.n)}</span></div></div>`).join('')}
   <div class="qnav">${s > 1 ? `<a class="btn" href="#/kuran/${s - 1}">‹ ${S_TR[s - 2]}</a>` : '<span></span>'}${s < 114 ? `<a class="btn" href="#/kuran/${s + 1}">${S_TR[s]} ›</a>` : ''}</div>
   <p class="taslak">Veri: Quranic Arabic Corpus (GNU GPL).</p></div>`;
  const setM = () => $$('.qmode [data-m]').forEach(b => b.setAttribute('aria-pressed', b.dataset.m === mode()));
  setM(); $$('.qmode [data-m]').forEach(b => b.onclick = () => { LS.set('mihrab.kwMode', b.dataset.m); setM() });
  if(focus){ const e = $('#a' + focus); if(e) e.scrollIntoView({ block: 'center' }) }
  if(w != null && focus) setTimeout(() => Kelime.open(s, focus, w), 300);
  LS.set('medrese.kuranSon', { s, a: focus || 1 });
  kuranSure.s = s;
}
V.addEventListener('click', e => kuranTap(e));
function kuranTap(e){ if(!location.hash.startsWith('#/kuran/')) return; const ay = e.target.closest('.ay'); if(!ay) return; LS.set('medrese.kuranSon', { s: kuranSure.s, a: +ay.dataset.a }); Kelime.onTap(e, kuranSure.s) }
if(window.Kelime){ Kelime.cfg.jump = (s, a, w) => go(`/kuran/${s}/${a}/${w}`); Kelime.cfg.irab = null }


/* ======================================================================
   KİTAPLAR (Binâ, Maksûd, İzzî, Avâmil, Âcurrûmiyye, Katru'n-nedâ)
   ====================================================================== */
const KITAPLAR = ['bina', 'maksud', 'izzi', 'avamil', 'birgivi', 'izhar', 'zuruf', 'kavaid', 'ajurrumiyye', 'katr', 'serhkatr'];
const KC = {}, KP = {};
const kitapYukle = id => KP[id] || (KP[id] = getJSON(`data/kitap/${id}.json`, j => Array.isArray(j.bolumler)).then(j => (KC[id] = j)).catch(e => { delete KP[id]; throw e }));
let YDSB = null, MOD = null;
const ydsYukle = () => YDSB ? Promise.resolve(YDSB) : getJSON('data/yds/banka.json', j => Array.isArray(j.sorular) && j.pasajlar).then(j => (YDSB = j));
const modYukle = () => MOD ? Promise.resolve(MOD) : getJSON('data/modern/modern.json', j => Array.isArray(j.metinler)).then(j => (MOD = j));
const YUK = Promise.all([...KITAPLAR.map(id => kitapYukle(id).catch(() => null)), ydsYukle().catch(() => null), modYukle().catch(() => null)]);
const YDS_TIP = {
  kelime: ['Kelime bilgisi', 'Cümlede boş bırakılan yere uygun sözcüğü bulunuz.'],
  gramer: ['Dilbilgisi', 'Cümlede boş bırakılan yere uygun sözcük veya ifadeyi bulunuz.'],
  cloze: ['Paragrafta boşluk doldurma (cloze)', 'Parçada numaralanmış yerlere uygun sözcük veya ifadeyi bulunuz.'],
  tamamlama: ['Cümle tamamlama', 'Verilen cümleyi uygun şekilde tamamlayan ifadeyi bulunuz.'],
  ceviri: ['Çeviri (Arapça ↔ Türkçe)', 'Verilen cümleye anlamca en yakın çeviriyi bulunuz.'],
  paragraf: ['Okuduğunu anlama (paragraf)', 'Parçaya göre soruları cevaplayınız.'],
  diyalog: ['Diyalog tamamlama', 'Diyalogda boş bırakılan yere uygun düşen ifadeyi bulunuz.'],
  yakin: ['Anlamca en yakın cümle', 'Verilen cümleye anlamca en yakın cümleyi bulunuz.'],
  bosluk: ['Parçada boşluğa uygun cümle', 'Parçada boş bırakılan yere, anlam bütünlüğünü sağlayacak cümleyi bulunuz.'],
  bozan: ['Anlam bütünlüğünü bozan cümle', 'Cümleler sırasıyla okunduğunda anlam bütünlüğünü bozan cümleyi bulunuz.']
};
const HARF5 = ['A', 'B', 'C', 'D', 'E'];
const arMi = s => /[؀-ۿ]/.test(s || '') && !/[a-zçğıöşü]{3}/i.test((s || '').replace(/[؀-ۿ]/g, ''));

function extQ(id){
  const [tip, a, b] = id.split('|');
  if(tip === 'kitap'){
    const K = KC[a], s = K && K.sorular && K.sorular[+b]; if(!s) return null;
    const sira = shuffle(s.k.map((x, i) => i));
    return { id, tag: 'kitap:' + a, soru: esc(s.s), kelime: s.w || '', secenek: sira.map(i => ({ v: i, t: arMi(s.k[i]) ? `<span lang="ar" class="ar2s">${esc(s.k[i])}</span>` : esc(s.k[i]) })), dogru: s.d, aciklama: esc(s.a || '') };
  }
  if(tip === 'yds'){
    const q = YDSB && YDSB.sorular.find(x => x.id === a); if(!q) return null;
    return { id, tag: 'yds:' + q.tip, soru: ydsSoruHTML(q), secenek: q.k.map((x, i) => ({ v: i, t: `<b class="sk">${HARF5[i]})</b> ` + (arMi(x) ? `<span lang="ar" class="ar2s">${esc(x)}</span>` : esc(x)) })), dogru: q.d, aciklama: esc(q.a || ''), ham: true };
  }
  if(tip === 'mo'){
    const m = MOD && MOD.metinler.find(x => x.id === a), s = m && m.sorular[+b]; if(!s) return null;
    return { id, tag: 'mo', soru: `<span class="qsrc">${esc(m.baslik)}</span> ` + (arMi(s.s) ? `<span lang="ar" class="ar2s">${esc(s.s)}</span>` : esc(s.s)), secenek: shuffle(s.k.map((x, i) => ({ v: i, t: arMi(x) ? `<span lang="ar" class="ar2s">${esc(x)}</span>` : esc(x) }))), dogru: s.d, aciklama: esc(s.a || '') };
  }
  if(tip === 'mk'){
    const all = kelimeHavuz(), w = all.find(x => x[0] === a); if(!w) return null;
    const yanlis = shuffle(all.filter(x => x[1] !== w[1])).slice(0, 3);
    const op = shuffle([w, ...yanlis]);
    return { id, tag: 'mk', soru: 'Bu kelimenin anlamı nedir?', kelime: w[0], secenek: op.map(x => ({ v: x[1], t: esc(x[1]) })), dogru: w[1], aciklama: `${w[0]}: ${w[1]}${w[2] ? ' — ' + w[2] : ''}` };
  }
  return null;
}
function kelimeHavuz(){ const out = []; if(MOD) MOD.kelime.forEach(t => t.liste.forEach(x => out.push(x))); if(YDSB && YDSB.kelime) YDSB.kelime.forEach(x => out.push(x)); return out }

function pasaj(p, serh){
  if(!serh || p.length < 380) return [p];
  const r = p.split(/\s(?=(?:ولما |فإن قلت|قلت |وأما |فأما |ثم ذكرت|ثم بينت|وقد تبين|والحاصل|ومثال |والدليل|ومن ذلك|وتقرير|الحالة |وذلك كقوله|قال الشاعر|وقال آخر|وقال الله|قال الله))/);
  const o = []; r.forEach(x => { if(o.length && o[o.length - 1].length < 160) o[o.length - 1] += ' ' + x; else o.push(x) }); return o;
}
async function kitapOku(id, bi){
  const b = BOOKS.find(x => x.id === id);
  V.innerHTML = bar(b ? b.ad : 'Kitap', '/kitap/' + id) + '<div class="wrap"><p class="lead">Yükleniyor…</p></div>';
  let K; try{ K = await kitapYukle(id) }catch(e){ V.querySelector('.lead').textContent = 'Kitap yüklenemedi; internet bağlantınızı kontrol edin.'; return }
  const ok = LS.get('medrese.okundu', {}), trA = LS.get('medrese.ktr', false);
  const sec = (s, i) => `<section class="sec" id="b-${i}"><h3><span class="kt">${esc(s.tr_b || '')}</span><span lang="ar">${esc(s.b || '')}</span></h3>
    ${s.n ? `<div class="dn">${s.n.map(x => `<p>${x}</p>`).join('')}</div>` : ''}
    ${s.ornek && s.ornek.length ? `<table class="orn">${s.ornek.map(o => `<tr><td lang="ar">${esc(o[0])}</td><td>${esc(o[1] || '')}</td></tr>`).join('')}</table>` : ''}
    ${(s.p || []).map((p, j) => `<div class="mp ${s.tr && s.tr[j] ? 'tk' : ''} ${trA ? 'ac' : ''} ${s.pt ? (s.pt[j] === 'm' ? 'mtn' : 'srh') : ''}">${s.pt && s.pt[j] === 'm' ? `<span class="etk">Matn · متن</span>` : ''}${!s.pt || s.pt[j] === 'm' ? `<button class="sesb" data-ses="${i}.${j}" aria-label="Sesli oku">🔊</button>` : ''}${pasaj(p, !!s.pt).map(x => `<p class="mt" lang="ar">${esc(x)}</p>`).join('')}${s.tr && s.tr[j] ? `<p class="mtr">${esc(s.tr[j])}</p>` : ''}</div>`).join('')}
    <div class="sf">${'speechSynthesis' in window ? `<button class="btn sm" data-sesb="${i}">🔊 Bölümü dinle</button> ` : ''}<button class="btn sm ${ok[id + '#' + i] ? 'on' : ''}" data-ok="${i}">${ok[id + '#' + i] ? '✓ Okundu' : 'Okudum'}</button>${K.sorular && K.sorular.some(q => q.b === i) ? ` <a class="btn sm" href="#" data-bq="${i}">Bu bâbtan sorular</a>` : ''} <a class="lnk" target="_blank" rel="noopener" href="${bugLink(id + ' bâb ' + (i + 1), s.tr_b || s.b)}">Hata bildir</a></div></section>`;
  V.innerHTML = bar(b ? b.ad : K.baslik, '/kitap/' + id) + `<div class="wrap">
    <div class="kbaslik"><div lang="ar">${esc(K.baslik)}</div><small>${esc(K.tur === 'serh' ? K.kaynak + ' · Altın çerçeveli kısımlar matn, altındakiler şerhtir' : K.tur === 'ders' ? 'Ders notu' : 'Matn: ' + K.kaynak)}${K.tr_kaynak ? ' · ' + esc(K.tr_kaynak) : ''}</small></div>
    ${K.tur !== 'ders' ? `<div class="tools"><span class="lnk">Türkçesi için cümleye dokunun</span> <label><input type="checkbox" id="ktr" ${trA ? 'checked' : ''}> Hepsini göster</label></div>` : ''}
    ${K.bolumler.length > 14 ? `<details class="tocd"><summary>📑 İçindekiler (${K.bolumler.length} bölüm)</summary><ol class="tocl">${K.bolumler.map((s, i) => `<li><a href="#" data-to="${i}" class="${ok[id + '#' + i] ? 'done' : ''}">${esc(s.tr_b || s.b)}</a></li>`).join('')}</ol></details>` : `<div class="toc">${K.bolumler.map((s, i) => `<a href="#" data-to="${i}" class="${ok[id + '#' + i] ? 'done' : ''}">${esc(s.tr_b || s.b)}</a>`).join('')}</div>`}
    ${K.bolumler.map(sec).join('')}
    <div class="end">${K.sorular ? `<a class="btn pri big" href="#/oku/${id}/alistirma">Bu kitaptan alıştırma (${K.sorular.length} soru) ›</a>` : ''}</div>
    </div>`;
  $$('.mp.tk').forEach(m => m.onclick = () => m.classList.toggle('ac'));
  $$('[data-ses]').forEach(x => x.onclick = e => { e.stopPropagation(); const [a, c] = x.dataset.ses.split('.'); seslendir(K.bolumler[a].p[c], x) });
  $$('[data-sesb]').forEach(x => x.onclick = () => seslendir(K.bolumler[x.dataset.sesb].p.join('\n'), x));
  const kt = $('#ktr'); if(kt) kt.onchange = e => { LS.set('medrese.ktr', e.target.checked); kitapOku(id) };
  $$('[data-to]').forEach(a => a.onclick = e => { e.preventDefault(); $('#b-' + a.dataset.to).scrollIntoView({ behavior: 'smooth' }) });
  $$('[data-ok]').forEach(x => x.onclick = () => { const o = LS.get('medrese.okundu', {}), k = id + '#' + x.dataset.ok; if(o[k]) delete o[k]; else o[k] = 1; LS.set('medrese.okundu', o); x.classList.toggle('on'); x.textContent = o[k] ? '✓ Okundu' : 'Okudum'; kitapRozet(id) });
  $$('[data-bq]').forEach(a => a.onclick = e => { e.preventDefault(); const n = +a.dataset.bq; alistirma({ ids: K.sorular.map((q, i) => [q, i]).filter(([q]) => q.b === n).map(([, i]) => `kitap|${id}|${i}`), title: b.ad }) });
  if(bi != null && bi !== '' && $('#b-' + bi)) $('#b-' + bi).scrollIntoView();
}
async function kitapAlistirma(id){ const K = await kitapYukle(id).catch(() => null); if(!K || !K.sorular) return go('/kitap/' + id); alistirma({ ids: shuffle(K.sorular.map((q, i) => `kitap|${id}|${i}`)).slice(0, 12), title: (BOOKS.find(b => b.id === id) || {}).ad + ' alıştırması' }) }
function kitapRozet(id){
  const K = KC[id]; if(!K) return; const o = LS.get('medrese.okundu', {}), hepsi = K.bolumler.every((s, i) => o[id + '#' + i]);
  const S = SRS.all(), ks = Object.keys(S).filter(k => k.startsWith('kitap|' + id + '|')), dog = ks.reduce((n, k) => n + S[k].ok, 0), yan = ks.reduce((n, k) => n + S[k].bad, 0);
  const rz = LS.get('medrese.rozet', {}), b = BOOKS.find(x => x.id === id);
  if(hepsi && (!K.sorular || (dog >= Math.min(10, K.sorular.length) && dog / Math.max(1, dog + yan) >= 0.8)) && !rz[id]){ rz[id] = Date.now(); LS.set('medrese.rozet', rz); sheet(`<div class="rozet"><div class="rz-i">✦</div><h2>${b.ad}’i bitirdin</h2><p>Bütün bâbları okudun${K.sorular ? ' ve alıştırmalarda başarılı oldun' : ''}. Tebrikler.</p></div>`) }
}

/* ======================================================================
   YDS ARAPÇA
   ====================================================================== */
function ydsSoruHTML(q){
  const P = q.p && YDSB.pasajlar[q.p];
  const pas = P ? `<div class="pas" lang="${arMi(P) ? 'ar' : 'tr'}">${esc(P).replace(/\((\d+)\)/g, '<b class="pn">($1)</b>').replace(/\n/g, '<br>')}</div>` : '';
  return `<div class="ydst">${esc(YDS_TIP[q.tip][1])}</div>${pas}<div class="${arMi(q.q) ? 'qar' : 'qtr'}" ${arMi(q.q) ? 'lang="ar"' : ''}>${esc(q.q).replace(/----/g, '<span class="bos">-----</span>').replace(/\n/g, '<br>')}</div>`;
}
async function yds(p1, p2){
  V.innerHTML = bar('YDS Arapça', '/') + '<div class="wrap"><p class="lead">Yükleniyor…</p></div>';
  try{ await ydsYukle() }catch(e){ V.querySelector('.lead').textContent = 'Soru bankası yüklenemedi.'; return }
  const Q = YDSB.sorular, S = SRS.all();
  if(p1 === 'tip') return alistirma({ ids: shuffle(Q.filter(q => q.tip === p2).map(q => 'yds|' + q.id)), title: 'YDS · ' + YDS_TIP[p2][0] });
  if(p1 === 'deneme') return p2 ? ydsDeneme(p2) : ydsDenemeler();
  if(p1 === 'kelime') return kartlar((YDSB.kelime || []), 'YDS kelime kartları', '/yds');
  if(p1 === 'rehber') return ydsRehber();
  if(p1 === 'metin'){ await modYukle(); const mm = MOD.metinler.find(x => x.id === p2); return modMetin(p2, mm && mm.alan ? '/yds/alan/' + mm.alan : '/yds') }
  if(p1 === 'alan'){ await modYukle(); const a = (MOD.alanlar || []).find(x => x[0] === p2); if(!a) return go('/yds');
    const L = MOD.metinler.filter(m => m.alan === p2);
    V.innerHTML = bar(a[1], '/yds') + `<div class="wrap"><h1 lang="ar" class="mh1" style="text-align:center">${esc(a[2])}</h1><div class="mlist">${L.map(m => `<a href="#/yds/metin/${m.id}" class="${LS.get('medrese.modOk', {})[m.id] ? 'done' : ''}"><span class="sv">${esc(m.seviye)}</span><b lang="ar">${esc(m.ar_baslik)}</b><span>${esc(m.baslik)}</span><small>${m.ar.join(' ').split(/\s+/).length} kelime · ${m.sorular.length} soru</small></a>`).join('')}</div></div>`; return }
  if(p1 === 'tema'){ await modYukle(); const tm = MOD.kelime[+p2]; return kartlar(tm.liste, tm.tema, '/yds') }
  if(p1 === 'haber'){ await modYukle(); return modHaber('/yds') }
  await modYukle().catch(() => null);
  const acc = t => { const ks = Q.filter(q => q.tip === t).map(q => 'yds|' + q.id).filter(k => S[k]); const o = ks.reduce((n, k) => n + S[k].ok, 0), b = ks.reduce((n, k) => n + S[k].bad, 0); return o + b ? `%${Math.round(o / (o + b) * 100)} doğru` : 'başlanmadı' };
  const son = LS.get('medrese.ydsSon', null);
  V.innerHTML = bar('YDS Arapça', '/') + `<div class="wrap">
   <div class="ydsh"><div class="hero-ar" lang="ar">اِخْتِبَارُ اللُّغَةِ</div><p><b>${ydsDn().length} deneme · ${Q.length} soru</b> · Her deneme 80 soru, 180 dakika · Yanlış doğruyu götürmez · Her doğru 1,25 puan</p>
    <div class="hero-b"><a class="btn pri" href="#/yds/deneme">Deneme sınavları (${ydsDn().length})</a><a class="btn" href="#/yds/kelime">Kelime kartları (${(YDSB.kelime || []).length})</a><a class="btn" href="#/yds/rehber">Sınav rehberi</a></div>
    ${son ? `<p class="lead">Son deneme${son.n ? ' (' + (+son.n) + '.)' : ''}: <b>${esc(String(son.puan))}</b> puan (${son.dogru}/${son.toplam}) · ${new Date(son.t).toLocaleDateString('tr-TR')}</p>` : ''}</div>
   ${MOD ? `<h2>Okuma metinleri</h2><div class="alanlar">${(MOD.alanlar || []).map(a => { const n = MOD.metinler.filter(m => m.alan === a[0]).length; return n ? `<a class="alan a-${a[0]}" href="#/yds/alan/${a[0]}"><span lang="ar">${esc(a[2])}</span><b>${esc(a[1])}</b><small>${n} metin</small></a>` : '' }).join('')}</div>
   <h2>Kelime temaları</h2><div class="tiplist">${MOD.kelime.map((k, i) => `<a href="#/yds/tema/${i}"><b>${esc(k.tema)}</b><small lang="ar">${esc(k.liste.slice(0, 3).map(x => x[0]).join('، '))} … (${k.liste.length})</small></a>`).join('')}<a href="#/yds/kelime"><b>YDS sık kelimeleri</b><small>${(YDSB.kelime || []).length} kelime</small></a><a href="#/yds/haber"><b>Haber Arapçası kalıpları</b><small>el-Cezîre okuma rehberi</small></a></div>` : ''}
   <h2>Konu konu çalış</h2><div class="tiplist">${Object.keys(YDS_TIP).map(t => { const n = Q.filter(q => q.tip === t).length; return n ? `<a href="#/yds/tip/${t}"><b>${YDS_TIP[t][0]}</b><small>${n} soru · ${acc(t)}</small></a>` : '' }).join('')}</div>
   <p class="taslak">Sorular ÖSYM YDS Arapça sınavının yapısına göre hazırlanmıştır. Gerçek çıkmış sorular için ÖSYM’nin yayımladığı kitapçıklara bakınız.</p></div>`;
}
function ydsRehber(){
  V.innerHTML = bar('YDS rehberi', '/yds') + `<div class="wrap"><div class="rehber">
  <h2>Sınavın yapısı (ÖSYM YDS Arapça)</h2>
  <table class="kwt"><tr><th>1–6</th><td>Cümlede boşluğa uygun sözcük (kelime bilgisi)</td></tr><tr><th>7–16</th><td>Cümlede boşluğa uygun sözcük/ifade (dilbilgisi: harf-i cerler, bağlaçlar, fiil kipleri, i‘râb)</td></tr>
  <tr><th>17–26</th><td>İki parçada numaralanmış boşluklar (cloze test)</td></tr><tr><th>27–36</th><td>Cümle tamamlama</td></tr><tr><th>37–42</th><td>Arapça → Türkçe ve Türkçe → Arapça en yakın çeviri</td></tr>
  <tr><th>43–62</th><td>Beş paragraf, her birinden 4 soru (okuduğunu anlama)</td></tr><tr><th>63–67</th><td>Diyalog tamamlama</td></tr><tr><th>68–71</th><td>Anlamca en yakın cümle</td></tr>
  <tr><th>72–75</th><td>Parçada boşluğa uygun cümle</td></tr><tr><th>76–80</th><td>Anlam bütünlüğünü bozan cümle</td></tr></table>
  <h2>Puan ve süre</h2><p>80 soru, 180 dakika; her doğru 1,25 puan, yanlış cevap doğruyu götürmez — boş bırakmayın. Soru başına ortalama 2 dakika 15 saniye düşer.</p>
  <h2>Strateji</h2><ul>
   <li><b>Önce kelime ve dilbilgisi (1–16):</b> hızlı geçin, 20 dakikayı aşmayın. Dilbilgisinde harf-i cerin fiille uyumu (رغب في / رغب عن), bağlaçlar (لكنّ، بل، حتى، إذ، كي) ve i‘râb (inne’nin ismi mansûb, kâne’nin haberi mansûb) sık çıkar.</li>
   <li><b>Cloze test:</b> boşluğun önünü ve arkasını birlikte okuyun; bağlaç sorularında iki cümlenin ilişkisine (sebep, zıtlık, sonuç) bakın.</li>
   <li><b>Çeviri:</b> önce zamanı (mâzî/muzâri), olumsuzluğu (لم، لن، ما، ليس) ve öznenin kim olduğunu kontrol edin; bunlardan birini bozan şıkları eleyin.</li>
   <li><b>Paragraf:</b> soruları önce okuyun, sonra metne dönün. Ana fikir soruları için ilk ve son cümleye; “metinde değinilmeyen” sorularında şıkları tek tek metinde arayın.</li>
   <li><b>Anlam bütünlüğünü bozan cümle:</b> konudan sapan, zamir veya bağlaçla önceki cümleye bağlanmayan cümleyi arayın.</li>
   <li><b>Okuma alışkanlığı:</b> her gün bir Arapça haber okuyun (Medrese › Modern Arapça). YDS paragrafları bilim, tarih, sağlık, coğrafya, şehirler ve kültür konularındandır.</li></ul>
  <h2>Resmî kaynak</h2><p>Geçmiş yılların soru kitapçıkları ve cevap anahtarları ÖSYM’nin sitesinde yayımlanır: <a href="https://www.osym.gov.tr" target="_blank" rel="noopener">osym.gov.tr</a> › Sınavlar › YDS › Soru kitapçıkları.</p>
  </div></div>`;
}
const YDS_SIRA = ['kelime', 'gramer', 'cloze', 'tamamlama', 'ceviri', 'paragraf', 'diyalog', 'yakin', 'bosluk', 'bozan'];
const ydsDn = () => [...new Set(YDSB.sorular.map(q => q.dn || 1))].sort((a, b) => a - b);
const ydsDQ = n => YDSB.sorular.filter(q => (q.dn || 1) === n).map((q, k) => [q, k]).sort((x, y) => (YDS_SIRA.indexOf(x[0].tip) - YDS_SIRA.indexOf(y[0].tip)) || (x[1] - y[1])).map(x => x[0]);
function ydsDenemeler(){
  const sn = LS.get('medrese.ydsSonlar', {}), yar = LS.get('medrese.ydsD', null);
  V.innerHTML = bar('Deneme sınavları', '/yds') + `<div class="wrap"><p class="lead">Her deneme gerçek sınav düzenindedir: 180 dakika, yanlış doğruyu götürmez. Sınav yarıda kalırsa kaldığınız yerden devam edersiniz.</p>
    ${yar && yar.n ? `<p><a class="btn pri" href="#/yds/deneme/${+yar.n}">Yarıda kalan ${+yar.n}. denemeye devam et</a></p>` : ''}
    <div class="dnl">${ydsDn().map(n => { const r = sn[n], k = ydsDQ(n).length; return `<a href="#/yds/deneme/${n}" class="${r ? 'done' : ''}"><b>${n}. Deneme</b><small>${k} soru</small><span>${r ? `${esc(String(r.puan))} puan · ${+r.dogru}/${+r.toplam}` : 'Henüz çözülmedi'}</span></a>` }).join('')}</div></div>`;
}
function ydsDeneme(n){
  n = +n; const Q = ydsDQ(n); if(!n || !Q.length) return ydsDenemeler();
  const SURE = 180 * 60e3, KEY = 'medrese.ydsD'; let cev = {}, bas = Date.now(), i = 0, tm, bitti = false;
  const esk = LS.get(KEY, null);
  if(esk && esk.n === n && esk.cev && typeof esk.cev === 'object' && Date.now() - esk.bas < SURE && esk.bas <= Date.now()){
    const ids = new Set(Q.map(q => q.id)); Object.keys(esk.cev).forEach(k => { const v = esk.cev[k]; if(ids.has(k) && Number.isInteger(v) && v >= 0 && v < 5) cev[k] = v });
    bas = esk.bas; i = Math.min(Math.max(0, esk.i | 0), Q.length - 1);
  }
  const kaydet = () => { if(!bitti) LS.set(KEY, { n, cev, bas, i }) };
  const sureYaz = k => `${Math.floor(k / 6e4)}:${String(Math.floor(k / 1e3) % 60).padStart(2, '0')}`;
  const show = () => {
    const q = Q[i], kalan = Math.max(0, SURE - (Date.now() - bas)); kaydet();
    V.innerHTML = bar(n + '. deneme sınavı', '/yds/deneme') + `<div class="wrap"><div class="gbar"><span>Soru <b>${i + 1}</b>/${Q.length}</span><span>Cevaplanan <b>${Object.keys(cev).length}</b></span><span>Süre <b id="dsure">${sureYaz(kalan)}</b></span></div>
      <div class="q">${ydsSoruHTML(q)}<div class="opts">${q.k.map((x, k) => `<button data-k="${k}" class="${cev[q.id] === k ? 'sel' : ''}"><b class="sk">${HARF5[k]})</b> ${arMi(x) ? `<span lang="ar" class="ar2s">${esc(x)}</span>` : esc(x)}</button>`).join('')}</div>
      <div class="qf dnav"><button class="btn" id="dp" ${i ? '' : 'disabled'}>‹ Önceki</button><button class="btn" id="dn">${i < Q.length - 1 ? 'Sonraki ›' : 'Bitir'}</button><button class="btn pri" id="db">Sınavı bitir</button></div>
      <div class="dmap">${Q.map((x, k) => `<button data-g="${k}" class="${cev[x.id] != null ? 'c' : ''} ${k === i ? 'cur' : ''}">${k + 1}</button>`).join('')}</div></div></div>`;
    $$('.opts button').forEach(b => b.onclick = () => { const k = +b.dataset.k; if(cev[q.id] === k) delete cev[q.id]; else cev[q.id] = k; if(cev[q.id] != null && i < Q.length - 1) i++; show() });
    $('#dp').onclick = () => { if(i > 0) i--; show() }; $('#dn').onclick = () => { if(i < Q.length - 1){ i++; show() } else if(confirm('Sınavı bitirmek istiyor musunuz?')) bitir() };
    $('#db').onclick = () => { const bos = Q.length - Object.keys(cev).length; if(confirm((bos ? bos + ' soru boş. ' : '') + 'Sınavı bitirmek istiyor musunuz?')) bitir() };
    $$('[data-g]').forEach(b => b.onclick = () => { i = +b.dataset.g; show() });
  };
  const bitir = () => {
    if(bitti) return; bitti = true; clearInterval(tm); LS.del(KEY); let d = 0; const by = {};
    Q.forEach(q => { const ok = cev[q.id] === q.d; if(ok) d++; by[q.tip] = by[q.tip] || [0, 0]; by[q.tip][ok ? 0 : 1]++; if(cev[q.id] != null) SRS.grade('yds|' + q.id, ok, 'yds:' + q.tip) });
    const puan = Math.round(d / Q.length * 100 * 100) / 100, kayit = { puan, dogru: d, toplam: Q.length, t: Date.now(), n };
    LS.set('medrese.ydsSon', kayit); const sn = LS.get('medrese.ydsSonlar', {}); sn[n] = kayit; LS.set('medrese.ydsSonlar', sn);
    V.innerHTML = bar(n + '. deneme sonucu', '/yds/deneme') + `<div class="wrap"><div class="empty"><div class="score">${puan}</div><p>${d} doğru / ${Q.length} soru · 100 üzerinden</p></div>
      <h2>Soru türüne göre</h2>${Object.entries(by).map(([t, [o, b]]) => `<div class="rr"><span>${YDS_TIP[t][0]}</span><span class="rb"><i style="width:${Math.round(b / (o + b) * 100)}%" class="${b / (o + b) >= .4 ? 'hi' : b / (o + b) >= .2 ? 'md' : ''}"></i></span><b>${o}/${o + b}</b><small><a href="#/yds/tip/${t}">çalış</a></small></div>`).join('')}
      <h2>Cevap anahtarı ve açıklamalar</h2>${Q.map((q, k) => `<details class="ck ${cev[q.id] === q.d ? 'ok' : 'bad'}"><summary>${k + 1}. ${YDS_TIP[q.tip][0]} — ${cev[q.id] == null ? 'boş' : cev[q.id] === q.d ? 'doğru' : 'yanlış (' + HARF5[cev[q.id]] + ')'} · doğru cevap ${HARF5[q.d]}</summary><div class="q">${ydsSoruHTML(q)}<ol type="A" class="ckk">${q.k.map((x, j) => `<li class="${j === q.d ? 'dc' : ''}" ${arMi(x) ? 'lang="ar"' : ''}>${esc(x)}</li>`).join('')}</ol><p>${esc(q.a || '')}</p></div></details>`).join('')}</div>`;
    scrollTo(0, 0);
  };
  tm = setInterval(() => { const e = $('#dsure'); if(!e) return clearInterval(tm); const k = SURE - (Date.now() - bas); if(k <= 0) return bitir(); e.textContent = sureYaz(k) }, 1000);
  show();
}

/* kelime kartları (SRS) */
function kartlar(liste, title, back){
  if(!liste.length){ V.innerHTML = bar(title, back) + '<div class="wrap"><p class="lead">Kelime yok.</p></div>'; return }
  const S = SRS.all(), t = today();
  const sira = [...liste].sort((a, b) => { const x = S['mk|' + a[0]], y = S['mk|' + b[0]]; return (x ? x.due : t - 0.5) - (y ? y.due : t - 0.5) }).slice(0, 20);
  let i = 0, bil = 0;
  const show = () => {
    if(i >= sira.length){ V.innerHTML = bar(title, back) + `<div class="wrap"><div class="empty"><div class="score">${bil}/${sira.length}</div><p>Bilemediğiniz kelimeler tekrar takvimine eklendi.</p><a class="btn pri" href="#" id="yk">Yeni 20 kart</a> <a class="btn" href="#${back}">Geri</a></div></div>`; $('#yk').onclick = e => { e.preventDefault(); kartlar(liste, title, back) }; return }
    const w = sira[i];
    V.innerHTML = bar(title, back) + `<div class="wrap"><div class="prog"><i style="width:${i / sira.length * 100}%"></i></div><div class="kart" id="kart"><div class="kw1" lang="ar">${esc(w[0])}</div><div class="kw2 hide">${esc(w[1])}${w[2] ? `<small>${esc(w[2])}</small>` : ''}</div><p class="kh">Anlamını düşünün, sonra karta dokunun</p></div>
      <div class="qf kq hide"><button class="btn" id="kb">Bilemedim</button><button class="btn pri" id="kk">Bildim</button>${'speechSynthesis' in window ? '<button class="btn" id="ks">▶ Dinle</button>' : ''}</div></div>`;
    $('#kart').onclick = () => { $('.kw2').classList.remove('hide'); $('.kh').classList.add('hide'); $('.kq').classList.remove('hide') };
    $('#kb').onclick = () => { SRS.grade('mk|' + w[0], false, 'mk'); i++; show() };
    $('#kk').onclick = () => { SRS.grade('mk|' + w[0], true, 'mk'); bil++; i++; show() };
    const ks = $('#ks'); if(ks) ks.onclick = () => seslendir(w[0], ks);
  };
  show();
}

/* ======================================================================
   MODERN ARAPÇA
   ====================================================================== */
async function modern(p1, p2){
  V.innerHTML = bar('Modern Arapça', '/') + '<div class="wrap"><p class="lead">Yükleniyor…</p></div>';
  try{ await modYukle() }catch(e){ V.querySelector('.lead').textContent = 'İçerik yüklenemedi.'; return }
  if(p1 === 'metin') return modMetin(p2);
  if(p1 === 'kelime'){ const t = MOD.kelime[+p2]; return kartlar(t.liste, t.tema, '/modern') }
  if(p1 === 'diyalog') return modDiyalog(+p2);
  if(p1 === 'haber') return modHaber();
  if(p1 === 'ders') return modDers();
  if(p1 === 'diyaloglar') return modDiyaloglar();
  location.replace('arapca.html?medrese=1');
}
function modDiyaloglar(){
  V.innerHTML = bar('Diyaloglar', '/modern') + `<div class="wrap"><div class="tiplist">${MOD.diyalog.map((d, i) => `<a href="#/modern/diyalog/${i}"><b>${esc(d.baslik)}</b><small lang="ar">${esc(d.ar_baslik || '')}</small></a>`).join('')}</div></div>`;
}
function modDers(){
  location.href = 'arapca.html?medrese=1';
}
function modMetin(id, geri){
  geri = geri || '/modern';
  const m = MOD.metinler.find(x => x.id === id); if(!m) return go(geri);
  const trG = LS.get('medrese.modTr', false), soz = new Map(m.sozluk.map(x => [x[0].replace(/[ً-ْ]/g, ''), x]));
  const norm = w => w.replace(/[ً-ْٰ]/g, '').replace(/[،.؛:؟!«»"()]/g, '');
  const kel = w => { const n = norm(w); let hit = soz.get(n) || soz.get(n.replace(/^(و|ف|ب|ل|ك)/, '')) || soz.get(n.replace(/^(و|ف)?(ال)/, '')) || soz.get(n.replace(/^(وال|فال|بال|لل)/, '')); return hit ? `<span class="gl" data-g="${esc(hit[0])}">${esc(w)}</span>` : esc(w) };
  V.innerHTML = bar(m.baslik, geri) + `<div class="wrap"><div class="mbas"><span class="sv">${esc(m.seviye)}</span> <small>${esc(m.konu)}</small><h1 lang="ar" class="mh1">${esc(m.ar_baslik)}</h1></div>
   <div class="tools"><label><input type="checkbox" id="mtr" ${trG ? 'checked' : ''}> Türkçesini göster</label>${'speechSynthesis' in window ? '<button class="btn sm" id="msesli">▶ Sesli oku</button>' : ''}<span class="lnk">Altı çizili kelimeye dokunun: anlamı çıkar</span></div>
   <div class="mtext">${m.ar.map((p, i) => `<p lang="ar" class="mpa">${p.split(/(\s+)/).map(w => /\s/.test(w) ? w : kel(w)).join('')}</p>${trG && m.tr[i] ? `<p class="mtr">${esc(m.tr[i])}</p>` : ''}`).join('')}</div>
   <h2>Sözlük</h2><table class="orn">${m.sozluk.map(x => `<tr><td lang="ar">${esc(x[0])}</td><td>${esc(x[1])}</td></tr>`).join('')}</table>
   <div class="end"><button class="btn pri big" id="msor">Sorular (${m.sorular.length}) ›</button></div></div>`;
  $('#mtr').onchange = e => { LS.set('medrese.modTr', e.target.checked); modMetin(id, geri) };
  $$('.gl').forEach(g => g.onclick = () => { const x = m.sozluk.find(s => s[0] === g.dataset.g); toast(`${x[0]} — ${x[1]}`) });
  const sb = $('#msesli'); if(sb) sb.onclick = () => seslendir(m.ar.join(' '), sb);
  $('#msor').onclick = () => { const o = LS.get('medrese.modOk', {}); o[id] = 1; LS.set('medrese.modOk', o); alistirma({ ids: m.sorular.map((s, i) => `mo|${id}|${i}`), title: m.baslik }) };
}
function modDiyalog(i){
  const d = MOD.diyalog[i]; if(!d) return go('/modern');
  V.innerHTML = bar(d.baslik, '/modern/diyaloglar') + `<div class="wrap"><h1 lang="ar" class="mh1">${esc(d.ar_baslik || '')}</h1><div class="dyl">${d.satirlar.map(s => `<div class="dy ${s[0] === d.satirlar[0][0] ? 'a' : 'b'}"><b>${esc(s[0])}</b><p lang="ar">${esc(s[1])}</p><small>${esc(s[2])}</small>${'speechSynthesis' in window ? `<button class="btn sm" data-s="${esc(s[1])}">▶</button>` : ''}</div>`).join('')}</div>
   ${d.not ? `<p class="knote">${esc(d.not)}</p>` : ''}</div>`;
  $$('[data-s]').forEach(b => b.onclick = () => seslendir(b.dataset.s, b));
}
function modHaber(geri){
  V.innerHTML = bar('Haber Arapçası', geri || '/modern') + `<div class="wrap"><div class="rehber">
  <h2>Nereden okumalı?</h2><p>Gerçek haber metinlerini kaynağında okuyun (telif sebebiyle uygulamaya kopyalanmaz):</p>
  <ul><li><a href="https://www.aljazeera.net/news/" target="_blank" rel="noopener">el-Cezîre — Haberler</a> (أخبار)</li><li><a href="https://www.aljazeera.net/ebusiness/" target="_blank" rel="noopener">el-Cezîre — Ekonomi</a> (اقتصاد)</li><li><a href="https://www.aljazeera.net/science/" target="_blank" rel="noopener">el-Cezîre — Bilim ve teknoloji</a></li><li><a href="https://www.aljazeera.net/culture/" target="_blank" rel="noopener">el-Cezîre — Kültür</a></li><li><a href="https://www.aa.com.tr/ar" target="_blank" rel="noopener">Anadolu Ajansı Arapça</a> · <a href="https://www.trtarabi.com" target="_blank" rel="noopener">TRT Arabi</a> · <a href="https://www.bbc.com/arabic" target="_blank" rel="noopener">BBC Arabic</a></li></ul>
  <h2>Nasıl çalışmalı?</h2><ol><li>Günde bir haber seçin; önce yalnızca başlığı ve ilk paragrafı okuyun (haberin özü oradadır).</li><li>Bilmediğiniz en fazla 10 kelimeyi not alın ve buradaki kelime kartlarına benzer şekilde tekrar edin.</li><li>Haberin kim, ne, nerede, ne zaman sorularını Arapça cevaplayın.</li><li>Haftada bir aynı konudan (ör. ekonomi) üç haber okuyun: kalıp ifadeler kendiliğinden yerleşir.</li></ol>
  <h2>Haber dilinin kalıp ifadeleri</h2><table class="orn">${(MOD.kaliplar || []).map(x => `<tr><td lang="ar">${esc(x[0])}</td><td>${esc(x[1])}</td></tr>`).join('')}</table></div></div>`;
}

/* ======================================================================
   GÜNLÜK SORU · İ'RÂB OYUNU · ÖĞRENME HARİTASI
   ====================================================================== */
function gunHavuz(){ const ids = []; MODEL_ROOTS.forEach(r => ['mazi', 'muz', 'lan', 'lam', 'nehy', 'emr'].forEach(k => [1, 3, 5, 9, 13].forEach(si => { if(secOf(r, MODEL[r].bab, k) && secOf(r, MODEL[r].bab, k).rows.some(x => x.si === si)) ids.push(['siga', r, MODEL[r].bab, k, si].join('|')) }))); KITAPLAR.forEach(id => (KC[id] && KC[id].sorular || []).forEach((q, i) => ids.push(`kitap|${id}|${i}`))); (YDSB ? YDSB.sorular : []).filter(q => !q.p).forEach(q => ids.push('yds|' + q.id)); return ids }
async function gunluk(){
  await YUK; const H = gunHavuz(), d = today(), id = H[(d * 2654435761 >>> 0) % H.length], g = LS.get('medrese.gunluk', {});
  const q = makeQ(id); if(!q) return home();
  const seri = (() => { let n = 0; for(let k = d - (g[d] ? 0 : 1); g[k] && g[k].ok; k--) n++; return n })();
  V.innerHTML = bar('Günün sorusu', '/') + `<div class="wrap"><div class="gbar"><span>${new Date().toLocaleDateString('tr-TR', { day: 'numeric', month: 'long' })}</span><span>Seri <b>${seri}</b> gün</span></div>
   <div class="q"><div class="qn">Bugün herkes aynı soruyu çözüyor · ${esc(TAGS[q.tag] || q.tag)}</div>${q.kelime ? `<div class="qw" lang="ar">${q.kelime}</div>` : ''}<div class="qs">${q.soru}</div>
   <div class="opts">${q.secenek.map((o, k) => `<button data-k="${k}">${o.t}</button>`).join('')}</div><div class="qa"></div></div></div>`;
  if(g[d]){ $('.opts').classList.add('done'); $$('.opts button').forEach((b, k) => { if(q.secenek[k].v === q.dogru) b.classList.add('ok') }); $('.qa').innerHTML = `<p>${g[d].ok ? 'Bugünkü soruyu doğru çözdünüz.' : 'Bugünkü soruyu kaçırdınız; yarın yeni soru gelecek.'} ${q.aciklama}</p>`; return }
  $$('.opts button').forEach(b => b.onclick = () => { const ok = q.secenek[+b.dataset.k].v === q.dogru; g[d] = { ok }; LS.set('medrese.gunluk', g); SRS.grade(id, ok, q.tag); gunluk() });
}
async function irabOyunu(){
  V.innerHTML = bar('İ‘râb oyunu', '/') + '<div class="wrap"><p class="lead">Yükleniyor…</p></div>';
  const s = 78 + Math.floor(Math.random() * 37); let d; try{ d = await Kelime.data(s) }catch(e){ V.querySelector('.lead').textContent = 'Yüklenemedi.'; return }
  const ETI = { NOM: 'merfû', ACC: 'mansûb', GEN: 'mecrûr', IND: 'merfû', SUBJ: 'mansûb', JUS: 'meczûm' };
  const etiket = W => { const S = W.map(x => { const f = {}; x[2].split('|').forEach(p => { const k = p.split(':'); f[k[0]] = k[1] || true }); return { t: x[0], pos: x[1], f } }); const m = S.find(x => x.pos === 'V') || S.find(x => x.pos === 'N' && !x.f.SUFF) || S[S.length - 1];
    if(m.pos === 'V') return m.f.IMPF && m.f.MOOD ? ETI[m.f.MOOD] : 'mebnî'; if(m.pos === 'N'){ for(const k of ['NOM', 'ACC', 'GEN']) if(m.f[k]) return ETI[k]; return 'mebnî' } return 'mebnî' };
  const ay = d.a.map((A, i) => [i + 1, A]).filter(([, A]) => A.length >= 3 && A.length <= 7); const [an, A] = pick(ay);
  const q = await fetch(`data/q/quran-uthmani/${s}.json`).then(r => r.json()); let tx = q.a[an - 1].t; if(an === 1 && s !== 9) tx = tx.split(' ').slice(4).join(' ');
  const tok = tx.split(' ').filter(w => /[ء-يٱ]/.test(w)), dog = A.map(etiket), sec = {};
  const SEC = ['merfû', 'mansûb', 'mecrûr', 'meczûm', 'mebnî'];
  V.innerHTML = bar('İ‘râb oyunu', '/') + `<div class="wrap"><p class="lead">Her kelimenin i‘râb hâlini seçin. Harfler ve mâzî fiiller <b>mebnî</b>dir. <small>(${S_TR[s - 1]} ${s}:${an})</small></p>
   <div class="iro">${A.map((W, i) => `<div class="irw"><b lang="ar">${esc(tok[i] || W.map(x => x[0]).join(''))}</b><div class="irs">${SEC.map(x => `<button data-w="${i}" data-v="${x}">${x}</button>`).join('')}</div></div>`).join('')}</div>
   <div class="qf"><button class="btn pri" id="irk">Kontrol et</button><button class="btn" onclick="irabOyunu()">Yeni âyet</button></div><div class="qa"></div></div>`;
  $$('.irs button').forEach(b => b.onclick = () => { sec[b.dataset.w] = b.dataset.v; $$(`.irs button[data-w="${b.dataset.w}"]`).forEach(x => x.classList.toggle('on', x === b)) });
  $('#irk').onclick = () => { let n = 0; A.forEach((W, i) => { const ok = sec[i] === dog[i]; if(ok) n++; $$(`.irs button[data-w="${i}"]`).forEach(x => { x.classList.remove('ok', 'bad'); if(x.dataset.v === dog[i]) x.classList.add('ok'); else if(x.dataset.v === sec[i]) x.classList.add('bad') }) });
    const best = LS.get('medrese.irabSkor', { d: 0, t: 0 }); best.d += n; best.t += A.length; LS.set('medrese.irabSkor', best);
    $('.qa').innerHTML = `<p class="${n === A.length ? 'okt' : 'badt'}">${n} / ${A.length} doğru. Toplam: ${best.d}/${best.t}. Bir kelimenin gerekçesini görmek için <a href="#/kuran/${s}/${an}">âyeti Kur’an i‘râbı modülünde açın</a>.</p>` };
}
async function harita(){
  await YUK; const o = LS.get('medrese.okundu', {}), rz = LS.get('medrese.rozet', {});
  const yuzde = id => { if(id === 'emsile'){ const ks = emsile('نصر', 1).map(s => s.key); return Math.round(ks.filter(k => o['نصر' + k]).length / ks.length * 100) } const K = KC[id]; if(!K) return 0; return Math.round(K.bolumler.filter((s, i) => o[id + '#' + i]).length / K.bolumler.length * 100) };
  const node = id => { const b = BOOKS.find(x => x.id === id), p = yuzde(id); return `<a class="hn ${rz[id] ? 'rz' : p ? 'go' : ''}" href="#/kitap/${id}"><span class="hc" style="--p:${p}"><i lang="ar">${b.ar.replace(/^(شرح|متن|التصريف) /, '').replace(/ .*/, '')}</i></span><b>${b.ad}</b><small>${rz[id] ? '✦ bitirildi' : '%' + p}</small></a>` };
  V.innerHTML = bar('Öğrenme haritam', '/') + `<div class="wrap"><p class="lead">Medrese yolunda neredesiniz? Her kitap, okunan bâbların oranıyla dolar; kitap bitince rozet alır.</p>
   <h2>Sarf</h2><div class="hyol">${['emsile', 'bina', 'maksud', 'izzi'].map(node).join('<span class="hl"></span>')}</div>
   <h2>Nahiv</h2><div class="hyol">${['avamil', 'birgivi', 'izhar', 'zuruf', 'kavaid', 'ajurrumiyye', 'serhkatr'].map(node).join('<span class="hl"></span>')}</div>
   <h2>Rozetler</h2><p>${Object.keys(rz).length ? Object.keys(rz).map(k => `<span class="rzb">✦ ${(BOOKS.find(b => b.id === k) || { ad: k }).ad}</span>`).join(' ') : 'Henüz rozet yok. Bir kitabın bütün bâblarını okuyup alıştırmalarında başarılı olunca rozet kazanırsınız.'}</p></div>`;
}

/* tema: el-Mihrâb ayarlarından */
try{ const st = JSON.parse(localStorage.getItem('beyan2.set') || '{}'); if(st.theme && st.theme !== 'parsomen') document.documentElement.dataset.theme = st.theme }catch(e){}
guvenliRoute();
