# Three memory regimes in a Prisoner's Dilemma with weak rewards

Let $1>T>R>P>S>0$ be the reward probabilities. Each player uses the same $L$ or $B$ tactic and has depth $n$ per action. Feedback pairs are independent in time conditional on the current profile, and their marginals are as specified by the game. Outcomes at a mixed profile are independent. At each symmetric profile assume that all four pairs of outcomes have positive probability, allowing either sign of correlation. Boundary coins for $B$ are independent of each other and of the feedback. Write $\pi_n$ for the unique stationary law. The order of the four action profiles is $CC,CD,DC,DD$.

Tsetlin gives the linear tactic and its one-player stationary weights in §2, p. 11, and introduces the randomized shallow boundary in §6, p. 25. The one-player weights enter the two-player result through an opponent facing a persistent defector. [Tsetlin, 1963](https://www.mathnet.ru/rus/rm6373)

## The weak-reward phase boundary

Suppose **$R<1/2$**. Define

$$
 u=\frac{1-2P}{2(1-P-S)},\qquad b=\frac{T-P}{1-P-S},\qquad
 \mu=\frac{(1-2P)(T+S-1)}{1-P-S}.
$$

| Payoffs | Stationary large-memory behavior |
|---|---|
| $T+S<1$ | Both absolute depths have uniformly bounded exponential moments. Each of the four action profiles has stationary probability bounded away from zero as $n\to\infty$. |
| $T+S=1$ | One player defects with depth divided by $n$ converging to the uniform law on $[0,1]$. The other player has a limiting geometric depth distribution on each action. Mutual cooperation has probability $\Theta(n^{-1})$. |
| $T+S>1$ | One player defects within a tight random distance of maximum depth $n$. The other player has the same limiting two-sided geometric distribution as at equality. |

In the last two rows the stationary action frequencies converge to

$$
 \boxed{\ (0,\ u/2,\ u/2,\ 1-u)\ } .
$$

The persistent defector's identity is equiprobable by exchange symmetry. Tightness is a statement under the stationary law for each $n$. It does not assert that a given labeled player keeps the role forever.

For example, in the independent game $(R,P,T,S)=(.45,.20,.95,.10)$, the limit for $L$ and $B$ is $(0,3/14,3/14,4/7)$. The independent Krinsky and Krylov criteria give the respective thresholds $2P-P^2=.36$ and $2P/(1+P^2)=5/13$. Both architectures select $CC$ at $R=.45$. This reverses the ordering observed with all four reward probabilities above one half. [Krinsky and Krylov phase criteria](phase1_architectures.md)

### Signed depth and the one-player environment

At physical depth $d\in\{1,\ldots,n\}$ use the signed coordinate $y=\pm(d-1/2)$ for $L$, and $y=\pm d$ for $B$, assigning positive sign to $D$. Write $M=n-1/2$ or $n$, respectively, for the cap. In the $B$ coordinate the gap between shallow states has length two. A penalty there crosses that gap with probability one half, so its **mean** signed displacement equals that of an ordinary penalty step. On the infinite-depth grid the respective signed drifts for $C,D$ are $1-2p_i,2p_i-1$ everywhere. At a finite cap $+M$ subtract $p_i$ from the drift, and at $-M$ add $p_i$.

Freeze one player's action at $D$. The opponent's infinite chain is a positive-recurrent birth–death chain whenever $S,P<1/2$. If $a=S$ on $C$ and $a=P$ on $D$, detailed balance gives

$$
 \nu(a,d)\ \propto\ \frac1{1-a}\left(\frac a{1-a}\right)^{d-1},\qquad d\ge1.
 \tag{1}
$$

At the central edge the factor $1/2$ for $B$ cancels from detailed balance. Consequently $\nu(C)=u$. Averaging the persistent defector's depth increment gives $u(2T-1)+(1-u)(2P-1)=\mu$. The same identity holds pointwise after adding a correction. If the defector has signed depth $x$ and the opponent signed depth $y$, then away from the deep caps and the defector's switch,

$$
 \mathbb E[\Delta(x-by)\mid x,y]=\mu .
 \tag{2}
$$

Indeed the two possible drifts of $x-by$ are $2T-1-b(1-2S)$ and $(1-b)(2P-1)$, which agree. This derivation uses only the feedback marginals.

### Tightness and escape from finite depths

Put $X=\max(y_1,y_2)$, $Y=\min(y_1,y_2)$. When $R<1/2$ there are $c,C>0$, independent of $n$, with

$$
 \mathbb E_{\pi_n}e^{c|Y|}\le C .
 \tag{3}
$$

For the negative tail, track either player's $C$ depth. Away from the shallow boundary its probability of deepening is at most $R<1/2$. For the positive tail of $Y$, both players are defecting when $Y$ is large. Track a player who currently has the smaller depth. Its deepening probability is $P<1/2$, and the next minimum is at most its next position. In each case a sufficiently small exponential moment contracts by a fixed factor away from the interface, with a bounded one-step contribution near it. Reflection at the relevant deep cap only reduces the moment. Stationary averaging gives (3).

If $\mu<0$, use $F=X-bY$. For $X>4$ and $X-Y>4$, the larger coordinate is a defector and the ordering cannot change. Formula (2) gives $\mathbb E\Delta F\le\mu$, including finite reflections. Reflection of $X$ at $+M$ or $Y$ at $-M$ decreases this drift. In the remaining states $F\le 4+(1+b)|Y|$. Bounded increments imply that $e^{\theta F}$ contracts by a fixed factor in the first set for sufficiently small $\theta>0$. In the second set its one-step expectation is uniformly integrable by (3), taking $\theta$ smaller if needed. Thus $\sup_n\mathbb E e^{\theta F}<\infty$, and $X=F+bY$ yields uniform exponential tails for both players' absolute depths. Every subsequential stationary limit is an invariant probability on the infinite grid. Full support permits a path to any action profile from any state, by prescribing each player's signed directions. The parity classes of the infinite $L$ walk both admit all four profiles. Every subsequential limit consequently charges each profile, proving the lower bounds in the first row.

If $\mu\ge0$, let $Z=y_1-y_2$. On the infinite grid, convexity makes $|Z|$ a submartingale. At a symmetric profile the two signed drifts agree. At a mixed profile the drift in the direction of the existing gap is $2(T+S-1)$. It is strictly positive when $T+S>1$. At equality full support gives a strictly positive one-step drift of $|Z|$ at a collision, or at an odd gap of one that can cross zero. Every state can reach a mixed profile and an interior pair of $D$ depths with gap zero or one (prescribe the directions, respecting parity for $L$). Hence the infinite chain admits no invariant probability. To see this even for a putative law without a first moment, stationarity of $\min(|Z|,K)$ implies zero expected drift of $|Z|$ upon letting $K\to\infty$, by bounded increments. The strict drift on an accessible set contradicts this.

A pointwise subsequential limit of finite stationary masses is an invariant subprobability on the infinite grid because every state has finitely many potential predecessors. It must have total mass zero. Together with (3) this proves $X\to+\infty$ in stationary probability. With probability tending to one the larger player is a defector, the smaller identity is stable for the next step, and the smaller player is away from either cap. Testing stationarity against any bounded, finitely supported function of $Y$ now gives the one-player balance equations (1). Tightness in (3) and uniqueness of $\nu$ yield $Y\Rightarrow\nu$, proving the limiting frequencies.

### Positive drift pins a defector to the deep cap

If $\mu>0$, define $G=M-X\ge0$. In stationarity, apply (2) to $F=X-bY$ and use the bounded increments, (3), and $X\to+\infty$. All errors except reflection of the larger player tend to zero. Consequently

$$
 \mathbb E_{\pi_n}[p_{\rm high}(Y)\mathbf 1_{\{G=0\}}]\ \longrightarrow\ \mu ,
 \qquad p_{\rm high}(y)=T\,\mathbf1_{\{y<0\}}+P\,\mathbf1_{\{y>0\}} .
 \tag{4}
$$

Take a pointwise subsequential limit of the laws of $(G,Y)$, of mass $m\le1$. This is an invariant finite measure for the chain with an always-defecting upper player reflected at $G=0$ and the opponent on the entire signed grid. Indeed the predecessor set of any bounded set is bounded in these coordinates and for large $n$ the finite transition rules coincide there. The quantity $-G-bY$ has mean increment $\mu-p_{\rm high}(Y)\mathbf1_{\{G=0\}}$ in that chain. Truncate it at both ends, then pass to the limit using bounded increments. Its integrated drift is zero, so the boundary flux of the limiting measure equals $m\mu$. By (3) one may also take the limit in (4), giving the same flux $\mu$. Therefore $m=1$, and the distance of the persistent defector from depth $n$ is tight.

### Zero drift spreads depth uniformly

Suppose $T+S=1$. At every profile the two signed drifts agree before finite-cap corrections. If $p_i$ denotes the current reward marginal, write $b_i=p_i(\mathbf1_{\{y_i=-M\}}-\mathbf1_{\{y_i=M\}})$. Stationarity applied to $Z^2$ gives the exact finite-$n$ identity

$$
 2\mathbb E\!\left[|Z|\sum_i p_i\mathbf1_{\{|y_i|=M\}}\right]
    =\mathbb E[(\Delta Z)^2]\le 16 .
 \tag{5}
$$

The event that a lower cap is occupied is exponentially small by (3). At an upper cap $|Z|\ge M/2$ except on an exponentially small event by (3). Thus the probability of any cap is $O(1/n)$. All limits of $Z/n$ are supported on $[-1,1]$, since the smaller signed coordinate is exponentially tight and the larger coordinate is at most $M$.

Along any subsequence where $Z/n\Rightarrow\lambda$, the joint limit of $(Z/n,Y)$ is $\lambda\otimes\nu$. For a bounded Lipschitz function $h(Z/n)$ and a finitely supported function $v(Y)$, test stationarity of the product. The first factor changes by $O(n^{-1})$, while the second uses the frozen-opponent transition with probability tending to one as above. In the limit each conditional law of $Y$ is invariant for that same chain, hence equals $\nu$.

For a smooth function $f$ on $[-2,2]$ with $f'(-1)=f'(1)=0$, Taylor-expand the one-step stationary balance of $f(Z/n)$ and multiply by $n^2$. The linear term is $n\mathbb E[f'(Z/n)(b_1-b_2)]$. On the upper cap, the mean-value bound gives $n|f'(Z/n)|\le C(1+|Y|)$. Its expected contribution tends to zero by the cap estimate and (3). Lower-cap contributions are exponentially small. The Taylor remainder is $O(n^{-1})$. Conditional second moments away from caps and switches of the larger identity depend only on $Y$. Their positive $\nu$-average is

$$
 \sigma^2=8uS(1-S)+8(1-u)P(1-P)(1-\kappa_P)
   +\mathbf1_{\{B\}}\frac{(1-2P)(1-2S)}{1-P-S}.
 \tag{6}
$$

In a mixed profile the two signed increments have the same mean and are independent. In $DD$ their covariance is $4\kappa_P P(1-P)$. A shallow $B$ penalty contributes one extra unit of conditional variance from its private boundary coin. Averaging that correction gives $\sum_{a=S,P}(1-a)\nu(a,1)$, the last term of (6). Therefore the remaining stationary identity is $\int f''\,d\lambda=0$. The second derivatives with these Neumann endpoint conditions include every smooth function of zero Lebesgue mean on $[-1,1]$. This identifies $\lambda$ as the uniform probability on $[-1,1]$. In particular $X/n\Rightarrow\operatorname{Uniform}[0,1]$, independently in the limit of $Y$. Equation (6) is the bulk variance in this stationary proof. A path-space Brownian invariance principle would require a separate argument.

### The $1/n$ window and the sharp order of mutual cooperation

Fix $R<1/2$, $P,S$, and both symmetric-profile correlations. Suppose $n(T_n+S-1)\to a\in\mathbb R$. Throughout this window the stationary limit of $(X/n,Y)$ is the product of (1) and the following density on $[0,1]$:

$$
 g_a(x)=\frac{e^{kx}}{\int_0^1e^{kt}\,dt},
 \qquad k=\frac{4 a u}{\sigma^2}.
$$

The action frequencies still converge to $(0,u/2,u/2,1-u)$, with $\pi_n(CC)=\Theta(n^{-1})$. Thus the symmetric $DD$ feedback correlation changes the shape of the transition window through (6).

The limiting infinite grid is the critical grid, so the same compact-escape proof and (3) give the same convergence of the shallow coordinate. The drift of $Z$ in the interior now equals
$2(T_n+S-1)\operatorname{sgn}(Z)\mathbf1_{\rm mixed}$. In (5) the right-hand side acquires the term $4(T_n+S-1)\mathbb E[|Z|\mathbf1_{\rm mixed}]$, which is bounded. The cap probability and the product limit argument therefore carry over. For $W=|Z|/n$ use a twice continuously differentiable test $\phi$ with $\phi'(0)=\phi'(1)=0$, smoothly extended beyond 1. Its even extension at zero is twice continuously differentiable. The additional first-order term in the scaled stationary equation converges to $2au\int\phi'\,d\lambda_W$. The second-order term remains $(\sigma^2/2)\int\phi''\,d\lambda_W$. The difference $W-X/n$ tends to zero by (3). Writing $\phi'(x)=e^{-kx}v(x)$ for test functions with $v(0)=v(1)=0$, the equation becomes $\int v'(x)e^{-kx}\,d\lambda_W(x)=0$. This identifies $g_a$, including the absence of endpoint atoms.

For the microscopic rate set $B_n=\sum_i p_i\mathbf1_{\{|y_i|=M\}}$. On the occupied upper cap one has $\big||Z|-n\big|\le 1+|Y|$; the exponentially rare lower cap has negligible effect. The cap probability bound and (3) give $\mathbb E[(n-|Z|)B_n]\to0$. The product law in the perturbed identity (5) now gives

$$
 n\mathbb E B_n\ \longrightarrow\
 \frac{\sigma^2}{2}+2au\int_0^1xg_a(x)\,dx
 =\frac{\sigma^2}{2}g_a(1).
$$

For an integer $j$, define the nonnegative crossing term
$L_j=|Z'-j|-|Z-j|-\operatorname{sgn}(Z-j)(Z'-Z)$, using $\operatorname{sgn}(0)=0$. It is bounded and vanishes for $|Z-j|>4$. Stationarity gives $\mathbb E L_j\le \mathbb E B_n+2|T_n+S-1|=O(1/n)$ uniformly in $j$. At $Z=j$ away from the caps, full support gives $\mathbb E[L_j\mid y_1,y_2]\ge c>0$. Hence $\Pr(Z=j)\le C/n$, including the cap contribution. When $j=0$ the sign of the cap drift points toward zero on $\{Z\ne0\}$. A cap with $Z=0$ is exponentially rare by (3). It follows that

$$
 n\,\mathbb E L_0\ \longrightarrow\
 \frac{\sigma^2}{2}g_a(1)-2au
 =\frac{\sigma^2}{2}g_a(0)>0 .
$$

To control excursions of the shallow player at a specified gap, take
$V=e^{\theta(-y_1)_+}+e^{\theta(-y_2)_+}+e^{\theta Y_+}$.
The proof of (3) gives a one-step bound $\mathcal PV\le\rho V+C$ for some $\rho<1$. Since $|\Delta Z|\le4$, multiplying by $e^{-\varepsilon|Z-j|}$ preserves contraction outside the additive term when $e^{4\varepsilon}\rho<1$. Stationarity and the uniform point-mass bound for $Z$ yield

$$
 \mathbb E[e^{-\varepsilon|Z-j|}V]\le C'\mathbb E e^{-\varepsilon|Z-j|}
 \le C''/n,\qquad
 \Pr(Z=j,|Y|\ge m)\le C''e^{-\theta m}/n .
$$

In $CC$, $|Y|\ge|Z|$, so summing this estimate over $j$ proves $\pi_n(CC)=O(1/n)$. Since $L_0$ is bounded and supported on $|Z|\le4$, its positive limiting scaled flux places at least $c/n$ probability there. The last estimate leaves at least $c/(2n)$ on $|Z|\le4,\ |Y|\le m_0$ for a fixed large $m_0$. From this finite set, full support gives a uniform positive probability of entering $CC$ within a fixed number of steps. Summing the stationary probabilities over those steps gives the matching $\pi_n(CC)\ge c'/n$.

## The cooperative phase with weak punishment

For $R>1/2$ the following two conditions each give an exact rate for the stationary probability that at least one player defects.

1. $P<1/2$ and $T+S\le1$.
2. $P=1/2$, with arbitrary $T,S$ satisfying the strict payoff ordering.

In either case

$$
 \boxed{\quad \lim_{n\to\infty}-\frac1n\log(1-\pi_n(CC))
    =\log\frac R{1-R}.\quad}
 \tag{7}
$$

**Duration of a $CC$ visit.** Put $h=\log(R/(1-R))>0$. From every entrance state of $CC$, its mean uninterrupted duration lies between $c e^{nh}$ and $C e^{nh}$ for constants independent of $n$. The duration is at most the exit time of one coordinate with frozen reward marginal $R$. For a reflecting one-dimensional depth walk the usual first-step equations give mean exit time $O(e^{nh})$ from depth $n$, also for the half-switch at shallow depth in $B$. For the lower bound first prescribe a fixed number $d_0$ of simultaneous rewards, which has uniformly positive probability. A frozen marginal walk starting at depth at least $d_0$ has probability at most $C e^{-h d_0}$ to exit before reaching $n$. Each subsequent excursion from $n$ has probability at most $C e^{-nh}$ to exit before returning. Over $c_0e^{nh}$ steps, the union bound for both walks leaves a positive probability of no exit, upon choosing $d_0$ large and $c_0$ small. The frozen coupling is valid until the first exit, for either sign of feedback correlation.

**Return with $P<1/2$ and $T+S\le1$.** From every outside state the mean time to $CC$ is polynomial in $n$. First reach $CC$ or a state with one defector and the other player shallow. From $DD$, monitor either player until the first switch. Both drifts toward depth one are at least $1-2P>0$. From a mixed profile the cooperator has drift toward depth one of $1-2S>0$ until somebody switches. A one-dimensional negative-drift walk with the allowed shallow holding has mean switch time $O(n)$. At a simultaneous switch in a mixed profile both players are shallow. Markov's inequality gives a fixed success probability for this preliminary step within $O(n)$ rounds.

Track the designated defector, initially at some depth $x$, with a shallow opponent. As long as the tracked player stays at depth greater than $m=A\log n$, its opponent follows the finite chain (1), truncated at $n$. In every round preserve the opponent's signal marginal, and decrease the conditional probability of the defector's reward, given the opponent's signal, by $\delta=(\log n)/n$. Full support makes this a legal change for all large $n$, with relative entropy $O(\delta^2)$ per step. Under this law the correction in (2) has drift at most $\mu-2\delta\le-2\delta$ while the opponent is away from its caps. The defector's upper cap only improves this bound.

From a shallow start the opponent has a uniform-in-time exponential depth tail by the same one-step drift estimate used for (3), since both $S,P<1/2$ here. Up to $H=\lceil 2n/\delta\rceil$ rounds the chance that its depth exceeds $m$ tends to zero for large fixed $A$. Stop at either this event or the first time the defector's depth is at most $m$. On the event of no stop by $H$, $x-by$ is at least $-b(m+2)$ despite starting at most $n+O(1)$. Azuma's inequality applied to the bounded-increment stopped process with its negative drift removed bounds this probability by $\exp(-c n^2/H)=o(1)$. Thus the tilted probability of getting both players to depth $O(\log n)$ by $H$ is at least $1/2$. The path relative entropy is $O(H\delta^2)=O(\log n)$. The binary relative-entropy inequality $Q(E)\ge1/2\Rightarrow P(E)\ge\exp[-2(D(Q\|P)+\log2)]$ yields original success probability $n^{-O(1)}$. From these depths, simultaneous prescribed directions bring both players into $CC$ in $O(\log n)$ rounds at another polynomial cost. A coordinate already in $C$ can oscillate there while the other crosses, preserving the possible $L$ parities. Uniform polynomial success in each polynomial-length trial proves the mean return bound.

**Return with $P=1/2$.** From a mixed profile reach $CC$ or $DD$ in $O(n)$ time with fixed probability by the same cooperator estimate; a simultaneous switch leaves both shallow and permits direct entry to $CC$ at bounded cost. It suffices to show a subexponential uniform mean return from $DD$. Let $m=\lceil n^{3/4}\rceil$ and $H=\lceil n^{4/3}\rceil$, for $n$ large. Within $O(m)$ prescribed rounds of the fair $DD$ walk put both depths between $m$ and $n-m$. Each coordinate can move away from the nearer cap and oscillate when already inside. This costs at most $\exp(Cm)$ in inverse probability.

From this interior point tilt the i.i.d. $DD$ increments to follow the line segment to $(2m,2m)$ in $H$ rounds. For the four increment pairs $s\in\{-1,1\}^2$, changing their probabilities by $v\cdot s/4$ gives the prescribed mean vector $v=O(n/H)$; full support ensures positivity. The total relative entropy is $O(H|v|^2)=O(n^{2/3})$. A maximal bounded-increment inequality gives probability tending to one to stay within $m/2$ of the line, because $m^2/H\to\infty$. On this event both players stay in $DD$ and finish within $3m$ of the interface. Prescribe $O(m)$ more directions to enter $CC$. Again the binary entropy bound gives success probability at least $\exp(-C n^{3/4})$, uniformly from $DD$, in $O(H)$ rounds. Iteration gives a subexponential mean return.

Under stationary sampling at entrances of $CC$, the ratio of total outside and inside probabilities is the ratio of their mean durations between such entrances. The outside duration is at least one and has subexponential mean by the return bounds. The inside mean is $\Theta(e^{nh})$. This proves (7).

## Pinning at and above the fair cooperation reward

Suppose instead $P<1/2$ and $T+S>1$. There is a constant $c>0$, depending on $P,S,T$ and the feedback in the mixed and $DD$ profiles, for which the pinned-defector conclusion in the third row continues to hold when $R=1/2$, and whenever $R>1/2$ and $\log(R/(1-R))<c$.

To see this, start from one defector at $+M$ and the opponent at depth $O(\log n)$. Fix a small $\varepsilon>0$ such that $2b\varepsilon<1/4$. Until the designated defector falls below $n/2$, the opponent follows the fixed-$D$ chain, whose geometric tail gives probability at most $\exp(-c_1n)$ to exceed $\varepsilon n$ by time $\exp(c_2 n)$, for small enough $c_2>0$. This follows by a union bound over times using the uniform exponential moment from the specified initial depth. Between visits of the defector to its cap, (2) gives positive drift $\mu$ and bounded increments. Thus $\exp[-\theta(x-by)]$ is a supermartingale for small $\theta>0$ until the defector returns to its cap or the opponent exceeds $\varepsilon n$. At the beginning of such an excursion $x-by\ge M-1-b\varepsilon n$. On hitting depth $n/2$ while the opponent stays in range it is at most $n/2+b\varepsilon n+O(1)$. The supermartingale bound, followed by a union over excursions, shows that the mean time before leaving

$$
 \{\text{some defector has depth at least }n/2,\ 
             \text{the other depth is at most }\varepsilon n\}
 \tag{8}
$$

is at least $\exp(c_3 n)$ for a fixed $c_3>0$.

For a return to the initial cap region, an outside start can be reduced to $CC$ or to a defector with a shallow opponent within $O(n)$ rounds with fixed probability, as in the preceding proof. From $CC$, the mean time to exit is at most $C n^2$ if $R=1/2$ by the scalar fair-walk first-step equations, or $C e^{nh}$ if $R>1/2$. On exit, both players may be shallow. Otherwise there is a shallow defector facing a possibly deep cooperator. With probability bounded below independently of $n$, this player remains a defector while the cooperator reaches shallow depth in $O(n)$ rounds. Indeed the two mixed feedbacks are independent, $T>1/2$, and the finitely capped biased defector walk started shallow survives $O(n)$ rounds with a uniform positive probability by the same ruin estimate as for the $CC$ holding time.

From a defector with a shallow opponent, prescribe $A\log n$ rounds to give the defector depth at least $A\log n$ (or hold it at its cap) while leaving the opponent shallow up to a bounded distance. This costs $n^{-O(1)}$. Until the defector reaches its cap, the opponent stays within $B\log n$ for $O(n)$ rounds with probability tending to one for large $B$. Take $A>4bB+4$. The exponential supermartingale just used prevents a return below $A\log(n)/2$ with probability tending to one on that interval. A bounded-increment lower-tail estimate for (2) then shows that the cap is reached by $C'n$ rounds with probability tending to one for large $C'$. At the hitting time the opponent has depth $O(\log n)$.

Markov's inequality and repetition of these trials give a mean time to that cap region of at most a polynomial times $1+e^{nh}$ for $R>1/2$, and a polynomial for $R=1/2$. Comparing these returns with the mean residence in (8) gives exponentially small stationary probability outside (8) when $h<c_3$ or $R=1/2$; one may reduce $c_3$ to absorb polynomial factors. On (8), the smaller coordinate follows the exponentially contracting fixed-$D$ chain. In the stationary drift bound for $e^{\theta|Y|}$, the complement of (8) contributes at most $C e^{\theta n}\pi_n((8)^c)$, uniformly bounded for small $\theta$. This recovers (3) and $X\to+\infty$; equations (1) and (4) give the same limiting frequencies and tight upper-cap distance. This argument supplies an open strip above $R=1/2$. Identifying its exact outer boundary requires the large-deviation escape cost from a persistent defector.

## The face $R=1/2$

Under the same full-support hypothesis, the stationary action-frequency alternatives on this face are as follows. Strict ordering gives $S<P<1/2<T$.

| Condition | Large-memory action frequencies |
|---|---|
| $T+S<1,\ \kappa_R\ge0$ | $\pi_n(CC)\to1$. |
| $T+S<1,\ \kappa_R<0$ | All four action profiles have positive lower limiting probabilities. |
| $T+S=1$ | The limit is $(0,u/2,u/2,1-u)$. In particular $\pi_n(CC)=O(n^{-\epsilon})$ for some $\epsilon>0$, and $O(n^{-1})$ if $\kappa_R<0$. |
| $T+S>1$ | The same limiting action frequencies hold, with one player pinned within a tight distance of the deep $D$ cap. |

The final row was proved above. For the remaining rows, write $r_j=\pi_n(C_i,\ d_i=j)$ for either fixed player. Level balance gives $r_{j+1}\le r_j$ since a cooperator's reward marginal never exceeds one half. Thus $r_n\le1/n$. Also $\min(y_1,y_2)_+$ has a uniform exponential tail because its large values require two defectors with reward $P<1/2$.

**A contraction away from $CC$ when $T+S<1$.** Here $b<1,\ \mu<0$. Smooth the expression $F=X-bY$ as

$$
 F_K=\tfrac12(1-b)(y_1+y_2)+\tfrac12(1+b)\psi_K(y_1-y_2),
$$

where $\psi_K$ is a smooth even convex approximation to absolute value, agrees with it outside $[-K,K]$, has $|\psi_K'|\le1$, and $|\psi_K''|\le C/K$. Such a function is obtained by convolution with a smooth symmetric density of radius $K$. Bounded increments give a Taylor error $O(1/K)$ in its one-step drift. In $DD$ the first-order drift equals $\mu$ before cap corrections. In a mixed profile away from the finite set $|Z|\le K+4$, (2) applies. In $CC$ the first-order drift is zero. Reflection at a positive cap has nonpositive effect on the first-order term, since the derivative in the larger coordinate is positive. Corrections at negative caps are bounded and their stationary mass is $O(1/n)$.

If $\kappa_R\ge0$, the infinite-depth chain has infinite mean duration of a $CC$ visit starting at any fixed pair of cooperative depths. For $L$, each marginal probability of surviving $t$ steps is at least $c/\sqrt{t+1}$ by the reflection principle for the simple symmetric walk. The two survival events are increasing functions of the respective reward sequences. Conditional on one reward sequence the other has independent coordinates whose reward probabilities increase with the corresponding first-player outcomes. Positive association of the independent first-player sequence gives a lower bound by the product of the marginal survivals. A $B$ player can also stay at a shallow penalty where $L$ would have already exited, giving the same lower bound. The divergent sum of $c^2/(t+1)$ proves the claim. Every closed communicating class visits $CC$ from outside with positive probability. Positive recurrence would give a finite mean return to an outside reference state, contradicting this infinite mean duration. Thus all finite compact sets have stationary mass tending to zero by the earlier local-limit argument. Stationarity of $F_K$ then gives
$\limsup_n |\mu|\pi_n((CC)^c)\le C/K$. Taking $K\to\infty$ proves the first row.

**Negative cooperative correlation when $T+S<1$.** Define $v=(1-T)/T<1,\ A=(1-T)/(2T-1)$, and set $\ell=1$ for $L$, $\ell=2$ for $B$. The positive function

$$
 H(C,d)=A+\ell+d-1,\qquad H(D,d)=A v^{d-1}
$$

is harmonic on the infinite grid against a fixed cooperator. A shallow penalty changes $H$ by $-1$ in mean on $C$ and $+1$ in mean on $D$, for both tactics. At deep $D$ the geometric ratio solves $T v+(1-T)v^{-1}=1$. Let $H_i=H(a_i,d_i)$. In $CC$, $\mathbb E\Delta(H_1H_2)=\kappa_R$, since conditional mean increments are $+1,-1$ and all boundary coins are private. In mixed profiles independence gives $\mathbb E\Delta(H_1H_2)=-(1-2S)H(D,d_D)<0$. In $DD$ the drift tends uniformly to zero as the larger depth grows, by geometric decay. Reflecting $C$ rewards only decrease the product. Truncation of $H(D,\cdot)$ at the positive cap costs $O(nv^{n-1})$.

For sufficiently large fixed $K$, $F_K+H_1H_2$ has a negative one-step drift bounded away from zero off a fixed finite set, uniformly for large $n$. In $CC$, the negative $\kappa_R$ dominates the $O(1/K)$ smoothing error. The only potentially adverse $F_K$ correction occurs at a negative cap when the other player lies within $K+4$ of it. There both are cooperators of depth $n-O(K)$; suppressing the cap player's reward reduces the product drift by order $n$, absorbing the bounded correction. When the other player is farther from a negative cap, the derivative in its smaller coordinate is $-b$, so its reflection helps. In $DD$ and in mixed profiles off the finite set, $\mu<0$ supplies the bound. Averaging the drift over $\pi_n$ gives a positive lower bound for the mass of that fixed finite set, since the drift inside is bounded above independently of $n$. From the set each profile is reachable in bounded time with uniformly positive probability. This proves the second row.

**The crossing $R=1/2,\ T+S=1$.** The unreflected signed difference still has zero drift. Equation (5) bounds the probability of a positive cap by $O(1/n)$, since a defector at that cap has $|Z|\ge n/2-O(1)$ unless both defectors are deep, an exponentially rare event by the minimum-depth bound. Negative caps have probability $O(1/n)$ by level balance. The crossing-term argument with $L_j$ consequently gives $\Pr(Z=j)\le C/n$ uniformly in $j$.

Use the same $H$ as above. For some small $\epsilon\in(0,1)$, consider the increasing, separately concave function

$$
 G_\epsilon(x,y)=\frac{xy}{(x+y)^{1-\epsilon}},\qquad (x,y)=(H_1,H_2).
$$

In $CC$ off a fixed finite set its drift is at most $-c(x+y)^{\epsilon-1}$. To check this, let $r=x+y$. At $\epsilon=0$ the Hessian term for two centered unit-variance increments with covariance $\kappa_R$ is $-(x^2+y^2-2\kappa_Rxy)/r^3\le-c/r$, uniformly on the simplex of directions $x/r+y/r=1$, since $\kappa_R<1$. Strict negativity persists for sufficiently small $\epsilon>0$, with the homogeneous factor $r^{\epsilon-1}$. Extra diagonal variances from a shallow $B$ coin only reduce the term, since both diagonal second derivatives are nonpositive. The Taylor remainder is $O(r^{\epsilon-2})$ by bounded increments. Suppressing deep $C$ rewards at finite caps decreases $G_\epsilon$.

In a mixed profile the $H$-increments are independent, the cooperator's $H$ decreases in mean, and the defector's is harmonic. Applying separate concavity successively and then monotonicity gives nonpositive drift up to $O(n^\epsilon v^{n-1})$ at a deep $D$ cap. In $DD$ the positive drift is at most $C v^{\max(d_1,d_2)-1}$, since $G_\epsilon(x,y)\le \min(x,y)\max(x,y)^\epsilon$ and both factors in this profile stay bounded after one step. Its integral is $O(1/n)$ by $\max(d_1,d_2)\ge|Z|$ and the uniform gap point-mass bound. The fixed exceptional set in $CC$ also has mass $O(1/n)$. Since $r\le 2n+O(1)$, stationary averaging yields $\pi_n(CC)=O(n^{-\epsilon})$. When $\kappa_R<0$, use $H_1H_2$ directly, with its constant negative $CC$ drift, to obtain $O(1/n)$.

For the profile limit set $c_j=\pi_n(CC,\ d_i=j)$. The exact level balance for each player on $C$ reads

$$
 r_{j+1}=\frac S{1-S}r_j+\frac{R-S}{1-S}(c_j+c_{j+1}),\qquad 1\le j<n .
$$

Consequently the stationary probability of a cooperative depth exceeding $m$ is bounded by $C(S/(1-S))^m+C\pi_n(CC)$. The vanishing cooperative mass just proved gives tightness of the smaller signed coordinate $Y$, using also the bound on its positive tail. The critical submartingale $|Z|$ again rules out any invariant probability on the infinite grid. Hence $X\to+\infty$ and $Y\Rightarrow\nu$ by the same finite-support balance test as in (1). This proves the third row.

The remaining competition for **$P<1/2<R,\ T+S>1$** lies between the exponentially stable cooperative profile and the persistent defector. The positive-drift argument above proves a nonempty pinned region adjacent to $R=1/2$. A sharp escape exponent, the exact separating curve for the full region, and behavior on that curve remain open here.

## A correlation endpoint and numerical checks

If $\kappa_R=\kappa_P=1$ for $L$, the diagonal is a closed class. From any symmetric-profile state a sufficiently long run of joint rewards brings both depths to the same cap. From a mixed profile one can prescribe a finite independent-outcome path into a symmetric profile. Hence the unique finite stationary law lives on the diagonal. Its exact cooperative mass is

$$
 \pi_n(CC)=\frac{w_n(R)}{w_n(R)+w_n(P)},\qquad
 w_n(a)=\frac1{1-a}\sum_{j=0}^{n-1}\left(\frac a{1-a}\right)^j .
$$

For $R<1/2$ this tends to $(1-2P)/(2(1-R-P))>1/2$, even if $T+S\ge1$. For $R=1/2>P$, $1-\pi_n(CC)\sim[2(1-2P)n]^{-1}$. This endpoint shows why a full-support assumption matters for the weak-reward result.

The following stationary values use the subtraction-free finite-chain solver with 70 decimal digits. Here $R=.40,\ P=.30,\ S=.25$. The threshold is $T=.75$, and the limiting critical and supercritical $DD$ probability is $5/9$.

| $T$ | Tactic, $(\kappa_R,\kappa_P)$ | $\pi_{16}(CC)$ | $\pi_{48}(CC)$ | $\pi_{48}(DD)$ | $\mathbb E_{\pi_{48}}\lvert Z\rvert/48$ |
|---:|---|---:|---:|---:|---:|
| .60 | $L,(0,0)$ | .061578781 | .059549305 | .454753442 | .105079517 |
| .75 | $L,(0,0)$ | .010681181 | .003635656 | .545196641 | .508240360 |
| .75 | $B,(.25,-.20)$ | .012875590 | .004504359 | .541492605 | .520599320 |
| .95 | $L,(0,0)$ | .000669403 | .000005151 | .555505020 | .889513294 |

At criticality the respective $L,B$ probabilities $\Pr(|Z|/48\le1/4)$ are .252787999 and .247293978. For (7), the independent $L$ game $(.60,.30,.70,.20)$ gives outside masses $2.530306100\,10^{-4}$ and $4.543273469\,10^{-7}$ at $n=32,48$. The independent $B$ game $(.65,.50,.90,.20)$ gives $2.562293712\,10^{-4}$ and $4.489031812\,10^{-8}$ at the same depths.

In the independent $L$ window $T_n=.75+a/n$, $k=10a/9$. For $a=-1,+1$ the measured mean scaled gaps at $n=48$ are .41211834 and .59848221, with exact limits .40925828 and .59074172. The independent reversal example $(.45,.20,.95,.10)$ gives $\pi_{64}(CC)$ equal to .00003355710, .00067773828, .9954778099, .9909530628 for $L,B,D,K$, respectively.

On the fair-$R$ face with $P=.30,\ S=.25,\ T=.60,\ \kappa_P=0$, the $L$ values of $\pi_{48}(CC)$ are .08933104, .22316489, .46507829 for $\kappa_R=-.65,0,.65$. The latter two converge to one, and the proof allows slow convergence at zero. Holding everything else fixed and taking $T=.75$ gives .00417031, .01379918, .05193589 at $n=48$, all with limit zero.

~~~bash
python3 experiments/phase1_weak_rewards.py --depths 8 16 32 48 --digits 70
~~~
