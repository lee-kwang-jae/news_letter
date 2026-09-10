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
<h4>2️⃣ 하남 미사 한강공원 가을맞이 어린이 생태체험 및 힐링 주말 프로그램 신청 개시</h4>
<div class="mom-detail"><strong>현황:</strong> 미사 한강공원에서 가을철을 맞아 어린이와 학부모가 함께 참여하는 숲 체험, 야생화 관찰 및 주말 생태 교육 프로그램 선착순 접수가 시작되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 주말 아이들과 함께 멀리 나가지 않고 자연 속에서 즐기는 무료 생태체험활동.</div>
<div class="mom-reaction">💬 주민 반응: "주말에 아이들과 갈 만한 알찬 프로그램이 생겼네요!", "선착순 접수 바로 신청했습니다" 학부모 높은 관심.</div>
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
