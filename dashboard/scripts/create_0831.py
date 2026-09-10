import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260828.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260831.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 8월 28일", "KJ's 하남 인사이드 - 2026년 8월 31일")
content = content.replace('28호 | 2026년 8월 28일 발행', '29호 | 2026년 8월 31일 발행')
content = content.replace('📅 발행일: 2026년 8월 28일', '📅 발행일: 2026년 8월 31일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 아시아경제: AI 국회 예산) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://view.asiae.co.kr/article/2026082716142985247" target="_blank" style="color: inherit; text-decoration: none;">[AI룰메이커] 이광재 "국회 예산 심사에 AI 도입 확대…500억원 규모 투입"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 800조 원 규모의 국가 예산안 심사에 인공지능(AI)을 본격 도입하고 관련 투자를 500억 원 규모로 확대하겠다고 밝혔습니다. 국회사무총장 재임 시절 'AI 국회' 구축 경험을 바탕으로 AI를 활용해 사업 타당성과 집행 성과를 정밀 분석하고, 소모적인 중복 질의 관행을 개선하며 '무늬만 AI' 사업을 가려내는 한편 GPU 등 국가적 AI 인프라 통합 관리 방안을 제안했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://view.asiae.co.kr/article/2026082716142985247" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (아시아경제) →</a></div>
</div>
<div class="source">
📌 출처: 아시아경제 (우수연·전영주 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 서울신문: 당 혁신 메가텐 가동) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.seoul.co.kr/news/politics/2026/08/25/20260825500236?wlog_tag3=naver" target="_blank" style="color: inherit; text-decoration: none;">김민석, 당 혁신 '메가텐' 가동…이광재·김경수·이언주 메가특위 이끈다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당이 공천·정당개혁부터 지방성장, 개헌, 청년정책 등 당 혁신을 전담할 10개 특별기구 '메가텐'을 출범시킨 가운데, 김민석 대표가 직접 위원장을 맡는 핵심 기구인 '메가프로젝트 및 지방성장지원특별위원회(메가성장특위)'의 수석부위원장에 이광재 의원이 임명되었습니다. 이 의원은 지방 성장 동력 확보 및 국가적 대형 메가프로젝트 추진을 주도할 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.seoul.co.kr/news/politics/2026/08/25/20260825500236?wlog_tag3=naver" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (서울신문) →</a></div>
</div>
<div class="source">
📌 출처: 서울신문 (한지은 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 청소년 주민참여예산 / 이미지: 0831_kj_01) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224394433325" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "하남 청소년의 생각이 예산이 되고, 더 따뜻한 하남을 만듭니다"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 2027년도 하남시 청소년 주민참여예산제 심의·의결에 참석하여 청소년들과 예산의 철학과 공공의 가치에 대해 깊이 소통했습니다. 학교 예산 활용, 재능 계발 및 체육시설 확충 등 청소년들의 아이디어가 실제 예산과 정책으로 결실을 맺을 수 있도록 지원하고, 청소년 대상 국회 견학 및 현장 직접 안내를 약속했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224394433325" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0831_kj_01.jpg" alt="하남 청소년 주민참여예산제 심의 및 이광재 의원 소통" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 위례신사선 / 이미지: 0831_kj_02) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224395098607" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "위례신사선, 이제는 속도의 문제입니다"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 위례 아파트 단지 회장단과 간담회를 열고 위례신사선 개통 속도전 및 현안 해결 방안을 논의했습니다. 서울시의 기본계획 예산(17.8억 원) 편성에 이어 국비 조기 확보와 하남(감일) 연장의 제5차 국가철도망 반영 추진, 출퇴근 불편 해소를 위한 수요응답형 버스 도입 및 복정역 환승 동선 개선 추진 의지를 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224395098607" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0831_kj_02.jpg" alt="위례 아파트 단지 회장단 간담회 및 위례신사선 논의" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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

# Section 2: 하남 지역 주요 뉴스 (2026.08.31 기준)
local_news_articles = """<!-- 지역 뉴스 기사 1 (공원/문화) -->
<div class="article-card">
<div class="badge">📰 공원/문화</div>
<h3><a href="https://m.ctnews.co.kr/40744" target="_blank" style="color: inherit; text-decoration: none;">하남, 위례근린공원4호 9월 1일 개방</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 위례근린공원4호(학암동 산 30 일원)를 10월 말 준공 예정보다 2개월 앞당겨 9월 1일부터 선개방합니다. 186,410㎡ 면적에 사계절 이용 가능한 황토길(174m, 비가림막 설치)과 소나무 200여 그루가 병풍을 이룬 솔향기길(80m), 숲속놀이터(약 200㎡), 인공폭포(1기), 배드민턴장(2면) 및 체육시설이 조성되었으며, 안전한 보행 환경 조성을 위해 CCTV도 설치됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://m.ctnews.co.kr/40744" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시티뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 시티뉴스 (고승선 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (유통/상권) -->
<div class="article-card">
<div class="badge">📰 유통/상권</div>
<h3><a href="https://www.popcornnews.net/news/articleView.html?idxno=131197" target="_blank" style="color: inherit; text-decoration: none;">스타필드 하남 10주년...주말 바꾼 ‘라이프스타일 플랫폼’으로 자리매김</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
2016년 국내 최초 쇼핑 테마파크로 문을 연 스타필드 하남이 개점 10주년을 맞아 누적 방문객 2억 5천만 명을 달성했습니다. 9월 13일까지 10주년 기념 '하이텐션 페스티벌'과 케이펫페어, 펫 팝업, 애스턴마틴 팝업 등 온가족이 즐길 수 있는 다채로운 나들이 축제와 신규 프리미엄 브랜드 입점을 선보입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.popcornnews.net/news/articleView.html?idxno=131197" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (팝콘뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 팝콘뉴스 (김지수 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (부동산/주택) -->
<div class="article-card">
<div class="badge">📰 부동산/주택</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1099843" target="_blank" style="color: inherit; text-decoration: none;">하남 스타포레 법 개정 효과 부각…정작 소유권 확보 15퍼센트대</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 덕풍동 일대 지역주택조합 '하남 스타포레 1·2차' 사업과 관련해 주택법 개정에 따른 사업 추진 기대감이 부각되고 있으나, 조합이 등기상 확보한 실질 토지 소유권 비율이 15%대에 머물고 있어 사업계획승인 등 향후 행정절차 이행 과정에서의 신중한 접근과 주의가 요구됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1099843" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 지역 뉴스 기사 4 (교육/교류) -->
<div class="article-card">
<div class="badge">📰 교육/교류</div>
<h3><a href="https://www.kyongbuk.co.kr/news/articleView.html?idxno=4082554" target="_blank" style="color: inherit; text-decoration: none;">구미 학부모회 활동 ‘눈길’…하남시가 벤치마킹 나섰다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
경기도 하남시학부모연합회가 구미시학부모회장협의회의 정책포럼, 학부모 연수, 지역사회 연계 교육 참여 등 선진 학부모회 운영 우수 사례를 벤치마킹하기 위해 구미를 방문하여 업무협약(MOU)을 체결하고 지속적인 교육 정보 공유 및 협력을 추진하기로 했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kyongbuk.co.kr/news/articleView.html?idxno=4082554" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경북일보) →</a></div>
</div>
<div class="source">
📌 출처: 경북일보 (이봉한 기자)
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 (2026.08.31 기준)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 미사호수공원 음악분수 신기술 재단장 가동 & 주말 야경 산책 현장 후기 폭발 (조회수 1.5만 / 댓글 190+)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시가 미사호수공원 음악분수를 최첨단 신기술 연출 노즐로 재단장해 주말 동안 시범 가동을 시작한 가운데, 저녁 호수공원 조명과 분수 연출을 관람한 주민들의 영상 및 사진 후기가 미사·하남 맘카페 조회수 1위를 달성했습니다.</div>
<div class="mom-point">💡 주민 포인트: 미사호수공원 음악분수 주말 가동 시간표(저녁 8시/9시), 명당 관람 벤치 위치, 주변 수변공원 산책로 및 주차 팁이 집중 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "분수 조명이 훨씬 입체적이고 화려해졌네요!", "열대야 늦더위에 주말 밤 아이들과 호수 산책하기 최고입니다" 등 190여 개의 추천 댓글이 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 감일지구 초·중학교 등하교 통학로 안전점검 & 옐로카펫 정비 후기 (조회수 1.1만 / 댓글 145+)</h4>
<div class="mom-detail"><strong>현황:</strong> 2학기 개학을 맞은 감일지구 맘카페에서 단지 내 초·중학생들의 안전 등하교를 위한 신호등 보행시간 연장 건의와 통학로 옐로카펫 정비 완료 현장 사진이 게시되어 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 감일 신도시 등하굣길 녹색어머니회 교통 봉사 일정 조율 및 아이들 보행 안전 주의 구간 정보가 집중 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 등하굣길 안전 장치가 늘어나서 다행입니다", "개학날 등교 시간 봉사해주시는 학부모님들 감사해요" 등 따뜻한 댓글 140여 개가 올랐습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남시립도서관 9월 가을학기 어린이 독서·AI 강좌 접수 열기 (조회수 9.5천 / 댓글 130+)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 31일(월)부터 시작된 하남시립 미사·나룰·덕풍도서관의 9월 가을학기 어린이 동화창작, AI 웹툰, 청소년 독서토론 교실 접수 마감 현황 및 신청 팁이 맘카페 인기글에 올랐습니다.</div>
<div class="mom-point">💡 주민 포인트: 도서관 수강 신청 로그인 팁과 미사·나룰도서관 주말 인기 유아·어린이 독서 프로그램 신청 성공 후기가 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "미사도서관 AI 강좌 인기 높아서 빠르게 마감되었네요!", "다음 신청 땐 팁 참고해서 꼭 성공해야겠어요" 등의 댓글이 작성되었습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 4: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[공연/문화] 2026 하남이성산성문화제 사전 예매 오픈 & 가을 야간 미디어파사드 공연</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시/장소:</b> 2026년 9월 1일(화)부터 선착순 예매 (하남문화재단 홈페이지) / 이성산성 및 미사호수공원<br/>
<b>내용:</b> 백제 역사 문화유산 이성산성을 배경으로 펼쳐지는 가을 빛의 축제. 야간 미디어파사드, 퓨전 국악 콘서트, 어린이 역사 체험 부스 운영.
</p>
</div>

<div class="event-card">
<strong>[생활/체육] 2026년 하남시민 생활체육 대축전 참가 동호회 모집</strong>
<p>기간: ~ 2026년 9월 4일(금)까지 (하남시체육회 이메일 접수)<br/>내용: 하남 종합운동장 및 당정근린공원 파크골프장에서 열리는 축구, 테니스, 배드민턴, 파크골프 등 체육 동호회 대항전 참가 모집.</p>
</div>

<div class="event-card">
<strong>[청년/창업] 하남시 청년창업피움 공간 '9월 AI 커머스 창업 원데이 특강' 신청</strong>
<p>기간: 2026년 9월 1일(화)부터 선착순 접수 (하남시 청년지원센터 홈페이지)<br/>대상: 하남시 거주 만 19~39세 청년 | 내용: AI 마케팅 활용법, 온라인 쇼핑몰 브랜딩 및 1:1 창업 컨설팅 무료 지원.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 8월 31일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 5: 공공기관 소식지
public_agency_news = """<!-- 기사 1 (하남시청 보도자료 - 고유가 피해지원금) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.08.27</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectBbsNttView.do?key=10048&bbsNo=1164&nttNo=502252" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 고유가 피해지원금 8월 31일까지 사용 당부 (잔액 자동 소멸 및 스미싱 주의)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>사용기한:</b> ~ 2026.8.31.(월) 24:00까지 | <b>대상:</b> 하남시민 (지급 완료자 19만 5,958명 중 잔액 보유자)<br/>
<b>주요내용:</b> 기한 경과 시 미사용 잔액 자동 소멸. 연 매출 30억 이하 관내 소상공인 가맹점에서 사용 가능.<br/>
<b>주의사항:</b> 시청 사칭 지원금 환수 빙자 URL 스미싱 문자 사기 주의 (하남시는 URL 포함 문자 미발송)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectBbsNttView.do?key=10048&bbsNo=1164&nttNo=502252" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">보도자료 원문 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 공시/보도자료
</div>
</div>

<!-- 기사 2 (하남시보건소) -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.08.31</div>
<h3>[하남시보건소] 2026년 가을맞이 성인·어르신 만성질환 예방 운동교실 수강생 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>모집기간:</b> 2026.8.31.(월) ~ 선착순 마감 | <b>대상:</b> 관내 성인 및 노인<br/>
<b>주요내용:</b> 기력 회복 및 고혈압·당뇨 맞춤 운동지도, 체성분 분석 및 맞춤형 건강 관리 서비스 제공<br/>
<b>접수방법:</b> 하남시보건소 모바일 앱 및 방문 접수 (문의: 보건사업과)
</div>
<div class="source">
📌 출처: 하남시 보건소 공지사항
</div>
</div>

<!-- 기사 3 (하남시립도서관) -->
<div class="article-card">
<div class="badge">🏛️ 하남시립도서관 | 2026.08.31</div>
<h3>[하남시립도서관] 2026년 9월 가을학기 독서문화프로그램 접수 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시립 미사·나룰·덕풍도서관에서 9월 개강하는 어린이·청소년·성인 독서 교실 및 AI 디지털 강좌 수강생을 도서관 홈페이지에서 모집합니다.
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

# Clean up duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260831.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated {target_path} and {index_path} with new field blog entries and images!")
