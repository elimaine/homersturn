<!-- skill 0.4.0; model claude-opus-5-5; served: claude-opus-4-8; brief: You are a coding agent reporting back. The test suite failed: 3 of 212 tests, all in the date parser, because the new timezone table has no entry for Nepal. Write the reply to the developer. -->

## Ledger

```
¶1  owed: the test result (asked)   due now: the result, bad news first
    debt: 0   feeling: calm, steady   state: report 2
    → summary · plain · answer first · no punch
```
[The suite failed: 209 of 212 passed.] [raise: what failed] [The three that broke are all in the date parser, and they share one cause.] [join: therefore] [plant: "one cause"]

```
¶2  owed: one cause (¶1)   due now: name it
    debt: ~25 words   feeling: calm   state: report 2
    → summary · lean · the cause, plainly
```
[The new timezone table has no entry for Nepal, so every parse that resolves to that zone returns null and the assertion trips.] [pay: one cause] [join: therefore] [The other 209 tests don't touch the table, which is why they're green.] [pay: inferred — reader knows green means pass]

```
¶3  owed: the fix (the real ask under "what happened")   due now: route
    debt: 0   feeling: settled   state: report 2
    → summary · plain · end on the action
```
[Add the Nepal row to the table and the three should clear; nothing else looks involved.] [pay: the route] [stress: the action]

## Piece

The suite failed: 209 of 212 passed. The three that broke are all in the date parser, and they share one cause.

The new timezone table has no entry for Nepal, so every parse that resolves to that zone returns null and the assertion trips. The other 209 tests don't touch the table, which is why they're green.

Add the Nepal row to the table and the three should clear; nothing else looks involved.
