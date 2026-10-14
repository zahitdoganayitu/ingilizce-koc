(async()=>{const a=document.querySelector('#studyArea');const sl=ms=>new Promise(r=>setTimeout(r,ms));
if(a.querySelector('.done'))return 'DONE';
const w=session.current;const tag=(a.querySelector('.tag')||{}).textContent||'';
const rate=a.querySelector('.rate button[data-r="easy"]')||a.querySelector('.rate button');if(rate){const t=rate.dataset.r;rate.click();return 'rate:'+t;}
const opts=a.querySelectorAll('.opts button');if(opts.length){[...opts].find(b=>b.textContent===w.tr).click();await sl(700);return 'pick:'+tag;}
const inp=a.querySelector('input.type-in');if(inp){inp.value=cleanForSpeech(w.en);a.querySelector('.btn.reveal').click();return 'typed:'+tag;}
const r=a.querySelector('.btn.reveal');if(r){r.click();return 'reveal:'+tag;}
return 'UNKNOWN';})()
