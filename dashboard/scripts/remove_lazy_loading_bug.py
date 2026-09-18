# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260918.html',
    r'd:\github\newsletter\newsletter\dashboard\scripts\create_0918.py',
    r'd:\github\newsletter\newsletter\dashboard\scripts\optimize_newsletter_performance.py'
]

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove loading="lazy" decoding="async" from img tags
        content = content.replace('loading="lazy" decoding="async" ', '')
        content = content.replace('loading="lazy" decoding="async"', '')
        content = content.replace('loading="lazy"', '')
        content = content.replace('decoding="async"', '')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed lazy loading from {fpath}")
