# -*- coding: utf-8 -*-
import os
import shutil
import re

img_dir = r'd:\github\newsletter\newsletter\images'
dash_img_dir = r'd:\github\newsletter\newsletter\dashboard\news\images'

src_thumb = os.path.join(img_dir, 'thumbnail-918.jpg')
if not os.path.exists(src_thumb):
    src_thumb = os.path.join(img_dir, 'thumbnail0918.jpg')

assert os.path.exists(src_thumb), "Thumbnail image not found!"

# Include thumbnail-0918.jpg as an alias and primary filename
aliases = ['thumbnail-0918.jpg', 'thumbnail-918.jpg', 'thumbnail0918.jpg', 'thumb.jpg']

for name in aliases:
    dst1 = os.path.join(img_dir, name)
    dst2 = os.path.join(dash_img_dir, name)
    if os.path.abspath(src_thumb) != os.path.abspath(dst1):
        shutil.copy2(src_thumb, dst1)
    if os.path.abspath(src_thumb) != os.path.abspath(dst2):
        shutil.copy2(src_thumb, dst2)
    print(f"Copied {src_thumb} -> {dst1} and {dst2}")

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html'
]

og_img_url = "https://lee-kwang-jae.github.io/news_letter/images/thumbnail-0918.jpg"

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Update og:image & twitter:image meta tags for KakaoTalk preview
        html = re.sub(
            r'<meta property="og:image" content="[^"]*"/>',
            f'<meta property="og:image" content="{og_img_url}"/>',
            html
        )
        html = re.sub(
            r'<meta property="og:image:url" content="[^"]*"/>',
            f'<meta property="og:image:url" content="{og_img_url}"/>',
            html
        )
        html = re.sub(
            r'<meta property="og:image:secure_url" content="[^"]*"/>',
            f'<meta property="og:image:secure_url" content="{og_img_url}"/>',
            html
        )
        html = re.sub(
            r'<meta name="twitter:image" content="[^"]*"/>',
            f'<meta name="twitter:image" content="{og_img_url}"/>',
            html
        )
        html = re.sub(
            r'<link rel="image_src" href="[^"]*"/>',
            f'<link rel="image_src" href="{og_img_url}"/>',
            html
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Successfully updated og:image in HTML file: {fpath}")

# Update create_0918.py script as well
create_script = r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
if os.path.exists(create_script):
    with open(create_script, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('images/thumbnail0918.jpg', 'images/thumbnail-0918.jpg')
    code = code.replace('images/thumbnail-918.jpg', 'images/thumbnail-0918.jpg')
    with open(create_script, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Updated {create_script}")
