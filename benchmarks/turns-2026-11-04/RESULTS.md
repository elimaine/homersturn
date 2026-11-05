# Turns bench, 2026-11-04: results

Intent card `INTENT.md`, written and committed before any call. Twelve
replies, every one served as `claude-fable-5-1` with no substitution
logged, one auth, 82 to 212 seconds a call. Sheet `BLIND.md`, key
`blind-key.json`, opened only after the ranking below.

## The ranking

Eli, on the blind sheet: "All of them the second, except Mara and tools."
The second is Q in every pair; Mara is the name in friend P. So:

| brief | picked | arm | the other |
|---|---|---|---|
| biopsy | Q | **B** 0.6.1 | A |
| tools | P | **B** 0.6.1 | A |
| backlog | Q | **A** 0.5.6 | B |
| hatch | Q | **B** 0.6.1 | A |
| house | Q | **B** 0.6.1 | A |
| friend | P | **A** 0.5.6 | B |

B, the keyed skill with the wheel, four of six. A took the post and the
message, the two briefs whose purpose row sits at dial 1 to 3 and whose
reader can leave. No reasons were given per pair, so that split is a
pattern to test, not a finding: it may be that the wheel pushes a writer
toward turns a leaving reader does not want, or it may be two draws.

Six pairs, once. A pattern, not a p-value.

## The secondary measure

Each reply's marked draft (the text under "## Ledger") was run through
`scripts/meaning_ledger.py` at 0.6.1, so both arms are priced on the
wheel whatever they were given. The trajectories, as marked:

| brief | A (0.5.6) | B (0.6.1) |
|---|---|---|
| biopsy | fear 3 → ease 2 → tenderness 3 | dread dorian 2 → dread 3 → joy 3 → joy mixolydian 2 (parallel) → shock 3 → sorrow dorian 2 |
| tools | anger 1 → anger 4 → (two marks the parser could not read) | eleven marks: anger 1 held → dread 2 → anger 2 → anger 4 → anger 1 → shock 2 (far, no bridge) → anger 1 → tenderness 1 |
| backlog | insistence 2 → tiredness 2 (three steps) → tenderness 2 | conviction 3 → conviction 3 → trust 2 → tenderness 2 → conviction 2 (lift) |
| hatch | curiosity 2 → fear 3 (relative flip) → awe 4 (parallel) | curiosity 2 → fear 3 (relative flip) → awe 4 (parallel) |
| house | tiredness 3 → tiredness 2 → tenderness 3 → ease 2 | ease 2 → ease 2 → sorrow 3 → sorrow dorian 2 (parallel) → ease 1 |
| friend | shame 3 → shame 4 → tenderness 2 (three steps) → tenderness 2 | shame 3 → shame 3 → trust 2 (lift) → tenderness 2 |

What it shows, read by hand:

- B marks more moves and names tints; A marks three or four states a
  piece. B's biopsy and house trajectories use the parallel where the
  brief wanted a re-read of one thing (joy to its own mixolydian, sorrow
  to its dorian), which is the wheel's own figure and was the picked
  piece both times.
- The hatch trajectories are identical in both arms. The brief dictated
  the path, and the wheel priced the same path as flip and parallel for
  both. That pair was picked B on the words, not the trajectory.
- tools-B has the one crossing with no bridge (anger to shock, far) and
  the most marks. Eli picked it anyway. The script's count is not the
  judge.
- The problem counts are noisy and not reported as a score: the marked
  section mixes the paper ledger lines with the draft, so word-debt
  figures run high, and "pays never raised" is high in both arms, which
  is marking discipline, not placement. biopsy-A's "not on the wheel"
  marks are arrows inside one bracket (`Fear 3 → Ease 2`), a format
  0.5.6 did not define, so a parse miss and not a fault.

## What to take

- The wheel is used when given: B's marks are wheel names with tints and
  the parallel appears where the brief asks for one thing re-read.
- Four of six for B on briefs built to force turns, with the two losses
  on the leaving-reader purposes. The next run that would pay: six
  leaving-reader briefs (posts, messages, agent replies) on the same two
  arms, to see whether the split holds.
- The secondary measure needs the marked draft separated from the paper
  ledger lines before it can count anything but trajectories.
