import Uncloakability

/-!
Finite reflection, counting and slope arguments for the multiplicity bounds.
A geometric reduction is recorded by its actual finite data: labeled vertices,
the shared endpoint values of the four-chain difference, or supporting strips
on the upper envelope. All affine calculations are over the rationals.
-/

namespace MultiplicityBounds

/-- Subtraction of a cyclic index from `h`, using representatives in `[0,n)`. -/
def reflection {n : Nat} (h i : Fin n) : Fin n :=
  if hi : i.val ≤ h.val then ⟨h.val - i.val, by omega⟩
  else ⟨n + h.val - i.val, by omega⟩

private theorem reflection_eq {n : Nat} (h i j : Fin n) :
    reflection h i = j ↔ i.val + j.val = h.val ∨ i.val + j.val = h.val + n := by
  rw [Fin.ext_iff]
  unfold reflection
  split <;> dsimp <;> omega

theorem reflection_involution {n : Nat} (h i : Fin n) :
    reflection h (reflection h i) = i := by
  have hs := (reflection_eq h i (reflection h i)).mp rfl
  apply (reflection_eq ..).mpr
  omega

/-- Passing from a marked point to the gap immediately following it subtracts one. -/
def preceding {n : Nat} (h : Fin n) : Fin n :=
  if hzero : h.val = 0 then ⟨n - 1, by have := h.isLt; omega⟩ else ⟨h.val - 1, by omega⟩

def gapReflection {n : Nat} (h i : Fin n) : Fin n := reflection (preceding h) i

/-- The reflection with center parameter `h` is free precisely for odd `h`. -/
theorem fixedPointFree_iff_odd {m : Nat} (h : Fin (2 * m)) :
    (∀ i, reflection h i ≠ i) ↔ h.val % 2 = 1 := by
  constructor
  · intro hfree
    apply Classical.byContradiction
    intro heven
    let i : Fin (2 * m) := ⟨h.val / 2, by omega⟩
    apply hfree i
    apply (reflection_eq ..).mpr
    left
    dsimp [i]
    omega
  · intro hodd i hi
    have := (reflection_eq h i i).mp hi
    omega

def firstFixed {m : Nat} (h : Fin (2*m)) : Fin (2*m) :=
  ⟨(h.val - 1) / 2, by omega⟩

def secondFixed {m : Nat} (h : Fin (2*m)) : Fin (2*m) :=
  ⟨(h.val - 1) / 2 + m, by omega⟩

private theorem gap_eq {m : Nat} (h i j : Fin (2*m)) (odd : h.val % 2 = 1) :
    gapReflection h i = j ↔ i.val + j.val = 2 * (firstFixed h).val ∨
      i.val + j.val = 2 * (firstFixed h).val + 2*m := by
  have hpos : h.val ≠ 0 := by omega
  unfold gapReflection
  rw [reflection_eq]
  simp [preceding, hpos, firstFixed]
  omega

theorem gap_fixed_labels {m : Nat} (h : Fin (2*m)) (free : ∀ i, reflection h i ≠ i) :
    firstFixed h ≠ secondFixed h ∧
      ∀ i, gapReflection h i = i ↔ i = firstFixed h ∨ i = secondFixed h := by
  have odd := (fixedPointFree_iff_odd h).mp free
  constructor
  · intro eq
    have he := congrArg Fin.val eq
    dsimp [firstFixed, secondFixed] at he
    have := h.isLt
    omega
  · intro i
    rw [gap_eq h i i odd]
    simp only [Fin.ext_iff, firstFixed, secondFixed]
    omega

/-- The open semicircle after the first fixed gap gives one member of every pair. -/
def pairFirst {m : Nat} (h : Fin (2*m)) (j : Fin (m-1)) : Fin (2*m) :=
  ⟨(firstFixed h).val + (j.val+1), by dsimp [firstFixed]; omega⟩

def InGapPair {m : Nat} (h : Fin (2*m)) (j : Fin (m-1)) (i : Fin (2*m)) : Prop :=
  i = pairFirst h j ∨ gapReflection h (pairFirst h j) = i

/-- Each index describes two different gaps exchanged by the reflection. Among
nonfixed gaps the index is unique. The two fixed labels are given above. -/
structure GapPartition {m : Nat} (h : Fin (2*m)) : Prop where
  involutive : ∀ i, gapReflection h (gapReflection h i) = i
  twoMembers : ∀ j, gapReflection h (pairFirst h j) ≠ pairFirst h j
  disjoint : ∀ {j k i}, InGapPair h j i → InGapPair h k i → j = k
  nonfixed : ∀ {j i}, InGapPair h j i → gapReflection h i ≠ i
  exhaustive : ∀ i, gapReflection h i ≠ i → ∃ j : Fin (m-1), InGapPair h j i

theorem gap_pair_partition {m : Nat} (h : Fin (2*m)) (free : ∀ i, reflection h i ≠ i) :
    GapPartition h := by
  have odd := (fixedPointFree_iff_odd h).mp free
  have inv (i) : gapReflection h (gapReflection h i) = i := reflection_involution ..
  have between (j : Fin (m-1)) :
      (firstFixed h).val < (pairFirst h j).val ∧ (pairFirst h j).val < (secondFixed h).val := by
    dsimp [pairFirst, firstFixed, secondFixed]
    omega
  have two (j : Fin (m-1)) : gapReflection h (pairFirst h j) ≠ pairFirst h j := by
    intro hf
    rcases (gap_fixed_labels h free).2 _ |>.mp hf with hf | hf <;>
      have := congrArg Fin.val hf <;> have := between j <;> omega
  have noCross (j k : Fin (m-1)) : gapReflection h (pairFirst h j) ≠ pairFirst h k := by
    intro heq
    have := (gap_eq _ _ _ odd).mp heq
    dsimp [pairFirst] at this
    omega
  have repInj {j k : Fin (m-1)} (eq : pairFirst h j = pairFirst h k) : j = k := by
    have e := congrArg Fin.val eq
    dsimp [pairFirst] at e
    exact Fin.ext (by omega)
  refine ⟨inv, two, ?_, ?_, ?_⟩
  · intro j k i hj hk
    rcases hj with rfl | hj
    · rcases hk with hk | hk
      · exact repInj hk
      · exact (noCross k j hk).elim
    · rcases hk with rfl | hk
      · exact (noCross j k hj).elim
      · have he := congrArg (gapReflection h) (hj.trans hk.symm)
        simp only [inv] at he
        exact repInj he
  · intro j i hi hfix
    rcases hi with rfl | rfl
    · exact two j hfix
    · rw [inv] at hfix
      exact two j hfix.symm
  · intro i moved
    have h₀ : i.val ≠ (h.val-1)/2 := by
      intro e
      exact moved (((gap_fixed_labels h free).2 i).mpr (Or.inl (Fin.ext e)))
    have h₁ : i.val ≠ (h.val-1)/2 + m := by
      intro e
      exact moved (((gap_fixed_labels h free).2 i).mpr (Or.inr (Fin.ext e)))
    by_cases left : i.val < (h.val-1)/2
    · let j : Fin (m-1) := ⟨(h.val-1)/2 - i.val - 1, by omega⟩
      refine ⟨j, Or.inr ((gap_eq _ _ _ odd).mpr (Or.inl ?_))⟩
      dsimp [j, pairFirst, firstFixed]
      omega
    · by_cases middle : i.val < (h.val-1)/2 + m
      · let j : Fin (m-1) := ⟨i.val - (h.val-1)/2 - 1, by omega⟩
        refine ⟨j, Or.inl (Fin.ext ?_)⟩
        dsimp [j, pairFirst, firstFixed]
        omega
      · let j : Fin (m-1) := ⟨2*m + (h.val-1)/2 - i.val - 1, by omega⟩
        refine ⟨j, Or.inr ((gap_eq _ _ _ odd).mpr (Or.inr ?_))⟩
        dsimp [j, pairFirst, firstFixed]
        omega

private theorem image_nodup {a b : Nat} {f : Fin a → Fin b} (hf : Function.Injective f) :
    ((List.finRange a).map f).Nodup :=
  (List.nodup_finRange a).map f (fun _ _ ne eq => ne (hf eq))

private theorem inside_finRange {k : Nat} (xs : List (Fin k)) (distinct : xs.Nodup) :
    xs.length ≤ k := by
  simpa only [List.length_finRange] using
    (distinct.length_le_of_subset (l₂ := List.finRange k) (fun {x} _ => List.mem_finRange x))

private theorem disjoint_images_bound {a b k : Nat} (f : Fin a → Fin k) (g : Fin b → Fin k)
    (hf : Function.Injective f) (hg : Function.Injective g) (apart : ∀ i j, f i ≠ g j) :
    a+b ≤ k := by
  have d : ((List.finRange a).map f ++ (List.finRange b).map g).Nodup := by
    refine List.nodup_append.mpr ⟨image_nodup hf, image_nodup hg, ?_⟩
    intro x hx y hy
    obtain ⟨i, _, rfl⟩ := List.mem_map.mp hx
    obtain ⟨j, _, rfl⟩ := List.mem_map.mp hy
    exact apart i j
  simpa using inside_finRange _ d

/-- Only the incidence data used by the polygon count. A vertex at a marked
point may be assigned `none`. A conjugate pair need only contain some vertex;
distinct witnesses for different pairs follow from the partition. -/
structure GapVertices {m : Nat} (h : Fin (2*m)) (k : Nat) where
  location : Fin k → Option (Fin (2*m))
  extremum : Fin 4 → Fin k
  distinctExtrema : Function.Injective extremum
  fixedExtrema : ∀ e, ∃ x, location (extremum e) = some x ∧ gapReflection h x = x
  meets : ∀ j : Fin (m-1), ∃ v x, location v = some x ∧ InGapPair h j x

private theorem gap_vertex_count {n k : Nat} {h : Fin (2*n)} (free : ∀ i, reflection h i ≠ i)
    (v : GapVertices h k) : 4 + (n-1) ≤ k := by
  have part := gap_pair_partition h free
  let extra (j : Fin (n-1)) := Classical.choose (v.meets j)
  have atExtra (j : Fin (n-1)) :
      ∃ x, v.location (extra j) = some x ∧ InGapPair h j x := Classical.choose_spec (v.meets j)
  apply disjoint_images_bound v.extremum extra v.distinctExtrema
  · intro i j eq
    obtain ⟨x, hx, px⟩ := atExtra i
    obtain ⟨y, hy, py⟩ := atExtra j
    rw [eq, hy] at hx
    cases Option.some.inj hx
    exact part.disjoint px py
  · intro i j eq
    obtain ⟨x, hx, fixed⟩ := v.fixedExtrema i
    obtain ⟨y, hy, paired⟩ := atExtra j
    rw [eq, hy] at hx
    cases Option.some.inj hx
    exact part.nonfixed paired fixed

theorem attractor_vertex_bound {m k : Nat} (h : Fin (2*m)) (free : ∀ i, reflection h i ≠ i)
    (v : GapVertices h k) : m+3 ≤ k ∧ m ≤ k-3 := by
  have := gap_vertex_count free v
  have := h.isLt
  omega

/-- Adding a free pair of neutral marks changes the half-count from `m` to `m+1`. -/
theorem mixed_vertex_bound {m k : Nat} (h : Fin (2*(m+1))) (free : ∀ i, reflection h i ≠ i)
    (v : GapVertices h k) : m+4 ≤ k := by
  have := gap_vertex_count free v
  omega

theorem mixed_quadrilateral {m : Nat} (h : Fin (2*(m+1))) (free : ∀ i, reflection h i ≠ i)
    (v : GapVertices h 4) : m = 0 := by
  have := mixed_vertex_bound h free v
  omega


/-! The geometric incidence used in the cycle count follows from the individual
half-flights. Use a unit coordinate on each successive marked gap. A flight
whose open gap encounters no polygon vertex is affine in these coordinates. -/

structure GapFlight (k : Nat) where
  image : Rat → Rat
  vertices : List (Fin k)
  stays : ∀ t, 0 ≤ t → t ≤ 1 → 0 ≤ image t ∧ image t ≤ 1
  affine : vertices = [] → ∃ a b : Rat, ∀ t, 0 ≤ t → t ≤ 1 → image t = a*t+b

def gapReturn (legs : List (GapFlight k)) (t : Rat) :=
  legs.foldl (fun x flight => flight.image x) t

private theorem unbroken_gap_affine (legs : List (GapFlight k))
    (unbroken : ∀ leg ∈ legs, leg.vertices = []) :
    ∃ a b : Rat, ∀ t, 0 ≤ t → t ≤ 1 → gapReturn legs t = a*t+b := by
  induction legs with
  | nil => exact ⟨1, 0, by intro t _ _; simp [gapReturn, Rat.one_mul, Rat.add_zero]⟩
  | cons leg tail ih =>
    obtain ⟨p, q, first⟩ := leg.affine (unbroken leg List.mem_cons_self)
    obtain ⟨a, b, rest⟩ := ih (fun flight member => unbroken flight (List.mem_cons_of_mem _ member))
    refine ⟨a*p, a*q+b, ?_⟩
    intro t lo hi
    obtain ⟨lo', hi'⟩ := leg.stays t lo hi
    change gapReturn tail (leg.image t) = _
    rw [rest _ lo' hi', first t lo hi]
    grind only

/-- A returning gap with fixed endpoints and a moving interior point encounters
a polygon vertex in at least one of its half-flights. -/
theorem nontrivial_gap_hits_vertex (legs : List (GapFlight k))
    (left : gapReturn legs 0 = 0) (right : gapReturn legs 1 = 1)
    (moves : ∃ t, 0 < t ∧ t < 1 ∧ gapReturn legs t ≠ t) :
    ∃ leg ∈ legs, ∃ v, v ∈ leg.vertices := by
  apply Classical.byContradiction
  intro missed
  have unbroken (leg : GapFlight k) (mem : leg ∈ legs) : leg.vertices = [] := by
    cases h : leg.vertices with
    | nil => rfl
    | cons v rest =>
      exact False.elim (missed ⟨leg, mem, v, h ▸ List.mem_cons_self⟩)
  obtain ⟨a, b, affine⟩ := unbroken_gap_affine legs unbroken
  obtain ⟨t, lo, hi, moving⟩ := moves
  have zero := affine 0 Rat.le_refl (by decide)
  have one := affine 1 (by decide) Rat.le_refl
  have atPoint := affine t (Rat.le_of_lt lo) (Rat.le_of_lt hi)
  grind only

/-- Data from following the half-flights of one marked gap in each conjugate
pair. The vertex label refers to its unique position on the original boundary. -/
structure MarkedGapReturns {r : Nat} (h : Fin (2*r)) (k : Nat) where
  location : Fin k → Option (Fin (2*r))
  extremum : Fin 4 → Fin k
  distinct : Function.Injective extremum
  fixedExtrema : ∀ i, ∃ x, location (extremum i) = some x ∧ gapReflection h x = x
  flights : Fin (r-1) → List (GapFlight k)
  located : ∀ j, ∀ leg ∈ flights j, ∀ v ∈ leg.vertices,
    ∃ x, location v = some x ∧ InGapPair h j x
  closed : ∀ j, gapReturn (flights j) 0 = 0 ∧ gapReturn (flights j) 1 = 1
  moves : ∀ j, ∃ t, 0 < t ∧ t < 1 ∧ gapReturn (flights j) t ≠ t

def MarkedGapReturns.toGapVertices {h : Fin (2*r)} (g : MarkedGapReturns h k) :
    GapVertices h k where
  location := g.location
  extremum := g.extremum
  distinctExtrema := g.distinct
  fixedExtrema := g.fixedExtrema
  meets j := by
    obtain ⟨leg, member, v, atLeg⟩ :=
      nontrivial_gap_hits_vertex _ (g.closed j).1 (g.closed j).2 (g.moves j)
    exact ⟨v, g.located j leg member v atLeg⟩

/-- The half-flight certificate gives both counts by taking r=m for an
attracting/repelling marking, or r=m+1 when the neutral pair is marked as well. -/
theorem marked_gap_vertex_bound {h : Fin (2*r)} (free : ∀ i, reflection h i ≠ i)
    (g : MarkedGapReturns h k) : r+3 ≤ k ∧ r ≤ k-3 :=
  attractor_vertex_bound h free g.toGapVertices

/-- Normalized coordinate on one affine piece. Consecutive pieces use one
value at their common endpoint, so continuity is part of the representation. -/
def interpolate (u v t : Rat) : Rat := (1-t)*u+t*v

abbrev OppositeEnds (u v : Rat) : Prop := (u < 0 ∧ 0 < v) ∨ (v < 0 ∧ 0 < u)

theorem affine_zero_unique {u v x y : Rat} (nonconstant : u ≠ v)
    (hx : interpolate u v x = 0) (hy : interpolate u v y = 0) : x = y := by
  unfold interpolate at hx hy
  have h : (x-y)*(u-v)=0 := by grind
  rcases Rat.mul_eq_zero.mp h with e | e <;> grind

theorem affine_two_zeros {u v x y : Rat} (different : x ≠ y)
    (hx : interpolate u v x = 0) (hy : interpolate u v y = 0) : u = 0 ∧ v = 0 := by
  have e : u = v := Classical.byContradiction fun h => different (affine_zero_unique h hx hy)
  unfold interpolate at hx
  grind

private theorem crossing_increasing {u v : Rat} (hu : u < 0) (hv : 0 < v) :
    ∃ t : Rat, 0 < t ∧ t < 1 ∧ interpolate u v t = 0 := by
  have hp : 0 < v-u := by grind
  let t := (-u)/(v-u)
  have eq : t * (v-u) = -u := Rat.div_mul_cancel (Rat.ne_of_gt hp)
  refine ⟨t, (Rat.lt_div_iff hp).mpr (by grind), (Rat.div_lt_iff hp).mpr (by grind), ?_⟩
  unfold interpolate
  grind

/-- Each nonconstant piece has an interior root precisely when its endpoint
values have opposite strict signs. This also characterizes the isolated roots
away from chain breaks. -/
theorem affine_interior_root_iff (u v : Rat) :
    (u ≠ v ∧ ∃ t : Rat, 0 < t ∧ t < 1 ∧ interpolate u v t = 0) ↔ OppositeEnds u v := by
  constructor
  · rintro ⟨hne, t, hpos, hlt, eq⟩
    have w : 0 < 1-t := by grind
    unfold interpolate at eq
    have up ⦃x : Rat⦄ (hx : 0 < x) : 0 < (1-t)*x := Rat.mul_pos w hx
    have vp ⦃x : Rat⦄ (hx : 0 < x) : 0 < t*x := Rat.mul_pos hpos hx
    have un ⦃x : Rat⦄ (hx : x < 0) : (1-t)*x < 0 := (Rat.mul_neg_iff_of_pos_left w).mpr hx
    have vn ⦃x : Rat⦄ (hx : x < 0) : t*x < 0 := (Rat.mul_neg_iff_of_pos_left hpos).mpr hx
    by_cases hp : 0 < u
    · right
      refine ⟨?_, hp⟩
      have := up hp
      by_cases hv : 0 < v
      · have := vp hv
        grind
      · grind
    · left
      by_cases hn : u < 0
      · have := un hn
        by_cases hv : v < 0
        · have := vn hv
          grind
        · grind
      · have uz : u = 0 := by grind
        by_cases hv : 0 < v
        · have := vp hv
          grind
        · have hvn : v < 0 := by grind
          have := vn hvn
          grind
  · rintro (⟨hu, hv⟩ | ⟨hv, hu⟩)
    · exact ⟨by grind, crossing_increasing hu hv⟩
    · obtain ⟨t, hp, hlt, eq⟩ := crossing_increasing hv hu
      refine ⟨by grind, 1-t, by grind, by grind, ?_⟩
      unfold interpolate at *
      grind

def crossingPieces {P : Nat} (values : Fin (P+1) → Rat) : List (Fin P) :=
  (List.finRange P).filter fun i => decide (OppositeEnds (values i.castSucc) (values i.succ))

private theorem crossing_mem {P : Nat} (values : Fin (P+1) → Rat) (i : Fin P) :
    i ∈ crossingPieces values ↔ OppositeEnds (values i.castSucc) (values i.succ) := by
  simp [crossingPieces, List.mem_finRange]

private theorem skip_one {n : Nat} {xs : List (Fin n)} (distinct : xs.Nodup) (a : Fin n)
    (ha : a ∉ xs) : xs.length+1 ≤ n := by
  simpa using inside_finRange (a::xs) (List.nodup_cons.mpr ⟨ha, distinct⟩)

private theorem skip_two {n : Nat} {xs : List (Fin n)} (distinct : xs.Nodup) (a b : Fin n)
    (hab : a ≠ b) (ha : a ∉ xs) (hb : b ∉ xs) : xs.length+2 ≤ n := by
  have hd := List.nodup_cons.mpr ⟨hb, distinct⟩
  have h := skip_one hd a (by simpa using And.intro hab ha)
  simpa using h

/-- A zero piece excludes itself and an adjacent piece, even if it is the
first or the last. The two cases of truncated subtraction include `P = 1`. -/
theorem affine_root_count {P : Nat} (values : Fin (P+1) → Rat) (flat : Fin P)
    (leftZero : values flat.castSucc = 0) (rightZero : values flat.succ = 0) :
    (crossingPieces values).length ≤ P-2 := by
  have distinct : (crossingPieces values).Nodup :=
    (List.nodup_finRange P).filter _
  have missLeft (i : Fin P) (h : values i.castSucc = 0) : i ∉ crossingPieces values := by
    intro mem
    have := (crossing_mem _ _).mp mem
    simp [h, OppositeEnds] at this
  have missRight (i : Fin P) (h : values i.succ = 0) : i ∉ crossingPieces values := by
    intro mem
    have := (crossing_mem _ _).mp mem
    simp [h, OppositeEnds] at this
  have missing := missLeft flat leftZero
  by_cases one : P = 1
  · have := skip_one distinct flat missing
    omega
  · by_cases right : flat.val+1 < P
    · let adj : Fin P := ⟨flat.val+1, right⟩
      have id : adj.castSucc = flat.succ := Fin.ext rfl
      have hm := missLeft adj (id ▸ rightZero)
      have ne : flat ≠ adj := fun e => by have he := congrArg Fin.val e; dsimp [adj] at he; omega
      have := skip_two distinct flat adj ne missing hm
      omega
    · let adj : Fin P := ⟨flat.val-1, by omega⟩
      have id : adj.succ = flat.castSucc := Fin.ext (by dsimp [adj, Fin.succ, Fin.castSucc]; omega)
      have hm := missRight adj (id ▸ leftZero)
      have ne : flat ≠ adj := fun e => by have he := congrArg Fin.val e; dsimp [adj] at he; omega
      have := skip_two distinct flat adj ne missing hm
      omega

theorem four_chain_bound {k P : Nat} (values : Fin (P+1) → Rat) (flat : Fin P)
    (leftZero : values flat.castSucc = 0) (rightZero : values flat.succ = 0)
    (chainCount : P ≤ k-3) :
    (crossingPieces values).length ≤ k-5 ∧ (0 < (crossingPieces values).length → 6 ≤ k) := by
  have := affine_root_count values flat leftZero rightZero
  omega

/-- The rational hexagon's four-chain displacement `v(X(-y))-y` at
`y = 0, 1/2, 3/4, 1`. Its first piece has a root at `y=1/4`, the last is flat.
The local coordinate of that root on the first piece is `1/2`. -/
theorem hexagon_four_chain_witness :
    let values : Fin 4 → Rat := fun i => ([1/8, -1/8, 0, 0] : List Rat)[i.val]'(by simp)
    (crossingPieces (P := 3) values).length = 1 ∧
      interpolate (values 0) (values 1) (1/2) = 0 ∧ values 2 = 0 ∧ values 3 = 0 := by
  decide +kernel


structure AffineLine where
  intercept : Rat
  slope : Rat
  deriving DecidableEq

def AffineLine.atHeight (l : AffineLine) (t : Rat) : Rat := l.intercept + l.slope*t

structure Strip where
  line : AffineLine
  positive : Bool
  deriving DecidableEq

/-- A folded strip maximizes its affine line at this ray slope. -/
def Dominates {h : Nat} (s : Fin h → Strip) (i : Fin h) (t : Rat) : Prop :=
  ∀ j, (s j).line.atHeight t ≤ (s i).line.atHeight t

def BothSigns {h : Nat} (s : Fin h → Strip) (t : Rat) : Prop :=
  ∃ i j, (s i).positive ≠ (s j).positive ∧ Dominates s i t ∧ Dominates s j t

/-- The interior extent of an isolating interval is part of the definition. -/
def IsolatedEquality {h : Nat} (s : Fin h → Strip) (t : Rat) : Prop :=
  BothSigns s t ∧ ∃ l r, l < t ∧ t < r ∧ ∀ z, l < z → z < r → z ≠ t → ¬ BothSigns s z

/-- Consecutive maximal affine cells in a finite window of the upper envelope.
At least one supporting strip is recorded per cell. Global distinctness of
their lines is proved below, using convexity of each dominance region. -/
structure Envelope {h : Nat} (s : Fin h → Strip) (P : Nat) where
  knot : Fin (P+1) → Rat
  increasing : ∀ {i j}, i.val < j.val → knot i < knot j
  carrier : Fin P → Fin h
  active : ∀ i t, knot i.castSucc ≤ t → t ≤ knot i.succ → Dominates s (carrier i) t
  adjacent : ∀ i j, i.val + 1 = j.val → (s (carrier i)).line ≠ (s (carrier j)).line

private theorem knot_le {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    {i j : Fin (P+1)} (hij : i.val ≤ j.val) : e.knot i ≤ e.knot j := by
  by_cases eq : i = j
  · rw [eq]
    exact Rat.le_refl
  · exact Rat.le_of_lt (e.increasing (show i.val < j.val from by
        have hn : i.val ≠ j.val := fun he => eq (Fin.ext he)
        omega))

private theorem width {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) (i : Fin P) :
    e.knot i.castSucc < e.knot i.succ := e.increasing (by change i.val < i.val+1; omega)

private theorem line_order_between {a b : AffineLine} {x y z : Rat}
    (hx : a.atHeight x ≤ b.atHeight x) (hy : a.atHeight y ≤ b.atHeight y)
    (xz : x ≤ z) (zy : z ≤ y) : a.atHeight z ≤ b.atHeight z := by
  unfold AffineLine.atHeight at *
  rcases (Rat.le_total : a.slope ≤ b.slope ∨ b.slope ≤ a.slope) with hd | hd
  · have := Rat.mul_nonneg (show 0 ≤ b.slope-a.slope by grind) (show 0 ≤ z-x by grind)
    grind
  · have := Rat.mul_nonneg (show 0 ≤ a.slope-b.slope by grind) (show 0 ≤ y-z by grind)
    grind

private theorem lines_equal_at_two {a b : AffineLine} {x y : Rat} (xy : x < y)
    (hx : a.atHeight x = b.atHeight x) (hy : a.atHeight y = b.atHeight y) : a = b := by
  cases a with | mk c d =>
  cases b with | mk f g =>
  unfold AffineLine.atHeight at hx hy
  dsimp at hx hy
  have eq : (d-g)*(y-x)=0 := by grind
  rcases Rat.mul_eq_zero.mp eq with z | z <;> grind

/-- An affine line below the active line on a cell that touches it in the
interior must coincide with it on the whole cell. -/
private theorem touching_lines {a b : AffineLine} {l x r : Rat}
    (lx : l < x) (xr : x < r) (hl : a.atHeight l ≤ b.atHeight l)
    (hr : a.atHeight r ≤ b.atHeight r) (hx : a.atHeight x = b.atHeight x) : a = b := by
  cases a with | mk c d =>
  cases b with | mk f g =>
  unfold AffineLine.atHeight at hl hr hx
  dsimp at hl hr hx
  by_cases h : d < g
  · have := Rat.mul_pos (show 0 < g-d by grind) (show 0 < x-l by grind)
    grind
  · by_cases h' : g < d
    · have := Rat.mul_pos (show 0 < d-g by grind) (show 0 < r-x by grind)
      grind
    · grind

/-- No line can return on a later maximal cell of an upper envelope. -/
theorem envelope_lines_injective {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) :
    Function.Injective (fun i => (s (e.carrier i)).line) := by
  have ordered (i j : Fin P) (lt : i.val < j.val)
      (same : (s (e.carrier i)).line = (s (e.carrier j)).line) : False := by
    let a : Fin P := ⟨i.val+1, by omega⟩
    have ad := e.adjacent i a rfl
    have endI := e.active i _ Rat.le_refl (Rat.le_of_lt (width e i)) (e.carrier a)
    have endJ := e.active j _ (Rat.le_of_lt (width e j)) Rat.le_refl (e.carrier a)
    rw [← same] at endJ
    have inside (u : Fin (P+1)) (iu : i.val ≤ u.val) (uj : u.val ≤ j.val+1) :
        (s (e.carrier a)).line.atHeight (e.knot u) ≤ (s (e.carrier i)).line.atHeight (e.knot u) :=
      line_order_between endI endJ (knot_le e (i := i.castSucc) iu) (knot_le e (j := j.succ) uj)
    have left := inside a.castSucc (by change i.val ≤ i.val+1; omega)
      (by change i.val+1 ≤ j.val+1; omega)
    have right := inside a.succ (by change i.val ≤ i.val+1+1; omega)
      (by change i.val+1+1 ≤ j.val+1; omega)
    have el := e.active a _ Rat.le_refl (Rat.le_of_lt (width e a)) (e.carrier i)
    have er := e.active a _ (Rat.le_of_lt (width e a)) Rat.le_refl (e.carrier i)
    exact ad (lines_equal_at_two (width e a) (Rat.le_antisymm el left) (Rat.le_antisymm er right))
  intro i j same
  by_cases lt : i.val < j.val
  · exact (ordered i j lt same).elim
  · by_cases gt : j.val < i.val
    · exact (ordered j i gt same.symm).elim
    · exact Fin.ext (by omega)

/-- Opposite signed copies of a supporting line coincide on this actual cell. -/
def NeutralCell {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) (i : Fin P) : Prop :=
  ∃ a b : Fin h, (s a).line = (s (e.carrier i)).line ∧
    (s b).line = (s (e.carrier i)).line ∧ (s a).positive ≠ (s b).positive

theorem neutral_cell_all_heights {h P : Nat} {s : Fin h → Strip} {e : Envelope s P} {i : Fin P}
    (neutral : NeutralCell e i) {t : Rat} (hl : e.knot i.castSucc ≤ t) (hr : t ≤ e.knot i.succ) :
    BothSigns s t := by
  obtain ⟨a, b, ha, hb, signs⟩ := neutral
  exact ⟨a, b, signs, fun j => ha ▸ e.active i t hl hr j, fun j => hb ▸ e.active i t hl hr j⟩

theorem envelope_pieces_bound {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) (i : Fin P)
    (neutral : NeutralCell e i) : P ≤ h-1 := by
  obtain ⟨a, b, ha, hb, signs⟩ := neutral
  have spare : ∃ u, (s u).line = (s (e.carrier i)).line ∧ u ≠ e.carrier i := by
    by_cases ae : a = e.carrier i
    · refine ⟨b, hb, ?_⟩
      intro be
      exact signs (congrArg (fun j => (s j).positive) (ae.trans be.symm))
    · exact ⟨a, ha, ae⟩
  obtain ⟨u, hu, une⟩ := spare
  have lInj := envelope_lines_injective e
  have cInj : Function.Injective e.carrier := fun _ _ eq => lInj (congrArg (fun j => (s j).line) eq)
  have sep (j : Fin P) (_ : Fin 1) : e.carrier j ≠ u := by
    intro eq
    have ji : j = i := lInj ((congrArg (fun k => (s k).line) eq).trans hu)
    exact une (ji ▸ eq.symm)
  have card := disjoint_images_bound e.carrier (fun _ : Fin 1 => u) cInj
    (fun a b _ => Fin.ext (show a.val = b.val from by omega)) sep
  omega

private theorem left_neutral_not_isolated {h : Nat} {s : Fin h → Strip} {a t : Rat}
    (ht : a < t) (persists : ∀ z, a ≤ z → z ≤ t → BothSigns s z) : ¬ IsolatedEquality s t := by
  rintro ⟨_, l, r, lt, tr, alone⟩
  by_cases al : a ≤ l
  · let z := (l+t)/2
    exact alone z (by dsimp [z]; grind) (by dsimp [z]; grind) (by dsimp [z]; grind)
      (persists z (by dsimp [z]; grind) (by dsimp [z]; grind))
  · let z := (a+t)/2
    exact alone z (by dsimp [z]; grind) (by dsimp [z]; grind) (by dsimp [z]; grind)
      (persists z (by dsimp [z]; grind) (by dsimp [z]; grind))

private theorem right_neutral_not_isolated {h : Nat} {s : Fin h → Strip} {t b : Rat}
    (ht : t < b) (persists : ∀ z, t ≤ z → z ≤ b → BothSigns s z) : ¬ IsolatedEquality s t := by
  rintro ⟨_, l, r, lt, tr, alone⟩
  by_cases br : b ≤ r
  · let z := (t+b)/2
    exact alone z (by dsimp [z]; grind) (by dsimp [z]; grind) (by dsimp [z]; grind)
      (persists z (by dsimp [z]; grind) (by dsimp [z]; grind))
  · let z := (t+r)/2
    exact alone z (by dsimp [z]; grind) (by dsimp [z]; grind) (by dsimp [z]; grind)
      (persists z (by dsimp [z]; grind) (by dsimp [z]; grind))

theorem neutral_cell_iff_both_signs {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    (i : Fin P) {t : Rat} (lt : e.knot i.castSucc < t) (rt : t < e.knot i.succ) :
    NeutralCell e i ↔ BothSigns s t := by
  constructor
  · intro neutral
    exact neutral_cell_all_heights neutral (Rat.le_of_lt lt) (Rat.le_of_lt rt)
  · intro both
    obtain ⟨a, b, different, da, db⟩ := both
    have same (j : Fin h) (dom : Dominates s j t) : (s j).line = (s (e.carrier i)).line :=
      touching_lines lt rt
        (e.active i _ Rat.le_refl (Rat.le_of_lt (width e i)) j)
        (e.active i _ (Rat.le_of_lt (width e i)) Rat.le_refl j)
        (Rat.le_antisymm (e.active i _ (Rat.le_of_lt lt) (Rat.le_of_lt rt) j) (dom _))
    exact ⟨a, b, same a da, same b db, different⟩

theorem envelope_cell_interior_not_isolated {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    (i : Fin P) {t : Rat} (lt : e.knot i.castSucc < t) (rt : t < e.knot i.succ) :
    ¬ IsolatedEquality s t := by
  intro iso
  have neutral := (neutral_cell_iff_both_signs e i lt rt).mpr iso.1
  exact left_neutral_not_isolated lt (fun _ hl hr =>
    neutral_cell_all_heights neutral hl (Rat.le_trans hr (Rat.le_of_lt rt))) iso

def breakLabel {P : Nat} (b : Fin (P-1)) : Fin (P+1) := ⟨b.val+1, by omega⟩

/-- This list counts isolated two-sign equalities at internal knots, with the
isolation condition quantified over ray slopes, rather than given as a label. -/
noncomputable def isolatedBreaks {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) :
    List (Fin (P-1)) := by
  classical
  exact (List.finRange (P-1)).filter fun b => decide (IsolatedEquality s (e.knot (breakLabel b)))

theorem envelope_transition_bound {h P : Nat} {s : Fin h → Strip} (e : Envelope s P) (i : Fin P)
    (neutral : NeutralCell e i) :
    (isolatedBreaks e).length ≤ P-2 ∧ (isolatedBreaks e).length ≤ h-3 ∧
      (0 < (isolatedBreaks e).length → 8 ≤ 2*h) := by
  classical
  have distinct : (isolatedBreaks e).Nodup := (List.nodup_finRange _).filter _
  have avoid (b : Fin (P-1)) (ne : ¬ IsolatedEquality s (e.knot (breakLabel b))) :
      b ∉ isolatedBreaks e := by simp [isolatedBreaks, ne]
  have persistence (z hl hr) : BothSigns s z := neutral_cell_all_heights neutral hl hr
  have hP := envelope_pieces_bound e i neutral
  suffices count : (isolatedBreaks e).length ≤ P-2 by omega
  by_cases one : P = 1
  · have card := inside_finRange _ distinct
    omega
  · by_cases interior : i.val+1 < P
    · let b : Fin (P-1) := ⟨i.val, by omega⟩
      have eq : breakLabel b = i.succ := Fin.ext rfl
      have ne := left_neutral_not_isolated (width e i) persistence
      have := skip_one distinct b (avoid b (eq ▸ ne))
      omega
    · let b : Fin (P-1) := ⟨i.val-1, by omega⟩
      have eq : breakLabel b = i.castSucc := Fin.ext (by dsimp [breakLabel, b, Fin.castSucc]; omega)
      have ne := right_neutral_not_isolated (width e i) persistence
      have := skip_one distinct b (avoid b (eq ▸ ne))
      omega


private theorem envelope_cover {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    {t : Rat} (hL : e.knot 0 < t) (j : Nat) : ∀ hj : j ≤ P, t ≤ e.knot ⟨j, by omega⟩ →
    ∃ i : Fin P, e.knot i.castSucc ≤ t ∧ t ≤ e.knot i.succ := by
  induction j with
  | zero =>
    intro hj up
    change t ≤ e.knot 0 at up
    grind
  | succ j ih =>
    intro hj up
    let i : Fin P := ⟨j, by omega⟩
    by_cases prev : t ≤ e.knot i.castSucc
    · exact ih (by omega) prev
    · exact ⟨i, by grind, up⟩

/-- Every isolated equality inside the window occurs at a counted internal
knot. The endpoints of an arbitrarily chosen finite window are excluded. -/
theorem isolated_height_is_break {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    {t : Rat} (hL : e.knot 0 < t) (hR : t < e.knot ⟨P, by omega⟩)
    (iso : IsolatedEquality s t) :
    ∃ b, t = e.knot (breakLabel b) ∧ b ∈ isolatedBreaks e := by
  classical
  obtain ⟨i, l, r⟩ := envelope_cover e hL P (by omega) (Rat.le_of_lt hR)
  have located : ∃ b, t = e.knot (breakLabel b) := by
    by_cases atLeft : t = e.knot i.castSucc
    · have pos : 0 < i.val := by
        by_cases z : i.val = 0
        · have iz : i.castSucc = 0 := Fin.ext z
          rw [iz] at atLeft
          grind
        · omega
      let b : Fin (P-1) := ⟨i.val-1, by omega⟩
      have lab : breakLabel b = i.castSucc := Fin.ext (by dsimp [breakLabel,b,Fin.castSucc]; omega)
      exact ⟨b, lab ▸ atLeft⟩
    · have atRight : t = e.knot i.succ := by
        apply Classical.byContradiction
        intro neq
        exact envelope_cell_interior_not_isolated e i (by grind) (by grind) iso
      have inside : i.val+1 < P := by
        by_cases ij : i.val+1 = P
        · have last : i.succ = ⟨P, by omega⟩ := Fin.ext ij
          rw [last] at atRight
          grind
        · omega
      exact ⟨⟨i.val, by omega⟩, atRight⟩
  obtain ⟨b, eq⟩ := located
  refine ⟨b, eq, ?_⟩
  simp only [isolatedBreaks, List.mem_filter, List.mem_finRange, true_and, decide_eq_true_eq]
  exact eq ▸ iso

/-- The cardinality statement for any family of distinct isolated ray slopes in
the window, without supplying in advance their breakpoint labels. -/
theorem central_attractor_bound {h P m : Nat} {s : Fin h → Strip} (e : Envelope s P)
    (flat : Fin P) (neutral : NeutralCell e flat) (root : Fin m → Rat)
    (distinct : Function.Injective root)
    (inside : ∀ i, e.knot 0 < root i ∧ root i < e.knot ⟨P, by omega⟩)
    (isolated : ∀ i, IsolatedEquality s (root i)) :
    m ≤ h-3 ∧ (0 < m → 8 ≤ 2*h) := by
  let witness (i : Fin m) := isolated_height_is_break e (inside i).1 (inside i).2 (isolated i)
  let b (i : Fin m) := Classical.choose (witness i)
  have spec (i : Fin m) : root i = e.knot (breakLabel (b i)) ∧ b i ∈ isolatedBreaks e :=
    Classical.choose_spec (witness i)
  have inj : Function.Injective b := by
    intro i j eq
    exact distinct ((spec i).1.trans ((congrArg (fun j => e.knot (breakLabel j)) eq).trans (spec j).1.symm))
  have incl : (List.finRange m).map b ⊆ isolatedBreaks e := by
    intro x hx
    obtain ⟨i, _, rfl⟩ := List.mem_map.mp hx
    exact (spec i).2
  have H := (image_nodup inj).length_le_of_subset incl
  simp only [List.length_map, List.length_finRange] at H
  have := envelope_transition_bound e flat neutral
  omega

/-- The contribution of a signed strip to the positive or negative ray
maximum is the absolute value of its signed affine expression. -/
def rayValue (s : Strip) (side : Bool) (t : Rat) : Rat :=
  if s.positive = side then (s.line.atHeight t).abs else (s.line.intercept - s.line.slope*t).abs

private theorem ray_value_bound (s : Strip) (side : Bool) {t : Rat}
    (ha : 0 < s.line.intercept) (hb : 0 < s.line.slope) (ht : 0 < t) :
    rayValue s side t ≤ s.line.atHeight t ∧
      (rayValue s side t = s.line.atHeight t ↔ s.positive = side) := by
  have := Rat.mul_pos hb ht
  grind only [rayValue, AffineLine.atHeight, Rat.abs]

def finiteMaximum {n : Nat} (hn : 0 < n) (f : Fin n → Rat) : Rat :=
  ((List.finRange n).map f).max (by
    intro eq
    have he := congrArg List.length eq
    simp at he
    omega)

private theorem finiteMaximum_spec {n : Nat} (hn : 0 < n) (f : Fin n → Rat) :
    (∀ i, f i ≤ finiteMaximum hn f) ∧ ∃ i, f i = finiteMaximum hn f := by
  constructor
  · intro i
    exact List.le_max_of_mem (List.mem_map_of_mem (f := f) (List.mem_finRange i))
  · obtain ⟨i, _, eq⟩ := List.mem_map.mp (List.max_mem (l := (List.finRange n).map f) (by
      intro eq
      have he := congrArg List.length eq
      simp at he
      omega))
    exact ⟨i, eq⟩

/-- For positive normal components and positive ray slope the two physical
ray denominators agree exactly when opposite signs share the folded envelope. -/
theorem rectangle_iff_two_active_signs {h : Nat} (s : Fin h → Strip) (hn : 0 < h)
    (positive : ∀ i, 0 < (s i).line.intercept ∧ 0 < (s i).line.slope) {t : Rat} (ht : 0 < t) :
    finiteMaximum hn (fun j => rayValue (s j) true t) =
      finiteMaximum hn (fun j => rayValue (s j) false t) ↔ BothSigns s t := by
  let E := finiteMaximum hn (fun j => (s j).line.atHeight t)
  let Q side := finiteMaximum hn (fun j => rayValue (s j) side t)
  have env := finiteMaximum_spec hn (fun j => (s j).line.atHeight t)
  have ray (side) := finiteMaximum_spec hn (fun j => rayValue (s j) side t)
  have localBound (j : Fin h) (side : Bool) := ray_value_bound (s j) side (positive j).1 (positive j).2 ht
  have Qle (side) : Q side ≤ E := by
    obtain ⟨j, hj⟩ := (ray side).2
    change rayValue (s j) side t = Q side at hj
    exact hj ▸ Rat.le_trans (localBound j side).1 (env.1 j)
  have atTop (side : Bool) : Q side = E ↔ ∃ j, (s j).positive = side ∧ Dominates s j t := by
    constructor
    · intro eq
      obtain ⟨j, hj⟩ := (ray side).2
      change rayValue (s j) side t = Q side at hj
      have je : rayValue (s j) side t = E := hj.trans eq
      have dom : (s j).line.atHeight t = E :=
        Rat.le_antisymm (env.1 j) (je ▸ (localBound j side).1)
      exact ⟨j, (localBound j side).2.mp (je.trans dom.symm), fun i => dom ▸ env.1 i⟩
    · rintro ⟨j, sign, dom⟩
      obtain ⟨k, hk⟩ := env.2
      have low : E ≤ Q side := calc
        E = (s k).line.atHeight t := hk.symm
        _ ≤ (s j).line.atHeight t := dom k
        _ = rayValue (s j) side t := ((localBound j side).2.mpr sign).symm
        _ ≤ Q side := (ray side).1 j
      exact Rat.le_antisymm (Qle side) low
  change Q true = Q false ↔ _
  constructor
  · intro eq
    obtain ⟨k, hk⟩ := env.2
    have dom : Dominates s k t := fun j => hk ▸ env.1 j
    have qe : Q (s k).positive = E := (atTop _).mpr ⟨k, rfl, dom⟩
    have both : Q true = E ∧ Q false = E := by
      cases sk : (s k).positive <;> rw [sk] at qe
      · exact ⟨eq.trans qe, qe⟩
      · exact ⟨qe, eq.symm.trans qe⟩
    obtain ⟨a, sa, da⟩ := (atTop true).mp both.1
    obtain ⟨b, sb, db⟩ := (atTop false).mp both.2
    exact ⟨a, b, by simp [sa, sb], da, db⟩
  · rintro ⟨a, b, signs, da, db⟩
    have qa := (atTop (s a).positive).mpr ⟨a, rfl, da⟩
    have qb := (atTop (s b).positive).mpr ⟨b, rfl, db⟩
    cases sa : (s a).positive <;> cases sb : (s b).positive <;>
      rw [sa] at qa <;> rw [sb] at qb <;> rw [sa, sb] at signs
    · exact (signs rfl).elim
    · exact qb.trans qa.symm
    · exact qa.trans qb.symm
    · exact (signs rfl).elim

private theorem fresh_height (xs : List Rat) {l r : Rat} (lr : l < r) :
    ∃ t, l < t ∧ t < r ∧ t ∉ xs := by
  induction xs generalizing l r with
  | nil => exact ⟨(l+r)/2, by grind, by grind, by simp⟩
  | cons x xs ih =>
    by_cases inside : l < x ∧ x < r
    · obtain ⟨t, lt, tx, avoid⟩ := ih inside.1
      exact ⟨t, lt, by have := inside.2; grind only, by simp [show t ≠ x from by grind, avoid]⟩
    · obtain ⟨t, lt, tr, avoid⟩ := ih lr
      exact ⟨t, lt, tr, by simp [show t ≠ x from by grind, avoid]⟩

/-- An open band of rectangles must contain a point strictly inside one
maximal envelope cell. Its opposite active signs are copies of the same line. -/
theorem neutral_interval_has_repeated_line {h P : Nat} {s : Fin h → Strip} (e : Envelope s P)
    {l r : Rat} (lr : l < r) (insideL : e.knot 0 ≤ l) (insideR : r ≤ e.knot ⟨P, by omega⟩)
    (band : ∀ t, l < t → t < r → BothSigns s t) : ∃ i, NeutralCell e i := by
  obtain ⟨t, lt, tr, fresh⟩ := fresh_height ((List.finRange (P+1)).map e.knot) lr
  have first : e.knot 0 < t := by grind only
  obtain ⟨i, lo, hi⟩ := envelope_cover e first P (by omega) (Rat.le_trans (Rat.le_of_lt tr) insideR)
  have ne (j : Fin (P+1)) : t ≠ e.knot j := by
    intro eq
    exact fresh (eq ▸ List.mem_map_of_mem (f := e.knot) (List.mem_finRange j))
  exact ⟨i, (neutral_cell_iff_both_signs e i (Rat.lt_of_le_of_ne lo (ne _).symm)
    (Rat.lt_of_le_of_ne hi (ne _))).mpr (band t lt tr)⟩

/-- Quantitative central bound directly from an open neutral band of the
two physical ray maxima, for positive normal components and ray slopes. -/
theorem central_cylinder_bound {h P m : Nat} {s : Fin h → Strip} (e : Envelope s P)
    (nonempty : 0 < h) (positive : ∀ i, 0 < (s i).line.intercept ∧ 0 < (s i).line.slope)
    {l r : Rat} (lr : l < r) (lpos : 0 ≤ l)
    (insideL : e.knot 0 ≤ l) (insideR : r ≤ e.knot ⟨P, by omega⟩)
    (band : ∀ t, l < t → t < r →
      finiteMaximum nonempty (fun j => rayValue (s j) true t) =
        finiteMaximum nonempty (fun j => rayValue (s j) false t))
    (root : Fin m → Rat) (distinct : Function.Injective root)
    (inside : ∀ i, e.knot 0 < root i ∧ root i < e.knot ⟨P, by omega⟩)
    (isolated : ∀ i, IsolatedEquality s (root i)) :
    P ≤ h-1 ∧ m ≤ h-3 ∧ (0 < m → 8 ≤ 2*h) := by
  obtain ⟨i, neutral⟩ := neutral_interval_has_repeated_line e lr insideL insideR (fun t lt tr =>
    (rectangle_iff_two_active_signs s nonempty positive (show 0 < t from by grind only)).mp (band t lt tr))
  exact ⟨envelope_pieces_bound e i neutral, central_attractor_bound e i neutral root distinct inside isolated⟩


/-- The side parameter selects the positive or negative wall height. -/
def wallArm (positive : Bool) (y : Rat) : Rat := if positive then y else -y

private theorem arm_same (b : Bool) (y : Rat) : wallArm b (wallArm b y) = y := by
  cases b <;> simp [wallArm, Rat.neg_neg]

private theorem arm_other (b : Bool) (y : Rat) : wallArm b (wallArm (!b) y) = -y := by
  cases b <;> simp [wallArm]

/-- Jensen concavity on the rational height axis. -/
def WallConcave (W : Rat → Rat) : Prop :=
  ∀ x y q : Rat, 0 ≤ q → q ≤ 1 → q * W x + (1-q) * W y ≤ W (q*x+(1-q)*y)

/-- A downward jump in the outward slope, on the indicated side at radius p. -/
def signedWallCut (W : Rat → Rat) (b : Bool) (p drop t : Rat) : Rat :=
  W t - drop * max 0 (wallArm b t - p)

private theorem hinge_le (x y q p : Rat) (hq : 0 ≤ q) (hq' : q ≤ 1) :
    max 0 ((q*x+(1-q)*y) - p) ≤
      q * max 0 (x-p) + (1-q) * max 0 (y-p) := by
  have vx : 0 ≤ max 0 (x-p) := by grind
  have vy : 0 ≤ max 0 (y-p) := by grind
  have ux : x-p ≤ max 0 (x-p) := by grind
  have uy : y-p ≤ max 0 (y-p) := by grind
  have hq'' : 0 ≤ 1-q := by grind only
  have nx := Rat.mul_nonneg hq vx
  have ny := Rat.mul_nonneg hq'' vy
  have ax := Rat.mul_le_mul_of_nonneg_left ux hq
  have ay := Rat.mul_le_mul_of_nonneg_left uy hq''
  rw [Rat.max_def]
  split <;> grind only

theorem signedWallCut_concave {W : Rat → Rat} (hW : WallConcave W) (b : Bool)
    (p drop : Rat) (hd : 0 ≤ drop) : WallConcave (signedWallCut W b p drop) := by
  intro x y q hq hq'
  have h := hW x y q hq hq'
  have a : wallArm b (q*x+(1-q)*y) = q*wallArm b x + (1-q)*wallArm b y := by
    cases b <;> simp [wallArm] <;> grind only
  have hhinge := hinge_le (wallArm b x) (wallArm b y) q p hq hq'
  have hscaled := Rat.mul_le_mul_of_nonneg_left hhinge hd
  simp only [signedWallCut, a]
  grind only

/-- Strict growth and inversion for one prescribed contraction. -/
theorem prescribedRateGrowth {G k : Rat} (hg : 0 < G) (hk : 0 < k) (hk' : k < 1) :
    G < G/k ∧ G/(G/k) = k := by
  have grow : G < G/k := by
    apply (Rat.lt_div_iff hk).mpr
    have := Rat.mul_lt_mul_of_pos_left hk' hg
    grind only
  have nz : G/k ≠ 0 := by grind only
  have eqn := Rat.div_mul_cancel (a := G) (Rat.ne_of_gt hk)
  have eqn' : k * (G/k) = G := by grind only
  refine ⟨grow, ?_⟩
  calc
    G/(G/k) = (k*(G/k))/(G/k) := congrArg (fun v => v/(G/k)) eqn'.symm
    _ = k := Rat.mul_div_cancel nz

/-- Intersection of y ↦ d(y-r) and y ↦ -e(y-s), with d,e both positive. -/
def slopeCrossing (r s d e : Rat) : Rat := (d*r+e*s)/(d+e)

theorem prescribedSlopeCrossing {r s d e : Rat} (hrs : r < s) (hd : 0 < d)
    (he : 0 < e) :
    r < slopeCrossing r s d e ∧ slopeCrossing r s d e < s ∧
    d*(slopeCrossing r s d e-r) = -e*(slopeCrossing r s d e-s) := by
  have hsum : 0 < d+e := by grind only
  have dl := Rat.mul_lt_mul_of_pos_left hrs hd
  have el := Rat.mul_lt_mul_of_pos_left hrs he
  have eqn := Rat.div_mul_cancel (a := d*r+e*s) (Rat.ne_of_gt hsum)
  unfold slopeCrossing
  refine ⟨(Rat.lt_div_iff hsum).mpr ?_, (Rat.div_lt_iff hsum).mpr ?_, ?_⟩ <;> grind only

private theorem cut_before {W : Rat → Rat} {p x drop : Rat} (b c : Bool)
    (hx : 0 ≤ x) (hxp : x ≤ p) :
    signedWallCut W b p drop (wallArm c x) = W (wallArm c x) := by
  have hw : wallArm b (wallArm c x) - p ≤ 0 := by
    cases b <;> cases c <;> simp [wallArm, Rat.neg_neg] <;> grind only
  have hm : max 0 (wallArm b (wallArm c x) - p) = 0 := by grind
  unfold signedWallCut
  rw [hm]
  grind only

private theorem cut_after {W : Rat → Rat} {p x drop : Rat} (b : Bool)
    (hp : 0 ≤ p) (hpx : p ≤ x) :
    signedWallCut W b p drop (wallArm b x) = W (wallArm b x) - drop*(x-p) ∧
    signedWallCut W b p drop (wallArm (!b) x) = W (wallArm (!b) x) := by
  have hm : max 0 (x-p) = x-p := by grind
  have hn : max 0 (-x-p) = 0 := by grind
  simp only [signedWallCut, arm_same, arm_other, hm, hn]
  constructor <;> grind only

/-- On an interval about r, the two outward faces agree at r and have slopes -kG and -G.
The side selector distinguishes the attracting orientation. -/
def LocalWallRate (W : Rat → Rat) (r k : Rat) : Prop :=
  ∃ (b : Bool) (lo hi c G : Rat), 0 ≤ lo ∧ lo < r ∧ r < hi ∧ 0 < G ∧
    0 < k ∧ k < 1 ∧ ∀ x, lo ≤ x → x ≤ hi →
      W (wallArm b x) = c - (k*G)*(x-r) ∧ W (wallArm (!b) x) = c - G*(x-r)

/-- Matching the two affine ordinates gives the unique contracted return throughout
the interval and the inverse law wherever both reversed heights belong to it. -/
theorem localWallReturn {W : Rat → Rat} {r k : Rat} (h : LocalWallRate W r k) :
    ∃ (b : Bool) (lo hi : Rat), lo < r ∧ r < hi ∧ 1 < 1/k ∧
      ∀ x, lo ≤ x → x ≤ hi →
        lo ≤ r+k*(x-r) ∧ r+k*(x-r) ≤ hi ∧
        ∀ y, lo ≤ y → y ≤ hi →
          (W (wallArm b x) = W (wallArm (!b) y) ↔ y = r+k*(x-r)) ∧
          (W (wallArm (!b) x) = W (wallArm b y) ↔ y = r+(x-r)/k) := by
  obtain ⟨b, lo, hi, c, G, _, hl, hh, hG, hk, hk', hf⟩ := h
  have forward (x y : Rat) (hx : lo ≤ x) (hx' : x ≤ hi) (hy : lo ≤ y) (hy' : y ≤ hi) :
      (W (wallArm b x) = W (wallArm (!b) y)) ↔ y = r+k*(x-r) := by
    rw [(hf x hx hx').1, (hf y hy hy').2]
    constructor
    · intro eqn
      have prod : G*(y-(r+k*(x-r))) = 0 := by grind only
      obtain hz | hz := Rat.mul_eq_zero.mp prod <;> grind only
    · intro h
      rw [h]
      grind only
  have inverse_law (x y : Rat) : (x = r+k*(y-r)) ↔ y = r+(x-r)/k := by
    have eqn := Rat.div_mul_cancel (a := x-r) (Rat.ne_of_gt hk)
    constructor
    · intro h
      have prod : k*(y-(r+(x-r)/k)) = 0 := by grind only
      obtain hz | hz := Rat.mul_eq_zero.mp prod <;> grind only
    · intro h
      rw [h]
      grind only
  refine ⟨b, lo, hi, hl, hh, (Rat.lt_div_iff hk).mpr (by grind only), ?_⟩
  intro x hx hx'
  have k0 := Rat.le_of_lt hk
  have k1 : 0 ≤ 1-k := by grind only
  have l₁ := Rat.mul_le_mul_of_nonneg_left hx k0
  have l₂ := Rat.mul_le_mul_of_nonneg_left (Rat.le_of_lt hl) k1
  have u₁ := Rat.mul_le_mul_of_nonneg_left hx' k0
  have u₂ := Rat.mul_le_mul_of_nonneg_left (Rat.le_of_lt hh) k1
  refine ⟨by grind only, by grind only, ?_⟩
  intro y hy hy'
  refine ⟨forward x y hx hx' hy hy', ?_⟩
  calc
    (W (wallArm (!b) x) = W (wallArm b y)) ↔ W (wallArm b y) = W (wallArm (!b) x) := eq_comm
    _ ↔ x = r+k*(y-r) := forward y x hy hy' hx hx'
    _ ↔ y = r+(x-r)/k := inverse_law x y

private theorem rate_preserved_by_cut {W : Rat → Rat} {r k p drop : Rat}
    (h : LocalWallRate W r k) (b : Bool) (hp : r < p) :
    LocalWallRate (signedWallCut W b p drop) r k := by
  obtain ⟨side, lo, hi, c, G, h0, hl, hh, hg, hk, hk', hf⟩ := h
  refine ⟨side, lo, min hi p, c, G, h0, hl, by grind, hg, hk, hk', ?_⟩
  intro x hx hx'
  have hx0 : 0 ≤ x := by grind only
  have hxp : x ≤ p := by grind
  rw [cut_before b side hx0 hxp, cut_before b (!side) hx0 hxp]
  exact hf x hx (by grind)

/-- The two exterior affine faces after any number of cuts. The outward derivative
on the side about to be cut is 'lead'; on the other side it is '-magnitude'. -/
structure SlopeFront where
  wall : Rat → Rat
  side : Bool
  root : Rat
  cut : Rat
  height : Rat
  lead : Rat
  magnitude : Rat
  cut_nonneg : 0 ≤ cut
  cut_le_root : cut ≤ root
  magnitude_pos : 0 < magnitude
  displacement_pos : 0 < lead+magnitude
  concave : WallConcave wall
  tails : ∀ y, cut ≤ y →
    wall (wallArm side y) = height + lead*(y-root) ∧
    wall (wallArm (!side) y) = height - magnitude*(y-root)

namespace SlopeFront

def initial : SlopeFront where
  wall t := t
  side := true
  root := 0
  cut := 0
  height := 0
  lead := 1
  magnitude := 1
  cut_nonneg := by decide
  cut_le_root := by decide
  magnitude_pos := by decide
  displacement_pos := by grind only
  concave := by intro x y q hq hq'; exact Rat.le_refl
  tails := by intro y _; simp [wallArm]; grind only

def crossing (F : SlopeFront) (s k : Rat) :=
  slopeCrossing F.root s (F.lead+F.magnitude) (F.magnitude/k-F.magnitude)

private theorem crossing_facts {F : SlopeFront} {s k : Rat}
    (hrs : F.root < s) (hk : 0 < k) (hk' : k < 1) :
    F.root < F.crossing s k ∧ F.crossing s k < s ∧
      (F.lead+F.magnitude)*(F.crossing s k-F.root) =
        -(F.magnitude/k-F.magnitude)*(F.crossing s k-s) := by
  have grow := (prescribedRateGrowth F.magnitude_pos hk hk').1
  exact prescribedSlopeCrossing hrs F.displacement_pos (by grind only)

/-- Insert the next prescribed root, keeping the previous portion of the wall untouched. -/
def advance (F : SlopeFront) (s k : Rat) (hrs : F.root < s) (hk : 0 < k)
    (hk' : k < 1) : SlopeFront := by
  let G := F.magnitude/k
  let p := F.crossing s k
  have grow : F.magnitude < G := (prescribedRateGrowth F.magnitude_pos hk hk').1
  obtain ⟨hleft, hright, hcross⟩ := crossing_facts hrs hk hk'
  change F.root < p at hleft
  change p < s at hright
  change (F.lead+F.magnitude)*(p-F.root) = -(G-F.magnitude)*(p-s) at hcross
  have hg := F.magnitude_pos
  have hgap := F.displacement_pos
  have hc0 := F.cut_nonneg
  have hcr := F.cut_le_root
  have hp : 0 ≤ p := by grind only
  refine {
    wall := signedWallCut F.wall F.side p (F.lead+G)
    side := !F.side
    root := s
    cut := p
    height := F.height - F.magnitude*(s-F.root)
    lead := -F.magnitude
    magnitude := G
    cut_nonneg := hp
    cut_le_root := Rat.le_of_lt hright
    magnitude_pos := by grind only
    displacement_pos := by grind only
    concave := signedWallCut_concave F.concave _ _ _ (by grind only)
    tails := ?_ }
  intro y hy
  have hyc : F.cut ≤ y := by grind only
  obtain ⟨top, bottom⟩ := F.tails y hyc
  obtain ⟨cutTop, cutBottom⟩ := cut_after (W := F.wall) (drop := F.lead+G) F.side hp hy
  simp only [Bool.not_not]
  rw [cutBottom, cutTop, top, bottom]
  constructor <;> grind only

/-- This is the signed alternation in physical height: consecutive cuts switch sides.
The old and new magnitudes on the next interval are exactly G and G/k. -/
theorem advance_geometry {F : SlopeFront} {s k : Rat} (hrs : F.root < s)
    (hk : 0 < k) (hk' : k < 1) :
    let F' := F.advance s k hrs hk hk'
    F.root < F'.cut ∧ F'.cut < s ∧ F'.side = !F.side ∧
      F'.lead = -F.magnitude ∧ F'.magnitude = F.magnitude/k ∧
      F.magnitude/F'.magnitude = k := by
  obtain ⟨hl, hr, _⟩ := crossing_facts hrs hk hk'
  exact ⟨hl, hr, rfl, rfl, rfl, (prescribedRateGrowth F.magnitude_pos hk hk').2⟩

/-- Slope of the signed physical displacement W(y)-W(-y) on the outer faces. -/
def displacementSlope (F : SlopeFront) : Rat :=
  if F.side then F.lead+F.magnitude else -(F.lead+F.magnitude)

theorem displacement_on_tail (F : SlopeFront) {y : Rat} (hy : F.cut ≤ y) :
    F.wall y - F.wall (-y) = F.displacementSlope*(y-F.root) := by
  obtain ⟨up, down⟩ := F.tails y hy
  cases side : F.side <;> simp [displacementSlope, side, wallArm] at up down ⊢ <;> grind only

/-- At each cut the two signed displacement lines meet, their slopes have opposite
signs, and the new slope has magnitude G/k-G. The initial displacement slope is 2. -/
theorem alternatingDisplacements {F : SlopeFront} {s k : Rat} (hrs : F.root < s)
    (hk : 0 < k) (hk' : k < 1) :
    let E := F.advance s k hrs hk hk'
    E.displacementSlope = (if F.side then -(F.magnitude/k-F.magnitude)
                          else F.magnitude/k-F.magnitude) ∧
    F.displacementSlope*E.displacementSlope < 0 ∧
    F.displacementSlope*(E.cut-F.root) = E.displacementSlope*(E.cut-s) := by
  let E := F.advance s k hrs hk hk'
  have key := (crossing_facts hrs hk hk').2.2
  change (F.lead+F.magnitude)*(E.cut-F.root) = -(F.magnitude/k-F.magnitude)*(E.cut-s) at key
  have grow := (prescribedRateGrowth F.magnitude_pos hk hk').1
  have hp := Rat.mul_pos F.displacement_pos (show 0 < F.magnitude/k-F.magnitude by grind only)
  change E.displacementSlope = _ ∧ F.displacementSlope*E.displacementSlope < 0 ∧
    F.displacementSlope*(E.cut-F.root) = E.displacementSlope*(E.cut-s)
  have es : E.side = !F.side := rfl
  have el : E.lead = -F.magnitude := rfl
  have eg : E.magnitude = F.magnitude/k := rfl
  unfold displacementSlope
  rw [es, el, eg]
  cases F.side <;> simp <;> grind only

theorem advance_localRate {F : SlopeFront} {s k : Rat} (hrs : F.root < s)
    (hk : 0 < k) (hk' : k < 1) :
    LocalWallRate (F.advance s k hrs hk hk').wall s k := by
  let F' := F.advance s k hrs hk hk'
  obtain ⟨_, hr, _, _, _, _⟩ := advance_geometry hrs hk hk'
  have hcancel := Rat.div_mul_cancel (a := F.magnitude) (Rat.ne_of_gt hk)
  refine ⟨F'.side, F'.cut, s+1, F'.height, F'.magnitude, F'.cut_nonneg, hr,
    by grind only, F'.magnitude_pos, hk, hk', ?_⟩
  intro x hx _
  obtain ⟨slow, fast⟩ := F'.tails x hx
  change F'.wall (wallArm F'.side x) = F'.height + -F.magnitude*(x-s) at slow
  change F'.wall (wallArm (!F'.side) x) = F'.height - F'.magnitude*(x-s) at fast
  have proportional : k*F'.magnitude = F.magnitude := by
    change k*(F.magnitude/k) = F.magnitude
    grind only
  rw [proportional]
  exact ⟨by grind only, fast⟩

end SlopeFront

private theorem arms_match (W : Rat → Rat) (b : Bool) (y : Rat) :
    (W y = W (-y)) ↔ W (wallArm b y) = W (wallArm (!b) y) := by
  cases b <;> simp [wallArm, eq_comm]

private theorem both_arms {W : Rat → Rat} {b : Bool} {y v : Rat}
    (h : W (wallArm b y) = v ∧ W (wallArm (!b) y) = v) :
    W y = v ∧ W (-y) = v := by
  cases b <;> simp [wallArm] at h <;> grind only

private theorem SlopeFront.match_on_tail (F : SlopeFront) {y : Rat} (hy : F.cut ≤ y) :
    (F.wall y = F.wall (-y)) ↔ y = F.root := by
  have hG := F.displacement_pos
  rw [arms_match F.wall F.side y, (F.tails y hy).1, (F.tails y hy).2]
  constructor
  · intro h
    have hz : (F.lead+F.magnitude)*(y-F.root) = 0 := by grind only
    obtain hz | hz := Rat.mul_eq_zero.mp hz <;> grind only
  · intro h
    rw [h]
    grind only

private theorem SlopeFront.advance_matches {F : SlopeFront} {s k y : Rat}
    (hrs : F.root < s) (hk : 0 < k) (hk' : k < 1) (hy : 0 ≤ y) :
    let F' := F.advance s k hrs hk hk'
    (F'.wall y = F'.wall (-y)) ↔ F.wall y = F.wall (-y) ∨ y = s := by
  let F' := F.advance s k hrs hk hk'
  obtain ⟨hl, hr, _, _, _, _⟩ := advance_geometry hrs hk hk'
  change F.root < F'.cut at hl
  change F'.cut < s at hr
  by_cases hcut : y ≤ F'.cut
  · have h1 := cut_before (W := F.wall) (drop := F.lead+F'.magnitude) F.side true hy hcut
    have h2 := cut_before (W := F.wall) (drop := F.lead+F'.magnitude) F.side false hy hcut
    change F'.wall y = F.wall y at h1
    change F'.wall (-y) = F.wall (-y) at h2
    change (F'.wall y = F'.wall (-y)) ↔ _
    rw [h1, h2]
    grind only
  · have old := F.match_on_tail (y := y) (by have := F.cut_le_root; grind only)
    have new := F'.match_on_tail (y := y) (by grind only)
    change (F'.wall y = F'.wall (-y)) ↔ y = s at new
    change (F'.wall y = F'.wall (-y)) ↔ _
    rw [new, old]
    grind only

/-- One raw (unnormalized) hinge, recorded in order of increasing absolute height. -/
structure WallJump where
  side : Bool
  radius : Rat
  drop : Rat

def applyWallJumps (W : Rat → Rat) : List WallJump → Rat → Rat
  | [] => W
  | j :: js => applyWallJumps (signedWallCut W j.side j.radius j.drop) js

/-- There is one alternating, strictly positive drop between successive target radii,
then a final drop at the neutral endpoint. -/
def InterlacedWallJumps (b : Bool) (prev : Rat) : List Rat → List WallJump → Prop
  | [], [j] => j.side = b ∧ j.radius = prev ∧ 0 < j.drop
  | r::rs, j::js => j.side = b ∧ prev < j.radius ∧ j.radius < r ∧ 0 < j.drop ∧
      InterlacedWallJumps (!b) r rs js
  | _, _ => False

/-- Data listed from the centre outwards, ending strictly before the neutral radius a. -/
def AdmissibleRates (prev a : Rat) : List (Rat × Rat) → Prop
  | [] => prev < a
  | (r,k)::rs => prev < r ∧ 0 < k ∧ k < 1 ∧ AdmissibleRates r a rs

/-- Iteration of G ↦ G/k over the prescribed rates. -/
def finalMagnitude (G : Rat) : List (Rat × Rat) → Rat
  | [] => G
  | (_,k)::rs => finalMagnitude (G/k) rs

private def SlopeFront.nextJump (F : SlopeFront) (s k : Rat) : WallJump :=
  ⟨F.side, F.crossing s k, F.lead+F.magnitude/k⟩

private structure RateConstruction (F : SlopeFront) (rs : List (Rat × Rat)) (a M : Rat) where
  jumps : List WallJump
  height : Rat
  placement : InterlacedWallJumps F.side F.root (rs.map Prod.fst ++ [a]) jumps
  scale_pos : 0 < M
  concave : WallConcave (applyWallJumps F.wall jumps)
  exterior : ∀ y, a ≤ y →
    applyWallJumps F.wall jumps y = height-M*(y-a) ∧
    applyWallJumps F.wall jumps (-y) = height-M*(y-a)
  rates : ∀ r k, (r,k) ∈ rs → LocalWallRate (applyWallJumps F.wall jumps) r k
  preserves : ∀ r k, r ≤ F.root → LocalWallRate F.wall r k →
    LocalWallRate (applyWallJumps F.wall jumps) r k
  levelSet : ∀ y, 0 ≤ y → y < a →
    ((applyWallJumps F.wall jumps y = applyWallJumps F.wall jumps (-y)) ↔
      F.wall y = F.wall (-y) ∨ ∃ k, (y,k) ∈ rs)

private theorem last_choice {G M : Rat} (hG : 0 < G) (hm : G < M) :
    0 < G/M ∧ G/M < 1 ∧ G/(G/M) = M := by
  have hp : 0 < M := by grind only
  have hq : 0 < G/M := (Rat.lt_div_iff hp).mpr (by grind only)
  have hq' : G/M < 1 := (Rat.div_lt_iff hp).mpr (by grind only)
  have prod := Rat.div_mul_cancel (a := G) (Rat.ne_of_gt hp)
  have eqn : M*(G/M) = G := by grind only
  refine ⟨hq, hq', ?_⟩
  calc
    G/(G/M) = (M*(G/M))/(G/M) := congrArg (fun z => z/(G/M)) eqn.symm
    _ = M := Rat.mul_div_cancel (Rat.ne_of_gt hq)

private def closeRateConstruction (F : SlopeFront) (a M : Rat) (hra : F.root < a)
    (hm : F.magnitude < M) : RateConstruction F [] a M := by
  let k := F.magnitude/M
  obtain ⟨hk, hk', hfinal⟩ := last_choice F.magnitude_pos hm
  let E := F.advance a k hra hk hk'
  let j := F.nextJump a k
  let z : WallJump := ⟨E.side, a, E.lead+E.magnitude⟩
  let raw := signedWallCut E.wall z.side z.radius z.drop
  have em : E.magnitude = M := hfinal
  obtain ⟨hl, hr, _, _, _, _⟩ := SlopeFront.advance_geometry hra hk hk'
  change F.root < E.cut at hl
  change E.cut < a at hr
  have gap := F.displacement_pos
  have hG := F.magnitude_pos
  have a0 : 0 ≤ a := by have := F.cut_nonneg; have := F.cut_le_root; grind only
  refine {
    jumps := [j, z]
    height := E.height
    placement := ⟨rfl, hl, hr, ?_, rfl, rfl, E.displacement_pos⟩
    scale_pos := by grind only
    concave := signedWallCut_concave E.concave _ _ _ (Rat.le_of_lt E.displacement_pos)
    exterior := ?_
    rates := by simp
    preserves := ?_
    levelSet := ?_ }
  · change 0 < F.lead+E.magnitude
    grind only
  · intro y hy
    change raw y = E.height-M*(y-a) ∧ raw (-y) = E.height-M*(y-a)
    apply both_arms (b := E.side)
    obtain ⟨u,v⟩ := E.tails y (by grind only)
    obtain ⟨h1,h2⟩ := cut_after (W := E.wall) (drop := E.lead+E.magnitude) E.side a0 hy
    change raw (wallArm E.side y) = E.wall (wallArm E.side y) - (E.lead+E.magnitude)*(y-a) at h1
    change raw (wallArm (!E.side) y) = E.wall (wallArm (!E.side) y) at h2
    change E.wall (wallArm E.side y) = E.height+E.lead*(y-a) at u
    change E.wall (wallArm (!E.side) y) = E.height-E.magnitude*(y-a) at v
    rw [h1,h2,u,v,em]
    constructor <;> grind only
  · intro r k' hr' h
    apply rate_preserved_by_cut (p := a) _ z.side (by grind only)
    apply rate_preserved_by_cut h F.side
    change r < E.cut
    grind only
  · intro y hy hya
    change (raw y = raw (-y)) ↔ _
    have h1 := cut_before (W := E.wall) (drop := z.drop) z.side true hy (Rat.le_of_lt hya)
    have h2 := cut_before (W := E.wall) (drop := z.drop) z.side false hy (Rat.le_of_lt hya)
    change raw y = E.wall y at h1
    change raw (-y) = E.wall (-y) at h2
    have he := SlopeFront.advance_matches hra hk hk' hy
    change (E.wall y = E.wall (-y)) ↔ F.wall y = F.wall (-y) ∨ y = a at he
    rw [h1, h2, he]
    simp
    grind only

private theorem root_mem_cons {y r k : Rat} {rs : List (Rat × Rat)} :
    (∃ q, (y,q) ∈ (r,k)::rs) ↔ y=r ∨ ∃ q, (y,q) ∈ rs := by
  constructor
  · rintro ⟨q, h⟩
    rcases List.mem_cons.mp h with eqn | hin
    · exact Or.inl (congrArg Prod.fst eqn)
    · exact Or.inr ⟨q, hin⟩
  · rintro (rfl | ⟨q, hin⟩)
    · exact ⟨k, .head ..⟩
    · exact ⟨q, .tail _ hin⟩

private def buildRateConstruction (F : SlopeFront) (a M : Rat) (rs : List (Rat × Rat))
    (h : AdmissibleRates F.root a rs) (hm : finalMagnitude F.magnitude rs < M) :
    RateConstruction F rs a M :=
  match rs with
  | [] => closeRateConstruction F a M h hm
  | (s,k)::rest => by
    obtain ⟨hs, hk, hk', hr⟩ := h
    let E := F.advance s k hs hk hk'
    let j := F.nextJump s k
    let tail := buildRateConstruction E a M rest hr hm
    obtain ⟨hl, hcut, _, _, _, _⟩ := SlopeFront.advance_geometry hs hk hk'
    change F.root < E.cut at hl
    change E.cut < s at hcut
    have grow := (prescribedRateGrowth F.magnitude_pos hk hk').1
    have hgap := F.displacement_pos
    refine {
      jumps := j::tail.jumps
      height := tail.height
      placement := ⟨rfl, hl, hcut, by change 0 < F.lead+F.magnitude/k; grind only,
        tail.placement⟩
      scale_pos := tail.scale_pos
      concave := tail.concave
      exterior := tail.exterior
      rates := ?_
      preserves := ?_
      levelSet := ?_ }
    · intro r q hin
      rcases List.mem_cons.mp hin with eqn | hin
      · cases eqn
        exact tail.preserves _ _ Rat.le_refl (SlopeFront.advance_localRate hs hk hk')
      · exact tail.rates _ _ hin
    · intro r q hfr rate
      apply tail.preserves r q (by change r ≤ s; grind only)
      apply rate_preserved_by_cut rate F.side
      change r < E.cut
      grind only
    · intro y hy hya
      rw [root_mem_cons]
      change (applyWallJumps E.wall tail.jumps y = applyWallJumps E.wall tail.jumps (-y)) ↔ _
      have he := SlopeFront.advance_matches hs hk hk' hy
      change (E.wall y = E.wall (-y)) ↔ F.wall y = F.wall (-y) ∨ y = s at he
      rw [tail.levelSet y hy hya, he]
      grind only

private theorem jump_count {roots : List Rat} {jumps : List WallJump} {b : Bool} {p : Rat}
    (shape : InterlacedWallJumps b p roots jumps) : jumps.length = roots.length+1 := by
  induction roots generalizing jumps b p with
  | nil =>
    cases jumps with
    | nil => contradiction
    | cons j rest =>
      cases rest with
      | nil => rfl
      | cons k rest => contradiction
  | cons r rest ih =>
    cases jumps with
    | nil => contradiction
    | cons j js =>
      have h := ih shape.2.2.2.2
      simp only [List.length_cons]
      omega

private theorem cutoff_above {prev a : Rat} {rs : List (Rat × Rat)}
    (h : AdmissibleRates prev a rs) : prev < a := by
  induction rs generalizing prev with
  | nil => exact h
  | cons pair rest ih =>
    obtain ⟨r,k⟩ := pair
    obtain ⟨hr, _, _, ht⟩ := h
    have h' := ih ht
    grind only

/-- Translate and scale a raw rational wall to the physical outer faces. -/
def normalizeRightWall (a c M : Rat) (W : Rat → Rat) (t : Rat) : Rat :=
  1-a+(W t-c)/M

private theorem normalize_concave {a c M : Rat} {W : Rat → Rat}
    (hM : 0 < M) (hW : WallConcave W) : WallConcave (normalizeRightWall a c M W) := by
  intro x y q hq hq'
  have hinv := Rat.le_of_lt (Rat.inv_pos.mpr hM)
  have hw := Rat.mul_le_mul_of_nonneg_right (hW x y q hq hq') hinv
  unfold normalizeRightWall
  simp only [Rat.div_def]
  grind only

private theorem normalize_rate {a c M r k : Rat} {W : Rat → Rat}
    (hM : 0 < M) (h : LocalWallRate W r k) : LocalWallRate (normalizeRightWall a c M W) r k := by
  obtain ⟨b, lo, hi, v, G, h0, hl, hh, hg, hk, hk', hf⟩ := h
  have gp : 0 < G/M := (Rat.lt_div_iff hM).mpr (by grind only)
  refine ⟨b, lo, hi, 1-a+(v-c)/M, G/M, h0, hl, hh, gp, hk, hk', ?_⟩
  intro x hx hx'
  obtain ⟨h₁,h₂⟩ := hf x hx hx'
  unfold normalizeRightWall
  rw [h₁, h₂]
  simp only [Rat.div_def]
  constructor <;> grind only

private theorem normalize_match {a c M y : Rat} {W : Rat → Rat} (hm : 0 < M) :
    (normalizeRightWall a c M W y = normalizeRightWall a c M W (-y)) ↔ W y = W (-y) := by
  unfold normalizeRightWall
  constructor
  · intro h
    have e : (W y-c)/M = (W (-y)-c)/M := by grind only
    have e' := congrArg (fun t : Rat => t*M) e
    simp only [Rat.div_mul_cancel (Rat.ne_of_gt hm)] at e'
    grind only
  · intro h
    rw [h]

private theorem above_chord {a t : Rat} {W : Rat → Rat} (ha : 0 < a) (hW : WallConcave W)
    (hwall : W a = 1-a ∧ W (-a) = 1-a) (hl : -a ≤ t) (hu : t ≤ a) :
    1-a ≤ W t := by
  let q := (t+a)/(2*a)
  have hpair : 0 < 2*a := by grind only
  have eqn : q*(2*a) = t+a := Rat.div_mul_cancel (Rat.ne_of_gt hpair)
  have h0 : 0 ≤ q := Rat.le_of_mul_le_mul_right (c := 2*a) (by grind only) hpair
  have h1 : q ≤ 1 := Rat.le_of_mul_le_mul_right (c := 2*a) (by grind only) hpair
  have eqt : q*a+(1-q)*(-a) = t := by grind only
  have chord := hW a (-a) q h0 h1
  rw [eqt, hwall.1, hwall.2] at chord
  grind only

/-- For every finite ordered list of rational locations and contraction factors, the
explicit alternating hinges give a concave right wall. Its isolated positive matching
heights and their local attracting rates are exactly the input, and its outer branches
are the two neutral faces. The crossing list includes the final cut at a. -/
theorem prescribedRateWall {a M : Rat} {rs : List (Rat × Rat)}
    (h : AdmissibleRates 0 a rs) (ha : a < 1) (hm : finalMagnitude 1 rs < M) :
    ∃ (js : List WallJump) (c : Rat),
      let W := normalizeRightWall a c M (applyWallJumps id js)
      InterlacedWallJumps true 0 (rs.map Prod.fst ++ [a]) js ∧
      js.length = rs.length + 2 ∧ WallConcave W ∧
      (∀ y, a ≤ y → W y = 1-y ∧ W (-y) = 1-y) ∧
      (∀ t, -a ≤ t → t ≤ a → 0 < W t ∧ 1-a ≤ W t) ∧
      (∀ r k, (r,k) ∈ rs → LocalWallRate W r k) ∧
      (∀ y, 0 < y → y < a → (W y = W (-y) ↔ ∃ k, (y,k) ∈ rs)) := by
  let result := buildRateConstruction SlopeFront.initial a M rs h hm
  let raw := applyWallJumps SlopeFront.initial.wall result.jumps
  let W := normalizeRightWall a result.height M raw
  have hW : WallConcave W := normalize_concave result.scale_pos result.concave
  have hM := result.scale_pos
  have hInv := Rat.mul_inv_cancel M (Rat.ne_of_gt hM)
  have outer (y : Rat) (hy : a ≤ y) : W y = 1-y ∧ W (-y) = 1-y := by
    obtain ⟨u,v⟩ := result.exterior y hy
    change raw y = result.height-M*(y-a) at u
    change raw (-y) = result.height-M*(y-a) at v
    unfold W normalizeRightWall
    rw [u,v]
    simp only [Rat.div_def]
    constructor <;> grind only
  refine ⟨result.jumps, result.height, result.placement, ?_, hW, outer, ?_, ?_, ?_⟩
  · have count := jump_count result.placement
    simpa only [List.length_append, List.length_map, List.length_cons, List.length_nil] using count
  · intro t hl hu
    change 0 < W t ∧ 1-a ≤ W t
    have ht := above_chord (cutoff_above h) hW (outer a Rat.le_refl) hl hu
    exact ⟨by grind only, ht⟩
  · intro r k hr
    exact normalize_rate hM (result.rates r k hr)
  · intro y hy hya
    change (W y = W (-y)) ↔ _
    rw [show (W y = W (-y)) ↔ raw y = raw (-y) from normalize_match hM]
    have lev := result.levelSet y (Rat.le_of_lt hy) hya
    change (raw y = raw (-y)) ↔ y = -y ∨ ∃ k, (y,k) ∈ rs at lev
    rw [lev]
    grind only

/-! The centrally symmetric octagon realizing the lower side count. -/

open Uncloakability (rightWall)

/-- Reflection of the right graph in the center of the octagon. -/
def octagonLeft (t : Rat) : Rat := -rightWall (-t)

def InCentralOctagon (u t : Rat) : Prop :=
  t.abs ≤ 1 ∧ octagonLeft t ≤ u ∧ u ≤ rightWall t

def OnCentralOctagon (u t : Rat) : Prop :=
  t.abs ≤ 1 ∧ (u = octagonLeft t ∨ u = rightWall t)

theorem centralOctagonSymmetry (u t : Rat) :
    (InCentralOctagon (-u) (-t) ↔ InCentralOctagon u t) ∧
    (OnCentralOctagon (-u) (-t) ↔ OnCentralOctagon u t) := by
  simp only [InCentralOctagon, OnCentralOctagon, octagonLeft, Rat.abs_neg, Rat.neg_neg]
  grind only

/-- The four supporting lines on each wall, including both endpoints at a join.
Restricting these equivalences to −1 ≤ t ≤ 1 gives eight nonempty faces. -/
theorem centralOctagonFaceRanges (t : Rat) :
    (rightWall t = 1+t ↔ t ≤ -1/2) ∧
    (rightWall t = 2/3+t/3 ↔ -1/2 ≤ t ∧ t ≤ 1/12) ∧
    (rightWall t = 3/4-2*t/3 ↔ 1/12 ≤ t ∧ t ≤ 3/4) ∧
    (rightWall t = 1-t ↔ 3/4 ≤ t) ∧
    (octagonLeft t = -1-t ↔ t ≤ -3/4) ∧
    (octagonLeft t = -3/4-2*t/3 ↔ -3/4 ≤ t ∧ t ≤ -1/12) ∧
    (octagonLeft t = -2/3+t/3 ↔ -1/12 ≤ t ∧ t ≤ 1/2) ∧
    (octagonLeft t = t-1 ↔ 1/2 ≤ t) := by
  have formulas (v : Rat) :
      (rightWall v = 1+v ↔ v ≤ -1/2) ∧
      (rightWall v = 2/3+v/3 ↔ -1/2 ≤ v ∧ v ≤ 1/12) ∧
      (rightWall v = 3/4-2*v/3 ↔ 1/12 ≤ v ∧ v ≤ 3/4) ∧
      (rightWall v = 1-v ↔ 3/4 ≤ v) := by
    grind only [rightWall, Rat.abs, Rat.min_def]
  have hr := formulas t
  have hl := formulas (-t)
  simp only [octagonLeft]
  grind only

/-- The vertices, in boundary order starting at the lower tip. -/
def centralOctagonVertices : List (Rat × Rat) :=
  [(0,-1), (1/2,-1/2), (25/36,1/12), (1/4,3/4),
   (0,1), (-1/2,1/2), (-25/36,-1/12), (-1/4,-3/4)]

theorem centralOctagonEightDistinctVertices :
    centralOctagonVertices.length = 8 ∧ centralOctagonVertices.Nodup ∧
    [(rightWall (-1), (-1 : Rat)), (rightWall (-1/2), -1/2), (rightWall (1/12), 1/12),
     (rightWall (3/4), 3/4), (rightWall 1, 1), (octagonLeft (1/2), 1/2),
     (octagonLeft (-1/12), -1/12), (octagonLeft (-3/4), -3/4)] = centralOctagonVertices := by
  decide +kernel

/-- The four pairs of parallel supporting half-planes. They give convexity
directly and identify the active constraints at every listed vertex. -/
theorem centralOctagonStrips (u t : Rat) :
    InCentralOctagon u t ↔
      (-1 ≤ u-t ∧ u-t ≤ 1) ∧ (-2/3 ≤ u-t/3 ∧ u-t/3 ≤ 2/3) ∧
      (-3/4 ≤ u+2*t/3 ∧ u+2*t/3 ≤ 3/4) ∧ (-1 ≤ u+t ∧ u+t ≤ 1) := by
  have upper (x y : Rat) : x ≤ rightWall y ↔
      x ≤ 1+y ∧ x ≤ 2/3+y/3 ∧ x ≤ 3/4-2*y/3 ∧ x ≤ 1-y := by
    grind only [rightWall, Rat.abs, Rat.min_def]
  simp only [InCentralOctagon, octagonLeft,
    show -rightWall (-t) ≤ u ↔ -u ≤ rightWall (-t) by grind only, upper]
  grind (splits := 12) only [Rat.abs]

/-- A point is extreme if it is the midpoint of no nonconstant segment in the
polygon, expressed here in rational characteristic coordinates. -/
def IsCentralOctagonExtreme (u t : Rat) : Prop :=
  InCentralOctagon u t ∧ ∀ a b, InCentralOctagon (u+a) (t+b) →
    InCentralOctagon (u-a) (t-b) → a = 0 ∧ b = 0

private theorem centralRightIn {t : Rat} (h : t.abs ≤ 1) :
    InCentralOctagon (rightWall t) t := by
  grind only [InCentralOctagon, rightWall, octagonLeft, Rat.abs, Rat.min_def]

private theorem centralFaceNotExtreme {t lo hi slope offset : Rat}
    (hl : lo < t) (hr : t < hi)
    (face : ∀ v, lo ≤ v → v ≤ hi → InCentralOctagon (slope*v+offset) v) :
    ¬ IsCentralOctagonExtreme (slope*t+offset) t := by
  intro ex
  let δ := min (t-lo) (hi-t)
  have hd : 0 < δ := by grind only [Rat.min_def]
  have pos := face (t+δ) (by grind only [Rat.min_def]) (by grind only [Rat.min_def])
  have neg := face (t-δ) (by grind only [Rat.min_def]) (by grind only [Rat.min_def])
  have h := ex.2 (slope*δ) δ
    (by rw [show slope*t+offset+slope*δ = slope*(t+δ)+offset by grind only]; exact pos)
    (by rw [show slope*t+offset-slope*δ = slope*(t-δ)+offset by grind only]; exact neg)
  grind only

private theorem rightExtremeHeight {t : Rat} (he : IsCentralOctagonExtreme (rightWall t) t) :
    t = -1 ∨ t = -1/2 ∨ t = 1/12 ∨ t = 3/4 ∨ t = 1 := by
  have ht := he.1.1
  have face (lo hi g c : Rat) (hl : lo < t) (hr : t < hi)
      (inside : ∀ v : Rat, lo ≤ v → v ≤ hi → v.abs ≤ 1)
      (wall : ∀ v : Rat, lo ≤ v → v ≤ hi → rightWall v = g*v+c) : False := by
    have bad := centralFaceNotExtreme hl hr (fun v hv hw =>
      wall v hv hw ▸ centralRightIn (inside v hv hw))
    exact bad (wall t (Rat.le_of_lt hl) (Rat.le_of_lt hr) ▸ he)
  by_cases h₀ : t = -1 ∨ t = -1/2 ∨ t = 1/12 ∨ t = 3/4 ∨ t = 1
  · exact h₀
  · exfalso
    by_cases ha : t < -1/2
    · apply face (-1) (-1/2) 1 1 (by grind only [Rat.abs]) ha
      · intro v hv hw; grind only [Rat.abs]
      · intro v hv hw; have eq := (centralOctagonFaceRanges v).1.mpr hw; grind only
    by_cases hb : t < 1/12
    · apply face (-1/2) (1/12) (1/3) (2/3) (by grind only) hb
      · intro v hv hw; grind only [Rat.abs]
      · intro v hv hw; have eq := (centralOctagonFaceRanges v).2.1.mpr ⟨hv, hw⟩; grind only
    by_cases hc : t < 3/4
    · apply face (1/12) (3/4) (-2/3) (3/4) (by grind only) hc
      · intro v hv hw; grind only [Rat.abs]
      · intro v hv hw; have eq := (centralOctagonFaceRanges v).2.2.1.mpr ⟨hv, hw⟩; grind only
    · apply face (3/4) 1 (-1) 1 (by grind only) (by grind only [Rat.abs])
      · intro v hv hw; grind only [Rat.abs]
      · intro v hv hw; have eq := (centralOctagonFaceRanges v).2.2.2.1.mpr hv; grind only

private theorem octagonExtremeReflected {u t : Rat} (h : IsCentralOctagonExtreme u t) :
    IsCentralOctagonExtreme (-u) (-t) := by
  refine ⟨(centralOctagonSymmetry u t).1.mpr h.1, ?_⟩
  intro a b pos neg
  have p := (centralOctagonSymmetry (u+a) (t+b)).1.mp (by
    rw [show -(u+a) = -u-a by grind only, show -(t+b) = -t-b by grind only]
    exact neg)
  have n := (centralOctagonSymmetry (u-a) (t-b)).1.mp (by
    rw [show -(u-a) = -u+a by grind only, show -(t-b) = -t+b by grind only]
    exact pos)
  exact h.2 a b p n

/-- The listed eight points are exactly the geometric extreme points. Inside a
face a short segment parallel to that face witnesses failure of extremality.
At each vertex two independent strip constraints rule out such a segment. -/
theorem centralOctagonExtremeIffVertex (u t : Rat) :
    IsCentralOctagonExtreme u t ↔ (u,t) ∈ centralOctagonVertices := by
  constructor
  · intro ex
    have reg := ex.1
    have onwall : u = octagonLeft t ∨ u = rightWall t := by
      by_cases h : u = octagonLeft t ∨ u = rightWall t
      · exact h
      · exfalso
        let δ := min (u-octagonLeft t) (rightWall t-u)
        have hIn := reg
        simp only [InCentralOctagon] at hIn
        have hd : 0 < δ := by grind only [Rat.min_def]
        have hp : InCentralOctagon (u+δ) (t+0) := by
          simp only [InCentralOctagon, Rat.add_zero]
          grind only [Rat.min_def]
        have hm : InCentralOctagon (u-δ) (t-0) := by
          simp only [InCentralOctagon, show t-0=t by grind only]
          grind only [Rat.min_def]
        have := ex.2 δ 0 hp hm
        grind only
    rcases onwall with hv | hv
    · obtain rfl : u = octagonLeft t := hv
      have he := octagonExtremeReflected ex
      simp only [octagonLeft, Rat.neg_neg] at he
      have hb := rightExtremeHeight he
      have heights : t = 1 ∨ t = 1/2 ∨ t = -1/12 ∨ t = -3/4 ∨ t = -1 := by grind only
      rcases heights with rfl | rfl | rfl | rfl | rfl <;> decide +kernel
    · obtain rfl : u = rightWall t := hv
      rcases rightExtremeHeight ex with rfl | rfl | rfl | rfl | rfl <;> decide +kernel
  · intro hm
    simp only [centralOctagonVertices, List.mem_cons, List.not_mem_nil, or_false,
      Prod.mk.injEq] at hm
    rcases hm with h | h | h | h | h | h | h | h <;> rcases h with ⟨rfl, rfl⟩
    all_goals
      refine ⟨by unfold InCentralOctagon; decide +kernel, ?_⟩
      intro a b pos neg
      have hp := (centralOctagonStrips _ _).mp pos
      have hn := (centralOctagonStrips _ _).mp neg
      grind only

/-- Each of the two entries is an endpoint, they are distinct, and the line
meets the entire polygon boundary only at those two coordinates. -/
def OctagonChord (fiber : Rat → Prop) (a b : Rat) : Prop :=
  a ≠ b ∧ ∀ w, fiber w ↔ w = a ∨ w = b

private theorem swapOctagonChord {p : Rat → Prop} {a b : Rat} (h : OctagonChord p a b) :
    OctagonChord p b a := by
  refine ⟨Ne.symm h.1, fun w => (h.2 w).trans or_comm⟩

private theorem otherOctagonEndpoint {p : Rat → Prop} {a b c : Rat}
    (h : OctagonChord p a b) (k : OctagonChord p a c) : b = c :=
  ((k.2 b).mp ((h.2 b).mpr (Or.inr rfl))).resolve_left (Ne.symm h.1)

private theorem octagonWallSigns {t : Rat} (h : t.abs < 1) :
    octagonLeft t < 0 ∧ 0 < rightWall t := by
  have pos (v : Rat) (hv : v.abs < 1) : 0 < rightWall v := by
    grind only [rightWall, Rat.abs, Rat.min_def]
  have h₁ := pos t h
  have h₂ := pos (-t) (by simpa only [Rat.abs_neg] using h)
  grind only [octagonLeft]

private theorem octagonHorizontal {t : Rat} (h : t.abs < 1) :
    OctagonChord (fun u => OnCentralOctagon u t) (octagonLeft t) (rightWall t) := by
  have hsign := octagonWallSigns h
  constructor
  · grind only
  · intro w
    constructor
    · exact And.right
    · exact fun hw => ⟨Rat.le_of_lt h, hw⟩

private theorem octagonReflectColumn {s a b : Rat}
    (h : OctagonChord (OnCentralOctagon s) a b) :
    OctagonChord (OnCentralOctagon (-s)) (-a) (-b) := by
  constructor
  · intro eq
    apply h.1
    grind only
  · intro w
    have hr := (centralOctagonSymmetry s (-w)).2
    simp only [Rat.neg_neg] at hr
    rw [hr, h.2 (-w)]
    grind only

/-- A physical four-leg itinerary, with several coordinates shared by construction.
Launch and landing are on the lower left wall at heights −y and −z. -/
structure OctagonFourLegs (y s t l z : Rat) : Prop where
  lower : OctagonChord (fun u => OnCentralOctagon u (-y)) (octagonLeft (-y)) s
  right : OctagonChord (OnCentralOctagon s) (-y) t
  upper : OctagonChord (fun u => OnCentralOctagon u t) s l
  left : OctagonChord (OnCentralOctagon l) t (-z)
  landing : l = octagonLeft (-z)

def CentralOctagonReturn (y z : Rat) : Prop := ∃ s t l, OctagonFourLegs y s t l z

private theorem octagonLandingUnique {y z z' : Rat} (h : CentralOctagonReturn y z)
    (k : CentralOctagonReturn y z') : z = z' := by
  obtain ⟨s, t, l, p⟩ := h
  obtain ⟨s', t', l', q⟩ := k
  obtain rfl : s = s' := otherOctagonEndpoint p.lower q.lower
  obtain rfl : t = t' := otherOctagonEndpoint p.right q.right
  obtain rfl : l = l' := otherOctagonEndpoint p.upper q.upper
  have he := otherOctagonEndpoint p.left q.left
  grind only

/-- The column through a positive right-wall coordinate cannot meet the left
wall. Its complete fiber follows from the two roots of the right graph. -/
private theorem octagonPositiveColumn {y w : Rat}
    (hy : 0 < y) (hy' : y < 1) (hw : 0 < w) (hw' : w < 1)
    (roots : ∀ t, rightWall t = rightWall (-y) ↔ t = -y ∨ t = w) :
    rightWall (-y) = rightWall w ∧
    OctagonChord (OnCentralOctagon (rightWall (-y))) (-y) w := by
  have he := ((roots w).mpr (Or.inr rfl)).symm
  have hr := (octagonWallSigns (t := -y) (by grind only [Rat.abs])).2
  refine ⟨he, by grind only, ?_⟩
  intro t
  constructor
  · intro h
    have hbound := h.1
    have hleft : octagonLeft t ≤ 0 := by
      grind only [octagonLeft, rightWall, Rat.abs, Rat.min_def]
    have eq : rightWall (-y) = rightWall t := h.2.resolve_left (by grind only)
    exact (roots t).mp eq.symm
  · rintro (rfl | rfl)
    · exact ⟨by grind only [Rat.abs], Or.inr rfl⟩
    · exact ⟨by grind only [Rat.abs], Or.inr he⟩

private theorem octagonComposeColumns {y t z : Rat} (hy : 0 < y) (hy' : y < 1)
    (ht : 0 < t) (ht' : t < 1)
    (right : rightWall (-y) = rightWall t ∧
      OctagonChord (OnCentralOctagon (rightWall (-y))) (-y) t)
    (reflected : rightWall (-t) = rightWall z ∧
      OctagonChord (OnCentralOctagon (rightWall (-t))) (-t) z) :
    OctagonFourLegs y (rightWall (-y)) t (octagonLeft t) z := by
  refine ⟨octagonHorizontal (by grind only [Rat.abs]), right.2, ?_, ?_, ?_⟩
  · rw [right.1]
    exact swapOctagonChord (octagonHorizontal (by grind only [Rat.abs]))
  · simpa only [octagonLeft, Rat.neg_neg] using octagonReflectColumn reflected.2
  · simp only [octagonLeft, Rat.neg_neg, reflected.1]

/-- Every height in the open outer band gives an actual rectangle, with all
four boundary fibers enumerated. Its four-leg return fixes the whole band. -/
theorem centralOctagonNeutralCylinder {y : Rat} (hy : 3/4 < y) (hy' : y < 1) :
    OctagonFourLegs y (1-y) y (y-1) y ∧
      ∀ z, CentralOctagonReturn y z ↔ z = y := by
  have heu : rightWall (-y) = 1-y := by
    have h := (Uncloakability.hexagonWallBounds (-y)).1 (by grind only [Rat.abs])
    grind only [Rat.abs]
  have hel : octagonLeft y = y-1 := by rw [octagonLeft, heu]; grind only
  have roots (t : Rat) : rightWall t = rightWall (-y) ↔ t = -y ∨ t = y := by
    rw [heu]
    grind only [rightWall, Rat.abs, Rat.min_def]
  have col := octagonPositiveColumn (by grind only : 0 < y) hy' (by grind only : 0 < y) hy' roots
  have legs := octagonComposeColumns (by grind only : 0 < y) hy' (by grind only : 0 < y) hy' col col
  rw [heu, hel] at legs
  have closed : CentralOctagonReturn y y := ⟨_, _, _, legs⟩
  exact ⟨legs, fun _ => ⟨fun hz => octagonLandingUnique hz closed, fun e => e ▸ closed⟩⟩

private def octagonHalfStep (y : Rat) : Rat := 1/8+y/2

private theorem octagonInnerColumn {y : Rat} (hy : 0 < y) (hy' : y < 1/2) :
    rightWall (-y) = rightWall (octagonHalfStep y) ∧
    OctagonChord (OnCentralOctagon (rightWall (-y))) (-y) (octagonHalfStep y) := by
  apply octagonPositiveColumn hy (by grind only) (by grind only [octagonHalfStep])
    (by grind only [octagonHalfStep])
  intro t
  have heu : rightWall (-y) = 2/3-y/3 := by grind only [rightWall, Rat.abs, Rat.min_def]
  rw [heu]
  grind only [rightWall, octagonHalfStep, Rat.abs, Rat.min_def]

/-- The complete local return on the lower left section. The two vertical
flights, after reflection in the center, each apply y ↦ 1/8+y/2. -/
theorem centralOctagonLocalReturn {y z : Rat} (hy : 0 < y) (hy' : y < 1/2) :
    CentralOctagonReturn y z ↔ z = 3/16+y/4 := by
  have ht : 0 < octagonHalfStep y := by grind only [octagonHalfStep]
  have ht' : octagonHalfStep y < 1/2 := by grind only [octagonHalfStep]
  have legs := octagonComposeColumns hy (by grind only) ht (by grind only)
    (octagonInnerColumn hy hy') (octagonInnerColumn ht ht')
  have eq : octagonHalfStep (octagonHalfStep y) = 3/16+y/4 := by grind only [octagonHalfStep]
  rw [eq] at legs
  have hit : CentralOctagonReturn y (3/16+y/4) := ⟨_, _, _, legs⟩
  exact ⟨fun h => octagonLandingUnique h hit, fun e => e ▸ hit⟩

/-- Coordinates of all four impacts at the isolated fixed point, its uniqueness
on the local section, and the exact affine multiplier throughout that section. -/
theorem centralOctagonAttractingRectangle :
    OctagonFourLegs (1/4) (7/12) (1/4) (-7/12) (1/4) ∧
    ∀ y, 0 < y → y < 1/2 →
      (CentralOctagonReturn y y ↔ y = 1/4) ∧
        ∀ z, CentralOctagonReturn y z → z - 1/4 = (1/4)*(y-1/4) := by
  constructor
  · have col := octagonInnerColumn (y := 1/4) (by decide +kernel) (by decide +kernel)
    rw [show octagonHalfStep (1/4) = 1/4 by decide +kernel] at col
    have legs := octagonComposeColumns (by decide +kernel : (0:Rat)<1/4)
      (by decide +kernel) (by decide +kernel : (0:Rat)<1/4) (by decide +kernel) col col
    rwa [show rightWall (-(1/4)) = 7/12 by decide +kernel,
      show octagonLeft (1/4) = -7/12 by decide +kernel] at legs
  · intro y hy hy'
    constructor
    · rw [centralOctagonLocalReturn hy hy']
      grind only
    · intro z h
      rw [(centralOctagonLocalReturn hy hy').mp h]
      grind only

end MultiplicityBounds
