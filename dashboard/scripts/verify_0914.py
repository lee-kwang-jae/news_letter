# -*- coding: utf-8 -*-
import os

files = [
    'index.html',
    'dashboard/news/index.html',
    'dashboard/news/kj_hanam_inside_20260914.html'
]

# Check video MP4 files
assert os.path.exists('images/shorts_0914.mp4'), "images/shorts_0914.mp4 does not exist"
assert os.path.exists('dashboard/news/images/shorts_0914.mp4'), "dashboard/news/images/shorts_0914.mp4 does not exist"

for fpath in files:
    print(f"=== Verification for {fpath} ===")
    assert os.path.exists(fpath), f"{fpath} does not exist"
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    assert '39호 | 2026년 9월 14일 발행' in html, "Issue text missing"
    assert 'id="lawmaker"' in html, "#lawmaker section missing"
    assert 'id="local-news"' in html, "#local-news section missing"
    assert 'id="mom-cafe"' in html, "#mom-cafe section missing"
    assert 'id="culture"' in html, "#culture section missing"
    assert 'id="public-news"' in html, "#public-news section missing"
    assert 'shorts_0914.mp4' in html, "shorts_0914.mp4 reference missing"
    assert 'video-yclRLijNE14' in html, "video-yclRLijNE14 ID missing"
    assert 'playNewsletterVideo()' in html, "playNewsletterVideo function call missing"

print("SUCCESS: Video card and YouTube Shorts embedding verified successfully!")
