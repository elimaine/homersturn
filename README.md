# homersturn

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

## Install

Claude Code reads skills from `~/.claude/skills/<name>/SKILL.md`:

```sh
git clone https://github.com/elimaine/homersturn ~/code/homersturn
ln -s ~/code/homersturn ~/.claude/skills/homersturn
```

Then `/homersturn` in a session, or let the description trigger it. For
Codex and other agents, point them at `SKILL.md` the way they take skills.

## What is in it

- `SKILL.md`: the method. The model (manifold, ledger, rhythm, tempo), the
  three punches (land, refrain, release), the stress position, forms and
  transitions, figures (the recursive paragraph, the litany, the withheld
  word), accents (the swear, the dash), the paper ledger, the workflow, and
  the do-nots.
- `references/manifold-and-ledger.md`: why. Surprisal and uniform
  information density, Gopen and Swan on the stress position, Ely,
  Frankel and Kamenica on suspense, Valve's director on rhythm switches,
  Caplin's sentence, song forms as grammars of return.
- `scripts/meaning_ledger.py`: arithmetic over your own marks. Mark a draft
  with `[raise: x]`, `[pay: x]` and `[plant: "line"]`; the script reports
  debt per paragraph, what is still owed, and the paragraph that spent its
  stress position on a quiet line while something was due.

```sh
python3 scripts/meaning_ledger.py < draft.txt
python3 scripts/meaning_ledger.py --strip < draft.txt > clean.txt
```

## One rule, if you take only one

End each paragraph on the thing that changed.

Whatever the density, the last sentence is where the reader puts the
weight. Never spend it on the setting, the weather, or a view. And do not
make the paragraphs the same length: a paragraph is as long as what it
carries, and a page of equal paragraphs reads as a machine humming.

And use the common word for the common thing. The second meaning rides
on a plain word; it falls off a rare one.

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
