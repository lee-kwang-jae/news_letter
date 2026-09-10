import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260907.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260908.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("<title>KJ's 하남 인사이드 - 2026년 9월 7일</title>", "<title>KJ's 하남 인사이드 - 2026년 9월 8일</title>")
content = content.replace("KJ's 하남 인사이드 - 2026년 9월 7일", "KJ's 하남 인사이드 - 2026년 9월 8일")
content = content.replace("KJ's 하남 인사이드 34호 (2026.09.07)", "KJ's 하남 인사이드 35호 (2026.09.08)")
content = content.replace('34호 | 2026년 9월 7일 발행', '35호 | 2026년 9월 8일 발행')
content = content.replace('📅 발행일: 2026년 9월 7일', '📅 발행일: 2026년 9월 8일')
content = content.replace('2026년 9월 7일 기준', '2026년 9월 8일 기준')
content = content.replace('하남·감일·위례 소통 소식지', 'Lee Kwang-jae Newsletter')

# Open Graph Meta Tags (대표 이미지 설정: 이광재 현장일지 첫 사진 https://lee-kwang-jae.github.io/news_letter/images/0907_kj_01.jpg)
og_meta_tags = """<meta property="og:type" content="website"/>
<meta property="og:url" content="https://lee-kwang-jae.github.io/news_letter/"/>
<meta property="og:title" content="KJ's 하남 인사이드 - 2026년 9월 8일"/>
<meta property="og:description" content="이광재 국회의원 의정활동, 하남 지역 주요 뉴스, 하남 맘카페 HOT 이슈, ALL IN 하남라이프 &amp; 공공기관 소식지"/>
<meta property="og:image" content="https://lee-kwang-jae.github.io/news_letter/images/0907_kj_01.jpg"/>
<meta property="twitter:card" content="summary_large_image"/>
<meta property="twitter:title" content="KJ's 하남 인사이드 - 2026년 9월 8일"/>
<meta property="twitter:description" content="이광재 국회의원 의정활동, 하남 지역 주요 뉴스, 하남 맘카페 HOT 이슈, ALL IN 하남라이프 &amp; 공공기관 소식지"/>
<meta property="twitter:image" content="https://lee-kwang-jae.github.io/news_letter/images/0907_kj_01.jpg"/>
<link rel="image_src" href="https://lee-kwang-jae.github.io/news_letter/images/0907_kj_01.jpg"/>"""

if '<meta property="og:image"' in content:
    content = re.sub(r'<meta property="og:type".*?<link rel="image_src".*?>\n?', '', content, flags=re.DOTALL)

content = content.replace('</title>', '</title>\n' + og_meta_tags)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - MBC: 이광재 "세종·대전은 워싱턴, 서울은 뉴욕... 지방 이전 성공하려면 교육에 파격적 대우 필요" - 2026.09.04) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://n.news.naver.com/mnews/article/214/0001522031?sid=100" target="_blank" style="color: inherit; text-decoration: none;">[정치/행정] 이광재 "세종·대전은 워싱턴, 서울은 뉴욕... 지방 이전 성공하려면 교육에 파격적 대우 필요"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원장을 맡고 있는 이광재 더불어민주당 의원이 MBC 라디오 '김종배의 시선집중'에 출연해 정부의 공공기관 지방 이전 방안과 관련해 "대통령실과 국회가 세종으로 이전하면서 행정수도가 사실상 완성된다"며 "세종시와 대전은 워싱턴, 서울은 뉴욕과 같은 도시로 발전할 것"이라고 강조했습니다. 이 의원은 공공기관 지방 이전의 성공을 위해 교육 환경의 파격적 지원과 AI 정부 및 교육 산업 육성을 통한 자족도시 조성을 핵심 과제로 제시했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://n.news.naver.com/mnews/article/214/0001522031?sid=100" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (MBC 뉴스) →</a></div>
</div>
<div class="source">
📌 출처: MBC (김종배의 시선집중)
</div>
</div>

<!-- 기사 2 (언론보도 - 연합뉴스: '대미 투자 협상' 관련 당정 입장하는 이광재 예결위원장 - 2026.09.07) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.yna.co.kr/view/PYH20260907094200013?input=1196m" target="_blank" style="color: inherit; text-decoration: none;">[의정/경제] '대미 투자 협상' 관련 당정협의회 참석하는 이광재 예결위원장</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 국회 의원회관에서 열린 '대미 투자 협상' 관련 당정협의회에 참석해 재정경제기획위원회, 산업통상자원중소벤처기업위원회, 외교통일위원회 등 관련 상임위 위원장 및 간사들과 함께 대미 투자 협상 대응 방안 및 국비·재정 지원 전략을 논의했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/PYH20260907094200013?input=1196m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (이동해 기자)
</div>
</div>

<!-- 기사 3 (현장일지 - 네이버 블로그: [주간 이광재] 9월 첫째 주 의정보고서) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224403391851" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "표적 감사 방지법 대표발의 & 메가성장특위 본격 활동" [주간 이광재] 9월 첫째 주 의정보고서</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 의원이 9월 첫째 주 의정보고서를 통해 표적 정책감사를 방지하는 &lt;감사원법 개정안&gt; 대표발의 소식을 전하고, 세종·충남 예산정책협의회 참석 및 민주당 메가성장특별위원회 수석부위원장 활동 등 한 주간의 의정활동 성과를 하남 시민들에게 상세히 보고했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224403391851" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0907_kj_01.jpg" alt="9월 첫째 주 의정보고서" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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

# Section 2: 하남 지역 주요 뉴스 (요청받은 기사 추가)
local_news_articles = """<!-- 지역 뉴스 기사 1 (이투데이 - 스타필드 하남 10주년) -->
<div class="article-card">
<div class="badge">📰 쇼핑/생활</div>
<h3><a href="https://www.etoday.co.kr/news/view/2622429" target="_blank" style="color: inherit; text-decoration: none;">10주년 맞은 스타필드 하남…펫 축제·최현우 마술쇼 열린다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
스타필드 하남이 개장 10주년을 기념해 오는 9월 12일부터 반려동물과 함께 즐기는 '펫블리타운' 축제를 비롯해 세계적인 마술사 최현우의 특별 마술쇼, 900여 종의 인기 피규어를 선보이는 대규모 팝업스토어 등 시민과 방문객을 위한 다채로운 문화·체험 행사를 개최합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.etoday.co.kr/news/view/2622429" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (이투데이) →</a></div>
</div>
<div class="source">
📌 출처: 이투데이 (김재은 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (데일리한국 - 하남시의회 QR코드 민원 접수) -->
<div class="article-card">
<div class="badge">📰 의정/행정</div>
<h3><a href="https://daily.hankooki.com/news/articleView.html?idxno=1403544" target="_blank" style="color: inherit; text-decoration: none;">하남시의회, QR코드 활용 '주민생활불편 민원 접수'</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회가 관내 주요 지점 18곳에 QR코드가 수록된 현수막을 설치하고 스마트폰으로 간편하게 접속해 교통, 복지, 환경 등 생활 속 불편 민원과 지역 발전 아이디어를 제출할 수 있는 디지털 주민 소통 창구를 구축했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://daily.hankooki.com/news/articleView.html?idxno=1403544" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (데일리한국) →</a></div>
</div>
<div class="source">
📌 출처: 데일리한국 (이성환 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (뉴시스 - 하남 중학교 과밀학급 포화) -->
<div class="article-card">
<div class="badge">📰 교육/사회</div>
<h3><a href="https://www.newsis.com/view/NISX20260907_0003779374" target="_blank" style="color: inherit; text-decoration: none;">하남시 중학교 교실 70%가 '과밀학급'…10개 반 중 7개 반 심각한 포화</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 교육위원회 고민정 의원실이 공개한 '2026년 과밀학급 현황'에 따르면, 경기 하남시 중학교 과밀학급(학급당 학생 수 28명 이상) 비율이 70.03%(243학급)에 달해 10개 학급 중 7개 반 이상이 과밀 포화 상태인 것으로 나타났습니다. 이는 수도권 지자체 중에서도 최상위권 수준으로, 지역 교육 환경 개선을 위한 과밀학급 해소 대책 촉구가 이어지고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsis.com/view/NISX20260907_0003779374" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴시스) →</a></div>
</div>
<div class="source">
📌 출처: 뉴시스 (정예빈 기자)
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 6: 하남 맘카페 HOT 이슈 (2026.09.08 최신 3건 전면 교체)
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 9월 12일 개막! 스타필드 하남 10주년 '하이텐션 페스티벌'… 펫 걷기대회·최현우 마술쇼·피규어 팝업 소식에 맘카페 열기 후끈</h4>
<div class="mom-detail"><strong>현황:</strong> 개장 10주년을 맞은 스타필드 하남이 오는 9월 12일부터 반려견 500팀 참여 '펫블리타운', 최현우 특별 마술쇼, 포켓몬·마블 900여 종 캐릭터 피규어 팝업스토어 등 대규모 축제를 연다는 소식에 미사·감일·위례 맘카페 문의글이 집중되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 설채현 수의사 펫 토크쇼 및 펫 운동회 사전 예약 꿀팁, 아이들과 함께 가볼 만한 캐릭터 팝업 일정 및 주차 정보 공유.</div>
<div class="mom-reaction">💬 주민 반응: "주말에 아이들과 최현우 마술쇼 보러 꼭 가야겠어요!", "반려견 걷기대회 마감 전 접수 성공했습니다" 등 기대감 폭발.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 국회 발표! 하남시 중학교 10개 반 중 7개 반(70.03%) '과밀학급' 포화 소식에 맘카페 중학 배정·교실환경 걱정 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 국회 교육위원회 발표 결과 하남시 중학교 과밀학급(학급당 28명 이상) 비율이 70.03%(243학급)로 수도권 최상위 포화 상태임이 밝혀지면서, 미사·감일·위례 등 신도시 맘카페에서 교실 환경 및 신설교 개교 촉구 게시글이 쇄도했습니다.</div>
<div class="mom-point">💡 주민 포인트: 2027학년도 중학교 단지별 지망 배정 전략, 모듈러 교실 및 학교 증축 현황 정보 공유.</div>
<div class="mom-reaction">💬 주민 반응: "학급당 30명 가까이 수업받는 아이들 걱정이 컸는데 현실로 확인됐네요", "교육청과 지자체의 적극적인 과밀 해소 대책이 시급합니다" 반응 거세.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "스마트폰 카메라만 대면 1분 만에 접수!" 하남시의회 시내 18곳 'QR코드 현수막' 민원 창구 개설에 맘카페 제안 인증 속출</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시의회가 시내 주요 지점 18곳에 QR코드가 수록된 현수막을 걸고 스마트폰 간편 민원 및 정책 아이디어 접수를 개시하자, 등하굣길 안전시설 및 보도블록 개선 제안 인증글이 맘카페에 속속 게재되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 복잡한 검색 없이 QR코드 스캔으로 유모차 보행 불편 및 교통·복지·환경 아이디어 즉시 접수 팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 통학로 횡단보도 위험했던 구간 바로 민원 작성했어요!", "앱 설치 없이 바로 연결되어 유모차 끄는 맘들에겐 정말 편리하네요" 호평.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">.*?</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 8일 기준 하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 5: Add ALL IN 하남라이프 culture articles
culture_articles = """<!-- 문화 기사 1 (생활문화센터 미사 마주침갤러리 세 번째 전시 「모녀 이음전」) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎨 2026.09.07 ~ 09.18 | 전시/갤러리</div>
<h3><a href="https://www.hnart.or.kr/space/selectBbsNttView.do?key=422&bbsNo=68&nttNo=7056&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">[전시/갤러리] 생활문화센터 미사 마주침갤러리 세 번째 전시 「모녀 이음전」 (9월 7일~18일)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"모녀의 따뜻한 감성과 예술적 교감을 담은 특별한 전시!"</b><br/>
생활문화센터 미사 마주침갤러리(마주침공간)에서 정지혜, 이옥자 작가의 세 번째 기획 전시 「모녀 이음전」이 개최됩니다. 관내 주민과 방문객 누구나 자유롭게 무료로 관람하실 수 있습니다.<br/><br/>
<b>📅 전시기간:</b> 2026년 9월 7일(월) ~ 9월 18일(금)<br/>
<b>📍 장소:</b> 생활문화센터 미사 마주침갤러리 (마주침공간)<br/>
<b>🎨 작가:</b> 모녀 이음전 (정지혜, 이옥자)<br/>
<b>⏰ 관람시간:</b> 월요일 ~ 금요일 오전 9시 ~ 오후 6시 (무료 관람)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hnart.or.kr/space/selectBbsNttView.do?key=422&bbsNo=68&nttNo=7056&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">전시 공지 상세보기 (하남문화재단 생활문화센터) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0908_kj_03.jpg" alt="생활문화센터 미사 마주침갤러리 모녀 이음전 포스터" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남문화재단 (생활문화센터 미사)
</div>
</div>

<!-- 문화 기사 2 (하남역사박물관 9월 문화가 있는 날 궁중지화 모란 꽃 만들기) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎨 2026.09.09 | 체험/가족</div>
<h3><a href="https://www.hnart.or.kr/museum/edctevntView.do?key=347&programId=museum&edctEvntNo=503" target="_blank" style="color: inherit; text-decoration: none;">[체험/가족] 하남역사박물관 9월 문화가 있는 날 『궁중지화_모란 꽃 만들기』 수강생 모집</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"전통 한지로 피워내는 아름다운 왕실의 꽃, 모란!"</b><br/>
하남역사박물관 소장품 연계 체험 교육 프로그램으로 전통 한지를 활용해 왕실의 꽃 '모란'을 만들어보는 궁중지화 체험을 진행합니다.<br/><br/>
<b>📅 일시:</b> 2026년 9월 9일(수) 16:00 ~ 18:00<br/>
<b>📍 장소:</b> 하남역사박물관 교육실<br/>
<b>👧 모집대상:</b> 성인, 가족 (아동 1명 + 보호자 1명) / 선착순 20팀 (수강료 팀당 15,000원)<br/>
<b>📝 신청방법:</b> 하남역사박물관 홈페이지 온라인 선착순 접수 (9월 1일~8일)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hnart.or.kr/museum/edctevntView.do?key=347&programId=museum&edctEvntNo=503" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">교육 신청 상세보기 (하남역사박물관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0907_kj_04.jpg" alt="하남역사박물관 궁중지화 모란 꽃 만들기 포스터" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남문화재단 (하남역사박물관)
</div>
</div>

<!-- 문화 기사 3 (하남시청소년수련관 청소년관장 공약사업 청소년멘토 원데이클래스) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎉 2026.09.12 | 교육/체험</div>
<h3><a href="https://www.hnyouth.kr/sub/program/apply/134" target="_blank" style="color: inherit; text-decoration: none;">[교육/체험] 하남시청소년수련관 청소년관장 공약사업 『청소년멘토 원데이클래스』 참가자 모집</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"고등학생·후기청소년 멘토와 함께하는 유니티 코딩 & 추석 쿠키 베이킹!"</b><br/>
하남시 9세~15세 청소년을 위해 특별히 마련된 원데이클래스! 직접 게임을 제작하는 '게임 코딩' 클래스와 마들렌·추석 쿠키를 만드는 '베이킹' 클래스가 진행됩니다.<br/><br/>
<b>📅 일시:</b> 2026년 9월 12일(토) (코딩: 10:00~12:30 / 베이킹: 1회차 10:00, 2회차 12:00)<br/>
<b>📍 장소:</b> 하남시청소년수련관 (2층 스포츠실 & 3층 쿠킹스튜디오)<br/>
<b>👧 모집대상:</b> 하남시 관내 9세~15세 청소년 (선착순 모집 / 참가비 무료)<br/>
<b>📝 신청방법:</b> 온라인 신청폼 작성 (https://moaform.com/q/pwjiwg)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hnyouth.kr/sub/program/apply/134" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">프로그램 상세 안내 (하남시청소년수련관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0908_kj_04.jpg" alt="하남시청소년수련관 청소년멘토 원데이클래스 포스터" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청소년수련관 (청소년활동팀)
</div>
</div>

<!-- 문화 기사 4 (하남시 가족센터 세계 한 바퀴! 다문화 체험 여행) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🌍 2026.09.12 | 체험/다문화</div>
<h3><a href="https://hanam.familynet.or.kr/" target="_blank" style="color: inherit; text-decoration: none;">[체험/다문화] 하남시 가족센터 『세계 한 바퀴! 다문화 체험 여행』 (9월 12일)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"온 가족이 함께 즐기는 다채로운 다문화 문화·체험 여행!"</b><br/>
하남시 가족센터에서 지역주민 400명을 대상으로 다문화 문화 체험 및 오프라인 행사인 『세계 한 바퀴! 다문화 체험 여행』을 개최합니다.<br/><br/>
<b>📅 행사일시:</b> 2026년 9월 12일(토)<br/>
<b>📝 접수기간:</b> 2026년 9월 12일(토) 10:00 ~ 15:00 (현장 오프라인 접수 / 정원 400명)<br/>
<b>📍 진행장소:</b> 경기 하남시 아리수로 565 (하남시미사강변종합사회복지관 주변)<br/>
<b>👧 참여대상:</b> 하남시 지역주민 (참가비 무료)<br/>
<b>📞 진행문의:</b> 070-4128-3394
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://hanam.familynet.or.kr/" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">프로그램 상세보기 (하남시 가족센터) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0908_kj_02.png" alt="세계 한 바퀴! 다문화 체험 여행" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 가족센터
</div>
</div>
"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 8일 기준 한눈에 보는 하남시 최신 문화·공연·체험 가이드</p>\n\n' + culture_articles + '\n',
    content
)

# Section 3: 공공기관 소식지 (2026.09.08 최신 공공기관 소식으로 전면 교체)
public_agency_news = """<!-- 기사 1 (하남시청 - K-스타월드 도시개발사업 민간참여자 공모) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.04 ~ 12.31</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] (가칭) K-컬처 복합 콤플렉스(K-스타월드) 도시개발사업 민간참여자 공모 정정 공고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>공모기간:</b> 2026.9.4.(금) ~ 12.31.(목) | <b>대상:</b> 민간 투자 컨소시엄 및 관련 기업<br/>
<b>주요내용:</b> 미사섬 일대 K-컬처 복합 콤플렉스(K-스타월드) 조성을 위한 대규모 도시개발사업 민간참여자 공모 진행.<br/>
<b>문의:</b> 하남시청 도시개발과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 도시개발과
</div>
</div>

<!-- 기사 2 (하남시립도서관 - 9월 독서의 달 108개 독서문화 행사) -->
<div class="article-card">
<div class="badge">🏛️ 하남시립도서관 | 2026.09.01 ~ 09.30</div>
<h3><a href="https://www.hanamlib.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시립도서관] 9월 '독서의 달' 맞이 9개 공공도서관 108개 독서문화 프로그램 및 '연체지우개' 이벤트</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>행사기간:</b> 2026.9.1.(화) ~ 9.30.(수) | <b>대상:</b> 하남시민 누구나<br/>
<b>주요내용:</b> 미사·나룰·위례·감일 등 9개 도서관 작가 초청 강연, AI 디지털 교육, 공연 및 9월 14일~20일 '연체지우개(대출 제한 해제)' 특별 운영.<br/>
<b>문의:</b> 하남시립도서관 미사도서관팀 / 도서관운영과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">프로그램 종합 안내 (하남시립도서관) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 도서관운영과
</div>
</div>

<!-- 기사 3 (하남시 보건소 - 인플루엔자 예방접종 및 건강증진사업) -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.09.08</div>
<h3><a href="https://www.hanam.go.kr/health/index.do" target="_blank" style="color: inherit; text-decoration: none;">[하남시 보건소] 2026년 가을·겨울철 대비 인플루엔자(독감) 국가 예방접종 및 시민 건강관리</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>접수/시행:</b> 2026.9월 중 순차 접종 시작 | <b>대상:</b> 하남시민 (어린이, 어르신, 임신부 및 취약계층 등 우선 지원)<br/>
<b>주요내용:</b> 독감 국가예방접종 사업 및 가을철 감염병 예방관리를 위한 보건소 전문 상담 및 간호지원 체계 가동.<br/>
<b>문의:</b> 하남시 보건소 감염병관리과 / 예방접종실
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/index.do" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">접종 안내 상세보기 (하남시 보건소) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 보건소 감염병관리과
</div>
</div>

<!-- 기사 4 (하남시청 - 감일·위례 스마트쉘터 버스정류장 CCTV 설치 행정예고) -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09.07 ~ 09.28</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[하남시청] 감일·위례 신도시 스마트쉘터 버스정류장 내부 방범 CCTV 설치 행정예고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>예고기간:</b> 2026.9.7.(월) ~ 9.28.(월) | <b>대상:</b> 감일·위례 신도시 스마트쉘터 버스정류장 이용자<br/>
<b>주요내용:</b> 대중교통 이용 시민 안전 및 범죄 예방을 위한 버스쉘터 내부 고화질 CCTV 설치 행정예고 및 의견 수렴.<br/>
<b>문의:</b> 하남시청 교통정책과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">행정예고문 확인하기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 교통정책과
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Clean up any duplicated newlines
content = re.sub(r'\n{3,}', '\n\n', content)

# Write target file kj_hanam_inside_20260908.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated {target_path} and {index_path} with new Public Agency News for 2026-09-08!")


