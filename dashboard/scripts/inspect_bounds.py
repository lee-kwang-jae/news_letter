# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard/news/kj_hanam_inside_20260911.html', 'r', encoding='utf-8') as f:
    html = f.read()

tag_mom = '<div id="mom-cafe">'
tag_culture = '<div id="culture">'

idx_mom = html.find(tag_mom)
idx_culture = html.find(tag_culture)

print(f"mom-cafe index: {idx_mom}")
print(f"culture index: {idx_culture}")

sub_text = html[idx_mom:idx_culture]
print("--- Between mom-cafe and culture ---")
print(sub_text[:300])
print("...")
print(sub_text[-300:])
