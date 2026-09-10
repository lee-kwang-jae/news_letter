# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title / Date replacements
content = content.replace("2026년 9월 9일</title>", "2026년 9월 10일</title>")
content = content.replace("인사이드 - 2026년 9월 9일", "인사이드 - 2026년 9월 10일")
content = content.replace("36호 | 2026년 9월 9일 발행", "37호 | 2026년 9월 10일 발행")
content = content.replace("2026년 9월 9일 기준 하남 지역 인터넷", "2026년 9월 10일 기준 하남 지역 인터넷")
content = content.replace("2026년 9월 9일 기준 한눈에 보는 하남시", "2026년 9월 10일 기준 한눈에 보는 하남시")
content = content.replace("발행일: 2026년 9월 9일 | Lee Kwang-jae Newsletter", "발행일: 2026년 9월 10일 | Lee Kwang-jae Newsletter")

# 2. Culture section replacement
new_culture = """<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 10일 기준 한눈에 보는 하남시 최신 문화·행사·도서관 프로그램 가이드</p>

<!-- 문화 기사 1 (2026 하남 이성산성 문화제 - 하남여행버스) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🚌 2026.09.19 | 축제/관광</div>
<h3><a href="https://onoffmix.com/event/348611" target="_blank" style="color: inherit; text-decoration: none;">[축제/관광] 축제와 함께 떠나는 하남여행버스 프로그램 신청 《2026 하남 이성산성 문화제》</a></h3>
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
<h3><a href="https://www.han5amlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&edcLctreNo=5084" target="_blank" style="color: inherit; text-decoration: none;">[교육/도서관] 하남시 미사도서관 독서문화 프로그램 강좌 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"미사도서관에서 만나는 알찬 독서문화 프로그램!"</b><br/>
하남시 미사도서관에서 운영하는 독서문화 프로그램 강좌입니다. 다양한 분야의 강좌를 통해 지역 주민의 문화·교육 역량을 높이고 독서를 생활화할 수 있는 기회를 제공합니다.<br/><br/>
<b>📍 장소:</b> 하남시 미사도서관<br/>
<b>💡 신청:</b> 하남시립도서관 홈페이지에서 신청 가능
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.han5amlib.go.kr/mslib/selectWebEdcLctreView.do?key=689&edcLctreNo=5084" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">강좌 상세 안내 (미사도서관) →</a></div>
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
<h3><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">[교육/도서관] 하남시 감일도서관 공지사항 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"감일도서관의 새로운 소식을 확인하세요!"</b><br/>
하남시 감일도서관에서 안내하는 최신 공지사항입니다. 감일·위례 지역 주민들이 이용 가능한 다양한 프로그램 및 도서관 관련 소식을 확인하실 수 있습니다.<br/><br/>
<b>📍 장소:</b> 하남시 감일도서관<br/>
<b>📞 문의:</b> 031-790-6368
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공지사항 보기 (감일도서관) →</a></div>
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
<h3><a href="https://www.hanamlib.go.kr/wilib/selectBbsNttView.do?key=883&bbsNo=131&nttNo=89769&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">[교육/도서관] ★위례도서관 9월 프로그램 안내★</a></h3>
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
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&bbsNo=30&nttNo=502113" target="_blank" style="color: inherit; text-decoration: none;">[시정/공지] 하남시청 공지사항 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"하남시청에서 전하는 최신 공지사항입니다!"</b><br/>
하남시청 공식 홈페이지에서 공지하는 시정 관련 최신 소식입니다. 하남시민 생활과 밀접한 행정 정보를 확인하실 수 있습니다.<br/><br/>
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

# Replace culture section
culture_pos = content.find('<div id="culture">')
if culture_pos != -1:
    hr_pos = content.find('<hr', culture_pos)
    if hr_pos != -1:
        content = content[:culture_pos] + new_culture + '\n\n' + content[hr_pos:]
        print("Culture section replaced!")

# 3. Remove 4 requested articles from public news section
# Articles to remove:
keywords_to_remove = [
    "K-컬처 복합 콤플렉스",
    "인플루엔자(독감)",
    "연체지우개",
    "생활폐기물 배출 일시 중단"
]

# Split public news section into article cards block
pub_start = content.find('<div id="public-news">')
culture_start = content.find('<div id="culture">')

if pub_start != -1 and culture_start != -1:
    pub_section = content[pub_start:culture_start]
    
    # We can remove individual article cards matching keywords
    # Article cards are wrapped as:
    # <!-- 기사 N ... --> <div class="article-card"> ... </div> <div class="source"> ... </div> </div>
    # Or simple <div class="article-card"> ... <div class="source">...</div>\n</div>
    
    # Split by <!-- 기사 or <div class="article-card"
    cards = re.split(r'(?=(?:<!--\s*기사|<div class="article-card"))', pub_section)
    
    filtered_cards = []
    for card in cards:
        remove = False
        for kw in keywords_to_remove:
            if kw in card:
                remove = True
                print(f"Removing article containing keyword: {kw}")
                break
        if not remove:
            filtered_cards.append(card)
            
    new_pub_section = "".join(filtered_cards)
    content = content[:pub_start] + new_pub_section + content[culture_start:]

# Save modified content
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully processed and updated {target_path} & {index_path}!")
