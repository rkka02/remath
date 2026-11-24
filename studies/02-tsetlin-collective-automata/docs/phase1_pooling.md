# Partial common funds in finite-memory automata

A public good requiring one quarter of the population to contribute has limiting optimal fund share $3/5$. Blind agents asymptotically attain the social optimum there, although contributing is strictly dominated. The limiting welfare is $.82$, compared with $.68$ under private rewards and $.67$ under full pooling. A separate volunteer's dilemma gives a half-pooling transition with critical welfare loss of order $(\log N)/\sqrt N$. Both use independent synchronous depth-one automata. An exact two-site placement calculation below gives different interior maximizers for the linear and randomized-boundary automata.

## A public good with a one-quarter quorum

At fraction $x=k/N$ contributing, everyone receives a base success probability $t(x)$. Below $\theta=1/4$ the base is $t_L=.80$, and when $x\ge\theta$ it is $t_H=.97$. Contributors each pay $c=.60$ whether or not the good is supplied. Thus their private success probability is $t(x)-c$ and a free rider's probability is $t(x)$. All individual probabilities are strictly interior for all $N$. The common fund returns $(1-\alpha)p_i+\alpha\bar p$ to each agent. Signals are conditionally independent, and the automata act simultaneously. A loss switches the action with probability $\nu$, equal to $1$ for $L_{2,2}$ and $1/2$ for $B_{2,2}$. The no-refund threshold public good belongs to the participation games of Palfrey and Rosenthal. [Palfrey and Rosenthal (1984)](https://doi.org/10.1016/0047-2727(84)90023-9)

For either architecture, write $W_N(\alpha)$ for the stationary mean success probability. Then

$$
\begin{aligned}
 W_N(0)&\longrightarrow .68,& W_N(2/3)&\longrightarrow .79,& W_N(1)&\longrightarrow .67,\\
 .82-W_N(3/5)&=\Theta(1/\log N),&
 \max_{0\le\alpha\le1}W_N(\alpha)&\longrightarrow .82,&
 \alpha_N^{\rm opt}&\longrightarrow 3/5 .
\end{aligned}
$$

The last limit holds for every choice of a finite-population maximizer. The best individual profile has welfare at most $.82=.97-.60/4$, and reaches it whenever $4$ divides $N$. The limiting gains over private and full pooling are $.14$ and $.15$, respectively.

A nonpivotal contribution changes the individual's pooled payoff by $-c[1-\alpha(1-1/N)]$. A pivotal contribution also supplies $t_H-t_L=.17$. Thus when the required number of contributors is at least two, the all-defector profile is always a strict Nash equilibrium, and exactly-quorum profiles become Nash at

$$
 \alpha_{\rm Nash}(N)=\frac{43N}{60(N-1)}.
$$

If this number exceeds one, the quorum equilibrium is unattainable within the allowable shares. At $3/5$ and $2/3$, even a pivotal contribution is strictly unprofitable. Defection is strictly dominant. The limiting optimal blind fund is below $\lim\alpha_{\rm Nash}=43/60$.

**Proof of the limiting welfare and optimizer.** In a branch with $e=1-t$, a contributor leaves with probability $\nu[e+c(1-\alpha+\alpha x)]$ and a free rider enters with probability $\nu(e+\alpha c x)$. Their independent Bernoulli draws give conditional mean fraction

$$
 F_e(x)=x+\nu b_e(x),\qquad
 b_e(x)=e(1-2x)+cx(2\alpha-1-2\alpha x).
$$

Conditional variance is at most $1/(4N)$ and deviations from $F_e(x)$ have Hoeffding tails. The branches have $e_L=.20$, $e_H=.03$. For each branch $b_e$ has a unique root $x_e\in(0,1/2]$, increasing strictly in $\alpha$. Its sign is positive below and negative above the root. The ratio $h_e(x)=(F_e(x)-x_e)/(x-x_e)$ extends to a nonincreasing affine function. Its endpoint values $1-\nu e/x_e<1$ and $1-\nu(e+c)/(1-x_e)>-1$ give $\sup_{[0,1]}|h_e|<1$. Each branch separately contracts about its root.

The root crosses $\theta$ at

$$
 A_e=\frac{c\theta-e(1-2\theta)}{2c\theta(1-\theta)},\qquad
 A_{e_L}=2/9,\quad A_{e_H}=3/5 .
$$

For $\alpha<2/9$, the low branch maps its entire interval strictly below $\theta$ with a uniform gap. Indeed $F_{e_L}'(x)=1-\nu+1.2\nu\alpha(1-2x)\ge0$ up to $\theta$, and $F_{e_L}(\theta)<\theta$. The high branch has strictly negative drift on $[\theta,1]$. Its mean time to enter the low region is bounded independently of $N$, by stopping its bounded fraction at first entrance and summing its drift. Hoeffding bounds the one-step rate of escape from the low region exponentially in $N$. Hence the stationary mass of the high region is exponentially small. This entrance-and-exit estimate follows, for instance, by bounding total expected outside occupancy during $T$ steps by the initial return time plus the expected length of an excursion following each exit. Divide by $T$ and let $T\to\infty$. Stationary mean-square contraction gives $X\to x_{e_L}$, so at zero pooling $x_{e_L}=1/5$ and welfare tends to $.80-.60/5=.68$.

For $\alpha>3/5$, the productive region is exponentially stable by the same argument. Concavity yields $\inf_{[\theta,1]}F_{e_H}>\theta$ since $F_{e_H}(\theta)>\theta$ and $F_{e_H}(1)=1-.63\nu>\theta$. The low drift is positive on $[0,\theta]$, giving a bounded mean entrance time. Hence $X\to x_{e_H}$ in mean square, and welfare tends to $.97-.60x_{e_H}$. Substitution gives $x_{e_H}(2/3)=3/10$ and $x_{e_H}(1)=1/2$.

As $\alpha\downarrow3/5$ through larger fixed shares, $x_{e_H}\downarrow1/4$. Since every profile has welfare at most $.82$, the limiting maximal stationary welfare is $.82$. Existence of maximizers follows from finite irreducibility and continuity. If $\alpha_N$ maximizes welfare, below-quorum profiles have welfare at most $.80$, so their stationary probability tends to zero. On productive profiles, the gap from $.82$ is $.60(X-\theta)$, hence $X\to\theta$ in probability. For any convergent subsequence of maximizing shares, stationarity of the bounded drift gives $b_{e_H}(\theta)=0$ at its limit. The sole solution is $3/5$.

**The fixed share $3/5$.** Here the high branch fixes $\theta$ with $F_{e_H}(x)-\theta=(x-\theta)h(x)$, where $h(x)=1-.12\nu-.72\nu x$. Write $0<u=\inf h\le \sup h=v<1$ on $[0,1]$. Below $\theta$ the drift is bounded below by $\eta=.085\nu$ from concavity and evaluation at the two endpoints. Take $0<\delta<\eta/4$. On $[\theta-\delta,1]$ the conditional mean next fraction is at least $\theta$, and below that interval mean entrance time is bounded by summing the positive drift. The stationary mass below $\theta-\delta$ is therefore exponentially small. From $[\theta-\delta,\theta)$ the next fraction is at least $\theta+2\delta$ with probability $1-e^{-\Omega(N)}$.

Starting at least $2\delta$ above $\theta$, the next $T=\lfloor(\log N)/(4|\log u|)\rfloor$ times are all productive with probability tending to one, uniformly over the initial state. Indeed, with probability at least $1-2T\exp(-2N^{1/3})$, each step deviates from its conditional mean by at most $N^{-1/3}$. The distance above threshold after $j\le T$ such steps is at least $2\delta u^j-N^{-1/3}/(1-u)>0$. A near-threshold unsuccessful time consequently initiates at least $T$ productive times with probability tending to one. The events “the current time is unsuccessful and the next $T$ times are productive” at times $0,\dots,T$ are disjoint, so stationarity bounds the unsuccessful probability by $O(1/\log N)$, including the exponentially rare lower tail.

For the reverse bound, continue the high kernel on all states and run it for $T'=O(\log N)$ steps from any productive state. Its mean-square distance to $\theta$ is $O(1/N)$, by global contraction and the conditional variance bound. With probability at least $1/2$ it lies within $B/\sqrt N$ of $\theta$ for some fixed $B$. From there the next count is below $\theta N$ with probability bounded below by a positive constant. Indeed it is a sum of $N$ independent Bernoulli variables whose success probabilities stay in a compact subinterval of $(0,1)$, and its mean is within $B\sqrt N$ of $\theta N$. The Berry–Esseen bound gives the assertion uniformly, including the integer rounding of a strict threshold. The continued chain agrees with the original up to its first unsuccessful time. It follows that from any state there is, with probability at least a positive constant, an unsuccessful time in a window of $T'+2$ steps. Summing the stationary probabilities in that window gives the lower bound $\Omega(1/\log N)$.

Finally, on productive states the conditional mean absolute distance contracts with factor $v$ plus an error at most $1/(2\sqrt N)$. Unsuccessful times have uniformly bounded absolute distance. Stationarity gives $\mathbb E|X-\theta|=O(1/\log N)$. Each unsuccessful time costs at least $.02$ relative to $.82$, while productive times cost $.60(X-\theta)$. These estimates give the claimed two-sided loss. $\square$

**Both orderings of the rational and automaton thresholds.** The proof gives an explicit range of parameters for a general quota $0<\theta<1/2$. Suppose $0<c<L<H<1$, $H-c\theta>L$, $\nu(1-H+c)<1-\theta$, and

$$
 A=\frac{c\theta-(1-H)(1-2\theta)}{2c\theta(1-\theta)}\in[0,1).
$$

Here $L,H$ denote the unproductive and productive base probabilities. For every stationary optimizer $\alpha_N\to A$, and $H-c\theta-W_N(A)=\Theta(1/\log N)$. This same $A$ is the only fixed share capable of attaining the optimum in the large-population limit. The proof for $\alpha>A$ uses $F_{1-H}(\theta)>\theta$ and $F_{1-H}(1)>\theta$. At $\alpha=A$, the productive branch fixes $\theta$, with $h(1)=(F_{1-H}(1)-\theta)/(1-\theta)>0$, $h(0)=1-\nu(1-H)/\theta<1$, and $h$ nonincreasing. The low drift is strictly positive on $[0,\theta]$ by concavity, its positivity at zero, and $b_{1-L}(\theta)=(H-L)(1-2\theta)>0$. These are precisely the trapping, contraction and return estimates used above. Welfare convergence forces $X\to\theta$, successful provision with probability tending to one, and hence $b_{1-H}(\theta)=0$ by stationarity. For $0<H-L<c$, the first quorum-Nash threshold tends to $1-(H-L)/c$.

| $\theta$ | $L$ | $H$ | $c$ | Efficient blind share $A$ | First quorum-Nash share, limiting | Optimal welfare |
|---:|---:|---:|---:|---:|---:|---:|
| $1/4$ | $.80$ | $.90$ | $.20$ | $0$ | $1/2$ | $.85$ |
| $1/4$ | $.67$ | $.97$ | $.60$ | $3/5$ | $1/2$ | $.82$ |
| $1/4$ | $.80$ | $.97$ | $.60$ | $3/5$ | $43/60$ | $.82$ |

In the first game, private feedback achieves asymptotically optimal provision while defection is strictly dominant. In the second, a quorum is already a rational equilibrium at a smaller fund share than the blind population needs for asymptotically optimal welfare. With $H=.97,c=.60$ the two thresholds coincide at $L=.73$. This comparison uses a fixed finite memory and growing population, and uses the appearance of an exactly-quorum *pure* Nash profile (efficient for sufficiently large $N$; note at small $N$ such as $N=5$ with $\alpha\ge 43/48$, a two-contributor quorum profile has welfare $.73 < .80$) as its rational benchmark.

**Sharp finite-population correction.** Under the general hypotheses in the preceding paragraph, let $\rho_N(\alpha)=H-c\theta-W_N(\alpha)$. Every maximizing sequence approaches $A$ from above, with a sharp order for both its displacement and its welfare loss.

$$
 \alpha_N^{\rm opt}-A=\Theta\!\left(\sqrt{\frac{\log N}{N}}\right),
 \qquad
 \min_\alpha \rho_N(\alpha)=\Theta\!\left(\sqrt{\frac{\log N}{N}}\right).
$$

The welfare loss at the fixed limit $A$ has the slower decay $\Theta(1/\log N)$. The assertions specify orders, and leave the leading constants open.

**Proof.** Write $\pi_U$ for the stationary probability of falling below the quota. Throughout a sufficiently small neighborhood of $A$, low-branch drift on $[0,\theta]$ is uniformly positive. The productive branch has a root $x_\alpha$ with $|x_\alpha-\theta|\le C|\alpha-A|$ and contracts about it by a factor $v<1$ uniform over this neighborhood. Indeed the root is simple since $b_{1-H}'(x_\alpha)=-(1-H)/x_\alpha-2\alpha c x_\alpha<0$, and the endpoint contraction inequalities persist. For $t=\alpha-A>0$ small, concavity and the strictly positive margin at $1$ give $\inf_{[\theta,1]}F_{1-H}\ge\theta+bt$ for some $b>0$. The one-step probability of missing quota from a productive state is at most $\exp(-2Nb^2t^2)$. Mean return time after a miss is bounded as above. Hence $\pi_U\le C\exp(-2Nb^2t^2)$. In stationarity,

$$
 \mathbb E|X-x_\alpha|\le v\mathbb E|X-x_\alpha|+\frac1{2\sqrt N}+C\pi_U .
$$

It follows that $\rho_N(A+t)\le C[t+N^{-1/2}+\exp(-2Nb^2t^2)]$. Choosing $t=D\sqrt{\log N/N}$ for a large fixed $D$ gives the claimed upper bound for the optimal loss.

For any $\alpha$, put $g=H-c\theta-L>0$. The per-profile deficit on failure is $g+cX\ge g$ and on success it is $c(X-\theta)$. Thus

$$
 \pi_U\le\rho_N/g,\qquad \mathbb E|X-\theta|\le \rho_N/c+\theta\rho_N/g .
$$

Stationarity, the uniform Lipschitz bound on the two branch drifts, and boundedness of their difference imply $|b_{1-H}(\theta)|\le C(\pi_U+\mathbb E|X-\theta|)$. Since $b_{1-H}(\theta)=2c\theta(1-\theta)(\alpha-A)$, this gives $|\alpha-A|\le C\rho_N(\alpha)$.

A quantitative lower bound for missing the quota completes the proof. For any $\alpha$ near $A$, continue the productive branch throughout the state space. From any productive state, in $T=O(\log N)$ steps this chain reaches mean-square distance $O(1/N)$ from $x_\alpha$, uniformly in $\alpha$. With probability at least $1/2$ it is within $B/\sqrt N$ for a fixed $B$. Conditional on that event, the next count has mean $\mu\le N\theta+CN(\alpha-A)_++C\sqrt N$, using monotonicity of $x_\alpha$. It misses quota with probability at least $c_1\exp[-C_1N(\alpha-A)_+^2]$. The elementary lower-tail estimate justifying this bound is proved below. The real chain agrees with the extension until it misses quota. Thus from any starting state there is a miss in the next $T+2$ times (including the initial time) with at least this probability times $1/2$. A union bound in stationarity gives

$$
 \pi_U\ge\frac{c_2}{\log N}\exp[-C_1 N(\alpha-A)_+^2].
$$

Use this bound at a maximizer, which is near $A$ by the preceding theorem. Since $g\pi_U\le\rho_N\le C\sqrt{\log N/N}$, we obtain
$C_1N(\alpha_N^{\rm opt}-A)_+^2\ge\frac12\log N-\frac32\log\log N-O(1)$. Together with $|\alpha_N^{\rm opt}-A|\le C\rho_N$ this gives both sharp orders. $\square$

**Lower-tail estimate.** Let $S$ be a sum of $N$ independent Bernoulli variables with parameters in a common compact subinterval of $(0,1)$, as holds for both roles in the productive extension above. Write $\mu=\mathbb ES$, and suppose $(\mu-N\theta)_+/N$ is sufficiently small. Then
$$
 \Pr(S<N\theta)\ge c_3\exp\!\left[-C_3\frac{(\mu-N\theta)_+^2}{N}\right].
$$
To see this, tilt the law by $\exp(\lambda S-\Lambda(\lambda))$, where $\Lambda(\lambda)=\log\mathbb E e^{\lambda S}$ and $\lambda\le0$ is chosen to put the tilted mean at $m=\min(\mu,N\theta-2\sqrt N)$. For large $N$ this mean is attainable. For $\lambda$ in a fixed finite neighborhood of zero, the tilted Bernoulli variances sum to between $cN$ and $N/4$, uniformly over the original parameters. Continuity and the lower derivative bound on the tilted mean yield $|\lambda|\le C[(\mu-N\theta)_+/N+N^{-1/2}]$ for the stated sufficiently small mean excess. Under the tilted law, $|S-m|\le\sqrt N$ has probability at least $3/4$ by Chebyshev, and throughout this event $S<N\theta$. The likelihood of the original law relative to the tilted law there is at least $\exp[-CN\lambda^2-|\lambda|\sqrt N]$, by Taylor's theorem for $\Lambda(\lambda)-\lambda\Lambda'(\lambda)$. This gives the desired estimate with constants uniform in the productive branch.

For the $(L,H,c)=(.80,.97,.60)$ quorum with $B_{2,2}$, 80-digit stationary calculations directly compare the limiting share with a slightly higher finite-population choice. These are two-share comparisons, and the higher shares in the table need not maximize at their respective population sizes.

| $N$ | $W_N(3/5)$ | Tested higher share | Its welfare |
|---:|---:|---:|---:|
| 64 | .767222470304035828 | $5/8$ | .767716356412821364 |
| 128 | .776057470980060377 | $19/30$ | .777595586652701635 |
| 256 | .783827534038269589 | $19/30$ | .786296684579626776 |
| 512 | .789995806091765006 | $19/30$ | .793358361316504435 |

## 1. One volunteer supplies a public good

Let $N\ge2$ and $0<a<1-c<1$. Without a volunteer every player has win probability $a$. Once at least one agent volunteers, a volunteer has win probability $1-c$ and everyone else succeeds with probability 1. Each additional volunteer pays the same private cost. This is the volunteer's dilemma, expressed in Bernoulli success units. The fund replaces $p_i$ by $(1-\alpha)p_i+\alpha\bar p$, with $0\le\alpha\le1$. All agents draw independent signals conditional on the action profile and update simultaneously. [Diekmann, *Volunteer's Dilemma* (1985)](https://doi.org/10.1177/0022002785029004003)

Take the linear automaton $L_{2,2}$ or the randomized-boundary automaton $B_{2,2}$, with a single state per action. On loss it switches actions with probability $\nu=1$ or $\nu=1/2$, respectively. Write $K$ for the number volunteering and $X=K/N$. For $k>0$, current volunteers leave with probability $\nu c(1-\alpha+\alpha x)$, and current free riders enter with probability $\nu c\alpha x$, where $x=k/N$. Thus

$$
 K' \mid k \ \overset{d}{=}\ \operatorname{Bin}\bigl(k,1-\nu c(1-\alpha+\alpha x)\bigr)
       +\operatorname{Bin}(N-k,\nu c\alpha x) . \tag{1}
$$

The summands are independent. At zero, $K'\sim\operatorname{Bin}(N,b)$ with $b=\nu(1-a)$. Any positive state can reach zero with positive probability, and zero can reach each state in one step. The unique stationary law has mean win probability

$$
 W_N(\alpha)=1-(1-a)\pi_0-c\,\mathbb E X .
$$

The social optimum $1-c/N$ occurs with just one volunteer. Subtracting $c/N$ from the loss below gives regret relative to this attainable optimum, with the same asymptotic orders. The strict pure Nash equilibria at every fund share are exactly the one-volunteer profiles. The sole volunteer strictly prefers supplying the good to losing it. When another volunteer already exists, the payoff change on joining is $-c[1-\alpha(1-1/N)]<0$.

### Three regimes

For each fixed $\alpha$, with constants allowed to depend on $a,c,\nu,\alpha$,

$$
 1-W_N(\alpha)=
 \begin{cases}
 \Theta(1/\log N), & 0\le\alpha<1/2,\\
 \Theta((\log N)/\sqrt N), & \alpha=1/2,\\
 c\bigl(1-\frac{1}{2\alpha}\bigr)+o(1), & 1/2<\alpha\le1 .
 \end{cases} \tag{2}
$$

In the middle regime a regenerative cycle has mean length $\Theta(\sqrt N)$ and accumulates $\Theta(\log N)$ volunteer fraction across its steps. In the upper regime $X$ converges in mean square to $x_*=1-1/(2\alpha)$. Every finite-$N$ maximizer $\alpha_N$ converges to $1/2$. The maximizing share may vary with $N$.

**Proof.** At a positive count the conditional drift is

$$
 \mathbb E[X'-X\mid X=x]=\nu c x[(2\alpha-1)-2\alpha x].
$$

Stationarity gives the exact identity

$$
 (1-a)\pi_0=c[(1-2\alpha)\mathbb E X+2\alpha\mathbb E X^2]. \tag{3}
$$

Let $L$ be the time between two successive visits to zero. The cycles are independent and identically distributed, and $\pi_0=1/\mathbb E L$. Equivalently, $L=1+\tau_0(K_1)$, where $K_1\sim\operatorname{Bin}(N,b)$ and $\tau_0(0)=0$.

**Below half.** Until hitting zero, $\mathbb E[K'\mid k]\le r k$, where $r=1-\nu c(1-2\alpha)<1$. The killed count therefore satisfies $\Pr(\tau_0>t)\le\min(1,Nr^t)$. Summation gives $\mathbb E L=O(\log N)$. At every positive state, each incumbent survives with probability at least $s=1-\nu c>0$. Couple the initial reset group to independent surviving lineages with one-step persistence $s$. As long as one initial lineage survives, the count has not vanished, so survival through its $t$th step has probability at least $1-(1-bs^t)^N$. Summing over $t\le(\log N)/(2|\log s|)$ gives $\mathbb E L=\Omega(\log N)$. Equation (3) gives $c\mathbb E X\le(1-a)\pi_0/(1-2\alpha)$, and outage loss gives the matching lower bound. For $\alpha=0$ the thinning process is exact, yielding

$$
 \mathbb E L=1+\sum_{t\ge0}\left[1-(1-bs^t)^N\right],\qquad
 1-W_N(0)=\frac{2(1-a)}{\mathbb E L}. \tag{4}
$$

In fact $\mathbb E L=(\log N)/|\log s|+O(1)$. Split the series at $\lfloor\log(Nb)/|\log s|\rfloor$. The contribution above the split is bounded by a geometric sum and the missing mass below the split by $\sum_{j\ge0}\exp(-s^{-j})$, up to an index shift.

**At half.** Put $h=\nu c/2$. For $k>0$ write $Y=K'$ and $m=\mathbb E Y=k-\nu c\,k^2/N$, so $(1-\nu c)k\le m\le k$. Each original volunteer survives with probability in $[1-2h,1-h]$. Its contribution bounds $\operatorname{Var}Y$ below by a positive constant times $k$. The variance of all newcomers is at most $hk$. Thus for constants independent of $k,N$,

$$
 v k\le\operatorname{Var}Y\le V k,\qquad
 \mathbb E(Y-m)^4\le3(\operatorname{Var}Y)^2+\operatorname{Var}Y\le C k^2. \tag{5}
$$

The fourth-moment bound follows by expanding a sum of independent centered Bernoulli variables. Choose $D>1$ so large that

$$
 \mathbb E\big[(Y-m)^2\mathbf 1_{\{Y\le Dk\}}\big]\ge vk/2. \tag{6}
$$

Indeed, on the complementary event $Y-m>(D-1)k$, so its contribution to the second moment is at most $C/(D-1)^2$.

Define two increasing concave functions, with continuous value zero at zero,

$$
 F(s)=s\log(1+N/s^2)+2\sqrt N\arctan(s/\sqrt N),\qquad G(s)=\log(1+s/\sqrt N). \tag{7}
$$

Then $F'=\log(1+N/s^2)$, $F''=-2N/[s(N+s^2)]$, and $G''=-1/(s+\sqrt N)^2$. For each $H=F,G$, split the expected decrease into $H(k)-H(m)$ and the Jensen gap $H(m)-\mathbb E H(Y)$.

* For $F$, the first term is at most a constant by $m\ge(1-\nu c)k$, $k-m=\nu c k^2/N$, and $\log(1+u)\le u$. For $k\ge\sqrt N$ it is at least $(k-m)F'(k)=\nu c(k^2/N)\log(1+N/k^2)\ge\nu c\log2$. For the Jensen gap, $-F''(s)\le2/s$ gives a tangent remainder at $m$ of at most $2[y\log(y/m)-y+m]\le2(y-m)^2/m$, with continuous extension at zero. Its expectation is $O(1)$ by (5). If $k\le\sqrt N$, then on the segment between $m$ and any $0\le y\le Dk$, one has $-F''(s)\ge2/[D(1+D^2)k]$ for positive $s$. The lower curvature bound and (6) give a positive lower bound for the Jensen gap. Hence $F(k)-\mathbb E F(Y)\asymp1$ for every $k\ge1$.
* For $G$, the first term is at most $(k-m)/(\sqrt N+m)=O(k/N)$ and is at least a positive constant times $k/N$ when $k\ge\sqrt N$. Since $-G''\le1/N$, (5) bounds the Jensen gap by $O(k/N)$. When $k\le\sqrt N$, $-G''(s)\ge[(1+D)^2 N]^{-1}$ on the segments used in (6), giving the matching lower bound. Hence $G(k)-\mathbb E G(Y)\asymp k/N$ for every $k\ge1$.

Stop at zero and sum the drifts. At each fixed $N$ the functions are bounded and the hitting time is integrable by finite irreducibility. The mean hitting time started at $k$ is comparable to $F(k)$, and the expected cumulative volunteer fraction until hitting zero is comparable to $G(k)$. After a reset $K_1\ge bN/2$ with probability tending to one. On this range $F(k)\asymp\sqrt N$ and $G(k)\asymp\log N$, with the same upper bounds over the entire state space. Mean welfare loss per cycle is $1-a$ plus $c$ times the expected cumulative volunteer fraction. Division by the mean cycle length gives (2) at half.

**Above half.** Let $F_\alpha(x)=x+\nu c x[(2\alpha-1)-2\alpha x]$ for positive $x$. Choose $0<\delta<\min(x_*/2,(1-\nu c)/2)$. On $I=[\delta,1]$, concavity gives $\inf_I F_\alpha>\delta$ by evaluating its endpoints. A conditional Hoeffding bound for (1) bounds the one-step probability of exiting $I$ by $e^{-\eta N}$ for some $\eta>0$. At $1\le k<\delta N$ the count has upward drift at least $\nu c[(2\alpha-1)-2\alpha\delta]>0$. The reset drift at zero equals $Nb$. Stopping on entrance to $I$ and summing the drift gives mean entrance time $O(N)$ uniformly over starting states. Each exit initiates an outside excursion with that bound on its mean duration, so stationary mass outside $I$ is $O(Ne^{-\eta N})$. Formally, bound expected outside occupancy over $T$ steps by the initial entrance time plus the mean duration after each exit in the interval, then divide by $T$.

The identity $F_\alpha(x)-x_*=(x-x_*)(1-2\alpha\nu c x)$ gives $\sup_I|1-2\alpha\nu c x|<1$. Since $\operatorname{Var}(X'\mid x)\le1/(4N)$, the stationary squared distance obeys $\mathbb E(X-x_*)^2=O(N^{-1}+Ne^{-\eta N})$. This gives the upper regime. For all $\alpha\le1/2-\epsilon$ the upper bound on mean cycle length is uniform and the outage loss is at least $C_\epsilon/\log N$. For all $\alpha\ge1/2+\epsilon$ the positive interval, drift and Hoeffding bounds can be chosen uniformly, giving a positive lower bound for loss. Stationary welfare is continuous in $\alpha$ by finite irreducibility, so maxima exist. Comparing these bounds with half pooling gives convergence of every maximizer. $\square$

**Full-support version.** Keep $a,c$ fixed and give volunteers and free riders positive-provision probabilities $1-c-N^{-2}$ and $1-N^{-2}$ for all sufficiently large $N$. Formula (2) and the maximizing-share conclusion persist. Couple the original and perturbed one-step draws with independent common uniforms. Conditional on $k>0$, their counts have expected absolute difference at most $\nu/N$. On integer arguments $F$ is Lipschitz with constant $F(1)=O(\log N)$, and $G$ with constant $O(N^{-1/2})$. The critical drifts change by $O((\log N)/N)=o(1)$ and $O(N^{-3/2})=o(k/N)$, respectively. Below half, the killed count retains a strict multiplicative upper bound since $k\ge1$ and the mean changes by at most $\nu/N$. Each initial volunteer retains a fixed positive persistence bound. Summing the contracting first moment from at most $N$ gives the uniform $O(1)$ upper bound for expected cumulative volunteer fraction per cycle. Above half, the conditional mean fraction changes by $O(N^{-2})$, preserving the entrance and concentration bounds. The per-profile welfare functions differ by at most $N^{-2}$. Fixed free-rider failure probability independent of $N$ is a different asymptotic problem.

**Fixed positive failure probability.** Suppose instead that free riders succeed with a fixed $1-\varepsilon$, volunteers with $1-\varepsilon-c$, and $0<a<1-\varepsilon-c$. Then every sequence of maximizing shares satisfies $\alpha_N\to0$. To see this, let $F(x)$ be the mean next volunteer fraction at positive $x$, extended continuously to zero. It satisfies
$$
 F(x)-x=\nu[\varepsilon(1-2x)+c x(2\alpha-1-2\alpha x)].
$$
The expression in brackets is positive at zero, nonpositive at $1/2$ and negative at one. It has one positive root $x_*(\alpha)\in(0,1/2]$, with $x_*(1)=1/2$. The root increases strictly in $\alpha$, because raising $\alpha$ increases the drift by a positive multiple of $x(1-x)$. Divide $F(x)-x_*$ by $x-x_*$ to obtain a decreasing affine function $h(x)$ (constant when $\alpha=0$). Its endpoint values are $h(0)=1-\nu\varepsilon/x_*<1$ and $h(1)=1-\nu(\varepsilon+c)/(1-x_*)>-1$. Continuity on the compact $\alpha$-interval gives $\sup_{\alpha,x}|h(x)|<1$. The actual zero-state reset has mean $b$. At every starting state every player's chance of volunteering next step is at least $\min(b,\nu\varepsilon,1-\nu(\varepsilon+c))>0$, so $\pi_0$ is exponentially small uniformly in $\alpha$. Conditional variance is again at most $1/(4N)$. Applying stationarity to $(X-x_*)^2$ gives uniformly $\mathbb E(X-x_*)^2=O(N^{-1})$, hence $W_N(\alpha)\to1-\varepsilon-cx_*(\alpha)$ uniformly. This strictly decreasing limiting welfare gives the asserted optimizer. Finite-population optima can differ markedly from their eventual limit, as in the example below.

The critical duration and cumulative-size scales have precedents in logistic epidemics. Dolgoarshinnykh and Lalley proved a diffusion limit for a continuous-time SIS process started with order $\sqrt N$ infectives. Foxall's Theorem 4 covers the continuous-time logistic extinction scale from macroscopic initial states as well. The calculation here uses the discrete synchronous transition and stationary welfare after continual regeneration. Priority for this combination requires a wider literature audit. [Dolgoarshinnykh and Lalley, *Critical Scaling for the Simple SIS Stochastic Epidemic*](https://arxiv.org/abs/math/0512252) · [Foxall, *Extinction Time of the Logistic Process*](https://arxiv.org/abs/1805.08339)

### Exact finite comparisons

Take $N=12$ and fixed probabilities strictly inside the unit interval. Without a volunteer success is $1/20$. A supplied good yields probability $3/20$ to a volunteer and $99/100$ to a free rider. The volunteer cost is $21/25$ and the best attainable profile has mean $0.92$. All entries of the 13-state kernel are rational. Exact Gaussian elimination gives these stationary mean win probabilities, rounded for display.

| Automaton | Private, $\alpha=0$ | Interior | Full, $\alpha=1$ | Interior gain over better endpoint |
|---|---:|---:|---:|---:|
| $B_{2,2}$ | 0.67132632228991455 | 0.75060448080495186 at $1/2$ | 0.61065614730841708 | 0.07927815851503731 |
| $L_{2,2}$ | 0.40512601566438969 | 0.71099147138525727 at $3/4$ | 0.61025999615958966 | 0.10073147522566761 |

The program verifies exact lower bounds $79/1000$ and $1/10$ for these gains and cross-checks each stationary probability against an 80-digit solve. For the asymptotic model with $a=0.1,c=0.75,\nu=1/2$, direct stationary calculations give the following values.

| $N$ | $W_N(0)$ | $W_N(1/2)$ | $W_N(1)$ | Mean critical cycle length |
|---:|---:|---:|---:|---:|
| 8 | .677634494 | .742642607 | .674120538 | 13.223548 |
| 16 | .742638214 | .814260339 | .652469629 | 21.778307 |
| 32 | .786631013 | .862264975 | .637565838 | 34.176848 |
| 64 | .818078316 | .896415255 | .631055148 | 51.950929 |

## 2. Exact interior maximizers in a placement game

Site capacities are $A=1$ and $b=9/10$. Each site shares its capacity equally among its occupants. Success is $(1+u_i)/2$, where $u_i$ is the individual's raw payoff before pooling. Two depth-one automata draw independently. With $k$ players at the rich site, the raw welfare means are $b/2,(A+b)/2,A/2$ in order $k=0,1,2$. The middle profile already has one player per site in the unpooled Nash equilibrium.

Let $d=\nu(1-b/2)/2$ be the switch probability in the all-weak profile, and $e=\nu(1-A/2)/2$ the corresponding probability at the all-rich profile. At a separated profile let $x$ and $y$ be the rich and weak player's switch probabilities. They equal $\nu[1-(1-\alpha)A-\alpha(A+b)/2]/2$ and $\nu[1-(1-\alpha)b-\alpha(A+b)/2]/2$. The transition on occupied counts is

$$
 \begin{pmatrix}
 (1-d)^2 &2d(1-d)&d^2\\
 x(1-y)&1-x(1-y)-y(1-x)&(1-x)y\\
 e^2&2e(1-e)&(1-e)^2
 \end{pmatrix}.
$$

Solving the three stationary equations and averaging the raw welfare gives

$$
 W_L(\alpha)=\frac{20\alpha^2-89\alpha+13180}{2(21\alpha^2-61\alpha+7349)},\qquad
 W_B(\alpha)=\frac{20\alpha^2-169\alpha+30780}{2(21\alpha^2-101\alpha+17029)} .
$$

The respective derivative numerators after multiplication by positive factors are $\alpha^2-400\alpha+231$ and $\alpha^2-400\alpha+151$. Each is positive at zero, strictly decreasing on $[0,1]$ and negative at one. The unique maximizing fractions are thus

$$
 \alpha_L^*=200-\sqrt{39769}=0.57833618184808656\ldots,\qquad
 \alpha_B^*=200-\sqrt{39849}=0.37785693966713654\ldots .
$$

These improvements are small. The exact maximizing shares exhibit the dependence on how losses change actions, even for the same two-site game.

## 3. The twelve-site placement calculation

Ginzburg, Krylov and Tsetlin divide a site's capacity among its occupants. Their 1964 simulations compare each individual's private return with the full common fund. Pittel studies a different experiment. In his 1965 paper, §1 distinguishes an independent-outcome Gur game from his variant in which every player simultaneously receives the same reward or penalty. His §2 uses two actions and synchronized depths with independent action redraws at the randomized boundary. The first linear-memory threshold in §3 concerns a specified step-shaped common feedback function. The archived twelve-site code draws independent Bernoulli signals even at full pooling. Pittel's theorem does not give a bound on its welfare. [Ginzburg, Krylov and Tsetlin (1964)](https://www.mathnet.ru/rus/at11654) · [Pittel (1965)](https://www.mathnet.ru/rus/ppi752)

For $N=12$ sites and players take one site of capacity $A=1$ and eleven of capacity $b=3/20$. At an unpooled equilibrium a weak sharer could profit by moving to an empty weak site, so weak occupancy never exceeds one. The rich site must be occupied. With $m$ players there, the two incentive inequalities require $A/m\ge b\ge A/(m+1)$, with endpoints treated as usual for unavailable deviations. There are exactly six rich-site players, since $1/6>3/20>1/7$. Raw Nash welfare per player is $19/120$, and optimal welfare at one player per site is $53/240$. Their ratio is $53/38$, an attainable gain of $39.47\%$. The original script's comment gives five occupied weak sites and a lower Nash welfare of 0.1458.

The same argument also gives all pure Nash occupancies throughout pooling. In a profile with $m\ge2$ rich players a move from the rich site to an empty weak site changes individual return by $b-A/m$ and mean welfare by $b/N$. The pooled deviation gain is
$$
 (1-\alpha)(b-A/m)+\alpha b/N .
$$
The reverse incentive from a weak site to the rich site is the negative of this expression with $m+1$ in place of $m$. A weak player moving to an already occupied weak site is worse off, and a rich player cannot prefer moving to an occupied weak site over an available empty one. If the rich site is empty, either a shared weak site exists or all $12$ players would occupy only $11$ weak sites singly, which is impossible. A move from a shared weak site to an empty weak site benefits both the individual and the common fund. If all weak sites are occupied with a weak collision, the empty rich site supplies the profitable move. These deviations exhaust the equilibrium checks. When $m=1$, all sites are singly occupied and a rich player earns the largest private return there.

For $\alpha<1$, put $z=A/[b(1+\alpha/(N(1-\alpha)))]$. The rich-site occupation is $\lfloor z\rfloor$ clipped to $[1,N]$ for nonintegral $z$. At an interior integer $z\ge2$, $z$ and $z-1$ are both equilibria. At $\alpha=1$ every site is singly occupied. In the present example the rich site successively loses one occupant at

$$
 4/7,\quad4/5,\quad8/9,\quad44/47,\quad28/29.
$$

The corresponding transitions are $6\to5\to4\to3\to2\to1$. At $28/29$ the social optimum first becomes a Nash equilibrium, and above it all Nash occupancies maximize welfare.

The original seed-42 simulation uses 40,000 rounds per cell, including 10,000 burn-in rounds. In its seven-point grid $\alpha\in\{0,.15,.30,.50,.70,.85,1\}$, the largest recorded mean raw welfare occurs at $.30,.70,.50$ for depths $3,6,12$ respectively. Its gains against the better endpoint are $.0010,.0044,.0034$. Independent replicas with 30,000 burn-in rounds and 120,000 measured rounds per cell give the following numbers. Parentheses report the estimated standard error of a mean across 16 independent replicas.

| Depth | No fund | Interior grid maximum | Full fund | Gain over private |
|---:|---:|---:|---:|---:|
| 3 | .16805962 (.00003726) | .16848804 (.00003354) at .30 | .14785638 (.00013547) | .00042842 |
| 6 | .16673492 (.00006680) | .16925941 (.00010564) at .70 | .15292940 (.00024640) | .00252449 |
| 12 | .16665376 (.00026482) | .17210967 (.00037128) at .85 | .16413062 (.00056858) | .00545591 |

These estimates quantify finite runs. The standard errors measure replicate variability and do not bound finite-time bias. Grid selection also introduces sampling uncertainty about the maximizing share.

A longer depth-12 check used eight replicas with 200,000 burn-in rounds and one million measured rounds each. The mean raw welfares at shares $0$, $.70$, $.85$, and $1$ were $.16632588$, $.17076175$, $.17194694$, and $.16358743$, with between-replica standard errors $.00008535$, $.00011815$, $.00012844$, and $.00015286$, respectively. The best observed share again was $.85$, with a gain of $.00562106$ over the better endpoint.

## 4. Pure Nash, finite stationary balance, and payoff concentration

For a two-player Prisoner's Dilemma write the four marginal win probabilities as $T>R>P>S$. Put $M=(T+S)/2$ and $\Delta=(T-S)/2$. At a mixed profile the cooperator's effective reward is $S_\alpha=S+\alpha\Delta$, and the defector's is $T_\alpha=T-\alpha\Delta$. The homogeneous payoffs $R,P$ stay fixed. Two different unilateral comparisons are relevant.

* $CC$ is a Nash equilibrium iff $\alpha\ge (T-R)/\Delta$.
* $DD$ is a Nash equilibrium iff $\alpha\le (P-S)/\Delta$.
* Cooperation is weakly dominant iff $\alpha\ge\max(T-R,P-S)/\Delta$, and strict dominance requires a strict inequality. A threshold above one is unattainable.

For the linear $N$-player public good with $k$ contributors, private probabilities $p_D(k)=a+bk$, $p_C(k)=a+bk-c$, assume $0<b<c<Nb$ and valid probabilities on the actual profiles. A deviation to contributing changes own private return by $b-c$ and mean return by $b-c/N$. The pooled deviation gain is $b-c+\alpha c(1-1/N)$, independent of other actions. Cooperation becomes weakly dominant at
$$
 \alpha_{\rm Nash}=\frac{c-b}{c(1-1/N)} .
$$
At equality all profiles are equilibria. Above it the all-cooperator action is uniquely dominant.

**Depth-one balance under independent signals.** Define $\alpha_{\rm bal}$ as the infimum of fund shares for which the stationary law of the $n=1$ chain satisfies $\pi(CC)\ge\pi(DD)$. Set
$$
 d=\nu(1-P),\qquad r=1-\nu(1-R),\qquad s=\nu(1-M),\qquad z=\nu\Delta(1-\alpha).
$$
The sign of $\pi(CC)-\pi(DD)$ is exactly the sign of
$$
 D(z)=\nu(R-P)\,[s(1-s)+z^2]-[d(1-d)+r(1-r)]z . \tag{8}
$$
Thus $\alpha_{\rm bal}=0$ when $D(\nu\Delta)\ge0$. Otherwise write $g=\nu(R-P)$, $H=d(1-d)+r(1-r)$ and set
$$
 z_*=\frac{2g\,s(1-s)}{H+\sqrt{H^2-4g^2s(1-s)}},\qquad
 \alpha_{\rm bal}=1-\frac{z_*}{\nu\Delta}.
$$

To prove this, let $u=1-\nu(1-S_\alpha)$, $v=\nu(1-T_\alpha)$. For the three states $DD$, mixed, $CC$, the directed stationary-tree numerator difference equals
$$
 Auv-B(1-u)(1-v),\qquad A=2d-d^2-(1-r)^2,\quad B=1-r^2-d^2 .
$$
Indeed the two endpoint tree sums are $(2d-d^2)uv+d^2(1-u)(1-v)$ and $(1-r)^2uv+(1-r^2)(1-u)(1-v)$ respectively. Substituting $u=1-s-z$ and $v=s-z$ gives twice (8). Here $A>0$, because $d>1-r$ and $0<d<1$ imply $2d-d^2>(1-r)^2$. If $B\le0$ the numerator is positive. If $B>0$ it is strictly increasing as $\alpha$ increases, since both $u$ and $v$ increase. At $\alpha=1$ the numerator is positive, which gives the stated threshold.

At weak dominance $u\ge1-d$ and $v\ge1-r$. For $B>0$ these inequalities imply the lower bound
$$
 A(1-d)(1-r)-Bdr=(d+r-1)^3=[\nu(R-P)]^3>0 .
$$
Thus finite stationary balance is achieved strictly by the time cooperation becomes weakly dominant, whenever that rational threshold exists. The weaker Nash condition for $CC$ admits both orderings, with exact examples.

| $(T,R,P,S)$ | Automaton | $\alpha_{\rm bal}$ | $CC$ becomes Nash | $C$ weakly dominant |
|---|---|---:|---:|---:|
| $(.95,.90,.60,.55)$ | $L_{2,2}$ | $0$ | $1/4$ | $1/4$ |
| $(.85,.80,.60,.40)$ | $L_{2,2}$ and $B_{2,2}$ | $4/9$ | $2/9$ | $8/9$ |

In the first case (8) is $3(16\alpha^2+56\alpha+3)/4000$. In the second it is $3(3\alpha+22)(9\alpha-4)/8000$ for $L$ and $3(3\alpha+62)(9\alpha-4)/64000$ for $B$. These results compare endpoint stationary masses at fixed depth one. Stationary concentration in a limit of growing memory is a separate criterion.

**An exact correlation example for any memory.** For $N$ linear automata of equal depth, suppose all-homogeneous action profiles give a shared Bernoulli signal, with win probabilities $1>R>P>1/2$ at all-$C$ and all-$D$, and mixed profiles give independent full-support signals. (At the absorbing endpoint $R=1$, the deepest all-$C$ state is the sole closed class and the stationary all-$D$ mass is zero already at every finite $n$.) From mixed actions there is a positive-probability path to all-$D$ by protecting existing defectors with wins and penalizing cooperators until they switch. From homogeneous actions, repeated common wins synchronize depths at the top. Equal-action, equal-depth states form the unique closed class, in which all $N$ agents follow the same two-action linear automaton. At the boundary detailed balance implies that the action masses have ratio
$$
 \frac{\pi(C,\ldots,C)}{\pi(D,\ldots,D)}
 =\frac{H_n(R)}{H_n(P)},\qquad
 H_n(p)=\frac1{1-p}\sum_{j=0}^{n-1}\left(\frac p{1-p}\right)^j.
$$
This ratio grows exponentially in $n$, so the cooperative concentration threshold is exactly zero even when $C$ is a strictly dominated private action. Pooling changes only the transient mixed-profile payoff signals in this example. The proof uses the deterministic action switch of $L$ and common shocks at both homogeneous profiles.

**A low-payoff obstruction for $L$ and $B$.** Suppose all payout probabilities lie in $[\ell,u]\subset(0,1/2)$, all signals are conditionally independent, and the number of players is fixed. Convex pooling preserves this interval. Each player's depth is stochastically dominated by the reflected walk with win probability $u$ and stationary geometric parameter $\rho=u/(1-u)<1$. This coupling uses a common uniform on each player's draws and reflection on $1,\ldots,n$. For a fixed $K$ sufficiently large, all depths are at most $K$ with stationary probability at least $1-N\rho^K\ge1/2$, uniformly in $n$. From this set any prescribed homogeneous action vector can be reached within exactly $K$ steps by forcing a losing player to switch at the boundary and subsequently forcing its wins, simultaneously for all players. The probability is at least $\min(\ell,\nu(1-u))^{NK}$. Thus both all-$C$ and all-$D$ have positive stationary mass bounded uniformly away from zero. For $(T,R,P,S)=(.45,.40,.30,.20)$, $CC$ becomes Nash at $2/5$ and cooperation is strictly dominant above $4/5$, yet no choice of the sharing fraction forces concentration at $CC$ as $n\to\infty$. The independent outcome law, automaton architecture and absolute feedback scale are material to any proposed general threshold.

## Reproduction

Run the following commands from the study root with Python, mpmath, and, for the Monte Carlo calculation, NumPy and Numba.

~~~sh
python experiments/phase1_pooling.py
python experiments/phase1_pooling.py --scaling
python experiments/phase1_pooling.py --quorum-shift
python experiments/phase1_pooling.py --placement-mc
python experiments/phase1_pooling.py --placement-mc --depths 12 --replicates 8 --burn 200000 --steps 1000000
~~~

The finite volunteer witnesses and two-player balances use exact rational stationary distributions, with every equation rechecked. The optional scaling run uses 80 decimal digits and independently verifies the first-moment identity and exact unpooled renewal formula.
