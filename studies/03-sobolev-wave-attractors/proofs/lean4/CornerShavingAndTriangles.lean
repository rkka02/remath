import Std

/-!
The triangle obstruction, the rational form of the shrinking-shell energy argument,
and the separation estimates for the shaved square (phase1_pde.md, Theorems 3, 4b).
Phase lifts have circumference two. All positions and slopes below are exact.
-/
namespace CornerShavingAndTriangles

/-- Both inequalities are weak, so a vertex on an entire extreme edge is included. -/
def Extremal {n : Nat} (f : Fin n → Rat) (v : Fin n) : Prop :=
  (∀ i, f v ≤ f i) ∨ (∀ i, f i ≤ f v)

theorem triangle_common_extremum (ξ η : Fin 3 → Rat) :
    ∃ v, Extremal ξ v ∧ Extremal η v := by
  simp only [Extremal, Fin.exists_fin_succ, Fin.exists_fin_zero, Fin.forall_fin_succ,
    Fin.forall_fin_zero, Rat.le_refl, true_and, and_true, or_false]
  grind only

private theorem distinct_extrema (f : Fin 4 → Rat) :
    ∃ v w, v ≠ w ∧ Extremal f v ∧ Extremal f w := by
  simp only [Extremal, Fin.exists_fin_succ, Fin.exists_fin_zero, Fin.forall_fin_succ,
    Fin.forall_fin_zero, Rat.le_refl, true_and, and_true, or_false,
    Fin.succ_inj, ne_eq]
  grind only

/-- On a characteristic edge one projection has a tied extremum. Its
extreme vertices must meet those of the other projection on four vertices. -/
theorem characteristic_quadrilateral_extremum (ξ η : Fin 4 → Rat) (v w : Fin 4)
    (different : v ≠ w) (tie : ξ v = ξ w) (face : Extremal ξ v) :
    ∃ i, Extremal ξ i ∧ Extremal η i := by
  have faceW : Extremal ξ w := by simpa only [Extremal, ← tie] using face
  have three (i j : Fin 4) (ne : i ≠ j) : Extremal ξ i ∨ Extremal ξ j := by
    by_cases hi : Extremal ξ i
    · exact Or.inl hi
    by_cases hj : Extremal ξ j
    · exact Or.inr hj
    have iv : i ≠ v := fun e => hi (e ▸ face)
    have iw : i ≠ w := fun e => hi (e ▸ faceW)
    have jv : j ≠ v := fun e => hj (e ▸ face)
    have jw : j ≠ w := fun e => hj (e ▸ faceW)
    have cover (z : Fin 4) : z = v ∨ z = w ∨ z = i ∨ z = j := by
      simp only [ne_eq, Fin.ext_iff] at different ne iv iw jv jw ⊢
      omega
    rcases face with low | high
    · rcases (Rat.le_total : ξ i ≤ ξ j ∨ ξ j ≤ ξ i) with order | order
      · exact Or.inr (Or.inr (fun z => by rcases cover z with rfl | rfl | rfl | rfl <;> grind only))
      · exact Or.inl (Or.inr (fun z => by rcases cover z with rfl | rfl | rfl | rfl <;> grind only))
    · rcases (Rat.le_total : ξ i ≤ ξ j ∨ ξ j ≤ ξ i) with order | order
      · exact Or.inl (Or.inl (fun z => by rcases cover z with rfl | rfl | rfl | rfl <;> grind only))
      · exact Or.inr (Or.inl (fun z => by rcases cover z with rfl | rfl | rfl | rfl <;> grind only))
  obtain ⟨x,y,ne,hx,hy⟩ := distinct_extrema η
  rcases three x y ne with h | h
  · exact ⟨x, h, hx⟩
  · exact ⟨y, h, hy⟩

/-- The contraction estimate applies on the nonnegative half-line. -/
theorem contraction_iterates {k : Rat} (T : Rat → Rat) (A : Rat → α)
    (hk : 0 < k ∧ k < 1) (step : ∀ x, 0 ≤ x → 0 ≤ T x ∧ T x ≤ k * x)
    (trace : ∀ x, 0 ≤ x → A (T x) = A x) {x : Rat} (hx : 0 ≤ x) (n : Nat) :
    A x = A (Nat.repeat T n x) ∧ 0 ≤ Nat.repeat T n x ∧ Nat.repeat T n x ≤ k ^ n * x := by
  induction n with
  | zero => simp [Nat.repeat, Rat.one_mul, hx, Rat.pow_zero]
  | succ n ih =>
    obtain ⟨equal, nonneg, bound⟩ := ih
    obtain ⟨lo, hi⟩ := step _ nonneg
    refine ⟨equal.trans (trace _ nonneg).symm, lo, ?_⟩
    have := Rat.mul_le_mul_of_nonneg_left bound (Rat.le_of_lt hk.1)
    simp only [Nat.repeat, Rat.pow_succ]
    grind only

private theorem nat_exceeds (x : Rat) : ∃ n : Nat, x < (n : Rat) := by
  refine ⟨x.floor.toNat + 1, ?_⟩
  have h := Rat.lt_floor_add_one x
  have h' := Rat.intCast_le_intCast.mpr (show x.floor + 1 ≤ ((x.floor.toNat + 1 : Nat) : Int) by omega)
  grind only [Rat.intCast_natCast]

/-- A one-sided epsilon-delta condition at the corner makes an invariant profile constant. -/
theorem contraction_kernel_at_corner {k : Rat} (T A : Rat → Rat) (hk : 0 < k ∧ k < 1)
    (step : ∀ x, 0 ≤ x → 0 ≤ T x ∧ T x ≤ k * x)
    (trace : ∀ x, 0 ≤ x → A (T x) = A x)
    (continuousAtZero : ∀ ε, 0 < ε → ∃ δ, 0 < δ ∧
      ∀ y, 0 ≤ y → y < δ → (A y - A 0).abs < ε) {x : Rat} (hx : 0 ≤ x) :
    A x = A 0 := by
  apply Classical.byContradiction
  intro different
  have epos : 0 < (A x - A 0).abs := Rat.abs_pos_iff.mpr (by grind only)
  obtain ⟨δ, hδ, modulus⟩ := continuousAtZero _ epos
  -- Bernoulli's inequality in reciprocal form bounds k^n even over the rationals.
  let c := 1/k - 1
  have hc : 0 < c := by
    have h : (1 : Rat) < 1/k := (Rat.lt_div_iff hk.1).mpr (by grind only)
    unfold c
    grind only
  have growth (n : Nat) : (1 + (n : Rat)*c)*k^n ≤ 1 := by
    induction n with
    | zero =>
      simp only [Rat.pow_zero, Rat.natCast_ofNat, Rat.zero_mul, Rat.add_zero, Rat.mul_one]
      exact Rat.le_refl
    | succ n ih =>
      have hp := Rat.pow_pos (n := n) hk.1
      have hnc := Rat.mul_nonneg (Rat.natCast_nonneg (a := n)) (Rat.le_of_lt hc)
      have hgap := Rat.mul_nonneg hnc (show 0 ≤ 1-k by grind only)
      have hscaled := Rat.mul_le_mul_of_nonneg_right (b := 1+(n:Rat)*c)
        (a := (1+((n:Rat)+1)*c)*k) (by dsimp [c] at *; grind only) (Rat.le_of_lt hp)
      rw [Rat.pow_succ, show (n.succ : Rat) = (n : Rat) + 1 from Rat.natCast_add n 1,
        Rat.mul_comm (k^n) k, ← Rat.mul_assoc]
      exact Rat.le_trans hscaled ih
  obtain ⟨n, hn⟩ := nat_exceeds ((x/δ)/c)
  have h1 := (Rat.div_lt_iff hc).mp hn
  have h2 := (Rat.div_lt_iff hδ).mp h1
  have hp := Rat.pow_pos (n := n) hk.1
  have h3 := Rat.mul_lt_mul_of_pos_right h2 hp
  have h4 := Rat.mul_le_mul_of_nonneg_right (growth n) (Rat.le_of_lt hδ)
  have h5 := Rat.mul_pos hδ hp
  obtain ⟨equal, lo, hi⟩ := contraction_iterates T A hk step trace hx n
  have clash := modulus _ lo (show Nat.repeat T n x < δ by grind only)
  rw [← equal] at clash
  exact Rat.lt_irrefl clash

/-- A closed rational cell of the piecewise-affine return on a projection interval. -/
structure SectionCell where
  lo : Rat
  hi : Rat
  slope : Rat
  intercept : Rat
  nonnegative : 0 ≤ lo
  ordered : lo ≤ hi

/-- A finite collection of closed affine cells covers the entire projection interval.
The same function on the closed cells enforces agreement at common endpoints. -/
structure FiniteAffineSection (T : Rat → Rat) (X : Rat) where
  cells : List SectionCell
  affine : ∀ c ∈ cells, ∀ t, c.lo ≤ t → t ≤ c.hi → T t = c.intercept + c.slope * t
  covers : ∀ t, 0 ≤ t → t ≤ X → ∃ c ∈ cells, c.lo ≤ t ∧ t ≤ c.hi

private theorem endpoint_scale {T : Rat → Rat} {X y : Rat} (zero : T 0 = 0)
    (shrinks : ∀ t, 0 < t → t < X → T t < t) (hy : 0 ≤ y) (hyX : y < X) :
    ∃ k : Rat, 0 < k ∧ k < 1 ∧ T y ≤ k * y := by
  by_cases hzero : y = 0
  · subst y
    exact ⟨1/2, by decide +kernel, by decide +kernel, by rw [zero, Rat.mul_zero]; exact Rat.le_refl⟩
  · have positive : 0 < y := Rat.lt_of_le_of_ne hy (Ne.symm hzero)
    have strict : T y / y < 1 := (Rat.div_lt_iff positive).mpr (by simpa using shrinks y positive hyX)
    let k := max (1/2 : Rat) (T y / y)
    have upper : T y / y ≤ k := by dsimp [k]; grind only [Rat.max_def]
    have scaled := Rat.mul_le_mul_of_nonneg_right upper hy
    rw [Rat.div_mul_cancel hzero] at scaled
    have halfBounds : 0 < (1/2 : Rat) ∧ (1/2 : Rat) < 1 := by decide +kernel
    exact ⟨k, by dsimp [k]; grind only [Rat.max_def], by dsimp [k]; grind only [Rat.max_def], scaled⟩

/-- A common strict upper factor at finitely many sample heights, including the zero endpoint. -/
private theorem sampled_scale {T : Rat → Rat} {X : Rat} (zero : T 0 = 0)
    (shrinks : ∀ t, 0 < t → t < X → T t < t) (sample : List Rat) :
    ∃ k : Rat, 0 < k ∧ k < 1 ∧ ∀ y ∈ sample, 0 ≤ y → y < X → T y ≤ k*y := by
  induction sample with
  | nil => exact ⟨1/2, by decide +kernel, by decide +kernel, by simp⟩
  | cons z zs ih =>
    obtain ⟨a, ha, ha₁, tail⟩ := ih
    by_cases usable : 0 ≤ z ∧ z < X
    · obtain ⟨b, hb, hb₁, head⟩ := endpoint_scale zero shrinks usable.1 usable.2
      let k := max a b
      have ka : a ≤ k := by dsimp [k]; grind only [Rat.max_def]
      have kb : b ≤ k := by dsimp [k]; grind only [Rat.max_def]
      refine ⟨k, by dsimp [k]; grind only [Rat.max_def], by dsimp [k]; grind only [Rat.max_def], ?_⟩
      intro y member hy hyX
      rcases List.mem_cons.mp member with rfl | later
      · exact Rat.le_trans head (Rat.mul_le_mul_of_nonneg_right kb hy)
      · exact Rat.le_trans (tail y later hy hyX) (Rat.mul_le_mul_of_nonneg_right ka hy)
    · refine ⟨a, ha, ha₁, ?_⟩
      intro y member hy hyX
      rcases List.mem_cons.mp member with rfl | later
      · exact (usable ⟨hy, hyX⟩).elim
      · exact tail y later hy hyX

/-- Strict descent on the open interval gives one geometric factor on every
closed subinterval [0,x] with x<X, even when factors tend to one at X. -/
theorem finite_affine_local_contraction {T : Rat → Rat} {X x : Rat} (e : FiniteAffineSection T X)
    (zero : T 0 = 0) (shrinks : ∀ t, 0 < t → t < X → T t < t) (hxX : x < X) :
    ∃ k : Rat, 0 < k ∧ k < 1 ∧ ∀ t, 0 ≤ t → t ≤ x → T t ≤ k*t := by
  let sample := x :: e.cells.flatMap (fun c => [c.lo, c.hi])
  obtain ⟨k, hk, hk₁, bounds⟩ := sampled_scale zero shrinks sample
  refine ⟨k, hk, hk₁, ?_⟩
  intro t ht htx
  obtain ⟨c, hc, cl, cr⟩ := e.covers t ht (Rat.le_trans htx (Rat.le_of_lt hxX))
  have leftMem : c.lo ∈ sample :=
    List.mem_cons_of_mem _ (List.mem_flatMap.mpr ⟨c, hc, by simp⟩)
  have rightMem : c.hi ∈ sample :=
    List.mem_cons_of_mem _ (List.mem_flatMap.mpr ⟨c, hc, by simp⟩)
  have left := bounds c.lo leftMem c.nonnegative (show c.lo < X by grind only)
  have affL := e.affine c hc c.lo Rat.le_refl c.ordered
  have affT := e.affine c hc t cl cr
  by_cases slope : c.slope ≤ k
  · have product := Rat.mul_nonneg (show 0 ≤ k - c.slope by grind only) (show 0 ≤ t - c.lo by grind only)
    grind only
  · let r := min c.hi x
    have tr : t ≤ r := by dsimp [r]; grind only [Rat.min_def]
    have rh : r ≤ c.hi := by dsimp [r]; grind only [Rat.min_def]
    have rx : r ≤ x := by dsimp [r]; grind only [Rat.min_def]
    have rMem : r ∈ sample := by
      dsimp [r]
      rw [Rat.min_def]
      split
      · exact rightMem
      · exact List.mem_cons_self
    have affR := e.affine c hc r (Rat.le_trans cl tr) rh
    have right := bounds r rMem (Rat.le_trans ht tr) (show r < X by grind only)
    have product := Rat.mul_nonneg (show 0 ≤ c.slope-k by grind only) (show 0 ≤ r-t by grind only)
    grind only

/-- On a finite affine corner section, a trace invariant under strict descent
equals its one-sided continuous value at zero throughout the open projection. -/
theorem finite_affine_corner_kernel {T A : Rat → Rat} {X x : Rat} (e : FiniteAffineSection T X)
    (zero : T 0 = 0) (descent : ∀ t, 0 < t → t < X → 0 ≤ T t ∧ T t < t)
    (trace : ∀ t, 0 ≤ t → t < X → A (T t) = A t)
    (continuousAtZero : ∀ ε, 0 < ε → ∃ δ, 0 < δ ∧
      ∀ t, 0 ≤ t → t < δ → (A t - A 0).abs < ε) (hx : 0 ≤ x) (hxX : x < X) :
    A x = A 0 := by
  obtain ⟨k, hk, hk₁, rate⟩ := finite_affine_local_contraction e zero
    (fun t ht hX => (descent t ht hX).2) hxX
  have maps (t : Rat) (ht : 0 ≤ t) (htx : t ≤ x) : 0 ≤ T t ∧ T t ≤ x := by
    by_cases hzero : t = 0
    · simpa only [hzero, zero] using And.intro (Rat.le_refl (a := 0)) hx
    · have inward := descent t (Rat.lt_of_le_of_ne ht (Ne.symm hzero)) (by grind only)
      grind only
  -- Extend the restricted dynamics by sending outside points to the corner.
  let cutT (t : Rat) := if t ≤ x then T t else 0
  let cutA (t : Rat) := if t ≤ x then A t else A 0
  have step (t : Rat) (ht : 0 ≤ t) : 0 ≤ cutT t ∧ cutT t ≤ k*t := by
    by_cases htx : t ≤ x
    · simpa only [cutT, ite_eq_left htx] using And.intro (maps t ht htx).1 (rate t ht htx)
    · simp only [cutT, ite_eq_right htx]
      exact ⟨Rat.le_refl, Rat.mul_nonneg (Rat.le_of_lt hk) ht⟩
  have invariant (t : Rat) (ht : 0 ≤ t) : cutA (cutT t) = cutA t := by
    by_cases htx : t ≤ x
    · simpa only [cutT, cutA, ite_eq_left htx, ite_eq_left (maps t ht htx).2] using
        trace t ht (by grind only)
    · simp only [cutT, cutA, ite_eq_right htx, ite_eq_left hx]
  have continuous (ε : Rat) (hε : 0 < ε) : ∃ δ, 0 < δ ∧
      ∀ t, 0 ≤ t → t < δ → (cutA t - cutA 0).abs < ε := by
    obtain ⟨δ, hδ, near⟩ := continuousAtZero ε hε
    refine ⟨δ, hδ, ?_⟩
    intro t ht htd
    by_cases htx : t ≤ x
    · simpa only [cutA, ite_eq_left htx, ite_eq_left hx] using near t ht htd
    · simpa only [cutA, ite_eq_right htx, ite_eq_left hx, Rat.sub_self, Rat.abs_zero] using hε
  have constant := contraction_kernel_at_corner cutT cutA ⟨hk, hk₁⟩ step invariant continuous hx
  simpa only [cutA, ite_eq_left (Rat.le_refl (a := x)), ite_eq_left hx] using constant

/-- One nondegenerate cell of the reference mesh in the nonnegative half-line. -/
structure ShellCell where
  lo : Rat
  hi : Rat
  nonnegative : 0 ≤ lo
  increasing : lo < hi

/-- The integral of y times the squared slope of the linear interpolant on [a,b]. -/
def cellEnergy (B : Rat → Rat) (a b : Rat) : Rat :=
  ((a+b)/2) * (B b - B a)^2 / (b-a)

def shellEnergy (B : Rat → Rat) (k : Rat) (n : Nat) (mesh : List ShellCell) : Rat :=
  (mesh.map (fun c => cellEnergy B (k^n * c.lo) (k^n * c.hi))).sum

theorem equal_weighted_shell_energy {B : Rat → Rat} {k : Rat} (hk : 0 < k)
    (scale : ∀ y, 0 ≤ y → B (k*y) = B y) (mesh : List ShellCell) (n : Nat) :
    shellEnergy B k n mesh = shellEnergy B k 0 mesh := by
  induction n with
  | zero => rfl
  | succ n ih =>
    refine Eq.trans ?_ ih
    unfold shellEnergy
    apply congrArg List.sum
    apply List.map_congr_left
    intro c _
    have hp := Rat.pow_pos (n := n) hk
    have hy := c.increasing
    have hpos := Rat.mul_pos hp (show 0 < c.hi-c.lo by grind only)
    have hpos' := Rat.mul_pos hk hpos
    have hlo := Rat.mul_nonneg (Rat.le_of_lt hp) c.nonnegative
    have hhi := Rat.mul_nonneg (Rat.le_of_lt hp) (Rat.le_trans c.nonnegative (Rat.le_of_lt hy))
    simp only [cellEnergy, Rat.pow_succ]
    rw [show k^n*k*c.hi = k*(k^n*c.hi) by grind only,
        show k^n*k*c.lo = k*(k^n*c.lo) by grind only, scale _ hhi, scale _ hlo]
    grind only

/-- A uniform bound on the accumulated energy forces each geometric shell to have zero energy. -/
theorem bounded_shell_energy_vanishes {B : Rat → Rat} {k C : Rat} (hk : 0 < k)
    (scale : ∀ y, 0 ≤ y → B (k*y) = B y) (mesh : List ShellCell)
    (bounded : ∀ n, ((List.range n).map (fun j => shellEnergy B k j mesh)).sum ≤ C)
    (n : Nat) : shellEnergy B k n mesh = 0 := by
  let E := shellEnergy B k 0 mesh
  have nonneg : 0 ≤ E := by
    change 0 ≤ shellEnergy B k 0 mesh
    clear bounded E
    induction mesh with
    | nil => exact Rat.le_refl
    | cons c cs ih =>
      have ha := c.nonnegative
      have hb := c.increasing
      have hd := Rat.inv_pos.mpr (show 0 < c.hi-c.lo by grind only)
      have sq : 0 ≤ (B c.hi - B c.lo)^2 := by
        rcases Rat.le_total (a := B c.hi - B c.lo) (b := 0) with h | h
        · have := Rat.mul_nonneg (show 0 ≤ -(B c.hi-B c.lo) by grind only)
            (show 0 ≤ -(B c.hi-B c.lo) by grind only)
          grind only
        · exact Rat.pow_nonneg h
      have prod := Rat.mul_nonneg (Rat.mul_nonneg (show 0 ≤ (c.lo+c.hi)/2 by grind only) sq)
        (Rat.le_of_lt hd)
      simpa only [shellEnergy, List.map_cons, List.sum_cons, cellEnergy, Rat.pow_zero,
        Rat.one_mul, Rat.div_def] using Rat.add_nonneg prod ih
  have total (N : Nat) : ((List.range N).map (fun j => shellEnergy B k j mesh)).sum = (N : Rat)*E := by
    induction N with
    | zero => simp [Rat.zero_mul]
    | succ N ih =>
      rw [List.range_succ, List.map_append, List.sum_append, ih]
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, Rat.add_zero]
      rw [equal_weighted_shell_energy hk scale mesh N]
      rw [show (N.succ : Rat) = (N : Rat) + 1 from Rat.natCast_add N 1, Rat.add_mul, Rat.one_mul]
  rw [equal_weighted_shell_energy hk scale mesh n]
  change E = 0
  apply Classical.byContradiction
  intro h
  have he : 0 < E := Rat.lt_of_le_of_ne nonneg (Ne.symm h)
  obtain ⟨N, hN⟩ := nat_exceeds (C/E)
  have hlarge := (Rat.div_lt_iff he).mp hN
  have lim := bounded N
  rw [total] at lim
  grind only

/-- Parameters of Theorem 4b, including a slope on the closed plateau. -/
structure BevelPlateau (m n : Nat) (u v s : Rat) : Prop where
  positive : 0 < m
  proper : m < n
  coprime : Nat.Coprime m n
  cut : 0 < u ∧ u ≤ v ∧ v < 1
  transverse : (m : Rat) / (n-u) < v/u
  small : v + (m : Rat)/(n-u)*u < 1/(n : Rat)
  onPlateau : (m : Rat)/n ≤ s ∧ s ≤ (m : Rat)/(n-u)

def totalDeficit (m n : Nat) (s : Rat) : Rat := (n : Rat) - (m : Rat)/s

def blockError (n k : Nat) (s D d : Rat) : Rat := 2*s*((k : Rat)*D/n - d)

private theorem le_div_pos_iff {a b c : Rat} (hb : 0 < b) : a ≤ c/b ↔ a*b ≤ c := by
  rw [← Rat.not_lt, Rat.div_lt_iff hb, Rat.not_lt]

private theorem div_pos_le_iff {a b c : Rat} (hb : 0 < b) : a/b ≤ c ↔ a ≤ c*b := by
  rw [← Rat.not_lt, Rat.lt_div_iff hb, Rat.not_lt]

private theorem bevel_positive {m n : Nat} {u v s : Rat} (h : BevelPlateau m n u v s) :
    0 < (n : Rat) ∧ 0 < s ∧ 0 < (n : Rat)-u := by
  have hm := Rat.natCast_pos.mpr h.positive
  have hmn := Rat.natCast_lt_natCast.mpr h.proper
  have h1 : (1 : Rat) ≤ (m : Rat) := Rat.natCast_le_natCast.mpr h.positive
  have hn : 0 < (n : Rat) := by grind only
  have hr : (0 : Rat) < (m : Rat)/n := (Rat.lt_div_iff hn).mpr (by grind only)
  have := h.onPlateau
  have := h.cut
  exact ⟨hn, by grind only, by grind only⟩

theorem plateau_deficit_bounds {m n : Nat} {u v s : Rat} (h : BevelPlateau m n u v s) :
    0 ≤ totalDeficit m n s ∧ totalDeficit m n s ≤ u ∧
    2*v < 2/(n : Rat) - 2*s*totalDeficit m n s := by
  obtain ⟨hn, hs, hnu⟩ := bevel_positive h
  have lower := (div_pos_le_iff hn).mp h.onPlateau.1
  have upper := (le_div_pos_iff hnu).mp h.onPlateau.2
  have lo : 0 ≤ totalDeficit m n s := by
    have := (div_pos_le_iff hs).mpr (show (m : Rat) ≤ (n : Rat)*s by grind only)
    unfold totalDeficit
    grind only
  have hi : totalDeficit m n s ≤ u := by
    have := (le_div_pos_iff hs).mpr (show ((n : Rat)-u)*s ≤ (m : Rat) by grind only)
    unfold totalDeficit
    grind only
  have h₁ := Rat.mul_le_mul_of_nonneg_left hi (Rat.le_of_lt hs)
  have h₂ := Rat.mul_le_mul_of_nonneg_right h.onPlateau.2 (Rat.le_of_lt h.cut.1)
  have := h.small
  exact ⟨lo, hi, by grind only⟩

theorem block_displacement_error {n k : Nat} {s D d : Rat} (hn : 0 < n) (hk : k ≤ n)
    (hs : 0 ≤ s) (hd : 0 ≤ d ∧ d ≤ D) : (blockError n k s D d).abs ≤ 2*s*D := by
  have hnq := Rat.natCast_pos.mpr hn
  have hD := Rat.le_trans hd.1 hd.2
  have product := Rat.mul_nonneg (Rat.natCast_nonneg (a := k)) hD
  have scaled := Rat.mul_le_mul_of_nonneg_right (Rat.natCast_le_natCast.mpr hk) hD
  have lo : 0 ≤ (k : Rat)*D/n := (le_div_pos_iff hnq).mpr (by grind only)
  have hi : (k : Rat)*D/n ≤ D := (div_pos_le_iff hnq).mpr (by grind only)
  have hl := Rat.mul_le_mul_of_nonneg_left (a := -D) (b := (k : Rat)*D/n-d) (by grind only) hs
  have hu := Rat.mul_le_mul_of_nonneg_left (a := (k : Rat)*D/n-d) (b := D) (by grind only) hs
  unfold blockError Rat.abs
  split <;> grind only

/-- Every lift by an even integer stays outside the forbidden gap around zero.
This expresses a lower bound on circle distance without choosing nearest lifts. -/
theorem microscopic_separation {m n k : Nat} {u v s d : Rat} (h : BevelPlateau m n u v s)
    (hk : 0 < k ∧ k < n) (hd : 0 ≤ d ∧ d ≤ totalDeficit m n s) (j : Int) :
    let D := totalDeficit m n s
    let offset := 2*((k*m : Nat) : Rat)/n + blockError n k s D d
    2*v < 2/(n : Rat)-2*s*D ∧ 2/(n : Rat)-2*s*D ≤ (offset-2*(j : Rat)).abs := by
  obtain ⟨hn, hs, _⟩ := bevel_positive h
  have nonzero : ((k*m : Nat) : Int) ≠ (n : Int)*j := by
    intro heq
    have dvd : n ∣ k*m := Int.ofNat_dvd.mp ⟨j, heq⟩
    exact Nat.not_le_of_gt hk.2 (Nat.le_of_dvd hk.1 (h.coprime.symm.dvd_of_dvd_mul_right dvd))
  have bound := block_displacement_error (by omega : 0 < n) (Nat.le_of_lt hk.2) (Rat.le_of_lt hs) hd
  generalize he : blockError n k s (totalDeficit m n s) d = e at bound ⊢
  dsimp only
  refine ⟨(plateau_deficit_bounds h).2.2, ?_⟩
  have heBounds : -(2*s*totalDeficit m n s) ≤ e ∧ e ≤ 2*s*totalDeficit m n s := by
    unfold Rat.abs at bound
    split at bound <;> grind only
  rcases Int.lt_or_gt_of_ne nonzero with hl | hr
  · have hi : ((k*m : Nat) : Int) + 1 ≤ (n : Int)*j := by omega
    have hq := Rat.intCast_le_intCast.mpr hi
    simp only [Rat.intCast_add, Rat.intCast_mul, Rat.intCast_natCast, Rat.intCast_one] at hq
    have hdiv := (div_pos_le_iff hn).mpr
      (show 2*((k*m : Nat) : Rat)+2 ≤ 2*(j : Rat)*(n : Rat) by grind only)
    have sign : 2*((k*m : Nat) : Rat)/n - 2*(j : Rat) ≤ -2/(n : Rat) := by grind only
    unfold Rat.abs
    split <;> grind only
  · have hi : (n : Int)*j + 1 ≤ ((k*m : Nat) : Int) := by omega
    have hq := Rat.intCast_le_intCast.mpr hi
    simp only [Rat.intCast_add, Rat.intCast_mul, Rat.intCast_natCast, Rat.intCast_one] at hq
    have hdiv := (le_div_pos_iff hn).mpr
      (show 2*(j : Rat)*(n : Rat) ≤ 2*((k*m : Nat) : Rat)-2 by grind only)
    have sign : 2/(n : Rat) ≤ 2*((k*m : Nat) : Rat)/n - 2*(j : Rat) := by grind only
    unfold Rat.abs
    split <;> grind only

private def partialDeficit (d : Nat → Rat) : Nat → Rat
  | 0 => 0
  | j + 1 => partialDeficit d j + d j

private theorem partialDeficit_mono {d : Nat → Rat} {n : Nat} (hn : ∀ j < n, 0 ≤ d j)
    {i j : Nat} (ij : i ≤ j) (jn : j ≤ n) : partialDeficit d i ≤ partialDeficit d j := by
  induction j with
  | zero => simpa only [Nat.le_zero.mp ij] using (Rat.le_refl (a := partialDeficit d 0))
  | succ j ih =>
    by_cases eq : i = j+1
    · rw [eq]
      exact Rat.le_refl
    · have prev := ih (by omega) (by omega)
      have next := hn j (by omega)
      change partialDeficit d i ≤ partialDeficit d j + d j
      grind only

private theorem lifted_position {n : Nat} {s : Rat} {phase d : Nat → Rat}
    (step : ∀ i < n, phase (i+1) = phase i + 2*s - 2*s*d i) {i : Nat} (hi : i ≤ n) :
    phase i = phase 0 + 2*s*(i : Rat) - 2*s*partialDeficit d i := by
  induction i with
  | zero =>
    simp only [partialDeficit, Rat.natCast_ofNat, Rat.mul_zero, Rat.add_zero]
    grind only
  | succ i ih =>
    rw [step i (by omega), ih (by omega), partialDeficit,
      show (i.succ : Rat) = (i : Rat) + 1 from Rat.natCast_add i 1]
    grind only

/-- Membership in one closed bevel interval on the circle of circumference two. -/
def InBevel (left v y : Rat) : Prop :=
  ∃ j : Int, left ≤ y-2*(j : Rat) ∧ y-2*(j : Rat) ≤ left+2*v

/-- Any two visits in one winding cycle have the same index. The deficit bounds
for a block are deduced here from the recurrence and closure of the lifted orbit. -/
theorem at_most_one_bevel_visit {m n : Nat} {u v s left : Rat} (h : BevelPlateau m n u v s)
    (phase d : Nat → Rat) (nonneg : ∀ i < n, 0 ≤ d i)
    (step : ∀ i < n, phase (i+1) = phase i + 2*s - 2*s*d i)
    (closedCycle : phase n = phase 0 + 2*(m : Rat))
    (i j : Fin n) (visitI : InBevel left v (phase i)) (visitJ : InBevel left v (phase j)) :
    i = j := by
  obtain ⟨hn, hs, _⟩ := bevel_positive h
  have full := lifted_position step (Nat.le_refl n)
  have sumD : partialDeficit d n = totalDeficit m n s := by
    unfold totalDeficit
    grind only
  suffices noPair : ∀ a b : Fin n, a < b →
      InBevel left v (phase a) → InBevel left v (phase b) → False by
    apply Fin.ext
    by_cases eq : i.val = j.val
    · exact eq
    · rcases Nat.lt_or_gt_of_ne eq with lt | gt
      · exact False.elim (noPair i j lt visitI visitJ)
      · exact False.elim (noPair j i gt visitJ visitI)
  intro a b ab visitA visitB
  let k := b.val - a.val
  let block := partialDeficit d b - partialDeficit d a
  have ak : a.val + k = b.val := by
    dsimp [k]
    omega
  have hk : 0 < k ∧ k < n := by
    dsimp [k]
    omega
  have ha := lifted_position step (Nat.le_of_lt a.isLt)
  have hb := lifted_position step (Nat.le_of_lt b.isLt)
  have hq := congrArg (fun z : Nat => (z : Rat)) ak
  simp only [Rat.natCast_add] at hq
  have h₁ := partialDeficit_mono nonneg (i := 0) (j := a.val) (Nat.zero_le _) (Nat.le_of_lt a.isLt)
  have h₂ := partialDeficit_mono nonneg (i := a.val) (j := b.val) (Nat.le_of_lt ab) (Nat.le_of_lt b.isLt)
  have h₃ := partialDeficit_mono nonneg (Nat.le_of_lt b.isLt) (Nat.le_refl n)
  have hd : 0 ≤ block ∧ block ≤ totalDeficit m n s := by
    change 0 ≤ partialDeficit d a at h₁
    dsimp [block]
    grind only
  have displacement : phase b - phase a =
      2*((k*m : Nat) : Rat)/n + blockError n k s (totalDeficit m n s) block := by
    rw [hb, ha, ← hq, Rat.natCast_mul]
    unfold blockError totalDeficit
    change _ = _ + 2*s*((k : Rat)*((n : Rat)-(m : Rat)/s)/n -
      (partialDeficit d b - partialDeficit d a))
    clear step nonneg
    grind only
  obtain ⟨ia, aLo, aHi⟩ := visitA
  obtain ⟨ib, bLo, bHi⟩ := visitB
  obtain ⟨strict, sep⟩ := microscopic_separation h hk hd (ib-ia)
  rw [← displacement, Rat.intCast_sub] at sep
  unfold Rat.abs at sep
  split at sep <;> grind only

def bevelMultiplier (τ s : Rat) := (τ-s)/(τ+s)

/-- The difference of the ordinates of the unfolded face points
(1−p,1−h(p)), (−3+q,−1−h(q)) equals s times the difference of their
abscissas, with h(p)=v−τp. -/
def BevelHit (v τ s p q : Rat) : Prop :=
  (-1-(v-τ*q)) - (1-(v-τ*p)) = s*((-3+q)-(1-p))

/-- The chord equation on the two unfolded faces gives both forward and
reverse return factors. Small perturbations on the same faces retain this itinerary. -/
theorem bevel_return_multiplier {v τ s : Rat} (hs : 0 < s) (ht : s < τ) :
    (∀ p q, BevelHit v τ s p q ↔ q = ((τ+s)*p+2-4*s)/(τ-s)) ∧
    (∀ p q p' q', BevelHit v τ s p q → BevelHit v τ s p' q' →
      p'-p = bevelMultiplier τ s*(q'-q) ∧ q'-q = (τ+s)/(τ-s)*(p'-p)) ∧
    0 < bevelMultiplier τ s ∧ bevelMultiplier τ s < 1 := by
  have diff : 0 < τ-s := by grind only
  have sum : 0 < τ+s := by grind only
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro p q
    unfold BevelHit
    constructor <;> intro eq <;> grind only
  · intro p q p' q' first second
    unfold BevelHit at first second
    unfold bevelMultiplier
    constructor <;> grind only
  · exact (Rat.lt_div_iff sum).mpr (by grind only)
  · exact (Rat.div_lt_iff sum).mpr (by grind only)

/-- Equal cut legs give a return factor determined by the slope alone. -/
theorem equal_leg_multiplier {ε s : Rat} (hε : 0 < ε) (hs : 0 < s ∧ s < 1) :
    bevelMultiplier (ε/ε) s = (1-s)/(1+s) ∧
    0 < bevelMultiplier (ε/ε) s ∧ bevelMultiplier (ε/ε) s < 1 := by
  have one : ε/ε = 1 := by grind only
  rw [one]
  have pos : 0 < 1+s := by grind only
  unfold bevelMultiplier
  exact ⟨rfl, (Rat.lt_div_iff pos).mpr (by grind only), (Rat.div_lt_iff pos).mpr (by grind only)⟩

theorem period_three_midpoint_multiplier {ε : Rat} (hε : 0 < ε ∧ ε < 1) :
    BevelHit ε (ε/ε) (1/(2-ε/2)) (ε/2) (ε/2) ∧
    bevelMultiplier (ε/ε) (1/(2-ε/2)) = (2-ε)/(6-ε) := by
  have hden : 0 < 2-ε/2 := by grind only
  have hs : 0 < (1 : Rat)/(2-ε/2) ∧ (1 : Rat)/(2-ε/2) < 1 :=
    ⟨(Rat.lt_div_iff hden).mpr (by grind only), (Rat.div_lt_iff hden).mpr (by grind only)⟩
  constructor
  · unfold BevelHit
    grind only
  rw [(equal_leg_multiplier hε.1 hs).1]
  have denom : 0 < 1 + (1 : Rat)/(2-ε/2) := by grind only
  grind only

/-- The same factor cancels for any density denominator. In the frequency
integral that denominator is (1+x²)^(3/2), treated here as a parameter. -/
theorem frequency_density_cancellation {F : Type} [Lean.Grind.Field F] {x : F} (hx : x ≠ -1) :
    (∀ denominator : F, x/(1+x)*((1+x)/denominator) = x/denominator) ∧
    x/(1+x)*((1+x)/(1+x^2)) = x/(1+x^2) := by
  have cancel (d : F) : x/(1+x)*((1+x)/d) = x/d := by grind only
  exact ⟨cancel, cancel _⟩

/-! Regular polygon phases are in units of π/N (phase1_regular.md). -/

/-- Vertex directions in units of h = π/N. Taking a direction modulo π gives
the integer lattice generated by 2 and N. -/
def IsProjectiveVertexIndex (N : Nat) (j : Int) : Prop :=
  ∃ a b : Int, j = 2 * a + (N : Int) * b

def vertexGridStep (N : Nat) : Nat := if N % 2 = 1 then 1 else 2

theorem projectiveVertexGrid (N : Nat) (j : Int) :
    IsProjectiveVertexIndex N j ↔ ∃ k : Int, j = (vertexGridStep N : Int) * k := by
  by_cases h : N % 2 = 1
  · have hN : (N : Int) = 2 * ((N / 2 : Nat) : Int) + 1 := by omega
    simp only [vertexGridStep, ite_eq_left h, Int.natCast_one, Int.one_mul, exists_eq', iff_true]
    refine ⟨-((N / 2 : Nat) : Int) * j, j, ?_⟩
    rw [hN]
    grind only
  · have hN : (N : Int) = 2 * ((N / 2 : Nat) : Int) := by omega
    simp only [vertexGridStep, ite_eq_right h, Int.cast_ofNat_Int]
    constructor
    · rintro ⟨a, b, rfl⟩
      refine ⟨a + ((N / 2 : Nat) : Int) * b, ?_⟩
      rw [hN]
      grind only
    · rintro ⟨k, hk⟩
      exact ⟨k, 0, by simpa using hk⟩

/-- Exact distance to the nearest integer. Both neighbors agree at a tie. -/
def unitGridDistance (x : Rat) : Rat :=
  min (x - (x.floor : Rat)) ((x.floor : Rat) + 1 - x)

private theorem unitCellBounds (x : Rat) :
    (x.floor : Rat) ≤ x ∧ x < (x.floor : Rat) + 1 :=
  ⟨Rat.floor_le x, by simpa using Rat.lt_floor_add_one x⟩

private theorem floorOfCell {x : Rat} {k : Int} (hl : (k : Rat) ≤ x)
    (hr : x < (k : Rat) + 1) : x.floor = k := by
  have h₁ := Rat.le_floor_iff.mpr hl
  have h₂ : x.floor < k + 1 := Rat.floor_lt_iff.mpr (by simpa using hr)
  omega

theorem unitGridDistance_add_int (x : Rat) (k : Int) :
    unitGridDistance (x + (k : Rat)) = unitGridDistance x := by
  simp only [unitGridDistance, Rat.floor_add_intCast, Rat.intCast_add]
  congr 1 <;> grind only

theorem unitGridDistance_half_shift (x : Rat) :
    unitGridDistance x + unitGridDistance (x + 1/2) = 1/2 := by
  obtain ⟨hl, hr⟩ := unitCellBounds x
  by_cases h : x + 1/2 < (x.floor : Rat) + 1
  · have hf : (x + 1/2).floor = x.floor := floorOfCell (by grind only) h
    simp only [unitGridDistance, hf, Rat.min_def]
    split <;> split <;> grind only
  · have hf : (x + 1/2).floor = x.floor + 1 := by
      apply floorOfCell <;> simp only [Rat.intCast_add, Rat.intCast_ofNat] <;> grind only
    simp only [unitGridDistance, hf, Rat.intCast_add, Rat.intCast_ofNat, Rat.min_def]
    split <;> split <;> grind only

/-- The computed distance is attained on the integer lattice and bounds every
other distance from below. -/
theorem unitGridDistance_is_min (x : Rat) :
    (∃ k : Int, unitGridDistance x = (x - (k : Rat)).abs) ∧
    (∀ k : Int, unitGridDistance x ≤ (x - (k : Rat)).abs) := by
  obtain ⟨hl, hr⟩ := unitCellBounds x
  constructor
  · unfold unitGridDistance
    rw [Rat.min_def]
    split
    · exact ⟨x.floor, (Rat.abs_of_nonneg (by grind only)).symm⟩
    · refine ⟨x.floor + 1, ?_⟩
      simp only [Rat.intCast_add, Rat.intCast_ofNat]
      rw [Rat.abs_of_nonpos (by grind only)]
      grind only
  · intro k
    by_cases h : k ≤ x.floor
    · have hi := Rat.intCast_le_intCast.mpr h
      rw [Rat.abs_of_nonneg (by grind only), unitGridDistance, Rat.min_def]
      split <;> grind only
    · have hi : x.floor + 1 ≤ k := by omega
      have hq := Rat.intCast_le_intCast.mpr hi
      simp only [Rat.intCast_add, Rat.intCast_ofNat] at hq
      rw [Rat.abs_of_nonpos (by grind only), unitGridDistance, Rat.min_def]
      split <;> grind only

/-- The horizontal axis has phase x = −φ/h and the vertical axis has phase
x + N/2. This distance is in units of h. -/
def vertexGridDistance (N : Nat) (x : Rat) : Rat :=
  let s : Rat := vertexGridStep N
  s * unitGridDistance (x / s)

private theorem ratDivOne (x : Rat) : x / 1 = x := by grind only

private theorem twiceAbs (x : Rat) : 2 * x.abs = (2*x).abs := by
  simp only [Rat.abs]
  split <;> split <;> grind only

private theorem rescaleGridAbs (N : Nat) (x : Rat) (k : Int) :
    (vertexGridStep N : Rat) * (x / (vertexGridStep N : Rat) - (k : Rat)).abs =
      (x - (((vertexGridStep N : Int) * k : Int) : Rat)).abs := by
  simp only [vertexGridStep, Rat.intCast_mul, Rat.intCast_natCast]
  split
  · simp only [Rat.natCast_ofNat, Rat.one_mul, ratDivOne]
  · simp only [Rat.natCast_ofNat]
    rw [twiceAbs]
    congr 1
    grind only

theorem vertexGridDistance_is_min (N : Nat) (x : Rat) :
    (∃ j : Int, IsProjectiveVertexIndex N j ∧ vertexGridDistance N x = (x - (j : Rat)).abs) ∧
    (∀ j : Int, IsProjectiveVertexIndex N j → vertexGridDistance N x ≤ (x - (j : Rat)).abs) := by
  obtain ⟨⟨k, he⟩, hmin⟩ := unitGridDistance_is_min (x / (vertexGridStep N : Rat))
  constructor
  · refine ⟨(vertexGridStep N : Int) * k, (projectiveVertexGrid N _).mpr ⟨k, rfl⟩, ?_⟩
    simp only [vertexGridDistance, he, rescaleGridAbs]
  · intro j hj
    obtain ⟨l, rfl⟩ := (projectiveVertexGrid N j).mp hj
    rw [← rescaleGridAbs]
    exact Rat.mul_le_mul_of_nonneg_left (hmin l) Rat.natCast_nonneg

/-- For odd N the two distances add to half the projective vertex spacing h. -/
theorem axisGridDistances_odd (N : Nat) (x : Rat) (h : N % 2 = 1) :
    vertexGridDistance N x + vertexGridDistance N (x + (N : Rat)/2) = 1/2 := by
  simp only [vertexGridDistance, vertexGridStep, ite_eq_left h, Rat.natCast_ofNat,
    ratDivOne, Rat.one_mul]
  have hN : N = 2 * (N/2) + 1 := by omega
  have hq := congrArg (fun n : Nat => (n : Rat)) hN
  simp only [Rat.natCast_add, Rat.natCast_mul, Rat.natCast_ofNat] at hq
  rw [show x + (N : Rat)/2 = (x + 1/2) + (((N/2 : Nat) : Int) : Rat) by
    simp only [Rat.intCast_natCast]
    grind only, unitGridDistance_add_int]
  exact unitGridDistance_half_shift x

/-- For N = 2 modulo 4, half the projective vertex spacing is h. -/
theorem axisGridDistances_two_mod_four (N : Nat) (x : Rat) (h : N % 4 = 2) :
    vertexGridDistance N x + vertexGridDistance N (x + (N : Rat)/2) = 1 := by
  have he : N % 2 ≠ 1 := by omega
  simp only [vertexGridDistance, vertexGridStep, ite_eq_right he, Rat.natCast_ofNat]
  have hN : N = 4 * (N/4) + 2 := by omega
  have hq := congrArg (fun n : Nat => (n : Rat)) hN
  simp only [Rat.natCast_add, Rat.natCast_mul, Rat.natCast_ofNat] at hq
  rw [show (x + (N : Rat)/2)/2 = (x/2 + 1/2) + (((N/4 : Nat) : Int) : Rat) by
    simp only [Rat.intCast_natCast]
    grind only, unitGridDistance_add_int]
  have hsum := unitGridDistance_half_shift (x/2)
  grind only

/-- When 4 divides N, the vertical shift is an integer multiple of the spacing 2h. -/
theorem axisGridDistances_four_dvd (N : Nat) (x : Rat) (h : 4 ∣ N) :
    vertexGridDistance N (x + (N : Rat)/2) = vertexGridDistance N x := by
  obtain ⟨k, rfl⟩ := h
  have he : (4*k) % 2 ≠ 1 := by omega
  simp only [vertexGridDistance, vertexGridStep, ite_eq_right he, Rat.natCast_ofNat, Rat.natCast_mul]
  rw [show (x + 4*(k : Rat)/2)/2 = x/2 + ((k : Int) : Rat) by
    simp only [Rat.intCast_natCast]
    grind only, unitGridDistance_add_int]

/-- The two angular corner bands have normalized widths 1−d₁ and 1−d₀.
The full quadrant has normalized length N/2. -/
def cornerAngularFraction (N : Nat) (x : Rat) : Rat :=
  2 * ((1 - vertexGridDistance N (x + (N : Rat)/2)) + (1 - vertexGridDistance N x)) / N

theorem cornerAngularFraction_odd (N : Nat) (x : Rat) (h : N % 2 = 1) :
    cornerAngularFraction N x = 3/(N : Rat) := by
  unfold cornerAngularFraction
  congr 1
  have hsum := axisGridDistances_odd N x h
  grind only

theorem cornerAngularFraction_two_mod_four (N : Nat) (x : Rat) (h : N % 4 = 2) :
    cornerAngularFraction N x = 2/(N : Rat) := by
  unfold cornerAngularFraction
  congr 1
  have hsum := axisGridDistances_two_mod_four N x h
  grind only

theorem cornerAngularFraction_four_dvd (N : Nat) (x : Rat) (h : 4 ∣ N) :
    cornerAngularFraction N x = (4/(N : Rat)) * (1 - vertexGridDistance N x) := by
  unfold cornerAngularFraction
  rw [axisGridDistances_four_dvd N x h, Rat.div_def, Rat.div_def]
  grind only

open Lean.Grind

/-- The smallest per-step contraction as a function of c = cos(π/N). -/
def minimumMultiplier {F : Type} [Field F] (c : F) : F := (2*c - 1)/(2*c + 1)

section
variable {F : Type} [Field F] [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F]
  [OrderedRing F]

theorem minimumMultiplier_strictMono {a b : F} (ha : -1/2 < a) (hab : a < b) :
    minimumMultiplier a < minimumMultiplier b := by
  have hap : 0 < 2*a+1 := by grind only
  have hbp : 0 < 2*b+1 := by grind only
  apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right hap).mp
  apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right hbp).mp
  rw [show minimumMultiplier b*(2*a+1)*(2*b+1) = minimumMultiplier b*(2*b+1)*(2*a+1) by
    rw [Semiring.mul_assoc, Semiring.mul_assoc, CommSemiring.mul_comm (2*a+1) (2*b+1)]]
  unfold minimumMultiplier
  rw [Field.div_mul_cancel (show 2*a+1 ≠ 0 by grind only),
      Field.div_mul_cancel (show 2*b+1 ≠ 0 by grind only)]
  grind only

theorem minimumMultiplier_lt_third {c : F} (hc : -1/2 < c) (h₁ : c < 1) :
    minimumMultiplier c < 1/3 := by
  have h := minimumMultiplier_strictMono hc h₁
  rwa [show minimumMultiplier (1 : F) = 1/3 by unfold minimumMultiplier; grind only] at h
end

section NormalizedPhase
attribute [local instance] Semiring.natCast

def phaseCellDistance {F : Type} [Field F] [LE F] [DecidableLE F] (p : F) : F :=
  if p ≤ 1-p then p else 1-p

/-- A phase measured as a fraction of one projective grid cell. The other axis
advances N/(2w) cells. Its fractional part is computed by integer remainder. -/
def normalizedCornerFraction {F : Type} [Field F] [LE F] [DecidableLE F]
    (N : Nat) (p : F) : F :=
  let w := vertexGridStep N
  let y := p + ((N%(2*w) : Nat) : F)/(2*(w : F))
  let q := if 1 ≤ y then y-1 else y
  2 * (2 - (w : F) * (phaseCellDistance p + phaseCellDistance q)) / (N : F)

section
variable {F : Type} [Field F] [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F]
  [OrderedRing F] [DecidableLE F]

/-- Calculation on a full phase cell over any linearly ordered field. The
phase may be irrational. The factor 2 in the last case converts distance in
cell units to distance in units of π/N. -/
theorem regular_corner_fractions (N : Nat) {p : F} (hp : 0 ≤ p) (hp' : p < 1) :
    (N % 2 = 1 → normalizedCornerFraction N p = 3/(N : F)) ∧
    (N % 4 = 2 → normalizedCornerFraction N p = 2/(N : F)) ∧
    (4 ∣ N → normalizedCornerFraction N p = (4/(N : F))*(1-2*phaseCellDistance p)) := by
  have halfDistance :
      phaseCellDistance p + phaseCellDistance (if 1 ≤ p+1/2 then (p+1/2)-1 else p+1/2) = 1/2 := by
    unfold phaseCellDistance
    split <;> split <;> split <;> grind only
  refine ⟨?_, ?_, ?_⟩
  · intro odd
    unfold normalizedCornerFraction vertexGridStep
    rw [ite_eq_left odd]
    simp only [odd, Semiring.natCast_one, Semiring.mul_one, halfDistance]
    grind only
  · intro two
    have even : N % 2 ≠ 1 := by omega
    simp only [normalizedCornerFraction, vertexGridStep, ite_eq_right even, Nat.reduceMul, two,
      show ((2 : Nat) : F) = 2 from Semiring.natCast_eq_ofNat 2]
    rw [show (2 : F)/(2*2) = 1/2 by grind only, halfDistance]
    grind only
  · intro four
    have even : N % 2 ≠ 1 := by omega
    have zero : N % 4 = 0 := by omega
    have hr : ¬1 ≤ p := by grind only
    simp only [normalizedCornerFraction, vertexGridStep, ite_eq_right even, Nat.reduceMul, zero, Semiring.natCast_zero,
      show (0 : F)/(2*2) = 0 by grind only, AddCommMonoid.add_zero, ite_eq_right hr, show ((2 : Nat) : F) = 2 from Semiring.natCast_eq_ofNat 2,
      Field.div_eq_mul_inv]
    grind only
end
end NormalizedPhase

end CornerShavingAndTriangles
