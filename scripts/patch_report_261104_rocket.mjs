// 11/04 보고 자료: 로켓 리플릿 6종의 최신판을 코드 초안 v2에서 실물 디자인형(10/27·11/02)으로 올린다. 1회용, 재실행해도 중복 적용되지 않는다.
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const R = p => path.join(ROOT, 'reports/261102', p);

function patch(file, edits) {
  let h = fs.readFileSync(file, 'utf8');
  if (h.includes('data-patched="261104-rocket"')) { console.log('이미 적용됨:', path.basename(file)); return; }
  let miss = 0;
  for (const [a, b] of edits) {
    if (a instanceof RegExp ? !a.test(h) : !h.includes(a)) { console.log('MISSING:', String(a).slice(0, 80)); miss++; continue; }
    h = h.replace(a, b);
  }
  if (miss) { console.log('적용 안 함(누락', miss, '):', path.basename(file)); process.exitCode = 1; return; }
  h = h.replace('<body', '<body data-patched="261104-rocket"');
  fs.writeFileSync(file, h);
  console.log('적용:', path.basename(file));
}

const L = (href, label) => `<a href="${href}" target="_blank">${label}</a>`;
const D = {
  indA: '../261026/리플릿_실물디자인형_로켓_산업체_식품공장_261102.html',
  indB: '../261026/리플릿_실물디자인형_로켓_산업체_식품공장_프레쉬제닉Max_261102.html',
  smlA: '../261026/리플릿_실물디자인형_프레쉬제닉Max·음식점로켓_261027.html#r',
  smlB: '../261026/리플릿_실물디자인형_로켓_소규모_음식점_프레쉬제닉Max_261102.html',
  homA: '../261026/리플릿_실물디자인형_로켓_가정집_센스미_261102.html',
  homB: '../261026/리플릿_실물디자인형_로켓_가정집_프레쉬제닉Max_261102.html',
};
const V = {
  indA: '../261026/리플릿_로켓_산업체_식품공장_시안_v2_261026.html',
  indB: '../261026/리플릿_로켓_산업체_식품공장_프레쉬제닉Max_시안_v2_261027.html',
  smlA: '../261026/리플릿_로켓_소규모_음식점_마스터식기세척기_시안_v2_261026.html',
  smlB: '../261026/리플릿_로켓_소규모_음식점_프레쉬제닉Max_시안_v2_261027.html',
  homA: '../261026/리플릿_로켓_가정집_센스미_시안_v2_261026.html',
  homB: '../261026/리플릿_로켓_가정집_프레쉬제닉Max_시안_v2_261027.html',
};

// ---------- 보고자료 (index.html + 동일 사본) ----------
const rowRe = name => new RegExp(`<tr><td>${name}</td>[\\s\\S]*?</tr>`);
const reportEdits = [
  ['<tr class="grp"><td colspan="4">리플릿 — 로켓 (원고 확정본은 10/26·27 v2 · 실물 디자인형은 음식점 식기세척기 1건만 완성)</td></tr>',
   '<tr class="grp"><td colspan="4">리플릿 — 로켓 (10/28 실물 디자인형 규격 · 산업체·소규모·가정집 6종 전부 디자인형 완성)</td></tr>'],
  [rowRe('산업체'),
   `<tr><td>산업체</td><td><div class="v">${L(D.indA, '식품공장 × 통합해충방제 · 실물 디자인형')}${L(D.indB, '식품공장 × 프레쉬제닉 Max · 실물 디자인형')}<span class="d">11/02 · A4 앞·뒷면 · 원고는 10/28 보고본(v2) 그대로</span></div></td><td class="hist">${L(V.indA, '10/26 코드 초안 v2')} · ${L(V.indB, '10/27 코드 초안 v2')}<span class="arr">←</span><s>10/22 v1</s><span class="arr">←</span>${L('../261020/슬림온_리플릿_타입별_SiHAW_261019.html', '10/19 슬림온 5종')}(10/21 보고). 10/28 규격(성적서 각주화·앞면 푸터 축소) 적용.</td><td class="c"><span class="st todo">피드백 대기</span></td></tr>`],
  [rowRe('소규모 사장님'),
   `<tr><td>소규모 사장님</td><td><div class="v">${L(D.smlA, '음식점 × 마스터 식기세척기 · 실물 디자인형')}${L(D.smlB, '음식점 × 프레쉬제닉 Max · 실물 디자인형')}<span class="d">10/27 · 11/02 · 원고는 10/28 보고본(v2) 그대로</span></div></td><td class="hist">${L(V.smlA, '10/26 코드 초안 v2')} · ${L(V.smlB, '10/27 코드 초안 v2')}<span class="arr">←</span><s>10/22 v1</s>. 확인 필요: 식기세척기 세척력·건조 수치, 시험성적서.</td><td class="c"><span class="st todo">피드백 대기</span></td></tr>`],
  [rowRe('가정집'),
   `<tr><td>가정집</td><td><div class="v">${L(D.homA, '가정집 × 센스미 · 실물 디자인형')}${L(D.homB, '가정집 × 프레쉬제닉 Max · 실물 디자인형')}<span class="d">11/02 · 원고는 10/28 보고본(v2) 그대로</span></div></td><td class="hist">${L(V.homA, '10/26 코드 초안 v2')} · ${L(V.homB, '10/27 코드 초안 v2')}<span class="arr">←</span><s>10/22 v1</s>. 확인 필요: 프레쉬제닉 Max 가정집 적용 가능 여부와 가정용 요금.</td><td class="c"><span class="st todo">피드백 대기</span></td></tr>`],
];
for (const f of ['index.html', '세스코 1104 보고자료.html']) patch(R(f), reportEdits);

// ---------- 요약 (summary.html + 동일 사본) ----------
const chip = (href, type, label) => `<a class="chip" href="${href}" target="_blank"><span class="type">${type}</span>${label}</a>`;
const rocketChips = chip(D.indA, '산업체', '식품공장 × 통합해충방제') + chip(D.indB, '산업체', '식품공장 × 프레쉬제닉 Max')
  + chip(D.smlA, '소규모', '음식점 × 식기세척기') + chip(D.smlB, '소규모', '음식점 × 프레쉬제닉 Max')
  + chip(D.homA, '가정집', '센스미') + chip(D.homB, '가정집', '프레쉬제닉 Max');
const summaryEdits = [
  ['로켓 리플릿의 디자인형 적용은 진행 중입니다.', '로켓 리플릿 6종도 같은 실물 디자인형으로 완성했습니다.'],
  ['<tr><td>제품 리플릿<br><span class="small" style="font-weight:400">실물 디자인형</span></td>',
   '<tr><td>제품·로켓 리플릿<br><span class="small" style="font-weight:400">실물 디자인형</span></td>'],
  ['기본형 1종과 기타형 3종(관리 단계형·가격표형·Q&amp;A형)을 디자인 전달이 가능한 수준으로 제작했습니다.</td>',
   '기본형 1종과 기타형 3종(관리 단계형·가격표형·Q&amp;A형)을 디자인 전달이 가능한 수준으로 제작했습니다. 로켓 리플릿도 산업체·소규모·가정집 3유형 × 2종(6건)을 같은 규격으로 디자인형을 입혔습니다. 원고는 10/28 보고본(v2) 그대로입니다.</td>'],
  [/<a class="chip" href="\.\.\/261026\/리플릿_실물디자인형_기타형_QA형_살균소독제70_261028\.html" target="_blank"><span class="type">Q&amp;A형<\/span>살균소독제 70<\/a>/,
   m => m + rocketChips],
  [rowRe('로켓 리플릿'), ''],
];
for (const f of ['summary.html', '세스코 1104 보고 요약.html']) patch(R(f), summaryEdits);
