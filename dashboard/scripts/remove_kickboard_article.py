# -*- coding: utf-8 -*-
import os
import re

target_files = [
    r'd:\github\newsletter\newsletter\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\index.html',
    r'd:\github\newsletter\newsletter\dashboard\news\kj_hanam_inside_20260911.html'
]

pattern = re.compile(r'\s*<!-- 지역 뉴스 기사 \d+ \(정병용 하남시의회 의장 공유킥보드 안전대책\) -->\s*<div class="article-card">\s*<div class="badge">📰 의정/안전</div>\s*<h3><a href="https://go\.seoul\.co\.kr/news/newsView\.php\?id=20260909500241&wlog_tag3=naver".*?</div>\s*</div>', re.DOTALL)

for filepath in target_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, count = pattern.subn('', content)
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Successfully removed article from {filepath} ({count} occurrence)")
        else:
            print(f"Failed to find target article in {filepath}")
    else:
        print(f"File not found: {filepath}")
