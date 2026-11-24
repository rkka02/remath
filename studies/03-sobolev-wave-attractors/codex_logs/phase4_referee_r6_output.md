## 1. REMAINING OR NEW BLOCKING DEFECTS

**REVISION REQUIRED.** All four named Round 5 replays pass. Five fresh numerical defects block sign-off. The strip examples use 95 decimal digits, with \(P=\texttt{strip_position}\) and \(T=\texttt{strip_coordinate}\).

1. **`half_period_cells` can certify a false square tongue.** At 75 digits, `half_period_cells(4, mp.e)` puts the caller-representable angle \(\theta=2^{-253}\lfloor 2^{253}(\pi-e)\rfloor\) inside. The exact lower edge is \(\pi-e>\theta\). A 450-digit interval chord-map replay returned `False`. The phase conversion freezes the lazy constant at its current binary approximation. [Phase conversion](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_regular.py:262)

2. **`mp.eps` changes value during refinement.** `P(mp.eps, 1, 1)` returns `1`. Unit slopes give the exactly representable \(1+2^{-318}\). A 15-digit clone also exposes a failure at zero. `P(-Fraction(1, 2**52), c.eps, c.eps)` raises `ValueError` although its exact exit is zero. [Callable detection](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:21) · [Epsilon evaluation](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:103)

3. **An exact rational can become an incorrect singleton enclosure.** Let `s = Fraction(1, 3)` and use `mpq` from `mpmath.rational`. `P(mpq(-1, 3), s, s)` returns \(6.8042717532826061\times10^{-203}\). Equal slopes give exactly \(-1/3+1/3=0\). The fallback rounds the input and uses that approximation as both bounds. [Scalar fallback](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:109)

4. **The callable error bound can miss a full unit.** For `f = lambda: (mp.mpf(2)**1000 + 1) - mp.mpf(2)**1000`, `P(f, 1, 1)` returns `1`. The expression represents one, so the exit is two. Cancellation loses the unit before the four-epsilon padding is applied. [Callable enclosure](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:106)

5. **Both strip helpers can reject a singleton before refining it.** Set \(q=2^{-800}\lfloor2^{800}\log 2\rfloor\), \(s=1+2^{-319}-q\), and \(t=1/2+2^{-320}\). Both `P(mp.ln2, s, s)` and `T(mp.ln2, q-t, t)` raise `ValueError`. Independent 1,500-bit enclosures round uniquely to \(1+2^{-318}\) and \(1/2+2^{-319}\), respectively. Both early exits treat the refinable bounds on `mp.ln2` as fixed input uncertainty. [Position rejection](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:232) · [Coordinate rejection](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/experiments/phase1_measure.py:281)

## 2. FINAL SIGN-OFF SUMMARY

| Audit item | Verified result |
|---|---|
| Round 5 square replays | All three exact-phase probes and both interval-phase probes lie in the returned uncertainty bands. Both cells meet their slivers exactly. At each interval-phase probe, the 450-digit chord map returned `False` at the lower phase and `True` at the upper phase. |
| Round 5 strip replays | The halfway tie and zero exit are exact. All 13 cloned constants gave 0 ULP error in both helpers. The narrow interval returned \(1/8\) and \(5/4\). Wide ambiguous intervals raised `ValueError`. |
| Fresh controls | All 880 rational strip outputs and 600 interval decisions agreed with independent fraction arithmetic. The quarter-turn formula agreed on all 57 resolved polygon cases. Another 12 reported insufficient resolution. |
| Unit tests and CLIs | **51/51 passed.** Both CLIs exited successfully, and `--tongues` printed all nine polygon rows. The measure CLI’s current maximum discrepancy is \(2.2472\times10^{-95}\) at \((\phi,\theta,R,y)=(17^\circ,61^\circ,0.28,0.057)\), above the chapter’s recorded \(1.5\times10^{-95}\). [Verification note](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/docs/phase1_measure.md:197) |
| Publications and Lean | Round 4 acceptance stands for all three manuscripts (19, 20, and 8 pages), all 10 embedded figures, and Lean 4.36.0 with 125 public theorems, including 40 principal results, and zero `sorry`. [Round 4 report](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/codex_logs/phase4_referee_r4_output.md) |