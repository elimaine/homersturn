#!/usr/bin/env python3
"""unblind.py: map every judge answer from X/Y back to arms A/B using runs/judge-key.json.

Writes runs/judge-unblinded.json and prints a compact view.
"""
import json
import re

from common import HERE

key = json.loads((HERE / "runs" / "judge-key.json").read_text())["order"]
out = {}
for name, order in key.items():
    raw = (HERE / "runs" / "judge" / f"{name}.md").read_text().split("\n", 1)[1]
    m = re.search(r"\{.*\}", raw, re.S)
    d = json.loads(m.group(0))
    arm = {"X": order[0], "Y": order[1]}

    def tag(items):
        return [dict(i, arm=arm[i["piece"]]) for i in items]

    v = d["better"]["verdict"]
    for k, a in arm.items():
        v = v.replace(k, a)
    par = d["parallel"]
    out[name] = {
        "order": order,
        "instances": tag(d["instances"]),
        "rules_no_longer_stated": tag(d["rules_no_longer_stated"]),
        "other_faults": tag(d["other_faults"]),
        "parallel": {"brief_invites": par["brief_invites"], "A": par[order.index("A") and "Y" or "X"], "B": par[order.index("B") and "Y" or "X"]},
        "better": {"verdict": v, "why": d["better"]["why"]},
    }
(HERE / "runs" / "judge-unblinded.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
for n, r in out.items():
    print(f"\n### {n} (order {r['order']}) better: {r['better']['verdict']} — {r['better']['why']}")
    for i in r["instances"]:
        print(f"  INSTANCE {i['arm']} [{i['where']}]: {i['piece_quote']!r} <- {i['skill_quote']!r}")
    for i in r["rules_no_longer_stated"]:
        print(f"  CUTRULE {i['arm']} cut {i['cut']}: {i['piece_quote']!r} — {i['why']}")
    for i in r["other_faults"]:
        print(f"  fault {i['arm']}: {i['rule']}: {i['piece_quote']!r}")
    p = r["parallel"]
    print(f"  parallel: invites={p['brief_invites']} A={p['A']} B={p['B']}")
