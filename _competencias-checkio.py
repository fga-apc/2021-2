import re
from collections import deque

WS = re.compile(r"\s*")
TITLE = re.compile(r"### *\[(?P<title>[^\]]+)\] *\((?P<url>[^)]+)\) *")
LINE = re.compile(r" *\* *(?P<slug>[\w_-]+): *(?P<points>\d+) *(?P<mod>\([^)]+\))?")


def parse_checkio(src: str, only_grades=False, accept_mods=False):
    lines = deque(src.splitlines())
    data = {}
    skip(lines)

    while lines:
        question = parse_question(lines, accept_mods=accept_mods)
        data[question["id"]] = question
        skip(lines)

    if only_grades:
        data = {k: v["grades"] for k, v in data.items()}

    return data


def parse_question(lines: deque, accept_mods: bool = False) -> dict:
    if not (m := TITLE.fullmatch(line := lines.popleft())):
        raise ValueError(f"invalid title: {line}")

    title = m.group("title")
    url = m.group("url")
    slug = url.removesuffix("/").rpartition("/")[-1]
    grades = {}

    while lines:
        skip_ws(lines)
        if not lines:
            break
        if not (m := LINE.fullmatch(line := lines.popleft())):
            lines.appendleft(line)
            break
        else:
            if accept_mods or not m.group("mod"):
                grades[m.group("slug")] = int(m.group("points"))

    return {"id": slug, "title": title, "url": url, "grades": grades}


def skip(lines: deque):
    skip = []
    while lines and not lines[0].startswith("###"):
        skip.append(lines.popleft())


def skip_ws(lines: deque):
    while lines and WS.fullmatch(lines[0]):
        lines.popleft()


if __name__ == "__main__":
    from pprint import pprint
    import json

    with open("CHECKIO.md") as fd:
        data = parse_checkio(fd.read(), only_grades=True)

    with open("competencias.json", "w") as fd:
        json.dump(data, fd, indent=2)
