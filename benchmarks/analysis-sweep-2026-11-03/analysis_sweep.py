#!/usr/bin/env python3
"""Analysis sweep: run the skill's analyze mode on good writing, on plain
machine prose, and on the skill's own output, and ask each time what the
framework does not account for. Then one synthesis call clusters the gaps.

  python3 analysis_sweep.py write    -> written/<brief>.txt (Opus writing with SKILL.md as its instructions)
  python3 analysis_sweep.py analyze  -> runs/<run>/analyses/<set>-<name>.md, one call per piece
  python3 analysis_sweep.py synth    -> runs/<run>/synthesis.md

Every reply is kept. Model: claude-opus-5-5 through CliProxyAPI.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL = (ROOT.parent.parent / "SKILL.md").read_text()
MODEL = "claude-opus-5-5"

BRIEFS = {
    "scene-lighthouse": "A scene, 250 words: a woman waits out a storm in a lighthouse. She is waiting for someone who is late. Ambiguity 4.",
    "post-naming": "A post, 250 words, for people who build software: why the name of a product should be chosen last. Ambiguity 3.",
    "repo-doc-saves": "A repo doc, 200 words: how the editor saves drafts (on a two-second pause and on leaving the page; the undo button undoes to the last save; hold it for a list of saves). Ambiguity 1.",
    "agent-reply-migration": "A reply from an agent to its orchestrator, 120 words: it migrated the payments table, found two rows with no customer, parked them in a holding table, and did not touch the invoices. Ambiguity 4, poetic language allowed, the plain reading must survive.",
}

ANALYZE_PROMPT = """You are using the writing skill below to analyze a piece. Follow its "Analyze a piece" section exactly: name the purpose from the evidence, read the glance, reconstruct the ledger, check the seams, give the five measurements per paragraph, the topic position, accidental readings, unearned weight, and the three changes that would pay the most. Report in the skill's shape: pattern, quoted line, fix in a few words. No score. Do not guess who wrote it.

Then, under a final heading "## What the framework does not account for", name anything in this piece that works or fails that no section of the skill names. Be concrete: quote the line, say what it does to a reader, and say whether the skill's model (where meaning goes; what the reader is owed; what the page looks like) could explain it if a section were added, or whether it is outside the model. If nothing is unaccounted for, say so in one line.

The skill:

<skill>
{skill}
</skill>

The piece:

<piece>
{piece}
</piece>"""

WRITE_PROMPT = """Write the piece described in the brief, following the skill below. Keep the paper ledger as the skill says, in brackets the final pass strips; then give the final text with the marks stripped. Output: first the ledger lines and the marked draft under "## Ledger", then the clean piece under "## Piece".

Brief: {brief}

<skill>
{skill}
</skill>"""

SYNTH_PROMPT = """Below are the "What the framework does not account for" sections from analyses of {n} pieces: well-known good writing, plain machine prose, and pieces written with the skill itself. Cluster them into candidate additions to the skill. For each cluster: a name; one line on what it is; how many analyses raised it and from which sets; whether the skill's model explains it (and the one-line account) or it is outside the model; one quoted example; and the evidence grade (seen in good writing, seen in machine prose, seen in the skill's own output). Rank by how much the skill would gain. Then list, separately, anything the analyses said the skill got wrong. Terse; every item on its own line.

{notes}"""


def proxy_key() -> str:
    conf = Path("/opt/homebrew/etc/cliproxyapi.conf").read_text()
    m = re.search(r"^api-keys:\s*\n\s*-\s*(\S+)", conf, re.M)
    if not m:
        sys.exit("no proxy key")
    return m.group(1)


EFFORT = "high"  # Eli, 2026-11-03: "Opus high is my preferred. Raise caps."; sweep-01 at the default returned nothing at 6000 tokens, the thinking ate it.


def call(key: str, text: str, max_tokens: int = 48000) -> str:
    body = json.dumps({"model": MODEL, "max_tokens": max_tokens, "reasoning_effort": EFFORT,
                       "messages": [{"role": "user", "content": text}]}).encode()
    req = urllib.request.Request("http://127.0.0.1:8317/v1/chat/completions", data=body,
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.load(r)
            return d["choices"][0]["message"]["content"] or ""
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(30 * (attempt + 1)); continue
            return f"ERROR {e.code}: {e.read().decode(errors='replace')[:300]}"
        except Exception as e:  # noqa: BLE001
            if attempt < 3:
                time.sleep(15); continue
            return f"ERROR {e!r}"
    return "ERROR unreachable"


def write(key: str) -> None:
    (ROOT / "written").mkdir(exist_ok=True)
    for name, brief in BRIEFS.items():
        out = ROOT / "written" / f"{name}.md"
        if out.exists():
            print("have", name); continue
        t0 = time.time()
        reply = call(key, WRITE_PROMPT.format(brief=brief, skill=SKILL))
        out.write_text(reply.strip() + "\n")
        print(f"wrote {name} ({len(reply.split())} words, {time.time() - t0:.0f}s)")
        time.sleep(3)


def pieces() -> list[tuple[str, str, str]]:
    out = []
    for f in sorted((ROOT / "good").glob("*.txt")):
        out.append(("good", f.stem, f.read_text()))
    for f in sorted((ROOT / "bad").glob("*.txt")):
        out.append(("machine", f.stem, f.read_text()))
    for f in sorted((ROOT / "written").glob("*.md")):
        t = f.read_text()
        m = re.search(r"## Piece\s*\n(.*)", t, re.S)
        out.append(("skill-written", f.stem, (m.group(1) if m else t).strip()))
    return out


def analyze(key: str, run: str) -> None:
    d = ROOT / "runs" / run / "analyses"
    d.mkdir(parents=True, exist_ok=True)
    (ROOT / "runs" / run / "protocol.json").write_text(json.dumps({
        "run": run, "model": MODEL, "started": datetime.now(timezone.utc).isoformat(),
        "reasoning_effort": EFFORT, "max_tokens": 48000, "analyze_prompt": ANALYZE_PROMPT, "write_prompt": WRITE_PROMPT, "synth_prompt": SYNTH_PROMPT,
        "skill_sha256": __import__("hashlib").sha256(SKILL.encode()).hexdigest()}, indent=1) + "\n")
    for kind, name, text in pieces():
        out = d / f"{kind}-{name}.md"
        if out.exists():
            print("have", out.name); continue
        t0 = time.time()
        reply = call(key, ANALYZE_PROMPT.format(skill=SKILL, piece=text))
        out.write_text(reply.strip() + "\n")
        print(f"{kind}/{name}: {len(reply.split())} words, {time.time() - t0:.0f}s" + (" ERROR" if reply.startswith("ERROR") else ""))
        time.sleep(3)


def synth(key: str, run: str) -> None:
    d = ROOT / "runs" / run / "analyses"
    notes = []
    for f in sorted(d.glob("*.md")):
        t = f.read_text()
        m = re.search(r"#+\s*[^\n]*does not account for[^\n]*\n(.*)", t, re.S | re.I)
        notes.append(f"### {f.stem}\n{(m.group(1) if m else '(section missing)').strip()}\n")
    reply = call(key, SYNTH_PROMPT.format(n=len(notes), notes="\n".join(notes)), 64000)
    (ROOT / "runs" / run / "synthesis.md").write_text(reply.strip() + "\n")
    print(reply[:3000])


if __name__ == "__main__":
    cmd = sys.argv[1]
    run = sys.argv[2] if len(sys.argv) > 2 else datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    k = proxy_key()
    {"write": lambda: write(k), "analyze": lambda: analyze(k, run), "synth": lambda: synth(k, run)}[cmd]()
