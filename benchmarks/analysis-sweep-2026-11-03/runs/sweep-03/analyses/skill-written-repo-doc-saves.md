# Analysis: "Saving and undo"

## 1. Purpose and mindset

**Genre: an end-user help doc** (the repo doc row). The evidence is an H1 that works as a label, second person, and imperatives ("use the undo button", "Hold", "Click", "reopen it"). There is no ask, no scene, and no code spans or paths, so it is help for users rather than a spec.

- **Dial: 1.** Nothing here should be held.
- **Rules that apply:**
  - The answer goes where the reader will look.
  - One name for one thing.
  - The smallest valid structure.
  - End on the last useful point.
  - Nothing withheld.
- **The reader** can leave and came for one thing, most likely one of three: where is the save button, how do I undo, I closed the tab.

**Mindset: calm and explanatory, 1.** Sentences run 7 to 30 words and break evenly. There are no hedges and no accents. The fear (losing work) is named in the second sentence, not walked around. No target mindset was given, so this is the help mode. Here is ¶5 three ways; pick by ear:

- **Calm, as written (1):** "If you close the page by accident, reopen it and the draft is there, as of the save made when you left."
- **Steady, for a reader who just panicked (2):** "If you closed the page by accident, reopen it. Your draft is there."
- **Exact, engineer-cautious (2):** "Reopening the page loads the save made when you left it."

## 2. The glance

These counts are by hand. The piece is under a page, so the script is not needed.

| ¶ | words | sentences |
|---|---|---|
| 1 | 22 | 2 |
| 2 | 79 | 4 |
| 3 | 29 | 2 |
| 4 | 40 | 3 |
| 5 | 22 | 1 |

- Total 192 words. The first paragraph's share is 11%.
- Lengths spread from 22 to 79. The longest block is ¶2, at 41% of the piece.
- There are no lists, no bold, no subheads, and no repeated openings.

**What the page says unread:** short and easy to start. The opening passes; the eye takes it whole. **¶2 is the next wall**, about 12 lines at phone width, and it is marked for the block.

The title is a label. For a doc that is defensible, since it is what the reader searches for. But a reader of the title and first lines learns "it saves for you" and nothing about undo, which is half the title.

## 3. The ledger, reconstructed

| ¶ | raises | pays | debt |
|---|---|---|---|
| title | saving; undo | | |
| 1 | how does it save? | saving (the claim); "you do not lose work" | ~0 |
| 2 | "a save" as a thing (noun) | how: two triggers, with numbers | ~0 |
| 3 | "one click" (what do two do?) | undo, on paper | ~0 |
| 4 | what an entry shows; how far back; what restoring does to the current draft | going back further than one save; "a save" as a list entry | ~0 |
| 5 | | repays ¶1 through ¶2's leaving trigger | 0 |

**Raised and never paid:**
- What a second click does.
- What happens to the current draft when you restore.
- What an entry shows, and how far back the list goes.

**Paid and never raised:** none.

**The collision.** ¶2: "two seconds after you stop typing, the editor writes the current draft to a save." ¶3: "One click rolls the draft back to the last save."

Read together, with "last" meaning most recent, one click returns the reader to what is already on screen. At most it takes back two seconds of typing. The payment the reader came for ("take back my mistake") looks paid and is not.

## 4. The seams

- **¶1→¶2: therefore.** The noun repeats ("save button" → "A save"). Good.
- **¶2→¶3: and then.** The join is the title's "and". This unwritten join is exactly where the bug lives. Write it as a therefore ("Because every pause is a save, one click…") and the writer hits the contradiction.
- **¶3→¶4: but** ("instead of clicking it"). The noun repeats ("undo button"). Good.
- **¶4→¶5: and then.** ¶5 picks up ¶2's "close the page", three paragraphs back. Its shape is the abstract completed: ¶1's "do not lose work" becomes "the draft is there". That shape suits a paper. In a doc it puts the panicked reader's answer last.

## 5. The five measurements

| ¶ | band | stress position spent on | held question moved | feeling, how keyed | planted line carried |
|---|---|---|---|---|---|
| 1 | plain | "forgetting to": the weight sits on an elided verb | raises *how* | reassurance, low | "you do not lose work" (paid ¶5) |
| 2 | lean | the perceptible consequence ("kept exactly as you left it"): earned | pays *how* | confidence, low | "as you left it" (→ ¶5 "when you left") |
| 3 | plain | mechanism restated ("most recent pause or exit") | answers *how far back*, wrongly or ambiguously | should be relief; confusion if the reader does the sum | "last save" |
| 4 | plain | the next action ("restore the draft to that save"): right for a doc | pays *further back* | control, low | none new |
| 5 | plain | mechanism ("the save made when you left"), with the consequence buried mid-sentence | none; it repays | relief, but late | "left" from ¶2 |

## 6. The topic position

- **Read twice: "writes the current draft to a save"** (¶2). "To a save" makes the save a container, so the reader reparses. Fix: "saves the draft."
- **¶3 opens on something new** ("To step back") while the reader still holds "kept as you left it". This is acceptable as a section turn in a doc, but nothing carries it. A subhead or a written join would.
- **The rest of the chain holds.** ¶4 opens on the undo button, which the reader already holds. ¶5 opens on closing the page, held from ¶2 but distant.

## 7. Accidental readings

- **One name for three things:** "save" is the act, the snapshot ("to a save"), and the button. Fix: give the snapshot its own noun and keep "save" as the verb.
- **One thing under five names:** "leaving", "navigate away", "walk away from", "the page goes", "exit", "left".
  - "Walk away from" also reads as leaving the desk with the tab open.
  - "Exit" also reads as quitting the browser.
  - Fix: "leave" throughout.
- **"the last save":** most recent or previous? Fix: say which, from the product.
- **"One click":** the number invites counting. Fix: say what each further click does.
- **A trailing participle:** "returning you to the state at your most recent pause or exit". It restates the clause before it and so restates the contradiction. Fix: cut it, or replace it with what one click discards.
- **"in order":** small. Fix: "newest first", and drop "with the newest at the top".

## 8. Unearned weight

There is little.
- No importance claims, bold, joining dashes, kickers, or swears.
- The colons in ¶2 define; they do not reveal.
- **¶2's "So…" sentence** restates the triggers, but it translates mechanism into what the reader perceives. Keep it.
- **¶5 restates** ¶2's last clause. That is the one real recap.
- **Two stress positions are spent quietly:**
  - ¶1, "by forgetting to." Fix: "There is no save button, so forgetting cannot cost you work."
  - ¶5, "the save made when you left." Fix: "reopen it, and your draft is there."

## 9. The three changes that would pay the most

1. **Resolve the undo contradiction.** "One click rolls the draft back to the last save, returning you to the state at your most recent pause or exit." By ¶2, that state is the current one. Fix: state which save one click reaches and what it discards. This is a fact only the writer can get from the product; go and look.
2. **One name for one thing.** "Writes the current draft to a save" / "save button" / "walk away from" / "exit". Fix: give the snapshot a noun of its own, keep "save" as the verb, and use "leave" for every exit.
3. **Pay the reader at the moment of commitment.** "Click an entry to restore the draft to that save." This is the reader's last step before an irreversible-looking act. Fix: say what becomes of the current draft and whether the restore can itself be undone. Concede before they are forced to ask.

## What the framework does not account for

- **The sum the reader computes.** ¶2's "two seconds after you stop typing" plus ¶3's "One click rolls the draft back to the last save". Each sentence is clear alone. The reader who adds them gets "undo does nothing", and the reader who tries it gets the same result. The skill's accidental readings are all sentence-local (pronoun, modifier, scope).
  - **Inside the model, if a section were added:** a reading made by combining two clean payments is still "where meaning goes". It would also price a cost the skill leaves out of "a number pays": a number is a payment the reader can audit, so every number has to agree with every rule.
  - **Outside the model:** whether either sentence matches the product. The model reads the page, not the software.
- **The borrowed word.** "To step back, use the undo button." "Undo" arrives with behaviour from every other program: step back one edit, repeatably, probably Ctrl-Z too. The doc redefines it as a rollback to a snapshot without closing that reading. The skill's rule ("the common word… in the words they would use") pushes toward exactly this word and does not name its failure: the common word that brings a behaviour the thing does not have.
  - **Inside the model:** this is a manifold whose dominant reading is supplied by other software, not the page. A section on the convention a word carries would cover it.
- **Absolute claims about the world.** "You never press a save button", "kept exactly as you left it", "before the page goes". A reader trusts these and stops guarding their work. If a save on leaving ever fails, the whole page loses its credit, not just that line.
  - **Inside the model, partly:** "Concede before you are forced to" could be extended to failure modes.
  - **Outside the model:** whether the claim is true.
- **What works, and is only half-named.** "So a draft you are working on stays current within two seconds of your last keystroke." Here mechanism is translated into what the reader perceives. The skill names this only in the game-turn row. The doc row should carry it too; that gap is inside the model.
