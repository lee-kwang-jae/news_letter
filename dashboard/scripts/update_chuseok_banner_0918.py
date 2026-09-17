# -*- coding: utf-8 -*-
import os
import re

new_chuseok_banner_html = """<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: contain; background-color: #ffffff; vertical-align: middle; cursor: pointer; border: 2px solid #fef08a; box-shadow: 0 0 10px rgba(254, 240, 138, 0.7);">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">🌾 풍요로운 한가위 · 우리동네 국회의원 이광재 🎑</span>
  </div>
</a>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

pattern = re.compile(r'<a href="#" onclick="window\.scrollTo\(\{top: 0, behavior: \'smooth\'\}\); return false;".*?🌾 풍요로운 한가위 · 우리동네 국회의원 이광재 🎑</span>\s*</div>\s*</a>', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        idx_lawmaker = content.find('<div id="lawmaker">')
        if idx_lawmaker != -1:
            idx_a_start = content.find('<a href="#"', idx_lawmaker)
            idx_a_end = content.find('</a>', idx_a_start)
            if idx_a_start != -1 and idx_a_end != -1:
                updated_content = content[:idx_a_start] + new_chuseok_banner_html + content[idx_a_end+4:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Successfully updated banner (removed moon icon) in {filepath}")
            else:
                print(f"Failed to locate a tag in {filepath}")
        else:
            print(f"Failed to find #lawmaker in {filepath}")

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
            updated_script_code = script_code[:idx_a_start] + new_chuseok_banner_html + script_code[idx_a_end+4:]
            with open(create_script_path, 'w', encoding='utf-8') as f:
                f.write(updated_script_code)
            print(f"Successfully updated {create_script_path}")
