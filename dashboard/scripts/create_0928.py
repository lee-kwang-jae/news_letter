# -*- coding: utf-8 -*-
import os
import shutil
import re

source_path = 'dashboard/news/kj_hanam_inside_20260923.html'
target_path = 'dashboard/news/kj_hanam_inside_20260928.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

img_dir = 'images'
dash_img_dir = 'dashboard/news/images'
os.makedirs(img_dir, exist_ok=True)
os.makedirs(dash_img_dir, exist_ok=True)

today_dir = os.path.join(img_dir, 'today')
# (원본 파일명, 저장 파일명) - 092803은 .jpeg 로 전달됨
for src_name, dst_name in [('092801.jpg', '092801.jpg'), ('092802.jpg', '092802.jpg'),
                           ('092803.jpeg', '092803.jpg'), ('092804.jpg', '092804.jpg'),
                           ('092805.jpg', '092805.jpg')]:
    src_today = os.path.join(today_dir, src_name)
    if os.path.exists(src_today):
        shutil.copy2(src_today, os.path.join(img_dir, dst_name))
        shutil.copy2(src_today, os.path.join(dash_img_dir, dst_name))
    elif os.path.exists(os.path.join(img_dir, dst_name)):
        shutil.copy2(os.path.join(img_dir, dst_name), os.path.join(dash_img_dir, dst_name))

primary_thumb = os.path.join(img_dir, 'thumbnail-928.jpg')
if os.path.exists(os.path.join(img_dir, '092804.jpg')):
    shutil.copy2(os.path.join(img_dir, '092804.jpg'), primary_thumb)
elif os.path.exists(os.path.join(img_dir, '092801.jpg')):
    shutil.copy2(os.path.join(img_dir, '092801.jpg'), primary_thumb)

if os.path.exists(primary_thumb):
    shutil.copy2(primary_thumb, os.path.join(dash_img_dir, 'thumbnail-928.jpg'))

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title, Issue Number, Date, Meta Image Tags
content = content.replace("46호 | 2026년 9월 23일 발행", "47호 | 2026년 9월 28일 발행")
content = content.replace("2026년 9월 23일 기준", "2026년 9월 28일 기준")

# Update og:image tags with thumbnail-928.jpg (900x600)
og_thumb_url = "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-928.jpg?v=2026092801"
content = re.sub(r'content="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'content="{og_thumb_url}"', content)
content = re.sub(r'href="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'content="{og_thumb_url}"', content)
content = content.replace('<meta property="og:image:width" content="996"/>', '<meta property="og:image:width" content="900"/>')
content = content.replace('<meta property="og:image:height" content="555"/>', '<meta property="og:image:height" content="600"/>')
content = content.replace('<meta name="twitter:image:width" content="996"/>', '<meta name="twitter:image:width" content="900"/>')
content = content.replace('<meta name="twitter:image:height" content="555"/>', '<meta name="twitter:image:height" content="600"/>')

# 1. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 현장일지 & 언론보도 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- [현장일지 1] (네이버 블로그: 이광재, [덕풍시장·신장시장에서 나눈 추석 인사]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224421064330" target="_blank" style="color: inherit; text-decoration: none;">이광재, "덕풍시장·신장시장에서 나눈 추석 인사"… 올해부터 덕풍시장까지 사랑나눔 확대, 연휴 후 상인회와 발전 방안 논의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
추석을 앞둔 9월 23일, 신장시장과 덕풍시장을 찾아 명절 준비로 분주한 상인분들께 인사를 드렸습니다. 그동안 신장시장에서 이어온 추석맞이 전통시장 사랑나눔 행사를 올해부터 덕풍시장에서도 함께 열게 됐습니다. 신장시장 상인회장님, 오랫동안 덕풍시장을 지켜온 김재근 회장님과 시장을 더 좋게 만들 방법을 이야기했습니다. 연휴가 끝나면 상인회 분들과 구체적인 발전 방안을 논의하는 자리를 마련할 계획입니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="images/092804.jpg" alt="추석맞이 전통시장 사랑나눔 (덕풍전통시장)" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224421064330" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [현장일지 2] (네이버 블로그: 이광재, [나라를 지킨 분들, 가까운 병원에서 제때]) -->
<div class="article-card card-field" style="margin-top: 16px;">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224421191433" target="_blank" style="color: inherit; text-decoration: none;">이광재, "나라를 지킨 분들, 가까운 병원에서 제때"… 하남시보훈회관 방문·보훈 위탁병원 확충 건의 약속</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
추석을 앞두고 하남시보훈회관을 찾아 보훈단체 어르신들께 인사를 드렸습니다. 이 자리에서 가장 시급한 과제로 병원 문제가 제기됐습니다. 하남 관내에는 안과 진료를 하는 보훈 위탁병원이 없고, 중앙보훈병원은 진료 예약에 석 달이 걸린다는 말씀이었습니다. 긴 대기시간과 위탁병원 문제를 꼼꼼히 살피고 권오을 국가보훈부 장관께 직접 건의해, 하남의 국가유공자분들이 가까운 병원에서 제때 진료받을 수 있는 길을 열겠다고 약속했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="images/092805.jpg" alt="하남시보훈회관 방문" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224421191433" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [언론보도 1] (경기일보: 이광재 예결위원장 "국민 세금 실질적 효과가 예산심사 기준") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kyeonggi.com/article/20260913580277" target="_blank" style="color: inherit; text-decoration: none;">[경기일보] 이광재 예결위원장 "국민 세금의 실질적 효과가 예산심사 기준"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장(하남갑)은 경기일보 인터뷰에서 "수도권이라는 한 단어로 경기도 31개 시군을 묶을 수 없다"며, 820조 원 규모의 2027년 예산을 지역이 아닌 '국민 삶의 변화'를 기준으로 심사하겠다고 밝혔습니다. 일자리·주택·보육·교육·의료·연금 6개 분야의 효과를 숫자로 검증하고, 여야 구분 없이 객관적 성과지표(KPI)로 심사하겠다는 방침입니다. 하남 현안으로는 교산신도시 철도망(3호선 연장·위례신사선·GTX-D), AI 연구캠퍼스 조성, 남한중학교 복합화(국비 240억 원 확보), 24시간 어린이병원 추진을 꼽았습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kyeonggi.com/article/20260913580277" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경기일보) →</a></div>
</div>
<div class="source">
📌 출처: 경기일보 (김영호 기자)
</div>
</div>

</div>"""

# 2. Section 2: 하남 지역 주요 뉴스
section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (KBS: 한밤중 하남 산부인과 건물서 불…산모·아기 등 60여명 대피) -->
<div class="article-card">
<div class="badge">📰 사건사고/안전</div>
<h3><a href="https://news.kbs.co.kr/news/pc/view/view.do?ncd=8671837&amp;ref=A" target="_blank" style="color: inherit; text-decoration: none;">한밤중 하남 산부인과 건물서 불…산모·아기 등 60여 명 대피</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
9월 26일 새벽 0시 20분쯤 하남시 풍산동의 산부인과가 입주한 건물에서 불이 나 20여 분 만에 진화됐습니다. 인명 피해는 없었지만 5층 산부인과와 6~7층 산후조리원에 있던 산모와 아기 등 60여 명이 대피했습니다. 불은 휴게실과 세탁실이 있는 7층에서 시작된 것으로 추정되며, 경찰과 소방 당국은 오늘(28일) 합동 감식을 통해 정확한 화재 경위를 조사할 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://news.kbs.co.kr/news/pc/view/view.do?ncd=8671837&amp;ref=A" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (KBS) →</a></div>
</div>
<div class="source">
📌 출처: KBS (이희연 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (하남일보: "하남 교산은 언제 내 집 되나!") -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge">📰 부동산/교산신도시</div>
<h3><a href="http://m.hanamilbo.net/news/articleView.html?idxno=12664" target="_blank" style="color: inherit; text-decoration: none;">"하남 교산은 언제 내 집 되나!"… 본청약 7개월 지연·분양가 17% 상승에 사전청약자 속앓이</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남교산신도시 첫 본청약 단지인 A2블록은 당초 계획보다 약 7개월 늦게 본청약이 시작됐고, 입주 예정일도 2027년 3월에서 2029년 6월로 2년 3개월가량 밀렸습니다. 전용 59㎡ 분양가는 사전청약 추정가 4억 8,695만 원에서 최고 약 5억 7,000만 원으로 17% 안팎 올랐습니다. 교산 전체 사전청약 당첨자 1,508명 중 308명(20.4%)이 취소·포기했고, A2블록 본청약 신청률은 84.1%로 138가구가 일반공급으로 전환됐습니다. 후속 블록의 공급 일정 관리가 주요 변수로 꼽힙니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="http://m.hanamilbo.net/news/articleView.html?idxno=12664" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (하남일보) →</a></div>
</div>
<div class="source">
📌 출처: 하남일보 (이재연 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (뉴스투데이24: 하남시, 공무원 정원 29명 늘어난다) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge">📰 지방행정/조직개편</div>
<h3><a href="http://www.newstoday.or.kr/news/articleView.html?idxno=27472" target="_blank" style="color: inherit; text-decoration: none;">하남시, 공무원 정원 29명 늘어난다… 노인·장애인복지과 분리, '원스톱민원과' 신설</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 지방공무원 정원을 1,103명에서 1,132명으로 29명 늘리는 규정 개정안을 입법예고했습니다. 9급이 14명으로 가장 많이 늘고 8급 7명, 6·7급 각 3명이 증원되며, 본청 정원은 667명에서 693명으로 26명 늘어납니다. 5급 1명 증원은 노인장애인복지과를 노인복지과와 장애인복지과로 분리하는 데 따른 것이며, 민원여권과는 '원스톱민원과'로 이름이 바뀝니다. 개정 규정은 10월 26일부터 시행됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="http://www.newstoday.or.kr/news/articleView.html?idxno=27472" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴스투데이24) →</a></div>
</div>
<div class="source">
📌 출처: 뉴스투데이24 (윤제양 기자)
</div>
</div>
</div>"""

# 3. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">추석 연휴(9.24~9.27) 동안 하남 지역 맘카페(미사맘스클럽, 아이품애 하남맘, 하남맘 모여라, 슬기로운 위례생활, 위례에서 공부하기 등)에서 가장 많이 오르내린 HOT 이슈 TOP 3입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ [안전] "산부인과·조리원 화재, 어디예요?"… 풍산동 산부인과 건물 새벽 화재에 산모·예비맘 불안</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 26일 새벽 풍산동 산부인과·산후조리원 건물 화재 소식이 알려지자 맘카페에는 "풍산동 산부인과 두 곳 중 어디냐"는 문의 글이 잇따랐습니다. 이후 해당 병원(연세아란산부인과)이 공식 카페에 사과문을 올리고, 화재가 8층 세탁실 건조기에서 시작된 것으로 파악됐다고 밝혔습니다. 병원은 시설 정비와 안전점검을 위해 9월 29일까지 휴진하고 9월 30일부터 정상 진료를 재개한다고 공지했습니다.</div>
<div class="mom-point">💡 주민 포인트: 해당 병원에 진료 예약이 있는 산모는 휴진 공지를 확인하고 병원에 일정을 직접 문의하세요. 산후조리원을 고를 때는 대피 동선과 비상구, 소방 설비도 함께 확인하는 것이 좋습니다.</div>
<div class="mom-reaction">💬 주민 반응: "피해 보신 분 없죠?"라며 걱정하는 글이 많았고, 29일 진료 예약이 있었는데 개별 연락 없이 공지만 올라왔다는 아쉬움, 신생아가 있는 조리원 운영은 언제 재개되는지 묻는 글도 이어졌습니다.</div>
<div class="source" style="margin-top: 8px;">📌 출처: 네이버 카페 (하남맘 모여라, 맘스홀릭 베이비, 하남미사연세아란산부인과 공식 카페)</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ [연휴 생활정보] "오늘 문 연 병원·마트 어디예요?"… 연휴 영업 정보 공유 봇물</h4>
<div class="mom-detail"><strong>현황:</strong> 연휴 내내 문 연 병원과 마트, 떡집을 묻고 답하는 글이 이어졌습니다. 미사맘스클럽에는 "연휴에 문 연 이비인후과가 많지 않아 오픈 시간에 사람이 몰리니 2시간쯤 뒤에 가는 게 좋다"는 후기와 하나로마트 추석 당일 영업(12:00~18:00) 정보가 올라왔습니다. 위례 카페에서는 스타필드위례가 연휴 내내 운영하되 추석 당일에는 낮 12시에 문을 열고, 트레이더스·노브랜드는 추석 당일 휴무라는 정보가 공유됐습니다.</div>
<div class="mom-point">💡 주민 포인트: 명절이나 휴일에 아이가 아프면 응급의료포털(e-gen.or.kr)이나 129에서 문 연 병원·약국을 확인하고, 야간·휴일에 소아 진료를 하는 '달빛어린이병원'도 미리 알아두세요.</div>
<div class="mom-reaction">💬 주민 반응: "떡을 사야 하는데 추석 당일 문 여는 떡집 있을까요?" 같은 급한 문의에 이웃들이 댓글로 정보를 나누며, 명절마다 맘카페가 '동네 생활 안내소' 역할을 톡톡히 했습니다.</div>
<div class="source" style="margin-top: 8px;">📌 출처: 네이버 카페 (미사강변도시 미사맘스클럽, 슬기로운 위례생활)</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ [교육] "연휴 끝나면 바로 중간고사"… 시험기간과 겹친 추석에 학부모 고민</h4>
<div class="mom-detail"><strong>현황:</strong> 올해 추석 연휴가 중·고등학교 2학기 중간고사 기간과 겹치면서, 시험 때문에 아이와 함께 시골이나 친척 집에 가지 않고 집에 남았다는 글이 여러 카페에 올라왔습니다. 연휴 중 스터디카페에 자리가 없어 대형 카페를 찾아다녔다는 후기도 있었고, 하남미사교산4050 카페에서는 연휴 중에 열린 입시설명회 신청 정보가 공유됐습니다.</div>
<div class="mom-point">💡 주민 포인트: 연휴 직후 시험이 있는 가정은 학교 알리미로 시험 일정을 다시 확인하고, 연휴 동안 흐트러진 수면·생활 리듬을 시험 전에 되찾도록 도와주세요.</div>
<div class="mom-reaction">💬 주민 반응: "쉬어야 한다는 아이와 공부시키려는 엄마 사이에서 결국 가정의 평화를 택했다", "이럴 거면 할머니 댁에 갈 걸 그랬다"며 공감하는 댓글이 줄을 이었습니다.</div>
<div class="source" style="margin-top: 8px;">📌 출처: 네이버 카페 (위례에서 공부하기, 미사강변도시 미사맘스클럽, 하남미사교산4050)</div>
</div>
</div>"""

# 4. Section 4: ALL IN 하남라이프
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 28일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (하남시 문화행사: 제26회 하남문학 작품공모) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">✍️ ~2026.09.30(수) 마감 | 문학 공모전</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/sosik/selectClturEventWebView.do?pageUnit=6&amp;pageIndex=1&amp;searchCnd=all&amp;key=10059&amp;clturEventNo=142" target="_blank" style="color: inherit; text-decoration: none;">제26회 하남문학 작품공모 (마감 임박)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"천고마비의 가을, 잠재된 문학의 소질을 펼쳐 보세요!"</b><br/>
지역 문화와 향토 문학 발전을 위한 하남문학공모전이 열립니다. 시·동시와 수필·콩트 분야에 관심 있는 학생과 일반인(기성 작가 제외) 누구나 응모할 수 있으며, 공모 마감이 이번 주 수요일입니다.<br/><br/>
<b>🗓 공모기간:</b> 2026년 9월 1일 ~ 9월 30일(수)<br/>
<b>📝 공모분야:</b> 시·동시(8~20행), 수필·콩트(A4 3쪽 이내)<br/>
<b>💡 응모주제:</b> 하남, 신발, 한글, 은행나무, 철새<br/>
<b>👥 응모자격:</b> 5세 이상 하남시민 (하남 소재 직장인 포함)<br/>
<b>📧 접수:</b> 이메일 hanampen@naver.com (제목: 하남문학공모전-분야-이름)<br/>
<b>🏆 시상:</b> 대상 1명(50만 원) 등 총 88명 / 발표 10월 12일(월)<br/>
<b>☎️ 문의:</b> (사)한국문인협회 하남지부 <a href="tel:010-8211-4568" style="color:#3182ce; font-weight:bold;">010-8211-4568</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectClturEventWebView.do?pageUnit=6&amp;pageIndex=1&amp;searchCnd=all&amp;key=10059&amp;clturEventNo=142" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청서 받기 (하남시청) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092801.jpg" alt="제26회 하남문학 작품공모" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 문화행사 / (사)한국문인협회 하남지부
</div>
</div>

<!-- 문화 기사 2 (미사도서관: 10월 책 읽어주는 날) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795; margin-top: 16px;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📖 2026.10월 매주 수·목 | 북스타트/영유아</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr/mslib/selectBbsNttView.do?key=695&amp;bbsNo=106&amp;nttNo=89885&amp;integrDeptCode=mslib" target="_blank" style="color: inherit; text-decoration: none;">미사도서관 10월 '책 읽어주는 날' 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"북스타트 프로그램 &lt;책 읽어 주세요&gt;, 아이와 함께 그림책 속으로!"</b><br/>
미사도서관 유아자료실에서 10월 한 달간 영유아와 가족을 위한 '책 읽어주는 날'을 운영합니다.<br/><br/>
<b>🗓 일정:</b> 10월 1·8·14·15·21·22·28·29일 10:30 / 15:30, 10월 7일(수) 10:30<br/>
<b>🚫 휴관·미운영:</b> 10월 3일(개천절), 5일(대체공휴일), 6·13·20일(휴관일), 9일(한글날)<br/>
<b>📍 장소:</b> 하남시 미사도서관 1층 유아자료실<br/>
<b>⚠️ 참고:</b> 학기 중 오전 시간은 단체 견학 중심으로 운영되며, 견학이 취소되면 운영하지 않을 수 있습니다.<br/>
<b>☎️ 문의:</b> 미사도서관 <a href="tel:031-790-6864" style="color:#3182ce; font-weight:bold;">031-790-6864</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/mslib/selectBbsNttView.do?key=695&amp;bbsNo=106&amp;nttNo=89885&amp;integrDeptCode=mslib" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 보기 (미사도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092802.jpg" alt="미사도서관 10월 책 읽어주는 날" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 미사도서관
</div>
</div>

<!-- 문화 기사 3 (미사도서관: [가족뮤지컬] 엄마가 사랑한 책벌레) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795; margin-top: 16px;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎭 2026.10.10(토) 14:00 | 가족 뮤지컬</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&amp;edcLctreNo=5129&amp;pageUnit=10&amp;pageIndex=1&amp;searchCnd=all" target="_blank" style="color: inherit; text-decoration: none;">미사도서관 가족 뮤지컬 &lt;엄마가 사랑한 책벌레&gt;</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"책을 낯설어하던 아이가 가족과 함께 독서의 즐거움을 찾아가는 이야기"</b><br/>
동화 &lt;엄마가 사랑하는 책벌레&gt;를 원작으로 한 극단 희의 가족 뮤지컬 공연입니다. 하남문화재단 '모든예술31' 선정사업으로 무료로 진행됩니다.<br/><br/>
<b>🗓 일시:</b> 2026년 10월 10일(토) 14:00 ~ 15:00<br/>
<b>📍 장소:</b> 하남시 미사도서관 4층 미사홀<br/>
<b>👥 대상:</b> 하남시민 누구나, 가족 단위 선착순 140명 (1인 최대 5명 신청)<br/>
<b>🗓 예약:</b> 9월 28일(월) 10:00부터 미사도서관 홈페이지<br/>
<b>🎟 관람료:</b> 무료 (주차 1시간 무료, 이후 자부담)<br/>
<b>☎️ 문의:</b> 미사도서관 <a href="tel:031-790-5754" style="color:#3182ce; font-weight:bold;">031-790-5754</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&amp;edcLctreNo=5129&amp;pageUnit=10&amp;pageIndex=1&amp;searchCnd=all" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 관람 신청하기 (미사도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092803.jpg" alt="가족 뮤지컬 엄마가 사랑한 책벌레" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 미사도서관
</div>
</div>
</div>"""

# 5. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 28일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1 (2026년 하남시 노후차 조기폐차 지원사업 3차 공고) -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🚗 하남시청 환경정책과 | 환경/지원금</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52702" target="_blank" style="color: inherit; text-decoration: none;">2026년 하남시 노후차 조기폐차 지원사업 3차 공고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95; padding: 14px; border-radius: 8px;">
<b>"배출가스 4·5등급 노후경유차, 오늘부터 조기폐차 보조금 신청하세요!"</b><br/>
하남시에 등록된 배출가스 4·5등급 노후경유차와 특정 건설기계를 대상으로 조기폐차 보조금 3차 신청을 받습니다. 보조금은 차량 시가표준액에 따라 차등 지급되며, 폐차 시(1차)와 대체차량 구입 시(2차)로 나눠 지원합니다.<br/><br/>
<b>🗓 접수기간:</b> 2026년 9월 28일(월) ~ 11월 20일(금) (예산 소진 시 조기 마감)<br/>
<b>👥 선정방법:</b> 1인 2대까지 선착순<br/>
<b>📝 신청방법:</b> 배출가스누리집 온라인 또는 한국자동차환경협회 등기우편<br/>
<b>📞 문의:</b> 한국자동차환경협회 <a href="tel:1577-7121" style="color:#3182ce; font-weight:bold;">1577-7121</a> / 하남시 환경정책과 <a href="tel:031-790-5284" style="color:#3182ce; font-weight:bold;">031-790-5284</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52702" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시청 고시공고) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 (환경정책과)
</div>
</div>

<!-- 공공기관 소식 2 (2026년 하반기 광견병 예방접종 실시) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🐶 하남시청 식품위생농업과 | 반려동물</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52677" target="_blank" style="color: inherit; text-decoration: none;">2026년 하반기 광견병 예방접종 실시</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95; padding: 14px; border-radius: 8px;">
<b>"우리 집 반려견·반려묘, 가까운 동물병원에서 1만 원에 광견병 예방접종!"</b><br/>
광견병 사전 예방을 위해 관내 참여 동물병원 33곳에서 하반기 광견병 예방접종을 실시합니다.<br/><br/>
<b>🗓 접종기간:</b> 2026년 10월 1일(목) ~ 10월 23일(금), 3주간<br/>
<b>👥 대상:</b> 동물등록된 생후 2개월 이상 개·고양이<br/>
<b>💰 비용:</b> 10,000원 (보호자 부담)<br/>
<b>📍 장소:</b> 관내 참여 동물병원 33개소<br/>
<b>📞 문의:</b> 하남시청 식품위생농업과 동물보호팀 <a href="tel:031-790-5853" style="color:#3182ce; font-weight:bold;">031-790-5853</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52677" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 및 참여 동물병원 보기 (하남시청 고시공고) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 (식품위생농업과)
</div>
</div>

<!-- 공공기관 소식 3 (2026년 우수 평생학습 동아리 지원사업 모집 공고) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">📚 하남시 평생교육과 | 평생학습/동아리</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52686" target="_blank" style="color: inherit; text-decoration: none;">2026년 우수 평생학습 동아리 지원사업 모집 공고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95; padding: 14px; border-radius: 8px;">
<b>"함께 배우고 나누는 우리 동아리, 지역사회와 성과를 공유해 보세요!"</b><br/>
자발적으로 학습해 온 평생학습동아리의 성과를 지역사회와 나누고 활동을 이어갈 수 있도록 우수 동아리를 선정해 지원합니다. 세부 지원 내용은 첨부 공고문을 확인해 주세요.<br/><br/>
<b>🗓 접수기간:</b> 2026년 9월 23일(수) 12:00 ~ 10월 6일(화) 18:00<br/>
<b>📝 신청방법:</b> 방문(평생학습관 2층, 하남대로 732 / 평일 09:00~18:00) 또는 이메일 ysy426@korea.kr<br/>
<b>📞 문의:</b> 하남시 평생교육과 <a href="tel:031-790-6043" style="color:#3182ce; font-weight:bold;">031-790-6043</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52686" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시청 고시공고) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 평생교육원 (평생교육과)
</div>
</div>

"""

# Combine all 5 sections cleanly
all_sections_content = (
    section1_content + '\n<hr/>\n' +
    section2_content + '\n<hr/>\n' +
    section3_content + '\n\n' +
    section4_content + '\n\n' +
    section5_content + '\n\n'
)

idx_lawmaker = content.find('<div id="lawmaker">')
idx_bottom = content.find('<div class="bottom-nav"')

content = content[:idx_lawmaker] + all_sections_content + content[idx_bottom:]

# Update visitor counter path ID to 0928
content = content.replace("lee-kwang-jae.news_letter.0923", "lee-kwang-jae.news_letter.0928")

# Save target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {target_path}")

# Save to news_index_path & root_index_path
with open(news_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {news_index_path}")

with open(root_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {root_index_path}")
