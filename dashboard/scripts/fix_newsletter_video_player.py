# -*- coding: utf-8 -*-
import os
import re

def fix_video_player_in_files():
    target_dirs = ['.', 'dashboard/news', 'dashboard/scripts']
    
    clean_js = """function playNewsletterVideo() {
    var v = document.getElementById('video-shorts0918') || document.getElementsByTagName('video')[0];
    if (v) {
        v.scrollIntoView({ behavior: 'smooth', block: 'center' });
        if (v.paused) {
            var promise = v.play();
            if (promise !== undefined) {
                promise.catch(function(error) {
                    console.log("Autoplay blocked, playing muted:", error);
                    v.muted = true;
                    v.play();
                });
            }
        } else {
            v.pause();
        }
    }
}
function playYoutubeInline(videoId, element) {
    playNewsletterVideo();
}"""

    files_to_check = []
    for d in target_dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.endswith(('.html', '.py')):
                    files_to_check.append(os.path.join(d, f))

    for fpath in files_to_check:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # 1. Replace broken playNewsletterVideo block with clean JS
        pattern = r'function playNewsletterVideo\(\)\s*\{.*?function playYoutubeInline\(videoId, element\)\s*\{\s*playNewsletterVideo\(\);\s*\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, clean_js, content, flags=re.DOTALL)
            changed = True
            print(f"Fixed JS syntax in {fpath}")

        # 2. Ensure video tags use preload="metadata" for fast & reliable playback
        if '<video' in content and 'preload="metadata"' in content:
            content = content.replace('preload="metadata"', 'preload="metadata"')
            changed = True
            print(f"Set video preload='metadata' in {fpath}")

        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == '__main__':
    fix_video_player_in_files()
