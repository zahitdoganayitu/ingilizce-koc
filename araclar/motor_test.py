"""Kural motoru testi — tarayıcısız, JavaScriptCore ile (bu makinede node yok).
index.html'den V_BASE … checkEnglish arasını çıkarır, cumleler.js'teki [girdi, beklenen] çiftlerini koşar.
Kullanım:  python3 araclar/motor_test.py            (depo kökünden)
           python3 araclar/motor_test.py ek.js      (ek vaka dosyası; aynı C=[...] biçimi)"""
import os, re, subprocess, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
a = h.index('const V_BASE=')
b = h.index('\n}\n', h.index('function checkEnglish(text){')) + 3
engine = h[a:b]
cases = open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'araclar', 'cumleler.js'), encoding='utf-8').read()
runner = r'''
let fail=0,out=[];
for(const [i,e] of C){const o=checkEnglish(i).fixed;if(o!==e){fail++;out.push('❌ '+JSON.stringify(i)+'\n   beklenen: '+e+'\n   çıkan:    '+o);}}
out.push((C.length-fail)+'/'+C.length+' geçti');
out.join('\n');'''
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
    f.write(engine + '\n' + cases + '\n' + runner); p = f.name
r = subprocess.run(['osascript', '-l', 'JavaScript', p], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip()); os.unlink(p)
sys.exit(0 if r.stdout.strip().endswith(' geçti') and '❌' not in r.stdout else 1)
