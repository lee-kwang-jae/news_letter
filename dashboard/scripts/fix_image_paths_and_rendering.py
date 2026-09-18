# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html',
    r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py'
]

for fpath in target_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace ./images/ with images/ for robust GitHub Pages path resolution
    content = content.replace('src="./images/', 'src="images/')

    # 2. Fix rigid height: 210px to flexible height: auto; max-height: 260px
    content = content.replace('height: 210px;', 'height: auto; max-height: 260px;')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed image paths and responsive styles in {fpath}")
