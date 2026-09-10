import os
import re

news_dir = "d:/github/newsletter/newsletter/dashboard/news"
html_files = [f for f in os.listdir(news_dir) if f.endswith(".html")]

toc_pattern = re.compile(r'(<li><a href="#legislative">)우리동네 국회의원 이광재 언론보도(</a></li>)')
title_pattern = re.compile(r'(<div class="section-title blue">🗣️ )우리동네 국회의원<br/>이광재 언론보도(</div>)')
title_pattern_2 = re.compile(r'(<div class="section-title blue">🗣️ )우리동네 국회의원 이광재 언론보도(</div>)')

new_block = """[우리동네 국회의원 이광재]</div>
        <div style="background-color: #f8fafc; padding: 20px; border-radius: 8px; margin-top: 15px; margin-bottom: 25px; border: 1px solid #e2e8f0; color: #334155; line-height: 1.6; font-size: 0.95rem;">
            <div style="font-weight: bold; color: #1e293b; margin-bottom: 8px; font-size: 1.05rem;">SECTION 1 : 현장미팅</div>
            <div style="padding-left: 10px; margin-bottom: 15px;">
                ㆍ국정 및 예산 관련 주요 인사 만남<br>
                ㆍ하남 현안 해결을 위한 지역 현장 소통 행보
            </div>
            <div style="font-weight: bold; color: #1e293b; margin-bottom: 8px; font-size: 1.05rem;">SECTION 2 : 언론보도</div>
            <div style="padding-left: 10px;">
                ㆍ주요 언론이 주목한 이광재 의원의 국정 활동<br>
                ㆍ국비 확보 및 하남 주요 현안 보도 모음
            </div>"""

for filename in html_files:
    filepath = os.path.join(news_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False
    
    # Update TOC
    if "우리동네 국회의원 이광재 언론보도" in content:
        content = toc_pattern.sub(r'\1[우리동네 국회의원 이광재]\2', content)
        content = title_pattern.sub(r'\1' + new_block, content)
        content = title_pattern_2.sub(r'\1' + new_block, content)
        changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
