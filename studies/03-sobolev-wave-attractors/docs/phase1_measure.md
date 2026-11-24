# A fixed tilted rectangle has attracting periodic rays at almost every supercritical frequency

Fix the aspect ratio $R>0$ and the tilt $0<\phi<\pi/4$. Let $\theta$ be the acute angle of the characteristic lines with the physical horizontal, so that $\lambda=\cos\theta$ and the spectral parameter is $\lambda^2$. The streamfunction $u$ is an eigenvector of $T=\Delta_D^{-1}\partial_z^2$ on $H_0^1(\Omega)$. Its image $\Delta_D u$ is an eigenvector of $P=\partial_z^2\Delta_D^{-1}$ on $H^{-1}(\Omega)$ because $P\Delta_D=\Delta_D T$. A regular periodic ray avoids the vertices. Hyperbolicity refers to the derivative of the first-return map on a transverse segment.

**Theorem.** In $J=(\phi,\pi/2-\phi)$, the set $E_{R,\phi}$ of angles with no regular hyperbolic attracting periodic ray satisfies

$$
\dim_H E_{R,\phi}\le d_\phi<1.
$$

The upper bound depends only on the tilt. The exceptional set is empty exactly when $\cot(2\phi)\le R\le\tan(2\phi)$. In every other tank its Hausdorff dimension is strictly larger than $1/2$. At every angle in $J\setminus E_{R,\phi}$ there are both a regular attracting and a regular repelling periodic ray. The angular measure of the periodic-attractor set is $\pi/2-2\phi$. Its measure in $\lambda$ is $\cos\phi-\sin\phi$, and its measure in the spectral variable $\lambda^2$ is $\cos(2\phi)$.

On the two exterior angular intervals, every nonfixed boundary orbit converges forward to one of the common extremal corners. Their combined measures in $\theta,\lambda,\lambda^2$ are $2\phi,1-\cos\phi+\sin\phi,1-\cos(2\phi)$, respectively. The common vertices are one-sided attractors of the oriented boundary map. Indeed, away from a characteristic edge a fixed point of the composition of the two involutions must be a common fixed point of both. In the exterior bands the two pairs of extrema coincide at opposite vertices. An increasing circle homeomorphism with exactly these two fixed points has monotone iterates on each intervening arc. Central symmetry exchanges the arcs and the vertices. At the upright orientation the billiard unfolds to straight lines of a single slope and has no hyperbolic orbits. Consequently the periodic-attractor measure in $\lambda$ tends to **one** as $\phi\downarrow0$, independently of $R$, and equals **zero** at $\phi=0$. These are Lebesgue measures in the frequency parameter.

## The checkerboard section

Rotate back to the rectangle's axes and divide its height by $R$, obtaining a unit square. The slopes are $a$ and $-b$, where

$$
a=\frac{\tan(\theta-\phi)}{R},\qquad
b=\frac{\tan(\theta+\phi)}{R}.
$$

Inside $J$ both are finite and $0<a<b$. Unfold the square across each wall. The ray advances to the right and upward, with slopes $a,b$ on the even and odd cells of the integer checkerboard, respectively. The lattice $L=\{(i,j)\in\mathbb Z^2:i+j\text{ even}\}$ preserves the slopes. A regular closed ray on the torus $\mathbb R^2/L$ returns to its original physical state after at most two circuits, since $2L\subset 2\mathbb Z^2$. Conversely a physical periodic ray lifts to a closed ray after finitely many traversals. The change of transverse coordinate and possible finite power preserve attraction and repulsion.

Write

$$
r=\sqrt{a/b},\quad u=r+r^{-1},\quad x=\sqrt{ab},\quad
m=\frac b{a+b}=\frac1{1+r^2},\qquad s=\frac{ab}{a+b}=\frac xu .
$$

The parameters $x,u$ label speeds and have no role as physical space coordinates below. In a strip of width one, define a vertical coordinate $H(y)$ by integrating the reciprocal of the local slope from $0$ to $y$, then dividing by $1/a+1/b$. It satisfies $H(y+2)=H(y)+1$ and $H(1)=m$. In this coordinate, crossing the strip adds $s$. The deck transformation $(1,1)$ identifies the far vertical side by shifting $y$ back by one. In the circle coordinate this shift is the involution with lift

$$
J_m(t)=
\begin{cases}
 m+r^2t,&0\le t\le m,\\
 1+r^{-2}(t-m),&m\le t\le1,
\end{cases}
\qquad J_m(t+1)=J_m(t)+1.
$$

The return is $J_m\circ T_s$, where $T_s(t)=t+s\pmod1$. Conjugating by $T_s$ gives $g_{m,s}=T_s\circ J_m$. A trajectory starting at section coordinate $t$ hits a grid vertex at the far side precisely when $t+s=0$ or $m$ modulo one. Thus a periodic cycle of the conjugated map avoiding its two breakpoints is a regular closed ray.

## Reduction at a fixed slope ratio

Temporarily keep $u>2$ fixed, so $r=(u-\sqrt{u^2-4})/2\in(0,1)$. For $x>0$ the checkerboard slopes are $rx,x/r$. For any real $x$ define the section directly by $g_{m,x/u}$.

Three transformations preserve the existence of a regular hyperbolic pair.

1. Translation $x\mapsto x+u$ leaves the circle map identical.
2. Changing $x\mapsto-x$ gives a circle map conjugate to the inverse, because $J_m$ is an involution on the circle. A pair exchanges attracting and repelling roles. An inverse visits the images of its forward breakpoints, and rotational conjugacy brings those images to the new breakpoints.
3. For $x>0$, swap the checkerboard coordinates and translate through one cell to exchange the colors. This gives the slopes $r/x,1/(rx)$ and proves invariance under $x\mapsto1/x$. A regular closed trajectory remains regular and closed under this coordinate change. Transverse first returns to different sections have conjugate holonomy around a primitive closed ray. The same equivalence for nonzero negative $x$ follows by the sign symmetry.

These transformations also preserve the property that the section has finite order. For transposition, a common horizontal winding $q$ bounds all vertical windings by $q\max(a,b)$, so their positive integer periods after transposition have a common multiple. Extend the identity across vertex itineraries by continuity. In the other direction transpose again. This argument applies to the dense set of regular points, since the set of initial ordinates that hit a vertex is countable.

If $r<x<r^{-1}$, then $1-m<s<m$. On the first branch of the lift, $g_{m,s}(t)-t$ decreases from $s+m>1$ to $s+1-m<1$. The second branch increases between the same two levels. Each has an interior fixed point modulo one, with derivatives $r^2$ and $r^{-2}$. This is the primary tongue $a<1<b$.

For any real $x$, subtract a nearest multiple $n_0u$, obtaining $|y_0|\le u/2$. If $r<|y_0|\le u/2$, the primary tongue and the symmetries give a hyperbolic pair. If $y_0=0$, the section is conjugate to the finite-order case $g_{m,0}=J_m$ (at later stages the conclusion follows by the preceding equivalences). Otherwise invert $-1/y_0$ and subtract a nearest multiple $n_1u$. Because $0<|y_0|\le r$ implies $1/|y_0|\ge r^{-1}>u/2$, this digit $n_1$ is nonzero. Continue with these two operations. A nearest-integer tie is already in the primary tongue.

Define

$$
\psi_{n,u}(z)=-\frac1{nu+z},\qquad n\in\mathbb Z\setminus\{0\}.
$$

The relation between consecutive centered remainders is $y_{j-1}=\psi_{n_j,u}(y_j)$. Let $K_u$ consist of $0$, all finite compositions applied to $0$, and all limits of infinite nested compositions applied to $0$. The maps send $[-1,1]$ into itself with Lipschitz constant at most $(u-1)^{-2}<1$. A direction yielding no hyperbolic pair must therefore lie in $n_0u+K_u$.

In fact this describes exactly the absence of any regular hyperbolic orbit. Every finite coded number reduces to zero and gives a finite-order section. To see that the digit is correctly recovered, all tails lie in $[-r,r]$, since $(u-r)^{-1}=r$. A truncation of any infinite code is finite and converges to the infinite coded number. A regular hyperbolic cycle persists on an open interval of $x$ for fixed $u$, by its strict multiplier and by avoidance of the finite set of breaks during the circuit. Thus neither type of regular hyperbolic orbit occurs at an infinite code. We have proved the equality

$$
E_{R,\phi}=\{\theta\in J:x(\theta)\in u(\theta)\mathbb Z+K_{u(\theta)}\}.
$$

## A uniform dimension gap for the coded sets

For the physical angles

$$
u(\theta)=\frac{2\sin(2\theta)}{\sqrt{\sin^2(2\theta)-\sin^2(2\phi)}}
\ge u_*=2\sec(2\phi)>2.
$$

Here is a direct estimate valid for all real $u\ge u_*$. Set $I=[-1,1]$ and let $I_w=\psi_w(I)$ for a word $w$ of nonzero digits. First-level images have disjoint interiors, since a shared value for two digits would imply $|(n-n')u|\le2$. All lie in $[-t,t]$ for $t=1/(u_*-1)<1$. The uniform Lipschitz constant is $L=t^2<1$. For real $z\in I$,

$$
|\partial_z\log \psi'_{n,u}(z)|\le 2t .
$$

Summing along a composition gives a uniform distortion ratio $D=\exp(4t/(1-L))$ between its largest and smallest derivative on $I$. The images of the two intervals outside $[-t,t]$ therefore remove at least a fraction $\eta=(1-t)/D>0$ of the length of every parent interval. Hence

$$
\sum_{|w|=k}|I_w|\le 2(1-\eta)^k,\qquad
\sum_{|w|=k}\sup_I \psi'_w\le D(1-\eta)^k .
$$

Choose a block length $k$ making the last bound strictly below one. For any $d_0\in(1/2,1)$, the $d_0$-powers of the block derivative suprema have summable upper bounds, uniformly in $u\ge u_*$, because $\sum_{n\ne0}(|n|u_*-1)^{-2d_0}<\infty$. For $v\in[0,1]$, $v^d\to v$ uniformly as $d\uparrow1$. Applying this to finitely many block words, then using summable domination for the tail, produces a $d_\phi<1$ for which

$$
\sup_{u\ge u_*}\sum_{|w|=k}\big(\sup_I\psi'_w\big)^{d_\phi}<1.
$$

Iteration covers the infinite codes with arbitrarily small total $d_\phi$-content. The finite codes form a countable set. This proves $\dim_H K_u\le d_\phi$ uniformly for all $u\ge u_*$.

## Intersecting the varying coded set with the physical curve

Both $x$ and $u$ vary with $\theta$ along a fixed physical tank. Its exceptional angles require an estimate for this curve.

For each finite or infinite code $w$, write $h_w(u)$ for its value, with the empty word giving $0$. All such functions are holomorphic on $\operatorname{Re}u>2$. Indeed the maps send the closed complex unit disc into its interior and contract uniformly on each compact subset of this half-plane, since $|nu+z|\ge |n|\operatorname{Re}u-1$. Distinct digits have disjoint images there, by $|(n-n')u|>2$. No nonempty tail can equal zero, and equality after a common prefix is equivalent to equality of the tails. Thus distinct codes remain distinct at every such complex $u$.

Fix a real $\theta_c\in J$. Choose a complex disc about it on which $x,u$ are holomorphic and $\operatorname{Re}u>2$. Use $z=h_w(u(\theta_c))\in K_{u(\theta_c)}$ as the real coordinate of a code. For two different codes, the positive harmonic function

$$
\log\!\left(3/|h_w(u(\zeta))-h_v(u(\zeta))|\right)
$$

and Harnack's inequality give, on a concentric disc with radius fraction $\rho<1$,

$$
|h_w(u(\zeta))-h_v(u(\zeta))|
\le 3^{1-\alpha}|z-z'|^\alpha,\qquad
\alpha=\frac{1-\rho}{1+\rho}.
$$

Cauchy's formula gives the same Hölder exponent in $z$ for the first $\theta$-derivative on a smaller disc. The other side of Harnack's inequality gives $|z-z'|\le 3^{1-\alpha}|h_w(u(\zeta))-h_v(u(\zeta))|^\alpha$. The exponent can be chosen as close to one as desired.

Each positive real code curve $H(u)=nu+h_w(u)$ has a monotonicity constraint. In the speed coordinates $A=rH$ and $B=H/r$, two points on a connected positive piece of this curve cannot have both speeds strictly larger at the second point. First take a finite code. Its strip map is finite order at every $u$, so its lift rotation number varies continuously and is rational, hence constant. To compare two strip maps use the same vertical coordinate $y$ of period two. Their natural lifts send $y$ to $Y-1$, where $\int_y^Y 1/v(t)\,dt=1$ and $v$ alternates between $A$ and $B$. Increasing both speeds strictly sends every $y$ to a strictly larger output. Two such ordered lifts of finite-order circle maps cannot have equal rotation number. Indeed, a common positive iterate would be the same integer translation for both lifts, contrary to their strict order. This proves the constraint for a finite code. For an infinite code, finite truncations converge uniformly on compact positive pieces. Two strict inequalities would persist for a sufficiently long finite truncation, giving a contradiction.

At an incidence of the physical curve with this code let

$$
F(\theta,z)=x(\theta)-H(u(\theta)).
$$

Along the code, at least one of $A'(\theta),B'(\theta)$ is nonpositive. Otherwise both speeds would strictly increase near the point. Both physical derivatives $a',b'$ are positive. At a zero of $F$, differentiating $a-A=rF$ and $b-B=F/r$ gives

$$
\partial_\theta F\ \ge\ \min(a'/r,\, rb')>0 .
$$

Every zero is a strict crossing from negative to positive, so each individual code crosses the physical curve at most once. On a small product neighborhood of an incidence, joint continuity makes $\partial_\theta F$ uniformly positive. The intermediate value theorem gives a unique nearby root $\theta(z)$ for every sufficiently close label $z$, and the mean value theorem gives $|\theta(z)-\theta(z')|\le C|z-z'|^\alpha$. Conversely, the reversed Harnack estimate at $\theta(z)$ gives

$$
|z-z'|\le C|F(\theta(z),z')-F(\theta(z'),z')|^\alpha
\le C'|\theta(z)-\theta(z')|^\alpha .
$$

Here $n$ is fixed locally, since $|h_w|\le r<u/2$. All nearby incidences are in this product neighborhood after shrinking the parameter interval. Indeed the uniform bound on the parameter derivatives forces their base labels to approach the original base label. Choosing $\theta_c$ at the incidence and shrinking the neighborhood makes both Hölder exponents arbitrarily close to one.

Every relative neighborhood of any point of $K_u$ contains a finite Möbius image of the full set $K_u$. For an infinite label use a long common prefix. At a finite label append one digit of sufficiently large magnitude. A finite composition is bi-Lipschitz on $I$. The local Hausdorff dimension at every point of $K_u$ thus equals $\dim_H K_u$. The two Hölder estimates give the more precise identity

$$
\lim_{\varepsilon\downarrow0}
\dim_H\big(E_{R,\phi}\cap(\theta_c-\varepsilon,\theta_c+\varepsilon)\big)
=\dim_H K_{u(\theta_c)}
\quad(\theta_c\in E_{R,\phi}).
$$

At a fixed Hölder exponent $\alpha<1$ close to one, countably many real neighborhoods cover the exceptional set. Their dimensions are at most $d_\phi/\alpha$. Letting $\alpha\uparrow1$ proves the theorem’s upper bound.

For each finite real $u>2$ one also has $\dim_H K_u>1/2$. Set $\ell_n=(|n|u+1)^{-2}$, the infimum of the branch derivative. The series $\sum_{n\ne0}\ell_n^{1/2}$ diverges, so a finite alphabet $S$ and an exponent $s>1/2$ satisfy $\sum_{n\in S}\ell_n^s>1$. Assign independent digit probabilities proportional to $\ell_n^s$. The mass of each cylinder $I_w$ is at most $(|I_w|/2)^s$, by the derivative lower bound along its word. With this finite alphabet, a child has length at least $D^{-1}\min_{n\in S}\ell_n$ times its parent length. Stop when the length first falls below a radius $\varepsilon$. Disjointness and this lower bound imply that an interval of length $2\varepsilon$ meets a bounded number of these stopping intervals. Its mass is at most $C\varepsilon^s$, proving the lower bound by the mass distribution principle. The local dimension identity transfers it to every nonempty physical exceptional set.

## Explicit reentry of infinitely many standing frequencies

The primary tongue is $a<1<b$. Its lower endpoint $\theta_0=\arctan R-\phi$ lies in $J$ exactly when $R>\tan(2\phi)$. In this case consider

$$
h_N(u)=\psi_{-1,u}^{\,N}(0)
=r\frac{1-r^{2N}}{1-r^{2N+2}},\qquad N\ge1.
$$

The formula follows by induction from $\psi_{-1,u}(z)=1/(u-z)$, and each $h_N$ increases strictly with $N$ at fixed $u$. At a physical solution to $x=h_N(u)$, all **regular physical rays** close. The corresponding iterate of the continuously extended boundary map is the identity everywhere. Equivalently,

$$
b(\theta)=\frac{1-r(\theta)^{2N}}{1-r(\theta)^{2N+2}}.
$$

These are the consecutive side-count families. Write $(M,V)$ for a primitive periodic ray's horizontal and vertical winding on $\mathbb R^2/L$. The physical lift before subtracting the deck vector rises by $V$ over $M$ strip returns. If $\rho$ is the translation number of the displayed lift $T_sJ_m$, this gives $V/M=2\rho-1$. Indeed $H(y-1)=J_m(H(y))-1$ for the chosen lifts. The transformation $x\mapsto u-x$ keeps $M$ and sends $V$ to $2M-V$. To see this, $s\mapsto1-s$, and $J_m^2=T_1$ gives $\rho(1-s)=2-\rho(s)$ in these lifts. Transposing swaps the windings. Starting with the order-two strip map at $s=0$ and its formal winding $(2,0)$, the recursion $h_{N+1}=1/(u-h_N)$ therefore gives $(M,V)=(2N+2,2N)$. Alternatively, begin at the positive speed $x=u$ with winding $(2,4)$ and transpose to obtain $h_1$. The pair $(2N+2,2N)$ is primitive in $L$ since its half has opposite parities. Its even components return to the physical rectangle after one such circuit. There are $N+1$ hits on each vertical side and $N$ hits on each horizontal side, counting wall hits at a vertex with multiplicity. The two-chord boundary map has period $2N+1$.

As $\theta\downarrow\phi$ the left side tends to $\tan(2\phi)/R<1$, and the right side tends to one. At $\theta_0$ the left side equals one and the right side is smaller. The unique-crossing result gives exactly one solution $\theta_N\in(\phi,\theta_0)$ for every $N$. Since $h_{N+1}>h_N$, the crossings are in strictly increasing order. They converge to $\theta_0$ since $r\le r(\pi/4)<1$. Set $t=\tan(2\phi)$. The exact geometric accumulation rate is

$$
\theta_0-\theta_N\sim
\frac{t}{1+Rt}
\left(\frac{R-t}{R(1+Rt)}\right)^N .
$$

Indeed $1-b(\theta_N)=r_N^{2N}(1-r_N^2)/(1-r_N^{2N+2})$ and $b'(\theta_0)=(1+R^2)/R$. The uniform bound on $r_N$ implies $N|\theta_N-\theta_0|\to0$, hence $r_N^{2N}/r(\theta_0)^{2N}\to1$. Substitution gives the formula.

Changing $R\mapsto 1/R$ and $\theta\mapsto\pi/2-\theta$ sends $x\mapsto1/x$ and keeps $u$ fixed. There is a second sequence above $\theta_1=\arctan R+\phi$ whenever $R<\cot(2\phi)$, with the preceding rate after $R\mapsto1/R$.

If neither strict inequality holds, then $\cot(2\phi)\le R\le\tan(2\phi)$, and the whole open supercritical interval lies in the primary tongue. Its section has precisely two fixed points and its other points converge to the appropriate fixed point under positive or negative iteration. A continuous invariant boundary trace is constant there and no neutral periodic interval exists. In all other aspect ratios the displayed sequences give infinitely many distinct finite-order billiards, hence infinitely many distinct frequency eigenspaces by the boundary trace criterion. Distinct eigenvalues of a self-adjoint operator on the separable energy space form at most a countable set. The two edge-parallel frequencies produce no modes either. For example, with one horizontal characteristic family the solution has the form $A(y)+B(y+bx)$. The bottom edge gives constant $B$ on $(0,b)$, and the two vertical edges give $B(y)=B(y+b)$ on $(0,1)$. Iterating gives a constant on its whole argument interval, hence the solution vanishes. The opposite critical angle follows by transposition. These trace statements may be read almost everywhere on the open edges. In particular, the classification gives zero or countably infinitely many standing frequencies, with zero exactly in the displayed closed aspect-ratio range. The finite-energy endpoint regularity and the construction of smooth modes on an open periodic interval are proved in the [polygonal boundary-profile theorem](phase1_pde.md).

## Numerical checks

Run the [frequency verification script](../experiments/phase1_measure.py) with Python and mpmath. At 95 decimal digits, direct cell-by-cell crossings and the exact section formula agreed within $2.3\times10^{-95}$ over the selected initial points and tank shapes. On the square tilted by $5^\circ$, the lower primary endpoint is $40^\circ$. The neutral root $N=32$ lies $1.6712795039601511\times10^{-6}$ radians below this endpoint. For $N=64$ the distance is $1.8633942722443263\times10^{-11}$ radians, and the ratio of the actual distance to the asymptotic expression is $0.99999999995819138427$. For the tested $N=1,2,4,8,16,32,64$ the lifted return advanced by $2N+1$ over $2N+2$ iterates on each sample orbit.

## A fixed rectangular trapezoid

The same argument sharpens the parameter quantifier for the physical rectangular trapezoid. In the notation of Lenci, Bonanno and Cristadoro, fix $\ell>0$ and the wall angle $0<\alpha<\pi/2$. Write $\vartheta\in(\alpha,\pi/2)$ for their ray parameter. Their Appendix A, (A.1) and (A.4), gives $m=(1+y)/2$ and $s=ky-1/2$, where $y=\tan\alpha/\tan\vartheta\in(0,1)$ and $k=2\ell/\tan\alpha+1/2$. Shift $s$ by one, which preserves the circle map. Its checkerboard speeds are then

$$
A(y)=\frac{2ky+1}{1+y},\qquad B(y)=\frac{2ky+1}{1-y}.
$$

Indeed $B/(A+B)=(1+y)/2$ and $AB/(A+B)=ky+1/2$. Both speeds are strictly increasing because $2k>1$. On any compact subinterval of $0<y<1$ the associated $u=2/\sqrt{1-y^2}$ is bounded below by a number greater than two. All estimates above apply, with the same strict-crossing proof. Thus for **every fixed $\ell,\alpha$** almost every supercritical ray parameter has a regular periodic attractor, and the exceptional set has dimension strictly below one on each compact interior subinterval. The lower bound on $u-2$ tends to zero at $y=0$, so the strict dimension estimate is local for this family. [Lenci, Bonanno and Cristadoro, Appendix A](https://arxiv.org/abs/2102.01654)

## Prior observations and scope

- Kopecz (2006), Theorems 1–3, treats the tilted square, proves corner capture, computes the four-reflection primary tongue and its multiplier, states the all-primary transition at square tilt $\pi/8$, and uses corner connections to characterize periodicity. On p. 9 he derives $k(t_1+t_2)=1$ analytically for every positive integer $k$ and uses numerical methods for more complicated itineraries. Bajars, Frank and Maas (2013), §2.4, present the odd–even standing-ray classification and two simple frequency families for the square. The elementary primary tongue, the square transition, and those parity observations precede this work. [Kopecz report](https://webspace.science.uu.nl/~maas0131/files/kopecz2006.pdf) · [Bajars, Frank and Maas](https://webspace.science.uu.nl/~frank011/Articles/BaFrMa12.pdf)
- Nogueira and Troubetzkoy, Theorem 13, prove that the periodic direction pairs for a square contain an open dense subset. The full periodic locus fails to be open. On the upright square the pair of slopes $\pm1$ is periodic and is approached by pairs $\pm s$ with irrational $s$ and irrational rotation $1/(1+s)$. Lenci, Bonanno and Cristadoro, Theorem 3.2 and Appendix A, prove an almost-everywhere statement for a two-parameter rectangular-trapezoid family by studying a fixed-break-ratio direction parameter. Their Remark 3.5 and equation (3.10) give the two break-return equations for arbitrary tongue boundaries. Their normalized two-break circle is the same $T_sJ_m$ used here. Its parabolic generators become a subgroup of index at most two in the Hecke group generated by $x\mapsto x+u$ and $x\mapsto-1/x$. The latter computation is recovered directly by the checkerboard symmetries above. Their dilation-surface argument draws on Boulanger, Fougeron and Ghazouani. [Chess billiards](https://arxiv.org/abs/2007.14773) · [Internal-wave billiards](https://arxiv.org/abs/2102.01654) · [Affine interval exchanges](https://arxiv.org/abs/1701.02332)
- For a fixed Hecke group of width $u>2$, the bounds $1/2<\dim_H\Lambda_u<1$ are classical and are reviewed by Soares (2021). Sally Zhu, working under the direction of Zhenhao Li (2022, §4.1), estimated dimensions numerically on fixed tilted squares. [Soares, introduction](https://link.springer.com/article/10.1007/s00023-021-01117-1) · [Zhu, §4.1](https://arxiv.org/html/2210.13384#S4.SS1)
- The fixed-tank conclusion uses the moving-code estimate and strict transversality in the two speed parameters. The local dimension identity, exact measure jump on every physical frequency curve, and geometric neutral accumulation at any interior primary-tongue edge are the additional conclusions here. A broader priority claim would require checking the rest of the spectral and dynamics literature.
