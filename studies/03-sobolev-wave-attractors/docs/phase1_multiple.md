# How many polygonal wave attractors can coexist?

At one frequency, a convex \(k\)-gon supports at most \(k-3\) two-sided attracting periodic boundary orbits when both characteristic directions are transverse to its edges. The bound holds at every period and is attained at period two by polygons with rational vertices and \(k-3\) distinct rates. A regular nonagon already attains the bound. A regular octagon can instead change from entirely neutral to finite exponential focusing under an arbitrarily small rotation.

Throughout, \(s=\tan\theta\) is the positive physical ray slope, \(\lambda=(1+s^2)^{-1/2}\) for the stationary PDE in the prompt, and
\[
 (u,v)=(z+sx,z-sx),\qquad b=\gamma^+\gamma^- .
\]
The first chord preserves \(v\), the second preserves \(u\). A regular cycle hits only open edges and avoids grazing. A two-sided attracting cycle attracts nearby boundary points on both sides. A support corner can attract from one side and repel from the other. All exponents below use one application of \(b\) as a time step.

## A sharp bound in every period

**Theorem 1.** For a convex \(k\)-gon with no characteristic edge, the number \(m\) of two-sided attracting cycles of \(b\) satisfies \(m\le k-3\). Other periodic points, intervals of periodic points and one-sided periodic corners may be present. The same upper bound \(k-3\) applies to regular hyperbolic **attracting** cycles avoiding every tangent chord at an edge-parallel parameter. By reversal it applies separately to repelling cycles.

**Proof.** Select any \(m\ge1\) attracting cycles. Both chord involutions reverse time for \(b\), since \(\gamma^- b\gamma^-=b^{-1}\) and \(\gamma^+ b\gamma^+=b^{-1}\). Thus \(\gamma^-\) takes the selected cycles to \(m\) distinct repelling cycles. All \(2m\) have the same least period \(q\), by the rotation-number theorem for orientation-preserving circle homeomorphisms.

Each coordinate has two extremal vertices. If a vertex is extremal for both coordinates, it is fixed by \(b\). Conversely \(bx=x\) forces \(\gamma^-x=\gamma^+x=x\), since the two characteristic lines through \(x\) intersect only at \(x\). In the presence of a fixed point all periodic orbits are fixed points, and each is its own time reverse, so none can be a two-sided attractor. Hence \(q\ge2\) and all four extremal vertices are distinct.

In cyclic order label the \(2mq\) selected attracting and repelling points by integers modulo \(2mq\). The homeomorphism \(b\) acts as a cyclic shift \(d\) of order \(q\), so \(\gcd(d,2mq)=2m\). The marked-point orbits and the orbits of gaps between consecutive marked points therefore each have \(2m\) labels modulo \(2m\). On marked-point labels \(\gamma^-\) induces \(i\mapsto h-i\). It fixes no orbit label, since it exchanges attraction and repulsion, so \(h\) is odd. On the gap following \(i\), the involution induces \(i\mapsto h-i-1\). Exactly two of the \(2m\) gap labels are fixed. The other \(2m-2\) form \(m-1\) pairs. The involution \(\gamma^+=b\gamma^-\) induces the same map on the labels.

The four extremal vertices lie outside the marked set. Each is fixed by one of the involutions and therefore lies in a gap with one of the two fixed labels. Each of the \(m-1\) other pairs requires a further vertex. Indeed, suppose the union of all gaps belonging to one pair contains no vertex. Choose a gap \(J\) in this union. Each \(b^iJ\) and each \(\gamma^- b^iJ\) lies in one open edge. Every half-step of \(b^q\) is then affine across \(J\) in edge coordinates. Its two endpoints are fixed by \(b^q\), so \(b^q\) fixes every point of \(J\), contrary to attraction or repulsion at its endpoints. Counting the disjoint vertex requirements gives \(k\ge4+(m-1)\).

At an edge-parallel parameter, any finite collection of regular hyperbolic **attracting** cycles whose chords stay transverse at every impact has the same edge sequences after a small perturbation of the slope. On each orbit the affine return has derivative different from one, so its fixed point and all the strict edge-interior conditions persist. The perturbed cycles remain attracting, so the noncharacteristic bound applies. Reversing the chords proves the separate bound for repellers. **∎**

The combined count can exceed \(k-3\). In the \(m=2\) construction below, intersect the pentagon with \(u\ge1/2\). This gives a hexagon with one characteristic edge. The transverse rectangles \([2,89]\times[-2,2]\) and \([4,86]\times[-4,4]\) survive. Their directed cycles have multipliers \(1/3,3,3/5,5/3\), giving two attractors and two repellers on six sides.

## Polygons with rational vertices attaining the bound with distinct rates

Fix \(m\ge1\). In characteristic coordinates take the closed region \(L(v)\le u\le R(v)\), with
\[
\begin{split}
L(v)&=|v|,\qquad a_j=(-1)^{j-1}(2j-1),\qquad C=10(m+1)^2,\\
R(v)&=C+\tfrac12v
       -2\sum_{a_j>0}(v-a_j)_+
       -2\sum_{a_j<0}(a_j-v)_+ .
\end{split}
\]
Here \(r_+=\max(r,0)\). The left graph is convex, the right graph is concave, and the latter's derivative drops by two at each \(a_j\). For \(|v|\le 2m\), \(R(v)\ge C-m-4m^2>2m\). The two affine tails meet \(L\) once each outside that range. They give the top and bottom vertices. Together with the left bend and the \(m\) right bends, these are exactly \(m+3\) vertices. Every edge has finite nonzero slope \(du/dv\). Taking \(s=1\) gives a polygon with rational vertices in physical \((x,z)\) at \(\lambda=1/\sqrt2\).

A nondegenerate rectangle with all four vertices on the boundary and sides in the two characteristic directions supplies a pair of \(b\)-cycles, one on each diagonal. The multipliers are reciprocal by time reversal. For \(t>0\), the left endpoints of the horizontal chords at \(v=\pm t\) both have \(u=t\). Their right endpoints have the same \(u\) exactly when \(D(t)=R(t)-R(-t)=0\). On the positive axis, \(D(0)=0\), its initial slope is \(+1\), and this slope alternates between \(+1\) and \(-1\) at \(1,3,\ldots,2m-1\). Thus there is a nondegenerate rectangle at each \(t=2j\), \(1\le j\le m\), with all contacts strictly inside edges.

The derivative of \(b^2\) on the southwest/northeast diagonal cycle, in the \(v\)-coordinate near its southwest point, is
\[
 M_{\mathrm{SW}}=-\frac{R'(-2j)}{R'(2j)}
 =\frac{1+4\lfloor j/2\rfloor}{4\lceil j/2\rceil-1}.
\]
The attracting diagonal has the smaller of \(M_{\mathrm{SW}},M_{\mathrm{SW}}^{-1}\). In particular,
\[
 \boxed{\quad M_j=\frac{2j-1}{2j+1},\qquad
 \Lambda_j=\tfrac12\log\frac{2j-1}{2j+1},\qquad 1\le j\le k-3 .\quad}
\]
These \(k-3\) distinct multipliers exhaust the bound in Theorem 1. For \(k=3\) the maximum zero follows from the bound itself.

## A stronger bound for centered polygons at period two

**Proposition 2.** A centrally symmetric convex polygon with \(2h\) edges, all noncharacteristic, has at most \(h-1\) two-sided period-two attractors. The bound is attained by every even regular polygon at the generic orientations in the next section.

Put its center at the origin. Every inscribed nondegenerate axis-parallel rectangle must be centered there. Otherwise its antipodal image is another inscribed rectangle, a translate by a nonzero vector \(d\). When both components of \(d\) are nonzero, choose the corner of the translated rectangle whose outward normal cone points oppositely to both components. Any nonzero normal \(n\) in this cone has \(n\cdot d<0\), and the corresponding corner of the first rectangle lies strictly farther in the \(n\)-direction. For any other \(n\), some point of the translated rectangle lies farther. Thus the chosen corner has no supporting line and lies inside the convex hull of the two rectangles. If one component of \(d\) vanishes, any possible support at a trailing corner has normal perpendicular to \(d\) and contains an entire rectangle side, forcing a characteristic edge of the polygon.

Let \(r(t)\) be the radial function of the centered polygon in the characteristic plane. Its inscribed rectangles correspond to solutions \(0<t<\pi/2\) of \(r(t)=r(-t)\). This equation also holds at \(0,\pi/2\) by central symmetry. Take \(m\) isolated roots giving two-sided attractors and include the two endpoints. Each interval between successive selected angles must contain at least one vertex angle on one of the two folded boundary arcs. Otherwise the two radii on the interval are intersections with two fixed straight lines, one reflected. Agreement at the distinct endpoint rays forces the lines to coincide and hence contributes a continuum of periodic points adjacent to a selected attractor. The two arcs lie in the right half-plane, which has at most \(h\) vertices with angles projecting into these open intervals. Thus \(m+1\le h\). A collapsed rectangle retraces through a fixed point of a chord involution, so its orbit is its own time reverse and cannot be a two-sided attractor. **∎**

## The complete equal-slope slice of every even regular polygon

**Theorem 3.** Let \(N=2h\ge4\) and \(s=1\). In characteristic coordinates the change of axes is a Euclidean rotation by \(-\pi/4\) and a uniform dilation. Let \(\beta\) be a vertex angle in these coordinates, reduced to \([0,\pi/N]\) by the polygon's rotations and reflection of the coordinate frame. For \(0<\beta<\pi/N\), there are exactly \(h-1\) attracting period-two cycles. Their rectangles have northeast angles \(t_j=j\pi/N\) and exponents
\[
 \varepsilon_j=
 \begin{cases}\beta,&j\text{ odd},\\ \beta-\pi/N,&j\text{ even},\end{cases}
 \qquad
 \Lambda_j=-\left|\log\frac{\tan(t_j+\varepsilon_j)}
                             {\tan(t_j-\varepsilon_j)}\right|,
 \qquad 1\le j<h .
\]
At \(\beta=0,\pi/N\) the two geometric axis reflections preserve the polygon. At a noncharacteristic such alignment, their product is the half-turn and \(b^2=\mathrm{Id}\). At an alignment with a characteristic edge, the same identity holds for the geometric-reflection extension, and a tangent ray on that wall requires a specified convention.

**Proof.** The radial function of a regular polygon has period \(2\pi/N\), is even about each dihedral symmetry axis, and is strictly monotone between consecutive axes. Consequently \(r(t)=r(-t)\) means that \(t-\beta\) and \(-t-\beta\) are equal modulo \(2\pi/N\) up to sign. At generic \(\beta\), this gives \(t=j\pi/N\). Proposition 2 identifies these roots with all nondegenerate rectangles. The contact angles are strictly between vertex angles. The outward edge normal at each of \(t_j,-t_j\) has angle \(t_j+\varepsilon_j,-t_j+\varepsilon_j\), respectively. An edge with normal at angle \(\eta\) has slope \(du/dv=-\tan\eta\). Central symmetry makes the slope at the opposite corner identical. Hence the value of \((b^2)'\) on the southwest diagonal orbit is
\[
 \left(\frac{\tan(t_j-\varepsilon_j)}{\tan(t_j+\varepsilon_j)}\right)^2 .
\]
Taking the smaller reciprocal and dividing its logarithm by two gives the result. A period-two retracing orbit would require the two opposite \(u\)- or \(v\)-support vertices to lie on a coordinate axis. The generic orientations exclude this possibility. Thus these \(2(h-1)\) diagonal cycles, counting both stability types, exhaust all periodic points. **∎**

**Large \(N\) on this slice.** Fix \(0<\tau<1\) and \(\beta=\tau\pi/N\). For \(t_j\) in a compact subinterval of \((0,\pi/2)\), the per-step focusing magnitude is \(O(1/N)\). On the first rectangle it tends to \(\log((1+\tau)/(1-\tau))>0\). The equal-weight average over all attracting cycles is
\[
  \frac1{h-1}\sum_{j=1}^{h-1}|\Lambda_j|
   =\frac{4\log N+O_\tau(1)}{N}.
\]
To see the last assertion, write \(\log\tan t=\log t-\log(\pi/2-t)+g(t)\), where \(g'\) is bounded on the closed interval by endpoint expansion. Put \(a_j=\tau\) for odd \(j\) and \(a_j=1-\tau\) for even \(j\). The \(j\)th positive summand becomes
\[
 \log\frac{j+a_j}{j-a_j}
 +\log\frac{h-j+a_j}{h-j-a_j}+O(N^{-1}).
\]
The first logarithm is \(2a_j/j+O_\tau(j^{-3})\). Its sum is \(\log N+O_\tau(1)\) by the alternating harmonic series. Reversing the index gives the same leading term for the second logarithm. This is an average over attracting cycles at the single frequency \(\lambda=1/\sqrt2\).

### A finite focusing rate after an arbitrarily small octagon tilt

Take a regular octagon with one physical vertex vertically above the origin, \(s=1\), and rotate the tank by \(\phi\in(0,\pi/8)\). Its characteristic vertex angle reduces to \(\beta=\phi\). At zero tilt the directions are transverse to all walls, \(b^2=\mathrm{Id}\), and every exponent is zero. For each positive tilt, the \(j=2\) cycle has
\[
  \lim_{\phi\downarrow0}\Lambda_2
   =\log\frac{\tan(\pi/8)}{\tan(3\pi/8)}
   =-2\log(1+\sqrt2)
   =-1.7627471740390860505\ldots .
\]
Its four impacts approach four vertices of the untilted octagon. The two other attracting exponents approach zero.

The basin of this finite-rate cycle covers exactly one quarter of the boundary when weighted by polar angle around the tank center. Its two stable points have characteristic polar angles \(-\pi/4,3\pi/4\). The neighbouring repellers are at \(-3\pi/8,-\pi/8\) and \(5\pi/8,7\pi/8\). On each intervening component \(b^2\) is increasing with no other fixed point, so every point between those repellers converges to the intervening attracting point. The two angular intervals total \(\pi/2\). The other two basins each have angular proportion \(3/8\). These measures refer to boundary launch position with uniform polar angle.

## Odd regular polygons attain the global bound at equal slopes

**Theorem 4.** For every odd \(N\ge5\) and \(s=1\), a regular \(N\)-gon with no characteristic edge has exactly \(N-3\) two-sided attracting cycles, all of period two. Put \(\delta=\pi/N\). Rotating the characteristic axes by a multiple of \(\pi/2\), and relabelling the polygon's vertices, reduces a vertex angle to \(0<\beta<\delta/2\). Indeed \(N\) is odd, so these quarter-turns generate the shifts by \(\delta/2\) modulo \(2\delta\). Interchanging the two foliations reverses time and exchanges each attracting diagonal cycle with its reciprocal repelling cycle. For \(l=0,\ldots,N-4\), put
\[
 t=(1+l/2)\delta,\qquad
 (a,b_0)=
 \begin{cases}
 (\delta-\beta,\ \beta),&l\text{ even},\\
 (\delta/2+\beta,\ \delta/2-\beta),&l\text{ odd}.
 \end{cases}
\]
The attracting round-trip multiplier and the per-step exponent are
\[
 M_l=\frac{\tan(t-a)\tan(t+b_0)}{\tan(t-b_0)\tan(t+a)},\qquad
 \Lambda_l=\tfrac12\log M_l .
\]
The excluded angles \(\beta=0\bmod(\delta/2)\) have a characteristic edge and a characteristic reflection symmetry. With geometric reflection on the tangent edge, that reflection commutes with the other chord involution and \(b^2=\mathrm{Id}\).

**Proof.** Scale the apothem to one. Reflect the unit outward normal of every edge into the first quadrant by taking the absolute values of its two components. Record the original quadrant as a label. The oriented edge normals have arguments \(\beta+(2i+1)\delta\). Their folded arguments, in increasing order, begin
\[
 \underbrace{\beta}_{\rm SW},\
 \underbrace{\delta-\beta}_{\rm SE},\
 \underbrace{\delta+\beta}_{\rm NE},\
 \underbrace{2\delta-\beta}_{\rm NW},\
 \underbrace{2\delta+\beta}_{\rm SW},\ldots .
\]
Each suffix repeats the preceding label pattern until the \(N\) normals are exhausted. The \(l\)th window of four consecutive normals therefore has arguments \(t-a,t-b_0,t+b_0,t+a\), with \(0<b_0<a<\delta\), \(a+b_0=\delta\), and \(\delta\le t\le\pi/2-\delta\).

We construct an axis-parallel rectangle with one corner on each of these four edges. After folding the contact points by their respective quadrant signs, the two southwest/northwest contacts share their first coordinate, as do the southeast/northeast contacts. The two lower contacts share their second coordinate, as do the two upper contacts. Since the four labels are in cyclic order, the two outer tangent lines \(t-a,t+a\) share either a first or a second coordinate, and the two inner lines \(t-b_0,t+b_0\) share the other value of that same coordinate. In the latter-coordinate case interchange the axes. This reverses the order, replaces \(t\) by \(\pi/2-t\) and leaves all the inequalities on \(t\) valid. In this frame the outer pair shares one first coordinate, the inner pair another. The first two lines in increasing angular order share a second coordinate \(y-H\), and the last two share \(y+H\). These labels impose no sign on \(H\).

Write \(A=\cos t,\ B=\sin t,\ T=(A,B),\ E=(-B,A)\). For \(r=a,b_0\), let \(X_r=(x_r,y)\). The two contacts on the normals \(t\pm r\) have coordinates \(X_r\pm(0,H)\). Adding and subtracting their unit tangent-line equations gives
\[
 T\cdot X_r=\sec r-HA\tan r,\qquad E\cdot X_r=-HB\cot r.
\]
In particular \(y=B\sec r-HAB(\tan r+\cot r)\). Equating this expression for \(r=a,b_0\) gives a unique solution,
\[
 K=\frac{\sin(\delta/2)}
          {\cos\delta\cos((a-b_0)/2)},\qquad
 H=-\frac{K\sin a\sin b_0}{A}.
\]
The signed distance along each oriented tangent from its point of tangency to its computed contact is
\[
 w_+(r)=-\tan r+H(A/\cos r-B/\sin r),\qquad
 w_-(r)= \tan r-H(A/\cos r+B/\sin r).
\]
An actual polygon edge extends a distance \(\tan\delta\) from its point of tangency in each direction. For \(r'= \delta-r\) we have
\[
 \max(|w_+(r)|,|w_-(r)|)=w_-(r)
          =\tan r+K\sin r'(\tan r+\tan t)<\tan\delta .
\]
Indeed the strict inequality simplifies to
\(\sin(\delta/2)\sin(t+r)<\cos((a-b_0)/2)\cos t\).
The right side is at least \(\cos(\delta/2)\sin\delta>\sin(\delta/2)\). Thus all four contacts lie strictly inside their assigned edges. They also have positive folded coordinates. At \(t-r\) the positive \(w_-\) puts the contact angle between \(t-r\) and \(t-r+\delta\), inside the first quadrant. This proves \(x_r>0\) and \(y-H>0\). At \(t+r\) the contact angle is between \(t+r-\delta>0\) and \(t+r+\delta<\pi\), proving \(y+H>0\). Unfolding now gives a nondegenerate rectangle.

For each reflected edge the magnitude of \(du/dv\) is \(\tan\) of its folded angle. The alternating product of the four slopes and its reciprocal give the two diagonal multipliers. Their smaller value is \(M_l<1\) as displayed. Swapping axes preserves that quotient because \(\tan(\pi/2-x)=1/\tan x\). Different windows use different sets of open edges, hence produce distinct rectangles. There are \(N-3\) windows, which saturates Theorem 1. **∎**

For fixed \(\beta/\delta=\tau\in(0,1/2)\) and \(N\) increasing through odd integers, the equal-weight mean is
\[
 \frac1{N-3}\sum_l |\Lambda_l|
   =\frac{2\log N+O_\tau(1)}{N}.
\]
Apply the expansion of \(\log\tan t\) in Theorem 3 to the two differences across \([t-a,t-b_0]\) and \([t+b_0,t+a]\). The contribution from the endpoint \(t=0\) in the \(l\)th term is \(2(a-b_0)/(\delta(l+2))+O_\tau((l+2)^{-3})\). The ratios \((a-b_0)/\delta\) alternate between \(1-2\tau\) and \(2\tau\), so this endpoint supplies \(\log N+O_\tau(1)\) after summation. The endpoint at \(\pi/2\) contributes the same amount. The bulk rates are \(O(1/N)\) for \(t\) bounded away from both ends, while the first focusing magnitude tends to
\(\tfrac12\log((1-\tau)(2-\tau)/(\tau(1+\tau)))>0\).

### Standing waves at the edge-parallel alignment

For a generic odd regular polygon at \(s=1\), the standing-wave eigenspace at \(\lambda^2=1/2\) is zero. Here is a geometric verification of the neutral-cylinder obstruction. In any circumscribed polygon with incircle of radius one in the characteristic plane, let \(p,q,r,d>0\) be the absolute slopes of the outward normals of the southwest, southeast, northeast and northwest contact edges of an inscribed rectangle. The signs of each normal agree with its corner quadrant because the rectangle lies inside the four supporting half-planes. Write \(F(t)=\sqrt{1+t^2}\). The four tangent equations for the signed half-plane coordinates are
\[
\begin{split}
 X_-+pY_-&=F(p),\qquad X_++qY_-=F(q),\\
 X_++rY_+&=F(r),\qquad X_-+dY_+=F(d).
\end{split}
\]
A cylinder would have a subinterval with fixed edge labels, since only finitely many initial points hit a vertex in four half-steps. A continuum of solutions of these four equations forces \(pr=qd\). Put \(q=hp,\ r=hd\). Subtracting \(h\) times the left-column equations from the right-column equations gives \(G_h(p)=G_h(d)\), where \(G_h(t)=F(ht)-hF(t)\). For \(h\ne1\), \(G_h'(t)=ht(h/F(ht)-1/F(t))\) has constant nonzero sign on \(t>0\). Therefore either \(p=d,\ q=r\), or \(h=1\) and \(p=q,\ r=d\). Each alternative requires two pairs of equal folded normals. In the generic odd regular polygon all folded normals are distinct. This excludes a nondegenerate periodic cylinder and hence, by the finite-energy criterion, any \(H_0^1\) eigenmode. Generic even regular polygons have the same zero eigenspace by Theorem 3, which gives a finite periodic set. [Finite-energy criterion](phase1_pde.md)

At the critical odd-\(N\) alignment \(\beta=0\), suppose the circumradius is one. The polygon is symmetric under \(v\mapsto-v\) and has a vertical characteristic edge with endpoint heights \(\pm\sin\delta\). Denote its upper half-height at \(u\) by \(Y(u)\). For any smooth bump \(h\) supported in \((\sin\delta,\max Y)\) away from all corner heights, the function
\[
 w(u,v)=h(Y(u))-h(|v|)
\]
vanishes on the full boundary, including the vertical edge. It is smooth in the polygon, belongs to \(H_0^1\), and solves \(w_{uv}=0\). The interval of bump heights is nonempty for every \(N\ge5\), since a vertex within \(\delta\) of the positive vertical axis has height at least \(\cos\delta>\sin\delta\). Taking disjoint bump supports gives infinitely many independent solutions. At positive tilt, the \(l=0\) branch satisfies
\[
 M_0=
 \frac{\tan\beta\,\tan(\delta+\beta)}
      {\tan(\delta-\beta)\,\tan(2\delta-\beta)}
 \ \sim\ \beta\cot(2\delta)
 \quad(\beta\downarrow0,\ N\text{ fixed}).
\]
Thus a tilt of arbitrarily small positive size both removes this eigenspace and produces a per-step exponent tending to \(-\infty\). The reference orientation has a characteristic edge. Both characteristic directions in the untilted octagon are transverse to every edge.

## Which symmetries force equal focusing rates?

For a tank with a vertical or horizontal reflection \(S\), that reflection interchanges the two characteristic foliations. The orientation-preserving circle map \(H=\gamma^+ S\) satisfies \(H^2=b\). It takes an attractor to an attractor with the same stability. For a regular cycle the local exponents agree because \(H\) is locally affine with nonzero derivative at the orbit points. More generally a piecewise-affine bi-Lipschitz conjugation preserves a one-sided exponential rate, with the corresponding side transported by \(H\).

If \(q\) is even, \(H\) must take each \(q\)-cycle to a different one, since restricting \(H=b^\ell\) to an invariant orbit would require \(2\ell\equiv1\pmod q\). Squaring shows that the resulting pairs are disjoint. Different pairs can have different rates, even when the same physical tank has both horizontal and vertical symmetry.

For the numerical table let \(V_j=(\cos\alpha_j,\sin\alpha_j)\) with \(\alpha_j=\pi/2+\phi+2\pi j/N\). Positive \(\phi\) is a counterclockwise tilt from a vertex-up polygon. The count at \(N=5,9\) saturates Theorem 1, while at \(N=6,8,10\) it saturates Proposition 2. All rows have period two.

| \(N\) | \(\phi\) | \(s\) | Attractors | Per-step exponents |
|---:|---:|---:|---:|---|
| 5 | \(0^\circ\) | \(9/10\) | 2 | \(-1.119139721\) twice |
| 5 | \(5^\circ\) | \(9/10\) | 2 | \(-2.315915973,\ -0.517344809\) |
| 6 | \(0^\circ\) | \(9/10\) | 2 | \(-1.521438093\) twice |
| 6 | \(5^\circ\) | \(9/10\) | 2 | \(-2.238415740,\ -0.989725581\) |
| 8 | \(5^\circ\) | \(19/20\) | 3 | \(-1.307924075,\ -0.612922879,\ -0.394192178\) |
| 9 | \(0^\circ\) | \(49/50\) | 6 | \(-0.853185884,\ -0.425836072,\ -0.390044045\), twice each |
| 10 | \(0^\circ\) | \(19/20\) | 4 | \(-0.983975700,\ -0.712758345\), twice each |

### Pentagon certificate

Write edge \(i=[V_i,V_{i+1}]\) in characteristic coordinates as \(u=A_i+B_iv\). If \((i_0,i_1,i_2,i_3)\) are the southwest, southeast, northeast and northwest contact edges in order, the two row heights \(v_0,v_1\) satisfy
\[
 A_{i_0}+B_{i_0}v_0=A_{i_3}+B_{i_3}v_1,\qquad
 A_{i_1}+B_{i_1}v_0=A_{i_2}+B_{i_2}v_1 .
\]
They determine a single rectangle whenever the denominator is nonzero and the solution satisfies the strict contact inequalities. Differentiation gives its exact algebraic round-trip multiplier on the southwest diagonal
\[
 M_{\rm SW}=\frac{B_{i_1}B_{i_3}}{B_{i_0}B_{i_2}},\qquad
 B_i=\frac{\sin\eta_i+s\cos\eta_i}{\sin\eta_i-s\cos\eta_i},\qquad
 \eta_i=\pi+\phi+(2i+1)\pi/N .
\]
At \(N=5,\ \phi=\pi/36,\ s=9/10\) the two edge sequences are \((2,3,0,1)\) and \((2,3,4,1)\). For the first, the four contact fractions measured from the initial vertex of each directed edge lie, respectively, in
\((.570,.571),(.449,.451),(.292,.294),(.012,.014)\).
For the second they lie in
\((.080,.082),(.962,.965),(.167,.170),(.858,.861)\).
The corresponding attracting multipliers are
\[
 0.0097369052787069466536826441230703326897\ldots,\qquad
 0.3553366536280175824951662911393568516056\ldots .
\]
Thus the preliminary \(-2.316\) and \(-0.517\) are already normalized per application of \(b\). At zero tilt the common exponent is \(-1.1191397206810692977\ldots\). Differentiating the displayed edge formula at zero gives opposite derivatives
\(-8.1610429463265227453\ldots\) and \(+8.1610429463265227453\ldots\) per radian, respectively. Both impacts remain in their edge interiors for small tilt, so these pentagon branches split continuously. The discontinuity in the octagon arises when the limiting orbit hits vertices.

## Reproduction and literature

Run the companion Python program with mpmath installed. It uses exact rational arithmetic to enumerate all regular hyperbolic rectangles for the sharp examples with four through eleven sides. At the regular polygons in the table, it uses 85-decimal outward interval arithmetic to enclose the coordinates, check every strict contact inequality, and evaluate the attracting multipliers. Each printed interval value is rounded independently at both endpoints and displayed only when those rounded values agree. It also checks both regular-polygon formulas against independently solved chord equations at selected even \(N\) through 32 and odd \(N\) through 51. [Reproducible computation](../experiments/phase1_multiple.py)

Nogueira and Troubetzkoy give a \(3k-4\) upper bound for periodic cylinders, including neutral ones, in Proposition 11. The sharp \(k-3\) result here counts two-sided attracting cycles using paired gap orbits. Hanusa and Mahankali give an explicit square cycle for a range of opposite slopes in §6.2. Their Questions 7.5 and 7.11 concern the existence and uniqueness of rigid cycles and their behavior under perturbation of the board. The polygon constructions and octagon limit give specific answers to those questions. [Nogueira–Troubetzkoy](https://arxiv.org/abs/2007.14773) · [Hanusa–Mahankali](https://arxiv.org/html/1901.01917)
