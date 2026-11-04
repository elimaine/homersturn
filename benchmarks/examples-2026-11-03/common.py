"""Shared proxy caller for the examples test.

One call, no concurrency. The served model is read from the proxy log line
whose request id matches the tail of this call's X-Cpa-Trace-Id header,
after the call completes, so another session's substitution cannot be
mistaken for this one's. The key is read by analysis_sweep.proxy_key() and
never printed.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "analysis-sweep-2026-11-03"))
import analysis_sweep as a  # noqa: E402

LOG = pathlib.Path.home() / ".cli-proxy-api/logs/main.log"
FORBIDDEN = ("anthropic-api/",)
KEY_BILLED = {"deepseek-flash", "deepseek-v4-pro", "deepseek-flash-china", "deepseek-v4-pro-china"}
WRITE_PROMPT = a.WRITE_PROMPT  # unchanged from the briefs bench


def served_for(model: str, req_id: str) -> str:
    # The warning is written as the call completes; give it a moment.
    for _ in range(5):
        for line in LOG.read_text(errors="replace").splitlines()[-4000:]:
            if f"[{req_id}]" in line and "served model" in line:
                m = re.search(r'served model "([^"]+)" for requested model "([^"]+)"', line)
                if m and m.group(2) == model:
                    return f"served: {m.group(1)} (substituted; log req {req_id})"
        time.sleep(1)
    return f"served: {model} (no substitution logged for req {req_id})"


def call(model: str, text: str, max_tokens: int = 48000, effort: str = "high") -> tuple[str, str, float]:
    if model.startswith(FORBIDDEN) or model in KEY_BILLED:
        sys.exit(f"refused: {model} bills a key; gate 2 covers subscription routes only")
    body = json.dumps({"model": model, "max_tokens": max_tokens, "reasoning_effort": effort,
                       "messages": [{"role": "user", "content": text}]}).encode()
    req = urllib.request.Request("http://127.0.0.1:8317/v1/chat/completions", data=body,
                                 headers={"Authorization": f"Bearer {a.proxy_key()}", "Content-Type": "application/json"})
    t0 = time.time()
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=900) as r:
                trace = r.headers.get("X-Cpa-Trace-Id", "")
                d = json.load(r)
            reply = d["choices"][0]["message"]["content"] or ""
            req_id = trace.rsplit("-", 1)[-1][-8:] if trace else "?"
            auth = trace.split("-")[1][:8] if trace.count("-") > 2 else "?"
            served = served_for(model, req_id) + f"; auth {auth}"
            return reply, served, time.time() - t0
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:300]
            if e.code in (429, 500, 502, 503, 529) and attempt < 2:
                wait = int(e.headers.get("Retry-After") or 0) or 90 * (attempt + 1)
                print(f"  {e.code}, backing off {wait}s", flush=True)
                time.sleep(wait)
                continue
            return f"ERROR {e.code}: {msg}", "served: none", time.time() - t0
        except Exception as e:  # noqa: BLE001
            if attempt < 2:
                print(f"  {e!r}, backing off 60s", flush=True)
                time.sleep(60)
                continue
            return f"ERROR {e!r}", "served: none", time.time() - t0
    return "ERROR unreachable", "served: none", time.time() - t0


def piece_of(text: str) -> str:
    m = re.search(r"^#+\s*Piece\s*\n(.*)", text, re.S | re.M)
    return (m.group(1) if m else text).strip()
