# Ölçüm ve doğrulama araçları

Bu makinede node/npm YOK — python3 + JavaScriptCore (`osascript -l JavaScript`) + Chrome.

| araç | ne yapar |
|---|---|
| `motor_test.py` | Kural motorunu (`V_BASE` … `checkEnglish`) index.html'den çıkarıp `cumleler.js`'teki vakaları koşar. Kural değiştirince ŞART. |
| `cumleler.js` | Regresyon vakaları `[girdi, beklenen]`; beklenen = girdi ise yanlış-pozitif testi. Yeni kural = yeni vaka. |
| `sessiz_kopya.py` | Önizleme için `speechSynthesis.speak` etkisiz kopya üretir (test sırasında hoparlörden ses çıkmasın). |
| `cdp.py` | Headless Chrome istemcisi (FALLOUER'dan uyarlama). `CDP_PORT` ile birden çok paralel oturum. |

Uygulama içi self-test: URL sonuna `#test`, konsola bak.

## Headless Chrome (ses kapalı)
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --mute-audio \
  --remote-debugging-port=9351 --user-data-dir=/tmp/ing-chrome-1 --no-first-run about:blank &
export CDP_PORT=9351
python3 araclar/cdp.py open about:blank
python3 araclar/cdp.py emu 375 812 1           # iPhone ölçüsü + dokunmatik
python3 araclar/cdp.py nav "http://localhost:8777/index.html?v=$RANDOM"
python3 araclar/cdp.py js 'WORDS.length'
python3 araclar/cdp.py shot /tmp/ekran.png
pkill -f remote-debugging-port=9351
```
Önizleme sunucusu (`~/.claude/launch.json` → `ingilizce`, port 8777) **sessiz kopyayı** sunar: önce `python3 araclar/sessiz_kopya.py`.
