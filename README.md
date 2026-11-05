# homersturn

Version 0.7.8.

**Writing is meaning manifolds manifested like music.**

A writing skill for Claude Code, Codex, and any agent that reads a
`SKILL.md`.

It teaches one thing: where meaning goes.

Most writing says what it means. Good writing also carries what it does not
say, and the trick is knowing where. Put it everywhere and the reader stops
hearing it. Put it where the reader is already waiting for something, and
it lands. So the skill is a set of habits for that placement: keep a ledger
of what you have promised the reader and what you have paid, write plain
where nothing is owed, end each paragraph on the thing that changed, pick
the rhythm from the feeling, and save the big moves for where they are
earned.

## Why it exists

I tried to make a game for players. The weak link was the writers. So I
tried to make a game for writers. The weak link was in language.

So I made this, and returned to my earlier efforts.

The rules were worked out inside Effect Co's writing tools, where a ledger
of what the reader has been promised and what has been paid decides what
each paragraph is for. This skill is the same method for a writer, or a
model, on its own: the ledger moves to paper, and a small script does the
arithmetic.

## The name

Three readings, all kept, which is the method in miniature: the bard's
turn at the fire, the same story every night told so the room leans in at
the same places; the model's turn in a session, where this gets applied;
and Homer turning in his grave at what the machines did with his trade
before this. The last one is the one to earn your way out of.

## What it is for

Write with it, revise with it, or hand it a piece and ask what works. Some
ways it earns its keep:

- **Say what kind of writing you want**, the literal meaning and the
  implied one, the vibe. The skill takes a purpose (a scene, an essay, a
  post, a message, a repo doc, UI copy, an agent's reply, a game turn) and
  lets it set the defaults, because each is a genre the song has to fit.
- **Set ambiguity as a dial.** "Ambiguity 1 to 5: 3" is the default; 1 is
  one reading per sentence and everything told, 5 is readings held to the
  last line for a reader who will read twice. The dial is on sense, never
  on reference: who spoke and who acted are clear at every setting.
- **Say who is writing, in what key, and how far gone.** The mindset is
  a second dial: at 1 the state is named once and the page is otherwise
  plain, at 5 it is never named and every detail and the rhythm are about
  it. The keys sit on a wheel that keeps the circle of fifths' arithmetic
  (`references/wheel.md`): twelve positions, a bright and a dark state at
  each sharing the same details, a neighbour one feature away, the far
  side a bridge away, the modes as tints, and every move priced, so the
  safe steps and the jarring ones are a lookup, not a derivation. Leave
  the dial out and the skill reads the state the draft is in and offers
  two or three it could present instead, one line each, for you to pick
  by ear.
- **Say how strong the reader is.** The third dial caps density: at 1
  one clause a sentence and every second sense told, at 5 a triple clause
  with the third left to infer. Ambiguity may not exceed it by more than
  one, and it drains as the page goes.
- **Analyze a piece.** Ask it why a draft feels dense, flat or hard to
  parse and it names the genre from the evidence, reads the shape of the
  page, reconstructs the ledger of what was promised and paid, and reports
  pattern, line, fix. No score, no guess at who wrote it.
- **Talk to an orchestrator in it.** Agent output is a chore to read.
  With this on, a model can pack layered meaning into few words, so you get
  a better sense of what it did, and you can talk back and forth in poetic
  language without either side losing the plain reading.
- **Look at the page before the words.** A page says something before a
  word is read, and a dense first paragraph says "don't". `--shape` prints
  what the glance sees.
- **Read the skill as its own example.** Each section of `SKILL.md` is
  written in one key of the wheel, named under its heading, so the rule
  is told and the key is shown on the same page.

It is a few days old. Not every machine tic is squashed yet, and the
genre rows could use more detail for specific kinds of text. If you notice
one, open an issue or a pull request.

## Install

Claude Code reads skills from `~/.claude/skills/<name>/SKILL.md`:

```sh
git clone https://github.com/elimaine/homersturn ~/code/homersturn
ln -s ~/code/homersturn ~/.claude/skills/homersturn
```

Then `/homersturn` in a session, or let the description trigger it. For
Codex and other agents, point them at `SKILL.md` the way they take skills.

## What is in it

- `SKILL.md`: the method. The brief and the dial, the model (manifold,
  ledger, rhythm, tempo), the glance, the topic and stress positions, the
  join, purpose and genre, the three punches (land, refrain, release), the
  entrance (a character introduced by the line a voice actor reads them
  from), figures (the recursive paragraph, the litany, the withheld word), accents
  (the swear, the dash), forms and transitions, the sentence rules the
  model explains, the paper ledger, the workflow, the analyze mode, and the
  do-nots.
- `references/wheel.md`: the mindset on the circle of fifths. The twelve
  positions with their bright and dark states, the math kept the same as
  notes (the fifth, the relative, the parallel, the tritone, the semitone
  jolt, dynamics as degree, modes as tints), the moves with their cost,
  and the theory-to-prose table Poet's margins share.
- `references/manifold-and-ledger.md`: why. Surprisal and uniform
  information density, Gopen and Swan on the stress position, Ely,
  Frankel and Kamenica on suspense, Valve's director on rhythm switches,
  Caplin's sentence, song forms as grammars of return.
- `references/evidence.md`: the tips taken from other writing guides
  (Strunk, Gopen and Swan, Williams, the skills on Eli's disk), each with
  its source, what the model makes of it, and the weight of its evidence.
  Most are assertions; the measured ones are marked.
- `scripts/meaning_ledger.py`: arithmetic over your own marks. Mark a draft
  with `[raise: x]`, `[pay: x]` and `[plant: "line"]`; the script reports
  words carried per paragraph, what is still owed, and the paragraph that spent its
  stress position on a quiet line while something was due. `--shape` needs
  no marks: it prints what the page says before a word is read, and the
  machine's tics as structural leads (the dash that joins, not X but Y,
  the tricolon, the colon before a reveal, the short copula ending), each
  to be read by hand. `--list`
  prints the skill's bits and moves, one line each, read from `SKILL.md`.
  `--wheel` prints the keys and the moves with their cost, and a marked
  draft's state turns are priced on it.
- `references/purposes.md` and `references/sentence.md`: the full genre
  table and the sentence rules with their accounts, kept out of the skill
  so the skill stays short enough to follow.
- The benches live in the sibling repo `homersturn-bench`
  (`~/code/homersturn-bench`): the intent cards, frozen skill texts,
  briefs, every reply, blind sheets and results. They are kept out of
  this directory so a model that loads the skill never reads a brief or
  a piece before it writes; the briefs are the strongest tint there is.

```sh
python3 scripts/meaning_ledger.py < draft.txt
python3 scripts/meaning_ledger.py --strip < draft.txt > clean.txt
python3 scripts/meaning_ledger.py --shape < draft.txt
python3 scripts/meaning_ledger.py --list
python3 scripts/meaning_ledger.py --wheel
```

## An example with every dial set

The brief, one line, as the skill asks for it before a word is written:

```
Purpose: a scene, the reader chose to stay. Plain: a woman takes a bird
feeder down in autumn. Under it: the person who filled it is gone.
Ambiguity 3. Mindset: tenderness, ionian, 2. Reader strength 3.
```

The balance line that goes above the paragraph on paper:

```
¶1  owed: nothing   due now: the hook
    carried: 0   feeling: tenderness 2   state: tenderness ionian 2 → tenderness ionian 2
    → scene · long sentences, soft stops · overture · lean · release
```

The draft, marked the way the script reads it:

```
[state: tenderness ionian 2] She took the feeder down in October, with
the seed still half full. [raise: half full] The hook had been screwed
into the beam at a height she had to reach for, and she reached for it
the way she had every week, on her toes, one hand flat on the post.
[raise: the height] The seed went into the bin. The feeder went on the
shelf in the shed, beside the gloves, which were not hers. [pay: half
full] [pay: the height] She left the hook where it was.
```

What the dials did. Ambiguity 3 is a second sense where something is
owed, paid within the paragraph: the seed half full and the height of the
hook are both raised, and the gloves pay them both at once, which is
the punch that pays many, with one debt held to the last line, the hook
left where it is. The mindset is tenderness at 2, so
the state is not named and the details are the ones tenderness picks,
the reaching and the hand on the post, at a volume where a reader can
still miss it. Reader strength 3 holds a seventy-word paragraph with one
long sentence in it and no more. The punch is a release, what changed in
seven words.

The same brief at other settings: at ambiguity 1 the gloves are "her
husband's" and nothing is left to find; at 5 the gloves are cut and only
the height says it, for a reader who reads twice. Tenderness at 4 would
let the sentence run on past the post and the stops soften further;
sorrow, its dark relative, keeps every detail and lowers the light.
Strength 1 would break the long sentence in three.

The script on the marked draft:

```
  ¶  words  carry  pool  owed / events
  1     78      0   100  state tenderness ionian 2, raise half full, raise the height, pay half full, pay the height

pool, strength 3 (capacity 100): █  low 100
```

Nothing carried out of the paragraph and the pool full, which is what a
scene's first paragraph should hand the second.

## One rule, if you take only one

End each paragraph on the thing that changed.

Whatever the density, the last sentence is where the reader puts the
weight. Never spend it on the setting, the weather, or a view. And do not
make the paragraphs the same length: a paragraph is as long as what it
carries, and a page of equal paragraphs reads as a machine humming.

And use the common word for the common thing. The second meaning rides
on a plain word; it falls off a rare one.

And open on a paragraph the eye can take whole. The page is read before
the words are, and a wall at the top is read as "don't".

## Provenance

Grown out of [Effect Co](https://effectco.game)'s writing tools: the Poet
(meaning layering, the ledger of readings) and the pacing work behind its
stories. Written with Claude, November 2026.

## Once

Where meaning goes is the whole of it. Where meaning goes is a question the
reader answers before you do, by waiting, and the waiting is the place.
Where meaning goes, then, is wherever the reader is already standing when it
arrives, and your work is to know where they stand. Where meaning goes is
where they are.

## License

MIT.
