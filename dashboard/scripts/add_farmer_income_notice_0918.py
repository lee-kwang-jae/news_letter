# -*- coding: utf-8 -*-
import os
import re

new_section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 18일 기준 경기도 및 하남시 공공기관 주요 공고·신청 안내입니다.</p>

<!-- 공공기관 소식 1: 2026-2027절기 인플루엔자·코로나19 무료 예방접종 -->
<div class="article-card">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">💉 하남시보건소 | 2026.09.21~</div>
<h3><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: inherit; text-decoration: none;">2026-2027절기 인플루엔자(독감)·코로나19 무료 예방접종 안내 (60~64세 하남시민 추가 지원)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시 보건소에서 환절기 건강 증진을 위해 2026-2027절기 독감 및 코로나19 무료 예방접종을 순차적으로 시행합니다.<br/><br/>
<b>👶 어린이·임신부:</b> 2026년 9월 21일(월)부터 접종 개시<br/>
<b>👵 어르신 (65세 이상):</b> 75세 이상(10/6~), 70~74세(10/12~), 65~69세(10/15~)<br/>
<b>🏥 하남시민 자체 추가 지원:</b> 60~64세, 50~59세 기초수급자/국가유공자, 15~59세 심한 장애인 (10/19부터 하남시 지정병원에서 무상 지원)<br/>
<b>📍 접종 장소:</b> 지정 위탁의료기관 (예방접종도우미 사이트 nip.kdca.go.kr 조회)
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/health/selectBbsNttView.do?key=915&amp;bbsNo=109&amp;nttNo=502516" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고 및 위탁의료기관 조회 (하남시보건소) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091802.jpg" alt="2026-27년도 인플루엔자 무료 예방접종 안내" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시 보건소 (보건정책과)
</div>
</div>

<!-- 공공기관 소식 2: 2026년 녹색건축물 조성 지원사업 안내 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🏡 하남시 도시전략과 | ~2026.09.30</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502750" target="_blank" style="color: inherit; text-decoration: none;">2026년 녹색건축물 조성 지원사업 공고 안내</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<div style="flex: 1;">
하남시 관내 사용승인 15년 이상 경과된 소규모 노후 주택 단열 창호 교체 및 LED 조명 교체 비용의 50% 이내(최대 900만 원)를 지원하는 공모 신청 안내입니다.<br/><br/>
<b>📅 신청 기간:</b> 2026년 9월 14일(월) ~ 9월 30일(수)<br/>
<b>📋 신청 자격:</b> 하남시 전역 15년 경과 단독·다세대·상가주택 건물 소유자<br/>
<b>🏢 접수 장소:</b> 하남시청 도시전략과 방문 접수
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&amp;bbsNo=30&amp;nttNo=502750" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 공고 확인하기 (하남시청) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/091803.jpg" alt="2026년 녹색건축물 조성 지원사업 공고" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남시청 도시전략과
</div>
</div>

<!-- 공공기관 소식 3: 2026년도 하남시 농어민 기회소득 지원사업 2차 신청접수 -->
<div class="article-card" style="margin-top: 16px;">
<div class="badge" style="background-color: #f3e8ff; color: #6b21a8; border: 1px solid #e9d5ff;">🌾 하남시 식품위생농업과 | 2026.09.21 ~ 10.23</div>
<h3><a href="https://farmbincome.gg.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026년도 하남시 농어민 기회소득 지원사업 2차 신청 접수 안내 (하남시 공고 제2026-1701호)</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
하남시 관내 농어업인의 공익적 가치 보장 및 삶의 질 향상을 위한 '2026년도 농어민 기회소득 지원사업' 2차 신청을 접수합니다.<br/><br/>
<b>📅 신청 기간:</b> 2026년 9월 21일(월) ~ 10월 23일(금)<br/>
<b>🌾 지원 대상:</b> 하남시 주소지 및 농어업경영체 등록 농어민 (연속 1년 이상 거주·영농, 농외소득 3,700만 원 미만)<br/>
<b>💰 지원 내용:</b> 농어민 개인별 지역화폐 지급 (청년·환경·귀농어민 월 15만 원 / 일반농어민 월 5만 원, 하반기 30~90만 원 이내)<br/>
<b>💻 신청 방법:</b> 주소지 동 행정복지센터 방문 신청 또는 농어민 기회소득 통합지원시스템 온라인 신청 (farmbincome.gg.go.kr)<br/>
<b>💵 지급 시기:</b> 2026년 12월 중 (지급일로부터 180일 이내 사용)<br/>
<b>📞 문의처:</b> 하남시청 담당부서 (031-790-5769) 및 각 동 행정복지센터
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://farmbincome.gg.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">농어민 기회소득 통합지원시스템 바로가기 (경기도) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 (공고 제2026-1701호)
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
        
        idx_public = content.find('<div id="public-news">')
        idx_bottom = content.find('<div class="bottom-nav"')
        if idx_bottom == -1:
            idx_bottom = content.find('<!-- 하단')
            
        if idx_public != -1 and idx_bottom != -1:
            idx_comment = content.find('<!-- ===== 섹션 5: 공공기관 소식지 ===== -->')
            start_pos = idx_comment if (idx_comment != -1 and idx_comment < idx_public) else idx_public
            updated_content = content[:start_pos] + new_section5_content + '\n\n' + content[idx_bottom:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated Section 5 in {filepath}")
        else:
            print(f"Failed to find indices in {filepath}")

# Also update create_0918.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_pattern = re.compile(r'section5_content = """.*?</div>"""', re.DOTALL)
    new_script_block = f'section5_content = """{new_section5_content}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
