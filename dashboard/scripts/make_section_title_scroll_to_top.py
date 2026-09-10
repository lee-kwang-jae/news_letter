# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

pattern = re.compile(
    r'<div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">\s*'
    r'<a href="index\.html".*?>\s*'
    r'<img src="\./images/kjicon\.png".*?>\s*'
    r'</a>\s*'
    r'<span>우리동네 국회의원 이광재</span>\s*'
    r'</div>',
    re.DOTALL
)

replacement = """<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer;">
    <span>우리동네 국회의원 이광재</span>
  </div>
</a>"""

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn(replacement, content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully updated {filepath} ({count} occurrence)")
        else:
            print(f"Failed to match pattern in {filepath}")
    else:
        print(f"File not found: {filepath}")
