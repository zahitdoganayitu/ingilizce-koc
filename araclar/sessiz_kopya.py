"""Önizleme için SESSİZ kopya: speechSynthesis.speak etkisiz — test sırasında kullanıcının hoparlöründen ses çıkmasın.
Kaynak dosyaya dokunmaz. Hedef: ~/.claude/launch.json "ingilizce" sunucusunun dizini (varsayılan scratchpad/ing).
Kullanım: python3 araclar/sessiz_kopya.py [hedef_dizin]"""
import os, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dst = sys.argv[1] if len(sys.argv) > 1 else '/private/tmp/claude-501/-Users-zahit/a23d21e5-1651-4009-9279-5f00ef8fb1f6/scratchpad/ing'
os.makedirs(dst, exist_ok=True)
for f in os.listdir(ROOT):
    if f.endswith(('.png', '.json', '.js')) and os.path.isfile(os.path.join(ROOT, f)):
        shutil.copy(os.path.join(ROOT, f), dst)
h = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
stub = '<head>\n<script>try{speechSynthesis.speak=function(){};}catch(e){}</script>'
open(os.path.join(dst, 'index.html'), 'w', encoding='utf-8').write(h.replace('<head>', stub, 1))
print('sessiz kopya:', dst)
