import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import json,sys
sys.path.insert(0,'.')
from content import DE,FR,ES
from b1 import HK
from b2 import GH as GH2
from b3 import IS as IS2
from b4 import OK as OK2
L={'almanca':('de-DE','Almanca','Deutsch','#c9a14a','#3b3b3b',DE,0,0,0),
   'fransizca':('fr-FR','Fransızca','Français','#7f9bd6','#2b3e74',FR,0,0,0),
   'ispanyolca':('es-ES','İspanyolca','Español','#e6a04a','#9b2d2d',ES,0,0,0)}
import os
_K=os.path.dirname(os.path.abspath(__file__))
T=open(os.path.join(_K,'tpl.html'),encoding='utf-8').read()
for k,(f,(lc,tr,nat,c1,c2,B,H,G,I)) in enumerate(L.items(),1):
    D={'temel':[{'t':t,'r':[[s,x] for s,x in r],'w':[[a,b] for a,b in w]} for t,r,w in B],
       'hikaye':[{'t':t,'r':[[r[k],r[0]] for r in rs]} for t,rs in HK],
       'gunluk':[{'t':t,'r':[[r[k+1],r[1],sp[r[0]][k-1]] for r in rs]} for t,sp,rs in GH2],
       'islami':[{'t':t,'r':[[r[k],r[0]] for r in rs]} for t,rs in IS2],
       'okuma':[{'t':t,'r':[[r[k],r[0]] for r in rs]} for t,rs in OK2]}
    h=(T.replace('%LC%',lc).replace('%TR%',tr).replace('%NAT%',nat).replace('%C1%',c1).replace('%C2%',c2)
        .replace('%KEY%',f).replace('%DATA%',json.dumps(D,ensure_ascii=False)))
    open(os.environ.get('CIKTI',os.path.join(_K,'..','..'))+'/'+f+'.html','w',encoding='utf-8').write(h)
print('ok')
