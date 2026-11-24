# Krinsky automata at the Fréchet endpoints

Two equal-memory Krinsky automata play a strict Prisoner's Dilemma with win probabilities $0<S<P<R<T<1$. A reward resets the player's current action to maximum depth. A penalty erodes one level, and a penalty at the shallowest level flips the action, leaving the new action shallow. Feedback is independent across players at a mixed profile and is redrawn conditionally on the current profile each round. The two homogeneous profiles may have any feasible, separately chosen Pearson correlations. Write $q_X=1-X$ and

$$
c=\Pr(--\mid DD)=q_P^2+\kappa_P Pq_P,\qquad
A=\max\{c,q_P q_T/q_S\}.
$$

**Theorem.** For every stationary law, with constants depending on the fixed feedback laws and independent of memory depth $n$,

$$
\frac{\pi_n(CC)}{\pi_n(DD)}
   =\Theta\!\left((A/q_R)^n\right),\qquad
\pi_n(CD)+\pi_n(DC)=O\!\left((q_P/q_S)^n\right).
$$

Since $q_P q_T/q_S<q_T<q_R$, mutual cooperation takes all the mass exactly when $c>q_R$. Mutual defection takes all the mass exactly when $c<q_R$. At equality, both homogeneous probabilities stay bounded away from zero. The two-round proof below includes feedback laws that forbid simultaneous rewards at either or both homogeneous profiles. The architecture analysis treats the positive double-reward case. [Architecture analysis](phase1_architectures.md)

At maximal anticorrelation, $c=(1-2P)_+$. Thus the selection boundary is **$R=2P$**. Even the strongest feasible anticorrelation selects full cooperation if $R>2P$. At $P\ge 1/2$, simultaneous penalties at $DD$ are impossible. Each departure from $DD$ then resets the remaining defector to maximum depth, and the odds decay with the exact exponential base $q_Pq_T/(q_Rq_S)$. The conclusion includes $P=1/2$, where every $DD$ outcome has exactly one winner.

## Two-round observations

Partition the feedback rounds into consecutive disjoint pairs. Mark the end of a pair if each player received at least one reward in the pair. From any initial state the conditional mark probability is at least $S^2$, by asking for a first-player reward followed by a second-player reward. After a mark each player's current action is either at maximum depth or one level below it. In particular it takes $n$ or $n-1$ successive penalties to change either action. Take $n\ge 6$ throughout the proof. Every fixed interval of $j$ consecutive rounds contains at least $j/2-1$ complete blocks. Its probability of avoiding marks is bounded by $K\theta^j$ for fixed $K<\infty$ and $\theta=\sqrt{1-S^2}<1$.

Write $H=R,P,M$ for the two homogeneous profiles and the union of the mixed profiles. Let $\alpha_H$ be the profile probabilities at marks in stationarity and $Q_{HG}$ the one-mark transition probabilities averaged over the stationary conditional distribution within $H$. A row with zero mass can be defined from an arbitrary marked state in its group. Then $\alpha Q=\alpha$. This balance identity only uses conditioning at consecutive marks. The grouped observations themselves can have memory.

The physical and marked masses obey $\pi(H)\asymp\alpha_H$, uniformly in $n$. Indeed, if $\lambda\ge S^2$ is the stationary probability of a mark at a block endpoint, $\lambda\alpha_H\le\pi(H)$. From any state in $H$ there is also a uniformly positive chance of a mark in $H$ within a bounded number of blocks. At a mixed profile a double reward suffices to put both players at maximum depth. At a homogeneous profile with positive double-reward probability the same construction works. Otherwise, if at most one player is shallow, reward that player first (either player if neither is shallow), then reward the other. If both are shallow, reward player one while player two flips, give the same player a reward and the other a penalty in the resulting mixed profile, then reward the newly returned second player. Both actions now belong to $H$ and their depths are within one of maximum. From there a mark in a complete next block has probability at least $S^2$, with at most one intervening round to align the blocks. Stationarity and a union bound over this bounded number of endpoints give the converse inequality. This short return through a mixed profile is needed when both players change action together into a profile with zero probability of a double reward.

## Bounds for one marked excursion

All bounds here hold uniformly for every marked starting state in the indicated profile. Write $m=n-1$ and $w=\max(c,q_T)$.

| Transition or sum | Bounds up to fixed positive factors |
|---|---|
| $Q_{RM}+Q_{RP}$ | $\asymp q_R^n$ |
| $Q_{PM}$ | $O(q_P^n)$, and $\asymp q_P^n$ when $c<q_P$ |
| $Q_{MP}$ | $\asymp q_S^n$ |
| $Q_{MR}$ | $\gtrsim q_T^n$, $O(w^n)$ |
| $Q_{PR}$ | $\gtrsim c^n$, $O(A^n)$ |

For the one-coordinate upper bounds, consider the last reward before the requisite first flip, using time zero if the player is still on their initial loss run. At least $m$ subsequent penalties are compulsory. Before a first departure from a homogeneous profile the loss marginal is $q_R$ or $q_P$. Before the initial mixed cooperator first defects its loss marginal is at most $q_S$. The geometric bound for a mark-free prefix sums over all possible last-reward times with a constant factor.

For a matching single-flip lower bound, ask the designated player to lose until it flips, with the other rewarded on the first and last rounds of that run. The two fixed outcomes cost a constant factor whenever the probability of a directed disagreement is positive. The other player stays put throughout the intervening rounds, and the penalized player prevents any earlier mark. At a mixed starting profile this gives both lower bounds $q_S^n$ and $q_T^n$. At $DD$ it gives $q_P^n$ when $c<q_P$. At $CC$ it gives $q_R^n$ whenever the rewards are imperfectly correlated. The new profile has one deeply committed player and one shallow player. A reward for the shallow player and a subsequent mark secure the profile. At perfect $CC$ correlation prescribe common losses until the first switch. If the original deficits differ, a double reward in the mixed profile settles the exit. If both switch together, the bounded homogeneous settlement above secures $DD$. During its initial excursion back through a mixed profile the same player wins twice, so no intervening mark can restore $CC$.

For the direct lower bound $Q_{PR}\gtrsim c^n$, use consecutive double penalties at $DD$ up to the first switch. If both switch together, use the homogeneous settlement at $CC$. Its first two rewards, if a detour is needed, go to the same player, and the preceding round contained two losses. Thus the first possible mark occurs after the desired $CC$ profile has been restored. If the deficits differ by one, the remaining defector is shallow. In one mixed round reward the new cooperator and penalize the remaining defector. This enters $CC$ with a deep player and a shallow player who can be rewarded immediately.

For the upper bound on $Q_{PR}$, stop at the first physical $CC$ in the excursion. For each player choose the last time they were rewarded as a defector before this stop, or zero if their marked initial $D$ commitment supplied the last reward. Each designated time begins $m$ compulsory rounds of defection and loss. Put the two start times in temporal order and write $d$ for their difference. During any unshared initial part of the first window its player loses with probability at most $q_P$. In the overlap, both defect and incur a double penalty with probability $c$. In the unshared end of the second window, the first player either cooperates, making the second loss probability $q_T$, or defects. In the latter case the first player must also lose because their last defector reward has already occurred. The round costs at most $w$ in either case. This conditioning includes arbitrarily many immediate flips back and forth at the shallow boundary.

For $d<m$ the prescribed windows therefore cost at most $c^{m-d}(q_Pw)^d$. For $d\ge m$ they cost at most $(q_Pw)^m$, with an additional geometric factor for the mark-free gap of length $d-m$. The prefix and gap bounds follow by conditional probability over disjoint deterministic intervals for each fixed pair of start times. Summing the prefix and gap, then using $c\le A$ and $q_Pw\le q_S A$, bounds the whole excursion probability by a constant times $A^m\sum_{d\ge0}q_S^d$. This proves $Q_{PR}=O(A^n)$.

For $M\to R$, if the initial cooperator is ever rewarded as a defector before first hitting $CC$, the same two-window argument bounds this contribution by $O(w^n)$, using $c\le w$ and $q_Pw<w$. Otherwise the initial defector's last defector reward alone supplies a compulsory length-$m$ window. Each required loss has probability at most $w$, by the same two alternatives for the other player. Summation over its mark-free prefix finishes the table.

## Stationary balance

Three-state balance gives

$$
\frac{\alpha_R}{\alpha_P}=
\frac{Q_{PR}(Q_{MR}+Q_{MP})+Q_{PM}Q_{MR}}
     {Q_{RP}(Q_{MR}+Q_{MP})+Q_{RM}Q_{MP}}.
$$

Since $w\le q_P<q_S$, the mixed exit sum is $\asymp q_S^n$. After dividing both numerator and denominator by this sum, the denominator is $\asymp q_R^n$. The numerator is at most a constant times $A^n+(q_Pw/q_S)^n=O(A^n)$. The direct route contributes a lower bound of order $c^n$. When $c<q_P$ the mixed route supplies an additional lower bound of order $(q_Pq_T/q_S)^n$. At $c=q_P$ the direct route already dominates. This proves the stated odds. Finally $\alpha_M(Q_{MR}+Q_{MP})=\alpha_R Q_{RM}+\alpha_P Q_{PM}$ gives the bound on the mixed mass. The comparison with the physical masses completes the proof.

## An exact prefactor when simultaneous defector penalties are impossible

Suppose $c=0$. Then $P\ge 1/2$. Write $b=q_Pq_T/(q_Rq_S)$ and let $M$ denote total mixed occupancy. The following equivalents identify the constants as well as the rates.

$$
\frac{\pi_n(CC)}{\pi_n(DD)}\sim
\begin{cases}
b^n,&\kappa_R<1,\\
\dfrac{2T}{1-q_Rq_T}\,b^n,&\kappa_R=1,
\end{cases}
\qquad
\frac{\pi_n(M)}{\pi_n(DD)}\sim 2(q_P/q_S)^n.
$$

The coefficient jumps at perfect synchrony of the cooperator rewards. For example, with $(R,P,T,S)=(.75,.50,.875,.25)$ the odds have base $1/3$ and their coefficient changes from $1$ to $56/31$. At $n=96$ the synchronized case gives $3^{96}\pi(CC)/\pi(DD)=1.80645161285795$, within $4.6\times10^{-11}$ of $56/31$.

**Regeneration and the mixed race.** Upon every $DD$ departure the other player must win. Up to exchange of players, the state is always the same newly switched, shallow cooperator and maximally deep defector. Use the interval between two such departures as a renewal cycle. Every state can reach this regeneration point, since in a mixed profile one player can be penalized through a switch while the other receives rewards, and the homogeneous settlement paths above have positive probability. The cycle contains exactly one uninterrupted final $DD$ visit. In the following, a deficit is the number of penalties still visible since the last reset, with deficit zero at maximum depth.

For independent mixed feedback let $U$ be the waiting time for $n$ consecutive cooperator penalties starting deep. The geometric sequence of loss runs gives
$\mathbb EU=(1-q_S^n)/(S q_S^n)$ and $\mathbb EU^2=O((\mathbb EU)^2)$. For the second bound, the conditional remaining mean from every deficit is at most $\mathbb EU$. Summing this bound over times before $U$ gives $\mathbb E[U(U+1)]\le 2(\mathbb EU)^2$. In the independent defector stream, count starts of the word consisting of a reward followed by $n$ penalties, completed before $U$. Their expected number is $Tq_T^n(\mathbb EU+O(n))$. Two occurrences at distance at most $n$ are mutually exclusive, and at larger distance the words are independent. The second factorial moment is $O(q_T^{2n}\mathbb EU^2)$, of smaller order than the first moment. The initial unpreceded loss run and a tie in completion time each contribute $O(q_T^{n-1})$ when the defector starts within one level of maximum.

The shallow cooperator must win the first round, of probability $S$, before this race begins. The probability of reaching $CC$ before $DD$ is consequently $T(q_T/q_S)^n(1+o(1))$, including the possible continuation after a simultaneous switch. Conditional on reaching $CC$, the incumbent cooperator has deficit at most $n/10$ with probability $1-o(1)$. Indeed, before $U$ the expected number of visits to deficit $j$ is $q_S^{j-n}$ for $0\le j<n$, by counting the loss runs that reach $j$. The expected number of the independent defector words that finish while the cooperator has deficit at least $k$ is therefore $O(q_T^n q_S^{k-n})$. Choosing $k=\lfloor n/10\rfloor$ makes their contribution negligible relative to the race probability.

**The first switch from a deep homogeneous profile.** With homogeneous win marginal $x$, write $q=1-x$ and $u=\Pr(--)$. If $u<q$, the mean time to the first switch from deficits at most $n/3$ is $(1+o(1))/(2xq^n)$, uniformly, and with probability $1-o(1)$ the other player has deficit at most $n/10$ at this switch. Here is a short proof. Freeze the outcome law and count the two players' reward-then-$n$-penalty words. In a block of length $L=\lfloor q^{-n/2}\rfloor$ their total mean is $(1+o(1))2xq^n L$. For overlapping words on different players with start difference $d\le n$, the joint probability is at most $q^{2d}u^{n-d}$. Summation of these overlaps costs $O(Ln\max(u,q^2)^n)=o(Lq^n)$. Nonoverlapping word pairs contribute $O((Lq^n)^2)$, and same-player overlaps are impossible. Thus a block contains a word with probability $(1+o(1))2xq^nL$. Complete blocks are independent. Up to time $v/(2xq^n)$ for fixed $v$, words crossing block boundaries have probability $O(vn/L)$, and an initial loss run from the stated deficits completes with probability at most $2q^{2n/3}$. The scaled first-switch time converges to a mean-one exponential and is uniformly integrable by the geometric bound using complete blocks. At a switch word, $k$ trailing losses of the other player cost an additional factor at most $(u/q)^k$ relative to the $q^n$ loss run. On the same time horizon a union bound with $k=\lfloor n/10\rfloor$, followed by $v\to\infty$, proves the deficit assertion. If $u=q$, one common reward synchronizes the depths before a switch with probability $1-o(1)$ from the same starting range. The resulting common run has mean waiting time $(1+o(1))/(xq^n)$.

**Occupation during a cooperative visit.** From any $CC$ starting state, the expected total $CC$ time before hitting $DD$ is $O(q_R^{-n})$. Each $CC$ episode ends within a mean single-player run time. At a single exit the new defector can win the next round, with probability $T$. From a maximally deep defector in mixed play, the chance of a defector switch before or together with a cooperator switch is $O((q_T/q_S)^n)$, uniformly over the cooperator's deficit. This follows by bounding the possible defector-run completions up to the independent cooperator waiting time. Thus the number of $CC$ episodes has a uniform geometric tail.

For $\kappa_R<1$, the first switch from a deep $CC$ occurs after mean $(1+o(1))/(2R q_R^n)$. The new defector is shallow, and the other player is far from the boundary with probability $1-o(1)$. Until the shallow player next wins, each of its penalties switches its action again. The probability its reward arrives while defecting is
$h=T/(1-q_Tq_R)$. The change of action of the other player during these retries has probability $o(1)$, since the time to the reward has a uniform geometric tail. A reward as defector gives a mixed state with a deep defector and hence hits $DD$ first with probability $1-o(1)$. A reward as cooperator reestablishes $CC$ with both deficits at most $n/3$ with probability $1-o(1)$. The expected $CC$ time before $DD$ from any such pair of deep starts is consequently $(1+o(1))/(2R h q_R^n)$. Formally, the liminf of the minimum and limsup of the maximum of these means, scaled by $q_R^n$, satisfy the respective lower and upper renewal inequalities with inhomogeneous term $1/(2R)$ and return coefficient $1-h$. The preceding uniform bound controls the exceptional starts.

At the first $CC$ entry of the cycle, the new cooperator is shallow. Its chance of committing to cooperation across the immediate retries is $R/(1-q_Rq_T)$. Thus the conditional expected $CC$ occupation before $DD$ is $(1+o(1))/(2Tq_R^n)$. For $\kappa_R=1$, a committed deep $CC$ pair instead exits jointly straight to $DD$ after mean $(1+o(1))/(Rq_R^n)$. The same initial commitment probability now gives conditional mean $(1+o(1))/[(1-q_Rq_T)q_R^n]$.

**Finishing the renewal cycle.** With probability $1-o(1)$ the first mixed episode ends when the cooperator switches, leaving a shallow defector beside an old defector of deficit at most $n/10$. For this last assertion, sample the old defector's independent stream at the cooperator's first-switch time. The chance of $k$ trailing defector penalties is at most $q_T^k$. The newborn defector immediately wins with probability $P$ and establishes $DD$. Otherwise the next penalty ends the cycle. All other initial $DD$ configurations have a uniform mean holding-time bound $O(q_P^{-n})$. Since $c=0<q_P$, the mean $DD$ occupation is asymptotic to $P/(2Pq_P^n)=1/(2q_P^n)$.

The mean length of the first mixed episode is asymptotic to $S\mathbb EU\sim q_S^{-n}$. Truncating $U$ at the rare defector switch changes its mean by $o(\mathbb EU)$ by the second-moment bound and Cauchy–Schwarz. Further mixed episodes occur with probability $o(1)$, and contribute $o(q_S^{-n})$. In detail, from any mixed start a first switch takes mean $O(q_S^{-n})$. A simultaneous switch leaves both players shallow, giving a fixed positive chance of reaching a homogeneous profile in one more round. This bounds the expected number of first-switch races per visit to mixed play by a constant. The uniform bound on the number of $CC$ episodes then gives an $O(q_S^{-n})$ bound on further mixed occupation, conditional on its being required. Multiplying the first-entry probability by the conditional $CC$ occupation derived above and dividing all cycle occupations by the mean $DD$ occupation gives the two asserted equivalents.

## Finite-memory checks

The following 75-digit calculations compare the full chain to the independent reward-epoch reduction at $n=4$, then use the latter for larger memories. The slope in the last column is the increment of $\log[\pi(CC)/\pi(DD)]$ between $n=32$ and $64$, divided by 32. The parameters are ordered $R,P,T,S$.

| Game | $(\kappa_R,\kappa_P)$ | Exact odds base | $\pi_{64}(CC)$ | Slope |
|---|---|---:|---:|---:|
| $(.90,.80,.95,.20)$ | $(0,-.25)$ | $1/8$ | $1.59307830\times10^{-58}$ | $-2.07926267$ |
| $(.75,.50,.875,.25)$ | $(0,-1)$ | $1/3$ | $2.91232356\times10^{-31}$ | $-1.09858459$ |
| $(.50,.20,.75,.10)$ | $(-1,-.25)$ | $6/5$ | $0.999184544$ | $0.18230773$ |
| $(.40,.20,.75,.10)$ | $(0,-.25)$ | $1$ | $0.0172651445$ | $-0.00000634$ |

In the third row neither homogeneous profile permits a double reward. The fourth row illustrates critical coexistence with very unequal finite-memory masses. At fixed payoffs $(.375,.20,.75,.10)$ and $\kappa_R=-.6$, changing $\kappa_P$ through the **negative** value $-3/32$ changes selection. The exact bases at $\kappa_P=-.25,-3/32,-.01$ are $24/25,1,3192/3125$, respectively. At $n=256$ the corresponding cooperation probabilities are $2.85851707\times 10^{-7}$, $0.0117166926$, and $0.748229337$.

```bash
python3 experiments/phase1_anticorrelated_reset.py
python3 experiments/phase1_anticorrelated_reset.py --cases complementary-synchronized-CC --n 24 48 96
python3 experiments/phase1_anticorrelated_reset.py --cases negative-defection negative-critical negative-cooperation --n 128 256
```
