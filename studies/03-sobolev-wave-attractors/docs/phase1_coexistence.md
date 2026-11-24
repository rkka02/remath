# Prescribing wave attractors while keeping an entire standing-wave eigenspace

At $\lambda=1/\sqrt2$ a convex hexagonal tank can support a smooth, infinite-dimensional family of standing waves and an isolated attracting four-reflection ray. The contraction of the attracting cycle can be chosen anywhere in $(0,1)$ with the physical cycle, the standing waves and their Dirichlet energies fixed. More generally, prescribing $N$ regular four-reflection attractors together with a neutral cylinder requires exactly $N+5$ sides. Their ordered half-heights and their $N$ contraction factors can all be specified independently. The bound concerns geometric loops, each counted once with its attracting orientation.

## A hexagon with rational vertices

Use characteristic coordinates $s=x+z$, $t=z-x$. The physical point is $(x,z)=((s-t)/2,(s+t)/2)$. A horizontal characteristic in these coordinates has physical slope $+1$, a vertical one slope $-1$. Let $H$ exchange endpoints along a horizontal chord, $V$ do the same on a vertical chord, and $b=VH$. The differential equation at this frequency is $u_{st}=0$. The eigenvalue of the Sobolev operator is $1/2$.

In characteristic coordinates the tank is

$$
-1\le t\le1,\qquad L(t)=|t|-1\le s\le
R(t)=\min\{1-|t|,\;2/3+t/3,\;3/4-2t/3\}.
$$

The boundary consists of the two walls $P_L(t)=(L(t),t)$ and $P_R(t)=(R(t),t)$. Its cyclic vertices are

$$
(-1,0),\quad(0,-1),\quad(1/2,-1/2),\quad
(25/36,1/12),\quad(1/4,3/4),\quad(0,1).
$$

After translating $(x,z)$ by $(1/2,1/2)$ this is the unit square with its upper-right corner cut by two straight walls. The physical vertices are $(0,0),(1,0),(1,1/2),(29/36,8/9),(1/4,1),(0,1)$. The attracting ray hits $(1/4,0),(11/12,2/3),(2/3,11/12),(0,1/4)$ in order.

All sides have nonzero finite slope in these coordinates. The four-reflection loop is the boundary of

$$
[-3/4,\,7/12]\times[-1/4,\,1/4].
$$

Every contact lies in an edge interior. Starting at $P_L(-y)$ near $y=1/4$, the horizontal chord reaches $P_R(-y)$. The vertical chord then meets $P_R(y')$ where $2/3-y/3=3/4-2y'/3$. The next two chords return to $P_L(-y')$. Thus

$$
y'=\tfrac18+\tfrac12y,\qquad
\log|(b^2)'|=-\log 2,\qquad
\chi_b=-\tfrac12\log 2=-0.346573590279972654708616060729\ldots .
$$

The attracting boundary cycle is $\{P_L(-1/4),P_R(1/4)\}$. Its reverse is $\{P_R(-1/4),P_L(1/4)\}$, with multiplier $2$. In the physical tank they trace the same four segments in opposite directions.

For $3/4<y<1$ the boundaries of $[-(1-y),1-y]\times[-y,y]$ form a neutral family. Its swept region inside the open tank is

$$
\mathcal R=\{(s,t)\in\Omega:\ 0<|s|<1/4\ \text{or}\ |t|>3/4\}.
$$

The closed family includes the central line and its bounding rays. Every $h\in C_c^\infty((3/4,1))$, extended by zero, gives the smooth Dirichlet eigenfunction

$$
u_h(x,z)=h(1-|x+z|)-h(|z-x|).
$$

On either horizontal leg of the attractor, $t=\pm1/4$, this reduces to $h(1-|s|)$. Both legs cross the neutral family, and every nonzero member is nonzero somewhere on each leg.

## Tuning one cutting line

Fix $0<r<a<1$ and $0<n<1$. Choose a full-return contraction $0<\kappa<1$, and set

$$
m=\kappa n,\qquad d=1-(1-n)a,\qquad c=d-(n-m)r.
$$

Keep the same left wall and use $R(t)=\min\{1-|t|,c+mt,d-nt\}$. The right-wall joins occur at heights $-\beta,\tau,a$ where

$$
\tau=\frac{n-m}{n+m}r<r,\qquad
\beta=\frac{(1-n)a+(n-m)r}{1-m}\in(r,a).
$$

The four slopes of $R$ are $1,m,-n,-1$. The lower cut and the peak move as $\kappa$ varies. The underlying manufacturing description is a single movable cutting line $s=c+mt$ pivoted around $(1-a+n(a-r),-r)$. The other cutting line stays fixed.

A nondegenerate four-reflection orbit is exactly an inscribed axis-aligned rectangle. Its two horizontal sides must lie at heights $\pm y$, since the common left ordinate satisfies $L(t_1)=L(t_2)$. Its right ordinates match exactly when $D(y)=R(y)-R(-y)=0$. Direct subtraction gives

$$
D(y)=
\begin{cases}
2my & 0\le y\le\tau,\\
(n-m)(r-y) & \tau\le y\le\beta,\\
(1-n)(y-a) & \beta\le y\le a,\\
0 & a\le y\le1 .
\end{cases}
$$

The positive solutions are $r$ and $[a,1]$. The limit $y=1$ is a vertical two-reflection trajectory between the two height extrema. A collapsed horizontal trajectory would require equal heights of the two $s$ extrema, whereas those heights are $0$ and $\tau>0$. Any collapsed horizontal or vertical leg in a closed four-leg path forces the opposite leg to collapse as well. This gives the full periodic set of $b^2$. The presence of a genuine two-cycle gives rotation number $1/2$, so every periodic point has least period two.

The isolated rectangle has fixed horizontal extent $[r-1,\,1-a+n(a-r)]$. Its local return on $P_L(-y)$ is exactly

$$
y'=r+\kappa(y-r).
$$

The neutral family is indexed by $a\le y\le1$. At its endpoint, the oriented cycle $\{P_R(-a),P_L(a)\}$ has exterior multiplier $n$ and interior multiplier $1$. The reverse pair $\{P_L(-a),P_R(a)\}$ has exterior multiplier $1/n$ and interior multiplier $1$. Indeed, starting on $P_R(-y)$ near $y=a$ on the exterior gives $1-y'=d-ny$, or $y'=a+n(y-a)$.

**Exact forward basins.** The table lists each nonperiodic boundary phase, and includes the isolated attractor in its basin. The two points of the isolated repeller and the neutral periodic points are listed separately.

| Forward fate | On the left wall | On the right wall |
|---|---|---|
| Interior attracting two-cycle | $-a<t<r$ | $-r<t<a$ |
| Neutral endpoint $\{P_R(-a),P_L(a)\}$ | $r<t<a$ | $-a<t<-r$ |
| Isolated repelling two-cycle | $t=r$ | $t=-r$ |
| Neutral periodic points, including endpoints | $a\le |t|\le1$ | $a\le |t|\le1$ |

To verify the intervals, consider $b^2$. Successive fixed points on either open wall arc $-a<t<a$ are at $t=-r,r$. Each intervening interval is invariant, and an increasing interval homeomorphism without an interior fixed point moves monotonically toward one endpoint. The local derivatives determine the signs at $\pm r$. The exterior one-sided derivative at the neutral endpoint gives the same assignment. For a horizontal launch, choose $t$ uniformly in $[-1,1]$ and choose each wall with equal probability. The masses of the neutral family, isolated attractor basin and neutral-endpoint basin are $1-a,(a+r)/2,(a-r)/2$. They equal $1/4,1/2,1/4$ in the rational example. These fractions use characteristic offset as the launch coordinate.

At $\kappa=1$ the inner two slopes match in absolute value and $R(-t)=R(t)$. Every vertical chord joins $t$ to $-t$ and this reflection commutes with $H$. Hence $b^2$ is the identity globally. Each $g\in C_c^\infty((0,a))$, extended by zero, supplies the additional mode

$$
g(1+s)+g((d-s)/n)-g(|t|).
$$

Its two $s$-profiles lie in $(-1,a-1)$ and $(1-a,d)$, respectively. On the left wall the first equals $g(|t|)$, and on the inner right wall the second does. Both vanish on the outer wall. This gives infinitely many independent additional modes at the symmetric endpoint.

## The complete eigenspace and its energy

The following argument applies to the hexagon and to all the many-attractor polygons constructed below. In each, $L(t)=|t|-1$, $R(t)=1-|t|$ for $|t|\ge a$, and the fixed set off the neutral arcs is finite.

**Theorem.** Extend $h\in H^1(a,1)$ with $h(a)=0$ by zero to $[0,a]$. All finite-energy Dirichlet eigenfunctions at $\lambda^2=1/2$ are given uniquely by

$$
u_h(s,t)=h(1-|s|)-h(|t|),\qquad
\int_\Omega |\nabla_{x,z}u_h|^2\,dx\,dz
=4\int_a^1|h'(y)|^2\,dy .
$$

**Proof.** On an open convex polygon the distributional equation $u_{st}=0$ gives $u=F(s)-G(t)$ with $F,G$ locally $H^1$ on their open projection intervals. Indeed, $\partial_su$ depends only on $s$ on each small rectangle. Its local representatives glue along each connected vertical line section. A primitive supplies $F$, and the remaining function depends only on $t$. The $H^1$ bound on interior rectangles supplies local one-dimensional $H^1$. Thus $F,G$ have continuous interior representatives. On an open edge away from projection extrema the zero trace gives $F(s)=G(t)$ pointwise by continuity. All four extrema of this polygon in either coordinate have an interior value of the other coordinate. Taking limits along the incident sides therefore extends both $F,G$ to their projection endpoints. Denote their common continuous boundary value by $B$. It is invariant under $H$, $V$ and $b$.

On each closed wall arc $-a\le t\le a$, $b^2$ has only finitely many interior fixed points. An invariant continuous function is constant on each intervening open gap since all its forwards iterates converge to the same endpoint. Continuity at the finitely many endpoints gives one constant for that whole wall arc. At an interior height, $H$ exchanges walls, so these two constants agree. Subtract the common constant from both $F,G$. The left wall then gives $G(t)=G(-t)=h(|t|)$ with $h=0$ up to $a$ and $F(y-1)=h(y)$. On the right, the unchanged wall gives $F(1-y)=h(y)$ for $a\le y\le1$. The inner right wall spans $[1-a,\max R]$ and forces $F$ to vanish there. At the center $s=0$ the function $F$ is locally $H^1$ and $F(y-1)=h(y)$, giving $h\in H^1$ up to $y=1$. The same relation near $a$ gives $h(a)=0$.

Conversely these formulas agree at every boundary point, and $u_{st}=0$ distributionally. For $a\le y\le1$, the two sections $s=\pm(1-y)$ have length $2y$, and the two sections $t=\pm y$ have length $2(1-y)$. The first equality follows because the right wall on $[-a,a]$ lies above $1-a$ by concavity. The left wall and outer right wall give the advertised endpoints of the sections. The characteristic change of variables gives $\int_\Omega |\nabla_{x,z}u|^2\,dx\,dz=\int (|u_s|^2+|u_t|^2)\,ds\,dt$. Slicing and adding the four contributions gives the formula. It proves uniqueness as well as finite energy. The continuous zero trace puts $u_h$ in $H_0^1(\Omega)$. ∎

For fixed $a$, the symmetric difference of any two tanks in these families is contained in $\{|t|<a,\ s\ge1-a\}$, where every $u_h$ vanishes. Their entire eigenspaces therefore agree even after zero extension into the same ambient $H^1(\mathbb R^2)$.

In the one-cut hexagon family, fix a bounded box $B$ containing all the physical polygons and give $H_0^1(B)$ its Dirichlet inner product. Let $\Pi_\kappa$ be the orthogonal projection onto the zero-extended eigenspace. The additional modes at $\kappa=1$ are energy-orthogonal to the common eigenspace for $0<\kappa<1$. Their $s$-derivatives are supported at $|s|>1-a$, and their $t$-derivatives at $|t|<a$. Each corresponding derivative of a persistent mode is supported in the complementary range. Consequently

$$
\|\Pi_1-\Pi_\kappa\|=1,\qquad
\operatorname{rank}(\Pi_1-\Pi_\kappa)=\infty \qquad(0<\kappa<1).
$$

Indeed the persistent subspace is included in the symmetric tank's eigenspace, so the difference is itself an orthogonal projection. The walls and hence the closed tanks converge uniformly and in Hausdorff distance as $\kappa\uparrow1$.

On either horizontal attractor leg in any of these examples, $h(|t|)=0$, and its $s$-range strictly contains $[-(1-a),1-a]$. Therefore a single physical leg $J$ recovers the profile and the energy exactly,

$$
\int_\Omega |\nabla u_h|^2\,dx\,dz
=\sqrt2\int_J |\partial_{\mathrm{arc}}u_h|^2\,d\mathrm{arc}.
$$

Here $d\mathrm{arc}=|ds|/\sqrt2$. Concentration in characteristic coordinates is compatible with this exact measurement on the focusing loop. For $h\in C_c^\infty((a,1))$ the formula extends smoothly across the absolute-value folds.

## The sharp side count

**Theorem.** At fixed noncharacteristic directions in a convex $k$-gon, at most $\max(0,k-5)$ isolated regular four-reflection attractors can coexist with a neutral four-reflection cylinder. For each $N\ge1$ there is a convex $(N+5)$-gon attaining $N$. Given any $0<r_1<\cdots<r_N<a<1$ and any $0<\kappa_i<1$, its horizontal half-heights in characteristic coordinates are exactly the prescribed $r_i$ and its full-return contractions are exactly the prescribed $\kappa_i$. All vertices are rational when the inputs and auxiliary slope below are rational. The eigenfunctions and Dirichlet norm are those just calculated for the same cutoff $a$.

**Upper bound.** Apply an invertible linear map taking the two characteristic directions to the coordinate axes. With the directions noncharacteristic every edge normal has two nonzero components. The signs of these components partition the polygon edges into at most four successive monotone chains. The southwest corner of a regular inscribed rectangle lies on the southwest chain, since the positive horizontal and vertical directions both enter the polygon from that corner. The other corners select the other three signs in the same way. Thus existence of a regular rectangle forces all four chains to be nonempty. If their edge counts are $e_1,\ldots,e_4$, they have $\sum(e_i-1)=k-4$ internal vertices in total.

Write the southwest and southeast wall positions at bottom height $t$ as $x(t),X(t)$, the northeast height over $X$ as $v(X)$, and the northwest height over $x$ as $w(x)$. A genuine rectangle at $t$ exists exactly when

$$
v(X(t))=w(x(t)),\qquad x(t)<X(t),\qquad t<v(X(t)).
$$

All four functions are strictly monotone. In particular $x$ decreases, $X$ increases, and $v$ decreases. The common domain of the compositions and of the two strict inequalities is an interval. Each internal chain vertex gives at most one break of the difference, since each preceding map in a composition is injective. Hence the difference has at most $k-3$ pieces of affinity. A neutral cylinder forces one entire piece to vanish. Unless this is the sole piece, an adjacent piece also ends at zero and contributes no regular isolated root in its interior. In every other piece there is at most one isolated root. A regular rectangle has no corner at a chain break. Each such root yields at most one geometric attracting loop because the two directed return multipliers are reciprocal. This proves the upper bound, including the impossibility for quadrilaterals and pentagons. Without the neutral requirement the same argument gives the upper bound $k-3$ for regular period-two attractors.

**Construction with prescribed locations and rates.** Keep $L(t)=|t|-1$. We prescribe the signed wall displacement $R(y)-R(-y)$, which determines the inscribed rectangles. Put $r_0=0$, $r_{N+1}=a$, $G_0=1$ and

$$
G_i=G_{i-1}/\kappa_i\quad(1\le i\le N),\qquad M>G_N .
$$

Set $d_0=2$, $d_i=(-1)^i(G_i-G_{i-1})$ for $1\le i\le N$, and $d_{N+1}=(-1)^{N+1}(M-G_N)$. Consecutive lines $\ell_i(y)=d_i(y-r_i)$ have opposite nonzero slopes. Their crossing

$$
p_i=\frac{d_i r_i-d_{i-1}r_{i-1}}{d_i-d_{i-1}}
\quad(1\le i\le N+1)
$$

lies strictly between $r_{i-1}$ and $r_i$. Join the lines at those crossings and extend by zero from $p_{N+2}=a$ onward to obtain $D_0$. Write $d_{N+2}=0$ and $\delta_i=d_i-d_{i-1}$.

Make one corner of the right wall for each jump $\delta_i$. If $\delta_i<0$, place the corner at $t=p_i$. If $\delta_i>0$, place it at $t=-p_i$. Start from $R(-1)=0$, $R'(-1+)=1$, and decrease the wall slope by $|\delta_i|/M$ at each corner in order of increasing $t$. The resulting wall is concave. To check its height and the normalization, consider the two raw slopes $M R'(y)$ and $M R'(-y)$ outwards from $y=0$. They start at $1,1$. Indeed the positive jumps have sum $M-1$, as is also seen by the following induction. At $p_1$ the positive-height slope jumps from $1$ to $-G_1$. At $p_2$ the negative-height slope changes outwards from $1$ to $G_2$ when $N\ge2$. Thereafter the side with smaller slope magnitude is increased past the other at every crossing. On the interval containing $r_i$ the respective magnitudes are $G_{i-1}$ and $G_i$, in alternating order. The last two jumps raise the smaller magnitude to $M$ and then the remaining magnitude to $M$. Thus both outer magnitudes are $M$, the final slope is $-1$, and there is no characteristic side.

In particular, $(R(y)-R(-y))'=D_0'(y)/M$ on every affine piece. Both differences vanish at $y=0$, hence $R(y)-R(-y)=D_0(y)/M$. At $|t|\ge a$ the wall is exactly $1-|t|$. Since $R$ is concave and $R(\pm a)=1-a>0$, it stays above $1-a$ on $[-a,a]$. The $N+2$ distinct right-wall corners and the two left faces give exactly $N+5$ sides. The nondegenerate isolated rectangle heights are precisely the simple roots $r_i$, and the only neutral interval is $[a,1]$.

At a simple root the full-return derivative on the lower left wall is $R'(-r_i)/(-R'(r_i))$. The reverse orbit has its reciprocal. The smaller of these values is $G_{i-1}/G_i=\kappa_i$. The right-wall maximum is attained at the positive first crossing $p_1$, so there is no additional horizontal collapsed cycle. The only vertical collapsed cycle lies at $y=1$ as in the hexagon. This also verifies the finite fixed-set hypothesis used in the eigenspace proof. ∎

For a concrete sequence at every side count, choose

$$
r_i=\frac{(i+1/2)a}{N+2},\qquad
\kappa_i=\frac{4i-3}{4i+1},\qquad M=G_N+2.
$$

The first four attracting multipliers are $1/5,5/9,9/13,13/17$. The simpler six-sided example at the beginning uses the independently prescribed value $1/2$.

**Corollary for polygons without a neutral cylinder.** Across all noncharacteristic convex $k$-gons the maximum number of isolated regular four-reflection attractors is $k-3$ for each $k\ge4$. The upper bound follows from the same four-chain argument. For equality, retain only the first $N$ corners $p_1,\ldots,p_N$ of the construction. Extend the two faces present at $t=\pm r_N$ to their intersections with the left wall $s=|t|-1$. Each extension intersects the corresponding side of the left wall exactly once, since $R'(-r_N)>0$, $R'(r_N)<0$ and $R(\pm r_N)>L(\pm r_N)$. There are $N+1$ right faces and two left faces. Up to the last prescribed root the displacement is unchanged, and beyond $r_N$ it is the single nonzero line $d_N(y-r_N)/M$. Thus the two ends have different absolute heights, the $N$ prescribed regular cycles and multipliers survive, and no neutral cylinder remains. Taking $N=k-3$ proves equality. For example, a pentagon can support two four-reflection attractors with independently specified rates. The two exact maxima concern the fixed four-reflection period.

## Why one interior cycle cannot capture every exterior launch

**Proposition.** Let $b=VH$ be a composition of two chord involutions on a noncharacteristic convex polygon. Suppose $b^q$ fixes a nondegenerate open interval and is not the identity globally. There is an open interval of nonperiodic boundary phases whose forward orbits approach a periodic endpoint of a maximal neutral component. In particular, a disjoint interior hyperbolic orbit cannot capture every launch outside the neutral periodic set.

**Proof.** The fixed set of the finite piecewise-affine circle map $b^q$ is a finite union of intervals and points. An endpoint $e$ of a maximal nondegenerate component adjoins an open fixed-free gap. Within that gap $b^q$ moves monotonically in one direction, so either all forwards iterates or all backwards iterates approach $e$. In the latter case, $H b^q H=b^{-q}$ converts the backward basin to an open forward basin of $H(e)$. The homeomorphism $H$ preserves the fixed set and sends maximal nondegenerate components to components of the same kind. Taking the finite $b$-orbit of the attracting endpoint gives the stated limiting periodic orbit. ∎

## Relation to the literature and reproducibility

Aleksandryan connects the hyperbolic Dirichlet problem with boundary dynamics. Nogueira and Troubetzkoy's Proposition 11 gives a general count of periodic cylinders. Their result covers arbitrary periods. Lenci, Bonanno and Cristadoro's theorem for their concave-wall trapezoid class already allows a neutral beam with attracting and repelling *boundary* rays. The constructions above give an additional, separate two-sided hyperbolic orbit, a sharp side count at period two, and an independently prescribed list of multipliers alongside the full eigenspace. The four monotone chains are also familiar in computational geometry from the largest axis-aligned inscribed rectangle problem. These comparisons identify the scope of the results against the checked primary sources. [Aleksandryan (1960)](https://www.mathnet.ru/eng/mmo111) · [Nogueira and Troubetzkoy](https://arxiv.org/abs/2007.14773) · [Lenci, Bonanno and Cristadoro](https://arxiv.org/abs/2102.01654) · [Alt, Hsu and Snoeyink](https://adacomp.org/wp-content/uploads/2016/01/cccg95.pdf)

The companion script uses rational arithmetic to intersect chords with every polygon edge, solve the piecewise-affine fixed-point equations, check both directed multipliers and the six fixed-free gap signs, and integrate a polynomial mode's energy from the polygon sections. It includes independently prescribed rates and locations and examples through eighteen sides. [Exact verification program](../experiments/phase1_coexistence.py)
