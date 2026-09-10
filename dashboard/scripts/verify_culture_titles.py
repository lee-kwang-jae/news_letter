# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html', 'r', encoding='utf-8') as f:
    html = f.read()

culture_idx = html.find('<div id="culture">')
pub_idx = html.find('<div id="public-news">')
culture_html = html[culture_idx:pub_idx]

h3s = re.findall(r'<h3>(.*?)</h3>', culture_html, re.DOTALL)
print(f"Total culture h3 titles: {len(h3s)}")
for i, h in enumerate(h3s):
    clean_h = re.sub(r'<[^>]+>', '', h).strip()
    print(f"{i+1}: {clean_h}")
