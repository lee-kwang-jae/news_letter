# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('[시정/공지] 하남시청 공지사항 안내', '[시정/공지] 2026년 하남시 청년의 날 기념 「청년 명랑 운동회」 개최')
pattern = r'<b>"하남시청에서 전하는 최신 공지사항입니다!"</b>\s*<br/>\s*하남시청 공식 홈페이지에서 공지하는 시정 관련 최신 소식입니다\.\s*하남시민 생활과 밀접한 행정 정보를 확인하실\s*수\s*있습니다\.'
replacement = '<b>"2026년 하남시 청년의 날 기념 「청년 명랑 운동회」 개최"</b><br/>\n2026년 청년의 날을 맞아 지역 청년 간 네트워킹 기회 마련을 위해 2025년 청년 명랑 운동회를 아래와 같이 개최하오니 많은 관심 바랍니다.'

code = re.sub(pattern, replacement, code)

with open('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_0910_clean.py script successfully!")
