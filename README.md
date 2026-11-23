# Project ReMath — Mathematical Archaeology & AI-Assisted Research Workbench

> **Public Cumulative Research Portal**: [https://rkka02.github.io](https://rkka02.github.io)  
> **Agent Onboarding & Constitution**: [`AGENTS.md`](AGENTS.md) · [`CLAUDE.md`](CLAUDE.md)  
> **Cumulative Study Ledger**: [`STUDIES.md`](STUDIES.md)

**Project ReMath** is a cumulative research repository dedicated to excavating overlooked, untranslated, or half-abandoned mathematical theories (especially from Soviet, Eastern Bloc, and classical traditions), connecting them to modern analysis, PDEs, and inverse problems, verifying every claim via high-precision computation + **Lean 4** formalization + **Codex Astra Max** mathematical refereeing, and publishing self-contained preprints and accessible Korean expositions.

---

## Archived Studies

| # | Study | Key Outputs | Links |
|---|---|---|---|
| **01** | **A. F. Leont'ev's *Series of Exponentials*** — Invisible Boundary Loads, Balayage Anatomy, Minimax Corner Recovery & Fokas's Global Relation | 3 PDFs (15p + 12p + 6p) · 10 dedicated figs · 31 Lean 4 theorems (`0 sorry`) · 8 primary PDFs | [STUDY.md](studies/01-leontiev-invisible-loads/STUDY.md) · [Live Brief ↗](https://rkka02.github.io/studies/01-leontiev-invisible-loads/) |

---

## Repository Structure

```text
remath/
├── AGENTS.md                        # Onboarding guide & workflow rules for ANY AI agent
├── CLAUDE.md                        # Claude Code entry pointer
├── STUDIES.md                       # Cumulative ledger of all studies (#01, #02, ...)
├── scripts/
│   ├── run_astra.sh                 # Summon Codex (gpt-6.2-astra, max reasoning) per study
│   ├── new_study.py                 # 1-command scaffolder for studies/<NN-slug>/
│   └── publish_to_portal.py         # Sync a study's PDFs & figures to ../rkka02.github.io
└── studies/
    └── 01-leontiev-invisible-loads/ # Self-contained Study #01 archive
        ├── STUDY.md                 # Deliverables map & exact verification commands
        ├── docs/                    # Research log, technical summary & Korean story
        ├── sources/                 # Primary PDFs (Math-Net.Ru, arXiv) + extracted text
        ├── experiments/             # 65–230 digit verification & figure generation scripts
        ├── proofs/lean4/            # Standalone Lean 4.36.0 proofs (0 sorry, standard axioms)
        ├── papers/                  # Non-overlapping LaTeX manuscripts, figs/ & compiled PDFs
        ├── figures/                 # Exploratory multi-panel gallery
        └── codex_logs/              # Reproducible prompts, Astra outputs & referee audit
```

---

## Workbench Quick Commands

```bash
# Start a new study (#02, #03, ...)
python3 scripts/new_study.py 02-next-slug "Short Study Title"

# Delegate heavy math / proofs / refereeing to Codex Astra Max inside a study
./scripts/run_astra.sh 02-next-slug phase1_scouting studies/02-next-slug/codex_logs/phase1_prompt.md workspace-write

# Sync a completed study's PDFs & figures to sibling portal ../rkka02.github.io
python3 scripts/publish_to_portal.py 01-leontiev-invisible-loads

# Independently verify Study #01 Lean 4 proofs (31 theorems, 0 sorry)
cd studies/01-leontiev-invisible-loads/proofs/lean4 && lake clean && lake build && lake env lean Main.lean
```
