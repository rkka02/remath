# Study #01 — Excavating A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*)

- **Slug**: `01-leontiev-invisible-loads`
- **Status**: Completed · Referee Audited (`gpt-6.2-astra` max) · Lean 4.36.0 Verified (`31 theorems`, `0 sorry`)
- **Live Research Brief & Visual Gallery**: [https://rkka02.github.io/studies/01-leontiev-invisible-loads/](https://rkka02.github.io/studies/01-leontiev-invisible-loads/)

---

## Publications (3 Self-Contained, Non-Overlapping PDFs)

1. **Paper 1 (English Academic Preprint, `amsart`, 15 pp.)** — [`papers/paper1_invisible_loads/paper1_invisible_loads.pdf`](papers/paper1_invisible_loads/paper1_invisible_loads.pdf) ([`.tex`](papers/paper1_invisible_loads/paper1_invisible_loads.tex))
   - *Invisible Boundary Loads on Convex Polygons: Leont'ev's Exponential Lattice, Balayage Anatomy, and Fokas's Global Relation*
   - Dedicated figures: `papers/paper1_invisible_loads/figs/p1_fig{1,2,3}_*.png`
2. **Paper 2 (English Academic Preprint, `amsart`, 12 pp.)** — [`papers/paper2_corner_recovery/paper2_corner_recovery.pdf`](papers/paper2_corner_recovery/paper2_corner_recovery.pdf) ([`.tex`](papers/paper2_corner_recovery/paper2_corner_recovery.tex))
   - *Minimax Recovery of Polygon Corner Charges from Bandlimited Leont'ev Frequencies: Parity, Angle-Dependent Exponents, and Super-Resolution*
   - Dedicated figures: `papers/paper2_corner_recovery/figs/p2_fig{1,2,3}_*.png`
3. **Expository Magazine Feature (Korean, `xeCJK`, 6 pp.)** — [`papers/expository_kr/expository_leontiev_kr.pdf`](papers/expository_kr/expository_leontiev_kr.pdf) ([`.tex`](papers/expository_kr/expository_leontiev_kr.tex))
   - *다각형이 들을 수 없는 파동들: 소련 우파(Ufa)의 잊힌 지수급수 이론에서 발굴한 7가지 수학적 기적*
   - Dedicated figures: `papers/expository_kr/figs/kr_fig{1,2,3,4}_*.png`

---

## Archive Contents

- **Markdown Reports & Research Log**: [`docs/DISCOVERY_STORY_KR.md`](docs/DISCOVERY_STORY_KR.md) · [`docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md`](docs/PAPER_LEONTIEV_INVISIBLE_LOADS.md) · [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md)
- **Primary Sources (`sources/`)**: [`sources/PRIMARY_SOURCES.md`](sources/PRIMARY_SOURCES.md) + 8 open-access Russian (Math-Net.Ru) and English (arXiv) PDFs in `sources/papers/`.
- **Formal Proofs (`proofs/lean4/`)**: 4 standalone Lean 4.36.0 modules (`PolygonParity`, `FiniteMinimax`, `SuperResolutionWindow`, `TwoSidedSymmetry`) + `Main.lean` axiom audit (31 verified theorems, 0 `sorry`, standard axioms `propext`, `Classical.choice`, `Quot.sound` only).
- **High-Precision Scripts (`experiments/`)**: 65–230 digit `mpmath` / interval-arithmetic probes + figure generators (`generate_paper_figures.py`, `generate_figures.py`).
- **Codex Astra Max Logs (`codex_logs/`)**: Full reproducible prompts, derivations, and line-by-line referee audit (`codex_logs/phase4_referee_output.md`).

---

## Reproducibility & Verification Commands

Run from `studies/01-leontiev-invisible-loads/`:

```bash
# 1. Machine-verify all 31 Lean 4 theorems from scratch + axiom audit
(cd proofs/lean4 && lake clean && lake build && lake env lean Main.lean)

# 2. Run 65-digit & 80-digit numerical verification probes
python3 experiments/phase1_probe.py
python3 experiments/phase2_theorems.py

# 3. Run 230-digit outward-rounded interval certificates on the unit square
python3 experiments/phase3_square_certificate.py 1
python3 experiments/phase3_square_certificate.py 2
python3 experiments/phase3_square_certificate.py 4

# 4. Regenerate all 10 dedicated publication figures & compile all 3 PDFs
python3 experiments/generate_paper_figures.py
(cd papers/paper1_invisible_loads && /opt/homebrew/bin/tectonic paper1_invisible_loads.tex)
(cd papers/paper2_corner_recovery && /opt/homebrew/bin/tectonic paper2_corner_recovery.tex)
(cd papers/expository_kr && /opt/homebrew/bin/tectonic expository_leontiev_kr.tex)
```
