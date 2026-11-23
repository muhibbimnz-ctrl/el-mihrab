# Arapça uzun ve zor (C1) metinler: İslâmî (I), Akademik (A) ve C1–C2 (C2) koleksiyonlarına eklenir.
# Her metin: 4 paragraf, 16 tam harekeli cümle + Türkçe çeviri, 8 kelime (örnek cümle + çeviri), 4 çoktan seçmeli soru.
# python3 tools/dil/ar/metin_c1.py   → veri/arapca.js içine /*AR-C1-METIN*/ … /*/AR-C1-METIN*/ bloğu (tekrar çalıştırılırsa eskisini siler, çift eklemez)
import json, os, sys
BU = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BU)
sys.path.insert(0, os.path.join(BU, '..', '..'))
from c1_veri1 import X as X1
from c1_veri2 import X as X2
from dil_veri import blok_yaz

X = X1 + X2
hata = []
for x in X:
    n = sum(len(p) for p in x['p'])
    if len(x['p']) != 4 or not 14 <= n <= 18: hata.append('%s: %d paragraf, %d cümle' % (x['tr'], len(x['p']), n))
    if len(x['v']) != 8 or len(x['mq']) != 4: hata.append('%s: kelime/soru sayısı' % x['tr'])
    for p in x['p']:
        for s in p:
            if len(s) != 2 or not s[0] or not s[1]: hata.append('%s: bozuk cümle' % x['tr'])
    for q in x['mq']:
        if len(q[1]) != 4 or not 0 <= q[2] < 4: hata.append('%s: bozuk soru' % x['tr'])
if hata:
    sys.exit('\n'.join(hata))

gr = {}
for x in X:
    k = x['kol']; y = {a: b for a, b in x.items() if a != 'kol'}
    gr.setdefault(k, []).append(y)
js = '/*AR-C1-METIN*/' + ''.join('%s.push.apply(%s,%s);' % (k, k, json.dumps(v, ensure_ascii=False, separators=(',', ':'))) for k, v in gr.items()) + '/*/AR-C1-METIN*/\n'
oz = blok_yaz('arapca', 'AR-C1-METIN', js)
print(len(X), 'C1 metin;', {k: len(v) for k, v in gr.items()}, ';', sum(sum(len(p) for p in x['p']) for x in X), 'cümle; damga', oz)
