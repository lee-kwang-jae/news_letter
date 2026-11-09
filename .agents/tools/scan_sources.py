"""하남 행사일정 달력 자동 수집 스캐너 (우리동네 하남소식)

calendar_sources.json 의 사이트 목록을 읽어 각 목록 첫 페이지의 '아직 검토하지 않은 새 글'만 출력한다.
축제·교육·공연·강의·기타·접수 일정인지 판단해 events.json 에 넣는 일은 Claude(또는 사람)가 한다.

  python -I .agents/tools/scan_sources.py              # 모든 출처의 새 글
  python -I .agents/tools/scan_sources.py --all        # 새 글 여부와 관계없이 전부
  python -I .agents/tools/scan_sources.py --mark       # 지금 보이는 글을 '검토함'으로 기록
  python -I .agents/tools/scan_sources.py --source hnart-shows   # 한 출처만

검토 기록은 sources_seen.json 에 출처별 글 번호로 남기고, 목록에서 내려간 글은 기록에서도 지운다 (누적하지 않음).
한 출처가 열리지 않아도 나머지는 계속 읽고, 마지막에 실패한 출처를 알려 준다.
"""
import html
import json
import os
import re
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(HERE, "calendar_sources.json")
SEEN = os.path.join(HERE, "sources_seen.json")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    for enc in ("utf-8", "cp949"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
    return raw.decode("utf-8", "ignore")


def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return re.sub(r"\s*(새글|핫이슈|new|NEW)\s*$", "", s).strip()


def strip_scripts(doc):
    return re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", doc)


# ---- 출처별 목록 읽기: [{"id", "title", "link", "info"}] ----

def popupzone(src):
    items, page, pages = [], 1, 1
    while page <= pages:
        doc = fetch(src["url"].format(page=page))
        if page == 1:
            m = re.search(r'페이지 <em class="em_count">\d+ / (\d+)</em>', doc)
            pages = int(m.group(1)) if m else 1
        for li in re.findall(r'<li class="p-media">(.*?)</li>', doc, re.S):
            img = re.search(r'<img src="([^"]+)"[^>]*alt="([^"]*)"', li, re.S)
            if not img:
                continue
            title = re.search(r'p-media__heading-text">(.*?)</span>', li, re.S)
            link = re.search(r'<a href="([^"]+)"', li)
            detail = re.sub(r"[ \t]+", " ", html.unescape(img.group(2))).strip()
            items.append({"id": img.group(1).rsplit("/", 1)[-1],
                          "title": clean(title.group(1)) if title else "",
                          "link": html.unescape(link.group(1)) if link else "",
                          "info": "\n".join(l.strip() for l in detail.splitlines() if l.strip())})
        page += 1
    return items


def _anchors(doc, needle, idkey, base):
    out, seen = [], set()
    for href, text in re.findall(r'<a[^>]+href="([^"]*' + needle + r'[^"]*)"[^>]*>(.*?)</a>', strip_scripts(doc), re.S):
        href = html.unescape(href)
        m = re.search(idkey + r"=(\d+)", href)
        t = clean(text)
        if not m or len(t) < 4 or m.group(1) in seen:
            continue
        seen.add(m.group(1))
        link = href if href.startswith("http") else base + href.lstrip("./")
        out.append({"id": m.group(1), "title": t, "link": link, "info": ""})
    return out


def egov_bbs(src):
    return _anchors(fetch(src["url"]), "selectBbsNttView", "nttNo", src["base"])


def hanam_culture(src):
    items = _anchors(fetch(src["url"]), "selectClturEventWebView", "clturEventNo", "https://www.hanam.go.kr/www/")
    for i in items:  # '제목 기간 2026-11-15 ~ 2026-11-15 장소 ...' → 제목과 정보 분리
        m = re.search(r"\s기간\s", i["title"])
        if m:
            i["info"], i["title"] = i["title"][m.start():].strip(), i["title"][:m.start()].strip()
        i["title"] = re.sub(r"^-->\s*", "", i["title"])
    return items


def hnart_show(src):
    items = _anchors(fetch(src["url"]), "showView", "shNo", src["base"])
    for i in items:
        m = re.search(r"\s기간\s", i["title"])
        if m:
            i["info"], i["title"] = i["title"][m.start():].strip(), i["title"][:m.start()].strip()
    return items


def gseek(src):
    doc = strip_scripts(fetch(src["url"]))
    out, seen = [], set()
    for sid, text in re.findall(r"fnView\('(\d+)'\)[^>]*>(.*?)</a>", doc, re.S):
        t = clean(re.sub(r"<strong[^>]*>.*?</strong>", "", text, flags=re.S))
        if sid in seen or not t:
            continue
        seen.add(sid)
        out.append({"id": sid, "title": t, "link": f"https://hanam.gseek.kr/user/homepage/notice/view?seq={sid}", "info": ""})
    return out


def rss(src):
    doc = fetch(src["url"])
    out = []
    for item in re.findall(r"<item>(.*?)</item>", doc, re.S):
        g = lambda tag: re.sub(r"<!\[CDATA\[|\]\]>", "", (re.search(rf"<{tag}>(.*?)</{tag}>", item, re.S) or [None, ""])[1]).strip()
        link = g("link").split("?")[0]
        m = re.search(r"(\d{9,})", link)
        out.append({"id": m.group(1) if m else link, "title": clean(g("title")), "link": link,
                    "info": "작성 " + g("pubDate")[:16] + " · " + clean(g("description"))[:160]})
    return out


def culture_center(src):
    doc = strip_scripts(fetch(src["url"]))
    out, seen = [], set()
    for href, text in re.findall(r'<a[^>]+href="(/board/bbs\d+/\d+)"[^>]*>(.*?)</a>', doc, re.S):
        t = clean(text)
        if href in seen or len(t) < 4:
            continue
        seen.add(href)
        out.append({"id": href, "title": t, "link": src["base"] + href, "info": ""})
    return out


PARSERS = {f.__name__: f for f in (popupzone, egov_bbs, hanam_culture, hnart_show, gseek, rss, culture_center)}


def main():
    args = sys.argv[1:]
    only = args[args.index("--source") + 1] if "--source" in args else None
    with open(SOURCES, encoding="utf-8") as f:
        sources = json.load(f)["sources"]
    seen = {}
    if os.path.exists(SEEN):
        with open(SEEN, encoding="utf-8") as f:
            seen = json.load(f)

    failed, total_new = [], 0
    for src in sources:
        if only and src["id"] != only:
            continue
        try:
            items = PARSERS[src["parser"]](src)
        except Exception as e:  # 한 곳이 막혀도 나머지는 계속
            failed.append(f"{src['name']}: {type(e).__name__} {e}")
            continue
        old = set(seen.get(src["id"], []))
        new = [i for i in items if i["id"] not in old]
        total_new += len(new)
        show = items if "--all" in args else new
        print(f"\n=== {src['name']} — 목록 {len(items)}건 · 새 글 {len(new)}건 ({src['id']})")
        for n, i in enumerate(show, 1):
            print(f"[{n}] {i['title']}\n    링크: {i['link'] or '없음'}")
            for line in (i["info"] or "").splitlines():
                print("    | " + line)
        live = {i["id"] for i in items}
        kept = [x for x in seen.get(src["id"], []) if x in live]
        seen[src["id"]] = sorted(set(kept) | live) if "--mark" in args else kept

    with open(SEEN, "w", encoding="utf-8", newline="\n") as f:
        json.dump(seen, f, ensure_ascii=False, indent=0)
    print(f"\n합계 새 글 {total_new}건" + (" · 검토함으로 기록했습니다" if "--mark" in args else ""))
    if failed:
        print("열지 못한 출처:")
        for x in failed:
            print("  - " + x)


if __name__ == "__main__":
    main()
