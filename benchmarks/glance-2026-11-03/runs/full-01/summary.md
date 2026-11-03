# Glance bench run full-01

inviting: 1 to 5, higher means the shape invites a reader to start and keep going, so higher is better.
Unit: the item (passage); samples averaged within item, shape, mode.

Calls: 162; malformed or failed: 0 (excluded from means, listed below).
- blur check, 01-harbour: 'CANNOT\n\nThe image is too blurred to transcribe exactly. I can make out the general shape of the word'
- blur check, 02-release-note: 'CANNOT\n\nThe image is too blurred to transcribe exactly. The first line might say something like "Thi'
- blur check, 03-letter: 'CANNOT\n\nThe image is too blurred to transcribe exactly. I can make out the shape of a short first li'
- blur check, 04-how-locks-work: 'CANNOT\n\nThe image is too blurred to transcribe the first line exactly. Judging from word shapes and '
- blur check, 05-after-the-match: 'CANNOT\n\nThe image is too blurred to read any line exactly. From word shapes and lengths, the first l'
- blur check, 06-on-naming: '**CANNOT**\n\nThe image is too blurred for an exact transcription. My low-confidence guess at the firs'

## mode: text

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 4.00 | 5.00 | 4.67 | 0.67 | -0.33 |
| 02-release-note | 3.00 | 4.67 | 3.67 | 0.67 | -1.00 |
| 03-letter | 3.00 | 5.00 | 4.67 | 1.67 | -0.33 |
| 04-how-locks-work | 3.00 | 4.67 | 4.00 | 1.00 | -0.67 |
| 05-after-the-match | 3.00 | 4.33 | 4.00 | 1.00 | -0.33 |
| 06-on-naming | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +1.00 (items n=6, bootstrap 95% +0.78 to +1.28); sign test 6 up / 0 down, two-sided p = 0.031

shaped − equal: mean -0.44 (items n=6, bootstrap 95% -0.72 to -0.22); sign test 0 up / 5 down, two-sided p = 0.062 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 18/18; equal: ¶1 named 3/18; shaped: ¶1 named 0/18

## mode: blur

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |
| 02-release-note | 3.00 | 4.67 | 4.00 | 1.00 | -0.67 |
| 03-letter | 3.00 | 4.67 | 4.33 | 1.33 | -0.33 |
| 04-how-locks-work | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |
| 05-after-the-match | 3.00 | 4.67 | 4.00 | 1.00 | -0.67 |
| 06-on-naming | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +1.06 (items n=6, bootstrap 95% +1.00 to +1.17); sign test 6 up / 0 down, two-sided p = 0.031

shaped − equal: mean -0.28 (items n=6, bootstrap 95% -0.56 to -0.06); sign test 0 up / 3 down, two-sided p = 0.250 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 18/18; equal: ¶1 named 0/18; shaped: ¶1 named 0/18

## mode: clear

| item | dense-open | equal | shaped | shaped − dense-open | shaped − equal |
|---|---:|---:|---:|---:|---:|
| 01-harbour | 4.00 | 5.00 | 5.00 | 1.00 | 0.00 |
| 02-release-note | 3.00 | 4.67 | 4.00 | 1.00 | -0.67 |
| 03-letter | 3.00 | 5.00 | 5.00 | 2.00 | 0.00 |
| 04-how-locks-work | 3.00 | 5.00 | 4.00 | 1.00 | -1.00 |
| 05-after-the-match | 3.00 | 4.33 | 4.00 | 1.00 | -0.33 |
| 06-on-naming | 3.00 | 4.00 | 4.00 | 1.00 | 0.00 |

shaped − dense-open: mean +1.17 (items n=6, bootstrap 95% +1.00 to +1.50); sign test 6 up / 0 down, two-sided p = 0.031

shaped − equal: mean -0.33 (items n=6, bootstrap 95% -0.67 to -0.06); sign test 0 up / 3 down, two-sided p = 0.250 (n too small to reach 0.05)

Where the judge said it would stall, share naming the first paragraph: dense-open: ¶1 named 18/18; equal: ¶1 named 2/18; shaped: ¶1 named 0/18

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

- 02-release-note · equal · text · s1: 5 @¶0: Four short, evenly sized paragraphs with regular breaks and a light opening ask little before the first pause.
- 06-on-naming · dense-open · text · s1: 3 @¶1: A dense first block asks a lot before any break; the short paragraphs that follow are easy, but you have to get through the wall first.
- 01-harbour · dense-open · clear · s0: 4 @¶1: A nine-line opening block asks for some commitment before the first break, but the short paragraphs and widening white space after it make the rest read at a glance.
- 01-harbour · shaped · text · s2: 5 @¶0: A one-line opener, then one modest block, then short paragraphs that get lighter toward the end, with white space arriving often enough that nothing feels heavy.
- 02-release-note · shaped · blur · s0: 4 @¶2: A one-line opener draws you in, then a dense seven-line block is the heaviest ask before the short, well-spaced paragraphs that follow.
- 04-how-locks-work · shaped · blur · s0: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the heaviest ask before the paragraphs taper to short, airy lines.
- 04-how-locks-work · equal · clear · s0: 5 @¶0: Four short, even blocks of about four lines each with generous white space between them; the first asks little, and the last is lighter still.
- 02-release-note · shaped · clear · s0: 4 @¶2: A one-line opener draws you in, then a seven-line block is the only heavy ask before the paragraphs taper to short, airy ones.
- 06-on-naming · equal · clear · s2: 4 @¶4: A five-line opener gives way to two light three-line blocks with even spacing, but the closing block swells back to five dense lines before a lone orphaned word.
- 03-letter · equal · text · s1: 5 @¶0: Four short, evenly sized paragraphs with a modest opening and steady white space; nothing heavy blocks the eye.
- 01-harbour · dense-open · text · s0: 4 @¶1: The opening block of about 130 words asks the most before the first break; after that the paragraphs shrink to a few lines and then one, with plenty of white space.
- 03-letter · shaped · clear · s2: 5 @¶0: A one-line opener, then one six-line block as the heaviest ask, then paragraphs that shrink toward a one-line close, with even white space throughout.
- 02-release-note · dense-open · blur · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break; the short paragraphs after it read easily.
- 04-how-locks-work · shaped · clear · s1: 4 @¶2: A one-line opener draws you in, but the six-line second block is the heaviest ask; after it the paragraphs shrink steadily to a one-line close.
- 01-harbour · equal · clear · s1: 5 @¶0: Four short, evenly sized blocks of three to four lines with generous gaps between them; the first break comes almost at once and no paragraph looks heavier than the rest.
- 02-release-note · dense-open · clear · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break; the short paragraphs after it are easy but come only once that wall is crossed.
- 01-harbour · dense-open · text · s2: 4 @¶1: A dense opening block of roughly 130 words asks a lot before the first break, but the short paragraphs after it shrink steadily and leave plenty of white space.
- 02-release-note · dense-open · text · s0: 3 @¶1: A dense opening block asks for the most effort before the first break, while the three short paragraphs after it read easily.
- 05-after-the-match · shaped · clear · s2: 4 @¶2: A one-line opener pulls you in, then a six-line block is the heaviest ask before the paragraphs shorten and the white space opens up again.
- 05-after-the-match · shaped · text · s2: 4 @¶2: A one-line opener pulls you in, but the densest block comes immediately after; the short paragraphs that follow lighten the page again.
- 03-letter · equal · blur · s0: 4 @¶0: Four short, evenly sized blocks of three to four lines with generous white space between them; nothing heavy up front and no dense wall to stall on.
- 02-release-note · dense-open · clear · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break; the short paragraphs after it are easy once you get there.
- 06-on-naming · equal · text · s0: 4 @¶1: The opening block is the heaviest ask before any white space; after it, shorter, even paragraphs with regular breaks carry you down the page easily.
- 06-on-naming · shaped · clear · s2: 4 @¶2: A one-line opener draws you in, but the seven-line block right after it is the page's only heavy stretch before the short, airy paragraphs that follow.
- 05-after-the-match · equal · text · s0: 5 @¶0: Four short, evenly sized paragraphs with a light opening block and frequent breaks; nothing looks heavy enough to stall on.
- 05-after-the-match · dense-open · blur · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short paragraphs and open white space below promise relief.
- 05-after-the-match · dense-open · text · s1: 3 @¶1: A dense opening block demands a lot before the first break, though the short paragraphs that follow pull you through quickly.
- 01-harbour · dense-open · blur · s1: 3 @¶1: A dense nine-line opening block demands effort up front before the page loosens into short, airy paragraphs that would read easily once reached.
- 05-after-the-match · dense-open · clear · s0: 3 @¶1: A dense twelve-line opening block demands a lot before the first break; the short airy paragraphs after it are easy, but you have to get through the wall first.
- 06-on-naming · equal · text · s1: 4 @¶1: The first paragraph is the densest block, but it is moderate and the shorter paragraphs after it break up the page with steady white space.
- 05-after-the-match · dense-open · clear · s2: 3 @¶1: A dense eleven-line opening block asks a lot before the first break, though the short, airy paragraphs after it make the rest of the page effortless.
- 04-how-locks-work · shaped · clear · s0: 4 @¶2: A one-line opener draws you in and the paragraphs shrink toward the end, but the dense seven-line second block arrives right away and is the likeliest place to stall.
- 03-letter · dense-open · text · s1: 3 @¶1: A dense opening block asks a lot before the first break, though the short, airy paragraphs below promise quick relief.
- 03-letter · shaped · blur · s0: 4 @¶2: A one-line opener and generous gaps draw you in, but the six-line second block is the heaviest ask before paragraphs taper to a one-line close.
- 02-release-note · shaped · blur · s2: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the one dense wall before the page relaxes into short, airy paragraphs.
- 05-after-the-match · shaped · blur · s1: 4 @¶2: A one-line opener and generous gaps draw you in, but the six-line second block is the heaviest ask before the page loosens into short paragraphs.
- 01-harbour · shaped · clear · s1: 5 @¶0: A single-line opener pulls you in, the one six-line block is short, and the paragraphs taper to two or three lines with generous white space between them.
- 04-how-locks-work · dense-open · text · s2: 3 @¶1: A dense opening block asks a lot before the first break, though the steadily shrinking paragraphs after it promise an easy, quick finish.
- 03-letter · equal · clear · s0: 5 @¶0: Four short, evenly sized paragraphs of three to four lines each with generous breaks between them; the first asks only four lines before white space and nothing grows heavier after.
- 03-letter · shaped · blur · s1: 4 @¶2: A one-line opener draws you in, then the six-line second block is the heaviest ask before blocks taper to a single closing line amid generous white space.
- 05-after-the-match · equal · blur · s2: 5 @¶0: Four short paragraphs of 3–5 lines with even gaps; the opener asks little, and the slightly longer third block is still light.
- 04-how-locks-work · dense-open · blur · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break; the shorter paragraphs that follow are easy, but the reader has to get through the wall first.
- 04-how-locks-work · equal · blur · s1: 4 @¶3: Four short, even blocks with generous gaps ask little up front, but the third is the densest, with a near-full last line and no visual relief, so the eye may slip there.
- 06-on-naming · equal · blur · s0: 4 @¶0: Four short blocks of 3–5 lines with generous gaps; the 5-line opener is a modest ask and the rhythm stays even, so nothing stands out to stall on.
- 02-release-note · equal · blur · s0: 4 @¶2: Four short, evenly spaced blocks with generous gaps; the second is the densest, with nearly full-width lines and no short tail to rest on.
- 06-on-naming · shaped · text · s1: 4 @¶2: A one-line opener pulls you in, then the second paragraph is the densest block on the page before short, airy paragraphs resume.
- 02-release-note · shaped · blur · s1: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the one heavy ask before the paragraphs taper to light two- and three-line closers.
- 02-release-note · dense-open · text · s2: 3 @¶1: One dense block asks for everything before the first break, then the page falls away into short, uneven fragments.
- 01-harbour · dense-open · text · s1: 4 @¶1: One moderately dense opening block asks the most up front; after that the paragraphs shrink fast and the white space pulls you through to the end.
- 06-on-naming · equal · blur · s1: 4 @¶4: A five-line opener, then two short three-line paragraphs with generous gaps, ease the way in, but the closing five-line block is denser and invites skimming.
- 02-release-note · equal · clear · s0: 5 @¶0: Four short, evenly sized paragraphs of three to four lines with generous breaks, and a brief first block that asks little before the first pause.
- 05-after-the-match · equal · text · s1: 4 @¶3: A modest three-sentence opener and four evenly sized short blocks read easily, though the third paragraph is the densest and the uniform rhythm offers no visual change of pace.
- 02-release-note · shaped · text · s0: 4 @¶2: A one-line opener draws you in, but the dense second block is the heaviest ask before the short, airy paragraphs that follow.
- 06-on-naming · shaped · blur · s1: 4 @¶2: A one-line opening draws you in, then a seven-line block is the heaviest ask before the paragraphs shorten to 3, 3 and 2 lines with generous breaks.
- 02-release-note · dense-open · text · s1: 3 @¶1: A dense opening block holds about two-thirds of the page before any break, while the short paragraphs after it are easy but come only once that first block is done.
- 02-release-note · shaped · clear · s1: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the one heavy wall before the page eases into short, airy paragraphs.
- 04-how-locks-work · equal · text · s2: 5 @¶0: Four short, evenly sized paragraphs with a modest opener and a shorter closer; frequent breaks and little asked before the first one.
- 04-how-locks-work · dense-open · blur · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the shrinking paragraphs and open white space below promise a quick finish.
- 02-release-note · equal · blur · s2: 5 @¶0: Four short, evenly sized paragraphs of three or four lines each, with generous breaks between them and a light first block, so nothing heavy stands in the way.
- 05-after-the-match · shaped · text · s1: 4 @¶2: A one-line opener pulls you in, then paragraph 2 is the densest block on the page; the third is nearly as long, and short closing paragraphs let the page breathe out.
- 05-after-the-match · dense-open · clear · s1: 3 @¶1: An eleven-line opening block asks a lot before the first break, though the short paragraphs after it promise quick, airy reading once you get through.
- 05-after-the-match · equal · clear · s2: 5 @¶0: Four short, evenly sized paragraphs of four to five lines with generous breaks, and the four-line opener asks little before the first pause.
- 01-harbour · dense-open · blur · s0: 3 @¶1: A dense nine-line opening block asks a lot before the first break; the short, well-spaced paragraphs after it read easily.
- 04-how-locks-work · equal · text · s0: 4 @¶0: Four short, even paragraphs with a modest opening block and regular breaks; nothing dense enough to stall on.
- 03-letter · dense-open · clear · s0: 3 @¶1: An eleven-line opening block asks a lot before the first break, though the short paragraphs after it make the rest effortless.
- 05-after-the-match · shaped · clear · s0: 4 @¶2: A one-line opener pulls you in, but the six-line block right after is the heaviest ask before the paragraphs thin into short, airy closers.
- 05-after-the-match · shaped · clear · s1: 4 @¶2: A one-line opener pulls you in, then a six-line block is the heaviest ask; after it the paragraphs shrink and the white space opens up.
- 05-after-the-match · dense-open · blur · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short paragraphs and open white space below promise a quick finish.
- 04-how-locks-work · shaped · text · s1: 4 @¶2: A one-line opener draws you in, but the jump to the densest block right after is the main hurdle, and the shrinking paragraphs that follow make the rest easy.
- 04-how-locks-work · equal · blur · s2: 4 @¶3: Four short, evenly spaced blocks of about four lines each with a light last paragraph, though the uniform rhythm makes the fully packed third block feel like the slowest stretch.
- 02-release-note · equal · clear · s2: 5 @¶0: Four short, evenly sized blocks with generous white space between them; the first is only four lines, so little is asked before the first break.
- 05-after-the-match · dense-open · text · s2: 3 @¶1: A dense opening block asks a lot before the first break; after it, three short paragraphs and generous white space make the rest effortless.
- 04-how-locks-work · shaped · blur · s1: 4 @¶2: A one-line opener draws you in, then a dense seven-line block asks the most before any relief; the paragraphs after it shrink steadily to a short closing line.
- 05-after-the-match · shaped · text · s0: 4 @¶2: A one-line opener pulls you in, and paragraph 2 is the densest block, but it's moderate and the page lightens into short paragraphs after it.
- 04-how-locks-work · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the shrinking paragraphs after it promise an easy finish.
- 01-harbour · dense-open · blur · s2: 3 @¶1: A dense nine-line opening block asks a lot before the first break, though the short, airy paragraphs below promise relief.
- 05-after-the-match · equal · text · s2: 4 @¶3: Short opening and even, modest blocks with regular breaks; the third is slightly the densest, though nothing stalls the eye.
- 03-letter · dense-open · clear · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs below show the page is brief.
- 01-harbour · shaped · text · s1: 4 @¶2: A one-line opener pulls you in, but paragraph 2 is the densest block; after that, short varied paragraphs let it flow easily.
- 04-how-locks-work · dense-open · clear · s1: 3 @¶1: An eleven-line opening block demands a lot before the first break, though the shrinking paragraphs after it promise a quick finish.
- 01-harbour · shaped · blur · s0: 4 @¶2: A one-line opener draws you in, then a six-line block is the only heavy stretch before short, well-spaced paragraphs.
- 02-release-note · shaped · clear · s2: 4 @¶2: A one-line opener draws you in, but the seven-line block right after it is the one heavy lift before the paragraphs shrink to easy two- and three-line pieces.
- 03-letter · equal · text · s2: 5 @¶0: Four short, evenly sized paragraphs with a modest first block and regular breaks; nothing dense enough to stall on.
- 06-on-naming · shaped · blur · s0: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the heaviest ask before the page lightens into short, airy paragraphs.
- 06-on-naming · shaped · text · s0: 4 @¶2: A one-line opener draws you in, but the second paragraph is the only dense block, nearly double any other, before the page eases into short, airy paragraphs.
- 03-letter · shaped · blur · s2: 5 @¶0: A one-line opener, then short blocks that taper (6, 4, 3, 1 lines) with generous gaps; the whole page fits at a glance and nothing is dense enough to stall on.
- 06-on-naming · equal · clear · s1: 4 @¶1: Short page with even breaks; the five-line opening block is the biggest ask, and the lighter three-line middle paragraphs carry you to a closing block of similar weight.
- 06-on-naming · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block demands a lot before the first break, though the short, airy paragraphs after it are easy to finish.
- 02-release-note · equal · clear · s1: 4 @¶0: Four short, evenly sized blocks of three to four lines with generous gaps ask little before the first break, though the sameness gives no visual anchor and the last line ends on a one-word widow.
- 06-on-naming · dense-open · clear · s1: 3 @¶1: An eleven-line opening block asks a lot before the first break; the short, airy paragraphs after it come as relief only once you are past it.
- 03-letter · equal · blur · s1: 5 @¶0: Four short, evenly sized blocks of three to four lines with generous gaps; the opening asks little before the first break and nothing grows heavier further down.
- 04-how-locks-work · equal · clear · s2: 5 @¶0: Four short, evenly sized paragraphs of about four lines each, generous breaks between them, and a first block small enough to start without commitment.
- 05-after-the-match · equal · blur · s0: 4 @¶3: Short, even blocks of 3 to 5 lines with generous gaps; only the slightly longer third paragraph adds weight before the light close.
- 01-harbour · equal · text · s1: 5 @¶0: A modest first paragraph and four short, evenly sized blocks with regular breaks mean little is asked before each pause; the slightly longer last paragraph is still light.
- 04-how-locks-work · equal · clear · s1: 5 @¶0: Four short, even blocks of about four lines each, a modest opening paragraph, generous gaps between blocks, and a lighter final paragraph make it effortless to start and finish.
- 04-how-locks-work · dense-open · clear · s2: 3 @¶1: A dense twelve-line opening block demands a lot before the first break, though the short paragraphs after it promise a quick, airy finish.
- 05-after-the-match · equal · clear · s0: 4 @¶3: Short four-line opener and even breaks invite starting; the third block is the longest at six lines and is the only slight drag before a short closing paragraph.
- 06-on-naming · dense-open · blur · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs after it promise an easy finish.
- 06-on-naming · shaped · clear · s1: 4 @¶2: A one-line opener pulls you in, but the seven-line block right after is the page's heaviest ask before the short, airy paragraphs that follow.
- 02-release-note · shaped · text · s1: 4 @¶2: A one-line opener draws you in, but the second paragraph is the densest block on the page before the shorter ones resume.
- 03-letter · dense-open · blur · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs after it are effortless.
- 05-after-the-match · equal · blur · s1: 5 @¶0: Four short, even blocks of 3–5 lines with generous breaks; the first asks only four lines before white space, and the slightly longer third paragraph is no real obstacle.
- 03-letter · dense-open · blur · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs below promise easy going once you're through it.
- 02-release-note · equal · blur · s1: 5 @¶0: Four short, even blocks of three to four lines with generous gaps; the first paragraph asks little before the first break.
- 04-how-locks-work · shaped · text · s0: 4 @¶2: A one-line opener pulls you in, then the densest block arrives immediately before any break, after which the paragraphs shrink and the page eases out.
- 06-on-naming · equal · clear · s0: 4 @¶1: A five-line opening block is the heaviest ask before the first break; the shorter paragraphs that follow and even spacing make the rest easy to keep reading.
- 03-letter · equal · blur · s2: 5 @¶0: Four short, even blocks of 3–4 lines with generous gaps; the opener asks little before the first break and nothing grows heavier after it.
- 05-after-the-match · equal · clear · s1: 4 @¶3: A short four-line opening and even breaks make it easy to start; paragraph 3, at six lines, is the densest block before the release of the last one.
- 03-letter · equal · text · s0: 5 @¶0: Four short, evenly sized paragraphs with a modest opening and regular breaks ask little before the first pause.
- 01-harbour · shaped · clear · s2: 5 @¶0: A one-line opener asks nothing; the longest block (paragraph 2, six lines) is still short, and the rest taper to two or three lines with generous white space between.
- 03-letter · shaped · clear · s1: 5 @¶0: A one-line opener, a modest six-line block as the heaviest ask, then paragraphs shrinking to a single closing line, with even white space throughout.
- 01-harbour · dense-open · clear · s1: 4 @¶1: A dense nine-line opening block asks a lot before the first break, but the short, airy paragraphs after it are visible and pull you through.
- 03-letter · shaped · text · s0: 5 @¶0: A one-line opener, then three modest blocks that shrink steadily toward a two-line close, with even white space and no wall of text anywhere.
- 01-harbour · dense-open · clear · s2: 4 @¶1: A dense nine-line opening block asks the most before any break, then short, well-spaced paragraphs taper to a single line and carry the eye down easily.
- 04-how-locks-work · equal · text · s1: 5 @¶0: Four short, evenly sized paragraphs with a modest opener and regular white space; nothing reads as a wall.
- 03-letter · equal · clear · s1: 5 @¶0: Four short, evenly sized blocks of three to four lines with generous gaps; the first asks only four lines before a break, and nothing ever thickens.
- 06-on-naming · dense-open · text · s0: 3 @¶1: A dense opening block demands a lot before the first break; the short paragraphs after it read easily.
- 02-release-note · shaped · text · s2: 3 @¶2: A one-line opener leads straight into the densest block on the page, so the effort spikes at paragraph 2 before the later paragraphs taper off.
- 06-on-naming · shaped · text · s2: 4 @¶2: A one-line opener pulls you in, then the densest block comes straight after; the shorter paragraphs that follow ease the pace again.
- 04-how-locks-work · dense-open · text · s0: 3 @¶1: One long dense block demands a lot before the first break; after it the paragraphs shrink quickly and read easily.
- 03-letter · shaped · text · s1: 4 @¶2: A one-line opener pulls you in, and paragraph 2 is the densest block, but the rest taper into short, airy paragraphs.
- 05-after-the-match · shaped · blur · s2: 4 @¶2: A one-line opener draws you in, but the six-line second block is the heaviest ask before the page loosens into short, airy paragraphs.
- 01-harbour · equal · blur · s1: 4 @¶4: Four short paragraphs with even breaks and a light first block, but the last is the densest, four nearly full lines with no short closing line.
- 06-on-naming · dense-open · clear · s2: 3 @¶1: An eleven-line opening block asks a lot before the first break; the short 2-, 3- and 1-line paragraphs after it are light, but you only reach them by getting through the dense top.
- 04-how-locks-work · dense-open · clear · s0: 3 @¶1: A dense twelve-line opening block demands a lot before the first break, though the short, tapering paragraphs below promise a quick finish.
- 04-how-locks-work · shaped · blur · s2: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the heaviest ask before the paragraphs shrink to an easy two-line and one-line close.
- 03-letter · equal · clear · s2: 5 @¶0: Four short, evenly sized blocks of three or four lines with generous breaks between them; the first asks very little before white space arrives, and nothing later is heavier.
- 03-letter · shaped · clear · s0: 5 @¶0: A one-line opener, then short blocks of 3 to 6 lines with generous white space between them, and a one-line close; the six-line second paragraph is the heaviest block but is not heavy enough to stall on.
- 02-release-note · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break; the short two-, two- and one-line paragraphs after it read easily.
- 02-release-note · equal · text · s0: 4 @¶0: A modest opening and four short, evenly sized paragraphs with frequent breaks ask little before each pause, though the uniform blocks give a slightly flat rhythm.
- 06-on-naming · equal · text · s2: 4 @¶1: The first paragraph is the heaviest block, asking the most before any break; after it, short evenly spaced paragraphs keep things moving.
- 03-letter · shaped · text · s2: 5 @¶0: A one-line opener asks almost nothing, the one denser block comes early and is still short, and the paragraphs then taper to a brief close, leaving no point to stall.
- 02-release-note · dense-open · clear · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break, then the page thins into short, airy paragraphs that are easy to finish.
- 01-harbour · equal · text · s2: 5 @¶0: Four short paragraphs of similar size, a light first block, and regular breaks; the last is only slightly longer and never feels heavy.
- 03-letter · dense-open · text · s2: 3 @¶1: A dense opening block asks the most before any break, though the short paragraphs after it are easy to see and pull you through.
- 06-on-naming · shaped · blur · s2: 4 @¶2: A one-line opener draws you in, then a seven-line block is the heaviest ask before the page eases into short, airy paragraphs.
- 06-on-naming · shaped · clear · s0: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the one dense wall before the page settles into short, airy paragraphs.
- 06-on-naming · dense-open · blur · s2: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short paragraphs that follow, ending in a one-liner, look easy.
- 03-letter · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs below promise relief.
- 02-release-note · dense-open · blur · s1: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short, airy paragraphs after it are easy to finish.
- 01-harbour · equal · clear · s0: 5 @¶0: Four short, even blocks of 3–4 lines with generous breaks; the opening asks little before the first rest, and the rhythm never thickens.
- 05-after-the-match · dense-open · text · s0: 3 @¶1: A dense opening block asks a lot before the first break, though the short paragraphs that follow open up with generous white space.
- 06-on-naming · dense-open · clear · s0: 3 @¶1: An eleven-line unbroken opening block asks a lot before the first break, though the short paragraphs that follow are light and easy.
- 01-harbour · shaped · blur · s2: 4 @¶2: A one-line opening draws you in, then a six-line block is the only heavy stretch before the page relaxes into short, well-spaced paragraphs.
- 03-letter · dense-open · clear · s1: 3 @¶1: An eleven-line opening block with no break asks a lot up front, though the short paragraphs below and the brief page overall make it easier to begin.
- 01-harbour · equal · clear · s2: 5 @¶0: Four short, evenly sized blocks of three to five lines with generous white space between them; the first break comes after only four lines.
- 04-how-locks-work · shaped · clear · s2: 4 @¶2: A one-line opener draws you in, but the seven-line second block is the heaviest ask; after it the paragraphs shrink steadily to a single closing line.
- 05-after-the-match · dense-open · blur · s0: 3 @¶1: A dense ten-line opening block asks a lot before the first break, though the short paragraphs below promise quick relief.
- 01-harbour · shaped · blur · s1: 4 @¶2: A one-line opening invites you in, but the six-line block right after is the heaviest ask before the page relaxes into short, airy paragraphs.
- 01-harbour · equal · text · s0: 5 @¶0: Four short, even paragraphs with a modest opener and regular breaks; the slightly longer last one is still light.
- 03-letter · dense-open · text · s0: 3 @¶1: A dense opening block asks a lot before the first break, then short paragraphs make the rest of the page quick and airy.
- 05-after-the-match · shaped · blur · s0: 4 @¶2: A one-line opener and short, airy blocks below make it easy to start; the six-line second paragraph is the only real block, and it is still modest.
- 01-harbour · equal · blur · s2: 4 @¶4: Short opening block, even breaks and generous gaps carry you down, but the final paragraph is a full, flush four-line block with no short closing line, the densest-looking point.
- 06-on-naming · equal · blur · s2: 4 @¶0: A moderate five-line opener, then two short three-line paragraphs and a five-line close, with even breaks and wide margins throughout.
- 04-how-locks-work · equal · blur · s0: 4 @¶3: Four evenly spaced, short blocks with an easy four-line opener; the third identical-sized block is the likeliest spot for a stall before the shorter closing paragraph.
- 01-harbour · shaped · clear · s0: 5 @¶0: A one-line opener draws you in, the only dense block is a modest six lines, and the paragraphs then shorten steadily with generous white space between them.
- 06-on-naming · dense-open · text · s2: 3 @¶1: A dense opening block demands a lot before the first break; the short paragraphs after it read easily.
- 01-harbour · shaped · text · s0: 5 @¶0: A one-line opener, then a single moderate block, then shorter paragraphs that keep shrinking, with frequent white space and no wall of text anywhere.
- 01-harbour · equal · blur · s0: 4 @¶4: Short, even paragraphs of three to four lines with generous gaps ask little up front, but the last block runs full-width to its final line with no trailing air, so it reads slightly denser than the rest.
- 04-how-locks-work · shaped · text · s2: 4 @¶2: A one-line opener draws you in, but the second paragraph is the densest block on the page, and the rest taper to short, easy lines.
- 02-release-note · equal · text · s2: 5 @¶0: Four short paragraphs of similar size with a modest opening and regular breaks, so no block asks much before the next pause.
- 04-how-locks-work · dense-open · text · s1: 3 @¶1: A heavy opening block asks a lot before the first break, though the page thins quickly into short paragraphs and one-line closers.
