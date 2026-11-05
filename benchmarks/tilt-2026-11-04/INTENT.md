# Intent: does the 0.7.0 tilt fix reach the page

Written before any call, 2026-11-04, on `main` at `625ddc2`.

## The user's words

Eli, 2026-11-04, after the turns bench: "our method has some negativity
hiding in it. If I random searched the page I see negative words"; on
the friend piece, "'It was my fault' is not what I want to read"; then
"Do all that. Next brief keep it to 2 stories"; and "Maybe not every!
Don't overcorrect."

## The construct

**Tilt**: the dark-against-light lexicon count of a page, per thousand
words, as `--shape` prints it at 0.7.0. The skill's own tilt is a prior
the writer reads before the brief (0.6.1: 32 dark, 23 light; 0.7.0: 17
and 23). The question is whether the lighter skill writes a lighter
piece on a brief that is bright-shaped, and whether the state stays
unnamed in its own word. Primary: Eli's blind preference per pair.
Secondary: each piece's tilt and named-state leads from `--shape`.

## The arms

- A: `skill-0.6.1-frozen.md` with its mindset and wheel references
  (the turns bench's arm B, byte-identical).
- B: `skill-0.7.0-frozen.md` (SKILL.md at `625ddc2`) with its mindset
  and wheel.

## The briefs

Two stories, both ending bright, neither loss-shaped: a father and
daughter at a station (station), a girl's kite that holds on the third
run (kite). The earlier six briefs were five parts loss, which was the
brief-writer's own tilt; these are the correction.

## The run

As the turns bench: writer claude-fable-5-1 at high over CliProxyAPI,
one call in flight, served model read per request, the same prompt.
Four calls. Eli ranks blind on `BLIND.md`; the key is sealed.
