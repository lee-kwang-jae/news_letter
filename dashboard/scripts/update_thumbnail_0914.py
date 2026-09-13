# -*- coding: utf-8 -*-
import os
import shutil
import re

img_dir = r'd:\github\newsletter\newsletter\images'
dash_img_dir = r'd:\github\newsletter\newsletter\dashboard\news\images'

src_thumb = os.path.join(img_dir, 'thumbnail0914.jpg')
if not os.path.exists(src_thumb):
    src_thumb = os.path.join(img_dir, 'thumbnail-914.jpg')

assert os.path.exists(src_thumb), "Thumbnail 0914 image not found!"

aliases = ['thumbnail0914.jpg', 'thumbnail-914.jpg', 'thumb.jpg']

for name in aliases:
    dst1 = os.path.join(img_dir, name)
    dst2 = os.path.join(dash_img_dir, name)
    if os.path.abspath(src_thumb) != os.path.abspath(dst1):
        shutil.copy2(src_thumb, dst1)
    shutil.copy2(src_thumb, dst2)
    print(f"Copied {src_thumb} -> {dst1} and {dst2}")

# Now update the HTML files
target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260914.html'
]

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 1. Update image in first 현장일지 card (224409939684)
        html = html.replace('./images/0914-3.jpg', './images/thumbnail0914.jpg')
        html = html.replace('./images/0914-03.jpg', './images/thumbnail0914.jpg')
        html = html.replace('./images/thumbnail-914.jpg', './images/thumbnail0914.jpg')
        
        # 2. Update og:image & twitter:image for KakaoTalk share preview
        html = re.sub(
            r'<meta property="og:image" content="[^"]*"/>',
            '<meta property="og:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0914.jpg"/>',
            html
        )
        html = re.sub(
            r'<meta property="og:image:url" content="[^"]*"/>',
            '<meta property="og:image:url" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0914.jpg"/>',
            html
        )
        html = re.sub(
            r'<meta property="og:image:secure_url" content="[^"]*"/>',
            '<meta property="og:image:secure_url" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0914.jpg"/>',
            html
        )
        html = re.sub(
            r'<meta name="twitter:image" content="[^"]*"/>',
            '<meta name="twitter:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0914.jpg"/>',
            html
        )
        html = re.sub(
            r'<link rel="image_src" href="[^"]*"/>',
            '<link rel="image_src" href="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0914.jpg"/>',
            html
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Successfully updated HTML file: {fpath}")

# Update create_0914.py script as well
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0914.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('./images/0914-3.jpg', './images/thumbnail0914.jpg')
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
