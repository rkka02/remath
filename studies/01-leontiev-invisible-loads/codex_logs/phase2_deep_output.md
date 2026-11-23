# Project ReMath, Phase 2 · What polygon frequencies determine

The one-sided lattice has **exactly one real invisible \(L^2\) flux on every triangle**, including the equilateral triangle. Its integrable kernel has dimension three. The Saint-Venant torsion flux fails even the first integer test. Every genuine quadrilateral has three invisible \(L^2\) fluxes and a fourth invisible measure carrying alternating corner atoms. Tilting a square preserves those dimensions. Adding the reflected lattice kills **every** real invisible measure as soon as central symmetry is broken.

For corner recovery, the odd-polygon minimax error has a sharp \(N^{-1/2}\) equivalent given below by a convergent formula depending only on the polygon. On an even polygon, adding \(N\) shifted samples changes the **exponent**. At a vertex of interior angle \(\omega_k\), the exact-data minimax order is \(N^{-1+\omega_k/(2\pi)}\). A half-step fails finite-band minimax optimality even on the unit square.

**One part of Problem B remains unresolved.** I obtained the exact finite-band minimax value and matching asymptotic orders on even polygons. I did not establish convergence of the normalized error at the improved even-polygon scale, its limiting prefactor, or a shift minimizing that prefactor. The finite-band counterexample does not decide the last question.

The verification script ran successfully, including its outward-rounded interval certificate. [Research report](/Users/mw/Desktop/math/remath/codex_logs/phase2_deep_output.md) · [Verification script](/Users/mw/Desktop/math/remath/experiments/phase2_theorems.py)

## A. Exact classification of invisible loads

Use the genuine vertices of a bounded positive-area convex polygon, ordered counterclockwise, with all interior angles strictly less than \(\pi\). Splitting a straight side changes the frequency data. Write
\[
 d_j=\gamma_{j+1}-\gamma_j,\qquad b_j=2\pi i/d_j,\qquad c_j=1/b_j,\qquad
 H(s)=\max_{w\in\bar D}\Re(sw).
\]
Thus \(H(s)\) is the Euclidean support function evaluated at the vector \(\bar s\). In the indicator convention \(h(\theta)=\max_{\zeta\in K}\Re(\zeta e^{-i\theta})\), the diagram is the complex reflection \(K=\{\bar w:w\in\bar D\}\). Every finite measure satisfies \(|B_\mu(s)|\le\|\mu\|_{\mathrm{TV}}e^{H(s)}\).

| Polygon | Real \(L^2\), one-sided | Real \(L^1\), one-sided | Real measures, one-sided | Real measures, two-sided |
|---|---:|---:|---:|---:|
| Equilateral triangle | 1 | 3 | 3 | 0 |
| Scalene triangle | 1 | 3 | 3 | 0 |
| Quadrilateral without parallel edges | 3 | 3 | 4 | 0 |
| Trapezoid with exactly one parallel pair | 3 | 3 | 4 | 0 |
| Parallelogram, including square | 3 | 3 | 4 | 4 |
| Regular pentagon | 3 | 5 | 5 | 0 |
| \(p=2k+1\) | \(2k-1\) | \(2k+1\) | \(2k+1\) | 0 |
| \(p=2k\) | \(2k-1\) | \(2k-1\) | \(2k\) | \(2k\) if centrally symmetric, otherwise 0 |

### A1. The Gamma product, including its zero rays

Let \(h=p/2\). Choose a unit direction \(u\) strictly exposing vertex \(v\) and set, with principal logarithms,
\[
 \tau=v-\sum_j c_j\Log(-c_j u),\qquad
 L(s)=e^{\tau s}\prod_{j=1}^p\Gamma(1-c_js)^{-1}.
\]
Then \(L(0)=1\), and its zeros are exactly the positive lattice, all simple. Opposite parallel edges have distinct oriented node rays.

On closed angular subintervals between the rays, uniformly as \(R\to\infty\),
\[
 L(Ru)=A(u)R^{-h}e^{Ru v}\bigl(1+O(R^{-1})\bigr),\qquad
 A(u)=(2\pi)^{-h}\exp\left(-\tfrac12\sum_j\Log(-c_ju)\right).
 \tag{1}
\]
Indeed, Stirling gives the exponential term \(s\sum c_j\Log(-c_ju)\). The terms involving \(s\log R\) and the common linear term vanish since \(\sum c_j=0\). The sum of logarithms weighted by \(c_j\) is constant within a sector. When \(\arg s\) increases across ray \(j\), it decreases by \(2\pi i c_j=d_j\), exactly the change from supporting vertex \(\gamma_{j+1}\) to \(\gamma_j\). This also proves independence of the choice used to define \(\tau\). Writing the leading power as \(s^{-h}\) on a continuous angular branch, its coefficient \(C_v\) changes sign at each ray. For odd \(p\), the half-integer power itself changes sign after a full turn. [Stirling expansion and its sector of uniformity](https://dlmf.nist.gov/5.11)

In a fixed small cone about ray \(j\), first apply the reflection formula
\[
 \Gamma(1-x)^{-1}=\Gamma(x)\sin(\pi x)/\pi
\]
to \(x=c_js\). Stirling on the remaining factors and on \(\Gamma(x)\) now gives
\[
 L(s)=C_{\gamma_j}s^{-h}e^{s\gamma_j}(1-e^{sd_j})
                 \bigl(1+O(|s|^{-1})\bigr).
 \tag{2}
\]
The factor containing the zeros is exact. On the ray, after removing \(e^{H(s)}|s|^{-h}\), the modulus is \(2|C_{\gamma_j}||\sin(\pi c_js)|(1+O(|s|^{-1}))\). The indicator on that ray is a limsup.

Consequently the following estimate holds uniformly for \(|s|\ge1\):
\[
 |L(s)|\asymp_D e^{H(s)}(1+|s|)^{-h}
          \min\{1,\operatorname{dist}(s,\Lambda_+)\}.
 \tag{3}
\]
In the transition cones this follows from the sine estimate in a strip and dominance of one exponential outside the strip. In particular,
\[
 |L'(\nu)|\asymp_D e^{H(\nu)}(1+|\nu|)^{-h}.
\]

### A2. Necessity and explicit construction of the loads

If \(B=B_\mu\) vanishes on the positive lattice, \(B=QL\) with \(Q\) entire. By (3), \(|Q(s)|\le C(1+|s|)^h\) outside small disjoint node disks. The maximum principle fills the disks. Cauchy's inequalities give \(\deg Q\le\lfloor h\rfloor\).

On a ray strictly exposing \(v\), dominated convergence gives \(e^{-sv}B(s)\to\mu\{v\}\). An \(L^1\) density gives limit zero. An \(L^2\) density gives the stronger bound \(o(|s|^{-1/2})\). On either incident side the decaying factor is bounded by \(e^{-c|s|x}\), with \(x\) the distance from \(v\). Apply Cauchy–Schwarz on \([0,\delta]\), then let \(\delta\downarrow0\). The remaining boundary contributes exponentially little. Thus
\[
 \deg Q<h\quad(L^1),\qquad \deg Q<h-\tfrac12\quad(L^2).
 \tag{4}
\]
Real loads require \(Q(0)\in\mathbb R\). For \(p=2k\), a top term \(q_ks^k\) produces vertex masses \(q_kC_v\). These alternate between \(q_kC\) and \(-q_kC\), imposing one real condition on \(q_k\).

The converse gives an explicit answer to what the invisible flux is on a scalene triangle. Start with the desired \(F=QL\). In the top even measure case subtract \(\sum_v q_kC_v e^{sv}\), and call the remainder \(F_0\). Equations (1) and (2) give \(F_0=O(e^H/(1+|s|))\) uniformly, including the transition cones. In the other cases take \(F_0=F\).

For \(z\) beyond supporting edge \(j\) define
\[
 C_F(z)=u_j\int_0^\infty F_0(tu_j)e^{-tu_j z}\,dt,\qquad u_j=b_j/|b_j|.
 \tag{5}
\]
The separating directions for a fixed exterior \(z\) form an arc, so contour rotation identifies the formulas on overlaps. At infinity the Laurent coefficients are \(F_0^{(n)}(0)\), by termwise Laplace integration. Consequently
\[
 \frac{1}{2\pi i}\oint e^{sz}C_F(z)\,dz=F_0(s)
\]
on an exterior contour around the polygon.

For \(\deg Q<h-1/2\), the functions \(F_0(tu_j)e^{-tH(u_j)}\) belong to \(L^2(0,\infty)\). This holds also for the even remainder after subtraction. Plancherel on the parallel lines in (5) proves that \(C_F(w)\,dw/(2\pi i)\) is a complex boundary density with \(L^2\) norm bounded by a polygon constant times the sum of these ray norms. For the contour limit, move every support line outward by \(\epsilon\). Its Fourier integrand acquires \(e^{-\epsilon t}\), giving strong \(L^2\) convergence, while the excess edge intervals have vanishing length.

For \(p=2k+1,\deg Q=k\), (2) instead gives two endpoint exponentials times \(t^{-1/2}\) with constant coefficients and a normalized \(O(t^{-3/2})\) remainder for \(t\ge1\). The remainder has a bounded inverse. The Laplace integral of \(t^{-1/2}\) is \(\sqrt\pi\,z^{-1/2}\) in the right half-plane. Thus the only upper singularities on the displaced sides are \(C|z-v|^{-1/2}\). The contour limit works in every \(L^q,\ 1<q<2\). This is the source of the two additional real integrable modes. Equation (4) excludes them from \(L^2\).

To obtain a **real** density, pull the complex boundary measure back by a disk Riemann map \(w=\Phi(e^{it})\) and write it as \((U+iV)\,dt\). With \(\mathcal H\) the circle Hilbert transform of multiplier \(-i\,\mathrm{sgn}(n)\), take
\[
 g(\Phi(e^{it}))=\frac{U(t)+\mathcal H V(t)}{|\Phi'(e^{it})|}.
 \tag{6}
\]
Restore the subtracted real atoms. The replacement preserves the negative Fourier coefficients and the mean, since the residual has real mass. It therefore preserves integration against analytic disk polynomials and, by uniform approximation, against \(e^{s\Phi}\).

The pulled-back density norm in arclength \(L^q\) uses weight \(|\Phi'|^{1-q}\). At a prevertex of angle \(\alpha\pi\), Schwarz–Christoffel gives \(|\Phi'|\asymp|t-t_v|^{\alpha-1}\). The weight exponent \((1-\alpha)(q-1)\) lies strictly between \(-1\) and \(q-1\), precisely the range for the weighted conjugate-function bound. For these power weights one can also use comparable dyadic annuli and the ordinary Hilbert bound. Between separated annuli of radii \(r,\rho\), Hölder and the cotangent kernel give norm \(C r^\delta\rho^{1-\delta}/\max(r,\rho)\), where \(\delta=(1+\text{weight exponent})/q\in(0,1)\). These bounds are summable over dyadic separations. [Hunt, Muckenhoupt and Wheeden](https://doi.org/10.1090/S0002-9947-1973-0312139-8)

Finally, a real boundary measure with zero entire transform vanishes. It annihilates analytic polynomials. Polynomial approximation on the closed Jordan polygon gives annihilation of every \((\Phi^{-1})^n\), and reality gives the conjugates. The circle pullback has all Fourier coefficients zero.

This proves existence, uniqueness, and the dimensions in the table. Explicit generators use \(Q=1,s,is,\ldots,s^d,is^d\) through the allowed degree, with \(Q=s^k/C\) added for even measures. On a triangle the unique mass-one invisible \(L^2\) density is (5)–(6) with \(Q=1\). Every invisible real measure has the listed density and atom decomposition.

**Complex \(L^2\).** The full kernel has infinite complex dimension. For example \(w^n\,dw/d\ell\), \(n\ge0\), annihilate every entire test. The zero-transform fiber consists exactly of densities whose circle pullback annihilates every analytic monomial. Modulo this fiber, the one-sided invisible space has complex dimension \(\lfloor p/2\rfloor\), given by all complex multipliers of degree at most \(\lfloor p/2\rfloor-1\). Existence follows directly from (5). The full closed kernel has countable Hilbert dimension and Hamel dimension continuum.

**Both signs.** With \(r\) parallel pairs, \(\Lambda_+\) has \(p\) distinct rays and \(\Lambda_\pm\) has \(2p-2r\). Infinitely many reflected nodes outside \(\Lambda_+\) force the polynomial \(Q\) to vanish. An unpaired side gives a whole missing ray. For an opposite pair of lengths \(a,b\), eventual inclusion in both directions requires \(mb/a\) and \(ma/b\) integral for all sufficiently large integers \(m\). Consecutive differences force \(a=b\). Equal opposite edges in cyclic order are equivalent to central symmetry, since \(\gamma_j+\gamma_{j+p/2}\) is constant. This proves the two-sided classification, including unequal commensurable lengths. For an asymmetric polygon the two-sided complex kernel is exactly the zero-transform fiber.

**Pure atoms.** To decide whether the even alternating charges alone are invisible, group the vertices for each \(j\) by equal values of \(e^{b_j(\gamma_l-\gamma_j)}\). The signed weights must sum to zero in every group. This is necessary by Vandermonde inversion on the distinct nonzero values and sufficient by summation. On a generic quadrilateral the invisible alternating mode requires its compensating density.

### A3. The torsion test

Stokes' theorem applied to \(e^{sw}d\bar w\) gives, for \(s\ne0\),
\[
 \int_D e^{sw}\,dA=
 -\frac1{2is^2}\sum_j\frac{\bar d_j}{d_j}
       (e^{s\gamma_{j+1}}-e^{s\gamma_j}).
 \tag{7}
\]
The value at zero is the area. For a triangle and \(s=mb_1\), the sum reduces to
\[
 (\bar d_2/d_2-\bar d_3/d_3)(e^{s\gamma_3}-e^{s\gamma_1}).
\]
Both factors are nonzero. More generally, invisibility of (7) requires the grouping test above with the nonzero weights \(\bar d_{j-1}/d_{j-1}-\bar d_j/d_j\). On each opposite supporting line there must be two vertices separated by an integer multiple of the tested edge. Applying this in both directions forces central symmetry.

Green's identity identifies (7) with the transform of \(-\partial_n u\) for \(-\Delta u=1,\ u|_{\partial D}=0\). On the unit equilateral triangle with base \([0,1]\), the explicit solution is \(u=l_1l_2l_3/H_0\), where \(l_j\) are inward side distances and \(H_0=\sqrt3/2\). Their gradients have pairwise product \(-1/2\) and their sum is \(H_0\). At the first base node,
\[
 B_{-\partial_n u}(2\pi i)
 =-\frac{\sqrt3}{8\pi^2}(1+e^{-\pi\sqrt3})
 =-0.0220317406018665421\ldots .
\]
The normal components have transforms \(s\int_D e^{sw}dA\) and \(is\int_D e^{sw}dA\), so both also fail the triangle test.

Sedletskii previously identified an exceptional odd-polygon \(E^2\) endpoint in the periodic-subspace problem. Publication priority for the results here has not been established. [Sedletskii on periodic projections](https://www.mathnet.ru/eng/im1217) · [Sedletskii on exponential bases](https://www.mathnet.ru/eng/im1928)

## B. Exact-data minimax corner recovery

### B1. The finite minimax value

Normalize each row to \(e^{s(w-\gamma_j)}\) and split real and imaginary parts into real functions \(h_i\). Let
\[
 Rg=(\langle h_i,g\rangle)_i,\qquad A_{il}=h_i(\gamma_l),\qquad G=RR^*.
\]
For distinct nonzero frequencies \(G>0\). A real row dependence would produce a holomorphic exponential sum whose real part vanishes on the boundary. Such a function is an imaginary constant, contrary to linear independence of the exponentials and the constant.

When \(A\) has full column rank, put \(K=(A^TG^{-1}A)^{-1}\). Then
\[
 \boxed{
 E_k=M\sqrt{K_{kk}},\qquad E_\infty=M\max_k\sqrt{K_{kk}},\qquad
 \widehat a=K A^TG^{-1}y.}
 \tag{8}
\]
The estimator reproduces the atom vector exactly, and the Gram matrix of its background error kernels is \(K\). For a matching lower witness take
\[
 a=M K e_k/\sqrt{K_{kk}},\qquad g=-R^*G^{-1}Aa.
\]
Then \(\|g\|=M\) and \(y=0\). The negative pair has the same data. Every estimator incurs error at least \(|a_k|\) on one of these two inputs. Taking the worst coordinate proves the vector formula. Rank loss gives infinite risk on coordinates that see \(\ker A\), with the pseudoinverse formula on the identifiable subspace. This argument covers nonlinear estimators. [Related optimal-recovery theorem](https://foucart.github.io/publi/DFPW_recovery_final.pdf)

Every Gram entry is elementary. Integrate \(fg\) and \(f\bar g\) to obtain the four real blocks. On a side the integral of one exponential is \(|d|(P_{\rm end}-P_{\rm start})/z\), with \(z\) its exponent increment and the removable value at zero. Equivalently, \(E_k/M\) is the minimum boundary \(L^2\) norm of a real row combination taking vertex values \(\delta_{kl}\).

Raw endpoint-sum inversion generally has **infinite finite-band worst-case error**. On a triangle the other vertex contributes \(N^{-1}\sum_{m=1}^N W^m\), nonzero for \(0<|W|<1\). The equilateral example has nonzero real leakage as well. An unrestricted charge can amplify it arbitrarily. For an averaging matrix \(V\), calibrate with \(W=(VA)^\dagger V\) when \(VA\) has full column rank. The exact finite ratio to optimal risk is
\[
 \sqrt{(WGW^T)_{kk}/K_{kk}}.
\]

### B2. The sharp odd-polygon constant

Let \(S_{jl}=\mathbf1_{l=j}+\mathbf1_{l=j+1}\). At each vertex \(v\), let \(u\) run over its two incident unit directions pointing into the sides. Use the real Hilbert spaces
\[
 X=\bigoplus_{v,u}L^2(\mathbb R_+,\mathbb R),\qquad
 Y=L^2((0,1),\mathbb C^p)
\]
with real scalar product on \(Y\). Define
\[
 (Tf)_j(t)=\sum_{v=\gamma_j,\gamma_{j+1}}\ \sum_{u\text{ at }v}
       \int_0^\infty e^{t b_j u x}f_{v,u}(x)\,dx .
 \tag{9}
\]
Own-side terms are \(L^2\) Fourier transforms. Damped terms are bounded Laplace transforms, since their squared norms are bounded by the quadratic form with kernel \(C/(x+y)\), bounded by Schur's test with weight \(x^{-1/2}\).

Let \(P\) project \(Y\) onto the real constant vector functions, and let \(\Pi\) project \(X\) onto \(\ker((I-P)T)\). Regard \(c=S^{-T}e_k\) as a constant function. Then
\[
 \boxed{
 E_k=\frac{M}{\sqrt N}\big(C_k+o(1)\big),\quad
 C_k=\|\Pi T^*c\|>0,\quad
 \lim_N\frac{E_{k,\mathrm{calibrated\ Ces}}}{E_k}
 =\frac{\|T^*c\|}{\|\Pi T^*c\|}>1.}
 \tag{10}
\]
The vector constant is \(\max_k C_k\).

**Explicit evaluation.** Partition \((0,1)\) into \(2^l\) equal intervals. Use the real and imaginary band integrals of (9) as rows, with atom matrix \(|I|S\) on real rows and zero on imaginary rows. Apply (8) with the Gram matrix on \(X\) and \(M=1\). The decreasing limit of the results is exactly \(C_k\), by weak compactness of the feasible balls and density of the nested dyadic steps. The constant tests already bound \(a\).

Each entry uses only elementary logarithms. The kernel for \([a,b]\) is \((e^{bzx}-e^{azx})/(zx)\), \(z=b_j u\). Its product integral with another interval is the double endpoint difference of
\[
 \frac{(-tz-t'w)\Log(-tz-t'w)}{zw},\qquad 0\Log0=0 .
\]
This follows by integration by parts and Abel limits. Replace \(w\) by \(\bar w\) for the Hermitian product. The dyadic rows are independent. At a vertex a dependence gives a bounded analytic sum of the two incident band integrals with zero real part on the wedge boundary. Poisson uniqueness and decay along the interior rays make it identically zero. Its frequency measure on two segments then annihilates analytic polynomials, which are dense on this compact tree. Thus its band coefficients vanish.

**Proof of the scaling limit.** At zero data give the background norm budget \(\sqrt N\). The supremum of \(|a_k|\) is \(\sqrt N E_k/M\). The atom vectors stay bounded. The real mean on its own side has norm at most \(\sqrt{|d_j|/N}\) by orthogonality. On an adjacent side it is bounded by \(C\min(1,1/(Nx))\) at distance \(x\) from the shared vertex, and elsewhere by \(C/N\). The mean atom matrix tends to the invertible \(S\).

Split each side at its midpoint and extend \(f_{v,u}(x)=N^{-1}g(v+ux/N)\) by zero past its half-edge. Then \(\|f\|_X\le1\). Pass to a weakly convergent subsequence. Testing the equations with \(N^{-1}\psi(m/N)\) for smooth compactly supported \(\psi\) gives \(Tf+Sa=0\). Indeed, on each own half-edge repeated summation by parts gives \(C_b(1+x)^{-b}\) up to \(N|d_j|/2\), before the next periodic copy. On damped half-edges one gets exponential decay. The Riemann-sum test functions therefore converge strongly in \(X\). This proves the upper bound by the continuum zero-data radius.

For the converse we need interpolation at uniformly bounded individual cost. For \(p=2k+1,\ \nu=mb_j\) set
\[
 D_\nu(s)=\frac{e^{\nu\gamma_j}L(s)}{(s-\nu)L'(\nu)}(s/\nu)^k .
 \tag{11}
\]
Its normalized samples are Kronecker deltas. Each complex multiple is represented by a real density with norm at most \(C_D\) times the modulus of the multiple. Its mass is zero. To verify the norm, use (3) and (5)–(6). On another ray the normalized modulus is bounded by \(C\sqrt m(1+t)^{-1/2}/(m+t)\) in ray-index units. On its own ray replace \(m+t\) by \(|m-t|\), using the sine zero in the middle range \(m/2<t<2m\) to obtain \(C/(1+|t-m|)\). The squared integrals are uniformly bounded.

Take a continuum feasible \((a,f)\). Average \(\lambda f(\lambda x)\) against a smooth probability density supported in \(1<\lambda<1+\epsilon\). These dilations preserve the equations on \((0,1)\), by evaluation at \(t/\lambda\). The averaged norm tends to \(\|f\|\) as \(\epsilon\downarrow0\). For fixed \(\epsilon\), its derivatives of order \(l=0,1,2\) are \(o(x^{-1/2-l})\) at infinity, by differentiation of the dilation kernel and Cauchy–Schwarz on \([x,(1+\epsilon)x]\). The transformed equations hold pointwise up to \(t=1\) by integration by parts on oscillatory tails.

Transplant \(Nf(Nx)\) onto each incident side with a smooth cutoff equal to one near the vertex and zero before the midpoint. Its norm is at most \(\sqrt N\|f\|\). The sum of the absolute normalized sample errors is \(o(\sqrt N)\). On an omitted oscillatory tail, two integrations by parts give \(o(\sqrt N)m^{-2}\), since the cut tail's second derivative has \(L^1\) norm \(o(N^{-3/2})\) in rescaled coordinates. Damped omitted tails give \(o(\sqrt N)e^{-cm}\). Nonincident transplanted pieces satisfy the same summable bound because \(\int_0^{CN}|f|=o(\sqrt N)\) and their supports stay away from the supporting line. Other atoms contribute \(O(e^{-cm})\). Formula (11) corrects all sample errors exactly at additional cost \(o(\sqrt N)\). The continuum and limiting discrete radii agree. Solving \(Sa=-PTf\) gives the projection in (10).

To prove positivity, any bounded data on the first \(N\) nodes can be interpolated at cost \(O_D(\sqrt N)\). In the sum of (11), extend the coefficients on each ray into \(N<m\le2N\) so that
\[
 \sum_{m\le2N}\frac{y_m e^{\nu\gamma_j}}{\nu^{k+1}L'(\nu)}=0 .
\]
The multipliers have magnitudes comparable to \(m^{-1/2}\). The added ones have total magnitude comparable to \(\sqrt N\), so bounded complex coefficients suffice. By \(1/(s-\nu)+1/\nu=s/[\nu(s-\nu)]\), this cancellation allows power \(k+1\) in the sum. For \(t\lesssim N\), away from comparable same-ray indices the normalized bound is \(C\sqrt t\sum_{m\le2N}m^{-1/2}/(m+t)\le C\). On a dyadic same-ray interval of scale \(J\), the common multiplier is bounded by \(C\sqrt J|\sin\pi t|\), and the comparable coefficients are \(O(J^{-1/2})\). Orthogonality of the integer sinc translates bounds the squared integral there by \(O(J)\). Sum over dyadic scales. For \(t\gg N\), the original power \(k\) gives \(O(N^{3/2}t^{-3/2})\). Formula (5) now bounds the squared spatial norm by \(O(N)\). Applying this to the data of a unit corner charge proves \(C_k>0\).

For calibrated Cesàro, the rescaled representing kernels converge strongly to \(T^*c\) using the square-integrable majorant \(C/(1+x)\). On an own half-edge the kernel is \(c_j\sin(|b_j|x)/(|b_j|x)\). Its other incident contribution has nonoscillatory tail \(c_l\Re[-1/(b_lu)]/x\). Thus the logarithmic coefficient of component \(j\) of \(TT^*c(t)\) at \(t\downarrow0\) is
\[
 L_j+L_{j+1},\qquad
 L_j=\sin\omega_j(c_{j-1}/|b_{j-1}|+c_j/|b_j|).
\]
A \(1/x\) tail gives \(\log(1/t)+O(1)\) in either the Fourier or damped Laplace limit, while the sinc tail stays bounded there. Invertibility of the odd cyclic sum map implies that vanishing of every logarithm would force first \(L_j=0\) for all \(j\), then \(c=0\). Therefore the projection in (10) strictly decreases the norm.

### B3. A shifted band on an even polygon

Put \(\beta_k=2-\omega_k/\pi\). With \(N\) shifted samples on a single edge in addition to all the integer samples,
\[
 \boxed{c_D M N^{-\beta_k/2}\le E_k\le C_D M N^{-\beta_k/2}.}
 \tag{12}
\]
For sufficiently large \(N\) the constants can be chosen uniformly in \(0<\theta<1\) in exact arithmetic. The slowest vector rate occurs at the largest interior angle. For fixed shift the calibrated Cesàro row still has order \(M/\sqrt N\). Its rescaled tangent kernels have finite norms, and the limiting kernel is continuous and equals one at the target corner. Its ratio to optimum therefore diverges with order \(N^{(\beta_k-1)/2}\).

**Proof.** Varga's arclength Christoffel estimate says that the minimum squared boundary \(L^2\) norm of a complex polynomial of degree \(\le n\) taking value 1 at a vertex of exterior-domain angle \(\beta\pi\) is comparable to \(n^{-\beta}\). Multiplication by a fixed vertex Lagrange polynomial imposes zero values at the other vertices for the same order. Two comparisons are needed to transfer this result to the exponential rows. [Varga, Theorem 2.4, Lemma 3.6 and Corollary 3.7](https://www.math.u-szeged.hu/pot/9VargaChristoffel.pdf)

Translate an interior disk about zero into \(D\). Let \(U\) be the monic product over the first \(J=\lfloor\kappa N\rfloor\) shifted nodes, with \(\kappa\) small enough that their moduli are at most \(b_*N/8,\ b_*=\min_j|b_j|\). Set \(F=LU\). Residues on large circles give
\[
 e^{tw}=\sum_{F(\lambda)=0}
       \frac{F(t)e^{\lambda w}}{(t-\lambda)F'(\lambda)},\qquad w\in\bar D .
 \tag{13}
\]
Indeed arbitrarily large circles avoid fixed small disks about the nodes, by their bounded radial counting density. By (3) the outer integral is \(O(R^{h-J})\) for fixed \(N,t\), and the series is absolutely summable for \(J>h+1\).

Truncate to measured rows. Every omitted \(\lambda\) has \(|\lambda|\ge b_*N\). For \(|t|\le\eta N\) and small \(\eta>0\),
\[
 |U(t)/U(\lambda)|\le(q b_*N/|\lambda|)^J,\qquad q<1.
\]
Using (3) for \(L'(\lambda)\), the summed tail is at most \(C e^{C_D\eta N}N^{h+1}q^J=O(e^{-cN})\) after choosing \(\eta\) sufficiently small. Cauchy differentiation in \(t\) approximates \(w^l\) by measured rows with error \(O(e^{-cN}l!(\eta N)^{-l})\). For \(P=\sum p_lw^l\), an interior circle of radius \(r\) gives \(|p_l|\le C r^{-l}\|P\|_{L^2(\partial D)}\). Summing to degree \(\eta rN/2\) gives uniform error \(O(e^{-cN}\|P\|_2)\). Approximate the fixed cardinal polynomials too. Their vertex matrix tends to identity, allowing exact correction of the exponentially small vertex discrepancies. Taking real parts proves the upper bound.

Conversely take a real row combination \(u=\Re f\) and set \(f_0=f-i\Im f(0)\). The conjugate-function bound under the centered disk map, now with weight \(|\Phi'|\in A_2\), gives \(\|f_0\|_2\le C_D\|u\|_2\). Thus \(f_0=O(\|u\|_2)\) on a smaller interior disk. On a fixed enclosing circle its size is at most \(e^{C_DN}\|u\|_2\). To see this independently of coefficient conditioning, take \(L_0=\lceil C_1N\rceil\) equal steps along a radius to that circle. The sampled values form a sum of \(q\le(p+1)N+1\) geometric sequences whose ratios have modulus \(\le B_D\). Choose \(C_1\) so the first \(q\) points lie in the interior disk. The generating function has denominator \(\prod(1-r_jz)\). Its numerator has degree less than \(q\) and coefficients bounded by \(C(1+B_D)^q\|u\|_2\) from those first values. On \(|z|=1/(2\max(1,B_D))\) its denominator is bounded below by \(2^{-q}\). Estimating coefficient \(L_0\) gives the assertion.

Choose the enclosing radius greater than twice the polygon radius. Taylor truncation at degree \(C_2N\) then has uniform error \(O(e^{-N}\|u\|_2)\). Varga's estimate bounds evaluation of this polynomial at \(\gamma_k\) by \(C N^{\beta_k/2}\|u\|_2\). Taking \(u(\gamma_k)=1\) in the extremal form of (8) proves the lower bound.

**Which shift?** The half-step maximizes \(|1-e^{2\pi i\theta}|\), the endpoint phase contrast. The full Gram matrix also changes with \(\theta\). On the unit square at \(M=1\) the interval certificate gives
\[
 .6612<E_\infty(1,1/2)<.6613,\qquad
 .6198<E_\infty(1,3/4)<.6200 .
\]
At \(N=2\) the maximum risks at a quarter-step and a half-step are \(0.38909512\) and \(0.40455410\).

There is an exact design-dependent prescription for finite optimization. Put \(J=\left(\begin{smallmatrix}G&A\\A^T&0\end{smallmatrix}\right)\), \(d=\det J\), and let \(d_j\) be minus its diagonal cofactor at atom coordinate \(j\). The squared normalized risks are \(d_j/d\). Check zeros of \(d\,d_j'-d_jd'\), crossings \(d_j=d_l\) for the maximum objective, endpoint limits and rank-loss points. Identical or constant active branches can be treated once. The elementary entries have real-analytic continuations across the endpoints, so each nonidentical numerator has finitely many roots. At the finer asymptotic scale the two polynomial comparisons in (12) use different multiples of \(N\). They leave the prefactor and its optimizer unresolved.

**One shifted sample behaves differently.**

- **Fixed frequency \(\xi\).** The transform \(q s^{k-1}(s-\xi)L(s)\), \(p=2k\), passes all integer tests and the extra test. Choose the phase of \(q\) to make its alternating masses real. The residual density is \(L^2\) by A2. Two rescaled opposite loads give a nonvanishing error floor for every \(N\). Integer-only data have the same obstruction and have infinite risk if the pure alternating atoms are invisible.
- **One point in the middle of the band.** For \((m+\theta)b_j,\ m/N\to t_0\in(0,1)\), the exact order is \(M/\sqrt N\). Subtract the rows \(m+l,\ |l|\le L_0\), with \(L_0\asymp N,\ m-L_0\ge cN,\ m+L_0\le N\), weighted by \(d_l=(e^{2\pi i\theta}-1)/(2\pi i(\theta-l))\). Fourier projection gives own-edge norm \(O(L_0^{-1/2})\). The endpoint values tend to opposite nonzero numbers since the symmetric Fourier sum at the jump is \((1+e^{2\pi i\theta})/2\). On adjacent sides, pairing \(l,-l\) gives \(C(1+L_0x)e^{-c(m-L_0)x}\), using \(d_l+d_{-l}=O(l^{-2})\). A real rotation, the integer means and vertex calibration give the upper bound. For the lower bound start with the integer-invisible measure with unit alternating masses. At the extra point each omitted cardinal (11) with even power \(k\) and index \(N<l\le2N\) on that ray has normalized modulus comparable to \(1/N\) by (2). Bounded complex coefficients therefore cancel its shifted response. Their summed real density has norm \(O(\sqrt N)\), by sinc orthogonality on comparable frequencies, the absolute bound \(O(1)\) on separated frequencies \(t=O(N)\), and \(O(N/t)\) for \(t\gg N\). Rescaling gives the lower bound.
- **Last shifted point \(m=N-1\).** The single omitted integer cardinal at \(l=N+1\) has shifted response bounded below and uniformly bounded spatial norm. The same-ray bound is \(C/(1+|t-l|)\), and on other rays it is \(C/(l+t)\). It cancels the shifted response at bounded cost. This placement again fails uniform consistency.

### B4. Smooth and analytic backgrounds

For one sample group write \(x_m=m\) or \(m-1+\theta\), \(t_m=x_m/N\). Choose a nonnegative smooth bump \(\chi\) supported in \([a,b]\subset(0,1)\), positive on an interval. For \(0\le l,j\le r\), set
\[
 H_{lj}=\sum_m\chi(t_m)t_m^{-l-j},\qquad h=H^{-1}e_0,\qquad
 w_m=\chi(t_m)\sum_{j=0}^r h_j t_m^{-j}.
 \tag{14}
\]
Then \(\sum w_m=1\) and \(\sum w_m x_m^{-l}=0\) for \(1\le l\le r\). For fixed \(r\), \(H/N\) tends to a positive definite Gram matrix. Hence \(\|w\|_1=O_r(1)\), \(\|w\|_2=O_r(N^{-1/2})\), and zero-extended differences of order \(b_0\) are \(O_r(N^{-1-b_0})\).

After vertex calibration, on bounded edgewise norm balls the rates are
\[
 O_{D,r}(N^{-r-1})\quad(C^r),\qquad
 O_{D,r}(N^{-r-1/2})\quad(H^r).
 \tag{15}
\]
Integrate by parts \(r\) times on each side. Each endpoint jet through order \(r-1\) is multiplied by \(x_m^{-l}\) and the exponential at that endpoint. The exposed endpoint factors are constant in \(m\), including the shifted phase, so all these terms cancel. Other endpoint factors are exponentially small. The own-edge remainder kernel against the \(r\)-th derivative satisfies
\[
 C_{b_0}N^{-r}(1+N\,\mathrm{dist}(t,\mathbb Z))^{-b_0}
\]
by summation by parts. The adjacent kernels have bound \(C N^{-r}e^{-cNx}\). Taking \(L^1\) and \(L^2\) norms proves (15), including weak integration by parts in the Sobolev case. These rates are sharp for this estimator. Its calibrated real row equals one at the target and has tangential Lipschitz constant \(O_r(N)\). An incident smooth bump of width \(\epsilon/N\) and height \(N^{-r}\) or \(N^{1/2-r}\) gives the two matching orders. Ordinary means allow a \(c/m\) endpoint term to contribute \(c(\log N+O(1))/N\).

For a uniformly bounded analytic extension to a fixed complex neighborhood of every closed side, **exponential exact-data accuracy is possible**. On a high band choose \(r+1\) equally spaced indices \(x_i=x_0+id\), \(d\asymp N/r\), and use
\[
 w_i=\frac{(-1)^{r-i}x_i^r}{d^r i!(r-i)!},\qquad 0\le i\le r .
 \tag{16}
\]
Use zero weights elsewhere. The \(r\)-th finite difference gives normalization and all the required cancellations. For \(r\le\epsilon N\), \(\sum|w_i|\le C_0^r\). Cauchy derivative estimates and \(r\) integrations by parts bound the remainder by \(C C_0^r C_1^r r!/(aN)^r\). The suppressed endpoint jets are bounded by \(C C_0^r e^{-cN}\sum_{l\le r}(C_1r/(aN))^{l-1}\). Both are exponentially small with \(r=\lfloor\epsilon N\rfloor\) for sufficiently small fixed \(\epsilon\). The off-face calibration terms obey the same exponential bound.

There is a cost for **any** window cancelling \(r\) powers exactly on \([aN,bN]\). It evaluates polynomials of degree \(\le r\) in \(N/x_m\) at zero. Use the Chebyshev polynomial taking \([1/b,1/a]\) to \([-1,1]\). Then
\[
 \|w\|_1\ge |T_r((a+b)/(b-a))|,\qquad
 \|w\|_2\ge |T_r((a+b)/(b-a))|/\sqrt N .
\]
Thus a fixed separated high band imposes exponential amplification in the cancellation order.

## C. The Laplace global relation and temperature jumps

### C1. The exact blind spot

For counterclockwise unit tangent \(t\), outward normal \(n=-it\), and real harmonic \(q\), Ashton uses \(\rho_j(\lambda)=\int_{\Gamma_j}e^{-i\lambda w}q_w\,dw\). Since \(q_w\,dw=(q_t+iq_n)d\ell/2\), at \(\lambda=is\),
\[
 2\sum_j\rho_j(is)=B_{q_t}(s)+iB_{q_n}(s)=0.
 \tag{17}
\]
The sample locations in Ashton's \(\lambda\) plane are \(imb_j=-2\pi m/d_j\), on the negative extension of his reconstruction ray of argument \(-\arg d_j\). The global relation holds for every complex parameter. At fixed Dirichlet data the residual difference is exactly \(iB_{\delta q_n}/2\). Its integer-sampled kernel on real \(L^2\) is therefore precisely the kernel in A. The underlying Dirichlet problem still has a unique physical Neumann trace. [Ashton, §2](https://arxiv.org/abs/1209.1584)

For \(p=2k\) or \(2k+1\), a minimal \(L^2\) completion is the real mass and the complex moments of degrees \(1,\ldots,k-1\). Since \(L(0)=1\), derivatives of \(QL\) give a triangular system for \(Q\). These are \(2k-1\) independent real conditions, the dimension lower bound. Their right-hand sides are obtained by differentiating (17). The physical total-flux equation already supplies the mass. For odd \(L^1\) and measures add the complex moment of degree \(k\). For even measures add the real component of that moment detecting the allowed leading-coefficient line.

A finite number of rows on unrestricted \(L^2\) always has infinite nullity. A finite trial space sees the continuous modes it contains. I used two independent affine traces per side, then enriched by the mass-one flux from A. On the unit square this flux is the torsion flux since the unit-area transform factors as \(L\). The other modes are \(n_x,n_y\). On the triangle the added mode is (5)–(6). The test compares orthogonal projectors onto nullspaces, since singular vectors can rotate within the square's three-dimensional subspace.

For \(q(w)=\Re(w^2+(0.3+0.2i)w)\), five frequencies per side, independent tangential data, and moment completion, the results were as follows.

| Domain | Affine-only nullity | Enriched nullity | Completed condition number | Maximum interior field error |
|---|---:|---:|---:|---:|
| Unit square | 2 | 3 | 16.45 | \(3.9\times10^{-16}\) |
| Equilateral triangle | 0 | 1 | 12.21 | \(2.4\times10^{-15}\) |

The enriched matrices before completion are singular in exact arithmetic. The flux errors on the affine part and enriched coefficient were below \(5.8\times10^{-14}\). Interior values were evaluated by Green's logarithmic representation. The nonpolynomial trial column was assembled by its exact transform. Independent checks used the physical square torsion sine series and a least-norm triangle density reconstructed from mass and sampled rows. The latter's transform error at \(0.91-0.52i\) fell from \(1.22\times10^{-5}\) at \(N=4\) to \(9.27\times10^{-9}\) at \(N=48\). In the continuous problem those least-norm reconstructions are projections onto increasing row spans whose joint orthogonal complement is zero after mass completion.

### C2. A plate with different constant wall temperatures

Let \(a_j=T_j-T_{j-1}\). The boundary tangential derivative is \(df=\sum a_j\delta_{\gamma_j}\), with \(\sum a_j=0\). At a corner write \(\varphi=0\) on the outgoing side and \(\varphi=\omega\) on the incoming side. The bounded Dirichlet solution satisfies
\[
 \begin{aligned}
 q&=T_j-a_j\varphi/\omega+O(r^{\pi/\omega}),\\
 q_{n,\mathrm{out}}&=a_j/(\omega r)+O(r^{\pi/\omega-1}),\\
 q_{n,\mathrm{in}}&=-a_j/(\omega r)+O(r^{\pi/\omega-1}).
 \end{aligned}
 \tag{18}
\]
Subtract the angular solution. The bounded remainder has zero values on both rays. The power map \(z^{\pi/\omega}\) straightens the sector, and odd harmonic reflection gives a removable bounded singularity. The Taylor expansion proves the remainder and its derivative estimate.

The jump flux belongs locally on each side to weak \(L^1\), fails \(L^1\), and fails weak \(L^2\). The angular solution has infinite Dirichlet energy. The two-sided finite part pairs the sides at equal physical radii.

For any entire analytic \(h\), excise small corner disks and apply Green's identity. The terms \(q\,\partial_n h\) on the small circles vanish by boundedness. The angular solution has zero radial derivative, and the remainder in (18) controls the other circle term. The two logarithmic divergences along the sides cancel. Since \(\partial_n h=-i\partial_t h\),
\[
 \langle {\rm fp}\,q_n,h\rangle
 =\int_{\partial D} f\,\partial_n h\,d\ell
 =i\langle df,h\rangle,\qquad
 \boxed{B_{{\rm fp}\,q_n}(s)=i\sum_j a_j e^{s\gamma_j}.}
 \tag{19}
\]

Thus the normalized integer Cesàro limit of the tangential transform is \(a_j+a_{j+1}\), by the bounded geometric mean. For the **normal finite part** it is \(i(a_j+a_{j+1})\) by (19). The shifted limit inserts \(e^{2\pi i\theta}\) at the terminal vertex. Odd plates reveal every jump. The even alternating direction survives the zero-sum constraint and disappears from all endpoint sums. Exact finite-frequency data can still see it when the pure-atom grouping test permits it. On the square every integer sample loses it exactly. The combined global-relation residual is identically zero, so reading jumps requires a separately observed spectral component or the prescribed temperatures. [Ashton and Fokas on distributional data and corner singularities](https://arxiv.org/abs/1301.1490)

I also evaluated the physical normal transform independently for triangle temperatures \((1,4,-2)\) and square temperatures \((1,4,-2,5)\). On the disk the Poisson solution gives radial flux density \(\sum a_j\cot((t-t_j)/2)/(2\pi)\) in principal value. Subtracting the test value at each pole gives a convergent integral. Mapping it to the regular polygons by the Schwarz–Christoffel arclength derivative proportional to \(|1-e^{ipt}|^{-2/p}\) gave discrepancies from (19) below \(6.5\times10^{-14}\) and \(7.2\times10^{-14}\), respectively, including shifted and off-grid tests.

## Numerical verification

All assertions passed with `python experiments/phase2_theorems.py`. The script uses 80-digit mpmath arithmetic for Gamma functions, small Gram matrices, residue interpolation and cancellation windows, 45-digit interval arithmetic for the shift counterexample, and NumPy/SciPy for the larger quadrature and SVD calculations. [Verification script](/Users/mw/Desktop/math/remath/experiments/phase2_theorems.py)

For the scalene triangle \(0,1.5+0.1i,0.2+1.1i\), at the origin:

| Quantity | \(N=4\) | \(N=12\) | \(N=32\) | \(N=64\) |
|---|---:|---:|---:|---:|
| \(\sqrt N E_k/M\) | .680890 | .673370 | .665516 | .660465 |
| \(\sqrt N E_{k,\mathrm{calibrated\ Ces}}/M\) | .762911 | .791685 | .806492 | .812491 |
| Finite ratio | 1.12046 | 1.17571 | 1.21183 | 1.23018 |

The independent tangent-ray Cesàro constant is \(0.821058200\). The dyadic formula gives **upper bounds** \(0.657442509,\ 0.649038254,\ 0.646252332\) for the optimal constant with 8, 32 and 64 bins. These give an asymptotic inefficiency ratio greater than \(1.2704\) to the displayed numerical precision. On the square, \(N^{3/4}E_\infty/M\) was \(0.68038,0.69335,0.71937,0.67671\) at \(N=2,4,8,12\).

The smooth-background tests used density \((1+j/4)e^{(j+1)t/5}\) on side \(j\), indexed from zero in fractional arclength. The charges were \((2,-1,3)\) and \((2,-1,3,-2)\).

| Polygon and band | Calibrated Cesàro error | Fixed \(r=3\) window | Extrapolation window |
|---|---:|---:|---:|
| Scalene triangle, \(N=32\) | \(5.76\times10^{-2}\) | \(4.50\times10^{-9}\) | \(1.45\times10^{-11}\) |
| Scalene triangle, \(N=64\) | \(3.37\times10^{-2}\) | \(2.78\times10^{-10}\) | \(3.96\times10^{-23}\) |
| Unit square, \(N=32\) | \(7.41\times10^{-2}\) | \(1.08\times10^{-8}\) | \(2.45\times10^{-11}\) |
| Unit square, \(N=64\) | \(4.32\times10^{-2}\) | \(6.81\times10^{-10}\) | \(5.60\times10^{-23}\) |

The extrapolation orders were 4 and 8. At \(N=64\) the largest group weight norm was \(9.40\times10^6\). That amplification is essential to interpreting the \(10^{-23}\) exact-data errors.

## Four Phase 3 Lean 4 targets

1. **Vertex grouping and cyclic parity.** Prove the Vandermonde grouping criterion for positive integer powers of distinct nonzero complex values. On cyclic indices derive the odd inverse of \(S\) and its even alternating kernel.
2. **Finite minimax recovery.** Formalize (8) on the finite row span, including the two indistinguishable opposite extremizers. Extend to a Hilbert background by orthogonal projection.
3. **Inverse-power cancellation.** Prove normalization and all vanishing moments in (16) over a characteristic-zero field using finite differences. Add the real Chebyshev lower bound on the weight norm.
4. **Triangle area nonvanishing.** Derive (7) on a reference triangle by elementary integration and affine change of variables. Prove nonvanishing at every integer node from the strict modulus inequality at the apex and nonparallelism of its two incident sides.