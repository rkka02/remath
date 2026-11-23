# Cumulative Study Ledger — Project ReMath

Each completed or active research expedition lives in its own self-contained folder under `studies/<NN-slug>/` and mirrors the same `<NN-slug>` on the public research portal at [https://rkka02.github.io](https://rkka02.github.io).

| ID | Slug | Status | Core Subject & Headline Results | Publications | Lean 4 | Live Brief |
|---|---|---|---|---|---|---|
| **01** | [`01-leontiev-invisible-loads`](studies/01-leontiev-invisible-loads/STUDY.md) | **Published · Referee Audited** | Excavates A. F. Leont'ev's untranslated Soviet exponential series (1969–1987) and bridges it to Fokas's Unified Transform Method: universal invisible-load table, parallelogram torsion criterion vs. equilateral triangle 1D Riemann-zeta Y-skeleton, 60°/120° rhombus two-slope minimax law ($N^{-5/6}$ vs. $N^{-2/3}$), 230-digit interval proof of half-step suboptimality, 23.5-order super-resolution, and Fokas PDE completion. | 2 EN preprints + 1 KR feature (3 PDFs, 10 figs) | 31 theorems (`0 sorry`) | [Study #01 ↗](https://rkka02.github.io/studies/01-leontiev-invisible-loads/) |

---

## Starting Study #02+

```bash
python3 scripts/new_study.py 02-next-slug "Short Study Title"
```

After completing a study, update this table and sync curated artifacts to `../rkka02.github.io` via:

```bash
python3 scripts/publish_to_portal.py 02-next-slug
```
