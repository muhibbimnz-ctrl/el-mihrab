# Kadem içeriğini şifreler / çözer. Şifre depoya yazılmaz; kullanıcıdan alınır.
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py kapat   → data/kadem/**/*.json  →  *.enc  (yayına giden dosyalar)
#   KADEM_SIFRE='…' python3 tools/kadem/sifre.py ac      → *.enc  →  *.json  (düzenlemek için; .json dosyaları git'e girmez)
# Biçim: base64( iv[12] + AES-256-GCM şifreli metin + etiket ). Anahtar = PBKDF2-SHA256(şifre, tuz, tur) — tuz ve tur data/kadem/anahtar.json'da.
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
G=AESGCM(key);mod=sys.argv[1] if len(sys.argv)>1 else ''
if mod=='kapat':
    n=0
    for f in glob.glob(R+'/**/*.json',recursive=True):
        if f.endswith('anahtar.json'): continue
        veri=open(f,'rb').read(); json.loads(veri)
        iv=hmac.new(key,os.path.relpath(f,R).encode()+veri,'sha256').digest()[:12]
        open(f[:-5]+'.enc','w').write(base64.b64encode(iv+G.encrypt(iv,veri,None)).decode()); n+=1
    for f in glob.glob(R+'/**/*.enc',recursive=True):
        if not os.path.exists(f[:-4]+'.json'): os.remove(f); print('silindi',f)
    print(n,'dosya şifrelendi')
elif mod=='ac':
    n=0
    for f in glob.glob(R+'/**/*.enc',recursive=True):
        u=base64.b64decode(open(f).read())
        open(f[:-4]+'.json','wb').write(G.decrypt(u[:12],u[12:],None)); n+=1
    print(n,'dosya çözüldü')
else: print(__doc__ or 'kullanım: sifre.py kapat|ac')
