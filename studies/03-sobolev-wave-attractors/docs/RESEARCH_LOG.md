# Research Log — Study #03: Aleksandryan–Zelenyak–Sobolev Spectral Billiards & Wave Attractors

## 2026-11-24 — Phase 0 Complete: Primary Excavation & Literature Audit
- **Archived 13 authentic primary PDFs** in `sources/papers/` and cataloged in `sources/PRIMARY_SOURCES.md`:
  - **5 Soviet/Russian classics (Math-Net.Ru)**: Sobolev (1954, *Izv. AN SSSR* 18:1, 48 pp.), Aleksandryan (1960, *Trudy MMO* 9, 51 pp.), Zelenyak (1965, *Dokl. AN SSSR* 164:6, 4 pp.), Fokin (2001, *Mat. Trudy* 4:2, 52 pp.), Fokin (2002, *Mat. Trudy* 5:1, 38 pp.).
  - **8 Modern bridges (arXiv)**: Colin de Verdière & Saint-Raymond (`1801.05582`), Dyatlov & Zworski (`1806.00809`), Nogueira & Troubetzkoy (`2007.14773`), Lenci, Bonanno & Cristadoro (`2102.01654`), Dyatlov, Wang & Zworski (`2112.10191`), Zhu under the direction of Li (`2210.13384`), Li (`2301.12365`), Li (`2402.01896`).
- **Literature Boundary Audited**:
  - Lenci–Bonanno–Cristadoro (2021) solved the supercritical rectangular trapezoid (2 slopes $\Lambda^{\pm 1}$: odd $q$ = open Arnold tongues with full measure, even $q$ = $f^q=\mathrm{Id}$).
  - Nogueira–Troubetzkoy (2020) proved general topological properties of chess billiards on circles, triangles, and squares. For the square, Theorem 13 gives an open dense subset of direction pairs $(\theta_1,\theta_2)$ with a periodic orbit. They also identify a countable family of neutral curves there.
  - Dyatlov–Wang–Zworski (2021) & Li (2024) established microlocal limiting absorption under fixed-$\lambda$ Morse–Smale assumptions.
- **Preliminary Python Sanity Probe**:
  - Observed exact $-\ln 3$ Lyapunov exponent on $15^\circ$-tilted square at characteristic slope $s=1$ ($\lambda=1/\sqrt{2}$, period 2 — flipping Lenci's trapezoid parity!).
  - Observed **two coexisting period-2 attractors with distinct Lyapunov exponents (`-0.517` vs. `-2.316`)** at characteristic slope $s=9/10$ ($\lambda=10/\sqrt{181}$) on a $5^\circ$-tilted regular pentagon!
  - Formulated 4 high-upside frontiers for Phase 1 Deep Scouting with Codex Astra Max (`gpt-6.2-astra`, `reasoning_effort=max`).

## 2026-11-24 — Phase 1 results

The [scouting report](phase1_scouting.md) indexes the proofs for all four frontiers. The [probe](../experiments/phase1_probe.py) reproduces the [results](../experiments/data/phase1_results.txt), the [hexagon with rational vertices](../figures/phase1_coexistence.png) and the [tilted-square phase diagram](../figures/phase1_square_tongues.png).

- Corrected the frequency convention from direct substitution. With \(s=\tan\theta\) measured from the physical horizontal, \(\lambda=\cos\theta\) and the spectral variable is \(\lambda^2\).
- A neutral interval away from characteristic sides gives an infinite-dimensional energy eigenspace. At a characteristic support edge the entire edge must carry constant boundary data. A common extremal corner suffices for uniqueness, yielding all triangles and the axis-diagonal diamond.
- A hexagon with rational vertices has an entire explicitly normed standing-mode space and a regular attracting circuit at the same frequency. The circuit halves one transverse displacement per round trip. Its basin has fraction \(1/2\) under uniform characteristic-offset launches. Arbitrary independent period-two multipliers coexist with a prescribed standing space at a sharp cost of \(m+5\) polygon sides for \(m\) attractors. A closed ray measures at least half the global peak of every standing mode.
- Every fixed reduced rectangle tilt \(0<\phi<\pi/4\) has full frequency measure of corner or regular periodic capture. At a fixed reduced tilt \(0<\phi<\pi/4\), its point spectrum is empty precisely for \(\cot(2\phi)\le R\le\tan(2\phi)\), and countably infinite (each eigenvalue of infinite multiplicity) for the complementary aspect ratios \(R<\cot(2\phi)\) or \(R>\tan(2\phi)\) (with \(\phi\ge\pi/8\) required for the extinction range to be nonempty). Kopecz and Bajars–Frank–Maas contain substantial earlier square results. The complete fixed-tank measure and point-spectrum proofs are linked in the report.
- The four axial support edges protect a tank from common supporting corners. Additional oblique edges force regular attracting periodic rays. The upright rectangle is the sole attractor-free convex polygon. Orthogonal polyominoes can be nonconvex, with the same point-spectrum set as one mesh rectangle.
- In the axis-aligned square with one shrinking corner cut, a family of explicit rational plateaus alone has limiting physical-frequency measure \(6(1-1/\sqrt2)/\pi^2\), about \(17.81\%\). In a centrally symmetric tank the sharp cost of \(m\) four-reflection attractors with a neutral beam is \(2m+6\) sides.
- At \(\lambda=1/\sqrt2\), every transverse odd regular \(N\)-gon attains the \(N-3\) maximum. Generic even regular polygons have \(N/2-1\) attractors. The aligned regular \(1002\)-gon has 500 at that one frequency, while an explicit Dirichlet quasimode has relative residual below \(0.000131\). The all-period attraction measure for arbitrary regular polygons remains undetermined.
- The regular-polygon measure of all periods up to \(Q=o(N/\sqrt{\log N})\) tends to zero uniformly in orientation. At half-frequency on aligned \(N=4j+2\) polygons, the median exponent under uniform arclength launch is asymptotic to \(-2\sqrt2\pi/N\).
- Use the captured [verification output](../experiments/data/phase1_results.txt) when quoting a multiplier, rotation convention or empirical count. Mathematical novelty against the checked sources and the outstanding historical priority checks are documented in the report.

## 2026-11-24 — Phase 2 repairs to the Phase 1 referee report

The period-three corner-cut theorem requires an axis-aligned parent rectangle and a proper straight cut. The cut tilted diamond has a common supporting vertex at every transverse slope. At a characteristic edge the \(k-3\) bound applies separately to attracting and repelling cycles. The test hexagon has two of each. The \(N/2-1\) count at half-frequency requires an even regular polygon. [Referee report](../codex_logs/phase1_verify_output.md) · [Corner-cut theorem](phase1_pde.md) · [Cycle bound](phase1_multiple.md)

The boundary verifier preserves every distinct rational knot and tests rational displacements exactly. For rounded geometry it encloses the errors in both lifts and in breakpoint positions. At \(s=1+10^{-60}\) the exact upright square excludes period two, and the 72-digit census is unresolved. The branch-seam regression checks evaluation and inversion at 95 digits. The chapter regressions also cover winding reversal, neutral interval endpoints, decimal rounding ties, empty resonance grids and insufficient re-entry precision. [Regression tests](../experiments/test_phase1_repairs.py)

The scouting and chapter notes now specify the streamfunction and distribution realizations, the reduced tilt, boundary and section rotations, and the interior trace obstruction for the separated products on the L triomino. The source comparisons distinguish the published break-return equations, Kopecz's arbitrary-\(k\) family, the square parity discussion, fixed-group dimension bounds and prior numerical work on fixed squares. [Scouting report](phase1_scouting.md) · [Primary-source catalog](../sources/PRIMARY_SOURCES.md)

The square portrait singles out all 900 critical grid samples and 450 primary endpoints. Every colored higher-period sample passes strict outward-interval endpoint tests. [Phase portrait](../figures/phase1_square_tongues.png)

The full verification command `python3 experiments/phase1_probe.py --scan --figure` exited 0. All eight chapter programs and 29 regression tests passed. The nine scan rows reproduce 496 corner samples, 402 isolated low-period samples and 182 unresolved candidates out of 1,080. Both regenerated figures were inspected. [First repair report](../codex_logs/phase2_repairs_output.md)

## 2026-11-24 — Phase 2 certification repairs, round 2

The upright square at exact slope \(1\) certifies period two. A tangent computed at 15 digits and passed to the 72-digit verifier now requires an enclosure. With a radius covering the intended slope, the square and aligned dodecagon both give an unresolved numerical identity test. The angular scan constructs vertex and slope intervals directly from rational multiples of \(\pi\). The lift comparison uses a single integer translation over the full period and accounts for a possible change of lap in independently normalized lifts. [Boundary verifier](../experiments/phase1_probe.py)

The finite-itinerary test assumes a convex polygon. In the audit’s notched hexagon the horizontal flight reaches \(x=3/4\) before its formal target at \(x=-3\). The scouting and chapter notes also specify the reduced tilt, denominator parity, self-reversing section orbits, rational vertex coordinates and the scope of the cited square results. [Scouting report](phase1_scouting.md) · [Audit counterexamples](../codex_logs/phase2_verify_output.md)

The rotated square at vertex phase \(10^{-8}\) degrees has four interior fixed points of the second return. The octagon at \(10^{-40}\) degrees has twelve. Its computed tongue endpoints resolve \(45^\circ\pm10^{-40}\) degrees. The regression suite also checks the exact integer rectangle and reflection, the checkerboard floor and the primary tongue at aspect one and tilt \(10^{-25}\) radians. [Regular-polygon calculation](../experiments/phase1_regular.py) · [Regression suite](../experiments/test_phase1_repairs.py)

Both requested commands exited 0 under the project’s Miniconda Python. All 45 regressions, eight chapters and four additional resonance runs passed. All nine scan rows match the scouting table. Among the 1,080 midpoint samples, 496 had a common supporting corner, 402 had isolated low-period orbits and 182 remained unresolved by the finite test. [Full scan transcript](../experiments/data/phase1_results.txt)

The independent read-only referee returned **CLEAN — READY TO PITCH** for all eight repair items. [Verification certificate](../codex_logs/phase2_verify_r2_output.md)

## 2026-11-24 — Phase 3 standalone Lean formalization

The half-amplitude bound holds for any detector level and any nonempty list of boundary values, with equality exactly at the midrange. Four-chord intersections give the hexagon return $y'=1/8+y/2$ and the centrally symmetric octagon return $y'=3/16+y/4$. The hexagon profile reaches 2 in the interior and 1 on the attracting circuit. The isolated hexagon basin has half the launch mass. [Uncloakability](../proofs/lean4/Uncloakability.lean) · [Multiplicity bounds and octagon](../proofs/lean4/MultiplicityBounds.lean)

In the exact tilted square a single boundary step exchanges $1/3$ and $7/3$. The second iterate fixes both with multiplier $1/16$ and fixes $4/3$ and $10/3$ with multiplier $16$. For each of the four canonical families, the regular-interior theorem constructs an attracting fixed point from any regular fixed sample under the finite affine and fixed-corner hypotheses, and gives the physical return on its whole cell. The corner-shaving proof bounds the displacement for every lift of every proper block and deduces at most one bevel visit per winding cycle. [Parity and square returns](../proofs/lean4/TiltedParity.lean) · [Corner-shaving proof](../proofs/lean4/CornerShavingAndTriangles.lean)

The required clean build exited 0 on Lean 4.36.0. All 125 public theorems, including 40 main results, passed the axiom audit. An isolated copy also passed with warnings treated as errors, and `leanchecker` replayed all five modules. [Theorem statements and kernel output](phase3_lean4_inventory.md)


## 2026-11-24 — Unanimous 3-Judge Gate, Phase 4 Publications & 8-Round Read-Only Astra Referee Sign-Off

- **Unanimous 3-Judge Wow-Factor Panel (`Round R1`)**: Passed unanimously 3/3 (`@judge-layperson`: 9.4, `@judge-theorist`: 9.3, `@judge-phenomena`: 9.3; Board `#14–#16`, milestone `#17`).
- **Three Non-Overlapping Manuscripts & Ten Dedicated Publication Figures (`47 pp.` total, 0 TeX errors, 0 Overfull warnings, 0 matplotlib warnings)**:
  1. [`papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.pdf`](../papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.pdf) (**19 pp.**, `amsart`) + 3 dedicated figures (`p1_fig1`–`p1_fig3`).
  2. [`papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.pdf`](../papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.pdf) (**20 pp.**, `amsart`) + 3 dedicated figures (`p2_fig1`–`p2_fig3`).
  3. [`papers/expository_kr/expository_sobolev_attractors_kr.pdf`](../papers/expository_kr/expository_sobolev_attractors_kr.pdf) (**8 pp.**, `xeCJK`) + 4 dedicated figures (`kr_fig1`–`kr_fig4`).
- **Iterative Read-Only Codex Astra Max Referee Audit (`phase4_referee_r1` through `phase4_referee_r8`)**:
  - **Rounds 1–4**: Closed all manuscript, theorem, citation, figure, and Lean 4 items (including replacing the solved $L^2$ error constant $\sqrt{\pi^4/30 + 17\pi^2/12 - \zeta(3) - 12} \approx 2.00670186$ out of Paper 2's Open Problems). Round 4 (`codex_logs/phase4_referee_r4_output.md`) granted **zero-defect acceptance** to all 3 PDFs (19 + 20 + 8 pp.), all 10 embedded figures (verified pixel-for-pixel including alpha), and the Lean 4.36.0 formalization (125 public theorems, 40 principal results, 0 `sorry`, standard axioms only).
  - **Rounds 5–8**: Hardened every numerical edge case in `experiments/phase1_regular.py` and `experiments/phase1_measure.py` (exact outward boundary slivers in `half_period_cells`, lazy mathematical constants across default and cloned contexts, exact rational slope ratios including `mp.degree / mp.pi = 1/180`, 170,000+-bit adaptive refinement budget, near-pole `parameters`, exact `involution` / `circle_distance` / `corner_widths`, outward-rounded `--tongues` decimal brackets, `mpq` / NumPy `longdouble` portability, and strict input validation), expanding `experiments/test_phase1_repairs.py` to **53/53 passing tests**.
  - **Round 8 Final Verdict (`codex_logs/phase4_referee_r8_output.md`)**: **`ZERO BLOCKING DEFECTS — ACCEPT AS IS (PUBLICATION SIGN-OFF GRANTED)`**.
