# Intent: does the keyed skill with the wheel place state turns better

Written before any call, 2026-11-04, on `main` at `0848109`.

## The user's words

Eli, 2026-11-04: "We will run a blind fable high to test. Ask me questions
first to get the settings right." The settings chosen: 0.6.1 against 0.5.6
as whole skills; six new briefs that force state turns; Eli judges blind
with a sealed key; six briefs by two arms, once.

## The construct

**A placed turn**: the state moves between paragraphs with its cause on
the page (therefore or but, or a bridge where the move is far), the
rhythm moves with it, and the piece ends in a state it did not start in
when the brief asks for that. The fault is the seam (a jump with no
cause), the hum (no move), and the subito (a jump in degree with no
cause). 0.6.1 adds the wheel (distances and priced moves) and writes each
section of the skill in its own key. The question is whether a writer
given 0.6.1 places turns better than one given 0.5.6, read blind.

Two measures. Primary: Eli's blind preference per pair, with a few words
why. Secondary, mechanical: each arm's marked draft run through
`scripts/meaning_ledger.py` at the current version, so both arms are
priced on the wheel whatever they were given; seams, crossings with no
bridge, hum and subito counted. The secondary reads 0.5.6's marks with a
tool 0.5.6 did not have, which is stated here so it is not mistaken for
a fair fight on its own.

## The arms

- A: `skill-0.5.6-frozen.md` (SKILL.md at `3e8cdf8`) with
  `mindset-0.5.6-frozen.md` (its `references/mindset.md`).
- B: `skill-0.6.1-frozen.md` (SKILL.md at `0848109`) with
  `mindset-0.6.1-frozen.md` and `wheel-0.6.1-frozen.md`.

The references are given in both arms because a single call has no tool
to read them with, and the wheel is what B is for. Earlier benches gave
the skill alone; this one differs there, on purpose.

## The briefs

`briefs-6.json`: a scene with two forced turns (biopsy), a confrontation
with a restraint that fails and returns (tools), a post with an honest
concession midway (backlog), a game turn climbing curiosity to fear to
something larger (hatch), a reflection with a verbatim refrain whose
sense turns with the state (house), and a message out of shame (friend).
Each names its purpose, plain meaning, what it carries, and the ambiguity
and strength dials; none names the mindset, which the writer sets and
must move.

## The run

Writer `claude-fable-5-1`, reasoning effort high, over CliProxyAPI on a
subscription route, one call in flight, the served model read from the
proxy log per request as the examples bench did. Prompt: the examples
bench's `WRITE_PROMPT`, unchanged. Output per reply: ledger and marked
draft under "## Ledger", the clean piece under "## Piece".

## The read

`blind.py` shuffles each pair into P and Q and seals the key. Eli ranks
each pair on `BLIND.md`. Unblinding and the secondary measure are written
to `RESULTS.md` after the ranking, never before. Six pairs show a pattern,
not a p-value.
