# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

root_dir = 'd:/github/newsletter/newsletter/dashboard'
target_text = "© 2026 우리동네 진짜일꾼 이광재"
replacement = "© 2026 우리동네 진짜일꾼 이광재"

count = 0
for root, dirs, files in os.walk(root_dir):
    for fn in files:
        if fn.endswith('.html') or fn.endswith('.py') or fn.endswith('.js'):
            fp = os.path.join(root, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    content = f.read()
                if target_text in content:
                    content = content.replace(target_text, replacement)
                    with open(fp, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {fp}")
                    count += 1
            except Exception as e:
                print(f"Error processing {fp}: {e}")

print(f"Total updated files: {count}")
