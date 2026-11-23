# AGENTS.md — Project ReMath Onboarding & Research Constitution

> **Read this file first** whenever starting a session in `/Users/mw/Desktop/math/remath`.
> It defines the mission, taste, multi-agent workflow, verification standards, local Mac toolchain gotchas, and cumulative folder conventions for **Project ReMath**.

---

## 1. What Project ReMath Is (Mission & Taste)

**Project ReMath** is a cumulative **Mathematical Archaeology & AI-Assisted Research Workbench** (`https://github.com/rkka02/remath`), paired with a public cumulative showcase portal at **https://rkka02.github.io** (sibling repo: `../rkka02.github.io`).

Our core mission is **not** chasing generic unsolved-problem clickbait. Instead, we:
1. **Excavate** overlooked, untranslated, or half-abandoned mathematical ideas from decades past (especially Soviet, Eastern Bloc, or classical schools whose monographs were never translated or never connected to modern tools).
2. **Ground** every study in authentic primary sources (Math-Net.Ru, arXiv, historical monographs) archived locally in `sources/papers/`.
3. **Bridge & Discover** genuinely original theorems connecting the excavated theory to modern mathematics (PDEs, inverse problems, optimal recovery, probability, spectral geometry, computation).
4. **Hold a High Taste Bar**: Do not stop at routine generalizations. Push until we uncover **surprising, concrete, rigorously verified results** that even a thoughtful outsider looks at and says *"오오! 이런게 이렇게 된다고?"* (e.g., Study #01's *Saint-Venant torsion iff parallelogram* vs. *equilateral triangle's 1D Riemann-zeta Y-skeleton*, the *60°/120° rhombus two-slope law*, and *interval-certified suboptimality of the half-step*).
5. **Verify Without Compromise** (high-precision `mpmath` / interval arithmetic + standalone **Lean 4** proofs with zero `sorry` + line-by-line mathematical refereeing) and **publish** crisp non-overlapping PDFs + a clean brief on `rkka02.github.io`.

---

## 2. Multi-Agent Division of Labor & Golden Editorial Rule

This workbench operates as a two-role research team:

- **Lead Agent (Director · Archaeologist · Author · Visualizer — you)**:
  - Steers research direction and decides which mathematical leads are genuinely astonishing vs. incremental.
  - Acquires and audits primary literature, runs independent numerical checks, designs clean publication figures (`matplotlib`), writes the manuscripts (English preprints + vivid Korean exposition), manages Git, and updates `../rkka02.github.io`.
- **Mathematical Subcontractor & Referee (`Codex CLI` — `gpt-6.2-astra`, `reasoning_effort=max`)**:
  - Summoned via `./scripts/run_astra.sh <study_slug> <task_slug> <prompt_file> [sandbox_mode]`.
  - Handles heavy symbolic/analytic derivations, high-precision proof probes, Lean 4 formalizations, and **read-only mathematical referee audits** of drafted manuscripts.

### Golden Editorial Rule (Follow Strictly)
- **On genuine mathematical or logical errors caught by Astra** (wrong formulas, missing hypotheses, invalid proof steps, sign errors, misquoted numerical certificates): **obey 100% and repair completely.**
- **On overly paranoid or pedantic stylistic nitpicks** (especially in Korean expository/magazine writing): **exercise sensible editorial judgment**—keep every statement mathematically truthful while preserving narrative flow, intuition, and reader excitement.

---

## 3. Repository Layout & Scaling Invariants

Every research expedition lives in its own **completely self-contained directory** under `studies/<NN-slug>/`, sharing the exact same `<NN-slug>` used in `../rkka02.github.io/content/studies/<NN-slug>/`.

```text
remath/
├── AGENTS.md                       # This universal agent onboarding constitution
├── CLAUDE.md                       # Claude Code pointer to AGENTS.md
├── README.md                       # Human-facing overview & live portal links
├── STUDIES.md                      # Cumulative study ledger (#01, #02, ...) + backlog
├── scripts/                        # Shared workbench tooling across ALL studies
│   ├── run_astra.sh                # Summon Codex (gpt-6.2-astra, max reasoning) for a study
│   ├── new_study.py                # Scaffold studies/<NN-slug>/ in 1 command
│   └── publish_to_portal.py        # Sync a study's PDFs & figures to ../rkka02.github.io
└── studies/
    └── 01-leontiev-invisible-loads/   # Reference gold-standard completed study
        ├── STUDY.md                # Study summary, deliverables map & verification commands
        ├── docs/                   # RESEARCH_LOG.md, technical summary & Korean story
        ├── sources/                # Primary PDFs (papers/), extracted text, PRIMARY_SOURCES.md
        ├── experiments/            # High-precision Python probes, figure generators, saved data
        ├── proofs/lean4/           # Standalone Lean 4 project (0 sorry, standard axioms only)
        ├── papers/                 # Self-contained LaTeX preprints & Korean feature + figs/ + PDFs
        ├── figures/                # Exploratory/overview figures
        └── codex_logs/             # Reproducible Astra prompts, outputs & referee audits
```

### Non-Negotiable Invariants
1. **Never scatter study-specific files in the repo root.** Everything belonging to a study goes under `studies/<NN-slug>/`.
2. **Use relative `Path(__file__).resolve()` paths** inside Python scripts so every study remains portable and self-contained.
3. **Keep `STUDIES.md` and `studies/<NN-slug>/docs/RESEARCH_LOG.md` updated** as discoveries happen so context survives across sessions and across different agents.
4. **Never commit transient logs or build caches** (`*.log`, `*.aux`, `.lake/`, `__pycache__/`, `.DS_Store` are gitignored). Always commit `codex_logs/*_prompt*.md` and `*_output.md` for reproducibility.

---

## 4. Standard 5-Phase Study Playbook

1. **Phase 0 — Scaffold & Primary Excavation**
   - Run `python3 scripts/new_study.py <NN-slug> "<Short Title>"`.
   - Download/archive open-access primary PDFs into `studies/<NN-slug>/sources/papers/` and catalog them in `sources/PRIMARY_SOURCES.md`.
2. **Phase 1 — Deep Scouting**
   - Formulate 3–4 high-upside mathematical bridges or hidden phenomena.
   - Delegate exploratory derivations + 50–80 digit `mpmath` numerical probes to Astra via `./scripts/run_astra.sh <NN-slug> phase1_scouting <prompt_file> workspace-write`.
   - Independently execute every Python script yourself and steer toward the single sharpest, most surprising discovery thread.
3. **Phase 2 — General Theorems & Quantitative Boundaries**
   - Push from special examples to general theorems, sharp necessary-and-sufficient criteria, phase transitions, and rigorous interval/high-precision checks.
4. **Phase 3 — Formalization (Lean 4) & Visual Anatomy**
   - Formalize the core algebraic/combinatorial/minimax pillars in `studies/<NN-slug>/proofs/lean4/` with zero external bloat when feasible.
   - Verify from scratch: `lake clean && lake build && lake env lean Main.lean` (**0 errors, 0 warnings, 0 `sorry`**, audit `#print axioms` to confirm only standard axioms `propext`, `Classical.choice`, `Quot.sound`).
5. **Phase 4 — Non-Overlapping PDFs & Read-Only Astra Referee Audit**
   - Partition outputs cleanly into self-contained publications (e.g., 1–2 English `amsart` academic preprints + 1 accessible Korean `xeCJK` expository feature) with **dedicated non-overlapping figures** in `papers/*/figs/`.
   - Run a **read-only** referee audit: `./scripts/run_astra.sh <NN-slug> phase4_referee <prompt_file> read-only`.
   - Repair every genuine math/logic flaw caught by Astra, compile all PDFs with `tectonic` (**0 errors, 0 overfull/layout warnings**), and visually inspect every PDF page.
6. **Phase 5 — Publish to Sibling Research Portal (`../rkka02.github.io`)**
   - Run `python3 scripts/publish_to_portal.py <NN-slug>` to sync compiled PDFs and figures into `../rkka02.github.io/content/studies/<NN-slug>/assets/`.
   - Author/update `../rkka02.github.io/content/studies/<NN-slug>/study.json` (set previous featured study to `"featured": false`, new one to `true`), rebuild with `python3 ../rkka02.github.io/scripts/build_site.py`, commit & push **both** `remath` and `rkka02.github.io`, and visually verify the live page at `https://rkka02.github.io`.

---

## 5. Local Mac Toolchain & Hard-Won Gotchas

- **Codex CLI (`gpt-6.2-astra`)**:
  - Always use `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex` (`v0.171+`) — already wired into `scripts/run_astra.sh`.
  - **Do NOT** use `/opt/homebrew/bin/codex` (older Homebrew binary breaks on `gpt-6.2-astra` model routing).
- **LaTeX PDF Compilation**:
  - Use `/opt/homebrew/bin/tectonic` (supports `amsart`, `xeCJK`, `tcolorbox` cleanly out of the box).
  - Working Korean font pair on this Mac: `\setCJKmainfont[BoldFont={NanumMyeongjoExtraBold}]{Nanum Myeongjo}` + `\setCJKsansfont{Apple SD Gothic Neo}`.
- **Matplotlib Figures (Zero Warnings)**:
  - For Korean-labeled figures: set `"font.family": "Arial Unicode MS"` and `"mathtext.fontset": "dejavusans"` (prevents missing `U+2212` minus-sign glyph warnings on log axes).
  - Use `\geq` / `\leq` instead of `\ge` / `\le` in matplotlib mathtext strings.
- **GitHub Pages (`rkka02/rkka02.github.io`)**:
  - Pages is configured with `build_type: workflow` (`.github/workflows/pages.yml` builds `dist/` via Python on push to `main`). Check workflow success via `gh run list --repo rkka02/rkka02.github.io`.

---

## 6. Quick Reference: Starting a New Study

```bash
# 1. Check existing studies and backlog
cat STUDIES.md

# 2. Scaffold Study #02
python3 scripts/new_study.py 02-next-topic-slug "Short Study Title"

# 3. Run Codex Astra Max scoped to Study #02
./scripts/run_astra.sh 02-next-topic-slug phase1_scouting studies/02-next-topic-slug/codex_logs/phase1_prompt.md workspace-write

# 4. Sync Study #02 outputs to ../rkka02.github.io once finished
python3 scripts/publish_to_portal.py 02-next-topic-slug
```
