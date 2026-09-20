# -*- coding: utf-8 -*-
import os
import shutil
import re

source_path = 'dashboard/news/kj_hanam_inside_20260918.html'
target_path = 'dashboard/news/kj_hanam_inside_20260921.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

# Copy image aliases to ensure availability across root & dashboard directories
img_dir = 'images'
dash_img_dir = 'dashboard/news/images'
os.makedirs(img_dir, exist_ok=True)
os.makedirs(dash_img_dir, exist_ok=True)

# Thumbnail aliases for 0921 (Representative thumbnail: thumbnail-092100.jpg)
primary_thumb = os.path.join(img_dir, 'thumbnail-092100.jpg')
if not os.path.exists(primary_thumb):
    primary_thumb = os.path.join(img_dir, 'thumbnail-921.jpg')

if os.path.exists(primary_thumb):
    aliases = ['thumbnail-092100.jpg', 'thumbnail-0921.jpg', 'thumbnail0921.jpg', 'thumbnail-921.jpg', '09.jpg']
    for alias in aliases:
        dst1 = os.path.join(img_dir, alias)
        dst2 = os.path.join(dash_img_dir, alias)
        if primary_thumb != dst1:
            shutil.copy2(primary_thumb, dst1)
        shutil.copy2(primary_thumb, dst2)

shorts_poster = os.path.join(img_dir, 'shorts_0921_poster.jpg')
if os.path.exists(shorts_poster):
    shutil.copy2(shorts_poster, os.path.join(dash_img_dir, 'shorts_0921_poster.jpg'))

img_092101 = os.path.join(img_dir, '092101.jpg')
if os.path.exists(img_092101):
    shutil.copy2(img_092101, os.path.join(dash_img_dir, '092101.jpg'))

img_092102 = os.path.join(img_dir, '092102.jpg')
if os.path.exists(img_092102):
    shutil.copy2(img_092102, os.path.join(dash_img_dir, '092102.jpg'))

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title, Issue Number, Date, Meta Image Tags
content = content.replace("43호 | 2026년 9월 18일 발행", "44호 | 2026년 9월 21일 발행")
content = content.replace("2026년 9월 18일 기준", "2026년 9월 21일 기준")
content = content.replace("images/thumbnail-0918.jpg", "images/thumbnail-092100.jpg")
content = content.replace("images/thumbnail-918.jpg", "images/thumbnail-092100.jpg")
content = content.replace("images/thumbnail-0921.jpg", "images/thumbnail-092100.jpg")
content = content.replace("https://lee-kwang-jae.github.io/news_letter/images/thumbnail-0918.jpg", "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-092100.jpg")
content = content.replace("https://lee-kwang-jae.github.io/news_letter/images/thumbnail-0921.jpg", "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-092100.jpg")

# 1. Section 1: 우리동네 국회의원 이광재 (현장일지 선배치 + 언론보도 후배치 지침 준수)
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 현장일지 & 언론보도 ===== -->
<div id="lawmaker">
<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>

<!-- [현장일지 1] (네이버 블로그: 이광재, [한강변에 기후부 장관님과 갔습니다]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224416869021" target="_blank" style="color: inherit; text-decoration: none;">이광재, "한강변에 기후부 장관님과 함께 갔습니다"… 미사 한강변 폐천부지·선동둔치 점검 현장</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
어제 미사 한강변을 김성환 기후에너지환경부 장관, 김용만 국회의원과 함께 걸으며 하남시와 정부 간 소송으로 방치되어온 폐천부지 현장을 점검했습니다. "누가 잘못했나"보다 "언제 깨끗해지나"라는 시민들의 요구에 따라 책임 가리기와 땅 살리기를 동시에 추진할 것을 장관께 제안했습니다. 이어 선동둔치 파크골프장을 방문해 어르신들의 소통 현장을 살피며, 한강이 하남시민이 매일 누리는 공간이 되도록 현장에서 답을 찾겠습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="images/thumbnail-092100.jpg" alt="한강변에 기후부 장관님과 갔습니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224416869021" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [현장일지 2] (네이버 블로그: 이광재, [이번 주말 하남 종주기 — 걷고, 탁구 치고, 장 보고]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224417244785" target="_blank" style="color: inherit; text-decoration: none;">이광재, "이번 주말 하남 종주기 — 걷고, 탁구 치고, 장 보고"… 시민과 함께한 생생 현장</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
주말 하남 곳곳을 누비며 하남시민 여러분을 만났습니다. '위례길사람들'과 함께 검단산과 한강변 산책길을 걸으며 소통하고, 생활체육 탁구 동호인분들과 함께 땀방울을 나누었으며, 한가위를 맞아 전통시장에서 명절 장을 보았습니다. 현장에서 따뜻하게 건네주시는 시민들의 목소리를 의정활동에 꼼꼼히 반영하겠습니다.
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224417244785" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>

<!-- [현장일지 3] (유튜브 숏폼 영상: 최대 권력 도시계획권 & 국공유지 발굴 현장) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">이광재, "최대 권력은 도시계획권… 숨어있는 국공유지를 찾자" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-HHx77yzsWrY" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-HHx77yzsWrY" poster="images/shorts_0921_poster.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="images/shorts_0921.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/HHx77yzsWrY?feature=oembed" title="이광재, &quot;최대 권력은 도시계획권… 숨어있는 국공유지를 찾자&quot; 현장 숏폼" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://youtube.com/shorts/HHx77yzsWrY" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 유튜브 (이광재 TV / 광재일하남)
</div>
</div>

<!-- [언론보도 1] (전자신문: 추미애 경기지사, 민주당과 첫 예산정책협의) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.etnews.com/20260919000008" target="_blank" style="color: inherit; text-decoration: none;">추미애 경기지사, 민주당과 첫 예산정책협의… 철도·반도체 국비 확대 건의 예정</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
추미애 경기도지사가 오는 21일 오전 경기도북부청사에서 민선 9기 첫 경기도-더불어민주당 예산정책협의회를 열고 지방재정 제도 개선과 철도·반도체 등 주요 현안, 10개 사업의 국비 확보 방안을 논의합니다. 당에서는 김민석 민주당 대표, 한병도 원내대표, 한정애 사무총장, 권칠승 정책위의장, 이광재 국회 예산결산특별위원장, 서영석 경기도당위원장 등이 참석해 경기도 주요 현안과 예산 협력 방안을 논의할 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.etnews.com/20260919000008" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (전자신문) →</a></div>
</div>
<div class="source">
📌 출처: 전자신문 (김동성 기자)
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

<!-- 지역 뉴스 기사 1 (시민의소리: 하남시학교밖청소년지원센터, 2026년 검정고시 85명 최종 합격) -->
<div class="article-card">
<div class="badge">📰 교육/청소년</div>
<h3><a href="https://www.siminsori.com/news/articleView.html?idxno=401618" target="_blank" style="color: inherit; text-decoration: none;">하남시학교밖청소년지원센터, 2026년 검정고시 85명 최종 합격</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시학교밖청소년지원센터('꿈드림')는 2026년 검정고시를 통해 학교 밖 청소년 85명이 최종 합격했다고 밝혔습니다. 센터는 1:1 학습 멘토링, 검정고시 대비반, 교재 지원 등 맞춤형 서비스를 제공해 청소년들의 학업 복귀와 자립을 적극 지원하고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.siminsori.com/news/articleView.html?idxno=401618" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시민의소리) →</a></div>
</div>
<div class="source">
📌 출처: 시민의소리 (김창현 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (스포츠동아: 하남시, 이사 후 '주소일괄정정' 신청 주의 당부) -->
<div class="article-card">
<div class="badge">📰 행정/시정</div>
<h3><a href="https://sports.donga.com/region/article/all/20260920/134703974/1" target="_blank" style="color: inherit; text-decoration: none;">하남시, 이사 후 '주소일괄정정' 신청 주의 당부</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시는 이사 후 카드사·통신사 등에 등록된 주소를 변경하려는 시민들에게 정부24의 '주소일괄정정' 민원을 잘못 신청하지 않도록 주의를 당부했습니다. '주소일괄정정'은 건물 도로명주소 변경 시 사용하는 행정 서비스로, 카드나 통신사 주소 변경은 별도의 금융·통신 주소이전 통합서비스를 이용해야 합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://sports.donga.com/region/article/all/20260920/134703974/1" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (스포츠동아) →</a></div>
</div>
<div class="source">
📌 출처: 스포츠동아 (고성철 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (기호일보: 하남시, 추석 연휴 24일부터 나흘간 공영주차장 무료 개방) -->
<div class="article-card">
<div class="badge">📰 교통/복지</div>
<h3><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035290" target="_blank" style="color: inherit; text-decoration: none;">하남시, 추석 연휴 24일부터 나흘간 공영주차장 무료 개방</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 추석을 맞아 귀성객과 시민들의 주차 편의를 높이고 전통시장 및 인근 상권을 활성화하기 위해 9월 24일부터 27일까지 나흘간 관내 공영주차장을 무료로 개방합니다. 또한 전통시장 주변 도로의 불법 주정차 단속을 한시적으로 유예하여 명절 장보기 편의를 대폭 지원합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035290" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (기호일보) →</a></div>
</div>
<div class="source">
📌 출처: 기호일보 (이홍재 기자)
</div>
</div>
</div>"""

# Slice replace Section 2
idx_local = content.find('<div id="local-news">')
idx_mom = content.find('<div id="mom-cafe">')
content = content[:idx_local] + section2_content + '\n<hr/>\n' + content[idx_mom:]

# 3. Section 3: 하남 맘카페 HOT 이슈 (2026년 9월 21일 기준 전면 교체 - 이광재 포함)
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 21일 기준 하남 지역 커뮤니티(맘카페)에서 화제성과 댓글이 가장 폭발했던 HOT 이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ "방치된 미사 한강변 폐천부지 드디어 깨끗해지나요?" 이광재 의원·기후부 장관 현장 점검 소식에 맘카페 '기대감 뿜뿜'</h4>
<div class="mom-detail"><strong>현황:</strong> 이광재 국회의원이 김성환 기후에너지환경부 장관과 함께 미사 한강변 방치된 폐천부지와 선동둔치 파크골프장 현장을 찾아 하남시와 정부의 소송 갈등을 풀고 시민들을 위한 힐링 공간으로 가꾸겠다는 소식이 전달되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 정부-지자체 소송 갈등으로 방치된 한강변 폐천부지 정비 및 시민 친화 공간 재탄생 추진.</div>
<div class="mom-reaction">💬 주민 반응: "누가 잘못했나 다투는 것보다 언제 깨끗해지나 궁금했는데 반가운 소식이네요!", "아이들과 미사 한강변 산책하기 더 좋은 힐링 명소로 잘 정비되면 좋겠습니다" 맘카페 큰 호응.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ "초등 저학년까지 아동수당 늘어나나요?" 정부 양육 지원 정책 발표에 맘카페 '초집중'</h4>
<div class="mom-detail"><strong>현황:</strong> 정부가 가계 양육 부담 경감을 위해 아동수당 지급 대상을 확대하고 영유아·초등 돌봄 지원을 강화하는 정부 정책 방향을 발표함에 따라, 하남 지역 육아맘들 사이에서 혜택 범위와 신청 시기에 대한 정보 공유가 활발히 이루어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 정부의 아동수당 지급 연령 확대 및 맞벌이 가구 돌봄 지원 강화 정책 발표.</div>
<div class="mom-reaction">💬 주민 반응: "초등학생 자녀 둔 가정까지 지원이 늘어난다니 정부 정책 반갑네요!", "맞벌이 돌봄 부담도 한결 덜 수 있으면 좋겠습니다" 맘카페 높은 관심.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "K-스타월드 추진 vs 교통·환경 대책 먼저!" 미사섬 개발 놓고 맘카페 갑론을박</h4>
<div class="mom-detail"><strong>현황:</strong> 하남 미사섬 K-스타월드(대형 공연장·스튜디오) 개발 사업 추진을 둘러싸고, 지역 자족도시 발전 기대감과 미사강변도시 교통 체증 및 환경 훼손 우려 목소리가 맘카페에서 팽팽하게 맞서며 hot한 지역 현안 논쟁이 벌어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: K-스타월드 개발 추진에 따른 하남 경제 활성화 기대 vs 미사 교통난·환경 대책 우선 수립 논쟁.</div>
<div class="mom-reaction">💬 주민 반응: "세계적 공연장과 기업이 들어와야 하남 가치가 올라간다" vs "지금도 출퇴근길 막히는데 교통 대책 없는 개발은 반대다" 주민 간 열띤 대립.</div>
</div>
</div>"""

# 4. Section 4: ALL IN 하남라이프 (하남시 공지사항 - 전국 소등행사 교체)
section4_content = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 21일 기준 한눈에 보는 하남시 최신 문화·행사·교육 안내 가이드</p>

<!-- 문화 기사 1 (하남시 공지사항: 전국 소등행사 안내) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">💡 매월 22일 21:00 (10분간) | 환경/시민참여</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502793" target="_blank" style="color: inherit; text-decoration: none;">매월 22일 밤 9시 '전국 소등행사' 안내 (불이 꺼진 자리, 별이 켜지는 시간)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"지구를 위한 10분간의 짧은 불끄기! 일상 속 기후행동에 함께해주세요"</b><br/>
기후에너지환경부와 하남시에서는 대국민 기후행동 실천을 유도하기 위해 매월 22일 밤 9시 10분간 소등행사를 정례화하여 추진합니다.<br/><br/>
<b>🗓 일시:</b> 매월 22일 21:00 ~ 21:10 (10분간)<br/>
<b>💡 참여 방법:</b> 실내외 불필요한 조명 소등하기<br/>
<b>👥 참여 대상:</b> 하남시민 누구나<br/>
<b>☎️ 문의:</b> 하남시청 환경정책과 <a href="tel:031-790-5586" style="color:#3182ce; font-weight:bold;">031-790-5586</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502793" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 시청 공고 보기 →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092101.jpg" alt="전국 소등행사 안내" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 (환경정책과)
</div>
</div>

<!-- 문화 기사 2 (하남시 나룰도서관 도서 재활용 이벤트 <다시봄>) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795; margin-top: 16px;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📖 2026.09.19~ | 도서관/시민나눔</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanamlib.go.kr/nalib/selectBbsNttView.do?key=76&amp;bbsNo=6&amp;nttNo=89864" target="_blank" style="color: inherit; text-decoration: none;">하남시 나룰도서관 도서 재활용 이벤트 &lt;다시봄&gt; 운영 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"도서의 가치를 다시 잇다! 나룰도서관 폐기 예정 도서 시민 무료 나눔"</b><br/>
하남시 나룰도서관에서 폐기 예정인 도서를 하남시립도서관 정회원 시민 여러분께 무료로 배부합니다.<br/><br/>
<b>🗓 배부 일시:</b> 2026년 9월 19일(토) ~ (10:00 ~ 18:00)<br/>
<b>👥 참여 대상:</b> 하남시립도서관 정회원 (1인당 3권 수령)<br/>
<b>📍 배부 장소:</b> 나룰도서관 1층 로비<br/>
<b>💳 준비물:</b> 하남시립도서관 회원증
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/nalib/selectBbsNttView.do?key=76&amp;bbsNo=6&amp;nttNo=89864" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 공고 보기 (나룰도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="images/092102.jpg" alt="나룰도서관 도서 재활용 이벤트 다시봄" style="width: 100%; height: auto; max-height: 260px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 나룰도서관
</div>
</div>
</div>"""

# 5. Section 5: 공공기관 소식지
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 21일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1 (하남도시공사 초이동 거주자우선주차장 정기권 모집) -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🚗 하남도시공사 | 공고 제2026-126호</div>
<h3><a href="https://www.huic.co.kr/www/selectBbsNttView.do?key=102&amp;bbsNo=36&amp;nttNo=11518" target="_blank" style="color: inherit; text-decoration: none;">초이동 거주자우선주차장 순환배정 정기권 모집 공고 (하남도시공사 공고 제2026-126호)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
하남도시공사에서는 공영주차장 정기권 이용 기회의 편중을 완화하고 공정한 이용 기회를 제공하기 위해 2027년 1월 1일부터 2년 주기 순환배정제로 전환됨에 따라, 초이동 78-4번지 일원 거주자우선주차장 정기권 이용자를 모집합니다.<br/><br/>
<b>📍 위치:</b> 경기도 하남시 초이동 78-4번지 일원 (초이동 거주자우선주차장)<br/>
<b>📋 운영 방식:</b> 2027. 1. 1.부터 2년 주기 순환배정제 전환에 따른 모집<br/>
<b>📞 문의처:</b> 하남도시공사 대표전화 <a href="tel:031-790-9500" style="color:#3182ce; font-weight:bold;">031-790-9500</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.huic.co.kr/www/selectBbsNttView.do?key=102&amp;bbsNo=36&amp;nttNo=11518" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고문 및 신청서 다운로드 (하남도시공사) →</a></div>
</div>
<div class="source">
📌 출처: 하남도시공사
</div>
</div>

<!-- 공공기관 소식 2 (하남시미사노인복지관 10월 전문 세무상담) -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💼 하남시미사노인복지관 | 2026.10.23</div>
<h3><a href="https://misanoin.co.kr/contents.html?pageId=HWNWWCQ8591VBVE9K1DL&amp;type=3&amp;wr_id=484&amp;page=1" target="_blank" style="color: inherit; text-decoration: none;">하남시미사노인복지관 10월 전문 세무상담 신청자 모집 (상속·증여·양도소득세 1:1 상담)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
하남시미사노인복지관에서 평소 궁금했던 상속·증여세 및 부동산 양도소득세 등 세금 관련 고민 해결을 위해 전문 세무사(김태진 세무사)와 함께하는 1:1 맞춤형 세무상담 신청자를 모집합니다.<br/><br/>
<b>🗓 상담 일시:</b> 2026년 10월 23일(금) 15:00 ~ 17:00 (1인당 30~40분 소요)<br/>
<b>👥 신청 대상:</b> 복지관 이용회원 4명 (선착순 마감)<br/>
<b>💡 상담 내용:</b> 상속·증여 세금, 부동산 양도세 및 기타 세금 관련 문의<br/>
<b>🏢 신청 장소:</b> 복지관 2층 제2사무실 (방문 및 유선 신청 가능)<br/>
<b>📞 문의처:</b> 문화복지팀 <a href="tel:070-4774-4490" style="color:#3182ce; font-weight:bold;">070-4774-4490</a>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://misanoin.co.kr/contents.html?pageId=HWNWWCQ8591VBVE9K1DL&amp;type=3&amp;wr_id=484&amp;page=1" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청 방법 확인 (미사노인복지관) →</a></div>
</div>
<div class="source">
📌 출처: 하남시미사노인복지관 (문화복지팀)
</div>
</div>
</div>"""

# Slice replace Section 3, Section 4 & Section 5
idx_mom = content.find('<div id="mom-cafe">')
idx_bottom = content.find('<div class="bottom-nav"')
content = content[:idx_mom] + section3_content + '\n\n' + section4_content + '\n\n' + section5_content + '\n\n' + content[idx_bottom:]

# Update visitor counter path ID to 0921
content = content.replace("lee-kwang-jae.news_letter.0918", "lee-kwang-jae.news_letter.0921")

# Remove visitor counter element from footer
content = re.sub(r'<div style="margin-top: 2px; text-align: center;">\s*<span[^>]*><span id="visitor_counter_val">.*?</span></span>\s*</div>', '', content, flags=re.DOTALL)

# Update playNewsletterVideo function for shorts_0921
new_script = """function playNewsletterVideo() {
    var v = document.getElementById('video-HHx77yzsWrY') || document.getElementById('video-shorts0921') || document.getElementById('video-shorts0918') || document.getElementById('video-A5H3SrB6qiE');
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

# Save to news_index_path & root_index_path
with open(news_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {news_index_path}")

with open(root_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {root_index_path}")
