#!/usr/bin/env python3
"""run_readback.py <reader> <arm: A|B>: one read-back call per reader per arm.

The reader gets the arm's frozen text and is asked, for each of the nineteen
entries (nine figures, ten sentence rules), when to use it, when not, an
example it invents, and a misuse. Output: runs/readback/<reader>-<arm>.md,
served model in the first line.

deepseek-flash is refused by common.call (Together bills a key); gate 2
covers subscription routes only.
"""
import sys

from common import HERE, call

ARMS = {"A": HERE / "skill-0.4.6-frozen.md", "B": HERE / "skill-0.5.0-stripped.md"}

ENTRIES = """F1 The recursive paragraph
F2 The litany
F3 The withheld word
F4 The crescendo
F5 The revision
F6 The parallel
F7 The swear
F8 The dash (with the semicolon, the comma-and, the participial tail and the parenthesis)
F9 The figure hums too
S1 The character in the subject, the action in the verb
S2 One thing, one name
S3 The common word for the common thing
S4 The narrator's opinion on the word, not in a trailing clause
S5 Open a sentence on its subject
S6 One hedge per claim
S7 The example after the claim, the definition before its use
S8 Concede before you are forced; the title is the first raise
S9 A name is a plant at the scale of the cast
S10 A cliché is a refrain planted by other texts"""

PROMPT = """Below is a writing skill. Read it, then take every figure in its section "The figures and the accents" and every rule in its section "The sentence". These are the nineteen entries, in the skill's order:

{entries}

For each entry, give exactly four lines:
When: when a writer should use it, in one line.
Not: when a writer should not, in one line.
Example: an example you invent, in one line.
Misuse: what misusing it looks like, in one line.

Head each entry with its id and name, as listed. Answer from the skill's text. Nothing before the first entry and nothing after the last.

<skill>
{skill}
</skill>"""

reader, arm = sys.argv[1], sys.argv[2]
out = HERE / "runs" / "readback" / f"{reader}-{arm}.md"
if out.exists():
    sys.exit(f"have {out.name}")
reply, served, secs = call(reader, PROMPT.format(entries=ENTRIES, skill=ARMS[arm].read_text()))
if reply.startswith("ERROR"):
    sys.exit(f"{reader} {arm}: {reply[:200]}")
out.write_text(f"<!-- read-back; reader {reader}; arm {arm} ({ARMS[arm].name}); {served}; {secs:.0f}s -->\n\n" + reply.strip() + "\n")
print(f"{reader} {arm}: {len(reply.split())} words, {secs:.0f}s; {served}", flush=True)
