# Hısnü'l-Müslim bölümlerini data/zikir.json'a "bolumler" olarak yazar: python3 tools/zikir/yap.py
import json,os,sys
D=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,D)
import hisn1,hisn2
p=os.path.join(D,'..','..','data','zikir.json');Z=json.load(open(p,encoding='utf-8'))
Z['bolumler']=[{'k':k,'b':[{'b':b,'z':[{'s':s,'t':t,'n':n,'k':kk,'f':f} for s,t,n,kk,f in zs]} for b,zs in bs]} for k,bs in hisn1.K1+hisn2.K2]
json.dump(Z,open(p,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(Z['bolumler']),'kategori',sum(len(c['b']) for c in Z['bolumler']),'bölüm',sum(len(b['z']) for c in Z['bolumler'] for b in c['b']),'dua')
