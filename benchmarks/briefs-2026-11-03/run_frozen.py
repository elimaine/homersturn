#!/usr/bin/env python3
"""run_frozen.py <name> <brief-file> <skill-file> <model>: one blind reply on a frozen skill text; served model recorded."""
import sys, time, pathlib, re, subprocess
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "analysis-sweep-2026-11-03"))
import analysis_sweep as a  # noqa: E402
name, brief, skill, a.MODEL = sys.argv[1], pathlib.Path(sys.argv[2]).read_text(), pathlib.Path(sys.argv[3]).read_text(), sys.argv[4]
version = re.search(r"^version: (.*)$", skill, re.M).group(1).strip()
t = time.time(); reply = a.call(a.proxy_key(), a.WRITE_PROMPT.format(brief=brief, skill=skill))
tail = subprocess.run(["tail", "-n", "40", str(pathlib.Path.home() / ".cli-proxy-api/logs/main.log")], capture_output=True, text=True).stdout
served = re.findall(r'served model "([^"]+)" for requested model "' + re.escape(a.MODEL) + '"', tail)
served_line = f"served: {served[-1]}" if served else f"served: {a.MODEL} (no substitution logged)"
out = ROOT / "runs" / f"{name}-{version}-{a.MODEL}.md"
out.write_text(f"<!-- skill {version}; model {a.MODEL}; {served_line}; brief: {brief} -->\n\n" + reply.strip() + "\n")
print(f"{name} {version} {a.MODEL}: {len(reply.split())} words, {time.time()-t:.0f}s; {served_line}", flush=True)
