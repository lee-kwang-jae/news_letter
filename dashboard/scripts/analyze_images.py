# -*- coding: utf-8 -*-
import os
from PIL import Image

img_dirs = ['images', 'dashboard/news/images']

print("=== Image Analysis ===")
for d in img_dirs:
    if os.path.exists(d):
        for f in os.listdir(d):
            fpath = os.path.join(d, f)
            if os.path.isfile(fpath) and f.lower().endswith(('.png', '.jpg', '.jpeg')):
                size_kb = os.path.getsize(fpath) / 1024
                if size_kb > 200:
                    try:
                        with Image.open(fpath) as img:
                            print(f"{fpath}: {img.size[0]}x{img.size[1]}, {size_kb:.1f} KB")
                    except Exception as e:
                        print(f"Error opening {fpath}: {e}")
