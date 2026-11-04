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
