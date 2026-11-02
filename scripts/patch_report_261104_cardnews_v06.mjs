// 11/04 보고 자료·시안 갤러리: 카드뉴스 매트리스 케어 편·배수구 편의 유형별 링크를 v06 파일(reports/261102/매트리스케어_4종_v06_윤문검토.html · 배수구_4종_v06_윤문검토.html)의 탭 앵커로 바꾼다.
// 유형 이름(제목)은 그대로 둔다. 1회용.
import fs from 'node:fs';
import path from 'node:path';
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1')), '..');
const MAP = [ // [옛 파일, 옛 해시, 새 파일, 새 해시]
  ['카드뉴스_가을매트리스케어_경험질문형_v03_윤문검토_dh_261102.html', 'main', '매트리스케어_4종_v06_윤문검토.html', 'v05'],
  ['카드뉴스_가을매트리스케어_스토리구성3안_v03_윤문검토_dh_261102.html', 'g1', '매트리스케어_4종_v06_윤문검토.html', 'v06'],
  ['카드뉴스_가을매트리스케어_스토리구성3안_v03_윤문검토_dh_261102.html', 'g2', '매트리스케어_4종_v06_윤문검토.html', 'v07'],
  ['카드뉴스_가을매트리스케어_스토리구성3안_v03_윤문검토_dh_261102.html', 'g3', '매트리스케어_4종_v06_윤문검토.html', 'v08'],
  ['카드뉴스_배수구_구성안_v03_윤문검토_261102.html', 'v1', '배수구_4종_v06_윤문검토.html', 'v01'],
  ['카드뉴스_배수구_구성안_v03_윤문검토_261102.html', 'v1b', '배수구_4종_v06_윤문검토.html', 'v02'],
  ['카드뉴스_배수구_구성안_v03_윤문검토_261102.html', 'v2', '배수구_4종_v06_윤문검토.html', 'v03'],
  ['카드뉴스_배수구_구성안_v03_윤문검토_261102.html', 'v3', '배수구_4종_v06_윤문검토.html', 'v04'],
];
// 보고 자료 4개: href="옛파일#해시" → href="새파일#새해시"
for (const f of ['index.html', '세스코 1104 보고자료.html', 'summary.html', '세스코 1104 보고 요약.html']) {
  const p = path.join(ROOT, 'reports/261102', f);
  let h = fs.readFileSync(p, 'utf8'); let n = 0;
  for (const [of, oh, nf, nh] of MAP) { const a = `href="${of}#${oh}"`, b = `href="${nf}#${nh}"`; const c = h.split(a).length - 1; n += c; h = h.split(a).join(b); }
  h = h.replace('지금 기준이 되는 파일 하나와 그 앞 판본을 적었습니다', '지금 기준이 되는 파일 하나를 적었습니다');
  fs.writeFileSync(p, h); console.log(f, '링크', n, '개 교체');
}
// 갤러리 manifest: 카드뉴스 g74~g80 의 파일·해시와 버전 목록 첫 항목, ver 꼬리표
const mp = path.join(ROOT, 'captures/261102/manifest.json');
const m = JSON.parse(fs.readFileSync(mp, 'utf8'));
const re = (file, hash) => { for (const [of, oh, nf, nh] of MAP) if (file === 'reports/261102/' + of && (hash || '') === oh) return ['reports/261102/' + nf, nh]; return null; };
const changed = [];
for (const it of m.items) {
  if (it.group !== 'cardnews') continue;
  const r = re(it.file, it.hash); if (r) { it.file = r[0]; it.hash = r[1]; changed.push(it.id); }
  if (it.ver) it.ver = it.ver.replace(/^v03 윤문 최종( · )?/, '').trim() || undefined;
  if (!it.ver) delete it.ver;
  for (const v of it.versions || []) { const q = re(v.file, v.hash); if (q) { v.file = q[0]; v.hash = q[1]; v.label = v.label.replace(/ · v03 윤문검토( \(확정\))?$/, ''); v.date = '2026-11-02'; } }
}
fs.writeFileSync(mp, JSON.stringify(m, null, 2) + '\n');
console.log('manifest 갱신:', changed.join(' '));
