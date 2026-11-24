# Read-Only Mathematical Referee Audit — Round 5 (`phase4_referee_r5`)

You are conducting **Round 5 (read-only)** of the final mathematical referee audit for **Project ReMath Study #03 (`studies/03-sobolev-wave-attractors/`)**.

## Context
In Round 4 (`studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r4_output.md`), you confirmed that **all three manuscripts (Paper 1, Paper 2, Korean Expository), all ten figures (matching embedded PDF plates pixel-for-pixel), and the entire Lean 4.36.0 formalization (125 public / 40 principal theorems, 0 sorry, standard axioms only) PASSED completely**, leaving only two numerical edge cases in `phase1_regular.py` and `phase1_measure.py`.

Both remaining numerical edge cases have now been repaired and added to `test_phase1_repairs.py` (`test_referee_r4_regressions`, `50/50` tests):
1. **`phase1_regular.py` (`_cluster_events`, `half_events`, `vertex_half_events`, `half_period_cells`, and `--tongues` CLI formatter)**:
   - `_cluster_events` now ALWAYS preserves the true extreme outward event bounds `(lo, hi)` instead of collapsing narrow clusters to `(rep, rep)` before directional rounding.
   - Tightened the non-singleton `ivmpf` phase-width check at `ctx_dps == base_dps` to `2 * min_eps_q * scale_q` (keeping `iv.pi/36` at ratio `1.43` and `degree_interval` at `ctx_dps = base_dps + 8`, while rejecting `75`-digit `[3/8, 3/8 + 2^-251]` at ratio `2.67`).
   - Lowered `noise_floor` to `max(10^-(2*base_dps + 2), 32 * phi_span)` and upgraded line 555 so every unresolved event emits an outward interval `iv.mpf([lo_e - tol, hi_e + tol])` instead of a bare scalar (covering `Fraction(1, 10**90)`, `Fraction(1, 10**200)`, and pentagon `9° + 10^-82°` cleanly).
   - Updated the `--tongues` CLI printer to format interval entries in `unresolved` cleanly.
2. **`phase1_measure.py` (`_is_mp_constant`, `_exact_rational`, `strip_position`, `strip_coordinate`)**:
   - `_exact_rational` now explicitly excludes lazy precision-dependent mpmath constants (`_constant` / callable objects such as `mp.pi`, `mp.e`, `mp.phi`, `mp.euler`) so they are NEVER frozen at the caller's precision.
   - Both `strip_position` and `strip_coordinate` now use adaptive outward-interval refinement (`MPIntervalContext` doubling extra precision until both outward endpoints round identically to `mp.mp.prec`) whenever a lazy constant or non-exact input is present, fixing `strip_position(-mp.mpf(mp.pi), mp.pi, mp.pi)` and `strip_coordinate(1, mp.pi, 3)` (and `mp.e`, `mp.phi`, `mp.euler`) to exact 0-ULP correct rounding.

## Audit Instructions (Strictly Read-Only)
1. Replay all Round 4 numerical counterexamples directly (in read-only mode with `PYTHONDONTWRITEBYTECODE=1`):
   - `half_period_cells(4, iv75.mpf([3/8, 3/8 + 2^-251]))` at 75 digits,
   - `half_period_cells(4, Fraction(1, 10**90))` at 75 digits (probe `pi/4 + 10^-90 / 2`),
   - `half_period_cells(5, degree_interval(Fraction(9) + Fraction(1, 10**82)))` at 75 digits (probe `45° - 0.5e-82°`),
   - `strip_position(-mp.mpf(mp.pi), mp.pi, mp.pi)` and `strip_coordinate(1, mp.pi, 3)` at 95 digits.
2. Run the full test suite `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'` and check `phase1_regular.py --tongues`.
3. Output:
   - `## 1. REMAINING OR NEW BLOCKING DEFECTS` — if **NONE** remain, state explicitly at the top: **`ZERO BLOCKING DEFECTS — ACCEPT`**.
   - `## 2. FINAL SIGN-OFF SUMMARY`.
