# Binbir Gece — Sindbad'ın yedi yolculuğu. el-Mihrâb için A1–A2 uyarlama (özgün metin değildir). Bölümler sindbad_*.py dosyalarından toplanır.
import importlib.util,glob,os
KITAP={'id':'sindbad','dil':'ar','seviye':'A2','baslik':'رِحْلَاتُ السِّنْدِبَادِ السَّبْعُ','tr_baslik':'Sindbad’ın Yedi Yolculuğu',
'yazar':'Binbir Gece Masalları — uyarlama',
'not':''}
B=[]
for p in sorted(glob.glob(os.path.join(os.path.dirname(__file__),'sindbad_[0-9]*.py'))):
    sp=importlib.util.spec_from_file_location('p',p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);B+=m.B
