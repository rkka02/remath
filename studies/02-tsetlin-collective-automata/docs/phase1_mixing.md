# Equal-barrier fluctuations and mixing under a common shock

The stationary joint tail of a reflected walk, the first joint flip in an action profile, and the time for an entire automata game to mix are three different observables. The results below specify the event and its initial law in every case. The synchronization theorem applies to the full linear-tactic game at the common-shock endpoint.

## 1. The stationary tail with infinite upper capacity

Write a loss as a step $+1$ toward an action change and a win as $-1$. Fix $1/2<p<1$, $q=1-p$, $\delta=p-q$, $\lambda=\log(p/q)$ and $-q/p\leq\kappa\leq1$. The iid pairs of increments have probabilities

$$
 a=q^2+\kappa pq,\quad b=pq(1-\kappa),\quad b,\quad c=p^2+\kappa pq
$$

in the order $(++),(+-),(-+),(--)$. For the free sums $S_i(k)$ starting at zero, let $M_i=\sup_{k\geq 0}S_i(k)$. The pair $(M_1,M_2)$ is the stationary law of the infinite-depth process $W_i(k+1)=\max(0,W_i(k)+X_i(k+1))$. Iterating from zero in the remote past gives the joint representation with the same sequence of *reversed* increments for both coordinates. Negative drift makes the suprema finite. [Loynes (1962)](https://doi.org/10.1017/S0305004100036781)

Malyshev studied stationary point asymptotics for two-dimensional positive walks. Flatto derived joint point asymptotics for two parallel queues with common arrivals and independent exponential servers. Kobayashi and Miyazawa analyzed directional marginal tails for two-dimensional reflected walks. A related free-walk problem of Pan and Borovkov requires the walk to enter a distant orthant at a single time. In the workload event below the two free coordinate maxima may be attained at different times. [Malyshev (1973)](https://www.mathnet.ru/eng/smj4352) [Flatto (1985)](https://doi.org/10.1137/0145052) [Kobayashi and Miyazawa (2012)](https://arxiv.org/abs/1201.3167) [Pan and Borovkov (2019)](https://arxiv.org/abs/1708.09605)

Set $H_n=\Pr(M_1\geq n,M_2\geq n)$, $h=\log[(p-\kappa\delta)/(q+\kappa\delta)]$ and, when $a>0$, $t=\tfrac12\log(c/a)$. The following are exact equivalents for each fixed admissible correlation.

| Correlation | $H_n$ as $n\to\infty$ |
|---|---|
| $-q/p\leq\kappa<0$ | $2\exp[-(\lambda+h)n](1+o(1))$ |
| $\kappa=0$ | $\exp(-2\lambda n)$ exactly |
| $0<\kappa<1$ | $C(p,\kappa)n^{-1/2}\exp(-2tn)(1+o(1))$ |
| $\kappa=1$ | $\exp(-\lambda n)$ exactly |

### The ordered first-passage identity

For a vector $\theta$ satisfying $\mathbb E e^{\theta\cdot X}=1$, write $\Pr_\theta$ for the iid law with one-step weights $e^{\theta\cdot X}\Pr(X)$. Let $T_i=\inf\{k:S_i(k)=n\}$. At $T_1<T_2$, the second coordinate's conditional probability of subsequently reaching $n$ is $e^{-\lambda(n-S_2(T_1))}$. The tilt $\theta=(h,\lambda)$ normalizes because the two terms with $X_1=+1$ have total weight $e^h(q+\kappa\delta)$, and the two terms with $X_1=-1$ have total weight $e^{-h}(p-\kappa\delta)$. Symmetry and summation over the discrete stopping time give the identity

$$
 H_n=e^{-(\lambda+h)n}\left[2\Pr_{(h,\lambda)}(T_1<T_2)+\Pr_{(h,\lambda)}(T_1=T_2<\infty)\right]. \tag{1}
$$

For $\kappa<0$, $h>\lambda$, the first tilted drift is $v_1=\delta(1-2\kappa)>0$, and $v_1-v_2=2b(e^{h-\lambda}-e^{\lambda-h})>0$. The strong law makes the first coordinate win this race with probability tending to one, even when $v_2\leq0$. The two ordered possibilities account for the coefficient 2. At $\kappa=0$ the original suprema are independent. At $\kappa=1$ the two coordinates coincide.

### The constant for positive correlation

The diagonal tilt $\Pr_* = \Pr_{(t,t)}$ interchanges $a$ and $c$ and preserves $b$. Each coordinate now has upward probability $p$. Put $\sigma^2=8b/\delta$ and, for even $d\geq0$, define

$$
 u_d=\Pr_*(S_1(k)>0,\ S_2(k)>-d\ \text{for every }k\geq1).
$$

Then the coefficient in the table is

$$
 C(p,\kappa)=\frac{2}{\delta\sigma\sqrt{2\pi}}
 \left[u_0+2\sum_{j\geq1}e^{-2j(\lambda-t)}u_{2j}\right]. \tag{2}
$$

This is a convergent expression in the step probabilities. Truncating the time in any $u_d$ at $K$ gives absolute error at most $2(2\sqrt{pq})^{K+1}/(1-2\sqrt{pq})$ by a union bound and the one-coordinate Chernoff inequality. The tail in $j$ is bounded by a geometric series. Also $u_0>0$, since after a fixed number $B$ of common upward steps the chance either coordinate ever drops to zero is at most $2(q/p)^B$.

To prove (2), stop when either free coordinate first reaches $n$. If the other coordinate has deficit $d$, its subsequent catch probability contributes $e^{-\lambda d}$. Removing the diagonal tilt contributes $e^{-2tn+td}$. Thus $e^{2tn}H_n=\mathbb E_* e^{-(\lambda-t)d}$. Only even deficits occur. For a specified first-hit endpoint $(n,n-d)$, reverse the order of all increments up to its arrival time. Every proper forward prefix lies below $n$ in both coordinates. In the reversed sums this requires $S_1(k)>0$ and $S_2(k)>-d$ for every positive time up to arrival. Hence the first-hit probability under the tilt equals the Green function at $(n,n-d)$ for a walk killed when either of these inequalities fails at a positive time.

For the unrestricted tilted Green function $G$, at every fixed even $j$,

$$
 \sqrt n\,G(n,n+j)\longrightarrow c_0=\frac{2}{\delta\sigma\sqrt{2\pi}},
 \qquad \sup_y G(n,y)\leq C_0/\sqrt n. \tag{3}
$$

Indeed, at the first passage $T_1$ to $n$, $S_2(T_1)-n$ is a sum of $n$ iid, centered, span-two ascending ladder displacements. Their variance is $\sigma^2$ by the stopped second-moment identity for $S_2-S_1$, whose one-step variance is $8b$, and $\mathbb E_* T_{1\text{ level}}=1/\delta$. The single-level ladder epoch has exponential tails by positive drift. The displacements $0$ and $-2$ both have positive one-step probability. The lattice local central limit theorem gives a point mass asymptotic $2/(\sigma\sqrt{2\pi n})$ at each fixed even displacement and a uniform bound of order $n^{-1/2}$. After the first passage, convolution with $G(0,\cdot)$ multiplies the limit by $\sum_jG(0,j)=1/\delta$, the expected number of visits of the one-dimensional upward-biased walk to zero. This proves (3).

For the killed Green function subtract from $G$ the paths after the first violation $\tau$ of the two strict inequalities. At fixed $\tau$ and $S(\tau)$, (3) gives the same constant $c_0$ for the translated target. The bound in (3) is uniform on $\tau\leq n/2$. On $\tau>n/2$ with $\tau<\infty$, the probability is exponentially small, since a coordinate with upward probability $p$ must be nonpositive at violation. Everywhere $G(x,y)\leq1/\delta$. The killed limit is therefore $c_0 u_d$. Summing against $e^{-(\lambda-t)d}$ uses (3) again, and there are two possible orientations when $d>0$.

For a simpler independent calculation, let $A_{12}$ mean that after the first visit of $X$ to $n$, the second coordinate reaches or exceeds $n$ at some time, including that instant. This definition permits earlier visits of the second coordinate. Then $\Pr(A_{12})\leq H_n\leq2\Pr(A_{12})$. With $L=S_2(T_1)-n$, the exact transform gives

$$
 e^{2tn}\Pr(A_{12})=\mathbb E_*\left[e^{-tL}{\bf1}_{L\geq0}+e^{(\lambda-t)L}{\bf1}_{L<0}\right].
$$

Its coefficient after multiplication by $\sqrt n$ is

$$
 C_{12}=\frac{2}{\sigma\sqrt{2\pi}}
 \left[\frac{1}{1-e^{-2t}}+\frac{e^{-2(\lambda-t)}}{1-e^{-2(\lambda-t)}}\right]. \tag{4}
$$

### Two critical windows

The powers change in different windows at the two endpoints of the positive-correlation interval.

* **Near independence.** If $\sqrt n\,\kappa_n\to z\in\mathbb R$, then
  $$
   e^{n(\lambda+h(\kappa_n))}H_n\longrightarrow 2\Phi\!\left(-z\sqrt{2\delta/(pq)}\right). \tag{5}
  $$
  Under the tilt in (1), both drifts tend to $\delta$ and $v_1-v_2=-4\delta\kappa_n+O(\kappa_n^2)$. For a direct first-passage central limit argument set $m=\lfloor n/\delta\rfloor$. Each $T_i=m+O_{\Pr}(\sqrt n)$ by maximal inequalities and positive drift. The centered sums over any $O(\sqrt n)$ window about $m$ fluctuate by $o_{\Pr}(\sqrt n)$, again by the maximal inequality. Consequently $T_i=n/v_i-(S_i(m)-v_i m)/v_i+o_{\Pr}(\sqrt n)$. At independence the limiting variance per step of $S_1-S_2$ is $8pq$. The bounded-increment triangular-array CLT gives the normal race probability in (5) and vanishing tie probability.
* **Near perfect correlation.** If $n(1-\kappa_n)\to w\geq0$, then
  $$
    e^{2t(\kappa_n)n}H_n\longrightarrow
     \mathbb E\left[(q/p)^{|N_+-N_-|}\right],\qquad
     N_+,N_-\ \text{independent Poisson}(pq w/\delta). \tag{6}
  $$
  Under the diagonal tilt the first boundary time divided by $n$ converges in probability to $1/\delta$. At the deterministic time $\lfloor n/\delta\rfloor$, the two counts of discordant shocks converge jointly to these independent Poisson variables. Replacing that time by the first boundary time changes neither count with probability tending to one, by first restricting the time difference to $\eta n$ and then sending $\eta$ to zero. The deficit is twice the absolute difference of the counts, and $2(\lambda-t)\to\lambda$.

### What transfers to a first corner

For a walk reflected at zero, started at $(0,0)$, let one excursion end at its next return to $(0,0)$. Count success when it reaches $(n,n)$ during that excursion, before any coordinate exceeds $n$. For fixed $0<\kappa<1$, the success probability is $\Theta(n^{-1/2}e^{-2tn})$. For the upper bound the expected occupation of $[n,\infty)^2$ per excursion is $H_n/\pi(0,0)$ by regeneration, where $\pi(0,0)>0$. For the lower bound use the diagonal tilt and force $B$ initial joint upward steps and $B$ final joint upward steps. During the central segment go from $(B,B)$ to $(n-B,n-B)$ in $s=(n-2B)/\delta+O(\sqrt n)$ steps of the required parity, staying within $[1,n-1]^2$.

The two-dimensional lattice local CLT gives mass at least $c_1/n$ for each such endpoint and time in a fixed-width central window on the $\sqrt n$ scale. Bad bridges hitting the lower boundary in the first half have mass at most $C(q/p)^B/n$ by the strong Markov property and the uniform local CLT. Reversing increments bounds bridges hitting the upper boundary in the second half the same way. Upper exits in the first half and lower exits in the second half have exponentially small mass by concentration and reversal. Fix $B$ large enough. The first arrival at the corner is the final step, so summing over order $\sqrt n$ distinct times and undoing the tilt gives the lower bound. The same construction provides a lower bound at a stationary doubly capped corner, since both reversed free walks then hit $n$ before their first visit to $-1$.

The cutoff changes the problem for sufficiently negative correlation. For instance, at $\kappa=-q/p$, a common upward step is impossible, hence a positive capped corner cannot be entered at all. The infinite reflected tail is still positive with the equivalent in the table. A finite upper cap in the reversed stationary event requires **each coordinate** to reach $n$ before it first visits $-1$. Indeed, the backward preimage of the target state $n$ is an upper interval whose width follows the reversed free increments until it fills the state space or becomes empty. The killed-corner power at negative correlation requires its own analysis.

### Independent shocks and the probability of an exactly simultaneous first switch

Let the two frozen profiles have independent jumps, fixed win probabilities $p_i>1/2$ and memories $n_i$. Start both at deepest memory. Write $q_i=1-p_i$, $r_i=q_i/p_i$, $\delta_i=p_i-q_i$, and $\rho_i=(\delta_i^2/p_i)r_i^{n_i}$. Suppose both memories grow and their ratio remains bounded above and below by positive constants. For the times $T_i$ of their first individual linear-tactic switches in the frozen medium,

$$
  \Pr(T_1=T_2)\sim\frac{\rho_1\rho_2}{\rho_1+\rho_2},\qquad
  \mathbb E\min(T_1,T_2)\sim\frac{1}{\rho_1+\rho_2}. \tag{7a}
$$

At equal rewards and equal depths this gives $\Pr(T_1=T_2)\sim[(2p-1)^2/(2p)](q/p)^n$. Both coordinates first reach their exit levels at this same time. The related event that merely visits the last pair of pre-switch states has a different coefficient involving the squared Catalan numbers. [Frozen-corner derivation](phase1_quadrant.md)

Use the independent equilibrium workloads reflected at zero, with state mass proportional to $r_1^i r_2^j$. A cycle starts at the origin and stops at its first positive return or the first visit to $\{i\geq n_1\}\cup\{j\geq n_2\}$. If its first hit is a point $x$, path reversal gives its probability as $[\pi(x)/\pi(0,0)]$ times the probability from $x$ of reaching the origin while staying strictly below both thresholds at every intervening positive time, including the first reverse step. For $x=(n_1,n_2)$ this reverse probability tends to $\delta_1\delta_2$. For $x=(n_1,j)$ with $j$ fixed it tends to $\delta_1$.

Here are finite-volume details for these limits. In each tip coordinate measure reverse position as its distance down from the tip. Before the distance reaches $n_i$ this is a free walk with upward probability $p_i$. Its probability of remaining strictly positive forever from zero is $p_i(1-r_i)=\delta_i$. A lower bound follows by first taking a fixed time horizon large enough that, except for arbitrarily small probability, each surviving tip coordinate has distance at least a fixed $K$. A violation from there before first reaching its bottom has probability at most $r_i^K$. After reaching the bottom, the chance of a threshold hit in $(n_1+n_2)^2$ more steps is $O((n_1+n_2)^2r_i^{n_i})$ by the stationary geometric tail and monotone coupling from zero. For a coordinate initially at fixed $j$, its probability of a threshold hit before first reaching zero is $O(r_i^{n_i-j})$. Reaching the joint bottom takes expected time $O(n_1+n_2)$ for the comparison with reflection at both ends. Each coordinate hits its bottom in that order of time in mean by the drift bound, and from the bottom its probability of occupying that point at any specified time is at least $1-r_i$ by monotonicity. Independence gives a uniform positive probability of simultaneous bottom occupancy at the end of a sufficiently long block of order $n_1+n_2$. Iterate the blocks. Thus the common time window suffices with probability tending to one. The upper limit for the reverse probability follows by retaining only the first fixed number of steps and then increasing that number. This proves both reverse limits.

The per-cycle tie probability is therefore asymptotic to $\delta_1\delta_2r_1^{n_1}r_2^{n_2}$. Summing the single-tip formula over $0\leq j<n_2$ with the summable weights $r_2^j$ gives $\delta_1r_1^{n_1}/(1-r_2)$ for the first player alone, and interchange gives the second term. A tie has smaller order than the sum of these terms. The ratio of the tie probability to any-exit probability gives the first statement of (7a). The mean truncated-cycle length converges by domination to the mean return time $1/[(1-r_1)(1-r_2)]$. Dividing it by the per-cycle exit probability gives the second statement.

## 2. Exact total-variation profile of the synchronized game

Take two linear-tactic $L_{2n,2}$ automata of equal depth. At each equal-action profile, both players receive the same reward or penalty. The reward probabilities are $p_C=p_R$ and $p_D=p_P$. At the two mixed profiles shocks are independent with probabilities $(p_S,p_T)$ for the cooperator and defector. Assume

$$
 0<p_S<1/2<p_D<p_C<p_T<1.
$$

Let $d_n(m)=\max_x\|P_n^m(x,\cdot)-\pi_n\|_{\rm TV}$ over **all** $4n^2$ starting states, including transient states. Set $R_a=p_a/(1-p_a)$, $\delta_a=2p_a-1$, and

$$
 M_a=\frac{R_a^n-1}{\delta_a},\qquad
 \mathcal R=1+\frac{1}{R_D-1}+\frac{1}{R_C-1},\qquad A_n=\mathcal R M_D.
$$

For every fixed $s>0$ and $0<\varepsilon<1$,

$$
 d_n(\lfloor sA_n\rfloor)\longrightarrow e^{-s},\qquad
 t_{\rm mix}^{(n)}(\varepsilon)\sim A_n\log(1/\varepsilon). \tag{7}
$$

The mean trip from deepest mutual defection to deepest mutual cooperation is asymptotic to $A_n$. The reverse mean is asymptotic to $\mathcal R M_C$. Their ratio grows exponentially. In particular the longer return time is compatible with rapid approach to a stationary distribution concentrated on cooperation. The exponential profile also implies absence of total-variation cutoff in this regime.

### Entry into the recurrent class

The synchronized states, where both actions and depths agree, form a closed irreducible birth-and-death path. Every start enters this class in expected time at most $K n$ for a constant depending only on the four payoffs.

In an unequal-depth, equal-action profile the shallower depth has ordinary biased steps before hitting its deepest level $n-1$ or the switching level $-1$. Its upper hitting probability is at least $1-(1-p_a)/p_a$. If it hits the top, the other depth is also at the top by order preservation. The expected absorption time is at most $n/\delta_a$ by the stopped drift identity. Otherwise the actions become mixed. In a mixed profile the time until an attempted profile change is bounded by the cooperator's time to switch if the profile were frozen, with expectation at most $n/(1-2p_S)$ by the negative drift of depth, including at its reflecting top. A simultaneous switch leaves the actions mixed. Conditional on a switch, the probability of exactly one switch is bounded below by a fixed positive number. If just one player is at switching depth it is one. If both are there it is $[p_S(1-p_T)+p_T(1-p_S)]/(1-p_Sp_T)$. The strong Markov property and geometric bounds on the number of attempts give the uniform $O(n)$ estimate. In particular the diagonal is the unique closed class. Pittel treated depth synchronization for a common-shock Goore game with randomized-boundary automata. Here common shocks occur only at equal actions, and the opposite-action parameters determine the transient estimate. [Pittel (1965), §2](https://www.mathnet.ru/eng/ppi752)

### The resistance and the passage law

Index each branch by depth $j=0,\ldots,n-1$, with $0$ next to the other action and $n-1$ deepest. On the diagonal the reversible mass is

$$
 \mu(a,j)=\frac{R_a^j}{1-p_a},\qquad \sum_j\mu(a,j)=M_a.
$$

The edge between the two depth-zero states has conductance one. The edge from depth $j-1$ to $j$ has conductance $R_a^j$. The stationary cooperation mass is $M_C/(M_C+M_D)\to1$. This one-dimensional geometric stationary law is part of Tsetlin's original random-medium setting. [Tsetlin (1961)](https://www.mathnet.ru/eng/at12417)

Order the path from deepest $D$ to deepest $C$. For an initial endpoint $x$ at deepest $D$ and a target $y$ of $C$-depth $k$ ($k=\lfloor n/2\rfloor$ or $k=n-1$), the finite-chain identity is

$$
 \mathbb E_x T_y=\sum_{e\text{ from }x\text{ to }y} r_e\,\mu([x,e^-]),\qquad r_e=(\mu(e^-)P(e^-,e^+))^{-1}. \tag{8}
$$

This follows by summing the discrete Poisson equation for the mean hitting time up to each edge and telescoping. For an edge on the $D$ side the omitted part of $M_D$ below that edge has mass $O(R_D^j)$ and the edge resistance is $R_D^{-j}$. On the $C$ side the additional prefix of $C$ has mass $O(R_C^j)$ and resistance $R_C^{-j}$. Thus (8) differs from $M_D\mathcal R_{n,k}$ by $O(n)$, where

$$
 \mathcal R_{n,k}=1+\sum_{j=1}^{n-1}R_D^{-j}+\sum_{j=1}^{k}R_C^{-j}\longrightarrow\mathcal R.
$$

The hitting time divided by its mean converges to a unit exponential law. To see this directly, let an attempt begin at $x$ and end after at least one step upon return to $x$ or arrival at $y$. Its duration is $V$ and success probability is $h_n=1/[\mu(x)\mathcal R_{n,k}]$ by the one-dimensional voltage formula. For that formula, from the neighbor of $x$ the chance of reaching $y$ first is the first edge's resistance divided by the total. Multiply by the probability of leaving $x$ in the first step. In particular $h_n$ decays exponentially. Up to absorption at either endpoint, the current depth has a positive conditional drift at least $\min(\delta_C,\delta_D)$, including at the central switching edge. Thus the expected remaining attempt duration from any interior point is $O(n)$. Repeating the Markov bound in blocks of order $n$ gives $\mathbb EV^2=O(n^2)$. Renewal gives $\mathbb E V=h_n\mathbb E_xT_y\to R_D/(R_D-1)>0$.

For $u=\theta/\mathbb E_xT_y$, the Laplace transform of $T_y$ equals $\mathbb E[e^{-uV};\text{success}]/(1-\mathbb E[e^{-uV};\text{failure}])$. The numerator is $h_n+o(h_n)$ because $\mathbb E[V;\text{success}]\leq O(n)\sqrt{h_n}$. Taylor expansion with the second-moment bound gives denominator $h_n+u\mathbb EV+o(h_n)$. Their ratio tends to $1/(1+\theta)$. The same argument with the two branches interchanged gives the reverse passage scale. Volkonskii proved an exponential limit for first action changes in related automata, and Fill relates general birth-and-death passage distributions to spectral data. [Volkonskii (1965), Theorem 1](https://www.mathnet.ru/eng/ppi735) [Fill (2009)](https://arxiv.org/abs/0707.4042)

### From passages to total variation

Adjacent states on the oriented path have right-step probability at the left state plus left-step probability at the right state at most one. The sum equals one within either branch and equals $(1-p_C)+(1-p_D)<1$ at the central edge. The quantile coupling therefore preserves order. When the process started at deepest $D$ reaches deepest $C$, all coupled diagonal starts have coalesced, including a stationary copy. This gives $d_{\rm diagonal}(m)\leq\Pr_x(T_{C,n-1}>m)$. For the lower bound use the set of $C$ states of depth at least $\lfloor n/2\rfloor$, whose stationary mass tends to one. From deepest $D$, the total-variation distance is at least $\Pr_x(T_{C,\lfloor n/2\rfloor}>m)-o(1)$. Both passage times have the same exponential limit after division by $A_n$. For transient starts split off $n^2$ initial steps. The uniform synchronization estimate gives failure probability $O(1/n)$, and $n^2=o(A_n)$. This proves (7).

### The leading eigenvalue below one

Put $M_{\rm eff}=(M_C^{-1}+M_D^{-1})^{-1}$. The absolute spectral gap of the full chain satisfies

$$
  1-\max_{\zeta\ne1}|\zeta|\sim\frac{1}{\mathcal R M_{\rm eff}}. \tag{9}
$$

The closed-class calculation works whenever both branch rewards exceed $1/2$, including equal rewards. Use unnormalized reversible energy $\mathcal E(f)=\sum_e r_e^{-1}(f(e^+)-f(e^-))^2$ and variance $\operatorname{Var}_\mu f=\sum_x\mu(x)(f(x)-\bar f)^2$. Replace $f$ on each branch by its value at its deepest endpoint, giving a two-valued function $g$. Cauchy–Schwarz along the path from depth $j$ to its own deepest endpoint gives $|f(a,j)-g(a,j)|^2\leq C R_a^{-j}\mathcal E(f)$. Summing yields $\|f-g\|_\mu^2\leq C n\mathcal E(f)$. The exact variance of $g$ is $M_{\rm eff}(g_C-g_D)^2\leq M_{\rm eff}\mathcal R_{n,n-1}\mathcal E(f)$. The triangle inequality for centered functions gives the lower bound on the positive spectral gap. For the matching upper bound, take the harmonic voltage between deepest endpoints, normalized to zero and one. Its energy is $1/\mathcal R_{n,n-1}$, and its variance is asymptotic to $M_{\rm eff}$ by the same two-valued approximation.

Negative eigenvalues cannot control this exponential scale. Change the sign of $f$ at every other vertex to form $v$. Then $\langle f,(I+P)f\rangle_\mu=\mathcal E(v)+2\sum_a \mu(a,n-1)p_a v(a,n-1)^2$. The approximation bound just proved and $M_a/\mu(a,n-1)=O(1)$ give $\|v\|_\mu^2\leq Cn\langle f,(I+P)f\rangle_\mu$, hence $1+\zeta_{\min}\geq c/n$ in the closed class. For transient states, if $\max_x\mathbb E_x T_{\rm sync}\leq Kn$, the substochastic transient block has survival norm at most $1/2$ after $\lceil2Kn\rceil$ steps. Its spectral radius is at most $2^{-1/\lceil2Kn\rceil}$. The spectrum of the full block-triangular transition matrix is the union of the two spectra, proving (9).

## Numerical checks

Run `python experiments/phase1_mixing.py --tv --certificates --windows` using an interpreter with `mpmath` and NumPy. The calculation uses 85-digit arithmetic and adds exact rational checks of detailed balance and of two independent finite-path hitting-time formulas. The Fourier integral for (4) uses the ascending ladder characteristic function, obtained by first-step decomposition. With the tilted step weights $c,b,b,a$, put $A(u)=ce^{iu}+be^{-iu}$ and $B(u)=be^{iu}+ae^{-iu}$. The first-level factor is $F(u)=2A(u)/(1+\sqrt{1-4A(u)B(u)})$. The centered ladder displacement has characteristic function $e^{-iu}F(u)$. The principal square root is continuous since $|4A(u)B(u)|\leq4pq<1$.

For $p_D=0.7,p_C=0.8$, the limiting resistance is $25/12$. The exact forward mean divided by $A_n$ is $0.998045647611483$ at $n=8$ and $0.999999999990694$ at $n=32$. At $n=32$ the reverse trip already takes $20,633,425.49$ times as long on average. At $p=0.7,\kappa=0.3$, the ordered probability $\sqrt n e^{2tn}\Pr(A_{12})$ is $1.50208976003886486$ at $n=64$ and $1.55804650421789468$ at $n=1024$, approaching the coefficient $1.56236469877528918$ in (4).

The certificate uses integer fixed-point masses and rational transition weights. Removed mass at each iteration, the probability of reaching the finite lower cutoff, and the probability of remaining active at the finite time horizon all have separate upper bounds. For $p=4/5$ and $\kappa=1/2$, (2) gives $C=1.51387951321209602894828971341941037\ldots$. The rational bracket before its elementary multiplier has width below $7.1\times10^{-54}$. The computed $\sqrt n e^{2tn}H_n$ is $1.46329419060599909$ at $n=32$ and $1.48685742374859918$ at $n=64$. The unscaled rational expectation at $n=64$ has an enclosure of width below $1.2\times10^{-54}$.

At $n=144$ and $p=4/5$, the finite values for (5) at $z=-1/2,+1/2$ are $1.85784228052823$ and $0.200394788450305$, respectively, with limits $1.82909647977$ and $0.170903520231$. For (6) at $w=1$ the finite value is $0.713615888406501$, with limit $0.71287423989554$. These rational finite-$n$ enclosures each have width below $10^{-18}$. For the synchronized game the closed-class worst total variation at $n=24$ and time $\lfloor A_n\rfloor$ is $0.3678767765708023$ and the normalized absolute gap $\mathcal R M_{\rm eff}\,(1-\max_{\zeta\ne1}|\zeta|)$ is $1.0000000316502$.

For (7a) the script diagonalizes each finite killed birth-and-death matrix. If $\Pr(T_i=t)=\sum_j b_{ij}\ell_{ij}^{t-1}$, summing the product of two such series gives the exact finite tie probability $\sum_{j,k}b_{1j}b_{2k}/(1-\ell_{1j}\ell_{2k})$. At $p=0.7$ and $n=32$ the exact-to-asymptotic ratios for the tie probability and the mean first-switch time are $1.000000000052407$ and $0.999999999995398$.
