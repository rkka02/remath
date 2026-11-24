# Phase 2 Repair Prompt — Fixing 100% of All Defects from `phase1_verify_output.md`

Read `codex_logs/phase1_verify_output.md` carefully. Your job is to repair **100% of EVERY SINGLE SEVERE, MAJOR, and MINOR defect** (mathematical wording, hypotheses, historical attributions, operator conventions, AND every single Python software bug) identified in `codex_logs/phase1_verify_output.md`, add explicit regression tests for every counterexample discovered by the auditor, re-run the full verification suite, and confirm zero errors!

## Strict Repair Checklist (Fix Every Single Item)

### SEVERE & MAJOR Repairs
1. **`docs/phase1_pde.md` (Theorem 4a, lines 83–89)**:
   - Restrict the corner-cut statement explicitly to an **axis-aligned rectangle** with a **proper straight corner cut** joining the relative interiors of two adjacent sides (and explicitly note the tilted-diamond counterexample $\{|x|+|z|\le 1, z \le 1/2\}$, which has a common supporting fixed vertex / one-sided corner trap at every transverse slope and zero period-three tongues!).
2. **`docs/phase1_multiple.md` (Theorem 1, lines 13–23)**:
   - Insert **"attracting"** in the last sentence of Theorem 1 and its closing proof paragraph ("The same upper bound $k-3$ applies to regular hyperbolic **attracting** cycles avoiding every tangent chord at an edge-parallel parameter", and by reversal separately to repelling cycles), and note why the combined count of attracting + repelling cycles can exceed $k-3$ (e.g., 4 in the characteristic hexagon).
3. **`experiments/phase1_probe.py` (`CirclePL`, knot merging, fixed-cell classification, rotation test, lines 22–175)**:
   - Fix **MAJOR #4**: Replace `math.floor` with precision-preserving `mp.floor` for `mpmath.mpf` and exact `//` (floor division) for `Fraction`/exact integers in BOTH evaluation and inversion of `CirclePL`! Add a regression unit test with knots `(0, 1/2, 1)`, images `(0, 1/4, 1)` at `x = 1 - 10^{-20}` (95 digits) confirming `1 - (3/2)*10^{-20}` and exact inverse!
   - Fix **MAJOR #3**: For exact `Fraction` inputs, use exact predicates with ZERO tolerance (no knot merging, no zeroing of nonzero displacements). For `mpmath` / trigonometric inputs, use outward interval enclosures (or strict separation checks) to certify nonzero signs and explicitly return **`unresolved`** whenever zero cannot be separated — NEVER claim an exact global identity or neutral piece from a floating-point tolerance alone! Add an explicit regression test on the upright unit square at `s = 1 + 10^{-60}` (both `Fraction` and 72-digit `mpf`) verifying that the exact path finds NO period-2 point and the floating path returns `unresolved` (NEVER a false period-2 identity!).
   - Also update `docs/phase1_regular.md` line 278 to reflect exact vs. interval/unresolved classification accurately.
4. **`docs/phase1_scouting.md` (line 188)**:
   - Fix **MAJOR #5**: Insert **"regular"** before "$N$-gon" ("a generic orientation of every even **regular** $N$-gon has exactly $N/2 - 1$ attracting two-cycles..."), and verify no other overview line drops "regular".

### ALL MINOR Repairs (Docs + Code + Historical Attributions)
5. **`docs/phase1_scouting.md`**:
   - Lines 5–11: State normalized design inputs $0 < r_1 < \cdots < r_m < a < 1$ on first use; state reduced tilt $0 < \phi < \pi/4$ explicitly before quoting $\cos\phi - \sin\phi$ (noting larger tilts reduce by swapping body axes, and at $\phi = 45^\circ$ the open supercritical window is empty and the characteristic angle has zero kernel).
   - Line 64: Restrict the algebraic-root assertion to **tongue endpoints and isolated neutral angles** (with coefficients depending on $R, \tan\phi$), since an interior rational label selects an open tongue.
   - Line 127: Match `docs/phase1_pde.md` line 219 wording — state clearly that on the L triomino the displayed separated sine products are provably incomplete (all vanish on the interior segment $x=1, 0<z<1$), and the separate completeness question concerns the **full eigenspaces**.
   - Line 256–260 & `docs/phase1_measure.md` lines 211–213 & `docs/phase1_rectangle.md` lines 297–324: Fix ALL historical attributions:
     - Nogueira–Troubetzkoy Theorem 13: periodic direction pairs **contain an open dense subset** (the full periodic locus is not open).
     - Kopecz (2006, p. 9): credit his analytic derivation of $k(t_1+t_2)=1$ for arbitrary $k$ (so do NOT describe all his high-period analysis as purely numerical).
     - Bajars–Frank–Maas (2013): cite **§2.4** consistently for the parity discussion.
     - Credit Lenci–Bonanno–Cristadoro Remark 3.5 & eq. (3.10) for the two break-return equations for arbitrary tongue boundaries, Soares (2021) for established fixed-Hecke-group dimension bounds, and Zhu–Li (2022, §4.1) for numerical dimension studies of fixed tilted squares.
     - Zhang–Temnov (2026): state **wall-normal component** in describing their reflection argument, note their frequency convention $\sin^2\theta = 1 - E_{\mathrm{study}}$ (agreeing at $1/2$), and keep the rebuttal scoped to the constant-coefficient Dirichlet streamfunction problem.
6. **Consistent Operator Convention across ALL docs (`phase1_pde.md`, `phase1_measure.md`, `phase1_scouting.md`, etc.)**:
   - Consistently use $T = \Delta_D^{-1}\partial_z^2$ on $H_0^1(\Omega)$ and $P = \partial_z^2 \Delta_D^{-1}$ on $H^{-1}(\Omega)$ ($P \Delta_D = \Delta_D T$), clarifying that the pointwise detector measures the streamfunction $u \in H_0^1(\Omega)$.
7. **`docs/phase1_canonical.md` (lines 71–76)**: State explicitly `for \rho(b) = 1/n` (vs. `\rho(F) = 1/(n-1)`) next to "Each odd $n$ is global".
8. **`docs/phase1_measure.md` (lines 173–179)**: State "all **regular physical rays** close" (and note global identity on the continuously extended boundary map, with multiplicity at vertices).
9. **`docs/phase1_multiple.md` (lines 25–36)**: Replace "rational polygon" with **"polygons with rational vertices"** throughout (to avoid collision with rational-angle billiards).
10. **Code Hardening across ALL scripts**:
    - `experiments/phase1_pde.py` (lines 46–62): In `periodic_set`, exclude points belonging to the cyclic closures of neutral intervals from `isolated` (or return subdivision points separately), so the critical diamond does not report 4 "isolated" vertices alongside its 4 fixed intervals!
    - `experiments/phase1_rectangle.py` (lines 18–46): Convert integer stretch inputs cleanly to `Fraction` before division so `section_tongue(1, 1, 2)` returns exact `(Fraction(1,3), Fraction(2,3))`.
    - `experiments/phase1_multiple.py` (lines 69–79 & 132–135): Normalize or assert counterclockwise vertex ordering in `sharp_polygon` / rectangle enumeration; check that both interval endpoints round identically to the displayed digits!
    - `experiments/phase1_regular.py` (lines 30–38 & 310–321): Label `q` as a candidate when $\gcd(k,N)=1$ until a genuine period-$q$ orbit is found (avoid printing "period 5" with empty census for `--resonance 5 1 5` inside the corner band!); raise precision or report insufficient resolution for tiny tilts like `8 4 1e-40`.
    - `experiments/phase1_measure.py` (lines 60–73): Enforce $R > \tan(2\phi)$, $N \ge 1$, and a resolved interior bracket in the re-entry root helper (raising a clear error or solving for scaled edge distance when under-resolved).
    - `experiments/phase1_probe.py` (lines 269–278 & 368–388): Strengthen the octagon probe to assert rotation numerator, both cycle counts, and absence of neutral/vertex roots; mask singular grid samples (`theta ± phi` on critical lines or primary tongue endpoints) using exact integer/symbolic grid checks so the tilted-square phase portrait NEVER miscolors boundary/critical points as regular interiors! Regenerate `figures/phase1_square_tongues.png` and `experiments/data/phase1_results.txt` via `python3 experiments/phase1_probe.py --scan --figure` and verify ALL tests + new regression tests pass with exit code 0!

## Deliverable
Apply all fixes cleanly, run `python3 experiments/phase1_probe.py --scan --figure` (and any individual script checks), and return a concise point-by-point summary confirming every single SEVERE, MAJOR, and MINOR item from `phase1_verify_output.md` has been fixed and regression-tested.
