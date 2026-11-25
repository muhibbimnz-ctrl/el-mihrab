# Menfelûtî, Mâcdûlîn (Alphonse Karr'ın "Sous les tilleuls" romanından Arapça serbest tercüme/uyarlama)
# Kaynak: OpenITI 1350AH — 1342MustafaLutfiManfaluti.Majdulin.Hindawi074280904-ara1 (CC BY-NC-SA 4.0)
# OpenITI metninde bölüm başlıkları "(N) Başlık" biçiminde bir önceki paragrafın sonuna yapışık; burada ayrılır.
# Kullanım: python3 tools/roman/openiti_majdulin.py <ara1 dosyası>
import re, json, os, sys
K = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(K, 'tools', 'hadis'))
from openiti import clean

AD = {'ماجدولين': ('Mâcdûlîn’den', 'Mâcdûlîn’e'), 'سوزان': ('Suzan’dan', 'Suzan’a'), 'استيفن': ('Stefan’dan', 'Stefan’a'),
      'إدوار': ('Edvar’dan', 'Edvar’a'), 'مولر': ('Müller’den', 'Müller’e'), 'أوجين': ('Öjen’den', 'Öjen’e'),
      'فردريك': ('Frederik’ten', 'Frederik’e')}
TR = {'خواطر استيفن': 'Stefan’ın düşünceleri', 'الحب': 'Aşk', 'الدعوة': 'Davet', 'الزيارة': 'Ziyaret', 'المرأة': 'Kadın',
      'الحيرة': 'Şaşkınlık', 'المكاشفة': 'İtiraf', 'النشوة': 'Coşku', 'العهد': 'Ahit', 'البحيرة': 'Göl', 'حديث': 'Bir konuşma',
      'الخبر': 'Haber', 'الوداع': 'Veda', 'السفر': 'Yolculuk', 'حفلة رقص': 'Balo', 'النفس العالية': 'Yüce ruh',
      'النفس الشعرية': 'Şair ruh', 'الحظ': 'Talih', 'غرفة استيفن': 'Stefan’ın odası', 'الطارق الجديد': 'Kapıyı çalan yeni misafir',
      'التضحية': 'Fedakârlık', 'الصداقة': 'Dostluk', 'الحياة الجديدة': 'Yeni hayat', 'الفتنة': 'Ayartı', 'الملعب': 'Eğlence yeri',
      'الرجل والمرأة': 'Erkek ve kadın', 'الدسيسة': 'Entrika', 'العرس': 'Düğün', 'المريض': 'Hasta', 'الموت': 'Ölüm',
      'إدوار': 'Edvar', 'سريرة المرأة': 'Kadının iç dünyası', 'الجريدة العسكرية': 'Askerî gazete', 'البيت الجديد': 'Yeni ev',
      'بروتس': 'Brütüs', 'الزفاف': 'Gelin alma', 'الهذيان': 'Sayıklama', 'اليأس': 'Ümitsizlik', 'السعادة': 'Mutluluk',
      'الهدوء': 'Sükûnet', 'الوحدة النفسية': 'Ruhun yalnızlığı', 'قلب استيفن': 'Stefan’ın kalbi', 'قلب ماجدولين': 'Mâcdûlîn’in kalbi',
      'الغرفة الزرقاء': 'Mavi oda', 'الجزاء': 'Karşılık', 'الدموع الأخيرة': 'Son gözyaşları', 'الكارثة': 'Felaket',
      'المقبرة': 'Mezarlık', 'بيتهوفن': 'Beethoven', 'لحن الموت': 'Ölüm ezgisi', 'النهاية': 'Son'}

def tr(t):
    m = re.match(r'^من (\S+) إلى (\S+)$', t)
    if m and m.group(1) in AD and m.group(2) in AD:
        return f'{AD[m.group(1)][0]} {AD[m.group(2)][1]} (mektup)'
    return TR.get(t, '')

def main(src):
    raw = open(src, encoding='utf-8').read().split('#META#Header#End#')[-1]
    P = []
    for l in raw.splitlines():
        if l.startswith('# '): P.append(l[2:])
        elif l.startswith('~~') and P: P[-1] += ' ' + l[2:]
    B = []; cur = None; beklenen = 1
    for p in P:
        m = None
        for x in re.finditer(r'\((\d+)\)', p):
            if int(x.group(1)) == beklenen: m = x
        on, bas = (p[:m.start()], p[m.end():]) if m else (p, None)
        on = clean(on)
        if cur is not None and on: cur['c'].append([on, ''])
        if bas is not None:
            t = re.sub(r'\s*ms\d+\s*', ' ', bas).strip()
            cur = {'b': f'({beklenen}) {t}', 'tr_b': tr(t), 'c': []}; B.append(cur); beklenen += 1
    assert beklenen == 100, beklenen
    B = [b for b in B if b['c']]
    d = {'id': 'majdulin', 'dil': 'ar', 'seviye': 'B2', 'baslik': 'ماجدولين', 'tr_baslik': 'Mâcdûlîn — Ihlamurların altında',
         'yazar': 'Mustafa Lutfî el-Menfelûtî (ö. 1924) · asıl metin', 'uzun': 1, 'bolumler': B, 'sozluk': {},
         'not': 'Asıl Arapça metin (OpenITI külliyatı, CC BY-NC-SA 4.0). Menfelûtî bu romanı Alphonse Karr’ın “Sous les tilleuls” (Ihlamurların altında) adlı eserinden serbestçe Arapçaya aktarmıştır. Bilmediğin kelimeye dokun: anlamı geniş sözlükten gelir.'}
    json.dump(d, open(os.path.join(K, 'data/roman/majdulin.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    L = json.load(open(os.path.join(K, 'data/roman/liste.json'), encoding='utf-8'))
    L = [x for x in L if x['id'] != 'majdulin']
    i = next((k for k, x in enumerate(L) if x['id'] == 'menfaluti'), len(L) - 1) + 1
    L.insert(i, {'id': 'majdulin', 'dil': 'ar', 'seviye': 'B2', 'baslik': 'ماجدولين', 'tr_baslik': d['tr_baslik'], 'yazar': d['yazar'],
                 'bolum': len(B), 'uzun': 1, 'grup': 'Klasik Arap edebiyatı — asıl metin'})
    json.dump(L, open(os.path.join(K, 'data/roman/liste.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(len(B), 'bölüm,', sum(len(p) for b in B for p, _ in b['c']) // 1000, 'bin harf')

if __name__ == '__main__':
    main(sys.argv[1])
