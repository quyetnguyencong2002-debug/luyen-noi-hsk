// Đo cao độ (YIN) + cắt âm tiết + phân loại thanh điệu tiếng Phổ thông theo khuôn Chao (55, 35, 214/21, 51)
(function(root){
const SR=16000, HOP=160, WIN=640;
function yin(x){ // trả về [{t (giây), f (Hz hoặc 0), e (năng lượng dB)}]
  const out=[], W=WIN, tauMin=Math.floor(SR/420), tauMax=Math.floor(SR/65), d=new Float32Array(tauMax+1);
  for(let st=0; st+W+tauMax<x.length; st+=HOP){
    let en=0; for(let i=0;i<W;i++) en+=x[st+i]*x[st+i]; const db=10*Math.log10(en/W+1e-10);
    d.fill(0);
    for(let tau=1;tau<=tauMax;tau++){ let s=0; for(let i=0;i<W;i++){ const v=x[st+i]-x[st+i+tau]; s+=v*v; } d[tau]=s; }
    let run=0, best=-1; const cm=new Float32Array(tauMax+1); cm[0]=1;
    for(let tau=1;tau<=tauMax;tau++){ run+=d[tau]; cm[tau]=d[tau]*tau/(run||1); }
    for(let tau=tauMin;tau<tauMax;tau++){ if(cm[tau]<0.15){ while(tau+1<tauMax&&cm[tau+1]<cm[tau]) tau++; best=tau; break; } }
    if(best<0){ let m=1e9; for(let tau=tauMin;tau<tauMax;tau++) if(cm[tau]<m){ m=cm[tau]; best=tau; } if(m>0.3) best=-1; }
    let f=0; if(best>0&&db>-50){ const a=cm[best-1],b=cm[best],c=cm[best+1]||b; const den=a-2*b+c; const sh=den?0.5*(a-c)/den:0; f=SR/(best+sh); }
    out.push({t:(st+W/2)/SR,f,e:db});
  }
  // làm mượt + bỏ nhảy quãng tám
  const v=out.map(o=>o.f);
  for(let i=1;i<v.length-1;i++){ if(v[i]&&v[i-1]&&v[i+1]){ const m=[v[i-1],v[i],v[i+1]].sort((a,b)=>a-b)[1]; if(Math.abs(Math.log2(v[i]/m))>0.5) out[i].f=m; } }
  for(let i=1;i<out.length-1;i++) if(out[i].f&&!out[i-1].f&&!out[i+1].f) out[i].f=0;
  return out;
}
const st=(f,b)=>12*Math.log2(f/b);
function median(a){ const s=a.slice().sort((x,y)=>x-y); return s.length?s[Math.floor(s.length/2)]:0; }
// Cắt N âm tiết khi không có mốc thời gian: theo khoảng lặng/vô thanh và các hõm năng lượng
function segment(fr,n){
  const vi=fr.map((o,i)=>o.f?i:-1).filter(i=>i>=0); if(!vi.length||n<1) return [];
  const a=vi[0], b=vi[vi.length-1]; if(n===1) return [[a,b]];
  const sm=fr.map((o,i)=>{ let s=0,c=0; for(let k=i-2;k<=i+2;k++) if(fr[k]){ s+=fr[k].e; c++; } return s/c; });
  const cand=[];
  for(let i=a+3;i<b-3;i++){
    const unv=!fr[i].f; const loc=sm[i]<=sm[i-1]&&sm[i]<=sm[i+1];
    if(unv||loc){ let l=-1e9,r=-1e9; for(let k=Math.max(a,i-12);k<i;k++) l=Math.max(l,sm[k]); for(let k=i+1;k<=Math.min(b,i+12);k++) r=Math.max(r,sm[k]);
      cand.push({i,depth:Math.min(l,r)-sm[i]+(unv?6:0)}); } }
  cand.sort((x,y)=>y.depth-x.depth);
  const cuts=[], minGap=Math.max(5,Math.floor((b-a)/n*0.45));
  for(const c of cand){ if(cuts.length>=n-1) break; if(cuts.every(k=>Math.abs(k-c.i)>=minGap)) cuts.push(c.i); }
  while(cuts.length<n-1){ // chia đều phần còn thiếu
    const pts=[a,...cuts.sort((x,y)=>x-y),b]; let gi=0,gl=0; for(let k=0;k<pts.length-1;k++) if(pts[k+1]-pts[k]>gl){ gl=pts[k+1]-pts[k]; gi=k; } cuts.push(Math.round((pts[gi]+pts[gi+1])/2)); }
  const pts=[a,...cuts.sort((x,y)=>x-y),b]; const segs=[]; for(let k=0;k<n;k++) segs.push([pts[k],pts[k+1]]); return segs;
}
// Khuôn thanh theo mức Chao 1–5 (5 điểm)
const TPL={1:[[5,5,5,5,5]],2:[[3,3.3,3.8,4.4,5]],3:[[2.2,1.6,1.1,1,1],[2,1.2,1,2,3.6]],4:[[5,4.3,3.3,2.2,1]]};
function contour(fr,seg,b){
  const [s,e]=seg, idx=[]; for(let i=s;i<=e;i++) if(fr[i]&&fr[i].f) idx.push(i);
  if(idx.length<4) return null; const cut=Math.floor(idx.length*0.12), use=idx.slice(cut,idx.length-cut||undefined);
  const sem=use.map(i=>st(fr[i].f,b)), pts=[];
  for(let k=0;k<5;k++){ const lo=Math.floor(k*sem.length/5), hi=Math.max(lo+1,Math.floor((k+1)*sem.length/5)); let sum=0; for(let j=lo;j<hi;j++) sum+=sem[j]; pts.push(sum/(hi-lo)); }
  return pts; // nửa cung so với giọng nền
}
function toChao(pts,span){ return pts.map(v=>Math.max(0.5,Math.min(5.5,3+v*2/(span/2)))); }
function classify(pts,span,final){
  const c=toChao(pts,span), res={};
  for(const t in TPL){ let best=1e9; for(const tp of TPL[t]){ if(t==='3'&&tp[4]>3&&!final) continue; let s=0; for(let k=0;k<5;k++) s+=(c[k]-tp[k])**2; best=Math.min(best,Math.sqrt(s/5)); } res[t]=best; }
  const order=Object.keys(res).sort((x,y)=>res[x]-res[y]);
  return {tone:+order[0],dist:res,chao:c,margin:res[order[1]]-res[order[0]]};
}
// Phân tích cả câu: expected = mảng thanh mong đợi (đã biến điệu), 5 = nhẹ. segs tùy chọn [[t0,t1]] theo giây (từ Azure)
function analyze(x,expected,opt={}){
  const fr=yin(x), voiced=fr.filter(o=>o.f).map(o=>o.f);
  if(voiced.length<8) return {ok:false,reason:'quiet',frames:fr};
  const b=opt.base||median(voiced), span=opt.span||(median(voiced)<170?9:10);
  let segs;
  if(opt.times&&opt.times.length===expected.length) segs=opt.times.map(([t0,t1])=>[Math.max(0,Math.round((t0*SR-WIN/2)/HOP)),Math.min(fr.length-1,Math.round((t1*SR-WIN/2)/HOP))]);
  else segs=segment(fr,expected.length);
  const syl=expected.map((exp,k)=>{ const sg=segs[k]; if(!sg) return {exp,tone:0,st:'unsure'};
    const pts=contour(fr,sg,b); if(!pts) return {exp,tone:0,st:'unsure',seg:sg};
    const cl=classify(pts,span,k===expected.length-1);
    let stt; if(exp===5) stt='skip'; else if(cl.tone===exp) stt='ok'; else if(cl.dist[exp]-cl.dist[cl.tone]<0.45) stt='near'; else stt='wrong';
    return {exp,tone:cl.tone,st:stt,chao:cl.chao,dist:cl.dist,seg:sg}; });
  const scored=syl.filter(s=>s.st!=='skip'&&s.st!=='unsure');
  const score=scored.length?Math.round(100*scored.reduce((a,s)=>a+(s.st==='ok'?1:s.st==='near'?0.6:0),0)/scored.length):null;
  return {ok:true,base:b,frames:fr,syl,score,segs};
}
root.HZPitch={yin,analyze,segment,classify,median};
})(typeof window!=='undefined'?window:globalThis);
