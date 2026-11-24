# A finite optimum for memory in a Stag Hunt

Two hunters independently receive binary feedback and both use Tsetlin's linear
tactic $L_{2n,2}$. A hare succeeds with probability $4/5$, whoever else joins.
A solo stag hunter succeeds with probability $1/2$. A joint stag hunt succeeds
with marginal probability $15/16$ for each hunter. The stationary frequency of
mutual stag hunting is 36.04% at memory 1, 82.30% at memory 16, and 0.43% at
memory 160. It tends to zero. The proof gives the power of $n$ multiplying the
exponential odds and also gives the worst-initial-state mixing scale.

## The cooperative fraction

Write $R$ for the success probability of a hunter at mutual stag $A=CC$,
$S$ for success at solo stag, and $P=T$ for the fixed probability of success
at hare. Assume $0<S<P<R<1$ and $P>1/2$. All feedback is independent across
players conditional on the current actions, with fresh draws each round. A reward
deepens the current action by one, up to depth $n-1$. A penalty shallows it by
one. A penalty at depth zero switches actions at depth zero.

Put
$$
 \rho_x=(1-x)/x,\quad G_n=\sum_{j=0}^{n-1}\left(\frac S{1-S}\right)^j,\quad
 \lambda=\frac{\rho_P^2}{\rho_R},\qquad U_n=\frac{\pi_n(A)}{1-\pi_n(A)} .
$$

**Theorem.** For constants $0<c<C<\infty$ independent of $n$,
$$
                  cG_n\lambda^n\ \le U_n\le\ C G_n\lambda^n.                 \tag{1}
$$
The constants may be taken uniform for $R$ in a compact subinterval of
$(P,1)$ with $S,P$ fixed. Consequently the sign of
$$
 \log\lambda+\max\{0,\log(S/(1-S))\}
$$
decides between convergence of $\pi_n(A)$ to one and to zero off the zero set.
On that set, $U_n=\Theta(1)$ for $S\ne1/2$, while
$1-\pi_n(A)=\Theta(1/n)$ for $S=1/2$.

For $1/2\le S<P$ the leading constant is explicit,
$$
 U_n\ \sim\ K(R,P,S)\,G_n\lambda^n,\qquad
 K(R,P,S)=\frac{(2P-1)^2}{(1-S)(2R-1)}.                                   \tag{2}
$$
At the critical equality this gives $1-\pi_n(A)\sim1/(Kn)$ for $S=1/2$.
For $S>1/2$ at criticality it gives
$\pi_n(A)\to K/(K+S/(1-S)-1)$.

**Arbitrarily high finite peaks.** Fix $P>1/2$ and $S=1/2$. The critical
joint-stag probability is $R_c=P^2/(P^2+(1-P)^2)$. For every $P<R<R_c$
the cooperative fraction tends to zero. As $R\uparrow R_c$, the largest
finite-memory cooperative fraction tends to one. More precisely, put
$\delta=-\log\lambda$. Every maximizing integer $n_*$ satisfies
$$
       \delta n_*\longrightarrow1,\qquad
       1-\max_n\pi_n(A)\sim\frac{e\,\delta}{K(R_c,P,1/2)}.
$$
Indeed, (1) bounds the odds above and below by constant multiples of
$n e^{-\delta n}$, uniformly near $R_c$. Evaluation at an integer nearest
$1/\delta$ gives odds of order $1/\delta$, the upper bound for all $n$.
At a maximizer, $x=\delta n_*$ therefore stays in a compact subset of
$(0,\infty)$. The uniform equivalent (2) gives
$\delta U_{n_*}=K(R_c,P,1/2)xe^{-x}+o(1)$. The unique maximum of
$xe^{-x}$ is $1/e$ at $x=1$, yielding the displayed constants.

## The two recurrence times

Let $D_*$ denote an individual at deepest hare. The product corner is
$z=(D_*,D_*)$. Define $w$ analogously at deepest stag. The following
argument proves (1).

**A product chain outside mutual stag.** Give each cooperator probability $S$
in every environment and each defector probability $P$. This reference chain
is a product of two reversible birth-and-death chains. It has exactly the
original transitions at every state outside $A$. Write $d$ for depth from
the switching boundary. The unnormalized stationary weights of one ladder are
$$
  m(D_d)=\rho_P^{n-1-d},\qquad
  m(C_d)=\frac{P\rho_P^n}{1-S}\left(\frac{S}{1-S}\right)^d ,
                  \qquad 0\le d<n.
$$
These follow by balancing each adjacent edge, including $C_0,D_0$. With
$Z=\sum m$ and $\mu=m/Z$, $Z$ is bounded above and below independently
of $n$, since $S<P$. The one-player stationary flux from $D$ to $C$
is $f=P\rho_P^n/Z$, and $u=\mu(C)=fG_n/(1-S)$. Independence gives the
exact stationary **entry** flux of the pair into $A$,
$$
   F=u^2-(u-f)^2
     = f^2\left(\frac{2G_n}{1-S}-1\right)
     \asymp G_n \rho_P^{2n}.                                                 \tag{3}
$$
For a fair solo hunt the multiplier in parentheses is $4n-1$.

**A uniformly likely return to deepest hare.** From every state outside $A$,
the reference chain has probability at least $\eta>0$ of reaching $z$
before $A$, in at most $H_n=K\lceil n^2\max(1,(S/(1-S))^n)\rceil$ steps.
Here $K$ is a sufficiently large constant. The details also control
solo hunts with positive drift.

1. On the stag half, write $E_j$ for the expected time to cross into hare
   from depth $j$, with $E_{-1}=0$. The reflected top gives
   $E_j-E_{j-1}=(1-S)^{-1}\sum_{k=0}^{n-1-j}(S/(1-S))^k$.
   Hence even from deepest stag the expected crossing time is at most
   $n^2\max(1,(S/(1-S))^n)/(1-S)$. On the hare half, a walk starting at its
   boundary has probability at least $1-\rho_P$ of reaching $D_*$ before
   switching, by gambler's ruin. The expected time to either boundary is at
   most $n/(2P-1)$ by the drift. Repeating the attempts shows that from any
   single level, $D_*$ is reached by time $H_n/2$ with probability at least
   $1/2$ for suitable $K$.
2. For every $t$, the probability of being at $D_*$ at time $t$ starting
   at $D_*$ is bounded below uniformly. At even times reversibility and
   Cauchy–Schwarz give $M^{2k}(D_*,D_*)\ge\mu(D_*)$. At odd times use the
   one-step hold of probability $P$. The strong Markov property therefore gives
   a uniformly positive probability of being at $D_*$ at time $H_n$ from
   any starting level.
3. One coordinate starts on hare. It reaches $D_*$ before switching and by
   time $H_n/2$ with probability bounded below, by the same gambler's-ruin
   and mean-time bounds. Starting from $D_*$, a switch within $H_n$ more
   steps has probability at most $H_n(1-P)\rho_P^{n-1}$. Indeed,
   $M^j(D_*,D_0)\le\mu(D_0)/\mu(D_*)=\rho_P^{n-1}$ by stationarity at each
   time $j$. This bound tends to zero because $S<P$. Subtracting it from
   the return bound in step 2 gives a positive probability of ending at $D_*$
   at time $H_n$ while staying on hare throughout. The second, independent
   coordinate also has a positive probability of being at $D_*$ at that time.
   The finitely many small $n$ can be absorbed into $\eta$. This proves the
   assertion.

In particular $H_n F\to0$, and repeated blocks bound the expected time to
hit either $A$ or $z$ from outside by $H_n/\eta$.

**Time to coordinate.** In the reference chain the mean return-cycle length at
$z$ is $1/\mu(D_*)^2=O(1)$. The expected number of entries into $A$ in
one such cycle is $F/\mu(D_*)^2$, by counting stationary edges over return
cycles. Given a first entry, the number of entries before returning to $z$
has mean at most $1/\eta$, since every exit has probability at least $\eta$
of reaching $z$ before the next entry. The probability of a successful cycle
is therefore comparable to $F$. Independent return cycles give
$\mathbb E_z\tau_A=O(1/F)$ by summing cycle lengths through the first success.
The reverse bound follows directly from
$\Pr_z(\tau_A\le t)\le t F/\mu(D_*)^2$, since each specified entrance
edge-time has at most its stationary probability divided by $\mu(D_*)^2$.
From any outside state, the uniformly likely visit to $z$ gives the same
lower bound. The time to hit $A$ or $z$, followed if necessary by an
attempt from $z$, gives the matching upper bound. Thus the true mean time to
the next $CC$ from **every** outside state is $\Theta(F^{-1})$.

The stationary fraction of mixed states conditional on being outside $A$
also tends to zero. In a reference return cycle at $z$, the mean mixed-state
occupation is $2u(1-u)/\mu(D_*)^2$. Summing whole cycles through the first
successful one bounds it by $O(u/F)$ before reaching $A$ from $z$.
From any other outside state add at most $O(H_n)$ for reaching $A$ or
$z$. Division by the outside mean gives $O(u+H_nF)=o(1)$. In particular
the zero-cooperation regime converges to mutual hare, and its mean individual
success probability tends to $P$.

**Time inside mutual stag.** Until the first switch, two independent
reflected walks on the $C$ half use success probability $R$. The mean
crossing time from deepest stag for one of them is exactly
$$
       \frac{R}{(2R-1)^2}\big(\rho_R^{-n}-1\big)-\frac{n}{2R-1},
$$
by the increment recurrence of step 1. This bounds the time until the first
of either player's switches from above. From any pair of stag levels, each
coordinate can reach deepest stag, remain on stag and be at its deepest level
at a common time $Kn^2$, with uniformly positive probability. The proof is
steps 2–3 applied to the reflecting stag half with success $R$, counting an
attempted outward crossing at the shallow boundary as failure. Once both are
deep, the probability of an exit by time $t$ is at most
$2t(1-R)\rho_R^{n-1}$, by the stationary edge bound for the walk reflected
at both ends. Thus every mean spell inside $A$ is $\Theta(\rho_R^{-n})$.
Taking the ratio of the mean inside and outside spell lengths under stationary
entrance and exit distributions proves (1). All success probabilities and
estimates involving $R$ above are uniform on the stated compact sets.

## The leading coefficient when the solo hunt is fair or favorable

Suppose $S\ge1/2$, so $G_n\to\infty$. Besides the outside product
reference $\nu_D=\mu^{\otimes2}$, use a reference on $A$ consisting of
two $R$-walks reflected at both ends of their stag halves. Its stationary
law is $\nu_C$. Mark a step whenever either individual at the shallow
boundary receives a penalty. In this reference the shallow penalty holds the
coordinate in place. In the game its first occurrence exits $A$. The
stationary mark flux is
$$
 F_C=1-(1-f_C)^2,\qquad
 f_C=(1-R)\frac{(1-\rho_R)\rho_R^{n-1}}{1-\rho_R^n}
     =\frac{(2R-1)\rho_R^n}{1-\rho_R^n}.
$$
We prove $U_n\sim F/F_C$.

**A deep resident at a crossing.** In the stationary outside reference,
all but $o(F)$ of the flux entering $A$ has one newcomer at depth zero
and a resident stag hunter whose depth tends to infinity in probability.
Simultaneous switches contribute $f^2=o(F)$. Crossings involving a resident
at depth bounded by any fixed $j$ have flux $O_j(f^2)$, by the displayed
ladder weights. Resident depth changes by at most one per step. Similarly,
all but $o(F_C)$ of the inside reference mark flux has just one marked
player, and the depth of the other tends to infinity. Its reflected equilibrium
is geometric in distance from the deepest stag level.

Two starting configurations account for the probabilities below. If both stag
depths tend to infinity, the chance of hitting $w$ before any exit tends
to one. For an initial depth $d$, switching before first reaching deepest
stag has probability at most $\rho_R^{d+1}$. Afterward the chance of a
switch in $n^3$ steps is $O(n^3\rho_R^n)$. Meanwhile the independently
reflected pair hits $w$ with probability tending to one within $n^3$
steps by repeated $O(n^2)$ blocks. If a hare hunter's depth tends to
infinity, it reaches $z$ with its partner before an entry into $A$ with
probability tending to one. The analogous bound on its switch by time
$nH_n$ is $\rho_P^{d+1}+O(nH_n\rho_P^n)=o(1)$, and the outside product
hits $z$ within that time with probability tending to one by the block bound.

Let $d_n$ be the chance from $z$ to enter $A$ before the next visit to
$z$. Reverse stationary entry edges in the reversible outside reference.
An edge $y\to x$ with $y\notin A,\ x\in A$ is the first entry of a
successful $z$-cycle precisely when, traced backward from $y$, the path
hits $z$ before $A$. Consequently $\nu_D(z)d_n$ is the sum of the
stationary entry-edge fluxes weighted by these backward probabilities. At
a typical edge $y$ has a shallow hare player and a resident stag hunter
of diverging depth. The probability of hitting $z$ before $A$ tends
to $1-\rho_P$. Indeed, run the shallow player's biased walk for a
diverging number of steps less than the resident's depth. Its probability of
avoiding a switch and acquiring diverging depth tends to $1-\rho_P$, its
infinite-half-line survival probability. The preceding deep-hare bound then
applies. Thus $\nu_D(z)d_n\sim F(1-\rho_P)$.

Let $c_n$ be the chance, starting from $w$, of a mark before the next
visit to $w$. The same backward-edge count gives
$\nu_C(w)c_n\sim F_C(1-\rho_R)$. Here a marked transition reverses to a
marked transition. For $n\ge2$, each marked coordinate holds at depth zero
and the other coordinate satisfies single-ladder detailed balance. From the
typical pre-mark state the probability of reaching $w$ before another mark
tends to $1-\rho_R$, by the corresponding half-line survival and deep-stag
bounds. In both backward counts the weights are at most one and the
successful-cycle flux is comparable to the total flux. The first crossing in
a successful cycle consequently also has a shallow newcomer and a resident
of diverging depth.

**Transmission between corners.** With a resident stag hunter of diverging
depth $j$, follow the other, shallow player for $\lfloor\sqrt j\rfloor$
steps. The resident stays on stag throughout, and the shallow player cannot reach
either deepest reflecting boundary. Its law during this interval agrees
exactly with the infinite ladder where the outward probabilities on the
stag and hare halves are respectively $R,P>1/2$. This ladder escapes to
one of its two infinite ends almost surely. Each boundary visit offers a
positive chance of permanent departure to the current end. If $h_C,h_D$
are the probabilities of escaping to the stag end from shallow stag or hare,
gambler's ruin gives
$$
 h_C=1-\rho_R+\rho_Rh_D,\qquad h_D=\rho_P h_C .
$$
At the end of the interval the focal depth diverges in probability on each
escape event, and the resident depth is at least $j-\sqrt j$. The deep
starting bounds prove that the chance of subsequently hitting $w$ before
$z$ tends to $h_C$ or $h_D$, according to the focal initial action.
In particular $h_C=(1-\rho_R)/(1-\rho_R\rho_P)$.

The two-state trace of the true game on $w,z$ balances its directed
crossing fluxes. Its probability of reaching $w$ from $z$ before a
return is $d_n(h_C+o(1))$. In the reverse direction it is
$c_n(1-h_D+o(1))$. Hence
$$
 \frac{\pi_n(w)}{\pi_n(z)}
 \sim \frac{F\,\nu_C(w)}{F_C\,\nu_D(z)}
       \frac{(1-\rho_P)h_C}{(1-\rho_R)(1-h_D)}
 =\frac{F\,\nu_C(w)}{F_C\,\nu_D(z)}.
$$

**Time normalization.** Conditional on being outside $A$, the true
stationary mass at $z$ is asymptotic to $\nu_D(z)$. From $z$ the number
of visits to $z$ before entering $A$, including the initial visit, has
mean $1/d_n$. The mean length of the reference cycles through the first
successful one is $1/(\nu_D(z)d_n)$. The portion after that first entry
has mean $O(H_n)$, by the uniform probability of reaching $z$ over a
reference block from any state. Thus stopping at the entry changes mean length
by $o(1/d_n)$. From an arbitrary outside state both leading means are
multiplied by the probability of hitting $z$ before $A$, bounded below
by $\eta$, with an initial extra time of $O(H_n)$. The ratio of occupation
to time is therefore asymptotic to $\nu_D(z)$ uniformly over initial
states. Likewise the true mass at $w$ conditional on $A$ is asymptotic
to $\nu_C(w)$. Use the reflected stag cycles through their first mark, for
which the discarded remainder to $w$ has mean $O(n^2)=o(1/c_n)$.
Taking the stationary corner ratio now gives $U_n\sim F/F_C$. Substitution
of (3), $Z\to1/(1-\rho_P)$ and the mark flux proves (2).

This proof also applies along every sequence $R_n\to R'\in(P,1)$. The
ruin probabilities and reflected bounds are uniform in a compact neighborhood
of $R'$. The escape probability of the infinite focal ladder by a diverging
time has the same uniform limit in the following sense. Stop it on first
reaching depth $m$ on either side. For fixed $m$ this finite hitting
time has a geometric tail uniformly on the compact set, and the probability
of returning to the boundary afterward is at most
$\max(\rho_P,\sup_R\rho_R)^{m+1}$. Taking $m$ large gives the asserted
uniformity and justifies the peak equivalent derived from (2).

## Worst-start total-variation mixing

**Theorem.** For the same labeled full chain, with threshold $1/4$,
$$
       t_{\rm mix}=\Theta\left(\min\left\{
                     \rho_R^{-n},\, \frac{\rho_P^{-2n}}{G_n}
                                      \right\}\right).                       \tag{4}
$$
In the defection regime, a direct wait from deepest hare for mutual stag
takes exponentially longer than worst-start mixing. At fair-solo criticality,
$t_{\rm mix}=\Theta(\rho_P^{-2n}/n)$.

Write $a=\rho_R^{-n}$ and $b=1/F$. Starting at $w$, the chance to leave
$A$ by time $t$ is $O(t/a)$. Starting at $z$, the chance to enter it
is $O(t/b)$. At a sufficiently small multiple of $\min(a,b)$, total
variation between those two starting laws is greater than $1/2$. This
gives the lower bound by the triangle inequality.

For the upper bound, the mean time from any starting point to hit $z$ is
$O(a+H_n)=O(a)$. Every outside excursion has a probability bounded below
of hitting $z$ before $A$, its mean time to either is $O(H_n)$, and a
failed attempt adds a mean $O(a)$ inside spell. Likewise the mean time to
hit $w$ is $O(b+n^2)=O(b)$. Each $A$ entry has a uniformly positive
chance to hit $w$ before exiting. Repeating the $Kn^2$-step bound inside
$A$ bounds the mean time to either $w$ or exit by $O(n^2)$.

For $u\le\epsilon b$, the true return probability $P^u(z,z)$ is bounded
below uniformly. The product reference return probability is bounded below at
all times by step 2, and the chance of entering $A$ by time $u$ is $O(u/b)$.
The same statement holds at $w$ for $u\le\epsilon a$, using the two reflecting
stag walks and their exit bound. In either case a fixed multiple $K$ in place
of $\epsilon$ still gives a positive bound depending on $K$. Split the
time into a bounded number of integer blocks of length at most $\epsilon b$
or $\epsilon a$ and use the Chapman–Kolmogorov inequality at the corner.

Choose $z$ when $a\le b$ and $w$ otherwise. By the mean hitting estimate,
every starting state hits the chosen corner by time $L=K\min(a,b)$ with
probability at least $1/2$ for fixed sufficiently large $K$ (round up to
an integer). Its return probability at each remaining time up to $L$ is
uniformly positive by the preceding paragraph. All $L$-step rows therefore
have a common fixed positive mass at the same corner. Iterating this
minorization contracts total variation by a fixed factor per block and proves
(4).

### Exponential passage laws and the mixing constant for $S\ge1/2$

With $F,F_C$ as above, define
$$
 \theta=\frac{(1-\rho_R)(1-\rho_P)}{1-\rho_R\rho_P},\qquad
 k=\theta(F+F_C),\qquad \alpha_n=\frac{F}{F+F_C}.
$$
Then
$$
 \mathbb E_z\tau_w\sim\frac1{\theta F},\qquad
 \mathbb E_w\tau_z\sim\frac1{\theta F_C},\qquad
 t_{\rm mix}(1/4)\sim\frac{\log(4\max(\alpha_n,1-\alpha_n))}{k}.            \tag{5}
$$
Each corner-to-corner time divided by its own mean converges in law to an
exponential random variable of mean one. The mean time to the first visit to
mutual stag is $\mathbb E_z\tau_A\sim1/[(1-\rho_P)F]$. The mean time
to the first departure from mutual stag, starting at $w$, is asymptotic to
$1/[(1-\rho_R)F_C]$.

**Renewal at the two corners.** Put $J_n=H_n+n^2$, so $J_n(F+F_C)\to0$.
The mean time to hit either corner is $O(J_n)$ from every state. Indeed,
from outside $A$ there is a uniform chance to hit $z$ in an $H_n$-block,
before entering $A$. From inside there is a uniform chance to hit $w$ in
a block of $O(n^2)$ steps before exiting. Repeating blocks of length
$O(J_n)$ gives the bound. From corner $i\in\{z,w\}$, define an attempt
to last until the next visit to either corner, with length $L_i$, mean
$\ell_i$, and success probability $p_i$ of reaching the other corner.
The preceding crossing counts yield
$$
 p_z\sim\frac{\theta F}{\nu_D(z)},\quad
 p_w\sim\frac{\theta F_C}{\nu_C(w)},\quad
 \ell_z=\frac1{\nu_D(z)}+o(1),\quad
 \ell_w=\frac1{\nu_C(w)}+o(1).
$$
For the length at $z$, compare a full return cycle of the outside product.
It agrees with the attempt up to return or the first $A$ entry. The latter
event has probability $d_n=O(F)$, and the respective remainders have mean
$O(J_n)$. For $w$ the same comparison uses the first mark and
$c_n=O(F_C)$. This proves the assertions for the lengths. The first-entry
and first-departure mean equivalents in (5)'s description also follow from
the time normalizations above.

Attempts starting at the same corner repeat independently until success, so
the mean passage time is $\ell_i/p_i$. Moreover
$\mathbb E L_i^2=O(J_n\ell_i)$, by summing the mean residual length
conditional on still waiting, using the uniform hitting bound.
Write $p=p_i,\ell=\ell_i,L=L_i$. For $v=sp/\ell,\ s>0$, the passage-time
Laplace transform at $v$ is
$\mathbb E[e^{-vL};\mathrm{success}]/(1-\mathbb E[e^{-vL};\mathrm{failure}])$.
Cauchy–Schwarz gives $\mathbb E[L;\mathrm{success}]\le
(\mathbb E L^2\,p)^{1/2}=o(1)$. Expanding $e^{-vL}$ with quadratic
remainder now yields $1/(1+s)+o(1)$, since $pJ_n\to0$.

**From the corner process to total variation.** On any subsequence where
$\alpha_n\to\alpha$, the last-visited corner on the time scale $1/k$,
starting from a corner, converges at each positive time to the two-state
continuous-time chain with rates $\alpha$ from $z$ to $w$ and
$1-\alpha$ in the reverse direction. This follows from the exponential
limits and independence of alternating passages by the strong Markov property.
A vanishing rate corresponds to a passage diverging on this time scale.
For a fixed number of passages the partial sums converge at every finite
positive continuity point. The chance of more than $m$ passages in a fixed
scaled time tends to zero as $m\to\infty$, by the same partial-sum bound for
the limiting exponential waits. From an arbitrary start the first corner is
reached in $o(1/k)$ time in probability uniformly, by the $O(J_n)$ bound.

To recover the entire distribution, take $g_n=\lceil nJ_n\rceil$.
Here $g_nk\to0$ by the strict inequalities $S<P<R$. Consider the first
corner hit between times $t-2g_n$ and $t-g_n$, for $kt\to c>0$.
Such a hit occurs with probability $1-o(1)$, uniformly in the initial
state. For the remaining $g_n$ to $2g_n$ steps, a start at $z$ has
probability $O(g_nF)$ to enter $A$, and a start at $w$ has probability
$O(g_nF_C)$ to leave it. The reference chains both mix to $o(1)$ total
variation over this interval. In the outside reference all rows have a fixed
common mass at $z$ after $H_n$ steps by the one-player bounds, and in the
inside reference the analogous time at $w$ is $O(n^2)$. Thus the true
distribution is $o(1)$ from a mixture of $\nu_D,\nu_C$ whose weight on
$\nu_C$ is the probability of last visiting $w$, up to $o(1)$.
The same argument in stationarity gives weight
$\pi_n(A)+o(1)=\alpha_n+o(1)$, since $\nu_D(A)=u^2\to0$ and
$\nu_C(A)=1$. The reference laws have total variation tending to one.

At scaled time $c$, the two extreme initial corners in the limiting chain
give probabilities $\alpha(1-e^{-c})$ and
$\alpha+(1-\alpha)e^{-c}$ at $w$. Any initial mixture lies between these
values. Consequently the worst-start distance is
$\max(\alpha_n,1-\alpha_n)e^{-c}+o(1)$ whenever $kt\to c>0$.
This applies to every convergent subsequence of $\alpha_n$, including zero
and one. Continuity and strict decrease at the threshold $1/4$ prove (5).

## Exact formulas at depths one and two

The following formulas also allow feasible correlations at the symmetric
profiles, with independent mixed-profile feedback. Write
$(h_C,b_C,b_C,c_C)$ and $(h_D,b_D,b_D,c_D)$ for the four ordered
probabilities $WW,WL,LW,LL$ at the symmetric actions. At $CD$ write
$(u,v,w,z)=(ST,S(1-T),(1-S)T,(1-S)(1-T))$.

At $n=1$, the stationary masses of $CC$, either mixed profile combined,
and $DD$ are proportional to the three tree polynomials
$$
 \begin{split}
 B_C&=v c_D+2v b_D+w c_D,\\
 B_M&=4b_C b_D+2b_C c_D+2c_C b_D,\\
 B_D&=c_C(v+w)+2b_C w .
 \end{split}
$$
They follow by listing the three directed trees rooted at each node of the
three-state quotient.

At $n=2$, a closed rational formula uses determinants of size six. In the
exchange quotient erase each profile's state with both coordinates deep. Order
the seven remaining states as $CC_{00},CC_{01},CD_{00},CD_{10},CD_{01},
DD_{00},DD_{01}$, where 0 is shallow. Their direct transition matrix is
$$
 Q=\begin{pmatrix}
 0&0&0&2b_C&0&c_C&0\\
 0&b_C&c_C&b_C&0&0&0\\
 0&v&z&0&0&0&w\\
 z&v&0&0&w&0&0\\
 0&0&0&v&0&z&w\\
 c_D&0&0&0&2b_D&0&0\\
 0&0&c_D&0&b_D&0&b_D
 \end{pmatrix}.
$$
Each row of profile $i=C,M,D$ reaches its erased state with probability
$h_i$, with $h_M=u$. The latter holds with probability $h_i$ per step
and has exit row
$$
 L_C=(c_C,2b_C,0,0,0,0,0),\quad
 L_M=(0,0,z,v,w,0,0),\quad L_D=(0,0,0,0,0,c_D,2b_D).
$$
Thus its trace row is $K_{j,*}=Q_{j,*}+h_i L_i/(1-h_i)$. Write $\tau_j$
for the principal cofactor of $I-K$ deleting row and column $j$. The
mass of action profile $i$ is proportional to
$(1-h_i)^{-1}\sum_{j\in i}\tau_j$. The factor restores the erased holding
time. These formulas apply when the stationary law is unique, and the script
checks them independently against full-level integer determinants.

## Numerical checks and the original scout

The entries below are stationary probabilities computed with 76-digit decimal
arithmetic, rounded for display. For the first two depths the exact fractions
are $3328/9233$ and $58905001984/110489411359$. An independent integer
determinant comparison at depth 10 proves the probability exceeds $4/5$.
The exact worst-start mixing times at threshold $1/4$ for depths 1 through 6
are respectively $5,\ 67,\ 943,\ 12{,}628,\ 172{,}177,\ 2{,}401{,}947$
rounds. Formula (5) gives $2{,}424{,}897.30$ rounds at depth 6.
For this certificate, each integer matrix stores entrywise lower bounds on
a labeled kernel power in units $10^{-70}$. Products are rounded down.
Column minima of a long power are lower bounds on the stationary law because
it is a convex combination of the rows. Missing row and stationary mass
bound the error of the computed total variation by half their sum. Binary
search with these two-sided bounds certifies the last integer above
$1/4$ and the first at or below it. At depths 1 and 2 an additional
unrounded integer-power calculation checks the answers directly.

| Memory | $P(CC)$, $R=15/16,\ P=T=4/5,\ S=1/2$ |
| ---: | ---: |
| 1 | 0.360446225496 |
| 2 | 0.533128027921 |
| 4 | 0.705439510211 |
| 10 | 0.809934794001 |
| 15 | 0.822971406315 |
| 16 | 0.823048115811 |
| 17 | 0.822545158796 |
| 40 | 0.712842214178 |
| 100 | 0.114567861654 |
| 128 | 0.026471650358 |
| 160 | 0.004291809740 |

Mean success per hunter is $0.8043972707$ at depth 1 and $0.9131691157$
at depth 16, with limit $0.8$. The stationary proportion of mixed profiles
at 16 is $1.5820731294\times10^{-9}$.

Here $\lambda=15/16$. Changing only $R$ to $0.94$ gives
$\lambda=47/48$, $P_1(CC)=0.3696332101$, $P_{40}(CC)=0.9335777921$
and $P_{140}(CC)=0.8572476494$, again with limit zero. With $R=0.94$ and
$S=0.45$, the solo stag has negative depth drift. Its cooperative fraction
goes from $500/1433=0.3489183531$ at depth 1 to $0.7081525801$ at depth 6
and $0.7375177941$ at depth 12. The integer determinant proves the depth-6
fraction exceeds $7/10$. Formula (1) proves the zero limit here as well.

At fair-solo criticality $R=0.9,\ P=T=0.75,\ S=0.5$, (2) predicts
$U_n/n\to5/8$. The computed values are $0.6203431582$ at depth 10,
$0.6238815049$ at 40 and $0.6243009406$ at 64. For a favorable solo hunt
$R=0.85,\ P=T=0.75,\ S=0.60$, the predicted
$U_n/(G_n\lambda^n)\to25/28$ is $0.8928571375$ at depth 40 and
$0.8928571428568262$ at 64.

Positive elimination of the mean-time equations down to $z,w$ independently
checks the passage constants. For the favorable solo hunt at depth 64,
$\theta F\,\mathbb E_z\tau_w=0.9999999999998174$ and
$\theta F_C\,\mathbb E_w\tau_z=1.000000000000000000277$.

The original StagHunt-2 parameters were $R=0.95,\ P=0.80,\ T=0.85,\ S=0.45$.
Its probabilities are $172/495=0.3474747475$ at $n=1$,
$0.8971686957$ at 16, $0.9602222027$ at 22 and $0.9981215179$ at 40.
Its limit is one. Although $T\ne P$ here, a direct bound suffices. Until
$CC$, the ordered levels deepest-$C$ through deepest-$D$ dominate the
independent reference ladders with $S=0.45,P=0.80$. The reference rightward
step probabilities $1-S\le P$ are nondecreasing in level, and the actual
hare probability against stag is $T\ge P$. Common uniform random numbers
give the coordinatewise comparison. Thus from any outside state there is
uniform positive probability to reach $z$ or $CC$ in $O(n^2)$ steps.

From $z$, consider a single unconstrained hare walk measured outwards from
deepest hare. Tilt it by exchanging $P$ and $1-P$, so its outward drift
is positive. With probability bounded below it reaches outward level $n$
before $-1$, and within $Kn$ steps, by gambler's ruin and the mean time
to either boundary. For at least one $t\le Kn$, first passage at that
specific time before $-1$ has tilted probability at least $c/n$.
Every such path has original likelihood $\rho_P^n$ times its tilted
likelihood. Two independent copies following this event switch together to
$CC$ with probability at least $c'\rho_P^{2n}/n^2$, staying on $DD$
up to the switch. Repeated $O(n^2)$-length attempts give an outside mean at
most $O(n^4\rho_P^{-2n})$. Inside mean is $\Theta(\rho_R^{-n})$, as above.
Therefore the actual cooperative odds grow at least as
$c(19/16)^n/n^4$, establishing the stated limit.

Run the exact certificates and the full-precision curves from the study folder.

~~~sh
python3 experiments/phase1_reversal.py --certificates-only
python3 experiments/phase1_reversal.py --extended
~~~

The stationary and mixing-time leading constants for $S<1/2$, and the
exact global maximizing integer depth in the displayed example, remain
undetermined.
