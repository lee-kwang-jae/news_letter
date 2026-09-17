# -*- coding: utf-8 -*-
import os
import shutil

src_img = 'images/thumbnail-918.jpg'
dest_img_news = 'dashboard/news/images/thumbnail-918.jpg'

if os.path.exists(src_img):
    os.makedirs('dashboard/news/images', exist_ok=True)
    shutil.copy(src_img, dest_img_news)
    print(f"Copied {src_img} to {dest_img_news}")

target_files = [
    'index.html',
    'dashboard/news/index.html',
    'dashboard/news/kj_hanam_inside_20260918.html',
    'dashboard/scripts/create_0918.py'
]

for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if './images/091808.jpg' in content:
            content = content.replace('./images/091808.jpg', './images/thumbnail-918.jpg')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated image in {file_path}")
        else:
            print(f"./images/091808.jpg not found in {file_path}")
    else:
        print(f"File not found: {file_path}")
