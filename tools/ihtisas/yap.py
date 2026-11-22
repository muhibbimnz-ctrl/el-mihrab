# İhtisas alanlarını data/ihtisas/<id>.json olarak üretir.  python3 tools/ihtisas/yap.py
import json, os, sys, importlib
B = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(B, '..', '..')
sys.path.insert(0, B)
SIRA = ['belagat', 'tefsir', 'hadis', 'fikih', 'akaid']
liste = []
for ad in SIRA:
    A = dict(importlib.import_module(ad).ALAN)
    if ad == 'belagat':
        P = json.load(open(os.path.join(B, 'kaynak', 'bel_persons.json')))
        A['sahsiyetler'] = [dict(ad=p['tr'], ar=p['ar'], v=f"{p['dH']}/{p['dM']}" if p.get('dH') else '', k=p.get('works', '')) for p in P['persons']]
        T = json.load(open(os.path.join(B, 'kaynak', 'bel_terms.json')))
        A['terimler'] = [dict(g=g['name'].split('. ', 1)[-1], items=[dict(ar=i['ar'], tr=i['tr'], d=i['d']) for i in g['items']]) for g in T['groups']]
    else:
        A['terimler'] = [dict(g='Temel terimler', items=A['terimler'])]
    n = 0
    for s in A['basamaklar']:
        for k in s['kitaplar']:
            n += 1; k['id'] = f"{ad}{n}"
            assert k['ad'] and k['mu'] and k['neden'], k
            if k['app']: k['app'] = dict(u=k['app'][0], t=k['app'][1])
    A['kitapSayisi'] = n
    json.dump(A, open(os.path.join(K, 'data', 'ihtisas', ad + '.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    liste.append(dict(id=ad, ad=A['ad'], ar=A['ar'], renk=A['renk'], kisa=A['kisa'], n=n, b=len(A['basamaklar'])))
    print(ad, n, 'kitap', len(A['sahsiyetler']), 'şahsiyet', sum(len(g['items']) for g in A['terimler']), 'terim')
json.dump(liste, open(os.path.join(K, 'data', 'ihtisas', 'liste.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
