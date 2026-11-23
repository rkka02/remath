# Phase 1 Mathematical Research Scouting Brief — Project ReMath (A. F. Leont'ev)

You are the lead mathematical researcher (`gpt-6.2-astra`, max reasoning) collaborating with a Research Director on an ambitious mathematical archaeology project in `/Users/mw/Desktop/math/remath`.

## Context & Primary Sources Available in This Repo
We have excavated and archived original Soviet primary papers of **A. F. Leont'ev** (Ufa/Moscow) and **Yu. F. Korobeinik** from Math-Net.Ru, plus modern convex-polygon PDE papers by **A. C. L. Ashton & A. S. Fokas**:
- `sources/extracted/Leontev_1987_TrMIAN_176_rus.txt` — Leont'ev's final 1987 Steklov anniversary master survey (*Ряды и последовательности полиномов из экспонент*), including Section 3 on convex polygons and periodic half-plane ray decompositions ($F(z) = \sum_{n=1}^p F_n(z)$ with $\lambda_m^{(n)} = \frac{2\pi i m}{\gamma_{n+1}-\gamma_n}$).
- `sources/extracted/Leontev_1973_IzvAN_37_rus.txt` — Leont'ev (1973) on closed convex domains.
- `sources/extracted/Leontev_1969_MatSb_80_first10p.txt` — Leont'ev (1969) landmark *Mat. Sb.* paper.
- `sources/extracted/Korobeinik_1981_UMN_36_first10p.txt` — Korobeinik (1981) *UMN* survey on representing systems and nontrivial expansions of zero.
- `sources/extracted/Ashton_2012_Fokas_Polygon.txt` — Ashton (2012) on Fokas's Unified Transform Method on convex polygons (rays $\ell_j$, spectral functions $\rho_j(\lambda)$, Global Relation $\sum_{j=1}^p \rho_j(\lambda) = 0$).

## Mission & Quality Bar
We do NOT want a textbook summary or a minor technical tweak. We are searching for a **genuinely original, rigorously provable, numerically verifiable, and conceptually astonishing mathematical discovery** rooted in A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*) — something so striking that even a mathematically curious non-specialist would say **"Whoa! Wait — THAT connects to THIS, and it actually works?!"**, while a professional complex analyst / PDE / applied mathematician would verify every step and say **"Wait, that's actually true and non-trivial!"**

## Your Phase 1 Task
Read the relevant sections of `sources/extracted/Leontev_1987_TrMIAN_176_rus.txt` and `sources/extracted/Ashton_2012_Fokas_Polygon.txt` (and check any needed details from the other extracted files). Then do deep mathematical analysis — AND run quick Python exploratory calculations (`experiments/phase1_probe.py` if helpful) using `numpy`/`scipy`/`mpmath`/`sympy` — to evaluate **FOUR candidate breakthrough frontiers** and find which one holds genuine mathematical gold (not fool's gold!):

### Candidate 1: Exact Bridge Between Leont'ev's Soviet Exponential Series (1969–1987) and Fokas's Unified Transform Method (1997–2020s) on Convex Polygons
- On a convex $p$-gon $D$ with vertices $\gamma_1,\dots,\gamma_p$, BOTH theories decompose holomorphic (hence harmonic!) functions along the **exact same $p$ rays** perpendicular to the edges of $D$:
  - Fokas: continuous ray integrals $F(z) = \frac{1}{2\pi}\sum_{j=1}^p \int_{\ell_j} e^{i\lambda z} \rho_j(\lambda)\,d\lambda$ with Global Relation $\sum_{j=1}^p \rho_j(\lambda) = 0$.
  - Leont'ev: discrete ray sums $F(z) = \sum_{j=1}^p F_j(z) = \sum_{j=1}^p \sum_{m=1}^\infty c_m^{(j)} e^{\lambda_m^{(j)} z}$, where $F_j$ is periodic along edge $j$ with period $\gamma_{j+1}-\gamma_j$, and representation exists iff nontrivial expansions of zero exist.
- **Probe deeply**:
  1. Is there an **exact analytic bridge theorem** (not just a vague analogy!) turning Fokas's continuous ray integral into Leont'ev's discrete periodic ray-series (e.g., via contour deformation / residue calculus against $1/L(\lambda)$ / Poisson summation / periodization of Cauchy kernels)? Derive the exact formula and check carefully for boundary terms, convergence, poles, and signs!
  2. Does Fokas's **Global Relation** $\sum_{j=1}^p \rho_j(\lambda) = 0$ have an exact algebraic/functional correspondence with Leont'ev's **space of nontrivial expansions of zero** $\mathcal{Z}(D,\Lambda)$ or Leont'ev's interpolating function $\omega_L(\lambda, F)$?
  3. Could this bridge produce a **brand-new exact/spectral PDE method** (e.g., solving Laplace, Helmholtz, or biharmonic/convolution PDEs on polygons using Leont'ev's periodic edge-waves directly, or resolving a subtlety in Fokas's method)?

### Candidate 2: "Ghost Waves / Perfect Silence" — The Exact Geometry, Gauge Theory & Non-Convex Breakthrough of Nontrivial Expansions of Zero
- On a convex $p$-gon $D$, a nontrivial expansion of zero splits as $Z_1(z) + \dots + Z_p(z) \equiv 0$ inside $D$, where each $Z_j(z)$ is a non-zero edge-periodic holomorphic wave on the half-plane $H_j$.
- **Probe deeply**:
  1. What is the **exact algebraic/cohomological/functional characterization** of the "Ghost Wave Space" (all tuples $(Z_1,\dots,Z_p)$ of edge-periodic half-plane holomorphic functions summing to $0$ on $D$)? Is it isomorphic to a concrete space of entire functions (via $L(\lambda)$)? Can we write down **stunning closed-form elementary examples** on an equilateral triangle or square and see what happens to $Z_1,\dots,Z_p$ *outside* $D$ (e.g., analytic continuation, singularities at vertices/periodically translated polygons, "ghost lattice" of the polygon)?
  2. **Can we break the convexity barrier?** For a **non-convex** polygon (e.g., an L-shape or star), classical single exponential series fail because convergence domains are always convex. Can we use a **Čech/Cousin gluing of Leont'ev decompositions on overlapping convex sub-polygons**, controlled by the **Zero-Expansion gauge freedom** on the overlap, OR a sharp **harmonic/analytic continuation obstruction**, to prove something genuinely surprising about non-convex domains?

### Candidate 3: Optimal Redundancy, Phase Transitions & Inverse Geometry ("Hearing the Polygon from Zero" / Sparse Overcomplete Leont'ev Frames)
- Because Leont'ev's system is overcomplete (nonzero kernel $\mathcal{Z}(D,\Lambda)$), any $f \in H(D)$ has an infinite affine space of valid exponential representations $c + \mathcal{Z}(D,\Lambda)$.
- **Probe deeply**:
  1. What happens when you choose the **minimum-norm** ($\ell^2$ or $\ell^1$) or **steered** representation inside $c + \mathcal{Z}(D,\Lambda)$? Does the nullspace of zero-expansions allow **dramatic super-compression** or **selective ray silencing** (deleting/suppressing an entire frequency subset or shifting energy between edges)?
  2. What is the **exact sharp threshold** (density / angle / frequency removal) where representation breaks? And can you uniquely recover the exact polygon $D$ (inverse problem) from the zero-expansion data or frequency spectrum?

### Candidate 4: Wild Card — An Even Deeper Hidden Gem in Leont'ev's Theory
- While digging into Leont'ev's 1969/1973/1987 papers and running calculations, if you uncover a **4th genuinely unexpected, sharper, or more mind-blowing theorem/connection** (for example involving quasi-analytic continuation on line segments from Section 3.3 of Leont'ev 1987, Mittag-Leffler $\rho$-convex curved polygons, discrete wave interference/superoscillations, number-theoretic Dirichlet series, or exact algebraic identities for $L(\lambda)$), propose and prototype it!

## Rigor & Deliverable Requirements
- **Be brutally honest**: If a candidate idea turns out to be trivial, already well-known in the literature, or mathematically false when checked carefully, SAY SO explicitly and kill it! Do NOT hype weak analogies.
- **Compute to check your intuition**: Write and run a Python verification script `experiments/phase1_probe.py` (using `mpmath` at high precision if needed) to numerically test at least the core explicit formulas (e.g., on an equilateral triangle and/or square) so we see REAL numbers, errors, convergence rates, and behaviors right away.
- **Produce a structured report** (as your final response, which will be saved to `codex_logs/phase1_scouting_output.md`) containing:
  1. Exact mathematical evaluation of Candidates 1–4 (with precise formulas, what works rigorously, what fails/is already known, and novelty assessment).
  2. Concrete results from `experiments/phase1_probe.py`.
  3. Your ranked recommendation of the **single strongest, most mathematically genuine AND most awe-inspiring ("오오! 이런게 이렇게 된다고?") research target** to push into full theorems, proofs, visuals, and formal verification in Phase 2.
