# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

pattern = re.compile(r'📌 출처: 뉴스프리존 \(김정수 기자\)\s*</div>\s*</div>\s*<div class="source">\s*📌 출처: 서울신문 \(양승현 리포터\)\s*</div>\s*</div>', re.DOTALL)
replacement = '📌 출처: 뉴스프리존 (김정수 기자)\n</div>\n</div>'

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn(replacement, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Cleaned up {filepath} ({count} occurrence)")
        else:
            print(f"No leftover found in {filepath}")
