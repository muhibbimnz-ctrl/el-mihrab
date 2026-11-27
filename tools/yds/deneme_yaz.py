#!/usr/bin/env python3
"""YDS Arapça tam deneme ekler: python3 tools/yds/deneme_yaz.py kaynak.txt [--yeniden]

Kaynak metin (depo dışında tutulur; banka.json şifreli gider):

  #dn 14
  @pasaj c1            → d14_c1  (cloze: (1) ---- … (5) ----)
  @pasaj p1            → okuma parçası (YDS boyu: tek paragraf, 90–200 kelime; elle harekeli yazılabilir)
  @pasaj b1            → parçada boşluk (tek ----)
  @pasaj z1            → anlamı bozan ((I) … (V))
  @sozluk p1           → satır satır  كلمة = anlam  (dokununca önce bu sözlük aranır)
  @soru <tip> [pasaj] [bozan için I-V]
  soru kökü (birden çok satır olabilir; cloze/bosluk/bozan için boş bırakılabilir)
  * doğru şık
  - yanlış şık  (4 tane)
  > Türkçe açıklama (şık harfine/sırasına atıf yapılmaz; şıklar yeniden dizilir)

Denetler: tip dağılımı, 5 farklı şık, pasaj varlığı, cloze boşluk sayısı, okuma parçası uzunluğu (YDS boyu) ve
4+4+3+3+3+3 dağılımı, id/pasaj çakışması, bankada aynı soru kökü. Doğru şıkları her harfte 16 olacak
biçimde dizer (anlamı bozan sorularının cevabı sabittir, öbürleri ona göre dengelenir).
"""
import json, os, random, re, sys

KOK = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
BANKA = os.path.join(KOK, 'data', 'yds', 'banka.json')
DAG = {'kelime': 6, 'gramer': 10, 'cloze': 10, 'tamamlama': 10, 'ceviri': 6, 'paragraf': 20,
       'diyalog': 5, 'yakin': 4, 'bosluk': 4, 'bozan': 5}
SIRA = list(DAG)
ROMA = ['I', 'II', 'III', 'IV', 'V']
HRK = re.compile('[ً-ْٰ]')
VARSAYILAN = {'bosluk': 'Parçada boş bırakılan yere hangi cümle gelmelidir?',
              'bozan': 'Hangi cümle anlam bütünlüğünü bozar?'}


def kelime_say(t):
    return len([w for w in HRK.sub('', t).split() if re.search('[ء-ي]', w)])


def oku(yol):
    dn, pas, soz, sor, hata = None, {}, {}, [], []
    blok = None
    for no, satir in enumerate(open(yol, encoding='utf-8').read().split('\n'), 1):
        s = satir.rstrip()
        if s.startswith('#dn'):
            dn = int(s.split()[1]); continue
        if s.startswith('##'):
            continue
        if s.startswith('@pasaj'):
            blok = ('p', s.split()[1], []); pas[blok[1]] = blok[2]; continue
        if s.startswith('@sozluk'):
            blok = ('s', s.split()[1], []); soz[blok[1]] = blok[2]; continue
        if s.startswith('@soru'):
            p = s.split()
            q = {'tip': p[1], 'p': p[2] if len(p) > 2 else None, 'sabit': p[3] if len(p) > 3 else None,
                 'kok': [], 'dogru': [], 'yanlis': [], 'a': [], 'satir': no}
            sor.append(q); blok = ('q', q, None); continue
        if blok is None:
            if s.strip(): hata.append(f'{no}: blok dışında satır')
            continue
        tur, ad, L = blok
        if tur == 'p':
            L.append(s)
        elif tur == 's':
            if s.strip():
                if '=' not in s: hata.append(f'{no}: sözlük satırında = yok'); continue
                k, v = s.split('=', 1); L.append([k.strip(), v.strip()])
        else:
            q = ad
            if s.startswith('* '): q['dogru'].append(s[2:].strip())
            elif s.startswith('- '): q['yanlis'].append(s[2:].strip())
            elif s.startswith('> '): q['a'].append(s[2:].strip())
            elif s.strip():
                if q['dogru'] or q['yanlis']: hata.append(f'{no}: şıklardan sonra kök satırı')
                q['kok'].append(s.strip())
    pas = {k: '\n'.join(x.strip() for x in v if x.strip()) for k, v in pas.items()}
    return dn, pas, soz, sor, hata


def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    yeniden = '--yeniden' in sys.argv
    dn, pas, soz, sor, hata = oku(sys.argv[1])
    if not dn: sys.exit('#dn yok')
    B = json.load(open(BANKA, encoding='utf-8'))
    on = f'd{dn}_'
    if any(q.get('dn') == dn for q in B['sorular']):
        if not yeniden: sys.exit(f'{dn}. deneme bankada zaten var (değiştirmek için --yeniden)')
        B['sorular'] = [q for q in B['sorular'] if q.get('dn') != dn]
        B['pasajlar'] = {k: v for k, v in B['pasajlar'].items() if not k.startswith(on)}
        B.setdefault('sozluk', {})
        B['sozluk'] = {k: v for k, v in B['sozluk'].items() if not k.startswith(on)}
    for k in pas:
        if on + k in B['pasajlar']: hata.append('pasaj çakışması: ' + on + k)
    eski_kok = {q['q'] for q in B['sorular'] if not q.get('p')}
    say, yeni, pq = {}, [], {}
    for q in sor:
        t = q['tip']; yer = f"satır {q['satir']} ({t})"
        if t not in DAG: hata.append(yer + ': tip geçersiz'); continue
        say[t] = say.get(t, 0) + 1
        qid = f'{on}{t}{say[t]}'
        if q['p']:
            if q['p'] not in pas: hata.append(yer + ': pasaj yok ' + q['p'])
            pq.setdefault(q['p'], []).append(qid)
        elif t in ('cloze', 'paragraf', 'bosluk', 'bozan'): hata.append(yer + ': pasaj gerekli')
        if t == 'bozan':
            if q['sabit'] not in ROMA: hata.append(yer + ': bozan cevabı I-V olmalı'); continue
            k, d, sabit = ROMA[:], ROMA.index(q['sabit']), True
        else:
            if len(q['dogru']) != 1 or len(q['yanlis']) != 4: hata.append(yer + ': 1 doğru + 4 yanlış şık olmalı'); continue
            k = [q['dogru'][0]] + q['yanlis']; d, sabit = 0, False
            if len(set(k)) != 5: hata.append(yer + ': şıklar farklı olmalı')
        if not q['a']: hata.append(yer + ': açıklama yok')
        kok = '\n'.join(q['kok']) or VARSAYILAN.get(t, '')
        if t == 'cloze' and not kok:
            kok = f'({len(pq[q["p"]])}) numaralı boşluk'
        if not kok: hata.append(yer + ': soru kökü yok')
        if not q['p'] and kok in eski_kok: hata.append(yer + ': bu kök bankada zaten var')
        r = {'id': qid, 'tip': t, 'q': kok, 'k': k, 'd': d, 'a': ' '.join(q['a']), 'dn': dn}
        if q['p']: r['p'] = on + q['p']
        r['_sabit'] = sabit; yeni.append(r)
    for t, n in DAG.items():
        if say.get(t, 0) != n: hata.append(f'{t}: {say.get(t, 0)}/{n}')
    # pasaj denetimleri
    okuma = []
    for k, v in pas.items():
        if k.startswith('c'):
            for i in range(1, 6):
                if f'({i}) ----' not in v: hata.append(f'{k}: ({i}) ---- yok')
            if len(pq.get(k, [])) != 5: hata.append(f'{k}: 5 soru olmalı')
        elif k.startswith('p'):
            n, pr = kelime_say(v), v.count('\n') + 1
            okuma.append((k, n, pr, len(pq.get(k, []))))
            if not 90 <= n <= 200: hata.append(f'{k}: {n} kelime (YDS boyu 90–200)')
        elif k.startswith('b'):
            if v.count('----') != 1: hata.append(f'{k}: tek ---- olmalı')
        elif k.startswith('z'):
            for r in ROMA:
                if f'({r})' not in v: hata.append(f'{k}: ({r}) yok')
        if k not in pq: hata.append(f'{k}: sorusu yok')
    if sorted(x[3] for x in okuma) != [3, 3, 3, 3, 4, 4]: hata.append('okuma dağılımı 4+4+3+3+3+3 değil: ' + str([x[3] for x in okuma]))
    for k in soz:
        if k not in pas: hata.append('sözlük pasajı yok: ' + k)
    if hata: sys.exit('\n'.join(hata))
    # doğru şıkları dengele: her harf 16
    hedef = [len(yeni) // 5] * 5
    for r in yeni:
        if r['_sabit']: hedef[r['d']] -= 1
    if min(hedef) < 0: sys.exit('sabit cevaplar dengelenemiyor')
    torba = [i for i in range(5) for _ in range(hedef[i])]
    rnd = random.Random(dn * 7919); rnd.shuffle(torba)
    for r in yeni:
        s = r.pop('_sabit')
        if s: continue
        d = torba.pop(); dogru, yan = r['k'][0], r['k'][1:]
        yan.insert(d, dogru); r['k'] = yan; r['d'] = d
    B['sorular'].extend(yeni)
    for k, v in pas.items(): B['pasajlar'][on + k] = v
    if soz:
        B.setdefault('sozluk', {})
        for k, v in soz.items(): B['sozluk'][on + k] = v
    json.dump(B, open(BANKA, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    from collections import Counter
    c = Counter(r['d'] for r in yeni)
    print(f'{dn}. deneme: {len(yeni)} soru, {len(pas)} pasaj · doğru şıklar', ' '.join(f'{"ABCDE"[i]}{c[i]}' for i in range(5)))
    for k, n, pr, s in okuma: print(f'  {k}: {n} kelime, {pr} paragraf, {s} soru')
    dns = sorted({q.get('dn', 1) for q in B['sorular']})
    print(f'banka: {len(dns)} deneme, {len(B["sorular"])} soru, {len(B["pasajlar"])} pasaj')


if __name__ == '__main__':
    main()
