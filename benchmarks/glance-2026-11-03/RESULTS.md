# The glance bench: results

Run `full-01` (2026-11-03). Every number here comes from
`runs/full-01/summary.md`; every reply is in `runs/full-01/replies.jsonl`.
Intent card and analysis plan: `INTENT.md`, written before the run.

## The question, in Eli's words

"That is how a page looks when a person hasn't read a word. I'm not sure
if you have a sense of that, or if image models do." And the example:
"starting with a dense paragraph is intimidating and shuts down a reader."

## The design in a line

Six passages, the same words broken three ways (a dense opening, equal
blocks, a one-sentence opening then varied blocks), judged by Claude Opus
5.5 three ways (the text alone, a blurred render no word of which can be
read, a clear render), three samples a cell, 162 calls. `inviting` is 1 to
5; higher means the shape invites a reader to start, so higher is better.
The unit is the passage.

## Findings

1. **A dense opening shuts the judge down.** *Clears zero* (the
   pre-declared primary). Shaped minus dense-open in the blur mode: +1.06
   on the 5-point scale, bootstrap 95% +1.00 to +1.17, all six passages
   the same way, exact sign test p = 0.031. The same in text (+1.00) and
   clear (+1.17), six of six each. Asked where it would stall, the judge
   named the first paragraph in 54 of 54 dense-open replies and in none of
   the 54 shaped ones.
2. **The judge has the sense from the text alone.** *Pattern.* The text
   mode and the blur mode give the same ordering and nearly the same
   numbers on every passage. A text-only model does see the wall; the
   image added nothing the words did not. This is what lets the skill
   stay text-only.
3. **At a glance, even short blocks beat the shaped page.** *Direction*
   (the interval touches zero in one mode). Shaped minus equal was
   negative in every mode (blur −0.28, text −0.44, clear −0.33) and never
   positive on any passage; the sign test does not clear 0.05 at six
   items. In the shaped arm the judge named the second paragraph as the
   stall in 43 of 54 replies: the five-sentence block after a one-line
   opening reads as a wall of its own. Equal blocks were mostly stall-free
   (35 of 54 replies named no paragraph).
4. **The blur was blind.** *Instrument.* Six readability probes, six
   "CANNOT".
5. **No floor, no ceiling, no malformed replies.** *Instrument.* Scores
   ran 3 to 5; 0 of 162 replies failed to parse.

## What it changes in the skill

- The glance rule stands and is stronger than it was: open on a paragraph
  the eye can take whole, and the second paragraph is the next wall. The
  bench's "shaped" arm put 45% of the words in paragraph two and was
  marked for it; the rule is not "one short paragraph then anything" but
  "no block the eye cannot take, early".
- The hum of equal paragraphs is not a glance effect. At a glance, even
  blocks invite. The equal-paragraph rule is a reading-time rule (the
  droning is heard, not seen) and the skill now says so.
- The model is the one writing, and it shares the sense when it looks.
  Running `--shape` is the look.

## Route

Bare `claude-opus-5-5` through CliProxyAPI. The run began on the
round-robin of the two Claude logins; Eli was given a command to route
every Opus call to lifthearth mid-run, and the proxy does not log which
login served a call, so the split is unknown. Subscription usage, no
per-call bill. 162 judge calls, about 800 tokens each, about 45 minutes
at one call in flight with a two-second pause.

## Threats to validity, most severe first

1. **The judge is a model, not a reader.** Eli's blind ratings of the
   same 18 blurred pages (`blind-sheet.png`) are the human check; until
   they are in, finding 1 is about Opus and the direction only is claimed
   for people. Eli's one pre-rating remark ("I think I like P best") picks
   a shaped page.
2. **A designed ordering.** The arms were built to test a hypothesis; the
   judge could be agreeing with the prompt's framing ("the size of the
   first paragraph") rather than seeing. Against this: the prompt also
   named the rest of the page, and the judge ranked equal above shaped,
   which the framing did not suggest.
3. **One judge model, one prompt, default temperature.** Not swapped.
4. **Six passages, all about 190 words, all plain prose.** No lists,
   headings or bold were in play; the glance rules about those are
   untested here.
5. **Breaks moved can shift sense at a seam.** Accepted; in blur mode the
   words were unreadable so it cannot have moved the primary.

## Not covered

Reading-time effects (the hum), the rendering width (one width, 640 px),
anything but English prose, any reader but Opus and, pending, Eli.
