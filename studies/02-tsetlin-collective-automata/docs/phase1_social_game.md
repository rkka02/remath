# Independent outcomes in symmetric two-player games

## Results and hypotheses

Two identical automata update simultaneously. At each date their wins are conditionally independent given the current actions, with independent innovations across dates. An agent has depths $0,\ldots,n-1$ in each action. A win increases depth by one with clipping at $n-1$. A loss decreases positive depth by one. At zero depth a loss switches action with probability $u$, otherwise leaving the agent at zero. Here $u=1$ is the linear tactic $L$ and $u=1/2$ is $B$ with independent private boundary coins. The proofs work for any fixed $0<u\le1$.

Write $R,P,S,T$ for the focal player's win probabilities in $CC,DD,CD,DC$, respectively. All lie strictly between zero and one. Let $H(x)=\log(x/(1-x))$, and let $r,p,s,t$ be $H(R),H(P),H(S),H(T)$. Let $\pi_R,\pi_P,\pi_M$ denote stationary action masses for $CC,DD,\{CD,DC\}$.

1. **All four probabilities exceed one half.** For any symmetric game in this sector, set

   $$
   W_R=p+\min(t,p+s),\qquad W_P=r+\min(s,r+t),\qquad W_M=r+p.
   $$

   For each $i,j$, $\lim n^{-1}\log(\pi_i/\pi_j)=W_j-W_i$. A unique minimum has stationary mass tending to one. If $M$ wins, its two orientations each have limiting mass $1/2$.
2. **The cooperator in a mixed profile has nonpositive drift.** If $R>1/2$, $T\ge P>1/2$ and $S\le1/2$, then

   $$
   \lim_{n\to\infty}\frac1n\log\frac{\pi_R}{\pi_P}=r-2p,\qquad
   \pi_M\longrightarrow0 .
   $$

   This includes $S=1/2$. For $S<1/2$ the stronger estimate is $\pi_R/\pi_P=\Theta(e^{n(r-2p)})$. In particular both homogeneous action masses are bounded away from zero on $r=2p$ in this sector. The full-chain bound counts all temporary single-agent switches.
3. **Strict Prisoner's Dilemma with $P>1/2$.** Suppose $T>R>P>S$. Define

   $$
   b=\begin{cases}
   2p,&S\le 1/2,\\
   \min(2p,p+t-s),&S>1/2 .
   \end{cases}
   $$

   The sharper relation is $\pi_R/\pi_P=\Theta(e^{n(r-b)})$. In particular both pure profiles retain positive lower limiting mass at $r=2p$, including $S=1/2$. When $S>1/2$, $p+t-s>t>r$. The slope therefore always has the sign of $r-2p$. In particular, $\pi_R\to1$ for $R/(1-R)>(P/(1-P))^2$ and $\pi_P\to1$ for the reversed inequality. A sequential escape can accelerate visits to cooperation in a defection phase. The inequality shows why that mechanism cannot create a cooperation phase in a strict Prisoner's Dilemma.
4. **Stag Hunt and Chicken.** For a conventional Stag Hunt $R>T>P>S>1/2$, the mixed mass vanishes and the winning homogeneous profile compares $r$ with $\min(2p,p+t-s)$. A sequential escape can select cooperation when $r<2p$. For a conventional Chicken $T>R>S>P>1/2$, $W_P>W_M$, and $CC$ wins when $r>p+s$. When $r<p+s$ the two mixed profiles win. The stationary odds of $CC$ versus $DD$ alone therefore do not determine the winner in Chicken.

The formulas determine exponential orders on ties. Items 2 and 3 give the stated bounded-factor coexistence results. Exact limiting mixture weights, arbitrary mixed-sign games outside item 2, and correlated shocks require separate analysis.

## Historical attribution

Volkonskii restricted his analysis to independent outcomes. In §6, printed pp. 46–47, he pointed out that two closely spaced changes can invalidate a return to deep states between action changes. He asserted an order estimate up to constant factors for symmetric two-player linear and Krinsky automata, omitted its proof, and displayed the three stationary weight sums. Their logarithmic exponents are exactly $W_R,W_M,W_P$ above. Item 1 gives a proof of the logarithmic statement for the present update conventions. The extension across $S=1/2$ in item 2 is outside the positivity hypothesis in §6. Later work on auxiliary chains by Gurvich is relevant to any broader priority claim. [Volkonskii, 1965, Russian original, pp. 46–47](../sources/papers/Volkonskii_1965_PPI_1_AsymptoticAutomataGame_rus.pdf) · [Math-Net bibliographic record](https://www.mathnet.ru/eng/ppi735) · [Gurvich, 1975](https://www.mathnet.ru/eng/at7793)

## The all-reinforcing proof

### Deep-state excursions

A core is a joint state with both agents at depth $n-1$. Record the chain at every visit to the set of four cores, including consecutive visits at consecutive dates. Interchange symmetry makes the three classes $R,M,P$ of this trace a Markov chain. Its invariant law is the stationary distribution of the original chain conditional on the core set, with both mixed cores summed.

From any state in a profile there is a probability $c>0$, uniform in $n$, of reaching that profile's core without changing action within $Cn$ steps. Fix a large integer $k$. First require $k$ wins for each player. For an inward-drifting player with win probability $x>1/2$, the probability of losing its $k$-step buffer before reaching greatest depth is at most $((1-x)/x)^k$. With $C$ large, a player that survives this first trip reaches greatest depth by $Cn/2$ with uniformly high probability, by the law of large numbers. After reaching greatest depth, the chance of switching by $Cn$ is $O(n e^{-nH(x)})$ by biased gambler's ruin and a union bound over attempts. The deficit from greatest depth at any fixed time after first arrival is bounded by the reflected constant-$x$ walk on the nonnegative integers in stationarity. The latter has upper tail $((1-x)/x)^k$. Thus with uniformly positive probability both deficits are at most $k$ at time $Cn-k$ without any previous action change. Requiring $k$ final joint wins puts the pair in the specified core. A smaller $c$ handles the finitely many small $n$.

The Markov property in blocks of $Cn$ bounds the probability that a core excursion lasts longer than $n^3$ by $e^{-c'n^2}$. Its expected duration is $O(n)$. The construction reaches its core at a prescribed time $\lceil Cn\rceil$ with probability at least $c$ from every state in that profile. Stationarity therefore gives $c\pi_i\le\pi_{i,\mathrm{core}}\le\pi_i$. It suffices to calculate the exponential orders in the three-state trace.

### One- and two-player changes

Write $\operatorname{cost}(a_n)=-n^{-1}\log a_n$. Cost comparisons below allow $o(1)$ errors. On a fixed polynomial horizon an initially deepest coordinate whose win probability is always at least $x>1/2$ flips with probability at most $\operatorname{poly}(n)e^{-nH(x)}$. Until the first flip its deficit is bounded by the reflected constant-$x$ walk driven by its own independent uniforms. A geometric stationary upper tail and the union bound give the estimate. A partial boundary switch only delays this first flip. Two necessary events defined by different independent uniform streams have probability bounded by the product of their bounds.

The following estimates suffice for the trace.

| Transition | Lower bound on cost | Upper bound on cost |
|---|---:|---:|
| $R\to M$ | $r$ | $r$ |
| $P\to M$ | $p$ | $p$ |
| $R\to P$ | $r+\min(r,s)$ | $2r$ |
| $P\to R$ | $p+\min(p,t)$ | $2p$ |
| $M\to P$ | $\min(s,t+r)$ | $s$ |
| $M\to R$ | $\min(t,s+p)$ | $t$ |

For $P\to R$, both original defectors must have flipped. The first experienced only $P$ while both remained defectors. The player who flips second experienced $P$ or $T$ up to its first flip, including during temporary returns of the first player. Apply the two independent dominating walks and sum over both orders. This proves the lower bound, including simultaneous flips. The argument for $R\to P$ interchanges action labels. For $M\to R$, if the original defector flips first, it has experienced only $T$. If the original cooperator flips first, that costs at least $s$, and the original defector must still flip under win probabilities at least $\min(T,P)$. The lower bound is $\min(t,s+\min(t,p))=\min(t,s+p)$. The formula for $M\to P$ follows by the same interchange. Truncating excursions at $n^3$ adds a superexponentially small probability.

For the constructive estimates, an initially deepest player can be forced to switch before revisiting greatest depth with probability at least $\exp[-nH(x)-o(n)]$. Take $m=\lceil n^{2/3}\rceil$. Force $m$ initial losses, then interchange the win/loss probabilities until a deterministic time $(n-3m)/(2x-1)+O(1)$ later. Under the tilted law the centered partial sums stay within $m/3$ with probability tending to one. The path stays away from both endpoints throughout this segment, finishes within $O(m)$ of the other end, and has likelihood ratio $\exp[-nH(x)+O(m)]$ under the original law, including the cost of the prescribed steps. Complete the switch with $O(m)$ forced steps. A nonswitching partner retains its action with probability tending to one over this $O(n)$ segment, since it started deepest. The new reinforcing profile reaches its core with uniformly positive probability. For a joint switch out of a homogeneous state apply the tilt to both independent streams. Before encountering endpoints the two deficits have equal parity at a common time. Use pairs of opposite increments in the last $O(m)$ steps to align both first switches on one date. Fixed private boundary choices contribute a constant factor. This gives costs at most $2p$ or $2r$ for a direct switch.

### Stationary weights

The finite Markov-chain tree theorem gives each stationary weight as a sum of products of two trace transitions. For root $R$, the trees are $P\to M\to R$, $M\to P\to R$, and both other vertices pointing to $R$. The first costs at least $p+\min(t,s+p)$. The second costs at least $p+\min(p,t)+\min(s,t+r)$, which is at least $p+\min(t,s+p)$. The lower bound on the third is at least that on the first. Conversely the first costs at most $p+t$ and the second at most $2p+s$. Hence $W_R=p+\min(t,p+s)$. Interchanging $C,D$ gives $W_P=r+\min(s,r+t)$. For $M$, both homogeneous vertices can point directly to $M$ at cost $r+p$. Every tree pays at least this much for their two exits. The equivalence of action and core exponents proves item 1.

## A nonreinforcing cooperator in a mixed profile

Assume $R>1/2$, $T\ge P>1/2$ and $S\le1/2$. Use only the two homogeneous deep cores. From $CC$ and $DD$ the fixed-profile argument still gives a uniform probability of reaching the corresponding core within $Cn$ steps. In a mixed state the defector has probability bounded below of remaining a defector for $Cn^2$ steps. This follows from the buffer argument with $x=T$ and a polynomial horizon. The cooperator switches to defection within this time with uniformly positive probability. At $S=1/2$, the expected time from any depth to a switching loss is $O_u(n^2)$ by the unbiased gambler's-ruin recurrence with a reflecting deepest end. A smaller $S$ only speeds the switch. These two stopped walks use independent streams. From the newly formed $DD$ profile the fixed-profile construction applies. Thus excursions between homogeneous cores have expected length $O(n^2)$ and tail at $n^4$ at most $e^{-c n^2}$.

Encode each coordinate from $0$ (deepest $D$) through $n-1$ (weakest $D$), $n$ (weakest $C$), to $2n-1$ (deepest $C$). Start two independent comparison chains $Y_i$ at zero with upward probability $1-P$ on the $D$ side and $v=\max(1-P,S)$ on the $C$ side. Use clipped endpoints and the original $u$ rule for an interface loss. Each game coordinate is at most its $Y_i$ up to and including the first $CC$. Indeed, the upward probability for a game defector is $1-P$ or $1-T\le1-P$, and for a cooperator before that hit it is $S\le v$. The upper chain's kernel is increasing in its starting state. At the interface the cross-edge comparison requires $u(1-P)\le1-u(1-v)$, which follows from $v\ge1-P$. Other nearest-neighbor comparisons follow by clipping and from the holding probability at an incomplete switch. Coupling by the inverse distribution at each step preserves this order, with independent comparison streams.

By detailed balance the stationary mass of the $C$ side of one comparison chain is at most

$$
C e^{-np}\sum_{j=0}^{n-1}\left(\frac{v}{1-v}\right)^j.
$$

The factor $u$ cancels from the interface ratio. Since $v\le1/2$, this bound is $O(ne^{-np})$. Starting at the least state gives domination by the stationary law at every fixed time. Thus

$$
\mathbb P_{P_{\rm core}}(\tau_{CC}\le L)\le C L n^2 e^{-2np}.
$$

This includes every temporary switch of a single agent. Taking $L=n^4$ and using the core tail gives cost at least $2p$ for the trace $P\to R$. The synchronized tilted path attains $2p$. For $R\to P$, the first change costs at least $r$. A single tilted change at cost $r$ leads to a mixed state, from which the preceding construction reaches $DD$ before revisiting $CC$ and then reaches its core with uniformly positive probability. Hence this trace transition has cost $r$.

The two-state invariant odds give $r-2p$ for the homogeneous-core and homogeneous-action odds. In one excursion the chance of any action change before the next homogeneous core is bounded by a polynomial times $e^{-n\min(p,r)}$, by the one-player bound up to the first change and truncation at $n^4$. Conditional on the first change the expected remaining excursion is $O(n^2)$ uniformly. The trace occupation formula bounds stationary mixed mass by a polynomial times $e^{-n\min(p,r)}$, proving item 2.

### Bounded factors away from the neutral mixed drift

For $S<1/2$ the fixed-$n$ two-state trace in the preceding proof has
$$
K_{PR}=\Theta(e^{-2np}),\qquad K_{RP}=\Theta(e^{-nr}).
$$
To sharpen the upper bound on $K_{PR}$, use the comparison pair $Y$ with origin $o=(0,0)$. If the true game reaches $CC$ before returning to the $DD$ core, $Y$ must visit $A=\{n,\ldots,2n-1\}^2$ before its own first return to $o$. Indeed, any earlier $Y=o$ forces the game to be at its $DD$ core by coordinatewise domination. The expected number of visits to $A$ in an $o$-excursion of $Y$ is exactly $\mu(A)/\mu(o)$, where $\mu$ is the product stationary law. For $S<1/2$ we have $v<1/2$, and the geometric sum in the one-coordinate detailed-balance formula is bounded uniformly in $n$. Thus $\mu(A)/\mu(o)=O(e^{-2np})$. The same occupation identity in the fixed $CC$ rectangle bounds the chance of visiting a state with at least one weakest cooperator before returning to its deep core by $O(e^{-nr})$. For this upper bound reflect at the weakest depth; paths up to the first visit there are identical in the true and reflected rectangles.

For the matching lower bounds, the homogeneous kernel killed at the first action change is a product of reversible one-dimensional substochastic kernels. In deficit coordinates measured from the deepest end, its reversible measure is proportional to $\exp[-H(x)(i+j)]$, where $x=P$ or $R$. Write $Q$ for this killed chain, $o$ for its deepest corner, and $z$ for another point. Reversing every path whose interior avoids $o,z$ gives
$$
\mathbb P_o^Q(\tau_z<\tau_o^+)=
e^{-H(x)(z_1+z_2)}\mathbb P_z^Q(\tau_o<\tau_z^+),
$$
where both events require survival until the stated hit. For the $DD$ rectangle choose $z=(n-1,n-1)$. Its reverse probability is bounded below by a positive constant independent of $n$. Force both inward for a fixed $k$ steps, after which the probability of either returning to a weakest position before its first deep-end visit is at most $2e^{-pk}$. The fixed-time core construction then succeeds with positive probability while avoiding both weakest edges. In detail, after each first deep visit use the geometric upper tail, discard an $O(ne^{-np})$ chance of a weakest-edge visit before time $Cn$, and require a fixed number of final joint wins. From $z$ in the forward direction two switching losses followed by reinforcement in $CC$ reach the other core with uniformly positive probability. This proves $K_{PR}\ge c e^{-2np}$.

For the $CC$ rectangle choose $z=(n-1,0)$. The same reverse argument gives a constant lower bound. From $z$ a switching loss for the weakest cooperator and a win for its partner enter the mixed profile. With uniformly positive probability this reaches $DD$ and its core before returning to $CC$, as established above. Hence $K_{RP}\ge c e^{-nr}$. The fixed-time core bound transfers the trace odds to action odds up to constants. Together with $\pi_M\to0$ this proves coexistence on the critical curve. The logarithmic correction in the independent, $S<1/2$ stationary log-odds is $O(1)$, so its $\log n$ coefficient is zero. This bound does not identify the limiting multiplicative constant.

## A bounded-factor estimate for the entire independent Prisoner's Dilemma

Suppose $T>R>P>S$, $P>1/2$. Count excursions from the deepest $DD$ core $o$ up to its next return or the first $CC$ profile. Let $N=n-1$, $q=1-P$, $q_T=1-T$, and let $j=0,\ldots,N$ denote a defector's deficit from greatest depth. A lone switch out of $DD$ creates a new cooperator and leaves a defector at some $j$ after the same update. We first bound how often such entries occur. To obtain an upper bound, also stop as soon as that remaining defector flips during a mixed bout, including a simultaneous exchange of roles. Every path to $CC$ either encounters this stopping event or flips both agents directly out of $DD$.

**Boundary entry count.** For either choice of the new cooperator, the expected count $F(j)$ of these lone entries before stopping or returning to $o$ obeys
$$
F(j)\le C e^{-pn}\xi_j,\qquad
\xi_j=e^{-pj}\bigl(1-uq\,\mathbf 1_{\{j=N\}}\bigr).
$$
The constant is independent of $n$ and $j$. The proof permits arbitrarily many cooperative bouts of unrestricted duration.

Freeze the $DD$ profile by reflecting both agents at their weakest $D$ depth. Mark each outward loss for which its private switch coin succeeds. In the frozen product's stationary law the two coordinates are independent with marginal proportional to $e^{-pj}$. A single mark of a specified agent leaves the other at $j$ with stationary flux proportional to $e^{-pN}uq\,\xi_j$. Indeed the second coordinate has marginal proportional to $e^{-pj}$ after its update, and the excluded second mark ends at $N$. The stationary flux of a double mark is proportional to $e^{-2pN}(uq)^2$, with the same product normalization.

Let $H$ be the substochastic kernel starting immediately after an actual mixed bout returns to $DD$. One tagged agent is now at weakest $D$, the other is at $j$. Run frozen $DD$ to the next single mark, killing on a visit to $o$ or a double mark. The output records the new tagged agent and the other agent's updated deficit. Then $\xi H\le\xi$ componentwise, using one copy of $\xi$ for each tag. To see this, in a stationary frozen trajectory pair each single mark with the next one only when no double mark or $o$ intervenes. Each output single mark has at most one predecessor. Dividing the two stationary fluxes by their common factor proves the inequality. The same counting with a double output gives $\xi H_{\rm double}\le C e^{-pn}$, where $H_{\rm double}$ is the chance that a double is next, before $o$ or a single. The first lone mark from $o$ before return has measure $F_0(j)\le C e^{-pn}\xi_j$ by the excursion occupation identity for marked transitions of the frozen chain. The first direct double similarly has probability at most $C e^{-2pn}$.

To pass through a mixed bout, let $\tau$ be the time to a switching loss for its new cooperator started at weakest $C$, with win probability $S$. Let $Q$ be the substochastic single-defector kernel with win probability $T$, killed at its first switching loss. These two processes are independent while the profile is fixed. The subkernel for a return to $DD$ is $A=\mathbb E Q^\tau$, preserving the identity of the tagged agent. The strict inequality $T>P$ yields constants $\lambda<1$, $C_1<\infty$ such that for every $k\ge1$
$$
(\xi Q^k)_j\le\lambda^k\xi_j+C_1e^{-tj}.
$$
For $1\le j<N$, the ratio $(\xi Q)_j/\xi_j$ is at most $q_T e^p+T e^{-p}<1$. At the terminal point $N$ the ratio is
$$
q_T\left(\frac{e^p}{1-uq}+1-u\right)<1.
$$
To check the inequality, replace $q_T$ by $q$. Then the result is at most one, since $P/(1-uq)+(1-u)q-1=-u(1-u)q^2/(1-uq)\le0$. Thus $\xi Q\le\lambda\xi+C_2\delta_0$. The killed kernel is reversible with weights $e^{-tj}$, so $(Q^\ell)_{0j}=e^{-tj}(Q^\ell)_{j0}\le e^{-tj}$. Iteration proves the bound. Since $\tau\ge1$, it follows that $(\xi A)_j\le\lambda\xi_j+C_1e^{-tj}$.

The total count of lone entries from $o$ has expectation $O(e^{-pn})$. Its first occurrence has this bound by $F_0$. After each subsequent return to $DD$ there is a uniform positive probability of reaching $o$ without any action change, by fixed-profile reinforcement. Thus the number of further entries is bounded by a geometric tail. For the counts $F_m$ through at most $m$ entries we have $F_1=F_0$ and $F_{m+1}=F_0+F_m A H$. Pick $\lambda'\in(\lambda,1)$. For all $j$ larger than a fixed $J$, $\lambda\xi_j+C_1e^{-tj}\le\lambda'\xi_j$ because $t>p$. If $F_m\le K e^{-pn}\xi$, this gives $F_m A\le \lambda'K e^{-pn}\xi$ for $j>J$. For $j\le J$ the bound on total counts gives $F_m A\le C_3 e^{-pn}\xi$ with $C_3$ independent of $K$. Apply $\xi H\le\xi$, choose $K\ge\max(C_0/(1-\lambda'),C_0+C_3)$ where $F_0\le C_0e^{-pn}\xi$, and take the limit in $m$. This proves the boundary entry count and also $F A=O(e^{-pn}\xi)$.

**Chance to finish.** From a lone entry with other defector at $j$, the probability it flips before or on the cooperator's return is at most
$$
C\left(e^{-t(n-j)}+e^{-tn}\,\mathbb E\tau\right),\qquad
\mathbb E\tau=\frac1{u(1-S)}\sum_{\ell=0}^{n-1}e^{s\ell}.
$$
The first term bounds reaching weakest $D$ before the first visit to its deepest state by gambler's ruin. From deepest $D$ each date has switching probability at most $Ce^{-tn}$ up to its first switch by reflection and a union bound. Condition on the independent $\tau$ to obtain the second term. The formula for $\mathbb E\tau$ follows by reflecting a single $C$ walk, marking successful switching losses at its weak end, and taking the reciprocal of their stationary flux. Each mark restarts the reflected walk at that same weak end.

Sum the last bound against $F(j)$. Since $t>p$, $\sum_{j=0}^N e^{-pj} e^{-t(n-j)}=O(e^{-pn})$. Direct double marks during later returns to $DD$ contribute at most $F A H_{\rm double}=O(e^{-2pn})$. Thus the probability of reaching $CC$ before the first return to $o$ is bounded by
$$
C\left(e^{-2pn}+e^{-(p+t)n}\sum_{\ell=0}^{n-1}e^{s\ell}\right).
$$
For $S=1/2$ the sum is $n$ and $t>p$, so the whole bound is still $O(e^{-2pn})$.

Reversing paths in the killed $DD$ rectangle as above always gives the lower bound $c e^{-2pn}$ for reaching the $CC$ core before returning to $o$. For $S>1/2$ there is also a lower bound $c e^{-(p+t-s)n}$. First reverse the path to $(N,0)$ in the $DD$ rectangle. A switching loss of that agent and a win for its partner, followed by joint reinforcement, reach a mixed core before returning to $o$ with probability at least $c e^{-pn}$. At that core use independent clocks for departures from the mixed profile. Over $L=\lfloor c_0e^{sn}\rfloor$ dates the cooperator stays with probability at least $1/2$, by the geometric-tail union bound from its greatest depth with $c_0$ small. The deep defector switches by date $L$ with probability at least $c L e^{-tn}$.

For the latter estimate, use successive excursions of a single reflected $T$ coordinate from its deep end. The probability of reaching the weak end and marking a switching loss on its first visit is $\Theta(e^{-tn})$ by gambler's ruin. Each failed excursion has uniformly bounded conditional mean length, since the unconditional mean is the reciprocal of the stationary deep mass and success is rare. A successful excursion has conditional mean $O(n)$. The walk conditioned to reach the weak end before revisiting the deep end has outward-step probability at least $T$, by the elementary gambler's-ruin harmonic function; the trip back after a mark has inward drift $2T-1>0$. In the first $\lfloor c_1 L\rfloor$ excursions a success has probability at least $c_2 L e^{-tn}$ since $L e^{-tn}\to0$. Conditional on a specified first successful excursion among these, its finish time has mean at most $C c_1L+O(n)$, hence is at most $L$ with probability at least $1/2$ for small fixed $c_1$. An earlier uncounted switching loss can only advance the first switch. After the mixed defector flips while the cooperator stays, $CC$ reinforcement reaches its core with a uniform positive probability.

In reverse, a switch out of the $CC$ core before its next return has probability $O(e^{-rn})$ by frozen rectangle occupation. The reversed surviving path to $(N,0)$ in $CC$ attains order $e^{-rn}$ for a lone switch. If $S\le1/2$, the mixed profile then reaches the $DD$ core with uniformly positive probability as above. If $S>1/2$, it first reinforces to the mixed core with uniformly positive probability. There the cooperator flips before the defector with probability tending to one because $s<t$. For example, take horizon $e^{(s+\delta)n}$ with $0<\delta<t-s$. The cooperator's mean switch time from deepest $C$ is $O(e^{sn})$ by the same excursion calculation, and the defector's probability of switching by the horizon is $O(e^{-(t-s-\delta)n})$. Fixed-profile reinforcement then reaches the $DD$ core with uniformly positive probability.

Take the trace solely on the two homogeneous deepest cores. Their transition probabilities before the respective first return are $\Theta(e^{-bn})$ from $DD$ and $\Theta(e^{-rn})$ from $CC$. Stationary odds on these cores are their ratio. The prescribed-time reinforcement bound transfers the result to action odds and proves $\pi_R/\pi_P=\Theta(e^{n(r-b)})$ for every $0<S<P$ in the stated dilemma.

## Passage and total-variation mixing in the strict Prisoner's Dilemma

Assume $T>R>P>S$ and $P>1/2$ with independent outcomes as above. From one homogeneous deepest core to the other, the directional mean passage exponents are

$$
\lim_{n\to\infty} n^{-1}\log \mathbb E_{P_{\rm core}}\tau_{R_{\rm core}}=b,\qquad
\lim_{n\to\infty} n^{-1}\log \mathbb E_{R_{\rm core}}\tau_{P_{\rm core}}=r .
$$

They also hold for first entrance into the corresponding homogeneous action profile. For fixed $0<\varepsilon<1$ and $r\ne 2p$, the worst-case discrete-time total-variation mixing time satisfies

$$
\lim_{n\to\infty}n^{-1}\log t_{\rm mix}(\varepsilon)=\min(r,b).
$$

This is a worst-case result. It allows the minority phase to have a short stationary lifetime compared with the mean wait for a return visit from the majority phase.

**Passage.** For $S\le1/2$ the two-core trace gives geometric passage times in trace steps. A physical trace step takes at least one date and has mean at most $O(n^2)$ uniformly, so its time change preserves the exponent. For $S>1/2$ write $a=K_{PM}$, $d=K_{MP}$, $f=K_{PR}$ and $g=K_{MR}$. With $R$ absorbing in the trace, the two first-step equations give

$$
\mathbb E_P N_R=\frac{a+d+g}{f(d+g)+ag},\qquad
\mathbb E_M N_R=\frac{a+f+d}{f(d+g)+ag},
$$

where $N_R$ counts trace steps. The numerator in both has cost $s$ since $s<p$ and $\operatorname{cost}(g)\ge\min(t,s+p)>s$. The denominator is exactly the tree weight of $R$, of cost $W_R$. Thus both passage exponents are $W_R-s=b$. For target $P$, the interchanged equations give denominator of cost $W_P=r+s$ and the numerator for a start at $R$ has cost $s$. The numerator for a start at $M$ has cost at least $s$, so this mean is bounded by $\exp(nr+o(n))$. The uniform $O(n)$ bound on conditional expected excursion duration at the start of a trace step transfers all these bounds to physical time by summing over trace steps. A start outside the cores first hits one in polynomial mean time.

The probability of hitting the $R$ core from the $P$ core before the latter's first return (which may occur at time one) is

$$
h_n=f+\frac{ag}{d+g}=\exp(-nb+o(n)).
$$

In the two-core case it is simply the one-step trace probability. Conditional on the first $CC$ action profile, the probability of reaching the $R$ core while continuously playing $CC$ is at least a fixed $c>0$. Thus the probability of hitting the $CC$ profile before the first return to the $P$ core is between $h_n$ and $h_n/c$. In $L$ physical dates there are at most $L+1$ potential starting visits to the $P$ core. By the Markov property and union bound,

$$
\mathbb P_{P_{\rm core}}(\tau_{CC}\le L)\le (L+1)e^{-nb+o(n)}.
$$

This gives the mean lower bound for first profile entrance, and the core result gives the upper bound. In the reverse direction, leaving $CC$ at all by $L$ from the $R$ core has probability at most $C(L+1)e^{-nr}$, by the fixed-profile reflected marginal walks. The reverse core result again supplies the upper bound.

**Mixing.** Let $H_0=\min(r,b)$ and $H_1=\max(r,b)$. The winning profile has stationary mass tending to one. Before $\exp(n(H_0-\delta))$ the other homogeneous core has vanishing probability of ever reaching it, by the two bounds above. This gives the lower bound for every fixed $\varepsilon<1$.

For the upper bound take any fixed $0<\delta<H_1-H_0$ and $L_n=\lceil\exp(n(H_0+\delta))\rceil$. From all starting states the expected time to the winning core is at most $\exp(nH_0+o(n))$, by the core passage bounds and the polynomial initial approach. With probability tending uniformly to one it is reached before $L_n/2$. Starting there, we show that the probability of being back at this same core at any deterministic time in $[L_n/2,L_n]$ is at least a constant independent of $n$.

If $CC$ wins, the chance of any action change from its core by $L_n$ is $o(1)$ because $H_1=r$. At a fixed date the deficits under the frozen $CC$ dynamics are each dominated by a geometric variable with ratio $e^{-r}$. Choose a fixed $k$ large enough to put both deficits within $k$ with probability at least $3/4$, then require $k$ final joint wins.

If $DD$ wins, the chance of reaching $CC$ by $L_n$ from its core is $o(1)$ because $H_1=b$. Prior to that hit the two upper comparison chains of the preceding section still apply, now also for $S>1/2$. For each, at any fixed date the probability of being outside the lowest $k+1$ positions is at most

$$
C e^{-pk} + C n e^{-n(p-\max(s,0))}.
$$

Indeed, positions on the $D$ side have geometric stationary upper tail, and on the $C$ side the displayed detailed-balance sum gives the second term; $p>\max(s,0)$ in this dilemma. Choose a fixed large $k$, then require $k$ final joint $DD$ wins. This proves the claimed positive return probability uniformly in the prescribed time.

Apply the Markov property at the first winning-core visit. Every row of the $L_n$-step transition matrix puts at least a common constant $\eta>0$ on that core. Coupling on this common atom bounds the $jL_n$-step total-variation distance by $(1-\eta)^j$. A fixed number of blocks suffices for each $\varepsilon>0$. Sending $\delta$ to zero proves the exponent.

### Critical mixing

On $r=2p$ in the strict independent dilemma, both core masses are bounded below by fixed positive constants, $b=r$, and for each fixed $0<\varepsilon<1/2$ one has
$$
t_{\rm mix}(\varepsilon)=\Theta(e^{rn}).
$$
The tolerance restriction matters when two phases carry comparable stationary mass.

For the lower bound start at the less occupied homogeneous phase's core. From deepest $CC$ the chance of any change by $L$ dates is at most $C(L+1)e^{-rn}$. From deepest $DD$ the bounded-factor excursion result gives the same upper bound for any visit to $CC$. The more occupied homogeneous phase has stationary mass at least $(1-\pi_M)/2=1/2-o(1)$. Taking $L=\lfloor c e^{rn}\rfloor$ for a sufficiently small constant gives total-variation distance greater than $\varepsilon$.

For the upper bound fix a small $c>0$ and put $T_n=\lfloor c e^{rn}\rfloor$. From deepest $DD$ the chance of reaching $CC$ by $T_n$ is at most $C(T_n+1)e^{-rn}<1/4$ for $c$ sufficiently small. The geometric coordinate comparison and a fixed number of final joint wins, as in the strict-phase proof, therefore give a uniform positive probability of being at deepest $DD$ at every prescribed time in $[T_n/2,T_n]$.

It remains to reach this core by $T_n/2$ with uniformly positive probability from every start, including deepest $CC$. Starting at deepest $CC$, consider successive full return cycles to this singleton. They are independent with mean duration $1/\pi_{R,\mathrm{core}}\le C_1$ by the bounded-factor coexistence and fixed-time reinforcement. Call a cycle good if it reaches the $DD$ core within $d_n=o(e^{rn})$ before returning. Its probability is at least $c_1e^{-rn}$. Indeed, in the killed $CC$ rectangle the reverse path used to reach $(N,0)$ can be restricted to $Cn$ dates with uniformly positive reverse probability. Then a single switch enters a mixed profile. If $S\le1/2$, the route to the $DD$ core can be restricted to $O(n^2)$ additional dates at positive probability. If $S>1/2$, first reinforce to the mixed core in $O(n)$ dates, then use $e^{(s+\delta)n}$ further dates with $0<\delta<\min(r,t)-s$, as in the preceding departure construction. The $DD$ reinforcement that follows takes $O(n)$ dates.

A good cycle also has probability at most $C_2e^{-rn}$ by the first-switch bound before return to the $CC$ core. Conditional on failure, a cycle thus has uniformly bounded mean duration. In the first $\lfloor c_3 T_n\rfloor$ cycles the probability of at least one good cycle is bounded below uniformly in $n$. Conditional on which of these is the first good cycle, the mean time before reaching the $DD$ core is at most $C_4c_3T_n+d_n$. Choose $c_3$ small to make the probability of completing this visit by $T_n/4$ bounded below. From other initial configurations, fixed-profile reinforcement reaches their own core in $O(n)$ dates with uniformly positive probability when all entries reinforce. A mixed core then has a positive-probability route to deepest $DD$ within $o(T_n)$ since $s<t$. For $S\le1/2$, a mixed starting configuration instead reaches deepest $DD$ in $O(n^2)$ dates with uniformly positive probability. These estimates establish the required uniform visit to the $DD$ core by $T_n/2$. Combining it with the prescribed-time return gives a common atom in every row of the $T_n$-step transition matrix. A fixed number of blocks yields the stated upper bound.

## Independent finite-depth checks

The standard-library script uses nonnegative Grassmann–Taksar–Heyman elimination on unordered coordinate pairs and the original simultaneous transitions. The individual coordinate runs continuously from deepest cooperation to deepest defection. This ordering differs from the separate action/depth encoding in the original probes. The program computes a componentwise invariant-measure residual and, on request, verifies the depth-two result against exact rational elimination.

At 65 decimal digits the following slopes use $n=16$ and $24$. Each entry gives the increment in $\log(\pi_R/\pi_P)$ divided by eight. At all sampled depths and cases the largest componentwise relative residual was $4.0\cdot10^{-64}$. These slopes are finite-difference checks.

| Game | $(R,P,S,T)$ | $L$ slope | $B$ slope | Limit |
|---|---|---:|---:|---:|
| Prisoner's Dilemma, $S<1/2$ | $(.80,.70,.20,.90)$ | $-.308657055$ | $-.308616368$ | $-.308301360$ |
| Prisoner's Dilemma, sequential escape | $(.76,.70,.69,.77)$ | $-.102862746$ | $-.102849660$ | $-.102810256$ |
| Stag Hunt, sequential selection | $(.78,.70,.67,.72)$ | $+.182085848$ | $+.182087896$ | $+.182091962$ |
| Chicken, eventual $CC$ | $(.72,.55,.66,.82)$ | $+.508389556$ | $+.511794624$ | $+.543120218$ |
| Chicken, eventual mixed pair | $(.74,.60,.70,.82)$ | $+.179981683$ | $+.181695523$ | $+.235038339$ |

At depth 24 the Stag Hunt has $\pi_R=0.9853906773$ for $L$ and $0.9853906744$ for $B$, even though the simultaneous-only criterion gives $r<2p$. In both Chicken games $\pi_R/\pi_P$ grows exponentially, yet the limits of $\pi_R$ are opposite.

At 75 decimal digits the slopes from depths 24 to 40 were $-.308328047$ and $-.308325186$ for the original Prisoner's Dilemma ($L,B$ respectively), $-.102811094$ and $-.102810886$ for its sequential-escape variant, and $+.182091919$ and $+.182091931$ for the Stag Hunt. The latter gave $\pi_R=0.9992510286$ under either tactic at depth 40. The largest componentwise relative residual in this run was $6.4\cdot10^{-74}$.

At a critical payoff pair $(R,P)=(.90,.75)$ with $T=.94$, the checked depth-40 values of $\pi_R$ were $0.0915635092$ ($L$) and $0.0708335645$ ($B$) at $S=.50$, and $0.0969731984$ ($L$) and $0.0734869463$ ($B$) at $S=.70$. The maximum 75-digit residual in this critical run was $7.0\cdot10^{-74}$. These are finite-depth values; the theorem gives uniform coexistence without specifying its limiting mixture.

The optional passage calculation replaces the target core's outgoing law by a certain move to the source core. A return cycle to the target then lasts $1+\mathbb E_{\rm source}\tau_{\rm target}$ dates, so its stationary target mass gives the full-chain mean without a subtraction from one. The depth-one passage solver also agrees with exact rational first-step equations. For the original $L$ dilemma at $n=40$, the directional means were $5.182228982\cdot10^{30}$ dates from $DD$ to $CC$ and $1.469180684\cdot10^{24}$ in reverse. The depth-24-to-40 slopes were $1.694622408$ and $1.386294361$, against limits $1.694595721$ and $1.386294361$. For the sequential-escape $L$ dilemma, the corresponding slopes were $1.240419708$ and $1.152623830$, against $1.255489766$ and $1.152679510$. At $n=40$ the mixed probability in that example was still $0.2385880349$.

Reproduce the table and the deeper checks from the study directory.

~~~sh
python3 experiments/phase1_social_game.py --cases pd-short pd-cascade stag-cascade chicken-cooperation chicken-mixed --n 2 8 16 24 --exact-check
python3 experiments/phase1_social_game.py --n 24 40 --cases pd-short pd-cascade stag-cascade --digits 75
python3 experiments/phase1_social_game.py --cases pd-critical-neutral pd-critical-positive --n 8 16 24 40 --digits 75 --exact-check
python3 experiments/phase1_social_game.py --cases pd-short pd-cascade --tactics L --n 16 24 40 --digits 75 --exact-check --passage
~~~
