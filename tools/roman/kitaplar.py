# Romanların sırası (okuma ekranındaki liste bu sırayla çıkar). Yeni kitap: buraya id ekle.
SIRA=['sindbad','cuha','hamama','kalila','hayy','battuta','gulistan','sohrab','masnavi','prince','aesop','crusoe','gulliver','holmes','carol','verne']
# Uzun romanlar (tools/roman/uzun/<id>/); 150 sayfayı geçince listeye kendiliğinden girer
UZUN=['arslan','secere','selahaddin','sharl']
# Listede gösterilmeyen (sözlüğü ortak havuzda kalan) kitaplar: uzun hâli olanların kısa sürümleri
GIZLI=[]  # Farsça: Gülistan, Mesnevî (Tûtî içinde) ve Rüstem ve Sührâb; silinenlerin sözlüğü fa_havuz_sozluk.txt'de
import importlib.util,os
def dil(id):
    sp=importlib.util.spec_from_file_location('k',os.path.join(os.path.dirname(os.path.abspath(__file__)),id+'.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m.KITAP['dil']
def DIL():
    d={}
    for i in SIRA:
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),i+'.py')):d.setdefault(dil(i),[]).append(i)
    return d
