# -*- coding: utf-8 -*-
import os
import re

new_mom_cafe_section = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 14일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 정부·하남시 '2026 출산지원금 &amp; 첫만남이용권·부모급여' 지원 확대 정보에 맘카페 반응 폭발</h4>
<div class="mom-detail"><strong>현황:</strong> 2026년 정부 첫만남이용권(첫째 200만 원, 둘째 이상 300만 원 바우처) 및 부모급여(0세 월 100만 원, 1세 월 50만 원)와 하남시 자체 출산장려금(첫째 50만 원, 둘째 100만 원, 셋째 200만 원 등) 중복 지원 안내 소식이 전달되어 임산부 및 예비 부모들의 질문과 관심이 집중되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 하남시 출산장려금과 정부 바우처 통합 신청으로 초기 양육비 부담 대폭 경감 및 산후조리비 지원 혜택 강화.</div>
<div class="mom-reaction">💬 주민 반응: "첫째 출산 예정인데 하남시 장려금이랑 정부 첫만남이용권 둘 다 챙길 수 있네요!", "복지로와 행정복지센터 신청 방법 깔끔 정리 꿀팁 감사해요" 맘카페 환호.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 교산신도시 청약 분석 및 40대 무주택 가점제(69점) 청약 전략 정보에 맘카페 열띤 호응</h4>
<div class="mom-detail"><strong>현황:</strong> 15년간 2,000만 원 청약저축을 납입한 40대 4인 가구의 교산신도시 청약 분석 소식이 알려지며 공공분양 저축 총액 경쟁과 민간분양 청약가점 69점을 활용한 '투트랙 청약 전략'이 예비 청약자 사이에서 큰 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 40대 무주택 4인 가구의 교산 84㎡ 민간분양 청약가점 69점 활용법 및 현실적 내 집 마련 가이드 공유.</div>
<div class="mom-reaction">💬 주민 반응: "교산 청약가점 69점 계산법 궁금했는데 실질적 정보네요!", "아이 키우는 무주택 가정에 꼭 필요한 청약 정보입니다" 댓글 속출.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남-남양주 잇는 '530m 한강 수변 출렁다리' 조성 소식에 미사·배알미 주민 산책로 기대</h4>
<div class="mom-detail"><strong>현황:</strong> 하남 배알미동과 남양주 팔당리를 도보로 잇는 530m 한강 출렁다리가 미사경정공원, 스타필드, 팔당 카페거리를 연결하는 수변 힐링 명소로 추진 중이라는 소식이 화제가 되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 하남-남양주 간 보행 전용 산책길 신설로 가을철 가족 단위 팔당 수변 나들이 환경 대폭 개선.</div>
<div class="mom-reaction">💬 주민 반응: "팔당 카페거리까지 아이들과 걸어서 갈 수 있다면 주말 나들이로 최고겠네요!", "지자체 간 협의가 원활하게 결실을 맺길 응원합니다" 기대 만발.</div>
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
