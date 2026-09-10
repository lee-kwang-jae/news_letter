import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260901.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260902.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 9월 1일", "KJ's 하남 인사이드 - 2026년 9월 2일")
content = content.replace('30호 | 2026년 9월 1일 발행', '31호 | 2026년 9월 2일 발행')
content = content.replace('📅 발행일: 2026년 9월 1일', '📅 발행일: 2026년 9월 2일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 이데일리: 이광재 인터뷰 - 2026.09.02) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.edaily.co.kr/News/Read?newsId=01922086645575856&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article" target="_blank" style="color: inherit; text-decoration: none;">[인터뷰] 이광재 "민주 전대가 DJ·盧적자논쟁 할 때였나...청년세대 주인공으로 만들어야"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 더불어민주당 예산결산특별위원회 위원장이 언론 인터뷰를 통해 8·17 전당대회 이후 당 지도부의 최우선 과제로 "AI 기술 전쟁 시대에 확실한 성과를 내어 미래로 가는 확실한 길을 열어야 한다"고 강조했습니다. 이 의원은 과거의 적자 논쟁에서 벗어나 청년 세대를 단순한 정책 수혜 대상이 아닌 세상의 주역으로 바로 세우고, 기술과 성장 중심의 국가 비전을 정립해야 함을 강력히 제언했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.edaily.co.kr/News/Read?newsId=01922086645575856&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (이데일리) →</a></div>
</div>
<div class="source">
📌 출처: 이데일리 (노희준 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 디스커버리뉴스: 감사원법 개정안) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100153" target="_blank" style="color: inherit; text-decoration: none;">[단독] 이광재 의원, 정책 타당성 감사 제외 법제화 추진…감사원법 개정안 대표발의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 이광재 국회의원이 정부의 중요 정책결정에 대한 타당성 판단은 감사원의 직무감찰 대상에서 제외하되, 정책 추진 과정에서 발생한 불법·부패행위는 계속 감찰하도록 하는 내용의 '감사원법 일부개정법률안'을 8월 31일 대표발의했습니다. 정권 교체 시 반복되는 표적·보복성 감사를 방지하고 공무원들이 소신 행정과 정책을 적극 추진할 수 있도록 보호하는 것이 핵심 취지입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100153" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 하남 주요 현안 챙기기 & 비전 제시) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224396108941" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "새로운 도시가 새로운 문명을 만듭니다…하남 현안 해결에 사활"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 하남드림 광역환승센터 기본계획 반영 및 위례근린공원4호 조기 개방 등 현장 의정 성과를 점검하고, AI 시대에 걸맞은 하남의 발전 방향을 제시했습니다. 산업·대학·보육·의료·문화가 어우러진 '메가성장' 모델로 하남 주민들의 삶의 질을 높이고 주요 숙원 사업 예산을 국회 차원에서 집중 지원하겠다고 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224396108941" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0901_kj_01.jpg" alt="새로운 도시와 문명 비전 제시" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles + '\n',
    content
)

# Section 2: 하남 지역 주요 뉴스 (사용자 지정 4개 기사 반영)
local_news_articles = """<!-- 지역 뉴스 기사 1 (의정/상권 - 연합뉴스: 정혜영 의원 교류) -->
<div class="article-card">
<div class="badge">📰 의정/상권</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260901150300055?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">정혜영 하남시의원, 전주시의회와 전통시장·상점가 활성화 우수사례 및 정책 교류</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회 '전통시장·상점가 육성 및 활성방안 연구회' 정혜영 대표의원을 비롯한 하남시의원 방문단이 9월 1일 전주시의회를 방문해 남부시장 야시장, 청년몰, 관광 연계 상권 등 우수 선도 모델을 공유받았습니다. 정혜영 의원은 "전주의 생생한 현장 경험을 면밀히 검토해 하남시 전통시장과 골목상권 활성화를 위한 실효성 있는 맞춤형 정책 대안을 마련하겠다"고 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/AKR20260901150300055?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (김동철 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (유통/상권 - 이코노미스트: 스타필드 하남 10주년) -->
<div class="article-card">
<div class="badge">📰 유통/상권</div>
<h3><a href="https://economist.co.kr/article/view/ecn202608310064" target="_blank" style="color: inherit; text-decoration: none;">10년 버틴 스타필드 하남...3040 세대 매료시키며 누적 2억 5천만 명 방문</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
스타필드 하남점이 오는 9월 9일 오픈 10주년을 맞습니다. 지난 10년 간 누적 방문객 2억 5,000만 명을 기록하며 국내 최초 체류형 복합 쇼핑 테마파크로 안착했습니다. 연간 380건의 다채로운 팝업스토어와 국내 최초 반려동물 동반 입장(펫 프렌들리) 허용 등으로 주말 방문객 중 3040세대 비중이 70%에 달하며 지역 경제의 거점 역할을 하고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://economist.co.kr/article/view/ecn202608310064" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (이코노미스트) →</a></div>
</div>
<div class="source">
📌 출처: 이코노미스트 (이지완 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (문화/지역 - 국민일보: 스테이지 하남) -->
<div class="article-card">
<div class="badge">📰 문화/지역</div>
<h3><a href="https://www.kmib.co.kr/article/view.asp?arcid=9000008081&cp=nv" target="_blank" style="color: inherit; text-decoration: none;">하남 미사호수공원서 9월 5일 '2026 하반기 스테이지 하남' 개막 공연 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
경기 하남시와 하남문화재단이 오는 9월 5일 미사호수공원 잔디광장에서 '2026 하반기 스테이지 하남 오픈공연'을 개최합니다. 2시간 동안 K-POP, 대중가요, 인디밴드, 스트리트댄스 무대가 펼쳐지며, 10월 31일까지 미사·위례·감일·원도심 주요 거점에서 매주 금·토요일 다채로운 버스킹 축제가 이어집니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kmib.co.kr/article/view.asp?arcid=9000008081&cp=nv" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (국민일보) →</a></div>
</div>
<div class="source">
📌 출처: 국민일보 (박재구 기자)
</div>
</div>

<!-- 지역 뉴스 기사 4 (행정/토지 - 뉴스핌: 개별공시지가) -->
<div class="article-card">
<div class="badge">📰 행정/토지</div>
<h3><a href="https://www.newspim.com/news/view/20260901000430" target="_blank" style="color: inherit; text-decoration: none;">하남시, 토지변동 278필지 개별공시지가 열람 및 의견 접수 실시</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
경기 하남시가 2026년 7월 1일 기준 지목변경, 분할·합병 등 토지변동이 발생한 278필지에 대한 개별공시지가를 9월 1일부터 22일까지 열람하고 토지소유자 의견을 접수합니다. 하남시청 토지정보과, 동 행정복지센터 및 부동산공시가격알리미 홈페이지에서 확인 가능합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newspim.com/news/view/20260901000430" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴스핌) →</a></div>
</div>
<div class="source">
📌 출처: 뉴스핌 (정종일 기자)
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 (2번 항목 도서관 독서의 달 소식으로 교체)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 스타필드 하남 10주년 오픈 소식 및 9월 가을 팝업스토어·할인 행사 소식에 맘카페 북적 (조회수 1.9만 / 댓글 260+)</h4>
<div class="mom-detail"><strong>현황:</strong> 스타필드 하남점이 9월 9일 오픈 10주년을 앞두고 애스턴마틴 팝업을 비롯한 9월 가을철 대형 패션·키즈 팝업 및 가족 체험 이벤트가 개최된다는 소식이 미사·위례·감일 맘카페 최고 인기글에 올랐습니다.</div>
<div class="mom-point">💡 주민 포인트: 9월 주말 아이와 방문하기 좋은 팝업스토어 혜택, 무료 주차 팁, 펫 유모차 대여 정보 및 10주년 기념 식음료 할인 쿠폰 공유.</div>
<div class="mom-reaction">💬 주민 반응: "벌써 스타필드 하남이 10주년이라니 세월 빠르네요!", "이번 주말 아이들과 팝업 체험하러 다녀와야겠어요" 등 댓글 260여 개가 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 9월 독서의 달 맞이 하남시립도서관 '도서 대출 2배(10권) 확대' & 작가 북토크 신청 열기 (조회수 1.5만 / 댓글 210+)</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 독서의 달을 맞아 하남시립도서관(미사·나룰·세미 등)에서 한 달간 도서 대출 수량을 기존 5권에서 10권으로 2배 확대하고, 어린이·청소년 독서 문화 프로그램 및 베스트셀러 작가 초청 북토크 신청이 시작되어 학부모들의 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 1인당 10권 대출 혜택 활용 팁, 미사도서관 및 나룰도서관 주말 어린이 문화 강좌 수강 신청 오픈 시간 공유.</div>
<div class="mom-reaction">💬 주민 반응: "가을 독서 계절에 아이들과 10권까지 넉넉하게 빌릴 수 있어 너무 좋네요!", "인기 작가 북토크 강연 신청 잊지 말고 해야겠어요" 등 추천 댓글 210여 개가 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 9월 추석 명절 앞두고 덕풍·신장 전통시장 '온누리상품권 현장 환급' 장보기 팁 공유 (조회수 1.2만 / 댓글 165+)</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 1일부터 덕풍시장과 신장전통시장에서 국산 농축수산물 구매 시 최대 2만 원 온누리상품권을 현장에서 즉시 환급받는 추석 이벤트가 시작되면서 알뜰 장보기 실시간 후기가 게재되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 온누리상품권 현장 환급 부스 위치, 하머니 지역화폐 10% 인센티브 충전 혜택과의 이중 할인 장보기 꿀팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "명절 앞두고 전통시장에서 장보고 2만 원 환급받으니 알뜰하게 장볼 수 있네요!", "주말에 장보러 시장 다녀와야겠어요" 댓글 잇따름.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 4: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[공연/축제] 2026 하반기 스테이지 하남 (Stage Hanam) 오픈공연 (9월 5일 개최)</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시/장소:</b> 2026년 9월 5일(토) 17:00~ / 미사호수공원 잔디광장<br/>
<b>내용:</b> 하반기 첫 오픈 무대! 치어리딩, 스트리트댄스, 인디밴드 및 K-POP 버스킹 공연 (무료 관람).
</p>
</div>

<div class="event-card">
<strong>[청년/행사] 2026 하남 청년명랑운동회 참가자 모집 (9월 19일 개최)</strong>
<p>일시/장소: 2026년 9월 19일(토) / 하남 종합운동장 실내체육관<br/>내용: 하남 청년(만 19~39세) 대상 단합 명랑운동회, E-스포츠 경기, 청년 정책 퀴즈대회 (선착순 접수).</p>
</div>

<div class="event-card">
<strong>[문화/전시] 하남역사박물관 9월 기획전 '이성산성에서 만난 백제의 숨결'</strong>
<p>기간: 2026년 9월 1일(화) ~ 10월 31일(토) / 하남역사박물관 1층 기획전시실<br/>내용: 하남 이성산성 발굴 유물 특별 전시 및 VR 가상현실 백제 성곽 체험존 운영 (무료 관람).</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 2일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 5: 공공기관 소식지
public_agency_news = """<!-- 기사 1 (하남시청 - 주민자치 수강생 모집) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.02</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 2026년 4분기 위례동 주민자치센터 수강생 모집 안내 (9.10~9.14)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접수기간:</b> 2026.9.10.(목) ~ 9.14.(월) | <b>추첨일:</b> 2026.9.15.(화)<br/>
<b>주요내용:</b> 하남시 위례동 주민자치센터 4분기 교양·문화·체육 강좌 수강생 모집 (인터넷 및 방문 접수).<br/>
<b>문의:</b> 위례동 주민자치센터
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 위례동 주민자치센터
</div>
</div>

<!-- 기사 2 (하남시청 - 전통시장 환급 행사) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.01</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 9월 추석 명절 맞이 전통시장 온누리상품권 현장 환급 행사 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>행사기간:</b> 2026.9.1.(화) ~ 9.15.(화) | <b>장소:</b> 덕풍·신장 전통시장<br/>
<b>주요내용:</b> 국산 농축수산물 구매 시 구매 금액대별 최대 2만 원 온누리상품권 현장 환급 제공.<br/>
<b>문의:</b> 하남시청 기업지원과 전통시장팀
</div>
<div class="source">
📌 출처: 하남시청 기업지원과
</div>
</div>

<!-- 기사 3 (하남시보건소) -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.09.01</div>
<h3>[하남시보건소] 2026년 가을철 쯔쯔가무시·인플루엔자 예방 수칙 및 무료 접종 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접종기간:</b> 2026.9.1.(화)부터 순차 실시 | <b>대상:</b> 65세 이상 어르신, 만성질환자, 어린이<br/>
<b>주요내용:</b> 관내 지정 의료기관 및 보건소에서 무료 인플루엔자 예방접종 실시 및 야외 활동 시 진드기 물림 주의 당부
</div>
<div class="source">
📌 출처: 하남시 보건소 감염병관리과
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Update Bottom Nav link to include 0901.html and set active 0902
bottom_nav_old = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260901.html" class="active">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'
bottom_nav_new = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260902.html" class="active">31호 (09/02)</a> | \n<a href="kj_hanam_inside_20260901.html">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'

content = content.replace(bottom_nav_old, bottom_nav_new)

# Clean up duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260902.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target_path} and updated {index_path} with item 2 replaced!")
