# Study #03 (`03-sobolev-wave-attractors`) — Scoped Final Read-Only Referee Verification (Round 8)

You are acting as a **strict, read-only mathematical & numerical referee** (`read-only` sandbox). Do NOT modify any files.

## Scope of This Final Verification Pass
Round 4 (`codex_logs/phase4_referee_r4_output.md`), Round 5, Round 6, and Round 7 already confirmed **ZERO defects** across:
- All 3 self-contained manuscripts (`paper1_uncloakable_coexistence.pdf` 19 pp., `paper2_tilt_rigidity_circle_limit.pdf` 20 pp., `expository_sobolev_attractors_kr.pdf` 8 pp.),
- All 10 dedicated embedded figures,
- The standalone Lean 4.36.0 formalization (`proofs/lean4/`, 125 public theorems including 40 principal results, 0 `sorry`, standard axioms only).

This **final verification pass (Round 8)** is explicitly scoped to confirming:
1. **All 10 Round 7 reproduced items (`codex_logs/phase4_referee_r7_output.md`) are cleanly closed** in `experiments/phase1_measure.py` and `experiments/phase1_regular.py`:
   - `170,000`-bit `ln 2` near-tie refinement (`_input_bit_budget` + `max_iters = 14`) in both `strip_position` and `strip_coordinate`.
   - Exact rational slope ratio `_exact_slope_ratio` (`mp.degree / mp.pi = 1/180`) in `strip_coordinate` (`strip_coordinate(181*t/180, mp.degree, mp.pi) == 0.5` by ties-to-even).
   - Near-pole `parameters(theta, phi, aspect)` adaptive outward interval evaluation (positive tangent & real square roots at `M = mp.pi/2, theta = 3/2, phi = M - theta - 2^{-320}, R = 1`).
   - Exact `involution(1 - 2^{-319}, 3 * 2^{-161}) ≈ 1.111111...` and exact `circle_distance(2**400, 1/4) == 0.25`.
   - Outward high-precision `corner_widths(4, 2**253 + 1) == 0.551419767598887...` matching a 420-digit reduction.
   - Outward decimal-rounded `--tongues` CLI brackets (`_fmt_ev`) enclosing the pentagon's true transition `[44.496034327574, 44.496034327575]`.
   - Boundary checks: `quadratic_roots(1, 0, 1/16, 1/4) == [0]` (strictly real at `discriminant == -tolerance`), `half_period_cells(4, 0, input_radius=-1)` raising `ValueError`, `np.complex128(1+2j)` raising `TypeError` in both strip helpers, and portable `frexp`/`ldexp` NumPy float extraction `_numpy_float_to_fraction` (no `float()` truncation on 80/128-bit `longdouble`).
2. **Zero regressions** across the 53-test unit suite (`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s studies/03-sobolev-wave-attractors/experiments -p 'test_*.py'`), both CLIs (`phase1_measure.py`, `phase1_regular.py --tongues`), and confirmation that the 3 compiled PDFs, 10 figures, and Lean 4 formalization remain untouched and valid since Round 4 acceptance.

**Out of scope for Round 8**: Do NOT conduct open-ended adversarial fuzzing of unbounded-bit edge cases outside the documented research helper contracts; restrict your verification strictly to items (1) and (2) above and any genuine regression in the Round 7 fixes.

## Required Output Format
Produce a concise two-section report:
- `## 1. FINAL VERDICT`: State clearly **`ZERO BLOCKING DEFECTS — ACCEPT AS IS (PUBLICATION SIGN-OFF GRANTED)`** if all Round 7 items are closed with zero regressions (or report any genuine failure in items 1–2).
- `## 2. FINAL SIGN-OFF SUMMARY`: Compact verification table covering all 10 Round 7 replays, unit test suite (53/53) & CLIs, and standing acceptance of the 3 manuscripts (19 + 20 + 8 pp.), 10 dedicated figures, and Lean 4.36.0 (`125` public theorems, `0 sorry`).
