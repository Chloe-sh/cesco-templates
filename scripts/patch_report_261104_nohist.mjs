// 11/04 보고 자료: 제작물 표의 "판 이력" 열에서 이전 판 링크·취소선·화살표 사슬을 지우고 비고 문장만 남긴다. 1회용, 재실행해도 중복 적용되지 않는다.
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const R = p => path.join(ROOT, 'reports/261102', p);

// 태그 밖 텍스트 기준으로 첫 문장 끝('.' 뒤에 공백·태그·끝)을 찾는다. 첫 문장에 링크·취소선·화살표가 있을 때만 그 문장을 떼어 낸다.
function stripChain(cell) {
  let inTag = false, i = 0;
  for (; i < cell.length; i++) {
    const c = cell[i];
    if (c === '<') inTag = true;
    else if (c === '>') inTag = false;
    else if (!inTag && c === '.' && (i + 1 >= cell.length || /[\s<]/.test(cell[i + 1]))) break;
  }
  if (i >= cell.length) return cell; // 문장 끝이 없으면 그대로
  const head = cell.slice(0, i + 1);
  if (!/<a |<s>|class="arr"/.test(head)) return cell;
  return cell.slice(i + 1).replace(/^\s+/, '');
}

function patch(file) {
  let h = fs.readFileSync(file, 'utf8');
  if (h.includes('data-patched3="261104-nohist"')) { console.log('이미 적용됨:', path.basename(file)); return; }
  let n = 0, changed = 0;
  h = h.replace(/<td class="hist">([\s\S]*?)<\/td>/g, (m, cell) => {
    n++;
    const out = stripChain(cell);
    if (out !== cell) changed++;
    return `<td class="hist">${out}</td>`;
  });
  h = h.split('<th>판 이력 · 비고</th>').join('<th>비고</th>');
  h = h.replace(/\s*<b>판 이력<\/b>은[^.]*\.\s*/, ' ');
  h = h.replace(/\s*판 이력은[^.]*\.\s*/, ' ');
  h = h.replace('<body', '<body data-patched3="261104-nohist"');
  fs.writeFileSync(file, h);
  console.log('적용:', path.basename(file), '— 이력 셀', n, '개 중', changed, '개 정리');
}
for (const f of ['index.html', '세스코 1104 보고자료.html']) patch(R(f));
