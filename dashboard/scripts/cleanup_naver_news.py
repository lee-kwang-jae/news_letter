import os
import re

news_dir = "d:/github/newsletter/newsletter/dashboard/news"
scripts_dir = "d:/github/newsletter/newsletter/dashboard/scripts"

print("--- Updating HTML files ---")
html_files = [f for f in os.listdir(news_dir) if f.endswith(".html")]

for filename in sorted(html_files):
    filepath = os.path.join(news_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Remove TOC entry
    content = re.sub(r'\s*<li>\s*<a href="#naver-news">.*?</a>\s*</li>', '', content)

    # 2. Remove naver-news section heading comments
    content = re.sub(r'\s*<!--\s*===== 섹션\s*\d*:\s*네이버.*?===== -->\s*', '\n', content)

    # 3. Remove <div id="naver-news">...</div> if any remaining
    content = re.sub(r'(?s)<div id="naver-news">.*?</div>', '', content)

    # 4. Remove leftover <ul class="news-list">...</ul> and its closing div/hr before next section or culture/public-news
    content = re.sub(r'(?s)\s*<ul class="news-list">.*?</ul>\s*(?:</div>)?\s*(?:<hr/?>)?', '', content)

    # Clean up double <hr/> or multiple newlines if created
    content = re.sub(r'(<hr/?>\s*)+<hr/?>', '<hr/>', content)
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated HTML: {filename}")

print("\nDone!")
