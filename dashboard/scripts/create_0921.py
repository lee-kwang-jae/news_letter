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

# Thumbnail aliases for 0921
primary_thumb = os.path.join(img_dir, 'thumbnail-921.jpg')
if os.path.exists(primary_thumb):
    aliases = ['thumbnail-0921.jpg', 'thumbnail0921.jpg', '09.jpg']
    for alias in aliases:
        dst1 = os.path.join(img_dir, alias)
        dst2 = os.path.join(dash_img_dir, alias)
        if primary_thumb != dst1:
            shutil.copy2(primary_thumb, dst1)
        shutil.copy2(primary_thumb, dst2)

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title, Issue Number, Date, Meta Image Tags
content = content.replace("43호 | 2026년 9월 18일 발행", "44호 | 2026년 9월 21일 발행")
content = content.replace("2026년 9월 18일 기준", "2026년 9월 21일 기준")
content = content.replace("images/thumbnail-0918.jpg", "images/thumbnail-0921.jpg")
content = content.replace("images/thumbnail-918.jpg", "images/thumbnail-0921.jpg")
content = content.replace("https://lee-kwang-jae.github.io/news_letter/images/thumbnail-0918.jpg", "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-0921.jpg")

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
  <img src="images/thumbnail-0921.jpg" alt="한강변에 기후부 장관님과 갔습니다" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
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
지방자치와 의정활동의 핵심 동력인 도시계획권을 적극 활용하여 하남시 관내에 숨어있는 국공유지를 발굴하고, 시민들을 위한 휴식·문화·공공 복지 공간으로 재창조하는 현장 구상을 담은 숏폼 영상입니다.
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-HHx77yzsWrY" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-HHx77yzsWrY" poster="images/thumbnail-0921.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
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

<!-- 지역 뉴스 기사 1 (디스커버리뉴스: 가을 하늘 아래 시민들로 채워진 미사호수공원…이성산성문화제 개막) -->
<div class="article-card">
<div class="badge">📰 문화/축제</div>
<h3><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1102154" target="_blank" style="color: inherit; text-decoration: none;">가을 하늘 아래 시민들로 채워진 미사호수공원… 2026 하남이성산성문화제 개막</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
19일 오후 높고 맑은 가을 하늘 아래 미사호수공원에서 '2026 하남이성산성문화제'가 화려하게 개막했습니다. 잔디광장을 찾은 가족과 연인, 시민들로 가득 찬 가운데, 하남의 역사적 유산인 이성산성과 미사호수공원을 잇는 야외 공연과 다채로운 역사 문화 체험 프로그램이 개최되어 큰 호응을 얻었습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.discoverynews.kr/news/articleView.html?idxno=1102154" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디스커버리뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 디스커버리뉴스 (이명수 기자)
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

# Update visitor counter path ID to 0921
content = content.replace("lee-kwang-jae.news_letter.0918", "lee-kwang-jae.news_letter.0921")

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
