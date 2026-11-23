# ReMath: Excavating A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*)

> **Interactive Research Brief & Visual Archive**: [https://rkka02.github.io/studies/01-leontiev-invisible-loads/](https://rkka02.github.io/studies/01-leontiev-invisible-loads/)
>
> **Mathematical Archaeology & Original Discovery Repository**
> Reviving A. F. Leont'ev's untranslated Soviet Ufa/Moscow theory of exponential series on convex polygons (1969–1987), bridging it to A. S. Fokas's modern Unified Transform Method, proving a universal classification of invisible physical loads and angle-dependent corner recovery laws, and machine-verifying the algebraic/minimax core in **Lean 4.36.0**.

## Publication Suite (3 Non-Overlapping PDFs)

1. **Paper 1 (English Academic Preprint PDF — Complex Analysis / Balayage / Fokas PDE)**
   - [`papers/paper1_invisible_loads/paper1_invisible_loads.pdf`](papers/paper1_invisible_loads/paper1_invisible_loads.pdf) ([LaTeX source](papers/paper1_invisible_loads/paper1_invisible_loads.tex))
   - *Invisible Boundary Loads on Convex Polygons: Leont'ev's Exponential Lattice, Balayage Anatomy, and Fokas's Global Relation*
2. **Paper 2 (English Academic Preprint PDF — Minimax Optimal Recovery / Super-Resolution)**
   - [`papers/paper2_corner_recovery/paper2_corner_recovery.pdf`](papers/paper2_corner_recovery/paper2_corner_recovery.pdf) ([LaTeX source](papers/paper2_corner_recovery/paper2_corner_recovery.tex))
   - *Minimax Recovery of Polygon Corner Charges from Bandlimited Leont'ev Frequencies: Parity, Angle-Dependent Exponents, and Super-Resolution*
3. **Expository Magazine Article (Korean PDF — 한국어 교양·해설 특집판)**
   - [`papers/expository_kr/expository_leontiev_kr.pdf`](papers/expository_kr/expository_leontiev_kr.pdf) ([LaTeX source](papers/expository_kr/expository_leontiev_kr.tex))
   - *다각형이 들을 수 없는 파동들: 소련 우파(Ufa)의 잊힌 지수급수 이론에서 발굴한 7가지 수학적 기적*

## Markdown Reports, Proofs & Archives

- **한국어 교양·해설 마크다운**: [`docs/DISCOVERY_STORY_KR.md`](docs/DISCOVERY_STORY_KR.md)
- **통합 기술 요약 마크다운**: [`docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md`](docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md)
- **전체 연구 일지 (Research Log)**: [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md)
- **Lean 4.36.0 기계 검증 (`proofs/lean4/`)**: 4 standalone modules, **31 verified theorems**, 0 warnings, 0 `sorry`, standard foundational axioms only (`propext`, `Classical.choice`, `Quot.sound`).
- **원전 아카이브 (`sources/`)**: [`sources/PRIMARY_SOURCES.md`](sources/PRIMARY_SOURCES.md) + 8 open-access Russian (Math-Net.Ru) and English (arXiv) primary PDFs in `sources/papers/`.
- **Codex (`gpt-6.2-astra`, `reasoning_effort=max`) 연구 및 레퍼리 감사 로그 (`codex_logs/`)**: Full reproducible prompts, mathematical derivations, and Phase 4 line-by-line referee audit (`codex_logs/phase4_referee_output.md`).

## Quick Verification Commands

```bash
# 1. Machine-verify all 31 Lean 4 theorems from scratch + print axiom audit
cd proofs/lean4 && lake clean && lake build && lake env lean Main.lean && cd ../..

# 2. Run 65-digit Phase 1 probes (Leont'ev-Fokas bridge, ghost waves, erasure, torsion)
python3 experiments/phase1_probe.py

# 3. Run 80-digit Phase 2 theorems (p-gon invisible loads, minimax, super-resolution, Fokas PDE)
python3 experiments/phase2_theorems.py

# 4. Run 230-digit interval-arithmetic square shift optimality certificates
python3 experiments/phase3_square_certificate.py 1
python3 experiments/phase3_square_certificate.py 2
python3 experiments/phase3_square_certificate.py 4

# 5. Regenerate all 10 dedicated publication figures + compile all 3 PDFs
python3 experiments/generate_paper_figures.py
(cd papers/paper1_invisible_loads && tectonic paper1_invisible_loads.tex)
(cd papers/paper2_corner_recovery && tectonic paper2_corner_recovery.tex)
(cd papers/expository_kr && tectonic expository_leontiev_kr.tex)
```

## Research Architecture
- **Research Director, Archaeologist, Prose Author, Visualizer & Editor**: Antigravity (Gemini)
- **Mathematical Computation, Proof, Lean Formalization & Referee Auditor**: Codex CLI (`gpt-6.2-astra`, `reasoning_effort=max`) via [`scripts/run_astra.sh`](scripts/run_astra.sh)
