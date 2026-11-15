#!/usr/bin/env python3
"""OpenITI (Şâmile kaynaklı) metni → data/kitap/<id>.json  {baslik, kaynak, bolumler:[{b, p:[paragraf]}]}"""
import sys, json, re
src, out, kimlik, baslik, kaynak = sys.argv[1:6]
t = open(src, encoding='utf8').read().split('#META#Header#End#', 1)[1]
t = re.sub(r'# PageV\d+P\d+\n', '', t)
t = re.sub(r'\n~~', ' ', t)
bol = []; cur = None
for line in t.split('\n'):
    line = line.strip()
    if not line: continue
    m = re.match(r'### \|+ ?(.*)', line)
    if m:
        h = m.group(1).strip()
        if re.fullmatch(r'[\d\-–. ]*', h) or len(h) < 2:
            if cur is not None: cur['p'].append('§' + h.strip(' -'))
            continue
        cur = {'b': h, 'p': []}; bol.append(cur); continue
    if line.startswith('#'):
        line = line.lstrip('# ').strip()
        if not line or line == '...': continue
        if cur is None: cur = {'b': 'مقدمة', 'p': []}; bol.append(cur)
        if cur['p'] and cur['p'][-1].startswith('§'):
            n = cur['p'].pop()[1:]; line = (n + '- ' if n else '') + line
        cur['p'].append(line)
bol = [b for b in bol if b['p']]
json.dump({'id': kimlik, 'baslik': baslik, 'kaynak': kaynak, 'bolumler': bol}, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=0)
print(kimlik, len(bol), 'bölüm', sum(len(b['p']) for b in bol), 'paragraf')
for b in bol: print(' ', b['b'], len(b['p']))
