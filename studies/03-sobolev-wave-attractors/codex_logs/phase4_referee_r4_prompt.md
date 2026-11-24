# Read-Only Mathematical Referee Audit — Round 4 (`phase4_referee_r4`)

You are conducting **Round 4 (read-only)** of the final mathematical referee audit for **Project ReMath Study #03 (`studies/03-sobolev-wave-attractors/`)**.

## Context
In Round 3 (`studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r3_output.md`), Paper 1 passed completely with zero defects, Lean 4.36.0 passed completely (`125` public / `40` principal theorems, `0 sorry`, standard axioms only), and only 6 specific items plus 2 input-validation notes remained across Paper 2, the Korean feature, `generate_paper_figures.py`, `phase1_regular.py`, `phase1_measure.py`, and `phase1_rectangle.py`.

All 6 remaining items, both input-validation notes, and the 2 stale comments in `generate_paper_figures.py` have now been repaired:
1. **Korean corner-shaving liminf wording** (`expository_sobolev_attractors_kr.tex` lines 144 & 158, `generate_paper_figures.py` line 890): Clarified explicitly that $C = \frac{6}{\pi^2}(1-1/\sqrt{2}) = 17.80577\ldots\%$ is the limit of the certified disjoint whole-plateau sums, establishing the **lower bound** $\liminf_{\varepsilon\downarrow 0} |\mathcal{A}_\varepsilon|_\lambda \ge C > 17.805\%$ (never asserting equality for the total liminf).
2. **`half_period_cells` phase reduction, interval soundness, and inward rounding** (`phase1_regular.py`):
   - Extracts exact rational endpoints `(lo_q, hi_q)` without premature rounding to `base_dps`.
   - Rejects non-exact intervals exceeding `4 * min(mp_eps, ctx_eps) * min(|mid|, 7)` (catching 100-digit `[3/8, 3/8 + 2^-251]`, 75-digit `[3/8, 3/8 + 2^-251]`, and coarse intervals) while keeping `iv.pi/36` and `degree_interval(...)`.
   - Reduces exact/interval phases modulo `2*pi/n` at `2*base_dps + 24 + int(mag_bits * 0.35) + 12` digits (fixing `2**253 + 1` radians cleanly).
   - Generates events at both `(phi_lo_red, phi_hi_red)` at `2*base_dps + 24` digits and rounds every returned `inside` cell strictly inward (`round_ceiling` on left endpoint, `round_floor` on right endpoint) while enclosing merged clusters outward in `unresolved` (fixing `22.5° + 10^-69°` and `9° + 10^-74°`).
3. **Separate-context `mpf` and singleton `ivmpf` in `strip_coordinate` & `strip_position`** (`phase1_measure.py`): `_exact_rational` now recognizes any object carrying `_mpf_` (finite) or singleton `_mpi_` (`a == b`, finite).
4. **Half-rotation endpoint diameter** (`paper2_tilt_rigidity_circle_limit.tex` line 473): Specified reflection in symmetry axis $L$ puts $p$ on the **perpendicular diameter $L^\perp$ (the first-flight direction)**.
5. **Open Problem 2 wording** (`paper2_tilt_rigidity_circle_limit.tex` line 512): Corrected "eigenvalues" to **"eigenangles"** inside $E_{R,\phi}$ before defining $S_{R,\phi} = \{\cos^2\theta : \theta \in E_{R,\phi}\}$.
6. **Korean Figure 3A caption & Figure 4B legend** (`expository_sobolev_attractors_kr.tex` line 170, `generate_paper_figures.py` line 1034): Removed "그 가운데" so $u_h$ is identified as belonging to the same eigenspace as the smooth modes (not one of the smooth modes), and updated Figure 4B's legend to `"정렬된 팔각형 (0°): 모든 광선 중립 (b^2 = Id, Lambda = 0)"`.
7. **Input validation & comments**: `wall_correction` now accepts NumPy integer scalars (`np.int64(1002)`), `section_tongue` rejects non-integer `Fraction` windings (`Fraction(3,2)` raises `TypeError`), and stale white-pixel comments in `generate_paper_figures.py` are updated. `test_phase1_repairs.py` now has `49/49` passing tests covering every Round 1, 2, and 3 counterexample.

## Audit Instructions (Strictly Read-Only)
1. Verify every single item above across the compiled PDFs (`paper2_tilt_rigidity_circle_limit.pdf`, `expository_sobolev_attractors_kr.pdf`), `.tex` sources, regenerated figures (`kr_fig2`, `kr_fig4`), and Python modules.
2. Replay all Round 3 code counterexamples (and test any edge cases you wish) in read-only mode (`PYTHONDONTWRITEBYTECODE=1`) and run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'`.
3. Output two sections:
   - `## 1. REMAINING OR NEW BLOCKING DEFECTS` — if **NONE** remain, state explicitly **`ZERO BLOCKING DEFECTS — ACCEPT`** at the top.
   - `## 2. FINAL ROUND 3 VERIFICATION SUMMARY`.
