---
name: homersturn
version: 0.2.1-slim-slim
description: Write, revise and analyze prose as a manifold of meanings presented like music; the ledger of promise and payment, the glance, three dials, the punches, the do-nots.
---

# homersturn

Ambiguity is the most powerful tool in good writing and the most abused one
in machine writing. A flat model says ambiguous things everywhere, at the
same density, and the reader stops hearing any of it. A writer places
meaning the way a composer places a chord: where something is owed, where
something is paid, and nowhere else. This skill is the placement.

## The brief and the three dials

Before writing, one line: the purpose (who reads, and whether they can
leave), the plain meaning, what it carries under that, and three dials.

- **Ambiguity 1 to 5, default 4**: how much the reader is asked to carry.
  1 is one reading a sentence, everything told; 5 is readings held to the
  last line for a reader who will read twice.
- **Mindset**: who is speaking, in what state, and how far gone, 1 to 5. A
  state is a prior over readings and reaches the page through attention:
  the state picks the details, the details set the length, the length the
  rhythm. A model's default state is helpful and even, with nothing at
  stake, and that is what the hum is. The state moves across a page, by
  therefore or but, and the rhythm switches where it turns and nowhere
  else. Felt below shown is tension; shown above felt is melodrama.
- **The reader's strength**: a pool. Dense sentences, raises and stacked
  clauses spend it; plain sentences regenerate it; payments and refrains
  refill it at once; empty, the reader skims and nothing planted returns to
  anyone. Pace the spend against the regen. Whether they keep spending is
  trust times what is due, and trust is paid promises.

## The model

- **A passage is a manifold.** Every sentence holds the plain reading and
  the ones under it. Writing is choosing which stay open and which close.
  A reading opened by accident (a pronoun with two candidates, a thing
  renamed, a loaded common word) is closed.
- **Meaning is a ledger.** A detail that is also a sign, a line with a
  second sense, a question: each raises. A consequence told plainly, a
  question answered, a line that returns: each pays. Density is earned only
  where something is being raised that will be paid; a punch only where
  something is owed. Pay only what was raised: the unasked clarification
  spends the pool and the trust.
- **Rhythm is emotion.** Short hard stops for fear and urgency; sentences
  that spill for panic or ecstasy; a line that sings for grief and love;
  joined, moving sentences for ease; few words and long gaps, or one
  sentence that will not stop, for awe.
- **Tempo is the frame.** Scene, summary, pause; say which. Most flat prose
  is scene tempo for what deserved summary.
- **The glance.** The page is read before the words. Open on a paragraph
  the eye takes whole, and the second paragraph is the next wall. Equal
  paragraphs hum, but at a glance even short blocks invite; the hum is
  heard while reading. A list of sentences is "and then" made visible.
- **Two positions.** The start of a unit holds what the reader already
  holds; the end holds what changed. Never end on the setting or a
  qualifier. The reader who can leave gets the point at the top; the one
  who stayed gets it at the bottom. At piece scale: the abstract first, and
  the ending completes it.
- **The join.** Between paragraphs, therefore or but; "and then" is a list.
  Because, "and closer", the iterative and, and the procedural then are
  honest.
- **The three punches**, one at most: land (the consequence, plainly),
  refrain (a line planted twice comes back with its sense shifted), release
  (what changed, under eight words). Every tell (the superlative, the
  colon, the recap, the question) is judged by whether a later line pays it,
  never by its shape.
- **Deception** is a reading the writer opens knowing it is wrong, paid by
  a reveal that re-reads the page: never state the false thing, leave the
  clue on the page, and pay the trust back with interest.
- **The figure hums too.** One device at a steady rate, one frame reused,
  one aphorism at the end of every paragraph: ration them to where the pool
  is full. The dash joins two sentences that should have been two; at most
  one a paragraph, as a rest, and the semicolon is the same mark.

## On paper

Keep the ledger beside the draft: before each paragraph, what is owed, what
is due, the debt, the feeling, the state, then tempo, rhythm, role, band,
punch. Mark the draft with `[raise: x]`, `[pay: x]`, `[plant: "line"]`,
`[join: therefore|but|and then]`, `[state: fear 4]`; `python3
scripts/meaning_ledger.py --strength 3 < draft.txt` does the arithmetic and
draws the pool; `--shape` reads the glance of an unmarked draft.

## Analyze a piece

Name the purpose and the mindset from the evidence (never the person's
state, only the page's). Read the glance. Reconstruct the ledger: raised,
paid, debt, never paid. Check the seams and the two positions. Name the
accidental readings and the unearned weight, pattern, quoted line, fix.
Rank the three changes that would pay the most. No score, no guess at who
wrote it.

## Do not

- Do not write every paragraph at the same density or length; do not open
  on a wall; do not end on atmosphere unless the atmosphere is the payment.
- Do not point at a planted meaning; do not clarify what the reader holds.
- Do not reach for the rare word when the common one is right, or rename a
  thing to avoid repeating it, unless the new name is a payment.
- Do not join with "and then"; do not switch rhythm mid-scene; do not
  refrain a line told once.
- Do not end every paragraph on an aphorism; do not reuse a frame.
- Do not invent a claim, a number, a feeling, or an experience the person
  did not supply.
