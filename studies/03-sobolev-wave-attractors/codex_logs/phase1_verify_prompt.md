# Hostile Read-Only Derivation-Verification Audit — Study #03 (Phase 1 Proofs & Computations)

You are acting as an **unforgiving, hostile *Annals of Mathematics* / *CPAM* Referee** running in **`read-only` mode** on `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors`.

Your SOLE mission is to **TRY TO BREAK EVERY SINGLE PROOF, FORMULA, SIGN, HYPOTHESIS, EDGE CASE, BOUNDARY CONDITION, AND NUMERICAL CERTIFICATE** in all Phase 1 documents and scripts before we pitch these discoveries to a strict 3-judge panel!

Do NOT be polite. Do NOT rubber-stamp anything. If you find a genuine mathematical flaw, missing hypothesis, wrong sign, invalid limiting step, overlooked degenerate case, false priority/novelty claim, or script bug, flag it with **SEVERE / MAJOR / MINOR** severity and specify the exact location and exact mathematical failure!

## Files to Audit Line-by-Line
Read and stress-test ALL of the following documents and corresponding Python verification scripts:
1. `docs/phase1_scouting.md` (overview & summary tables)
2. `docs/phase1_coexistence.md` & `docs/phase1_central_bounds.md` & `experiments/phase1_coexistence.py`
   - **Attack specifically**:
     - Is the **Uncloakability Theorem** ($\|u\|_{L^\infty(\Gamma)} = \max_{w\in H(\partial\Omega)}|w-c_\Gamma| \ge \frac12 \|u\|_{L^\infty(\Omega)}$) 100% airtight for ALL convex polygons, ALL noncharacteristic rational frequencies, ALL finite-energy $H_0^1(\Omega)$ eigenfunctions, and ALL regular periodic cycles $\Gamma$ of primitive period $q \ge 2$? Check:
       - Can $H(\partial\Omega)$ achieve its maximum/minimum ONLY on a degenerate/vertex orbit, and does the Jordan-curve intersection argument genuinely handle a 2-chord retracing vertex orbit or an orbit passing through a vertex?
       - Does every point of $\Gamma$ lie in $\Omega$ (with boundary impacts) and is $u$ genuinely continuous on $\overline{\Omega}$ so $\|u\|_{L^\infty(\Gamma)}$ is well-defined?
       - Check the sharpness example ($u_h$ with global norm 2, circuit norm 1, Dirichlet energy 256).
     - Check the **sharp side-count bounds**: $k-3$ for general convex $k$-gon attractors (all periods $q$), $k-5$ with a neutral period-2 beam, $h-3$ for centrally symmetric $2h$-gons with a neutral period-2 beam, and **$k \ge m+4$** (ruling out mixed dynamics in ALL quadrilaterals at ALL periods $q$, including characteristic directions!). Try to build a counterexample!
     - Check the **inverse construction** with $m+5$ sides and independently prescribed heights $r_i$ and contraction factors $\kappa_i \in (0,1)$: verify convexity, strict edge-interior contact, exact multipliers, exact eigenspace $u_h(s,t) = h(1-|s|)-h(|t|)$, exact Dirichlet energy $4\int_a^1 |h'|^2\,dy$, and the rank-$\infty$ norm-1 projection discontinuity $\|\Pi_1 - \Pi_\kappa\| = 1$.
     - Check the exact basin fractions $(1/4, 1/2, 1/4)$ and the no-global-exterior-capture proposition.
3. `docs/phase1_measure.md`, `docs/phase1_parity.md`, `docs/phase1_rectangle.md`, `docs/phase1_canonical.md`, and `experiments/phase1_{measure,parity,rectangle,canonical}.py`
   - **Attack specifically**:
     - Check the **fixed-tilt full-measure & Hausdorff-dimension $< 1$ proof**:
       - Check the checkerboard conjugacy $g = T_s J_m$, the Hecke group reduction $y = x$, $L_v = 2\cosh v$, and whether the limit set of the Hecke group REALLY contains ALL exceptional directions (no missed boundary/parabolic/elliptic cases!).
       - Check the **1-Lipschitz log-graph bound** $|\frac{d}{dv}\log|t(v)|| \le 1$ and the **Harnack holomorphic-motion Hölder estimate** — check for ANY flaw when $n_0 = 0$ or when two codes cross or approach $0$, or when taking countably many patches!
       - Check the **exact $9/10$ integer tenth-power certificate** for $\phi \ge 15^\circ$ (verify the formula for $M_{ijk}$, monotonicity in $\ell \ge L = 4/\sqrt{3}$, the integral-test tail $T$, and the chain-rule bound $3S^2T + 3ST^2 + T^3$!).
     - Check the **exact parity law** for all 5 canonical quadrilaterals (upright rectangle, right trapezoid, isosceles trapezoid, sheared parallelogram, tilted rectangle), the universal attracting multiplier $\mu^{-2}$ vs $\Lambda^{-1}$ vs $\Lambda^{-2}$, and the **exact point-spectrum extinction criterion** $\sigma_p(P) = \emptyset \iff \cot(2\phi) \le R \le \tan(2\phi)$ (including critical angles $\theta = \phi, \pi/2-\phi$ and $\lambda = 0, 1$!).
     - Check the **geometric re-entry accumulation law** $\theta_0 - \theta_N \sim \frac{t}{1+Rt}\left(\frac{R-t}{R(1+Rt)}\right)^N$ and the Zhang–Temnov (2026) counterexample!
4. `docs/phase1_pde.md` & `docs/phase1_rigidity.md` & `experiments/phase1_pde.py`
   - **Attack specifically**:
     - Check **Theorem 1–3 of `phase1_pde.md`**: Does weak $u \in H_0^1(\Omega)$ solving $(1-\lambda^2)u_{zz}-\lambda^2 u_{xx}=0$ really force $A,B \in H^1$ up to EVERY endpoint (especially the shell-scaling corner proof and characteristic sides)? Is the converse 100% rigorous?
     - Check **All-Polygon Rigidity (`phase1_rigidity.md`, Theorems 1–3)**:
       - Scrutinize the unfolded travel-time identity (5)–(6), the $O(s^3)$ vs $O(s^2)$ error across breakpoints, the sign of the log-derivative jump at interior corners on BOTH halves of the reflected period (check convexity/concavity after reflection!), and the deduction of $\operatorname{dist}(n\beta_h,\mathbb{Z}) \le C/n$!
       - Check the centrally symmetric period-2 criterion $S_r K \ne K$ (Theorem 3 of `phase1_rigidity.md`), especially the determinant $\det(q', S_s p') = -s'(t)/s(t)$ and the $p=q$ case!
     - Check **Theorem 4b & Corollary 4c (Microscopic Corner-Shaving Lower Bound $\frac{6}{\pi^2}(1 - 1/\sqrt{2}) \approx 17.81\%$)**:
       - Try to break the separation inequality $2/n - 2sD > 2v$, the regular-ray proof (no corner hits), the reflection across $s=1$, the Jacobian $g_\lambda(x) = (1+x)/(1+x^2)^{3/2}$, and the Möbius primitive-lattice limit (especially the $n < \delta N$ truncation error!).
     - Check **Theorems 5–6 (Nonconvex Orthogonal Polyominoes)** — especially odd extension across re-entrant corners in $H^1(X)$! (Does odd reflection of $u \in H_0^1(\Omega)$ across horizontal and vertical walls really belong to $H^1(X)$ near a re-entrant $270^\circ$ corner, and is a point of $X$ removable for $D_+ D_- U = 0$?)
5. `docs/phase1_regular.md`, `docs/phase1_regular_measure.md`, `docs/phase1_multiple.md`, and `experiments/phase1_{regular,multiple}.py`
   - **Attack specifically**:
     - Check the **Regular $N$-gon grid theorem** (especially the sine product, the telescoping product $\prod_{j=1}^{g-1} M_j = [\tan(r d_0)\tan(r d_g)]^2$, and the $N=4m+2$ basin distribution $-N\ell_N \Rightarrow 2\pi/\sin(\pi U)$).
     - Check **Theorem 4 of `phase1_multiple.md`** (odd regular $N$-gon attains $N-3$ attracting 2-cycles at $s=1$) — check EVERY trig inequality and quadrant sign!
     - Check the **quasimode bound** $O(N^{-3/2})$ and its explicit constant `0.000130638` at $N=1002$ (verify integration by parts on $P_N$, the formula for $\|\nabla E_N\|_2^2$, and the factor $1/2$ in $|\langle (T_N - 1/2)w_N, v\rangle| \le \frac12 \|\nabla E_N\|_2 \|\nabla v\|_2$!).
     - Check the **growing-period measure bound** in `phase1_regular_measure.md` (especially constants `6`, `18`, `200`, `1000` and the monotonicity of $F_\theta$!).

## Output Format Required
Structure your hostile audit report clearly:
1. **Verdict Summary Table**: For each of the 4 pillars and every major theorem/claim, mark `AIRTIGHT`, `NEEDS MINOR FIX`, or `BROKEN / GAP FOUND`.
2. **Detailed List of ALL Bugs, Gaps, Sign Errors, Missing Hypotheses, or Subtle Flaws Found** (ordered by severity: SEVERE, MAJOR, MINOR), with exact file paths, line numbers, mathematical counterexample or diagnosis, and exact repair required.
3. **Final Audit Recommendation**: Which theorems are already rock-solid for a Pitch Packet to the 3-judge panel, and which exact items MUST be repaired or tightened first.
