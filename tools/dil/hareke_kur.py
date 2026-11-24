# Sözlük başlıklarının harekesi -> data/roman/hareke_ar.json {kelime: harekeli}
# Öncelik: tools/dil/ar_hareke_el.txt (elle) > otomatik (Kur'an morfolojisi lemmaları + harekeli ders/kitap metinleri; /tmp/hr/oto.json)
import json,re,os,sys
HAR='ً-ْٰ'
S=json.load(open('data/roman/sozluk_ar.json'))
oto=json.load(open(sys.argv[1])) if len(sys.argv)>1 else json.load(open('data/roman/hareke_ar.json'))
el={};hata=[]
for f in ['tools/dil/ar_hareke_el.txt']:
    for l in open(f,encoding='utf-8'):
        if l.startswith('#') or '=' not in l:continue
        k,v=l.strip().split('=',1)
        if re.sub('['+HAR+']','',v).replace('ى','ي')!=k.replace('ى','ي') or k not in S:hata.append((k,v));continue
        el[k]=v
out={k:v for k,v in oto.items() if k in S};out.update(el)
json.dump(out,open('data/roman/hareke_ar.json','w'),ensure_ascii=False,separators=(',',':'))
print('harekeli',len(out),'/',len(S),'elle',len(el),'uyumsuz',hata[:20],len(hata))
