# Project ReMath — Mathematical Archaeology & AI-Assisted Research Workbench

> **Public Cumulative Research Portal**: [https://rkka02.github.io](https://rkka02.github.io)  
> **Agent Onboarding & Constitution**: [`AGENTS.md`](AGENTS.md) · [`CLAUDE.md`](CLAUDE.md)  
> **Cumulative Study Ledger**: [`STUDIES.md`](STUDIES.md)

**Project ReMath** is a cumulative research repository dedicated to excavating overlooked, untranslated, or half-abandoned mathematical theories (especially from Soviet, Eastern Bloc, and classical traditions), connecting them to modern analysis, probability, dynamical systems, PDEs, and inverse problems, verifying every claim via high-precision computation + **Lean 4** formalization + **Codex Astra Max** mathematical refereeing, and publishing self-contained preprints and accessible Korean expositions.

---

## Archived Studies

| # | Study | Key Outputs | Links |
|---|---|---|---|
| **01** | **A. F. Leont'ev's *Series of Exponentials*** — Invisible Boundary Loads, Balayage Anatomy, Minimax Corner Recovery & Fokas's Global Relation | 3 PDFs (15p + 12p + 6p) · 10 dedicated figs · 31 Lean 4 theorems (`0 sorry`) · 8 primary PDFs | [STUDY.md](studies/01-leontiev-invisible-loads/STUDY.md) · [Live Brief ↗](https://rkka02.github.io/studies/01-leontiev-invisible-loads/) |
| **02** | **M. L. Tsetlin's *Collective Automata*** — Shared-Fate Hierarchies, Volkonskii (1965) Erratum, Optimal Imperfect Synchrony $\kappa_*(\gamma)$, Fair-$DD$ Elliptic Cancellation, $+1$-Depth Cliffs, Stag-Hunt Mirages & Common-Fund Cutoff $n_c=2$ | 3 PDFs (15p + 11p + 7p) · 10 dedicated figs · 117 public Lean 4 theorems (911 audited constants, `0 sorry`) · 13 primary PDFs | [STUDY.md](studies/02-tsetlin-collective-automata/STUDY.md) · [Live Brief ↗](https://rkka02.github.io/studies/02-tsetlin-collective-automata/) |
| **03** | **Sobolev–Aleksandryan–Zelenyak–Fokin *Wave Attractors*** — Sharp $1/2$ Uncloakability, $m+5$ Prescribed Coexistence, Fixed-Tank $\cos\phi-\sin\phi$ Tilt Catastrophe, Hecke Dimension, $\ge 17.806\%$ Corner Shaving, All-Polygon Rigidity & $1000$- vs. $1002$-Gon Paradox | 3 PDFs (19p + 20p + 8p) · 10 dedicated figs · 125 public Lean 4 theorems (40 principal, `0 sorry`) · 13 primary PDFs | [STUDY.md](studies/03-sobolev-wave-attractors/STUDY.md) · [Live Brief ↗](https://rkka02.github.io/studies/03-sobolev-wave-attractors/) |

---

## Repository Structure

```text
remath/
├── AGENTS.md                           # Onboarding guide & workflow rules for ANY AI agent
├── CLAUDE.md                           # Claude Code entry pointer
├── STUDIES.md                          # Cumulative ledger of all studies (#01, #02, #03, ...)
├── scripts/
│   ├── run_astra.sh                    # Summon Codex (gpt-6.2-astra, max reasoning) per study
│   ├── new_study.py                    # 1-command scaffolder for studies/<NN-slug>/
│   └── publish_to_portal.py            # Sync a study's PDFs & figures to ../rkka02.github.io
└── studies/
    ├── 01-leontiev-invisible-loads/    # Study #01: A. F. Leont'ev & Fokas PDEs (31 Lean 4)
    ├── 02-tsetlin-collective-automata/ # Study #02: M. L. Tsetlin Collective Automata (117 Lean 4)
    └── 03-sobolev-wave-attractors/     # Study #03: Sobolev–Aleksandryan Wave Attractors (125 Lean 4)
        ├── STUDY.md                    # Deliverables map & exact verification commands
        ├── docs/                       # Research log & detailed proof chapters
        ├── sources/                    # Primary PDFs (Math-Net.Ru, arXiv) + extracted text
        ├── experiments/                # High-precision / interval verification & figure scripts
        ├── proofs/lean4/               # Standalone Lean 4.36.0 proofs (0 sorry, standard axioms)
        ├── papers/                     # Non-overlapping LaTeX manuscripts, figs/ & compiled PDFs
        ├── figures/                    # Exploratory multi-panel figures
        └── codex_logs/                 # Reproducible prompts, Astra outputs & referee audits
```

---

## Workbench Quick Commands

```bash
# Start a new study (#04, ...)
python3 scripts/new_study.py 04-next-slug "Short Study Title"

# Delegate heavy math / proofs / refereeing to Codex Astra Max inside a study
./scripts/run_astra.sh 04-next-slug phase1_scouting studies/04-next-slug/codex_logs/phase1_prompt.md workspace-write

# Sync a completed study's PDFs & figures to sibling portal ../rkka02.github.io
python3 scripts/publish_to_portal.py 03-sobolev-wave-attractors

# Independently verify all 273 Lean 4 theorems (0 sorry) across Studies #01–#03
for s in 01-leontiev-invisible-loads 02-tsetlin-collective-automata 03-sobolev-wave-attractors; do
  (cd "studies/$s/proofs/lean4" && lake build && lake env lean Main.lean)
done
```
