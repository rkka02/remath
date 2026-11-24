# How many frequencies can have short periods in a regular polygon?

Let \(P_N\) be a unit-circumradius regular polygon with arbitrary vertex phase, \(N\ge5\), and put \(h=\pi/N\). The rays have slopes \(+\tan\theta,-\tan\theta\), in that order, with \(0<\theta<\pi/2\) and physical frequency \(\lambda=\cos\theta\). One boundary iteration consists of both flights. Use clockwise rotation numbers \(p/q\) in lowest terms.

**Theorem.** Uniformly in the vertex phase, the angular measure of parameters with a periodic orbit of primitive period at most \(Q\) satisfies

\[
 |\mathcal R_{N,Q}|
 \ \le\ 2h+200hQ+200h^2Q^2\log(2Q)
 \qquad
 \left(1\le Q\le\frac{1}{1000h\sqrt{\log(2/h)}}\right).
\]

The same bound holds in physical frequency. In particular, for every \(Q_N=o(N/\sqrt{\log N})\) tending to infinity, the frequency measure of all periods up to \(Q_N\) tends to zero. The estimate includes attracting, repelling, neutral and vertex cycles. It also bounds the frequency measure of regular attracting cycles with these periods. Edge-parallel parameters form a finite set.

### The angular error of one chord

Let \(r(t)\) be the radial function and let \(\eta\) be a normal to a chord direction. For the unit disk the other endpoint has polar angle \(2\eta-t\). Write \(d(t,\eta)=\operatorname{dist}(t-\eta,\pi\mathbb Z)\) and \(\psi(d)=h^2/(h+d)\). For the polygon, the endpoint lift \(G_\eta(t)\) satisfies

\[
 |G_\eta(t)-(2\eta-t)|\le \min\{2h,\ 6\psi(d(t,\eta))\}.
 \tag{1}
\]

To prove this, place the endpoint angles at \(a-D,a+D\) along their shorter arc, with \(0<D\le\pi/2\). In radial and tangential coordinates at \(a\), the chord has components \((r_2-r_1)\cos D,(r_2+r_1)\sin D\). Thus \(u=\operatorname{dist}(a-\eta,\pi\mathbb Z)\) obeys

\[
 \tan u=\frac{|r_2-r_1|}{r_2+r_1}\cot D
 \le \min\left\{\tfrac12|\log r_2-\log r_1|,\ \tan^2(h/2)\right\}\cot D .
\]

Here \(\cos h\le r\le1\) and \(\log r\) is \(\tan h\)-Lipschitz, by the face formula \(r(t)=\cos h/\cos(t-\nu)\) with face normal angle \(\nu\). The first bound gives \(u\le h\) since \(D\cot D\le1\). The angular error is \(2u\). If \(d(t,\eta)\ge2h\), then \(D\ge d(t,\eta)-h\ge d(t,\eta)/2\), so \(2u\le4h^2/d(t,\eta)\le6\psi(d(t,\eta))\). Otherwise \(2h\le6\psi(d(t,\eta))\). A zero-length chord is at a supporting point, where \(d(t,\eta)\le h\) by the normal cone. This proves (1) in that case as well.

The two normals are \(\eta_\pm=\pi/2\pm\theta\). In counterclockwise polar coordinates the two-flight lift has the form

\[
 F_\theta(t)=t-4\theta+e_\theta(t),\qquad
 |e_\theta(t)|\le 6\psi(d(t,\pi/2+\theta))
                  +18\psi(d(t,\pi/2+3\theta)).
 \tag{2}
\]

Indeed the ideal second launch is \(2\eta_+-t\) and the true launch differs by at most \(2h\). A shift by \(2h\) increases \(\psi\) by a factor of at most three. Reflecting the second normal through the first gives \(2\eta_+-\eta_-=\pi/2+3\theta\).

### Summing the error on a rational grid

Fix \(0<p<q\) and \((p,q)=1\). Set \(\theta_0=\pi p/(2q)\), \(y_j=x-2\pi jp/q\) and \(x_j=F_\theta^j(x)\). Modulo \(\pi\), the \(q\) reference points \(y_0,\ldots,y_{q-1}\) have spacing at least \(\pi/q\) and multiplicity at most two. Suppose \(|x_j-y_j|\le1/q\) at the beginnings of the steps in a prefix of these \(q\) steps. For any axis \(\eta\), at most four reference points satisfy \(d(y_j,\eta)<2/q\), contributing at most \(4h\) to the sum of \(\psi(d(x_j,\eta))\).

Each shell \(\ell/q\le d(y_j,\eta)<(\ell+1)/q\), \(2\le\ell\le2q\), contains at most four reference points, counting the two sides of the axis and the possible multiplicity. Each actual distance there is at least \(\ell/(2q)\). Summing the reciprocal distances gives

\[
 \sum_{\text{prefix}}\psi(d(x_j,\eta))
 \le 4h+8qh^2\log(2q),\qquad
 \sum_{\text{prefix}}|e_\theta(x_j)|\le B_q,\quad
 B_q=200\big(h+qh^2\log(2q)\big).
 \tag{3}
\]

Evaluate the return at \(\theta_\pm=\theta_0\pm B_q/(2q)\) under the condition \(3qB_q<1\). Both angles are interior since the center's distance from either endpoint of the angular window is at least \(\pi/(2q)\). The disk's \(q\)-step displacement relative to the grid is \(\mp2B_q\). Induction applies (3) at each step since the total detuning over any prefix is at most \(2B_q\), and so \(|x_j-y_j|\le3B_q<1/q\) throughout. Consequently

\[
 F_{\theta_+}^q(x)-x+2\pi p\le-B_q,\qquad
 F_{\theta_-}^q(x)-x+2\pi p\ge B_q
 \quad\text{for every }x .
 \tag{4}
\]

### Ordering across characteristic directions

Use for \(G_\eta\) the lift within \(2h<\pi\) of \(2\eta-t\) from (1). At a characteristic support edge, pair its points by reflection in the edge midpoint. This extends the chord pairing from the two neighboring boundary arcs to a decreasing circle homeomorphism at that angle. Equations (1) and (2) still hold since the paired endpoints lie on the same support line.

For fixed \(t\), \(G_\eta(t)\) is nondecreasing in \(\eta\). Indeed as a target moves counterclockwise on a convex boundary from a fixed starting point, its chord bearing moves counterclockwise. Directions supporting a vertex return that vertex. When the chord is an incident flat edge, its two limiting targets enclose the edge, and the midpoint pairing selects a target between them. This order is consistent on the real lifts because \(G_{\eta+\pi}(t)=G_\eta(t)+2\pi\) in the normalization (1). Since each \(G_\eta\) reverses boundary order, \(F_\theta=G_{\eta_-}\circ G_{\eta_+}\) is nonincreasing in \(\theta\) at every input. Its iterates preserve this parameter ordering because \(F_\theta\) preserves boundary order.

It follows from (4) that every parameter with clockwise rotation \(p/q\) satisfies

\[
 \left|\theta-\frac{\pi p}{2q}\right|\le\frac{B_q}{2q}.
 \tag{5}
\]

For \(q\le1/(1000h\sqrt{\log(2/h)})\), we have \(\log(2/h)>1\), \(q\le1/h\), and \(3qB_q\le600(10^{-3}+10^{-6})<1\). Summing (5) over the \(\varphi(q)\le q\) reduced numerators for each \(2\le q\le Q\) gives the bound in the theorem. For period one, a fixed point and \(|F_\theta(t)-t+4\theta|\le4h\) put \(\theta\) within \(h\) of either \(0\) or \(\pi/2\), adding at most \(2h\). Finally, \(|d\lambda|=\sin\theta\,d\theta\le d\theta\).

### Which rational-rotation frequencies can lack a regular attractor?

**Proposition.** For any fixed convex polygon with \(N\) vertices and each reduced \(0<p/q<1\), at most \(N\) transverse parameters of that rotation can have a periodic trajectory through a vertex. At all other transverse parameters of the same rotation, every periodic cycle is regular and hyperbolic, and there is an attracting cycle. Thus outside the common-support corner ranges, the frequencies without a regular periodic attractor agree with the irrational-rotation set up to a countable set.

The ordering argument uses only convexity. For an arbitrary polygon, choose decreasing chord lifts in any positively oriented boundary coordinate of period \(2\pi\), ordered in the normal angle and satisfying \(G_{\eta+\pi}=G_\eta+2\pi\). Every such lift squares to the identity because it has a real fixed point and its square covers the identity. Consequently \(F_0(t)=t\) and \(F_{\pi/2}(t)=t-2\pi\), fixing the clockwise lift convention throughout. If \(0<\theta_1<\theta_2<\pi/2\), equality \(F_{\theta_1}(t)=F_{\theta_2}(t)\) in the ordering above forces the two first-flight targets to coincide, by strict decrease in the input of the second chord map. The two second-flight targets then also coincide. Two different directions from a boundary point have the same target only when that target is the starting point. Both flights therefore fix \(t\), giving rotation zero. At transverse parameters of rotation \(p/q\ne0\), the two lifts are consequently strictly ordered everywhere, as are their \(q\)th powers. For each vertex \(v\), the equation \(F_\theta^q(v)=v-2\pi p\) has at most one such solution. A vertex met halfway through a two-flight step also lies on a periodic orbit of the boundary map since the first chord involution conjugates that map to its inverse.

In arclength coordinates, the \(q\)-fold return is piecewise affine. Every breakpoint has a flight itinerary meeting a vertex, since between open transverse edges each chord correspondence is affine. A proper fixed interval must end at such a breakpoint, and global finite order makes every vertex periodic. After the vertex parameters are removed, the fixed points of the \(q\)-fold return are therefore finitely many simple zeros of its displacement, all on regular itineraries. The affine displacement changes sign at each zero. Its positive-to-negative crossings give the attracting cycles.

### A sharp fixed-period example and the full-measure question

For \(4\mid N\), choose the vertex phase so that the nearest mirror axis is \(h/2\) from \(45^\circ\). The exact open period-two tongue then has angular width \(h\), attaining the order \(1/N\) for a fixed period. For the octagon with vertex phase \(11.25^\circ\), the independent polygon-intersection routine gives endpoints \(33.75^\circ,56.25^\circ\) and physical-frequency width \(\sqrt2\sin(\pi/16)=0.27589937928294301234\ldots\). [Exact half-period band](phase1_regular.md#exact-half-period-tongues) · [Polygon intersection calculation](../experiments/phase1_regular.py)

The measure contributed by all periods above \(Q_N\) remains open for general fixed regular polygons. A known full-measure theorem for two-break circle maps uses Lebesgue measure on the space of maps. The trapezoid calculation uses its special two-break family. On a fixed closed dilation surface, a general theorem gives density of directions admitting closed geodesics. Khmelev's one-parameter theorem requires a dominant break, and its chess-billiard application treats a convex boundary with one corner. For the physical polygonal family the two directions, the break locations, and the branch slopes vary together. None of these cited statements supplies its all-period measure. [Ghazouani](https://arxiv.org/abs/1803.10129) · [Lenci, Bonanno and Cristadoro](https://arxiv.org/abs/2102.01654) · [Boulanger, Ghazouani and Tahar](https://doi.org/10.2140/gt.2025.29.2217) · [Khmelev](https://doi.org/10.1017/S0143385704000628) · [Nogueira and Troubetzkoy, §4.4](https://arxiv.org/abs/2007.14773)
