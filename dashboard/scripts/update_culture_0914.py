# -*- coding: utf-8 -*-
import os
import re

new_culture_section = """<!-- ===== 섹션 4: ALL IN 하남라이프 ===== -->
<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 한눈에 보는 하남시 최신 문화·행사·추석 시장 이벤트 가이드</p>

<!-- 문화 기사 1 (추석 연휴 전통시장 이벤트: 신장전통시장 경품 & 하남수산물전통시장 온누리 환급) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎁 2026.09.16~09.23 | 전통시장/추석</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026년 추석 명절 맞이 하남시 전통시장 경품 행사 &amp; 온누리상품권 최대 30% 환급 이벤트</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"풍성한 한가위, 하남시 전통시장에서 장보고 경품과 온누리상품권 혜택 받으세요!"</b><br/>
하남시 관내 전통시장에서 2026년 추석 명절을 맞아 시민과 상인이 함께하는 풍성한 경품 및 온누리상품권 환급 행사를 개최합니다.<br/><br/>
<b>🛍️ 신장전통시장 『추석명절 경품 행사』</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 22일(화) ~ 9월 23일(수)<br/>
&nbsp;&nbsp;• <b>장소:</b> 신장전통시장 고객센터 1층<br/>
&nbsp;&nbsp;• <b>내용:</b> 3만 원 이상 구매 고객 대상 경품 선착순 지급<br/><br/>
<b>🐟 하남수산물전통시장 『온누리상품권 환급행사』</b><br/>
&nbsp;&nbsp;• <b>기간:</b> 2026년 9월 16일(수) ~ 9월 20일(일) (11:00 ~ 19:00)<br/>
&nbsp;&nbsp;• <b>내용:</b> 당일 구매 금액의 최대 30%를 온누리상품권으로 환급 (1인 20,000원 한도)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;— 34,000원 이상 ~ 67,000원 미만: <b>10,000원 환급</b><br/>
&nbsp;&nbsp;&nbsp;&nbsp;— 67,000원 이상: <b>20,000원 환급</b>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">전통시장 행사 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 신장전통시장상인회 / 하남수산물전통시장상인회 / 하남시청
</div>
</div>

<!-- 문화 기사 2 (추석 연휴 전통시장 고객전용주차장 운영 및 덕풍주차장 무료 개방) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🚗 2026.09.25~09.26 무료 | 교통/주차</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">추석 연휴 하남시 덕풍·신장 전통시장 주차장 운영 및 덕풍주차장 무료 개방 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"추석 장보기 주차 걱정 끝! 덕풍전통시장 주차장 9월 25일~26일 2일간 무료 개방"</b><br/>
추석 연휴 전통시장을 방문하는 시민분들의 주차 편의를 위해 덕풍·신장전통시장 고객전용주차장을 24시간 운영하며, 덕풍전통시장 주차장은 추석 연휴 기간 무료로 개방합니다.<br/><br/>
<b>🅿️ 덕풍전통시장 고객전용주차장</b><br/>
&nbsp;&nbsp;• <b>위치:</b> 하남시 신장로154번길 57 (130면, 24시간 운영)<br/>
&nbsp;&nbsp;• <b>🎉 무료 개방: 2026년 9월 25일(금) ~ 9월 26일(토) (2일간 전면 무료)</b><br/>
&nbsp;&nbsp;• <b>문의:</b> 덕풍전통시장상인회 <a href="tel:031-794-3753" style="color:#3182ce; font-weight:bold;">031-794-3753</a> (관리자 근무 08:00~22:00)<br/><br/>
<b>🅿️ 신장전통시장 고객전용주차장</b><br/>
&nbsp;&nbsp;• <b>위치:</b> 하남시 신장1로3번길 42 (100면, 24시간 운영)<br/>
&nbsp;&nbsp;• <b>이용요금:</b> 최초 30분 600원, 추가 10분당 200원<br/>
&nbsp;&nbsp;• <b>문의:</b> 신장전통시장상인회 <a href="tel:031-794-4626" style="color:#3182ce; font-weight:bold;">031-794-4626</a> (관리자 근무 06:00~23:00)
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">주차장 위치 및 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 덕풍전통시장상인회 / 신장전통시장상인회
</div>
</div>

<!-- 문화 기사 3 (생활문화센터 하반기 생~긋! 프로그램 참여자 모집) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🎨 2026.10~12 | 문화/강좌</div>
<h3 style="margin-top: 6px;"><a href="https://www.hnart.or.kr/space/selectBbsNttView.do?key=422&amp;bbsNo=68&amp;nttNo=7061" target="_blank" style="color: inherit; text-decoration: none;">하남시 생활문화센터 하반기 『생~긋!』 공예·댄스 프로그램 참여자 모집 (선착순)</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"일상에 향기와 즐거움을 더하는 하남시 생활문화센터 하반기 강좌!"</b><br/>
하남시 생활문화센터에서 향기, 테라리움, 가죽공예, 코바늘 등 다양한 공예 강좌부터 부모와 아이가 함께 즐기는 비보이 댄스까지 알찬 하반기 『생~긋!』 문화 프로그램을 운영합니다.<br/><br/>
<b>📅 운영기간:</b> 2026년 10월 ~ 12월<br/>
<b>📝 모집기간:</b> 2026년 9월 9일(수) ~ 선착순 접수 마감<br/>
<b>📍 운영장소:</b> 하남시 생활문화센터 4개소 (하다, 덕풍, 미사, 감일)<br/>
<b>☎️ 센터별 문의:</b><br/>
&nbsp;&nbsp;— 하다/덕풍 센터: <a href="tel:031-790-7930" style="color:#3182ce; font-weight:bold;">031-790-7930</a><br/>
&nbsp;&nbsp;— 미사 센터: <a href="tel:031-790-7969" style="color:#3182ce; font-weight:bold;">031-790-7969</a><br/>
&nbsp;&nbsp;— 감일 센터: <a href="tel:031-790-7927" style="color:#3182ce; font-weight:bold;">031-790-7927</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hnart.or.kr/space/selectBbsNttView.do?key=422&amp;bbsNo=68&amp;nttNo=7061" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">상세 안내 및 신청하기 (하남문화재단) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0914-4.jpg" alt="하남시 생활문화센터 하반기 생~긋! 프로그램 모집" style="width: 100%; height: 210px; object-fit: contain; background-color: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 하남문화재단 / 하남시 생활문화센터
</div>
</div>

<!-- 문화 기사 4 (2026 하남 이성산성 문화제) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">🏛️ 2026.09.19~09.20 | 역사/축제</div>
<h3 style="margin-top: 6px;"><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">2026 하남 이성산성 문화제 《백제의 숨결, 이성산성 가을 나들이》 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"하남의 소중한 역사 유적 이성산성에서 펼쳐지는 가을 축제!"</b><br/>
하남시 대표 역사 문화 축제인 '2026 하남 이성산성 문화제'가 오는 9월 19일부터 펼쳐집니다. 이성산성 야외 투어, 어린이 백제 역사 체험, 하남 여행 버스투어 등 풍성한 가족 프로그램이 준비되어 있습니다.<br/><br/>
<b>📅 일시:</b> 2026년 9월 19일(토) ~ 9월 20일(일)<br/>
<b>📍 장소:</b> 하남 이성산성 및 하남시 주요 역사 문화 거점<br/>
<b>🏛️ 문의:</b> 하남문화재단 / 하남시 문화체육과
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">축제 프로그램 안내 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 / 하남문화재단
</div>
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260914.html'
]

pattern = re.compile(r'<div id="culture">.*?</div>\n</div>\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn(new_culture_section + '\n</div>\n<hr style="border: none; border-top: 1px solid #e2e8f0; margin: 35px 0;"/>', content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath} (replaced {count} occurrence)")
        else:
            print(f"Failed to match culture section in {filepath}")
    else:
        print(f"File not found: {filepath}")

# Also update create_0914.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0914.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_pattern = re.compile(r'section4_content = """.*?</div>"""', re.DOTALL)
    new_script_block = f'section4_content = """{new_culture_section}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
