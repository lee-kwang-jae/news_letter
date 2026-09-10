# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def remove_hanam_city(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove [하남시청] and any following space if inside <h3><a ...>[하남시청] ...</a></h3>
    new_content = content.replace('[하남시청] ', '').replace('[하남시청]', '')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Removed [하남시청] from {file_path}")

remove_hanam_city('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
remove_hanam_city('d:/github/newsletter/newsletter/dashboard/news/index.html')
remove_hanam_city('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
