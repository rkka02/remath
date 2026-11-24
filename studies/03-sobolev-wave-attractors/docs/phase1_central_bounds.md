# The cost of a neutral cylinder in a centrally symmetric polygon

Fix two characteristic directions transverse to the sides of a convex polygon. Choose linear coordinates \((u,v)\) parallel to them. Write \(b=VH\) for the boundary map that first takes a horizontal chord and then a vertical chord. A regular four-reflection loop is an inscribed rectangle whose four contacts lie in edge interiors. Its two diagonals give two period-two boundary orbits with reciprocal multipliers. We count the attracting orbit once.

**Theorem.** Suppose a centrally symmetric \(2h\)-gon has a neutral cylinder of four-reflection loops. The number of regular attracting four-reflection loops is at most \(\max(0,h-3)\). For every \(m\ge1\), precisely \(2m+6\) sides suffice to realize \(m\) such attractors together with a neutral cylinder. Their \(m\) contraction factors can be prescribed independently. In particular, eight is the smallest central side count for coexistence at this period.

## A one-dimensional envelope

Put the center at the origin and write \(C=-I\). If \(b\) has a primitive two-cycle, its rotation number is \(1/2\). In normalized boundary arclength \(C\) translates by \(1/2\). A lift \(F\) of \(b\) satisfies \(F(x+1/2)=F(x)+1/2\), since commutation modulo integers first gives a constant integer discrepancy and doubling gives zero. Thus \(Cb\) has rotation number zero. Every periodic point of an orientation-preserving circle map of rotation number zero is fixed. Since \((Cb)^2=b^2\), each two-cycle comprises \(p,-p\). The two remaining impacts of its rectangle are also antipodal. Every regular rectangle therefore has corners \((\pm u,\pm v)\) for some \(u,v>0\).

Represent the polygon as the intersection of its \(h\) pairs of supporting half-planes,

\[
 |a_i u+\sigma_i b_i v|\le1,\qquad a_i,b_i>0,\qquad \sigma_i\in\{+1,-1\}.
\]

Transversality gives the strict inequalities on the normal components. At \(t>0\), the positive horizontal coordinates of the boundary on the rays \(v=\pm tu\) are \(1/Q_\pm(t)\), where

\[
 Q_\pm(t)=\max_i |a_i\pm\sigma_i b_i t|,\qquad
 E(t)=\max_i(a_i+b_i t)=\max\{Q_+(t),Q_-(t)\}.
\]

The rectangle condition is \(Q_+(t)=Q_-(t)\). Since \(|a_i-b_i t|<a_i+b_i t\), equality holds exactly when among the lines attaining \(E(t)\) at least one has each sign \(\sigma_i\). A regular isolated rectangle uses one supporting edge on each of the two rays. Its two lines have opposite signs and different slopes. They exchange dominance at their crossing, which is a breakpoint of the upper envelope.

A neutral cylinder gives an open interval of \(t\) with equality. Indeed its corner in the first quadrant moves along a boundary arc, on which the radial angle is strictly monotone. Inside an open piece of the envelope, equality throughout requires two identical lines of opposite signs. Thus the envelope has at most \(h-1\) distinct affine pieces. Every line can supply at most one piece, by convexity of its set of dominance. If there are at least two pieces, at least one breakpoint abuts a neutral piece and cannot represent an isolated attracting loop. With \(P\) pieces this leaves at most \(P-2\le h-3\) regular attracting loops. A single piece allows none in the presence of a neutral cylinder. Without the neutral requirement the same argument gives the upper bound \(h-1\).

## A construction with prescribed rates

Choose \(0<t_1<\cdots<t_m<t_{m+1}\) and desired full-return multipliers \(0<\kappa_i<1\). The values \(t_i\) prescribe the ratios \(v/u\) at the northeast corners. Choose \(p_0,a_0>0\), set \(p_i=p_{i-1}/\sqrt{\kappa_i}\) for \(1\le i\le m\), and choose any \(p_{m+1}>p_m\). Define

\[
 a_i=a_{i-1}\frac{1+p_{i-1}t_i}{1+p_i t_i},\qquad
 b_i=a_i p_i\quad(0\le i\le m+1),
\]

where the recurrence for \(a_i\) starts at \(i=1\). The lines \(a_i+b_i t\) have strictly decreasing intercepts and strictly increasing slopes. Consecutive lines intersect at \(t_i\). Since those crossings occur in ascending order, every line supplies the entire envelope between its neighboring crossings. This follows by successive comparison against all earlier and all later lines.

Give the lines \(i=0,\ldots,m\) alternating signs and give the final line \(i=m+1\) both signs. Use the resulting \(m+3\) strips in the half-plane representation above. Each strip uniquely supports the polygon along an open sector of one of the two rays, together with its antipodal sector, so the polygon has exactly \(2m+6\) genuine sides. At \(t_i\), \(1\le i\le m\), exactly one edge is active on each ray and the four contacts are regular. The two absolute edge slopes \(|du/dv|\) are \(p_{i-1}\) and \(p_i\). Horizontal chords preserve \(v\), vertical chords preserve \(u\), and opposite edges have the same slope. The two full-return derivatives are therefore \((p_{i-1}/p_i)^2=\kappa_i\) and its reciprocal. The range \(t>t_{m+1}\) gives the neutral cylinder. For rational input locations and rational square roots of the multipliers, rational choices of the auxiliary parameters produce rational vertices.

There is also a realization with prescribed *row half-heights* instead of radial ratios. Take the right wall \(u=R(v)\) of the construction with prescribed heights and multipliers and set its left wall to \(u=-R(-v)\). The rectangle equation remains \(R(y)=R(-y)\), and its full-return derivatives are the squares of the previous derivatives. Input rates \(\sqrt{\kappa_i}\) therefore give the requested rates \(\kappa_i\). Each wall has \(m+3\) edges. [Explicit right-wall construction](phase1_coexistence.md)

For the octagon with rational vertices, take \(-1\le v\le1\) and

\[
 R(v)=\min\{1-|v|,\,2/3+v/3,\,3/4-2v/3\},\qquad -R(-v)\le u\le R(v).
\]

The rectangle \([-7/12,7/12]\times[-1/4,1/4]\) has attracting multiplier \(1/4\). The rectangles with half-heights \(3/4<y<1\) form a neutral cylinder. At physical slope one, take \(u=z+x,\ v=z-x\). Every \(g\in C_c^\infty((3/4,1))\), extended by zero, gives the smooth Dirichlet mode \(g(1-|u|)-g(|v|)\) at \(\lambda^2=1/2\). The boundary equality follows from the unchanged outer walls and \(R(v)\ge1/4\) on \([-3/4,3/4]\).

## Quadrilaterals at arbitrary periods

At transverse directions, in any convex \(k\)-gon the presence of a neutral periodic cylinder and \(m\ge1\) regular attracting cycles forces \(k\ge m+4\), for any primitive period \(q\). To see this, mark the \(m\) attracting orbits, their \(m\) distinct repelling reverses, a generic neutral orbit \(N\) and its reverse \(H N\). Choose \(N\) away from vertices and the finitely many fixed points of \(b^jH\), \(0\le j<q\), so the last two marked orbits are distinct. All marked orbits have the same least period by the rotation number. Existence of a regular attractor forces \(q\ge2\), and the four extremal vertices of the coordinate projections are distinct. Each is fixed by a chord involution and lies outside the marked set.

There are \(2(m+1)\) orbit labels in boundary order, and equally many labels for the gaps between consecutive marks. On the orbit labels \(H\) acts by \(i\mapsto d-i\) with \(d\) odd, since all reverse marks are paired. On gap labels it acts by \(i\mapsto d-i-1\), with precisely two fixed labels. The other involution \(V=bH\) induces the same action on the labels. The four extrema lie in the fixed gap classes. Each of the remaining \(m\) gap pairs must contain a vertex. Indeed, a gap between the two neutral labels is reversal-invariant, so each noninvariant gap abuts a hyperbolic mark. If its entire gap pair contained no vertex, all half-steps of \(b^q\) would be affine on the chosen gap. The return fixes both endpoints and would be the identity there, contradicting its hyperbolic endpoint. The \(m\) extra vertices are distinct from each other and from the four extrema. [Underlying cyclic gap argument](phase1_multiple.md)

At a characteristic direction of a quadrilateral, at least one of the four coordinate-support faces contains two vertices. Pairwise disjoint faces would require at least five vertices. Hence two faces of different coordinates share a weak extremum. This forces every finite-energy Dirichlet mode to vanish and precludes any neutral cylinder whose full orbit avoids the tangent faces. Intervals of periodic points defined by reflecting a tangent edge in its midpoint can still occur. For example, the midpoint extension on a characteristic-coordinate rectangle satisfies \(b^2=\mathrm{Id}\). [Weak-extremum theorem and critical-mode criterion](phase1_pde.md)
