The standalone Lean 4.36.0 suite passed the clean build with **0 errors, 0 warnings, 0 `sorry`, and 0 custom axioms**. It contains **117 public theorems and 60 private lemmas**, for 177 declared theorems. All files are under `proofs/lean4/`, and the package has no external dependencies.

| Module | Public theorems | Verified results |
|---|---:|---|
| [ArchitectureHierarchy.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/ArchitectureHierarchy.lean) | 12 | Both factorizations, strict hierarchy, synchronized boundary, Krylov reduction, and rational witnesses |
| [EscapeGeometry.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/EscapeGeometry.lean) | 25 | Unique drift alignment, positive curvature, interface inequalities, exact flip thresholds and barrier, public-good cutoff, and the exact \((1,1)\) to \((2,1)\) stationary memory-upgrade witness |
| [FairGameCancellation.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/FairGameCancellation.lean) | 17 | Finite Green identities, three-way cancellation under its stated hypotheses, and both depth-one transition matrices and stationary laws |
| [StagHuntMirage.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/StagHuntMirage.lean) | 23 | Reference flux, ladder cancellation, critical curve, unique four-state stationary distribution, and all three corner bounds. At \((47/50,4/5,1/2)\), \(\pi_1(CC)=1300/3517\). |
| [CommonFundCutoff.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/CommonFundCutoff.lean) | 40 | Quota balance, both ratio monotonicities, the exact \(n_c=2\) cutoff, exclusion of every productive fixed point below or at Nash, and a uniform depth-two stationary welfare gap of at least \(3027/1600000\) |
| [Main.lean](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/Main.lean) | 0 | Individual `#print axioms` audits and a build-time axiom check covering private and compiler-generated proofs |

**Source corrections verified in Lean**

- At \(M=N=1\), the transition matrices give \((d_L,b_L)=(1/4,1/3)\) and \((d_B,b_B)=(1/16,1/7)\). The cancellation applies to the leading coefficients. For distinct finite corners, the revisit factor is \(V=G_{cc}-G_{oc}^2/G_{oo}\).
- The feasible depth-two share satisfies \(25A_2^2-110A_2+73=0\) and \(43/60<814/1000<A_2<815/1000\). The proposed expression \(5A_2^2-22A_2+19\) equals exactly \(22/5\).
- At depth one, \(A_1=0\) can already attain quota welfare. The suite proves strict improvement over private fixed points when \(A_1>0\).
- Hesitation raises \(\Phi_u(z)\), tightening the feasibility condition \(z_D\ge\Phi_u(z_C)\). The interval \((27/35,81/97)\) describes the aspect-three asymptotic selection thresholds. The finite \((240,80)\) stationary probabilities are a separate calculation in the [escape showcase](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/docs/phase2b_escape_showcase.md).

**Clean verification**

```text
lake clean                 exit 0
lake build                 exit 0 · 14 jobs completed
lake env lean Main.lean    exit 0 · 117/117 public theorems audited
```

Of the 117 public theorems, 115 use `propext`, `Classical.choice`, and `Quot.sound`. Two use `propext` alone. The additional check passed for all 911 theorem constants in the five proof modules. [Full verification transcript](/Users/mw/Desktop/math/remath/studies/02-tsetlin-collective-automata/proofs/lean4/.lake/phase3-verification.log)