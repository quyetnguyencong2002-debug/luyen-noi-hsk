/* ---------- Luyện viết câu ---------- */
// 3 chế độ: Chép (có nét mờ) → Nghe viết (pinyin + âm thanh) → Dịch viết (chỉ nghĩa tiếng Việt)
const SMODES={copy:{n:'Chép câu',d:'Nhìn câu chữ Hán, viết theo nét mờ.'},dict:{n:'Nghe viết',d:'Nghe và nhìn pinyin, tự viết chữ Hán.'},tran:{n:'Dịch viết',d:'Chỉ xem nghĩa tiếng Việt, tự viết cả câu.'}};
let SENTS=null;
function sentAll(){
  if(SENTS) return SENTS; const seen=new Set(), out=[];
  const add=(zh,py,vi,lv,src,ord)=>{ if(!zh||seen.has(zh)) return; const cs=[...zh].filter(c=>HANRE.test(c)); if(cs.length<2||cs.length>16) return; seen.add(zh); out.push({zh,py:py||'',vi:vi||'',lv,src,ord,cs}); };
  HSK.forEach(G=>G.lessons.forEach((L,li)=>L.items.forEach(it=>add(it.ex,it.exp,it.exv,G.lv,`HSK ${G.lv} · ${L.title}`,G.lv*1000+li))));
  PATH.forEach(L=>{ const g=GRAM[L.n]; if(g) g.p.forEach(p=>p.ex.forEach(x=>add(x[0],x[1],x[2],L.lv,`Ngữ pháp · ${L.t}`,L.lv*1000+500+L.k))); });
  return (SENTS=out.sort((a,b)=>a.ord-b.ord));
}
function sentLearnedRatio(s){ const k=s.cs.filter(c=>WR.writing[c]&&WR.writing[c].card).length; return k/s.cs.length; }
function sentPick(n){
  const lv=WR.set.lv, S=WR.sent||{}, pool=sentAll().filter(s=>s.lv<=lv);
  const fresh=pool.filter(s=>!S[s.zh]).sort((a,b)=>sentLearnedRatio(b)-sentLearnedRatio(a)||a.ord-b.ord);
  const weak=pool.filter(s=>S[s.zh]&&S[s.zh].best<.8).sort((a,b)=>S[a.zh].last-S[b.zh].last);
  return weak.slice(0,Math.ceil(n/3)).concat(fresh).slice(0,n);
}
function wOpenSent(zh){ loadWD().then(()=>{ const s=sentAll().find(x=>x.zh===zh)||(()=>{ const D=wdict(); return {zh,py:'',vi:'',lv:0,src:'',cs:[...zh].filter(c=>HANRE.test(c))}; })(); go('viet',{sent:{q:[s],i:0,mode:WR.set.smode||'copy'}}); }).catch(()=>toast('Không tải được dữ liệu viết (cần mạng lần đầu).')); }
function sentStart(list){ if(!list.length){ toast('Không còn câu phù hợp trong phạm vi này.'); return; } go('viet',{sent:{q:list,i:0,mode:WR.set.smode||'copy'}}); }
function renderSentHome(){
  const S=WR.sent||{}, lv=WR.set.lv, pool=sentAll().filter(s=>s.lv<=lv), done=pool.filter(s=>S[s.zh]), mode=WR.set.smode||'copy';
  const avg=done.length?Math.round(done.reduce((a,s)=>a+S[s.zh].best,0)/done.length*100):null;
  const groups={}; pool.forEach(s=>{ (groups[s.src]=groups[s.src]||[]).push(s); });
  const keys=Object.keys(groups); const cur=WR.set.sgroup&&groups[WR.set.sgroup]?WR.set.sgroup:keys[0];
  return `<div class="kpi" style="margin:10px 0"><div><b>${done.length}</b><span>câu đã viết</span></div><div><b>${avg==null?'—':avg+'%'}</b><span>độ chính xác TB</span></div><div><b>${pool.length}</b><span>câu trong phạm vi</span></div></div>
   <h3>Chế độ</h3><div class="row" style="gap:6px">${Object.entries(SMODES).map(([k,m])=>`<button class="chip" data-smode="${k}" aria-pressed="${k===mode}" style="min-height:44px">${m.n}</button>`).join('')}</div>
   <p class="small muted" style="margin:6px 0 10px">${SMODES[mode].d} Nên đi theo thứ tự: chép → nghe viết → dịch viết.</p>
   <button class="btn pri" id="sgo" style="width:100%">Viết 5 câu (ưu tiên câu có chữ đã học viết)</button>
   <h3 style="margin-top:16px">Chọn câu theo bài</h3>
   <select id="sgrp" style="width:100%;min-height:44px">${keys.map(k=>`<option ${k===cur?'selected':''}>${esc(k)}</option>`).join('')}</select>
   <div class="list" style="margin-top:8px">${(groups[cur]||[]).map(s=>{ const r=S[s.zh]; const col=!r?'':r.best>=.9?'var(--jade)':r.best>=.6?'var(--warn)':'var(--bad)';
     return `<button class="item" data-sz="${esc(s.zh)}" style="min-height:48px"><div><div style="font-family:'Noto Serif SC',serif;font-size:1.1rem">${esc(s.zh)}</div><div class="small muted">${esc(s.vi)}</div></div><span class="small" style="color:${col};font-weight:700">${r?Math.round(r.best*100)+'%':''}</span></button>`; }).join('')}</div>`;
}
function bindSentHome(){
  V.querySelectorAll('[data-smode]').forEach(b=>b.onclick=()=>{ WR.set.smode=b.dataset.smode; wSave(); render(); });
  $('#sgo').onclick=()=>sentStart(sentPick(5));
  $('#sgrp').onchange=e=>{ WR.set.sgroup=e.target.value; wSave(); render(); };
  V.querySelectorAll('[data-sz]').forEach(b=>b.onclick=()=>{ const s=sentAll().find(x=>x.zh===b.dataset.sz); sentStart([s]); });
}
function sentRecord(T){
  const s=T.s, res=T.res, ok=res.filter(r=>r.m<=2&&!r.skip).length, sc=ok/res.length;
  WR.sent=WR.sent||{}; const p=WR.sent[s.zh]; WR.sent[s.zh]={best:Math.max(sc,p?p.best:0),n:(p?p.n:0)+1,last:Date.now(),mode:T.mode};
  WR.shist=WR.shist||[]; WR.shist.push({t:Date.now(),s:s.zh,sc:Math.round(sc*100),mode:T.mode}); if(WR.shist.length>1000) WR.shist=WR.shist.slice(-1000);
  // chữ đã học viết và đang đến hạn: tính luôn là một lượt ôn viết (chỉ khi viết không có nét mờ)
  if(T.mode!=='copy'){ const now=Date.now(), t=todayN(); res.forEach(r=>{ if(r.dup) return; if(WR.writing[r.c]&&WR.writing[r.c].card&&wIsDue(r.c,now,t)) wRecord(r.c,wGrade(r.m,0,r.skip),r.m,false); }); }
  wSave(); return sc;
}
function renderSent(){
  const Q=SUB.sent; if(Q.i>=Q.q.length) return renderSentDone();
  const s=Q.q[Q.i];
  if(!Q.cur||Q.cur.s!==s||Q.cur.mode!==Q.mode){ const seen=new Set(); Q.cur={s,mode:Q.mode,k:0,res:[],peek:false,done:false,units:[...s.zh].map(ch=>({ch,han:HANRE.test(ch)}))}; Q.cur.units.forEach(u=>{ if(u.han){ u.dup=seen.has(u.ch); seen.add(u.ch); } }); }
  const T=Q.cur, hz=T.units.filter(u=>u.han), N=hz.length, cur=hz[T.k], mode=T.mode;
  const head=`<div class="row" style="justify-content:space-between"><div class="small muted">Viết câu · ${SMODES[mode].n} · ${Q.i+1}/${Q.q.length}</div><button class="btn sm" id="sback">← Danh sách câu</button></div>`;
  let hz_i=-1;
  const strip=`<div style="display:flex;flex-wrap:wrap;gap:4px;justify-content:center;margin:10px 0">${T.units.map(u=>{ if(!u.han) return `<span style="font-family:'Noto Serif SC',serif;font-size:1.4rem;align-self:flex-end">${esc(u.ch)}</span>`;
     hz_i++; const r=T.res[hz_i], isCur=hz_i===T.k&&!T.done, show=r||mode==='copy'||T.done;
     const col=r?(r.skip?'var(--bad)':r.m===0?'var(--jade)':r.m<=2?'var(--warn)':'var(--bad)'):'var(--muted)';
     return `<span style="width:36px;height:40px;display:grid;place-items:center;border:${isCur?'2px solid var(--jade)':'1px solid var(--line)'};border-radius:6px;background:var(--surface);font-family:'Noto Serif SC',serif;font-size:1.35rem;color:${r?col:'var(--muted)'};${!r&&mode==='copy'&&!isCur?'opacity:.45':''}">${show?esc(u.ch):''}</span>`; }).join('')}</div>`;
  const prompt=mode==='copy'?`<div style="font-family:'Noto Serif SC',serif;font-size:1.25rem">${esc(s.zh)}</div><div class="small" style="color:var(--jade)">${esc(s.py)}</div><div class="small muted">${esc(s.vi)}</div>`
    :mode==='dict'?`<div style="color:var(--jade);font-weight:600">${esc(s.py)}</div><div class="small muted">${esc(s.vi)}</div>`
    :`<div style="font-weight:600">${esc(s.vi)}</div>${T.peek?`<div class="small" style="color:var(--jade)">${esc(s.py)}</div>`:''}`;
  V.innerHTML=head+`<div class="card" style="padding:12px;text-align:center">${prompt}
     <div class="row" style="justify-content:center;gap:6px;margin-top:6px"><button class="btn sm" id="ssay">🔊 Nghe câu</button>${mode==='tran'&&!T.peek?'<button class="btn sm" id="speek">Gợi ý pinyin</button>':''}</div></div>
   ${strip}
   ${T.done?'':`<div class="card" style="padding:10px"><div class="small muted" style="text-align:center;margin-bottom:6px">Chữ ${T.k+1}/${N}${cur.dup?' · đã viết ở trên, viết lại':''}</div>
     <div id="wbox" style="position:relative;margin:0 auto;touch-action:none;user-select:none;-webkit-user-select:none;background:var(--surface);border-radius:8px"></div>
     <div id="wfb" class="small" style="text-align:center;min-height:1.6em;margin-top:6px"></div>
     <div class="acts" style="margin-top:4px"><button class="btn" id="sskip">${mode==='copy'?'Bỏ qua chữ':'Không nhớ chữ này'}</button></div></div>`}
   <div id="sres"></div>`;
  $('#sback').onclick=()=>{ WW=null; go('viet'); WR.set.tab='sent'; };
  $('#ssay').onclick=()=>playRef(s.zh);
  const pk=$('#speek'); if(pk) pk.onclick=()=>{ T.peek=true; render(); };
  if(T.done) return sentShowResult();
  if(T.k===0&&!T.res.length&&mode!=='copy') playRef(s.zh);
  const cfg=mode==='copy'?{showOutline:true,showHintAfterMisses:1}:{showOutline:false,showHintAfterMisses:3};
  const w=wMount(cur.ch,Object.assign({showCharacter:false},cfg)); const fb=$('#wfb');
  if(!w){ fb.textContent='Không tải được nét của chữ này.'; return; }
  let miss=0, ended=false;
  const next=(skip)=>{ if(ended) return; ended=true; T.res.push({c:cur.ch,m:skip?99:miss,skip:!!skip,dup:cur.dup});
    const go2=()=>{ T.k++; if(T.k>=N){ T.done=true; T.sc=sentRecord(T); } render(); };
    if(skip){ try{ w.cancelQuiz(); }catch(e){} w.showCharacter(); fb.innerHTML=`Chữ đúng: <b style="font-family:'Noto Serif SC',serif;font-size:1.2rem">${esc(cur.ch)}</b>`; setTimeout(go2,1100); }
    else setTimeout(go2,miss?650:350); };
  w.quiz({onMistake:st=>{ miss++; fb.innerHTML=`<span style="color:var(--bad)">Sai nét ${st.strokeNum+1}</span> · ${miss} lỗi`; },
    onCorrectStroke:st=>{ fb.innerHTML=`<span style="color:var(--jade)">✓ nét ${st.strokeNum+1}</span>${miss?` · ${miss} lỗi`:''}`; },
    onComplete:()=>next(false)});
  $('#sskip').onclick=()=>next(true);
}
function sentShowResult(){
  const Q=SUB.sent, T=Q.cur, bad=[...new Set(T.res.filter(r=>r.skip||r.m>=3).map(r=>r.c))];
  const nextMode=T.mode==='copy'?'dict':T.mode==='dict'?'tran':null;
  $('#sres').innerHTML=`<div class="card" style="text-align:center;padding:16px">
    <div style="font-size:2.2rem;font-weight:700">${Math.round(T.sc*100)}%</div>
    <p class="small muted" style="margin:2px 0 8px">${T.res.filter(r=>r.m<=2&&!r.skip).length}/${T.res.length} chữ viết đạt (sai ≤ 2 nét)${T.mode!=='copy'?' · chữ đến hạn ôn viết đã được tính lượt ôn':''}</p>
    ${bad.length?`<p class="small">Chữ cần luyện thêm: <span style="font-family:'Noto Serif SC',serif;font-size:1.3rem;color:var(--bad)">${bad.map(esc).join(' ')}</span></p>`:''}
    <div class="row" style="justify-content:center;gap:8px;flex-wrap:wrap">
     <button class="btn pri" id="snext">${Q.i<Q.q.length-1?'Câu tiếp':'Xong'} <small style="opacity:.7">(Enter)</small></button>
     <button class="btn" id="sagain">Viết lại</button>
     ${nextMode&&T.sc>=.8?`<button class="btn" id="sup">Thử ${SMODES[nextMode].n}</button>`:''}
     ${bad.length?`<button class="btn" id="sbad">Luyện riêng chữ sai</button>`:''}</div></div>`;
  $('#snext').onclick=()=>{ Q.i++; Q.cur=null; render(); window.scrollTo(0,0); };
  $('#sagain').onclick=()=>{ Q.cur=null; render(); };
  const up=$('#sup'); if(up) up.onclick=()=>{ Q.mode=nextMode; Q.cur=null; render(); };
  const sb=$('#sbad'); if(sb) sb.onclick=()=>wStartLearn(bad.join(''));
  setTimeout(()=>{ const b=$('#snext'); if(b) b.focus({preventScroll:true}); },50);
}
function renderSentDone(){
  const Q=SUB.sent, S=WR.sent||{}, rows=Q.q.map(s=>({s,r:S[s.zh]}));
  V.innerHTML=`<div class="card" style="text-align:center;padding:20px 14px"><div class="small muted">Viết câu · ${SMODES[Q.mode].n}</div><div style="font-size:2rem;font-weight:700;margin:6px 0">${Q.q.length} câu</div>
    <div class="list" style="text-align:left;margin-top:8px">${rows.map(({s,r})=>`<div class="item"><div><div style="font-family:'Noto Serif SC',serif">${esc(s.zh)}</div><div class="small muted">${esc(s.vi)}</div></div><b class="small">${r?Math.round(r.best*100)+'%':''}</b></div>`).join('')}</div>
    <div class="row" style="justify-content:center;gap:8px;margin-top:12px"><button class="btn pri" id="smore">Viết 5 câu nữa</button><button class="btn" id="slist">Về danh sách</button></div></div>`;
  $('#smore').onclick=()=>sentStart(sentPick(5)); $('#slist').onclick=()=>{ WR.set.tab='sent'; go('viet'); };
}
document.addEventListener('click',e=>{ const b=e.target.closest&&e.target.closest('[data-ws]'); if(!b) return; e.preventDefault(); wOpenSent(b.dataset.ws); });

