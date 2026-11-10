"""행사일정 달력 데이터 반영 스크립트 (우리동네 하남소식)

events.json 을 검사하고, index.html 의 <!-- EVENTS-DATA:START --> ~ <!-- EVENTS-DATA:END -->
사이에 달력 데이터(JSON)를 넣는다.
('오늘의 하남일정' 섹션은 2026-11-11 사용자 요청으로 없앴다. 오늘 일정은 달력에서 날짜를 눌러 본다.)

  python -I .agents/tools/build_calendar.py            # 오늘 날짜 기준
  python -I .agents/tools/build_calendar.py 2026-12-01 # 날짜 지정 (발행일)
  python -I .agents/tools/build_calendar.py 2026-11-20 --check  # 미리 보기만: 아무 파일도 고치지 않음

※ 발행일이 아닌 미래 날짜로 시험할 때는 반드시 --check 를 붙인다.
  (교육의 신청 마감·지난달 정리가 실제로 events.json 에서 지워지기 때문)

한 달치 누적 규칙: 기준일이 속한 달의 1일보다 먼저 끝난 행사는 events.json 에서 지운다.
분류는 행사·공연.전시·강의·교육·접수일정·기타 6가지(이 순서)만 허용하고, 색은 events.json 의 categories 로 고정한다.
"""
import datetime
import html as html_mod
import json
import os
import sys
from urllib.parse import urlsplit

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EVENTS = os.path.join(ROOT, "events.json")
INDEX = os.path.join(ROOT, "index.html")
CATS = ["행사", "공연.전시", "강의", "교육", "접수일정", "기타"]
START, END = "<!-- EVENTS-DATA:START -->", "<!-- EVENTS-DATA:END -->"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_only = "--check" in sys.argv
    base = datetime.date.fromisoformat(args[0]) if args else datetime.date.today()
    month_start = base.replace(day=1)
    with open(EVENTS, encoding="utf-8") as f:
        data = json.load(f)

    if list(data.get("categories", {})) != CATS:
        sys.exit(f"categories 는 {CATS} 순서 그대로여야 합니다.")
    seen, keep, dropped, closed = set(), [], [], []
    for e in data["events"]:
        for k in ("id", "category", "title", "start", "end"):
            if not e.get(k):
                sys.exit(f"'{k}' 가 비어 있습니다: {e}")
        if e["id"] in seen:
            sys.exit(f"id 중복: {e['id']}")
        seen.add(e["id"])
        # 링크는 http/https 주소만 허용 (javascript: 같은 주소가 섞여 들어오는 것을 막음)
        if e.get("link") and urlsplit(e["link"]).scheme.lower() not in ("http", "https"):
            sys.exit(f"link 는 http:// 또는 https:// 주소만 쓸 수 있습니다: {e['id']} → {e['link']}")
        if e["category"] not in CATS:
            sys.exit(f"분류는 {CATS} 중 하나여야 합니다: {e['id']} → {e['category']}")
        s, t = datetime.date.fromisoformat(e["start"]), datetime.date.fromisoformat(e["end"])
        if t < s:
            sys.exit(f"종료일이 시작일보다 빠릅니다: {e['id']}")
        # 요일 지정(weekdays) 또는 날짜 지정(dates)이 있으면 달력에 그 날만 색 표시
        bad = [w for w in e.get("weekdays", []) if w not in "일월화수목금토" or len(w) != 1]
        if bad:
            sys.exit(f"weekdays 는 일·월·화·수·목·금·토 한 글자씩: {e['id']} → {bad}")
        for ds in e.get("dates", []):
            if not s <= datetime.date.fromisoformat(ds) <= t:
                sys.exit(f"dates 의 날짜가 start~end 밖에 있습니다: {e['id']} → {ds}")
        if e.get("weekdays"):
            days = [s + datetime.timedelta(n) for n in range((t - s).days + 1)]
            if not any("월화수목금토일"[x.weekday()] in e["weekdays"] for x in days):
                sys.exit(f"start~end 안에 지정한 요일이 하루도 없습니다: {e['id']}")
        # 교육은 신청이 살아 있는 것만: 신청 방법(signup) 필수, 신청 마감일(signup_end)이 지나면 지운다
        if e["category"] == "교육":
            if not e.get("signup"):
                sys.exit(f"교육에는 signup(신청 방법)이 꼭 있어야 합니다: {e['id']}")
            if e.get("signup_end") and datetime.date.fromisoformat(e["signup_end"]) < base:
                closed.append(e)
                continue
        (keep if t >= month_start else dropped).append(e)

    keep.sort(key=lambda e: (e["start"], e["end"]))
    data["events"] = keep
    with open(EVENTS if not check_only else os.devnull, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    payload = json.dumps({"categories": data["categories"], "events": keep}, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("</", "<\\/")
    block = f'{START}\n<script type="application/json" id="hanam-events">{payload}</script>\n{END}'
    with open(INDEX, encoding="utf-8") as f:
        html = f.read()
    i, j = html.find(START), html.find(END)
    if i < 0 or j < 0:
        sys.exit("index.html 에 EVENTS-DATA 표시가 없습니다 (행사일정 달력 섹션이 빠졌는지 확인).")
    html = html[:i] + block + html[j + len(END):]

    if not check_only:
        with open(INDEX, "w", encoding="utf-8", newline="") as f:
            f.write(html)
    else:
        print("[--check] 미리 보기만 했습니다. events.json·index.html 은 바꾸지 않았습니다.")

    print(f"기준일 {base} · 남은 행사 {len(keep)}건 · 지난달 행사 정리 {len(dropped)}건 · 신청 마감된 교육 정리 {len(closed)}건")
    for e in closed:
        print("  - 신청 마감으로 제외:", e["title"])
    for c in CATS:
        print(f"  {c}: {sum(1 for e in keep if e['category'] == c)}건")


if __name__ == "__main__":
    main()
