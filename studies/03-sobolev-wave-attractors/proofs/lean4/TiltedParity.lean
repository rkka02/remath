import Std

/-! Arithmetic of the four canonical sections. The boundary winding is clockwise,
so that the reduced label is `p/q = n/(m+n)`. A boundary step comprises two
chords. The last section constructs these chords on a tilted unit square. -/

namespace TiltedParity

/-- Denominator after reducing the fraction with numerator `u` and denominator `v`. -/
def reducedDen (u v : Nat) : Nat := v / Nat.gcd u v

/-- Division by the actual gcd preserves the winding ratio and produces a
coprime numerator and positive denominator. -/
theorem reduced_winding_fraction {m n : Nat} (hm : 0 < m) :
    let g := Nat.gcd (m + n) (2 * m)
    let P := (m + n) / g
    let D := reducedDen (m + n) (2 * m)
    0 < D ∧ Nat.Coprime P D ∧ P * (2 * m) = (m + n) * D := by
  dsimp only [reducedDen]
  have hd : 0 < 2 * m := by omega
  have num := Nat.div_mul_cancel (Nat.gcd_dvd_left (m + n) (2 * m))
  have den := Nat.div_mul_cancel (Nat.gcd_dvd_right (m + n) (2 * m))
  refine ⟨Nat.div_gcd_pos_of_pos_right _ hd,
    Nat.coprime_div_gcd_div_gcd (Nat.gcd_pos_of_pos_right _ hd), ?_⟩
  calc
    _ = ((m + n) / Nat.gcd (m + n) (2 * m)) *
        ((2 * m / Nat.gcd (m + n) (2 * m)) * Nat.gcd (m + n) (2 * m)) :=
      congrArg (_ * ·) den.symm
    _ = (((m + n) / Nat.gcd (m + n) (2 * m)) * Nat.gcd (m + n) (2 * m)) *
        (2 * m / Nat.gcd (m + n) (2 * m)) := by ac_rfl
    _ = _ := congrArg (· * _) num

private theorem double_gcd {m u : Nat} (h : Nat.Coprime m u) :
    Nat.gcd u (2 * m) = if u % 2 = 0 then 2 else 1 := by
  rw [h.gcd_mul_right_cancel_right 2, Nat.gcd_comm u 2, Nat.gcd_rec 2 u]
  by_cases hu : u % 2 = 0
  · simp [hu]
  · have hu' : u % 2 = 1 := by omega
    simp [hu']

private theorem winding_coprime {m n : Nat} (h : Nat.Coprime m n) :
    Nat.Coprime m (m + n) := by
  simpa [Nat.Coprime] using h.gcd_eq_one

private theorem coprime_not_both_even {m n : Nat} (h : Nat.Coprime m n) :
    ¬ (m % 2 = 0 ∧ n % 2 = 0) := by
  rintro ⟨hm, hn⟩
  exact Nat.not_coprime_of_dvd_of_dvd (by decide : 1 < 2)
    (Nat.dvd_of_mod_eq_zero hm) (Nat.dvd_of_mod_eq_zero hn) h

private theorem reduced_double_den {m u : Nat} (h : Nat.Coprime m u) :
    reducedDen u (2 * m) = if u % 2 = 0 then m else 2 * m := by
  unfold reducedDen
  rw [double_gcd h]
  split <;> omega

/-- An even boundary period, its factor of two, and the odd section period. -/
theorem even_boundary_winding {m n : Nat} (h : Nat.Coprime m n) :
    ((m + n) % 2 = 0 ↔ m % 2 = 1 ∧ n % 2 = 1) ∧
    ((m + n) % 2 = 0 ↔ Nat.gcd (m + n) (2 * m) = 2) ∧
    ((m + n) % 2 = 0 ↔
      reducedDen (m + n) (2 * m) = m ∧ reducedDen (m + n) (2 * m) % 2 = 1) := by
  have hpar := coprime_not_both_even h
  rw [double_gcd (winding_coprime h), reduced_double_den (winding_coprime h)]
  split <;> omega

/-- An odd boundary period leaves the entire even section denominator intact. -/
theorem odd_boundary_winding {m n : Nat} (h : Nat.Coprime m n) :
    ((m + n) % 2 = 1 ↔ m % 2 ≠ n % 2) ∧
    ((m + n) % 2 = 1 ↔ Nat.gcd (m + n) (2 * m) = 1) ∧
    ((m + n) % 2 = 1 ↔
      reducedDen (m + n) (2 * m) = 2 * m ∧ reducedDen (m + n) (2 * m) % 2 = 0) := by
  have hpar := coprime_not_both_even h
  rw [double_gcd (winding_coprime h), reduced_double_den (winding_coprime h)]
  split <;> omega

inductive Tank where
  | rightTrapezoid | isoscelesTrapezoid | shearedParallelogram | tiltedRectangle
  deriving DecidableEq

/-- The right tank uses the complete wall return. The other three geometries
use the reduced denominators of the respective half-section rotations. -/
def sectionDen (tank : Tank) (m n : Nat) : Nat :=
  match tank with
  | .rightTrapezoid => m
  | .isoscelesTrapezoid => reducedDen n (2 * m)
  | .shearedParallelogram | .tiltedRectangle => reducedDen (m + n) (2 * m)

/-- Boundary parity selecting an even (globally periodic) section.
The arguments are the reduced boundary numerator and denominator. -/
def globalLabel (tank : Tank) (p q : Nat) : Prop :=
  match tank with
  | .rightTrapezoid => (q - p) % 2 = 0
  | .isoscelesTrapezoid => p % 2 = 1
  | .shearedParallelogram | .tiltedRectangle => q % 2 = 1

/-- The number of model steps in a physical circuit, before division by the
primitive section period. -/
def modelSteps (tank : Tank) (m : Nat) : Nat :=
  match tank with
  | .rightTrapezoid => m
  | _ => 2 * m

/-- This quotient counts full traversals of the model cycle. -/
def coverDegree (tank : Tank) (m n : Nat) : Nat :=
  modelSteps tank m / sectionDen tank m n

/-- In each row the boundary label selects the even section period exactly.
There is one circuit in the even case. In the odd case only the right
trapezoid closes after one circuit. -/
theorem canonical_parity_table (tank : Tank) {m n : Nat} (hm : 0 < m)
    (h : Nat.Coprime m n) :
    (sectionDen tank m n % 2 = 0 ↔ globalLabel tank n (m + n)) ∧
    (sectionDen tank m n % 2 = 1 ↔ ¬ globalLabel tank n (m + n)) ∧
    coverDegree tank m n =
      (if tank = .rightTrapezoid ∨ sectionDen tank m n % 2 = 0 then 1 else 2) := by
  have hpar := coprime_not_both_even h
  have hd : 0 < 2 * m := by omega
  have hsingle := Nat.div_self hm
  have hdouble := Nat.div_self hd
  have htwice : (2 * m) / m = 2 := Nat.mul_div_cancel _ hm
  cases tank <;>
    simp only [sectionDen, globalLabel, coverDegree, modelSteps, reduced_double_den h,
      reduced_double_den (winding_coprime h), reduceCtorEq, true_or, false_or, ite_true,
      Nat.add_sub_cancel] <;> repeat' first | split | constructor
  all_goals omega

/-- An actual section itinerary. A true entry contributes the expanding slope
and a false entry its reciprocal. -/
def wordProduct (μ : Rat) (word : List Bool) : Rat :=
  (word.map fun expanding => if expanding then μ else μ⁻¹).prod

def branchProduct (μ : Rat) (A B : Nat) : Rat := μ ^ ((A : Int) - (B : Int))

/-- The product of the individual slopes depends only on the signed discrepancy. -/
theorem word_product_formula {μ : Rat} (hμ : μ ≠ 0) (word : List Bool) :
    wordProduct μ word = branchProduct μ (word.count true) (word.count false) := by
  induction word with
  | nil => simp [wordProduct, branchProduct, Rat.zpow_zero]
  | cons step tail ih =>
    cases step <;> simp only [wordProduct, List.map_cons, List.prod_cons, Bool.false_eq_true,
      ite_true, ite_false, List.count_cons_self, List.count_cons_of_ne (by decide : true ≠ false),
      List.count_cons_of_ne (by decide : false ≠ true)] at *
    · unfold branchProduct at *
      rw [show ((tail.count true : Int) - ((tail.count false + 1 : Nat) : Int)) =
        ((tail.count true : Int) - (tail.count false : Int)) - 1 by omega,
        Lean.Grind.Field.zpow_sub_one hμ, ih, Rat.mul_comm]
    · unfold branchProduct at *
      rw [show (((tail.count true + 1 : Nat) : Int) - (tail.count false : Int)) =
        ((tail.count true : Int) - (tail.count false : Int)) + 1 by omega,
        Lean.Grind.Field.zpow_add_one hμ, ih, Rat.mul_comm]

/-- Repetition of the same itinerary multiplies its slope once for each lap. -/
theorem word_product_cover (μ : Rat) (word : List Bool) (laps : Nat) :
    wordProduct μ (List.replicate laps word).flatten = wordProduct μ word ^ laps := by
  letI : Std.Associative (α := Rat) (· * ·) := ⟨Rat.mul_assoc⟩
  letI : Std.LeftIdentity (α := Rat) (· * ·) 1 := ⟨⟩
  letI : Std.LawfulLeftIdentity (α := Rat) (· * ·) 1 := ⟨Rat.one_mul⟩
  induction laps with
  | zero => simp [wordProduct]
  | succ laps ih =>
    simp only [wordProduct, List.replicate_succ, List.flatten_cons, List.map_append,
      List.prod_append, Rat.pow_succ] at *
    rw [ih, Rat.mul_comm]

/-- The interlacing bound forces exact cancellation on an even section cycle. -/
theorem even_balanced_multiplier {D A B : Nat} (hcount : A + B = D)
    (hAB : A ≤ B + 1) (hBA : B ≤ A + 1) (hD : D % 2 = 0) (μ : Rat) :
    A = B ∧ (A : Int) - (B : Int) = 0 ∧ branchProduct μ A B = 1 := by
  have he : (A : Int) - (B : Int) = 0 := by omega
  exact ⟨by omega, he, by rw [branchProduct, he, Rat.zpow_zero]⟩

/-- On an odd section cycle one excess factor survives. Traversing twice
squares that same factor, with its sign fixed by the order of the counts. -/
theorem odd_balanced_multiplier {D A B : Nat} (hcount : A + B = D)
    (hAB : A ≤ B + 1) (hBA : B ≤ A + 1) (hD : D % 2 = 1) (μ : Rat) :
    (((A : Int) - (B : Int) = 1 ∧ branchProduct μ A B = μ ∧
        branchProduct μ A B ^ 2 = μ ^ 2) ∨
     ((A : Int) - (B : Int) = -1 ∧ branchProduct μ A B = μ⁻¹ ∧
        branchProduct μ A B ^ 2 = μ⁻¹ ^ 2)) := by
  by_cases hab : B < A
  · have he : (A : Int) - (B : Int) = 1 := by omega
    exact Or.inl ⟨he, by rw [branchProduct, he, Lean.Grind.Field.zpow_one],
      by rw [branchProduct, he, Lean.Grind.Field.zpow_one]⟩
  · have he : (A : Int) - (B : Int) = -1 := by omega
    exact Or.inr ⟨he, by rw [branchProduct, he, Lean.Grind.Field.zpow_neg_one],
      by rw [branchProduct, he, Lean.Grind.Field.zpow_neg_one]⟩

/-- At a regular attracting section point the complete boundary circuit has
multiplier μ⁻¹ in the right tank and (μ⁻¹)² in the other three geometries. -/
theorem canonical_attracting_multiplier (tank : Tank) {m n A B : Nat} (hm : 0 < m)
    (h : Nat.Coprime m n) {μ : Rat} (hμ : 1 < μ)
    (hcount : A + B = sectionDen tank m n)
    (hAB : A ≤ B + 1) (hBA : B ≤ A + 1) (attracts : branchProduct μ A B < 1) :
    ¬ globalLabel tank n (m + n) ∧ branchProduct μ A B ^ coverDegree tank m n =
      (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2) := by
  obtain ⟨_, hodd, hcover⟩ := canonical_parity_table tank hm h
  have hD : sectionDen tank m n % 2 = 1 := by
    by_cases heven : sectionDen tank m n % 2 = 0
    · have he := (even_balanced_multiplier hcount hAB hBA heven μ).2.2
      grind only
    · omega
  have hs : branchProduct μ A B = μ⁻¹ := by
    rcases odd_balanced_multiplier hcount hAB hBA hD μ with ⟨_, he, _⟩ | ⟨_, he, _⟩
    · grind only
    · exact he
  refine ⟨hodd.mp hD, ?_⟩
  rw [hs, hcover]
  by_cases hr : tank = .rightTrapezoid <;> simp [hr, hD]

private theorem word_visit_count (word : List Bool) :
    word.count true + word.count false = word.length := by
  induction word with
  | nil => decide
  | cons step tail ih => cases step <;> simp <;> omega

/-- The full product along a regular physical attracting itinerary in each
of the four families, with its actual number of model laps. -/
theorem canonical_physical_word (tank : Tank) {m n : Nat} (hm : 0 < m)
    (h : Nat.Coprime m n) {μ : Rat} (hμ : 1 < μ) (word : List Bool)
    (period : word.length = sectionDen tank m n)
    (hAB : word.count true ≤ word.count false + 1)
    (hBA : word.count false ≤ word.count true + 1) (attracts : wordProduct μ word < 1) :
    ¬ globalLabel tank n (m + n) ∧
    wordProduct μ (List.replicate (coverDegree tank m n) word).flatten =
      (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2) := by
  have hword := word_product_formula (by grind only : μ ≠ 0) word
  rw [hword] at attracts
  rw [word_product_cover, hword]
  exact canonical_attracting_multiplier tank hm h hμ
    ((word_visit_count word).trans period) hAB hBA attracts

/-! ## Finite affine section certificates

The lift is the normalized section iterate after subtracting its integer translation.
A cell records the two visit counts on a single affine branch of that iterate.
Closed-cell interpolation makes neighboring formulas agree at their common endpoint.
-/

/-- One closed affine cell of a reduced section iterate. -/
structure SectionCell where
  left : Rat
  right : Rat
  visitsA : Nat
  visitsB : Nat
  deriving DecidableEq

/-- The expanding and contracting visits multiply to the signed power of `μ`. -/
def SectionCell.slope (cell : SectionCell) (μ : Rat) : Rat :=
  branchProduct μ cell.visitsA cell.visitsB

/-- Successive strictly positive intervals tile the whole interval from `a` to `b`. -/
inductive SectionMesh (F : Rat → Rat) (μ : Rat) (D : Nat) :
    Rat → Rat → List SectionCell → Prop where
  | point (a : Rat) : SectionMesh F μ D a a []
  | prepend (cell : SectionCell) {endPoint : Rat} {rest : List SectionCell}
      (width : cell.left < cell.right) (count : cell.visitsA + cell.visitsB = D)
      (affine : ∀ x, cell.left ≤ x → x ≤ cell.right →
        F x = F cell.left + cell.slope μ * (x - cell.left))
      (tail : SectionMesh F μ D cell.right endPoint rest) :
      SectionMesh F μ D cell.left endPoint (cell :: rest)

/-- The same bound is required on both incident branches when the fixed point is a vertex. -/
def BalancedFixedGerms (F : Rat → Rat) (cells : List SectionCell) : Prop :=
  ∀ cell ∈ cells, ∀ x, cell.left ≤ x → x ≤ cell.right → F x = x →
    cell.visitsA ≤ cell.visitsB + 1 ∧ cell.visitsB ≤ cell.visitsA + 1

/-- Pointwise fixedness on a closed interval in the lift. -/
def FixedOnSection (F : Rat → Rat) (a b : Rat) : Prop :=
  ∀ x, a ≤ x → x ≤ b → F x = x

private theorem mesh_ordered {F μ D a b cells} (mesh : SectionMesh F μ D a b cells) :
    a ≤ b := by
  induction mesh with
  | point _ => exact Rat.le_refl
  | prepend _ width _ _ _ ih => exact Rat.le_trans (Rat.le_of_lt width) ih

private theorem even_cell_fixed {F : Rat → Rat} {μ : Rat} {D : Nat} {cell : SectionCell}
    (count : cell.visitsA + cell.visitsB = D) (even : D % 2 = 0)
    (affine : ∀ x, cell.left ≤ x → x ≤ cell.right →
      F x = F cell.left + cell.slope μ * (x - cell.left))
    (balance : ∀ x, cell.left ≤ x → x ≤ cell.right → F x = x →
      cell.visitsA ≤ cell.visitsB + 1 ∧ cell.visitsB ≤ cell.visitsA + 1)
    {x : Rat} (hx : cell.left ≤ x) (hx' : x ≤ cell.right) (fixed : F x = x) :
    FixedOnSection F cell.left cell.right := by
  have ⟨hab, hba⟩ := balance x hx hx' fixed
  have eqVisits : cell.visitsA = cell.visitsB := by omega
  have unit : cell.slope μ = 1 := by simp [SectionCell.slope, branchProduct, eqVisits]
  have h₁ := affine x hx hx'
  intro y hy hy'
  have h₂ := affine y hy hy'
  rw [unit, Rat.one_mul] at h₁ h₂
  grind only

/-- A fixed point anywhere on an even mesh forces the reduced lift to fix the entire mesh. -/
theorem even_section_mesh_identity {F μ D a b cells} (mesh : SectionMesh F μ D a b cells)
    (even : D % 2 = 0) :
    BalancedFixedGerms F cells → (∃ x, a ≤ x ∧ x ≤ b ∧ F x = x) →
      FixedOnSection F a b := by
  induction mesh with
  | point a =>
    intro _ ⟨x, hax, hxa, fx⟩ y hay hya
    grind only
  | @prepend cell b rest width count affine tail ih =>
    intro balance ⟨x, hlx, hxb, fx⟩
    have cellBalance := balance cell List.mem_cons_self
    have restBalance : BalancedFixedGerms F rest :=
      fun c hc => balance c (List.mem_cons_of_mem _ hc)
    have cellLe := Rat.le_of_lt width
    have tailLe := mesh_ordered tail
    have both : FixedOnSection F cell.left cell.right ∧ FixedOnSection F cell.right b := by
      by_cases hx : x ≤ cell.right
      · have first := even_cell_fixed count even affine cellBalance hlx hx fx
        exact ⟨first, ih restBalance
          ⟨cell.right, Rat.le_refl, tailLe, first _ cellLe Rat.le_refl⟩⟩
      · have last := ih restBalance ⟨x, by grind only, hxb, fx⟩
        exact ⟨even_cell_fixed count even affine cellBalance cellLe Rat.le_refl
          (last _ Rat.le_refl tailLe), last⟩
    intro y hy hy'
    by_cases h : y ≤ cell.right
    · exact both.1 y hy h
    · exact both.2 y (by grind only) hy'

private theorem section_pow_succ_gt_one {μ : Rat} (hμ : 1 < μ) (n : Nat) :
    1 < μ ^ (n + 1) := by
  induction n with
  | zero => simpa using hμ
  | succ n ih =>
    rw [Rat.pow_succ μ (n + 1)]
    have pos : 0 < μ ^ (n + 1) := by grind only
    have step := Rat.mul_lt_mul_of_pos_left hμ pos
    rw [Rat.mul_one] at step
    grind only

private theorem section_zpow_ne_one {μ : Rat} (hμ : 1 < μ) {e : Int} (nonzero : e ≠ 0) :
    μ ^ e ≠ 1 := by
  cases e with
  | ofNat n =>
    cases n with
    | zero => exact False.elim (nonzero rfl)
    | succ n => exact Rat.ne_of_gt (section_pow_succ_gt_one hμ n)
  | negSucc n =>
    change (μ ^ (n + 1))⁻¹ ≠ 1
    intro h
    have h' := congrArg (fun x : Rat => x⁻¹) h
    rw [Rat.inv_inv] at h'
    have invOne : (1 : Rat)⁻¹ = 1 := by
      simpa only [Rat.one_mul] using Rat.mul_inv_cancel (1 : Rat) (by decide)
    have : μ ^ (n + 1) = 1 := h'.trans invOne
    exact (Rat.ne_of_gt (section_pow_succ_gt_one hμ n)) this

private theorem two_fixed_points_force_unit {F : Rat → Rat} {μ : Rat} {cell : SectionCell}
    (affine : ∀ x, cell.left ≤ x → x ≤ cell.right →
      F x = F cell.left + cell.slope μ * (x - cell.left))
    {x y : Rat} (hlx : cell.left ≤ x) (hxy : x < y) (hyr : y ≤ cell.right)
    (fx : F x = x) (fy : F y = y) : cell.slope μ = 1 := by
  have ax := affine x hlx (by grind only)
  have ay := affine y (by grind only) hyr
  have cancel : (cell.slope μ - 1) * (y - x) = 0 := by grind only
  have diff : y - x ≠ 0 := by grind only
  rcases Rat.mul_eq_zero.mp cancel with unit | zero
  · grind only
  · exact False.elim (diff zero)

/-- An odd mesh with `μ > 1` admits no fixed subinterval of positive length.
Only the length of each branch itinerary is used. -/
theorem odd_section_mesh_no_fixed_interval {F μ D a b cells}
    (mesh : SectionMesh F μ D a b cells) (odd : D % 2 = 1) (hμ : 1 < μ) :
    ∀ x y, a ≤ x → x < y → y ≤ b → ¬FixedOnSection F x y := by
  induction mesh with
  | point a =>
    intro x y hax hxy hya
    grind only
  | @prepend cell b rest width count affine tail ih =>
    intro x y hlx hxy hyb fixed
    by_cases hxr : x < cell.right
    · let z := min y cell.right
      have hxz : x < z := by
        unfold z
        rw [Rat.min_def]
        split <;> grind only
      have hzr : z ≤ cell.right := by
        unfold z
        rw [Rat.min_def]
        split <;> grind only
      have hzy : z ≤ y := by
        unfold z
        rw [Rat.min_def]
        split <;> grind only
      have unit := two_fixed_points_force_unit affine hlx hxz hzr
        (fixed x Rat.le_refl (Rat.le_of_lt hxy)) (fixed z (Rat.le_of_lt hxz) hzy)
      have nonzero : (cell.visitsA : Int) - (cell.visitsB : Int) ≠ 0 := by omega
      exact section_zpow_ne_one hμ nonzero unit
    · exact ih x y (by grind only) hxy hyb fixed

/-- Degree one for the normalized horizontal section. -/
def DegreeOneSectionLift (F : Rat → Rat) : Prop := ∀ x, F (x + 1) = F x + 1

private theorem mesh_nat_translate {F : Rat → Rat} (degree : DegreeOneSectionLift F)
    (x : Rat) (n : Nat) : F (x + n) = F x + n := by
  induction n with
  | zero => simp [Rat.add_zero]
  | succ n ih =>
    have next := degree (x + n)
    change F (x + ((n + 1 : Nat) : Rat)) = F x + ((n + 1 : Nat) : Rat)
    rw [Rat.natCast_add]
    grind only

private theorem mesh_int_translate {F : Rat → Rat} (degree : DegreeOneSectionLift F)
    (x : Rat) (k : Int) : F (x + k) = F x + k := by
  cases k with
  | ofNat n =>
    exact mesh_nat_translate degree x n
  | negSucc n =>
    let d : Rat := ((n + 1 : Nat) : Rat)
    have shift := mesh_nat_translate degree (x - d) (n + 1)
    have cast : ((Int.negSucc n : Int) : Rat) = -d := by
      simp [d, Int.negSucc_eq, Rat.intCast_natCast]
    rw [cast]
    change F (x - d + d) = F (x - d) + d at shift
    grind only

private theorem section_fraction_bounds (x : Rat) :
    0 ≤ x - (x.floor : Rat) ∧ x - (x.floor : Rat) < 1 := by
  have lower := Rat.floor_le x
  have upper := Rat.lt_floor_add_one x
  simp only [Rat.intCast_add, Rat.intCast_one] at upper
  grind only

/-- Fixed-germ balance in one unit mesh and a single fixed point imply global lift identity. -/
theorem even_reduced_section_lift_identity {F μ D cells}
    (mesh : SectionMesh F μ D 0 1 cells) (degree : DegreeOneSectionLift F)
    (even : D % 2 = 0) (balance : BalancedFixedGerms F cells)
    (existsFixed : ∃ x, F x = x) : ∀ x, F x = x := by
  obtain ⟨x, fx⟩ := existsFixed
  have atFrac := mesh_int_translate degree (x - x.floor) x.floor
  have ⟨lo, hi⟩ := section_fraction_bounds x
  have normalized : F (x - x.floor) = x - x.floor := by grind only
  have onUnit := even_section_mesh_identity mesh even balance
    ⟨x - x.floor, lo, Rat.le_of_lt hi, normalized⟩
  intro y
  have ⟨lo', hi'⟩ := section_fraction_bounds y
  have fy := onUnit _ lo' (Rat.le_of_lt hi')
  have shift := mesh_int_translate degree (y - y.floor) y.floor
  grind only

/-- The odd exclusion holds on the entire degree-one lift, including intervals across a cut. -/
theorem odd_reduced_section_lift_no_fixed_interval {F μ D cells}
    (mesh : SectionMesh F μ D 0 1 cells) (degree : DegreeOneSectionLift F)
    (odd : D % 2 = 1) (hμ : 1 < μ) :
    ∀ x y, x < y → ¬FixedOnSection F x y := by
  intro x y hxy fixed
  let k := x.floor
  let left := x - (k : Rat)
  let right := min 1 (y - (k : Rat))
  have ⟨lo, hi⟩ := section_fraction_bounds x
  have hleft : 0 ≤ left := lo
  have inside : left < right ∧ right ≤ 1 ∧ right ≤ y - (k : Rat) := by
    unfold left right k
    rw [Rat.min_def]
    split <;> grind only
  apply odd_section_mesh_no_fixed_interval mesh odd hμ left right hleft inside.1 inside.2.1
  intro z hlz hzr
  have hlo : x ≤ z + k := by unfold left at hlz; grind only
  have hhi : z + k ≤ y := by grind only
  have fz := fixed (z + k) hlo hhi
  have shift := mesh_int_translate degree z k
  grind only

/-! ## Gap interlacing and the two fixed-germ certificates -/

/-- Advance a label of a primitive cycle in temporal order. -/
def sectionCycleNext {D : Nat} (positive : 0 < D) (i : Fin D) : Fin D :=
  ⟨(i.val + 1) % D, Nat.mod_lt _ positive⟩

/-- Label the gaps of the first cycle in temporal order, starting with the gap
containing the initial point of the second. If the return carries each occupied
gap to its successor, each gap contains exactly one point of the second cycle. -/
theorem one_reflected_point_per_gap {D : Nat} (positive : 0 < D)
    (gapOf : Fin D → Fin D) (start : gapOf ⟨0, positive⟩ = ⟨0, positive⟩)
    (commute : ∀ i, gapOf (sectionCycleNext positive i) =
      sectionCycleNext positive (gapOf i)) :
    ∀ gap, ∃ i, gapOf i = gap ∧ ∀ j, gapOf j = gap → j = i := by
  have onIndex : ∀ n (hn : n < D), gapOf ⟨n, hn⟩ = ⟨n, hn⟩ := by
    intro n
    induction n with
    | zero => intro _; exact start
    | succ n ih =>
      intro hn
      let i : Fin D := ⟨n, by omega⟩
      have next : sectionCycleNext positive i = ⟨n + 1, hn⟩ :=
        Fin.ext (Nat.mod_eq_of_lt hn)
      have fixed : gapOf i = i := ih i.isLt
      rw [← next, commute, fixed]
  intro gap
  exact ⟨gap, onIndex gap.val gap.isLt,
    fun j hj => (onIndex j.val j.isLt).symm.trans hj⟩

/-- The cyclic ordering of two interlaced orbits labels their points alternately.
The double reduction includes arcs crossing the cut of the normalized circle. -/
def interlacedArcOwners (D start length : Nat) : List Bool :=
  (List.range' start length).map fun i => i % (2 * D) % 2 == 0

private def alternatingOwners (first : Bool) : Nat → List Bool
  | 0 => []
  | n + 1 => first :: alternatingOwners (!first) n

private theorem alternating_owner_counts (first : Bool) (n : Nat) :
    (alternatingOwners first n).count (!first) ≤ (alternatingOwners first n).count first ∧
    (alternatingOwners first n).count first ≤ (alternatingOwners first n).count (!first) + 1 := by
  induction n generalizing first with
  | zero => simp [alternatingOwners]
  | succ n ih =>
    have tail := ih (!first)
    cases first <;> simp_all [alternatingOwners]

private theorem interlaced_arc_alternates (D start n : Nat) :
    interlacedArcOwners D start n = alternatingOwners (start % 2 == 0) n := by
  induction n generalizing start with
  | zero => simp [interlacedArcOwners, alternatingOwners]
  | succ n ih =>
    have cyclic : start % (2 * D) % 2 = start % 2 :=
      Nat.mod_mod_of_dvd _ (Nat.dvd_mul_right _ _)
    have flip : ((start + 1) % 2 == 0) = !(start % 2 == 0) := by
      by_cases even : start % 2 = 0
      · have odd : (start + 1) % 2 ≠ 0 := by omega
        simp [even, odd]
      · have : (start + 1) % 2 = 0 := by omega
        simp [even, this]
    change (start % (2 * D) % 2 == 0) :: interlacedArcOwners D (start + 1) n = _
    rw [cyclic, ih, flip, alternatingOwners]

/-- On every contiguous cyclic arc, the two owner counts differ by at most one. -/
theorem interlaced_arc_discrepancy (D start length : Nat) :
    let arc := interlacedArcOwners D start length
    arc.count true ≤ arc.count false + 1 ∧ arc.count false ≤ arc.count true + 1 := by
  dsimp only
  rw [interlaced_arc_alternates]
  have bounds := alternating_owner_counts (start % 2 == 0) length
  cases h : (start % 2 == 0) <;> simp [h] at bounds ⊢ <;> omega

/-- In the disjoint case, the reflecting semicircle selects a contiguous arc
from the joint cyclic ordering. In the invariant case all interior visits pair
under reflection and each of the two seam points occurs at most once. Each
half-open germ assigns at most one seam point to each side. -/
inductive FixedGermOrbitCounts (D A B : Nat) : Prop where
  | disjoint (start : Nat)
      (sideA : A = (interlacedArcOwners D start D).count true)
      (sideB : B = (interlacedArcOwners D start D).count false)
  | invariant (pairs : Nat) (seamA seamB : Bool)
      (sideA : A = pairs + seamA.toNat) (sideB : B = pairs + seamB.toNat)

/-- Both orbit configurations give the two-sided discrepancy used by even return germs. -/
theorem fixed_germ_discrepancy {D A B : Nat} (orbits : FixedGermOrbitCounts D A B) :
    A ≤ B + 1 ∧ B ≤ A + 1 := by
  cases orbits with
  | disjoint start sideA sideB =>
    rw [sideA, sideB]
    exact interlaced_arc_discrepancy D start D
  | invariant pairs seamA seamB sideA sideB =>
    cases seamA <;> cases seamB <;> simp_all [Bool.toNat] <;> omega

/-- Orbit and seam data on the incident branches suffice for global even identity. -/
theorem even_reduced_section_lift_from_orbits {F μ D cells}
    (mesh : SectionMesh F μ D 0 1 cells) (degree : DegreeOneSectionLift F)
    (even : D % 2 = 0) (existsFixed : ∃ x, F x = x)
    (orbits : ∀ cell ∈ cells, ∀ x, cell.left ≤ x → x ≤ cell.right → F x = x →
      FixedGermOrbitCounts D cell.visitsA cell.visitsB) :
    ∀ x, F x = x := by
  apply even_reduced_section_lift_identity mesh degree even _ existsFixed
  intro cell hc x hxl hxr fixed
  exact fixed_germ_discrepancy (orbits cell hc x hxl hxr fixed)

/-- The normalized return in the four-family parity table. The mesh is a
subdivision of one unit into affine branches of the actual return. The fixed
point records the attained rational winding, and the orbit data describe the
two one-sided itineraries at each fixed point. -/
structure CanonicalReturn (tank : Tank) (m n : Nat) (μ : Rat) (F : Rat → Rat) where
  cells : List SectionCell
  mesh : SectionMesh F μ (sectionDen tank m n) 0 1 cells
  degreeOne : DegreeOneSectionLift F
  fixedPoint : ∃ x, F x = x
  fixedOrbits : ∀ cell ∈ cells, ∀ x, cell.left ≤ x → x ≤ cell.right → F x = x →
    FixedGermOrbitCounts (sectionDen tank m n) cell.visitsA cell.visitsB

/-- For all four tanks the displayed boundary parity is equivalent to the
normalized reduced return being the identity at every rational coordinate. -/
theorem canonical_global_identity_iff (tank : Tank) {m n : Nat} (hm : 0 < m)
    (h : Nat.Coprime m n) {μ : Rat} (hμ : 1 < μ) {F : Rat → Rat}
    (model : CanonicalReturn tank m n μ F) :
    globalLabel tank n (m+n) ↔ ∀ x, F x = x := by
  have ⟨even, odd, _⟩ := canonical_parity_table tank hm h
  constructor
  · intro label
    exact even_reduced_section_lift_from_orbits model.mesh model.degreeOne (even.mpr label)
      model.fixedPoint model.fixedOrbits
  · intro ident
    by_cases label : globalLabel tank n (m+n)
    · exact label
    · have excluded := odd_reduced_section_lift_no_fixed_interval model.mesh model.degreeOne
        (odd.mpr label) hμ 0 1 (by decide)
      exact False.elim (excluded (fun x _ _ => ident x))

/-- A complete return in the physical wall section comprises either one or
two laps of the reduced model. A nondecreasing real-line lift has no genuine
two-cycle, so passing to two laps preserves the global classification. -/
theorem canonical_physical_identity_iff (tank : Tank) {m n : Nat} (hm : 0 < m)
    (h : Nat.Coprime m n) {μ : Rat} (hμ : 1 < μ) {F : Rat → Rat}
    (model : CanonicalReturn tank m n μ F) (ordered : ∀ x y, x ≤ y → F x ≤ F y) :
    globalLabel tank n (m+n) ↔
      ∀ x, Nat.repeat F (coverDegree tank m n) x = x := by
  rw [canonical_global_identity_iff tank hm h hμ model]
  have cover := (canonical_parity_table tank hm h).2.2
  split at cover
  · rw [cover]
    rfl
  · rw [cover]
    change (∀ x, F x = x) ↔ ∀ x, F (F x) = x
    constructor
    · intro fixed x
      rw [fixed x, fixed x]
    · intro fixed x
      have twice := fixed x
      cases (Rat.le_total : x ≤ F x ∨ F x ≤ x) with
      | inl le => have image := ordered _ _ le; grind only
      | inr le => have image := ordered _ _ le; grind only

/-! ## Regular attractors in the interior of a tongue

At a fixed corner the two one-sided slopes lie on opposite sides of one.
A regular fixed point lies strictly inside an affine cell. -/

/-- At every fixed internal knot the two adjacent germs turn back to the same
side of the diagonal. Knots outside the fixed set impose no restriction. -/
def TangentFixedKnots (F : Rat → Rat) (μ : Rat) (cells : List SectionCell) : Prop :=
  ∀ first second before after, cells = before ++ first :: second :: after →
    F first.right = first.right →
      (first.slope μ < 1 ∧ 1 < second.slope μ) ∨ (1 < first.slope μ ∧ second.slope μ < 1)

/-- An interior fixed point and its affine return on the entire incident cell. -/
def RegularSectionSink (F : Rat → Rat) (μ : Rat) (D : Nat) (cells : List SectionCell) : Prop :=
  ∃ cell ∈ cells, ∃ x, cell.left < x ∧ x < cell.right ∧ F x = x ∧
    cell.visitsA + cell.visitsB = D ∧ 0 < cell.slope μ ∧ cell.slope μ < 1 ∧
    ∀ y, cell.left ≤ y → y ≤ cell.right → F y - x = cell.slope μ * (y - x)

private theorem strict_affine_crossing {F : Rat → Rat} {s l r : Rat}
    (width : l < r) (positive : l < F l) (negative : F r < r)
    (affine : ∀ y, l ≤ y → y ≤ r → F y = F l + s*(y-l)) :
    ∃ x, l < x ∧ x < r ∧ F x = x ∧ s < 1 ∧
      ∀ y, l ≤ y → y ≤ r → F y - x = s*(y-x) := by
  have atRight := affine r (Rat.le_of_lt width) Rat.le_refl
  have drop : (1-s)*(r-l) = (F l-l) - (F r-r) := by grind only
  have posWidth : 0 < r-l := by grind only
  have denom : 0 < 1-s := (Rat.mul_pos_iff_of_pos_right posWidth).mp (by rw [drop]; grind only)
  let dx := (F l-l)/(1-s)
  have dxPos : 0 < dx := (Rat.lt_div_iff denom).mpr (by rw [Rat.zero_mul]; grind only)
  have dxLimit : dx < r-l := (Rat.div_lt_iff' denom).mpr (by rw [drop]; grind only)
  have xLo : l < l+dx := by grind only
  have xHi : l+dx < r := by grind only
  have atX := affine (l+dx) (Rat.le_of_lt xLo) (Rat.le_of_lt xHi)
  have cancel : dx*(1-s) = F l-l := Rat.div_mul_cancel (Rat.ne_of_gt denom)
  have fixed : F (l+dx) = l+dx := by grind only
  refine ⟨l+dx, xLo, xHi, fixed, by grind only, ?_⟩
  intro y hy hz
  have atY := affine y hy hz
  grind only

private theorem tangent_knots_tail {F μ c rest} (knots : TangentFixedKnots F μ (c :: rest)) :
    TangentFixedKnots F μ rest := by
  intro first second before after h eq
  exact knots first second (c :: before) after (by rw [h]; rfl) eq

private theorem sink_in_cons {F μ D rest} (c : SectionCell)
    (sink : RegularSectionSink F μ D rest) : RegularSectionSink F μ D (c :: rest) := by
  obtain ⟨cell, member, data⟩ := sink
  exact ⟨cell, List.mem_cons_of_mem _ member, data⟩

private def StartsAbove (F : Rat → Rat) (μ a : Rat) (cells : List SectionCell) : Prop :=
  a < F a ∨ (F a = a ∧ ∃ cell rest, cells = cell :: rest ∧ 1 < cell.slope μ)

private theorem empty_mesh_ends {F μ D a b} (mesh : SectionMesh F μ D a b []) : a = b := by
  cases mesh
  rfl

private theorem mesh_crossing_from_above {F μ D a b cells} (mesh : SectionMesh F μ D a b cells)
    (hμ : 0 < μ) : TangentFixedKnots F μ cells → StartsAbove F μ a cells → F b < b →
      RegularSectionSink F μ D cells := by
  induction mesh with
  | point a =>
    rintro _ (above | ⟨_, cell, rest, eq, _⟩) below
    · grind only
    · cases eq
  | @prepend cell b rest width count affine tail ih =>
    intro knots start below
    have wpos : 0 < cell.right-cell.left := by grind only
    have atEnd := affine cell.right (Rat.le_of_lt width) Rat.le_refl
    have change : (cell.slope μ-1)*(cell.right-cell.left) =
        (F cell.right-cell.right) - (F cell.left-cell.left) := by grind only
    have pass (start' : StartsAbove F μ cell.right rest) : RegularSectionSink F μ D (cell::rest) :=
      sink_in_cons cell (ih (tangent_knots_tail knots) start' below)
    rcases start with above | ⟨leftFixed, first, others, eq, grows⟩
    · have trichotomy : F cell.right < cell.right ∨
          F cell.right = cell.right ∨ cell.right < F cell.right := by grind only
      rcases trichotomy with down | fixed | up
      · obtain ⟨x, xl, xr, fx, contracts, germ⟩ :=
          strict_affine_crossing width above down affine
        exact ⟨cell, List.mem_cons_self, x, xl, xr, fx, count, Rat.zpow_pos hμ, contracts, germ⟩
      · by_cases empty : rest = []
        · subst rest
          have ends := empty_mesh_ends tail
          grind only
        · cases rest with
          | nil => exact False.elim (empty rfl)
          | cons next more =>
            have negProd : (cell.slope μ-1)*(cell.right-cell.left) < 0 := by
              rw [change, fixed]; grind only
            have damp : cell.slope μ < 1 := by
              have neg := (Rat.mul_neg_iff_of_pos_right wpos).mp negProd
              grind only
            have turns := knots cell next [] more rfl fixed
            have rises : 1 < next.slope μ := by grind only
            exact pass (Or.inr ⟨fixed, next, more, rfl, rises⟩)
      · exact pass (Or.inl up)
    · have same := (List.cons.inj eq).1
      subst first
      have posProd := Rat.mul_pos (by grind only : 0 < cell.slope μ-1) wpos
      rw [change, leftFixed] at posProd
      exact pass (Or.inl (by grind only))

/-- Opposite strict displacement signs in the indicated order give a regular
attracting fixed point. A fixed corner with reciprocal one-sided slopes can
occur anywhere inside the interval. -/
theorem regular_sink_of_crossing {F μ D a b cells} (mesh : SectionMesh F μ D a b cells)
    (hμ : 0 < μ) (knots : TangentFixedKnots F μ cells) (left : a < F a) (right : F b < b) :
    RegularSectionSink F μ D cells :=
  mesh_crossing_from_above mesh hμ knots (Or.inl left) right

/-- The closed cell containing an attracting fixed point is forward invariant.
Every actual iterate acts on that cell by the corresponding power of its slope. -/
theorem attracting_cell_iteration {F : Rat → Rat} {l x r s : Rat}
    (xl : l ≤ x) (xr : x ≤ r) (hs : 0 ≤ s) (hs' : s ≤ 1)
    (germ : ∀ y, l ≤ y → y ≤ r → F y - x = s*(y-x))
    (k : Nat) {y : Rat} (yl : l ≤ y) (yr : y ≤ r) :
    l ≤ Nat.repeat F k y ∧ Nat.repeat F k y ≤ r ∧
      Nat.repeat F k y - x = s^k*(y-x) := by
  have stay (z : Rat) (zl : l ≤ z) (zr : z ≤ r) : l ≤ F z ∧ F z ≤ r := by
    have affine := germ z zl zr
    have lower : F z-l = s*(z-l) + (1-s)*(x-l) := by grind only
    have upper : r-F z = s*(r-z) + (1-s)*(r-x) := by grind only
    have other : 0 ≤ 1-s := by grind only
    have p₁ := Rat.mul_nonneg hs (by grind only : 0 ≤ z-l)
    have p₂ := Rat.mul_nonneg other (by grind only : 0 ≤ x-l)
    have p₃ := Rat.mul_nonneg hs (by grind only : 0 ≤ r-z)
    have p₄ := Rat.mul_nonneg other (by grind only : 0 ≤ r-x)
    grind only
  induction k with
  | zero => simpa only [Nat.repeat, Rat.pow_zero, Rat.one_mul] using
      (show l ≤ y ∧ y ≤ r ∧ y-x = y-x from ⟨yl, yr, rfl⟩)
  | succ k ih =>
    obtain ⟨lo, hi, eq⟩ := ih
    have ⟨lo', hi'⟩ := stay _ lo hi
    refine ⟨lo', hi', ?_⟩
    change F (Nat.repeat F k y) - x = s^(k+1)*(y-x)
    rw [germ _ lo hi, eq, Rat.pow_succ]
    grind only

/-- Starting with strict displacement signs, this constructs the regular
attracting itinerary and its full physical multiplier for every tank. -/
theorem canonical_tongue_interior_sink (tank : Tank) {m n : Nat} (hm : 0 < m)
    (cop : Nat.Coprime m n) {F μ a b cells} (hμ : 1 < μ)
    (mesh : SectionMesh F μ (sectionDen tank m n) a b cells)
    (balance : BalancedFixedGerms F cells) (knots : TangentFixedKnots F μ cells)
    (left : a < F a) (right : F b < b) :
    ¬ globalLabel tank n (m+n) ∧ ∃ cell ∈ cells, ∃ x,
      cell.left < x ∧ x < cell.right ∧ F x = x ∧ cell.visitsB = cell.visitsA+1 ∧
      cell.slope μ = μ⁻¹ ∧ cell.slope μ ^ coverDegree tank m n =
        (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2) ∧
      (∀ y, cell.left ≤ y → y ≤ cell.right → F y - x = μ⁻¹*(y-x)) ∧
      ∀ y, cell.left ≤ y → y ≤ cell.right →
        Nat.repeat F (coverDegree tank m n) y - x =
          (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2)*(y-x) := by
  obtain ⟨c, hc, x, xl, xr, fx, count, pos, contracts, germ⟩ :=
    regular_sink_of_crossing mesh (by grind only) knots left right
  have ⟨ab, ba⟩ := balance c hc x (Rat.le_of_lt xl) (Rat.le_of_lt xr) fx
  have ⟨label, full⟩ := canonical_attracting_multiplier tank hm cop hμ count ab ba contracts
  change c.slope μ ^ coverDegree tank m n =
    (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2) at full
  have odd := (canonical_parity_table tank hm cop).2.1.mpr label
  have exponent : (c.visitsA : Int) - (c.visitsB : Int) = -1 ∧ c.slope μ = μ⁻¹ := by
    change branchProduct μ c.visitsA c.visitsB < 1 at contracts
    rcases odd_balanced_multiplier count ab ba odd μ with ⟨_, val, _⟩ | ⟨e, val, _⟩
    · grind only
    · exact ⟨e, val⟩
  refine ⟨label, c, hc, x, xl, xr, fx, by omega, exponent.2, full, ?_, ?_⟩
  · rwa [exponent.2] at germ
  · intro y yl yr
    have actual := (attracting_cell_iteration (Rat.le_of_lt xl) (Rat.le_of_lt xr)
      (Rat.le_of_lt pos) (Rat.le_of_lt contracts) germ (coverDegree tank m n) yl yr).2.2
    rwa [full] at actual

private theorem mesh_cell_data {F μ D a b cells} (mesh : SectionMesh F μ D a b cells)
    {c : SectionCell} (hc : c ∈ cells) :
    c.visitsA + c.visitsB = D ∧ ∀ y, c.left ≤ y → y ≤ c.right →
      F y = F c.left + c.slope μ*(y-c.left) := by
  induction mesh with
  | point => cases hc
  | prepend first _ count affine _ ih =>
    rcases List.mem_cons.mp hc with same | inTail
    · subst c; exact ⟨count, affine⟩
    · exact ih inTail

private theorem inv_lt_unit {μ : Rat} (hμ : 1 < μ) : μ⁻¹ < 1 := by
  have pos : 0 < μ := by grind only
  apply (Rat.mul_lt_mul_right pos).mp
  rw [Rat.inv_mul_cancel _ (Rat.ne_of_gt pos), Rat.one_mul]
  exact hμ

/-- A regular fixed point of an odd return gives a descending pair of
strict displacement signs on the periodic lift, even when this fixed point
itself is repelling. -/
theorem regular_odd_fixed_has_crossing {F μ D a b cells} (mesh : SectionMesh F μ D a b cells)
    (degree : DegreeOneSectionLift F) (hμ : 1 < μ) (odd : D % 2 = 1)
    (balance : BalancedFixedGerms F cells)
    {c : SectionCell} (hc : c ∈ cells) {x : Rat}
    (xl : c.left < x) (xr : x < c.right) (fixed : F x = x) :
    ∃ l r, l < r ∧ l < F l ∧ F r < r := by
  have ⟨count, affine⟩ := mesh_cell_data mesh hc
  have ⟨ab, ba⟩ := balance c hc x (Rat.le_of_lt xl) (Rat.le_of_lt xr) fixed
  let d := min (1/4 : Rat) (min (x-c.left) (c.right-x))
  have bounds : 0 < d ∧ d ≤ 1/4 ∧ c.left ≤ x-d ∧ x+d ≤ c.right := by
    unfold d
    simp only [Rat.min_def]
    repeat' split
    all_goals grind only
  obtain ⟨dpos, dsmall, dlo, dhi⟩ := bounds
  have atX := affine x (Rat.le_of_lt xl) (Rat.le_of_lt xr)
  have before := affine (x-d) dlo (by grind only)
  have after := affine (x+d) (by grind only) dhi
  have fm : F (x-d) = x-d - (c.slope μ-1)*d := by grind only
  have fp : F (x+d) = x+d + (c.slope μ-1)*d := by grind only
  rcases odd_balanced_multiplier count ab ba odd μ with ⟨_, val, _⟩ | ⟨_, val, _⟩
  · change c.slope μ = μ at val
    have pos := Rat.mul_pos (by grind only : 0 < c.slope μ-1) dpos
    have shifted := degree (x-d)
    exact ⟨x+d, x-d+1, by grind only, by grind only, by grind only⟩
  · change c.slope μ = μ⁻¹ at val
    have damp := inv_lt_unit hμ
    have neg := (Rat.mul_neg_iff_of_pos_right dpos).mpr (by grind only : c.slope μ-1 < 0)
    exact ⟨x-d, x+d, by grind only, by grind only, by grind only⟩

/-- Any compact piece of the periodic lift can be cut at its genuine affine
breaks. The one-sided orbit counts and fixed-corner slopes are checked on
that finite subdivision. -/
def TongueCharts (F : Rat → Rat) (μ : Rat) (D : Nat) : Prop :=
  ∀ a b, a < b → ∃ cells, SectionMesh F μ D a b cells ∧
    BalancedFixedGerms F cells ∧ TangentFixedKnots F μ cells

/-- For an attained regular-interior parameter the complementary boundary
parity is equivalent to existence of a regular attracting return with the
specified physical multiplier. The input sample can be any regular fixed
point, including a repeller. -/
theorem canonical_regular_interior_iff (tank : Tank) {m n : Nat} (hm : 0 < m)
    (cop : Nat.Coprime m n) {F μ} (hμ : 1 < μ) (model : CanonicalReturn tank m n μ F)
    (charts : TongueCharts F μ (sectionDen tank m n))
    (sample : ∃ cell ∈ model.cells, ∃ x, cell.left < x ∧ x < cell.right ∧ F x = x) :
    ¬ globalLabel tank n (m+n) ↔
      ∃ x l r : Rat, l < x ∧ x < r ∧ F x = x ∧
        (∀ y, l ≤ y → y ≤ r → F y-x = μ⁻¹*(y-x)) ∧
        μ⁻¹ ^ coverDegree tank m n = (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2) ∧
        ∀ y, l ≤ y → y ≤ r → Nat.repeat F (coverDegree tank m n) y-x =
          (if tank = .rightTrapezoid then μ⁻¹ else μ⁻¹ ^ 2)*(y-x) := by
  constructor
  · intro label
    have odd := (canonical_parity_table tank hm cop).2.1.mpr label
    have balance : BalancedFixedGerms F model.cells := by
      intro c hc x lo hi fx
      exact fixed_germ_discrepancy (model.fixedOrbits c hc x lo hi fx)
    obtain ⟨c, hc, x, lo, hi, fx⟩ := sample
    obtain ⟨a, b, ab, up, down⟩ := regular_odd_fixed_has_crossing model.mesh
      model.degreeOne hμ odd balance hc lo hi fx
    obtain ⟨cells, mesh, balanced, knots⟩ := charts a b ab
    obtain ⟨_, cell, _, z, zl, zr, fz, _, slope, full, germ, physical⟩ :=
      canonical_tongue_interior_sink tank hm cop hμ mesh balanced knots up down
    exact ⟨z, cell.left, cell.right, zl, zr, fz, germ, by rwa [slope] at full, physical⟩
  · rintro ⟨x, l, r, lo, hi, _, germ, _, _⟩ label
    have ident := (canonical_global_identity_iff tank hm cop hμ model).mp label
    have atRight := germ r (by grind only) Rat.le_refl
    rw [ident r] at atRight
    have damp := Rat.mul_lt_mul_of_pos_right (inv_lt_unit hμ) (by grind only : 0 < r-x)
    rw [Rat.one_mul] at damp
    grind only

section Extinction
open Lean.Grind

variable {K : Type} [Field K] [LE K] [LT K] [Std.LawfulOrderLT K] [Std.IsLinearOrder K]
  [OrderedRing K]

private theorem reciprocal_le {t R : K} (ht : 0 < t) :
    1 / t ≤ R ↔ 1 ≤ R * t := by
  calc
    _ ↔ (1/t)*t ≤ R*t := (Field.IsOrdered.mul_le_mul_iff_of_pos_right ht).symm
    _ ↔ _ := by rw [Field.div_mul_cancel (by grind only : t ≠ 0)]

/-- With t = tan(2φ), the reciprocal aspect-ratio interval is exactly the
simultaneous saturation of the two edge bands. Endpoints are included. -/
theorem extinction_interval {t R : K} (ht : 0 < t) (hR : 0 < R) :
    (1 / t ≤ R ∧ R ≤ t) ↔ (R ≤ t ∧ 1 / R ≤ t) := by
  rw [reciprocal_le ht, reciprocal_le hR, CommSemiring.mul_comm R t, and_comm]

/-- Extinction is possible at some aspect ratio exactly when t ≥ 1, and
the square realizes the threshold (in angle variables, φ = π/8). -/
theorem extinction_threshold {t : K} (ht : 0 < t) :
    ((∃ R : K, 0 < R ∧ 1 / t ≤ R ∧ R ≤ t) ↔ 1 ≤ t) ∧
    ((1 / t ≤ 1 ∧ 1 ≤ t) ↔ 1 ≤ t) := by
  have square : (1 / t ≤ 1 ∧ 1 ≤ t) ↔ 1 ≤ t := by
    simp only [reciprocal_le ht, Semiring.one_mul, and_self]
  refine ⟨⟨?_, fun h => ⟨1, OrderedRing.zero_lt_one, square.mpr h⟩⟩, square⟩
  rintro ⟨R, _, hlo, hhi⟩
  have hprod := (reciprocal_le ht).mp (Std.le_trans hlo hhi)
  by_cases threshold : 1 ≤ t
  · exact threshold
  · have hsmall : t < 1 := by grind only
    have hlt := OrderedRing.mul_lt_mul_of_pos_right hsmall ht
    grind only

/-- In the variable z = tan φ, the square threshold tan(2φ) ≥ 1 becomes
(1+z)² ≥ 2. Its positive equality root is tan(π/8) = √2 − 1. -/
theorem square_half_angle_threshold {z : K} (hz : 0 < z) (hz' : z < 1) :
    1 ≤ 2*z / (1-z^2) ↔ 2 ≤ (1+z)^2 := by
  have hs := OrderedRing.mul_lt_mul_of_pos_right hz' hz
  have hd : 0 < 1 - z^2 := by
    rw [Semiring.pow_succ, Semiring.pow_one]
    grind only
  have scale : 1 ≤ 2*z / (1-z^2) ↔ 1-z^2 ≤ 2*z := by
    rw [Field.div_eq_mul_inv, Field.IsOrdered.le_mul_inv_iff_mul_le _ _ hd, Semiring.one_mul]
  have eq : (1+z)^2 = 1 + 2*z + z^2 := by grind only
  rw [scale, eq]
  grind only

/-- In any ordered field containing a positive square root r of two, the
endpoint z = r − 1 is admissible and gives exactly t = 1. -/
theorem square_algebraic_endpoint {r : K} (hr : 0 < r) (root : r^2 = 2) :
    0 < r-1 ∧ r-1 < 1 ∧ 2*(r-1) / (1-(r-1)^2) = 1 := by
  have above : 0 < r-1 := by
    apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right (show 0 < r+1 by grind only)).mp
    rw [Semiring.zero_mul, show (r-1)*(r+1) = 1 by grind only]
    exact OrderedRing.zero_lt_one
  have below : r-1 < 1 := by
    apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right (show 0 < r+2 by grind only)).mp
    rw [Semiring.one_mul, show (r-1)*(r+2) = r by grind only]
    grind only
  refine ⟨above, below, ?_⟩
  have den : 1-(r-1)^2 = 2*(r-1) := by grind only
  rw [den, Field.div_eq_mul_inv, Field.mul_inv_cancel (by grind only : 2*(r-1) ≠ 0)]

/-- In the reduced tangent coordinate z = tan φ, the square extinction
interval includes exactly z ≥ tan(π/8) = r − 1, where r is the positive
square root of two in the coordinate field. -/
theorem square_extinction_angle_iff {z r : K} (hz : 0 < z) (hz' : z < 1)
    (hr : 0 < r) (root : r^2 = 2) :
    (1 / (2*z/(1-z^2)) ≤ 1 ∧ 1 ≤ 2*z/(1-z^2)) ↔ r-1 ≤ z := by
  have pos : 0 < 1+z+r := by grind only
  have fact : (1+z-r)*(1+z+r) = (1+z)^2-2 := by grind only
  have order : 0*(1+z+r) ≤ (1+z-r)*(1+z+r) ↔ 0 ≤ 1+z-r :=
    Field.IsOrdered.mul_le_mul_iff_of_pos_right pos
  rw [Semiring.zero_mul, fact] at order
  have criterion : 1 ≤ 2*z/(1-z^2) ↔ r-1 ≤ z := by
    rw [square_half_angle_threshold hz hz']
    grind only
  constructor
  · exact fun interval => criterion.mp interval.2
  · intro angle
    have ht := criterion.mpr angle
    exact (extinction_threshold (show 0 < 2*z/(1-z^2) by grind only)).2.mpr ht

end Extinction

/-! The tilted square in the counterexample has wall slopes 1/2 and −2.
Edges carry their Cartesian coordinate. The cyclic parameter runs along the
bottom, right, top and left edges in that order, one unit per edge. Vertices
have two edge representatives and a single Cartesian position. -/

inductive SquareEdge where
  | bottom (x : Rat) | right (y : Rat) | top (x : Rat) | left (y : Rat)
  deriving DecidableEq

namespace SquareEdge

def position : SquareEdge → Rat × Rat
  | .bottom x => (x, 0)
  | .right y => (1, y)
  | .top x => (x, 1)
  | .left y => (0, y)

def valid : SquareEdge → Prop
  | .bottom s | .right s | .top s | .left s => 0 ≤ s ∧ s ≤ 1

def perimeter : SquareEdge → Rat
  | .bottom x => x
  | .right y => 1 + y
  | .top x => 3 - x
  | .left y => 4 - y

/-- The other endpoint of the chord 2y − x = constant. -/
def rising : SquareEdge → SquareEdge
  | .bottom x => .right ((1 - x) / 2)
  | .right y => if y ≤ 1/2 then .bottom (1 - 2*y) else .left (y - 1/2)
  | .top x => .left (1 - x / 2)
  | .left y => if y ≤ 1/2 then .right (y + 1/2) else .top (2*(1-y))

/-- The other endpoint of the chord y + 2x = constant. -/
def falling : SquareEdge → SquareEdge
  | .bottom x => if x ≤ 1/2 then .left (2*x) else .top (x - 1/2)
  | .right y => .top ((1 + y) / 2)
  | .top x => if x ≤ 1/2 then .bottom (x + 1/2) else .right (2*x - 1)
  | .left y => .bottom (y / 2)

def step (p : SquareEdge) : SquareEdge := falling (rising p)

/-- Both computed hits lie on the square and preserve the correct chord
projection. Hence the rational formulas give the physical chess map. -/
theorem chord_projections (p : SquareEdge) (hp : p.valid) :
    p.rising.valid ∧ p.falling.valid ∧
    2 * p.rising.position.2 - p.rising.position.1 = 2 * p.position.2 - p.position.1 ∧
    p.falling.position.2 + 2 * p.falling.position.1 = p.position.2 + 2 * p.position.1 := by
  cases p <;> grind only [valid, rising, falling, position]

end SquareEdge

open SquareEdge

/-- On the two horizontal edges an entire circuit is affine and attracting.
the formulas use the increasing counterclockwise perimeter coordinate. -/
theorem square_horizontal_return (x : Rat) :
    (step (step (.bottom x))).perimeter = 1/3 + (x - 1/3) / 16 ∧
    (step (step (.top x))).perimeter = 7/3 + ((3 - x) - 7/3) / 16 := by
  simp only [step, rising, falling, perimeter]
  grind only

/-- On open neighborhoods of the two vertical-edge points the multiplier of
the first return is 16. Here u is signed perimeter distance from the orbit. -/
theorem square_vertical_return {u : Rat} (hl : -(1/48) < u) (hr : u < 1/48) :
    (step (step (.right (1/3 + u)))).perimeter = 4/3 + 16*u ∧
    (step (step (.left (2/3 - u)))).perimeter = 10/3 + 16*u := by
  constructor <;> grind only [step, rising, falling, perimeter]

/-- The two-chord map exchanges the two attracting points and also exchanges
the two repelling points. The complete circuit has two boundary steps. -/
theorem zhang_temnov_cycles :
    (2 : Rat) / (1/2) = 4 ∧ ((2 : Rat) / (1/2)) ^ (-2 : Int) = 1/16 ∧
    step (.bottom (1/3)) = .top (2/3) ∧ step (.top (2/3)) = .bottom (1/3) ∧
    step (.right (1/3)) = .left (2/3) ∧ step (.left (2/3)) = .right (1/3) := by
  decide +kernel

/-- Exhaustion of the first-return fixed set in cyclic coordinates.
Cartesian equality identifies both representatives of each corner. -/
theorem square_period_two_iff (p : SquareEdge) (hp : p.valid) :
    p.step.step.position = p.position ↔
      p.perimeter = 1/3 ∨ p.perimeter = 4/3 ∨ p.perimeter = 7/3 ∨ p.perimeter = 10/3 := by
  have clear (x k : Rat) : x = k/3 ↔ 3*x = k := by grind only
  simp only [clear]
  clear clear
  cases p <;> simp only [valid, perimeter] at hp ⊢ <;>
    simp only [step, rising.eq_1, rising.eq_2, rising.eq_3, rising.eq_4,
      falling.eq_1, falling.eq_2, falling.eq_3, falling.eq_4, position.eq_1,
      position.eq_2, position.eq_3, position.eq_4, apply_ite rising, apply_ite falling,
      apply_ite position]
  all_goals repeat' split
  all_goals simp only [Prod.mk.injEq] <;> grind only

end TiltedParity
