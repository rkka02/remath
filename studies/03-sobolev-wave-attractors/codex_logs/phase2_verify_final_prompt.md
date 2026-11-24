# Independent Read-Only Verification Audit (`phase2_verify_final`) — Study #03

You are an **independent, unforgiving `read-only` mathematical & computational referee** (`gpt-6.2-astra`, max reasoning) auditing `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors` BEFORE a Pitch Packet is submitted to a strict 3-judge panel.

Do NOT trust prior summary files (`phase2_repairs_r2_output.md`, `phase2_verify_r2_output.md`) without checking the actual source documents and executing the Python scripts yourself (read-only execution via Python without modifying any project files; use `PYTHONDONTWRITEBYTECODE=1`).

## Mandatory Checks
1. **Verify ALL 4 Flagship Pillars & Proofs in `docs/phase1_*.md`**:
   - Pillar 1 (`phase1_coexistence.md`, `phase1_central_bounds.md`, `phase1_multiple.md`, `phase1_scouting.md`):
     - Sharp Half-Amplitude Uncloakability Theorem ($\|u\|_{L^\infty(\Gamma)} = \max_{w\in H(\partial\Omega)}|w-c_\Gamma| \ge \frac12 \|u\|_{L^\infty(\Omega)}$, including vertex-only extrema and energy 256 sharpness example).
     - Prescribed-rate $m+5$-side inverse construction ($0 < r_1 < \cdots < r_m < a < 1$, $\kappa_i \in (0,1)$, exact eigenspace $u_h$, Dirichlet energy $4\int_a^1 |h'|^2$, infinite-rank norm-1 jump $\|\Pi_1-\Pi_\kappa\|=1$).
     - Sharp side-count bounds: $k-3$ attracting cycles (all periods, including transverse-chord characteristic extension counting attractors and repellers separately), $k-5$ with period-2 neutral beam, central $h-3$ ($2h=2m+6$), and $k \ge m+4$ excluding mixed quadrilaterals at all periods.
     - Hexagon basin fractions $(1/4, 1/2, 1/4)$ and no-global-exterior-capture proposition.
   - Pillar 2 (`phase1_measure.md`, `phase1_parity.md`, `phase1_rectangle.md`, `phase1_canonical.md`):
     - Reduced-tilt ($0 < \phi < \pi/4$) fixed-tank full measure ($\cos\phi - \sin\phi$ in $\lambda$, $\pi/2-2\phi$ in $\theta$, $\cos(2\phi)$ in $\lambda^2$), uniform Hausdorff dimension $< 1$ & $> 1/2$, local dimension identity, exact integer $9/10$ certificate (`< 991/1000` for $\phi \ge 15^\circ$).
     - All five canonical quadrilateral boundary parity laws and universal attracting multipliers ($\Lambda^{-1}, \Lambda^{-2}, \Lambda^{-2}, \mu^{-2}$).
     - Exact extinction criterion $\sigma_p(T) = \emptyset \iff \cot(2\phi) \le R \le \tan(2\phi)$, geometric re-entry rate, small-tilt tongue widths, and Zhang–Temnov (2026) counterexamples.
   - Pillar 3 (`phase1_pde.md`, `phase1_rigidity.md`):
     - Finite-energy PDE criterion (Theorems 1–3), all triangles & axis-diagonal diamonds ($\sigma_p = \emptyset$), global convex-polygon rigidity (axis-aligned rectangle unique), shallow travel-time obstruction, central period-2 criterion $S_r K \ne K$.
     - Corrected axis-aligned corner-cut Theorem 4a (plus tilted-diamond counterexample), Theorem 4b plateaus ($[m/n, m/(n-u)]$ with $\varepsilon$-independent multiplier $(\tau-s)/(\tau+s)$), Corollary 4c microscopic shaving liminf $\frac{6}{\pi^2}(1-1/\sqrt{2}) \approx 17.80577\%$.
     - Nonconvex orthogonal/polyomino Theorems 5–6 (including L-triomino separated-product incompleteness).
   - Pillar 4 (`phase1_regular.md`, `phase1_regular_measure.md`, `phase1_multiple.md`):
     - Corner ranges, exact mirror frequencies ($N = 4mq$), resonance grid & telescoping product, $N=4m+2$ half-frequency 500 attractors & $-N\ell_N \Rightarrow 2\pi/\sin(\pi U)$ distribution, odd-$N$ attaining $N-3$, octagon discontinuous cliff $-2\log(1+\sqrt{2})$, $O(N^{-3/2})$ quasimode (`0.000130638` at $N=1002$), growing-period measure bound $Q = o(N/\sqrt{\log N})$.
2. **Verify ALL Prior Blockers from `phase1_verify_output.md` and `phase2_verify_output.md` Are 100% Closed**:
   - Test `PYTHONDONTWRITEBYTECODE=1 python3 experiments/test_phase1_repairs.py` and `PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_probe.py`.
   - Independently stress-test the exact tricky cases: 15-digit `mp.tan(mp.pi/4)` at 72 dps, `s = 1 + 10^{-60}`, `CirclePL` at `1 - 10^{-20}`, notched nonconvex hexagon convexity guard, `boundary_map(2,1)`, `reflect` at `10**20`, `normal_return(1-1e-20, 1, 2)`, `primary_low_intervals` at `phi=1e-25`, `--resonance 4 2 1e-8`, and `8 4 1e-40` bisection.
   - Check notation consistency ($T = \Delta_D^{-1}\partial_z^2$ on $H_0^1$, $P = \partial_z^2\Delta_D^{-1}$ on $H^{-1}$, $s = \tan\theta = \sqrt{1-\lambda^2}/\lambda$, $\lambda = \cos\theta$), reduced-tilt scoping, rational-vertex wording, and historical attributions.

## Required Verdict
State clearly **`CLEAN — READY TO PITCH`** (if 0 SEVERE, 0 MAJOR, and 0 open proof/code/attribution defects remain) OR list every single remaining defect with exact file path and line number.
