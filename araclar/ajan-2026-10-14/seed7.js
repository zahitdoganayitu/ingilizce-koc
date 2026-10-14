(()=>{localStorage.clear();
const T0=new Date().setHours(0,0,0,0), D=86400000, st={};
// 7 gün önce başladı, her gün 6 yeni (2 lvl5 + 4 seviye sırası), tekrarlarda %80 kolay %20 zor
let rnd=1;const R=()=>{rnd=(rnd*16807)%2147483647;return rnd/2147483647;};
for(let d=-7; d<0; d++){
  for(const w of WORDS){const s=st[w.id];if(s&&s.next<=d){ if(R()<0.2){s.iv=s.iv<1?1:Math.max(1,Math.round(s.iv*1.2));s.box=Math.max(1,s.box);} else {s.iv=s.iv<1?2:Math.max(2,Math.round(s.iv*2.5));s.box++;} s.next=d+s.iv; }}
  const unseen=WORDS.filter(w=>!st[w.id]);
  const l5=unseen.filter(w=>w.lvl===5).slice(0,2);
  const rest=unseen.filter(w=>!l5.includes(w)).sort((a,b)=>a.lvl-b.lvl).slice(0,4);
  for(const w of [...l5,...rest]) st[w.id]={box:1,iv:0,next:d+1};
}
const states={};for(const id in st){const s=st[id];states[id]={seen:true,box:s.box,interval:s.iv,nextReview:T0+s.next*D};}
const y=new Date(Date.now()-D), ys=y.getFullYear()+'-'+(y.getMonth()+1)+'-'+y.getDate();
const wk=Math.floor(Date.now()/(7*D));
const stats={streak:6,lastStudy:ys,newToday:6,newDate:ys,dailyGoal:6,reviews:120,freezes:2,freezeWeek:wk,cue:'Akşam yemeğinden sonra'};
localStorage.setItem('ing:srs:states',JSON.stringify(states));localStorage.setItem('ing:srs:stats',JSON.stringify(stats));
return Object.keys(states).length+' kelime, due '+Object.values(states).filter(s=>s.nextReview<=Date.now()).length;})()
