# -*- coding: utf-8 -*-
import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260917.html'
target_path = 'dashboard/news/kj_hanam_inside_20260918.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Issue Number, and Date
content = content.replace("42호 | 2026년 9월 17일 발행", "43호 | 2026년 9월 18일 발행")
content = content.replace("2026년 9월 17일 기준", "2026년 9월 18일 기준")
content = content.replace("images/thumbnail0917.jpg", "images/thumbnail0918.jpg")
content = content.replace("images/thumbnail-917.jpg", "images/thumbnail0918.jpg")
content = content.replace("images/thumb.jpg", "images/thumbnail0918.jpg")

# 2. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- 기사 1 (언론보도 - 기호일보: 이광재 국회의원 "평창올림픽 시설, 국가가 직접 관리·운영") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035071" target="_blank" style="color: inherit; text-decoration: none;">이광재 국회의원 "평창올림픽 시설, 국가가 직접 관리·운영"… '국민체육진흥법 개정안' 대표발의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
2018 평창 동계올림픽 시설의 사후 관리 책임을 지방자치단체가 떠안으며 발생한 누적 적자(약 410억 원) 해결을 위해 이광재(민주·하남갑) 국회의원이 나섰습니다. 이 의원은 올림픽 체육시설 관리·운영 주체를 서울올림픽기념국민체육진흥공단으로 확대해 국가 차원에서 책임지고 운영하도록 하는 '국민체육진흥법' 일부개정법률안을 대표발의했습니다. 이 의원은 서울올림픽공원처럼 평창·강릉·정선의 올림픽 유산 시설들도 국가 차원의 체계적인 운영 시스템으로 전환되어야 한다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035071" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (기호일보) →</a></div>
</div>
<div class="source">
📌 출처: 기호일보 (이홍재 기자)
</div>
</div>


<!-- 기사 2 (현장일지 - 네이버 블로그: 이광재, [800조 예산안 옆에 놓인 상자 하나]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224414956518" target="_blank" style="color: inherit; text-decoration: none;">국민 삶에 직결된 800조 예산 꼼꼼히 챙기며 우리동네 현장도 달려갑니다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
예산결산특별위원회 위원장으로서 내년도 820조 원 규모의 국가 예산안 심의에 임하는 이광재 의원의 현장일지입니다. 국민 삶에 직결된 예산 항목 하나하나를 꼼꼼히 살피고, 국가 발전과 하남시민을 위한 세밀한 예산 검토를 이어가겠습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/thumbnail-918.jpg" alt="국민 삶에 직결된 800조 예산 꼼꼼히 챙기며 우리동네 현장도 달려갑니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224414956518" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 3 (현장일지 - 유튜브 숏폼 영상: 적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
대한적십자사 봉사회 하남지구협의회와 함께한 2026년 추석맞이 사랑의 한가위 나눔 현장을 담은 숏폼 영상입니다. 정성 담긴 명절 나눔과 봉사자 분들의 따뜻한 마음을 영상으로 확인해보세요.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-shorts0918" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-shorts0918" poster="./images/thumbnail0918.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0918.mp4" type="video/mp4">
      <p style="color: #fff; text-align: center; padding: 20px;">브라우저가 동영상 재생을 지원하지 않습니다.</p>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/@lee_kwang_jae" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 유튜브 (이광재 TV / 광재일하남)
</div>
</div>
</div>"""

# Slice replace Section 1
idx_lawmaker = content.find('<div id="lawmaker">')
idx_local = content.find('<div id="local-news">')
content = content[:idx_lawmaker] + section1_content + '\n<hr/>\n' + content[idx_local:]

# 3. Section 2: 하남 지역 주요 뉴스
section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (뉴시스: 하남시 독감·코로나19 무료 예방접종) -->
<div class="article-card">
<div class="badge">📰 보건/복지</div>
<h3><a href="https://www.newsis.com/view/NISX20260917_0003794093" target="_blank" style="color: inherit; text-decoration: none;">하남시, 독감·코로나19 무료 예방접종… 21일부터 순차 시작 (60~64세 하남시민 무상 추가지원)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
하남시가 독감 및 코로나19 유행에 대비해 어린이와 임신부, 어르신 대상 무료 예방접종을 9월 21일부터 순차적으로 실시합니다. 정부 국가 지원 대상 외에도 하남시 지자체 자체 예산으로 60~64세 하남시민 및 취약계층 독감 백신 무상 접종 혜택이 추가 지원됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsis.com/view/NISX20260917_0003794093" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴시스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091802.jpg" alt="무료 예방접종 진행 일정" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 뉴시스 (이호진 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (연합뉴스: 제네시스 스타필드 하남서 레이싱 페스티벌) -->
<div class="article-card">
<div class="badge">📰 경제/문화</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260917038600003?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">제네시스, 24∼27일 스타필드 하남서 레이싱 페스티벌… 르망 24시간 하이퍼카 실물 공개</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
제네시스가 추석 연휴를 맞아 스타필드 하남에서 '제네시스 마그마 레이싱 라이브 페스티벌'을 개최합니다. 르망 24시간 경기를 완주한 하이퍼카를 국내 최초로 전시하며, 몰입감 높은 심레이싱 체험 존과 팝업스토어 등 쇼핑몰 방문객들을 위한 다양한 즐길 거리를 선보입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/AKR20260917038600003?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (김윤구 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (디스커버리뉴스: 하남 지주택 7곳 어디까지 왔나…소유권 확보율 0∼69% 격차) -->
<div class="article-card">
<div class="badge">📰 부동산/이슈</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1101969" target="_blank" style="color: inherit; text-decoration: none;">[기자수첩] 하남 지주택 7곳 어디까지 왔나… 소유권 확보율 0∼69% 격차</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남지역에서 추진 중인 지역주택조합(지주택) 7개 사업장의 진행 상황과 토지 소유권 확보율이 0%에서 69%까지 큰 격차를 보이는 것으로 나타났습니다. 일부 사업장은 토지사용권원을 80% 이상 확보했으나 실제 토지 소유권은 15%대에 불과해, 조합 가입자와 주민들의 '토지 확보율' 의미와 인허가 단계에 대한 상세한 확인이 당부됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1101969" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 지역 뉴스 기사 4 (국제뉴스: 강성삼 경기도의원, 영유아 교육·보육 통합지원 논의…정책토론회 개최) -->
<div class="article-card">
<div class="badge">📰 의정/복지</div>
<h3><a href="https://www.gukjenews.com/news/articleView.html?idxno=3695038" target="_blank" style="color: inherit; text-decoration: none;">강성삼 경기도의원, '유보통합 시대' 영유아 교육·보육 통합지원체계 구축 정책토론회 개최</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
강성삼 경기도의원이 오는 29일 하남시가족어울림센터 대회의실에서 '유보통합 시대, 경기도 영유아 교육·보육 통합지원체계 구축 방안 정책토론회'를 개최합니다. 전국 최대 교육·보육 수요를 가진 경기도의 통합 지원체계 마련을 위해 유치원·어린이집 관계자, 학부모, 전문가들이 한자리에 모여 현장 의견을 청취하고 정책 과제를 논의할 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.gukjenews.com/news/articleView.html?idxno=3695038" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (국제뉴스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091807.jpg" alt="유보통합 시대 경기도 영유아 교육·보육 통합지원체계 구축 방안 정책토론회 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 국제뉴스 (강정훈 기자)
</div>
</div>
</div>"""

# Slice replace Section 2
idx_local = content.find('<div id="local-news">')
idx_mom = content.find('<div id="mom-cafe">')
content = content[:idx_local] + section2_content + '\n<hr/>\n' + content[idx_mom:]

# 4. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->

<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 18일 기준 하남 지역 커뮤니티(맘카페)에서 화제성과 댓글이 가장 폭발했던 HOT 이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ "이번 주말 아이와 어디 가시나요?" 2026 하남이성산성문화제(9/19~20) 개막 소식에 맘카페 '기대 만발'</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 대표 가을축제인 '2026 하남이성산성문화제'가 9월 19일(토)~20일(일) 미사호수공원 잔디광장과 이성산성 일원에서 개최된다는 소식이 전해지면서, 아이와 함께할 주말 나들이 코스로 맘카페 게시판이 들썩이고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 큰별쌤 최태성 역사콘서트, 개막 주제공연, 어린이 랜덤플레이댄스, 다채로운 체험 부스 운영 등 전 세대 가족 참여 프로그램 풍성.</div>
<div class="mom-reaction">💬 주민 반응: "최태성 선생님 역사 콘서트 아이들이랑 꼭 들으러 가야겠어요!", "주말 미사호수공원 잔디광장 자리 잡기 치열하겠네요", "가족 주말 나들이로 딱입니다" 맘카페 추천 이어져.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ "우리 아이 등하굣길 한층 안전해진다!" 개학기 초등학교 통학로 불법주정차·유해환경 집중 단속 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시가 2학기 개학기를 맞아 관내 초등학교 주변 어린이보호구역(스쿨존) 내 불법주정차 단속을 강화하고, 통학로 유해 광고물 정비 및 룸카페·편의점 청소년 유해환경 집중 점검에 나섰다는 소식에 학부모 엄마들의 열띤 호응이 이어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 초등학교 어린이보호구역 통학로 안전 강화, 불법 주정차 단속 및 청소년 유해환경 집중 정비.</div>
<div class="mom-reaction">💬 주민 반응: "학교 앞 횡단보도 불법 주정차 때문에 늘 불안했는데 단속 강화되어 다행이에요!", "아이들 안심 통학로 조성을 적극 환영합니다" 맘카페 학부모 찬사.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "우리 동네 생활 사업 주민이 직접 뽑았다!" 13개 동 주민총회 성료… '어린이 플로깅 &amp; 미술대회' 확정 관심</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 13개 동에서 약 4,800여 명의 주민이 직접 투표에 참여한 2026년 동별 주민총회가 성공적으로 마무리되며, '망월천 어린이 플로깅', '나룰어린이 미술대회', '치매예방 웃음치료' 등 주민 생활 밀착형 2027년 사업들이 확정되어 맘카페에서 큰 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 13개 동 주민참여예산 직접 투표 결과 및 아이·가족 맞춤형 마을 사업 확정.</div>
<div class="mom-reaction">💬 주민 반응: "아이와 함께 손잡고 가서 투표했던 어린이 플로깅 사업이 선정되어 정말 기뻐요!", "우리 동네에 꼭 필요한 사업들이 잘 집행되면 좋겠네요" 맘카페 따뜻한 호응.</div>
</div>
</div>"""

# Slice replace Section 3
idx_mom = content.find('<div id="mom-cafe">')
idx_culture = content.find('<div id="culture">')
content = content[:idx_mom] + section3_content + '\n\n' + content[idx_culture:]

# 5. Section 4: ALL IN 하남라이프
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 18일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (하남시어린이영어도서관 시민 추천도서 의견수렴) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📚 ~2026.11.30 | 도서관/시민참여</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr" target="_blank" style="color: inherit; text-decoration: none;">하남시어린이영어도서관 시민 추천도서 의견수렴 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"여러분이 추천한 영어도서가 어린이영어도서관의 책이 됩니다!"</b><br/>
하남시어린이영어도서관에서 시민들이 원하는 영문 서적을 구입·비치하기 위해 의견수렴을 진행합니다.<br/><br/>
<b>👥 참여 대상:</b> 하남시민 누구나<br/>
<b>📅 진행 기간:</b> 2026년 9월 14일(월) ~ 11월 30일(월)<br/>
<b>📖 추천 분야:</b> 어린이 영어도서 (그림책, 챕터북 등)<br/>
<b>📱 참여 방법:</b> 안내 포스터 QR코드 스캔 후 온라인 작성
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">하남시립도서관 홈페이지 바로가기 →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091804.jpg" alt="시민 추천도서 의견수렴 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시어린이영어도서관
</div>
</div>

<!-- 문화 기사 2 (하남시위례도서관 10월 프로그램) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🍁 2026.10월 운영 | 도서관/문화강좌</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr" target="_blank" style="color: inherit; text-decoration: none;">하남시위례도서관 10월 독서문화 프로그램 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"가을의 풍요로움을 책과 함께! 10월 독서문화 프로그램"</b><br/>
하남시위례도서관에서 단풍 계절 10월을 맞이하여 풍성한 독서 토론 및 유아·어린이·성인 대상 문화 프로그램을 진행합니다.<br/><br/>
<b>📍 장소:</b> 하남시위례도서관 강당 및 문화교실<br/>
<b>📝 신청 방법:</b> 하남시립도서관 홈페이지 온라인 선착순 접수<br/>
<b>☎️ 문의:</b> 위례도서관 안내 desk
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (위례도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091805.jpg" alt="위례도서관 10월 프로그램" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시위례도서관
</div>
</div>

<!-- 문화 기사 3 (감일건강생활지원센터 임산부 요가교실 4기) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🧘‍♀️ 2026.09.22~09.27 접수 | 임산부/건강교실</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/health/index.do" target="_blank" style="color: inherit; text-decoration: none;">2026 감일건강생활지원센터 &lt;임산부 요가교실 4기&gt; 수강생 모집</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"다 함께 더 건강하게! 감일지구 임산부 맞춤형 건강 요가 강좌"</b><br/>
감일건강생활지원센터에서 임산부의 건강 관리와 순산을 돕기 위한 요가교실 4기 수강생을 모집합니다.<br/><br/>
<b>👥 교육 대상:</b> 15~36주 하남시 등록 임산부 12명<br/>
<b>📅 운영 일정:</b> 10월 7일(수), 10월 14일(수), 10월 21일(수) 10:00~11:00<br/>
<b>📍 운영 장소:</b> 감일건강생활지원센터 모자교육실<br/>
<b>📝 신청 기간:</b> 9월 22일(화) 09:00 ~ 9월 27일(일) 18:00 (QR코드 온라인 신청)<br/>
<b>☎️ 문의:</b> 감일건강생활지원센터 <a href="tel:031-5182-1588" style="color:#3182ce; font-weight:bold;">031-5182-1588</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/index.do" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 홈페이지 바로가기 →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091806.jpg" alt="감일건강생활지원센터 임산부 요가교실 4기" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 보건소 (감일건강생활지원센터)
</div>
</div>

</div>"""

# Slice replace Section 4
idx_culture = content.find('<div id="culture">')
idx_public = content.find('<div id="public-news">')
content = content[:idx_culture] + section4_content + '\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>\n\n' + content[idx_public:]

# 6. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 18일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1: 2026-2027절기 인플루엔자·코로나19 무료 예방접종 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💉 하남시보건소 | 2026.09.21~</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: inherit; text-decoration: none;">2026-2027절기 인플루엔자(독감)·코로나19 무료 예방접종 안내 (60~64세 하남시민 추가 지원)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시 보건소에서 환절기 건강 증진을 위해 2026-2027절기 독감 및 코로나19 무료 예방접종을 순차적으로 시행합니다.<br/><br/>
<b>👶 어린이·임신부:</b> 2026년 9월 21일(월)부터 접종 개시<br/>
<b>👵 어르신 (65세 이상):</b> 75세 이상(10/6~), 70~74세(10/12~), 65~69세(10/15~)<br/>
<b>🏥 하남시민 자체 추가 지원:</b> 60~64세, 50~59세 기초수급자/국가유공자, 15~59세 심한 장애인 (10/19부터 하남시 지정병원에서 무상 지원)<br/>
<b>📍 접종 장소:</b> 지정 위탁의료기관 (예방접종도우미 사이트 nip.kdca.go.kr 조회)
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고 및 위탁의료기관 조회 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091802.jpg" alt="2026-27년도 인플루엔자 무료 예방접종 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 보건소 (보건정책과)
</div>
</div>

<!-- 공공기관 소식 2: 2026년 녹색건축물 조성 지원사업 안내 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏡 하남시 도시전략과 | ~2026.09.30</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502750" target="_blank" style="color: inherit; text-decoration: none;">2026년 녹색건축물 조성 지원사업 공고 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시 관내 사용승인 15년 이상 경과된 소규모 노후 주택 단열 창호 교체 및 LED 조명 교체 비용의 50% 이내(최대 900만 원)를 지원하는 공모 신청 안내입니다.<br/><br/>
<b>📅 신청 기간:</b> 2026년 9월 14일(월) ~ 9월 30일(수)<br/>
<b>📋 신청 자격:</b> 하남시 전역 15년 경과 단독·다세대·상가주택 건물 소유자<br/>
<b>🏢 접수 장소:</b> 하남시청 도시전략과 방문 접수
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502750" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고 확인하기 (하남시청) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091803.jpg" alt="2026년 녹색건축물 조성 지원사업 공고" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 도시전략과
</div>
</div>

<!-- 공공기관 소식 3: 2026년도 하남시 농어민 기회소득 지원사업 2차 신청접수 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🌾 하남시 식품위생농업과 | 2026.09.21 ~ 10.23</div>
<h3><a href="https://farmbincome.gg.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026년도 하남시 농어민 기회소득 지원사업 2차 신청 접수 안내 (하남시 공고 제2026-1701호)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
하남시 관내 농어업인의 공익적 가치 보장 및 삶의 질 향상을 위한 '2026년도 농어민 기회소득 지원사업' 2차 신청을 접수합니다.<br/><br/>
<b>📅 신청 기간:</b> 2026년 9월 21일(월) ~ 10월 23일(금)<br/>
<b>🌾 지원 대상:</b> 하남시 주소지 및 농어업경영체 등록 농어민 (연속 1년 이상 거주·영농, 농외소득 3,700만 원 미만)<br/>
<b>💰 지원 내용:</b> 농어민 개인별 지역화폐 지급 (청년·환경·귀농어민 월 15만 원 / 일반농어민 월 5만 원, 하반기 30~90만 원 이내)<br/>
<b>💻 신청 방법:</b> 주소지 동 행정복지센터 방문 신청 또는 농어민 기회소득 통합지원시스템 온라인 신청 (farmbincome.gg.go.kr)<br/>
<b>💵 지급 시기:</b> 2026년 12월 중 (지급일로부터 180일 이내 사용)<br/>
<b>📞 문의처:</b> 하남시청 담당부서 (031-790-5769) 및 각 동 행정복지센터
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://farmbincome.gg.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">농어민 기회소득 통합지원시스템 바로가기 (경기도) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 (공고 제2026-1701호)
</div>
</div>

</div>"""

# Slice replace Section 5
idx_public = content.find('<div id="public-news">')
idx_footer = content.find('<!-- 하단')
content = content[:idx_public] + section5_content + '\n\n' + content[idx_footer:]

# 7. Update playNewsletterVideo JavaScript function
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video-shorts0918') || document.getElementById('video-A5H3SrB6qiE') || document.getElementById('video--X7EDD6ADSY') || document.getElementById('video-8BKrEO0X7I4');
    if (v) {
        v.scrollIntoView({ behavior: 'smooth', block: 'center' });
        if (v.paused) {
            var promise = v.play();
            if (promise !== undefined) {
                promise.catch(function(error) {
                    console.log("Autoplay blocked:", error);
                    v.muted = true;
                    v.play();
                });
            }
        } else {
            v.pause();
        }
    }
}"""

content = re.sub(r'function playNewsletterVideo\(\)\s*\{.*?\}', new_script, content, flags=re.DOTALL)

# Save target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {target_path}")

# Update news_index_path & root_index_path
with open(news_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {news_index_path}")

with open(root_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {root_index_path}")
