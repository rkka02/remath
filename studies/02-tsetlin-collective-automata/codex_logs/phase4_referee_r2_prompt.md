# Study #02 — Phase 4 Read-Only Mathematical Referee Audit Round 2 (`phase4_referee_r2`)

You are the strict read-only mathematical referee (`gpt-6.2-astra`, max reasoning) performing **Round 2 re-verification** of **Project ReMath Study #02 (`02-tsetlin-collective-automata`)** following full repairs of all 5 critical, 30 moderate, and 5 minor findings reported in `codex_logs/phase4_referee_r1_output.md`.

**STRICT READ-ONLY MODE**: Do NOT edit, create, or delete any files.

## Verification Checklist
1. **Verify ALL 5 Critical Repairs (`C1–C5`)**:
   - `C1` (`Paper 1`, Theorem 3.1 proof): aggregate numerator bounds, synchronized deterministic $\kappa_R=\kappa_P=1$ handled separately, survey-$D$ compulsory loss-window bound covering $B_P=0$, and renewal-reward excursion-occupation comparison for the $n^{-1/2}$ prefactor.
   - `C2` (`Paper 2`, Theorem 4.2(1)): feasibility criterion $R_n(c) \ge r_\theta$, strict increase over feasible depths, eventual feasibility for $p_* > 1/2$, and benchmark all-depth feasibility.
   - `C3` (`Paper 2`, Theorem 4.2(1)–(2)): large-depth quorum loss restricted to the one-quarter benchmark (avoiding the general counterexample), and $N=4, \alpha=0.99 \implies W_{4,n}\to 0.82$ stated accurately as fixed-$N$ dependence rather than claiming the reversed iterated outer limit.
   - `C4` (`KR`, Section 3): $8{,}994\times$ amplification ends at per-excursion escape probability in $(60,20), R=0.80, \kappa_P=0.99$, paired separately with the phase-flip example $(R=0.78, \gamma=2, \kappa_P=0.99)$.
   - `C5` (`Paper 2`, Fig. 1 caption & `generate_paper_figures.py` / `p2_fig1_memory_cliffs.png`): legend and caption both read `Unanimous defection -> 1 (peer coop -> 0, d > d_*)`, shading stops at $d/h = 1$, arrow points strictly above the curve, and y-axis reads `Defection advantage / public benefit (d/h)`.
2. **Verify ALL 30 Moderate Repairs (`M1–M30`) and ALL 5 Minor Repairs (`S1–S5`)** across:
   - `papers/paper1_correlated_automata/paper1_correlated_automata.tex` (+ compiled `.pdf`),
   - `papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex` (+ compiled `.pdf`),
   - `papers/expository_kr/expository_tsetlin_kr.tex` (+ compiled `.pdf`),
   - `experiments/generate_paper_figures.py` (+ all 10 PNGs embedded in the 3 PDFs),
   - Bibliography entries (`Krinskii1964`, `Krinskii1966`, `Gurvich1975`, `Jiao2021`, `Belaid2023`, `DJR2019`).
3. **Check for ANY newly introduced errors** (math, signs, hypotheses, numbers, Lean cross-references, figure/PDF embedding parity, or LaTeX glitches).

## Required Output Format
1. **Executive Referee Verdict**: `ACCEPT AS IS (0 critical, 0 moderate, 0 minor)` or `REVISIONS REQUIRED` with exact counts.
2. **Itemized Resolution Audit** confirming `C1–C5`, `M1–M30`, `S1–S5` (highlighting any remaining or newly introduced issue with exact `file:line`, reason, and minimal fix).
3. **Final Publication Readiness Sign-Off**.
