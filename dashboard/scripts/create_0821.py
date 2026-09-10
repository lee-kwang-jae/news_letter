import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260820.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260821.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Date and Issue number updates
content = content.replace('KJ\'s 하남 인사이드 - 2026년 8월 20일', 'KJ\'s 하남 인사이드 - 2026년 8월 21일')
content = content.replace('22호 | 2026년 8월 20일 발행', '23호 | 2026년 8월 21일 발행')
content = content.replace('📅 발행일: 2026년 8월 20일', '📅 발행일: 2026년 8월 21일')

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 부산일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.busan.com/view/busan/view.php?code=2026081914524242930" target="_blank" style="color: inherit; text-decoration: none;">이광재 "국가 4개 돈주머니 풀어 미래투자… 부산도 과감히 키워야"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원회 이광재 위원장이 부산일보와의 인터뷰에서 국가의 4개 돈주머니(일반회계·특별회계·기금·공공기관 예산)를 적극 활용해 미래 기술·인재·인프라에 대대적인 투자를 집행해야 한다고 강조했습니다. 아울러 부산 북항 돔 아레나 조성, 문현 금융단지 및 동삼 혁신도시 고도화, 가덕도 신공항 중심 교통망 구축 등 지역 미래 성장 동력 확보를 위한 과감한 투자 방안을 제안했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.busan.com/view/busan/view.php?code=2026081914524242930" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (부산일보) →</a></div>
</div>

<!-- 기사 2 (언론보도 - ZDNet Korea) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://zdnet.co.kr/view/?no=20260820082427" target="_blank" style="color: inherit; text-decoration: none;">[이광재 칼럼] 디지털 월세의 시대, 일할 권리에 임대료가 붙었다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 ZDNet Korea 칼럼을 통해 AI, 클라우드, SaaS 등 디지털 서비스 구독료가 개인과 기업의 부담스러운 '디지털 월세'로 작용하고 있음을 지적했습니다. 일할 권리와 생산성 도구에 대한 부과 부담을 줄이고, 국민과 기업의 디지털 자립 및 데이터 주권, 공공 디지털 인프라 및 기술 역량 강화를 위한 국가 차원의 대응 전략 필요성을 역설했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://zdnet.co.kr/view/?no=20260820082427" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (지디넷코리아) →</a></div>
</div>

<!-- 기사 3 (현장소식 1) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.21 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224384696612" target="_blank" style="color: inherit; text-decoration: none;">국비240억 확보! 교산지구 복합커뮤니티 학교</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
'하남교산지구 복합커뮤니티센터 건립' 사업이 최종 확정되어 국비 240억 원을 전격 확보했습니다! 남한중학교가 교산신도시로 이전·신축되며, 학교 시설과 수영장·체육관·도서관 등이 어우러진 지역 맞춤형 복합커뮤니티 학교로 거듭납니다. 학생들에게는 최첨단 교육 환경을, 주민들에게는 쾌적한 문화·체육·복지 인프라를 제공하여 교산지구를 명품 교육·주거 도시로 만들어 가겠습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224384696612" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 국비240억 확보! 교산지구 복합커뮤니티 학교 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0821_kj_02.jpg" alt="국비240억 확보! 교산지구 복합커뮤니티 학교" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 4 (현장소식 2) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.21 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224384568276" target="_blank" style="color: inherit; text-decoration: none;">동서울변전소 협의체 첫걸음 국회 공청회</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
국회에서 동서울변환소 증설 문제를 해결하기 위한 '정부-한전-주민 대표 상생 협의체'가 첫걸음을 뗐습니다. 이광재 의원의 제안으로 성사된 이번 회의에는 기후에너지환경부 장관, 한전 관계자, 하남 주민 대표 등이 참석해 주민 피해 최소화 및 실질적 대책을 논의했습니다. 2달 간의 집중 협의를 통해 주민 중심의 원만한 해결 방안을 끌어내겠습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224384568276" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 동서울변전소 협의체 첫걸음 국회 공청회 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0821_kj_01.jpg" alt="동서울변전소 협의체 첫걸음 국회 공청회" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles,
    content
)

# Section 2: 하남 지역 주요 뉴스
local_news_articles = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 교통/시정</div>
<h3>하남시, 감일·위례 신도시 대중교통 노선 확충 및 주민 이동 편의 개선 본격 추진</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 신도시 입주민들의 출퇴근 교통 불편을 해소하기 위해 감일지구 및 위례지구 내 주요 대중교통 노선 증차와 배차간격 단축을 전격 시행합니다. 시는 대중교통 이용 현황 모니터링을 지속하여 주요 지하철역과의 연계성을 강화하고 출퇴근길 편의를 향상할 방침입니다.
</div>
<div class="source">
📌 출처: 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 아동/복지</div>
<h3>하남시, '대한민국 아동성장환경지표' 전국 9위… 돌봄 인프라 구축 가속화</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 초록우산 발표 '2026 대한민국 아동성장환경지표'에서 전국 9위에 오르며 아동친화도시 입지를 굳혔습니다. 총사업비 260억 원 규모의 '(가칭)하남시 어린이회관' 건립과 24시간 아이돌봄 체계 구축 등 아동 중심 복지 인프라 확충에 속도를 냅니다.
</div>
<div class="source">
📌 출처: 하남시청 보도자료
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 안보/시정</div>
<h3>하남시 및 하남시의회, '2026 을지연습' 종합 상황 점검 완료</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시와 하남시의회는 8월 18일부터 21일까지 진행된 2026 을지연습을 통해 전시 국가위기관리 대책과 관·군·경·소방 긴급재난 대응체계를 면밀히 점검하고 비상 대비 태세를 완벽하게 구축했습니다.
</div>
<div class="source">
📌 출처: 시티뉴스
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 TOP 3
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 2026년 2학기 초등 돌봄교실 & 방과후 학교 수강 신청 개시 (미사맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 넷째 주 개학을 앞두고 하남 관내 초등학교 2학기 방과후 학교 수강 신청 및 돌봄교실 추가 모집 안내가 발표되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 인기 강좌 수강 신청 팁, 맞벌이 가정 추가 증빙 제출서류, 학년별 시간표 매칭 등 엄마들의 정보 공유가 활발히 이뤄졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "인기 컴퓨터/코딩반 수강신청 오픈런 준비 중이에요", "돌봄교실 신청 서류 미리 챙겨야겠네요" 등 뜨거운 반응이 전해졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 감일지구 2학기 개학 대비 '통학순환버스' 시간표 공유 및 올림픽공원역 연계 버스 노선 개편 관심 (감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 넷째 주 개학을 앞두고 감일지구 초등생 통학순환버스 운영 안내와 함께 방아다리길 연결 도로 개통에 따른 올림픽공원역 연계 버스 노선 조정 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 초등학교별 안전 통학버스 승하차 구역, 출퇴근·통학 시간대 지하철역 연계 배차 간격 등 감일 주민들의 실생활 교통 정보가 활발히 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "개학 전 통학버스 노선과 시간표 미리 체크해 둬야겠어요", "올림픽공원역 방향 연결 버스 노선 확충으로 이동이 훨씬 편해지겠네요" 등의 반응이 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 위례복합체육센터 9월 1일 정식 개장 앞두고 '다함께돌봄센터' & 키즈카페 개소 기대감 폭발 (위례맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 개관식을 마친 위례복합체육센터가 시범 운영을 거쳐 9월 1일 정식 개장하며, 센터 내 초등 '다함께돌봄센터(정원 33명)'와 공공형 키즈카페가 9월 중 순차 개소합니다.</div>
<div class="mom-point">💡 주민 포인트: 수영장·체육강좌 수강 신청 일정, 맞벌이 가정을 위한 다함께돌봄센터 신청 조건, 아동 키즈카페 이용 방법 등 위례맘 커뮤니티의 최대 관심사로 등극했습니다.</div>
<div class="mom-reaction">💬 주민 반응: "위례에 드디어 수영장과 돌봄센터가 함께 생겨서 정말 좋습니다", "9월 다함께돌봄센터 접수 일정 나오자마자 바로 신청하려 하고 있어요" 등 기대가 모였습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

content = re.sub(
    content
)

# Section 6: 공공기관 소식지 (Badge dates update)
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.21</div>
<h3>[하남시청] 교산신도시 '학교복합시설' 국비 240억 확보 &amp; '2026 청년 명랑 운동회' 참가 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 교산지구 내 추진 중인 학교복합시설(어울림林캠퍼스) 건립 사업이 교육부 공모에 선정되어 국비 240억 원(총사업비 481억)을 확보했습니다! 실내수영장과 체육관, 도서관 등이 들어서며, 이와 함께 9월 19일 개최되는 청년의 날 기념 '2026 청년 명랑 운동회' 참가자(19~39세 청년 100명)를 8월 20일부터 선착순으로 모집합니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 공고 및 보도자료
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시보건소·재난안전과 | 2026.08.21</div>
<h3>[하남시보건소] 2026년 하반기 민방위 보충교육 실시 및 맞춤형 건강운동교실 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 8월 31일부터 9월 5일까지 하남시청 대회의실에서 1~2년차 민방위 대원 대상 하반기 보충 1차 집합교육을 실시합니다(사이버교육은 9월 18일까지). 아울러 하남시보건소 및 미사보건센터에서 성인과 어르신을 위한 맞춤형 건강증진 운동교실 참가자 모집을 진행합니다.
</div>
<div class="source">
📌 출처: 하남시보건소 및 하남시 재난안전과 공지
</div>
</div>

<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남소방서·하남시의회 | 2026.08.21</div>
<h3>[하남소방서·시의회] 2026 을지연습 비상대응 점검 완료 및 제3회 추경예산안 의결</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남소방서와 하남시의회는 8월 18일부터 21일까지 진행된 2026 을지연습 국가위기관리 및 긴급재난 대응 출동 훈련을 차질 없이 마무리했습니다. 또한 하남시의회는 제351회 임시회를 폐회하고 시민 생활과 밀접한 2026년도 제3회 추가경정예산안 등 주요 20개 안건 심의·의결을 완료했습니다.
</div>
<div class="source">
📌 출처: 하남소방서·하남시의회 보도자료
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Section 5: ALL IN 하남라이프 (지역 문화 소식)
culture_events = """<div class="event-card">
<strong>[축제/공연] 2026 '스테이지 하남!(STAGE HANAM)' 8·9월 주말 야외 버스킹</strong>
<p>일시: 2026년 8월~9월 매주 금·토요일 저녁<br/>장소: 미사호수공원 수변무대, 미사문화거리, 감일·위례 거점 광장<br/>내용: 하남시와 하남문화재단이 주최하는 도심 거리 공연 프로젝트! K-POP, 인디밴드, 재즈, 다채로운 퍼포먼스가 어우러져 한여름 밤 무더위를 식혀줄 야외 버스킹 축제입니다. (전석 무료 관람)</p>
</div>
<div class="event-card">
<strong>[공연/기획] 하남문화예술회관 8월 기획공연 &lt;고상지 콰르텟: 열정과 탱고&gt; & &lt;피아노 마라톤&gt;</strong>
<p>일시: 2026.08.26(수) 19:30 / 08.29(토) 17:00<br/>장소: 하남문화예술회관 대극장(아랑홀)<br/>내용: 반도네온 연주자 고상지 콰르텟의 매혹적인 탱고 무대(8.26)와 대한민국 대표 피아니스트 3인(김태형X김다솔X박진형)이 선사하는 릴레이 피아노 마라톤 공연(8.29)이 찾아옵니다. 하남시민 할인 혜택 제공!</p>
</div>
<div class="event-card">
<strong>[스포츠/체험] 2026 서울올림픽기념 '88RUN' 마라톤 대회 참가자 모집</strong>
<p>일시: 2026년 9월 12일(토) 오전 8시 (온라인 사전 선착순 접수 중)<br/>장소: 하남 미사경정공원 일원<br/>내용: 아름다운 미사경정공원 호수 산책로를 달리는 대표 가을 마라톤 행사입니다. 10km, 5km 및 온 가족이 함께 즐기는 패밀리런 코스로 구성되며 사전 참가 신청이 진행 중입니다.</p>
</div>
<div class="event-card">
<strong>[전시/가족] 하남문화예술회관 아트갤러리 기획전시 &lt;ATO : NOLJA - 도하야 놀자!&gt;</strong>
<p>기간: ~ 2026년 8월 30일(일)까지 (매주 월요일 휴관)<br/>장소: 하남문화예술회관 2층 아트갤러리<br/>내용: 함도하 작가의 해학적이고 친근한 가구 조형 아트퍼니처 작품전입니다. 매주 주말 전시장 내 도슨트 작품 해설 프로그램이 운영되어 아이들과 온 가족이 무료로 관람하실 수 있습니다.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?</div>\s*</div>',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">한눈에 보는 8·9월 하남시 문화·공연·전시 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>\n</div>',
    content
)

# Write to kj_hanam_inside_20260821.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created kj_hanam_inside_20260821.html and updated news/index.html!")
