# Phase 2 Repair Round 2 — Closing 100% of Every Remaining Item in `phase2_verify_output.md`

Read `codex_logs/phase2_verify_output.md` carefully. Every single item listed there must be fixed cleanly so that a subsequent read-only audit gives **`CLEAN — READY TO PITCH`** with **ZERO** open blockers!

## Exact Fix List

### Two Certification Blockers
1. **Explicit input uncertainty for non-exact certification (`experiments/phase1_probe.py`)**:
   - In `chess(...)`, `certify_rotation(...)`, and `one_lap_lift(...)`:
     - NEVER silently infer a tiny input error radius from current `mp.dps` when handed a pre-computed `mpf` (which may have been created at 15 digits like `s = mp.tan(mp.pi/4)` at 15 dps!).
     - Require an explicit `input_radius` (or `mp.iv.mpf` interval / exact `Fraction` / exact symbolic angle constructor computed at working precision) for rigorous certification! If `chess(verts, s)` receives a bare `mpf` without an explicit `input_radius`, either require `input_radius` explicitly in `certify_rotation` (defaulting to raising `ValueError` or returning `unresolved` when uncertified bare floats/mpfs are passed without an enclosure) OR accept `mp.iv` intervals / `Fraction` / `(value, input_radius)` pairs! Make sure our scan (`--scan`) constructs rigorous `mp.iv` enclosures of $\tan(\theta)$ at working precision and passes the genuine enclosure radius!
     - Also fix `one_lap_lift` seam comparison (line 154): compare lifts modulo the integer period without letting a seam wrap around `0` vs `1 - \epsilon` mask a perturbation!
     - Also fix `rational_degrees` (line 270): NEVER convert a binary64 trigonometric slope into a `Fraction` with zero uncertainty — keep it as a genuine interval/mpf with tracked radius or exact rational only for exact rational slopes!
2. **Convexity hypothesis for the finite-$q$ itinerary test (`docs/phase1_scouting.md`, line 204)**:
   - Change "Exact finite-$q$ test for any polygon" $\to$ "Exact finite-$q$ test for any **convex** polygon" (and explicitly note that for nonconvex polygons a first-hit / interior-visibility check along every chord is additionally required, since a reflex notch can intercept an otherwise valid chord).

### All Remaining Partial Minor Items & Additional Reproducible Defects
3. **`docs/phase1_canonical.md` (lines 106, 120)**: Explicitly state the reduced tilt range $0 < \phi < \pi/4$ before the extinction condition and before the $\cos\phi - \sin\phi$ measure formula (matching `phase1_scouting.md`).
4. **`docs/phase1_scouting.md` (line 64 & line 44 & prior-work table)**:
   - Line 64: Add the **even-denominator** qualifier when stating that an interior rational label selects an open tongue (odd-denominator labels occur at a single angle!).
   - Line 44: Note explicitly that a regular section orbit can equal its own reversal (in which case its points occur in pairs contributing equally to the two semicircles, as proved in `phase1_parity.md` line 44), while **distinct** orbits interlace!
   - Prior-work table: Explicitly state Nogueira–Troubetzkoy Theorem 13 gives an open dense subset **for the square**.
5. **`docs/phase1_coexistence.md` (line 5) & `docs/phase1_central_bounds.md` (line 43)**:
   - Replace "rational hexagon" / "rational octagon" with **"hexagon with rational vertices"** / **"octagon with rational vertices"** (and check for any other stray "rational polygon/hexagon/octagon" across `docs/phase1_*.md`!).
6. **`docs/phase1_parity.md` (line 131)**:
   - Replace "low-order resonance curves" with "two explicit unbounded winding families" (or "selected exact winding families") for Bajars–Frank–Maas §2.4.
7. **`experiments/phase1_regular.py` (lines 78 & 128)**:
   - Fix `--resonance 4 2 1e-8` crash (`AssertionError` in grid check when $N=4, k=2$!).
   - Fix the fixed bisection limit (line 128): scale bisection tolerance / step count dynamically to the active `mp.dps` (and/or tilt scale) so tiny tilts like `8 4 1e-40` do not stop at `~3e-16`!
8. **Exact-input helpers (`phase1_rectangle.py`, `phase1_pde.py`, `phase1_parity.py`)**:
   - `experiments/phase1_rectangle.py` (line 54 & line 98): Convert integer inputs in `boundary_map(a, b)` to `Fraction` so `boundary_map(2, 1)` certifies period 3 cleanly; in `primary_low_intervals`, convert `aspect` and `m` to `mp.mpf` (NEVER binary64 `aspect/m`!) before dividing so `R=1, phi=1e-25` works at full working precision!
   - `experiments/phase1_pde.py` (line 24): Convert integer vertex coordinates / projection levels in `reflect` to `Fraction` so large integers like `n = 10**20` never cast through binary64 `float`!
   - `experiments/phase1_parity.py` (line 30): Replace `math.floor` with precision-preserving `mp.floor` / exact `//` in `normal_return` so `normal_return(1 - 1e-20, 1, 2)` at 95 digits returns `1 - d/2`!

## Regression Tests & Verification
- Add regression tests in `experiments/test_phase1_repairs.py` covering EVERY SINGLE ONE of these 8 items (including 15-digit `s = mp.tan(mp.pi/4)` tested at 72 dps, `boundary_map(2, 1)`, `reflect` at `n=10**20`, `normal_return(1-1e-20, 1, 2)` at 95 dps, `primary_low_intervals` at `R=1, phi=1e-25`, `--resonance 4 2 1e-8`, and `8 4 1e-40` bisection!).
- Run `python3 experiments/test_phase1_repairs.py` and `python3 experiments/phase1_probe.py --scan` and verify 0 errors!
