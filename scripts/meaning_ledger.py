#!/usr/bin/env python3
"""Arithmetic over a draft's own ledger marks (references/manifold-and-ledger.md).

Reads a draft on stdin. Marks: [raise: name] opens a promise, [pay: name]
pays it, [plant: "line"] plants a refrain, [join: therefore|but|and then] names
how the paragraph follows the last ([join: bridge] marks the bridge paragraph,
all momentum and no new fact), [state: name degree] marks the speaker's
state when it moves, with a tint between when there is one ([state: fear
phrygian 3]); the trajectory is listed beside the debt and priced on the
wheel (references/wheel.md). --strength N
(1 to 5, default 3) sets the reader's pool, drawn as a wave at the end. Reports per paragraph the debt
(words since the last payment), what is owed, and the failures the marks
make visible. Strips nothing; use --strip to print the draft without marks.

--shape needs no marks: it prints what a page says before a word is read
(the glance): each paragraph's words and sentences, the first paragraph's
share, the spread of lengths, the longest block, one-line paragraphs, lists,
bold, subheads, dashes, and neighbouring paragraphs that open on the same
words. --wheel prints the keys and the moves between them, with their cost.
"""
from __future__ import annotations

import pathlib
import re
import sys

MARK = re.compile(r"\[(raise|pay|plant|join|state):\s*(.+?)\]")

# The wheel (references/wheel.md): twelve positions round the circle of
# fifths, a bright and a dark state at each sharing the same details. A step
# is a fifth; the far side is six. The names are the defaults; a state not on
# the wheel is reported and not priced.
WHEEL = [("ease", "tiredness"), ("tenderness", "anger"), ("trust", "suspicion"),
         ("conviction", "insistence"), ("pride", "shame"), ("curiosity", "fear"),
         ("anticipation", "dread"), ("surprise", "shock"), ("awe", "terror"),
         ("joy", "sorrow"), ("abandon", "maudlin"), ("relish", "disgust")]
ALIASES = {"drunkenness": (11, None), "drink": (11, None), "sadness": (10, "dark"),
           "grief": (10, "dark"), "rage": (2, "dark"), "calm": (1, "bright"),
           "wonder": (9, "bright"), "menace": (7, "dark"), "contempt": (4, "dark")}
MODES = {"ionian": "bright", "aeolian": "dark", "lydian": "bright", "mixolydian": "bright",
         "dorian": "dark", "phrygian": "dark", "locrian": None, "bright": "bright", "dark": "dark"}
MOVE_COSTS = [("Hold", "0", "none; rhythm holds", "the form holding; a hum by the fifth paragraph"),
         ("Relative flip", "0, mood", "a payment, no new cause", "restraint failing, or composure regained"),
         ("Neighbour", "1", "one therefore or but", "the story moving"),
         ("Lift", "2", "the \"and closer\" join", "escalation"),
         ("Parallel", "3, mood", "the next fact", "the revision: the same thing re-read"),
         ("Far", "4 to 6", "a bridge paragraph", "a turn earned, or a seam"),
         ("Jolt", "5 or 7, mood", "once a piece, late", "the twist, the swear"),
         ("Degree up three", "any", "never without one of the above", "melodrama, or a seam")]


def place(name: str) -> tuple[int, str | None] | None:
    """A state's position on the wheel, 1 to 12, and its mood."""
    key = name.strip().lower()
    for i, (bright, dark) in enumerate(WHEEL, 1):
        if key == bright:
            return i, "bright"
        if key == dark:
            return i, "dark"
    return ALIASES.get(key)


def parse_state(mark: str) -> tuple[str, str | None, int | None]:
    """'fear phrygian 3' -> ('fear', 'phrygian', 3); the tint and degree optional."""
    words = mark.split()
    degree = int(words.pop()) if words and re.fullmatch(r"[1-5]", words[-1]) else None
    tint = words.pop().lower() if len(words) > 1 and words[-1].lower() in MODES else None
    return " ".join(words), tint, degree


def move(a: tuple[int, str | None], b: tuple[int, str | None]) -> tuple[str, int]:
    """The move from one place to another, named as the wheel names it, with its steps."""
    steps = min((a[0] - b[0]) % 12, (b[0] - a[0]) % 12)
    flip = a[1] is not None and b[1] is not None and a[1] != b[1]
    if steps == 0:
        return ("relative flip" if flip else "hold"), 0
    if steps == 3 and flip and ((a[1] == "bright" and (a[0] - b[0]) % 12 == 3) or (a[1] == "dark" and (b[0] - a[0]) % 12 == 3)):
        return "parallel", 3
    if steps == 5 and flip:
        return "jolt", 5
    if steps == 1:
        return "neighbour", 1
    if steps == 2:
        return "lift", 2
    if steps >= 4:
        return "far", steps
    return "three steps", steps


def wheel() -> int:
    """--wheel: the keys and the moves, read from the table above."""
    print("the wheel: a step is a fifth; the far side is six; bright and dark share the details")
    for i, (bright, dark) in enumerate(WHEEL, 1):
        print(f"  {i:>2}  {bright:<13} {dark:<11} opposite {((i + 5) % 12) + 1}")
    print("the moves")
    for name, steps, cost, reads in MOVE_COSTS:
        print(f"  {name:<16} {steps:<13} {cost:<32} {reads}")
    print("tints (modes): " + ", ".join(m for m in MODES if m not in ("bright", "dark")))
    return 0

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
    leads = tics(rows)
    if leads:
        print("\ntic leads (structural, each a lead to read by hand, not a finding):")
        for line in leads[:24]:
            print(" -", line)
        if len(leads) > 24:
            print(f"   and {len(leads) - 24} more")
    return 0


# The machine's tics, as structure and never as a word list (evidence.md,
# "Detectors worth borrowing"): a word list goes stale and these do not.
TICS = [
    ("the dash that joins", re.compile(r"\w[—–] ?\w|\w [—–-] \w")),
    ("not X but Y", re.compile(r"\b(?:not|never)\b[^.;:?!]{1,40}?\bbut\b|\bnot (?:only|just|merely)\b", re.I)),
    ("the rhetorical question", re.compile(r"\?(?:\s|$)")),
    ("the trailing judgement clause", re.compile(r", which (?:is|was|makes|means|matters|says)\b")),
    ("the colon before a reveal", re.compile(r":\s(?:[\w'\"]+\s){0,3}[\w'\"]+[.!]$")),
    ("the tricolon", re.compile(r"\b(?!(?:" + "|".join(sorted(STOP)) + r")\b)\w+, \w+,? and \w+\b")),
    ("the stacked hedge", re.compile(r"\b(?:perhaps|may|might|could|seems?|arguably|somewhat|likely|possibly)\b[^.]*\b(?:perhaps|may|might|could|seems?|arguably|somewhat|likely|possibly)\b", re.I)),
    ("the announced structure", re.compile(r"\b(?:in this (?:section|post|essay)|let's|let us|we will|first,)\b", re.I)),
    ("the both-sides close", re.compile(r"^(?:ultimately|in the end|overall|at the end of the day|in conclusion)\b", re.I)),
]


def tics(rows: list[tuple[int, str, int, int, str]]) -> list[str]:
    """Structural leads per paragraph: the pattern, the paragraph, the words it sits on."""
    out: list[str] = []
    for i, kind, words, sentences, para in rows:
        if kind in ("sub", "code") or para.startswith("|"):
            continue
        plain = re.sub(r"`[^`]*`", "", para)
        for name, pat in TICS:
            for m in pat.finditer(plain):
                snippet = plain[max(0, m.start() - 24):m.end() + 12].replace("\n", " ").strip()
                out.append(f"¶{i} {name}: '{snippet}'")
                break
        last = [x for x in SENTENCE_END.split(plain) if x.strip()]
        if kind == "prose" and last:
            tail = last[-1].strip()
            n = len(tail.split())
            if 2 <= n <= 8 and re.search(r"\b(?:is|are)\b", tail) and not re.search(r"\d", tail) and sentences > 1:
                out.append(f"¶{i} the short copula ending (an aphorism, or a land: judge against the ledger): '{tail}'")
    return out


BITS = ["The figures and the accents", "The three punches"]
MOVES = ["The join", "The two positions", "Forms", "The entrance"]


def _sections(skill: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    name = ""
    for line in skill.splitlines():
        if line.startswith("## "):
            name = re.sub(r"\s·\s\w+ \d$", "", line[3:].strip())
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
    if "--wheel" in sys.argv:
        return wheel()
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
    state_place: tuple[int, str | None] | None = None
    state_since = 0
    bridged_last = False
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
                label, tint, degree = parse_state(name)
                here = place(label)
                shown = label + (f" {tint}" if tint else "") + (f" {degree}" if degree is not None else "")
                if here is None:
                    events.append(f"state {shown} (not on the wheel)")
                elif state_place is not None:
                    kind_of, steps = move(state_place, here)
                    events.append(f"state {shown} ({kind_of}" + (f", {steps} steps" if kind_of in ("far", "lift") else "") + ")")
                    if steps >= 4 and join_word != "bridge" and not bridged_last:
                        problems.append(f"¶{i}: the state crosses the wheel, {state[0]} → {label}, {steps} steps, with no bridge paragraph (mark the bridge [join: bridge], or come round by steps)")
                    if kind_of == "jolt":
                        problems.append(f"¶{i}: {state[0]} → {label} is the jolt (the semitone): once a piece, late, and paid")
                else:
                    events.append(f"state {shown}")
                if state is not None and degree is not None and state[1] is not None and abs(degree - state[1]) >= 2 and join_word == "and then":
                    problems.append(f"¶{i}: the state jumps {state[0]} {state[1]} → {label} {degree} across a seam joined by \"and then\" (a turn with no cause)")
                if state is not None and degree is not None and state[1] is not None and abs(degree - state[1]) >= 3 and join_word in ("", "and then"):
                    problems.append(f"¶{i}: the degree jumps {state[1]} → {degree} with no join named: a subito, which is melodrama unless the ledger paid for it")
                state, state_since = (label, degree), i
                if here is not None:
                    state_place = here
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
        bridged_last = join_word == "bridge"
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
