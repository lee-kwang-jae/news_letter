# -*- coding: utf-8 -*-
import os
import re

new_mom_cafe_section = """<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 11일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ '미사·감일 3·9호선 연장선' 세부 승인 속도 및 착공 가시화 소식에 맘카페 열띤 호응</h4>
<div class="mom-detail"><strong>현황:</strong> 하남 미사강변도시 및 감일지구를 경유하는 지하철 3호선·9호선 연장 사업의 세부 절차가 순조롭게 추진되며 2026년 하반기 착공 준비가 가시화되고 있다는 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 강남·여의도 직주근접 출퇴근 환경 대폭 개선 및 미사·감일 학부모 교통 복지·지역 가치 상승 기대.</div>
<div class="mom-reaction">💬 주민 반응: "3호선과 9호선 착공 소식만 기다리고 있었는데 드디어!", "아이들 서울 학원가 이동이랑 주말 이동이 훨씬 편해지겠네요" 미사·감일 맘카페 환호.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 하남시 초·중·고 통학로 '공유킥보드 무단방치 30분 즉시 견인' 단속 강화 소식에 학부모 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시의회(정병용 의장)가 관계자 간담회를 열고 등하굣길 안전을 위협하던 인도 및 스쿨존 내 공유킥보드 무단방치 방지를 위해 단속 기준 시간을 30분으로 단축하고 강력한 견인 단속을 추진한다는 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 초·중·고 등하굣길 학생 보행 안전 확보 및 보행자 충돌 사고 위험 사전 차단.</div>
<div class="mom-reaction">💬 주민 반응: "학교 앞 횡단보도와 인도에 막 방치되어 있어서 위험했는데 30분 견인 조치 너무 반갑습니다!", "학부모 안심 통학로 조성을 환영합니다" 맘카페 열띤 호응.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ '2026 하남 이성산성 문화제' 어린이 역사체험·가족 버스투어 사전예약에 학부모 관심 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 오는 9월 19일 개막하는 '2026 하남 이성산성 문화제'의 하남여행버스 및 어린이 유적 체험 프로그램 사전 접수가 오픈되었다는 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 가을 주말 가족 단위 역사 문화 체험 및 하남 이성산성 야외 버스투어 선착순 참여 가능.</div>
<div class="mom-reaction">💬 주민 반응: "작년에도 광속 마감이었는데 올해는 꼭 예약 성공하고 싶네요!", "아이와 가을 주말 나들이 가기 딱 좋은 축제" 맘카페 기대 만발.</div>
</div>
</div>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
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
