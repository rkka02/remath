# Who gains from a longer memory?

All payoffs below are win probabilities. An ordinary linear Tsetlin tactic has depths $0,\ldots,m-1$ for each action. A reward deepens the current action by one, with reflection at the cap. A penalty decreases depth, and a penalty at zero switches actions at depth zero. The results in this note concern this tactic. All probabilities are stationary probabilities at the indicated finite memories before a memory limit is taken.

## The omitted eleventh memory state

Use independent feedback and the strict Prisoner's Dilemma $(R,P,T,S)=(.8,.6,.9,.2)$. The preliminary grid skipped the integer immediately to the right of equality. The stationary solution gives the following probabilities and player 1 payoffs.

| Player 1 memory | Player 2 memory | Mutual cooperation | Mutual defection | Player 1 win probability |
|---:|---:|---:|---:|---:|
| 9 | 10 | .615263131134 | .379258008603 | .722378566153 |
| 10 | 10 | .720608517332 | .276208843970 | .743962571531 |
| 11 | 10 | .731673697007 | .265772327122 | .746391275680 |
| 12 | 10 | .677011848789 | .320313395716 | .735637981029 |
| 24 | 10 | .015771496651 | .978454927221 | .604873609708 |
| 34 | 10 | .000267550534 | .993885597383 | .601807347883 |
| $m\to\infty$ | 10 | 0 | $216064/217335$ | $435941/724450$ |

The last row follows from the theorem below. Its payoff is approximately .601754434399. Across all 31 integers from 4 through 34, the 75-digit calculation peaks at 11 for both measures. Exact rational bounds certify both gains from ten to eleven. A sufficiently large upgrade destroys mutual cooperation. A fixed-opponent experiment supplies no fixed-ratio phase boundary.

## One growing player against a finite population

Fix every opponent's memory. Let $e$ encode their joint internal state. Assume the joint feedback law depends on actions and that the tagged player's reward and penalty each have probability at least $\varepsilon>0$ in every state. With the tagged action held at $a\in\{C,D\}$, assume the opponent chain on the state space under consideration is finite and irreducible. Write its transition matrix as $P_a$, its invariant law as $\nu_a$, and the tagged win probability in phase $e$ as $p_a(e)$. The frozen payoff and mean depth increment are

$$
 w_a=\nu_a p_a,\qquad u_a=2w_a-1.
$$

The tagged reward and the simultaneous transitions of the opponents may be correlated. For any stationary law of the full finite system the following conclusions hold as the tagged memory $m$ grows.

1. If $u_D>0>u_C$, the fraction of time in $D$ tends to one, the opponent state law tends to $\nu_D$, and the tagged payoff tends to $w_D$. The action labels can be exchanged.
2. If at least one frozen drift is positive, the stationary action-switch rate tends to zero. Every subsequential limit of the joint law on $(a,e)$ has the form $t\,\delta_C\nu_C+(1-t)\,\delta_D\nu_D$.
3. If both frozen drifts are negative, the tagged player's limiting upper payoff is at most $1/2$.

**Proof.** Each visit to action $a$ starts at depth zero. Extend its terminal step to depth $-1$ when the next action begins. Under frozen dynamics solve the finite Poisson equation $(I-P_a)g=2p_a-1-u_a$. In the uncapped walk, depth plus $g(e)$ has conditional drift $u_a$. With a negative drift, stopping at the first exit or at time $t$ and using the lower bound $-1+\min g$ gives mean exit time at most $(1+\max g-\min g)/|u_a|$, uniformly over starting phases. A capped walk driven by the same frozen outcomes stays below the uncapped one up to exit. Its sojourn has the same uniform upper bound.

For $u_a>0$, the uncapped partial sums divided by time converge almost surely to $u_a$, by the finite-state ergodic theorem and the bounded martingale difference law. Their all-time infimum is finite almost surely. Consequently, from height $H$ the chance of never falling to $-1$ exceeds $1/2$ for sufficiently large fixed $H$, uniformly in the finitely many starting phases. The first $H$ steps may all be wins, with probability at least $\varepsilon^H$. Thus a visit reaches the cap with probability at least $\varepsilon^H/2$ for every $m>H+1$. It then takes at least $m$ steps to switch. Mean visit length grows at least linearly in $m$.

Entries into the two actions alternate. In stationarity their equal individual entry rates multiplied by the respective mean visit lengths, averaged over entry phases, give the action masses. The preceding uniform bounds imply the first assertion about action masses, and the switch-rate assertion. For the stationary subprobability vector $\eta_a(e)=\Pr(a,e)$, the discrepancy $\|\eta_aP_a-\eta_a\|_1$ is at most the total switch rate. Every limit of $\eta_a$ is therefore an invariant subprobability vector of $P_a$, which proves the conclusions about phases and payoffs.

With two negative drifts, let $\tau_\infty$ be the uncapped exit time in one visit. The expected number of visits to the cap in that sojourn is bounded by $\mathbb E[\tau_\infty\mathbf 1_{\{\tau_\infty\ge m-1\}}]$, which tends to zero uniformly over starting phases. The stationary cap probability also tends to zero, since the sojourn entry rate is at most one. In stationarity the exact depth balance of the tagged player is

$$
 2W_1-1=\mathbb E[p_a(e)\mathbf 1_{\{d=m-1\}}]
       -\mathbb E[(1-p_a(e))\mathbf 1_{\{d=0\}}].
$$

This proves the upper bound. All constants here may depend on the fixed opponents. In particular the proof does not take a simultaneous fixed-ratio limit.

### When both actions have positive drift

There is also an exponential selection rule at fixed opponent memories. Let $B_a^+(e,e')$ and $B_a^-(e,e')$ give the joint probability of the indicated tagged increment and opponent transition under the frozen action, so $P_a=B_a^++B_a^-$. For $u_a>0$ there is a unique positive root

$$
 \rho(e^{-\theta_a}B_a^++e^{\theta_a}B_a^-)=1.
$$

The expected duration of an $a$-visit starting at depth zero is bounded above and below by positive constants times $e^{\theta_a m}$, uniformly in the entering opponent phase. Thus, when both frozen drifts are positive and the roots differ, the larger root selects the tagged action with probability tending to one. The corresponding payoff is its frozen mean. Equal roots need a finer comparison.

Indeed, the logarithm of the Perron root is convex by Hölder's inequality applied to the finite-time moment transforms, followed by the limit of their normalized logarithms. It is zero at the origin with derivative $-u_a$, and tends to infinity since every row has loss probability at least $\varepsilon$. These facts give the unique positive crossing. With positive Perron right vector $v$, $e^{-\theta_a d}v(e)$ is a martingale on interior depths. At deep cap $b=m-1$, consider an attempt ending at the next visit to $b$ or at switching depth $-1$. The martingale from $b-1$ bounds the chance of a switch in this attempt by $C e^{-\theta_a m}$. For the reverse bound first demand $H$ consecutive losses, with $e^{\theta_a H}\min v>\max v$. At stopping from $b-H$, the cap contribution to the martingale expectation is at most $e^{-\theta_a b}\max v$, and the exit contribution at most $e^{\theta_a}\max v$ times the exit probability. This yields an exit probability at least $c e^{-\theta_a m}$, including the fixed initial losses. Conditional mean attempt duration is uniformly bounded *when conditioning on the starting phase*: the positive-drift Poisson identity from $b-1$ up to either endpoint gives $\mathbb E\tau\le(1+\operatorname{osc}g)/u_a$. A cap visit therefore requires order $e^{\theta_a m}$ expected steps to exit by summing over successive attempts. From zero the cap is reached with probability bounded below as proved above, and the time to reach either endpoint has expectation $O(m)$ by the same drift identity. The alternating-visit argument proves the selection rule.

For a depth-one opponent with independent outcomes and $(R,P,T,S)=(.70,.60,.80,.55)$, exact rational determinants bracket $e^{\theta_C}$ in $(1.5340660,1.5340661)$ and $e^{\theta_D}$ in $(2.2361037,2.2361038)$. The long-memory player therefore defects with limiting payoff $59/85$. The determinant check uses the two opponent actions as the two phases.

### Evaluating the frozen law against one opponent

For an opponent whose win probabilities for its two actions are $x,y$, birth–death balance gives

$$
 H_n(x)=\frac1{1-x}\sum_{j=0}^{n-1}\left(\frac{x}{1-x}\right)^j,
 \qquad F_n(x,y)=\frac{H_n(x)}{H_n(x)+H_n(y)}.
$$

Here $F_n$ is the opponent's probability of cooperation. The factors $1/(1-x)$ and $1/(1-y)$ come from equality of the action-switch fluxes at depth zero. If $x,y<1/2$, then

$$
 F_\infty(x,y)=\frac{1-2y}{2(1-x-y)}.
$$

If the larger of $x,y$ is strictly above $1/2$ and exceeds the other one, $F_n$ concentrates on the better action. A tie gives exactly $1/2$ for every $n$. For a symmetric game the tagged player's two frozen payoffs are

$$
 w_C=S+(R-S)F_n(R,T),\qquad w_D=P+(T-P)F_n(S,P).
$$

For the original ten-state opponent, $F_{10}(R,T)=1271/3171075$ and $F_{10}(S,P)=1271/217335$. Thus $w_C<1/2<w_D$, giving the last row of the table. For a single fixed opponent these frozen means use only the marginal feedback probabilities. Consequently the same limiting payoff and action law hold for every admissible within-round outcome correlation at every profile, including correlations that change the finite-depth stationary law.

## Opposite incentives in two games

At each homogeneous action profile give the two players the same Bernoulli outcome, i.e. $\kappa_R=\kappa_P=1$. At a mixed profile use independent outcomes with the specified marginals. For equal depths the two players synchronize on a single closed class. From any state a finite sequence rewarding every current cooperator and penalizing every current defector leads to the deepest all-cooperate state with positive probability. From synchronized states identical outcomes preserve identical full states. It follows exactly that $\Pr(CC)=F_n(R,P)$ and $W_1=P+(R-P)F_n(R,P)$.

**A cooperative Prisoner's Dilemma with profitable upgrades.** Take $(R,P,T,S)=(.55,.40,.99,.39)$. Equal depths give $\Pr(CC)\to1$ and $W_1(n,n)\to 11/20$. Against a fixed opponent of depth $n$, the two frozen payoffs tend, as $n\to\infty$, to $.39$ and $.40+.59(10/21)=143/210$. The strict signs persist for all sufficiently large $n$. Therefore

$$
 \lim_{n\to\infty}\lim_{m\to\infty} W_1(m,n)=143/210>11/20.
$$

Every sufficiently large equal-depth profile admits a strictly profitable unilateral upgrade and so fails the Nash condition for unrestricted memory choices. In the iterated limit the upgrader defects and the probability of mutual cooperation vanishes. A deviation by a single unit already has certified payoffs $.5499755023<W_1(40,40)<.5499755025$ and $.6704057221<W_1(41,40)<.6704057224$. The corresponding mutual-cooperation probabilities are approximately .9998366820 and .0000180153. The finite adjacent certificate and the all-large global Nash statement use different arguments. They leave open eventual adjacent optimality for this fixed game.

**An upgrade can lose in Chicken.** Take $(R,P,T,S)=(.70,.20,.71,.23)$, with the same feedback convention. Equality gives $W_1(n,n)\to .70$. The two frozen payoffs tend to $.23$ and $.20+.51(10/19)=89/190<.5$. Thus for every sufficiently large $n$, $\limsup_{m\to\infty} W_1(m,n)\le .5$. An unrestricted upgrade can lose strictly despite the Chicken payoff ordering. There is also a certified adjacent loss at opponent memory ten, from .6999303147 to .6979957709. These statements use the admissible endpoint correlation. For fixed finite memories the strict comparisons also persist under sufficiently small perturbations of the feedback law, by continuity at a matrix with one closed class.

## An adjacent deviation at arbitrarily large equal memories

**Theorem.** In the strict Prisoner's Dilemma $(R,P,T,S)=(.52,.45,.999,.44)$, with common shocks at homogeneous profiles and independent mixed shocks, at least one of $(n,n)$ and $(n+1,n+1)$ admits a profitable one-unit deviation for **every $n\ge40$**. Equal memories select mutual cooperation as $n\to\infty$. The direction of the profitable deviation can be either an upgrade from $n$ or a downgrade from $n+1$ in this argument.

Write $M=\{CD,DC\}$. We will show at depths $(n+1,n)$ that

$$
 W_1+W_2-2R=(T+S-2R)\pi_M-2(R-P)\pi_{DD}>.0449\,\pi_M>0.
$$

At either equal pair the individual payoff is strictly below $R$, since the synchronized chain assigns positive mass to $DD$. At least one of the two payoffs at the unequal pair exceeds $R$. By exchange symmetry the player receiving it makes a profitable one-unit deviation from the equal pair with the same opponent memory.

**Bounding homogeneous blocks.** A homogeneous block is a maximal interval without a mixed profile. Whenever a $DD$ run starts, the smaller defection depth is zero. Until at least one player cooperates, this minimum moves down on a shared penalty and increases by at most one on a shared reward. Its terminal value is $-1$ when the first cooperator appears. The mean duration from minimum zero is at most $g=1/(1-2P)$, by stopping the drift inequality. Let

$$
 c=1-(1-R)/R,\qquad A_n=((1-R)/R)^n,\qquad B_n=(P/(1-P))^{n-1}.
$$

If both depths coincide, the common walk remains synchronized until a win at their shared depth $n-1$ separates the deeper-cap player. From equal cooperative depth zero, gambler's ruin gives probability at least $c$ of separation at that cap before any $DD$. Once the cap separates the players, the longer player is one level deeper. Under subsequent common steps it retains that lead until the first mixed profile. Every direct $DD\to CC$ jump starts at equal cooperative depth zero. Thus the expected total number of $DD$ dates in a homogeneous block starting from equal depths zero is at most $g/c$, by summing the successive $DD$ runs.

For *distinct* initial depths, a common walk can bring them together only at the short cap. Starting in $CC$, simultaneous defection then requires hitting the switching edge before a further win at that cap separates them. From the common cap the gambler's-ruin probability of that event is at most $A_n$. Starting instead in $DD$ with smaller depth zero, the probability of reaching that cap before the first switch is at most $B_n$, again by gambler's ruin. The first $DD$ run has mean at most $g$. Over a homogeneous block entered from mixed play with *distinct* depths, the expected number of $DD$ dates is therefore at most $gH_n$, where $H_n=\max(1+B_n/c,A_n/c)$. An entry from mixed play into equal depths must place both players at depth zero. This requires both mixed-profile signals to be losses. Its stationary rate is at most $(1-S)(1-T)\pi_M$. Every other entry from mixed play has exactly one newly switched player at depth zero.

**Bounding mixed blocks.** Let $v_j$ be the survival probability through $j$ steps of the uncapped walk starting at cooperative depth zero, with reward probability $S$ and killing at $-1$. For $n\ge K=15$, a cooperator beginning at any depth in a mixed profile has survival probability at least $v_j$ through $j<K$ frozen-profile steps. Requiring that the original defector has not suffered a loss costs at most $j(1-T)$ by a union bound. Thus a new mixed block has expected duration at least $L=\sum_{j=0}^{K-1}(v_j-j(1-T))$. The stationary entry rate of homogeneous blocks equals that of mixed blocks and is at most $\pi_M/L$. The preceding occupation bounds yield

$$
 \frac{\pi_{DD}}{\pi_M}\ \le\ g\left(\frac{H_n}{L}+\frac{(1-S)(1-T)}{c}\right).
$$

The unequal-memory recurrent class spends positive time in mixed play, since $n$ successive losses from the deepest all-cooperate state switch only the shorter player. Both terms in $H_n$ are nonincreasing in $n$. The script evaluates $v_j$ by exact rational birth–death recursion and checks $L>4.092$. At $n=40$, substitution in the payoff identity gives a lower bound greater than $.0449$ after division by $\pi_M$. It therefore holds at every larger $n$ as claimed.

## A public-goods threshold for one growing player

For $N\ge3$, consider the symmetric linear public good

$$
 p_i=b+ h\frac{k_{-i}}{N-1}+d\,\mathbf 1_{\{i\text{ defects}\}},
 \qquad 0<d<h,
$$

where $k_{-i}$ counts cooperating opponents. Defection privately gains $d$, while a contribution raises the sum of other players' win probabilities by $h$. All-cooperate gives $R=b+h$, all-defect gives $P=b+d$, and the largest individual probability is $T=b+h+d$. At each round draw two independent uniforms, one for each action. Players taking the same action compare its uniform with their identical win probability. Thus rewards are shared within an action group and independent across the two groups. This specifies the full outcome law.

Suppose $0<b<1/2<P$, $R-h/(N-1)>1/2$, and $T<1$. Give one player memory $m$ and the other $N-1$ players memory $n$. In the unique stationary class those $N-1$ players have the same action and depth. Indeed a sequence rewarding cooperators and penalizing defectors leads from any initial state to the deepest all-cooperate state, and equal-memory players then stay synchronized. With $m=n$ the entire population synchronizes, so that $\Pr(\text{all cooperate})=F_n(R,P)\to1$.

Denote by $G_{m,n}$ the stationary probability that all $N-1$ ordinary players cooperate. Set

$$
 d_* = h\frac{N-2}{N-1},\qquad
 g(d) = \begin{cases}1 & d<d_*,\\[2pt]1/2&d=d_*,\\[2pt]0& d>d_* .\end{cases}
$$

**Theorem.** One growing memory produces the sharp limit

$$
 \lim_{n\to\infty}\limsup_{m\to\infty}|G_{m,n}-g(d)|=0.
$$

For $d>d_*$ the stationary probability of *unanimous defection* tends to one in the same order of limits. Below threshold all ordinary players continue to cooperate in that limit. At the threshold the ordinary players remain synchronized, so the value $1/2$ is a frequency of collective cooperation.

**Proof.** Conditional on a frozen tagged action the synchronized group is a single linear automaton. Its cooperation probabilities when the tag is respectively $C,D$ are

$$
 f_C=F_n\big(R,P+h/(N-1)\big),\qquad
 f_D=F_n\big(R-h/(N-1),P\big).
$$

In both comparisons the advantage of cooperation is exactly $d_*-d$. By the assumed win-probability bounds, both fractions tend to one below threshold and to zero above it. At equality both are exactly $1/2$. The frozen tagged payoffs are $w_C=b+(R-b)f_C$ and $w_D=P+(T-P)f_D$. Since $w_D\ge P>1/2$, at every fixed $n$ all limits as $m$ grows assign group cooperation a probability between $f_C$ and $f_D$, by the vanishing switch-rate theorem. Above threshold, eventually $w_C<1/2<w_D$, so the tag defects with probability tending to one, and the limiting probability of unanimous defection at fixed $n$ equals $1-f_D$. This proves both claims.

For example, take $N=3,b=.45,h=.25$. All equal-memory societies cooperate asymptotically for $d=.07,.125,.16$. With one growing memory the other two cooperate respectively with limiting probabilities $1,1/2,0$. The example uses a shared signal within each action group. Independent individual signals require a different frozen-population law. Finite ratios $m/n\to\gamma$ are a further problem.

## Reproduction and historical scope

Run the verification from the study directory.

```sh
python3 experiments/phase1_memory.py --certify
```
 The script uses 75-digit decimal arithmetic for the full chain and rational arithmetic for the frozen laws. Its optional finite payoff certificate computes a trial potential $v$, then evaluates every entry of $r+Pv-v$ as an exact fraction on the recurrent class. Stationarity puts the mean reward between the smallest and largest entries, independent of how the trial potential was obtained.

Krinskii explicitly treats unequal memory volumes and logarithmic ratios in Examples 1 and 2 of §7 for zero-sum automata. This predates any new interpretation of memory choice here. The public-goods result uses feedback shared by an action group, whereas Pittel's Gur model shares a signal across the population and randomizes action choice at the switching boundary. [Krinskii, pp. 52–53](https://www.mathnet.ru/eng/ppi1933) · [Pittel, 1965](https://www.mathnet.ru/eng/ppi752)
