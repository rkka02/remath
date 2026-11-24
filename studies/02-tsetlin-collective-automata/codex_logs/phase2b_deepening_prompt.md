# Phase 2B Targeted Deepening — Answering All Three Round-R1 Judge Demands (`02-tsetlin-collective-automata`)

All three judges on the Wow-Factor Panel reviewed Round R1 (`judge-theorist`: 8.0/10, `judge-phenomena`: 7.8/10, `judge-layperson`: 6.8/10) and gave razor-sharp, completely constructive demands to reach **3/3 unanimous `PASS` (`>= 9.0/10`) in Round R2**.

We have already repaired 100% of the Phase 2 audit findings (`C1–C3`, `M1–M17`, `Minor 1–4`). Your mission in this **focused Phase 2B deepening run** is to rigorously derive, prove, and verify (at 70+ digit / exact rational precision) **FOUR targeted extensions** that directly close every phenomenological, intuitive, and theoretical critique from R1 — keeping all proofs crisp, airtight, and 100% honest about hypotheses!

---

## Targeted Extension 1 — General Memory Depth $n \ge 2$ in the Quorum Partial Common Fund (`docs/phase2b_quorum_memory.md` + `experiments/phase2b_quorum_memory.py`)

Both `judge-phenomena` and `judge-layperson` asked the exact same killer question about Theorem 5 (the 1/4-quorum threshold public good with $L=0.80, H=0.97, c=0.60, \theta=1/4$, or general $\theta \in (0, 1/2)$):
> *"Theorem 5 used depth-1 (`n=1`, Win-Stay-Lose-Shift) automata. What happens when agents actually have **memory depth $n \ge 2$** ($L_{2n,2}$ and $B_{2n,2}$)? Does the below-Nash Goldilocks window survive, collapse at a **sharp critical memory depth $n_c$** ('only shallow minds beat Nash via partial pooling; deeper memory destroys the Goldilocks tax'), or bifurcate into bistable hysteresis?"*

**Derive & prove cleanly**:
1. For general finite memory $n \ge 1$ (fixed $n$, growing population $N \to \infty$!) with independent synchronous $L_{2n,2}$ or $B_{2n,2}$ automata in the quorum public good $(L, H, c, \theta)$:
   - Compute the exact single-agent stationary cooperation fraction $F_n(p_C, p_D) = \frac{H_n(p_C)}{H_n(p_C) + H_n(p_D)}$ (where $H_n(p) = \frac{1}{1-p}\sum_{j=0}^{n-1}(p/(1-p))^j$ for $L$, and check exact formula for $B$ too — note $B$ differs by a factor of $2$ at the boundary, which cancels in $F_n$!).
   - Solve the productive-branch equilibrium condition $F_n(p_C^H(\theta,\alpha), p_D^H(\theta,\alpha)) = \theta$ for the exact critical sharing fraction $\alpha_{\text{opt}}(n)$ as a function of memory depth $n = 1, 2, 3, \dots$!
   - **Check BOTH stability AND global convergence / bistability!** Specifically:
     - For our benchmark $(L=0.80, H=0.97, c=0.60, \theta=1/4)$ where $\lim\alpha_{\text{Nash}} = 43/60 \approx 0.71667$: compute $\alpha_{\text{opt}}(n)$ for $n = 1, 2, 3, 4, 5, 6, \dots$! At what **exact critical memory depth $n_c$** does $\alpha_{\text{opt}}(n)$ cross $\alpha_{\text{Nash}} = 43/60$?!
     - Does $\alpha_{\text{opt}}(n)$ converge to $1$ as $n \to \infty$ (with exact exponential rate $1 - \alpha_{\text{opt}}(n) \sim C/n$ or $\Theta(1/n)$? Check: since $p_D^H - p_C^H = c(1-\alpha)$ and both are $> 1/2$ near $\alpha = 1$, $(p_D/q_D)^n / (p_C/q_C)^n \approx \exp(n \cdot \text{const} \cdot (1-\alpha)) = (1-\theta)/\theta \implies \mathbf{1 - \alpha_{\text{opt}}(n) = \Theta(1/n)}$!! CHECK THAT EXACT FORMULA!!)?
     - Check whether for $n \ge 2$ the mean-field $2n$-dimensional Markov dynamics has **unique global stability** or **bistable hysteresis** (two fixed points, low-branch vs. high-branch!) — and verify against **exact finite-$N$ Markov chains** (or exact mean-field ODE/discrete map + high-precision finite-$N$ exact / long-run calculations for $n=1, 2, 3$)!
   - Prove a clean, completely airtight theorem for arbitrary memory depth $n \ge 1$ characterizing the **exact critical memory depth $n_c$** beyond which blind automata can no longer beat the pivotal Nash threshold via partial pooling, AND showing the sharp exact $1 - \alpha_{\text{opt}}(n) \sim \frac{H(1-H)}{c}\frac{\ln((1-\theta)/\theta)}{n}$ (check exact constant!) scaling as $n \to \infty$! (Keep every stability / finite-$N$ claim 100% rigorous — clearly distinguish mean-field fixed-point / local-stability theorems vs. full finite-$N$ stationary-measure proofs!)

---

## Targeted Extension 2 — Stag-Hunt Finite-Memory Mirage Robustness Off $S = 1/2$ (`docs/phase2b_staghunt_robustness.md` + `experiments/phase2b_staghunt_robustness.py`)

Both `judge-layperson` and `judge-phenomena` noticed that our R1 example used $S = 1/2$ on the nose and $R = 15/16$ near $16/17$, and asked:
> *"Does a real, dramatic rise-and-crash mirage still occur across an **open region** away from $S = 1/2$? And what is the clean, exact mathematical role of $S = 1/2$ as the phase boundary?"*

**Derive & compute cleanly**:
1. Using the exact two-sided order theorem $U_n \asymp G_n (\rho_P^2/\rho_R)^n$ and exact 72-digit GTH solves across the 2D $(S, R)$ plane for fixed $P = T = 0.80$ (e.g., $S \in \{0.35, 0.40, 0.45, 0.48, 0.50, 0.52\}$ and $R$ subcritical below $R_c(P, S)$):
   - Note what happens for **ALL THREE regimes** of $S$:
     - **$S < 1/2$**: $G_n = \frac{1 - (S/(1-S))^n}{1 - S/(1-S)}$ rises from $1$ to $\frac{1-S}{1-2S}$! Prove an explicit theorem / bound showing how high the finite-memory peak $\max_n \pi_n(CC)$ rises across an **entire open strip** of $(S, R)$ with $S < 1/2$ while $\lim_{n\to\infty}\pi_n(CC) = 0$! (Give concrete, verified 72-digit witnesses like $S = 0.45, R = 0.94$ or $S = 0.48, R = 0.94$ where cooperation climbs from ~35% to **$> 75\%$–$80\%$** and crashes to **0%**!)
     - **$S = 1/2$ (exact critical watershed)**: $G_n = n$ grows unboundedly yet subexponentially, allowing $\max_n \pi_n(CC) \to 1$ while $\lim_{n\to\infty}\pi_n(CC) = 0$!
     - **$S > 1/2$**: $G_n \sim \frac{S}{2S-1}\left(\frac{S}{1-S}\right)^{n-1}$ becomes exponential, shifting the critical Stag threshold DOWN from $R_c = \frac{P^2}{P^2+(1-P)^2}$ to the cascade threshold $R_c^{\text{casc}}(P, S) = \frac{P^2(1-S)}{P^2(1-S)+(1-P)^2 S}$! Check whether a finite-memory mirage STILL happens just below $R_c^{\text{casc}}$ for $S > 1/2$ (e.g. $S = 0.55$) or whether it disappears because $G_n$ is purely exponential!
   - Also produce clean saved JSON data (`experiments/data/phase2b_staghunt_grid.json`) for plotting both the $x e^{-x}$ master collapse as $R \uparrow R_c$ and the off-$S=1/2$ robustness curves!

---

## Targeted Extension 3 — Overwhelming Unequal-Memory Showcase & 2D Escape-Geometry Data (`docs/phase2b_escape_showcase.md` + `experiments/phase2b_escape_showcase.py`)

Both `judge-layperson` and `judge-phenomena` praised Theorem 2 (`9.5/10`!) and asked for two concrete upgrades:
1. **Overwhelming cooperation at $\kappa_* = 2/3$**: At `(120, 40)`, $\pi_L(CC) = 51.78\%$ looked visually modest compared to `99.99%`! Compute exact (or rationally certified / 72-digit GTH) stationary cooperation probabilities for $(R,P,T,S) = (0.8, 0.6, 0.9, 0.2)$ at $\gamma = 3$ for larger memory pair(s) — e.g., **`(180, 60)`** and/or **`(240, 80)`** — OR even cleaner, choose a slightly larger gap $h_R - 3 h_P$ (e.g. $R = 0.85, P = 0.60, T = 0.90, S = 0.20$ where $h_R = \ln(17/3) = 1.7346 > 3 h_P = 3\ln(1.5) = 1.2164$, while at $\kappa = 0$ cost is $4 h_P = 1.6219 < h_R$ — wait: pick $R$ between $3h_P$ and $4h_P$! Check: $3h_P = 1.2164$, $4h_P = 1.6219$, so $e^{1.50}/(1+e^{1.50}) = 0.8176$: try **`R = 0.82, P = 0.60, T = 0.90, S = 0.20`** where $h_R = \ln(41/9) = 1.5163$, giving $+0.30/n_2$ slope at $\kappa_*=2/3$ and $-0.105/n_2$ slope at $\kappa=0$ so ALREADY at `(120, 40)` or `(150, 50)` cooperation exceeds **99%** at $\kappa=2/3$ while plunging below **$10^{-3}$** at $\kappa=0$ and **$10^{-20}$** at $\kappa=1$!!). Check BOTH `(0.8, 0.6, 0.9, 0.2)` at larger depth AND `(0.82, 0.60, 0.90, 0.20)` at `(120, 40)` (keeping $\kappa_R = 0$ explicitly labeled AND also recording $\kappa_R = \kappa_P$)!
2. **2D $(d_1, d_2)$ Memory-Plane Escape-Geometry Data**: To build `judge-phenomena`'s requested wall-worthy visual anatomy, compute and export clean JSON grids (`experiments/data/phase2b_escape_geometry.json`) for a concrete unequal-memory rectangle (e.g., `(60, 20)` or `(72, 24)` in $(0.8, 0.6, 0.9, 0.2)$) showing the exact conditional 2D **reactive/bridge occupancy density** (probability that a successful excursion from deepest $DD$ to first $CC$ visits state $(d_1, d_2)$, computed via exact forward Green function × backward committor $G(o, x) \cdot q(x)$!) at:
   - $\kappa_P = 0$ (axis-hugging / two-leg route),
   - $\kappa_P = 2/3$ (straight diagonal instanton hitting $(n_1, n_2)$ simultaneously!),
   - $\kappa_P = 0.99$ for **$L$** vs. **$B$** (showing visually how $\kappa \approx 1$ slams early into the short player's switching wall $d_2 = n_2$ and how $B$ surfs the switching interface to beat $L$!).
   This makes Theorem 2 + Theorem 3 **visually unforgettable**!

---

## Targeted Extension 4 — Direct Interacting-Game Observable for Theorem 3's Fair-Corner Elliptic Laws (`docs/phase2b_fair_game_link.md` + `experiments/phase2b_fair_game_link.py`)

Both `judge-layperson` and `judge-phenomena` flagged Theorem 3 as physically orphaned unless tied to an **observable dynamical quantity in the actual interacting game**!
- **Derive & prove cleanly**: In the actual interacting 2-player game (equal memory $n$ or unequal memory $m/n \to \gamma \ge 1$) with **fair mutual defection $P = 1/2$**, independent feedback, and $R > 1/2$, $S < 1/2 < T$:
  - How does the fair-corner elliptic per-excursion probability $h_{m,n}^{(L)} \sim \frac{\pi I(\gamma)}{4 D_0} \frac{1}{n^2 \log n}$ and $h_{m,n}^{(B)} \sim \frac{\pi I(\gamma)}{D_{1/4}} \frac{1}{n^2 \log n}$ enter an actual game observable?
  - Specifically, check the **direct simultaneous-switch excursion probability** (reaching $CC$ directly from deepest $DD$ without ever visiting a mixed profile $CD/DC$ or returning to deepest $DD$!), OR the **actual mean waiting time / stationary ratio** in the interacting game at $P = 1/2$!
  - Be **100% mathematically truthful**: in the interacting game at $P = 1/2$ with $S < 1/2 < T$, single-player exits into mixed states occur at rate $\Theta(1/n)$ (much larger than $1/(n^2 \log n)$), so do NOT falsely claim the unconditional total waiting time is $n^2 \log n$ if single-player mixed excursions dominate — instead identify the **EXACT** interacting-game observable governed by $C_L$ and $C_B$ (e.g., the probability of **direct zero-betrayal breakout** from deepest $DD$ straight to $CC$ without passing through a sucker-punched mixed round $CD/DC$, where $B$ beats $L$ by the exact **elliptic speedup factor** $\frac{C_B}{C_L} \cdot \text{(exact switch factor)}$ — check the exact factor carefully, noting $B$ also flips both switches with prob $1/4$ at the corner!! WAIT A SECOND: CHECK THAT FACTOR OF $1/4$!! In $h_{m,n}^{(B)}$, reaching corner $c = (m,n)$ gives $C_B / C_L = \frac{5(4-\pi)}{4\log 3 - \pi} \approx 3.4258$, AND then actually flipping BOTH actions at $c$ in the next step has probability $(1/2)^2 \cdot (1/2)^2 = 1/16$ for $B$ vs $(1/2)^2 = 1/4$ for $L$, OR after any number of holds at $c$! Compute the EXACT asymptotic ratio of direct zero-betrayal $DD \to CC$ breakout probability for $B$ vs. $L$ in the actual game!!).
  - Verify your exact formula to 60+ digits on the actual interacting game Markov chain!

---

## Deliverable Rules
- Write clean, modular, self-contained scripts in `experiments/phase2b_*.py` using exact rational / 70-digit arithmetic (zero float64 underflow!).
- Save clean JSON data in `experiments/data/phase2b_*.json` so we can immediately build our 3 wall-worthy prototype pitch figures.
- Write concise, airtight proof notes in `docs/phase2b_*.md` (every hypothesis explicit, zero handwaving, every open boundary honestly stated!).
- Finish with a crisp summary of all 4 extensions and exact verified numbers.
