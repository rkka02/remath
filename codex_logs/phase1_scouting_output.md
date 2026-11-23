**Advance Candidate 4. A polygon’s edge frequencies can distinguish a charge at a corner from flux spread along the boundary. Whether they can identify every corner charge depends on whether the polygon has an odd or even number of sides.** On a square, four alternating corner charges pass every integer-frequency test exactly. Shift the frequencies on just one edge by half a step, and the first measurement reads **1.91357216** against an integer-grid reading of **zero**.

The proofs, source comparisons, and reproducible calculations are saved in the [full scouting report](/Users/mw/Desktop/math/remath/codex_logs/phase1_scouting_output.md) and [Python probe](/Users/mw/Desktop/math/remath/experiments/phase1_probe.py).

## Candidate 4 · What the polygon can hear

Let \(d_j=\gamma_{j+1}-\gamma_j\) be a counterclockwise edge and \(\nu_{jm}=2\pi i m/d_j\). For a finite real boundary measure \(\mu\), define
\[
B(s)=\int_{\partial D}e^{sw}\,d\mu(w).
\]
When two proposed Neumann traces have the same Dirichlet data and differ by \(d\mu=g\,d\ell\), their Fokas global relations differ by \(iB(s)/2\) at \(\lambda=is\). Thus \(B\) measures an actual ambiguity in the boundary data. [Ashton, §2](https://arxiv.org/abs/1209.1584)

Write \(a_j=\mu(\{\gamma_j\})\) for the charge at vertex \(j\). On **any convex polygon**,
\[
\boxed{\displaystyle
\lim_{N\to\infty}\frac1N\sum_{m=1}^N
e^{-\nu_{jm}\gamma_j}B(\nu_{jm})=a_j+a_{j+1}.}
\]

The proof explains why both endpoints appear. Put \(W=\exp(2\pi i(w-\gamma_j)/d_j)\). Convexity gives \(|W|\le1\). Both endpoints of the edge map to \(W=1\), and every other point of the closed polygon maps elsewhere. The bounded average \(N^{-1}\sum_{m=1}^N W^m\) therefore tends to the indicator of those two endpoints. Integrating proves the formula, even in the presence of an arbitrary singular continuous background.

Three consequences make this worth pursuing.

- **Odd polygons reveal every vertex charge.** On a triangle, for example, \(a_1=(S_1-S_2+S_3)/2\), where \(S_j\) is the measured endpoint sum. In a scalene-triangle test with charges \((2,-1,3)\) and unit flux density along the entire boundary, 1,024 frequencies per side recovered \((2.00117,-0.99830,3.00125)\) in the real parts.
- **Even polygons lose the alternating pattern in these averages.** Shifting \(m\) to \(m+\theta\) changes the limit to \(a_j+e^{2\pi i\theta}a_{j+1}\). A half-step on one edge supplies its endpoint **difference**. That one difference and the ordinary sums recover every corner charge.
- **The finite-band error has a sharp scale.** With an \(L^2\) background \(g\), its contribution to the average is at most \(C_D\|g\|_2/\sqrt N\). A unit-norm density concentrated on an edge interval of length \(1/(8N)\) attains this order. In the square experiment, multiplying the error by \(\sqrt N\) gave \(0.34802,0.34822,0.34828,0.34829\) at \(N=16,64,256,1024\). Sharpness here is for this explicit estimator.

There is also an exact answer for **all** the lattice samples on every centrally symmetric \(2k\)-gon. Write the centered polygon as the sum of segments \([-d_r/2,d_r/2]\), \(1\le r\le k\). Its Leont’ev symbol is
\[
L(s)=\prod_{r=1}^k\frac{\sinh(sd_r/2)}{sd_r/2}
=\mathbb E\,e^{s\sum_r d_rU_r},
\qquad U_r\ \text{independent uniform on }[-1/2,1/2].
\]
Thus the spectral symbol is the transform of a concrete probability distribution, the polygon’s box spline. [Box splines and zonotopes](https://arxiv.org/abs/1211.1187)

| Real boundary loads invisible at every lattice node | Exact dimension | Additional measurements that remove the ambiguity |
|---|---:|---|
| Integrable flux densities, also square-integrable densities | \(2k-1\) | Mass and complex moments of degrees \(1,\ldots,k-1\) |
| Finite signed boundary measures | \(2k\) | The same moments and one real component of the degree-\(k\) moment |

The proof divides \(B\) by \(L\). Vanishing at the lattice makes the quotient entire. Growth estimates force it to be a polynomial of degree at most \(k-1\) for densities. A degree-\(k\) term forces equal-magnitude alternating vertex masses. Conversely, replacing selected uniform segments in the box spline by differences of their endpoint masses produces every allowed polynomial multiplier. Moving the resulting interior measures to the boundary by harmonic measure preserves their transforms.

**On the square, the three invisible integrable fluxes have familiar meanings.** Two are the outward normal components \(n_x,n_y\). The third is \(-\partial_n u\) for the torsion problem \(-\Delta u=1,\ u|_{\partial D}=0\). Their transforms are \(sL(s),isL(s),L(s)\), respectively. In particular, \(+1\) on the right edge and \(-1\) on the left passes every lattice test **and** has zero total flux. Its first moment is exactly \(1\). Direct boundary quadrature gave a maximum normalized residual of \(5.98\times10^{-67}\) on 24 lattice nodes, while the off-grid measurement at \(s=1+0.4i\) was \(1.00032771+0.399048426i\).

**Novelty assessment.** Fulton, Fokas and Xenophontos already used the integer lattice for collocation, with endpoint information. A later scheme used half-steps for one part of the global relation. Sedletskii’s Hardy–Smirnov theory already anticipates the polynomial complement for square-integrable data. The research lead is the explicit identification of the invisible *physical loads*, the extra alternating mode introduced by corner atoms, and quantitative recovery in a diffuse background. I did not find that combination in the primary sources checked. Publication priority remains unverified. [Fulton, Fokas and Xenophontos](https://www.mas.ucy.ac.cy/xenophon/pubs/FFX.pdf) · [Half-step collocation](https://doi.org/10.1016/j.cam.2007.07.012) · [Sedletskii](https://www.mathnet.ru/eng/im1217)

## Candidate 1 · An exact bridge exists

Use \(s=i\lambda\) for the reconstruction and \(R_j(s)=\int_{\Gamma_j}e^{-sw}F(w)\,dw\). Ashton’s outward ray becomes \(\mathcal R_j=\mathbb R_+(i/d_j)\). For \(F\) holomorphic inside and continuous on the closed polygon, the transfer to Leont’ev coefficients is
\[
\boxed{\displaystyle
c_\nu=\frac{1}{2\pi i L'(\nu)}
\sum_j\int_{\mathcal R_j}\frac{L(s)R_j(s)}{s-\nu}\,ds,
\qquad F(z)=\sum_{\nu\in\Lambda} c_\nu e^{\nu z}.}
\]
For a general polygon the full-integer-lattice symbol is \(L(s)=e^{\tau s}\prod_j\Gamma(1-d_js/(2\pi i))^{-1}\), with \(\tau\) matching the polygon’s support function. I retained every positive node in the triangle calculation. Leont’ev’s 1987 printed construction removes one node when the number of sides is odd. [1987 survey, p. 322](/Users/mw/Desktop/math/remath/sources/papers/Leontev_1987_TrMIAN_176_rus.pdf) · [Leont’ev’s 1974 polygon theorem](https://www.mathnet.ru/eng/sm3472)

The residue identity behind the transfer is
\[
e^{sz}=\sum_{\nu\in\Lambda}
\frac{L(s)e^{\nu z}}{(s-\nu)L'(\nu)}.
\]
The outer contour vanishes uniformly on interior compact sets. The zero of \(L\) removes the apparent pole on an integration ray. The remaining ray integrand has an integrable \(O((1+|s|)^{-p/2})\) majorant after the edge-transform growth cancels. For traces analytic near the closure, the numerator of the coefficient is precisely Leont’ev’s node functional \(\omega_L(\nu,0,F)\). [Leont’ev’s interpolation construction](https://www.mathnet.ru/eng/sm3608)

The constant \(F=1\) disproves direct edge-by-edge sampling: **every own-edge sample \(R_j(\nu_{jm})\) vanishes**. The transfer works because every output coefficient uses all the input rays. The global relation holds for every analytic trace, whereas a synthesis null vector represents the zero field. Formula (3) of the report reconstructs from the complex boundary trace. Determining the missing Neumann data remains the PDE problem.

## Candidate 2 · An explicit ghost, with a sharp nonconvex obstruction

For positive-mode edge waves, the full synthesis kernel is
\[
c_\nu=\frac{A(\nu)}{L'(\nu)},\qquad
|A(s)|\le C_\epsilon e^{\epsilon|s|}\quad\text{for every }\epsilon>0.
\]
Korobeinik published the general classification. On the square, \(A=1\) gives a particularly transparent example:
\[
G(w)=\sum_{m\ge1}\frac{(-1)^m(2\pi m)^2}{2\sinh(\pi m)}e^{2\pi mw},
\qquad \sum_{\ell=0}^3 i^\ell G(i^\ell z)=0.
\]
Each wave continues meromorphically, with triple poles on a translated half-lattice. The continuations still cancel. At \(z=0.71+0.17i\), outside the square, the 40th term on one ray had magnitude \(5.27\times10^{27}\), yet the sum of the four *continued* waves had magnitude \(4.89\times10^{-65}\). [Korobeinik’s kernel theorem](https://www.mathnet.ru/eng/sm1316)

Convex gluing gives valid local representations on an L-shape. A single normally convergent exponential series extends to the interior of its convex hull by Hölder’s inequality. A pole placed in the missing notch, inside that hull, proves that local gauge freedom cannot produce a global series for every holomorphic function on the L-shape.

## Candidate 3 · A sharp erasure threshold and a failed compression principle

For the full polygon lattice, deleting \(E\subset\Lambda\) preserves absolute representation of every \(F\in H(D)\) **if and only if**
\[
\#\{\nu\in E:|\nu|\le R\}=o(R).
\]
Representing even \(1\) on the retained nodes gives, by differentiation, a nonzero ghost whose entire numerator vanishes on \(E\). Jensen’s formula gives necessity. Conversely, \(\prod_{\nu\in E}(1-s^2/\nu^2)\) has zero exponential type under precisely the stated counting bound and supplies a ghost on the retained system. The original \(L\) supplies the indicator hypothesis in Korobeinik’s representation theorem. Thus all square-numbered harmonics on one edge can be erased. Erasing a positive upper density prevents reconstruction even of \(1\). [Korobeinik, Chapter III §1](https://www.mathnet.ru/eng/rm2642)

A single nonzero ghost also determines the polygon’s **position**, provided its coefficients use a calibrated coordinate origin. In each ray direction \(u_j=\nu_{j1}/|\nu_{j1}|\), the supporting-line offset is
\[
h_D(u_j)=-\limsup_m\frac{\log|c_{jm}|}{|\nu_{jm}|}.
\]
The frequency spacings alone recover the directed side vectors and leave translation undetermined.

Raw coefficient minimization gives a cautionary result. On the centered square, \(\inf\|c\|_2=0\) for every represented function, and no nonzero function attains it. Also \(\inf\|c\|_1=|F(0)|\), which even \(F=1\) fails to attain. The proof combines the ghost classification with the Pólya–Valiron theorem on zero-type entire functions bounded on an integer lattice. [Pólya sequences](https://arxiv.org/abs/0903.4499)

## Numerical verdict and ranking

The residue checks used 65 decimal digits. An independent double-precision quadrature of the four continuous rays recovered a square coefficient to \(2.24\times10^{-10}\). [Reproducible probe](/Users/mw/Desktop/math/remath/experiments/phase1_probe.py)

| Modes per ray | Square ghost residual | Square exponential error | Square constant error after square-index erasure | Triangle exponential error |
|---:|---:|---:|---:|---:|
| 8 | \(2.48\times10^{-5}\) | \(3.89\times10^{-7}\) | \(1.73\times10^{-6}\) | \(1.74\times10^{-3}\) |
| 16 | \(5.06\times10^{-12}\) | \(4.89\times10^{-14}\) | \(2.45\times10^{-13}\) | \(1.90\times10^{-6}\) |
| 32 | \(7.54\times10^{-26}\) | \(3.66\times10^{-28}\) | \(8.76\times10^{-28}\) | \(1.66\times10^{-12}\) |

**Ranking: 4, 3, 1, 2.** The single Phase 2 target I recommend is **optimal recovery of polygon vertex charges from finitely many noisy Leont’ev-frequency measurements with an \(L^2\)-bounded background flux**. It has an explicit estimator, a sharp rate for that estimator, exact invisible loads, and a half-step measurement that resolves the even-polygon corner ambiguity. The open mathematical question is whether any estimator can improve the noise–resolution tradeoff.