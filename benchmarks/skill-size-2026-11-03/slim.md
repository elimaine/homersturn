---
name: homersturn
version: 0.2.1-slim
description: Write, revise and analyze prose as a manifold of meanings presented like music. Use when a passage must carry more than it says (ambiguity on purpose, foreshadowing, a second sense the reader completes later) without turning into flat, uniformly "deep" machine prose; and to analyze a piece with the same framework (name its genre, read its shape, reconstruct its ledger, name what fails and why). Covers the three dials (ambiguity; the writer's mindset; the reader's strength as a pool), the ledger of promise and payment, the glance, the topic and stress positions, purpose and genre, the three punches, rhythm as emotion, tempo, forms, the figures, the swear and the dash. Pairs with the Poet tool when it is available; works without it.
---

# homersturn

Ambiguity is the most powerful tool in good writing and the most abused one in
machine writing. A flat model says ambiguous things everywhere, at the same
density, and the reader stops hearing any of it. A writer places meaning the
way a composer places a chord: where something is owed, where something is
paid, and nowhere else. This skill is the placement. The name holds three
readings and keeps all of them: the bard's turn at the fire, the same story
every night told so the room leans in at the same places; the model's turn in
a session, where this gets applied; and Homer turning in his grave at what the
machines did with his trade before this. The last one is the one to earn your
way out of.

References, read when needed: `manifold-and-ledger.md` (why), `mindset.md`
(states by degree), `purposes.md` (the full genre table), `sentence.md` (the
sentence rules), `evidence.md` (every borrowed tip, graded). The script is
`scripts/meaning_ledger.py` (`--strength N` draws the reader's pool, `--shape`
reads an unmarked draft's glance).

## The brief and the three dials

Before writing, one line: the purpose (who reads, and whether they can
leave), the plain meaning, what it carries under that, and three numbers.
When the user gives none, name them from the evidence and say which you took.

- **Ambiguity, 1 to 5, default 4**: how much the reader is asked to carry. 1
  is one reading a sentence and everything told (an error message, a label);
  2 is plain with one planted line a page (a message, a doc); 3 a second
  sense where something is owed, nothing held past the paragraph; 4 the
  ledger as written here, readings kept open across paragraphs and paid on
  their beat; 5 readings held to the last line, more found than told, for a
  reader who will read twice.
- **The mindset**: who is speaking, in what state, and how far gone, 1 to 5.
  A grieving writer at 1 names the loss in the first line; at 5 never names
  it and every detail is about it. An angry one at 1 writes a cold note; at
  5 slams the door in four-word sentences. The state sets how far the
  accents go and how far the rhythm runs; it is the speaker's, not the
  reader's, which rhythm carries. Felt below shown is tension; shown above
  felt is melodrama. When the mindset is not given, do not assume it: read
  the state the draft presents and offer two or three it could present
  instead, one line each, and let them pick.
- **The reader's strength**: a pool, with the dial as its capacity (1 a
  child, a tired reader, a phone at a bus stop; 3 the default; 5 a reader
  who reads twice). A dense sentence, a raise, a stacked clause, a reading
  left open: each spends. Mana regenerates: every plain sentence puts some
  back, white space more, a chapter break fills it; a payment, a release and
  the refrain refill at once. Empty, the reader does not stop, they skim, and
  what was planted returns to nobody. So pace a spend rate against the regen
  rate; "dense where nothing is owed" is a rate the page cannot sustain.
  Whether the reader keeps spending is a judgement remade at every beat,
  trust times what is due: paid promises raise trust, unpaid ones lower it, a
  name or a number fills it, a stacked hedge drains it. Ambiguity may not
  exceed strength by more than one.

## The model

- **A passage is a manifold, not a line.** Every sentence holds the plain
  reading and the ones under it. Writing is choosing which stay open and
  which close. A second sense the reader completes later is worth more than
  a third image on the surface. A reading opened by accident (a pronoun with
  two candidates, a thing renamed, a modifier on the wrong noun, a common
  word another domain has loaded) is closed.
- **Meaning is a ledger of promise and payment.** A detail that is also a
  sign, a line with a second sense, an unanswered question: each raises. A
  consequence told plainly, a question answered, a line that returns: each
  pays. Density is earned only where something is being raised that will be
  paid; a punch only where something is owed. Pay only what was raised: a
  clarification the reader did not need spends the pool and the trust.
- **The mindset is upstream of the manifold.** A state is a prior over
  readings and reaches the page through attention: the state picks the
  details, the details set the length, the length sets the rhythm. A model's
  default state is helpful and even with nothing at stake, and uniform
  density is what a mind with no state sounds like. The state moves across
  the page and the move is the story: it follows the ledger (a payment
  brings relief, a raise dread), it turns by therefore or but, and a jump
  with no cause is the seam failure in another costume.
- **Rhythm is emotion.** Short hard stops for urgency and fear; sentences
  that spill and break for panic or ecstasy; a line that sings for grief
  and love; moving, joined sentences for ease; few words and long gaps, or
  one sentence that will not stop, for awe. Switch rhythm where the state
  turns and nowhere else, unless the rhythm is the content (a count that is
  the scene's clock).
- **Tempo is the frame.** Scene: every moment told. Summary: ground covered.
  Pause: time stops on one image. Say which; most flat prose is scene tempo
  for what deserved summary.
- **Paragraph length is tempo made visible.** A paragraph is as long as what
  it carries. Equal paragraphs are the hum at the scale of the page.

## The glance

Before a word is read, the page is read, and in anything the reader can
leave the glance decides whether any other reading is taken. Judge it at the
width it will be read: four printed lines are half a phone screen.

- **A dense opening shuts the reader down.** Open on a paragraph the eye
  takes whole; the opening's only debt is to the second sentence. The second
  paragraph is the next wall. (The skill's glance bench: the same words
  broken three ways; a dense opening lost a full point of five on every
  passage, and a text-only judge saw it as well as an image did.)
- **Equal paragraphs hum**, but while reading, not at a glance: even short
  blocks invite. Shape the opening for the glance and the rest for the ear.
- **A list of sentences is "and then" made visible.** Bold is a punch; on a
  keyword it pays nothing. A subhead states something or raises nothing.

## The two positions

Readers put the weight of a unit at its end and expect its start to say what
it is about (Gopen and Swan). The **stress position** is the last sentence
of a paragraph, the last words of a sentence: where the most changes. End on
what is different now, never on the setting, the weather, a view, or a
qualifier; a dense sentence on a low-stakes final beat is the commonest
thing that makes good prose hard to parse. The **topic position** is the
first sentence, the first words: what the reader already holds, the thing
the last unit ended on. When a paragraph has to be read twice, check this
chain first.

The reader who can leave is owed the point at the top (a paper, a memo, a
post, a doc); the reader who stays is owed it at the bottom (a scene, an
essay that reaches its conclusion). Never both as a template: a page where
every paragraph opens on its topic sentence is a tell. At the scale of the
piece: start with the abstract and complete it at the end; the conclusion
pays the opening with the same claim, now carried, and the postscript is
what is said after the ledger closes, outside the frame.

## The join: therefore, but, never and then

Between any two beats the word is "therefore" or "but"; if "and then" fits,
you have a list and the paragraph is not yet written. Four joins wear its
clothes and are honest: "because" (the cause told after the effect), "and
closer" (an escalation), the iterative "and" of a thing that happened many
times, and the procedural "then" of a doc. Between paragraphs the repeated
noun joins better than "however" or "therefore", and never lies.

## Purpose: the reader who can leave

An email's reader has a reason to finish; a post's reader does not. What is
owed, and when, follows from that. Name the purpose before writing and let it
set the defaults; the full table is `references/purposes.md`.

| Purpose | The reader | What is owed, and when | Dial |
|---|---|---|---|
| A scene, a story | chose to stay | promises carried across paragraphs, paid on their beat; fragments earned by the scene | 4 to 5 |
| An essay that reaches a conclusion | stays while the question holds | the question at the top, the turn earned, never announced | 4 |
| A post, a thread | can leave at every scroll | the claim in the first line, paid at every scroll, one loop open; a consequence at the end, never an aphorism | 2 to 3 |
| A message, an email | has a reason to finish | one ask, once, in the first screen; context after the ask; bad news first | 1 to 2 |
| A repo doc, a spec | came for one thing | the answer where they will look; one name for one thing; the smallest valid structure | 1 to 2 |
| A reply from an agent | asked | the answer first, the last useful point last, no preamble or recap | 2 to 3 |
| A game turn | acted, and waits | every turn pays a fact, a cost, a reaction, a threat, a route; the actor's intent kept | 3 to 4 |

Withholding the reveal is for readers who stay; the leaving reader gets the
claim first. Prose to be heard keeps its repetitions, since a listener cannot
go back.

## The three punches

A punch is a short last line that pays. Pick one; never stack them.

1. **Land**: the consequence, said plainly, in few words.
2. **Refrain**: a line already told comes back, word for word or nearly, its
   sense shifted; only after it has been planted at least twice.
3. **Release**: what changed, in under eight words, and stop; for a long
   stretch where little was owed.

The unearned punch has names: the importance claim, the fake-profound
kicker, the recap, the colon before a reveal, the denied reading nobody held,
the three by reflex, the rhetorical question. Each is judged against the
ledger, never by its shape: a superlative or a question can be load-bearing
when a later line pays it. Look forward before firing.

**Deception** is a reading the writer opens knowing it is wrong, paid by a
reveal that re-reads the page. Never state the false thing (the reader
completes it); leave the clue on the page; pay the trust back with
interest, so twists are rare and late ones larger and fewer. **The
question** is a raise the reader can decline: ask it only when the piece will
pay it or honestly cannot. The writer's own unanswered question, written
down and then looked into, is the ledger used as a tool.

## The figures and the accents

- **The recursive paragraph**: each sentence begins on the same phrase and
  takes it one step further. Once, at the end or as the overture.
- **The litany**: a list said as prose, the number of items the content has,
  never three by reflex; earned by a scene, a tic in a post.
- **The withheld word**: three em dashes withhold a word the piece still
  holds open and will pay; once, and only after the reader has reached for it
  more than once.
- **The crescendo**: the evaluative word climbing by degrees; cut the low
  first step and the climb is gone.
- **The swear** is a sforzando: one hit on the line that lands, earned only
  by a shock the reader just felt, in the mouth of the person it belongs to,
  followed by silence. Never explain it.
- **The dash** is a rest, the one mark that is a silence: at most one in a
  paragraph, only where a sentence breaks off before the thing arrives. The
  dash that joins two clauses that should have been two sentences is the mark
  of machine prose, and the semicolon, the comma-and and the participial tail
  are the same mark in other clothes. The parenthesis is the aside under the
  breath, once a page.
- **The figure hums too.** One device at a steady rate (the turn that pivots
  on a word in every paragraph, a frame used twice, an aphorism at the end of
  every paragraph) is uniform density by figure. Each figure at most twice a
  page, never in consecutive paragraphs; a frame never reused unless it is
  the refrain. `--shape` lists the frames a page repeats.

## Forms and transitions

| Situation | Form | Shape |
|---|---|---|
| Confrontation, argument | The musical sentence | State; restate from a step closer; fragment and accelerate; cadence that lands |
| Exploration, travel | Rondo | A refrain between episodes; each return pays a little |
| Revelation, the turn | Recapitulation | Earlier themes return at home; closure held to the last line |
| Reflection, aftermath | Villanelle | A verbatim refrain whose sense shifts each time |

Hold a form while the scene is engaged; leave it through one bridge
paragraph, all momentum and no new fact; let one cadence open the next form.

## The sentence

The rules other guides give as taste, kept because the model explains them
(`references/sentence.md` has each with its account): the character in the
subject and the action in the verb; one thing, one name, unless the new name
is a payment; the common word for the common thing, unless the rare one is
the only carrier or the common one is loaded by another domain; one hedge per
claim; a number pays, an adjective raises; the example after the claim, the
definition a paragraph before its use; concede before you are forced; the
title is the first raise; a cliché is a refrain planted by other texts and
pays nothing, while an exact detail pays in kind; a borrowed phrase carries
the character and the narrator at once.

## Keep the ledger on paper

A prompt alone forgets the balance by the third paragraph, so write it down
beside the draft. Before each paragraph, one line:

```
¶7  owed: the letter (¶2), who locked the door (¶4)   due now: the letter
    debt: 310 words since ¶4 paid   feeling: dread, low   state: fear 3 → 4, because ¶6 opened the door
    → scene · staccato · restate · plain · no punch
```

Mark the draft in brackets the final pass strips: `[raise: x]`, `[pay: x]`
(`[pay: inferred]` when the reader's own knowledge pays it), `[plant:
"line"]`, `[join: therefore|but|and then]`, `[state: fear 4]`. The script
reports the debt, the pool as a wave, what is still owed, what was raised and
never paid, a refrain returned before it was planted twice, a stress position
spent on a quiet line while something was due, a state that jumps across an
"and then", and a state that has not moved in five paragraphs. It is
arithmetic over your own marks; the judgement is yours when you mark.

## Workflow

1. The brief: purpose, plain meaning, what it carries, the three dials.
2. The balance before the passage: owed, due, debt, the feeling left, the
   state.
3. Tempo, rhythm, form role, punch or none: four words before drafting.
4. Draft, with the surface clear enough that a first reader is never lost.
5. The two positions: open on what the reader holds, end on what changed.
6. Density against the ledger: every dense sentence names what it raises,
   every punch what it pays; remove what names nothing.
7. Look at the page: run `--shape`. Fix the shape before the words.
8. Run the analyze pass below on your own draft before handing it over; the
   writing pass does not see its own dashes.
9. With Poet: ask what else the dense sentences can mean and close the
   readings you did not mean. Without it, list and close them by hand.

## Analyze a piece

Report pattern, quoted line, fix in a few words. No score, no guess at who
wrote it; readers cannot tell and neither can you.

1. The purpose and the mindset, from the evidence (headings and code spans
   say a doc, a greeting and an ask a message, dialogue a scene). Read the
   state the page presents, never the person's; if no mindset was asked for,
   offer two or three the piece could present, one line each.
2. The glance (`--shape`): the first paragraph's share, the spread, the
   longest block, repeated frames.
3. The ledger, reconstructed: per paragraph, raised, paid, debt; never paid;
   paid and never raised.
4. The seams: therefore, but, or and then; the repeated noun or a faked
   connective.
5. Per paragraph: the band (plain, lean, dense, punch); what the stress
   position was spent on; whether a held question moved; the feeling and
   how keyed; which planted line it carried; the state and its cause; the
   sentences that exceed the reader's strength, with the split.
6. Accidental readings, unearned weight, the figure humming, the dash that
   joins.
7. The three changes that would pay the most, ranked, each tied to a line.

## Do not

- Do not write every paragraph at the same density or length. Do not open on
  a wall.
- Do not point at a planted meaning. Do not clarify what the reader already
  holds.
- Do not end on atmosphere unless the atmosphere is the payment; do not end
  dense on a beat that owes nothing; do not end every paragraph on an
  aphorism.
- Do not join with "and then"; do not switch rhythm mid-scene; do not
  refrain a line told once; do not reuse a frame.
- Do not reach for the rare word when the common one is right, and do not
  rename a thing to avoid repeating it.
- Do not withhold from a reader who can leave, and do not front-load a
  reader who stayed for the turn.
- Do not deceive by stating what is false.
- Do not invent a claim, a number, a feeling, or an experience the person
  did not supply.

Outside this skill: sound (alliteration, rhyme, the stress cluster; a
revision here can break a rhyme it cannot hear; Poet holds it), the reader's
time and knowledge, and whether a claim is true.
