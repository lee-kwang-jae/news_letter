"""행사일정 달력 데이터 반영 스크립트 (우리동네 하남소식)

events.json 을 검사하고, index.html 의 <!-- EVENTS-DATA:START --> ~ <!-- EVENTS-DATA:END -->
사이에 달력 데이터(JSON)를 넣는다. 또 <!-- TODAY-SCHEDULE:START --> ~ END 사이에
기준일(발행일)의 '오늘의 하남일정' 카드를 만들어 넣는다.

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

    today_events, today_html = build_today(keep, data["categories"], base)
    i, j = html.find(T_START), html.find(T_END)
    if i < 0 or j < 0:
        sys.exit("index.html 에 TODAY-SCHEDULE 표시가 없습니다 (오늘의 하남일정 섹션이 빠졌는지 확인).")
    html = html[:i] + T_START + "\n" + today_html + T_END + html[j + len(T_END):]
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
    print("  오늘의 하남일정:", ", ".join(e["title"] for e in today_events) if today_events else "없음 (다가오는 일정 표시)")


DOW = "월화수목금토일"
ICON = {"행사": "🎉", "공연.전시": "🎵", "강의": "🎤", "교육": "📚", "접수일정": "✍️", "기타": "📌"}
T_START, T_END = "<!-- TODAY-SCHEDULE:START -->", "<!-- TODAY-SCHEDULE:END -->"


def on(e, day):
    """그 날 실제로 열리는지 (weekdays·dates 지정 반영)"""
    if not e["start"] <= day.isoformat() <= e["end"]:
        return False
    if e.get("dates"):
        return day.isoformat() in e["dates"]
    if e.get("weekdays"):
        return DOW[day.weekday()] in e["weekdays"]
    return True


def md(d):
    return f"{d.month}.{d.day}({DOW[d.weekday()]})"


def card(e, colors, note=""):
    esc = html_mod.escape
    color = colors.get(e["category"], "#cbd5e0")
    s, t = datetime.date.fromisoformat(e["start"]), datetime.date.fromisoformat(e["end"])
    period = md(s) if s == t else f"{md(s)} ~ {md(t)}"
    title = esc(e["title"])
    if e.get("link"):
        title = f'<a href="{esc(e["link"])}" target="_blank" rel="noopener noreferrer">{title}</a>'
    meta = [f"🗓 {esc(note + period)}"]
    if e.get("time"):
        meta.append(f"⏰ {esc(e['time'])}")
    lines = " · ".join(meta)
    if e.get("place"):
        lines += f"<br/>📍 {esc(e['place'])}"
    if e.get("signup"):
        lines += f"<br/>✍️ 신청: {esc(e['signup'])}"
    link = ""
    if e.get("link"):
        label = "공고원문클릭 →"
        link = f'\n<div class="today-link"><a href="{esc(e["link"])}" target="_blank" rel="noopener noreferrer">{label}</a></div>'
    return (f'<div class="today-card" style="border-left-color: {color};">\n'
            f'<span class="today-tag" style="background: {color};">{ICON.get(e["category"], "")} {esc(e["category"])}</span>\n'
            f'<h3>{title}</h3>\n<div class="today-meta">{lines}</div>{link}\n</div>\n')


def build_today(events, colors, base):
    """오늘의 하남일정: 달력에서 기준일에 열리는 일정을 카드로 만든다"""
    # 접수 일정은 접수 기간 내내 넣지 않고, 접수가 시작하는 날과 마감하는 날에만 보여 준다
    signups = [e for e in events if e["category"] == "접수일정"]
    events = [e for e in events if e["category"] != "접수일정"]
    day = base.isoformat()
    sign_today = sorted([e for e in signups if day in (e["start"], e["end"])], key=lambda e: (e["end"] != day, e["title"]))
    todays = [e for e in events if on(e, base)]
    # 오늘 하루 열리는 일정(단일일·요일·회차 지정·오늘 시작)을 먼저, 며칠째 이어지는 기간 행사는 '진행 중'으로
    def is_ongoing(e):
        return e["start"] != e["end"] and not e.get("weekdays") and not e.get("dates") and e["start"] != day
    main = sorted([e for e in todays if not is_ongoing(e)], key=lambda e: (e.get("time") or "99", e["title"]))
    ongoing = sorted([e for e in todays if is_ongoing(e)], key=lambda e: e["end"])
    out = [f'<p class="today-intro">{base.month}월 {base.day}일({DOW[base.weekday()]}) 하남 일정입니다. <span style="color:#a0aec0;">(하남 행사일정 달력 기준)</span></p>\n']
    if main:
        out += [card(e, colors) for e in main]
    if ongoing:
        out += [card(e, colors, "진행 중 · ") for e in ongoing]
    if sign_today:
        out += [card(e, colors, "오늘 마감 · " if e["end"] == day else "오늘부터 접수 · ") for e in sign_today]
    todays = todays + sign_today
    if not todays:
        upcoming = []
        for e in events:
            d = max(base + datetime.timedelta(1), datetime.date.fromisoformat(e["start"]))
            end = datetime.date.fromisoformat(e["end"])
            while d <= end and not on(e, d):
                d += datetime.timedelta(1)
            if d <= end:
                upcoming.append((d, e))
        upcoming.sort(key=lambda x: (x[0], x[1]["title"]))
        if upcoming:
            out.append('<div class="today-sub">🔜 다가오는 일정</div>\n')
            out += [card(e, colors, f"{md(d)} 예정 · ") for d, e in upcoming[:3]]
    return todays, "".join(out)


if __name__ == "__main__":
    main()
