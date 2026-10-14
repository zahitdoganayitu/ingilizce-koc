# WCAG kontrast: python3 kontrast.py  (çiftleri aşağıda düzenle)
def h(x):x=x.lstrip('#');return [int(x[i:i+2],16)/255 for i in (0,2,4)]
def lum(c):
    c=[v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4 for v in c];return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def mix(fg,a,bg):f,b=h(fg),h(bg);return '#'+''.join('%02x'%round((f[i]*a+b[i]*(1-a))*255) for i in range(3))
def cr(a,b):la,lb=lum(h(a)),lum(h(b));la,lb=max(la,lb),min(la,lb);return round((la+.05)/(lb+.05),2)
S='#FBFAF5'
P=[('Tekrar','#ffffff','#FF7A6B'),('Kolay','#ffffff','#4FD1A5'),('Zor','#3d2b06','#F4B740'),('ai-btn','#ffffff','#9B8CFF'),
   ('tag','#E09A2D',mix('#F4B740',.14,S)),('cloze b','#E09A2D',S),('muted2/bg3','#8085AD','#262A50'),('progress track','#262A50','#16182F')]
for n,a,b in P:print(f'{cr(a,b):5}  {"OK " if cr(a,b)>=4.5 else "FAIL"} {n}  ({a} on {b})')
