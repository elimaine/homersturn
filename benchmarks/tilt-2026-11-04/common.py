"""Shared proxy caller for the turns test: the examples bench's caller, unchanged in
route and served-model check, with the arm's references given beside its skill.

One call, no concurrency. The served model is read from the proxy log line whose
request id matches this call's trace header, after the call completes.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
_examples = HERE.parent / "examples-2026-11-03"
sys.path.insert(0, str(_examples))
_spec = importlib.util.spec_from_file_location("examples_common", _examples / "common.py")
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
WRITE_PROMPT, call, piece_of = _mod.WRITE_PROMPT, _mod.call, _mod.piece_of

ARMS = {
    "A": ("skill-0.6.1-frozen.md", ["mindset-0.6.1-frozen.md", "wheel-0.6.1-frozen.md"]),
    "B": ("skill-0.7.0-frozen.md", ["mindset-0.7.0-frozen.md", "wheel-0.7.0-frozen.md"]),
}


def arm_text(arm: str) -> str:
    skill, refs = ARMS[arm]
    parts = [(HERE / skill).read_text()]
    for r in refs:
        name = r.split("-")[0] + ".md"
        parts.append(f'\n<reference name="references/{name}">\n{(HERE / r).read_text()}\n</reference>')
    return "\n".join(parts)
