## 1. REMAINING OR NEW BLOCKING DEFECTS

**Revision required.** All 48 tests passed, and all six named Round 2 counterexamples now give the expected results. Additional inputs still produce false half-period classifications. I also found a stronger corner-shaving bound that disproves an equality stated in the Korean feature.

### 1. The total corner-shaving liminf is strictly larger than the value stated in Korean Figure 2

The Korean caption and body say the **total** attracting-frequency liminf stays at \(C=17.8057725666\ldots\%\). Paper 2 correctly identifies \(C\) as the limit of its selected plateau sums. In fact, its own one-bevel argument gives a total liminf of **at least \(22.1940137673\ldots\%\)**. [Korean caption, line 144](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex:144) · [Korean text, line 158](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex:158) · [Paper 2, one-bevel proof, line 355](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex:355)

For coprime \(1\le m<n<1/\varepsilon\), put \(x=m/n\). Every slope in
\[
x<s<x+\min\!\left\{\frac{\varepsilon x}{n-\varepsilon},\frac{1/n-\varepsilon}{n}\right\}
\]
has deficit \(D=n-m/s\) satisfying \(0<D<\varepsilon\) and \(\varepsilon+sD<1/n\). These are precisely the inequalities used in the proof to separate visits to the bevel and produce a regular attracting orbit with zero kernel. Distinct reduced windings give disjoint intervals. This includes **parts of additional plateaus** for which the paper’s whole-plateau test fails.

Including the reciprocals gives frequency density \(g(x)=(1+x)/(1+x^2)^{3/2}\). Writing \(t=\varepsilon n\), the primitive-lattice sum uses \(\int_0^1\min\{x,1/t-1\}\,dt=\log(1+x)\). Hence
\[
\liminf_{\varepsilon\downarrow0}|\mathcal A_\varepsilon|_\lambda
\ \ge\ \frac6{\pi^2}\int_0^1 g(x)\log(1+x)\,dx
=\frac6{\pi^2}(\sqrt2-1)\log(1+\sqrt2)
=0.2219401376739817\ldots .
\]
At \(\varepsilon=1/512\), the enlarged sum is already \(22.12532861\%\). I also checked five additional intervals by exact rational chord iteration. The published \(17.72785286\%\) finite sum and Paper 2’s lower-bound theorem both reproduce. [Paper 2, lattice sum, line 359](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex:359)

### 2. `half_period_cells` still reports incorrect membership in both parity branches

The routine rounds the phase midpoint before generating events. The event bounds then enclose roots computed for that rounded midpoint. Three direct replays show the consequences. [Phase conversion, line 400](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:400) · [Even-event bounds, line 277](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:277) · [Odd-event bounds, line 348](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:348) · [Cell classification, line 452](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:452)

| Counterexample at 75 digits | Verified failure |
|---|---|
| Exact square phase `2**253 + 1` radians | Returns \((25.70175409^\circ,64.29824591^\circ)\) with no uncertainty. The square formula and a 225-digit replay give \((31.59402542^\circ,58.40597458^\circ)\). The routine incorrectly includes **\(60^\circ\)**. |
| Square radian interval \([3/8,3/8+2^{-251}]\) from a 100-digit interval context | Returns one cell with no uncertainty and includes \(\theta=\pi/4+3/8+2^{-253}\). The lower permitted phase excludes this angle and the upper permitted phase includes it. |
| Square \(22.5^\circ+10^{-69}{}^\circ\) and pentagon \(9^\circ+10^{-74}{}^\circ\) | The square cell includes \(22.5^\circ+0.9999995\cdot10^{-69}{}^\circ\), below its true lower endpoint. The pentagon omits \(45^\circ-0.96\cdot10^{-74}{}^\circ\) from both its cells and uncertainty bands. Direct 340-digit chord-map checks give **false** and **true**, respectively. |

The repair needs to carry the original phase enclosure through event generation and return `InsufficientResolution` whenever it cannot bound membership.

### 3. Both strip helpers still misround an exact `mpf` from another context

At 95 digits, let `one = mp.mp.clone().mpf(1)`. Its stored value is exactly one. `strip_coordinate(one, 1, 2**320-2)` returns \(1\), while the correctly rounded answer is \(1-2^{-319}\). For `strip_position`, take the exact `Fraction` \(a=2^{-319}+2^{-700}\). The exact exit is \(1+a\), just above a rounding midpoint. `strip_position(one, a, a)` returns \(1\), while the correctly rounded answer is \(1+2^{-318}\). Both failures also reproduce with the singleton interval `mp.iv.mpf(1)`. The exact conversion recognizes only the default context’s `mpf` class. [Type check, line 35](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:35) · [Position fallback, line 92](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:92) · [Coordinate fallback, line 128](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:128)

### 4. The half-rotation endpoint proof identifies the wrong diameter

Paper 2, Proposition 4.4, correctly restores ordered lifts and distinguishes vertex, face, tie, and zero-width endpoints. One geometric statement in the new proof is false. If the first involution is reflection in a line \(L\), then \(p'=-p\) puts \(p\) on **\(L^\perp\)**, the first-flight line. For the octagon with \(\phi=5^\circ\) at the upper endpoint \(\theta=50^\circ\), the reflection axis is \(140^\circ\). The \(50^\circ\) vertex maps under \(b\) to its antipode. The \(140^\circ\) vertex does not. Identifying the perpendicular diameter restores the endpoint argument and preserves the stated width. [Paper 2, line 473, PDF p. 17](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex:473)

### 5. Open Problem 2 still places eigenvalues in the angular set

The projection now correctly uses \(S_{R,\phi}=\{\cos^2\theta:\theta\in E_{R,\phi}\}\). The preceding sentence still says \(E_{R,\phi}\) contains the eigenvalues. For \(R=10,\phi=40^\circ\), the period-three eigenangle is \(0.7722552838579\ldots\) radians, with eigenvalue \(0.5131413660991\ldots\). Every angle in \(E_{R,\phi}\) exceeds \(40^\circ=0.6981317\ldots\) radians. The dense subset of \(E_{R,\phi}\) consists of **eigenangles**. [Paper 2, line 512, PDF p. 19](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex:512)

### 6. Two Korean figure labels retain the earlier mathematical claims

- **Figure 3A, p. 6.** The caption now labels \(u_h\) piecewise linear and finite energy, but “그 가운데” still identifies it as one of the preceding smooth modes. The profile derivative jumps from \(16\) to \(-16\) at \(13/16\). The plotted mode belongs to the same eigenspace as the smooth modes. [Korean caption, line 170](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex:170) · [Exact profile, Paper 1, line 256](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.tex:256)
- **Figure 4B, p. 8.** The prose correctly states \(b^2=\mathrm{Id}\) and infinite-dimensionality of the eigenspace. The embedded legend still reads “모든 고리 정상파” (“all circuits are standing waves”). The plotted zero exponent establishes that all ray circuits are neutral. [Figure generator, line 1034](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/generate_paper_figures.py:1034) · [Korean caption, line 201](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex:201)

## 2. ROUND 2 VERIFICATION MATRIX AND FINAL AUDIT SUMMARY

| Manuscript or figure item | Round 3 result |
|---|---|
| 1. Local dimension and spectral projection | **Partial.** The abstract requires \(\theta_c\in E_{R,\phi}\), and the projection uses \(S_{R,\phi}\). The eigenvalue sentence remains incorrect. |
| 2. Half-rotation endpoints | **Partial.** The ordered-lift exclusion and endpoint cases are present. The reflection-axis identification needs the correction above. |
| 3. Central symmetry | **Verified.** \(g_\pm(e)=e_z\pm se_x\) are defined. \(S_r\) preserves \(\xi\), and \(-S_r\) preserves \(\eta\). |
| 4. Corner shaving | **Partial.** The 39,797 reciprocal pairs give 79,594 intervals and \(17.72785286\%\). The midpoint factor and dyadic-sum wording are correct. The Korean total-liminf equality fails. |
| 5. Disk convergence and Figure 3A | **Verified.** Both Hausdorff distances equal \(1-\cos(\pi/N)\). The caption specifies interior-band convergence and uniform arclength launch. I reproduced the 32 clipped rates and the first rate \(1100.81608\). |
| 6. Figure 1A key and extinction horn | **Verified in print.** White is “other/unclassified,” singular pixels have a separate key, and the horn reaches \(45^\circ\). Two source comments retain the old description of white. [Generator, line 437](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/generate_paper_figures.py:437) |
| 7. Korean hexagon | **Partial.** Attraction, ordered half-heights, the circuit maximum, the possibility of a zero point reading, and the \(b^{2n}\) endpoint limit are correct. Figure 3A retains the smoothness contradiction. |
| 8. Korean physical geometry | **Verified.** The text specifies focusing incidence and body-frame square aspect. The arrows target \((0,0)\) and \((0.001^\circ,99.9982546555\%)\). |
| 9. Korean 1000/1002 comparison | **Partial.** The phases, finite factor \(0.333331148829275\ldots\), and \(U\sim\mathrm{Unif}(0,1)\) are correct. Figure 4B retains the standing-wave label. |
| 10. Chronology and priority | **Verified.** The 1943 completion, 1951 talk, 1952 account, and 1954 memoir are distinguished. The Korean text credits Poincaré and Stewartson, dates the 35 years from 1960 to 1995, and names all four experimental authors. [Sobolev’s author footnote](https://www.mathnet.ru/links/dfd8f998b18ad2225cd9a723173ce6f0/pmtf9593.pdf) · [Society minutes, p. 139](https://www.mathnet.ru/links/1d60c8f2e2ffcc68cec71c1702de204b/rm8284.pdf) · [Poincaré’s memoir](https://henripoincarepapers.univ-nantes.fr/chp/hp-pdf/hp1885ama.pdf) · [Stewartson, p. 283](https://a.tellusjournals.se/articles/2659/files/submission/proof/2659-1-45830-1-10-20221014.pdf) · [1997 experiment](https://www.nature.com/articles/41509) |

| Numerical or code item | Direct replay |
|---|---|
| 1. `strip_coordinate` | `1`, `1.0`, and `"1"` all give \(1-2^{-319}\) at 95 digits. The separate-context failure is documented above. |
| 2. `strip_position` | The named call gives exactly \(2^{321}+64\) at 95 digits. Both strip helpers also passed 350 independent rational comparisons. |
| 3. Coarse interval | The specified 10-digit enclosure raises `InsufficientResolution` at 75 digits. A narrower accepted enclosure still gives contradictory membership. |
| 4. Near-coincident events | The named square \(10^{-68}\) case retains an uncertainty band. Pentagon \(10^{-40}\) raises at 75 digits and resolves at 150 digits to endpoints \(45^\circ-10^{-40}{}^\circ\) and \(45^\circ+1.60357456591\ldots\,10^{-41}{}^\circ\). The 75-digit band for \(10^{-72}\) encloses the 300-digit cell. |
| 5. `wall_correction` | At \(N=10^{50}+2\), the scaled energy is \(32.55549387646022234227\ldots\), within \(3.5\times10^{-75}\) of independent 260-digit quadrature. The \(N=1002\) residual bound is \(0.0001306377586182534\). |
| 6. NumPy-backed `Fraction` | All five requested helpers passed direct exact comparisons, including `normal_return` and `section_tongue`. The original column height and section coordinate reproduce as \(9223372036854775815/2\) and \(11529215046068469762/5\). |

**Open Problem 3 removal verified.** Paper 2 §5.1 and PDF p. 19 contain exactly two problems. **All four non-blocking editorial repairs are present** in the compiled papers and plates. The legend cites Theorem 3.4, Figure 2C defines \(C,b\), the upright theorem specifies \(0<p<q\), and Korean line 139 gives both directed multipliers \(1/16,16\).

Two additional implementation issues concern input handling. `wall_correction(np.int64(1002))` raises `TypeError` at the conversion to `mp.mpf`. `section_tongue(Fraction(3,2),1,Fraction(2))` silently truncates the winding and returns the interval for \(m=1\). [Wall correction, line 503](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:503) · [Winding conversion, line 56](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_rectangle.py:56)

**Artifact and execution checks.** I rendered all **19, 20, and 8 pages**. All **10 embedded figures** match their source PNGs pixel-for-pixel, including alpha masks. Independent in-memory regeneration of `p2_fig1`, `p2_fig2`, and `kr_fig2` gave **zero differing pixels**. All TeX reference and citation keys resolve. The discovery suite passed **48/48** with the project’s Miniconda Python and `PYTHONDONTWRITEBYTECODE=1`. The default verifier and all eight chapter programs passed. Lean 4.36.0 re-elaborated the sources in memory, and all 125 public theorems reported only standard axioms. The Tectonic warning count comes from the supplied build. The audit made no file changes.