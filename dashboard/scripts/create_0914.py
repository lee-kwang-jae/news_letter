# -*- coding: utf-8 -*-
import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260911.html'
target_path = 'dashboard/news/kj_hanam_inside_20260914.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Issue Number, and Date
content = content.replace("38호 | 2026년 9월 11일 발행", "39호 | 2026년 9월 14일 발행")
content = content.replace("2026년 9월 11일 기준", "2026년 9월 14일 기준")

# 2. Section 1: 우리동네 국회의원 이광재 (언론보도 1 + 현장일지 2 + 현장일지 영상 1)
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer;">
    <span>우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- 기사 1 (언론보도 - 경기일보: 이광재 예결위원장 “국민 세금 실질적 효과가 예산심사 기준”) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kyeonggi.com/article/20260913580277" target="_blank" style="color: inherit; text-decoration: none;">이광재 예결위원장 “국민 세금 실질적 효과가 예산심사 기준” [경기인터뷰]</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장(경기 하남갑)이 경기일보 인터뷰를 통해 820조 원 규모의 국가 예산안 심사 방향과 하남시 주요 현안 구상을 밝혔습니다. 이 위원장은 "경기도 31개 시·군의 지역 특성에 맞춘 예산 편성이 필요하다"며, 하남 교산신도시 철도망 확충과 AI 연구캠퍼스 조성, 학교 복합화 사업 등 하남시 개발 및 교통 인프라 강화를 차질 없이 추진하겠다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kyeonggi.com/article/20260913580277" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (경기일보) →</a></div>
</div>
<div class="source">
📌 출처: 경기일보 (김영호 기자)
</div>
</div>

<!-- 기사 2 (현장일지 - 네이버 블로그: [집도, 삶도 든든한 하남] - 이미지 0914-3 적용) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224409939684" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] "집도, 삶도 든든한 하남"… 미사강변복지관·신안아파트 재건축 현장 행보</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
미사강변사회복지관 개관 10주년 축하, 신안아파트 재건축 설명회 방문, 하남시 사회복지협의회 간담회 등 주말 현장 소통 소식을 공유했습니다. 신안아파트 주민들의 평생 자산이 걸린 재건축·재개발 상시 지원조직을 하남시와 협의해 마련하고, 힘들고 어려운 이웃을 지키는 사회복지 현장의 수고를 예산으로 든든히 뒷받침하겠다고 밝혔습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/0914-3.jpg" alt="집도, 삶도 든든한 하남 현장 행보" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224409939684" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- 기사 3 (현장일지 - 칼럼: “벤처 키우려면 기술보증기금 곳간부터 채워야 한다”) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224410224892" target="_blank" style="color: inherit; text-decoration: none;">[이광재 칼럼] “벤처 키우려면 기술보증기금 곳간부터 채워야 한다”</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
AI·바이오·로봇 등 미개척 기술을 보유한 첨단 벤처기업들이 금융 장벽을 넘을 수 있도록 기술보증기금의 재원을 대폭 확충해야 한다는 칼럼을 게재했습니다. 은행 출연요율 인상(0.135%→0.18% 이상), 정부 출연 확대, 벤처금융 실패 평가 구조 개선 등 기술 도전과 성장을 뒷받침할 3대 개혁 방안을 제시했습니다.
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224410224892" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">칼럼 전문 보기 (이광재 블로그 / 지디넷코리아) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그 / 지디넷코리아
</div>
</div>

<!-- 기사 4 (현장일지 - 유튜브 숏폼 영상: 하남 시민 모두의 교통 환경을 위하여 끝까지 힘을 다하겠습니다) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"하남 시민 모두의 교통 환경을 위하여 끝까지 힘을 다하겠습니다" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
GTX-D 노선 확충 및 황산사거리 교통 체증 개선 등 하남시 주민들의 교통 편의를 대폭 향상시키기 위해 현장에서 적극 행정을 펼치는 이광재 의원의 의정활동 현장 숏폼 영상입니다.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-yclRLijNE14" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-yclRLijNE14" poster="https://img.youtube.com/vi/yclRLijNE14/hqdefault.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0914.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/yclRLijNE14?feature=oembed" title="하남 시민 모두의 교통 환경을 위하여 끝까지 힘을 다하겠습니다" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/shorts/yclRLijNE14?si=eAim5VuUHw2Tm-m-" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 유튜브 (이광재 TV)
</div>
</div>
</div>"""

# Replace Section 1
content = re.sub(r'<div id="lawmaker">.*?</div>\n</div>\n<hr/>', section1_content + '\n<hr/>', content, flags=re.DOTALL)

# 3. Section 2: 하남 지역 주요 뉴스
section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (청약통장 15년, 교산신도시 당첨 가이드) -->
<div class="article-card">
<div class="badge">📰 부동산/청약</div>
<h3><a href="https://www.sisajournal.com/news/articleView.html?idxno=386726" target="_blank" style="color: inherit; text-decoration: none;">“15년간 모은 청약통장, 교산신도시 당첨될까요?” [사이다 부동산]</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
15년간 2,000만 원을 납입한 40대 무주택 4인 가구의 하남 교산신도시 청약 전략 분석이 눈길을 끕니다. 공공분양의 높은 당첨선(2,300만~2,800만 원)을 고려해, 무주택·통장가입 기간 15년 이상 기준 청약가점 69점을 활용한 민간분양 가점제를 동시에 노리는 '투트랙 전략'이 효과적이라는 전문 진단이 전해졌습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.sisajournal.com/news/articleView.html?idxno=386726" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시사저널) →</a></div>
</div>
<div class="source">
📌 출처: 시사저널 (서진형 교수 / 정기환 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (하남-남양주 한강 수변 출렁다리) -->
<div class="article-card">
<div class="badge">📰 교통/수변개발</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260911117200061?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">[현장in] 하남-남양주 잇는 '한강 수변 출렁다리'… 남양주시 재검토에 제동?</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 배알미동과 남양주시 와부읍 팔당리를 잇는 530m 보행 전용 한강 출렁다리 조성 사업이 지방선거 이후 남양주시의 신중 재검토 방침에 부딪혀 후속 실무 협의가 지연되고 있습니다. 연임에 성공한 이현재 하남시장은 수변 관광 및 연결성 강화를 위해 추진을 강구하는 반면, 남양주시는 법적 타당성과 한강유역환경청 규제 우려를 이유로 면밀 검토를 진행 중입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/AKR20260911117200061?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (이우성 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (하남시 하자 발생 필름식 번호판 무상교체) -->
<div class="article-card">
<div class="badge">📰 교통/행정</div>
<h3><a href="https://www.newsis.com/view/NISX20260912_0003786738" target="_blank" style="color: inherit; text-decoration: none;">하남시 "하자 발생한 필름식 자동차번호판 무상 교체 지원"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 필름 들뜸 및 벗겨짐 등 자재 하자로 식별이 불량해진 태극문양 필름식 자동차번호판의 무상 교체를 추진합니다. 최초 등록 5년 이내 차량은 타 지역 발급 번호판이라도 무상 교체가 가능하며, 하남시 번호판제작소 제작 후 하남시청 차량등록과 방문을 통해 처리받을 수 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsis.com/view/NISX20260912_0003786738" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴시스) →</a></div>
</div>
<div class="source">
📌 출처: 뉴시스 (이호진 기자)
</div>
</div>
</div>"""

# Replace Section 2
content = re.sub(r'<div id="local-news">.*?</div>\n</div>\n<hr/>', section2_content + '\n<hr/>', content, flags=re.DOTALL)

# 4. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 정부·하남시 '2026 출산지원금 &amp; 첫만남이용권·부모급여' 지원 확대 정보에 맘카페 반응 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 2026년 정부 첫만남이용권(첫째 200만 원, 둘째 이상 300만 원 바우처) 및 부모급여(0세 월 100만 원, 1세 월 50만 원)와 하남시 자체 출산장려금(첫째 50만 원, 둘째 100만 원, 셋째 200만 원 등) 중복 지원 안내 소식이 전달되어 임산부 및 예비 부모들의 질문과 관심이 집중되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 하남시 출산장려금과 정부 바우처 통합 신청으로 초기 양육비 부담 대폭 경감 및 산후조리비 지원 혜택 강화.</div>
<div class="mom-reaction">💬 주민 반응: "첫째 출산 예정인데 하남시 장려금이랑 정부 첫만남이용권 둘 다 챙길 수 있네요!", "복지로와 행정복지센터 신청 방법 깔끔 정리 꿀팁 감사해요" 맘카페 환호.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 교산신도시 청약 분석 및 40대 무주택 가점제(69점) 청약 전략 정보에 맘카페 열띤 호응</h4>
<div class="mom-detail"><strong>현황:</strong> 15년간 2,000만 원 청약저축을 납입한 40대 4인 가구의 교산신도시 청약 분석 소식이 알려지며 공공분양 저축 총액 경쟁과 민간분양 청약가점 69점을 활용한 '투트랙 청약 전략'이 예비 청약자 사이에서 큰 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 40대 무주택 4인 가구의 교산 84㎡ 민간분양 청약가점 69점 활용법 및 현실적 내 집 마련 가이드 공유.</div>
<div class="mom-reaction">💬 주민 반응: "교산 청약가점 69점 계산법 궁금했는데 실질적 정보네요!", "아이 키우는 무주택 가정에 꼭 필요한 청약 정보입니다" 댓글 속출.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남-남양주 잇는 '530m 한강 수변 출렁다리' 조성 소식에 미사·배알미 주민 산책로 기대</h4>
<div class="mom-detail"><strong>현황:</strong> 하남 배알미동과 남양주 팔당리를 도보로 잇는 530m 한강 출렁다리가 미사경정공원, 스타필드, 팔당 카페거리를 연결하는 수변 힐링 명소로 추진 중이라는 소식이 화제가 되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 하남-남양주 간 보행 전용 산책길 신설로 가을철 가족 단위 팔당 수변 나들이 환경 대폭 개선.</div>
<div class="mom-reaction">💬 주민 반응: "팔당 카페거리까지 아이들과 걸어서 갈 수 있다면 주말 나들이로 최고겠네요!", "지자체 간 협의가 원활하게 결실을 맺길 응원합니다" 기대 만발.</div>
</div>
</div>"""

# Replace Section 3
content = re.sub(r'<div id="mom-cafe">.*?</div>\n</div>\n\n<div id="culture">', section3_content + '\n\n<div id="culture">', content, flags=re.DOTALL)

# 5. Section 4: ALL IN 하남라이프
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 한눈에 보는 하남시 최신 문화·행사·추석 시장 이벤트 가이드</p>

<!-- 문화 기사 1 (추석 연휴 전통시장 이벤트: 신장전통시장 경품 & 하남수산물전통시장 온누리 환급) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎁 2026.09.16~09.23 | 전통시장/추석</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026년 추석 명절 맞이 하남시 전통시장 경품 행사 &amp; 온누리상품권 최대 30% 환급 이벤트</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"풍성한 한가위, 하남시 전통시장에서 장보고 경품과 온누리상품권 혜택 받으세요!"</b><br/>
하남시 관내 전통시장에서 2026년 추석 명절을 맞아 시민과 상인이 함께하는 풍성한 경품 및 온누리상품권 환급 행사를 개최합니다.<br/><br/>
<b>🛍️ 신장전통시장 『추석명절 경품 행사』</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 22일(화) ~ 9월 23일(수)<br/>
&nbsp;&nbsp;• <b>장소:</b> 신장전통시장 고객센터 1층<br/>
&nbsp;&nbsp;• <b>내용:</b> 3만 원 이상 구매 고객 대상 경품 선착순 지급<br/><br/>
<b>🐟 하남수산물전통시장 『온누리상품권 환급행사』</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 16일(수) ~ 9월 20일(일) (11:00 ~ 19:00)<br/>
&nbsp;&nbsp;• <b>내용:</b> 당일 구매 금액의 최대 30%를 온누리상품권으로 환급 (1인 20,000원 한도)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;— 34,000원 이상 ~ 67,000원 미만: <b>10,000원 환급</b><br/>
&nbsp;&nbsp;&nbsp;&nbsp;— 67,000원 이상: <b>20,000원 환급</b>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">전통시장 행사 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 신장전통시장상인회 / 하남수산물전통시장상인회 / 하남시청
</div>
</div>

<!-- 문화 기사 2 (추석 연휴 전통시장 고객전용주차장 운영 및 덕풍주차장 무료 개방) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🚗 2026.09.25~09.26 무료 | 교통/주차</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">추석 연휴 하남시 덕풍·신장 전통시장 주차장 운영 및 덕풍주차장 무료 개방 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"추석 장보기 주차 걱정 끝! 덕풍전통시장 주차장 9월 25일~26일 2일간 무료 개방"</b><br/>
추석 연휴 전통시장을 방문하는 시민분들의 주차 편의를 위해 덕풍·신장전통시장 고객전용주차장을 24시간 운영하며, 덕풍전통시장 주차장은 추석 연휴 기간 무료로 개방합니다.<br/><br/>
<b>🅿️ 덕풍전통시장 고객전용주차장</b><br/>
&nbsp;&nbsp;• <b>위치:</b> 하남시 신장로154번길 57 (130면, 24시간 운영)<br/>
&nbsp;&nbsp;• <b>🎉 무료 개방: 2026년 9월 25일(금) ~ 9월 26일(토) (2일간 전면 무료)</b><br/>
&nbsp;&nbsp;• <b>문의:</b> 덕풍전통시장상인회 <a href="tel:031-794-3753" style="color:#3182ce; font-weight:bold;">031-794-3753</a> (관리자 근무 08:00~22:00)<br/><br/>
<b>🅿️ 신장전통시장 고객전용주차장</b><br/>
&nbsp;&nbsp;• <b>위치:</b> 하남시 신장1로3번길 42 (100면, 24시간 운영)<br/>
&nbsp;&nbsp;• <b>이용요금:</b> 최초 30분 600원, 추가 10분당 200원<br/>
&nbsp;&nbsp;• <b>문의:</b> 신장전통시장상인회 <a href="tel:031-794-4626" style="color:#3182ce; font-weight:bold;">031-794-4626</a> (관리자 근무 06:00~23:00)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">주차장 위치 및 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 덕풍전통시장상인회 / 신장전통시장상인회
</div>
</div>

<!-- 문화 기사 3 (2026 하남 이성산성 문화제) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🏛️ 2026.09.19~09.20 | 역사/축제</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026 하남 이성산성 문화제 《백제의 숨결, 이성산성 가을 나들이》 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"하남의 소중한 역사 유적 이성산성에서 펼쳐지는 가을 축제!"</b><br/>
하남시 대표 역사 문화 축제인 '2026 하남 이성산성 문화제'가 오는 9월 19일부터 펼쳐집니다. 이성산성 야외 투어, 어린이 백제 역사 체험, 하남 여행 버스투어 등 풍성한 가족 프로그램이 준비되어 있습니다.<br/><br/>
<b>📅 일시:</b> 2026년 9월 19일(토) ~ 9월 20일(일)<br/>
<b>📍 장소:</b> 하남 이성산성 및 하남시 주요 역사 문화 거점<br/>
<b>🏛️ 문의:</b> 하남문화재단 / 하남시 문화체육과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">축제 프로그램 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 / 하남문화재단
</div>
</div>
</div>"""

# Replace Section 4
content = re.sub(r'<div id="culture">.*?</div>\n</div>\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>', section4_content + '\n</div>\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>', content, flags=re.DOTALL)

# 6. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 하남시청 및 보건소 공공기관 주요 안내입니다.</p>

<!-- 공공기관 소식 1: 2026년 추석 명절 문 여는 병·의원 및 약국 안내 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏥 하남시보건소 | 2026.09.24~09.27</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502441" target="_blank" style="color: inherit; text-decoration: none;">2026년 추석 명절 연휴 문 여는 병·의원 및 약국 운영 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시보건소에서 2026년 추석 명절 연휴 기간 중 시민들의 응급 상황 및 의료 이용 불편을 최소화하기 위해 <b>문 여는 병·의원 및 약국(비상진료기관)</b>을 운영합니다.<br/><br/>
<b>운영 기간:</b> 2026년 9월 24일(목) ~ 9월 27일(일)<br/>
<b>확인 방법:</b><br/>
&nbsp;&nbsp;① 응급의료포털(<a href="https://www.e-gen.or.kr" target="_blank" style="color:#3182ce; font-weight:bold;">www.e-gen.or.kr</a>)에서 하남시 문 여는 의료기관/약국 검색<br/>
&nbsp;&nbsp;② 안내 콜센터 문의: 129(보건복지상담), 119(구급상황관리), 120(경기도 콜센터)<br/>
※ 방문 전 의료기관 운영 여부를 반드시 전화로 사전 확인하시기 바랍니다.
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502441" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0914-1.jpg" alt="2026년 추석 명절 문 여는 병의원 및 약국 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시보건소 보건정책과
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
</div>"""

# Replace Section 5
content = re.sub(r'<div id="public-news">.*?</div>\n</div>\n\n<!-- 하단', section5_content + '\n\n<!-- 하단', content, flags=re.DOTALL)

# 7. Update playNewsletterVideo JavaScript function
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video-yclRLijNE14') || document.getElementById('video-3BlZC9feiyw') || document.getElementById('video-9VpL5CdPQls');
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
