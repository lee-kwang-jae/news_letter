# -*- coding: utf-8 -*-
import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260916.html'
target_path = 'dashboard/news/kj_hanam_inside_20260917.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Issue Number, and Date
content = content.replace("41호 | 2026년 9월 16일 발행", "42호 | 2026년 9월 17일 발행")
content = content.replace("2026년 9월 16일 기준", "2026년 9월 17일 기준")
content = content.replace("images/thumbnail0916.jpg", "images/thumbnail0917.jpg")
content = content.replace("images/thumb.jpg", "images/thumbnail0917.jpg")

# 2. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer;">
    <span>우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- 기사 1 (언론보도 - 시대일보: [시대리포트]'노무현의 남자' 이광재 "지방이전, 박정희때 포철처럼") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.sidae.com/article/2026091515273636450" target="_blank" style="color: inherit; text-decoration: none;">[시대리포트]'노무현의 남자' 이광재 "지방이전, 박정희때 포철처럼"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
1988년 23세 청년 시절 노무현 의원 보좌관으로 인연을 맺은 이광재 의원이 국토 균형 발전과 공공기관·기업의 지방 이전에 대한 비전을 제시했습니다. 박정희 대통령 시절 포항제철(포스코)을 전폭 지원해 지방 경제의 기틀을 다졌던 국가적 결단처럼, 수도권 집중을 해소하기 위해 교육·의료·기업 인센티브가 어우러진 과감한 지방 이전 결단과 국가적 재설계가 시급함을 피력했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.sidae.com/article/2026091515273636450" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시대일보) →</a></div>
</div>
<div class="source">
📌 출처: 시대일보
</div>
</div>

<!-- 기사 2 (언론보도 - 매일신문: [사설] 李 기자회견, 추락하는 민심 돌리려면 국민만 봐야) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.imaeil.com/page/view/2026091618040964679" target="_blank" style="color: inherit; text-decoration: none;">[사설] 李 기자회견, 추락하는 민심 돌리려면 국민만 봐야</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
대통령 기자회견을 앞두고 정국 불확실 해소와 민심 수습 필요성이 제기되는 가운데, 국회 예결위원장 이광재 의원이 "기자회견 전에 사전 언급을 자제하되 국민들이 느끼는 국정 현안과 의문점들에 대해 대통령이 명확하고 진정성 있게 소통해 주길 바란다"고 정국 구상을 밝혔습니다.
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.imaeil.com/page/view/2026091618040964679" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (매일신문) →</a></div>
</div>
<div class="source">
📌 출처: 매일신문 사설
</div>
</div>

<!-- 기사 3 (현장일지 - 네이버 블로그: 이광재, "대전을 기업이 머무는 도시로 만들겠습니다") -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224413843999" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] 이광재, "대전을 기업이 머무는 도시로 만들겠습니다"… 대전 예산정책협의회</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
대전 예산정책협의회에 참석하여 허태정 시장, 지역 국회의원들과 대전의 미래 발전과 국비 예산 확보를 논의했습니다. KAIST, 충남대, 대덕연구개발특구의 우수한 인재와 연구 성과가 벤처·스타트업 창업과 기업 성장으로 연결되도록 규제 완화, 부지 확보, 반도체·AI 기업 유치 지원 방안을 강조했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/thumbnail-917.jpg" alt="대전을 기업이 머무는 도시로 만들겠습니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224413843999" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 유튜브 숏폼 영상: 노무현 대통령이 말씀하셨던 ‘진정한 용기’) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"노무현 대통령이 말씀하셨던 ‘진정한 용기’" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
고(故) 노무현 전 대통령이 강조했던 '진정한 용기'의 정치적 의미와 소신 있는 의정활동 철학을 청문회 및 의정 현장의 모습과 함께 담아낸 이광재 의원의 숏폼 영상입니다.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-A5H3SrB6qiE" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-A5H3SrB6qiE" poster="https://img.youtube.com/vi/A5H3SrB6qiE/hqdefault.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0917.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/A5H3SrB6qiE?feature=oembed" title="노무현 대통령이 말씀하셨던 ‘진정한 용기’" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/shorts/A5H3SrB6qiE?si=9CtNtg9_I_uzTYtm" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 유튜브 (이광재 TV)
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

<!-- 지역 뉴스 기사 1 (하남시 노후주택 집수리 지원사업) -->
<div class="article-card">
<div class="badge">📰 주거/복지</div>
<h3><a href="https://www.gukjenews.com/news/articleView.html?idxno=3697774" target="_blank" style="color: inherit; text-decoration: none;">하남시, 노후주택 집수리 지원사업으로 주거환경 개선… 반지하 침수방지 및 단열·방수 맞춤형 지원</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 소규모 노후주택 집수리 지원사업을 실시해 가구당 최대 1,200만 원(공사비 최대 90%)을 지원하고 있습니다. 반지하 물막이 차수판 설치, 옥상 방수, 단열 창호 교체, 안전손잡이 등 맞춤형 주거환경 개선과 패시브 리모델링 지원으로 안심하고 거주할 수 있는 환경을 만듭니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.gukjenews.com/news/articleView.html?idxno=3697774" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (국제뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 국제뉴스 (강정훈 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (2026 한돈런 미사경정공원 개최) -->
<div class="article-card">
<div class="badge">📰 체육/축제</div>
<h3><a href="https://www.nocutnews.co.kr/news/6578874?utm_source=naver&utm_medium=article&utm_campaign=20260916103317" target="_blank" style="color: inherit; text-decoration: none;">'2026 한돈런' 즐길거리 풍성… 9월 20일 하남 미사경정공원서 개최</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
한돈자조금관리위원회가 오는 9월 20일 경기 하남시 미사경정공원에서 '2026 한돈런'을 개최합니다. 10km 및 6km 코스 완주자 전원에게 한돈 도시락이 제공되며, 10개 협찬 브랜드 체험존, '삼겹살(3) 골인러' 선물 등 다채로운 이벤트가 준비됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.nocutnews.co.kr/news/6578874?utm_source=naver&utm_medium=article&utm_campaign=20260916103317" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (노컷뉴스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091701.jpg" alt="2026 한돈런 미사경정공원 개최" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 노컷뉴스
</div>
</div>

<!-- 지역 뉴스 기사 3 (스타필드 한가위 문화 바캉스) -->
<div class="article-card">
<div class="badge">📰 생활/문화</div>
<h3><a href="https://www.newsis.com/view/NISX20260916_0003791227" target="_blank" style="color: inherit; text-decoration: none;">스타필드 하남·고양, 추석 맞아 '한가위 문화 바캉스' 명소로 변신… 대형 벌룬 아트 전시</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
스타필드 하남과 고양이 추석을 맞아 센트럴 아트리움에 대형 벌룬 아트와 세계 명소·문화 테마 전시를 마련했습니다. 가족과 함께 포토존에서 추억을 남길 수 있는 풍성한 '한가위 문화 바캉스' 프로그램이 펼쳐집니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsis.com/view/NISX20260916_0003791227" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴시스) →</a></div>
</div>
<div class="source">
📌 출처: 뉴시스 (오제일 기자)
</div>
</div>
</div>"""

# Slice replace Section 2
idx_local = content.find('<div id="local-news">')
idx_mom = content.find('<div id="mom-cafe">')
content = content[:idx_local] + section2_content + '\n<hr/>\n' + content[idx_mom:]

# 4. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 17일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ "신학기 등하굣길 안심!" 관내 초등학교 스쿨존 안전시설 확충 &amp; 안전지킴이 배치 소식 환영</h4>
<div class="mom-detail"><strong>현황:</strong> 가을 신학기를 맞아 하남 관내 초등학교(미사·위례·감일·신장) 주변 스쿨존 옐로카펫 보수, 횡단보도 바닥형 신호등 확충 및 등하굣길 교통안전 지킴이 배치 소식이 맘카페에서 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들의 안전한 등하굣길 환경 조성 및 초등학교 주변 교통안전 대폭 강화.</div>
<div class="mom-reaction">💬 주민 반응: "아이 학교 앞 바닥 신호등 켜지니 야간이나 비 올 때 훨씬 안심돼요!", "등하교시간 봉사해 주시는 안전지킴이분들 정말 감사합니다" 학부모 응원 잇따라.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ "가을 저녁 온 가족 힐링 산책!" 공원 산책로 야간 조명 교체 &amp; 버스킹 공연 정보 입소문</h4>
<div class="mom-detail"><strong>현황:</strong> 미사호수공원, 덕풍천 산책로, 당정뜰 일대의 산책로 야간 보행등 교체 사업과 주말 가을밤 야외 음악회·버블쇼 개최 소식이 주민들 사이에서 가을 산책 추천 코스로 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 쾌적하고 밝아진 야간 산책로 및 온 가족이 즐기는 공원 문화 체험.</div>
<div class="mom-reaction">💬 주민 반응: "요즘 저녁 바람 선선해서 덕풍천 걸어 다니는데 조명이 밝아져서 훨씬 안전해요", "주말에 호수공원 버블쇼 아이 유모차 끌고 가봐야겠네요" 호평 만발.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "주말 아이와 뭐 하지?" 하남시립도서관 가을맞이 어린이 유아 독서·체험 프로그램 신청 열기</h4>
<div class="mom-detail"><strong>현황:</strong> 미사·위례·일기도서관 등 하남시립도서관에서 운영하는 9~10월 '유아 체험형 동화구현실' 및 '어린이 주말 독서 특강' 수강생 모집 소식이 전해지며 엄마들 사이에서 신청 정보가 빠르게 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 방과 후 및 주말 자녀와 함께 즐기는 무료 알짜 독서·문화 체험.</div>
<div class="mom-reaction">💬 주민 반응: "미사도서관 동화구현실 수업 알차서 광클로 신청 성공했어요!", "도서관 주말 프로그램 아이가 너무 좋아해서 매번 챙겨 봅니다" 만족 반응 호응.</div>
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 17일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (하남시 찾아가는 마을학교) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🏫 ~2026.10.16 | 교육/마을공동체</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502734" target="_blank" style="color: inherit; text-decoration: none;">&lt;2026년 하남시 찾아가는 마을학교&gt; 참여자 모집</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"마을 활동에 관심 있는 시민 모임으로 찾아가는 맞춤형 교육!"</b><br/>
하남시에서 마을공동체 이해 및 사례 공유, 맞춤형 상담을 진행하는 찾아가는 마을학교 참여자를 모집합니다.<br/><br/>
<b>👥 모집 대상:</b> 마을활동에 관심 있는 시민 3명 이상 모임 (선착순)<br/>
<b>📅 교육 기간:</b> 2026년 10월 6일(화) ~ 10월 23일(금)<br/>
<b>📍 교육 장소:</b> 신청자와 협의 후 시간 및 장소 확정<br/>
<b>📝 신청 기간:</b> 2026년 9월 16일(수) ~ 10월 16일(금)<br/>
<b>🎁 참가 혜택:</b> 2027년 마을공동체 공모사업 참여 시 가점 부여
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502734" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (하남시청 공지) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091704.jpg" alt="찾아가는 마을학교 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청
</div>
</div>

<!-- 문화 기사 2 (추석 연휴 종합안내) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🌕 2026.09.16~09.20 | 추석/생활정보</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/cleanh/cleanhBbsNttWebView.do?key=4348&amp;nttNo=3460" target="_blank" style="color: inherit; text-decoration: none;">2026년 추석 연휴 종합안내 (교통·의료·안전·생활편의)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"편안하고 안전한 한가위! 하남시 추석 연휴 종합대책 추진"</b><br/>
하남시가 시민들의 안전하고 편안한 명절을 위해 교통, 응급 의료, 생활폐기물 수거, 안전사고 예방 종합 상황반을 운영합니다.<br/><br/>
<b>🚑 응급 의료:</b> 연휴 기간 문 여는 병·의원 및 약국 상황근무반 운영<br/>
<b>🚗 교통·주차:</b> 원활한 차량 통행 안내 및 공영주차장 운영<br/>
<b>🛍️ 전통시장 이벤트:</b> 9.16~9.20 동안 3만 원 이상 구매 시 경품 증정 (11:00~19:00)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/cleanh/cleanhBbsNttWebView.do?key=4348&amp;nttNo=3460" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 연휴 정보 확인 (청정하남) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091706.jpg" alt="추석 연휴 종합안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 청정하남 (하남시 공보담당관)
</div>
</div>

<!-- 문화 기사 3 (별별캠퍼스 화상학습 온라인캠퍼스) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">💻 2026.09.28~ (선착순) | 온라인/평생교육</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502714" target="_blank" style="color: inherit; text-decoration: none;">[학습자모집] 2026년 마지막 별별캠퍼스 화상학습 (온라인캠퍼스)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"집에서 편하게 배우는 2026년 마지막 실시간 온라인 배움터!"</b><br/>
하남시 평생학습포털에서 10월 개강하는 2026년 마지막 별별캠퍼스 온라인 화상학습(Zoom) 수강생을 모집합니다.<br/><br/>
<b>📅 운영 기간:</b> 2026년 10월 13일(화)부터 강좌별 순차 개강<br/>
<b>📝 신청 기간:</b> 2026년 9월 28일(월) 09:00부터 (선착순 접수)<br/>
<b>💻 준비 사항:</b> Zoom 접속 가능한 PC·노트북 또는 스마트폰<br/>
<b>☎️ 문의:</b> 하남시청 평생교육과 <a href="tel:031-790-5545" style="color:#3182ce; font-weight:bold;">031-790-5545</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502714" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 수강신청하기 (하남시 평생학습포털) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091705.jpg" alt="별별캠퍼스 화상학습 모집 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 평생교육과
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 17일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1: 2026년 경기도 청년기본소득 3분기 접수 안내 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💼 경기도 / 하남시 | ~2026.10.02</div>
<h3><a href="https://apply.jobaba.net/special/gibon/main.do" target="_blank" style="color: inherit; text-decoration: none;">2026년 경기도 청년기본소득 3분기 신청 접수 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
경기도와 하남시가 청년의 사회적 기본권 보장 및 삶의 질 향상을 위해 2026년 3분기 청년기본소득 신청을 접수합니다.<br/><br/>
<b>👥 신청 대상:</b> 경기도 내 3년 이상 계속 또는 합산 10년 이상 거주 24세 청년<br/>
<b>💰 지원 내용:</b> 1인당 분기별 25만 원 (연 최대 100만 원, 지역화폐 지급)<br/>
<b>📝 접수 기간:</b> 2026년 9월 1일(화) ~ 10월 2일(금) 18:00까지<br/>
<b>🌐 신청 방법:</b> 경기도일자리재단 '잡아바 어플라이' 온라인 접수
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://apply.jobaba.net/special/gibon/main.do" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (잡아바 어플라이) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091702.jpg" alt="경기도 청년기본소득 3분기 접수" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 경기도 / 경기도일자리재단 (잡아바)
</div>
</div>

<!-- 공공기관 소식 2: 2026년 9월 정기분 재산세(토지·주택) 납부 안내 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏛️ 위택스 / 하남시세무과 | ~2026.09.30</div>
<h3><a href="https://www.wetax.go.kr/tcp/wtg/J040401M02.do?bbsId=10000000000000003405" target="_blank" style="color: inherit; text-decoration: none;">2026년 9월 정기분 재산세(토지·주택) 납부 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
2026년 9월 정기분 재산세(토지 및 주택 2기분) 납부 기간이 진행됩니다. 연체에 따른 가산금이 발생하지 않도록 기한 내 납부를 권장합니다.<br/><br/>
<b>📅 납부 기간:</b> 2026년 9월 16일(수) ~ 9월 30일(수)까지<br/>
<b>📋 과세 대상:</b> 토지 및 주택(2차분) 소유자<br/>
<b>💳 납부 방법:</b> 위택스(wetax.go.kr), 스마트 위택스 앱, 가상계좌, ARS, 금융기관 CD/ATM<br/>
<b>☎️ 문의:</b> 하남시청 세무과 및 위택스 고객센터
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.wetax.go.kr/tcp/wtg/J040401M02.do?bbsId=10000000000000003405" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고 및 납부하기 (위택스) →</a></div>
</div>
<div class="source">
📌 출처: 행정안전부 위택스 / 하남시청
</div>
</div>

</div>"""

# Slice replace Section 5
idx_public = content.find('<div id="public-news">')
idx_footer = content.find('<!-- 하단')
content = content[:idx_public] + section5_content + '\n\n' + content[idx_footer:]

# 7. Update playNewsletterVideo JavaScript function
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video-A5H3SrB6qiE') || document.getElementById('video--X7EDD6ADSY') || document.getElementById('video-8BKrEO0X7I4');
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
