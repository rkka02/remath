# Phase 4 Read-Only Mathematical Referee Audit — Round 1 (`Study #03: 03-sobolev-wave-attractors`)

You are the **strict, adversarial read-only mathematical referee** (`gpt-6.2-astra`, `reasoning_effort=max`) for **Project ReMath Study #03 (`studies/03-sobolev-wave-attractors/`)**. You have read-only access: **do not modify any files**; instead try your hardest to **BREAK** every proof, formula, sign, hypothesis, constant, numerical table, figure-generation formula, historical attribution, Lean 4 cross-reference, and Python verification script across the complete Phase 4 package.

## Exact Scope to Audit Line-by-Line

1. **Paper 1 (English `amsart` preprint, 18 pp.)**:
   - `studies/03-sobolev-wave-attractors/papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.tex`
   - Audit EVERY theorem, proposition, remark, proof step, sign, factor, quantifier, edge case, table entry (Table 1 & Table 2), citation, and Lean 4 theorem identifier.
   - Check specifically:
     - Operator conventions ($T = \Delta_D^{-1}\partial_z^2$ on $H_0^1$, $P = \partial_z^2\Delta_D^{-1}$ on $H^{-1}$, $P\Delta_D = \Delta_D T$, $s = \tan\theta = \sqrt{1-\lambda^2}/\lambda$, $\lambda = \cos\theta$, $b_\lambda = \gamma_\lambda^+\gamma_\lambda^-$).
     - Theorem 2.1 (3 endpoint cases, geometric-shell energy scaling), Theorem 2.2 (periodic intervals avoiding dihedral translates of characteristic sides $E$), Theorem 2.3 (common-extremum annihilation for triangles & diamonds), Theorem 2.4 (nonconvex orthogonal polyominoes, Masur + Veech, L-triomino trace incompleteness).
     - Theorem 3.1 (Universal Half-Amplitude Uncloakability, Jordan-curve interlacing proof, exact midrange equality, Remark sharpness: energy $256$, $|u_h(1/16, 13/16)| = 2$, single-leg energy recovery $\sqrt{2}\int_J |\partial_{\mathrm{arc}} u_h|^2$).
     - Theorems 4.1 & 4.2 (universal $m \le k-3$, characteristic-edge separate attractor/repeller bound & hexagon counterexample, universal mixed $k \ge m+4$ & no mixed convex quadrilaterals, period-two $m \le k-5$ and central $m \le h-3$), Proposition 4.4 (odd regular $N$-gon $N-3$ formula, symmetry pairing, Table 1 numbers).
     - Theorems 5.1 & 5.3 (minimal hexagon, pivoting-wall $D_\kappa(y)$, exact Dirichlet energy $4\int_a^1 |h'|^2$, basins $(1/4,1/2,1/4)$, norm-1 infinite-rank jump $\|\Pi_1 - \Pi_\kappa\| = 1$, Reversibility Proposition, prescribed-rate right-wall formula $R(\eta) = 1 + \eta - \frac{1}{M}\sum |\Delta_i|(\eta-\eta_i)_+$ — check signs and boundary values $R(\pm 1) = 0$!).
     - Every Lean 4 declaration name in Table 2 against actual declarations in `proofs/lean4/`.

2. **Paper 2 (English `amsart` preprint, 17 pp.)**:
   - `studies/03-sobolev-wave-attractors/papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex`
   - Audit EVERY theorem, proposition, remark, proof step, sign, factor, quantifier, table entry (Table 1 & Table 2), citation, open-problem statement, and Lean 4 cross-reference.
   - Check specifically:
     - Theorem 2.1 & Table 1 (checkerboard reduction, unified 5-tank boundary parity in clockwise $p/q$, exact multipliers $\Lambda^{-1}, \Lambda^{-2}, \Lambda^{-2}, \mu^{-2}$, $15^\circ$ five-tank values $1, 1/\sqrt{3}, 1, 1/3, 1/9$).
     - Theorem 2.2 (finite floor-and-product formula $C_{s_0}(P,D)$, CCW vs. CW orientation consistency, exact rotation range $[1/(2\lceil R\cot 2\phi\rceil),\, 1 - 1/(2\lceil\cot(2\phi)/R\rceil)]$ — CHECK WHETHER $R$ AND $1/R$ ARE IN THE RIGHT ENDPOINTS FOR CLOCKWISE VS. COUNTERCLOCKWISE!).
     - Theorem 2.3 (fixed-slice full measure $\cos\phi-\sin\phi$, $\pi/2-2\phi$, $\cos(2\phi)$, $1-\sin\alpha$, Hecke coding, holomorphic motion & Harnack bounds, moving-gap transversality $\partial_\theta F \ge \min(a'/r, r b_1') > 0$, local dimension identity, exact $9/10$ integer certificate formula $M_{ijk}$).
     - Theorem 2.4 & Remark 2.5 (extinction horn $\cot(2\phi) \le R \le \tan(2\phi)$, geometric re-entry formula $\theta_0 - \theta_N$, small-tilt tongue scaling $2\phi/(mn)$ and $|E_1|_\theta = 2\phi\log(1/\phi) + O_R(\phi)$, Zhang–Temnov counterexamples at $\tan\phi=1/3, 1/2$ and irrational $a=\sqrt{2}-1, b_1=2-\sqrt{2}$).
     - Theorem 3.1, Remark 3.2, Proposition 3.3 (all-polygon rigidity, shallow travel-time $\dist(n\beta_h, \Z) \le C/n$, chamfered octagon $\beta_{1/2} = \log 2/(1+2\log 2)$, period-3 tongue $(1/2, 2/3)$ and multipliers, central $S_r K \ne K$ criterion).
     - Theorem 3.4 (microscopic corner shaving: axis-aligned cut + tilted-diamond counterexample, Theorem 4b exact plateaus $[m/n, m/(n-u)]$ and multiplier $(\tau-s)/(\tau+s)$, Corollary 4c integral calculation $\frac{6}{\pi^2}(1-1/\sqrt{2})$ and angular integral — CHECK THE FACTOR OF $2$ AND $\frac{1}{2}$ IN THE ANGULAR INTEGRAL LINE!).
     - Theorems 4.1, 4.2, 4.3, 4.5 & Proposition 4.4 (mod-4 corner fractions, shadowing $|\rho_{\mathrm{CW}}-2\theta/\pi|\le 2/N$, resonance grid & telescoping product, aligned $8\mid N$ survival caveat vs. $1-x^2-z^2$, aligned $N=4m+2$ half-frequency paradox & $O(N^{-3/2})$ quasimode bound $D_N$, octagon cliff $-2\log(1+\sqrt{2})$, growing-$Q$ bound).
     - Every Lean 4 declaration name in Table 2 against actual declarations in `proofs/lean4/`.

3. **Korean Expository Feature (Korean `xeCJK`, 7 pp.)**:
   - `studies/03-sobolev-wave-attractors/papers/expository_kr/expository_sobolev_attractors_kr.tex`
   - Audit EVERY mathematical statement, numerical figure ($0.001^\circ \to 99.998\%$, $22.5^\circ$, $9/10$, $1/16$, $17.80577\%$, $39{,}797$, $0.00019\%$, $1/3$, $50\%$, $1/2$, $25\%/50\%/25\%$, $1000$ vs. $1002$, $500$ attractors, $0.333331$, $0.013\% / 0.000131$, $0.00001^\circ \to -1.7627 / 5.83\times$, $40/125$ Lean theorems), and historical fact for strict mathematical truthfulness. (Keep genuine factual/mathematical errors clearly separated from optional prose suggestions.)

4. **Python Code & Figure Generator Audit (including the 4 post-signoff patches)**:
   - `studies/03-sobolev-wave-attractors/experiments/generate_paper_figures.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_probe.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_regular.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_multiple.py`
   - `studies/03-sobolev-wave-attractors/experiments/phase1_pde.py`
   - `studies/03-sobolev-wave-attractors/experiments/test_phase1_repairs.py`
   - Verify all 4 recently patched edge cases (`float`/`np.floating` rejection, `np.int64` `Fraction(int(...))` normalization, `strip_coordinate` `extradps`, pentagon preview edge-contact cap) AND check `generate_paper_figures.py` for any plotting or formula bug (e.g., plotted curves, formulas, legend labels, axis coordinates, exact values).

5. **Lean 4 Consistency Check**:
   - `studies/03-sobolev-wave-attractors/proofs/lean4/{Uncloakability,MultiplicityBounds,TiltedParity,CornerShavingAndTriangles,Main}.lean`
   - Confirm zero `sorry`, zero custom axioms, and exact match with every Lean theorem name and description cited in Papers 1, 2, and the Korean Feature.

## Required Report Format

Structure your report cleanly into two strictly separated sections:
1. **BLOCKING / GENUINE MATHEMATICAL, LOGICAL, NUMERICAL, CITATION, OR CODE DEFECTS** (numbered `B1, B2, ...`, giving exact file, line number, exact quote, why it is mathematically/logically/factually wrong or incomplete, and the exact fix). If there are ZERO genuine defects, state explicitly: `ZERO BLOCKING DEFECTS`.
2. **NON-BLOCKING EDITORIAL / CLARITY NOTES** (numbered `N1, N2, ...`, optional improvements that are NOT mathematical errors).

Be merciless on genuine math/logic/sign/formula/code errors. Do NOT gloss over anything!
