#!/usr/bin/env python3
"""Uzun (C1) okuma metinlerini modern.json'a ekler: python3 tools/yds/c1_ekle.py tools/yds/c1/*.txt

Dosya biçimi:
  @alan id | Türkçe ad | Arapça ad          (yeni alan; varsa atlanır)
  === id | alan | Türkçe başlık | Arapça başlık
  Arapça paragraflar (her satır bir paragraf)
  ---
  Türkçe paragraflar (Arapçayla aynı sayıda)
  ---
  kelime = anlam
  ---
  ? Türkçe soru
  * doğru
  - yanlış (3 tane)
  = Arapça dayanak ifadesi

Aynı id yeniden verilirse metin güncellenir. Metin en az 250 kelime ve 4 paragraf olmalı.
Uzun metinler (uzun: 1) her alanın listesinde başa alınır.
"""
import json, os, re, sys

KOK = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
MP = os.path.join(KOK, 'data', 'modern', 'modern.json')


def kelime(t):
    return len([w for w in t.split() if re.search('[ء-ي]', w)])


def oku(yol):
    alanlar, metinler, hata = [], [], []
    cur = None
    for no, s in enumerate(open(yol, encoding='utf-8').read().split('\n'), 1):
        s = s.strip()
        if s.startswith('@alan'):
            alanlar.append([x.strip() for x in s[5:].split('|')]); continue
        if s.startswith('==='):
            p = [x.strip() for x in s[3:].split('|')]
            cur = {'h': p, 'b': [[]], 'no': no}; metinler.append(cur); continue
        if cur is None or not s:
            continue
        if s == '---':
            cur['b'].append([]); continue
        cur['b'][-1].append(s)
    out = []
    for m in metinler:
        yer = f"{yol}:{m['no']}"
        if len(m['h']) != 4 or len(m['b']) != 4: hata.append(yer + ': başlık ya da bölüm sayısı hatalı'); continue
        id_, alan, b, ab = m['h']; ar, tr, sz, sr = m['b']
        if len(ar) != len(tr): hata.append(f'{id_}: {len(ar)} Arapça / {len(tr)} Türkçe paragraf')
        n = kelime(' '.join(ar))
        if n < 250 or len(ar) < 4: hata.append(f'{id_}: {n} kelime, {len(ar)} paragraf')
        soz = []
        for x in sz:
            if '=' not in x: hata.append(f'{id_}: sözlük satırı: {x}'); continue
            k, v = x.split('=', 1); soz.append([k.strip(), v.strip()])
        sor, q = [], None
        for x in sr:
            if x.startswith('? '): q = {'s': x[2:], 'k': [], 'd': 0, 'a': ''}; sor.append(q)
            elif q is None: hata.append(f'{id_}: soru dışında satır')
            elif x.startswith('* '): q['k'].insert(0, x[2:])
            elif x.startswith('- '): q['k'].append(x[2:])
            elif x.startswith('= '): q['a'] = x[2:]
            else: hata.append(f'{id_}: tanınmayan satır: {x}')
        for q in sor:
            if len(q['k']) != 4 or len(set(q['k'])) != 4: hata.append(f'{id_}: 4 farklı şık olmalı: {q["s"]}')
        if len(sor) < 4: hata.append(f'{id_}: en az 4 soru')
        if len(soz) < 8: hata.append(f'{id_}: en az 8 sözlük maddesi')
        out.append(dict(id=id_, alan=alan, baslik=b, ar_baslik=ab, konu=b, seviye='C1', uzun=1,
                        ar=ar, tr=tr, sozluk=soz, sorular=sor))
    return alanlar, out, hata


def main():
    M = json.load(open(MP, encoding='utf-8'))
    hata, yeni, alan_yeni = [], [], []
    for f in sys.argv[1:]:
        a, m, h = oku(f); alan_yeni += a; yeni += m; hata += h
    var = {a[0] for a in M['alanlar']}
    for a in alan_yeni:
        if a[0] not in var: M['alanlar'].append(a); var.add(a[0])
    for m in yeni:
        if m['alan'] not in var: hata.append(f'{m["id"]}: alan yok {m["alan"]}')
    eski = {x['id']: x for x in M['metinler']}
    for m in yeni:
        if m['id'] in eski and not eski[m['id']].get('uzun'): hata.append(f'{m["id"]}: eski bir metnin kimliği')
    if hata: sys.exit('\n'.join(hata))
    ids = {m['id'] for m in yeni}
    L = [x for x in M['metinler'] if x['id'] not in ids] + yeni
    sira = {a[0]: i for i, a in enumerate(M['alanlar'])}
    # alan sırası korunur; alan içinde önce uzun (C1) metinler
    L.sort(key=lambda x: (sira.get(x['alan'], 99), 0 if x.get('uzun') else 1))
    M['metinler'] = L
    json.dump(M, open(MP, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    from collections import Counter
    c = Counter(x['alan'] for x in L if x.get('uzun'))
    print(f'{len(yeni)} metin yazıldı; toplam {len(L)} metin; uzun:', dict(c))
    for m in yeni: print(f'  {m["id"]}: {kelime(" ".join(m["ar"]))} kelime, {len(m["ar"])} paragraf, {len(m["sorular"])} soru')


if __name__ == '__main__':
    main()
