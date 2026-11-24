# Phase 4 Read-Only Referee Audit — Round 3 (Final Sign-Off Verification)
**Study**: `02-tsetlin-collective-automata`
**Mode**: STRICT READ-ONLY REFEREE AUDIT (do NOT edit or write any files anywhere).

## Context
Round 1 (`codex_logs/phase4_referee_r1_output.md`) identified 5 critical, 30 moderate, and 5 minor items. Round 2 (`codex_logs/phase4_referee_r2_output.md`) verified 20 closed and identified **2 remaining critical (C1, C4), 11 remaining moderate (M1, M2, M4, M5, M6, M15, M16, M20, M23, M25, M26), and 8 minor (C5 minor, M8, M10, M18, M19, M22, M24, N1)** items.

All 21 remaining Round 2 items have now been repaired across:
1. `papers/paper1_correlated_automata/paper1_correlated_automata.tex` (and recompiled `.pdf`, 15 pp., 0 TeX warnings)
2. `papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex` (and recompiled `.pdf`, 11 pp., 0 TeX warnings)
3. `papers/expository_kr/expository_tsetlin_kr.tex` (and recompiled `.pdf`, 7 pp., 0 TeX/hyperref/overfull warnings)
4. `experiments/generate_paper_figures.py` (regenerated all 10 PNGs with `python3 -W error::UserWarning`, 0 warnings)
5. `proofs/lean4/` (re-verified via fresh `lake clean && lake build && lake env lean Main.lean`, exit 0, 0 warnings, 0 `sorry`, 911 audited theorem constants).

## Your Task (Strict Read-Only Verification)
1. **Verify EVERY SINGLE ONE of the 21 remaining Round 2 items** (`C1`, `C4`, `C5-minor`, `M1`, `M2`, `M4`, `M5`, `M6`, `M8`, `M10`, `M15`, `M16`, `M18`, `M19`, `M20`, `M22`, `M23`, `M24`, `M25`, `M26`, `N1`) directly against the updated `.tex` sources, compiled `.pdf` files, `experiments/generate_paper_figures.py`, and proof notes (`docs/`).
   - Especially scrutinize **C1** (Paper 1, Theorem 3.1 Parts 2 and 3 proof on PDF pages 5–6): check the upper bound $Q_{MC_0} \le e^{-n\min(H(T), H(S)+H(P))+o(n)}$, the indirect numerator branch, perfect $DD$ synchrony ($\kappa_P = 1$, arbitrary $\kappa_R$, for $L, B, D$), the general frozen-workload tail $\mu(W_1 \ge N, W_2 \ge m) \le C e^{-\theta(N+m)}(N^{-1/2}+m^{-1/2})$ + scalar ruin sum for $0 < \kappa_{\mathrm{eff}} < 1$, the separate product-kernel contraction $\mathcal{T}f(x) = \E_x[e^{H I_Y}f(X_1)]$ for $\kappa_P = 0$, the 2-core trace for $S \le 1/2$, and Krylov's thinned increment law throughout.
   - Scrutinize **C4** (Korean PDF page 4): confirm the phase-flip sentence now states the exact proved signs ($L \to 0\%$ mutual cooperation, $B \to 100\%$ mutual cooperation).
   - Scrutinize **M2** (Paper 1 Abstract + Theorem 3.3 + Korean text): confirm full support is stated consistently (`0 <= kappa_P < 1`, no undefined `E_1^K`).
   - Scrutinize **M15** (Paper 2 Theorem 3.1 proof two-sided compactness envelope $\delta_j G_n \lambda_j^n \le x e^{-(1-\max(0,b_j))x}$ and Korean subcritical condition $R < R_c(P,S)$).
   - Check that NO regressions or new mathematical, logical, numerical, typography, layout, or citation errors were introduced by the Round 2 -> Round 3 edits across all 33 compiled PDF pages (`15 + 11 + 7 = 33 pp.`).
2. **Output Structure**:
   - Executive Referee Verdict (`ACCEPT AS IS` if 0 critical and 0 moderate remain; otherwise list exact remaining counts).
   - Itemized closure table for all 21 Round 2 items (`C1`, `C4`, `C5-minor`, `M1`, `M2`, `M4`, `M5`, `M6`, `M8`, `M10`, `M15`, `M16`, `M18`, `M19`, `M20`, `M22`, `M23`, `M24`, `M25`, `M26`, `N1`) with exact file:line citations and verification notes.
   - Any newly detected issues (if any), and explicit final publication readiness sign-off.
