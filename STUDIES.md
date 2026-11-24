# Cumulative Study Ledger — Project ReMath

Each completed or active research expedition lives in its own self-contained folder under `studies/<NN-slug>/` and mirrors the same `<NN-slug>` on the public research portal at [https://rkka02.github.io](https://rkka02.github.io).

| ID | Slug | Status | Core Subject & Headline Results | Publications | Lean 4 | Live Brief |
|---|---|---|---|---|---|---|
| **01** | [`01-leontiev-invisible-loads`](studies/01-leontiev-invisible-loads/STUDY.md) | **Published · Referee Audited** | Excavates A. F. Leont'ev's untranslated Soviet exponential series (1969–1987) and bridges it to Fokas's Unified Transform Method: universal invisible-load table, parallelogram torsion criterion vs. equilateral triangle 1D Riemann-zeta Y-skeleton, 60°/120° rhombus two-slope minimax law ($N^{-5/6}$ vs. $N^{-2/3}$), 230-digit interval proof of half-step suboptimality, 23.5-order super-resolution, and Fokas PDE completion. | 2 EN preprints + 1 KR feature (3 PDFs, 33 pp., 10 figs) | 31 theorems (`0 sorry`) | [Study #01 ↗](https://rkka02.github.io/studies/01-leontiev-invisible-loads/) |
| **02** | [`02-tsetlin-collective-automata`](studies/02-tsetlin-collective-automata/STUDY.md) | **Published · Unanimous 3-Judge · 4-Round Referee Sign-Off** | Excavates M. L. Tsetlin's Moscow collective automata school (1961–1966): strict correlated-feedback hierarchy $F_L=F_B<F_D<F_K$, diffusive $n^{-1/2}$ criticality, 61-year Volkonskii (1965, p. 47) erratum refutation, weak-reward inversion, payoff-independent optimal imperfect correlation $\kappa_*(\gamma)=\frac{1+1/\gamma}{2}$, Möbius interface splitting ($8{,}994\times$), fair-$DD$ three-way elliptic cancellation ($3.4258\to 0.8565\to 1$), unilateral $+1$-depth social collapse ($99.98\%\to 0.0018\%$), open-region Stag-Hunt mirages, and below-Nash partial Common Funds with sharp memory cutoff $n_c=2$. | 2 EN preprints + 1 KR feature (3 PDFs, 33 pp., 10 figs) | 117 public theorems · 911 audited constants (`0 sorry`) | [Study #02 ↗](https://rkka02.github.io/studies/02-tsetlin-collective-automata/) |
| **03** | [`03-sobolev-wave-attractors`](studies/03-sobolev-wave-attractors/STUDY.md) | **Published · Unanimous 3-Judge · 8-Round Referee Sign-Off** | Excavates the Soviet Sobolev–Aleksandryan–Zelenyak–Fokin rotating-fluid school (1943–2002): sharp half-amplitude uncloakability $\|u\|_{L^\infty(\Gamma)}\ge\frac{1}{2}\|u\|_{L^\infty(\Omega)}$, exact $N\ge m+5$ multi-attractor coexistence threshold, fixed-tank tilt catastrophe $|\mathcal{A}_{R,\phi}|_\lambda=\cos\phi-\sin\phi$ ($99.998\%$ at $0.001^\circ$), uniform $\dim_H E_{R,\phi}<1$ with local Hecke dimension identity, spectral extinction iff $\cot(2\phi)\le R\le\tan(2\phi)$ (refuting Zhang–Temnov 2026), permanent $\ge 17.806\%$ microscopic corner-shaving jump, all-polygon rigidity, and the $1000$-gon vs. $1002$-gon disk-limit paradox with $O(N^{-3/2})$ quasimode. | 2 EN preprints + 1 KR feature (3 PDFs, 47 pp., 10 figs) | 125 public theorems · 40 principal (`0 sorry`) | [Study #03 ↗](https://rkka02.github.io/studies/03-sobolev-wave-attractors/) |

---

## Starting Study #04+

```bash
python3 scripts/new_study.py 04-next-slug "Short Study Title"
```

After completing a study, update this table and sync curated artifacts to `../rkka02.github.io` via:

```bash
python3 scripts/publish_to_portal.py 04-next-slug
```
