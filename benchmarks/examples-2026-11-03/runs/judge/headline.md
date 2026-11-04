<!-- judge gpt-5.6-sol; served: gpt-5.6-sol (no substitution logged for req 6f7c5021); auth 56fbe8cf; 36s; brief headline; X = arm A, Y = arm B (key in runs/judge-key.json, seed 20261103) -->

{
  "instances": [],
  "rules_no_longer_stated": [],
  "other_faults": [
    {
      "piece": "Y",
      "rule": "A post owes the reader the full claim at the top.",
      "piece_quote": "Fourth Street Bridge Closes Monday"
    },
    {
      "piece": "Y",
      "rule": "A post should end on a consequence rather than merely completing the factual recap.",
      "piece_quote": "Repairs will keep it closed for six months."
    }
  ],
  "parallel": {
    "brief_invites": false,
    "X": {
      "parallel": false,
      "name_plant": false,
      "evidence": "There are no characters or character names; “Fourth Street” identifies the bridge."
    },
    "Y": {
      "parallel": false,
      "name_plant": false,
      "evidence": "There are no characters or character names; “Fourth Street” identifies the bridge."
    }
  },
  "better": {
    "verdict": "X slightly",
    "why": "X puts the closure, start date, duration, and reason in the headline, then uses the first line for the practical consequence; Y divides the core claim and largely restates it."
  }
}
