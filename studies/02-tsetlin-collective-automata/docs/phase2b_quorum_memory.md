# The quorum fund after one more unit of memory

In the one-quarter public good, the efficient fund share rises from $3/5$ at depth one to $0.814359353944898165\ldots$ at depth two and $0.8862545035778\ldots$ at depth three. These three numbers are limits of actual finite-population welfare maximizers. The pivotal Nash share $43/60$ lies strictly between the first two. At **every** depth $n\ge2$, shares at or below $43/60$ have no productive mean-field fixed point and incur a positive stationary welfare gap uniform in population size. At depth two a certified orbit at share $7/10$ supplies the good every third round. At depth three, stationary provision vanishes throughout the below-Nash range as the population grows.

For greater depths the exact quota-balance shares approach full pooling at rate $1/n$. Every fixed partial share eventually loses the quorum as the population limit is followed by the deep-memory limit. At $n\ge4$, their interpretation as limits of finite-population maximizers requires an additional selection theorem. All population limits below fix the memory depth first. The original depth-one welfare theorem and the finite-$N$ Nash calculation are in the [partial pooling study](phase1_pooling.md).

## The exact quota equation

Use $0<c<L<H<1$, $0<\theta<1/2$, fund share $0\le\alpha\le1$, population fraction $x$, and base $t=L$ for $x<\theta$, $t=H$ for $x\ge\theta$. Independent agents update synchronously. The depth runs from 1 at the switching boundary to $n$ at the reflecting end. A loss at depth one switches roles with probability $\nu=1$ for the linear automaton and $\nu=1/2$ for the randomized-boundary automaton. The probabilities of a win are

$$
p_D=t-c\alpha x,\qquad p_C=p_D-d,\qquad d=c(1-\alpha).
$$

For fixed payoffs write $q_i=1-p_i$, $r_i=p_i/q_i$, and

$$
h_n(p)=\frac1{1-p}\sum_{j=0}^{n-1}\left(\frac p{1-p}\right)^j,\qquad
F_n(p_C,p_D)=\frac{h_n(p_C)}{h_n(p_C)+h_n(p_D)}.
$$

Detailed balance gives mass proportional to $r_i^{j-1}/q_i$ at depth $j$ of role $i$. The two boundary fluxes agree because each equals the common normalization times $\nu$. Thus both architectures give $F_n$. Dividing the role mass by its outward flux gives the mean length $h_n(p_i)/\nu$ of an episode started at the switching boundary.

A mean-field state is a probability row vector $\mu$ on the $2n$ internal states, $x=\mu{\bf1}_C$. Write $K_t(x,\alpha)$ for the one-agent transition matrix. The update is $\mu\mapsto\mu K_{t(x)}(x,\alpha)$. A fixed point of a smooth branch is exactly a solution to $x=F_n(p_C^t(x),p_D^t(x))$ with the depth distribution just calculated. The physical branch also requires the specified quorum inequality. The scalar equation describes equilibria. The vector update determines their stability.

Set $p_*=H-c\theta$, $r_\theta=(1-\theta)/\theta$. The precise efficient-quorum test is

$$
R_n(d)=\frac{h_n(p_*+\theta d)}{h_n(p_*-(1-\theta)d)}=r_\theta,\qquad
A_n=1-d_n/c. \tag{1}
$$

For each $n$, $R_n$ increases strictly from 1 as $d$ increases. There is one feasible solution $d_n\in(0,c]$ exactly when $R_n(c)\ge r_\theta$. Otherwise the productive response at the quota already exceeds $\theta$ for all shares. Equation (1) is an exact algebraic specification for rational inputs. With $S_n(p,q)=\sum_{j=0}^{n-1}p^jq^{n-1-j}$, its polynomial is

$$
(1-\theta)q_D^n S_n(p_C,q_C)-\theta q_C^n S_n(p_D,q_D)=0.
$$

At fixed $d>0$, $R_{n+1}(d)>R_n(d)$ because $h_{n+1}(p)/h_n(p)=1+1/\sum_{k=1}^n r^{-k}$ increases strictly with $p$. Consequently the feasible shares $A_n$ increase strictly with $n$. For a limiting pivotal Nash share $a=1-(H-L)/c\in(0,1)$, the first depth requiring at least $a$ is exactly $\min\{n:R_n(H-L)\ge r_\theta\}$, with infinity for an empty set. A strict inequality gives a strict crossover. For $p_*>1/2$ and $H>L$ the set is nonempty.

## The benchmark and the large-depth law

Here $(L,H,c,\theta)=(4/5,97/100,3/5,1/4)$. Write $A_{n,L}$ for the continuation of the low branch to $x=\theta$. The equality state itself uses $H$. At $a=43/60$, the productive loss probabilities at the quota are $q_D=55/400$ and $q_C=123/400$. Since $h_1=1/q$ and $h_2=1/q^2$, the ratios in (1) are $123/55<3<(123/55)^2$. Thus **the exact critical depth is two**. In particular,

$$
A_1=\frac35,\qquad
A_2=\frac{c-(\sqrt3-1)(1-H)}
           {c[1+\theta(\sqrt3-1)]}=\frac{11-4\sqrt3}{5}.
$$

| Depth $n$ | Low-branch quota share | Productive quota share $A_n$ | $n(1-A_n)$ |
|---:|---:|---:|---:|
| 1 | .2222222222 | .6000000000 | .4000000000 |
| 2 | .6390320771 | .8143593539 | .3712812921 |
| 3 | .7769191184 | .8862545036 | .3412364893 |
| 4 | .8436633571 | .9194048535 | .3223805858 |
| 5 | .8819345294 | .9378593254 | .3107033732 |
| 6 | .9062040151 | .9494831501 | .3031010993 |
| 7 | .9226936495 | .9574493354 | .2978546521 |
| 8 | .9344886485 | .9632447248 | .2940422020 |
| 32 | .9862870736 | .9913822381 | .2757683812 |
| 1024 | .9995925694 | .9997359113 | .2704268736 |

**Large-depth theorem.** If $p_*>1/2$, then

$$
1-A_n\sim\frac{p_*(1-p_*)}{c\,n}\log\frac{1-\theta}{\theta}.
\tag{2}
$$

For $p\ne1/2$, $h_n(p)=(r^n-1)/(2p-1)$, with $h_n(1/2)=2n$. Put $d=y/n$ in (1). On bounded positive $y$-intervals both payoffs approach $p_*$. Expand $\log r$, whose derivative is $1/[p(1-p)]$. The $r^{-n}$ errors vanish exponentially and the ratio of $2p-1$ factors tends to one. Hence $R_n(y/n)\to\exp[y/\{p_*(1-p_*)\}]$. Bracketing the unique solution by two fixed $y$'s proves (2). The benchmark coefficient is $(123/500)\log3=0.27025862301235498408323032828294132334\ldots$. The fully pooled success probability at the quota is $0.82$.

At $p_*=1/2$, $nd_n\to y>0$, where $e^{4\theta y}+e^{-4(1-\theta)y}=2$. Indeed $h_n(1/2+b/n)/(2n)\to(e^{4b}-1)/(4b)$ with the continuous value at zero. The limiting response ratio increases strictly from 1 to infinity. For $p_*<1/2$, put $d_*=(1-2\theta)(1-2p_*)/[4\theta(1-\theta)]$. If $d_*<c$, then $p_*+\theta d_*<1/2$, and on a feasible neighborhood of $d_*$ both durations converge exponentially to $1/(1-2p)$. The limiting ratio has positive derivative and equals $r_\theta$ at $d_*$, so solutions eventually exist and $d_n=d_*+O(\lambda^n)$ for some $\lambda<1$. If $d_*\ge c$, both actual payoffs at $c$ are below $1/2$. Substituting the limiting durations there gives a ratio at most $r_\theta$, so the finite ratios at $c$ stay strictly smaller by depth monotonicity. Thus the efficient quota can be unattainable even at zero sharing.

## Stationarity and the exact loss of below-Nash efficiency

Assume $M=H-c\theta>L$, and let $W_N(\alpha)$ be stationary mean welfare $E[t(X)-cX]$. At finite $N$ the labeled chain is irreducible and aperiodic. Each agent can reach deepest $C$, hold there, and move to any prescribed state. Conditional independence and interior probabilities give each coordinated finite path positive probability. The stationary law and welfare depend continuously on $\alpha$.

If $W_{N_j}(\alpha_j)\to M$, the profilewise welfare gaps $M-L+cX$ below quota and $c(X-\theta)$ above it imply $P(X<\theta)\to0$ and $X\to\theta$ in probability. For any subsequence $\alpha_j\to a$, the stationary empirical depth vector $Y$ satisfies $E Y=E[Y K_{t(X)}(X,\alpha_j)]$. Along a further subsequence $E Y\to m$, boundedness and continuity of the productive kernel give $m=mK_H(\theta,a)$ and $m{\bf1}_C=\theta$. The unique frozen stationary law forces $a=A_n$. This argument applies to arbitrary stationary laws along the population sequence without assuming convergence of deterministic trajectories.

There is also an explicit positive lower bound at every population size. Fix $n\ge2,\ \alpha\le43/60$. At the quota both $F_n\le F_2$ and the response increases in $\alpha$, hence
$\theta-F_n\ge 3027/36308$. Write $g=M-L=.02,\ \Delta=H-L=.17,\ m=2n-1,\ B=m(200/3)^m$. Then

$$
M-W_N(\alpha)\ \ge\
\frac{3027/36308}{(1+c\alpha B)(1/c+\theta/g)+\Delta B/g}>0. \tag{3}
$$

For the frozen one-agent kernel $K=K_H(\theta,\alpha)$, from every state follow the path left to deepest $C$ and hold there to fill $m$ steps. Its probability is at least $(3/200)^m$. The resulting total-variation contraction yields a solution of $(I-K)u={\bf1}_C-F_n$ with $\operatorname{osc}(u)\le B$, by summing $K^j({\bf1}_C-F_n)$. Changing a row's win probability by $\epsilon$ changes its expectation of $u$ by at most $|\epsilon|B$. Consequently
$$
|\theta-F_n|\le(1+c\alpha B)E|X-\theta|+\Delta B\,P(X<\theta).
$$
For $\rho=M-W_N$, the welfare gaps give $P(X<\theta)\le\rho/g$ and $E|X-\theta|\le(1/c+\theta/g)\rho$, proving (3).

The benchmark also excludes **every productive fixed point** at or below Nash. At $a=43/60$, write $k=ca,\ d=c-k,\ y=(1-H+kx)/d$. The depth-two high response is $y^2/[y^2+(1+y)^2]$. Its derivative in $x$ is $(k/d)v/(1+v)^2$, $v=2y(1+y)$, bounded by $43/68<1$. The response is already below $\theta$ at the quota. At any $\alpha\le a$, any $x\ge\theta$ and any $n\ge2$, its value can only decrease by the two monotonicities above. The depth-one population attains its efficiency bound below Nash, with limiting maximizer $3/5$.

## Can the low and high fixed points coexist?

Let $B_n=A_{n,L}$ be the low-branch crossing in the table. For the benchmark there is exactly one low fixed point for $\alpha<B_n$, **no physical fixed point for $B_n\le\alpha<A_n$**, and exactly one productive fixed point for $\alpha\ge A_n$. This classification holds at every depth. For other payoffs two stable fixed points can coexist, as the rational example below shows.

Let $f=\log h_n,\ g=f'$, $q=1-p,\ r=p/q$, and let $J\in\{0,\ldots,n-1\}$ have probabilities proportional to $r^j$. Write $M_J=EJ,\ V_J=\operatorname{Var}J$. Direct differentiation gives

$$
g=\frac{M_J+p}{pq},\qquad
(pq)^2g'=V_J+(2p-1)M_J+p^2.
$$

In particular $f$ is strictly convex. For $p<1/2$, write $J$ as a sum of nested tail indicators. Their covariances are nonnegative, and summing their variances gives $V_J\ge P(J=0)M_J\ge(1-r)M_J\ge(1-2p)M_J$. Convexity shows that at a fixed $d>0$, $F_n(p_D-d,p_D)$ decreases strictly in $p_D$, and hence in the base $t$.

At any productive root $x$ with $n\ge2,\ \alpha<1$, $1/4\le x<1/2$ and $F_n\le F_2$ give
$$
q_C\le q_D\sqrt{(1-x)/x}
\le .03\sqrt3+.6\sqrt{x(1-x)}<.36 .
$$
On $p\ge16/25$ one has $qg'/g\le6/5$. To verify this for $n\ge11$, the reversed variable $n-1-J$ is a truncated geometric with ratio $q/p$. Its mean is at most $q/(2p-1)$, since truncation is conditioning below a cutoff. Its variance, obtained by differentiating its finite geometric sum, is at most $pq/(2p-1)^2$. Thus $M_J\ge61/7>400/49\ge p/(2p-1)^2$, $V_J\le qM_J$, and the derivative formula gives $qg'/g\le1$. For the remaining ten integers set $G=\sum_{j=0}^{n-1}r^j,\ U=G+(1+r)G'$ with primes in $r$. The bound $qg'/g\le6/5$ is equivalent to
$$
UG+5(1+r)(UG'-U'G)\ge0 .
$$
Expansion at $r=16/9+z$ has only positive coefficients, with minimum coefficient exactly $n$ for each $1\le n\le10$. The script verifies these finite rational expansions.

At a root, differentiating the branch response $F(x)$ and integrating $g'$ between $p_C$ and $p_D$ now gives

$$
F'(x)=c\alpha x(1-x)[g(p_D)-g(p_C)]
\le\frac65\,\frac{c\alpha x}{q_D}(1-x)\log\frac{1-x}{x}
<\frac9{10}\log3<1.
$$

Every productive root is a strict downward crossing of $F(x)-x$. Since $F(1/2)<1/2$, it exists uniquely exactly when $F(\theta)\ge\theta$. The depth-one claim follows directly from its scalar quadratic, and $\alpha=1$ gives $F\equiv1/2$. When the high root exists, $p_D^H(\theta)\ge H-c\theta>L\ge p_D^L(x)$ for $x<\theta$. Strict log convexity then gives $F_L(x)>F_H(\theta)\ge\theta$ for $\alpha<1$, excluding a low root. Stability of the full vector update is addressed separately below.

**Low-branch classification.** At a low root $x\le1/4$ one has $13/20\le p_D\le4/5$. If $p_C\ge4/7$, then $qg'/g\le2$ throughout the payoff interval. For $n\ge32$ the same geometric variance bound gives $M_J\ge n-4\ge28\ge p/(2p-1)^2$. For $n\le31$ the preceding polynomial certificate uses factor 1 in place of 5 and offset $r=4/3$. All shifted coefficients have minimum $n$. As above, $F'_L(x)\le 2c\alpha x(1-x)\log((1-x)/x)/(.20+c\alpha x)<1$. Indeed putting $w=(1-x)/x$ and using $c\alpha\le.60$, the strict inequality follows from $6w\log w<w^2+5w+4$, by the tangent bound for $\log$ at 6 and $6\log6<11$.

If $p_C<4/7$ and $n\ge17$, then $g(p_D)\le25n/4$ and
$$
F'_L(x)\le\frac{15n}{4}\,\frac{21}{5}\,
       \frac{(28/39)^n}{1-(7/13)^n}<1.
$$
Here $x\le h_n(4/7)/h_n(p_D)$ and the geometric sums give the ratio on the right. The bound decreases from less than $.958$ at $n=17$. For $1\le n\le16$, divide $[1/5,4/7]\times[13/20,4/5]$ into $5\times5$ equal rectangles $[u,v]\times[y,z]$. On each put $R=h_n(v)/h_n(y)<1$. Since $k=c-(p_D-p_C)$, convexity and the increasing function $R/(1+R)^2$ on $[0,1]$ bound the slope by $(c-y+v)R[g(z)-g(u)]/(1+R)^2$. The maximum of the 400 exact rational bounds is less than $22/25$.

Thus every low root crosses downward as well. Its continuation satisfies $F_L(0)>0$ and has exactly one root in $[0,\theta)$ iff $F_L(\theta)<\theta$. At zero sharing the low quota ratio is already $4^n>3$, whereas at full sharing both branches give $1/2$. Strict log convexity orders the responses, giving $0<B_n<A_n<1$. Equality at $B_n$ cannot be a low root because the quota itself takes the high branch.

**A genuine bistable game.** Take $n=2,\ c=1/2,\ \alpha=333/400,\ \theta=1/200,\ L=303733/304760,\ H=1999/2000$. Substitution gives physical equilibria $x_L=1/401<\theta$ and $x_H=1/5>\theta$. For either branch put $k=c\alpha,\ q=1-p_D,\ r=1-p_C$. In the two-step recurrence below the characteristic polynomial is $\lambda^2-A\lambda-B$, where
$$
A=1+\nu[k(q(1-x)-rx)-q-r],\qquad
B=\nu[q(1-q+k(1-x))+r(1-r-kx)].
$$
Both $A,B>0$, and $1-A-B$ is $\nu\cdot399664849/92647040000$ on the low root and $\nu\cdot22981/3200000$ on the high root. Hence both roots are locally attracting, for each of the two switch rules. Their strict branch inequalities and nonsingular fixed-point derivatives give coexistence on an open parameter neighborhood.

## The actual depth-two welfare optimizer

For the benchmark, both architectures satisfy

$$
\lim_{N\to\infty}\max_{\alpha\in[0,1]}W_N(\alpha)=.82,\qquad
\alpha_N^{\rm opt}\longrightarrow A_2,\qquad
W_N(A_2)\longrightarrow .82. \tag{4}
$$

For $A_2<\alpha\le.82$, every mean-field trajectory converges to the unique productive equilibrium $x_\alpha>\theta$ and the stationary finite-population fraction concentrates there as $N\to\infty$.

**Reduction to two successive fractions.** Let $k=c\alpha,\ d=c-k,\ q_t(x)=1-t+kx$. After a round with fraction $y$ and base $s$, the two deep masses equal $p_C^s(y)y$ and $p_D^s(y)(1-y)$. The next round's current fraction $x$ and base $t$ therefore give the recurrence

$$
G_{st}(y,x)=x+\nu\big[q_t(x)\{1-x-p_D^s(y)(1-y)\}
 -(q_t(x)+d)\{x-p_C^s(y)y\}\big]. \tag{5}
$$

It applies from the second step for every starting distribution. At finite $N$, each deep mass and the next fraction differ from their respective conditional means by at most $u$, except with probability at most $6e^{-2Nu^2}$, by Hoeffding and a union bound. The resulting error in (5) is at most $3u$. This bound holds uniformly over each fixed time horizon after a union bound over time.

**Global entrance certificate.** For $.81\le\alpha\le.82$, partition $[0,1]^2$ into $100^2$ squares with the threshold on a grid line. The exact rational calculation encloses $G_{st}(I,J)+[-10^{-4},10^{-4}]$ on each square, independently allowing $k\in[.486,.492]$. It retains every possible next square, always using $H$ at the threshold itself. Images of the full grid are nested. After 14 steps the linear rule's 101 remaining squares lie in $[.24,.44]^2$. After 26 steps the randomized-boundary rule's 75 remaining squares lie in $[.24,.47]^2$. Thus the larger square traps both subsequent trajectories and their sufficiently small step perturbations.

On that square the partial derivatives of (5) in $y,x$ satisfy $G_y>0,\ G_x>1/10$ on each branch extension used here. For a low current base the $x$ domain stops at $\theta$. These inequalities are certified by substitution of rational intervals in

$$
\begin{aligned}
G_y/\nu&=q_t(x)(s+k-2ky)+(q_t(x)+d)(s-d-2ky),\\
G_x&=1+\nu\{k[1-4x-(s-ky)(1-2y)-dy]-2(1-t)-d\}.
\end{aligned}
$$

Writing $a=q_s(z), b=q_t(z)$, the diagonal drift is
$\nu[(1-z)ab-z(a+d)(b+d)]$. Both partial derivatives of the bracket in $a,b$ exceed $3/100$ for $.24\le z\le.26$, since they are at least $(1-2z)(1-H+kz)-dz$. In particular $G_{st}(z,z)\ge G_{HH}(z,z)$ there. Throughout $[.24,.47]$ the frozen high response has $F'<3/5,\ F(.47)<.34$. These rational endpoint bounds follow from the formula $F'=(k/d)v/(1+v)^2$ above with $v>1$. The diagonal high drift has the sign of $F(z)-z$.

For fixed $A_2<\alpha\le.82$, take $\theta<\ell<\min(.26,x_\alpha)$. On $[.24,\ell]$, $G_{HH}(z,z)-z$ has a positive minimum $b$. Whenever both coordinates exceed $z$ in this interval, monotonicity on the required smooth extensions gives next coordinate at least $z+b$. Errors bounded by $b/2$ raise the lower bound on the pair by $b/2$ every two rounds up to $\ell$, and preserve it afterwards. Both coordinates are then productive. On $[\ell,.47]^2$ the order-preserving update $(y,x)\mapsto(x,G_{HH}(y,x))$ has monotone bounding trajectories from its lower and upper corners. Their limits are fixed points and both must be $(x_\alpha,x_\alpha)$. Reaching any prescribed accuracy thus takes uniformly bounded time. Continuity of this finite iterate and the preceding finite-time error bound imply stationary concentration at $x_\alpha$. Taking fixed shares down to $A_2$ proves the supremum in (4), and the necessary stationary balance gives the limit of every maximizing sequence.

**At the critical share.** The welfare loss and probability of a missed quorum both have sharp order
$$
P_{\rm stat}(X<\theta)\asymp .82-W_N(A_2)\asymp 1/\log N.
$$
Write $Z_j=(X_{j-1},X_j)$, $V_j=\|Z_j-(\theta,\theta)\|_\infty$, and $e_{j+1}=X_{j+1}-G_{st}(Z_j)$. The two realized deep masses at $j$ differ from their formulas in (5) by errors $D_j^C,D_j^D$. From the independent bounded draws and (5),
$$
E(|e_{j+1}|+|D_j^C|+|D_j^D|)=O(N^{-1/2}),\qquad
P(|e_{j+1}|>u)\le6e^{-bNu^2}.
$$
These bounds are uniform in the microscopic initial condition after the first step. The true conditional mean of $X_{j+1}$ differs from $G_{st}(Z_j)$ by at most $|D_j^C|+|D_j^D|$.

At $\alpha=A_2$ the preceding finite-time lower-bound argument reaches any fixed $\theta-\delta$ close to $\theta$. In stationarity $Z_j$ is outside $[\theta-\delta,.47]^2$ with probability $O_\delta(e^{-b_\delta N})$. At $(\theta,\theta)$, both $G_{HL}$ and $G_{LH}$ exceed $\theta$ by $\nu(H-L)[(1-2\theta)q_H(\theta)-d\theta]>0$, and $G_{LL}\ge G_{HL}$. By continuity and positive partial derivatives, one low round in this square therefore pushes the next two fractions above $\theta+\eta$ for some fixed $\delta,\eta>0$ and sufficiently small errors. On subsequent all-high rounds $G_{HH}(y,x)-\theta\ge(x-\theta)/10$ for $y,x\ge\theta$ in the square. For $T=\lfloor\log N/(4\log10)\rfloor$ steps the gap remains positive when all errors are $\le N^{-1/3}$, since $\eta\,10^{-j}-N^{-1/3}/(1-1/10)>0$ through that window. A union bound makes exceptions exponentially small in $N^{1/3}$ up to the factor $T$. The events “low now and high for the next $T$ rounds” at times $0,\ldots,T$ are disjoint. Stationarity yields the upper bound $P(X<\theta)=O(1/\log N)$.

Conversely, the sum of the two positive partial derivatives of $G_{HH}$ at $(\theta,\theta)$ is $1+\nu[q^2+(q+d)^2]\bigl(F'(\theta)-1\bigr)<1$, where $q=q_H(\theta)$. In a fixed neighborhood two all-high updates thus satisfy $V_{j+2}\le r V_j+|e_{j+1}|+|e_{j+2}|$ for some $r<1$. On an all-high window, the grid followed by monotone squeezing from $(.47,.47)$ brings every trajectory into a smaller such neighborhood in a fixed time $J$, allowing uniformly small errors. The contraction keeps it there while those errors stay small. On a window of $t=J+2m=O(\log N)$ steps with $r^m\le N^{-1/2}$, a fixed-size error has probability $O(t e^{-bN})$. Hence, writing $E_t$ for an entirely productive window, iteration and the unconditional first-moment error bound give $E[V_t{\bf1}_{E_t}]=O(N^{-1/2})$.

If $P(E_t)<1/2$, a miss has already occurred with probability at least $1/2$. Otherwise with probability at least $1/4$ the window is productive and $V_t+|D_t^C|+|D_t^D|\le B/\sqrt N$ for a fixed $B$, by Markov's inequality. Here the next conditional mean is within $O(B/\sqrt N)$ of the quota, and the defector boundary mass approaches $q(1-\theta)>0$. The next count is a sum of independent Bernoulli variables conditionally on the microscopic state. A positive fraction flip with probability $\nu q_H(X_t)$ bounded away from zero and one. Conditional variance is thus $\Omega(N)$, and the bounded-summand Berry–Esseen estimate gives a positive lower bound for missing the strict integer quota. A miss consequently has probability bounded below in an $O(\log N)$ window from any initial state. The stationary union bound gives the reverse order.

Finally the local two-step contraction applies except with probability $O(P(X<\theta)+e^{-bN})$, since it suffices that a fixed preceding window and the next two updates are all high with small errors. Boundedness and stationarity then give $(1-r)E V_j=O(P(X<\theta)+N^{-1/2})$. A low round costs at least .02 and the mean welfare deficit is at most $(H-L)P(X<\theta)+cE V_j$, proving the welfare order.

The critical mean-field fixed point is **globally attracting and Lyapunov unstable**. Every trajectory enters $[\theta-\delta,.47]^2$. A subsequent low round resets two consecutive fractions strictly above $\theta$. From two high fractions, order preservation and $G_{HH}(\theta,\theta)=\theta$ keep the trajectory in $[\theta,.47]^2$, where the high-branch squeeze converges to $(\theta,\theta)$. If there are no more low rounds, that same squeeze applies directly. The depth masses follow from (5). Yet perturbing the physical fixed distribution arbitrarily little to the low side makes its next fraction converge to $G_{HL}(\theta,\theta)>\theta$, a jump of fixed positive size.

**A period of three below Nash.** At depth two and $\alpha=7/10$, both rules have a locally attracting orbit with the following fractions in cyclic order. Its basin includes a relative neighborhood of the orbit in the physical simplex.

| Rule | First low round | Second low round | Productive round |
|---|---:|---:|---:|
| Linear | .2475632256 | .2480136799 | .2592180959 |
| Randomized boundary | .2467642728 | .2448125256 | .2513976015 |

The rational verifier starts (5) on squares of radius $10^{-80}$ around the first two coordinates. It checks the three strict branch inequalities and positivity of the reconstructed boundary masses at each step. The product of the three interval Jacobians gives return-map infinity norm $<18/25$ for the linear rule and $<17/20$ for the randomized boundary. The center returns within $10^{-83}$. The contraction theorem therefore produces a physical periodic orbit, and the itinerary forces least period three. At this share $F'_{2,t}\le7/12$ in either continuation and $F_{2,L}(\theta)>\theta>F_{2,H}(\theta)$, so the piecewise mean-field dynamics has no fixed point. The certificate proves local attraction of the cycle.

## The actual depth-three welfare optimizer

For $n=3$ both architectures satisfy $W_N(A_3)\to.82$, $\max_\alpha W_N(\alpha)\to.82$, and $\alpha_N^{\rm opt}\to A_3$. At fixed $A_3<\alpha\le.887$ every deterministic trajectory converges to the productive equilibrium and the stationary population concentrates there.

Write $k=c\alpha,\ d=c-k$ and $p=p_D$. On any complete limiting trajectory the comparison proved in the deep-memory section gives $x\le1/2$, even allowing either label at $x=\theta$. Thus throughout the share range $[A_3,.887]$ one has $.0678\le d\le.0684$, $.666\le p\le.838$, and on productive rounds $.703\le p\le.838$. Order the six states $D_3,D_2,D_1,C_1,C_2,C_3$ and let $U_j$ be the mass on states of index at least $j$, indexed from zero. Then $U_0=1,\ U_6=0,\ U_3=x$, and $U'=T(p)U$. Put $q=1-p,\ Q=q+d$. On rows 1 and 2 the two neighboring coefficients are $(q,p)$, on rows 4 and 5 they are $(p-d,Q)$, and row 3 has coefficients $\nu q,1-\nu(q+Q),\nu Q$ on columns 2, 3, 4. All are nonnegative, with fixed exterior rows.

Let $u(p)$ be the frozen stationary tails, and let $Z(p)=-T'(p)u(p)$. Multiplication by a positive normalization gives the vector
$$
\big(0,\ pQ^3,\ qQ^3,\ \nu d q^2Q^2,\ -Qq^3,\ -(p-d)q^3,\ 0\big).
$$
For $p\in[.703,.838]$, every product of the allowed update matrices applied to this vector has **strictly positive central coordinate**. The exact verifier partitions the reference payoff and the gap in steps of $.0001$. It forms a componentwise rational lower bound on each starting vector and checks all endpoint words through length seven using nonnegative matrices. At each multiplication the enclosure allows both ends of the gap cell, uses the smaller row result, and rounds down in units of $10^{-11}$. Affinity in the update payoff covers every intermediate value by convexity. The smallest certified central entries at lengths 0 through 7 are $9396362/10^{11}$ for the linear rule and $4698181/10^{11}$ for the randomized boundary. At length 7 every interior entry is at least $6858693/10^{11}$ or $4067157/10^{11}$, respectively. Further updates preserve strict positivity in every interior row. Integer dot products are bounded by $20000\cdot10^{11}<2^{63}$.

For any fixed reference $p_*$, iteration of
$$
U_{s+1}-u(p_*)=T(p_s)[U_s-u(p_*)]+(p_*-p_s)Z(p_*)
$$
now compares the entire past schedule with the frozen response. The initial term vanishes from the remote past by common-endpoint mixing of the underlying state kernels. If every past $p_s\le p_*$, then $x_t\ge F_3(p_*-d,p_*)$, strictly when any earlier inequality was strict. Reversing the inequalities gives the opposite bound.

Take $p_*=H-k\theta$. This is the maximum possible payoff, and low rounds have $p_s\le L<p_*$. For $\alpha>A_3$ the frozen response already exceeds $\theta$, so every complete trajectory is productive. At $\alpha=A_3$ the frozen response equals $\theta$. A low label would force every later $x_t>\theta$ and so can occur at most once on a complete path. Stationarity then gives zero probability of a low label by summing its marginal probabilities in arbitrarily long windows.

On an all-high complete path set $m=\inf_t x_t,\ M=\sup_t x_t$. The reference payoffs $H-km,H-kM$ lie in the certified interval. The comparisons give $m\ge F_H(m)$ and $M\le F_H(M)$. The unique downward crossing of $F_H(x)-x$ on $[\theta,1/2]$ forces $m=M=x_\alpha$. The depth law is frozen as well by remote-past mixing. Thus every stationary subsequential limit at $A_3$ has $x=\theta$ and supplies the good, proving its efficiency and identifying all optimizing shares. For $\alpha>A_3$ in the specified interval every complete path is this same equilibrium. Shifting a sequence of late deterministic deviations to the origin and taking a compact limit proves global convergence. The finite-$N$ rate at $A_3$ remains open.

## Local stability at every depth

For either benchmark architecture and every $n$, the unique productive equilibrium is **locally attracting for every $\alpha>A_n$**. At $\alpha=A_n$ the smooth productive continuation is locally attracting, while the physical fixed point is Lyapunov unstable. Indeed every nondegenerate quota crossing has $q_D b_D=q_C b_C$ for its shallow masses and $q_C>q_D$, hence $b_D>b_C$. An arbitrarily small perturbation to $x<\theta$ makes the next fraction tend to $\theta+\nu(H-L)(b_D-b_C)>\theta$. The smooth-branch stability proof checks the full $(2n-1)$-dimensional tangent dynamics.

Order the internal states $D_n,\ldots,D_1,C_1,\ldots,C_n$. Use cumulative masses to the right of each of the $2n-1$ intervening cuts. Cut $0$ is the action boundary, with coordinate $x$. Cut $(s,j)$ is $j=1,\ldots,n-1$ levels into flank $s\in\{C,D\}$. At a fixed productive payoff define $p_s,\ q_s=1-p_s,\ t_s=q_s/p_s,\ x_C=x,\ x_D=1-x$, and let $b_s$ be the stationary mass of the shallowest state of role $s$. Write $k=c\alpha$. In these coordinates the Jacobian is $J=A+v e_0^\top$. A frozen flank row of $A$ moves toward the central cut with weight $p_s$, away with $q_s$, and loses its exterior term at the far endpoint. The central row assigns weights $\nu q_D,\nu q_C$ to its neighbors and keeps $1-\nu(q_D+q_C)$. Differentiating the probability flux across each cut gives
$$
v_0=\nu k(b_D-b_C),\qquad
v_{s,j}=\sigma_s k b_s(p_s/q_s)^{j-1}/q_s,\qquad
\sigma_D=1,\ \sigma_C=-1.
$$
The frozen cut matrix is substochastic with spectral radius below one by endpoint killing. Its reversible weights are $m_0=1,\ m_{s,j}=\nu t_s^j$. Conjugation by $\operatorname{diag}(\sqrt m)$ makes $A$ symmetric, and the perturbation has squared operator norm
$$
\delta^2=v_0^2+\nu k^2\sum_s b_s(x_s-b_s)/p_s^2 .
$$
The variational test vector $\sqrt m$ lower-bounds the largest frozen eigenvalue by $1-\nu\sum_s q_s t_s^{n-1}/\sum m$. Deleting the center gives two Dirichlet paths, so interlacing bounds the second eigenvalue above by $2\sqrt{p_Cq_C}\cos(\pi/n)$. The smallest eigenvalue is at least $-2\sqrt{p_Cq_C}\cos(\pi/(2n))$ by comparison with the path of $2n-1$ cuts with maximum off-diagonal weight. Here $p_D\ge p_C\ge16/25$ and the central diagonal is nonnegative.

For $n\ge16$, $b_s\le x_s(9/16)^{n-1}$ gives $\delta^2\le\bigl[.36+(.60/.64)^2\bigr]\,(9/16)^{n-1}$, hence $\delta<.015$. The top frozen eigenvalue is at least $1-.72(9/16)^{n-1}$. All others lie in $[-.96,.96]$. The symmetric resolvent bound places each perturbed eigenvalue within $\delta$ of a frozen eigenvalue. Along the linear perturbation from 0 to $v$ the top disk stays disjoint. It contains one real eigenvalue by continuity and complex conjugacy. The others have modulus $<.975$. The determinant lemma gives
$$
\det(I-J)=\det(I-A)(1-F'_H(x))>0 .
$$
Indeed differentiating the stationary cut equations with respect to the exogenous fraction gives $(I-A)^{-1}v$, whose central coordinate is $F'_H(x)$. The strict scalar bound proved above places the remaining real eigenvalue below one. At $\alpha=1,\ x=1/2$, the response is constant and the same identity applies.

For $2\le n\le15$ the exact interval verifier covers $1/4\le x\le1/2$, including both switching probabilities. The implicit productive curve has $d'(x)=-c(1-F'_H)/(\partial_\alpha F_H)<0$, so endpoint bisections at rational values of $x$ enclose the gaps on each subinterval. The same spectral bounds separate the top eigenvalue on most boxes. On the remaining boxes the verifier brackets all $2n-1$ roots by strict real characteristic-polynomial signs on $\{-1,-47/48,\ldots,47/48,1\}$, using the positive determinant at 1. It evaluates the determinant by eliminating the two tridiagonal flanks: a leading minor of size $j$ is $D_0=1,\ D_1=z,\ D_j=zD_{j-1}-p_sq_sD_{j-2}$; the central column consists of the frozen coupling and the displayed $v_{s,j}$. All arithmetic uses exact rational endpoints and outward-rounded square roots. At most six dyadic subdivisions suffice; the depth-one scalar proof covers the remaining case. [All-depth stability verifier](../experiments/phase2b_quorum_stability.py)

**Low equilibria.** The low fixed point is also locally attracting whenever $\alpha<B_n$. Its central frozen diagonal is nonnegative since $p_C+p_D=1+k(1-2x)\ge1$. The preceding weighted perturbation formula applies with either payoff potentially giving the larger $p_sq_s$. Here $b_C/b_D=q_D/q_C\le1$, $b_D\le(7/13)^{n-1}$, and $p_C\ge1/5$. Hence $\delta\le\sqrt{.36+9}(7/13)^{(n-1)/2}<1/(2n^2)$ for $n\ge29$ (check $n=29$ and the ratio of consecutive bounds). The Dirichlet estimates give $\lambda_2\le\cos(\pi/n)\le1-2/n^2$ and $\lambda_{\min}\ge-\cos(\pi/(2n))\ge-1+1/(2n^2)$. If $\lambda_1\le1-\delta$, all perturbation disks lie in the closed unit disk and only $+1$ can touch the circle. The positive determinant excludes that point. Otherwise $\lambda_1>1-\delta>\lambda_2+2\delta$ and the isolated real eigenvalue argument applies.

For $2\le n\le28$ the exact verifier subdivides $k\in[0,c]$. The physical root increases with $k$ by its downward crossing and positive share derivative. The function extended by clipping at $\theta$ therefore has interval enclosures from endpoint bisections. Entirely clipped subintervals may be discarded. The same disk tests use $\max_s p_sq_s$ over both flanks, with the additional sufficient bound $3\delta+\lambda_2^{\rm upper}<1$ together with the lower spectral bound. Remaining boxes use the same real-polynomial sign test. The saved low-branch cover has 251 disk certificates and 93 polynomial certificates, reaching dyadic subdivision depth 13. These are local stability results for the strict branches. Global attraction through the whole share range would be a stronger statement.

**Direct checks at the quota.** At $x=\theta,\ \alpha=A_n$, write $K=K_H(\theta,A_n)$, let $\pi$ be the frozen law, and drop the last (deepest $D$) mass from simplex coordinates in the original deepest-$C$-first order. The productive continuation then has tangent Jacobian
$$
J_{ij}=K_{ji}-K_{2n,i}+{\bf1}_{j\in C}(\pi\,\partial_x K)_i,
\qquad 1\le i,j<2n .
$$
At fixed $\alpha$, $\partial_xK=-c\alpha(K_{\rm win}-K_{\rm loss})$. Outward-rounded interval products give the following upper bounds for $\|J^m\|_\infty$. They certify smooth-branch local attraction and its continuation to productive solutions just above $A_n$. At the threshold a below-quorum perturbation uses the other branch.

| Depth | Linear $(m,\text{bound})$ | Randomized boundary $(m,\text{bound})$ |
|---:|---:|---:|
| 1 | $1,\ .7000000001$ | $1,\ .8500000001$ |
| 2 | $8,\ .9691073998$ | $16,\ .9194814802$ |
| 3 | $128,\ .7582711145$ | $256,\ .6482416022$ |

## Global endpoint behavior and finite-population checks

**Global endpoint behavior at fixed depth.** Order the states from deepest $C$ to deepest $D$. A constant nearest-neighbor kernel with probabilities $p_C,p_D$ is stochastically monotone in this order when $\nu(q_C+q_D)\le1$, by comparing adjacent rows. At $\alpha=0$, the kernel with $p_C=.37,\ p_D=.80$ bounds every agent on the cooperative side in either branch. Starting the comparison agents at deepest $C$ and using independent common uniforms gives an independent upper population. Its limiting fraction satisfies $F_n(.37,.80)\le F_1(.37,.80)=20/83<\theta$. After a fixed number of rounds this bound has a uniform margin from $\theta$. The mean field then stays low and converges to the frozen low law. In finite stationary populations the productive probability is exponentially small in $N$ by a binomial concentration bound, and the limiting welfare is $L-cF_n(L-c,L)=.80-.60/(1+4^n)$.

At $\alpha=1$, the two roles share the same payoff, so every one-step kernel commutes with the reflection $S$ interchanging roles and matching depths. Over $2n-1$ steps any history of such kernels has a common positive deepest-$C$ column, by the uniform path estimate in (3). For a row law $\mu$, the antisymmetric difference $\mu-\mu S$ therefore decays geometrically along every trajectory. Thus $x\to1/2$ uniformly, eventually all steps are productive, and the law converges to the frozen symmetric law $\pi_*$ at $p=H-c/2$. The same block contraction, applied to the law minus $\pi_*$ with vanishing kernel errors, proves this last assertion.

For each fixed $n$ this global convergence extends to an open interval $1-\epsilon_n<\alpha\le1$. Indeed along any trajectory the actual kernel differs rowwise by total variation at most $d=c(1-\alpha)$ from the symmetric kernel with payoff $p_D$. The block contraction bounds the antisymmetric part by a geometrically decaying initial error plus $O_n(d)$. After a uniform burn-in the trajectory is productive and its kernels lie arbitrarily close to the frozen one at $H-c/2$ when $d$ is small. A second block contraction brings it into an arbitrarily small neighborhood of $\pi_*$. At $\alpha=1$ the high-branch Jacobian on the simplex tangent space is block triangular in even and odd perturbations under $S$. Indeed even tangent vectors have zero cooperative-mass variation, and $\pi_*\,\partial_xK$ is even. The two diagonal blocks are restrictions of the primitive frozen kernel and have spectral radii below one. An adapted norm thus gives a common locally invariant contraction neighborhood for nearby $\alpha$, by continuity, and all trajectories enter it. The same finite-block estimates tolerate small per-step errors even at a quorum crossing, since the comparison before productive entry was uniform in the base. Conditional Hoeffding bounds then give stationary convergence at these fixed shares. The size of this stable interval remains open.

### Every fixed partial fund loses the quorum in deep memory

For any compact set $I\subset[0,1)$, there are $C_I<\infty,\ r_I<1$ such that for all sufficiently large $n$
$$
\limsup_{N\to\infty}\sup_{\alpha\in I}
 |W_{N,n}(\alpha)-.80|\le C_I r_I^n .
$$
Full pooling gives limiting fraction $1/2$ and welfare $.67$ at every fixed depth. A productive quota crossing can approach this endpoint along (2).

At fixed $n$ take any subsequential stationary population limit, retaining both the two-sided empirical trajectory $z(t)$ and its branch labels. Compactness and vanishing one-step conditional variances give the exact propagation $z(t+1)=z(t)K_{t(x)}(x,\alpha)$ with either label permitted at equality. For any realized schedule one can construct a tagged Markov path with these marginals and those prescribed, time-dependent matrices.

For every share, $x(t)\le1/2$ on every such path of distributions. For the proof use a comparison chain with both payoffs equal to the actual $p_D(t)$, the original switch $\nu$ at $D_1$, and a smaller switch $\nu/\kappa$ at $C_1$. It bounds the actual chain on the cooperative side. Adjacent-row comparison shows it is monotone if $\nu(1-p_D)(1+1/\kappa)\le1$. Each of these matrices preserves the relation $z_{C,j}=\kappa z_{D,j}$ by the balanced boundary fluxes. Uniform mixing of their products, from the common deepest endpoint, gives $x\le\kappa/(1+\kappa)$ by starting the upper chain in the remote past. Since $p_D\ge.37$, $\kappa=63/37$ first gives $x\le.63$. Consequently $p_D\ge\min(.65,.97-.60\cdot.63)=.592$, and the comparison with $\kappa=1$ gives $x\le1/2$.

For shares below $43/60$ the possible branches now obey
$$
p_C\le u=.37+.45\alpha,\qquad p_D\ge v=.80-.15\alpha .
$$
The constant upper comparison kernel $(u,v)$ is monotone since $u+v\ge1$. Starting in the remote past gives $x\le F_n(u,v)$. Here $u<v,\ v>1/2$, so the bound tends to zero exponentially in $n$, uniformly on compact subintervals below $43/60$.

For $2/3<\alpha<1$ both payoffs belong to $[p_0,1-q_0]$ with $p_0=\min(.20+.45\alpha,.37+.30\alpha)>1/2,\ q_0=.03$, and their gap is $d=.60(1-\alpha)>0$. The following comparison holds for any prescribed two-sided schedule with these bounds. Put $\rho=(1-p_0)/p_0$, and let $J_t$ be distance from deepest confidence. Comparison with the reflected depth walk of constant win probability $p_0$ gives $P(J_t\ge k)\le\rho^k$ from its truncated-geometric equilibrium in the remote past. Hence $|x(t+1)-x(t)|\le\rho^{n-1}$. Let $y(t)$ be the probability that the first deepest visit at or after $t$ lands at $C_n$. Such a visit occurs almost surely by a block of wins. Biased gambler's ruin from $1\le J_t\le m=\lfloor(n-1)/2\rfloor$ bounds the chance of touching the shallow level first by $\rho^{n-1-m}$. Thus $|y(t)-x(t)|\le E_n=2\rho^m$.

For role $i$, starting at $i_n$ at time $t$, let $e_i(t)$ be the probability that the next strictly later deepest visit has the opposite role, and $h_i(t)$ the probability of hitting its shallow level before the first deepest return. Choose $1<\lambda<\min(p_0/(1-p_0),1+d/(1-p_0))$. Modify the scheduled $D$ losses to $q'(s)=\lambda q_D(s)\le q_C(s)$. The new win probability satisfies $1-q'(s)\ge p_D(s)/\lambda$. On every first path to the shallow level, losses outnumber wins by $n-1$. Comparing that path at the same start time under the two schedules gives $h_D(t)\le\lambda^{-(n-1)}h'(t)\le\lambda^{-(n-1)}h_C(t)$, the last inequality by monotone coupling up to hitting either endpoint. At $C_1$ the immediate switch and subsequent ascent to $D_n$ have probability at least $b=\nu q_0(1-\rho)$ by gambler's ruin. Consequently $e_D(t)\le U_n e_C(t)$, $U_n=b^{-1}\lambda^{-(n-1)}$, while $e_C(t)\ge bq_0^{n-1}$ by an initial sequence of losses.

The future deepest label changes its definition between $t$ and $t+1$ only on paths currently at a deepest endpoint. This gives the exact identity
$$
y(t+1)-y(t)=z_{D,n}(t)e_D(t)-z_{C,n}(t)e_C(t).
$$
For $k\le n-2$, requiring $k$ wins from $C$ agents with $J_{t-k}\le k$ gives $z_{C,n}(t)\ge p_0^k[x(t)-k\rho^{n-1}-\rho^{k+1}]$. Let
$$
a_n=k\rho^{n-1}+\rho^{k+1}+2U_n p_0^{-k}.
$$
If $y(t)\ge a_n+E_n$, the identity gives a decrease of at least $U_n bq_0^{n-1}>0$. Its upward increment is always at most $U_n$. A bounded two-sided trajectory therefore satisfies $y(t)\le a_n+E_n+U_n$, since any larger value would force a strictly increasing unbounded sequence backwards. Thus $x(t)\le a_n+2E_n+U_n$. Take $k=\lfloor\eta n\rfloor$ for $0<\eta<\min(1,\log\lambda/|\log p_0|)$ to obtain exponential decay.

The two share ranges overlap. Their estimates are uniform on compact subintervals with the respective strict gaps. For all sufficiently large $n$, every stationary fluid trajectory for $\alpha\in I$ therefore stays a fixed distance below the quorum. Compactness also allows $N$-dependent shares to converge inside $I$. This proves the displayed iterated bound without presupposing an inner stationary limit.

### Finite-population and trajectory checks

**A depth-three cutoff.** For both architectures at $n=3$, the stationary productive probability tends to zero uniformly over every $\alpha\le43/60$. On any complete stationary fluid trajectory, the half-mass bound gives $277/400\le p_D\le97/100,\ p_C\le p_D-17/100$. Dominate each actual step by the ordered comparison kernel with $p_C=p_D-17/100$. In the cumulative tail coordinates above add the fixed exterior tails 1 and 0. The seven-coordinate update has nonnegative entries and is affine in $p_D$. A product of 12 allowed matrices is therefore a convex combination of the $2^{12}$ endpoint products. Start from the all-cooperative tail envelope. After each 12-step block take its componentwise maximum over these products, rounding every individual step upwards in units $10^{-9}$. After 50 blocks of exact integer arithmetic the cooperative component is at most $219568943/10^9$ for the linear rule and $229430952/10^9$ for the randomized boundary, both strictly below $1/4$. Starting 600 steps in the past proves the limiting support bound, including sequences of shares tending to the Nash endpoint. This is stronger than the absence of a productive fixed point at depth two, where the periodic example supplies the good.

At each fixed depth covered by either strict abandonment certificate, the stationary productive probability is in fact $O(e^{-bN})$ for some $b>0$ uniform on its stated compact set of shares. The piecewise update has a closed graph when either branch is allowed at equality. Every complete trajectory of that graph obeys the same comparisons. If no fixed time window with a positive tolerance forced its last fraction below quota, there would be trajectories of increasing duration, with one-step errors tending to zero, ending at or above quota. By diagonal compactness their backward histories and shares have a convergent subsequence. Its limit extends forward to a complete exact trajectory with a productive endpoint, contradicting the strict support bound. The resulting fixed window tolerates small coordinate errors, so conditional Hoeffding and a finite union bound give the asserted exponential estimate.

At the original depth-one efficient share $\alpha=3/5$, the depth-three limiting stationary welfare is **$.73969382168754269496\ldots$**, with $x=.10051029718742884173\ldots$ in either architecture. Indeed the eventual low kernel has $p_C(x)=.56-.36x,\ p_D(x)=.80-.36x$. If every complete low trajectory lies in $[\ell,u]$, monotone frozen comparisons from the remote past tighten the range to
$$
[F_3(p_C(u),p_D(\ell)),\,F_3(p_C(\ell),p_D(u))].
$$
The two comparison kernels are order preserving since $p_C+p_D\ge1.18$. Six outward-rounded iterations from $[0,1/4]$ enter $[.09,.112]$. The two-endpoint update preserves this square and has infinity-norm Lipschitz constant $<4/5$ there. The verifier bounds each gradient row using $F(1-F)\le\sup F$ and $(\log h_3)'=3/(1-p)+(2p-1)/(1-p+p^2)$. Its unique fixed pair has equal endpoints by symmetry. This identifies every stationary fluid limit and gives the displayed welfare.

On the productive side, at depth three and $\alpha=.89$ the unique productive fraction is $0.26374759058233191593718335128653696715\ldots$. In 110-decimal, 50,000-round deterministic runs, all six pure internal starting states for each architecture reached this fraction within $10^{-78}$. The data record the last unproductive round for each start. These twelve initial states give a finite numerical check of the attraction basin.

**Direct finite chains.** The exchangeable chain on sorted internal-state tuples has $\binom{N+2n-1}{2n-1}$ states. The script constructs exact integer transition rows from the independent one-agent moves, applies 175-digit GTH elimination, and normalizes the output as a rational vector $v$. Its exact integer balance residual gives
$$
\|v-\pi_N\|_1\le (2n-1)(200/3)^{N(2n-1)}
                    \|vP-v\|_1<10^{-84}
$$
in every saved case. The bound follows from the common deepest-$C$ population column, using the same path as (3) for every agent. The table gives stationary productive probability and welfare at $N=5$, where the integer quorum requires two contributors.

| Depth | Rule | $P(\mathrm{productive}),\ \alpha=.75$ | $W_5(.75)$ | $P(\mathrm{productive}),\ \alpha=.90$ | $W_5(.90)$ |
|---:|---|---:|---:|---:|---:|
| 1 | Linear | .6151559900 | .6823498419 | .6989404986 | .6678729482 |
| 1 | Randomized boundary | .6282205116 | .6849075499 | .7135266084 | .6702310232 |
| 2 | Linear | .4272818560 | .7180435351 | .6104490568 | .6963789048 |
| 2 | Randomized boundary | .4372285706 | .7196892143 | .6201118808 | .6981612542 |
| 3 | Linear | .2276369571 | .7511288292 | .4914785717 | .7233826041 |
| 3 | Randomized boundary | .2347817714 | .7516941375 | .4992915214 | .7243236257 |

At $n\ge4$, global selection down to $A_n$ and efficiency of $W_N(A_n)$ remain open. The stationary obstruction (3), the lack of a below-Nash productive fixed point, the benchmark fixed-point classification, and the large-depth quota law apply at every depth.

From the study root, run the verification with Python, mpmath, and NumPy. NumPy performs integer matrix products in the depth-three sign certificate.

```sh
python3 experiments/phase2b_quorum_memory.py
```

The saved file contains the rationally bracketed branch crossings through depth 1024, the trapping and periodic-orbit certificates, and the finite-chain observables and error bounds. [Reproduction script](../experiments/phase2b_quorum_memory.py) · [Numerical data](../experiments/data/phase2b_quorum_memory.json)
