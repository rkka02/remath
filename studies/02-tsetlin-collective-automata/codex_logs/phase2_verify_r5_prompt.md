# Study #02 — Final Focused Read-Only Sign-Off Audit (`phase2_verify_r5`)

You are the strict read-only mathematical & numerical referee (`gpt-6.2-astra`, max reasoning) performing the **final sign-off check** on the 4 remaining code/JSON items flagged in `codex_logs/phase2_verify_r4_output.md` (where all theorems, proofs, historical sources, and rendered pitch-figure annotations had already passed).

**Read-only mode**: Do NOT modify any files. Only inspect, execute read-only verification snippets, and deliver a concise PASS/FAIL table + explicit Round-R2 panel clearance verdict.

## Items to Verify (from `phase2_verify_r4_output.md`)

1. **`experiments/phase1_mpmath_check.py`** (`_to_exact_fraction` & `_exact_frechet_check`):
   - Verify `mp.nan`, `mp.inf`, `-mp.inf`, `float('nan')`, `float('inf')`, `-float('inf')`, `Decimal('NaN')`, `Decimal('Inf')` are all strictly rejected with `ValueError` (never mapped to zero).
   - Verify `1 + mp.eps` at 80 digits still raises `ValueError`, and `(1/3, 2/3), kappa = -1` at 30 digits gives exact zero double-loss transition.
2. **`experiments/phase1_aspect.py`** (`_to_exact_fraction` & `critical_ratio`):
   - Verify passing `mp.mpf('-.5083870026647190707775001435296')` created at 80 digits while global `mp.mp.dps = 30` returns the exact positive root `gamma_c - 1 = 8.196138908446...e-32` for both `L` and `B`, while `-.50838700266471908` (as string or 80-digit `mpf`) returns `None`.
   - Verify infeasible/non-finite inputs (`mp.nan`, `mp.inf`, `1 + mp.eps`, `-1`) raise `ValueError`.
3. **`experiments/phase2b_staghunt_robustness.py` & `experiments/data/phase2b_staghunt_grid.json`**:
   - Verify `rectangles()` and exact determinant verification pass cleanly (no `AssertionError`) using exact rational enclosure + 76-digit agreement, and that `scaled()` matches the metadata `"94-digit Decimal arithmetic"`.
   - Spot-check ALL 12 `two_parameter_crossover` ordinates (especially `R=9604/10229, S=49/99, n=12` -> suffix `88094`) and `fair_master_collapse` (`R=15/16, S=1/2, n=4` -> suffix `50876`) against exact rational stationary odds to confirm 0-ULP agreement to 76 significant digits.
4. **`experiments/generate_pitch_figures.py`**:
   - Verify the docstring accurately reflects the precision (`70-80 digits` saved data + `80-digit` subtraction-free GTH solves for Panel B1/B2) and that Panel B1/B2 use `digits=80` (giving exact 72+ digit agreement on depth-8 `L`).

## Output Format
Produce a concise Markdown report with:
1. **Executive Sign-Off Verdict**: `CLEAN (0 critical, 0 moderate, 0 minor)` or `REQUIRES FIXES` with exact counts.
2. **4-Row Verification Table** with exact numerical/code checks.
3. **Round-R2 Panel Clearance**: explicit statement clearing (or withholding) the Study #02 Round-R2 package for the 3-Judge Wow-Factor Panel.
