# -*- coding: utf-8 -*-
import os

old_title = '국민 삶에 직결된 800조 예산! 잠시 내려놓고 한가위 나눔 현장으로!'
new_title = '국민 삶에 직결된 800조 예산 꼼꼼히 챙기며 우리동네 현장도 달려갑니다'

target_files = [
    'index.html',
    'dashboard/news/index.html',
    'dashboard/news/kj_hanam_inside_20260918.html',
    'dashboard/scripts/create_0918.py'
]

for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if old_title in content:
            content = content.replace(old_title, new_title)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated title in {file_path}")
        else:
            print(f"old_title not found in {file_path}")
    else:
        print(f"File not found: {file_path}")
