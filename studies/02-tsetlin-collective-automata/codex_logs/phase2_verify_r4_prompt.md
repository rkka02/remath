# Phase 2 Round-4 Final Read-Only CLEAN Sign-Off Audit — Study #02 (`02-tsetlin-collective-automata`)

You are conducting a fast, focused **read-only final sign-off audit** verifying that ALL 9 moderate and 6 minor findings listed in `codex_logs/phase2_verify_r3_output.md` have been 100% repaired with ZERO regressions:

1. **M3** (`experiments/phase1_mpmath_check.py`): Confirm `1 + mp.eps` at 80 digits is rejected (`ValueError`) AND `(1/3, 2/3)` with `kappa = -1` at 30 digits gives exact zero double-loss transition (not `4.93e-32`).
2. **M7** (`experiments/phase1_aspect.py`): Confirm `-.5083870026647190707775001435296` at 30 digits returns non-`None` with exact `gamma_c - 1 ≈ 8.19613890845e-32` for both L and B, while `-.50838700266471908` still returns `None`.
3. **Historical sources** (`sources/PRIMARY_SOURCES.md`): Confirm Tsetlin (1963) §3 eq. (15) symmetric switching + swapped `(a,-a), (-a,a)` qualifier, §6 ergodicity + `n -> inf` qualifier, and Pittel (1965) explicit $B_{2n,2}$ vs $D'_{2n,2}$ weight distinction.
4. **Two R2 minor text/JSON fixes**: Confirm `docs/phase1_optimal_correlation.md:40` gives `1.971979021289...`, AND `experiments/data/phase2b_staghunt_grid.json` (`R=15/16, S=1/2, n=4` and other `fair_master_collapse` entries) now ends in `50876` computed from guard digits (and `experiments/phase2b_staghunt_robustness.py` uses `DIGITS + 8` guard digits).
5. **All 3 rendered pitch figures** (`experiments/generate_pitch_figures.py` + `figures/pitch_fig{1,2,3}_*.png`): Confirm every annotation matches the exact audited theorems and data:
   - Fig 1: title has `kappa_P < 1`, Panel B1/B2 use `digits=72`.
   - Fig 2: Panel A labels the three `(240, 80)` values as `L` masses; Panels B–D label `Corner CC (60,20)`, Panel C says `92.0% enter CC at (60,20)`, Panel D says `87.5% of B escapes visit site (40,19) (vs 0.63% for L)` and `B escape prob. = 8,994 x L`.
   - Fig 3: Panel A labels `sampled max`, Panel B title states `S = 1/2`, Panel C states `ONLY below-Nash efficient optimum` and `Quota-balance share A_n (opt. proved n <= 3)`.

## Output Format
1. **Executive Sign-Off Verdict**: **`CLEAN` (0 critical, 0 moderate, 0 minor)** or `REQUIRES FIXES` (with exact counts).
2. **Itemized Status Table (Items 1–5)**.
3. **Explicit Round-R2 Panel Clearance Statement**.
