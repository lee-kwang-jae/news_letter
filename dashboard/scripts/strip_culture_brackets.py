# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

def remove_brackets_from_culture(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    culture_idx = content.find('<div id="culture">')
    if culture_idx == -1:
        print(f"No culture section found in {file_path}")
        return

    hr_idx = content.find('<hr', culture_idx)
    if hr_idx == -1:
        hr_idx = content.find('<div id="public-news">', culture_idx)

    culture_block = content[culture_idx:hr_idx]

    # Regex to remove [...] and any following space from <h3><a ...>[...] Title</a></h3>
    # e.g., >[축제/관광] 축제와 -> >축제와
    new_culture_block = re.sub(r'(<h3><a [^>]+>)\s*\[[^\]]+\]\s*', r'\1', culture_block)

    content = content[:culture_idx] + new_culture_block + content[hr_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} successfully!")

remove_brackets_from_culture('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html')
remove_brackets_from_culture('d:/github/newsletter/newsletter/dashboard/news/index.html')
remove_brackets_from_culture('d:/github/newsletter/newsletter/dashboard/scripts/build_0910_clean.py')
