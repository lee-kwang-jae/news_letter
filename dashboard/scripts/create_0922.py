# -*- coding: utf-8 -*-
import os
import shutil
import re

source_path = 'dashboard/news/kj_hanam_inside_20260921.html'
target_path = 'dashboard/news/kj_hanam_inside_20260922.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

img_dir = 'images'
dash_img_dir = 'dashboard/news/images'
os.makedirs(img_dir, exist_ok=True)
os.makedirs(dash_img_dir, exist_ok=True)

primary_thumb = os.path.join(img_dir, 'thumbnail-922.jpg')
if not os.path.exists(primary_thumb):
    primary_thumb = os.path.join(img_dir, 'today', 'thumbnail-922.jpg')

if os.path.exists(primary_thumb):
    dst1 = os.path.join(img_dir, 'thumbnail-922.jpg')
    dst2 = os.path.join(dash_img_dir, 'thumbnail-922.jpg')
    if os.path.abspath(primary_thumb) != os.path.abspath(dst1):
        shutil.copy2(primary_thumb, dst1)
    shutil.copy2(primary_thumb, dst2)

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title, Issue Number, Date, Meta Image Tags
content = content.replace("44호 | 2026년 9월 21일 발행", "45호 | 2026년 9월 22일 발행")
content = content.replace("2026년 9월 21일 기준", "2026년 9월 22일 기준")

# Update og:image tags with thumbnail-922.jpg
og_thumb_url = "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-922.jpg?v=2026092201"
content = re.sub(r'content="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'content="{og_thumb_url}"', content)
content = re.sub(r'href="https://lee-kwang-jae\.github\.io/news_letter/images/[^"]*"', f'href="{og_thumb_url}"', content)
content = content.replace('content="1200"', 'content="996"')
content = content.replace('content="630"', 'content="555"')

# 1. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 현장일지 & 언론보도 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- [현장일지 1] (네이버 블로그: 이광재, [국회에서 600조와 40조 이야기를 했습니다]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224418485113" target="_blank" style="color: inherit; text-decoration: none;">이광재, "국회에서 600조와 40조 이야기를 했습니다"… 제5차 국가철도망 구축계획 대규모 투자·제도 개혁 촉구</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
오늘 아침 국회에서 철도 이야기를 했습니다. 전국 지방정부가 건의한 제5차 국가철도망 구축계획 신규 사업 규모는 600조 원에 달하지만, 40조 원 수준의 기존 정부 예산 틀에 매여 있어서는 안 됩니다. AI 시대를 맞아 대한민국을 '반나절 생활권'으로 묶고 국토 공간 혁명을 이루기 위해 철도망에 대한 대규모 투자 확대와 함께 낡은 예산 편성 및 예비타당성조사 체계의 전면 개편을 촉구했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="images/thumbnail-922.jpg" alt="국회에서 600조와 40조 이야기를 했습니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224418485113" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [언론보도 1] (조선비즈: [인터뷰] 이광재 예결위원장 "아이 태어나면 나라가 1억씩 펀드 넣어주자") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://biz.chosun.com/policy/politics/assembly/2026/09/21/S6XVYFVPXZD7VFATJ6AIC2G664/?utm_source=naver&amp;utm_medium=original&amp;utm_campaign=biz" target="_blank" style="color: inherit; text-decoration: none;">[인터뷰] 이광재 예결위원장 "아이 태어나면 나라가 1억씩 펀드 넣어주자"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회 예산결산특별위원장이 조선비즈와의 인터뷰에서 "아이가 태어나면 나라가 1억 원을 국부펀드에 넣어 굴린 뒤 청년 사회 진출 자금(3억8천만 원)과 노후 자금을 제공하는 방안을 제안한다"고 밝혔습니다. 이 위원장은 "국가는 소비자가 아니라 투자자여야 하며, 국가 자산이 국민의 집과 일자리, 교육으로 연결되도록 예결위 심사의 기준을 '생산성'과 '지속가능성'에 두겠다"고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://biz.chosun.com/policy/politics/assembly/2026/09/21/S6XVYFVPXZD7VFATJ6AIC2G664/?utm_source=naver&amp;utm_medium=original&amp;utm_campaign=biz" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (조선비즈) →</a></div>
</div>
<div class="source">
📌 출처: 조선비즈 (송복규·이건 기자)
</div>
</div>


</div>"""

# Slice replace Section 1
idx_lawmaker = content.find('<div id="lawmaker">')
idx_local = content.find('<div id="local-news">')
content = content[:idx_lawmaker] + section1_content + '\n<hr/>\n' + content[idx_local:]

# 2. Section 2: 하남 지역 주요 뉴스
section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (스포츠동아: 하남시의회, 추석 앞두고 전통시장서 ‘민생 현장 챙겨’) -->
<div class="article-card">
<div class="badge">📰 의정/전통시장</div>
<h3><a href="https://sports.donga.com/region/article/all/20260921/134712269/1" target="_blank" style="color: inherit; text-decoration: none;">하남시의회, 추석 앞두고 전통시장서 ‘민생 현장 챙겨’</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시의회가 추석 명절을 앞두고 관내 덕풍·신장전통시장과 석바대 토성로 상점가를 찾아 지역 상권 활성화와 소상공인 지원을 위한 민생 행보에 나섰습니다. 시의원 10명 전원이 장보기에 참여해 제수용품과 명절 물품을 구매하고 상인들의 애로사항을 청취하며 전통시장 이용 및 가치 소비를 적극 독려했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://sports.donga.com/region/article/all/20260921/134712269/1" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (스포츠동아) →</a></div>
</div>
<div class="source">
📌 출처: 스포츠동아 (고성철 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (디스커버리뉴스: 정병용 하남시의장, 전동킥보드 면허인증 의무화 등 제도 정비 촉구) -->
<div class="article-card">
<div class="badge">📰 교통/안전</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1102214" target="_blank" style="color: inherit; text-decoration: none;">정병용 하남시의장, 전동킥보드 면허인증 의무화 등 제도 정비 촉구</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
청소년 무면허 운전과 보행자 안전 사고가 급증하는 개인형 이동장치(PM) 관리체계 구축을 위해 정병용 하남시의회 의장이 대표발의한 '개인형 이동수단 안전 법안 조속 통과 촉구 건의안'이 의회에서 만장일치로 의결되었습니다. 대여 사업자 면허인증 의무화, 최고속도 하향, 주정차 위반 견인 등 국회 차원의 실효적 법 제정을 강력 촉구했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1102214" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (아주경제: 오민용 경기도의원·하남시 학교운영협의회, 한국디지털미디어고 방문...하남시 미래교육 발전방안 모색) -->
<div class="article-card">
<div class="badge">📰 교육/미래</div>
<h3><a href="https://www.ajunews.com/view/20260921164055712" target="_blank" style="color: inherit; text-decoration: none;">오민용 경기도의원·하남시 학교운영협의회, 한국디지털미디어고 방문… 하남시 미래교육 발전방안 모색</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
오민용 경기도의원(더불어민주당·하남1)이 하남시 학교운영협의회 및 학부모회 회장단과 함께 IT 특성화 고교인 한국디지털미디어고등학교를 방문했습니다. 첨단 교육시설과 학생 맞춤형 IT 교육 시스템을 기획 점검하며, 교산신도시 개발에 발맞춘 하남시 미래형 IT 특성화 교육 인프라 유치 및 발전 방안을 긴밀히 모색했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.ajunews.com/view/20260921164055712" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (아주경제) →</a></div>
</div>
<div class="source">
📌 출처: 아주경제 (강대웅 기자)
</div>
</div>
</div>"""

# Slice replace Section 2
idx_local = content.find('<div id="local-news">')
idx_mom = content.find('<div id="mom-cafe">')
content = content[:idx_local] + section2_content + '\n<hr/>\n' + content[idx_mom:]

# 3. Section 3: 하남 맘카페 HOT 이슈
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 22일 기준 하남 지역 커뮤니티(맘카페)에서 화제성과 댓글이 가장 폭발했던 HOT 이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ "국회에서 600조 철도망 외친 이광재 의원! 교산 3호선·GTX-D 하남 연장 기대감 UP"</h4>
<div class="mom-detail"><strong>현황:</strong> 이광재 의원이 국회에서 제5차 국가철도망 구축계획의 대규모 투자 확대와 예타 개편을 촉구하며 600조 원대 전국 지방정부 철도망 과제를 강조함에 따라 하남 미사·교산 주민들 사이에서 3호선 연장 및 GTX-D 하남 연결 기대감이 크게 높아졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 40조 원 기존 예산 틀을 넘어선 국가 철도망 대규모 투자를 통한 하남 교통 숙원사업 촉진.</div>
<div class="mom-reaction">💬 주민 반응: "교산신도시 입주 전 철도 개통이 진정한 출퇴근 혁명이죠", "이광재 의원님 예결위원장 파워로 하남 철도망 예산 팍팍 챙겨주세요!" 맘카페 뜨거운 응원.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ "학원가 전동킥보드 2인 탑승 위험천만! 하남시의회 면허인증 의무화 촉구에 맘카페 '격하게 공감'"</h4>
<div class="mom-detail"><strong>현황:</strong> 미사강변도시 및 감일지구 학원가·초중고 인근에서 청소년들의 전동킥보드 무면허 및 2인 탑승 위험 운행이 늘어나자, 하남시의회가 대여 사업자 면허인증 의무화와 속도 제한을 담은 안전 법안 통과 촉구 건의안을 만장일치 의결했다는 소식에 맘카페에서 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 킥보드 면허인증 의무화, 최고속도 하향 및 아파트·학원가 보행 안전 확보.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 학원 하원길 킥보드 쌩쌩 달릴 때마다 아찔했는데 국회 법안 꼭 통과되길!", "무면허 청소년 대여 차단이 최우선입니다" 맘카페 열띤 지지.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "추석 연휴 아이 아플 때 어디 가나요? 하남시 추석 문 여는 병원·약국 정보 공유"</h4>
<div class="mom-detail"><strong>현황:</strong> 9월 24일부터 시작되는 추석 연휴를 앞두고 미사·감일·위례 맘카페에서 연휴 기간 진료하는 소아과, 병의원, 당직 약국 정보와 응급의료포털 이용 팁 공유글이 쇄도하고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 추석 연휴(9.24~9.27) 관내 비상진료 병의원 및 약국 사전 확인 필수.</div>
<div class="mom-reaction">💬 주민 반응: "명절 연휴 소아과 여는 곳 리스트 미리 저장해둬야 마음이 놓여요", "119나 응급의료포털(e-gen) 앱 켜두면 요용하네요" 정보 공유 붐.</div>
</div>
</div>"""

# 4. Section 4: ALL IN 하남라이프
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 22일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (하남문화재단 기획공연: 안중근, 천국에서의 춤 - 스페셜 발레 갈라) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🩰 2026.09.30(수) 19:30 | 문화가 있는 날 기획공연</div>
<h3 style="margin-top: 6px;"><a href="https://www.hnart.or.kr/artcenter/showView.do?key=183&amp;programId=artcenter&amp;shNo=3456&amp;cal=1" target="_blank" style="color: inherit; text-decoration: none;">하남문화재단 기획공연 &lt;안중근, 천국에서의 춤 - 스페셜 발레 갈라&gt; 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"안중근 의사의 영웅적 삶과 자유를 향한 열정을 그려낸 감동의 발레 갈라 무대!"</b><br/>
하남문화예술회관 대극장(검단홀)에서 대한민국 대표 발레 무용수들과 함께하는 기획공연이 펼쳐집니다. 9월 문화가 있는 날을 맞아 전석 1만 원 특별 할인 혜택으로 시민들을 찾아갑니다.<br/><br/>
<b>🗓 일시:</b> 2026년 9월 30일(수) 19:30 (90분간)<br/>
<b>📍 장소:</b> 하남문화예술회관 대극장(검단홀)<br/>
<b>🎟 티켓:</b> 전석 10,000원 (문화가 있는 날 특별가)<br/>
<b>👥 관람연령:</b> 초등학생 이상 관람가<br/>
<b>☎️ 문의:</b> 하남문화재단 <a href="tel:031-790-7979" style="color:#3182ce; font-weight:bold;">031-790-7979</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hnart.or.kr/artcenter/showView.do?key=183&amp;programId=artcenter&amp;shNo=3456&amp;cal=1" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 티켓 예매하기 (하남문화예술회관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092201.jpg" alt="안중근, 천국에서의 춤 스페셜 발레 갈라" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남문화재단 (하남문화예술회관)
</div>
</div>
</div>"""

# 5. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 22일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1 (하남시가족센터 가족상담 신청 안내) -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏠 하남시가족센터 | 가족/상담</div>
<h3><a href="https://hanam.familynet.or.kr/center/lay1/program/S295T322C449/receipt/view.do?seq=192310" target="_blank" style="color: inherit; text-decoration: none;">[연중사업] 2026년 하남시가족센터 가족상담 신청 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95;">
<div style="flex: 1;">
<b>"개인·부부·가족의 건강한 소통과 관계 회복을 위한 전문 상담 지원!"</b><br/>
하남시가족센터에서 하남시민을 대상으로 무료 가족상담(개인·부부·가족상담)을 연중 운영합니다. 전문가와의 1:1 맞춤형 상담을 통해 삶의 고민을 해결하고 건강한 가족 관계 형성을 도와드립니다.<br/><br/>
<b>👥 대상:</b> 상담이 필요한 개인, 부부, 가족(구성원 2인 이상)<br/>
<b>💰 비용:</b> 무료 (개인상담 6회기 / 부부·가족상담 10회기)<br/>
<b>📍 장소:</b> 하남시가족센터 4층 상담실 (경기 하남시 신장동로 15)<br/>
<b>📞 문의:</b> 가족상담사례팀 <a href="tel:070-4128-3341" style="color:#3182ce; font-weight:bold;">070-4128-3341</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://hanam.familynet.or.kr/center/lay1/program/S295T322C449/receipt/view.do?seq=192310" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (하남시가족센터) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092202.jpg" alt="2026년 하남시가족센터 가족상담 신청 안내" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시가족센터
</div>
</div>

<!-- 공공기관 소식 2 (하남시청 자원순환과: 2026년 추석 연휴 생활폐기물 배출 및 수거일정 안내) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🗑️ 하남시청 | 생활/환경</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502524" target="_blank" style="color: inherit; text-decoration: none;">2026년 추석 연휴 생활폐기물 배출 및 수거일정 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid #e9d5ff; color: #4c1d95;">
<div style="flex: 1;">
<b>"추석 당일(9.25.) 생활쓰레기 수거 휴무! 배출금지 시간을 확인하세요"</b><br/>
하남시에서 추석 연휴 기간 쾌적한 도시환경 조성을 위해 생활폐기물 수거 일정을 안내합니다. 추석 당일인 9월 25일(금)은 수거 작업이 휴무되오니 주민께서는 배출금지 기간을 준수해 주시기 바랍니다.<br/><br/>
<b>🚫 배출금지 기간:</b> 2026년 9월 24일(목) ~ 9월 25일(금) 18:00까지<br/>
<b>🚛 수거 재개:</b> 2026년 9월 25일(금) 저녁 6시 이후 정상 배출<br/>
<b>📞 문의처:</b> 하남시청 자원순환과 <a href="tel:031-790-6251" style="color:#3182ce; font-weight:bold;">031-790-6251</a> / 콜센터 <a href="tel:031-790-6114" style="color:#3182ce; font-weight:bold;">031-790-6114</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502524" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 보기 (하남시청 누리집) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092203.jpg" alt="2026년 추석 연휴 생활폐기물 배출 및 수거일정 안내" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 (자원순환과)
</div>
</div>
</div>"""

# Slice replace Section 3, Section 4 & Section 5
# Re-find idx_mom dynamically after previous replacements
idx_mom = content.find('<div id="mom-cafe">')
idx_bottom = content.find('<div class="bottom-nav"')
content = content[:idx_mom] + section3_content + '\n\n' + section4_content + '\n\n' + section5_content + '\n\n' + content[idx_bottom:]

# Update visitor counter path ID to 0922
content = content.replace("lee-kwang-jae.news_letter.0921", "lee-kwang-jae.news_letter.0922")

# Remove visitor counter element from footer if present
content = re.sub(r'<div style="margin-top: 2px; text-align: center;">\s*<span[^>]*><span id="visitor_counter_val">.*?</span></span>\s*</div>', '', content, flags=re.DOTALL)

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
