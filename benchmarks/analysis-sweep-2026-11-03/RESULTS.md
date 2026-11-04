# The analysis sweep: what the framework did not account for

Run `sweep-03` (2026-11-03). Claude Opus 5.5 at high reasoning effort,
48,000-token cap, through CliProxyAPI on the Claude logins. Every analysis
is in `runs/sweep-03/analyses/`, the synthesis in `runs/sweep-03/synthesis.md`,
the prompts and the skill's hash in `runs/sweep-03/protocol.json`. Two
earlier runs failed on the instrument: at the default effort Opus spent a
6,000-token budget thinking and returned nothing for 15 of 16 calls
(`runs/sweep-01-empty`), and a low-effort rerun was stopped when Eli asked
for high (`runs/sweep-02-low`).

## The design in a line

Sixteen pieces: six acknowledged good (public domain, `good/`), six plain
machine prose (Haiku 5.5 to a one-line brief, `bad/`), four written by
Opus with the skill as its only instructions (`written/`, briefs in the
script). Each was analyzed with the skill's analyze mode and then asked,
under a fixed heading, what the framework does not account for. One
synthesis call clustered the 16 answers and listed what the analyses said
the skill got wrong. This is a model reading a model's rules against
texts; it finds gaps and contradictions, not truths. Evidence grade:
*instrument* for every item.

## Taken into the skill (commit after this run)

Ranked as the synthesis ranked them, with what was done.

1. **Voices other than the writer's** (5 analyses; good, machine, skill).
   A borrowed phrase is a manifold with two readings. Added under the
   sentence rules.
2. **The purpose table misfiles by form** (6; all sets). Rows added: the
   vignette (owes exactness), the opening of a long work, advice, the
   message to someone owed nothing. The principle (by reader, not form)
   was already the table's header.
3. **Honest joins beyond therefore/but** (4; all sets). Because, "and
   closer", the iterative "and", the procedural "then". Added to the join.
4. **Judge each tell against the ledger, not by its shape** (5; good
   only). Added to the unearned punch: look forward before firing.
5. **The joiner beyond the dash** (3; machine, skill). Semicolon,
   comma-and, participial tail. Added to the accents.
6. **Form that enacts its subject** (5; all sets). Rhythm as the scene's
   clock. Added to rhythm, with the exemption from the no-switch rule.
7. **Cliché and stock detail** (3; machine only). A refrain planted by
   other texts. Added to the sentence rules.
13. **Specificity and exactness** (4; machine only). The exact detail
    pays in kind and needs no promise. Added beside the cliché, and the
    vignette row carries it.
14. **Comedy and irony** (4; good, skill). Irony, bathos, deadpan under
    the trust account; amusement named as a feeling the rhythm list lacks.
15. **A trust column** (4; all sets). Already begun as the reader's
    willingness; the fillers and drains were added.
17. **Tempo: frequency** (2; good, skill). The iterative "and" covers the
    frequency case under the joins.
19. **The word-scale motif** and 24. **crescendo** (good). The crescendo
    is a figure now; the motif is the refrain at word scale and is named
    there.
20. **Renaming as payment** and 21. **the rare word as carrier** (good
    only). Carve-outs added to "one name" and "the common word".
22. **Punctuation as rest and aside** (good). The parenthesis added to the
    accents.
25. **Convention exemption** (good). Dialogue turns and step lists are
    exempt from the one-line-paragraph rule.
9. **The off-page ledger** (4; all sets). The `[pay: inferred]` mark, so
   dial 5 and the script stop contradicting each other.

## Ruled out, or left outside, and why

- **Sound** (10; 5 analyses). Outside the model. Named in a new section
  as what the skill does not hold, with a pointer to Poet, which does.
- **Whether a claim is true** (16). Outside; said so.
- **The reader as a parameter of time and knowledge** (23). Outside for
  writing; it belongs to a gloss. Said so.
- **Address and stance** (8), **the extended field** (18), **accidental
  readings beyond the sentence** (11), **the common word with a claimed
  sense** (12), **deliberate grammatical strain** (27), **a referent
  completed by preoccupation** (28), **the borrowed genre signal** (26).
  Real, and inside the model; 12 was taken (the loaded common word). The
  rest are one or two mentions and wait for a second sighting before they
  earn a line, since every line costs the reader of the skill.

## What the analyses said the skill got wrong, and the rulings

- "One thing, one name" closes renaming as approach: **conceded**, the
  carve-out is in.
- The join rule marks because, escalation, iteration and procedure as
  "and then": **conceded**, the four honest joins are in.
- The unearned-weight list fires on shape (colon, recap, superlative,
  question, adverb): **conceded**, judged forward now.
- "Do not end on atmosphere" contradicts the manifold where the
  atmosphere is the payment: **conceded**, with the Mississippi as the
  example.
- The recursive paragraph only at the end: **conceded**, the overture is
  in.
- Awe as few words and long gaps: **conceded**, the long sentence that
  will not stop is awe's other shape.
- "Do not switch rhythm inside a scene" flags rhythm used as a clock:
  **conceded**, exempted.
- One-line paragraphs flag dialogue: **conceded**, the convention
  exemption.
- The rare-word rule and the common word with a claimed sense:
  **conceded**, both carve-outs.
- The vignette fails by definition under the scene row: **conceded**, a
  row of its own.
- The estranged friend filed as a reader with a reason to finish:
  **conceded**, a row of its own.
- "The colour of strong tea" cut as dense on a quiet beat: **conceded**,
  exactness pays in kind.
- The withheld word and "raised, never paid" against dial 5: **conceded**,
  `[pay: inferred]`.
- The dash rule passes a letter made of other joiners: **conceded**, the
  other joiners are named.
- "Do not refrain a line told once" flags "distant land" (Walden): **not
  conceded**; the second telling of a line is the plant, the rule is about
  the third, and the analysis misread it. Clarity could be better; left.
- "Unfortunately" read as a propping adverb; "natural and pertinent" as a
  doublet (Walden): **not a rule error**; the analysis applied the sentence
  rules without looking forward, which the new sentence under the unearned
  punch now forbids.
- A 318-word block can only be read as a wall (Walden): **partly
  conceded** under the opening-of-a-long-work row, where the long block
  can be stance; the glance bench says it still costs the first reader
  (`../glance-2026-11-03/RESULTS.md`).
- In an excerpt the ledger marks off-page raises as missing (Origin):
  **an artifact of excerpting**, noted; `[pay: off-page]` covers it.
- A proposed revision broke a round/sound rhyme the skill could not hear
  (lighthouse): **conceded** as the sound limitation, stated in the new
  section.

## The skill's own tics, from its four pieces

- The dash as a joiner survived in the skill-written scene and in a blind
  draft outside the sweep (the mouse story): the writing pass does not
  catch what the analyze pass does. Open.
- The agent reply and the repo doc reached for a loaded common word (undo,
  step back). Now a carve-out.
- The lighthouse scene left a raise paid only by inference and the script
  flagged it: now `[pay: inferred]`.
- The naming post used "and closer" escalation and the analysis flagged
  it under the old join rule: fixed by the rule, not the piece.

## Threats

One judge model reading its own output; a model's rules read by a model;
16 pieces; no human read of the analyses yet. Every item is tagged
*instrument*. Nothing here is a finding about readers.
