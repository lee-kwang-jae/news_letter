import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260821.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260824.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Date and Issue number updates
content = content.replace('KJ\'s 하남 인사이드 - 2026년 8월 21일', 'KJ\'s 하남 인사이드 - 2026년 8월 24일')
content = content.replace('23호 | 2026년 8월 21일 발행', '24호 | 2026년 8월 24일 발행')
content = content.replace('📅 발행일: 2026년 8월 21일', '📅 발행일: 2026년 8월 24일')

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 데일리한국) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://daily.hankooki.com/news/articleView.html?idxno=1398158" target="_blank" style="color: inherit; text-decoration: none;">이광재, 하남시 대중교통 이용 환경 개선</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 이광재 국회의원(경기 하남시갑)이 지역 광역버스 교통 대책 주민간담회를 개최했습니다. 감일동 KJ프라자에서 진행된 이번 간담회에서는 철도망이 미비한 감일·위례 지역의 신규 버스 노선 신설, 기존 노선 증차, 서울 거점 연결 수소버스 DRT(수요응답형 버스) 도입 등 실효성 있는 교통 개선 대책이 집중 논의되었습니다. 현장에는 국토교통부 대도시권광역교통위원회(대광위) 관계자도 함께 참여해 주민 목소리를 청취했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://daily.hankooki.com/news/articleView.html?idxno=1398158" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (데일리한국) →</a></div>
</div>

<!-- 기사 2 (언론보도 - 기호일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3032277" target="_blank" style="color: inherit; text-decoration: none;">하남시 주민생계조합, 이광재 국회의원과 간담회 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 주민생계조합이 이광재 국회의원 지역사무소에서 하남시 발전을 위한 주요 현안과 사업 성공 방향을 모색하는 제2차 간담회를 가졌습니다. 이광재 의원은 세종시 주민생계조합 및 강원도 주민주식회사 성공 사례를 강조하며, 하남시 주민생계조합이 지역의 앵커 기업으로 성장해 일자리 창출과 소득 증대를 이뤄낼 수 있도록 예산결산특별위원장으로서 지속적인 성원과 지원을 아끼지 않겠다고 약속했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3032277" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (기호일보) →</a></div>
</div>

<!-- 기사 3 (현장소식 1 - 주민생계조합) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.24 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224385861698" target="_blank" style="color: inherit; text-decoration: none;">하남 주민생계조합이 성공하는 길</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 신장동 사무실에서 하남교산 주민생계조합 관계자들과 면담을 갖고, 신도시 원주민의 안정적인 생계 지원과 재정착을 뒷받침하기 위한 입법 및 제도 정비 방안을 논의했습니다. 세종시 성공 사례 연구를 바탕으로 공공택지지구 개발 과정에서 주민생계조합이 신뢰받는 파트너로 자리매김하고 원주민들이 온당한 보상과 정착 지원을 받을 수 있도록 조만간 구체적인 입법 대책을 발표하고 지원할 것을 약속했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224385861698" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 하남 주민생계조합이 성공하는 길 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0824_kj_01.jpg" alt="하남 주민생계조합이 성공하는 길" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 4 (현장소식 2 - 청년인재양성 아카데미) -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.24 | 현장소식</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae" target="_blank" style="color: inherit; text-decoration: none;">청년이 더 큰 꿈과 계획을 가질 수 있도록</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 의원이 청년인재양성 프로젝트 ‘YIP 인생개념 아카데미’에 참석해 청년과 대한민국의 미래를 주제로 뜻깊은 대화를 나눴습니다. 시대의 에너지가 한 세대를 단단하게 만들듯, 미래펀드·대학도시·국가 보육 및 교육 시스템을 구축하여 청년들이 스무 살 출발선부터 자산, 취업, 주거 부담 없이 안심하고 도전할 수 있도록 국가적 지원 체계를 혁신하고 더 큰 꿈을 응원해 나가겠다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 청년이 더 큰 꿈과 계획을 가질 수 있도록 | 작성자 이광재</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0824_kj_02.jpg" alt="청년이 더 큰 꿈과 계획을 가질 수 있도록" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles,
    content
)

# Section 2: 하남 지역 주요 뉴스 (2026년 8월 24일 최신 뉴스)
local_news_articles = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 경제/소상공인</div>
<h3>하남시, '2026 소상공인 경영환경개선 지원사업' 참여자 모집… 점포당 최대 180만 원 지원</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시와 경기테크노파크가 관내 소상공인의 자생력과 경쟁력을 높이기 위해 '2026년 소상공인 경영환경개선 지원사업'을 전격 추진합니다. 점포 환경 개선, 키오스크·POS 등 시스템 개선, 제품 제작 및 홍보 비용 등을 점포당 최대 180만 원(공급가액의 90%)까지 지원하며, 신청은 8월 31일 오후 6시까지 온·오프라인으로 접수합니다.
</div>
<div class="source">
📌 출처: 하남시청 보도자료 / GNI뉴스
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 도시개발/교육</div>
<h3>하남 교산지구 '어울림(林) 캠퍼스' 국비 240억 확보 확정… 2029년 개교 목표</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남 교산 신도시 내 추진 중인 세대 통합형 학교복합시설 '어울림(林) 캠퍼스(가칭 교산1초)'가 교육부 공모사업에 선정되어 국비 240억 원(총사업비 481억 원)을 전격 확보했습니다. 남한중학교 이전·신축과 연계되어 생존수영장, 다목적체육관, 돌봄 공간이 어우러진 융복합 거점으로 조성됩니다.
</div>
<div class="source">
📌 출처: 뉴스천지 / 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 부동산/도시계획</div>
<h3>서울 근교 그린벨트 해제 추진 본격화… 하남 감북·초이 지구 발전 전망 관심 고조</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
정부의 수도권 주택 공급 확대 대책에 따라 서울 경계 신규 개발제한구역(GB) 해제 대상지 논의가 구체화되면서, 하남시 감북·초이 등 입지 우수 지역의 광역 교통망 연계 및 명품 주거 단지 조성 가능성에 지역사회의 관심이 집중되고 있습니다.
</div>
<div class="source">
📌 출처: 서울경제 / 경기일보
</div>
</div>

<!-- 지역 뉴스 기사 4 -->
<div class="article-card">
<div class="badge">📰 행정/시민안전</div>
<h3>하남시, 8월 정기분 주민세 납부 기간 운영 &amp; 폭염 대응 실외 안전점검 강화</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 2026년 8월 정기분 주민세(개인분 및 사업소분) 납부 안내를 실시하며, 9월 2일까지 위택스 및 금융기관을 통해 납부할 수 있습니다. 한편 연일 이어지는 폭염에 대비해 야외 근로자 보호, 무더위 쉼터 점검 등 온열질환 예방 종합대책을 철저히 집행하고 있습니다.
</div>
<div class="source">
📌 출처: 하남시청 공지사항
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 TOP 3 (2026년 8월 24일 최신 기준)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 하남 관내 초·중학교 8월 24일 2학기 개학 시작… 스쿨존 안전점검 &amp; 학사 일정 정보 열기 (미사맘/감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 24일(월)부터 하남 관내 주요 초·중학교(미사, 감일, 위례, 덕풍 등)가 2학기 개학을 맞이했습니다.</div>
<div class="mom-point">💡 주민 포인트: 학교별 등하교 시간표 변경, 스쿨존 통학로 안전요원 배치 현황, 8월 넷째 주 급식표 및 2학기 준공·준비물 체크리스트 등 학부모 실생활 정보가 활발히 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "긴 여름방학이 드디어 끝나고 개학이네요!", "개학 첫날 통학로 스쿨존 안전지도 잘 체크해야겠어요" 등의 반응이 이어졌습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 위례복합체육센터 9월 1일 정식 개장… 수영장·'다함께돌봄센터' 사전 접수 열기 (위례맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 시범 운영을 마친 위례복합체육센터가 9월 1일 정식 개장을 앞두고, 8월 24일부터 수영강좌 및 초등 '다함께돌봄센터(33명 정원)' 사전 수강 신청을 개시했습니다.</div>
<div class="mom-point">💡 주민 포인트: 수강신청 오픈런 팁, 맞벌이 가정 다함께돌봄센터 증빙서류 제출 기준, 센터 내 공공형 키즈카페 이용 방법 등 위례맘 커뮤니티 최대 관심사로 부상했습니다.</div>
<div class="mom-reaction">💬 주민 반응: "위례 주민 숙원이었던 수영장이 드디어 정식 개장하네요!", "돌봄센터와 수영장 수강 신청 성공하길 기원합니다" 등 기대가 모였습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남시 소상공인 경영환경개선사업 최대 180만 원 지원 8월 31일 마감 임박 (덕풍맘/미사맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시와 경기테크노파크가 주관하는 '2026 소상공인 경영환경개선 지원사업(점포당 최대 180만 원 지원)' 접수가 8월 31일 마감을 앞두고 커뮤니티 내 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 관내 학원, 카페, 공방 등을 운영하는 자영업 학부모(맘사장님)들 사이에 간판 교체, 키오스크·POS 교체 모범 사례 및 견적서 제출 방법 등 실질적 정보가 전해졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "동네 상가 점포 리모델링이나 키오스크 지원받기 좋은 정보네요", "주변 자영업 하시는 분들 마감 전에 꼭 신청하시라고 알렸어요" 등의 반응이 전해졌습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=\s*</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈 TOP 3</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

content = re.sub(
    content
)

# Section 5: ALL IN 하남라이프 (2026년 8월 24일 자 기준 교체)
culture_events = """<div class="event-card">
<strong>[축제/버스킹] 2026 '스테이지 하남!(STAGE HANAM)' 8·9월 주말 도심 야외 버스킹</strong>
<p>일시: 2026.08.29(토) ~ 9월 말 매주 주말 저녁<br/>장소: 미사호수공원 수변무대, 미사문화거리, 감일·위례 거점 광장<br/>내용: 하남시와 하남문화재단이 주최하는 도심 거리 공연 프로젝트! K-POP, 인디 밴드, 퓨전 국악, 재즈 등 다채로운 퍼포먼스가 어우러져 늦여름과 가을밤을 수놓을 야외 버스킹 축제입니다. (전석 무료 관람)</p>
</div>
<div class="event-card">
<strong>[공연/기획] 하남문화예술회관 8·9월 기획공연 &lt;피아노 마라톤&gt; & &lt;가을밤 클래식 산책&gt;</strong>
<p>일시: 2026.08.29(토) 17:00 / 09.05(토) 19:00<br/>장소: 하남문화예술회관 대극장(아랑홀)<br/>내용: 대한민국 정상급 피아니스트 3인이 선사하는 릴레이 피아노 마라톤 공연(8.29)과 9월 가을맞이 챔버 오케스트라 클래식 콘서트(9.05)가 펼쳐집니다. 하남시민 할인 혜택 제공!</p>
</div>
<div class="event-card">
<strong>[스포츠/체험] 2026 서울올림픽기념 '88RUN' 하남 미사경정공원 마라톤 대회 사전 접수</strong>
<p>일시: 2026년 9월 12일(토) 오전 8시 (온라인 사전 선착순 접수 중)<br/>장소: 하남 미사경정공원 및 호수 산책로 일원<br/>내용: 시원한 미사경정공원 호숫가를 달리는 수도권 대표 가을 러닝 축제! 10km, 5km 및 온 가족이 함께 달리는 패밀리런 코스로 구성되며 사전 신청자에게 기념 품목이 제공됩니다.</p>
</div>
<div class="event-card">
<strong>[전시/가족] 하남문화예술회관 아트갤러리 기획전시 &lt;ATO : NOLJA - 도하야 놀자!&gt;</strong>
<p>기간: ~ 2026년 8월 30일(일)까지 (매주 월요일 휴관)<br/>장소: 하남문화예술회관 2층 아트갤러리<br/>내용: 함도하 작가의 해학적이고 친근한 가구 조형 아트퍼니처 작품전입니다. 주말 도슨트 작품 해설과 체험 프로그램이 운영되어 아이들과 온 가족이 무료로 관람하실 수 있습니다.</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?</div>\s*</div>',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">한눈에 보는 8·9월 하남시 문화·공연·전시 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>\n</div>',
    content
)

# Section 6: 공공기관 소식지 (2026년 8월 24일 자 기준 교체)
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.24</div>
<h3>[하남시청] 관내 자연녹지지역 토지거래허가구역 지정 &amp; '2026 청년 명랑 운동회' 모집</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국토교통부 지정에 따라 8월 18일부터 12월 31일까지 하남시 관내 24개 동 자연녹지지역 전역(70.14㎢)이 토지거래허가구역으로 신규 지정되었습니다. 한편 9월 19일 개최되는 청년의 날 기념 '2026 청년 명랑 운동회' 참가자(19~39세 청년 100명) 및 청년지원센터 '일잘러 실무클래스 5기' 수강생을 선착순 모집합니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 고시공고 및 보도자료
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시보건소·재난안전과 | 2026.08.24</div>
<h3>[하남시보건소] 2026년 하반기 민방위 보충교육 실시 &amp; 9월 시민 평생학습 참가 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 8월 31일부터 9월 5일까지 하남시청 대회의실에서 1~2년차 민방위 대원 대상 하반기 보충 1차 집합교육을 실시합니다(사이버교육은 9월 18일까지). 아울러 9월 공모형 시민주도 평생학습강좌 및 미사보건센터 맞춤형 건강증진 운동교실 참가자 모집을 진행 중입니다.
</div>
<div class="source">
📌 출처: 하남시보건소 및 하남시 평생교육과 공지
</div>
</div>

<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남소방서·하남시의회 | 2026.08.24</div>
<h3>[하남소방서·시의회] 2026 을지연습 비상대응 점검 완료 및 제351회 임시회 추경 의결</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남소방서와 하남시의회는 8월 21일 2026 을지연습 국가위기관리 및 긴급재난 대응 출동 훈련을 차질 없이 마무리했습니다. 또한 하남시의회는 제351회 임시회를 폐회하고 시민 생활과 밀접한 2026년도 제3회 추가경정예산안 등 주요 20개 안건 심의·의결을 완료했습니다.
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

# Write to kj_hanam_inside_20260824.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated kj_hanam_inside_20260824.html with Public Agency Notices as of 0824!")
