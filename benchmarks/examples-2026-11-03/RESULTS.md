# Results: do the examples tint the output, and do the rules read without them

The question, in Eli's words: the examples "tint the output"; do the rules
still read without them. Arm A is 0.4.6 with its examples
(`skill-0.4.6-frozen.md`). Arm B is the 0.5.0 candidate with sixteen
particulars cut and each rule stated bare (`skill-0.5.0-stripped.md`,
`cuts.md`). The design and its limits are in `INTENT.md`, which was
written before any call. Every number below comes from the files in
`runs/`.

**In one paragraph.** The tint is real, and it lands in the writer's
working notes far more than in the piece. Ten of twelve arm-A ledgers
carry a cut particular, and none of the twelve arm-B ledgers does.
Taking out the copied ledger format, eight of twelve still carry one:
"strength 1 (phone, bus stop)", "names the loss in the first line" for an
apology, "slams the door", "fear 3 → 4" twice, and "the count as clock"
twice. One or two arm-A pieces carry a particular to the reader, and no
arm-B piece does. Arm B lost one rule the examples had carried: the
arm-B agent reply guesses a mechanism (cut 14), while the arm-A ledger
for the same brief used that example as a checklist ("no mechanism").
The judge preferred arm A on eight of twelve briefs, seven of them
"slightly", but the preferred piece was also the first one shown on
eight of twelve, so position and arm cannot be told apart. In the
read-back, arm A and arm B each had five wrong readings in 114. The one
wrong reading that traces to a cut is Opus on arm B for the figure hums
(cut 9's new wording). On arm B, the name-plant (cut 12) narrowed to an
ironic single name for all three readers. One reply per brief per arm,
an unvalidated judge, and me scoring the read-back: everything here is a
**pattern**, never "clears zero".

## Served models and routes

Each call's model was read from `~/.cli-proxy-api/logs/main.log` after
the call completed, matching the log line by the request id at the end
of the call's `X-Cpa-Trace-Id` header. It is in the first line of every
file under `runs/`.

| role | requested | served | calls | auth |
|---|---|---|---|---|
| writer | claude-fable-5-1 | claude-fable-5-1, all | 24 | dd82b88e (Claude OAuth) |
| judge | gpt-5.6-sol | gpt-5.6-sol, all | 12 | 56fbe8cf (Codex OAuth) |
| read-back | claude-fable-5-1 | claude-fable-5-1 | 2 | dd82b88e |
| read-back | claude-opus-5-5 | **claude-opus-5-5** (no 4.8 substitution this time) | 2 | 931b11e6 (Claude OAuth) |
| read-back, substitute | gpt-5.6-luna | gpt-5.6-luna | 2 | 56fbe8cf |
| read-back | deepseek-flash | **not run** | 0 of 2 | Together key (see below) |
| probes | fable, sol | as requested | 2 | |

That is 42 calls plus two probes, all on subscription and none on an
`anthropic-api/` id. One call was in flight at a time, arm A's twelve
ran before arm B's, and there were no 429s.

**Blocked on Eli.** `deepseek-flash` is `owned_by: together` in
`/v1/models`. That route bills a key, and gate 2 covers subscription only,
so `common.call` refuses it. If you approve the Together key, its two
calls are
`python3 run_readback.py deepseek-flash A` and `... B`, after removing
`deepseek-flash` from `KEY_BILLED` in `common.py`. `gpt-5.6-luna` ran in
its place as a non-Claude reader and is labelled as a substitute
everywhere.

## Test 1: the write side

Twelve briefs, one Fable reply per brief per arm. The judge
(`gpt-5.6-sol`) saw the two clean pieces in a seeded order (seed
20261103, key in `runs/judge-key.json`, unblinded in
`runs/judge-unblinded.json` by `unblind.py`), `cuts.md`, and the
stripped text as the rule list. It never saw the ledgers. I read every
ledger myself, and `grep_tint.py` searched them for each cut's
particulars (`runs/tint-grep.md`). My ruling sits beside each judge
call, and where we disagree it says so.

**How to read the table.** "Instance" means a cut particular carried
into the reply that the brief did not supply. A ledger instance stays in
the working notes, and a piece instance reaches the reader. "Cut rule
broken" means the piece breaks a rule only a cut example stated.
"Better" is the judge's preference between the pieces, with the arm
substituted back in.

| brief | ledger instance (my grep + read) | piece instance (judge → my ruling) | cut rule broken (judge → my ruling) | better (judge) | X was |
|---|---|---|---|---|---|
| apology | **A**: "names the loss in the first line" (cut 4), "a phone, a hurt reader" (cut 5) | none | none | A slightly | A |
| headline | **A**: "strength 1 (phone, bus stop)" (cut 5) | none | none | A slightly | A |
| error | **A**: "read on a phone", "tired" (cut 5); "Ambiguity 1 (an error message)" is the brief's own word | none | none. Judge: A's "Nothing was charged" is an invented claim, a rule both arms state | B slightly | A |
| toast | A: ledger format only | judge: "door" in both ← "who locked the door". **Ruled spurious**: the door is the brief's library | judge: B's opening ends on snow (cut 6). **Ruled spurious**: snow is the brief's fact and the claim | B slightly | B |
| release-note | A: ledger format only | none | none | B slightly | B |
| game-turn | **A**: "state: fear 3 → 4" (cuts 15, 16), "staccato count" | judge: **A** "You count. One. Two. At seven the bed creaks again" ← "a count is the scene's clock" (cut 1). **Upheld, plausible** | judge: A ends on a setting (cut 6). **Ruled not a break**: the soft tallow is the threat, what changed. A also has that rule | A slightly | A |
| agent-reply | **A**: "no test names, no file, no mechanism" (the cut-14 example used as a checklist) | judge listed B's guessed mechanism here; **reclassified** to the next column | **B**: "a row added by hand to a generated table is gone on the next build", a mechanism the brief did not supply (cut 14). **Upheld** | A slightly | A |
| thread-opener | **A**: "a thread opener at 4 slams the door" (cut 4) | none | none | A slightly | B |
| eulogy | none | none | none (judge: B names its own parallel, "the way he held me", a rule both arms state) | A slightly | B |
| insult | none | none | none | B slightly | A |
| parallel-invited | **A**: "Mae fear 3 → 4" (cuts 15, 16) | judge: A "He never said he had been there. She never said she had looked." ← "a thing they refuse to say" (cut 10). **Weak**: a natural move for the brief | none | A much | A |
| single-character | **A**: "due: the count as clock" (cut 1) | judge: both arms count the drips ← "a count is the scene's clock". **Ruled brief-led**: a dripping tap invites counting, and both arms do it | none | A slightly | A |

**Counts.**

- Ledgers carrying a cut particular: A 10 of 12, B 0 of 12. Without the
  ledger-format words copied from the cut-15 filled line ("no punch" in
  8, "staccato" in 3, "restate" in 1; B writes its slot values in its
  own words), A has 8 of 12 and B 0.
- Pieces carrying a cut particular to the reader: A 1 plausible
  (game-turn) and 1 weak (parallel-invited), B 0.
- Pieces breaking a rule that only a cut example stated: B 1
  (agent-reply, cut 14). A 0 that hold up: the judge's two cut-6 calls
  were both ruled out above, and one of them was against A, which still
  has that rule.
- The judge preferred A on 8 and B on 4. The first-shown piece (X) won 8
  of 12. In the eight AB-order briefs A won 6 to 2. In the four BA-order
  briefs it was 2 to 2. Arm and position are confounded, and the
  two-sided sign test on 8 to 4 gives p = 0.39. Direction only, and it
  may be the position.

**Parallel and name.**

| brief | invites a parallel? | parallel in A | parallel in B | name-plant |
|---|---|---|---|---|
| parallel-invited | yes, by design | yes: keys, "hot on the left", the burned tray, bins at four; the unmirrored beat is Walter's truck at the curb and none for Mae | yes: the key, "two, ovens; four, loaves", "just the quiet"; the unmirrored beat is Ruth in the car across the street | none in either |
| single-character | no, by design | no | no | none (both leave the man unnamed) |
| eulogy (judge's call) | judge: yes, a shared nightly situation | no | yes, "his on me … mine under him", which the judge says the narrator then names | none |
| insult (judge's call) | judge: yes, two men | no | no | none |

Both arms staged the parallel when the brief invited it, built it the
same way, and ended on the same unmirrored beat: the old owner watching
or not watching. Neither staged one when it was not invited. The
parallel entry is word-for-word the same in both arms, so this was
expected. It is a check that the figure fires on cue and not by habit,
and on both arms it did. The single-character pieces both imply an
absent woman, which both texts license at mindset 5.

## Test 2: the read-back

Six calls, each asked for When, Not, Example and Misuse on nineteen
entries. That makes 114 entry readings, which I scored against the
0.4.6 entry's text. **I am Opus scoring Opus among others**, so read
Opus's row with that in mind. Only two of the nineteen entries differ
between the arms: F9 (cut 9) and S9 (cut 12). The other seventeen are
word-for-word the same, so arm differences on them are context or
sampling noise.

**How to read the table.** ✓ reads right, ✗ reads wrong, — missing.
"n" marks a reading that is right but narrowed, explained below.

| entry | Fable A | Fable B | Opus A | Opus B | luna A | luna B |
|---|---|---|---|---|---|---|
| F1 recursive paragraph | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F2 litany | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| F3 withheld word | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| F4 crescendo | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| F5 revision | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F6 parallel | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| F7 swear | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F8 dash | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ |
| **F9 figure hums** (differs) | ✓ | ✓ | ✓ | **✗** | ✓ | ✓ |
| S1 character in subject | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S2 one thing, one name | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S3 common word | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S4 opinion on the word | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S5 open on the subject | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S6 one hedge | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S7 example after claim | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| S8 concede; title | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **S9 name as plant** (differs) | ✓ | n | ✓ | n | ✓ | n |
| S10 cliché | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| wrong | 2 | 0 | 0 | 1 | 3 | 4 |

Arm A has 5 wrong and arm B has 5 wrong. Nothing was missing: every
reader answered every entry.

**Every entry that reads wrong, with the reader's words.**

- **F9, Opus, arm B.** "When: On every draft, as a check that keeps each
  device, verb mood and grammatical person under twice a page and out of
  consecutive paragraphs". This puts mood and person under the
  twice-a-page cap. The entry means the opposite: holding one mood and
  one person across the page is the hum. The cut-9 wording "whatever the
  device, down to one verb mood and one person" makes mood and person
  devices, so the cap seems to apply to them. Of the ten wrong
  readings, this is the only one that traces to a cut. The same reader's
  example ("three paragraphs of second-person present, then the fourth
  drops to first-person past where the speaker's state turns") reads
  right, so the misreading is in one line and not in the whole entry.
- **F3, Fable, arm A.** "Example: 'She had always called the house —
  well. She had always called it that.'" This is one break-off dash
  plus "well", which is the dash figure, not three em dashes over a word
  the reader has reached for.
- **S5, Fable, arm A.** "Misuse: 'Monday mornings fell apart for her,'
  where the reader parses the mornings as the actor and must go back".
  Here "Monday mornings" really is the subject, so there is no garden
  path.
- **F2, luna, both arms.** A: "When: Use a prose list whose number of
  items belongs to the scene or the post's content." B: "When: When a
  scene or tic earns a prose list". The entry's "Earned by a scene, a
  tic in a post" means a litany in a post is a tic. luna read the post,
  or the tic, as something that licenses it, on both arms. The phrase is
  the same in both arms, so the ambiguity is in the entry, not the cut.
- **F6, luna, both arms.** A: "Mara returned the borrowed coat clean;
  Eli returned the borrowed key bent." B: "Mara hid the letter in her
  coat; at the station, Ivo hid the ticket in his shoe, but only Mara
  boarded." Both shrink a figure meant for the scale of an arc to one
  sentence, which makes it carried by a line. The entry says "carried by
  beats and never by a line".
- **F8, luna, arm A.** "Example: She lifted the lid—and stopped." This
  is a dash that joins, and the sentence completes. The entry allows the
  dash only where a sentence breaks off before the thing arrives.
- **F3, luna, arm B.** "Example: She reached for the — — —, but the lock
  opened from inside." The word withheld here is one nobody was reaching
  for, which is the entry's own misuse.
- **F4, luna, arm B.** "Not: When the low first step is unnecessary".
  That inverts the entry: "Cut the low first step and the climb is
  gone."

**S9, narrowed on arm B (n).** All three arm-B readers read the
name-plant as a single name whose meaning foreshadows: Fable "a landlord
named Mr. Grice who, four scenes later, keeps the deposit", Opus "a loan
officer named Mercy who never shows any", luna "Mercy signed the
receipt". All three arm-A readers read it as a relation between two
names: Fable "Ada and Ida", Opus "Ada enters on the first page and Zoe on
the last", luna "Mara … Maren". The 0.5.0 sentence ("it opens a reading
before the person has spoken") is true of the ironic single name, so
these are not wrong. But "at the scale of the cast" no longer reads as
two names that say something about each other, and the ironic single
name sits close to the cliché the S10 entry warns about. I count it as
a lost sense, three of three.

**Tint in the read-back.** On the two entries that differ, arm-A
readers' invented examples took the skill's own instances in six of six
cases. For F9, Fable's and Opus's misuse lines are the cut list ("every
paragraph ends on an aphorism and pivots on a word", "the same pivot in
every paragraph, an aphorism closing each one"), and luna's is a reused
frame ("By morning"). For S9, all three are a bracket or a shared sound.
Arm-B readers took none: their F9 misuse lines name a rhetorical
question, a participial phrase in the imperative, a dash. Asked to
invent, a reader on arm A gives the example back.

## Evidence grades

| finding | grade | why not stronger |
|---|---|---|
| Arm-A ledgers carry cut particulars (A 10 or 8 of 12, B 0) | pattern | one reply each; mechanical grep plus my hand ruling, so not judge-dependent |
| Arm-A pieces rarely carry them to the reader (A 1 or 2, B 0) | pattern, instrument-dependent | rests partly on the judge; two of its four piece-instance calls were ruled spurious or brief-led |
| Arm B loses the "no guessed mechanism" check (agent-reply) | pattern, one brief | n = 1; arm A also invented a claim ("Nothing was charged") |
| The judge prefers A, 8 to 4 | instrument | confounded with position (X won 8 of 12); sign test p = 0.39; judge not validated against a human |
| Both arms stage the parallel only when invited | pattern | two designed briefs; the entry is identical across arms |
| Read-back wrong counts equal (5 and 5 of 114) | pattern, instrument | one call per reader per arm; scored by me, an Opus, with Opus a reader |
| The F9 misreading follows cut 9's wording | pattern, one reader | 1 of 3 arm-B readers |
| The S9 relational sense is lost on arm B (3 of 3) | pattern | small, but consistent across three engines |
| Read-back examples copy instances on A (6 of 6), B none | pattern | two entries, three readers |

## The strongest case for cutting the examples, from this evidence alone

The examples are copied. Fable on 0.4.6 put a cut particular into eight
of twelve ledgers where the brief did not call for it. It applied the
griever's "names the loss in the first line" to an apology, the
reader-at-a-bus-stop to a headline, and the angry writer's "slams the
door" to a thread opener. It used the filled ledger line's
"fear 3 → 4" and "no punch" as values. Readers asked to invent an
example handed back the skill's own instance six times in six. On 0.5.0,
none of that appears. What arm B costs is small and repairable: in
quality, nothing the judge can separate from position bias; in reading,
five wrong in 114, the same as arm A. The one cut-traced misreading
(F9) is a wording slip in the new sentence, not a need for an example.

## The strongest case for keeping them, from this evidence alone

Some of the tint is the rule working. Arm A's agent-reply ledger used the
cut-14 example list as a checklist ("no test names, no file, no
mechanism") and its piece guessed nothing. Arm B's guessed how the table
is built. Two of the bare restatements read worse than the examples did:
the figure hums sent Opus to cap mood and person, and the name-plant
lost the relation between two names for all three readers, narrowing to
the ironic single name. The judge leaned to arm A on eight of twelve and
gave its one "much" to an arm-A piece. Most of the tint never reaches
the reader: it stays in ledgers that the final pass strips.

## What I left out, and why

- **deepseek-flash** as a reader: the route bills a key, and gate 2 covers
  subscription only. This is blocked on Eli, and the command is above.
- **A position-swapped judge pass**: the brief specified one shuffled
  order. Without the swap, the 8-to-4 preference is uninterpretable.
- **Human validation of the judge** (benchmark-design phase 2): Eli was
  not watching. My rulings beside the judge's are a second reader, not a
  human check.
- **More samples per cell**: one reply per brief per arm, as briefed. No
  within-arm variance, so no interval.
- **The judge prompt's own example** ("a piece that ends on the weather
  breaks the cut…") may have primed it. Two of its three cut-rule calls
  were cut 6, and I ruled both out. Noted, not rerun.
- **The rhythm pointer confound**: arm B's rhythm rule points at
  `references/mindset.md`, which a writer given only the frozen text
  cannot read. I found no rhythm fault in the arm-B pieces that this
  explains. I did not test it with the reference supplied.
- **Read-back of the other cut sites** (rhythm, the dials, the two
  positions, the punches, the entrance): out of the brief's scope. It
  matters, though, because seventeen of the nineteen entries tested are
  unchanged between the arms.
- **Quality beyond the judge's one-line verdict**: not scored on a
  scale. My own read of the 24 pieces agrees with "slightly" in most
  briefs. I would call parallel-invited closer to even than "A much".

## Proposals, ranked

Do now:

1. **(Recommended first move)** Take the 0.5.0 cut. The tint it removes
   is real and frequent, and the cost it shows is small. Before it goes
   to main, have Fable repair two bare restatements, in direction only,
   since the text is not mine to write. **F9**: make clear that the hum
   is one mood and one person *held* across the page, not a cap of twice
   a page on mood and person. **S9**: restore that a name can say how
   two people stand to each other, without naming a bracket or a sound.
2. Restore the cut-14 rule as a bare rule where the writer will use it:
   in non-fiction, supply no detail the brief did not give, including a
   cause or a mechanism. This belongs in the brief section's "never
   invent" line, not only in the analyze pass. That was the one rule
   arm B broke that arm A's ledger kept.
3. Approve or decline the Together key for the two deepseek-flash
   read-backs, which are one command each.

Later:

4. Rerun the judge with X and Y swapped on all twelve briefs (12
   subscription calls), counting a preference only if it survives both
   orders. This is the only way to read the 8-to-4.
5. Read three or four pairs blind yourself against the judge's verdicts
   (no calls). This is the validation the instrument lacks.
6. Rerun the read-back on the 0.5.0 text after the F9 and S9 repairs,
   and extend it to the cut sites outside the figures and the sentence
   (rhythm, the dials, the two positions, the entrance), since those
   carry fourteen of the sixteen cuts.
7. Fix the litany's "Earned by a scene, a tic in a post", which luna
   misread on both arms. That ambiguity is the entry's, not the cut's.
8. A second writer sample per brief per arm (24 Fable calls). This is
   needed only if the quality question has to be answered rather than
   left at "not detectably worse".
9. Decide whether a frozen `SKILL.md` must stand without `references/`.
   If so, arm B's rhythm pointer needs the shapes back in bare form.
