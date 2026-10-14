"""Minimal CDP client (FALLOUER araclar/cdp.py uyarlaması). Port: CDP_PORT ortam değişkeni. Usage:
  cdp.py open URL            -> prints target id (stored in tgt.txt)
  cdp.py emu W H MOBILE      -> device metrics + touch
  cdp.py nav URL
  cdp.py js FILE_OR_EXPR     -> Runtime.evaluate (awaitPromise), prints JSON value
  cdp.py shot OUT.png
"""
import sys, json, socket, base64, os, struct, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get('CDP_PORT','9333'))  # her ajan/oturum kendi portunu verir

def ws_connect(url):
    host, rest = url[len('ws://'):].split('/', 1)
    h, p = host.split(':')
    s = socket.create_connection((h, int(p)))
    key = base64.b64encode(os.urandom(16)).decode()
    s.send(f"GET /{rest} HTTP/1.1\r\nHost: {host}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n".encode())
    buf = b''
    while b'\r\n\r\n' not in buf:
        buf += s.recv(4096)
    return s, buf.split(b'\r\n\r\n', 1)[1]

class WS:
    def __init__(self, url):
        self.s, self.buf = ws_connect(url)
        self.i = 0
    def send(self, txt):
        d = txt.encode(); mask = os.urandom(4)
        hdr = bytes([0x81])
        n = len(d)
        if n < 126: hdr += bytes([0x80 | n])
        elif n < 65536: hdr += bytes([0x80 | 126]) + struct.pack('>H', n)
        else: hdr += bytes([0x80 | 127]) + struct.pack('>Q', n)
        self.s.sendall(hdr + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(d)))
    def _read(self, n):
        while len(self.buf) < n:
            c = self.s.recv(1 << 20)
            if not c: raise EOFError
            self.buf += c
        r, self.buf = self.buf[:n], self.buf[n:]
        return r
    def recv(self):
        msg = b''
        while True:
            b0, b1 = self._read(2)
            n = b1 & 0x7f
            if n == 126: n = struct.unpack('>H', self._read(2))[0]
            elif n == 127: n = struct.unpack('>Q', self._read(8))[0]
            msg += self._read(n)
            if b0 & 0x80: return msg.decode('utf-8', 'replace')
    def call(self, method, **params):
        self.i += 1; mid = self.i
        self.send(json.dumps({'id': mid, 'method': method, 'params': params}))
        while True:
            m = json.loads(self.recv())
            if m.get('id') == mid:
                return m

def target_ws():
    tid = open(os.path.join(HERE, f'.tgt-{PORT}.txt')).read().strip()
    for t in json.load(urllib.request.urlopen(f'http://127.0.0.1:{PORT}/json')):
        if t['id'] == tid: return t['webSocketDebuggerUrl']

cmd = sys.argv[1]
if cmd == 'open':
    req = urllib.request.Request(f'http://127.0.0.1:{PORT}/json/new?' + sys.argv[2], method='PUT')
    t = json.load(urllib.request.urlopen(req))
    open(os.path.join(HERE, f'.tgt-{PORT}.txt'), 'w').write(t['id']); print(t['id']); sys.exit()
ws = WS(target_ws())
def apply_emu():
    if os.path.exists(os.path.join(HERE, f'.emu-{PORT}.txt')):
        w,h,mob=open(os.path.join(HERE, f'.emu-{PORT}.txt')).read().split()
        mob=mob=='1'
        ws.call('Emulation.setDeviceMetricsOverride', width=int(w), height=int(h), deviceScaleFactor=2 if mob else 1, mobile=mob)
        ws.call('Emulation.setTouchEmulationEnabled', enabled=mob, maxTouchPoints=5 if mob else 1)
        if mob: ws.call('Emulation.setUserAgentOverride', userAgent='Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1')
if cmd!='emu': apply_emu()
if cmd == 'emu':
    open(os.path.join(HERE, f'.emu-{PORT}.txt'),'w').write(' '.join(sys.argv[2:5])); apply_emu(); print('emu set')
elif cmd == 'nav':
    print(ws.call('Page.navigate', url=sys.argv[2]))
elif cmd == 'js':
    a = sys.argv[2]
    expr = open(a).read() if os.path.exists(a) else a
    r = ws.call('Runtime.evaluate', expression=expr, awaitPromise=True, returnByValue=True)
    res = r.get('result', {})
    if 'exceptionDetails' in res: print('EXC', json.dumps(res['exceptionDetails'])[:800])
    else: print(json.dumps(res.get('result', {}).get('value'), ensure_ascii=False, indent=0))
elif cmd == 'shot':
    import time; time.sleep(float(os.environ.get('W','0.6')))
    r = ws.call('Page.captureScreenshot', format='png')
    open(sys.argv[2], 'wb').write(base64.b64decode(r['result']['data'])); print('ok')
