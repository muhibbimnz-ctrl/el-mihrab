# Mesnevî, I. cilt: Tüccar ile papağan (Tûtî ve Tüccar). Ayrı kitap olarak duran Tûtî ve Tüccar buraya katıldı.
import importlib.util,os
_d=os.path.dirname(os.path.abspath(__file__))
B=[]
for _f in ('tuti_1.py','tuti_2.py'):
    _s=importlib.util.spec_from_file_location('t',os.path.join(_d,_f));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
    B+=[('طوطی و بازرگان: '+b,'Tüccar ile papağan: '+tb,ss) for b,tb,ss in _m.B]
