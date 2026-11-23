# Phase 3 Research & Formal Verification Brief — Project ReMath (A. F. Leont'ev)

You are `gpt-6.2-astra` (max reasoning), continuing Project ReMath in `/Users/mw/Desktop/math/remath`.
Phase 2 (`codex_logs/phase2_deep_output.md`, `experiments/phase2_theorems.py`) was independently executed and every single assertion passed!

Now in **Phase 3**, we execute TWO high-impact deliverables that will make our discovery completely bulletproof, formally verified, and visually astonishing:

---

## Part 1: Formal Machine Verification in Lean 4 (`proofs/lean4/`)

Lean 4 (`lean --version` = `4.36.0`) is installed locally on this Mac!
Create a **self-contained, zero-external-dependency** Lean 4 verification package in `proofs/lean4/` (using ONLY pure Lean 4 standard library / `Init`, so it builds instantaneously offline via `lean proofs/lean4/...` or `lake build` with ZERO `sorry`, ZERO `axiom` declarations, and verified via `#print axioms` to use at most standard axioms `propext`, `Classical.choice`, `Quot.sound`!).

Formalize and machine-check ALL FOUR core algebraic/structural theorems of our discovery:

1. **`PolygonParity.lean` — Odd/Even Cyclic Incidence & Single-Shift Unmasking Theorem**:
   - Define the cyclic vertex-edge sum operator $(S a)_j = a_j + a_{(j+1) \bmod p}$ over `Rat` (or any field / commutative ring with `2 ≠ 0` — `Rat` or a clean abstract `Field`-like structure or `Rat` with exact algebraic proofs is super clean in pure Lean 4!). Even better: prove it over an abstract `CommRing` / `Field` class (or `Rat` + `ComplexRat` = $\mathbb{Q}[i]$ so shifts like $\zeta \in \mathbb{Q}(i)$ work cleanly!).
   - Prove:
     - **Odd $p = 2k+1$**: $S$ is injective AND surjective, with the explicit closed-form inverse formula $a_j = \frac{1}{2}\sum_{r=0}^{2k} (-1)^r (S a)_{(j+r)\bmod p}$.
     - **Even $p = 2k$ ($k \ge 1$)**: Every vector $a$ in $\ker(S)$ satisfies $a_j = (-1)^j a_0$, and conversely $a_j = (-1)^j c$ lies in $\ker(S)$ (so $\ker(S)$ is exact 1-dimensional!).
     - **Single-Shift Unmasking Theorem**: For even $p = 2k$, augmenting $S a = b$ with ONE shifted edge equation $a_0 + \zeta a_1 = d$ for ANY $\zeta \neq 1$ makes the system **injective** with explicit recovery $a_0 = \frac{d - \zeta b_0}{1 - \zeta}$ (and in particular for half-step $\zeta = -1$, $a_0 = (d + b_0)/2$, $a_1 = (b_0 - d)/2$, and all $a_j$ recovered inductively!).

2. **`FiniteMinimax.lean` — Exact Minimax Optimal Recovery & Nonlinear Lower Bound Theorem**:
   - Formalize the core Hilbert/Euclidean optimal recovery theorem behind Equation (8):
     - Given linear measurement map $y = A a + R g$ (over $\mathbb{R}$ modeled cleanly via an abstract ordered field / `Rat` inner-product space, or an exact finite-dimensional inner-product / Cauchy-Schwarz formulation over `Rat` or an abstract `ArchimedeanOrderedField`!).
     - Prove BOTH halves:
       1. **Upper bound**: Any linear estimator $\hat{a}_k = \langle w, y \rangle$ calibrated so $A^T w = e_k$ has worst-case error $\sup_{\|g\| \le M} |\hat{a}_k(A a + R g) - a_k| \le M \|R^* w\|$.
       2. **Universal Nonlinear Lower Bound (Indistinguishable Opposite Witnesses)**: If there exists a nonzero pair $(a^*, g^*)$ with $A a^* + R g^* = 0$ and $\|g^*\| \le M$, then for **ANY function whatsoever** $\Phi$ (linear OR completely arbitrary nonlinear estimator!), $\max(|\Phi(0) - a_k^*|, |\Phi(0) - (-a_k^*)|) \ge |a_k^*|$!
       3. **Exact Saddle-Point Equality**: When $w^*$ satisfies $A^T w^* = e_k$ and $R^* w^* = -c g^*$ (the normal equation $G w^* = A K e_k$ with $a^* = M K e_k / \sqrt{K_{kk}}$, $g^* = -R^* w^* M / \|R^* w^*\|$), the upper bound and universal nonlinear lower bound **COINCIDE EXACTLY**, proving no nonlinear estimator can beat the linear minimax estimator!

3. **`SuperResolutionWindow.lean` — Exact Inverse-Power Cancellation Identity**:
   - Prove over `Rat` (for all $r \in \mathbb{N}$, $x_0, d \in \mathbb{Q}$ with $d \neq 0$ and $x_0 + i d \neq 0$ for $0 \le i \le r$) that the explicit extrapolation weights
     $$w_i = \frac{(-1)^{r-i} (x_0 + i d)^r}{d^r \, i! \, (r-i)!}$$
     satisfy:
     - **Exact normalization**: $\sum_{i=0}^r w_i = 1$, AND
     - **Exact annihilation of all $r$ inverse powers**: $\sum_{i=0}^r w_i (x_0 + i d)^{-l} = 0$ for every $1 \le l \le r$!
   - *(Tip: Notice this is equivalent to the classic $r$-th forward finite difference of the polynomial $P(i) = (x_0 + i d)^{r-l}$ vanishing for $0 \le \deg P < r$ and equaling $r! d^r$ for $\deg P = r$! That proof in pure Lean 4 is clean, elementary, and 100% airtight!)*

4. **`TwoSidedSymmetry.lean` — Symmetry-Breaking Collapse & Pure-Atom Grouping Algebra**:
   - Prove in Lean 4 the exact arithmetic lemma behind the two-sided lattice collapse: if positive rationals/reals $a, b$ satisfy that $m b / a$ and $m a / b$ are integers for two consecutive integers $m$ and $m+1$, then $a = b$!
   - Prove that if a convex $2k$-gon has opposite directed edges equal in magnitude and opposite in direction ($d_{j+k} = -d_j$ for all $j$), then $\gamma_j + \gamma_{j+k}$ is independent of $j$ (central symmetry!).
   - Prove the algebraic Vandermonde non-degeneracy / grouping lemma for pure corner atoms (or the exact equilateral-triangle Stokes area formula non-vanishing identity on the positive ray!).

Create a master file `proofs/lean4/Main.lean` (or `AllTheorems.lean`) that imports all four modules and prints `#print axioms` for every major theorem, AND run `lean` / `lake build` to verify **zero errors, zero warnings (or clean build), and zero `sorry`**!

---

## Part 2: Two "Whoa!" Scientific Probes & Data Generation for Publication-Grade Figures (`experiments/phase3_anatomy_and_rhombus.py`)

Before we render the final visual gallery, run TWO jaw-dropping mathematical & physical probes that we haven't seen yet:

1. **Anatomy of the Equilateral Triangle's Unique Invisible $L^2$ Flux $g_\triangle$ (and Its Two $L^1 \setminus L^2$ Siblings!)**:
   - Compute $g_\triangle(s)$ accurately along the boundary of the unit equilateral triangle (both via the exact Cauchy-Laplace / Schwarz-Christoffel Hilbert formula (5)–(6) AND independently via high-resolution least-norm projection from `B(nu) = 0, mass = 1` so the two completely independent methods agree!).
   - Answer these concrete questions with hard numbers:
     - **Is $g_\triangle$ mirror-symmetric along each edge, OR IS IT CHIRAL (asymmetric along each edge because the one-sided lattice $\Lambda_+$ has counterclockwise orientation)?!**
     - **Does $g_\triangle$ stay strictly positive like the square's Saint-Venant torsion flux, OR does it change sign?!**
     - **What is its exact asymptotic behavior as $x \to 0$ (approaching a vertex of the triangle)?** (Check power law $x^\alpha$ numerically and analytically!)
     - Also compute the profile of the **two additional $L^1 \setminus L^2$ invisible fluxes** on the triangle (confirming their exact $|z - v|^{-1/2}$ corner blowup!) and save high-precision boundary arrays to `experiments/data/` (JSON/NPZ) so our figure script can plot them cleanly!

2. **The Two-Slope Rhombus Experiment (Smoking-Gun Proof of the Angle-Dependent Minimax Exponent $N^{-(1 - \omega_k/(2\pi))}$!)**:
   - Take a **$60^\circ / 120^\circ$ unit rhombus** (centrally symmetric even 4-gon with two sharp corners $\omega = \pi/3$ and two blunt corners $\omega = 2\pi/3$).
   - Add $N$ shifted samples ($\theta = 1/2$) on one edge and compute the EXACT finite minimax vertex risks $E_{\text{sharp}}(N)$ (at the $60^\circ$ corner) and $E_{\text{blunt}}(N)$ (at the $120^\circ$ corner) for $N = 2, 4, 6, 8, 12, 16, 20$ (high precision `mpmath` so ill-conditioning never pollutes the Gram matrix!).
   - Verify our Theorem B3 prediction on ONE SINGLE POLYGON:
     - Sharp $60^\circ$ corner scales as **$N^{-(1 - 1/6)} = N^{-5/6}$** ($N^{5/6} E_{\text{sharp}}(N)$ stabilizes!)
     - Blunt $120^\circ$ corner scales as **$N^{-(1 - 1/3)} = N^{-2/3}$** ($N^{2/3} E_{\text{blunt}}(N)$ stabilizes!)
   - Also compute the full curve $E_\infty(N, \theta)$ for $\theta \in (0, 1)$ (dense grid of ~40 points) at $N = 1, 2, 4$ on the unit square, identifying the exact finite-band optimal shift $\theta^*(N)$ (proving visually why $\theta = 1/2$ is NOT optimal!).
   - Also compute the symmetry-breaking curve for the two-sided lattice $\Lambda_\pm$ as a square is tilted by angle $\varepsilon \in [0, 0.2]$ into a non-parallel quadrilateral (watching the 4 invisible modes' smallest singular values jump sharply off 0 the instant $\varepsilon > 0$!).

Save all computed data cleanly into `experiments/phase3_data.npz` (or `.json`) and report EVERY finding, Lean compilation output, and `#print axioms` audit in your final response (saved to `codex_logs/phase3_lean_and_anatomy_output.md`).
