# Read-Only Mathematical Referee Audit — Round 3 (`phase4_referee_r3`)

You are conducting **Round 3 (read-only)** of the final mathematical referee audit for **Project ReMath Study #03 (`studies/03-sobolev-wave-attractors/`)**.

## Context
In Round 2 (`studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r2_output.md`), you verified that 23 of 36 Round 1 blocking items and all 6 non-blocking items were already resolved, and identified a crisp remaining list:
- **10 manuscript & figure items** (Items 1–10 in Section 1 of Round 2),
- **6 numerical/code items** (`strip_coordinate`, `strip_position`, `half_period_cells` coarse interval + even/odd near-coincident events, `wall_correction` at huge $N = 10^{50}+2$, and NumPy-backed `Fraction` normalization in `phase1_parity.py` & `phase1_rectangle.py`),
- **Open Problem 3** (where both questions were resolved, so Open Problem 3 has been removed, leaving the two genuinely open problems in Section 5.1 of Paper 2),
- **4 non-blocking editorial notes** (Thm. 3.4 figure legend, naming $C,b$ in Fig. 2C caption, $0 < p < q$ in upright rectangle theorem, and both directed cycles $1/16, 16$ in Korean line 139).

All of these items have now been repaired, the 3 affected figures (`p2_fig1`, `p2_fig2`, `kr_fig2`) have been regenerated, all 3 PDFs have been recompiled cleanly with `tectonic` (0 errors, 0 Overfull warnings), and `test_phase1_repairs.py` has been expanded to `48/48` passing tests covering every Round 1 and Round 2 counterexample.

## Audit Instructions (Strictly Read-Only)
1. **Verify every single Round 2 item**:
   - Check Items 1–10 and Open Problem 3 removal across:
     - `studies/03-sobolev-wave-attractors/papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.tex` and `.pdf` (19 pp.)
     - `studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex` and `.pdf` (20 pp.)
     - `studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex` and `.pdf` (8 pp.)
     - `studies/03-sobolev-wave-attractors/experiments/generate_paper_figures.py` and the regenerated PNGs (`p2_fig1`, `p2_fig2`, `kr_fig2`).
   - Replay ALL 6 Round 2 numerical/code counterexamples directly (and try to find any remaining edge cases) in read-only mode (`PYTHONDONTWRITEBYTECODE=1`):
     - `strip_coordinate(1, 1, 2**320 - 2)` vs `1.0` vs `"1"` at 95 digits,
     - `strip_position(2**321, 48, 96)` at 95 digits,
     - `half_period_cells` with 10-digit interval `[1/16, 1/16 + 2**-40]` at 75 digits,
     - `half_period_cells` at square `22.5° + 10^-68°` (75 digits) and pentagon `9° + 10^-40°` (75 and 150 digits) & `9° + 10^-72°` (75 digits),
     - `wall_correction(10**50 + 2)` at 75 digits,
     - NumPy-backed `Fraction` inputs to `column_height`, `section_coordinate`, `normal_return`, `section_endpoint`, `section_tongue`.
   - Run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'`.
   - Confirm embedded figures in the 3 compiled PDFs match their regenerated source PNGs.
2. **Hunt for any remaining or newly introduced mathematical, logical, numerical, figure, citation, or code defect**.
3. **Output Format**:
   - **Section 1: `## 1. REMAINING OR NEW BLOCKING DEFECTS`**
     - If **NONE** remain, state explicitly at the top: **`ZERO BLOCKING DEFECTS — ACCEPT`**.
     - Otherwise list every genuine blocking defect with exact file, line number, and counterexample/gap.
   - **Section 2: `## 2. ROUND 2 VERIFICATION MATRIX AND FINAL AUDIT SUMMARY`**
     - Concise verification status for all 10 manuscript/figure items, all 6 numerical/code items, Open Problem 3, and the 4 non-blocking notes.
