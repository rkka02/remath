# CLAUDE.md

Read and follow [AGENTS.md](./AGENTS.md) in full before starting any task in this repository.

## Quick Context Summary
- **Project ReMath** (`rkka02/remath`) is a cumulative **Mathematical Archaeology & AI-Assisted Research Workbench**, paired with the public showcase portal at `https://rkka02.github.io` (`../rkka02.github.io`).
- Every research expedition lives in a self-contained folder under `studies/<NN-slug>/` (see `STUDIES.md` and gold-standard reference `studies/01-leontiev-invisible-loads/STUDY.md`).
- **Role split**: You direct research, curate primary sources, write prose/figures, and verify everything; summon Codex (`gpt-6.2-astra`, `reasoning_effort=max`) via `./scripts/run_astra.sh <study_slug> <task_slug> <prompt_file> [workspace-write|read-only]` for heavy derivations, Lean 4 formalizations, and read-only mathematical refereeing.
- **Editorial rule**: Obey Astra strictly on every genuine mathematical/logical error; exercise flexible, reader-friendly editorial judgment on overly pedantic expository/prose nitpicks.
- **Toolchain**: Use `/opt/homebrew/bin/tectonic` for LaTeX PDFs, `scripts/run_astra.sh` (bundled ChatGPT Codex binary, never Homebrew `codex`), and `scripts/publish_to_portal.py <slug>` to sync finished PDFs & figures to `../rkka02.github.io`.
