# The skill on itself, 2026-11-03

The analyze pass of homersturn 0.3.3 run on the skill's own text, three
times with one prompt (`prompt-0.3.3.md`):

| run | model | route | words | time |
|---|---|---|---|---|
| `runs/0.3.3-claude-opus-5-5.md` | Opus 5.5, high | CliProxyAPI, no substitution logged | 3554 | 357s |
| `runs/0.3.3-claude-fable-5-1.md` | Fable 5.1, high | CliProxyAPI, no substitution logged | 4152 | 329s |
| `runs/0.3.3-claude-fable-5-1-subagent.md` | Fable 5.1, high | a fresh Claude Code subagent, the prompt file its only context | 5335 | 423s |

Eli's prompt for this: "I also wonder if we should reorganize the skill to
show the skill as an example." The three readings agreed on the faults
and differed on the additions. What 0.4.0 took is in
`references/evidence.md` under "The skill on itself". The shape before
and after, frontmatter stripped:

| | 0.3.3 | 0.4.0 |
|---|---|---|
| first paragraph | 131 words | 45 words |
| bold runs | 30 | 0 |
| semicolons | about 30 | 17, all between list items |
| parentheses | about 20 | 9 |
| lines for the narrator | 2 | 0 |

One reading each: pattern, not finding. The check that counts is whether
the skill still writes, which is the chinchilla rerun in
`../skill-size-2026-11-03/runs/v0.4.0.md`.
