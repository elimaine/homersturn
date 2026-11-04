# Intent: do the examples tint the output, and do the rules read without them

Written before any call, 2026-11-03 22:45 CST, on branch `lane/examples`
at `0f3e51f`.

## The user's words

Eli, 2026-11-03: "I don't like know that I like having examples, they
tint the output", then "Go ahead with your recs" (the recs being the two
tests below), then the ruling "I do not like" the examples, "for actual
writing the skill use fable". Gate 1 passed on those words. Gate 2 passed
for subscription routes only.

## The construct

**Tint**: a reply carries a particular that the skill text supplied as an
example, and the brief did not ask for. A particular is a named
state and its rhythm, a reader type, a genre's tells, a listed device, a
filled-in ledger value, a quoted line. Copying a rule's own terms
(therefore and but, the four honest joins, the bands, the dials' numbers,
the purpose-table rows) is not tint: those are kept in both arms on
purpose. A particular that the brief itself supplies is not tint either.

**Reads**: a reader given the skill text states, for an entry, when to
use it, when not, an example it invents, and a misuse, and the four lines
match the entry's intent. The key is the entry's own text in 0.4.6, which
holds the rule plus its examples; where 0.5.0 restates the rule, both
texts are given and the 0.4.6 intent is what has to survive.

## The arms

- A: `skill-0.4.6-frozen.md`, byte-identical to `SKILL.md` at `0f3e51f~1`.
- B: `skill-0.5.0-stripped.md`, byte-identical to `SKILL.md` at `0f3e51f`
  (Fable's cut, not this lane's).
- Mechanical diff (`git diff --no-index --word-diff`): the version line
  and exactly the sixteen places in `cuts.md`, nothing else. Checked
  before this file was written.

Both arms point at `references/` files that the model is not given.
Arm B's rhythm rule now sends the writer to the state table in
`references/mindset.md` for the shapes it used to list. With a frozen
text as the only instruction, B's writer cannot follow that pointer and
A's can read the shapes inline. This is a confound the cut made, it
favours A on any rhythm judgment, and it is reported.

## Test 1: the write side

This test is trying to reveal whether a writer given the 0.4.6 text puts
the skill's own examples into its pieces, and whether a writer given the
stripped text breaks a rule that only the examples stated.
(Eli: "they tint the output".)

- Items: the ten briefs in `../briefs-2026-11-03/briefs.json`, plus two
  added in `briefs-12.json`. `parallel-invited`: two people given the
  same beat forty years apart, which invites a parallel without naming
  the figure. `single-character`: one person alone, no second character
  and no occasion for a parallel or a name-plant.
- Writer: `claude-fable-5-1`, bare id, Claude OAuth logins (subscription),
  `reasoning_effort: high`, max_tokens 48000, the `WRITE_PROMPT` of
  `analysis_sweep.py` unchanged, the arm's text as the only instruction.
  One reply per brief per arm. One call in flight. Arm A's twelve run in
  full, then arm B's twelve, never interleaved in parallel.
- Judge: `gpt-5.6-sol` (Codex OAuth, subscription), a different engine
  from the writer. For each brief it gets the brief, the two clean
  pieces (the `## Piece` section only) in a seeded shuffled order as X
  and Y, `cuts.md` (the removed particulars), and the rule list, which
  is the full stripped 0.5.0 text (the rules as they now stand). It
  answers in JSON: which piece reproduces an instance from the skill,
  with the quote; which piece breaks a rule the stripped text no longer
  states, with the rule; for the two added briefs, whether a parallel or
  a name-plant appears and whether the brief invited it. The shuffle and
  its seed are recorded in `runs/judge-key.json`.
- The judge never sees the ledgers, since arm B's slot-template ledger
  would unblind it. I check the ledgers myself by `grep` for the cut
  ledger's particulars ("the letter", "locked the door", "310 words",
  "fear 3", "fear 4") and report them separately.
- Unit: the brief. Twelve data points, one reply each, so the result is
  a pattern (counts, no interval). No claim of "clears zero": with one
  sample per cell there is no variance estimate, and the brief-level
  sign test cannot reach 0.05 unless at least six briefs all go one way.

## Test 2: the read-back

This test is trying to reveal whether a model that reads only the rules,
with no examples, can still say when to use each figure and each sentence
rule, when not to, and what misuse looks like. (Eli: "do the rules still
read without them", from the recs.)

- Entries: the nine figures in "The figures and the accents" (recursive
  paragraph, litany, withheld word, crescendo, revision, parallel, swear,
  dash, the figure hums) and the ten rules in "The sentence". Nineteen
  entries in total.
- Readers: `claude-fable-5-1`, `claude-opus-5-5` (subscription), one call
  per arm each, at high effort. Four calls.
- `deepseek-flash` is named in the brief, but `/v1/models` shows it
  `owned_by: together`, which is a key-billed route. The gate-2 rule says
  that "no call may go to any `anthropic-api/` id or any id that bills a
  key", so its two calls are not made. The script takes the reader as an
  argument, so Eli can run them with one command if he approves the
  Together key. In their place, and labelled as a substitute, I run
  `gpt-5.6-luna` (Codex OAuth, subscription, a non-Claude engine), one
  call per arm.
- Scoring: I score every line against the entry's 0.4.6 text as reads
  right, reads wrong, or missing, and quote the reader's words for every
  entry that reads wrong. The scorer is Opus, and Opus is also one of the
  readers. That is a self-preference risk, and it is reported. I also
  note any invented example that copies an instance from the skill,
  because that is tint showing in the read-back.

## Call count and routes

| role | model | route | calls |
|---|---|---|---|
| writer | claude-fable-5-1 | Claude OAuth (subscription) | 24 |
| judge | gpt-5.6-sol | Codex OAuth (subscription) | 12 |
| read-back | claude-fable-5-1, claude-opus-5-5 | Claude OAuth | 4 |
| read-back (substitute) | gpt-5.6-luna | Codex OAuth | 2 |
| read-back (not run, key-billed) | deepseek-flash | Together key | 0 of 2 |
| probes | each model, tiny | as above | up to 3 |

That makes 42 real calls, all on subscription. None goes to an
`anthropic-api/` id. The served model is read from
`~/.cli-proxy-api/logs/main.log` after each call completes, using only
the log lines written during that call, and is put in each file's first
line.

## What would surprise Eli

- No arm-A piece reproduces a cut instance. That would mean the examples
  do not tint at this scale, and the reason to cut them would rest on
  the read-back alone.
- Arm-B readers get an entry wrong that arm-A readers get right. That
  would mean an example was carrying the rule, and the bare statement
  does not.
- Arm B writes worse on rhythm, which the pointer confound above
  predicts. That would be a fault of the cut's pointer, not evidence
  that the examples were needed.
