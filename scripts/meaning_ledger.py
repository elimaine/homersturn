#!/usr/bin/env python3
"""Arithmetic over a draft's own ledger marks (references/meaning-as-music.md).

Reads a draft on stdin. Marks: [raise: name] opens a promise, [pay: name]
pays it, [plant: "line"] plants a refrain, [join: therefore|but|and then] names
how the paragraph follows the last. Reports per paragraph the debt
(words since the last payment), what is owed, and the failures the marks
make visible. Strips nothing; use --strip to print the draft without marks.
"""
from __future__ import annotations

import re
import sys

MARK = re.compile(r"\[(raise|pay|plant|join):\s*(.+?)\]")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")


def main() -> int:
    strip = "--strip" in sys.argv
    text = sys.stdin.read()
    if strip:
        sys.stdout.write(MARK.sub("", text))
        return 0
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    owed: dict[str, int] = {}
    planted: dict[str, int] = {}
    debt = 0
    problems: list[str] = []
    print(f"{'¶':>3}  {'words':>5}  {'debt':>5}  owed / events")
    for i, para in enumerate(paragraphs, 1):
        plain = MARK.sub("", para)
        words = len(plain.split())
        events: list[str] = []
        for kind, name in MARK.findall(para):
            if kind == "join":
                events.append(f"join {name}")
                if name.strip().lower().replace("-", " ") == "and then":
                    problems.append(f"¶{i}: joined to the last by \"and then\" (a list, not a story)")
                continue
            name = name.strip().strip('"')
            if kind == "raise":
                owed[name] = i
                events.append(f"raise {name}")
            elif kind == "pay":
                if name in owed:
                    del owed[name]
                    debt = 0
                    events.append(f"pay {name}")
                else:
                    events.append(f"pay {name} (never raised)")
                    problems.append(f"¶{i}: pays '{name}', which was never raised")
            else:
                n = planted.get(name, 0)
                if n >= 2:
                    events.append(f"refrain {name!r} (returns, planted {n}x)")
                else:
                    events.append(f"plant {name!r} ({n + 1}x)")
                planted[name] = n + 1
        if not any(e.startswith("pay") for e in events):
            debt += words
        last_raw = para.strip().rsplit(". ", 1)[-1]
        due_before = {k for k, v in owed.items() if v < i}
        if due_before and "[pay:" not in last_raw and "[plant:" not in last_raw:
            problems.append(f"¶{i}: something is due ({', '.join(sorted(due_before))}) and the last "
                            "sentence pays nothing: the stress position is spent on a quiet line")
        if debt > 450:
            problems.append(f"¶{i}: {debt} words since anything was paid: a release is due")
        print(f"{i:>3}  {words:>5}  {debt:>5}  {', '.join(events) or '-'}")
    if owed:
        print("\nstill owed:", ", ".join(f"{k} (¶{v})" for k, v in owed.items()))
    if problems:
        print("\nproblems:")
        for p in problems:
            print(" -", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
