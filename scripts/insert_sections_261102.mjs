// 2026-11-02: cesco-skills 10/21~10/28 변경을 마스터 문서에 반영 (1회용, 다시 돌려도 중복 삽입하지 않음)
//  d59 §5 실물 디자인형·앞뒷면 역할 분리·기타형 3종 (cesco-leaflet/변경요약_실물디자인형_261028.md §4)
//  d95 §6 헤드라인 5안 생성 규칙·공간 POP 보조 문장 (cesco-pop/SKILL.md 2026-10-26 개정)
//  d99 §7 글+디자인 템플릿 (cesco-case-templates v2.1, 2026-10-21)
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const indexPath = path.join(ROOT, 'index.html');
let html = fs.readFileSync(indexPath, 'utf8');
const enc = f => f.split('/').map(encodeURIComponent).join('/');
const a = (f, t) => `<a href="${enc(f)}" target="_blank" rel="noopener">${t}</a>`;
const tw = t => `<div class="wide tablewrap">${t}</div>`;

const SECTIONS = [
  {
    doc: 'd59', id: 'd59-s7', title: '실물 디자인형 · 앞뒷면 역할 분리 · 기타형 3종 (2026-10-28 회의)',
    hist: '2026-11-02: §5 실물 디자인형·앞뒷면 역할 분리·성적서 각주화·기타형 3종 추가(2026-10-28 회의, cesco-skills <code>cesco-leaflet/references/leaflet-real-design-spec.md</code>). 실물 디자인형 시안 4종은 reports/261026, 문서 위 "이 템플릿으로 만든 시안"에서 바로 볼 수 있습니다.',
    body: `<p>제품 리플릿은 담당자가 보고 바로 수정·디자인 전달할 수 있도록 <strong>실물 규격(A4 세로 1장 앞·뒷면, 접지 없음 기본)</strong>으로 냅니다. 앞면은 핵심(고객 말 → 문제 → 원인·근거 → 해결책 → 상품 선언), 뒷면은 세부(특장점 → 스펙·가격 → 근거 각주 → 연계·문의 → 푸터)입니다.</p>
<ul><li><strong>중복 제거</strong>: 같은 문장 12자 이상을 앞뒤에 다시 쓰지 않습니다. 상품 정의문은 앞면 1회, 수치 USP는 1회, 4줄 푸터·©·명함스티커는 뒷면에만 둡니다.</li><li><strong>성적서는 이미지 대신 각주</strong>: 시험성적서 이미지는 넣지 않고 근거 패널(헤드 1줄 + 번호 각주 + 환경 문구 1회)로 씁니다. 각주 번호는 앞면 → 뒷면 등장 순서로 한 체계입니다. 성적이 없는 상품은 "시험완료" 헤드를 만들지 않습니다.</li><li><strong>공란 없음</strong>: 모든 블록에 이미지 자리와 지면 비율을 두고, 면마다 여백을 흡수하는 이미지 자리를 1개 이상 둡니다. 아이콘·누끼 수는 특장점 수와 같게 맞춥니다.</li></ul>
${tw(`<table><thead><tr><th>유형</th><th>언제 쓰나</th><th>뒷면 중심축</th><th>실물 디자인형 시안</th></tr></thead><tbody>
<tr><td><strong>기본형</strong></td><td>아래 셋에 해당하지 않는 보통 제품 전부</td><td>특장점 → 스펙·가격 표 → 근거 각주</td><td>${a('reports/261026/리플릿_실물디자인형_기본형_프레쉬제닉Max_261028.html', '프레쉬제닉 Max')}</td></tr>
<tr><td><strong>기타형 · 가격표형</strong></td><td>한 제품군에 용량·라인업이 여럿이고 고를 것이 "어느 것을 얼마에"일 때</td><td>품목 × 핵심 장점 1줄 → 4단 가격표</td><td>${a('reports/261026/리플릿_실물디자인형_기타형_가격표형_마이랩마스터_261028.html', '마이랩 마스터')}</td></tr>
<tr><td><strong>기타형 · 관리 단계형</strong></td><td>서비스가 붙어 "어떤 순서로 해 주느냐"가 곧 상품일 때. 보통 제품에 STEP을 붙이지 않음</td><td>STEP 01~06 → POINT → 서비스 안내 표</td><td>${a('reports/261026/리플릿_실물디자인형_기타형_관리단계형_에어컨클리닝_261028.html', '에어컨 클리닝')}</td></tr>
<tr><td><strong>기타형 · Q&amp;A 규제 대응형</strong></td><td>살생물제·의약외품처럼 표기 규제가 있어 "써도 되나요 / 어디에 / 얼마나"를 먼저 풀어야 하는 제품</td><td>Q&amp;A 4~6문항 → 구·신 비교표 → 법정 각주 4요소</td><td>${a('reports/261026/리플릿_실물디자인형_기타형_QA형_살균소독제70_261028.html', '살균소독제 70')}</td></tr>
</tbody></table>`)}
<p>기타형도 앞면은 기본형과 같고 뒷면 중심축만 다릅니다. 판정이 애매하면 기본형입니다. 규격·출고 점검표 전문은 cesco-skills <code>cesco-leaflet/references/leaflet-real-design-spec.md</code>에 있습니다.</p>
<blockquote><p><strong>결정 대기 (10/28 변경 요약 §6)</strong>: 판형 기본값(A4 낱장 2P), 앞면 푸터 축소, 각주 번호 체계, 10/26~27 시안의 성적서 자리 소급 여부, 기타형 코드명, Q&amp;A형 신규 문항·부처 표기, 마스터 라인업 6종 구성. 로켓 리플릿(d68~d70) 실물 디자인형 5건은 10/27 샘플 형식이라 성적서 이미지 자리와 앞면 푸터가 남아 있습니다.</p></blockquote>`
  },
  {
    doc: 'd95', id: 'd95-s8', title: '헤드라인 5안 생성 규칙 · 공간 POP 보조 문장 (2026-10-22 신설 · 10-26 개정)',
    hist: '2026-11-02: §6 헤드라인 5안 생성 규칙(라벨 5종·문장 규칙 10)과 공간 POP 보조 문장 규칙 추가. 출처 cesco-skills <code>cesco-pop/SKILL.md</code> 2026-10-26 개정(장식 문장 제거, 보조 문장 뱅크 25). 16종 특장점 10개·기준 USP·5안 샘플은 reports/261022.',
    body: `<p>카피 4단 공식(브랜드 로크업 → 세스코 과학 수식구 → 헤드라인 2행 → 근거 각주)은 그대로 두고, 헤드라인 자리만 제품마다 <strong>가이드 공식 카피(기준선) 1개 + 라벨이 서로 다른 5안</strong>으로 냅니다. 헤드라인에는 기준 USP 1개만 쓰고, 추천 표시는 하지 않고 담당자가 고릅니다. 제품별 기준 USP와 특장점 10개는 ${a('reports/261022/제품POP_제품별특장점10_16종_261022.html', '16종 특장점·기준 USP·5안 샘플')}에 있습니다.</p>
${tw(`<table><thead><tr><th>라벨</th><th>문형</th><th>쓰는 조건</th></tr></thead><tbody>
<tr><td><strong>① 관리 선언형</strong></td><td><code>{관리 대상·장치} / 가동 중입니다</code></td><td>모든 제품</td></tr>
<tr><td><strong>② 관리 범위형</strong></td><td><code>{A}부터 / {B}까지 {관리}</code></td><td>관리 항목이 2개 이상일 때</td></tr>
<tr><td><strong>③ 수치·인증형</strong></td><td><code>{대상} / {수치} {살균·제거·저감·불검출}</code></td><td>시험기관·조건이 있는 수치만, 각주 의무. 수치가 없으면 ③ 기술 근거형. 공간 POP에는 쓰지 않음</td></tr>
<tr><td><strong>④ 상시 작동형</strong></td><td><code>{주기·조건} / {자동 작동}</code></td><td>주기·센서·자동 작동이 코퍼스에 있을 때</td></tr>
<tr><td><strong>⑤ 정기 관리형</strong></td><td><code>세스코 전문가가 / {항목} 정기 {점검·교체·관리}</code></td><td>전문가 정기 관리가 있으면 그것을, 없으면 소속 솔루션명</td></tr>
</tbody></table>`)}
<h3>문장 규칙</h3>
<ol><li><strong>평이한 서술문</strong>: 코퍼스·가이드에 있는 명사와 동사만 씁니다. 비유, 대구, 격언형, 의인화, 과장 수식, "당신" 호명은 헤드라인에 쓰지 않습니다. 10/26 반려 예: "공기가 탁해지면 먼저 / 살균엔진이 가동됩니다", "냄새를 덮지 않고 / 원인부터 없애는 중".</li><li><strong>USP 1개</strong>: 특장점을 2개 이상 나열하지 않습니다. 제품명·펫네임은 로크업·각주 자리에 둡니다.</li><li><strong>시제는 현재진행</strong>: 가동 중입니다 / 관리 중입니다 / 관리합니다.</li><li><strong>주어</strong>: 제품 POP는 제품 또는 무주어 명사구, 공간 POP는 공간("이 화장실은"). "세스코 전문가가"는 ⑤형에서만 씁니다.</li><li><strong>수치</strong>는 ③형에만, 시험기관·조건이 함께 있는 수치만 씁니다. 작동 주기(20분마다)는 효능 수치가 아니라 각주 의무가 없습니다.</li><li><strong>분량</strong>: 2행, 행당 8~13자. 3행이 되면 수식구를 줄입니다.</li><li><strong>어미</strong>: 높임말 또는 명사형. "~다." 평서체, 느낌표, 명령형은 쓰지 않습니다.</li><li><strong>금지 표현</strong>: 안심·안전·완벽·친환경·무독성·인체 무해. 가이드 공식 카피 원문은 원문 유지, 새 안에는 넣지 않습니다.</li><li><strong>브랜드 고정</strong>: 로크업·컬러스킴은 제품 라인대로, 태그라인 "CESCO Science, ON Life", 기술 상표 ™는 첫 등장에만.</li><li><strong>지어내지 않음</strong>: 코퍼스·가이드·세스코몰에 없는 기능·수치·기관을 만들지 않고, 안마다 특장점 번호를 적습니다.</li></ol>
<h3>공간 POP 보조 문장</h3>
<p>공간 POP C형(관리 선언형)과 서비스형 제품 POP의 보조 문장은 보조 문장 뱅크 25문장에서 고릅니다. 헤드라인이 말한 관리 대상과 수식구는 반복하지 않고, 헤드라인이 "무엇을"이면 보조 문장은 "어떤 태도로"를 말합니다. 태도 축은 한 문장에 하나(보이지 않는 곳 · 모르는 사이 · 매번·상시 · 끝까지 · 미리 · 다음 사람)이고, 주어는 세스코 또는 세스코 전문가, 1~2행·행당 20자 안팎, 수치 없음입니다. 적용 예는 ${a('reports/261020/제품POP_공간POP_샘플_화장실_블루제닉_에어퍼퓸100_261020.html', '화장실 공간 POP 샘플')}과 ${a('reports/261022/제품POP_헤드라인·보조문장_샘플16종_261022.html', '헤드라인·보조 문장 샘플 16종')}입니다.</p>`
  },
  {
    doc: 'd99', id: 'd99-s9', title: '글 + 디자인 템플릿 · STEP형과 명인형 (cesco-case-templates v2.1, 2026-10-21)',
    hist: '2026-11-02: §7 글+디자인 템플릿 추가. 출처 cesco-skills <code>cesco-case-templates</code> v2.1(2026-10-21) — 유형 2종 분리(STEP형 · [명인]형), HTML 템플릿, 외항선 S-IPM 사례 2종. 예시 HTML 4건은 reports/261021.',
    body: `<p>영업 우수사례·명인 콘텐츠를 <strong>글과 디자인이 한 번에 나오도록</strong> 묶은 템플릿입니다. 글은 이 가이드로 쓰고, 디자인은 HTML 템플릿을 복사해 텍스트만 바꿉니다.</p>
${tw(`<table><thead><tr><th>유형</th><th>언제 쓰나</th><th>예시</th></tr></thead><tbody>
<tr><td><strong>A. 우수사례 STEP형</strong></td><td>한 건의 계약 서사(거절 → 전환 → 계약 성공)</td><td>${a('reports/261021/우수사례_템플릿예시_step_gov_health_center.html', '보건소(관공서)')} · ${a('reports/261021/우수사례_템플릿예시_step_ship_sipm.html', '외항선 S-IPM')}</td></tr>
<tr><td><strong>B. [명인]형</strong></td><td>한 사람의 평소 원칙 5개</td><td>${a('reports/261021/우수사례_템플릿예시_master_aircurtain.html', '에어커튼')} · ${a('reports/261021/우수사례_템플릿예시_master_ship_sipm.html', '외항선 S-IPM')}</td></tr>
</tbody></table>`)}
<ol><li><strong>유형 판정</strong>: 계약 서사면 STEP형, 평소 원칙이면 명인형입니다.</li><li><strong>글 먼저</strong>: 작성 가이드 Part A(STEP형) 또는 Part B(명인형) 절차대로 원고를 씁니다.</li><li><strong>템플릿 복사</strong>: <code>templates/step.html</code> 또는 <code>templates/master.html</code>을 복사해 <code>{{ }}</code> 자리만 채웁니다.</li><li><strong>구조는 고정</strong>: 섹션 순서·개수·클래스명은 바꾸지 않습니다. 색·글씨·간격은 <code>:root</code> 토큰에서만 바꿉니다.</li><li><strong>확인 필요 표시</strong>: 비어 있는 수치·실명·발화는 <code>{확인 필요: …}</code>로 남기고 게시 전에 지웁니다.</li><li><strong>렌더 확인</strong>: 430px 폭으로 열어 포털 캡처와 대조합니다.</li></ol>
<p>디자인은 모바일 1열 430px, 색은 파랑(라벨·강조) / 노랑(명인 노하우) / 회색(보조) 3계열이고 STEP형 Tip에만 주황을 씁니다. 섹션 사이는 여백으로 구분하고 가로선은 쓰지 않습니다. 기호는 <code>•</code>와 <code>↓</code>만 씁니다(음성 듣기 대응). 템플릿 원본과 작성 가이드 v2.1 전문은 cesco-skills <code>cesco-case-templates/</code>에 있습니다.</p>`
  },
];

let changed = 0;
for (const s of SECTIONS) {
  if (html.includes(`id="${s.id}"`)) { console.log('이미 있음:', s.id); continue; }
  const at = html.indexOf(`<article class="doc" id="${s.doc}"`);
  const end = html.indexOf('</article>', at);
  const seg = html.slice(at, end);
  const m = [...seg.matchAll(/<h2 id="([^"]+)"><span class="secnum">(\d+)<\/span>근거와 이력/g)].pop();
  if (!m) throw new Error(s.doc + ': 근거와 이력 절을 찾지 못했습니다');
  const n = Number(m[2]);
  let newSeg = seg.replace(m[0], `<h2 id="${s.id}"><span class="secnum">${n}</span>${s.title}</h2>\n${s.body}\n<h2 id="${m[1]}"><span class="secnum">${n + 1}</span>근거와 이력`);
  const li = newSeg.lastIndexOf('</ul>');
  newSeg = newSeg.slice(0, li) + `<li>${s.hist}</li>` + newSeg.slice(li);
  html = html.slice(0, at) + newSeg + html.slice(end);
  // SECS
  const re = new RegExp(`"${s.doc}": (\\[[^\\]]*\\])`);
  const list = JSON.parse(html.match(re)[1]);
  const hi = list.findIndex(x => x.id === m[1]);
  list[hi].num = String(n + 1);
  list.splice(hi, 0, { id: s.id, num: String(n), txt: s.title });
  html = html.replace(re, `"${s.doc}": ${JSON.stringify(list)}`);
  changed++;
}
fs.writeFileSync(indexPath, html);
console.log('삽입', changed, '건');
