**All four Lean modules passed.** Lean 4.36.0 reported `Build completed successfully (12 jobs)`, with zero warnings, zero `sorry` occurrences, and zero custom axiom declarations. A fresh-kernel replay also passed. Of the 31 audited theorems, `Cycle.mod_index` used only `propext` and `Quot.sound`. The other 30 used exactly those two plus `Classical.choice`. [Full report and compilation transcript](/Users/mw/Desktop/math/remath/codex_logs/phase3_lean_and_anatomy_output.md) · [Lean audit driver](/Users/mw/Desktop/math/remath/proofs/lean4/Main.lean)

### Triangle flux

The mass-one invisible flux is **mirror-symmetric and strictly positive on every open edge**. Its midpoint value is \(0.43199552663931634\). At arclength \(x\) from either vertex,
\[
g_\triangle(x)=\sqrt{2/\pi}\,x^{1/2}+O(x^2).
\]
The numerical exponent was \(0.4999999724\). Positivity follows analytically by expressing the flux as the Poisson integral of a positive measure on the three vertex-to-centroid segments.

The independent 768-harmonic least-norm projection agreed within \(1.07\times10^{-5}\) on the middle 90% of an edge. The direct Cauchy–Laplace check agreed within \(3.80\times10^{-50}\). Both \(L^1\setminus L^2\) siblings have nonzero signed \(x^{-1/2}\) singularities on both sides of every vertex. The archive contains all twelve leading coefficients and 27-significant-digit profiles at 549 positions per edge. [Triangle arrays](/Users/mw/Desktop/math/remath/experiments/data/phase3_triangle.npz)

### Rhombus risks

The 100- and 132-digit computations agreed at all 45 saved significant digits for every risk. Vertices 0 and 1 are the endpoints of the shifted edge.

| \(N\) | Sharp 0 | Blunt 1 | Sharp 2 | Blunt 3 |
|---:|---:|---:|---:|---:|
| 2 | 0.297543 | 0.329437 | 0.384641 | 0.420274 |
| 4 | 0.183563 | 0.212085 | 0.225462 | 0.276781 |
| 6 | 0.127175 | 0.166360 | 0.170535 | 0.201798 |
| 8 | 0.097530 | 0.134887 | 0.119856 | 0.170470 |
| 12 | 0.068153 | 0.104066 | 0.087327 | 0.129868 |
| 16 | 0.053327 | 0.085047 | 0.068823 | 0.104223 |
| 20 | 0.044467 | 0.073686 | 0.055211 | 0.091207 |

The fitted exponents were **0.84293 and 0.84865** at the sharp corners, and **0.65268 and 0.67096** at the blunt corners. These support the predicted \(5/6\) and \(2/3\) orders on one polygon. Convergence of the normalized prefactors remains open. [Full-precision risks and scaled curves](/Users/mw/Desktop/math/remath/experiments/phase3_data.json)

### Square shifts and symmetry breaking

An outward-rounded certificate established the global result over \(0<\theta<1\) for each band.

| \(N\) | Best shift | Best \(E_\infty\) | Half-step \(E_\infty\) |
|---:|---|---:|---:|
| 1 | Infimum as \(\theta\uparrow1\) | 0.6098793956160494 | 0.6612539973234749 |
| 2 | Infimum as \(\theta\downarrow0\) | 0.3734754456819021 | 0.4045541022567613 |
| 4 | Unique interior minimizer at \(\theta\approx0.113299116655307389\) | 0.2421610914177466 | 0.2451356264257993 |

At bands 1 and 2, approaching an integer retains derivative information in the limiting measurements. Setting the shift exactly to that integer loses it. [Global optimality certificate](/Users/mw/Desktop/math/remath/experiments/phase3_square_certificate.py)

Tilting one square vertex lifted **all four** invisible measure modes linearly from zero. With six reflected harmonics per edge and the coefficient normalization documented in the report, the four initial singular-value slopes were **169.52610622, 6.92604454, 6.92604454, and 0.54905563**. The saved data include all 52 tilts and all 120 square shift designs. [Reproducible experiment](/Users/mw/Desktop/math/remath/experiments/phase3_anatomy_and_rhombus.py) · [Complete data](/Users/mw/Desktop/math/remath/experiments/phase3_data.json)