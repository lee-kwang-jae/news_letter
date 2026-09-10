import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260819.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260820.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Date and Issue number updates
content = content.replace('KJ\'s 하남 인사이드 - 2026년 8월 19일', 'KJ\'s 하남 인사이드 - 2026년 8월 20일')
content = content.replace('21호 | 2026년 8월 19일 발행', '22호 | 2026년 8월 20일 발행')
content = content.replace('📅 발행일: 2026년 8월 19일', '📅 발행일: 2026년 8월 20일')
content = content.replace('📅 발행일: 2026년 8월 17일', '📅 발행일: 2026년 8월 20일')

# Mobile responsive CSS update for max width & readability
mobile_opt_css = """
        /* ---- 모바일 최적화 미디어 쿼리 (가로폭 활용 극대화) ---- */
        @media (max-width: 600px) {
            body {
                padding: 2px !important;
            }
            .container {
                padding: 12px 8px !important;
                border-radius: 8px !important;
            }
            .header-box {
                padding: 16px 12px !important;
                border-radius: 8px !important;
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            .header-box h1 {
                font-size: 1.4rem;
            }
            .weather-widget {
                position: static;
                align-self: flex-start;
                margin-top: 5px;
            }
            .top-nav {
                padding: 6px 10px !important;
                margin-bottom: 14px !important;
                gap: 8px;
            }
            .top-nav a { font-size: 1.2rem; }
            .top-nav span { font-size: 0.75rem; }
            .alert-banner {
                padding: 10px 12px !important;
                font-size: 0.88rem !important;
            }
            .toc {
                padding: 10px 14px !important;
                margin-bottom: 18px !important;
            }
            h2, .section-title {
                font-size: 1.05rem;
                padding: 6px 12px;
                margin-top: 30px;
            }
            .article-card {
                padding: 12px 10px !important;
                margin-bottom: 14px !important;
                border-radius: 10px;
            }
            .article-card h3 {
                font-size: 1rem;
                margin-bottom: 8px;
                word-break: keep-all;
            }
            .summary {
                padding: 10px 8px !important;
                font-size: 0.95rem !important;
                text-align: left;
                word-break: keep-all;
                letter-spacing: -0.3px;
                line-height: 1.65 !important;
            }
            .flex-summary {
                flex-direction: column-reverse !important;
                gap: 12px !important;
            }
            .flex-summary .img-box {
                width: 100% !important;
            }
            .flex-summary .img-box img {
                width: 100% !important;
                height: auto !important;
                max-height: 240px !important;
                object-fit: cover !important;
            }
            .event-grid {
                grid-template-columns: 1fr;
                gap: 12px;
            }
            .event-card {
                padding: 10px !important;
            }
            .mom-issue-card {
                padding: 12px 10px !important;
            }
        }
"""

# Clean replacement of old mobile media query block
content = re.sub(
    r'(?s)/\* ---- 모바일 최적화 미디어 쿼리 ---- \*/\s*@media \(max-width: 600px\) \{.*?\n        \}',
    mobile_opt_css.strip(),
    content
)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260819138300530?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">[전력망 확충 시험대 동서울변환소…정부·주민 '두달 협의' 시작]</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
정부의 전력망 확충 역량을 가늠할 시험대로 꼽히는 '동서울변환소 증설 문제'를 논의하기 위한 협의체가 20일 국회에서 첫 회의를 개최합니다. 회의에는 김성환 기후에너지환경부 장관과 동서울변환소 증설이 추진되는 경기 하남시 감일동을 지역구로 둔 더불어민주당 이광재 의원, 김정호 기후에너지환경노동위원장, 한국전력 관계자, 주민 단체 및 13개 아파트 단지 입주자 대표 등이 참석하여 주민 피해 최소화 및 상생 방안을 논의합니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.yna.co.kr/view/AKR20260819138300530?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>

<!-- 기사 2 (언론보도) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.jeonmae.co.kr/news/articleView.html?idxno=1283636" target="_blank" style="color: inherit; text-decoration: none;">[[PICK! 이 안건] 윤후덕·이광재 등 10인 "경형자동차 이용하는 가계의 유류비 부담 완화해야"]</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 윤후덕·이광재 의원 등 10인이 서민과 소상공인의 유류비 부담을 줄이기 위한 '조세특례제한법 일부개정법률안'을 발의했습니다. 최근 중동 지역 지정학적 불안으로 인한 유류가격 상승으로 가계 부담이 커짐에 따라, 주로 서민과 소상공인이 이동과 생업을 위해 이용하는 배기량 1,000cc 미만의 경형승용 및 경형승합자동차에 대한 세제지원을 확대해야 한다는 취지입니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.jeonmae.co.kr/news/articleView.html?idxno=1283636" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (전국매일신문) →</a></div>
</div>

<!-- 기사 3 (현장소식 1 - 2컬럼 샘플 레이아웃 적용) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.20 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224383586116" target="_blank" style="color: inherit; text-decoration: none;">[오늘 기후에너지환경부 차관을 만났습니다]</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
기후에너지환경부 차관을 만나 동서울변전소 문제, 교산지구 AI 혁신클러스터 등 하남시 주요 시정 및 숙원 현안을 하나하나 짚으며 실질적인 해결책을 강력히 요구했습니다. 동서울변환소 주민 협의체 발족 등 주민 중심의 소통과 해결 방안 마련을 위해 최선을 다하겠습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224383586116" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 오늘 기후에너지환경부 차관을 만났습니다 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0820_kj_01.jpg" alt="오늘 기후에너지환경부 차관을 만났습니다" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 4 (현장소식 2 - 2컬럼 샘플 레이아웃 및 0820_kj_02.jpg 적용) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.20 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224383635069" target="_blank" style="color: inherit; text-decoration: none;">[결산은 성적표가 아니라 설계도입니다]</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
국회 의원회관에서 더불어민주당 예산결산위원회 위원들과 함께 2025회계연도 결산을 앞두고 정부 부처별 주요 쟁점을 점검했습니다. 결산은 단순히 지난해의 성적표가 아닌 내년도 예산의 설계도입니다. 일자리 예산의 고용 창출 효과, AI 투자의 산업 현장 적용, 소상공인 지원의 골목상권 매출 기여도 등을 세심하게 짚어보겠습니다. 잘 쓰인 예산은 확대하고 헛돈 예산은 바로잡아, 지표 너머 국민 삶에 실질적 보탬이 되도록 꼼꼼히 챙기겠습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224383635069" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 결산은 성적표가 아니라 설계도입니다 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0820_kj_02.jpg" alt="결산은 성적표가 아니라 설계도입니다" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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
<div class="badge">📰 아동/복지</div>
<h3>하남시, '대한민국 아동성장환경지표' 전국 9위… (가칭)어린이회관 건립 탄력</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 초록우산 발표 '2026 대한민국 아동성장환경지표'에서 전국 9위를 기록하며 아이 키우기 좋은 우수 지자체로 인정받았습니다. 시는 이에 발맞춰 총사업비 260억 원을 투입해 2027년 하반기 개관을 목표로 풍산동에 건립 중인 '(가칭)하남시 어린이회관' 사업을 차질 없이 추진하고, 24시간 보육 및 돌봄 통합 체계를 더욱 확대할 계획입니다.
</div>
<div class="source">
📌 출처: 하남시청 보도자료
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 교통/시정</div>
<h3>하남시, 국회 국토위에 'GTX-D 황산·교산 경유' 및 '위례신사선 연장' 건의</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 교산신도시와 위례지구의 광역교통난 해소를 위해 국회 국토교통위원회를 방문해 GTX-D 노선의 황산·교산 경유를 제5차 국가철도망 구축계획에 반영하고, 위례신사선 하남 연장을 제5차 광역교통시행계획에 포함해 줄 것을 건의했습니다. 이와 함께 교산신도시 내 생활SOC 15곳의 LH 무상 귀속도 촉구했습니다.
</div>
<div class="source">
📌 출처: 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 안보/시정</div>
<h3>하남시의회, '2026 을지연습' 전시종합상황실 참관 및 안보태세 점검</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회는 8월 18일부터 21일까지 진행되는 2026 을지연습을 맞아 하남시청 전시종합상황실을 방문했습니다. 의원들은 비상근무 공직자들을 격려하고 전시 국가위기관리 대책 및 관·군·경 합동 대응태세를 종합적으로 점검했습니다.
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
<h4>1️⃣ 2026년 가정보육 어린이 '건강과일 지원사업' 신청 접수 시작 (미사맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시에서 어린이집이나 유치원을 이용하지 않고 가정보육 중인 어린이를 대상으로 제철 과일을 지원하는 '2026 가정보육 어린이 건강과일 지원사업' 신청 접수가 시작되었습니다.</div>
<div class="mom-point">💡 주민 포인트: '경기민원24' 온라인 신청 방법, 동 행정복지센터 방문 접수 팁, 지원대상 아동 기준 및 과일 꾸러미 배송 일정 관련 정보가 활발히 공유되고 있습니다.</div>
<div class="mom-reaction">💬 주민 반응: "가정보육 맘들에게 단비 같은 제철 과일 지원이라 바로 신청했어요!", "온라인으로 5분 만에 쉽게 신청 가능하네요" 등 육아맘들의 긍정적 후기가 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 감일지구 '천마산 어린이 숲 놀이터' 8월 말 완공 앞두고 기대감 폭발 (감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 감일지구 인근 천마산 일원에 조성 중인 자연 친화형 '어린이 숲 놀이터'가 8월 말 완공을 목표로 막바지 단장 단계에 들어섰습니다.</div>
<div class="mom-point">💡 주민 포인트: 짚라인, 숲 체험 놀이시설, 황토길 및 야외 휴게 쉼터 등 자연 속에서 아이들이 마음껏 뛸 놀이 공간 개장 소식에 주차 및 진입로 정보 문의가 잇따르고 있습니다.</div>
<div class="mom-reaction">💬 주민 반응: "감일 인근에 아이들 갈 만한 숲놀이터가 생겨 너무 기대됩니다", "날씨 선선해지는 가을 주말 나들이 코스로 딱이겠어요"라며 큰 관심을 모았습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 2학기 개학 맞이 학원가 시간표 & 셔틀버스 노선 정보 공유 (위례맘/미사맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 넷째 주 초·중·고등학교 2학기 개학을 일주일 앞두고 미사·위례 신도시 주요 학원가의 2학기 수강 스케줄과 특강 안내가 잇따르고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 2학기 교재 준비, 학원별 셔틀버스 운행 노선 변경 사항, 방학 숙제 및 개학 준비물 체크리스트 등 학부모 간 실질적인 교육 정보 교환이 이뤄졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "여름방학이 벌써 끝나 아쉽지만 2학기 학원 스케줄 알차게 짜봐야겠네요", "학원 셔틀노선 표 공유해주셔서 큰 도움 됐습니다" 등의 반응이 전해졌습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

content = re.sub(
    content
)

# Section 5: ALL IN 하남라이프
culture_events = """<div class="event-grid">
<div class="event-card">
<strong>[공연/클래식] 하남문화예술회관 기획 &lt;피아노 마라톤: 김태형 X 김다솔 X 박진형&gt;</strong>
<p>일시: 2026년 8월 29일(토) 오후 5시<br/>장소: 하남문화예술회관 대극장(아랑홀)<br/>내용: 대한민국 클래식계를 이끄는 세 명의 정상급 피아니스트가 선보이는 감동의 피아노 마라톤 무대입니다. 하남시민 대상 할인 혜택이 제공되며, 예매는 하남문화재단 홈페이지에서 가능합니다.</p>
</div>
<div class="event-card">
<strong>[전시/체험] 하남문화예술회관 아트갤러리 기획전시 &lt;ATO : NOLJA - 도하야 놀자!&gt;</strong>
<p>기간: 2026.07.28 ~ 08.30 (매주 월요일 휴관)<br/>장소: 하남문화예술회관 2층 아트갤러리<br/>내용: 함도하 작가의 친근하고 해학적인 가구 조형 예술 전시입니다. 매주 주말 전시장 내 도슨트 작품 해설 프로그램이 운영되어 어린이와 온 가족이 함께 무료로 즐기실 수 있습니다.</p>
</div>
<div class="event-card">
<strong>[공연/가족] 어서와! 클래식은 처음이지? ③ &lt;비발디 사계 - 그림자극&gt;</strong>
<p>일시: 2026년 9월 19일(토) 오후 5시 (사전 예매 진행 중)<br/>장소: 하남문화예술회관 대극장<br/>내용: 현악 앙상블의 생생한 라이브 연주와 동화 같은 그림자극이 한데 어우러진 어린이·가족 맞춤형 융합 공연입니다. 명작 '사계'를 시각적 재미와 함께 만나보실 수 있습니다.</p>
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title"[^>]*>🎭 ALL IN 하남라이프</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">.*?</p>\s*<div class="event-grid">.*?</div>\s*</div>',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">한눈에 보는 8·9월 하남시 문화·공연·전시 가이드</p>\n' + culture_events + '\n</div>',
    content
)

# Section 6: 공공기관 소식지
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.20</div>
<h3>[하남시청] 9월 맞춤형 청년 취업지원 및 소상공인 경영환경개선 사업 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시청은 청년 취업 준비생을 위한 '9월 맞춤형 취업지원 프로그램' 참여자 모집과 함께, 관내 소상공인의 마케팅 및 판로 개척을 돕는 '2026년 소상공인 경영환경개선 지원사업' 참여자를 모집합니다. 지원 조건 및 신청 방법은 하남시청 고시/공고 게시판에서 확인하실 수 있습니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 공고
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시보건소 | 2026.08.20</div>
<h3>[하남시보건소] 2026년 하반기 성인·어르신 맞춤형 '건강운동교실' 참가자 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시보건소 및 미사보건센터에서 시민들의 건강증진을 위해 '비만예방 운동교실', '시니어 밸런스 요가', '어르신 활력 운동교실' 참가자를 8월 21일까지 모집합니다. 안내문 QR코드 온라인 접수를 통해 선착순으로 모집하며, 결과는 8월 26일 개별 안내됩니다.
</div>
<div class="source">
📌 출처: 하남시보건소 공지
</div>
</div>

<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남소방서·하남경찰서 | 2026.08.20</div>
<h3>[하남소방서·경찰서] 2026 을지연습 긴급재난합동대응 및 2학기 스쿨존 사전점검</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남소방서와 하남경찰서는 8월 18일부터 21일까지 진행되는 '2026 을지연습' 기간 중 화재·재난 긴급 대응 출동 훈련을 실시하고 있습니다. 아울러 8월 넷째 주 2학기 개학을 앞두고 관내 초등학교 어린이보호구역(스쿨존) 신호기 및 교통안전 시설물 사전 합동 점검을 전개합니다.
</div>
<div class="source">
📌 출처: 하남소방서·하남경찰서 보도자료
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Write to kj_hanam_inside_20260820.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully cleaned mobile CSS media queries and regenerated HTML!")
