# -*- coding: utf-8 -*-
import os
import re

new_mom_cafe_section = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 하남시 초·중·고 통학로 '스마트 가온길 &amp; 노란색 횡단보도' 대폭 확대 소식에 학부모 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 관내 초등학교 및 중학교 주변 스쿨존 내 바닥형 음성안내 보조장치(스마트 가온길) 및 노란색 횡단보도·보행자 신호등 조성을 2026년 하반기 대폭 확대 추진한다는 소식이 학부모 커뮤니티에서 큰 호응을 얻었습니다.</div>
<div class="mom-point">💡 주민 포인트: 어린이 등하굣길 스쿨존 교통사고 예방 및 학부모가 안심할 수 있는 안전한 보행 환경 조성.</div>
<div class="mom-reaction">💬 주민 반응: "아이 학교 앞에도 노란 횡단보도랑 바닥 신호등이 설치되어 한시름 놓이네요!", "등하굣길 안전장치가 늘어나서 마음이 든든합니다" 학부모 응원 속출.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ '2026 하남 이성산성 문화제' 가족 유적 탐험·하남 여행 버스투어 사전예약에 학부모 관심 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 오는 9월 19일 개막하는 '2026 하남 이성산성 문화제'의 하남여행버스 및 어린이 유적 체험 프로그램 사전 접수가 오픈되었다는 소식이 전해지며 주말 나들이를 준비하는 학부모들의 예약 열기가 뜨겁습니다.</div>
<div class="mom-point">💡 주민 포인트: 가을 주말 가족 단위 백제 역사 문화 체험 및 이성산성 야외 투어 버스 선착순 무료 참여 가능.</div>
<div class="mom-reaction">💬 주민 반응: "작년에도 접수 광속 마감이었는데 올해는 꼭 예약 성공하고 싶네요!", "아이와 가을 주말 나들이 가기 딱 좋은 역사 축제" 기대 만발.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 감일·위례 신도시 주요 지하철역 연결 시내버스 노선 증차 및 배차간격 단축 소식에 주민 호응</h4>
<div class="mom-detail"><strong>현황:</strong> 감일 및 위례 신도시 주민들의 출퇴근 및 학생 통학 불편 해소를 위해 5호선 올림픽공원역, 마천역 및 8호선 복정역을 잇는 주요 시내버스 및 마을버스 노선 증차가 확정되었다는 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 출퇴근길 버스 대기시간 단축 및 지하철역 환승 편의 대폭 향상으로 지역 교통 복지 개선.</div>
<div class="mom-reaction">💬 주민 반응: "드디어 감일 버스 배차간격이 좁혀지네요!", "아이들 학원 가고 서울 이동할 때 한결 수월해지겠어요" 감일·위례 맘카페 열띤 호응.</div>
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260914.html'
]

# Update index files using slice indexing
for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        idx_mom = content.find('<div id="mom-cafe">')
        idx_culture = content.find('<div id="culture">')
        if idx_mom != -1 and idx_culture != -1:
            updated_content = content[:idx_mom] + new_mom_cafe_section + '\n\n' + content[idx_culture:]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath}")
        else:
            print(f"Failed to find indices in {filepath}")

# Also update create_0914.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0914.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_pattern = re.compile(r'section3_content = """.*?</div>"""', re.DOTALL)
    new_script_block = f'section3_content = """{new_mom_cafe_section}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
