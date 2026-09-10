# -*- coding: utf-8 -*-
import os
import re
import shutil

# Copy image to root images directory if not present
src_img = r'd:\github\newsletter\newsletter\dashboard\news\images\0911-01.jpg'
dst_img = r'd:\github\newsletter\newsletter\images\0911-01.jpg'

if os.path.exists(src_img):
    shutil.copy2(src_img, dst_img)
    print(f"Copied image from {src_img} to {dst_img}")
else:
    print(f"Warning: {src_img} not found")

new_culture = """<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 11일 기준 한눈에 보는 하남시 최신 문화·행사·축제 가이드</p>

<!-- 문화 기사 (특별한 오후 미사숲한마당축제 & 황산음악회 with 플리마켓) -->
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
        
        updated_content, count = pattern.subn(new_culture, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath} (replaced {count} occurrence)")
        else:
            print(f"Failed to match culture section in {filepath}")
    else:
        print(f"File not found: {filepath}")
