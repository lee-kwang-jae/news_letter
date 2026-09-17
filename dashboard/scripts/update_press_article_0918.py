# -*- coding: utf-8 -*-
import os
import re

new_press_card = """<!-- 기사 1 (언론보도 - 기호일보: 이광재 국회의원 "평창올림픽 시설, 국가가 직접 관리·운영") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035071" target="_blank" style="color: inherit; text-decoration: none;">이광재 국회의원 "평창올림픽 시설, 국가가 직접 관리·운영"… '국민체육진흥법 개정안' 대표발의</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
2018 평창 동계올림픽 시설의 사후 관리 책임을 지방자치단체가 떠안으며 발생한 누적 적자(약 410억 원) 해결을 위해 이광재(민주·하남갑) 국회의원이 나섰습니다. 이 의원은 올림픽 체육시설 관리·운영 주체를 서울올림픽기념국민체육진흥공단으로 확대해 국가 차원에서 책임지고 운영하도록 하는 '국민체육진흥법' 일부개정법률안을 대표발의했습니다. 이 의원은 서울올림픽공원처럼 평창·강릉·정선의 올림픽 유산 시설들도 국가 차원의 체계적인 운영 시스템으로 전환되어야 한다고 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kihoilbo.co.kr/news/articleView.html?idxno=3035071" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (기호일보) →</a></div>
</div>
<div class="source">
📌 출처: 기호일보 (이홍재 기자)
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

pattern = re.compile(r'<!-- 기사 1 \(언론보도 - .*?--\>\s*<div class="article-card card-press">.*?<div class="source">.*?</div>\s*(?:<div class="source">.*?</div>\s*)*</div>', re.DOTALL)

# Update HTML files
for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            updated_content = pattern.sub(new_press_card, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated press article in {filepath}")
        else:
            print(f"Failed to find press article pattern in {filepath}")

# Update create_0918.py
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    if pattern.search(script_code):
        updated_script_code = pattern.sub(new_press_card, script_code)
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated press article in {create_script_path}")
    else:
        print(f"Failed to match press article pattern in {create_script_path}")
