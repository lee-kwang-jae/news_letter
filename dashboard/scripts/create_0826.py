import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260825.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260826.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 8월 25일", "KJ's 하남 인사이드 - 2026년 8월 26일")
content = content.replace('25호 | 2026년 8월 25일 발행', '26호 | 2026년 8월 26일 발행')
content = content.replace('📅 발행일: 2026년 8월 25일', '📅 발행일: 2026년 8월 26일')

# Remove weather widget HTML and weather script
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 뉴스프리존) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.newsfreezone.co.kr/news/articleView.html?idxno=705677" target="_blank" style="color: inherit; text-decoration: none;">이광재 의원 끈질긴 설득 결실! 뉴홈 사전청약자 전용 모기지(40년 만기·1.9~3.0% 금리) 확정 이끌어내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
국토교통부가 위례·감일지구 등 뉴홈 사전청약자들의 주거 부담을 크게 낮추는 최장 40년 만기, 고정금리 1.9~3.0% 전용 모기지 적용 방안을 최종 확정했습니다. 이광재 더불어민주당 국회의원(경기 하남시갑)이 사전청약 입주예정자들의 목소리를 국토부에 지속적으로 전달하고 끈질기게 제도 개선을 촉구·설득하여 거둔 뜻깊은 성과입니다. 고금리 시대에 이자 부담을 획기적으로 줄이고 실질적 주거 안정을 든든하게 뒷받침하게 되었습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsfreezone.co.kr/news/articleView.html?idxno=705677" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴스프리존) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0826_kj_01.jpg" alt="이광재 의원 뉴홈 사전청약자 전용 모기지 확정 결실" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 2 (언론보도 - 강원일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kwnews.co.kr/article/20260825501880" target="_blank" style="color: inherit; text-decoration: none;">이광재 의원, K-콘텐츠 경쟁력 대폭 강화! ‘게임·음악·출판’ 제작 세액공제 확대법 대표발의</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
더불어민주당 이광재 국회의원(경기 하남시갑)이 기존 영상콘텐츠에 편중되어 있던 제작·투자 세액공제 지원 대상 범위를 게임·음악·출판 등 핵심 문화콘텐츠 산업 전반으로 넓히는 '조세특례제한법 일부개정법률안'을 대표 발의했습니다. 문화 산업 간 세제 불균형을 해소하고 K-콘텐츠의 핵심 뿌리이자 지식재산권(IP) 생태계를 공고히 다지는 이광재 의원의 선제적 입법 성과로 평가받고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kwnews.co.kr/article/20260825501880" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (강원일보) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0826_kj_02.jpg" alt="이광재 의원 게임 음악 출판 세액공제 확대법 대표발의" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 3 (언론보도 - 동아일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.donga.com/news/Economy/article/all/20260826/134543564/2" target="_blank" style="color: inherit; text-decoration: none;">이광재 예결위원장, "27년 동결 배우자 상속공제(5억) 시대상황에 맞게 재검토"… 국세청장 상향 공감 및 중산층 감세 주도</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원장인 이광재 국회의원이 국회 예결위 전체회의에서 1997년 이후 27년째 5억 원으로 동결된 배우자 상속공제 최저한도 문제를 강력히 지적하고 세제 틀의 현실화 재검토를 주도했습니다. 이광재 위원장의 질의와 촉구에 임광현 국세청장도 "물가 상승으로 중산층 세 부담이 과도해진 측면이 있어 개선이 시급하다"며 적극적인 공감과 정상화 추진 의사를 밝혔습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.donga.com/news/Economy/article/all/20260826/134543564/2" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (동아일보) →</a></div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles + '\n',
    content
)

# Section 2: 하남 지역 주요 뉴스
local_news_articles = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 의정/의회</div>
<h3>하남시의회 최승태 운영위원장, 인수 앞둔 위례 근린공원 현장점검</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회 최승태 의회운영위원장이 인수 절차를 앞둔 위례신도시 5단계 근린공원 4호 현장을 직접 찾아 산책로, 운동기구 및 안전 시설물 전반을 꼼꼼히 점검하고, 미비 사항에 대한 시설 보완이 완료된 후 철저히 인수 절차를 진행할 것을 주문했습니다.
</div>
<div class="source">
📌 출처: 글로벌이코노믹
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 교통/도시</div>
<h3>하남시, 감일·위례지구 맞춤형 '수소 DRT(수요응답형 버스)' 9월 전격 도입 확정</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 감일·위례 신도시 주민들의 대중교통 이용 불편을 해소하기 위해 친환경 수소 버스 기반 수요응답형 교통수단(DRT) 운행 계획을 확정하고, 출퇴근시간대 거점 지하철역 연결 노선을 9월부터 대폭 강화하여 배차 간격을 대폭 줄이기로 했습니다.
</div>
<div class="source">
📌 출처: 하남시청 / 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 보건/복지</div>
<h3>하남시 보건소, 폭염 장기화 대응 '취약계층 맞춤형 방문건강관리' 총력</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
8월 말 폭염 지속에 따라 하남시 보건소가 독거어르신 및 만성질환자 등 보건 취약계층 3,000여 가구를 대상으로 전담 간호사 방문 건강점검과 온열질환 예방물품 지급 등 밀착 돌봄 활동을 한층 강화합니다.
</div>
<div class="source">
📌 출처: 인천일보 / 하남뉴스
</div>
</div>

<!-- 지역 뉴스 기사 4 -->
<div class="article-card">
<div class="badge">📰 교육/청소년</div>
<h3>하남시 청소년수련관, 2026 가을학기 청소년 융합인재·디지털 캠프 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시청소년수련관이 2학기를 맞아 초·중·고 청소년 대상 AI코딩, 로봇 공학, 미디어 크리에이터 등 미래 기술 및 창의 융합 인재 육성 프로그램 참가자를 8월 26일부터 선착순 모집합니다.
</div>
<div class="source">
📌 출처: 미디어투데이 / 하남시청소년재단
</div>
</div>

<!-- 지역 뉴스 기사 5 -->
<div class="article-card">
<div class="badge">📰 환경/스마트시티</div>
<h3>하남 미사호수공원 '스마트 수질 자동 측정 &amp; 쿨링포그' 확대 가동</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 미사호수공원의 쾌적한 수변 환경을 유지하기 위해 실시간 AI 수질 자동 모니터링 체계를 갖추고, 늦더위에 지친 산책 시민들을 위해 친환경 미세안개 쿨링포그를 확대 운영합니다.
</div>
<div class="source">
📌 출처: 기호일보 / 하남타임즈
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->|<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 TOP 3
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 뉴홈 사전청약자 40년 장기 모기지 확정 소식… "주거 부담 덜었다" 위례·감일 학부모 환호 (위례맘/감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 국토부의 뉴홈 사전청약자 전용 모기지(40년 만기, 1.9~3.0% 고정금리) 확정 발표 소식이 전해지며 대출 이자 걱정에 떨던 청약 입주예정 학부모들의 관심이 집중되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 고금리 시대에 실질적인 내 집 마련 부담이 대폭 줄어들게 되었다며 이광재 의원의 지속적인 제도 개선 요구와 성과에 깊은 감사를 표했습니다.</div>
<div class="mom-reaction">💬 주민 반응: "대출 금리 때문에 밤잠 설치셨던 분들 숨통이 트이겠어요!", "이광재 의원님이 끝까지 챙겨주신 덕분입니다" 등의 감동 반응이 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 감일·위례 수소 DRT(똑버스) 9월 도입 &amp; 2학기 통학버스 증차 소식 (감일맘/위례맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 감일·위례 신도시 대중교통난을 단비처럼 해소할 친환경 수소 DRT 버스의 9월 개통안과 지하철역 연계 노선 개편 소식이 맘카페에 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들의 학원·학교 등하교길과 직장인 출퇴근길 배차 간격 단축 효과, 똑버스 모바일 앱 예약 사용법이 꿀팁으로 전해졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 학원 갈 때 버스 안 와서 걱정이었는데 정말 반가운 소식이에요", "9월 개통일만 손꼽아 기다립니다" 등의 의견이 나누어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 8월 26일 청소년수련관 가을학기 디지털 캠프 &amp; 문화강좌 수강신청 열기 (미사맘/덕풍맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 26일부터 접수가 시작되는 하남시청소년수련관의 AI코딩·미디어 교실과 주민자치센터 가을 문화강좌 수강신청 소식이 핫이슈로 부상했습니다.</div>
<div class="mom-point">💡 주민 포인트: 아동 로봇 교실, 미술·음악 프로그램 수강신청 성공 노하우와 대기열 조기 마감 정보가 공유되며 열띤 정보 교환이 이어졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "오전 9시 정각 접수 광클 성공했어요!", "2학기 아이들 주말 유익한 수업 들려줄 수 있어 기대됩니다" 등의 반응이 나타났습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

content = re.sub(
    content
)

# Section 5: ALL IN 하남라이프 (모바일 최적화 밀착형 카드 배치)
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[청년/지원] 2026년 청년드림, 제주애(愛) 올레(Olle)? 참가자 모집 공고</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>모집기간:</b> 2026. 8. 25.(화) ~ 8. 31.(월)<br/>
<b>선정규모:</b> 100팀 (팀당 1~2명, 만 19세~34세 청년, 하남 청년 응모 가능!)<br/>
<b>주요내용:</b> 제주시 읍·면 지역 한달살이(21일 이상) 숙박비 지원, 지역 관광자원·문화예술·역사·축제 체험 및 개인 SNS 홍보 진행<br/>
<b>접수방법:</b> 신청서 작성 후 이메일(cnr2013@korea.kr) 개별 접수 (문의: 청년일자리과)
</p>
</div>

<div class="event-card">
<strong>[공연/기획] 8월 26일(수) 오늘 개최! 하남문화예술회관 &lt;피아노 마라톤&gt; &amp; &lt;고상지 콰르텟&gt;</strong>
<p>일시: 2026년 8월 26일(수) 19:30 (대극장 검단홀)<br/>내용: 오늘 저녁! 피아니스트 김태형·김다솔·박진형의 릴레이 클래식 무대와 '문화가 있는 날' 반도네오니스트 고상지 콰르텟의 탱고 연주회가 열립니다. (하남시민 할인 제공)</p>
</div>

<div class="event-card">
<strong>[전시/생활] 하남 미사 마주침갤러리 가을맞이 '그리다 민화전' 개최</strong>
<p>기간: 2026년 8월 24일(월) ~ 9월 4일(금) (하남시 생활문화센터 미사)<br/>내용: 하남 지역 작가와 시민 동호회가 참여하여 전통 민화와 현대적 조형미가 어우러진 40여 점의 작품을 무료 관람할 수 있습니다.</p>
</div>

<div class="event-card">
<strong>[체험/교육] 하남시 청소년수련관 '2026 가을학기 융합인재 디지털 캠프' 8월 26일 접수 시작</strong>
<p>기간: 2026년 8월 26일(수)부터 선착순 모집 (하남시청소년수련관 홈페이지)<br/>내용: 초·중·고 청소년 대상 AI코딩, 3D프린팅, 미디어 크리에이터 2학기 특화 과정이 운영됩니다.</p>
</div>

<div class="event-card">
<strong>[스포츠/축제] 2026 하남 미사경정공원 가을 '88RUN' 러닝 페스티벌 사전 접수</strong>
<p>일시: 2026년 9월 12일(토) 08:00 (미사경정공원 호수산책로)<br/>내용: 시원한 미사 경정호수를 달리는 10km, 5km 및 온 가족 패밀리 코스 사전 예매 신청이 진행 중입니다.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 8월 26일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 6: 공공기관 소식지 (모바일 최적화 밀착형 배치)
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.26</div>
<h3>[하남시청] 감일·위례 신도시 맞춤형 '수소 DRT(똑버스)' 9월 운행 및 2학기 통학노선 확충</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 감일 및 위례 지구 대중교통 이용 편의 확대를 위해 친환경 수소 수요응답형 버스(DRT) 운행 체계를 확정하고, 지하철역 연계 노선과 2학기 맞춤형 학생 통학버스를 증차 배치합니다.
</div>
<div class="source">
📌 출처: 하남시청 도시교통과 고시공고
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.08.26</div>
<h3>[하남시보건소] 8월 말 폭염 지속 대응 취약계층 3,000여 가구 맞춤형 방문건강관리 실시</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 보건소는 늦더위 폭염 경보 지속에 따라 독거어르신 및 만성질환자 가구를 전담 방문하여 혈압·혈당 측정 등 기초 건강 상태 체크와 열사병 예방 물품을 지원합니다.
</div>
<div class="source">
📌 출처: 하남시 보건소 보도자료
</div>
</div>

<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.26</div>
<h3>[청년일자리과] 2026년 청년드림, 제주애(愛) 올레(Olle)? 참가자 모집 공고 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>모집기간:</b> 2026.8.25.(화)~8.31.(월) | <b>선정규모:</b> 100팀(만 19~34세 청년)<br/>
<b>주요내용:</b> 제주시 읍·면 지역 한달살이(21일 이상) 숙박비 지원, 관광자원·문화 체험 및 SNS 홍보<br/>
<b>접수방법:</b> 신청서 이메일 접수(cnr2013@korea.kr / 문의: 청년일자리과)
</div>
<div class="source">
📌 출처: 하남시청 청년일자리과 공지사항
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

# Write to kj_hanam_inside_20260826.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully formatted youth recruitment card for mobile!")
