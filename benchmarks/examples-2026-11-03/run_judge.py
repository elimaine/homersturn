#!/usr/bin/env python3
"""run_judge.py [brief ...]: blind paired judge, gpt-5.6-sol, one call per brief.

The two clean pieces (## Piece only; the ledgers would unblind arm B) go in a
seeded shuffled order as X and Y. The key is runs/judge-key.json. Output:
runs/judge/<brief>.md, served model in the first line, the raw answer below.
"""
import json
import random
import sys
import time

from common import HERE, call, piece_of

JUDGE = "gpt-5.6-sol"
SEED = 20261103
briefs = json.loads((HERE / "briefs-12.json").read_text())
cuts = (HERE / "cuts.md").read_text()
rules = (HERE / "skill-0.5.0-stripped.md").read_text()

keyfile = HERE / "runs" / "judge-key.json"
if keyfile.exists():
    key = json.loads(keyfile.read_text())
else:
    rng = random.Random(SEED)
    key = {"seed": SEED, "order": {n: ("AB" if rng.random() < 0.5 else "BA") for n in briefs}}
    keyfile.write_text(json.dumps(key, indent=1) + "\n")

PROMPT = """You are judging two short pieces written to the same brief by a writer that followed a writing skill. Two versions of the skill exist. They are the same text, except that one version has had its examples removed: the particulars it gave (a named state and its rhythm, a reader type, a genre's tells, a list of devices, a filled-in ledger line) were cut and the rule each served was stated bare. The cut list below gives every cut with the text before and after. The rule list is the full skill as it stands after the cuts. You are not told which piece was written with which version. Do not guess the version. Answer only from what is on the page.

Brief: {brief}

<piece id="X">
{x}
</piece>

<piece id="Y">
{y}
</piece>

<cut_list>
{cuts}
</cut_list>

<rule_list>
{rules}
</rule_list>

Answer four questions.

1. Instances. Does either piece reproduce an instance from the skill: a particular that the skill text gives as an example (in a cut list "Before" or anywhere in the rule list), carried into the piece word for word or in close paraphrase, when the brief did not supply it? A rule's own terms (therefore, but, the bands, the dial numbers, the names of figures) are not instances. A particular that the brief supplies is not an instance. For each one, quote the piece, quote the skill, and say whether the skill text you quote is only in a cut list "Before" ("cut") or is still in the rule list ("kept").

2. Rules no longer stated. Does either piece break a rule that only a cut example stated, a rule the rule list no longer says in so many words? For example, a piece that ends on the weather breaks the cut "never on the setting, the weather, a view". For each one, name the cut by its number, quote the piece, and say why it breaks it. Do not list faults against rules the rule list still states; list those separately under "other_faults" (at most three per piece, the largest).

3. Parallel and name. Does either piece contain a parallel (two characters given the same beat in different keys, one beat deliberately not mirrored) or a name used as a plant (a name that opens a reading before the person has spoken)? Does the brief invite a parallel, that is, does it give two characters a shared beat or situation?

4. Which piece is better written for its brief, judged by the rule list, and by how much ("X much", "X slightly", "even", "Y slightly", "Y much"), with one line why.

Reply with JSON only, in this shape:
{{
 "instances": [{{"piece": "X|Y", "piece_quote": "...", "skill_quote": "...", "where": "cut|kept"}}],
 "rules_no_longer_stated": [{{"piece": "X|Y", "cut": 0, "piece_quote": "...", "why": "..."}}],
 "other_faults": [{{"piece": "X|Y", "rule": "...", "piece_quote": "..."}}],
 "parallel": {{"brief_invites": true, "X": {{"parallel": false, "name_plant": false, "evidence": "..."}}, "Y": {{"parallel": false, "name_plant": false, "evidence": "..."}}}},
 "better": {{"verdict": "X much|X slightly|even|Y slightly|Y much", "why": "..."}}
}}
Empty lists are allowed and expected when there is nothing."""

names = sys.argv[1:] or list(briefs)
for name in names:
    out = HERE / "runs" / "judge" / f"{name}.md"
    if out.exists():
        print("have", out.name, flush=True)
        continue
    order = key["order"][name]
    pieces = {arm: piece_of((HERE / "runs" / "write" / f"{name}-{arm}.md").read_text().split("\n", 1)[1]) for arm in "AB"}
    x, y = pieces[order[0]], pieces[order[1]]
    reply, served, secs = call(JUDGE, PROMPT.format(brief=briefs[name], x=x, y=y, cuts=cuts, rules=rules))
    head = f"<!-- judge {JUDGE}; {served}; {secs:.0f}s; brief {name}; X = arm {order[0]}, Y = arm {order[1]} (key in runs/judge-key.json, seed {SEED}) -->"
    if reply.startswith("ERROR"):
        print(f"{name}: {reply[:200]}", flush=True)
        sys.exit(1)
    out.write_text(head + "\n\n" + reply.strip() + "\n")
    print(f"{name}: {secs:.0f}s; {served}", flush=True)
    time.sleep(5)
