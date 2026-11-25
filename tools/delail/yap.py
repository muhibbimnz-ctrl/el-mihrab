#!/usr/bin/env python3
"""Delâilü'l-Hayrât verisini (data/delail.json) kurar.

Kaynak: github.com/zboon/dalailul-khayrat deposundaki content/dalail/ klasörü
(İstanbul tertibi, 8 hizib). Yalnız Arapça metin alınır; o depodaki
transliterasyon ve İngilizce çeviri ALINMAZ. Harekeler kaynaktaki gibidir.

Kullanım: python3 tools/delail/yap.py <dalailul-khayrat>/content/dalail
"""
import json, os, re, sys

BOLUM = [  # (kaynak dosya, Türkçe ad, hizb günü: JS getDay, None = gün yok)
    ('the-opening-dua', 'Başlangıç duası', None),
    ('the-names-of-allah', 'Esmâ-i Hüsnâ', None),
    ('seeking-refuge-from-shirk', 'Şirkten istiâze duası', None),
    ('sayyid-al-istighfar', 'Seyyidü’l-istiğfâr', None),
    ('the-names-of-the-prophet', 'Esmâ-i Nebî', None),
    ('monday-part-1', '1. Hizb · Pazartesi', 1),
    ('tuesday', '2. Hizb · Salı', 2),
    ('wednesday', '3. Hizb · Çarşamba', 3),
    ('thursday', '4. Hizb · Perşembe', 4),
    ('friday', '5. Hizb · Cuma', 5),
    ('saturday', '6. Hizb · Cumartesi', 6),
    ('sunday', '7. Hizb · Pazar', 0),
    ('monday-part-2', '8. Hizb · Pazartesi (hatim)', None),
    ('the-dua-of-completion', 'Hatim duası', None),
]

def temizle(s):
    s = s.replace('‖', ' ')
    return '\n'.join(re.sub(r'[ \t]+', ' ', l).strip() for l in s.split('\n')).strip()

def main(src):
    out = []
    for dosya, ad, gun in BOLUM:
        d = json.load(open(os.path.join(src, dosya + '.json'), encoding='utf-8'))
        m = []
        for v in d['verses']:
            t = temizle(v.get('ar', ''))
            if not t:
                continue
            x = {'a': t}
            if v.get('sep'): x['s'] = v['sep']
            if v.get('instruction'): x['y'] = 1
            if v.get('band'): x['b'] = temizle(v['band'])
            m.append(x)
        b = {'id': dosya, 'ad': ad, 'ar': temizle(d.get('titleArabic', '')), 'm': m}
        if gun is not None: b['gun'] = gun
        out.append(b)
    veri = {
        'kaynak': 'Arapça metin: zboon/dalailul-khayrat (İstanbul tertibi, 8 hizib) — github.com/zboon/dalailul-khayrat. '
                  'Delâilü’l-Hayrât, Muhammed b. Süleyman el-Cezûlî (ö. 870/1465).',
        'bolumler': out,
    }
    hedef = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'delail.json')
    with open(hedef, 'w', encoding='utf-8') as f:
        json.dump(veri, f, ensure_ascii=False, separators=(',', ':'))
    print(len(out), 'bölüm,', sum(len(b['m']) for b in out), 'paragraf,',
          sum(len(x['a']) for b in out for x in b['m']), 'harf →', os.path.normpath(hedef))

if __name__ == '__main__':
    main(sys.argv[1])
