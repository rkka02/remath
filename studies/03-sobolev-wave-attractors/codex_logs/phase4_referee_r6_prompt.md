# Study #03 (`03-sobolev-wave-attractors`) — Read-Only Mathematical & Numerical Referee Audit (Round 6)

You are acting as a **strict, read-only mathematical & numerical referee** (`read-only` sandbox). Do NOT modify any files.

Round 4 (`codex_logs/phase4_referee_r4_output.md`) and Round 5 (`codex_logs/phase4_referee_r5_output.md`) have already accepted with **ZERO defects**:
- All three non-overlapping manuscripts (`paper1_uncloakable_coexistence.pdf` 19 pp., `paper2_tilt_rigidity_circle_limit.pdf` 20 pp., `expository_sobolev_attractors_kr.pdf` 8 pp.),
- All 10 dedicated embedded figures,
- The standalone Lean 4.36.0 formalization (`proofs/lean4/`, 125 public theorems including 40 principal results).

Round 5 identified **4 narrow Python numerical edge cases** in `experiments/phase1_regular.py` and `experiments/phase1_measure.py`. All 4 have now been repaired, with regression tests added in `experiments/test_phase1_repairs.py` (`test_referee_r5_regressions`, now **51 tests total**):

1. **`half_period_cells` boundary sliver contiguity (`experiments/phase1_regular.py`)**:
   - Added `eval_pad = 10^{-max(24, 2*base_dps - 10)}` prior to outward rounding `(lo_r, hi_r)` at `base_prec` in both `half_events` and `vertex_half_events`.
   - Every active open cell `(left_end, right_end) = (hi_idx, lo_{idx+1})` now unconditionally emits its trimmed boundary slivers `[lo_idx, hi_idx]` and `[lo_{idx+1}, hi_{idx+1}]` into `unresolved` (and encloses the entire cell in `unresolved` if `left_end >= right_end`), giving exact bit-for-bit gap-free contiguity (`unres[0].b == cell.a` and `unres[1].a == cell.b`).
   - Removed the premature `if curve.support_vertices:` exit from `event_status` so `power.displacement(1)` directly certifies same-side exclusion using `margin = max(power.error, power.tol)`.
   - Verify Round 5 counterexamples:
     - Exact square phase `phi = Fraction(1, 2)` at 75 digits (probes `1/2`, `1/2 + 2^{-253}`, `1/2 + 2^{-252}`).
     - Accepted 75-digit phase interval `[3/8, 3/8 + 2^{-252}]` (probes `pi/4 - 3/8 - 2^{-253}` and `pi/4 + 3/8 + 2^{-253}`).
     - Plus any fresh adversarial `half_period_cells` boundary/interval probes you choose.

2. **`strip_coordinate` & `strip_position` exact monotonicity + equal-slope shortcut + zero silent scalar fallback (`experiments/phase1_measure.py`)**:
   - Replaced the uncertified scalar fallback in both `strip_coordinate` and `strip_position` with exact rational monotonic endpoint enclosures:
     - $P(y; a, b)$ is continuous and increasing in $(y, a, b)$ on $a, b > 0$, so $P(y_{\text{lo}}; a_{\text{lo}}, b_{\text{lo}}) \le P(y; a, b) \le P(y_{\text{hi}}; a_{\text{hi}}, b_{\text{hi}})$.
     - $T(y; a, b)$ is continuous, strictly increasing in $y$, non-increasing in $a$, and non-decreasing in $b$, so $T(y_{\text{lo}}; a_{\text{hi}}, b_{\text{lo}}) \le T(y; a, b) \le T(y_{\text{hi}}; a_{\text{lo}}, b_{\text{hi}})$.
     - Equal slopes (`_same_slope(a, b)`, including identical lazy constants across default and cloned contexts via `a.func is b.func`) use the exact identities $T(y; a, a) = y/2$ and $P(y; a, a) = y + a$.
     - Raises `ValueError` rather than silently returning an uncertified scalar if inputs are non-positive, non-finite, or non-singleton intervals that do not uniquely determine a rounded output at active working precision.
   - Verify Round 5 counterexamples:
     - `strip_coordinate(Fraction(1, 2) + Fraction(15, 1 << 320), mp.pi, mp.pi)` at 95 digits -> exact ties-to-even `1/4 + 8 * 2^{-320}`.
     - `strip_position(-Fraction(1, 3), mp.pi, Fraction(1, 3))` at 95 digits -> exact `0`.

3. **Cloned-context lazy mathematical constants (`experiments/phase1_measure.py`)**:
   - `_is_math_constant` and `_exact_bounds` evaluate all 13 lazy `mpmath` mathematical `_constant`s (`pi, e, phi, euler, catalan, khinchin, glaisher, apery, mertens, twinprime, ln2, ln10, degree`) from ANY default or cloned context via `val.func(prec, round_floor)` and `val.func(prec, round_ceiling)` at full adaptive `prec`, while keeping context-specific `c.eps` at its own value.
   - Verify Round 5 counterexamples: `c = mp.mp.clone(); c.dps = 15` with `c.e`, `c.phi`, `c.euler` (and other constants) in `strip_coordinate` and `strip_position` at 95 digits -> 0 ULP error.

4. **Non-singleton `ivmpf` interval inputs (`experiments/phase1_measure.py`)**:
   - `_exact_bounds` reads exact rational endpoints via `to_rational(val._mpi_[0/1])` with zero `NotImplementedError` and zero conversion loss.
   - Verify Round 5 counterexamples: `y = iv.mpf([1/4, 1/4 + 2^{-400}])`, `a = b = 1` at 95 digits -> exact `0.125` (`strip_coordinate`) and `1.25` (`strip_position`), plus rejection (`ValueError`) on genuinely ambiguous intervals.

## Audit Tasks
1. Independently execute `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'` and `PYTHONDONTWRITEBYTECODE=1 python3 studies/03-sobolev-wave-attractors/experiments/phase1_regular.py --tongues` and `phase1_measure.py`.
2. Independently probe all 4 Round 5 repairs and attempt to break `experiments/phase1_regular.py` and `experiments/phase1_measure.py` with fresh adversarial edge cases.
3. Produce a concise report with two sections:
   - `## 1. REMAINING OR NEW BLOCKING DEFECTS` (state clearly **`ZERO BLOCKING DEFECTS — ACCEPT`** if none remain, or list any genuine mathematical/numerical defect with exact file/line and counterexample).
   - `## 2. FINAL SIGN-OFF SUMMARY` (compact table summarizing Round 5 replay verification, fresh adversarial probes, unit tests & CLI, and standing Round 4 acceptance of all 3 manuscripts, all 10 figures, and Lean 4.36.0).
