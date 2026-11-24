# Repeated action changes and the escape rates of the linear and randomized-boundary tactics

For Tsetlin's deterministic two-action linear tactic $L$, a loss at depth one changes the action. For his randomized-boundary tactic $B$, a weak loss chooses uniformly between the two weak actions. We use independent internal choices for the two automata. At a mixed profile the players' outcome coins are independent. The joint shock at DD can be correlated. A player can change its action a number of times proportional to the other player's memory during a successful transition. Tsetlin gave the distinction between a marginal-payoff game and a joint-outcome game in §5, equations (17)–(20), of his 1963 survey, and described the weak-state randomization in §6. [Archived primary source](../sources/papers/Tsetlin_1963_UMN_18_FiniteAutomataBehavior_rus.pdf)

## The full two-player result

Write $P,R,T,S$ for the four win probabilities and assume

$$
0<S\le\tfrac12<P<R<T<1,\qquad n_2=n,\qquad n_1/n\longrightarrow\gamma\ge1.
$$

Let $a=\log(P/(1-P))$, $a_R=\log(R/(1-R))$, $a_T=\log(T/(1-T))$, and let $\kappa$ be the DD correlation. The CC correlation can be any fixed feasible value. Use signed coordinates increasing towards cooperation. Each coordinate starts at 0 at the deepest D state, first plays C at $n_i$, and reaches its deepest C state at $2n_i-1$. In DD a loss increases the coordinate. In a mixed profile the short cooperator advances on a reward.

With $q=1-P$, set $w=P^2+\kappa Pq$, $b=(1-\kappa)Pq$, $d=q^2+\kappa Pq$. For $s$ the long tilt and $t$ the short tilt, define

$$
\begin{aligned}
D(s,t)&=w e^{-s-t}+b(e^{s-t}+e^{-s+t})+d e^{s+t},\\
C(s,t)&=(T e^{-s}+(1-T)e^s)(S e^t+(1-S)e^{-t}).
\end{aligned}
$$

Let $V$ denote the cost per unit of short memory for a transition from the deepest DD state to the deepest CC state before the next return to the deepest DD state. The four displayed cases below first give $L$. The final section gives $B$ and every fixed weak-state switch probability $u\in(0,1]$. For each case the limit exists. The stationary action odds satisfy

$$
  \lim_{n\to\infty}{1\over n}\log{\pi_n(CC)\over\pi_n(DD)}=a_R-V,
  \qquad \pi_n(CD)+\pi_n(DC)\longrightarrow0.
$$

Thus either strict sign selects its corresponding pure profile. At equality, the formula specifies only the exponential scale.

1. **Ordinary positive tilts.** If $0\le\kappa<1$ and $\gamma(2\kappa-1)\le1$, then
   $$
   V=\max\{\gamma s+t:0\le s,t\le a,\ D(s,t)\le1\}.
   \tag{1}
   $$
   In particular, independent DD outcomes give $V=(\gamma+1)a$. At equal memories,
   $$
   V=\log(w/d),\qquad 0\le\kappa\le1.
   $$
2. **The switching interface.** If $1/2<\kappa<1$ and $\gamma(2\kappa-1)>1$, then
   $$
   V=\max\{\gamma s+t:s\ge0,\ t\le0,\ D(s,t)\le1,\ C(s,t)\le1\}.
   \tag{2}
   $$
   If the unconstrained DD endpoint maximizer satisfies $C\le1$, the path can stay in DD up to a sublinear terminal adjustment. If $C>1$ there, the maximizing pair $(s_I,t_I)$ satisfies $D=C=1$. The optimal path reaches the short switching threshold early and repeatedly crosses it while the long player continues towards C. Over this range $V=\gamma s_I+t_I$ is affine in $\gamma$.
3. **Perfectly common DD outcomes.** If $\kappa=1$, set $W=P/(1-P)$, and let $s_I>a$ solve $C(s_I,a-s_I)=1$. For every $\gamma\ge1$,
   $$
   V=a+(\gamma-1)s_I,\qquad
   \gamma_c=1+\frac{a_R-a}{s_I}.
   \tag{3}
   $$
   Cooperation wins below this memory ratio, and defection wins above it. To evaluate the slope, let $v=e^{2s_I}/W$. It is the larger positive root of
   $$
   (1-T)(1-S)v^2+
   \big((1-T)SW+T(1-S)/W-1\big)v+TS=0.
   $$
   At $s=a$, $C(a,0)<1$, and $C(s,a-s)$ tends to infinity as $s$ increases. This identifies the root uniquely on $s>a$.
4. **An open range of negative correlations.** Suppose $\kappa<0$, all four DD shocks have positive probability, and set
   $$
   h=\log\frac{b e^a+w e^{-a}}{d e^a+b e^{-a}}.
   $$
   If $h\le a_T$ and $D_s(a,h)\ge0$, then for all $\gamma\ge1$
   $$
   V=\gamma a+h. \tag{4}
   $$
   Both inequalities hold for sufficiently small negative $\kappa$ at fixed $T>P$. The companion note treats the strict selection boundary across the full negative range. [Negative-correlation analysis](phase1_negative_krylov.md)

The arguments establish exponential rates. A polynomial prefactor would require estimates finer than the limits here.

## A certified reversal with all four DD probabilities positive

Take $P=.51,\ T=.55,\ S=.20,\ \kappa=.997,\ \gamma=2$. Ordinarily reflecting a frozen DD walk and asking that both stationary deficits exceed their thresholds gives $2a$. Killing that walk at the first action change and forcing its corner endpoint has cost $H=\max_{D\le1}(2s+t)$. The full action-changing chain has an intermediate barrier.

| Quantity | Cost per unit of short memory |
|---|---:|
| Frozen stationary joint exceedance $2a$ | 0.08001066922739832287 |
| Full two-player transition $V$ | 0.08581376346450921821 |
| Frozen DD corner endpoint $H$ | 0.28750951686113529171 |

For $R=.53$, $a_R=0.12014431184206324732$ lies between $V$ and $H$. The full chain cooperates. Using the killed endpoint in its place predicts defection. For $R=.5206$, $a_R=0.08244667056018101686$ lies between $2a$ and $V$. The full chain defects. Using stationary joint exceedance predicts cooperation.

At the interface, $s_I=0.04584893509408259372$ and $t_I=-0.00588410672365596924$. Under this tilt the long player's mean increment in the mixed profile is $-0.05443255739573832170$. Averaging its increments over the successive returns to DD gives $+0.01761184963153615313$. A path confined to the mixed profile misses the positive advance along the interface.

The script brackets $e^{s_I}$ between $1.04691$ and $1.04692$ by exact rational kernel evaluations. It also certifies the strict inequalities between the phase odds with fractions and independently checks the first-return transform at 80-digit working precision. [Reproducible calculation](../experiments/phase1_interface.py)

As a finite-game check, use $P=.7,\ T=.75,\ S=.2,\ \kappa=.9,\ \gamma=4$. Solving the full finite Dirichlet problem for first CC before a strict return to $K_D$ gives $0.0000033699949800684435620290820184423523102266143352960905372973664706$ at $n=3$, with 80-digit working precision. The sparse calculations agree with that solve at small depth and give a secant slope of $3.62229970076469$ between $n=64$ and $80$ for the negative log probability. Equation (2) gives $3.62229970076468702194$. The corresponding frozen endpoint and stationary exceedance costs are $4.06751281334980978043$ and $3.38919144154881445484$.

## Regeneration at the two deepest states

Write $K_D,K_C$ for the deepest joint DD and CC states. A uniform estimate used below is that from any state in either pure profile there is a fixed probability $c>0$ of reaching that profile's deepest joint state in $Bn$ steps while retaining both actions. To see this at win probability $p>1/2$, first require $k$ joint wins, whose probability is positive since the joint win probability is at least $2p-1$. In a frozen profile the chance a coordinate drops to its switching edge before its first arrival at the deep cap is at most $((1-p)/p)^k$, up to a harmless one-step shift. A further $O(n)$ trials to escape from the cap cost $O(n)((1-p)/p)^{n_i-O(1)}$. Choose $k$ fixed and large. At a deterministic time $Bn$, both deficits from their respective deep caps are bounded by a fixed $K$ with probability at least $3/4$. Indeed, for a small positive $\theta$ each frozen reflected marginal satisfies

$$
\mathbb E[e^{\theta Y_{j+1}}]\le m_p(\theta)\mathbb E[e^{\theta Y_j}]+O(1),
\qquad m_p(\theta)=p e^{-\theta}+(1-p)e^\theta<1.
$$

Choose $B$ large enough to absorb the initial $e^{O(n)}$, then $K$ large enough for the tail estimate. Another $K$ joint wins place both coordinates at the deep caps. All numerical constants may depend on the fixed memory ratio and the fixed outcomes.

From a mixed state the cooperator has drift towards D, and the defector has drift into D. The mixed coins are independent. In $Bn$ steps the cooperator reaches its D action with probability at least $3/4$ for sufficiently large $B$, by a bounded-increment concentration estimate. Reflection at deepest C can only help. For this entire interval the initial defector survives with probability bounded below, uniformly even at depth one, by the same one-dimensional ruin estimate after a fixed number of wins. Thus $K_D$ can be attained with uniformly positive probability from any mixed state in $O(n)$ time. In particular, every block of $Bn$ steps has a uniformly positive chance of hitting either deep state. Before first CC the same argument applies with targets $K_D$ and the first CC visit. Before first exit from CC use the targets $K_C$ and the first exit. The probability of avoiding either applicable target until time $n^3$ is $e^{-\Omega(n^2)}$.

The preceding mixed-state time estimate uses $S<1/2$. At $S=1/2$ a reflected simple random walk on sites $0,\ldots,M$ has expected time $j(2M+1-j)$ to reach 0 from $j$, as follows from the one-step difference equation with holding on an outward step from $M$. Thus a cooperator reaches the weak edge with probability bounded below in $O(n^2)$ time, and an immediate loss with a successful switch has positive fixed probability. The strongly biased defector survives that polynomial interval with the same uniform lower bound. At this parameter endpoint use $O(n^2)$ blocks, expectation $O(n^2)$ between deep states, and a time cutoff $n^4$ in all polynomial-window estimates below. The discarded probability remains $e^{-\Omega(n^2)}$.

For a CC excursion from $K_C$, the chance of a first action change before returning has cost $a_R$. The upper bound follows from gambler's ruin for each frozen marginal, a union bound over $n^3$ possible last departures from its deep cap, and the preceding tail estimate. The matching lower bound is a first short-coordinate excursion that reaches its switch before it revisits its deep cap. One may sample the frozen CC coins ahead of time. An earlier exit by the other coordinate also realizes the desired event. At a first exit there is a uniformly positive probability of reaching $K_D$ before another CC visit, by the mixed and DD estimates. Likewise every first CC visit from DD has a uniformly positive chance of reaching $K_C$ before leaving CC. Consequently, computing the first CC cost before a return to $K_D$ gives the forward transition cost.

Observe the chain only on $\{K_C,K_D\}$. Its two-state stationary flux identity gives

$$
\frac{\pi(K_C)}{\pi(K_D)}=
\frac{\Pr_{K_D}(\tau_{K_C}<\tau^+_{K_D})}
     {\Pr_{K_C}(\tau_{K_D}<\tau^+_{K_C})}.
$$

The accessibility estimates and the positive paths between the two states give a unique closed class. Moreover $c\pi(CC)\le(Bn+1)\pi(K_C)$, by counting possible visits in a stationary time window, and similarly for DD. The reverse comparisons hold with factor one. To bound mixed mass, sum the expected number of mixed visits per excursion from the two deep states with their stationary weights. Each mixed visit requires a first pure-profile exit. The excursion's expected remaining length from this exit is $O(n)$ by the block estimate. In either pure profile, a first exit before returning to its joint deep state has probability at most $\exp[-n\log(p/(1-p))+o(n)]$, by the same marginal calculation. This gives exponentially vanishing total mixed mass.

## Positive tilts and last visits to the reflecting edges

Clip each signed coordinate $Y_i$ at $n_i$, so every C depth contributes $n_i$ to the clipped variable $Z_i$. Up to the first CC, a clipped coordinate already in C can only stay put or decrease. In DD and away from its reflecting edge the two-coordinate exponential weight $e^{s Z_1+t Z_2}$ has expected multiplier $D(s,t)$. In a mixed profile the multiplier is at most $m_T(t)$ or $m_T(s)$ when $s,t\ge0$. This bound uses only the defector's marginal. Before its last departure from zero a coordinate need not be charged.

More explicitly, fix deterministic last-zero times of both coordinates and a terminal time, all at most $n^3$. After the earlier departure charge its coordinate alone. After the later departure charge both. Kill a path on a further zero of a charged coordinate or an earlier CC. The single-coordinate multiplier is at most one if its tilt is in $[0,a]$, and the two-coordinate multiplier is at most one if $D\le1$ and both tilts are at most $a_T$. At the two designated departures bound the omitted increments by $e^{s+t}$ apiece. Iterating these one-step bounds and summing over a polynomial number of time triples gives the upper probability bound $\exp[-s n_1-t n_2+o(n)]$. The excursion tail controls later terminal times. This proves the required barrier lower bound for (1).

For the converse, the maximizer for (1) can be taken with $s\ge t$ by symmetry. On the unconstrained smooth DD boundary, $\nabla D$ is parallel to $(\gamma,1)$. Tilting a DD step by $e^{s\Delta X+t\Delta Y}$ therefore moves linearly to the target, and the original log probability costs $s n_1+t n_2+o(n)$. At a constrained maximizer $s=a$, the short positive root of $D(a,t)=1$ is
$$
h=\log\frac{b e^a+w e^{-a}}{d e^a+b e^{-a}}.
$$
For $0\le\kappa<1/2$, $0<h\le a$. Under the one-coordinate tilt $(a,0)$ the means are $2P-1$ and $(2\kappa-1)(2P-1)$. Thus one can first advance the long coordinate while the reflected short coordinate stays $o(n)$. Under $(a,h)$, the short mean is positive and the two means, $v_x,v_y$, satisfy $v_x\ge v_y>0$. The supporting-normal condition gives $\gamma\ge v_x/v_y$. Switch tilts at long position $(\gamma-v_x/v_y)n$, then use the two-coordinate tilt to reach the endpoint. At $\kappa=0$ this is the independent two-leg construction. For $\kappa\ge1/2$ in (1), the direct-path regime extends to $\gamma(2\kappa-1)=1$, where $(a,0)$ already has the target slope. These statements follow by strict convexity and the preceding signs on $D(a,t)=1$. The upper-bound rectangle contributes no other active edge at positive target slope.

Here and below a tilted path can be kept inside the relevant open region until an $O(\varepsilon n)$ terminal segment. Insert $O(\varepsilon n)$ initial steps for a buffer from $K_D$, scale an incoming path to leave $O(\varepsilon n)$ room at its endpoint, and use the law of large numbers for the finite-step distributions. On a reflected coordinate with negative input drift, its maximum draw-up over $O(n)$ time is $o(n)$ in probability. This follows from gambler's ruin and a union bound, or from the uniform law of large numbers for the input and the reflection formula. With positive drift a reflecting start changes the endpoint by $o(n)$ in probability. The tilts of nonzero reflected local time are used only on buffered coordinates or where the tilt is zero. Any remaining coordinate deficits of size $O(\varepsilon n)$ can be paid for with $O(\varepsilon n)$ prescribed steps. When the short player starts cooperating, a mixed cooperator win and defector loss have positive probability. A possible earlier long switch is handled by the exchanged mixed event. Send $\varepsilon$ to zero. These modifications avoid a return to $K_D$ before success.

For (4), in each last-zero ordering use tilt $a$ on the coordinate departing first and $h$ on the second. They give $D(a,h)=1$, $h>a$, and both mixed multipliers are at most one. The two costs are $a n_1+h n_2$ and $h n_1+a n_2$, whose minimum is the former. In the lower construction the short mean of the $(a,0)$ tilt is negative. Under $(a,h)$, $v_y>v_x$ by symmetry and $v_y>0$ because $h$ is the upper root. The assumed $v_x\ge0$ puts the start of the second segment, $(\gamma-v_x/v_y)n$, inside the long player's D interval. At $v_x=0$ use an $O(\varepsilon n)$ buffer. This proves (4).

## A negative short tilt through the actual switching interface

Suppose $\gamma(2\kappa-1)>1$. For any strict feasible pair in (2) with $s>0,\ t<0$, let $z=e^t$ and $m=m_T(s)$. Since $S\le1/2$, $S z+(1-S)/z>1$, so $0<m<1$. The short cooperator's discounted return factor on a half-line is the smaller root
$$
z_C^-=\frac{2m(1-S)}{1+\sqrt{1-4m^2 S(1-S)}}\quad\text{of}\quad
m S z^2-z+m(1-S)=0.
$$
Strict feasibility gives $z_C^-<z$. For the finite C half with its reflecting deep cap let $h_n(k)=\mathbb E_k[m^{\tau_0}]$, where $0$ is the last short-D site and $k=1,\ldots,n$ are its C sites. Then $h_n(1)\to z_C^-$. Indeed the infinite and finite paths coincide until the distant cap, and the contribution from that event is bounded by $m^{n-1}$ for each walk. Choose $c_n=(z-h_n(1))/(1-h_n(1))$, uniformly positive for large $n$. Define a positive test function of the short coordinate by

$$
 f_n(y)=
 \begin{cases}
 e^{t y}, &0\le y\le n-1,\\
 e^{t(n-1)}[c_n+(1-c_n)h_n(y-n+1)],& n\le y\le 2n-1 .
 \end{cases}
$$

At the switching edge $f_n(n)/f_n(n-1)=z$. While the long player remains D and is above its bottom, $e^{s X}f_n(Y)$ is a supermartingale. In DD the interior multiplier is $D\le1$. Reflection at short zero helps because $t<0$. In the mixed half, independence factors out the longitudinal $m$, the discounted return function satisfies the first-step equation including reflection, and the added constant has multiplier $m<1$. Everywhere $c e^{tn}\le f_n\le1$ with fixed $c>0$.

On the last departure of the long coordinate from zero before its *first* C action, this weight is at most $e^s$. At that first C action it is at least $c e^{s n_1+t n}$, for every possible short state. Summing over last departures in the polynomial time window bounds the probability of first CC, which requires this long switch. Boundary values of (2) follow by scaling $(s,t)$ towards the origin and taking the limit. At $t=0$ use $f_n=1$. This argument includes arbitrarily many intervening short action changes.

## The matching paths at the switch

Use $A_D=d e^s+b e^{-s}$ and $B_D=b e^s+w e^{-s}$, so $D=A_D e^t+B_D e^{-t}$. For $s\ge a$, let $t_D(s)$ be the upper root of $D(s,t)=1$, up to the rightmost point of its sublevel set. With $1/2<\kappa<1$, $t_D(a)=0$ and $D_t(a,0)>0$. The upper boundary is strictly concave and decreases to the right. On $t\le0$ the mixed kernel decreases strictly with $t$. Hence a given $s$ can be feasible only when its upper boundary $t_D(s)$ is feasible, and the feasible projection in $s$ is an interval by convexity. The point $s=a$ has strict mixed slack. At the origin of this interval the objective increases to the right because $\gamma>1/(2\kappa-1)$. The maximizer in (2) is the bulk maximizer or its truncation at the first mixed intersection. In the former case the incoming DD tilt has positive mean vector parallel to $(\gamma,1)$, so the straight path above achieves the bound.

In the strictly truncated case write $(u_x,u_y)=\nabla D(s_I,t_I)$ and $(v_x,v_y)=\nabla C(s_I,t_I)$. Then $u_x,u_y>0,\ v_y<0,\ \gamma>u_x/u_y$. At the intersection the mixed lower-root graph crosses the DD upper-root graph with strictly larger derivative. To see strictness, their difference is convex and starts strictly below zero at $s=a$. Implicit differentiation gives
$$
 \bar v_x=\frac{-v_y u_x+u_y v_x}{u_y-v_y}>0.
$$

First follow the tilted DD path with velocity $(u_x,u_y)$ to the short threshold, at long position $(u_x/u_y)n+o(n)$. On the infinite strip around that threshold, let the tilted transition law multiply each original signed step by $e^{s_I\Delta X+t_I\Delta Y}$ in both profiles. Both row sums equal one. The normal coordinate is a birth–death chain with mean $u_y>0$ in the DD half and $v_y<0$ in the mixed half. It is positive recurrent with geometric tails and its stationary mass on the DD side is $-v_y/(u_y-v_y)$, since its mean increment vanishes. The long coordinate obeys the law of large numbers with positive speed $\bar v_x$, by regeneration at the interface. The same conclusion follows from the ergodic theorem and the bounded-increment martingale for conditional means. Over $O(n)$ steps the normal displacement stays $o(n)$ with probability tending to one, by the geometric excursion tails. Thus the strip can be used inside the finite game until the long player is within $O(\varepsilon n)$ of its switch. A bounded or $O(\varepsilon n)$ join at the interface absorbs any microscopic endpoint mismatch from the incoming path, at a cost $O(\varepsilon n)$.

The likelihood factor for both segments telescopes to $e^{-s_I\Delta X-t_I\Delta Y}$, yielding total cost $s_I n_1+t_I n+o(n)$ after the terminal adjustment. If the constraints meet exactly at the bulk optimizer, its direct path suffices. For $\kappa=1$, $D=m_P(s+t)$. Until the short switch the two DD coordinates advance synchronously from $K_D$, giving the incoming direction $(1,1)$. After the switch the same tilted strip proof applies at $s+t=a$ for $\gamma>1$. With identical finite memories one biased walk reaches both switches together. If $\gamma=1$ with unequal finite memories, relabel the shorter player when necessary, take the synchronous path to its first switch, then require $|n_1-n_2|=o(n)$ successive mixed wins for the new cooperator and losses for the remaining defector. This costs $o(n)$ in negative log probability. This proves (2) and (3).

The same interface condition can be read from its first-return transform. Set $A_C=S m_T(s)$, $B_C=(1-S)m_T(s)$ and denote the upper DD and lower mixed roots of $A_j z^2-z+B_j=0$ by $z_D^+$ and $z_C^-$. Starting at the last short-D site, the transform of one first return in the unbounded strip is
$$
 \mathcal R(s)=B_D/z_D^++A_D z_C^- .
$$
A step to the DD side returns with transform $1/z_D^+$. A step to the C side returns with transform $z_C^-$. Both follow by the one-dimensional first-step quadratic, choosing the minimal positive root for a hitting transform. At the interface optimum $z_D^+=z_C^-$, so $\mathcal R(s_I)=1$.

For the frozen stationary exceedance entry in the table, the long marginal alone gives the lower bound $2a$ on its cost. Under the long tilt $(a,0)$, accumulating $2n$ units in that coordinate accumulates $2(2\kappa-1)n>n$ in the other. The free-duration input path realizes the matching joint exceedance in the stationary reflected chain, by the usual backward-supremum representation of Lindley's recursion. For the endpoint entry, a negative short tilt only improves the exponential upper probability bound at the short reflecting edge. Starting at the last long departure and stopping at the corner gives the bulk support bound $H$. Its normal tilt follows the straight interior path and realizes it. Where exact simultaneous terminal lattice sites are required, the nonzero off-diagonal DD steps and an initial single-coordinate reflection allow a parity adjustment at bounded cost.

## An independent random choice at each weak loss

Let a weak loss change the action with fixed probability $u\in(0,1]$, and otherwise leave the player at its current weak state. Choices are independent across players and times. Tsetlin's $B$ has $u=1/2$. Equations (1) and (4) hold for this entire family. In their supermartingales the tilts are nonnegative, so suppressing a weak D switch can only decrease the charged increment. A weak C coordinate remains clipped until it actually crosses. The lower paths can prescribe each required random switch during the short terminal adjustment at a cost $O(\varepsilon n)$. In the regeneration proof, for $S<1/2$ one reaches the weak cooperator state from a mixed state in $O(n)$ steps with uniformly positive probability and then requires an appropriate loss with a successful switch; at the fair endpoint $S=1/2$ (where the exact mean switch time from deepest cooperation is $n(n-1)+2n/u$), one uses $O(n^2)$ blocks, requires one accepted weak loss, and truncates at $n^4$ with discarded probability $e^{-\Omega(n^2)}$, exactly as in the $L$ fair-endpoint argument above. For the reverse transition from $K_C$, the marginal excursion to the weak edge incurs the same cost $a_R$, and one additional loss that changes action suffices. These changes preserve the stationary-odds identity.

In the remaining strong-correlation regime use the upper DD root $z_D(s)=e^{t_D(s)}$ and the lower C root $z_C(s)$ of $A_C z^2-z+B_C=0$, with $A_C=S m_T(s)$ and $B_C=(1-S)m_T(s)$. Put
$$
\Phi_u(z)=(1-u)+\frac{u^2 z}{1-(1-u)z}.
$$
For $1/2<\kappa<1,\ \gamma(2\kappa-1)>1$, the exact cost is
$$
 V_u=\max_s\{\gamma s+\log z_D(s):
 a\le s\le a_T,\quad 4A_D(s)B_D(s)\le1,\quad
 z_D(s)\ge\Phi_u(z_C(s))\}.
 \tag{5}
$$
The $s$ interval uses the rightward DD branch starting at $a$. For $\kappa=1,\ \gamma>1$, use $z_D(s)=e^{a-s}$ in (5). There is a unique active cutoff $s_{I,u}>a$ determined by
$$
 e^{a-s_{I,u}}=\Phi_u(z_C(s_{I,u})),\qquad
 V_u=a+(\gamma-1)s_{I,u}.
$$
At $\gamma=1,\kappa=1$ the cost is $a$ for every $u$. Thus perfect DD synchrony gives the same threshold expression as (3) on replacing $s_I$ by $s_{I,u}$. For $B$, $\Phi_{1/2}(z)=1/(2-z)$.

To prove (5), place the normal coordinate $k=0$ at the weak D site and $k=1$ at the weak C site. Starting at $1$, the transform for the first return to $0$ in the infinite C half is
$$
 g_C=\frac{uB_C}{1-A_C z_C-(1-u)B_C}
     =\frac{u z_C}{1-(1-u)z_C}.
$$
Indeed an upward step must first return from site 2, a weak loss may hold at 1, and a successful weak loss returns directly to 0. At site 0 the effective factor for a DD upward step is $(1-u)+u g_C=\Phi_u(z_C)$.

For the upper probability bound take an $s$ satisfying the interface inequality strictly, with $s>a$, and write $m=m_T(s)<1$. The finite-C discounted return function $h_n(k)=\mathbb E_k[m^{\tau_0}]$ now uses the weak C toss. It has $h_n(1)\to g_C$ by the same distant-cap estimate. Put $\rho=(z_D-(1-u))/u$, so $g_C<\rho\le1$. Use the previous short test function with $t=\log z_D$ and $c_n=(\rho-h_n(1))/(1-h_n(1))$. Its C-to-D boundary values have ratio $f_n(n)/f_n(n-1)=\rho$. At the weak D site the upward factor is exactly $(1-u)+u\rho=z_D$. The mixed side is superharmonic by its own finite return equation. A weak long D loss blocked by its own coin can only lower $e^{s\Delta X}$. Independence of its coin allows this inequality also when both automata are weak. The first-long-switch bound follows with exponent $\gamma s+\log z_D$. Approximate a binding endpoint from its feasible left side. This works because $\log z_D(s)$ is concave, $\log z_C(s)$ is convex as the lower boundary of a convex sublevel set, and $v\mapsto\log\Phi_u(e^v)$ is increasing and convex by its positive exponential series. At $s=a$ the inequality is strict. The objective increases until its bulk optimum. Its constrained optimizer is therefore the bulk point or its truncation at a single cutoff.

For a strict truncation the infinite-strip tilted kernel multiplies each step by $e^{s_{I,u}\Delta X}H(k')/H(k)$, where
$$
 H(k)=
 \begin{cases}
 z_D^k,&k\le0,\\
 g_C z_C^{k-1},&k\ge1 .
 \end{cases}
$$
Both interior root equations and the two weak-edge equations give row sums one. In the normal direction the bulk drifts point toward the switching edge, including at $\kappa=1$. The finite changes at the two weak sites preserve positive recurrence, geometric excursion-height tails, and a finite mean return time. For $\kappa<1$ a strictly active truncation occurs before the unconstrained optimum and hence before the DD root coalesces, so the normal drift on the DD side is strictly positive. The mixed lower root has negative normal drift.

For the mean longitudinal increment per return, differentiate the first-return transform at the cutoff. For all $s$ in a neighborhood of an active interior cutoff this transform is
$$
 \mathcal R_u(s)=B_D/z_D+A_D\Phi_u(z_C).
$$
The first term accounts for a left DD excursion. The second includes both a weak D hold and a crossing into the C excursion. At $a$, $\mathcal R_u(a)<1$, while $\mathcal R_u(s_{I,u})=1$ by matching. Since it is a sum of positive longitudinal exponential moments, it is convex. Both roots have nonzero discriminant at the active point, so its derivative there exists and is strictly positive. Return paths under the tilted law have exactly the longitudinal likelihood factor $e^{s_{I,u}\Delta X}$, because their initial and final $H$ values agree. Thus $\mathcal R_u'(s_{I,u})>0$ is their mean longitudinal increment. Concatenate the incoming straight DD path with the tilted recurrent path as above. Its incoming cost uses $\log z_D$, and the bounded or sublinear endpoint mismatch in $H$ costs $o(n)$. This proves the matching lower probability bound. When the cutoff coincides with the bulk optimum the incoming straight path suffices.

Since $\Phi_u(z)-z=(1-u)(1-z)^2/[1-(1-u)z]\ge0$, (5) gives $V_B\le V_L$ throughout the positive-correlation weak-sucker regime. The inequality can change the selected pure profile. For
$$
 P=.6,\quad R=.78,\quad T=.9,\quad S=.2,\quad
 \kappa=.99,\quad \gamma=2
$$
one obtains
$$
 V_B=1.15386227926998031783
 \;<\; a_R=\log(39/11)=1.26566637333127588339
 \;<\; V_L=1.38348782377731947056 .
$$
Consequently $B$ concentrates on CC and $L$ on DD at the identical joint outcome law. The script validates the ordering with rational arithmetic. It also solves the finite $B$ first-CC Dirichlet problem at 80-digit precision for $n=3$. The sparse secant between $n=64$ and $80$ is $1.15386227919273$. [Kernel, exact inequalities, and finite games](../experiments/phase1_interface.py)

At $(n_1,n_2)=(80,40)$, the two finite-game first-CC probabilities in this example admit the following certified rounding.

| Tactic | Probability before a strict return to deepest DD | Width of enclosing rational interval |
|---|---:|---:|
| $L$ | $1.25381701957350534793313981274169802719428332643933805688890838080987578407\times10^{-25}$ | $<1.943\times10^{-112}$ |
| $B$ | $5.92352609835928960409523655919805994310261045299981696442880985753227193736\times10^{-22}$ | $<1.925\times10^{-112}$ |

The transient matrix has 9,599 states. The script clears denominators from the rational Dirichlet system $Av=b$, where $A=I-Q$, and refines an integer approximation on a $10^{-115}$ grid. A floating-point factorization proposes each correction. It then verifies each component of $AY\ge\mathbf1$ for a nonnegative rational vector $Y$, and computes the residual $b-A\widehat v$ exactly with integers. Since $A^{-1}$ is nonnegative,
$$
 \|v-\widehat v\|_\infty
 \le \|Y\|_\infty\,\|b-A\widehat v\|_\infty .
$$
The same bound applies to the probability after the initial step. Both rational endpoints round to the 75 significant digits displayed.
