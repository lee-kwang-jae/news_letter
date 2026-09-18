import os
import re

SCRIPT_CONTENT = """<script>
(function() {
    function initGlobalVisitorCounter() {
        var pvEl = document.getElementById('visitor_counter_val');
        if (!pvEl) return;
        
        var storageKey = 'kj_hanam_global_pv_backup';
        var cachedCount = localStorage.getItem(storageKey) || '1,437';
        pvEl.innerText = cachedCount;
        
        var pathId = 'lee-kwang-jae.news_letter.0918';
        var primaryUrl = 'https://api.visitorbadge.io/api/visitors?path=' + encodeURIComponent(pathId);
        
        try {
            var controller = new AbortController();
            var timeoutId = setTimeout(function() { controller.abort(); }, 3000);
            
            fetch(primaryUrl, { signal: controller.signal })
                .then(function(res) { return res.text(); })
                .then(function(svgText) {
                    clearTimeout(timeoutId);
                    var numStr = null;
                    var match = svgText.match(/VISITORS:\\s*(\\d+)/i);
                    if (match && match[1]) {
                        numStr = match[1];
                    } else {
                        var matches = svgText.match(/<text[^>]*>([^<]+)<\\/text>/g);
                        if (matches) {
                            for (var i = matches.length - 1; i >= 0; i--) {
                                var txt = matches[i].replace(/<[^>]+>/g, '').trim();
                                if (/^\\d+$/.test(txt)) {
                                    numStr = txt;
                                    break;
                                }
                            }
                        }
                    }
                    
                    if (numStr) {
                        var val = parseInt(numStr, 10);
                        if (val < 1437) {
                            val = val + 1437;
                        }
                        pvEl.innerText = val.toLocaleString();
                        localStorage.setItem(storageKey, val.toLocaleString());
                    }
                })
                .catch(function(err) {
                    // Fallback remains cachedCount
                });
        } catch(e) {}
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGlobalVisitorCounter);
    } else {
        initGlobalVisitorCounter();
    }
})();
</script>"""

FILES_TO_UPDATE = [
    r"d:\github\newsletter\newsletter\index.html",
    r"d:\github\newsletter\newsletter\dashboard\news\index.html",
    r"d:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html"
]

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace existing visitor counter script block
    pattern = re.compile(r'<script>\s*\(function\(\)\s*\{\s*function initVisitorCounter\(\).*?</script>', re.DOTALL)
    if pattern.search(content):
        new_content = pattern.sub(lambda m: SCRIPT_CONTENT, content)
    else:
        new_content = content.replace("</body>", f"{SCRIPT_CONTENT}\n</body>")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {filepath}")

for path in FILES_TO_UPDATE:
    update_file(path)

print("Visitor counter script update complete!")
