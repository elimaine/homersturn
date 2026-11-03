#!/usr/bin/env python3
"""Arithmetic over a draft's own ledger marks (references/manifold-and-ledger.md).

Reads a draft on stdin. Marks: [raise: name] opens a promise, [pay: name]
pays it, [plant: "line"] plants a refrain, [join: therefore|but|and then] names
how the paragraph follows the last. Reports per paragraph the debt
(words since the last payment), what is owed, and the failures the marks
make visible. Strips nothing; use --strip to print the draft without marks.

--shape needs no marks: it prints what a page says before a word is read
(the glance): each paragraph's words and sentences, the first paragraph's
share, the spread of lengths, the longest block, one-line paragraphs, lists,
bold, subheads, dashes, and neighbouring paragraphs that open on the same
words.
"""
from __future__ import annotations

import re
import sys

MARK = re.compile(r"\[(raise|pay|plant|join):\s*(.+?)\]")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
STOP = set("a an and are as at be but by for from had has have he her his i if in is it its of on or she so that the their them they this to was we were with you your".split())


def opening(para: str) -> tuple[str, ...]:
    words = [w.strip(".,;:!?\"'()").lower() for w in para.split()]
    return tuple(w for w in words if w and w not in STOP)[:6]


def shape(text: str) -> int:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", MARK.sub("", text).strip()) if p.strip()]
    if not paragraphs:
        print("no paragraphs")
        return 1
    rows = []
    for i, para in enumerate(paragraphs, 1):
        kind = "sub" if para.startswith("#") else "list" if re.match(r"^\s*([-*+]|\d+[.)])\s", para) else "code" if para.startswith("```") else "prose"
        words = len(para.split())
        sentences = len([s for s in SENTENCE_END.split(para) if s.strip()]) if kind == "prose" else 0
        rows.append((i, kind, words, sentences, para))
    prose = [r for r in rows if r[1] == "prose"]
    total = sum(r[2] for r in prose) or 1
    print(f"{'¶':>3}  {'kind':5} {'words':>5} {'sent':>4}  opens on")
    for i, kind, words, sentences, para in rows:
        flag = ""
        if kind == "prose":
            if i == rows[0][0] and words / total >= 0.35:
                flag = "  <- a wall at the top"
            if words >= 180:
                flag += "  <- long block"
            if para.count("—") + para.count(" - ") > 1:
                flag += "  <- more than one dash"
        print(f"{i:>3}  {kind:5} {words:>5} {sentences:>4}  {' '.join(para.split()[:7])}{flag}")
    if prose:
        lens = [r[2] for r in prose]
        mean = sum(lens) / len(lens)
        sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5
        first = prose[0][2] / total
        ones = sum(1 for r in prose if r[3] == 1)
        print(f"\nprose paragraphs {len(prose)}, words {total}, first paragraph {first:.0%} of the words, "
              f"longest {max(lens)}, spread (sd/mean) {sd / mean:.2f}, one-sentence paragraphs {ones}")
        if first >= 0.35:
            print("the opening is a wall: the eye cannot take the first paragraph whole")
        if len(prose) >= 4 and sd / mean < 0.25:
            print("the paragraphs are the same size: the page hums before it is read")
        if ones >= 3:
            print("three or more one-line paragraphs: emphasis spent until it is none")
        for a, b in zip(prose, prose[1:]):
            oa, ob = opening(a[4]), opening(b[4])
            if oa and ob and oa[:3] == ob[:3]:
                print(f"¶{a[0]} and ¶{b[0]} open on the same words: a repeated beat, or a refrain told once too often")
    bold = len(re.findall(r"\*\*[^*]+\*\*", text))
    subs = sum(1 for r in rows if r[1] == "sub")
    lists = sum(1 for r in rows if r[1] == "list")
    if bold or subs or lists:
        print(f"bold runs {bold}, subheads {subs}, list blocks {lists}")
    return 0


def main() -> int:
    strip = "--strip" in sys.argv
    text = sys.stdin.read()
    if "--shape" in sys.argv:
        return shape(text)
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
