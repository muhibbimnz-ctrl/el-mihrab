"""Dil sayfalarının (arapca/ingilizce/farsca) büyük ders verisini ayrı dosyada tutar.

Neden: 1 MB'lık HTML her açılışta ağdan yeniden indiriliyor ve tarayıcı satır içi
betiği ana iş parçacığında derliyordu; zayıf telefonlarda donma yapıyordu.
Şimdi veri  veri/<ad>.js  dosyasında; HTML onu  ?v=<özet>  ile çağırır.
Service worker bu dosyaları önce telefondaki kopyadan verir (özet değişince yenisi iner),
tarayıcı da ayrı dosyayı arka planda derleyip önbelleğe alır.

Kullanım:
  python3 tools/dil_veri.py            # üç sayfayı böl (bölünmüşse sadece özeti tazele)
Diğer araçlar:
  from dil_veri import blok_yaz;  blok_yaz('arapca','YDS-METIN',js)
"""
import hashlib, os, re, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAYFALAR = ['arapca', 'ingilizce', 'farsca']
BLOKLAR = ['YDS-METIN', 'FA-METIN']


def _y(ad):
    return os.path.join(KOK, ad + '.html'), os.path.join(KOK, 'veri', ad + '.js')


def damga(ad):
    h, v = _y(ad)
    s = open(h, encoding='utf-8').read()
    oz = hashlib.sha1(open(v, 'rb').read()).hexdigest()[:10]
    s2 = re.sub(r'<script src="veri/%s\.js(\?v=[0-9a-f]*)?"></script>' % ad,
                '<script src="veri/%s.js?v=%s"></script>' % (ad, oz), s)
    assert s2.count('veri/%s.js?v=' % ad) == 1, ad
    open(h, 'w', encoding='utf-8').write(s2)
    return oz


def bol(ad):
    h, v = _y(ad)
    s = open(h, encoding='utf-8').read()
    if ('<script src="veri/%s.js' % ad) in s:
        return damga(ad)
    bas = s.index('<script>\nvar D=[')
    son = s.index('</script>', bas)
    gov = s[bas + len('<script>'):son]
    k = gov.index('/* ===== Durum ===== */')
    veri, kod = gov[:k], gov[k:]
    ek = ''
    for b in BLOKLAR:
        for m in list(re.finditer(r'/\*%s\*/.*?/\*/%s\*/\n' % (b, b), kod, re.S)):
            ek += m.group(0)
        kod = re.sub(r'/\*%s\*/.*?/\*/%s\*/\n' % (b, b), '', kod, flags=re.S)
    os.makedirs(os.path.dirname(v), exist_ok=True)
    open(v, 'w', encoding='utf-8').write('/* %s.html ders verisi — tools/dil_veri.py ile ayrıldı */' % ad + veri + ek)
    s = s[:bas] + '<script src="veri/%s.js"></script>\n<script>\n' % ad + kod + s[son:]
    open(h, 'w', encoding='utf-8').write(s)
    return damga(ad)


def blok_yaz(ad, isim, js):
    """Araçların eklediği metin bloğunu veri dosyasına yazar (eskisini siler)."""
    bol(ad)
    h, v = _y(ad)
    s = open(v, encoding='utf-8').read()
    s = re.sub(r'/\*%s\*/.*?/\*/%s\*/\n' % (isim, isim), '', s, flags=re.S)
    if not s.endswith('\n'):
        s += '\n'
    open(v, 'w', encoding='utf-8').write(s + js)
    return damga(ad)


if __name__ == '__main__':
    for a in (sys.argv[1:] or SAYFALAR):
        print(a, bol(a), os.path.getsize(_y(a)[0]), os.path.getsize(_y(a)[1]))
