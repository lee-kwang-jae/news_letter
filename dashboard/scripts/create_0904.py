import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260903.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260904.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("<title>KJ's 하남 인사이드 - 2026년 9월 3일</title>", "<title>KJ's 하남 인사이드 - 2026년 9월 4일</title>")
content = content.replace("KJ's 하남 인사이드 - 2026년 9월 3일", "KJ's 하남 인사이드 - 2026년 9월 4일")
content = content.replace('32호 | 2026년 9월 3일 발행', '33호 | 2026년 9월 4일 발행')
content = content.replace('📅 발행일: 2026년 9월 3일', '📅 발행일: 2026년 9월 4일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 한국경제: 이광재 예결위원장 기술보증기금 특강 - 2026.09.03) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.hankyung.com/article/202609032444i" target="_blank" style="color: inherit; text-decoration: none;">[특강/경영] 이광재 예결위원장, 기술보증기금 부산 본점 특별강연..."메가프로젝트 시대, 기술금융으로 中企 성장 도약"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 부산 기술보증기금 본점에서 열린 '2026년 제2차 경영전략워크숍'에 참석해 '국민을 부자로 만드는 나라'를 주제로 특별강연을 진행했습니다. 이 위원장은 AI 주권 확보, 성장 사다리 복원, 기술가치평가 및 M&A·기술거래 활성화, 기술보호 등 대한민국이 세계적 벤처 강국으로 도약하기 위한 핵심 과제와 기술금융 지원 방안을 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hankyung.com/article/202609032444i" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (한국경제) →</a></div>
</div>
<div class="source">
📌 출처: 한국경제 (민지혜 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 경인일보: 동서울HVDC 건축허가 4자 협의체 - 2026.09.03) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kyeongin.com/article/1770169" target="_blank" style="color: inherit; text-decoration: none;">[행정/교통] 동서울HVDC 2차보완 미제출…이광재 의원 주도 4자 협의체 결과에 '건축 허가' 향방 달렸다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
한국전력공사가 동서울변전소 내 초고압 직류변환소(HVDC) 건축허가 2차 보완 제출기한을 넘겼으나, 이광재 국회의원이 주도하는 '4자 협의체(하남시·기후부·한전·주민대표)'가 해법 찾기에 착수함에 따라 하남시가 최종 결정을 2개월 유예하기로 했습니다. 4자 협의체 합의 도출 시 이르면 11월 착공이 가능해져 감일신도시 주민 수용성 강화와 지역 갈등 봉합의 핵심 분수령이 될 전망입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kyeongin.com/article/1770169" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경인일보) →</a></div>
</div>
<div class="source">
📌 출처: 경인일보 (문성호 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 부산 기술보증기금 특강 & 부산 기술거래소 제안) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224400005768" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "기술이 돈이 되는 도시, 부산" 기술보증기금 특강 및 부산 기술거래소 제안</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 의원이 부산 기술보증기금을 찾아 중소·벤처기업과 기술 혁신 미래에 대한 특강을 진행했습니다. 좋은 기술을 보유한 벤처기업이 제값을 받고 평가받을 수 있도록 기보의 기술평가 역량과 부산의 금융 인프라를 결합한 '부산 기술거래소' 설립을 제안하고, 전재수 부산시장과 면담하여 부산의 미래 성장동력 확보 및 M&A, 벤처투자 활성화 방안을 논의했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224400005768" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0904_kj_01.jpg" alt="부산 기술보증기금 특강 현장" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 뉴:홈 전용 모기지 원복 감사패 수상) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224399852945" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "뉴:홈 청약자 여러분, 고생 많으셨습니다" 전용 모기지 원복 성과 감사패 수상</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 국회의원이 '뉴:홈 나눔형·선택형 전용모기지 원복 비상대책위원회'로부터 원안 적용을 위한 의정활동 공로를 인정받아 감사패를 받았습니다. 이 의원은 정부 정책 변경으로 인한 분양가·이자 부담 가중으로 고통받던 8,018세대 청약자들을 위해 국토교통부와 지속적인 협의 및 설득 과정을 거쳐 전용 모기지 원안 적용을 이끌어냈습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224399852945" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0904_kj_02.jpg" alt="뉴홈 모기지 원복 감사패 전달식" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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

# Section 2: 하남 지역 주요 뉴스 (9월 3일~4일 최신 지정 기사 4개 반영)
local_news_articles = """<!-- 지역 뉴스 기사 1 (의정/주거 - 디스커버리뉴스: 최승태 시의원 뉴홈 모기지 감사패) -->
<div class="article-card">
<div class="badge">📰 의정/주거</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100474" target="_blank" style="color: inherit; text-decoration: none;">최승태 하남시의원, 뉴홈 전용모기지 갈등 해결 기여 감사패 수상</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
정부의 뉴홈 전용모기지 정책 변경으로 8,018세대 청약자들의 주거·자금 조달 계획 차질 갈등이 국토교통부의 원안 이행 결정으로 타결된 가운데, 하남시의회 최승태 의원(의회운영위원장)이 주민 목소리를 정부와 정치권에 적극 전하고 문제 해결에 기여한 공로로 감사패를 받았습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1100474" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (사회/복지 - 머니투데이: 지호한방삼계탕 하남시미사노인복지관 삼계탕 후원) -->
<div class="article-card">
<div class="badge">📰 사회/복지</div>
<h3><a href="https://www.mt.co.kr/industry/2026/09/03/2026090310015520557" target="_blank" style="color: inherit; text-decoration: none;">지호한방삼계탕, 하남시미사노인복지관에 삼계탕 140인분 후원 물품 전달</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국내 삼계탕 대표 브랜드 지호한방삼계탕이 폭염에 취약한 지역 어르신들의 건강한 여름나기를 돕기 위해 하남시미사노인복지관을 찾아 삼계탕 140인분(약 270만 원 상당)을 기부하고 마음을 전달했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.mt.co.kr/industry/2026/09/03/2026090310015520557" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (머니투데이) →</a></div>
</div>
<div class="source">
📌 출처: 머니투데이 (김재련 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (보건/복지 - 위클리오늘: 하남시 실버벨 선생님 양성) -->
<div class="article-card">
<div class="badge">📰 보건/복지</div>
<h3><a href="https://www.weeklytoday.com/news/articleView.html?idxno=792915" target="_blank" style="color: inherit; text-decoration: none;">하남시, 어르신 치매 예방 돕는 ‘실버벨 선생님’ 양성교육 진행</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시(시장 이현재)가 미사보건센터 대강당에서 관내 요양기관 및 유관기관 종사자들을 대상으로 '실버벨 선생님 양성교육'을 실시했습니다. 종사자들에게 치매 기본 지식과 인지재활 교구 활용법을 교육하여 어르신 맞춤형 인지재활 프로그램을 적극 운영할 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.weeklytoday.com/news/articleView.html?idxno=792915" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (위클리오늘) →</a></div>
</div>
<div class="source">
📌 출처: 위클리오늘 (박종국 기자)
</div>
</div>

<!-- 지역 뉴스 기사 4 (사회/동물보호 - 시사오늘: 재개발 길고양이 특별법 청원 5만 돌파) -->
<div class="article-card">
<div class="badge">📰 사회/동물보호</div>
<h3><a href="https://www.sisaon.co.kr/news/articleView.html?idxno=204087" target="_blank" style="color: inherit; text-decoration: none;">재개발·재건축 길고양이 특별법 국회 국민동의청원 5만 명 돌파…상임위 심사 착수</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
재개발·재건축 지역의 길고양이 구조와 안전 이소를 의무화하는 특별법 제정 촉구 국회 국민동의청원이 5만 6,000여 명의 동의를 얻어 청원 성립 요건을 충족하고 국회 소관 상임위원회 심사 절차에 본격 들어갔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.sisaon.co.kr/news/articleView.html?idxno=204087" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시사오늘) →</a></div>
</div>
<div class="source">
📌 출처: 시사오늘 (윤진석 기자)
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈 (조회수/댓글 수치 제거, 2건 유지)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 하남드림 광역환승센터 ‘제4차 광역교통 기본계획’ 전격 반영 소식에 미사·감일·위례 맘카페 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 핵심 사업인 '하남드림 광역환승센터' 구축안이 국토교통부 대도시권광역교통위원회의 '제4차 환승센터 및 복합환승센터 구축 기본계획(2026~2030)'에 최종 포함·발표(8월 31일)되면서 지역 커뮤니티의 최대 화제로 부상했습니다.</div>
<div class="mom-point">💡 주민 포인트: 서울 도심 접근성 획기적 개선, 환승센터 연계 광역버스 노선 확충 및 GTX-D·지하철 연계 가능성 꿀팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "드디어 광역환승센터가 국가 계획에 반영됐네요! 서울 출퇴근길 확 달라질듯", "GTX-D 연계까지 속도 냈으면 좋겠습니다" 등 환영 반응 잇따름.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 9월 1일 오픈! 경기도 3분기 청년기본소득 및 하남시 '아빠 육아휴직 장려금(월 30만 원)' 신청 안내 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 1일부터 시작된 2026년 3분기 청년기본소득(24세 청년 분기별 25만 원 하남지역화폐)과 하남시 특화 사업인 '아빠 육아휴직 장려금'(월 30만 원씩 최대 6개월, 총 180만 원) 지원 자격과 신청 팁 공유 글이 맘카페에 연이어 게재되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 잡아바 어플라이 자동신청 동의 확인, 하남시 1년 이상 거주 조건, 고용보험 육아휴직급여 수령 증빙 서류 작성 팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "남편 육아휴직 장려금 덕분에 생활비 부담 덜었어요!", "2001~2002년생 자녀 있는 집 청년기본소득 잊지 마세요" 등 추천 반응 활발.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 5: 공공기관 소식지 (2026년 9월 4일 최신 고시/공고 교체)
public_agency_news = """<!-- 기사 1 (하남시청 - 숏폼 공모전) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.03</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 2026년 하남시 SNS 숏폼 영상 공모전 『하남 30초 프로젝트 - 내가 담은 하남』 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접수기간:</b> 2026.9.7.(월) ~ 10.8.(목) | <b>응모자격:</b> 하남시민 및 하남시에 관심 있는 누구나<br/>
<b>주요내용:</b> 하남시의 매력, 정책, 일상을 담은 30초~60초 숏폼 영상 공모 (총상금 200만 원, 4팀 선정).<br/>
<b>문의:</b> 하남시청 홍보담당관
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 홍보담당관
</div>
</div>

<!-- 기사 2 (하남시청 - 주민자치센터 수강생 모집) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.03</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 2026년 4분기 신장1동·위례동·미사동 주민자치센터 교양·문화 강좌 수강생 모집</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접수기간:</b> 2026.9.10.(목) ~ 9.14.(월) | <b>추첨일:</b> 2026.9.15.(화)<br/>
<b>주요내용:</b> 4분기 교양·문화·체육·외국어 강좌 수강생 모집 (인터넷 및 방문 접수).<br/>
<b>문의:</b> 각 동 주민자치센터
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 각 동 주민자치센터
</div>
</div>

<!-- 기사 3 (하남시청 - 농산물 공급지원사업) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.03</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 2026년 농산물 안정적 공급지원사업 추가모집 공고 (9.3~9.15)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>신청기간:</b> 2026.9.3.(목) ~ 9.15.(화) | <b>대상:</b> 관내 농업인 및 생산자 단체<br/>
<b>주요내용:</b> 친환경 농산물 생산·유통 기반 구축을 위한 농자재 및 생산 시설 보조 지원.<br/>
<b>문의:</b> 하남시청 식품위생농업과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 식품위생농업과
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Update Bottom Nav link to include 0903.html and set active 0904
bottom_nav_old = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260903.html" class="active">32호 (09/03)</a> | \n<a href="kj_hanam_inside_20260902.html">31호 (09/02)</a> | \n<a href="kj_hanam_inside_20260901.html">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> | \n<a href="kj_hanam_inside_20260828.html">28호 (08/28)</a> |'
bottom_nav_new = '<div class="bottom-nav">\n<a href="index.html">🏠 최신호 보기</a> | \n<a href="kj_hanam_inside_20260904.html" class="active">33호 (09/04)</a> | \n<a href="kj_hanam_inside_20260903.html">32호 (09/03)</a> | \n<a href="kj_hanam_inside_20260902.html">31호 (09/02)</a> | \n<a href="kj_hanam_inside_20260901.html">30호 (09/01)</a> | \n<a href="kj_hanam_inside_20260831.html">29호 (08/31)</a> |'

content = content.replace(bottom_nav_old, bottom_nav_new)

# Clean up any duplicated lines if needed
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260904.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated {target_path} and updated {index_path} with new public agency announcements!")
