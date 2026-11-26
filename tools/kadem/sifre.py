# Kadem içeriğini şifreler / çözer. Şifre depoya yazılmaz; kullanıcıdan alınır.
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py kapat   → data/kadem/**/*.json  →  *.enc  (yayına giden dosyalar)
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py ac      → *.enc  →  *.json  (düzenlemek için; .json dosyaları git'e girmez)
# Biçim: base64( iv[12] + AES-256-GCM şifreli metin + etiket ). Anahtar = PBKDF2-SHA256(şifre, tuz, tur) — tuz ve tur data/kadem/anahtar.json'da.
# AÇIK dosyalar (şifrelenmez, düz .json olarak yayına gider): sınav listesi ve sınav dosyaları (data/kadem/*.json)
# ile örnek olarak ilk dersin ilk konusu (konu/kuran-1.json) ve 1. MBSTS denemesi (deneme/mbsts-1.json). kadem.html'deki acik() kuralıyla aynı olmalı.
# iv içerikten türetilir (HMAC), böylece içerik değişmeyen dosyanın .enc'i de değişmez.
# PAKETLER: ana anahtardan HMAC ile iki alt anahtar türetilir: alt(p) = HMAC-SHA256(ana, 'kadem:'+p).
#   mbsts → MBSTS sınavının konuları ve denemeleri (data/kadem/mbsts.json'daki ref'ler)   · Pro MBSTS üyesine verilir
#   yds   → YDS Arapça soru bankası (data/yds/banka.json → banka.enc; ornek.json açık örnek) · Pro YDS üyesine verilir
#   ana   → geri kalan bütün Kadem içeriği · Max üyesi ana anahtarı alır, alt anahtarları kendisi türetir.
# kilit.js'deki türetme kuralıyla aynı olmalı.
import os,sys,json,glob,base64,hmac,hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data','kadem')
pw=os.environ.get('KADEM_SIFRE') or input('Şifre: ')
A=os.path.join(R,'anahtar.json')
if not os.path.exists(A):
    json.dump({'tuz':base64.b64encode(os.urandom(16)).decode(),'tur':250000},open(A,'w'))
a=json.load(open(A))
key=hashlib.pbkdf2_hmac('sha256',pw.encode(),base64.b64decode(a['tuz']),a['tur'],32)
ACIK={'konu/kuran-1.json','deneme/mbsts-1.json'}  # örnek olarak açık bırakılanlar: ilk dersin ilk konusu ve bir tam deneme
def acik(rel): return '/' not in rel or rel in ACIK
def alt(p): return hmac.new(key,('kadem:'+p).encode(),'sha256').digest()
_m=json.load(open(os.path.join(R,'mbsts.json')))
MBSTS={'konu/'+k['ref']+'.json' for k in _m['konular'] if k.get('ref')}|{'deneme/'+k['ref']+'.json' for k in _m['denemeler'] if k.get('ref')}
def anahtar_icin(rel): return alt('mbsts') if rel in MBSTS else key
Y=os.path.join(R,'..','yds')
def sifrele(k,ad,veri):
    iv=hmac.new(k,ad.encode()+veri,'sha256').digest()[:12]
    return base64.b64encode(iv+AESGCM(k).encrypt(iv,veri,None)).decode()
def coz(u):
    for k in (key,alt('mbsts'),alt('yds')):
        try: return AESGCM(k).decrypt(u[:12],u[12:],None)
        except Exception: pass
    raise SystemExit('çözülemedi (şifre yanlış?)')
def yds_kapat():
    f=os.path.join(Y,'banka.json')
    if not os.path.exists(f): return
    veri=open(f,'rb').read(); B=json.loads(veri)
    open(os.path.join(Y,'banka.enc'),'w').write(sifrele(alt('yds'),'yds/banka.json',veri))
    # açık örnek: 1. deneme ve onun parçaları; kelime listesi yok
    S=[q for q in B['sorular'] if (q.get('dn') or 1)==1]
    P={k:v for k,v in B['pasajlar'].items() if any(q.get('p')==k for q in S)}
    json.dump({'ornek':1,'toplam':{'soru':len(B['sorular']),'deneme':len({q.get('dn') or 1 for q in B['sorular']}),'kelime':len(B.get('kelime',[]))},'pasajlar':P,'sorular':S,'kelime':[]},
              open(os.path.join(Y,'ornek.json'),'w'),ensure_ascii=False,separators=(',',':'))
    print('yds: banka.enc + ornek.json',len(S),'örnek soru')
G=AESGCM(key);mod=sys.argv[1] if len(sys.argv)>1 else ''
if mod=='kapat':
    n=0
    for f in glob.glob(R+'/**/*.json',recursive=True):
        if f.endswith('anahtar.json'): continue
        veri=open(f,'rb').read(); json.loads(veri)
        if acik(os.path.relpath(f,R).replace(os.sep,'/')):
            if os.path.exists(f[:-5]+'.enc'): os.remove(f[:-5]+'.enc')
            continue
        rel=os.path.relpath(f,R).replace(os.sep,'/')
        open(f[:-5]+'.enc','w').write(sifrele(anahtar_icin(rel),rel,veri)); n+=1
    for f in glob.glob(R+'/**/*.enc',recursive=True):
        if not os.path.exists(f[:-4]+'.json') and os.path.exists(f): os.remove(f); print('silindi',f)
    print(n,'dosya şifrelendi'); yds_kapat()
elif mod=='ac':
    n=0
    for f in glob.glob(R+'/**/*.enc',recursive=True)+[os.path.join(Y,'banka.enc')]:
        if not os.path.exists(f): continue
        u=base64.b64decode(open(f).read())
        open(f[:-4]+'.json','wb').write(coz(u)); n+=1
    print(n,'dosya çözüldü')
else: print(__doc__ or 'kullanım: sifre.py kapat|ac')
