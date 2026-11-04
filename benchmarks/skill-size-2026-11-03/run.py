#!/usr/bin/env python3
"""Three sizes of the skill, one blind brief each: which size writes best?
Outputs runs/<variant>.md (ledger + piece). Opus 5.5, high effort, through CliProxyAPI."""
import sys, time, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "analysis-sweep-2026-11-03"))
import analysis_sweep as a  # noqa: E402
BRIEF = ("A one-page story (about 500 words): a mouse finds a sword and defends the kingdom against an evil chinchilla. "
         "The reader should feel inspired, and should hate the chinchilla. Ambiguity 4. Mindset: the writer's choice; say it in the ledger.")
key = a.proxy_key()
(ROOT / "runs").mkdir(exist_ok=True)
for variant in sys.argv[1:] or ("slim-slim", "slim", "now"):
    skill = (ROOT / f"{variant}.md").read_text()
    t = time.time()
    reply = a.call(key, a.WRITE_PROMPT.format(brief=BRIEF, skill=skill))
    (ROOT / "runs" / f"{variant}.md").write_text(reply.strip() + "\n")
    print(f"{variant}: skill {len(skill.splitlines())} lines, reply {len(reply.split())} words, {time.time() - t:.0f}s", flush=True)
