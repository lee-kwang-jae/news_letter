# -*- coding: utf-8 -*-
import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260909.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("2026\ub144 9\uc6d4 9\uc77c</title>", "2026\ub144 9\uc6d4 10\uc77c</title>")
content = content.replace("\uc778\uc0ac\uc774\ub4dc - 2026\ub144 9\uc6d4 9\uc77c", "\uc778\uc0ac\uc774\ub4dc - 2026\ub144 9\uc6d4 10\uc77c")
content = content.replace("36\ud638 | 2026\ub144 9\uc6d4 9\uc77c \ubc1c\ud589", "37\ud638 | 2026\ub144 9\uc6d4 10\uc77c \ubc1c\ud589")
content = content.replace("2026\ub144 9\uc6d4 9\uc77c \uae30\uc900 \ud558\ub0a8 \uc9c0\uc5ed \uc778\ud130\ub137", "2026\ub144 9\uc6d4 10\uc77c \uae30\uc900 \ud558\ub0a8 \uc9c0\uc5ed \uc778\ud130\ub137")
content = content.replace("2026\ub144 9\uc6d4 9\uc77c \uae30\uc900 \ud55c\ub208\uc5d0 \ubcf4\ub294 \ud558\ub0a8\uc2dc", "2026\ub144 9\uc6d4 10\uc77c \uae30\uc900 \ud55c\ub208\uc5d0 \ubcf4\ub294 \ud558\ub0a8\uc2dc")
content = content.replace("\ubc1c\ud589\uc77c: 2026\ub144 9\uc6d4 9\uc77c | Lee Kwang-jae Newsletter", "\ubc1c\ud589\uc77c: 2026\ub144 9\uc6d4 10\uc77c | Lee Kwang-jae Newsletter")

# New public news article for Gyeonggi Ansim Eum Care
new_article = """<!-- \uc2e0\uaddc: \uacbd\uae30\uc548\uc2ec\uc774\uc74c\ucf00\uc5b4 \ud1f4\uc6d0\ud658\uc790 \uc9c0\uc6d0\uc0ac\uc5c5 -->
<div class="article-card">
<div class="badge">\ud558\ub0a8\uc2dc\uccad | 2026.07~12</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">[\ud558\ub0a8\uc2dc\uccad] \ud1f4\uc6d0\ud658\uc790\uc758 \uc548\uc804\ud55c \uc77c\uc0c1\ubcf5\uadc0\uc9c0\uc6d0\uc0ac\uc5c5 &#34;\uacbd\uae30\uc548\uc2ec\uc774\uc74c\ucf00\uc5b4&#34;</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
\uacbd\uae30\ub3c4\uc0ac\ud68c\uc11c\ube44\uc2a4\uc6d0\uc5d0\uc11c\ub294 \ud1f4\uc6d0\ud658\uc790\uc758 \ub3cc\ubd04 \uacf5\ubc31\uc744 \ucd5c\uc18c\ud654\ud558\uace0 \uac00\uc815 \ub0b4 \uc548\uc815\uc801\uc778 \ubcf5\uadc0\ub97c \uc9c0\uc6d0\ud558\uae30 \uc704\ud574 <b>&#12300;\uacbd\uae30\uc548\uc2ec\uc774\uc74c\ucf00\uc5b4&#12301;</b> \uc0ac\uc5c5\uc744 \uc6b4\uc601\ud558\uace0 \uc788\uc2b5\ub2c8\ub2e4.<br/><br/>
<b>\uc2e0\uccad\uae30\uac04:</b> 2026\ub144 7\uc6d4 ~ 12\uc6d4 (\uc608\uc0b0 \uc18c\uc9c4 \uc2dc \uc0ac\uc5c5 \uc885\ub8cc)<br/>
<b>\uc11c\ube44\uc2a4 \ub300\uc0c1:</b> \uc9c8\ubcd1\u00b7\ubd80\uc0c1\u00b7\uc218\uc220 \ub4f1\uc73c\ub85c \uc785\uc6d0 \uce58\ub8cc \ud6c4 \ud1f4\uc6d0\ud558\ub294(\ud1f4\uc6d0 7\uc77c \uc774\ub0b4) \uacbd\uae30\ub3c4\ubbfc \uc911 \ub3cc\ubd04 \uacf5\ubc31\uc774 \uc6b0\ub824\ub418\ub294 \ubd84<br/>
<b>\uc81c\uacf5 \uc11c\ube44\uc2a4:</b> AI \uc758\ub8cc \ubaa8\ub2c8\ud130\ub9c1, \uc0dd\ud65c(\uac00\uc0ac)\ub3cc\ubd04, \ubcd1\uc6d0 \ub3d9\ud589 \ub3cc\ubd04, \ub9de\ucda4\ud615 \uc2dd\uc0ac \uc9c0\uc6d0, \uc2ec\ub9ac\uc7ac\ud65c \uc11c\ube44\uc2a4 \ub4f1<br/>
<b>\uc81c\uacf5 \uae30\uac04:</b> \ud1f4\uc6d0 \ud6c4 30\uc77c \uc774\ub0b4<br/>
<b>\uc9c0\uc6d0 \ud55c\ub3c4:</b> 1\uc778 100\ub9cc \uc6d0 \uc774\ub0b4 (\uc18c\ub4dd \uae30\uc900\uc5d0 \ub530\ub77c \ubcf8\uc778\ubd80\ub2f4\uae08 \ubc1c\uc0dd \uac00\ub2a5)<br/>
<b>\ubb38\uc758:</b><br/>
&nbsp;&nbsp;\u2014 \uacbd\uae30\ub3c4\uc0ac\ud68c\ubcf5\uc9c0\uad00\ud611\ud68c: <a href="tel:031-928-6935" style="color:#3182ce; font-weight:bold;">031-928-6935</a><br/>
&nbsp;&nbsp;\u2014 \uacbd\uae30\ub3c4\uc0ac\ud68c\uc11c\ube44\uc2a4\uc6d0: <a href="tel:031-884-8573" style="color:#3182ce; font-weight:bold;">031-884-8573</a>
<div style="margin-top: 14px; text-align: center;">
<img src="./images/0910-06.jpg" alt="\uacbd\uae30\uc548\uc2ec\uc774\uc74c\ucf00\uc5b4 \uc0ac\uc5c5 \uc548\ub0b4" style="max-width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="\ud074\ub9ad\ud558\uc5ec \uc6d0\ubcf8 \ubcf4\uae30">
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">\uacf5\uace0\ubb38 \uc790\uc138\ud788 \ubcf4\uae30 (\ud558\ub0a8\uc2dc\uccad) \u2192</a></div>
</div>
<div class="source">
\ucd9c\uc2a4: \ud558\ub0a8\uc2dc\uccad
</div>
</div>

"""

# Insert new article right after the public-news section title
old_section_header = '<div id="public-news">\n<div class="section-title purple">'
old_first_article_comment = '<!-- \uae30\uc0ac 1 (\ud558\ub0a8\uc2dc\uccad - \ucd94\uc11d \uc5f0\ud734 \uc0dd\ud65c\ud3d0\uae30\ubb3c \ubc30\ucd9c \uc548\ub0b4) -->'
# Fix the badge dates to 2026.09.10
content = content.replace('class="badge">\n\ud558\ub0a8\uc2dc\uccad | 2026.09.09', 'class="badge">\n\ud558\ub0a8\uc2dc\uccad | 2026.09.10')

# Find the public-news section and prepend the new article
pub_pattern = r'(<div id="public-news">[\s\S]*?<div class="section-title purple">.*?</div>\s*\n)'
pub_match = re.search(pub_pattern, content)
if pub_match:
    insert_pos = pub_match.end()
    content = content[:insert_pos] + '\n' + new_article + content[insert_pos:]
    print("Successfully inserted new article into public-news section.")
else:
    print("ERROR: Could not find public-news section!")

content = re.sub(r'\n{3,}', '\n\n', content)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! Generated: {target_path}")
print(f"Updated: {index_path}")
