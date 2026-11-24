# The randomized Tsetlin boundary and unequal memories

In Tsetlin's $B_{2n,2}$ rule, a penalty at the shallowest state chooses between the two actions with equal probabilities. Suppose each player uses a fresh private coin. With sufficiently correlated penalties, the shorter-memory player can decline switches for a macroscopic part of a successful excursion while its partner catches up. This changes the exponential rate, and changes the power of memory even at the threshold where the rates coincide. [Tsetlin's survey, §6](../sources/extracted/Tsetlin_1963_UMN_18_FiniteAutomataBehavior_rus.txt) · [Hard-boundary calculation](phase1_quadrant.md)

## The stopped experiment

Let $1/2<p<1$, $q=1-p$, $\delta=p-q$, $\rho=q/p$, $r=\log(p/q)$ and $c=\log 2$. Measure deficits from the deepest states. The increment pair $(U,V)$ is drawn independently from round to round, with probabilities $(a,b,b,d)$ on $(+,+),(+,-),(-,+),(-,-)$, where

$$
 b=pq(1-\kappa),\qquad a=q-b,\qquad d=p-b,
 \qquad -q/p\le\kappa\le1.
$$

The coordinates reflect at zero. Put $m=n_1-1\ge n=n_2-1\ge1$. If an increment would carry coordinate $i$ above its upper barrier, that player flips with probability $1/2$ or stays at the barrier with probability $1/2$. A flip stops the experiment. Start at $(0,0)$. Write $h^B_{m,n}$ for the probability of visiting $(m,n)$ before a flip or the first positive return to $(0,0)$. A rejected shallow switch can therefore occur before the target is reached.

## The corner theorem

Fix an aspect ratio $\gamma\ge1$ and $m=\gamma n+O(1)$. For $-q/p<\kappa<1$,

$$
 h^B_{m,n}=\Theta\!\left(n^{\beta_B}e^{-nE_B}\right).
$$

Write $M(s,t)=a e^{s+t}+2b\cosh(s-t)+d e^{-s-t}$ and $H(x,y)=\max_{M\le1}(sx+ty)$. Let $(s_\gamma,t_\gamma)$ be the support point in direction $(\gamma,1)$. The hard-boundary exponent $E_L$ and power $\beta_L$ in the companion theorem apply to $B$ throughout the oblique and vertical regimes. In the hard direct regime the rule is

| Condition | $E_B$ | $\beta_B$ |
|---|---:|---:|
| $t_\gamma>-c$ | $H(\gamma,1)$ | $-1/2$ |
| $t_\gamma\le-c$ | $s_B\gamma-c$ | $0$ |

Here $M(s_B,-c)=1$ on the right branch. At equality $E_B=H(\gamma,1)$, whereas for $t_\gamma<-c$ the inequality $E_B<H(\gamma,1)$ is strict by uniqueness of the support point. In particular, every equal-memory case with $0<\kappa<1$ has $E_B=\log(d/a)$ and $\beta_B=-1/2$. At independence $E_B=(\gamma+1)r$ and $\beta_B=0$. All three negative-correlation powers $0,-1/2,-3/2$ and their thresholds carry over from the hard rectangle. [Full hard-boundary phase table](phase1_quadrant.md)

The additional regime exists for some finite aspect ratio exactly when $b<b_B(p)$, where $b_B(p)$ is the unique root in $(0,q/5)$ of

$$
             (4p-5b)(q-5b)=16(pq-b)^2.                    \tag{1}
$$

In that range define

$$
 A=a/2+2b,\qquad D=b/2+2d,\qquad
 z=\frac{1+\sqrt{1-4AD}}{2A},\qquad s_B=\log z,
$$

$$
 v_x=Az-D/z,\qquad v_y=(a/2-2b)z+(b/2-2d)/z,\qquad
 \gamma_B=v_x/v_y.
$$

Then $v_x,v_y>0$, $\gamma_B>1$, and the second line of the table applies exactly when $\gamma\ge\gamma_B$. For example, $p=7/10$ requires $\kappa>25/27$. Taking $\kappa=181/189$ gives $(s_B,-c)=(\log4,-\log2)$, $(v_x,v_y)=(23/75,1/6)$ and $\gamma_B=46/25$. At $\gamma=3$ the rates are $E_B=5\log2=3.4657359028\ldots$ and $E_L=3.5112801159\ldots$.

To check (1), increase $\gamma$ from 1 to infinity. By strict convexity $t_\gamma$ decreases from $\tfrac12\log(d/a)>0$ to the value $t_\infty$ at the rightmost point of $M\le1$. At $\kappa=1/2$ the rightmost point is $(r,0)$. For $\kappa<1/2$ the hard direct branch has $t_\gamma>0$ throughout (the adjacent oblique tilt is $(r,t_*)$ with $t_*>0$). If $1/2<\kappa<1$, the equation $t_\infty=-c$ requires $M=1$, $M_t=0$. With $z=e^s$ it becomes

$$
 a z+b/z=1,\qquad b z+d/z=1/4.
$$

The determinant is $ad-b^2=pq-b>0$. Solving the two linear equations for $z,1/z$ and taking their product gives (1) and $a>4b$. The difference of its two sides is the convex quadratic $9b^2-(20p+5q-32pq)b+4pq\delta^2$. It is positive at 0 and negative at $q/5$, hence has just one admissible root. As $b\downarrow0$ the rightmost $s$ tends to infinity. Indeed, bounded $s$ forces $t$ bounded on $M=1$ for small $b$, yet the limiting equations $q e^{s+t}+p e^{-s-t}=1$ and $q e^{s+t}-p e^{-s-t}=0$ are incompatible for $p>1/2$. The rightmost $s$ is nonnegative and $M\le1$ bounds $s+t$ above, so $t_\infty\to-\infty$. Continuity proves the criterion. At the crossing for a finite aspect ratio, differentiating $M$ at $(s_B,-c)$ gives the displayed speeds.

### The correlation that minimizes the corner cost

For every $\gamma>1$, both tactics have the same unique optimal correlation for the frozen corner,

$$
       \kappa_{\rm opt}=\frac{1+1/\gamma}{2},\qquad
       \min_\kappa E_B=\min_\kappa E_L=\gamma\log(p/q),\qquad
       \beta_B=\beta_L=-1/2\quad\text{at }\kappa_{\rm opt}.
$$

The optimum depends only on the memory ratio. At this correlation both players can reach their shallow boundaries at the exponential cost of the longer player's marginal excursion. Indeed, $M(r,0)=1$ for every correlation and the tilted drift there is $\delta(1,2\kappa-1)$. Its slope agrees with the target for exactly the displayed $\kappa_{\rm opt}$. The strict convexity of $M\le1$ makes its support $H(\gamma,1)$ strictly greater than $r\gamma$ for every other correlation in the direct regime. The oblique and vertical exponents both exceed $r\gamma$ by their positive vertical term. In the soft upper-wall regime the inequality is strict at $\gamma_B$ and persists at larger ratios because $s_B>r$ along the direct-support arc after $t=0$.

In fact the cost decreases strictly up to $\kappa_{\rm opt}$ and increases strictly thereafter, for both tactics. At a smooth support point the derivative of $H$ in $\kappa$ has the sign opposite to $M_\kappa=4pq\sinh(s)\sinh(t)$, by Lagrange multipliers. In a direct phase $s>0$, and $t$ crosses zero exactly as the tilted slope at $(r,0)$ crosses the target. In the oblique phase $t_*$ decreases strictly with $\kappa$. In the vertical phase both coordinates of the supporting tilt at $(0,1)$ are positive. In the soft upper-wall phase $s_B'=-M_\kappa/M_s>0$. The formulas agree at their joins. At $\kappa=1$ the hard corner is inaccessible while $s_B\to r+c$ in the soft formula, agreeing with (4).

In particular, for $B$ fully common feedback has a higher exponential cost than independent feedback exactly when $\gamma>1+r/\log2$. At $p=7/10,\gamma=3$ the costs are $2.54189$ at the optimum $\kappa=2/3$, $3.38919$ at independence, and $3.92819$ at perfect synchrony.

## Upper bounds and the price of a rejected switch

Couple the capped pair to the unrestricted reflected pair $W$ with the same increments. Each capped coordinate is at most its unrestricted counterpart. Consequently a surviving $B$ excursion ends by the next return of $W$ to the joint origin. The unrestricted return has finite mean and the stationary marginals have tails $\rho^k$. The stationary occupation formula for a return cycle therefore bounds the expected visits to an axis point at distance $k$ in the capped excursion by $C e^{-rk}$. [Unrestricted cycle construction](phase1_quadrant.md)

A stronger axis bound is needed when $\kappa\ge1/2$. For any $s\ge0$, $-c\le t\le0$ with $M(s,t)=1$, tilt the increment probabilities by $e^{sU+tV}$. Along a segment starting at $(0,j)$ and having positive horizontal coordinate after departure, let $D_i$ and $C_i$ count attempts to move below zero and above the ceiling in coordinate $i$. The original probability of the increments and survival, relative to the tilted increment probability, is

$$
 e^{-s\Delta X-t\Delta Y}\,
  e^{s D_x+t D_y}(e^{-s}/2)^{C_x}(e^{-t}/2)^{C_y}.       \tag{2}
$$

Here $D_x=0$ and each boundary factor is at most one. Hence the first hit of $(k,0)$ before the next horizontal zero has probability at most $e^{-sk+tj}\le e^{-sk}$. Starting from that hit, the expected number of visits to horizontal level $k$ before horizontal zero is at most $1/\delta$. After each visit there is probability at least $p(1-\rho)=\delta$ to step down and reach zero without revisiting $k$ (an earlier kill also terminates visits). The expected number of starting visits $(0,j)$ is bounded by the unrestricted mean cycle duration. The axis occupation bound follows with

$$
             A_B=\max\{s:M(s,t)\le1,\ -c\le t\le0\}.
$$

By symmetry the same bound applies on the other axis. For $\kappa\ge1/2$ the unconstrained rightmost point has $t_\infty\le0$. On a direct ray with $t_\gamma>-c$, strict convexity gives $s_\gamma<A_B$ and $t_\gamma\le s_\gamma$. If the rightmost point lies below $-c$, use the point at $t=-c$ on the arc beyond the support point. When $\kappa<1/2$, use $A_B=r$ as the axis bound throughout the hard-case estimates.

After the last visit to either lower axis, the two lower reflection counts vanish. Suppose that visit was $(k,0)$. If the final upper rejection counts equal $i,j$, the free increment path ends at $(m+i,n+j)$ when started at $(k,0)$ and never exceeds these two expanded ceilings. Indeed for a coordinate with start $x$ and ceiling $m$, its current upper count is $\max_{u\le l}(x+S_u-m)^+$ after $l$ steps. The weight of the rejection coins is $2^{-i-j}$. After tilting by any $(s,t)$ on $M=1$, the extra factors relative to targeting the physical corner are

$$
                        e^{-(s+c)i-(t+c)j}.                 \tag{3}
$$

These factors are summable in the first line of the table. The direct Green-function bound for fixed $i,j$ is $C(n+j)^{-1/2}$ from the horizontal axis, or $C(m+i)^{-1/2}$ from the vertical axis. Sum over the last axis point using $A_B>s_\gamma,t_\gamma$, or the hard direct inequalities when $\kappa<1/2$. This gives $C n^{-1/2}e^{-s_\gamma m-t_\gamma n}$. Keeping only paths without a rejected switch supplies the matching hard lower bound. [Tilted Green and ballot estimates](phase1_quadrant.md)

In the hard oblique, tangent and vertical regimes the relevant tilts all have positive components. For the oblique bound, at each $i,j$ sum the tilted horizontal endpoint mass over all last-axis positions, bounded by 1, then the vertical potential at $n+j$, bounded by $1/v_y$. For the vertical bound, write $\ell=m-k$. The one-wall ballot factor at an endpoint of distance $\ell+i$ is $2(\ell+i+1)/(l+\ell+i+2)$ in $l$ steps, giving an upper potential $C(\ell+i+1)(n+j)^{-3/2}$. With strictly negative $g$ in the hard table, the remaining weight $e^{-(s_0-r)\ell}$ is summable. At tangency, summing over $\ell+i\ge i$ is bounded by summing over all nonnegative horizontal endpoints, giving $C(n+j)^{-1/2}$ as in the centered ballot estimate. The sums in (3) absorb the factor $1+i$ where it occurs. The other last axis uses the same exchanged or unexchanged tilt as in the hard proof. Thus the hard upper powers carry over in all these regimes, and the hard paths give the corresponding lower bounds.

## A path along the shorter player's upper boundary

For $\gamma\ge\gamma_B$, use $(s,t)=(s_B,-c)$ in (2). Work from the last horizontal zero, allowing visits to either vertical boundary. The last factor in (2) is exactly one even for a path with very many vertical rejections. First hitting the physical corner before the next horizontal zero costs at most $e^{-s_Bm+cn-cj}\le e^{-s_Bm+cn}$ from $(0,j)$. Summing over starts again incurs only the finite unrestricted mean cycle duration.

For the lower bound, work in the tilted free walk with positive drift $(v_x,v_y)$. Use endpoints $(m,n+j)$ for

$$
    j=m v_y/v_x-n+O(\sqrt n),\qquad l=m/v_x+O(\sqrt n).
$$

There are order $n$ admissible pairs $(j,l)$ with $j\ge0$ and $m\equiv n+j\equiv l\pmod 2$, including at equality $\gamma=\gamma_B$. For example, take $j$ in a window of width $\sqrt n$ above $\max(0,m v_y/v_x-n)$. The positive-drift rectangle estimate gives mass at least $c_1/n$ for each such bridge to stay above zero after departure and below the two expanded ceilings. Require the horizontal coordinate to hit $m$ for the first time on its last step. The same estimate holds with this condition by forcing a fixed final string of joint upward steps and keeping the intervening path below the buffered ceiling, as in the hard proof.

After capping the second coordinate at $n$, the path remains positive there provided its free path has no drawdown of size $n$ after reaching that level. Among $l=O(n)$ positive-drift increments the probability of such a drawdown is $O(n^2e^{-c_2n})$ by an exponential bound on every subinterval. Removing those paths preserves the lower mass for each bridge. Its endpoint is a free vertical record, so the capped endpoint is $(m,n)$ and there are exactly $j$ rejected vertical switches. Formula (2) gives the same original weight multiplier $e^{-s_Bm+cn}$ for every bridge. The first horizontal hit fixes $l$, and the increments determine $j$, so the bridge events are disjoint. Their sum gives the claimed power zero, including at the transition. Beyond the transition the typical value in this construction is $j=(\gamma/\gamma_B-1)n+O(\sqrt n)$.

## The two endpoints and the first profile exit

At $\kappa=-q/p$, simultaneous penalties have probability zero. From the last lower-axis point to the target, the sum of the free increments is nonpositive in every round and an upper rejection further decreases the physical increment. The last axis point has sum at most $m$, so $h^B_{m,n}=0$.

At $\kappa=1$ the following sharper equivalent holds at every fixed aspect ratio,

$$
                 h^B_{m,n}\sim \delta\,\rho^m 2^{-(m-n)}.      \tag{4}
$$

Before the first horizontal hit of $m$, the long coordinate is at least the short coordinate and their difference never exceeds $m-n$. A rejected short upward attempt increases that difference only while the long coordinate is moving to a level at most $m$. A short reflection at zero decreases it. Thus the first horizontal hit of $m$ is the first corner hit, and return to the joint origin is horizontal return. Tilt the common increment by $r$. The probability under this positive-drift law of hitting $m$ before positive return is $\delta/(1-\rho^m)$ by gambler's ruin. At least $m-n$ short rejections are necessary. If no drawdown of size $n$ occurs after the first record $n$, exactly $m-n$ are necessary. Under the tilt an excursion from a record level $k\in\{n,\ldots,m-1\}$ falls to $k-n$ before the next record with probability at most $\rho^n$. A union bound therefore sandwiches $h^B_{m,n}/(\rho^m 2^{-(m-n)})$ between $\delta/(1-\rho^m)-(m-n)\rho^n$ and $\delta/(1-\rho^m)$. For $m=n$ the upper value is exact. Under hard overflow and $m>n$, identical increments make the corner inaccessible.

In a full sequence of returns to the deep origin, the probability of a simultaneous first flip is $\Theta(n^{\beta_B}e^{-n(E_B-r)})$ for each fixed interior correlation. Indeed the probability of any flip in one excursion is $\Theta(e^{-rn})$. The stationary marginal tail gives the upper bound. For the lower bound, follow the short coordinate to $n$ before its first return to zero, then prescribe its next loss and accepted coin, of probability $q/2$. An earlier flip already achieves the event. The simultaneous flip probability per excursion is between $a h^B_{m,n}/4$ and $h^B_{m,n}$, since a joint penalty and two accepted coins flip both players from the corner. Regeneration gives the ratio of the two per-excursion probabilities. The mean time until any first flip has order $e^{rn}$ since the expected truncated excursion length is bounded above by the unrestricted mean return and below by one. These first-exit statements concern the frozen profile.

Under perfect synchrony, set $k=m-n$ and $x=(\rho/2)^k$. Uniformly for $0\le k\le Cn$ with fixed $C$,

$$
 \Pr\{\text{simultaneous first flip}\}\sim
          \frac{(2p-q)x}{4p-q+2\delta x}.                  \tag{5}
$$

For equal barriers the probability is exactly $1/3$. Until a switch has occurred both states coincide, and at each shallow joint penalty two coins accept with probability $1/4$ while at least one accepts with probability $3/4$. At $p=7/10$, one extra memory state changes the limiting probability from $1/3$ to $3/34$.

To prove (5), a deep excursion first reaches the short upper level at $(n,n)$ with probability $H_n=\delta\rho^n/(1-\rho^n)$. From there provisionally remove both distant lower walls. Before the long coordinate reaches $m$, the next short upper attempt is exactly the next unit record of the free common walk. From any record it is reached with probability $\rho$. It yields a short flip with probability $\rho/2$ or a new record with both players surviving with probability $\rho/2$. Reaching the $k$th such record with both surviving costs $x$. Thereafter the two upper walls are aligned. From their common corner the probability of an eventual switch is $A_2=3q/(4p-q)$, of which $S_2=q/(4p-q)$ is simultaneous. These follow by summing over common record attempts, each continuing with probability $\rho/4$. The total chance of any flip from $(n,n)$ in this model is

$$
                A_k=\frac{q}{2p-q}(1-x)+x A_2.
$$

Until the short coordinate first reaches zero the finite and distant-wall-free paths agree. Once it reaches zero the free path returns to the short upper wall with probability $\rho^n$. In the finite walk a visit to either upper wall requires the short coordinate to reach $n$, since $0\le X-Y\le k$. From its zero the chance of doing so within $Ln$ steps is at most $Ln\rho^n$, by domination by a stationary reflected coordinate. A large fixed $L$ bounds the probability that the long coordinate, initially at most $(1+C)n$, avoids zero or killing throughout those steps by $e^{-c_3n}$, using negative drift. The true chance of any flip after reaching $(n,n)$ therefore differs from $A_k$ by $o(1)$ uniformly. The same argument from $(m,n)$ gives $S_2+o(1)$ for a simultaneous flip before return. By (4) and its quantitative error bound, $h^B_{m,n}/H_n=x(1+o(1))$ uniformly. The ratio of per-excursion probabilities is thus $x S_2/A_k$ times $1+o(1)$, which simplifies to (5).

## The leading constant at independence

For $\kappa=0$ and every fixed aspect ratio,

$$
 h^B_{m,n}\sim C_B(p)\rho^{m+n},\qquad
 C_B(p)=\frac{[(1-\rho)/(1-\rho/2)]^2}{\sum_{j\ge0} f_j^2},
 \qquad \sum_{j\ge0}f_j z^j=\frac{2}{1-qz+\sqrt{1-4pqz^2}}.     \tag{6}
$$

The independent surviving one-coordinate kernels satisfy detailed balance with weights $\rho^x$, including their holding steps. Reversing a successful path therefore extracts the factor $\rho^{m+n}$. The remaining committor starts at the corner, avoids killing and positive return there, and reaches the deep origin. In coordinates measured from their shallow walls, its limit is the probability that two independent positive-drift walks survive forever without jointly revisiting zero. At a shallow wall a downward attempt kills with probability $1/2$ and otherwise holds. To justify passage to the half-line, run for $\lfloor n/3\rfloor$ steps, before either distant edge is reachable. Except on a set of exponentially small probability, both surviving coordinates are then at distance $\Omega(n)$ from their shallow wall, by concentration of the free sums and domination by lower reflection. From there, the chance of a shallow-wall visit within $O(n^2)$ steps is exponentially small while the chance of reaching the deep pair in that time tends to one, by the negative-drift block argument in the companion note. For the half-line process the probability of a subsequent shallow-wall visit is also exponentially small by gambler's ruin. [Finite-to-half-line bounds](phase1_quadrant.md)

One walk survives from zero with probability $u=\delta/(p-q/2)$. Indeed, after stepping away with probability $p$ it returns with probability $\rho$ and after a declined penalty of probability $q/2$ it is at zero again. Decomposing joint survival at the last joint visit gives $u^2=C_B(p)\sum_j f_j^2$, where $f_j$ is the one-coordinate surviving return probability at time $j$. Its first positive return is a retained one-step penalty, with generating function $qz/2$, or a strictly positive excursion of generating function $(1-\sqrt{1-4pq z^2})/2$. Summing successive returns yields (6).

For a rational truncation bound put $R=2/(1+4pq)>1$. The generating function in (6) evaluates to $F(R)=(1+4pq)/p$. Its nonnegative coefficients give

$$
           \sum_{j\ge N}f_j^2\le F(R)^2 R^{-2N}/(1-R^{-2}).
$$

At $p=7/10$, 1024 terms enclose $C_B$ between
$0.48137834861935646834220323676437287069885815801417223865353386816017$
and
$0.48137834861935646834220323676437287069885815801417223865353386816018$.
The hard constant at the same $p$ is $0.30941719082791247349\ldots$.

## Finite checks

At $p=7/10$, the following entries are $h^B_{m,n}e^{nE_B}/n^{\beta_B}$ from positive Decimal elimination. At the critical aspect ratio the pair of sizes is chosen to have integral barriers.

| $\kappa$ | $\gamma$ | $\beta_B$ | Short barriers | Normalized $B$ committors |
|---:|---:|---:|---|---|
| $1/2$ | 1 | $-1/2$ | 10, 20, 40 | 0.557965, 0.530653, 0.516472 |
| 0 | 1 | 0 | 10, 20, 40 | 0.481347, 0.481378, 0.481378 |
| $-19/50$ | 1 | $-3/2$ | 10, 20, 40 | 4.04750, 4.70030, 5.14022 |
| $181/189$ | $46/25$ | 0 | 25, 50 | 0.127883, 0.117423 |
| $181/189$ | 3 | 0 | 10, 20, 40 | 0.165870, 0.162568, 0.162512 |
| 1 | 3 | 0 | 10, 20, 40 | 0.399779, 0.400000, 0.400000 |

For $\kappa=181/189$ and $(m,n)=(120,40)$ the two committors, rounded to 60 significant figures, are

$$
\begin{aligned}
 h^B_{120,40}&\simeq1.01131510213573625669387847738246449239460209224757880842414\times10^{-61},\\
 h^L_{120,40}&\simeq2.11390076797060445400441942936785014009921609371427478989924\times10^{-64}.
\end{aligned}
$$

For a trial committor $v$, the script computes the exact rational maximum Dirichlet residual. From every state $m$ joint wins suffice for absorption, so the inverse Dirichlet matrix has infinity norm at most $m/d^m$. The resulting rational enclosures have relative widths below $9\cdot10^{-73}$ and $2\cdot10^{-71}$, respectively. The program also checks nine finite identities by exact elimination, including boundary models at both correlation endpoints. [Reproducible experiment](../experiments/phase1_random_boundary.py)

```sh
python3 -B experiments/phase1_random_boundary.py --sizes 10 20 40 --certify 40 --digits 60 --compare-hard
python3 -B experiments/phase1_random_boundary.py --gamma 46/25 --sizes 25 50 --compare-hard
python3 -B experiments/phase1_random_boundary.py --kappa 0 --gamma 1 --sizes 10 20 40 --independent-terms 1024
python3 -B experiments/phase1_random_boundary.py --kappa 1 --gamma 3 --sizes 10 20 40 --first-flip
```
