# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for date in ['20260901', '20260902', '20260903', '20260904', '20260907', '20260908', '20260909']:
    fn = f'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_{date}.html'
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            html = f.read()
        m_idx = html.find('<div id="mom-cafe">')
        c_idx = html.find('<div id="culture">')
        if c_idx == -1:
            c_idx = html.find('<div id="public-news">')
        print(f"=== {date} ===")
        h4s = re.findall(r'<h4>(.*?)</h4>', html[m_idx:c_idx])
        for h in h4s:
            print('  -', re.sub(r'<[^>]+>', '', h).strip())
    except Exception as e:
        print(date, e)
