# Kadem içeriğini şifreler / çözer. Şifre depoya yazılmaz; kullanıcıdan alınır.
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py kapat   → data/kadem/**/*.json  →  *.enc  (yayına giden dosyalar)
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py ac      → *.enc  →  *.json  (düzenlemek için; .json dosyaları git'e girmez)
# Biçim: base64( iv[12] + AES-256-GCM şifreli metin + etiket ). Anahtar = PBKDF2-SHA256(şifre, tuz, tur) — tuz ve tur data/kadem/anahtar.json'da.
# AÇIK dosyalar (şifrelenmez, düz .json olarak yayına gider): sınav listesi ve sınav dosyaları (data/kadem/*.json)
# ile örnek olarak ilk dersin ilk konusu (konu/kuran-1.json) ve 1. MBSTS denemesi (deneme/mbsts-1.json). kadem.html'deki acik() kuralıyla aynı olmalı.
# iv içerikten türetilir (HMAC), böylece içerik değişmeyen dosyanın .enc'i de değişmez.
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
G=AESGCM(key);mod=sys.argv[1] if len(sys.argv)>1 else ''
if mod=='kapat':
    n=0
    for f in glob.glob(R+'/**/*.json',recursive=True):
        if f.endswith('anahtar.json'): continue
        veri=open(f,'rb').read(); json.loads(veri)
        if acik(os.path.relpath(f,R).replace(os.sep,'/')):
            if os.path.exists(f[:-5]+'.enc'): os.remove(f[:-5]+'.enc')
            continue
        iv=hmac.new(key,os.path.relpath(f,R).replace(os.sep,'/').encode()+veri,'sha256').digest()[:12]
        open(f[:-5]+'.enc','w').write(base64.b64encode(iv+G.encrypt(iv,veri,None)).decode()); n+=1
    for f in glob.glob(R+'/**/*.enc',recursive=True):
        if not os.path.exists(f[:-4]+'.json') and os.path.exists(f): os.remove(f); print('silindi',f)
    print(n,'dosya şifrelendi')
elif mod=='ac':
    n=0
    for f in glob.glob(R+'/**/*.enc',recursive=True):
        u=base64.b64decode(open(f).read())
        open(f[:-4]+'.json','wb').write(G.decrypt(u[:12],u[12:],None)); n+=1
    print(n,'dosya çözüldü')
else: print(__doc__ or 'kullanım: sifre.py kapat|ac')
