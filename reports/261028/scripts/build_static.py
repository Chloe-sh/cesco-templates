# -*- coding: utf-8 -*-
"""위쳌 사업장 상세 최종 시안 (10/30 수정 반영): 치킨집·산후조리원.
상세페이지형 + 장소정보 탭을 앞에 크게, 관리 구조·명칭 후보, 그 아래 사장님 선택 화면·수치형·인터뷰형 비교.
실행: python3 reports/261028/scripts/build_static.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B, build_tpl as T

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = 'wecheck_draft_261028.html'
TYPES = [('A','수치형','세스코 실측 계기판 아래에 사장님 문장이 "이 집은 ~"으로 붙습니다'),('B','인터뷰형','고른 항목이 질문이 되고 사장님 문장이 답이 됩니다')]

CSS = r"""
.lead{max-width:1320px;margin:0 auto;padding:20px 20px 0}
.lead .desc h1{font-size:18px}
.lead .desc p{color:#3E444A;font-size:13px;line-height:1.65}
.lead .desc p+p{margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chips span{font-size:11.5px;font-weight:800;color:var(--wc);background:var(--wc-bg);border-radius:999px;padding:4px 10px}
.chips span.g{color:#0E8F4A;background:#E8F6EE}
.chips span.y{color:#9A6B12;background:#FBF7EC}
.toc{display:flex;flex-wrap:wrap;gap:4px 14px;margin-top:10px;font-size:12px}
.toc a{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid #C9D0D8}
.blk{max-width:1320px;margin:0 auto;padding:0 20px 18px}
.blk h2{margin:0 0 4px;font-size:17px;font-weight:900;color:var(--ink)}
.blk h2 small{font-size:12px;font-weight:600;color:var(--muted);margin-left:8px}
.blk .sub{font-size:12.5px;color:var(--muted);margin-bottom:12px;line-height:1.55}
.panel{background:#fff;border-radius:12px;padding:16px 18px}
/* 관리 구조 */
.struct{display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:12px}
@media (max-width:900px){.struct{grid-template-columns:1fr}}
.st{border:1.5px solid var(--line);border-radius:12px;padding:12px 14px;font-size:12.5px;line-height:1.6;color:#3E444A}
.st .lb{display:inline-block;font-size:10.5px;font-weight:900;border-radius:6px;padding:2px 8px;color:#fff;margin-bottom:6px}
.st b.t{display:block;font-size:14px;font-weight:900;color:var(--ink);margin-bottom:6px}
.st ul{margin:0;padding-left:16px}
.st li{margin:2px 0}
.st.auto{border-color:#C9D0D8}.st.auto .lb{background:#6B7684}
.st.cesco{border-color:var(--wc);background:#F7FAFE}.st.cesco .lb{background:var(--wc)}
.st.owner{border-color:var(--amber);background:#FFFCF6}.st.owner .lb{background:var(--amber)}
.rule{margin-top:12px;display:flex;gap:12px;flex-wrap:wrap;font-size:12.5px}
.rule div{flex:1;min-width:240px;border-radius:10px;padding:10px 12px;line-height:1.55}
.rule .no{background:#FBECEE;color:#8A1024}.rule .ok{background:#E8F6EE;color:#0B5E31}
.rule b{display:block;font-size:12px;margin-bottom:2px}
/* 명칭 후보 */
.names{width:100%;border-collapse:collapse;font-size:12.5px}
.names th,.names td{border-top:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top;line-height:1.55}
.names th{font-size:11px;color:var(--muted);border-top:0;white-space:nowrap}
.names td.n{font-weight:900;color:var(--ink);white-space:nowrap}
.names tr.rec td{background:var(--wc-bg)}
.names .pick{display:inline-block;font-size:9.5px;font-weight:900;color:#fff;background:var(--wc);border-radius:999px;padding:1px 7px;margin-right:5px;vertical-align:middle}
/* 업종 대표 화면 */
.bizsec{max-width:1320px;margin:0 auto;padding:10px 20px 40px}
.bizsec h2{margin:0 0 4px;font-size:18px;font-weight:900;color:var(--ink)}
.bizsec h2 small{font-size:12px;font-weight:600;color:var(--muted);margin-left:8px}
.bizsec .sub{font-size:12.5px;color:var(--muted);margin-bottom:14px}
.feat{display:flex;gap:24px;align-items:flex-start;justify-content:center;flex-wrap:wrap;background:#fff;border-radius:16px;padding:20px 20px 24px;margin-bottom:22px}
.feat figure{margin:0;width:390px;max-width:100%}
.feat figcaption b{display:block;font-size:13.5px}
.feat figcaption small{font-size:11px}
.notes{width:300px;font-size:12.5px;color:#3E444A;line-height:1.6}
.notes h3{margin:0 0 8px;font-size:13.5px;font-weight:900;color:var(--ink)}
.notes ol{margin:0;padding-left:0;list-style:none}
.notes li{display:grid;grid-template-columns:22px 1fr;gap:6px;margin-bottom:8px}
.notes li i{font-style:normal;width:20px;height:20px;border-radius:50%;background:var(--ink);color:#fff;font-size:10.5px;font-weight:900;display:flex;align-items:center;justify-content:center;margin-top:1px}
.notes li b{color:var(--ink)}
.notes li.c i{background:var(--wc)}
.notes li.o i{background:var(--amber)}
.notes .lg2{margin-top:10px;padding-top:8px;border-top:1px solid var(--line);font-size:11px;color:var(--muted)}
.notes .lg2 i{display:inline-block;width:9px;height:9px;border-radius:50%;vertical-align:middle;margin:0 3px 0 6px}
@media (max-width:760px){.notes{width:100%}}
/* 비교 행 */
.opts{background:#fff;border-radius:12px;padding:14px 18px;margin-bottom:18px}
.opts h3{margin:0 0 8px;font-size:13.5px;font-weight:900;color:var(--ink)}
.opts h3 small{font-weight:600;color:var(--muted);font-size:11.5px;margin-left:8px}
.opts .tw{overflow-x:auto}
.opts table{width:100%;min-width:720px;border-collapse:collapse;font-size:12px}
.opts th,.opts td{border-top:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top;line-height:1.5}
.opts th{font-size:11px;color:var(--muted);font-weight:800;border-top:0;white-space:nowrap}
.opts td.n{width:26px;font-weight:900;color:var(--ink)}
.opts tr.sel td{background:var(--wc-bg)}
.opts td .pick{display:inline-block;font-size:9.5px;font-weight:900;color:#fff;background:var(--wc);border-radius:999px;padding:1px 7px;margin-right:4px}
.opts td .cs{font-size:10px;font-weight:800;color:var(--wc);white-space:nowrap}
.opts td .cs.o{color:var(--muted)}
.opts td.cp{color:var(--txt)}
.row3{display:flex;gap:20px;align-items:flex-start;justify-content:center;flex-wrap:wrap}
.row3 .ed{width:390px}
.row3 figure{margin:0;width:390px;max-width:100%;min-width:0}
.row3 figcaption b{display:block;font-size:13px}
.row3 figcaption small{font-size:11px}
.cmp-h{font-size:13.5px;font-weight:900;color:var(--ink);margin:6px 0 10px}
.cmp-h small{font-weight:600;color:var(--muted);font-size:11.5px;margin-left:8px}
.memo{max-width:1280px}
@media (max-width:760px){.panel{overflow-x:auto}.names td.n{white-space:normal}.lead,.blk{padding:12px 0 0}.panel,.feat,.opts{border-radius:0}.bizsec{padding:10px 0 30px}.row3{gap:14px}.row3 .ed{width:100%}}
"""

def opts_table(bk):
    t = T.TPL[bk]; sel = t['default_sel']
    rows = ''
    for i, (label, title, copy, chip, cesco) in enumerate(t['items']):
        q = T.QS[bk][i]
        on = i in sel
        pick = f'<span class="pick">기본 선택 {sel.index(i)+1}</span>' if on else ''
        rows += f'<tr class="{"sel" if on else ""}"><td class="n">{i+1}</td><td>{pick}<b>{label}</b><br><span class="cs{"" if cesco else " o"}">{"세스코 점검 항목" if cesco else "매장 기록"}</span></td><td>{title.replace("<br>"," ")}</td><td class="cp">{copy}</td><td class="cp">{q}</td></tr>'
    return f'<div class="opts"><h3>{t["owner"]}이 고르는 항목 {len(t["items"])}개<small>2~3개 선택 · 고른 순서대로 노출 · 파란 줄은 기본 선택({t["owner"]}이 아무것도 고르지 않았을 때)</small></h3><div class="tw"><table><thead><tr><th>#</th><th style="width:19%">항목</th><th style="width:17%">제목 (고정)</th><th>기본 설명 ({t["owner"]} 수정 가능 · 140자)</th><th style="width:20%">인터뷰형 질문</th></tr></thead><tbody>{rows}</tbody></table></div></div>'

def struct_block():
    return f'''<div class="blk" id="struct"><h2>관리 구조<small>사업장마다 문장을 새로 쓰지 않고, 업종별로 정해 둔 항목 중 해당하는 것만 켭니다</small></h2>
<div class="sub">페이지는 세 부분으로 나뉩니다. 가운데 세스코 영역이 제일 크고, 사업장마다 다른 건 어느 항목이 켜지느냐뿐입니다. {T.TPL['chicken']['owner']}은 오른쪽 영역에서만 고르고 고칩니다.</div>
<div class="panel"><div class="struct">
<div class="st auto"><span class="lb">① 등록 정보</span><b class="t">위쳌 등록 때 적은 것이 그대로</b><ul><li>상호 · 업종 · 대표 사진</li><li>주소 · 영업시간 · 전화 · 결제</li><li>편의시설 (유아의자 · 단체석 · 주차 …)</li><li>리뷰 수 · 리뷰 한눈에 (연동)</li></ul></div>
<div class="st cesco"><span class="lb">② 세스코가 채우는 영역 · 변주 불가</span><b class="t">업종별 항목 목록에서 해당하는 것만 켜짐</b><ul><li><b>위쳌 AI</b> 요약 · ✅ 3줄 (점검 데이터에서 자동)</li><li><b>{T.STICKER_NAME}</b>(네모 스티커): 블루 멤버스 / 화이트 멤버스 탭, 실제 받는 솔루션만</li><li><b>도구 측정</b>: 악취, 배수구 오염도. 기준 안이면 통과 표시</li><li><b>세스코가 특별히 체크한 장소 정보</b>: 현황 문진, 유효 3개월</li><li>위생 등급 · 점검일 · 리포트 번호</li></ul></div>
<div class="st owner"><span class="lb">③ {T.TPL['chicken']['owner']}이 고르는 영역</span><b class="t">정해진 범위 안에서만</b><ul><li>특장점 10개 중 2~3개 체크 (고른 순서 = 노출 순서)</li><li>항목 설명 140자 · 소개 160자 · 한마디 40자 수정</li><li>사진 추가 (없으면 점검 때 촬영한 사진)</li><li>제목 · 칩 · 측정값 · 점검일은 못 바꿈</li></ul></div>
</div>
<div class="rule"><div class="no"><b>안 되는 것</b>사업장마다 스티커 문장을 새로 쓰는 것, 사장님이 측정값이나 등급을 적는 것, 업종에 없는 항목을 만드는 것</div><div class="ok"><b>되는 것</b>업종별 항목(스티커, 문진, 도구) 중 점검 결과에 맞는 것이 켜지는 것, 사장님이 10개 중 고르고 문장을 다듬는 것</div></div>
</div></div>'''

def naming_block():
    rows = [
        (1,'체크 스탬프','카드 안 CESCO CHECK 도장과 같은 말이고, "체크 완료" 문구와 이어진다. 앱 라벨로 쓰기 짧다.','스탬프 모으기 이벤트로 오해할 수 있다.'),
        (0,'세스코 체크 카드','생긴 그대로 부르는 이름이라 밖에 설명하기 쉽다.','위쳌 AI 카드와 헷갈리고 길다.'),
        (0,'위생 스탬프','위생정보 탭 안에 있다는 게 이름에 드러난다.','위생 등급과 헷갈릴 수 있다.'),
        (0,'위생 배지','네이버 플레이스 배지처럼 읽힌다.','네모 카드 모양과 안 맞고 세스코 느낌이 약하다.'),
    ]
    tr = ''.join(f'<tr class="{"rec" if r else ""}"><td class="n">{"<span class=\'pick\'>추천</span>" if r else ""}{n}</td><td>{a}</td><td>{b}</td></tr>' for r,n,a,b in rows)
    return f'''<div class="blk" id="naming"><h2>네모 스티커 이름 후보<small>팀 안에서 부르는 말을 정하기 위한 후보. 이 시안에서는 "{T.STICKER_NAME}"(가칭)으로 적었습니다</small></h2>
<div class="panel"><table class="names"><thead><tr><th style="width:18%">이름</th><th>이유</th><th style="width:32%">걸리는 점</th></tr></thead><tbody>{tr}</tbody></table></div></div>'''


def place_block():
    rows = [
        ('구조','네이버 편의시설 칸을 세스코 항목으로 늘린 모양입니다. 3열 타일에 아이콘과 짧은 라벨을 두고, 누르면 아래에 문진 원문과 체크일이 펼쳐집니다.'),
        ('고른 이유','한눈에 들어오고, 네이버를 쓰던 사람에게 익숙합니다. 항목이 늘어도 화면이 길어지지 않습니다.'),
        ('만들 때 챙길 것','문진 원문은 한 번 더 눌러야 보이니 첫 타일은 펼쳐진 상태로 둡니다. 항목마다 아이콘을 정해야 합니다.'),
        ('검토 뒤 뺀 안','B 손님 질문형(묻는 말을 Q로, 문진 원문을 A로)은 제일 길고 업종마다 질문 10개를 써야 해서, C 기본정보 통합(주소·영업시간 아래 체크 칩)은 세스코가 묻힐 수 있어서 빼기로 했습니다.'),
    ]
    tr = ''.join(f'<tr><td class="n">{k}</td><td>{v}</td></tr>' for k,v in rows)
    figs = ''
    for bk in ['chicken','care']:
        t = T.TPL[bk]; mt = 'white' if bk=='chicken' else 'blue'
        figs += f'<figure><figcaption><b>아이콘 그리드 · {t["key"]}</b><small>{t["reg"]["name"]} · 장소정보 탭. 타일을 누르면 문진 원문이 펼쳐집니다</small></figcaption><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div data-static data-biz="{bk}" data-t="C" data-tab="place" data-mt="{mt}" data-pv="A"></div></div></figure>'
    return f'''<div class="blk" id="place"><h2>장소정보 탭 · 아이콘 그리드로 확정<small>11/02 결정. 기본 정보와 세스코 체크 {len(T.PLACE["chicken"]["checks"])}개를 3열 타일로 보여 줍니다</small></h2>
<div class="sub">위쪽 기본 정보(주소, 영업시간, 전화, 결제, 편의)는 네이버와 같은 모양이고, 그 아래 "세스코가 특별히 체크한 장소 정보"를 아이콘 타일로 둡니다. 10/30에 비교했던 세 안 가운데 A 아이콘 그리드를 골랐습니다.</div>
<div class="panel"><table class="names"><thead><tr><th style="width:18%">항목</th><th>내용</th></tr></thead><tbody>{tr}</tbody></table></div>
<div class="row3" style="margin-top:16px">{figs}</div></div>'''

def tools_block():
    rows = [
        ('모양','계기판 반원 2개를 나란히 두고 바늘이 파란 칸을 가리킵니다. 게이지를 누르면 그 아래에 쉬운 설명, 기준 단계, 예시 문구, 체크일이 펼쳐집니다. 처음에는 첫 게이지만 펼쳐 두고, 같은 제목을 두 번 쓰지 않습니다.'),
        ('이름','측정 항목 이름 대신 결과가 좋다는 말을 씁니다. 악취 → <b>냄새 없이 쾌적해요</b>, 배수구 오염도 → <b>배수구가 청결하게 관리되고 있어요</b>. 측정 항목과 도구 이름은 그 아래 작은 글씨로 남깁니다.'),
        ('색','제일 좋은 단계(청결)는 초록이 아니라 세스코 파랑입니다. 바늘 끝 체크, 결과 칩, 펼친 단계 칩도 같은 파랑이고, 주의·경고·심각은 노랑·주황·빨강 그대로입니다.'),
        ('만들 때 챙길 것','접힌 항목은 게이지를 눌러야 보입니다. 게이지가 수치처럼 읽힐 수 있어 "바늘이 파란 칸이면 기준 안" 한 줄을 넣었습니다. 단계 설명은 이 사업장 단계 한 줄만 보이고 나머지는 칩 이름만 둡니다.'),
        ('검토 뒤 뺀 안','스탬프형(초록 체크 도장)은 한때 확정했다가 게이지형으로 되돌렸습니다. A 검사 리포트형(종이 리포트 모양)은 금색 표식이 없어 위생정보 카드와 톤이 달라 보이고, C 점검 기록형(타임라인·단계 사다리·전문가 메모 말풍선)은 셋 중 제일 길어서 뺐습니다. 처음 금색 표식형은 참고 캡처(<a href="ref/도구측정블록_현재디자인_261102.png" target="_blank">ref/도구측정블록_현재디자인_261102.png</a>)로 남깁니다.'),
    ]
    tr = ''.join(f'<tr><td class="n">{k}</td><td>{v}</td></tr>' for k,v in rows)
    figs = ''
    for bk in ['chicken','care']:
        t = T.TPL[bk]
        figs += f'<figure><figcaption><b>게이지형 · {t["key"]}</b><small>{t["reg"]["name"]} · 각 화면 맨 아래 블록만 떼어 본 것. 게이지를 눌러 펼치고 접습니다</small></figcaption><div class="phone part"><div data-tools data-biz="{bk}" data-tv="B"></div></div></figure>'
    return f'''<div class="blk" id="tools"><h2>도구 측정 블록 · 게이지형으로 확정<small>11/02 결정. 내용(쉬운 설명, 기준 단계, 예시 문구, 체크일)은 그대로입니다</small></h2>
<div class="sub">위 업종별 화면 맨 아래 블록이 이 모양으로 들어가 있습니다. 11/02에 검사 리포트형, 게이지형, 점검 기록형, 스탬프형을 비교해 게이지형으로 정했고, 게이지 이름은 결과가 좋다는 말로, 제일 좋은 칸 색은 세스코 파랑으로 했습니다.</div>
<div class="panel"><table class="names"><thead><tr><th style="width:18%">항목</th><th>내용</th></tr></thead><tbody>{tr}</tbody></table></div>
<div class="row3" style="margin-top:16px">{figs}</div></div>'''

def tools_more_block():
    rows = [
        ('D','스탬프형','초록 체크 도장 카드 2장. 카드를 누르면 아래에 설명이 펼쳐집니다.','체크 스탬프(네모 스티커)와 같은 "도장" 말로 이어지고 글이 가장 적습니다.','도장만 있어 무엇을 쟀는지가 작은 글씨에만 있습니다.'),
        ('E','한 줄 리스트형','아이콘, 결과 문장, 기준 안 칩을 한 줄에. 줄 아래 가는 단계 칸(초록이 이 사업장). 줄을 누르면 펼쳐집니다.','세로로 제일 짧고 항목이 늘어도 한 줄씩만 늘어납니다. 위쳌 AI 카드의 체크 줄과 닮았습니다.','도장보다 눈에 덜 띕니다.'),
        ('F','요약 카드형','파란 머리에 "2항목 모두 기준 안"을 크게, 아래에 결과 문장 2줄. 줄을 누르면 펼쳐집니다.','결론이 제일 먼저 보입니다. 화면 맨 아래 마무리 카드 역할을 합니다.','파란 머리가 위쳌 AI 카드와 겹쳐 보일 수 있습니다. 항목별 상태는 줄을 봐야 압니다.'),
    ]
    tr = ''.join(f'<tr><td class="n">{k} · {n}</td><td>{d}</td><td>{g}</td><td>{b}</td></tr>' for k,n,d,g,b in rows)
    figs = ''
    for k, nm in [('D','스탬프형'),('E','한 줄 리스트형'),('F','요약 카드형')]:
        for bk in ['chicken','care']:
            t = T.TPL[bk]
            figs += f'<figure><figcaption><b>{k}안 · {nm}</b><small>{t["reg"]["name"]} · 블록만 떼어 본 것. 게이지나 줄을 눌러 펼치고 접습니다</small></figcaption><div class="phone part"><div data-tools data-biz="{bk}" data-tv="{k}"></div></div></figure>'
    return f'''<div class="blk" id="tools2"><h2>도구 측정 블록 · 함께 비교한 3안<small>게이지형과 같은 규칙(결과 문장 먼저, 글은 눌러야 보임)으로 모양만 다른 것</small></h2>
<div class="sub">위 게이지형이 지금 들어가 있는 안입니다. 아래 셋은 비교용으로 남긴 것이고, 펼쳤을 때 내용은 넷이 같습니다.</div>
<div class="panel"><table class="names"><thead><tr><th style="width:14%">안</th><th style="width:32%">모양</th><th>좋은 점</th><th style="width:24%">걸리는 점</th></tr></thead><tbody>{tr}</tbody></table></div>
<div class="row3" style="margin-top:16px">{figs}</div></div>'''

def feat_notes(bk):
    t = T.TPL[bk]; o = t['owner']
    return f'''<div class="notes"><h3>화면 구성 (위에서 아래로)</h3><ol>
<li class="c"><i>1</i><div><b>위쳌 AI</b>: 업종 소개, 점검 3줄, 매장정보, 리뷰 한눈에</div></li>
<li><i>2</i><div><b>기본 정보</b>: 주소, 영업시간, 전화, 결제, 태그, 편의. 등록 정보에서 자동</div></li>
<li class="c"><i>3</i><div><b>위생정보 / 장소정보 탭</b>: 둘 다 눌러 볼 수 있습니다</div></li>
<li class="c"><i>4</i><div><b>{T.STICKER_NAME}</b>(네모 스티커): 블루 멤버스(파랑) / 화이트 멤버스(식품안전, 초록) 탭. 실제 받는 솔루션만</div></li>
<li class="o"><i>5</i><div><b>{o}이 고른 POINT 01~03</b>: 10개 중 2~3개. 아래 선택 화면에서 바꿔 볼 수 있습니다</div></li>
<li class="c"><i>6</i><div><b>도구 측정 "세스코가 전문적으로 체크했습니다"</b>: 각 화면 맨 아래, 두 탭 공통. 게이지형(11/02 확정). 카드 2장에 초록 체크 도장이 찍혀 있으면 기준 안. 이름은 "냄새 없이 쾌적해요", "배수구가 청결하게 관리되고 있어요"이고, 카드를 누르면 쉬운 설명, 기준 단계, 예시 문구, 체크일이 펼쳐짐. <a href="#tools">자세히</a></div></li>
<li class="c"><i>7</i><div><b>장소정보 탭</b>(아이콘 그리드로 확정): 기본 정보 전체와 <b>세스코가 특별히 체크한 장소 정보</b>. 유아의자, 단체석, 국내산 김치, 조리자 비흡연, 손세정제, 알레르기 표기처럼 가 봐야만 아는 짧은 사실, 타일을 누르면 문진 원문</div></li>
</ol><div class="lg2">세스코 영역<i style="background:var(--wc)"></i> · 등록 정보<i style="background:#6B7684"></i> · {o} 선택<i style="background:var(--amber)"></i></div></div>'''

def build():
    secs = ''
    for bk in ['chicken', 'care']:
        t = T.TPL[bk]; reg = t['reg']; o = t['owner']; mt = 'white' if bk=='chicken' else 'blue'
        feat = f'''<div class="feat">
<figure><figcaption><b>상세페이지형 · 위생정보 탭</b><small>풀블리드 사진과 POINT 01~03. {T.STICKER_NAME} 탭과 카드는 눌러서 넘길 수 있습니다</small></figcaption><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div data-static data-biz="{bk}" data-t="C" data-tab="hy" data-mt="{mt}"></div></div></figure>
<figure><figcaption><b>같은 화면 · 장소정보 탭</b><small>네이버식 기본 정보와 세스코가 특별히 체크한 장소 정보를 아이콘 그리드로. 타일을 누르면 문진 원문이 펼쳐집니다</small></figcaption><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div id="pv-{bk}" data-static data-biz="{bk}" data-t="C" data-tab="place" data-mt="{mt}" data-pv="A"></div></div></figure>
{feat_notes(bk)}</div>'''
        figs = f'<figure><figcaption><b>{o} 선택 화면</b><small>위쳌 사업주용. 2~3개 체크, 기본 문안이 들어 있고, 여기서 바꾸면 이 업종 화면이 다 같이 바뀝니다</small></figcaption><div class="ed"><div class="bar">위생 페이지 관리<span class="sv">저장</span></div><div class="in" data-ed data-biz="{bk}"></div></div></figure>'
        for code, nm, ds in TYPES:
            figs += f'<figure><figcaption><b>{nm}</b><small>{ds}</small></figcaption><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div data-static data-biz="{bk}" data-t="{code}" data-tab="hy" data-mt="{mt}"></div></div></figure>'
        secs += f'''<section class="bizsec" id="{bk}"><h2>{t["key"]} · {reg["name"]}<small>{o} 입력이 없는 기본 상태. 상호와 수치는 예시</small></h2>
<div class="sub">위쳌 AI, 기본 정보, {T.STICKER_NAME}, 도구 측정은 세 유형이 같고, 그 사이 본문만 유형에 따라 다릅니다.</div>
{feat}
<div class="cmp-h">참고: 다른 두 유형과 {o} 선택 화면<small>팀장님 평가는 인터뷰형, 상세페이지형이 수치형보다 좋다는 쪽</small></div>
{opts_table(bk)}<div class="row3">{figs}</div></section>'''
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 사업장 상세 시안, 치킨집과 산후조리원</title>{B.FONT}<style>{B.CSS}{T.EXTRA_CSS}{CSS}</style></head>
<body>
<div class="lead"><div class="desc"><h1>위쳌 사업장 상세 시안, 치킨집과 산후조리원</h1>
<p>10/30 회의에서 나온 7가지를 반영한 판입니다. 업종마다 <b>상세페이지형</b>을 먼저 크게 두고, 같은 화면의 <b>장소정보 탭</b>을 옆에 붙였습니다. 사장님 선택 화면, 수치형, 인터뷰형은 아래에 참고로 있습니다. 장소정보 탭 UI는 11/02에 A 아이콘 그리드로, 도구 측정 블록은 스탬프형으로 정해서 그 모양만 남겼습니다.</p>
<p>화면 안의 탭, 카드, 체크박스는 다 눌러 볼 수 있습니다. 상호, 주소, 수치는 예시입니다.</p>
<div class="chips"><span>① 장소정보 탭 (아이콘 그리드 확정)</span><span class="g">② {T.STICKER_NAME} 블루/화이트 멤버스</span><span class="y">③ 도구 측정 블록 (스탬프형 확정)</span><span>④ 문장 손질</span><span>⑤ 상세페이지형 앞으로</span><span>⑥ 관리 구조</span><span>⑦ 명칭 후보</span></div>
<div class="toc"><a href="#struct">관리 구조</a><a href="#naming">명칭 후보</a><a href="#place">장소정보 탭</a><a href="#tools">도구 측정 블록</a><a href="#tools2">더 그린 3안</a><a href="#chicken">치킨집</a><a href="#care">산후조리원</a><a href="#memo">확인 필요</a></div></div></div>
{struct_block()}
{naming_block()}
{place_block()}
{tools_block()}
{tools_more_block()}
{secs}
<div class="memo" id="memo"><h2>확인 필요, 출처</h2>
<div class="tw"><table><thead><tr><th style="width:22%">항목</th><th>내용</th></tr></thead><tbody>
<tr><td><b>장소 정보</b></td><td>탭 UI는 11/02에 아이콘 그리드로 확정했습니다. 회의록에 나온 예시(유아의자, 단체석, 국내산 김치, 조리자 비흡연, 손세정제, 알레르기 표기)를 짧은 한 줄로 쓰고, 엑셀 ②시트 "내용" 열의 문진 원문을 그 아래 작게 두었습니다. 유아의자, 단체석, 모자동실, CCTV는 문진 시트에 없어서 "현장 문진"으로 표시한 예시입니다.</td></tr>
<tr><td><b>{T.STICKER_NAME}</b></td><td>엑셀 ①시트에 치킨집 행이 없어서 치킨집 6장(식품안전 3, 전문클리닝, 에어, 종합방제)은 같은 형식으로 쓴 초안입니다. 산후조리원 5장은 10/23 개선안 1안 원문입니다. <span class="flag">확인 필요</span>블루는 IPM, 바이러스케어, 에어, 워터, 레스트룸(바디케어), 전문클리닝, 마이랩, 화이트는 식품안전으로 묶었습니다. 초록은 세스코 푸드 색(#0E8F4A)으로 잡았습니다.</td></tr>
<tr><td><b>도구 측정</b></td><td>디자인은 11/02 게이지형(청결 칸 파랑)으로 확정. 엑셀 ③시트. 악취 예시 문구는 원문 그대로입니다(화장실 기준 문장). <span class="flag">확인 필요</span>배수구 오염도는 ③시트에 예시 문구가 없어서 ②시트 숙박 행의 배수구 문장을 가져왔습니다. 단계 이름은 "양호" 대신 "청결"로 맞췄습니다.</td></tr>
<tr><td><b>명칭</b></td><td>이 시안에서는 "{T.STICKER_NAME}"(가칭)으로 적었습니다. 이름이 정해지면 한 번에 바꿉니다.</td></tr>
<tr><td><b>글자 수 · 검수</b></td><td>글자 수 상한(160, 140, 40), 사진 장수, 사장님이 고친 글의 검수 방식(바로 게시 / 세스코 승인 후 게시), 금지어 필터 위치는 아직 정하지 않았습니다.</td></tr>
</tbody></table></div></div>
<script>{T.js_block()}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
