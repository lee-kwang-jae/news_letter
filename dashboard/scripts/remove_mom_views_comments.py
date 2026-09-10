# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def remove_views_and_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    m_start = content.find('<div id="mom-cafe">')
    c_start = content.find('<div id="culture">')

    if m_start != -1 and c_start != -1:
        mom_block = content[m_start:c_start]
        
        # Remove (조회수 ... / 댓글 ...) pattern from <h4> tags
        new_mom_block = re.sub(r'\s*\(조회수[^\)]*\)', '', mom_block)

        content = content[:m_start] + new_mom_block + content[c_start:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully removed views/comments from {file_path}")

remove_views_and_comments('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
remove_views_and_comments('d:/github/newsletter/newsletter/dashboard/news/index.html')
remove_views_and_comments('d:/github/newsletter/newsletter/dashboard/scripts/update_mom_cafe_0910.py')
