# The finite-memory Stag Hunt on both sides of a fair solo hunt

Two hunters with hare success $P=T=0.80$, solo-stag success $S=0.49$,
and joint-stag success $R=0.9385$ hunt stag together **35.99%** of the
time at depth one, **81.82%** at depth sixteen, and **1.04%** at depth
160. The three stationary probabilities are $0.359886336596$,
$0.818212119577$, and $0.010354095442$. The geometric factor in this
game tends to $51/2$, and the odds have exponential base $1877/1968<1$.

With the same hare success, every game in the open rectangle
$$
              0.47<S<0.50,\qquad 0.94<R<16/17
$$
has mutual-stag frequency below $37.5\%$ at depth one, above $80\%$ at
depth sixteen, and tending to zero as memory grows. A second open region
crosses $S=0.55$ and has the same rise by depth eighteen. If both payoffs
approach the fair critical point, the peak can approach $100\%$ from
either side of $S=1/2$.

## The phase boundary

Both players use the synchronous linear tactic $L_{2n,2}$ with equal
finite depth $n$. Feedback is independent between players conditional on
the action profile, with fresh draws each round. Mutual stag pays success
probability $R$ to each hunter, solo stag pays $S$, and hare always pays
$P$. Assume $0<S<P<R<1$ and $P>1/2$. Let $p_n=\pi_n(CC)$ and
$$
 U_n=\frac{p_n}{1-p_n},\qquad \rho_t=\frac{1-t}{t},\qquad
 a=\frac{S}{1-S},\qquad \lambda=\frac{\rho_P^2}{\rho_R},\qquad
 G_n=\sum_{j=0}^{n-1}a^j .
$$
A cooperator playing alone takes a one-step walk in depth. Its stationary
depth weights in the outside reference chain are proportional to $a^j$.
Their sum $G_n$ counts the weighted opportunities for the other player to
join. The two-sided order theorem gives $U_n\asymp G_n\lambda^n$. For
$S\geq 1/2$ it also gives the equivalent $U_n\sim K G_n\lambda^n$, with
$$
                    K=K(R,P,S)=\frac{(2P-1)^2}{(1-S)(2R-1)} .
$$
The theorem and the excursion proof are in the [constant-hare study](phase1_reversal.md).

| Solo stag | Depth factor | Exponential base of the odds | Behavior at base one |
|---|---|---|---|
| $S<1/2$ | $G_n=(1-a^n)/(1-a)\to(1-S)/(1-2S)$ | $\lambda$ | $U_n=\Theta(1)$ |
| $S=1/2$ | $G_n=n$ | $\lambda$ | $1-p_n\sim 1/(Kn)$ |
| $S>1/2$ | $G_n=(a^n-1)/(a-1)\sim a^n/(a-1)$ | $a\lambda$ | $p_n\to K/(K+a-1)$ |

In the last row, $1/(a-1)=(1-S)/(2S-1)$, giving $S/(2S-1)$ as the
coefficient of $a^{n-1}$. The critical mutual-stag payoff is
$$
 R_c(P,S)=\frac{P^2}{P^2+(1-P)^2\max(1,a)}.
$$
At $S>1/2$ this equals
$P^2(1-S)/[P^2(1-S)+(1-P)^2 S]$. In all three rows $p_n\to0$ for
$R<R_c$ and $p_n\to1$ for $R>R_c$, by the sign of the exponential
rate. For fixed $S<1/2$ the exact constant at criticality is open here.
For $P=4/5,\ S=0.55$, $R_c=144/155$, $K(R_c,P,S)=124/133$, and the
critical limiting probability is $558/691$, about $80.75\%$.

For each fixed $S\ne1/2$, the peaks stay bounded away from one as
$R\uparrow R_c(P,S)$. The upper order bound is uniform for $R$ in a
compact neighborhood of $R_c$ at fixed $P,S$. On its subcritical side
$G_n\lambda^n\le 1/(1-a)$ if $a<1$, and
$G_n\lambda^n\le 1/(a-1)$ if $a>1$. These bounds hold at every depth.

## Finite-depth bounds on open regions

**Monotonicity.** Whenever $1-P\le S\le R$, $p_n$ is nondecreasing
in $S,R$ at fixed $P,n$, within this range. Order each player's levels
from deepest hare to deepest stag. The probability of a step toward stag
is $1-P$ on the hare half, $S$ at solo stag and $R$ at mutual stag.
It is nondecreasing in both players' levels and both parameters. Use the
same independent pair of uniform random numbers to update two ordered
copies. A step toward stag in the lower copy forces such a step in the upper
copy for the same player. Reflection at either deepest level preserves the
order. This couples all times. Every finite chain is irreducible and
aperiodic. Each coordinate can be steered to deepest hare and held there
while steering its partner, and from that corner one may delay either
coordinate before steering it to any intended level. All required feedback
patterns have positive probability. The increasing event $CC$ therefore
inherits the ordering in stationarity.

For $P=4/5$, put $\sigma(r)=16(1-r)/(16(1-r)+r)$. Each table row
gives a region
$$
              S_0<S<S_1,\qquad R_0<R<R_c(4/5,S).
$$
Throughout it $p_1<3/8,\ p_m>4/5,\ p_n\to0$. In particular the global
finite-memory maximum is at least $p_m$. The stated depth $m$ is a
witness, and other depths may give larger probabilities.

| $S_0$ | $R_0$ | $S_1$ | $m$ | $p_m(S_0,R_0)$ | Upper bound on $p_1$ |
|---:|---:|---:|---:|---:|---:|
| $0.47$ | $0.94$ | $1/2$ | 16 | 0.803242363556 | $3757/10042$ |
| $0.52$ | $0.935$ | $208/395=\sigma(0.935)$ | 10 | 0.812762631556 | $220211/597796$ |
| $0.5499$ | $0.929$ | $1136/2065=\sigma(0.929)$ | 18 | 0.800865084694 | $9854063369/27894660164$ |

For the lower bound, compute the stationary value at the lower corner
with exact rational arithmetic, then apply monotonicity. The depth-one
upper bound uses the upper comparison parameters $(S_1,R_c(4/5,S_0))$
and the three-state tree formula. The zero limit follows from the strict
upper bound on $R$. The JSON contains the numerator and denominator of
each lower-corner value, including the depth-18 certificate.

The same comparison applied to the opening example gives
$p_{16}>0.8182$ throughout $0.49<S<1/2,\ 0.9385<R<16/17$,
with the same upper bound $3757/10042$ at depth one and the same zero
limit. Here the lower corner uses the certified stationary interval.

At $R=0.94$ the grid gives $p_6=0.5162059839$ for $S=0.35$ and
$p_8=0.6103936637$ for $S=0.40$. At $S=0.45$ the depth-one
probability is $500/1433$ and the
depth-twelve probability is $0.7375177941$. At $S=0.48$ with the **same**
$R$, depth one gives $0.3612553624$ and depth twenty gives
$0.8410506141$. Above fairness, $S=0.55,\ R=0.928$ gives $0.34994401$
at depth one and $0.76003453$ at depth twelve. Moving to $R=0.929$
gives $0.35302574$ at depth one and $0.80485418$ at depth thirty.
For favorable solo stag the finite-depth factor is a difference of exponentials,
$G_n\lambda^n=((a\lambda)^n-\lambda^n)/(a-1)$. In this last game the
faster base is $\lambda=929/1136$ and the slower base is $10219/10224$.
The slow term takes about 2,044 additional depth levels to fall by a factor
of $e$. Each of these games has limiting probability zero.

## Approaching fairness from either side

**Two-parameter peak law.** Fix $P\in(1/2,1)$, put $R_*=R_c(P,1/2)$
and $K_*=K(R_*,P,1/2)$. Take any sequence of games indexed by $j$ with
$$
 R_j\to R_*,\quad \delta_j=-\log\lambda(R_j)>0,\quad
 S_j\to1/2,\quad b_j=\frac{\log(S_j/(1-S_j))}{\delta_j}\to b<1 .
$$
Write $U_{j,n}$ for the odds. If $\delta_j n_j\to x\in(0,\infty)$,
then
$$
 \frac{\delta_j U_{j,n_j}}{K_*}\longrightarrow
 g_b(x)=e^{-x}\int_0^x e^{bt}\,dt
 =\begin{cases}(e^{-(1-b)x}-e^{-x})/b,&b\ne0,\\
                xe^{-x},&b=0.\end{cases}
$$
Every sufficiently late game is subcritical and hence has a maximizing
finite depth $m_j$. Every choice of maximizer satisfies
$$
 \delta_jm_j\to x_b,\qquad
 1-\max_n p_{j,n}\sim\frac{\delta_j}{K_*g_b(x_b)},\qquad
 x_b=\begin{cases}-\log(1-b)/b,& b\ne0,\\1,& b=0.\end{cases}
$$
In particular $1-\max p_{j,n}\sim e\delta_j/K_*$ on the fair line.
Positive $b<1$ and negative $b$ give arbitrarily high peaks in
subcritical games strictly above and strictly below fair solo success.

**Uniform excursion estimate.** We record why the leading constant also
applies in this joint limit from below. For any sequence $n\to\infty$,
$S_n\to1/2$, $R_n\to R'\in(P,1)$, we claim
$$
            U_n\sim K(R_n,P,S_n)\,G_n\lambda_n^n.                 \tag{1}
$$
In the independent outside reference chain let
$$
 Z_n=\frac{1-\rho_P^n}{1-\rho_P}+
             \frac{P\rho_P^nG_n}{1-S_n},\quad f=P\rho_P^n/Z_n .
$$
The stationary one-step flux entering $CC$ equals
$F=f^2(2G_n/(1-S_n)-1)$. In the inside reflected reference a mark is
a penalty at a shallow boundary for either player. Its flux is
$F_C=c(2-c)$, $c=(2R_n-1)\rho_{R_n}^n/(1-\rho_{R_n}^n)$.

Choose $A\ge1$ with $a_n\le A<1/\rho_P$ eventually, and keep $R_n$
in a compact subinterval of $(P,1)$. The outside return blocks in the
constant-hare proof can all have length $H_n=O(n^2 A^n)$. Indeed the
solo-stag mean crossing time is at most $n^2 A^n/(1-S_n)$, the chance
of reaching deepest hare from shallow hare before switching is at least
$1-\rho_P$, and the probability of switching again from deepest hare
within $nH_n$ steps is $O(nH_n\rho_P^n)=o(1)$. The one-coordinate
stationary weight of deepest hare stays bounded below since
$G_n\le n A^n$ and $Z_n\to1/(1-\rho_P)$. Reversibility bounds return
probabilities at even times below by that weight, and a deepest-level hold
handles odd times. Thus the positive probability of hitting deepest $DD$
before $CC$ per outside block is uniform. The inside bounds use $O(n^2)$
blocks, with $R_n$ bounded away from $1/2$ and 1. In particular
$H_nF\to0$ and $n^2F_C\to0$.

For every fixed $M$, $\liminf G_n\ge M$ by keeping its first $M$
summands. Hence $G_n\to\infty$, even when $S_n<1/2$. Simultaneous
switches account for $f^2=o(F)$ at entrance. Entry flux with a resident
stag hunter of bounded depth is $O_M(f^2)=o(F)$ by the geometric depth
weights. At a typical inside mark the other hunter also has diverging depth,
since its distance from deepest stag has a uniformly geometric tail.

These two estimates give the same corner-cycle flux calculation on each
sequence. In reverse time, the shallow hare at a typical entry reaches
deepest $DD$ before $CC$ with probability $1-\rho_P+o(1)$. The
shallow stag at a typical mark reaches deepest $CC$ before another mark
with probability $1-\rho_{R_n}+o(1)$. To see this, run the shallow
player for a diverging number of steps smaller than the resident depth.
Its chance of surviving and acquiring diverging depth tends to the
half-line survival probability. The uniform return blocks above then
give the asserted corner hit. After a crossing, the focal infinite
two-sided ladder escapes to stag with probabilities
$$
 h_C=\frac{1-\rho_{R_n}}{1-\rho_{R_n}\rho_P},\qquad h_D=\rho_P h_C
$$
from shallow stag and hare respectively. For uniformity in $R_n$, first
stop at depth $M$ on either side, use a uniform geometric tail for this
finite stopping problem, then bound a return to
the interface by $\max(\rho_P,\sup_n\rho_{R_n})^{M+1}$.

The two-state trace balances its two directed crossing fluxes. The
transmission factors cancel because
$(1-\rho_P)h_C=(1-\rho_{R_n})(1-h_D)$.
The stationary corner masses conditional on being outside and inside are
asymptotic to their reference masses. Indeed, truncating a reference
return cycle at its first entry or mark discards respectively
$O(H_n)$ or $O(n^2)$ expected steps on a successful cycle, versus
total times through that first success of order $1/F$ or $1/F_C$.
These comparisons apply uniformly to the initial truncated piece of a
spell using the positive probability to reach the appropriate corner.
Consequently $U_n\sim F/F_C$. Substituting the displayed fluxes proves
(1). The return-cycle identities used here are given with their
normalizations in the [constant-hare proof](phase1_reversal.md).

**Maximizing the limit.** We have
$\delta_j G_{n_j}=\delta_j\sum_{k<n_j}\exp(b_j\delta_j k)
\to\int_0^x e^{bt}\,dt$, a Riemann sum. Equation (1) gives the limit
profile. The eventual inequality $b_j<1$ gives subcriticality.
Evaluating at the nearest depth to $1/\delta_j$ yields odds of order
$1/\delta_j$. Thus a maximizing depth diverges, since at any fixed
depth the finite-chain law is continuous and strictly between zero and
one. For $x=\delta_jn$,
$$
   \delta_jG_n\lambda_j^n\le x\exp[-(1-\max(0,b_j))x].
$$
This tends to zero if $x\to0$ or $x\to\infty$, so (1) keeps the
scaled maximizers in a compact subinterval of $(0,\infty)$. The unique
maximizer of $g_b$ is $x_b$ by differentiation. Applying the profile
limit along subsequences proves both peak statements.

## Numerical data

The data combine 368 distinct finite-chain solves. The main grid has 22
subcritical $(S,R)$ curves. Other arrays give the
four critical contacts, stationary samples of the fair master curve, and
two rational parameter pairs on each of the paths
$\log(a)/\delta=\pm1/2$. For the last paths use $v=49/50,99/100$,
$\lambda=v^2$, with $a=v$ giving $b=-1/2$ and $a=1/v$ giving $b=+1/2$. All displayed
stationary observations come from the finite game. The fair master-curve
ordinate is $\delta U_n/K_*$, with $K_*=102/125$ at $P=4/5$.
The analytic overlay $xe^{-x}$ is stored separately.

| Fair $S=1/2$, $R$ | $n$ | $x=\delta n$ | $\delta U_n/K_*$ from stationary masses | $xe^{-x}$ |
|---:|---:|---:|---:|---:|
| 0.9350 | 9 | 0.957865 | 0.367441247470 | 0.367543565331 |
| 0.9400 | 47 | 0.989510 | 0.367877427987 | 0.367859059223 |
| 0.9405 | 82 | 0.996578 | 0.367891660671 | 0.367877281867 |

Each reported stationary probability is rounded to 76 significant digits.
The solver checks them by evaluating the residual of a rational trial
solution to the Poisson equation in every state. For reward
$g={\bf1}_{CC}$ and transition kernel $Q$, the minimum and maximum
of $g+Qh-h$ enclose $\pi(g)$, since its stationary average equals
$\pi(g)$. Both endpoints must round to the same printed value. Rational
GTH also gives the three exact lower-corner fractions and an integer
determinant checks a separate depth-six value.
[Computation](../experiments/phase2b_staghunt_robustness.py) ·
[Full data](../experiments/data/phase2b_staghunt_grid.json)

~~~sh
python3 experiments/phase2b_staghunt_robustness.py --workers 2
~~~
