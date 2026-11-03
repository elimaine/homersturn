#!/usr/bin/env python3
"""The glance bench: does a page's shape, before a word is read, predict whether
a reader starts? Same words, only the paragraph breaks move.

  build   -> arms/<item>-<shape>.txt, pages/<item>-<shape>.png, pages/*-blur.png, metrics.json
  judge   -> runs/<run-id>/replies.jsonl, one row per call, every reply kept
  report  -> runs/<run-id>/summary.md

Needs Pillow in the interpreter, and CliProxyAPI on 127.0.0.1:8317 for judge.
"""
from __future__ import annotations

import argparse
import base64
import json
import math
import os
import random
import re
import statistics
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ITEMS = ROOT / "items"
ARMS = ROOT / "arms"
PAGES = ROOT / "pages"
RUNS = ROOT / "runs"

SHAPES = ("dense-open", "equal", "shaped")
MODES = ("text", "blur", "clear")

JUDGE_PROMPT = (
    "You are looking at a page before reading it. Judge it by its shape alone: "
    "the size of the first paragraph, the sizes of the rest, where the white "
    "space falls, how much is asked of you before the first break. Do not judge "
    "the words, the voice or the meaning; the words are not the question. "
    "Answer with JSON only, no prose around it: "
    '{"inviting": 1-5, "hesitate_at": paragraph number or 0, "why": "one line"}. '
    "inviting 5 means you would start at once and keep going without effort; "
    "1 means you would not start, or would skim. hesitate_at is the paragraph, "
    "counted from the top, where you would most likely stall or skip; 0 if none."
)
TEXT_TAIL = "\n\nThe page:\n\n"
IMAGE_TAIL = "\n\nThe page is the attached image."
BLUR_TAIL = (
    "\n\nThe page is the attached image. It is blurred on purpose so that only "
    "the shape can be judged."
)
TRANSCRIBE_PROMPT = "Transcribe the first line of text in this image, exactly. If you cannot read it, say CANNOT."


# ---------- build ----------

def shape_paragraphs(sentences: list[str], shape: str) -> list[list[str]]:
    n = len(sentences)
    if shape == "dense-open":
        head = math.ceil(n * 0.6)
        paras = [sentences[:head]]
        rest = sentences[head:]
        paras += [rest[i:i + 2] for i in range(0, len(rest), 2)]
    elif shape == "equal":
        k = max(1, round(n / 4))
        paras = [sentences[i:i + k] for i in range(0, n, k)]
        if len(paras) > 1 and len(paras[-1]) < k // 2 + 1:
            last = paras.pop()
            paras[-1] += last
    elif shape == "shaped":
        plan = [1, 5, 3, 2]
        paras, i = [], 0
        for c in plan:
            paras.append(sentences[i:i + c])
            i += c
        if i < n:
            paras.append(sentences[i:])
    else:
        raise ValueError(shape)
    return [p for p in paras if p]


def metrics_for(paras: list[list[str]]) -> dict:
    words = [len(" ".join(p).split()) for p in paras]
    total = sum(words)
    mean = total / len(words)
    sd = statistics.pstdev(words) if len(words) > 1 else 0.0
    return {
        "paragraphs": len(words),
        "words": words,
        "first_share": round(words[0] / total, 3),
        "max_share": round(max(words) / total, 3),
        "cv": round(sd / mean, 3) if mean else 0.0,
    }


def render(text: str, out: Path, blur: Path | None) -> None:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont

    width, margin, size, lead = 640, 40, 17, 27
    font = None
    for cand in ("/System/Library/Fonts/Supplemental/Georgia.ttf",
                 "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
                 "/Library/Fonts/Georgia.ttf"):
        if Path(cand).exists():
            font = ImageFont.truetype(cand, size)
            break
    if font is None:
        font = ImageFont.load_default()
    probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    lines: list[str] = []
    for para in text.split("\n\n"):
        cur = ""
        for word in para.split():
            trial = (cur + " " + word).strip()
            if probe.textlength(trial, font=font) > width - 2 * margin:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
        lines.append("")
    if lines and lines[-1] == "":
        lines.pop()
    height = margin * 2 + lead * len(lines)
    im = Image.new("RGB", (width, height), "white")
    d = ImageDraw.Draw(im)
    y = margin
    for line in lines:
        if line:
            d.text((margin, y), line, font=font, fill="black")
        y += lead
    im.save(out)
    if blur is not None:
        im.filter(ImageFilter.GaussianBlur(radius=5.5)).save(blur)


def build() -> None:
    ARMS.mkdir(exist_ok=True)
    PAGES.mkdir(exist_ok=True)
    metrics = {}
    for item in sorted(ITEMS.glob("*.txt")):
        sentences = [s.strip() for s in item.read_text().splitlines() if s.strip()]
        for shape in SHAPES:
            paras = shape_paragraphs(sentences, shape)
            text = "\n\n".join(" ".join(p) for p in paras)
            key = f"{item.stem}-{shape}"
            (ARMS / f"{key}.txt").write_text(text + "\n")
            render(text, PAGES / f"{key}.png", PAGES / f"{key}-blur.png")
            metrics[key] = {"item": item.stem, "shape": shape, **metrics_for(paras)}
            assert " ".join(sentences) == text.replace("\n\n", " "), key
    (ROOT / "metrics.json").write_text(json.dumps(metrics, indent=1) + "\n")
    print(f"built {len(metrics)} arms")


# ---------- judge ----------

def proxy_key() -> str:
    conf = Path("/opt/homebrew/etc/cliproxyapi.conf").read_text()
    m = re.search(r"^api-keys:\s*\n\s*-\s*(\S+)", conf, re.M)
    if not m:
        sys.exit("no proxy key")
    return m.group(1)


def call(key: str, model: str, text: str, image: Path | None, max_tokens: int = 1500) -> dict:
    content: list[dict] = [{"type": "text", "text": text}]
    if image is not None:
        b64 = base64.b64encode(image.read_bytes()).decode()
        content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}})
    body = json.dumps({"model": model, "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": content}]}).encode()
    req = urllib.request.Request(
        "http://127.0.0.1:8317/v1/chat/completions", data=body,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            err = e.read().decode(errors="replace")
            if e.code in (429, 500, 502, 503, 529) and attempt < 3:
                time.sleep(20 * (attempt + 1))
                continue
            return {"error": err, "status": e.code}
        except Exception as e:  # noqa: BLE001
            if attempt < 3:
                time.sleep(10)
                continue
            return {"error": repr(e)}
    return {"error": "unreachable"}


def parse_reply(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, re.S)
    d: dict = {}
    if m:
        try:
            d = json.loads(m.group(0))
        except json.JSONDecodeError:
            d = {}
    if not d:  # a reply cut short: take the two numbers if both are there
        mi = re.search(r'"inviting"\s*:\s*(\d)', text)
        mh = re.search(r'"hesitate_at"\s*:\s*(\d+)', text)
        mw = re.search(r'"why"\s*:\s*"([^"]*)', text)
        if not (mi and mh):
            return None
        d = {"inviting": mi.group(1), "hesitate_at": mh.group(1), "why": (mw.group(1) + " [cut]") if mw else "[cut]"}
    try:
        inv = int(d.get("inviting"))
        hes = int(d.get("hesitate_at", 0))
    except (TypeError, ValueError):
        return None
    if not 1 <= inv <= 5:
        return None
    return {"inviting": inv, "hesitate_at": hes, "why": str(d.get("why", ""))[:300]}


def judge(args: argparse.Namespace) -> None:
    key = proxy_key()
    metrics = json.loads((ROOT / "metrics.json").read_text())
    items = sorted({m["item"] for m in metrics.values()})
    if args.items:
        items = items[: args.items]
    modes = args.modes.split(",")
    run_id = args.run or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    protocol = {
        "run": run_id, "model": args.model, "modes": modes, "items": items,
        "shapes": list(SHAPES), "samples": args.samples, "judge_prompt": JUDGE_PROMPT,
        "commit": sha, "started": datetime.now(timezone.utc).isoformat(),
        "temperature": "provider default", "max_tokens": 1500,
    }
    (run_dir / "protocol.json").write_text(json.dumps(protocol, indent=1) + "\n")
    out = (run_dir / "replies.jsonl").open("a")
    cells = [(it, sh, mo, s) for it in items for sh in SHAPES for mo in modes for s in range(args.samples)]
    rng = random.Random(args.seed)
    rng.shuffle(cells)
    print(f"run {run_id}: {len(cells)} calls on {args.model}")
    if "blur" in modes and not args.no_transcribe:
        for it in items:
            img = PAGES / f"{it}-shaped-blur.png"
            r = call(key, args.model, TRANSCRIBE_PROMPT, img, 600)
            txt = r.get("choices", [{}])[0].get("message", {}).get("content", r.get("error"))
            out.write(json.dumps({"kind": "transcribe", "item": it, "reply": txt}) + "\n")
            print(f"  transcribe {it}: {txt!r}"[:140])
    for n, (it, sh, mo, s) in enumerate(cells, 1):
        key_ = f"{it}-{sh}"
        if mo == "text":
            prompt = JUDGE_PROMPT + TEXT_TAIL + (ARMS / f"{key_}.txt").read_text()
            img = None
        elif mo == "blur":
            prompt = JUDGE_PROMPT + BLUR_TAIL
            img = PAGES / f"{key_}-blur.png"
        else:
            prompt = JUDGE_PROMPT + IMAGE_TAIL
            img = PAGES / f"{key_}.png"
        t0 = time.time()
        r = call(key, args.model, prompt, img)
        txt = r.get("choices", [{}])[0].get("message", {}).get("content") if "choices" in r else None
        row = {"kind": "judge", "item": it, "shape": sh, "mode": mo, "sample": s,
               "reply": txt, "error": r.get("error"), "parsed": parse_reply(txt or ""),
               "usage": r.get("usage"), "seconds": round(time.time() - t0, 1)}
        out.write(json.dumps(row) + "\n")
        out.flush()
        p = row["parsed"]
        print(f"  {n:3}/{len(cells)} {it} {sh:10} {mo:5} -> {p and p['inviting']} @{p and p['hesitate_at']} {row['seconds']}s" + (f" ERR {row['error'][:80]}" if row["error"] else ""))
        time.sleep(args.pause)
    out.close()
    report(argparse.Namespace(run=run_id, seed=args.seed))


# ---------- report ----------

def report(args: argparse.Namespace) -> None:
    run_dir = RUNS / args.run
    rows = [json.loads(l) for l in (run_dir / "replies.jsonl").read_text().splitlines()]
    judged = [r for r in rows if r["kind"] == "judge"]
    metrics = json.loads((ROOT / "metrics.json").read_text())
    modes = sorted({r["mode"] for r in judged}, key=MODES.index)
    items = sorted({r["item"] for r in judged})
    lines = [f"# Glance bench run {args.run}", "",
             "inviting: 1 to 5, higher means the shape invites a reader to start and keep going, so higher is better.",
             "Unit: the item (passage); samples averaged within item, shape, mode.", ""]
    bad = [r for r in judged if r["parsed"] is None]
    lines.append(f"Calls: {len(judged)}; malformed or failed: {len(bad)} (excluded from means, listed below).")
    for r in rows:
        if r["kind"] == "transcribe":
            lines.append(f"- blur check, {r['item']}: {str(r['reply'])[:100]!r}")
    lines.append("")

    def cell(it, sh, mo):
        vals = [r["parsed"]["inviting"] for r in judged if r["item"] == it and r["shape"] == sh and r["mode"] == mo and r["parsed"]]
        return statistics.mean(vals) if vals else None

    for mo in modes:
        lines += [f"## mode: {mo}", "", "| item | " + " | ".join(SHAPES) + " | shaped − dense-open | shaped − equal |", "|---|" + "---:|" * (len(SHAPES) + 2)]
        d1, d2 = [], []
        for it in items:
            c = {sh: cell(it, sh, mo) for sh in SHAPES}
            a = (c["shaped"] - c["dense-open"]) if c["shaped"] is not None and c["dense-open"] is not None else None
            b = (c["shaped"] - c["equal"]) if c["shaped"] is not None and c["equal"] is not None else None
            if a is not None: d1.append(a)
            if b is not None: d2.append(b)
            fmt = lambda v: "–" if v is None else f"{v:.2f}"
            lines.append(f"| {it} | " + " | ".join(fmt(c[sh]) for sh in SHAPES) + f" | {fmt(a)} | {fmt(b)} |")
        for name, d in (("shaped − dense-open", d1), ("shaped − equal", d2)):
            if d:
                pos, neg = sum(1 for x in d if x > 0), sum(1 for x in d if x < 0)
                k = pos + neg
                p = 2 * sum(math.comb(k, i) for i in range(0, min(pos, neg) + 1)) * 0.5 ** k if k else 1.0
                p = min(p, 1.0)
                mean = statistics.mean(d)
                lo, hi = bootstrap(d, args.seed)
                lines.append(f"\n{name}: mean {mean:+.2f} (items n={len(d)}, bootstrap 95% {lo:+.2f} to {hi:+.2f}); sign test {pos} up / {neg} down, two-sided p = {p:.3f}" + (" (n too small to reach 0.05)" if k < 6 else ""))
        # hesitation
        hes = {}
        for sh in SHAPES:
            hs = [r["parsed"]["hesitate_at"] for r in judged if r["shape"] == sh and r["mode"] == mo and r["parsed"]]
            hes[sh] = f"¶1 named {sum(1 for h in hs if h == 1)}/{len(hs)}" if hs else "–"
        lines.append("\nWhere the judge said it would stall, share naming the first paragraph: " + "; ".join(f"{sh}: {hes[sh]}" for sh in SHAPES))
        lines.append("")
    lines += ["## Shape metrics (the deterministic view)", "", "| arm | paragraphs | first share | max share | cv |", "|---|---:|---:|---:|---:|"]
    for k, m in metrics.items():
        lines.append(f"| {k} | {m['paragraphs']} | {m['first_share']:.2f} | {m['max_share']:.2f} | {m['cv']:.2f} |")
    if bad:
        lines += ["", "## Malformed or failed", ""] + [f"- {r['item']} {r['shape']} {r['mode']}: {str(r['error'] or r['reply'])[:160]!r}" for r in bad]
    lines += ["", "## Every reply", ""]
    for r in judged:
        if r["parsed"]:
            lines.append(f"- {r['item']} · {r['shape']} · {r['mode']} · s{r['sample']}: {r['parsed']['inviting']} @¶{r['parsed']['hesitate_at']}: {r['parsed']['why']}")
    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:60]))
    print(f"... full summary: {run_dir / 'summary.md'}")


def bootstrap(d: list[float], seed: int, n: int = 10000) -> tuple[float, float]:
    rng = random.Random(seed)
    means = sorted(statistics.mean(rng.choices(d, k=len(d))) for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n) - 1]


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    j = sub.add_parser("judge")
    j.add_argument("--model", default="claude-opus-5-5")
    j.add_argument("--modes", default="text,blur,clear")
    j.add_argument("--items", type=int, default=0, help="first N items only (pilot)")
    j.add_argument("--samples", type=int, default=1)
    j.add_argument("--seed", type=int, default=7)
    j.add_argument("--pause", type=float, default=2.0)
    j.add_argument("--run", default=None)
    j.add_argument("--no-transcribe", action="store_true")
    r = sub.add_parser("report")
    r.add_argument("--run", required=True)
    r.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()
    {"build": lambda a: build(), "judge": judge, "report": report}[args.cmd](args)


if __name__ == "__main__":
    main()
