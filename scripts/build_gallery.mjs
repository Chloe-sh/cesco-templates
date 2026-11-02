// captures/<날짜>/manifest.json 으로 index.html 의 d103 "시안 갤러리" 문서를 (재)생성한다.
// 사용: node scripts/build_gallery.mjs [captures/261102/manifest.json]
// index.html 안의 마커 사이만 바꾼다: <!-- GALLERY:START --> … <!-- GALLERY:END --> (문서 본문),
// /* GALLERY:CSS:START */ … /* GALLERY:CSS:END */ (스타일), SECS 의 "d103" 항목, 목차 버튼의 건수.
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const manifestPath = path.resolve(ROOT, process.argv[2] || 'captures/261102/manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const capDir = path.relative(ROOT, path.dirname(manifestPath)).replace(/\\/g, '/');
const indexPath = path.join(ROOT, 'index.html');
let html = fs.readFileSync(indexPath, 'utf8');

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const href = f => f.split('/').map(encodeURIComponent).join('/');
const link = it => href(it.file) + (it.hash ? '#' + it.hash : '');
const docTitle = {};
for (const m of html.matchAll(/<article class="doc" id="(d\d+)"[\s\S]*?<span class="cr-label">([^<]*)<\/span>/g)) docTitle[m[1]] = m[2];
const tplLabel = id => docTitle[id] ? `${id} ${docTitle[id]}` : id;

const items = manifest.items;
const groups = manifest.groups.map((g, i) => ({ ...g, n: i + 1, items: items.filter(it => it.group === g.key) })).filter(g => g.items.length);
const total = items.length;
const capDate = manifest.captured;
const [cy, cm, cd] = capDate.split('-');

function card(it, skipTpl) {
  const thumb = `${capDir}/${it.id}_thumb.jpg`, full = `${capDir}/${it.id}_full.jpg`;
  const meta = [it.date.replace(/^2026-/, '').replace('-', '/'), it.ver].filter(Boolean).join(' · ');
  let c = `<figure class="gal-card${it.star ? ' star' : ''}" data-gal-item="${it.id}">`;
  c += `<button type="button" class="gal-thumb" data-full="${full}" data-open="${link(it)}" data-title="${esc(it.type + ' — ' + it.title)}" aria-label="${esc(it.title)} 전체 캡처 보기"><img src="${thumb}" alt="" loading="lazy" width="640" height="800"></button>`;
  c += `<figcaption><span class="gal-type">${esc(it.type)}${it.star ? ' <em>★</em>' : ''}</span><b class="gal-title">${esc(it.title)}</b><span class="gal-meta">${esc(meta)}</span>`;
  c += `<span class="gal-actions"><a class="gal-open" href="${link(it)}" target="_blank" rel="noopener">열기 ↗</a>`;
  if (it.draft) c += `<a class="gal-draft" href="${href(it.draft)}" target="_blank" rel="noopener" title="원고 확인용 코드 초안형">초안</a>`;
  for (const t of it.tpl) if (t !== skipTpl) c += `<button type="button" class="xref gal-xref" data-goto="${t}" title="${esc(tplLabel(t))}">${t}</button>`;
  return c + `</span></figcaption></figure>`;
}

// ---------- 본문 ----------
let body = '';
body += `<article class="doc" id="d103" hidden><header class="dochead"><div class="crumb"><span class="cr-code">··</span><span class="cr-name">개요</span><span class="cr-sep">/</span><span class="cr-label">시안 갤러리</span><span class="stat s-ok">${capDate} 캡처</span></div><div class="path">${capDir}/ · reports/ 폴더의 시안 ${total}건을 ${capDate}에 캡처 · 재생성은 scripts/capture_reports.mjs → scripts/build_gallery.mjs</div></header>`;
body += `<h1>시안 갤러리 — 템플릿별 시안 ${total}건 한눈에 보기</h1>`;
body += `<p class="idx-lead">10월에 만든 시안을 채널별로 모았습니다. 템플릿을 고를 때 글로 된 규칙보다 완성된 모습부터 보고 싶을 때 씁니다. <strong>썸네일을 누르면 전체 캡처</strong>가 크게 열리고, <strong>열기 ↗</strong>는 탭·스와이프가 그대로 움직이는 실제 페이지를 새 창에 엽니다. 카드 아래 칩은 그 시안이 따른 템플릿 문서입니다.</p>`;
body += `<div class="wide gal-filter" role="tablist" aria-label="채널 필터"><button type="button" class="gal-chip on" data-gal="all">전체 <b>${total}</b></button>`;
for (const g of groups) body += `<button type="button" class="gal-chip" data-gal="${g.key}">${esc(g.label)} <b>${g.items.length}</b></button>`;
body += `</div>`;

for (const g of groups) {
  body += `<section class="wide gal-group" data-gal-group="${g.key}">`;
  body += `<h2 id="d103-s${g.n}"><span class="secnum">${String(g.n).padStart(2, '0')}</span>${esc(g.label)} <span class="gal-count">${g.items.length}건</span></h2>`;
  body += `<p class="gal-desc">${esc(g.desc)}`;
  if (g.tpl.length) body += ` <span class="gal-tpl">템플릿: ${g.tpl.map(t => `<button type="button" class="xref" data-goto="${t.id}">${esc(t.label)}</button>`).join(' · ')}</span>`;
  else body += ` <span class="gal-tpl">템플릿 문서 없음 (콘텐츠·기능 트랙 — 보고 자료 <a href="reports/261028/index.html" target="_blank" rel="noopener">10/28 위쳌 9종 비교 ↗</a>)</span>`;
  body += `</p><div class="gal-grid">`;
  for (const it of g.items) body += card(it);
  body += `</div></section>`;
}
body += `<h2 id="d103-s${groups.length + 1}"><span class="secnum">${String(groups.length + 1).padStart(2, '0')}</span>근거와 이력</h2><ul><li>${capDate}: reports/261020·261022·261026·261028 폴더의 시안 HTML ${total}건을 Edge 헤드리스(1280px 폭)로 캡처. 썸네일은 상단 1600px, 전체 캡처는 5200px까지 찍고 아래 빈 여백을 잘랐습니다. 탭·스와이프·버튼이 있는 시안은 첫 화면 기준이라 실제 페이지와 다를 수 있습니다.</li><li>2026-11-02: 리플릿은 전부 실물 디자인형(A4 2면, 원고는 v2 그대로)으로 캡처했습니다. 코드 초안형은 카드의 "초안" 링크로 볼 수 있습니다.</li><li>포함하지 않은 파일: 보고 자료 2건(reports/261026/index.html · reports/261028/index.html), 옛 주소 안내 페이지, 엑셀·이미지·스크립트.</li><li>시안이 늘면 <code>${capDir}/manifest.json</code>에 항목을 추가하고 <code>node scripts/capture_reports.mjs</code> → <code>node scripts/build_gallery.mjs</code> 순서로 다시 만듭니다. 캡처 1건당 2초쯤 걸립니다.</li></ul>`;
const lbHtml = `<div class="gal-lb" id="gal-lb" hidden><div class="gal-lb-bar"><span id="gal-lb-title"></span><a id="gal-lb-open" href="#" target="_blank" rel="noopener">실제 페이지 열기 ↗</a><button type="button" id="gal-lb-close" aria-label="닫기">닫기 ✕</button></div><div class="gal-lb-scroll"><img id="gal-lb-img" src="" alt=""></div></div>`;
body += `</article>`;

// ---------- 스타일 ----------
const css = `
.gal-filter{display:flex;flex-wrap:wrap;gap:.4rem;margin:.2rem 0 1.2rem}
.gal-chip{font-size:.82rem;font-weight:600;border:1px solid var(--rule);border-radius:999px;padding:.28rem .8rem;background:var(--surface);color:var(--ink-2)}
.gal-chip b{font-weight:700;color:var(--ink-3);margin-left:.15rem}
.gal-chip:hover{border-color:var(--accent);color:var(--accent)}
.gal-chip.on{background:var(--accent);border-color:var(--accent);color:#fff}
.gal-chip.on b{color:rgba(255,255,255,.8)}
.gal-group.hide{display:none}
.gal-count{font-size:.78rem;font-weight:600;color:var(--ink-3);margin-left:.1rem}
.gal-desc{color:var(--ink-2);font-size:.9rem}
.gal-tpl{display:inline-block;margin-left:.2rem;color:var(--ink-3);font-size:.84rem}
.gal-tpl .xref{font-size:.84rem}
.gal-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(15.5rem,1fr));gap:.9rem;margin:.2rem 0 1.6rem}
.gal-card{margin:0;display:flex;flex-direction:column;background:var(--surface);border:1px solid var(--rule);border-radius:10px;overflow:hidden;box-shadow:var(--shadow);transition:border-color .12s}
.gal-card:hover{border-color:var(--accent)}
.gal-card.star{border-color:var(--ok)}
.gal-thumb{display:block;width:100%;padding:0;background:#fff;border-bottom:1px solid var(--rule-soft);cursor:zoom-in;aspect-ratio:4/5;overflow:hidden}
.gal-thumb img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.gal-card figcaption{display:flex;flex-direction:column;gap:.25rem;padding:.65rem .8rem .75rem}
.gal-type{font-size:.7rem;font-weight:700;letter-spacing:.01em;color:var(--accent);text-transform:none}
.gal-type em{font-style:normal;color:var(--ok)}
.gal-title{font-size:.92rem;font-weight:700;letter-spacing:-.01em;line-height:1.35;text-wrap:balance}
.gal-meta{font-size:.74rem;color:var(--ink-3);font-variant-numeric:tabular-nums}
.gal-actions{display:flex;flex-wrap:wrap;gap:.3rem;align-items:center;margin-top:.35rem;padding-top:.45rem;border-top:1px dashed var(--rule-soft)}
.gal-open{font-size:.78rem;font-weight:700;color:var(--accent);text-decoration:none;border:1px solid var(--rule);border-radius:999px;padding:.14rem .6rem;background:var(--paper)}
.gal-open:hover{border-color:var(--accent);background:var(--accent-soft)}
.gal-draft{font-size:.74rem;color:var(--ink-3);text-decoration:underline;text-underline-offset:2px}
.gal-draft:hover{color:var(--accent)}
.gal-xref{font-size:.72rem;font-family:var(--mono);border:1px solid var(--rule-soft);border-radius:999px;padding:.1rem .45rem;background:var(--surface-2);color:var(--ink-2)}
.gal-xref:hover{color:var(--accent);border-color:var(--accent)}
.gal-strip{margin:1.1rem 0 .4rem;padding:.8rem .9rem .9rem;background:var(--surface-2);border:1px solid var(--rule);border-radius:10px}
.gal-strip-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4rem .8rem;margin-bottom:.65rem;font-size:.86rem}
.gal-strip-head b{font-weight:800;letter-spacing:-.01em}
.gal-strip-head b span{font-weight:600;color:var(--accent);margin-left:.1rem}
.gal-strip-hint{color:var(--ink-3);font-size:.76rem;flex:1}
.gal-strip-head .xref{font-size:.8rem}
.gal-grid-s{grid-template-columns:repeat(auto-fill,minmax(12.5rem,1fr));gap:.65rem;margin:0}
.gal-grid-s .gal-title{font-size:.84rem}
.gal-grid-s .gal-card figcaption{padding:.5rem .65rem .6rem}
.gal-lb{position:fixed;inset:0;z-index:50;background:rgba(10,16,21,.86);display:flex;flex-direction:column}
.gal-lb[hidden]{display:none!important}
.gal-lb-bar{display:flex;align-items:center;gap:1rem;padding:.6rem 1rem;background:var(--surface);border-bottom:1px solid var(--rule);color:var(--ink);font-size:.86rem}
.gal-lb-bar span{font-weight:700;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.gal-lb-bar a{color:var(--accent);font-weight:600;white-space:nowrap}
.gal-lb-bar button{font-weight:700;color:var(--ink-2);white-space:nowrap}
.gal-lb-scroll{flex:1;overflow:auto;padding:1.2rem 1rem 3rem;cursor:zoom-out}
.gal-lb-scroll img{display:block;margin:0 auto;max-width:min(1000px,100%);height:auto;background:#fff;box-shadow:0 18px 50px rgba(0,0,0,.5);border-radius:4px}
@media (max-width:760px){.gal-grid{grid-template-columns:repeat(2,1fr);gap:.6rem}.gal-card figcaption{padding:.5rem .6rem .6rem}.gal-lb-bar{font-size:.8rem;gap:.6rem}}
`;

// ---------- 스크립트 ----------
const js = `
  // 시안 갤러리: 채널 필터 + 전체 캡처 라이트박스
  var lb = document.getElementById('gal-lb');
  function lbClose(){ if(lb){ lb.hidden = true; document.getElementById('gal-lb-img').src = ''; } }
  document.addEventListener('click', function(e){
    var chip = e.target.closest('.gal-chip');
    if(chip){
      var k = chip.dataset.gal;
      document.querySelectorAll('.gal-chip').forEach(function(c){ c.classList.toggle('on', c === chip); });
      document.querySelectorAll('.gal-group').forEach(function(g){ g.classList.toggle('hide', k !== 'all' && g.dataset.galGroup !== k); });
      return;
    }
    var th = e.target.closest('.gal-thumb');
    if(th && lb){
      document.getElementById('gal-lb-img').src = th.dataset.full;
      document.getElementById('gal-lb-title').textContent = th.dataset.title;
      document.getElementById('gal-lb-open').href = th.dataset.open;
      lb.hidden = false; lb.querySelector('.gal-lb-scroll').scrollTop = 0;
      return;
    }
    if(e.target.id === 'gal-lb-close' || e.target.classList.contains('gal-lb-scroll')){ lbClose(); return; }
  });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && lb && !lb.hidden) lbClose(); });
`;

// ---------- index.html 에 반영 ----------
// index.html 은 CRLF·LF 가 섞여 있어 줄바꿈은 \r?\n 으로 찾는다.
function locate(src, str) {
  const re = new RegExp(str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\n/g, '\\r?\\n'));
  const m = re.exec(src);
  return m ? { at: m.index, len: m[0].length } : null;
}
function replaceBetween(src, start, end, content, insertBefore) {
  const a = locate(src, start), b = locate(src, end);
  if (a && b) return src.slice(0, a.at + a.len) + content + src.slice(b.at);
  const ins = locate(src, insertBefore);
  if (!ins) throw new Error('삽입 위치를 찾지 못했습니다: ' + insertBefore);
  return src.slice(0, ins.at) + start + content + end + '\n' + src.slice(ins.at);
}
html = replaceBetween(html, '<!-- GALLERY:START -->\n', '<!-- GALLERY:END -->', body + '\n', '    </div>\n  </main>');
html = replaceBetween(html, '<!-- GALLERY:LB:START -->\n', '<!-- GALLERY:LB:END -->', lbHtml + '\n', '<script>\n(function(){');

// ---------- 문서별 시안 띠: 각 템플릿 문서의 도입 인용문 바로 아래 ----------
const byDoc = {};
for (const it of items) for (const t of it.tpl) (byDoc[t] = byDoc[t] || []).push(it);
let stripped = 0;
for (const [doc, list] of Object.entries(byDoc)) {
  const strip = `<div class="wide gal-strip" data-gal-strip="${doc}"><div class="gal-strip-head"><b>이 템플릿으로 만든 시안 <span>${list.length}건</span></b><span class="gal-strip-hint">썸네일 = 전체 캡처 · 열기 ↗ = 실제 페이지 · ${capDate} 캡처</span><button type="button" class="xref" data-goto="d103">시안 갤러리 전체 →</button></div><div class="gal-grid gal-grid-s">${list.map(it => card(it, doc)).join('')}</div></div>`;
  const start = `<!-- GALLERY:DOC:${doc}:START -->`, end = `<!-- GALLERY:DOC:${doc}:END -->`;
  const a = html.indexOf(start), b = html.indexOf(end);
  if (a !== -1 && b !== -1) { html = html.slice(0, a + start.length) + strip + html.slice(b); stripped++; continue; }
  const at = html.indexOf(`<article class="doc" id="${doc}"`);
  if (at === -1) { console.warn('문서 없음:', doc); continue; }
  const h2 = html.indexOf('<h2', at);
  let pos = html.indexOf('</blockquote>', at);
  if (pos === -1 || pos > h2) pos = html.indexOf('</h1>', at) + 5; else pos += '</blockquote>'.length;
  html = html.slice(0, pos) + '\n' + start + strip + end + html.slice(pos);
  stripped++;
}
console.log('문서별 시안 띠', stripped, '건:', Object.keys(byDoc).sort().join(' '));

html = replaceBetween(html, '/* GALLERY:CSS:START */', '/* GALLERY:CSS:END */', css, '</style>\n\n<div class="app">');
html = replaceBetween(html, '  /* GALLERY:JS:START */', '  /* GALLERY:JS:END */', js, '  var start = (location.hash || \'\').replace(\'#\',\'\');');

// SECS["d103"]
const secs = groups.map(g => ({ id: `d103-s${g.n}`, num: String(g.n).padStart(2, '0'), txt: `${g.label} (${g.items.length})` }));
secs.push({ id: `d103-s${groups.length + 1}`, num: String(groups.length + 1).padStart(2, '0'), txt: '근거와 이력' });
const secsStr = `"d103": ${JSON.stringify(secs)}`;
if (/"d103": \[[^\]]*\]/.test(html)) html = html.replace(/"d103": \[[^\]]*\]/, secsStr);
else html = html.replace('var SECS = {', 'var SECS = {' + secsStr + ', ');

// 목차 버튼 건수
html = html.replace(/(data-goto="d103"[^>]*>시안 갤러리) \(\d+\)/, `$1 (${total})`);
// 상단 바 버튼 건수
html = html.replace(/(data-goto="d103">시안 갤러리 · 10월 시안 )\d+건/, `$1${total}건`);
// 마스터 인덱스 링크 건수
html = html.replace(/(class="xref" data-goto="d103">시안 갤러리 )\d+건/, `$1${total}건`);

fs.writeFileSync(indexPath, html);
console.log(`d103 시안 갤러리 생성: ${groups.length}그룹 ${total}건 → index.html`);
