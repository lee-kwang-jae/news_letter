import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260902.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260903.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 9월 2일", "KJ's 하남 인사이드 - 2026년 9월 3일")
content = content.replace('31호 | 2026년 9월 2일 발행', '32호 | 2026년 9월 3일 발행')
content = content.replace('📅 발행일: 2026년 9월 2일', '📅 발행일: 2026년 9월 3일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재 (사용자 지정 2개 뉴스 URL 및 최신 현장일지 반영)
lawmaker_articles = """<!-- 기사 1 (언론보도 - MBC 뉴스투데이: 용혜인 사퇴 촉구 & 개각/예산 인터뷰 - 2026.09.02) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://imnews.imbc.com/replay/2026/nwtoday/article/6849014_37012.html" target="_blank" style="color: inherit; text-decoration: none;">[인터뷰] 이광재 "용혜인 성평등부 장관 후보 사퇴해야…당내 분위기도 당연" [MBC 모닝콜]</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 더불어민주당 예산결산특별위원장(메가성장특위 수석부위원장)이 MBC 뉴스투데이 '모닝콜' 인터뷰에서 청와대 개각 논란과 관련해 "용혜인 후보자가 장관을 하려면 국회의원직을 사퇴하는 청년다운 과감한 결단이 필요하다"고 당내 분위기를 전달했습니다. 또한 70~80년대생 인사 등용을 긍정 평가하고, 미중 기술패권 전쟁 속 내년 820조 슈퍼 예산안 심의 방향으로 AI 미래 기술 투자, 서민·중소기업 지원 및 청년 자립펀드 조성을 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://imnews.imbc.com/replay/2026/nwtoday/article/6849014_37012.html" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (MBC 뉴스투데이) →</a></div>
</div>
<div class="source">
📌 출처: MBC 뉴스투데이 (손령 앵커 대담)
</div>
</div>

<!-- 기사 2 (언론보도 - 오마이뉴스: 세종시 예산정책협의회 - 2026.09.02) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003263955&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news" target="_blank" style="color: inherit; text-decoration: none;">[현장] 이광재 예결위원장, 세종시 예산정책협의회 참석..."AI 정부 메카 등 자족기능 확보 지원"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 지도부와 세종특별자치시 간 2026 예산정책협의회에 참석한 이광재 국회 예산결산특별위원장이 세종시의 자족도시 전환을 위한 3대 핵심 과제로 ▲중앙부처 연계 'AI 정부 메카 및 교육도시' 브랜드 구축, ▲고교·카이스트 대학·병원 등 정주여건 대책, ▲대전·충남·세종 철도망 연결을 제시하고 헌법 개정을 통한 행정수도 완성 및 국비 지원에 당 차원의 적극 협력을 약속했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003263955&CMPT_CD=P0010&utm_source=naver&utm_medium=newsearch&utm_campaign=naver_news" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (오마이뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 오마이뉴스 (뉴스피치 김이연심 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 노무현의 꿈, 행정수도 세종의 완성 비전) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224398813817" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "노무현의 꿈, 행정수도 세종의 완성으로 나아갈 때입니다"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 더불어민주당 세종시 예산정책협의회에 참석하여 세종시를 단순 공무원 도식을 넘어 전 세계에 AI 정부 모델을 수출하고 교육·의료·문화 정주 여건을 대폭 확충하는 '글로벌 AI 혁신도시'로 성장시킬 비전을 발표했습니다. 이 의원은 개헌 추진과 국회의사당 완전 이전을 통해 명실상부한 행정수도를 완성하겠다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224398813817" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0903_kj_01.jpg" alt="행정수도 세종 완성 예산정책협의회" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 부천 특강: 만화·웹툰 IP 미래 먹거리 & 원도심 비전) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224398571067" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "부천의 만화·웹툰 IP를 미래 먹거리로, 원도심 변화는 주민과 함께"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 이건태 의원 초청으로 부천시병 당원 대상 특강을 열고 부천의 강력한 만화·웹툰 콘텐츠를 고부가가치 IP 및 신산업 일자리로 키우는 미래 먹거리 전략을 발표했습니다. 이 의원은 원도심 정비 개발의 성과가 지역 주민들의 삶의 질 향상과 양질의 일자리로 환원되어야 함을 피력했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224398571067" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0903_kj_02.jpg" alt="부천 당원 강연 현장" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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

# Section 2: 하남 지역 주요 뉴스 (9월 2일~3일 최신 4개 기사 반영)
local_news_articles = """<!-- 지역 뉴스 기사 2 (문화/교육 - 글로벌에픽: 하남시 9개 도서관 독서의 달) -->
<div class="article-card">
<div class="badge">📰 문화/교육</div>
<h3><a href="https://www.globalepic.co.kr/view.php?ud=2026090215465065815f69d33b22_29" target="_blank" style="color: inherit; text-decoration: none;">하남시, 독서의 달 맞아 도서관서 108개 다채로운 문화 프로그램 운영</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 9월 ‘독서의 달’을 맞아 관내 9개 공공도서관(미사·신장·나룰·위례·감일·일가·세미·덕풍·디지털)에서 총 108개의 독서문화 프로그램을 본격 운영합니다. 베스트셀러 작가 초청 북토크, 중장년층 대상 'AI 자서전 작성 강좌', 초등 문해력·샌드아트 공연과 함께 도서 대출 2배 확대(10권) 및 '연체지우개' 이벤트가 펼쳐집니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.globalepic.co.kr/view.php?ud=2026090215465065815f69d33b22_29" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (글로벌에픽) →</a></div>
</div>
<div class="source">
📌 출처: 글로벌에픽 (이정훈 CP)
</div>
</div>

<!-- 지역 뉴스 기사 3 (체육/지역 - 중부일보: 하남 남한중 핸드볼 결승 진출) -->
<div class="article-card">
<div class="badge">📰 체육/지역</div>
<h3><a href="https://www.joongboo.com/news/articleView.html?idxno=363735606" target="_blank" style="color: inherit; text-decoration: none;">하남 남한중, 핸드볼코리아 중고선수권 준결승서 33-32 승리하며 결승 진출…3일 우승 도전</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남 남한중학교 핸드볼 팀이 9월 2일 경북 김천종합운동장에서 열린 '핸드볼코리아 전국중고등선수권대회' 남중부 준결승에서 부천남중과의 접전 끝에 33-32로 극적인 승리를 거두며 결승 무대에 올랐습니다. 남한중은 9월 3일 결승전에서 전국 정상 도전에 나섭니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.joongboo.com/news/articleView.html?idxno=363735606" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (중부일보) →</a></div>
</div>
<div class="source">
📌 출처: 중부일보 (조승화 기자)
</div>
</div>

<!-- 지역 뉴스 기사 4 (정치/예산 - 경기신문: 민주당 전국 예산 챙기기 예결위 심사) -->
<div class="article-card">
<div class="badge">📰 정치/예산</div>
<h3><a href="https://www.kgnews.co.kr/news/article.html?no=910092" target="_blank" style="color: inherit; text-decoration: none;">민주당, 전국 '예산 챙기기' 시동…이광재 예결위원장 "지역 숙원 국회 예산 심사서 집중 지원"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당이 9월 2일 세종시청에서 첫 예산정책협의회를 열고 전국 순회 일정에 돌입했습니다. 이광재 국회 예산결산특별위원장은 당 지도부와 함께 참석하여 지자체별 핵심 현안과 민생 숙원 사업 예산이 이번 정기국회 예산 심의 과정에서 차질 없이 반영될 수 있도록 최우선으로 챙기겠다고 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kgnews.co.kr/news/article.html?no=910092" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경기신문) →</a></div>
</div>
<div class="source">
📌 출처: 경기신문 (한주희 기자)
</div>
</div>

<!-- 지역 뉴스 기사 5 (안전/교통 - 경기신문: 하남시 포트홀 민원 4배 급증) -->
<div class="article-card">
<div class="badge">📰 안전/교통</div>
<h3><a href="https://www.kgnews.co.kr/news/article.html?no=909830" target="_blank" style="color: inherit; text-decoration: none;">[하남시 포트홀 민원 4배 급증] 이상기후 여파 도로 파손 잇따라…신속 보수 및 안전 대책 시급</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
폭염과 집중호우 등 이상기후 영향으로 도내 도로 파손이 늘어나는 가운데, 하남시의 포트홀 관련 피해 민원이 2022년 11건에서 지난해 46건으로 4배 이상 급증하고 보상액도 불어났습니다. 야간 운전자 및 시민 안전 확보를 위해 단순 일회성 응급복구를 넘어 하남시 차원의 철저한 점검과 재발 방지 중심의 도로 관리 체계 마련이 촉구됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kgnews.co.kr/news/article.html?no=909830" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경기신문) →</a></div>
</div>
<div class="source">
📌 출처: 경기신문 (김민준 기자)
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 (9월 3일 최신 소식으로 업데이트)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 위례근린4호공원 맨발 황토길·온수 세족장 9월 1일 조기 개방 소식에 주민 환호 (조회수 2.1만 / 댓글 310+)</h4>
<div class="mom-detail"><strong>현황:</strong> 위례신도시 주민 숙원이었던 위례근린4호공원이 9월 1일부터 전격 조기 개방되어 174m 사계절 맨발 황토길과 온수 세족장, 인공폭포 생생 이용 후기가 미사·위례·감일 맘카페에 연이어 게재되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들과 주말 황토길 맨발 걷기 체험 후기, 온수 세족장 위치, 세면도구 챙기기 및 인공폭포 포토존 꿀팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "인수인계 전인데 주민 위해 빠르게 열어줘서 최고네요!", "주말에 아이들 데리고 인공폭포랑 황토길 다녀와야겠어요" 등 댓글 310여 개 돌파.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 하남 9개 도서관 9월 '독서의 달' AI 자서전·작가 북토크 수강신청 오픈 (조회수 1.8만 / 댓글 240+)</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 독서의 달을 맞아 하남시 9개 공공도서관의 대출 2배 확대(10권) 혜택 및 초등 AI 자서전·디자이너 클래스, 유명 작가 북토크 수강신청이 시작되어 학부모들의 신청 열기가 뜨겁습니다.</div>
<div class="mom-point">💡 주민 포인트: 미사·나룰·감일도서관 인기 특강 선착순 신청 마감 시간 및 어린이 샌드아트 공연 관람 팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "가을에 도서관 대출도 10권으로 늘고 특강도 다양해서 좋네요", "아이 AI 클래스 광속으로 신청 성공했습니다!" 추천 댓글 잇따름.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 9월 5일 '스테이지 하남' 미사호수공원 개막 공연 라인업 피프티피프티·KCM 반응 폭발 (조회수 1.6만 / 댓글 190+)</h4>
<div class="mom-detail"><strong>현황:</strong> 오는 9월 5일(토) 미사호수공원 잔디광장에서 열리는 2026 하반기 스테이지 하남 오픈공연에 피프티피프티, KCM, 분리수거 밴드 출연 소식이 전해지며 맘카페에서 큰 기대를 모으고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 미사호수공원 잔디광장 돗자리 명당자리 자리잡기 팁, 미사역 주차 및 가족 간식 준비 팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "피프티피프티가 미사호수공원에 오다니 무조건 가야겠네요!", "이번 주 토요일 저녁 가족 나들이 장소 확정입니다" 기대감 고조.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 4: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[공연/축제] 2026 하반기 스테이지 하남 (Stage Hanam) 개막 공연 (9월 5일 개최)</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시/장소:</b> 2026년 9월 5일(토) 17:00~ / 미사호수공원 잔디광장<br/>
<b>내용:</b> 피프티피프티, KCM, 밴드 분리수거, 치어리딩, 스트리트댄스 개막 공연 (무료 관람).
</p>
</div>

<div class="event-card">
<strong>[문화/체험] 하남시립도서관 9월 '독서의 달' 108개 강연·AI 클래스 (9월 1일~30일)</strong>
<p>기간: 2026년 9월 1일(화) ~ 9월 30일(수) / 관내 9개 공공도서관<br/>내용: 대출 권수 2배 확대(10권), 작가 북토크, 초등 AI 교실, 샌드아트 공연 (무료 수강).</p>
</div>

<div class="event-card">
<strong>[공원/힐링] 위례근린4호공원 맨발 황토길 & 온수 세족장 조기 개방 (9월 1일~)</strong>
<p>위치: 위례신도시 위례근린4호공원 내<br/>내용: 174m 사계절 황토길, 온수 세족장, 인공폭포, 어린이 숲속 놀이터 운영 (시민 무료 이용).</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 3일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 5: 공공기관 소식지 (9월 3일 기준 최신 소식)
public_agency_news = """<!-- 기사 1 (하남시청 - 위례근린4호공원 개방) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.02</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 위례근린4호공원 9월 1일 자 시민 조기 개방 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>개방일시:</b> 2026.9.1.(화)부터 시민 조기 개방 | <b>위치:</b> 위례신도시 위례근린4호공원<br/>
<b>주요시설:</b> 174m 황토길, 온수 세족장, 인공폭포, 숲속 놀이터 이용 가능.<br/>
<b>문의:</b> 하남시청 공원녹지과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 공원녹지과
</div>
</div>

<!-- 기사 2 (하남시립도서관 - 독서의 달) -->
<div class="article-card">
<div class="badge">🏛️ 하남시 도서관 | 2026.09.02</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시립도서관] 2026년 9월 '독서의 달' 108개 강연·행사 통합 일정 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>행사기간:</b> 2026.9.1.(화) ~ 9.30.(수) | <b>장소:</b> 미사·나룰·위례 등 9개 공공도서관<br/>
<b>주요내용:</b> 9월 한 달간 도서 대출 2배 확대(10권), 작가 북토크 및 AI 클래스 운영.<br/>
<b>문의:</b> 하남시 미사도서관
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시 도서관) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 미사도서관
</div>
</div>

<!-- 기사 3 (하남시청 - 주민자치 수강생 모집) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.02</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 2026년 4분기 위례동·미사동 주민자치센터 수강생 모집 공고 (9.10~9.14)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접수기간:</b> 2026.9.10.(목) ~ 9.14.(월) | <b>추첨일:</b> 2026.9.15.(화)<br/>
<b>주요내용:</b> 4분기 교양·문화·체육 강좌 수강생 모집 (인터넷 및 방문 접수).<br/>
<b>문의:</b> 위례동/미사동 주민자치센터
</div>
<div class="source">
📌 출처: 하남시 주민자치센터
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Update Bottom Nav link to include 0902.html and set active 0903
bottom_nav_old = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260902.html" class="active">31호 (09/02)</a> | \n<a href="kj_hanam_inside_20260901.html">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'
bottom_nav_new = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260903.html" class="active">32호 (09/03)</a> | \n<a href="kj_hanam_inside_20260902.html">31호 (09/02)</a> | \n<a href="kj_hanam_inside_20260901.html">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'

content = content.replace(bottom_nav_old, bottom_nav_new)

# Clean up duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260903.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target_path} and updated {index_path} with 2026-09-03 issue!")
