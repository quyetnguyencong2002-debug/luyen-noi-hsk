/* Luyện Nói HSK — micro trực tiếp, chấm phát âm bằng Azure (key của người dùng, gói Free) + đường thanh điệu tính trên máy. */
{
const $=s=>document.querySelector(s), V=$('#view');
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const SPK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4z" fill="currentColor" stroke="none"/><path d="M15.5 8.5a5 5 0 0 1 0 7M18.5 5.5a9 9 0 0 1 0 13"/></svg>';
const ME='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>';
const KEY='luyennoi-v1';
let ST={prof:{name:'乔',lv:1},az:{key:'',region:'southeastasia',ok:false},hist:[],weak:{},done:{},rate:1};
try{ const s=JSON.parse(localStorage.getItem(KEY)||'null'); if(s) ST=Object.assign(ST,s); }catch(e){}
function save(){ try{ localStorage.setItem(KEY,JSON.stringify(ST)); }catch(e){} }
let tt; function toast(m,ms){ const el=$('#toast'); el.textContent=m; el.hidden=false; clearTimeout(tt); tt=setTimeout(()=>el.hidden=true,ms||2800); }
const scCls=v=>v==null?'':v>=80?'hi':v>=60?'mid':'lo';
const HZ=/[\u3400-\u9fff]/;
const chars=s=>[...(s||'')].filter(c=>HZ.test(c));

/* ---------- Dữ liệu ---------- */
let HSK=null, DLG=null, AUKEY={}, HZD={}, STK=null, STKP=null;
function loadStrokes(){ if(STK) return Promise.resolve(STK); if(!STKP) STKP=fetch('data/strokes.json').then(r=>{ if(!r.ok) throw 0; return r.json(); }).then(j=>(STK=j)).catch(e=>{ STKP=null; throw e; }); return STKP; }
async function loadData(){
  const [h,d,hz,pth]=await Promise.all([fetch('data/hsk.json').then(r=>r.json()),fetch('data/dlg.json').then(r=>r.json()).catch(()=>[]),fetch('data/hanzi.json').then(r=>r.json()).catch(()=>({})),fetch('data/path.json').then(r=>r.json())]);
  HSK=h; DLG=d; HZD=hz||{}; setupPath(pth);
  for(const L of HSK) for(const les of L.lessons) for(const it of les.items){ AUKEY[it.hz]=les.au; if(it.ex) AUKEY[it.ex]=les.au; }
  for(const s of DLG) for(const t of s.turns){ AUKEY[t.a.zh]='dlg'; for(const u of t.u) AUKEY[u.zh]='dlg'; }
}

/* ---------- Âm thanh: giọng mẫu ---------- */
let actx=null; const ctx=()=>{ if(!actx) actx=new (window.AudioContext||window.webkitAudioContext)(); if(actx.state==='suspended') actx.resume().catch(()=>{}); return actx; };
const AUD={}, AUDP={}, BUF=new Map();
function audFile(k){ if(AUD[k]) return Promise.resolve(AUD[k]); if(!AUDP[k]) AUDP[k]=fetch('audio/'+k+'.json').then(r=>{ if(!r.ok) throw 0; return r.json(); }).then(j=>(AUD[k]=j)).catch(e=>{ delete AUDP[k]; throw e; }); return AUDP[k]; }
async function refBuffer(text){
  if(BUF.has(text)) return BUF.get(text);
  const k=AUKEY[text]; if(!k) return null; const j=await audFile(k); const b64=j[text]; if(!b64) return null;
  const bin=atob(b64), u=new Uint8Array(bin.length); for(let i=0;i<bin.length;i++) u[i]=bin.charCodeAt(i);
  const buf=await ctx().decodeAudioData(u.buffer); BUF.set(text,buf); return buf;
}
let playing=null;
function stopPlay(){ try{ if(playing) playing.stop(); }catch(e){} playing=null; }
async function playBuf(buf,rate){ stopPlay(); const c=ctx(), s=c.createBufferSource(); s.buffer=buf; s.playbackRate.value=rate||1; s.connect(c.destination); s.start(); playing=s; return new Promise(r=>s.onended=r); }
async function playRef(text){
  try{ const b=await refBuffer(text); if(b) return playBuf(b,ST.rate); }catch(e){}
  if('speechSynthesis' in window){ const v=speechSynthesis.getVoices().find(x=>/^zh/i.test(x.lang)); if(v){ const u=new SpeechSynthesisUtterance(text); u.lang='zh-CN'; u.voice=v; u.rate=.85; speechSynthesis.speak(u); return; } }
  toast('Câu này chưa có giọng mẫu.');
}
async function to16k(buf){ // AudioBuffer → Float32 16 kHz mono
  const n=Math.ceil(buf.duration*16000), oc=new OfflineAudioContext(1,n,16000), s=oc.createBufferSource(); s.buffer=buf; s.connect(oc.destination); s.start(); const r=await oc.startRendering(); return r.getChannelData(0);
}

/* ---------- Ghi âm ---------- */
const REC={stream:null,src:null,node:null,chunks:[],on:false,t0:0,lvl:0};
async function micOpen(){
  if(REC.stream&&REC.stream.active) return true;
  if(!navigator.mediaDevices||!navigator.mediaDevices.getUserMedia){ toast('Trình duyệt này không cho dùng micro. Hãy mở bằng Chrome (Android) hoặc Safari (iPhone).',5000); return false; }
  try{ REC.stream=await navigator.mediaDevices.getUserMedia({audio:{channelCount:1,echoCancellation:true,noiseSuppression:true,autoGainControl:true}}); return true; }
  catch(e){ toast('Chưa được phép dùng micro. Bấm biểu tượng ổ khóa cạnh địa chỉ trang → cho phép Micro, rồi thử lại.',6000); return false; }
}
function micClose(){ try{ if(REC.stream) REC.stream.getTracks().forEach(t=>t.stop()); }catch(e){} REC.stream=null; }
async function recStart(){
  if(!(await micOpen())) return false; const c=ctx(); stopPlay();
  REC.src=c.createMediaStreamSource(REC.stream); REC.node=c.createScriptProcessor(4096,1,1); REC.chunks=[]; REC.on=true; REC.t0=performance.now();
  REC.node.onaudioprocess=e=>{ if(!REC.on) return; const d=e.inputBuffer.getChannelData(0); REC.chunks.push(new Float32Array(d)); let s=0; for(let i=0;i<d.length;i+=8) s+=d[i]*d[i]; REC.lvl=Math.min(1,Math.sqrt(s/(d.length/8))*6); const b=$('#micb'); if(b) b.style.setProperty('--lv',REC.lvl.toFixed(2)); };
  REC.src.connect(REC.node); REC.node.connect(c.destination); return true;
}
async function recStop(){
  REC.on=false; try{ REC.src.disconnect(); REC.node.disconnect(); }catch(e){}
  const c=ctx(), n=REC.chunks.reduce((a,b)=>a+b.length,0); if(!n) return null;
  const buf=c.createBuffer(1,n,c.sampleRate); let o=0; for(const ch of REC.chunks){ buf.copyToChannel(ch,0,o); o+=ch.length; }
  let x=await to16k(buf);
  // cắt lặng hai đầu, chừa 0,25 s
  let a=0,b=x.length-1; const thr=0.02; const win=320;
  const rms=i=>{ let s=0; for(let k=i;k<Math.min(x.length,i+win);k++) s+=x[k]*x[k]; return Math.sqrt(s/win); };
  while(a<x.length-win&&rms(a)<thr) a+=win; while(b>win&&rms(b-win)<thr) b-=win;
  if(b-a<1600) return {x,buf,empty:true};
  x=x.slice(Math.max(0,a-4000),Math.min(x.length,b+4000));
  // chuẩn hóa mức
  let pk=0; for(const v of x) pk=Math.max(pk,Math.abs(v)); if(pk>0&&pk<0.5){ const g=0.6/pk; for(let i=0;i<x.length;i++) x[i]*=g; }
  const out=c.createBuffer(1,x.length,16000); out.copyToChannel(x,0); return {x,buf:out};
}
function toWav16(x){ const n=x.length, b=new ArrayBuffer(44+n*2), v=new DataView(b); const w=(o,s)=>{ for(let i=0;i<s.length;i++) v.setUint8(o+i,s.charCodeAt(i)); };
  w(0,'RIFF'); v.setUint32(4,36+n*2,true); w(8,'WAVE'); w(12,'fmt '); v.setUint32(16,16,true); v.setUint16(20,1,true); v.setUint16(22,1,true); v.setUint32(24,16000,true); v.setUint32(28,32000,true); v.setUint16(32,2,true); v.setUint16(34,16,true); w(36,'data'); v.setUint32(40,n*2,true);
  for(let i=0;i<n;i++){ const s=Math.max(-1,Math.min(1,x[i])); v.setInt16(44+i*2,s<0?s*0x8000:s*0x7fff,true); } return b; }

/* ---------- Azure Pronunciation Assessment ---------- */
const azReady=()=>!!(ST.az.key&&ST.az.region);
async function azRest(x,ref){
  const cfg={ReferenceText:ref||'',GradingSystem:'HundredMark',Granularity:'Phoneme',Dimension:'Comprehensive',EnableMiscue:!!ref,NBestPhonemeCount:5,PhonemeAlphabet:'SAPI'};
  const b64=btoa(unescape(encodeURIComponent(JSON.stringify(cfg))));
  const url=`https://${ST.az.region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=zh-CN&format=detailed`;
  let r; try{ r=await fetch(url,{method:'POST',headers:{'Ocp-Apim-Subscription-Key':ST.az.key.trim(),'Content-Type':'audio/wav; codecs=audio/pcm; samplerate=16000','Pronunciation-Assessment':b64,'Accept':'application/json'},body:toWav16(x)}); }
  catch(e){ const er=new Error('Không kết nối được máy chủ Azure (mạng/tường lửa chặn?)'); er.net=true; throw er; }
  if(r.status===401||r.status===403) throw new Error('Key hoặc Region chưa đúng (HTTP '+r.status+'). Kiểm tra lại KEY 1 và Region = southeastasia.');
  if(r.status===429) throw new Error('Đã hết lượt miễn phí tạm thời (HTTP 429), thử lại sau ít phút.');
  if(!r.ok) throw new Error('Azure trả lỗi HTTP '+r.status);
  const j=await r.json(); if(j.RecognitionStatus&&j.RecognitionStatus!=='Success') return {nomatch:true}; return j;
}
async function azAssess(x,ref){ try{ return await azRest(x,ref); }catch(e){ if(e.net&&window.SpeechSDK) return azSdk(x,ref); throw e; } }
function azSdk(x,ref){
  return new Promise((resolve,reject)=>{
    const S=window.SpeechSDK; if(!S) return reject(new Error('SDK chưa tải xong'));
    const cfg=S.SpeechConfig.fromSubscription(ST.az.key.trim(),ST.az.region); cfg.speechRecognitionLanguage='zh-CN'; cfg.outputFormat=S.OutputFormat.Detailed;
    const fmt=S.AudioStreamFormat.getWaveFormatPCM(16000,16,1), push=S.AudioInputStream.createPushStream(fmt);
    push.write(toWav16(x).slice(44)); push.close();
    const rec=new S.SpeechRecognizer(cfg,S.AudioConfig.fromStreamInput(push));
    const pa=new S.PronunciationAssessmentConfig(ref||'',S.PronunciationAssessmentGradingSystem.HundredMark,S.PronunciationAssessmentGranularity.Phoneme,!!ref);
    try{ pa.nbestPhonemeCount=5; }catch(e){}
    pa.applyTo(rec);
    const to=setTimeout(()=>{ try{ rec.close(); }catch(e){} reject(new Error('timeout')); },25000);
    rec.recognizeOnceAsync(r=>{ clearTimeout(to); try{ rec.close(); }catch(e){}
      if(r.reason===S.ResultReason.Canceled){ const cd=S.CancellationDetails.fromResult(r); return reject(new Error(cd.errorDetails||'canceled')); }
      if(r.reason===S.ResultReason.NoMatch) return resolve({nomatch:true});
      let j=null; try{ j=JSON.parse(r.properties.getProperty(S.PropertyId.SpeechServiceResponse_JsonResult)); }catch(e){}
      resolve(j||{}); }, e=>{ clearTimeout(to); try{ rec.close(); }catch(_){} reject(new Error(String(e))); });
  });
}
// Đổi kết quả Azure thành từng chữ: {hz, acc, err, t0, t1, ph:[{p,acc,nb}]}
function azPerChar(j,target){
  const nb=j&&j.NBest&&j.NBest[0]; if(!nb) return null;
  const pa=nb.PronunciationAssessment||nb, out=[];
  for(const w of nb.Words||[]){
    const wp=w.PronunciationAssessment||w, cs=chars(w.Word), syl=w.Syllables||[], phs=w.Phonemes||[];
    const T=o=>o.Offset/1e7, D=o=>o.Duration/1e7;
    cs.forEach((hz,k)=>{
      const s=syl[k]; let t0,t1;
      if(s&&s.Offset!=null){ t0=T(s); t1=t0+D(s); } else if(w.Offset!=null){ const a=T(w), d=D(w)/Math.max(1,cs.length); t0=a+k*d; t1=t0+d; }
      const ph=phs.filter(p=>p.Offset!=null&&t0!=null?(T(p)>=t0-0.01&&T(p)<t1-0.005):false).map(p=>({p:p.Phoneme,acc:(p.PronunciationAssessment||p).AccuracyScore,nb:((p.PronunciationAssessment||p).NBestPhonemes||[]).map(x=>({p:x.Phoneme,s:x.Score}))}));
      out.push({hz,acc:s?(s.PronunciationAssessment||s).AccuracyScore:wp.AccuracyScore,err:wp.ErrorType||'None',t0,t1,ph,sy:s&&s.Syllable});
    });
  }
  // gióng theo câu đích (miscue có thể chèn/bỏ chữ)
  const tg=chars(target), res=[]; let i=0;
  for(const c of tg){
    let k=i; while(k<out.length&&out[k].hz!==c&&out[k].err==='Insertion') k++;
    if(k<out.length&&(out[k].hz===c||out[k].err==='Omission'||out[k].err==='Mispronunciation'||out[k].err==='None')){ res.push(Object.assign({},out[k],{hz:c})); i=k+1; }
    else res.push({hz:c,acc:0,err:'Omission',ph:[]});
  }
  return {chars:res,acc:pa.AccuracyScore,flu:pa.FluencyScore,comp:pa.CompletenessScore,pron:pa.PronScore,text:nb.Display||j.DisplayText||''};
}

/* ---------- Mẹo sửa cho người Việt ---------- */
const INI=['zh','ch','sh','b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s','y','w'];
const split=b=>{ for(const i of INI) if(b.startsWith(i)) return [i,b.slice(i.length)]; return ['',b]; };
const TIPI={zh:'zh: cong đầu lưỡi lên chạm vòm miệng phía sau lợi (uốn lưỡi), không bật hơi — khác "tr" tiếng Việt ở chỗ lưỡi cong nhiều hơn.',
 ch:'ch: uốn lưỡi như zh nhưng BẬT HƠI mạnh (để tay trước miệng thấy luồng hơi).',
 sh:'sh: uốn lưỡi, để hơi xì qua khe — như "s" miền Bắc nhưng lưỡi cong lên.',
 r:'r: uốn lưỡi như sh nhưng rung dây thanh, gần "r" nhẹ; không đọc thành "z" hay "l".',
 z:'z: đầu lưỡi chạm sau răng trên, đọc như "ch" tiếng Việt nhưng lưỡi phẳng ra trước, không bật hơi (ts).',
 c:'c: như z nhưng bật hơi mạnh (ts‘). Không đọc thành "x" hay "k".',
 s:'s: đầu lưỡi sau răng, lưỡi phẳng, như "x" tiếng Việt.',
 j:'j: mặt lưỡi chạm ngạc cứng, môi dẹt, không bật hơi — gần "ch" tiếng Việt nhưng lưỡi rộng hơn.',
 q:'q: như j nhưng bật hơi mạnh. Không đọc như "k" hay "c".',
 x:'x: mặt lưỡi gần ngạc cứng, môi dẹt, hơi xì nhẹ — mềm hơn "x" tiếng Việt.',
 p:'p: bật hơi mạnh (p‘). Tiếng Việt không có âm này ở đầu từ — đừng đọc thành "b".',
 t:'t: bật hơi mạnh như "th" tiếng Việt.',
 k:'k: bật hơi mạnh như "kh" nhưng ngắn và gọn, không xát.',
 b:'b: không bật hơi, không rung — gần "p" trong "pin" nhẹ; đừng đọc thành "b" Việt (có hơi ngậm).',
 d:'d: không bật hơi, như "t" tiếng Việt (không phải "đ").',
 g:'g: không bật hơi, như "c/k" tiếng Việt.',
 h:'h: xát ở cuống họng, mạnh hơn "h" tiếng Việt, gần "kh".',
 f:'f: răng trên chạm môi dưới như "ph".', n:'n: đầu lưỡi chạm lợi trên.', l:'l: đầu lưỡi chạm lợi, đừng lẫn với n.', m:'m: như "m".'};
const TIPF=f=>/ü|^u$/.test(f)?'ü: tròn môi như nói "u" nhưng lưỡi giữ vị trí "i".':/ng$/.test(f)?'-ng: kết thúc ở cuống lưỡi (như "ng" tiếng Việt), miệng mở, không khép môi.':/n$/.test(f)?'-n: kết thúc đầu lưỡi chạm lợi trên, đừng đọc thành -ng.':
 /^e$/.test(f)?'e: miệng hé, lưỡi lùi sau, gần "ơ" chuyển sang "ưa" — không đọc thành "e" Việt.':/^er$/.test(f)?'er: "ơ" rồi cong lưỡi lên.':/^i$/.test(f)?'i sau z/c/s/zh/ch/sh/r là âm "ư" ngắn, không phải "i".':/ian/.test(f)?'ian đọc gần "iên".':/ui/.test(f)?'ui đọc như "uây".':/iu/.test(f)?'iu đọc như "iêu".':/un/.test(f)?'un sau j/q/x/y là "uyn"; sau âm khác là "uân".':'';
const TIPT={1:'Thanh 1: giữ giọng CAO và BẰNG như đang hát một nốt dài; đừng để rơi xuống cuối.',2:'Thanh 2: đi từ giữa lên cao, như hỏi lại "hả?" hoặc dấu sắc kéo dài.',
 3:'Thanh 3: hạ giọng xuống thấp (gần dấu nặng nhưng kéo dài); đứng cuối câu thì hơi vòng lên.',4:'Thanh 4: rơi mạnh từ cao xuống thấp, dứt khoát như ra lệnh.',5:'Thanh nhẹ: đọc ngắn, nhẹ, không nhấn.'};
function tipsFor(item,tg){ // tg = {b,t:[...]}
  const out=[]; if(!tg) return out; const [ini,fin]=split(tg.b);
  const lowPh=(item.ph||[]).filter(p=>p.acc!=null&&p.acc<60);
  const phTxt=lowPh.map(p=>String(p.p||'').toLowerCase());
  const iniBad=ini&&phTxt.some(p=>p.replace(/[\s\d]/g,'')===ini), finBad=phTxt.some(p=>p.replace(/[\s\d]/g,'')===fin||(/\d/.test(p)&&p.replace(/[\s\d]/g,'')===fin));
  if(iniBad&&TIPI[ini]) out.push(TIPI[ini]);
  if(finBad&&TIPF(fin)) out.push(TIPF(fin));
  if(item.toneWrong&&tg.t[0]!==5) out.push(TIPT[tg.t[tg.t.length-1]]);
  if(!out.length&&item.acc!=null&&item.acc<60){ if(TIPI[ini]) out.push(TIPI[ini]); else if(TIPF(fin)) out.push(TIPF(fin)); if(tg.t[0]!==5) out.push(TIPT[tg.t[tg.t.length-1]]); }
  return out.slice(0,3);
}

/* ---------- So đường thanh điệu với giọng mẫu ---------- */
function toneCompare(userX,refX,tones,times){
  const ex=tones.map(t=>t.t[t.t.length-1]);
  const u=HZPitch.analyze(userX,ex,{times}), r=refX?HZPitch.analyze(refX,ex):null;
  return {u,r,notes:[]}; // luật tự kết luận sai thanh báo nhầm ~26% trên giọng chuẩn → chỉ dùng để vẽ
  if(!u.ok) return {u,r,notes:[]};
  const slope=s=>s&&s.chao?s.chao[4]-s.chao[0]:null, dip=s=>s&&s.chao?Math.min(...s.chao.slice(1,4))-Math.min(s.chao[0],s.chao[4]):null;
  const notes=u.syl.map((s,k)=>{ const t=ex[k]; if(t===5||!s.chao) return null; const sl=slope(s), rs=r&&r.ok?slope(r.syl[k]):null;
    if(t===4&&sl>-0.6) return {k,msg:'thanh 4 chưa rơi xuống'}; if(t===2&&sl<0.4) return {k,msg:'thanh 2 chưa đi lên'};
    if(t===1&&Math.abs(sl)>1.4) return {k,msg:sl>0?'thanh 1 đang bị lên giọng':'thanh 1 đang bị rơi giọng'};
    if(t===3&&sl>1.2&&k<ex.length-1) return {k,msg:'thanh 3 giữa câu nên hạ thấp, không vòng lên'};
    if(rs!=null&&Math.sign(rs)!==Math.sign(sl)&&Math.abs(rs-sl)>2) return {k,msg:'hướng giọng khác giọng mẫu'}; return null; }).filter(Boolean);
  return {u,r,notes};
}
function drawPitch(cv,cmp,n){
  const r=cv.getBoundingClientRect(), dpr=window.devicePixelRatio||1; cv.width=r.width*dpr; cv.height=r.height*dpr; const g=cv.getContext('2d'); g.scale(dpr,dpr);
  const W=r.width,H=r.height,pad=8,slot=(W-pad*2)/n, cs=getComputedStyle(document.documentElement);
  g.strokeStyle=cs.getPropertyValue('--line'); g.lineWidth=1; for(let k=1;k<n;k++){ g.beginPath(); g.moveTo(pad+k*slot,6); g.lineTo(pad+k*slot,H-6); g.stroke(); }
  const plot=(an,color,dash,w)=>{ if(!an||!an.ok) return; const fr=an.frames; g.strokeStyle=color; g.lineWidth=w; g.setLineDash(dash); g.lineJoin='round'; g.lineCap='round';
    an.syl.forEach((s,k)=>{ const sg=s.seg||an.segs[k]; if(!sg) return; const [a,b]=sg; const pts=[]; for(let i=a;i<=b;i++) if(fr[i]&&fr[i].f) pts.push([i,12*Math.log2(fr[i].f/an.base)]);
      if(pts.length<2) return; g.beginPath(); pts.forEach(([i,v],m)=>{ const x=pad+k*slot+slot*0.08+(i-a)/Math.max(1,b-a)*slot*0.84, y=H/2-v*(H/2-12)/7; m?g.lineTo(x,Math.max(4,Math.min(H-4,y))):g.moveTo(x,Math.max(4,Math.min(H-4,y))); }); g.stroke(); });
    g.setLineDash([]); };
  plot(cmp.r,cs.getPropertyValue('--ref'),[5,4],2.5); plot(cmp.u,cs.getPropertyValue('--seal'),[],3);
}

/* ---------- Thẻ luyện (dùng chung) ---------- */
let CUR=null; // {target:{zh,py,vi,t}, el, onDone, last}
function micUI(show){ const m=$('#mic'); m.hidden=!show; document.body.classList.toggle('has-mic',show); }
function micLabel(t){ const l=$('#micl'); if(l) l.textContent=t; }
function practiceHTML(tg,opt={}){
  const cs=chars(tg.zh), size=cs.length<=2?'big':cs.length>8?'sm':'';
  return `<div class="target"><div class="cells ${size}" id="cells">${cs.map((c,k)=>`<button class="cell" data-k="${k}"><span class="g">${esc(c)}</span><span class="s"></span></button>`).join('')}</div>
    <div class="tpy">${esc(tg.py)}</div><div class="tvi">${esc(tg.vi)}</div>
    <div class="acts"><button class="btn sm" id="pref">${SPK} Nghe mẫu</button><button class="btn sm" id="pslow">Nghe chậm</button><button class="btn sm" id="pme" hidden>${ME} Nghe lại tôi</button></div></div>
    <div id="pres"></div>`;
}
function bindPractice(root,tg,onDone){
  CUR={tg,root,onDone,last:null,sel:null};
  root.querySelector('#pref').onclick=()=>playRef(tg.zh);
  root.querySelector('#pslow').onclick=async()=>{ const b=await refBuffer(tg.zh).catch(()=>null); if(b) playBuf(b,0.75); else playRef(tg.zh); };
  root.querySelector('#pme').onclick=()=>{ if(CUR.last&&CUR.last.buf) playBuf(CUR.last.buf,1); };
  root.querySelector('#cells').onclick=e=>{ const c=e.target.closest('.cell'); if(!c||!CUR.last) return; const k=+c.dataset.k; CUR.sel=CUR.sel===k?null:k; renderDetail(); };
  micUI(true); micLabel(azReady()?'Giữ nút đỏ để nói, thả ra để chấm':'Giữ nút đỏ để nói, thả ra để chấm (chưa có key Azure: chỉ so đường thanh điệu)');
}
async function assess(rec){
  const tg=CUR.tg, res=CUR.root.querySelector('#pres'), refX=await refBuffer(tg.zh).then(b=>b?to16k(b):null).catch(()=>null);
  res.innerHTML=`<div class="res"><div class="muted small"><span class="spin"></span> Đang chấm…</div></div>`;
  let az=null, err=null;
  if(azReady()){ try{ const j=await azAssess(rec.x,tg.zh); az=j.nomatch?{nomatch:true}:azPerChar(j,tg.zh); }catch(e){ err=e.message||String(e); } }
  const times=az&&az.chars&&az.chars.every(c=>c.t0!=null)?az.chars.map(c=>[c.t0,c.t1]):null;
  const cmp=toneCompare(rec.x,refX,tg.t,times);
  const per=chars(tg.zh).map((hz,k)=>{ const a=az&&az.chars?az.chars[k]:null, note=cmp.notes.find(n=>n.k===k);
    const it={hz,acc:a?a.acc:null,err:a?a.err:null,ph:a?a.ph:[],toneWrong:!!note,toneNote:note&&note.msg};
    return it; });
  const overall=az&&az.pron!=null?Math.round(az.pron):null;
  CUR.last={rec,az,cmp,per,overall,err,buf:rec.buf};
  renderResult();
  logAttempt(tg,CUR.last);
  if(CUR.onDone) CUR.onDone(CUR.last);
}
function renderResult(){
  const L=CUR.last, tg=CUR.tg, res=CUR.root.querySelector('#pres');
  CUR.root.querySelector('#pme').hidden=false;
  CUR.root.querySelectorAll('.cell').forEach((c,k)=>{ const p=L.per[k]; c.classList.remove('ok','mid','bad','miss');
    const v=p.err==='Omission'?null:p.acc; const cl=p.err==='Omission'?'miss':v==null?'':v>=80?'ok':v>=60?'mid':'bad'; if(cl) c.classList.add(cl);
    const py=tg.t[k]; c.querySelector('.s').textContent=p.err==='Omission'?'thiếu':v==null?'':Math.round(v); c.setAttribute('aria-pressed',CUR.sel===k); });
  if(L.rec.empty){ res.innerHTML='<div class="res"><div>Máy chưa nghe thấy tiếng. Giữ nút đỏ, nói to và rõ, rồi mới thả ra.</div></div>'; return; }
  const az=L.az, bars=az&&!az.nomatch?[['Chính xác',az.acc],['Trôi chảy',az.flu],['Đầy đủ',az.comp]]:[];
  const worst=L.per.map((p,k)=>({p,k})).filter(o=>o.p.acc!=null&&(o.p.acc<70||o.p.toneWrong)).sort((a,b)=>(a.p.acc||0)-(b.p.acc||0)).slice(0,2);
  const tips=[]; worst.forEach(o=>tipsFor(o.p,tg.t[o.k]).forEach(t=>{ if(!tips.includes(t)) tips.push(`<b class="han">${esc(o.p.hz)}</b> — ${t}`); }));
  res.innerHTML=`<div class="res">
    <div class="score"><div class="ring" style="--v:${L.overall||0};--c:var(--${L.overall>=80?'jade':L.overall>=60?'warn':'bad'})">${L.overall==null?'—':L.overall}</div>
      <div class="bars">${bars.map(([l,v])=>`<span>${l}</span><span class="bar"><i style="width:${v||0}%"></i></span><b>${v==null?'—':Math.round(v)}</b>`).join('')||`<span class="muted small" style="grid-column:1/-1">${L.err?'Azure lỗi: '+esc(L.err)+' — đang dùng chấm thanh điệu trên máy.':'Chưa có key Azure nên chưa chấm điểm. Xem đường giọng của anh so với giọng mẫu bên dưới; thêm key ở tab Cài đặt để chấm từng âm.'}</span>`}</div></div>
    ${az&&az.text?`<div class="heard">Máy nghe được: <b>${esc(az.text)}</b></div>`:''}
    ${az&&az.nomatch?'<div class="heard">Azure không nhận ra câu nào — nói to, rõ và sát micro hơn.</div>':''}
    ${tips.length?`<div class="tips">${tips.map(t=>`<div>${t}</div>`).join('')}</div>`:L.overall>=85?'<div class="tips"><div>Tốt lắm! Thử đọc nhanh và liền mạch hơn như người bản ngữ.</div></div>':''}
    ${L.cmp.notes.length?`<div class="note">Thanh điệu (đo trên máy, tham khảo): ${L.cmp.notes.map(n=>`<b class="han">${esc(L.per[n.k].hz)}</b> ${esc(n.msg)}`).join(' · ')}</div>`:''}
    <div><div class="legend"><span><i style="background:var(--ref)"></i>Giọng mẫu</span><span><i style="background:var(--seal)"></i>Giọng anh</span><span>Đường giọng: lên/xuống phải cùng hướng với mẫu</span></div>
      <div class="fig"><canvas id="pcv"></canvas></div></div>
    <div id="pdet"></div>
    <div class="acts"><button class="btn sm" id="pagain">↻ Đọc lại</button></div></div>`;
  const cv=res.querySelector('#pcv'); requestAnimationFrame(()=>drawPitch(cv,L.cmp,L.per.length));
  res.querySelector('#pagain').onclick=()=>{ res.innerHTML=''; CUR.root.querySelectorAll('.cell').forEach(c=>{ c.className='cell'; c.querySelector('.s').textContent=''; }); toast('Giữ nút đỏ và đọc lại.'); };
  renderDetail();
}
function renderDetail(){
  const d=CUR.root.querySelector('#pdet'); if(!d) return; CUR.root.querySelectorAll('.cell').forEach((c,k)=>c.setAttribute('aria-pressed',CUR.sel===k));
  if(CUR.sel==null){ d.innerHTML=''; return; }
  const k=CUR.sel, p=CUR.last.per[k], t=CUR.tg.t[k], tips=tipsFor(Object.assign({},p,{acc:p.acc==null?50:p.acc}),t);
  d.innerHTML=`<div class="detail"><div><b class="han" style="font-size:1.4rem">${esc(p.hz)}</b> · ${esc(t.b)} thanh ${t.t.join(' hoặc ')} · ${p.err==='Omission'?'<b class="lo">bỏ sót</b>':p.acc==null?'':'điểm <b class="'+scCls(p.acc)+'">'+Math.round(p.acc)+'</b>'}${p.toneNote?' · '+esc(p.toneNote):''}</div>
    ${p.ph&&p.ph.length?`<div class="ph">${p.ph.map(x=>`<span>${esc(x.p)} <b class="${scCls(x.acc)}">${x.acc==null?'':Math.round(x.acc)}</b>${x.nb&&x.nb[0]&&x.nb[0].p!==x.p&&x.acc<60?' → nghe giống '+esc(x.nb[0].p):''}</span>`).join('')}</div>`:''}
    ${tips.map(x=>`<div>${x}</div>`).join('')}
    <div class="acts" style="justify-content:flex-start"><button class="btn sm" id="pone">${SPK} Nghe mẫu chữ này</button></div></div>`;
  d.querySelector('#pone').onclick=()=>playRef(p.hz);
}
function logAttempt(tg,L){
  if(L.rec.empty||L.overall==null) return;
  ST.hist.push({t:Date.now(),zh:tg.zh,s:L.overall,a:L.az&&L.az.acc!=null?Math.round(L.az.acc):null,az:!!(L.az&&!L.az.nomatch)});
  if(ST.hist.length>2000) ST.hist=ST.hist.slice(-2000);
  L.per.forEach((p,k)=>{ const t=tg.t[k]; if(!t) return; const bad=(p.acc!=null&&p.acc<60)||p.toneWrong; const key=t.b+t.t[t.t.length-1];
    const w=ST.weak[key]||(ST.weak[key]={n:0,bad:0,hz:p.hz}); w.n++; if(bad) w.bad++; });
  ST.done[tg.zh]=Math.max(ST.done[tg.zh]||0,L.overall); save();
}
// nút micro: giữ để nói (hoặc chạm 1 lần để bắt đầu, chạm lần nữa để dừng)
{ const b=$('#micb'); let down=0, toggle=false, busy=false;
  const start=async()=>{ if(busy||REC.on) return; const ok=await recStart(); if(!ok) return; b.classList.add('on'); micLabel('Đang nghe… thả ra để chấm'); };
  const stop=async()=>{ if(!REC.on) return; b.classList.remove('on'); busy=true; b.disabled=true; micLabel('Đang xử lý…');
    const rec=await recStop(); b.disabled=false; busy=false; micLabel('Giữ nút đỏ để nói, thả ra để chấm');
    if(rec&&CUR) assess(rec); };
  b.addEventListener('pointerdown',e=>{ e.preventDefault(); if(!CUR) return; if(toggle&&REC.on){ toggle=false; stop(); return; } down=performance.now(); start(); });
  b.addEventListener('pointerup',()=>{ if(!REC.on&&!down) return; if(performance.now()-down<350&&!toggle){ toggle=true; micLabel('Đang nghe… chạm lần nữa để chấm'); down=0; return; } down=0; if(!toggle) stop(); });
  b.addEventListener('pointercancel',()=>{ if(!toggle) stop(); });
  b.addEventListener('contextmenu',e=>e.preventDefault());
  document.addEventListener('keydown',e=>{ if(e.code==='Space'&&CUR&&!e.target.matches('input,select,textarea')){ e.preventDefault(); if(!REC.on) start(); } });
  document.addEventListener('keyup',e=>{ if(e.code==='Space'&&CUR&&REC.on){ e.preventDefault(); stop(); } });
  setInterval(()=>{ if(REC.on&&performance.now()-REC.t0>15000){ toggle=false; stop(); } },500);
}

/* ---------- Màn hình ---------- */
let view=['hoi-thoai','luyen','on-tu','tien-bo','cai-dat'].includes(location.hash.slice(1))?location.hash.slice(1):'hoi-thoai', SUB=null;
function go(v,sub){ view=v; SUB=sub||null; CUR=null; micUI(false); stopPlay(); try{ history.replaceState(null,'','#'+v); }catch(e){} render(); window.scrollTo(0,0); }
document.querySelectorAll('nav.tabs button').forEach(b=>b.onclick=()=>go(b.dataset.v));
function render(){
  document.querySelectorAll('nav.tabs button').forEach(b=>b.setAttribute('aria-selected',b.dataset.v===view));
  const azb=$('#azb'); azb.textContent=ST.az.ok?'Chấm Azure':'Chấm cơ bản'; azb.classList.toggle('on',!!ST.az.ok);
  if(!HSK){ V.innerHTML='<p class="muted"><span class="spin"></span> Đang tải dữ liệu…</p>'; return; }
  if(view==='hoi-thoai') return SUB?renderChat():renderScenarios();
  if(view==='luyen') return SUB&&SUB.ptest?renderPTest():SUB&&SUB.item!=null?renderDrill():SUB&&SUB.lesson?renderLesson():renderLessons();
  if(view==='on-tu') return renderSRS();
  if(view==='tien-bo') return renderProgress();
  return renderSettings();
}
/* Hội thoại */
const KIND={s:'Đơn giản',n:'Tự nhiên',p:'Phong cách của anh'};
function renderScenarios(){
  V.innerHTML=`<h2>Hội thoại theo tình huống</h2><p class="muted small">Đối phương nói trước. Anh chọn một trong 3 câu trả lời (đơn giản, tự nhiên, hoặc theo phong cách của anh), giữ micro và nói. Máy chấm từng chữ rồi đi tiếp.</p>
  ${ST.az.ok?'':'<div class="tip" style="margin:10px 0">Chưa có key Azure nên chưa chấm điểm, chỉ so đường thanh điệu. <a href="#cai-dat" id="gs">Thêm key miễn phí</a> để chấm từng âm như ELSA.</div>'}
  <div class="scn">${DLG.map(s=>{ const best=s.turns.flatMap(t=>t.u.map(u=>ST.done[u.zh]||0)).filter(Boolean); return `<button data-s="${s.id}"><strong>${esc(s.title)}</strong><span>${esc(s.who)}</span>${best.length?`<em>Đã luyện ${best.length} câu · TB ${Math.round(best.reduce((a,b)=>a+b,0)/best.length)}</em>`:''}</button>`; }).join('')}</div>
  ${DLG.length?'':'<p class="muted">Chưa có kịch bản.</p>'}`;
  V.querySelectorAll('[data-s]').forEach(b=>b.onclick=()=>go('hoi-thoai',{s:DLG.find(s=>s.id===b.dataset.s),i:0,log:[],pick:null}));
  const gs=$('#gs'); if(gs) gs.onclick=e=>{ e.preventDefault(); go('cai-dat'); };
}
function renderChat(){
  const S=SUB, sc=S.s, T=sc.turns, i=S.i;
  const hist=S.log.map(l=>`<div class="msg ai"><span class="who">${esc(sc.who.split(',')[0])}</span><div class="zh">${esc(l.a.zh)}</div><div class="vil">${esc(l.a.vi)}</div></div>
     ${l.u?`<div class="msg me"><span class="who">Anh · ${KIND[l.u.k]||''} · ${l.s==null?'—':l.s} điểm</span><div class="zh">${esc(l.u.zh)}</div></div>`:''}`).join('');
  const t=T[i], last=i===T.length-1;
  if(!t){ return renderSummary(); }
  V.innerHTML=`<div class="row" style="justify-content:space-between"><div><h2>${esc(sc.title)}</h2><div class="muted small">${esc(sc.who)} · lượt ${i+1}/${T.length}</div></div><button class="btn sm" id="back">← Tình huống khác</button></div>
   ${sc.words.length?`<div class="note" style="margin:8px 0">Từ mới: ${sc.words.map(w=>`<b class="han">${esc(w.hz)}</b> ${esc(w.py)} – ${esc(w.vi)}`).join(' · ')}</div>`:''}
   <div class="chat">${hist}
    <div class="msg ai"><span class="who">${esc(sc.who.split(',')[0])}</span><div class="line"><button class="spk" id="ai">${SPK}</button><div><div class="zh">${esc(t.a.zh)}</div><div class="pyl">${esc(t.a.py)}</div><div class="vil">${esc(t.a.vi)}</div></div></div></div>
    ${last?`<div class="acts"><button class="btn pri" id="fin">Kết thúc &amp; xem tổng kết</button></div>`:`
    ${S.pick==null?`<h3>Anh trả lời thế nào?</h3><div class="opts">${t.u.map((u,k)=>`<button class="opt" data-k="${k}"><div style="flex:1"><div class="k">${KIND[u.k]||''}</div><div class="zh">${esc(u.zh)}</div><div class="pyl">${esc(u.py)}</div><div class="vil">${esc(u.vi)}</div><div class="why">${esc(u.why)}</div></div></button>`).join('')}</div>${t.tip?`<div class="tip" style="margin-top:8px">💡 ${esc(t.tip)}</div>`:''}`
    :`<div class="card" id="prac">${practiceHTML(t.u[S.pick])}<div class="acts" style="margin-top:10px"><button class="btn sm" id="other">Chọn câu khác</button><button class="btn pri" id="next">Tiếp tục →</button></div></div>`}`}
   </div>`;
  $('#back').onclick=()=>go('hoi-thoai');
  $('#ai').onclick=()=>playRef(t.a.zh);
  if(!S.played){ S.played=true; playRef(t.a.zh); }
  V.querySelectorAll('.opt').forEach(b=>b.onclick=()=>{ S.pick=+b.dataset.k; S.score=null; renderChat(); });
  const fin=$('#fin'); if(fin) fin.onclick=()=>{ S.log.push({a:t.a}); S.i++; renderChat(); };
  if(S.pick!=null){ const u=t.u[S.pick]; bindPractice($('#prac'),u,L=>{ S.score=L.overall; });
    $('#other').onclick=()=>{ S.pick=null; CUR=null; micUI(false); renderChat(); };
    $('#next').onclick=()=>{ S.log.push({a:t.a,u,s:S.score}); S.i++; S.pick=null; S.played=false; CUR=null; micUI(false); renderChat(); window.scrollTo(0,document.body.scrollHeight); };
    $('#prac').scrollIntoView({block:'nearest'}); }
}
function renderSummary(){
  const S=SUB, sc=S.s, said=S.log.filter(l=>l.u), sco=said.map(l=>l.s).filter(v=>v!=null), avg=sco.length?Math.round(sco.reduce((a,b)=>a+b,0)/sco.length):null;
  micUI(false); CUR=null;
  V.innerHTML=`<h2>Tổng kết: ${esc(sc.title)}</h2>
   <div class="score card" style="margin:10px 0"><div class="ring" style="--v:${avg||0};--c:var(--${avg>=80?'jade':avg>=60?'warn':'bad'})">${avg==null?'—':avg}</div><div><b>${said.length} câu đã nói</b><div class="muted small">${avg==null?'':avg>=85?'Rất tốt — thử phương án "Phong cách của anh" ở lượt sau.':avg>=70?'Khá — luyện lại các câu dưới 70 điểm.':'Cần luyện thêm — dùng tab Luyện từ & câu cho các âm yếu.'}</div></div></div>
   <div class="list">${said.map(l=>`<div class="item"><div><div class="z">${esc(l.u.zh)}</div><div class="p">${esc(l.u.py)}</div></div><span class="sc ${scCls(l.s)}">${l.s==null?'—':l.s}</span></div>`).join('')}</div>
   <div class="acts" style="margin-top:14px"><button class="btn" id="again">Làm lại tình huống</button><button class="btn" id="copy">Chép tóm tắt gửi Claude</button><button class="btn pri" id="home">Tình huống khác</button></div>`;
  $('#again').onclick=()=>go('hoi-thoai',{s:sc,i:0,log:[],pick:null});
  $('#home').onclick=()=>go('hoi-thoai');
  $('#copy').onclick=()=>copyText(`Tôi vừa luyện nói tiếng Trung tình huống "${sc.title}" (HSK ${ST.prof.lv}). Điểm từng câu:\n`+said.map(l=>`- ${l.u.zh} (${l.u.py}): ${l.s??'—'}`).join('\n')+`\nÂm hay sai: ${weakList(6).map(w=>w.key).join(', ')||'chưa đủ dữ liệu'}.\nHãy nhận xét và cho tôi bài luyện tiếp theo.`);
}
/* Luyện từ & câu */
function renderLesson(){
  const les=SUB.lesson, rows=[]; les.items.forEach((it,i)=>{ rows.push({i,kind:'w',zh:it.hz,py:it.py,vi:it.vi,t:it.tw}); if(it.ex) rows.push({i,kind:'e',zh:it.ex,py:it.exp,vi:it.exv,t:it.te}); });
  SUB.rows=rows;
  V.innerHTML=`<div class="row" style="justify-content:space-between"><h2>Bài ${les.k} · ${esc(les.title)}</h2><button class="btn sm" id="back">← Danh sách bài</button></div>
   <div class="acts" style="justify-content:flex-start;margin:8px 0"><button class="btn pri" id="start">Luyện lần lượt từ đầu</button></div>
   <div class="list">${rows.map((r,k)=>{ const s=ST.done[r.zh]; return `<button class="item" data-r="${k}"><div><div class="z">${esc(r.zh)}</div><div class="p">${esc(r.py)}</div><div class="v">${esc(r.vi)}</div></div><span class="sc ${scCls(s)}">${s==null?'':s}</span></button>`; }).join('')}</div>`;
  $('#back').onclick=()=>go('luyen');
  $('#start').onclick=()=>{ SUB.item=0; render(); };
  V.querySelectorAll('[data-r]').forEach(b=>b.onclick=()=>{ SUB.item=+b.dataset.r; render(); });
}
function renderDrill(){
  const r=SUB.rows[SUB.item], n=SUB.rows.length;
  V.innerHTML=`<div class="row" style="justify-content:space-between"><div class="muted small">Bài ${SUB.lesson.k} · ${SUB.item+1}/${n} · ${r.kind==='w'?'Từ':'Câu ví dụ'}</div><button class="btn sm" id="back">← Bài học</button></div>
   <div class="card" id="prac" style="margin-top:8px">${practiceHTML(r)}</div>
   <div class="acts" style="margin-top:10px"><button class="btn" id="prev" ${SUB.item?'':'disabled'}>← Trước</button><button class="btn pri" id="next">${SUB.item<n-1?'Tiếp →':'Xong bài'}</button></div>`;
  $('#back').onclick=()=>{ SUB.item=null; CUR=null; micUI(false); render(); };
  $('#prev').onclick=()=>{ SUB.item--; render(); };
  $('#next').onclick=()=>{ if(SUB.item<n-1){ SUB.item++; render(); } else { SUB.item=null; CUR=null; micUI(false); render(); toast('Đã xong bài!'); } };
  bindPractice($('#prac'),r); playRef(r.zh);
}
/* ---------- Lộ trình HSK theo bài + bài kiểm tra (theo Sổ Từ HSK) ---------- */
const PKEY='luyennoi-path-v1', PASS=.9;
const shuf2=a=>{ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; };
let PT={passed:{}}; try{ PT=Object.assign(PT,JSON.parse(localStorage.getItem(PKEY)||'null')||{}); }catch(e){}
function pSave(){ try{ localStorage.setItem(PKEY,JSON.stringify(PT)); }catch(e){} }
let PATH=[], PREAD={}, WBH=null, NOF={};
function setupPath(j){
  PATH=j.L; PREAD=j.R; const cnt={};
  PATH.forEach(L=>{ cnt[L.lv]=(cnt[L.lv]||0)+1; L.k=cnt[L.lv]; L.w.forEach(h=>NOF[h]=L.n); });
}
function pUnlocked(n){ const L=PATH.find(x=>x.n===n); if(!L) return false; if(L.k===1) return L.lv===1||!!PT.passed['f'+(L.lv-1)]; return !!PT.passed[n-1]; }
function pFinalUnlocked(lv){ return PATH.filter(x=>x.lv===lv).every(x=>PT.passed[x.n]); }
function wordsByHz(){ if(!WBH){ WBH={}; allWords().forEach(w=>{ if(!WBH[w.hz]) WBH[w.hz]=w; }); } return WBH; }
function hskLessonFor(L){ const G=HSK.find(x=>x.lv===L.lv); return G.lessons.find(x=>x.title===L.t)||G.lessons[L.k-1]; }
function rd(x){ // đọc một câu đọc hiểu thành câu hỏi
  const t=x[0];
  if(t==='F'){ const o=x[2].split('/'), ans=o[+x[3]], so=shuf2(o); return {sec:'read',type:'F',title:'Chọn từ điền vào chỗ trống',text:x[1],opts:so.map(v=>({t:v,han:true})),correct:so.indexOf(ans),answerText:ans,explain:x[4]}; }
  if(t==='T'){ return {sec:'read',type:'T',title:'Đọc và phán đoán đúng hay sai',passage:x[1],text:x[2],opts:[{t:'Đúng'},{t:'Sai'}],correct:x[3]==='1'?0:1,answerText:x[3]==='1'?'Đúng':'Sai',explain:x[4]}; }
  const o=x[3].split('/'), ans=o[+x[4]], so=shuf2(o);
  return {sec:'read',type:'R',title:'Đọc hiểu: chọn câu trả lời đúng',passage:x[1],text:x[2],opts:so.map(v=>({t:v,han:/[一-鿿]/.test(v)})),correct:so.indexOf(ans),answerText:ans,explain:x[5]};
}
function vq(w,pool,sec){
  const types=['hz2vi','vi2hz','py2hz']; const type=types[Math.floor(Math.random()*types.length)];
  const dis=[]; for(const x of shuf2(pool.filter(v=>v.hz!==w.hz&&v.vi!==w.vi))){ if(dis.length===3) break; if(!dis.some(y=>y.vi===x.vi||y.hz===x.hz||y.py===x.py)) dis.push(x); }
  const opts=shuf2([w,...dis]), han=type!=='hz2vi';
  const title={hz2vi:'Chữ này nghĩa là gì?',vi2hz:'Chọn chữ Hán đúng',py2hz:'Pinyin này là chữ nào?'}[type];
  return {sec,type,w,title,opts:opts.map(o=>({t:han?o.hz:o.vi,han})),correct:opts.indexOf(w),answerText:han?w.hz:w.vi,explain:`${w.hz} · ${w.py} · ${w.vi}`};
}
function buildTest(id){
  const pool=wordsByHz(); let qs=[], name, key, lv;
  if(String(id)[0]==='f'){
    lv=+String(id).slice(1); key=id; name='Thi thử HSK '+lv;
    const lw=PATH.filter(x=>x.lv===lv).flatMap(x=>x.w).map(h=>pool[h]);
    const all=Object.values(pool).filter(w=>w.lv===lv);
    qs=shuf2(lw).slice(0,40).map(w=>vq(w,all,'vocab'));
    const rs=PATH.filter(x=>x.lv===lv).flatMap(x=>(PREAD[x.n]||[]));
    qs=qs.concat(shuf2(rs).slice(0,10).map(rd));
  } else {
    const n=+id, L=PATH.find(x=>x.n===n); lv=L.lv; key=n; name=`HSK ${L.lv} · Bài ${L.k} · ${L.t}`;
    const cur=L.w.map(h=>pool[h]), prev=PATH.filter(x=>x.n<n).flatMap(x=>x.w).map(h=>pool[h]);
    const all=Object.values(pool).filter(w=>w.lv===lv);
    qs=shuf2(cur).map(w=>vq(w,all,'vocab'));
    const rv=Math.min(prev.length,Math.max(4,Math.ceil(cur.length*.4)));
    const weak=prev.map(w=>({w,s:(SR.c[w.hz]&&SR.c[w.hz].q==='review'?Math.min(5,SR.c[w.hz].iv)/5:0)+Math.random()*.6})).sort((a,b)=>a.s-b.s).slice(0,rv).map(x=>x.w);
    qs=qs.concat(shuf2(weak).map(w=>vq(w,all,'review')));
    qs=qs.concat((PREAD[n]||[]).map(rd));
  }
  return {id,key,name,qs,i:0,ans:[],done:false,pass:false,score:0};
}
function startPathTest(id){ SUB={ptest:buildTest(id)}; render(); window.scrollTo(0,0); }
function speakHz(h){ playRef(h); }
function renderPTest(){
  const T=SUB.ptest, N=T.qs.length;
  if(T.done) return renderPResult();
  const q=T.qs[T.i];
  let prompt='';
  if(q.sec!=='read'){ const w=q.w; prompt = q.type==='hz2vi'?`<div style="font-family:'Noto Serif SC',serif;font-size:4.5rem;line-height:1.1">${esc(w.hz)}</div>`:q.type==='vi2hz'?`<div style="font-size:1.6rem;font-weight:600">${esc(w.vi)}</div>`:`<div style="font-size:2rem;color:var(--jade);font-weight:600">${esc(w.py)}</div>`; }
  else if(q.type==='F') prompt=`<div style="font-family:'Noto Serif SC',serif;font-size:1.3rem;line-height:1.8">${esc(q.text).replace('＿＿','<span style="display:inline-block;min-width:3em;border-bottom:2px solid var(--seal)"></span>')}</div>`;
  else prompt=`<div style="font-family:'Noto Serif SC',serif;font-size:1.1rem;line-height:1.8;background:var(--sunk);border-radius:10px;padding:10px">${esc(q.passage)}</div><div style="font-family:'Noto Serif SC',serif;font-size:1.25rem;margin-top:8px">${q.type==='T'?'★ ':''}${esc(q.text)}</div>`;
  const secName={vocab:'Từ vựng của bài',review:'Ôn từ bài trước',read:'Đọc hiểu'}[q.sec];
  V.innerHTML=`<div class="row" style="justify-content:space-between"><div class="small muted">${esc(T.name)} · ${T.i+1}/${N}</div><button class="btn sm" id="pquit">Thoát</button></div>
   <div style="height:6px;border-radius:99px;background:var(--line);overflow:hidden;margin:8px 0"><i style="display:block;height:100%;width:${T.i/N*100}%;background:var(--jade)"></i></div>
   <div class="card" style="text-align:center;padding:20px 14px"><span class="small muted">${secName}</span><h3 style="margin:6px 0 10px;text-transform:none;letter-spacing:0;color:var(--ink);font-size:1rem">${q.title}</h3>${prompt}
     ${q.type==='py2hz'||q.type==='hz2vi'?'':''}</div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px">${q.opts.map((o,i)=>`<button class="btn" data-i="${i}" style="${o.han?"font-family:'Noto Serif SC',serif;font-size:1.3rem":''}"><small style="opacity:.6;margin-right:6px">${i+1}</small>${esc(o.t)}</button>`).join('')}</div>
   <p class="muted small" style="margin-top:8px">Cần từ 90% để qua bài. Bấm phím <b>1</b>–<b>4</b> để chọn đáp án.</p>`;
  $('#pquit').onclick=()=>{ SUB=null; render(); };
  V.querySelectorAll('[data-i]').forEach(b=>b.onclick=()=>{ T.ans[T.i]=+b.dataset.i; T.i++; if(T.i>=N) finishPTest(); renderPTest(); });
}
function finishPTest(){
  const T=SUB.ptest; T.done=true; let ok=0; const wrong=[];
  T.qs.forEach((q,k)=>{ if(T.ans[k]===q.correct) ok++; else if(q.w) wrong.push(q.w); });
  T.score=ok/T.qs.length; T.pass=T.score>=PASS;
  const now=Date.now();
  wrong.forEach(w=>{ const c=SR.c[w.hz]; if(!c) return; SR.c[w.hz]={...c, q:c.q==='review'?'relearn':c.q, due:now}; });
  if(T.pass){ const p=PT.passed[T.key]; PT.passed[T.key]={best:Math.max(T.score,p?p.best:0),date:Date.now()}; }
  pSave(); srsSave(); T.wrong=wrong.length;
}
function nextTestOf(id){
  if(String(id)[0]==='f'){ const lv=+String(id).slice(1); const nx=PATH.find(x=>x.lv===lv+1&&x.k===1); return nx?{id:nx.n,name:`Bài 1 · ${nx.t} (HSK ${nx.lv})`}:null; }
  const n=+id, L=PATH.find(x=>x.n===n); if(!L) return null;
  const nx=PATH.find(x=>x.n===n+1&&x.lv===L.lv);
  if(nx) return {id:nx.n,name:`Bài ${nx.k} · ${nx.t}`};
  return {id:'f'+L.lv,name:`Thi thử HSK ${L.lv}`};
}
function renderPResult(){
  const T=SUB.ptest, N=T.qs.length, need=Math.ceil(PASS*N), ok=T.qs.filter((q,k)=>T.ans[k]===q.correct).length;
  const nx=T.pass?nextTestOf(T.id):null;
  const grp=(sec,lbl)=>{ const a=T.qs.map((q,k)=>q).filter(q=>q.sec===sec); if(!a.length) return ''; const c=a.filter(q=>T.ans[T.qs.indexOf(q)]===q.correct).length; return `<span>${lbl}: <b>${c}/${a.length}</b></span>`; };
  const wrong=T.qs.map((q,k)=>({q,a:T.ans[k],k})).filter(x=>x.a!==x.q.correct);
  const reason=q=>{
    if(q.sec==='read') return esc(q.explain||'');
    const w=q.w; const ex=w.ex?`<div class="small" style="margin-top:4px">Ví dụ: <span style="font-family:'Noto Serif SC',serif">${esc(w.ex)}</span> <span class="muted">${esc(w.exv||'')}</span></div>`:'';
    return `<div class="small muted">${esc(w.hz)} · ${esc(w.py)} · ${esc(w.vi)}</div>${ex}`;
  };
  V.innerHTML=`<div class="card" style="text-align:center;padding:22px 14px">
    <span class="badge ${T.pass?'b-rev':'b-learn'}">${T.pass?'ĐẠT':'CHƯA ĐẠT'}</span>
    <div style="font-size:2.6rem;font-weight:700;margin:6px 0">${Math.round(T.score*100)}%</div>
    <p class="muted small">Đúng ${ok}/${N} · cần ${need} câu (≥ ${PASS*100}%)</p>
    <div class="row" style="justify-content:center;gap:14px" class="small">${grp('vocab','Từ vựng')} ${grp('review','Ôn từ cũ')} ${grp('read','Đọc hiểu')}</div>
    <p style="max-width:52ch;margin:10px auto">${T.pass?(nx?`Đã mở ${nx.name}.`:'Chúc mừng, bạn đã qua hết lộ trình hiện có.'):'Các từ làm sai đã được đưa lên mục Ôn hôm nay. Ôn lại rồi làm lại bài.'}</p>
    <div class="row" style="justify-content:center;margin-top:10px;gap:8px">
      ${nx?`<button class="btn pri" id="pnext">Bài kiểm tra tiếp theo</button>`:''}
      <button class="btn" id="pretry">Làm lại bài này</button>
      ${T.pass?'':'<button class="btn" id="pstudy">Ôn hôm nay</button>'}
      <button class="btn" id="pback">Về màn hình chính</button></div></div>
   <h3 style="margin:14px 0 6px">Câu làm sai (${wrong.length}/${N})</h3>
   ${wrong.length?`<div class="list">${wrong.map(({q,a})=>`<div class="item" style="flex-direction:column;align-items:flex-start;gap:4px;border-left:4px solid var(--bad)">
      <span class="small"><b>${esc(q.title)}</b> · ${q.sec==='read'?'Đọc hiểu':q.sec==='review'?'Ôn từ cũ':'Từ vựng'}</span>
      ${q.sec==='read'?`<span class="small muted">${esc((q.passage?q.passage+' ':'')+q.text)}</span>`:''}
      <span class="small">Bạn chọn: <b style="color:var(--bad)">${esc(q.opts[a]?q.opts[a].t:'(bỏ trống)')}</b> · Đáp án đúng: <b style="color:var(--jade)">${esc(q.answerText)}</b></span>
      ${reason(q)}</div>`).join('')}</div>`:'<p class="muted small">Không có câu nào làm sai.</p>'}`;
  $('#pretry').onclick=()=>startPathTest(T.id);
  $('#pback').onclick=()=>{ SUB=null; render(); window.scrollTo(0,0); };
  const pn=$('#pnext'); if(pn) pn.onclick=()=>startPathTest(nx.id);
  const ps=$('#pstudy'); if(ps) ps.onclick=()=>go('on-tu');
}
function renderLessons(){
  const lvs=[...new Set(PATH.map(x=>x.lv))], lv=ST.prof.lvView||1, L=PATH.filter(x=>x.lv===lv);
  const fin=PT.passed['f'+lv], fu=pFinalUnlocked(lv);
  V.innerHTML=`<h2>Lộ trình HSK</h2><p class="muted small">Qua bài (≥ 90%) mới mở bài sau. Cuối mỗi cấp có thi thử. Từ của bài mở sẽ vào mục Ôn hôm nay.</p>
   <div class="row" style="margin:10px 0">${lvs.map(x=>`<button class="chip" data-lv="${x}" aria-pressed="${x===lv}">HSK ${x} · ${PATH.filter(y=>y.lv===x&&PT.passed[y.n]).length}/${PATH.filter(y=>y.lv===x).length}</button>`).join('')}</div>
   <div class="list">${L.map(les=>{ const un=pUnlocked(les.n), p=PT.passed[les.n], seen=les.w.filter(h=>SR.c[h]).length;
     return `<div class="card" style="padding:12px;${un?'':'opacity:.6'}"><div class="row" style="justify-content:space-between"><b>${les.k}. ${esc(les.t)}</b><span class="small" style="color:${p?'var(--jade)':'var(--muted)'}">${p?'✓ Đã qua':un?`${seen}/${les.w.length} từ`:'🔒 Khóa'}</span></div>
     ${un?`<div class="row" style="margin-top:8px"><button class="btn sm" data-learn="${les.n}">Học từ</button><button class="btn sm pri" data-test="${les.n}">${p?'Làm lại':'Kiểm tra'}</button></div>`:'<p class="small muted" style="margin:6px 0 0">Qua bài trước để mở</p>'}</div>`; }).join('')}
   <div class="card" style="padding:12px;${fu?'':'opacity:.6'}"><div class="row" style="justify-content:space-between"><b>Thi thử HSK ${lv}</b><span class="small" style="color:${fin?'var(--jade)':'var(--muted)'}">${fin?'✓ Đã qua':fu?'Mở':'🔒 Khóa'}</span></div>
     ${fu?`<div class="row" style="margin-top:8px"><button class="btn sm pri" data-test="f${lv}">${fin?'Thi lại':'Thi thử'}</button></div>`:'<p class="small muted" style="margin:6px 0 0">Qua hết bài của cấp để mở</p>'}</div></div>`;
  V.querySelectorAll('[data-lv]').forEach(b=>b.onclick=()=>{ ST.prof.lvView=+b.dataset.lv; save(); render(); });
  V.querySelectorAll('[data-learn]').forEach(b=>b.onclick=()=>{ const les=PATH.find(x=>x.n===+b.dataset.learn); const H=hskLessonFor(les); go('luyen',{lesson:H}); });
  V.querySelectorAll('[data-test]').forEach(b=>b.onclick=()=>startPathTest(b.dataset.test));
}
function forecastHTML(){
  const t=todayN(), cnt=Array(7).fill(0);
  Object.values(SR.c).forEach(c=>{ if(!c||c.q!=='review') return; const off=Math.max(0,c.dd-t); if(off<7) cnt[off]++; });
  const mx=Math.max(1,...cnt), wd=['CN','T2','T3','T4','T5','T6','T7'];
  return `<div class="card" style="margin-bottom:12px"><span class="small muted">Lịch ôn 7 ngày tới</span><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px;align-items:end;height:90px;margin-top:8px">${cnt.map((n,i)=>{ const d=new Date(); d.setDate(d.getDate()+i); return `<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;font-size:.72rem;color:var(--muted)"><span>${n}</span><i style="display:block;width:100%;max-width:32px;background:${n?'var(--jade)':'var(--line)'};border-radius:4px 4px 0 0;height:${Math.max(2,n/mx*56)}px"></i><span>${i===0?'Nay':wd[d.getDay()]}</span></div>`; }).join('')}</div></div>`;
}

/* Tiến bộ */
function weakList(n){ return Object.entries(ST.weak).filter(([k,w])=>w.n>=2&&w.bad>0).map(([k,w])=>({key:k,rate:w.bad/w.n,...w})).sort((a,b)=>b.rate-a.rate||b.bad-a.bad).slice(0,n); }
function renderProgress(){
  const now=Date.now(), DAY=864e5, days=[...Array(14)].map((_,k)=>{ const d0=new Date(now-(13-k)*DAY); d0.setHours(0,0,0,0); const d1=+d0+DAY; const h=ST.hist.filter(x=>x.t>=+d0&&x.t<d1); return {d:d0,n:h.length,avg:h.length?Math.round(h.reduce((a,b)=>a+b.s,0)/h.length):null}; });
  const mx=Math.max(1,...days.map(d=>d.n)), recent=ST.hist.slice(-50), avg=recent.length?Math.round(recent.reduce((a,b)=>a+b.s,0)/recent.length):null;
  const wk=weakList(12);
  V.innerHTML=`<h2>Tiến bộ</h2>
   <div class="kpi" style="margin:10px 0"><div><b>${ST.hist.length}</b><span>lần nói</span></div><div><b class="${scCls(avg)}">${avg==null?'—':avg}</b><span>điểm TB 50 lần gần nhất</span></div><div><b>${Object.keys(ST.done).length}</b><span>câu/từ đã luyện</span></div></div>
   <h3>14 ngày qua (số lần nói)</h3><div class="card"><div class="days">${days.map(d=>`<div style="height:${d.n/mx*100}%" title="${d.n} lần${d.avg!=null?', TB '+d.avg:''}"><span>${d.d.getDate()}</span></div>`).join('')}</div><div style="height:18px"></div></div>
   <h3>Âm hay sai nhất</h3>${wk.length?`<div class="weak">${wk.map(w=>`<span><b class="han">${esc(w.hz)}</b> ${esc(w.key)} · sai ${w.bad}/${w.n}</span>`).join('')}</div><p class="note">Bấm luyện lại các từ chứa những âm này trong tab Luyện từ &amp; câu.</p>`:'<p class="muted small">Chưa đủ dữ liệu.</p>'}
   <div class="acts" style="justify-content:flex-start;margin-top:14px"><button class="btn" id="copy">Chép tóm tắt gửi Claude</button></div>`;
  $('#copy').onclick=()=>copyText(`Tiến bộ luyện nói tiếng Trung của tôi: ${ST.hist.length} lần nói, điểm trung bình gần đây ${avg??'—'}/100.\nÂm hay sai: ${wk.map(w=>`${w.hz} ${w.key} (sai ${w.bad}/${w.n})`).join(', ')||'chưa có'}.\nHãy giải thích vì sao người Việt hay sai những âm này và cho tôi bài luyện 10 phút.`);
}
function copyText(t){ (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>toast('Đã chép. Mở Claude và dán vào khung chat.'),()=>{ const a=document.createElement('textarea'); a.value=t; document.body.appendChild(a); a.select(); try{ document.execCommand('copy'); toast('Đã chép.'); }catch(e){ toast('Không chép được.'); } a.remove(); }); }
/* Cài đặt */
const REGIONS=['southeastasia','eastasia','japaneast','koreacentral','centralindia','australiaeast','westeurope','northeurope','eastus','eastus2','westus','westus2','centralus'];
function renderSettings(){
  V.innerHTML=`<h2>Cài đặt</h2>
   <h3>Chấm phát âm bằng Azure (miễn phí 5 giờ/tháng)</h3>
   <div class="card list">
    <div class="field">Key (Key 1 của tài nguyên Speech)<input id="k" type="password" autocomplete="off" value="${esc(ST.az.key)}" placeholder="Dán key vào đây"></div>
    <div class="field">Khu vực (Region)<select id="rg">${REGIONS.map(r=>`<option ${r===ST.az.region?'selected':''}>${r}</option>`).join('')}</select></div>
    <div class="row"><button class="btn pri" id="test">Lưu &amp; kiểm tra</button><span id="tr" class="small muted">${ST.az.ok?'✓ Đã kết nối':''}</span></div>
    <p class="note">Key chỉ lưu trên máy này, không gửi đi đâu ngoài máy chủ Azure của Microsoft. Lần kiểm tra dùng một câu giọng mẫu có sẵn, không cần nói.</p>
    <details><summary><b>Cách lấy key miễn phí (5 phút)</b></summary><ol class="steps">
     <li>Vào <b>portal.azure.com</b>, đăng ký tài khoản Microsoft Azure miễn phí (cần thẻ để xác minh; gói Free không trừ tiền).</li>
     <li>Ô tìm kiếm trên cùng → gõ <b>Speech services</b> → <b>Create</b>.</li>
     <li>Resource group: tạo mới (ví dụ <i>luyen-noi</i>). Region: <b>Southeast Asia</b>. Name: tên bất kỳ. <b>Pricing tier: Free F0</b>.</li>
     <li>Create → đợi xong → <b>Go to resource</b> → mục <b>Keys and Endpoint</b> → chép <b>KEY 1</b> và <b>Location/Region</b>.</li>
     <li>Dán key ở trên, chọn đúng Region, bấm <b>Lưu &amp; kiểm tra</b>.</li></ol>
     <p class="note">Gói F0 tự dừng khi hết 5 giờ/tháng (không tính tiền). Mỗi câu khoảng 2–5 giây → vài nghìn lần chấm/tháng.</p></details>
   </div>
   <h3>Hồ sơ</h3>
   <div class="card list">
    <div class="field">Tên tiếng Trung<input id="nm" value="${esc(ST.prof.name)}"></div>
    <div class="field">Tốc độ giọng mẫu<select id="rt">${[[0.8,'Chậm'],[0.9,'Hơi chậm'],[1,'Bình thường']].map(([v,l])=>`<option value="${v}" ${ST.rate==v?'selected':''}>${l}</option>`).join('')}</select></div>
    <div class="row"><button class="btn" id="sv">Lưu</button><button class="btn" id="exp">Xuất tiến độ</button><label class="btn" style="cursor:pointer">Nhập tiến độ<input type="file" id="imp" accept=".json" hidden></label></div>
    <div class="field">Đồng bộ từ Sổ Từ HSK: dán đoạn đã sao chép từ mục “Xuất tiến trình sang ứng dụng Luyện nói”<textarea id="swin" placeholder="Dán đoạn JSON vào đây" style="min-height:90px;font-size:.8rem"></textarea></div>
    <div class="row"><button class="btn" id="swgo">Nhập tiến trình từ Sổ Từ HSK</button></div>
    <p class="note">Tiến độ lưu trong trình duyệt của máy này. Dùng Xuất/Nhập để chuyển sang máy khác. Phiên bản ứng dụng: v14.</p>
   </div>`;
  $('#test').onclick=async()=>{ ST.az.key=$('#k').value.trim(); ST.az.region=$('#rg').value; ST.az.ok=false; save(); const tr=$('#tr');
    if(!ST.az.key){ tr.textContent='Chưa nhập key.'; render(); return; }
    
    tr.innerHTML='<span class="spin"></span> Đang kiểm tra…';
    try{ const T='您好！我叫乔。'; const b=await refBuffer(T); if(!b) throw new Error('chưa tải được giọng mẫu, kiểm tra mạng rồi thử lại'); const x=await to16k(b); const j=await azAssess(x,T); if(j&&j.nomatch) throw new Error('Azure không nhận ra giọng mẫu'); const r=azPerChar(j,T);
      if(!r) throw new Error('Không có kết quả'); ST.az.ok=true; save(); tr.textContent=`✓ Kết nối được. Giọng mẫu “您好！我叫乔。” đạt ${Math.round(r.pron)} điểm.`; $('#azb').textContent='Chấm Azure'; $('#azb').classList.add('on'); }
    catch(e){ tr.textContent='✗ Chưa được: '+(/401|403|Unauthorized|invalid subscription/i.test(e.message)?'key hoặc region chưa đúng.':e.message); } };
  $('#sv').onclick=()=>{ ST.prof.name=$('#nm').value.trim()||'乔'; ST.rate=+$('#rt').value; save(); toast('Đã lưu.'); };
  $('#exp').onclick=()=>{ const d={...ST,az:{region:ST.az.region}}; const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([JSON.stringify(d)],{type:'application/json'})); a.download='luyen-noi-tien-do.json'; a.click(); };
  $('#swgo').onclick=()=>{
    let d; try{ d=JSON.parse($('#swin').value.trim()); }catch(e){ toast('Đoạn dán không phải JSON hợp lệ.'); return; }
    if(!d||d.src!=='so-tu-hsk'||!d.c){ toast('Đoạn này không phải tiến trình của Sổ Từ HSK.'); return; }
    let nc=0, np=0;
    for(const k in d.c){ const hz=k.replace(/^w:/,''); if(!/^[\u3400-\u9fff]+$/.test(hz)) continue; const a=d.c[k], l=SR.c[hz];
      if(!l || (a.r||0)>(l.r||0)){ SR.c[hz]={q:a.q,st:a.st||0,iv:a.iv||0,ef:a.ef||2.5,r:a.r||0,l:a.l||0,due:a.due,dd:a.dd}; nc++; } }
    for(const k in (d.passed||{})){ const a=d.passed[k], l=PT.passed[k]; if(!l||(a.best||0)>(l.best||0)){ PT.passed[k]={best:a.best||0,date:a.date||Date.now()}; np++; } }
    pSave(); srsSave(); $('#swin').value=''; toast(`Đã nhập ${nc} thẻ và ${np} bài đã qua.`); render();
  };
  $('#imp').onchange=async e=>{ const f=e.target.files[0]; if(!f) return; try{ const d=JSON.parse(await f.text()); ST.hist=(d.hist||[]).concat(ST.hist).sort((a,b)=>a.t-b.t); ST.done=Object.assign({},d.done||{},ST.done); ST.weak=Object.assign({},d.weak||{},ST.weak); save(); toast('Đã nhập tiến độ.'); render(); }catch(err){ toast('File không hợp lệ.'); } };
}
window.addEventListener('hashchange',()=>{ const h=location.hash.slice(1); if(h&&h!==view&&['hoi-thoai','luyen','on-tu','tien-bo','cai-dat'].includes(h)) go(h); });
document.addEventListener('keydown',e=>{
  if(e.ctrlKey||e.metaKey||e.altKey) return;
  const tg=e.target; if(tg&&(/^(INPUT|TEXTAREA|SELECT)$/.test(tg.tagName)||tg.isContentEditable)) return;
  if(view==='luyen'&&SUB&&SUB.ptest&&!SUB.ptest.done){
    if(['1','2','3','4'].includes(e.key)){ const b=V.querySelector(`[data-i="${+e.key-1}"]`); if(b){ e.preventDefault(); b.click(); } }
    return;
  }
  if(view!=='on-tu'||SUB) return;
  const t=e.target; if(t&&(/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)||t.isContentEditable)) return;
  if(!SR.cur) return;
  if(!SR.shown){ if(e.key===' '||e.key==='Enter'){ e.preventDefault(); SR.shown=true; renderSRS(); if(SR.cur) playRef(SR.cur.hz); } return; }
  if(['1','2','3','4'].includes(e.key)){ e.preventDefault(); srsGrade(+e.key-1); }
});
document.addEventListener('visibilitychange',()=>{ if(document.hidden&&!REC.on) micClose(); });

/* ---------- Hán Việt, bộ thủ, thứ tự nét ---------- */
function hanInfoHTML(hz){
  const cs=[...new Set([...hz].filter(c=>HZD[c]))];
  if(!cs.length) return '';
  return `<div style="background:var(--sunk);border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;gap:6px">${cs.map(c=>{ const d=HZD[c]; return `<div class="small"><b style="font-family:'Noto Serif SC',serif;font-size:1.2rem;color:var(--ink)">${esc(c)}</b> <span style="color:var(--seal);font-weight:700;letter-spacing:.08em">${esc(d.hv)}</span>${d.comp?` · <span class="muted">${esc(d.comp)}</span>`:''}${d.mn?`<div class="muted" style="margin-top:2px">${esc(d.mn)}</div>`:''}</div>`; }).join('')}</div>`;
}
/* ---------- Thứ tự nét: dùng HanziWriter như artifact Sổ Từ HSK ---------- */
let HWP=null;
function loadHW(){ if(window.HanziWriter) return Promise.resolve(); if(!HWP) HWP=new Promise((res,rej)=>{ const s=document.createElement('script'); s.src='https://cdn.jsdelivr.net/npm/hanzi-writer@3.7.2/dist/hanzi-writer.min.js'; s.onload=()=>res(); s.onerror=()=>{ HWP=null; rej(new Error('hw')); }; document.head.appendChild(s); }); return HWP; }
async function showStrokes(hz){
  const box=$('#srs-strokes'); if(!box) return;
  if(box.dataset.open===hz){ box.innerHTML=''; box.dataset.open=''; return; }
  box.dataset.open=hz; box.innerHTML='<p class="muted small"><span class="spin"></span> Đang tải thứ tự nét…</p>';
  let D, ok=true; try{ [D]=await Promise.all([loadStrokes(),loadHW()]); }catch(e){ box.innerHTML='<p class="small muted">Không tải được dữ liệu nét (cần mạng). Thử lại sau.</p>'; return; }
  if(box.dataset.open!==hz) return;
  const cs=[...new Set([...hz].filter(c=>HANRE.test(c)))].filter(c=>D[c]);
  if(!cs.length){ box.innerHTML='<p class="small muted">Chưa có dữ liệu nét cho các chữ này.</p>'; return; }
  box.innerHTML=`<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:8px">${cs.map((c,k)=>`<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><div data-ch="${esc(c)}" style="width:150px;height:150px;border:1px solid var(--line);border-radius:10px;background:var(--surface)"></div><span class="small muted">${esc(c)} · ${D[c].strokes.length} nét</span></div>`).join('')}</div>
    <div class="row" style="justify-content:center;margin-top:8px"><button class="btn sm" id="sw-play">▶ Xem lại nét</button><button class="btn sm" id="sw-quiz" aria-pressed="false">✍ Tập viết</button></div>`;
  const tok=n=>getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const opts={width:150,height:150,padding:8,showCharacter:false,showOutline:true,strokeAnimationSpeed:1.1,delayBetweenStrokes:180,
    strokeColor:tok('--ink'),radicalColor:tok('--seal'),outlineColor:tok('--line'),highlightColor:tok('--jade'),drawingColor:tok('--jade'),drawingWidth:5,showHintAfterMisses:2,
    charDataLoader:(c,onLoad,onErr)=>D[c]?onLoad(D[c]):onErr()};
  let ws=[];
  try{ ws=[...box.querySelectorAll('[data-ch]')].map(el=>HanziWriter.create(el, el.dataset.ch, opts)); }catch(e){ box.innerHTML='<p class="small muted">Không khởi tạo được bộ vẽ nét.</p>'; return; }
  let run=0;
  const play=()=>{ const id=++run; let i=0; ws.forEach(x=>x.hideCharacter());
    const next=()=>{ if(id!==run||i>=ws.length) return; ws[i++].animateCharacter({onComplete:()=>setTimeout(next,250)}); }; next(); };
  $('#sw-play').onclick=play;
  const qb=$('#sw-quiz'); let quizzing=false, left=0, miss=0;
  const stopQuiz=()=>{ quizzing=false; qb.setAttribute('aria-pressed','false'); ws.forEach(x=>{ try{ x.cancelQuiz(); }catch(e){} }); };
  qb.onclick=()=>{ if(quizzing){ stopQuiz(); return; } quizzing=true; qb.setAttribute('aria-pressed','true'); left=ws.length; miss=0; run++;
    ws.forEach(x=>{ x.hideCharacter(); x.quiz({onMistake:()=>miss++, onComplete:()=>{ if(--left===0){ quizzing=false; qb.setAttribute('aria-pressed','false'); toast(miss?`Viết xong, sai ${miss} nét. Bấm Tập viết để thử lại.`:'Viết đúng toàn bộ nét!'); } }}); });
    toast('Vẽ từng nét theo đúng thứ tự lên ô chữ. Sai 2 lần sẽ có gợi ý.'); };
  setTimeout(play,300);
}


/* ---------- Tra từ trong câu mẫu: chạm vào từ để xem pinyin, Hán Việt, nghĩa ---------- */
let WDICT=null;
function wdict(){ if(!WDICT){ WDICT={}; allWords().forEach(w=>{ if(!WDICT[w.hz]) WDICT[w.hz]=w; }); } return WDICT; }
const HANRE=/[㐀-鿿]/;
function segSentence(s){
  const D=wdict(), arr=[...(s||'')], out=[]; let i=0;
  while(i<arr.length){
    let hit=null;
    for(let L=Math.min(4,arr.length-i); L>=2; L--){ const t=arr.slice(i,i+L).join(''); if(D[t]){ hit=L; break; } }
    if(hit){ out.push(arr.slice(i,i+hit).join('')); i+=hit; }
    else { out.push(arr[i]); i++; }
  }
  return out;
}
function segHTML(s){
  return segSentence(s).map(t=>HANRE.test(t)?`<span class="tk" data-t="${esc(t)}" style="cursor:pointer;border-bottom:1px dotted var(--muted);border-radius:3px;padding:0 1px">${esc(t)}</span>`:esc(t)).join('');
}
function tokInfoHTML(t){
  const D=wdict(), chars=[...t].filter(c=>HANRE.test(c)), d=D[t];
  const hv=chars.map(c=>HZD[c]?HZD[c].hv:'').filter(Boolean).join(' ');
  const per=chars.length>1?`<div class="small muted" style="margin-top:6px">${chars.map(c=>{ const dc=D[c]; const hc=HZD[c]; return `<span style="margin-right:12px"><b style="font-family:'Noto Serif SC',serif;color:var(--ink)">${esc(c)}</b> ${dc?`<span style="color:var(--jade)">${esc(dc.py)}</span> `:''}${hc?`<span style="color:var(--seal);font-weight:700">${esc(hc.hv)}</span>`:''}</span>`; }).join('')}</div>`:'';
  return `<div style="margin-top:10px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 12px">
    <div class="row" style="gap:10px"><b style="font-family:'Noto Serif SC',serif;font-size:1.5rem">${esc(t)}</b>${d?`<span style="color:var(--jade);font-weight:600;font-size:1.1rem">${esc(d.py)}</span>`:'<span class="muted small">chưa có pinyin trong bộ từ</span>'}</div>
    <div class="small" style="margin-top:4px">Hán Việt: <b style="color:var(--seal);letter-spacing:.06em">${esc(hv||'—')}</b></div>
    <div style="margin-top:4px">Nghĩa: ${d?`<b>${esc(d.vi)}</b>`:'<span class="muted small">chưa có nghĩa trong bộ từ, xem từng chữ bên dưới</span>'}</div>${per}</div>`;
}
function bindTokens(){
  V.querySelectorAll('.tk').forEach(el=>el.onclick=()=>{
    const box=$('#tok-info'); if(!box) return;
    const same=box.dataset.t===el.dataset.t;
    V.querySelectorAll('.tk').forEach(x=>x.style.background='');
    if(same){ box.innerHTML=''; box.dataset.t=''; return; }
    el.style.background='var(--jade-soft)'; box.dataset.t=el.dataset.t; box.innerHTML=tokInfoHTML(el.dataset.t);
  });
}

/* ---------- Ôn từ: thẻ lặp lại ngắt quãng (SM-2 rút gọn, theo Sổ Từ HSK) ---------- */
const SRSKEY='luyennoi-srs-v1';
let SR={c:{}, day:null, newPerDay:20, cur:null, shown:false};
try{ const s=JSON.parse(localStorage.getItem(SRSKEY)||'null'); if(s) SR=Object.assign(SR,s); }catch(e){}
function srsSave(){ try{ localStorage.setItem(SRSKEY,JSON.stringify({c:SR.c,day:SR.day,newPerDay:SR.newPerDay})); }catch(e){} }
const MINS=6e4, DAYS=864e5, STEPS=[1,10], RELEARN=10, GRAD=1, EASY_GRAD=4, START_EF=2.5, MIN_EF=1.3, MATURE=21;
const todayN=()=>Math.floor((Date.now()-new Date().getTimezoneOffset()*MINS)/DAYS);
function dayS(){ const t=todayN(); if(!SR.day||SR.day.d!==t) SR.day={d:t,n:0,r:0}; return SR.day; }
function allWords(){ const out=[]; if(!HSK) return out; for(const L of HSK) for(const les of L.lessons) for(const it of les.items){ out.push({id:it.hz,hz:it.hz,py:it.py,vi:it.vi,em:it.em,ex:it.ex,exp:it.exp,exv:it.exv,lv:L.lv,lesson:les.k,title:les.title}); } return out; }
function srsSchedule(c0,g,now){
  const t=todayN(); const c=c0?{...c0}:{q:'new',st:0,iv:0,ef:START_EF,r:0,l:0};
  if(c.q==='new'||c.q==='learn'){
    if(g===0){ c.q='learn'; c.st=0; c.due=now+STEPS[0]*MINS; }
    else if(g===1){ c.q='learn'; c.due=now+(c.st===0?Math.round((STEPS[0]+STEPS[1])/2):STEPS[c.st])*MINS; }
    else if(g===2){ if(c.st+1<STEPS.length){ c.q='learn'; c.st++; c.due=now+STEPS[c.st]*MINS; } else { c.q='review'; c.iv=GRAD; c.dd=t+c.iv; } }
    else { c.q='review'; c.iv=EASY_GRAD; c.dd=t+c.iv; }
  } else if(c.q==='relearn'){
    if(g<=1){ c.due=now+RELEARN*MINS; } else { c.q='review'; if(g===3) c.iv+=1; c.dd=t+c.iv; }
  } else {
    if(g===0){ c.l++; c.ef=Math.max(MIN_EF,c.ef-.2); c.iv=1; c.q='relearn'; c.due=now+RELEARN*MINS; }
    else if(g===1){ c.ef=Math.max(MIN_EF,c.ef-.15); c.iv=Math.max(c.iv+1,Math.round(c.iv*1.2)); c.dd=t+c.iv; }
    else if(g===2){ c.iv=Math.max(c.iv+1,Math.round(c.iv*c.ef)); c.dd=t+c.iv; }
    else { c.ef+=.15; c.iv=Math.max(c.iv+2,Math.round(c.iv*c.ef*1.3)); c.dd=t+c.iv; }
  }
  c.r++; return c;
}
function fmtDaysN(d){ return d<30?d+' ngày':d<365?(d/30).toFixed(1).replace('.',',')+' tháng':(d/365).toFixed(1).replace('.',',')+' năm'; }
function srsNext(c,g,now){ const n=srsSchedule(c,g,now); if(n.q==='learn'||n.q==='relearn'){ const m=Math.round((n.due-now)/MINS); return m<1?'< 1 phút':m<60?m+' phút':Math.round(m/60)+' giờ'; } return fmtDaysN(n.iv); }
function srsBuckets(){
  const now=Date.now(), t=todayN(), learn=[], rev=[], fresh=[], W=allWords();
  for(const w of W){ const c=SR.c[w.id];
    if(!c){ if(pUnlocked(NOF[w.id])) fresh.push(w); continue; }
    if(c.q==='review'){ if(c.dd<=t) rev.push(w); } else if(c.due<=now) learn.push(w);
  }
  return {learn,rev,fresh,total:W.length};
}
function srsPick(){
  const b=srsBuckets(), now=Date.now();
  const due=[...b.learn.sort((x,y)=>SR.c[x.id].due-SR.c[y.id].due), ...b.rev];
  if(due.length) return due[0];
  if(dayS().n<SR.newPerDay && b.fresh.length) return b.fresh[Math.floor(Math.random()*Math.min(b.fresh.length,50))];
  return null;
}
function srsGrade(g){
  const w=SR.cur; if(!w||!SR.shown) return;
  const d=dayS(); if(!SR.c[w.id]) d.n++; d.r++;
  SR.c[w.id]=srsSchedule(SR.c[w.id],g,Date.now()); srsSave();
  SR.shown=false; SR.cur=srsPick(); renderSRS();
}
function srsDeckCard(){
  if(!HSK) return '<p class="muted"><span class="spin"></span> Đang tải dữ liệu…</p>';
  const b=srsBuckets(), d=dayS(), mature=Object.values(SR.c).filter(c=>c.q==='review'&&c.iv>=MATURE).length;
  const pct=b.total?Math.round(mature/b.total*100):0;
  const left=Math.max(0,SR.newPerDay-d.n);
  if(!SR.cur) SR.cur=srsPick();
  const w=SR.cur;
  let card;
  if(!w){
    card=`<div class="card" style="text-align:center;padding:28px 16px"><h2>Xong lượt hôm nay</h2><p class="muted small" style="margin:8px 0 0">Đã ôn ${d.r} lần. Hẹn lại vào ngày mai, hoặc tăng số từ mới mỗi ngày trong Cài đặt.</p></div>`;
  } else {
    const c=SR.c[w.id], stage=!c?'Từ mới':c.q==='review'?(c.iv>=MATURE?'Đã thuộc':'Đang nhớ'):'Đang học';
    const now=Date.now();
    const grades=[[0,'Lại','Lại'],[1,'Khó','Khó'],[2,'Được','Được'],[3,'Dễ','Dễ']].map(([g,label])=>`<button class="btn ${g===2?'pri':''}" data-g="${g}" style="flex-direction:column;gap:2px;padding:8px 4px"><small style="opacity:.7">${g+1}</small><b>${label}</b><span class="small" style="font-weight:400;opacity:.85">${srsNext(c,g,now)}</span></button>`).join('');
    card=`<div class="card" style="padding:0;overflow:hidden">
      <div style="display:flex;justify-content:space-between;padding:10px 14px" class="small muted"><span>${esc(w.title)} · Bài ${w.lesson} · HSK ${w.lv}</span><span>${stage}</span></div>
      <div style="text-align:center;padding:18px 14px 12px"><div style="font-size:4.2rem;line-height:1.1;font-family:'Noto Serif SC',serif">${esc(w.hz)}</div>${SR.shown?'':'<p class="muted small" style="margin:6px 0 0">Tự nhớ nghĩa rồi bấm hiện đáp án</p>'}</div>
      ${SR.shown?`<div style="border-top:1px dashed var(--line);padding:14px;display:flex;flex-direction:column;gap:10px">
        <div class="row" style="justify-content:space-between"><div><div style="font-size:1.25rem;color:var(--jade);font-weight:600">${esc(w.py)}</div><div style="font-size:1.1rem;font-weight:600">${esc(w.vi)}</div></div><span style="font-size:2rem">${esc(w.em||'')}</span></div>
        ${w.ex?`<div style="background:var(--sunk);border-radius:10px;padding:10px 12px"><div style="font-family:'Noto Serif SC',serif;font-size:1.15rem;line-height:1.9">${segHTML(w.ex)}</div><div id="tok-info"></div><div class="small" style="color:var(--jade)">${esc(w.exp||'')}</div><div class="small muted">${esc(w.exv||'')}</div></div>`:''}
        ${hanInfoHTML(w.hz)}
        <div class="row" style="justify-content:center"><button class="btn sm" id="srs-play">🔊 Nghe giọng mẫu</button><button class="btn sm" id="srs-strk">✍ Thứ tự nét</button></div>
        <div id="srs-strokes"></div>
        <div class="grades" style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">${grades}</div></div>`
      :`<div style="padding:0 14px 14px"><button class="btn pri" id="srs-show" style="width:100%">Hiện đáp án <small style="opacity:.7">(Space / Enter)</small></button></div>`}
    </div>`;
  }
  return `<div class="row" style="justify-content:space-between;margin-bottom:8px"><h2>Ôn hôm nay</h2><span class="small muted">Còn ${left} từ mới hôm nay</span></div>
   <div class="card" style="margin-bottom:12px"><div class="row" style="justify-content:space-between" class="small">
     <span class="small">Cần ôn: <b>${b.learn.length+b.rev.length}</b></span><span class="small">Từ mới: <b>${b.fresh.length}</b></span><span class="small">Đã thuộc: <b>${mature}</b> (${pct}%)</span></div>
     <div style="height:6px;border-radius:99px;background:var(--line);overflow:hidden;margin-top:8px"><i style="display:block;height:100%;width:${pct}%;background:var(--jade)"></i></div></div>
   ${forecastHTML()}
   ${card}
   <p class="muted small" style="margin-top:10px">Phím tắt: <b>Space</b> hoặc <b>Enter</b> để hiện đáp án, rồi <b>1</b> Lại · <b>2</b> Khó · <b>3</b> Được · <b>4</b> Dễ. Nghĩ trước khi xem đáp án, rồi chấm trung thực.</p>`;
}
function renderSRS(){
  V.innerHTML=srsDeckCard();
  bindTokens();
  const sh=$('#srs-show'); if(sh) sh.onclick=()=>{ SR.shown=true; renderSRS(); if(SR.cur) playRef(SR.cur.hz); };
  const sk=$('#srs-strk'); if(sk) sk.onclick=()=>showStrokes(SR.cur.hz);
  const pl=$('#srs-play'); if(pl) pl.onclick=()=>{ if(SR.cur) playRef(SR.cur.hz); };
  V.querySelectorAll('[data-g]').forEach(b=>b.onclick=()=>srsGrade(+b.dataset.g));
}

render(); loadData().then(render).catch(e=>{ console.error('LN',e&&e.stack); V.innerHTML='<p>Không tải được dữ liệu. Kiểm tra mạng rồi tải lại trang.</p>'; });
if('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(()=>{});
window.__LN={ST,azPerChar,toneCompare,assess:x=>assess(x),get CUR(){return CUR;}};
}
