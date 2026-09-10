# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate public-news section
pub_idx = content.find('<div id="public-news">')
culture_idx = content.find('<div id="culture">')

print(f"pub_idx: {pub_idx}, culture_idx: {culture_idx}")

pub_html = content[pub_idx:culture_idx]

# Keywords to remove
keywords_to_remove = [
    "K-컬처 복합 콤플렉스",
    "인플루엔자",
    "연체지우개",
    "생활폐기물"
]

# Let's inspect the cards in pub_html by splitting by <div class="article-card"
parts = pub_html.split('<div class="article-card"')

header = parts[0] # contains <div id="public-news"> and section title
new_parts = [header]

removed_count = 0
for part in parts[1:]:
    card_html = '<div class="article-card"' + part
    should_remove = False
    for kw in keywords_to_remove:
        if kw in card_html:
            should_remove = True
            print(f"Removing card containing: {kw}")
            removed_count += 1
            break
    if not should_remove:
        new_parts.append(card_html)

new_pub_html = "".join(new_parts)
print(f"Total cards removed: {removed_count}")

# Replace pub section in content
content = content[:pub_idx] + new_pub_html + content[culture_idx:]

# Save
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved cleaned files successfully!")
