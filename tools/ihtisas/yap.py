# İhtisas alanlarını data/ihtisas/<id>.json olarak üretir.  python3 tools/ihtisas/yap.py
import json, os, sys, importlib, re
B = os.path.dirname(os.path.abspath(__file__)); K = os.path.join(B, '..', '..')
sys.path.insert(0, B)
SIRA = ['belagat', 'tefsir', 'hadis', 'fikih', 'usul', 'akaid']
from ek import TARIH, EK, NISPET
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
        A['terimler'] = [dict(g='Temel terimler', items=A['terimler'])]
        A['tarih'] = TARIH[ad]
        A['kutuphane'] = [dict(c=s['ad'], tr=k['ad'], ar=k['ar'], mu=k['mu'], v=k['v'], d=k['neden']) for s in A['basamaklar'] for k in s['kitaplar']] + EK[ad]
    n = 0
    for s in A['basamaklar']:
        for k in s['kitaplar']:
            n += 1; k['id'] = f"{ad}{n}"
            assert k['ad'] and k['mu'] and k['neden'], k
            if k['ad'] in NISPET: k['nispet'] = NISPET[k['ad']]
            if k['app']: k['app'] = dict(u=k['app'][0], t=k['app'][1])
    A['kitapSayisi'] = n
    json.dump(A, open(os.path.join(K, 'data', 'ihtisas', ad + '.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    liste.append(dict(id=ad, ad=A['ad'], ar=A['ar'], renk=A['renk'], kisa=A['kisa'], n=n, b=len(A['basamaklar'])))
    print(ad, n, 'kitap', len(A['sahsiyetler']), 'şahsiyet', sum(len(g['items']) for g in A['terimler']), 'terim')
json.dump(liste, open(os.path.join(K, 'data', 'ihtisas', 'liste.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
