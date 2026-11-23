# İhtisas alanlarını data/ihtisas/<id>.json olarak üretir.  python3 tools/ihtisas/yap.py
import json, os, sys, importlib, re
B = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(B, '..', '..')
sys.path.insert(0, B)
SIRA = ['tefsir', 'fikih', 'hadis', 'akaid', 'belagat']  # usul → fıkıh içinde Usûl-i Fıkıh
from ek import TARIH, EK, NISPET
from z_program import PROGRAM, ALISTIRMA
J = lambda n: json.load(open(os.path.join(B, 'kaynak', 'bel_' + n + '.json')))
TEZ = re.compile(r"[^.;]*(?:(?<![’'‘ʿ\w-])(?:tez|tezin|tezinde|tezi|tezler)\b|makale|DergiPark|doktora)[^.;]*[.;]?\s*", re.I)
temiz = lambda t: TEZ.sub('', t or '').strip()
liste = []
for ad in SIRA:
    A = dict(importlib.import_module(ad).ALAN)
    if ad == 'belagat':
        P = J('persons')
        A['sahsiyetDonem'] = P['eras']
        A['sahsiyetler'] = [dict(ad=p['tr'], ar=p['ar'], v=f"{p['dH']}/{p['dM']}" if p.get('dH') else '', k=p.get('works', ''), donem=p.get('era', ''), alan=p.get('field', ''), ekol=p.get('school', ''), bio=temiz(p.get('bio')), notu=temiz(p.get('note')), eserler=p.get('eserler', [])) for p in P['persons']]
        T = J('terms')
        A['terimler'] = [dict(g=g['name'].split('. ', 1)[-1], items=[dict(ar=i['ar'], tr=i['tr'], d=i['d'], ex=i.get('ex', '')) for i in g['items']]) for g in T['groups']]
        A['tarih'] = dict(donemler=[dict(ad=v, aralik='', d='') for v in P['eras'].values()], olaylar=[dict(t=o['date'], kim=o['who'], ne=o['what'], neden=temiz(o['why'])) for o in J('timeline') if not TEZ.search(o['what'])])
        BK = J('books')
        A['kutuphane'] = [dict(c=BK['cats'][b['cat']], tr=b['tr'], ar=b['ar'], mu=b['author'], v=b['d'].replace('ö. ', ''), d=temiz(b['desc'])) for b in BK['items'] if b['cat'] != 'bati']
        A['metinler'] = [dict(b=v['work'], ne=temiz(v['readWhat']), ar=v['text'], ref=v['ref'] if v['text'] else '') for v in J('primary').values()]
        W = J('works'); A['agac'] = dict(b=W['title'], kok=W['tree'], diger=W.get('other', []))
        E = J('edebiyat'); AD = J('adab'); NV = J('novels')
        A['edebiyat'] = dict(
            donemler=[dict(k=d['key'], ad=d['name'], aralik=d['range'], d=d['desc']) for d in E['periods']],
            sahsiyetler=[dict(donem=x['per'], ad=x['tr'], ar=x['ar'], v=x['d'].replace('ö. ', ''), alan=x['field'], k=x['works'], notu=temiz(x['note']), bio=temiz(x.get('bio')), eserler=x.get('eserler', [])) for x in E['persons']],
            yol=[temiz(x) for x in E['path'] if temiz(x)],
            klasikler=[dict(c=AD['cats'][x['cat']], tr=x['tr'], ar=x['ar'], mu=x['author'], v=x['d'].replace('ö. ', ''), d=temiz(x['desc'])) for x in AD['items']],
            romanlar=[dict(c=NV['groups'][x['group']], tr=x['tr'], ar=x['ar'], mu=x['author'], v=x['year'], d=temiz(x['desc']), ulke=x.get('country', '')) for x in NV['items']])
    else:
        Z = importlib.import_module('z_' + ad)
        A['terimler'] = [dict(g='Temel terimler', items=A['terimler'])]
        A['tarih'] = TARIH[ad]
        A['sahsiyetDonem'] = Z.DONEM; A['sahsiyetler'] = Z.KISILER; A['metinler'] = Z.METINLER
        kut = lambda bs: [dict(c=x['ad'], tr=k['ad'], ar=k['ar'], mu=k['mu'], v=k['v'], d=k['neden']) for x in bs for k in x['kitaplar']]
        KT = kut(A['basamaklar']) + EK[ad] + Z.KUT
    n = 0
    for s in A['basamaklar']:
        for k in s['kitaplar']:
            n += 1; k['id'] = f"{ad}{n}"
    on = [ad]
    if ad != 'belagat':
        U = dict(Z.USUL)
        if U.get('kaynak'):  # fıkıh: eski usul alanı
            O = importlib.import_module(U.pop('kaynak')).ALAN; on.append('usul'); m = 0
            for x in O['basamaklar']:
                for k in x['kitaplar']:
                    m += 1; k['id'] = f"usul{m}"
            U['basamaklar'] = O['basamaklar']; U['nasil'] = O['nasil']; U['tarih'] = TARIH['usul']
            ars = {t['ar'] for t in U['terimler']}
            U['terimler'] = O['terimler'] + [t for t in U['terimler'] if t['ar'] not in {x['ar'] for x in O['terimler']}]
            KT += kut(O['basamaklar']) + EK['usul']
        else:
            tasi = U.pop('tasi', [])
            U['basamaklar'] = [x for x in A['basamaklar'] if x['ad'] in tasi] + U['basamaklar']
            A['basamaklar'] = [x for x in A['basamaklar'] if x['ad'] not in tasi]
            for x in U['basamaklar']:
                for k in x['kitaplar']:
                    if 'id' not in k: n += 1; k['id'] = f"{ad}{n}"
            KT += [dict(c=x['ad'], tr=k['ad'], ar=k['ar'], mu=k['mu'], v=k['v'], d=k['neden']) for x in U['basamaklar'][len(tasi):] for k in x['kitaplar']]
        U['terimler'] = [dict(g='Terimler', items=U['terimler'])]
        A['usul'] = U
        g = set(); A['kutuphane'] = [b for b in KT if not (b['tr'] + b['mu'] in g or g.add(b['tr'] + b['mu']))]
    tum = A['basamaklar'] + (A['usul']['basamaklar'] if 'usul' in A else [])
    n = 0
    for s in tum:
        for k in s['kitaplar']:
            n += 1
            assert k['ad'] and k['mu'] and k['neden'], k
            if k['ad'] in NISPET: k['nispet'] = NISPET[k['ad']]
            if k['app'] and isinstance(k['app'], (tuple, list)): k['app'] = dict(u=k['app'][0], t=k['app'][1])
    A['program'] = PROGRAM[ad]; A['alistirma'] = ALISTIRMA[ad]
    A['kitapSayisi'] = n
    json.dump(A, open(os.path.join(K, 'data', 'ihtisas', ad + '.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    liste.append(dict(id=ad, ad=A['ad'], ar=A['ar'], renk=A['renk'], kisa=A['kisa'], n=n, b=len(tum), on=on, u=A['usul']['ad'] if 'usul' in A else ('Edebiyat' if ad == 'belagat' else '')))
    print(ad, n, 'kitap', len(A['sahsiyetler']), 'şahsiyet', len(A['kutuphane']), 'kütüphane', ('usul şahsiyet %d' % len(A['usul']['sahsiyetler'])) if 'usul' in A else '')
json.dump(liste, open(os.path.join(K, 'data', 'ihtisas', 'liste.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
