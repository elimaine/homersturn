<!-- judge gpt-5.6-sol; served: gpt-5.6-sol (no substitution logged for req 9b2ced13); auth 56fbe8cf; 93s; brief agent-reply; X = arm A, Y = arm B (key in runs/judge-key.json, seed 20261103) -->

{
  "instances": [
    {
      "piece": "Y",
      "piece_quote": "I do not know whether the table is written by hand or generated, and a row added by hand to a generated table is gone on the next build.",
      "skill_quote": "In anything but fiction, a detail the brief did not supply: a dinner offered, a season named, a mechanism guessed.",
      "where": "cut"
    }
  ],
  "rules_no_longer_stated": [],
  "other_faults": [
    {
      "piece": "X",
      "rule": "Never invent a claim or number the brief did not supply.",
      "piece_quote": "Nepal is UTC+05:45."
    },
    {
      "piece": "Y",
      "rule": "Never invent a claim or number the brief did not supply.",
      "piece_quote": "The missing row is UTC+05:45."
    },
    {
      "piece": "Y",
      "rule": "In nonfiction, do not add a detail the brief did not supply.",
      "piece_quote": "I do not know whether the table is written by hand or generated, and a row added by hand to a generated table is gone on the next build."
    },
    {
      "piece": "Y",
      "rule": "A reply from an agent should have no recap; do not clarify what the reader already holds.",
      "piece_quote": "The other 209 pass, and the three failures share that one cause."
    }
  ],
  "parallel": {
    "brief_invites": false,
    "X": {
      "parallel": false,
      "name_plant": false,
      "evidence": "There are no characters or mirrored character beats. Nepal is a place supplied by the brief, not a cast name opening a reading."
    },
    "Y": {
      "parallel": false,
      "name_plant": false,
      "evidence": "There are no characters or mirrored character beats. Nepal is a place supplied by the brief, not a cast name opening a reading."
    }
  },
  "better": {
    "verdict": "X slightly",
    "why": "Both add the unsupported offset, but X reports the failure and next-step choice directly, while Y repeats the diagnosis and adds an unsupported mechanism."
  }
}
