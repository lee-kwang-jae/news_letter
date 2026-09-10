# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Cute chubby rounded stroke arrow
cute_svg_arrow = """<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 11.5l7-7 7 7"/></svg>"""

new_button = f"""<button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    {cute_svg_arrow}
  </button>"""

def update_button(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'<button onclick="scrollToTop\(\)".*?</button>'
    content = re.sub(pattern, new_button, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated cute thick arrow in {file_path}")

update_button('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
update_button('d:/github/newsletter/newsletter/dashboard/news/index.html')
update_button('d:/github/newsletter/newsletter/dashboard/scripts/enlarge_arrow_icon.py')
update_button('d:/github/newsletter/newsletter/dashboard/scripts/swap_footer_order.py')
update_button('d:/github/newsletter/newsletter/dashboard/scripts/update_center_top_btn.py')
