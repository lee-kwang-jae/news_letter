# -*- coding: utf-8 -*-
import os

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html',
    r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
]

leftover = """<div class="source">
📌 출처: 경기일보 (김영호 기자)
</div>
</div>"""

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if leftover in content:
            updated_content = content.replace(leftover, '', 1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Cleaned leftover in {filepath}")
        else:
            print(f"Leftover not found in {filepath}")
