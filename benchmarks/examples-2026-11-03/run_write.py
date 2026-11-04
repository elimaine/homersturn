#!/usr/bin/env python3
"""run_write.py <arm: A|B> [brief ...]: one reply per brief on one arm's frozen text, writer claude-fable-5-1.

Sequential, one call in flight. Skips briefs already written. Output:
runs/write/<brief>-<arm>.md, served model in the first line.
"""
import json
import sys
import time

from common import HERE, WRITE_PROMPT, call

WRITER = "claude-fable-5-1"
ARMS = {"A": HERE / "skill-0.4.6-frozen.md", "B": HERE / "skill-0.5.0-stripped.md"}

arm = sys.argv[1]
skill = ARMS[arm].read_text()
briefs = json.loads((HERE / "briefs-12.json").read_text())
names = sys.argv[2:] or list(briefs)
for name in names:
    out = HERE / "runs" / "write" / f"{name}-{arm}.md"
    if out.exists():
        print("have", out.name, flush=True)
        continue
    reply, served, secs = call(WRITER, WRITE_PROMPT.format(brief=briefs[name], skill=skill))
    head = f"<!-- arm {arm} ({ARMS[arm].name}); writer {WRITER}; {served}; {secs:.0f}s; brief: {briefs[name]} -->"
    if reply.startswith("ERROR"):
        print(f"{name} {arm}: {reply[:200]}", flush=True)
        (HERE / "runs" / "write" / f"{name}-{arm}.error.md").write_text(head + "\n\n" + reply + "\n")
        sys.exit(1)
    out.write_text(head + "\n\n" + reply.strip() + "\n")
    print(f"{name} {arm}: {len(reply.split())} words, {secs:.0f}s; {served}", flush=True)
    time.sleep(5)
