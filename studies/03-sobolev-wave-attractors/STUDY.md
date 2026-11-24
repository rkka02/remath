# Study #03 — Excavating the Soviet Sobolev–Aleksandryan–Zelenyak–Fokin School of Wave Attractors

- **Slug**: `03-sobolev-wave-attractors`
- **Status**: Completed · Unanimous 3-Judge PASS (Round R1: `9.4 / 9.3 / 9.3`) · Read-Only Referee Sign-Off (`ZERO BLOCKING DEFECTS — ACCEPT AS IS`, after 8 rounds of `gpt-6.2-astra` max) · Lean 4.36.0 Verified (`125 public theorems`, `40 principal results`, `0 sorry`)
- **Research Portal Target**: `https://rkka02.github.io/studies/03-sobolev-wave-attractors/`

---

## Publications (3 Self-Contained, Non-Overlapping PDFs · 47 pp. Total)

1. **Paper 1 (English Academic Preprint, `amsart`, 19 pp.)** — [`papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.pdf`](papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.pdf) ([`.tex`](papers/paper1_uncloakable_coexistence/paper1_uncloakable_coexistence.tex))
   - *Uncloakable Standing Waves and Prescribed Multi-Attractor Coexistence in Polygonal Sobolev Tanks*
   - Dedicated figures (3): `papers/paper1_uncloakable_coexistence/figs/p1_fig{1_hexagon_uncloakability,2_prescribed_multi_attractors,3_pentagon_and_obstructions}.png`
2. **Paper 2 (English Academic Preprint, `amsart`, 20 pp.)** — [`papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.pdf`](papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.pdf) ([`.tex`](papers/paper2_tilt_rigidity_circle_limit/paper2_tilt_rigidity_circle_limit.tex))
   - *Tilt Catastrophe, Microscopic Corner Shaving, All-Polygon Rigidity, and the Disk-Limit Paradox for Sobolev Wave Attractors*
   - Dedicated figures (3): `papers/paper2_tilt_rigidity_circle_limit/figs/p2_fig{1_tilted_square_and_extinction,2_shaving_and_rigidity,3_circle_paradox_and_octagon}.png`
3. **Expository Magazine Feature (Korean, `xeCJK`, 8 pp.)** — [`papers/expository_kr/expository_sobolev_attractors_kr.pdf`](papers/expository_kr/expository_sobolev_attractors_kr.pdf) ([`.tex`](papers/expository_kr/expository_sobolev_attractors_kr.tex))
   - *1943년 소련의 회전 팽이 방정식에서 발굴한 '파동 블랙홀'의 비밀: 종이 한 장 기울기의 대붕괴, 모래알 모서리 절단, 완벽 은폐 불가능 정리, 그리고 1000각형 대 1002각형의 역설*
   - Dedicated figures (4): `papers/expository_kr/figs/kr_fig{1_compass_and_two_walls,2_tilt_and_sand_chip,3_impossible_cloak_hexagon,4_1000_vs_1002_and_octagon}.png`

---

## Headline Discoveries (All Verified & Referee-Signed)

1. **Universal Half-Amplitude Uncloakability & Sharp $m+5$ Multi-Attractor Coexistence** (Paper 1, Theorems 3.1, 4.1–4.3, 5.1; Lean `Uncloakability.lean`, `MultiplicityBounds.lean`):
   - On any convex polygon at a noncharacteristic rational-rotation frequency, every finite-energy standing mode $u \in H_0^1(\Omega)$ satisfies $\|u\|_{L^\infty(\Gamma)} = \max_{w \in H(\partial\Omega)} |w - c_\Gamma| \ge \frac{1}{2}\|u\|_{L^\infty(\Omega)}$ along the spatial path $\Gamma$ of *every* coexisting regular periodic ray (including every attracting wave-attractor circuit), with sharp constant $1/2$ attained uniquely at the midrange level.
   - Coexistence of a full infinite-dimensional standing-mode space with $m$ independent period-$2$ (4-reflection) attractors of arbitrary prescribed multipliers $\mu_1,\dots,\mu_m \in (0,1)$ has the sharp side threshold $N \ge m + 5$ ($N \ge 2m + 6$ under central symmetry), realized concretely on a rational-vertex hexagon ($m = 1$, exact return $y' = 1/8 + y/2$, basin fraction $1/2$, interior peak $2$ vs. circuit peak $1$) and a centrally symmetric octagon ($y' = 3/16 + y/4$).
   - Complete finite-energy $H_0^1$ boundary-profile criterion yields $\sigma_p(T) = \varnothing$ on every triangle and axis-diagonal diamond, sharp side-count caps on simultaneous periodic cycles ($k - 3$ per orientation, attained on odd regular $N$-gons at $\lambda = 1/\sqrt{2}$), and an orthogonal-polyomino spectral theorem (every $a\times b$ grid polyomino shares the exact point spectrum of its $a\times b$ mesh rectangle, while separated sine products fail completeness in $H_0^1$ on the L-triomino).
2. **Fixed-Tank Tilt Catastrophe, Local Hecke Dimension Identity, Five-Tank Parity Law & Spectral Extinction** (Paper 2, Theorems 2.1–2.5; Lean `TiltedParity.lean`):
   - For *every fixed* tilted rectangle of aspect ratio $R > 0$ and reduced tilt $0 < \phi < \pi/4$, regular periodic attractors occupy exact physical frequency length $\cos\phi - \sin\phi$ (jumping discontinuously from $0$ at $\phi = 0$ to $1 - O(\phi)$ as $\phi \downarrow 0$, e.g. $99.998\%$ at $0.001^\circ$), with corner capture filling $1 - \cos\phi + \sin\phi$; analogously $1 - \sin\alpha$ and $\sin\alpha$ for every fixed horizontal-base right trapezoid, isosceles trapezoid, and sheared parallelogram of wall tilt $\alpha \in (0,\pi/2)$.
   - Via Hecke-group coding, holomorphic motion, and strict moving-gap transversality: uniform Hausdorff-dimension gap $\dim_H E_{R,\phi} \le d_\phi < 1$, exact local dimension identity $\lim_{\varepsilon\downarrow 0}\dim_H(E_{R,\phi}\cap(\theta_c-\varepsilon,\theta_c+\varepsilon)) = \dim_H K_{u(\theta_c)} > 1/2$, and an exact integer tenth-power certificate $\dim_H E_{R,\phi} \le 9/10$ for all $\phi \ge 15^\circ$.
   - Exact spectral extinction law $\sigma_p(T) = \varnothing \iff \cot(2\phi) \le R \le \tan(2\phi)$ (with geometric re-entry accumulation rates outside extinction), exact five-tank boundary-parity table, small-tilt tongue widths $2\phi/(mn)$, and explicit counterexamples refuting both directions of Zhang–Temnov (2026, Thm. 2.3).
3. **Microscopic Corner-Shaving Permanence & All-Polygon Rigidity** (Paper 2, Theorems 3.1 & 3.2; Lean `CornerShavingAndTriangles.lean`):
   - Shaving a single corner of the unit square by equal legs $\varepsilon \downarrow 0$ (area $\varepsilon^2/2 \to 0$) produces exact rational plateaus $[m/n, m/(n-\varepsilon)]$ with $\varepsilon$-independent multiplier $(1-s)/(1+s)$, giving the permanent physical-frequency measure jump $\liminf_{\varepsilon\downarrow 0} |\mathcal{A}_\varepsilon|_\lambda \ge \frac{6}{\pi^2}(1 - 1/\sqrt{2}) = 0.1780577\ldots$ ($79{,}594$ certified intervals already achieve $17.728\%$ at $\varepsilon = 0.00195$, shaved area $0.00019\%$).
   - **All-Polygon Rigidity**: among all bounded convex polygons, the axis-aligned rectangle is the unique shape free of both regular hyperbolic attractors and one-sided attracting corners at every transverse slope (with a density-$1$ attracting period census on a square-symmetric chamfered octagon via Hermite–Lindemann).
4. **The Disk-Limit Paradox ($1000$-gon vs. $1002$-gon) & Polar-Shell Quasimode** (Paper 2, Theorems 4.1–4.3):
   - At the midpoint frequency $\lambda = 1/\sqrt{2}$, the vertex-aligned regular $N$-gon with $N = 4m$ (e.g. $N = 1000$) has an infinite-dimensional standing-mode eigenspace, whereas adding two sides to $N = 4m + 2$ (e.g. $N = 1002$) shatters the frequency into $2m = N/2 - 1$ ($500$) simultaneous attracting wave-attractor circuits (strongest per-step factor $(2\cos(\pi/N)-1)/(2\cos(\pi/N)+1) \to 1/3$, equal-weight mean Lyapunov exponent $\frac{2}{N/2-1}\log\tan(\pi/(2N))$, arclength-weighted median $\sim -2\sqrt{2}\pi/N$).
   - Simultaneously, for every $Q = o(N/\sqrt{\log N})$, the total frequency measure of all periods $\le Q$ vanishes uniformly in orientation as $N \to \infty$, and an explicit $H_0^1$ polar-shell Dirichlet quasimode achieves relative residual $\le 1.307\times 10^{-4}$ at $N = 1002$ (decaying as $O(N^{-3/2})$ with exact scaled energy constant $\frac{4}{15}\pi^4 + \frac{2}{3}\pi^2$).

---

## Archive Contents

- **Primary Sources (`sources/`)**: [`sources/PRIMARY_SOURCES.md`](sources/PRIMARY_SOURCES.md) + 13 open-access PDFs (5 Soviet/Russian Math-Net.Ru classics: Sobolev 1954, Aleksandryan 1960, Zelenyak 1965, Fokin 2001/2002 + 8 modern arXiv papers: Colin de Verdière–Saint-Raymond 2018, Dyatlov–Zworski 2018, Nogueira–Troubetzkoy 2020, Lenci–Bonanno–Cristadoro 2021, Dyatlov–Wang–Zworski 2021, Zhu–Li 2022, Li 2023, Li 2024) in `sources/papers/`.
- **Formal Proofs (`proofs/lean4/`)**: 4 standalone Lean 4.36.0 modules (`Uncloakability.lean`, `MultiplicityBounds.lean`, `TiltedParity.lean`, `CornerShavingAndTriangles.lean`) + `Main.lean` kernel axiom audit (**125 public theorems** including **40 principal results**, 101 private lemmas, **0 `sorry`**, **0 warnings** under `-DwarningAsError=true`, standard axioms `propext`, `Classical.choice`, `Quot.sound` only). Full inventory in [`docs/phase3_lean4_inventory.md`](docs/phase3_lean4_inventory.md).
- **Technical Proofs & Logs (`docs/`)**: [`docs/RESEARCH_LOG.md`](docs/RESEARCH_LOG.md), [`docs/phase1_scouting.md`](docs/phase1_scouting.md), and 10 detailed technical chapters (`docs/phase1_*.md`, `docs/phase3_lean4_inventory.md`).
- **High-Precision Scripts & Regression Suite (`experiments/`)**: 75–420+ digit `mpmath` / outward-interval verification modules (`phase1_probe.py`, `phase1_measure.py`, `phase1_regular.py`, `phase1_coexistence.py`, `phase1_parity.py`, `phase1_rectangle.py`, `phase1_rigidity.py`, `phase1_central_bounds.py`, `phase1_multiple.py`, `phase1_pde.py`), 53-test regression suite (`test_phase1_repairs.py`), and zero-warning figure generator (`generate_paper_figures.py`).
- **Codex Astra Max Logs (`codex_logs/`)**: Full reproducible prompts and outputs across Phase 1 scouting, Phase 2 verification rounds R1–R2 (`phase2_verify_r2_output.md`), Phase 3 Lean 4 formalization (`phase3_lean4_output.md`), and Phase 4 read-only referee rounds R1–R8 (`phase4_referee_r1..r8_output.md`, ending with `ZERO BLOCKING DEFECTS — ACCEPT AS IS (PUBLICATION SIGN-OFF GRANTED)`).

---

## Reproducibility & Verification Commands

Run from `studies/03-sobolev-wave-attractors/`:

```bash
# 1. Machine-verify all 125 public Lean 4 theorems (40 principal) from scratch + axiom audit
(cd proofs/lean4 && /Users/mw/.elan/bin/lake clean && /Users/mw/.elan/bin/lake build && /Users/mw/.elan/bin/lake env lean Main.lean)

# 2. Run the full 53-test high-precision & interval-arithmetic regression suite
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s experiments -p 'test_*.py' -v

# 3. Run the core numerical verification CLIs
PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_measure.py
PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_regular.py --tongues
PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_probe.py --scan

# 4. Regenerate all 10 dedicated publication figures (0 matplotlib warnings)
PYTHONDONTWRITEBYTECODE=1 python3 -W error::UserWarning experiments/generate_paper_figures.py

# 5. Compile all 3 self-contained PDFs (0 TeX errors, 0 Overfull warnings)
(cd papers/paper1_uncloakable_coexistence && /opt/homebrew/bin/tectonic paper1_uncloakable_coexistence.tex)
(cd papers/paper2_tilt_rigidity_circle_limit && /opt/homebrew/bin/tectonic paper2_tilt_rigidity_circle_limit.tex)
(cd papers/expository_kr && /opt/homebrew/bin/tectonic expository_sobolev_attractors_kr.tex)
```
