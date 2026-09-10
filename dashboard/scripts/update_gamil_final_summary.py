# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_inner_summary = """<b>"감일도서관 9월 독서의 달 프로그램 안내"</b><br/>
- 9월 프로그램 많은 관심 부탁드립니다!<br/>
링크를 누르시면 9월프로그램을 모두 확인가능합니다."""

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find article 3 summary block
    # Matches between <b>"감일도서관 9월 독서의 달 프로그램 안내"</b> and <div style="margin-top: 12px;
    pattern = r'(<b>"감일도서관 9월 독서의 달 프로그램 안내"</b>[\s\S]*?)(<div style="margin-top: 12px; font-size: 0\.9em; color: #718096;"><a href="https://www\.hanamlib\.go\.kr/gamlib/selectBbsNttView\.do)'
    
    if re.search(pattern, content):
        content = re.sub(pattern, new_inner_summary + '\n' + r'\2', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {file_path}")
    else:
        print(f"Pattern not found in {file_path}")

update_file('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
update_file('d:/github/newsletter/newsletter/dashboard/news/index.html')
update_file('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
