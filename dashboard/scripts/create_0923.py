# -*- coding: utf-8 -*-
import os
import shutil
import re

source_path = 'dashboard/news/kj_hanam_inside_20260922.html'
target_path = 'dashboard/news/kj_hanam_inside_20260923.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

img_dir = 'images'
dash_img_dir = 'dashboard/news/images'
os.makedirs(img_dir, exist_ok=True)
os.makedirs(dash_img_dir, exist_ok=True)

today_dir = os.path.join(img_dir, 'today')
for img_name in ['092301.jpg', '092302.jpg', '092303.jpg', '092304.jpg']:
    src_today = os.path.join(today_dir, img_name)
    if os.path.exists(src_today):
        shutil.copy2(src_today, os.path.join(img_dir, img_name))
        shutil.copy2(src_today, os.path.join(dash_img_dir, img_name))
    elif os.path.exists(os.path.join(img_dir, img_name)):
        shutil.copy2(os.path.join(img_dir, img_name), os.path.join(dash_img_dir, img_name))

primary_thumb = os.path.join(img_dir, 'thumbnail-923.jpg')
if os.path.exists(os.path.join(img_dir, '092304.jpg')):
    shutil.copy2(os.path.join(img_dir, '092304.jpg'), primary_thumb)
elif os.path.exists(os.path.join(img_dir, '092301.jpg')):
    shutil.copy2(os.path.join(img_dir, '092301.jpg'), primary_thumb)

if os.path.exists(primary_thumb):
    shutil.copy2(primary_thumb, os.path.join(dash_img_dir, 'thumbnail-923.jpg'))

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title, Issue Number, Date, Meta Image Tags
content = content.replace("45호 | 2026년 9월 22일 발행", "46호 | 2026년 9월 23일 발행")
content = content.replace("2026년 9월 22일 기준", "2026년 9월 23일 기준")

# Update og:image tags with thumbnail-923.jpg
og_thumb_url = "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-923.jpg?v=2026092301"
content = re.sub(r'content="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'content="{og_thumb_url}"', content)
content = re.sub(r'href="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'content="{og_thumb_url}"', content)

# 1. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 현장일지 & 언론보도 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- [현장일지 1] (네이버 블로그: 이광재, [지방재정과 수도권 교통, 새로운 접근을 찾겠습니다]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224420260387" target="_blank" style="color: inherit; text-decoration: none;">이광재, "지방재정과 수도권 교통, 새로운 접근을 찾겠습니다"… 인천 예산정책협의회 참석·광역교통 및 철도 투자 체계 개혁 촉구</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
인천시-민주당 예산정책협의회에 참석해 2006년 이후 19.24%에 고착된 지방교부세 법정률 문제와 국세 감소 시 지방재정이 함께 악화되는 구조적 한계를 지적했습니다. 아울러 서울·경기·인천을 통합하는 대도시권 광역교통체계 구축과 함께, 제5차 국가철도망 구축계획의 600조 원 과제를 기존 40조 원 예산 틀에 가두지 않고 도로·철도 모빌리티 통합 평가, 교통시설특별회계 개선, 기후대응기금 및 공단 채권 발행 등 대규모 투자와 재원 다변화로 대한민국 국토 공간 혁신을 이끌어야 한다고 강력히 촉구했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="images/092304.jpg" alt="지방재정과 수도권 교통, 새로운 접근을 찾겠습니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224420260387" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [언론보도 1] (연합뉴스: 메가성장특위, 발언하는 이광재 수석부위원장) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.yna.co.kr/view/PYH20260922014700013?input=1196m" target="_blank" style="color: inherit; text-decoration: none;">[연합뉴스] 민주당 메가성장특위 워크숍… 발언하는 이광재 수석부위원장</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 메가성장특별위원회 수석부위원장을 맡고 있는 이광재 국회의원(국회 예산결산특별위원장)이 국회 의원회관에서 열린 메가성장특위 워크숍에 참석해 대한민국 지속가능한 성장 동력 창출과 수도권-지방 상생 발전을 위한 핵심 성장 전략 및 정책 대안을 발표했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/PYH20260922014700013?input=1196m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (배재만 기자)
</div>
</div>

<!-- [언론보도 2] (머니투데이: "수소를 AI 전력 및 산업원료로…일관된 국가 에너지 정책 필요") -->
<div class="article-card card-press" style="margin-top: 16px;">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.mt.co.kr/industry/2026/09/21/2026092116481823479" target="_blank" style="color: inherit; text-decoration: none;">[머니투데이] 이광재 예결위원장 "수소를 AI 전력 및 산업원료로… 국가 에너지 대전환 준비해야"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 서울 여의도 켄싱턴호텔에서 열린 '제2회 수소경제 대토론회' 기조강연에서 "수소를 단순 연료를 넘어 국가 에너지 시스템의 핵심 축으로 확장해야 한다"며, AI 데이터센터 전력 공급, 산업 원료 전환, 재생에너지 저장 등 수소경제 생태계 조성을 위한 국가적 통합 전략의 필요성을 역설했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.mt.co.kr/industry/2026/09/21/2026092116481823479" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (머니투데이) →</a></div>
</div>
<div class="source">
📌 출처: 머니투데이 (최경민 기자)
</div>
</div>

</div>"""

# 2. Section 2: 하남 지역 주요 뉴스
section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (메트로신문: 하남시, 추석 연휴 종합대책 가동…25일 쓰레기 수거 중단) -->
<div class="article-card">
<div class="badge">📰 지방행정/추석연휴</div>
<h3><a href="https://www.metroseoul.co.kr/article/20260922500205" target="_blank" style="color: inherit; text-decoration: none;">하남시, 추석 연휴 종합대책 가동…25일 쓰레기 수거 중단</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 오는 24일부터 27일까지 나흘간 추석 연휴 종합대책을 가동합니다. 안전·물가·교통·환경·의료·급수 등 8개 분야에 80명의 인력을 배치하고 비상상황실을 운영합니다. 특히 생활쓰레기 수거는 추석 당일인 25일 하루 중단되며, 연휴 기간 비상진료 상황실 운영, 명절 성수품 물가 점검, 온누리상품권 환급 및 하머니 5% 캐시백 등 종합 민생·안전 대책을 추진합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.metroseoul.co.kr/article/20260922500205" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (메트로신문) →</a></div>
</div>
<div class="source">
📌 출처: 메트로신문 (유진채 기자)
</div>
</div>
</div>"""

# 3. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 23일 기준 하남 지역 커뮤니티(맘카페)에서 화제성과 댓글이 가장 폭발했던 HOT 이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ [추석 이슈] "추석 연휴 장보기 혜택부터 비상진료·쓰레기 배출 일정 정보 공유 맘카페 화제!"</h4>
<div class="mom-detail"><strong>현황:</strong> 추석 연휴(9.24~9.27)를 앞두고 덕풍·신장 전통시장 15% 환급 및 무료주차 혜택, 추석 당일(9.25) 쓰레기 배출 금지 안내, 연휴 기간 관내 문 여는 병의원·당직약국(응급의료포털) 리스트가 맘카페 핵심 인기 게시글로 집중 공유되고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 전통시장 온누리 15% 환급 활용 및 연휴 기간 쓰레기 배출금지(9.24~9.25)·비상진료병원 사전 확인.</div>
<div class="mom-reaction">💬 주민 반응: "전통시장 환급 혜택 덕분에 장바구니 부담 줄었어요", "아이 아플까 봐 걱정이었는데 당직 소아과 정보 공유 감사합니다" 주부들 호평 쇄도.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ [정부 정책] "2026년 저출생 반전 & 육아휴직 급여 인상 등 정부 보육 정책 확대에 부모들 관심 집중"</h4>
<div class="mom-detail"><strong>현황:</strong> 육아휴직 급여 상한액 인상, 아빠 육아휴직 인센티브 강화, 0~5세 무상보육 및 유보통합 추진 등 정부의 저출생 반전 및 맞벌이 가정 지원 정책 확대가 미사·감일·위례 맘카페 부모들 사이에서 뜨거운 이슈로 부상했습니다.</div>
<div class="mom-point">💡 주민 포인트: 육아휴직 급여 인상 조건 및 지자체 맞춤형 양육·돌봄 지원 신청 절차 사전 확인.</div>
<div class="mom-reaction">💬 주민 반응: "남편 육아휴직 사용 부담이 덜어지겠어요", "아이 키우기 좋은 환경을 만드는 실질적인 저출생 대책이 더 확대되길 기대합니다" 양육자 호평.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ [보육/육아] "하남시 육아종합지원센터 영유아 장난감 무료 대여 & 가을맞이 놀이체험 프로그램 학부모 만족도 최고!"</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 육아종합지원센터와 관내 장난감도서관에서 제공하는 영유아 맞춤형 최신 장난감 대여 서비스와 가을맞이 부모-자녀 참여 힐링 놀이 프로그램 정보가 어린 자녀를 둔 맘카페 영유아 부모들 사이에서 만족도 높은 추천 소식으로 확산되고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 육아종합지원센터 영유아 회원 등록 및 장난감도서관 지점별 대여·놀이실 예약 이용.</div>
<div class="mom-reaction">💬 주민 반응: "고가 장난감을 부담 없이 대여해서 아이가 정말 좋아해요", "주말에 아이와 함께하는 놀이 프로그램 정보 유용하네요" 초보 맘 만족도 폭발.</div>
</div>
</div>"""

# 4. Section 4: ALL IN 하남라이프
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 23일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (미사도서관: 제46회 미사초대석 <미술관에 간 심리학> 저자 문주) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📚 2026.09.30(수) 19:00 | 독서문화프로그램</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&amp;edcLctreNo=5111&amp;pageUnit=10&amp;pageIndex=1&amp;searchCnd=all" target="_blank" style="color: inherit; text-decoration: none;">하남시 미사도서관 제46회 미사초대석 &lt;미술관에 간 심리학&gt; 저자 문주 강연</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"미술 작품 속에 숨겨진 심리학의 비밀! &lt;미술관에 간 심리학&gt; 문주 작가 초청 강연"</b><br/>
하남시 미사도서관에서 9월 문화가 있는 날을 맞아 제46회 미사초대석을 개최합니다. 명화 속에 담긴 인간 심리와 감정의 결을 인문학적 시선으로 풀어내는 감동의 작가 강연에 하남시민 여러분을 초대합니다.<br/><br/>
<b>🗓 일시:</b> 2026년 9월 30일(수) 19:00 ~ 20:30<br/>
<b>📍 장소:</b> 하남시 미사도서관 4층 미사홀<br/>
<b>👥 대상:</b> 하남시민 누구나 (11세 이상, 선착순 150명)<br/>
<b>🎟 수강료:</b> 무료 (온라인 신청 접수 중)<br/>
<b>☎️ 문의:</b> 미사도서관 <a href="tel:031-790-6884" style="color:#3182ce; font-weight:bold;">031-790-6884</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&amp;edcLctreNo=5111&amp;pageUnit=10&amp;pageIndex=1&amp;searchCnd=all" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 강연 신청하기 (미사도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092303.jpg" alt="제46회 미사초대석 미술관에 간 심리학 저자 문주 강연" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 미사도서관
</div>
</div>
</div>"""

# 5. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 23일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1 (2027년 하남마을체험학교 마을체험처 모집 공고) -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏫 하남시 평생교육원 | 교육/마을학교</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52703" target="_blank" style="color: inherit; text-decoration: none;">2027년 하남마을체험학교 마을체험처 모집 공고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95; padding: 14px; border-radius: 8px;">
<b>"지역자원을 활용한 하남 학생 맞춤형 학교 안·밖 교육! 2027년 마을체험처 모집"</b><br/>
하남미래교육협력지구 마을체험학교를 통해 지역자원을 활용한 다양한 교육 프로그램을 학생들에게 제공하고자 2027년 마을체험학교 체험처를 모집합니다.<br/><br/>
<b>🗓 모집기간:</b> 2026년 9월 22일(화) ~ 10월 8일(목)<br/>
<b>👥 모집대상:</b> 교육 운영이 가능한 하남시 소재 민간단체 및 법인 등<br/>
<b>📚 모집분야:</b> 역사, 인문, 문화, 디지털, 진로 (5개 분야)<br/>
<b>📞 문의:</b> 하남시 평생교육원 평생교육과 <a href="tel:031-790-5357" style="color:#3182ce; font-weight:bold;">031-790-5357</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52703" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시청 고시공고) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 평생교육원 (평생교육과)
</div>
</div>

<!-- 공공기관 소식 2 (하남 교산지구 자족용지 핵심 타깃기업 발굴 용역 제안서 평가위원 모집) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏢 하남시청 | 투자유치/교산신도시</div>
<h3><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52650" target="_blank" style="color: inherit; text-decoration: none;">「하남 교산지구 자족용지 핵심 타깃기업 발굴 용역」 제안서 평가위원(후보자) 모집 공고</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95; padding: 14px; border-radius: 8px;">
<b>"교산신도시 자족용지 우수 기업 유치를 위한 전문가 제안서 평가위원 모집!"</b><br/>
하남시에서 추진하는 「하남 교산지구 자족용지 핵심 타깃기업 발굴 용역」 수행업체 선정과 관련하여 전문성과 경험을 갖춘 제안서 평가위원(후보자)을 모집합니다.<br/><br/>
<b>🗓 모집기간:</b> 2026년 9월 22일(화) ~ 10월 8일(목) 18:00까지<br/>
<b>💼 모집분야:</b> 기업투자유치, 산업·지역경제, 경영·기업전략, 도시계획·개발 (4개 분야)<br/>
<b>👥 모집인원:</b> 21명 (평가위원 구성인원의 3배수)<br/>
<b>📞 문의:</b> 하남시청 투자유치과 <a href="tel:031-5182-1441" style="color:#3182ce; font-weight:bold;">031-5182-1441</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/sosik/selectGosiData.do?key=10055&amp;not_ancmt_se_code=01,04&amp;not_ancmt_mgt_no=52650" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시청 고시공고) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 (투자유치과)
</div>
</div>

<!-- 공공기관 소식 3 (하남시정신건강복지센터: 2026 노인우울예방프로그램 활력충전 청춘스텝 모집) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🧠 하남시정신건강복지센터 | 보건/복지</div>
<h3><a href="http://cmhc.co.kr/sub.php?menukey=39&amp;mode=view&amp;idx=133" target="_blank" style="color: inherit; text-decoration: none;">2026 노인우울예방프로그램 &lt;활력충전ㆍ청춘스텝&gt; 참가자 모집</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95;">
<div style="flex: 1;">
<b>"어르신들의 활기찬 일상과 마음건강 회복을 돕는 우울예방 힐링 프로그램!"</b><br/>
하남시정신건강복지센터에서 관내 어르신들을 대상으로 정서적 안정과 우울감 해소를 위한 &lt;활력충전ㆍ청춘스텝&gt; 프로그램을 운영하오니 많은 신청 바랍니다.<br/><br/>
<b>🗓 일시:</b> 2026년 10월 2일 ~ 11월 2일 (매주 10:30 ~ 12:30)<br/>
<b>📍 장소:</b> 미사보건센터 2층 대강당<br/>
<b>👥 모집인원:</b> 선착순 30명<br/>
<b>🗓 접수기간:</b> 2026년 9월 15일(화) ~ 9월 28일(월) 17:00까지<br/>
<b>📞 문의:</b> 하남시정신건강복지센터 <a href="tel:031-794-6508" style="color:#3182ce; font-weight:bold;">031-794-6508</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="http://cmhc.co.kr/sub.php?menukey=39&amp;mode=view&amp;idx=133" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 교육 신청하기 (하남시정신건강복지센터) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092301.jpg" alt="2026 노인우울예방프로그램 활력충전 청춘스텝 모집" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시정신건강복지센터
</div>
</div>"""

# Combine all 5 sections cleanly
all_sections_content = (
    section1_content + '\n<hr/>\n' +
    section2_content + '\n<hr/>\n' +
    section3_content + '\n\n' +
    section4_content + '\n\n' +
    section5_content + '\n\n'
)

idx_lawmaker = content.find('<div id="lawmaker">')
idx_bottom = content.find('<div class="bottom-nav"')

content = content[:idx_lawmaker] + all_sections_content + content[idx_bottom:]

# Update visitor counter path ID to 0923
content = content.replace("lee-kwang-jae.news_letter.0922", "lee-kwang-jae.news_letter.0923")

# Save target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {target_path}")

# Save to news_index_path & root_index_path
with open(news_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {news_index_path}")

with open(root_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {root_index_path}")
