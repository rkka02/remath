# ReMath: Excavating A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*)

> **Mathematical Archaeology & Original Discovery Repository**
> Reviving A. F. Leont'ev's untranslated Soviet Ufa/Moscow theory of exponential series on convex polygons (1969–1987), bridging it to A. S. Fokas's modern Unified Transform Method, proving a universal classification of invisible physical loads and angle-dependent corner recovery laws, and machine-verifying the core theorems in **Lean 4.36.0**.

## Key Deliverables (Start Here!)

- **한국어 교양·해설 리포트 ("오오! 이런게 이렇게 된다고?!")**: [`docs/DISCOVERY_STORY_KR.md`](docs/DISCOVERY_STORY_KR.md)
- **영문 엄밀 학술 보고서 (Technical Preprint)**: [`docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md`](docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md)
- **전체 연구 일지 (Research Log)**: [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md)
- **시각화 갤러리 (`figures/`)**:
  - [`figures/fig1_ghost_waves_and_frequencies.png`](figures/fig1_ghost_waves_and_frequencies.png) — Polygon frequency rays, square ghost waves ($10^{-47}$ inside, $10^{-65}$ continued outside against $10^{27}$ term), and $m=k^2$ erasure resilience
  - [`figures/fig2_invisible_loads_square_vs_triangle.png`](figures/fig2_invisible_loads_square_vs_triangle.png) — Square uniform charge (Saint-Venant torsion) vs. Equilateral triangle Y-shaped Zeta skeleton ($\zeta(4),\zeta(10),\zeta(16),\dots$), $L^1\setminus L^2$ corner blowups, and two-sided symmetry collapse
  - [`figures/fig3_rhombus_two_slopes_and_shift_paradox.png`](figures/fig3_rhombus_two_slopes_and_shift_paradox.png) — Two-slope $60^\circ/120^\circ$ rhombus ($N^{-5/6}$ vs. $N^{-2/3}$), interval-certified half-step suboptimality, and odd-polygon sharp constant
  - [`figures/fig4_super_resolution_and_fokas_pde.png`](figures/fig4_super_resolution_and_fokas_pde.png) — 24-order corner super-resolution ($10^{-26}$), Fokas PDE blind-spot removal ($10^{-16}$), and discontinuous-wall heated plates
- **Lean 4.36.0 기계 검증 (`proofs/lean4/`)**: 4 standalone modules, **31 verified theorems**, 0 warnings, 0 `sorry`, standard axioms only (`propext`, `Classical.choice`, `Quot.sound`).
- **원전 아카이브 (`sources/`)**: [`sources/PRIMARY_SOURCES.md`](sources/PRIMARY_SOURCES.md) + 8 open-access Russian (Math-Net.Ru) and English (arXiv) primary PDFs in `sources/papers/`.
- **Codex (`gpt-6.2-astra`, `reasoning_effort=max`) 연구 로그 (`codex_logs/`)**: Full reproducible prompts and mathematical derivations across Phases 1–3.

## Quick Verification Commands

```bash
# 1. Machine-verify all 31 Lean 4 theorems from scratch + print axiom audit
cd proofs/lean4 && lake clean && lake build && lake env lean Main.lean && cd ../..

# 2. Run 65-digit Phase 1 probes (Leont'ev-Fokas bridge, ghost waves, erasure, torsion)
python3 experiments/phase1_probe.py

# 3. Run 80-digit Phase 2 theorems (p-gon invisible loads, minimax, super-resolution, Fokas PDE)
python3 experiments/phase2_theorems.py

# 4. Run 45-digit interval-arithmetic square shift optimality certificates
python3 experiments/phase3_square_certificate.py 1
python3 experiments/phase3_square_certificate.py 2
python3 experiments/phase3_square_certificate.py 4

# 5. Regenerate all 4 multi-panel figures
python3 experiments/generate_figures.py
```

## Research Architecture
- **Research Director, Archaeologist, Auditor & Narrator**: Antigravity (Gemini)
- **Mathematical Computation, Proof & Lean Formalization Subcontractor**: Codex CLI (`gpt-6.2-astra`, `reasoning_effort=max`) via [`scripts/run_astra.sh`](scripts/run_astra.sh)
