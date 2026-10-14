# readiness simülasyonu: günde 6 yeni (2 lvl5 + 4 sıradaki), hepsi 'easy' (en iyi durum) veya %20 'hard'
import random
N=258; L5=70
def run(p_hard, days=120, seed=1):
    random.seed(seed)
    words=[{'lvl':5 if i<L5 else 1,'st':None} for i in range(N)]
    out={}
    for d in range(days):
        due=[w for w in words if w['st'] and w['st']['next']<=d]
        newn=0 if len(due)>25 else 6
        unseen=[w for w in words if not w['st']]
        l5=[w for w in unseen if w['lvl']==5][:min(2,newn)]
        rest=[w for w in unseen if w['lvl']!=5][:newn-len(l5)]
        if len(l5)<min(2,newn): rest=[w for w in unseen if w not in l5][:newn-len(l5)]
        for w in due[:40]:
            s=w['st']
            if random.random()<p_hard: s['iv']=1 if s['iv']<1 else max(1,round(s['iv']*1.2))
            else: s['iv']=2 if s['iv']<1 else max(2,round(s['iv']*2.5)); s['box']+=1
            s['next']=d+s['iv']
        for w in l5+rest: w['st']={'box':1,'iv':0,'next':d}  # öğrenme adımı aynı gün; ertesi gün due
        for w in l5+rest: w['st']['next']=d+1  # yaklaşık: ikinci geçiş aynı gün başarı sayılmaz, ertesi gün ilk aralık
        seen=sum(1 for w in words if w['st'])
        m=lambda s: s and (s['box']>=6 or s['iv']>=35)
        ma=sum(1 for w in words if m(w['st'])); im=sum(1 for w in words if w['lvl']==5 and m(w['st']))
        r=min(100,round(15+85*(seen/N*0.2+ma/N*0.4+im/L5*0.4)))
        out[d+1]=(r,seen,ma,len(due))
    return out
for ph in (0,0.25):
    o=run(ph); print('p_hard',ph)
    for d in (1,7,14,30,45,60,90,120): print(' gün',d,'hazırlık%',o[d][0],'görülen',o[d][1],'pekişen',o[d][2],'due',o[d][3])
    for t in (25,50,75):
        print('  %',t,'ilk gün:',next((d for d in o if o[d][0]>=t),None))
