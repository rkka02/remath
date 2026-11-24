# Study 03 · Lean 4.36.0 theorem inventory

The clean build passed with zero errors, warnings, proof placeholders or project-declared axioms. The four modules contain 40 main results and 85 supporting public lemmas. Lean printed the transitive axiom dependencies of all 125. The package manifest lists zero external packages. [Lake manifest](../proofs/lean4/lake-manifest.json) · [Audit entry point](../proofs/lean4/Main.lean)

| Module | Main results | Supporting results | Total audited |
|---|---:|---:|---:|
| [Uncloakability.lean](../proofs/lean4/Uncloakability.lean) | 10 | 7 | 17 |
| [MultiplicityBounds.lean](../proofs/lean4/MultiplicityBounds.lean) | 10 | 33 | 43 |
| [TiltedParity.lean](../proofs/lean4/TiltedParity.lean) | 10 | 25 | 35 |
| [CornerShavingAndTriangles.lean](../proofs/lean4/CornerShavingAndTriangles.lean) | 10 | 20 | 30 |
| **Total** | **40** | **85** | **125** |

## Verification

Run the following from `proofs/lean4/`.

```sh
lake clean && lake build && lake env lean Main.lean
```

The command exited 0 on Lean 4.36.0, commit `611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9`. A second build from a fresh directory contained only the five Lean sources, toolchain pin, Lake file and manifest. All five source files also passed individually with `-DwarningAsError=true`. Lean’s `leanchecker` replayed the declarations in all five compiled modules. The existing Python programs independently reproduced the exact hexagon and tilted-square orbits. [Coexistence calculation](../experiments/phase1_coexistence.py) · [Boundary calculation](../experiments/phase1_pde.py)

Of the 125 kernel reports, 120 list `[propext, Classical.choice, Quot.sound]`, 4 list `[propext, Quot.sound]`, and 1 has only `[Quot.sound]`. The final section reproduces the output for every name.

## Uncloakability

The detector level $c$ may be any rational number, including values outside the boundary range. In the trace lemma each involution preserves its own characteristic coordinate. The hexagon results derive the return from wall intersections and use an explicit continuous piecewise-linear profile. The absolute mode reaches its circuit maximum of 1 at $s=1/16$ on the top horizontal leg. [Detector argument](phase1_scouting.md) · [Hexagon and launch intervals](phase1_coexistence.md)

### Main results

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `sharpHalfAmplitude` | For $m\le M$ and any $c$, the larger distance from $c$ to the endpoints is at least $(M-m)/2$, with equality exactly at $c=(m+M)/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 14](../proofs/lean4/Uncloakability.lean#L14) |
| `finiteSharpHalfAmplitude` | For any nonempty rational list and any $c$, the largest absolute deviation from $c$ is at least half the list’s range. Equality holds exactly at its midrange, including constant lists. | `[propext, Classical.choice, Quot.sound]` | [Line 22](../proofs/lean4/Uncloakability.lean#L22) |
| `dihedralTimeReversal` | For two involutions, $g_-g_+$ is both a left and right inverse of $b=g_+g_-$. Conjugating $b$ by either involution gives that inverse. | `[propext, Quot.sound]` | [Line 45](../proofs/lean4/Uncloakability.lean#L45) |
| `dihedralIterates` | For either chord involution $g$ and every natural $q$, $g b^q=(g_-g_+)^q g$. These forward and backward iterates are two-sided inverses. | `[propext, Quot.sound]` | [Line 86](../proofs/lean4/Uncloakability.lean#L86) |
| `zeroTraceInvariance` | If each chord preserves its characteristic coordinate and $A\circ\xi=B\circ\eta$ on the boundary, the common profile is invariant under each chord and their composition. | `[Quot.sound]` | [Line 106](../proofs/lean4/Uncloakability.lean#L106) |
| `hexagonZeroTrace` | If $h$ vanishes on $[0,3/4]$, then $h(1-\lvert s\rvert)-h(\lvert t\rvert)=0$ on both boundary graphs, covering all six faces. | `[propext, Classical.choice, Quot.sound]` | [Line 140](../proofs/lean4/Uncloakability.lean#L140) |
| `hexagonFixedPointAndContraction` | The only local fixed height is $1/4$. For every local return, $z-1/4=(y-1/4)/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 200](../proofs/lean4/Uncloakability.lean#L200) |
| `sharpGlobalAmplitude` | The absolute mode is bounded by 2 everywhere and attains 2 at the interior point $(1/16,13/16)$. | `[propext, Classical.choice, Quot.sound]` | [Line 245](../proofs/lean4/Uncloakability.lean#L245) |
| `sharpCircuitAmplitude` | The absolute mode is bounded by 1 on the entire attracting rectangle and attains 1 at $(1/16,1/4)$ on its top leg. | `[propext, Classical.choice, Quot.sound]` | [Line 258](../proofs/lean4/Uncloakability.lean#L258) |
| `hexagonBasinDynamics` | On the left wall, $(-3/4,1/4)$ converges to $-1/4$ and $(1/4,3/4)$ converges to $3/4$. The outer closed arcs and the repeller are fixed. The right-wall limits are their reflections. | `[propext, Classical.choice, Quot.sound]` | [Line 411](../proofs/lean4/Uncloakability.lean#L411) |

<details><summary>7 supporting results</summary>

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `hexagonWallBounds` | $R(t)\le 1-\lvert t\rvert$ everywhere. Equality holds for $\lvert t\rvert\ge3/4$, and $R(t)\ge1/4$ when $\lvert t\rvert\le3/4$. | `[propext, Classical.choice, Quot.sound]` | [Line 131](../proofs/lean4/Uncloakability.lean#L131) |
| `hexagonLocalReturn` | For $0<y<1/2$, four successive distinct boundary intersections give a return to height parameter $z$ exactly when $z=1/8+y/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 176](../proofs/lean4/Uncloakability.lean#L176) |
| `hexagonPeriodicHeights` | For $0<y<1$, opposite rows match exactly at $y=1/4$ and throughout $[3/4,1)$. | `[propext, Classical.choice, Quot.sound]` | [Line 212](../proofs/lean4/Uncloakability.lean#L212) |
| `sharpProfileData` | At $3/4,13/16,7/8,15/16,1$ the piecewise-linear profile takes $0,1,0,-1,0$. Its full range is contained in $[-1,1]$, and its mode has zero boundary trace. | `[propext, Classical.choice, Quot.sound]` | [Line 226](../proofs/lean4/Uncloakability.lean#L226) |
| `hexagonVerticalFibers` | For $\lvert t\rvert\le1$, the complete vertical fibers through the right and left graphs have height pairs $\{t,-F_L(t)\}$ and $\{t,-t\}$, respectively. | `[propext, Classical.choice, Quot.sound]` | [Line 292](../proofs/lean4/Uncloakability.lean#L292) |
| `hexagonBasinSigns` | The left-wall return advances on $(-3/4,-1/4)$ and $(1/4,3/4)$ and retreats on $(-1/4,1/4)$. Reflecting the height exchanges the two walls and reverses the displacement sign. | `[propext, Classical.choice, Quot.sound]` | [Line 300](../proofs/lean4/Uncloakability.lean#L300) |
| `hexagonBasinWeights` | With uniform height on each of two equally likely launch walls, the normalized lengths of the neutral region, isolated basin and endpoint basin are $1/4,1/2,1/4$, and sum to 1. | `[propext, Classical.choice, Quot.sound]` | [Line 446](../proofs/lean4/Uncloakability.lean#L446) |

</details>

## MultiplicityBounds

The universal counts start from finite cyclic markings, four distinct extrema, and the locations of vertices in the marked gaps. The half-flight argument derives the extra vertex whenever a returning gap has fixed endpoints and a moving interior point. At period two, the four-chain difference is represented by affine pieces sharing endpoint values. The central count starts from positive strip coefficients, their upper envelope on a finite slope window containing the band and selected roots, and an open interval of equal ray maxima. All subtractions in natural-number upper bounds truncate at zero. [Cyclic markings](phase1_multiple.md) · [Four chains and prescribed rates](phase1_coexistence.md) · [Central envelope](phase1_central_bounds.md)

### Main results

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `fixedPointFree_iff_odd` | On $2m$ labels, $i\mapsto h-i$ is fixed-point-free exactly when the representative of $h$ is odd. | `[propext, Classical.choice, Quot.sound]` | [Line 36](../proofs/lean4/MultiplicityBounds.lean#L36) |
| `gap_fixed_labels` | Under the free marked-point reflection, the gap reflection fixes exactly the two distinct labels $(h-1)/2$ and $(h-1)/2+m$. | `[propext, Classical.choice, Quot.sound]` | [Line 67](../proofs/lean4/MultiplicityBounds.lean#L67) |
| `gap_pair_partition` | The remaining gaps form disjoint pairs indexed by $\mathrm{Fin}(m-1)$. The two members are exchanged, and each moved label belongs to exactly one pair. | `[propext, Classical.choice, Quot.sound]` | [Line 98](../proofs/lean4/MultiplicityBounds.lean#L98) |
| `attractor_vertex_bound` | For $m$ attracting and reversed pairs with the stated extremal and gap incidences, $m+3\le k$ and $m\le k-3$. | `[propext, Classical.choice, Quot.sound]` | [Line 207](../proofs/lean4/MultiplicityBounds.lean#L207) |
| `mixed_vertex_bound` | With one additional free pair of neutral orbit labels and the corresponding vertex incidences, $m+4\le k$. | `[propext, Classical.choice, Quot.sound]` | [Line 214](../proofs/lean4/MultiplicityBounds.lean#L214) |
| `four_chain_bound` | If the four-chain displacement uses $P\le k-3$ pieces and has a zero piece, there are at most $\max(0,k-5)$ crossing pieces. A positive count requires $k\ge6$. | `[propext, Classical.choice, Quot.sound]` | [Line 422](../proofs/lean4/MultiplicityBounds.lean#L422) |
| `central_cylinder_bound` | For positive strip coefficients, an open band of $Q_+=Q_-$ and $m$ distinct isolated interior equalities imply $P\le h-1$, $m\le\max(0,h-3)$, and $2h\ge8$ when $m>0$. | `[propext, Classical.choice, Quot.sound]` | [Line 846](../proofs/lean4/MultiplicityBounds.lean#L846) |
| `localWallReturn` | On a pair of local wall faces with the prescribed relative slopes at $r$, the forward return is $y=r+\kappa(x-r)$ and the reversed relation has slope $1/\kappa>1$. | `[propext, Classical.choice, Quot.sound]` | [Line 962](../proofs/lean4/MultiplicityBounds.lean#L962) |
| `prescribedRateWall` | For any finite strictly ordered list of heights below $a<1$ and rates in $(0,1)$, normalization with $M>G_m$ produces a positive inner concave wall, $m+2$ alternating cuts, exactly the prescribed inner roots and rates, and matching exterior faces. | `[propext, Classical.choice, Quot.sound]` | [Line 1458](../proofs/lean4/MultiplicityBounds.lean#L1458) |
| `centralOctagonAttractingRectangle` | The rectangle with half-width $7/12$ and half-height $1/4$ is a four-chord circuit. Its local fixed height is unique, and $z-1/4=(y-1/4)/4$. | `[propext, Classical.choice, Quot.sound]` | [Line 1818](../proofs/lean4/MultiplicityBounds.lean#L1818) |

<details><summary>33 supporting results</summary>

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `reflection_involution` | On a cyclic set of size $n$, applying $i\mapsto h-i$ twice returns $i$. | `[propext, Classical.choice, Quot.sound]` | [Line 23](../proofs/lean4/MultiplicityBounds.lean#L23) |
| `mixed_quadrilateral` | Substituting $k=4$ into the mixed gap count forces $m=0$ for every period covered by the marking. | `[propext, Classical.choice, Quot.sound]` | [Line 219](../proofs/lean4/MultiplicityBounds.lean#L219) |
| `nontrivial_gap_hits_vertex` | If a chain of half-flights fixes both endpoints and moves an interior point, some half-flight meets a vertex, provided vertex-free half-flights are affine on their normalized gap. | `[propext, Classical.choice, Quot.sound]` | [Line 255](../proofs/lean4/MultiplicityBounds.lean#L255) |
| `marked_gap_vertex_bound` | With $2r$ marked classes and a nontrivial return for each conjugate gap pair, the half-flight data imply $r+3\le k$ and $r\le k-3$. | `[propext, Classical.choice, Quot.sound]` | [Line 299](../proofs/lean4/MultiplicityBounds.lean#L299) |
| `affine_zero_unique` | A nonconstant affine interpolant cannot vanish at two different coordinates. | `[propext, Classical.choice, Quot.sound]` | [Line 309](../proofs/lean4/MultiplicityBounds.lean#L309) |
| `affine_two_zeros` | If an affine interpolant vanishes at two distinct coordinates, both endpoint values are zero. | `[propext, Classical.choice, Quot.sound]` | [Line 315](../proofs/lean4/MultiplicityBounds.lean#L315) |
| `affine_interior_root_iff` | A nonconstant affine piece has an interior zero exactly when its endpoint values have opposite strict signs. | `[propext, Classical.choice, Quot.sound]` | [Line 333](../proofs/lean4/MultiplicityBounds.lean#L333) |
| `affine_root_count` | A continuous chain of $P$ affine pieces with a zero piece has at most $\max(0,P-2)$ pieces carrying a strict interior crossing. | `[propext, Classical.choice, Quot.sound]` | [Line 391](../proofs/lean4/MultiplicityBounds.lean#L391) |
| `hexagon_four_chain_witness` | The three-piece displacement with endpoints $[1/8,-1/8,0,0]$ has one crossing at the midpoint of its first piece and a flat last piece. | `[propext, Classical.choice, Quot.sound]` | [Line 432](../proofs/lean4/MultiplicityBounds.lean#L432) |
| `envelope_lines_injective` | Distinct maximal cells of an upper envelope of affine lines have distinct supporting lines. | `[propext, Classical.choice, Quot.sound]` | [Line 521](../proofs/lean4/MultiplicityBounds.lean#L521) |
| `neutral_cell_all_heights` | On a cell carried by a line with both signs, the two signed maxima agree at every point of the closed cell. | `[propext, Classical.choice, Quot.sound]` | [Line 552](../proofs/lean4/MultiplicityBounds.lean#L552) |
| `envelope_pieces_bound` | An active repeated line of opposite signs reduces the number of distinct envelope pieces to $P\le h-1$ for $h$ signed strips. | `[propext, Classical.choice, Quot.sound]` | [Line 558](../proofs/lean4/MultiplicityBounds.lean#L558) |
| `neutral_cell_iff_both_signs` | At an interior point of an envelope cell, two active signs are present exactly when that cell’s line occurs with both signs. | `[propext, Classical.choice, Quot.sound]` | [Line 600](../proofs/lean4/MultiplicityBounds.lean#L600) |
| `envelope_cell_interior_not_isolated` | A two-sign equality in the interior of a maximal affine cell cannot be isolated. | `[propext, Classical.choice, Quot.sound]` | [Line 615](../proofs/lean4/MultiplicityBounds.lean#L615) |
| `envelope_transition_bound` | With a neutral cell, at most $\max(0,P-2)\le\max(0,h-3)$ internal knots carry isolated equalities. A positive count requires $2h\ge8$. | `[propext, Classical.choice, Quot.sound]` | [Line 632](../proofs/lean4/MultiplicityBounds.lean#L632) |
| `isolated_height_is_break` | Every isolated two-sign equality strictly inside the represented slope range occurs at an internal knot counted by the envelope. | `[propext, Classical.choice, Quot.sound]` | [Line 676](../proofs/lean4/MultiplicityBounds.lean#L676) |
| `central_attractor_bound` | For a neutral envelope cell and $m$ distinct isolated interior equalities, $m\le\max(0,h-3)$, and $m>0$ implies $2h\ge8$. | `[propext, Classical.choice, Quot.sound]` | [Line 711](../proofs/lean4/MultiplicityBounds.lean#L711) |
| `rectangle_iff_two_active_signs` | For positive strip coefficients and $t>0$, the two physical ray maxima $Q_+(t),Q_-(t)$ agree exactly when both signs attain the upper envelope. | `[propext, Classical.choice, Quot.sound]` | [Line 766](../proofs/lean4/MultiplicityBounds.lean#L766) |
| `neutral_interval_has_repeated_line` | An open interval of two-sign equality meets the interior of a cell whose active line occurs with both signs. | `[propext, Classical.choice, Quot.sound]` | [Line 832](../proofs/lean4/MultiplicityBounds.lean#L832) |
| `signedWallCut_concave` | Subtracting a nonnegative multiple of a one-sided linear hinge preserves Jensen concavity of the right wall. | `[propext, Classical.choice, Quot.sound]` | [Line 894](../proofs/lean4/MultiplicityBounds.lean#L894) |
| `prescribedRateGrowth` | For $G>0$ and $0<\kappa<1$, $G/\kappa>G$ and $G/(G/\kappa)=\kappa$. | `[propext, Classical.choice, Quot.sound]` | [Line 906](../proofs/lean4/MultiplicityBounds.lean#L906) |
| `prescribedSlopeCrossing` | For $r<s$ and opposite slopes $d,-e$ with $d,e>0$, the two lines through the prescribed roots meet at $(dr+es)/(d+e)$ strictly between $r$ and $s$. | `[propext, Classical.choice, Quot.sound]` | [Line 923](../proofs/lean4/MultiplicityBounds.lean#L923) |
| `SlopeFront.advance_geometry` | The next cut lies strictly between the old and new root, switches sides, changes the leading slope to $-G$, and increases magnitude to $G/\kappa$. The ratio is exactly $\kappa$. | `[propext, Classical.choice, Quot.sound]` | [Line 1102](../proofs/lean4/MultiplicityBounds.lean#L1102) |
| `SlopeFront.displacement_on_tail` | Beyond the current cut, the signed difference $W(y)-W(-y)$ equals its outward slope times $y-r$. | `[propext, Classical.choice, Quot.sound]` | [Line 1115](../proofs/lean4/MultiplicityBounds.lean#L1115) |
| `SlopeFront.alternatingDisplacements` | Consecutive signed displacement lines meet at the prescribed cut and have opposite signs of slope. The new slope has magnitude $G/\kappa-G$. | `[propext, Classical.choice, Quot.sound]` | [Line 1122](../proofs/lean4/MultiplicityBounds.lean#L1122) |
| `SlopeFront.advance_localRate` | Advancing one step constructs two actual affine faces around the new prescribed root with the requested contraction ratio. | `[propext, Classical.choice, Quot.sound]` | [Line 1143](../proofs/lean4/MultiplicityBounds.lean#L1143) |
| `centralOctagonSymmetry` | Central inversion preserves both membership in the octagon and membership in its boundary. | `[propext, Classical.choice, Quot.sound]` | [Line 1512](../proofs/lean4/MultiplicityBounds.lean#L1512) |
| `centralOctagonFaceRanges` | All eight affine face equations have explicit active ranges. On the right the joins occur at $-1/2,1/12,3/4$. On the left they occur at the reflected heights. | `[propext, Classical.choice, Quot.sound]` | [Line 1520](../proofs/lean4/MultiplicityBounds.lean#L1520) |
| `centralOctagonEightDistinctVertices` | The ordered list of eight wall junctions has length eight, has no duplicates, and agrees with the listed rational coordinates. | `[propext, Classical.choice, Quot.sound]` | [Line 1545](../proofs/lean4/MultiplicityBounds.lean#L1545) |
| `centralOctagonStrips` | The octagon region equals the intersection of four explicit pairs of parallel supporting half-planes. | `[propext, Classical.choice, Quot.sound]` | [Line 1554](../proofs/lean4/MultiplicityBounds.lean#L1554) |
| `centralOctagonExtremeIffVertex` | The geometric extreme points, tested by midpoints of rational segments, are exactly the eight listed vertices. | `[propext, Classical.choice, Quot.sound]` | [Line 1632](../proofs/lean4/MultiplicityBounds.lean#L1632) |
| `centralOctagonNeutralCylinder` | For every $3/4<y<1$, the four boundary chords form the rectangle with horizontal coordinates $\pm(1-y)$ and vertical coordinates $\pm y$. The four-chord return fixes $y$ uniquely. | `[propext, Classical.choice, Quot.sound]` | [Line 1775](../proofs/lean4/MultiplicityBounds.lean#L1775) |
| `centralOctagonLocalReturn` | On $0<y<1/2$ the four-chord return is exactly $z=3/16+y/4$. | `[propext, Classical.choice, Quot.sound]` | [Line 1805](../proofs/lean4/MultiplicityBounds.lean#L1805) |

</details>

## TiltedParity

Write $p=n$, $q=m+n$ for the clockwise boundary label. The general return theorem takes a normalized degree-one rational lift, its finite affine branches, a fixed point recording attained rational winding, and the interlacing or reflection data at that point and the other fixed points. These data determine global identity. The regular-attractor equivalence also uses a fixed sample strictly inside an affine cell and finite subdivisions on which any fixed break has slopes on opposite sides of 1. The proof constructs an attracting point and gives the full physical return on its cell. In the rational tilted square, the explicit square chord maps give the geometric example directly. The points $1/3$ and $7/3$ are exchanged by $b$ and fixed by $b^2$. [Canonical sections](phase1_canonical.md) · [Itinerary parity](phase1_parity.md) · [Square counterexample](phase1_pde.md)

| Tank | Even section denominator and global boundary label | Factor at a regular attractor |
|---|---|---|
| Right trapezoid | $q-p$ even | $\Lambda^{-1}$ |
| Isosceles trapezoid | $p$ odd | $\Lambda^{-2}$ |
| Sheared parallelogram | $q$ odd | $\Lambda^{-2}$ |
| Tilted rectangle | $q$ odd | $\mu^{-2}$ |

The right trapezoid uses one model lap. Each of the other three uses two laps at odd section denominator and one at even section denominator.

### Main results

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `even_boundary_winding` | For coprime $m,n$, even $q=m+n$, both windings odd, gcd equal to 2, and $D=m$ odd are equivalent. | `[propext, Classical.choice, Quot.sound]` | [Line 58](../proofs/lean4/TiltedParity.lean#L58) |
| `odd_boundary_winding` | For coprime $m,n$, odd $q=m+n$, opposite winding parities, gcd equal to 1, and $D=2m$ even are equivalent. | `[propext, Classical.choice, Quot.sound]` | [Line 68](../proofs/lean4/TiltedParity.lean#L68) |
| `canonical_parity_table` | For coprime winding $n/m$, the even-section criterion is $q-p$ even in the right trapezoid, $p$ odd in the isosceles trapezoid, and $q$ odd in the shear and tilted rectangle. It covers one section lap for the right trapezoid or an even section denominator, and two laps otherwise. | `[propext, Classical.choice, Quot.sound]` | [Line 111](../proofs/lean4/TiltedParity.lean#L111) |
| `even_balanced_multiplier` | If $A+B=D$ is even and the counts differ by at most one, then $A=B$, the exponent is zero and the product is 1. | `[propext, Classical.choice, Quot.sound]` | [Line 167](../proofs/lean4/TiltedParity.lean#L167) |
| `odd_balanced_multiplier` | If $A+B=D$ is odd and the counts differ by at most one, the signed exponent is $+1$ or $-1$. One lap has factor $\mu$ or $\mu^{-1}$, and two laps square that factor. | `[propext, Classical.choice, Quot.sound]` | [Line 175](../proofs/lean4/TiltedParity.lean#L175) |
| `canonical_physical_identity_iff` | For the same return with a nondecreasing lift, the family’s boundary parity is equivalent to identity of the physical wall return after its actual number of section laps. | `[propext, Classical.choice, Quot.sound]` | [Line 607](../proofs/lean4/TiltedParity.lean#L607) |
| `canonical_regular_interior_iff` | For a canonical return with finite charts, balanced fixed itineraries, tangential fixed knots and a regular fixed sample, the complementary boundary parity is equivalent to a regular attracting fixed point. Its full physical return is affine near that point with factor $\mu^{-1}$ in the right trapezoid and $\mu^{-2}$ in the other three families. | `[propext, Classical.choice, Quot.sound]` | [Line 862](../proofs/lean4/TiltedParity.lean#L862) |
| `extinction_interval` | For positive $t,R$ in a linearly ordered field, $1/t\le R\le t$ is equivalent to $R\le t$ and $1/R\le t$. | `[propext, Classical.choice, Quot.sound]` | [Line 907](../proofs/lean4/TiltedParity.lean#L907) |
| `extinction_threshold` | An admissible positive aspect ratio exists exactly for $t\ge1$. At $R=1$ the extinction interval holds exactly under this same inequality. | `[propext, Classical.choice, Quot.sound]` | [Line 913](../proofs/lean4/TiltedParity.lean#L913) |
| `square_period_two_iff` | For every valid square boundary point, $b^2(p)=p$ in Cartesian position exactly at perimeter coordinates $1/3,4/3,7/3,10/3$. | `[propext, Classical.choice, Quot.sound]` | [Line 1058](../proofs/lean4/TiltedParity.lean#L1058) |

<details><summary>25 supporting results</summary>

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `reduced_winding_fraction` | Dividing $m+n$ and $2m$ by their gcd gives coprime $P,D$ with $D>0$ and $P(2m)=(m+n)D$ when $m>0$. | `[propext, Quot.sound]` | [Line 14](../proofs/lean4/TiltedParity.lean#L14) |
| `word_product_formula` | The product of the actual reciprocal branch factors in a finite word is $\mu^{A-B}$ for $\mu\ne0$, where $A,B$ count its two branch types. | `[propext, Classical.choice, Quot.sound]` | [Line 136](../proofs/lean4/TiltedParity.lean#L136) |
| `word_product_cover` | Repeating a word for $d$ laps raises its factor product to the $d$th power. | `[propext, Classical.choice, Quot.sound]` | [Line 154](../proofs/lean4/TiltedParity.lean#L154) |
| `canonical_attracting_multiplier` | With $\mu>1$ and balanced visits, a section factor below 1 selects the non-global row and gives a physical factor $\mu^{-1}$ in the right trapezoid and $\mu^{-2}$ in the other three families. | `[propext, Classical.choice, Quot.sound]` | [Line 191](../proofs/lean4/TiltedParity.lean#L191) |
| `canonical_physical_word` | For a regular attracting itinerary of the section period with balanced visits, the product along the full repeated physical word is $\mu^{-1}$ for the right trapezoid and $\mu^{-2}$ for the other three. | `[propext, Classical.choice, Quot.sound]` | [Line 219](../proofs/lean4/TiltedParity.lean#L219) |
| `even_section_mesh_identity` | On a finite closed interval partition, an even return with one fixed point and balanced visits on the incident branches at every fixed point fixes the entire interval. | `[propext, Classical.choice, Quot.sound]` | [Line 296](../proofs/lean4/TiltedParity.lean#L296) |
| `odd_section_mesh_no_fixed_interval` | A finite affine section with odd branch itinerary length and $\mu>1$ has no fixed subinterval of positive length. | `[propext, Classical.choice, Quot.sound]` | [Line 367](../proofs/lean4/TiltedParity.lean#L367) |
| `even_reduced_section_lift_identity` | For a degree-one reduced lift, the even fixed-branch criterion on a unit interval and a single fixed point imply $F(x)=x$ for every rational $x$. | `[propext, Classical.choice, Quot.sound]` | [Line 431](../proofs/lean4/TiltedParity.lean#L431) |
| `odd_reduced_section_lift_no_fixed_interval` | For an odd section and $\mu>1$, no positive-length interval is fixed anywhere on the degree-one lift, including intervals crossing a period cut. | `[propext, Classical.choice, Quot.sound]` | [Line 448](../proofs/lean4/TiltedParity.lean#L448) |
| `one_reflected_point_per_gap` | A labeling of a second orbit that commutes with cyclic advancement and sends label 0 to gap 0 puts exactly one point in every gap. | `[propext, Quot.sound]` | [Line 479](../proofs/lean4/TiltedParity.lean#L479) |
| `interlaced_arc_discrepancy` | On any consecutive arc of the cyclic ordering of two interlaced orbits, the numbers of points of each type differ by at most one. | `[propext, Classical.choice, Quot.sound]` | [Line 534](../proofs/lean4/TiltedParity.lean#L534) |
| `fixed_germ_discrepancy` | Disjoint interlacing or reflection-invariant pairs with the permitted seam points give a visit-count discrepancy of at most one. | `[propext, Classical.choice, Quot.sound]` | [Line 554](../proofs/lean4/TiltedParity.lean#L554) |
| `even_reduced_section_lift_from_orbits` | At even section period, fixed-point orbit data on each incident affine branch and one fixed point force identity on the entire degree-one lift. | `[propext, Classical.choice, Quot.sound]` | [Line 564](../proofs/lean4/TiltedParity.lean#L564) |
| `canonical_global_identity_iff` | For a four-family normalized return carrying the finite affine section and orbit data, the family’s global boundary parity is equivalent to pointwise identity of the reduced return. | `[propext, Classical.choice, Quot.sound]` | [Line 588](../proofs/lean4/TiltedParity.lean#L588) |
| `regular_sink_of_crossing` | On a finite affine mesh with positive branch slopes, $F(a)>a$ and $F(b)<b$ yield a fixed point strictly inside a contracting cell whenever each fixed internal knot has one slope above and one below 1. | `[propext, Classical.choice, Quot.sound]` | [Line 733](../proofs/lean4/TiltedParity.lean#L733) |
| `attracting_cell_iteration` | If $F(y)-x=s(y-x)$ on a closed interval containing $x$ with $0\le s\le1$, then every iterate stays in that interval and $F^k(y)-x=s^k(y-x)$. | `[propext, Classical.choice, Quot.sound]` | [Line 740](../proofs/lean4/TiltedParity.lean#L740) |
| `canonical_tongue_interior_sink` | In the four-family section with balanced fixed itineraries and tangential fixed knots, a downward crossing gives an interior fixed point with $B=A+1$. Its actual physical affine return has factor $\mu^{-1}$ for the right trapezoid and $\mu^{-2}$ for the other three families. | `[propext, Classical.choice, Quot.sound]` | [Line 769](../proofs/lean4/TiltedParity.lean#L769) |
| `regular_odd_fixed_has_crossing` | In a degree-one lift with odd section period and balanced fixed itineraries, any fixed point in an affine cell’s interior gives $l<r$ with $F(l)>l$ and $F(r)<r$, even if the sampled point repels. | `[propext, Classical.choice, Quot.sound]` | [Line 821](../proofs/lean4/TiltedParity.lean#L821) |
| `square_half_angle_threshold` | For $0<z<1$, $2z/(1-z^2)\ge1$ exactly when $(1+z)^2\ge2$, giving the square threshold in $z=\tan\phi$. | `[propext, Classical.choice, Quot.sound]` | [Line 929](../proofs/lean4/TiltedParity.lean#L929) |
| `square_algebraic_endpoint` | If $r>0$ and $r^2=2$, then $z=r-1$ lies in $(0,1)$ and $2z/(1-z^2)=1$, including equality at the square threshold. | `[propext, Classical.choice, Quot.sound]` | [Line 943](../proofs/lean4/TiltedParity.lean#L943) |
| `square_extinction_angle_iff` | In an ordered field containing a positive $r$ with $r^2=2$, the square extinction inequalities hold exactly for $z\ge r-1$ on $0<z<1$. Here $z=\tan\phi$ and $r-1=\tan(\pi/8)$. | `[propext, Classical.choice, Quot.sound]` | [Line 960](../proofs/lean4/TiltedParity.lean#L960) |
| `SquareEdge.chord_projections` | From every valid square edge point, both computed chord hits lie on the boundary and preserve the correct levels of $2y-x$ and $y+2x$. | `[propext, Classical.choice, Quot.sound]` | [Line 1023](../proofs/lean4/TiltedParity.lean#L1023) |
| `square_horizontal_return` | On the bottom and top edges, the complete return in perimeter coordinates is $c+(t-c)/16$, with $c=1/3$ and $c=7/3$ respectively. | `[propext, Classical.choice, Quot.sound]` | [Line 1035](../proofs/lean4/TiltedParity.lean#L1035) |
| `square_vertical_return` | Within perimeter distance $1/48$ of $c=4/3$ or $10/3$, the complete return is $c+16(t-c)$. | `[propext, Classical.choice, Quot.sound]` | [Line 1043](../proofs/lean4/TiltedParity.lean#L1043) |
| `zhang_temnov_cycles` | At slopes $1/2,-2$, $\mu=4$ and $\mu^{-2}=1/16$. One boundary step exchanges $1/3$ and $7/3$, and exchanges $4/3$ and $10/3$. | `[propext, Classical.choice, Quot.sound]` | [Line 1050](../proofs/lean4/TiltedParity.lean#L1050) |

</details>

## CornerShavingAndTriangles

Contraction applies to nonnegative coordinates. Profile constancy uses one-sided continuity at the corner. The discrete shell energy integrates the squared slope of each linear interpolant against the coordinate weight. For the bevel, $D=n-m/s$, $s_*=m/(n-u)$, and the phase circle has circumference two. The small-cut conditions include $0<u\le v<1$, $s_*<v/u$ and $v+s_*u<1/n$. The frequency-density cancellation assumes $x\ne-1$, as holds on the physical slope interval. The regular polygon calculation uses angles in units of $\pi/N$ and also treats arbitrary reduced phases over a linearly ordered field. [Corner energy and Theorem 4b](phase1_pde.md) · [Regular polygon corner law](phase1_regular.md)

### Main results

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `triangle_common_extremum` | For arbitrary rational functions $\xi,\eta$ on the three vertices, some vertex is a weak minimum or maximum of both projections, including ties. | `[propext, Classical.choice, Quot.sound]` | [Line 14](../proofs/lean4/CornerShavingAndTriangles.lean#L14) |
| `finite_affine_corner_kernel` | A finite affine section fixing 0 and satisfying $0\le T(t)<t$ on $(0,X)$ forces each invariant profile continuous at 0 to equal $A(0)$ on $[0,X)$. | `[propext, Classical.choice, Quot.sound]` | [Line 213](../proofs/lean4/CornerShavingAndTriangles.lean#L213) |
| `equal_weighted_shell_energy` | If $B(ky)=B(y)$ on nonnegative arguments and $k>0$, the exact weighted energy of the linear interpolant on any finite mesh is unchanged by scaling all cells by $k^n$. | `[propext, Classical.choice, Quot.sound]` | [Line 264](../proofs/lean4/CornerShavingAndTriangles.lean#L264) |
| `microscopic_separation` | For every $0<k<n$, block deficit $0\le d\le D$ and integer $j$, the corrected displacement from $2j$ has magnitude at least $2/n-2sD>2v$. | `[propext, Classical.choice, Quot.sound]` | [Line 395](../proofs/lean4/CornerShavingAndTriangles.lean#L395) |
| `at_most_one_bevel_visit` | On a closed lifted orbit with nonnegative deficits, the shaved-square step recurrence and winding $m$ force any two visits to the same closed bevel arc of width $2v$ within one period to have identical indices. | `[propext, Classical.choice, Quot.sound]` | [Line 465](../proofs/lean4/CornerShavingAndTriangles.lean#L465) |
| `bevel_return_multiplier` | For $0<s<\tau$, the unfolded chord equation gives $q=((\tau+s)p+2-4s)/(\tau-s)$. Differences along the two directions have reciprocal factors, and the reverse factor lies in $(0,1)$. | `[propext, Classical.choice, Quot.sound]` | [Line 529](../proofs/lean4/CornerShavingAndTriangles.lean#L529) |
| `period_three_midpoint_multiplier` | For $0<\varepsilon<1$ and $s=1/(2-\varepsilon/2)$, $p=\varepsilon/2$ is a fixed intersection of the unfolded faces, and the multiplier is $(2-\varepsilon)/(6-\varepsilon)$. | `[propext, Classical.choice, Quot.sound]` | [Line 557](../proofs/lean4/CornerShavingAndTriangles.lean#L557) |
| `frequency_density_cancellation` | In any Lean field, for $x\ne-1$, $(x/(1+x))((1+x)/d)=x/d$. Taking $d=1+x^2$ gives the stated rational identity. The general identity also applies to the frequency density’s denominator. | `[propext, Classical.choice, Quot.sound]` | [Line 572](../proofs/lean4/CornerShavingAndTriangles.lean#L572) |
| `minimumMultiplier_lt_third` | For $-1/2<c<1$, the minimum-factor expression is strictly below $1/3$, its value at $c=1$. | `[propext, Classical.choice, Quot.sound]` | [Line 781](../proofs/lean4/CornerShavingAndTriangles.lean#L781) |
| `regular_corner_fractions` | For any reduced phase $0\le p<1$ in a linearly ordered field, the fraction is $3/N$ for odd $N$, $2/N$ for $N\equiv2\pmod4$, and $(4/N)(1-2\min(p,1-p))$ for $4\mid N$. | `[propext, Classical.choice, Quot.sound]` | [Line 809](../proofs/lean4/CornerShavingAndTriangles.lean#L809) |

<details><summary>20 supporting results</summary>

| Theorem | Mathematical statement | Axioms | Source |
|---|---|---|---|
| `characteristic_quadrilateral_extremum` | On four vertices, if two distinct vertices share an extreme value of one projection, the two projections have a common weak extremal vertex. This covers the support-face pigeonhole at a characteristic edge. | `[propext, Classical.choice, Quot.sound]` | [Line 29](../proofs/lean4/CornerShavingAndTriangles.lean#L29) |
| `contraction_iterates` | If $0\le T(x)\le kx$ and $A(Tx)=A(x)$ on $x\ge0$ with $0<k<1$, then $A(T^nx)=A(x)$ and $0\le T^nx\le k^nx$ for all $n$. | `[propext, Classical.choice, Quot.sound]` | [Line 58](../proofs/lean4/CornerShavingAndTriangles.lean#L58) |
| `contraction_kernel_at_corner` | Under this contraction, an invariant rational profile continuous from the right at zero has $A(x)=A(0)$ for every $x\ge0$. | `[propext, Classical.choice, Quot.sound]` | [Line 79](../proofs/lean4/CornerShavingAndTriangles.lean#L79) |
| `finite_affine_local_contraction` | If a finite affine section fixes 0 and $T(t)<t$ on $(0,X)$, each interval $[0,x]$ with $x<X$ has a single $k\in(0,1)$ satisfying $T(t)\le kt$ throughout that interval. | `[propext, Classical.choice, Quot.sound]` | [Line 178](../proofs/lean4/CornerShavingAndTriangles.lean#L178) |
| `bounded_shell_energy_vanishes` | If the partial sums of those identical, nonnegative shell energies have a common finite upper bound, every shell has zero energy. | `[propext, Classical.choice, Quot.sound]` | [Line 287](../proofs/lean4/CornerShavingAndTriangles.lean#L287) |
| `plateau_deficit_bounds` | Under the conditions of Theorem 4b, every $s\in[m/n,m/(n-u)]$ gives $0\le D=n-m/s\le u$ and $2v<2/n-2sD$. | `[propext, Classical.choice, Quot.sound]` | [Line 361](../proofs/lean4/CornerShavingAndTriangles.lean#L361) |
| `block_displacement_error` | For $0\le k\le n$, $n>0$, $s\ge0$, and $0\le d\le D$, the error satisfies $\lvert2s(kD/n-d)\rvert\le2sD$. | `[propext, Classical.choice, Quot.sound]` | [Line 380](../proofs/lean4/CornerShavingAndTriangles.lean#L380) |
| `equal_leg_multiplier` | For equal positive legs and $0<s<1$, the attracting factor is $(1-s)/(1+s)$ and lies strictly between zero and one. | `[propext, Classical.choice, Quot.sound]` | [Line 548](../proofs/lean4/CornerShavingAndTriangles.lean#L548) |
| `projectiveVertexGrid` | The projective vertex indices form $2\mathbb Z+N\mathbb Z=w\mathbb Z$, with $w=1$ for odd $N$ and $w=2$ for even $N$. | `[propext, Classical.choice, Quot.sound]` | [Line 587](../proofs/lean4/CornerShavingAndTriangles.lean#L587) |
| `unitGridDistance_add_int` | Translating the rational phase by any integer preserves its distance to the integer lattice. | `[propext, Classical.choice, Quot.sound]` | [Line 619](../proofs/lean4/CornerShavingAndTriangles.lean#L619) |
| `unitGridDistance_half_shift` | Distances to the integer lattice at phases $x$ and $x+1/2$ add to $1/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 624](../proofs/lean4/CornerShavingAndTriangles.lean#L624) |
| `unitGridDistance_is_min` | The computed nearest-integer distance is attained by an integer and bounds the distance to every integer from below. | `[propext, Classical.choice, Quot.sound]` | [Line 638](../proofs/lean4/CornerShavingAndTriangles.lean#L638) |
| `vertexGridDistance_is_min` | The computed distance from a rational phase to the projective vertex grid is attained on that grid and is a lower bound for every other grid-point distance. | `[propext, Classical.choice, Quot.sound]` | [Line 685](../proofs/lean4/CornerShavingAndTriangles.lean#L685) |
| `axisGridDistances_odd` | For odd $N$, the horizontal and vertical axis distances, measured in units of $\pi/N$, sum to $1/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 698](../proofs/lean4/CornerShavingAndTriangles.lean#L698) |
| `axisGridDistances_two_mod_four` | For $N\equiv2\pmod4$, the two axis distances in units of $\pi/N$ sum to 1. | `[propext, Classical.choice, Quot.sound]` | [Line 711](../proofs/lean4/CornerShavingAndTriangles.lean#L711) |
| `axisGridDistances_four_dvd` | For $4\mid N$, the $N/2$ shift preserves the projective grid distance, so both axis distances agree. | `[propext, Classical.choice, Quot.sound]` | [Line 725](../proofs/lean4/CornerShavingAndTriangles.lean#L725) |
| `cornerAngularFraction_odd` | For odd $N$, the corner angular fraction is $3/N$ for every rational phase. | `[propext, Classical.choice, Quot.sound]` | [Line 739](../proofs/lean4/CornerShavingAndTriangles.lean#L739) |
| `cornerAngularFraction_two_mod_four` | For $N\equiv2\pmod4$, the corner angular fraction is $2/N$ for every rational phase. | `[propext, Classical.choice, Quot.sound]` | [Line 746](../proofs/lean4/CornerShavingAndTriangles.lean#L746) |
| `cornerAngularFraction_four_dvd` | For $4\mid N$, the fraction is $(4/N)(1-d_0)$, where $d_0$ is the horizontal-axis distance in units of $\pi/N$. | `[propext, Classical.choice, Quot.sound]` | [Line 753](../proofs/lean4/CornerShavingAndTriangles.lean#L753) |
| `minimumMultiplier_strictMono` | In a linearly ordered field, $c\mapsto(2c-1)/(2c+1)$ is strictly increasing on $c>-1/2$. | `[propext, Classical.choice, Quot.sound]` | [Line 768](../proofs/lean4/CornerShavingAndTriangles.lean#L768) |

</details>

## Exact kernel output

The names below are fully qualified. Main prints the principal results first within each module, followed by its supporting results. [Main.lean](../proofs/lean4/Main.lean)

<details><summary>125 reports from lake env lean Main.lean</summary>

```text
'Uncloakability.sharpHalfAmplitude' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.finiteSharpHalfAmplitude' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.dihedralTimeReversal' depends on axioms: [propext, Quot.sound]
'Uncloakability.dihedralIterates' depends on axioms: [propext, Quot.sound]
'Uncloakability.zeroTraceInvariance' depends on axioms: [Quot.sound]
'Uncloakability.hexagonZeroTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonFixedPointAndContraction' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.sharpGlobalAmplitude' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.sharpCircuitAmplitude' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonBasinDynamics' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonWallBounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonLocalReturn' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonPeriodicHeights' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.sharpProfileData' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonVerticalFibers' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonBasinSigns' depends on axioms: [propext, Classical.choice, Quot.sound]
'Uncloakability.hexagonBasinWeights' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.fixedPointFree_iff_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.gap_fixed_labels' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.gap_pair_partition' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.attractor_vertex_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.mixed_vertex_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.four_chain_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.central_cylinder_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.localWallReturn' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.prescribedRateWall' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonAttractingRectangle' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.reflection_involution' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.mixed_quadrilateral' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.nontrivial_gap_hits_vertex' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.marked_gap_vertex_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.affine_zero_unique' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.affine_two_zeros' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.affine_interior_root_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.affine_root_count' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.hexagon_four_chain_witness' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.envelope_lines_injective' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.neutral_cell_all_heights' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.envelope_pieces_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.neutral_cell_iff_both_signs' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.envelope_cell_interior_not_isolated' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.envelope_transition_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.isolated_height_is_break' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.central_attractor_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.rectangle_iff_two_active_signs' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.neutral_interval_has_repeated_line' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.signedWallCut_concave' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.prescribedRateGrowth' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.prescribedSlopeCrossing' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.SlopeFront.advance_geometry' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.SlopeFront.displacement_on_tail' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.SlopeFront.alternatingDisplacements' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.SlopeFront.advance_localRate' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonSymmetry' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonFaceRanges' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonEightDistinctVertices' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonStrips' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonExtremeIffVertex' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonNeutralCylinder' depends on axioms: [propext, Classical.choice, Quot.sound]
'MultiplicityBounds.centralOctagonLocalReturn' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.even_boundary_winding' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.odd_boundary_winding' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_parity_table' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.even_balanced_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.odd_balanced_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_physical_identity_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_regular_interior_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.extinction_interval' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.extinction_threshold' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_period_two_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.reduced_winding_fraction' depends on axioms: [propext, Quot.sound]
'TiltedParity.word_product_formula' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.word_product_cover' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_attracting_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_physical_word' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.even_section_mesh_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.odd_section_mesh_no_fixed_interval' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.even_reduced_section_lift_identity' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.odd_reduced_section_lift_no_fixed_interval' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.one_reflected_point_per_gap' depends on axioms: [propext, Quot.sound]
'TiltedParity.interlaced_arc_discrepancy' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.fixed_germ_discrepancy' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.even_reduced_section_lift_from_orbits' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_global_identity_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.regular_sink_of_crossing' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.attracting_cell_iteration' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.canonical_tongue_interior_sink' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.regular_odd_fixed_has_crossing' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_half_angle_threshold' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_algebraic_endpoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_extinction_angle_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.SquareEdge.chord_projections' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_horizontal_return' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.square_vertical_return' depends on axioms: [propext, Classical.choice, Quot.sound]
'TiltedParity.zhang_temnov_cycles' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.triangle_common_extremum' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.finite_affine_corner_kernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.equal_weighted_shell_energy' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.microscopic_separation' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.at_most_one_bevel_visit' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.bevel_return_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.period_three_midpoint_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.frequency_density_cancellation' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.minimumMultiplier_lt_third' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.regular_corner_fractions' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.characteristic_quadrilateral_extremum' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'CornerShavingAndTriangles.contraction_iterates' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.contraction_kernel_at_corner' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.finite_affine_local_contraction' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.bounded_shell_energy_vanishes' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.plateau_deficit_bounds' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.block_displacement_error' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.equal_leg_multiplier' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.projectiveVertexGrid' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.unitGridDistance_add_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.unitGridDistance_half_shift' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.unitGridDistance_is_min' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.vertexGridDistance_is_min' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.axisGridDistances_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.axisGridDistances_two_mod_four' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.axisGridDistances_four_dvd' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.cornerAngularFraction_odd' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.cornerAngularFraction_two_mod_four' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'CornerShavingAndTriangles.cornerAngularFraction_four_dvd' depends on axioms: [propext, Classical.choice, Quot.sound]
'CornerShavingAndTriangles.minimumMultiplier_strictMono' depends on axioms: [propext, Classical.choice, Quot.sound]
```

</details>
