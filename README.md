# homersturn

**Writing is meaning manifolds presented like music.**

A writing skill for Claude Code, Codex and any agent that reads `SKILL.md`
files. It teaches one thing: where meaning goes. A sentence holds a cloud of
readings; a passage raises promises and pays them; density is earned only
where something is owed, a punch only where something is paid, and
everything else is plain. The rest of the skill is the craft of placing
those: three punches, rhythm as emotion, tempo, song forms and their
transitions, the stress position at the end of every paragraph, three
one-off figures, the swear as an accent, and the dash redeemed as a rest.

## Why it exists

I tried to make a game for players. The weak link was the writers. So I
tried to make a game for writers. The weak link was in language. So I made
this, and returned to my earlier efforts.

The rules here were first built as an engine: a kernel that keeps a ledger
of what a reader has been promised and what has been paid, and tells the
model, each paragraph, what that paragraph is for. This skill is the same
method for a writer, or a model, with no engine behind it. The ledger moves
to paper, and a small script does the arithmetic.

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

Whatever the density, the last sentence of a paragraph is where the most
changes. End on what is different now, never on the setting, the weather or
a view.

## Provenance

Grown out of [Effect Co](https://effectco.game)'s writing tools: the Poet (meaning layering, the
ledger of readings) and the pacing engine of its narrative kernel, where
every rule here is enforced by code rather than asked of a prompt. Written
with Claude, November 2026.

## License

MIT.
