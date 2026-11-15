/* el-Mihrâb · MEDRESE — klasik Arapça (sarf · nahiv · Kur'an i'râbı)
   Bütün içerik "taslak → onaylı" kuralına tâbidir: ehil onayı olmayan her şey "taslak" damgalıdır. */
'use strict';
const $ = (s, r) => (r || document).querySelector(s), $$ = (s, r) => [...(r || document).querySelectorAll(s)];
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const LS = { get(k, d){ try{ const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v) }catch(e){ return d } }, set(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)) }catch(e){} } };
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
  { id: 'bina', ad: 'Binâ', ar: 'البناء', yol: 'sarf', sira: 2, durum: 'yakinda',
    tanitim: { muellif: 'Müellifi kesin olarak bilinmiyor; Emsile’den sonra okutulur.', amac: 'Fiilin yapısını (binâsını) öğretmek: sülâsî-rubâî, mücerred-mezîd, sahîh-mu‘tel; bâbların ve kalıpların nasıl türediği; i‘lâle giriş.', yontem: 'Emsile’deki her kalıbın kuralını Binâ’da arayın; her kuralı bir Kur’an örneğiyle eşleyin.' } },
  { id: 'maksud', ad: 'Maksûd', ar: 'المقصود', yol: 'sarf', sira: 3, durum: 'yakinda',
    tanitim: { muellif: 'İmâm-ı Âzam Ebû Hanîfe’ye nisbet edilir; bu nisbet tartışmalıdır.', amac: 'Sarf kurallarını, özellikle mezîd bâbları ve i‘lâl kaidelerini sistemli biçimde vermek.', yontem: 'Her kaideyi önce matnından, sonra örnek kelimelerin çözümlemesiyle okuyun.' } },
  { id: 'izzi', ad: 'İzzî', ar: 'التصريف العزي', yol: 'sarf', sira: 4, durum: 'yakinda',
    tanitim: { muellif: 'İzzeddîn Abdülvehhâb b. İbrâhîm ez-Zencânî (7./13. yy).', amac: 'Tasrîf ilmini (kelimenin kalıptan kalıba çevrilmesi) özlü ve ileri seviyede vermek.', yontem: 'Maksûd’dan sonra okunur; şerhleriyle birlikte, kaide kaide.' } },
  { id: 'avamil', ad: 'Avâmil', ar: 'العوامل', yol: 'nahiv', sira: 1, durum: 'yakinda',
    tanitim: { muellif: 'İmâm Birgivî (Mehmed Birgivî, ö. 981/1573) — “el-Avâmilü’l-cedîde”.', amac: 'Kelimelerin sonunu değiştiren yüz âmili (harfler, fiiller, isimler) tasnif ederek nahvin temelini kurmak.', yontem: 'Her âmili, etkilediği kelimeyle birlikte cümlede görün. Kur’an modülündeki “Avâmil notları” bu kitaba köprüdür.' } },
  { id: 'tuhfe', ad: 'Tuhfetü’s-seniyye', ar: 'التحفة السنية', yol: 'nahiv', sira: 2, durum: 'yakinda',
    tanitim: { muellif: 'Muhammed Muhyiddîn Abdülhamîd (ö. 1972); İbn Âcurrûm’un “el-Mukaddimetü’l-Âcurrûmiyye”sinin şerhi.', amac: 'Nahvin bütün temel bâblarını sade bir dille ve bol örnekle öğretmek.', yontem: 'Her bâbın sonundaki soruları cevaplayın; öğrendiğiniz i‘râbı Kur’an modülünde deneyin.' } },
  { id: 'katr', ad: 'Şerhu Katri’n-nedâ', ar: 'شرح قطر الندى', yol: 'nahiv', sira: 3, durum: 'yakinda',
    tanitim: { muellif: 'İbn Hişâm el-Ensârî (ö. 761/1360).', amac: 'Nahvi orta-ileri seviyede, şâhidleriyle birlikte vermek.', yontem: 'Şâhidleri (âyet, hadis, şiir) i‘râb ederek okuyun.' } },
  { id: 'kuran', ad: 'Kur’an i‘râbı', ar: 'إعراب القرآن', yol: 'kuran', sira: 1, durum: 'hazir',
    tanitim: { muellif: 'Kelime verisi: Quranic Arabic Corpus (Leeds Üniversitesi, corpus.quran.com, GNU GPL). Türkçe medrese terimleri, i‘râb cümleleri, bâb tespiti ve çekim tabloları bu verinin üzerine kural ile üretilir.', amac: 'Kur’ân-ı Kerîm’in her kelimesine dokununca sarf (kök, bâb, sîga) ve nahiv (i‘râb) çözümlemesini görmek; Emsile ve Avâmil’de öğrenileni Kur’an üzerinde uygulamak.', yontem: 'Bir sûre açın, kelimeye dokunun. Üstteki anahtarla Sarf ve Nahiv arasında geçin. Otomatik çözümlemeler “taslak”tır; ehil onayı alanlar “Onaylı” damgası taşır.' } },
  { id: 'yds', ad: 'YDS Arapça', ar: 'اختبار اللغة', yol: 'yds', sira: 1, durum: 'yakinda',
    tanitim: { muellif: '—', amac: 'Kelime, dilbilgisi, cümle tamamlama, çeviri ve paragraf soruları; deneme sınavı.', yontem: 'Günlük kısa setler ve aralıklı tekrar.' } },
  { id: 'modern', ad: 'Modern Arapça', ar: 'العربية المعاصرة', yol: 'modern', sira: 1, durum: 'yakinda',
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
addEventListener('hashchange', route);
function route(){
  if(window.Kelime) Kelime.close(); const sh = $('#sh'); if(sh) sh.classList.add('hide');
  const h = (location.hash || '#/').slice(2).split('/').map(decodeURIComponent);
  scrollTo(0, 0);
  const [p0, p1, p2, p3, p4] = h;
  if(!p0) return home();
  if(p0 === 'kitap') return kitap(p1);
  if(p0 === 'emsile') return p1 === 'alistirma' ? alistirma({ scope: 'emsile' }) : emsileOku();
  if(p0 === 'tekrar') return alistirma({ scope: 'tekrar' });
  if(p0 === 'yanlislar') return yanlislar();
  if(p0 === 'rapor') return rapor();
  if(p0 === 'oyun') return babOyunu(p1 === 'hizli');
  if(p0 === 'kuran') return p1 ? kuranSure(+p1, +p2 || 0, p3 ? +p3 : null) : kuranListe();
  home();
}

/* ---- ana ekran ---- */
function home(){
  const due = SRS.due().length, wr = SRS.wrong().length, rozet = LS.get('medrese.rozet', {});
  const kart = b => `<button class="bk ${b.durum}" onclick="go('/kitap/${b.id}')"><span class="bar" lang="ar">${b.ar}</span><b>${b.ad}</b>${b.durum === 'yakinda' ? '<small>yakında</small>' : rozet[b.id] ? '<small class="rz">✓ bitirildi</small>' : '<small class="ok">açık</small>'}</button>`;
  V.innerHTML = bar('Medrese') + `<div class="wrap">
   <div class="hero"><div class="hero-ar" lang="ar">المَدْرَسَة</div><p>Medrese usûlüyle sarf ve nahiv: <b>oku, anla, unutma.</b></p>
    <div class="hero-b"><a class="btn pri" href="#/tekrar">Bugünün tekrarı <i>${due}</i></a><a class="btn" href="#/yanlislar">Yanlışlarım <i>${wr}</i></a><a class="btn" href="#/rapor">Zayıf konularım</a></div></div>
   ${['sarf', 'nahiv'].map(y => `<h2>${YOL[y][0]} <span lang="ar">${YOL[y][1]}</span></h2><div class="path">${BOOKS.filter(b => b.yol === y).sort((a, b) => a.sira - b.sira).map(kart).join('<span class="arr">›</span>')}</div>`).join('')}
   <h2>Kur’an <span lang="ar">القرآن</span></h2>
   <button class="kuran-tile" onclick="go('/kitap/kuran')"><span lang="ar">إِعْرَابُ الْقُرْآنِ</span><b>Kur’an i‘râbı</b><small>Her kelimeye dokun: sarf ve nahiv çözümlemesi</small></button>
   <h2>Oyunlar</h2>
   <div class="games"><button onclick="go('/oyun')"><b>Bâb bul</b><span lang="ar">نَصَرَ؟ ضَرَبَ؟</span><small>Kur’an fiillerinden</small></button><button onclick="go('/oyun/hizli')"><b>Hızlı tur</b><span>60 saniye</span><small>En iyi: ${LS.get('medrese.babBest', 0)}</small></button></div>
   <h2>Diğer</h2><div class="path">${BOOKS.filter(b => b.yol === 'yds' || b.yol === 'modern').map(kart).join('')}</div>
   <p class="foot">Bütün içerik <b>taslaktır</b>; ehil onayından geçenler “Onaylı” damgası taşır. Hata görürseniz her ekrandaki <i>Hata bildir</i> bağlantısını kullanın.<br><a href="#" onclick="$('#src').classList.remove('hide');return false">Kaynaklar ve lisans</a></p></div>`;
}

/* ---- kitap tanıtım ekranı ---- */
function kitap(id){
  const b = BOOKS.find(x => x.id === id); if(!b) return home();
  const T = b.tanitim, hedef = id === 'emsile' ? '/emsile' : id === 'kuran' ? '/kuran' : null;
  const seen = LS.get('medrese.tanitim', {});
  V.innerHTML = bar(b.ad, '/') + `<div class="wrap"><div class="intro"><div class="intro-ar" lang="ar">${b.ar}</div><h1>${b.ad}</h1><div class="yolt">${YOL[b.yol][0]}</div>
    <dl><dt>Müellif ve dönem</dt><dd>${T.muellif}</dd><dt>Bu kitaptan maksat</dt><dd>${T.amac}</dd><dt>Nasıl çalışılır</dt><dd>${T.yontem}</dd></dl>
    ${hedef ? `<a class="btn pri big" href="#${hedef}">${seen[id] ? 'Devam et' : 'Başla'} ›</a>${id === 'emsile' ? ' <a class="btn big" href="#/emsile/alistirma">Alıştırma</a>' : ''}` : '<p class="soon">Bu kitap hazırlanıyor. Matn, Türkçe açıklama ve alıştırmalar Emsile ile aynı kalıpta eklenecek.</p>'}
    <p class="taslak">Tanıtım bilgileri taslaktır; ehil onayı bekliyor.</p></div></div>`;
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
    <p class="taslak">Kalıplar kökten kural ile üretildi. Sıralama ve masdarlar matbu Emsile nüshasıyla karşılaştırılıp onaylanacak (taslak).</p></section>
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
  const sb = $('#sesli'); if(sb) sb.onclick = () => seslendir(mh.map(x => x.f).join('، '));
}
function seslendir(t){ try{ speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(t); u.lang = 'ar-SA'; u.rate = 0.8; const v = speechSynthesis.getVoices().find(v => v.lang && v.lang.startsWith('ar')); if(v) u.voice = v; else toast('Cihazınızda Arapça ses bulunamadı'); speechSynthesis.speak(u) }catch(e){ toast('Sesli okuma desteklenmiyor') } }
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
   <div class="kok">Kural ile üretildi · <b>taslak</b></div></div>`);
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
  else if(opt.scope === 'yanlis') ids = shuffle(SRS.wrong()).slice(0, 15);
  else ids = newIds(10, opt.key ? { root: opt.root, bab: opt.bab, key: opt.key } : null);
  let i = 0, dogru = 0;
  const title = opt.scope === 'tekrar' ? 'Bugünün tekrarı' : opt.scope === 'yanlis' ? 'Yanlışlarım' : 'Emsile alıştırması';
  const next = () => {
    if(i >= ids.length){ V.innerHTML = bar(title, '/') + `<div class="wrap"><div class="empty"><div class="score">${dogru} / ${ids.length}</div><p>${dogru === ids.length ? 'Mükemmel.' : 'Yanlışlar “Yanlışlarım” listesine ve tekrar takvimine eklendi.'}</p><a class="btn pri" href="#/emsile/alistirma" onclick="setTimeout(route)">Yeni set</a> <a class="btn" href="#/">Medrese</a></div></div>`; rozetKontrol(); return }
    const q = makeQ(ids[i]); if(!q){ i++; return next() }
    V.innerHTML = bar(title, '/') + `<div class="wrap"><div class="prog"><i style="width:${i / ids.length * 100}%"></i></div><div class="q"><div class="qn">${i + 1} / ${ids.length} · ${TAGS[q.tag]}</div>
      ${q.kelime ? `<div class="qw" lang="ar">${q.kelime}</div>` : ''}<p class="qs">${q.soru}</p>
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
    acc(by, r.tag || tip); if(tip !== 'bab'){ acc(bySiga, si); acc(byKip, key) }
  }
  const S0 = emsile('نصر', 1);
  const line = (ad, x) => { const n = x.ok + x.bad, p = n ? Math.round(x.bad / n * 100) : 0; return `<div class="rr"><span>${ad}</span><span class="rb"><i style="width:${p}%" class="${p >= 40 ? 'hi' : p >= 20 ? 'md' : ''}"></i></span><b>%${p}</b><small>${n} cevap</small></div>` };
  const zayif = Object.entries(bySiga).concat(Object.entries(byKip).map(([k, v]) => ['k' + k, v])).filter(([, x]) => x.ok + x.bad >= 3).map(([k, x]) => [k, x.bad / (x.ok + x.bad), x]).filter(x => x[1] >= 0.3).sort((a, b) => b[1] - a[1]).slice(0, 3);
  const ad = k => k[0] === 'k' ? (S0.find(s => s.key === k.slice(1)) || { tr: k }).tr : SIGA[+k] ? SIGA[+k][0] + ' sîgası' : k;
  V.innerHTML = bar('Zayıf konularım', '/') + `<div class="wrap">${Object.keys(o).length ? `
   ${zayif.length ? `<div class="warn"><b>Öncelikli çalışılacaklar:</b><ul>${zayif.map(([k, p]) => `<li>${ad(k)} — %${Math.round(p * 100)} hata</li>`).join('')}</ul></div>` : '<div class="okbox">Belirgin bir zayıf konu yok. Böyle devam.</div>'}
   <h2>Soru türüne göre hata oranı</h2>${Object.entries(by).map(([k, x]) => line(TAGS[k] || k, x)).join('')}
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
  if(hizli) tm = setInterval(() => { const s = $('#sure'); const k = Math.max(0, Math.ceil((bitis - Date.now()) / 1000)); if(s) s.textContent = k; if(k <= 0){ clearInterval(tm); son() } }, 250);
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
   <p class="taslak">Çözümlemeler otomatik ve taslaktır. Veri: Quranic Arabic Corpus (GNU GPL).</p></div>`;
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

/* tema: el-Mihrâb ayarlarından */
try{ const st = JSON.parse(localStorage.getItem('beyan2.set') || '{}'); if(st.theme && st.theme !== 'parsomen') document.documentElement.dataset.theme = st.theme }catch(e){}
route();
