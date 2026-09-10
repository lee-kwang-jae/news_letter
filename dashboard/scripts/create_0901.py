import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260831.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260901.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 8월 31일", "KJ's 하남 인사이드 - 2026년 9월 1일")
content = content.replace('29호 | 2026년 8월 31일 발행', '30호 | 2026년 9월 1일 발행')
content = content.replace('📅 발행일: 2026년 8월 31일', '📅 발행일: 2026년 9월 1일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 디스커버리뉴스: 감사원법 개정안) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100153" target="_blank" style="color: inherit; text-decoration: none;">[단독] 이광재 의원, 정책 타당성 감사 제외 법제화 추진…감사원법 개정안 대표발의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 이광재 국회의원이 정부의 중요 정책결정에 대한 타당성 판단은 감사원의 직무감찰 대상에서 제외하되, 정책 추진 과정에서 발생한 불법·부패행위는 계속 감찰하도록 하는 내용의 '감사원법 일부개정법률안'을 8월 31일 대표발의했습니다. 현행 감사사무 처리규칙에 명시된 원칙을 법률로 승격해 정권별 political 감사를 방지하고 공무원들의 소신 행정과 정책 결정을 소신 있게 추진할 수 있도록 보호하는 것이 핵심 취지입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100153" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 이데일리: 이광재 인터뷰) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.edaily.co.kr/News/Read?newsId=01931926645575856&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article" target="_blank" style="color: inherit; text-decoration: none;">[인터뷰] 이광재 "국가 전체 돈을 일하게 하자…증세 부담 적은 복지 가능해"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 정부 예산(약 800조 원)에만 의존하지 않고 연기금(1600조 원), 국공유재산(3500조 원), 국부펀드 등 국가 자산을 총동원해 적극 투자하는 '국가 자산 효율적 운용 전략'을 제안했습니다. 워런 버핏의 투자 철학처럼 국가 돈이 스스로 일하게 만들어 세금 인상 부담을 최소화하면서도 AI 인프라 등 국가 성장 동력 확보와 복지 지출 확대를 동시에 달성하겠다는 혁신적 제언입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.edaily.co.kr/News/Read?newsId=01931926645575856&mediaCodeNo=257&utm_source=naver&utm_medium=referral&utm_campaign=news_syndication&utm_content=original_article" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (이데일리) →</a></div>
</div>
<div class="source">
📌 출처: 이데일리 (노희준 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 새로운 도시와 문명 / 이미지: 0901_kj_01) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224396108941" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "새로운 도시가 새로운 문명을 만듭니다…기회가 사람을 찾아가는 나라로"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 산업화, 정보화 시대를 지나 AI 시대의 도시 발전 방향을 제시했습니다. 산업과 대학, 인재, 보육·교육·의료·문화가 어우러진 '메가성장' 모델을 통해 서울에 가지 않아도 고향에서 꿈꿀 수 있고 기회가 사람을 찾아가는 대한민국을 만들겠다는 비전과 이를 뒷받침할 연내 입법·예산 추진 의지를 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224396108941" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0901_kj_01.jpg" alt="새로운 도시와 문명 비전 제시" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 감일3통 현장 방문 / 이미지: 0901_kj_02) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224395766939" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "개발을 기다리는 동안 주민의 안전이 멈춰서는 안 됩니다" (감일3통 현장 방문)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 하남 감일3통 현장을 직접 방문해 교산신도시 개발 추진 과정에서 도로·교통 안전과 정주 여건 불편을 겪고 있는 감일 주민들의 목소리를 직접 들었습니다. 신도시 개발이 완성될 때까지 주민들의 안전과 일상이 방치되거나 소외되지 않도록 즉각적인 안전대책 마련과 환경 개선에 최선을 다하겠다고 약속했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224395766939" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0901_kj_02.jpg" alt="감일3통 현장 방문 및 주민 소통" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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

# Section 2: 하남 지역 주요 뉴스 (2026.09.01 기준)
local_news_articles = """<!-- 지역 뉴스 기사 1 (교통/도시 - 연합뉴스) -->
<div class="article-card">
<div class="badge">📰 교통/도시</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260831087900061?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">하남드림 광역환승센터, 정부 기본계획 반영…2030년 준공 목표</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
경기 하남시 중부고속도로 하남드림휴게소 일원에 추진 중인 '하남드림 광역환승센터' 구축 사업이 국토교통부 대도시권광역교통위원회의 '제4차 환승센터 및 복합환승센터 구축 기본계획(2026~2030)'에 신규 반영되었습니다. 고속도로 버스 환승과 지하철 3호선 연장선(송파하남선)을 하나로 연결하는 총사업비 1,297억 원 규모의 광역 교통 거점으로 2030년 준공을 목표로 추진됩니다.
</div>
<div class="source">
📌 출처: 연합뉴스 (이우성 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (공원/행정) -->
<div class="article-card">
<div class="badge">📰 공원/행정</div>
<h3>하남시 위례근린공원4호 9월 1일 우선 개방…황토길·숲놀이터 주민 맞이</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 위례신도시 주민 숙원인 위례근린공원4호(학암동 산 30 일원, 186,410㎡)를 10월 말 예정보다 2개월 앞당겨 9월 1일부터 조기 선개방했습니다. 사계절 이용 가능한 174m 맨발 황토길과 세족장, 솔향기길 산책로, 숲속놀이터, 인공폭포, 배드민턴장이 갖춰져 신도시 주민들의 쾌적한 쉼터가 될 것으로 기대를 모읍니다.
</div>
<div class="source">
📌 출처: 인천일보 (이연희 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (경제/복지) -->
<div class="article-card">
<div class="badge">📰 경제/복지</div>
<h3>하남시, 9월 추석 맞아 '하머니' 지역화폐 10% 특별 할인 및 구매 한도 확대</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 9월 추석 명절과 가을철 장바구니 물가 안정을 위해 하남사랑상품권(하머니) 인센티브 할인율 10%를 적용하고 충전 한도를 확대합니다. 관내 전통시장과 골목상권 소상공인 매출 증진과 시민들의 명절 지출 부담 완화에 기여할 것으로 전망됩니다.
</div>
<div class="source">
📌 출처: 하남시청 소식지
</div>
</div>

<!-- 지역 뉴스 기사 4 (의정/시정 - 서울신문) -->
<div class="article-card">
<div class="badge">📰 의정/시정</div>
<h3><a href="https://go.seoul.co.kr/news/newsView.php?id=20260831500212&wlog_tag3=naver" target="_blank" style="color: inherit; text-decoration: none;">정혜영 하남시의회 도시건설위원장 "음악분수는 제대로 검증하고, 민생은 더 촘촘히 살필 것"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
정혜영 하남시의회 도시건설위원장이 미사호수공원 음악분수 및 워터스크린 교체 사업과 관련해 수질, 수심, 토사 퇴적 현황과 향후 유지관리비까지 객관적·체계적으로 검증해야 한다고 강조했습니다. 소상공인 간담회를 통해 주차 공간 확보, 온누리상품권 사용 확대, 문화행사 분산 개최 등 실질적인 상권 활성화 및 민생 지원 대책을 논의했습니다.
</div>
<div class="source">
📌 출처: 서울신문 (서울Pn 명종혁 기자)
</div>
</div>""" tests,StartLine:113,TargetContent:"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 (2026.09.01 기준)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 9월 1일 조기 개방 '위례근린4호공원' 맨발 황토길 첫날 다녀온 실시간 후기 (조회수 1.6만 / 댓글 210+)</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 1일 선개방된 위례근린공원4호(학암동) 황토길과 세족장, 숲속 놀이터 첫날 이용 사진 및 후기가 위례·감일·미사 맘카페에 대거 업로드되어 지역 주민들의 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 황토길 신발 보관함 위치, 세족장 이용법, 유모차 산책 산책로 코스 및 주차 가능 장소가 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "공사가 빨리 끝나 9월 시작부터 황토길 산책할 수 있어 좋네요!", "주말에 아이들과 맨발 걷기하러 꼭 가봐야겠어요" 등 환호 댓글 200여 개가 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ '하남드림 광역환승센터' 국토부 기본계획 최종 확정 소식에 감일·교산·미사 들썩 (조회수 1.3만 / 댓글 175+)</h4>
<div class="mom-detail"><strong>현황:</strong> 지하철 3호선 연장선(송파하남선)과 중부고속도로, 교산신도시 대중교통망을 잇는 '하남드림 광역환승센터' 확정 뉴스가 맘카페에 공유되어 교통 호재로 뜨겁게 논의되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 3호선 역사 위치 예상안, 서울 및 강남 방향 출퇴근 버스 환승 동선과 교산신도시 연결 도로 추진 시점이 집중 질문되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "지하철 3호선과 고속도로 환승이 진짜 획기적이네요", "하남 교통이 날로 좋아져서 기대됩니다" 등 긍정적 댓글이 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 9월 추석맞이 '하머니' 10% 인센티브 충전 오픈…오전부터 신청 열기 폭주 (조회수 1.0만 / 댓글 140+)</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 1일 오전 9시부터 9월 추석맞이 하머니 10% 인센티브 충전이 시작되면서 사용 어플 접속 팁과 명절 장보기 할인 가맹점 정보가 맘카페에 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 전통시장 온누리상품권 중복 혜택 장보기 팁과 마감 전 빠른 인센티브 충전 유의사항 안내.</div>
<div class="mom-reaction">💬 주민 반응: "추석 앞두고 10% 인센티브 받아서 알뜰하게 장볼 수 있겠네요", "오전에 빠르게 충전 성공했습니다!" 등의 반응이 작성되었습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 4: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[청년/행사] 2026 하남 청년명랑운동회 참가자 모집 (9월 19일 개최)</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시/장소:</b> 2026년 9월 19일(토) / 하남 종합운동장 실내체육관<br/>
<b>내용:</b> 하남 청년(만 19~39세) 대상 단합 명랑운동회, E-스포츠 경기, 청년 정책 제안 퀴즈대회 및 풍성한 경품 추첨 (선착순 접수).
</p>
</div>

<div class="event-card">
<strong>[문화/전시] 하남역사박물관 9월 기획전 '이성산성에서 만난 백제의 숨결'</strong>
<p>기간: 2026년 9월 1일(화) ~ 10월 31일(토) / 하남역사박물관 1층 기획전시실<br/>내용: 하남 이성산성 발굴 유물 특별 전시 및 VR 가상현실 백제 성곽 체험존 운영 (무료 관람).</p>
</div>

<div class="event-card">
<strong>[시민/환경] 9월 '하남시민과 함께하는 미사경정공원 가을 줍깅(Plogging) 캠페인'</strong>
<p>일시: 2026년 9월 5일(토) 오전 10시 / 미사경정공원 잔디광장<br/>내용: 미사호수공원 및 경정공원 일대 환경 정화 걷기 활동 (봉사시간 2시간 인정 및 에코백 증정).</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 1일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 5: 공공기관 소식지
public_agency_news = """<!-- 기사 1 (하남시청 - 전통시장 환급 행사) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.01</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 9월 추석 명절 맞이 전통시장 온누리상품권 현장 환급 행사 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>행사기간:</b> 2026.9.1.(화) ~ 9.15.(화) | <b>장소:</b> 덕풍·신장 전통시장<br/>
<b>주요내용:</b> 국산 농축수산물 구매 시 구매 금액대별 최대 2만 원 온누리상품권 현장 환급 제공.<br/>
<b>문의:</b> 하남시청 기업지원과 전통시장팀
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">보도자료 원문 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 기업지원과
</div>
</div>

<!-- 기사 2 (하남시보건소) -->
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
</div>

<!-- 기사 3 (하남시립도서관) -->
<div class="article-card">
<div class="badge">🏛️ 하남시립도서관 | 2026.09.01</div>
<h3>[하남시립도서관] 9월 독서의 달 기념 '도서 대출 수 2배 확대' & 작가 초청 북토크</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시립 미사·나룰·세미도서관에서 9월 독서의 달을 맞아 1인당 도서 대출 수량을 기존 5권에서 10권으로 한 달간 확대하고 베스트셀러 작가 초청 강연회를 개최합니다.
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

# Update Bottom Nav link to include 0831.html and set active 0901
bottom_nav_old = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260831.html" class="active">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'
bottom_nav_new = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260901.html" class="active">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'

content = content.replace(bottom_nav_old, bottom_nav_new)

# Clean up duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260901.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target_path} and updated {index_path}!")
