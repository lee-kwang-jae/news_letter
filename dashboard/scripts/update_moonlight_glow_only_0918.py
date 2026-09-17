# -*- coding: utf-8 -*-
import os
import re

css_addition = """
        /* ---- 추석 은은한 달빛 효과 (점선 회전 제거, 달빛 후광 유지) ---- */
        @keyframes moonlightGlow {
            0%, 100% {
                box-shadow: 0 0 10px rgba(254, 240, 138, 0.6), 0 0 20px rgba(253, 224, 71, 0.4);
            }
            50% {
                box-shadow: 0 0 22px rgba(254, 240, 138, 0.95), 0 0 38px rgba(253, 224, 71, 0.75);
            }
        }
        .moonlight-avatar-img {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            object-fit: contain;
            background-color: #ffffff;
            border: 2px solid #fef08a;
            position: relative;
            z-index: 1;
            animation: moonlightGlow 3s ease-in-out infinite alternate;
        }
"""

banner_html = """<a href="#" onclick="window.scrollTo({top: 0, behavior: 'smooth'}); return false;" style="text-decoration: none; color: inherit; display: block; cursor: pointer;">
  <div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 35%, #431407 80%, #78350f 100%); border: 2px solid #fbbf24; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.35); position: relative; padding: 10px 20px; border-radius: 10px;">
    <img src="./images/kjicon.png" alt="이광재 국회의원" class="moonlight-avatar-img">
    <span style="color: #fef08a; text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: bold; letter-spacing: -0.5px;">🌾 풍요로운 한가위 · 우리동네 국회의원 이광재 🎑</span>
  </div>
</a>"""

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

css_remove_pattern = re.compile(r'/\* ---- 추석 은은한 달빛 회전 효과 ---- \*/.*?(?=\.article-card|\n\s*</style>)', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old CSS addition if present
        content = css_remove_pattern.sub('', content)
        
        # Add new clean CSS
        if 'moonlightGlow' not in content:
            idx_style = content.find('</style>')
            if idx_style != -1:
                content = content[:idx_style] + css_addition + content[idx_style:]
        
        # Replace Banner HTML
        idx_lawmaker = content.find('<div id="lawmaker">')
        if idx_lawmaker != -1:
            idx_a_start = content.find('<a href="#"', idx_lawmaker)
            idx_a_end = content.find('</a>', idx_a_start)
            if idx_a_start != -1 and idx_a_end != -1:
                content = content[:idx_a_start] + banner_html + content[idx_a_end+4:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully updated (dashed ring removed) in {filepath}")

# Update create_0918.py script
create_script_path = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script_path):
    with open(create_script_path, 'r', encoding='utf-8') as f:
        script_code = f.read()
    
    script_code = css_remove_pattern.sub('', script_code)
    if 'moonlightGlow' not in script_code:
        idx_style = script_code.find('</style>')
        if idx_style != -1:
            script_code = script_code[:idx_style] + css_addition + script_code[idx_style:]
    
    idx_lawmaker = script_code.find('<div id="lawmaker">')
    if idx_lawmaker != -1:
        idx_a_start = script_code.find('<a href="#"', idx_lawmaker)
        idx_a_end = script_code.find('</a>', idx_a_start)
        if idx_a_start != -1 and idx_a_end != -1:
            script_code = script_code[:idx_a_start] + banner_html + script_code[idx_a_end+4:]
    
    with open(create_script_path, 'w', encoding='utf-8') as f:
        f.write(script_code)
    print(f"Successfully updated {create_script_path}")
