# -*- coding: utf-8 -*-
import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260914.html'
target_path = 'dashboard/news/kj_hanam_inside_20260915.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Issue Number, and Date
content = content.replace("39호 | 2026년 9월 14일 발행", "40호 | 2026년 9월 15일 발행")
content = content.replace("2026년 9월 14일 기준", "2026년 9월 15일 기준")
content = content.replace("images/thumbnail0914.jpg", "images/thumbnail0915.jpg")
content = content.replace("images/thumb.jpg", "images/thumbnail0915.jpg")

# 2. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer;">
    <span>우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- 기사 1 (언론보도 - 아주경제: 이광재, 강원 예산정책협의회서 "평창올림픽 시설 활용 늘려야") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.ajunews.com/view/20260914135809182" target="_blank" style="color: inherit; text-decoration: none;">이광재, 강원 예산정책협의회서 "평창올림픽 시설 활용 늘려야"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장(경기 하남갑)이 14일 강원도와의 예산정책협의회에 참석해 내년도 국가 예산안 지원 방안을 논의했습니다. 이 위원장은 "강원도는 평창 동계올림픽 시설 등 귀중한 유산을 보유하고 있는 만큼, 시설의 활용도를 대폭 늘려 지역 경제와 관광 활성화로 이어지도록 국가 차원의 적극적인 예산 지원과 관심이 필요하다"고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.ajunews.com/view/20260914135809182" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (아주경제) →</a></div>
</div>
<div class="source">
📌 출처: 아주경제 (송승현 기자)
</div>
</div>

<!-- 기사 2 (현장일지 - 네이버 블로그: 이광재, [한국과 독일, 함께 답을 찾아야 할 때]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224411464805" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] 이광재, "한국과 독일, 함께 답을 찾아야 할 때"… 독일 연방하원 대표단 면담</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
한독의원친선협회장으로서 크리스티안 괴르케 독일 연방하원 재무위원회 위원장 직무대행 및 대표단을 만났습니다. 전쟁과 분단을 딛고 산업강국으로 성장한 양국이 AI 시대와 인구 변화 속에서 국민 소득·자산 확대 및 안정적 노후 보장이라는 공동 과제에 대해 경험을 나누고 협력을 강화해 나가기로 뜻을 모았습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/thumbnail0915.jpg" alt="한국과 독일 함께 답을 찾아야 할 때" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224411464805" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 3 (현장일지 - 네이버 블로그: 이광재, [9월 둘째주 의정활동 보고]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224411371626" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] 이광재, [9월 둘째주 의정활동 보고]… 등원 100일 현장 행보</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
국회 등원 100일을 맞아 감북·초이동을 비롯해 하남시 관내 여러 마을을 방문하고 부영아파트 주민간담회를 가졌습니다. 주민분들과 현장에서 마주 앉아 소통하며 현장의 목소리를 청취하고, 하남의 묵은 현안 해결과 새로운 도전을 위해 발로 뛰는 의정활동을 이어갈 것을 다짐했습니다.
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224411371626" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 4 (현장일지 - 유튜브 숏폼 영상: 세금 먹는 하마, 올림픽 시설 살려낼 법안) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"세금 먹는 하마, 올림픽 시설 살려낼 법안" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
동계올림픽 시설 등 방치된 국가 유산 시설의 활용도를 높이고 예산 낭비를 막아 관광 자원으로 전환하기 위한 이광재 의원의 입법 및 의정활동 현장 숏폼 영상입니다.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-8BKrEO0X7I4" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-8BKrEO0X7I4" poster="https://img.youtube.com/vi/8BKrEO0X7I4/hqdefault.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0915.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/8BKrEO0X7I4?feature=oembed" title="세금 먹는 하마, 올림픽 시설 살려낼 법안" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/shorts/8BKrEO0X7I4?si=LRcWH2uPtuKQY554" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
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

<!-- 지역 뉴스 기사 1 (하남시의회 전통시장 정책연구 착수) -->
<div class="article-card">
<div class="badge">📰 지역경제/상권</div>
<h3><a href="https://sports.donga.com/region/article/all/20260914/134666813/1" target="_blank" style="color: inherit; text-decoration: none;">하남시의회, 전통시장 ‘지원 이후’ 성과 따진다… ‘정책연구’ 착수</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회 의원연구단체 '하남시 전통시장·상점가 육성 및 활성방안 연구회'(의장 정병용)가 신장·덕풍전통시장 및 석바대상점가 등 관내 전통시장에 투입된 최근 5년간 지원사업의 사후 효과를 종합 분석하고, 상권별 특성에 맞춘 자생력 강화 정책 수립 연구에 본격 나섰습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://sports.donga.com/region/article/all/20260914/134666813/1" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (스포츠동아) →</a></div>
</div>
<div class="source">
📌 출처: 스포츠동아
</div>
</div>

<!-- 지역 뉴스 기사 2 (하남시청 광장 추석 맞이 농산물 직거래 장터) -->
<div class="article-card">
<div class="badge">📰 행정/농산물</div>
<h3><a href="https://www.asiatoday.co.kr/kn/view.php?key=20260913010004740" target="_blank" style="color: inherit; text-decoration: none;">하남시청 광장에 추석 맞이 '농산물 직거래 장터' 선다</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 추석 명절을 앞두고 9월 15일 오전 10시부터 시청 미관광장에서 하남 지역 농가들이 직접 생산한 신선한 로컬푸드와 추석 제수용 농산물을 시중보다 저렴한 가격에 판매하는 '농산물 직거래 장터'를 운영합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.asiatoday.co.kr/kn/view.php?key=20260913010004740" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (아시아투데이) →</a></div>
</div>
<div class="source">
📌 출처: 아시아투데이 (박준성 기자)
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 15일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 하남시 '어린이 365 24시간 언제나 어린이집' 및 야간·휴일 긴급돌봄 확대 소식에 학부모 큰 호응</h4>
<div class="mom-detail"><strong>현황:</strong> 맞벌이 및 긴급 상황 시 야간·주말에도 안심하고 아이를 맡길 수 있는 '365 24시간 언제나 어린이집'과 일시 긴급돌봄 전담 시설 확대 소식이 학부모 커뮤니티에서 폭발적인 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 365일 야간·휴일 긴급 양육 공백 해소 및 24시간 안심 돌봄 체계 구축.</div>
<div class="mom-reaction">💬 주민 반응: "급한 야근이나 주말 경조사 때 정말 든든하네요!", "하남시 아이 키우기 좋은 환경 계속 늘어나서 마음이 놓입니다" 학부모 응원 속출.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 추석 연휴 전통시장 주변 불법주정차 단속 완화 &amp; 마루공원 성묘객 갓길 주차 허용 반가운 소식</h4>
<div class="mom-detail"><strong>현황:</strong> 추석 연휴를 맞아 신장·덕풍전통시장 주변 도로 주정차 단속이 한시 완화(9.24~9.27)되고, 하남등기소 맞은편 갓길 주차 단속이 유예(9.25 09:00~16:00)된다는 발표에 주민들의 주차 편의 호응이 이어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 명절 장보기 및 마루공원 성묘객 주차 공간 확보로 주차 난 해소.</div>
<div class="mom-reaction">💬 주민 반응: "전통시장 장볼 때 주차 걱정 덜었네요!", "성묘 가시는 분들 갓길 주차 시간 체크하세요" 맘카페 공유 활발.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 2026년 가정보육 어린이 '건강과일 지원사업' 신청 접수 마감(9/18) 임박에 학부모 신청 인증 속출</h4>
<div class="mom-detail"><strong>현황:</strong> 경기도 및 하남시 가정보육 영유아(가정양육수당·부모급여 수급자)에게 제철 과일 바우처를 지원하는 신청 접수 마감일(9월 18일)이 다가오면서 신청 인증글이 급증했습니다.</div>
<div class="mom-point">💡 주민 포인트: 경기민원24를 통한 간편 신청으로 우리 아이 제철 과일 지원 혜택 누리기.</div>
<div class="mom-reaction">💬 주민 반응: "신청 5분도 안 걸려요! 가정보육 아이들 잊지 말고 신청하세요", "알찬 정보 감사합니다" 맘카페 추천 속출.</div>
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
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 15일 기준 한눈에 보는 하남시 최신 문화·행사·추석 주차 단속 안내 가이드</p>

<!-- 문화 기사 1 (추석 연휴 불법주정차 단속 완화 안내) -->
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

<!-- 문화 기사 2 (2026 코스트코 하남점 추석 영업시간 & 휴무일 안내) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🛒 2026.09.24~09.27 | 쇼핑/추석</div>
<h3 style="margin-top: 6px;"><a href="https://blog.naver.com/jyoon930/224391683753" target="_blank" style="color: inherit; text-decoration: none;">2026 코스트코 하남점 9월 휴무일 &amp; 추석 연휴 영업시간 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"추석 명절 장보기 일정 미리 체크하세요! 코스트코 하남점 추석 연휴 운영시간"</b><br/>
2026년 추석 명절을 맞아 코스트코 하남점의 9월 추석 연휴 기간 영업시간 및 휴무일 일정이 전해졌습니다.<br/><br/>
<b>🛒 코스트코 하남점 추석 연휴 영업 안내</b><br/>
&nbsp;&nbsp;• <b>9월 24일(목):</b> <b>오후 7시 조기 폐점</b><br/>
&nbsp;&nbsp;• <b>9월 25일(금):</b> <b>추석 당일 휴무</b><br/>
&nbsp;&nbsp;• <b>9월 26일(토):</b> <b>정상 영업</b><br/>
&nbsp;&nbsp;• <b>9월 27일(일):</b> <b>정기 휴무</b> (넷째 주 일요일)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/jyoon930/224391683753" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 보기 (네이버 블로그 / 작성자 제이윤) →</a></div>
</div>
<div class="source">
📌 출처: 네이버 블로그 (제이윤)
</div>
</div>

<!-- 문화 기사 3 (HPV 국가예방접종 남아 대상 확대 지원) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">💉 2026년~ | 건강/보건</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=498785" target="_blank" style="color: inherit; text-decoration: none;">하남시보건소, HPV(사람유두종바이러스) 국가예방접종 남아 대상 확대 시행 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"우리 아이 건강을 지키는 HPV 백신 무료 접종, 남학생까지 확대 지원!"</b><br/>
하남시보건소에서 기존 여아 대상이었던 HPV(사람유두종바이러스) 무료 예방접종 대상을 12세~17세 남자 청소년(남아)까지 확대 실시합니다.<br/><br/>
<b>💉 접종 대상:</b> 12세~17세 남·여 청소년 (2007년생~2013년생)<br/>
<b>🏥 접종 장소:</b> 관내 지정 위탁의료기관 및 전국 지정 의료기관<br/>
<b>📋 접종 백신:</b> HPV 2가 및 4가 백신 (무료 접종 지원)<br/>
<b>☎️ 문의:</b> 하남시보건소 예방접종실 <a href="tel:031-790-6575" style="color:#3182ce; font-weight:bold;">031-790-6575</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=498785" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 및 카드뉴스 보기 (하남시보건소) →</a></div>
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

# Slice replace Section 4
idx_culture = content.find('<div id="culture">')
idx_public = content.find('<div id="public-news">')
content = content[:idx_culture] + section4_content + '\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>\n\n' + content[idx_public:]

# 6. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 15일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1: 2026년 가정보육 어린이 건강과일 지원사업 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🍎 경기민원24 | ~2026.09.18</div>
<h3><a href="https://gg24.gg.go.kr/svcreqst/selectSvcReqst.do?svc_seq=953" target="_blank" style="color: inherit; text-decoration: none;">2026년 가정보육 어린이 건강과일 지원사업 신청 안내 (신청마감 9.18)</a></h3>
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

<!-- 공공기관 소식 2: 2026-2027절기 인플루엔자(독감)·코로나19 무료 예방접종 실시 -->
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

<!-- 공공기관 소식 3: '9.14 아토피피부염의 날 기념' 워크온 걷기 챌린지 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">👟 하남시보건소 | 2026.09.07~09.20</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502355" target="_blank" style="color: inherit; text-decoration: none;">'9.14 아토피피부염의 날 기념' 워크온 걷기 챌린지 참여 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시보건소에서 9월 14일 '세계 아토피피부염의 날'을 기념하여 하남시민 대상 모바일 걷기 앱(워크온) 챌린지를 진행합니다.<br/><br/>
<b>기간:</b> 2026년 9. 7.(월) ~ 9. 20.(일) (14일간)<br/>
<b>대상:</b> 하남시민 누구나<br/>
<b>내용:</b> 14일간 누계 91,400걸음 달성 (1일 최대 9,140걸음 인정)<br/>
<b>상품:</b> 핸드크림 (목표 달성 후 [응모하기] 완료자 중 300명 추첨 증정)<br/>
※ 주소지가 하남시인 시민 대상 배송 지원
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502355" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091403.jpg" alt="'9.14 아토피피부염의 날 기념' 워크온 걷기 챌린지" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시보건소 건강증진과
</div>
</div>
</div>"""

# Slice replace Section 5
idx_public = content.find('<div id="public-news">')
idx_footer = content.find('<!-- 하단')
content = content[:idx_public] + section5_content + '\n\n' + content[idx_footer:]

# 7. Update playNewsletterVideo JavaScript function
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video-8BKrEO0X7I4') || document.getElementById('video-yclRLijNE14') || document.getElementById('video-3BlZC9feiyw');
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
