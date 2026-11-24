# Research Log — M. L. Tsetlin's Collective Automata & Zero-Communication Games (`02-tsetlin-collective-automata`)

## 2026-11-24 — Phase 0: Primary Source Excavation Completed
- Archived **13 authentic open-access primary PDFs** in `sources/papers/` (10 Soviet classics from Math-Net.Ru: Tsetlin 1961, Tsetlin 1963 UMN, Tsetlin–Krylov 1963 DAN, Krylov 1963 AT, Gelfand–Pyatetskii-Shapiro–Tsetlin 1963 DAN, Ginzburg–Krylov–Tsetlin 1964 AT, Volkonskii 1965 PPI, Ginzburg–Tsetlin 1965 PPI, Pittel 1965 PPI, Krinsky 1966 PPI; plus 3 modern Granmo Tsetlin Machine arXiv papers) and extracted full text layers into `sources/extracted/`.
- Cataloged exact citations, URLs, historical formulas, and four major theoretical chasms in `sources/PRIMARY_SOURCES.md`.
- Next: Phase 1 fast exact Markov probes (`experiments/phase1_scout_quick.py`) across all four discovery veins, followed by deep analytical & high-precision scouting with Codex Astra Max (`phase1_scouting`).

## 2026-11-24 · Phase 1 mathematical scouting

The equal-memory strict dilemma with $(R,P,T,S)=(.8,.7,.9,.2)$ has positive-correlation thresholds $13/63$ for L/B and $11/21$ for D. K selects DD even at external correlation one. The positive-correlation square correction is $-\tfrac12\log n$ in the log stationary odds. In the independent well the directional passage and mixing scales are $(7/3)^{2n}$ and $4^n$. The order of the classical architectures can reverse with weaker rewards. [Classical architectures](phase1_architectures.md) · [Weak rewards](phase1_weak_rewards.md)

The killed frozen rectangle exhibits a direct path, an initial stretch on an axis, and a terminal path constrained by a ceiling under strong negative correlation. Positive, tangent and negative-tilt regimes have different powers. The randomized boundary introduces a further transition. In the interacting game an unequal-memory pair can progress through repeated changes of the shorter player's action. The original equality example improves at $(11,10)$, an integer omitted from the initial grid. [Frozen rectangle](phase1_quadrant.md) · [Interacting rectangle](phase1_interface.md) · [Memory incentives](phase1_memory.md)

A constant-hare Stag Hunt rises from 36.04% cooperation to 82.30% and reaches 0.43% at depth 160. Its large-memory limit is zero. The independent fund calculations distinguish a Nash threshold from stationary selection. In a fixed depth-one quorum public good, the optimal pooling fraction tends to three fifths. The improved welfare in the historical placement example is smaller and comes from a replicated simulation. [Stag Hunt](phase1_reversal.md) · [Partial pooling](phase1_pooling.md)

All new calculations and proofs are indexed in the study report. The finite pair checks compare dense mpmath and subtraction-free elimination, the small-depth Stag Hunt uses exact integer determinants, and the frozen-corner residual checks enclose probabilities at 60 relative decimal digits. The original Phase 1 prompt is retained in the study's research logs. [Phase 1 report](phase1_scouting.md) · [Reproduction commands](../STUDY.md)

The optimal DD shock correlation for unequal memories is $(1+1/\gamma)/2$ in the strong-reward dilemma with $S\le1/2$. At memories $(120,40)$ the linear game gives $1.12438\times10^{-6}$, $.517847$ and $4.68957\times10^{-22}$ cooperation at correlations $0,\ 2/3,\ 1$ while all four payoffs and the CC feedback law stay fixed. The limiting cooperative window closes at $\gamma=h_R/h_P$. [Proof and phase diagram](phase1_optimal_correlation.md)

Fair independent feedback gives a square corner probability asymptotic to $\Gamma(1/4)^4/[128(4-\pi)n^2\log n]$ for L. Randomizing the boundary multiplies the coefficient by $5(4-\pi)/(4\log3-\pi)$. A separate 75-digit spectral solver checks both constants against small exact rational chains. [Green function and elliptic shape factor](phase1_fair_corner.md)


## 2026-11-24 — Phase 2: Adversarial Read-Only Astra Derivation Audit & 100% Repair Pass
- Ran hostile read-only audit (`codex_logs/phase2_verify_output.md`): **ALL FIVE headline theorem packages survived intact** (including 0 defects on the Constant-Hare Stag Hunt finite-memory mirage, both fair-corner elliptic constants $C_L, C_B$, the 2D quadrant $(0, -1/2, -3/2)$ trichotomy, the unique unequal-memory optimal correlation $\kappa_*(\gamma) = (1+1/\gamma)/2$, the $3/5$ quorum partial-fund optimizer with $\Theta(\sqrt{\log N/N})$ regret, and the architecture hierarchy $F_L=F_B<F_D<F_K$ + weak-reward reversal).
- **Archaeological bonus uncovered by audit**: Volkonskii (1965, §6, pp. 46–47) printed Pyatetskii-Shapiro's example $(R,P,T,S)=(0.85, 0.65, 0.90, 0.60)$ where survey-D selects DD ($\pi_{40}(CC)=1.02\times 10^{-4}$) and claimed linear automata behave analogously — which is **false**: our hierarchy $F_L = 169/218 < 0.85 < 351/400 = F_D$ proves linear $L$ selects **CC** ($\pi_{40}(CC)=0.99999991$ at $n=40$)! Also recorded Volkonskii §7 p. 48 printed inequality inversion.
- Repaired **100%** of all 3 critical (C1–C3), 17 moderate (M1–M17), and 4 minor audit findings across `experiments/`, `docs/`, and `sources/PRIMARY_SOURCES.md`, and verified every counterexample (`176946/689125` exact rational bracket width `4.41e-76`, unequal-depth lumping guard, empty cooperative ratio returns `None`, nearly-fair/nearly-diagonal adaptive precision, Volkonskii 1965 split, Krylov `27/227` check).
- Next: Post Pitch Packet `Study #02 — Round R1` to `@judge-layperson`, `@judge-theorist`, and `@judge-phenomena`.

## 2026-11-24 · Phase 2B results following Round R1

The one-quarter fund's limiting stationary welfare optimizer rises from $3/5$ at depth one to $(11-4\sqrt3)/5$ at depth two and $.886254503577869\ldots$ at depth three. The pivotal Nash share is $43/60$. At every depth at least two, shares at or below Nash have a positive welfare gap uniform in population size. The balance share at general depth satisfies $n(1-A_n)\to(123/500)\log3$. The benchmark excludes simultaneous low and productive fixed points. At $\alpha=.70$ the depth-two map has a locally attracting cycle that supplies the good every third round. At depth three the stationary probability of provision tends to zero throughout the below-Nash range. Global stationary selection at the balance share remains open at depths four and greater. [Quorum proofs and population calculations](phase2b_quorum_memory.md)

The off-fair Stag Hunt at $(S,R)=(.49,.9385)$ gives mutual stag with probabilities .3598863366, .8182121196 and .01035409544 at depths 1, 16 and 160. Both sides of the fair-solo boundary contain open regions with a finite-depth peak above 80% and a zero limit. A joint approach to $S=1/2$ and the critical mutual reward gives a family of peak profiles containing $xe^{-x}$. The data include 368 certified stationary solves. [Stag Hunt proof and grid](phase2b_staghunt_robustness.md)

The original $(.80,.60,.90,.20)$ dilemma with depths $(240,80)$ and independent $CC$ feedback exhibits .998529067253 stationary mutual cooperation for L at $\kappa_P=2/3$, between $9.0843\times10^{-11}$ at zero and $2.1501\times10^{-42}$ at perfect correlation. The six $(60,20)$ escape grids distinguish expected visits from the probability of ever hitting each site. At $\kappa_P=.99$ the randomized boundary B increases per-excursion success by a factor of 8,994.22447. [Stationary and reactive evidence](phase2b_escape_showcase.md)

With fair independent $DD$ feedback, the actual probability of switching directly into $CC$ before a positive return to deepest $DD$ is $a^2G_{oc}/G_{oo}$. Both rules have the same leading coefficient $\pi I(\gamma)/16$. Counting every return to the shallow corner explains the cancellation between B's higher corner-hit rate and its lower simultaneous-switch probability. Exact rational game rows and spectral runs up to $(12288,4096)$ verify the finite formulas. [Fair-game proof and checks](phase2b_fair_game_link.md)

Independent reruns reproduced all 368 Stag Hunt stationary values, all 120 unequal-memory profile masses and their enclosures, and the exact and spectral fair-game results. Recomputing the six bridge grids at 160 working digits reproduced all 75-digit cells obtained at 150 digits. The quorum experiment includes the branch brackets, stability certificates and 24 finite-population stationary solves. [Reproduction commands](../STUDY.md)


## 2026-11-24 — Unanimous 3-Judge Gate, Phase 3 Lean 4 Formalization, & Phase 4 Referee Sign-Off

### Unanimous 3-Judge Wow-Factor Panel (`Round R2`)
- Following Round R1 feedback, executed Phase 2B deepening and 5 consecutive read-only Astra verification rounds (`codex_logs/phase2_verify_output.md` through `phase2_verify_r5_output.md`), patching the final two minor Python context/docstring issues (`phase2b_staghunt_robustness.py`, `generate_pitch_figures.py`).
- Pitched **Round R2** to `@judge-layperson`, `@judge-theorist`, and `@judge-phenomena` and achieved **3/3 UNANIMOUS `PASS`** (board `#19` `@judge-phenomena`: `9.4/10`; `#20` `@judge-layperson`: `9.1/10`; `#21` `@judge-theorist`: `9.3/10`). Reported milestone to `@coordinator` at `#22`.

### Phase 3 — Standalone Lean 4.36.0 Formalization (`proofs/lean4/`)
- Built a zero-external-dependency standalone Lean 4.36.0 project (`lean-toolchain`: `leanprover/lean4:v4.36.0`, `lakefile.toml`) across 5 theorem modules + `Main.lean`:
  - `ArchitectureHierarchy.lean` (12 public theorems, 4 private lemmas, 70 audited constants)
  - `EscapeGeometry.lean` (25 public theorems, 11 private lemmas, 152 audited constants)
  - `FairGameCancellation.lean` (17 public theorems, 7 private lemmas, 128 audited constants)
  - `StagHuntMirage.lean` (23 public theorems, 12 private lemmas, 191 audited constants)
  - `CommonFundCutoff.lean` (40 public theorems, 26 private lemmas, 370 audited constants)
  - Total: **117 public theorems**, 60 private lemmas, **911 audited theorem constants** (out of 1,168 declarations).
- Lean formalization caught and fixed two genuine algebraic slips: (1) $A_2 = (11-4\sqrt{3})/5$ satisfies $25A_2^2 - 110A_2 + 73 = 0$ (not $5A_2^2 - 22A_2 + 19 = 0$); (2) lowering $u$ raises $\Phi_u(z)$, which tightens $z_D(s) \ge \Phi_u(z_C(s))$ and shrinks the feasible interval in the maximization $V_u$, thereby strictly lowering $V_B < V_L$.
- Verified from scratch (`lake clean && lake build && lake env lean Main.lean`): exit 0, 0 errors, 0 warnings, 0 `sorry`, only standard axioms `{propext, Classical.choice, Quot.sound}`.

### Phase 4 — 3 Non-Overlapping PDFs, 10 Dedicated Figures & 4-Round Read-Only Astra Referee Loop
- Authored `experiments/generate_paper_figures.py` (`python3 -W error::UserWarning` -> 0 warnings), generating 10 non-overlapping publication PNGs across `papers/paper1_correlated_automata/figs/` (3), `papers/paper2_memory_and_common_fund/figs/` (3), and `papers/expository_kr/figs/` (4).
- Authored and compiled 3 self-contained PDFs with `/opt/homebrew/bin/tectonic` (**0 TeX errors, 0 overfull/underfull/hyperref warnings**):
  1. `papers/paper1_correlated_automata/paper1_correlated_automata.pdf` (**15 pp.**, `amsart`)
  2. `papers/paper2_memory_and_common_fund/paper2_memory_and_common_fund.pdf` (**11 pp.**, `amsart`)
  3. `papers/expository_kr/expository_tsetlin_kr.pdf` (**7 pp.**, `xeCJK` with `\xeCJKsetup{CJKspace=true}` and `Nanum Myeongjo` + `Apple SD Gothic Neo`)
- Executed **4 iterative read-only Codex Astra Max referee rounds** (`codex_logs/phase4_referee_r1_output.md` -> `r2` -> `r3` -> `r4`), resolving **41/41 cumulative items** (including general trace/occupation/product-kernel proofs in Paper 1 Theorem 3.1, exact perfect-synchrony trace squeeze, weak-reward full-support interval, general Common Fund quota feasibility, $n=2$ three-step return map certification, Korean phase-flip typo fix, exact Stag Hunt two-sided compactness envelope, and all historical citations/precisions).
- **Final Verdict (`codex_logs/phase4_referee_r4_output.md`)**: **`ACCEPT AS IS — PUBLICATION SIGN-OFF GRANTED`** (**0 critical, 0 moderate, 0 minor**; all 33 compiled PDF pages, all 107 internal links, all 10 pixel-identical embedded figures, and all 911 Lean theorem constants verified).
