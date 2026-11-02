# -*- coding: utf-8 -*-
"""위쳌 도구 측정 블록(스탬프형) 글 편집 페이지.
왼쪽 입력칸에서 글을 고치면 오른쪽 치킨집·산후조리원 블록이 바로 바뀐다. "바뀐 글 복사"로 목록을 복사해 전달.
실행: python3 reports/261028/scripts/build_tools_editor.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B, build_tpl as T

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = 'wecheck_tools_text_editor_261102.html'

CSS = r"""
body{margin:0;background:var(--bg);font-family:Pretendard Variable,Pretendard,-apple-system,BlinkMacSystemFont,system-ui,sans-serif;color:var(--ink)}
.wrap{max-width:1320px;margin:0 auto;padding:20px}
.wrap h1{font-size:18px;margin:0 0 4px}
.wrap .desc{font-size:12.5px;color:#3E444A;line-height:1.6;margin:0 0 14px}
.lay{display:grid;grid-template-columns:1fr 410px;gap:20px;align-items:start}
@media (max-width:980px){.lay{grid-template-columns:1fr}}
.form{background:#fff;border-radius:12px;padding:6px 18px 14px}
.grp{padding:12px 0 6px;border-top:1px solid var(--line)}
.grp:first-child{border-top:0}
.grp h3{margin:0 0 6px;font-size:13px;font-weight:900}
.grp h3 small{font-weight:600;color:var(--muted);font-size:11px;margin-left:6px}
.f{display:grid;grid-template-columns:150px 1fr;gap:4px 12px;align-items:start;padding:5px 0}
.f label{font-size:11.5px;font-weight:800;color:#3E444A;padding-top:7px;line-height:1.4}
.f label i{display:block;font-style:normal;font-weight:600;color:var(--muted);font-size:10.5px}
.f label .x{display:inline-block;font-size:9.5px;font-weight:900;color:#9A6B12;background:#FBF7EC;border-radius:4px;padding:1px 5px;margin-top:3px}
.f input,.f textarea{width:100%;box-sizing:border-box;font:inherit;font-size:12.5px;line-height:1.5;padding:6px 9px;border:1px solid #C9D0D8;border-radius:8px;background:#fff;color:var(--ink)}
.f textarea{min-height:52px;resize:vertical}
.f input.ch,.f textarea.ch{border-color:var(--wc);background:#F3F8FE}
@media (max-width:600px){.f{grid-template-columns:1fr}.f label{padding-top:0}}
.prev{position:sticky;top:12px}
.prev .bar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.prev button,.form button{font:inherit;font-size:12px;font-weight:800;padding:8px 12px;border-radius:8px;border:1px solid #C9D0D8;background:#fff;color:var(--ink);cursor:pointer}
.prev button.pri{background:var(--wc);border-color:var(--wc);color:#fff}
.prev .msg{font-size:11.5px;color:#0B5E31;margin:0 0 8px;min-height:16px}
.prev .pvbox{background:var(--bg);border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.14),0 0 0 1px rgba(0,0,0,.06);padding:10px 0;margin-bottom:14px}
.prev .pvbox .cap{font-size:11.5px;font-weight:800;margin:0 16px 6px;color:var(--ink)}
.prev .pvbox .cap small{font-weight:500;color:var(--muted);margin-left:6px}
.out{margin-top:14px;width:100%;box-sizing:border-box;font:inherit;font-size:11.5px;line-height:1.5;padding:8px 10px;border:1px solid #C9D0D8;border-radius:8px;min-height:120px;white-space:pre-wrap}
"""

JS = r"""
const F=[
 ['공통',[
  ['TXT.title','제목','',0],['TXT.sub','부제','',0],['TXT.lg','파란 표식','<br>로 줄바꿈',0],['TXT.seal','도장 안 글자','',0],['TXT.more','펼침 글자','',0],['TXT.date','체크일 앞말','',0]]],
 ['악취 · 두 업종 공통',[
  ['tools.0.hl','결과 문장','도장 아래 큰 글씨',0],['tools.0.k','측정 항목','작은 글씨 앞',0],['tools.0.tool','측정 도구','작은 글씨 뒤',0],
  ['tools.0.levels.0.0','단계 1 이름','이 사업장 단계',1],['tools.0.levels.0.1','단계 1 설명','',1],['tools.0.levels.1.0','단계 2 이름','',1],['tools.0.levels.1.1','단계 2 설명','펼쳤을 때는 안 보이고 칩에 마우스 올리면',1],['tools.0.levels.2.0','단계 3 이름','',1],['tools.0.levels.2.1','단계 3 설명','',1],
  ['tools.0.ex','예시 문구','',1]]],
 ['악취 · 업종별',[
  ['chicken.tools.0.easy','치킨집 쉬운 설명','',0],['chicken.tools.0.date','치킨집 체크일','',0],['care.tools.0.easy','산후조리원 쉬운 설명','',0],['care.tools.0.date','산후조리원 체크일','',0]]],
 ['배수구 · 두 업종 공통',[
  ['tools.1.hl','결과 문장','도장 아래 큰 글씨',0],['tools.1.k','측정 항목','',0],['tools.1.tool','측정 도구','',0],
  ['tools.1.levels.0.0','단계 1 이름','이 사업장 단계',1],['tools.1.levels.0.1','단계 1 설명','',1],['tools.1.levels.1.0','단계 2 이름','',1],['tools.1.levels.1.1','단계 2 설명','',1],['tools.1.levels.2.0','단계 3 이름','',1],['tools.1.levels.2.1','단계 3 설명','',1],['tools.1.levels.3.0','단계 4 이름','',1],['tools.1.levels.3.1','단계 4 설명','',1],
  ['tools.1.ex','예시 문구','②시트 숙박 행 문구',1]]],
 ['배수구 · 업종별',[
  ['chicken.tools.1.easy','치킨집 쉬운 설명','',0],['chicken.tools.1.date','치킨집 체크일','',0],['care.tools.1.easy','산후조리원 쉬운 설명','',0],['care.tools.1.date','산후조리원 체크일','',0]]],
];
const KEY='wc_tools_txt_261102';
function targets(path){ // path -> [obj,key][]
  const p=path.split('.');
  if(p[0]==='TXT') return [[TXT,p[1]]];
  const bks=(p[0]==='chicken'||p[0]==='care')?[p.shift()]:['chicken','care'];
  return bks.map(bk=>{let o=D[bk]; for(let i=0;i<p.length-1;i++) o=o[p[i]]; return [o,p[p.length-1]];});
}
function getv(path){const [[o,k]]=targets(path); return o[k];}
function setv(path,v){targets(path).forEach(([o,k])=>o[k]=v);}
const DEF={}; F.forEach(([g,fs])=>fs.forEach(([p])=>DEF[p]=getv(p)));
function buildForm(){
  const el=document.getElementById('form');
  el.innerHTML=F.map(([g,fs])=>`<div class="grp"><h3>${g}</h3>${fs.map(([p,l,h,x])=>{const v=getv(p); const long=v.length>40; return `<div class="f"><label for="f_${p}">${l}${h?`<i>${h}</i>`:''}${x?'<span class="x">엑셀 원문</span>':''}</label>${long?`<textarea id="f_${p}" data-p="${p}">${v}</textarea>`:`<input id="f_${p}" data-p="${p}" value="${v.replace(/"/g,'&quot;')}">`}</div>`;}).join('')}</div>`).join('');
}
function apply(){ document.querySelectorAll('[data-p]').forEach(i=>{setv(i.dataset.p,i.value); i.classList.toggle('ch',i.value!==DEF[i.dataset.p]);}); Object.keys(D).forEach(refreshPreviews); save(); }
function save(){ try{const o={}; document.querySelectorAll('[data-p]').forEach(i=>{if(i.value!==DEF[i.dataset.p]) o[i.dataset.p]=i.value;}); localStorage.setItem(KEY, JSON.stringify(o));}catch(e){} }
function load(){ try{const o=JSON.parse(localStorage.getItem(KEY)||'{}'); Object.entries(o).forEach(([p,v])=>{const i=document.getElementById('f_'+p); if(i) i.value=v;});}catch(e){} }
function diffText(){
  const lines=[]; let n=0;
  F.forEach(([g,fs])=>fs.forEach(([p,l])=>{const i=document.getElementById('f_'+p); if(i&&i.value!==DEF[p]){n++; lines.push(`${n}. [${g} · ${l}]\n   전: ${DEF[p]}\n   후: ${i.value}`);}}));
  return lines.length?lines.join('\n\n'):'바뀐 글이 없어요.';
}
document.getElementById('form').addEventListener('input',apply);
document.getElementById('copy').addEventListener('click',async()=>{const t=diffText(); document.getElementById('out').textContent=t; try{await navigator.clipboard.writeText(t); document.getElementById('msg').textContent='복사했어요. 그대로 붙여 넣어 주세요.';}catch(e){document.getElementById('msg').textContent='아래 상자 글을 직접 복사해 주세요.';}});
document.getElementById('reset').addEventListener('click',()=>{if(!confirm('고친 글을 모두 처음으로 되돌릴까요?'))return; document.querySelectorAll('[data-p]').forEach(i=>i.value=DEF[i.dataset.p]); apply(); document.getElementById('out').textContent=''; document.getElementById('msg').textContent='처음 글로 되돌렸어요.';});
buildForm(); load(); apply();
"""

def build():
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 도구 측정 블록 글 편집</title>{B.FONT}<style>{B.CSS}{T.EXTRA_CSS}{CSS}</style></head>
<body><div class="wrap">
<h1>위쳌 도구 측정 블록 · 글 편집</h1>
<p class="desc">왼쪽 칸의 글을 고치면 오른쪽 치킨집·산후조리원 블록이 바로 바뀝니다. 고친 칸은 파랗게 표시되고 이 브라우저에 남습니다(사이트에는 반영되지 않습니다). 다 고친 뒤 <b>바뀐 글 복사</b>를 눌러 그대로 보내 주시면 시안 세 파일에 넣습니다. "엑셀 원문" 표시가 있는 칸은 ③시트 문구라 고치면 원문 수정으로 알고 진행합니다. 블록의 카드를 누르면 펼쳐지고 접힙니다.</p>
<div class="lay">
<div class="form" id="form"></div>
<div class="prev">
<div class="bar"><button type="button" class="pri" id="copy">바뀐 글 복사</button><button type="button" id="reset">처음 글로</button></div>
<p class="msg" id="msg"></p>
<div class="pvbox"><div class="cap">치킨집<small>열한시 치킨</small></div><div data-tools data-biz="chicken" data-tv="D"></div></div>
<div class="pvbox"><div class="cap">산후조리원<small>볕드는집 산후조리원</small></div><div data-tools data-biz="care" data-tv="D"></div></div>
<pre class="out" id="out"></pre>
</div></div></div>
<script>{T.js_block()}</script>
<script>{JS}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
