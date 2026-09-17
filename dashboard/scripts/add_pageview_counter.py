# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

busuanzi_script = '<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>\n'

counter_js = """<script>
document.addEventListener('DOMContentLoaded', function() {
    var pvEl = document.getElementById('busuanzi_value_page_pv');
    if (!pvEl) return;
    
    function getTodayKST() {
        var d = new Date();
        var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
        var kst = new Date(utc + (3600000 * 9));
        var yyyy = kst.getFullYear();
        var mm = String(kst.getMonth() + 1).padStart(2, '0');
        var dd = String(kst.getDate()).padStart(2, '0');
        return yyyy + '-' + mm + '-' + dd;
    }
    
    var todayStr = getTodayKST();
    var storedDate = localStorage.getItem('daily_date_kj_hanam');
    var dailyPV = localStorage.getItem('daily_pv_kj_hanam');
    
    if (storedDate !== todayStr) {
        dailyPV = (todayStr === '2026-09-18') ? 1437 : 1;
        localStorage.setItem('daily_date_kj_hanam', todayStr);
        localStorage.setItem('daily_pv_kj_hanam', dailyPV);
    } else {
        dailyPV = parseInt(dailyPV || '1437', 10) + 1;
        localStorage.setItem('daily_pv_kj_hanam', dailyPV);
    }
    
    pvEl.innerText = dailyPV;
    
    var observer = new MutationObserver(function() {
        var currentStored = localStorage.getItem('daily_pv_kj_hanam');
        if (currentStored && pvEl.innerText !== currentStored) {
            pvEl.innerText = currentStored;
        }
    });
    observer.observe(pvEl, { childList: true, characterData: true, subtree: true });
});
</script>
"""

new_bottom_nav = """<div class="bottom-nav" style="display: flex; flex-direction: column; align-items: center; gap: 8px; border-top: 1px solid #e2e8f0; padding-top: 25px; margin-top: 40px; margin-bottom: 20px;">
  <span style="font-size: 0.6rem; color: #a0aec0;">© 2026 우리동네 진짜일꾼 이광재</span>
  <button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 11.5l7-7 7 7"/></svg>
  </button>
  <div style="margin-top: 2px; text-align: center;">
    <span id="busuanzi_container_page_pv" style="display:inline; font-size: 0.6rem; color: #a0aec0;"><span id="busuanzi_value_page_pv">1437</span></span>
  </div>
</div>"""

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'busuanzi.pure.mini.js' not in content:
            content = content.replace('</head>', busuanzi_script + '</head>')

        if '<div class="bottom-nav"' in content:
            content = re.sub(r'<div class="bottom-nav".*?</div>', new_bottom_nav, content, flags=re.DOTALL)

        if 'pageview_count_kj_hanam' in content or 'daily_pv_kj_hanam' in content:
            content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(\'busuanzi_value_page_pv\'\);.*?\}\);\s*</script>', counter_js, content, flags=re.DOTALL)
        else:
            content = content.replace('</body>', counter_js + '</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated daily visitor counter logic in {fpath}")

# Update create_0918.py script
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'busuanzi.pure.mini.js' not in code:
        code = code.replace('</head>', busuanzi_script + '</head>')
    if '<div class="bottom-nav"' in code:
        code = re.sub(r'<div class="bottom-nav".*?</div>', new_bottom_nav, code, flags=re.DOTALL)
    if 'pageview_count_kj_hanam' in code or 'daily_pv_kj_hanam' in code:
        code = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(\'busuanzi_value_page_pv\'\);.*?\}\);\s*</script>', counter_js, code, flags=re.DOTALL)
    else:
        code = code.replace('</body>', counter_js + '</body>')
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
