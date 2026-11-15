#!/usr/bin/env python3
"""Kur'an kelime çözümleme verisini üretir (Medrese / Kelime kartı).

Kaynak: Quranic Arabic Corpus Morphology v0.4 (corpus.quran.com, GNU GPL),
mustafa0x/quran-morphology düzeltilmiş çatalı. Kullanım:
  python3 tools/morph_build.py /yol/quran-morphology.txt
Çıktı: data/morph/{1..114}.json, data/morph/roots.json, data/morph/babs.json
"""
import sys, json, re, os, collections, unicodedata

SRC = sys.argv[1]
OUT = os.path.join(os.path.dirname(__file__), '..', 'data', 'morph')
os.makedirs(OUT, exist_ok=True)

HARAKA = {'َ': 'a', 'ِ': 'i', 'ُ': 'u'}
BASE = re.compile(r'[ء-غف-يٱ]')
HAMZA = set('ءأإؤئآ')
WEAK = set('ويى')
HALQ = set('ءهعحغخ')

def norm(c):
    if c in HAMZA: return 'ء'
    if c == 'ى': return 'ي'
    return c

def letters(t):
    """[(harf, haraka)] — haraka: a/i/u/'' """
    out = []
    for ch in t:
        if BASE.match(ch):
            out.append([norm(ch), ''])
        elif ch in '\u0654\u0655':          # üstte/altta hemze (يَسْـَٔلُ)
            out.append(['ء', ''])
        elif ch in HARAKA and out:
            out[-1][1] = HARAKA[ch]
    return out

# ---------- oku ----------
rows = []
for line in open(SRC, encoding='utf8'):
    line = line.rstrip('\n')
    if not line: continue
    loc, txt, pos, feats = line.split('\t')
    s, a, w, g = map(int, loc.split(':'))
    rows.append((s, a, w, g, txt, pos, feats))

def fd(feats):
    d = {}
    for f in feats.split('|'):
        if ':' in f:
            k, v = f.split(':', 1); d[k] = v
        else:
            d[f] = True
    return d

# ---------- bâb çıkarımı (sülâsî mücerred) ----------
perfV = collections.defaultdict(collections.Counter)
impfV = collections.defaultdict(collections.Counter)
lemV = collections.defaultdict(collections.Counter)

def vowel_at(L, i, want):
    if i < len(L) and L[i][0] == want and L[i][1]:
        return L[i][1]
    return None

for s, a, w, g, txt, pos, feats in rows:
    if pos != 'V': continue
    d = fd(feats)
    if d.get('VF') != '1' or d.get('PASS') or 'ROOT' not in d: continue
    R = [norm(c) for c in d['ROOT']]
    if len(R) != 3: continue
    r1, r2, r3 = R
    L = letters(txt)
    dbl = r2 == r3
    # nâkısta cem/muhâtaba sîgalarında hareke değişir (يَبْغُونَ، خَشُوا) — sayma
    if r3 in WEAK and any(k in d for k in ('3MP', '2MP', '1P', '2FS', 'MP')) and not ('1P' in d and d.get('PERF')):
        continue
    if d.get('PERF'):
        if L and L[0][0] == r1:
            v = vowel_at(L, 1, r2)
            if v and not (dbl and len(L) > 2 and L[2][0] != r3): perfV[d['ROOT']][v] += 1
    elif d.get('IMPF'):
        if len(L) < 2: continue
        st = L[1:]
        v = None
        if r1 in WEAK and st and st[0][0] != r1:      # misal: vav düşmüş (يَعِدُ)
            if st[0][0] == r2: v = st[0][1]
        elif r2 in WEAK and st and st[0][0] == r1:    # ecvef: harekesi R1'e geçer
            v = st[0][1]
        elif dbl and st and st[0][0] == r1:
            if len(st) > 2 and st[1][0] == r2 and st[2][0] == r3: v = st[1][1]
            else: v = st[0][1]
        elif st and st[0][0] == r1:
            v = vowel_at(st, 1, r2)
        if v: impfV[d['ROOT']][v] += 1
    # lemma mâzî ise yardımcı oy
    if 'LEM' in d:
        Lm = letters(d['LEM'])
        if Lm and Lm[0][0] == r1 and len(Lm) >= 2 and Lm[1][0] == r2 and Lm[1][1] and not (dbl and len(Lm) == 2):
            lemV[d['ROOT']][Lm[1][1]] += 1

TABLE = {('a','u'):1, ('a','i'):2, ('a','a'):3, ('i','a'):4, ('i','i'):5, ('u','u'):6}
babs = {}
for root in set(perfV) | set(impfV) | set(lemV):
    R = [norm(c) for c in root]
    pv = (perfV[root] or lemV[root]).most_common(1)
    iv = impfV[root].most_common(1)
    p = pv[0][0] if pv else None
    i = iv[0][0] if iv else None
    b, sure = None, 0
    if R[1] in WEAK and p in (None, 'a'):           # ecvef: mâzî harekesi görünmez
        p = None
    if p and i:
        b = TABLE.get((p, i)); sure = 1 if b else 0
    elif i:
        b = {'u': 1, 'i': 2}.get(i)
        if i == 'a': b = 3 if (R[1] in HALQ or R[2] in HALQ) and R[1] not in WEAK else 4
    elif p:
        b = {'u': 6}.get(p)
        if p == 'i': b = 4
        if b: sure = 0
    if b: babs[root] = [b, sure]
# Sülâsî mücerred masdarı semâîdir: korpusta geçen masdarı ekle
vn = collections.defaultdict(collections.Counter)
for s, a, w, g, txt, pos, feats in rows:
    d = fd(feats)
    if d.get('VN') and d.get('VF') == '1' and 'ROOT' in d and 'LEM' in d:
        vn[d['ROOT']][d['LEM']] += 1
for root, c in vn.items():
    if root in babs: babs[root].append(c.most_common(1)[0][0])
# Yazımı otomatik çözümlemeye elvermeyen birkaç meşhur fiil
babs.update({'رأي': [3, 1], 'جيأ': [2, 1]})

# ---------- sûre dosyaları ----------
words = collections.OrderedDict()
for s, a, w, g, txt, pos, feats in rows:
    words.setdefault((s, a, w), []).append((txt, pos, feats))

roots = collections.defaultdict(lambda: collections.defaultdict(list))
per = collections.defaultdict(lambda: collections.defaultdict(list))
for (s, a, w), segs in words.items():
    out = []
    for txt, pos, feats in segs:
        d = fd(feats)
        if 'ROOT' in d and d.get('VF') == '1' and d['ROOT'] in babs:
            b, sure = babs[d["ROOT"]][:2]
            feats += f'|BAB:{b}{"" if sure else "?"}'
        out.append([txt, pos, feats])
        if 'ROOT' in d:
            roots[d['ROOT']][d.get('LEM', '')].append(f'{s}:{a}:{w}')
    per[s][a].append(out)

# "Basit yazı" (quran-simple) bazen يا/ها nidâsını ayrı yazar: belirteç → kelime eşlemesi
DIAC = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
LET = re.compile(r'[\u0621-\u064A\u0671]')
def simple_map(s):
    p = os.path.join(os.path.dirname(__file__), '..', 'data', 'q', 'quran-simple', f'{s}.json')
    if not os.path.exists(p): return {}
    res = {}
    for x in json.load(open(p, encoding='utf8'))['a']:
        t = x['t']
        if x['n'] == 1 and s not in (1, 9): t = ' '.join(t.split(' ')[4:])
        toks = [k for k in t.split() if LET.search(k)]
        n = len(per[s][x['n']])
        if len(toks) == n: continue
        ex = len(toks) - n; mp = []; w = 0; i = 0
        while i < len(toks):
            mp.append(w)
            if ex > 0 and DIAC.sub('', toks[i]) in ('يا', 'ها', 'ويا', 'فيا', 'وها') and i + 1 < len(toks):
                mp.append(w); i += 1; ex -= 1
            i += 1; w += 1
        if w == n: res[x['n']] = mp
        else: print('eşlenemedi', s, x['n'])
    return res

for s in range(1, 115):
    A = per[s]
    data = {'s': s, 'a': [A[a] for a in sorted(A)]}
    sm = simple_map(s)
    if sm: data['sm'] = sm
    with open(os.path.join(OUT, f'{s}.json'), 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))

R = {r: {l: sorted(set(v), key=lambda x: tuple(map(int, x.split(':')))) for l, v in lems.items()} for r, lems in roots.items()}
with open(os.path.join(OUT, 'roots.json'), 'w', encoding='utf8') as f:
    json.dump(R, f, ensure_ascii=False, separators=(',', ':'))
with open(os.path.join(OUT, 'babs.json'), 'w', encoding='utf8') as f:
    json.dump(babs, f, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
print('kelime', len(words), 'kök', len(R), 'bâb', len(babs), 'kesin', sum(1 for v in babs.values() if v[1]))
