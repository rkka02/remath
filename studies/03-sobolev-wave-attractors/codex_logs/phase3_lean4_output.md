**The standalone Lean 4.36.0 project passed the clean build and axiom audit.** The [full theorem inventory](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/docs/phase3_lean4_inventory.md) gives the name, mathematical statement, source line, and exact `#print axioms` output for all **40 main results and 85 supporting lemmas**.

| Module | Main | Supporting | Results |
|---|---:|---:|---|
| `Uncloakability` | 10 | 7 | Sharp half-amplitude bound and equality case, dihedral invariance, exact hexagon return and basin weights |
| `MultiplicityBounds` | 10 | 33 | Cyclic gap pairing, polygonal counting bounds, prescribed multipliers, sharp octagon example |
| `TiltedParity` | 10 | 25 | Four-family parity classification, physical return multipliers, extinction threshold, tilted-square cycles |
| `CornerShavingAndTriangles` | 10 | 20 | Common extrema, contraction and shell energy, single bevel visit per cycle, regular-polygon fractions |

`lake clean && lake build && lake env lean Main.lean` exited **0**, with zero errors, warnings, `sorry`s, project-declared axioms, or external packages. A fresh copy also passed with warnings treated as errors. `leanchecker` replayed all five modules. The only reported axioms were `propext`, `Classical.choice`, and `Quot.sound`. [Audit entry point](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/proofs/lean4/Main.lean)

One correction to the prompt matters mathematically. In the tilted square, \(b\) **exchanges** \(1/3\) and \(7/3\). Its second iterate fixes both with multiplier \(1/16\). The other period-two orbit, \(4/3\leftrightarrow10/3\), has second-return multiplier \(16\). The general four-family theorem states the finite affine and regularity hypotheses under which it constructs an attracting orbit. [Tilted-square classification](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/proofs/lean4/TiltedParity.lean:1058) · [Four-family theorem](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/proofs/lean4/TiltedParity.lean:862)

I updated the [study research log](/Users/mw/Desktop/math/remath/studies/03-sobolev-wave-attractors/docs/RESEARCH_LOG.md). The repository-wide `STUDIES.md` was outside the writable workspace.