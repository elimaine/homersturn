---
name: homersturn
description: Write and revise prose as a manifold of meanings presented like music. Use when a passage must carry more than it says (ambiguity on purpose, foreshadowing, a second sense the reader completes later) without turning into flat, uniformly "deep" machine prose. Covers the ledger of promise and payment, where density is earned and where it is noise, the three punches (land, refrain, release), rhythm as emotion, tempo, forms with transitions, the stress position, the figures (recursive paragraph, litany, the withheld word), the swear as an accent, and the dash redeemed as a rest. Pairs with the Poet tool when it is available; works without it.
---

# homersturn

Ambiguity is the most powerful tool in good writing and the most abused one in
machine writing. A flat model says ambiguous things everywhere, at the same
density, and the reader stops hearing any of it. A writer places meaning the
way a composer places a chord: where something is owed, where something is
paid, and nowhere else. This skill is the placement. The name holds three
readings and keeps all of them, which is the method in miniature: the bard's
turn at the fire, the same story every night told so the room leans in at
the same places; the model's turn in a session, where this gets applied;
and Homer turning in his grave at what the machines did with his trade
before this. The last one is the one to earn your way out of.

Read `references/manifold-and-ledger.md` when the piece is longer than a page,
or when the user asks why a passage feels dense, flat, or hard to parse. The
ledger script is `scripts/meaning_ledger.py`; the paper ledger below says
when to run it.

Ambiguity is the most powerful tool in good writing and the most abused one in
machine writing. A flat model says ambiguous things everywhere, at the same
density, and the reader stops hearing any of it. A writer places meaning the
way a composer places a chord: where something is owed, where something is
paid, and nowhere else. This skill is the placement.

Read `references/manifold-and-ledger.md` first when the piece is longer than a
page or when the user asks why a passage feels dense, flat, or hard to parse.

## The model

- **A passage is a manifold, not a line.** Every sentence holds a cloud of
  readings a reader could take: the plain one and the ones that sit under it.
  Writing is choosing which readings stay open and which close. Before adding
  a layer, list the readings already present; a second sense a reader can
  complete later is worth more than a third image on the surface.
- **Meaning is a ledger of promise and payment.** A detail that is also a
  sign, a line with a second sense, an unanswered question: each raises a
  promise. A consequence told plainly, a question answered, a line that
  returns: each pays one. The reader carries the balance. Density is only
  earned where something is being raised that will be paid; a punch is only
  earned where something is owed. Dense on a beat that owes nothing is the
  failure mode: it reads as hard work for no payoff.
- **Rhythm is emotion, not decoration.** Pick the sentence rhythm from what
  the passage should make the reader feel: short hard stops for urgency and
  fear; sentences that spill and break for panic or ecstasy; a line that sings
  a little for grief and love; moving, joined sentences for ease; few words
  and long gaps for awe and aftermath. Do not switch rhythm inside an engaged
  scene; switch at its edge.
- **Tempo is the frame.** Scene: every moment told. Summary: ground covered,
  time passing between beats, one sentence holding an hour. Pause: time stops
  on one image. Say which one a paragraph is in; most flat prose is scene
  tempo used for things that deserved summary.

## The three punches

A punch is a short last line that pays. Pick one; never stack them.

1. **Land**: the consequence, said plainly, in few words. The default when
   something is owed and the beat is consequential.
2. **Refrain**: a line already told comes back word for word or nearly, so
   the reader completes it before it ends. Repetition is the emphasis; the
   sense has shifted since the first telling. Only after the line has been
   planted at least twice.
3. **Release**: what changed, in under eight words, and stop. For a long
   stretch where little was owed: it gets the reader out of reading a lot for
   little payoff. Prefer this to manufacturing a landing.

## The withheld word

Three em dashes (———) withhold a word: "Mr. ———", the name on the letter,
what someone cannot say. It is the gap the reader fills and fills wrong,
the grand pause of the piece, the machine's own tic made into its longest
silence. Use it once, only for a thing the piece still holds open and will
pay later, and only after the reader has reached for that thing more than
once; never for a thing you will not answer at all.

## Accents: the swear and the dash

Two smaller units, neither a cadenza.

- **The swear** is a sforzando: one hit on the line that lands. It is
  earned only by a shock the reader just felt (a person turning on them, a
  try that failed with much at stake), goes in the mouth of the person the
  shock belongs to, and is followed by a long silence of swearing. It jars
  when nothing was owed, when the voice has not earned it, when the setting
  would not say it, or when it comes twice in a stretch. Never explain it.
- **The dash** is a rest, the one mark that is a silence. Its meta meaning
  first: the dash is the mark of machine prose, the joiner of two clauses
  that should have been two sentences, and every droning paragraph carries
  it. Redeemed, it is spacing, not joining: at most one in a paragraph,
  only where a sentence breaks off before the thing arrives, or at a pause.
  Everywhere else, no dash.

## The stress position

Whatever the density, the last sentence of a paragraph is where the most
changes. End on what is different now, never on the setting, the weather, or
a view. A dense sentence placed on a low-stakes final beat is the single most
common thing that makes good prose hard to parse: readers weight the end of
the paragraph, so put the weight there.

## Forms and transitions

Organise return like a song, not a list. Four forms cover most prose:

| Situation | Form | Shape |
|-----------|------|-------|
| Confrontation, boss fight, argument | The musical sentence | State; restate from a step closer; fragment and accelerate, plant nothing new; cadence that lands |
| Exploration, travel, investigation | Rondo | A refrain between episodes; each return pays a little; the contrast makes the return feel like home |
| Revelation, the turn of a story | Recapitulation | Earlier themes return at home; closure held to the last line |
| Reflection, aftermath | Villanelle | A verbatim refrain whose sense shifts each time it comes back |

Transitions matter more than the forms. Hold a form while the scene is
engaged (a fight changes the pacing anyway). Leave a form early through one
bridge paragraph: all momentum, no new fact. Let the cadence of one form open
the next.

## Keep the ledger on paper

A prompt alone forgets the balance by the third paragraph (Eli, 2026-11-02:
"I'm not sure how effective just a prompt will be without the ledger"). So
write the ledger down and keep it beside the draft. Before each paragraph,
one line:

```
¶7  owed: the letter (raised ¶2), who locked the door (¶4)   due now: the letter
    debt: 310 words since ¶4 paid    feeling: dread, low
    → scene · staccato · restate · plain · no punch
```

Mark the draft as you go, in brackets the final pass strips:

- `[raise: the letter]` on a sentence that opens a promise.
- `[pay: the letter]` on the sentence that pays it.
- `[plant: "the boards creak under nothing"]` on a line meant to return.

`python3 scripts/meaning_ledger.py < draft.txt` (this skill's `scripts/`) reads the marks and reports,
per paragraph, the debt (words since the last payment), what is still owed,
what was raised and never paid, any refrain planted fewer than twice before
it returned, and any paragraph written while something was due whose last
sentence pays nothing (the stress position spent on a quiet line). It is arithmetic over your own
marks, not a judgement; the judgement is yours when you mark.

## Workflow

1. Name the reader's balance before the passage, on paper (above): what has
   been promised and not paid; what is due now; the feeling the previous
   passage left.
2. Choose tempo, rhythm, form role, and whether this paragraph punches, and
   which punch. Write those four words down before drafting.
3. Draft. Keep the surface clear enough that a first reader is never lost.
   One meaning per sentence where nothing is owed; two or three details that
   are also signs where something is being raised.
4. Check the stress position: is the last sentence the one where the most
   changes? If not, move or cut until it is.
5. Check density against the ledger: every dense sentence names what it
   raises; every punch names what it pays. Remove what names nothing.
6. With the Poet tool available: ask what else the dense sentences can mean,
   close the readings you did not mean, keep the one you did. Without it: list
   the readings yourself and close them by hand.

## Do not

- Do not write every paragraph at the same density. Plain is a band, not a
  failure.
- Do not point at a planted meaning. If the reader must be told it is there,
  it is not planted.
- Do not end on atmosphere. Do not end dense on a beat that owes nothing.
- Do not change rhythm mid-scene or refrain a line that was told once.

## Sources

Grown out of [Effect Co](https://effectco.game)'s writing tools: the Poet (meaning layering, the
ledger of readings) and the pacing engine of its narrative kernel
(2026-11-02), where every rule here is enforced by a kernel rather than
asked of a prompt. Without that kernel, the paper ledger is the substitute.
