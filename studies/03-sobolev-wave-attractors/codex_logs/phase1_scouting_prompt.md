# Phase 1 Deep Scouting Prompt — Study #03: Sobolev–Aleksandryan–Zelenyak Rotating-Fluid PDE & Polygonal Wave Attractors

You are serving as the Mathematical Subcontractor (`gpt-6.2-astra`, max reasoning) for **Project ReMath Study #03 (`03-sobolev-wave-attractors`)** in `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors`.

## Strict Workspace & Quality Rules
- ONLY create/edit files inside the current working directory (`studies/03-sobolev-wave-attractors/`).
- We have archived 13 primary sources in `sources/papers/` (including Sobolev 1954, Aleksandryan 1960, Zelenyak 1965, Fokin 2001/2002, Nogueira–Troubetzkoy 2020 `2007.14773`, Lenci–Bonanno–Cristadoro 2021 `2102.01654`, Dyatlov–Wang–Zworski 2021 `2112.10191`, Li 2024 `2402.01896`).
- **CRITICAL NOVELTY BAR**: We MUST NOT merely restate Sobolev (1954), Aleksandryan (1960), Zelenyak (1965–70), Fokin (1981–2002), Maas–Lam (1995), Nogueira–Troubetzkoy (2020), Lenci–Bonanno–Cristadoro (2021 — rectangular trapezoid with 2 slopes $\Lambda^{\pm 1}$, odd-$q$ tongues / even-$q$ neutral), Dyatlov–Wang–Zworski (2021), or Li (2024).
- Hunt for **genuinely NEW, sharp, airtight, counterintuitive, quantitatively exact theorems** that simultaneously:
  1. Astonish a skeptical pure mathematician (exact necessary-and-sufficient criteria, exact algebraic formulas, exact spectral/PDE theorems in $H_0^1(\Omega)$),
  2. Shatter physical/dynamical intuition (shocking paradoxes, discontinuous phase transitions, exact reversals of symmetry intuition), and
  3. Can be explained vividly with concrete shocking numbers to a curious non-specialist.

## Mathematical Setting
Let $\Omega \subset \mathbb{R}^2_{x,z}$ be a bounded convex polygon. Consider Sobolev's 2D rotating/stratified fluid internal-wave operator
$$P := \partial_z^2 \Delta_\Omega^{-1} : H^{-1}(\Omega) \to H^{-1}(\Omega) \quad (\text{unitarily equivalent to } \Delta_\Omega^{-1}\partial_z^2 \text{ on } H_0^1(\Omega)),$$
which is bounded, self-adjoint, with $\sigma(P) = [0,1]$. Its spectral / stationary-mode equation at frequency $\lambda \in (0,1)$ is the hyperbolic Dirichlet problem
$$(1-\lambda^2) u_{zz} - \lambda^2 u_{xx} = 0 \quad \text{in } \Omega, \qquad u|_{\partial\Omega} = 0, \qquad u \in H_0^1(\Omega).$$
Set characteristic slope $c := \tan\theta := \frac{\lambda}{\sqrt{1-\lambda^2}} \in (0,\infty)$, $\theta \in (0,\pi/2)$, and characteristic coordinates $\ell_\pm(x,z) = z \pm c x$. The Aleksandryan–John boundary reflection involutions $\gamma_\lambda^\pm : \partial\Omega \to \partial\Omega$ preserve $\ell_\pm$, and the chess billiard / Aleksandryan map is $b_\lambda := \gamma_\lambda^+ \circ \gamma_\lambda^- : \partial\Omega \to \partial\Omega$ (an orientation-preserving piecewise-affine circle homeomorphism).

## Four High-Upside Frontiers to Scout, Derive & Numerically Probe
Write clean, self-contained, high-precision Python scripts in `experiments/phase1_probe.py` (using `mpmath` at 50–80 digits and/or exact `sympy`/rational arithmetic alongside fast NumPy phase-diagram scans) and report **complete, rigorous derivations + exact verified numbers** for ALL FOUR frontiers below, flagging clearly what is **PROVED**, what is **DISPROVED / CORRECTED**, and what is the **SINGLE SHARPEST BREAKTHROUGH THREAD**:

### Frontier 1: Exact Spectral & Billiard Anatomy of the Tilted Rectangle $\Omega(R,\phi)$ (and Tilted Square $R=1$)
Consider a rectangle $[0,1]\times[0,R]$ rotated counterclockwise by $\phi \in (0,\pi/4)$.
1. **Exact Normal Form of $b_{\theta,\phi,R}$**: Derive the exact piecewise-affine circle map (or exact first-return section map) in the supercritical window $\phi < \theta < \pi/2-\phi$, where slopes are built from $\mu(\theta,\phi) := \frac{\tan(\theta+\phi)}{\tan(\theta-\phi)} = \frac{\sin(2\theta)+\sin(2\phi)}{\sin(2\theta)-\sin(2\phi)} > 1$ (including pieces of slope $1$, $\mu$, and $\mu^{-1}$!).
2. **Arnold-Tongue Parity & Exact Closed-Form Laws**:
   - In Lenci–Bonanno–Cristadoro's rectangular trapezoid, odd $q$ give open tongues and ALL even $q$ give $f^q = \mathrm{Id}$.
   - **What is the EXACT rule on the tilted square ($R=1$) and tilted rectangle ($R \ne 1$)?!** Our preliminary check showed that on a $15^\circ$-tilted square, $q=2$ ($\rho=1/2$) IS a huge hyperbolic attractor with exact per-step Lyapunov exponent $-\ln\mu = -\ln 3$ at $\theta=\pi/4$, and $q=4$ is also a hyperbolic attractor!
   - Determine **for which $(p,q)$** the tilted square / tilted rectangle has: (a) open Arnold tongues with hyperbolic attractors, (b) degenerate neutral curves ($b^q = \mathrm{Id}$), or (c) **coexisting neutral beams and attractors**!
   - Derive **EXACT CLOSED-FORM** algebraic formulas for:
     - The Arnold tongue boundaries $\mathcal{T}_{p/q}(\phi, R)$ (at least for primary families $1/2, 1/3, 1/4, 2/5, 1/q, \dots$ and general structure),
     - The **EXACT quantized Lyapunov exponent** $\Lambda_{p/q}(\theta,\phi,R)$ (is the multiplier of EVERY hyperbolic attractor on a tilted rectangle an exact integer power $\mu^{-k}$, and what is the exact integer $k$ as a function of $(p,q)$ and parity?!).
   - **The Infinitesimal Tilt Catastrophe ($\phi \to 0^+$)**:
     - At $\phi = 0$: 100% pure-point spectrum (complete orthonormal basis $\sin(m\pi x)\sin(n\pi z/R)$), ZERO attractors.
     - For ANY $\phi > 0$: determine the exact measure of corner-black-hole frequencies ($[0,\phi) \cup (\pi/2-\phi,\pi/2]$) AND the exact asymptotics / total measure of periodic-attractor frequencies in $(\phi,\pi/2-\phi)$! Can you prove whether the total measure of attractor frequencies jumps discontinuously from **0 to 1** (100% of $(0,1)$!) at $\phi = 0^+$, OR compute exact explicit lower bounds / tongue-width scaling as $\phi \to 0^+$?
   - **Re-entrant Standing Modes**: On a fixed tilted rectangle $(R,\phi)$ with $\phi > 0$, does $\sigma_p(P)$ remain **EMPTY**, **FINITE**, or **COUNTABLY INFINITE** (with each eigenvalue of $\infty$-multiplicity!)? Find the EXACT condition on $(R,\phi,\theta)$ for $b_{\theta,\phi,R}^q = \mathrm{Id}$ or a nontrivial neutral cylinder!

### Frontier 2: Exact Polygonal Classification for Sobolev's Operator $P$ — "Total Annihilation of Standing Waves" vs. "Attractor-Free Polygons"
1. **Exact $H_0^1(\Omega)$ Eigenvalue Criterion (Aleksandryan–John–Fokin Bridge)**:
   - Give a completely rigorous theorem characterizing $\ker_{H_0^1(\Omega)}(P - \lambda^2)$ (finite-energy standing modes $u \in H_0^1(\Omega)$ solving $(1-\lambda^2)u_{zz} - \lambda^2 u_{xx} = 0$, $u|_{\partial\Omega}=0$) in terms of $b_\lambda$ and $\gamma_\lambda^\pm$ on an arbitrary convex polygon $\Omega$.
   - Specifically clarify:
     - Does an open **neutral periodic cylinder** $I \subset \partial\Omega$ (where $b_\lambda^q|_I = \mathrm{Id}$) ALWAYS yield an **infinite-dimensional subspace of $H_0^1(\Omega)$ (even $C^\infty$ on $\Omega$, vanishing outside the swept polygonal ribbon!)** eigenfunctions of $P$? Check the dihedral symmetry condition ($F \circ \gamma^+ = F$, $F \circ \gamma^- = F$) carefully!
     - Conversely, if EVERY non-periodic orbit of $b_\lambda$ converges to a finite set of attracting periodic orbits / attracting vertices (or if $b_\lambda$ is uniquely ergodic / minimal with irrational rotation number!), prove rigorously whether $\ker_{H_0^1(\Omega)}(P - \lambda^2) = \{0\}$! (Pay special attention to: (i) the critical frequencies where a characteristic is parallel to an edge, and (ii) minimal irrational orbits — can a weak $H_0^1$ eigenfunction exist when $\rho(b_\lambda) \notin \mathbb{Q}$?)
2. **Theorem Candidate — Total Annihilation of Standing Waves ($\sigma_p(P) = \emptyset$)**:
   - Test and attempt to PROVE:
     - **Every triangle** $\Delta \subset \mathbb{R}^2$ (arbitrary shape & orientation — including the $45^\circ$ right triangle obtained by cutting an upright square in half!) has **$\sigma_p(P) = \emptyset$** (ZERO finite-energy standing waves at EVERY frequency $\lambda \in [0,1]$)!
     - **Every rhombus / kite / quadrilateral** whose 4 vertices include two opposite corners that are extremal for BOTH $\ell_+$ and $\ell_-$ at all non-parallel $\lambda$ — in particular the **$45^\circ$-tilted square (diamond)**! — has **$\sigma_p(P) = \emptyset$**!
     - **WAIT — CHECK EVERY POSSIBLE EXCEPTION!** Could an obtuse/acute triangle or a special symmetric triangle EVER have a neutral period-2 or period-3 orbit at some $\lambda$? Check ALL orientations and ALL critical edge-parallel frequencies rigorously!
3. **Theorem Candidate — Uniqueness of Attractor-Free Convex Polygons**:
   - Prove or disprove: **Among ALL convex polygons $\Omega \subset \mathbb{R}^2$, Sobolev's operator $P$ is attractor-free across all $\lambda \in (0,1)$ (equivalently, no hyperbolic periodic orbit and no attracting corner exists at any $\lambda \in (0,1)$) IF AND ONLY IF $\Omega$ is an axis-aligned rectangle!**
   - Wait: Check axis-aligned polygons (Wait: convex axis-aligned polygon MUST be an axis-aligned rectangle!). Check **non-convex** axis-aligned polygons (e.g. L-shaped tank!) as a bonus surprise — what happens to Sobolev's PDE in an L-shaped tank with ONLY horizontal and vertical walls?!

### Frontier 3: Coexisting "Standing-Wave Cloaks + Black-Hole Wave Attractors" & Multi-Attractor Bifurcations
1. **Can an Infinite-Dimensional $H_0^1$ Standing-Wave Eigenspace Coexist with a Hyperbolic Wave Attractor at the EXACT SAME Frequency $\lambda$ in a Convex Polygon?**
   - In Lenci's rectangular trapezoid, neutral beams CANNOT coexist with hyperbolic attractors (either $f^q = \mathrm{Id}$ globally, or pure hyperbolic attractor).
   - What about a **symmetric pentagon, hexagon, chamfered rectangle, or tilted rectangle**?
   - Explicitly construct (if possible!) a simple, natural convex polygon $\Omega$ and explicit frequency $\lambda_*$ where $b_{\lambda_*}$ has BOTH:
     - A **non-degenerate neutral periodic cylinder** $I \subset \partial\Omega$ ($b_{\lambda_*}^q|_I = \mathrm{Id}$), supporting an **infinite-dimensional space of exact $C^\infty$/$H_0^1$ standing waves** strictly localized to a polygonal ribbon inside $\Omega$, AND
     - A **hyperbolic wave attractor** $\mathcal{A} \subset \Omega$ outside that ribbon, capturing all waves launched outside the ribbon!
   - If this exists, verify it BOTH symbolically and numerically (plot/print exact ribbon geometry, exact eigenfunction formula $u(x,z) = F(z+cx) + G(z-cx)$, and exact Lyapunov exponent of the coexisting attractor!).
   - If there is an obstruction forbidding it in certain polygons (e.g., all quadrilaterals or centrally symmetric polygons), PROVE that obstruction theorem!
2. **Sharp Multi-Attractor Coexistence & Symmetry-Breaking Splits**:
   - Earlier we saw a $5^\circ$-tilted regular pentagon at $c = 0.9$ had TWO distinct coexisting period-2 attractors with DIFFERENT Lyapunov exponents (`-0.517` vs `-2.316`)!
   - Investigate **coexisting distinct attractors** in symmetric vs. tilted regular $N$-gons (pentagon, hexagon, octagon) and general $k$-gons:
     - What is the sharp maximum number of coexisting attracting periodic orbits on a convex $k$-gon?
     - Can a **single symmetric tank** (vertical/horizontal symmetry) split into **asymmetric coexisting attractors** with different focusing rates or different basins, or exhibit a **symmetry-breaking Lyapunov cliff** under infinitesimal tilt?

### Frontier 4: The Regular $N$-Gon vs. Circle Spectral Paradox ($N \to \infty$) & Exact Comparison of Canonical 4-Gons
1. **Circle vs. Regular $N$-Gon Paradox**:
   - On the **circle** ($N = \infty$): Aleksandryan (1960) proved $P$ has a **100% pure-point** polynomial eigenbasis and **0%** attractors.
   - On a **regular $N$-gon** $P_N$ ($N = 3, 4, 5, 6, 7, 8, 10, 12, 20, \dots$):
     - Compute the **EXACT closed-form formula** for the fraction of characteristic angles $\theta \in (0,\pi/2)$ (and frequencies $\lambda \in (0,1)$) trapped in **corner black holes** ($\rho(b_\lambda) = 0$) as a function of $N$ and orientation $\phi$!
     - Compute the exact period-2 / period-$q$ Arnold tongues and Lyapunov exponents on $P_N$ as $N$ grows!
     - Test numerically and analyze theoretically: as $N \to \infty$, how do the corner-black-hole measure, the attractor frequency measure, and the maximum/typical Lyapunov exponent scale with $N$? Does an arbitrarily fine regular $N$-gon approximation of a circular tank STILL destroy the circle's standing-wave spectrum (e.g., full-measure attractors for every $N \ge 5$, or exact $O(1/N)$ vs $O(1)$ behavior)?!
2. **Exact Four-Way Comparison of Equal-Slope 4-Gons**:
   - Compare four canonical tanks with the exact same wall inclination angle $\alpha$ (say $\alpha = 15^\circ$ or general $\alpha \in (0,\pi/4)$):
     1. Upright Rectangle ($\phi = 0$)
     2. Rectangular Trapezoid (`| \`, 1 slanted wall)
     3. Symmetric Isosceles Trapezoid (`/ \`, 2 oppositely slanted walls)
     4. Sheared Parallelogram (`/ /`, 2 parallel slanted walls) & Tilted Square (4 rotated walls)
   - Determine the **EXACT Arnold-tongue parity rule**, **exact multiplier quantization**, **exact corner-black-hole range**, and **exact standing-wave existence** for EACH of the four! Look for shocking contrasts (e.g., does `/ \` flip parity relative to `| \` or `/ /`? Does `/ /` have strictly DOUBLE the focusing exponent of `| \`? Does adding a SECOND slanted wall to make the tank symmetric `/ \` paradoxically *create* or *destroy* standing waves?!).

## Deliverables Required From You
1. Create and run `experiments/phase1_probe.py` verifying every symbolic formula and numerical phenomenon to high precision (`mpmath` 50+ digits where exact constants/roots/Lyapunov exponents are computed, plus clean phase-diagram diagnostics).
2. Return a comprehensive, brutally honest, crystal-clear mathematical scouting report containing:
   - Exact statements of every **newly discovered theorem** (with complete proof sketches or full proofs, exact edge cases, and explicit novelty delta vs. Sobolev 1954, Aleksandryan 1960, Zelenyak 1965–70, Fokin 1981–2002, Nogueira–Troubetzkoy 2020, Lenci–Bonanno–Cristadoro 2021, DWZ 2021, Li 2024).
   - Every failed hypothesis or subtlety you caught (so we never fool ourselves!).
   - Concrete numerical tables & shocking numbers verified by `experiments/phase1_probe.py`.
   - Your candid recommendation for the **top 3–4 interconnected flagship theorems** that form an unforgettable, airtight, unified Study #03 package capable of clearing a unanimous 3-judge panel (layperson + pure mathematician + applied physicist).
