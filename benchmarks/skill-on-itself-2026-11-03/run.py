#!/usr/bin/env python3
"""The skill's analyze pass run on the skill itself. Opus 5.5, high effort, through CliProxyAPI.
Writes runs/<version>.md. The piece is SKILL.md with its frontmatter stripped; the skill is SKILL.md whole."""
import sys, time, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "analysis-sweep-2026-11-03"))
import analysis_sweep as a  # noqa: E402
if len(sys.argv) > 1:
    a.MODEL = sys.argv[1]  # e.g. claude-fable-5-1; Eli, 2026-11-03: "Run it with fable high. Fable for high stakes."
SKILL = (ROOT.parent.parent / "SKILL.md").read_text()
version = re.search(r"^version: (.*)$", SKILL, re.M).group(1).strip()
piece = re.sub(r"^---\n.*?\n---\n", "", SKILL, count=1, flags=re.S)
PROMPT = a.ANALYZE_PROMPT + ("\n\nThe piece is the skill's own text. Its purpose is a repo doc read by a model and by a person who can leave; "
    "judge it as that, and judge it against its own rules: where does the skill fail to do what it says? "
    "Where the skill's text could demonstrate a rule structurally (its shape, its two positions, one refrain) "
    "without a flourish a reader who came for a rule would notice, say where.")
(ROOT / "runs").mkdir(exist_ok=True)
key = a.proxy_key()
t = time.time()
reply = a.call(key, PROMPT.format(skill=SKILL, piece=piece))
out = ROOT / "runs" / f"{version}-{a.MODEL}.md"
out.write_text(reply.strip() + "\n")
print(f"{version} {a.MODEL}: reply {len(reply.split())} words, {time.time() - t:.0f}s" + (" ERROR" if reply.startswith("ERROR") else ""), flush=True)
