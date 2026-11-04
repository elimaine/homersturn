# Protocol: skill-size test, 2026-11-03

Route: CliProxyAPI, bare `claude-opus-5-5`, `reasoning_effort: high`,
max_tokens 48000, round-robin over the two Claude OAuth logins.

**Served model.** The proxy log (`~/.cli-proxy-api/logs/main.log`,
`usage_helpers.go:300`) shows that every story in this folder was served
upstream as `claude-opus-4-8` for the requested `claude-opus-5-5`:

| output | written | warning | auth index |
|---|---|---|---|
| runs/slim-slim.md | 19:18 | 19:17:01 | 931b11e6 (lifthearth) |
| runs/slim.md | 19:20 | 19:18:48 | 931b11e6 |
| runs/now.md | 19:22 | 19:20:35 | dd82b88e (elijmaine) |
| runs/v0.3.0.md | 19:37 | 19:37:35 | dd82b88e |
| runs/v0.4.0.md | 20:04 | 20:04:39 | 931b11e6 |

The warning is written when the call completes, beside the request's
200 line, not when it starts: a check made 45 seconds into a two-minute
call sees nothing, which is how the 0.4.0 rerun was first reported as
served by 5.5. Read the log after the call ends. An earlier substitution
at 17:56:32 covers the third blind chinchilla
story of the day. The glance bench and the analysis sweep ran before any
substitution was logged. The three-way comparison is still within one
model; the model is Opus 4.8, not 5.5, and comparisons against the
day's earlier stories cross models. The 0.3.0 and 0.4.0 reruns are both
Opus 4.8, so that pair is within one model. Short probes at 19:53 and the
six-minute self-analysis at 19:46 were served as 5.5 with no warning, so
the substitution is not every call and not the account. Found 2026-11-03 19:55 while checking
the Fable route for Eli.
