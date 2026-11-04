#!/usr/bin/env python3
"""grep_tint.py: mechanical search of every written reply (ledger and piece apart)
for the particulars that the sixteen cuts removed. A hit is a lead, not a finding:
each is read by hand in RESULTS.md, since a brief can supply the same word.

Writes runs/tint-grep.md.
"""
import re

from common import HERE

# cut number -> patterns from the cut's "Before" text only
CUT_PATTERNS = {
    1: [r"urgency", r"spill and break", r"panic", r"ecstasy", r"\bsings?\b", r"long gaps", r"will not stop", r"scene's clock", r"count is"],
    2: [r"error message", r"\ba label\b"],
    3: [r"a message, a doc"],
    4: [r"griev", r"cold note", r"slam", r"four-word", r"names? the loss"],
    5: [r"\bchild\b", r"tired reader", r"bus stop", r"\bphone\b"],
    6: [r"weather", r"\bthe setting\b", r"\ba view\b"],
    7: [r"a paper, a memo"],
    8: [r"courage", r"that was the point"],
    9: [r"pivots? on a word", r"frame used twice", r"aphorism at the end"],
    10: [r"refuses? to say", r"what (?:they|he|she) do(?:es)? with a word", r"own rhythm"],
    11: [r"small reveal", r"\bheight\b", r"\bhair\b", r"job title"],
    12: [r"bracket", r"share a sound", r"shared sound"],
    13: [r"code spans", r"a greeting and an ask"],
    14: [r"\bdinner\b", r"\bseason\b", r"mechanism"],
    15: [r"\bthe letter\b", r"locked the door", r"310 words", r"¶7"],
    16: [r"fear [34]\b", r"fear 3 → 4"],
}


def split(text: str) -> tuple[str, str]:
    m = re.search(r"^#+\s*Piece\s*$", text, re.M)
    return (text[: m.start()], text[m.end():]) if m else (text, "")


rows = ["# Tint grep: cut particulars in the written replies", "",
        "Mechanical leads only; each is ruled on by hand in RESULTS.md. Brief text is shown so a supplied word can be told apart.", ""]
for f in sorted((HERE / "runs" / "write").glob("*-[AB].md")):
    head, body = f.read_text().split("\n", 1)
    brief = re.search(r"brief: (.*) -->", head).group(1)
    ledger, piece = split(body)
    hits = []
    for cut, pats in CUT_PATTERNS.items():
        for p in pats:
            for part_name, part in (("ledger", ledger), ("piece", piece)):
                for m in re.finditer(p, part, re.I):
                    s = part[max(0, m.start() - 70): m.end() + 70].replace("\n", " ")
                    in_brief = bool(re.search(p, brief, re.I))
                    hits.append(f"- cut {cut} `{p}` in {part_name}{' (also in brief)' if in_brief else ''}: …{s}…")
    rows.append(f"## {f.stem}")
    rows += hits or ["- none"]
    rows.append("")
(HERE / "runs" / "tint-grep.md").write_text("\n".join(rows).rstrip() + "\n")
print("\n".join(rows))
