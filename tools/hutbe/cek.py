#!/usr/bin/env python3
"""Diyanet Din Hizmetleri'nden Cuma hutbelerini alır, data/hutbe.json'u yazar.
GitHub Actions her gün çalıştırır (.github/workflows/hutbe.yml). Elle: python3 tools/hutbe/cek.py
Kaynak sayfa SharePoint listesidir; satırlar sayfanın içinde JSON olarak durur (WPQ1ListData)."""
import json, re, sys, os, io, html, datetime, urllib.request, urllib.parse
KOK = 'https://dinhizmetleri.diyanet.gov.tr'
LISTE = KOK + '/kategoriler/yayinlarimiz/hutbeler/t%C3%BCrk%C3%A7e'
CIKTI = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'hutbe.json')
UA = {'User-Agent': 'Mozilla/5.0 (el-Mihrab hutbe arsivi; +https://muhibbimnz-ctrl.github.io/el-mihrab/)'}

def al(url, ikili=False):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
    b = r.read()
    return b if ikili else b.decode('utf-8', 'replace')

def satirlar(sayfa_html):
    out = []
    for blok in re.findall(r'\{\r?\n"ID"[\s\S]*?\r?\n\}', sayfa_html):
        try:
            d = json.loads(blok)
        except Exception:
            continue
        m = re.fullmatch(r'(\d{1,2})\.(\d{1,2})\.(\d{4})', d.get('Tarih', '').strip())
        if not m or not d.get('Title'):
            continue
        g, a, y = m.group(1).zfill(2), m.group(2).zfill(2), m.group(3)
        tam = lambda p: (KOK + urllib.parse.quote(html.unescape(p), safe="/%()!,'-")) if p else ''
        out.append(dict(tarih=f'{y}-{a}-{g}', baslik=html.unescape(d['Title']).strip(), pdf=tam(d.get('PDF', '')), doc=tam(d.get('Word', '')), ses=tam(d.get('Ses', ''))))
    out.sort(key=lambda x: x['tarih'], reverse=True)
    return out

def metin(pdf_url):
    """PDF'ten paragrafları çıkarır; pypdf yoksa ya da PDF okunamazsa boş döner."""
    try:
        from pypdf import PdfReader
    except Exception:
        return []
    try:
        r = PdfReader(io.BytesIO(al(pdf_url, True)))
        t = '\n'.join((s.extract_text() or '') for s in r.pages)
    except Exception:
        return []
    t = t.replace('\r', '')
    # satır sonlarını birleştir, boş satırlarda paragraf aç
    ps = [re.sub(r'\s*\n\s*', ' ', p).strip() for p in re.split(r'\n\s*\n', t)]
    if len(ps) < 3:  # PDF boş satır vermezse cümle sonlarından böl
        ps = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'(?<=[.!?:”"])\s*\n', t)]
    def arapca(p):
        return len(re.findall(r'[\u0600-\u06FF]', p)) > 0.3 * max(1, len(p))
    ps = [p for p in ps if len(p) > 2 and not arapca(p)]
    # PDF'teki Arapça kısımlar düzgün çıkmaz (harekeler kayar); onlar için PDF bağlantısı verilir
    ps = [re.sub(r'^Tarih:\s*\d{1,2}\.\d{1,2}\.\d{4}\s*', '', p) for p in ps]
    ps = [p for p in ps if p and p.strip() != 'Din Hizmetleri Genel Müdürlüğü']
    return ps[:80]

def main():
    eski = {}
    try:
        eski = {h['tarih']: h for h in json.load(open(CIKTI, encoding='utf-8')).get('hutbeler', [])}
    except Exception:
        pass
    S = satirlar(al(LISTE))
    if not S:
        print('Liste okunamadı; dosyaya dokunulmadı.'); return 1
    for i, h in enumerate(S[:20]):
        e = eski.get(h['tarih'])
        if e and e.get('metin') and e.get('baslik') == h['baslik'] and e.get('v') == 2:
            h['metin'] = e['metin']; h['v'] = 2
        elif i < 6 and h['pdf']:
            h['metin'] = metin(h['pdf']); h['v'] = 2
    yeni = dict(kaynak='Diyanet İşleri Başkanlığı, Din Hizmetleri Genel Müdürlüğü', sayfa=LISTE,
                guncel=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'), hutbeler=S[:20])
    eskiS = json.dumps({k: v for k, v in (json.load(open(CIKTI, encoding='utf-8')) if os.path.exists(CIKTI) else {}).items() if k != 'guncel'}, ensure_ascii=False, sort_keys=True) if os.path.exists(CIKTI) else ''
    yeniS = json.dumps({k: v for k, v in yeni.items() if k != 'guncel'}, ensure_ascii=False, sort_keys=True)
    if eskiS == yeniS:
        print('Değişiklik yok.'); return 0
    json.dump(yeni, open(CIKTI, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print('Yazıldı:', S[0]['tarih'], S[0]['baslik'], len(S[0].get('metin') or []), 'paragraf')
    return 0

if __name__ == '__main__':
    sys.exit(main())
