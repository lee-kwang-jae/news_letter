# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260909.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue updates
content = content.replace("2026년 9월 9일</title>", "2026년 9월 10일</title>")
content = content.replace("인사이드 - 2026년 9월 9일", "인사이드 - 2026년 9월 10일")
content = content.replace("36호 | 2026년 9월 9일 발행", "37호 | 2026년 9월 10일 발행")
content = content.replace("2026년 9월 9일 기준 하남 지역 인터넷", "2026년 9월 10일 기준 하남 지역 인터넷")
content = content.replace("2026년 9월 9일 기준 한눈에 보는 하남시", "2026년 9월 10일 기준 한눈에 보는 하남시")
content = content.replace("발행일: 2026년 9월 9일 | Lee Kwang-jae Newsletter", "발행일: 2026년 9월 10일 | Lee Kwang-jae Newsletter")

# 2. Define New Culture Section
new_culture_section = """<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 10일 기준 한눈에 보는 하남시 최신 문화·행사·도서관 프로그램 가이드</p>

<!-- 문화 기사 1 (2026 하남 이성산성 문화제 - 하남여행버스) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🚌 2026.09.19 | 축제/관광</div>
<h3><a href="https://onoffmix.com/event/348611" target="_blank" style="color: inherit; text-decoration: none;">축제와 함께 떠나는 하남여행버스 프로그램 신청 《2026 하남 이성산성 문화제》</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"하남의 역사와 자연을 함께 즐기는 특별한 버스 여행!"</b><br/>
2026 하남 이성산성 문화제와 함께하는 하남여행버스 프로그램입니다. 하남의 역사 유적지와 자연경관을 둘러보는 체험형 버스투어로, 축제 현장의 풍성한 프로그램을 함께 즐기실 수 있습니다.<br/><br/>
<b>📅 일시:</b> 2026년 9월 19일(토) 10:00 출발<br/>
<b>📍 장소:</b> 하남 이성산성 일대<br/>
<b>💡 참가신청:</b> 온오프믹스(onoffmix.com)에서 선착순 신청
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://onoffmix.com/event/348611" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">프로그램 신청하기 (온오프믹스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-05.jpg" alt="2026 하남 이성산성 문화제 하남여행버스" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 / 온오프믹스
</div>
</div>

<!-- 문화 기사 2 (미사도서관 강좌) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📚 2026.09 | 교육/도서관</div>
<h3><a href="https://www.hanamlib.go.kr/mslib/index.do" target="_blank" style="color: inherit; text-decoration: none;">하남시 미사도서관 독서문화 프로그램 강좌 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"미사도서관에서 만나는 알찬 독서문화 프로그램!"</b><br/>
하남시 미사도서관에서 운영하는 독서문화 프로그램 강좌입니다. 다양한 분야의 강좌를 통해 지역 주민의 문화·교육 역량을 높이고 독서를 생활화할 수 있는 기회를 제공합니다.<br/><br/>
<b>📍 장소:</b> 하남시 미사도서관<br/>
<b>💡 신청:</b> 하남시립도서관 홈페이지에서 신청 가능
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/mslib/index.do" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">강좌 상세 안내 (미사도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-02.jpg" alt="미사도서관 독서문화 프로그램" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 미사도서관
</div>
</div>

<!-- 문화 기사 3 (감일도서관 공지) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">📖 2026.09 | 교육/도서관</div>
<h3><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">감일도서관 9월 독서의 달 프로그램 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"감일도서관 9월 독서의 달 프로그램 안내"</b><br/>
- 9월 프로그램 많은 관심 부탁드립니다!<br/>
링크를 누르시면 9월프로그램을 모두 확인가능합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">프로그램 안내 보기 (감일도서관) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-03.jpg" alt="감일도서관 공지사항" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 감일도서관
</div>
</div>

<!-- 문화 기사 4 (위례도서관 9월 프로그램) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">⭐ 2026.09 | 교육/도서관</div>
<h3><a href="https://www.hanamlib.go.kr/wilib/selectBbsNttView.do?key=883&bbsNo=131&nttNo=89769&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">★위례도서관 9월 프로그램 안내★</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"위례도서관에서 9월을 알차게 보내세요!"</b><br/>
하남시 위례도서관의 2026년 9월 독서문화 프로그램 안내입니다. 독서의 달을 맞아 다채로운 프로그램이 준비되어 있으며, 위례동 주민 누구나 참여 가능합니다.<br/><br/>
<b>📍 장소:</b> 하남시 위례도서관<br/>
<b>💡 신청:</b> 하남시립도서관 홈페이지에서 신청 가능
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/wilib/selectBbsNttView.do?key=883&bbsNo=131&nttNo=89769&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">9월 프로그램 안내 보기 (위례도서관) →</a></div>
</div>
<div class="source">
📌 출처: 하남시 위례도서관
</div>
</div>

<!-- 문화 기사 5 (하남시청 공지사항) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🏙️ 2026.09 | 시정/공지</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&bbsNo=30&nttNo=502113" target="_blank" style="color: inherit; text-decoration: none;">2026년 하남시 청년의 날 기념 「청년 명랑 운동회」 개최</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"2026년 하남시 청년의 날 기념 「청년 명랑 운동회」 개최"</b><br/>
2026년 청년의 날을 맞아 지역 청년 간 네트워킹 기회 마련을 위해 2025년 청년 명랑 운동회를 아래와 같이 개최하오니 많은 관심 바랍니다.<br/><br/>
<b>📍 문의:</b> 하남시청 ☎ 031-790-5114
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&bbsNo=30&nttNo=502113" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공지사항 자세히 보기 (하남시청) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-04.jpg" alt="하남시청 공지사항" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청
</div>
</div>
</div>"""

# 3. Replace culture section
culture_idx = content.find('<div id="culture">')
pub_idx = content.find('<div id="public-news">')

before_culture = content[:culture_idx]

# 4. Construct Public News Section cleanly
new_ansim_article = """<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.07~12</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">퇴원환자의 안전한 일상복귀지원사업 &#34;경기안심이음케어&#34;</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
경기도사회서비스원에서는 퇴원환자의 돌봄 공백을 최소화하고 가정 내 안정적인 복귀를 지원하기 위해 <b>『경기안심이음케어』</b> 사업을 운영하고 있습니다.<br/><br/>
<b>신청기간:</b> 2026년 7월 ~ 12월 (예산 소진 시 사업 종료)<br/>
<b>서비스 대상:</b> 질병·부상·수술 등으로 입원 치료 후 퇴원하는(퇴원 7일 이내) 경기도민 중 돌봄 공백이 우려되는 분<br/>
<b>제공 서비스:</b> AI 의료 모니터링, 생활(가사)돌봄, 병원 동행 돌봄, 맞춤형 식사 지원, 심리재활 서비스 등<br/>
<b>제공 기간:</b> 퇴원 후 30일 이내<br/>
<b>지원 한도:</b> 1인 100만 원 이내 (소득 기준에 따라 본인부담금 발생 가능)<br/>
<b>문의:</b><br/>
&nbsp;&nbsp;— 경기도사회복지관협회: <a href="tel:031-928-6935" style="color:#3182ce; font-weight:bold;">031-928-6935</a><br/>
&nbsp;&nbsp;— 경기도사회서비스원: <a href="tel:031-884-8573" style="color:#3182ce; font-weight:bold;">031-884-8573</a>
<div style="margin-top: 14px; text-align: center;">
<img src="./images/0910-06.jpg" alt="경기안심이음케어 사업 안내" style="max-width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청
</div>
</div>"""

# Extract imageModal part
modal_idx = content.find('<div id="imageModal"')

new_public_news_section = f"""<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>

<!-- 신규: 경기안심이음케어 퇴원환자 지원사업 -->
{new_ansim_article}
</div>

"""

final_html = before_culture + new_culture_section + '\n\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>\n\n' + new_public_news_section + content[modal_idx:]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Build 0910 clean complete!")
