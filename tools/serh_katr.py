import re,json,sys
src=sys.argv[1]
t=open(src,encoding='utf8').read().split('#META#Header#End#',1)[1]
t=re.sub(r'# PageV\d+P\d+\n','',t); t=re.sub(r'\n~~',' ',t); t=re.sub(r'\s*ms\d+\s*',' ',t); t=re.sub(r'PageV\d+P\d+','',t)
B=[];cur=None
for line in t.split('\n'):
    line=line.strip()
    if not line: continue
    m=re.match(r'### \|+ ?(.*)',line)
    if m:
        h=m.group(1).strip()
        cur={'b':h,'p':[],'pt':[]};B.append(cur);continue
    if not line.startswith('#'): continue
    line=re.sub(r'\s+',' ',line.lstrip('# ').strip())
    if not line: continue
    if cur is None: cur={'b':'مقدمة','p':[],'pt':[]};B.append(cur)
    # split by markers
    parts=re.split(r'(?:^|\s)(ص|ش)\s',' '+line)
    last=cur['pt'][-1] if cur['pt'] else 's'
    buf=parts[0].strip()
    if buf:
        if cur['p'] and cur['pt'][-1]==last and len(cur['p'][-1])<600: cur['p'][-1]+=' '+buf
        else: cur['p'].append(buf); cur['pt'].append(last)
    for i in range(1,len(parts),2):
        typ='m' if parts[i]=='ص' else 's'; txt=parts[i+1].strip()
        if txt: cur['p'].append(txt); cur['pt'].append(typ)
B=[b for b in B if b['p']]
# merge tiny sections into previous (headings with <1 paragraph handled)
json.dump({'id':'serhkatr','baslik':'شرح قطر الندى وبل الصدى','kaynak':'İbn Hişâm’ın kendi şerhi · OpenITI (Şâmile 6970)','tur':'serh','bolumler':B},open('data/kitap/serhkatr.json','w'),ensure_ascii=False,separators=(',',':'))
print(len(B),'bölüm',sum(len(b['p']) for b in B),'paragraf',sum(b['pt'].count('m') for b in B),'matn parçası')
for b in B[:12]: print(' ',b['b'],len(b['p']),b['pt'][:6])
