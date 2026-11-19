# Yayın öncesi kontrol: HTML içindeki bütün betiklerin ve JS dosyalarının sözdizimini node ile denetler.
import re,glob,subprocess,sys,tempfile,os
hata=0
for f in sorted(glob.glob('*.html')):
    s=open(f,encoding='utf-8').read()
    for i,m in enumerate(re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',s,re.S)):
        js=m.group(1)
        if not js.strip() or 'application/ld+json' in m.group(0): continue
        t=tempfile.NamedTemporaryFile('w',suffix='.js',delete=False,encoding='utf-8');t.write(js);t.close()
        r=subprocess.run(['node','--check',t.name],capture_output=True,text=True);os.unlink(t.name)
        if r.returncode: hata+=1;print('HATA',f,'betik',i,r.stderr.splitlines()[:4])
for f in sorted(glob.glob('*.js')):
    r=subprocess.run(['node','--check',f],capture_output=True,text=True)
    if r.returncode: hata+=1;print('HATA',f,r.stderr.splitlines()[:4])
print('sorun yok' if not hata else f'{hata} hata');sys.exit(1 if hata else 0)
