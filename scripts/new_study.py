#!/usr/bin/env python3
"""
Scaffold a new self-contained research study under studies/<NN-slug>/.

Usage:
  python3 scripts/new_study.py 02-my-next-topic "Short Study Title"
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STUDIES = ROOT / "studies"


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python3 scripts/new_study.py <NN-slug> ["Short Study Title"]')
        sys.exit(1)

    slug = sys.argv[1].strip().strip("/")
    title = sys.argv[2].strip() if len(sys.argv) >= 3 else slug
    today = dt.date.today().isoformat()

    study_dir = STUDIES / slug
    if study_dir.exists():
        print(f"Error: study directory already exists: {study_dir}")
        sys.exit(1)

    for rel in [
        "docs",
        "sources/papers",
        "sources/extracted",
        "experiments/data",
        "proofs/lean4",
        "papers",
        "figures",
        "codex_logs",
    ]:
        (study_dir / rel).mkdir(parents=True, exist_ok=True)

    (study_dir / "STUDY.md").write_text(
        f"""# Study — {title}

- **Slug**: `{slug}`
- **Started**: {today}
- **Status**: Phase 0 — Excavation & Scouting
- **Live Brief (once published)**: https://rkka02.github.io/studies/{slug}/

---

## Core Research Question & Motivation

- What forgotten, untranslated, or overlooked mathematical theory are we excavating?
- What modern mathematical / computational bridge are we testing?

## Deliverables Checklist

- [ ] Primary sources archived in `sources/papers/` + `sources/PRIMARY_SOURCES.md`
- [ ] Phase 1 scouting & high-precision `mpmath` probes (`experiments/`)
- [ ] Phase 2 general theorems & independent verification
- [ ] Phase 3 standalone Lean 4 formalization (`proofs/lean4/`, 0 `sorry`, standard axioms only)
- [ ] Phase 4 non-overlapping PDFs (`papers/`) + dedicated figures + read-only Astra referee audit
- [ ] Phase 5 synced to `../rkka02.github.io` via `python3 scripts/publish_to_portal.py {slug}`
""",
        encoding="utf-8",
    )

    (study_dir / "docs" / "RESEARCH_LOG.md").write_text(
        f"""# Research Log — {title} (`{slug}`)

## {today} — Phase 0: Study Initialized
- Scaffolded via `scripts/new_study.py`.
- Next: Excavate primary literature into `sources/papers/`, record bibliographic details in `sources/PRIMARY_SOURCES.md`, and prepare Phase 1 scouting hypotheses for Codex Astra Max (`./scripts/run_astra.sh {slug} phase1_scouting ...`).
""",
        encoding="utf-8",
    )

    (study_dir / "sources" / "PRIMARY_SOURCES.md").write_text(
        f"""# Primary Source Archive — {title}

Catalog every downloaded primary PDF (`sources/papers/`) with exact bibliographic citation, archive URL (Math-Net.Ru, arXiv, Numdam, etc.), and extracted key formulas/theorems.

| # | Author(s) & Year | Title & Venue | Local File | Source URL |
|---|---|---|---|---|
| 1 | | | `papers/...` | |
""",
        encoding="utf-8",
    )

    print(f"Created new study scaffold at: {study_dir}")
    print("Next steps:")
    print(f"  1. Add primary PDFs to {study_dir / 'sources' / 'papers'}")
    print(f"  2. Run Astra scouting: ./scripts/run_astra.sh {slug} phase1_scouting <prompt_file> workspace-write")
    print(f"  3. Register the study in STUDIES.md")


if __name__ == "__main__":
    main()
