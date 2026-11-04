#!/usr/bin/env python3
"""Arithmetic over a draft's own ledger marks (references/manifold-and-ledger.md).

Reads a draft on stdin. Marks: [raise: name] opens a promise, [pay: name]
pays it, [plant: "line"] plants a refrain, [join: therefore|but|and then] names
how the paragraph follows the last, [state: name degree] marks the speaker's
state when it moves (the trajectory is listed beside the debt). --strength N
(1 to 5, default 3) sets the reader's pool, drawn as a wave at the end. Reports per paragraph the debt
(words since the last payment), what is owed, and the failures the marks
make visible. Strips nothing; use --strip to print the draft without marks.

--shape needs no marks: it prints what a page says before a word is read
(the glance): each paragraph's words and sentences, the first paragraph's
share, the spread of lengths, the longest block, one-line paragraphs, lists,
bold, subheads, dashes, and neighbouring paragraphs that open on the same
words.
"""
from __future__ import annotations

import pathlib
import re
import sys

MARK = re.compile(r"\[(raise|pay|plant|join|state):\s*(.+?)\]")

# The reader's pool (SKILL.md, the third dial). Untuned sketch: the shape is
# the claim, the numbers are placeholders until a bench sets them. Mana
# regenerates: a plain sentence puts some back, a long one spends.
POOL_CAPACITY = {1: 40, 2: 70, 3: 100, 4: 130, 5: 160}
PLAIN_WORDS = 18            # a sentence this long or shorter is taken without effort
REGEN_PER_PLAIN_WORD = 0.25 # and regenerates
COST_PER_LONG_WORD = 0.35   # a longer sentence spends per word
COST_PER_RAISE = 4          # a promise opened is carried
REFILL_PAY = 14             # a payment: the reader leans in again
REFILL_REFRAIN = 8          # a line already theirs
REGEN_SHORT = 6             # a paragraph of 40 words or fewer is a breath
SPARK = " ▁▂▃▄▅▆▇█"
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
    frames: dict[tuple[str, ...], set[int]] = {}
    for i, kind, words, sentences, para in rows:
        if kind != "prose":
            continue
        toks = [w.strip(".,;:!?\"'()").lower() for w in para.split()]
        for j in range(len(toks) - 2):
            gram = tuple(toks[j:j + 3])
            if all(w in STOP for w in gram) or not all(gram):
                continue
            frames.setdefault(gram, set()).add(i)
    repeated = sorted(((g, ps) for g, ps in frames.items() if len(ps) >= 2), key=lambda x: (-len(x[1]), x[0]))
    if repeated:
        shown = []
        for g, ps in repeated[:8]:
            shown.append(f"'{' '.join(g)}' (¶{', ¶'.join(str(p) for p in sorted(ps))})")
        print("frames repeated across paragraphs (a refrain, or the figure humming): " + "; ".join(shown))
    bold = len(re.findall(r"\*\*[^*]+\*\*", text))
    subs = sum(1 for r in rows if r[1] == "sub")
    lists = sum(1 for r in rows if r[1] == "list")
    if bold or subs or lists:
        print(f"bold runs {bold}, subheads {subs}, list blocks {lists}")
    return 0


BITS = ["The figures and the accents", "The three punches"]
MOVES = ["The join", "The two positions", "Forms", "The entrance"]


def _sections(skill: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    name = ""
    for line in skill.splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            out[name] = []
        elif name:
            out[name].append(line)
    return out


def _items(lines: list[str]) -> list[tuple[str, str]]:
    """(name, first sentence) per bullet, numbered item or table row; the
    section's first sentence when it has none."""
    items: list[tuple[str, str]] = []
    buf: list[str] = []
    rows: list[str] = []

    def flush() -> None:
        if not buf:
            return
        text = " ".join(x.strip() for x in buf)
        text = re.sub(r"^(?:- |\d+\. )", "", text)
        m = re.match(r"(.{3,60}?)(?::| is | are |\.) ?(.*)", text)
        if m:
            name, rest = m.group(1).strip(), m.group(2).strip()
        else:
            name, rest = text, ""
        if name.lower().startswith("the figure hums"):
            buf.clear()
            return
        first = re.split(r"(?<=[.!?])\s", rest, maxsplit=1)[0] if rest else ""
        items.append((name[0].upper() + name[1:], first))
        buf.clear()

    for line in lines:
        if line.startswith("|"):
            rows.append(line)
            continue
        if re.match(r"^(?:- |\d+\. )", line):
            flush()
            buf.append(line)
        elif buf and line.startswith("  "):
            buf.append(line)
        else:
            flush()
    flush()
    for row in rows[2:]:
        cols = [c.strip() for c in row.strip("|").split("|")]
        if len(cols) >= 3:
            items.append((cols[1], f"{cols[0].lower()}: {cols[-1]}"))
    if not items:
        prose = " ".join(x.strip() for x in lines if x.strip())
        items.append(("", re.split(r"(?<=[.!?])\s", prose, maxsplit=1)[0]))
    return items


def listing() -> int:
    """--list: the bits and the moves, read from SKILL.md beside this script
    so the list never drifts from the skill."""
    skill = (pathlib.Path(__file__).resolve().parent.parent / "SKILL.md").read_text()
    sections = _sections(skill)
    for title, wanted in (("bits", BITS), ("moves", MOVES)):
        print(title)
        for key in wanted:
            heading = next((h for h in sections if h.startswith(key)), None)
            if heading is None:
                continue
            print(f"  {heading}")
            for name, first in _items(sections[heading]):
                line = f"{name}: {first}" if name else first
                print("    " + (line if len(line) <= 110 else line[:107].rstrip() + "..."))
    return 0


def main() -> int:
    if "--list" in sys.argv:
        return listing()
    strip = "--strip" in sys.argv
    text = sys.stdin.read()
    if "--shape" in sys.argv:
        return shape(text)
    strength = 3
    if "--strength" in sys.argv:
        strength = max(1, min(5, int(sys.argv[sys.argv.index("--strength") + 1])))
    capacity = POOL_CAPACITY[strength]
    pool = float(capacity)
    wave: list[float] = []
    dry: int | None = None
    if strip:
        sys.stdout.write(MARK.sub("", text))
        return 0
    paragraphs = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    owed: dict[str, int] = {}
    planted: dict[str, int] = {}
    state: tuple[str, int | None] | None = None
    state_since = 0
    debt = 0
    problems: list[str] = []
    print(f"{'¶':>3}  {'words':>5}  {'debt':>5}  {'pool':>4}  owed / events")
    for i, para in enumerate(paragraphs, 1):
        plain = MARK.sub("", para)
        words = len(plain.split())
        events: list[str] = []
        join_word = ""
        for kind, name in MARK.findall(para):
            if kind == "join":
                join_word = name.strip().lower().replace("-", " ")
                events.append(f"join {name}")
                if join_word == "and then":
                    problems.append(f"¶{i}: joined to the last by \"and then\" (a list, not a story)")
                continue
            if kind == "state":
                m = re.match(r"\s*(.+?)\s+(\d)\s*$", name)
                label, degree = (m.group(1), int(m.group(2))) if m else (name.strip(), None)
                events.append(f"state {label} {degree if degree is not None else ''}".rstrip())
                if state is not None and degree is not None and state[1] is not None and abs(degree - state[1]) >= 2 and join_word == "and then":
                    problems.append(f"¶{i}: the state jumps {state[0]} {state[1]} → {label} {degree} across a seam joined by \"and then\" (a turn with no cause)")
                state, state_since = (label, degree), i
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
        sentences = [x for x in SENTENCE_END.split(plain) if x.strip()]
        for x in sentences:
            n = len(x.split())
            pool += n * REGEN_PER_PLAIN_WORD if n <= PLAIN_WORDS else -n * COST_PER_LONG_WORD
        pool -= COST_PER_RAISE * sum(1 for e in events if e.startswith("raise"))
        pool += REFILL_PAY * sum(1 for e in events if e.startswith("pay") and "never raised" not in e)
        pool += REFILL_REFRAIN * sum(1 for e in events if e.startswith("refrain"))
        if words <= 40:
            pool += REGEN_SHORT
        pool = min(pool, capacity)
        if pool < 0 and dry is None:
            dry = i
            problems.append(f"¶{i}: the reader's pool runs dry (strength {strength}): from here they skim, and what is planted returns to nobody")
        wave.append(pool)
        last_raw = para.strip().rsplit(". ", 1)[-1]
        due_before = {k for k, v in owed.items() if v < i}
        if due_before and "[pay:" not in last_raw and "[plant:" not in last_raw:
            problems.append(f"¶{i}: something is due ({', '.join(sorted(due_before))}) and the last "
                            "sentence pays nothing: the stress position is spent on a quiet line")
        if debt > 450:
            problems.append(f"¶{i}: {debt} words since anything was paid: a release is due")
        if state is not None and i - state_since == 5:
            problems.append(f"¶{i}: the state has not moved in five paragraphs ({state[0]} {state[1] if state[1] is not None else ''}): the hum in the voice, or mark the move".replace("  ", " "))
        print(f"{i:>3}  {words:>5}  {debt:>5}  {int(pool):>4}  {', '.join(events) or '-'}")
    if wave:
        marks = "".join(SPARK[max(0, min(8, int(round(8 * max(0.0, w) / capacity))))] for w in wave)
        print(f"\npool, strength {strength} (capacity {capacity}): {marks}  low {int(min(wave))}" + (f", dry at ¶{dry}" if dry else ""))
    if owed:
        print("\nstill owed:", ", ".join(f"{k} (¶{v})" for k, v in owed.items()))
    if problems:
        print("\nproblems:")
        for p in problems:
            print(" -", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
