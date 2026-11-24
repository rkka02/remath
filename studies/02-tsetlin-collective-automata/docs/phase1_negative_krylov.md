# Negative outcome correlation in the full two-player game

Fix a symmetric strict Prisoner’s Dilemma with independent outcomes between rounds and independent player outcomes at mixed action profiles. Let $R,P,T,S$ denote the probabilities of a step toward the deepest state of the current action. For linear and randomized-boundary tactics these are the payoff probabilities. For Krylov replace each raw payoff probability $u$ by $(1+u)/2$. A raw covariance at a symmetric profile is divided by four under independent private Krylov penalty coins. Thus its effective Pearson coefficient is $\kappa u/(1+u)$. Throughout,

$$
  1>T>R>P>S>0,\qquad P>1/2,
  \qquad (r,p,t,s)=(\operatorname{logit} R,\operatorname{logit} P,
                     \operatorname{logit} T,\operatorname{logit} S).
$$

The effective correlation at $DD$ is nonpositive. Every admissible correlation at $CC$ is permitted, including perfect synchronization. The stable mixed-profile case $S>1/2$ includes every strict raw Prisoner’s Dilemma for Krylov. The two automata use the same tactic. In the randomized-boundary tactic each shallow penalty changes action with probability $1/2$, independently between players.

## The phase boundary

Use deficits measured from the deepest $D$ state, with a loss giving an increment of $+1$. The probabilities at $DD$ of the increment pairs $(+,+),(+,-),(-,+),(-,-)$ are $(a,b,b,d)$. Write

$$
 M(u,v)=a e^{u+v}+b e^{u-v}+b e^{-u+v}+d e^{-u-v},\qquad
 h=\sup\{v\ge0:\min_{u\ge p} M(u,v)\le1\}.
$$

The frozen, preflip corner exponent for memory lengths $(\lfloor\gamma n\rfloor,n)$, $\gamma\ge1$, is $E_\gamma=\gamma p+h$. Both the oblique and vertical terminal paths in this identity are proved in the [frozen-walk calculation](phase1_quadrant.md). At zero double-loss probability $a=0$, set $h=+\infty$. The frozen corner is then inaccessible.

1. **Stable mixed profiles, equal memories.** If $S>1/2$, the full stationary odds satisfy
   $$
   \lim_{n\to\infty}\frac1n\log\frac{\pi_n(CC)}{\pi_n(DD)}
         =r-\min\{p+h,\ p+t-s\}.                                      \tag{1}
   $$
2. **Unstable or neutral mixed cooperation, unequal memories.** If $S\le1/2$ and the memory ratio tends to $\gamma\ge1$, the liminf and limsup of the normalized log odds are bounded respectively by
   $$
          r-E_\gamma\quad\text{and}\quad r-\gamma p-\min(h,t).       \tag{2}
   $$
   If $S=1/2$, the upper expression is the limit. For $S<1/2$, write $c_*=-s/2$ and let $v_m>t$ be the larger root of
   $$
      T e^{-v_m}+(1-T)e^{v_m}=\cosh c_*=\frac{1}{2\sqrt{S(1-S)}}.
   $$
   For the deterministic linear tactic the exact limit is
   $$
                   r-\gamma p-\min(h,v_m).                           \tag{2a}
   $$
   Formula (2a) also holds for $B$ if $c_*\le\log(2-e^{-p})$, or if $h\le t$ by (2). The general $B$ slope when $h>t$ and the shallow holding rule is active remains open here.
3. **Strict selection.** In both settings the mixed mass vanishes exponentially. In the parameter ranges of (1) and (2), $r>E_\gamma$ selects $CC$ and $r<E_\gamma$ selects $DD$, with an exponentially small losing mass. For the first claim take $\gamma=1$. Indeed $t>r$ and $p>s$, so the stable mixed cascade has cost $p+t-s>r$, and the cutoff in (2) cannot reverse the strict sign. For $S\le1/2$ and finite $h$, equality occurs at $\gamma_c=(r-h)/p$ whenever $\gamma_c\ge1$. If $\gamma_c<1$, every $\gamma\ge1$ selects $DD$. The equality surface has zero exponential slope. These statements leave its limiting stationary probabilities open.

### A rational test at equal memories

Put $x=P/(1-P)$, $y=[R/(1-R)]/x>1$, $A=a y+b/y$, and $B=b y+d/y$. The sign of $r-E_1$ is the sign of

$$
   \begin{cases}
      A x+B/x-1,& B\le Ax^2,\\[2pt]
      4AB-1,& B>Ax^2.
   \end{cases}                                                       \tag{3}
$$

These quantities are rational whenever the raw game and the raw shock are rational. In fact $\min_{w\ge x}(Aw+B/w)$ occurs at $\max(x,\sqrt{B/A})$. The projection onto $v$ of the convex set $\{u\ge p,\ M(u,v)\le1\}$ is an interval, with a strict inequality at every $0<v<h$. To see strictness, $M(p,0)=1$ and the derivative in $v$ there is strictly negative for nonpositive correlation. Convexity gives the rest of the open interval. Substituting $v=\log y$ proves (3), including $a=0$.

For numerical evaluation, let $w=(b x+d/x)/(a x+b/x)$, so $M(p,\log w)=1$. If $M_u(p,\log w)\ge0$, then $h=\log w$. If the derivative is negative and $a>0$, the maximizer has $M_u(u_0,h)=0$, and

$$
 D_0=\tfrac14-ad-b^2,\qquad
 Z=\frac{D_0+\sqrt{D_0^2-4ab^2d}}{2ab},\qquad
 h=\tfrac12\log Z,\qquad u_0=\tfrac12\log\frac{bZ+d}{aZ+b}.         \tag{4}
$$

Indeed $\min_u M(u,v)=2\sqrt{(a e^v+b e^{-v})(b e^v+d e^{-v})}$. At its top the outward normal points vertically and $M_v>0=M_u$. Since $M_u-M_v=4b\sinh(u-v)$, this gives $p<u_0<h$. On the first branch $u_0=p\le h$, because $M(p,p)\le1$ at nonpositive correlation. These descriptions identify the two roots with the frozen exponent in the cited calculation. For $a=0$, $M(v,v)=2b+d e^{-2v}<1$ for every $v>0$.

## A barrier that survives switches of the first player

Write $N_i$ for player $i$'s depth. Until the first action profile $CC$, define the capped deficit $Z_i$ to be the current deficit from deepest $D$ if the player defects, and $N_i$ if the player cooperates. Thus the first $CC$ is the first time both capped deficits equal their caps. Let $v=\min(h,t)$. There exists $u$ with

$$
                     p\le u\le v\le t,\qquad M(u,v)\le1.            \tag{5}
$$

When $h<\infty$, interpolate in $(u,v)$ between $(p,p)$ and $(u_0,h)$. When $a=0$, take $u=v=t$. Here $t>p$.

Away from the lower wall of both coordinates, $\exp(uZ_i+vZ_j)$, stopped or killed on first $CC$, has conditional mean at most its present value. This holds in $DD$ by (5). In a mixed profile the cooperator stays capped or decreases by one. The remaining defector has one-step exponential moment at most one for each tilt in $[0,t]$. This argument permits arbitrary repeated flips of the other player. At a shallow $B$-penalty the positive increment is either the proposed $+1$ or zero, which preserves the bound. Similarly $\exp(pZ_i)$ is superharmonic away from $Z_i=0$, irrespective of the other player's state before the first $CC$.

Let $H$ be any polynomial horizon. Starting with both players at deepest $DD$, bound the chance of first $CC$ by time $H$. For each successful path fix its terminal time and the last time each coordinate visits zero. Suppose coordinate $i$ leaves zero earlier than $j$. Tilt only $i$ by $p$ up to the later departure, then tilt $i,j$ by $(u,v)$. Increasing the first tilt at this time multiplies the exponential by at most $e^{(u-p)N_i}$. Each of the two departure steps from zero costs at most a fixed factor $e^{u+v}$. Between the chosen departure times, paths hitting forbidden lower walls are discarded. The supermartingale bounds apply at deterministic times without conditioning on a future last exit. At the specified terminal time the two-tilt exponential equals $e^{uN_i+vN_j}$. Sum the bound over the two orders, coincident departure times included, and at most $(H+1)^3$ time triples. The result is

$$
  \Pr_{DD\,\mathrm{deep}}(\tau_{CC}\le H)
     \le C(H+1)^3\exp[-\min_{i\ne j}(pN_i+vN_j)].                   \tag{6}
$$

For $N_1\ge N_2$, the minimum is $pN_1+vN_2$. This argument uses the actual game after the first player switches.

For equal memories a second initial condition is needed. Suppose one capped deficit is at most $n$ and the other's initial value is $y\in[0,n]$. The chance of first $CC$ by time $H$ is at most

$$
                    C(H+1)^3 e^{-v(n-y)}.                             \tag{7}
$$

If neither coordinate visits zero in the time interval, put $u$ on the first and $v$ on the second throughout. If only the second visits zero, put $p$ on the first until the second's last departure, then use $(u,v)$. The initial value of the first costs at most $e^{pn}$, leaving an exponent of at least $vn$. If only the first visits zero, put $p$ on the second until the first's last departure. The resulting cost is at least $(p+v)n-py\ge v(n-y)$. If both visit zero, start at the earlier last departure as in (6). All estimates discard paths on a subsequent forbidden wall hit. This proves (7).

## From a short excursion to stationary probabilities

A *core* is the single state in which both players are at the deepest levels of their current actions. A profile where both players have strictly positive depth drift reaches its own core before a switch within $C\max_i N_i$ steps with probability bounded below independently of the depths. To verify uniformity, start with a sufficiently large fixed number $K$ of joint inward moves. Such moves have positive probability here, including at the negative Fréchet endpoint. Before the first hit of a player's deep wall the probability of losing this buffer is at most $e^{-cK}$ by one-dimensional gambler's ruin. Later the chance of a switch in $CN$ steps is $O(N e^{-c N_{\min}})$, by summing over the last departure from the deep wall. At time $CN$ each deficit is within a fixed distance $L$ of zero with high probability. In the frozen reflected-walk formula the initial displacement term has negative linear drift, and the maximum terminal suffix sum has a geometric tail. Apply the union bound to the two coordinates and finish with $L$ joint inward moves. For fixed $\gamma$ these estimates are uniform over starting depths. By stationarity the stationary probability of such a profile is between its core mass and $O(N)$ times its core mass.

For $S>1/2$ trace the chain on all four cores and aggregate the two mixed cores by player exchange. For $S\le1/2$ use only the two symmetric cores. From any mixed state in the latter case, stay with the independent frozen mixed feedback until the first action switch. The cooperating coordinate exits its action within $C N^2$ steps with probability at least $1/2$, by monotone comparison with a fair walk. From deepest cooperation that fair walk has mean exit time $N(N+1)$ for $L$, or $N(N+3)$ for $B$, by the first-step recurrences. The defecting coordinate independently stays in $D$ throughout this window with probability bounded below. This follows from positive drift up to its deep wall and the polynomial-horizon return estimate. Once both defect the joint core can be reached without a further switch with uniformly positive probability. It follows in both traces that, from any state, the chance to hit some traced core in $CN^2$ steps exceeds a fixed constant. The first positive return time to the set of traced cores therefore has tail at $H=N^4$ bounded by $\exp(-cN^2)$, after allowing the first step. All estimates at polynomial horizons below apply to full core excursions at exponential precision.

At a deep symmetric profile the cost of any action change before that return is at least its one-coordinate log odds times the shorter depth, by summing a marginal exponential bound over last wall departures and times. A matching way to depart is to tilt the shorter player's proposed increments by its log odds. The targeted deficit then has positive drift. With fixed positive probability it becomes positive at the first step, stays positive, and reaches its shallow level in $O(N)$ steps. Stop earlier if the partner changes action. Up to this stopping time the likelihood in the original law is at least $e^{-rN_{\rm short}}$ at $CC$, since the targeted deficit has traveled at most that distance. At the shallow level force a penalty and, if needed, one boundary acceptance. At $CC$ any resulting mixed profile reaches its own core with fixed positive probability in the four-core regime or reaches deepest $DD$ in the two-core regime; a double switch reaches deepest $DD$ with fixed positive probability. These paths avoid a prior return to the starting core. Consequently deepest $CC$ reaches another traced core at cost exactly $rN_{\rm short}+o(N)$, even if the two feedbacks there are perfectly synchronized.

At deepest $DD$ an analogous single-player tilt costs $pN_i+o(N)$ for either chosen player. Under this tilt the other player's marginal outward probability is no larger than its untilted value, because the covariance is nonpositive. Over $O(N)$ steps the probability that this other coordinate leaves its action tends to zero. Therefore one can prescribe which player defects no longer. In the four-core trace this supplies the edge from $DD$ to a mixed core at cost $pn+o(n)$. In a mixed core with positive drifts the same tilt uses independence and can prescribe either switch: the edge to $DD$ has cost at most $sn+o(n)$; the one to $CC$ costs at most $tn+o(n)$.

There is also a direct four-core or two-core route from deepest $DD$ to deepest $CC$ at cost at most $E_\gamma n+o(n)$ for $a>0$. Take a frozen excursion to the preflip corner $(N_1-1,N_2-1)$ before any overflow or core return, then force the double loss (and both boundary acceptances for $B$). From the two newly cooperating states the $CC$ core is reached without a further switch with fixed positive probability. Restricting to the killed frozen paths is valid for $B$: they contain no earlier proposed overflow. When ratios tend to $\gamma$ with sublinear rounding errors, the frozen exponential bound follows from the same axis and terminal-bridge construction with the actual longer barrier. Its initial axis segment absorbs the $o(n)$ change at subexponential cost, including when the two long sides agree to first order.

## The mixed-core contribution

For equal memories and $s>0$, write $A,B_0,J$ for the $CC,DD,\mathrm{mixed}$ core classes. Denote the one-excursion transitions from $i=A,B_0$ to $J$ by $x_i$, to the other symmetric core by $z_i$, and from $J$ to $A,B_0$ by $U,V$. The first switch out of $J$ costs at least $sn+o(n)$, hence $V=e^{-sn+o(n)}$. To bound $U$, start with a deep cooperator and a deep defector. If the original defector switches at or before the first switch of the cooperator, reaching that defector's shallow boundary costs at least $tn+o(n)$. Otherwise the original cooperator switches while the defector has deficit $y$. In the independent frozen mixed profile, the probability of a cooperator switch and a defector deficit of at least $y$ by the polynomial horizon is bounded by $\operatorname{poly}(n)e^{-sn-ty}$, by the respective last wall departures. Apply (7) at the switch and sum over $0\le y<n$. This proves

$$
       e^{-tn+o(n)}\ \le U\ \le e^{-n\min(t,s+v)+o(n)},\qquad
       U/V\longrightarrow0\ \text{exponentially}.                    \tag{8}
$$

The stationary core ratio is exactly

$$
      \frac{\pi(A)}{\pi(B_0)}=
       \frac{z_{B_0}+x_{B_0}U/(U+V)}{z_A+x_AV/(U+V)}.                \tag{9}
$$

This follows by eliminating the single mixed class in the stationary balance equations. The denominator is $e^{-rn+o(n)}$. In the numerator $x_{B_0}=e^{-pn+o(n)}$; (6) gives $z_{B_0}\le e^{-n(p+v)+o(n)}$. The direct frozen passage bounds $z_{B_0}$ below when $h<\infty$, while the lower estimate in (8) supplies the mixed cascade for every shock. The matching exponent of the numerator is therefore

$$
     \min(p+h,p+t-s)=\min(p+v,p+t-s).
$$

The mixed core balance gives $\pi(J)(U+V)=\pi(A)x_A+\pi(B_0)x_{B_0}$. Since $s<p<r$, its mass is exponentially smaller than the sum of the symmetric masses. The polynomial comparisons of core and profile masses complete (1). The traced process is irreducible on these core classes: the single-switch routes give the required connections, and every state reaches a core. This also gives uniqueness of the stationary law before exchange aggregation because both labeled mixed cores are accessible from $DD$.

For $s\le0$ the two-core stationary ratio is just the excursion probability from $DD$ to $CC$ divided by the reverse probability. The denominator costs $rn+o(n)$; (6) and the frozen passage give (2). A mixed profile can occur only after one player leaves its symmetric starting action, at per-excursion cost at least $\min(p,r)n+o(n)$. Its subsequent expected occupation until the first traced core is polynomial by the uniform core hitting bound. The stationary excursion formula makes its total mass exponentially small. The two cores communicate even at $a=0$: first force the longer defector across alone, then force mixed cooperator rewards and remaining defector penalties until both cooperate. Each finite-depth event has positive probability.

At $s=0$ the lone first switch of the longer defector costs $pN_1+o(n)$. Over the next $Cn$ steps the newborn cooperator has probability $e^{-o(n)}$ of keeping its action. For instance force $\lceil n^{2/3}\rceil$ initial inward moves of that fair coordinate and use a maximal deviation bound for its next $Cn$ fair steps. Its deep reflecting wall is order $n$ away. Independently the shorter defector traverses to its shallow level and switches in that window at cost at most $tn+o(n)$, using the positive-deficit tilt from any initial depth and forcing the last acceptance. These two requirements can run at the same time, and $Cn$ is chosen large enough for the defector. The symmetric $CC$ core then establishes with uniformly positive probability. This gives the matching upper cost $\gamma p+t$ for (2).

## The cost of a sustained mixed spell when cooperation has negative drift

Take $S<1/2$. In addition to the frozen passage, a single mixed spell costs at most $(\gamma p+v_m)n+o(n)$. First have the longer player switch alone, using its one-coordinate $DD$ tilt, which costs $pN_1+o(n)$. While it cooperates, a unit of transverse displacement further into $C$ has moment $m_S(c)=S e^c+(1-S)e^{-c}$. An outward step of the remaining defector has moment $m_T(v)=T e^{-v}+(1-T)e^v$. At $(c_*,v_m)$ their product is one. Under this tilt the cooperator is a fair walk and the defector has positive outward drift. Spend $O(n^{2/3})$ prescribed mixed steps to give the cooperator an initial buffer and, if needed, move the defector away from its deep wall. A defector already near its switch can instead complete the crossing during this sublinear adjustment. With probability bounded below under the tilt, the defector then reaches its shallow level in $O(n)$ steps and the cooperator moves by at most $O(n^{2/3})$, staying within its action. A maximal bounded-increment estimate gives the latter bound; for the former use the positive-drift law of large numbers and preserve a buffer from the lower wall. The likelihood cost is at most $v_m n+o(n)$. Finish by requiring a switch of the defector and an inward move of the cooperator, then entrench the $CC$ profile. This lower probability construction works for $L$ and $B$.

For the matching upper probability bound in $L$, write $v=\min(h,v_m)$. If $v\le t$, inequality (6) already gives the desired exponent. For $v>t$, let $0<c\le c_*$ be the smaller solution of $m_T(v)m_S(c)=1$. There exists a tilt $u\in[\max(p,c),v]$ with $M(u,v)\le1$. To verify this, the interpolation in (5) supplies a point of $[p,v]$ in the $DD$ sublevel set at this $v$, using $(v,v)$ when $a=0$. Let $u_+$ be its larger unconstrained root in the first coordinate. Write $m_P(v)=P e^{-v}+(1-P)e^v=M(0,v)$. The two-exponential form of $M$ gives
$$
      m_P(v)=\cosh(u_+)-M_u(u_+,v)\sinh(u_+)\le\cosh(u_+).
$$
Here $u_+\ge p>0$. Also $m_P(v)>m_T(v)$ because $T>P$ and $v>0$. Since $0\le\tanh c\le1-2S$, one has $m_S(c)\cosh c\le1$. Thus $\cosh u_+>m_T(v)=1/m_S(c)\ge\cosh c$. Finally $m_T(v)<\cosh v$ gives $c<v$. Convexity of the sublevel interval permits increasing the supplied tilt to $c$ whenever needed.

For a signed coordinate $z$ running from deepest $D$ at zero through shallowest $C$ at $N$, give a two-coordinate tilt of size $\theta\in\{u,v\}$ the weight
$$
 F_\theta(z)=\begin{cases}e^{\theta z},&z<N,\\
                  e^{\theta N+c(z-N)},&z\ge N.
               \end{cases}
$$
The product $F_u F_v$ is superharmonic before the first $CC$ whenever both lower walls are avoided. The $DD$ assertion uses $M(u,v)\le1$. At a mixed profile the defector's multiplier is at most $\max(1,m_T(v))$ by convexity on $[0,v]$. The cooperator's multiplier is at most $m_S(c)$, also at its shallow state because both $u,v\ge c$. Reflection at deepest $C$ decreases the weight. Independence in the mixed profile proves the product estimate.

For the earlier single-coordinate portion of the last-zero argument, put $G(z)=e^{pz}$ on $D$ and
$$
    G(z)=e^{pN}\big(1-\eta+\eta e^{c(z-N)}\big)\quad(z\ge N).
$$
In the interior of $C$ its mean multiplier is at most one by $m_S(c)\le1$. At the shallow state choose a fixed $\eta>0$ sufficiently small that $S(1-\eta+\eta e^c)+(1-S)e^{-p}\le1$; at $\eta=0$ the inequality is strict. All $D$ states away from zero satisfy the single-coordinate bound by $T>P$. Everywhere $F_u/G\le\eta^{-1}e^{(u-p)N}$. Consequently raising this tilt at the later last-zero departure costs only a constant times the original surcharge. At the target, $F_u F_v\ge e^{uN_i+vN_j}$. The proof of (6) now gives cost at least $pN_1+vN_2$ also for this larger $v$, proving (2a).

For the stated $B$ subregion multiply the $C$ parts of $F_\theta$ and $G$ by $2-e^{-\theta}$ and $2-e^{-p}$, respectively. The jump ratio from shallow $D$ to shallow $C$ is then $2e^\theta-1$. After averaging over the private boundary coin, the proposed positive step has multiplier exactly $e^\theta$, including when both players are shallow in $DD$. From shallow $C$ a penalty has average multiplier $(2-e^{-\theta})^{-1}$. This is at most $e^{-c}$ under $c\le c_*\le\log(2-e^{-p})$ and $\theta\ge p$. The single-coordinate construction still works with sufficiently small $\eta$, since $(2-e^{-p})^{-1}<1$. All weights at the first $CC$ increase by fixed positive factors. This completes the $B$ assertion.

### A boundary coin can change the exponential rate

Let $v_b>t$ solve $m_T(v_b)(1-S)/2=1$. The shallow $B$ cooperator can hold its level for every round of the remaining defector's climb. Each such hold has probability $(1-S)/2$. Under the normalized one-coordinate law with weights $((1-S)/2)e^{v_b\Delta}$ times the defector's original transition probabilities, its drift toward the switch is positive. The preceding one-dimensional tilt argument therefore gives cost at most $\gamma p+v_b$ to reach the $CC$ core. An initial sublinear buffer for the defector and a prescribed final switch change the cost by $o(n)$. In particular $S<1/17$ implies $v_b<v_m$. If also $h>v_b$, the limiting $L$ log odds are strictly below the liminf of the $B$ log odds. Both games select $DD$.

For an example with all four $DD$ signals strictly positive, take raw $(R,P,T,S)=(.64,.60,.68,.04)$, $\kappa_R=0$, $\kappa_P=-.65$. Then $(a,b,d)=(1,99,51)/250$. The test point $y=7$ certifies the separation using three fractions,
$$
 M(\log5,\log7)=\frac{4301}{4375}<1,\qquad
 4S(1-S)m_T(\log7)^2=\frac{16058976}{19140625}<1,\qquad
 \frac{1-S}{2}m_T(\log7)=\frac{4908}{4375}>1.
$$
Thus $h,v_m>\log7>v_b$. At equal depths the exact $L$ log-odds slope is $-1.8553409824$, whereas the $B$ liminf is at least $-1.6491143272$. The two stationary $CC$ probabilities at $n=48$ are $3.749\times10^{-41}$ and $2.179\times10^{-30}$, respectively. This proves an exponential change from the private boundary coin alone.

## Computed examples

The script uses raw payoff order $(R,P,T,S)$. The certificate signs below are exact rational comparisons. The finite chains use subtraction-free state elimination at 72 decimal digits. The independent 80-digit dense solver agrees on every profile mass at depths (3,2) to relative error below 1.2 × 10⁻⁷¹ for all nine cases.

| Tactic and raw game | Raw $(\kappa_R,\kappa_P)$ | Frozen $E_1$ | Limiting log-odds slope | $\pi_{48}(CC)$ |
|---|---|---:|---:|---:|
| Krylov $(.71,.40,.83,.22)$ | $(0,0)$ | 1.694595721 | +0.079772006 | 0.7428504570 |
| Same Krylov game | $(-.30,-.30)$ | 1.863774452 | −0.089406726 | 0.0014837604 |
| Krylov $(.976,.55,.992,.12)$ | $(0,-.765)$ | 4.039997690 | +0.370778358 | 0.9999676308 |
| Krylov $(.93,.625,.95,.25)$ | $(0,-.6)$ | $+\infty$ | −1.302293051 | $1.8172\times10^{-27}$ |
| $L$, $(.84,.65,.86,.25)$ | $(0,-.52)$ | 2.858266770 | −0.964987560 | $1.7788\times10^{-22}$ |
| $B$, $(.84,.65,.86,.50)$ | $(0,-.52)$ | 2.858266770 | −0.776101098 | $1.8060\times10^{-15}$ |

For the third row, the diagonal estimate gives $\log(d/a)=5.124805890>r=4.410776048$; the vertical terminal path gives $E_1<r$. The diagonal estimate would reverse the stationary verdict. For the first two rows the exact common-shock crossing is $\kappa_c=-413/2864$, obtained by setting $w=y$ on the oblique branch of (3). The fourth row has exactly zero double-loss probability. The two mandatory separate switches give its displayed finite exponent.

As an unequal-memory example, take $L$ or $B$, raw $(R,P,T,S)=(4/5,3/5,9/10,1/5)$, and $\kappa_R=\kappa_P=-1/5$. The oblique branch gives $p=\log(3/2)$, $h=\log(16/9)$, $r=\log4$. The critical memory ratio is exactly two. At short depth 24 the full $L$ chain gives $\pi(CC)=0.9916103221$ for equal depths and $4.9591\times10^{-7}$ for a threefold long depth.

```bash
python3 experiments/phase1_negative_krylov.py --n 8 16 32 48
python3 experiments/phase1_negative_krylov.py --verify --n
python3 experiments/phase1_negative_krylov.py --cases aspect --ratio 2 --n 8 16 24
```
