# -*- coding: utf-8 -*-
import os
import re

new_culture_section = """<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 11일 기준 한눈에 보는 하남시 최신 문화·행사·축제 가이드</p>

<!-- 문화 기사 1 (특별한 오후 미사숲한마당축제 & 황산음악회 with 플리마켓) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎪 2026.09.12(토) | 축제/행사</div>
<h3><a href="#" style="color: inherit; text-decoration: none;">특별한 오후 《미사숲한마당축제 &amp; 황산음악회 with 플리마켓》 시민 여러분을 초대합니다</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"미사숲공원에서 펼쳐지는 특별한 오후! 미사숲한마당축제 &amp; 황산음악회 with 플리마켓"</b><br/>
미사3동 주민자치회에서 마련한 이번 축제는 아름다운 음악 공연과 다채로운 플리마켓, 즐거운 체험이 어우러지는 하남 시민 초청 행사입니다. 미사숲공원 잔디광장에서 가족, 이웃과 함께 풍성하고 즐거운 주말 오후를 즐기세요.<br/><br/>
<b>📅 일시:</b> 2026년 9월 12일(토) 오후 1시 ~ 3시<br/>
<b>📍 장소:</b> 미사숲공원 내 잔디광장<br/>
<b>🏛️ 주최:</b> 미사3동 주민자치회
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0911-01.jpg" alt="미사숲한마당축제 &amp; 황산음악회 with 플리마켓" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 미사3동 주민자치회
</div>
</div>

<!-- 문화 기사 2 (2026 경기도자박물관 생생 국가유산 교육 - 탐정 수첩) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🔍 2026.09.11~ | 교육/체험</div>
<h3><a href="https://www.kocef.org/html/board_view.html?cate=mbb_notice_expo&amp;gubun=0&amp;b_idx=MzEzNCAg" target="_blank" style="color: inherit; text-decoration: none;">2026 경기도자박물관 [생생 국가유산 교육] 『탐정 수첩 : 도자기 속 단서들』 참여 가족 모집 (무료)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"우리 가족이 탐정이 되어 도자기 속 숨겨진 단서를 밝혀라!"</b><br/>
경기도자박물관에서 초등 자녀를 둔 가족을 대상으로 생생 국가유산 교육 프로그램 『탐정 수첩 : 도자기 속 단서들』 참가 가족을 모집합니다. 가족이 함께 미션을 해결하며 역사와 도자 문화를 생생하게 체험할 수 있습니다.<br/><br/>
<b>📅 운영기간:</b> 2026년 10월 10일(토) ~ 10월 25일(일) (주말 총 6회)<br/>
<b>📝 모집기간:</b> 2026년 9월 11일(금) 10:00 ~ 선착순 마감 (무료)<br/>
<b>👨‍👩‍👧‍👦 대상:</b> 초등 자녀를 둔 3~5인 가족 (회당 10가족)<br/>
<b>📍 장소:</b> 분원백자자료관, 팔당전망대, 경기도자박물관 등
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kocef.org/html/board_view.html?cate=mbb_notice_expo&amp;gubun=0&amp;b_idx=MzEzNCAg" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (한국도자재단) →</a></div>
</div>
<div class="source">
📌 출처: 한국도자재단 / 경기도자박물관
</div>
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

pattern = re.compile(r'<div id="culture">.*?</div>\s*(?=\n\n?<hr|\n\n?<!-- ===== 섹션|\n\n?<div id="public-news")', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn(new_culture_section, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath} (replaced {count} occurrence)")
        else:
            print(f"Failed to match culture section in {filepath}")
    else:
        print(f"File not found: {filepath}")
