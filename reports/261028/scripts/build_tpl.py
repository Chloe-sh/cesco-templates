# -*- coding: utf-8 -*-
"""위쳌 기본 템플릿 + 사장님 선택·수정 시연 페이지 생성.
핵심: 템플릿은 이미 다 채워져 있고(업종 기본 문안), 사장님은 특장점 2~3개만 고르면 되고, 원하면 문장을 고칠 수 있다.
실행: python3 reports/261028/scripts/build_tpl.py
"""
import os, json, sys
sys.path.insert(0, os.path.dirname(__file__))
import build as B

OUT = os.path.join(os.path.dirname(__file__), '..')
FNAME = '위쳌_기본템플릿_사장님선택수정_261028.html'

# ── 업종 기본 템플릿 (등록 정보만 들어가면 완성되는 문안) ──
TPL = {
'chicken': dict(
  key='치킨집', owner='사장님', tabs=['홈','메뉴','리뷰','사진','위생'], cta='이 가게 방역 알림 받기',
  reg=dict(name='열한시 치킨', cat='치킨·닭강정', town='성수동', years='17', rating='4.7', rv='리뷰 2,041', date='10.16', report='2026-1016-0512', n=5),
  hero_lab='{town} · {years}년', hero='오늘 기름,<br>오늘 닭으로 튀겨요',
  about_h='기름과 닭과 도마를<br>매일 같은 순서로',
  about='{town}에서 {years}년째 치킨을 튀기는 {name}이에요. 기름과 닭, 도마를 매일 같은 순서로 챙겨요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('영업','등록 정보'),('메뉴','등록 정보'),('이용','등록 정보'),('주차','등록 정보')],
  pt_h='이 집이 특히<br>신경 쓰는 세 가지',
  review='리뷰에서 가장 많이 나온 말은 "바삭하다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['chicken']['hc'],
  items=[
   ('튀김 기름 교체 주기','기름은 정해진 날,<br>전부 갈아요','튀김 기름은 요일을 정해 놓고 통째로 갈아요. 조금씩 보충하는 식은 안 하고요. 새 기름으로 튀긴 날은 바삭함부터 다르니까, 사장님이 제일 먼저 챙기는 일이에요.','세스코 실측 · 튀김유 산가',1),
   ('생닭 당일 소진','오늘 들어온<br>닭만 써요','아침에 들어온 닭은 그날 다 쓰고, 남아도 다음 날로 넘기지 않아요. 가끔 일찍 문을 닫는 날이 있는 것도 그래서예요.','세스코 실측 · 생닭 냉장 온도',1),
   ('염지·숙성 시간','염지는<br>시간을 지켜요','들어온 닭은 바로 염지해서 냉장고에 두고, 정해진 시간을 채운 것만 튀겨요. 간이 속까지 배고 살이 촉촉한 건 이 시간 덕이에요.','세스코 실측 · 냉장 보관 온도',1),
   ('도마·칼 색 구분','생닭 도마는<br>따로 있어요','생닭 손질하는 도마와 칼은 색을 따로 정해 두고 그 용도로만 써요. 직원이 바뀌어도 헷갈릴 일이 없게요.','세스코 실측 · 칼·도마 ATP',1),
   ('두 번 튀김·조리 온도','온도계 보고<br>두 번 튀겨요','튀김기 온도는 온도계로 확인하고, 한 번 튀긴 닭을 다시 한 번 튀겨요. 시간은 더 걸리지만, 식은 뒤에도 바삭한 건 그 덕이에요.','매장 기록',0),
   ('후드·덕트 청소 주기','후드 안쪽까지<br>닦아요','겉에 보이는 데만 닦는 게 아니라 후드 안쪽과 덕트까지 정기적으로 청소해요. 기름때가 쌓이면 주방 공기도, 안전도 장담하기 어려워서요.','세스코 실측 · 주방 공기',1),
   ('포장 방식','포장은<br>눅눅해지지 않게','포장 상자는 김이 빠지게 구멍을 내고, 뚜껑도 바로 닫지 않아요. 집에 가져가서 드셔도 바삭하라고요.','매장 기록',0),
   ('닭 호수·원산지 표시','닭은 호수와 원산지를<br>적어 둬요','어떤 닭을 쓰는지는 메뉴판과 매장 안에 적어 둬요. 손님이 묻기 전에 먼저 보여 드리는 거죠.','매장 기록',0),
   ('홀 테이블·소스통 관리','테이블과 소스통은<br>손님마다','손님이 나가면 테이블은 두 번 닦고, 소스통과 양념 그릇도 새로 채워서 내요. 앞 손님이 쓰던 걸 그대로 내는 일은 없어요.','매장 기록',0),
   ('배달 용기·위생 장갑','배달도 매장과<br>같은 손으로','조리할 땐 장갑을 끼고, 배달 용기는 밀봉해서 보내요. 배달 주문이라고 매장과 다르게 하는 건 없어요.','매장 기록',0)],
  default_sel=[0,1,3],
  edit=dict(about='성수동 골목에서 17년째, 아버지가 열고 아들이 이어서 하는 집이에요. 테이블은 네 개뿐이고 손님 열에 일곱은 포장이에요. 벽 메뉴판은 손글씨고 가격은 3년째 그대로예요.',
            pts={0:'문은 열한 시에 여는데 저는 네 시 반에 나와요. 월·수·금. 알람 세 개 맞춰 놓고요. 작년에 한 번 늦잠 자서 열 시에 갈았는데 단골이 "오늘 좀 다르네" 하더라고요.'},
            say='기름은 새벽에 갈아요. 점검 오시는 날도, 안 오시는 날도요.')),
'meat': dict(
  key='고깃집', owner='사장님', tabs=['홈','메뉴','리뷰','사진','위생'], cta='이 가게 방역 알림 받기',
  reg=dict(name='일도씨 정육식당', cat='돼지고기 구이·삼겹살', town='마포', years='3', rating='4.6', rv='리뷰 1,318', date='10.14', report='2026-1014-0287', n=5),
  hero_lab='{town} · {years}년', hero='고기는<br>온도로 관리해요',
  about_h='고기는 온도로, 불판은 손님마다,<br>반찬은 당일로',
  about='{town}에서 {years}년째 고기를 굽는 {name}이에요. 고기는 온도로, 불판은 손님마다, 반찬은 당일로 관리해요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('영업','등록 정보'),('메뉴','등록 정보'),('이용','등록 정보'),('주차','등록 정보')],
  pt_h='이 집이 특히<br>신경 쓰는 세 가지',
  review='리뷰에서 가장 많이 나온 말은 "불판을 자주 바꿔 준다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['meat']['hc'],
  items=[
   ('숙성고 온도·숙성 일수','고기는<br>온도로 관리해요','숙성고 온도를 정해 두고 하루에도 몇 번씩 확인해요. 입고일을 적어 두고 정해진 날이 지난 고기는 내지 않아요.','세스코 실측 · 숙성고 온도',1),
   ('입고 검수','고기는 사장님이<br>직접 받아요','들어오는 고기는 상자를 열어 색과 온도를 확인하고 받아요. 기준에 안 맞으면 돌려보내요.','매장 기록',0),
   ('불판 교체 기준','불판은<br>손님마다 새것','불판은 손님마다 새것으로 내고, 타기 시작하면 바로 바꿔 드려요. 닦아 둔 불판을 따로 쌓아 둬요.','세스코 실측 · 세척 불판 ATP',1),
   ('집게·가위 분리','생고기 집게는<br>따로 있어요','생고기용 집게와 익은 고기용 집게를 색으로 나눠요. 처음 오신 분께는 직원이 먼저 알려드려요.','세스코 실측 · 집게·가위 ATP',1),
   ('남은 반찬 폐기·소분 냉장','남은 반찬은<br>다시 안 내요','테이블에서 남은 반찬은 그 자리에서 버려요. 반찬은 소분해서 냉장에 두고 당일 것만 나가요.','세스코 확인 · 반찬 소분 냉장',1),
   ('숯·화덕 관리','숯은<br>때맞춰 갈아요','숯이 약해지면 바로 바꿔 드려요. 불판 바꿀 때 숯도 같이 봐요.','매장 기록',0),
   ('테이블 후드·연기','연기는 테이블에서<br>바로 빼요','테이블마다 후드가 있어 연기가 홀에 머물지 않아요. 옷에 냄새가 덜 배는 이유예요.','세스코 실측 · 홀 공기',1),
   ('등급판정서·원산지 게시','오늘 고기의<br>등급판정서가 있어요','축산물 등급판정서와 원산지를 매장에 붙여 둬요. 어디서 온 고기인지 보고 드실 수 있어요.','세스코 확인 · 등급판정서',1),
   ('직접 담근 재료','된장·김치는<br>직접 담가요','찌개 된장과 김치는 직접 담근 걸 써요. 사 오는 것보다 손이 많이 가지만 맛이 달라서요.','매장 기록',0),
   ('홀 환기·공기청정기','홀 공기도<br>관리해요','공기청정기를 영업 내내 켜 두고 환기 시간을 정해 둬요. 고기 연기 속 미세먼지까지 신경 써요.','세스코 실측 · 홀 공기',1)],
  default_sel=[0,2,4],
  edit=dict(about='마포 골목 안쪽, 테이블 여섯 개. 정육점 9년 하다 연 지 3년이에요. 상호의 \'일도\'는 숙성고 온도. 단골들이 붙인 별명이 그대로 간판이 됐어요.',
            pts={0:'제 폰 잠금화면이 숙성고 온도예요. 2년 전에 정전으로 4도까지 올라간 적이 있어서 그날 고기 다 뺐어요. 그 뒤로 센서 달고 알림 오게 했어요. 사흘 넘긴 고기는 안 냅니다.', 2:'한 테이블에 세 번 바꿀 때도 있어요. 불판만 닦으시는 분이 두 시에 오세요. 오셔서 제일 먼저 불판을 세요. 마흔 장 아래면 저한테 문자가 와요.'},
            say='고기는 온도로 먹는 거예요. 숙성고 1도, 불판 새것, 반찬 새것.')),
'care': dict(
  key='산후조리원', owner='원장님', tabs=['홈','프로그램','리뷰','사진','위생'], cta='이 조리원 방역 알림 받기',
  reg=dict(name='볕드는집 산후조리원', cat='산후조리원 · 민간형', town='분당', years='6', rating='4.9', rv='후기 412', date='10.15', report='2026-1015-0341', n=6),
  hero_lab='{town} · 민간형', hero='아기한테 닿는<br>순서대로 봐요',
  about_h='공기, 젖병, 수유실을<br>먼저 봐요',
  about='{town}에 있는 {name}이에요. 산모와 아기가 2주를 지내는 곳이라 공기와 젖병, 수유실을 먼저 봐요. 세스코가 정기 점검으로 확인한 결과를 이 페이지에 그대로 올려요.',
  strip=[('이용','등록 정보'),('식사','등록 정보'),('면회','등록 정보'),('프로그램','등록 정보')],
  pt_h='2주를 지내는 곳이라<br>이 세 가지를 봐요',
  review='후기에서 가장 많이 나온 말은 "방이 밝다"예요. (리뷰 데이터 연결 시 자동 요약)',
  hc=B.BIZ['care']['hc'],
  items=[
   ('신생아실 공기 수치 공개','신생아실 공기 수치를<br>공개해요','신생아실 공기는 매달 세스코가 재고, 그 결과를 복도에 붙여 둬요. 숫자는 있는 그대로 보여 드려요.','세스코 실측 · 신생아실 부유세균',1),
   ('젖병·수건 아기별 구분','젖병은<br>아기마다 따로','젖병과 수건은 아기마다 따로 두고 쓰고, 매일 고온으로 살균해요. 다른 아기 것과 섞일 일이 없어요.','세스코 실측 · 젖병 내부 ATP',1),
   ('산모 방 창·환기','산모 방은<br>창을 열어요','방마다 창이 있어서 정해진 시간에 환기를 해요. 2주를 지내는 방이니까 공기와 햇볕부터 챙겨요.','세스코 실측 · 산모 방 부유세균',1),
   ('면회·출입 관리','면회는<br>창 너머로','신생아실은 창 너머로만 보실 수 있고, 외부 방문은 시간과 인원을 정해 두었어요. 그 대신 폰으로 아기를 볼 수 있어요.','매장 기록',0),
   ('수유실 소독 주기','수유실은<br>시간마다 소독해요','수유실 소파와 손잡이는 정해진 간격으로 소독하고, 할 때마다 체크표에 시간과 사인을 남겨요.','세스코 실측 · 수유실 손잡이 ATP',1),
   ('침구·세탁 동선 분리','침구는 매일,<br>세탁은 동선을 나눠요','침구는 매일 갈고, 속싸개는 하루 두 번 바꿔요. 세탁한 것과 세탁할 것이 같은 문으로 드나들지 않게 동선을 나눴어요.','세스코 확인 · 세탁 동선',1),
   ('산모식 식재료·조리실','산모식은<br>조리실부터 봐요','식재료 보관 온도와 조리대를 관리하고, 미역국은 하루 두 번 새로 끓여요.','세스코 실측 · 산모식 조리대 ATP',1),
   ('좌욕기·비데 소독','좌욕기는 쓰고 나면<br>바로 소독','좌욕기와 비데는 쓰고 나면 바로 소독해요. 순서표를 붙여 두고 그 순서 그대로요.','세스코 실측 · 좌욕기 ATP',1),
   ('신생아실 야간 운영','밤에도 신생아실은<br>같은 인원','밤에도 간호 인력은 그대로 신생아실을 지키고, 조명만 낮춰요. 밤에 폰으로 봐도 아기가 잘 보여요.','매장 기록',0),
   ('간호 인력','신생아실은<br>간호사가 봐요','신생아실엔 간호사가 상주하고, 원장도 직접 돌아봐요. 궁금한 게 있으면 그 자리에서 물어보시면 돼요.','매장 기록',0)],
  default_sel=[0,1,2],
  edit=dict(about='분당에 있는 방 열두 개짜리 민간 조리원이에요. 원장인 저는 신생아실 간호사를 12년 했어요. 매달 세스코가 재고 가면 신생아실 공기 수치를 새 종이에 손으로 써서 복도에 붙여요.',
            pts={0:'지난달 숫자 위에 덧쓰지 않고 새 종이로 바꿔요. 숫자는 세스코가 재고 저는 옮겨 적기만 해요. 제가 쓰면 그건 광고잖아요.'},
            say='숫자는 세스코가 재요. 저는 복도에 붙이기만 해요.')),
}


# 위생 정보 카드 (스와이프). 산후조리원 = 10/23 개선안 최종 1안 원문. 치킨집 = 10/23 개선안에 행이 없어 같은 형식으로 쓴 초안.
HCARDS = {
'care': dict(src='10/23 개선안 1안 원문', cards=[
  ('VIRUSCARE','신생아와 산모가 생활하는 모든 공간!','전문 방역업체가 월 1회 이상 살균·소독하고 집기는 수시로 살균·소독해요.','바이러스케어 솔루션','전문 살균'),
  ('VIRUSCARE','우리 아기 젖병과 수건!','아기마다 개별로 구분해서 매일 고온 살균으로 관리해요.','바이러스케어 솔루션','신생아 용품 살균'),
  ('VIRUSCARE','산모와 아기가 숨 쉬는 공기!','공기 중 부유세균을 150 CFU/m³ 이하로 유지해요. 산후조리원 법정 기준의 5분의 1 수준으로 낮아요.','바이러스케어 솔루션','공기 살균'),
  ('BODYCARE','출산 후 감염에 약한 산모의 몸!','안심하고 회복할 수 있도록 청결 관리를 돕는 비데를 전 객실에 설치했어요.','바디케어 솔루션','비데 위생 관리'),
  ('FOOD','아기에게까지 닿는 산모의 식사!','식자재 입고부터 조리, 배식, 보관까지 모든 과정을 국내 식품위생법 기준으로 운영해요.','식품안전 솔루션','산모 식재료 위생')]),
'chicken': dict(src='초안 · 엑셀 ①시트에 치킨집 행이 없어 같은 형식으로 작성 [확인 필요]', cards=[
  ('FOOD','오늘 튀기는 기름!','튀김유 산가를 측정해서 식품위생법 기준(3.0 이하) 안으로 관리해요.','식품안전 솔루션','튀김유 산가'),
  ('FOOD','냉장고 안의 생닭!','생닭은 0~5℃ 냉장에서 보관하고 실온에 오래 두지 않아요.','식품안전 솔루션','생닭 보관 온도'),
  ('FOOD','생닭을 손질한 칼과 도마!','생닭용 칼·도마를 따로 구분하고 쓰고 나면 세척·소독해요.','식품안전 솔루션','칼·도마 위생'),
  ('IHM','기름 연기가 지나가는 후드!','기름때가 쌓이지 않도록 후드와 배기 덕트를 정기적으로 전문 클리닝해요.','전문클리닝 솔루션','후드·배기 청소'),
  ('AIR','튀김 연기가 머무는 주방 공기!','공기청정기를 24시간 가동해서 초미세먼지와 휘발성유기화합물을 관리해요.','에어 솔루션','주방 공기질'),
  ('IPM','기름과 음식 냄새에 꼬이는 해충!','전문 방제 서비스로 월 1회 이상 점검하고 관리해요.','종합방제 솔루션','해충 방제')]),
'meat': dict(src='', cards=[]),
}
# 네모 스티커(체크 스탬프) 탭 · 색 구분. 블루 멤버스 = IPM·바이러스케어·에어·워터·레스트룸(바디케어) 등 파랑, 화이트 멤버스 = 식품안전(세스코 푸드 초록)
MEMBERS = [
  dict(key='blue',  name='블루 멤버스',  color='#0072CE', bg='#EAF3FC', line='#2F7CE8', svcs=['IPM','VIRUSCARE','AIR','WATER','RESTROOM','BODYCARE','IHM','MYLAB']),
  dict(key='white', name='화이트 멤버스', color='#0E8F4A', bg='#E8F6EE', line='#2FA86A', svcs=['FOOD']),
]
# 네모 스티커 명칭(가칭) — 팀 내 결정 필요
STICKER_NAME = '체크 스탬프'

# 장소 정보 탭: 네이버식 기본 정보 + "세스코가 특별히 체크한 장소 정보"(엑셀 ②시트 현황검진 문진 · 가야만 아는 정보)
PLACE = {
'chicken': dict(
  addr='서울 성동구 성수이로 00길 00, 1층', hours='11:00 ~ 23:00 · 라스트오더 22:30 · 월요일 휴무', tel='02-0000-0000', pay='카드 · 간편결제 · 현금영수증', tags='#바삭 #포장 #배달',
  conv=['유아의자','단체석 (최대 12명)','남녀 구분 화장실','포장 · 배달','주차 2대'],
  checks=[
   ('CHECK','유아의자가 있어요','유아의자 2개가 있어요. 아이와 같이 와도 돼요.'),
   ('CHECK','단체석이 있어요','12명까지 한 자리에 앉아요. 회식이나 모임은 예약을 받아요.'),
   ('FOOD','김치는 국내산이에요','국내산 김치라고 하지만 믿을 수 있나요? 식재료의 출처까지 국내산 김치를 확인했습니다.'),
   ('FOOD','닭은 국내산이에요','모두 국내산 닭이라고 하지만 믿을 수 있나요? 세스코가 국내산 닭을 확인했습니다.'),
   ('FOOD','조리하는 분은 모두 비흡연이에요','위생은 조리사의 손끝에서 시작됩니다! 조리 종사자가 모두 담배를 피지 않는 사업장입니다.'),
   ('VIRUSCARE','화장실에 손세정제가 있어요','물로만 손 씻기에는 부족합니다! 손세정제를 화장실에 비치해 고객의 손 위생까지 생각하는 사업장입니다.'),
   ('FOOD','알레르기 유발 재료를 표기해요','누군가에게는 치명적이기에! 알레르기 유발 식재료를 명확히 표기한 사업장입니다.'),
   ('IHM','화장실은 하루 1회 이상 청소해요','기본을 지키는 일, 깨끗한 화장실의 시작입니다! 화장실을 하루 1회 이상 청소해 쾌적함을 유지하는 것을 확인했습니다.'),
   ('FOOD','마감 후 테이블을 전체 살균해요','이곳에서 수저는 테이블 위에 직접 놓으세요! 매일 마감 후 테이블을 전체 살균·소독하는 것을 확인했습니다.'),
   ('FOOD','위생 위반 이력이 없어요','한 번이 두 번, 세 번 되기는 쉽습니다! 위생 위반 이력이 없는, 기본을 지키는 안심 사업장입니다.')]),
'care': dict(
  addr='경기 성남시 분당구 00로 00, 3~5층', hours='상담 10:00 ~ 18:00 · 입소 상담 예약제 · 면회 14:00 ~ 17:00', tel='031-000-0000', pay='카드 · 계좌이체 · 현금영수증', tags='#모자동실 #신생아실CCTV #민간형',
  conv=['모자동실','신생아실 24시간 CCTV','창 너머 면회실','산모 전용 주차','배우자 동반 입실'],
  checks=[
   ('CHECK','모자동실이 있어요','아기와 같은 방에서 지내요. 원할 때만 신생아실에 맡겨요.'),
   ('CHECK','신생아실을 폰으로 볼 수 있어요','신생아실 CCTV를 24시간 폰으로 봐요. 면회는 창 너머로 해요.'),
   ('CHECK','모든 직원이 손소독 기록을 남겨요','신생아 감염은 ‘손’으로부터! 모든 직원이 손소독을 철저히 시행하고 손소독 기록지를 통해 체계적으로 관리합니다.'),
   ('IPM','산모 침대 매트리스는 매번 스팀 소독해요','산모와 아이가 오랜 시간을 함께 지내야 하는 침대! 분유나 음식물에 쉽게 오염될 수 있기에, 침대 매트리스는 매번 스팀 소독하며, 매월 정기 매트리스 위생 관리 서비스를 받고 있습니다.'),
   ('CHECK','수건, 옷, 담요는 친환경 세제로 빨아요','아기 피부에 닿는 모든 섬유, 세제부터 확인했습니다! 친환경 세제를 사용합니다.'),
   ('MYLAB','문 손잡이 같은 접촉면은 하루 3회 소독해요','문 손잡이가 교차 감염의 가장 빈번한 경로입니다! 하루 3번, 손이 닿는 모든 곳을 정해진 기준에 따라 소독하는 사업장입니다.'),
   ('IHM','좌욕기는 쓰고 나면 바로 소독해요','산모의 상처 부위가 직접 닿는 좌욕기! 사용 후 즉시 소독하고, 월 1회 분해 세척합니다.'),
   ('IHM','에어컨은 연 2회 분해 세척해요','세균과 곰팡이로 가득한 공기를 숨 쉬지 않도록! 에어컨 내부 분해 세척을 연 2회 이상 진행하는 것을 확인했습니다.'),
   ('IHM','가습기는 정기적으로 소독해요','가습기에서 세균 가득한 수증기를 뿜지 않도록! 단순 청소가 아닌 정기 소독으로 관리하는 것을 체크했습니다.')]),
'meat': dict(addr='',hours='',tel='',pay='',tags='',conv=[],checks=[]),
}

# 장소 정보 항목 메타(PLACE checks와 같은 순서): (아이콘, 그룹, 손님 질문, 칩 라벨)
PLACE_META = {
'chicken': [('👶','아이·모임','아이랑 가도 돼요?','유아의자'),('👥','아이·모임','여럿이 가도 돼요?','단체석 12명'),('🥬','먹거리','김치는 국내산이에요?','국내산 김치'),('🍗','먹거리','닭은 어디 거예요?','국내산 닭'),('🚭','사람·주방','조리하는 분이 담배 피우진 않죠?','조리자 비흡연'),('🧴','화장실','화장실에 손세정제 있어요?','손세정제'),('⚠️','먹거리','알레르기 표시 있어요?','알레르기 표기'),('🚻','화장실','화장실 깨끗해요?','하루 1회 청소'),('🧽','사람·주방','테이블은 매일 닦아요?','마감 살균'),('📋','사람·주방','위생 문제 있었던 곳은 아니죠?','위반 이력 없음')],
'care': [('🍼','산모·아기','아기랑 같은 방 쓸 수 있어요?','모자동실'),('📹','산모·아기','신생아실 볼 수 있어요?','CCTV 24시간'),('🧼','청결','직원분들 손 소독은요?','손소독 기록'),('🛏️','청결','침대는 깨끗해요?','매트리스 스팀'),('🧺','청결','아기 수건은 뭘로 빨아요?','친환경 세제'),('🚪','시설 관리','손잡이 같은 데 소독해요?','접촉면 3회 소독'),('🛁','시설 관리','좌욕기 같이 써도 괜찮아요?','좌욕기 즉시 소독'),('❄️','시설 관리','에어컨 청소는요?','에어컨 분해 세척'),('💨','시설 관리','가습기 관리해요?','가습기 소독')],
'meat': [],
}
SVC_KO = {'VIRUSCARE':'바이러스케어','BODYCARE':'바디케어','FOOD':'식품안전','IHM':'전문클리닝','IPM':'종합방제','AIR':'에어','MYLAB':'마이랩','CHECK':'현장 문진'}

# 도구 측정 블록(엑셀 ③시트) — 치킨집·산후조리원 각각 악취 + 배수구 오염도. 실제 수치 대신 기준 범위 안 통과 표시.
# levels: (단계명, 소비자 설명) · 첫 단계가 통과 위치. ex = 엑셀 '예시 문구' 원문(배수구는 ③시트에 없어 ②시트 숙박 행 문구를 가져옴 [확인 필요])
ODOR_LV = [('청결','냄새 민감군도 감지하기 어려운 수준'),('주의','불쾌감이 시작되고 해충 유입 위험이 증가하는 수준'),('위험','눈·코·입 점막을 자극해 알레르기 반응, 기관지염 등 건강에 실질적인 영향을 미칠 수 있는 수준')]
ODOR_EX = '일반적으로 악취 민원이 발생하는 화장실의 주요 악취 유발물질 농도는 암모니아 1.0 ~ 3.5 ppm, 황화수소 0.01 ~ 0.04 ppm, 메틸메르캅탄 0.003 ~ 0.01 ppm 이지만, 우리 사업장은 방향탈취기를 사용하여 냄새 민감군도 감지하기 어려운 수준인 암모니아 0.5 ppm 이하, 황화수소 0.005 ppm 이하, 메틸메르캅탄 0.001 ppm 이하로 쾌적하게 관리합니다.'
DRAIN_LV = [('청결','병원 내 조리시설 관리 수준'),('주의','경미한 악취가 시작되는 수준'),('경고','식중독균이 서식할 수 있는 수준'),('심각','악취가 심각하고 해충 서식 위험이 높은 수준')]
DRAIN_EX = '배수구는 악취만의 문제가 아니라 세균 증식, 해충 유입의 원인이 됩니다! 배수구 전용 클린 서비스로 관리하는 사업장입니다.'
TOOLS = {
'chicken': [
  dict(k='악취', hl='냄새 없이 쾌적해요', ic='💨', tool='악취측정기', easy='튀김 기름과 음식물 쓰레기 냄새를 측정기로 재요. 냄새에 예민한 분도 못 느낄 정도인지 봐요.', levels=ODOR_LV, ex=ODOR_EX, date='2026.10.16'),
  dict(k='배수구 오염도', hl='배수구가 청결하게 관리되고 있어요', ic='🚿', tool='배관 내시경', easy='주방 바닥 배수구 안을 내시경으로 봐요. 기름때와 찌꺼기가 쌓이면 냄새, 세균, 해충이 생기는 자리라서요.', levels=DRAIN_LV, ex=DRAIN_EX, date='2026.10.16')],
'care': [
  dict(k='악취', hl='냄새 없이 쾌적해요', ic='💨', tool='악취측정기', easy='산모 방과 공용 화장실 냄새를 측정기로 재요. 출산 뒤 냄새에 예민해진 산모도 못 느낄 정도인지 봐요.', levels=ODOR_LV, ex=ODOR_EX, date='2026.10.15'),
  dict(k='배수구 오염도', hl='배수구가 청결하게 관리되고 있어요', ic='🚿', tool='배관 내시경', easy='좌욕실과 조리실 배수구 안을 내시경으로 봐요. 찌꺼기가 쌓이면 냄새, 세균, 해충이 생기는 자리라서요.', levels=DRAIN_LV, ex=DRAIN_EX, date='2026.10.15')],
'meat': [],
}
# 위쳌 AI 카드 (세스코 CT Way PPT 'WeCheck 시연' 상세 화면 구조: 인트로 + ✅ 3 / 매장정보 3 / 리뷰 한눈에 3)
AICARD = {
'chicken': dict(intro='기름과 높은 온도 때문에 세균이나 해충이 생기기 쉬운 곳이라, 그만큼 더 꼼꼼하게 관리해요.',
  checks=['튀김 기름 산가를 정기 점검해 3.0 이하로 유지','닭고기는 입고 즉시 냉장 보관','주방 후드에 쌓인 기름때, 정기 전문 클리닝'],
  info=[('👶','유아의자가 있어서 아이와 같이 가도 괜찮아요.'),('👥','단체석이 있어서 모임이나 회식도 할 수 있어요.'),('🚻','매장 내부에 남녀 구분된 화장실이 있어요.')],
  review=['튀김이 바삭하고 기름 냄새가 안 나요.','고기가 촉촉하고 부드러워요.','포장해 가도 눅눅하지 않아요.'],
  quote='바삭한 건 기본이고,<br>주방 안쪽 위생까지<br>믿고 먹을 수 있는 치킨집이에요.'),
'care': dict(intro='면역력이 약한 신생아와 산모가 오래 머무는 곳이라 공기부터 손 닿는 자리까지 더 꼼꼼하게 관리해요.',
  checks=['전문 방역업체가 월 1회 이상 전체 살균·소독','젖병·수건은 아기별로 구분해 매일 고온 살균','신생아실 공기 살균기 상시 가동'],
  info=[('🍼','모자동실을 운영해 아기와 함께 지낼 수 있어요.'),('📹','폰으로 신생아실을 24시간 볼 수 있어요.'),('🪟','방마다 바깥 창이 있어 환기가 잘 돼요.')],
  review=['신생아실이 항상 깨끗하게 유지돼요.','산모식이 정갈하고 회복에 좋아요.','선생님들이 세심하게 돌봐주세요.'],
  quote='공기부터 젖병까지,<br>아기에게 닿는 순서대로<br>챙기는 조리원이에요.'),
'meat': dict(intro='',checks=[],info=[],review=[],quote=''),
}
SVC_EN = {'VIRUSCARE':'Viruscare','BODYCARE':'Bodycare','FOOD':'Food','IHM':'Cleaning','IPM':'IPM','AIR':'Air','MYLAB':'MyLab','CHECK':'Check'}

# 인터뷰형 질문(셀프 인터뷰) · 수치형 매핑(위생 카드 실측 항목 index, 없으면 -1)
QS = {
'chicken': ['기름은 언제 갈아요?','닭은 언제 들어오고 언제까지 써요?','염지는 어떻게 해요?','생닭 손질할 때 도마는요?','두 번 튀기는 이유가 있어요?','후드 청소는 누가, 얼마나 자주 해요?','포장하면 눅눅해지지 않나요?','어떤 닭을 쓰세요?','테이블이랑 소스통은요?','배달은 매장이랑 다른 게 있어요?'],
'meat': ['고기는 몇 도에 두세요?','고기 들어올 때 뭘 보세요?','불판은 언제 바꿔 줘요?','집게가 두 개 나오던데요?','남은 반찬은 어떻게 해요?','숯은 언제 갈아요?','연기는 어떻게 빼요?','오늘 고기는 어디서 온 거예요?','된장이랑 김치는 직접 담그세요?','홀 공기는 어떻게 관리해요?'],
'care': ['신생아실 공기는 어떻게 확인해요?','젖병은 아기마다 따로 써요?','산모 방 환기는요?','면회는 어떻게 해요?','수유실 소독은 얼마나 자주 해요?','침구랑 세탁은요?','산모식은 누가 어떻게 만들어요?','좌욕기는 쓰고 나면요?','밤에는 신생아실에 누가 있어요?','신생아실은 누가 봐요?'],
}
MET = {
'chicken': [0,1,1,2,-1,3,-1,-1,-1,-1],
'meat':    [0,-1,1,2,-1,-1,3,-1,-1,3],
'care':    [0,1,-1,-1,2,-1,3,-1,-1,-1],
}

# JS로 넘길 데이터
DATA = {}
for k, t in TPL.items():
    d = dict(t); d['hcards'] = HCARDS[k]; d['aicard'] = AICARD[k]; d['svc_en'] = SVC_EN; d['svc_ko'] = SVC_KO; d['members'] = MEMBERS; d['sticker'] = STICKER_NAME; d['placeinfo'] = PLACE[k]; d['placemeta'] = PLACE_META[k]; d['tools'] = TOOLS[k]; d['place'] = '조리원' if k=='care' else '가게'; d['default_mt'] = 'white' if k=='chicken' else 'blue'; d['items'] = [dict(label=a, title=b, copy=c, chip=e, cesco=f, q=QS[k][i], metric=MET[k][i]) for i, (a, b, c, e, f) in enumerate(t['items'])]
    hc = t['hc']; d['hc'] = dict(pill=hc['pill'], hl=hc['hl'], ds=hc['ds'], sum=hc['sum'], metrics=[dict(k=m[0], v=m[1], u=m[2], pct=m[3], base=m[4]) for m in hc['metrics']])
    DATA[k] = d

EXTRA_CSS = r"""
.top{max-width:1320px;margin:0 auto;padding:20px 20px 0}
.two-col{display:flex;gap:28px;justify-content:center;align-items:flex-start;flex-wrap:wrap;max-width:1320px;margin:0 auto;padding:0 20px 60px}
.col{width:390px;flex-shrink:0}
.col h3{margin:0 0 8px 4px;font-size:12.5px;font-weight:800;color:var(--ink)}
.col h3 small{display:block;font-weight:500;color:var(--muted);font-size:11.5px}
/* 사장님 편집 화면 */
.ed{background:#fff;border-radius:28px;box-shadow:0 10px 30px rgba(0,0,0,.14),0 0 0 1px rgba(0,0,0,.06);overflow:hidden}
.ed .bar{height:52px;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:var(--ink);border-bottom:1px solid var(--line);position:relative}
.ed .bar .sv{position:absolute;right:12px;top:12px;height:28px;padding:0 12px;border-radius:8px;background:var(--wc);color:#fff;font-size:12px;font-weight:800;display:flex;align-items:center}
.ed .in{padding:14px 16px 18px;display:flex;flex-direction:column;gap:14px}
.ed .seg{display:flex;gap:6px}
.ed .seg button{flex:1;font:inherit;font-size:12px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.ed .seg button.on{background:var(--wc);border-color:var(--wc);color:#fff}
.ed .fs{border:0;padding:0;margin:0}
.ed .lb{display:flex;align-items:baseline;gap:6px;font-size:12.5px;font-weight:900;color:var(--ink);margin-bottom:6px}
.ed .lb small{font-weight:600;color:var(--muted);font-size:10.5px;margin-left:auto}
.ed .lock{font-size:11px;color:var(--muted);background:#F2F4F7;border-radius:10px;padding:9px 11px;line-height:1.5}
.ed .lock b{color:var(--ink2)}
.ed .chk{display:flex;flex-direction:column;gap:5px}
.ed .chk label{display:grid;grid-template-columns:18px 1fr auto;gap:8px;align-items:center;padding:8px 10px;border:1px solid #E3E6E1;border-radius:10px;font-size:12.5px;font-weight:700;color:var(--ink);cursor:pointer}
.ed .chk label.on{border-color:var(--wc);background:var(--wc-bg)}
.ed .chk label.dis{opacity:.45}
.ed .chk input{margin:0;width:16px;height:16px;accent-color:var(--wc)}
.ed .chk .ord{font-size:9.5px;font-weight:900;color:#fff;background:var(--wc);border-radius:999px;padding:1px 7px;visibility:hidden}
.ed .chk label.on .ord{visibility:visible}
.ed .chk .cs{font-size:9.5px;font-weight:800;color:var(--wc);margin-left:6px}
.ed .chk .cs.o{color:var(--muted)}
.ed textarea,.ed input[type=text]{width:100%;font:inherit;font-size:12.5px;line-height:1.5;color:var(--ink2);border:1px solid #D9DCD6;border-radius:10px;padding:9px 10px;resize:vertical;background:#fff}
.ed textarea:focus,.ed input:focus{outline:2px solid var(--wc);border-color:var(--wc)}
.ed textarea.changed,.ed input.changed{background:var(--amber-bg);border-color:#F0C27A}
.ed .cnt{font-size:10px;color:var(--muted);text-align:right;margin-top:2px}
.ed .pt-ed{border:1px solid #E3E6E1;border-radius:12px;padding:10px;margin-top:8px}
.ed .pt-ed .t{font-size:11.5px;font-weight:900;color:var(--wc);margin-bottom:5px}
.ed .pt-ed .t span{color:var(--ink);margin-left:6px}
.ed .pt-ed .ph{height:52px;margin-top:6px;font-size:10px}
.ed .btns{display:flex;gap:6px}
.ed .btns button{flex:1;font:inherit;font-size:11.5px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.ed .btns button.ex{border-color:var(--amber);color:var(--amber);background:var(--amber-bg)}
.hc{overflow:hidden;min-width:0;background:#fff;border-radius:0;box-shadow:none;padding:18px 0 18px}
.head .pho2{height:150px;margin:-12px -16px 0;background:linear-gradient(160deg,#E6EAEF,#CBD3DC);display:flex;align-items:flex-end;padding:10px 14px;color:#6B7684;font-size:10.5px;font-weight:700}
.head{padding-bottom:12px}
.wai{border:1.5px solid transparent;border-radius:14px;padding:14px 14px 12px;background:linear-gradient(#fff,#fff) padding-box,linear-gradient(135deg,#22B8B0,#3D6FD9) border-box}
.wai-t{display:flex;align-items:center;gap:6px;font-size:14.5px;font-weight:900;color:var(--ink)}
.wai-t .inf{width:14px;height:14px;border:1.3px solid #A6AFBB;border-radius:50%;font-size:9px;color:#A6AFBB;display:inline-flex;align-items:center;justify-content:center;font-weight:800}
.wai-i{font-size:12.5px;font-weight:800;color:var(--ink);line-height:1.6;margin-top:8px}
.wai ul{list-style:none;margin:8px 0 0;padding:0}
.wai li{display:flex;gap:6px;font-size:12px;color:var(--ink2);line-height:1.55;padding:2px 0}
.wai li .em{flex:none;font-size:12px}
.wai-h{font-size:12px;font-weight:900;color:#0072CE;margin-top:12px}
.tabs2{display:flex;background:#fff;border-bottom:1px solid var(--line);margin-top:10px}
.tabs2 span{flex:1;height:44px;display:flex;align-items:center;justify-content:center;font-size:13.5px;color:#8A8A8A}
.tabs2 span.on{color:var(--ink);font-weight:900;border-bottom:2.5px solid var(--ink)}
.qt2{text-align:center;font-size:17px;font-weight:800;color:var(--ink);line-height:1.45;padding:6px 20px 16px;letter-spacing:-.01em}
.hc .sw{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 calc((100% - 262px)/2) 4px;scrollbar-width:none}
.hc .sw::-webkit-scrollbar{display:none}
.hc .swc{flex:none;width:262px;scroll-snap-align:center;background:#E3E8EE;border-radius:20px;padding:12px;cursor:pointer}
.hc .swin{background:#fff;border-radius:12px;border:1.4px solid #E3E8EE;border-top-color:#2F7CE8;border-left-color:#2F7CE8;padding:14px 14px 12px;height:100%;display:flex;flex-direction:column}
.hc .swt{display:flex;align-items:flex-start;justify-content:space-between}
.hc .logo{display:flex;align-items:baseline;gap:4px}
.hc .logo b{font-family:Georgia,"Times New Roman",serif;font-size:16px;font-weight:700;color:#1E2B49;letter-spacing:-.02em}
.hc .logo i{font-style:normal;font-size:13px;color:#1E2B49;font-weight:600}
.hc .stamp{flex:none;margin-top:-4px}
.hc .hk{font-size:12px;color:#6B7684;margin-top:12px;line-height:1.5}
.hc .hl{font-size:14px;font-weight:800;color:#1A2E5A;line-height:1.5;margin-top:6px;flex:1}
.hc .ck{display:flex;gap:6px;align-items:flex-start;margin-top:12px;font-size:10.5px;color:#1A2E5A;line-height:1.45}
.hc .ck .bx{flex:none;width:13px;height:13px;border:1.4px solid #1A2E5A;border-radius:2px;font-size:9px;line-height:11px;text-align:center;font-weight:900}
.hc .dt{font-size:10px;color:#6B9AD4;margin-top:3px;padding-left:19px}
.hc .rp{align-self:center;margin-top:10px;font-size:10px;color:#6B7684;background:#F2F4F7;border-radius:999px;padding:3px 10px}
.hc .swbar{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:12px}
.hc .swnav{width:26px;height:26px;border-radius:50%;border:1px solid var(--wc-line);background:#fff;color:var(--wc);font-size:16px;font-weight:900;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;padding:0 0 2px}
.hc .dots{display:flex;gap:5px;justify-content:center}
.hc .dots i{width:6px;height:6px;border-radius:50%;background:#D5DCE4;cursor:pointer}
.hc .dots i.on{width:16px;border-radius:3px;background:var(--wc)}
.hc .hcsum{text-align:center;font-size:10.5px;color:var(--muted);margin-top:10px}
.hc .hcsum b{color:var(--wc)}
.hc .grid{padding:0 16px;margin-top:14px}
/* 기본 정보(네이버식) */
.binfo{margin-top:12px;border-top:1px solid var(--line);padding-top:10px}
.bi{display:flex;align-items:flex-start;gap:8px;font-size:12px;color:var(--ink2);line-height:1.5;padding:3px 0}
.bi .ic{flex:none;width:16px;text-align:center;font-size:12px}
.bi b{flex:none;margin-left:auto;font-size:11px;color:var(--wc);font-weight:700;white-space:nowrap}
.tabs2 span{cursor:pointer}
/* 체크 스탬프(네모 스티커) · 블루/화이트 멤버스 탭 */
.sh3{display:flex;align-items:baseline;gap:6px;padding:0 16px;font-size:12.5px;font-weight:900;color:var(--ink)}
.sh3 small{font-weight:600;color:var(--muted);font-size:10.5px}
.mtabs{display:flex;gap:6px;padding:8px 16px 12px}
.mtab{flex:1;font:inherit;font-size:12px;font-weight:800;padding:8px 0;border-radius:999px;border:1.5px solid #E3E6E1;background:#fff;color:var(--muted);cursor:pointer}
.mtab small{font-weight:700;margin-left:4px;font-size:10px}
.mtab.on{border-color:var(--mc);background:var(--mc);color:#fff}
.hc .swc{background:var(--mbg,#E3E8EE)}
.hc .swin{border-top-color:var(--ml,#2F7CE8);border-left-color:var(--ml,#2F7CE8)}
.hc .logo b,.hc .logo i{color:var(--mc,#1E2B49)}
.hc .ck{color:var(--mc,#1A2E5A)}
.hc .ck .bx{border-color:var(--mc,#1A2E5A)}
.hc .sw:empty:before{content:"이 탭에 해당하는 항목이 없어요";font-size:11px;color:var(--muted);padding:12px 0}
/* 도구 측정 블록 */
.tools-wrap{background:var(--bg);padding:6px 0 18px}
.tools{margin:0 16px;background:#fff;border:1.5px solid #E6D9B8;border-radius:16px;padding:14px}
.tl-h{display:flex;gap:10px;align-items:center}
.gold{flex:none;width:44px;height:44px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#F6E7B0,#C9A227 70%,#A8841A);color:#5A4200;font-size:7.5px;font-weight:900;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.15;box-shadow:0 1px 3px rgba(0,0,0,.2)}
.tl-h b{display:block;font-size:13.5px;font-weight:900;color:var(--ink)}
.tl-h small{font-size:10.5px;color:var(--muted)}
.tl{margin-top:12px;padding-top:12px;border-top:1px dashed #E6D9B8}
.tl-k{display:flex;align-items:baseline;gap:6px;font-size:13px;font-weight:900;color:var(--ink)}
.tl-k small{font-weight:600;color:var(--muted);font-size:10.5px}
.tl-k .pass{margin-left:auto;font-size:10px;font-weight:900;color:#5A4200;background:#F6E7B0;border-radius:999px;padding:2px 8px;white-space:nowrap}
.tl-e{font-size:11.5px;color:var(--txt);line-height:1.55;margin-top:5px}
.scale{display:flex;gap:3px;margin-top:24px}
.scale .lv{flex:1;height:22px;border-radius:5px;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:800;color:#fff;opacity:.3;position:relative}
.scale .lv:nth-child(1){background:#0E8F4A}.scale .lv:nth-child(2){background:#E0A100}.scale .lv:nth-child(3){background:#E2641B}.scale .lv:nth-child(4){background:#C8102E}
.scale .lv.on{opacity:1;box-shadow:0 0 0 2px #fff,0 0 0 3.5px #C9A227}
.scale .lv.on:after{content:"✓ 이 사업장";position:absolute;top:-17px;left:50%;transform:translateX(-50%);font-size:9.5px;font-weight:900;color:#5A4200;white-space:nowrap}
.lvd{margin-top:8px;font-size:10px;color:var(--muted);line-height:1.45}
.lvd div{display:flex;gap:6px}
.lvd b{flex:none;width:28px;color:var(--ink2);font-weight:800}
.tl-x{font-size:11px;color:var(--ink2);line-height:1.6;margin-top:8px;background:#FBF7EC;border-radius:10px;padding:9px 10px}
.tl-d{font-size:10px;color:#9A6B12;margin-top:6px;font-weight:700}

/* 도구 측정 블록 디자인 3안 */
.phone.part{border-radius:16px;padding:10px 0}
/* A 검사 리포트형 */
.tv-a{margin:0 16px;background:#FCFBF7;border:1px solid #E3DFD2;border-radius:10px;padding:0 0 10px;font-size:11.5px}
.tv-a .rh{display:flex;align-items:center;gap:8px;padding:11px 14px;border-bottom:2px solid #1A1A1A}
.tv-a .rh .no{font-size:9.5px;letter-spacing:.08em;color:#6B6B6B;font-weight:800;text-transform:uppercase}
.tv-a .rh b{display:block;font-size:13.5px;font-weight:900;color:var(--ink)}
.tv-a .rh .dt{margin-left:auto;text-align:right;font-size:9.5px;color:#6B6B6B;line-height:1.3}
.tv-a .rh .dt b{font-size:11px;color:var(--ink)}
.tv-a .ri{padding:12px 14px 2px;border-bottom:1px solid #E3DFD2}
.tv-a .ri:last-child{border-bottom:0}
.tv-a .rt{display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center}
.tv-a .rt b{font-size:13px;font-weight:900;color:var(--ink)}
.tv-a .rt small{font-size:10px;color:#6B6B6B}
.tv-a .rs{grid-row:1/3;display:flex;align-items:center;gap:5px;font-size:12px;font-weight:900;color:#0B5E31;background:#E8F6EE;border:1px solid #BFE5CF;border-radius:6px;padding:5px 9px}
.tv-a .rs i{font-style:normal;width:16px;height:16px;border-radius:50%;background:#0E8F4A;color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center}
.tv-a .re{color:var(--txt);line-height:1.55;margin:7px 0 0}
.tv-a .rb{position:relative;display:flex;gap:2px;margin-top:22px;height:8px}
.tv-a .rb i{flex:1;border-radius:2px;background:#DAD6C9}
.tv-a .rb i.on{background:#0E8F4A}
.tv-a .rb i.on:after{content:"▼ 이 사업장";position:absolute;top:-16px;left:0;width:var(--w);text-align:center;font-size:9.5px;font-weight:900;color:#0B5E31;font-style:normal;white-space:nowrap}
.tv-a .rl{display:grid;grid-template-columns:auto 1fr;gap:3px 8px;margin-top:8px;font-size:10px;color:#6B6B6B;line-height:1.4}
.tv-a .rl b{color:var(--ink2);font-weight:800;min-width:24px}
.tv-a .rl .on{color:#0B5E31}
.tv-a .rq{margin:9px 0 10px;padding:0 0 0 10px;border-left:2px solid #C9A227;font-size:10.5px;color:var(--ink2);line-height:1.6}
.tv-a .rf{padding:9px 14px 0;font-size:9.5px;color:#6B6B6B;display:flex;justify-content:space-between}
/* D 스탬프형(확정) + 같은 방식 B·E·F */
.tv-b{margin:0 16px;background:#fff;border-radius:16px;padding:14px;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.tv-b .bh{display:flex;align-items:center;gap:8px}
.tv-b .bh .lg{flex:none;width:34px;height:34px;border-radius:10px;background:var(--wc);color:#fff;font-size:8px;font-weight:900;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.1}
.tv-b .bh b{display:block;font-size:13.5px;font-weight:900;color:var(--ink)}
.tv-b .bh small{font-size:10.5px;color:var(--muted)}
.tv-b .gg{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.tv-b .g{font:inherit;cursor:pointer;position:relative;padding:10px 8px 22px;border:1px solid var(--wc-line);border-radius:14px;text-align:center;background:#FAFCFF;color:inherit}
.tv-b .g.on{border-color:var(--wc);background:#fff;box-shadow:0 0 0 2px var(--wc-bg)}
.tv-b .g svg{width:100%;max-width:130px;display:block;margin:0 auto}
.tv-b .g .gk{font-size:11.5px;font-weight:900;color:var(--ink);margin-top:-2px;line-height:1.3;word-break:keep-all}
.tv-b .g .gk small{display:block;font-size:9.5px;color:var(--muted);font-weight:600;margin-top:1px}
.tv-b .g .gv{display:inline-block;margin-top:6px;font-size:11px;font-weight:900;color:#0B5E31;background:#E8F6EE;border-radius:999px;padding:2px 9px}
.tv-b .g .more{position:absolute;left:0;right:0;bottom:6px;font-style:normal;font-size:9.5px;color:var(--muted);font-weight:700}
.tv-b .g .more:after{content:" ⌄"}
.tv-b .g.on .more{color:var(--wc)}.tv-b .g.on .more:after{content:" ⌃"}
.tv-b .bd{margin-top:8px}
.tv-b .bp{display:none;border-top:1px solid var(--line);padding-top:8px}
.tv-b .bp.on{display:block}
.tv-b .be{font-size:11.5px;color:var(--txt);line-height:1.55;margin:0}
.tv-b .bl{display:flex;flex-wrap:wrap;align-items:center;gap:4px;margin-top:8px}
.tv-b .bl span{font-size:10px;font-weight:800;color:#9A9A9A;padding:3px 8px;border-radius:999px;background:#F4F5F2}
.tv-b .bl span.on{background:#E8F6EE;color:#0B5E31}
.tv-b .bl small{flex-basis:100%;font-size:10px;color:var(--muted);line-height:1.4;margin-top:1px}
.tv-b .bx{font-size:10.5px;color:var(--ink2);line-height:1.6;margin-top:8px;background:var(--wc-bg);border-radius:10px;padding:8px 10px}
.tv-b .bdt{font-size:10px;color:var(--muted);margin-top:5px;font-weight:700}
/* D 스탬프형 */
.tv-d .g{padding-top:14px}
.tv-d .seal{display:flex;flex-direction:column;align-items:center;justify-content:center;width:58px;height:58px;margin:0 auto 8px;border-radius:50%;border:2px solid #0E8F4A;outline:2px dashed #BFE5CF;outline-offset:3px;color:#0E8F4A;transform:rotate(-8deg)}
.tv-d .seal i{font-style:normal;font-size:22px;font-weight:900;line-height:1}
.tv-d .seal small{font-size:7px;font-weight:900;letter-spacing:.08em}
.tv-d .g.on .seal{background:#E8F6EE}
/* E 한 줄 리스트형 */
.tv-e .gg{grid-template-columns:1fr;gap:6px;margin-top:10px}
.tv-e .g{display:grid;grid-template-columns:34px 1fr auto;grid-template-rows:auto auto;align-items:center;gap:2px 10px;text-align:left;padding:10px 12px 10px 10px;border-radius:12px}
.tv-e .g .ic{grid-row:1/3;width:34px;height:34px;border-radius:50%;background:#fff;border:1px solid var(--wc-line);display:flex;align-items:center;justify-content:center;font-size:17px}
.tv-e .g .gk{grid-column:2;grid-row:1;margin:0;font-size:12.5px}
.tv-e .g .gv{margin:0;grid-column:3;grid-row:1;align-self:center;font-size:10px;padding:2px 7px}
.tv-e .g .seg{grid-column:2/3;grid-row:2;display:flex;gap:2px;height:5px;margin-top:4px}
.tv-e .g .seg i{flex:1;border-radius:2px;background:#E4E6E1}.tv-e .g .seg i.on{background:#0E8F4A}
.tv-e .g:after{content:"⌄";grid-column:3;grid-row:2;justify-self:end;font-size:11px;line-height:1;color:var(--muted)}
.tv-e .g.on:after{content:"⌃";color:var(--wc)}
/* F 요약 카드형 */
.tv-f{padding:0 14px 12px;overflow:hidden}
.tv-f .top{margin:0 -14px;padding:16px 16px 14px;background:linear-gradient(135deg,#1A3668,#0072CE);color:#fff}
.tv-f .top small{display:block;font-size:9.5px;font-weight:800;letter-spacing:.06em;opacity:.8}
.tv-f .top b{display:block;font-size:20px;font-weight:900;margin-top:4px;line-height:1.2}
.tv-f .top span{display:block;font-size:10.5px;opacity:.85;margin-top:3px}
.tv-f .gg{grid-template-columns:1fr;gap:0;margin-top:4px}
.tv-f .g{display:flex;align-items:center;gap:9px;text-align:left;padding:11px 0;border:0;border-bottom:1px solid var(--line);border-radius:0;background:none;box-shadow:none}
.tv-f .g.on{box-shadow:none;background:none}
.tv-f .g .ok{flex:none;width:20px;height:20px;border-radius:50%;background:#0E8F4A;color:#fff;font-style:normal;font-size:11px;font-weight:900;display:flex;align-items:center;justify-content:center}
.tv-f .g .gk{margin:0;flex:1;font-size:12.5px;text-align:left}
.tv-f .g .more{position:static;flex:none}
/* C 점검 기록형 */
.tv-c{margin:0 16px;background:#fff;border-radius:16px;padding:14px 14px 10px;border:1px solid var(--line)}
.tv-c .ch{display:flex;align-items:center;gap:9px}
.tv-c .ch .av{flex:none;width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#1A3668,#0072CE);color:#fff;font-size:8.5px;font-weight:900;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.1}
.tv-c .ch b{display:block;font-size:13.5px;font-weight:900;color:var(--ink)}
.tv-c .ch small{font-size:10.5px;color:var(--muted)}
.tv-c .ch .st{margin-left:auto;font-size:9.5px;font-weight:900;color:var(--wc);border:1.5px solid var(--wc);border-radius:6px;padding:3px 7px;white-space:nowrap;text-align:center;line-height:1.2}
.tv-c .tl2{position:relative;margin-top:12px;padding-left:22px}
.tv-c .tl2:before{content:"";position:absolute;left:6px;top:8px;bottom:14px;border-left:2px dotted #CFE0F3}
.tv-c .ci{position:relative;padding:2px 0 14px}
.tv-c .ci:before{content:"✓";position:absolute;left:-22px;top:2px;width:14px;height:14px;border-radius:50%;background:var(--wc);color:#fff;font-size:9px;font-weight:900;display:flex;align-items:center;justify-content:center}
.tv-c .ck{display:flex;align-items:center;gap:6px;font-size:13px;font-weight:900;color:var(--ink)}
.tv-c .ck small{font-size:10px;color:var(--muted);font-weight:600}
.tv-c .ck .ok{margin-left:auto;font-size:10px;font-weight:900;color:#0B5E31;background:#E8F6EE;border-radius:999px;padding:2px 8px;white-space:nowrap}
.tv-c .ce{font-size:11.5px;color:var(--txt);line-height:1.55;margin:5px 0 0}
.tv-c .ld{margin-top:8px;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.tv-c .ld div{display:flex;gap:8px;align-items:center;padding:5px 9px;font-size:10px;color:#9A9A9A;line-height:1.35;border-top:1px solid var(--line)}
.tv-c .ld div:first-child{border-top:0}
.tv-c .ld b{flex:none;width:26px;font-weight:800;color:#B0B0B0}
.tv-c .ld div.on{background:#E8F6EE;color:#0B5E31;font-weight:700}
.tv-c .ld div.on b{color:#0B5E31}
.tv-c .ld div.on:after{content:"◀ 이 사업장";margin-left:auto;font-size:9.5px;font-weight:900;white-space:nowrap}
.tv-c .cm{position:relative;margin-top:9px;background:#F4F5F2;border-radius:12px;padding:8px 10px;font-size:10.5px;color:var(--ink2);line-height:1.6}
.tv-c .cm:before{content:"";position:absolute;left:14px;top:-6px;border:6px solid transparent;border-bottom-color:#F4F5F2;border-top:0}
.tv-c .cm b{display:block;font-size:9.5px;color:var(--wc);margin-bottom:2px}
.tv-c .cd{font-size:10px;color:var(--muted);margin-top:6px;font-weight:700}
/* 장소 정보 탭 */
.place{background:#fff;padding:14px 16px 18px}
.pl-sec{padding:4px 0 14px}
.pl-t{font-size:13.5px;font-weight:900;color:var(--ink);margin-bottom:8px}
.pl-t small{display:block;font-size:10.5px;color:var(--muted);font-weight:600;margin-top:2px}
.pl-row{display:grid;grid-template-columns:58px 1fr;gap:8px;font-size:12px;color:var(--ink2);padding:7px 0;border-top:1px solid var(--line);line-height:1.5}
.pl-row span:first-child{color:var(--muted);font-weight:700}
.pl-chips{display:flex;flex-wrap:wrap;gap:5px}
.pl-chips i{font-style:normal;font-size:11px;font-weight:700;color:var(--ink2);background:#F2F4F7;border-radius:999px;padding:3px 9px}
.pl-sec.cesco{margin-top:4px;background:linear-gradient(#fff,#fff) padding-box,linear-gradient(135deg,#22B8B0,#3D6FD9) border-box;border:1.5px solid transparent;border-radius:14px;padding:14px 14px 8px}
.pc{padding:10px 0;border-top:1px solid var(--line)}
.pc.first{border-top:0;padding-top:4px}
.pc-h{display:flex;align-items:center;gap:7px}
.pc-h .svc{flex:none;margin-left:auto;font-size:9px;font-weight:800;color:var(--mc);border:1px solid var(--mc);border-radius:5px;padding:1px 5px;white-space:nowrap}
.pc-h .ok{flex:none;width:16px;height:16px;border-radius:50%;background:var(--wc);color:#fff;font-size:9px;font-weight:900;display:flex;align-items:center;justify-content:center}
.pc-h b{font-size:12.5px;font-weight:900;color:var(--ink);line-height:1.3}
.pc p{font-size:10.5px;color:var(--muted);line-height:1.5;margin-top:4px;padding-left:23px}
.pc-f{font-size:9.5px;color:var(--wc);font-weight:800;margin-top:3px;padding-left:23px}
.pc-f .bx{width:12px;height:12px;border:1.3px solid var(--wc);border-radius:2px;font-size:8px;line-height:10px;text-align:center}

/* 장소정보 A · 아이콘 그리드 */
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:4px}
.tile{position:relative;background:#F6F8FA;border:1.5px solid #E6EAEF;border-radius:12px;padding:10px 6px 8px;text-align:center;cursor:pointer}
.tile .ic{font-size:20px;display:block}
.tile b{display:block;font-size:10.5px;font-weight:800;color:var(--ink);line-height:1.3;margin-top:4px;word-break:keep-all}
.tile i{position:absolute;right:5px;top:5px;width:13px;height:13px;border-radius:50%;background:var(--mc);color:#fff;font-size:8px;font-style:normal;font-weight:900;display:flex;align-items:center;justify-content:center}
.tile.on{background:#fff;border-color:var(--mc);box-shadow:0 0 0 2px var(--wc-bg)}
.sheet{margin-top:10px;background:#fff;border:1.5px solid var(--mc);border-radius:12px;padding:11px 12px;position:relative}
.sheet:before{content:"";position:absolute;left:14%;top:-7px;width:12px;height:12px;background:#fff;border-left:1.5px solid var(--mc);border-top:1.5px solid var(--mc);transform:rotate(45deg)}
.sh-h{display:flex;gap:8px;align-items:center}
.sh-h .ic{font-size:22px}
.sh-h b{display:block;font-size:12.5px;font-weight:900;color:var(--ink)}
.sh-h small{font-size:10px;color:var(--mc);font-weight:800}
.sheet p{font-size:11px;color:var(--txt);line-height:1.55;margin-top:7px}
.sh-f{font-size:9.5px;color:var(--muted);margin-top:6px}
/* 장소정보 B · 손님 질문형 */
.qg{margin-top:8px}
.qg-t{font-size:10px;font-weight:900;letter-spacing:.08em;color:var(--wc);padding:6px 0 2px}
.qi{padding:8px 0;border-top:1px solid var(--line)}
.qi .q{font-size:12px;font-weight:800;color:var(--ink);line-height:1.4}
.qi .q:before{content:"Q";color:var(--red);font-weight:900;margin-right:6px}
.qi .a{margin-top:4px;padding-left:16px;position:relative;line-height:1.5}
.qi .a:before{content:"A";position:absolute;left:0;top:0;color:var(--mc);font-weight:900;font-size:11px}
.qi .a b{display:block;font-size:12px;font-weight:800;color:var(--ink2)}
.qi .a small{display:block;font-size:10px;color:var(--muted);margin-top:2px}
.qi .a .chk{display:inline-block;font-size:9.5px;font-weight:800;color:var(--mc);margin-top:3px}
/* 장소정보 C · 기본정보 통합 */
.pl-t .badge{display:inline-block;font-size:9.5px;font-weight:800;color:#fff;background:var(--wc);border-radius:999px;padding:2px 8px;margin:0 0 0 8px;vertical-align:middle}
.pl-chips i.cc{color:var(--mc);background:#fff;border:1.3px solid var(--mc);font-weight:800}
.pl-chips i.cc.on{background:var(--mc);color:#fff}
.lgc{font-size:9.5px;color:var(--muted);margin-top:8px}
.lgc i{font-style:normal;font-size:9.5px;font-weight:800;color:var(--wc);border:1.3px solid var(--wc);border-radius:999px;padding:1px 6px;margin-right:2px}
.pop{position:relative;margin-top:10px;background:#1A1A1A;color:#fff;border-radius:10px;padding:10px 12px}
.pop-a{position:absolute;left:24px;top:-6px;width:12px;height:12px;background:#1A1A1A;transform:rotate(45deg)}
.pop b{display:block;font-size:12px;font-weight:900}
.pop p{font-size:10.5px;color:#D6DBE2;line-height:1.5;margin-top:4px}
.pop small{display:block;font-size:9.5px;color:#9FB4DC;margin-top:5px;font-weight:700}
.pvsel{display:flex;gap:5px;margin:0 0 8px}
.pvsel button{flex:1;font:inherit;font-size:11px;font-weight:800;padding:6px 0;border-radius:8px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.pvsel button.on{background:var(--wc);border-color:var(--wc);color:#fff}
.tsel{display:flex;gap:6px;margin:0 0 10px}
.tsel button{flex:1;font:inherit;font-size:12px;font-weight:800;padding:8px 0;border-radius:10px;border:1px solid #D9DCD6;background:#fff;color:var(--ink);cursor:pointer}
.tsel button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.ed .pt-ed .qq{font-size:10.5px;color:var(--muted);margin:-2px 0 6px}
.ed .note{font-size:10.5px;color:var(--muted);line-height:1.5}
/* 손님 화면 쪽 수정 표시 */
mark.ed{background:var(--amber-bg);color:inherit;box-shadow:0 0 0 2px var(--amber-bg);border-radius:2px}
.dp .say2{margin:0 24px 28px;background:#FFF8E8;border:1px solid #F3E2B8;border-radius:12px;padding:12px 14px;text-align:left}
.dp .say2 .lb{font-size:9.5px;letter-spacing:.1em;color:#9A6B12}
.dp .say2 p{font-size:13px;color:#111;font-weight:600;line-height:1.6;margin-top:4px}
.dp .say2 small{font-size:10.5px;color:#8A8A8A}
.dp .pt .pho{height:200px}
.dp .hr{height:300px}
.memo{max-width:1240px;margin:0 auto 40px;background:#fff;border-radius:12px;padding:16px 18px;font-size:12.5px;color:#3E444A;line-height:1.6}
.memo h2{margin:0 0 8px;font-size:15px;font-weight:900;color:var(--ink)}
.memo .tw{overflow-x:auto;margin-top:8px}
.memo table{width:100%;min-width:640px;border-collapse:collapse;font-size:12px}
.memo th,.memo td{border:1px solid var(--line);padding:7px 9px;vertical-align:top;text-align:left;line-height:1.5}
.memo th{background:#F6F7F4;font-weight:800;color:var(--ink);white-space:nowrap}
.memo .flag{display:inline-block;background:var(--amber-bg);color:var(--amber);font-weight:800;border-radius:3px;padding:0 5px;font-size:10.5px;margin-right:3px}
@media (max-width:760px){.top{padding:12px 0 0}.two-col{padding:0 0 40px;gap:16px}.col{width:100%}.ed{border-radius:0;box-shadow:none}.col h3{padding:0 16px}.memo{border-radius:0}}
"""

JS = r"""
const D = __DATA__;
const CHK = '__CHK__';
let cur = (location.hash.slice(1) in D) ? location.hash.slice(1) : 'chicken';
let typ = 'C';
const state = {};   // per biz: {sel:[...], about, pts:{i:copy}, say, example:false}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;');}
function fill(s, reg){return s.replace(/\{(\w+)\}/g,(m,k)=>reg[k]||m);}
function init(bk){const t=D[bk]; state[bk]={sel:[...t.default_sel], about:fill(t.about,t.reg), pts:{}, say:'', example:false}; t.items.forEach((it,i)=>state[bk].pts[i]=it.copy);}
Object.keys(D).forEach(init);
window.addEventListener('hashchange',()=>{const k=location.hash.slice(1); if(k in D){cur=k;render();}});
function mark(txt, base){ return txt!==base ? '<mark class="ed">'+esc(txt)+'</mark>' : esc(txt); }

function editorHtml(bk, s, withBiz){
  const t=D[bk], reg=t.reg;
  let h='';
  if(withBiz) h+='<div class="fs"><div class="lb">업종<small>등록 정보로 자동 선택</small></div><div class="seg">'+['chicken','care'].map(k=>`<button type="button" data-biz="${k}" class="${k===bk?'on':''}">${D[k].key}</button>`).join('')+'</div></div>';
  h+=`<div class="lock"><b>세스코가 입력 · ${t.owner}은 수정 불가</b><br>위생 등급 A · 점검일 ${reg.date} · 실측 ${reg.n}항목 · 리포트 No. ${reg.report}<br><b>등록 정보에서 자동</b> ${reg.name} · ${reg.cat} · ${reg.town} · ${reg.years}년 · 영업시간 · 메뉴 · 주차</div>`;
  h+=`<div class="fs"><div class="lb">① 우리 ${t.place}${t.place==='조리원'?'이':'가'} 특히 신경 쓰는 것<small>2~3개 선택 · 고른 순서대로 노출</small></div><div class="chk">`;
  t.items.forEach((it,i)=>{const on=s.sel.includes(i); const dis=!on&&s.sel.length>=3;
    h+=`<label class="${on?'on':''}${dis?' dis':''}"><input type="checkbox" data-i="${i}" ${on?'checked':''} ${dis?'disabled':''}><span>${it.label}<span class="cs ${it.cesco?'':'o'}">${it.cesco?'세스코 점검 항목':'매장 기록'}</span></span><span class="ord">${on?(s.sel.indexOf(i)+1):''}</span></label>`;});
  h+='</div></div>';
  h+=`<div class="fs"><div class="lb">② ${t.place} 소개<small>기본 문안이 들어 있어요 · 160자</small></div><textarea data-f="about" rows="4" class="${s.about!==fill(t.about,reg)?'changed':''}">${esc(s.about)}</textarea><div class="cnt">${s.about.length}/160</div></div>`;
  h+='<div class="fs"><div class="lb">③ 고른 항목의 설명<small>그대로 둬도 돼요 · 각 140자</small></div>';
  s.sel.forEach((i,n)=>{const it=t.items[i]; h+=`<div class="pt-ed"><div class="t">POINT 0${n+1}<span>${it.title.replace('<br>',' ')}</span></div><div class="qq">인터뷰형에선 이 질문의 답으로 나가요: “${it.q}”</div><textarea data-pt="${i}" rows="3" class="${s.pts[i]!==it.copy?'changed':''}">${esc(s.pts[i])}</textarea><div class="cnt">${s.pts[i].length}/140</div><div class="ph">사진 추가 (선택) · 없으면 점검 때 촬영한 사진</div></div>`;});
  h+='</div>';
  h+=`<div class="fs"><div class="lb">④ ${t.owner} 한마디<small>선택 · 40자</small></div><input type="text" data-f="say" value="${esc(s.say)}" placeholder="비워 두면 이 칸은 손님 화면에 안 나와요" class="${s.say?'changed':''}"><div class="cnt">${s.say.length}/40</div></div>`;
  h+='<div class="btns"><button type="button" data-act="reset">기본 내용으로 저장</button><button type="button" class="ex" data-act="example">수정한 내용으로 저장</button></div>';
  h+=`<div class="note">저장하면 손님 화면에 바로 반영돼요. 세스코 측정값·등급·점검일은 ${t.owner}이 바꿀 수 없어요. 주황색 칸이 ${t.owner}이 고친 곳이에요.</div>`;
  return h;
}

const TXT={title:'세스코가 전문적으로 체크했습니다', sub:'측정 장비로 직접 쟀어요. 도장이 찍혔으면 기준 안이에요', lg:'CESCO<br>측정', more:'자세히', seal:'CESCO', pass:'기준 안', date:'체크일', lvsep:' · '};
function toolsBlock(t, tv){
  const T=t.tools;
  if(tv==='A'){
    const rows=T.map(x=>`<div class="ri"><div class="rt"><b>${x.k}</b><span class="rs"><i>✓</i>${x.levels[0][0]}</span><small>측정 도구 · ${x.tool}</small></div><p class="re">${x.easy}</p><div class="rb" style="--w:${(100/x.levels.length).toFixed(2)}%">${x.levels.map((l,i)=>`<i class="${i===0?'on':''}"></i>`).join('')}</div><div class="rl">${x.levels.map((l,i)=>`<b class="${i===0?'on':''}">${l[0]}</b><span class="${i===0?'on':''}">${l[1]}</span>`).join('')}</div><p class="rq">${x.ex}</p></div>`).join('');
    return `<div class="tv-a"><div class="rh"><div><span class="no">CESCO · 측정 리포트</span><b>세스코가 전문적으로 체크했습니다</b></div><div class="dt">체크일<br><b>${T[0].date}</b></div></div>${rows}<div class="rf"><span>측정 장비로 직접 쟀어요. 기준 안이면 통과예요</span><span>${T.length}항목 모두 통과</span></div></div>`;
  }
  const detail=(x,i)=>`<div class="bp${i===0?' on':''}" data-tgp="${i}"><p class="be">${x.easy}</p><div class="bl">${x.levels.map((l,j)=>`<span class="${j===0?'on':''}" title="${l[1]}">${j===0?'✓ ':''}${l[0]}</span>`).join('')}<small>${x.levels[0][1]}</small></div><p class="bx">${x.ex}</p><div class="bdt">${TXT.date} ${x.date}</div></div>`;
  const head=(sub)=>`<div class="bh"><span class="lg">${TXT.lg}</span><div><b>${TXT.title}</b><small>${sub}</small></div></div>`;
  if(tv==='B'){
    const COL=['#0E8F4A','#E0A100','#E2641B','#C8102E'];
    const gauge=(x)=>{const n=x.levels.length; const r=44, cx=60, cy=56; const arc=(a0,a1)=>{const p=a=>[cx+r*Math.cos(Math.PI*(1-a)), cy-r*Math.sin(Math.PI*(1-a))]; const [x0,y0]=p(a0),[x1,y1]=p(a1); return `M${x0.toFixed(1)} ${y0.toFixed(1)}A${r} ${r} 0 0 1 ${x1.toFixed(1)} ${y1.toFixed(1)}`;};
      const segs=x.levels.map((l,i)=>`<path d="${arc(i/n+0.01,(i+1)/n-0.01)}" stroke="${COL[i]}" stroke-width="10" fill="none" stroke-linecap="butt" opacity="${i===0?1:.28}"/>`).join('');
      const a=0.5/n; const nx=cx+(r-16)*Math.cos(Math.PI*(1-a)), ny=cy-(r-16)*Math.sin(Math.PI*(1-a));
      return `<svg viewBox="0 0 120 64">${segs}<line x1="${cx}" y1="${cy}" x2="${nx.toFixed(1)}" y2="${ny.toFixed(1)}" stroke="#1A1A1A" stroke-width="2.5" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="4" fill="#1A1A1A"/><text x="${cx}" y="${cy-8}" text-anchor="middle" font-size="9" font-weight="900" fill="#0B5E31">✓</text></svg>`;};
    const gg=T.map((x,i)=>`<button type="button" class="g${i===0?' on':''}" data-tg="${i}">${gauge(x)}<div class="gk">${x.hl}<small>${x.k}${TXT.lvsep}${x.tool}</small></div><span class="gv">${x.levels[0][0]}${TXT.lvsep}${TXT.pass}</span><i class="more">${TXT.more}</i></button>`).join('');
    return `<div class="tv-b" data-tvbox>${head('측정 장비로 직접 쟀어요. 바늘이 초록이면 기준 안이에요')}<div class="gg">${gg}</div><div class="bd">${T.map(detail).join('')}</div></div>`;
  }
  if(tv==='D'){
    const gg=T.map((x,i)=>`<button type="button" class="g${i===0?' on':''}" data-tg="${i}"><span class="seal"><i>✓</i><small>${TXT.seal}</small></span><div class="gk">${x.hl}<small>${x.k}${TXT.lvsep}${x.tool}</small></div><i class="more">${TXT.more}</i></button>`).join('');
    return `<div class="tv-b tv-d" data-tvbox>${head(TXT.sub)}<div class="gg">${gg}</div><div class="bd">${T.map(detail).join('')}</div></div>`;
  }
  if(tv==='E'){
    const rows=T.map((x,i)=>`<button type="button" class="g${i===0?' on':''}" data-tg="${i}"><span class="ic">${x.ic}</span><div class="gk">${x.hl}<small>${x.k} · ${x.tool}</small></div><span class="gv">✓ 기준 안</span><span class="seg">${x.levels.map((l,j)=>`<i class="${j===0?'on':''}"></i>`).join('')}</span></button>`).join('');
    return `<div class="tv-b tv-e" data-tvbox>${head('측정 장비로 직접 쟀어요. 초록 칸이 기준 안이에요')}<div class="gg">${rows}</div><div class="bd">${T.map(detail).join('')}</div></div>`;
  }
  if(tv==='F'){
    const rows=T.map((x,i)=>`<button type="button" class="g${i===0?' on':''}" data-tg="${i}"><i class="ok">✓</i><div class="gk">${x.hl}<small>${x.k} · ${x.tool}</small></div><i class="more">자세히</i></button>`).join('');
    return `<div class="tv-b tv-f" data-tvbox><div class="top"><small>CESCO 전문 측정 · ${T[0].date}</small><b>${T.length}항목 모두 기준 안</b><span>측정 장비로 직접 쟀어요</span></div><div class="gg">${rows}</div><div class="bd">${T.map(detail).join('')}</div></div>`;
  }
  if(tv==='C'){
    const items=T.map(x=>`<div class="ci"><div class="ck">${x.k}<small>${x.tool}</small><span class="ok">✓ ${x.levels[0][0]}</span></div><p class="ce">${x.easy}</p><div class="ld">${x.levels.slice().reverse().map((l,i,arr)=>`<div class="${i===arr.length-1?'on':''}"><b>${l[0]}</b><span>${l[1]}</span></div>`).join('')}</div><div class="cm"><b>세스코 전문가 메모</b>${x.ex}</div><div class="cd">체크일 ${x.date}</div></div>`).join('');
    return `<div class="tv-c"><div class="ch"><span class="av">세스코<br>전문가</span><div><b>세스코가 전문적으로 체크했습니다</b><small>측정 장비로 직접 쟀어요. 기준 안이면 통과예요</small></div><span class="st">${T.length}항목<br>모두 통과</span></div><div class="tl2">${items}</div></div>`;
  }
  return `<div class="tools"><div class="tl-h"><span class="gold">CESCO<br>전문<br>측정</span><div><b>세스코가 전문적으로 체크했습니다</b><small>측정 장비로 직접 쟀어요. 기준 안이면 통과예요</small></div></div>${T.map(x=>`<div class="tl"><div class="tl-k">${x.k}<small>${x.tool}</small><span class="pass">기준 안 · ${x.levels[0][0]}</span></div><p class="tl-e">${x.easy}</p><div class="scale">${x.levels.map((l,i)=>`<div class="lv ${i===0?'on':''}">${l[0]}</div>`).join('')}</div><div class="lvd">${x.levels.map(l=>`<div><b>${l[0]}</b><span>${l[1]}</span></div>`).join('')}</div><p class="tl-x">${x.ex}</p><div class="tl-d">체크일 ${x.date}</div></div>`).join('')}</div>`;
}
function previewHtml(bk, typ, s, o){
  const t=D[bk], reg=t.reg, hc=t.hc; o=o||{}; const tab=o.tab||'hy', mt=o.mt||t.default_mt;
  const tabs=t.tabs.map(x=>`<span class="${x==='위생'?'on':''}">${x}</span>`).join('');
  const ai=[ `세스코가 ${reg.date}에 ${reg.n}가지를 직접 재서 모두 기준 안이었어요.`, `${t.owner}이 고른 관리 포인트: ${s.sel.map(i=>t.items[i].label).join(', ')}`, t.review ].map(x=>`<li>${x}</li>`).join('');
  const ms=hc.metrics.map(m=>`<div class="m"><div class="k">${m.k}<i>적합</i></div><div class="v">${m.v}${m.u?' <small>'+m.u+'</small>':''}</div><div class="bar"><i style="width:${m.pct}%"></i></div><div class="b">${m.base}</div></div>`).join('');
  const strip=t.strip.map(x=>`<div><b>${x[0]}</b><span>${x[1]}</span></div>`).join('');
  const pts=s.sel.map((i,n)=>{const it=t.items[i]; return `<div class="pt${n%2?' alt':''}"><div class="pho">사진 자리 · ${it.label}</div><div class="tx"><div class="num">POINT 0${n+1}</div><h3>${it.title}</h3><p>${mark(s.pts[i],it.copy)}</p><div class="fx"><i>${CHK}</i>${it.chip}</div></div></div>`;}).join('');
  const say = s.say ? `<div class="say2"><div class="lb">${t.owner} 한마디</div><p><mark class="ed">"${esc(s.say)}"</mark></p><small>${reg.name} ${t.owner}</small></div>` : '';
  const A=t.aicard;
  const aiHtml=`<div class="wai"><div class="wai-t"><span class="sp">✨</span>위쳌 AI<span class="inf">i</span></div><p class="wai-i">${A.intro}</p><ul>${A.checks.map(x=>`<li><span class="em">✅</span>${x}</li>`).join('')}</ul><div class="wai-h">매장정보</div><ul>${A.info.map(x=>`<li><span class="em">${x[0]}</span>${x[1]}</li>`).join('')}</ul><div class="wai-h">리뷰 한눈에</div><ul>${A.review.map(x=>`<li><span class="em">✅</span>${x}</li>`).join('')}</ul></div>`;
  const mem=t.members.find(m=>m.key===mt)||t.members[0];
  const cards=t.hcards.cards.filter(c=>mem.svcs.includes(c[0]));
  const N=cards.length;
  const mcol=svc=>svc==='FOOD'?t.members[1].color:svc==='CHECK'?'#1A3668':t.members[0].color;
  const P=t.placeinfo;
  const basicHtml=`<div class="binfo"><div class="bi"><span class="ic">📍</span><span>${P.addr}</span><b>복사 · 길찾기</b></div><div class="bi"><span class="ic">🕒</span><span>${P.hours}</span></div><div class="bi"><span class="ic">📞</span><span>${P.tel}</span><b>복사</b></div><div class="bi"><span class="ic">💳</span><span>${P.pay}</span></div><div class="bi"><span class="ic">#</span><span>${P.tags}</span></div><div class="bi"><span class="ic">🛋️</span><span>${P.conv.join(', ')}</span></div></div>`;
  const mtabs=`<div class="mtabs">${t.members.map(m=>`<button type="button" class="mtab ${m.key===mt?'on':''}" data-mt="${m.key}" style="--mc:${m.color}">${m.name}<small>${t.hcards.cards.filter(c=>m.svcs.includes(c[0])).length}</small></button>`).join('')}</div>`;
  const cardsHtml=cards.map((c,ci)=>`<div class="swc" style="--mc:${mem.color};--mbg:${mem.bg};--ml:${mem.line}"><div class="swin"><div class="swt"><span class="logo"><b>CESCO</b><i>${t.svc_en[c[0]]||c[0]}</i></span><span class="stamp"><svg viewBox="0 0 44 44" width="40" height="40"><circle cx="22" cy="22" r="20" fill="none" stroke="#8FA3BF" stroke-width="1.4"/><circle cx="22" cy="22" r="15" fill="none" stroke="#8FA3BF" stroke-width=".8"/><text x="22" y="20" text-anchor="middle" font-size="6.5" font-weight="800" fill="#6F86A6">CESCO</text><text x="22" y="28" text-anchor="middle" font-size="6.5" font-weight="800" fill="#6F86A6">CHECK</text></svg></span></div><div class="hk">${c[1]}</div><div class="hl">${c[2]}</div><div class="ck"><span class="bx">✓</span><span>[${c[3]}] ${c[4]} 체크 완료</span></div><div class="dt">최근 점검일 : 2026.${reg.date}</div><div class="rp">ⓘ 점검 리포트 보기</div></div></div>`).join('');
  const toolsHtml=toolsBlock(t, o.tv||'D');
  const M=t.placemeta, pv=o.pv||'A';
  const chkRow=(c,i)=>`<div class="pc${i===0?' first':''}" style="--mc:${mcol(c[0])}"><div class="pc-h"><span class="ok">✓</span><b>${c[1]}</b><span class="svc">${t.svc_ko[c[0]]||c[0]}</span></div><p>${c[2]}</p><div class="pc-f">세스코 체크 완료 · 2026.${reg.date} · 유효 3개월</div></div>`;
  const basicRows=`<div class="pl-row"><span>주소</span><span>${P.addr}</span></div><div class="pl-row"><span>${t.key==='산후조리원'?'상담·면회':'영업시간'}</span><span>${P.hours}</span></div><div class="pl-row"><span>전화</span><span>${P.tel}</span></div><div class="pl-row"><span>결제</span><span>${P.pay}</span></div>`;
  const convRow=`<div class="pl-row"><span>편의</span><span class="pl-chips">${P.conv.map(c=>`<i>${c}</i>`).join('')}</span></div><div class="pl-row"><span>태그</span><span>${P.tags}</span></div>`;
  const groups=[...new Set(M.map(m=>m[1]))];
  const cescoHead=(sub)=>`<div class="pl-t">세스코가 특별히 체크한 장소 정보<small>${sub}</small></div>`;
  let placeBody='';
  if(pv==='A'){
    const tiles=P.checks.map((c,i)=>`<div class="tile${i===0?' on':''}" style="--mc:${mcol(c[0])}"><span class="ic">${M[i][0]}</span><b>${M[i][3]}</b><i>✓</i></div>`).join('');
    const c0=P.checks[0];
    placeBody=`<div class="pl-sec"><div class="pl-t">기본 정보</div>${basicRows}${convRow}</div>
<div class="pl-sec cesco">${cescoHead('가 봐야만 아는 것 '+P.checks.length+'가지. 누르면 자세히 나와요')}<div class="tiles">${tiles}</div>
<div class="sheet" style="--mc:${mcol(c0[0])}"><div class="sh-h"><span class="ic">${M[0][0]}</span><div><b>${c0[1]}</b><small>${t.svc_ko[c0[0]]} · 세스코 체크 완료 2026.${reg.date}</small></div></div><p>${c0[2]}</p><div class="sh-f">3개월마다 다시 확인해요</div></div></div>`;
  } else if(pv==='B'){
    const qa=groups.map(g=>`<div class="qg"><div class="qg-t">${g}</div>${P.checks.map((c,i)=>M[i][1]===g?`<div class="qi" style="--mc:${mcol(c[0])}"><div class="q">${M[i][2]}</div><div class="a"><b>${c[1]}</b><small>${c[2]}</small><span class="chk">✓ 세스코 확인 · 2026.${reg.date}</span></div></div>`:'').join('')}</div>`).join('');
    placeBody=`<div class="pl-sec"><div class="pl-t">기본 정보</div>${basicRows}${convRow}</div>
<div class="pl-sec cesco">${cescoHead('가기 전에 많이 묻는 것들이에요. 답은 세스코가 가서 확인했어요')}${qa}</div>`;
  } else if(pv==='C'){
    const rows=groups.map(g=>`<div class="pl-row"><span>${g}</span><span class="pl-chips">${P.checks.map((c,i)=>M[i][1]===g?`<i class="cc${i===0?' on':''}" style="--mc:${mcol(c[0])}">✓ ${M[i][3]}</i>`:'').join('')}</span></div>`).join('');
    const c0=P.checks[0];
    placeBody=`<div class="pl-sec"><div class="pl-t">기본 정보<small class="badge">세스코 체크 ${P.checks.length} · 2026.${reg.date} · 유효 3개월</small></div>${basicRows}<div class="pl-row"><span>편의</span><span class="pl-chips">${P.conv.map(c=>`<i>${c}</i>`).join('')}</span></div>${rows}<div class="pl-row"><span>태그</span><span>${P.tags}</span></div>
<div class="lgc"><i>✓ 파란 칩</i>은 세스코가 가서 확인한 것, 회색은 등록 정보예요</div>
<div class="pop" style="--mc:${mcol(c0[0])}"><div class="pop-a"></div><b>${c0[1]}</b><p>${c0[2]}</p><small>${t.svc_ko[c0[0]]} · 세스코 체크 완료 2026.${reg.date}</small></div></div>`;
  } else {
    placeBody=`<div class="pl-sec"><div class="pl-t">기본 정보</div>${basicRows}${convRow}</div>
<div class="pl-sec cesco">${cescoHead('가 봐야만 아는 것 '+P.checks.length+'가지를 세스코가 가서 확인했어요')}${P.checks.map((c,i)=>chkRow(c,i)).join('')}</div>`;
  }
  const placeHtml=`<div class="place">${placeBody}</div>`;
  const headHtml=`
<div class="appbar"><button class="back" aria-label="뒤로 가기"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg></button><div class="t">${reg.name}</div></div>
<div class="head"><div class="pho2">사진 자리 · 대표 사진 (${t.owner} 업로드)</div><div class="nm" style="margin-top:12px"><span class="cat">${reg.cat}</span></div><div class="nm"><h2>${reg.name}</h2></div><div class="rv"><b>리뷰</b><span style="color:#0072CE;font-weight:700">${reg.rv.replace(/\D+/g,'')}개</span><span>· ${reg.town}</span></div></div>
<div class="body" style="padding-bottom:4px;background:#fff">${aiHtml}${basicHtml}</div>
<div class="tabs2"><span class="${tab==='hy'?'on':''}" data-tab="hy">위생정보</span><span class="${tab==='place'?'on':''}" data-tab="place">장소정보</span></div>` + (tab==='place' ? placeHtml : `
<div class="hc">
<div class="qt2">“${A.quote}”</div>
<div class="sh3">${t.sticker}<small>세스코 솔루션을 받는 항목</small></div>
${mtabs}
<div class="sw">${cardsHtml}</div>
<div class="swbar"><button type="button" class="swnav" data-d="p" aria-label="이전 카드">‹</button><div class="dots">${cards.map((c,ci)=>`<i class="${ci===0?'on':''}"></i>`).join('')}</div><button type="button" class="swnav" data-d="n" aria-label="다음 카드">›</button></div>
<div class="hcsum">세스코가 ${reg.date}에 직접 체크한 ${t.key} 위생 정보 ${t.hcards.cards.length}가지 · 위생 등급 <b>A</b></div>
${typ==='A'?'<div class="grid">'+ms+'</div>':''}</div>`);
  const bodyC=`<div class="dp">
<div class="hr"><div class="pho">사진 자리 · 대표 세로 컷 (사장님 또는 점검 촬영)</div><div class="ov"><span class="lab">${fill(t.hero_lab,reg)}</span><h1>${t.hero}</h1><div class="sub">${reg.name} · 세스코 위생 실측 A</div></div></div>
<div class="sec"><span class="lab">ABOUT</span><h2>${t.about_h}</h2><p>${mark(s.about, fill(t.about,reg))}</p><div class="strip">${strip}</div></div>
<div class="sec alt" style="padding-bottom:10px"><span class="lab">POINT</span><h2>${t.pt_h}</h2></div>
${pts}
${say}
<div style="height:8px"></div>
<div class="rep"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A3668" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg><div class="t">위생점검 리포트 No. ${reg.report}<small>세스코 전문가 현장 측정·서명 원본</small></div><a class="btn sec" href="#">원본 보기</a></div>
<p class="fine2">측정값은 점검일 기준이고, 다음 정기 점검 때 새로 바뀌어요. POINT는 ${t.owner}이 고른 항목이에요. "세스코 실측·확인" 표시가 있는 것만 세스코가 점검에서 직접 봤어요.</p>
</div>`;
  const repRow=`<div class="report"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1A3668" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg><div class="t">위생점검 리포트 No. ${reg.report}<small>세스코 전문가 현장 측정·서명 원본</small></div><a class="btn sec" href="#">원본 보기</a></div>`;
  const fine=`<p class="fine">측정값은 점검일 기준이고, 다음 정기 점검 때 새로 바뀌어요. 관리 포인트는 ${t.owner}이 고른 항목이에요. "세스코 실측·확인" 표시가 있는 것만 세스코가 점검에서 직접 봤어요.</p>`;
  const sayCard = s.say ? `<div class="card say"><div class="lb">${t.owner} 한마디</div><p><mark class="ed">"${esc(s.say)}"</mark></p><div class="sg">${reg.name} ${t.owner}</div></div>` : '';
  // A · 수치형
  const gauges=hc.metrics.map((m,mi)=>{
    const sel=s.sel.filter(i=>t.items[i].metric===mi);
    const why=sel.map(i=>`<div class="why1"><b>이 집은</b> ${mark(s.pts[i],t.items[i].copy)}</div>`).join('');
    return `<div class="r"><div class="k">${m.k}</div><div class="mt" style="margin-top:3px"><div class="mrow"><b>${m.v}</b>${m.u?'<small>'+m.u+'</small>':''}<span class="pill2">기준의 ${m.pct}%</span></div><div class="mb"><i style="width:${m.pct}%"></i></div><div class="ml"><span>0</span><span>${m.base}</span></div></div>${why}</div>`;}).join('');
  const rest=s.sel.filter(i=>t.items[i].metric<0);
  const restList = rest.length ? `<div class="card list"><div class="hd"><b>실측 항목 밖에서 ${t.owner}이 고른 것</b><span>매장 기록</span></div>${rest.map(i=>`<div class="row"><span style="width:8px;height:8px;border-radius:50%;background:#C9D0D8;display:block;margin:0 auto"></span><div class="k">${t.items[i].title.replace('<br>',' ')}<small>${mark(s.pts[i],t.items[i].copy)}</small></div><span class="tag o">매장 기록</span></div>`).join('')}</div>` : '';
  const bodyA=`<div class="body">
<div class="card intro"><div class="byline"><div class="av"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0072CE" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg></div><div><b>${reg.name}은요</b><span>${t.owner}이 적은 소개</span></div></div><p style="margin-top:8px">${mark(s.about, fill(t.about,reg))}</p></div>
<div class="sh2"><b>항목별로 얼마나 여유 있나</b><small>${reg.date} 세스코 실측 · 값과 기준선</small></div>
<div class="res">${gauges}</div>
${restList}
${sayCard}
${repRow}${fine}</div>`;
  // B · 인터뷰형 (셀프 인터뷰)
  const qa=s.sel.map(i=>{const it=t.items[i]; return `<div class="it"><div class="q">${it.q}</div><div class="a">${mark(s.pts[i],it.copy)}</div><div class="fact"><i>${CHK}</i>${it.chip}</div></div>`;}).join('');
  const pull = s.say ? `<div class="pull"><p><mark class="ed" style="background:transparent;box-shadow:none">"${esc(s.say)}"</mark></p><span>${reg.name} ${t.owner}</span></div>` : '';
  const bodyB=`<div class="body">
<div class="iv-hero"><div class="ph">사진 자리 · ${t.owner} · 대표 컷 (${t.owner} 업로드 또는 점검 촬영)</div><div class="eb">${t.owner} 셀프 인터뷰 · ${reg.date} 점검 후</div><h3>${t.about_h}</h3><div class="who">${reg.name} · 질문은 위쳌이, 답은 ${t.owner}이 직접 적었어요</div></div>
<div class="card intro"><p>${mark(s.about, fill(t.about,reg))}</p></div>
<div class="card iv">${qa}</div>
${pull}
${repRow}${fine}</div>`;
  const body = typ==='A'?bodyA : typ==='B'?bodyB : bodyC;
  return headHtml + (tab==='place'?'':body) + `<div class="tools-wrap">${toolsHtml}</div>` + `<div class="actions"><div class="ico">전화</div><div class="ico">저장</div><div class="cta">${t.cta}</div></div>`;
}
function refreshPreviews(bk){
  document.querySelectorAll('[data-tools]').forEach(el=>{ if(el.dataset.biz===bk) el.innerHTML='<div class="tools-wrap">'+toolsBlock(D[bk], el.dataset.tv)+'</div>'; });
  document.querySelectorAll('[data-static]').forEach(el=>{ if(el.dataset.biz===bk) el.innerHTML=previewHtml(bk, el.dataset.t, state[bk], {tab:el.dataset.tab, mt:el.dataset.mt, pv:el.dataset.pv, tv:el.dataset.tv}); });
}
function refresh(bk){
  document.querySelectorAll('[data-ed]').forEach(el=>{ if(el.dataset.biz===bk) el.innerHTML=editorHtml(bk, state[bk], el.hasAttribute('data-withbiz')); });
  refreshPreviews(bk);
}
const edIn=document.getElementById('ed-in'), pv=document.getElementById('pv');
function render(){
  if(edIn){ edIn.dataset.biz=cur; pv.dataset.biz=cur; pv.dataset.t=typ; document.querySelectorAll('.tsel button').forEach(b=>b.classList.toggle('on',b.dataset.t===typ)); }
  Object.keys(D).forEach(refresh);
}
document.addEventListener('click',e=>{
  const tb=e.target.closest('.tsel button[data-t]'); if(tb){typ=tb.dataset.t; render(); return;}
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const b=e.target.closest('button[data-biz]'); if(b){cur=b.dataset.biz;history.replaceState(null,'','#'+cur);render();return;}
  const a=e.target.closest('button[data-act]'); if(!a) return;
  const t=D[bk]; if(a.dataset.act==='reset'){init(bk);} else {const s=state[bk]; s.about=t.edit.about; Object.entries(t.edit.pts).forEach(([i,c])=>{i=+i; if(!s.sel.includes(i)) s.sel=[i,...s.sel].slice(0,3); s.pts[i]=c;}); s.say=t.edit.say;}
  refresh(bk);
});
document.addEventListener('change',e=>{
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const c=e.target; if(c.type!=='checkbox') return; const s=state[bk], i=+c.dataset.i;
  if(c.checked){ if(!s.sel.includes(i)&&s.sel.length<3) s.sel.push(i);} else s.sel=s.sel.filter(x=>x!==i);
  refresh(bk);
});
document.addEventListener('input',e=>{
  const ed=e.target.closest('[data-ed]'); if(!ed) return; const bk=ed.dataset.biz;
  const el=e.target, s=state[bk];
  if(el.dataset.f==='about') s.about=el.value.slice(0,160);
  else if(el.dataset.f==='say') s.say=el.value.slice(0,40);
  else if(el.dataset.pt!==undefined) s.pts[+el.dataset.pt]=el.value.slice(0,140);
  else return;
  const t=D[bk]; el.classList.toggle('changed', el.dataset.f==='about'? s.about!==fill(t.about,t.reg) : el.dataset.f==='say'? !!s.say : s.pts[+el.dataset.pt]!==t.items[+el.dataset.pt].copy);
  el.parentElement.querySelector('.cnt').textContent=el.value.length+'/'+(el.dataset.f==='about'?160:el.dataset.f==='say'?40:140);
  refreshPreviews(bk);
});
document.addEventListener('click',e=>{
  const tb=e.target.closest('.tabs2 span[data-tab]'); if(tb){const el=tb.closest('[data-static]'); if(el){el.dataset.tab=tb.dataset.tab; el.innerHTML=previewHtml(el.dataset.biz, el.dataset.t, state[el.dataset.biz], {tab:el.dataset.tab, mt:el.dataset.mt, pv:el.dataset.pv, tv:el.dataset.tv});} return;}
  const pb=e.target.closest('.pvsel button[data-pv]'); if(pb){const el=document.querySelector(pb.closest('.pvsel').dataset.for); if(el){el.dataset.pv=pb.dataset.pv; el.dataset.tab='place'; el.innerHTML=previewHtml(el.dataset.biz, el.dataset.t, state[el.dataset.biz], {tab:el.dataset.tab, mt:el.dataset.mt, pv:el.dataset.pv, tv:el.dataset.tv}); pb.parentElement.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b===pb));} return;}
  const tg=e.target.closest('[data-tvbox] .g[data-tg]'); if(tg){const box=tg.closest('[data-tvbox]'); const k=tg.dataset.tg; const open=!tg.classList.contains('on'); box.querySelectorAll('.g').forEach(b=>b.classList.toggle('on',open&&b.dataset.tg===k)); box.querySelectorAll('.bp').forEach(b=>b.classList.toggle('on',open&&b.dataset.tgp===k)); return;}
  const mb=e.target.closest('.mtab[data-mt]'); if(mb){const el=mb.closest('[data-static]'); if(el){el.dataset.mt=mb.dataset.mt; el.innerHTML=previewHtml(el.dataset.biz, el.dataset.t, state[el.dataset.biz], {tab:el.dataset.tab, mt:el.dataset.mt, pv:el.dataset.pv, tv:el.dataset.tv});} return;}
});
function swGo(sw,k){const n=sw.children.length; k=(k+n)%n; const c=sw.children[k]; sw.scrollTo({left:c.offsetLeft-(sw.clientWidth-c.offsetWidth)/2-sw.offsetLeft*0,behavior:'smooth'});}
document.addEventListener('click',e=>{
  const dot=e.target.closest('.hc .dots i'); if(dot){const sw=dot.closest('.hc').querySelector('.sw'); swGo(sw,[...dot.parentElement.children].indexOf(dot)); return;}
  const nav=e.target.closest('.hc .swnav'); if(nav){const sw=nav.closest('.hc').querySelector('.sw'); const cur=[...sw.closest('.hc').querySelectorAll('.dots i')].findIndex(d=>d.classList.contains('on')); swGo(sw,cur+(nav.dataset.d==='n'?1:-1)); return;}
  const card=e.target.closest('.hc .swc'); if(card){const sw=card.parentElement; const i=[...sw.children].indexOf(card); const cur=[...sw.closest('.hc').querySelectorAll('.dots i')].findIndex(d=>d.classList.contains('on')); swGo(sw, i===cur? i+1 : i);}
});
document.addEventListener('scroll',e=>{const sw=e.target; if(!sw.classList||!sw.classList.contains('sw')) return; const w=sw.firstElementChild?sw.firstElementChild.offsetWidth+12:1; const k=Math.round(sw.scrollLeft/w); sw.parentElement.querySelectorAll('.dots i').forEach((d,i)=>d.classList.toggle('on',i===k));},true);
render();
"""

def js_block():
    return JS.replace('__DATA__', json.dumps(DATA, ensure_ascii=False)).replace('__CHK__', B.CHK.replace("'", "\\'"))

def build():
    rows = ''
    for k, t in TPL.items():
        if k == 'meat': continue
        for i, (a, b, c, e, f) in enumerate(t['items'], 1):
            rows += f'<tr><td>{t["key"]}</td><td>{i}</td><td>{a}</td><td>{b.replace("<br>"," ")}</td><td>{c}</td><td>{e}</td></tr>'
    doc = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>위쳌 기본 템플릿 + 사장님 선택·수정 (10/28)</title>{B.FONT}<style>{B.CSS}{EXTRA_CSS}</style></head>
<body>
<div class="top"><div class="desc"><h1>위쳌 사업장 상세 — 기본 템플릿은 이미 채워져 있고, 사장님은 2~3개만 고르고, 원하면 고친다</h1>
<p>왼쪽은 <b>사장님 편집 화면</b>, 오른쪽은 <b>손님이 보는 화면</b>입니다. 업종을 고르면 기본 문안이 다 들어간 페이지가 바로 나오고(0 입력 상태), 특장점을 체크하면 그 순서대로 POINT가 바뀌고, 입력칸의 글을 고치면 오른쪽에 바로 반영됩니다. 고친 곳은 주황색으로 보입니다(검토용). "수정한 내용으로 저장"을 누르면 사장님이 손본 상태가 어떻게 달라지는지 볼 수 있습니다. 세스코 측정값·등급·점검일·등록 정보는 사장님이 못 건드립니다.</p></div></div>
<div class="two-col">
<div class="col"><h3>사장님 편집 화면<small>위쳌 사업주용 · 기본 문안이 미리 들어 있음</small></h3><div class="ed"><div class="bar">위생 페이지 관리<span class="sv">저장</span></div><div class="in" id="ed-in" data-ed data-withbiz data-biz="chicken"></div></div></div>
<div class="col"><h3>손님이 보는 화면<small>같은 데이터로 유형만 바꿔 봅니다 · 편집 즉시 반영</small></h3><div class="tsel"><button type="button" data-t="A">수치형</button><button type="button" data-t="B">인터뷰형</button><button type="button" data-t="C" class="on">상세페이지형</button></div><div class="phone"><div class="fold"><span>첫 화면 끝</span></div><div id="pv" data-static data-biz="chicken" data-t="C"></div></div></div>
</div>
<div class="memo"><h2>구조 메모</h2>
<div class="tw"><table><thead><tr><th style="width:18%">단계</th><th style="width:32%">누가 무엇을</th><th>화면에 나오는 것</th></tr></thead><tbody>
<tr><td><b>0 · 기본 제공</b></td><td>세스코 점검 데이터 + 등록 정보만 있음. 사장님 입력 없음</td><td>업종 기본 소개 문구, 업종 기본 특장점 3개(기본 선택), 기본 문안 그대로. 이 상태로도 완성된 페이지</td></tr>
<tr><td><b>1 · 고르기</b></td><td>사장님이 특장점 10개 중 2~3개 체크 (고른 순서 = 노출 순서)</td><td>POINT 01~03이 고른 항목의 기본 문안으로 바뀜. AI 요약 두 번째 줄도 같이 바뀜</td></tr>
<tr><td><b>2 · 고치기</b></td><td>사장님이 소개(160자)·항목 설명(140자)·한마디(40자)를 고침. 사진 추가</td><td>고친 문장만 바뀜. 안 고친 칸은 기본 문안 유지. 한마디는 적었을 때만 나옴</td></tr>
<tr><td><b>유형 (세스코가 정함)</b></td><td>수치형 · 인터뷰형 · 상세페이지형. 사장님 입력은 세 유형 공통</td><td>수치형: 실측 계기판 아래 "이 집은 ~"로 사장님 문장이 붙음. 인터뷰형: 고른 항목이 질문이 되고 사장님 문장이 답이 됨(셀프 인터뷰). 상세페이지형: POINT 01~03</td></tr>
<tr><td><b>세스코 전용</b></td><td>측정값·등급·점검일·리포트·"세스코 확인" 칩</td><td>사장님이 못 바꿈. 사장님이 고른 항목이라도 점검 항목이 아니면 POINT 아래 칩이 "매장 기록"으로만 표시</td></tr>
</tbody></table></div>
<p style="margin-top:10px"><span class="flag">확인 필요</span>글자 수 상한(160·140·40), 사진 장수, 사장님 수정분의 검수 여부(자동 게시 vs 세스코 승인 후 게시), 금지어 필터(가이드라인 표기법 ⑭⑮) 적용 위치.</p>
<h2 style="margin-top:18px">업종별 기본 문안 20개 (치킨집·산후조리원 특장점 선택 항목)</h2>
<p>각 항목은 제목 2줄 + 설명 2~3문장 + 세스코 확인 칩 조건으로 한 벌입니다. 수치·법령·효능 표현은 넣지 않았고, 매장이 하는 "행동"만 적었습니다. 사장님은 설명 문장만 고칠 수 있고 제목과 칩은 고정입니다.</p>
<div class="tw"><table><thead><tr><th>업종</th><th>#</th><th>선택 항목</th><th>제목(고정)</th><th>기본 설명(사장님 수정 가능)</th><th>칩</th></tr></thead><tbody>{rows}</tbody></table></div>
</div>
<script>{js_block()}</script>
</body></html>'''
    with open(os.path.join(OUT, FNAME), 'w', encoding='utf-8') as f:
        f.write(doc)
    print('wrote', FNAME)

if __name__ == '__main__':
    build()
