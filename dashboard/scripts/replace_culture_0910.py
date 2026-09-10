# -*- coding: utf-8 -*-
import re

target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260910.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_culture = """<div id="culture">
<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">\U0001f3ad ALL IN \ud558\ub0a8\ub77c\uc774\ud504</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026\ub144 9\uc6d4 10\uc77c \uae30\uc900 \ud55c\ub208\uc5d0 \ubcf4\ub294 \ud558\ub0a8\uc2dc \ucd5c\uc2e0 \ubb38\ud654\u00b7\ud589\uc0ac\u00b7\ub3c4\uc11c\uad00 \ud504\ub85c\uadf8\ub7a8 \uac00\uc774\ub4dc</p>

<!-- \ubb38\ud654 \uae30\uc0ac 1 (2026 \ud558\ub0a8 \uc774\uc131\uc0b0\uc131 \ubb38\ud654\uc81c - \ud558\ub0a8\uc5ec\ud589\ubc84\uc2a4) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">\U0001f68c 2026.09.19 | \ucd95\uc81c/\uad00\uad11</div>
<h3><a href="https://onoffmix.com/event/348611" target="_blank" style="color: inherit; text-decoration: none;">[\ucd95\uc81c/\uad00\uad11] \ucd95\uc81c\uc640 \ud568\uaed8 \ub5a0\ub098\ub294 \ud558\ub0a8\uc5ec\ud589\ubc84\uc2a4 \ud504\ub85c\uadf8\ub7a8 \uc2e0\uccad \u300a2026 \ud558\ub0a8 \uc774\uc131\uc0b0\uc131 \ubb38\ud654\uc81c\u300b</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"\ud558\ub0a8\uc758 \uc5ed\uc0ac\uc640 \uc790\uc5f0\uc744 \ud568\uaed8 \uc990\uae30\ub294 \ud2b9\ubcc4\ud55c \ubc84\uc2a4 \uc5ec\ud589!"</b><br/>
2026 \ud558\ub0a8 \uc774\uc131\uc0b0\uc131 \ubb38\ud654\uc81c\uc640 \ud568\uaed8\ud558\ub294 \ud558\ub0a8\uc5ec\ud589\ubc84\uc2a4 \ud504\ub85c\uadf8\ub7a8\uc785\ub2c8\ub2e4. \ud558\ub0a8\uc758 \uc5ed\uc0ac \uc720\uc801\uc9c0\uc640 \uc790\uc5f0\uacbd\uad00\uc744 \ub458\ub7ec\ubcf4\ub294 \uccb4\ud5d8\ud615 \ubc84\uc2a4\ud22c\uc5b4\ub85c, \ucd95\uc81c \ud604\uc7a5\uc758 \ud48d\uc131\ud55c \ud504\ub85c\uadf8\ub7a8\uc744 \ud568\uaed8 \uc990\uae38 \uc218 \uc788\uc2b5\ub2c8\ub2e4.<br/><br/>
<b>\ud83d\udcc5 \uc77c\uc2dc:</b> 2026\ub144 9\uc6d4 19\uc77c(\ud1a0) 10:00 \ucd9c\ubc1c<br/>
<b>\ud83d\udccd \uc7a5\uc18c:</b> \ud558\ub0a8 \uc774\uc131\uc0b0\uc131 \uc77c\ub300<br/>
<b>\ud83d\udca1 \ucc38\uac00\uc2e0\uccad:</b> \uc628\uc624\ud504\ubbf9\uc2a4(onoffmix.com)\uc5d0\uc11c \uc120\ucc29\uc21c \uc2e0\uccad
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://onoffmix.com/event/348611" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">\ud504\ub85c\uadf8\ub7a8 \uc2e0\uccad\ud558\uae30 (\uc628\uc624\ud504\ubbf9\uc2a4) \u2192</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-05.jpg" alt="2026 \ud558\ub0a8 \uc774\uc131\uc0b0\uc131 \ubb38\ud654\uc81c \ud558\ub0a8\uc5ec\ud589\ubc84\uc2a4" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="\ud074\ub9ad\ud558\uc5ec \uc6d0\ubcf8 \ubcf4\uae30">
</div>
</div>
<div class="source">
\ud83d\udccc \ucd9c\uc798: \ud558\ub0a8\uc2dc / \uc628\uc624\ud504\ubbf9\uc2a4
</div>
</div>

<!-- \ubb38\ud654 \uae30\uc0ac 2 (\ubbf8\uc0ac\ub3c4\uc11c\uad00 \uac15\uc88c) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">\ud83d\udcda 2026.09 | \uad50\uc721/\ub3c4\uc11c\uad00</div>
<h3><a href="https://www.hanamlib.go.kr/mslib/index.do" target="_blank" style="color: inherit; text-decoration: none;">[\uad50\uc721/\ub3c4\uc11c\uad00] \ud558\ub0a8\uc2dc \ubbf8\uc0ac\ub3c4\uc11c\uad00 \ub3c5\uc11c\ubb38\ud654 \ud504\ub85c\uadf8\ub7a8 \uac15\uc88c \uc548\ub0b4</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"\ubbf8\uc0ac\ub3c4\uc11c\uad00\uc5d0\uc11c \ub9cc\ub098\ub294 \uc54c\ucc2c \ub3c5\uc11c\ubb38\ud654 \ud504\ub85c\uadf8\ub7a8!"</b><br/>
\ud558\ub0a8\uc2dc \ubbf8\uc0ac\ub3c4\uc11c\uad00\uc5d0\uc11c \uc6b4\uc601\ud558\ub294 \ub3c5\uc11c\ubb38\ud654 \ud504\ub85c\uadf8\ub7a8 \uac15\uc88c\uc785\ub2c8\ub2e4. \ub2e4\uc591\ud55c \ubd84\uc57c\uc758 \uac15\uc88c\ub97c \ud1b5\ud574 \uc9c0\uc5ed \uc8fc\ubbfc\uc758 \ubb38\ud654\u00b7\uad50\uc721 \uc5ed\ub7c9\uc744 \ub192\uc774\uace0 \ub3c5\uc11c\ub97c \uc0dd\ud65c\ud654\ud560 \uc218 \uc788\ub294 \uae30\ud68c\ub97c \uc81c\uacf5\ud569\ub2c8\ub2e4.<br/><br/>
<b>\ud83d\udccd \uc7a5\uc18c:</b> \ud558\ub0a8\uc2dc \ubbf8\uc0ac\ub3c4\uc11c\uad00<br/>
<b>\ud83d\udca1 \uc2e0\uccad:</b> \ud558\ub0a8\uc2dc\ub9bd\ub3c4\uc11c\uad00 \ud648\ud398\uc774\uc9c0\uc5d0\uc11c \uc2e0\uccad \uac00\ub2a5
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/mslib/index.do" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">\uac15\uc88c \uc0c1\uc138 \uc548\ub0b4 (\ubbf8\uc0ac\ub3c4\uc11c\uad00) \u2192</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-02.jpg" alt="\ubbf8\uc0ac\ub3c4\uc11c\uad00 \ub3c5\uc11c\ubb38\ud654 \ud504\ub85c\uadf8\ub7a8" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="\ud074\ub9ad\ud558\uc5ec \uc6d0\ubcf8 \ubcf4\uae30">
</div>
</div>
<div class="source">
\ud83d\udccc \ucd9c\uc798: \ud558\ub0a8\uc2dc \ubbf8\uc0ac\ub3c4\uc11c\uad00
</div>
</div>

<!-- \ubb38\ud654 \uae30\uc0ac 3 (\uac10\uc77c\ub3c4\uc11c\uad00 \uacf5\uc9c0) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">\ud83d\udcd6 2026.09 | \uad50\uc721/\ub3c4\uc11c\uad00</div>
<h3><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">[\uad50\uc721/\ub3c4\uc11c\uad00] \ud558\ub0a8\uc2dc \uac10\uc77c\ub3c4\uc11c\uad00 \uacf5\uc9c0\uc0ac\ud56d \uc548\ub0b4</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"\uac10\uc77c\ub3c4\uc11c\uad00\uc758 \uc0c8\ub85c\uc6b4 \uc18c\uc2dd\uc744 \ud655\uc778\ud558\uc138\uc694!"</b><br/>
\ud558\ub0a8\uc2dc \uac10\uc77c\ub3c4\uc11c\uad00\uc5d0\uc11c \uc548\ub0b4\ud558\ub294 \ucd5c\uc2e0 \uacf5\uc9c0\uc0ac\ud56d\uc785\ub2c8\ub2e4. \uac10\uc77c\u00b7\uc704\ub840 \uc9c0\uc5ed \uc8fc\ubbfc\ub4e4\uc774 \uc774\uc6a9 \uac00\ub2a5\ud55c \ub2e4\uc591\ud55c \ud504\ub85c\uadf8\ub7a8 \ubc0f \ub3c4\uc11c\uad00 \uad00\ub828 \uc18c\uc2dd\uc744 \ud655\uc778\ud558\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4.<br/><br/>
<b>\ud83d\udccd \uc7a5\uc18c:</b> \ud558\ub0a8\uc2dc \uac10\uc77c\ub3c4\uc11c\uad00<br/>
<b>\ud83d\udcde \ubb38\uc758:</b> 031-790-6368
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/gamlib/selectBbsNttView.do?key=1517&bbsNo=230&nttNo=89738&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">\uacf5\uc9c0\uc0ac\ud56d \ubcf4\uae30 (\uac10\uc77c\ub3c4\uc11c\uad00) \u2192</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-03.jpg" alt="\uac10\uc77c\ub3c4\uc11c\uad00 \uacf5\uc9c0\uc0ac\ud56d" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="\ud074\ub9ad\ud558\uc5ec \uc6d0\ubcf8 \ubcf4\uae30">
</div>
</div>
<div class="source">
\ud83d\udccc \ucd9c\uc798: \ud558\ub0a8\uc2dc \uac10\uc77c\ub3c4\uc11c\uad00
</div>
</div>

<!-- \ubb38\ud654 \uae30\uc0ac 4 (\uc704\ub840\ub3c4\uc11c\uad00 9\uc6d4 \ud504\ub85c\uadf8\ub7a8) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">\u2b50 2026.09 | \uad50\uc721/\ub3c4\uc11c\uad00</div>
<h3><a href="https://www.hanamlib.go.kr/wilib/selectBbsNttView.do?key=883&bbsNo=131&nttNo=89769&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: inherit; text-decoration: none;">[\uad50\uc721/\ub3c4\uc11c\uad00] \u2605\uc704\ub840\ub3c4\uc11c\uad00 9\uc6d4 \ud504\ub85c\uadf8\ub7a8 \uc548\ub0b4\u2605</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<b>"\uc704\ub840\ub3c4\uc11c\uad00\uc5d0\uc11c 9\uc6d4\uc744 \uc54c\ucc28\uac8c \ubcf4\ub0b4\uc138\uc694!"</b><br/>
\ud558\ub0a8\uc2dc \uc704\ub840\ub3c4\uc11c\uad00\uc758 2026\ub144 9\uc6d4 \ub3c5\uc11c\ubb38\ud654 \ud504\ub85c\uadf8\ub7a8 \uc548\ub0b4\uc785\ub2c8\ub2e4. \ub3c5\uc11c\uc758 \ub2ec\uc744 \ub9de\uc544 \ub2e4\uccb4\ub85c\uc6b4 \ud504\ub85c\uadf8\ub7a8\uc774 \uc900\ube44\ub418\uc5b4 \uc788\uc73c\uba70, \uc704\ub840\ub3d9 \uc8fc\ubbfc \ub204\uad6c\ub098 \ucc38\uc5ec \uac00\ub2a5\ud569\ub2c8\ub2e4.<br/><br/>
<b>\ud83d\udccd \uc7a5\uc18c:</b> \ud558\ub0a8\uc2dc \uc704\ub840\ub3c4\uc11c\uad00<br/>
<b>\ud83d\udca1 \uc2e0\uccad:</b> \ud558\ub0a8\uc2dc\ub9bd\ub3c4\uc11c\uad00 \ud648\ud398\uc774\uc9c0\uc5d0\uc11c \uc2e0\uccad \uac00\ub2a5
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanamlib.go.kr/wilib/selectBbsNttView.do?key=883&bbsNo=131&nttNo=89769&searchCtgry=&searchCnd=all&searchKrwd=&pageIndex=1&integrDeptCode=" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">9\uc6d4 \ud504\ub85c\uadf8\ub7a8 \uc548\ub0b4 \ubcf4\uae30 (\uc704\ub840\ub3c4\uc11c\uad00) \u2192</a></div>
</div>
<div class="source">
\ud83d\udccc \ucd9c\uc798: \ud558\ub0a8\uc2dc \uc704\ub840\ub3c4\uc11c\uad00
</div>
</div>

<!-- \ubb38\ud654 \uae30\uc0ac 5 (\ud558\ub0a8\uc2dc\uccad \uacf5\uc9c0\uc0ac\ud56d) -->
<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">
<div class="badge" style="background-color: #e6fffa; color: #2c7a7b; border: 1px solid #b2f5ea;">\ud83c\udfd9\ufe0f 2026.09 | \uc2dc\uc815/\uacf5\uc9c0</div>
<h3><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&bbsNo=30&nttNo=502113" target="_blank" style="color: inherit; text-decoration: none;">[\uc2dc\uc815/\uacf5\uc9c0] \ud558\ub0a8\uc2dc\uccad \uacf5\uc9c0\uc0ac\ud56d \uc548\ub0b4</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; background: rgba(255, 255, 255, 0.75); border: 1px solid rgba(178, 245, 234, 0.6); color: #22543d;">
<div style="flex: 1;">
<b>"\ud558\ub0a8\uc2dc\uccad\uc5d0\uc11c \uc804\ud558\ub294 \ucd5c\uc2e0 \uacf5\uc9c0\uc0ac\ud56d\uc785\ub2c8\ub2e4!"</b><br/>
\ud558\ub0a8\uc2dc\uccad \uacf5\uc2dd \ud648\ud398\uc774\uc9c0\uc5d0\uc11c \uacf5\uc9c0\ud558\ub294 \uc2dc\uc815 \uad00\ub828 \ucd5c\uc2e0 \uc18c\uc2dd\uc785\ub2c8\ub2e4. \ud558\ub0a8\uc2dc\ubbfc \uc0dd\ud65c\uacfc \ubc00\uc811\ud55c \ud589\uc815 \uc815\ubcf4\ub97c \ud655\uc778\ud558\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4.<br/><br/>
<b>\ud83d\udccd \ubb38\uc758:</b> \ud558\ub0a8\uc2dc\uccad \u260e 031-790-5114
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr/www/selectBbsNttView.do?key=170&bbsNo=30&nttNo=502113" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">\uacf5\uc9c0\uc0ac\ud56d \uc790\uc138\ud788 \ubcf4\uae30 (\ud558\ub0a8\uc2dc\uccad) \u2192</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0910-04.jpg" alt="\ud558\ub0a8\uc2dc\uccad \uacf5\uc9c0\uc0ac\ud56d" style="width: 100%; height: 210px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="\ud074\ub9ad\ud558\uc5ec \uc6d0\ubcf8 \ubcf4\uae30">
</div>
</div>
<div class="source">
\ud83d\udccc \ucd9c\uc798: \ud558\ub0a8\uc2dc\uccad
</div>
</div>
</div>"""

old_culture = re.search(r'(?s)<div id="culture">.*?</div>\s*\n\s*\n\s*<hr', content)
if old_culture:
    start = old_culture.start()
    end = content.index('<hr', old_culture.start() + 10)
    content = content[:start] + new_culture + '\n\n<hr' + content[end + 3:]
    print("Culture section replaced successfully!")
else:
    print("ERROR: Could not find culture section")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Files saved!")
