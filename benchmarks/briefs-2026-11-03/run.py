#!/usr/bin/env python3
"""One brief, the current SKILL.md as the only instructions, one blind reply.
usage: run.py <name> <brief text> [model]. Writes runs/<name>-<model>.md and appends the served model
from the proxy log (the warning is logged when the call completes)."""
import sys, time, pathlib, re, subprocess
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "analysis-sweep-2026-11-03"))
import analysis_sweep as a  # noqa: E402
name, brief = sys.argv[1], sys.argv[2]
if len(sys.argv) > 3:
    a.MODEL = sys.argv[3]
skill = (ROOT.parent.parent / "SKILL.md").read_text()
version = re.search(r"^version: (.*)$", skill, re.M).group(1).strip()
key = a.proxy_key()
t = time.time()
reply = a.call(key, a.WRITE_PROMPT.format(brief=brief, skill=skill))
log = pathlib.Path.home() / ".cli-proxy-api/logs/main.log"
tail = subprocess.run(["tail", "-n", "40", str(log)], capture_output=True, text=True).stdout
served = re.findall(r'served model "([^"]+)" for requested model "' + re.escape(a.MODEL) + '"', tail)
served_line = f"served: {served[-1]}" if served else f"served: {a.MODEL} (no substitution logged in the last 40 log lines)"
out = ROOT / "runs" / f"{name}-{a.MODEL}.md"
out.write_text(f"<!-- skill {version}; model {a.MODEL}; {served_line}; brief: {brief} -->\n\n" + reply.strip() + "\n")
print(f"{name} {a.MODEL} skill {version}: reply {len(reply.split())} words, {time.time() - t:.0f}s; {served_line}", flush=True)
