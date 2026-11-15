"""우하소 달력 승계 (3주소 순환, 2026-11-15)

새 호를 만들 때 이 폴더의 events.json을 다음 두 곳을 합쳐서 만든다.
  1) 하루 전날 호를 올린 주소 폴더의 events.json  (우선)
  2) newsletter(news_letter) 폴더의 events.json      (자동 수집이 쌓이는 곳)
같은 id는 1)을 쓰고, 2)에만 있는 일정을 더한다. 그래서 자동 수집분도 빠지지 않고 누적된다.
그다음 build_calendar.py 발행일 을 돌린다.

사용법 (이 폴더에서):
  python -I .agents/tools/carry_calendar.py <전날 폴더> [--master <newsletter 폴더>]
  예) python -I .agents/tools/carry_calendar.py ../news_letter_02
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load(folder):
    path = os.path.join(folder, "events.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    prev = os.path.abspath(argv[0])
    master = os.path.abspath(os.path.join(HERE, "..", "newsletter"))
    if "--master" in argv:
        master = os.path.abspath(argv[argv.index("--master") + 1])

    base = load(prev)
    seen = {e["id"] for e in base["events"]}
    added = []
    if os.path.normcase(master) != os.path.normcase(prev) and os.path.exists(os.path.join(master, "events.json")):
        for e in load(master)["events"]:
            if e["id"] not in seen:
                base["events"].append(e)
                seen.add(e["id"])
                added.append(e["id"])

    out = os.path.join(HERE, "events.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(base, f, ensure_ascii=False, indent=2)
    print(f"전날 폴더 {os.path.basename(prev)} 에서 {len(base['events']) - len(added)}건, "
          f"newsletter 자동 수집분 {len(added)}건 추가 → {out}")
    for i in added:
        print("  +", i)
    print("다음: python -I .agents/tools/build_calendar.py 발행일(YYYY-MM-DD)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
