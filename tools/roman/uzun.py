# Uzun romanlar (150+ sayfa): her cümlenin çevirisi yok, yalnız zor kelimeler sözlükte.
# Kaynak: tools/roman/uzun/<id>/kitap.py (KITAP) + NN.txt bölümleri (# Arapça başlık | Türkçe başlık, sonra boş satırla ayrılmış paragraflar)
#         tools/roman/uzun/<id>/sozluk.txt (yalnız zor kelimeler: kelime=Türkçe)
# 150 sayfadan (≈37.500 kelime) kısa kitaplar uygulama listesine eklenmez.
import os,re,json,glob,importlib.util
K0=os.path.dirname(os.path.abspath(__file__))
H=re.compile(r'[ً-ْٰـ]')
SAYFA=250;ESIK=150
def norm(w,dil):
    if dil=='en':
        w=w.lower().strip("'\".,!?;:");return w[:-2] if w.endswith("'s") else w
    return H.sub('',re.sub(r'[«»،.؟!:؛()\-"]','',w))
def kur(id,yaz=True):
    d=os.path.join(K0,'uzun',id)
    sp=importlib.util.spec_from_file_location('k',os.path.join(d,'kitap.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    K=dict(m.KITAP);dil=K['dil'];K['uzun']=1;devam=K.pop('devam',0)
    G={}
    for ln in open(os.path.join(d,'sozluk.txt'),encoding='utf-8'):
        if '=' in ln:k,v=ln.rstrip('\n').split('=',1);G[norm(k.strip().replace('_','\u200c'),dil)]=v.strip()
    bl=[];kel=0
    for f in sorted(glob.glob(os.path.join(d,'[0-9]*.txt'))):
        t=open(f,encoding='utf-8').read().strip().split('\n',1)
        bas=t[0].lstrip('#').strip();b,tb=(bas.split('|')+[''])[:2]
        if dil=='fa':t=[x.replace('_','\u200c') for x in t]
        ps=[re.sub(r'\s+',' ',p).strip() for p in re.split(r'\n\s*\n',t[1] if len(t)>1 else '') if p.strip()]
        kel+=sum(len(p.split()) for p in ps)
        bl.append({'b':b.strip(),'tr_b':tb.strip(),'c':[[p,''] for p in ps]})
    # Önekli biçimler (و، ف، ب، ل، ك، ال…) sözlükteki yalın kelimeye bağlanır: «وأسوار» → «أسوار»
    if dil=='ar':
        PRE=sorted(['وال','بال','فال','كال','لل','ال','و','ف','ب','ل','ك','وب','ول','فب','وك'],key=len,reverse=True)
        for b0 in bl:
            for p0,_ in b0['c']:
                for w in p0.split():
                    n=norm(w,dil)
                    if not n or n in G:continue
                    for pr in PRE:
                        r=n[len(pr):]
                        if n.startswith(pr) and len(r)>=3:
                            for c in (r,'ال'+r,r[2:] if r.startswith('ال') else None):
                                if c and c in G:G[n]=G[c];break
                            if n in G:break
    elif dil=='fa':
        for b0 in bl:
            for p0,_ in b0['c']:
                for w in p0.split():
                    n=norm(w,dil)
                    if n and n not in G:
                        for c in (n[1:] if n[:1] in 'وب' else None, n[:-1] if n[-1:] in 'یش' else None, n[:-2] if n[-2:] in ('ها','ای','اش') else None):
                            if c and len(c)>=3 and c in G:G[n]=G[c];break
    K['bolumler']=bl;K['sozluk']=G
    sayfa=kel//SAYFA
    if yaz:json.dump(K,open(os.path.join(K0,'..','..','data','roman',id+'.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    print(f'[uzun] {id}: {len(bl)} bölüm, {kel} kelime ≈ {sayfa} sayfa, {len(G)} zor kelime'+('' if sayfa>=ESIK else f' — {ESIK} sayfaya ulaşmadı'+(' (yazılıyor, listede)' if devam else ', listeye eklenmedi')))
    if devam and sayfa<ESIK:K['tr_baslik']+=f' (yazılıyor · {sayfa} sayfa)'
    return ({k:K[k] for k in ['id','dil','seviye','baslik','tr_baslik','yazar']}|{'bolum':len(bl),'uzun':1}) if sayfa>=ESIK or devam else None
