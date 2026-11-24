# Phase 2 Read-Only Verification Audit — Confirming 100% Repair of `phase1_verify_output.md`

You are acting as a strict **`read-only` mathematical and software verifier** auditing `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors`.

Read `codex_logs/phase1_verify_output.md` and `codex_logs/phase2_repairs_output.md`, then verify EVERY SINGLE repair across ALL docs (`docs/phase1_*.md`) and ALL Python scripts (`experiments/phase1_*.py`, `experiments/test_phase1_repairs.py`):

1. Verify that **ALL 5 SEVERE/MAJOR defects** from `phase1_verify_output.md` are **100% resolved** and that NO new counterexamples or regressions were introduced:
   - Defect 1 (Theorem 4a in `docs/phase1_pde.md`): axis-aligned rectangle + proper corner cut + tilted-diamond counterexample noted.
   - Defect 2 (Theorem 1 in `docs/phase1_multiple.md`): characteristic-direction bound explicitly says **attracting** cycles (separate from repelling).
   - Defect 3 (`experiments/phase1_probe.py`): exact rational predicates with zero tolerance; floating/trig inputs certify strict signs or return `unresolved` (verify `s = 1 + 10^{-60}` on upright square!).
   - Defect 4 (`experiments/phase1_probe.py`): `CirclePL` uses precision-preserving floor in both directions (verify `x = 1 - 10^{-20}` at 95 digits!).
   - Defect 5 (`docs/phase1_scouting.md`): "even **regular** $N$-gon" fixed.
2. Verify that **ALL 12+ MINOR defects** (notation `T = \Delta_D^{-1}\partial_z^2` vs `P = \partial_z^2\Delta_D^{-1}`, reduced tilt `0 < \phi < \pi/4`, algebraic endpoint wording, L-triomino incompleteness wording, rational-vertex wording, historical credits for Nogueira–Troubetzkoy / Kopecz / Bajars–Frank–Maas / Lenci–Bonanno–Cristadoro / Soares / Zhu–Li / Zhang–Temnov, helper validations, rounding checks, octagon assertions, singular phase-portrait masking) are **100% resolved**.
3. Run `python3 experiments/test_phase1_repairs.py` and `python3 experiments/phase1_probe.py` (read-only execution) and probe for ANY newly introduced bug or mathematical gap.

Output a crisp, unambiguous **Final Pre-Pitch Verification Certificate**:
- Table confirming the status of all 5 SEVERE/MAJOR items, all MINOR items, and all 4 Flagship Pillars.
- Explicit verdict: **`CLEAN — READY TO PITCH`** (if 0 SEVERE, 0 MAJOR, 0 mathematical/code errors remain) or list any remaining defects.
