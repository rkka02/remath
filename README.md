# ReMath: Excavating A. F. Leont'ev's *Series of Exponentials* (*Ряды экспонент*)

> **Mathematical Archaeology Project** — Reviving the forgotten Soviet Ufa/Moscow theory of A. F. Leont'ev (1917–1987) on representing analytic functions on convex domains by non-orthogonal exponential series $\sum c_n e^{\lambda_n z}$, and connecting it to modern mathematics, computation, and PDEs.

## Research Architecture
- **Research Direction, Archaeology, Verification & Narrative**: Antigravity (Gemini)
- **Mathematical Computation, Derivation & Proof Subcontractor**: Codex CLI (`gpt-6.2-astra`, `reasoning_effort=max`)

## Directory Layout
- `sources/` — Primary Russian/English bibliography, archived open-access papers/abstracts from Math-Net.Ru and arXiv, and structured translations/summaries of Leont'ev's foundational theorems.
- `docs/` — Research journal (`RESEARCH_LOG.md`), accessible non-specialist exposition, and full mathematical writeup.
- `codex_logs/` — Full reproducible prompts and outputs from Codex (`gpt-6.2-astra`, max reasoning).
- `experiments/` — Reproducible Python (`numpy`, `scipy`, `mpmath`, `sympy`, `matplotlib`) simulations and numerical stress tests.
- `figures/` — High-resolution visual figures generated from experiments.
- `proofs/` — Rigorous mathematical proofs, symbolic checks, and formal verification scripts.
- `scripts/` — Automation wrappers (including `run_astra.sh` for invoking Codex `gpt-6.2-astra` at `max` reasoning effort).

*(Living document — updated continuously via Git as discoveries accumulate.)*
