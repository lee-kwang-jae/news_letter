# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

old_video_container = r'<div id="yt-container-shorts0918".*?</video>\s*</div>'

new_video_container = """<div id="yt-container-shorts0918" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-shorts0918" poster="./images/thumbnail-918.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_0918.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/A5H3SrB6qiE?feature=oembed" title="&quot;적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사&quot; 현장 숏폼" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>"""

clean_js = """function playNewsletterVideo() {
    var v = document.getElementById('video-shorts0918') || document.getElementsByTagName('video')[0];
    if (v) {
        v.scrollIntoView({ behavior: 'smooth', block: 'center' });
        if (v.paused) {
            var promise = v.play();
            if (promise !== undefined) {
                promise.catch(function(error) {
                    console.log("Video playback note:", error);
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

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '<div id="yt-container-shorts0918"' in content:
            content = re.sub(r'<div id="yt-container-shorts0918".*?</video>\s*</div>', new_video_container, content, flags=re.DOTALL)

        pattern = r'function playNewsletterVideo\(\)\s*\{.*?function playYoutubeInline\(videoId, element\)\s*\{\s*playNewsletterVideo\(\);\s*\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, clean_js, content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed video embed container & JS in {fpath}")

# Update create_0918.py script
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    if '<div id="yt-container-shorts0918"' in code:
        code = re.sub(r'<div id="yt-container-shorts0918".*?</video>\s*</div>', new_video_container, code, flags=re.DOTALL)
    pattern = r'function playNewsletterVideo\(\)\s*\{.*?function playYoutubeInline\(videoId, element\)\s*\{\s*playNewsletterVideo\(\);\s*\}'
    if re.search(pattern, code, flags=re.DOTALL):
        code = re.sub(pattern, clean_js, code, flags=re.DOTALL)
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
