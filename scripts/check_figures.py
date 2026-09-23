#!/usr/bin/env python3
"""The cross-repository figures gate.

This site states role-call's test and decision counts. role-call
counts them with a test of its own (its D-031 and the figures rule),
but the copy here was typed by hand and went stale twice in a month.
This reads role-call's README on main and refuses a mismatch; with
--fix it rewrites the two figures here to match.
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = "https://raw.githubusercontent.com/tltaylor1/role-call/main/README.md"
STATED = re.compile(r"(\d+) tests, (\d+) recorded(\s+)decisions")
FILES = ["README.md", "index.html"]


def source_figures() -> tuple[int, int]:
    with urllib.request.urlopen(SOURCE, timeout=30) as response:  # noqa: S310  (https, fixed host)
        text = response.read().decode()
    tests = re.search(r"\*\*(\d+) tests in \d+ files\*\*", text)
    decisions = re.search(r"\*\*(\d+) recorded decisions\*\*", text)
    if not tests or not decisions:
        print("role-call's README no longer states its figures in the expected form")
        raise SystemExit(2)
    return int(tests.group(1)), int(decisions.group(1))


def main() -> int:
    fix = "--fix" in sys.argv
    tests, decisions = source_figures()
    failures = 0
    for name in FILES:
        path = ROOT / name
        text = path.read_text()
        found = STATED.search(text)
        if not found:
            print(f"{name}: states no figures in the expected form")
            failures += 1
            continue
        stated = (int(found.group(1)), int(found.group(2)))
        if stated == (tests, decisions):
            continue
        if fix:
            new = STATED.sub(lambda m: f"{tests} tests, {decisions} recorded{m.group(3)}decisions", text, count=1)
            path.write_text(new)
            print(f"{name}: {stated[0]} tests, {stated[1]} decisions -> {tests}, {decisions}")
        else:
            print(f"{name}: states {stated[0]} tests and {stated[1]} decisions; role-call reports {tests} and {decisions}")
            failures += 1
    if failures and not fix:
        return 1
    print(f"figures match role-call: {tests} tests, {decisions} decisions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
