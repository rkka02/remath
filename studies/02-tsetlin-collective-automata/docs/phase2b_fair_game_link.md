# A fair DD visit can end in joint cooperation

Start two independent linear (L) or randomized-boundary (B) automata at their deepest mutual-defection state. At the first action change, they either switch together into CC or one player spends a round cooperating alone. The two architectures have the **same leading probability of switching together**, although the limiting ratio of probabilities of at least one joint shallow visit per excursion is $3.4258007428\ldots$ (B over L).

## Exact law in the interacting game

Let $M,N$ be the numbers of memory states **per action**, with $M\ge N$. In DD the erosion coordinates run from $o=(0,0)$ to $c=(M-1,N-1)$. The deficit barriers called $m,n$ in the fair-corner theorem are therefore $M-1,N-1$. Each round at DD gives each player an independent fair reward or penalty, independently across rounds. At a shallow state the one-round probability of holding on a declined penalty is $w$, and the probability of switching is $a=1/2-w$. Thus $(w,a)=(0,1/2)$ for L and $(1/4,1/4)$ for B, whose boundary coins are independent. We can take $R>1/2$, $S<1/2<T$. Only $P=1/2$ enters transitions before the first exit.

Write $\sigma$ for the first exit from DD and $\zeta$ for the first positive return to $o$. Holding at $o$ for one round counts as a return. One excursion ends at $\sigma\wedge\zeta$. Write $d$ for the probability of reaching CC during that excursion and $b$ for the probability that the first exit from DD is to CC, allowing any number of returns to $o$. Both events require every earlier profile to be DD. When $M,N\ge2$, a round holds at $o$ with probability $1/4$. Conditioning the excursion on an actual departure in its first round therefore multiplies $d$ by $4/3$.

Restrict the **actual game transition matrix** to DD to obtain the substochastic matrix $K$, and write $G=(I-K)^{-1}$, including time zero. For every depth pair,

$$
\boxed{\quad d=a^2\frac{G_{oc}}{G_{oo}},\qquad b=a^2G_{oc},\qquad
  \Pr_o(\sigma<\zeta)=\frac1{G_{oo}}.\quad} \tag{1}
$$

Indeed, only $c$ permits a direct transition to CC, with one-round probability $a^2$. Summing this outgoing probability over visits to $c$ before $\sigma$ gives $b$. Successive excursions renew at $o$. The expected number of excursion starts before exit is $G_{oo}$, and each start has probability $d$ of a direct exit and probability $\Pr_o(\sigma<\zeta)$ of any exit. This proves all three identities. Equivalently, if $\tau_M,\tau_N$ are the independent one-player switching times in a continuing fair environment, then the actual first DD exit time has law $\min(\tau_M,\tau_N)$, and $b=\Pr(\tau_M=\tau_N)$. The equality in distribution follows by coupling up to the first action change.

**The corner revisit factor.** Suppose $c\ne o$, and let $h$ be the probability of visiting $c$ within an excursion. The expected number $V$ of visits to $c$, starting at $c$ and stopping on first reaching $o$ or exiting DD, includes the initial visit. The two-point Green formulas give

$$
V=G_{cc}-G_{oc}^2/G_{oo},\qquad
h=\frac{G_{oc}}{G_{oo}V},\qquad d=h\,a^2 V. \tag{2}
$$

For the first formula, starting at $c$ the probability of reaching $o$ before exit is $G_{co}/G_{oo}$. Those paths subsequently contribute $G_{oc}$ visits on average. The killed matrix is symmetric, so $G_{co}=G_{oc}$. Decomposing corner occupation in an origin excursion at its first visit to $c$ gives the second formula. After arriving at $c$, the probability of revisiting it at positive time before stopping is $1-1/V$, by renewal. Thus $a^2 V$ includes every opportunity to switch together. Requiring a switch on the very next round instead gives $h a^2$. When $M,N\ge2$, allowing any number of consecutive holds at the first visit, and ending the attempt on departure from $c$, gives $h a^2/(1-w^2)$. Subsequent visits after a departure supply the remaining terms in (2).

## Two elliptic laws and the cancellation

Assume $M/N\to\gamma\in[1,\infty)$ finite and $N\to\infty$. The transfer and diagonal equivalents in the fair-corner theorem are

$$
 G_{oc}\sim\frac{I(\gamma)}{(1-2w)^2 N^2},\qquad
 G_{oo}\sim\frac4\pi\log N,\qquad G_{cc}\longrightarrow D_w,
$$

where $I(\gamma)=2\pi\sum_{k\ge0}(-1)^k(2k+1)/\cosh((2k+1)\pi\gamma/2)$, $D_0=16/\pi-4$ and $D_{1/4}=16(4\log(3)/\pi-1)/5$. Shifting both barriers by one preserves these equivalents. [Fair-corner theorem and elliptic shape factor](phase1_fair_corner.md)

Since $1-2w=2a$, (1) gives, for **both** L and B,

$$
\boxed{\quad d\sim\frac{\pi I(\gamma)}{16N^2\log N},\qquad
              b\sim\frac{I(\gamma)}{4N^2}.\quad} \tag{3}
$$

For a square the coefficients are $\Gamma(1/4)^4/(128\pi)\approx 0.4296991136262733$ and $\Gamma(1/4)^4/(32\pi^2)\approx 0.5471099038066192$ ($0.5471099038066191597\ldots$), respectively. The ratio depends on precisely which event is recorded.

| Observable in one excursion | Limiting B/L ratio |
|---|---:|
| Both players reach their shallow DD states | $4D_0/D_{1/4}=5(4-\pi)/(4\log3-\pi)=3.42580074281620\ldots$ |
| Both switch in the round immediately following their first joint shallow visit | $D_0/D_{1/4}=0.856450185704050\ldots$ |
| Both switch before a mixed round or a positive return to deepest DD | $1$ |

The factor $D_{1/4}/D_0$ from visits after first reaching the corner cancels the immediate-flip ratio. The first-exit observable $b$, which also allows returns to deepest DD, has the same limiting B/L ratio of one.

## A single exit and its waiting time

From (1), the **chance of exactly one player switching** before the first positive return to the joint origin is $(1-b)/G_{oo}\sim\pi/(4\log N)$. Across an entire DD residence that chance is $1-b=1-I(\gamma)/(4N^2)+o(N^{-2})$. A different clock counts excursions of *one coordinate* from its own deepest state, regardless of the other player. For a single depth-$N$ fair automaton, the switching probability per such excursion and its mean time to switch from the deepest state are exactly

$$
 \frac{1}{2(N-1)+1/a},\qquad \mathbb E\tau_N=N(N-1+1/a). \tag{4}
$$

For $N\ge2$, the chance of switching before returning to zero from deficit $j$ is $j/(N-1+1/(2a))$, by the linear harmonic recurrence and the shallow boundary equation. From zero the first step erodes with probability $1/2$. For the mean, solving the Poisson recurrence subtracts $j(j+1)$ from the starting mean at zero. The boundary equation gives mean $N/a$ at $j=N-1$. For $N=1$ the one-step switch probability is $a$ and the mean is $1/a$. This identifies the $1/N$ scale in (4).

There is also an explicit mean number of **actual game rounds** until the first DD exit. With $r_k=2k+1$, set

$$
 K(\gamma)=1-\frac{32}{\pi^3}\sum_{k\ge0}
       \frac{(-1)^k}{r_k^3\cosh(r_k\pi\gamma/2)},\qquad
 J(\gamma)=\frac4\pi\sum_{k\ge0}
       \frac{(-1)^k}{r_k\cosh(r_k\pi\gamma/2)}.
$$

Then $\mathbb E_o\sigma\sim K(\gamma)N^2$. The probabilities that the long player alone and the short player alone switch at $\sigma$ tend to $J(\gamma)$ and $1-J(\gamma)$. Per joint-origin excursion their probabilities are asymptotic to $\pi J(\gamma)/(4\log N)$ and $\pi(1-J(\gamma))/(4\log N)$. For a square $K(1)=0.5893708262521105\ldots$ and $J(1)=1/2$. At $\gamma=3$, the long player exits first with limiting probability $0.02287330150133\ldots$, and $K(3)=0.98145915680118\ldots$.

**Proof.** For L, the one-coordinate generating function from zero is $\mathbb E z^{\tau_N}=\cosh(\xi/2)/\cosh((N+1/2)\xi)$, where $\cosh\xi=1/z$. This follows from the reflected recurrence at zero and the value one at overflow $N$. At $z=e^{-s/N^2}$ it tends to $\operatorname{sech}(\sqrt{2s})$. B follows the same path until the first shallow visit, from which its mean remaining time is $N/a=4N$ by (4). The remaining hard time has mean $2N$, so both scaled laws have the same limit. The Laplace transform identifies that continuous limit $\tau$ as standard Brownian exit time from $(-1,1)$ started at zero, by solving $u''/2=su$ with endpoint values one. From any deficit the mean is bounded by the mean from zero in (4). Repeated applications of Markov's inequality in blocks of twice that mean give uniform exponential tails for $\tau_N/N^2$. Independence, continuity of the limit, and uniform integrability now give limits $\mathbb E\min(\gamma^2\tau_1,\tau_2)$ and $\Pr(\gamma^2\tau_1<\tau_2)$, with independent copies $\tau_1,\tau_2$.

For $t>0$, the Dirichlet heat equation on $(-1,1)$ gives $\Pr(\tau>t)=\sum_{k\ge0} b_k e^{-\lambda_k t}$, with $b_k=4(-1)^k/(\pi r_k)$ from the cosine expansion of 1, and $\lambda_k=\pi^2r_k^2/8$. Evaluating at the independent time $\gamma^2\tau_1$ gives $J$ by the Laplace transform, with an absolutely summable series of expected absolute terms. Integrating the same expansion against $\Pr(\gamma^2\tau_1>t)$ gives $K$, since $\sum b_k/\lambda_k=\mathbb E\tau=1$ and $\sum |b_k|/\lambda_k<\infty$. Renewal at $o$ supplies the per-excursion probabilities. The waiting time derived here ends at the first DD exit. Stationary profile masses and later passage times also use the payoffs following that exit.

## Verification on the game rows

The program generates the entire labeled rational game chain, extracts its DD rows and classifies each outgoing transition as CC, CD, or DC. Exact rational Dirichlet solves separately allow and forbid origin returns. They agree with an independent 105-decimal-digit spectral computation at memory pairs $(1,1),(3,1),(2,2),(4,3),(7,5),(12,9)$ for each architecture. The maximum relative discrepancy across all nonzero checked quantities is below $1.1\times10^{-104}$. A second set of $R,S,T$ gives exactly the same DD rows.

| Depths | Rule | Direct CC before first origin return $d$ | First DD exit is CC $b$ |
|---|---|---:|---:|
| $(2,2)$ | L | $1/16$ | $3/25$ |
| $(2,2)$ | B | $7/284$ | $7/117$ |
| $(4,3)$ | L | $4287/329408$ | $72879/2288497$ |
| $(4,3)$ | B | $1019271/124640168$ | $3057813/134906297$ |

At $(12,9)$ the exact game rows give $d_L=0.00111354737424516730868092594139545750936628596859163418700127531357620\ldots$ and $d_B=0.00092859204638327438819958148039658620575635129527718585847498782220424\ldots$.

| Depths | B/L, corner hit $h$ | B/L, immediate flip | B/L, direct within excursion $d$ | B/L, first DD exit $b$ |
|---|---:|---:|---:|---:|
| $(64,64)$ | 3.310738 | 0.827684 | 0.966414 | 0.969560 |
| $(4096,4096)$ | 3.424035 | 0.856009 | 0.999484 | 0.999512 |
| $(192,64)$ | 3.472845 | 0.868211 | 1.013733 | 1.016914 |
| $(12288,4096)$ | 3.426661 | 0.856665 | 1.000251 | 1.000278 |

The large rectangles use the short-coordinate spectrum and closed tridiagonal endpoint resolvents on the long coordinate. Recomputing both architectures at $(4096,4096)$ and $(12288,4096)$ with 135 working digits gave a maximum relative difference below $2.8\times10^{-99}$ across all observables. To reproduce the tables, run `python experiments/phase2b_fair_game_link.py` from the study directory with mpmath installed. [Verification program](../experiments/phase2b_fair_game_link.py) · [Exact fractions and 82-digit finite data](../experiments/data/phase2b_fair_game_link.json)
