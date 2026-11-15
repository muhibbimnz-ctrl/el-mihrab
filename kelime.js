/* el-Mihrâb · Kelime kartı — Sarf ve Nahiv çözümlemesi
   Veri: Quranic Arabic Corpus Morphology v0.4 (corpus.quran.com, GNU GPL) — data/morph/
   Bütün açıklamalar kural tabanlı ve OTOMATİKTİR: "taslak" sayılır; data/morph/onay.json'a
   girilen ehil onaylı i'râb, otomatik metnin yerine geçer. */
(function(){
'use strict';
const K = window.Kelime = {};
/* Sayfanın verebileceği kancalar: irab(a) — âyetin tam i'râbını aç; jump(s,a,w) — başka âyete git */
K.cfg = { irab: null, jump: null };
const $q = (s, r) => (r || document).querySelector(s);
const E = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const store = { get(k, d){ try{ const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v) }catch(e){ return d } }, set(k, v){ try{ localStorage.setItem(k, JSON.stringify(v)) }catch(e){} } };

/* ---------------- veri ---------------- */
const cache = {};
function getJ(u){ return fetch(u).then(r => { if(!r.ok) throw new Error(r.status); return r.json() }) }
K.data = s => cache[s] || (cache[s] = getJ(`data/morph/${s}.json`).catch(e => { delete cache[s]; throw e }));
let rootsP, babsP, onayP;
const roots = () => rootsP || (rootsP = getJ('data/morph/roots.json').catch(e => { rootsP = null; throw e }));
const babs  = () => babsP  || (babsP  = getJ('data/morph/babs.json').catch(() => ({})));
const onay  = () => onayP  || (onayP  = getJ('data/morph/onay.json').catch(() => ({})));

function seg(x){ const f = {}; x[2].split('|').forEach(p => { const i = p.indexOf(':'); if(i > 0) f[p.slice(0, i)] = p.slice(i + 1); else f[p] = true }); return { t: x[0], pos: x[1], f } }

/* ---------------- harf / hareke yardımcıları ---------------- */
const BASE = /[ء-غف-يٱ]/;
const HAR = { 'َ':'a', 'ِ':'i', 'ُ':'u', 'ْ':'o', 'ۡ':'o', 'ً':'an', 'ٌ':'un', 'ٍ':'in' };
function letters(t){ const L = []; for(const ch of t){ if(BASE.test(ch)) L.push({ c: ch, v: '', sh: false }); else if(ch === 'ٔ' || ch === 'ٕ') L.push({ c: 'ء', v: '', sh: false }); else if(ch === 'ٰ') L.push({ c: 'ا', v: '', sh: false }); else if(L.length){ if(HAR[ch]) L[L.length-1].v = HAR[ch]; else if(ch === 'ّ') L[L.length-1].sh = true } } return L }
/* kelimenin son harekesi: {v, weak} — v: a i u o an un in ''; weak: sondaki harf-i illet */
function finalV(t){
  const L = letters(t); if(!L.length) return { v: '' };
  let i = L.length - 1, x = L[i];
  if(!x.v && 'اى'.includes(x.c) && i > 0 && L[i-1].v === 'an') return { v: 'an' };
  if(!x.v && 'اىوي'.includes(x.c)) return { v: '', weak: x.c };
  return { v: x.v, sh: x.sh, last: x.c };
}
const nf = c => 'أإآءؤئ'.includes(c) ? 'ء' : c === 'ى' ? 'ي' : c;
const rootL = r => [...(r || '')].map(nf);
const WEAK = 'وي';

/* ---------------- terimler ---------------- */
const ALE = { feth: 'ale’l-feth', kesr: 'ale’l-kesr', damm: 'ale’d-damm', 'sükûn': 'ale’s-sükûn' };
const ale = h => ALE[h[0]] || ('ale’l-' + h[0]);
const HN = { a: ['feth', 'الفتح'], i: ['kesr', 'الكسر'], u: ['damm', 'الضم'], o: ['sükûn', 'السكون'] };
const CASE = { NOM: ['merfû', 'مرفوع', 'ref', 'رفعه'], ACC: ['mansûb', 'منصوب', 'nasb', 'نصبه'], GEN: ['mecrûr', 'مجرور', 'cerr', 'جره'] };
const MOOD = { IND: ['merfû', 'مرفوع', 'ref', 'رفعه'], SUBJ: ['mansûb', 'منصوب', 'nasb', 'نصبه'], JUS: ['meczûm', 'مجزوم', 'cezm', 'جزمه'] };
const NTYPE = { PN: ['Alem (özel isim)', 'علم'], PRON: ['Zamir', 'ضمير'], DEM: ['İsm-i işâret', 'اسم إشارة'], REL: ['İsm-i mevsûl', 'اسم موصول'],
  T: ['Zarf-ı zaman', 'ظرف زمان'], LOC: ['Zarf-ı mekân', 'ظرف مكان'], NV: ['İsm-i fiil', 'اسم فعل'], INTG: ['İsm-i istifhâm', 'اسم استفهام'], COND: ['İsm-i şart', 'اسم شرط'] };
const PART = {
  P: ['Harf-i cer', 'حرف جر'], CONJ: ['Harf-i atf', 'حرف عطف'], SUB: ['Harf-i masdarî', 'حرف مصدري'], ACC: ['Harf-i nasb', 'حرف نصب'],
  AMD: ['Harf-i istidrâk', 'حرف استدراك'], ANS: ['Harf-i cevâb', 'حرف جواب'], AVR: ['Harf-i red‘', 'حرف ردع'], CAUS: ['Harf-i sebebiyye', 'حرف سببية'],
  CERT: ['Harf-i tahkîk', 'حرف تحقيق'], CIRC: ['Vâv-ı hâliyye', 'واو الحال'], COM: ['Vâv-ı maiyye', 'واو المعية'], EQ: ['Hemze-i tesviye', 'همزة التسوية'],
  EXH: ['Harf-i tahdîd', 'حرف تحضيض'], EXL: ['Harf-i tafsîl', 'حرف تفصيل'], EXP: ['Edât-ı istisnâ', 'أداة استثناء'], FUT: ['Harf-i istikbâl', 'حرف استقبال'],
  INC: ['Harf-i ibtidâ', 'حرف ابتداء'], INT: ['Harf-i tefsîr', 'حرف تفسير'], NEG: ['Harf-i nefy', 'حرف نفي'], PREV: ['Harf-i kâff', 'حرف كافّ'],
  PRO: ['Lâ-yı nâhiye', 'لا الناهية'], REM: ['Harf-i isti’nâf', 'حرف استئناف'], RES: ['Edât-ı hasr', 'أداة حصر'], RET: ['Harf-i idrâb', 'حرف إضراب'],
  RSLT: ['Cevâb-ı şart harfi', 'حرف واقع في جواب الشرط'], SUP: ['Harf-i zâid', 'حرف زائد'], SUR: ['Harf-i müfâcee', 'حرف فجاءة'], VOC: ['Harf-i nidâ', 'حرف نداء'],
  ATT: ['Harf-i tenbîh', 'حرف تنبيه'], DIST: ['Lâm-ı bu‘d', 'لام البعد'], ADDR: ['Harf-i hitâb', 'حرف خطاب'], INL: ['Hurûf-ı mukatta‘a', 'حروف مقطعة'],
  EMPH: ['Lâm-ı tekîd', 'لام التوكيد'], IMPV: ['Lâm-ı emr', 'لام الأمر'], PRP: ['Lâm-ı ta‘lîl', 'لام التعليل'], DET: ['Harf-i ta‘rîf', 'حرف تعريف'],
  INTG: ['Harf-i istifhâm', 'حرف استفهام'], COND: ['Harf-i şart', 'حرف شرط']
};
const INNA = { 'إِنّ': 'tekîd', 'أَنّ': 'tekîd', 'كَأَنّ': 'teşbîh', 'لٰكِنّ': 'istidrâk', 'لَكِنّ': 'istidrâk', 'لَيْت': 'temennî', 'لَعَلّ': 'tereccî' };
/* Avâmil köprüsü: âmil harflerin işi */
const AMIL = {
  'لَم': 'Hurûf-ı cevâzimdendir: muzâriyi cezmeder ve mânâsını geçmişe çevirir.',
  'لَمّا': 'Hurûf-ı cevâzimdendir: muzâriyi cezmeder; olumsuzluğun konuşma ânına kadar sürdüğünü bildirir.',
  'لَن': 'Hurûf-ı nevâsıbdandır: muzâriyi nasbeder ve olumsuzluğu geleceğe tahsis eder.',
  'أَن': 'Hurûf-ı nevâsıbdandır: muzâriyi nasbeder; fiille birlikte masdar mânâsı verir (an-ı masdariyye).',
  'كَي': 'Hurûf-ı nevâsıbdandır: muzâriyi nasbeder; sebep ve gâye bildirir.',
  'إِذَن': 'Hurûf-ı nevâsıbdandır: şartları bulununca muzâriyi nasbeder.',
  'إِنّ': 'Hurûf-ı müşebbehe bi’l-fiildendir: ismini nasb, haberini ref eder.',
  'أَنّ': 'Hurûf-ı müşebbehe bi’l-fiildendir: ismini nasb, haberini ref eder; cümleyi masdar te’vîline sokar.',
  'كَأَنّ': 'Hurûf-ı müşebbehe bi’l-fiildendir (teşbîh): ismini nasb, haberini ref eder.',
  'لٰكِنّ': 'Hurûf-ı müşebbehe bi’l-fiildendir (istidrâk): ismini nasb, haberini ref eder.',
  'لَكِنّ': 'Hurûf-ı müşebbehe bi’l-fiildendir (istidrâk): ismini nasb, haberini ref eder.',
  'لَيْت': 'Hurûf-ı müşebbehe bi’l-fiildendir (temennî): ismini nasb, haberini ref eder.',
  'لَعَلّ': 'Hurûf-ı müşebbehe bi’l-fiildendir (tereccî): ismini nasb, haberini ref eder.'
};
const AMIL_TAG = {
  P: 'Hurûf-ı cârradandır: kendinden sonraki ismi cerreder.',
  PRO: 'Muzâriyi cezmeder (nehiy).', IMPV: 'Muzâriyi cezmeder (emr-i gâib).',
  PRP: 'Muzâriyi, takdîr edilen (gizli) أَنْ ile nasbeder.',
  VOC: 'Münâdâyı nasbeder; münâdâ müfred alem veya nekre-i maksûde ise damme üzere mebnî olur.',
  FUT: 'Muzâriyi şimdiki zamandan ayırıp geleceğe tahsis eder; amel etmez.',
  CERT: 'Mâzî ile tahkîk (kesinlik) ve yakınlık, muzâri ile takrîb veya taklîl bildirir; amel etmez.'
};
const SIGA = [null,
  ['Müfred müzekker gâib', 'هُوَ'], ['Tesniye müzekker gâib', 'هُمَا'], ['Cem‘-i müzekker gâib', 'هُمْ'],
  ['Müfred müennes gâibe', 'هِيَ'], ['Tesniye müennes gâibe', 'هُمَا'], ['Cem‘-i müennes gâibe', 'هُنَّ'],
  ['Müfred müzekker muhâtab', 'أَنْتَ'], ['Tesniye müzekker muhâtab', 'أَنْتُمَا'], ['Cem‘-i müzekker muhâtab', 'أَنْتُمْ'],
  ['Müfred müennes muhâtaba', 'أَنْتِ'], ['Tesniye müennes muhâtaba', 'أَنْتُمَا'], ['Cem‘-i müennes muhâtaba', 'أَنْتُنَّ'],
  ['Nefs-i mütekellim vahdehû', 'أَنَا'], ['Nefs-i mütekellim ma‘a’l-gayr', 'نَحْنُ']];
const PERS = { '3MS':1, '3MD':2, '3D':2, '3MP':3, '3FS':4, '3FD':5, '3FP':6, '2MS':7, '2MD':8, '2D':8, '2MP':9, '2FS':10, '2FD':11, '2FP':12, '1S':13, '1P':14 };
const TAKDIR = { 1:'هُوَ', 4:'هِيَ', 7:'أَنْتَ', 13:'أَنَا', 14:'نَحْنُ' };
const BAB = [null,
  ['Nasara', 'نَصَرَ يَنْصُرُ', 'فَعَلَ يَفْعُلُ', 'a', 'u'], ['Daraba', 'ضَرَبَ يَضْرِبُ', 'فَعَلَ يَفْعِلُ', 'a', 'i'], ['Fetaha', 'فَتَحَ يَفْتَحُ', 'فَعَلَ يَفْعَلُ', 'a', 'a'],
  ['Alime', 'عَلِمَ يَعْلَمُ', 'فَعِلَ يَفْعَلُ', 'i', 'a'], ['Hasibe', 'حَسِبَ يَحْسِبُ', 'فَعِلَ يَفْعِلُ', 'i', 'i'], ['Kerume', 'كَرُمَ يَكْرُمُ', 'فَعُلَ يَفْعُلُ', 'u', 'u']];
const MEZID = { 2: ['Tef‘îl', 'فَعَّلَ يُفَعِّلُ تَفْعِيلًا'], 3: ['Mufâale', 'فَاعَلَ يُفَاعِلُ مُفَاعَلَةً'], 4: ['İf‘âl', 'أَفْعَلَ يُفْعِلُ إِفْعَالًا'],
  5: ['Tefa‘‘ul', 'تَفَعَّلَ يَتَفَعَّلُ تَفَعُّلًا'], 6: ['Tefâ‘ul', 'تَفَاعَلَ يَتَفَاعَلُ تَفَاعُلًا'], 7: ['İnfi‘âl', 'اِنْفَعَلَ يَنْفَعِلُ اِنْفِعَالًا'],
  8: ['İfti‘âl', 'اِفْتَعَلَ يَفْتَعِلُ اِفْتِعَالًا'], 9: ['İf‘ilâl', 'اِفْعَلَّ يَفْعَلُّ اِفْعِلَالًا'], 10: ['İstif‘âl', 'اِسْتَفْعَلَ يَسْتَفْعِلُ اِسْتِفْعَالًا'],
  11: ['İf‘îlâl', 'اِفْعَالَّ يَفْعَالُّ اِفْعِيلَالًا'] };

function numberOf(f){ for(const k of ['MS','MD','MP','FS','FD','FP','M','F','S','D','P']) if(f[k]) return k; return '' }
const NUM_TR = { S: 'müfred', D: 'tesniye (müsennâ)', P: 'cem‘' };
const GEN_TR = { M: 'müzekker', F: 'müennes' };
function numGen(f){ const k = numberOf(f); if(!k) return ''; const g = k.length === 2 ? k[0] : (k === 'M' || k === 'F' ? k : ''); const n = k.length === 2 ? k[1] : (k === 'S' || k === 'D' || k === 'P' ? k : ''); return [n && NUM_TR[n], g && GEN_TR[g]].filter(Boolean).join(', ') }

/* kökün sınıfı (Binâ / Maksûd) */
function rootClass(r){
  const R = rootL(r); if(R.length === 4) return R.includes('و') || R.includes('ي') ? 'Rubâî (mu‘tel)' : 'Rubâî';
  if(R.length !== 3) return '';
  const [a, b, c] = R, W = x => WEAK.includes(x);
  const cls = [];
  if(W(a) && W(c)) cls.push('Lefîf-i mefrûk');
  else if(W(b) && W(c)) cls.push('Lefîf-i makrûn');
  else if(W(a)) cls.push(`Misâl (${a === 'و' ? 'vâvî' : 'yâî'})`);
  else if(W(b)) cls.push(`Ecvef (${b === 'و' ? 'vâvî' : 'yâî'})`);
  else if(W(c)) cls.push(`Nâkıs (${c === 'و' ? 'vâvî' : 'yâî'})`);
  if(b === c && !W(b)) cls.push('Muzâaf');
  if(a === 'ء') cls.push('Mehmûzü’l-fâ'); if(b === 'ء') cls.push('Mehmûzü’l-ayn'); if(c === 'ء') cls.push('Mehmûzü’l-lâm');
  return cls.length ? cls.join(' · ') : 'Sahîh (sâlim)';
}
const isSalim = r => { const R = rootL(r); return R.length === 3 && !R.some(x => WEAK.includes(x) || x === 'ء') && R[1] !== R[2] };

/* ---------------- Emsile motoru (sâlim kökler) ---------------- */
const F = 'َ', Ki = 'ِ', D = 'ُ', S = 'ْ', SH = 'ّ';
const V = { a: F, i: Ki, u: D };
const MAZI_SUF = [null, F, F+'ا', D+'وا', F+'تْ', F+'تَا', S+'نَ', S+'تَ', S+'تُمَا', S+'تُمْ', S+'تِ', S+'تُمَا', S+'تُنَّ', S+'تُ', S+'نَا'];
const MUZ_PRE = [null, 'ي','ي','ي','ت','ت','ي','ت','ت','ت','ت','ت','ت','أ','ن'];
const MUZ_SUF = [null, D, F+'انِ', D+'ونَ', D, F+'انِ', S+'نَ', D, F+'انِ', D+'ونَ', Ki+'ينَ', F+'انِ', S+'نَ', D, D];
const EMR_SUF = [S, F+'ا', D+'وا', Ki+'ي', F+'ا', S+'نَ'];
function join(stem, suf){ const last = stem.slice(-1);
  if(suf[0] === S && suf[1] === last && (last === 'ن' || last === 'ت')) return stem + SH + suf.slice(2);
  return stem + suf }
function forms(r, vf, pv, iv){
  const [a, b, c] = [...r];
  const T = {
    1: [a+F+b+V[pv]+c, a+S+b+V[iv]+c, F, (iv === 'u' ? 'اُ' : 'اِ')+a+S+b+V[iv]+c, a+F+'ا'+b+Ki+c, 'مَ'+a+S+b+D+'و'+c],
    2: [a+F+b+SH+F+c, a+F+b+SH+Ki+c, D, a+F+b+SH+Ki+c, 'مُ'+a+F+b+SH+Ki+c, 'مُ'+a+F+b+SH+F+c, 'تَ'+a+S+b+Ki+'ي'+c+'ٌ'],
    3: [a+F+'ا'+b+F+c, a+F+'ا'+b+Ki+c, D, a+F+'ا'+b+Ki+c, 'مُ'+a+F+'ا'+b+Ki+c, 'مُ'+a+F+'ا'+b+F+c, 'مُ'+a+F+'ا'+b+F+c+'َةٌ'],
    4: ['أَ'+a+S+b+F+c, a+S+b+Ki+c, D, 'أَ'+a+S+b+Ki+c, 'مُ'+a+S+b+Ki+c, 'مُ'+a+S+b+F+c, 'إِ'+a+S+b+F+'ا'+c+'ٌ'],
    5: ['تَ'+a+F+b+SH+F+c, 'تَ'+a+F+b+SH+F+c, F, 'تَ'+a+F+b+SH+F+c, 'مُتَ'+a+F+b+SH+Ki+c, 'مُتَ'+a+F+b+SH+F+c, 'تَ'+a+F+b+SH+D+c+'ٌ'],
    6: ['تَ'+a+F+'ا'+b+F+c, 'تَ'+a+F+'ا'+b+F+c, F, 'تَ'+a+F+'ا'+b+F+c, 'مُتَ'+a+F+'ا'+b+Ki+c, 'مُتَ'+a+F+'ا'+b+F+c, 'تَ'+a+F+'ا'+b+D+c+'ٌ'],
    7: ['اِنْ'+a+F+b+F+c, 'نْ'+a+F+b+Ki+c, F, 'اِنْ'+a+F+b+Ki+c, 'مُنْ'+a+F+b+Ki+c, 'مُنْ'+a+F+b+F+c, 'اِنْ'+a+Ki+b+F+'ا'+c+'ٌ'],
    8: ['اِ'+a+S+'تَ'+b+F+c, a+S+'تَ'+b+Ki+c, F, 'اِ'+a+S+'تَ'+b+Ki+c, 'مُ'+a+S+'تَ'+b+Ki+c, 'مُ'+a+S+'تَ'+b+F+c, 'اِ'+a+S+'تِ'+b+F+'ا'+c+'ٌ'],
    10: ['اِسْتَ'+a+S+b+F+c, 'سْتَ'+a+S+b+Ki+c, F, 'اِسْتَ'+a+S+b+Ki+c, 'مُسْتَ'+a+S+b+Ki+c, 'مُسْتَ'+a+S+b+F+c, 'اِسْتِ'+a+S+b+F+'ا'+c+'ٌ']
  }[vf];
  if(!T) return null;
  const [mz, mu, pre, em, fa, mf, ms] = T;
  return {
    mazi: SIGA.map((_, i) => i && join(mz, MAZI_SUF[i])),
    muz: SIGA.map((_, i) => i && (MUZ_PRE[i] + pre + join(mu, MUZ_SUF[i]))),
    emr: EMR_SUF.map(s => join(em, s)),
    fail: fa + 'ٌ', meful: (vf === 1 ? mf : mf) + 'ٌ', masdar: ms || ''
  };
}
const IFTIAL_BAD = 'صضطظدذزثو';

/* ---------------- çözümleme ---------------- */
function wordInfo(W, i){ return W[i] ? W[i].map(seg) : null }
function mainSeg(S){ return S.find(x => x.pos === 'V') || S.find(x => x.pos === 'N' && !x.f.SUFF && x.f.PREF !== true) || S.find(x => !x.f.PREF) || S[0] }

function sarf(S, B){
  const m = mainSeg(S), f = m.f, rows = [];
  const row = (k, v, ar) => rows.push(`<tr><th>${k}</th><td>${v}${ar ? ` <span class="kar" lang="ar">${E(ar)}</span>` : ''}</td></tr>`);
  if(m.pos === 'V'){
    const t = f.PERF ? ['Fiil-i mâzî', 'فعل ماض'] : f.IMPF ? ['Fiil-i muzâri‘', 'فعل مضارع'] : ['Fiil-i emr', 'فعل أمر'];
    row('Kelime', t[0] + (f.PASS ? ' — meçhûl' : ' — ma‘lûm'), t[1] + (f.PASS ? ' مبني للمجهول' : ''));
  } else if(m.pos === 'N'){
    let t = ['İsim', 'اسم']; for(const k in NTYPE) if(f[k]){ t = NTYPE[k]; break }
    if(f.ACT_PCPL) t = ['İsm-i fâil', 'اسم فاعل']; else if(f.PASS_PCPL) t = ['İsm-i mef‘ûl', 'اسم مفعول']; else if(f.VN) t = ['Masdar', 'مصدر'];
    row('Kelime', t[0] + (f.ADJ ? ' (sıfat/na‘t olarak)' : ''), t[1]);
  } else {
    const p = Object.keys(PART).find(k => f[k]) || ''; row('Kelime', 'Harf' + (p ? ' — ' + PART[p][0] : ''), p ? PART[p][1] : 'حرف');
  }
  if(f.ROOT){ row('Kök', `<b class="kar" lang="ar">${E([...f.ROOT].join(' '))}</b>`); row('Kök sınıfı', rootClass(f.ROOT)) }
  if(f.LEM) row('Sözlük şekli', `<span class="kar" lang="ar">${E(f.LEM)}</span>`);
  const vf = +f.VF || 0;
  if(vf === 1 || (f.ROOT && !vf && m.pos === 'V' && rootL(f.ROOT).length === 3)){
    const b = f.BAB ? +f.BAB.replace('?', '') : 0;
    if(b) row('Bâb', `Sülâsî mücerred · <b>${BAB[b][0]} bâbı</b> (${b}. bâb) <span class="kar" lang="ar">${BAB[b][1]}</span>${f.BAB.includes('?') ? ' <small class="tah">tahmin</small>' : ''}`);
    else row('Bâb', 'Sülâsî mücerred <small class="tah">bâbı tespit edilemedi</small>');
  } else if(vf > 1 && MEZID[vf]) row('Bâb', `Sülâsî mezîd · <b>${MEZID[vf][0]} bâbı</b> <span class="kar" lang="ar">${MEZID[vf][1]}</span>`);
  else if(f.ROOT && rootL(f.ROOT).length === 4 && m.pos === 'V') row('Bâb', 'Rubâî');
  if(m.pos === 'V'){
    const p = Object.keys(PERS).find(k => f[k]); let si = p ? PERS[p] : 0;
    if(si === 2 && f.IMPF && /^ت/.test(m.t.replace(/[^ء-ي]/g, ''))) si = 5;
    if(si === 2 && f.PERF && /تا$/.test((m.t + (S[S.indexOf(m) + 1] || { t: '' }).t).replace(/[^ء-ي]/g, ''))) si = 5;
    if(si) row('Sîga', `${SIGA[si][0]} <span class="kar" lang="ar">(${SIGA[si][1]})</span>`);
    if(f.MOOD) row('İ‘râb hâli', MOOD[f.MOOD][0], MOOD[f.MOOD][1]);
    if(f.FAM) row('Ailesi', f.FAM.startsWith('كَا') && f.FAM.includes('د') ? 'Ef‘âl-i mukârebe' : 'Ef‘âl-i nâkısa (kâne ve kardeşleri)');
  } else if(m.pos === 'N'){
    const ng = numGen(f); if(ng) row('Sayı / cinsiyet', ng);
    if(m.f.CASE || f.NOM || f.ACC || f.GEN){ const c = f.NOM ? 'NOM' : f.ACC ? 'ACC' : 'GEN'; row('İ‘râb hâli', CASE[c][0], CASE[c][1]) }
    const det = S.some(x => x.f.DET); if(det || f.INDEF || f.PN) row('Belirlilik', det ? 'Ma‘rife (ال ile)' : f.PN ? 'Ma‘rife (alem)' : 'Nekre (tenvînli)');
  }
  return { rows: rows.join(''), m, vf };
}

function emsileTable(m, vf, B){
  const f = m.f; if(!f.ROOT || !vf) return '';
  const R = rootL(f.ROOT), tense = f.PERF ? 'mazi' : f.IMPF ? 'muz' : f.IMPV ? 'emr' : '';
  const p = Object.keys(PERS).find(k => f[k]); let si = p ? PERS[p] : 0;
  if(R.length !== 3) return '';
  if(!isSalim(f.ROOT)) return `<p class="knote">Bu kök <b>${rootClass(f.ROOT)}</b> sınıfındandır. Bu tür fiillerin çekiminde i‘lâl/idgâm/hemze kuralları devreye girer; i‘lâlli çekim tabloları sonraki aşamada (Binâ ve Maksûd dersleriyle) eklenecek.</p>`;
  if(vf === 8 && IFTIAL_BAD.includes(R[0])) return `<p class="knote">İfti‘âl bâbında fâ’ü’l-fiil <b class="kar" lang="ar">${R[0]}</b> olunca bâbın ت harfi değişir (ibdâl/idgâm); bu tablo sonraki aşamada.</p>`;
  let pv = 'a', iv = 'a';
  if(vf === 1){ const b = f.BAB ? +f.BAB.replace('?', '') : 0; if(!b) return ''; pv = BAB[b][3]; iv = BAB[b][4] }
  const T = forms(R.join(''), vf, pv, iv); if(!T) return '';
  const vn = vf === 1 ? (B[f.ROOT] && B[f.ROOT][2]) : T.masdar;
  const cell = (x, on) => `<td class="${on ? 'on' : ''}" lang="ar">${E(x)}</td>`;
  let h = `<div class="kems"><div class="kemh">Emsile-i muhtelife</div><div class="kemm" lang="ar">${E(T.mazi[1])} · ${E(T.muz[1])}${vn ? ' · ' + E(vn) : ''} · ${E(T.fail)} · ${E(T.meful)}</div>`;
  h += `<table class="kemt"><thead><tr><th>Sîga</th><th>Mâzî</th><th>Muzâri‘</th></tr></thead><tbody>`;
  for(let i = 1; i <= 14; i++) h += `<tr><th>${SIGA[i][0]} <span lang="ar">${SIGA[i][1]}</span></th>${cell(T.mazi[i], tense === 'mazi' && si === i && !f.PASS)}${cell(T.muz[i], tense === 'muz' && si === i && !f.PASS)}</tr>`;
  h += `</tbody></table><table class="kemt"><thead><tr><th>Emr-i hâzır</th><th></th></tr></thead><tbody>`;
  const EM = [7, 8, 9, 10, 11, 12];
  EM.forEach((s, i) => { if(i === 4) return; h += `<tr><th>${SIGA[s][0]} <span lang="ar">${SIGA[s][1]}</span></th>${cell(T.emr[i], tense === 'emr' && si === s)}</tr>` });
  h += `</tbody></table><p class="knote">Kök ve bâbdan kural ile üretildi (ma‘lûm). ${f.PASS ? 'Bu kelime meçhûl olduğu için tabloda işaretlenmedi.' : ''}</p></div>`;
  return h;
}

/* ---- nahiv ---- */
function lastWeakRoot(f){ const R = rootL(f.ROOT); return R.length && WEAK.includes(R[R.length - 1]) }
function verbSubjectSuffix(S, i){ // fiilden sonraki ilk zamir fâil zamiri mi?
  const v = S[i].f, nx = S[i+1]; if(!nx || !nx.f.PRON) return false;
  const p = Object.keys(PERS).find(k => v[k]);
  if(v.PERF) return p && p !== '3MS' && p !== '3FS';
  return p && /(D|MP|FP|2FS)$/.test(p) && !/^1/.test(p);
}
function ira(ctx){
  const { S, prevW, ayah, wi } = ctx, out = [];
  const add = (seg, tr, ar, note) => out.push({ seg, tr, ar, note });
  const verbIdx = S.findIndex(x => x.pos === 'V');
  S.forEach((x, i) => {
    const f = x.f, fv = finalV(x.t);
    const mebniV = fv.v && HN[fv.v[0] === 'a' || fv.v[0] === 'i' || fv.v[0] === 'u' ? fv.v[0] : 'o'] || HN.o;
    if(x.pos === 'P'){
      const tag = Object.keys(PART).find(k => f[k] && k !== 'PREF' && k !== 'SUFF') || 'P';
      let nm = PART[tag] || ['Harf', 'حرف'];
      if(tag === 'ACC' && INNA[f.LEM]) nm = [`Harf-i tekîd ve nasb (${INNA[f.LEM]})`, f.LEM === 'إِنّ' || f.LEM === 'أَنّ' ? 'حرف توكيد ونصب' : 'حرف ناسخ'];
      if(tag === 'EMPH' && f.LEM === 'ن') nm = ['Nûn-ı tekîd', 'نون التوكيد'];
      const mb = tag === 'DET' ? '' : `, mebnî ${ale(mebniV)}`;
      add(x.t, `${nm[0]}${mb}; i‘râbtan mahalli yoktur.`, `${nm[1]}${tag === 'DET' ? '' : ' مبني على ' + mebniV[1]}، لا محل له من الإعراب.`, AMIL[f.LEM] || AMIL_TAG[tag] || '');
      return;
    }
    if(x.pos === 'V'){
      const fam = f.FAM ? (f.FAM.includes('د') ? 'ef‘âl-i mukârebeden' : 'ef‘âl-i nâkısadan') : '';
      const p = Object.keys(PERS).find(k => f[k]); const si = p ? PERS[p] : 0;
      const subjSuf = verbSubjectSuffix(S, i);
      if(f.PERF){
        let v = fv.v ? (fv.v[0] === 'o' ? 'o' : fv.v[0]) : 'a', muk = !fv.v && fv.weak;
        if(p === '3FS' || p === '3FD') v = 'a';
        const tr = `Fiil-i mâzî${f.PASS ? ' (meçhûl)' : ''}${fam ? ', ' + fam : ''}; mebnî ${ale(HN[v])}${muk ? ' (mukadder)' : ''}.`;
        const ar = `فعل ماض${f.PASS ? ' مبني للمجهول' : ''}${f.FAM ? ' ناقص' : ''} مبني على ${HN[v][1]}${muk ? ' المقدر' : ''}.`;
        add(x.t, tr, ar, (p === '3FS' ? 'Sonundaki ت, te’nîs (müenneslik) harfidir; i‘râbtan mahalli yoktur. ' : '') + (f.FAM ? 'İsmini ref, haberini nasbeder.' : ''));
      } else {
        const em = S.some(y => y.f.EMPH && y.f.SUFF), nisa = p && /FP$/.test(p) && !/^1/.test(p);
        const hamse = subjSuf && !nisa;
        if(f.IMPV){
          let tr, ar;
          if(hamse){ tr = 'Fiil-i emr; hazf-ı nûn üzere mebnî.'; ar = 'فعل أمر مبني على حذف النون.' }
          else if(em){ tr = 'Fiil-i emr; nûn-ı tekîd sebebiyle feth üzere mebnî.'; ar = 'فعل أمر مبني على الفتح لاتصاله بنون التوكيد.' }
          else if(nisa){ tr = 'Fiil-i emr; sükûn üzere mebnî (nûn-ı nisve ile).'; ar = 'فعل أمر مبني على السكون لاتصاله بنون النسوة.' }
          else if(lastWeakRoot(f) && !/[وي]$/.test(x.t.replace(/[^ء-ي]/g, ''))){ tr = 'Fiil-i emr; harf-i illetin hazfı üzere mebnî.'; ar = 'فعل أمر مبني على حذف حرف العلة.' }
          else { tr = 'Fiil-i emr; sükûn üzere mebnî' + (fv.v && fv.v !== 'o' ? ' (iltikâ-i sâkineyn sebebiyle harekelendi)' : '') + '.'; ar = 'فعل أمر مبني على السكون.' }
          add(x.t, tr, ar, si === 7 ? 'Fâili, vücûben gizli (müstetir) zamirdir; takdîri أَنْتَ.' : '');
        } else {
          const M = MOOD[f.MOOD] || MOOD.IND; let tr, ar, alT, alA;
          if(em){ tr = `Fiil-i muzâri‘${f.PASS ? ' (meçhûl)' : ''}; nûn-ı tekîd ile bitiştiği için feth üzere mebnî.`; ar = 'فعل مضارع مبني على الفتح لاتصاله بنون التوكيد.' }
          else if(nisa){ tr = 'Fiil-i muzâri‘; nûn-ı nisve ile bitiştiği için sükûn üzere mebnî.'; ar = 'فعل مضارع مبني على السكون لاتصاله بنون النسوة.' }
          else {
            if(hamse){ alT = f.MOOD === 'IND' ? 'nûnun sübûtu' : 'nûnun hazfı'; alA = f.MOOD === 'IND' ? 'ثبوت النون' : 'حذف النون'; alT += ' (ef‘âl-i hamsedendir)'; alA += ' لأنه من الأفعال الخمسة' }
            else if(f.MOOD === 'JUS'){
              if(lastWeakRoot(f) && !fv.weak){ alT = 'harf-i illetin hazfı'; alA = 'حذف حرف العلة' }
              else if(fv.v === 'o' || !fv.v){ alT = 'sükûn'; alA = 'السكون' }
              else { alT = 'sükûn (iltikâ-i sâkineyn veya idgâm sebebiyle harekelendi)'; alA = 'السكون، وحُرِّك لالتقاء الساكنين' }
            } else {
              const want = f.MOOD === 'SUBJ' ? 'a' : 'u', nm = want === 'a' ? ['fetha', 'الفتحة'] : ['damme', 'الضمة'];
              if(fv.v === want){ alT = 'zâhir ' + nm[0]; alA = nm[1] + ' الظاهرة' }
              else { alT = 'mukadder ' + nm[0] + (fv.weak === 'ا' || fv.weak === 'ى' ? ' (taazzur)' : ' (sıklet)'); alA = nm[1] + ' المقدرة' }
            }
            tr = `Fiil-i muzâri‘${f.PASS ? ' (meçhûl)' : ''}${fam ? ', ' + fam : ''}; ${M[0]}, ${M[2]} alâmeti ${alT}.`;
            ar = `فعل مضارع${f.PASS ? ' مبني للمجهول' : ''}${f.FAM ? ' ناقص' : ''} ${M[1]} وعلامة ${M[3]} ${alA}.`;
          }
          add(x.t, tr, ar, f.FAM ? 'İsmini ref, haberini nasbeder.' : '');
        }
      }
      if(!subjSuf && !f.IMPV && TAKDIR[si]) add('', `${f.PASS ? 'Nâib-i fâili' : f.FAM ? 'İsmi' : 'Fâili'} gizli (müstetir) zamirdir; takdîri ${TAKDIR[si]}${si === 1 || si === 4 ? ' (cümlede açık bir isim gelmiyorsa)' : ''}.`, `${f.PASS ? 'ونائب الفاعل' : f.FAM ? 'واسمه' : 'والفاعل'} ضمير مستتر تقديره ${TAKDIR[si]}.`, '');
      return;
    }
    // isimler
    if(f.PRON){
      const prev = S[i-1];
      let role, rar;
      if(prev && prev.pos === 'V' && i - 1 === verbIdx && verbSubjectSuffix(S, i - 1)){
        const pf = prev.f, rl = pf.PASS ? ['mahallen merfû, nâib-i fâil', 'في محل رفع نائب فاعل'] : pf.FAM ? ['mahallen merfû, fiilin ismi', 'في محل رفع اسمه'] : ['mahallen merfû, fâil', 'في محل رفع فاعل'];
        const sk = x.t.replace(/[^ء-ي]/g, ''), h0 = letters(x.t)[0] || { v: '' };
        const nm = sk[0] === 'و' ? ['Vâv-ı cemâat', 'واو الجماعة', 'o'] : sk[0] === 'ا' ? ['Elif-i tesniye', 'ألف الاثنين', 'o'] : sk[0] === 'ي' ? ['Yâ-yı muhâtaba', 'ياء المخاطبة', 'o']
          : sk === 'نا' ? ['“Nâ” zamiri', '«نا» الفاعلين', 'o'] : sk[0] === 'ن' ? ['Nûn-ı nisve', 'نون النسوة', 'a'] : ['Tâ-yı fâil', 'تاء الفاعل', (h0.v || 'a')[0]];
        const hv = HN[nm[2]] || HN.o;
        add(x.t, `${nm[0]} — muttasıl zamir, mebnî ${ale(hv)}; ${rl[0]}.` + (/^(ون|ان|ين)$/.test(sk) ? ' Sondaki ن, i‘râb alâmetidir (nûnun sübûtu).' : sk === 'وا' ? ' Sondaki elif, elif-i fârikadır.' : ''),
          `${nm[1]} ضمير متصل مبني على ${hv[1]} ${rl[1]}.`, '');
        return;
      }
      if(f.LEM === 'إِيّا'){ add(x.t, 'Munfasıl nasb zamiri إِيَّا, mebnî ale’s-sükûn; mahallen mansûb, mef‘ûlün bih (fiilden önce gelmiş: hasr ifade eder). Sonundaki ك, harf-i hitâbdır.', 'إيّا: ضمير منفصل مبني على السكون في محل نصب مفعول به مقدم، والكاف حرف خطاب.', ''); return }
      if(prev && (prev.pos === 'V' || (prev.f.PRON && S[i-2] && S[i-2].pos === 'V'))) role = ['mahallen mansûb, mef‘ûlün bih', 'في محل نصب مفعول به'];
      else if(prev && prev.pos === 'P' && prev.f.P) role = ['harf-i cer ile mahallen mecrûr', 'في محل جر بحرف الجر'];
      else if(prev && prev.pos === 'P' && prev.f.ACC) role = ['mahallen mansûb, ism-i ' + (prev.f.LEM || 'inne'), 'في محل نصب اسم ' + (prev.f.LEM || 'إن')];
      else if(prev && prev.pos === 'N') role = ['mahallen mecrûr, muzâfun ileyh', 'في محل جر مضاف إليه'];
      else if(f.LEM === 'إِيّا') role = ['mahallen mansûb (mef‘ûlün bih)', 'في محل نصب مفعول به'];
      else role = ['cümledeki yerine göre mahallen i‘râb alır', ''];
      const kind = i > 0 ? ['Muttasıl zamir', 'ضمير متصل'] : ['Munfasıl zamir', 'ضمير منفصل'];
      add(x.t, `${kind[0]}, mebnî ${ale(mebniV)}; ${role[0]}.`, `${kind[1]} مبني على ${mebniV[1]}${role[1] ? ' ' + role[1] : ''}.`, '');
      return;
    }
    if(f.DEM || f.REL){
      const nm = f.DEM ? NTYPE.DEM : NTYPE.REL, c = f.NOM ? 'NOM' : f.ACC ? 'ACC' : f.GEN ? 'GEN' : '';
      if(c && (f.MD || f.FD || f.D)) add(x.t, `${nm[0]} (tesniye); ${CASE[c][0]}, ${CASE[c][2]} alâmeti ${c === 'NOM' ? 'elif' : 'yâ'}.`, `${nm[1]} ${CASE[c][1]} وعلامة ${CASE[c][3]} ${c === 'NOM' ? 'الألف' : 'الياء'}.`, '');
      else add(x.t, `${nm[0]}, mebnî ${ale(mebniV)}; mahalli i‘râbı cümledeki yerine göredir.`, `${nm[1]} مبني على ${mebniV[1]}.`, '');
      return;
    }
    const c = f.NOM ? 'NOM' : f.ACC ? 'ACC' : f.GEN ? 'GEN' : '';
    if(!c){ add(x.t, (f.INL ? 'Hurûf-ı mukatta‘a' : 'İsim') + '; mebnî.', f.INL ? 'حروف مقطعة.' : 'اسم مبني.', ''); return }
    const pvS = S.slice(0, i).reverse().find(y => !y.f.DET);
    if(f.LEM === 'أَيّ' && pvS && pvS.f.VOC){ add(x.t, 'Münâdâ (nekre-i maksûde), damme üzere mebnî; mahallen mansûb. Sonraki ها, harf-i tenbîhtir.', 'منادى نكرة مقصودة مبني على الضم في محل نصب.', ''); return }
    const lw = prevW && prevW[prevW.length - 1];
    if(c === 'ACC' && !S.some(y => y.f.DET || y.f.PRON) && lw && lw.f.NEG && lw.f.LEM === 'لا' && fv.v === 'a'){
      add(x.t, 'Lâ-yı nâfiye li’l-cinsin ismi (muhtemel); feth üzere mebnî, mahallen mansûb.', 'اسم «لا» النافية للجنس مبني على الفتح في محل نصب.', 'Lâ-yı nâfiye li’l-cins, inne gibi amel eder: ismini nasb, haberini ref eder; ismi müfred nekre ise feth üzere mebnî olur.'); return }
    const C = CASE[c], num = numberOf(f), skel = x.t.replace(/[^ء-يٰ]/g, '').replace(/ٰ/g, 'ا');
    const R = rootL(f.ROOT), lastR = R[R.length - 1];
    let alT, alA;
    const lemS = (f.LEM || '').replace(/[^ء-ي]/g, '');
    if(/D$/.test(num) || num === 'D'){ alT = c === 'NOM' ? 'elif (müsennâdır)' : 'yâ (müsennâdır)'; alA = (c === 'NOM' ? 'الألف' : 'الياء') + ' لأنه مثنى' }
    else if(num === 'MP' && (/(ون|ين)$/.test(skel) && lastR !== 'ن' || /[وي]$/.test(skel) && !WEAK.includes(lastR))){ alT = c === 'NOM' ? 'vâv (cem‘-i müzekker sâlimdir)' : 'yâ (cem‘-i müzekker sâlimdir)'; alA = (c === 'NOM' ? 'الواو' : 'الياء') + ' لأنه جمع مذكر سالم' }
    else if(['اب', 'اخ', 'ذو', 'فو', 'حم'].includes(lemS.replace(/^[أإآ]/, 'ا')) && /[واي]$/.test(skel) && !/MP|D/.test(num)){ alT = { NOM: 'vâv', ACC: 'elif', GEN: 'yâ' }[c] + ' (esmâ-i hamsedendir)'; alA = { NOM: 'الواو', ACC: 'الألف', GEN: 'الياء' }[c] + ' لأنه من الأسماء الخمسة' }
    else if(num === 'FP' && /ات$/.test(skel) && lastR !== 'ت' && c === 'ACC'){ alT = 'kesre (cem‘-i müennes sâlimde fethaya niyâbeten)'; alA = 'الكسرة نيابة عن الفتحة لأنه جمع مؤنث سالم' }
    else {
      const want = { NOM: 'u', ACC: 'a', GEN: 'i' }[c], nm = { u: ['damme', 'الضمة'], a: ['fetha', 'الفتحة'], i: ['kesre', 'الكسرة'] }[want];
      const nx = S[i+1];
      if(nx && nx.f.PRON && nx.f['1S'] && c !== 'GEN'){ alT = `mukadder ${nm[0]} (mahal, mütekellim yâsına münâsib hareke ile meşgul)`; alA = `${nm[1]} المقدرة منع من ظهورها اشتغال المحل بحركة المناسبة` }
      else if(fv.v && fv.v[0] === want[0]){ alT = 'zâhir ' + nm[0]; alA = nm[1] + ' الظاهرة' }
      else if(c === 'GEN' && fv.v === 'a'){ alT = 'kesreye niyâbeten fetha (gayr-i munsarıftır)'; alA = 'الفتحة نيابة عن الكسرة لأنه ممنوع من الصرف' }
      else if(!fv.v && (fv.weak === 'ا' || fv.weak === 'ى')){ alT = `mukadder ${nm[0]} (taazzur)`; alA = `${nm[1]} المقدرة للتعذر` }
      else if(!fv.v && fv.weak === 'ي'){ alT = `mukadder ${nm[0]} (sıklet)`; alA = `${nm[1]} المقدرة للثقل` }
      else { alT = nm[0]; alA = nm[1] }
    }
    // muhtemel görev (dikkatli, işaretli)
    let role = '', roleA = '';
    const prevSeg = S.slice(0, i).reverse().find(y => !y.f.DET) || (prevW && prevW[prevW.length - 1]);
    if(c === 'GEN' && prevSeg && prevSeg.pos === 'P' && prevSeg.f.P){ role = 'harf-i cer ile'; roleA = `بـ«${prevSeg.t}»` }
    else if(f.ADJ){ role = 'na‘t (sıfat), mevsûfuna tâbi'; roleA = 'نعت' }
    else if(c === 'GEN' && prevW && !S.some(y => y.f.DET)){ /* nothing */ }
    if(!role && c === 'GEN' && prevW){ const pm = prevW.find(y => y.pos === 'N' && !y.f.PRON); const pv = pm && finalV(pm.t).v;
      if(pm && !pm.f.PN && !prevW.some(y => y.f.DET) && !(pv === 'an' || pv === 'un' || pv === 'in') && !pm.f.ADJ && prevW.length === prevW.indexOf(pm) + 1){ role = 'muzâfun ileyh (muhtemel)'; roleA = 'مضاف إليه' } }
    if(!role && c === 'ACC' && (f.T || f.LOC)){ role = 'zarf, mef‘ûlün fîh'; roleA = 'مفعول فيه' }
    if(!role && c === 'ACC' && f.VN && ctx.prevVerbRoot && ctx.prevVerbRoot === f.ROOT){ role = 'mef‘ûl-i mutlak (muhtemel)'; roleA = 'مفعول مطلق' }
    if(!role && c === 'ACC' && prevW && prevW.some(y => y.pos === 'P' && y.f.ACC && INNA[y.f.LEM]) && !prevW.some(y => y.f.PRON)){ role = `ism-i ${prevW.find(y => y.f.ACC).f.LEM} (muhtemel)`; roleA = 'اسم ' + prevW.find(y => y.f.ACC).f.LEM }
    if(!role && c === 'NOM' && ctx.fail){ role = ctx.fail + ' (muhtemel)'; roleA = { 'fâil': 'فاعل', 'nâib-i fâil': 'نائب فاعل', 'ism-i kâne': 'اسم كان' }[ctx.fail] || '' }
    const title = f.PN ? 'Alem' : f.VN ? 'Masdar' : f.ACT_PCPL ? 'İsm-i fâil' : f.PASS_PCPL ? 'İsm-i mef‘ûl' : 'İsim';
    const titleA = f.PN ? 'اسم علم' : f.VN ? 'مصدر' : f.ACT_PCPL ? 'اسم فاعل' : f.PASS_PCPL ? 'اسم مفعول' : 'اسم';
    add(x.t, `${title}${role ? ' — ' + role : ''}; ${C[0]}, ${C[2]} alâmeti ${alT}.`, `${roleA && !roleA.startsWith('بـ') ? roleA : titleA} ${C[1]}${roleA.startsWith('بـ') ? ' ' + roleA : ''} وعلامة ${C[3]} ${alA}.`,
      role ? '' : 'Cümledeki görevi (mübtedâ, haber, mef‘ûl, hâl…) için âyetin tam i‘râbına bakınız.');
  });
  return out;
}

/* fâil adayı: önceki fiil gizli zamirliyse ve aradaki kelimelerde merfû isim yoksa */
function failCtx(A, wi){
  for(let j = wi - 1; j >= 0 && j >= wi - 4; j--){
    const S = A[j].map(seg), v = S.find(x => x.pos === 'V');
    if(v){ const p = Object.keys(PERS).find(k => v.f[k]); if((p === '3MS' || p === '3FS') && !v.f.IMPV && !S.some(x => x.f.PRON && x.f.SUFF && S.indexOf(x) > S.indexOf(v)))
        return v.f.PASS ? 'nâib-i fâil' : v.f.FAM ? 'ism-i kâne' : 'fâil';
      return '' }
    if(S.some(x => x.f.NOM || x.pos === 'V')) return '';
  }
  return '';
}
function prevVerbRoot(A, wi){ for(let j = wi - 1; j >= 0 && j >= wi - 3; j--){ const v = A[j].map(seg).find(x => x.pos === 'V'); if(v) return v.f.ROOT } return '' }

/* ---------------- arayüz ---------------- */
let ov, cur = null;
const MODE = () => store.get('mihrab.kwMode', 'sarf');
function ensure(){
  if(ov) return;
  ov = document.createElement('div'); ov.id = 'kwOv'; ov.className = 'kwov hide';
  ov.innerHTML = `<div class="kws" role="dialog" aria-modal="true" aria-labelledby="kwW">
    <div class="kwh"><button class="kwx" data-k="next" title="Sonraki kelime" aria-label="Sonraki kelime">‹</button><div class="kwref" id="kwRef"></div><button class="kwx" data-k="prev" title="Önceki kelime" aria-label="Önceki kelime">›</button><button class="kwx kwc" data-k="close" aria-label="Kapat">✕</button></div>
    <div class="kww" id="kwW" lang="ar"></div><div class="kwsg" id="kwSg"></div>
    <div class="kwtab" role="tablist"><button data-m="sarf" role="tab">Sarf <i lang="ar">صرف</i></button><button data-m="nahiv" role="tab">Nahiv · İ‘râb <i lang="ar">إعراب</i></button></div>
    <div class="kwb" id="kwB"></div>
    <div class="kwf"><button class="pill" data-k="irab">Âyetin tam i‘râbı ›</button><button class="pill" data-k="kok">Kökün Kur’an’daki yerleri</button><a class="pill" id="kwBug" target="_blank" rel="noopener">Hata bildir</a></div>
  </div>`;
  document.body.appendChild(ov);
  ov.addEventListener('click', e => {
    if(e.target === ov) return K.close();
    const b = e.target.closest('[data-k],[data-m],[data-go]'); if(!b) return;
    if(b.dataset.m){ store.set('mihrab.kwMode', b.dataset.m); show(); return }
    if(b.dataset.go){ const [s, a, w] = b.dataset.go.split(':').map(Number); K.close(); K.jump(s, a, w - 1); return }
    const k = b.dataset.k;
    if(k === 'close') K.close();
    else if(k === 'next') step(1); else if(k === 'prev') step(-1);
    else if(k === 'irab'){ const s = cur.s, a = cur.a; K.close(); if(K.cfg.irab) K.cfg.irab(s, a) }
    else if(k === 'kok') kokYerleri();
  });
  document.addEventListener('keydown', e => { if(!cur || ov.classList.contains('hide')) return;
    if(e.key === 'Escape') K.close(); else if(e.key === 'ArrowLeft') step(1); else if(e.key === 'ArrowRight') step(-1) });
}
function step(d){ if(!cur) return; const n = cur.w + d; if(n < 0 || n >= cur.A.length) return; cur.w = n; mark(); show() }
K.close = () => { if(ov) ov.classList.add('hide'); unmark(); cur = null; document.documentElement.classList.remove('kwlock') };

K.open = async (s, a, w) => {
  ensure();
  let d; try{ d = await K.data(s) }catch(e){ if(typeof toast === 'function') toast('Kelime çözümlemesi yüklenemedi; internet bağlantınızı kontrol edin'); return }
  const A = d.a[a - 1]; if(!A || !A[w]) return;
  cur = { s, a, w, A, d };
  ov.classList.remove('hide'); document.documentElement.classList.add('kwlock');
  mark(); show();
};

async function show(){
  const { s, a, w, A } = cur, S = A[w].map(seg), B = await babs(), O = await onay();
  const mode = MODE();
  $q('[data-k="irab"]', ov).style.display = K.cfg.irab ? '' : 'none';
  $q('#kwRef', ov).textContent = `${s}:${a} · ${w + 1}. kelime`;
  $q('#kwW', ov).textContent = S.map(x => x.t).join('');
  $q('#kwSg', ov).innerHTML = S.length > 1 ? S.map(x => `<span lang="ar" class="${x.pos === 'V' ? 'v' : x.pos === 'N' ? 'n' : 'p'}">${E(x.t)}</span>`).join('<b>+</b>') : '';
  ov.querySelectorAll('[data-m]').forEach(b => b.setAttribute('aria-selected', b.dataset.m === mode));
  $q('[data-k="prev"]', ov).disabled = w === 0; $q('[data-k="next"]', ov).disabled = w === A.length - 1;
  const ok = O[`${s}:${a}:${w + 1}`];
  const badge = ok ? `<div class="kok ok">✓ Onaylı${ok.by ? ' · ' + E(ok.by) : ''}</div>` : `<div class="kok">Otomatik çözümleme · <b>taslak</b> (ehil onayı bekliyor)</div>`;
  let h = '';
  if(mode === 'sarf'){
    const r = sarf(S, B);
    h = `<table class="kwt">${r.rows}</table>` + emsileTable(r.m, r.vf || (r.m.pos === 'V' && r.m.f.ROOT && rootL(r.m.f.ROOT).length === 3 ? 1 : 0), B) + badge;
  } else {
    if(ok && ok.ar) h = `<div class="kir"><p class="ira" lang="ar">${E(ok.ar)}</p>${ok.tr ? `<p>${E(ok.tr)}</p>` : ''}</div>`;
    else {
      const ctx = { S, prevW: w > 0 ? A[w - 1].map(seg) : null, wi: w, fail: failCtx(A, w), prevVerbRoot: prevVerbRoot(A, w) };
      h = ira(ctx).map(r => `<div class="kir">${r.seg ? `<span class="kseg" lang="ar">${E(r.seg)}</span>` : ''}<p class="ira" lang="ar">${E(r.ar)}</p><p>${E(r.tr)}</p>${r.note ? `<p class="knote">${E(r.note)}</p>` : ''}</div>`).join('');
    }
    h += badge;
  }
  $q('#kwB', ov).innerHTML = h;
  const t = encodeURIComponent(`Kelime kartı hatası: ${s}:${a}:${w + 1} (${S.map(x => x.t).join('')})`);
  const body = encodeURIComponent(`Âyet: ${s}:${a}, ${w + 1}. kelime\nMod: ${mode}\n\nHata nedir, doğrusu ne olmalı?\n`);
  $q('#kwBug', ov).href = `https://github.com/muhibbimnz-ctrl/el-mihrab/issues/new?title=${t}&body=${body}&labels=kelime-karti`;
}

function uniq(refs){ const m = new Map(); refs.forEach(r => { const k = r.split(':').slice(0, 2).join(':'); if(m.has(k)) m.get(k)[1]++; else m.set(k, [r, 1]) }); return [...m.values()] }
async function kokYerleri(){
  const m = mainSeg(cur.A[cur.w].map(seg)); const B = $q('#kwB', ov);
  if(!m.f.ROOT){ B.insertAdjacentHTML('afterbegin', '<p class="knote">Bu kelimenin kökü yoktur (harf veya câmid).</p>'); return }
  B.innerHTML = '<p class="knote">Yükleniyor…</p>';
  let R; try{ R = (await roots())[m.f.ROOT] }catch(e){ B.innerHTML = '<p class="knote">Kök dizini yüklenemedi.</p>'; return }
  const SNm = typeof SN === 'function' ? SN() : null;
  const lem = Object.entries(R || {}).sort((x, y) => y[1].length - x[1].length);
  const tot = lem.reduce((n, x) => n + x[1].length, 0);
  B.innerHTML = `<p class="knote"><b class="kar" lang="ar">${E([...m.f.ROOT].join(' '))}</b> kökü Kur’an’da <b>${tot}</b> yerde, <b>${lem.length}</b> farklı kelime şekliyle geçer.</p>` +
    lem.map(([l, refs]) => `<details class="kkd" ${l === m.f.LEM ? 'open' : ''}><summary><span lang="ar">${E(l || '—')}</span> <small>${refs.length}</small></summary><div class="kref">${uniq(refs).map(([r, n]) => { const [s, a] = r.split(':'); return `<button data-go="${r}" title="${SNm ? E(SNm[s - 1]) : ''}">${s}:${a}${n > 1 ? ' ×' + n : ''}</button>` }).join('')}</div></details>`).join('');
}

/* metindeki kelimeyi işaretle */
function unmark(){ document.querySelectorAll('.kl.on').forEach(x => x.classList.remove('on')); if(window.CSS && CSS.highlights) CSS.highlights.delete('kw') }
function mark(){
  unmark(); if(!cur) return;
  const el = document.getElementById('a' + cur.a); if(!el) return;
  const t = el.querySelector(`.ar-t .kl[data-t="${tokenOfWord(cur.w)}"]`);
  if(t){ t.classList.add('on'); return }
  const box = el.querySelector('.ar-t'); if(!box || !(window.CSS && CSS.highlights && window.Highlight)) return;
  const r = rangeOfToken(box, tokenOfWord(cur.w)); if(r) CSS.highlights.set('kw', new Highlight(r));
}
const HAS_L = /[ء-يٱ]/;
function tokenOfWord(w){ const sm = cur && cur.d.sm && cur.d.sm[cur.a] && isSimple() ? cur.d.sm[cur.a] : null; return sm ? sm.indexOf(w) : w }
function wordOfToken(d, a, t){ const sm = d.sm && d.sm[a] && isSimple() ? d.sm[a] : null; return sm ? sm[t] : t }
const isSimple = () => typeof set !== 'undefined' && set.script === 'simple';

/* düz metni kelimelere böl */
let hinted = false;
K.wrap = text => {
  if(!hinted){ hinted = true; if(!store.get('mihrab.kwHint', 0)) setTimeout(() => { store.set('mihrab.kwHint', 1); if(typeof toast === 'function') toast('Yeni: âyetteki bir kelimeye dokunun — Sarf ve Nahiv kartı açılır') }, 2500) } let t = -1; return text.split(' ').map(x => HAS_L.test(x) ? `<span class="kl" data-t="${++t}">${E(x)}</span>` : E(x)).join(' ') };
/* tecvidli (HTML) metinde dokunulan noktanın kelime sırası */
function tokenAtPoint(box, x, y){
  let node, off;
  if(document.caretPositionFromPoint){ const p = document.caretPositionFromPoint(x, y); if(!p) return -1; node = p.offsetNode; off = p.offset }
  else if(document.caretRangeFromPoint){ const r = document.caretRangeFromPoint(x, y); if(!r) return -1; node = r.startContainer; off = r.startOffset }
  else return -1;
  if(!box.contains(node) || (node.parentElement && node.parentElement.closest('.num'))) return -1;
  const r = document.createRange(); r.setStart(box, 0); r.setEnd(node, off);
  const before = r.toString(); const parts = before.split(/\s+/);
  const done = parts.slice(0, -1).filter(p => HAS_L.test(p)).length;
  return done;
}
function rangeOfToken(box, ti){
  if(ti < 0) return null;
  const walker = document.createTreeWalker(box, NodeFilter.SHOW_TEXT); let n, tok = -1, inTok = false, start = null, startOff = 0, lastN = null, lastOff = 0;
  while((n = walker.nextNode())){
    if(n.parentElement && n.parentElement.closest('.num')) continue;
    const s = n.data;
    for(let i = 0; i < s.length; i++){
      const sp = /\s/.test(s[i]);
      if(!sp && !inTok){ inTok = true; tok++; if(tok === ti){ start = n; startOff = i } }
      else if(sp && inTok){ inTok = false; if(tok === ti){ const r = document.createRange(); r.setStart(start, startOff); r.setEnd(n, i); return r } }
      if(!sp){ lastN = n; lastOff = i + 1 }
    }
  }
  if(start){ const r = document.createRange(); r.setStart(start, startOff); r.setEnd(lastN, lastOff); return r }
  return null;
}

/* âyet metnine dokunma */
K.onTap = (e, s) => {
  if(typeof set !== 'undefined' && set.kelime === false) return false;
  const box = e.target.closest('.ar-t'); if(!box) return false;
  const ay = box.closest('.ay'); if(!ay) return false;
  const a = +ay.dataset.a; let t;
  const sp = e.target.closest('.kl');
  if(sp) t = +sp.dataset.t;
  else if(box.classList.contains('qf')) return false;
  else t = tokenAtPoint(box, e.clientX, e.clientY);
  if(t == null || t < 0) return false;
  K.data(s).then(d => { const w = wordOfToken(d, a, t); if(w != null && w >= 0) K.open(s, a, w) }).catch(() => K.open(s, a, t));
  return true;
};

/* başka bir yere git ve kelimeyi göster */
K._t = { seg, sarf, ira, failCtx, prevVerbRoot, emsileTable, forms };
K.jump = async (s, a, w) => {
  if(K.cfg.jump) return K.cfg.jump(s, a, w);
  if(typeof st !== 'undefined' && st.s === s && document.getElementById('a' + a)){ const e = document.getElementById('a' + a); e.scrollIntoView({ block: 'center', behavior: 'smooth' }) }
  else if(typeof loadSurah === 'function') await loadSurah(s, a);
  setTimeout(() => K.open(s, a, w), 350);
};
})();
