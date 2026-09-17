# -*- coding: utf-8 -*-
import os
import re
from PIL import Image

def optimize_images():
    img_dirs = ['images', 'dashboard/news/images']
    total_saved = 0

    for d in img_dirs:
        if not os.path.exists(d):
            continue
        for f in os.listdir(d):
            fpath = os.path.join(d, f)
            if not os.path.isfile(fpath):
                continue
            
            fname_lower = f.lower()
            if not fname_lower.endswith(('.png', '.jpg', '.jpeg')):
                continue

            orig_size = os.path.getsize(fpath)
            
            try:
                with Image.open(fpath) as img:
                    width, height = img.size
                    
                    # 1. Special case: kjicon.png (used as 48x48 avatar icon)
                    if fname_lower == 'kjicon.png':
                        if width > 256:
                            img = img.resize((256, 256), Image.Resampling.LANCZOS)
                        img.save(fpath, format='PNG', optimize=True)
                    
                    # 2. JPEG optimization
                    elif fname_lower.endswith(('.jpg', '.jpeg')):
                        # Resize if excessively large resolution (width > 1280 for content images)
                        if width > 1280:
                            new_h = int(height * (1280 / width))
                            img = img.resize((1280, new_h), Image.Resampling.LANCZOS)
                        
                        # Convert RGBA to RGB if needed
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGB')
                            
                        img.save(fpath, format='JPEG', quality=82, optimize=True)
                    
                    # 3. PNG optimization
                    elif fname_lower.endswith('.png'):
                        if width > 1280:
                            new_h = int(height * (1280 / width))
                            img = img.resize((1280, new_h), Image.Resampling.LANCZOS)
                        
                        img.save(fpath, format='PNG', optimize=True)
                        
                new_size = os.path.getsize(fpath)
                saved = orig_size - new_size
                if saved > 0:
                    total_saved += saved
                    print(f"Optimized {fpath}: {orig_size/1024:.1f}KB -> {new_size/1024:.1f}KB (Saved {saved/1024:.1f}KB)")
            except Exception as e:
                print(f"Error optimizing {fpath}: {e}")
                
    print(f"\nTotal image bytes saved: {total_saved / 1024 / 1024:.2f} MB")

def update_html_performance():
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
            
        # 1. Update <video> tags to preload="none"
        content = re.sub(r'preload=["\'](?:metadata|auto)["\']', 'preload="none"', content)
        
        # 2. Add loading="lazy" decoding="async" to article content images if missing
        # Avoid top banner top01.png
        def img_replacer(match):
            img_tag = match.group(0)
            if 'top01.png' in img_tag or 'top.png' in img_tag or 'kjicon.png' in img_tag:
                return img_tag
            if 'loading=' not in img_tag:
                img_tag = img_tag.replace('<img ', '<img loading="lazy" decoding="async" ')
            return img_tag

        content = re.sub(r'<img [^>]+>', img_replacer, content)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML performance attributes in {fpath}")

if __name__ == '__main__':
    print("=== Step 1: Optimizing Image File Sizes ===")
    optimize_images()
    print("\n=== Step 2: Updating HTML Preload & Lazy Loading Attributes ===")
    update_html_performance()
