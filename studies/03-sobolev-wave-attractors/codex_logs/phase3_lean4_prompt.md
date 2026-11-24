# Phase 3 Prompt — Standalone Lean 4.36.0 Formalization for Study #03 (`03-sobolev-wave-attractors`)

You are formalizing the core algebraic, combinatorial, dynamical, and spectral theorems of **Study #03 (`03-sobolev-wave-attractors`)** as a **100% standalone Lean 4.36.0 project** inside `proofs/lean4/` (zero external Mathlib dependencies — pure Lean 4 core / `Std`, matching Study #01's exact architecture!).

## Project Layout & Build Contract
Create inside `proofs/lean4/`:
- `lean-toolchain`: `leanprover/lean4:v4.36.0`
- `lakefile.toml`:
  ```toml
  name = "sobolev_attractors"
  version = "0.1.0"
  defaultTargets = ["SobolevAttractors"]

  [[lean_lib]]
  name = "SobolevAttractors"
  roots = ["Uncloakability", "MultiplicityBounds", "TiltedParity", "CornerShavingAndTriangles", "Main"]
  ```
- **MANDATORY ZERO-DEFECT BUILD GATE**:
  Run from `proofs/lean4/`:
  ```bash
  lake clean && lake build && lake env lean Main.lean
  ```
  MUST exit with code 0, **0 errors, 0 warnings, 0 `sorry`, 0 `axiom` declarations**, and `#print axioms` in `Main.lean` MUST show ONLY standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound`, or empty list `[]` for pure constructive proofs)!

## Four Thematic Modules to Formalize (Aim for 30–40 Non-Trivial Verified Theorems!)

Use `Rat` (Lean 4 core `Rat`, or exact integer/rational arithmetic) and clean structural definitions — NO trivial `1 + 1 = 2` filler theorems; every theorem must formalize a genuine mathematical pillar from `docs/phase1_*.md`:

### 1. `Uncloakability.lean` — Sharp Half-Amplitude Uncloakability & Coexistence Hexagon
Formalize:
- **Exact Sharp Half-Amplitude Theorem**: For any rational bounds $m \le M$ and any $c \in [m, M]$ (representing $c_\Gamma \in [\min H, \max H]$), prove $\max(|M - c|, |m - c|) \ge \frac{1}{2}(M - m)$, AND prove equality holds **if and only if** $c = \frac{1}{2}(m + M)$, AND for any finite nonempty list of boundary values `vals : List Rat`, $\max_{w \in \mathrm{vals}} |w - c_\Gamma| \ge \frac{1}{2}(\max \mathrm{vals} - \min \mathrm{vals})$!
- **Dihedral Invariance & Zero-Trace Algebra**: For any domain boundary with involutions `gPlus gMinus : α → α` ($g_+^2 = \mathrm{id}$, $g_-^2 = \mathrm{id}$) and $b = g_+ \circ g_-$, prove:
  - Time-reversal conjugacy $g_- \circ b \circ g_- = b^{-1}$ and $g_+ \circ b \circ g_+ = b^{-1}$ (and for iterates $g_- \circ b^q = b^{-q} \circ g_-$).
  - If $u = A \circ \xi - B \circ \eta$ vanishes on $\partial\Omega$ ($A(\xi(p)) = B(\eta(p))$ for all $p \in \partial\Omega$), then the common boundary profile $H(p) := A(\xi(p))$ satisfies $H(g_+(p)) = H(p)$, $H(g_-(p)) = H(p)$, and $H(b(p)) = H(p)$!
- **Exact Coexistence Hexagon (`a = 3/4, r = 1/4, κ = 1/2`)**:
  - Define the exact right-wall function $R(t) = \min(1 - |t|, \frac{2}{3} + \frac{t}{3}, \frac{3}{4} - \frac{2t}{3})$ and left wall $L(t) = |t| - 1$ on $[-1, 1]$.
  - Prove $R(t) = 1 - |t|$ for $3/4 \le |t| \le 1$, and $R(t) \ge 1/4$ for $|t| \le 3/4$ (verifying that $u_h(s,t) = h(1-|s|) - h(|t|)$ vanishes identically on all 6 walls whenever $h(y) = 0$ on $[0, 3/4]$!).
  - Prove the exact return map near $y = 1/4$ satisfies $y' = \frac{1}{8} + \frac{1}{2}y$, with unique fixed point $y = 1/4$, exact contraction $y' - \frac{1}{4} = \frac{1}{2}(y - \frac{1}{4})$, and exact sharpness profile ($h$ taking $0, 1, 0, -1, 0$ at $3/4, 13/16, 7/8, 15/16, 1$) attaining global $|u| = 2$ at $(1/16, 13/16)$ and circuit $|u| = 1$ along $t = 1/4$ (plus exact basin weights $1/4 + 1/2 + 1/4 = 1$)!

### 2. `MultiplicityBounds.lean` — Sharp Cycle & Coexistence Counting ($k-3$, $k-5$, $h-3$, $k \ge m+4$)
Formalize:
- **Exact Cyclic Gap-Orbit Involution Lemma**: On `ZMod` / `Fin (2 * m)` ($m \ge 1$), if an orientation-reversing involution `σ(i) = (h - i) mod (2m)` has NO fixed points, prove `h` is **odd**; and the induced gap involution `τ(i) = (h - i - 1) mod (2m)` has **EXACTLY TWO** fixed points (namely `(h-1)/2` and `(h-1)/2 + m` mod `2m`) and partitions the remaining $2m - 2$ gap labels into $m - 1$ disjoint 2-cycles!
- **Corollary — Universal $k - 3$ Attractor Bound (`m ≤ k - 3`)**: From 4 extremal vertices (lying in the 2 fixed gap classes) plus $\ge 1$ distinct extra vertex in each of the $m - 1$ conjugate gap pairs, prove $k \ge 4 + (m - 1) = m + 3$, i.e. $m \le k - 3$!
- **Corollary — Universal Mixed-Dynamics Bound (`k ≥ m + 4`) & No Mixed Quadrilaterals**: Adding a generic neutral orbit and its distinct reversal gives $2(m+1)$ cyclic labels with $2$ fixed gap classes and $m$ non-invariant gap pairs each requiring a distinct non-extremal vertex, proving $k \ge 4 + m$; in particular, for **$k = 4$ (any convex quadrilateral)**, **$m = 0$** (mixed neutral + regular attracting dynamics is impossible at ANY period!).
- **Period-2 Four-Chain & Central-Symmetry Sharp Bounds (`m ≤ k - 5`, `m ≤ h - 3`)**:
  - Formalize the piecewise-affine root-counting lemma: if a continuous piecewise-affine function on an interval has $P \le k - 3$ pieces and vanishes identically on at least one piece, then at most $\max(0, P - 2) \le \max(0, k - 5)$ pieces can carry an isolated interior sign-changing zero — proving **$k = 6$ is minimal** for general period-2 coexistence!
  - Formalize the centrally symmetric upper-envelope lemma: $h$ strip pairs with one repeated neutral pair yield at most $h - 1$ distinct envelope pieces and at most $\max(0, h - 3)$ isolated transitions — proving **$2h = 8$ is minimal** under central symmetry!
- **Exact Prescribed-Rate Algebraic Recurrence (`G_i = G_{i-1} / κ_i`)**: Formalize that the slope-jump construction for $0 < r_1 < \cdots < r_m < a < 1$ and $0 < \kappa_i < 1$ produces strictly monotone crossing points $r_{i-1} < p_i < r_i$, concave right wall, and exact attracting multiplier $\kappa_i = G_{i-1} / G_i$ at every $r_i$!

### 3. `TiltedParity.lean` — Boundary-vs-Section Parity Flip, Canonical 4-Way Table & Extinction Threshold
Formalize:
- **Exact Coprime Winding Parity Theorem**: For coprime positive integers $m, n$ (`Nat.Coprime m n`), write $q = m + n$ and consider the reduced fraction $(m + n)/(2m) = P/D$:
  - Prove: $q$ is **even** $\iff$ both $m, n$ are odd $\iff$ $\gcd(m+n, 2m) = 2$ $\iff$ section denominator $D = m$ is **odd**!
  - Prove: $q$ is **odd** $\iff$ $m, n$ have opposite parity $\iff$ $\gcd(m+n, 2m) = 1$ $\iff$ section denominator $D = 2m$ is **even**!
- **Unified Canonical 4-Way Parity Classification**: For coprime positive $M, N$ (wall-section winding $N/M$, boundary label $p/q = N/(M+N)$):
  - Right trapezoid: section period $M = q - p$ is even $\iff q - p$ even (global identity), odd $\iff$ attracting multiplier $\Lambda^{-1}$.
  - Isosceles trapezoid: half-map rotation $N/(2M)$ has even reduced denominator $\iff N = p$ is odd (global identity), odd $\iff p$ is even (attracting multiplier $\Lambda^{-2}$).
  - Sheared parallelogram & Tilted rectangle: half-map rotation $(M+N)/(2M)$ has even reduced denominator $\iff q = M+N$ is odd (global identity), odd $\iff q$ is even (attracting multiplier $\Lambda^{-2}$ / $\mu^{-2}$).
- **Exact Universal Multiplier & Parity Interlacing**: For a $D$-step product $\mu^{N_A - N_B}$ with $N_A + N_B = D$ and $|N_A - N_B| \le 1$, prove:
  - $D$ even $\implies N_A = N_B \implies N_A - N_B = 0$ (neutral, multiplier $1$).
  - $D$ odd $\implies |N_A - N_B| = 1$ (hyperbolic, multiplier $\mu^{\pm 1}$, squared to $\mu^{\pm 2}$ on the physical double cover!).
- **Exact Extinction Biconditional & Zhang–Temnov Counterexample**:
  - For $t = \tan(2\phi) > 0$ and $R > 0$: prove $1/t \le R \le t \iff R \le t \land 1/R \le t$ (and requires $t \ge 1$, i.e. $\phi \ge \pi/8$ for $R = 1$!).
  - Verify the exact rational tilted-square Zhang–Temnov counterexample: $a = 1/2, b_1 = 2 \implies \mu = 4, \mu^{-2} = 1/16$, and exact boundary map fixed points $1/3, 7/3$ with multiplier $1/16$!

### 4. `CornerShavingAndTriangles.lean` — Triangle Pigeonhole Annihilation, Corner-Shaving Plateaus & Regular $N$-Gon Identities
Formalize:
- **Triangle Common-Extremum Pigeonhole Theorem**: For ANY two functions $\xi, \eta : \mathrm{Fin}\,3 \to \mathbb{Q}$ (each attaining a min and max on $\mathrm{Fin}\,3$), prove there exists a vertex $v \in \mathrm{Fin}\,3$ that is simultaneously extremal ($\min$ or $\max$) for BOTH $\xi$ and $\eta$!
- **Monotone Contraction Kernel Annihilation**: If $T : \mathbb{Q} \to \mathbb{Q}$ satisfies $0 \le T(x) \le k x$ for $0 < k < 1$ and $A(T(x)) = A(x)$, prove $A(x) = A(T^n(x))$ for all $n \in \mathbb{N}$ (and for discrete geometric shells $B(ky) = B(y)$, every shell has equal weighted energy!).
- **Exact Microscopic Corner-Shaving Separation Theorem (Theorem 4b)**:
  - For coprime $1 \le m < n$, rational bevel $0 < u \le v < 1$ with $\tau = v/u \ge 1$, $s_* = m/(n - u) < \tau$, and $v + s_* u < 1/n$:
  - Prove that for EVERY $s \in [m/n, s_*]$, $D := n - m/s$ satisfies $0 \le D \le u$, and for EVERY $1 \le k < n$ and $0 \le D_k \le D$, the circular displacement error satisfies $|2s(kD/n - D_k)| \le 2sD$, so the separation from any distinct orbit point is $\ge 2/n - 2sD > 2v$ (strictly exceeding the bevel support width $2v$, forcing at most ONE bevel visit per $n$-cycle!).
  - Prove the exact $\varepsilon$-independent multiplier formula: when $\tau = 1$ ($u = v = \varepsilon$), for $0 < s < 1$, $(\tau - s)/(\tau + s) = (1 - s)/(1 + s) \in (0, 1)$, and at $s = 1/(2 - \varepsilon/2)$ (period-3 midpoint), the multiplier equals $(2 - \varepsilon)/(6 - \varepsilon)$!
  - Prove the exact algebraic integrand identity $\frac{x}{1+x} \cdot \frac{1+x}{(1+x^2)} = \frac{x}{1+x^2}$ (and the exact $(1+x)$ cancellation in Corollary 4c's frequency density!).
- **Regular $N$-Gon Corner-Fraction Arithmetic mod 4**: Formalize the exact arithmetic mod 4 of the regular $N$-gon corner angular fractions ($3/N$ for odd $N$, $2/N$ for $N \equiv 2 \pmod 4$, and exact $m_{\min}$ rational/algebraic monotonicity $\frac{2c - 1}{2c + 1} < \frac{1}{3}$ for $0 < c < 1$)!

### 5. `Main.lean`
Import all 4 modules and run `#print axioms` on EVERY SINGLE main theorem across all 4 modules so that `lake clean && lake build && lake env lean Main.lean` audits every theorem cleanly with zero warnings, zero `sorry`, and ONLY standard Lean axioms!

## Execution & Report
Build and test from scratch (`cd proofs/lean4 && lake clean && lake build && lake env lean Main.lean`). Return a clean theorem inventory (exact module, theorem name, mathematical statement, and `#print axioms` output).
