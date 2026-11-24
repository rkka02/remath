import Init

namespace EscapeGeometry
open Lean.Grind
attribute [local instance] Semiring.natCast

variable {F : Type} [Field F]

def odds (p : F) := p / (1 - p)

/-- Erosion increments in long/short order. A reward gives −1 and a penalty gives +1. -/
structure StepLaw (F : Type) where
  mm : F
  mp : F
  pm : F
  pp : F

def ddLaw (p κ : F) : StepLaw F :=
  let q := 1 - p
  ⟨p^2 + κ*p*q, (1-κ)*p*q, (1-κ)*p*q, q^2 + κ*p*q⟩

/-- Multiply each joint weight by exp(s U), where x = exp(s) and U is the long step. -/
def tiltLong (x : F) (w : StepLaw F) : StepLaw F :=
  ⟨w.mm / x, w.mp / x, w.pm * x, w.pp * x⟩

def naturalTilt (p κ : F) := tiltLong (odds p) (ddLaw p κ)

def StepLaw.mass (w : StepLaw F) := w.mm + w.mp + w.pm + w.pp
def StepLaw.longDrift (w : StepLaw F) := -w.mm - w.mp + w.pm + w.pp
def StepLaw.shortDrift (w : StepLaw F) := -w.mm + w.mp - w.pm + w.pp

theorem natural_tilt_weights {p : F} (κ : F) (hp : p ≠ 0) (hq : 1-p ≠ 0) :
    naturalTilt p κ =
      ⟨(1-p)*(p + κ*(1-p)), (1-κ)*(1-p)^2,
       (1-κ)*p^2, p*((1-p) + κ*p)⟩ := by
  have ip := Field.mul_inv_cancel hp
  have iq := Field.mul_inv_cancel hq
  unfold naturalTilt tiltLong odds ddLaw
  simp only [Field.div_eq_mul_inv]
  congr 1 <;> grind only

theorem tilted_mass_and_drifts {p : F} (κ : F) (hp : p ≠ 0) (hq : 1-p ≠ 0) :
    (naturalTilt p κ).mass = 1 ∧
    (naturalTilt p κ).longDrift = 2*p-1 ∧
    (naturalTilt p κ).shortDrift = (2*p-1)*(2*κ-1) := by
  rw [natural_tilt_weights κ hp hq]
  simp only [StepLaw.mass, StepLaw.longDrift, StepLaw.shortDrift]
  exact ⟨by grind only, by grind only, by grind only⟩

/-- The second moment of V − wU under the natural tilt, with w = 2κ−1. -/
theorem tilted_transverse_variance {p : F} (κ : F) (hp : p ≠ 0) (hq : 1-p ≠ 0) :
    let t := naturalTilt p κ
    let w := 2*κ - 1
    (t.mm + t.pp)*(1-w)^2 + (t.mp + t.pm)*(1+w)^2 =
      (1-w)*(1 + w*(2*p-1)^2) := by
  rw [natural_tilt_weights κ hp hq]
  dsimp only
  grind only

/-- The first-return multiplier for switching on a weak loss with probability u. -/
def phi (u z : F) := (1-u) + u^2*z/(1-(1-u)*z)

theorem phi_one (z : F) : phi 1 z = z := by
  unfold phi
  rw [show 1-(1-1)*z = 1 by grind only, Field.div_eq_mul_inv, Field.inv_one]
  grind only

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

private theorem div_pos {a b : F} (ha : 0 < a) (hb : 0 < b) : 0 < a/b := by
  rw [Field.div_eq_mul_inv]
  exact OrderedRing.mul_pos ha (Field.IsOrdered.inv_pos_iff.mpr hb)

private theorem half_double : (2 : F) * (1/2) = 1 := by
  have hi := Field.mul_inv_cancel (show (2 : F) ≠ 0 by grind only)
  rw [Field.div_eq_mul_inv]
  grind only

def optimalCorrelation (γ : F) := (1 + 1/γ)/2

theorem optimal_correlation_interior {γ : F} (hγ : 1 < γ) :
    1/2 < optimalCorrelation γ ∧ optimalCorrelation γ < 1 := by
  have hh := half_double (F := F)
  have hg : 0 < γ := by grind only
  have hr := div_pos (show (0:F) < 1 by grind only) hg
  have hu : (1:F)/γ < 1 := by
    rw [Field.div_eq_mul_inv, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ hg]
    grind only
  have eq := Field.div_mul_cancel (x := 1+1/γ) (show (2:F) ≠ 0 by grind only)
  unfold optimalCorrelation
  constructor <;> grind only

/-- In particular the tilted weights at the optimum are strictly positive. -/
theorem tilted_weights_positive {p κ : F} (hp : 0 < p) (hp₁ : p < 1)
    (hκ : 0 ≤ κ) (hκ₁ : κ < 1) :
    let t := naturalTilt p κ
    0 < t.mm ∧ 0 < t.mp ∧ 0 < t.pm ∧ 0 < t.pp := by
  have hq : 0 < 1-p := by grind only
  have hk : 0 < 1-κ := by grind only
  have hkp := OrderedRing.mul_nonneg hκ (Preorder.le_of_lt hp)
  have hkq := OrderedRing.mul_nonneg hκ (Preorder.le_of_lt hq)
  have hp₂ := OrderedRing.mul_pos hp hp
  have hq₂ := OrderedRing.mul_pos hq hq
  rw [natural_tilt_weights κ (Preorder.ne_of_gt hp) (Preorder.ne_of_gt hq)]
  exact ⟨OrderedRing.mul_pos hq (by grind only), OrderedRing.mul_pos hk (by grind only),
    OrderedRing.mul_pos hk (by grind only), OrderedRing.mul_pos hp (by grind only)⟩

theorem drift_alignment_iff {p κ γ : F} (hp : 1/2 < p) (hp₁ : p < 1) (hγ : 1 < γ) :
    (naturalTilt p κ).longDrift = γ * (naturalTilt p κ).shortDrift ↔
      κ = optimalCorrelation γ := by
  have hh := half_double (F := F)
  have hδ : 0 < 2*p-1 := by grind only
  have ht := tilted_mass_and_drifts κ (show p ≠ 0 by grind only)
    (show 1-p ≠ 0 by grind only)
  rw [ht.2.1, ht.2.2]
  have ig := Field.mul_inv_cancel (show γ ≠ 0 by grind only)
  have id := Field.mul_inv_cancel (Preorder.ne_of_gt hδ)
  unfold optimalCorrelation
  simp only [Field.div_eq_mul_inv] at *
  constructor <;> intro h <;> grind only

def curvature (p γ : F) :=
  2*γ*(2*p-1) / ((1 - 1/γ)*(1 + (2*p-1)^2/γ))

theorem curvature_pos {p γ : F} (hp : 1/2 < p) (hγ : 1 < γ) :
    0 < curvature p γ := by
  have hh := half_double (F := F)
  have hδ : 0 < 2*p-1 := by grind only
  have hg : 0 < γ := by grind only
  have hrec : (1:F)/γ < 1 := by
    rw [Field.div_eq_mul_inv, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ hg]
    grind only
  have hsq := OrderedRing.mul_pos hδ hδ
  have hterm := div_pos (show 0 < (2*p-1)^2 by grind only) hg
  exact div_pos (OrderedRing.mul_pos (OrderedRing.mul_pos (by grind only) hg) hδ)
    (OrderedRing.mul_pos (by grind only) (by grind only))

private theorem phi_den_pos {u z : F} (hu : 0 ≤ u) (hz : 0 < z) (hz₁ : z < 1) :
    0 < 1-(1-u)*z := by
  have := OrderedRing.mul_nonneg hu (Preorder.le_of_lt hz)
  grind only

private theorem phi_times_den {u z : F} (h : 0 < 1-(1-u)*z) :
    phi u z * (1-(1-u)*z) = 1-u-z+2*u*z := by
  have e := Field.div_mul_cancel (x := u^2*z) (Preorder.ne_of_gt h)
  unfold phi
  grind only

theorem phi_squeeze {u z : F} (hu : 0 < u) (hu₁ : u < 1) (hz : 0 < z) (hz₁ : z < 1) :
    z < phi u z ∧ phi u z < 1 := by
  have hd := phi_den_pos (Preorder.le_of_lt hu) hz hz₁
  have hmul := Field.div_mul_cancel (x := u^2*z) (Preorder.ne_of_gt hd)
  have hlow := OrderedRing.mul_pos (show 0 < 1-u by grind only)
    (OrderedRing.mul_pos (show 0 < 1-z by grind only) (show 0 < 1-z by grind only))
  have hhigh := OrderedRing.mul_pos hu (show 0 < 1-z by grind only)
  constructor
  · apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right hd).mp
    unfold phi
    grind only
  · apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right hd).mp
    unfold phi
    grind only

/-- Strict antitonicity on positive u includes the deterministic endpoint u₂ = 1. -/
theorem phi_strict_antitone {u₁ u₂ z : F} (hu₁ : 0 < u₁) (hu : u₁ < u₂)
    (hz : 0 < z) (hz₁ : z < 1) : phi u₂ z < phi u₁ z := by
  have hd₁ := phi_den_pos (show 0 ≤ u₁ by grind only) hz hz₁
  have hd₂ := phi_den_pos (show 0 ≤ u₂ by grind only) hz hz₁
  have pos := OrderedRing.mul_pos (show 0 < u₂-u₁ by grind only)
    (OrderedRing.mul_pos (show 0 < 1-z by grind only) (show 0 < 1-z by grind only))
  apply (Field.IsOrdered.mul_lt_mul_iff_of_pos_right (OrderedRing.mul_pos hd₁ hd₂)).mp
  calc
    phi u₂ z * _ = (phi u₂ z * (1-(1-u₂)*z)) * (1-(1-u₁)*z) := by grind only
    _ = (1-u₂-z+2*u₂*z) * (1-(1-u₁)*z) := by rw [phi_times_den hd₂]
    _ < (1-u₁-z+2*u₁*z) * (1-(1-u₂)*z) := by grind only
    _ = (phi u₁ z * (1-(1-u₁)*z)) * (1-(1-u₂)*z) := by rw [phi_times_den hd₁]
    _ = _ := by grind only

theorem phi_half {z : F} (hz : 0 < z) (hz₁ : z < 1) :
    phi (1/2) z = 1/(2-z) ∧ phi 1 z < phi (1/2) z := by
  have hh := half_double (F := F)
  have hd := phi_den_pos (u := (1/2 : F)) (by grind only) hz hz₁
  have e := Field.div_mul_cancel (x := (1/2 : F)^2*z) (Preorder.ne_of_gt hd)
  have f := Field.div_mul_cancel (x := (1 : F)) (show 2-z ≠ 0 by grind only)
  constructor
  · unfold phi
    grind only
  · apply phi_strict_antitone (by grind only) (by grind only) hz hz₁

/-- The B feasibility condition z_D ≥ Φ_{1/2}(z_C) implies strict L feasibility. -/
theorem hesitant_feasibility {zD zC : F} (hz : 0 < zC) (hz₁ : zC < 1)
    (hB : phi (1/2) zC ≤ zD) : phi 1 zC < zD :=
  Std.lt_of_lt_of_le (phi_half hz hz₁).2 hB

private theorem div_lt_div_iff {a b c d : F} (hb : 0 < b) (hd : 0 < d) :
    a/b < c/d ↔ a*d < c*b := by
  rw [Field.div_eq_mul_inv, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ hb,
    Field.div_eq_mul_inv, show c*d⁻¹*b=(c*b)*d⁻¹ by grind only,
    Field.IsOrdered.lt_mul_inv_iff_mul_lt _ _ hd]

theorem odds_lt_iff {p r : F} (hp : p < 1) (hr : r < 1) : odds p < odds r ↔ p < r := by
  unfold odds
  rw [div_lt_div_iff (by grind only) (by grind only)]
  constructor <;> intro h <;> grind only

theorem flip_threshold_odds :
    (240 : Rat)/80 = 3 ∧ optimalCorrelation (3 : Rat) = 2/3 ∧
    odds (3/5 : Rat) = 3/2 ∧
    odds (27/35 : Rat) = odds (3/5 : Rat)^3 ∧ odds (27/35 : Rat) = 27/8 ∧
    odds (81/97 : Rat) = odds (3/5 : Rat)^4 ∧ odds (81/97 : Rat) = 81/16 := by decide +kernel

/-- The whole open interval, expressed directly in the odds of cooperation. -/
theorem flip_interval_iff {r : F} (hr : r < 1) :
    (27/35 < r ∧ r < 81/97) ↔
      (odds (3/5)^3 < odds r ∧ odds r < odds (3/5)^4) := by
  have low : odds (27/35 : F) = odds (3/5 : F)^3 := by unfold odds; grind only
  have high : odds (81/97 : F) = odds (3/5 : F)^4 := by unfold odds; grind only
  rw [← low, ← high, odds_lt_iff (by grind only) hr, odds_lt_iff hr (by grind only)]

theorem flip_benchmark :
    (27/35 : Rat) < 4/5 ∧ (4/5 : Rat) < 81/97 ∧
    odds (3/5 : Rat)^3 < odds (4/5 : Rat) ∧ odds (4/5 : Rat) < odds (3/5 : Rat)^4 := by
  decide +kernel

/-- The mixed short-coordinate return equation at a longitudinal tilt x = exp(s). -/
def mixedReturnPolynomial (t s x z : F) :=
  let m := t/x + (1-t)*x
  m*s*z^2 - z + m*(1-s)

theorem perfect_correlation_barrier_data :
    mixedReturnPolynomial (9/10 : Rat) (1/5) 2 0 = 13/25 ∧
    mixedReturnPolynomial (9/10 : Rat) (1/5) 2 (2/3) = -4/45 ∧
    odds (3/5 : Rat)/2 = 3/4 ∧
    odds (3/5 : Rat)*2^2 = 6 ∧ (3/2 : Rat)^4 < 6 := by decide +kernel

/-- At x = 2 the short DD weight is 3/4. Both return rules satisfy the interface bound. -/
theorem perfect_correlation_return {z : F} (hz : 0 < z) (hz₁ : z ≤ 1)
    (hroot : mixedReturnPolynomial (9/10) (1/5) 2 z = 0) :
    z < 2/3 ∧ phi 1 z < 3/4 ∧ phi (1/2) z < 3/4 := by
  have hsq := OrderedRing.mul_nonneg (Preorder.le_of_lt hz) (show 0 ≤ 1-z by grind only)
  unfold mixedReturnPolynomial at hroot
  have h : z < 2/3 := by grind only
  have hz' : z < 1 := by grind only
  rw [phi_one, (phi_half hz hz').1]
  refine ⟨h, by grind only, ?_⟩
  rw [Field.div_eq_mul_inv, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ (by grind only)]
  grind only

/-- The ordinary player's reward in a linear public good with a frozen tagged player. -/
def publicPayoff (N : Nat) (b h d : F) (cooperatingOthers : Nat) (defects : Bool) :=
  b + h*(cooperatingOthers : F)/((N-1 : Nat) : F) + if defects then d else 0

def groupAdvantage (N : Nat) (b h d : F) (tagCooperates : Bool) :=
  if tagCooperates then
    publicPayoff N b h d (N-1) false - publicPayoff N b h d 1 true
  else
    publicPayoff N b h d (N-2) false - publicPayoff N b h d 0 true

def publicGoodCutoff (N : Nat) (h : F) := h*((N-2 : Nat) : F)/((N-1 : Nat) : F)

theorem public_good_advantage {N : Nat} (hN : 3 ≤ N) (b h d : F) (tagCooperates : Bool) :
    groupAdvantage N b h d tagCooperates = publicGoodCutoff N h - d := by
  have e : ((N-2 : Nat) : F) + 1 = ((N-1 : Nat) : F) := by
    rw [← Semiring.natCast_succ, show N-2+1=N-1 by omega]
  have hh := OrderedRing.pos_natCast_of_pos (R := F) (N-1) (by omega)
  have hi := Field.mul_inv_cancel (Preorder.ne_of_gt hh)
  cases tagCooperates <;> simp only [groupAdvantage, publicPayoff, publicGoodCutoff,
    Bool.false_eq_true, ↓reduceIte, Semiring.natCast_zero, Semiring.natCast_one,
    Field.div_eq_mul_inv] <;> grind only

theorem public_good_balance {N : Nat} (hN : 3 ≤ N) (b h d : F) (tagCooperates : Bool) :
    (groupAdvantage N b h d tagCooperates = 0 ↔ d = publicGoodCutoff N h) ∧
    (0 < groupAdvantage N b h d tagCooperates ↔ d < publicGoodCutoff N h) ∧
    (groupAdvantage N b h d tagCooperates < 0 ↔ publicGoodCutoff N h < d) := by
  rw [public_good_advantage hN]
  grind only

theorem public_good_three_player (tagCooperates : Bool) :
    publicGoodCutoff 3 (1/4 : Rat) = 1/8 ∧
    groupAdvantage 3 (9/20 : Rat) (1/4) (7/100) tagCooperates = 11/200 ∧
    groupAdvantage 3 (9/20 : Rat) (1/4) (1/8) tagCooperates = 0 ∧
    groupAdvantage 3 (9/20 : Rat) (1/4) (4/25) tagCooperates = -7/200 := by
  cases tagCooperates <;> decide +kernel

abbrev MemoryState := Nat × Nat

/-- The labeled L ladder runs from deepest C at 0 to deepest D at 2n−1. -/
def linearMove (n i : Nat) (win : Bool) : Nat :=
  if i < n then (if win then i-1 else i+1)
  else if win then min (i+1) (2*n-1) else i-1

def memoryStates (m n : Nat) : List MemoryState :=
  (List.range (2*m)).flatMap fun i => (List.range (2*n)).map fun j => (i,j)

/-- Tagged payoff in the separate two-player memory-upgrade example in the notes. -/
def memoryPayoff (m n : Nat) (x : MemoryState) : Rat :=
  if x.1 < m then (if x.2 < n then 11/20 else 39/100)
  else if x.2 < n then 99/100 else 2/5

/-- Common rewards in a homogeneous profile and independent rewards in a mixed profile. -/
def memoryNext (m n : Nat) (f : MemoryState → Rat) (x : MemoryState) : Rat :=
  let atOutcome := fun u v => f (linearMove m x.1 u, linearMove n x.2 v)
  let p := memoryPayoff m n x
  if decide (x.1 < m) == decide (x.2 < n) then
    p * atOutcome true true + (1-p) * atOutcome false false
  else
    let q := memoryPayoff n m (x.2,x.1)
    p*q * atOutcome true true + p*(1-q) * atOutcome true false +
      (1-p)*q * atOutcome false true + (1-p)*(1-q) * atOutcome false false

def weightedTotal (π f : MemoryState → Rat) : List MemoryState → Rat
  | [] => 0
  | x :: xs => π x * f x + weightedTotal π f xs

def memoryMean (m n : Nat) (π : MemoryState → Rat) :=
  weightedTotal π (memoryPayoff m n) (memoryStates m n)

def cooperationMass (m n : Nat) (π : MemoryState → Rat) :=
  weightedTotal π (fun x => if x.1 < m ∧ x.2 < n then 1 else 0) (memoryStates m n)

def memoryKernel (m n : Nat) (x y : MemoryState) :=
  memoryNext m n (fun z => if z = y then 1 else 0) x

/-- Direct finite checks of normalization, nonnegativity, and each column of πP = π. -/
def stationaryRows (m n : Nat) (π : MemoryState → Rat) : Prop :=
  let states := memoryStates m n
  weightedTotal π (fun _ => 1) states = 1 ∧
  states.all (fun x => decide (0 ≤ π x)) = true ∧
  states.all (fun y => decide (weightedTotal π (fun x => memoryKernel m n x y) states = π y)) = true

private def tableValue (rowLength : Nat) (entries : List Int) (den : Nat) (x : MemoryState) : Rat :=
  ((entries[x.1*rowLength + x.2]?.getD 0 : Int) : Rat) / (den : Rat)

def equalSmallLaw : MemoryState → Rat := tableValue 2 [4, 0, 0, 3] 7

def unequalSmallLaw : MemoryState → Rat := tableValue 2
  [847286103826, 559196139645, 682964183394, 889123310355,
   27892789328145, 951285347604, 17542606221855, 46364915852811] 95730166487635

theorem adjacent_memory_stationarity :
    stationaryRows 1 1 equalSmallLaw ∧ stationaryRows 2 1 unequalSmallLaw := by
  unfold stationaryRows
  decide +kernel

theorem adjacent_memory_witness :
    memoryMean 1 1 equalSmallLaw = 17/35 ∧
    memoryMean 2 1 unequalSmallLaw = 65314004318137/95730166487635 ∧
    memoryMean 1 1 equalSmallLaw < memoryMean 2 1 unequalSmallLaw ∧
    cooperationMass 1 1 equalSmallLaw = 4/7 ∧
    cooperationMass 2 1 unequalSmallLaw = 306050057444/19146033297527 ∧
    cooperationMass 2 1 unequalSmallLaw < cooperationMass 1 1 equalSmallLaw := by
  decide +kernel

private theorem weight_zero (xs : List MemoryState) (f : MemoryState → Rat) :
    weightedTotal (fun _ => 0) f xs = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih => rw [weightedTotal, ih]; grind only

private theorem split_weight (ys : List MemoryState) (p : Rat) (u v f : MemoryState → Rat) :
    weightedTotal (fun y => p*u y + v y) f ys =
      p*weightedTotal u f ys + weightedTotal v f ys := by
  induction ys with
  | nil => simp only [weightedTotal]; grind only
  | cons y ys ih => simp only [weightedTotal, ih]; grind only

private theorem sum_by_columns (xs ys : List MemoryState) (π f : MemoryState → Rat)
    (k : MemoryState → MemoryState → Rat) :
    weightedTotal π (fun x => weightedTotal (k x) f ys) xs =
      weightedTotal (fun y => weightedTotal π (fun x => k x y) xs) f ys := by
  induction xs with
  | nil => exact (weight_zero ys f).symm
  | cons x xs ih => simp only [weightedTotal, ih, split_weight]

private theorem weight_congr (xs : List MemoryState) (u v f : MemoryState → Rat)
    (h : ∀ x ∈ xs, u x = v x) : weightedTotal u f xs = weightedTotal v f xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    rw [weightedTotal, weightedTotal, h x (by simp),
      ih (fun y hy => h y (List.mem_cons_of_mem x hy))]

private theorem poisson_sum (xs : List MemoryState) (π r next bias : MemoryState → Rat) (μ : Rat)
    (h : ∀ x ∈ xs, r x + next x - bias x = μ) :
    weightedTotal π r xs + weightedTotal π next xs - weightedTotal π bias xs =
      μ * weightedTotal π (fun _ => 1) xs := by
  induction xs with
  | nil => simp only [weightedTotal]; grind only
  | cons x xs ih =>
    have hx := congrArg (fun t : Rat => π x*t) (h x (by simp))
    have ht := ih (fun y hy => h y (List.mem_cons_of_mem x hy))
    simp only [weightedTotal]
    grind only

private def poissonCheck (m n : Nat) (bias : MemoryState → Rat) (μ : Rat) :=
  let xs := memoryStates m n
  xs.all fun x => decide
    (memoryPayoff m n x + weightedTotal (memoryKernel m n x) bias xs - bias x = μ)

/-- The finite Poisson certificate applies to every normalized stationary distribution. -/
private theorem certified_mean {m n : Nat} {π bias : MemoryState → Rat} {μ : Rat}
    (hπ : stationaryRows m n π) (hc : poissonCheck m n bias μ = true) : memoryMean m n π = μ := by
  obtain ⟨hnorm, _, hrows⟩ := hπ
  let xs := memoryStates m n
  have inv : weightedTotal π (fun x => weightedTotal (memoryKernel m n x) bias xs) xs =
      weightedTotal π bias xs := by
    rw [sum_by_columns]
    apply weight_congr
    intro s hs
    exact of_decide_eq_true (List.all_eq_true.mp hrows s hs)
  have h := poisson_sum xs π (memoryPayoff m n)
    (fun x => weightedTotal (memoryKernel m n x) bias xs) bias μ
    (fun s hs => of_decide_eq_true (List.all_eq_true.mp hc s hs))
  rw [inv, show weightedTotal π (fun _ => 1) xs = 1 from hnorm] at h
  change weightedTotal π (memoryPayoff m n) xs = μ
  grind only

theorem adjacent_memory_payoffs {π₁ π₂ : MemoryState → Rat}
    (h₁ : stationaryRows 1 1 π₁) (h₂ : stationaryRows 2 1 π₂) :
    memoryMean 1 1 π₁ = 17/35 ∧ memoryMean 2 1 π₂ = 65314004318137/95730166487635 ∧
      memoryMean 1 1 π₁ < memoryMean 2 1 π₂ := by
  let b₁ := tableValue 2 [0, -382099, 894281, -188418] 1318926
  let b₂ := tableValue 2 [0, -10542136511283, 19664144631000, 16883216999917,
    189511917811000, 60581316179917, 190440882531400, 162489980087917] 57438099892581
  have w₁ := certified_mean h₁ (show poissonCheck 1 1 b₁ (17/35) = true by decide +kernel)
  have w₂ := certified_mean h₂ (show
    poissonCheck 2 1 b₂ (65314004318137/95730166487635) = true by decide +kernel)
  exact ⟨w₁, w₂, by rw [w₁, w₂]; decide +kernel⟩

/-- The state after consecutive shared penalties from deepest CC. -/
def lossPath (m n : Nat) : Nat → MemoryState
  | 0 => (0,0)
  | t+1 =>
    let x := lossPath m n t
    (linearMove m x.1 false, linearMove n x.2 false)

def lossPathProbability (m n : Nat) : Nat → Rat
  | 0 => 1
  | t+1 =>
    let x := lossPath m n t
    let q := 1 - memoryPayoff m n x
    let bothLose := if decide (x.1 < m) == decide (x.2 < n) then q
      else q * (1 - memoryPayoff n m (x.2,x.1))
    lossPathProbability m n t * bothLose

theorem forty_loss_path :
    lossPath 40 40 40 = (40,40) ∧ lossPath 41 40 40 = (40,40) ∧
    memoryPayoff 40 40 (lossPath 40 40 40) = 2/5 ∧
    memoryPayoff 41 40 (lossPath 41 40 40) = 39/100 ∧
    lossPathProbability 40 40 40 = (9/20 : Rat)^40 ∧
    lossPathProbability 41 40 40 = (9/20 : Rat)^40 ∧ 0 < (9/20 : Rat)^40 := by decide +kernel

end EscapeGeometry
