# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

old_title = '하남시 감일도서관 공지사항 안내'
new_title = '감일도서관 9월 독서의 달 프로그램 안내'

old_slogan = '<b>"감일도서관의 새로운 소식을 확인하세요!"</b>'
new_slogan = '<b>"감일도서관 9월 독서의 달 프로그램 안내"</b>'

old_link_btn = '공지사항 보기 (감일도서관) →'
new_link_btn = '프로그램 안내 보기 (감일도서관) →'

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_title, new_title)
    content = content.replace(old_slogan, new_slogan)
    content = content.replace(old_link_btn, new_link_btn)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}")

update_file('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
update_file('d:/github/newsletter/newsletter/dashboard/news/index.html')
update_file('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
update_file('d:/github/newsletter/newsletter/dashboard/scripts/replace_culture_0910.py')
