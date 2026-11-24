# Phase 1 Deep Mathematical Scouting — Study #02 (`02-tsetlin-collective-automata`)

You are acting as our senior mathematical theorist & computational analyst for **Project ReMath Study #02**: excavating and pushing FAR beyond M. L. Tsetlin (1961, 1963), Gelfand–Pyatetskii-Shapiro–Tsetlin (1963), Ginzburg–Krylov–Tsetlin (1964), Volkonskii (1965), Pittel (1965), and Krinsky (1966) on **collective games of finite-memory learning automata**.

All 13 primary PDFs (and extracted text layers) are already archived in `sources/papers/` and `sources/extracted/`. Our preliminary exact Markov probes (`experiments/phase1_scout_quick.py` and `experiments/phase1_mpmath_check.py`) just uncovered **THREE extraordinary, completely original mathematical phenomena** that we want you to dissect, prove rigorously (or find the exact sharp truth where our first guesses had subtleties!), and push to the absolute highest level of originality, sharpness, and counterintuitive shock!

---

## Core Mission & High Taste Bar

We must earn unanimous approval from a skeptical pure mathematician (*Annals/PTRF* bar), a nonlinear-dynamics/complex-systems physicist (Michael Berry / Strogatz bar), and a tough non-specialist general reader. Therefore:
- Reject vague heuristics or routine restatements of Tsetlin/Volkonskii/Pittel.
- Hunt for **exact necessary-and-sufficient phase boundaries**, **exact algebraic / large-deviations / spectral formulas**, **sharp critical exponents & polynomial prefactors**, **surprising impossibilities/reversals**, and **clean structural theorems** (that will later also have a Lean 4 core formalization!).
- Verify every single analytic formula to high precision (`mpmath`, 50–80 digits) using standalone Python scripts you write inside `experiments/`.

---

## Four High-Upside Research Targets to Investigate Thoroughly

### Target 1 — Exact Large-Deviations & Phase-Transition Theory of Correlated-Outcome Blind Social Dilemmas ("Same Payoff Matrix, Opposite Civilization")
Consider two blind automata ($L_{2n,2}$ linear tactic, $B_{2n,2}$ randomized-boundary linear tactic, Krinsky $D_{2n,2}$, and Krylov $K_{2n,2}$) playing a symmetric $2\times 2$ game with marginal win probabilities:
- $(C,C) \mapsto (p_R, p_R)$, $(D,D) \mapsto (p_P, p_P)$, $(C,D) \mapsto (p_S, p_T)$, $(D,C) \mapsto (p_T, p_S)$,
specifically the **Prisoner's Dilemma** $1 > p_T > p_R > p_P > p_S > 0$ (where $(D,D)$ is the unique strict dominant-strategy Nash equilibrium!), and also **Stag Hunt** & **Chicken/Hawk-Dove**.

Crucially, recall Tsetlin (1963 UMN, §5, eqs. (17)–(20)): the payoff matrix $V_j(f) = 2p_j(f)-1$ does **NOT** uniquely determine the joint outcome distribution $P(f, s)$. Parameterize the joint win/loss outcome at symmetric profiles $(C,C)$ and $(D,D)$ by Pearson correlation $\kappa \in [\kappa_{\min}(p), 1]$ while keeping ALL marginal payoffs **100% IDENTICAL**:
$$p_{++} = p^2 + \kappa pq, \quad p_{--} = q^2 + \kappa pq, \quad p_{+-} = p_{-+} = pq(1-\kappa), \quad q = 1-p.$$

**Key Questions to Prove / Resolve Exactly**:
1. **Exact 2D Reflected-Quadrant Escape Rate for $L_{2n,2}$ / $B_{2n,2}$**:
   In our 60-digit probe (`experiments/phase1_mpmath_check.py`) at $p_R=0.8, p_P=0.7, p_T=0.9, p_S=0.2$, we observed that $\frac{1}{n}\ln\frac{\pi_n(C,C)}{\pi_n(D,D)}$ closely tracked
   $$A_{\text{diag}}(\kappa) = \ln\!\left(\frac{q_P^2 + \kappa p_P q_P}{p_P^2 + \kappa p_P q_P}\right) - \ln\!\left(\frac{q_R}{p_R}\right)$$
   with a puzzling logarithmic correction $B(\kappa)\ln n$ ($B \approx 0$ at $\kappa=0$, $B \approx -0.5$ to $-0.8$ for $\kappa > 0$) and a slight residual difference at $n \le 18$.
   - **IS $I_{\text{double}}(p, \kappa) = \ln\!\left(\frac{p^2 + \kappa pq}{q^2 + \kappa pq}\right)$ THE EXACT EXPONENTIAL LARGE-DEVIATIONS RATE** for simultaneous escape from $(n,n)$ to $(1,1)$ in the 2D correlated random walk on $\{1,\dots,n\}^2$ (staying strictly inside $\{1,\dots,n\}^2$ until hitting $(1,1)$), **OR** is there a **sharper / different true 2D rate function** (e.g., from a boundary-hugging instanton, or from the exact kernel / Fayolle–Malyshev / Cramér large deviations of the absorbed quadrant walk)?!
   - **CHECK CAREFULLY** for BOTH $\kappa > 0$ AND $\kappa < 0$ (anti-correlated shocks!) AND check whether correlation on $(C,C)$ affects the single-flip escape rate from $(C,C)$!
   - Compute the **EXACT** asymptotic formula (including the **EXACT** polynomial prefactor $n^\beta$ if possible, and verify to $n=40+$ using efficient sparse / block-tridiagonal / exact 2D solver or high-precision `mpmath`!).
2. **Exact Phase Boundary & Architecture Inversion ($L_{2n,2}$ vs. $D_{2n,2}$ vs. $K_{2n,2}$)**:
   - Derive the **exact necessary-and-sufficient cooperation phase boundary** in $(p_R, p_P, p_T, p_S, \kappa)$ for:
     - Tsetlin linear tactic $L_{2n,2}$ (and $B_{2n,2}$),
     - Krinsky automaton $D_{2n,2}$,
     - Krylov stochastic automaton $K_{2n,2}$!
   - Check our remarkable finding: even at $\kappa = 0$ (independent coin flips), **Tsetlin $L_{2n,2}$ cooperates in a STRICTLY LARGER region than Krinsky $D_{2n,2}$** (even though Krinsky's automaton is strictly superior in single-agent random media)! Does **Krylov $K_{2n,2}$** beat BOTH or lose to BOTH? Can you prove a **strict nesting theorem** of cooperation phases across the classical Soviet automaton families ($L, B, D, K$), AND check the exact critical correlation thresholds $\kappa_c^L < \kappa_c^D$?!
   - Wait: what happens when $p_S > 1/2$ (so the single-flip cascade $(D,D) \to (C,D) \to (C,C)$ competes with simultaneous double-flip $(D,D) \to (C,C)$)? Derive the **complete 2-mechanism phase diagram** (Double-Flip Tunneling vs. Single-Flip Cascade vs. Defection)!

### Target 2 — The "Cognitive Equality" Paradox & Asymmetric Memory ($n_1 = \gamma n_2$)
In `experiments/phase1_scout_deep.py` Probe 3 (`pR=0.80, pP=0.60, pT=0.90, pS=0.20, kappa=0`), fixing $n_2 = 10$ and increasing Player 1's memory $n_1$ from $4 \to 34$:
- Mutual cooperation peaked **sharply at exact equality $n_1 = n_2 = 10$** (`P(CC) = 72.1%, W1 = 0.7440`),
- Increasing Player 1's own memory past $n_2$ **IMMEDIATELY HURT PLAYER 1'S OWN PAYOFF**, and collapsed cooperation to `0.03%` (`W1 = 0.6018`) past $\gamma_c = \frac{\ln(p_R/q_R)}{\ln(p_P/q_P)} - 1 \approx 2.419$!
- **Key Questions to Prove / Discover**:
  1. Derive the **exact asymmetric-memory phase boundary $\gamma_c(\kappa; p_R, p_P, p_T, p_S)$** for arbitrary memory ratio $\gamma = n_1 / n_2 \geq 1$ AND arbitrary outcome correlation $\kappa \in (\kappa_{\min}, 1]$!
     - **CRITICAL CHECK**: When $\kappa > 0$ AND $\gamma > 1$, does the 2D correlated random walk from $(\gamma n, n)$ to $(1, 1)$ undergo a **WALL-HUGGING vs. STRAIGHT-LINE INSTANTON TRANSITION**?! Compute the exact 2D Cramér–Legendre rate function $E(\gamma, \kappa; p_P)$! If there is a sharp algebraic transition in $\gamma$ or $\kappa$ (a **two-regime / corner-hugging boundary** in the $(\gamma, \kappa)$ plane!!), that would be an **ASTONISHING** pure-math theorem!
  2. **The Memory-Choice Meta-Game**: Treat $(n_1, n_2)$ as strategies! Prove rigorously that in Prisoner's Dilemma (in the cooperation regime), **unilateral memory upgrades are strictly self-defeating beyond $n_1 \approx n_2$** (every $(n, n)$ for large $n$ is a meta-Nash equilibrium or locally optimal along $n_1$, whereas in **Chicken/Hawk-Dove** unilateral memory upgrades are strictly profitable — an exact **strategic duality between Cooperation-by-Equality vs. Domination-by-Stubbornness**!).
  3. **What about $N$ players with heterogeneous memories $(n_1, \dots, n_N)$** in an $N$-player Prisoner's Dilemma / Public Goods game?! Does adding ONE "genius" (high-memory) player to a cooperative society of $N-1$ equal-memory automata **crash the entire society**?!

### Target 3 — Partial Common Fund (`Частичная общая касса`, $\alpha \in [0, 1]$) & Finite-Memory / Large-$N$ Paradoxes
In Gelfand–Pyatetskii-Shapiro–Tsetlin (1963) and Ginzburg–Krylov–Tsetlin (1964), ONLY $\alpha=0$ vs. $\alpha=1$ was studied (and only by mainframe simulation!).
Under partial pooling $\alpha \in [0, 1]$, each agent receives effective win probability $p_i^{\text{eff}}(f) = (1-\alpha) p_i(f) + \alpha \bar{p}(f)$.
- **Key Questions to Investigate**:
  1. **Exact Double-Inversion Theorem ($\alpha_c^{\text{Tsetlin}}$ vs. $\alpha_{\text{Nash}}$)**:
     In $2$-player and $N$-player Prisoner's Dilemma / Public Goods games, compute the exact closed-form threshold $\alpha_c^{\text{Tsetlin}}$ vs. $\alpha_{\text{Nash}}$! Show precisely when $\alpha_c^{\text{Tsetlin}} = 0 < \alpha_{\text{Nash}}$ ("blind beats rational") vs. when $\alpha_c^{\text{Tsetlin}} > \alpha_{\text{Nash}}$ ("blind needs MORE socialism than rational Nash players!"), AND analyze what happens when you compare **Common Fund redistribution $\alpha$** vs. **Zero-Cost Shock Correlation $\kappa$**!
  2. **Does Partial Pooling $\alpha^* \in (0, 1)$ Provably Beat BOTH $\alpha=0$ AND $\alpha=1$ — with a DRAMATIC, Provable Large-$N$ / Finite-$n$ Phase Window?!**
     In our preliminary run (`N=12` GKT Placement Game), $\alpha^* \in (0.3, 0.7)$ beat both $\alpha=0$ and $\alpha=1$, because $\alpha=0$ suffers Price of Anarchy while $\alpha=1$ hits Pittel's $n = \Omega(N)$ signal-dilution collapse!
     Can we find a **clean, canonical, analytically tractable** $N$-player game (e.g., 2-site Placement / Pigou Congestion / Public Goods / Binary Symmetric Resource Sharing) where we can **PROVE** a sharp theorem showing a **three-phase diagram** or a **dramatic quantitative peak at $\alpha^* \in (0, 1)$**? Be completely honest if the gap in Placement Games is modest vs. huge!

### Target 4 — Hunt for an Additional "Jaw-Dropper" Finite-Memory Collapse Paradox (More Memory = Worse Society!)
Look for the **cleanest, most natural, most dramatic** case where **increasing EVERY player's memory $n$ simultaneously** (equal memory $n_1 = \dots = n_N = n$) causes collective welfare or cooperation to **FIRST RISE SHARPLY and THEN CRASH CATASTROPHICALLY** (e.g., climbing to $> 70\%$ at small optimal finite memory $n^*$ and plunging to $0\%$ as $n \to \infty$!) — WITHOUT rigging the game!
Check:
- Symmetric $2\times 2$ Stag Hunt / Prisoner's Dilemma / Chicken / Pyatetskii-Shapiro coordination games (note: in `experiments/phase1_scout_deep.py` Probe 2, check why `StagHunt-2` climbed `0.347 -> 0.837` before float64 underflow — wait: `StagHunt-2` had $\rho_{DD}^2 > \rho_{CC}$, so it actually went to 1! What if $\rho_{DD}^2 < \rho_{CC}$ slightly while $p_R \gg p_P$ or $p_S > 1/2$?! Test **exact** 50-digit curves of $P_n(C,C)$ vs. $n$!).
- Also check **Exact $n=1, 2$ closed-form rational formulas** and **exact mixing time / metastability scaling** (how long does it take to reach cooperation vs. how fast does correlation $\kappa$ accelerate mixing time exponentially?!).
  **WAIT A SECOND — CHECK MIXING TIME / CONVERGENCE SPEED TOO!!**
  At $\kappa = 0$, escaping `(D, D)` takes time $\tau_{\text{mix}} \sim (p_P/q_P)^{2n}$ (super-slow!), whereas correlation $\kappa > 0$ cuts the mixing exponent from $2\ln(p_P/q_P)$ down to $\ln\frac{p_P^2+\kappa p_P q_P}{q_P^2+\kappa p_P q_P}$ — an **EXPONENTIAL SPEEDUP** in spontaneous coordination!

---

## Deliverables Requested From You in This Phase 1 Run

1. Write clean, fast, reproducible high-precision Python scripts in `experiments/` (e.g., `experiments/phase1_astra_probes.py`) that use `mpmath` (50–80 digits) AND/OR fast exact sparse/block-tridiagonal / exact rational solvers so there is **ZERO float64 underflow**.
2. Run your scripts and report **exact numerical evidence** alongside **rigorous mathematical derivations** (clearly separating what is **PROVED** vs. what is **CONJECTURED / NEEDS FURTHER PROOF**!).
3. Specifically resolve:
   - What is the **TRUE EXACT** large-deviations exponent $E(\gamma, \kappa; p)$ of the 2D correlated absorbed/reflected quadrant walk for $L_{2n,2}$ and $B_{2n,2}$ (both equal memory $\gamma=1$ and unequal memory $\gamma > 1$, and both $\kappa > 0$ and $\kappa < 0$)?! Is there a **wall-hugging vs. straight-line instanton phase transition**?!
   - What is the **EXACT** polynomial prefactor $n^\beta$ at $\kappa=0$ vs. $\kappa > 0$?
   - What are the **EXACT** cooperation phase boundaries for $L_{2n,2}, B_{2n,2}, D_{2n,2}, K_{2n,2}$ (proving the exact architecture hierarchy!)?
   - What is the **SHARPEST, MOST DRAMATIC** finite-memory reversal / partial Common Fund / $N$-player theorem?
4. Recommend the **top 3–4 headline theorems** that will form the sharpest, most astonishing, 100%-provable + Lean-4-formalizable package to pitch to the 3-Judge Wow-Factor Panel!
