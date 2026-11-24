# Final Read-Only Pre-Pitch Sign-Off Round 2 (`phase2_signoff_r2`) — Study #03

You are performing a focused, independent **`read-only`** sign-off check on `/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors` confirming that **100% of the remaining items in `codex_logs/phase2_signoff_output.md`** are now closed with zero remaining blockers!

Use `PYTHONDONTWRITEBYTECODE=1` and do NOT modify any files.

## Focused Verification Items
1. **Major 2 (`phase1_canonical.py`, `phase1_pde.py`)**: Confirm `ChessMap.forward(0.1)` rejects binary floats with `TypeError`, and `reflect(np.array([0,1,2,1], dtype=np.int64), Fraction(1,3))` returns `Fraction(11, 3)`.
2. **Major 3 (`phase1_regular.py`)**: Confirm `half_period_cells` rejects BOTH wide enclosures (`[4.99°, 5.01°]`) AND tiny positive uncertainty (`5° ± 10^{-68}°` at 75 dps) with `InsufficientResolution`, while resolving exact `degree_interval(Fraction(1, 10**40))` at 75 dps (`1` cell, width `2e-40°`, `0` unresolved) and working-precision `iv.pi/36`.
3. **Major 4 (`sources/PRIMARY_SOURCES.md:25`)**: Confirm Zelenyak (1965) attributes the integral subspace to his 1961–1962 papers (refs. 7–8) and near-disk non-almost-periodic domains to Aleksandryan's 1949 dissertation (ref. 3).
4. **Other 1–2 (`phase1_multiple.py`, `phase1_measure.py`)**: Confirm `affine_edges` on `np.int64` coordinates at `n = 10**10` recovers `Fraction(10**10, 10**10 + 1)`, and `strip_coordinate(-2**319 - 1, mp.mpf(2), mp.mpf(3))` at 95 dps rounds identically to the exact value.
5. **Preview script (`experiments/generate_phase2_previews.py`)**:
   - Confirm pentagon branches are strictly verified by edge-contact inequalities `0 < f < 1` and stop cleanly before the `5.9872°` characteristic alignment (plotting `0°` to `5.5°`).
   - Confirm `certified_shaving_measure` uses exact `Fraction` predicates (giving `24` pairs at `0.0767859605911377`? Wait: check `Fraction(eps)`!), the Panel A title says `\geq 17.805\%` (strictly below `17.8057726...%`), and Panel B distinguishes regular periodic attractors (`\cos\phi - \sin\phi`) from total capture (`= 1` with corner capture).
6. Run `PYTHONDONTWRITEBYTECODE=1 python3 experiments/test_phase1_repairs.py` and `PYTHONDONTWRITEBYTECODE=1 python3 experiments/phase1_probe.py`.

## Required Output
Concise sign-off table + explicit verdict **`CLEAN — READY TO PITCH`** (if 0 open defects remain) or list any remaining blocker.
