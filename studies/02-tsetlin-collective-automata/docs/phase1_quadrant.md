# A frozen Tsetlin profile up to its first flip

## The stopped event

Fix a common win probability $1/2<p<1$, write $q=1-p$,
$\delta=p-q$, and $r=\log(p/q)$. A loss contributes $+1$ to
the distance from the deepest memory state. During a frozen profile the
increments $(U,V)$ are independent across rounds and have joint law

| $(U,V)$ | $(1,1)$ | $(1,-1)$ | $(-1,1)$ | $(-1,-1)$ |
|---|---:|---:|---:|---:|
| Probability | $a=q^2+\kappa pq$ | $b=pq(1-\kappa)$ | $b$ | $d=p^2+\kappa pq$ |

The feasible interval is $-q/p\leq\kappa\leq1$. Starting at $(0,0)$,
apply $X'=\max(0,X+U)$, $Y'=\max(0,Y+V)$. Let $m\ge n\ge1$.
Stop on the first positive return to $(0,0)$, the first overflow
$X>m$ or $Y>n$, or the first visit to $(m,n)$.
Write $h_{m,n}$ for the probability of this last outcome. An axis
visit between departure and return is permitted. With memories
$n_1,n_2$ the preflip barriers are $m=n_1-1$, $n=n_2-1$.

## Sharp corner asymptotics

For $-q/p<\kappa<1$, define the moment generating function and its
support function by

$$
 M(s,t)=a e^{s+t}+2b\cosh(s-t)+d e^{-s-t},\qquad
 H(x,y)=\max_{M(s,t)\leq1}(sx+ty).
$$

Fix $\gamma\ge1$ and put $m=\gamma n+O(1)$. Then
$$
                 h_{m,n}=\Theta\!\left(n^\beta e^{-nE}\right).
$$
The constants can depend on the parameters and the bound on the rounding
error. When $\kappa<1/2$, set
$$
 \lambda=1-2\kappa,\qquad
 t_*=\log\frac{1+\delta\lambda}{1-\delta\lambda},\qquad
 g=\frac{1+(1-\delta^2)\lambda-\lambda^2}
          {\lambda(1-\delta^2\lambda^2)}.
$$

| Parameters | $E$ | $\beta$ | Route to the corner |
|---|---|---:|---|
| $\kappa\ge1/2$, or $\kappa<1/2$ and $g>\gamma$ | $H(\gamma,1)$ | $-1/2$ | Positive velocity in both coordinates |
| $\kappa<1/2,\ 0<g\le\gamma$ | $r\gamma+t_*$ | $0$ | Along the longer axis, then at velocity ratio $g:1$ |
| $\kappa<1/2,\ g=0$ | $r\gamma+t_*$ | $-1/2$ | The second leg has zero horizontal drift |
| $\kappa<1/2,\ g<0$ | $r\gamma+H(0,1)$ | $-3/2$ | The second leg starts a bounded distance from the upper horizontal-coordinate barrier |

At $g=\gamma>0$ an initial excursion along the longer axis of order
$\sqrt n$ contributes the full power $\beta=0$. For $g=0$ the
distance of the departure point from $X=m$ has this same order. For
$g<0$ the walk can fluctuate a distance of order $\sqrt n$ away
from the wall during its second leg.

For the diagonal $m=n$ the positive-correlation rate simplifies to
$\log(d/a)$, with power $-1/2$, for every $0<\kappa<1$.
Independence gives $2r$ with power zero. For $\kappa<0$ the change
from an oblique second leg to a vertical leg occurs at
$$
  \lambda_0=\frac{1-\delta^2+\sqrt{(1-\delta^2)^2+4}}{2},\qquad
  \kappa_0=(1-\lambda_0)/2.
$$
The powers for $\kappa_0<\kappa<0$, $\kappa=\kappa_0$, and
$-q/p<\kappa<\kappa_0$ are respectively $0,-1/2,-3/2$. The
same transition applies at every fixed $\gamma\ge1$. For
$0<\kappa<1/2$ the change from a direct route to an initial stretch
along an axis occurs at the memory ratio $\gamma=g>1$.

At $\kappa=1$ the two coordinates coincide at all times. For $m>n$
the corner is unreachable. For $m=n$, one-dimensional gambler's ruin
gives
$$
               h_{n,n}=q\,\frac{e^r-1}{e^{rn}-1}.
$$
At $\kappa=-q/p$ the probability is zero for all $m,n\ge1$.
Here $a=0$. The sum of the deficits cannot increase during a segment
in the open quadrant. The last axis point has sum at most $m$, and
the target has sum $m+n$.

### A radical formula for the direct rate

For $x,y\ge0,\ x+y>0$, set $\eta=|x-y|/(x+y)$,
$e=\eta^2,\ c=4b^2+e(1-4ad)$, and
$$
 z=\frac{c}{e+\sqrt{e^2+(1-e)c}},\quad
 u=\log\frac{1-z+\sqrt{(1-z)^2-4ad}}{2a},\quad
 v=\operatorname{arcosh}\frac{z}{2b}.
$$
Then $H(x,y)=((x+y)u+|x-y|v)/2$. To see this, assume $x\ge y$,
write $u=s+t,\ v=s-t$, and impose $M=1$. The normal condition
gives $2b\sinh v=\eta(a e^u-d e^{-u})$. Its two sides are
nonnegative. Squaring with $z=2b\cosh v$ gives
$z^2-4b^2=e((1-z)^2-4ad)$, whose indicated root lies in
$[2b,1-2\sqrt{ad}]$. Symmetry gives the formula for $x<y$.

## Proof

### Axis visits during an excursion

The unrestricted reflected chain has a stationary version. In a
two-sided sequence of increments, each present coordinate is the
supremum of the backward partial sums of that coordinate, including
the zero-length sum. Both suprema are finite by negative drift.
This representation follows by iterating the reflection recursion.
A fixed string of joint wins clears any bounded initial pair, so the
stationary origin has positive probability. All states reachable
from the origin can return to it, and the stationary cycle formula
identifies the expected visits to a point before the next return with
its stationary probability divided by the stationary mass of the origin.
The one-coordinate marginal has mass $(1-e^{-r})e^{-rk}$ at $k$,
by the birth-and-death balance equations. Thus the expected number of
visits to either axis point at distance $k$ before any of our stopping
events is at most $C e^{-rk}$. The initial origin is counted once.

A sharper bound applies when $\kappa\ge1/2$. Let
$A=H(1,0)$, and write $(A,t_0)$ for its maximizing point. It
satisfies $t_0\le0$. Indeed, at $(r,0)$ the tilted mean of $V$
is $\delta(2\kappa-1)\ge0$, and tilting $U$ farther to the right
increases this mean since the conditional regression of $V$ on $U$
has slope $\kappa>0$. Also $M(s,0)>1$ for $s>r$. Minimizing in
$t$ at the rightmost feasible $s\ge r$ therefore gives $t_0\le0$.
In the backward representation, the event $X\ge k,Y=0$ requires the
unreflected horizontal sum to hit $k$ while its vertical sum is at
most zero. At that first horizontal hit the likelihood of the original
increments relative to the $(A,t_0)$-tilted law is at most $e^{-Ak}$.
One can sum over all finite hitting times. This gives the axis bound
$C e^{-Ak}$. Below, use $A=r$ when $\kappa<1/2$.

For $\kappa<1/2$, the following matching lower bound will be needed.
For all sufficiently large $k\le m=O(n)$, the probability of reaching
$(k,0)$ at the first horizontal hit of $k$, with no joint return or
overflow, is at least $c e^{-rk}$. Under the $(r,0)$ tilt, the
unreflected horizontal sum has drift $\delta>0$ and the vertical
sum has drift $u_0=\delta(2\kappa-1)<0$. The blocks between successive
ascending horizontal ladder levels are iid. Their durations $L$ have
an exponential tail, since failure to reach level 1 by time $j$
implies that the horizontal sum at $j$ is at most zero. The net
vertical increment $Z$ in a block satisfies
$\mathbb E Z=u_0\mathbb E L<0$ by Wald's identity. The reflected
vertical height after a block is $\max(Y+Z,C)$, with $0\le C\le L$
the maximum nonnegative terminal suffix sum of the block. For a small
$h>0$, $\mathbb E e^{h Z}<1$ and $\mathbb E e^{hL}<\infty$.
The inequality $e^{h\max(Y+Z,C)}\le e^{hY}e^{hZ}+e^{hC}$ now gives
a uniform exponential moment for the height at every ladder level.
The maximum height inside a block is at most its initial height plus $L$.

Start with a fixed string of $(1,-1)$ steps to a level $K_0$ so
large that the tilted probability of a later horizontal visit to zero
is below $1/8$. Choose $K$ such that the chance of vertical height
above $K$ at the first horizontal hit of $k-K$ is below $1/8$.
The chance of any vertical overflow in the first $O(n)$ ladder
blocks is $O(n e^{-c n})$. Force another $K$ steps of $(1,-1)$.
With probability bounded below under the tilt, the path ends at
$(k,0)$ without an earlier hit of $k$ or a horizontal reflection.
Its original likelihood is $e^{-rk}$ times its tilted likelihood.

### Interior passages and the ceiling ballot factor

After its last axis point the reflected walk has ordinary iid
increments. From a horizontal-axis point $(k,0)$ write
$\ell=m-k$. Only $\ell\equiv n\bmod 2$ can contribute. If
$M(s,t)=1$, changing to the $(s,t)$ tilt multiplies every interior
path probability to the corner by $e^{-s\ell-tn}$ in the
original measure. The first step into the open quadrant has its
ordinary increment. The same construction interchanges the axes.

We record the estimates used below. All tilted laws have four positive
step probabilities. Denote their mean by $(v_x,v_y)$.
For any tilted law with $v_y>0$,
$$
 \sum_{j\ge0}\Pr_\theta(S_j=(\ell,n))\le C n^{-1/2},\qquad
 \sum_{j\ge0}\Pr_\theta(S^Y_j=n)=1/v_y.                 \tag{1}
$$
The second identity follows by first hitting $n$, then using the
one-dimensional return probability $1-v_y$. Conditional on the
vertical sum at time $j$, the horizontal sum is the sum of two
independent binomial counts, up to a scale and translation. At least
one count involves $j/2$ trials with success probability strictly
between zero and one, so every point has conditional probability
at most $C/\sqrt j$. Since $j\ge n$, the first bound follows.
For the same reason an unrestricted two-dimensional point mass at time
$j$ is at most $C/j$. It is at least $c/j$ on the proper parity
class whenever the endpoint differs from $j(v_x,v_y)$ by
$O(\sqrt j)$. For this lower bound the vertical count is within a
fixed multiple of its standard deviation, both conditional groups have
order $j$ trials, and summing the two binomial probabilities over a
window of order $\sqrt j$ gives the assertion by Stirling's bounds.

For the single ceiling $X\le m$, conditional on the two endpoint
sums the horizontal sign sequence is a uniform permutation of its
signs. This is because the conditional law of the *total* vertical
increment given the entire horizontal sequence depends only on the
number of horizontal plus signs. The one-dimensional reflection
principle therefore gives the exact fraction of bridges from
$m-\ell$ to $m$ staying below or on $m$ as
$$
                      \frac{2(\ell+1)}{j+\ell+2}.         \tag{2}
$$
In particular, the sum in (1) with this extra ceiling is bounded by
$C(\ell+1)n^{-3/2}$.

Two lower estimates also hold with all four rectangle constraints.
The vertical lower boundary is avoided after departure, and the
corner is reached for the first time on the last step.

1. Suppose $v_x,v_y>0$ and $(\ell,n)=j(v_x,v_y)+O(\sqrt n)$,
   with $j\asymp n$ of admissible parity. From $(k,0)$ the
   constrained passage has tilted probability at least $c/n$.
2. Suppose $v_x=0,v_y>0,\ m\asymp n,\ 0\le\ell\le C\sqrt n$, and
   $j=n/v_y+O(\sqrt n)$ of admissible parity. The constrained
   passage has tilted probability at least $c(\ell+1)/n^2$.

Here are details accounting for the rectangle edges in these lower
bounds. In the first case force $K$ initial and $K$ final
$(1,1)$ steps. The intervening unrestricted endpoint mass is at
least $c/n$. For any fixed $K$, the same positive $c$ works
for all sufficiently large $n$, by the binomial lower bound. The
probability of a displacement against either positive drift through
a buffer $K$ at time $i$ is at most $C e^{-c_1(K+i)}$ by an
exponential moment. For $i$ in the first half of the intervening
passage the remaining point mass is at most $C/n$. For $i$ in the
second half the first probability alone is exponentially small in
$n$. This treats either lower edge. Apply the same argument to
the increments in reverse order from the specified endpoint for the
upper edges. Keep all intermediate heights below the final corner
height in the vertical coordinate. Taking $K$ large leaves positive
mass of order $1/n$, and the two fixed strings cost a constant.

For the second case force $K$ initial $(-1,1)$ steps and $K$
final $(1,1)$ steps. The intervening bridge starts and ends at
distances $D=\ell+K$ and $K$ from the horizontal-coordinate
ceiling. Conditional on the endpoint sums, the ceiling fraction is
bounded above by
$$
           C\min(1,(D+1)(K+1)/j)
$$
and is bounded below by $c(D+1)(K+1)/j$ in our range for all
sufficiently large $n$. In fact the reflected binomial count for
a nonnegative bridge from distance $D$ to $K$ is subtracted from
the unrestricted count, giving the ratio
$$
  1-\frac{\binom{j}{(j+K+D+2)/2}}
           {\binom{j}{(j+K-D)/2}}.                      \tag{3}
$$
For the upper bound exchange the endpoints if necessary and expand
the binomial quotient as a product of $\min(D,K)+1$ factors.
When $(D+1)(K+1)\ll j$, their logarithms sum to order
$-(D+1)(K+1)/j$. If either distance is comparable to $j$,
the stated upper bound follows from the bound by 1, after adjusting
the absolute constant. The same product gives the lower bound for
$D=O(\sqrt j)$ and fixed $K$, with absolute comparison constants.
Thus the ceiling-constrained intervening mass is at least
$c(D+1)(K+1)/n^2$.

The chance of also crossing a vertical edge at time $i$ in the
appropriate half is at most
$$
  C e^{-c_1(K+i)}(D+i+1)(K+1)/n^2
$$
for the lower edge. Condition on the position at time $i$, use the
upper bound in (3) for the rest and the $C/n$ unrestricted
two-dimensional point-mass bound. For the upper edge reverse the
increments and exchange $D,K$. Outside the indicated half the
exponential bound alone suffices. Crossings of the distant edge
$X=0$ have probability $O(n e^{-c_2 n})$, by concentration of
the centered horizontal sums. Summing and choosing $K$ large proves
the second estimate. Both constructions force a unique last axis
visit and a unique first visit to the corner at the specified time.

### Optimizing the tilted path and collecting the powers

The set $M\le1$ is strictly convex, smooth at its boundary, and
compact. Its Hessian is positive definite because the four possible
increments span the plane. For a nonzero direction, its unique support
point has outward normal $\nabla M$ parallel to that direction. This
normal is the drift of the tilted increments since $M=1$. The support
point $(s,t)$ for $(x,1)$ moves from the highest to the rightmost
point as $x$ increases from zero to infinity. Its first coordinate
increases strictly and its second coordinate decreases strictly for
$x>0$.

For $\kappa<1/2$, $M(r,0)=M(r,t_*)=1$. At $(r,0)$
the mean of $U$ is $\delta$. The regression of $V$ on $U$ is
unchanged by this tilt and has slope $\kappa$, giving
$u_0=\mathbb E V=-\delta\lambda$ and
$\operatorname{Cov}(U,V)=\kappa(1-\delta^2)$.
The further tilt by $t_*$ interchanges the two vertical-sign
probabilities. At $(r,t_*)$ the two drifts are therefore
$$
 v_y=-u_0=\delta\lambda,\qquad
 v_x=\delta-\frac{2u_0\kappa(1-\delta^2)}{1-u_0^2}.
$$
For the second identity use the affine regression of $U$ on the
binary variable $V$. Its slope at the first tilt is the covariance
divided by $1-u_0^2$. Direct simplification gives $g=v_x/v_y$.
Also
$$
  g-1=\frac{(1-\lambda^2)(1-\delta^2\lambda)}
                 {\lambda(1-\delta^2\lambda^2)} .
$$
Here $\delta\lambda<1$ for every feasible $\kappa<1/2$.
Consequently $g>1$ for $0<\kappa<1/2$, $g=1$ at independence,
and $g<1$ for negative correlation. The numerator of $g$ has
one positive zero $\lambda_0$. At the lower feasibility endpoint
the drift after this tilt has $v_x+v_y<0$ because $a=0,d>0$.
This places $\kappa_0$ strictly between $-q/p$ and 0.

For an upper bound, sum over all possible last axis visits during
one excursion. Use the axis occupation bounds and the Markov property
at each visit. If the last visit is $(k,0)$, every subsequent step
uses its original increment until the corner. A given admissible tilt
contributes an exponential factor
$$
     C e^{-A k-s(m-k)-tn}
        = C e^{-sm-tn} e^{-(A-s)k}.                     \tag{4}
$$
Multiply this by the appropriate tilted interior Green function
(the sum of the point probabilities over passage durations). A last
visit to the other axis has the corresponding formula with exchanged
coordinates. For the lower bounds, use the first hit of $k$ from the
axis lemma and the interior first-corner passages constructed above.
The last axis point and the passage duration are uniquely determined by
the resulting successful path, so the contributions can be added.

**Direct route.** Use the support point of $(\gamma,1)$. Its two
drifts are positive. Both $s,t<A$ when $\kappa\ge1/2$, by strict
convexity and finiteness of the positive slope. When $g>\gamma$
and $\kappa<1/2$, the support point of $(g,1)$ has $s=r=A$,
so $s<A$. In this case $\kappa>0$ and
$t\le\frac12\log(d/a)<r$, by comparing with the support point
of $(1,1)$. The geometric sums in (4) converge and (1) gives
the upper factor $n^{-1/2}$. For the lower bound begin at the
origin if $m\equiv n\bmod 2$, or at $(1,0)$ after one forced
mixed step otherwise. Use the first interior lower estimate at
$\Theta(\sqrt n)$ admissible times about $n/v_y$. This gives the
same factor. At $\gamma=1$ the support point is $s=t=\frac12\log(d/a)$,
and the two tilted drifts both equal $d-a=\delta$.

**Oblique second leg.** For $0<g\le\gamma$, use $(r,t_*)$ on
the horizontal axis. Summing the tilted endpoint mass first over
$\ell=m-k$, and then over times, gives an upper bound $1/v_y$
by (1). The exponential factor is $e^{-rm-t_*n}$. If $t_*\ge r$,
the exchanged bound on the other axis is $Ce^{-t_*m-rn}$, at most
the required order. If $t_*<r$, use the original tilt on the other
axis. Its additional weight at $(0,j)$ is $e^{-(r-t_*)j}$;
the horizontal endpoint mass summed over times is at most $1/v_x$.
For the lower bound select $\Theta(\sqrt n)$ eligible axis heights
$k=m-gn+O(\sqrt n)$. If $g=\gamma$ take
$\sqrt n\le k\le2\sqrt n$. For each $k$, sum the first interior
lower estimate over $\Theta(\sqrt n)$ central times. Each $k$
contributes at least $c n^{-1/2}e^{-rm-t_*n}$.

**Vertical second leg.** Let $(s_0,T)$ be the support point for
$(0,1)$, so $T=H(0,1)$, horizontal drift zero, and vertical
drift $v_y>0$. If $g<0$, the outward normal at $(r,t_*)$ points
to the left of vertical. The highest point therefore has $s_0>r$
and $T>t_*>r$. For $g=0$, $s_0=r,\ T=t_*>r$.
The horizontal-axis weight in both cases is
$$
              e^{-rm-Tn}e^{-(s_0-r)\ell}.               \tag{5}
$$
For $g<0$ the last factor is summable against $\ell+1$.
Equations (1) and (2) give an upper bound $C n^{-3/2}e^{-rm-Tn}$.
On the other axis interchange the coordinates. The bound only
decreases when $m\ge n$, since $T>r$. Take $\ell=0$ or $1$
of the correct parity for the matching lower bound. The axis lemma
and the second interior lower estimate, summed over $\Theta(\sqrt n)$
central times, give $c n^{-3/2}e^{-rm-Tn}$.

At $g=0$ the weight in (5) is independent of $\ell$. At fixed
duration $j$, equation (2) bounds the sum of the constrained
endpoint masses over $\ell\ge0$ by
$$
 \frac{C}{j}\Pr_\theta(S^Y_j=n)
                \bigl(1+\sqrt j+|n-v_yj|\bigr).
$$
Indeed, the conditional variance of $S^X_j$ is at most $j$
and its conditional mean given $S^Y_j=n$ is a fixed constant
times $n-v_yj$, by binary regression and zero horizontal drift.
In the vertical potential measure the sum over $j$ of
$\Pr_\theta(S^Y_j=n)|n-v_yj|$ is $O(\sqrt n)$. To see this,
the first hitting time of $n$ is a sum of $n$ iid one-level
ladder durations with mean $1/v_y$ and finite variance. Convolve
its distribution with the return potential at zero, whose time
weights have an exponential tail by positive drift. Since $j\ge n$,
the upper bound after summation is $C n^{-1/2}e^{-rm-Tn}$.
The exchanged-axis bound again suffices. For the lower bound sum
over $\sqrt n\le\ell\le2\sqrt n$ of the proper parity. Each such
$\ell$ contributes at least $c(\ell+1)n^{-3/2}e^{-rm-Tn}$
by the second interior lower estimate. This proves the table.

Parity restricts the interior segments to one time class and one
axis-height class. The permitted mixed steps at a reflecting face
supply the required initial parity. All sums over windows of
order $\sqrt n$ preserve their stated orders.

## The leading constant at independence

At $\kappa=0$ the same constant works for every fixed aspect ratio.
Writing $\rho=q/p$ and $C_j=\binom{2j}{j}/(j+1)$ gives

$$
 h_{m,n}\sim \rho^{m+n}
 \frac{(1-\rho)^2}{\displaystyle\sum_{j=0}^\infty
                    C_j^2(pq)^{2j}}.
$$

Indeed, the independent reflected coordinates are reversible under
their product geometric law. Reverse every successful excursion
between the origin and the upper corner, including its first and
last steps. The probability of the forward path is $\rho^{m+n}$
times that of the reversed path. The reverse event starts at the
upper corner, reaches the origin, avoids overflow, and avoids a
positive return to the upper corner before reaching the origin.

Measure each reversed coordinate downward from its upper ceiling.
Its raw increments have positive mean $\delta$. In the first
$L=\lfloor n/3\rfloor$ steps, neither coordinate can reach its
distant reflecting edge. The two raw sums therefore describe all
admissible paths over these steps. With probability
$1-O(e^{-c n})$ both sums at time $L$ are at least $\delta L/2$.
From such positions the two free positive-drift walks have probability
$O(e^{-c' n})$ of ever reaching either near edge. For the finite
walk, the probability of reaching the deep pair before a return
to the near edges also tends to one. Here are uniform bounds for
this last statement.

In the original deficit coordinates its two starting values are
$x\le m-\delta L/2$ and $y\le n-\delta L/2$. For any deterministic
time $j$, iterating the one-coordinate reflection formula gives
$\Pr_x(X_j\ge m)\le \rho^{m-x}+\rho^m$. The first term bounds the
initial position plus the full sum, and the second bounds the maximum
of all terminal suffix sums by reversal and gambler's ruin. There
is an identical vertical bound. Thus the chance of reaching either
near edge in $O(n^2)$ rounds is exponentially small. From any state
inside the rectangle, the unrestricted reflected process has probability
at least $c_0>0$ of being at the deep origin after $Bn$ rounds for
sufficiently large fixed $B$. Couple it to a chain started at zero
with the same increments. Each coordinate coalesces as soon as
the larger process hits zero, which occurs by time $Bn$ except with
exponentially small probability by negative drift. The chain started
at zero is stochastically dominated by the stationary product
geometric law, and hence is at the origin with probability at least
$(1-\rho)^2$ at every time. Iterating blocks proves that the
probability of avoiding both a stopping event and the deep pair for
$O(n^2)$ rounds is exponentially small.

It follows that the reversed committor tends to the probability
$\alpha$ that two independent free positive-drift walks started at
zero both stay nonnegative forever and never jointly revisit zero.
The probability of joint survival is $(1-\rho)^2$. Decomposing
survival at the last joint visit to zero gives
$(1-\rho)^2=G_{00}\alpha$. At time $2j$ a one-dimensional walk
killed below zero returns to zero with probability $C_j(pq)^j$,
by the reflection principle. Independence gives the stated sum for
$G_{00}$. The ratio of successive summands is at most $(4pq)^2<1$,
which also bounds the truncation error geometrically. At $p=0.7$,
512 terms certify the first 60 decimal places of
$0.3094171908279124734941549399526586847723850474581558640869787\ldots$.

## Repeated attempts, simultaneous flips and the first exit time

Starting at the deepest pair, the committor with repeated attempts
before the first overflow is different from $h_{m,n}$. Let
$b_{m,n}$ be the chance of **either** a corner visit or an overflow
during one origin excursion. Then $b_{m,n}=\Theta(e^{-rn})$.
For the lower bound follow the shorter coordinate on an excursion
from 1 to $n+1$ before it returns to zero. Its gambler's-ruin
probability, including its first upward step, has this order. Reaching
the other stopping set earlier is also a success for $b_{m,n}$.
For the upper bound, an unbounded excursion must visit a state
with $X\ge m$ or $Y\ge n$. Sum the two geometric stationary
marginals in the occupation formula. Regeneration now gives
$$
 \Pr_{(0,0)}\{\hbox{corner before either overflow}\}
        ={h_{m,n}}/{b_{m,n}}
        =\Theta\!\left(n^\beta e^{-n(E-r)}\right)
$$
for the nondegenerate table.

If both players must stay strictly below their shallow levels until they first
reach $(m,n)$ together, the immediately preceding state must be $(m-1,n-1)$.
Reaching that predecessor before either shallow level or the excursion's end
has probability $h_{m-1,n-1}$. An immediate joint loss then suffices.
The stricter per-excursion probability lies between
$a h_{m-1,n-1}$ and $h_{m-1,n-1}$ for $m,n\ge2$. Thus the exponent and
power in the table also apply to this convention whenever $a>0$.

For the linear automaton $L$, a simultaneous first flip requires
a visit to the preflip corner followed by a joint loss. The probability
per excursion of doing this before an earlier flip lies between
$a h_{m,n}$ and $h_{m,n}$. The probability per excursion of any
flip is $\Theta(e^{-rn})$, by the same marginal and gambler's-ruin
bounds with overflow barriers. Regeneration gives the same $E-r$
and $\beta$ for a simultaneous first flip. The mean time from the
deep pair to the first flip of either coordinate is
$\Theta(e^{rn})$. In fact the mean duration of an excursion
truncated by an overflow tends to the finite positive mean return
time, and the renewal equation divides this duration by the per-cycle
exit probability. These assertions about the **first** profile exit
use only the frozen outcome law. Stationary game odds also require
the evolution after that exit. Randomized boundary retention in a
$B$ automaton changes the killing rule.

## Positive and zero deficit drift

The same stopped event also has a sharp form for $0<p<1/2$.
The feasible lower endpoint is now $-p/q$. For
$-p/q\le\kappa<1$ and fixed $\gamma\ge1$,

$$
       h_{m,n}=\Theta\!\left(n^{-1/2}e^{-nH(\gamma,1)}\right).
$$

Use the same $M$, $H$ and radical expression above. In particular
$H(1,1)=0$. On every unequal ray $H(\gamma,1)>0$ by strict convexity
and the fact that the outward normal at $(0,0)$ is parallel to $(1,1)$.
The support point $(s,t)$ has $s\ge0,\ t\le0$, with both inequalities
strict at $\gamma>1$. This follows by varying the supporting normal
from $(1,1)$ toward the horizontal. Its two tilted drifts are positive.
At $\kappa=-p/q$, $d=0$ and the remaining three steps are noncollinear.
The positive-quadrant support point is still finite, as the radical
formula with $a,b>0,d=0$ also shows.

For the upper bound let the original reflected walk run without
upper ceilings. Its horizontal marginal now has positive drift.
The expected total number of visits to $X=0$ is finite, since after
each visit there is probability at least $q(1-p/q)>0$ of permanent
departure. The weighted occupation of the other axis satisfies

$$
  \sum_{j\ge0}\mathbb E[e^{sX_j}\mathbf1_{\{Y_j=0\}}]
  \ \le\ \left(\sum_{i\ge0}\Pr(X_i=0)\right)
           \left(1+\sum_{h\ge1}\Pr_{s,t}(S^Y_h\le0)\right)<\infty .
$$

Indeed, on a path with $X_j>0$, split at its last $X_i=0$. There is
no subsequent horizontal reflection, and terminal $Y_j=0$ forces
the unreflected vertical increment over that segment to be nonpositive.
The tilt removes $e^{sX_j}$, leaving $e^{-tS^Y_h}\le1$. The sum on
$h$ converges exponentially by the positive tilted vertical drift.
For last visits to $X=0$ their other weight $e^{tY_i}$ is at most one.
Consequently the last-axis decomposition and (1), used in both
coordinate directions, give the claimed upper bound. The positive
interior bridge lower bound applies from the origin, or after one
mixed step to select parity. When $d=0$, conditional on the group of
positive vertical increments, the horizontal signs in this group
still have nonzero binomial variance. Whenever the vertical sum is
nonnegative, the group has at least half the trials. In the central
range both groups have order $j$ trials and the nonconstant group
alone yields the local lower bound. Global $C/j$ point bounds
follow by treating an atypically small positive group with an
exponential tail. These observations justify the same bridge
estimates at the endpoint. Both fixed initial and final $(1,1)$
strings still have positive probability.

The chance per excursion of reaching a corner or an overflow is
bounded below by $q-p$, by letting the shorter coordinate start
an excursion that never returns to zero. Consequently a simultaneous
first flip has the same exponential rate and power as $h_{m,n}$.
The mean time to any flip is $\Theta(n)$. It is at least $n$ by
bounded speed and at most $(n+1)/(q-p)$ by comparison of the shorter
coordinate with its unreflected positive-drift walk.

At $p=q=1/2,\ -1<\kappa<1$, the logarithmic rate of $h_{m,n}$ is
zero on every fixed positive ray. Indeed, the covariance matrix at
zero tilt is nonsingular. For any sufficiently small $\epsilon>0$
choose a tilt $\theta_\epsilon$ whose mean is
$\epsilon(\gamma,1)$ by local inversion of $\nabla\log M$.
Under this tilt the positive interior bridge estimate applies at
times $n/\epsilon+O(\sqrt n)$. The likelihood in the original
measure is $e^{-\theta_\epsilon\cdot(m,n)}M(\theta_\epsilon)^j$,
with $M(\theta_\epsilon)\ge1$ by Jensen's inequality. A possible
initial parity correction changes this estimate by a fixed constant.
Letting $\theta_\epsilon\to0$ proves the assertion. The corresponding
first-flip probability has the same zero exponential rate. The mean
time to the first flip is $\Theta(n^2)$. The one-coordinate recursion
gives $(n+1)(n+2)$ as the mean time to the shorter overflow. In the
other direction, every reflected height through time $j$ is bounded
by twice the running absolute maximum of its free sum. The $L^2$
maximal inequality and a union bound give a probability below $1/2$
of either overflow by time $c n^2$, for a sufficiently small $c>0$.
For independent fair rewards, a two-point Green function gives the exact equivalent $C(\gamma)/(n^2\log n)$, with an elliptic shape factor and different leading constants for L and B. The power for nonzero interior correlations at fair rewards remains open. [Neutral independent corner](phase1_fair_corner.md)

At $\kappa=1$ the corner requires equal barriers. For $m=n$ and
$p<1/2$ its committor is $q((p/q)-1)/((p/q)^n-1)\to q-p$.
For $m=n$ and $p=q=1/2$ it is $1/(2n)$. At $p=q=1/2,\ \kappa=-1$
the missing joint loss makes the corner unreachable as in the
endpoint argument above.

## Finite-rectangle checks

The script builds the Dirichlet system directly from the four
increments and the stopping sets. It eliminates interior states by
positive arithmetic on Decimal transition probabilities. Each
pivot normalizes its off-diagonal transfers, redirects incoming paths,
and preserves the two absorbing outcomes. Equal barriers permit
lumping by coordinate exchange. A second solve at higher precision
supplies trial values for an outward-rounded interval residual.
From every transient state, a block of $m+1$ consecutive joint wins
or a block of $m+1$ consecutive joint losses gives absorption.
Independent blocks imply
$\|(I-Q)^{-1}\|_\infty\le (m+1)/\max(a,d)^{m+1}$. Multiplying this bound by the
maximum interval residual encloses the committor error. The program
prints both endpoints of the resulting enclosure.

The entries below are $h_{m,n}e^{nE}/n^\beta$ at $p=0.7$, computed
with 60-digit Decimal state elimination. Every $n=40$ committor in
this table was also enclosed to at least 60 relative decimal digits.

| $\kappa$ | $\gamma$ | $E$ | $\beta$ | $n=20$ | $n=40$ | $n=80$ |
|---:|---:|---:|---:|---:|---:|---:|
| $0.5$ | 1 | 1.1155618470 | $-1/2$ | 0.331953 | 0.317394 | 0.310266 |
| $0$ | 1 | 1.6945957208 | 0 | 0.309417 | 0.309417 | 0.309417 |
| $-0.12$ | 1 | 1.9352717509 | 0 | 0.525931 | 0.584905 | 0.616826 |
| $\kappa_0$ | 1 | 2.2393769454 | $-1/2$ | 1.131219 | 1.144706 | 1.146877 |
| $-0.38$ | 1 | 2.8418174312 | $-3/2$ | 3.507153 | 3.824454 | 4.019633 |
| $0.2$ | 3 | 3.0314418065 | 0 | 0.153730 | 0.153804 | 0.156318 |
| $0.8$ | 3 | 2.6249795394 | $-1/2$ | 0.026284 | 0.027955 | 0.028918 |


Run the following command in the study directory with Python and mpmath.

```sh
python3 -B experiments/phase1_quadrant.py --sizes 20 40 80 --verify-size 40 --digits 60 --catalan-terms 512
```

For an example below the binary64 range, take $p=1-10^{-20}$,
$\kappa=\kappa_0$, and $m=n=10$. The certified committor is
approximately $5.0300000000000000010478\times10^{-598}$.

At $p=0.3,\ \kappa=-3/7,\ \gamma=2$, the three-step endpoint law
gives $E=0.054371212257424\ldots$. The rescaled values at
$n=20,40,80$ are $0.0745716,\ 0.0704803,\ 0.0685647$.
At $p=0.5,\ \kappa=0.5,\ \gamma=1$ the corresponding values of
$-\log(h_{n,n})/n$ are $0.318419,\ 0.194158,\ 0.114584$.
Both $n=40$ committors were also enclosed to 60 relative digits.

## Related work

Kobayashi and Miyazawa analyze stationary probabilities on reflecting
quarter-plane axes and stationary marginal tails. Kurkova and Raschel
derive Green function asymptotics for homogeneous walks absorbed at the
axes. Here the lower axes reflect, the two upper sides bound an excursion,
and the specified target is their common corner. [Kobayashi and Miyazawa
(2012)](https://arxiv.org/abs/1201.3167) · [Kurkova and Raschel
(2011)](https://www.numdam.org/articles/10.24033/bsmf.2611/)
