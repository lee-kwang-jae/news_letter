# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_mom_cafe_html = """<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 9일~10일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 서하남농협 감북 하나로마트 9월 17일 개장 소식 및 오픈 특가 행사에 감북·감일·위례 맘카페 들썩</h4>
<div class="mom-detail"><strong>현황:</strong> 서하남농협 감북 하나로마트가 오는 9월 17일 정식 개장을 앞두고 오픈 기념 농축수산물 할인 이벤트와 사은품 증정 소식이 알려지면서 지역 맘카페를 중심으로 장보기 정보 공유글이 급증했습니다.</div>
<div class="mom-point">💡 주민 포인트: 대형 신규 마트 개장에 따른 장보기 편의 대폭 향상 및 추석 명절 전 신선식품·한우 특가 쇼핑 정보.</div>
<div class="mom-reaction">💬 주민 반응: "감북동 쪽에 대형 하나로마트가 들어서서 장보기 너무 편해지겠어요!", "추석 선물세트랑 명절 장보기 여기서 해결해야겠어요" 환호.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 미사호수공원 '워터스크린' 3수 끝 시의회 예산 심의 소식에 미사·풍산 맘카페 관심 집중</h4>
<div class="mom-detail"><strong>현황:</strong> 두 차례 부결되었던 미사호수공원 워터스크린 설치 사업이 하남시의회 추경 심의에 재상정된다는 소식이 전해지며 미사·풍산 지역 맘카페에서 야경 명소화에 대한 기대감이 고조되고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 기존 음악분수와 연계한 레이저·워터스크린 야간 볼거리 조성 및 가족 산책 코스 활성화.</div>
<div class="mom-reaction">💬 주민 반응: "이번엔 꼭 시의회 문턱을 넘어 미사호수공원 야경이 더 멋져졌으면 좋겠어요!", "아이들과 밤산책 갈 때 색다른 볼거리가 생기겠네요" 응원.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 자녀와 함께하는 9월 '가족 플로깅 봉사활동' 모집 소식에 학부모 문의 및 신청 열기 폭주</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시 모두가족봉사단에서 주관하는 9월 가을맞이 가족 플로깅(쓰레기 줍기) 환경 봉사 프로그램 모집에 초·중등 자녀를 둔 학부모들의 참여 신청과 봉사시간 인정 문의가 이어졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 1365 자원봉사 포털 연계 봉사시간 인정 및 가을철 가족 단위 야외 환경보호 체험활동.</div>
<div class="mom-reaction">💬 주민 반응: "아이에게 환경보호 실습도 시켜주고 봉사시간도 챙길 수 있어 바로 등록했어요", "가족이 함께 가을바람 쐬며 의미 있는 시간 보내기 좋아 보여요" 호응.</div>
</div>
</div>"""

def replace_mom_cafe(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    m_start = content.find('<div id="mom-cafe">')
    c_start = content.find('<div id="culture">')

    if m_start != -1 and c_start != -1:
        content = content[:m_start] + new_mom_cafe_html + '\n\n' + content[c_start:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated mom-cafe section in {file_path}")

replace_mom_cafe('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
replace_mom_cafe('d:/github/newsletter/newsletter/dashboard/news/index.html')
