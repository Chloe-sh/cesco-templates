// wecheck_draft_261028.html(치킨집+산후조리원 합본)을 업종별 단독 페이지 2개로 나눈다.
//   node scripts/split_by_biz.mjs
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = join(dirname(fileURLToPath(import.meta.url)), "..");
const SRC = join(HERE, "wecheck_draft_261028.html");

const BIZ = {
  chicken: { ko: "치킨집", other: "care", out: "wecheck_draft_261028_치킨집.html",
    stamp: "엑셀 ①시트에 치킨집 행이 없어서 치킨집 6장(식품안전 3, 전문클리닝, 에어, 종합방제)은 같은 형식으로 쓴 초안입니다." },
  care: { ko: "산후조리원", other: "chicken", out: "wecheck_draft_261028_산후조리원.html",
    stamp: "산후조리원 5장은 10/23 개선안 1안 원문입니다." },
};

function build(key) {
  const b = BIZ[key], o = BIZ[b.other];
  let html = readFileSync(SRC, "utf8");
  const swap = (from, to) => { if (!html.includes(from)) throw new Error("not found: " + from.slice(0, 40)); html = html.replace(from, to); };

  // 다른 업종 section 통째로 제거
  const sec = new RegExp(`<section class="bizsec" id="${b.other}">[\\s\\S]*?</section>`);
  if (!sec.test(html)) throw new Error("section " + b.other);
  html = html.replace(sec, "");
  // 장소정보 탭(아이콘 그리드) 블록에서 다른 업종 휴대폰 화면만 제거
  html = html.replace(new RegExp(`<figure>(?:(?!</figure>)[\\s\\S])*?data-biz="${b.other}"(?:(?!</figure>)[\\s\\S])*?</figure>`, "g"), "");

  // 제목, 안내문, 목차
  html = html.replaceAll("위쳌 사업장 상세 시안, 치킨집과 산후조리원", "위쳌 사업장 상세 시안, " + b.ko);
  swap("업종마다 <b>상세페이지형</b>을", "<b>상세페이지형</b>을");
  swap(`<a href="#${b.other}">${o.ko}</a>`, "");
  // 확인 필요 표: 체크 스탬프 출처는 이 업종 것만
  swap(BIZ.chicken.stamp + " " + BIZ.care.stamp, b.stamp);
  // 첫 진입 업종
  swap(": 'chicken';", `: '${key}';`);

  if (html.includes(`data-biz="${b.other}"`)) throw new Error("leftover " + b.other);
  writeFileSync(join(HERE, b.out), html);
  console.log("wrote", b.out, html.length);
}

Object.keys(BIZ).forEach(build);
