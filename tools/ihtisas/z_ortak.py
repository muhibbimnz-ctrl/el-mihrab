# Zenginleştirme yardımcıları (şahsiyet, konu, terim, kitap, metin)
def P(ad, ar, v, donem, alan, bio, eserler=(), notu='', ekol=''):
    return dict(ad=ad, ar=ar, v=v, donem=donem, alan=alan, ekol=ekol, k='; '.join(list(eserler)[:3]), bio=bio, notu=notu, eserler=list(eserler))
KN = lambda b, ar, d: dict(b=b, ar=ar, d=d)
T = lambda ar, tr, d: dict(ar=ar, tr=tr, d=d)
B = lambda c, tr, ar, mu, v, d: dict(c=c, tr=tr, ar=ar, mu=mu, v=v, d=d)
K = lambda ad, ar, mu, v, tur, neden, zincir=(), app=None: dict(ad=ad, ar=ar, mu=mu, v=v, tur=tur, neden=neden, zincir=list(zincir), app=app)
M = lambda b, ne, ar, ref: dict(b=b, ne=ne, ar=ar, ref=ref)
