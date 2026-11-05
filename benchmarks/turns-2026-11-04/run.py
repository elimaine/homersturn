#!/usr/bin/env python3
"""run.py <arm: A|B> [brief ...]: one reply per brief on one arm's frozen text plus
its references, writer claude-fable-5-1 at high. Sequential, one call in flight.
Skips briefs already written. Output: runs/<brief>-<arm>.md, served model in the
first line.
"""
import json
import sys
import time

from common import ARMS, HERE, WRITE_PROMPT, arm_text, call

WRITER = "claude-fable-5-1"
arm = sys.argv[1]
skill = arm_text(arm)
briefs = json.loads((HERE / "briefs-6.json").read_text())
for name in sys.argv[2:] or list(briefs):
    out = HERE / "runs" / f"{name}-{arm}.md"
    if out.exists():
        print("have", out.name, flush=True)
        continue
    reply, served, secs = call(WRITER, WRITE_PROMPT.format(brief=briefs[name], skill=skill))
    head = f"<!-- arm {arm} ({ARMS[arm][0]} + {', '.join(ARMS[arm][1])}); writer {WRITER} high; {served}; {secs:.0f}s -->"
    if reply.startswith("ERROR"):
        print(f"{name} {arm}: {reply[:200]}", flush=True)
        (HERE / "runs" / f"{name}-{arm}.error.md").write_text(head + "\n\n" + reply + "\n")
        sys.exit(1)
    out.write_text(head + "\n\n" + reply.strip() + "\n")
    print(f"{name} {arm}: {len(reply.split())} words, {secs:.0f}s; {served}", flush=True)
    time.sleep(5)
