(()=>{const RD=Date, base=RD.now(); let off=0;
const FD=class extends RD{constructor(...a){if(a.length)super(...a);else super(base+off);} static now(){return base+off;}};
window.Date=FD; const savedP=window.persist; window.persist=async()=>{};
states={};stats={...DEF_STATS};
const fmt=b=>b<=1?'klasik':b===2?'dinle':b===3?'TRdenHatirla':b===4?'dikte':'yaz';
const out=[];let firstTyped=null;const fails=0.15;
for(let d=0;d<70;d++){off=d*86400000+9*3600000; rolloverDay(); buildSession();
 const c={klasik:0,dinle:0,TRdenHatirla:0,dikte:0,yaz:0};let n=0;
 let w; while((w=nextCard())&&n<200){n++;const st=states[w.id];const b=(st&&st.seen)?(st.box||0):0;c[fmt(b)]++;
   if(fmt(b)==='yaz'&&firstTyped===null)firstTyped=d;
   const r=Math.random()<fails?'again':'easy'; const res=grade(w.id,r); if(res.sameSession)session.relearn.push(w);}
 if(d%5===0||d<3)out.push('gün '+d+' '+JSON.stringify(c));}
window.Date=RD; window.persist=savedP;
const m=WORDS.filter(w=>isMastered(states[w.id])).length;
return out.join('\n')+'\nilk yaz kartı günü: '+firstTyped+' | 70. gün pekişen: '+m;})()
