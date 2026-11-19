# Fıkıh meselelerindeki hadis arama bağlantılarının sonuç verdiğini denetler
import json,re,urllib.parse as up,os
d=json.load(open('data/fikih/meseleler.json'));K=json.load(open('data/hadis/kutub.json'))
def an(t):
    t=re.sub('[ً-ٰـۖ-ۭ‌-‏]','',t);t=re.sub('[أإآٱ]','ا',t).replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return re.sub(r'\s+',' ',re.sub('[^ء-ي\\s]',' ',t)).strip()
C={};S=['bukhari','muslim','abudawud','tirmidhi','nasai','ibnmajah']
def kit(kap):
    if kap=='sitte':return S
    if kap=='tisa':return S+['malik','ahmed','darimi']
    if kap.startswith('k:'):return [kap[2:]]
    return [b['k'] for b in K]
bad=0
for x in d:
  for t,et,u,ac in x['delil']:
    if 'ara=' not in u:continue
    q=up.unquote(re.search('ara=([^&]+)',u).group(1));kap=re.search('kap=(.+)',u).group(1);W=an(q).split(' ');n=0
    for k in kit(kap):
      f=f'data/hadis/ara/{k}.json'
      if not os.path.exists(f):continue
      if k not in C:C[k]=json.load(open(f))
      n+=sum(1 for r in C[k] if all(w in r[1] for w in W))
    if n==0 or n>80: bad+=1;print(x['id'],'|',et,'|',q,'|',kap,'->',n)
print('sorunlu',bad)
