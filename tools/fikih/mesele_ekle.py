# Yeni fıkhi meseleleri data/fikih/meseleler.json'a ekler (aynı id varsa atlar).
#   python3 tools/fikih/mesele_ekle.py tools/fikih/yeni_N.py
# Dosya, M adında bir liste tanımlar; her öğe meseleler.json biçimindedir (metin/ibare isteğe bağlı).
import json, sys, os, urllib.parse
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'fikih', 'meseleler.json')
def hadis(ar):  # hadis arama bağlantısı
    return 'hadis.html#ara=' + urllib.parse.quote(ar) + '&kap=tisa'
G = {'hadis': hadis}
exec(open(sys.argv[1], encoding='utf-8').read(), G)
D = json.load(open(R, encoding='utf-8'))
var = {x['id'] for x in D}
eklendi = 0
for m in G['M']:
    for k in ('id', 'yol', 'baslik', 'ar', 'hanefi', 'mez', 'sebep', 'delil', 'usul'):
        assert k in m, (m.get('id'), k)
    assert set(m['mez']) == {'maliki', 'safii', 'hanbeli'}, m['id']
    m.setdefault('metin', [])
    if m['id'] in var:
        print('var, atlandı:', m['id']); continue
    # aynı alt başlıktaki son meselenin arkasına koy
    yer = max([i for i, x in enumerate(D) if x['yol'][:2] == m['yol'][:2]] or [len(D) - 1])
    D.insert(yer + 1, m); var.add(m['id']); eklendi += 1
json.dump(D, open(R, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(eklendi, 'mesele eklendi; toplam', len(D))
