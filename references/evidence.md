# Evidence: the tips taken from other guides, and what the model makes of them

Every rule in `SKILL.md` that did not come from the manifold and the ledger
came from somewhere, and that somewhere is listed here with the weight of
its evidence. The stance: a tip is evidence, not canon. It is kept when the
model explains it (where meaning goes, what the reader is owed, what the
page looks like), marked as a convention when it does not, and dropped
when it contradicts the model without a genre to excuse it.

Evidence grades: **measured** (a bench, a study, a test); **authority** (a
named writer on writing); **assertion** (stated in a guide, unsourced).
Most of what follows is assertion. That is the state of the field, and it
is why the skill's own bench exists (`benchmarks/`).

Sources read on 2026-11-03, all on Eli's disk under `~/code/`:
`ai-writing/writing` (ivangdavila/writing v1.1.2; W), `ai-writing/effco-w-style`
(Eli's distillation of effectco's writing checks; E), `ai-writing/humanize`
(Wikipedia's "Signs of AI writing"; H), `ai-writing/no-ai-slop`
(petergyang; N), `elements-of-style-for-agents` (Strunk, CC0; S),
`improve-writing-quality` (Q), `ai-writing/benchmarks/on-structure-and-ai-2026-07-28`
(Eli's bench of those skills; B), and the one study on disk, Sears and
Weisberg, "Bot or not", Judgment and Decision Making 2026.

## The glance

| Tip | Source | The model's account | Evidence |
|---|---|---|---|
| Cap paragraphs at three or four sentences for anything read on a phone; four printed lines are half a screen | W structure, posts | the page the reader sees is the device's; shape is judged at the rendering width | assertion |
| A one-sentence paragraph is emphasis and stops working at three on a page | W structure | a punch stacked is no punch; said per page, not per beat | assertion |
| The first pass is a scroll: the piece must survive being read as subheads and first lines | W posts | the glance is a reading taken before the plain one; in a leaving genre it decides whether any other is taken | assertion |
| Subheads state something; a reader who reads only subheads should get the argument | W structure, posts | the subhead is the ledger's visible column; a label raises nothing | assertion |
| Bold the claim, not the keyword | W posts | bold is a visual punch; spent on a keyword it pays nothing | assertion |
| A list of full sentences that flow into each other is a paragraph in a costume | W posts; N formatting; H inline-header lists | a list is "and then" made visible | assertion, three sources |
| Excess bold and emoji are machine marks | H, N | a second accent system competing with the stress position | assertion |
| Delete the first paragraph and check whether anything was lost; the opening is always overworked | W structure, revision, voice, posts | a dense first paragraph is density where nothing is yet owed | assertion, four files |
| The first forty characters of a title carry the decision in any truncating surface | W structure, emails, posts | a stress position imposed by the surface | assertion |
| One subhead per 200 to 300 words; none under 500 | W structure | convention; numbers unsourced | assertion |
| It must work with formatting stripped | W social | the plain reading stands without the visual accents | assertion |
| A dense opening shuts the reader down | this skill's glance bench (`benchmarks/glance-2026-11-03`, run full-01) | density where nothing is yet owed | measured on Opus: shaped − dense-open +1.06 of 5, six passages of six, p = 0.031; the human check pending |
| A text-only judge sees the wall as well as an image judge does | the glance bench | the glance can be judged from the text, so the skill stays text-only | pattern (text and blur modes agree on every passage) |
| Even blocks invite at a glance; one long block repels; the hum is a reading-time effect | the glance bench | the hum of equal paragraphs is heard in reading, not seen before it | direction only (−0.28 to −0.44 of 5, interval touching zero) |

## The two positions

| Tip | Source | The model's account | Evidence |
|---|---|---|---|
| Begin each paragraph with a topic sentence; end it in conformity with the beginning | Strunk rule 9 (S) | the topic position holds what the reader holds; the stress position holds the change; at the scale of the piece this is the abstract completed by the conclusion | authority |
| Start with the abstract and complete it at the end; a postscript is a thing | Eli's professor, via Eli 2026-11-03 | the abstract is the first raise, the conclusion pays it, the refrain at piece scale; the PS is said after the ledger closes | authority (taught) |
| Place the emphatic words of a sentence at the end | Strunk rule 18 (S); Q principle 13 | the stress position at sentence scale | authority |
| Topic position: old, known information; stress position: what the reader will remember | W clarity; Gopen and Swan | the two slots, named | authority |
| The known-new chain: each sentence starts on what the last ended on; when a paragraph reads twice, check this first | W clarity; Gopen and Swan | the ledger at sentence scale: the topic slot re-presents what was just paid | authority |
| Open with the sentence that states the job; a point in the last sentence works in an essay and fails in anything skimmed | W structure | a genre split: the reader who can leave is owed the point at the top | assertion |
| Front-load only when it improves clarity; do not force every paragraph into one shape | N editing principles | topic-first is a choice per paragraph, not a template | assertion |
| Every paragraph the same length, each opening on its topic sentence, is a machine tell | W clarity | the template is the hum | assertion |
| The repeated-noun link beats every connective | W structure | the seam is a known-new join; it never lies about the relation | assertion |
| Never end a sentence on a qualifier | W clarity | the stress position spent on a hedge | assertion |
| Examples after the claim; definitions one paragraph before use | W structure | a detail before its promise has nothing to carry it; pay just before it is due | assertion |
| Restating the prompt, announcing the structure, a dictionary definition, a rhetorical question: banned openings | W structure, clarity; N; Q | a sentence about the piece raises nothing in the piece; a question raises a promise the reader can decline | assertion |
| The opening's job is to make the second sentence unavoidable; written last | W structure, posts | the opening's only debt is to the next line | assertion |
| Passive voice is right when the receiver must hold the topic position | W clarity; S | the topic slot belongs to the thing the reader is holding | authority (Gopen-style) |

## Purpose

| Tip | Source | The model's account | Evidence |
|---|---|---|---|
| Every structural rule follows from one asymmetry: an email's reader has a reason to finish, a post's reader does not | W posts | the balance a reader will carry depends on whether they can leave; the whole genre table derives from this | assertion |
| Withholding the conclusion works in fiction and loses non-fiction readers | W posts | the reveal is held for readers who stay | assertion |
| Never make the reader hold more than one open loop | W structure | true for the leaving reader; the staying reader carries several | assertion |
| If the piece has a counterintuitive claim, the hook is the claim; do not save it | W posts | the leaving reader gets the claim first | assertion |
| Format budgets (email 50 to 150 words, blog 800 to 1500, essay 1500 to 4000, memo BLUF, exec summary SCQA, X 280) | W SKILL | convention; the essay row ("the tension, not the thesis; the turn earned, not announced") matches the model | assertion; Minto for SCQA |
| Shapes by purpose: BLUF, SCQA, inverted pyramid, question-attempts-turn, criteria-first; one shape per piece | W structure | each shape is a schedule of when the main promise pays | assertion; Minto |
| Reading time is words over 240; speech is words over 140 | W SKILL; Rayner | measurement | authority |
| Prose to be read rewards compression; prose to be heard needs redundancy | W SKILL, revision | the refrain costs nothing because the words are the reader's; a listener cannot go back | assertion |
| A reader who stops after the first paragraph must act correctly | W workplace | the whole debt paid by the first stress position in a decision document | assertion |
| One ask, once, in the first screen; context after the ask | W SKILL, emails | in a message the ask is the only thing owed | assertion |
| Bad news: the news, the cause in one line, what happens next; delaying adds the discovery that you delayed | W emails | withholding is earned only when the reader will pay for the wait | assertion |
| Line one carries the payload; a thread with the payoff in the last post is never reached | W social | same asymmetry | assertion |
| Does the piece exist to transmit a conclusion or to reach one | W SKILL, drafting | a piece that reaches keeps the reveal open; one that transmits pays up front | assertion |
| Endings: consequence, next action, callback, the hard sentence, open question (exploratory only) | W structure | land, next action (genre), refrain, land, release | assertion |
| A blocked or failed beat still gives a fact, a cost, a reaction, a threat, a route, or a decision | E interactive profile | every turn pays or the player carries debt into the next input | assertion, from effectco's engine tests |
| Keep implementation language out of reader-facing prose; translate IDs, state and scores into consequences | E SKILL, principles | machinery is a reading the reader cannot complete | assertion |
| Give the actual words when dialogue matters | E | a bargain or refusal is a scene beat, not summary | assertion |
| Agent replies: begin with the answer, end with the last useful point; no preamble or closing | S; Q | the asking reader is owed the answer at the top | assertion |
| Let code and non-prose artifacts follow their own conventions | S | out of the model's scope | assertion |

Nothing on disk covers UI copy. The row in the skill's table is the
model's own derivation (a reader mid-task is owed the one thing to do) and
is unsourced.

## The sentence

| Tip | Source | The model's account | Evidence |
|---|---|---|---|
| Character in the subject, action in the verb | W clarity; E; N; S rule 10; Q; Williams | an abstraction in the subject slot hides who acts, opening readings nobody will pay | authority (Williams, Strunk) |
| Un-nominalise: -tion, -ment, -ance, -ity, -ness; the verb form is the sentence | W clarity; Q | same | assertion, Williams-derived |
| Ambiguous pronoun, dangling modifier, stacked nouns, false range, negation scope | W clarity; S; Q | readings opened by accident: a manifold the writer did not choose | assertion; Strunk for pronouns |
| One thing, one name; elegant variation is a comprehension failure | W clarity, style-guide; E; H; N; S | a renamed thing is a new referent raised that nothing pays | assertion, six sources |
| One strong sensory anchor per beat; no stacked adjectives, metaphors or lore | E | the sign that raises is one detail, not a pile | assertion |
| One hedge per claim; keep the hedge that changes the truth | W; E; N; Q | a hedge is a reading kept open on purpose; a second opens nothing | assertion, four sources |
| Adverbs: cut the -ly that props a weak verb; keep only, rarely, almost, nearly | W; King | the carrying adverb is the claim | authority (King), assertion |
| Cutting formulas (in order to, due to the fact that, it is important to note) | W; E; H; Q | plain where nothing is owed | assertion, identical lists |
| Fake-strong verbs (serves as, stands as, boasts) | H; N | a raised importance never paid | assertion |
| Negative parallelism, "not X but Y" | H; N | a denied reading the reader never held | assertion |
| The rule of three by reflex | H; W clarity | the litany is the earned version; the tricolon the unearned | assertion |
| Importance puffery (pivotal, a testament to) | H; N; E; S | a punch where nothing was owed | assertion, four sources |
| The -ing tail that explains (highlighting, reflecting) | H; N | points at the planted meaning | assertion |
| Weasel attribution (experts believe) | H; N | a promise with no payer | assertion |
| The colon before a dramatic reveal | N | a manufactured stress position mid-sentence | assertion |
| Faux-insight setups (what most people miss) | N | promises a reveal, pays an ordinary claim | assertion |
| Fake-profound kickers: delete, do not rewrite into a better metaphor | N | the punch where nothing is owed; in a post nothing is owed at the end but a consequence | assertion; B's single rater rewarded the consequence ending |
| Summary and recap endings | N; W; H | the stress position spent on nothing | assertion, four sources |
| A number with a source beats an adjective; protect the specific fact | W posts; N; E | a number pays; an adjective raises | assertion |
| Concede before you are forced to | W structure, posts | close the reading the reader would open | assertion |
| Strongest argument first, second-strongest last | W structure | the stress position at the scale of the piece | assertion; the serial-position effect is real but uncited there |
| A title makes a promise the piece must pay; write it after | W structure, posts | the first raise | assertion |
| Never invent a claim, a number, an opinion, or an experience the person did not supply | W voice; E; N | outside the model; fidelity | assertion; B measured the cost (the humanize arm invented experience) |
| Metaphor when it clarifies; never to avoid saying what happened | S; E | a second reading is earned where something is raised | assertion |
| Introduce a concept plainly before relying on its name; no coined terms | S; Q | a coined term is a reading the reader cannot pay | assertion |
| Put statements in positive form | Strunk 11 | a negation raises the thing denied | authority |
| Parallel form for coordinate ideas | Strunk 15; Q | the refrain at phrase scale, recurrence that costs nothing | authority |
| Keep related words together | Strunk 16; Q | distance opens a wrong reading | authority |
| Read aloud; the place you stumble is the place to cut | W; B rubric | the ear hears the rhythm the eye reads past | assertion; a rubric dimension in B |

## Process (outside the model, kept as practice)

- Revision passes in order: structure, cut, clarity, voice, proof. Polishing
  a sentence the structure pass would have deleted is the common waste (W).
- The cut order: whole sections, the first paragraph, the summary
  paragraph, restating sentences, qualifying clauses, formulas, adjectives
  last (W; King's ten percent).
- Reverse outline: one verb per paragraph; two with the same job merge; a
  paragraph whose job is "transitions" goes; every entry "explains" means no
  argument (W). The nonfiction twin of the paper ledger.
- Zero draft before editing; write the ending first; `[TK]` for what is
  missing (W).
- Stop revising when two passes produce only synonym swaps; a reversed
  change two passes later means the problem is structural (W).
- Beta readers: ask for the place, not the opinion ("where did you stop,
  reread, skim?"); weight what they felt, discount what they prescribe (W).
  The place a reader rereads is a stress position misspent.
- Feedback in tiers: blocking, substantive, preference; more than a fifth
  preference means you are rewriting in your own voice (W).
- Forced choice: two variants that differ on one dimension; the pick is the
  signal; never three (W). Poet works this way.

## Contradictions, and how the model rules on them

1. **Topic sentence first** (Strunk, W, Q, N) against **the end carries the
   change** (this skill). Both, by genre: the reader who can leave is owed
   the point at the top; the reader who stays is owed it at the bottom. The
   end still carries the change in both.
2. **One open loop** (W) against a ledger carrying several. Genre: one for
   the leaving reader, several for the staying one.
3. **Do not save the claim** (W posts) against holding the reveal. Genre.
4. **Delete the kicker** (N) against the punch. Reconciled: the punch is
   earned only where something is owed; a post owes a consequence at the
   end and nothing else.
5. **Complete sentences, no fragments** (N; Strunk 6) against the musical
   sentence and the staccato rhythm. Earned by a scene, a tic in a post.
6. **Vary sentence length, flag three in a row within three words** (W, N,
   H) against **do not switch rhythm inside an engaged scene**. B measured
   it: the triplet rate did not track judged quality (the best arm had the
   highest rate, the worst the lowest). The model's framing holds.
7. **Dash caps**: per piece (N) against per paragraph (this skill). Same
   direction; the paragraph is the unit here because the dash is a rest.
8. **Hedge lists** that include perhaps, arguably, rather (Q's script)
   against "keep the hedge that changes the truth" (W, E, N, Q's own
   reference). The reference wins; the list is a trigger to look.

## What the benches say

- **B** (one essay, six rewriting arms, one rater, unblinded): the
  integrated arm won on quality (96 of 100) and the no-ai-slop arm was the
  best single; humanize scored highest on voice and invented experience
  the author never had. Regex slop counts went to zero for every
  skill-driven rewrite, so they cannot rank skills. The uniform-triplet
  rate did not track quality. Single item, single rater: pattern, not
  finding.
- **Bot or not** (Sears and Weisberg 2026; N = 1,682 and 905): readers
  rated the AI story higher in quality and absorption than the human one,
  rated whichever they were told was human higher, and could not tell
  which was which (below chance). Readers who said they relied on the
  language were wrong two-thirds of the time. The authors' account: AI
  output averages tendencies and smooths rough edges, the way averaged
  faces are judged more attractive, and is homogeneous across a body of
  work. For this skill: "reads as human" is not a target; word lists catch
  what editors notice, not what readers feel; the hum is rated well on one
  short piece, so a bench must measure absorption over length, the payment
  of a planted promise, and variance across many outputs.
- **The analysis sweep** (`benchmarks/analysis-sweep-2026-11-03`): the
  skill's analyze mode run by Opus over six good passages, six machine
  passages and four pieces the skill wrote, each asked what the framework
  does not account for; 28 candidates and 23 contradictions, of which
  nineteen were conceded into the skill (voices other than the writer's,
  honest joins, tells judged forward, the other joiners, rhythm as a
  clock, cliché and exactness, comedy, the trust fillers, renaming as
  payment, the rare word as carrier, the loaded common word, the
  parenthesis, the crescendo, the convention exemption, four purpose rows,
  the off-page payment) and sound was named as outside. Grade: instrument.
  RESULTS.md there has every ruling.
- **The glance bench** (`benchmarks/glance-2026-11-03`): the same words
  broken three ways, judged by Opus 5.5 from the text, from a blurred
  render, and from a clear render. Its intent card and analysis plan are
  in the folder; its findings are written into the skill only after the
  human check.
- **The skill-size test** (`benchmarks/skill-size-2026-11-03`): one blind
  story per skill length (108, 315 and 685 lines), same brief, Opus at
  high effort, the skill as the only instructions. The 315-line text gave
  the best story and the cleanest page (one repeated frame against eight,
  spread 0.42 against 0.57 and 0.70); the 685-line text opened its second
  paragraph on a 107-word wall and told the fight in a sentence. One story
  per arm: direction, not finding. Version 0.3.0 is the 315-line text.
  Eli's read of the short-skill story gave four rules (opinion on the
  word, not a trailing clause; the garden path; the accidental reading
  that agrees is a gift; the refrain pays the largest debt and a shadowed
  thing is paid by an action). Grade: pattern. A rerun on the adopted
  text (`runs/v0.3.0.md`) gave both characters an entrance with a spoken
  line, and copied the skill's own example sentence word for word into
  the story: a quoted example in a rule is reproduced whenever the brief
  is near it, so 0.3.1 describes the pattern and quotes no line.

## Detectors worth borrowing for the analyze mode

- Name the pattern, quote the line, give the fix; do not score; do not
  guess authorship (N). The output shape the skill uses.
- Structural tells over lexical ones: uniform rhythm, the tricolon reflex,
  hedge stacking, symmetrical paragraphs, the both-sides close, restating
  the prompt, abstract subjects, announced structure, empty intensifiers,
  the summary that adds nothing (W). "A word list gets stale; these
  patterns do not."
- Paragraph-opening fingerprint: the first six content words of
  neighbouring paragraphs compared (E's checker). In `--shape`.
- Per-paragraph readability outlier, never a target number (W).
- The subject-slot tally and the concreteness ratio (W voice).
- Delete-the-first-paragraph and delete-the-last-paragraph tests (W).
- The transitions table: however between compatible claims, therefore
  without entailment, three alsos in a row (W).
