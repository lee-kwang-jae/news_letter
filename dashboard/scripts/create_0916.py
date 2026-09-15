# -*- coding: utf-8 -*-
import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260915.html'
target_path = 'dashboard/news/kj_hanam_inside_20260916.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Issue Number, and Date
content = content.replace("40호 | 2026년 9월 15일 발행", "41호 | 2026년 9월 16일 발행")
content = content.replace("2026년 9월 15일 기준", "2026년 9월 16일 기준")
content = content.replace("images/thumbnail0915.jpg", "images/thumbnail0916.jpg")
content = content.replace("images/thumb.jpg", "images/thumbnail0916.jpg")

# 2. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer;">
    <span>우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- 기사 1 (언론보도 - 조선일보: 이광재 "李지지율 빨간불 직전… 부동산 등 입장 밝혀야") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.chosun.com/politics/assembly/2026/09/15/YGTNAUOXAJHZBBYTNI2BRFDTVI/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news" target="_blank" style="color: inherit; text-decoration: none;">이광재 "李지지율 빨간불 직전… 부동산 등 입장 밝혀야"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
4선 중진이자 국회 예산결산특별위원장인 이광재 의원이 15일 KBS라디오 ‘전격 시사’에서 이재명 대통령의 지지율 흐름에 대해 “빨간 불 바로 직전의 주황색 불이라고 봐야 한다”고 진단하며, 공소 취소, 연임 개헌, 부동산 등 민생 현안과 정국 불확실성에 대해 대통령 기자회견을 통해 분명한 입장을 밝혀 국민적 의구심을 해소해야 한다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.chosun.com/politics/assembly/2026/09/15/YGTNAUOXAJHZBBYTNI2BRFDTVI/?utm_source=naver&utm_medium=referral&utm_campaign=naver-news" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (조선일보) →</a></div>
</div>
<div class="source">
📌 출처: 조선일보 (유종헌 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 디지털타임스: [논설실의 서가] 이광재 의원이 밝히는 대한민국 재설계 플랜) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.dt.co.kr/article/12084128?ref=naver" target="_blank" style="color: inherit; text-decoration: none;">[논설실의 서가] 이광재 의원이 밝히는 대한민국 재설계 플랜</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 예산결산특별위원장 이광재 의원(더불어민주당)이 청와대 국정상황실장, 국회 사무총장, 강원도지사 등 입법·행정·외교 현장에서 다진 국정 경험을 바탕으로 제시하는 대한민국 지속가능 발전 전략이 서평으로 조명됐습니다. AI 문명사적 전환기와 미·중 기술 패권 경쟁 속 국가 생존과 지속가능한 마스터플랜을 차분히 담았습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.dt.co.kr/article/12084128?ref=naver" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디지털타임스) →</a></div>
</div>
<div class="source">
📌 출처: 디지털타임스 (강현철 논설위원)
</div>
</div>

<!-- 기사 3 (현장일지 - 네이버 블로그: 이광재, [국가의 성장을 국민의 삶으로]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224413002371" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] 이광재, "국가의 성장을 국민의 삶으로"… 이형일 경제부총리 후보자 인사청문회</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이형일 경제부총리 겸 재정경제부장관 후보자 인사청문회를 가졌습니다. 국가의 거시적 경제적 성장이 국민 개개인의 실질적인 삶의 질 향상과 자산 형성, 주거 및 노후 안정을 담보할 수 있도록 정책적 대안을 질의하고 재정·경제 정책의 나아갈 방향을 철저히 검증했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/thumbnail0916.jpg" alt="국가의 성장을 국민의 삶으로" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224413002371" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 유튜브 숏폼 영상: 망신 주기 청문회, 이제는 바꿔야 합니다) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"망신 주기 청문회, 이제는 바꿔야 합니다" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
인사청문회가 소모적인 망신 주기나 인격 모독에 그치지 않고 국정 수행 능력과 정책 검증 본연의 목적에 충실하도록 제도적 개선과 품격 있는 정치를 촉구하는 이광재 의원의 의정활동 현장 숏폼 영상입니다.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container--X7EDD6ADSY" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video--X7EDD6ADSY" poster="https://img.youtube.com/vi/-X7EDD6ADSY/hqdefault.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0916.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/-X7EDD6ADSY?feature=oembed" title="망신 주기 청문회, 이제는 바꿔야 합니다" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/shorts/-X7EDD6ADSY?si=y2Wgwed3HmsniRbs" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
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

<!-- 지역 뉴스 기사 1 (2026 하남 이성산성 문화제 19일 개막) -->
<div class="article-card">
<div class="badge">📰 문화/축제</div>
<h3><a href="https://www.hani.co.kr/arti/area/capital/1277899.html" target="_blank" style="color: inherit; text-decoration: none;">천년의 울림 ‘요고’와 함께… ‘2026 하남 이성산성 문화제’ 19일 개막</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
삼국시대 역사와 문화가 숨 쉬는 하남시 대표 향토 문화축제인 ‘2026 하남 이성산성 문화제’가 9월 19일과 20일 미사호수공원과 이성산성 일대에서 열립니다. 국내 최초 발굴 타악 유물 ‘요고’와 대북 퍼포먼스, 퓨전 국악, 신유·윤종신·비비 등 초대가수 공연과 최태성의 역사 콘서트 등 다채로운 프로그램이 펼쳐집니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hani.co.kr/arti/area/capital/1277899.html" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (한겨레) →</a></div>
</div>
<div class="source">
📌 출처: 한겨레 (이정하 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (하남시 전통시장 물가안정 캠페인) -->
<div class="article-card">
<div class="badge">📰 지역경제/전통시장</div>
<h3><a href="https://www.gukjenews.com/news/articleView.html?idxno=3696054" target="_blank" style="color: inherit; text-decoration: none;">하남시, 추석 앞두고 전통시장 물가안정 캠페인… 가격표시 준수 홍보</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 추석 명절을 맞아 15일 신장전통시장과 덕풍전통시장 일대에서 소비자단체 회원 40여 명과 함께 전통시장 물가안정과 건전한 상거래 질서 확립 캠페인을 전개했습니다. 가격 및 원산지 표시 준수, 합리적 소비와 착한 가격 업소 이용을 집중 홍보했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.gukjenews.com/news/articleView.html?idxno=3696054" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (국제뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 국제뉴스 (강정훈 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (하남 국제 트레일런 페스티벌 12월 개최) -->
<div class="article-card">
<div class="badge">📰 체육/관광</div>
<h3><a href="https://www.topstarnews.net/news/articleView.html?idxno=16194534" target="_blank" style="color: inherit; text-decoration: none;">“검단산·남한산성 잇는 코스”… 12월 '하남 국제 트레일런 페스티벌' 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
2026 연합뉴스 하남 국제 트레일런 페스티벌(YHITF)이 12월 12~13일 미사경정공원과 검단산, 남한산성 일대에서 펼쳐집니다. 황영조 감독이 디자인한 생태 수변과 산악 순환 코스로, 5·10km 로드와 15·28km 트레일 종목에서 엘리트 러너와 동호인이 함께 즐기는 대형 러닝 축제가 준비 중입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.topstarnews.net/news/articleView.html?idxno=16194534" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (톱스타뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 톱스타뉴스 (임가영 기자)
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 16일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ '2026 하남 이성산성 문화제' 19일~20일 미사호수공원 개막 소식에 맘카페 관심 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 이번 주말(9/19~20) 미사호수공원과 이성산성에서 열리는 이성산성 문화제 대형 개막 공연(윤종신, 비비, 신유, 최태성 역사콘서트)과 어린이 유물발굴 체험 부스 소식이 맘카페에서 큰 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 온 가족 무료 국악·가수 공연 관람 및 어린이 백제 문화 체험 활동.</div>
<div class="mom-reaction">💬 주민 반응: "이번 주말 아이들이랑 미사호수공원 필수 코스네요!", "윤종신이랑 비비도 오다니 가족 나들이로 딱입니다" 기대감 만발.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 추석 전통시장 알뜰 장보기 &amp; 주정차 단속 완화 완벽 가이드 주민 호평</h4>
<div class="mom-detail"><strong>현황:</strong> 추석 연휴 신장·덕풍전통시장 주정차 단속 한시 완화(9.24~9.27) 및 성묘객 마루공원 갓길 주차 허용과 더불어 전통시장 물가안정 캠페인 정보가 맘카페에서 널리 공유되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 명절 장보기 주차 우려 해소 및 로컬 푸드 알뜰 장보기 팁 공유.</div>
<div class="mom-reaction">💬 주민 반응: "전통시장 주차 시간표 미리 캡처해뒀어요", "장보기 물가안정 혜택 꿀정보 감사합니다" 반응 뜨거움.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 2026년 가정보육 어린이 '건강과일 지원사업' 신청 마감(9/18) D-2 막바지 신청 공유</h4>
<div class="mom-detail"><strong>현황:</strong> 경기도 및 하남시 가정보육 영유아(가정양육수당·부모급여 수급자) 제철 과일 바우처 지원 신청 마감일(9월 18일)이 이틀 앞으로 다가오면서 신청 팁과 인증글이 이어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 경기민원24를 통한 온라인 5분 간편 신청으로 우리 아이 제철 과일 혜택 챙기기.</div>
<div class="mom-reaction">💬 주민 반응: "깜빡할 뻔했는데 맘카페 덕분에 신청 완료했네요", "가정보육 하시는 분들 내일까지 꼭 챙기세요" 권장 속출.</div>
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 16일 기준 한눈에 보는 하남시 최신 문화·행사·추석 안내 가이드</p>

<!-- 문화 기사 1 (2026 하남 이성산성 문화제 19일 개막) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🏛️ 2026.09.19~09.20 | 축제/문화</div>
<h3 style="margin-top: 6px;"><a href="https://www.hani.co.kr/arti/area/capital/1277899.html" target="_blank" style="color: inherit; text-decoration: none;">2026 하남 이성산성 문화제 개막 (미사호수공원 &amp; 이성산성 일원)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"하남의 역사, 미래를 두드리다! 온 가족이 함께 즐기는 K-컬처 역사문화 축제"</b><br/>
하남시의 대표 향토 축제인 '2026 하남 이성산성 문화제'가 9월 19일(토)부터 20일(일)까지 미사호수공원과 이성산성에서 개최됩니다.<br/><br/>
<b>🥁 개막 주제공연 (9.19 토 19:00~):</b> 타악기 '요고' &amp; 대북 울림, 미디어퍼포먼스, 퓨전 국악<br/>
<b>🎤 초대가수 공연 (9.19 토 19:30~):</b> 신유, 윤종신, 비비 등 정상급 가수 무대<br/>
<b>📚 전세대 프로그램 (9.20 일):</b> 최태성의 '역사 콘서트', 플래시몹 댄스, 3인 3색 콘서트<br/>
<b>🎯 체험 부스:</b> 유물발굴장, 수비대 훈련소, 요고 만들기, 백제 포토존, 플리마켓 상시 운영
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hani.co.kr/arti/area/capital/1277899.html" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 프로그램 보기 →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 / 한겨레
</div>
</div>

<!-- 문화 기사 2 (추석 연휴 불법주정차 단속 완화 안내) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🚗 2026.09.24~09.27 | 추석/교통</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">추석 연휴 하남시 전통시장 주변 도로 불법주정차 단속 완화 &amp; 마루공원 성묘객 주차 유예</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"추석 명절 장보기 및 성묘길 주차 편의 지원!"</b><br/>
하남시에서 2026년 추석 연휴를 맞아 시민분들의 전통시장 이용 활성화와 마루공원 성묘객의 편의를 위해 불법주정차 단속 완화 및 갓길 주차 유예를 실시합니다.<br/><br/>
<b>🛒 신장·덕풍전통시장 주변 도로 주정차 단속 완화</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 24일(목) ~ 9월 27일(일)<br/>
&nbsp;&nbsp;• <b>내용:</b> 전통시장 이용객 주차 편의를 위한 주정차 단속 한시 완화<br/><br/>
<b>🪦 하남등기소 맞은편 갓길주차 단속 유예 (마루공원 성묘객)</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 25일(금) 09:00 ~ 16:00<br/>
&nbsp;&nbsp;• <b>내용:</b> 마루공원 성묘객 주차 지원을 위한 하남등기소 맞은편 갓길 주차 유예
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 / 하남시 주차관리과
</div>
</div>

<!-- 문화 기사 3 (2026 코스트코 하남점 추석 영업시간 & 휴무일 안내) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🛒 2026.09.24~09.27 | 쇼핑/추석</div>
<h3 style="margin-top: 6px;"><a href="https://blog.naver.com/jyoon930/224391683753" target="_blank" style="color: inherit; text-decoration: none;">2026 코스트코 하남점 9월 휴무일 &amp; 추석 연휴 영업시간 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"추석 명절 장보기 일정 미리 체크하세요! 코스트코 하남점 추석 연휴 운영시간"</b><br/>
2026년 추석 명절을 맞아 코스트코 하남점의 9월 추석 연휴 기간 영업시간 및 휴무일 일정이 전해졌습니다.<br/><br/>
<b>🛒 코스트코 하남점 추석 연휴 영업 안내</b><br/>
&nbsp;&nbsp;• <b>9월 24일(목):</b> <b>오후 7시 조기 폐점</b><br/>
&nbsp;&nbsp;• <b>9월 25일(금):</b> <b>추석 당일 휴무</b><br/>
&nbsp;&nbsp;• <b>9월 26일(토):</b> <b>정상 영업</b><br/>
&nbsp;&nbsp;• <b>9월 27일(일):</b> <b>정기 휴무</b> (넷째 주 일요일)
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091404.png" alt="2026 코스트코 하남점 추석 연휴 영업시간 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 16일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1: 2026년 하남시 일자리박람회 참가기업 모집 안내 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💼 하남시청 | ~2026.10.12</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502693" target="_blank" style="color: inherit; text-decoration: none;">하남시, '2026 온세대+경기도 5070 일자리박람회' 참가기업 모집 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시가 경기도, 경기도일자리재단, 하남고용복지+센터와 협력하여 10월 30일(금) 하남종합운동장에서 열리는 '2026 하남시 온세대+경기도 5070 일자리박람회'에 참여할 구인기업(40개사)을 모집합니다.<br/><br/>
<b>📅 일시 및 장소:</b> 2026년 10월 30일(금) 13:00~16:00 / 하남종합운동장 제2체육관<br/>
<b>🏢 모집 규모:</b> 구인기업 40개사 (직접채용 30개사, 간접채용 10개사)<br/>
<b>📝 접수 기간:</b> 2026년 9월 14일 ~ 10월 12일 18:00까지 (방문·팩스·이메일 접수)<br/>
<b>☎️ 문의:</b> 하남일자리센터 <a href="tel:031-790-6890" style="color:#3182ce; font-weight:bold;">031-790-6890</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502693" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 및 신청서 보기 (하남시청) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091602.png" alt="2026년 하남시 일자리박람회 참가기업 모집 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 지역경제과 / 하남일자리센터
</div>
</div>

<!-- 공공기관 소식 2: 하남도시공사 공영주차장 정기권 순환배정 공개추첨 모집 공고 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🅿️ 하남도시공사 | 주차/공공</div>
<h3><a href="https://www.huic.co.kr/www/selectBbsNttView.do?key=102&amp;bbsNo=36&amp;nttNo=11517" target="_blank" style="color: inherit; text-decoration: none;">하남도시공사, 공영주차장 정기권 순환배정 공개추첨 모집 공고</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남도시공사에서 관내 일반 공영주차장의 공정한 이용 기회 제공 및 시민 주차 편의를 위한 '일반공영주차장 사용자(정기권) 순환배정 공개추첨' 모집을 실시합니다.<br/><br/>
<b>🚗 대상 시설:</b> 관내 일반공영주차장 (덕풍·신장·미사 등)<br/>
<b>📋 신청 대상:</b> 하남시민 및 관내 사업장 근무자<br/>
<b>📝 신청 방법:</b> 하남도시공사 홈페이지 공지사항 공고문 접수<br/>
<b>☎️ 문의:</b> 하남도시공사 주차사업팀
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.huic.co.kr/www/selectBbsNttView.do?key=102&amp;bbsNo=36&amp;nttNo=11517" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 및 신청 서식 보기 (하남도시공사) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091601.png" alt="하남도시공사 공영주차장 정기권 모집" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남도시공사
</div>
</div>

<!-- 공공기관 소식 3: 2026년 가정보육 어린이 건강과일 지원사업 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🍎 경기민원24 | ~2026.09.18 (D-2)</div>
<h3><a href="https://gg24.gg.go.kr/svcreqst/selectSvcReqst.do?svc_seq=953" target="_blank" style="color: inherit; text-decoration: none;">2026년 가정보육 어린이 건강과일 지원사업 신청 안내 (신청마감 9.18 D-2)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
경기도와 하남시에서 어린이집·유치원 등 시설을 이용하지 않는 가정보육 어린이에게 신선한 제철 과일 바우처(연 1회)를 지원합니다.<br/><br/>
<b>지원 대상:</b> 신청기간(8.18 ~ 9.18) 중 경기도 내 주민등록이 되어 있고 시설을 이용하지 않는 가정보육 어린이<br/>
&nbsp;&nbsp;• 가정양육수당 수급자 (24개월 이상 ~ 86개월 미만 미취학 아동)<br/>
&nbsp;&nbsp;• 부모급여(현금) 수급자 (0 ~ 23개월 아동)<br/>
<b>신청 기간:</b> 2026년 8월 18일 ~ 9월 18일 (마감 임박!)<br/>
<b>신청 방법:</b> 경기민원24 온라인 신청 (<a href="https://gg24.gg.go.kr/svcreqst/selectSvcReqst.do?svc_seq=953" target="_blank" style="color:#3182ce; font-weight:bold;">gg24.gg.go.kr</a>) 또는 아동 주소지 동 행정복지센터 방문 신청
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://gg24.gg.go.kr/svcreqst/selectSvcReqst.do?svc_seq=953" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (경기민원24) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091401.png" alt="2026년 가정보육 어린이 건강과일 지원사업" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 경기도 / 경기민원24 / 하남시
</div>
</div>

<!-- 공공기관 소식 4: 2026-2027절기 인플루엔자(독감)·코로나19 무료 예방접종 실시 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💉 하남시보건소 | 2026.09~</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: inherit; text-decoration: none;">2026-2027절기 인플루엔자(독감) 및 코로나19 무료 예방접종 실시 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시보건소에서 2026-2027절기 독감 및 코로나19 무료 예방접종을 실시합니다. 접종 쏠림 방지를 위해 연령별·대상별 접종 일자가 상이하오니 사전 확인 후 지정 의료기관을 방문해 주세요.<br/><br/>
<b>접종 백신:</b> 인플루엔자 3가 백신 / 코로나 XFG 백신 (화이자, 모더나)<br/>
<b>접종 대상:</b> 65세 이상 어르신(독감+코로나 동시접종 가능), 어린이, 임신부, 취약계층, 60~64세<br/>
<b>접종 장소:</b> 관내 지정 위탁의료기관 (하남시보건소 자체 접종은 실시하지 않음)<br/>
<b>준비물:</b> 신분증, 아기수첩, 임신확인서, 수급자/장애인 증명서 등 대상별 확인서류<br/>
<b>문의:</b> 하남시보건소 예방접종실 <a href="tel:031-790-6575" style="color:#3182ce; font-weight:bold;">031-790-6575</a> / 미사보건센터 <a href="tel:031-790-6560" style="color:#3182ce; font-weight:bold;">031-790-6560</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">위탁의료기관 현황 및 공고 보기 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0914-2.jpg" alt="2026-2027절기 인플루엔자 및 코로나19 무료 예방접종" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시보건소 보건정책과
</div>
</div>

<!-- 공공기관 소식 5: HPV 국가예방접종 남아 대상 확대 지원 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💉 하남시보건소 | 2026년~</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=498785" target="_blank" style="color: inherit; text-decoration: none;">하남시보건소, HPV(사람유두종바이러스) 국가예방접종 남아 대상 확대 시행 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시보건소에서 기존 여아 대상이었던 HPV(사람유두종바이러스) 무료 예방접종 대상을 12세~17세 남자 청소년(남아)까지 확대 실시합니다.<br/><br/>
<b>💉 접종 대상:</b> 12세~17세 남·여 청소년 (2007년생~2013년생)<br/>
<b>🏥 접종 장소:</b> 관내 지정 위탁의료기관 및 전국 지정 의료기관<br/>
<b>📋 접종 백신:</b> HPV 2가 및 4가 백신 (무료 접종 지원)<br/>
<b>☎️ 문의:</b> 하남시보건소 예방접종실 <a href="tel:031-790-6575" style="color:#3182ce; font-weight:bold;">031-790-6575</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=498785" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 및 카드뉴스 보기 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091403.jpg" alt="HPV 예방접종 남아 확대 시행 안내 포스터" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시보건소 보건정책과
</div>
</div>
</div>"""

# Slice replace Section 5
idx_public = content.find('<div id="public-news">')
idx_footer = content.find('<!-- 하단')
content = content[:idx_public] + section5_content + '\n\n' + content[idx_footer:]

# 7. Update playNewsletterVideo JavaScript function
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video--X7EDD6ADSY') || document.getElementById('video-8BKrEO0X7I4') || document.getElementById('video-yclRLijNE14') || document.getElementById('video-3BlZC9feiyw');
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
