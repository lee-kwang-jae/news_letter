# -*- coding: utf-8 -*-
import os
import re

new_section2_content = """<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->
<div id="local-news">
<div class="section-title green">📰 하남 지역 주요 뉴스</div>

<!-- 지역 뉴스 기사 1 (뉴시스: 하남시 독감·코로나19 무료 예방접종) -->
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

<!-- 지역 뉴스 기사 2 (연합뉴스: 제네시스 스타필드 하남서 레이싱 페스티벌) -->
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

<!-- 지역 뉴스 기사 3 (하남일보: [기자수첩] "미사리 경정장은 하남에서 당장 떠나라") -->
<div class="article-card">
<div class="badge">📰 지역/이슈</div>
<h3><a href="http://www.hanamilbo.net/news/articleView.html?idxno=12633" target="_blank" style="color: inherit; text-decoration: none;">[기자수첩] "미사리 경정장은 하남에서 당장 떠나라"… 사행성 폐해 지적 및 퇴출 촉구</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
2002년부터 운영되어 온 미사리 경정장에 대해 도박 중독 및 사행성 사업으로 인한 시민들의 가산 탕진, 가정 파탄 등 부정적인 사회적 여파를 비판하는 목소리가 커지고 있습니다. 지역 커뮤니티와 시민단체를 중심으로 경정장 퇴출 및 이전 강경 투쟁 선언이 이어지며 미사리 경정장 유치의 실익에 대한 열띤 논의가 계속되고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="http://www.hanamilbo.net/news/articleView.html?idxno=12633" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (하남일보) →</a></div>
</div>
<div class="source">
📌 출처: 하남일보 (승웅 기자)
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
                updated_content = content[:idx_hr] + '<hr/>\n' + new_section2_content + '\n<hr/>\n' + content[idx_mom:]
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
    new_script_block = f'section2_content = """{new_section2_content}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
