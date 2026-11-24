# The tilted rectangle

Let the tank be the counterclockwise rotation through $0<\phi<\pi/4$ of
$[0,1]\times[0,R]$, with $R>0$. Write $\tan\theta$ for the geometric ray
slope. For $(1-\lambda^2)u_{zz}-\lambda^2u_{xx}=0$, the frequency is
$\lambda=\cos\theta$ and the spectral parameter is $\lambda^2$. We use the
counterclockwise boundary circle and apply the positive-slope chord first.

## Exact return maps

Suppose $\phi<\theta<\pi/2-\phi$. Rotate back into tank coordinates and scale
the height to one. The two directions in the unit square have slopes $a$ and
$-b$, where

$$a=\frac{\tan(\theta-\phi)}R,\qquad b=\frac{\tan(\theta+\phi)}R,
\qquad \mu=\frac ba=\frac{\sin2\theta+\sin2\phi}{\sin2\theta-\sin2\phi}>1.$$

An exact full-boundary formula uses the increasing CCW coordinate $s$, measured
from $(1,0)$ using $|d(y-ax)|$. The perimeter in this coordinate is $2(1+a)$.
Let $H$ be the corresponding coordinate measured using $|d(y+bx)|$ from the
same vertex. It is the increasing piecewise-linear lift taking successive
vertices to vertices, with slopes $1$ on vertical walls and $\mu$ on
horizontal walls. The extrema of $y-ax$ are at $s=0,1+a$, and the extrema of
$y+bx$ are at $H=1,2+b$. Thus

$$ B(s)=H^{-1}\bigl(2-H(-s)\bigr)\pmod {2(1+a)}. $$

Its affine pieces have slopes in $\{1,\mu,\mu^{-1}\}$. Arclength and
edge-fraction coordinates can give other *one-step* slopes. Full-period
multipliers at regular points are invariant under these coordinate changes.

For a convenient section, unfold both square walls by reflection. Choose the
forward unfolded direction northeast. The slope is $a$ on unit squares whose
lower-left corner has even coordinate sum and $b$ on the other squares.
Quotient by $L=\{(i,j)\in\mathbb Z^2:i+j\text{ even}\}$. The section $x=0$
has coordinate $y\pmod2$. In $0<x<1$ let $h(y)$ be the increasing lift
with $h(0)=0$, $h(y+2)=h(y)+1$, and derivative proportional to $1/a$ on the
first row, $1/b$ on the second. During a crossing of the column, $h(y)$
increases by $t$. At $x=1$ identify with $x=0$ by the lattice translation
$(-1,1)$. In $h$ coordinates this adds the half-turn involution $K$. After
conjugating by a circle translation the vertical return lift becomes

$$F(x)=K(x)+t,\qquad t=\frac{ab}{a+b},\quad l=\frac b{a+b},$$

$$K(x)=\begin{cases}l+\mu^{-1}x,&0\le x\le l,\\
1+\mu(x-l),&l\le x\le1,\end{cases}\qquad K(x+1)=K(x)+1.$$

This is the two-break circle family analyzed by Lenci, Bonanno and Cristadoro.
Nogueira and Troubetzkoy give a different, three-piece diagonal section of the
square. Their square model also covers tilted rectangles by an affine change
of variables. [Lenci–Bonanno–Cristadoro, §3 and Appendix A](https://arxiv.org/abs/2102.01654) · [Nogueira–Troubetzkoy, §5](https://arxiv.org/abs/2007.14773)

## Winding, parity, multiplier, endpoints

Write $\eta$ for the mean unfolded vertical displacement per horizontal unit.
The section rotation in the chosen lift is $(1+\eta)/2$ because its coordinate
is $y\pmod2$ and the return includes an upward unit shift. If $\eta=n/m$
in lowest terms ($m,n>0$), put $q=m+n$ and reduce $q/(2m)=P/D$. The section
period is $D=m$ when both counts are odd and $D=2m$ when their parity differs.
In the first case the primitive displacement of a periodic checkerboard leaf
is $(m,n)$, followed by its translate to close on the physical unfolding
$\mathbb R^2/(2\mathbb Z)^2$. In the second case its primitive displacement
already equals $(2m,2n)$. The full folded cycle has $2(m+n)$ wall hits and
$q=m+n$ chess steps. A corner in the unfolded grid records a zero-length
tangent chord between its two wall hits. Interior conclusions can equivalently
be passed to tongue endpoints by continuity of the transverse polygon map.

The CCW boundary rotation is $m/(m+n)=1/(1+\eta)$. For a direct justification
of the numerator, keep $P/D$ fixed, continuously decrease $\mu$ to one and
choose $t$ continuously within its level interval. Its edges are the roots
$F^D(0)=P$ and $F^D(l)=l+P$, continuous in $\mu$ by strict translation
monotonicity. Existence of a folded periodic point with period dividing $q$
keeps the CCW rotation in a finite set throughout this deformation. At $a=b$,
the boundary formula above gives rotation $1/(1+a)$ and $a=\eta$. Irrational
values follow by continuity, for instance by varying $t$ at fixed $\mu$.

The section proof of parity is short. The points of one $D$-periodic orbit,
ordered around the circle, cut it into $D$ intervals. Their $F$-images
permute the intervals transitively. Within any one interval the log slope of
$F^D$, divided by $\log\mu$, changes at most once by $+2$ and at most once by
$-2$, since the $D$ iterated intervals exhaust the circle and there are just
two breaks. Its possible exponents there are two neighboring values of the
same parity as $D$, separated by two. The mean derivative on every interval
equals one, because its endpoints are fixed modulo the lift increment $P$.
For even $D$ this forces derivative identically one. For odd $D$ the two
exponents must be $-1,+1$ on every such interval. Between two consecutive
periodic points there are at most two changes of slope. If neither break is
periodic, both breaks are represented in each interval and the graph has one
additional crossing of the diagonal in each. Thus there is one attracting
and one repelling cycle. When a break is periodic, the other break is outside
its orbit (otherwise no break remains inside a gap and the slope would be
one). Now there is a single change in each gap, leaving one semistable cycle.
This is also the content of the two-break classification. [Lenci–Bonanno–Cristadoro, Theorem 2.2 and Proposition 3.1](https://arxiv.org/abs/2102.01654)

Consequently **even boundary denominator $q$ gives a tongue with attracting
multiplier $\mu^{-2}$ and repelling multiplier $\mu^2$ in its interior**.
The multiplier is squared when the checkerboard leaf doubles to close in the
physical tank. The attracting Lyapunov exponent per chess step is
$-2\log\mu/q$. At a tongue edge the orbit is semistable, with the corresponding
one-sided rates. **Odd $q$ gives the global identity $B^q=\mathrm{Id}$**.
An irrational boundary rotation is minimal by the piecewise-linear Denjoy
theorem. A neutral ribbon and a hyperbolic orbit cannot coexist in this tank.

For fixed $R,\phi$, the two speeds $a,b$ strictly increase with $\theta$.
The unnormalized $y$ exit from one unfolded column therefore increases
strictly at every starting point, since the travel time to any prescribed
higher level is the integral of the reciprocal speed. Continuity and comparison
of circle lifts give a continuous nondecreasing $\eta(\theta)$. A global
periodic return is attained at only one angle by strict monotonicity of its
iterate, and each regular attracting orbit persists on an open interval. A
semistable orbit has its return displacement of one sign with isolated zeros,
so strict monotonicity places it at an edge of its plateau.

## Finite expression for every tongue

For coprime $m,n$ and $P/D=(m+n)/(2m)$ as above, take any $s>0$ and set
$l_s=s/(1+s)$. For $j=0,\ldots,D-1$, write

$$r_j=jP\bmod D,\qquad d_j=\left\lfloor\frac{(j+1)P}D\right\rfloor-
\left\lfloor\frac{jP}D\right\rfloor,$$

$$ (s_j,c_j)=\begin{cases}(1/s,l_s),&2r_j<D,\\
(s,1-s l_s),&2r_j\ge D.\end{cases}$$

With the empty product equal to one, define

$$W_j=\prod_{k=j+1}^{D-1}s_k,\qquad
C_s(P,D)=\frac{\sum_{j=0}^{D-1} W_j(d_j-c_j)}{\sum_{j=0}^{D-1}W_j}.$$

The exact condition is that $t$ lie in the closed interval between
$C_\mu(P,D)$ and $C_{1/\mu}(P,D)$. These are distinct for odd $D$ and agree
for even $D$. Each expression is rational in $\mu$. In particular, replacing
$a,b$ by their tangent formulas produces polynomial boundary equations in
$\tan\theta$, $\tan\phi$, and $R$, after clearing denominators inside the
supercritical window.

To verify the formula, start on the periodic break $0$. The ordered ranks of
the iterates are $r_j$, and their successive lift carries are $d_j$. For odd
$D$, the right slope at the return of $0$ is $s^{-1}$ and the left slope is
$s$ because the jump at $0$ exchanges the two slopes and all other factors
are identical. This argument also works when $s<1$, with the jump reversed.
It follows that precisely the first $(D+1)/2$ ranks, including $0$, are on
the first branch. For even $D$ the return is the identity and exactly $D/2$
ranks are on that branch, using right derivatives to count endpoints. Hence
the fractional iterates satisfy $x_{j+1}=s_jx_j+c_j+t-d_j$, with $x_0=x_D=0$.
Solving this scalar equation gives $C_s$. Translating the other break to the
origin interchanges $s$ with $1/s$. At fixed shape the lift increases strictly
with $t$, so these break returns give the only possible endpoints.

## Primary bands, exact rotation range and the point spectrum

For $n=1$ the horizontal column section is obtained by replacing $(a,b)$
with $(1/b,1/a)$. If $m=2k+1$, its winding is an integer, so its fixed-point
condition reduces to

$$ (k+1)a+kb\ \le 1\le\ ka+(k+1)b. \tag{1}$$

For $m=2k$, its half-integer winding gives $k(a+b)=1$. The reflected formulas
for $m=1$ interchange $(a,b)$ with $(1/b,1/a)$. Examples in CCW orientation
are as follows.

| Boundary rotation | Exact condition |
| --- | --- |
| $1/2$ | $a\le1\le b$, or $|\theta-\arctan R|\le\phi$ in the open supercritical window |
| $1/3$ | $a+b=ab$ |
| $1/4$ | $2/b+1/a\le1\le1/b+2/a$ |
| $2/5$ | $ab(a+b)=a^2+ab+b^2$ |
| $1/(2k+1)$, $k\ge1$ | $k(1/a+1/b)=1$ |
| $1/(2k+2)$, $k\ge0$ | $(k+1)/b+k/a\le1\le k/b+(k+1)/a$ |

At $\theta=\phi+$, $(a,b)\to(0,\tan(2\phi)/R)$. Equation (1) gives a
nonempty band adjacent to that endpoint with $m=M=2\lceil R\cot(2\phi)\rceil-1$.
If $R\cot(2\phi)$ is an integer, equality on the right side of (1) becomes
strict as $\theta$ increases, which explains the ceiling. Swapping axes gives
$n=N=2\lceil\cot(2\phi)/R\rceil-1$ on the opposite edge. Monotonicity and
continuity now give the **entire range of boundary rotation numbers**

$$\boxed{\quad \frac1{2\lceil\cot(2\phi)/R\rceil}
\le\rho(B)\le 1-\frac1{2\lceil R\cot(2\phi)\rceil}.\quad}$$

Every even-denominator rational in this range is realized by an open tongue,
every odd-denominator rational by a single globally periodic frequency.
In the tilted square with $\phi=15^\circ$ the range is $[1/4,3/4]$.
At $\theta=45^\circ$ one has $\mu=3$ and Lyapunov exponent $-\log3$.

The two edge bands meet precisely when $M=N=1$, or

$$ \boxed{\quad \tan(2\phi)\ge\max(R,R^{-1}).\quad} $$

In this case **the full point spectrum is empty**. In all other cases it is
**countably infinite**, with infinite multiplicity at every eigenvalue. The
spectral input is the boundary-invariant criterion for the energy space. On a
globally periodic boundary, the two chord involutions generate a finite group.
One can symmetrize smooth test functions in disjoint small regular orbit
neighborhoods and pass to characteristic profiles to obtain infinitely many
independent Dirichlet eigenfunctions. Minimal irrational dynamics and a
rational map with no fixed interval force the locally continuous invariant
profile to be constant on regular arcs, using the endpoint energy/trace
argument in the study's spectral audit. Outside the supercritical window
common extreme vertices trap the orbits, giving the same vanishing conclusion.

At either critical angle a characteristic is parallel to two opposite sides.
Taking suitable tank coordinates gives profiles $A(y),G(y+kx)$ with $k>0$.
At $x=0,1$ the zero trace says $G(y+k)=G(y)$ for $0<y<1$. At $y=0$ the
other profile has a finite trace, since the edge has positive length. Thus
$G$ is constant on $(0,k)$. The preceding shift propagates this value to
$(0,1+k)$, giving a zero solution. The endpoint parameters $\lambda=0,1$
also have zero kernels by the energy identity and Dirichlet trace.

## Small tilt and measure

The angular measure of corner trapping is $2\phi$, or fraction $4\phi/\pi$.
Its measure in frequency $\lambda$ is $1-\cos\phi+\sin\phi$. For every
$R>0$ and every positive tilt in the stated range, regular periodic-attractor
frequencies have angular measure $\pi/2-2\phi$ and frequency measure
$\cos\phi-\sin\phi$. Thus the regular-attractor frequency measure tends to
one as $\phi\downarrow0$ and equals zero at $\phi=0$. The two-parameter
result of Lenci et al. by itself yields the conclusion for almost every tilt
at fixed $R$. The proof for each tilt uses the uniform gaps of a real
continued-fraction construction and their transversality to the physical
frequency curve. [Fixed-tilt proof](phase1_parity.md)

The simple families admit a concrete quantitative calculation independently
of the total-measure statement. Let $E_1(\phi,R)$ be the union of all tongues
with $m=1$ or $n=1$. For fixed $R$ and $\phi\downarrow0$,

$$ |E_1|_\theta=2\phi\log(1/\phi)+O_R(\phi),\qquad
   |E_1|_\lambda=\phi\log(1/\phi)+O_R(\phi). $$

Indeed, for $m=2k+1\ge3,n=1$, (1) becomes
$|m\sin2\theta-R\cos2\theta-R\cos2\phi|\le\sin2\phi$. Its unclipped endpoints
are

$$\theta_\pm=\frac12\left(\arctan(R/m)+
\arcsin\frac{R\cos2\phi\pm\sin2\phi}{\sqrt{m^2+R^2}}\right).$$

Intersect this interval with the supercritical window. All $1\le k<R\cot2\phi$
contribute, and only the last can be clipped. For large $m$ the unclipped
width is $(\sin2\phi)/m\,[1+O_R(m^{-2})]$ uniformly, by the mean-value theorem.
The sum of $1/m$ over odd $m$ up to $O_R(1/\phi)$ equals
$\tfrac12\log(1/\phi)+O_R(1)$. The $m=1$ family contributes equally after
reflection and $R\mapsto1/R$, with the common central tongue counted once.
For frequency measure, $|d\lambda/d\theta|=\sin\theta$. On the shallow family
$\theta=O_R(1/m)$, giving total $O_R(\phi)$. Its steep reflection contributes
its angular width plus an $O_R(\phi)$ correction.

More generally, for every fixed coprime odd pair $m,n$, the individual tongue
opens around $\theta_0=\arctan(Rn/m)$ with endpoints

$$\theta_\pm=\theta_0\pm\frac{\phi}{mn}+O_{R,m,n}(\phi^2).$$

To see this, put $u=\tan\theta/R$. Then $t=u/2+O(\phi^2)$ and
$l=1/2+\epsilon$, where
$\epsilon=\phi\sec^2\theta/(2\tan\theta)+O(\phi^2)$. Uniformly on the circle,
$K(x)=x+1/2+\epsilon\,\tau(x)+O(\epsilon^2)$ with the continuous triangular
wave $\tau(x)=1-4x$ on $[0,1/2]$, reflected on the other half. At unperturbed
rotation $P/m$, with $m$ odd, $\sum_{j=0}^{m-1}\tau(x+jP/m)=\tau(mx)/m$.
This follows by summing the two constant slopes, or from its odd Fourier
harmonics with coefficients proportional to the inverse square harmonic index.
Iterating the expansion $m$ times at the two periodic breaks gives the two
shifts of $t$ by $\pm\epsilon/m^2+O(\epsilon^2)$. Dividing by
$dt/d\theta=\sec^2\theta/(2R)$ at zero tilt gives the stated endpoints.

In particular, for every finite $Q$, the total angular measure $A_Q$ of
hyperbolic tongues of boundary period at most $Q$ satisfies

$$\lim_{\phi\downarrow0}\frac{A_Q(\phi,R)}\phi=
2\sum_{\substack{m+n\le Q,\; (m,n)=1\\m,n\ \mathrm{odd}}}\frac1{mn}
\sim\frac4{\pi^2}(\log Q)^2\qquad(Q\to\infty).$$

The last statement concerns successive limits. To obtain the coefficient,
the triangle $m+n\le Q$ lies between the squares of sidelengths $Q/2$ and
$Q$ for the purpose of bounding this positive sum. Möbius inversion over
odd common divisors gives leading coefficient
$\tfrac14\prod_{p\text{ odd}}(1-p^{-2})=2/\pi^2$ on either square before
the outer factor two. Thus every finite set of periods captures a vanishing
fraction under infinitesimal tilt, even as the union over all periods tends
to full measure. The first-order coefficient for a fixed cutoff is independent
of aspect ratio.

For the square, direct evaluation at 80 decimal digits gives the following
measures of $E_1$. The last two columns measure a subset of the hyperbolic
frequencies.

| Tilt (radians) | Primary tongues | Angular measure | Frequency measure |
| ---: | ---: | ---: | ---: |
| 0.1 | 9 | 0.509657497216346 | 0.326185982977941 |
| 0.01 | 99 | 0.0975028932492004 | 0.0568433887297031 |
| 0.001 | 999 | 0.0143562254353223 | 0.00799636936947100 |
| 0.0001 | 9999 | 0.00189614062960625 | 0.00102998604316286 |

`experiments/phase1_rectangle.py` also checks the finite all-period word
formula at $\mu=2,7/3$ for every coprime $1\le m,n\le7$. The independent
polygon composition verifies 122 exact rational cases, including displacement
signs, identity returns, and both multipliers.

## Primary-source comparison

- Kopecz (2006), Theorems 1–3, proves corner attraction, the square's simple
  four-wall attractor and its squared multiplier, and the $\pi/8$ saturation
  angle for the square. On p. 9 he derives the global-periodicity family
  $k(t_1+t_2)=1$ analytically for every positive integer $k$. [Kopecz, *Fractal internal wave patterns in a tilted square*](https://webspace.science.uu.nl/~maas0131/files/kopecz2006.pdf)
- Bajars, Frank and Maas (2013), §2.4, describe the odd–even wall-count rule in
  the periodic regime and give analytical equations for the $(2k,1)$ and
  $(1,2k)$ globally periodic square families. Their Fig. 3 shows the tilted
  square phase diagram. [Bajars–Frank–Maas, JFM](https://webspace.science.uu.nl/~frank011/Articles/BaFrMa12.pdf)
- For arbitrary tongue boundaries Lenci, Bonanno and Cristadoro already give the two break-return equations $F^q(a_j)=a_j+p$, $j=0,1$, in Remark 3.5 and (3.10). The floor-and-product formula here evaluates those equations and converts the result to boundary winding in a fixed rectangle. It also yields the full-circuit multiplier, rotation range, aspect-ratio extinction threshold and small-tilt widths. [Lenci, Bonanno and Cristadoro, Remark 3.5](https://arxiv.org/pdf/2102.01654#page=20)
- Soares (2021) reviews the established dimension bounds $1/2<\dim_H\Lambda_u<1$ for a fixed Hecke group with $u>2$. In 2022 Sally Zhu, under the direction of Zhenhao Li, studied dimensions numerically on fixed tilted squares (§4.1). The moving-group transversality argument transfers bounds to each physical slice, and the integer certificate gives a uniform $9/10$ upper bound for the specified tilts. [Soares, introduction](https://link.springer.com/article/10.1007/s00023-021-01117-1) · [Zhu, §4.1](https://arxiv.org/html/2210.13384#S4.SS1)
- Zhang and Temnov (2026), Theorem 2.3, assert that point spectrum is
  characterized by rational wall-relative characteristic slope. For the
  constant-coefficient Dirichlet streamfunction equation in their proof, both
  implications fail. Their reflection argument reverses the wall-normal component
  in tank coordinates. For the same geometric ray angle their normalized squared
  frequency is $\sin^2\theta=1-E_{\rm study}$, agreeing with ours at $1/2$.
  At $R=1$, $\theta=\pi/4$, $\phi=\arctan(1/2)$ the two
  wall-relative slope magnitudes are $1/3$ and $3$. The attracting multiplier
  is $1/81$, and there is no finite-energy eigenfunction. Conversely take
  $R=1$, $a=\sqrt2-1$, $b=2-\sqrt2$ and recover $\theta,\phi$ as the half-sum
  and half-difference of the corresponding arctangents. Both magnitudes are
  irrational, but $a+b=1$ gives an everywhere period-three return and an
  infinite-dimensional eigenspace. An unfolded ray alternates slopes after
  each wall crossing, which invalidates the single straight-slope ray argument
  at pages 377–378. [Zhang–Temnov, Theorem 2.3](https://www.mathnet.ru/eng/cmfd638)
