# Finite-energy standing waves on polygons

## The boundary criterion

Let \(K=\overline{\Omega}\) be a convex polygon with nonempty interior. The streamfunction operator is \(T=\Delta_D^{-1}\partial_z^2\) on \(H_0^1(\Omega)\) with the Dirichlet energy inner product. The Dirichlet Laplacian \(\Delta_D:H_0^1(\Omega)\to H^{-1}(\Omega)\) intertwines it with \(P=\partial_z^2\Delta_D^{-1}\) on \(H^{-1}(\Omega)\) via \(P\Delta_D=\Delta_D T\). Pointwise observations use the continuous representative of the streamfunction eigenmode \(u\) constructed below. For \(0<\lambda<1\), put

\[
 s=\frac{\sqrt{1-\lambda^2}}{\lambda},\qquad
 \xi=z+sx,\qquad \eta=z-sx.
\]

Substitution transforms \((1-\lambda^2)u_{zz}-\lambda^2u_{xx}=0\) into \(u_{\xi\eta}=0\). Thus \(\theta=\arctan s\) is the angle of a ray to the horizontal and \(\lambda=\cos\theta\). Both endpoint eigenspaces are zero. Indeed \(\langle Tu,u\rangle=\|u_z\|_2^2\) and \(\langle (I-T)u,u\rangle=\|u_x\|_2^2\). Extending \(u\) by zero and slicing on coordinate lines shows that either derivative can vanish identically only for \(u=0\).

Write \(r_\xi,r_\eta\) for the boundary involutions preserving the indicated projection. At a unique extremal vertex the corresponding involution fixes the vertex. On a whole characteristic supporting side use reflection in its midpoint, which makes the map an orientation-reversing, piecewise affine circle homeomorphism. Merge collinear subdivisions when specifying these sides. Set \(b=r_\xi r_\eta\).

**Theorem 1.** The eigenspace at \(\lambda^2\) is naturally isomorphic to the following space modulo constants:

\[
 \left\{h\in H^1(\partial K):
 h\circ r_\xi=h\circ r_\eta=h,\quad
 h\text{ is constant on each characteristic side}\right\}.
\]

If \(h=A\circ\xi=B\circ\eta\) on the boundary, its mode is \(u=A(\xi)-B(\eta)\). Both profiles belong to ordinary \(H^1\) on their full bounded projection intervals. In particular \(h\) is a continuous boundary *profile*. The actual Dirichlet trace of \(u\) is zero.

**Proof.** In characteristic coordinates slice the distribution \(\partial_\eta u_\xi=0\) on each interior rectangle. The \(L^2\) function \(u_\xi\) depends only on \(\xi\) there. Countably many interior rectangles and connectedness of each vertical slice identify the local functions on the entire slice almost everywhere. The same argument works for \(u_\eta\). Taking one-variable primitives and using connectedness gives

\[
 u=A(\xi)-B(\eta),\qquad A,B\in H^1_{\rm loc}.
\]

Writing \(w_\xi(t)\) and \(w_\eta(t)\) for the corresponding section lengths in characteristic coordinates, the energy bounds

\[
 \int w_\xi(t)|A'(t)|^2\,dt+\int w_\eta(t)|B'(t)|^2\,dt<\infty.
\]

An invertible linear change of coordinates only changes the constants in this estimate. The zero boundary trace gives \(A(\xi)=B(\eta)\) pointwise on the relative interiors of transverse sides, away from extreme coordinate values. This follows by continuity of the local representatives up to each such open side.

Three observations handle the ends of the projection intervals.

1. When \(\xi\) is constant along a supporting side of positive length, the nearby parallel sections have lengths bounded below. Thus \(A\) belongs to ordinary \(H^1\) up to that endpoint. The zero trace on this side gives \(B(\eta)=A(\xi_{\rm end})\) on its relative interior.
2. Suppose the \(\xi\)-extreme is a single vertex \(v\), and \(B\) is already \(H^1\) near \(\eta(v)\). A transverse incident side identifies \(A\) with \(B\) under an affine change of variable with nonzero slope. At least one such side exists. This case includes an interior value of \(\eta\), and an extreme attained on a side, by the previous observation.
3. It remains to consider a vertex that uniquely realizes extremes of both projections. Translate it to the origin and reverse coordinate signs if needed. The incident sides have equations \(\eta=a\xi\) and \(\eta=d\xi\), with \(0<a<d\). Hence \(B(at)=B(dt)\) for all small \(t>0\). Put \(k=a/d<1\). Near zero, \(w_\eta(y)=(1/a-1/d)y\). Differentiating \(B(ky)=B(y)\) locally shows that each shell \([k^{j+1}c,k^jc]\) contributes the same integral of \(y|B'(y)|^2\). Finite energy makes each contribution zero. Thus \(B\), and then \(A\), is constant near this corner. This use of the boundary conditions is essential. The weight \(y\) alone permits a divergent profile such as \(\log\log(1/y)\).

Interchanging the coordinates gives the assertion at every endpoint. The two boundary representatives therefore agree everywhere and give \(h\in H^1(\partial K)\). Conversely, the involutions and the constancy condition identify every fiber of each projection on the boundary, providing \(A,B\). Along either monotone boundary chain for a given projection, composition with its piecewise affine inverse gives an \(H^1\) profile on the entire interval. The resulting \(u\) has finite energy, solves the PDE, and vanishes on the boundary. Its vanishing throughout the polygon is equivalent to \(A,B\) being the same constant. \(\square\)

## Which periodic intervals support modes?

Let \(E\) be the union of the closed characteristic sides. If \(C\) is an open interval with \(b^q|_C=\mathrm{Id}\), its full reflected orbit consists of the intervals \(b^jC\) and \(r_\eta b^j C\), \(0\le j<q\).

**Theorem 2.** An eigenfunction exists if and only if some such \(C\) can be chosen with its full reflected orbit disjoint from \(E\). Away from characteristic sides this is simply the existence of an open interval of periodic points. Each qualifying interval supports an infinite-dimensional family of \(C^\infty(\overline{\Omega})\) modes. Its members vanish outside the union of the characteristic strips swept out by their reflected boundary data.

**Necessity.** A nonconstant continuous invariant of an orientation-preserving circle homeomorphism forces a periodic point. For a real invariant choose a component of a strict superlevel set on which the oscillation exceeds some \(\delta>0\). All its images have the same oscillation. Uniform continuity bounds their lengths below, so some image repeats and the two endpoints are periodic. Apply this argument to a real part of a complex invariant after multiplying by a constant phase if necessary.

Take an iterate \(b^q\) with fixed points. Its fixed set is a finite union of points and closed intervals because \(b^q\) is piecewise affine with finitely many pieces. On each complementary interval the iterates tend monotonically to an endpoint, so continuity and invariance make \(h\) constant on that closed gap. Thus variation is possible only on the interiors of periodic intervals. There the dihedral orbit has at most \(2q\) sheets. The intersection with the translates of \(E\) is a finite union of closed intervals and points because powers reduce modulo \(q\) on the periodic set. Each such translated side carries a constant value. If \(h\) varies, a subinterval remains outside these translates.

**Construction.** Within a qualifying \(C\) choose a point whose full orbit avoids all polygon corners and all breakpoints of the finitely many sheet maps. Use the least period on the periodic set. Remove the finitely many fixed points of \(r_\eta b^j\), which are orientation-reversing involutions. A sufficiently short interval \(J\) about the chosen point then has \(2q\) disjoint affine sheets. Transport any \(f\in C_c^\infty(J)\) with identical values to all of them and extend by zero. The resulting \(h\) satisfies both reflection identities. Its profiles are smooth compactly supported away from the ends of their coordinate intervals. Their difference is the required mode, and \(f\mapsto u\) is injective. In particular an irrational rotation number excludes every finite-energy mode. A rational rotation number with only finitely many periodic points has the same conclusion. Attraction of the complementary orbits, by itself, leaves open the possibility of a neutral interval.

**Critical example.** In characteristic coordinates a diamond tank at its edge-parallel angle becomes a rectangle. The midpoint extensions give \(b^2=\mathrm{Id}\) everywhere. The whole boundary consists of characteristic sides, so no admissible interval exists. The same conclusion follows directly from \(A(\xi)-B(\eta)=0\) along the four sides.

## A common extremum excludes every mode

**Theorem 3.** If the characteristic-coordinate polygon contains any corner of its axis-aligned bounding box, its eigenspace at that frequency is zero. A single shared extremum suffices, and either supporting face can be a whole side.

**Proof.** Arrange that the shared corner is \((0,0)\) and \(K\subset[0,X]\times[0,Y]\). Write

\[
 l(t)=\min\{y:(t,y)\in K\},\quad
 M(t)=\max\{y:(t,y)\in K\},\quad
 m(y)=\min\{t:(t,y)\in K\}.
\]

These functions are continuous and piecewise affine. The function \(l\) is nonnegative and convex with \(l(0)=0\), hence nondecreasing. For \(0<t<X\), the section has positive length. Taking \(t'<t\) sufficiently close gives \(l(t')\le l(t)<M(t')\). Thus \(T(t)=m(l(t))<t\). By the boundary relations \(A(t)=B(l(t))=A(T(t))\). Iteration decreases to the only possible limiting fixed point, zero, proving \(A(t)=A(0)\). Continuity gives the endpoints and all values of \(B\). \(\square\)

* **Triangles.** For each coordinate, at least two of the three vertices realize a minimum or maximum. The two sets intersect. Theorem 3 applies at every slope, including critical slopes in the square cut along its diagonal. A period two or three for the auxiliary boundary map at an exceptional direction can therefore carry no regular standing-wave beam.
* **Quadrilaterals.** A common extremum at each noncritical slope implies the same weak condition at the finitely many critical slopes, by passing to a subsequence with the same vertex and the same choices of maximum and minimum. This proves the assertion for the quadrilaterals specified by the common-extremum hypothesis. For \(|x|/a+|z|/b\le1\), the upper and lower vertices supply the extrema when \(s<b/a\), the right and left vertices do so when \(s>b/a\), and the critical case is a characteristic rectangle. Shape labels such as kite or rhombus alone supply no such hypothesis.

The historical all-triangles conclusion is explicitly attributed to Troitskaya in §1.3 of Dyatlov, Wang and Zworski. Her 1999 Theorem 1 gives the related \(W_2^1\) uniqueness at two curves lying inside a characteristic wedge. Her 2017 paper discusses exact solutions and energy concentration at vertices of certain right triangles. The short bounding-box proof above includes the edge-parallel cases explicitly. [Troitskaya, 1999](https://www.mathnet.ru/links/e355d3624dcb24d144f7c3664ee1c6d7/mzm1052.pdf) · [Troitskaya, 2017](https://arxiv.org/abs/1610.06605) · [Dyatlov, Wang and Zworski, §1.3](https://msp.org/apde/2025/18-1/apde-v18-n1-p01-p.pdf)

## How far the attractor-free classification goes

Call a corner trap here a fixed vertex of the noncritical boundary map attracting from one side. At a fixed vertex both characteristic lines must support the polygon, since two distinct points cannot lie on both characteristic lines through a point. The converse holds. In coordinates as in Theorem 1, alternation scales the distance along one edge by \(a/d\) and along the other by \(d/a\), giving one attracting side and one repelling side. This is a statement about geometric rays. Concentration of a forced or time-dependent PDE solution is a separate question. [Nogueira and Troubetzkoy, Proposition 5 and Corollary 7](https://arxiv.org/abs/2007.14773)

**Proposition 4.** A convex polygon has a corner trap at some noncritical slope if and only if one of its four extremal horizontal or vertical support lines touches a single vertex. Indeed the two signed outward normals for a common extremum are chosen from \(\pm(s,1)\) and \(\pm(-s,1)\). Their sum is horizontal or vertical and lies in the interior of the vertex normal cone. Conversely, an axial normal in the interior of a normal cone can be bracketed by the appropriate pair for all sufficiently small or sufficiently large \(s\).

**Theorem 4a.** Among convex polygons with at most five genuine sides, the axis-aligned rectangle is the only table free of geometric attractors at every slope. For an **axis-aligned rectangle** with a proper straight corner cut joining the relative interiors of two adjacent sides, there is an open interval of slopes with a regular period-three attractor. All four axial support edges survive, so every noncritical slope is free of fixed corner traps.

The tilted diamond \(\{|x|+|z|\le1,\ z\le1/2\}\) shows why alignment matters. At \(0<s<1\) the bottom vertex \((0,-1)\) strictly minimizes both \(z+sx\) and \(z-sx\). At \(s>1\) the right vertex \((1,0)\) strictly maximizes the first and strictly minimizes the second. These ranges exhaust the transverse slopes. Each has a common supporting fixed vertex, hence a one-sided corner trap and rotation zero. A circle homeomorphism with a fixed point has only fixed periodic points, so the cut diamond has no period-three tongue.

**Proof.** An axis-aligned rectangle unfolds to straight-line motion on a torus. By Proposition 4 a polygon without a corner trap must retain four axial support edges. With at most four sides this forces the axis-aligned rectangle. With five sides the remaining edge makes a proper straight cut across a corner of its axis-aligned bounding rectangle. Scale the axes so the box is the unit square, reflect as needed to cut the northeast corner, and interchange axes so the horizontal and vertical legs of the cut obey \(0<u\le v<1\). These transformations preserve the family of pairs of rays with slopes of opposite sign and equal magnitude, after a change of slope parameter. Put \(\tau=v/u\). Unfold only the horizontal and vertical walls. The omitted regions become open diamonds

\[
 \frac{|X-(2i+1)|}{u}+\frac{|Z-(2j+1)|}{v}<1,\qquad i,j\in\mathbb Z.
\]

Choose a sufficiently small \(h>0\), put \(p=u(1-h/v)\) and \(s=1/(2-p)\), and join

\[
 A=(1-p,1-h),\qquad A'=(-3+p,-1-h).
\]

The segment has slope \(s<1\le\tau\), and its two endpoints fold to the same point on the oblique wall. It misses every intervening diamond. Indeed for a center with fixed abscissa \(c\) the weighted distance along the line to that center decreases up to \(X=c\) and then increases, since \(1/u>s/v\). In the endpoint columns the nearest points are the endpoints, where the indicated diamonds meet the segment transversely. In the only intermediate column \(X=-1\), the ordinate is \(-h\), at distance \(1-h>v\) from the nearest center. The remaining columns have horizontal separation greater than \(u\). The vertical integral grid lines crossed are \(0,-1,-2\), with ordinates \(s-h,-h,-s-h\). For sufficiently small \(h\) these avoid all horizontal integral grid lines, because \(s\to1/(2-u)<1\). The entire orbit is regular.

Folding the segment gives three vertical and two horizontal reflections followed by return to the oblique side. The arriving and departing rays have opposite signed slopes, so the six-reflection path closes under the internal-wave rule and has period three under \(b\). Its reverse occurs in the other set of three alternating boundary points. To compute the multiplier keep the slope fixed and vary the initial \(p\). The next intersection on the same unfolded face has parameter \(p'\), where the line equation gives

\[
 (\tau-s)p'=(\tau+s)p+2-4s.
\]

The return multiplier on this orbit is \((\tau+s)/(\tau-s)>1\). Reversing the order of reflection gives the conjugate companion orbit of \(b\) with multiplier \((\tau-s)/(\tau+s)<1\). The admissible \(h\)'s vary over an open interval and so do the corresponding slopes. \(\square\)

For example, \(u=v=1/2,\ h=1/10\) gives \(p=2/5,\ s=5/8,\ \lambda^2=64/89\) and attracting multiplier \(3/13\) per three iterates. The exact script finds three attracting and three repelling boundary points and no periodic interval. A different argument using the jumps of the shallow-slope return map proves rigidity for every convex polygon. [General rigidity theorem](phase1_rigidity.md)

**Exact period-three window for a small cut.** Suppose \(0<u\le v\le1/2\) in the normalized box, and restrict to \(0<s<1\). The slopes with a regular hyperbolic period-three orbit are precisely

\[
                   \frac12<s<\frac1{2-u}.
\]

There is no finite-energy standing mode anywhere in this open interval. For sufficiency in the construction above take every \(0<h<v\). Then \(h<1-v\), \(h<s\), and \(h+s<1\). For the last inequality \(h+s(h)\) increases since \(s'(h)=-(u/v)s^2\), and its limiting value at \(h=v\) is \(v+1/2\). Thus the segment avoids all vertices throughout the claimed interval.

For necessity, a regular orbit reflects from the bevel by reversing its horizontal velocity, since \(s<1\le\tau\). The horizontal reversal also occurs at the vertical walls, while vertical reversal occurs only at the horizontal walls. Normalize the speed components to \(1,s\) in absolute value. The right boundary has abscissa \(W(z)\in[1-u,1]\). For a periodic orbit with \(m\) vertical and \(n\) horizontal round trips in one circuit, the elapsed time computed from the two coordinates gives

\[
 m/s=\sum_{j=1}^n W(z_j),
\]

where \(z_j\) are its right-hand impact heights. A period-three orbit of \(b\) has six regular reflections, so \(m+n=3\), with \(m,n\ge1\). Since \(s<1\) and \(W\le1\), this forces \(m=1,n=2\). The unfolded vertical advance between the two right-hand impacts is \(s(W(z_1)+W(z_2))=1\), giving \(z_2=1-z_1\) after folding into the unit square. The bevel lies above height \(1-v\ge1/2\). The two regular visits can therefore meet the bevel at most once. If neither meets it, then \(s=1/2\) and every reflection is axial. Otherwise \(2-u<1/s<2\), with strict inequalities because the bevel impact is regular. A cycle with a single bevel reflection has the nonunit multiplier displayed above or its reciprocal. In the open interval the rotation denominator is three by the constructed orbit. Every open periodic interval would contain a regular period-three cycle with multiplier one, which the right-impact argument excludes. Theorem 2 now gives the spectral conclusion.

For equal cut legs \(u=v=\varepsilon\le1/2\), the removed area is \(\varepsilon^2/2\) and the exact slope window has length \(\varepsilon/[2(2-\varepsilon)]\). At \(h=p=\varepsilon/2\), the attracting multiplier is \((2-\varepsilon)/(6-\varepsilon)\). It tends to \(1/3\) as the removed area tends to zero. At the limiting uncut square and \(s=1/2\), the return is neutral and \(\lambda^2=4/5\) has infinite multiplicity.

## Exact rational tongues for a small corner cut

Continue with the one-corner cut, \(0<u\le v<1\), \(\tau=v/u\). Work in \(0<s<\tau\), where the slant acts as a vertical wall. Let \(t\) be the unfolded vertical phase at a right-hand impact on the circle of length two. The width \(W(t)\) is even and two-periodic. In one period it is one except on \(|t-1|<v\), where

\[
 W(t)=1-u+\frac{u}{v}|t-1|.
\]

Travel to the left wall and back defines the increasing right-return lift \(T_s\) implicitly by \(t'-t=s[W(t)+W(t')]\). The functions \(t\mapsto t\pm sW(t)\) are strictly increasing, so \(T_s\) is well-defined, continuous, and strictly increasing with \(s\) at every fixed \(t\). Right-return rotation numbers below count full turns on this circle, each of length two. Lenci, Bonanno and Cristadoro already include the pentagon in their class of concave right walls with a lower vertical segment. Their general theorem classifies the dynamical regimes. The following formulas use the finite length of the chamfer to determine specific plateau endpoints and the corresponding PDE kernels. [Lenci, Bonanno and Cristadoro, §§2–3](https://arxiv.org/abs/2102.01654)

**Theorem 4b.** Let \(1\le m<n\) be coprime and set \(s_*=m/(n-u)\). Suppose

\[
 s_*<\tau,\qquad v+s_*u<1/n .
\]

The full plateau of right-return rotation number \(m/n\) in \(0<s<\tau\) is \([m/n,s_*]\). The lower endpoint has an infinite-dimensional space of smooth standing modes. Throughout \((m/n,s_*]\) the finite-energy eigenspace is zero. At each interior parameter the two directed periodic cycles traverse one geometric ray in opposite directions. It reflects \(2(m+n)\) times per circuit and the multipliers per \(m+n\) iterates of \(b\) are \((\tau+s)/(\tau-s)\) and its reciprocal.

**Proof.** Put \(y=t-sW(t)\), and write \(d(y)=1-W(t)\). In this coordinate the lift becomes

\[
 S_s(y)=y+2s-2s\,d(y).
\]

The support of \(d\) is a single closed interval \(B\) of length \(2v\) on the phase circle. Both endpoints of its \(t\)-interval have \(W=1\), so the change of variables preserves their separation. The tent has a unique maximum \(u\) and exactly two preimages for every value in \((0,u)\).

On an \(n\)-periodic orbit of winding \(m\), the total deficit is \(D=\sum_{j=0}^{n-1}d(y_j)=n-m/s\). For a block of \(k<n\) iterates with deficit \(D_k\), their displacement differs from \(2km/n\) by \(2s(kD/n-D_k)\), whose absolute value is at most \(2sD\). Since \(m,n\) are coprime, distinct visits are separated on the circle by at least \(2/n-2sD\). For \(0\le D\le u\) in the claimed interval this is greater than \(2v\). Therefore at most one visit lies in \(B\).

For \(0<D<u\), take either \(y_0\) with \(d(y_0)=D\). The candidate points \(y_k=y_0+2sk-2sD\), \(1\le k\le n\), return to \(y_0+2m\) at \(k=n\). The same distance estimate shows every intermediate point lies outside \(B\), so this is an actual orbit. Conversely every periodic orbit must arise from one of these two choices. At the single active impact the derivative of \(S_s\) equals \((1+sW'(t))/(1-sW'(t))\), and all other derivatives are one. The two active phases have opposite vertical velocities and opposite values of \(W'=\pm1/\tau\), giving the two stated multipliers. Their directed curves are time reverses. Passage through an axial right-angle corner would make a folded trajectory retrace its incoming path, identifying its directed cycle with its reverse. This contradicts the opposite vertical velocities at the unique bevel visit. The other right-side junctions are outside the orbit by the strict separation. Thus these rays are regular. Their \(n\) horizontal and \(m\) vertical round trips give \(2(m+n)\) reflections. A neutral boundary interval would give an interval of regular periodic rays, impossible for two isolated cycles.

At \(D=0\), take translates by \(2m/n\) avoiding \(B\). Their starting phases contain an open interval since \(2nv<2\). After excluding finitely many corner itineraries this gives regular neutral rays, to which Theorem 2 applies. At \(D=u\) the unique maximum is the only possible active impact and the preceding construction gives its corner cycle. There is no regular periodic interval. For \(s<m/n\), every step of the lift has displacement at most \(2s\), so its rotation number is smaller than \(m/n\). Just above \(s_*\), \(D>u\), while \(2/n-2sD>2v\) still holds by strictness. A periodic orbit would have to place its total deficit above \(u\) on a single visit, which is impossible. The monotonicity of \(T_s\) in \(s\) excludes any later return to this rational rotation number. \(\square\)

For \(\varepsilon=u=v=1/16\) and \(m/n=2/5\) the plateau is \([2/5,32/79]\). At \(s=64/159\) the 14-reflection attracting ray has multiplier \(95/223\). Exhaustive rational perimeter subdivision gives 14 regular periodic boundary points in the interior example, periodic intervals at the lower endpoint, seven isolated corner-orbit points at the upper endpoint, and no period-seven boundary points at \(s=13/32\). [Exact rational verification](../experiments/phase1_pde.py)

**Corollary 4c.** Let \(\Omega_\varepsilon\) be the unit square with a northeast cut of equal legs \(\varepsilon\). Let \(\mathcal A_\varepsilon\) be the set of frequencies with a regular hyperbolic attractor and zero Dirichlet kernel. Then

\[
 \liminf_{\varepsilon\downarrow0}|\mathcal A_\varepsilon|
 \ \ge\ \frac6{\pi^2}(1-1/\sqrt2)=0.1780577256659594\ldots .
\]

The corresponding lower bound on the fraction of the angular interval \((0,\pi/2)\) is

\[
 \frac{12}{\pi^3}\left(\frac\pi4-\tfrac12\log2\right)
 =0.1698331899603879\ldots .
\]

The uncut square has attractor measure zero. These lower bounds count only the disjoint plateaus certified by Theorem 4b.

**Proof.** Take \(N=\lfloor1/\varepsilon\rfloor-1\) and every coprime pair \(1\le m<n\) with \(m+n\le N\). Then \(s_*<1\) and

\[
 n\varepsilon(1+s_*)=\varepsilon(m+n)+\frac{m\varepsilon^2}{n-\varepsilon}<1.
\]

The plateaus for distinct reduced rationals have disjoint interiors. On \(0<s<1\) each gives an interval of length \(\varepsilon(m/n)/(n-\varepsilon)\). Symmetry in the diagonal supplies its reciprocal interval above one. The combined density of the two changes of variable for the physical frequency \(\lambda\) is \(g_\lambda(x)=(1+x)/(1+x^2)^{3/2}\) at a slope \(x<1\). For the angle the density is \(g_\theta(x)=2/(1+x^2)\).

For either density \(g\), uniform continuity and the shrinking maximal interval length allow \(g\) to be evaluated at \(m/n\) in the sum. Its limit is

\[
 \frac6{\pi^2}\int_0^1\frac{x}{1+x}g(x)\,dx .
\]

Indeed rescale \((m,n)\) by \(N\) to \((a,b)\) in \(0<a<b,\ a+b\le1\). Primitive lattice points have density \(1/\zeta(2)=6/\pi^2\) there by Möbius inversion. The weight becomes \((a/b^2)g(a/b)\), since \(N\varepsilon\to1\). The contribution from \(n<\delta N\) is \(O(\delta)\), uniformly in \(N\), by summing at most \(n\) terms of size \(O(\varepsilon/n)\) for each \(n\). Thus the singularity at \(b=0\) does not change the limit. Setting \(x=a/b\) gives the displayed integral. For \(\lambda\) the integral is \(1-1/\sqrt2\). The angle integral is \(\pi/4-\tfrac12\log2\), which must be divided by \(\pi/2\) after multiplication by \(6/\pi^2\). \(\square\)

## The point spectrum of a tiled tank

Let \(\Omega\) be a bounded, connected orthogonal polygonal domain with Lipschitz boundary. Holes are allowed. Reflection at each regular wall is specular for the ray directions \((1,\pm s)\). Four reflected copies, indexed by the sign changes in \(x,z\) and glued along matching sides, form the compact translation surface \(X\). Cone points are the images of reentrant corners. The two sign changes induce commuting isometries \(H,V\) of \(X\); their product \(R=HV\) has derivative \(-I\) in translation coordinates. All regular transverse return maps are translations in the unfolded coordinates. In particular every regular periodic orbit has multiplier one, and recurrence for the preserved finite area excludes a positive-measure basin attracted to a corner or periodic ray.

**Theorem 5.** Every such \(\Omega\), with arbitrary positive wall lengths, has a dense set of eigenfrequencies with infinite-dimensional eigenspaces.

**Proof.** A regular periodic orbit of a straight-line flow on \(X\) has a surrounding open cylinder of parallel closed orbits. Choose a smooth transverse bump \(f\) on an inner subcylinder for direction \((1,s)\), extended by zero elsewhere. Its support can avoid all lifts of vertices by excluding finitely many transverse levels. Define

\[
 F=(I+R^*)f,\qquad U=(I-H^*)F .
\]

Here \(g^*f=f\circ g\). The two summands in \(U\) are constant along \((1,s)\) and \((1,-s)\), respectively, so \(U\) solves the factored wave equation. It is odd under both \(H\) and \(V\), so its restriction to one copy vanishes on every wall. For injectivity choose the support interval so that its subcylinder and its image under \(R\) are disjoint. Distinct maximal cylinders of the same direction are disjoint. On an \(R\)-invariant cylinder the transverse coordinate is reversed, so a suitable interval still exists. On a torus the same selection can be made on the circle of parallel closed geodesics. If \(U=0\), then \(F\) is constant along both directions, hence constant on the connected regular surface. Its small support makes that constant zero and disjointness gives \(f=0\). Odd symmetry propagates vanishing on one copy to every copy. Masur's density theorem supplies regular periodic directions in every angular interval, proving the claim. [Masur, 1986, Theorems 1 and 2](https://www.labri.fr/perso/vdelecro/grenoble_school/refs/Masur-1986-ClosedTrajectoriesForQuadraticDifferentialsWithAnApplicationToBilliards.pdf)

**Theorem 6.** Suppose the vertical and horizontal walls lie on the lines \(x=x_0+ia,\ z=z_0+jb\), with \(i,j\in\mathbb Z\). Then the complete point spectrum, with each eigenvalue of infinite multiplicity, is

\[
 \sigma_p(T)=\sigma_p(P)=\left\{
 \frac{(n/b)^2}{(m/a)^2+(n/b)^2}:m,n\in\mathbb N,\ m,n\ge1
 \right\}.
\]

In particular every ordinary polyomino with Lipschitz boundary, including the L triomino, has the same point spectrum and multiplicities as the square. On the L triomino every separated sine product displayed below vanishes on the interior segment \(x=1,\ 0<z<1\). Continuity of the local \(H^1\) trace gives the same vanishing for their closed energy span, whereas an interior smooth bump can have nonzero trace there. Thus these products are incomplete. Completeness of the **full eigenspaces** in the energy space is a separate question.

**Proof.** Every displayed value is realized by

\[
 \sin\left(\frac{m\pi(x-x_0)}a\right)
 \sin\left(\frac{n\pi(z-z_0)}b\right).
\]

All positive multiples of \((m,n)\) have the same eigenvalue and are linearly independent by restriction to an open mesh cell. Conversely, extend any \(H_0^1\) mode oddly across both families of flat walls. Matching zero traces give \(U\in H^1(X)\). Across an open vertical or horizontal wall the weak PDE continues by odd reflection: testing on the two copies gives a difference of smooth tests whose trace on the wall vanishes. Thus on the regular surface away from finitely many vertex lifts,

\[
 D_+D_-U=0,\qquad D_\pm=\partial_x\pm s\partial_z .
\]

In flow-box coordinates \(D_-U\in L^2\) is constant along \(D_+\) trajectories almost everywhere. Singular trajectories through the omitted finite set have area zero, so the function is flow-invariant modulo null sets. Likewise \(D_+U\) is invariant under the other flow. Rescaling the mesh to unit squares makes \(X\) square-tiled, with directional slopes \(\pm sa/b\). For \(sa/b\notin\mathbb Q\) both straight-line flows are uniquely ergodic for flat area by the arithmetic case of Veech's dichotomy. In particular each invariant \(L^2\) derivative is a constant. The identity \(U\circ R=U\) changes the sign of both directional derivatives, forcing both constants to be zero. Thus \(U\) is constant, and oddness forces \(U=0\). Finally \(sa/b\in\mathbb Q_{>0}\) is precisely the displayed frequency condition. [Hubert and Lelièvre, §1 and Appendix C](https://www.imo.universite-paris-saclay.fr/~samuel.lelievre/papers/sts-h2/sts-h2.pdf)

## An exact test of a published rectangular resonance rule

Zhang and Temnov's Theorem 2.3 proposes commensurability of a local ray slope with \(H/L\) as an eigenvalue criterion for a tilted rectangle. We consider the constant-coefficient Dirichlet streamfunction problem. In the necessity proof the authors reverse the wall-normal component in tank coordinates. For the same geometric ray angle their normalized squared frequency is \(\sin^2\theta=1-E_{\rm study}\), where \(E_{\rm study}=\cos^2\theta\). The conventions agree at \(1/2\). For internal waves, reflection exchanges the two characteristic line families fixed in the laboratory, whose absolute local slopes differ. This can be tested at a parameter satisfying both proposed local rationality conditions. [Zhang and Temnov, 2026, Theorems 2.3 and 3.1](https://journals.rudn.ru/CMFD/article/view/50766)

Take a square tilted by \(\tan\phi=1/3\), with laboratory \(\theta=\pi/4\) and \(\lambda^2=1/2\). Its two local ray slopes are \(1/2\) and \(-2\). Write \(t\in\mathbb R/4\mathbb Z\) for its perimeter coordinate increasing counterclockwise from the bottom-left corner. Alternate reflections preserving \(2z-x\) and \(z+2x\), with \(x,z\) now local tank coordinates. The second iterate \(b^2\) has exactly four fixed points.

| \(t\) | \(b(t)\) | \((b^2)'(t)\) |
|---:|---:|---:|
| \(1/3\) | \(7/3\) | \(1/16\) |
| \(4/3\) | \(10/3\) | \(16\) |
| \(7/3\) | \(1/3\) | \(1/16\) |
| \(10/3\) | \(4/3\) | \(16\) |

For a reproducible exhaustive check, pull the four vertices back by each of the first zero through four reflections. These cuts partition the boundary into twelve intervals. On each interval every reflection has fixed source and target sides and hence is affine. Solving each fixed-point equation over the rationals and testing the twelve endpoints gives exactly the table and no fixed interval. An orientation-preserving circle homeomorphism with a point of period two has all periodic points fixed by its second iterate. Thus Theorem 2 excludes every finite-energy mode at this frequency despite the rational local slopes. The same script checks the critical diamond and a \(4/13\) eigenvalue on the L triomino. Run \(\texttt{python3 experiments/phase1_pde.py}\). [Exact rational verification](../experiments/phase1_pde.py)

## Historical scope

John's 1941 paper studies the boundary map of \(u_{\xi\eta}=0\). Aleksandryan assumed an arbitrarily smooth boundary met by lines in at most two points in §4, p. 482. His Theorems 8 and 8 bis prove uniqueness for dense or irrational dynamics in that setting. His §6, Theorem 11, p. 492 explicitly constructs an eigenfunction when the periodic set has interior. Theorem 1 supplies the finite-energy polygon endpoint argument, and Theorem 2 supplies the condition on characteristic sides. The elementary corner degeneration above explains why those sides matter. [John, 1941, author’s collected paper](https://link.springer.com/chapter/10.1007/978-1-4612-5406-5_28) · [Aleksandryan, 1960, archived original](../sources/papers/Aleksandryan_1960_TrMMO_9_rus.pdf)

Ralston's paper appeared in *Journal of Mathematical Analysis and Applications* 44 (1973), 366–383. The smooth-domain singular-continuous examples of Fokin concern spectral measures, a finer classification than absence of eigenfunctions. The translation-surface argument above uses only density of periodic directions and ergodicity at irrational slopes on square-tiled surfaces. The classical sources inspected here do not settle completeness of the polyomino eigenspaces. [Ralston, 1973](https://doi.org/10.1016/0022-247X(73)90065-6) · [Dyatlov, Wang and Zworski, §1.3](https://msp.org/apde/2025/18-1/apde-v18-n1-p01-p.pdf)
