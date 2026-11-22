# python3 tools/cocuk/yap.py  -> data/cocuk/icerik.json
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from dersler import DERSLER
from hikayeler import HIKAYELER
from buyukler import BUYUKLER
from siyer import SIYER
from kissalar import KISSALAR
from namaz import ABDEST, NAMAZ, VAKIT, SURELER, DUALAR, DOGRU_YANLIS, HAFIZA

SIYER_SORU = [
 ['Peygamberimiz hangi yıl doğdu?', '571', ['610', '622', '632']],
 ['İlk vahiy hangi mağarada geldi?', 'Hira', ['Sevr', 'Uhud', 'Nur']],
 ['Hicrette Peygamberimizle birlikte mağarada saklanan sahabi kimdir?', 'Hz. Ebû Bekir', ['Hz. Ömer', 'Hz. Bilâl', 'Hz. Hamza']],
 ['Mekke’den Medine’ye göçe ne denir?', 'Hicret', ['Mi‘râc', 'Hac', 'Fetih']],
 ['Medinelilere ne ad verilir?', 'Ensâr', ['Muhâcir', 'Kureyş', 'Sahabe']],
 ['Hendek kazma fikrini kim verdi?', 'Selmân-ı Fârisî', ['Hz. Ali', 'Hz. Osman', 'Hz. Bilâl']],
 ['Bedir’de Müslümanlar kaç kişiydi?', '313', ['1000', '40', '10.000']],
 ['Uhud’da şehit olan Peygamberimizin amcası kimdir?', 'Hz. Hamza', ['Ebû Tâlib', 'Hz. Abbas', 'Ebû Leheb']],
 ['İslam’ın ilk müezzini kimdir?', 'Hz. Bilâl', ['Hz. Enes', 'Hz. Zeyd', 'Hz. Mus‘ab']],
 ['Peygamberimiz Mekke’yi fethedince Mekkelilere ne dedi?', 'Bugün size kınama yok, serbestsiniz', ['Hepiniz cezalandırılacaksınız', 'Şehri terk edin', 'Malınızı verin']],
 ['Veda Hutbesi nerede okundu?', 'Arafat’ta', ['Medine’de', 'Tâif’te', 'Bedir’de']],
 ['Peygamberimiz kaç yaşında vefat etti?', '63', ['40', '53', '70']],
]

def quiz_pool():
    out = []
    for d in DERSLER:
        for s in d['s']:
            out.append(dict(q=s[0], d=s[1], y=s[2], k=d['id']))
    for s in SIYER_SORU:
        out.append(dict(q=s[0], d=s[1], y=s[2], k='siyer'))
    ads = [b['ad'] for b in BUYUKLER]
    for i, b in enumerate(BUYUKLER):
        yan = [ads[(i + j) % len(ads)] for j in (3, 7, 11)]
        out.append(dict(q=f'“{b["lakap"]}” kimdir?', d=b['ad'], y=yan, k='buyuk'))
    kads = [k['ad'] for k in KISSALAR]
    for i, k in enumerate(KISSALAR):
        out.append(dict(q=f'“{k["ozet"]}” hangi peygamberin kıssasıdır?', d=k['ad'], y=[kads[(i + j) % len(kads)] for j in (2, 5, 7)], k='kissa'))
    return out

def kontrol():
    for grup in (DERSLER, HIKAYELER, BUYUKLER, SIYER, KISSALAR):
        ids = [d['id'] for d in grup]
        assert len(ids) == len(set(ids)), ids
    did = {d['id'] for d in DUALAR}
    for n in NAMAZ:
        for o in n['o']:
            assert o in did or (o.startswith('s') and o[1:].isdigit()), o
    for q in quiz_pool():
        assert q['d'] not in q['y'] and len(set(q['y'])) == 3, q

kontrol()
V = dict(
    surum=1,
    dersler=DERSLER, hikayeler=HIKAYELER, kissalar=KISSALAR, buyukler=BUYUKLER, siyer=SIYER,
    abdest=[dict(i=a, b=b, a=c) for a, b, c in ABDEST], namaz=NAMAZ,
    vakit=[dict(i=a, b=b, r=c) for a, b, c in VAKIT],
    sureler=[dict(n=a, ad=b, a=c) for a, b, c in SURELER], dualar=DUALAR,
    oyun=dict(bilgi=quiz_pool(), dy=[dict(c=a, d=b) for a, b in DOGRU_YANLIS], hafiza=[dict(i=a, t=b) for a, b in HAFIZA]),
)
os.makedirs('data/cocuk', exist_ok=True)
json.dump(V, open('data/cocuk/icerik.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
kel = sum(len(' '.join(x['p']).split()) for x in DERSLER + HIKAYELER + BUYUKLER + SIYER + [b for k in KISSALAR for b in k['bolumler']])
print('ok', os.path.getsize('data/cocuk/icerik.json') // 1024, 'KB;', len(DERSLER), 'ders,', len(HIKAYELER), 'hikâye,', len(BUYUKLER), 'büyük,', len(SIYER), 'siyer,', len(KISSALAR), 'kıssa,', len(DUALAR), 'dua,', len(V['oyun']['bilgi']), 'soru;', kel, 'kelime')
