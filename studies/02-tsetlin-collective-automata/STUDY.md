# Study #02 — Excavating M. L. Tsetlin's *Collective Automata* (*Коллективное поведение автоматов*)

- **Slug**: `02-tsetlin-collective-automata`
- **Status**: Completed · Unanimous 3-Judge PASS (Round R2: `9.4 / 9.1 / 9.3`) · Read-Only Referee Sign-Off (`ACCEPT AS IS`, 0 critical / 0 moderate / 0 minor after 4 rounds of `gpt-6.2-astra` max) · Lean 4.36.0 Verified (`117 public theorems`, `911 audited theorem constants`, `0 sorry`)
- **Research Portal Target**: `https://rkka02.github.io/studies/02-tsetlin-collective-automata/`

---

## Publications (3 Self-Contained, Non-Overlapping PDFs · 33 pp. Total)

1. **Paper 1 (English Academic Preprint, `amsart`, 15 pp.)** — [`papers/paper1_correlated_automata/paper1_correlated_automata.pdf`](papers/paper1_correlated_automata/paper1_correlated_automata.pdf) ([`.tex`](papers/paper1_correlated_automata/paper1_correlated_automata.tex))
   - *Shared Fate and Imperfect Synchrony in Tsetlin's Collective Automata: Architecture Hierarchies, Unequal-Memory Optimal Correlation, and Two-Dimensional Escape Geometry*
   - Dedicated figures (3): `papers/paper1_correlated_automata/figs/p1_fig{1_architecture_hierarchy,2_unequal_escape_instanton,3_fair_elliptic_cancellation}.png`
2. **Paper 2 (English Academic Preprint, `amsart`, 11 pp.)** — [`papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.pdf`](papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.pdf) ([`.tex`](papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.tex))
   - *Finite-Memory Mirages, Unilateral Memory Cliffs, and Partial Common Funds in Zero-Communication Automata Games*
   - Dedicated figures (3): `papers/paper2_memory_and_common_fund/figs/p2_fig{1_memory_cliffs,2_staghunt_mirages,3_common_fund_cutoff}.png`
3. **Expository Magazine Feature (Korean, `xeCJK`, 7 pp.)** — [`papers/expository_kr/expository_tsetlin_kr.pdf`](papers/expository_kr/expository_tsetlin_kr.pdf) ([`.tex`](papers/expository_kr/expository_tsetlin_kr.tex))
   - *눈먼 로봇들의 기적과 배신: 소련 체틀린(M. L. Tsetlin) 집단 오토마타에서 발굴한 5가지 기억의 역설*
   - Dedicated figures (4): `papers/expository_kr/figs/kr_fig{1_shared_fate_and_volkonskii,2_imperfect_sync_and_plus1_cliff,3_staghunt_and_fair_cancellation,4_goldilocks_tax_nc2}.png`

---

## Headline Discoveries (All Verified & Referee-Signed)

1. **Multi-Architecture Hierarchy, Critical $n^{-1/2}$ Selection, 61-Year Volkonskii (1965) Erratum & Weak-Reward Reversal** (Paper 1, Theorems 3.1 & 3.3):
   - Exact algebraic factorizations prove $F_L = F_B < F_D < F_K$ ($0 \le \kappa_P < 1$) and $F_L = F_B = F_D = P < F_K = \frac{2P}{1+P}$ at $\kappa_P = 1$ via Krylov's exact reduction $(p,\kappa)\mapsto(\frac{1+p}{2}, \frac{\kappa p}{1+p})$.
   - On criticality $R = F$, survey-$D$ and independent ($\kappa_P = 0$) $L, B, K$ exhibit $\Theta(1)$ coexistence, whereas positively correlated $L, B$ ($0 < \kappa_P < 1$) and Krylov $K$ ($0 < \kappa_P \le 1$) undergo diffusive $n^{-1/2}$ selection of $DD$.
   - Refutes Volkonskii (1965, p. 47) on Pyatetskii-Shapiro's $(0.85, 0.65, 0.90, 0.60)$ at $\kappa = 0$: $F_L = 169/218 < 0.85 < 351/400 = F_D$, so survey-$D$ selects $DD$ ($\pi_{40}^D(CC) = 1.02\times 10^{-4}$) while linear $L$ selects $CC$ ($\pi_{40}^L(CC) = 0.99999991$, slope $\log(833/507) > 0$).
   - Weak-reward ($R < 1/2$, full support) trichotomy across $T + S \lesseqgtr 1$ completely inverts the hierarchy ($D, K \to 100\%$ $CC$ while $L, B \to 0\%$ $CC$) whenever $T + S \ge 1$, $0 \le \kappa_P < 1$, and $R > F_K > F_D$.
2. **Payoff-Independent Optimal Imperfect Correlation $\kappa_*(\gamma) = \frac{1+1/\gamma}{2}$ & Doorway Hesitation Splitting** (Paper 1, Theorems 4.1 & 4.2):
   - For unequal memories $n_1/n_2 \to \gamma > 1$ ($S \le 1/2 < P$), the escape barrier attains its unique global minimum $\gamma h_P$ at $\kappa_*(\gamma) = \frac{1+1/\gamma}{2}$ with curvature $C_\gamma = \frac{2\gamma\delta}{(1-1/\gamma)(1+\delta^2/\gamma)}$ and supremum $\gamma_{\max} = h_R/h_P$.
   - Certified $DD$–$CC$–$DD$ flip at $(0.80,0.60,0.90,0.20)$, $(240,80)$ across $\kappa_P = 0 \to 2/3 \to 1$: $9.084\times 10^{-11} \to 99.8529\% \to 2.150\times 10^{-42}$ for $L$.
   - M\"obius return operator $\Phi_u(z) = (1-u) + \frac{u^2 z}{1-(1-u)z}$ splits $V_B < V_L$ at active high-correlation interfaces ($B \to 100\%$ $CC$ while $L \to 0\%$ $CC$ at $(0.78,0.60,0.90,0.20, \kappa_P=0.99, \gamma=2)$, and $8{,}994.22\times$ per-excursion escape amplification at $(60,20), R=0.80, \kappa_P=0.99$).
3. **2D Correlated Quadrant $(0,-1/2,-3/2)$ Trichotomy & Fair-$DD$ Three-Way Elliptic Cancellation** (Paper 1, Theorems 5.1 & 5.2):
   - Complete four-regime stopped-quadrant classification with explicit rate $H(x,y)$ and $(0,-1/2,-3/2)$ prefactor exponents.
   - At fair independent $DD$ ($P=1/2$, $M/N \to \gamma \ge 1$), exact finite Green identities $b = a^2 G_{oc}$, $d = b/G_{oo} = h a^2 V$ produce three-way $B/L$ limiting cancellation: corner hits $\to \frac{5(4-\pi)}{4\log 3-\pi} \approx 3.4258$, immediate switches $\to 0.8565$, yet direct zero-betrayal $DD \to CC$ breakouts $\to 1$ universally, governed by $I(\gamma) = \frac{4kk'K(k)^2}{\pi}$.
4. **Unilateral $+1$-Depth Apocalypse, Adjacent-Pair Instability & $N$-Player Public-Good Cliff** (Paper 2, Theorem 2.2):
   - Upgrading one player from 40 to 41 depths per action (80 to 82 states) in $(0.55,0.40,0.99,0.39)$, $\kappa_R=\kappa_P=1$ boosts their payoff from $0.550$ to $0.670$ while crashing mutual cooperation from $99.9837\%$ to $0.0018\%$ (rational enclosures width $4.0\times 10^{-70}$ and $1.76\times 10^{-66}$).
   - Sharp $N$-player ($N \ge 3$) action-group-shared public-good peer collapse at $d_* = h\frac{N-2}{N-1}$.
5. **Open-Region Stag-Hunt Finite-Memory Mirages on Both Sides of $S=1/2$** (Paper 2, Theorem 3.1):
   - Exact odds scaling $U_n \asymp G_n \lambda^n$ with constant $K = \frac{(2P-1)^2}{(1-S)(2R-1)}$ ($S \ge 1/2$) via ladder cancellation $(1-\rho_P)h_C = (1-\rho_R)(1-h_D)$, certified open regions strictly on *both* sides of $S=1/2$ (`<37.5%` at $n=1$, `>80%` at moderate $n$, `-> 0%` as $n\to\infty$), and universal two-parameter collapse $g_b(x) = e^{-x}\int_0^x e^{bt}\,dt$.
6. **Partial Common Funds Below Nash & Exact Critical Memory Cutoff $n_c = 2$** (Paper 2, Theorems 4.1 & 4.2):
   - General parametric depth-$1$ partial pooling optimum $A_1 = \frac{c\theta-(1-H)(1-2\theta)}{2c\theta(1-\theta)}$ attains the social optimum $H-c\theta$ strictly below $\alpha_{\mathrm{Nash}} = 1-(H-L)/c$ with sharp finite-$N$ scaling $\Theta(\sqrt{\log N/N})$ (on $(0.80,0.97,0.60,1/4)$: $A_1 = 3/5 < 43/60 = \alpha_{\mathrm{Nash}}$, welfare $0.82$ vs. private $0.68$ and full pooling $0.67$).
   - Increasing memory from $n=1$ to $n=2$ immediately shatters below-Nash provision ($n_c = 2$: $A_1 = 3/5 < 43/60 < A_2 = \frac{11-4\sqrt{3}}{5} \approx 0.8144 < A_3 \approx 0.8863$), with uniform-in-$N$ welfare gap for all $n \ge 2, \alpha \le 43/60$, certified locally attracting period-$3$ limit cycles at $(n=2, \alpha=0.70)$ (contraction $<18/25$ for $L$, $<17/20$ for $B$ on radius-$10^{-80}$ boxes), and $1-A_n \sim \frac{p_*(1-p_*)}{cn}\log\frac{1-\theta}{\theta}$.

---

## Archive Contents

- **Primary Sources (`sources/`)**: [`sources/PRIMARY_SOURCES.md`](sources/PRIMARY_SOURCES.md) + 13 open-access PDFs (10 Russian Math-Net.Ru classics from 1961–1966 + 3 modern Granmo Tsetlin Machine arXiv papers) in `sources/papers/` and extracted text layers in `sources/extracted/`.
- **Formal Proofs (`proofs/lean4/`)**: 5 standalone Lean 4.36.0 modules (`ArchitectureHierarchy` [12], `EscapeGeometry` [25], `FairGameCancellation` [17], `StagHuntMirage` [23], `CommonFundCutoff` [40]) + `Main.lean` axiom audit (**117 public theorems**, 60 private lemmas, **911 audited theorem constants** out of 1,168 declarations, **0 `sorry`**, standard axioms `propext`, `Classical.choice`, `Quot.sound` only).
- **Technical Proofs & Logs (`docs/`)**: [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md), [`docs/phase1_scouting.md`](docs/phase1_scouting.md), and 17 detailed proof notes (`docs/phase1_*.md`, `docs/phase2b_*.md`).
- **High-Precision Scripts & Data (`experiments/`)**: 72–434 digit working-precision Python + GMP C++ solvers, rational Poisson residual certificates, interval contraction boxes (`experiments/data/*.json`), and zero-warning figure generator (`experiments/generate_paper_figures.py`).
- **Codex Astra Max Logs (`codex_logs/`)**: Full reproducible prompts and outputs across Phase 1 scouting, Phase 2 verification rounds R1–R5 (`phase2_verify*_output.md`), Phase 3 Lean 4 formalization (`phase3_lean4_output.md`), and Phase 4 read-only referee rounds R1–R4 (`phase4_referee_r1..r4_output.md`, ending with `ACCEPT AS IS — PUBLICATION SIGN-OFF GRANTED`).

---

## Reproducibility & Verification Commands

Run from `studies/02-tsetlin-collective-automata/`:

```bash
# 1. Machine-verify all 117 public Lean 4 theorems (911 theorem constants) from scratch
(cd proofs/lean4 && /Users/mw/.elan/bin/lake clean && /Users/mw/.elan/bin/lake build && /Users/mw/.elan/bin/lake env lean Main.lean)

# 2. Regenerate all 10 dedicated publication figures (0 matplotlib warnings)
python3 -W error::UserWarning experiments/generate_paper_figures.py

# 3. Compile all 3 self-contained PDFs (0 TeX errors, 0 layout warnings)
(cd papers/paper1_correlated_automata && /opt/homebrew/bin/tectonic paper1_correlated_automata.tex)
(cd papers/paper2_memory_and_common_fund && /opt/homebrew/bin/tectonic paper2_memory_and_common_fund.tex)
(cd papers/expository_kr && /opt/homebrew/bin/tectonic expository_tsetlin_kr.tex)

# 4. Run core high-precision & rational-certificate probes
python3 experiments/phase1_astra_probes.py --verify-only --memory-boundaries
python3 experiments/phase1_memory.py --certify
python3 experiments/phase2b_quorum_memory.py
python3 experiments/phase2b_fair_game_link.py
python3 experiments/phase2b_staghunt_robustness.py --workers 2
python3 experiments/phase2b_escape_showcase.py --jobs 2
python3 experiments/phase2b_escape_showcase.py --geometry --jobs 2
```
