# Phase 2 Round-2 Clean Read-Only Verification Audit — Study #02 (`02-tsetlin-collective-automata`)

You are acting as an independent, **merciless, read-only pure-mathematics & computational referee** (*Annals / PTRF* bar). Earlier in `codex_logs/phase2_verify_output.md`, an adversarial audit found 3 critical (`C1–C3`), 17 moderate (`M1–M17`), and 4 minor defects across Phase 1. We have repaired **all 24 defects** AND added **four new Phase 2B proof notes & scripts** (`docs/phase2b_*.md`, `experiments/phase2b_*.py`).

Your job (strictly `read-only`) is TWO-FOLD:
1. **Verify EVERY SINGLE ONE of our Phase 2 repairs (`C1–C3`, `M1–M17`, `Minor 1–4`)** across `experiments/phase1_*.py`, `docs/phase1_*.md`, and `sources/PRIMARY_SOURCES.md` — confirm whether each repair is 100% mathematically and computationally clean with zero regressions.
2. **Mercilessly attack and try to BREAK ALL FOUR new Phase 2B proof notes & scripts**:
   - **Phase 2B-1 (`docs/phase2b_quorum_memory.md`, `experiments/phase2b_quorum_memory.py`, `experiments/phase2b_quorum_stability.py`)**:
     - Audit the exact quota equation $R_n(d) = r_\theta$, $A_1 = 3/5$, $A_2 = (11-4\sqrt{3})/5$, $A_3 = 0.8862545\dots$, the exact critical depth $n_c = 2$ crossing $\alpha_{\text{Nash}} = 43/60$, and the large-depth scaling $1 - A_n \sim \frac{p_*(1-p_*)}{c\,n}\log\frac{1-\theta}{\theta}$ (including $p_* = 1/2$ and $p_* < 1/2$).
     - Try to BREAK: (a) the uniform finite-$N$ welfare-gap lower bound eq. (3) for all $n \ge 2, \alpha \le 43/60$, (b) the all-depth log-convexity / unique downward-crossing proof (`q g'/g <= 6/5` and low-branch classification), (c) the depth-2 global trap + $\Theta(1/\log N)$ critical deficit + period-3 cycle at $\alpha = 7/10$, (d) the depth-3 matrix-positivity comparison proof, (e) the all-depth local-stability Jacobian proof, and (f) the deep-memory quorum loss bound $|W_{N,n}(\alpha) - 0.80| \le C_I r_I^n$ and the $n=2$ bistable rational example!
   - **Phase 2B-2 (`docs/phase2b_staghunt_robustness.md`, `experiments/phase2b_staghunt_robustness.py`)**:
     - Audit the monotone coupling proof ($1-P \le S \le R$), the open-rectangle certificates on BOTH sides of $S=1/2$ (`0.47 < S < 0.50`, `0.52 < S < 208/395`, `0.5499 < S < 1136/2065`), and the two-parameter universal scaling law $\delta_j U_{j,n_j}/K_* \to g_b(x) = e^{-x}\int_0^x e^{bt}\,dt$ (checking the uniform excursion estimate as $S_n \to 1/2$ from below!).
   - **Phase 2B-3 (`docs/phase2b_escape_showcase.md`, `experiments/phase2b_escape_showcase.py`, `experiments/phase2b_escape_geometry.py`, `experiments/phase2b_stationary.py`)**:
     - Audit the exact $\log 6 > 4h$ perfect-correlation bound, the exact dyadic Poisson-residual certification in `phase2b_stationary.py` (confirming it builds exact rational kernels directly from fractions with ZERO Decimal round-trip — no C2 regression!), the `(240,80)` and `(120,40)` stationary probabilities, and the reactive visitation / ever-hit identities $O_x = g_x q_x / h$, $B_x = g_x q_x / (h G_{xx})$ plus the `8,994.22x` $B/L$ speedup at `(60,20), kappa_P=0.99`.
   - **Phase 2B-4 (`docs/phase2b_fair_game_link.md`, `experiments/phase2b_fair_game_link.py`)**:
     - Audit the exact game-chain identities $d = a^2 G_{oc}/G_{oo}$, $b = a^2 G_{oc}$, $\Pr_o(\sigma<\zeta) = 1/G_{oo}$, the corner-revisit cancellation $d = h a^2 V$, the universal $B/L$ ratio table (`3.42580... -> 0.85645... -> 1`), the exact universal game-observable limits $d \sim \frac{\pi I(\gamma)}{16 N^2 \log N}$ and $b \sim \frac{I(\gamma)}{4 N^2}$, and the Brownian exit-time waiting-time formulas $K(\gamma), J(\gamma)$!
   - **Also check**: `docs/phase1_memory.md` (`(40,40) -> (41,40)` single-memory-state deviation, $n \ge 40$ theorem, and $N$-player public good $d_* = h(N-2)/(N-1)$) so we can safely cite them in Round R2!

---

## Required Output Format
1. **Executive Audit Verdict**: `CLEAN` (if 0 critical and 0 moderate mathematical/verification defects remain) or `REQUIRES FIXES` (with exact counts).
2. **Phase 2 Repair Verification Checklist**: Explicit PASS/FAIL status for `C1–C3`, `M1–M17`, and `Minor 1–4`.
3. **Phase 2B Itemized Audit (Extensions 1–4 + `phase1_memory.md`)**: Every single error, subtle gap, hypothesis omission, or numerical discrepancy found (with exact file:line references and exact repairs), OR explicit confirmation of every verified formula, proof step, and computational check.
4. **Final Round-R2 Judge-Pitch Clearance**: Exact list of theorems cleared with 100% rigor and any remaining explicit open boundaries that must be stated honestly.
