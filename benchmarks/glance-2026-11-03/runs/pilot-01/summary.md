# Glance bench run pilot-01

inviting: 1 to 5, higher means the shape invites a reader to start and keep going, so higher is better.
Unit: the item (passage); samples averaged within item, shape, mode.

Calls: 18; malformed or failed: 7 (excluded from means, listed below).
- blur check, 01-harbour: ''
- blur check, 02-release-note: ''

## mode: text

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 4.00 | 5.00 | – | – | – |
| 02-release-note | – | – | 4.00 | – | – |

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 1/1; equal: ¶1 named 0/1; shaped: ¶1 named 0/1

## mode: blur

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 3.00 | – | 4.00 | 1.00 | – |
| 02-release-note | 3.00 | – | 4.00 | 1.00 | – |

shaped − dense-open: mean +1.00 (items n=2, bootstrap 95% +1.00 to +1.00); sign test 2 up / 0 down, two-sided p = 0.500 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 2/2; equal: –; shaped: ¶1 named 0/2

## mode: clear

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 4.00 | 5.00 | – | – | – |
| 02-release-note | 3.00 | – | 4.00 | 1.00 | – |

shaped − dense-open: mean +1.00 (items n=1, bootstrap 95% +1.00 to +1.00); sign test 1 up / 0 down, two-sided p = 1.000 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 2/2; equal: ¶1 named 0/1; shaped: ¶1 named 0/1

## Shape metrics (the deterministic view)

| arm | paragraphs | first share | max share | cv |
|---|---:|---:|---:|---:|
| 01-harbour-dense-open | 4 | 0.65 | 0.65 | 0.94 |
| 01-harbour-equal | 4 | 0.26 | 0.31 | 0.21 |
| 01-harbour-shaped | 5 | 0.05 | 0.47 | 0.72 |
| 02-release-note-dense-open | 4 | 0.73 | 0.73 | 1.12 |
| 02-release-note-equal | 4 | 0.25 | 0.30 | 0.12 |
| 02-release-note-shaped | 5 | 0.05 | 0.50 | 0.81 |
| 03-letter-dense-open | 4 | 0.70 | 0.70 | 1.07 |
| 03-letter-equal | 4 | 0.24 | 0.27 | 0.08 |
| 03-letter-shaped | 5 | 0.05 | 0.42 | 0.68 |
| 04-how-locks-work-dense-open | 4 | 0.70 | 0.70 | 1.08 |
| 04-how-locks-work-equal | 4 | 0.30 | 0.30 | 0.16 |
| 04-how-locks-work-shaped | 5 | 0.05 | 0.49 | 0.84 |
| 05-after-the-match-dense-open | 4 | 0.75 | 0.75 | 1.16 |
| 05-after-the-match-equal | 4 | 0.24 | 0.30 | 0.15 |
| 05-after-the-match-shaped | 5 | 0.06 | 0.44 | 0.74 |
| 06-on-naming-dense-open | 4 | 0.66 | 0.66 | 0.96 |
| 06-on-naming-equal | 4 | 0.35 | 0.35 | 0.30 |
| 06-on-naming-shaped | 5 | 0.07 | 0.46 | 0.70 |

## Malformed or failed

- 02-release-note equal clear: '{"inviting": 5, "hesitate_at": 0, "why": "Four short, evenly sized paragraphs of three to four lines with generous g'
- 02-release-note dense-open text: '{"inviting": 3, "hesitate_at": 1, "why": "One long, unbroken opening block asks a lot'
- 01-harbour shaped text: ''
- 02-release-note equal blur: '{"inviting": 4, "hesitate_at": 2, "why": "Four short blocks of 3–4 lines with generous gaps;'
- 01-harbour shaped clear: ''
- 02-release-note equal text: '{"inviting": 4, "hesitate_at": 2, "why": "A short opening and four even, modest blocks with regular breaks; paragra'
- 01-harbour equal blur: '{"inviting": 5, "hesitate_at": 0, "why": "Four short, even blocks of three to four lines'

## Every reply

- 01-harbour · dense-open · clear · s0: 4 @¶1: A nine-line opening block asks the most before any break, but the short, widely spaced paragraphs after it are effortless and visible from the start.
- 02-release-note · shaped · blur · s0: 4 @¶2: A one-line opener is easy, but the seven-line second block is the only dense wall; after it the paragraphs shrink to 3, 2 and 2 lines with generous white space.
- 01-harbour · shaped · blur · s0: 4 @¶2: A one-line opener draws you in and the short later blocks have generous gaps, but the six-line second paragraph is the one dense slab early on.
- 02-release-note · dense-open · clear · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs below promise relief.
- 01-harbour · equal · text · s0: 5 @¶0: Four short, evenly sized paragraphs with a light opening and regular breaks; the last runs slightly longer but stays easy to take in.
- 01-harbour · equal · clear · s0: 5 @¶0: Four short, even paragraphs of three to four lines each, with generous breaks and a light opening block that asks little before the first pause.
- 02-release-note · shaped · text · s0: 4 @¶2: A one-line opener draws you in, but the second paragraph is the heaviest block on the page; after it, shorter paragraphs and more white space make the rest easy.
- 01-harbour · dense-open · blur · s0: 3 @¶1: A dense nine-line opening block asks a lot before the first break, though the short, airy paragraphs below promise relief.
- 01-harbour · dense-open · text · s0: 4 @¶1: A dense opening block asks for sustained attention before any break, but the short paragraphs that follow pay it back with white space and an easy run to the end.
- 02-release-note · shaped · clear · s0: 4 @¶2: A one-line opener draws you in, then a seven-line block is the heaviest ask on the page before it eases into short, airy paragraphs.
- 02-release-note · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block must be crossed before any white space; the short paragraphs after it read easily but sit behind that wall.
