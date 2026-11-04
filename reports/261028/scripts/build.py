# -*- coding: utf-8 -*-
"""reports/261028 위쳌 사업장 상세 풀페이지 9종 + index 생성기.
실행: python3 reports/261028/scripts/build.py  (저장소 루트에서)
디자인 토큰·클래스는 reports/261026/위쳌_모바일상세페이지형(M안)·L안·B안 파일에서 그대로 가져왔다.
"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), '..')
FONT = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">'

CSS = r"""
:root{--ink:#111111;--ink2:#1A1A1A;--txt:#555555;--muted:#8A8A8A;--line:#EEEEEE;--bg:#F6F7F4;--card:#FFFFFF;--red:#C8102E;--chip:#EDEFE9;--navy:#1A3668;--amber:#C77700;--amber-bg:#FFF6E8;--wc:#0072CE;--wc-bg:#EAF3FC;--wc-line:#CFE0F3}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#E9EBE7;color:var(--txt);font-family:"Pretendard Variable",Pretendard,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;font-size:13px;line-height:1.55;-webkit-font-smoothing:antialiased;word-break:keep-all}
p{margin:0}
.wrap{max-width:1320px;margin:0 auto;padding:20px 20px 60px}
.desc{background:#fff;border-radius:12px;padding:14px 18px;margin-bottom:18px}
.desc h1{margin:0;font-size:16px;font-weight:800;color:var(--ink)}
.desc p{font-size:12.5px;color:var(--muted);margin-top:4px}
.desc a{color:var(--wc)}
.stage{display:flex;gap:28px;align-items:flex-start;justify-content:center;flex-wrap:wrap}
.stage > figure{margin:0}
figcaption{font-size:12.5px;font-weight:800;color:var(--ink);margin:0 0 8px 4px}
figcaption small{display:block;font-weight:500;color:var(--muted);font-size:11.5px}
.phone{width:390px;background:var(--bg);border-radius:28px;box-shadow:0 10px 30px rgba(0,0,0,.14),0 0 0 1px rgba(0,0,0,.06);overflow:hidden;position:relative}
.fold{position:absolute;left:0;right:0;top:844px;border-top:2px dashed #C8102E;pointer-events:none;z-index:5}
.fold span{position:absolute;right:10px;top:-9px;background:#C8102E;color:#fff;font-size:9.5px;font-weight:800;border-radius:4px;padding:1px 6px}
.appbar{height:52px;background:#fff;display:flex;align-items:center;padding:0 12px;gap:8px;border-bottom:1px solid var(--line)}
.appbar .back{width:36px;height:36px;border-radius:50%;border:0;background:#fff;display:flex;align-items:center;justify-content:center}
.appbar .t{flex:1;font-size:15px;font-weight:800;color:var(--ink);text-align:center;margin-right:36px}
.head{background:#fff;padding:12px 16px 0}
.head .nm{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.head h2{margin:0;font-size:19px;font-weight:900;color:var(--ink)}
.head .cat{font-size:12px;color:#595959}
.head .rv{display:flex;align-items:center;gap:5px;font-size:12px;color:var(--txt);margin-top:4px}
.head .rv b{color:var(--ink2);font-weight:700}
.tabs{display:flex;background:#fff;border-bottom:1px solid var(--line);margin-top:10px}
.tabs span{flex:1;height:42px;display:flex;align-items:center;justify-content:center;font-size:13px;color:#595959}
.tabs span.on{border-bottom:3px solid var(--wc);font-weight:900;color:var(--wc)}
.body{padding:12px 16px 16px;display:flex;flex-direction:column;gap:10px}
.card{background:var(--card);border-radius:14px;padding:12px 14px;box-shadow:0 1px 4px rgba(0,0,0,.05);position:relative}
/* AI 요약 */
.ai{background:#fff;border:1px solid var(--wc-line);border-radius:14px;padding:11px 13px}
.ai .lb{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:900;color:var(--wc);letter-spacing:.04em}
.ai .lb small{margin-left:auto;font-weight:600;color:var(--muted);letter-spacing:0;font-size:10px}
.ai ul{margin:7px 0 0;padding:0;list-style:none}
.ai li{font-size:12.5px;color:var(--ink2);line-height:1.5;padding:3px 0 3px 14px;position:relative}
.ai li:before{content:"";position:absolute;left:2px;top:10px;width:5px;height:5px;border-radius:50%;background:var(--wc)}
/* 위생 정보 카드 (261027 사업장 상세 시안의 공통 카드 + 실측 2열, 위쳌 파란색) */
.hc{background:#fff;border-radius:14px;padding:12px 14px;box-shadow:0 1px 4px rgba(0,0,0,.05)}
.hc .top{display:flex;align-items:center;gap:10px}
.grade{width:46px;height:46px;border-radius:50%;background:var(--wc);display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;flex-shrink:0}
.grade b{font-size:19px;line-height:1}
.grade span{font-size:8px;font-weight:800;margin-top:2px}
.hc .top .t{flex:1}
.hc .top .t b{display:block;font-size:13.5px;font-weight:900;color:var(--ink);line-height:1.3}
.hc .top .t span{font-size:10.5px;color:var(--muted)}
.hc .pt{margin-top:10px;padding-top:10px;border-top:1px solid var(--line)}
.hc .pill{display:inline-block;font-size:10px;font-weight:900;color:#595959;background:var(--chip);border-radius:6px;padding:2px 7px}
.hc .pill+small{float:right;font-size:10px;color:var(--muted)}
.hc .hl{font-size:13px;font-weight:900;color:var(--ink);margin-top:6px}
.hc .ds{font-size:11.5px;color:var(--txt);line-height:1.5;margin-top:3px}
.hc .grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.hc .m{border:1px solid var(--wc-line);border-radius:12px;padding:10px 11px}
.hc .m .k{display:flex;align-items:center;justify-content:space-between;font-size:10.5px;font-weight:700;color:#595959}
.hc .m .k i{font-style:normal;font-size:9px;font-weight:900;color:#fff;background:var(--wc);border-radius:5px;padding:2px 6px}
.hc .m .v{font-size:19px;font-weight:900;color:var(--wc);line-height:1;margin-top:5px}
.hc .m .v small{font-size:10.5px;font-weight:700}
.hc .m .bar{height:6px;border-radius:3px;background:#E6EDF5;margin-top:6px;position:relative}
.hc .m .bar i{display:block;height:6px;border-radius:3px;background:var(--wc)}
.hc .m .b{font-size:9.5px;color:var(--muted);margin-top:4px;line-height:1.3}
.hc .sum{display:flex;align-items:center;gap:8px;background:var(--wc-bg);border-radius:10px;padding:9px 11px;margin-top:10px;font-size:11.5px;color:var(--ink2);line-height:1.45}
.hc .sum b{color:var(--ink);font-weight:900}
/* 사업주 영역 표시 (검토용 표식 · 실제 서비스에는 노출 안 됨) */
.own-tag{position:absolute;right:10px;top:-8px;z-index:2;font-size:9.5px;font-weight:900;color:#fff;background:var(--amber);border-radius:999px;padding:2px 8px;white-space:nowrap}
.own-in{outline:1.5px dashed var(--amber);outline-offset:3px;border-radius:14px;position:relative}
.own-tag.l{right:auto;left:10px}
.lg{display:flex;gap:12px;flex-wrap:wrap;font-size:10px;color:var(--muted);font-weight:700;padding:0 2px}
.lg i{display:inline-block;width:9px;height:9px;border-radius:50%;vertical-align:middle;margin-right:4px}
/* 결과 카드 (B안 계기판형) */
.sh2{display:flex;align-items:baseline;gap:8px;padding:4px 2px 0}
.sh2 b{font-size:13.5px;font-weight:900;color:var(--ink)}
.sh2 small{margin-left:auto;font-size:10.5px;color:var(--muted);font-weight:600}
.res{display:flex;flex-direction:column;gap:8px}
.r{background:#fff;border:1px solid var(--wc-line);border-radius:12px;padding:10px 12px}
.r .k{font-size:10.5px;font-weight:700;color:#6B7684}
.r .vd{display:flex;align-items:flex-start;gap:5px;margin-top:3px;font-size:16px;font-weight:900;color:var(--wc);line-height:1.25}
.r .vd svg{flex-shrink:0;margin-top:3px;background:var(--wc);color:#fff;border-radius:50%;padding:2px}
.mt{margin-top:7px}
.mrow{display:flex;align-items:baseline;gap:3px}
.mrow b{font-size:17px;font-weight:900;color:var(--ink);line-height:1}
.mrow small{font-size:10px;font-weight:700;color:var(--muted)}
.pill2{margin-left:auto;font-size:9.5px;font-weight:800;color:var(--wc);background:var(--wc-bg);border-radius:999px;padding:2px 7px;white-space:nowrap}
.mb{position:relative;height:7px;border-radius:4px;background:#E6EDF5;margin-top:6px}
.mb i{display:block;height:7px;border-radius:4px;background:var(--wc)}
.mb:after{content:"";position:absolute;right:0;top:-3px;width:2px;height:13px;background:#1A1A1A;border-radius:1px}
.ml{display:flex;justify-content:space-between;font-size:9px;color:var(--muted);margin-top:4px;font-weight:600}
.ml span:last-child{color:var(--ink2);font-weight:800}
.r .why1{font-size:10.5px;color:var(--txt);margin-top:5px;padding-top:5px;border-top:1px dashed var(--wc-line);line-height:1.4}
.r .why1 b{color:var(--ink2);font-weight:800}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.two .card .lb{font-size:9.5px;font-weight:900;letter-spacing:.1em;color:var(--wc)}
.two .card .big{font-size:14px;font-weight:900;color:var(--ink);line-height:1.25;margin-top:3px}
.two .card .big em{font-style:normal;color:var(--wc)}
.two .card .sm{font-size:10.5px;color:var(--muted);margin-top:4px;line-height:1.4}
/* 점검 이력표 (E안) */
.hist .lb{font-size:9.5px;font-weight:900;letter-spacing:.1em;color:var(--wc)}
.hist table{width:100%;border-collapse:collapse;margin-top:8px;table-layout:fixed}
.hist th,.hist td{padding:0;text-align:center;font-weight:600}
.hist th{font-size:9px;color:var(--muted);padding-bottom:6px;font-weight:700}
.hist th:first-child,.hist td:first-child{text-align:left;width:88px}
.hist td{height:30px;border-top:1px solid var(--line)}
.hist td:first-child{font-size:11px;font-weight:800;color:var(--ink)}
.hist td i{display:inline-block;width:16px;height:16px;border-radius:50%;background:var(--wc);vertical-align:middle;position:relative}
.hist td i:after{content:"";position:absolute;left:5px;top:3px;width:4px;height:8px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
.hist td.now{background:var(--wc-bg)}
.hist th.now{color:var(--wc)}
.hist .ft{font-size:10px;color:var(--muted);margin-top:8px;line-height:1.45}
/* 한 줄 목록 */
.list{padding:4px 14px}
.list .hd{display:flex;align-items:center;gap:8px;padding:8px 0 4px;flex-wrap:wrap}
.list .hd b{font-size:12.5px;font-weight:900;color:var(--ink)}
.list .hd span{font-size:10px;color:var(--muted);font-weight:700;margin-left:auto;text-align:right}
.list .row{display:grid;grid-template-columns:16px 1fr auto;gap:0 8px;align-items:center;padding:9px 0;border-bottom:1px solid var(--line)}
.list .row:last-child{border-bottom:0}
.list .ok{width:16px;height:16px;border-radius:50%;background:var(--wc);display:flex;align-items:center;justify-content:center}
.list .ok.o{background:#fff;border:1.5px solid #C9D0D8}
.list .k{font-size:12.5px;font-weight:900;color:var(--ink)}
.list .k small{display:block;font-weight:600;color:var(--muted);font-size:10.5px;margin-top:1px}
.list .tag{font-size:9.5px;font-weight:800;color:var(--wc);background:var(--wc-bg);border-radius:6px;padding:2px 6px;white-space:nowrap}
.list .tag.o{color:var(--muted);background:#F2F4F7}
.list .num{width:16px;height:16px;border-radius:50%;background:var(--ink);color:#fff;font-size:9.5px;font-weight:900;display:flex;align-items:center;justify-content:center}
/* 사진 자리 · 팩트 칩 · 바이라인 */
.ph{border:1.5px dashed #C9D0D8;border-radius:12px;background:#F2F4F7;display:flex;align-items:center;justify-content:center;color:#8A95A3;font-size:10.5px;font-weight:700;text-align:center;line-height:1.4;padding:6px}
.ph.wide{aspect-ratio:16/9;margin-top:10px}
.ph.sq{aspect-ratio:1}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:10px}
.cap2{font-size:10.5px;color:var(--muted);margin-top:5px;line-height:1.4}
.fact{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;font-weight:800;color:var(--wc);background:var(--wc-bg);border-radius:999px;padding:3px 9px;margin-top:8px}
.fact i{width:12px;height:12px;border-radius:50%;background:var(--wc);display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.byline{display:flex;align-items:center;gap:8px}
.byline .av{width:30px;height:30px;border-radius:50%;background:var(--wc-bg);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.byline b{display:block;font-size:12px;font-weight:900;color:var(--ink)}
.byline span{font-size:10.5px;color:var(--muted)}
/* 인터뷰·에디터형 (J안·I안) */
.iv-hero{background:#fff;border-radius:14px;padding:14px;box-shadow:0 1px 4px rgba(0,0,0,.05);position:relative}
.iv-hero .ph{height:150px}
.iv-hero .eb{font-size:9.5px;font-weight:900;letter-spacing:.1em;color:var(--wc);margin-top:10px}
.iv-hero h3{margin:4px 0 0;font-size:18px;font-weight:900;color:var(--ink);line-height:1.3;letter-spacing:-.01em}
.iv-hero .who{font-size:11px;color:var(--muted);margin-top:6px}
.intro p{font-size:12.5px;color:var(--ink2);line-height:1.65}
.intro p+p{margin-top:8px}
.intro p b{font-weight:900;color:var(--ink)}
.iv .it{padding:10px 0;border-top:1px solid var(--line)}
.iv .it:first-child{border-top:0;padding-top:0}
.iv .it:last-child{padding-bottom:0}
.iv .q{font-size:12.5px;font-weight:900;color:var(--ink);line-height:1.4}
.iv .q:before{content:"Q";color:var(--red);font-weight:900;margin-right:7px}
.iv .a{font-size:12.5px;color:var(--ink2);line-height:1.65;margin-top:6px;padding-left:18px;position:relative}
.iv .a:before{content:"A";position:absolute;left:0;top:0;color:var(--wc);font-weight:900}
.iv .a small{display:block;color:var(--muted);font-size:10.5px;margin-top:3px}
.iv .fact{margin-left:18px;margin-top:6px}
.pull{background:var(--navy);border-radius:14px;padding:14px 16px;color:#fff}
.pull p{font-size:15px;font-weight:900;line-height:1.4;letter-spacing:-.01em}
.pull span{display:block;font-size:10.5px;color:#9FB4DC;margin-top:6px}
.say{background:#FFF8E8;border:1px solid #F3E2B8}
.say .lb{font-size:9.5px;font-weight:900;letter-spacing:.1em;color:#9A6B12}
.say p{font-size:13px;color:var(--ink);line-height:1.6;margin-top:6px;font-weight:600}
.say .sg{font-size:10.5px;color:var(--muted);margin-top:6px}
.say .ph{height:96px;margin-top:8px}
.report{display:flex;align-items:center;gap:10px;border:1px dashed #C9CFD6;border-radius:14px;padding:10px 12px;background:#fff}
.report .t{flex:1;font-size:12px;color:var(--ink2);font-weight:700}
.report .t small{display:block;color:var(--muted);font-size:10.5px;font-weight:500}
.btn{display:inline-block;border-radius:10px;padding:8px 12px;font-size:12px;font-weight:800;text-decoration:none;white-space:nowrap}
.btn.sec{background:#fff;color:var(--ink);border:1px solid #E3E6E1}
.fine{font-size:10px;color:var(--muted);line-height:1.5}
.actions{background:#fff;border-top:1px solid var(--line);padding:10px 16px 14px;display:flex;gap:8px;align-items:center}
.actions .ico{width:44px;height:44px;border-radius:12px;border:1px solid #E3E6E1;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:9.5px;color:#595959;gap:2px}
.actions .cta{flex:1;height:44px;border-radius:12px;background:var(--wc);color:#fff;font-size:14px;font-weight:900;display:flex;align-items:center;justify-content:center}
/* 상세페이지형 (M안 풀블리드) */
.dp{background:#fff;color:#222}
.dp .pho{background:linear-gradient(160deg,#E6EAEF 0%,#CBD3DC 100%);position:relative;display:flex;align-items:flex-end;padding:12px 14px;color:#6B7684;font-size:10.5px;font-weight:700;line-height:1.4}
.dp .pho:before{content:"";position:absolute;inset:10px;border:1px dashed rgba(107,118,132,.45);border-radius:6px;pointer-events:none}
.dp .hr{position:relative;height:400px}
.dp .hr .pho{position:absolute;inset:0;height:auto;align-items:flex-start}
.dp .hr .ov{position:absolute;left:0;right:0;bottom:0;padding:28px 24px 30px;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.62) 100%);color:#fff}
.dp .hr .lab{color:#BFD6F2}
.dp .hr h1{margin:8px 0 6px;font-size:26px;font-weight:900;line-height:1.25;letter-spacing:-.02em;color:#fff}
.dp .hr .sub{font-size:13px;color:#E3EAF2;font-weight:600}
.dp .sec{padding:36px 24px 32px;text-align:center;position:relative}
.dp .lab{display:block;font-size:10.5px;letter-spacing:.2em;font-weight:800;color:var(--wc)}
.dp h2{margin:10px 0 14px;font-size:22px;font-weight:900;line-height:1.3;letter-spacing:-.02em;color:#111}
.dp p{font-size:13.5px;line-height:1.8;color:#444;word-break:keep-all}
.dp p b{font-weight:800;color:#111}
.dp .alt{background:#F4F5F2}
.dp .strip{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #E6E8E4;border-bottom:1px solid #E6E8E4;margin-top:26px}
.dp .strip div{padding:12px 4px;border-right:1px solid #E6E8E4}
.dp .strip div:last-child{border-right:0}
.dp .strip b{display:block;font-size:10px;color:#8A8A8A;font-weight:800;letter-spacing:.06em}
.dp .strip span{display:block;font-size:11.5px;color:#222;font-weight:700;margin-top:4px;line-height:1.35}
.dp .pt{position:relative}
.dp .pt .pho{height:250px}
.dp .pt .tx{padding:28px 24px 36px;text-align:center}
.dp .pt .num{font-size:11px;letter-spacing:.2em;font-weight:900;color:var(--wc)}
.dp .pt h3{margin:8px 0 12px;font-size:21px;font-weight:900;line-height:1.3;letter-spacing:-.02em;color:#111}
.dp .pt .fx{display:inline-flex;align-items:center;gap:6px;margin-top:16px;font-size:11px;font-weight:800;color:var(--wc);border:1px solid var(--wc-line);border-radius:999px;padding:5px 12px;background:#fff}
.dp .pt .fx i{width:14px;height:14px;border-radius:50%;background:var(--wc);display:inline-flex;align-items:center;justify-content:center}
.dp .pt .own-tag{top:10px;right:14px}
.dp .qt{position:relative;height:340px}
.dp .qt .pho{position:absolute;inset:0;height:auto;align-items:flex-start}
.dp .qt .ov{position:absolute;left:0;right:0;bottom:0;padding:30px 24px 32px;background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,.7) 100%);color:#fff;text-align:left}
.dp .qt .ov .lab{color:#BFD6F2}
.dp .qt .ov .q{font-size:21px;font-weight:900;line-height:1.35;letter-spacing:-.02em;margin-top:8px}
.dp .qt .ov .by{font-size:11.5px;color:#D6DEE8;margin-top:10px}
.dp .qa{padding:8px 24px 32px;text-align:left}
.dp .qa .it{padding:16px 0;border-bottom:1px solid #ECEEEA}
.dp .qa .it:last-child{border-bottom:0}
.dp .qa .q{font-size:14px;font-weight:900;color:#111;line-height:1.45}
.dp .qa .a{font-size:13.5px;color:#444;line-height:1.75;margin-top:8px}
.dp .daily{padding:32px 24px 36px;text-align:left}
.dp .daily .lab,.dp .daily h2{text-align:center}
.dp .daily .it{display:grid;grid-template-columns:20px 1fr auto;gap:0 10px;align-items:center;padding:12px 0;border-bottom:1px solid #E6E8E4}
.dp .daily .it:last-child{border-bottom:0}
.dp .daily .ok{width:20px;height:20px;border-radius:50%;background:var(--wc);display:flex;align-items:center;justify-content:center}
.dp .daily .ok.o{background:#fff;border:1.5px solid #C9D0D8}
.dp .daily .k{font-size:13px;font-weight:800;color:#111}
.dp .daily .k small{display:block;font-size:10.5px;color:#8A8A8A;font-weight:600;margin-top:1px}
.dp .daily .tag{font-size:9.5px;font-weight:800;color:var(--wc);white-space:nowrap}
.dp .daily .tag.o{color:#9AA3AE}
.dp .rep{margin:0 24px 28px;display:flex;align-items:center;gap:12px;border:1px solid #E6E8E4;border-radius:12px;padding:14px;text-align:left}
.dp .rep .t{flex:1;font-size:12.5px;font-weight:800;color:#111}
.dp .rep .t small{display:block;font-size:10.5px;color:#8A8A8A;font-weight:500}
.dp .fine2{padding:0 24px 24px;font-size:10px;color:#9AA3AE;line-height:1.5;text-align:left}
.dp .sec .own-in{outline-offset:0;padding:16px 10px 8px;margin-top:4px}
/* 옆 메모 */
.side{width:300px;font-size:12.5px;color:#3E444A;line-height:1.6}
.side h3{margin:0 0 8px;font-size:13px;font-weight:800;color:var(--ink)}
.side ol,.side ul{margin:0;padding-left:16px}
.side li{margin-bottom:6px}
.side .flag{display:inline-block;background:var(--amber-bg);color:var(--amber);font-weight:800;border-radius:3px;padding:0 5px;font-size:10.5px;margin-right:3px}
.side p{margin-bottom:8px}
.side p b{color:var(--ink)}
.side .nav{margin-top:14px;padding-top:10px;border-top:1px solid #D9DCD6;font-size:12px}
.side .nav a{color:var(--wc);text-decoration:none;font-weight:700}
.side .nav a+a{margin-left:8px}
@media (max-width:760px){.wrap{padding:12px 0 40px}.desc{border-radius:0}.phone{width:100%;border-radius:0;box-shadow:none}.side{width:auto;padding:16px}}
"""

CHK = '<svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
CHK14 = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"/></svg>'
BACK = '<button class="back" aria-label="뒤로 가기"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>'
STAR = '<svg width="13" height="13" viewBox="0 0 24 24" fill="#C77700" aria-hidden="true"><path d="M12 2l2.9 6.2 6.6.8-4.9 4.6 1.3 6.5L12 16.8 6.1 20l1.3-6.5L2.5 9l6.6-.8z"/></svg>'
DOC = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A3668" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>'
SPARK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="#0072CE" aria-hidden="true"><path d="M12 2l1.8 6.2L20 10l-6.2 1.8L12 18l-1.8-6.2L4 10l6.2-1.8zM19 16l.9 2.6L22.5 19.5l-2.6.9L19 23l-.9-2.6-2.6-.9 2.6-.9z"/></svg>'
PHONE_ICO = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#595959" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.6a2 2 0 0 1-.5 2.1L8.1 9.7a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.8.3 1.7.5 2.6.7a2 2 0 0 1 1.9 2z"/></svg>'
SAVE_ICO = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#595959" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>'
USER_ICO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0072CE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>'
PEN_ICO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0072CE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg>'

def fact(txt):
    return f'<div class="fact"><i>{CHK}</i>{txt}</div>'

# ───────────────────────────── 업종 공통 데이터 ─────────────────────────────
BIZ = {
'chicken': dict(
    key='치킨집', name='열한시 치킨', cat='치킨·닭강정', rating='4.7', rv='리뷰 2,041 · 성수동',
    tabs=['홈','메뉴','리뷰','사진','위생'], date='10.16', n=5, cta='이 가게 방역 알림 받기',
    report='2026-1016-0512', owner='박OO 사장님', owner_sub='성수동 17년',
    ai=['식어도 바삭하다는 말이 리뷰에 가장 자주 나와요. 사장님은 그 이유를 새 기름과 두 번 튀김이라고 적었어요.',
        '세스코가 10월 16일에 기름·닭·도마·손·공기 5가지를 직접 재서 모두 기준 안이었어요. 6회 연속이에요.',
        '사장님이 올린 매장 루틴 6개 중 4개를 이번 점검에서 세스코가 실제로 봤어요.'],
    hc=dict(pill='치킨집 공통 위생 포인트', hl='오늘 튀기는 기름, 산가까지 확인했어요',
            ds='생닭은 교차 오염이 생기기 쉽고, 오래 쓴 기름은 산패하기 쉬워요. 그래서 튀김유 산가, 생닭 보관 온도, 칼·도마 소독, 작업자 손 위생, 후드·배기 기름때를 집중해서 봐요.',
            metrics=[('튀김유 산가','0.8','',27,'기준 3.0 이하 (식품위생법 시행규칙)'),
                     ('생닭 냉장 온도','2','℃',40,'기준 0~5℃ · 24시간 센서'),
                     ('칼·도마 오염도','120','RLU',60,'관리 기준 200 이하 (ATP)'),
                     ('공기 중 부유세균','180','CFU/㎥',22,'기준 800 이하')],
            sum='<b>5개 항목 모두 기준 안</b>. 세스코 전문가가 10.16에 측정기(산가계·ATP·부유균)로 직접 쟀어요'),
    top3=[('월·수·금 새벽, 튀김 기름 전량 교체','새벽 4시 30분 · 폐유는 화요일 수거','세스코 확인'),
          ('생닭은 들어온 날 다 써요','아침 7시 입고 → 바로 염지 12시간 · 다음 날로 안 넘김','세스코 확인'),
          ('도마·칼은 색으로 구분','빨강은 생닭 전용, 하양은 완제품','세스코 확인')],
    daily=[(1,'튀김 기름 월·수·금 전량 교체','새벽 4시 30분','세스코 확인'),
           (1,'생닭 당일 소진','다음 날로 안 넘김','세스코 확인'),
           (1,'도마·칼 색 구분','빨강은 생닭 전용','세스코 확인'),
           (1,'후드 안쪽 청소','2주에 한 번 업체','세스코 확인'),
           (0,'홀 테이블 두 번 닦기','젖은 행주, 마른 행주','매장 기록'),
           (0,'포장 상자 구멍 두 개','김 빠지게','매장 기록')],
),
'meat': dict(
    key='고깃집', name='일도씨 정육식당', cat='돼지고기 구이·삼겹살', rating='4.6', rv='리뷰 1,318 · 마포',
    tabs=['홈','메뉴','리뷰','사진','위생'], date='10.14', n=5, cta='이 가게 방역 알림 받기',
    report='2026-1014-0287', owner='이재형 사장님', owner_sub='정육점 9년, 고기집 3년',
    ai=['리뷰에서 가장 많이 나오는 말은 "불판을 계속 바꿔 준다"예요. 손님마다 새 불판, 한 테이블에 세 번까지도요.',
        '세스코가 10월 14일에 숙성고·불판·집게·반찬 냉장·공기 5가지를 직접 재서 모두 기준 안이었어요. 4회 연속이에요.',
        '정육점 9년 하다 연 집이에요. 사장님이 적은 루틴 6개 중 4개를 이번 점검에서 세스코가 실제로 봤어요.'],
    hc=dict(pill='고깃집 공통 위생 포인트', hl='오늘 구워 드시는 고기, 보관 온도부터 확인했어요',
            ds='생고기는 교차 오염되기 쉽고 기름과 연기가 쌓이면 세균·해충이 번식하기 좋아져요. 축산물 품질, 반찬 재사용 금지, 조리도구 청결, 주방 조리 환경, 연기 속 유해물질 5가지를 집중 관리해요.',
            metrics=[('숙성고 온도','1','℃',10,'식육 냉장 기준 10℃ 이하 · 24시간 센서'),
                     ('세척 불판 오염도','90','RLU',45,'관리 기준 200 이하 (ATP)'),
                     ('집게·가위 오염도','110','RLU',55,'관리 기준 200 이하 (ATP)'),
                     ('공기 중 부유세균','260','CFU/㎥',32,'기준 800 이하')],
            sum='<b>5개 항목 모두 기준 안</b>. 세스코 전문가가 10.14에 측정기(온도계·ATP·부유균)로 직접 쟀어요'),
    top3=[('숙성고 1도, 사흘 규칙','입고일·부위·무게 손글씨 라벨 · 사흘 넘기면 안 냄','세스코 확인'),
          ('손님마다 새 불판','불판만 닦는 분이 오후 2시 출근 · 숯도 같이','세스코 확인'),
          ('남은 반찬은 그 자리에서 버려요','파절이는 다섯 시에 한 번 더 · 소분 냉장','세스코 확인')],
    daily=[(0,'입고 때 색·온도 확인','월요일 9시 사장님 직접 · 2도 넘으면 반품','매장 기록'),
           (1,'숙성고 사흘 규칙','입고일 라벨 · 사흘 넘기면 폐기','세스코 확인'),
           (1,'손님마다 새 불판','전담 세척 · 숯도 같이','세스코 확인'),
           (1,'남은 반찬 폐기 · 파절이 재무침','다섯 시 · 소분 냉장','세스코 확인'),
           (1,'집게 두 종류 안내','빨간 손잡이는 생고기용','세스코 확인'),
           (0,'후드 테이블별 · 소화기 둘','화덕 옆 · 올해 교체분 1','매장 기록')],
),
'care': dict(
    key='산후조리원', name='볕드는집 산후조리원', cat='산후조리원 · 민간형', rating='4.9', rv='후기 412 · 분당',
    tabs=['홈','프로그램','리뷰','사진','위생'], date='10.15', n=6, cta='이 조리원 방역 알림 받기',
    report='2026-1015-0341', owner='최OO 원장', owner_sub='신생아실 간호사 12년',
    ai=['후기에서 가장 많이 나오는 건 "방이 밝다"와 "태명으로 불러 준다"예요. 열두 방 전부 바깥 창이에요.',
        '세스코가 10월 15일에 신생아실 공기·젖병·수유실·좌욕기·조리실 6가지를 직접 재서 모두 기준 안이었어요. 8회 연속이에요.',
        '신생아실 공기 수치는 매달 복도에 붙어요. 숫자는 세스코가 재고, 원장님은 새 종이에 손으로 옮겨 적어요.'],
    hc=dict(pill='산후조리원 공통 위생 포인트', hl='신생아와 산모가 지내는 모든 공간, 전문 살균을 확인했어요',
            ds='면역이 약한 신생아와 산모가 2주를 지내는 곳이에요. 그래서 전문 살균, 신생아 용품 살균, 공기 살균, 비데 위생, 산모 식재료 위생 5가지를 집중해서 관리해요.',
            metrics=[('신생아실 부유세균','210','CFU/㎥',26,'산후조리원 유지기준 800 이하'),
                     ('젖병 내부 오염도','40','RLU',20,'소독 후 ATP · 관리 기준 200 이하'),
                     ('수유실 손잡이','90','RLU',45,'관리 기준 200 이하 (ATP)'),
                     ('산모식 조리대','110','RLU',55,'관리 기준 200 이하 · 냉장 3℃')],
            sum='<b>6개 항목 모두 기준 안</b>. 세스코 전문가가 10.15에 측정기(부유균 샘플러·ATP)로 직접 쟀어요'),
    top3=[('방 열두 개가 전부 바깥 창','환기는 오전 10시·오후 4시 방송으로','세스코 확인'),
          ('젖병은 아기마다 색 스티커','섞이지 않게 · 매일 고온 살균 · 퇴소 때 가져감','세스코 확인'),
          ('신생아실 공기 수치를 복도에 붙여요','매달 새 종이에 손글씨 · 숫자는 세스코','세스코 확인')],
    daily=[(0,'환기 방송','오전 10시 · 오후 4시','매장 기록'),
           (1,'침구 매일 · 속싸개 하루 두 번','세탁 카트 들어오는 문·나가는 문 분리','세스코 확인'),
           (1,'수유실 2시간마다 소독','체크표에 시간·사인','세스코 확인'),
           (1,'젖병 아기별 이름 스티커','섞이지 않게','세스코 확인'),
           (1,'공기청정기 필터 교체일 표시','신생아실 문에','세스코 확인'),
           (1,'좌욕기 사용 후 즉시 소독','순서표는 그림으로','세스코 확인')],
),
}

# ───────────────────────────── 공통 블록 ─────────────────────────────
def appbar(b):
    tabs = ''.join(f'<span class="{"on" if t=="위생" else ""}">{t}</span>' for t in b['tabs'])
    return f'''<div class="appbar">{BACK}<div class="t">{b['name']}</div></div>
<div class="head"><div class="nm"><h2>{b['name']}</h2><span class="cat">{b['cat']}</span></div>
<div class="rv">{STAR}<b>{b['rating']}</b><span>{b['rv']}</span></div>
<div class="tabs">{tabs}</div></div>'''

def ai_block(b):
    lis = ''.join(f'<li>{x}</li>' for x in b['ai'])
    return f'<div class="ai"><div class="lb">{SPARK}AI 요약<small>리뷰 · 세스코 리포트 · 사장님 기록 기준</small></div><ul>{lis}</ul></div>'

def hc_block(b, grid=False):
    h = b['hc']
    ms = ''
    for k, v, u, pct, base in h['metrics']:
        unit = f' <small>{u}</small>' if u else ''
        ms += f'<div class="m"><div class="k">{k}<i>적합</i></div><div class="v">{v}{unit}</div><div class="bar"><i style="width:{pct}%"></i></div><div class="b">{base}</div></div>'
    return f'''<div class="hc">
<div class="top"><div class="grade"><b>A</b><span>위생 등급</span></div><div class="t"><b>세스코 전문가 실측 · {b['date']} · {b['n']}가지 모두 기준 안</b><span>위생점검 리포트 No. {b['report']} · 다음 점검 11월</span></div></div>
<div class="pt"><span class="pill">{h['pill']}</span><small>CESCO 위쳌 기준</small><div class="hl">{h['hl']}</div><div class="ds">{h['ds']}</div></div>
{('<div class="grid">'+ms+'</div>') if grid else ''}
<div class="sum">{CHK14.replace('currentColor','#0072CE')}<div>{h['sum']}</div></div>
</div>'''

def report_row(b, cls='report'):
    return f'<div class="{cls}">{DOC}<div class="t">위생점검 리포트 No. {b["report"]}<small>세스코 전문가 현장 측정·서명 원본</small></div><a class="btn sec" href="#">원본 보기</a></div>'

def actions(b):
    return f'<div class="actions"><div class="ico">{PHONE_ICO}전화</div><div class="ico">{SAVE_ICO}저장</div><div class="cta">{b["cta"]}</div></div>'

FINE = '측정값은 점검일 기준이고, 다음 정기 점검 때 새로 바뀌어요. 매장 기록은 사장님이 적은 내용이고, 세스코 확인 표시가 있는 것만 이번 점검에서 실제로 봤어요.'

def top3_list(b, hd='사장님이 고른 세 가지', sub='업종 공통 항목 중 사업주가 상위 3개 선택'):
    rows = ''
    for i, (k, s, tag) in enumerate(b['top3'], 1):
        rows += f'<div class="row"><div class="num">{i}</div><div class="k">{k}<small>{s}</small></div><span class="tag">{tag}</span></div>'
    return f'<div class="card list own-in"><span class="own-tag">사업주 선택 TOP 3</span><div class="hd"><b>{hd}</b><span>{sub}</span></div>{rows}</div>'

def daily_list(b):
    rows = ''
    for ok, k, s, tag in b['daily']:
        okc = f'<div class="ok">{CHK}</div>' if ok else '<div class="ok o"></div>'
        tc = '' if ok else ' o'
        rows += f'<div class="row">{okc}<div class="k">{k}<small>{s}</small></div><span class="tag{tc}">{tag}</span></div>'
    return f'<div class="card list"><div class="hd"><b>매장이 매일 하는 일</b><span>사장님 기록</span></div>{rows}</div>'

LEGEND = '<div class="lg"><span><i style="background:#C77700"></i>주황 표식 = 사업주가 고르거나 적는 자리 (검토용, 실제 화면엔 안 보임)</span></div>'

PAGES = {}

def page(fname, title, desc, figcap, figsub, body_html, side_html, b, dp=False):
    inner = body_html if dp else f'<div class="body">{body_html}</div>'
    PAGES[fname] = dict(title=title, figcap=figcap, figsub=figsub, phone=f'{appbar(b)}\n{inner}\n{actions(b)}', side=side_html)
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>{FONT}<style>{CSS}</style></head>
<body><div class="wrap">
<div class="desc"><h1>{title}</h1><p>{desc} · <a href="index.html">9개 조합 비교로 돌아가기</a></p></div>
<div class="stage">
<figure><figcaption>{figcap}<small>{figsub}</small></figcaption>
<div class="phone"><div class="fold"><span>첫 화면 끝</span></div>
{appbar(b)}
{inner}
{actions(b)}
</div></figure>
<aside class="side">{side_html}</aside>
</div></div></body></html>'''
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', fname)

def nav(bk, tp):
    order = ['chicken','meat','care']
    links = []
    for t in 'ABC':
        if t == tp: continue
        links.append(f'<a href="{FN[bk][t]}">같은 업종 {t}안 →</a>')
    for k in order:
        if k == bk: continue
        links.append(f'<a href="{FN[k][tp]}">{BIZ[k]["key"]} {tp}안 →</a>')
    return '<div class="nav">' + ''.join(links) + '</div>'

FN = {
 'chicken': {'A':'위쳌_치킨집_A수치형_261028.html','B':'위쳌_치킨집_B인터뷰에디터형_261028.html','C':'위쳌_치킨집_C상세페이지형_261028.html'},
 'meat':    {'A':'위쳌_고깃집_A수치형_261028.html','B':'위쳌_고깃집_B인터뷰에디터형_261028.html','C':'위쳌_고깃집_C상세페이지형_261028.html'},
 'care':    {'A':'위쳌_산후조리원_A수치형_261028.html','B':'위쳌_산후조리원_B인터뷰에디터형_261028.html','C':'위쳌_산후조리원_C상세페이지형_261028.html'},
}

# ───────────────────────────── A안 · 수치형 ─────────────────────────────
A = {
'chicken': dict(
  gauges=[('튀김유 산가 · 바삭함의 기준','아주 바삭바삭해요','0.8','', '기준의 27% · 새 기름 수준',27,'0','기준선 3.0 (식품위생법)','기름이 산화되면 눅눅해지고 냄새가 나요. 월·수·금 새벽에 전량 교체하는 집이라 재면 늘 이 수준이에요.'),
          ('생닭 보관 온도','신선하게 보관되고 있어요','2','℃','0~5℃ 범위 안 · 24시간 센서',40,'0℃','5℃','온도가 오르면 세균이 빠르게 늘어요. 센서 기록을 보면 밤 세 시에도 2도 언저리예요.'),
          ('칼·도마 오염도','청결하게 관리되고 있어요','120','RLU','기준의 60%',60,'0','기준선 200','생닭을 만진 도마가 완제품에 닿으면 교차 오염이 생겨요. 빨간 도마는 생닭 전용이에요.'),
          ('조리하는 손','깨끗한 손으로 조리해요','60','RLU','기준의 30%',30,'0','기준선 200','손을 거친 교차 오염은 가장 흔한 경로예요. 닭을 만지면 바로 씻는 습관이 숫자로 보여요.'),
          ('공기 중 부유세균','주방 공기도 깨끗해요','180','CFU/㎥','기준의 23%',22,'0','기준선 800','튀김 연기와 습기 많은 주방은 공기 중 세균이 늘기 쉬워요. 후드 안쪽을 2주마다 닦는 집이에요.')],
  two=[('동네에서 보면','성수동 치킨집 <em>상위 3%</em>','위쳌 측정 94곳 중 3위'),('꾸준한지 보면','<em>6회 연속</em> 기준 통과','칼·도마 5월 190 → 10월 120 RLU')],
  hist=('튀김유 산가·칼·도마·공기', ['5월','6월','7월','8월','9월','10월'], ['튀김유 산가','칼·도마','공기']),
  memo='기름은 새벽에 갈아요. 점검 오시는 날도, 안 오시는 날도요.'),
'meat': dict(
  gauges=[('숙성고 온도','차갑게 숙성되고 있어요','1','℃','기준 10℃의 10분의 1 · 24시간 센서',10,'0℃','기준선 10℃','돼지고기는 온도가 오르면 육즙이 빠지고 세균이 늘어요. 사장님 폰 잠금화면이 이 숫자예요.'),
          ('세척 불판','새 불판처럼 깨끗해요','90','RLU','기준의 45%',45,'0','기준선 200','기름때가 남은 불판은 숫자가 튀어요. 손님마다 새 불판, 전담으로 닦는 분이 따로 계세요.'),
          ('생고기 집게·가위','교차 오염 없이 관리돼요','110','RLU','기준의 55%',55,'0','기준선 200','생고기 집게로 익은 고기를 집으면 교차 오염이 생겨요. 빨간 손잡이가 생고기용이에요.'),
          ('반찬 소분 냉장','당일 반찬만 나가요','4','℃','재사용 없음 · 오늘 날짜',40,'0℃','기준선 10℃','남은 반찬을 다시 내면 세균이 옮아요. 파절이는 다섯 시에 한 번 더 무쳐요.'),
          ('공기 중 부유세균','연기 많은 집치고 깨끗해요','260','CFU/㎥','기준의 32%',32,'0','기준선 800','고기 연기엔 초미세먼지와 기름 입자가 섞여 있어요. 테이블마다 후드가 내려오는 집이에요.')],
  two=[('동네에서 보면','마포 고깃집 <em>상위 5%</em>','위쳌 측정 112곳 중 6위'),('꾸준한지 보면','<em>4회 연속</em> 기준 통과','불판 7월 140 → 10월 90 RLU')],
  hist=('숙성고·불판·집게·공기', ['5월','6월','7월','8월','9월','10월'], ['숙성고','불판','공기']),
  memo='고기는 온도로 먹는 거예요. 숙성고 1도, 이틀째가 제일 맛있어요.'),
'care': dict(
  gauges=[('신생아실 부유세균','아기 방 공기가 깨끗해요','210','CFU/㎥','기준의 26% · 필터 지난주 교체',26,'0','유지기준 800','아기가 하루 종일 지내는 방이에요. 필터 교체일을 문에 적어 두는 조리원이에요.'),
          ('산모 방 부유세균','창 열어 두는 방이에요','190','CFU/㎥','기준의 24%',24,'0','유지기준 800','열두 방 전부 바깥 창이라 환기가 돼요. 오전 10시, 오후 4시에 방송으로 환기해요.'),
          ('젖병 내부','거의 0에 가까워요','40','RLU','기준의 20% · 소독 후',20,'0','기준선 200','젖병은 아기 입에 바로 닿아요. 아기마다 색 스티커로 구분해서 섞이지 않아요.'),
          ('수유실 손잡이 · 소파','손 닿는 곳도 깨끗해요','90','RLU','기준의 45% · 소파 120',45,'0','기준선 200','엄마들이 하루 여덟 번 드나드는 곳이에요. 2시간마다 소독하고 체크표에 사인해요.'),
          ('좌욕기','사용 후 바로 소독해요','70','RLU','기준의 35%',35,'0','기준선 200','회복 중인 산모 몸에 직접 닿아요. 소독 순서표가 그림으로 붙어 있어요.'),
          ('산모식 조리대 · 냉장','식사도 같은 기준이에요','110','RLU','기준의 55% · 냉장 3℃',55,'0','기준선 200','수유 중인 산모의 식사는 아기에게까지 닿아요. 미역국은 하루 두 번 새로 끓여요.')],
  two=[('동네에서 보면','분당 산후조리원 <em>상위 10%</em>','위쳌 측정 31곳 중 3위'),('꾸준한지 보면','<em>8회 연속</em> 기준 통과','신생아실 공기 3월 310 → 10월 210')],
  hist=('신생아실 공기·젖병·수유실', ['5월','6월','7월','8월','9월','10월'], ['신생아실 공기','젖병','수유실']),
  memo='숫자는 세스코가 재요. 저는 복도에 붙이기만 해요.'),
}

def build_A(bk):
    b, a = BIZ[bk], A[bk]
    g = ''
    for k, vd, v, u, pil, pct, l0, l1, why in a['gauges']:
        unit = f'<small>{u}</small>' if u else ''
        g += f'''<div class="r"><div class="k">{k}</div><div class="vd">{CHK14}{vd}</div>
<div class="mt"><div class="mrow"><b>{v}</b>{unit}<span class="pill2">{pil}</span></div><div class="mb"><i style="width:{pct}%"></i></div><div class="ml"><span>{l0}</span><span>{l1}</span></div></div>
<div class="why1"><b>왜 보나요?</b> {why}</div></div>'''
    two = ''.join(f'<div class="card"><div class="lb">{l}</div><div class="big">{bg}</div><div class="sm">{sm}</div></div>' for l, bg, sm in a['two'])
    cols, months, rows = a['hist']
    th = ''.join(f'<th class="{"now" if i==5 else ""}">{m}</th>' for i, m in enumerate(months))
    tr = ''
    for r in rows:
        tr += f'<tr><td>{r}</td>' + ''.join(f'<td class="{"now" if i==5 else ""}"><i></i></td>' for i in range(6)) + '</tr>'
    hist = f'<div class="card hist"><div class="lb">점검 이력</div><table><thead><tr><th></th>{th}</tr></thead><tbody>{tr}</tbody></table><div class="ft">월 1회 세스코 정기 점검 · {len(months)}회 연속 기준 통과 · 다음 점검 11월</div></div>'
    memo = f'<div class="card say own-in"><span class="own-tag">사업주 입력</span><div class="lb">사장님 한마디</div><p>"{a["memo"]}"</p><div class="sg">{b["owner"]} · 사업주가 직접 적는 한 줄 (선택)</div></div>'
    body = f'''{ai_block(b)}{hc_block(b, grid=True)}{LEGEND}
<div class="sh2"><b>항목별로 얼마나 여유 있나</b><small>{b['date']} 세스코 실측 · 값과 기준선</small></div>
<div class="res">{g}</div>
<div class="two">{two}</div>
{hist}
{top3_list(b, '이 집이 특히 신경 쓰는 세 가지')}
{memo}
{daily_list(b)}
{report_row(b)}
<p class="fine">{FINE}</p>'''
    side = f'''<h3>A안 · 수치형 — {b['key']}</h3>
<p>위생 정보 카드의 수치를 본문에서 <b>계기판·추이·동네 비교</b>로 다시 풀어 보여 줍니다. 수치가 곧 콘텐츠라 글을 거의 안 써도 되고 40만 사업장에 자동으로 깔 수 있습니다.</p>
<ol>
<li><b>항목별 계기판</b> — 값 · 기준의 몇 % · 0~기준선 눈금 · "왜 보나요?" 한 줄. 상단 카드와 같은 수치가 반복됩니다(10/28 결정과 상충, 비교용으로 그대로 둠).</li>
<li><b>동네 비교 · 연속 통과 · 점검 이력</b> — 수치형에서만 가능한 "꾸준함" 표현. 순위 수치는 예시.</li>
<li><span class="flag">사업주 선택</span>업종 공통 항목 중 상위 3개. 수치형에서는 체크리스트로만 보여 집마다 차이가 작게 보입니다.</li>
<li><span class="flag">사업주 입력</span>한 줄 멘트 하나. 사진 자리는 없습니다.</li>
</ol>
<p><b>장점</b> 근거가 또렷하고 자동 생성 가능. <b>단점</b> 상단 카드와 중복, 집마다 비슷해 보임, "왜 이 집인지"가 숫자 뒤에 숨음.</p>
{nav(bk,'A')}'''
    page(FN[bk]['A'], f'위쳌 사업장 상세 — {b["key"]} × A안 수치형 ({b["name"]}, 10/28)',
         '상단은 AI 요약 + 위생 정보 카드(기존 재사용), 본문은 수치 중심. 상호·수치·순위는 시안용 예시', f'A안 · {b["key"]} · {b["name"]}', '계기판 · 동네 비교 · 점검 이력 · 사업주 선택 3 · 매장 루틴', body, side, b)

# ───────────────────────────── B안 · 인터뷰·에디터형 ─────────────────────────────
B = {
'meat': dict(   # ★ 완성 라이팅
  eb='위쳌 에디터 방문기 · 10.14 점검 동행', h3='숙성고 온도가<br>폰 잠금화면인 사장님',
  who='일도씨 정육식당 · 이재형 사장님 · 글 위쳌 에디터 · 인터뷰는 녹음을 풀어 사장님이 확인했어요',
  hero_ph='사장님 사진 · 숙성고 앞, 고기 든 모습 · 세로',
  intro=['일도씨 정육식당은 마포 골목 안쪽, 테이블 여섯 개짜리 삼겹살집이에요. 간판에 \'정육식당\'이 붙은 건 사장님이 정육점을 9년 했기 때문이고, \'일도씨\'는 숙성고 온도예요. 1도. 단골들이 붙인 별명이 그대로 상호가 됐대요.',
         '10월 14일 오전 열 시, 세스코 점검에 따라 들어갔어요. 문 열기 일곱 시간 전이라 홀은 불이 꺼져 있고 주방만 환했어요. 사장님은 숙성고 앞에 서 있다가 "오늘은 2.4kg짜리가 제일 좋아요" 하고 먼저 말했어요. 물어보지도 않았는데요.'],
  pair=('숙성고 문 연 모습 · 1℃','손글씨 라벨 · 10/13 삼겹 4.2kg','글씨가 급해요. 월요일 아홉 시에 받으면서 쓴 거래요.'),
  intro2=['점검은 한 시간 반 걸렸어요. 전문가가 숙성고, 불판, 집게, 반찬 냉장고, 홀 공기 순서로 재는 동안 사장님은 뒤에서 팔짱을 끼고 보다가 숫자가 나올 때마다 "네" 했어요. 라디오는 두 시간 내내 켜져 있었고요. 숫자는 위에 카드로 있으니 여기선 안 적을게요. 대신 사장님한테 물어본 걸 그대로 옮겨요.'],
  pull=('"손님 자리에서 안 보이는 데가<br>전부예요."','이재형 사장님 · 정육점 9년, 고기집 3년'),
  qa=[('폰 잠금화면이 숙성고 온도라면서요.','네. (폰을 보여 주며) 지금 1.1이네요. 새벽에 깨면 이거부터 봐요. 2년 전에 정전으로 4도까지 올라간 적이 있어요. 그날 들어 있던 고기 다 뺐어요. 그 뒤로 센서 달고, 알림 오게 하고, 잠금화면으로요.','', '세스코 실측 · 숙성고 24시간 센서 기록 확인'),
      ('월요일 고기가 화요일에 제일 맛있다는 얘기를 들었어요.','정육점 할 때부터 그랬어요. 돼지는 1도에 두면 이틀째가 제일 쫀쫀해요. 사흘 넘어가면 육즙이 빠지기 시작해서 안 내요. 그래서 라벨에 날짜를 써요. 수요일 저녁에 월요일 고기가 남으면 직원들이 먹어요. (웃음) 그게 제일 아까워요.','숙성 설명은 사장님 경험담이에요. 위쳌이 사실로 단정하는 문장이 아니에요.',''),
      ('불판은 손님마다 바꿔요?','한 테이블에 세 번 바꿀 때도 있어요. 불판만 닦으시는 분이 두 시에 오세요. 오셔서 제일 먼저 불판을 세요. 마흔 장 아래면 저한테 문자가 와요.<br>— 오늘은 몇 장이에요?<br>마흔세 장이요.','', '세스코 실측 · 세척 불판 ATP 기준 안'),
      ('집게가 두 개 나오던데요.','빨간 손잡이가 생고기용이에요. 처음 오신 분한텐 직원이 말해 드려요. 근데 손님들이 자꾸 바꿔 쓰세요. 그래서 익은 고기는 저희가 거의 다 구워 드려요. 그게 제일 확실해요.','',''),
      ('파절이가 저녁에 더 맛있다는 리뷰가 있어요.','다섯 시에 한 번 더 무쳐요. 점심에 무친 건 그때 버리고요. 남은 반찬은 그 자리에서 다 버려요. 아까워도요. 정육점 할 때 반찬 다시 내는 집들 많이 봤거든요. 그게 싫어서 시작한 거라.','', '세스코 확인 · 남은 반찬 폐기 · 소분 냉장'),
      ('된장찌개는 왜 맛있어요?','어머니가 담근 된장이에요. 1년에 한 번 가져와요. 그 이상은 저도 몰라요. 여쭤봤는데 안 알려 주세요.','',''),
      ('정육점 때랑 뭐가 제일 달라요?','거기선 고기만 보면 됐어요. 여기는 손님 자리에서 안 보이는 데가 전부예요. 불판 닦는 데, 숙성고 안, 집게 통. 보이는 데는 손님이 봐 주시니까 괜찮아요.','','')],
  memo=('에디터 메모','나오는 길에 사장님이 문 앞까지 나왔어요. 저녁에 다시 가서 2인분 먹었어요. 두 번째 불판부터는 사장님이 직접 구워 주셨고, 삼겹살은 쫀득했어요. 된장찌개는 그냥 맛있었어요. 이유는 결국 못 물어봤어요. 라디오 주파수는 알려 주셨는데 그건 여기 안 적을게요.'),
  say='고기는 온도로 먹는 거예요. 숙성고 1도, 불판 새것, 반찬 새것. 이 세 개는 정육점 때부터 안 바꿨습니다.',
  say_ph='사장님이 올린 사진 · 선택 (예: 숙성고 라벨, 불판 더미)'),
'chicken': dict(
  eb='위쳌 에디터 방문기 · 10.16 점검 동행', h3='새벽 네 시 반,<br>기름부터 가는 집',
  who='열한시 치킨 · 박OO 사장님 · 글 위쳌 에디터 · 인터뷰는 녹음을 풀어 사장님이 확인했어요',
  hero_ph='사장님 사진 · 튀김기 앞, 앞치마 · 세로',
  intro=['열한시 치킨은 열한 시에 열어요. 사장님은 네 시 반에 나오고요. 기름 가는 날이라서. 월, 수, 금. 성수동 골목에서 17년째, 아버지가 열고 아들이 이어서 하는 집이에요. 테이블은 네 개뿐이고 손님 열에 일곱은 포장이에요이에요.',
         '10월 16일 세스코 점검에 따라갔어요. 주방은 네 평쯤, 튀김기 두 대, 라디오 하나. 사장님은 말수가 적어요. "네", "그렇죠". 기름이나 반죽 얘기만 나오면 길어져요.'],
  pair=('왼쪽 통 · 새벽에 간 기름','뒷골목 · 폐유통 세 개','왼쪽이 새벽에 간 기름. 눈금이 비쳐요.'),
  intro2=['수치는 위 카드에 있으니 여기엔 안 적어요. 사장님이 한 말만 옮길게요.'],
  pull=('"말로 하면 안 지켜져요.<br>색이 있어야 돼요."','박OO 사장님 · 성수동 17년'),
  qa=[('기름 가는 날은 알람이 세 개라면서요.','네 시, 네 시 십 분, 네 시 이십 분. 작년에 한 번 늦잠 자서 열 시에 갈았는데 단골이 "오늘 좀 다르네" 하더라고요. 그 뒤로 세 개예요.','', '세스코 실측 · 튀김유 산가 새 기름 수준'),
      ('도마가 빨간 건요.','생닭은 빨강, 완제품은 하양. 칼도 빨간 테이프. 직원이 헷갈리니까요. 말로 하면 안 지켜져요.','', '세스코 실측 · 칼·도마 ATP 기준 안'),
      ('금요일 저녁에 일찍 닫을 때가 있던데요.','닭이 떨어져서요. 아침 일곱 시에 들어온 닭을 그날 다 써요. 남으면 다음 날 안 써요. 손님은 헛걸음이죠. 죄송한데 그건 못 바꿔요.','',''),
      ('단골 주문을 다 외우세요?','목소리로요. 번호는 못 외워요. "늘 먹던 걸로요" 하면 알아요.','',''),
      ('손등 자국은요.','17년이면 이 정도는.','','')],
  memo=('에디터 메모','점검 끝나고 한 마리 시켰어요. 껍질에서 소리가 나요. 반쯤 남겨 포장했는데 상자 뚜껑에 송곳으로 구멍 두 개를 더 뚫어 주셨어요. 김 빠지라고. 저녁에 먹었는데 괜찮았어요. 저는 순살파인데 여기는 뼈로 드세요.'),
  say='기름은 새벽에 갈아요. 점검 오시는 날도, 안 오시는 날도요.',
  say_ph='사장님이 올린 사진 · 선택 (예: 새벽 기름 교체, 손글씨 메뉴판)'),
'care': dict(
  eb='위쳌 에디터 방문기 · 10.15 점검 동행', h3='복도 끝 A4 한 장,<br>숫자는 세스코 글씨는 원장님',
  who='볕드는집 산후조리원 · 최OO 원장 · 글 위쳌 에디터 · 인터뷰는 녹음을 풀어 원장님이 확인했어요',
  hero_ph='원장님 사진 · 신생아실 창 앞 · 세로',
  intro=['볕드는집은 분당에 있는 방 열두 개짜리 민간 조리원이에요. 원장님은 신생아실 간호사를 12년 했어요. 2층 복도 끝에 A4 한 장이 붙어 있는데, 신생아실 공기 수치예요. 매달 세스코가 재면 원장님이 새 종이에 손으로 옮겨 적어요.',
         '10월 15일, 그 숫자가 어떻게 나오는지 보러 갔어요. 두 시간 동안 원장님 목소리가 한 번도 안 올라갔어요. 제가 같은 걸 두 번 물어도요.'],
  pair=('2층 복도 끝 · A4 한 장','산모 방 창가 · 오후 햇빛','블라인드를 반만 내렸는데도 이만큼.'),
  intro2=['수치는 위 카드에 있어요. 여기엔 원장님 말만 옮길게요.'],
  pull=('"제가 쓰면<br>그건 광고잖아요."','최OO 원장 · 신생아실 간호사 12년'),
  qa=[('복도 A4는 왜 새 종이로 바꾸세요? 위에 쓰면 되는데.','지난달 숫자 위에 덧쓰면 지저분하잖아요. 그리고 제가 쓰면 그건 광고고요. 숫자는 세스코가 재고, 저는 옮겨 적기만 해요.','', '세스코 실측 · 신생아실 공기 매달 측정'),
      ('방이 넓던데요. 창도 다 있고.','건물 고를 때 그것만 봤어요. 햇볕 안 드는 방에서 2주 있으면 사람이 처져요. 환기는 열 시, 네 시에 방송으로 해요. 체크표 말고 방송으로요.','',''),
      ('젖병 스티커 색은 누가 골라요?','엄마들이요. 분홍이 제일 많아요. 아기마다 색이 달라서 안 섞여요. 퇴소할 때 가져가는 분이 많아요.','', '세스코 실측 · 젖병 내부 ATP 거의 0'),
      ('태명을 다 외우세요?','일곱 명이니까요. 열두 명일 때도요. 퇴소하고 1년 뒤에 오셔도 태명으로 기억해요.','',''),
      ('간호사 때 제일 불편했던 게 뭐였어요?','수유실 소파요. 그래서 여기 소파는 깊어요. 두 시간마다 닦고요.','','')],
  memo=('에디터 메모','10분 동안 아기 한 명이 깼고, 간호사분이 안아서 재웠어요. 엄마들은 밤 두 시에 폰으로 이 방을 제일 많이 본대요. 미역국에 들기름이 많았어요. 그건 위생이 아니라 그냥 맛있으라고요. 다음 달이면 복도 종이가 새것으로 바뀌어요.'),
  say='숫자는 세스코가 재요. 저는 복도에 붙이기만 해요.',
  say_ph='원장님이 올린 사진 · 선택 (예: 복도 A4, 젖병 스티커)'),
}

def build_B(bk, full=False):
    b, d = BIZ[bk], B[bk]
    ps = ''.join(f'<p>{p}</p>' for p in d['intro'])
    p1, p2, cap = d['pair']
    ps2 = ''.join(f'<p>{p}</p>' for p in d['intro2'])
    qa = ''
    for q, a, sm, fc in d['qa']:
        small = f'<small>{sm}</small>' if sm else ''
        qa += f'<div class="it"><div class="q">{q}</div><div class="a">{a}{small}</div>{fact(fc) if fc else ""}</div>'
    mt, mb = d['memo']
    body = f'''{ai_block(b)}{hc_block(b)}{LEGEND}
<div class="iv-hero own-in"><span class="own-tag">사업주 사진 (없으면 점검 때 촬영)</span><div class="ph">{d['hero_ph']}</div><div class="eb">{d['eb']}</div><h3>{d['h3']}</h3><div class="who">{d['who']}</div></div>
<div class="card intro">{ps}<div class="pair"><div class="ph sq">{p1}</div><div class="ph sq">{p2}</div></div><div class="cap2">{cap}</div>{ps2}</div>
<div class="pull"><p>{d['pull'][0]}</p><span>{d['pull'][1]}</span></div>
<div class="card iv">{qa}</div>
<div class="card intro"><div class="byline"><div class="av">{PEN_ICO}</div><div><b>{mt}</b><span>점검 동행 · {b['date']}</span></div></div><p style="margin-top:8px">{mb}</p></div>
{top3_list(b)}
<div class="card say own-in"><span class="own-tag">사업주 입력</span><div class="lb">사장님 한마디</div><p>"{d['say']}"</p><div class="sg">{b['owner']} · 사업주가 직접 적는 한 줄 (선택)</div><div class="ph">{d['say_ph']}</div></div>
{daily_list(b)}
{report_row(b)}
<p class="fine">{FINE} 방문기는 위쳌 에디터가 점검에 동행해 쓴 글이에요.</p>'''
    star = ' ★ 완성 라이팅' if full else ''
    side = f'''<h3>B안 · 인터뷰·에디터형 — {b['key']}{star}</h3>
<p>수치는 상단 카드에 두고, 본문은 <b>에디터 방문기 + 사장님 문답</b>으로 "왜 이 집이 관리되는지"를 사람 말로 전달합니다. 위생 사실이 답에 섞여 나올 때만 파란 팩트 칩을 붙이고 숫자는 다시 쓰지 않습니다.</p>
<ol>
<li><b>방문기 도입</b> 2~3문단 + 글 중간 사진 두 장. 점검 동행 장면이라 "세스코가 봤다"는 근거가 글 자체에 있습니다.</li>
<li><b>인용 한 줄 + 문답 {len(d['qa'])}개</b>. 질문은 업종별 질문 풀에서 사장님이 고른 것. 위생 밖 질문(된장찌개·태명·손등)이 하나 이상.</li>
<li><span class="flag">사업주 선택</span>문답 아래 "사장님이 고른 세 가지". 업종 공통 항목 8~10개 중 상위 3개.</li>
<li><span class="flag">사업주 입력</span>헤드 사진 1장, 한마디 1줄, 사진 1장(선택). 비어 있으면 점검 때 전문가가 찍은 사진과 인용으로 채웁니다.</li>
</ol>
<p><b>장점</b> 집마다 다른 글이 나오고 생성문 티가 가장 적음. 위생이 자랑이 아니라 이야기의 증거로 읽힘. <b>단점</b> 전문가 현장 양식(본 것·잰 것·사장님 말·질문 2~3개)이 비면 못 쓰고, 사장님 확인 단계가 필요.</p>
{'<p><b>이 조합을 완성 라이팅으로 고른 이유</b> — 고깃집은 숙성고 온도·불판·반찬처럼 사장님이 매일 손으로 하는 일이 많아 문답만으로도 위생 근거가 자연스럽게 따라 나오고, 상호(일도씨)·잠금화면·마흔세 장 같은 고유 디테일이 생성문 티를 가장 잘 지웁니다.</p>' if full else ''}
{nav(bk,'B')}'''
    page(FN[bk]['B'], f'위쳌 사업장 상세 — {b["key"]} × B안 인터뷰·에디터형 ({b["name"]}, 10/28){star}',
         '상단은 AI 요약 + 위생 정보 카드(기존 재사용), 본문은 에디터 방문기 + 사장님 문답. 상호·인터뷰는 시안용 창작' + (' · 이 조합은 실제 게시 수준까지 라이팅을 완성한 1차본' if full else ''),
         f'B안 · {b["key"]} · {b["name"]}{star}', '방문기 · 인용 · 문답 · 사업주 선택 3 · 사장님 한마디 · 매장 루틴', body, side, b)

# ───────────────────────────── C안 · 상세페이지형 (M안 틀) ─────────────────────────────
C = {
'chicken': dict(
  hero=('사진 자리 · 갓 튀긴 후라이드 · 세로 클로즈업','성수동 · 17년','새벽 네 시 반,<br>기름부터 갑니다','열한시 치킨 · 세스코 위생 실측 A'),
  about=('아버지가 열고,<br>아들이 잇는 집','성수동 골목에서 17년. 테이블은 네 개뿐이고 손님 열에 일곱은 포장이에요이에요. 벽 메뉴판은 손글씨고 가격은 3년째 그대로. 반죽 비율은 아버지 때 그대로라는데, 그건 안 알려줘요.'),
  strip=[('영업','11:00~22:00<br>월 휴무'),('메뉴','후라이드<br>양념·반반'),('이용','홀 4테이블<br>포장·배달'),('주차','없음<br>공영 3분')],
  pt_h='바삭함에는<br>이유가 세 가지 있어요',
  pts=[('사진 자리 · 튀김기 두 대 · 맑은 기름','월·수·금 새벽,<br>기름 전량 교체','문은 열한 시에 여는데 사장님은 네 시 반에 나와요. 알람 세 개. 작년 여름 한 번 늦잠 자서 열 시에 갈았더니 단골이 그날 "오늘 좀 다르네" 했대요.','세스코 실측 · 튀김유 산가 새 기름 수준'),
       ('사진 자리 · 냉장고 안 · 염지 중인 10호 닭','들어오자마자 염지,<br>그날 다 써요','아침 일곱 시에 들어온 닭을 바로 염지해서 냉장고에 열두 시간. 그날 못 쓴 닭은 다음 날 안 써요. 금요일 저녁에 가끔 일찍 닫는 이유.','세스코 실측 · 생닭 냉장 24시간 센서'),
       ('사진 자리 · 빨간 도마 · 빨간 테이프 칼','도마도 칼도<br>색으로 나눠요','생닭은 빨강, 완제품은 하양. 칼도 빨간 테이프. "말로 하면 안 지켜져요. 색이 있어야 돼요." 직원이 바뀌어도 이건 안 바뀌어요.','세스코 실측 · 칼·도마 ATP 기준 안')],
  qt=('사진 자리 · 사장님 · 튀김기 앞, 앞치마','"말로 하면 안 지켜져요.<br>색이 있어야 돼요."','박OO 사장님 · 성수동 17년'),
  qa=[('Q. 단골 주문을 다 외우세요?','목소리로요. 번호는 못 외워요. "늘 먹던 걸로요" 하면 알아요.'),('Q. 손등 자국은요.','17년이면 이 정도는.')],
  say='기름은 새벽에 갈아요. 점검 오시는 날도, 안 오시는 날도요.'),
'meat': dict(
  hero=('사진 자리 · 불판 위 삼겹살 · 육즙 · 세로','마포 · 정육점 9년, 고기집 3년','고기는<br>온도로 먹는 거예요','일도씨 정육식당 · 세스코 위생 실측 A'),
  about=('숙성고 온도가<br>폰 잠금화면인 사장님','마포 골목 안쪽, 테이블 여섯 개. 정육점 9년 하다 연 지 3년이에요. 상호의 \'일도\'는 숙성고 온도. 단골들이 붙인 별명이 그대로 간판이 됐어요. 사장님은 새벽에 깨면 폰부터 본대요.'),
  strip=[('영업','17:00~23:00<br>일 휴무'),('메뉴','삼겹·목살<br>된장찌개'),('이용','홀 6테이블<br>참숯·예약'),('주차','없음<br>골목 주차')],
  pt_h='쫀득함에는<br>이유가 세 가지 있어요',
  pts=[('사진 자리 · 숙성고 안 · 손글씨 라벨','숙성고 1도,<br>이틀째가 제일 맛있어요','입고일·부위·무게를 손으로 적어요. 월요일엔 사장님이 직접 받아서 온도계를 찔러 보고요. 1도에서 이틀째가 제일 쫀쫀하다는 게 사장님 말. 사흘 넘기면 안 내요.','세스코 실측 · 숙성고 24시간 센서'),
       ('사진 자리 · 세척된 불판 마흔세 장','손님마다<br>새 불판','한 테이블에 세 번 바꿀 때도 있어요. 불판 설거지만 하시는 분이 두 시에 오세요. 그 인건비가 저희 맛이라고 사장님이 그래요. 숯도 불판 바꿀 때 같이 뒤집어요.','세스코 실측 · 세척 불판 ATP 기준 안'),
       ('사진 자리 · 파절이 통 · 오늘 날짜','파절이는<br>다섯 시에 한 번 더','남은 반찬은 그 자리에서 버려요. 소분한 파절이는 냉장에 오늘 날짜. "저녁 파절이가 더 맛있다"는 리뷰가 그래서 있어요.','세스코 확인 · 반찬 재사용 없음 · 소분 냉장')],
  qt=('사진 자리 · 사장님 · 숙성고 앞, 고기 든 모습','"손님 자리에서 안 보이는 데가<br>전부예요."','이재형 사장님 · 정육점 9년, 고기집 3년'),
  qa=[('Q. 된장찌개 맛있다는 리뷰가 많던데요.','어머니가 담근 된장이에요. 1년에 한 번 가져와요. 그 이상은 저도 몰라요.'),('Q. 정육점 때랑 뭐가 달라요?','거기선 고기만 보면 됐어요. 여기는 손님 자리에서 안 보이는 데가 전부예요.')],
  say='고기는 온도로 먹는 거예요. 숙성고 1도, 불판 새것, 반찬 새것.'),
'care': dict(
  hero=('사진 자리 · 산모 방 창가 · 오후 햇빛 · 세로','분당 · 12실 · 간호사 출신 원장','엄마가 못 보는 곳을<br>대신 봤어요','볕드는집 산후조리원 · 세스코 위생 실측 A'),
  about=('복도 끝 A4 한 장,<br>숫자는 세스코, 글씨는 원장님','분당에 있는 방 열두 개짜리 민간 조리원이에요. 원장님은 신생아실 간호사 12년. 매달 세스코가 재고 가면 신생아실 공기 수치를 새 종이에 손으로 써서 복도에 붙여요. "제가 쓰면 그건 광고잖아요."'),
  strip=[('이용','2주 기본<br>모자동실 선택'),('식사','하루 5식<br>미역국 요일별'),('면회','창 너머<br>폰 CCTV 24h'),('프로그램','좌욕·마사지<br>목욕 11시')],
  pt_h='2주를 사는 곳이라<br>이 세 가지를 봐요',
  pts=[('사진 자리 · 산모 방 · 창가 햇빛 · 전동침대','방 열두 개가<br>전부 바깥 창','제일 작은 방이 여섯 평. 환기는 열 시, 네 시에 방송으로. 제왕절개 산모 방엔 전동침대가 있어요. 배에 힘 주지 않고 리모컨으로 등을 세우라고.','세스코 실측 · 산모 방 공기 기준 안'),
       ('사진 자리 · 젖병 소독기 · 색색 스티커','젖병은 아기마다<br>색 스티커','색은 엄마가 골라요. 분홍이 제일 많대요. 매일 고온 살균하고, 퇴소할 때 다들 가져가요. 콩이 엄마, 복댕이 엄마. 열두 명일 때도 태명을 다 외워요.','세스코 실측 · 젖병 내부 ATP 거의 0'),
       ('사진 자리 · 2층 복도 끝 · A4 한 장','공기 수치를<br>매달 복도에 붙여요','지난달 숫자 위에 덧쓰지 않고 새 종이로. 숫자는 세스코가 재고 원장님은 옮겨 적기만 해요. 엄마는 못 들어가는 신생아실, 밤 두 시에 폰으로 제일 많이 본대요.','세스코 실측 · 신생아실 공기 매달 측정')],
  qt=('사진 자리 · 원장님 · 신생아실 창 앞','"제가 쓰면<br>그건 광고잖아요."','최OO 원장 · 신생아실 간호사 12년'),
  qa=[('Q. 방이 넓던데요. 창도 다 있고.','건물 고를 때 그것만 봤어요. 햇볕 안 드는 방에서 2주 있으면 사람이 처져요.'),('Q. 미역국에 들기름이 많던데요.','하루 두 번 끓여요. 그건 위생이 아니라 그냥 맛있으라고요.')],
  say='숫자는 세스코가 재요. 저는 복도에 붙이기만 해요.'),
}

def build_C(bk):
    b, d = BIZ[bk], C[bk]
    hp, hl, hh, hs = d['hero']
    ah, ap = d['about']
    strip = ''.join(f'<div><b>{k}</b><span>{v}</span></div>' for k, v in d['strip'])
    pts = ''
    for i, (ph, h3, p, fx) in enumerate(d['pts'], 1):
        alt = ' alt' if i % 2 == 0 else ''
        pts += f'<div class="pt{alt}"><span class="own-tag">사업주 선택 {i}</span><div class="pho">{ph}</div><div class="tx"><div class="num">POINT 0{i}</div><h3>{h3}</h3><p>{p}</p><div class="fx"><i>{CHK}</i>{fx}</div></div></div>'
    qp, qq, qb = d['qt']
    qa = ''.join(f'<div class="it"><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a in d['qa'])
    daily = ''
    for ok, k, s, tag in b['daily']:
        okc = f'<div class="ok">{CHK}</div>' if ok else '<div class="ok o"></div>'
        daily += f'<div class="it">{okc}<div class="k">{k}<small>{s}</small></div><span class="tag{"" if ok else " o"}">{tag}</span></div>'
    body = f'''<div class="body" style="padding-bottom:12px">{ai_block(b)}{hc_block(b)}{LEGEND}</div>
<div class="dp">
<div class="hr own-in"><span class="own-tag" style="top:10px;right:14px">사업주 사진 · 세로 1장</span><div class="pho">{hp}</div><div class="ov"><span class="lab">{hl}</span><h1>{hh}</h1><div class="sub">{hs}</div></div></div>
<div class="sec"><span class="lab">ABOUT</span><h2>{ah}</h2><div class="own-in"><span class="own-tag">사업주 입력 · 소개 문구 (비면 업종 기본 문구)</span><p>{ap}</p></div><div class="strip">{strip}</div></div>
<div class="sec alt" style="padding-bottom:10px"><span class="lab">POINT</span><h2>{d['pt_h']}</h2><p style="font-size:11.5px;color:#8A8A8A;margin-top:-6px">업종 공통 특장점 중 사업주가 고른 세 가지 · 세스코가 본 것만 체크 표시</p></div>
{pts}
<div class="qt"><div class="pho">{qp}</div><div class="ov"><span class="lab">INTERVIEW</span><div class="q">{qq}</div><div class="by">{qb}</div></div></div>
<div class="qa">{qa}<div class="it own-in" style="padding:14px 10px"><span class="own-tag">사업주 입력 · 한마디</span><div class="q">사장님 한마디</div><div class="a">"{d['say']}"</div></div></div>
<div class="daily alt"><span class="lab">EVERY DAY</span><h2>매장이 매일 하는 일</h2>{daily}</div>
<div style="height:28px"></div>
{report_row(b,'rep')}
<p class="fine2">{FINE} 위생 수치는 맨 위 카드 한 곳에만 있어요.</p>
</div>'''
    side = f'''<h3>C안 · 상세페이지형 — {b['key']}</h3>
<p>브랜드 상세페이지처럼 사진이 화면 가득 깔리고 큰 제목과 짧은 카피가 내려오는 구성(10/28 M안 틀). 수치는 맨 위 카드에만 두고, 본문은 <b>소개 → 특장점 3 → 인터뷰 → 매일 하는 일</b>로 "이 집이 다른 이유"만 보여 줍니다. M안에 있던 검정 스펙표(CESCO CHECK)는 상단 카드와 겹쳐 뺐습니다.</p>
<ol>
<li><b>히어로</b> 세로 사진 1장 + 한 줄 카피. <span class="flag">사업주 사진</span>없으면 점검 때 촬영한 대표 컷.</li>
<li><b>ABOUT</b> <span class="flag">사업주 입력</span>소개 두세 문장. 비어 있으면 업종 기본 문구("성수동 17년 치킨집이에요")로 자동 채움. 영업·메뉴·이용·주차는 등록 정보.</li>
<li><b>POINT 01~03</b> <span class="flag">사업주 선택</span>업종 공통 특장점 8~10개 중 상위 3개. 제목·카피는 항목별 기본 문안이 있고, 사장님 말이 있으면 바꿔 넣습니다. 세스코가 본 항목만 파란 칩.</li>
<li><b>INTERVIEW</b> 인용 1 + 문답 2. 전문가 현장 양식의 "사장님이 한 말 1줄"이 인용이 됩니다. <span class="flag">사업주 입력</span>한마디 1줄.</li>
</ol>
<p><b>장점</b> 가장 "마케팅 페이지"답고 사진이 일을 함. 선택 항목 구조라 40만 사업장에 자동 적용 가능. <b>단점</b> 세로 사진 5장이 필요하고, 사진이 없으면 회색 상자가 길게 남음. 기본 문안만 쓰면 B안보다 집마다 비슷해 보임.</p>
{nav(bk,'C')}'''
    page(FN[bk]['C'], f'위쳌 사업장 상세 — {b["key"]} × C안 상세페이지형 ({b["name"]}, 10/28)',
         '상단은 AI 요약 + 위생 정보 카드(기존 재사용), 본문은 M안 풀블리드 상세페이지 틀. 상호·인터뷰는 시안용 창작', f'C안 · {b["key"]} · {b["name"]}', '히어로 · ABOUT · POINT 01~03(사업주 선택) · INTERVIEW · EVERY DAY', body, side, b, dp=True)

# ───────────────────────────── index ─────────────────────────────
OPTS = {
'치킨집': ['튀김 기름 교체 주기 (요일·시간)','생닭 당일 소진 · 입고 시간','염지·숙성 방식과 시간','도마·칼 색 구분 (생닭 전용)','두 번 튀김 · 조리 온도','후드·덕트 청소 주기','포장 방식 (김 빠지는 구멍 등)','닭 호수·원산지 표시','홀 테이블·소스통 관리','배달 용기 밀봉 · 위생 장갑'],
'고깃집': ['숙성고 온도 · 숙성 일수 규칙','입고 검수 (사장님 직접 · 반품 기준)','불판 교체 기준 (손님마다 · 횟수)','집게·가위 생고기/익은 고기 분리','남은 반찬 폐기 · 소분 냉장','숯·화덕 관리 (교체 시점)','테이블 후드 · 연기 관리','축산물 등급판정서 · 원산지 게시','직접 담근 재료 (된장·김치)','홀 환기 · 공기청정기'],
'산후조리원': ['신생아실 공기 수치 공개 (복도 게시)','젖병·수건 아기별 구분 · 고온 살균','산모 방 창·환기 (방송·시간)','면회·출입 관리 (창 너머 · CCTV)','수유실 소독 주기 · 체크표','침구·세탁 동선 분리','산모식 식재료 · 조리실 관리','좌욕기·비데 사용 후 소독','신생아실 야간 운영 · 조명','간호 인력 (간호사 출신 원장 등)'],
}

def build_index():
    rows = ''
    for bk in ['chicken','meat','care']:
        b = BIZ[bk]
        tds = ''
        for t, nm in [('A','수치형'),('B','인터뷰·에디터형'),('C','상세페이지형')]:
            star = ' <span class="st done">완성 라이팅</span>' if (bk=='meat' and t=='B') else ''
            tds += f'<td><a class="chip" href="{FN[bk][t]}" target="_blank"><span class="type">{t}안 · {nm}</span>{b["name"]}</a>{star}</td>'
        rows += f'<tr><td><b>{b["key"]}</b><br><span class="small">{b["name"]} · {b["rv"]}</span></td>{tds}</tr>'
    opts = ''
    for k, lst in OPTS.items():
        lis = ''.join(f'<li>{x}</li>' for x in lst)
        opts += f'<div class="opt"><b>{k} · {len(lst)}개</b><ol>{lis}</ol></div>'
    doc = f'''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 사업장 상세 풀페이지 9종 비교 (10/28)</title>{FONT}
<style>
:root{{--ink:#111;--ink2:#444;--ink3:#777;--line:#e3e3e3;--soft:#f5f7fa;--blue:#0072CE;--blue-soft:#e6f1fb;--amber:#b35c00;--amber-soft:#fff4e5;--green:#1b7f3b;--green-soft:#e8f5ec}}
*{{box-sizing:border-box}}
html,body{{margin:0;background:#fff;color:var(--ink);font-family:"Pretendard Variable",Pretendard,-apple-system,"Malgun Gothic","Apple SD Gothic Neo",sans-serif;font-size:15px;line-height:1.65;word-break:keep-all}}
.wrap{{max-width:960px;margin:0 auto;padding:48px 24px 80px}}
header.top{{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:28px}}
.kicker{{font-size:13px;letter-spacing:.02em;color:var(--blue);font-weight:700;margin-bottom:6px}}
h1{{font-size:26px;line-height:1.3;margin:0 0 10px;font-weight:800}}
.meta{{display:flex;flex-wrap:wrap;gap:6px 22px;color:var(--ink2);font-size:14px}}
.meta b{{color:var(--ink);font-weight:600}}
h2{{font-size:19px;margin:40px 0 12px;padding-top:18px;border-top:1px solid var(--line);font-weight:800;display:flex;align-items:baseline;gap:10px}}
h2 .num{{color:var(--blue);font-size:15px;font-weight:800;min-width:2ch}}
p{{margin:0 0 10px}}
.lead{{font-size:16px;color:var(--ink2)}}
ul,ol{{margin:0 0 10px;padding-left:22px}}
li{{margin:3px 0}}
table{{width:100%;border-collapse:collapse;font-size:14px;margin:10px 0 16px}}
th,td{{border-bottom:1px solid var(--line);padding:9px 10px;text-align:left;vertical-align:top}}
th{{background:var(--soft);font-weight:700;font-size:13px;color:var(--ink2);white-space:nowrap}}
.small{{font-size:12.5px;color:var(--ink3)}}
.box{{border:1px solid var(--line);border-left:4px solid var(--blue);border-radius:6px;background:var(--soft);padding:14px 18px;margin:14px 0}}
.box.amber{{border-left-color:var(--amber);background:var(--amber-soft)}}
.box b.h{{display:block;margin-bottom:6px}}
.chip{{display:inline-flex;flex-direction:column;align-items:flex-start;gap:1px;line-height:1.25;padding:6px 12px;border:1px solid var(--blue);border-radius:999px;background:var(--blue-soft);color:var(--blue);font-size:12.5px;font-weight:600;text-decoration:none;white-space:nowrap}}
.chip .type{{font-size:10px;font-weight:600;opacity:.75;letter-spacing:.02em}}
.st{{display:inline-block;font-size:11px;font-weight:700;padding:1px 8px;border-radius:4px;white-space:nowrap;vertical-align:middle;margin-left:4px}}
.st.done{{background:var(--green-soft);color:var(--green)}}
.tbl{{overflow-x:auto}}
.tbl table{{min-width:640px}}
.opts{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.opt{{border:1px solid var(--line);border-radius:8px;padding:12px 14px;font-size:13.5px}}
.opt b{{display:block;margin-bottom:6px}}
.opt ol{{padding-left:20px;margin:0}}
.opt li{{margin:2px 0}}
.foot{{margin-top:48px;padding-top:14px;border-top:1px solid var(--line);color:var(--ink3);font-size:12.5px}}
.need{{color:var(--amber);font-weight:700}}
@media (max-width:720px){{.wrap{{padding:28px 16px 60px}}h1{{font-size:22px}}table{{font-size:13px}}th,td{{padding:7px 6px}}.opts{{grid-template-columns:1fr}}.chip{{white-space:normal}}}}
</style></head>
<body><div class="wrap">
<header class="top"><div class="kicker">세스코 WeCheck(위쳌) · 사업장 상세 페이지 1차본</div>
<h1>업종 3 × 유형 3 = 모바일 풀페이지 9종 비교</h1>
<div class="meta"><span><b>기준일</b> 2026-10-28 (수)</span><span><b>용도</b> 이번 주말~다음 주 초 세스코 1차 공유 · 11/4(수) 이사님 보고</span><span><b>작성</b> 시하 W. 김선희</span><span><b>이전 자료</b> <a href="../261026/index.html">10/28 보고 자료</a></span></div></header>

<p class="lead">10/28 미팅 결정대로 본문은 상단 <b>위생 정보 카드</b>가 보여 주는 수치를 반복하지 않고 <b>"이 사업장이 왜 위생적으로 관리되는지, 다른 사업장과 무엇이 다른지"</b>를 전달하는 역할에 집중했습니다. 9개 모두 실제 서비스 화면(모바일 390px) 기준이고, 상단에는 AI 요약과 위생 정보 카드(10/27 사업장 상세 시안의 공통 카드 + 실측 2열을 위쳌 파란색으로 재사용)를 그대로 올렸습니다. 사업주가 고르거나 적는 자리는 <span class="need">주황 표식</span>으로 표시했고, 실제 화면에는 보이지 않습니다.</p>

<div class="box"><b class="h">완성 라이팅으로 고른 조합 — 고깃집 × B안(인터뷰·에디터형)</b>고깃집은 숙성고 온도·불판·반찬처럼 사장님이 매일 손으로 하는 일이 많아 문답만으로 위생 근거가 자연스럽게 따라 나오고, 상호(일도씨)·폰 잠금화면·마흔세 장 같은 고유 디테일이 생성문 티를 가장 잘 지워서 골랐습니다. 나머지 8개는 비교 가능한 초안입니다.</div>

<h2><span class="num">01</span>9개 조합 (업종 × 유형)</h2>
<div class="tbl"><table><thead><tr><th style="width:22%">업종 · 가상 사업장</th><th>A안 · 수치형</th><th>B안 · 인터뷰·에디터형</th><th>C안 · 상세페이지형</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="small">상호는 모두 가상이며 검색으로 동일 상호가 확인되지 않은 것으로 골랐습니다(열한시 치킨 · 일도씨 정육식당 · 볕드는집 산후조리원). 10/26~28 시안의 바삭마을 치킨·화로마당·포근 산후조리원은 실존 상호와 겹칠 수 있어 바꿨습니다. 수치·순위·점검 횟수는 시안용 예시입니다.</p>

<h2><span class="num">02</span>유형별 역할과 장단점</h2>
<div class="tbl"><table><thead><tr><th style="width:16%">유형</th><th style="width:30%">본문이 하는 일</th><th>장점</th><th>단점 · 전제</th></tr></thead><tbody>
<tr><td><b>A · 수치형</b></td><td>위생 카드의 수치를 계기판(값·기준의 몇 %·눈금)·동네 비교·점검 이력으로 다시 풀어 "얼마나 여유 있는지"를 읽게 함</td><td>근거가 또렷하고 글 없이 자동 생성 가능. 꾸준함(연속 통과·추이)을 보여 줄 수 있는 유일한 유형</td><td>상단 카드와 수치가 중복(10/28 결정과 상충). 집마다 비슷해 보이고 "왜 이 집인지"가 숫자 뒤에 숨음</td></tr>
<tr><td><b>B · 인터뷰·에디터형</b></td><td>에디터 방문기 + 사장님 문답. 위생 사실은 답에 섞여 나올 때만 팩트 칩으로 표시, 숫자는 다시 안 씀</td><td>집마다 다른 글이 나오고 생성문 티가 가장 적음. 위생이 자랑이 아니라 이야기의 증거로 읽힘. 마케팅 콘텐츠로 2차 활용 가능</td><td>전문가 현장 양식(본 것·잰 것·사장님 말·질문 2~3개)이 비면 못 씀. 사장님 확인 단계 필요. 글 분량이 가장 김</td></tr>
<tr><td><b>C · 상세페이지형</b></td><td>풀블리드 사진 + 큰 카피. 소개 → 특장점 3(사업주 선택) → 인터뷰 → 매일 하는 일. 수치는 맨 위 카드에만</td><td>가장 "마케팅 페이지"답고 사진이 일을 함. 선택 항목 + 기본 문안 구조라 40만 사업장에 자동 적용 가능</td><td>세로 사진 5장 필요, 없으면 회색 상자가 길게 남음. 기본 문안만 쓰면 B보다 집마다 비슷해 보임</td></tr>
</tbody></table></div>

<h2><span class="num">03</span>사업주 선택 항목 (업종별 특장점 리스트 초안)</h2>
<p>업종마다 공통 항목 8~10개를 두고 사업주가 <b>상위 3개</b>를 고르면 본문(B안 "사장님이 고른 세 가지", C안 POINT 01~03)에 우선 노출됩니다. 항목마다 기본 제목·카피 한 벌을 두고, 사장님 말이 있으면 바꿔 넣습니다. 세스코가 이번 점검에서 실제로 본 항목에만 파란 "세스코 확인" 칩이 붙고, 나머지는 회색 "매장 기록"으로 남습니다.</p>
<div class="opts">{opts}</div>
<p class="small" style="margin-top:10px">사업주가 직접 적는 자리는 세 곳입니다: ① 소개 문구(C안 ABOUT, 비면 업종 기본 문구) ② 사장님 한마디 1줄(A·B·C 공통) ③ 사진(히어로 세로 1장 + 선택 1장, 없으면 점검 때 전문가가 촬영).</p>

<h2><span class="num">04</span>상단 공통 요소 (3유형 동일)</h2>
<ul>
<li><b>AI 요약</b> — 리뷰·세스코 리포트·사장님 기록 세 출처에서 한 줄씩. <span class="need">[확인 필요]</span> 실제 위쳌 상세 페이지의 AI 요약 위치·형식·데이터 출처(리뷰 요약만인지, 점검 리포트까지 읽는지).</li>
<li><b>위생 정보 카드</b> — 등급 + 점검일 + 업종 공통 위생 포인트(10/23 개선안 1안 문구 기준). 실측 수치 2열 격자는 <b>A안(수치형)에만</b> 들어가고 B·C안 상단은 글 카드만 둡니다(10/30 수정). 치킨집은 10/23 개선안에 행이 없어 10/27 시안의 문구를 썼습니다.</li>
<li><b>리포트 원본 · 매장이 매일 하는 일 · 면책 문구</b> — 10/28 M안·L안과 동일.</li>
</ul>

<h2><span class="num">05</span>[확인 필요] 목록</h2>
<ol>
<li><span class="need">[확인 필요]</span> ATP 200 RLU는 법정 기준이 아닌 관리 기준(세스코 내부 또는 업계 통용)으로 표기했습니다. 실제 세스코 기준값과 측정 장비 명칭으로 맞춰야 합니다.</li>
<li><span class="need">[확인 필요]</span> 튀김유 산가 3.0 이하(식품위생법 시행규칙 별표 17), 식육 냉장 10℃ 이하(축산물 위생관리법령), 산후조리원 총부유세균 800 CFU/㎥(실내공기질 관리법 시행규칙 별표 2)는 조문 원문 대조가 필요합니다.</li>
<li><span class="need">[확인 필요]</span> 고깃집 "이틀째가 제일 쫀쫀하다"는 숙성 설명은 사장님 경험담으로만 적었고 위쳌이 단정하지 않습니다. 실제 콘텐츠에서도 사장님 말로 받아 적는 규칙 유지 여부.</li>
<li><span class="need">[확인 필요]</span> AI 요약 블록의 실제 사양(위 04).</li>
<li><span class="need">[확인 필요]</span> 동네 비교 순위("성수동 치킨집 상위 3%")는 A안에만 넣은 예시이며, 위쳌이 순위를 공개할 수 있는지.</li>
<li><span class="need">[확인 필요]</span> 가상 상호 3개의 실존 여부는 웹 검색으로만 확인했습니다. 네이버 지도·사업자 조회로 최종 확인이 필요합니다.</li>
<li><span class="need">[확인 필요]</span> 산후조리원 공통 포인트 문구는 10/23 개선안의 "치명적" 표현을 "면역이 약한"으로 낮췄습니다. 질환·감염 표현 수위.</li>
<li><span class="need">[확인 필요]</span> 10/27 사업장 상세 시안의 "식기 오염도(위생급식실 기준)" 항목은 이번 치킨집 카드에서 "생닭 냉장 온도"로 바꿨습니다. 업종별 4항목 구성.</li>
</ol>

<h2><span class="num">06</span>실장님이 결정해야 할 사항</h2>
<ol>
<li><b>유형 선택</b> — 세스코 1차 공유에 B·C 두 유형만 보낼지, A를 비교 기준으로 함께 보낼지. (미팅 의견은 B·C)</li>
<li><b>완성 라이팅 조합</b> — 고깃집 × B안으로 간 것이 맞는지, 11/4 보고에 치킨집 × C안을 한 개 더 완성할지.</li>
<li><b>사업주 선택 항목 수</b> — 업종당 10개 초안 중 세스코 FS(현장)와 맞출 항목, 상위 3개 외 나머지를 "매장이 매일 하는 일"로 내릴지.</li>
<li><b>상호 교체</b> — 10/26~28 시안의 바삭마을 치킨·화로마당·포근 산후조리원도 이번 상호로 통일할지(이전 파일은 그대로 둠).</li>
<li><b>검토용 주황 표식</b> — 세스코 공유본에 그대로 둘지, 표식 없는 버전을 따로 낼지(CSS 한 줄로 끌 수 있음).</li>
</ol>

<div class="foot">파일: 위쳌_{{업종}}_{{A수치형|B인터뷰에디터형|C상세페이지형}}_261028.html 9종 + index.html · 생성 스크립트 scripts/build.py · 디자인 토큰은 reports/261026 위쳌 M안·L안·B안과 동일(#0072CE 포인트, Pretendard) · 모바일 390px Playwright 스크린샷 검수 완료</div>
</div></body></html>'''
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote index.html')

ALL = '위쳌_전체보기_9종_261028.html'

def build_all():
    ids = {}
    for bk in ['chicken','meat','care']:
        for t in 'ABC':
            ids[FN[bk][t]] = f'{bk}-{t}'
    btns = ''
    for bk in ['chicken','meat','care']:
        for t in 'ABC':
            star = ' ★' if (bk=='meat' and t=='B') else ''
            nm = {'A':'수치형','B':'인터뷰·에디터형','C':'상세페이지형'}[t]
            btns += f'<button type="button" class="sel" data-id="{bk}-{t}">{BIZ[bk]["key"]} × {t}안<small>{nm}{star}</small></button>'
    secs = ''
    for fname, d in PAGES.items():
        side = d['side']
        for k, v in ids.items():
            side = side.replace(f'href="{k}"', f'href="#{v}"')
        secs += f"""<section class="view" id="{ids[fname]}" hidden>
<div class="desc"><h1>{d['title']}</h1></div>
<div class="stage"><figure><figcaption>{d['figcap']}<small>{d['figsub']}</small></figcaption>
<div class="phone"><div class="fold"><span>첫 화면 끝</span></div>{d['phone']}</div></figure>
<aside class="side">{side}</aside></div></section>"""
    idx = open(os.path.join(OUT, 'index.html'), encoding='utf-8').read()
    for k, v in ids.items():
        idx = idx.replace(f'href="{k}" target="_blank"', f'href="#{v}" target="_top"')
    idx = idx.replace('href="../261026/index.html"', 'href="https://chloe-sh.github.io/cesco-templates/reports/261026/index.html" target="_blank"')
    srcdoc = html.escape(idx, quote=True)
    doc = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 사업장 상세 9종 전체보기 (10/28)</title>{FONT}<style>{CSS}
.selbar{{position:sticky;top:0;z-index:20;background:#fff;border-bottom:1px solid #D9DCD6;padding:10px 16px;display:flex;flex-wrap:wrap;gap:6px;align-items:center}}
.selbar .ttl{{font-size:12.5px;font-weight:900;color:var(--ink);margin-right:6px}}
.sel{{font:inherit;font-size:12px;font-weight:800;color:var(--ink);background:#fff;border:1px solid #D9DCD6;border-radius:999px;padding:5px 11px;cursor:pointer;line-height:1.2;text-align:left}}
.sel small{{display:block;font-weight:600;color:var(--muted);font-size:10px}}
.sel.on{{background:var(--wc);border-color:var(--wc);color:#fff}}
.sel.on small{{color:#CFE0F3}}
.sel.cmp{{margin-left:auto;background:var(--chip)}}
.view .desc h1{{font-size:15px}}
#cmp iframe{{width:100%;border:0;background:#fff;border-radius:12px;display:block}}
.view{{scroll-margin-top:70px}}
@media (max-width:760px){{.selbar{{position:static}}}}
</style></head><body>
<div class="selbar"><span class="ttl">위쳌 사업장 상세 9종</span>{btns}<button type="button" class="sel cmp" data-id="cmp">비교 표·메모<small>index</small></button></div>
<div class="wrap">
<section class="view" id="cmp"><iframe id="cmpf" srcdoc="{srcdoc}" title="9개 조합 비교"></iframe></section>
{secs}
</div>
<script>
(function(){{
  var views=document.querySelectorAll('.view'), btns=document.querySelectorAll('.sel');
  function show(id){{
    if(!document.getElementById(id)) id='cmp';
    views.forEach(function(v){{v.hidden=(v.id!==id)}});
    btns.forEach(function(b){{b.classList.toggle('on',b.dataset.id===id)}});
    window.scrollTo(0,0);
    setTimeout(function(){{window.scrollTo(0,0)}},0);
  }}
  btns.forEach(function(b){{b.addEventListener('click',function(){{location.hash=b.dataset.id}})}});
  window.addEventListener('hashchange',function(){{show(location.hash.slice(1))}});
  var f=document.getElementById('cmpf');
  function fit(){{try{{f.style.height=(f.contentDocument.documentElement.scrollHeight+20)+'px'}}catch(e){{f.style.height='4000px'}}}}
  f.addEventListener('load',function(){{fit();
    try{{f.contentDocument.addEventListener('click',function(e){{var a=e.target.closest('a[href^="#"]');if(a){{e.preventDefault();location.hash=a.getAttribute('href').slice(1)}}}})}}catch(e){{}}
  }});
  window.addEventListener('resize',fit);
  show(location.hash.slice(1)||'cmp');
}})();
</script></body></html>"""
    with open(os.path.join(OUT, ALL), 'w', encoding='utf-8') as fh:
        fh.write(doc)
    print('wrote', ALL)

if __name__ == '__main__':
    for bk in ['chicken','meat','care']:
        build_A(bk); build_B(bk, full=(bk=='meat')); build_C(bk)
    build_index()
    build_all()
