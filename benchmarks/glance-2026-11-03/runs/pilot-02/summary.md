# Glance bench run pilot-02

inviting: 1 to 5, higher means the shape invites a reader to start and keep going, so higher is better.
Unit: the item (passage); samples averaged within item, shape, mode.

Calls: 18; malformed or failed: 0 (excluded from means, listed below).
- blur check, 01-harbour: 'CANNOT\n\nThe image is too blurred for an exact transcription. I can make out the rough shape of the w'
- blur check, 02-release-note: 'CANNOT\n\nThe image is too blurred to transcribe the line exactly. The word shapes suggest something l'

## mode: text

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 3.00 | 5.00 | 4.00 | 1.00 | -1.00 |
| 02-release-note | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +1.00 (items n=2, bootstrap 95% +1.00 to +1.00); sign test 2 up / 0 down, two-sided p = 0.500 (n too small to reach 0.05)

shaped − equal: mean -0.50 (items n=2, bootstrap 95% -1.00 to +0.00); sign test 0 up / 1 down, two-sided p = 1.000 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 2/2; equal: ¶1 named 0/2; shaped: ¶1 named 0/2

## mode: blur

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 3.00 | 5.00 | 4.00 | 1.00 | -1.00 |
| 02-release-note | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +1.00 (items n=2, bootstrap 95% +1.00 to +1.00); sign test 2 up / 0 down, two-sided p = 0.500 (n too small to reach 0.05)

shaped − equal: mean -0.50 (items n=2, bootstrap 95% -1.00 to +0.00); sign test 0 up / 1 down, two-sided p = 1.000 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 2/2; equal: ¶1 named 0/2; shaped: ¶1 named 0/2

## mode: clear

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 4.00 | 5.00 | 4.00 | 0.00 | -1.00 |
| 02-release-note | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +0.50 (items n=2, bootstrap 95% +0.00 to +1.00); sign test 1 up / 0 down, two-sided p = 1.000 (n too small to reach 0.05)

shaped − equal: mean -0.50 (items n=2, bootstrap 95% -1.00 to +0.00); sign test 0 up / 1 down, two-sided p = 1.000 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 2/2; equal: ¶1 named 0/2; shaped: ¶1 named 0/2

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

## Every reply

- 02-release-note · equal · clear · s0: 4 @¶0: Four short blocks of three to four lines with even, generous gaps and a light first paragraph; nothing dense enough to stall on, though the uniform sizes give the eye no clear landmark.
- 01-harbour · dense-open · clear · s0: 4 @¶1: A dense nine-line opening block asks the most before any break, but the short, airy paragraphs after it and the open white space make the page easy to keep going.
- 02-release-note · dense-open · text · s0: 3 @¶1: A dense opening block asks a lot before the first break, though the three short paragraphs after it read easily.
- 02-release-note · shaped · blur · s0: 4 @¶2: A one-line opener and short closing paragraphs leave plenty of white space, but the seven-line second block is a wall right after the start.
- 01-harbour · shaped · blur · s0: 4 @¶2: A one-line opener and wide gaps make it easy to start, but the six-line second block is the only real demand before the page lightens into short paragraphs.
- 01-harbour · shaped · text · s0: 4 @¶2: A one-line opening pulls you in, then the densest block arrives at once before the paragraphs shorten and loosen toward the end.
- 02-release-note · dense-open · clear · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short paragraphs after it read easily.
- 01-harbour · equal · text · s0: 5 @¶0: Four short, evenly sized paragraphs with frequent breaks; the opener asks little, and the slightly longer last one comes once momentum is established.
- 02-release-note · equal · blur · s0: 4 @¶2: Short opening block, even breaks and ample margins make it easy to start, but paragraph 2 is the densest run of full-width lines in a row of uniform blocks.
- 01-harbour · equal · clear · s0: 5 @¶0: Four short, even blocks of three to four lines each with generous breaks; the opening asks little before the first rest.
- 02-release-note · shaped · text · s0: 4 @¶2: A one-line opener draws you in, then a dense five-sentence block is the main ask before the page loosens into short paragraphs.
- 01-harbour · shaped · clear · s0: 4 @¶2: A one-line opening draws you in, but the six-line block right after is the page's heaviest and only real stall point before the shorter, airy paragraphs.
- 01-harbour · dense-open · blur · s0: 3 @¶1: A dense nine-line opening block asks a lot before the first break; the short, airy paragraphs after it read easily.
- 01-harbour · dense-open · text · s0: 3 @¶1: A single dense block of about nine sentences comes before any break, so the reader pays up front, and the white space only arrives with the three short paragraphs after it.
- 02-release-note · shaped · clear · s0: 4 @¶2: A one-line opener draws you in, but the seven-line second block is a heavy ask before the shorter, airier paragraphs that follow.
- 02-release-note · equal · text · s0: 4 @¶0: Four short, evenly sized paragraphs with a modest opening and regular breaks; nothing heavy, though the uniform blocks give the page a slightly flat rhythm.
- 01-harbour · equal · blur · s0: 5 @¶0: Four short, even paragraphs of 3–4 lines with generous white space between them, so no block asks much before a break.
- 02-release-note · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block asks a lot before any white space; the short, airy paragraphs after it come too late to pull you in.
