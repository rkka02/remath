# Canonical quadrilaterals, boundary parity and exceptional frequencies

## Frequencies and orientation

Throughout this note \(s=\tan\beta=\sqrt{1-\lambda^2}/\lambda\) is the physical ray slope \(dz/dx\). The equation \((1-\lambda^2)u_{zz}-\lambda^2u_{xx}=0\) factors in \(z\pm sx\). The boundary map first follows the slope \(+s\) and then the slope \(-s\). Write its **clockwise** rotation as \(p/q\) in lowest terms. In the counterclockwise convention replace \(p\) everywhere by \(q-p\). The period \(q\) always counts pairs of chords.

Take horizontal bases separated by height \(H\), with full width \(W\) at midheight. Let \(A=\tan\alpha>0\) be the absolute slope \(dx/dz\) of an inclined side, so \(\alpha\) is the wall's departure from vertical. For \(sA<1\) define

\[
\Lambda=\frac{1+sA}{1-sA}.
\]

| Tank | Globally periodic rational directions | Regular attracting directions | Multiplier of the complete attracting \(b\)-cycle |
|---|---|---|---|
| Upright rectangle | Every rational rotation | None | — |
| Right trapezoid, one inclined side | \(q-p\) even | \(q-p\) odd, tongue interior | \(\Lambda^{-1}\) |
| Isosceles trapezoid, opposite side inclinations | \(p\) odd | \(p\) even, tongue interior | \(\Lambda^{-2}\) |
| Sheared parallelogram, equal side inclinations | \(q\) odd | \(q\) even, tongue interior | \(\Lambda^{-2}\) |
| Tilted rectangle or square, \(\phi<\beta<\pi/2-\phi\) | \(q\) odd | \(q\) even, tongue interior | \(\mu^{-2}\), \(\mu=\tan(\beta+\phi)/\tan(\beta-\phi)\) |

Each rational line in the table refers to rotations attained by the fixed geometry. The global cases have \(b^q=\mathrm{Id}\) and infinitely many independent smooth Dirichlet modes. The remaining cases have no finite-energy mode, including tongue endpoints whose periodic ray hits a corner. An irrational direction has dense boundary orbits. Section and boundary periods enter differently in this table. The source two-break theorem classifies the denominator of a wall return. [Lenci, Bonanno and Cristadoro, Theorem 2.2 and Proposition 3.1](../sources/papers/Lenci_Bonanno_Cristadoro_2021_InternalWaveBilliards_2102.01654.pdf) · [Polygonal finite-energy criterion](phase1_pde.md)

In particular, give all four horizontal-base tanks the same \(H,W\) and choose \(s=H/W\), \(AH<W\). At this one frequency all four have clockwise rotation \(1/2\). The upright and isosceles tanks have \(b^2=\mathrm{Id}\). The right trapezoid contracts by \(\Lambda^{-1}\) per cycle and the shear by \(\Lambda^{-2}\). For \(H=W\) and \(\alpha=15^\circ\), these two contraction factors are \(1/\sqrt3\) and \(1/3\). A square tilted through \(15^\circ\) at the same frequency contracts by \(1/9\). These are full-cycle factors. The Lyapunov exponent per application of \(b\) is their logarithm divided by two.

## A common wall section

Write the walls \(L(z)\le x\le R(z)\), with affine \(L,R\), and unfold top and bottom into the increasing phase \(t\pmod {2H}\), with \(V(t)=\operatorname{dist}(t,2H\mathbb Z)\). The physical height is \(V(t)\). In the transverse regime \(s\max(|L'|,|R'|)<1\), a side collision reverses horizontal velocity and preserves vertical velocity. All maps \(E_X^\pm(t)=t\pm sX(V(t))\) are increasing lifts. The side-to-side maps and the full left return are

\[
T_{LR}=(E_R^-)^{-1}E_L^-,\qquad
T_{RL}=(E_L^+)^{-1}E_R^+,\qquad F=T_{RL}T_{LR}.
\]

For example \(T_{LR}(t)-t=s[R(V(T_{LR}(t)))-L(V(t))]\). This gives the first formula, and taking the difference of abscissas in the reverse order gives the second. If \(F\) has lift rotation \(N/M\) in units of \(2H\), a primitive regular orbit has \(2M\) side hits and \(2N\) horizontal-base hits. Thus

\[
q=M+N,\qquad p=N,\qquad \rho(b)=\frac{\rho(F)}{1+\rho(F)}.
\]

For the numerator, normalize position across the local width to \(0\le h\le1\), and reflect alternate traversals so that \(h\pmod2\) increases. Its velocity is positive because \(s\max(|L'|,|R'|)<1\). Let \(y=t/H\pmod2\). On this torus the boundary points with outgoing positive-slope chord form the entry edges of the two cells where \(h\) and \(y\) have equal integer parity. Clockwise they form the staircase from \((0,0)\) to \((0,1),(-1,1),(-1,2),(-2,2)\). Successive sections can be lifted by \((2,0)\). The period vector \((2M,2N)\) equals \(q(2,0)+p(-2,2)\). The same intersection formula follows for irrational slopes by mean crossings. At a simultaneous horizontal and lateral hit the two crossings count with multiplicity, or one can take limits of paths through regular starting points. In particular the reported winding counts the original chord map even where a corner ray has a zero-length reflected chord.

Normalize \(t\) to circumference one for the rest of the section, and now let \(V(t)=\operatorname{dist}(t,\mathbb Z)\). Reflect the physical tank vertically when needed to take the slope of a model right wall positive. This reflection exchanges the two ray directions and reverses the boundary orientation, preserving the stated clockwise rotation. With \(e=sA,\ a=(1-e)/2,\ d=1-a\), define

\[
U(t)=t-eV(t),\quad J(t)=t+\tfrac12,\quad
K_a=UJU^{-1},\qquad
K_a(t)=
\begin{cases}
a+(d/a)t,&0\le t\le a,\\
1+(a/d)(t-a),&a\le t\le 1.
\end{cases}
\]

Extend by degree one. The identity \(K_a^2(t)=t+1\) follows from the conjugacy, and \(U(t+1/2)=t+eV(t)+a\). Denote by \(h=T_\delta K_a\) the two-break map with output translation \(\delta\).

- **Right trapezoid.** Set \(L=0,\ R(z)=W+A(z-H/2)\). The full section map is \(E_R^+(E_R^-)^{-1}\). Writing \(c=sW/(2H)-e/4\), this is \(T_c T_{-a} K_a T_c\), conjugate to \(h\) with \(\delta=2c-a=sW/H-1/2\). Its primitive period is \(M\).
- **Isosceles trapezoid.** Center the tank and write \(L=-B,\ R=B\). Both side-to-side maps are the same lift \(G=(E_B^-)^{-1}E_B^+\). Conjugation by \(E_B^-\) gives the right-trapezoid map for half the midheight width. Thus \(\delta=sW/(2H)-1/2\), and \(F=G^2\). If \(\rho(F)=N/M\), the denominator of \(\rho(G)=N/(2M)\) is odd exactly when \(N\) is even. In that case a complete physical cycle makes two trips round the model orbit. At \(sW=H\) the affine equality \(s[B(z)+B(H-z)]=H\) gives \(G(t)=t+1/2\) for every \(t\).
- **Sheared parallelogram.** Take \(L(z)=Az,\ R(z)=W+Az\). Then \(T_{LR}=U^{-1}T_\delta U\), with \(\delta=sW/(2H)\). Central inversion identifies the other half trip by the half-period translation \(J\). Put \(G=JT_{LR}\). As circle maps \(F=G^2\), and their natural lifts satisfy \(F=G^2-1\). Conjugating \(G\) by \(U\) and a translation gives \(h\). Thus \(\rho(h)=(M+N)/(2M)\). Its denominator is odd exactly when \(q=M+N\) is even, in which case it is \(M\). The complete physical cycle then squares the model multiplier.
- **Upright rectangle.** Clockwise boundary length density \(s|dx|+|dz|\) makes the two involutions isometric and \(b\) a translation through \(2sW\) on a circle of length \(2(H+sW)\). The rotation is \(sW/(H+sW)\). Separation gives \(\lambda_{mn}^2=(n/H)^2/[(m/W)^2+(n/H)^2]\), \(m,n\ge1\), and the separated sine products form a complete eigenbasis.

The family \(h\) has reciprocal slopes \(\Lambda=d/a,\Lambda^{-1}\) and exactly two breaks. Its increasing branch has length \(a\) and the left endpoint advances by \(\delta+a\). These data identify it up to rotation with the surface section in Lenci et al., Appendix A, with their \(m=d\) and projective direction \(s_{\mathrm{LBC}}=\delta\pmod1\). Their rational classification gives global finite order for an even section denominator \(D\) and excludes every identity interval when \(D\) is odd. In an odd-denominator tongue interior the two regular \(D\)-cycles interlace. Between consecutive fixed points of \(h^D\) there must be a break because an affine map fixing both endpoints is the identity there. There are \(2D\) gaps and at most \(2D\) breaks, so each gap has one. Adjacent fixed-point slopes differ by a factor \(\Lambda^2\). Their exponents are odd and have opposite signs, hence are exactly \(+1,-1\). This proves the full multipliers in the table. At a tongue boundary the returning physical orbit can have different one-sided slopes. [Lenci, Bonanno and Cristadoro, pp. 14–21 and Appendix A](../sources/papers/Lenci_Bonanno_Cristadoro_2021_InternalWaveBilliards_2102.01654.pdf)

## Corner windows, critical lines and re-entry

For an inclined side the open corner regime is \(\beta>\pi/2-\alpha\), or \(0<\lambda<\sin\alpha\). There is one common extremal vertex for a right trapezoid. An isosceles trapezoid whose bottom is wider has the two bottom vertices, and a shear has two opposite vertices. This follows directly by checking the signs of \(d(z\pm sx)\) on each pair of incident edges. An orientation-preserving circle map with these fixed points moves monotonically to an endpoint of each complementary interval. A common fixed corner has reciprocal one-sided multipliers, so a ray approaching one of its branches is enough for the finite-energy obstruction. [Corner energy proof](phase1_pde.md)

The critical value \(sA=1\) also has zero kernel. For a parallelogram straighten the two characteristic-parallel sides to \(\xi=0,C\) in ray coordinates. The other sides are \(\eta=k\xi,\eta=k\xi+D\), \(D>0\). For a solution \(P(\xi)+Q(\eta)\), the first characteristic side makes \(Q\) constant on \((0,D)\). The remaining side equalities \(Q(k\xi)=Q(k\xi+D)\) propagate this value over the entire projected interval. Coordinate reversals reduce to \(k\ge0\). If \(k=0\), all sides are characteristic and the same conclusion follows directly. A positive-length fiber gives the corresponding one-variable profile its ordinary \(H^1\) endpoint trace.

For a right trapezoid take \(L=0,\ R(z)=W_0-Az\). Put \(\xi=z+sx,\eta=z-sx,\ B=sW_0>H\). The right side is \(\xi=B\), so \(Q\) is constant for \(-B<\eta<2H-B\). On the bottom \(\eta=-\xi\) and on the top \(\eta=2H-\xi\). Thus \(Q(y)=Q(y+2H)\) on \((-B,-H)\). Starting with the known interval of length \(2H\) propagates constancy up to \(\eta=H\), the entire projection. For the isosceles tank take \(L(z)=Az,\ R(z)=W_0-Az\), hence \(B>2H\). The same two parallel-line relations now hold on \((-B,-2H)\) and propagate constancy up to \(\eta=0\), its projected maximum. The energy identities at \(\lambda=0,1\) also exclude Dirichlet modes.

All three horizontal-base tanks with \(A>0\) admit infinite sequences of standing frequencies accumulating at \(\lambda=1\). Their full-section lifts increase strictly with \(s\). For example the equation defining \(T_{LR}\) has a right arrival at larger horizontal position than the departure, while \(t\mapsto t-sR(V(t))\) is strictly increasing. Raising \(s\) therefore raises the arrival phase. The other trip has the same property. The full-section rotation \(\rho(F)\) is continuous, positive and tends to zero as \(s\downarrow0\). Hence it attains \(1/(n-1)\) for all sufficiently large \(n\), giving clockwise boundary rotation \(\rho(b)=1/n\). For \(\rho(b)=1/n\), each odd \(n\) in this range gives a global period-\(n\) boundary map in all three geometries. Strict pointwise order gives uniqueness of a finite-order angle by comparing complete iterates.

In fact if \(w(z)=R(z)-L(z)\), the original unnormalized section gives \(F(t)=t+2s w(V(t))+O(s^2)\) uniformly. This uses the uniform Lipschitz constants of \(L,R,V\) and an \(O(s)\) flight increment. Introduce length coordinate \(Y'(t)=[2w(V(t))]^{-1}\) of circumference \(I=\int_0^H dz/w(z)\). Its uniform increment per return is \(s+O(s^2)\), so \(\rho(F)=s/I+O(s^2)\). Consequently along the neutral subsequence \(\rho(b)=1/n\),

\[
s_n=\frac I n+O(n^{-2}),\qquad
\lambda_n=1-\frac{I^2}{2n^2}+O(n^{-3}).
\]

For a nonconstant affine width, \(I=H\log(w(H)/w(0))/(w(H)-w(0))\). For the shear \(I=H/W\).

## Tilted rectangle and closed families

Let \(u=\tan(\beta-\phi),\ v=\tan(\beta+\phi)\) on the open supercritical interval of a rectangle with sides \(1,R\). In body coordinates the rays have slopes \(u,-v\). The change \(x=X+(v^{-1}-u^{-1})Y/2,\ z=(v^{-1}+u^{-1})Y/2\) turns these into slopes \(+1,-1\), maps horizontal sides to horizontal lines and gives a sheared parallelogram. A horizontal reflection makes the shear positive when convenient. The model is precisely

\[
a=\frac u{u+v},\quad d=\frac v{u+v},\quad
\mu=\frac vu,\quad \delta=\frac{uv}{R(u+v)},\qquad
\rho(b)=1-\frac1{2\rho(h)}
\]

with the lift above. The direct boundary map can have branches of slope one even though the reduced return has only two slopes. The half-period shift accounts for their different rotation numbers.

For every \(j\ge1\), the full two-chord map satisfies

\[
\begin{aligned}
\rho(b)=1/(2j)&\iff j u+(j-1)v\le R\le(j-1)u+jv,\\
\rho(b)=1/(2j+1)&\iff j(u+v)=R,\\
\rho(b)=2/5&\iff R=(u^2+uv+v^2)/(u+v).
\end{aligned}
\]

Here the first set is intersected with the supercritical angular window. To obtain the first two equations observe that \(h^2(x)=1+x+\delta/d\) on the part of the expanding branch whose first image stays in \([a,1]\). Starting at \(a\), the complementary calculation gives increments \(\delta/a\) as long as the two-step itinerary stays on that branch. At \(\delta=ad/j\), \(h^{2j}(0)=j+a,\ h^{2j}(a)=j+1\). This gives the global finite-order direction with boundary rotation \(1/(2j+1)\). For \(j\ge2\), at \(\delta=ad/(j-1+a)\) the first \(j-1\) double steps from zero give \(j-1+(j-1)\delta/d\), then \(h^{2j-1}(0)=j\). At \(\delta=ad/(j-1+d)\) the opposite endpoint gives \(h^{2j-1}(a)=j+a\). The intermediate points remain on the stated branches by the displayed inequalities for \(\delta\). These are the only two tongue boundaries by the two-break theorem and strict ordering in \(\delta\). For \(j=1\) the fixed point condition is \(a\le\delta\le d\). For \(2/5\) substitute \(\delta=ad/(1-ad)\), obtaining \(h^3(0)=2+a,\ h^3(a)=3\) and lift rotation \(5/6\). Uniqueness follows from global finite order and strict ordering. Other rational boundaries can be obtained by solving the two piecewise-affine break images \(h^D(0),h^D(a)\) on their stated branches. [General tongue formulas and earlier literature](phase1_rectangle.md)

Use the reduced tilt \(0<\phi<\pi/4\). For a larger acute tilt exchange the body axes, sending \((\phi,R)\) to \((\pi/2-\phi,1/R)\). At \(\phi=\pi/4\) the open supercritical window is empty and the characteristic angle has zero Dirichlet kernel. In the reduced range the \(1/2\) tongue covers the entire supercritical window exactly when \(\cot(2\phi)\le R\le\tan(2\phi)\). In that range the point spectrum is empty. Otherwise the continuous rotation assumes a nondegenerate interval of values, including infinitely many reduced fractions with odd denominator. The resulting eigenvalue set is countably infinite and every eigenspace is infinite dimensional. For a square the transition is \(\phi=\pi/8\). Kopecz identified the square's geometric saturation angle and computed the squared slope ratio for the simple attractor. Bajars, Frank and Maas identified the parity phenomenon and wrote the full square resonance families with one winding count equal to one. [Kopecz, Theorems 2–3](https://webspace.science.uu.nl/~maas0131/files/kopecz2006.pdf) · [Bajars, Frank and Maas, §2.4](https://webspace.science.uu.nl/~frank011/Articles/BaFrMa12.pdf)

## Full-measure capture in each fixed canonical tank

Write \(h=T_\delta K_a\), with \(d=1-a\). Set \(U_*=\delta/d,\ V_*=\delta/a\) for a choice of translation lift making \(\delta>0\). These are the two positive body slopes of a corresponding unit-aspect square. For a fixed horizontal-base tank choose

| Geometry | \(\delta=C+Ds\) | \(a\) |
|---|---|---|
| Right trapezoid | \(1/2+sW/H\) | \((1-sA)/2\) |
| Isosceles trapezoid | \(1/2+sW/(2H)\) | \((1-sA)/2\) |
| Shear | \(sW/(2H)\) | \((1-sA)/2\) |

The first two lifts add one to the earlier translation. Direct differentiation gives \(U_*'>0\) and \(V_*'>0\), since their signs are respectively those of \(D-AC\) and \(D+AC\). The shorter base being positive implies \(W/H>A/2\) for the right tank and \(W/(2H)>A/2\) for the isosceles tank. The shear has \(C=0\).

For any smooth path on which \(0<U_*<V_*\) and both derivatives are positive, almost every parameter has a regular attracting cycle. This follows from the Hecke-group crossing argument in the companion proof. It applies to each fixed member of all three horizontal-base families, including every admissible individual right trapezoid. In \(\beta\) the measure of regular periodic attraction is \(\pi/2-\alpha\). In \(\lambda\) it is \(1-\sin\alpha\), and the corner interval has complementary measure \(\sin\alpha\). At each reduced tilt \(0<\phi<\pi/4\), a fixed rectangle has regular periodic-attractor measures \(\pi/2-2\phi\) and \(\cos\phi-\sin\phi\) in the respective variables. Its two corner windows fill the complementary measure. [Fixed-parameter moving-gap proof](phase1_parity.md) · [Original two-parameter result, Theorem 3.2 and Appendix A](../sources/papers/Lenci_Bonanno_Cristadoro_2021_InternalWaveBilliards_2102.01654.pdf)

## A Hausdorff-dimension gap on every tilted-rectangle slice

**Claim.** For each \(0<\phi<\pi/4\) there is a \(D_\phi<1\), independent of \(R>0\), such that the supercritical directions without a regular periodic attractor have Hausdorff dimension at most \(D_\phi\). The same holds in \(\lambda\). On every compact subinterval of the transverse regime of any of the three horizontal-base tanks, the exceptional set likewise has dimension strictly below one.

**Fixed surface.** In Lenci et al., Appendix A, the real projective direction is \(\delta\) above. Their group has generators \(\delta\mapsto\delta+1\) and \(\delta\mapsto\delta/(k\delta+1)\), \(k=1/(ad)>4\). Its discontinuity domain is carried into their fundamental interval (A.8), strictly inside the regular fixed-point tongue \((a,d)\), and affine symmetries preserve the hyperbolic closed trajectories. Thus every exceptional direction is in the group's limit set. In the coordinate \(y=\ell\delta,\ \ell=\sqrt{k}>2\), the group lies in the Hecke group generated by \(T(y)=y+\ell,\ S(y)=-1/y\). Its finite limit points lie in the translates by \(m\ell,\ m\in\mathbb Z\), of finite and infinite strings of

\[
\varphi_{n,\ell}(z)=-1/(n\ell+z),\qquad n\in\mathbb Z\setminus\{0\}.
\]

Finite strings end at zero. This inclusion follows by writing reduced words \(T^m S T^{n_1}\cdots S T^{n_j}\) and taking subsequences. A digit tending to infinity sends the remaining tail uniformly to zero. Stable digits at every depth give a unique infinite limit by uniform contraction on the complex unit disk. A final \(S\) fixes the base point \(i\) used to take group orbit limits.

**Uniform fiber dimension.** Fix \(\ell\ge L>2\), and put \(I=[-1,1]\), \(r=(L-1)^{-1}<1\). The first-level intervals are disjoint, lie in \([-r,r]\), and every map contracts by at most \(r^2\). Log derivatives are \(2r\)-Lipschitz on \(I\), so the ratio of the largest to smallest derivative of every word is at most \(K=\exp(4r/(1-r^2))\). Each cylinder consequently loses at least the proportion \(\eta=(1-r)/(2K)>0\) through the image of \((r,1)\). The total length of level \(j\) is at most \(2(1-\eta)^j\), uniformly in \(\ell\ge L\). Choose \(j\) so that \(K(1-\eta)^j<1/2\). If \(M_w\) is the supremum derivative of a length-\(j\) word, then \(\sum_w M_w<1/2\).

This last strict bound persists uniformly for \(\sum_w M_w^t\) at some \(t=t_L<1\). In detail, \(M_w\le\prod_{n\in w}(|n|L-1)^{-2}\), so \(\sum_w M_w^{2/3}\) is uniformly bounded by a finite product of convergent sums. For \(3/4\le t<1,\ 0<x<1\), \(0\le x^t-x\le C(1-t)x^{2/3}\) by the mean value theorem applied to \(x^t\). Choose \(t\) sufficiently close to one to obtain \(\sum_w M_w^t<1\) uniformly. Covering by blocks of \(j\) digits bounds the Hausdorff dimension of the infinite strings by \(t_L\). Countably many finite strings and integer translates preserve this bound.

**Motion of addresses.** Fix a real \(\ell_0>2\). On a small complex disk about \(\ell_0\) with \(\operatorname{Re}\ell>2+\varepsilon\), the branches map the closed unit disk strictly into itself and contract uniformly. Each address \(y_\omega(\ell)\), including a fixed outer translate, varies holomorphically by uniform convergence. Distinct addresses give distinct complex values. Different next digits would require \(|(n-m)\ell|\le2\), and an infinite branch cannot equal the terminal zero. Outer translates satisfy the same separation. For a fixed outer translate choose \(C\) greater than all pairwise distances on this disk. For two different addresses the positive harmonic function \(\log(C/|y_\omega(\ell)-y_\nu(\ell)|)\) obeys Harnack's inequality. On a sufficiently small concentric disk this yields, for any chosen \(\eta_0<1\),

\[
|y_\omega(\ell)-y_\nu(\ell)|
 \le C^{1-\eta_0}|y_\omega(\ell_0)-y_\nu(\ell_0)|^{\eta_0}.
\]

Thus motion of an entire fixed fiber has a uniform Hölder estimate whose exponent can be taken arbitrarily close to one locally. This uses the same analytic disk and constant for all words.

**Crossing the physical path.** Write
\[
v_0=\tfrac12\log(V_*/U_*),\quad x=\log\sqrt{U_*V_*},
\qquad \ell=2\cosh v_0,\quad y=e^x.
\]
For any positive address the graph \(E_\omega(v_0)=\log y_\omega(2\cosh v_0)\) is 1-Lipschitz. To check this, start a finite word with \(z=0\) and set \(d_0=e^{-v_0}\). The two inequalities \(|z'|\le|z|\le d_0\) propagate under each \(\varphi_n\), because \(|n\ell+z|\ge|n|\ell-d_0\), \(|n\ell'+z'|\le|n|\ell'+d_0\) and \(\ell-\ell'=2d_0\). Taking the negative reciprocal preserves the logarithmic derivative bound and its new absolute value is at most \(d_0\). The final translation satisfies the same logarithmic derivative bound. Infinite words follow by limits locally where the address is positive. Along the physical path \(x\) increases and \(|dv_0/dx|<1\) since \(U_*',V_*'>0\).

Near a fixed transverse point take \(|dv_0/dx|\le\kappa<1\). The function \(x-E_\omega(v_0(x))\) increases by at least \((1-\kappa)\Delta x\), and each address intersects the path at most once locally. If two addresses meet at \(x_1,x_2\), evaluate this bound for the first graph at the second crossing. On an interval of positive \(y\) bounded away from zero, the logarithm is Lipschitz. Thus

\[
|x_1-x_2|\le C_1|y_{\omega_1}(\ell(x_2))-y_{\omega_2}(\ell(x_2))|
\le C_2|y_{\omega_1}(\ell_0)-y_{\omega_2}(\ell_0)|^{\eta_0}.
\]

Patches can be chosen so that all crossing addresses remain positive and bounded away from zero throughout the patch, by the uniform holomorphic bound (or the 1-Lipschitz log bound at the crossing). Choose \(\eta_0>t_L\). The image of the crossing subset of the frozen fiber then has dimension at most \(t_L/\eta_0<1\). Countably many outer translates and patches suffice, and \(\eta_0\) can approach one using smaller patches. It follows that the slice has dimension at most \(t_L\) whenever \(\ell\ge L>2\). Smooth changes between \(x,\beta,\lambda\) preserve this upper bound locally in the open window.

For a tilted rectangle, \(\ell=\sqrt{v/u}+\sqrt{u/v}\ge2/\cos(2\phi)>2\) throughout the supercritical interval. Take \(L=2/\cos(2\phi)\). For a horizontal-base tank, \(\ell=2/\sqrt{1-(sA)^2}>2\) on every compact range bounded away from \(s=0\). This proves the claim. It gives an upper bound on exceptional directions and makes no assertion about their exact dimension. The uniform estimate comes from the strictly positive wall tilt and the dimension argument above. [Lenci, Bonanno and Cristadoro, Appendix A](../sources/papers/Lenci_Bonanno_Cristadoro_2021_InternalWaveBilliards_2102.01654.pdf)

**An explicit bound at fifteen degrees.** For every \(15^\circ\le\phi<45^\circ\) and every \(R>0\), the exceptional set has Hausdorff dimension at most \(9/10\). Here \(\ell\ge L=4/\sqrt3\), and each branch preserves \([-d_0,d_0]\) with \(d_0=1/\sqrt3\). A single digit has derivative supremum at most \(M_n=3/(4|n|-1)^2\). For three nonzero signed digits, the product of the fractional linear matrices bounds the derivative supremum by

\[
M_{ijk}=\frac{27}
{\bigl(|64ijk-12i-12k|-|16ij-3|\bigr)^2}.
\]

In fact the reciprocal square root of the derivative supremum at \(\ell\) is
\(\lvert ijk\ell^3-(i+k)\ell\rvert-d_0\lvert ij\ell^2-1\rvert\).
Its derivative is at least \(\lvert ijk\rvert(3\ell^2-2-2d_0\ell)>0\), because the first term inside each absolute value has larger magnitude on \([L,\infty)\). Evaluation at \(L\) gives the formula above.

Take \(t=9/10,\ N=24\). The finite head is \(\sum_{1\le |i|,|j|,|k|\le N}M_{ijk}^t\). Write \(S=2\sum_{n=1}^N M_n^t\) and let \(T=(4N-1)M_N^t/[2(2t-1)]\), an upper bound for the one-digit tail by the integral test. All omitted three-digit words together cost at most \(3S^2 T+3S T^2+T^3\) by the chain rule. The script rounds every power **up** to a multiple of \(10^{-12}\) by exact integer comparisons of tenth powers. The resulting rational upper bound for head and tail is less than \(991/1000\) (approximately \(0.990179874\)). The covering sum for three-digit blocks at \(t=9/10\) is consequently less than one throughout \(\ell\ge4/\sqrt3\). The Hölder motion proof transfers this exponent to every fixed rectangle of the indicated tilt. [Exact integer certificate](../experiments/phase1_canonical.py)

## Exact reproducibility

The companion script independently intersects every chord with the physical boundary using rational arithmetic. It pulls every possible break of \(b^q\) back to the original boundary, tests identity on the entire partition and locates all isolated attracting and repelling points. The effective tilted-body slopes \((1/6,1/2),(2/3,2),(3/2,9/2)\) all yield complete attracting multiplier \(1/9\), at boundary rotations \(1/4,1/2,7/10\), respectively. For \((4/3,4)\) it verifies \(b^3=\mathrm{Id}\) at rotation \(2/3\). It also checks the two \(1/(2j)\) break equations and the \(1/(2j+1)\) global identities for \(1\le j\le4\) at each of two independent break positions, and the \(2/5\) resonance. Run **python3 experiments/phase1_canonical.py**. [Exact original-map checks](../experiments/phase1_canonical.py)
