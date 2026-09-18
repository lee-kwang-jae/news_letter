# -*- coding: utf-8 -*-
import os
import re

files = [
    'index.html',
    'dashboard/news/index.html',
    'dashboard/news/kj_hanam_inside_20260918.html'
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    dir_name = os.path.dirname(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    srcs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|jpeg|gif|mp4))["\']', html)
    print(f"=== {fpath} ({len(srcs)} media refs) ===")
    for src in set(srcs):
        if src.startswith('http'):
            continue
        rel_path = os.path.normpath(os.path.join(dir_name, src))
        exists = os.path.exists(rel_path)
        size = os.path.getsize(rel_path) if exists else 0
        print(f"  {src} -> {rel_path}: exists={exists}, size={size/1024:.1f}KB")
