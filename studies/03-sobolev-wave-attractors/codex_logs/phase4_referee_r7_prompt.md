# Study #03 (`03-sobolev-wave-attractors`) — Read-Only Mathematical & Numerical Referee Audit (Round 7)

You are acting as a **strict, read-only mathematical & numerical referee** (`read-only` sandbox). Do NOT modify any files.

Round 4 (`codex_logs/phase4_referee_r4_output.md`), Round 5, and Round 6 have already accepted with **ZERO defects**:
- All three non-overlapping manuscripts (`paper1_uncloakable_coexistence.pdf` 19 pp., `paper2_tilt_rigidity_circle_limit.pdf` 20 pp., `expository_sobolev_attractors_kr.pdf` 8 pp.),
- All 10 dedicated embedded figures,
- The standalone Lean 4.36.0 formalization (`proofs/lean4/`, 125 public theorems including 40 principal results).

Round 6 (`codex_logs/phase4_referee_r6_output.md`) identified **5 numerical edge-case defects** in `experiments/phase1_regular.py` and `experiments/phase1_measure.py` (plus one historical discrepancy note in `docs/phase1_measure.md:197`). All 5 defects and the doc note have been repaired, with regression tests added in `experiments/test_phase1_repairs.py` (`test_referee_r6_regressions`, now **52 tests total**):

1. **`half_period_cells` lazy mathematical constants (`experiments/phase1_regular.py`)**:
   - `_exact_phase_endpoints` now detects precision-independent lazy `mpmath` mathematical `_constant`s (excluding context-dependent `eps`) before `_mpf_`, and `half_period_cells` encloses them via `lazy_const.func(iv_red.prec, round_floor/round_ceiling)` with outward interval reduction modulo `2*pi/n` at `red_dps >= 2*base_dps + 48`.
   - Also added `hasattr(phi, "_mpq_")` (ahead of `numbers.Rational`) for `mpmath.rational.mpq` and explicit rejection of `bool`.
   - Verify Round 6 counterexample: at 75 digits, `half_period_cells(4, mp.e)` (and cloned `c.e`) excludes `theta = 2^{-253} floor(2^{253} (pi - e))` from `inside` and encloses it in `unresolved`.

2. **`mp.eps` / cloned `c.eps` preservation (`experiments/phase1_measure.py`)**:
   - Removed `or callable(val)` from `_is_mp_constant` so `_constant` `eps` (which is callable in `mpmath`) is never re-evaluated inside higher precision, instead reading its exact context value `val._mpf_` once via `_exact_rational`.
   - Verify Round 6 counterexamples at 95 digits: `strip_position(mp.eps, 1, 1) == 1 + 2^{-318}` and `strip_position(-Fraction(1, 2**52), c.eps, c.eps) == 0` for a 15-digit clone `c`.

3. **Exact `mpmath.rational.mpq` support & removal of silent scalar fallback (`experiments/phase1_measure.py`)**:
   - `_exact_rational` checks `hasattr(val, "_mpq_")` before `numbers.Rational` so `mpq` is converted losslessly to `Fraction`.
   - Removed the uncertified `mp.mpmathify` singleton fallback in `_exact_bounds`; non-finite reals raise `ValueError` and unsupported types raise `TypeError`.
   - Verify Round 6 counterexample: `strip_position(mpq(-1, 3), Fraction(1, 3), Fraction(1, 3)) == 0`.

4. **Arbitrary callable rejection (`experiments/phase1_measure.py`)**:
   - Arbitrary Python callables (such as `lambda: (mp.mpf(2)**1000 + 1) - mp.mpf(2)**1000`) now raise `TypeError` instead of applying an uncertified error bound.

5. **Refinable lazy constants never trigger the fixed-interval early exit (`experiments/phase1_measure.py`)**:
   - Guarded the non-singleton early exit with `not _is_math_constant(...)` (and added symmetric fast early exits for fixed non-singleton `a` and `b` intervals).
   - Verify Round 6 counterexamples at 95 digits: with `q = 2^{-800} floor(2^{800} ln 2)`, `s = 1 + 2^{-319} - q`, `t = 1/2 + 2^{-320}`, `strip_position(mp.ln2, s, s) == 1 + 2^{-318}` and `strip_coordinate(mp.ln2, q - t, t) == 1/2 + 2^{-319}`.

6. **Historical CLI discrepancy bound (`docs/phase1_measure.md:197`)**:
   - Updated `$1.5\times10^{-95}$` to `$2.3\times10^{-95}$` to match the current exact-rounding CLI maximum discrepancy `2.247e-95`.

## Audit Tasks
1. Independently run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'` (confirm 52/52 pass) and run `phase1_regular.py --tongues` and `phase1_measure.py`.
2. Independently verify all 5 Round 6 repairs and probe `experiments/phase1_regular.py` and `experiments/phase1_measure.py` for any remaining numerical or soundness defects.
3. Produce a concise two-section report:
   - `## 1. REMAINING OR NEW BLOCKING DEFECTS` (explicitly state **`ZERO BLOCKING DEFECTS — ACCEPT`** if none remain).
   - `## 2. FINAL SIGN-OFF SUMMARY` (compact table summarizing Round 6 replays, fresh adversarial probes, unit tests & CLIs, and standing Round 4 acceptance of all 3 manuscripts, all 10 figures, and Lean 4.36.0).
