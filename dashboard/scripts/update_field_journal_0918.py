# -*- coding: utf-8 -*-
import os
import urllib.request

# 1. Download image
img_url = "https://blogthumb.pstatic.net/MjAyNjA5MTdfNCAg/MDAxNzg9NjI1NDYyOTAz.Fpx6E_YjMsW20FxgJ_ZkLO6BIYBmFGMObS0JZiWA9Gsg.cdhWoJbBPUXyicAqlDaf7KMYWIoO97djZ3jwLE_BzbIg.JPEG/1.jpeg?type=w2"
img_dest = "images/091808.jpg"

try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(img_url, headers=headers)
    with urllib.request.urlopen(req) as response, open(img_dest, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Downloaded {img_dest}")
except Exception as e:
    print(f"Image download error: {e}")

old_card = '''<!-- 기사 2 (현장일지 - 네이버 블로그: 이광재, "적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사") -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224409939684" target="_blank" style="color: inherit; text-decoration: none;">[의정활동] 이광재, "적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사"… 이웃을 향한 따뜻한 손길</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
대한적십자사 봉사회 하남지구협의회가 주관한 \'추석맞이 사랑의 한가위 나눔행사\' 현장을 찾았습니다. 명절을 앞두고 정성스레 송편과 나눔 물품을 준비하시는 적십자 봉사원분들께 깊은 감사를 전하며, 헌신하는 봉사자들의 수고가 빛나고 하남의 소외된 이웃들이 온정을 느낄 수 있도록 민생 지원과 의정활동에 더욱 최선을 다하겠다고 약속했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/091801.jpeg" alt="적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224409939684" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>'''

new_card = '''<!-- 기사 2 (현장일지 - 네이버 블로그: 이광재, [800조 예산안 옆에 놓인 상자 하나]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224414956518" target="_blank" style="color: inherit; text-decoration: none;">[800조 예산안 옆에 놓인 상자 하나] 예결위 위원장 이광재, 내년도 820조 국가 예산안 세밀한 검토 착수</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
예산결산특별위원회 위원장으로서 내년도 820조 원 규모의 국가 예산안 심의에 임하는 이광재 의원의 현장일지입니다. 국민 삶에 직결된 예산 항목 하나하나를 꼼꼼히 살피고, 국가 발전과 하남시민을 위한 세밀한 예산 검토를 이어가겠습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/091808.jpg" alt="800조 예산안 옆에 놓인 상자 하나" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224414956518" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>'''

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
        if old_card in content:
            content = content.replace(old_card, new_card)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_path}")
        else:
            print(f"old_card not found exact match in {file_path}, trying partial replacement...")
            # Fallback replacement logic if formatting differs
            blog_url_pattern = "https://blog.naver.com/lee_kwang_jae/224409939684"
            if blog_url_pattern in content:
                # Replace url and title
                content = content.replace("https://blog.naver.com/lee_kwang_jae/224409939684", "https://blog.naver.com/lee_kwang_jae/224414956518")
                content = content.replace('[의정활동] 이광재, "적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사"… 이웃을 향한 따뜻한 손길', '[800조 예산안 옆에 놓인 상자 하나] 예결위 위원장 이광재, 내년도 820조 국가 예산안 세밀한 검토 착수')
                content = content.replace("대한적십자사 봉사회 하남지구협의회가 주관한 '추석맞이 사랑의 한가위 나눔행사' 현장을 찾았습니다. 명절을 앞두고 정성스레 송편과 나눔 물품을 준비하시는 적십자 봉사원분들께 깊은 감사를 전하며, 헌신하는 봉사자들의 수고가 빛나고 하남의 소외된 이웃들이 온정을 느낄 수 있도록 민생 지원과 의정활동에 더욱 최선을 다하겠다고 약속했습니다.", "예산결산특별위원회 위원장으로서 내년도 820조 원 규모의 국가 예산안 심의에 임하는 이광재 의원의 현장일지입니다. 국민 삶에 직결된 예산 항목 하나하나를 꼼꼼히 살피고, 국가 발전과 하남시민을 위한 세밀한 예산 검토를 이어가겠습니다.")
                content = content.replace("./images/091801.jpeg", "./images/091808.jpg")
                content = content.replace('alt="적십자와 함께하는 추석맞이 사랑의 한가위 나눔행사"', 'alt="800조 예산안 옆에 놓인 상자 하나"')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Partially updated {file_path}")
    else:
        print(f"File not found: {file_path}")
