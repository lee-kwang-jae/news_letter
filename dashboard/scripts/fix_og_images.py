# -*- coding: utf-8 -*-
import os
import re

files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260914.html'
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Replace 0911 thumbnail with 0914 thumbnail in head meta tags
        html = html.replace('images/thumbnail0911.jpg', 'images/thumbnail0914.jpg')
        html = html.replace('images/thumb.jpg', 'images/thumbnail0914.jpg')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated meta tags in {fpath}")

# Also update create_0914.py
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0914.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    
    code = code.replace('images/thumbnail0911.jpg', 'images/thumbnail0914.jpg')
    code = code.replace('images/thumb.jpg', 'images/thumbnail0914.jpg')
    
    # Add head meta tag update in create_0914.py
    if 'content = content.replace("images/thumbnail0911.jpg", "images/thumbnail0914.jpg")' not in code:
        code = code.replace(
            'content = content.replace("2026년 9월 11일 기준", "2026년 9월 14일 기준")',
            'content = content.replace("2026년 9월 11일 기준", "2026년 9월 14일 기준")\ncontent = content.replace("images/thumbnail0911.jpg", "images/thumbnail0914.jpg")\ncontent = content.replace("images/thumb.jpg", "images/thumbnail0914.jpg")'
        )
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
