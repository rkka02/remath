# Study #02 — Phase 3: Standalone Lean 4.36.0 Formalization

You are the mathematical formalization specialist (`gpt-6.2-astra`, max reasoning) building the standalone **Lean 4.36.0** proof suite for **Project ReMath Study #02 (`02-tsetlin-collective-automata`)** inside:
`/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/`

## Strict Isolation & Toolchain Rules
1. ONLY create/edit files inside `/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/`. Do NOT modify any other directory.
2. Match Study #01's standalone zero-bloat Lean 4.36.0 setup (NO Mathlib dependency):
   - Inspect `/Users/mw/Desktop/math/remath/studies/01-leontiev-invisible-loads/proofs/lean4/lean-toolchain`, `lakefile.toml`, `PolygonParity.lean`, and `Main.lean` as a reference for Lean 4.36.0 syntax (`import Init`, `open Lean.Grind`, `[Field F]`, ordered-field typeclasses, `Rat`, etc.).
   - Use `/Users/mw/.elan/bin/lake` and `/Users/mw/.elan/bin/lean` (Lean 4.36.0).
   - `lean-toolchain`: `leanprover/lean4:v4.36.0`
   - `lakefile.toml`: package `remath_tsetlin`, `defaultTargets = ["ReMathTsetlin"]`, library `ReMathTsetlin` with roots listing all 5 modules + `Main`.
3. **ZERO `sorry`, ZERO custom axioms, ZERO compiler warnings, ZERO errors**. Every single public theorem MUST be audited in `Main.lean` via `#print axioms ...` and depend ONLY on standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound` — or fewer).

## Mandatory Grounding (Read Verified Proof Notes First)
Before writing any Lean definitions, read the exact formulas in:
- `studies/02-tsetlin-collective-automata/docs/phase1_architectures.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_weak_rewards.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_optimal_correlation.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_interface.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_memory.md`
- `studies/02-tsetlin-collective-automata/docs/phase2b_escape_showcase.md`
- `studies/02-tsetlin-collective-automata/docs/phase2b_fair_game_link.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_reversal.md`
- `studies/02-tsetlin-collective-automata/docs/phase2b_staghunt_robustness.md`
- `studies/02-tsetlin-collective-automata/docs/phase1_pooling.md`
- `studies/02-tsetlin-collective-automata/docs/phase2b_quorum_memory.md`

Every formalized formula MUST match the exact definitions and hypotheses in these verified proof notes.

## Required 5 Modules + `Main.lean` (Substantive Theorems Only)

1. **`ArchitectureHierarchy.lean`** (Pillar 1 — Multi-Architecture Hierarchy, Krylov Thinning, Volkonskii 1965 Errata, Weak-Reward Reversal):
   - Over an arbitrary ordered field (or `Rat` where rational witnesses are proved, and general ordered field for the algebraic theorems):
   - Define `F_L`, `F_D`, `F_K` and Krylov's private-coin map `(p, κ) ↦ ((1+p)/2, κ*p/(1+p))`.
   - Prove the **exact positive factorizations**:
     - `F_D p κ - F_L p κ = 2 * (1 - κ) * p * (1 - p)^2 * (1 - (1 - κ) * p) / (1 - 2 * (1 - κ) * p * (1 - p))`
     - `F_K p κ - F_D p κ = p * (1 - p) * (1 - (1 - κ) * p) * (1 - (1 - κ) * (1 - p)) / (1 + p - (1 - κ) * p * (1 - p))`
   - Prove the **strict hierarchy** `F_L p κ < F_D p κ` and `F_D p κ < F_K p κ` for all `0 < p < 1` and `0 ≤ κ < 1`, AND the boundary collapse at `κ = 1`: `F_L p 1 = p`, `F_D p 1 = p`, `p < F_K p 1 = 2*p/(1+p)`.
   - Prove Krylov's reduction identity linking `F_K p κ` directly to `F_L` evaluated at Krylov's effective parameters `((1+p)/2, κ*p/(1+p))` (check exact algebraic relation in `docs/phase1_architectures.md`!).
   - Prove exact rational witnesses:
     - Benchmark `(4/5, 7/10, 9/10, 1/5)`: `F_L (7/10) (13/63) = 4/5`, `F_D (7/10) (11/21) = 4/5`, and `4/5 < F_K (7/10) 1`.
     - **Volkonskii (1965, p. 47) refutation** on `(17/20, 13/20, 9/10, 3/5)` at `κ = 0`: `F_L (13/20) 0 = 169/218 < 17/20 < 351/400 = F_D (13/20) 0`, and the linear log-odds ratio `((17/20)/(3/20)) / ((169/218)/(49/218)) = 833/507 > 1`.
     - **Weak-reward reversal** witness `(9/20, 1/5, 19/20, 1/10)` at `κ = 0`: `T + S = 21/20 > 1`, `u = (1 - 2*P)/(2*(1 - P - S)) = 3/7`, and `F_D (1/5) 0 < F_K (1/5) 0 < 9/20`.

2. **`EscapeGeometry.lean`** (Pillar 2 — Optimal Imperfect Correlation `κ*(γ)`, Interface Splitting `Φ_u`, `(240,80)` Flip Interval & `N`-Player Public Good Cutoff):
   - Formalize the tilted joint DD step law `(a, b, b, d)` at the exact natural tilt `e^s = p/q` (from `docs/phase1_optimal_correlation.md`) and prove the **unique optimal correlation theorem**: for `1/2 < p < 1` and `γ > 1`, the tilted drift alignment condition holds **if and only if** `κ = (1 + 1/γ)/2` (completely independent of `p`!), and prove strict positivity of the curvature `C_γ = 2*γ*(2*p-1) / ((1 - 1/γ)*(1 + (2*p-1)^2/γ)) > 0`.
   - Formalize the interface-splitting Möbius operator `Φ_u(z) = (1 - u) + u^2 * z / (1 - (1 - u)*z)` (from `docs/phase1_interface.md`): prove `Φ_1(z) = z`, prove `z < Φ_u(z) < 1` for all `0 < u < 1` and `0 < z < 1`, and prove strict monotonicity in `u` (`u1 < u2 → Φ_u2(z) < Φ_u1(z)` — showing why hesitant `B` at `u=1/2` strictly relaxes the constraint compared to `L` at `u=1`).
   - Prove the exact rational `(240,80)` DD–CC–DD flip interval for `(P, T, S) = (3/5, 9/10, 1/5)`, `γ = 3` (from `docs/phase2b_escape_showcase.md`): exact threshold odds giving `27/35 < 4/5 < 81/97`, and the exact rational barrier witness `6 > (3/2)^4` (proving `log 6 > 4 h_P`).
   - Prove the exact `N`-player public-good memory-asymmetry balance identity `d_* = h * (N - 2) / (N - 1)` (from `docs/phase1_memory.md`) and verify the exact rational `(40,40)` vs `(41,40)` or small-depth rational witness if algebraic.

3. **`FairGameCancellation.lean`** (Pillar 3 — Exact Fair-DD Green's-Function Identities & 3-Way Revisit Cancellation):
   - Formalize the exact finite-game harmonic / Green's-function identities from `docs/phase2b_fair_game_link.md`: given `G_oo > 0`, `G_oc > 0`, `G_cc > 0`, and doorway switch parameter `a > 0`, define `b := a^2 * G_oc`, `d := b / G_oo`, `h := G_oc / (G_oo * G_cc)`, `V := G_cc`, `j_imm := h * a^2`, and prove:
     - `d = h * a^2 * V` (revisit factorization),
     - `j_imm / h = a^2` and `d / j_imm = V`,
     - **3-Way Exact Cancellation Theorem**: comparing `L` (`a_L = 1/2`) and `B` (`a_B = 1/4`) under the exact asymptotic/harmonic relation `G_oc^B = 4 * G_oc^L` and `G_oo^B = G_oo^L` (or general `ρ = G_oo^L / G_oo^B`), prove:
       - `b_B / b_L = 1` identically,
       - `d_B / d_L = 1` when `G_oo^B = G_oo^L`,
       - `h_B / h_L = 4 * (G_cc^L / G_cc^B)` (so `4 D_0 / D_{1/4}`), while `j_imm^B / j_imm^L = (1/4) * (h_B / h_L) = G_cc^L / G_cc^B`!
   - Formalize the **exact finite `M = N = 1` interacting fair-DD game** directly from the transition matrix for both `L` and `B` (as in `docs/phase2b_fair_game_link.md` & `phase2b_fair_game_link.json`): verify the exact rational stationary/Green values `G_oo, G_oc, G_cc, h, j_imm, d, b` and prove `d_B = d_L` and `b_B = b_L` directly for `M = N = 1`!

4. **`StagHuntMirage.lean`** (Pillar 4 — Reference Flux, Infinite-Ladder Cancellation, Critical Curve & Exact Depth-1 Open-Region Upper Certificates):
   - Define the geometric sum `G n s = ∑_{j=0}^{n-1} (s/(1-s))^j` recursively and prove:
     - At `s = 1/2`: `G n (1/2) = n`,
     - Closed form for `s ≠ 1/2`: `(2*s - 1) * G n s = (1 - s) * ((s/(1-s))^n - 1)`,
     - Strict monotonicity of `G n s` in `n` (for `0 < s < 1`).
   - Formalize the exact critical curve `R_c P S = P^2 / (P^2 + (1-P)^2 * max(1, S/(1-S)))` and prove the equivalence `λ(R,P) * max(1, S/(1-S)) < 1 ↔ R < R_c P S` (for `0 < S < P < R < 1`).
   - Formalize the **exact infinite-ladder transmission cancellation** from `docs/phase1_reversal.md`: `(1 - ρ_P) * h_C = (1 - ρ_R) * (1 - h_D)` and the exact leading constant identity `K(R,P,S) = (2*P - 1)^2 / ((1 - S) * (2*R - 1))`.
   - Formalize the **exact 4-state depth-1 (`n = 1`) Stag-Hunt Markov stationary distribution** `π_1(R, P, S)` directly, prove it satisfies the exact stationary balance equations `π P = π` and `∑ π = 1`, AND prove the exact rational open-region upper-corner certificates (`π_1 < 3/8`):
     - Corner 1 (`S=1/2, R=16/17, P=4/5`): `π_1(CC) = 3757/10042 < 3/8`,
     - Corner 2 (`S=208/395, R=R_c(4/5, 52/100), P=4/5`): `π_1(CC) = 220211/597796 < 3/8`,
     - Corner 3 (`S=1136/2065, R=R_c(4/5, 5499/10000), P=4/5`): `π_1(CC) = 9854063369/27894660164 < 3/8`!
   - Also check the exact `n=1` formula at `(R=47/50, P=4/5, S=1/2)`.

5. **`CommonFundCutoff.lean`** (Pillar 5 — General Parametric Depth-1 Optimum Below Nash & Exact `n_c = 2` Memory Cutoff):
   - Formalize the general depth-1 (`n = 1`) quorum Common Fund model (`θ ∈ (0, 1/2)`, `0 < c < L < H < 1`, `H - c*θ > L`):
     - Define `A_1 = (c*θ - (1-H)*(1-2*θ)) / (2*c*θ*(1-θ))` and `α_Nash = 1 - (H - L)/c`.
     - Prove exact quota balance at `α = A_1`: the depth-1 stationary volunteering fraction equals `θ` identically, yielding exact social welfare `W = H - c*θ`.
     - Prove strict dominance over both extremes: `H - c*θ > L` (beats pure private `α=0`) and `H - c*θ > H - c/2` (beats full Common Fund `α=1`, where `1/2` volunteer!).
     - Prove the exact algebraic characterization of `A_1 < α_Nash`.
   - Formalize the **all-depth `n ≥ 1` quota-balance ratio** `R_n(α)` from `docs/phase2b_quorum_memory.md` (check exact formula in `docs/phase2b_quorum_memory.md`!) and prove:
     - Exact monotonicity of `R_n(α)` in `n` (for `p_high > 1/2`) and in `α`,
     - On the benchmark `(L=4/5, H=97/100, c=3/5, θ=1/4)`: `α_Nash = 43/60`, `A_1 = 3/5 < 43/60`,
     - **Exact `n_c = 2` cutoff theorem**: at `α = 43/60`, `R_1(43/60) < 3` while for **every `n ≥ 2`** and **every `α ≤ 43/60`** (within the feasible domain), `R_n(α) > 3` (proving NO productive fixed point exists at or below Nash for ANY memory depth `n ≥ 2`!),
     - Exact quadratic equation for `A_2`: `5 * A_2^2 - 22 * A_2 + 19 = 0` (check exact coefficients from `docs/phase2b_quorum_memory.md`!) together with certified rational bracket `814/1000 < A_2 < 815/1000` (and `43/60 < A_2`),
     - Exact rational depth-2 welfare-gap certificate / bound (matching `docs/phase2b_quorum_memory.md`).

6. **`Main.lean`**:
   - Import all 5 modules and run `#print axioms` on EVERY public theorem.

## Mandatory Self-Verification Before Finishing
Run from scratch:
```bash
cd /Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4 && /Users/mw/.elan/bin/lake clean && /Users/mw/.elan/bin/lake build && /Users/mw/.elan/bin/lake env lean Main.lean
```
Confirm:
- Exit code `0`,
- **0 errors, 0 warnings, 0 `sorry`**,
- Every `#print axioms` line lists ONLY subsets of `{propext, Classical.choice, Quot.sound}` (or "does not depend on any axioms").

Report the exact module list, total theorem count, and the full `lake clean && lake build && lake env lean Main.lean` summary in your output.
