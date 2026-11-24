# Final Read-Only Pre-Pitch Sign-Off (`phase2_signoff`) — Study #03

You are running an independent **`read-only` sign-off audit** on `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors` confirming that **all 4 major findings and all 4 other open defects** from `codex_logs/phase2_verify_final_output.md` are 100% closed and that no new errors were introduced (including checking `experiments/generate_phase2_previews.py` formulas!).

Use `PYTHONDONTWRITEBYTECODE=1` for all Python executions and do NOT modify any files.

## Focused Verification Checklist
1. Verify **Major Finding 1** (`docs/phase1_scouting.md:271`): confirms the mirror sequence preserves the exact disk eigenfrequency $E = 1/2$ with infinite multiplicity (explicitly NOT the disk polynomial $1-x^2-z^2$).
2. Verify **Major Finding 2** (`experiments/phase1_canonical.py`, `experiments/phase1_pde.py`): `ChessMap` and `reflect` reject binary floats (`TypeError`) and handle exact `Fraction` / `Integral` inputs cleanly (`ChessMap(polygon(0,0,1,1), Fraction.from_float(math.nextafter(1.0, 0.0))).periodic_data(1, 2) == (False, {})`).
3. Verify **Major Finding 3** (`experiments/phase1_regular.py`): `half_period_cells` rejects wide phase enclosures like `[4.99°, 5.01°]` with `InsufficientResolution`, and cleanly resolves exact tiny phase `1e-40°` at 75 digits (`1` open cell of width `2e-40°`, `0` unresolved).
4. Verify **Major Finding 4** (`docs/phase1_regular.md:299`, `sources/PRIMARY_SOURCES.md:19,25,85`): Aleksandryan (1949/1960) credited for disk polynomial basis and arbitrarily near-disk non-almost-periodic examples; Zelenyak (1965) credited accurately for finite-time boundary dependence & explicit integral subspace (citing Aleksandryan p. 1225 ref. 3); Li (2024) strict inequality $|\log\alpha_\kappa(\lambda)| < \sqrt{3}\pi$.
5. Verify **4 Other Open Defects**:
   - `experiments/phase1_multiple.py`: `affine_edges` exact on $n=10^{20}$ integers (recovering $n/(n+1)$); `rational_rectangles` rejects floats (`TypeError`).
   - `experiments/phase1_parity.py` & `experiments/phase1_measure.py`: `column_height(10**20, 2, 3)`, `section_coordinate(10**20+1, 2, 3)`, `strip_coordinate(-10**20-1, mpf(2), mpf(3))` at 95 dps all exact.
   - `docs/phase1_scouting.md:152`, `docs/phase1_regular_measure.md:83`, `docs/RESEARCH_LOG.md:11-23`: rational-boundary-rotation terminology, $s=9/10$ ($\lambda=10/\sqrt{181}$), reduced-tilt extinction summary.
6. Verify `experiments/generate_phase2_previews.py` formulas match the proved theorems (`certified_shaving_measure`, `(1-1/sqrt(2))*6/pi^2`, `cot(2*phi) <= R <= tan(2*phi)`, `N=4m+2` `m_j` & quasimode bound, octagon Theorem 3, pentagon `B_i`).
7. Run `PYTHONDONTWRITEBYTECODE=1 python3 experiments/test_phase1_repairs.py` and `PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_probe.py`.

## Output
Concise sign-off table + explicit verdict: **`CLEAN — READY TO PITCH`** (if 0 open defects remain) or list any remaining blocker.
