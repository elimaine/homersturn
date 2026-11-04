# homersturn

Version 0.2.0 (2026-11-03). The version is in `SKILL.md`'s front matter and
as a git tag; it moves when a rule changes, not when a word does.

**Writing is meaning manifolds presented like music.**

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
- **Set ambiguity as a dial.** "Ambiguity 1 to 5: 4" is the default; 1 is
  one reading per sentence and everything told, 5 is readings held to the
  last line for a reader who will read twice.
- **Say who is writing, and how far gone.** The mindset is a second
  dial: a grieving writer at 1 names the loss in the first line, at 5
  never names it and every detail is about it. Leave it out and the skill
  reads the state the draft is in and offers two or three it could present
  instead, one line each, for you to pick by ear.
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
  figures (the recursive paragraph, the litany, the withheld word), accents
  (the swear, the dash), forms and transitions, the sentence rules the
  model explains, the paper ledger, the workflow, the analyze mode, and the
  do-nots.
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
  debt per paragraph, what is still owed, and the paragraph that spent its
  stress position on a quiet line while something was due. `--shape` needs
  no marks: it prints what the page says before a word is read.
- `benchmarks/`: the glance bench. The same words broken three ways and
  judged, with the intent card, the analysis plan, every reply, and the
  human check beside the numbers.

```sh
python3 scripts/meaning_ledger.py < draft.txt
python3 scripts/meaning_ledger.py --strip < draft.txt > clean.txt
python3 scripts/meaning_ledger.py --shape < draft.txt
```

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
