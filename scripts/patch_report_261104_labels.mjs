// 11/04 보고 자료: 제작물 표에서 버전·윤문 꼬리표(v03 윤문 최종, v4 수정본 등)를 떼고 유형 이름만 남긴다.
// 카드뉴스의 템플릿 행·에어컨 클리닝 편·11월 4편 행은 뺀다. 1회용, 재실행해도 중복 적용되지 않는다.
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const R = p => path.join(ROOT, 'reports/261102', p);

function patch(file, edits, after) {
  let h = fs.readFileSync(file, 'utf8');
  if (h.includes('data-patched2="261104-labels"')) { console.log('이미 적용됨:', path.basename(file)); return; }
  let miss = 0;
  for (const [a, b, all] of edits) {
    if (a instanceof RegExp ? !a.test(h) : !h.includes(a)) { console.log('MISSING:', String(a).slice(0, 90)); miss++; continue; }
    h = all ? h.split(a).join(b) : h.replace(a, b);
  }
  if (miss) { console.log('적용 안 함(누락', miss, '):', path.basename(file)); process.exitCode = 1; return; }
  if (after) h = after(h);
  h = h.replace('<body', '<body data-patched2="261104-labels"');
  fs.writeFileSync(file, h);
  console.log('적용:', path.basename(file));
}
const row = start => new RegExp(start.replace(/[.*+?^${}()|[\]\\\/]/g, '\\$&') + '[\\s\\S]*?</tr>\\n?');

const reportEdits = [
  // 행 삭제
  [row('<tr><td>템플릿</td><td><div class="v"><a href="../../index.html#d102"'), ''],
  [row('<tr><td>에어컨 클리닝 편</td>'), ''],
  [row('<tr><td>11월 카드뉴스 4편</td>'), ''],
  // 꼬리표 제거
  ['>경험 질문형 · v03 윤문 최종</a>', '>경험 질문형</a>'],
  ['<span class="d">11/02 v03 문장 검수·윤문 · 표지 후보 4 채택</span>', '<span class="d">11/02 · 표지 후보 4 채택</span>'],
  ['<span class="d">11/02 v03 문장 검수·윤문</span>', '<span class="d">11/02</span>', true],
  ['>오해 교정형 · 파일럿</a>', '>오해 교정형</a>'],
  ['>카케어 16P · v4 수정본</a>', '>카케어</a>'],
  ['>가정집 · 외식업장 · 유통시설 v6 (기존 페이지 중심)</a>', '>가정집 · 외식업장 · 유통시설 통합안</a>'],
  ['>최종 채택본 · 기본 템플릿 + 사장님 선택·수정</a>', '>기본 템플릿 + 사장님 선택·수정</a>'],
  ['<span class="d">10/30 수정 7건 반영 · 11/02 문장 윤문</span>', '<span class="d">10/30 · 11/02</span>'],
  ['>작성 가이드 v2 + 글·디자인 템플릿 (d99)</a>', '>작성 가이드 + 글·디자인 템플릿 (d99)</a>'],
  ['원고는 10/28 보고본(v2) 그대로</span>', '원고는 10/28 보고본 그대로</span>', true],
];
// 상단 요약 수치: 뺀 행 3개(포맷 20→17), 뺀 링크 3개(템플릿 2 + 에어컨 클리닝 편 1, 파일 31→28).
function recount(h) {
  return h.replace('<span><b>제작물 최신판</b> 포맷 20 · 파일 31</span>', '<span><b>제작물 최신판</b> 포맷 17 · 파일 28</span>');
}
for (const f of ['index.html', '세스코 1104 보고자료.html']) patch(R(f), reportEdits, recount);

const summaryEdits = [
  ['>경험 질문형 (확정 · v03 윤문)</a>', '>경험 질문형</a>'],
  [/<a class="chip" href="\.\.\/\.\.\/index\.html#d102" target="_blank"><span class="type">템플릿<\/span>A\/B\/C 초안 생성 v1\.7<\/a>/, ''],
];
for (const f of ['summary.html', '세스코 1104 보고 요약.html']) patch(R(f), summaryEdits);
