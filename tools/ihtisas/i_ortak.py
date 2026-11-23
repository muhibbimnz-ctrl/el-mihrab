# İhtisas yenileme katmanı: i_<alan>.py modüllerini eski çıktının (yap.py) üzerine uygular.
# Bir i_ modülü şu adları tanımlayabilir (hepsi isteğe bağlı):
#   DONEM, DONEM_ATA {ad: anahtar}, EK {ad: (bio_ek, not_ek, [eser_ek])}, KISILER [P(...)]
#   TASNIF dict(tesekkul, tasnif, ekoller, tabakat=[...], agac=[...])  — verilen anahtar eskisini değiştirir
#   TERIM [dict(g, items)], DONEMLER [dict(ad, aralik, d)], OLAY [dict(t,kim,ne,neden)], METIN [M], KUT [B]
#   GIRIS [..], NASIL [..], USUL dict(aynı anahtarlar + KONU [dict(g, items=[dict(b,ar,d)])], ad, kisa)
import re
def yil(s):
    m = re.match(r'\D*(\d+)', s or '')
    return int(m[1]) if m else 99999


def _kisiler(X, M, varsayilan_donem):
    D = getattr(M, 'DONEM', None) if not isinstance(M, dict) else M.get('DONEM')
    g = (lambda k, d=None: M.get(k, d)) if isinstance(M, dict) else (lambda k, d=None: getattr(M, k, d))
    if D: X['sahsiyetDonem'] = D
    ata = g('DONEM_ATA', {}) or {}
    ek = g('EK', {}) or {}
    L = X.get('sahsiyetler', [])
    eko = g('EKOL_ATA', {}) or {}
    for p in L:
        if p['ad'] in ata: p['donem'] = ata[p['ad']]
        if p['ad'] in eko: p['ekol'] = eko[p['ad']]
        if p['ad'] in ek:
            e = ek[p['ad']]
            if e[0]: p['bio'] = (p.get('bio', '') + ' ' + e[0]).strip()
            if len(e) > 1 and e[1]: p['notu'] = (p.get('notu', '') + ' ' + e[1]).strip()
            if len(e) > 2 and e[2]:
                p['eserler'] = p.get('eserler', []) + [x for x in e[2] if x not in p.get('eserler', [])]
                p['k'] = '; '.join(p['eserler'][:3])
    adlar = {p['ad'] for p in L}
    L += [p for p in (g('KISILER', []) or []) if p['ad'] not in adlar]
    D = D or X.get('sahsiyetDonem')
    if D:
        sira = list(D.keys())
        L.sort(key=lambda p: (sira.index(p['donem']) if p['donem'] in sira else 99, yil(p.get('v'))))
    X['sahsiyetler'] = L


def _ortak(X, M):
    g = (lambda k, d=None: M.get(k, d)) if isinstance(M, dict) else (lambda k, d=None: getattr(M, k, d))
    _kisiler(X, M, None)
    if g('GIRIS'): X['giris'] = g('GIRIS')
    if g('NASIL'): X['nasil'] = g('NASIL')
    if g('TASNIF'):
        T = dict(X.get('tasnif') or {})
        eski_tab = T.get('tabakat'); eski_agac = T.get('agac')
        for k, v in g('TASNIF').items(): T[k] = v
        tb = g('TASNIF').get('tabakat')
        if isinstance(tb, list) and eski_tab and isinstance(eski_tab, dict) and eski_tab['b'] not in [x['b'] for x in tb]: T['tabakat'] = tb + [eski_tab]
        ag = g('TASNIF').get('agac')
        if isinstance(ag, list) and eski_agac and isinstance(eski_agac, dict) and eski_agac['b'] not in [x['b'] for x in ag]: T['agac'] = [eski_agac] + ag
        X['tasnif'] = T
    if g('TERIM'):
        G = X.get('terimler') or []
        var = {t['ar'] for x in G for t in x['items']}
        for grp in g('TERIM'):
            it = [t for t in grp['items'] if t['ar'] not in var]
            var |= {t['ar'] for t in it}
            if it: G.append(dict(g=grp['g'], items=it))
        X['terimler'] = G
    if g('DONEMLER') or g('OLAY'):
        T = dict(X.get('tarih') or dict(donemler=[], olaylar=[]))
        if g('DONEMLER'): T['donemler'] = g('DONEMLER')
        vr = {o['t'] + o['ne'][:20] for o in T['olaylar']}
        T['olaylar'] = sorted(T['olaylar'] + [o for o in (g('OLAY') or []) if o['t'] + o['ne'][:20] not in vr], key=lambda o: yil(o['t']))
        X['tarih'] = T
    if g('METIN'): X['metinler'] = (X.get('metinler') or []) + g('METIN')
    if g('KUT'):
        K = X.get('kutuphane') or []
        s = {b['tr'] + b['mu'] for b in K}
        X['kutuphane'] = K + [b for b in g('KUT') if not (b['tr'] + b['mu'] in s or s.add(b['tr'] + b['mu']))]
    if g('KAYNAK'): X['kaynak'] = g('KAYNAK')
    if g('KONU'): X['konular'] = (X.get('konular') or []) + g('KONU')
    for k in ('ad', 'kisa'):
        if g(k.upper()): X[k] = g(k.upper())


def uygula(A, M):
    _ortak(A, M)
    U = getattr(M, 'USUL', None)
    if U and 'usul' in A: _ortak(A['usul'], U)
