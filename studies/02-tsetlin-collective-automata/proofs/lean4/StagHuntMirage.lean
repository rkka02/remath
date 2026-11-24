import Init

namespace StagHuntMirage
open Lean.Grind

variable {F : Type} [Field F]
attribute [local instance] Semiring.natCast

/-- Geometric weight of the solo-stag levels from depth zero through depth (n-1). -/
def G : Nat → F → F
  | 0, _ => 0
  | n + 1, s => G n s + (s / (1 - s)) ^ n

/-- The inverse odds of a reward and the exponential base of the cooperative odds. -/
def rho (p : F) := (1 - p) / p
def lambda (R P : F) := (rho P) ^ 2 / rho R

private theorem eq_div_iff {x y z : F} (hz : z ≠ 0) :
    x = y / z ↔ x * z = y := by
  constructor
  · intro h
    rw [h, Field.div_mul_cancel hz]
  · intro h
    rw [← h, Field.div_eq_mul_inv, Semiring.mul_assoc, Field.mul_inv_cancel hz,
      Semiring.mul_one]

/-- The cleared geometric identity applies on the fair line as well. -/
theorem G_closed (n : Nat) {s : F} (hs : s ≠ 1) :
    (2 * s - 1) * G n s = (1 - s) * ((s / (1 - s)) ^ n - 1) := by
  have ratio : s / (1 - s) * (1 - s) = s := Field.div_mul_cancel (by grind only)
  induction n with
  | zero => simp only [G, Semiring.pow_zero]; grind only
  | succ n ih =>
    rw [G, Semiring.left_distrib, ih, Semiring.pow_succ]
    grind only

/-- One-player cooperative mass in the outside product reference, given its switch flux. -/
def referenceMass (n : Nat) (s f : F) := f * G n s / (1 - s)

/-- Entry means both cooperate now and at least one was previously on hare. -/
def referenceEntryFlux (n : Nat) (s f : F) :=
  (referenceMass n s f) ^ 2 - (referenceMass n s f - f) ^ 2

theorem reference_entry_flux (n : Nat) (s f : F) :
    referenceEntryFlux n s f = f ^ 2 * (2 * G n s / (1 - s) - 1) := by
  simp only [referenceEntryFlux, referenceMass, Field.div_eq_mul_inv]
  grind only

section Ordered
variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

private theorem div_pos {x y : F} (hx : 0 < x) (hy : 0 < y) : 0 < x / y := by
  rw [Field.div_eq_mul_inv]
  exact OrderedRing.mul_pos hx (Field.IsOrdered.inv_pos_iff.mpr hy)

private theorem div_le_of_cross {a b c d : F} (hb : 0 < b) (hd : 0 < d)
    (h : a * d ≤ c * b) : a / b ≤ c / d := by
  rw [Field.div_eq_mul_inv c d, Field.IsOrdered.le_mul_inv_iff_mul_le _ _ hd]
  apply (Field.IsOrdered.mul_le_mul_iff_of_pos_right hb).1
  have cancel : a / b * b = a := Field.div_mul_cancel (Preorder.ne_of_gt hb)
  have eqn : a / b * d * b = a * d := by grind only
  rwa [eqn]

private theorem half_times_two : (1 / 2 : F) * 2 = 1 :=
  Field.div_mul_cancel (by grind only)

theorem G_half (n : Nat) : G n (1 / 2 : F) = (n : F) := by
  have half := half_times_two (F := F)
  have den : (1 - 1 / 2 : F) ≠ 0 := by grind only
  have fair : (1 / 2 : F) / (1 - 1 / 2) = 1 := by
    apply Eq.symm
    apply (eq_div_iff den).2
    grind only
  induction n with
  | zero => simp only [G, Semiring.natCast_zero]
  | succ n ih => rw [G, ih, fair, Semiring.one_pow, Semiring.natCast_succ]

theorem reference_entry_flux_half (n : Nat) (f : F) :
    referenceEntryFlux n (1 / 2) f = f ^ 2 * (4 * (n : F) - 1) := by
  rw [reference_entry_flux, G_half]
  have half := half_times_two (F := F)
  have den : (1 - 1 / 2 : F) ≠ 0 := by grind only
  have factor : 2 * (n : F) / (1 - 1 / 2) = 4 * (n : F) := by
    apply Eq.symm
    apply (eq_div_iff den).2
    grind only
  rw [factor]

omit [Std.LawfulOrderLT F] in
private theorem positive_power {x : F} (hx : 0 < x) (n : Nat) : 0 < x ^ n := by
  induction n with
  | zero => simpa only [Semiring.pow_zero] using (OrderedRing.zero_lt_one (R := F))
  | succ n ih => rw [Semiring.pow_succ]; exact OrderedRing.mul_pos ih hx

/-- Increasing the memory from any (m) to any larger (n) adds positive levels. -/
theorem G_strict_mono {s : F} (hs : 0 < s) (hs' : s < 1) {m n : Nat} (hmn : m < n) :
    G m s < G n s := by
  have step (k : Nat) : G k s < G (k + 1) s := by
    have h := positive_power (div_pos hs (by grind only : 0 < 1 - s)) k
    rw [G]
    grind only
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases h : m = n
    · subst n; exact step m
    · exact Std.lt_trans (ih (by omega)) (step n)

def R_c [Max F] (P S : F) := P ^ 2 / (P ^ 2 + (1 - P) ^ 2 * max 1 (S / (1 - S)))

theorem below_critical_iff [Max F] [Std.LawfulOrderMax F] {R P S : F}
    (hS : 0 < S) (hSP : S < P) (hPR : P < R) (hR : R < 1) :
    lambda R P * max 1 (S / (1 - S)) < 1 ↔ R < R_c P S := by
  let m := max 1 (S / (1 - S))
  have hp : 0 < P := Std.lt_trans hS hSP
  have hp' : P < 1 := Std.lt_trans hPR hR
  have m1 : 1 ≤ m := Std.left_le_max
  have psq : 0 < P ^ 2 := OrderedRing.sq_pos (by grind only)
  have qsq : 0 < (1 - P) ^ 2 := OrderedRing.sq_pos (by grind only)
  have scale := OrderedRing.mul_pos qsq (by grind only : 0 < m)
  have den : 0 < P ^ 2 + (1 - P) ^ 2 * m := by grind only
  have den' : 0 < P ^ 2 * (1 - R) := OrderedRing.mul_pos psq (by grind only)
  have base : lambda R P * m = (1 - P) ^ 2 * R * m / (P ^ 2 * (1 - R)) := by
    simp only [lambda, rho, Field.div_eq_mul_inv, Field.inv_mul, Field.inv_pow]
    grind only
  change lambda R P * m < 1 ↔ R < P ^ 2 / (P ^ 2 + (1 - P) ^ 2 * m)
  rw [base, Field.div_eq_mul_inv, Field.div_eq_mul_inv,
    Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ den', Field.IsOrdered.lt_mul_inv_iff_mul_lt _ _ den]
  grind only

/-- A higher solo-stag success weakly lowers the critical mutual-stag payoff. -/
theorem critical_antitone [Max F] [Std.LawfulOrderMax F] {P S T : F} (hp : 0 < P)
    (hst : S ≤ T) (ht : T < 1) : R_c P T ≤ R_c P S := by
  let factor (x : F) := max 1 (x / (1 - x))
  have odds : S / (1 - S) ≤ T / (1 - T) :=
    div_le_of_cross (by grind only) (by grind only) (by grind only)
  have increase : factor S ≤ factor T :=
    Std.max_le_iff.mpr ⟨Std.left_le_max, Std.le_trans odds Std.right_le_max⟩
  have psq : 0 < P ^ 2 := OrderedRing.sq_pos (Preorder.ne_of_gt hp)
  have qsq : 0 ≤ (1 - P) ^ 2 := OrderedRing.sq_nonneg
  have pos (x : F) : 0 < P ^ 2 + (1 - P) ^ 2 * factor x := by
    have one : 1 ≤ factor x := Std.left_le_max
    have product := OrderedRing.mul_nonneg qsq (by grind only : 0 ≤ factor x)
    grind only
  have scaled := OrderedRing.mul_le_mul_of_nonneg_left increase qsq
  have larger : P ^ 2 + (1 - P) ^ 2 * factor S ≤ P ^ 2 + (1 - P) ^ 2 * factor T := by
    grind only
  exact div_le_of_cross (pos T) (pos S)
    (OrderedRing.mul_le_mul_of_nonneg_left larger (Std.le_of_lt psq))

/-- Escape to the stag end of the infinite ladder from each of its two shallow levels. -/
def hC (R P : F) := (1 - rho R) / (1 - rho R * rho P)
def hD (R P : F) := rho P * hC R P

private theorem ruin_bounds {x : F} (half : (1 / 2 : F) < x) (top : x < 1) :
    0 < rho x ∧ rho x < 1 := by
  have hc := half_times_two (F := F)
  have hx : 0 < x := by grind only
  constructor
  · exact div_pos (by grind only) hx
  · rw [rho, Field.div_eq_mul_inv, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ hx]
    grind only

private theorem ladder_denom_pos {R P : F} (hp : (1 / 2 : F) < P) (hpr : P < R)
    (hr : R < 1) : 0 < 1 - rho R * rho P := by
  obtain ⟨_, hp'⟩ := ruin_bounds hp (Std.lt_trans hpr hr)
  obtain ⟨hr₀, hr'⟩ := ruin_bounds (Std.lt_trans hp hpr) hr
  have h := OrderedRing.mul_lt_mul_of_pos_left hp' hr₀
  grind only

/-- The gambler's-ruin recurrences uniquely determine both boundary escape probabilities. -/
theorem ladder_equations_iff {R P : F} (hp : (1 / 2 : F) < P) (hpr : P < R)
    (hr : R < 1) (x y : F) :
    (x = 1 - rho R + rho R * y ∧ y = rho P * x) ↔
      (x = hC R P ∧ y = hD R P) := by
  have pos := ladder_denom_pos hp hpr hr
  have den : 1 - rho R * rho P ≠ 0 := by grind only
  constructor
  · rintro ⟨hx, hy⟩
    have xc : x = hC R P := by
      apply (eq_div_iff den).2
      rw [hy] at hx
      grind only
    exact ⟨xc, by rw [hy, xc, hD]⟩
  · rintro ⟨rfl, rfl⟩
    have cross : hC R P * (1 - rho R * rho P) = 1 - rho R :=
      Field.div_mul_cancel den
    constructor
    · rw [hD]; grind only
    · rfl

theorem transmission_cancellation {R P : F} (hp : (1 / 2 : F) < P) (hpr : P < R)
    (hr : R < 1) : (1 - rho P) * hC R P = (1 - rho R) * (1 - hD R P) := by
  obtain ⟨hc, hd⟩ := (ladder_equations_iff hp hpr hr (hC R P) (hD R P)).2 ⟨rfl, rfl⟩
  grind only

/-- Ratio of the leading entry and mark flux coefficients in the source asymptotic for
solo success at least one half. The one-player factors are P times (1 − ρ_P) outside
mutual stag and R times (1 − ρ_R) inside. -/
def K (R P S : F) :=
  (2 * (P * (1 - rho P)) ^ 2 / (1 - S)) / (2 * (R * (1 - rho R)))

theorem leading_constant {R P S : F} (hp : (1 / 2 : F) < P) (hpr : P < R) :
    K R P S = (2 * P - 1) ^ 2 / ((1 - S) * (2 * R - 1)) := by
  have hc := half_times_two (F := F)
  have single (t : F) (ht : t ≠ 0) : t * (1 - rho t) = 2 * t - 1 := by
    have balance : rho t * t = 1 - t := Field.div_mul_cancel ht
    grind only
  rw [K, single P (by grind only), single R (by grind only), Field.div_div_left]
  have two := Field.mul_inv_cancel (by grind only : (2 : F) ≠ 0)
  simp only [Field.div_eq_mul_inv, Field.inv_mul]
  grind only

end Ordered

/-- The two mixed states distinguish which hunter plays stag. -/
inductive Profile where
  | cc | cd | dc | dd
  deriving DecidableEq

def sumProfiles (v : Profile → F) := v .cc + v .cd + v .dc + v .dd

private def independentActions (x y : F) : Profile → F
  | .cc => x * y
  | .cd => x * (1 - y)
  | .dc => (1 - x) * y
  | .dd => (1 - x) * (1 - y)

/-- At depth one a stag hunter repeats on reward, and a hare hunter switches on loss.
The conditional updates of the two labelled hunters are independent. -/
def transition (R P S : F) : Profile → Profile → F
  | .cc => independentActions R R
  | .cd => independentActions S (1 - P)
  | .dc => independentActions (1 - P) S
  | .dd => independentActions (1 - P) (1 - P)

theorem transition_row_sum (R P S : F) (i : Profile) :
    sumProfiles (transition R P S i) = 1 := by
  cases i <;> simp only [sumProfiles, transition, independentActions] <;> grind only

/-- The three rooted-tree weights of the exchange quotient, split equally over CD and DC. -/
private def treeWeight (R P S : F) : Profile → F :=
  let bC := R * (1 - R)
  let cC := (1 - R) * (1 - R)
  let bD := P * (1 - P)
  let cD := (1 - P) * (1 - P)
  let v := S * (1 - P)
  let w := (1 - S) * P
  fun
  | .cc => v * cD + 2 * v * bD + w * cD
  | .cd | .dc => 2 * bC * bD + bC * cD + cC * bD
  | .dd => cC * (v + w) + 2 * bC * w

def pi1 (R P S : F) (i : Profile) :=
  treeWeight R P S i / sumProfiles (treeWeight R P S)

private theorem tree_balance (R P S : F) (j : Profile) :
    sumProfiles (fun i => treeWeight R P S i * transition R P S i j) = treeWeight R P S j := by
  cases j <;> simp only [sumProfiles, treeWeight, transition, independentActions] <;> grind only

/-- All four balance equations use columns of the labelled transition matrix. -/
theorem pi1_stationary (R P S : F) (j : Profile) :
    sumProfiles (fun i => pi1 R P S i * transition R P S i j) = pi1 R P S j := by
  have scale (u v : Profile → F) (z : F) :
      sumProfiles (fun i => u i / z * v i) = sumProfiles (fun i => u i * v i) / z := by
    simp only [sumProfiles, Field.div_eq_mul_inv]
    grind only
  unfold pi1
  rw [scale, tree_balance]

section Probabilities
variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

theorem transition_positive {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R)
    (hr : R < 1) (i j : Profile) : 0 < transition R P S i j := by
  cases i <;> cases j <;> simp only [transition, independentActions] <;>
    apply OrderedRing.mul_pos <;> grind only

private theorem plus_pos {x y : F} (hx : 0 < x) (hy : 0 < y) : 0 < x + y := by grind only

private theorem tree_positive {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R)
    (hr : R < 1) (j : Profile) : 0 < treeWeight R P S j := by
  have hp : 0 < P := Std.lt_trans hs hsp
  have hr' : 0 < R := Std.lt_trans hp hpr
  have ps : 0 < 1 - S := by grind only
  have pp : 0 < 1 - P := by grind only
  have pr : 0 < 1 - R := by grind only
  have two : (0 : F) < 2 := by grind only
  cases j <;> simp only [treeWeight] <;>
    repeat first | assumption | apply plus_pos | apply OrderedRing.mul_pos

private theorem tree_sum_positive {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R)
    (hr : R < 1) : 0 < sumProfiles (treeWeight R P S) := by
  unfold sumProfiles
  have pos := tree_positive hs hsp hpr hr
  exact plus_pos (plus_pos (plus_pos (pos .cc) (pos .cd)) (pos .dc)) (pos .dd)

theorem pi1_positive {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R) (hr : R < 1)
    (j : Profile) : 0 < pi1 R P S j :=
  div_pos (tree_positive hs hsp hpr hr j) (tree_sum_positive hs hsp hpr hr)

theorem pi1_normalized {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R)
    (hr : R < 1) : sumProfiles (pi1 R P S) = 1 := by
  let w := treeWeight R P S
  have scale (u : Profile → F) (z : F) :
      sumProfiles (fun i => u i / z) = sumProfiles u / z := by
    simp only [sumProfiles, Field.div_eq_mul_inv]
    grind only
  have h := tree_sum_positive hs hsp hpr hr
  have nz : sumProfiles w ≠ 0 := by change sumProfiles (treeWeight R P S) ≠ 0; grind only
  change sumProfiles (fun i => w i / sumProfiles w) = 1
  rw [scale, Field.div_eq_mul_inv, Field.mul_inv_cancel nz]

omit [Field F] [LT F] [Std.LawfulOrderLT F] [OrderedRing F] in
private theorem max_profile (v : Profile → F) : ∃ j, ∀ i, v i ≤ v j := by
  have comparePair (a b : Profile) : ∃ k, v a ≤ v k ∧ v b ≤ v k := by
    rcases Std.le_total (a := v a) (b := v b) with h | h
    · exact ⟨b, h, Std.le_refl _⟩
    · exact ⟨a, Std.le_refl _, h⟩
  obtain ⟨a, hcc, hcd⟩ := comparePair .cc .cd
  obtain ⟨b, hdc, hdd⟩ := comparePair .dc .dd
  obtain ⟨j, ha, hb⟩ := comparePair a b
  refine ⟨j, fun i => ?_⟩
  cases i
  · exact Std.le_trans hcc ha
  · exact Std.le_trans hcd ha
  · exact Std.le_trans hdc hb
  · exact Std.le_trans hdd hb

/-- A stationary vector of total mass one is unique. Positivity of the kernel forces a
maximizer of the ratio to the tree law to have the same ratio at every state. -/
theorem pi1_unique {R P S : F} (hs : 0 < S) (hsp : S < P) (hpr : P < R) (hr : R < 1)
    (u : Profile → F) (balance : ∀ j, sumProfiles (fun i => u i * transition R P S i j) = u j)
    (mass : sumProfiles u = 1) : u = pi1 R P S := by
  let v := pi1 R P S
  obtain ⟨j, hj⟩ := max_profile (fun i => u i / v i)
  let k := u j / v j
  let gap (i : Profile) := k * v i - u i
  have vpos (i) : 0 < v i := pi1_positive hs hsp hpr hr i
  have gapNonneg (i) : 0 ≤ gap i := by
    have h := OrderedRing.mul_le_mul_of_nonneg_right (hj i) (Std.le_of_lt (vpos i))
    change u i / v i * v i ≤ k * v i at h
    rw [Field.div_mul_cancel (Preorder.ne_of_gt (vpos i))] at h
    unfold gap
    grind only
  have top : gap j = 0 := by
    unfold gap k
    rw [Field.div_mul_cancel (Preorder.ne_of_gt (vpos j))]
    grind only
  let into (i : Profile) := gap i * transition R P S i j
  have componentNonneg (i) : 0 ≤ into i :=
    OrderedRing.mul_nonneg (gapNonneg i) (Std.le_of_lt (transition_positive hs hsp hpr hr i j))
  have total : sumProfiles into = 0 := by
    have bu := balance j
    have bv : sumProfiles (fun i => v i * transition R P S i j) = v j := pi1_stationary R P S j
    simp only [sumProfiles, into, gap] at top bu bv ⊢
    grind only
  have all (i) : u i = k * v i := by
    have hcc := componentNonneg .cc
    have hcd := componentNonneg .cd
    have hdc := componentNonneg .dc
    have hdd := componentNonneg .dd
    have zero : into i = 0 := by cases i <;> unfold sumProfiles at total <;> grind only
    have vanished := (Field.of_mul_eq_zero zero).resolve_right
      (Preorder.ne_of_gt (transition_positive hs hsp hpr hr i j))
    change k * v i - u i = 0 at vanished
    grind only
  have scale (w : Profile → F) : sumProfiles (fun i => k * w i) = k * sumProfiles w := by
    unfold sumProfiles
    grind only
  have uv : u = fun i => k * v i := funext all
  have vm : sumProfiles v = 1 := pi1_normalized hs hsp hpr hr
  rw [uv, scale, vm, Semiring.mul_one] at mass
  funext i
  rw [all, mass, Semiring.one_mul]

/-- The depth-one tree numerator grows with the solo payoff. The other three tree
weights taken together decrease with either stag payoff when hare success exceeds half. -/
theorem pi1_cc_mono {R R' P S S' : F} (hs : 0 < S) (hss : S ≤ S') (hsp : S' < P)
    (hp : (1 / 2 : F) < P) (hpr : P < R) (hrr : R ≤ R') (hr : R' < 1) :
    pi1 R P S .cc ≤ pi1 R' P S' .cc := by
  let a (r s : F) := treeWeight r P s .cc
  let b (r s : F) :=
    treeWeight r P s .cd + treeWeight r P s .dc + treeWeight r P s .dd
  let z (r s : F) := sumProfiles (treeWeight r P s)
  have half := half_times_two (F := F)
  have pc : 0 < P := by grind only
  have pq : 0 < 1 - P := by grind only
  have sq : 0 < 1 - S := by grind only
  have rGap : 0 ≤ R' - R := by grind only
  have sGap : 0 ≤ S' - S := by grind only
  have rSum : 0 < R + R' - 1 := by grind only
  have psDeficit : 0 < 2 - P - S := by grind only
  have rDeficit : 0 < 1 - R' := by grind only
  have rPlus : 0 < 2 * P + R' - 1 := by grind only
  have agrow : a R' S' - a R S = (1 - P) ^ 2 * (S' - S) := by
    simp only [a, treeWeight]; grind only
  have across := OrderedRing.mul_nonneg (OrderedRing.sq_nonneg (a := 1 - P)) sGap
  have ha : a R S ≤ a R' S' := by grind only
  let base := 2 * P * (1 - P) + P * (1 - S) + S * (1 - P)
  have basePos : 0 < base :=
    plus_pos (plus_pos (OrderedRing.mul_pos (by grind only) pq) (OrderedRing.mul_pos pc sq))
      (OrderedRing.mul_pos hs pq)
  have rdiff : b R S - b R' S =
      (R' - R) * (base + (R + R' - 1) * (2 - P - S)) := by
    simp only [b, treeWeight, base]; grind only
  have rsign := OrderedRing.mul_nonneg rGap
    (Std.le_of_lt (plus_pos basePos (OrderedRing.mul_pos rSum psDeficit)))
  have sdiff : b R' S - b R' S' = (S' - S) * ((1 - R') * (2 * P + R' - 1)) := by
    simp only [b, treeWeight]; grind only
  have ssign := OrderedRing.mul_nonneg sGap (Std.le_of_lt (OrderedRing.mul_pos rDeficit rPlus))
  have hb : b R' S' ≤ b R S := by grind only
  have hpR' : P < R' := Std.lt_of_lt_of_le hpr hrr
  have hs' : 0 < S' := Std.lt_of_lt_of_le hs hss
  have pos := tree_positive hs' hsp hpR' hr
  have bg : 0 < b R' S' := plus_pos (plus_pos (pos .cd) (pos .dc)) (pos .dd)
  have left := OrderedRing.mul_le_mul_of_nonneg_right ha (Std.le_of_lt bg)
  have right := OrderedRing.mul_le_mul_of_nonneg_left hb (Std.le_of_lt (pos .cc))
  change a R' S' * b R' S' ≤ a R' S' * b R S at right
  have splitZ (r s : F) : z r s = a r s + b r s := by
    simp only [z, sumProfiles, a, b]; grind only
  apply div_le_of_cross (tree_sum_positive hs (Std.lt_of_le_of_lt hss hsp) hpr
    (Std.lt_of_le_of_lt hrr hr)) (tree_sum_positive hs' hsp hpR' hr)
  change a R S * z R' S' ≤ a R' S' * z R S
  rw [splitZ, splitZ]
  grind only

/-- A single upper-corner calculation bounds the subcritical strip between two
solo-stag payoffs and below the critical curve. -/
theorem open_region_upper [Max F] [Std.LawfulOrderMax F] {R P S lo hi bound : F}
    (hlo : 0 < lo) (hls : lo < S) (hsh : S < hi) (hhp : hi < P)
    (hp : (1 / 2 : F) < P) (hp' : P < 1) (hpr : P < R)
    (hcritical : R < R_c P S) (htop : R_c P lo < 1)
    (hcorner : pi1 (R_c P lo) P hi .cc < bound) : pi1 R P S .cc < bound := by
  have hs := Std.lt_trans hlo hls
  have hsp := Std.lt_trans hsh hhp
  have order := critical_antitone (Std.lt_trans hs hsp) (Std.le_of_lt hls) (Std.lt_trans hsp hp')
  have upperR := Std.lt_of_lt_of_le hcritical order
  exact Std.lt_of_le_of_lt (pi1_cc_mono hs (Std.le_of_lt hsh) hhp hp hpr
    (Std.le_of_lt upperR) htop) hcorner

end Probabilities

theorem corner_one :
    pi1 (16 / 17 : Rat) (4 / 5) (1 / 2) .cc = 3757 / 10042 ∧
      (3757 / 10042 : Rat) < 3 / 8 := by decide +kernel

theorem corner_two :
    pi1 (R_c (4 / 5 : Rat) (52 / 100)) (4 / 5) (208 / 395) .cc = 220211 / 597796 ∧
      (220211 / 597796 : Rat) < 3 / 8 := by decide +kernel

theorem corner_three :
    pi1 (R_c (4 / 5 : Rat) (5499 / 10000)) (4 / 5) (1136 / 2065) .cc =
      9854063369 / 27894660164 ∧ (9854063369 / 27894660164 : Rat) < 3 / 8 := by decide +kernel

theorem three_open_regions {R S : Rat} (hcritical : R < R_c (4 / 5) S)
    (region : (47 / 100 < S ∧ S < 1 / 2 ∧ 47 / 50 < R) ∨
      (52 / 100 < S ∧ S < 208 / 395 ∧ 935 / 1000 < R) ∨
      (5499 / 10000 < S ∧ S < 1136 / 2065 ∧ 929 / 1000 < R)) :
    pi1 R (4 / 5) S .cc < 3 / 8 := by
  have strip (lo hi r₀ : Rat) (hlo : 0 < lo) (hhi : hi < 4 / 5) (hr₀ : 4 / 5 ≤ r₀)
      (cut : R_c (4 / 5) lo < 1) (corner : pi1 (R_c (4 / 5) lo) (4 / 5) hi .cc < 3 / 8)
      (h : lo < S ∧ S < hi ∧ r₀ < R) : pi1 R (4 / 5) S .cc < 3 / 8 :=
    open_region_upper hlo h.1 h.2.1 hhi (by decide +kernel) (by decide +kernel)
      (Std.lt_of_le_of_lt hr₀ h.2.2) hcritical cut corner
  rcases region with h | h | h
  · refine strip _ _ _ (by decide +kernel) (by decide +kernel) (by decide +kernel)
      (by decide +kernel) ?_ h
    have fair : R_c (4 / 5 : Rat) (47 / 100) = 16 / 17 := by decide +kernel
    rw [fair, corner_one.1]
    exact corner_one.2
  · exact strip _ _ _ (by decide +kernel) (by decide +kernel) (by decide +kernel)
      (by decide +kernel) (corner_two.1 ▸ corner_two.2) h
  · exact strip _ _ _ (by decide +kernel) (by decide +kernel) (by decide +kernel)
      (by decide +kernel) (corner_three.1 ▸ corner_three.2) h

theorem benchmark_47_50 (j : Profile) :
    pi1 (47 / 50 : Rat) (4 / 5) (1 / 2) j =
      (match j with
       | .cc => 1300 / 3517
       | .cd | .dc => 522 / 3517
       | .dd => 1173 / 3517) := by
  cases j <;> decide +kernel

end StagHuntMirage
