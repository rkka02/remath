# Primary Sources Archive — M. L. Tsetlin's Collective Automata & Zero-Communication Games

All 13 primary PDFs archived in `sources/papers/` are authentic open-access copies retrieved from the All-Russian Mathematical Portal (**Math-Net.Ru**, Steklov Mathematical Institute RAS) and **arXiv.org**, with full extracted text layers in `sources/extracted/`.

## 1. Core Soviet Primary Sources (M. L. Tsetlin, I. M. Gelfand, I. I. Pyatetskii-Shapiro & School)

1. **M. L. Tsetlin (1961)** — *О поведении конечных автоматов в случайных средах* (*On the behavior of finite automata in random media*)
   - **Original**: *Avtomat. i Telemekh.* (Автомат. и телемех.), 22:10 (1961), 1345–1354.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/at12417`
   - **Local Archive**: `sources/papers/Tsetlin_1961_AT_22_AutomataRandomMedia_rus.pdf`
   - **Key Contribution**: Introduces the linear-tactic automaton $L_{2n,2}$ (memory depth $n$ per action; note Tsetlin's original $p_i$ denotes the *penalty* probability!), proves exact stationary distributions in stationary random media, establishes asymptotic optimality for distinct interior two-action win probabilities whenever $\max_i w_i \ge 1/2$ (including the fair boundary $w_{\max} = 1/2$ where action weights are $2n$ vs. $O(1)$; equal rewards are trivially optimal), and discovers non-monotonic optimal finite memory $n_0$ in exogenously Markov-switching (composite) random media.

2. **M. L. Tsetlin (1963)** — *Конечные автоматы и моделирование простейших форм поведения* (*Finite automata and models of simple forms of behaviour*)
   - **Original**: *Uspekhi Mat. Nauk* (УМН), 18:4(112) (1963), 3–28; English trans.: *Russian Math. Surveys* 18:4 (1963), 1–27.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/rm6373`
   - **Local Archive**: `sources/papers/Tsetlin_1963_UMN_18_FiniteAutomataBehavior_rus.pdf`
   - **Key Contribution**: Grand synthesis of Tsetlin's theory: $L_{kn,k}$, $B_{kn,k}$, $V_{kn,k}$ automata; the Tsetlin book-stack library (§2); exact closed-form $W(L_{2n,2}, K)$ in 2-state composite media with symmetric environmental switching and swapped payoff pairs $(a,-a), (-a,a)$ (§3, eq. (15)); formal definition of *automata games* $\Gamma$ via joint outcome distributions $P(f, s)$ vs. equivalent $N$-player payoff functions $V_j(f)$ (§5, eqs. (17)–(20) — explicitly noting that $V_j(f)$ does **not** uniquely determine $P(f,s)$!); ergodic zero-sum games of two $B_{Mn,M}$/$B_{Nn,N}$ automata with complementary realized outcomes (§6: in the memory limit $n \to \infty$, yielding the harmonic-mean value when the payoff matrix contains a nonnegative row or a nonpositive column, and signed value zero when neither exists).

3. **M. L. Tsetlin & V. Yu. Krylov (1963)** — *Примеры игр автоматов* (*Examples of automata games*)
   - **Original**: *Dokl. Akad. Nauk SSSR* (ДАН СССР), 149:2 (1963), 284–287.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/dan27706`
   - **Local Archive**: `sources/papers/Tsetlin_Krylov_1963_DAN_149_AutomataGames_rus.pdf`
   - **Key Contribution**: First formal examples of zero-communication automata games and ergodic Markov-chain formulation.

4. **V. Yu. Krylov (1963)** — *Об одном автомате, асимптотически оптимальном в случайной среде* (*On one automaton that is asymptotically optimal in a random medium*)
   - **Original**: *Avtomat. i Telemekh.* (Автомат. и телемех.), 24:9 (1963), 1226–1228.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/at12262`
   - **Local Archive**: `sources/papers/Krylov_1963_AT_24_StochasticAutomaton_rus.pdf`
   - **Key Contribution**: Introduces the stochastic Krylov automaton $K_{2n,2}$ (on penalty, moves inward/outward with probability $1/2$ each), lifting the $w_{\max} \ge 1/2$ (minimum penalty $\le 1/2$) restriction of linear $L_{2n,2}$ for distinct interior rewards so asymptotic optimality holds in **all** stationary random media!

5. **I. M. Gelfand, I. I. Pyatetskii-Shapiro, & M. L. Tsetlin (1963)** — *О некоторых классах игр и игр автоматов* (*On certain classes of games and automata games*)
   - **Original**: *Dokl. Akad. Nauk SSSR* (ДАН СССР), 152:4 (1963), 845–848.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/dan28648`
   - **Local Archive**: `sources/papers/Gelfand_PS_Tsetlin_1963_DAN_152_ClassesGames_rus.pdf`
   - **Key Contribution**: Introduces local-neighborhood graph games (circle, lattice), Nash games, pure-solidarity $K$-games, the **full Common Fund** averaging construction $M_k(f) = \frac{1}{N}\sum_{i=1}^N m_i(f)$ (eq. (2)), and homogeneous (automorphism-transitive) games with Moore-optimal vs. Nash plays.

6. **S. L. Ginzburg, V. Yu. Krylov, & M. L. Tsetlin (1964)** — *Об одном примере игры многих одинаковых автоматов* (*On an example of a game of many identical automata*)
   - **Original**: *Avtomat. i Telemekh.* (Автомат. и телемех.), 25:5 (1964), 668–672.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/at11654`
   - **Local Archive**: `sources/papers/Ginzburg_Krylov_Tsetlin_1964_AT_25_CommonFund_rus.pdf`
   - **Key Contribution**: Introduces the symmetric *Placement Game* (*игра в размещения*, resource sharing with capacities $a_1 \geq \dots \geq a_k$) and simulates $\alpha=0$ (no Common Fund) vs. $\alpha=1$ (full *Общая касса*). Table 1 reveals (purely numerically, without theory!) a finite-memory crossover: Common Fund *hurts* at small sampled depths ($n \leq 5$) and *helps* at the larger sampled depths $n \in \{7, 10, 12\}$.

7. **V. A. Volkonskii (1965)** — *Асимптотические свойства поведения простейших автоматов в игре* (*Asymptotic properties of the behavior of the simplest automata in a game*)
   - **Original**: *Probl. Peredachi Inf.* (Пробл. передачи информ.), 1:2 (1965), 36–53; English trans.: *Problems Inform. Transmission* 1:2 (1965), 26–39.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/ppi735`
   - **Local Archive**: `sources/papers/Volkonskii_1965_PPI_1_AsymptoticAutomataGame_rus.pdf`
   - **Key Contribution**: Proves exponential holding-time asymptotics in random media (explicitly attaching positive mean payoff $w_{ij} > 1/2$ on every action to linear $L$ in his model description) and proposes a reduced "trigger-chain" approximation on action profiles as $n \to \infty$, stating the full-chain constant-factor comparison without proof.
   - **Two Newly Uncovered 1965 Original-Source Errata**:
     1. In §6 (pp. 46–47), Pyatetskii-Shapiro's example (`q00=0.35, q10=0.40, q01=0.10, q11=0.15`, i.e., strict Prisoner's Dilemma $(R,P,T,S)=(0.85, 0.65, 0.90, 0.60)$) gives survey-D weight bases $(0.060, 0.0525, 0.049)$ selecting DD ($\pi_{40}(CC)\approx 1.02\times 10^{-4}$), and Volkonskii prints *"Аналогичный результат верен и для линейных автоматов"* — **which is false**: linear $L$ gives weights $(2/17, 21/221, 98/507)$ with positive log-odds slope $\log(833/507)>0$, selecting **CC** ($\pi_{40}(CC)\approx 0.99999991$)! Volkonskii's own 1965 example lies inside our architecture gap $(F_L, F_D) = (169/218, 351/400)$!
     2. In §7 (p. 48), for the step-function Gur game with $p_- > 1/2$, Volkonskii's printed inequalities for $R\to 0$ vs. $R\to\infty$ around $a_c = \log_2(\rho_-/\rho_+)/(1-H(r))$ are inverted relative to his own ratio formula (and at $\nu = a_c n + O(1)$ the $\nu^{-1/2}$ factor sends $R \to 0$).

8. **S. L. Ginzburg & M. L. Tsetlin (1965)** — *О некоторых примерах моделирования коллективного поведения автоматов* (*On some examples of modeling collective behavior of automata*)
   - **Original**: *Probl. Peredachi Inf.* (Пробл. передачи информ.), 1:2 (1965), 54–62; English trans.: *Problems Inform. Transmission* 1:2 (1965), 40–46.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/ppi736`
   - **Local Archive**: `sources/papers/Ginzburg_Tsetlin_1965_PPI_1_CollectiveBehaviorSim_rus.pdf`
   - **Key Contribution**: Simulates fault-tolerant "shirt-collar-to-hem" reliability of Placement Games with Common Fund and two-level decentralized task-allocation automata.

9. **B. G. Pittel (1965)** — *Об асимптотических свойствах одного варианта игры Гура* (*Asymptotic properties of a variant of the Gur game*)
   - **Original**: *Probl. Peredachi Inf.* (Пробл. передачи информ.), 1:3 (1965), 99–112; English trans.: *Problems Inform. Transmission* 1:3 (1965), 76–88.
   - **Math-Net.Ru**: `https://www.mathnet.ru/rus/ppi752`
   - **Local Archive**: `sources/papers/Pittel_1965_PPI_1_GurGameAsymptotics_rus.pdf`
   - **Key Contribution**: Solves the **simultaneously rewarded** Gur/Goore game (where all $N$ automata receive the exact same reward/penalty at each step) by proving depth synchronization ($\max_{j,k}|\alpha_j - \alpha_k| \geq 1$ are transient!), yielding exact stationary weights $\pi_k \propto \binom{N}{k}q_k^{-1}\sum_{j=0}^{n-1}(p_k/q_k)^j$ for the randomized-boundary $B_{2n,2}$ rule (in this study's convention where $p_k$ is the win probability and $q_k = 1 - p_k$), and $\pi_k \propto \binom{N}{k} q_k^{-n}$ for Pittel's $D'_{2n,2}$ rule, together with the exact critical linear scaling threshold $\lim n/N > \chi$. Leaves the original independent-outcome game unproved.

10. **V. I. Krinsky (1966)** — *Об играх с нулевой суммой двух асимптотически оптимальных последовательностей автоматов* (*Zero-sum games of two asymptotically optimal sequences of automata*)
    - **Original**: *Probl. Peredachi Inf.* (Пробл. передачи информ.), 2:2 (1966), 43–53.
    - **Math-Net.Ru**: `https://www.mathnet.ru/rus/ppi1933`
    - **Local Archive**: `sources/papers/Krinsky_1966_PPI_2_ZeroSumAutomata_rus.pdf`
    - **Key Contribution**: Studies zero-sum games of two Krinsky $D_{Mn,M}$/$D_{Nn,N}$ or linear-tactic automata as $n \to \infty$, bounding the limiting payoff between the game's upper and lower values (saddle-point bounds).

## 2. Modern Contrast Sources (Granmo's Tsetlin Machines)

11. **O.-C. Granmo (2018)** — *The Tsetlin Machine — A Game Theoretic Bandit Driven Approach to Optimal Pattern Recognition with Propositional Logic*
    - **arXiv**: `arXiv:1804.01508`
    - **Local Archive**: `sources/papers/Granmo_2018_TsetlinMachine_1804.01508.pdf`
    - **Contrast**: Repurposes teams of $L_{2n,2}$ Tsetlin automata to learn propositional logic clauses (supervised classification) and explicitly discusses/analyzes the Goore game as a game-theoretic framework, while leaving correlated-feedback social dilemmas, unequal-memory optimization, endogenous Stag-Hunt finite-memory mirages, and partial Common Fund transitions untouched.

12. **L. Jiao, X. Zhang, & O.-C. Granmo (2021)** — *On the Convergence of Tsetlin Machines for the AND and the OR Operators*
    - **arXiv**: `arXiv:2109.09488`
    - **Local Archive**: `sources/papers/Jiao_Zhang_Granmo_2021_TM_AND_OR_2109.09488.pdf`

13. **M.-B. Belaid, J. Sharma, L. Jiao, O.-C. Granmo, P.-A. Andersen, & A. Yazidi (2023)** — *Generalized Convergence Analysis of Tsetlin Machines: A Probabilistic Approach to Concept Learning*
    - **arXiv**: `arXiv:2310.02005`
    - **Local Archive**: `sources/papers/TM_GeneralizedConvergence_2310.02005.pdf`
    - **Note**: Focuses on probabilistic concept learning rather than correlated-feedback social dilemmas, unequal-memory optimization, or partial Common Fund phase transitions.

---

## 3. Specific Historical Boundaries & Related Antecedents

1. **Correlated-Outcome Social Dilemmas & Architecture Separation**: Tsetlin (1963 §5) distinguished joint outcome laws $P(f,s)$ from marginal payoffs $V(f)$, and Volkonskii (1965 §6) stated independent all-positive-drift $L/D$ weights up to constants (without full-chain comparison proof and misstating $L$'s selection on his own example). Our Theorems 1–2 prove exact correlated-outcome phase boundaries across $L, B$, survey-$D$ (Tsetlin 1963 §2; distinct from Krinsky's 1964 *Doklady* full-depth redraw), and $K$, critical $n^{-1/2}$ tie-breaking vs. coexistence, weak-reward reversal, and the unique unequal-memory optimal correlation $\kappa_*(\gamma) = (1+1/\gamma)/2$ (contrasting with the Brownian equal-capital plateau of Dębicki–Ji–Rolski, `arXiv:1906.09347`).
2. **2D Correlated Quadrant Escape & Fair-Corner Elliptic Laws**: While Kobayashi–Miyazawa (`arXiv:1201.3167`), Pan–Borovkov (`arXiv:1708.09605`), and Ignatiouk-Robert (`arXiv:2311.06652`) study reflected-walk stationary tails, free-walk orthant entry, and killed Green functions, and Evans–Pugh (`arXiv:1404.1877`) evaluate the squared-Catalan generating function yielding $D_0 = 16/\pi - 4$, our Theorem 3 resolves the exact moving-barrier stopped quadrant event for correlated $(L, B)$ excursions with parity-preserving interior increments, including the soft-wall boundary splitting and the exact hard/soft fair-rectangle elliptic constants $C_L, C_B$ with Jacobi shape factor $I(\gamma) = 4kk'K(k)^2/\pi$.
3. **Endogenous Finite-Memory Reversal**: Tsetlin (1961, 1963 §3) found optimal finite memory in an *exogenously* Markov-switching single-agent medium. Our Theorem 4 proves an *endogenous* finite-memory mirage in a completely stationary independent constant-hare Stag Hunt, where $\max_n \pi_n(CC) \to 1$ as $R \uparrow R_c$ while $\lim_{n\to\infty}\pi_n(CC) = 0$.
4. **Partial Common Fund (`Частичная общая касса`)**: Gelfand–Pyatetskii-Shapiro–Tsetlin (1963) and Ginzburg–Krylov–Tsetlin (1964) studied only $\alpha \in \{0, 1\}$ (with a finite-memory simulation table for placement, and later Gurvich 1975 `at7793` disproved general placement/common-fund assertions; Tung–Kleinrock 1996 studied independent depth-1 automata; Apt–Schäfer `arXiv:1105.2432` and Palfrey–Rosenthal 1984 cover static threshold/altruism Nash benchmarks; Dolgoarshinnykh–Lalley / Lalley / Foxall cover $\sqrt{N}$ critical logistic/SIS extinction). Our Theorem 5 proves that in the independent depth-1 quorum public good, every optimal partial fund share satisfies $\alpha_N^{\text{opt}} \to 3/5 < \alpha_{\text{Nash}} = 43/60$ with exact welfare convergence to the social optimum $0.82$ (vs. $0.68$ private and $0.67$ full) and a sharp gap between $\Theta(\sqrt{\log N/N})$ optimal regret and $\Theta(1/\log N)$ fixed-$3/5$ regret, alongside the regenerative Volunteer's Dilemma welfare loss $\Theta((\log N)/\sqrt{N})$ at $\alpha = 1/2$ and 2-player threshold double inversion.

## Phase 1 source corrections and subsequent work

- Volkonskii §6, pp. 46–47, gives the independent all-positive-drift stationary-weight orders for symmetric games of two linear or Krinsky automata. He states that the action-level comparison holds up to constants and omits its proof. This part of the independent phase diagram has a historical antecedent. [Volkonskii (1965)](https://www.mathnet.ru/eng/ppi735)
- Pittel's binary game uses a common win/penalty outcome, and the linear memory-to-population comparison concerns a specified feedback curve. Full redistribution in the placement code still uses independent outcome draws. The two models have different transition laws. [Pittel (1965)](https://www.mathnet.ru/eng/ppi752)
- Krinskii §7 already uses unequal memory volumes in zero-sum examples. The phase-1 asymmetric-memory arguments concern a social dilemma and specified common or independent feedback. The publisher lists the English translation at pp. 33–41. [Krinskii (1966)](https://www.mathnet.ru/eng/ppi1933)
- E. T. Gurvich later developed auxiliary-chain methods for automata games and explicitly considered placement and common-fund claims. This later source is bibliographic context outside the original 13-PDF archive. A publication-level originality assessment should compare its hypotheses and conclusions. [Gurvich (1975)](https://www.mathnet.ru/eng/at7793)
