# A loss-run criterion for Krinsky automata in a Prisoner's Dilemma

Let $1>T>R>P>S>0$ be the four reward probabilities. Outcomes are freshly sampled in each round, with independent outcomes at a mixed action profile. At a symmetric profile with reward probability $p$, write $q=1-p$ and

$$
 A_p=p^2+\kappa_p pq,\qquad B_p=q^2+\kappa_p pq,\qquad
 C_p=(1-\kappa_p)pq .
$$

These are the probabilities of two rewards, two penalties and each directed disagreement, respectively. Each player has the same depth $n$. All logarithms are natural. The results below concern the stationary law of the coupled game. A frozen profile appears as an auxiliary process in the proofs.

## Historical updates

Depth runs from 1 (shallow) to $n$ (deep). The original scans distinguish three different kinds of randomization.

| Tactic | Reward | Penalty |
|---|---|---|
| Tsetlin $L$ | Deepen one step, capped at $n$ | Lose one depth, flipping to the other shallow state at depth 1 |
| Tsetlin $B$ | As in $L$ | As in $L$ above depth 1. At depth 1, independently choose either action with equal probability and stay shallow |
| Krinsky $D$ | Jump to depth $n$ of the current action | As in $L$, including the deterministic shallow flip |
| Krylov $K$ | As in $L$ | Toss a private fair coin. One face applies the $L$ reward move, the other applies the $L$ penalty move |

Tsetlin's survey gives the $L,D,K$ definitions in §2, pp. 11–13, and $B$ in §6. Krylov's original graph and the two central balance equations on p. 1227 show transitions between the two shallow states. The paper numbers those states $n$ and $2n$. [Tsetlin, 1963](https://www.mathnet.ru/rus/rm6373), [Krylov, 1963](https://www.mathnet.ru/rus/at12262)

In a pair of $K$ automata, independently thinning each external penalty by a factor of two produces the **entire $L$ game** with transformed probabilities

$$
 q_i'=q_i/2,\qquad p_i'=(1+p_i)/2,\qquad
 \operatorname{Cov}'=\operatorname{Cov}/4,\qquad
 \kappa_p'=\kappa_p p/(1+p).
$$

The primes describe the actual direction of the confidence update. Every confidence drift is positive even when $S<1/2$.

## Stationary exponents and strict thresholds

Write $H_i=H(i)$ for $i=R,P,T,S$. In the following ranges, the stationary probabilities satisfy

$$
 \lim_{n\to\infty}\frac1n\log\frac{\pi_n(CC)}{\pi_n(DD)}
 = H_R-\min\{J,\ H_P+H_T-H_S\}.
 \tag{1}
$$

| Architecture and range | $H(p)$ | $J$ |
|---|---|---|
| Krinsky $D$, all feasible signs of $\kappa_P$, $A_R,A_P>0$ | $-\log(1-p)$ | $-\log B_P$, with $J=+\infty$ at $B_P=0$ |
| Krylov $K$, $0\le\kappa_P\le1$, arbitrary feasible $\kappa_R$ | $\log((1+p)/(1-p))$ | $\log(((1+P)^2+\kappa_P P(1-P))/B_P)$ |
| $L,B$, $S>1/2$, $0\le\kappa_P\le1$, arbitrary feasible $\kappa_R$ | $\log(p/(1-p))$ | $\log(A_P/B_P)$ |

The total mixed mass tends to zero exponentially in every row. At a strict inequality the sign of (1) selects $CC$ or $DD$. The second term in the minimum is the cost to leave $DD$ for a mixed profile and then escape to $CC$ before returning to $DD$. For strict PD payoffs the ordering alone implies $H_T-H_S>H_R-H_P$. Thus this mechanism can change the negative slope but cannot generate a cooperating phase. At $\kappa_P=1$ a synchronized $D$ or $L$ pair can go directly from $DD$ to $CC$, which gives (1) at this endpoint.

The three strict cooperation criteria $R>F(P,\kappa_P)$ have explicit thresholds. With $p=P, q=1-p, h=1-\kappa_P$,

$$
 F_L=F_B=\frac{p^2+\kappa_Ppq}{p^2+q^2+2\kappa_Ppq},
 \qquad F_D=p+h p q,\qquad
 F_K=\frac{2p}{1+p^2+\kappa_P p q}.
 \tag{2}
$$

Their differences factor as follows.

$$
 F_D-F_L=\frac{2hpq^2(1-hp)}{1-2hpq},\qquad
 F_K-F_D=\frac{pq(1-hp)(1-hq)}{1+p-hpq}.
$$

In their common proved range $S>1/2$, the ordering is strict for $0\le\kappa_P<1$. At $\kappa_P=1$ the first two thresholds equal $P$ and the Krylov threshold is $2P/(1+P)$. For example with $P=0.7, R=0.8, S=0.6, T=0.9$, the $L,B$ threshold in correlation is $13/63$, and the $D$ threshold is $11/21$. Krylov automata select $DD$ even at complete external synchronization. The comparison of $D$ and $K$ remains valid when $S=0.2$.

For $D$, critical equality $R=F_D$ yields coexistence in the sense that both $\pi_n(CC)$ and $\pi_n(DD)$ stay bounded away from zero. Thus the strict criterion $R>F_D$ is necessary and sufficient for $\pi_n(CC)\to1$ under the stated nondegeneracy assumption. At positive effective correlation strictly below one, the nearest-neighbor odds at criticality have order $n^{-1/2}$ and $DD$ wins. This covers Krylov at every positive external correlation, including one. At independent $DD$ feedback the sharp bound below yields coexistence at critical equality for $L,B,K$. If $\kappa_P<0$, the $K$ and all-stable $L,B$ formula with cascade cost alone still follows whenever $H_P+H_T-H_S\le 2H_P$. The two-interval bound below recovers a portion of the negative-correlation diagram. The full equal-depth Krylov exponent follows by replacing $J$ in (1) by the constrained reflected-walk exponent proved separately. A two-round observation scheme also extends the Krinsky theorem through vanishing double-reward probabilities and gives bounded multiplicative factors throughout the phase diagram. [Negative-correlation Krylov theorem](phase1_negative_krylov.md), [Krinsky endpoints](phase1_anticorrelated_reset.md)

## Trace on the deepest states

Observe the finite chain at successive visits to the four states where both players are deepest. Consecutive observations may be one round apart. The stationary law of this trace is the original stationary law conditional on these states. Exchange symmetry lumps the two mixed states into $M$. Write $D_0,C_0$ for the $DD,CC$ trace states, respectively, and $Q_{ij}$ for the one-step trace probabilities. Eliminating $M$ in the three stationary equations gives

$$
 \frac{\nu(C_0)}{\nu(D_0)}
 =
 \frac{Q_{D_0C_0}+Q_{D_0M}Q_{MC_0}/(Q_{MC_0}+Q_{MD_0})}
      {Q_{C_0D_0}+Q_{C_0M}Q_{MD_0}/(Q_{MC_0}+Q_{MD_0})}.
 \tag{3}
$$

If $M$ is transient its outgoing probabilities still define the same identity. For $D$ let $g>0$ be the minimum joint-reward probability over all profiles. Any joint reward reaches the matching deepest state, so the waiting time to the trace has a uniform geometric tail. Stationarity also implies $g\pi_n(\alpha)\le\pi_n(\text{deep }\alpha)\le\pi_n(\alpha)$ for every profile.

For a nearest-neighbor architecture with all confidence drifts positive, each deepest state also has a uniformly positive fraction of its profile mass. In detail, use $W=n-\text{depth}$ as the distance from the deepest state, with reflection at both endpoints when actions are ignored. Each conditional erosion probability is at most $v<1/2$. A coordinate can be coupled below a scalar reflected walk driven by i.i.d. erosion indicators of probability $v$. Starting from any state, after $Cn$ steps the dominating walk has $W\le m$ with probability at least $1-\varepsilon$, for large enough fixed $C,m$. Indeed the initial distance is cleared by negative drift except with probability exponentially small in $n$, and the remaining reflected maximum has tail bounded by $(v/(1-v))^m$. A union bound applies to the two coordinates. A fixed number of subsequent joint deepening steps has probability bounded away from zero, since at each profile the sum of the erosion probabilities is strictly less than one. Hence failure to hit any trace state by time $k(Cn+m)$ has a geometric upper bound in $k$. To preserve a particular starting profile, first force $m$ joint deepening steps. The ruin bound makes the probability of either player changing action before the first return to depth $n$ as small as desired. The probability of a later crossing in $Cn$ rounds, starting from depth $n$, is $O(n(v/(1-v))^{n-1})$. Choose the two bad-event probabilities below $1/4$ and force the terminal deepening steps on the remaining good event. Starting anywhere in the specified profile, this places the pair at its matching deepest state at the fixed time $Cn+2m$, with probability bounded below independently of $n$. Stationarity at that deterministic time gives the asserted constant comparison.

Consequently one can truncate a $D$ excursion at $n^2$, or a nearest-neighbor excursion at $n^3$, with a superexponentially small error on the scale $n$. Write $u_n\doteq e^{-nh}$ for $-n^{-1}\log u_n\to h$. At either symmetric starting corner, the probability of any first flip in a polynomial horizon is at most $e^{-nH_i+o(n)}$. For $D$ this follows by taking a union over length-$n$ loss windows. For a nearest-neighbor walk, take a union over increments of the reflected walk from its last visit to depth $n$. The exponential martingale at $H_i$, or ordinary gambler's ruin, gives the bound.

The total exit probability from $C_0$ has exponent $H_R$. For $D$, force $n$ losses of one player from the start and a joint reward immediately after the first flip. Before the flip the profile is fixed, and the partner can flip on the same round. For a nearest-neighbor walk, make one coordinate's first excursion from depth $n$ reach the switch. Its probability has exponent $H_R$. An earlier switch by the other player also reaches a different profile. Starting from the first flip, the uniform probability of stabilizing the resulting profile supplies the lower bound. The first coordinate can be held away from the deepest state until that flip by choosing the successful scalar excursion in the frozen law. For $B$, the private boundary choice costs a constant. Equivalently, use a first-arrival at the shallow boundary, force an erosion on an eligible coordinate, and accept either new profile. The analogous argument gives $Q_{MD_0}\doteq e^{-nH_S}$ and $Q_{MC_0}\ge e^{-nH_T+o(n)}$. For the mixed lower bounds, independently tilt or prescribe only the chosen coordinate. Its partner, with positive confidence drift, stays on its action for $O(n)$ rounds with probability tending to one. The mixed total exit probability is at most $e^{-nH_S+o(n)}$.

For $\kappa_P<1$ the homogeneous corner has $Q_{D_0M}\doteq e^{-nH_P}$. For $D$, during $n$ consecutive penalties of one specific player, the conditional probability that the other loses every round is $(B_P/(1-P))^n\to0$. For a nearest-neighbor rule, tilt only the erosion increments of the first player by $e^{H_P X_1}$. Its mean erosion speed is positive, and the second player's speed is strictly smaller. The difference is $2C(e^{H_P}-e^{-H_P})>0$, where $C$ is the probability of each disagreement of the **effective** increments. Thus one coordinate reaches the switching boundary before the other with probability bounded away from zero under the tilt. Taking a successful first excursion, followed by stabilization, gives the stated exponent. At $\kappa_P=1$, privately randomized Krylov increments still disagree with positive probability. For a synchronized $D,L$ pair, $J=H_P<H_P+H_T-H_S$, so the direct route alone furnishes the required lower bound. A $B$ pair can additionally use independent shallow choices.

By the mixed balance equation,

$$
 \nu(M)(Q_{MC_0}+Q_{MD_0})
 =\nu(C_0)Q_{C_0M}+\nu(D_0)Q_{D_0M}.
$$

The mixed-to-$DD$ exponent $H_S$ is strictly smaller than either symmetric exit exponent. This proves exponential decay of the mixed probability for the trace and hence for the original chain. The denominator in (3) has exponent $H_R$, since the fraction $Q_{MD_0}/(Q_{MC_0}+Q_{MD_0})$ has exponent zero.

## Krinsky's two compulsory loss runs

Set $b=B_P$ and $q_i=1-i$. To reach $CC$ from $D_0$, mark, for each player, the last time they earned a reward while playing $D$ before the first $CC$. The initial state supplies a mark at time zero if necessary. Immediately after each mark the player is deepest in $D$ and must incur $n$ consecutive penalties before their next cooperation.

Fix the two mark times. Order the ensuing length-$n$ windows and let $k$ be their overlap. During the first window's unshared steps the designated defector loses with probability at most $q_P$. During the overlap both players defect and both must lose, with probability $b$. During the second window's unshared steps, either the first player cooperates and the still-defecting player loses with probability $q_T$, or the first player defects and its last marked $D$-reward prevents it from winning. The latter requires a double penalty with probability $b$. By successive conditioning the probability of the witness is at most

$$
 q_P^{n-k} b^k\max(q_T,b)^{n-k}
 \le \max(b,q_Pq_T)^n.
 \tag{4}
$$

For disjoint windows the unrestricted gap contributes a factor at most one. A polynomial union over mark times yields $Q_{D_0C_0}\le\max(b,q_Pq_T)^{n+o(n)}$, with the exponent notation interpreted through logarithms. Conversely, $n$ joint penalties followed by a joint $CC$ reward give $Q_{D_0C_0}\ge A_R b^n$.

For a start at $M$, if the original cooperator earns a reward while defecting before the first $CC$, both players have marks and (4) applies. Otherwise the original defector still needs its own full window. Whenever its opponent defects within that window both must lose, since its opponent never earned a $D$-reward. In all cases $Q_{MC_0}\le\max(q_T,b)^{n+o(n)}$. These upper bounds include repeated shallow action flips and partial preparation before entering a mixed profile.

Substitution in (3) proves (1). In multiplicative terms the rate base in its numerator is exactly $\max(b,q_P q_T/q_S)$. The terms $q_Pq_T$ from (4) and $q_Pb/q_S$ from the mixed upper bound are bounded by this maximum. The two matching lower bounds come from the double loss run and the two single transitions through $M$.

At critical equality $b=q_R>q_T$, (4) gains a factor $q_P^j$ beyond $b^n$ when the two starting times differ by $j<n$. For $j\ge n$ the factor is $q_P^n$, and the idle gap of $j-n$ steps without a trace return has a geometric bound. The prefix to the first mark has the same geometric bound. Summing these bounds gives $Q_{D_0C_0}=\Theta(b^n)$. The one-mark case likewise has $Q_{MC_0}=O(b^n)$. For a single exit from a symmetric corner, or the faster mixed exit to $D_0$, sum over the start of the compulsory run with the geometric bound on the prefix. Hence $Q_{C_0D_0}+Q_{C_0M}=\Theta(q_R^n)$, $Q_{D_0M}=O(q_P^n)$ and $Q_{MD_0}=\Theta(q_S^n)$. Formula (3) and the uniform comparison with physical profile masses give the coexistence claim.

## Krylov's correlation after the private coin

Use the $L$ representation and let $X_i=+1$ mean erosion, $X_i=-1$ deepening in a frozen $DD$ profile. Denote the two-deepening and two-erosion probabilities by $a,b$. For $K$ these are $((1+P)^2+\kappa_P P(1-P))/4$ and $B_P/4$. For $L,B$ they equal $A_P,B_P$. Take $J=\log(a/b)$ and $\theta=J/2$. The joint moment generating function has $M(\theta,\theta)=1$. For nonnegative correlation, $\theta\le H_P$, giving $M(\theta,0)=M(0,\theta)\le1$.

Each of the two original defectors must flip to reach $CC$. Up to its first flip its erosion can be dominated by the coordinate of a single frozen i.i.d. $DD$ process. Before the first change this is the actual profile. Afterwards, sample the untouched defector by thinning that coordinate's erosion whenever its partner cooperates, using $q_T'\le q_P'$ (or $q_T\le q_P$ for $L,B$). Generate the other feedback conditionally to recover the correct game law. The frozen reflected walk for each coordinate must therefore have an increment sum at least $n-O(1)$ on some subinterval. The two intervals can have arbitrary endpoints. In their overlap the exponential moment is 1, and on the remainder it is at most 1. A polynomial union over the endpoints bounds $Q_{D_0C_0}\le e^{-nJ+o(n)}$.

For the matching lower bound, tilt the increment law by $e^{\theta(X_1+X_2)}$. This exchanges $a,b$, so the two coordinates have equal positive mean erosion. Force $O(n^{2/3})$ initial joint erosion steps. Concentration then lets both coordinates travel through the interior to distances $O(n^{2/3})$ from the switch before hitting either boundary. This costs $e^{-nJ+o(n)}$ under the original law, by the likelihood ratio on that event. Their difference has even parity. Prescribe $O(n^{2/3})$ disagreement steps to equalize the coordinates and joint erosions to cross together. When disagreement is impossible the depths already coincide. Stabilize the new profile. This constructs a direct trace transition with the claimed exponent.

Finally, on a direct trace excursion $M\to C_0$, either the incumbent defector flips first, at cost at least $H_T$, or the original cooperator flips first and both original coordinates must flip. In the second case build independent dominating scalar walks with erosions of types $S$ and $P$. Until the first flip both coordinates have independent mixed feedback. Afterwards only the original defector is constrained, and its erosion is bounded by its private $P$ comparison walk. A union over time intervals thus bounds the second probability by $e^{-n(H_S+H_P)+o(n)}$. Consequently $Q_{MC_0}\le e^{-n\min(H_T,H_S+H_P)+o(n)}$. In (3) any resulting additional route has cost at least $2H_P\ge J$, while the direct and ordinary cascade lower bounds attain the minimum in (1).

For negative correlation take the scalar tilt $H_P$ in each coordinate of the two-interval upper bound. Its individual moment is 1 and its joint moment is at most 1. This gives the interval of possible costs for the numerator of (3),

$$
 \min(2H_P,H_P+H_T-H_S)
 \ \le\ \liminf -n^{-1}\log(\text{numerator})
 \ \le\ \limsup -n^{-1}\log(\text{numerator})
 \ \le\ \min(J,H_P+H_T-H_S).
$$

The term $J$ here is the cost of the exhibited straight simultaneous path when $b>0$, with $J=+\infty$ when $b=0$. If the cascade costs at most $2H_P$ both ends agree.

## The square-root loss for Krylov's direct transition

Assume strict positive effective correlation below one, and use $H=H_P$, $\theta=J/2<H$. When $J<H_P+H_T-H_S$, the physical stationary odds satisfy

$$
 \frac{\pi_n(CC)}{\pi_n(DD)}
 =\Theta\!\left(n^{-1/2}e^{n(H_R-J)}\right).
$$

This holds for $K$ throughout its nonnegative-correlation theorem whenever its raw correlation is positive and the displayed cost inequality holds. For all-stable $L,B$ it holds when $0<\kappa_P<1$ and the same cost inequality holds. At $J=H_R$ strict PD payoffs ensure the required cost inequality. The two architectures therefore behave differently on their respective critical curves. Krinsky's loss streak keeps both phases visible, while Krylov's private coin gives $\pi_n(CC)=\Theta(n^{-1/2})$.

To see the upper bound, drive the two frozen $DD$ workloads $W$ by their correlated erosion increments, with reflection at zero and no upper cap. Let $z=(0,0)$ and let $\mu$ be their joint stationary law. A frozen cycle from $z$ to its next visit to $z$ has bounded mean independent of $n$. For example, the Lyapunov function $e^{uW_1}+e^{uW_2}$ for small $u>0$ contracts outside a fixed box, and the origin is accessible there by a fixed run of joint deepening. Before either physical defector first switches, its workload is bounded by its frozen coordinate. A return of the frozen pair to $z$ therefore reaches the physical trace as well.

For arbitrary positive integer levels $N,m$ the stationary workloads satisfy

$$
 \mu(W_1\ge N,W_2\ge m)
 \le C e^{-\theta(N+m)}(N^{-1/2}+m^{-1/2}).                       \tag{5}
$$

Run a stationary construction backward. Its two workloads are the separate running maxima of the same free negative-drift walk. Split the event according to which coordinate first reaches its level. At the first hit of $N$ by coordinate 1, tilt by $e^{\theta(X_1+X_2)}$ stepwise and put $L=Y-m$ for the current second coordinate $Y$. After dropping the ordering restriction, the contribution to the expected hitting probability is at most

$$
 e^{-\theta(N+m)}
 \mathbb E_*\left[e^{-\theta L}\mathbf{1}_{L\ge0}
 +e^{(H-\theta)L}\mathbf{1}_{L<0}\right].
$$

Indeed if $Y<m$, the remaining free crossing has probability $e^{-H(m-Y)}$. Under the tilt $Y$ is the sum of the second-coordinate displacements in $N$ independent first-coordinate upward ladder periods. These displacements have exponential tails and positive variance, since the tilted first coordinate has positive drift and disagreement steps have positive probability. The lattice local central limit bound places at most $C/\sqrt N$ at any one value of $L$, uniformly in $m$. The two geometric sums converge as $0<\theta<H$. Exchange the players to obtain the other term in (5). With $m=0$ the same upper bound holds after replacing $m^{-1/2}$ by 1, by the scalar tail.

At the first physical switch, suppose the other original defector still needs $k$ erosion levels to switch. A simultaneous switch contributes $k=O(1)$. Before that defector next reaches deepest, the probability it also switches is at most $Ce^{-Hk}$ by the scalar ruin bound, since it faces reward probability at least the $DD$ value. If it first reaches deepest, a subsequent switch before the trace has probability at most a polynomial times $e^{-nH}$, by the excursion truncation and scalar estimate. This second possibility already requires a first switch of probability $O(e^{-nH})$. The latter bound follows from scalar stationary occupancy near level $n$ during a frozen cycle. Any $B$ refusal at the shallow state only lowers the physical workload.

For the first possibility, charge the first flip to its preceding visit in the frozen cycle with $W_1\ge n-O(1)$ and $W_2\ge n-k-O(1)$, or exchange labels. Expected visits are the stationary tail divided by $\mu(z)$. Multiplying (5) by $Ce^{-Hk}$, and summing $0\le k\le n$, gives $O(n^{-1/2}e^{-Jn})$. The sum for $k\le n/2$ converges geometrically with ratio $e^{-(H-\theta)}$. Larger $k$ contribute an exponentially smaller term. The correction from reaching deepest is negligible because $2H>J$.

For a matching lower bound use a confined local central limit bridge. Start and finish with a sufficiently large fixed number of joint erosions. Under the diagonal tilt the increments have positive drift in both coordinates, and, for the correct parity and times $n/v+O(\sqrt n)$, their two-dimensional point probability at the terminal site is at least $c/n$. A first-half deviation bound away from the lower walls, a reversed final-half bound away from the upper walls, and the uniform $O(1/n)$ point bound on the opposite half show that a positive fraction of these bridges stays interior. The times are disjoint first-switch events. Summing them and undoing the tilt gives $c n^{-1/2}e^{-Jn}$. The new $CC$ profile stabilizes with probability bounded below. [Confined bridge calculation](phase1_square_prefactor.md)

Finally the total exit from $C_0$ is $\Theta(e^{-nH_R})$. Bound its probability above by the frozen cycle occupation near either boundary and below by one specified coordinate's successful initial scalar excursion followed by stabilization of the changed profile. The mixed escape fraction towards $D_0$ is bounded away from zero since $Q_{MC_0}\le e^{-n\min(H_T,H_S+H_P)+o(n)}$ and $Q_{MD_0}\doteq e^{-nH_S}$. Thus the denominator of (3) has the asserted constant-order bounds. Its numerator's indirect term costs at least $\min(H_P+H_T-H_S,2H_P)>J$. Equation (3) and fixed-time comparison of physical and trace masses give the result.

## Linear rules with a nonpositive mixed cooperator drift

For $L,B$, the square-root result also covers strict PD payoffs with $R>P>1/2$ and $0<S\le1/2$. At every $0<\kappa_P<1$ and every feasible $\kappa_R$,

$$
 \frac{\pi_n(CC)}{\pi_n(DD)}
 =\Theta\!\left(n^{-1/2}e^{n(H_R-\log(A_P/B_P))}\right).
$$

Use only the two homogeneous deepest states for the trace. From a mixed profile the original defector can remain in $D$ for $Cn^2$ rounds with uniformly positive probability. Independently, the original cooperator has nonpositive depth drift and mean time $O(n^2)$ to switch, by the one-dimensional fair-walk recurrence at the slowest case $S=1/2$. After the first switch to $DD$, there is a uniform positive probability of reaching its core while preserving both actions. From either homogeneous profile, the fixed-time maturation argument still applies because $P,R>1/2$. Consequently every excursion to the two-core trace has uniform mean $O(n^2)$ and can be truncated at $n^4$ with superexponentially small error. This mixed-state estimate uses only independent mixed feedback. [Independent-game proof of the return-time bound](phase1_social_game.md)

The direct $DD$ transition upper bound just proved uses only that the surviving original defector's erosion probability is bounded above by its $DD$ value. Its scalar ruin and two-interval estimates therefore carry over to the two-core trace, even if the process passes through mixed deepest states. The lower bound is the same simultaneous confined bridge followed by $CC$ maturation. Conversely, the $CC$ first-exit rate is $\Theta(e^{-nH_R})$ by the scalar frozen-cycle bound and successful initial excursion. A single exit reaches $DD$ before returning to $CC$ with uniformly positive probability by the mixed-state estimate above, and a double exit goes directly to $DD$. Thus the reverse two-core transition has order $e^{-nH_R}$. The two-state stationary odds are the ratio of these forward and reverse transition probabilities. The homogeneous profile-to-core comparisons have bounded factors as before. Mixed occupation per trace excursion is bounded by the probability of any exit from its homogeneous profile times $O(n^2)$, so its stationary mass vanishes exponentially.

At $\kappa_P=1$, the direct $L$ transition requires just one scalar first passage. For $B$ both independent boundary choices switch with a fixed positive probability at their first joint boundary erosion. The scalar upper bound also applies, yielding stationary odds of order $e^{n(H_R-H_P)}$. At independent $DD$ feedback, with arbitrary feasible $CC$ correlation, the log slope is $H_R-2H_P$ and the odds have order $e^{n(H_R-2H_P)}$. [Independent-game bounds](phase1_social_game.md)

## Independent shocks and critical coexistence

For independent $DD$ and mixed-profile feedback, with arbitrary feasible $CC$ correlation, every strict equal-depth PD with effective $P>1/2$ satisfies

$$
 \frac{\pi_n(CC)}{\pi_n(DD)}=\Theta\!\left(e^{n(r-V)}\right),\qquad
 V=\begin{cases}
 \min(2p,p+t-s),& S>1/2,\\
 2p,& S\le1/2.
 \end{cases}
$$

Here the probabilities are effective reward probabilities and $(r,p,t,s)$ are their log odds. The result applies to $L,B$ and, after thinning the external penalties, to $K$. It includes the neutral mixed cooperator $S=1/2$. The uniform upper and lower factors imply coexistence at $r=2p$. In a strict PD the cascade cost is larger than $r$.

**A defector with a partially depleted memory.** Fix a polynomial horizon $L=L(n)$ and suppose player $Y$ is a defector who still needs $k$ levels of erosion to flip. The other player $X$ can be in any state. There are $\varepsilon,C>0$, independent of $n,k$ and both starting states, such that

$$
 \Pr(\text{some } CC\text{ by time }L)\le C e^{-(p+\varepsilon)k}.       \tag{6}
$$

Use $x=-n,\ldots,-1$ for $X$'s states from deepest to shallowest $D$ and $x=0,\ldots,n-1$ from shallowest to deepest $C$. Fix $0<\delta<p$ and write $w(x)=e^{\delta\min(x,0)}$. Until $Y$'s first flip we may simulate $X$ in the environment where its partner always defects. Write $I_Y=1$ for a proposed erosion and $I_Y=-1$ for a proposed deepening of $Y$. Define a positive kernel on $X$ by

$$
 {\cal T} f(x)=\mathbb E_x[e^{pI_Y}f(X_1)].
$$

When $x<0$, the two players' updates are independent, $\mathbb E e^{pI_Y}=1$, and in the interior

$$
 \mathbb E_x w(X_1)\le w(x)\big(Pe^{-\delta}+(1-P)e^\delta\big).
$$

A $B$ refusal at $x=-1$ only reduces this expectation. At $x=-n$ the reflection costs at most $C e^{-\delta n}$. When $x\ge0$, $w(x)=1$ and $\mathbb E e^{pI_Y}=Te^{-p}+(1-T)e^p<1$ because $T>P$. Thus, for some $\rho<1$, $\mathcal T1\le1$ and $\mathcal T w\le \rho w+C e^{-\delta n}$. Iteration gives $\mathcal T^j w\le \rho^j+C'e^{-\delta n}$.

First count paths on which $Y$ flips at step $j$ before a visit back to its deepest state. Up to the flip its proposed erosion sum is at least $k$, so $j\ge k$. A $B$ refusal can increase the proposed sum relative to the actual displacement. If $X$ still defects at that flip, its probability of also cooperating within the remaining horizon is at most $Cw(X_j)+CL e^{-pn}$. Indeed it must first switch under erosion probability at most $1-P$. Apply scalar ruin before its next visit to deepest and allow at most $L$ fresh excursions afterwards. The same bound covers $X_j\ge0$ since $w=1$ there.

Bound the original event indicator by $e^{-pk}e^{p\sum I_Y}$ on the specified paths. Dropping all path constraints inside the resulting nonnegative expectation, its upper bound summed over the crossing times becomes

$$
 C e^{-pk}\sum_{j=k}^{L}\big(\rho^j+C'e^{-\delta n}+L e^{-pn}\big).
$$

If $Y$ first visits deepest, repeat the estimate at its last such visit before flipping, with $k=n$. There are at most $L+1$ possible departure times, and the bounds are uniform in the state of $X$ at departure. Since $k\le n$ and $L$ is polynomial, choosing a sufficiently small fixed $\varepsilon>0$ absorbs all polynomially weighted errors and proves (6). The strict $T>P$ is what gives contraction while $X$ cooperates.

**Two flips out of $DD$.** Up to the first switch, compare with the frozen pair of independent reflected workloads. By independence the stationary mass above levels $n-O(1),n-k-O(1)$ is at most $C e^{-pn-p(n-k)}$. The same estimate up to a constant holds for the expected number of visits in a frozen cycle. If the other player is $k$ levels short just after the first switch, apply (6) and sum over $k$. The sum of $e^{-\varepsilon k}$ is finite. The polynomial truncation of a physical trace excursion therefore gives $Q_{D_0C_0}=O(e^{-2pn})$.

For the lower bound, the frozen independent unbounded workloads are reversible with stationary mass $\mu(n,n)=\mu(0,0)e^{-2pn}$. Starting from $(n,n)$ backward, both can stay strictly below their thresholds until hitting $(0,0)$ with probability bounded below. Force a fixed number of initial joint deepening steps, apply the scalar ruin bound to the subsequent descent and finish with the fixed-time maturation estimate. By reversal and the stationary cycle identity, the probability in a forward origin excursion of first touching either level $n$ exactly at $(n,n)$ is at least $c e^{-2pn}$. The two $B$ decisions at that moment contribute a constant. The new $CC$ profile can reach its core while preserving both actions with a uniformly positive probability. [Independent bridge calculation](phase1_square_prefactor.md)

**The mixed trace entry.** When $S>1/2$, freeze the independent $S,T$ pair from the mixed core until its first action change. A first flip by the original defector has probability $O(e^{-tn})$ by its frozen cycle occupancy. At a first flip by the original cooperator, the probability weight with the defector $k$ levels short is at most $C e^{-sn-t(n-k)}$ by the product geometric tails. Apply (6) at that flip. Taking $\varepsilon<t-p$ gives

$$
 Q_{MC_0}\le C e^{-tn}+C e^{-(s+p+\varepsilon)n}.
$$

There is also the lower bound $Q_{MC_0}\ge c e^{-tn}$. One designated player's independent biased excursion hits the switch before its first return to deepest in $O(n)$ rounds with probability at least a constant times its scalar ruin probability. The other player remains on its action over these rounds with probability tending to one. The new profile matures with uniformly positive probability. The same one-coordinate arguments give $Q_{D_0M}=\Theta(e^{-pn})$ and $Q_{MD_0}=\Theta(e^{-sn})$. The frozen-cycle marginal bound and first successful scalar excursion give $Q_{C_0D_0}+Q_{C_0M}=\Theta(e^{-rn})$ for any feasible correlation at $CC$.

In (3) the mixed escape fraction toward $D_0$ is bounded below. The possible error term in its numerator now has order at most $e^{-(2p+\varepsilon)n}$, smaller than the direct transition. This proves the displayed stationary odds throughout the stable region. When $S\le1/2$, use the two homogeneous cores as in the preceding section. The proof of (6) did not require a positive cooperator drift at mixed profiles, so the sharp bounds on the forward and reverse transitions apply there as well. The constant comparisons between homogeneous action and core masses complete both cases.

## Numerical checks

The included Decimal experiment computes $D$ by observing the chain after every round containing a reward. From one observation to the next, consecutive double penalties move the pair deterministically until a two-cycle (or a one-cycle after exchange lumping). Sum its geometric tail, solve the resulting $4n-1$ state chain, and weight each state by occupation during the intervening rounds. The code also compares with the full-chain stationary solver at $n=3$. For $K$ it solves the full transformed chain. All quantities below were calculated with 70 decimal digits.

| $R,P,T,S$ | $\kappa_R,\kappa_P$ | Tactic | $\pi_{24}(CC)$ | $\pi_{48}(CC)$ | Secant in log odds, $24\to48$ | Limit (1) |
|---|---|---|---:|---:|---:|---:|
| .80, .70, .90, .20 | 0, .70 | $D$ | .946506 | .999039 | .16974277 | .16974277 |
| .95, .70, .98, .20 | 0, −.20 | $D$ | .086728 | .034424 | −.04082199 | −.04082199 |
| .805, .70, .93, .20 | 0, .50 | $D$ | .216054 | .216054 | .00000000 | 0 |
| .76, .70, .77, .69 | 0, 0 | $D$ | .079021 | .018642 | −.07534944 | −.07534944 |

With $R=.80,P=.70,T=.90,S=.20$ and $\kappa_R=0,\kappa_P=1$, $\pi_{24}(CC)=.99981509$ for $D$ and $.00274120$ for $K$. The limiting log odds slopes are $+.40546511$ and $-.13815034$, respectively. These two computations use identical marginal payoffs and external correlations. At the Krylov critical endpoint $R=.75,P=.60,T=.90,S=.20,\kappa_P=1,\kappa_R=0$, the values of $\sqrt n\,\pi_n(CC)$ at $n=16,32,48,64$ are $.229115,.225575,.225033,.224949$, consistent with the proved square-root law. At an independent-shock Krylov tie $R=.80,P=.50,T=.90,S=.20$, the computed $CC$ masses at $n=16,32,48$ are $.08692916,.08685952,.08685896$.

```bash
python3 experiments/phase1_architectures.py --kinds D --n 8 24 48 --digits 70
python3 experiments/phase1_architectures.py --kinds K --cases private synchronized cascade --n 8 16 24 --digits 70
python3 experiments/phase1_architectures.py --kinds K --cases krylov-critical krylov-private-critical --n 16 32 48 64 --digits 70
```
