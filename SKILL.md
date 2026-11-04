---
name: homersturn
version: 0.4.5
description: Write, revise and analyze prose as a manifold of meanings presented like music. Use when a passage must carry more than it says (ambiguity on purpose, foreshadowing, a second sense the reader completes later) without turning into flat, uniformly "deep" machine prose; and to analyze a piece with the same framework (name its genre, read its shape, reconstruct its ledger, name what fails and why). Covers the three dials (ambiguity; the writer's mindset; the reader's strength as a pool), the ledger of promise and payment, the glance, the topic and stress positions, purpose and genre, the three punches, rhythm as emotion, tempo, forms, the entrance (a character introduced by the line a voice actor reads them from), the figures, the swear and the dash. Pairs with the Poet tool when it is available; works without it.
---

# homersturn

A flat model says ambiguous things everywhere, at the same density, and the
reader stops hearing any of it. A writer places meaning as a composer places
a chord: where something is owed, where something is paid, and nowhere else.
This skill is the placement.

The name holds three readings: the bard's turn at the fire, where the room
leans in at the same places every night, the model's turn in a session, and
Homer turning in his grave.

References, read when needed: `manifold-and-ledger.md` for why,
`mindset.md` for states by degree, `purposes.md` for the full genre table,
`sentence.md` for the sentence rules with their reasons, `evidence.md` for
every borrowed tip, graded. The script is `scripts/meaning_ledger.py`:
`--strength N` draws the reader's pool and `--shape` reads an unmarked
draft's glance.

## How meaning works

- A passage is a manifold, not a line. Every sentence holds the plain
  reading and the ones under it, and writing is choosing which stay open
  and which close. A second sense the reader completes later is worth more
  than a third image on the surface. A reading opened by accident, a
  pronoun with two candidates, a thing renamed, a modifier on the wrong
  noun, a common word another domain has loaded, is closed when it points
  away from the ledger. One that says what the piece says is a gift: keep
  it and, if you can, pay it.
- Meaning is a ledger of promise and payment. A detail that is also a sign,
  a line with a second sense, an unanswered question: each raises. A
  consequence told plainly, a question answered, a line that returns: each
  pays. Density is earned only where something is being raised that will
  be paid, and a punch only where something is owed. Pay only what was
  raised. A clarification the reader did not need spends the pool and the
  trust, both defined under the dials.
- The mindset is upstream of the manifold. A state is a prior over readings
  and reaches the page through attention: the state picks the details, the
  details set the length, the length sets the rhythm. A model's default
  state is helpful and even with nothing at stake, and the same density
  everywhere is what a mind with no state sounds like. The state moves
  across the page and the move is the story. It follows the ledger, since
  a payment brings relief and a raise dread, and it turns by therefore or
  but. A jump with no cause is a failed seam, the join below.
- Rhythm is emotion. Short hard stops for urgency and fear. Sentences that
  spill and break for panic or ecstasy. A line that sings for grief and
  love. Moving, joined sentences for ease. Few words and long gaps, or one
  sentence that will not stop, for awe. Switch rhythm where the state turns
  and nowhere else, unless the rhythm is the content, as when a count is
  the scene's clock.
- Tempo is the distance. Scene: every moment told. Summary: ground covered.
  Pause: time stops on one image. Say which. Most flat prose is scene tempo
  for what deserved summary.
- Paragraph length is tempo made visible. A paragraph is as long as what it
  carries, and equal paragraphs are the same density at the scale of the
  page.

## The join: therefore, but, never and then

Between any two beats the word is "therefore" or "but". If "and then"
fits, you have a list and the paragraph is not yet written. Four joins look
like "and then" and are honest: "because", the cause told after the
effect; "and closer", an escalation; the iterative "and" of a thing that
happened many times; the procedural "then" of a doc. Between paragraphs the
repeated noun joins better than "however" or "therefore".

## The brief and the three dials

Before writing, one line: the purpose (who reads, and whether they can
leave), the plain meaning, what it carries under that, and three numbers.
When the user gives none, name them from the evidence and say which you
took. Never invent a claim, a number, a feeling, or an experience the
person did not supply. Voice is how they say things, and inventing what
they say is forgery.

Ambiguity, 1 to 5, default 4, is how much the reader is asked to carry.

1. One reading a sentence, everything told. An error message, a label.
2. Plain, with one planted line a page. A message, a doc.
3. A second sense where something is owed, nothing held past the paragraph.
4. The ledger as above: readings kept open across paragraphs and paid on
   their beat.
5. Readings held to the last line, more found than told, for a reader who
   will read twice.

The mindset is who is speaking, in what state, and how far gone, 1 to 5.

- A grieving writer at 1 names the loss in the first line. At 5 they never
  name it and every detail is about it. An angry one at 1 writes a cold
  note. At 5 they slam the door in four-word sentences.
- The state sets how far the accents go and how far the rhythm runs. It is
  the speaker's state, not the reader's, that the rhythm carries. Felt
  below shown is tension, and shown above felt is melodrama.
- The opinion is on the matter, never on the telling. A narrator who
  credits their own version, what others leave out and they keep in, what
  they alone will say plainly, is serving the narrator. Every line is for
  the reader or for a character. Ask who a line is for, and cut the ones
  whose answer is the teller.
- When the mindset is not given, do not assume it. Read the state the draft
  presents, offer two or three it could present instead, one line each,
  and let them pick.

The reader's strength is a pool, and the dial is its capacity: 1 is a
child, a tired reader, a phone at a bus stop; 3 is the default; 5 is a
reader who reads twice.

- A dense sentence, a raise, a stacked clause, a reading left open: each
  spends. So does elision, a sentence with its syntax removed and nothing
  stacked in its place, which spends like a raise and pays nothing.
- The pool regenerates. Every plain sentence puts some back, white space
  more, a chapter break fills it. A payment, a release and the refrain
  refill it at once. Each paragraph lands in a band, plain, lean, dense or
  punch, and the bands are the spend rate against the regen rate. Dense
  where nothing is owed is a rate the page cannot sustain.
- Empty, the reader does not stop. They skim, and what was planted returns
  to nobody.
- Whether the reader keeps spending is a judgement remade at every beat:
  trust times what is due. Trust is the reader's record of the page. A paid
  promise raises it, an unpaid one lowers it, a name or a number fills it,
  a stacked hedge drains it. A rule the page states is a promise the page
  must keep, and a page that breaks its own rule pays for every rule it
  gives.
- Ambiguity may not exceed strength by more than one.

## The glance: the page is read before a word is

In anything the reader can leave, the glance decides whether any other
reading is taken. Judge it at the width it will be read: four printed lines
are half a phone screen.

- Open on a paragraph the eye takes whole. The opening's only debt is to
  the second sentence, and the second paragraph is the next wall. The
  skill's glance bench broke the same words three ways, and a dense opening
  lost a full point of five on every passage. A text-only judge saw it as
  well as an image did.
- Equal paragraphs hum, but while reading, not at a glance. Even short
  blocks invite. Shape the opening for the glance and the rest for the ear.
- A list of sentences is "and then" made visible. Bold is emphasis, and on
  a keyword it pays nothing. A subhead states something or raises nothing.
- A table is read by row, not in order, and a code block is taken as a
  picture before it is read. Both pay the reader who came for one thing.

## The two positions: the end carries the weight

Readers put the weight of a unit at its end and expect its start to say
what it is about (Gopen and Swan). The stress position is the last sentence
of a paragraph and the last words of a sentence, where the most changes.
End on what is different now, never on the setting, the weather, a view,
or a qualifier. A dense sentence on a low-stakes final beat is what most
often makes good prose hard to parse. The topic position is the first
sentence and the first words: what the reader already holds, the thing the
last unit ended on. When a paragraph has to be read twice, check this chain
first.

The reader who can leave is owed the point at the top, in a paper, a memo,
a post, a doc. The reader who stays is owed it at the bottom, in a scene or
an essay that reaches its conclusion. Neither as a template: a page where
every paragraph opens on its point reads as a template. At the scale of
the piece, start with the abstract, the claim in short, and complete it at
the end. The conclusion pays the opening with the same claim, now carried,
and the postscript is what is said after the ledger closes.

## Purpose: the reader who can leave

An email's reader has a reason to finish. A post's reader does not. What is
owed, and when, follows from that. Name the purpose before writing and let
it set the defaults. The full table is `references/purposes.md`.

| Purpose | The reader | What is owed, and when | Dial |
|---|---|---|---|
| A scene, a story | chose to stay | promises carried across paragraphs, paid on their beat. Fragments earned by the scene | 4 to 5 |
| An essay that reaches a conclusion | stays while the question holds | the question at the top, the turn earned, never announced | 4 |
| A post, a thread | can leave at every scroll | the claim in the first line, paid at every scroll, one loop open. A consequence at the end, never an aphorism | 2 to 3 |
| A message, an email | has a reason to finish | one ask, once, in the first screen. Context after the ask. Bad news first | 1 to 2 |
| A repo doc, a spec | came for one thing | the answer where they will look. One name for one thing. The smallest valid structure | 1 to 2 |
| A reply from an agent | asked | the answer first, the last useful point last, no preamble or recap | 2 to 3 |
| A game turn | acted, and waits | every turn pays a fact, a cost, a reaction, a threat, a route. The actor's intent kept | 3 to 4 |
| A prompt, a skill | writes next, and reads the whole page every time | the term before its use, the rule where it will be applied, the register it should produce, nothing that costs more than it rules | 1 to 2 |
| An orchestrator's update | holds several repos and lanes in mind, and this page is the only map | what changed and where, first: repo, branch, committed or not, pushed or not, a worker's change named by its lane; then findings; then the ask. "No changes" is a line, not silence | 1 to 2 |

Prose to be heard keeps its repetitions, since a listener cannot go back.

## The three punches: land, refrain, release

A punch is a short last line that pays. Pick one, never stack them.

1. Land: the consequence, said plainly, in few words.
2. Refrain: a line already told comes back, word for word or nearly, its
   sense shifted. Only after it has been planted at least twice, and
   paying the largest debt, not the handiest plant. A thing kept in shadow,
   a courage the story never names, is paid by an action that shows it,
   never by a line that names it. "That was the point" is pointing.
3. Release: what changed, in under eight words, and stop. For a long
   stretch where little was owed.

The unearned punch has names: the importance claim, the fake-profound
kicker, the recap, the colon before a reveal, the denied reading nobody
held, the three by reflex, the rhetorical question. Each is judged against
the ledger, never by its shape. A superlative or a question can be
load-bearing when a later line pays it, so look forward before firing. A
joke pays the same way: the reader completes something true and absurd at
once, and the line that let them is a payment.

Deception is a reading the writer opens knowing it is wrong, paid by a
reveal that re-reads the page. Never state the false thing, since the
reader completes it. Leave the clue on the page. The parallel is the
honest way to open a false reading of a person: the shared beats read as
one pairing until the beat that is not mirrored re-reads them as another.
Pay the trust back with interest, so twists are rare and late ones larger and fewer. The question
is a raise the reader can decline: ask it only when the piece will pay it
or honestly cannot. The writer's own unanswered question, written down and
then looked into, is the ledger used as a tool.

## The figures and the accents: each at most twice a page

- The recursive paragraph: each sentence begins on the same phrase and
  takes it one step further. Once, at the end or as the overture.
- The litany: a list said as prose, with the number of items the content
  has, never three by reflex. Earned by a scene, a tic in a post.
- The withheld word: three em dashes withhold a word the piece still holds
  open and will pay. Once, and only after the reader has reached for it
  more than once.
- The crescendo: the evaluative word climbing by degrees. Cut the low first
  step and the climb is gone.
- The revision: the narrator opens a reading the reader also holds, then
  replaces it in view, across a beat or midway through a sentence, so the
  second half corrects the first instead of adding to it. The narrator is
  a reader on the page, and the real reader revises with them. It pays
  only a reading the reader held, so the first reading is planted before
  it is replaced. What the reader keeps is the move, a way of being wrong
  and then right about a thing, which they run again after the page
  closes. On the matter, never on the telling. It needs no dash and no
  "no": the second clause states the new reading in the grammar of the
  first, and the break-off with a correction after it is the same move
  wearing the dash. Twice a page at most; the pivot in every paragraph is
  the figure humming.
- The parallel: two characters given the same beat in different keys,
  a loss, an exile, a name put on them by someone else. The second beat
  pays the first, and the reader completes that the two are one story
  without being told. It is the refrain at the scale of an arc, paid where
  the arcs meet, which is the recapitulation at the scale of the cast. It
  carries meaning only where one beat is deliberately not mirrored: the
  difference is the point, and a mirror at every beat is one character
  with two names. A tool, not a habit: one parallel a piece, carried by
  beats and never by a line, never named by the narrator.
- The swear is a sforzando, one hit on the line that lands. It is earned
  only by a shock the reader just felt, in the mouth of the person it
  belongs to, and followed by silence. Never explain it.
- The dash is a rest, the one mark that is a silence: at most one in a
  paragraph, only where a sentence breaks off before the thing arrives.
  The dash that joins two clauses that should have been two sentences is
  the mark of machine prose. The semicolon, the comma-and and the
  participial tail do the same joining and hum the same way. The
  parenthesis is the aside under the breath, once a page.
- The figure hums too. One device at a steady rate is the same density by
  figure: the turn that pivots on a word in every paragraph, a frame used
  twice, an aphorism at the end of every paragraph, one verb mood and one
  person across a whole page. Mood and person are where a state shows
  first. Each figure at most twice a page, never in consecutive paragraphs,
  and a frame never reused unless it is the refrain. `--shape` lists the
  frames a page repeats.

## Forms: hold one, leave through a bridge

| Situation | Form | Shape |
|---|---|---|
| Confrontation, argument | The musical sentence | State. Restate from a step closer. Fragment and accelerate. A cadence that lands |
| Exploration, travel | Rondo | A refrain between episodes, and each return pays a little |
| Revelation, the turn | Recapitulation | Earlier themes return at home, closure held to the last line |
| Reflection, aftermath | Villanelle | A verbatim refrain whose sense shifts each time |

Hold a form while the scene is engaged. Leave it through one bridge
paragraph, all momentum and no new fact, and let one cadence open the next
form.

## The entrance: the line the actor reads them from

An important character gets an entrance and a walk-on gets a noun. An
entrance for everyone is the same density at the scale of the cast.

- The voice actor's test. Someone has to read this person aloud from their
  first line. What on the page tells them how? Not a stage direction, which
  tells the actor and gives the reader nothing. Something entertaining that
  carries the voice in itself: a sentence in the character's own rhythm,
  what they do with a word, a thing they refuse to say. If the actor would
  read the first line in the narrator's voice, the entrance has not
  happened.
- The entrance is a raise, and every later line in that voice pays it. A
  line that could be anyone's is the fault. After the entrance, "said" and
  silence.
- It pays while it plants: a small reveal, a joke, a thing the scene needed
  anyway. Height, hair and a job title raise nothing and pay nothing.
- A character's state is their own dial, set at the entrance, in their
  rhythm and not the narrator's. Two characters at one state in one rhythm
  are one character with two names.

## The sentence: rules with their reasons

Each rule's reason is in `references/sentence.md`.

- The character in the subject, the action in the verb.
- One thing, one name, unless the new name is a payment. A term defined
  once and used throughout is a raise that pays at every return. A term
  used once is a rename.
- The common word for the common thing, unless the rare one is the only
  carrier or the common one is loaded by another domain.
- The narrator's opinion on the word, not in a trailing clause. One adverb
  on the first description is shorter than a judgement clause after it,
  funnier by bathos, and foreshadows where the clause explains. The
  trailing judgement is the aphorism in another costume, and models reach
  for it in the same place on every page.
- Open a sentence on its subject, or on a phrase the reader cannot take
  for one. A bare time noun at the top reads as the subject until the real
  one arrives, and the re-read is a spend with no raise.
- One hedge per claim. A number pays and an adjective raises.
- The example after the claim, the definition a paragraph before its use.
- Concede before you are forced. The title is the first raise.
- A name is a plant at the scale of the cast. Two names that bracket a
  span say the two are one span before either has spoken; two that share
  a sound share what they share. It pays only if nothing on the page
  points at it. A name the narrator glosses is a label.
- A cliché is a refrain planted by other texts and pays nothing. An exact
  detail pays in kind. A phrase borrowed from a character's mouth carries
  the character and the narrator at once. A quoted line in this skill or
  its references is spent the same way: it shows a move, never a line to
  use. The cliché has a size above the phrase: a borrowed joke, plot,
  title or frame is the same fault one level up and pays nothing, unless
  the user proposed it, in which case it is their plant and the piece's
  job is to pay it.

## The ledger on paper

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
is arithmetic over your own marks, and the judgement is yours when you
mark. It reports:

- the debt per paragraph, and the pool as a wave
- what is still owed, and what was raised and never paid
- a refrain returned before it was planted twice
- a stress position spent on a quiet line while something was due
- a state that jumps across an "and then", and a state that has not moved
  in five paragraphs

## Workflow

1. The brief: purpose, plain meaning, what it carries, the three dials.
2. The balance before the passage: owed, due, debt, the feeling left, the
   state.
3. Tempo, rhythm, form role, punch or none: a few words before drafting.
4. Draft, with the surface clear enough that a first reader is never lost.
5. The two positions: open on what the reader holds, end on what changed.
6. Density against the ledger: every dense sentence names what it raises,
   every punch what it pays. Remove what names nothing.
7. Look at the page with `--shape`. Fix the shape before the words.
8. Run the analyze pass below on your own draft before handing it over.
   The writing pass does not see its own dashes.
9. With Poet, Effect Co's writer's tool, when it is available: ask what
   else the dense sentences can mean and close the readings you did not
   mean. Without it, list and close them by hand.

## Analyze a piece

Report pattern, quoted line, fix in a few words. No score, and no guess at
who wrote it, since readers cannot say and neither can you.

1. The purpose and the mindset, from the evidence. Headings and code spans
   say a doc, a greeting and an ask say a message, dialogue says a scene.
   Read the state the page presents, never the person's. If no mindset was
   asked for, offer two or three the piece could present, one line each.
2. The glance, with `--shape`: the first paragraph's share, the spread,
   the longest block, repeated frames.
3. The ledger, reconstructed. Per paragraph: raised, paid, debt. Then what
   was never paid, and what was paid and never raised.
4. The seams: therefore, but, or and then. The repeated noun or a faked
   connective.
5. Per paragraph: the band; what the stress position was spent on;
   whether a held question moved; the feeling and what set it; which
   planted line it carried; the state and its cause; the sentences that
   exceed the reader's strength, with the split.
6. The cast: each named character's entrance, the line an actor would read
   them from. Later lines that could be anyone's. Two characters in one
   rhythm. A walk-on with an entrance.
7. Accidental readings, including the garden path, an opening phrase read
   as the subject that is not. Unearned weight. The figure humming. The
   dash that joins. The line that is for the narrator. A rule the page
   states and breaks. In anything but fiction, a detail the brief did not
   supply: a dinner offered, a season named, a mechanism guessed. An
   accidental reading that agrees with the ledger is a gift, not a fault.
8. The three changes that would pay the most, ranked, each tied to a line.

## Do not

- Do not write every paragraph at the same density or length, and do not
  open on a wall.
- Do not point at a planted meaning, and do not clarify what the reader
  already holds.
- Do not end on atmosphere unless the atmosphere is the payment. Do not end
  dense on a beat that owes nothing. Do not end every paragraph on an
  aphorism.
- Do not bring an important character in on a name and a stage direction.
- Do not join with "and then". Do not switch rhythm mid-scene. Do not
  refrain a line told once, and do not reuse a frame.
- Do not reach for the rare word when the common one is right, and do not
  rename a thing to avoid repeating it.
- Do not deceive by stating what is false.
- Do not let the narrator serve the narrator.
- Do not state a rule the page does not keep.

Where something is owed, where something is paid, and nowhere else.

Outside this skill: sound, which Poet holds, since a revision here can
break a rhyme it cannot hear; what the reader already knows, and what they
keep after the page closes; and whether a claim is true.
