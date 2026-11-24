# Phase 4 Read-Only Referee Audit — Round 4 (Final Publication Sign-Off Check)
**Study**: `02-tsetlin-collective-automata`
**Mode**: STRICT READ-ONLY REFEREE AUDIT (do NOT edit or write any files anywhere).

## Context
Round 3 (`codex_logs/phase4_referee_r3_output.md`) closed 17 of the 21 Round 2 items (37 of 41 cumulative items closed, including 100% of Paper 2, all 10 figures, all 107 internal PDF links, and the entire Lean 4 suite of 911 theorem constants) and identified **4 localized remaining items**:
1. **C1 (Critical, `paper1_correlated_automata.tex:178`)**: Removed the false $Q_{D_0 M} = 0$ assertion at $\kappa_P = 1$ with arbitrary feasible $\kappa_R$, replacing it with the exact squeeze $Q_{D_0 C_0} \le N_D \le Q_{D_0 C_0} + Q_{D_0 M}$, scalar first-passage upper bound $O(e^{-n H(P)})$ on total exit from $D_0$, and simultaneous switch + $CC$ maturation lower bound $Q_{D_0 C_0} \ge e^{-n H(P) + o(n)}$ (with factor $1/4$ for $B$, $A_R > 0$ for $D$, and $A_R \ge 2R-1 > 0$ for $L,B$; plus explicit mention of the 2-core trace $\{C_0, D_0\}$ for $L,B$ with $S \le 1/2 < P$).
2. **M2 (Moderate, `paper1_correlated_automata.tex:232` & `expository_tsetlin_kr.tex:111, 143, 152`)**: Removed the false equivalence `i.e. kappa_R, kappa_P < 1`, stating exact weak-reward full support $-\frac{p}{1-p} < \kappa_p < 1$ for $p \in \{R,P\} < 1/2$, and explicitly stating $0 \le \kappa_P < 1$ alongside full support in all three Korean weak-reward reversal passages.
3. **M15 (Moderate, `expository_tsetlin_kr.tex:195`)**: Scoped the Korean Stag Hunt 100%-peak statement strictly to the existence of subcritical ($R < R_c(P,S)$) approach paths from either side of $S = 1/2$ to the joint critical point $(S, R) = (1/2, R_c(P, 1/2))$, matching Paper 2 Theorem 3.1(3).
4. **M23 (Minor, `experiments/generate_paper_figures.py:190`)**: Replaced the comment `"exact 80-digit sweeps"` with `"80-digit working-precision GTH sweeps"`.

Both modified PDFs (`paper1_correlated_automata.pdf`, 15 pp.; `expository_tsetlin_kr.pdf`, 7 pp.) were recompiled with `/opt/homebrew/bin/tectonic --print` with zero errors and zero overfull/underfull/hyperref warnings.

## Your Task (Strict Read-Only Final Verification)
1. Verify all 4 remaining Round 3 items (**C1, M2, M15, M23**) directly against the updated `.tex` sources, compiled `.pdf` files, and `experiments/generate_paper_figures.py`.
2. Confirm no typography, pagination, or mathematical regression was introduced on the edited PDF pages (Paper 1 pages 5, 8; Korean pages 1, 3, 5, 7).
3. Issue your final executive referee verdict (`ACCEPT AS IS — PUBLICATION SIGN-OFF GRANTED` if 0 critical, 0 moderate, and 0 minor remain; otherwise list exact remaining items).
