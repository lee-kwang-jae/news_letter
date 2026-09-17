# -*- coding: utf-8 -*-
import os
import re

new_section2_full = """<hr/>
<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (YTN: 제네시스, 추석 연휴 스타필드 하남에서 레이싱 페스티벌) -->
<div class="article-card">
<div class="badge">📰 기업/행사</div>
<h3><a href="https://www.ytn.co.kr/_ln/0102_202609171646424829" target="_blank" style="color: inherit; text-decoration: none;">제네시스, 추석 연휴 스타필드 하남에서 '마그마 레이싱 라이브 페스티벌' 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
'마그마 레이싱 팀'을 운영 중인 제네시스가 추석 연휴 기간 스타필드 하남에서 레이싱 행사를 개최합니다. 오는 24일부터 나흘간 진행되는 '마그마 레이싱 라이브 페스티벌'에는 르망 24시간 내구 레이스를 완주한 실제 하이퍼 카가 전시되며, 레이싱 시뮬레이터 체험 및 대형 스크린 중계 등 다채로운 이벤트가 열립니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.ytn.co.kr/_ln/0102_202609171646424829" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (YTN) →</a></div>
</div>
<div class="source">
📌 출처: YTN (정현우 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (뉴시스: 하남시 독감·코로나19 무료 예방접종) -->
<div class="article-card">
<div class="badge">📰 보건/복지</div>
<h3><a href="https://www.newsis.com/view/NISX20260917_0003794093" target="_blank" style="color: inherit; text-decoration: none;">하남시, 독감·코로나19 무료 예방접종… 21일부터 순차 시작 (60~64세 하남시민 무상 추가지원)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
하남시가 독감 및 코로나19 유행에 대비해 어린이와 임신부, 어르신 대상 무료 예방접종을 9월 21일부터 순차적으로 실시합니다. 정부 국가 지원 대상 외에도 하남시 지자체 자체 예산으로 60~64세 하남시민 및 취약계층 독감 백신 무상 접종 혜택이 추가 지원됩니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.newsis.com/view/NISX20260917_0003794093" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴시스) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091802.jpg" alt="무료 예방접종 진행 일정" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 뉴시스 (이호진 기자)
</div>
</div>

<!-- 지역 뉴스 기사 3 (연합뉴스: 제네시스 스타필드 하남서 레이싱 페스티벌) -->
<div class="article-card">
<div class="badge">📰 경제/문화</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260917038600003?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">제네시스, 24∼27일 스타필드 하남서 레이싱 페스티벌… 르망 24시간 하이퍼카 실물 공개</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
제네시스가 추석 연휴를 맞아 스타필드 하남에서 '제네시스 마그마 레이싱 라이브 페스티벌'을 개최합니다. 르망 24시간 경기를 완주한 하이퍼카를 국내 최초로 전시하며, 몰입감 높은 심레이싱 체험 존과 팝업스토어 등 쇼핑몰 방문객들을 위한 다양한 즐길 거리를 선보입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/AKR20260917038600003?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (김윤구 기자)
</div>
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

# Update target index files
for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        idx_lawmaker = content.find('<div id="lawmaker">')
        idx_mom = content.find('<div id="mom-cafe">')
        if idx_lawmaker != -1 and idx_mom != -1:
            idx_hr = content.find('<hr/>', idx_lawmaker)
            if idx_hr != -1 and idx_hr < idx_mom:
                updated_content = content[:idx_hr] + new_section2_full + '\n<hr/>\n' + content[idx_mom:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Successfully updated Section 2 in {filepath}")
            else:
                print(f"Failed to find hr in {filepath}")
        else:
            print(f"Failed to find indices in {filepath}")

# Also update create_0918.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_pattern = re.compile(r'section2_content = """.*?</div>"""', re.DOTALL)
    new_script_block = f'section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->\n{new_section2_full[11:]}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
