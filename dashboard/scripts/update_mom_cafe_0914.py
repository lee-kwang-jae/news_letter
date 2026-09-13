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
<h4>2️⃣ 미사 한강공원 &amp; 당정뜰 가을맞이 '어린이 생태 탐험단' 주말 무료 체험 선착순 접수 오픈</h4>
<div class="mom-detail"><strong>현황:</strong> 미사 한강공원과 당정뜰 야외 생태공원에서 가을철을 맞아 유아 및 초등학생 가족이 함께 참여하는 숲 체험, 야생화 탐방 및 곤충 관찰 주말 생태 프로그램 선착순 접수가 시작되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 주말 아이들과 멀리 나가지 않고 자연 속에서 무료로 즐기는 알찬 가을 야외 생태 체험활동.</div>
<div class="mom-reaction">💬 주민 반응: "주말에 아이들과 갈 만한 무료 생태 프로그램이라 선착순 바로 신청했습니다!", "가을 나들이 겸 생태 체험하기 딱 좋네요" 맘카페 관심 폭발.</div>
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

pattern = re.compile(r'<div id="mom-cafe">.*?</div>\s*(?=\n\n?<div id="culture")', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn(new_mom_cafe_section, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath} (replaced {count} occurrence)")
        else:
            print(f"Failed to match mom-cafe section in {filepath}")
    else:
        print(f"File not found: {filepath}")

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
