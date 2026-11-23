# Phase 4 Mathematical Accuracy Referee Audit Brief — Project ReMath

You are `gpt-6.2-astra` (`reasoning_effort=max`) acting as an exacting mathematical journal referee for our three newly drafted LaTeX manuscripts in `/Users/mw/Desktop/math/remath`:

1. **Paper 1 (Academic Preprint)**: `papers/paper1_invisible_loads/paper1_invisible_loads.tex`
   (*Invisible Boundary Loads on Convex Polygons: Leont'ev's Exponential Lattice, Balayage Anatomy, and Fokas's Global Relation*)
2. **Paper 2 (Academic Preprint)**: `papers/paper2_corner_recovery/paper2_corner_recovery.tex`
   (*Minimax Recovery of Polygon Corner Charges from Bandlimited Leont'ev Frequencies: Parity, Angle-Dependent Exponents, and Super-Resolution*)
3. **Expository Article (Korean)**: `papers/expository_kr/expository_leontiev_kr.tex`
   (*다각형이 들을 수 없는 파동들: 소련 우파(Ufa)의 잊힌 지수급수 이론에서 발굴한 7가지 수학적 기적*)

## Ground-Truth Verification Assets in This Repo
- Scripts & data: `experiments/phase1_probe.py`, `experiments/phase2_theorems.py`, `experiments/phase3_anatomy_and_rhombus.py`, `experiments/phase3_square_certificate.py`, `experiments/phase3_data.json`, `experiments/data/phase3_triangle.npz`
- Lean 4 proofs: `proofs/lean4/*.lean`
- Previous detailed derivations: `codex_logs/phase1_scouting_output.md`, `codex_logs/phase2_deep_output.md`, `codex_logs/phase3_lean_and_anatomy_output.md`

## Your Audit Instructions (Read-Only Mode — Do NOT Edit Files)
Read ALL THREE `.tex` files line by line and check every theorem, proposition, lemma, proof step, sign, constant, exponent, quantifier, regularity hypothesis, figure caption claim, and numerical value!

Pay special attention to:
1. **Paper 1, Lemma 2.2**: Signs of $\tau$, $\Log(-c_j u)$ branch jumps across $\mathcal{R}_j$, exposed-vertex transitions $\gamma_{j+1} \to \gamma_j$, and alternating vertex constants $C_{\gamma_{j+1}} = -C_{\gamma_j}$.
2. **Paper 1, Theorem 3.1 & Theorem 3.2**: Signs/orientations in the continuous-to-discrete Fokas-to-Leont'ev residue transfer ($s = i\lambda$, $R_j(s)$), the Lambert continuation formula, the zero-density erasure proof, and the 4th-derivative argument in Theorem 3.2(3) showing $\inf\|c\|_1 = 1$ is unattained for $F \equiv 1$ on $[-\frac12,\frac12]^2$.
3. **Paper 1, Theorem 4.1 & Theorem 4.2**: Exact hypotheses and proof of the universal dimension table, the directional Laplace transform $C_F(z)$, Muckenhoupt $A_q$ weight exponents for the Riemann-map Hilbert realification, and the two-sided symmetry collapse.
4. **Paper 1, Theorem 5.1 & Theorem 5.2**:
   - Check carefully our newly sharpened **Parallelogram Criterion** in Theorem 5.1(2) (that uniform Saint-Venant torsion $-\partial_n u$ for $-\Delta u = 1$ lies in $\mathcal{K}_{L^2}(\Lambda_+)$ **if and only if** $D$ is a parallelogram $p=4$, whereas on $2k$-zonotopes with $k \ge 3$ it is the box-spline torsion $-\partial_n u_{\mathrm{box}}$ that generates $L(s)$)! Verify every step of that proof (including $w_{j+1} = -w_j \implies \zeta_{j+1} = \zeta_{j-1} \implies 2k \le 4$)!
   - Check Theorem 5.2 (the equilateral triangle Y-skeleton formula (16)–(17), exact signs/factors in the Binet $\zeta(6m+4)$ generating function, spoke vector $u_j$ vs. $r$ parameterization — WAIT: check carefully whether in `phase3_anatomy_and_rhombus.py` the radial coordinate along the median spoke was `z + u * y^2` vs `z + u * r`!! Verify the exact variable $r$ vs $y^2$ in (17) and in the conformal $w^3$ Poisson integral derivation of $\sqrt{2/\pi}\,x^{1/2}$!).
5. **Paper 1, Theorem 6.1**: Signs in $2\sum \rho_j(is) = B_{q_t}(s) + i B_{q_n}(s) = 0 \implies B_{q_n}(s) = i B_{q_t}(s)$! Check whether $B_{q_t} + i B_{q_n} = 0$ gives $B_{q_n} = +i B_{q_t}$ or $-i B_{q_t}$! (`i * (+i B_{q_t}) = -B_{q_t}`, so `B_{q_t} + i(i B_{q_t}) = 0` — check if `B_{q_n} = +i B_{q_t}` is right or if there is a minus sign anywhere!).
6. **Paper 2, All Sections (2–7)**:
   - Check every sign, index shift ($m-1+\theta$ vs. $m+\theta$!), calibration remark, Gram matrix positivity proof, tangent-ray operator $T$ and $C_k = \|\Pi T^* c^{(k)}\|_X$, cardinal interpolant $D_\nu(s)$, Varga Christoffel upper/lower polynomial comparisons in Theorem 5.1, single-shift regimes in Proposition 5.3, interval-certified numbers in Theorem 5.4, super-resolution weights & Chebyshev bound in Theorem 6.1, and Green's identity signs in Theorem 7.1 ($B_{\mathrm{fp}\,q_n}(s) = +i\sum a_j e^{s\gamma_j}$ vs. $-i$, check against `phase2_theorems.py`!).
7. **Expository Korean Article**: Check that no mathematical statement or number in `expository_leontiev_kr.tex` contradicts Paper 1 or Paper 2.

## Required Output Format
Categorize EVERY finding strictly into three buckets:
1. **`[CRITICAL / LOGICAL OR MATHEMATICAL ERROR]`** — Anything mathematically false, missing a required hypothesis without which a statement is false, having a wrong sign/factor/index/variable power, or mismatching our verified computational numbers. Provide the exact file, line/equation number, why it is wrong, and the exact mathematical correction.
2. **`[MODERATE / TECHNICAL PRECISION]`** — Genuine mathematical subtleties (e.g., convergence justification, boundary regularity, edge-case quantifier) where tightening 1–2 sentences prevents a referee objection.
3. **`[MINOR / STYLISTIC]`** — Purely stylistic or expositional comments.
