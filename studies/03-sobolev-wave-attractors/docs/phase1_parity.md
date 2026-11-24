# Tilted rectangles, parity and full measure at fixed tilt

Let a rectangle of side lengths $1,R$ be tilted by $0<\phi<\pi/4$. Let $\theta$ be the angle of the *physical characteristic line* with the horizontal. For the operator in this study, $\lambda=\cos\theta$. In the supercritical interval $\phi<\theta<\pi/2-\phi$, set

$$
a=\frac{\tan(\theta-\phi)}R,\qquad b=\frac{\tan(\theta+\phi)}R,\qquad \mu=b/a>1.
$$

Both $a,b$ strictly increase with $\theta$. Wall-aligned coordinates with each side rescaled to length one give physical ray slopes $a,-b$. Reflection across successive grid edges unfolds the ray to a northeast graph whose slopes alternate between $a$ on the even cells and $b$ on the odd cells of the unit checkerboard. The parity of the cell with lower left corner $(i,j)$ is that of $i+j$. The integral curve through a grid vertex has an unambiguous continuation as a northeast graph, the continuous extension of the regular trajectories. The interpretation of a ray hitting a physical corner uses this convention only where specified.

## The exact two-slope return

Quotient the checkerboard by the lattice $L=\{(i,j)\in\mathbb Z^2:i+j\text{ even}\}$. The section $x=0$ has vertical coordinate $y\pmod 2$. Write $S(y)=a$ on $(0,1)$ and $S(y)=b$ on $(1,2)$, extended with period two. Put

$$
T(y)=\int_0^y \frac{dt}{S(t)},\qquad Z(y)=\frac1{a+b}\int_0^y S(t)\,dt.
$$

After crossing one column the height is $H(y)=T^{-1}(T(y)+1)$. Translating back by $(1,1)$ gives the quotient return $f(y)=H(y)-1$. The coordinate $z=Z(y)\pmod1$ gives the lift

$$
g(z)=h_\mu(z)+\frac{b(a-1)}{a+b},\qquad
h_\mu(z)=\begin{cases}\mu z,&0\le z\le 1/(1+\mu),\\ 1+\mu^{-1}(z-1),&1/(1+\mu)\le z\le1.\end{cases}
$$

Indeed $Z(y-1)=abT(y)/(a+b)-b/(a+b)$, and $abT(y)/(a+b)=h_\mu(Z(y))$. This section identifies the tilted rectangle with the reciprocal-slope family in Appendix A of Lenci, Bonanno and Cristadoro. In their notation the dilation parameter is $M=b/(a+b)>1/2$ and the projective direction is $s=ab/(a+b)>0$. Their translation $s+1-M$ differs from the displayed lift translation $s-M$ by one. The chess-billiard boundary section and this vertical section have different return times. [Lenci, Bonanno and Cristadoro, §3 and Appendix A](https://arxiv.org/html/2102.01654)

## Rational winding and the physical period

Let the mean unfolded rise per unit horizontal distance be $n/m>0$, in lowest terms. The normalized translation number of $f$ is $(n-m)/(2m)$, since each column subtracts one unit of height on a circle of length two. A periodic orbit of $f$ has primitive period

$$
r=\begin{cases}m,&m,n\ \text{both odd},\\2m,&m,n\ \text{of opposite parity}.\end{cases}
$$

The physical marked ray lives on $\mathbb R^2/(2\mathbb Z)^2$, a double cover of $\mathbb R^2/L$. Its winding vector is $(2m,2n)$. A regular closed ray encounters $2(m+n)$ walls, hence the period of the two-chord boundary map is $q=m+n$. For the usual counterclockwise boundary orientation and positive-slope chord first, the boundary rotation is $m/(m+n)$. To see the numerator, the lift of the counterclockwise boundary section is the staircase through $(0,0),(1,0),(1,-1),(2,-1),(2,-2)$, repeated by its period $(2,-2)$. Consecutive northeast sections differ by $(0,2)$. After $q$ returns the excess displacement is $(2m,2n)-q(0,2)=m(2,-2)$. Reversing the convention gives $n/(m+n)$. This computation extends to corner parameters by continuity. In a globally periodic case one may choose a regular starting point at the original parameter.

The quotient $f$ obeys $JfJ=f^{-1}$ for $J(y)=-y\pmod2$. Geometrically, central inversion of the unfolded plane reverses the foliation. Algebraically $S(-y)=S(y+1)$ away from integers, and $T(1-y)=T(1)-T(y)$, which gives the same identity. At regular points,

$$
f'(y)=\frac{ab}{S(y)S(f(y))}.
$$

For a regular point of an $r$-cycle $O$ this gives $D f^r=\mu^{N_A-N_B}$, where $N_A,N_B$ count visits to the two open semicircles $A=(0,1), B=(1,2)$. Two distinct cycles of a circle homeomorphism with reduced rotation of denominator $r$ interlace, since the action transitively permutes the gaps of either cycle. Applied to $O,JO$, this implies $|N_A-N_B|\le1$, as $J$ exchanges the semicircles. If $O=JO$, its regular points occur in pairs contributing one of each type. If a cycle contains an integer, it is $J$-invariant. On a cyclically ordered set of $r$ points an orientation-reversing involution with a fixed point has one fixed point for odd $r$ and two for even $r$. The only possible fixed points of $J$ are $0,1$. Since $f$ preserves order, one-sided derivatives are counted by assigning every integer consistently to its right or left semicircle.

- For even $r$ every periodic point has two one-sided return derivatives equal to one. Each fixed point of the reduced lift of $f^r$ therefore has a neighborhood of fixed points, by finite piecewise affinity. Its fixed set is nonempty, open and closed. Consequently $f^r=\mathrm{Id}$ as a circle map, and the physical boundary map obeys $b_\lambda^q=\mathrm{Id}$. These are precisely the attained rational boundary rotations with **odd $q$**.
- For odd $r$ every regular periodic point has multiplier $\mu$ or $\mu^{-1}$. A periodic orbit through an integer has opposite one-sided exponents $+1,-1$. A translated column lift with a neutral interval would contain a regular fixed point of derivative one, so this is impossible. The physical full cycle goes twice around the quotient orbit, giving the attracting multiplier **$\mu^{-2}$** and per-boundary-step exponent **$-2\log\mu/q$** for every regular attractor. These are precisely the attained rational boundary rotations with **even $q$**.

Strict parameter order follows directly from the defining column integral. For fixed initial height, increasing both $a,b$ strictly decreases the horizontal distance required to reach any prescribed larger height. Thus the lifted column endpoint and every positive iterate strictly increase. A globally periodic rational rotation is attained at only one angle. Comparison of its iterate at a different angle gives a strict uniform displacement gap by compactness. A rational rotation whose iterate is not the identity occurs on a nondegenerate parameter interval if attained within the open domain. At any zero of the iterate displacement one can move the parameter to create either sign, while preserving a strict sign already present elsewhere. Inside this parameter interval both displacement signs occur, so there is a sign-changing zero. An orbit through an integer has coincident displacement signs on its two sides and cannot be such a zero. The tongue interior consequently has a regular attractor and repellor. Endpoints can carry a corner orbit. More precisely Lenci, Bonanno and Cristadoro's Proposition 3.1 and Theorem 2.2 give the global attractor and repellor for this return. The argument here specifies the different parity and the squared multiplier on the physical boundary. [Lenci, Bonanno and Cristadoro](https://arxiv.org/html/2102.01654)

## Every fixed tilt has full-measure attraction

For every $R>0$ and every $0<\phi<\pi/4$, almost every supercritical $\theta$ has a regular periodic attractor. This fixed-rectangle assertion needs a slice argument because $M$ varies with the wave frequency. The following proof applies to any smooth one-parameter curve along which $0<a<b$ and both slope derivatives are positive.

**The exceptional set in a fixed dilation surface.** Appendix A of Lenci, Bonanno and Cristadoro shows that directions in the domain of discontinuity of the group generated by $s\mapsto s+1$ and $s\mapsto s/(Ks+1)$, with $K=1/[M(1-M)]$, have an attracting and a repelling cycle. Their fundamental interval (A.8) lies strictly inside the fixed-point tongue $(1-M,M)$ for $M>1/2$, and the affine symmetries transport these hyperbolic cycles. Consequently each exceptional direction belongs to that group's limit set. Use the coordinates

$$
v=\tfrac12\log(b/a)>0,\qquad t=\sqrt{ab},\qquad L_v=2\cosh v,
\qquad u=\log t.
$$

Here $L_v=\sqrt K$ and $t=L_vs$. In $t$-coordinates the group is a subgroup of the Hecke group generated by $A(t)=t+L_v$ and $J(t)=-1/t$, since the second generator is $JA^{-1}J$. The larger group's limit set contains all the exceptional parameters. [Lenci, Bonanno and Cristadoro, (A.5)–(A.8) and Remark A.4](https://arxiv.org/html/2102.01654)

**Real continued fractions.** Write $d=e^{-v}<1$, $D=[-d,d]$, and

$$
F_{k,v}(x)=-\frac{1}{kL_v+x},\qquad k\in\mathbb Z\setminus\{0\}.
$$

Each branch sends $D$ into $D$ and has Lipschitz constant at most $d^2$, since $L_v-d=1/d$. The intervals $F_{k,v}(D)$ are disjoint. The finite limit points of the Hecke group belong to the translates $k_0L_v+x$, with $k_0\in\mathbb Z$, where $x$ is either a finite word applied to $0$ or an infinite nested word in the branches. Indeed, use $i$ as an orbit basepoint and write a reduced group word as $A^{k_0}F_{k_1,v}\cdots F_{k_h,v}$, since an optional terminal $J$ fixes $i$. The closed complex unit disk is invariant under the branches, with uniform contraction at most $(L_v-1)^{-2}<1$. In any sequence with bounded real limit choose a constant $k_0$ subsequence. At each subsequent digit either there is a constant subsequence or the digit tends to infinity in absolute value, collapsing the tail uniformly to zero. Stabilization at every digit gives an infinite nested word by contraction. Finite words with all digits bounded cannot accumulate on the real line through a new value.

Any finite word interval $F_{k_1,v}\cdots F_{k_h,v}(D)$ contains a complementary gap of a uniformly positive relative size on every compact $v$-interval in $(0,\infty)$. As the initial gap use

$$
G_v=\left(-\frac{1}{L_v+d},-\frac{1}{2L_v-d}\right),
$$

between the $k=1,2$ images. Its relative width in $D$ has a positive minimum on the compact interval. The logarithm of each branch derivative has $x$-Lipschitz constant at most $2/(L_v-d)$. Summing these constants along a word with the geometric contraction factors bounds the logarithmic distortion independently of the word length. Its image of $G_v$ therefore retains a uniform positive fraction of the word interval. Translation by $k_0L_v$ preserves this fraction. On compact positive $t$-intervals, passing to $u=\log t$ also preserves a uniform positive lower bound.

**Transversality and moving gaps.** The endpoints of every word interval and its chosen gap are finite compositions applied to $d,-d$. Each such endpoint $t(v)\ne0$, including its outer translation $k_0L_v$, satisfies

$$
\left|\frac{d}{dv}\log|t(v)|\right|\le1.
$$

To verify this, start with $x=\pm d$ or $0$ and $|x'|\le|x|\le d$. For any $k\ne0$,

$$
\frac{|kL_v'+x'|}{|kL_v+x|}
\le \frac{|k|L_v'+d}{|k|L_v-d}\le1,
\qquad L_v-L_v'=2d.
$$

Taking a negative reciprocal preserves the logarithmic bound and maps back into $D$. The same estimate treats the final translation, while $k_0=0$ needs none. In particular, every positive marked endpoint is a 1-Lipschitz graph in the coordinates $(v,u)$.

Along the physical curve $u=(\log a+\log b)/2$ is strictly increasing, and

$$
\left|\frac{dv}{du}\right|=
\frac{|b'/b-a'/a|}{b'/b+a'/a}<1.
$$

The physical slice also has the explicit equation $\sinh v=\tan(2\phi)\cosh(u+\log R)$, obtained from $R(b-a)=\tan(2\phi)(1+R^2ab)$. On a compact subinterval take a uniform upper bound $\kappa<1$. For any marked positive endpoint graph $E(v)=\log t(v)$, the function $u-E(v(u))$ then grows at speeds between $1-\kappa$ and $1+\kappa$, in the sense of difference quotients. A finite code yields at most one parameter per compact subinterval. These parameters form a countable set.

Fix a point of the physical curve in an infinite nested sequence. For deep words its positive cylinder stays in a compact $t$-interval locally, by continuity of a fixed prefix. Let $I=[u_-,u_+]$ be the set of local parameters between its two moving endpoint graphs. For deep enough words both endpoints of $I$ exist in the chosen neighborhood. In fact the frozen width tends to zero at the specified point, and the crossing speeds are at least $1-\kappa$. For every $u\in I$, the width $W(v(u))$ between the two *frozen* endpoint heights satisfies

$$
(1-\kappa)|I|\le W(v(u))\le(1+\kappa)|I|.
$$

This follows by adding the distances to the two endpoint graphs at $u$, and comparing each with its distance to the appropriate crossing parameter $u_-,u_+$. The same inequalities apply to the interval $I_G\subset I$ cut out by the two moving gap endpoints. At any $u\in I_G$, the frozen gap occupies at least a fraction $c>0$ of the frozen cylinder, by bounded distortion. Hence

$$
|I_G|\ \ge\ c\,\frac{1-\kappa}{1+\kappa}\,|I|.
$$

The interior of this parameter gap misses the entire limit set. Distinct outer translates are disjoint, since $L_v>2d$, and images of distinct branch interiors are disjoint at every depth. The intervals $I$ shrink to the specified parameter. The Lebesgue density theorem now excludes positive measure for the infinite-code intersections. A countable cover of the open angular interval proves the assertion. This argument uses a uniform relative gap after crossing the moving cylinder.

Thus the angular measure of regular periodic-attractor frequencies **inside the supercritical window** is exactly $\pi/2-2\phi$. The complementary two open corner-attraction windows have angular measure $2\phi$. In Lebesgue measure of the physical frequency $\lambda=\cos\theta$, the respective values are $\cos\phi-\sin\phi$ and $1-\cos\phi+\sin\phi$. At $\phi=0$ every regular ray is neutral or aperiodic, with zero attracting-frequency measure. The limit of the regular periodic-attractor frequency measure as $\phi\downarrow0$ is one, independent of $R$.

## Point spectrum at fixed geometry

The primitive $n/m=1$ tongue is exactly $a<1<b$, with a corner cycle at $a=1$ or $b=1$. Within it, the lifted ray from $(0,y)$ to $(1,1+y)$ crosses the horizontal line $y=1$ and obeys $y=b[1-(1-y)/a]$, giving $y=b(1-a)/(b-a)\in(0,1)$. Inversion gives the other cycle. If $b<1$ or $a>1$, all local slopes lie strictly on one side of one, so the mean slope differs from one. Every positive $R$ has some angle inside the tongue, since the interval $(\arctan R-\phi,\arctan R+\phi)$ intersects the supercritical window. The latter is entirely inside this tongue exactly when

$$
\cot(2\phi)\le R\le\tan(2\phi).
$$

In this aspect range no supercritical frequency has a neutral cylinder. Outside the range, continuity of the mean winding gives a nontrivial interval of values between one and a different winding. Reduced fractions of mixed parity are dense. Each gives a different globally periodic frequency, whose eigenspace is infinite dimensional by the polygonal energy criterion. Conversely, each eigenfrequency must be globally periodic here. The rational mixed windings are countable and each is attained at only one angle. The subcritical dynamics has attracting corners. At a critical angle choose coordinates so the characteristic variables are $y,y+kx$, $k>0$, on the unit square, interchanging or reversing the axes when needed. For $u=F(y)+G(y+kx)$, boundary traces at $x=0,1$ imply $G(y)=G(y+k)$ for $0<y<1$, and the bottom trace makes $G$ constant on $(0,k)$. Translation propagates this across $(0,1+k)$. The same conclusion follows distributionally by tangential differentiation and does not require endpoint values of $F,G$. At $\lambda=0,1$, the energy identity implies one weak coordinate derivative of a Dirichlet mode vanishes, so the mode is zero. Consequently the point spectrum is empty in the displayed aspect range and **countably infinite** outside it. The tilted square's transition is $\phi=\pi/8$.

Kopecz already gives the square's simple-attractor saturation angle and the periodic-corner connection criterion. Bajars, Frank and Maas describe the odd-even winding rule and two explicit unbounded winding families, $(2k,1)$ and $(1,2k)$ for $k\ge1$, in §2.4. Nogueira and Troubetzkoy use the checkerboard unfolding and a three-branch diagonal section. The contributions established here are the exact connection to the reciprocal-slope section, the physical-cycle multiplier and spectral classification, and the full-measure assertion on *every* fixed physical slice. [Kopecz, Theorems 2–3](https://webspace.science.uu.nl/~maas0131/files/kopecz2006.pdf) · [Bajars, Frank and Maas, §2.4](https://webspace.science.uu.nl/~frank011/Articles/BaFrMa12.pdf) · [Nogueira and Troubetzkoy, §5](https://arxiv.org/abs/2007.14773)

## Reproducible checks

Run `python experiments/phase1_parity.py` with mpmath installed. The script compares direct wall crossing with the conjugated map on 544 rational slope and starting-height combinations, including multirow columns. For a square tilted by five degrees, it checks the moving-cylinder inequalities at 80 decimal digits. Along the alternating word with digits $-1,1,-1,1,\ldots$, the depth-12 interval in $u$ has length $2.281070521819031339\times10^{-9}$. Its selected gap removes $0.040886351828214031539$ of that interval. These finite checks illustrate the constants in the proof.
