# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

old_text = '하남시 감일도서관에서 안내하는 최신 공지사항입니다. 감일·위례 지역 주민들이 이용 가능한 다양한 프로그램 및 도서관 관련 소식을 확인하실 수 있습니다.'
new_text = ' - 9월 프로그램 많은 관심 부탁드립니다!'

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_text in content:
        content = content.replace(old_text, new_text)
    else:
        # Fallback regex
        content = re.sub(r'하남시 감일도서관에서 안내하는 최신 공지사항입니다\.\s*감일·위례 지역 주민들이 이용 가능한 다양한 프로그램 및 도서관 관련 소식을 확인하실 수 있습니다\.', new_text, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

update_file('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
update_file('d:/github/newsletter/newsletter/dashboard/news/index.html')
update_file('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
update_file('d:/github/newsletter/newsletter/dashboard/scripts/replace_culture_0910.py')
