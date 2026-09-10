# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

top_banner_old = re.compile(r'<div class="header-box">\s*<img src="\./images/top01\.png".*?>', re.DOTALL)
top_banner_new = """<div class="header-box">
  <a href="index.html" style="display: block; text-decoration: none; cursor: pointer;" title="홈으로 이동">
    <img src="./images/top01.png" alt="매일전하는 이광재의원의 하남인사이드" style="width: 100%; height: auto; display: block; cursor: pointer;" onerror="this.src='./images/top.png'">
  </a>"""

kjicon_old = re.compile(r'<img src="\./images/kjicon\.png"[^>]+>', re.DOTALL)
kjicon_new = """<a href="index.html" style="display: inline-flex; align-items: center; justify-content: center; text-decoration: none; cursor: pointer;" title="홈으로 이동">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer; transition: transform 0.2s ease;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
  </a>"""

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Avoid double-wrapping top banner
        if '<a href="index.html"' not in content:
            content = top_banner_old.sub(top_banner_new, content)
            content = kjicon_old.sub(kjicon_new, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully updated {filepath}")
        else:
            # Update kjicon if top banner already wrapped
            content = kjicon_old.sub(kjicon_new, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated kjicon in {filepath}")
    else:
        print(f"File not found: {filepath}")
