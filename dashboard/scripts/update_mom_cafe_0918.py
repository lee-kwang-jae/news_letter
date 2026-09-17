# -*- coding: utf-8 -*-
import os
import re

new_section_full = """<hr/>
<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 18일 기준 하남 지역 커뮤니티(맘카페)에서 화제성과 댓글이 가장 폭발했던 HOT 이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ "이번 주말 아이와 어디 가시나요?" 2026 하남이성산성문화제(9/19~20) 개막 소식에 맘카페 '기대 만발'</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 대표 가을축제인 '2026 하남이성산성문화제'가 9월 19일(토)~20일(일) 미사호수공원 잔디광장과 이성산성 일원에서 개최된다는 소식이 전해지면서, 아이와 함께할 주말 나들이 코스로 맘카페 게시판이 들썩이고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 큰별쌤 최태성 역사콘서트, 개막 주제공연, 어린이 랜덤플레이댄스, 다채로운 체험 부스 운영 등 전 세대 가족 참여 프로그램 풍성.</div>
<div class="mom-reaction">💬 주민 반응: "최태성 선생님 역사 콘서트 아이들이랑 꼭 들으러 가야겠어요!", "주말 미사호수공원 잔디광장 자리 잡기 치열하겠네요", "가족 주말 나들이로 딱입니다" 맘카페 추천 이어져.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ "우리 아이 등하굣길 한층 안전해진다!" 개학기 초등학교 통학로 불법주정차·유해환경 집중 단속 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시가 2학기 개학기를 맞아 관내 초등학교 주변 어린이보호구역(스쿨존) 내 불법주정차 단속을 강화하고, 통학로 유해 광고물 정비 및 룸카페·편의점 청소년 유해환경 집중 점검에 나섰다는 소식에 학부모 엄마들의 열띤 호응이 이어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 초등학교 어린이보호구역 통학로 안전 강화, 불법 주정차 단속 및 청소년 유해환경 집중 정비.</div>
<div class="mom-reaction">💬 주민 반응: "학교 앞 횡단보도 불법 주정차 때문에 늘 불안했는데 단속 강화되어 다행이에요!", "아이들 안심 통학로 조성을 적극 환영합니다" 맘카페 학부모 찬사.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ "우리 동네 생활 사업 주민이 직접 뽑았다!" 13개 동 주민총회 성료… '어린이 플로깅 &amp; 미술대회' 확정 관심</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 13개 동에서 약 4,800여 명의 주민이 직접 투표에 참여한 2026년 동별 주민총회가 성공적으로 마무리되며, '망월천 어린이 플로깅', '나룰어린이 미술대회', '치매예방 웃음치료' 등 주민 생활 밀착형 2027년 사업들이 확정되어 맘카페에서 큰 화제를 모았습니다.</div>
<div class="mom-point">💡 주민 포인트: 13개 동 주민참여예산 직접 투표 결과 및 아이·가족 맞춤형 마을 사업 확정.</div>
<div class="mom-reaction">💬 주민 반응: "아이와 함께 손잡고 가서 투표했던 어린이 플로깅 사업이 선정되어 정말 기뻐요!", "우리 동네에 꼭 필요한 사업들이 잘 집행되면 좋겠네요" 맘카페 따뜻한 호응.</div>
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
        
        idx_local = content.find('<div id="local-news">')
        idx_culture = content.find('<div id="culture">')
        if idx_local != -1 and idx_culture != -1:
            idx_hr = content.find('<hr/>', idx_local)
            if idx_hr != -1 and idx_hr < idx_culture:
                updated_content = content[:idx_hr] + new_section_full + '\n\n' + content[idx_culture:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Successfully updated {filepath}")
            else:
                print(f"Failed to find hr in {filepath}")
        else:
            print(f"Failed to find indices in {filepath}")

# Also update create_0918.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_pattern = re.compile(r'section3_content = """.*?</div>"""', re.DOTALL)
    new_script_block = f'section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->\n{new_section_full[5:]}"""'
    updated_script_code, s_count = script_pattern.subn(new_script_block, script_code)
    if s_count > 0:
        with open(create_script_path, 'w', encoding='utf-8') as f:
            f.write(updated_script_code)
        print(f"Successfully updated {create_script_path}")
