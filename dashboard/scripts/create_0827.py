import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260826.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260827.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 8월 26일", "KJ's 하남 인사이드 - 2026년 8월 27일")
content = content.replace('26호 | 2026년 8월 26일 발행', '27호 | 2026년 8월 27일 발행')
content = content.replace('📅 발행일: 2026년 8월 26일', '📅 발행일: 2026년 8월 27일')
content = content.replace('하남 맘카페 HOT 이슈 TOP 3', '하남 맘카페 HOT 이슈')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 국제뉴스) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.gukjenews.com/news/articleView.html?idxno=3675712" target="_blank" style="color: inherit; text-decoration: none;">이광재, "친일재산 192만 평 미매각…국가가 매입해 독립유공자 후손 지원해야"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 더불어민주당 국회의원(경기 하남시갑)이 국가보훈부 자료를 분석한 결과, 국가 귀속 친일귀속재산 1,600필지(약 265만 평) 중 매각 완료는 27.4%(73만 평)에 불과하고 여의도 면적의 2.2배에 달하는 819필지(약 192만 평)가 여전히 미매각 상태로 방치되어 있다고 지적했습니다. 이 의원은 미매각 친일재산을 국가가 직접 매입하여 독립유공자 후손 지원을 위한 든든한 재원으로 적극 활용해야 한다고 촉구했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.gukjenews.com/news/articleView.html?idxno=3675712" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (국제뉴스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0827_kj_01.jpg" alt="이광재 의원 친일재산 국가 매입 및 독립유공자 후손 지원 제안" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 2 (언론보도 - 포춘코리아) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.fortunekorea.co.kr/news/articleView.html?idxno=53752" target="_blank" style="color: inherit; text-decoration: none;">[포춘코리아 인터뷰] 이광재 예결위원장, "말로만 국민 사랑한다고요? 더 나은 삶 선물해야죠"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원장 중책을 맡은 이광재 국회의원(경기 하남시갑)이 포춘코리아와의 단독 인터뷰에서 국가 세금 800조 원 외에 연기금, 국·공유재산, 정책금융 및 민간자본을 종합적으로 활용하는 '네 개의 돈주머니' 국가 자산 재설계 구상과 신생아 1억 원 지원 '누구나 인생계좌', 코스닥 체질 개선 등 국민 삶을 바꾸는 정밀한 재정·정책 비전을 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.fortunekorea.co.kr/news/articleView.html?idxno=53752" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (포춘코리아) →</a></div>
</div>
<div class="source">
📌 출처: 포춘코리아
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles + '\n',
    content
)

# Section 2: 하남 지역 주요 뉴스
local_news_articles = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 의정/환경</div>
<h3>최승태 의원, "덕풍천 산책로 잡목 방치 및 뱀 출몰 위험…LH·하남시 대책 마련 시급" 촉구</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회 최승태 의회운영위원장이 3기 신도시 교산지구 편입 후 풀과 잡목이 무성하게 방치되고 뱀까지 출몰하여 주민 안전이 위협받고 있는 덕풍천 산책로 현장을 방문 점검하고, 한국토지주택공사(LH)와 하남시에 조속한 긴급 예초 작업 및 안전 관리 대책 수립을 강력 촉구했습니다.
</div>
<div class="source">
📌 출처: 팩트저널
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 도시/공원</div>
<h3>하남시, 위례근린공원4호 9월 1일 전격 선개방…황토길·솔향기길·숲속놀이터 조성</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 학암동 산 30 일원에 위치한 위례근린공원4호(186,410㎡)의 공원 시설이 조기 설치되고 주민 이용 수요가 높아짐에 따라 당초 10월 말 준공 예정보다 2개월 앞당겨 9월 1일부터 전격 선개방하기로 결정했습니다. 공원 내 사계절 비가림막 황토길(174m), 소나무 솔향기길(80m), 숲속놀이터, 인공폭포, 배드민턴장 등 다양한 휴식·체육 시설이 들어서며 안전을 위한 주변 CCTV도 확충됩니다.
</div>
<div class="source">
📌 출처: 시티뉴스
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 하남시 관내 어린이 물놀이장 &amp; 수변공원 8월 말 막바지 운영 소식 (미사맘/감일맘/위례맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 말 늦더위 속 관내 미사·감일 어린이 물놀이장과 수변공원 분수시설 막바지 운영 일정 및 수질·안전 점검 소식이 카페에 공유되어 큰 관심을 받았습니다.</div>
<div class="mom-point">💡 주민 포인트: 방학 마무리를 앞두고 집 가까운 곳에서 안전하게 물놀이를 즐길 수 있는 운용 시간표와 주차 꿀팁 정보가 주민들 사이에서 활발히 소통되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "개학 전에 아이들 데리고 한 번 더 다녀와야겠어요!", "올여름 집 가까이서 시원하게 잘 보냈습니다" 등의 반응이 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 교산지구 세대통합형 학교복합시설 '어울림(林)캠퍼스' 국비 240억 확보 소식 (미사맘/감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 교산신도시 내 들어설 학교복합시설이 교육부 공모에 최종 선정되어 국비 240억 원을 확보, 수영장·체육관·돌봄교실 등을 갖춘 어울림캠퍼스가 건립된다는 소식이 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 초등 돌봄교실과 생존수영장, 문화 복합시설이 대거 확충되어 아이들의 안전한 체육 활동과 촘촘한 돌봄 환경이 조성될 것이란 기대를 모았습니다.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 수영장과 돌봄 교실이 대규모로 들어서서 정말 든든하네요", "하남이 명품 교육 도시로 발전하는 게 체감됩니다" 등의 반가운 반응이 달렸습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 5: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[축제/행사] 스타필드 하남 '2026 더 좋은소비 페스타 in 하남' (8월 28일~30일)</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시:</b> 2026년 8월 28일(금) ~ 8월 30일(일) (3일간)<br/>
<b>장소:</b> 스타필드 하남 센트럴 아트리움<br/>
<b>내용:</b> 경기·하남 지역 우수 사회적경제기업 30여 곳의 친환경 공예, 유기농 식품 유통 및 가족 만들기 체험 부스 운영 (방문객 선착순 사은품 증정)
</p>
</div>

<div class="event-card">
<strong>[보건/생활] 하남시 보건소 9월 '성인·노인 만성질환 예방 운동교실' 수강생 모집</strong>
<p>기간: 2026년 8월 27일(목)부터 선착순 모바일/방문 접수 (하남시보건소)<br/>내용: 늦더위 폭염 장기화 대응 어르신 및 고혈압·당뇨 만성질환자 맞춤형 근력 및 유산소 운동 프로그램이 9월부터 가동됩니다.</p>
</div>

<div class="event-card">
<strong>[교육/도서관] 하남시립도서관 2026년 가을학기 어린이·청소년 독서강좌 수강생 모집</strong>
<p>기간: 2026년 8월 27일(목)부터 선착순 접수 (하남시립도서관 홈페이지)<br/>내용: 미사·나룰도서관 동화 창작, AI 디지털 웹툰, 주말 독서 토론 교실 등 9월 맞춤형 강좌 운영.</p>
</div>

<div class="event-card">
<strong>[청년/지원] 2026년 청년드림, 제주애(愛) 올레(Olle)? 참가자 모집 중 (8월 31일까지)</strong>
<p>기간: 2026년 8월 25일(화) ~ 8월 31일(월)<br/>내용: 하남 만 19~34세 청년 대상 제주시 한달살이 숙박비 지원 사업 (이메일 cnr2013@korea.kr 접수)</p>
</div>

<div class="event-card">
<strong>[전시/생활] 하남 미사 마주침갤러리 가을맞이 '그리다 민화전' 개최</strong>
<p>기간: 2026년 8월 24일(월) ~ 9월 4일(금) (하남시 생활문화센터 미사)<br/>내용: 전통 민화와 현대적 감각이 어우러진 40여 점의 하남 지역 작가 작품 무료 관람.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 8월 27일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 6: 공공기관 소식지
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.08.27</div>
<h3>[하남시보건소] 2026년 가을맞이 성인·어르신 맞춤형 만성질환 예방 운동교실 모집 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>모집기간:</b> 2026.8.27.(목) ~ 선착순 마감 | <b>대상:</b> 관내 성인 및 노인<br/>
<b>주요내용:</b> 폭염 지속에 따른 기력 회복 및 고혈압·당뇨 맞춤 운동지도, 체성분 측정 지원<br/>
<b>접수방법:</b> 하남시보건소 모바일 앱 또는 현장 방문 (문의: 보건사업과)
</div>
<div class="source">
📌 출처: 하남시 보건소 공지사항
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시립도서관 | 2026.08.27</div>
<h3>[하남시립도서관] 2026년 가을학기 어린이·청소년 독서문화 강좌 수강생 모집 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 미사·나룰·덕풍도서관에서 9월 개강하는 초·중학생 맞춤형 동화 창작, AI 웹툰, 독서토론 교실 수강생을 8월 27일부터 도서관 홈페이지에서 선착순 모집합니다.
</div>
<div class="source">
📌 출처: 하남시립도서관 공지사항
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Clean up any leftover duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write to kj_hanam_inside_20260827.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created 2026-08-27 newsletter issue #27!")
