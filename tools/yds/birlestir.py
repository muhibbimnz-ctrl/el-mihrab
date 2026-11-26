#!/usr/bin/env python3
"""Çok kısa eski okuma metinlerini aynı alandaki yakın konulu kısa metinlerle birleştirir (bir kez çalışır).
İlk metnin id'si korunur; sonraki parçaların başlıkları "§ " ile başlayan ara başlık paragrafı olur
(medrese.js modMetin bunu başlık olarak gösterir). Sözlük ve sorular birleştirilir."""
import json, os
KOK = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
MP = os.path.join(KOK, 'data', 'modern', 'modern.json')
GRUP = [
 ['saglikli-uyku','alzheimer'],['diyabet','su-icmek'],
 ['kitap-okuma','ogretmen-mektubu'],['sinav-kaygisi','ezber-anlama'],
 ['sosyal-medya','dijital-bagimlilik'],['mahalle-kulturu','yaslilar'],
 ['nesir-cahiz','makame'],['kalile-dimne','cocuk-edebiyati'],['ibn-hazm-tavk','endulus-siiri'],['arapca-dunya','turkcedeki-arapca'],
 ['yapay-zeka-tip','yapay-zeka-sinirlar'],['mikroplar','dna'],
 ['iklim-tarim','kuraklik-cölleşme'],['ari','ormanlar'],['gida-israf','geri-donusum'],
 ['para-tarihi','dijital-para'],['karz-hasen','islami-finans'],['paylasim-ekonomisi','kucuk-isletme'],
 ['semerkand','ipek-yolu'],['kanuni','istanbul'],['endulus','kurtuba-camii'],
 ['ramazan','ramazan-dayanisma'],['cuma','mescid-medeniyet'],['komsu-hakki','birrul-valideyn'],['hicret','kuran-cem'],['akl-iman','ilim-yolculugu'],
 ['hk-anayasa','hk-yargi'],['hk-secim','hk-belediye'],['hk-bm','hk-diplomasi'],['hk-insan-haklari','cocuk-haklari','hk-multeci'],['hk-tuketici','arabuluculuk'],
 ['md-gazete','md-basin-ozgurlugu','md-vatandas'],['md-yalan-haber','dijital-iz'],['md-podcast','radyo'],['md-reklam','md-fenomen','md-cocuk-ekran'],['md-belgesel','md-altyazi'],
 ['sn-hat','ebru'],['sn-resim','sn-mimari'],['sn-muzik','arap-muzik-makam'],['sn-sinema','sn-tiyatro'],['sn-olimpiyat','sn-yuruyus'],['sn-futbol','sn-satranc'],
]
SV = ['A1','A2','B1','B2','C1','C2']
M = json.load(open(MP, encoding='utf-8')); X = {m['id']: m for m in M['metinler']}
sil = set()
for g in GRUP:
    L = [X[i] for i in g]; a = L[0]
    assert len({m['alan'] for m in L}) == 1, g
    assert not any(any(p.startswith('§ ') for p in m['ar']) for m in L), ('zaten birleşmiş', g)
    ar, tr = list(a['ar']), list(a['tr'])
    for m in L[1:]:
        ar += ['§ ' + m['ar_baslik']] + m['ar']; tr += ['§ ' + m['baslik']] + m['tr']
    soz, gor = [], set()
    for m in L:
        for x in m['sozluk']:
            if x[0] not in gor: gor.add(x[0]); soz.append(x)
    a.update(ar=ar, tr=tr, sozluk=soz, sorular=[s for m in L for s in m['sorular']],
             baslik=' · '.join(m['baslik'] for m in L), konu=' · '.join(dict.fromkeys(m['konu'] for m in L)),
             seviye=max((m['seviye'] for m in L), key=lambda s: SV.index(s) if s in SV else 0))
    sil.update(g[1:])
M['metinler'] = [m for m in M['metinler'] if m['id'] not in sil]
json.dump(M, open(MP, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(len(GRUP), 'grup birleşti,', len(sil), 'metin kaldırıldı; toplam', len(M['metinler']))
