# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

redundant_text = '감일도서관 9월 독서의달 프로그램 안내<br/>'

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if redundant_text in content:
        content = content.replace(redundant_text, '')
    else:
        # Fallback regex search
        content = re.sub(r'감일도서관 9월 독서의달 프로그램 안내\s*<br/>\s*', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {file_path}")

clean_file('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
clean_file('d:/github/newsletter/newsletter/dashboard/news/index.html')
clean_file('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
clean_file('d:/github/newsletter/newsletter/dashboard/scripts/update_gamil_summary.py')
