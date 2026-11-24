# Regular polygons approaching the disk

Take the unit circumradius regular \(N\)-gon with vertex arguments \(\phi+2jh\), where \(h=\pi/N\). Here \(\phi\) locates a **vertex**. The first flight has slope \(s=\tan\theta\), the second has slope \(-s\), and the PDE frequency is \(\lambda=\cos\theta\). In counterclockwise coordinates the disk boundary map rotates by \(-4\theta\). In this note \(p/q\) labels the **clockwise** rotation number. The counterclockwise label is \(1-p/q\) for \(0<p/q<1\). Each iteration of \(b\) comprises two flights.

## The half-frequency paradox

At the single frequency \(\lambda=1/\sqrt2\), a regular \(N=4m+2\) polygon with a vertex on the horizontal axis has **exactly \(N/2-1\) attracting period-two boundary orbits**. There are equally many repelling orbits. The table has both a horizontal and a vertical reflection symmetry. On the aligned decagon four attractors realize two different contraction factors. On the disk the same frequency gives an exact half-turn of the whole boundary.

Write \(L=N/2-1\). The list of per-iteration contraction factors, with multiplicity, is

\[
 m_j=\frac{\sin(2jh)-\sin h}{\sin(2jh)+\sin h},
 \qquad 1\leq j\leq L.
\]

The full period multiplier is \(m_j^2\). The most strongly focusing branch has \(m_{\min}=(2\cos h-1)/(2\cos h+1)\to1/3\). The weakest has \(m_{\max}=(\cos h-\sin h)/(\cos h+\sin h)\to1\). Uniformly weighting the attracting orbits gives

\[
 \frac1L\sum_{j=1}^{L}\log m_j
 =\frac{2\log\tan(h/2)}{L}
 \sim-\frac{4\log(2N/\pi)}{N}.
\]

| \(N\) | Attractors | Strongest factor | Weakest factor | Mean log factor |
|---:|---:|---:|---:|---:|
| 6 | 2 | 0.26794919 | 0.26794919 | −1.31695790 |
| 10 | 4 | 0.31084697 | 0.50952545 | −0.92136502 |
| 22 | 10 | 0.32877862 | 0.74859062 | −0.52755168 |
| 102 | 50 | 0.33312248 | 0.94022239 | −0.16693244 |
| 1002 | 500 | 0.33333115 | 0.99374893 | −0.02583268 |

Thus the strongest Lyapunov exponent converges to \(-\log3\) per boundary iteration. The average in the table weights each orbit equally.

**Uniformly launched rays.** Choose a point with uniform polygon-boundary arclength and let \(\ell_N\) be its asymptotic log contraction per application of \(b\), at the same frequency. Up to a null set the ray converges to one of the cycles. Its basin-weighted mean and limiting distribution are

\[
 \mathbb E\ell_N=\frac{2\log\tan(h/2)+\log m_{\min}}{N/2},
 \qquad
 -N\ell_N\Longrightarrow \frac{2\pi}{\sin(\pi U)},
 \quad U\sim {\rm Uniform}(0,1).
\]

In particular the median of \(-\ell_N\) is asymptotic to \(2\sqrt2\pi/N\). The limiting positive random variable has tail probability asymptotic to \(4/y\) at threshold \(y\). This explains how a logarithm enters the mean while most rays experience contraction on the \(1/N\) scale.

## The resonance grid and its proof

**Theorem.** Put \(\theta=k\pi/(2N)\) with \(1\leq k<N\), \(g=\gcd(k,N)\), and \(k/N=p/q\) in lowest terms. Set \(\eta=\pi/2+\theta\). Assume \(\eta\notin\phi+h\mathbb Z\), so neither propagation direction is parallel to a wall and every grid impact is inside a wall. There are \(2g-2\) explicit period-\(q\) cycles on the rays

\[
 t_j=\eta+jh,\qquad j\bmod 2N .
\]

For odd \(q\), every one of these cycles belongs to an open interval fixed by \(b^q\). For even \(q=2r\), \(g-1\) of these cycles attract and \(g-1\) repel. Their attracting **full-period** multipliers are

\[
 M_j=\left[\frac{\tan(r(jh-d_j))}{\tan(r(jh+d_j))}\right]^2,
 \quad 1\leq j<g,
 \qquad \prod_{j=1}^{g-1} M_j
       =[\tan(r d_0)\tan(r d_g)]^2 ,
\]

where \(d_j\) is the absolute angle between \(t_j\) and its edge's outward normal. In particular \(0<d_j<h\), and \(d_j+d_{j+1}=h\). The Lyapunov exponent per application of \(b\) is \(q^{-1}\log M_j\). Every listed hyperbolic orbit persists over an open frequency interval. For \(q>2\) the theorem counts the constructed grid cycles. It gives lower bounds for the full cycle counts.

**Proof.** Two rays whose arguments differ by an integer multiple of \(2h\) have equal polygonal radius. Reflecting \(t_j\) across \(\eta\) gives \(\eta-jh\), a ray of the same radius. The chord between the two points has the first flight direction. Reflecting the intermediary across \(\eta-kh=\pi/2-\theta\) gives \(t_{j-2k}\), again at the same radius. Convexity guarantees these are the two flight endpoints whenever distinct.

The formal index action \(j\mapsto j-2k\bmod 2N\) has \(2g\) cycles of length \(q\). A step repeats a point at its first or second reflection precisely when its starting index is \(0\) or \(k\bmod N\). Among the orbit residues modulo \(2g\), these indices and their translates by \(N\) comprise precisely \(0,g\), because \(p,q\) are coprime. Removing these two cycles leaves the claimed \(2g-2\). For \(g=1\) the construction certifies no cycle.

Let \(\delta_j\) be the signed normal offset at \(t_j\), so \(d_j=|\delta_j|\). Every actual impact in one constructed orbit is a polygon rotation of the initial impact and has the same offset. The absolute derivative of a flight between two edges is the ratio of the absolute tangential derivatives of its conserved linear form. With \(A(u)=|\sin(uh+\delta_j)/\sin(uh-\delta_j)|\), this gives

\[
 (b^q)'(t_j)=\prod_{\ell=0}^{q-1}
    \frac{A(j-2k\ell)}{A(j-(2\ell+1)k)} .
\]

The derivative denotes the return derivative in boundary length. Changing the local coordinate leaves a periodic multiplier invariant. \(A\) has period \(N\). For odd \(q\), multiplication by two permutes the residue classes modulo \(q\), so the factors cancel. A return fixing an edge-interior point with derivative one is the identity on a neighborhood since its whole itinerary is affine there.

For \(q=2r\), the numerator visits \(r\) sine arguments modulo \(\pi\), each twice, with spacing up to permutation equal to \(\pi/r\). Applying \(\prod_{\ell=0}^{r-1}|\sin(x+\ell\pi/r)|=2^{1-r}|\sin(rx)|\) and \(rkh=p\pi/2\) gives

\[
 (b^q)'(t_j)=
 \left|\frac{\tan(r(jh+\delta_j))}{\tan(r(jh-\delta_j))}\right|^2 .
\]

The indices \(j\) and \(2g-j\) have the same offset and reciprocal derivatives. For \(1\le j<g\), the two positive angles \(r(jh\pm d_j)\) lie strictly between \(0\) and \(\pi/2\). Exactly one derivative contracts. Consecutive normal offsets have complementary absolute values since the grid spacing is half an edge angle. Each numerator at \(j+1\) therefore cancels the denominator at \(j\) in the product formula. Hyperbolic persistence follows directly by solving the affine fixed-point equation on the same itinerary under a small angle perturbation.

**Why the \(q=2\) list is exhaustive.** Every even regular polygon is centrally symmetric. Its half-turn \(C\) commutes with \(b\). If \(b\) has rotation number \(1/2\), then \(Cb\) has rotation number zero, by commuting the half-period lift with the lift of \(b\). An orientation-preserving circle homeomorphism with a fixed point has no longer periodic orbits. Hence \(\mathrm{Fix}(b^2)=\mathrm{Fix}(Cb)\), so every period-two orbit has \(b(p)=-p\). Solving the two line equations forces the intermediate point to be \(-S_s p\), where

\[
 S_s(x,z)=(z/s,sx).
\]

At \(s=1\), this is the coordinate swap. If \(\pi/4\notin\phi+h\mathbb Z\), the regular polygon and its reflected image have the same radius only on \(t=\pi/4+jh\). Indeed the radial function is \(\cos h/\cos(\operatorname{wrap}_{2h}(t-\phi-h))\), where wrap takes values in \([-h,h)\). Equality at \(t\) and \(\pi/2-t\) gives either \(2t=\pi/2\bmod 2h\) or the excluded mirror orientation. On the four rays \(t=\pi/4\bmod\pi/2\), a reflected endpoint would coincide with its starting point. These ray intersections lie in wall interiors and the required characteristic there is transverse, so they give no orbit. The other \(2N-4\) intersections give exactly \(N-2\) period-two orbits, equally split between attracting and repelling ones. The two boundary orbit directions around an inscribed four-flight parallelogram describe a reciprocal pair.

For \(N=4m+2,\phi=0\), all \(d_j=h/2\), and the identity \(\tan(x-y)/\tan(x+y)=(\sin(2x)-\sin(2y))/(\sin(2x)+\sin(2y))\) now gives the opening formulas. The minimum occurs at \(j=1,N/2-1\). The maximum occurs at the two integers closest to \(N/4\).

For the launch distribution, pass to the antipodal boundary quotient. Its \(N-2\) fixed points alternate between attraction and repulsion, as follows from their strict crossing derivatives. They occupy all \(N\) grid rays modulo \(\pi\) except for the two perpendicular grazing rays. The open basin of an attractor lies between its two neighboring repellers. Away from the two omitted rays it spans angle \(2h\) and has exactly one edge length by rotational symmetry. Each omitted ray lengthens the basin adjacent to it. The attracting point in each such basin lies one grid spacing from that ray, hence has the extremal factor associated with \(j=1\) or \(N/2-1\). The two wider basins together account for one extra edge length, since the full quotient perimeter is \(N/2\) edges and there are \(N/2-1\) attractors. This proves the mean formula using the telescoping product. Piecewise-affine derivatives of rays in each basin eventually agree with those of its attracting cycle, apart from the countably many preimages of breaks.

The arclength law of the cycle index differs in total variation from the uniform law on \(1,\ldots,N/2-1\) by \(O(1/N)\). Under uniform sampling the mesh \(x_j=2j/N\) converges in law to a uniform point. On every compact subinterval of \(0<x_j<1\), the exact factors give \(-N\log m_j=2\pi/\sin(\pi x_j)+o(1)\) uniformly. Truncating the two ends of the mesh proves weak convergence. The tail of the limiting variable equals \((2/\pi)\arcsin(2\pi/y)\) for \(y\ge2\pi\), which yields the stated median and tail.

**Infinitesimal rotation.** At \(N=8,\phi=0,\theta=\pi/4\), both normals lie on opposite-vertex axes, so \(b=C\) on the whole boundary. For any sufficiently small nonzero vertex rotation three attractors and three repellers replace that neutral half-turn. The \(j=2\) contracting factor per iteration tends to \((1-\sin(\pi/4))/(1+\sin(\pi/4))=3-2\sqrt2\), while the other two tend to one. The limiting regular octagon has a noncharacteristic wall configuration. Derivatives at impacts approaching its vertices account for the discontinuity.

## Which frequencies survive exactly

**Mirror construction.** For every \(\theta=\pi p/(2q)\), \(0<p<q\), take \(N=4mq,\phi=0\). Each normal \(\pi/2\pm\theta\) is an opposite-vertex axis, since dividing either angle by \(2\pi/N\) gives \(m(q\pm p)\). Reflection in that axis exchanges the endpoints of every chord in its direction family. Consequently \(b\) is the actual Euclidean rotation through \(-2\pi p/q\), and \(b^q\) is globally the identity. There are no parallel walls for these two directions. Applying the neutral-interval trace construction yields an infinite-dimensional finite-energy eigenspace at \(\lambda^2=\cos^2\theta\). Along \(N=4m!\) every fixed interior disk eigenfrequency eventually survives exactly. For odd \(q\) the nongrazing grid result already gives neutral intervals on *any* generic orientation when \(q\mid N\) and \(N/q\ge2\).

This leaves total Lebesgue measure of periodic-attractor frequencies on general regular polygons open. The disk point spectrum itself is countable. Infinite multiplicity or retention of a dense list of disk frequencies does not supply a positive-measure frequency set.

## A disappearing eigenvalue with a quantitative spectral limit

Take the same horizontal vertex orientation for every \(N\). When \(8\mid N\), the mirror construction makes spectral value \(1/2\) an eigenvalue of infinite multiplicity. When \(N=4m+2\), \(b^2\) has only finitely many fixed points at \(\theta=\pi/4\), so the finite-energy trace criterion gives
\(\ker(T_N-\tfrac12)=0\). Here \(T_N=\Delta_D^{-1}\partial_z^2\) acts in the Dirichlet energy space. Both sequences of tables converge to the same disk. There is a quantitative sense in which a smooth disk mode is recovered even in the sequence with no such eigenvalue.

Let \(R(t)\) be the polygon radius at argument \(t\), \(a=\cos h\), and \(g(t)=1-R(t)^2\). The disk polynomial \(u=1-x^2-z^2\) solves \(u_{zz}=u_{xx}\). On the polygon put

\[
 E_N(r,t)=g(t)\left(\frac r{R(t)}\right)^N,\qquad w_N=u-E_N .
\]

The piecewise smooth angular function is continuous at each vertex, and the power of \(r\) removes the origin singularity. Thus \(w_N\in H^1_0(P_N)\), and it agrees with the disk quadratic up to an explicit correction concentrated near the walls. For every Dirichlet test function \(v\), integration by parts using the polynomial equation gives

\[
 |\langle (T_N-\tfrac12)w_N,v\rangle_{H^1_0}|
 =\tfrac12\left|\int_{P_N}
     (\partial_x E_N\,\partial_x\bar v-\partial_z E_N\,\partial_z\bar v)\right|
 \le\tfrac12\|\nabla E_N\|_2\|\nabla v\|_2 .
\]

Integrating first in \(r\), using \(g'=-2R^2(\log R)'\), gives the exact correction energy

\[
 \|\nabla E_N\|_2^2=\frac1{2N}\int_0^{2\pi}
     \left[N^2g^2+\{2+(N-2)g\}^2\{(\log R)'\}^2\right]\,dt.
\]

Since \(0\leq g\leq\sin^2h\) and \(|(\log R)'|\leq\tan h\), put

\[
 D_N^2=\frac{N^2\sin^4h+(2+(N-2)\sin^2h)^2\tan^2h}{2N}.
\]

Then \(\|\nabla E_N\|_2\leq\sqrt{2\pi}D_N\). The incircle gives \(\|\nabla u\|_{L^2(P_N)}\ge\sqrt{2\pi}\,a^2\). Whenever \(a^2>D_N\),

\[
 \frac{\|(T_N-\tfrac12)w_N\|_{H^1_0}}{\|w_N\|_{H^1_0}}
 \leq\frac{D_N}{2(a^2-D_N)}
 =O(N^{-3/2}).
\]

For the normalized spectral measure of \(w_N\), the mass a distance at least \(\delta>0\) from \(1/2\) is bounded by the square of this residual divided by \(\delta^2\). It is \(O_\delta(N^{-3})\). This compares prepared modes on different polygons to one specific disk eigenfunction. The two-sided spectral type outside this single energy and the sharp residual constant are separate questions.

For \(N=102\) the relative residual bound is \(0.00410815\). For \(N=1002\) it is \(0.000130638\), at an energy where the table has 500 attracting period-two boundary orbits and a zero eigenspace.

More generally, in \(H^1_0(D)\) use zero extension to identify the polygon space with a closed subspace with orthogonal projection \(\Pi_N\). The common energy forms give \(T_N=\Pi_N T_D|_{H^1_0(P_N)}\). The projections converge strongly to the identity because every compactly supported smooth disk test eventually belongs to all polygon spaces. The extended compressions \(\Pi_N T_D\Pi_N\) therefore converge strongly to \(T_D\), irrespective of nesting or vertex phase.

## Exact corner ranges and circle convergence

**Corner law.** Let

\[
 d(t)=\operatorname{dist}\big(t,\phi+2h\mathbb Z+\pi\mathbb Z\big),
 \quad A=h-d(\pi/2),\quad B=h-d(0).
\]

At a noncharacteristic angle the clockwise rotation number is zero modulo one precisely for \(0<\theta<A\) or \(\pi/2-B<\theta<\pi/2\). Both fixed endpoints of a common chord would determine a line in two different directions, so \(b(p)=p\) forces both separate flights to fix \(p\). Thus both projection normals must lie in the normal cone at one vertex, allowing either normal to change sign. Its half-width is \(h\). The two possible middle directions on the projective normal circle are vertical and horizontal, with respective offsets \(\theta\) and \(\pi/2-\theta\). This proves the range. A fixed corner can attract on just one side. In particular the label “corner trapping” here means the existence of a common support vertex.

The angular fraction is \(2(A+B)/\pi\). For odd \(N\) the vertex grid modulo \(\pi\) has spacing \(h\), and the two axis phases are a half-grid apart. For \(N=2\bmod4\) the grid has spacing \(2h\) and the phases are a half-grid apart. For \(N=0\bmod4\) the phases agree. Therefore

\[
 \text{angular fraction}=
 \begin{cases}3/N& N\ {\rm odd},\\
 2/N& N=2\bmod4,\\
 (4/N)(1-d(0)/h)&4\mid N .
 \end{cases}
 \qquad
 |\{\lambda:\text{corner}\}|=1-\cos A+\sin B.
\]

Physical frequency measure is \(B+\tfrac12 A^2+O(N^{-3})\) uniformly in orientation. For odd \(N\) it is of order \(1/N\). For \(N=2\bmod4\) with \(B=0\), it is \(1-\cos(\pi/N)\sim\pi^2/(2N^2)\). A regular \(4m\)-gon with horizontal and vertical sides has zero corner measure. The finite set of characteristic-wall angles does not affect either measure.

| \(N\), vertex angle \(5^\circ\) | Angular fraction | Physical frequency length |
|---:|---:|---:|
| 3 | 1 | 1 |
| 4 | 8/9 | 0.87674317 |
| 5 | 3/5 | 0.59453322 |
| 6 | 1/3 | 0.42642356 |
| 7 | 3/7 | 0.40188403 |
| 8 | 7/18 | 0.34698885 |
| 10 | 1/5 | 0.22875636 |
| 12 | 2/9 | 0.18884042 |
| 20 | 4/45 | 0.07219242 |

**Uniform shadowing.** Every noncritical polygon rotation number has a lift satisfying

\[
 |\rho_{\rm clockwise}-2\theta/\pi|\le 2/N .
\]

Indeed \(|(\log r)'|\le\tan h\) for the radial function of the inscribed polygon. For a nonzero chord use endpoint angles \(a-d,a+d\) chosen modulo \(2\pi\) with \(0<d\le\pi/2\) and radii \(r_1,r_2\). The angular deviation \(e\) of the chord from the tangent at the radial bisector satisfies

\[
 |\tan e|=\frac{|r_2-r_1|}{r_2+r_1}\cot d
 \le \tfrac12|\log r_2-\log r_1|\cot d
 \le d\,\tan h\,\cot d\le \tan h .
\]

A single chord therefore differs in endpoint angle from its disk reflection by at most \(2h\). The same estimate holds for a supporting vertex by its normal cone. Two flights differ from disk rotation by at most \(4h\) on the lift obtained by composing the individual reflection lifts. Summing these errors per iteration proves the rotation bound. Every fixed \(p/q\) tongue lies within \(\pi/N\) of its disk angle \(\pi p/(2q)\), modulo the endpoint identification for rotation zero. Thus angles of any bounded, fixed range of periods occupy \(O(1/N)\) measure, also in frequency because \(\cos\theta\) is 1-Lipschitz. The estimate permits long periods to cover positive measure.

## Exact half-period tongues

**Quarter-turn symmetry.** If \(4\mid N\), set \(\epsilon=\operatorname{dist}(\pi/4,\phi+h\mathbb Z)\). Then the entire open half-rotation tongue is

\[
                \pi/4-\epsilon<\theta<\pi/4+\epsilon .
\]

Its angular width is \(2\epsilon\le\pi/N\), and its frequency length is \(\sqrt2\sin\epsilon\). Every angle strictly outside the closed interval is excluded. When \(\epsilon=0\), the only possible half-rotation angle is the center. Transverse characteristic directions there yield \(b=C\). For \(0<\epsilon<h/2\), a tongue endpoint determined by a vertex-axis mirror carries a degenerate period-two orbit on an antipodal vertex pair. A side-axis endpoint is characteristic. A tie \(\epsilon=h/2\) yields characteristic endpoints. Throughout the open band away from the finite vertex events the periodic orbits are hyperbolic.

For a square with walls tilted by \(\alpha\in[0,\pi/4]\) from the coordinate axes, \(\epsilon=\min(\alpha,\pi/4-\alpha)\). When \(\alpha\ge\pi/8\), every angle strictly between \(\alpha\) and \(\pi/2-\alpha\) has period two. The complementary open bands have common support corners. For general \(4\mid N\), the angular lengths of the corner and half-period sets sum to \(2(h-d)+2\min(d,h-d)\) with \(d=d(0)\).

**Existence proof.** In the first quadrant take the boundary points with \(xz=H>0\). Write \(x=\sqrt H e^u,\ z=\sqrt H e^{-u}\). The inverse square root of the corresponding boundary value of \(H\) is

\[
 D(u)=\max_i\frac{a_i e^u+b_i e^{-u}}{\cos h},
\]

where \((a_i,b_i)\) ranges over the unit outward normals. This positive function tends to infinity at both ends. On each smooth piece \(D''=D>0\), with upward derivative jumps at a change of maximizing face. Thus \(D\) is strictly convex and has a unique minimum. At each level \(0<H<H_{\max}\) there are exactly two boundary points \((x_1,H/x_1),(x_2,H/x_2)\) there, continuously varying with \(H\). The map \(S_s\) interchanges them for \(s=H/(x_1x_2)\). At \(H\downarrow0\) this slope tends to the ratio of the two axial intercepts, which equals one by quarter-turn symmetry. At the maximum it tends to \(z_*/x_*\).

Let \(\beta\) be a mirror axis nearest \(\pi/4\). If it is a vertex direction, that vertex maximizes \(xz\), since the gradient \((z_*,x_*)\) lies in its support cone by \(|2\beta-\pi/2|\le h\). More explicitly, the superlevel sets of \(xz\) in this quadrant are convex and their supporting tangent there coincides with a supporting line of the table. Equivalently one may maximize the concave function \(\log x+\log z\). If \(\beta\) is a face-normal direction, the point of radial angle \(\pi/2-\beta\) lies on that face by the same bound, and its gradient is its normal. In both cases the terminal slope angle is \(\pi/4\pm\epsilon\). A quarter rotation converts a parallelogram at \(s\) into one at \(1/s\). Continuity now supplies every interior angle, and the grid theorem covers the center when \(\epsilon>0\). There are no characteristic slopes in this open interval.

**Exclusion proof.** The noncritical chord maps admit lifts ordered in the direction angle. At a fixed starting point, the bearing of the chord to a second point varies monotonically as the second point traverses the convex boundary. A supporting vertex can keep the second point fixed over an angle interval. At a flat side the two one-sided limiting endpoints bound that side in boundary order. Reflection in the midpoint chooses a value between them. Use this last convention solely to compare the lifts across an exceptional parameter. As \(\theta\) increases, the two direction angles change in opposite senses, and the second chord map reverses boundary order. Thus \(b_\theta\), and \(Cb_\theta\), have pointwise ordered lifts through the whole range. The rotation number is monotone in the corresponding lift order.

At a positive-width endpoint at least one chord map is reflection in a polygon symmetry axis. Reversing the two flights exchanges \(b\) with \(b^{-1}\), so we may call that reflection the first one. Given \(p\) and its reflected point \(p'\), the segment from \(p'\) to \(-p\), if nonzero, is perpendicular to the first flight. As \(\theta\ne\pi/4\), a half-period orbit would require \(p'=-p\), followed by a supporting second flight. The only candidates are two antipodal radial points along the first flight. At a unique nearest vertex-axis mirror, the second normal lies in the required support cone by \(2\epsilon<h\). A face-midpoint endpoint gives no fixed point of \(Cb\), since the only tangent there is perpendicular to the radius and the required direction differs. At a tie both chord maps are symmetry reflections, and their rigid rotation has angle different from a half-turn.

In the noncritical endpoint case the two candidate zeros are antipodal. The displacement of \(Cb\) has one sign elsewhere, since antipodal equivariance identifies its two complementary arcs and each arc has no zeros. At the center it takes both signs, as the grid supplies attracting and repelling regular roots. Thus on the exterior side of this endpoint monotonicity forces one sign everywhere, and a zero could persist there only at one of the endpoint vertices. For any fixed boundary point \(v=(x,z)\), the necessary condition \(S_s v\in\partial P\) has finitely many positive solutions because at face \((a,b)\) it reads \(bxs^2-(\cos h)s+az=0\). If the half-rotation number occurred at any farther parameter, monotonicity of rotation would force it throughout the intervening interval, contradicting finiteness for those two vertices. A critical endpoint whose midpoint-reflection map has rotation different from \(1/2\) already precludes continuation by monotonicity. Finally when \(\epsilon=0\), both midpoint-extended chord maps at the center are mirror symmetries and \(b=C\). Pointwise monotonicity would force any fixed point at another half-rotation parameter to stay fixed for every intermediate parameter, again violating that quadratic finiteness.

On an open cell of fixed edge itinerary a neutral half-period would give coincident segments of \(\partial P\) and \(S_s\partial P\). Their equal apothems force equality of the corresponding unit normals after applying \(S_s^T\). For \(s\ne1\), the resulting length identity \(s^2b^2+a^2/s^2=a^2+b^2=1\) forces \(a=\pm sb\), a characteristic wall. At \(s=1\) the non-mirror case is covered by the explicit multipliers. This proves generic hyperbolicity inside the band.

**Every \(N\).** For even \(N\) the preceding vertex equation and the characteristic slopes supply all possible changes of the half-period condition. Test each candidate root for membership in the target face segment. At the midpoint of a complementary cell the test becomes intersection of the two polygon boundaries \(\partial P,S_s\partial P\), deleting the intersections with \(S_s p=\pm p\). Such a deleted intersection could give a true grazing orbit only at a supporting vertex, already among the candidate events.

For odd \(N\) retain a general four-flight parallelogram. Let \(v\) be one of its vertices on a polygon vertex. Its adjacent flight endpoints have the form

\[
 v+u(1,s),\qquad v+w(1,-s).
\]

If their target faces have normals \(n_1=(a,b), n_3=(c,d)\), then
\(u=(H_0-n_1\cdot v)/(a+bs),\quad
w=(H_0-n_3\cdot v)/(c-ds)\), where \(H_0=\cos h\). The opposite impact lives on face \(n_2=(e,f)\) precisely when

\[
\begin{split}
0={}&(n_2\cdot v-H_0)(a+bs)(c-ds)\\
 &+(H_0-n_1\cdot v)(e+fs)(c-ds)\\
 &+(H_0-n_3\cdot v)(e-fs)(a+bs).
\end{split}
\]

Every equation has degree at most two. Retain real positive roots with all three impacts on the specified finite faces. Add edge-parallel angles and directions through pairs of vertices to include retraced two-cycles. In a noncritical open parameter cell an isolated regular crossing persists. A loss of all periodic solutions inside such a cell would require a periodic point at a break of \(b^2\), or an affine fixed interval, whose endpoint reaches such a break. Following flights from that break gives a periodic polygon vertex, so the quadratic list exhausts tongue boundaries. For degeneracies of the polynomial, one can partition its identically-zero case by the roots of the edge-membership inequalities. In the four-flight test a nondegenerate configuration starting at a specified vertex with the other three impacts in open faces cannot persist on an interval of \(s\) because the first nonzero flight endpoint moves strictly in direction angle and the ordered compositions preserve that strict inequality. If a second impact is a vertex at an isolated solution, its second incident face or the chord between two neighboring impacts adds the event. Exact root expressions involve elementary trigonometric coefficients and square roots. The implementation orders and displays the candidate angles at 75 digits and samples each numerical open cell at a rational angle between its estimated endpoints. The table gives the hull and total width of those cells. For an event estimate outside them, the test covers the bracket between its two neighboring samples. On a bracket free of characteristic walls, a common supporting vertex or strict displacement of the same sign at both samples excludes period two throughout, by the pointwise ordering of the lifts. The program lists inconclusive event brackets by their estimated angles.

| \(N\), vertex angle \(5^\circ\) | Lower half-period boundary | Upper boundary | Open width |
|---:|---:|---:|---:|
| 3 | — | — | 0° |
| 4 | 40° | 50° | 10° |
| 5 | 44.49603433° | 49° | 4.50396567° |
| 6 | 41.39098538° | 55° | 13.60901462° |
| 7 | 43.57142857° | 45.19304030° | 1.62161172° |
| 8 | 40° | 50° | 10° |
| 10 | 41° | 46.22638492° | 5.22638492° |
| 12 | 40° | 50° | 10° |
| 20 | 41° | 49° | 8° |

**Arbitrary fixed \(q\).** For a convex polygon, a finite system gives exact period-\(q\) inequalities even when a concise list of explicit endpoints is unavailable. For the wall with initial vertex \(V_i\) and edge vector \(E_i\), use \(V_i+tE_i\), \(0<t<1\). Write \(L_\sigma(x,z)=z-\sigma sx\), \(\sigma=\pm1\). For a transition \(i\to j\) the new parameter is

\[
 t'=\frac{L_\sigma(V_i-V_j)+t L_\sigma(E_i)}{L_\sigma(E_j)} .
\]

Enumerate \(2q\) alternating transitions, with \(j\ne i\) at each nondegenerate flight and the last index equal to the first. Each composition gives \(t\mapsto Mt+D\). Test \(t=D/(1-M)\) in every one of the \(2q\) interval conditions. When \(M=1,D=0\) the admissible interval is neutral. Track the lift's integer winding to distinguish \(p/q\) from a proper divisor. At the boundary use closed inequalities and actual supporting-vertex rules for repeated impacts. Denominators and numerators are products or sums of affine functions of \(s\), hence a fixed word gives semialgebraic membership and an exact multiplier. For a polygon with rational vertices and a rational slope, the companion script computes every affine piece of \(b^q\) over the rationals and tests each knot exactly. For rounded or trigonometric data the verifier requires outward intervals or an explicit absolute input radius. It propagates those bounds to the lift and the positions of its subdivision marks. Strictly separated displacement signs certify crossings or exclusion. If a required sign enclosure contains zero, the classification is **unresolved**. A neutral interval or global identity requires exact data or a separate proof such as the mirror symmetry above. A closed measure formula summing tongues of unbounded periods remains open.

The following noncritical angle components were located numerically by bisection on the two extrema of the displacement of the full PL lift. The trigonometric multiplier formula proves the behavior at the central grid value. The rounded endpoints below are numerical diagnostics.

| \(N\) | Vertex phase | Clockwise \(p/q\) | Grid angle | Lower angle | Upper angle |
|---:|---:|---:|---:|---:|---:|
| 9 | 5° | 1/3 | 30° | 30.00000000° | 30.80065099° |
| 16 | 5° | 1/4 | 22.5° | 21.10330970° | 24.52695413° |
| 15 | 5° | 2/5 | 36° | 36.00000000° | 36.16579012° |
| 24 | 3° | 1/6 | 15° | 14.51472955° | 15.75063608° |

## Checks and historical scope

From the study directory with mpmath installed, run the following commands.

    python3 experiments/phase1_regular.py --tongues
    python3 experiments/phase1_regular.py --resonance 16 4 5 --tongues
    python3 experiments/phase1_regular.py --resonance 9 3 5 --tongues

The first command checks return multipliers on the actual full piecewise-affine map, separately from the trigonometric grid product, and computes the quadratic event table. The other commands inspect a period-four and a period-three example. When \(\gcd(k,N)=1\), the grid supplies no orbit. The program reports a candidate period until it finds an orbit at the required winding. It tests alignment in rational degree units and encloses the polygon and ray slope from those angles. A repelling grid orbit is checked with the inverse return. The bisection resolves the distance to grid alignment at the active working precision and reports the width in degrees. At \(N=16,k=4,\phi=5^\circ\) the six constructed cycles account for all 24 interior fixed points of \(b^4\), with three attracting cycles. At \(N=9,k=3,\phi=5^\circ\), there are four certified grid cycles with local neutral intervals. The floating census at that grid is unresolved. Neutrality there follows from the odd-period grid formula. The count of affinity pieces of \(b^q\) on which the displacement vanishes depends on the subdivision, so one should count maximal cylinders separately.

The disk rotation law, the common support criterion, and the general \(3N-4\) bound for periodic cylinders already appear as Propositions 3, 5 and 11 of Nogueira and Troubetzkoy. The elementary normal-cone count here evaluates their criterion for regular polygons. Aleksandryan established the disk polynomial basis and constructed arbitrarily near-disk domains with non-almost-periodic solutions (already cited by Zelenyak on p. 1225 of his 1965 note on finite-time boundary dependence). [Nogueira and Troubetzkoy](https://arxiv.org/abs/2007.14773), [Aleksandryan](https://www.mathnet.ru/eng/mmo111), [Zelenyak](https://www.mathnet.ru/eng/dan31716).

Maas and Lam developed geometric focusing. Manders, Duistermaat and Maas computed perturbative tongues for smooth near-circular basins. Ogilvie analyzed the focusing product in a four-flight quadrilateral and treated a tilted square. Bajars, Frank and Maas exhibited tilted-square families over frequency bands. Lenci, Bonanno and Cristadoro's parity result refers to their trapezoidal section and angle family. None of the inspected sources states the regular-polygon resonance grid, its exact multiplicity and product, or the \(N=4m+2\) limit above. Priority remains subject to a wider literature search. [Maas and Lam](https://www.staff.science.uu.nl/~maas0131/files/maas_lam_jfm95.pdf), [Manders, Duistermaat and Maas](https://www.staff.science.uu.nl/~maas0131/files/mandersDuistermaatMaas03.pdf), [Ogilvie](https://arxiv.org/abs/astro-ph/0506450), [Bajars, Frank and Maas](https://doi.org/10.1017/jfm.2012.479), [Lenci, Bonanno and Cristadoro](https://arxiv.org/abs/2102.01654).
