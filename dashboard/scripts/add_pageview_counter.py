# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

new_bottom_nav = """<div class="bottom-nav" style="display: flex; flex-direction: column; align-items: center; gap: 8px; border-top: 1px solid #e2e8f0; padding-top: 25px; margin-top: 40px; margin-bottom: 20px;">
  <span style="font-size: 0.6rem; color: #a0aec0;">© 2026 우리동네 진짜일꾼 이광재</span>
  <button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 11.5l7-7 7 7"/></svg>
  </button>
  <div style="margin-top: 2px; text-align: center;">
    <span style="font-size: 0.6rem; color: #a0aec0;">1437</span>
  </div>
</div>"""

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove busuanzi script from head
        content = content.replace('<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>\n', '')
        content = content.replace('<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>', '')

        # Update bottom-nav to static HTML
        if '<div class="bottom-nav"' in content:
            content = re.sub(r'<div class="bottom-nav".*?</div>', new_bottom_nav, content, flags=re.DOTALL)

        # Remove dynamic counter scripts
        content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(\'busuanzi_value_page_pv\'\);.*?\}\);\s*</script>', '', content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated static visitor counter in {fpath}")

# Update create_0918.py script
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>\n', '')
    code = code.replace('<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>', '')
    if '<div class="bottom-nav"' in code:
        code = re.sub(r'<div class="bottom-nav".*?</div>', new_bottom_nav, code, flags=re.DOTALL)
    code = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(\'busuanzi_value_page_pv\'\);.*?\}\);\s*</script>', '', code, flags=re.DOTALL)
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
