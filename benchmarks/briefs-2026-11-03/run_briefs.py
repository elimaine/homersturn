#!/usr/bin/env python3
"""Every brief in briefs.json, one model, sequential. usage: run_briefs.py <model>"""
import json, subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
model = sys.argv[1]
for name, brief in json.load(open(ROOT / "briefs.json")).items():
    if (ROOT / "runs" / f"{name}-{model}.md").exists():
        print("have", name, model, flush=True); continue
    subprocess.run([sys.executable, str(ROOT / "run.py"), name, brief, model])
