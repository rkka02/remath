# Read-Only Mathematical Referee Audit — Round 2 (`phase4_referee_r2`)

You are an uncompromising, world-class mathematical referee conducting **Round 2 (read-only)** of the final publication audit for **Project ReMath Study #03 (`studies/03-sobolev-wave-attractors/`)**.

## Context
In Round 1 (`studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r1_output.md`), you identified 36 blocking defects (`B1`–`B36`) and 6 non-blocking editorial notes (`N1`–`N6`) across the three manuscripts, ten figures, Python verification scripts, and Lean 4 formalization.

All 36 blocking defects and all 6 non-blocking notes have now been repaired, all 10 figures have been regenerated, all 3 PDFs have been recompiled with `tectonic` (0 errors, 0 Overfull warnings), and the Python regression suite has been expanded (`47/47` tests).

## Files to Audit (Read-Only)
1. **Round 1 Audit Baseline**:
   - `studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r1_output.md`
2. **Three Revised Manuscripts (TeX + Compiled PDFs)**:
   - `studies/03-sobolev-wave-attractors/papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.tex` and `.pdf` (19 pp.)
   - `studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex` and `.pdf` (20 pp.)
   - `studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex` and `.pdf` (8 pp.)
3. **Ten Regenerated Figures & Generator**:
   - `studies/03-sobolev-wave-attractors/experiments/generate_paper_figures.py`
   - All PNGs in `papers/paper1_uncloakable_coexistence/figs/`, `papers/paper2_tilt_rigidity_circle_limit/figs/`, and `papers/expository_kr/figs/`.
4. **Repaired Python Verification Code & Tests**:
   - `studies/03-sobolev-wave-attractors/experiments/phase1_multiple.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_probe.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_measure.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_regular.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_pde.py`
   - `studies/03-sobolev-wave-attractors/experiments/test_phase1_repairs.py`
5. **Lean 4 Formalization (verify consistency with Tables 2 of Papers 1 & 2 and Korean summary)**:
   - `studies/03-sobolev-wave-attractors/proofs/lean4/*.lean`

## Audit Instructions
1. **Verify every single Round 1 item (`B1`–`B36` and `N1`–`N6`)**:
   - Check that every repaired theorem statement, proof step, sign, coordinate convention, interval restriction, uniform asymptotic, bibliography entry, figure panel, caption, and Korean exposition claim is now 100% mathematically, logically, numerically, and historically accurate.
   - Actively test ALL four Round 1 numerical/code counterexamples (`B30a`, `B30b`, `B31a`, `B31b`) — plus try to craft NEW adversarial inputs — against the repaired Python functions in read-only mode (do not write files or `__pycache__`; use `PYTHONDONTWRITEBYTECODE=1`).
   - Run the full Python unit test suite (`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'`).
   - Check that the repaired figures visually and quantitatively match their captions and underlying data (`p1_fig1`–`p1_fig3`, `p2_fig1`–`p2_fig3`, `kr_fig1`–`kr_fig4`).
2. **Hunt relentlessly for ANY remaining or newly introduced defects**:
   - Check for variable collisions, missing hypotheses, broken cross-references, subtle gaps in newly expanded proofs (e.g. Paper 1 complex uncloakability, apothem-1 critical $\beta=0$ modes, Paper 2 physical monotonicity, uniform $E_1$ summation, general proper-cut existence & global plateau exclusion, regular-$N$-gon arclength conjugation, mirror-axis maximizers, Open Problem 3).
   - Check internal consistency across Paper 1, Paper 2, the Korean feature, and the Lean 4 tables.
3. **Output Format**:
   - **Section 1: `## 1. REMAINING OR NEW BLOCKING DEFECTS`**
     - List every genuine mathematical, logical, numerical, figure, citation, or code defect that still blocks acceptance, with exact file, line number, counterexample or proof gap, and required fix.
     - If **NONE** remain, state explicitly: **`ZERO BLOCKING DEFECTS — ACCEPT`**.
   - **Section 2: `## 2. VERIFICATION MATRIX (B1–B36 & N1–N6) AND NON-BLOCKING NOTES`**
     - Give a concise line-by-line status (`RESOLVED` / `REMAINING`) for `B1`–`B36` and `N1`–`N6`, plus any purely optional non-blocking polish notes.
