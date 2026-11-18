# Romanların sırası (okuma ekranındaki liste bu sırayla çıkar). Yeni kitap: buraya id ekle.
SIRA=['sindbad','cuha','hamama','kalila','zeydan','hayy','tuti','gulistan','sohrab','leyla','shams','mantik','prince','aesop','crusoe','gulliver','holmes','carol']
import importlib.util,os
def dil(id):
    sp=importlib.util.spec_from_file_location('k',os.path.join(os.path.dirname(os.path.abspath(__file__)),id+'.py'));m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m.KITAP['dil']
def DIL():
    d={}
    for i in SIRA:
        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)),i+'.py')):d.setdefault(dil(i),[]).append(i)
    return d
