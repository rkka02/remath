# Research Log — Project ReMath (A. F. Leont'ev)

## 2026-11-23 — Session Start & Infrastructure Setup
- **Mission**: Excavate A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*, 1950s–1987, Ufa/Moscow), delegate heavy mathematical research/calculations/proofs to Codex (`gpt-6.2-astra`, `reasoning_effort=max`), steer toward a genuinely original, rigorously verified, and widely astonishing ("오오! 이런게 이렇게 된다고?") mathematical discovery, and keep everything version-controlled and archived.
- **Environment verified**:
  - Codex binary: `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex` (`codex-cli 0.171.0-alpha.13`) — verified working with `-m gpt-6.2-astra`. (Note: Homebrew's older `0.144.1` failed on `models_cache.json` / ChatGPT account routing; using the bundled newer binary solved it immediately.)
  - Python 3.13.11 with `numpy`, `scipy`, `sympy`, `mpmath`, `matplotlib`, `torch`.
  - Lean 4 toolchain (`lean`, `elan`, `lake`) installed.
- **Initial strategic scouting hypothesis**:
  - Literature scan confirmed **zero existing papers** bridging A. F. Leont'ev's 1966–1976 Soviet discrete exponential series on convex polygons with A. S. Fokas's Unified Transform Method (1997–2020s) for PDEs on convex polygons!
  - Additional high-upside frontiers to scout simultaneously before locking in:
    1. **Leont'ev $\leftrightarrow$ Fokas Exact Residue/Global-Relation Duality & Discrete Polygon PDE Solver** (and whether Leont'ev's *nontrivial expansion of zero* IS the exact discrete manifestation of Fokas's Global Relation!)
    2. **The Physics & Geometry of "Nontrivial Expansions of Zero"**: splitting a zero-expansion on an $m$-gon into $m$ half-plane waves ("Perfect Silence / Complex Wave Cloaking inside a Polygon") + gauge freedom / optimal sparse compression / stealth waves.
    3. **Breaking the Convexity Barrier**: non-convex domains via sheaf/Cousin gluing of convex Leont'ev expansions, overconvergence grouping, or Mittag-Leffler $E_\rho(\lambda_n z)$ $\rho$-convex curved domains.
    4. **Spectral Geometry & Quasicrystalline / Arithmetic Structure of Polygon Zero-Rays**: inverting the polygon from its frequencies, exact arithmetic/diophantine phenomena in $L(\lambda) = \sum a_k e^{v_k \lambda}$.
- **Next**: Excavate and archive authentic primary sources from Math-Net.Ru and arXiv, then launch Phase 1 Deep Scouting with Codex (`gpt-6.2-astra`, max reasoning).

## 2026-11-23 — Phase 1 Scouting Complete (Codex `gpt-6.2-astra`, `reasoning_effort=max`)
- **Primary Sources Archived**: 6 original Russian PDFs from Math-Net.Ru (Leont'ev 1969 *UMN*, 1969 *Mat. Sb.*, 1973 *Izv. AN SSSR*, 1987 *Tr. MIAN*, 1987 *Mat. Sb.*; Korobeinik 1981 *UMN*) + 2 arXiv PDFs (Ashton 2012, Ashton & Fokas 2013), with extracted text layers.
- **Key Verified Discoveries from Phase 1 (`codex_logs/phase1_scouting_output.md`, `experiments/phase1_probe.py`)**:
  1. **Exact Continuous-to-Discrete Leont'ev–Fokas Bridge**: Derived and verified the exact residue transfer formula turning Fokas's continuous outward-ray boundary transforms $R_j(s)$ into Leont'ev's discrete periodic edge-wave coefficients $c_\nu$ (double-precision quadrature error $2.24\times 10^{-10}$; 65-digit reconstruction error $1.55\times 10^{-49}$ on the square, $6.40\times 10^{-31}$ on the equilateral triangle).
  2. **Explicit Ghost Waves & Exterior Cancellation**: On the square, $G(w) = \sum_{m\ge 1} \frac{(-1)^m (2\pi m)^2}{2\sinh(\pi m)} e^{2\pi m w}$ satisfies $\sum_{\ell=0}^3 i^\ell G(i^\ell z) = 0$ (verified to $5.5\times 10^{-47}$ inside), continues meromorphically outside with triple poles, and its 4 continuations still cancel to $4.89\times 10^{-65}$ outside the square even where a single divergent-ray term has magnitude $5.27\times 10^{27}$.
  3. **Sharp Erasure Threshold**: Deleting $E \subset \Lambda$ preserves absolute representation in $H(D)$ iff $\#\{\nu \in E : |\nu| \le R\} = o(R)$ (verified by erasing all square-numbered modes $m = k^2$ on an edge and still reconstructing $1$ to $4.45\times 10^{-50}$). Also proved raw $\ell^2$/$\ell^1$ coefficient minimization fails to attain its infimum ($\inf\|c\|_2 = 0$, $\inf\|c\|_1 = |F(0)|$).
  4. **THE HEADLINE BREAKTHROUGH — Polygon Parity Paradox, Corner Recovery & Invisible Physical Loads**:
     - Universal vertex-sum limit on EVERY convex polygon: $\lim_{N\to\infty}\frac{1}{N}\sum_{m=1}^N e^{-\nu_{jm}\gamma_j} B(\nu_{jm}) = a_j + a_{j+1}$, annihilating arbitrary diffuse or singular-continuous background fluxes!
     - **Odd vs. Even Polygon Parity Paradox**: Odd polygons uniquely determine all corner charges; even polygons have an invisible alternating corner mode $(+1,-1,\dots)$, unmasked immediately by a **single half-step shift** ($m \mapsto m+\tfrac12$) on ONE edge (jumping from $0$ to $1.91357216$ at $m=0$ on the square!).
     - **Exact Box-Spline / Zonotope Classification on Centrally Symmetric $2k$-gons**: $L(s) = \prod_{r=1}^k \frac{\sinh(sd_r/2)}{sd_r/2} = \mathbb{E}[e^{s\sum d_r U_r}]$. Exact invisible load dimension is $2k-1$ for $L^1$/$L^2$ fluxes and $2k$ for signed measures.
     - **Stunning Physical Realization on the Square**: The 3 invisible continuous fluxes are literally $n_x$, $n_y$, and the **Saint-Venant elastic torsion / Poiseuille pipe shear stress** $-\partial_n u$ ($-\Delta u = 1, u|_{\partial D}=0$)!
- **Strategic Decision for Phase 2**:
  Unify these into a single flagship mathematical breakthrough centered on **"The Invisible Loads & Corner Parity of Convex Polygons under Leont'ev's Frequencies"** and push Codex Astra Max to solve the **3 genuinely deep open questions**:
  - (A) **Beyond Zonotopes**: What is the EXACT invisible load space (dimension + explicit physical/measure structure!) on **ARBITRARY convex $p$-gons** — specifically **triangles ($p=3$)**, **pentagons ($p=5$)**, and **asymmetric quadrilaterals/trapezoids**?! Does symmetry vs. asymmetry trigger a dramatic collapse or phase change in the invisible load space?!
  - (B) **Minimax Optimal Corner Recovery**: Prove the sharp information-theoretic lower bound (can ANY estimator beat $O(1/\sqrt{N})$ against $L^2$ background?) AND find whether optimal tapering/windowing achieves **super-resolution** ($O(N^{-s-1/2})$) against smooth ($H^s$/$C^k$) backgrounds, plus determine the exact minimax-optimal fractional shift $\theta^*$ for even polygons!
  - (C) **Direct PDE Application (Fokas Unified Transform Solver)**: Prove & demonstrate how the invisible loads create an exact rank deficiency / blind spot in Leont'ev-lattice Fokas Global Relation collocation on polygons, and how our minimal moment + single-half-step completion yields a provably nonsingular, spectrally accurate polygon PDE solver (including discontinuous-corner Dirichlet problems)!

## 2026-11-23 — Phase 2 Deep Theorems Complete & Independently Verified (`experiments/phase2_theorems.py`)
- **Breakthrough A — Universal Classification of Invisible Loads on ALL Convex $p$-gons**:
  - One-sided Leont'ev/Fokas lattice $\Lambda_+$:
    - Odd $p = 2k+1$: real $L^2$ dim $= 2k-1$, real $L^1$ dim $= 2k+1$ (a shocking 2D $L^1\setminus L^2$ singularity gap with $|z-v|^{-1/2}$ vertex blowup!), real signed measures dim $= 2k+1$.
    - Even $p = 2k$: real $L^2$ dim $= 2k-1$, real $L^1$ dim $= 2k-1$, real signed measures dim $= 2k$ (extra alternating corner mode — even on non-parallel asymmetric quadrilaterals, with compensating density!).
    - **Saint-Venant Torsion Test**: Invisible to $\Lambda_+$ **if and only if** $D$ is centrally symmetric! On the unit equilateral triangle, $B_{-\partial_n u}(2\pi i) = -\frac{\sqrt 3}{8\pi^2}(1 + e^{-\pi\sqrt 3}) \approx -0.02203174 \ne 0$, yet a **unique** distinct real invisible $L^2$ flux $g_\triangle$ still exists via the Gamma-product Laplace transform + Schwarz–Christoffel Hilbert pullback!
  - Two-sided reflected lattice $\Lambda_\pm$: ALL invisible real measures **collapse to 0** the instant central symmetry is broken (even for trapezoids or unequal-length parallel edges)!
- **Breakthrough B — Exact Minimax Optimality, Angle-Dependent Exponent Jump & Super-Resolution**:
  - Odd $p$-gons: sharp minimax rate $E_k = (M/\sqrt N)(C_k + o(1))$ with $C_k = \|\Pi T^* c\| > 0$, strictly beating calibrated Cesàro (ratio $> 1.27$ on scalene triangle).
  - Even $p$-gons with one shifted edge ($N$ shifted nodes): **breaks the $N^{-1/2}$ barrier!** Exact angle-dependent minimax exponent $E_k \asymp M N^{-(1 - \omega_k/(2\pi))}$ ($N^{-3/4}$ on a square!).
  - **Half-Step Suboptimality (Certified by 45-digit Interval Arithmetic)**: On the unit square at $N=1$, $\theta = 3/4$ gives $0.6198 < E_\infty < 0.6200$, strictly beating the half-step $\theta = 1/2$ ($0.6612 < E_\infty < 0.6613$)!
  - **Single-Shifted-Sample Phase Transition**: Fixed shift $\implies$ error floor $\Theta(1)$; end-of-band shift ($m=N-1$) $\implies$ error floor $\Theta(1)$; middle-of-band shift ($m \approx t_0 N$) $\implies$ restores $\Theta(N^{-1/2})$!
  - **Smooth-Background Super-Resolution**: Inverse-power-annihilating windows smash corner recovery error from $4.3\times 10^{-2}$ (Cesàro) to $6.8\times 10^{-10}$ ($r=3$) and $6.0\times 10^{-26}$ (order-8 extrapolation at $N=128$), with exact Chebyshev weight-norm lower bound $\|w\|_1 \ge |T_r((a+b)/(b-a))|$.
- **Breakthrough C — Fokas PDE Blind-Spot Removal & Discontinuous-Wall Metal Plate**:
  - Verified exact nullities (3 on square, 1 on equilateral triangle) before minimal $2k-1$ moment completion, collapsing condition numbers to $16.45$ and $12.21$ and interior Laplace field error to $3.9\times 10^{-16}$ and $2.4\times 10^{-15}$.
  - Proved exact Hadamard finite-part heat-flux identity $B_{\mathrm{fp}\,q_n}(s) = i\sum a_j e^{s\gamma_j}$ for discontinuous wall temperatures, independently verified via Schwarz–Christoffel Poisson kernel pullback to $< 7.2\times 10^{-14}$.
- **Next (Phase 3)**:
  1. Formal machine verification in **Lean 4.36.0** (zero `sorry`, standard axioms only) of the 4 core theorems in `proofs/lean4/`.
  2. Deep physical/geometric anatomy of the equilateral triangle's unique invisible $L^2$ flux $g_\triangle$ (checking chirality/mirror symmetry, sign changes, corner behavior) + two-slope **$60^\circ/120^\circ$ rhombus** numerical verification ($N^{-5/6}$ vs. $N^{-2/3}$ on the same polygon!) + full high-resolution visualization suite in `figures/`.
