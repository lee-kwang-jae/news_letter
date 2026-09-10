# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

new_bottom_nav = """<!-- 하단 맨위로 버튼 및 푸터 -->
<div class="bottom-nav" style="display: flex; flex-direction: column; align-items: center; gap: 14px; border-top: 1px solid #e2e8f0; padding-top: 25px; margin-top: 40px; margin-bottom: 20px;">
  <span style="font-size: 0.6rem; color: #a0aec0;">© 2026 우리동네 진짜일꾼 이광재</span>
  <button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 11.5l7-7 7 7"/></svg>
  </button>
</div>"""

def swap_order(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<!-- 하단 맨위로 버튼.*?>\s*<div class="bottom-nav".*?</div>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_bottom_nav, content, flags=re.DOTALL)
    else:
        content = re.sub(r'<div class="bottom-nav">.*?</div>', new_bottom_nav, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Swapped footer order in {file_path}")

swap_order('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
swap_order('d:/github/newsletter/newsletter/dashboard/news/index.html')
swap_order('d:/github/newsletter/newsletter/dashboard/scripts/update_center_top_btn.py')
swap_order('d:/github/newsletter/newsletter/dashboard/scripts/remove_floating_top_btn.py')
swap_order('d:/github/newsletter/newsletter/dashboard/scripts/add_sticky_header_and_top_btn.py')
