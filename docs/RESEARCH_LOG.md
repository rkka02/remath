# Research Log — Project ReMath (A. F. Leont'ev)

## 2026-11-23 — Session Start & Infrastructure Setup
- **Mission**: Excavate A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*, 1950s–1987, Ufa/Moscow), delegate heavy mathematical research/calculations/proofs to Codex (`gpt-6.2-astra`, `reasoning_effort=max`), steer toward a genuinely original, rigorously verified, and widely astonishing ("오오! 이런게 이렇게 된다고?") mathematical discovery, and keep everything version-controlled and archived.
- **Environment verified**:
  - Codex binary: `/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex` (`codex-cli 0.171.0-alpha.13`) — verified working with `-m gpt-6.2-astra`. (Note: Homebrew's older `0.144.1` failed on `models_cache.json` / ChatGPT account routing; using the bundled newer binary solved it immediately.)
  - Python 3.13.11 with `numpy`, `scipy`, `sympy`, `mpmath`, `matplotlib`, `torch`.
  - Lean 4 toolchain (`lean`, `elan`, `lake`) installed.
- **Initial strategic scouting hypothesis**:
  - Literature scan confirmed **zero existing papers** bridging A. F. Leont'ev's 1966–1976 Soviet discrete exponential series on convex polygons with A. S. Fokas's Unified Transform Method (1997–2020s) for PDEs on convex polygons!
  - Additional high-upside frontiers to scout simultaneously before locking in:
    1. **Leont'ev $\leftrightarrow$ Fokas Exact Residue/Global-Relation Duality & Discrete Polygon PDE Solver** (and whether Leont'ev's *nontrivial expansion of zero* IS the exact discrete manifestation of Fokas's Global Relation!)
    2. **The Physics & Geometry of "Nontrivial Expansions of Zero"**: splitting a zero-expansion on an $m$-gon into $m$ half-plane waves ("Perfect Silence / Complex Wave Cloaking inside a Polygon") + gauge freedom / optimal sparse compression / stealth waves.
    3. **Breaking the Convexity Barrier**: non-convex domains via sheaf/Cousin gluing of convex Leont'ev expansions, overconvergence grouping, or Mittag-Leffler $E_\rho(\lambda_n z)$ $\rho$-convex curved domains.
    4. **Spectral Geometry & Quasicrystalline / Arithmetic Structure of Polygon Zero-Rays**: inverting the polygon from its frequencies, exact arithmetic/diophantine phenomena in $L(\lambda) = \sum a_k e^{v_k \lambda}$.
- **Next**: Excavate and archive authentic primary sources from Math-Net.Ru and arXiv, then launch Phase 1 Deep Scouting with Codex (`gpt-6.2-astra`, max reasoning).
