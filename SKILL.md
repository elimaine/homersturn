---
name: homersturn
version: 0.2.1
description: Write, revise and analyze prose as a manifold of meanings presented like music. Use when a passage must carry more than it says (ambiguity on purpose, foreshadowing, a second sense the reader completes later) without turning into flat, uniformly "deep" machine prose; and to analyze a piece with the same framework (name its genre, read its shape, reconstruct its ledger, name what fails and why). Covers the three dials (ambiguity 1 to 5, default 4; the writer's mindset and how far gone; the reader's strength, which caps density), the ledger of promise and payment, the glance (what a page says before a word is read), the topic and stress positions, purpose and genre, the three punches (land, refrain, release), rhythm as emotion, tempo, forms with transitions, the figures (recursive paragraph, litany, withheld word), the swear as an accent, and the dash redeemed as a rest. Pairs with the Poet tool when it is available; works without it.
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
or when the user asks why a passage feels dense, flat, or hard to parse.
`references/evidence.md` holds the tips taken from other writing guides, each
with its source, what the model makes of it, and how good the evidence is;
read it when a rule here is questioned. The ledger script is
`scripts/meaning_ledger.py`; the paper ledger below says when to run it, and
`--shape` runs on an unmarked draft.

## Before writing: the brief and the dial

Ask for, or take from the request, three things: what kind of writing this is
(the purpose, below), what it says plainly, and what it should carry under
that (the implied meanings, the vibe). Write them down in a line. When the
user gives none, name the purpose from the evidence (see Analyze) and say
which you took.

**Ambiguity is a dial, 1 to 5, default 4.** It sets how much the reader is
asked to carry, never where meaning goes.

1. One reading per sentence, everything told. An error message, a label.
2. Plain, with one planted line on a page. A message, a doc.
3. A second sense where something is owed; nothing held past the paragraph.
4. The ledger as written here: readings kept open across paragraphs and paid
   on their beat; a withheld word allowed.
5. Readings held to the last line, more found than told. For a reader who
   chose to stay and will read twice.

The purpose sets the default; the user's number overrides it.

**The mindset is the second dial.** Say who is writing and in what state,
and how far gone, 1 to 5. A grieving writer at 1 names the loss in the
first line and the piece is about living with it; at 5 the loss is never
named and every detail on the page is about it. An angry one at 1 writes a
cold note; at 5 slams the door in four-word sentences. The mindset sets how
far the accents go (how hard the punch, whether the swear comes, what
stays unsaid) and how far the rhythm runs toward its extreme. It is not
the reader's feeling, which rhythm carries; it is the speaker's state,
which the voice follows. The two dials are independent: a calm writer can
write at ambiguity 5, a furious one at 1.

**The reader's strength is the third dial**, the mirror of the mindset:
the writer's state sets what can be said, the reader's strength what can
be carried. 1 to 5, default 3. At 1 (a child, a tired reader, a second
language, a phone at a bus stop): one clause a sentence, one idea a
paragraph, every second sense told, no loop open past the paragraph. At 3:
two clauses, one inference a sentence, two loops open. At 5 (a reader who
will read twice): a triple clause with the third left to infer, four loops
held, a debt that runs long. Strength is a pool, not a ceiling (Eli: "like a wave, or
a mana pool"). The dial is its capacity; the level is where the reader is
on the page, and the writer surfs it. A dense sentence, a raise, a clause
stacked on a clause, a reading left open: each spends. And mana
regenerates on its own: every plain sentence the reader takes without
effort puts some back, white space puts more back, and a chapter break
fills it. On top of the regen, a payment refills at once (the reader
leans in again), and so do a release and the refrain, which costs nothing
because the words are already theirs. So the writer paces a spend rate
against a regen rate: a page that spends below what plain prose returns
is sustainable for as long as you like, and a page that spends above it
drains however full it began. "Dense where nothing is owed" is not one
spend; it is a rate the page cannot sustain. An empty pool does not stop the reader; it
makes them skim: readings stop being carried, the manifold collapses to
the plain one, and the planted line that returns later returns to nobody.
That is the true failure of the dense sentence on a quiet beat: it spends
the pool where no refill is coming. Rhythm is a spending pattern
(staccato: small spends at the regen rate; chaos: spent to zero on
purpose, which works only if the refill is the next line; stillness: pure
regen), and
the forms are wave shapes (the musical sentence spends down to the cadence
and the cadence refills; the rondo refills at each refrain;
recapitulation arrives with the pool full, since everything in it is
already paid for). The pool is what the reader can spend; whether they
spend it is a judgement, made again at every beat, on whether it is worth
expending more (Eli). That judgement is trust times what is due: every
raise is the writer's claim that a spend will pay, every payment made on
its beat raises the trust, and every promise left unpaid lowers it. Trust
is also filled by a name, a number, a source, and a grammar that holds,
and drained by a hedge stacked, a register that slips, and an absolute
claim; and the truth of a claim is outside this skill entirely, which
scores a false payment the same as a true one. So a
reader with a full pool and no trust leaves (the post's reader at the
second scroll), and a reader with an empty pool and full trust rests and
comes back (the chapter break). The glance is this judgement made first,
with no evidence but the shape. **Approachable is the pool read honestly**:
not plainer, but plain where nothing is owed, so the dense line lands on a
full pool. A page whose every paragraph ends on a second-sense line is
written for strength 5 and never refills; the brilliant bits are exactly
those lines, and keeping two of four makes the other two land. Ration the
aphorism: at most one a paragraph, never at the end of every paragraph,
and most paragraphs ending on the plain fact. **The figure hums too.** One
device at a steady rate is uniform density by figure, which no length
measure sees: the turn that pivots on a word ("not the taking, but the
thanking") in every paragraph, the same frame twice ("the way you know
your own name", "the way you think a thing you do not yet believe"), the
same pair twice ("took the grain and called it a tax", "took the medicine
and called it an order"). Each figure at most twice on a page, never in
consecutive paragraphs, and a frame never reused unless it is the refrain
and was planted as one. `--shape` lists the frames a page repeats. Ambiguity may not exceed strength by more
than one; past that the readings cannot be completed. Purpose sets the
capacity (a post's reader is at 2, a scene's chosen reader at 3 or 4) and
the user's number overrides it. The ledger script draws the wave
(`--strength`).

An example, Eli's, from a blind draft: "the winter grain to his own
stores, the children's portion halved, and when they had learned to live
on that, halved again" is strength 4: three clauses and an escalation to
infer. At 2: "He took the winter grain for his own stores and halved the
children's portion. When they had learned to live on that, he halved it
again."

**When the mindset is not given, do not assume it.** Read the draft for
the state it is in (the help mode, under Analyze), say what you see, and
offer two or three salient mindsets the piece could present, each as the
same line rewritten. The pick is the signal; never pick for them, and
never offer more than three.

## The model

- **A passage is a manifold, not a line.** Every sentence holds a cloud of
  readings a reader could take: the plain one and the ones that sit under it.
  Writing is choosing which readings stay open and which close. Before adding
  a layer, list the readings already present; a second sense a reader can
  complete later is worth more than a third image on the surface. A reading
  opened by accident (a pronoun with two candidates, a thing renamed, a
  modifier hanging off the wrong noun) is a manifold the writer did not
  choose; close it.
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
  and long gaps for awe and aftermath, or one sentence that will not stop,
  which is awe's other shape (Darwin's tangled bank). Do not switch rhythm
  inside an engaged scene; switch at its edge, which is where the state
  turns. Rhythm can also enact its subject rather than the reader's
  feeling: a count that is the scene's clock ("Forty-one. Forty-two."),
  a syntax bent to carry the claim; then the rhythm is the content and the
  rule about switching does not apply to it.
- **Tempo is the frame.** Scene: every moment told. Summary: ground covered,
  time passing between beats, one sentence holding an hour. Pause: time stops
  on one image. Say which one a paragraph is in; most flat prose is scene
  tempo used for things that deserved summary.
- **Paragraph length is tempo made visible.** A paragraph is as long as what
  it carries: a landing gets one line, a stretch of ground gets a long one.
  Equal paragraphs are the droning at the scale of the page, the same
  uniform density the ledger forbids within a paragraph.
- **The mindset is upstream of the manifold.** The ledger says where meaning
  goes, rhythm what the reader feels, purpose what is owed; the mindset says
  who is speaking and what they can see. A state is a prior over readings:
  it decides which second senses are open to the writer at all. A grieving
  writer cannot see a harbour as a harbour; a furious one sees one thing and
  nothing beside it. It reaches the page through attention: the state picks
  the details (the anxious notice the exits, the bereaved the empty chair),
  and the details set the length, and the length sets the rhythm. That is
  how a state is shown without being named. A model's default state is
  helpful, even, mildly pleased, with nothing at stake, and uniform density
  is what a mind with no state sounds like; setting one is the strongest
  single move out of machine prose. The long form is `references/mindset.md`.
- **The mindset moves, and the move is the story.** A fixed state is a
  setting; a shifting one is a trajectory the reader tracks like the ledger,
  and it follows the ledger: a promise paid brings relief, one raised brings
  dread, a reading closed brings calm, one opened against the writer's will
  brings fear. A state turns because of what was just paid, or against it
  (therefore, or but); a jump with no cause is the seam failure in another
  costume, and a state that never moves across a page is the hum in the
  voice. Felt and shown can cross mid-page: the cold note that cracks in its
  last paragraph is restraint failing, and that is a punch, because the
  reader carried the withheld anger as debt. Switch rhythm where the state
  turns, and nowhere else.

## The glance

Before a word is read, the page is read. The reader sees the shape and
decides whether to start, and in anything the reader can leave, the glance is
the reading that decides whether any other is taken. Look at the shape of the
page before the words, at the width it will be read: four printed lines are
half a phone screen.

- **A dense opening shuts the reader down.** A long first paragraph is
  density where nothing is yet owed, the ledger's failure at word one. Open
  on a paragraph the eye takes whole: one to three sentences. The opening's
  only debt is to the second sentence; write it last, and try deleting the
  first paragraph to see whether anything was lost.
- **Equal paragraphs hum.** A page of same-sized blocks reads as a machine
  before it is read at all. A one-line paragraph is emphasis, and it stops
  working at three on a page, except where the page's convention makes it
  nothing: dialogue turns, a list of steps. A convention the reader
  already holds carries no emphasis and costs none.
- **A list of sentences is "and then" made visible.** Items that flow into
  each other are a paragraph in a costume. Lists are for things that are
  really several; tables for what is compared by row and column.
- **Bold is a punch.** Spent on a keyword it pays nothing. A subhead is the
  ledger's visible column: it states something, so a reader who reads only
  subheads gets the argument; a label raises nothing.
- **The glance is not the read.** At a glance, even short blocks invite and
  one long block repels; the hum of equal paragraphs is heard while reading,
  not seen before it. So shape the opening for the glance and the rest for
  the ear. And the second paragraph is the next wall: a one-line opening
  followed by a block the eye cannot take is marked for the block.
- **The model has the sense when it looks.** The skill's glance bench
  (`benchmarks/glance-2026-11-03`): the same words broken three ways, judged
  by Opus from the text alone and from a blurred render, agreed on every
  passage. A dense opening lost by a full point of five in each of six
  passages, and the judge named it as the stall every time; a text-only
  judge saw it as well as the image did. Even blocks beat the shaped page
  at a glance by a third of a point (direction only). The human check is
  recorded beside the numbers.

`python3 scripts/meaning_ledger.py --shape < draft.txt` prints the shape:
each paragraph's words and sentences, the first paragraph's share, the
spread of lengths, the longest block, and the paragraphs that open on the
same words.

## The two positions: topic and stress

Readers put the weight of a unit at its end and expect its start to say what
the unit is about (Gopen and Swan). Two slots, at every scale.

- **The stress position** is the last sentence of a paragraph, the last
  words of a sentence. Whatever the density, it is where the most changes.
  End on what is different now, never on the setting, the weather, a view,
  or a qualifier. A dense sentence placed on a low-stakes final beat is the
  single most common thing that makes good prose hard to parse: readers
  weight the end, so put the weight there.
- **The topic position** is the first sentence of a paragraph, the first
  words of a sentence. It holds what the reader is already holding: the
  thing the last unit ended on, or the thing this unit is about. The
  known-new chain follows: each sentence opens on what the one before it
  paid. When a paragraph has to be read twice, check this first.
- **Where the point goes depends on who is reading.** The reader who can
  leave is owed the point at the top: a paper, a memo, a post, a doc. The
  reader who stays is owed it at the bottom: a scene, an essay that reaches
  its conclusion rather than transmitting one. Either way the end carries
  the change, and either way a page of paragraphs each opening on its
  topic sentence is a tell: open on the point when the reader needs it to
  stay, not as a template.
- **At the scale of the piece: the abstract, completed.** The rule a
  professor gives for a paper (Eli, 2026-11-03): start with the abstract
  and complete it at the end. The abstract is the first raise, a promise
  of what the piece will establish; the conclusion pays it with the same
  claim, now carried, so the reader completes the opening before the end
  arrives. That is the refrain at the scale of the piece, and Strunk's
  rule for the paragraph ("begin with a topic sentence; end it in
  conformity with the beginning") is the same shape one size down. The
  postscript is what is said after the ledger closes: outside the frame,
  one line, the only place an afterthought belongs. Do not put the point
  there.
- **Between paragraphs, the repeated noun.** End on a term and open the
  next paragraph with it. It is invisible and never lies about the
  relation, which "however" and "therefore" often do.

## The join: therefore, but, never and then

Parker and Stone's rule for the beats of a story: between any two beats
the word is "therefore" or "but". If "and then" fits, you have a list.
Every paragraph is caused by the one before it or turns against it. The
forms below say where a thing comes back; this says why the next thing
happens at all. Check it at the seam of every paragraph, and when "and
then" is the honest word, the paragraph is not yet written.

Four joins are honest and are not "and then", though they wear its
clothes: "because" (the cause told after the effect, a payment backwards);
"and closer" (each step the same thing nearer, an escalation); the
iterative "and" of a thing that happened many times (summary tempo, not a
list); and the procedural "then" of a doc or a recipe, where the order is
the point. A join is honest when it pays or advances the raise before it,
forward or back. Between paragraphs, the repeated noun does the joining
that "however" and "therefore" fake.

## Purpose: the reader who can leave

One asymmetry derives the genres: an email's reader has a reason to finish,
and a post's reader does not. What is owed, and when, follows from whether
the reader can leave. Each purpose is a genre the song must fit; name it
before writing and let it set the defaults.

| Purpose | The reader | What is owed, and when | The end | Dial |
|---|---|---|---|---|
| A scene, a story | chose to stay | promises carried across paragraphs, paid on their beat; fragments and the litany earned by the scene | land, refrain, or release | 4 to 5 |
| An essay that reaches a conclusion | stays while the question holds | the question at the top, the turn earned, never announced; the hook is the tension, not the thesis | the hard sentence, or the callback | 4 |
| A paper, a report, a memo | came for the finding | the abstract first: what will be established, in the words the conclusion will complete; the body pays it in order; a postscript outside the frame for what came after | the abstract completed | 1 to 2 |
| A post, a thread, a page that can be scrolled past | can leave at every scroll | the claim in the first line, if it is surprising; paid at every scroll; survives being read as subheads and first lines; at most one loop open | a consequence, never an aphorism | 2 to 3 |
| A message, an email | has a reason to finish | one ask, once, in the first screen; context after the ask; bad news first, cause in one line, then what happens next | the next action | 1 to 2 |
| A repo doc, a spec, a runbook | came for one thing | the answer where they will look; one name for one thing; the smallest valid structure; code keeps its own conventions | the last useful point | 1 to 2 |
| UI copy, an error, a label | is mid-task | the one thing to do, in the words they would use; nothing withheld | none | 1 |
| A reply from an agent | asked | the answer first, no preamble; the last useful point last, no recap; with an orchestrator that reads poetic language, a layered line that packs what was done into few words | the last useful point | 2 to 3, or 4 by agreement |
| A vignette, a description for its own sake | came to look | exactness; no promise need be raised, and an exact image pays in kind; the ledger is nearly idle and that is correct | the last exact thing | 3 to 4 |
| The opening of a long work | has not decided to stay | the promise of the whole, raised and not yet paid; the overture may use what the body cannot (the recursive paragraph, the long block as stance) | the raise, held | 4 |
| Advice, a how-to | came to do a thing | the one instruction, in order, with the procedural "then" honest; the case where it fails | the last step | 1 to 2 |
| A message to someone owed nothing (the estranged friend, the stranger) | has no reason to finish | the reason to read, earned in the first line; the relationship's register, or it reads as a stranger's | the next action, offered not asked | 2 to 3 |
| A game turn, interactive narration | acted, and waits | every turn pays: a fact, a cost, a reaction, a threat, a route, a decision; the actor's intent kept, never silently extended; machinery translated into what they can perceive | what is different now | 3 to 4 |

Where the rules turn with the genre: withholding the reveal is for readers
who stay, and the leaving reader gets the claim first. Several open loops
for the staying reader, one for the leaving one. A fragment or a litany is
earned by a scene and is a tic in a post. Prose to be read rewards
compression; prose to be heard keeps its repetitions, because a listener
cannot go back.

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

The unearned punch has names: the importance claim (pivotal, a testament
to), the fake-profound kicker, the recap, the colon before a reveal, the
denial of a reading nobody held ("it is not X, it is Y"), the three by
reflex. Each promises a weight and pays an ordinary line. But every one of
them is judged against the ledger, never by its shape: a superlative, a
colon, a recap, a rhetorical question, an adverb, can each be load-bearing
when a later line pays it ("There never was so wonderful a book written by
man" is paid by the page that follows). Look forward before firing. The
tell is the shape with no payment behind it.

Comedy is in the same account. Irony is a raise paid by a reversal within
reach; bathos is the stress position spent on something smaller than it
promised, on purpose; deadpan is a plain reading the voice disowns.
Amusement is a feeling the rhythm list does not name, and it is made by
timing, which is placement.

## Deception

A reading the writer opens on purpose, knowing it is wrong, and closes
later with a payment that re-reads everything before it: the twist is a
payment that rewrites the ledger backwards. The trust account says when it
is earned.

- **Never state the false thing.** The reader completes it. Deception by
  manifold, not by lie: the plain reading stays true all the way through,
  and the wrong reading was the reader's own. A narrator may be wrong (that
  is mindset at 5); the writer may not be.
- **The clues were on the page.** A second reader, or the first on a second
  pass, sees it was always there. A twist the reader could not have seen
  through is a lie, and a lie is never repaid.
- **The reveal pays back the trust with interest.** A deception spends
  trust at the reveal, when the reader learns they were led, so it must pay
  more than it cost. Rarer twists hit harder; late ones must be larger and
  fewer; a small deception late in a piece is the worst trade there is.

The strongest form makes the reader's own susceptibility the point: they
trust the soft smile as the miller did, and the reveal convicts them with
the kingdom. The deception enacts the thesis instead of decorating it.

## The question

A question is a raise the reader can decline. Ask one only when the piece
will pay it, or honestly cannot. The rhetorical question opens a reading
the writer already closed, so the reader pays nothing and feels the setup;
it is the weakest opening there is, because the reader answers it and
leaves. Three uses are earned:

- **The question the writer cannot answer.** Write it down in the draft,
  then go and look. What comes back reworks the paragraph or removes it;
  the question itself rarely survives, and the piece is better for having
  asked. This is the ledger used as a tool: a raise the writer owes
  themself.
- **The question the reader did not know to ask**, raised and then
  answered. One unit that raises and pays, which is why it reads as a gift
  and not a setup. Its unearned cousin is the faux insight ("what most
  people miss"), which raises the same way and pays an ordinary claim.
- **The open question as a release**, at the end of exploratory writing,
  where the piece does not know and says so. Once, and only when true.

## The figures

- **The recursive paragraph**: each sentence begins on the same phrase and
  takes it one step further, so the phrase means more at the end than at
  the start. Once in a piece: at the end, where the ledger closes, or as
  the overture, where it opens everything at once (Bleak House's fog).
- **The crescendo**: the evaluative word climbing by degrees across a
  paragraph, the low step first ("beautiful", then "most beautiful and
  most wonderful"). Placement at the scale of word choice; cut the first
  step and the climb is gone.
- **The litany**: a list said as prose, one frame repeated with the number
  of items the content has, never three by reflex. It is the refrain at the
  scale of a phrase, and it is earned by a scene.
- **The withheld word**: three em dashes (———) withhold a word: "Mr. ———",
  the name on the letter, what someone cannot say. It is the gap the reader
  fills and fills wrong, the grand pause of the piece, the machine's own tic
  made into its longest silence. Use it once, only for a thing the piece
  still holds open and will pay later, and only after the reader has
  reached for that thing more than once; never for a thing you will not
  answer at all.

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
  Everywhere else, no dash. The semicolon, the comma-and, and the
  participial tail ("…, leaving the rest untouched") are the dash in other
  clothes: the same joining of two sentences that should have been two, and
  the same hum. A page with no dashes can still be all joiner.
- **The parenthesis** is the aside said under the breath, the one mark for
  a voice lowered; the comma is the shorter rest. Once a page, like the
  swear, and never to smuggle a second clause past the reader.

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

## The sentence, in the model's terms

Rules other guides state as taste, kept here because the model explains
them (the long form, with sources, is `references/evidence.md`):

- The character in the subject, the action in the verb. An abstraction in
  the subject slot hides who acts, and opens readings nobody will pay.
- One thing, one name. A renamed thing is a new thing to the reader, a
  referent raised that nothing pays. The refrain repeats on purpose; the
  synonym cycle repeats by accident.
- The common word for the common thing. A pig is a pig, a key is a key. The
  second meaning rides on a plain word and falls off a rare one, because the
  reader stops on the word instead of the meaning. Two carve-outs: the
  rare word is right when the second meaning lives only there ("a sojourner
  in civilized life" carries what "visitor" drops); and a common word that
  another domain has loaded (undo, save, commit, in software) is not the
  common word to that reader, and its borrowed sense arrives whether you
  meant it or not.
- One thing, one name, except where the new name is a payment: rename when
  the reader's knowledge has changed or the image has tightened (the lady
  with the dog, then Anna Sergeyevna, then "her"). Each new name moves the
  ledger; the synonym cycle moves nothing.
- A cliché is a refrain planted by other texts. The reader completes it
  before reading it, and its sense never shifts, so it pays nothing: an old
  man feeding pigeons, a city that never sleeps. The exact detail is the
  opposite case: "the colour of strong tea" is not dense and owes nothing,
  it pays in kind. Concreteness is a payment; exactness never needs a
  promise behind it.
- Pay only what was raised. A clarification the reader did not need is a
  payment with no promise behind it: it spends their pool on words, and
  it spends their trust, because it says you took them for strength 1.
  The test is deletion: if nothing is lost, it was telling them what they
  already held. Keep a clarification only where the reading it closes was
  really open (a pronoun with two candidates, a loaded common word), or
  where the purpose owes it (a doc, where the reader came for exactly
  that). The over-clarifier's state is insistence, and the reader hears
  it before they read it.
- A borrowed phrase is a manifold with two readings. When the narration
  takes a character's words ("for when he comes"), the reader hears the
  character and the narrator at once, and the distance between them is a
  second sense the skill otherwise assumes away. A character's misplaced
  stress is a raise the writer pays on the next line.
- One hedge per claim. A hedge is a reading kept open on purpose; a second
  one opens nothing new. Keep the adverbs that carry the claim (only,
  rarely, almost); cut the ones that prop a weak verb.
- A number pays; an adjective raises. "Cut review time from thirty minutes
  to eight" pays what "significantly improves" only promises.
- The example after the claim, the definition one paragraph before its use.
  A detail before its promise is a raise with nothing to carry it; pay just
  before it is due.
- Concede before you are forced to. An objection you raise costs a sentence;
  the same objection occurring to the reader costs their trust. Close the
  reading they would open on their own.
- The title is the first raise. Write it last and check that the piece paid
  it.
- A trailing participle that explains (highlighting, underscoring,
  reflecting) points at the planted meaning. Cut it; the meaning was planted
  or it was not.
- Cut at the scale of the debt. Whole sections, then the first paragraph,
  then the summary paragraph, then restating sentences; adjectives last.
  Adjective-hunting leaves the balance where it was.

## Keep the ledger on paper

A prompt alone forgets the balance by the third paragraph (Eli, 2026-11-02:
"I'm not sure how effective just a prompt will be without the ledger"). So
write the ledger down and keep it beside the draft. Before each paragraph,
one line:

```
¶7  owed: the letter (raised ¶2), who locked the door (¶4)   due now: the letter
    debt: 310 words since ¶4 paid    feeling: dread, low    state: fear 3 → 4, because ¶6 opened the door
    → scene · staccato · restate · plain · no punch
```

Mark the draft as you go, in brackets the final pass strips:

- `[raise: the letter]` on a sentence that opens a promise.
- `[pay: the letter]` on the sentence that pays it.
- `[plant: "the boards creak under nothing"]` on a line meant to return.
- `[join: therefore]` or `[join: but]` at the head of a paragraph; write `[join: and then]`
  when that is the truth, and the ledger script will name it.
- `[pay: inferred]` or `[pay: off-page]` when a raise is paid by the
  reader's own knowledge, an allusion, or a thing the dial at 5 leaves
  found rather than told; the script counts it as paid and you have said
  so on purpose.
- `[state: fear 4]` at the head of a paragraph when the speaker's state or
  its degree has moved; the script lists the trajectory beside the debt,
  names a jump of two or more steps at a seam joined by "and then", and a
  state that has not moved in five paragraphs.

`python3 scripts/meaning_ledger.py --strength 3 < draft.txt` (this skill's `scripts/`) reads the marks and reports,
per paragraph, the debt (words since the last payment), the reader's pool
(spent by long sentences and raises, regenerated by plain sentences and
short paragraphs, refilled at once by payments and refrains, drawn as a
wave at the end, with the paragraph where it runs dry named), what is
still owed,
what was raised and never paid, any refrain planted fewer than twice before
it returned, and any paragraph written while something was due whose last
sentence pays nothing (the stress position spent on a quiet line). It is arithmetic over your own
marks, not a judgement; the judgement is yours when you mark.

## Workflow

1. Write the brief: the purpose (the table above), the plain meaning, what
   it carries under that, the three dials (ambiguity, mindset, the
   reader's strength).
2. Name the reader's balance before the passage, on paper (above): what has
   been promised and not paid; what is due now; the feeling the previous
   passage left.
3. Choose tempo, rhythm, form role, and whether this paragraph punches, and
   which punch. Write those four words down before drafting.
4. Draft. Keep the surface clear enough that a first reader is never lost.
   One meaning per sentence where nothing is owed; two or three details that
   are also signs where something is being raised.
5. Check the two positions: does the paragraph open on what the reader
   holds, and is the last sentence the one where the most changes? If not,
   move or cut until it is.
6. Check density against the ledger: every dense sentence names what it
   raises; every punch names what it pays. Remove what names nothing.
7. Look at the page. Run `--shape`. A dense opening, equal blocks, a list
   in a costume: fix the shape before the words.
8. With the Poet tool available: ask what else the dense sentences can mean,
   close the readings you did not mean, keep the one you did. Without it: list
   the readings yourself and close them by hand.

## Analyze a piece

When asked to analyze, review, or say why a piece works or fails, apply the
framework to it and report in this shape: name the pattern, quote the line,
give the fix in a few words. No score, and no guess at who wrote it; readers
cannot tell and neither can you (`references/evidence.md`, Bot or not).

1. **The purpose, from the evidence.** Headings, code spans, paths and
   imperatives say a repo doc; a greeting and an ask say a message; dialogue
   and a tense say a scene; a claim in line one and subheads say a post; an
   answer with no preamble says an agent's reply. Name the genre, the dial
   it implies, and the rules that turn with it. Say which you took and why.
   Then the mindset, from the evidence too: sentence length and where it
   breaks, what is named and what is walked around, the accents spent, the
   hedges. Say what state the draft is in and how far gone, 1 to 5. If the
   writer did not say what mindset they want to present, this is the help
   mode: do not assume one. Show the state you read, and offer two or
   three mindsets the piece could present instead, each as one line of the
   draft rewritten in that state, so they can pick by ear. Read the state
   the page presents, never the state the person is in; it is a reading of
   the text, not a diagnosis.
2. **The glance.** Run `--shape`. The first paragraph's share, the spread,
   the longest block, lists and bold and subheads, repeated openings. Say
   what the page tells a reader who has not read a word.
3. **The ledger, reconstructed.** Per paragraph: what it raises, what it
   pays, the running debt. What was raised and never paid. What was paid
   and never raised (a reveal with no setup). Mark the draft with the
   brackets and run the script if the piece is longer than a page.
4. **The seams.** At each paragraph break: therefore, but, or and then. The
   repeated-noun link, or a connective faking motion.
5. **The five measurements**, per paragraph: the band it landed in (plain,
   lean, dense, punch); what the stress position was spent on; whether a
   held question moved; what it makes the reader feel and how keyed up;
   which planted line it carried. These find every dense sentence on a
   low-stakes beat and every stretch run too long unpaid. Then the
   strength check: the sentences whose clauses or inferences exceed the
   reader's strength (stacked clauses with an escalation to infer, three
   readings open in one line, a debt still running past the point the
   strength would have drained), quoted, with the split that would carry
   them at the strength named.
6. **The topic position.** Where a paragraph must be read twice, check the
   known-new chain first.
6b. **The state trajectory.** The state per paragraph, with its cause. A
   flat line across the page is the machine voice; a jump without a cause
   is a seam to fix; a trajectory that moves with the ledger is the
   mechanism of the reader's feeling, and the thing to protect in revision.
   Note where felt and shown part, and where they cross.
7. **Accidental readings.** A pronoun with two candidates; a thing renamed;
   a dangling modifier; a negation whose scope is unclear; a stack of nouns;
   the rare word where the common one was right; the pointing participle.
8. **Unearned weight.** The importance claim, the fake-profound kicker, the
   recap, the colon reveal, the denied reading, the three by reflex, the
   dash that joins, the swear nobody earned.
9. **The three changes that would pay the most**, ranked, each tied to a
   quoted line.

## Do not

- Do not write every paragraph at the same density, or the same length.
  Plain is a band, not a failure; short is a tempo, not a lapse.
- Do not open on a wall. The first paragraph is the one the eye must take
  whole.
- Do not clarify what the reader already holds. Every explanation is a
  spend; the unasked one is a spend with no payoff and a drain on trust.
- Do not end every paragraph on an aphorism. Brilliance on every line is a
  page nobody finishes; ration it to where the pool is full.
- Do not deceive by stating what is false. Let the reader complete the
  wrong reading, leave the clue on the page, and pay the trust back with
  interest.
- Do not point at a planted meaning. If the reader must be told it is there,
  it is not planted.
- Do not end on atmosphere, unless the atmosphere is the payment: the
  Mississippi's water read as a book ends on the water because the water
  is what changed. Do not end dense on a beat that owes nothing.
- Do not change rhythm mid-scene or refrain a line that was told once.
- Do not join two paragraphs with "and then". Therefore, or but.
- Do not reach for a rarer word when the common one is right, and do not
  rename a thing to avoid repeating it.
- Do not withhold from a reader who can leave, and do not front-load a
  reader who stayed for the turn.
- Do not invent a claim, a number, a feeling, or an experience the person
  did not supply. Voice is how they say things; inventing what they say is
  forgery.

## What this skill does not hold

Sound: alliteration, rhyme, the stress cluster, chiasmus, how the words
sound in the mouth. Three analyses in the skill's own sweep called it a
fourth axis ("what the page sounds like"); two called it rhythm at the
scale of a syllable. It is not in the model here, and a revision this
skill proposes can break a rhyme it cannot hear. Effect Co's Poet holds
it (the library's `sound` tool and the figures note). Also outside: the
reader's time and knowledge (a chaise and four), which belong to a gloss,
and whether a claim is true.

## Sources

Grown out of [Effect Co](https://effectco.game)'s writing tools: the Poet
(meaning layering, the ledger of readings) and the pacing work behind its
stories (2026-11-02). There the ledger is kept for the writer; here it is
kept on paper. The rules taken from other guides, with their sources and
the weight of their evidence, are in `references/evidence.md`; most are
assertions, a few are measured, and the measured ones are marked.
