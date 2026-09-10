# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = [(m.start(), m.group(0)) for m in re.finditer(r'(bottom-nav|맨위로|TOP|top|footer)', html, re.IGNORECASE)]
for pos, txt in matches[10:30]:
    print(f"Pos {pos}: {txt}")
    print(html[pos-30:pos+120])
    print("-" * 40)
