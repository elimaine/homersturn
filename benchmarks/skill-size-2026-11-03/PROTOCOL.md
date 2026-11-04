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

An earlier substitution at 17:56:32 covers the third blind chinchilla
story of the day. The glance bench and the analysis sweep ran before any
substitution was logged. The three-way comparison is still within one
model; the model is Opus 4.8, not 5.5, and comparisons against the
day's earlier stories cross models. Found 2026-11-03 19:55 while checking
the Fable route for Eli.
