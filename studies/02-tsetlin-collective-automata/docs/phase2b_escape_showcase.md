# Unequal memories in the same dilemma

Two players use the same linear tactic L, or both use the randomized-boundary tactic B with independent internal coins. The first has three times the memory of the second. Holding the four payoffs fixed, changing the correlation of the players' rewards during mutual defection changes the stationary frequency of mutual cooperation. The stationary frequency and the paths of a single successful escape are different measurements of the same game.

## Which games switch their long-run outcome?

Let the payoffs in the order `(R,P,T,S)` be `(R,.60,.90,.20)` with $.60<R<.90$. Feedback is fresh each round, independent at a mixed profile, and has the indicated correlation at each homogeneous profile. Write $n_1=3n_2$, $h=\log(3/2)$ and $h_R=\log(R/(1-R))$. For either architecture and every $0\le\kappa_P\le1$ (and globally for $L$, while for $B$ across negative correlations we use the lower limiting cost $\underline V=\liminf -n_2^{-1}\log\Pr(\text{successful excursion})$), $n_2^{-1}\log[\pi(CC)/\pi(DD)]\to h_R-V$, where $V$ is the escape cost from deep $DD$ to deep $CC$. The mixed stationary mass tends to zero under these hypotheses. At $\kappa_P=0$ the cost is $4h$. At $\kappa_P=2/3$ it is $3h$. The unique minimum follows by tilting the long player's $DD$ increments by $h$. The tilted mean increments of the two deficits are $2P-1$ and $(2P-1)(2\kappa_P-1)$. At $2/3$ their ratio is exactly $3:1$, so the shortest admissible exponential cost for the long player alone brings both players to their switching thresholds on the same macroscopic time scale. The strictness proof and the high-correlation costs are given in the two earlier notes. [Unique minimum](phase1_optimal_correlation.md) · [Actual switching interface](phase1_interface.md)

Consequently every $27/35<R<81/97$ has opposite strict selection at zero and optimal correlation. These bounds are $\operatorname{logistic}(3h)$ and $\operatorname{logistic}(4h)$. At perfect $DD$ correlation the costs are $V_L\approx 2.5570821561$ for L and $V_B\approx 1.9719790213$ ($1.971979021289\ldots$) for B. An exact check gives $V\ge\log 6>4h$ for both. In the perfect-correlation interface bound take the long-coordinate tilt $s=\log 2$, which sets the short exponential weight to $3/4$. The mixed return weight is the smaller positive root $z$ of $(13/100)z^2-z+13/25=0$. The polynomial is positive at zero and equals $-4/45$ at $2/3$, so $z<2/3$. Both boundary return factors, $z$ for L and $1/(2-z)$ for B, lie below $3/4$. This feasible tilt gives $V\ge h+2\log 2=\log 6$. Thus the whole interval also selects defection at perfect correlation. [Interface bound and weak-boundary transform](phase1_interface.md)

The log-odds slopes at $\kappa_P=2/3$ and $0$ are respectively $+0.16989904,-0.23556607$ for $R=.80$, and $+0.29995217,-0.10551294$ for $R=.82$. These slopes multiply $n_2$. They determine the limiting signs, while finite probabilities require the complete chain.

## Finite stationary probabilities

With the original $R=.80$ and independent $CC$ rewards, L spends **99.85290673%** of rounds cooperating at depths $(240,80)$ and $\kappa_P=2/3$. With the same depths, payoffs and $CC$ rewards, the stationary probability falls below $10^{-10}$ at $\kappa_P=0$ and below $10^{-41}$ at $\kappa_P=1$. B exceeds 99.89% at the middle setting, and falls below $10^{-21}$ at perfect correlation. The original $(120,40)$ result at $2/3$ was 51.785% for L. [Original finite-depth calculation](phase1_optimal_correlation.md)

Entries below are probabilities. Each architecture has its own three-point comparison with $\kappa_R=0$ throughout.

| $R$ | Depths | Tactic | $\kappa_P=0$ | $\kappa_P=2/3$ | $\kappa_P=1$ |
|---|---|---|---:|---:|---:|
| .80 | (240,80) | L | $9.0843316\cdot10^{-11}$ | .998529067253 | $2.1501415\cdot10^{-42}$ |
| .80 | (240,80) | B | $9.7114445\cdot10^{-11}$ | .998943198152 | $3.4878007\cdot10^{-22}$ |
| .82 | (120,40) | L | .000197847350 | .994723315810 | $8.2213056\cdot10^{-20}$ |
| .82 | (120,40) | B | .000208829046 | .996256849172 | $9.0488375\cdot10^{-10}$ |
| .82 | (150,50) | L | .000068842767 | .999704385378 | $2.4836389\cdot10^{-24}$ |
| .82 | (150,50) | B | .000072667036 | .999788597919 | $9.5019078\cdot10^{-12}$ |

Matching $\kappa_R=\kappa_P$ also changes the finite stationary law. At $(240,80)$ with $R=.80$, the $2/3$ probabilities become .998777763597 for L and .998994151294 for B. At $(120,40)$ with $R=.82$ they become .995500572184 and .996409813064. The JSON includes both protocols at all three depths, all four action-profile masses, and their numerical enclosures. [76-digit stationary data](../experiments/data/phase2b_escape_showcase.json)

**Certification.** For each recurrent class, let $f$ indicate one action profile. For any vector $u$, the identity $\pi P=\pi$ puts $\pi f$ between the smallest and largest entries of $f+Pu-u$. Subtraction-free state reduction supplies a numerical solution of the corresponding Poisson equation. Rounding its coordinates to dyadic rationals and evaluating both extrema with integer arithmetic encloses the exact stationary probability. Every reported full-precision mass has identical 76-digit rounding at both endpoints. Small asymmetric chains are independently checked with integer determinants. [Reproduction script](../experiments/phase2b_escape_showcase.py) · [Certified solver](../experiments/phase2b_stationary.py)

## What the memory-plane grids measure

Let $d_i=0$ at player $i$'s deepest D state, $d_i=n_i-1$ at the last D state, and $d_i=n_i$ at the first C state. The deepest C state is $2n_i-1$. Start at $o=(0,0)$ and stop at

$$
\tau=\min\{t\ge1:X_t=o\ \text{or}\ X_t\in CC\}.
$$

Success $E$ means $X_\tau\in CC$. The walk may cross either switching interface and visit mixed profiles before it succeeds. Let $D$ contain the states outside $\{o\}\cup CC$, $Q=P_{D,D}$, $a=P_{o,D}$, $b=P_{D,CC}\mathbf1$ and $G=(I-Q)^{-1}$. At each correlation in the grids all four joint DD outcomes have positive probability. From every transient state a finite sequence of outcomes gives an exit to $o$ or $CC$, so the finite Green matrix exists. The finite identities are

$$
q=Gb,\qquad g=aG,\qquad h=\mathbb P_o(E)=P(o,CC)+a q.
$$

The expected number of visits to a transient site $x$ on a successful excursion and its probability of **ever** visiting that site are, respectively,

$$
 O_x=\frac{g_x q_x}{h},\qquad
 B_x=\frac{g_x q_x}{h G_{xx}}.
$$

For the first identity, sum the indicators of visits to $x$ and apply the Markov property to the future of each visit. For the second, stop at the first visit to $x$. The unconditional expected number of visits is its hitting probability times $G_{xx}$. Multiplying the hitting probability by $q_x/h$ conditions on success. Thus $B_x\le1$ even where $O_x>1$. The source is visited once on every successful path. Adding it gives $1+\sum_{x\in D}O_x=\mathbb E_o[\tau\mid E]$. The endpoint distribution on $CC$ is the entry flux into each terminal state, divided by $h$. An entire path ensemble, including switches back into $DD$, contributes to these grids. [Finite-chain reactive visitation probabilities](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.104.015301)

At independence a cost-minimizing construction first moves the long coordinate along the reflecting short-coordinate axis and then advances both coordinates toward the corner. At $2/3$ a cost-minimizing macroscopic trajectory is straight in the scaled rectangle. The finite bridge can switch one player first. At $.99$ the $DD$ tilt hits the short switching boundary early. Applying the interface formula gives $V_L\approx 2.4090308534$ ($2.409030853362\ldots$) and $V_B\approx 1.9184231732$ at aspect ratio three. B can decline a loss at a shallow state. Its smaller exponential cost predicts more successful escapes. The forward and backward calculations below measure how often the bridge actually uses this option at finite memory.

## Six ways out of a 60-by-20 memory rectangle

Each row uses $R=.80$ and independent $CC$ feedback. The first numeric column is the unconditional chance that the excursion succeeds. The remaining columns condition on success. The midpoint column is the mean short coordinate among all visits to $DD$ with $d_1=30$, weighted by occupation. The last column counts every transition of the short player from D to C, up to and including the terminal step.

| Tactic | $\kappa_P$ | Success per excursion | First switches simultaneous | Mean $d_2$ at the midpoint | Mean short D→C crossings |
|---|---:|---:|---:|---:|---:|
| L | 0 | $6.9435340\cdot10^{-16}$ | 46.927% | 2.434 | 1.426 |
| B | 0 | $3.5741321\cdot10^{-16}$ | 51.332% | 2.461 | 1.192 |
| L | $2/3$ | $1.3937409\cdot10^{-13}$ | 36.847% | 8.338 | 2.582 |
| B | $2/3$ | $1.0225009\cdot10^{-13}$ | 39.083% | 8.726 | 1.898 |
| L | $.99$ | $1.5767893\cdot10^{-22}$ | $3.26163\cdot10^{-6}$% | 15.616 | 35.702 |
| B | $.99$ | $1.4181997\cdot10^{-18}$ | 0.00143836% | 16.703 | 12.367 |

At $.99$ the short player is first to switch on over 99.998% of the successful paths of either tactic. Conditional on switching first, it does so when the long player has progressed an average of 22.375 sites for L and 24.003 for B, out of the required 60. B declines an average of 30.727 losses at its last short-D site over the successful excursion. B's success probability is **8,994.22447 times** L's. A single site illustrates what the two heatmaps show. At $(40,19)$, just inside the short switching boundary, 87.4764% of B bridges visit the site and their mean visit count over *all* B bridges is 1.81720. For L the corresponding values are 0.6254% and 0.02103.

The array axes are $d_1=0,\ldots,119$ and $d_2=0,\ldots,39$. Each grid includes the origin and the first $CC$ site. Terminal cells sum to one. All expected-visit cells together sum to $1+\mathbb E[\tau\mid E]$. For an occupation distribution of a uniformly sampled transition-time observation pooled across successful paths, divide each **preterminal** expected-visit cell by $\mathbb E[\tau\mid E]$. For the chance a successful path passes through a given site, use the ever-hit grid directly. [75-digit geometry grids](../experiments/data/phase2b_escape_geometry.json) · [Green solver and rational inverse checks](../experiments/phase2b_escape_geometry.py)
