# Phase 2 Adversarial Read-Only Derivation Verification Audit — Study #02 (`02-tsetlin-collective-automata`)

You are acting as a **hostile, merciless, read-only pure-mathematics referee** (think *Annals of Mathematics* / *Probability Theory and Related Fields*) auditing EVERY proof, formula, constant, edge case, sign, exponent, hypothesis, and computational script produced in Phase 1 under `docs/phase1_*.md` and `experiments/phase1_*.py`.

**CRITICAL RULE**: You are in `read-only` mode. Do NOT assume ANY claim in `docs/phase1_*.md` is true until you independently re-derive and stress-test EVERY step, check for hidden gaps, unstated assumptions, boundary edge cases, sign/factor-of-2 errors, parity mistakes, and exact script-vs-theorem consistency!

---

## Specific Targets to Attack & Try to Break

Audit ALL FIVE headline theorem packages we intend to pitch to the 3-Judge Wow-Factor Panel:

### Audit Target 1 — Architecture Threshold Hierarchy & Critical Prefactor (`docs/phase1_architectures.md`, `docs/phase1_square_prefactor.md`, `docs/phase1_weak_rewards.md`, `docs/phase1_anticorrelated_reset.md`, `docs/phase1_social_game.md`)
1. Check every transition rule against the **archived primary Soviet sources** in `sources/extracted/` (Tsetlin 1961/1963 $L, B$, Krylov 1963 $K$, Krinsky 1964/1966 $D$). Does Krylov's private coin really transform $(p, \kappa)$ into $(p'=(1+p)/2, \kappa'=\kappa p/(1+p))$ for BOTH symmetric and mixed profiles? Check carefully!
2. Re-derive $F_L = F_B = \frac{p^2+\kappa pq}{p^2+q^2+2\kappa pq}$, $F_D = p + (1-\kappa)pq$, $F_K = \frac{2p}{1+p^2+\kappa pq}$ and the exact factorizations of $F_D - F_L$ and $F_K - F_D$. Check all signs and boundary cases ($\kappa = 0$, $\kappa = 1$, $p = 1/2$, $S \le 1/2$ vs $S > 1/2$).
3. Audit the **trace-chain reduction** and the **square-root prefactor proof** $\frac{\pi_n(CC)}{\pi_n(DD)} = \Theta(n^{-1/2} e^{n(H_R - J)})$ for $0 < \kappa_P < 1$ (and all $\kappa_P \in (0, 1]$ for $K$!), AND the $\Theta(e^{n(r-V)})$ coexistence proof at $\kappa_P = 0$. Try to break the confined local-CLT bridge, the backward-running-maxima bound (eq. (5)), and the $S \le 1/2$ two-core trace extension!
4. Audit the **weak-reward reversal** (`docs/phase1_weak_rewards.md`): at $(R,P,T,S) = (0.45, 0.20, 0.95, 0.10)$ with independent feedback, do $L,B$ really converge to $(0, 3/14, 3/14, 4/7)$ while $D,K$ converge to $(1, 0, 0, 0)$? Check every step of that proof!

### Audit Target 2 — Unique Optimal Imperfect Correlation $\kappa_*(\gamma) = \frac{1+1/\gamma}{2}$ & Interface Splitting (`docs/phase1_optimal_correlation.md`, `docs/phase1_interface.md`, `docs/phase1_negative_krylov.md`)
1. Try to BREAK the proof that for $0 < S \le 1/2 < P < R < T < 1$ and $\gamma = \lim n_1/n_2 > 1$, the unique correlation minimizing the exponential cost $V(\gamma, \kappa)$ of reaching $CC$ from deep $DD$ is $\kappa_*(\gamma) = \frac{1 + 1/\gamma}{2}$ with minimum cost $\gamma h_P$ and supremum sustainable ratio $\gamma_{\max} = h_R / h_P$!
2. Check EVERY detail of:
   - The strictness proof for all $\kappa \neq \kappa_*(\gamma)$ (especially $\kappa < 0$, $\kappa = 0$, $\kappa = 1/2$, $\kappa \in (1/2, \kappa_*)$, $\kappa \in (\kappa_*, 1)$, and $\kappa = 1$)!
   - The exact quadratic curvature coefficient $C_\gamma = \frac{2\gamma\delta}{(1 - 1/\gamma)(1 + \delta^2/\gamma)}$ and the square-root window formula $\kappa_\pm(\gamma)$! Re-compute $s'(0), s''(0), D_2$ from scratch!
   - The supermartingale / test function $f_n(y)$ in `docs/phase1_interface.md` (both for $L$ and for general weak-switch probability $u \in (0,1]$ including $B$ with $u=1/2$), the first-return transform $\mathcal R_u(s)$, and the strict separation $V_B < a_R < V_L$ at $(P,R,T,S,\kappa,\gamma) = (0.6, 0.78, 0.9, 0.2, 0.99, 2)$!
   - Check the $(120, 40)$ example at $\kappa \in \{0, 2/3, 1\}$ — are there any hidden caveats (e.g., $\kappa_R = 0$ vs $\kappa_R = \kappa_P$)?

### Audit Target 3 — 2D Correlated Quadrant Escape, $(0, -1/2, -3/2)$ Trichotomy & Fair-Corner Elliptic Constant (`docs/phase1_quadrant.md`, `docs/phase1_random_boundary.md`, `docs/phase1_fair_corner.md`)
1. Audit the 4-regime table $(E, \beta)$ in `docs/phase1_quadrant.md`: check the exact algebraic expressions for $\lambda, t_*, g, \lambda_0, \kappa_0$, the radical formula for $H(x,y)$, the Catalan leading constant at $\kappa = 0$, AND the conditional ballot identity (eq. (2)–(3)) giving $\beta = -3/2$ when $g < 0$!
2. Audit `docs/phase1_fair_corner.md` line-by-line!! Check:
   - $h_{m,n} = \frac{G_{oc}}{G_{oo} G_{cc} - G_{oc}^2}$ — is this identity exact?
   - $G_{oo} \sim (4/\pi)\log n$ — check the factor of $4/\pi$ (folding at $-1/2$ vs $0$)!
   - $D_0 = 16/\pi - 4$ and $D_{1/4} = (16/5)(4\log 3 / \pi - 1)$ — re-evaluate BOTH integrals from scratch!
   - $n^2 G_{oc} \to I(\gamma) / (1 - 2w)^2$ with $I(\gamma) = 2\pi \sum_{k=0}^\infty \frac{(-1)^k(2k+1)}{\cosh((2k+1)\pi\gamma/2)} = \frac{4kk'K(k)^2}{\pi}$ — check EVERY factor of $2$ and $\pi$!
   - Confirm $C_L = \frac{\Gamma(1/4)^4}{128(4-\pi)}$ and $C_B = \frac{5\Gamma(1/4)^4}{128(4\log 3 - \pi)}$!

### Audit Target 4 — Constant-Hare Stag Hunt Finite-Memory Mirage (`docs/phase1_reversal.md`)
1. Audit EVERY step of the proof of $U_n = \frac{\pi_n(CC)}{1 - \pi_n(CC)} \sim K(R,P,S) G_n (\rho_P^2 / \rho_R)^n$ for $1/2 \le S < P < R < 1$, with $K(R,P,S) = \frac{(2P-1)^2}{(1-S)(2R-1)}$!
2. Check the exact reference-chain flux identity $F = f^2(\frac{2G_n}{1-S} - 1)$, the backward-edge count $\nu_D(z) d_n \sim F(1-\rho_P)$ and $\nu_C(w) c_n \sim F_C(1-\rho_R)$, and the infinite-ladder transmission probabilities $h_C, h_D$! Does $U_n \sim F/F_C$ REALLY hold without a missing factor of $2$ or $(1-\rho_P)/(1-\rho_R)$?! **CHECK THIS WITH EXTREME CARE!!**
3. Check the uniform asymptotics $\delta n_* \to 1$ and $1 - \max_n \pi_n(CC) \sim \frac{e\delta}{K(R_c, P, 1/2)}$ as $R \uparrow R_c$! Check the exact rational certificates $\pi_1(CC) = 3328/9233$, $\pi_2(CC) = 58905001984/110489411359$, $\pi_{10}(CC) > 4/5$.

### Audit Target 5 — Partial Common Fund $\alpha_N^{\text{opt}} \to 3/5$ & Double Threshold Inversion (`docs/phase1_pooling.md`, `docs/phase1_fund_boundary.md`, `docs/phase1_memory.md`)
1. Audit the 1/4-quorum threshold public good (`docs/phase1_pooling.md`):
   - Check $F_e(x) = x + \nu[e(1-2x) + cx(2\alpha - 1 - 2\alpha x)]$, $A_{e_L} = 2/9$, $A_{e_H} = 3/5$, $\alpha_{\text{Nash}}(N) = \frac{43N}{60(N-1)}$, welfare limits $.68, .79, .67, .82$.
   - Try to BREAK the $\Theta(1/\log N)$ proof at $\alpha = 3/5$ and the $\Theta(\sqrt{\log N / N})$ proof for $\alpha_N^{\text{opt}} - A$ and $\min_\alpha \rho_N(\alpha)$! Check the Berry–Esseen / tilted-Bernoulli lower-tail step and the stopping-time stationarity step!
   - Also check the Volunteer's Dilemma $\alpha = 1/2$ Lyapunov functions $F(s), G(s)$ giving $\Theta((\log N)/\sqrt{N})$!
2. Audit `docs/phase1_fund_boundary.md` (the two examples with $\alpha_{\text{Nash}} = 1/3$ vs blind thresholds $0$ and $0.6260592764...$) and `docs/phase1_memory.md` (both the $(11,10)$ correction and the $N$-player anonymous public good boundary $d = h(N-2)/(N-1)$!).

### Audit Target 6 — Novelty & Priority Honesty Check
Check every theorem against Tsetlin (1961, 1963), Gelfand–Pyatetskii-Shapiro–Tsetlin (1963), Ginzburg–Krylov–Tsetlin (1964), Volkonskii (1965), Pittel (1965), Krinsky (1966), and modern Tsetlin Machine / random-walk literature (Kobayashi–Miyazawa, Pan–Borovkov, Dolgoarshinnykh–Lalley, Foxall). Flag ANY statement that could be challenged as overclaiming novelty or omitting a subtle hypothesis.

---

## Required Output Format

Organize your report strictly as:
1. **Executive Audit Verdict**: `CLEAN` vs. `REQUIRES FIXES` (count of CRITICAL math/logic errors, MODERATE hypothesis/proof gaps, MINOR typos/clarifications).
2. **Itemized Findings by Target (1–6)**: For every single error or gap found, cite exact file + line/formula, show the exact counterexample or failure point, and specify the exact mathematical repair needed.
3. **Confirmed Verified Claims**: Explicitly list every theorem/formula/constant that survived your hostile attack 100% intact.
4. **Pitch-Readiness Assessment**: Which exact theorems are bulletproof right now for the 3-Judge Wow-Factor Panel, and which (if any) must be repaired or scoped before pitching.
