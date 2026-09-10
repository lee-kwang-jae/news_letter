# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

css_rule = """
        /* 썸네일 이미지 잘림 방지 (전체 비율 유지) */
        .img-box img {
            object-fit: contain !important;
            background-color: #ffffff !important;
        }
"""

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Replace inline object-fit: cover with object-fit: contain; background-color: #ffffff;
        content = content.replace("object-fit: cover;", "object-fit: contain; background-color: #ffffff;")
        
        # 2. Add CSS rule to <style> tag if not present
        if ".img-box img" not in content:
            content = content.replace("</style>", css_rule + "\n</style>")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated {filepath}")
    else:
        print(f"File not found: {filepath}")
