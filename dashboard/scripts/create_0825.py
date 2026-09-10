import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260824.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260825.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace('KJ\'s 하남 인사이드 - 2026년 8월 24일', 'KJ\'s 하남 인사이드 - 2026년 8월 25일')
content = content.replace('24호 | 2026년 8월 24일 발행', '25호 | 2026년 8월 25일 발행')
content = content.replace('📅 발행일: 2026년 8월 24일', '📅 발행일: 2026년 8월 25일')

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 파이낸셜뉴스) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.fnnews.com/news/202608241112046347" target="_blank" style="color: inherit; text-decoration: none;">이광재 예결위원장, 내년도 800조 '슈퍼예산' 당정협의 주도… 국가 미래사업 및 지역 예산 확보 총력</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원장인 더불어민주당 이광재 국회의원(경기 하남시갑)이 지도부 및 기획예산처 장관과 함께 800조 원이 넘는 규모의 내년도 정부 예산안 당정협의에 나섭니다. 이광재 위원장은 예결위 수장으로서 100조 원 규모의 미래대응기금 신설 및 AI·반도체 등 3대 메가프로젝트 국비 지원을 면밀히 심의하고, 하남시 광역 교통망 및 자족도시 인프라 예산 반영을 주도할 방침입니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.fnnews.com/news/202608241112046347" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (파이낸셜뉴스) →</a></div>
</div>

<!-- 기사 2 (언론보도 - 기호일보/강원도민일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3032541" target="_blank" style="color: inherit; text-decoration: none;">이광재 의원, 3기 신도시 원주민 생계·재정착 의무화 '공공주택 특별법 개정안' 대표발의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 이광재 국회의원(경기 하남시갑)이 3기 신도시 등 공공주택지구 개발 시 원주민들의 실질적인 생계 대책과 재정착 지원을 의무화하는 '공공주택지구 원주민 생계지원법(공공주택 특별법 일부개정법률안)'을 대표 발의했습니다. 현행 임의규정이었던 주민 지원대책을 의무화하고 직업전환 훈련, 소득창출 지원, 주민생계조합의 법적 근거 신설 등을 명시하여 일회성 보상을 넘어 지속 가능한 상생 방안을 마련했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3032541" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (기호일보) →</a></div>
</div>

<!-- 기사 3 (현장소식 1 - 이광재 네이버 블로그 [국민에게는 대안이 필요합니다]) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.25 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224388658273" target="_blank" style="color: inherit; text-decoration: none;">이광재 의원, "비판 넘어 실질적 대안 중심 예결위 결산 심사 및 공공주택 특별법 추진"</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회 예산결산특별위원장이 예결위 결산 심사 시작에 맞춰 '단순 비판을 넘어 국민의 삶을 위한 실질적 대안'을 제시하는 의정 철학을 밝혔습니다. 교산지구 등 3기 신도시 원주민 생계 대책과 신속 주택 공급을 동시에 달성하는 '공공주택 특별법 개정안' 발의 취지를 전하며, 지난해 정부 예산 심의에 그치지 않고 내년도 예산이 하남시민과 국민을 위해 차질 없이 쓰이도록 '대안을 만드는 국회'를 이끌겠다고 선언했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224388658273" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 이광재, [국민에게는 대안이 필요합니다] | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0825_kj_02.jpg" alt="이광재, 국민에게는 대안이 필요합니다" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 4 (현장소식 2 - 이광재 네이버 블로그 [주간이광재]) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.25 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224388287653" target="_blank" style="color: inherit; text-decoration: none;">[주간이광재] 이광재 국회의원 8월 셋째 주 의정활동 보고… 교통·교산지구·청년 예산 현장 소통 총력</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원(경기 하남시갑)이 8월 셋째 주 주요 의정활동 소식을 하남시민들에게 보고했습니다. 교산 신도시 원주민의 안정적인 재정착과 소득 창출을 보장하는 '공공주택 특별법 개정안' 대표 발의부터, 감일·위례 대중교통 노선 증차 및 DRT 수소버스 도입 주민간담회, 국회 예결위원장으로서 800조 원 규모 내년도 예산안 당정협의 주도, 청년 인재 양성을 위한 국가 지원 체계 구축 구상까지 하남 발전과 시민 삶의 질 향상을 위한 현장 밀착 의정 행보를 종합 발표했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224388287653" target="_blank" style="color: #718096; text-decoration: underline;">[출처] [주간이광재] 8월 셋째 주 의정보고서 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0825_kj_01.jpg" alt="[주간이광재] 8월 셋째 주 의정보고서" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles,
    content
)

# Section 2: 하남 지역 주요 뉴스 (2026년 8월 25일 최신 뉴스)
local_news_articles = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 행정/치안</div>
<h3>하남시 미사권역 지구대 통폐합 계획 전면 백지화… 주민 5천 명 서명 결실</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남 미사권역 지구대 통폐합 추진에 대한 주민 반발과 5,000여 명의 서명부 전달 끝에 하남경찰서가 미사 지구대 통폐합 계획을 전면 철회하기로 최종 결정했습니다. 치안 공백 우려를 해소하고 미사지구 주민들의 안전한 거주 환경이 유지되게 되었습니다.
</div>
<div class="source">
📌 출처: 1간경기 / 인천일보
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 세정/교통</div>
<h3>하남시, 8월 25일 '체납차량 일제단속의 날' 전격 단속 실시</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 8월 25일을 2026년 3분기 체납차량 일제단속의 날로 지정하고 자동차세 2회 이상 체납 차량 및 30만 원 이상 과태료 체납 차량에 대해 번호판 영치를 실시합니다. 생계형 체납자에 대해서는 체납 분납을 유도하며 유연한 대응을 병행합니다.
</div>
<div class="source">
📌 출처: 미디어투데이 / 깜짝뉴스
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 안전/사회</div>
<h3>하남시안전체험장 - 나래에너지서비스, 지역 안전문화 확산 MOU 체결</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시안전체험장과 나래에너지서비스가 8월 24일 지역 사회 안전문화 확산 및 에너지·전기안전 체험교육 협력을 위한 업무협약(MOU)을 체결하고 시민 맞춤형 안전 캠페인을 공동 추진하기로 했습니다.
</div>
<div class="source">
📌 출처: 모닝투데이 / 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 4 -->
<div class="article-card">
<div class="badge">📰 상하수도/주거</div>
<h3>하남시, '노후 옥내 급수관 개량 지원사업' 잔여 예산 추가 접수</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 20년 이상 경과한 노후 주택의 녹슨 수도관 교체 및 갱생 비용을 최대 지원하는 사업의 잔여 예산(약 10%)에 대해 소진 시까지 추가 신청을 접수받아 깨끗한 수돗물 공급에 나섭니다.
</div>
<div class="source">
📌 출처: 오마이뉴스 / 하남시청
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 TOP 3 (2026년 8월 25일 최신 기준)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 하남 미사 지구대 통폐합 철회 확정… "주민 치안 지켜내 다행" 환호 (미사맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 주민 5천여 명 서명 운동과 지역 정치권 항의 전달로 하남 미사 지구대 통폐합안이 전면 취소되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들 안전 및 야간 치안 불안에 떨던 미사 학부모 커뮤니티에서 기쁜 소식이 전해지며 서로 감사를 나눴습니다.</div>
<div class="mom-reaction">💬 주민 반응: "지구대 사라지는 줄 알고 걱정 많았는데 철회되어서 정말 다행이에요!", "아이들 등하교길 치안 지켜내서 뿌듯합니다" 등의 반응이 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 8월 25일 체납차량 단속 및 노후 수도관 교체비 지원 추가 신청 정보 (감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시의 체납차량 번호판 영치 단속 소식과 함께, 20년 이상 된 아파트·빌라 노후 옥내 급수관 개량 지원사업 잔여 예산 추가 신청 정보가 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 오래된 빌라 및 단독주택 녹물 문제 해결을 위한 최대지원금 신청 팁 및 체납 자동차세 주의사항이 함께 전달되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "우리 빌라 수도관 녹물 걱정이었는데 지원금 신청 알아봐야겠어요", "주민세랑 세금 납부일 체크하세요" 등의 유용한 팁이 공유되었습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 2학기 개학 이튿날 학교 통학로 스쿨존 안전점검 &amp; 방과후 수업 신청 열기 (위례맘/덕풍맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 개학 2일차를 맞이해 각 초등학교별 학부모 폴리스 및 스쿨존 보행 안전점검, 2학기 방과후 학교 수강신청 공유가 활발합니다.</div>
<div class="mom-point">💡 주민 포인트: 2학기 교내 동아리·방과후 인기 강좌 티켓팅 성공 후기, 스쿨존 내 펜스 및 신호등 안전점검 요청 글이 큰 공감을 얻었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "방과후 컴퓨터·수학 교실 신청 겨우 성공했네요!", "아이들 등하교 통학로 횡단보도 안전 신경 써주세요" 등의 의견이 전해졌습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

content = re.sub(
    content
)

# Section 5: ALL IN 하남라이프 (2026년 8월 25일 자 최신 기획 공연·전시·축제 기준 교체)
culture_events = """<div class="event-card">
<strong>[공연/기획] 8월 26일(수) 하남문화예술회관 &lt;피아노 마라톤&gt; &amp; &lt;고상지 콰르텟&gt;</strong>
<p>일시: 2026년 8월 26일(수) 19:30 (대극장 검단홀)<br/>내용: 피아니스트 김태형·김다솔·박진형이 선보이는 릴레이 클래식 무대와 '문화가 있는 날' 반도네오니스트 고상지 콰르텟의 낭만 탱고 라이브 연주회가 펼쳐집니다. (하남시민 할인 제공)</p>
</div>

<div class="event-card">
<strong>[축제/버스킹] 2026 '스테이지 하남!(STAGE HANAM)' 9월 도심 야외 버스킹 개막</strong>
<p>일시: 2026년 9월 첫째 주말부터 매주 금·토 저녁<br/>장소: 미사문화거리, 미사호수공원 수변무대, 하남시청역 광장 일원<br/>내용: 하남시 대표 도심 버스킹 프로젝트! 하절기 휴식기를 마치고 9월부터 K-POP, 인디 밴드, 댄스, 포크송 등 풍성한 버스킹 공연이 시작됩니다. (전석 무료 관람)</p>
</div>

<div class="event-card">
<strong>[전시/생활] 생활문화센터 미사 마주침갤러리 '그리다 민화전' 개최</strong>
<p>기간: 2026년 8월 24일(월) ~ 9월 4일(금) (하남시 생활문화센터 미사)<br/>내용: 하남 지역 작가와 시민 동호회가 참여하여 전통 민화와 현대적 아름다움이 조화된 40여 점의 작품을 선보이는 가을맞이 특별 무료 기획 전시회입니다.</p>
</div>

<div class="event-card">
<strong>[스포츠/체험] 2026 서울올림픽기념 '88RUN' 하남 미사경정공원 마라톤 사전 예매</strong>
<p>일시: 2026년 9월 12일(토) 오전 8시 (온라인 사전 선착순 접수 중)<br/>장소: 하남 미사경정공원 및 호수 산책로 일원<br/>내용: 시원한 미사경정공원 호숫가를 달리는 가을 러닝 축제! 10km, 5km 및 가족 패밀리런 코스가 운영되며 참가자에게 기념품이 지급됩니다.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?</div>\s*</div>',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 8월 25일 기준 한눈에 보는 하남시 최신 문화·공연·전시 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>\n</div>',
    content
)

# Section 6: 공공기관 소식지 (2026년 8월 25일 자 기준 교체)
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.25</div>
<h3>[하남시청] 8월 25일 체납차량 일제단속 실시 &amp; 노후 옥내 급수관 개량 지원 추가 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 8월 25일을 3분기 체납차량 일제단속의 날로 지정하여 자동차세 및 과태료 체납 차량 번호판 영치를 실시합니다. 또한 20년 이상 경과 노후 주택의 녹슨 수도관 교체 지원사업 잔여 예산 추가 신청을 접수 중입니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 고시공고 및 보도자료
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시 복지센터 | 2026.08.25</div>
<h3>[하남시감일종합사회복지관] 8월 25일 지역주민 대상 고립·고독사 예방 교육 실시</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 감일종합사회복지관은 8월 25일 사회적 고립 가구 발굴 및 고독사 예방을 위해 지역 주민 및 복지 리더를 대상으로 '우리 동네 이웃 보살핌 맞춤 교육'을 개최합니다.
</div>
<div class="source">
📌 출처: 하남시 감일종합사회복지관 공지사항
</div>
</div>

<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남시 안전체험장 | 2026.08.25</div>
<h3>[하남시안전체험장] 나래에너지서비스 업무협약 체결 및 시민 안전체험 교육 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시안전체험장과 나래에너지서비스가 지역 사회 안전 문화 정착을 위해 에너지·전기안전 인프라 공유 MOU를 체결하고 9월 시민 맞춤형 체공형 안전교육 프로그램 수강생을 모집합니다.
</div>
<div class="source">
📌 출처: 하남시안전체험장 보도자료
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Write to kj_hanam_inside_20260825.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated 0825_kj_01.jpg image for Weekly Lee Kwang-jae card!")
