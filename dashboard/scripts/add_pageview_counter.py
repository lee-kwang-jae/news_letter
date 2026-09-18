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
(function() {
    function initMobileVisitorCounter() {
        var pvEl = document.getElementById('busuanzi_value_site_uv') || document.getElementById('busuanzi_value_page_pv');
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
        var dateKey = 'kj_hanam_mobile_pv_date';
        var countKey = 'kj_hanam_mobile_pv_count';
        var sessionKey = 'kj_hanam_counted_session_' + todayStr;
        
        var storedDate = localStorage.getItem(dateKey);
        var currentCount = parseInt(localStorage.getItem(countKey) || '0', 10);
        
        if (storedDate !== todayStr) {
            currentCount = 1;
            localStorage.setItem(dateKey, todayStr);
            localStorage.setItem(countKey, '1');
            try { sessionStorage.setItem(sessionKey, 'true'); } catch(e){}
        } else {
            var alreadyCounted = false;
            try { alreadyCounted = sessionStorage.getItem(sessionKey); } catch(e){}
            
            if (!alreadyCounted) {
                currentCount = Math.max(1, currentCount + 1);
                localStorage.setItem(countKey, currentCount.toString());
                try { sessionStorage.setItem(sessionKey, 'true'); } catch(e){}
            }
        }
        
        if (currentCount <= 0) currentCount = 1;
        pvEl.innerText = currentCount;
        
        var observer = new MutationObserver(function() {
            var raw = pvEl.innerText.replace(/[^0-9]/g, '');
            if (raw && parseInt(raw, 10) > 0) {
                var val = Math.max(parseInt(raw, 10), currentCount);
                pvEl.innerText = val;
                localStorage.setItem(countKey, val.toString());
            }
        });
        observer.observe(pvEl, { childList: true, characterData: true, subtree: true });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileVisitorCounter);
    } else {
        initMobileVisitorCounter();
    }
})();
</script>
"""

new_bottom_nav = """<div class="bottom-nav" style="display: flex; flex-direction: column; align-items: center; gap: 8px; border-top: 1px solid #e2e8f0; padding-top: 25px; margin-top: 40px; margin-bottom: 20px;">
  <span style="font-size: 0.6rem; color: #a0aec0;">© 2026 우리동네 진짜일꾼 이광재</span>
  <button onclick="scrollToTop()" title="맨위로" style="background: linear-gradient(135deg, #2b6cb0, #4299e1); color: white; border: none; width: 46px; height: 46px; border-radius: 50%; cursor: pointer; box-shadow: 0 4px 12px rgba(43,108,176,0.3); display: flex; align-items: center; justify-content: center; transition: transform 0.2s, box-shadow 0.2s;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 11.5l7-7 7 7"/></svg>
  </button>
  <div style="margin-top: 2px; text-align: center;">
    <span style="font-size: 0.6rem; color: #a0aec0;"><span id="busuanzi_value_site_uv">1</span></span>
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

        if '<script>\n(function() {\n    function initMobileVisitorCounter()' in content or 'kj_hanam_daily_date' in content or 'kj_hanam_live_visitor_pv' in content or 'pageview_count_kj_hanam' in content:
            content = re.sub(r'<script>\s*(?:\(function\(\)\s*\{)?\s*function initMobileVisitorCounter\(\).*?\)\(\);\s*</script>', counter_js, content, flags=re.DOTALL)
            content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(.*?\);.*?\}\);\s*</script>', counter_js, content, flags=re.DOTALL)
        else:
            content = content.replace('</body>', counter_js + '</body>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated universal mobile & PC visitor counter in {fpath}")

# Update create_0918.py script
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    if 'busuanzi.pure.mini.js' not in code:
        code = code.replace('</head>', busuanzi_script + '</head>')
    if '<div class="bottom-nav"' in code:
        code = re.sub(r'<div class="bottom-nav".*?</div>', new_bottom_nav, code, flags=re.DOTALL)
    if 'kj_hanam_daily_date' in code or 'kj_hanam_live_visitor_pv' in code or 'pageview_count_kj_hanam' in code or 'initMobileVisitorCounter' in code:
        code = re.sub(r'<script>\s*(?:\(function\(\)\s*\{)?\s*function initMobileVisitorCounter\(\).*?\)\(\);\s*</script>', counter_js, code, flags=re.DOTALL)
        code = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var pvEl = document\.getElementById\(.*?\);.*?\}\);\s*</script>', counter_js, code, flags=re.DOTALL)
    else:
        code = code.replace('</body>', counter_js + '</body>')
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
