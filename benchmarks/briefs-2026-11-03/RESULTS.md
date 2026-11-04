# One-line briefs, 2026-11-03

Eli: "Let's try a different prompt test: tell me a joke", then "Go ahead
and stress test". Ten briefs in `briefs.json`, the skill at 0.4.0 as the
only instructions, one reply per brief per model. `run.py` writes the
served model into each file's first line, read from the proxy log after
the call completes. Opus was served as `claude-opus-4-8` on all ten;
Fable was served as itself.

| Brief | Purpose row | Opus (4.8) | Fable 5.1 |
|---|---|---|---|
| joke | reply | the doctor and the two places: a cliché | separation anxiety: deception rule used as written |
| apology | message | ask once, but a dinner the brief did not supply | ask once, nothing invented, no excuse offered |
| headline | post | "until spring", a season inferred | plain, says the closure twice |
| error | label, dial 1 | clean | clean, added two buttons the brief did not ask for |
| toast | heard | the light as a refrain planted once; two dashes | "The library was open" four times, which is what spoken prose keeps |
| release note | doc | two headline sentences, each paid | tells the fixes in the opening and again below |
| game turn | game turn | fact, reaction, threat, route; no cost | all five payments; the pick bent; ends on the threat; a reused frame |
| agent reply | reply | answer first; "returns null", a guessed mechanism | answer first; the quarter-hour offset supplied from world knowledge; the alternative fix conceded |
| thread opener | post | three paragraphs for a 280-character brief | one paragraph with the loop open |
| eulogy | grief at 4 | "the chest keeps rising anyway"; one-word land | "seven thousand nights"; the number pays; ends on not knowing how to sleep |
| insult | comedy | "do hold still" | "This time toward me" |

What survived at the smallest scale: the purpose row, the loaded word,
the land, the refrain for prose to be heard, deception at the scale of a
line. What broke: invented detail in non-fiction on both models, the dash
on Opus, over-telling and the frame on Fable, length on Opus. Taken into
0.4.1: the invented detail in the analyze pass, the cliché above the
phrase in the sentence rules. One reply each: pattern, not finding.

## The revision, four blind stories

The chinchilla brief plus "the narrator has an opinion of the chinchilla
and changes it once, in view of the reader, midway through a sentence",
on the skill at 0.4.1 (the figure not yet named) and 0.4.2 (named), Opus
through the proxy (served as 4.8 both times) and a Fable subagent.
Files: `runs/revision-*`.

| arm | the revision |
|---|---|
| Opus, 0.4.1 | "He was a thief, I thought at first... and then I learned what he did in the nurseries, and thief was far too clean a word": across a beat, with a dash |
| Opus, 0.4.2 | "I called him cruel, at first, the way you call winter cruel—no: winter takes what it needs and goes": mid-sentence, dash and "no", then an aphorism |
| Fable, 0.4.1 | "a creature built like that can hardly be blamed for— no. He rolled in it.": mid-sentence, dash and "no" |
| Fable, 0.4.2 | "he was soft, we had meant, because he was weak, and he was soft, I saw then, because nothing had ever got through to him": mid-sentence, no dash, built on a joke planted in the first paragraph |

The brief asked for the revision, so every arm staged one; naming the
figure changed its shape, not its presence. Without the figure, three of
four reached for the break-off dash and "no" as the revision's mark; with
it, Fable stated the new reading in the grammar of the old and paid a
plant. 0.4.3 adds that line to the figure. One story per arm: pattern.
