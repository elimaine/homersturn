#!/usr/bin/env python3
"""blind.py: build the blind sheet. For each brief the two pieces (ledger stripped)
are shuffled and lettered P and Q; the key goes to blind-key.json, which the
reader does not open. The sheet is BLIND.md: brief, then P, then Q.
"""
import json
import random

from common import HERE, piece_of

briefs = json.loads((HERE / "briefs-2.json").read_text())
rng = random.Random()
key = {}
out = ["# Tilt bench, blind sheet", "", "Two pieces per brief, lettered P and Q at random. Rank each pair: which is the better piece for its brief, and in a few words why. The key is sealed in `blind-key.json`.", ""]
for name, brief in briefs.items():
    arms = ["A", "B"]
    rng.shuffle(arms)
    key[name] = {"P": arms[0], "Q": arms[1]}
    out += [f"## {name}", "", f"*Brief:* {brief}", ""]
    for letter, arm in zip("PQ", arms):
        text = (HERE / "runs" / f"{name}-{arm}.md").read_text()
        out += [f"### {name} {letter}", "", piece_of(text), ""]
(HERE / "blind-key.json").write_text(json.dumps(key, indent=2) + "\n")
(HERE / "BLIND.md").write_text("\n".join(out))
print("BLIND.md written; key sealed")
