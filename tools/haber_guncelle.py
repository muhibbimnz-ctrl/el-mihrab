#!/usr/bin/env python3
"""Haberler bölümünü her gün kendiliğinden günceller (GitHub Actions çalıştırır; Claude gerekmez).
Google Haberler RSS aramalarından son 2 günün Müslümanları ilgilendiren haberlerini alır,
data/haber.json'a başlık + kaynak + bağlantı olarak ekler. Elle eklenen haberler (oto alanı olmayanlar) korunur.
Yalnız Python standart kütüphanesi kullanır."""
import json, re, sys, html, datetime, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

DOSYA = 'data/haber.json'
EN_FAZLA = 60          # listede tutulacak en fazla haber
OTO_GUNLUK = 8         # bir günde eklenecek en fazla otomatik haber
# (etiket, arama) — Google Haberler arama dili; when:2d = son 2 gün
ARAMALAR = [
    ('Türkiye',  'Diyanet İşleri when:2d'),
    ('Türkiye',  '(cami OR hutbe OR müftülük) when:2d'),
    ('Takvim',   '(kandil OR "üç aylar" OR ramazan OR hac OR umre) Diyanet when:2d'),
    ('Filistin', '("Mescid-i Aksa" OR Kudüs OR Gazze) when:2d'),
    ('Dünya',    '(Müslümanlar OR "Müslüman toplum" OR İslamofobi) when:2d'),
    ('Asya',     '("Doğu Türkistan" OR Uygur OR Arakan OR Keşmir) when:2d'),
    ('Dünya',    '("İslam İşbirliği Teşkilatı" OR İİT) when:2d'),
]
# Bu kelimeleri taşıyan başlıklar alınmaz (magazin, spor, fal vb.)
HARIC = re.compile(r'(burç|fal|magazin|maç|gol|transfer|dizi|bölüm fragman|iddaa|kripto|borsa|altın fiyat|hava durumu)', re.I)
GUVENILIR = ['Anadolu Ajansı','AA','TRT Haber','TRT','Diyanet Haber','DHA','İHA','NTV','CNN TÜRK','Hürriyet','Sabah','Milliyet',
             'Yeni Şafak','Türkiye Gazetesi','Habertürk','Al Jazeera','Aljazeera','BBC','BBC News Türkçe','Euronews','Independent Türkçe','Haberler.com','Milli Gazete','Star','Karar','Yeni Akit','Dünya Bülteni']

def rss(q):
    url = 'https://news.google.com/rss/search?' + urllib.parse.urlencode({'q': q, 'hl': 'tr', 'gl': 'TR', 'ceid': 'TR:tr'})
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (el-Mihrab haber botu)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def ayikla(xml_bayt):
    kok = ET.fromstring(xml_bayt)
    for it in kok.iter('item'):
        bas = html.unescape(it.findtext('title') or '').strip()
        kaynak = (it.findtext('source') or '').strip()
        if kaynak and bas.endswith(' - ' + kaynak):
            bas = bas[: -len(' - ' + kaynak)].strip()
        elif ' - ' in bas:
            bas, _, k = bas.rpartition(' - ')
            kaynak = kaynak or k
        link = (it.findtext('link') or '').strip()
        try:
            t = parsedate_to_datetime(it.findtext('pubDate')).astimezone(datetime.timezone(datetime.timedelta(hours=3)))
        except Exception:
            continue
        yield {'baslik': bas, 'kaynak': kaynak, 'link': link, 'zaman': t}

def anahtar(s):
    s = s.lower()
    for a, b in zip('çğıöşüâîû', 'cgiosuaiu'):
        s = s.replace(a, b)
    return set(w for w in re.findall(r'[a-z0-9]{4,}', s))

def benzer(a, b):
    A, B = anahtar(a), anahtar(b)
    return bool(A and B) and len(A & B) / min(len(A), len(B)) >= 0.6

def main():
    d = json.load(open(DOSYA, encoding='utf-8'))
    eski = d.get('haberler', [])
    simdi = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))
    sinir = simdi - datetime.timedelta(days=2)
    adaylar = []
    for etiket, q in ARAMALAR:
        try:
            for h in ayikla(rss(q)):
                if h['zaman'] < sinir or not h['baslik'] or HARIC.search(h['baslik']):
                    continue
                h['etiket'] = etiket
                h['puan'] = (2 if any(h['kaynak'].startswith(g) for g in GUVENILIR) else 0) + h['zaman'].timestamp() / 1e10
                adaylar.append(h)
        except Exception as e:
            print('Arama alınamadı:', q, e, file=sys.stderr)
    adaylar.sort(key=lambda h: -h['puan'])
    yeni = []
    for h in adaylar:
        if any(h['link'] == x.get('link') or benzer(h['baslik'], x.get('baslik', '')) for x in eski + yeni):
            continue
        yeni.append(h)
        if len(yeni) >= OTO_GUNLUK:
            break
    if not yeni:
        print('Yeni haber yok'); return
    kayit = [{'tarih': h['zaman'].strftime('%Y-%m-%d'), 'etiket': h['etiket'], 'baslik': h['baslik'], 'ozet': '',
              'kaynak': h['kaynak'], 'link': h['link'], 'oto': True} for h in yeni]
    hepsi = sorted(kayit + eski, key=lambda x: x.get('tarih', ''), reverse=True)[:EN_FAZLA]
    d['haberler'] = hepsi
    d['guncelleme'] = simdi.strftime('%Y-%m-%d')
    with open(DOSYA, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=2); f.write('\n')
    print(len(yeni), 'yeni haber eklendi:'); [print(' -', h['baslik'], '|', h['kaynak']) for h in yeni]

if __name__ == '__main__':
    main()
