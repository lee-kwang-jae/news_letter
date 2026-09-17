# -*- coding: utf-8 -*-
import os
import re

banner_html = """<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">우리동네 국회의원 이광재</span>
  </div>
</a>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        idx_lawmaker = content.find('<div id="lawmaker">')
        if idx_lawmaker != -1:
            idx_a_start = content.find('<a href="#"', idx_lawmaker)
            idx_a_end = content.find('</a>', idx_a_start)
            if idx_a_start != -1 and idx_a_end != -1:
                content = content[:idx_a_start] + banner_html + content[idx_a_end+4:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated banner (removed '풍요로운 한가위') in {filepath}")

# Update create_0918.py script as well
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    idx_lawmaker = script_code.find('<div id="lawmaker">')
    if idx_lawmaker != -1:
        idx_a_start = script_code.find('<a href="#"', idx_lawmaker)
        idx_a_end = script_code.find('</a>', idx_a_start)
        if idx_a_start != -1 and idx_a_end != -1:
            script_code = script_code[:idx_a_start] + banner_html + script_code[idx_a_end+4:]
    
    with open(create_script_path, 'w', encoding='utf-8') as f:
        f.write(script_code)
    print(f"Successfully updated {create_script_path}")
