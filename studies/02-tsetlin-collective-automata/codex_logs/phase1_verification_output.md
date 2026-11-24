# Phase 1 verification record · 24 November 2026

The numerical exhibits below use finite chains. The large-memory and large-population conclusions are proved separately in the [research report](../docs/phase1_scouting.md). The study index lists the [reproduction commands](../STUDY.md).

| Independent check | Observation |
|---|---|
| Dense mpmath versus nonnegative state elimination | The small labeled chains agree with their exchange quotients and dense stationary solutions. The depth-40 synchronized L probability also agrees with its exact one-dimensional law. |
| Independent memory payoffs | Rational bounds give $.743962571531403<W_1(10,10)<.743962571531405$ and $.746391275680355<W_1(11,10)<.746391275680358$. |
| Hard frozen square, $P=.7,\ \kappa=.5$ | At $(40,40)$ the per-excursion corner probability is $2.0954398658851021016682068531065350563710911352133316737990808\times10^{-21}$, with relative enclosure width below $4.8\times10^{-63}$. |
| Neutral independent rectangle | At $p=1/2$ the finite spectral formula matches exact rational state elimination at $(2,2)$ and $(5,3)$. Independent quadrature and Jacobi elliptic evaluation at 75 working digits verify square coefficients $1.57260953586626338$ for L and $5.38744691613048646$ for B. |
| Soft and hard frozen rectangles | At $(120,40)$ with $P=7/10,\ \kappa=181/189$, the B and L probabilities are respectively $1.01131510213573625669\times10^{-61}$ and $2.11390076797060445400\times10^{-64}$. Exact rational Dirichlet residuals give relative interval widths below $10^{-80}$ for both. |
| Full-game interface | With $(P,T,S,\kappa_P)=(.6,.9,.2,.99)$, depths $(80,40)$ and the first CC entry as target, the per-excursion probabilities are $1.25381701957350534793\times10^{-25}$ for L and $5.92352609835928960410\times10^{-22}$ for B. Both exact rational enclosures have absolute width below $2\times10^{-112}$. |
| Stag Hunt | Exact integer determinants give $\pi_1(CC)=3328/9233$, $\pi_2(CC)=58905001984/110489411359$ and $\pi_{10}(CC)>4/5$. Worst-start total-variation mixing at tolerance $1/4$ takes exactly 5 and 67 rounds at depths 1 and 2. |
| One-quarter quorum | At $N=512$ with depth-one B, the 80-digit chain gives $W(3/5)=.789995806091765005542068626362$ and $W(19/30)=.793358361316504434715727484115$. |

The hard-corner and full-game calculations use different stopping events. The full interface script also reports a floating-point convergence scan through short depth 80. Its depth-40 rational certificate and the mpmath kernel solve provide independent checks. The complete pair stationary data retain 72 working digits. [Square and rectangular stationary data](../experiments/data/phase1_shocks.json) · [Optimal-correlation data](../experiments/data/phase1_aspect.json) · [Stag Hunt data](../experiments/data/phase1_reversal_curve.json)
