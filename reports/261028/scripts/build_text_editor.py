# -*- coding: utf-8 -*-
"""위쳌 화면 전체 글 편집 페이지. 화면 안 글자를 누르면 그 자리에서 고치고, 고친 글은 "바뀐 글 복사"로 전·후 목록을 복사해 전달.
치킨집·산후조리원 × 상세페이지형·수치형·인터뷰형 × 위생정보·장소정보 탭 + 사장님 선택 화면 전부.
실행: python3 reports/261028/scripts/build_text_editor.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B, build_tpl as T

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = 'wecheck_text_editor_261102.html'

CSS = r"""
body{margin:0;background:var(--bg);font-family:Pretendard Variable,Pretendard,-apple-system,BlinkMacSystemFont,system-ui,sans-serif;color:var(--ink)}
.wrap{max-width:1320px;margin:0 auto;padding:20px}
.wrap h1{font-size:18px;margin:0 0 4px}
.wrap .desc{font-size:12.5px;color:#3E444A;line-height:1.6;margin:0 0 12px}
.ctl{display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;margin-bottom:12px}
.ctl .grp{display:flex;gap:4px;align-items:center;font-size:11.5px;font-weight:800;color:var(--muted)}
.ctl button{font:inherit;font-size:12px;font-weight:800;padding:7px 11px;border-radius:8px;border:1px solid #C9D0D8;background:#fff;color:var(--ink);cursor:pointer}
.ctl button.on{background:var(--wc);border-color:var(--wc);color:#fff}
.lay{display:grid;grid-template-columns:410px 1fr;gap:20px;align-items:start}
@media (max-width:900px){.lay{grid-template-columns:1fr}}
.stage{position:relative}
.stage .phone{margin:0 auto;cursor:text}
.stage .ed{width:390px;margin:0 auto;cursor:text}
.stage .phone *:hover,.stage .ed *:hover{outline:1px dashed rgba(0,114,206,.55);outline-offset:-1px}
mark.edt{background:#FFF3B0;color:inherit;border-radius:2px;padding:0 1px}
.side{position:sticky;top:12px}
.side .bar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
.side button{font:inherit;font-size:12px;font-weight:800;padding:8px 12px;border-radius:8px;border:1px solid #C9D0D8;background:#fff;color:var(--ink);cursor:pointer}
.side button.pri{background:var(--wc);border-color:var(--wc);color:#fff}
.side .msg{font-size:11.5px;color:#0B5E31;margin:0 0 8px;min-height:16px}
.list{background:#fff;border-radius:12px;padding:6px 14px;max-height:60vh;overflow:auto}
.list .e{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:9px 0;border-top:1px solid var(--line);font-size:12px;line-height:1.5}
.list .e:first-child{border-top:0}
.list .e .o{color:#9A9A9A;text-decoration:line-through;grid-column:1}
.list .e .n{color:var(--ink);font-weight:700;grid-column:1}
.list .e button{grid-column:2;grid-row:1/3;align-self:center;font-size:11px;padding:4px 8px}
.list .empty{font-size:12px;color:var(--muted);padding:10px 0}
.out{margin-top:12px;width:100%;box-sizing:border-box;font:inherit;font-size:11.5px;line-height:1.5;padding:8px 10px;border:1px solid #C9D0D8;border-radius:8px;min-height:80px;white-space:pre-wrap;background:#fff}
.pop{position:absolute;z-index:50;background:#fff;border:1px solid #C9D0D8;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.18);padding:10px;width:300px;max-width:calc(100vw - 32px)}
.pop textarea{width:100%;box-sizing:border-box;font:inherit;font-size:13px;line-height:1.5;padding:7px 9px;border:1px solid #C9D0D8;border-radius:8px;min-height:64px;resize:vertical}
.pop .row{display:flex;gap:6px;justify-content:flex-end;margin-top:6px}
.pop .row small{margin-right:auto;font-size:10.5px;color:var(--muted);align-self:center}
.pop button{font:inherit;font-size:12px;font-weight:800;padding:6px 10px;border-radius:8px;border:1px solid #C9D0D8;background:#fff;cursor:pointer}
.pop button.pri{background:var(--wc);border-color:var(--wc);color:#fff}
"""

JS = r"""
const KEY='wc_text_edits_261102';
let EDITS=[]; // {o:원문, n:새 글}
try{EDITS=JSON.parse(localStorage.getItem(KEY)||'[]');}catch(e){}
const stage=document.getElementById('stage'), pop=document.getElementById('pop');
let view={bk:'chicken', t:'C', tab:'hy', ed:false};
function ren(){
  pop.hidden=true;
  if(view.ed){ stage.innerHTML=`<div class="ed"><div class="bar">위생 페이지 관리<span class="sv">저장</span></div><div class="in" data-ed data-biz="${view.bk}"></div></div>`; }
  else { stage.innerHTML=`<div class="phone"><div data-static data-biz="${view.bk}" data-t="${view.t}" data-tab="${view.tab}" data-mt="${view.bk==='chicken'?'white':'blue'}"></div></div>`; }
  refresh(view.bk);
  document.querySelectorAll('.ctl button[data-k]').forEach(b=>{const k=b.dataset.k, v=b.dataset.v; b.classList.toggle('on', k==='ed'?(view.ed===(v==='1')):(!view.ed||k==='bk')&&String(view[k])===v);});
}
function textNodes(root){const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>{if(!n.nodeValue.trim())return NodeFilter.FILTER_REJECT; const p=n.parentElement; if(!p||p.closest('script,style'))return NodeFilter.FILTER_REJECT; return NodeFilter.FILTER_ACCEPT;}}); const a=[]; let n; while(n=w.nextNode()) a.push(n); return a;}
let applying=false;
function applyEdits(){
  if(applying) return; applying=true;
  textNodes(stage).forEach(n=>{
    const raw=n.nodeValue, tx=raw.trim(); const e=EDITS.find(x=>x.o===tx); if(!e) return;
    const lead=raw.slice(0,raw.indexOf(tx)), trail=raw.slice(raw.indexOf(tx)+tx.length);
    const m=document.createElement('mark'); m.className='edt'; m.dataset.o=e.o; m.textContent=e.n;
    const f=document.createDocumentFragment(); if(lead) f.appendChild(document.createTextNode(lead)); f.appendChild(m); if(trail) f.appendChild(document.createTextNode(trail));
    n.parentNode.replaceChild(f,n);
  });
  applying=false; save(); renderList();
}
new MutationObserver(()=>{ if(!applying) applyEdits(); }).observe(stage,{childList:true,subtree:true});
const hasWord=n=>/[가-힣A-Za-z0-9]/.test(n.nodeValue);
function nodeAt(x,y,el){
  let r=null;
  if(document.caretPositionFromPoint){const c=document.caretPositionFromPoint(x,y); r=c&&c.offsetNode;}
  else if(document.caretRangeFromPoint){const c=document.caretRangeFromPoint(x,y); r=c&&c.startContainer;}
  if(r&&r.nodeType===3&&hasWord(r)&&el.contains(r)) return r;
  // 아이콘(✅ 👶 같은 기호만 있는 조각)은 건너뛰고, 누른 자리와 겹치는 글 조각, 없으면 제일 긴 글 조각
  const ns=textNodes(el).filter(hasWord); if(!ns.length) return null;
  for(const n of ns){const rg=document.createRange(); rg.selectNodeContents(n); for(const b of rg.getClientRects()){ if(x>=b.left-4&&x<=b.right+4&&y>=b.top-4&&y<=b.bottom+4) return n; }}
  return ns.slice().sort((a,b)=>b.nodeValue.trim().length-a.nodeValue.trim().length)[0];
}
let target=null;
stage.addEventListener('click',e=>{
  const m=e.target.closest('mark.edt');
  let orig, cur, node;
  if(m){ orig=m.dataset.o; cur=m.textContent; node=m; }
  else { let n=nodeAt(e.clientX,e.clientY,e.target); if(!n&&e.target.parentElement&&stage.contains(e.target.parentElement)) n=nodeAt(e.clientX,e.clientY,e.target.parentElement); if(!n) return; orig=n.nodeValue.trim(); cur=orig; node=n; }
  e.preventDefault(); e.stopPropagation();
  target={orig};
  document.getElementById('ta').value=cur; document.getElementById('po').textContent=orig;
  const r=(node.nodeType===3?node.parentElement:node).getBoundingClientRect(), sr=stage.getBoundingClientRect();
  pop.hidden=false; pop.style.left=Math.max(0,Math.min(r.left-sr.left, sr.width-310))+'px'; pop.style.top=(r.bottom-sr.top+6)+'px';
  document.getElementById('ta').focus();
},true);
function setEdit(o,n){ EDITS=EDITS.filter(x=>x.o!==o); if(n!==o) EDITS.push({o,n}); save(); ren(); }
document.getElementById('ok').addEventListener('click',()=>{const n=document.getElementById('ta').value.trim(); if(!n){return;} setEdit(target.orig,n);});
document.getElementById('undo').addEventListener('click',()=>setEdit(target.orig,target.orig));
document.getElementById('cancel').addEventListener('click',()=>pop.hidden=true);
document.getElementById('ta').addEventListener('keydown',e=>{if(e.key==='Enter'&&(e.metaKey||e.ctrlKey)) document.getElementById('ok').click(); if(e.key==='Escape') pop.hidden=true;});
let DB=null, dbReady=false, saveT=null;
function save(){ try{localStorage.setItem(KEY, JSON.stringify(EDITS));}catch(e){} if(DB){ clearTimeout(saveT); saveT=setTimeout(saveDb,600); } }
async function saveDb(){ try{ await DB.doc('edits/current').set({items:EDITS, at:Date.now()}); setSt('저장됨 · 클로드가 바로 읽을 수 있어요'); }catch(e){ setSt('저장 실패: '+(e&&e.code||e)); } }
function setSt(t){ const el=document.getElementById('st'); if(el) el.textContent=t; }
(async()=>{
  if(!window.claude||!window.claude.use){ setSt('이 브라우저에만 저장됨 · "바뀐 글 복사"로 보내 주세요'); return; }
  try{ DB=await window.claude.use('db'); }catch(e){ DB=null; }
  if(!DB){ setSt('이 브라우저에만 저장됨 · "바뀐 글 복사"로 보내 주세요'); return; }
  try{ const snap=await DB.doc('edits/current').get(); if(snap.exists){ const d=snap.data(); if(Array.isArray(d.items)&&(!EDITS.length||(d.at||0)>0)){ EDITS=d.items; try{localStorage.setItem(KEY, JSON.stringify(EDITS));}catch(e){} ren(); } } setSt('저장됨 · 클로드가 바로 읽을 수 있어요'); }
  catch(e){ setSt('공유 저장소를 못 읽었어요: '+(e&&e.code||e)); }
})();
function renderList(){ const el=document.getElementById('list'); el.innerHTML=EDITS.length?EDITS.map((e,i)=>`<div class="e"><span class="o">${esc(e.o)}</span><span class="n">${esc(e.n)}</span><button type="button" data-rm="${i}">되돌리기</button></div>`).join(''):'<div class="empty">아직 고친 글이 없어요. 왼쪽 화면의 글자를 눌러 보세요.</div>'; document.getElementById('cnt').textContent=EDITS.length; }
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
document.getElementById('list').addEventListener('click',e=>{const b=e.target.closest('[data-rm]'); if(b){EDITS.splice(+b.dataset.rm,1); save(); ren();}});
function diffText(){ return EDITS.length?EDITS.map((e,i)=>`${i+1}.\n   전: ${e.o}\n   후: ${e.n}`).join('\n\n'):'바뀐 글이 없어요.'; }
document.getElementById('copy').addEventListener('click',async()=>{const t=diffText(); document.getElementById('out').textContent=t; try{await navigator.clipboard.writeText(t); document.getElementById('msg').textContent='복사했어요. 그대로 붙여 넣어 주세요.';}catch(e){document.getElementById('msg').textContent='아래 상자 글을 직접 복사해 주세요.';}});
document.getElementById('reset').addEventListener('click',()=>{if(!confirm('고친 글을 모두 처음으로 되돌릴까요?'))return; EDITS=[]; save(); ren(); document.getElementById('out').textContent=''; document.getElementById('msg').textContent='처음 글로 되돌렸어요.';});
document.querySelector('.ctl').addEventListener('click',e=>{const b=e.target.closest('button[data-k]'); if(!b) return; const k=b.dataset.k, v=b.dataset.v; if(k==='ed') view.ed=(v==='1'); else { view[k]=v; if(k!=='bk') view.ed=false; } ren();});
// 화면 안 탭·카드 조작으로 다시 그려져도 편집이 유지되도록 MutationObserver가 처리
ren();
"""

def build():
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 화면 글 편집</title>{B.FONT}<style>{B.CSS}{T.EXTRA_CSS}{CSS}</style></head>
<body><div class="wrap">
<h1>위쳌 화면 · 글 편집</h1>
<p class="desc">왼쪽 화면에서 <b>고치고 싶은 글자를 누르면</b> 입력창이 뜹니다. 고치면 그 자리에 노란 표시로 바로 바뀌고, 같은 글이 다른 화면에 있으면 거기도 같이 바뀝니다. 고친 글은 이 브라우저에만 남고 사이트에는 반영되지 않습니다. 다 고친 뒤 <b>바뀐 글 복사</b>를 눌러 그대로 보내 주시면 시안 세 파일과 생성 스크립트에 넣습니다. 화면 안 탭, 카드, 체크박스는 평소처럼 눌러 볼 수 있습니다. 상호·수치·문진 원문·엑셀 원문을 고치면 원문 수정으로 알고 진행합니다.</p>
<div class="ctl">
<div class="grp">업종 <button type="button" data-k="bk" data-v="chicken">치킨집</button><button type="button" data-k="bk" data-v="care">산후조리원</button></div>
<div class="grp">화면 <button type="button" data-k="t" data-v="C">상세페이지형</button><button type="button" data-k="t" data-v="A">수치형</button><button type="button" data-k="t" data-v="B">인터뷰형</button><button type="button" data-k="ed" data-v="1">사장님 선택 화면</button></div>
<div class="grp">탭 <button type="button" data-k="tab" data-v="hy">위생정보</button><button type="button" data-k="tab" data-v="place">장소정보</button></div>
</div>
<div class="lay">
<div class="stage" id="stage"></div>
<div class="side">
<div class="bar"><button type="button" class="pri" id="copy">바뀐 글 복사</button><button type="button" id="reset">처음 글로</button><span style="font-size:12px;color:var(--muted);align-self:center">고친 글 <b id="cnt">0</b>개</span></div>
<p class="msg" id="st" style="color:var(--muted)"></p>
<p class="msg" id="msg"></p>
<div class="list" id="list"></div>
<pre class="out" id="out"></pre>
</div></div></div>
<div class="pop" id="pop" hidden><div style="font-size:10.5px;color:var(--muted);margin-bottom:4px">원래 글: <span id="po"></span></div><textarea id="ta"></textarea><div class="row"><small>Ctrl+Enter 저장 · Esc 닫기</small><button type="button" id="undo">원래대로</button><button type="button" id="cancel">닫기</button><button type="button" class="pri" id="ok">바꾸기</button></div></div>
<script>{T.js_block()}</script>
<script>{JS}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
