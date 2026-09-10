# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

old_span = '<span style="font-size: 0.88rem; color: #718096;">© 2026 우리동네 진짜일꾼 이광재</span>'
new_span = '<span style="font-size: 0.6rem; color: #a0aec0;">© 2026 우리동네 진짜일꾼 이광재</span>'

def update_font(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_span in content:
        content = content.replace(old_span, new_span)
    else:
        # Fallback regex search
        content = re.sub(r'<span style="font-size:\s*[\d\.]+rem;\s*color:\s*#[a-fA-F0-9]+;">© 2026 우리동네 진짜일꾼 이광재</span>', new_span, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated font size in {file_path}")

update_font('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
update_font('d:/github/newsletter/newsletter/dashboard/news/index.html')
update_font('d:/github/newsletter/newsletter/dashboard/scripts/swap_footer_order.py')
update_font('d:/github/newsletter/newsletter/dashboard/scripts/update_center_top_btn.py')
