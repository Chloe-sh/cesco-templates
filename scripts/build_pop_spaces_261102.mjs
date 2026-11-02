// 공간별 공간 POP 카피 초안 페이지를 만든다. 틀·CSS는 10/20 화장실 샘플과 같다. 사용: node scripts/build_pop_spaces_261102.mjs
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const sample = fs.readFileSync(path.join(ROOT, 'reports/261020/제품POP_공간POP_샘플_화장실_블루제닉_에어퍼퓸100_261020.html'), 'utf8');
const css = sample.match(/<style>[\s\S]*?<\/style>/)[0];
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');

// 공간 8곳. 헤드라인은 가이드 p.16 서비스형(C형)과 실물 B형(리플릿 334_1)의 문장 틀만 쓰고, 관리 대상은 설치 제품의 가이드 v.4 공식 카피·상세페이지 코퍼스 표현으로 채웠다.
const SPACES = [
  { key: 'restroom', name: '사업장 화장실', where: '출입문 안쪽 또는 세면대 거울 옆(시선 높이)', line: 'Viruscare 마젠타 또는 Science, ON Life 블루',
    a: '손 위생부터 변기, 공기까지', subj: '이 화장실은', b: '손과 변기, 공기까지',
    sup: ['손을 씻고 나서는 당신처럼,<br>세스코는 다음 사람이 쓸 공간을 미리 살핍니다.', '세스코 과학으로 24시간 상시 관리하는 구역입니다.'],
    supAxis: ['㉥ 다음 사람 (뱅크 21 · 10/20 A안)', '㉢ 매번·상시 (뱅크 11)'],
    prod: '핸드제닉 손세정기 · 새니제닉 손소독기 · 프레쉬제닉 변기세정기 · 에어퍼퓸', src: '가이드 p.2·p.3·p.4·p.13, 상세페이지 "화장실 360˚입체살균 시스템" · 10/20 샘플 A안과 같은 문안' },
  { key: 'lobby', name: '출입구 · 로비', where: '출입문 안쪽 벽면, 안내 데스크 옆', line: 'Science, ON Life 블루',
    a: '외부 공기부터 손 소독까지', subj: '이 출입구는', b: '외부 공기와 손 소독까지',
    sup: ['이용하는 분의 동선을 따라 미리 관리합니다.', '사람이 없는 시간에도 세스코가 관리합니다.'],
    supAxis: ['㉤ 미리 (뱅크 16)', '㉡ 모르는 사이 (뱅크 7)'],
    prod: '블루쉴드 에어커튼 · 새니제닉 손소독기 · 트루살균 공기청정기 판테온', src: '상세페이지 23 블루쉴드 에어커튼(외부 공기 유입 차단), 가이드 p.3·p.8' },
  { key: 'office', name: '사무실 · 회의실', where: '출입문 안쪽 또는 정수기 옆 벽면', line: 'Science, ON Life 블루',
    a: '실내 공기부터 식수까지', subj: '이 사무실은', b: '공기와 식수, 향기까지',
    sup: ['근무하시는 동안에도 관리는 계속됩니다.', '세스코 전문가가 정기적으로 방문해 점검합니다.'],
    supAxis: ['㉡ 모르는 사이 (뱅크 5 · "이용" → "근무")', '㉤ 미리 (뱅크 17)'],
    prod: '트루살균 공기청정기 판테온(또는 듀얼케어) · 통합 정수기 · 에어퍼퓸', src: '가이드 p.8·p.10·p.13·p.14, 상세페이지 케어서비스(정기 점검·필터 교체)' },
  { key: 'class', name: '어린이시설 교실', where: '교실 출입문 안쪽, 손세정기 위 벽면', line: 'Viruscare 마젠타',
    a: '공기 살균부터 손 위생까지', subj: '이 교실은', b: '공기와 손, 식수까지',
    sup: ['문제가 보이기 전에 세스코가 먼저 점검합니다.', '위생이 생명인 곳과 같은 기준으로 관리합니다.'],
    supAxis: ['㉤ 미리 (뱅크 15)', '㉥ 다음 사람 (뱅크 23)'],
    prod: 'UV파워공기살균기 · 핸드제닉 손세정기 · 새니제닉 손소독기 · 통합 정수기', src: '카드뉴스 836(어린이시설 공간 POP 실물) · 가이드 p.2·p.3·p.6·p.14' },
  { key: 'nursery', name: '산후조리원 신생아실', where: '신생아실 출입문 밖(보호자 시선 높이)', line: 'Viruscare 마젠타',
    a: '공기 살균부터 손 소독까지', subj: '이 신생아실은', b: '공기 살균과 손 소독까지',
    sup: ['눈에 띄지 않는 자리도 같은 기준으로 관리합니다.', '점검이 끝날 때까지 세스코가 확인합니다.'],
    supAxis: ['㉠ 보이지 않는 곳 (뱅크 3)', '㉣ 끝까지 (뱅크 13)'],
    prod: 'UV파워공기살균기 · 핸드제닉 손세정기 · 새니제닉 손소독기', src: '리플릿 333 산후조리원 로켓 · 가이드 p.2·p.3·p.6' },
  { key: 'room', name: '산후조리원 · 숙박 객실', where: '객실 출입문 안쪽 또는 욕실 거울 옆', line: 'Bodycare 오렌지 또는 Science, ON Life 블루',
    a: '공기부터 물, 비데까지', subj: '이 객실은', b: '공기와 물, 비데까지',
    sup: ['다음에 사용하실 분을 위해 사용 후마다 다시 관리합니다.', '세스코 전문가가 작동 상태를 확인하고 마무리합니다.'],
    supAxis: ['㉥ 다음 사람 (뱅크 18)', '㉣ 끝까지 (뱅크 12)'],
    prod: '유어핏 비데 · 통합 정수기 · 트루살균 공기청정기 판테온 · 에어퍼퓸', src: '가이드 p.8·p.13·p.14·p.15, 리플릿(비데) "매번 자동으로 전해수 살균"' },
  { key: 'kitchen', name: '음식점 주방 · 조리실', where: '조리실 입구 손세정기 위 벽면(직원 동선)', line: 'Science, ON Life 블루',
    a: '손 세정부터 건조까지', subj: '이 주방은', b: '손 세정과 건조, 물까지',
    sup: ['하루에 몇 번을 사용해도 관리 기준은 같습니다.', '눈에 보이지 않는 곳까지 세스코가 관리합니다.'],
    supAxis: ['㉢ 매번·상시 (뱅크 10)', '㉠ 보이지 않는 곳 (뱅크 1)'],
    prod: '핸드제닉 손세정기 · 핸드드라이어 · 통합 정수기', src: '가이드 p.2·p.14·p.16(핸드드라이어 "세척부터 세균까지")' },
  { key: 'hall', name: '음식점 홀 · 객석', where: '출입문 안쪽 또는 카운터 옆(손님 시선 높이)', line: 'Science, ON Life 블루',
    a: '공기부터 향기, 식수까지', subj: '이 매장은', b: '공기와 향기, 식수까지',
    sup: ['앞 손님이 떠난 뒤에도 같은 상태로 관리합니다.', '세스코 과학으로 24시간 상시 관리하는 구역입니다.'],
    supAxis: ['㉥ 다음 사람 (뱅크 19)', '㉢ 매번·상시 (뱅크 11)'],
    prod: '트루살균 공기청정기 판테온 · 에어퍼퓸 · 통합 정수기', src: '가이드 p.8·p.13·p.14, 상세페이지 배너 "24시간 상시 관리하는 구역"' },
];

const cardC = s => `
  <div class="popwrap">
    <div class="poplabel"><b>A안 · C형 관리 선언형</b> — 85 × 56 mm · ${esc(s.line)} · ${esc(s.where)}</div>
    <div class="pop blue s85 cut">
      <div>
        <div class="lockup"><span class="brand"><span class="c">CESCO</span><span class="sub">Science, ON Life</span></span><span class="icon">C</span></div>
        <div class="sci">세스코 사이언스케어 서비스</div>
        <div class="head">${esc(s.subj)} <em>${esc(s.a)}</em><br>세스코 과학으로 관리합니다.</div>
        <div class="sup">${s.sup[0]}</div>
      </div>
      <div class="note">* ${esc(s.prod)} 설치 공간</div>
      <span class="rule">85×56</span>
    </div>
    <p class="pos">보조 문장 1안 ${esc(s.supAxis[0])}. 2안: "${esc(s.sup[1])}" ${esc(s.supAxis[1])}.</p>
  </div>`;
const cardB = s => `
  <div class="popwrap">
    <div class="poplabel"><b>B안 · B형 관리 진행 고지형(압축)</b> — 56 × 50 mm · 제품 옆 작은 자리</div>
    <div class="pop blue s56 cut">
      <div>
        <div class="lockup"><span class="brand"><span class="c">CESCO</span><span class="sub">Science, ON Life</span></span><span class="icon">C</span></div>
        <div class="head"><em>${esc(s.b)}</em><br>청결하고 위생적인<br>관리 진행</div>
      </div>
      <div class="foot"><span class="tag2">세스코 과학으로 관리합니다</span></div>
      <span class="rule">56×50</span>
    </div>
    <p class="pos">실물 B형(리플릿 334_1)의 위해요소 자리에 관리 대상을 넣은 압축형입니다.</p>
  </div>`;

let sections = '';
SPACES.forEach((s, i) => {
  sections += `
<!-- ───────── ${i + 1} ───────── -->
<h2 id="${s.key}"><span class="num">${String(i + 1).padStart(2, '0')}</span>${esc(s.name)}</h2>
<p class="small">설치 제품(각주 기준): ${esc(s.prod)} · 근거: ${esc(s.src)}</p>
<div class="board">${cardC(s)}${cardB(s)}</div>`;
});

const rows = SPACES.map(s => `<tr><td><a href="#${s.key}">${esc(s.name)}</a></td><td>${esc(s.subj)} <b>${esc(s.a)}</b> / 세스코 과학으로 관리합니다.</td><td>${esc(s.sup[0].replace(/<br>/g, ' '))}<br><span class="small">${esc(s.sup[1])}</span></td><td class="small">${esc(s.prod)}</td></tr>`).join('\n');

const html = `<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>공간별 공간 POP 카피 초안 · 8개 공간</title>
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
${css}
</head>
<body>
<div class="wrap">
<header class="top">
  <div class="kicker">세스코 제품 POP 가이드 v.4 준용 · 공간 부착용 POP</div>
  <h1>공간별 공간 POP 카피 초안 — 8개 공간 × 2안</h1>
  <div class="meta"><span><b>작성</b> 2026-11-02</span><span><b>템플릿</b> 마스터 d45 공간 부착용 POP · d95 제품 부착형</span><span><b>근거</b> 표시홍보물 비주얼 가이드 v.4(2026.06) p.16 서비스형 문장 틀 · 공간 POP 보조 문장 뱅크(cesco-pop) · 공통 브랜드 언어 원칙 §8</span></div>
</header>

<p class="lead">제품 POP 가이드 v.4의 공통 규격(소재 · 형태 · 사이즈 · 컬러스킴 · 각주 의무)과 p.16 서비스형 POP의 문장 틀을 그대로 두고, 공간마다 관리 대상만 바꿔 넣은 초안입니다. 모든 안은 주어가 공간이고 시제는 현재진행이며, 수치 · 각주 · 금지 표현(안심 · 안전 · 완벽 · 친환경 · 무독성)이 없습니다. 보조 문장은 뱅크 25문장에서 헤드라인의 관리 대상 명사와 겹치지 않는 것을 태도 축이 다르게 2개씩 골랐습니다.</p>

<div class="box amber"><b>확인이 필요한 것</b> ① 공간 POP 실물은 아직 미확인이라 사이즈는 가이드 v.4 값(85 × 56 / 56 × 50 mm)을 준용했습니다. ② 각주의 설치 제품 구성은 공간별 대표 조합이며 계약 사업장마다 실제 설치 제품으로 바꿔 넣습니다. ③ 출입구 · 로비의 에어커튼(블루쉴드)은 가이드 v.4 16종에 없는 제품이라 상세페이지 코퍼스 표현을 썼습니다. ④ 컬러스킴은 한 공간에 여러 라인 제품이 섞일 때 Science, ON Life 블루를 기본으로 두었습니다(10/20 샘플과 같은 기준, 결정 필요).</div>

<h2><span class="num">00</span>한눈에 보기</h2>
<table>
<thead><tr><th>공간</th><th>헤드라인 (A안 · C형)</th><th>보조 문장 1안 / 2안</th><th>설치 제품(각주)</th></tr></thead>
<tbody>
${rows}
</tbody>
</table>
${sections}

<h2><span class="num">09</span>검수 — d45 §0 · d95 §4 · 보조 문장 뱅크 §0</h2>
<table>
<thead><tr><th>점검</th><th>결과</th><th>메모</th></tr></thead>
<tbody>
<tr><td>파는 말 · 연락처 · QR 없음</td><td><span class="tag g">통과</span></td><td>POP는 CTA가 없는 채널</td></tr>
<tr><td>해충 · 바이러스 위협 소재 없음</td><td><span class="tag g">통과</span></td><td>관리 대상(공기 · 손 · 물 · 변기 · 향기)만 표기</td></tr>
<tr><td>수치 · 각주</td><td><span class="tag g">통과</span></td><td>16안 모두 수치 없음 → 효능 각주 불필요. 각주 자리는 설치 제품 목록</td></tr>
<tr><td>금지 표현 (§8 ⑭⑮)</td><td><span class="tag g">통과</span></td><td>안심 · 안전 · 완벽 · 친환경 · 무독성 없음</td></tr>
<tr><td>장식 어휘 (당신 · 집요 · 움직입니다 · 켜집니다 · 드나드는 · 숨 쉬는)</td><td><span class="tag g">통과</span></td><td>관리 대상은 수식어 없는 명사만(외부 공기 · 실내 공기 · 식수 · 손 소독). "당신처럼"은 가이드 p.16 실물 문형을 옮긴 화장실 A안에만 사용</td></tr>
<tr><td>보조 문장 반복 금지 · 태도 축</td><td><span class="tag g">통과</span></td><td>헤드라인의 관리 대상 명사를 보조 문장에 다시 쓰지 않음. 공간마다 축이 다른 2안</td></tr>
<tr><td>주어 = 공간 · 시제 = 현재진행</td><td><span class="tag g">통과</span></td><td>"이 교실은" "이 매장은" / 관리합니다 · 관리 진행</td></tr>
<tr><td>헤드라인 1행 길이</td><td><span class="tag g">통과</span></td><td>C형 1행 8공간 모두 공백 제외 13자 이내(최장 화장실 · 출입구 12자)</td></tr>
<tr><td>상품명 표기</td><td><span class="tag a">확인</span></td><td>블루제닉 신명칭 ↔ 제닉 시리즈 공식 카피 적용 여부(10/20 과제와 동일)</td></tr>
</tbody>
</table>

<h2><span class="num">10</span>결정 요청</h2>
<ul>
<li><b>기본 안</b> 공간마다 A안(C형)을 기본으로 두고, B안은 제품 옆 작은 자리용 보조로 제안합니다.</li>
<li><b>보조 문장</b> 공간마다 1안 · 2안 중 하나를 고르거나, 전 공간 공통 문장 하나로 통일할지 결정이 필요합니다.</li>
<li><b>컬러스킴</b> 복합 공간은 Science, ON Life 블루로 통일할지, 주력 제품 라인(교실 · 신생아실은 Viruscare 마젠타)을 따를지.</li>
<li><b>사이즈</b> 공간 POP 전용 사이즈가 정해지면 d45 §4 표에 고정합니다.</li>
</ul>
<p class="small">근거 — 마스터 템플릿 d45(공간 부착용 POP, 가이드 v.4 준용) · d95(제품 부착형 POP 가이드 v.4 전사) · cesco-pop 스킬 「공간 POP 보조 문장 규칙」 · 보조 문장 뱅크 25문장(출처 원문 병기) · 공통 브랜드 언어 원칙 d01 §8 ⑭⑮ · 10/20 화장실 공간 POP 샘플.</p>
</div>
</body>
</html>`;
const out = path.join(ROOT, 'reports/261102/제품POP_공간별_카피초안_8공간_261102.html');
fs.writeFileSync(out, html);
console.log('생성:', out, html.length, 'chars');
