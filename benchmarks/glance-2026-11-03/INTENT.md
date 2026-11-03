# The glance bench: intent card and analysis plan

## The request, in Eli's words (2026-11-03, champco session)

> There's another dimension to add as well, and it's related to the
> paragraphs of equal length, which, was a symptom. That is how a page looks
> when a person hasn't read a word. I'm not sure if you have a sense of that,
> or if image models do, perhaps a bench (use Lifthearth Anthropic opus if
> available, lots of usage available that will be reset tomorrow).
>
> For example on last: starting with a dense paragraph is intimidating and
> shuts down a reader.

Same turn: "Which vision" (answered: Claude Opus 5.5's own image input,
through the local proxy). And: "the skill shouldn't rely on image
analysis. The skill is the lite. The heavy we are saving for
champco/humanitieswake/effectco and is private. Image is useful for us to
use to learn, but we should probably distill."

## Piles

- **User instruction**: the quotes above; the route (lifthearth Claude
  login, Opus); the example (a dense opening shuts a reader down); the
  image mode is for learning, the skill stays text-only.
- **Pasted material**: none.
- **My inference**: the three shapes, the blur, the deterministic metrics,
  the 1 to 5 scale, the sample sizes, the sign test.

## The construct

**The glance**: what a page says to a reader before a word is read. In:
the size of the first paragraph, the sizes of the rest and how they vary,
where white space falls. Out: the words, the voice, the meaning, lists and
headings (the items are plain prose so those stay frozen).

## What each test is trying to reveal

1. **Dense opening.** This test is trying to reveal whether a judge, shown a
   page's shape, rates one that opens on a long paragraph as less inviting
   than the same words opened on one sentence. From Eli: "starting with a
   dense paragraph is intimidating and shuts down a reader."
2. **Equal paragraphs.** This test is trying to reveal whether paragraphs of
   equal length read as less inviting than varied ones at a glance. From
   Eli: "the paragraphs of equal length, which, was a symptom."
3. **Who has the sense.** This test is trying to reveal whether a text-only
   judge has the sense at all, and whether an image judge has it more. From
   Eli: "I'm not sure if you have a sense of that, or if image models do."
   *Proposed by me*: the blurred render, so the image judge cannot read the
   words and only the shape is left. What the image judge sees that the
   text judge misses is what the skill must say in words, or measure with
   the shape check in the ledger script, because the skill never sees an
   image.

## The contrast

Varies: the paragraph breaks only. Frozen: every word, in order (the build
asserts it); the font, width and margins of the render; the judge prompt;
the model.

Three shapes per passage:

- `dense-open`: the first 60% of the sentences in one paragraph, then pairs.
- `equal`: paragraphs of about three sentences each.
- `shaped`: one sentence, then five, three, two, and the rest.

Three modes: `text` (the judge reads the text, told to judge by shape),
`blur` (a render blurred until no word can be read), `clear` (the render,
readable; exploratory).

## Outcome

`inviting`, 1 to 5. Higher means the shape invites the reader to start and
keep going, so higher is better. Gradient, not pass/fail. Also
`hesitate_at`: the paragraph the judge would stall on (the first paragraph
named is the dense-opening claim in another form).

## Headline

`shaped − dense-open` on `inviting`, per item, in the `blur` mode: the
shape alone, with nothing else to read. Secondary: the same in `text`
(does a text-only model have the sense). Exploratory: `shaped − equal`,
the `clear` mode, `hesitate_at`, and the deterministic metrics
(`first_share`, `cv`) against the judgments.

## Items

Six passages, synthetic, written for the bench on 2026-11-03, no famous
text, no dates, no real people, no contested facts, different registers
(a scene, a release note, a letter, an explanation, a sports aftermath, a
note on naming). Thirteen sentences each, 170 to 200 words.

Confound screen: no date; no leakage (the words are identical across arms,
only breaks move; in `blur` the words are unreadable); no alignment
triggers; one variable (a break moved can shift sense slightly at the seam,
accepted and noted); floor and ceiling checked in the pilot; not famous;
the truth is a designed ordering, so the human check below is what makes
it a finding; one frozen rendering per arm; JSON of three fields is
answerable.

## Analysis plan (written before the full run)

- Unit: the item. Samples averaged within item × shape × mode.
- Primary: `shaped − dense-open`, `blur` mode. Mean difference with a
  10,000-resample bootstrap over items (seed 7) and an exact two-sided sign
  test over items. With six items all one way, p = 0.031; with five, 0.063.
- Everything else exploratory; no correction claimed.
- Exclusions: a reply with no parseable JSON or an inviting outside 1 to 5
  is listed and left out of means, never silently.
- Sample size: 6 items × 3 shapes × 3 modes × 3 samples = 162 judge calls
  plus 6 blur-readability probes. Pilot first: 2 items, 1 sample, 18 calls.
- Minimum detectable effect, six items, sign test: only a difference that
  goes the same way on every item clears 0.05. Anything less is direction.

## Route

Bare `claude-opus-5-5` through CliProxyAPI, which round-robins the two
Claude logins (lifthearth, elijmaine); subscription usage, no per-call
bill. Steering every call to lifthearth needs an edit to the other login's
auth file, which the session's classifier refused, so the run is split
between the two logins unless Eli adds `"excluded_models": ["claude-opus-*"]`
to the elijmaine auth JSON for the run.

## Instrument validation (the human check)

The judge is Opus 5.5 and has not been checked against a person. Before
any number from this bench goes into the skill as more than "pattern",
Eli rates the 18 blurred pages blind (file names hashed, order shuffled)
on the same 1 to 5 scale and names the stalling paragraph; agreement with
the judge is reported, and the headline recomputed on Eli's labels.

## What the result changes

If the shape moves the judge the way Eli expects: the skill's page-shape
section cites this as pattern evidence that the glance is real for a model
and can be judged from the shape alone, and says it in words a text-only
writer can act on. If it does not: the section stays, on Eli's and the
readers' evidence, and says the model does not share the sense, which
matters because the model is the one writing.
