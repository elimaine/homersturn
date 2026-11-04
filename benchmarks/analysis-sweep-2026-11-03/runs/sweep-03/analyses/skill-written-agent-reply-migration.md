# Analysis

## 1. Purpose and mindset

**Purpose: a reply from an agent.** There is no greeting, and the first line is the answer ("The payments table is migrated"). It speaks in the first person about work done ("I didn't drop them", "I left untouched") and ends on a decision handed back ("Tell me…"). The genre implies:

- **Dial:** 2 to 3, or 4 by agreement with an orchestrator that reads poetic language.
- **Rules that apply:** the answer first, the last useful point last, no recap, and one ask (borrowed from the message row, since this reply ends on one).

The piece runs at about 4. Its second reading is kept open across all four paragraphs. Nothing on the page shows that agreement, so I took the default of 2 to 3 and judged the layer against it.

**Mindset read: careful, scrupulous, a little ceremonious. Two of five.** The evidence:

- Sentences are balanced and unhurried.
- The only hedge is "nobody I can find".
- The accents go into clearing its own hands: "I didn't drop them and I didn't guess", "Nothing of mine reached them".
- Nothing is walked around except the operational specifics: no table names, no counts.

The writer did not name a mindset, so this is the help mode. Here is one line, "Tell me to claim the pair or let them go, and I'll finish it.", rewritten three ways:

- **Brisk, 1:** "Name a customer for the two rows or tell me to delete them, and I'll finish."
- **Wary, 3:** "I won't decide this one. Attach the two rows to a customer, or delete them?"
- **Decisive, 2:** "Unless you name a customer for them, I'll delete the two rows and finish."

The third changes the default action. Pick it only if that is the policy you want.

## 2. The glance

I counted these by hand because no script or file was given.

| ¶ | Words | Sentences |
|---|---|---|
| 1 | 10 | 1 |
| 2 | 48 | 3 |
| 3 | 29 | 3 |
| 4 | 26 | 2 |

- The total is 113 words. The first paragraph is 9% of it, and the spread runs from 10 to 48.
- The longest block is ¶2, about three phone lines, which the eye can take whole.
- There are no lists, no bold and no subheads, which is right at this length.
- ¶1 and ¶3 both open on "The". That reads as a parallel (the payments, the invoices), not as a hum.

**What the page says unread:** a short status with a decision at the bottom. The shape is sound, and nothing needs fixing before the words.

## 3. The ledger, reconstructed

| ¶ | Raises | Pays | Running debt |
|---|---|---|---|
| 1 | the two rows ("but two") | the status: migrated | the two |
| 2 | the decision ("until you say which way they go"); how hard the search was ("nobody I can find") | the two: orphaned, parked | decision opens; ~31 words to ¶ end |
| 3 | "not one line is settled": settled how? | invoices untouched (never raised) | decision ~60; new open question |
| 4 | nothing | the decision, restated as the ask | decision paid at the last line; "settled" never paid |

Four items need attention:

- **Paid, never raised.** ¶3 answers a question the piece never asked. If the user's task asked it, ¶3 is owed. If not, it is a reveal with no setup.
- **Raised, never paid.** "not one line is settled" and "nobody I can find" (what was searched) are never answered.
- **The ask is made twice.** It closes ¶2 and closes ¶4, against "one ask, once".
- **The opening claim is revised by the end.** ¶1 says "The payments table is migrated". ¶4 says "I'll finish it". The close does not complete the opening; it takes it back.

## 4. The seams

- **¶1→¶2: therefore.** The link is a repeated noun ("but two" → "Those two"). This is the best seam in the piece.
- **¶2→¶3: and then.** The topic jumps from "which way they go" to "The invoices" with no link. The fronted object ("The invoices I left untouched") marks a contrast, but the reader is not yet holding invoices. → Tie it to the scope: "The migration stopped at payments; I didn't touch invoices."
- **¶3→¶4: a faked "So".** ¶4's first sentence does not follow from ¶3. It sums ¶1 to ¶3, so it is a recap wearing a "therefore".

## 5. The five measurements

| ¶ | Band | Stress position spent on | Held question moved? | Feeling, key | Planted line carried |
|---|---|---|---|---|---|
| 1 | lean, a landing as opening | "but two": the exception (well spent) | opens the two | calm, a small tug; low | plants "crossed" |
| 2 | dense | "until you say which way they go": the handoff (well spent) | the two answered; decision opened | care, faintly eerie; low-mid | plants "claimed", "which way they go" |
| 3 | **dense on a beat that owes nothing** | "not one line is settled": an ambiguous negation | none moved; a new one opened | meant as reassurance, lands as unease; mid | carries "carried"/"settled"; nothing returns them |
| 4 | lean, then a land | "I'll finish it": the next action (right for the genre) | the decision restated, not moved | tidy closure; low | echoes "claim", "go" from ¶2 (planted once) |

¶3 is the failure the skill names: a liturgical cadence ("Whatever they carried before, they carry still") spent on a null result.

## 6. Topic position

- **"The invoices I left untouched."** The new topic sits in the topic slot, so the known-new chain breaks. → Open on what the reader holds, which is the migration's scope.
- **"So holding keeps the two"** garden-paths. "Holding" first parses as a gerund (the act of holding keeps them), and only then as the table's name. → Use the table name in a code span.

## 7. Accidental readings

- **Two names for the same move, with opposite truth values.** "every row crossed but two" says the two did not cross. "Those two came over" says they did. → Use one verb, with the destination: "All but two rows are in `payments`."
- **"Crossed" as struck out.** In a migration, "every row crossed" can read as "every row deleted". ¶2 closes this, one line late. → "landed".
- **A synonym cycle.** The rows are called "two", "Those two", "names", "them", "the two" and "the pair". "Names" also reads as the name field. → Say "the two rows" throughout.
- **"settled" is a payments term of art.** "not one line is settled" can read as "every invoice line is unpaid or unreconciled", which is a financial claim the agent may not have checked. → Cut it.
- **The ask is underspecified.** In "Tell me to claim the pair or let them go", claim them for whom? And "let them go" could mean delete them or release them into `payments` without a customer. These are opposite actions on payment data. → "Name a customer for them, or tell me to delete them."
- **"Nothing of mine reached them."** The "of mine" possessive is odd. → "I made no changes to invoices."

## 8. Unearned weight

- **The recap.** "So holding keeps the two, payments keeps the rest, invoices keep themselves." → Cut it, or move it to the top as the status line. Three is the honest count here, so it is not three by reflex, but the genre forbids a recap at the end.
- **Restatement.** ¶3 says "untouched" four ways. → Keep one sentence.
- **The repeated ask.** "held there until you say which way they go" → End ¶2 on "parked in a holding table".
- **Earned, keep it.** "I didn't drop them and I didn't guess who they meant" closes the two fears a reader of a payments migration actually has (lost rows, fuzzy matching). It concedes before the reader is forced to ask.
- There are no dashes, swears, importance claims or colon reveals.

## 9. The three changes that would pay the most

1. **Make the ask unambiguous.** "Tell me to claim the pair or let them go" → "Name a customer for the two rows, or tell me to delete them." This is the one line the user acts on, and right now two of its readings are opposite operations on payment data.
2. **One verb, one count, a status that holds.** "The payments table is migrated; every row crossed but two" → "All but two of [N] rows are in `payments`; the migration finishes when you decide on those two." This fixes the crossed/came-over contradiction, pays a number instead of "every", and stops ¶4 from revising ¶1. Use the real count; I have not supplied one.
3. **Collapse ¶3 to one plain sentence and drop "settled".** "Whatever they carried before, they carry still, and not one line is settled" → "I didn't touch invoices." If invoices reference payments, also say whether those references still resolve. That is the question this paragraph should have answered.

## What the framework does not account for

- **A field built across sentences.** "crossed", "came over", "point at nobody", "waiting to be claimed", "which way they go", "carried", "settled", "let them go". No single sentence carries the afterlife reading (souls ferried across, two unclaimed in limbo awaiting judgment, debts unsettled), but together they assemble it. The reader feels a routine migration turn solemn and a little uncanny. The skill's manifold works per sentence and its ledger tracks discrete raises and payments. A reading that accumulates from vocabulary, never raised in one line and never paid, has no entry. *Inside the model:* it is the manifold at the scale of the piece, and a section on "the field" could say where it may be spent and where it must stop.
- **The plain word that is a term of art.** "settled", "claim", "let go". The skill trusts the common word to carry the second meaning safely and warns only against rare words. Here the common words are near-jargon in payments and data work, so the second sense lands exactly on the operational one. *Inside the model:* it belongs under "one thing, one name" and "the common word", as an exception for words the reader's domain has already claimed.
- **Sound at the phrase level.** "Whatever they carried before, they carry still." This is a chiasmus (carried/carry) with a near-metrical fall. It makes the line memorable and scriptural, which is why it reads as crafted on the sentence that should be plainest. The skill measures rhythm by sentence length and where sentences break, not by stress pattern or echo. *Inside the model* if "rhythm is emotion" were extended to the phrase.
- **Handles for verification.** No table name, row IDs or count appear anywhere ("a holding table", "every row"). The reader cannot check the work or act on it without asking. "A number pays" covers the count, but identifiers are neither numbers nor adjectives. *Inside the model:* it belongs in the agent-reply row as part of what the reader is owed.
- **The semicolon as joiner.** "The payments table is migrated; every row crossed but two." It does the joining the skill bans for the dash. *Inside the model:* the dash rule extends to it unchanged.
- **Register as a trust signal.** The poetic register as a whole makes the reader recalibrate how much to trust every factual claim in the report. A writer visibly choosing cadence over exactness in a payments status loses some credibility on the numbers it did not give. This is a judgment the reader makes about the writer, not a meaning placed or a debt owed. *Outside the model:* the skill has no notion of the writer's credibility beyond "do not invent".
