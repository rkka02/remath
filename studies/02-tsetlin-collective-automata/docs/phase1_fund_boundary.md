# Redistribution thresholds in an independent two-player dilemma

Let the original entries be T>R>P>S, with P>1/2. Take independent synchronous outcomes conditional on the profile and linear or private-random-boundary tactics of equal depth. Pooling leaves R and P fixed and sends T to Tα=T−α(T−S)/2 and S to Sα=S+α(T−S)/2.

A cooperative pair is a Nash equilibrium when Tα≤R. Cooperation is weakly dominant when this and Sα≥P both hold. The thresholds are respectively $2(T-R)/(T-S)$ and $2\max(T-R,P-S)/(T-S)$, provided the relevant number is at most one. Strictness requires the corresponding strict inequalities. For the linear N-player public good $p_i=b+v k-c\mathbf1_{\{i=C\}}$, $k$ counts all cooperators. A unilateral switch to C changes its effective payoff by $v-c+\alpha c(1-1/N)$, giving the exact common Nash and dominance threshold $(c-v)/(c(1-1/N))$ for $c/N<v<c$, with feasible probabilities. The stationary result below concerns the paired automata.

In the constant-mean family $T+S=2P$, write $h_x=\log(x/(1-x))$ and $d=(T-S)/2$. At all fund levels $S_\alpha\le P\le T_\alpha$. If $h_R>2h_P$, the automata select CC at every fund level. If $h_R<2h_P$, the strict phase transition occurs at
$$
K=\exp(h_R-h_P),\qquad
z_* = \frac{2(K-1)P(1-P)}
{K+1+\sqrt{(K+1)^2-4(K-1)^2P(1-P)}},\qquad
\alpha_*=1-z_*/d .
$$
Below it DD is selected, above it CC is selected. The formula here compares strict exponential phases. At an all-positive-drift exponential tie the tree exponents alone do not identify the limiting masses.

Indeed, on $S_\alpha\le1/2$ the odds exponent is $h_R-2h_P$. On $S_\alpha>1/2$ the three-core tree gives $h_R-\min(2h_P,h_P+h_{T_\alpha}-h_{S_\alpha})$. The mixed core is no more stable than DD because $S_\alpha\le P$. At full pooling $S_1=T_1=P$, CC wins strictly since $R>P$. At a candidate cascade crossing in the second case, $h_{T_\alpha}-h_{S_\alpha}=h_R-h_P<h_P$, so $S_\alpha>1/2$. The left hand side decreases strictly from a value above $h_R-h_P$ to zero. Setting $z=(1-\alpha)d$ reduces the equation to $(K-1)(P(1-P)+z^2)=(K+1)z$. This proves existence, uniqueness and the formula even when the initial S lies below one half. The same strict argument uses the sign when $h_R>2h_P$. [Independent-game proof](phase1_social_game.md)

| Original game (R, P, T, S) | Cooperative-pair Nash threshold | Automaton threshold (strict phases) |
|---|---:|---:|
| (.80, .60, .90, .30) | 1/3 | 0 |
| (.80, .70, .85, .55) | 1/3 | $1-(19-\sqrt{340})/1.5=0.62605927639051641334\ldots$ |

At zero pooling the second game instead selects cooperation by varying the DD correlation through $13/63$ with its original incentives fixed. Both effects admit an exact comparison in the same game. The Nash column uses the existence of a cooperative equilibrium. Strict dominance would be a different comparison. The finite-depth population result uses a specified volunteer game and a different limiting parameter. [Partial funds with finite memory and growing population](phase1_pooling.md)

For the preliminary fund run $(R,P,T,S)=(.80,.70,.95,.35)$ itself, the cooperative-pair Nash threshold is exactly $.50$. The strict large-depth L/B threshold is
$$
  1-\frac{38-\sqrt{1353}}{6}=0.79719138591650697502\ldots .
$$
Here the mixed mean is $.65$. While $S_\alpha\le.5$, $T_\alpha\ge.8>P$, so the independent short-sucker result selects DD. For $S_\alpha>.5$ both mixed rewards exceed one half and $S_\alpha\le.65<P$. The tree test reduces to $h_{T_\alpha}-h_{S_\alpha}<h_R-h_P$ because $2h_P>h_R$. Write $S_\alpha=.65-z$, $T_\alpha=.65+z$. The same odds equation now has $P(1-P)$ in the quadratic replaced by $.65\cdot.35$, giving the displayed solution. Weak cooperative dominance is unattainable because $S_1=.65<P$.
