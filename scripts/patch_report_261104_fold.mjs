// 11/04 보고 자료: 01 템플릿 · 02 콘텐츠 섹션을 접힌 상태(details)로 바꾼다. 멱등. 사용: node scripts/patch_report_261104_fold.mjs
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const files = ['reports/261102/index.html', 'reports/261102/세스코 1104 보고자료.html'];
const CSS = `details.fold{margin:44px 0 12px;padding-top:18px;border-top:1px solid var(--line)}
details.fold>summary{list-style:none;cursor:pointer;display:flex;align-items:baseline;gap:10px;font-size:20px;font-weight:800}
details.fold>summary::-webkit-details-marker{display:none}
details.fold>summary .num{color:var(--blue);font-size:15px;font-weight:800;min-width:2ch}
details.fold>summary .hint{margin-left:auto;font-size:12px;font-weight:500;color:var(--muted,#6b7280)}
details.fold[open]>summary .hint .c{display:none}details.fold:not([open])>summary .hint .o{display:none}
details.fold h2{display:none}
@media print{details.fold{display:block}details.fold>summary .hint{display:none}details.fold:not([open])>*:not(summary){display:block}}`;
for (const rel of files) {
  const p = path.join(ROOT, rel); let s = fs.readFileSync(p, 'utf8');
  if (s.includes('data-patched-fold')) { console.log('skip', rel); continue; }
  const wrap = (id, nextId) => {
    const re = new RegExp(`(<h2 id="${id}">)([^]*?)(</h2>)([^]*?)(?=<h2 id="${nextId}">)`);
    const m = s.match(re); if (!m) throw new Error('no section ' + id + ' in ' + rel);
    const title = m[2];
    s = s.replace(re, `<details class="fold" id="${id}"><summary>${title}<span class="hint"><span class="c">펼치기 ▾</span><span class="o">접기 ▴</span></span></summary>$4</details>\n`);
  };
  wrap('s1', 's2'); wrap('s2', 's3');
  s = s.replace('</style>', CSS + '\n</style>');
  // 01 안에 남은 버전 꼬리표
  s = s.replace(/ ?\(확정 · v03 윤문\)/g, '').replace(/초안 생성 v1\.7/g, '초안 생성');
  s = s.replace(/<body([^>]*)>/, '<body$1 data-patched-fold="1">');
  fs.writeFileSync(p, s); console.log('ok', rel);
}
