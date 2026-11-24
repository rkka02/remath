# All-frequency rigidity for convex polygonal tanks

Let $K$ be a bounded convex polygon with nonempty interior. Combine adjacent collinear walls. Write $s>0$ for the physical slope in the $(x,z)$ plane. For the stationary equation $(1-\lambda^2)u_{zz}-\lambda^2u_{xx}=0$, the two characteristic families have slopes $\pm s$, where

\[
s=\frac{\sqrt{1-\lambda^2}}{\lambda},\qquad \lambda=(1+s^2)^{-1/2}.
\]

Write $g_\pm= z\pm sx$, let $\gamma_\pm$ exchange the two endpoints of each corresponding chord, and put $b_s=\gamma_+\gamma_-$. We use slopes transverse to all walls. A regular hyperbolic attracting cycle avoids all vertices and has a return derivative strictly between zero and one. A corner attracts from one side if the iterates on a nonempty boundary arc converge exponentially to the vertex. Each characteristic involution swaps the two sides of a common supporting corner and conjugates the chess map to its inverse.

## The rigidity theorem

**Theorem 1.** An axis-aligned rectangle is the only bounded convex polygon for which every transverse physical slope has neither a regular hyperbolic attracting cycle nor a one-sided attracting corner. Every other polygon has an open interval of transverse slopes with one of these types of attraction.

If all four horizontal and vertical supporting lines meet the polygon in positive-length edges, and the polygon has an oblique edge, the regular attracting cycles occur on infinitely many open intervals accumulating at $s=0$. The same conclusion holds at $s=\infty$ by exchanging the axes.

**Theorem 2.** Suppose the top and bottom supporting lines carry positive-length horizontal edges and at least one of the left and right wall chains has a genuine vertex strictly between the two heights. Translate the bottom to $z=0$ and let the top height be $H$. Write $L(z),R(z)$ for the horizontal endpoints, $W(z)=R(z)-L(z)>0$, and define

\[
T(y)=\int_0^y\frac{dz}{W(z)},\qquad A=T(H),\qquad \beta_h=\frac{T(h)}{A}.
\]

Consider rays which, after unfolding at the horizontal edges, ascend one vertical period $2H$ in $n$ returns from the left wall to itself. For every sufficiently large $n$, either their slopes contain an open interval of regular attracting $b_s$-cycles of primitive period $n+1$, or

\[
\operatorname{dist}(n\beta_h,\mathbb Z)\leq C/n
\tag{1}
\]

at **every** interior wall vertex of height $h$. The constant is independent of $n$. Every one-turn resonance in this statement lies at $s=A/n+O(n^{-3})$. At least one in each pair of sufficiently large consecutive values of $n$ supplies such an open interval. If any $\beta_h$ is irrational, the set of $n$ supplying open intervals has natural density one. If $\beta_h=a/d$ in lowest terms, all sufficiently large exceptions must be divisible by $d$. These are statements about the integer period labels.

## Supporting corners and the rectangle

If the top horizontal support consists of a single vertex $v$, that vertex strictly maximizes both $g_+$ and $g_-$ for all sufficiently small $s>0$. The same argument applies at a singleton bottom support and, using sufficiently large $s$, at a singleton left or right support. Choose a slope transverse to every wall. With $u,v_1$ the two edge directions pointing from the common supporting vertex into its incident edges, the local multipliers on the two sides of the vertex are

\[
D=\left|\frac{g_-(u)g_+(v_1)}{g_-(v_1)g_+(u)}\right|,\qquad D^{-1}.
\]

Here the linear forms act on vectors. Each ratio $g_\pm(u)/g_\pm(v_1)$ is positive. Equality $D=1$ would imply that the two images under the invertible linear map $(g_-,g_+)$ are collinear. Thus one side contracts. The fixed-corner criterion and its semistability already appear in Nogueira–Troubetzkoy, Proposition 5. [Chess Billiards](https://arxiv.org/abs/2007.14773)

For an axis-aligned rectangle the boundary length measure $d\ell_s=|dz|+s|dx|$ agrees on every open edge with both $|dg_+|$ and $|dg_-|$. Both involutions are orientation-reversing isometries of the circle in that length coordinate. Their composition is a rigid rotation. A common supporting vertex for the two distinct directions is impossible because the four coordinate supports are edges. A polygon with all four coordinate support edges and an oblique wall has an interior left or right wall vertex. Applying Theorem 2 there completes the proof of Theorem 1. The proof after interchanging axes is identical.

If “attracting corner” is given the stronger meaning of a two-sided attracting fixed point, the axis-right isosceles triangle is a counterexample to that version. Each transverse slope gives at least one common support vertex, since both pairs of supporting vertices belong to a three-element set. Thus the rotation number is zero and every periodic point is a common support vertex with reciprocal one-sided slopes. At the only positive edge-parallel slope $s=1$, the midpoint-extended map on the triangle with vertices $(0,0),(1,0),(0,1)$ satisfies $b_1^2=\mathrm{Id}$. For instance $(0,u)$ follows the four successive impacts $((1-u)/2,(1+u)/2)$, $((1+u)/2,(1-u)/2)$, $(u,0)$, $(0,u)$. Interchanging the coordinates covers the other vertical and horizontal starting points, and their first chord images cover the hypotenuse.

## The unfolded return map

Extend $L,R$ by reflection about $0,H$ and then periodically with period $P=2H$. The functions are globally Lipschitz and piecewise affine. The width is bounded below by a positive constant, including at the two folds. In the reflected channel an ascending leg from the left wall at $z$ reaches the right wall at $w=U_s(z)$. The next leg reaches the left wall at $t=V_s(w)$. They satisfy

\[
w-z=s[R(w)-L(z)],\qquad t-w=s[R(w)-L(t)].
\tag{2}
\]

For sufficiently small $s$, each of $y\mapsto y\pm sR(y)$ and $y\mapsto y\pm sL(y)$ is an increasing, bi-Lipschitz lift commuting with translation by $P$. Equations (2) therefore define increasing piecewise-affine lifts $U_s,V_s$. Each height increment lies between $c s$ and $C s$ uniformly. For example, if $M$ bounds the two wall Lipschitz constants, then

\[
\frac{s W(z)}{1+sM}\leq w-z\leq\frac{s W(z)}{1-sM}.
\]

The analogous bounds on $t-w$ use $W(w)$. The straight legs stay inside the unfolded channel because their horizontal speed in the height variable exceeds both wall Lipschitz constants. Reflection at a cap folds them to the physical billiard. Their endpoints and iterates increase strictly with $s$ by (2) and positivity of each leg's horizontal travel. Define the left and right return lifts $F_s=V_sU_s$ and $G_s=U_sV_s$. They are continuous in the parameter and strictly increasing in it at each fixed initial height.

One turn with $n$ left returns has $2n$ wall impacts and crosses exactly two cap lines. Away from vertices, this gives $2n+2$ physical impacts and $n+1$ iterates of the two-chord map. Choose a left impact in a rising physical half of the unfolded channel, which exists for small $s$ because a single left return advances less than $H$. The first physical chord then has slope $+s$, as required by the convention $b_s=\gamma_+\gamma_-$. The starting physical point together with that outgoing slope uniquely determines its unfolded height modulo $P$. Since $F_s^n(z)=z+P$ has reduced winding fraction $1/n$, any shorter physical return would contradict the primitive $n$ of this left orbit. The local physical multiplier of $b_s^{n+1}$ is the derivative of $F_s^n$ on the corresponding left wall.

## An interval of slopes or a globally periodic return

For each large $n$ and each start $z\bmod P$, the equation

\[
F_s^n(z)=z+P
\tag{3}
\]

has a unique small positive solution $s_n(z)$. Existence follows by taking $s$ on either side of fixed constant multiples of $1/n$, using the uniform increment bounds. Strict increase gives uniqueness and continuity in $z$. If $s_n(z)$ is constant, (3) holds for all $z$ at one slope. Otherwise its image contains an interval. At every slope strictly between its extremes, the displacement $F_s^n(z)-z-P$ takes both signs.

Only finitely many slopes in this interval can carry a winding-one period-$n$ orbit hitting any specified physical vertex. For a left vertex of unfolded height $c$ the necessary condition $F_s^n(c)=c+P$ has at most one solution. For a right vertex use $G_s^n(c)=c+P$. Include the cap vertices and the reflected copies in this finite list. At any remaining slope all the zeros of the displacement occur in affine branches. A transition from positive to negative gives a regular zero with derivative $0<(F_s^n)'<1$. A nontrivial interval of zeros would have a breakpoint at an endpoint, which has already been excluded. This regular periodic orbit persists on an open interval because its itinerary avoids all vertices and its affine return has derivative different from one.

## Why a uniformly periodic orbit must meet a fold

Write $k_s(m)=(1+sm)/(1-sm)$. Differentiate (2) on both sides of a winding-one periodic orbit, always using the same one-sided derivative because all the intermediate maps increase. If the $n$ left heights are $z_i$, and their right-wall images $w_i$, telescoping gives

\[
(F_s^n)'_\pm(z_0)=\prod_{i=0}^{n-1}
\frac{k_s(R'_\pm(w_i))}{k_s(L'_\pm(z_i))}.
\tag{4}
\]

For a globally periodic return both sides of (4) are one. On each unfolded open half-period $R$ is concave and $L$ convex, also on reflected copies. Since $m\mapsto\log k_s(m)$ increases, every genuine interior wall corner reached by this orbit makes a strictly **negative** contribution to the jump from the left to the right value of the logarithm in (4). Other interior impacts contribute zero or a negative quantity. Consequently an orbit through any genuine interior wall corner must also hit a fold $0$ or $H\bmod P$, on one wall or the other. This conclusion also applies when the chosen corner is on the right wall by taking its unique preceding left impact.

## Uniform travel-time estimate

Extend $T$ to the unfolded real line by integrating the reflected $1/W$, so $T(z+P)=T(z)+2A$. If the complete left return from $z$ to $t=F_s(z)$ crosses no wall breakpoint, let $l=L'$ and $r=R'$ on that interval. Equations (2) give exactly

\[
t-z=\frac{2sW(z)}{(1-sr)(1+sl)},\qquad
T(t)-T(z)=\frac{\log k_s(r)-\log k_s(l)}{r-l}=2s+O(s^3).
\tag{5}
\]

At $r=l$ the quotient takes its derivative value $2s/(1-s^2r^2)$. The constants are uniform over the finitely many possible slopes. On a return crossing a wall breakpoint, Lipschitz continuity in (2) gives $t-z=2sW(z)+O(s^2)$, hence $T(t)-T(z)=2s+O(s^2)$. Any partial one-turn orbit has only boundedly many such exceptional returns, since successive height intervals have disjoint interiors and there are finitely many wall vertices per period. Summing (5) for any $k\leq n$ gives

\[
T(F_s^k(z))-T(z)=2ks+O(ns^3+s^2)=2ks+O(s^2).
\tag{6}
\]

The bounds preceding (3) give $n\asymp s^{-1}$. One half-leg has travel time $s+O(s^2)$ by (2), uniformly, including across corners. For a full one-turn orbit (6) implies $2A=2ns+O(s^2)$, giving $s=A/n+O(n^{-3})$.

Take a globally periodic slope, an interior wall corner of height $h\in(0,H)$, and a fold on its orbit furnished by (4). The oriented path between these two impacts has an integer $m\leq2n$ of half-legs. All complete left returns have the accumulated error (6), and at most two half-legs remain. Its travel time therefore equals $ms+O(s^2)$. Modulo $2A$, the difference of the endpoint travel coordinates is $T(h)$ or $T(h)-A$, up to sign. Substitution of $s=A/n+O(n^{-3})$ proves (1).

If two consecutive large $n,n+1$ were globally periodic, subtracting their approximations in (1) would give $\operatorname{dist}(\beta_h,\mathbb Z)=O(1/n)$, impossible for the fixed interior value $0<\beta_h<1$. For rational $\beta_h=a/d$, a nonintegral $n\beta_h$ is at least $1/d$ from an integer. For irrational $\beta_h$, the fractional parts $n\beta_h\bmod1$ are equidistributed. The upper density of exceptions is at most $2\varepsilon$ for every $\varepsilon>0$, by (1). This proves Theorem 2.

The same estimate gives an upper bound on the total length in slope. The one-turn resonances for label $n$ occupy at most $C/n^3$. For $0<s<\varepsilon$ their combined length is $O(\varepsilon^2)$, by summing over $n\gtrsim1/\varepsilon$. Thus this family can realize almost every period label while occupying a vanishing proportion of a shrinking slope interval. Other winding numbers are outside this estimate.

## An exact octagon with square symmetry

Take the octagon

\[
K=\{(x,z): |x|,|z|\leq1,\ |x|+|z|\leq3/2\}.
\]

It has the eight symmetries of a square. Its oblique edges eliminate the all-frequency neutrality of the square. In unfolded height $h=z+1\bmod 4$ its half-width is

\[
d(h)=\min\{1,\tfrac12+\operatorname{dist}(h,2\mathbb Z)\}.
\]

Both leg maps are the same increasing map $J_s$, where $J_s(h)-h=s[d(h)+d(J_s(h))]$, valid for $0<s<1$, and $J_s(h+2)=J_s(h)+2$. The one-turn $n=2$ condition $J_s^4(h)=h+4$ is equivalent to $J_s^2(h)=h+2$ since an increasing lift $J_s^2-2$ has no nontrivial two-cycle. The two leg lengths are then equal, giving $J_s(h)=h+1$. Thus

\[
1/s=d(h)+d(h+1)\in[3/2,2].
\]

The full closed resonance interval is $[1/2,2/3]$. For every interior slope an attracting branch starts at $h=5/2-1/s\in(1/2,1)$. Its four unfolded wall impacts have heights $h,h+1,h+2,h+3\bmod4$. The half-width derivatives at them are $0,-1,0,-1$. The multiplier of $b_s^3$ is $((1-s)/(1+s))^2$. At $s=3/5$, the physical cycle has period three, the four unfolded wall heights are $5/6,11/6,17/6,23/6$, the multiplier is $1/16$, and $\lambda=5/\sqrt{34}$.

At the interior sidewall height $h=1/2$, one finds $T(1/2)=\tfrac12\log 2$, $A=T(2)=\log 2+\tfrac12$, and $\beta_{1/2}=\log 2/(1+2\log2)$. Irrationality follows from the transcendence of $\log2$ by Hermite–Lindemann. Theorem 2 therefore supplies a density-one set of period labels with attracting tongues in this octagon with rational vertices.

Independent rational composition of the two chord involutions on all eight physical edges gives the following checks. At each listed slope there are two attracting and two repelling cycles, all regular. Rotation uses counterclockwise perimeter orientation.

| $s$ | Rotation | Primitive period | Attracting full-period multiplier | Repelling full-period multiplier |
| --- | --- | ---: | ---: | ---: |
| $3/5$ | $2/3$ | 3 | $1/16$ | $16$ |
| $7/18$ | $3/4$ | 4 | $121/625$ | $625/121$ |
| $5/17$ | $4/5$ | 5 | $36/121$ | $121/36$ |

## A separate period-two criterion for centrally symmetric polygons

**Theorem 3.** Put the center of a centrally symmetric polygon at the origin and let $(a,0),(0,b)$ be its positive axis intercepts. Write $r=b/a$ and $S_r(x,z)=(z/r,rx)$. A regular hyperbolic period-two cycle exists at a transverse slope if and only if $S_r K\ne K$. When it exists it persists on an open interval. If $S_rK=K$, every transverse slope carrying any primitive period-two point equals $r$. At $r$ the chess map is central inversion, using midpoint reflection on any characteristic support edge if necessary.

Let $C=-I$. It commutes with $b_s$ and acts as a half-turn in normalized arclength. If $b_s$ has a primitive period-two point, its rotation number is $1/2$ and $Cb_s$ has rotation number zero. Indeed a lift of $b_s$ commutes with translation by $1/2$, as follows by applying twice its commutation with $C$ modulo integers. An orientation-preserving circle map of rotation number zero has only fixed points among its periodic points. Since $(Cb_s)^2=b_s^2$, the two points of every such $b_s$ orbit are $p,-p$. If its intermediate positive-slope impact is $-q$, the chord equations give $q=S_s p$. The ordered four impacts are $p,-q,-p,q$.

Consider the positive-coordinate quadrant. On the outer boundary arc from the positive horizontal axis to the positive vertical axis, $xz$ increases strictly to one maximum and then decreases strictly to zero. To see this, the set $K\cap\{x,z>0,\ xz\geq t\}$ is convex for each $t>0$. Its radial angles form an interval and agree with the angles where the outer boundary has $xz\geq t$. Strict concavity of $\log x+\log z$ gives a unique maximizer. No straight polygonal arc has constant positive product. Thus at every $t$ strictly between zero and the maximum there are exactly two points $p(t),q(t)$, ordered along the arc, and they vary continuously. They satisfy

\[
q(t)=S_{s(t)}p(t),\qquad
s(t)=\frac{t}{x_p(t)x_q(t)},\qquad
\lim_{t\downarrow 0}s(t)=r.
\]

The last limit follows from $s=z_q/x_p$. For the other pair of opposite quadrants first reflect one coordinate. This interchanges the characteristic labels and preserves the period-two and hyperbolicity questions, including the existence of an attracting companion under reversal.

On each fixed pair of edge interiors the functions are real analytic away from stationary points of the product. There are finitely many branches. If $S_r K\ne K$, $s(t)$ cannot be constant on both quadrant arcs, since a constant would have to be $r$ and each pair of points would be exchanged by $S_r$ up to central inversion. Choose $t$ on a varying branch with $s'(t)\ne0$ and with $s(t)$ transverse to every wall. The multiplier at $p$ is $D^2$, with

\[
D=\left|\frac{g_-(e_p)g_+(e_q)}{g_-(e_q)g_+(e_p)}\right|,
\]

for incident edge tangents $e_p,e_q$. If $D=1$, elementary expansion gives $e_q\parallel e_p$ or $e_q\parallel S_s e_p$. Two parallel support edges in a centrally symmetric polygon lie on the same line or opposite support lines. Thus the first alternative puts either $p,q$ or $-p,q$ on one edge, making a characteristic parallel to it. For the second, differentiate $q=S_{s(t)}p$. Writing $p=(x,z)$ and using $(xz)'=1$ gives

\[
\det(q',S_sp')=-s'(t)/s(t).
\]

This is nonzero. Therefore $D\ne1$, and the cycles $\{p,-p\}$ and $\{q,-q\}$ have reciprocal multipliers. One attracts regularly.

Conversely suppose $S_rK=K$. After a coordinate reflection if necessary, examine a four-impact cycle with $p,q$ in the first quadrant. If they are distinct with positive product, the two points at that product are exchanged by $S_r$ and hence $s=r$. If $p=q=(x,sx)$, the other characteristic has slope $-s$ and supports at $p$. For any $(x',z')$ in this quadrant of $K$,

\[
x'z'\leq (z'+sx')^2/(4s)\leq (2sx)^2/(4s)=xz.
\]

Thus $p$ is the unique product maximizer. Symmetry fixes that maximizer, again giving $s=r$. If either coordinate vanishes, the two axis intercepts force $s=r$ directly. Finally $S_r$ and $-S_r$ preserve $g_+$ and $g_-$ respectively and exchange the chord endpoints, so their composition is $C$. In particular the octagon above has regular period-three focusing and no regular period-two focusing at any physical slope.

For an even regular $N$-gon the covariance matrix of its vertices is scalar. Every linear symmetry is therefore orthogonal. The period-two criterion reduces to whether the line at $45^\circ$ is a dihedral symmetry axis, equivalently whether $\phi+k\pi/N=\pi/4\bmod\pi$ for some integer $k$, where $\phi$ is one vertex angle. A tilted rectangle with $0<\phi<\pi/4$ has one edge direction of positive slope and one of negative slope. The map $S_r$ preserves slope sign and could preserve both edge directions only if their absolute slopes were equal, which requires $\phi=\pi/4$. All rectangles in the stated open tilt range have a regular period-two tongue, at every aspect ratio. The criterion also covers any nontrivial horizontal shear of an axis-aligned rectangle, since it then has horizontal edges and no vertical ones.

## Literature scope

Nogueira–Troubetzkoy prove the general fixed-corner criterion, give bounds on periodic cylinders, and vary two independent directions on a fixed square. Lenci–Bonanno–Cristadoro analyze channels with one sloping or curved boundary and give a parity law for a rectangular trapezoid. Sibgatullin–Petrov–Xu–Maas compute exact regions and multipliers in that trapezoid for the family with one reflection on each lateral wall. Our argument uses a single physical parameter, two general polygonal wall chains, the sign of their combined derivative jumps, and the second-order travel coordinate at near-horizontal slopes. These references establish the adjoining results. An exhaustive priority claim would require checking the wider historical literature. [Nogueira–Troubetzkoy](https://arxiv.org/abs/2007.14773) · [Lenci–Bonanno–Cristadoro](https://arxiv.org/abs/2102.01654) · [Sibgatullin–Petrov–Xu–Maas](https://doi.org/10.3390/sym14020319)
