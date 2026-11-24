import Init

namespace FairGameCancellation

open Lean.Grind

section Green

variable {F : Type} [Field F]

abbrev Kernel (F : Type) (n : Nat) := Fin n → Fin n → F

private def total : {n : Nat} → (Fin n → F) → F
  | 0, _ => 0
  | n+1, f => total (fun i : Fin n => f i.castSucc) + f (Fin.last n)

/-- One step in the DD block. Missing row mass exits DD. -/
def step (K : Kernel F n) (f : Fin n → F) (i : Fin n) : F :=
  total (fun j => K i j * f j)

def residual (K : Kernel F n) (f : Fin n → F) (i : Fin n) : F :=
  f i - step K f i

def mark (i j : Fin n) : F := if i = j then 1 else 0

/-- The columns solve the Green equations, and the Dirichlet operator is injective.
These are the defining properties of the inverse of I − K. -/
structure IsGreen (K G : Kernel F n) : Prop where
  column (i j : Fin n) : residual K (fun k => G k j) i = mark i j
  unique {f g : Fin n → F} : (∀ i, residual K f i = residual K g i) → f = g

private theorem linear_sum {n : Nat} (f g : Fin n → F) (a b : F) :
    total (fun j => a * f j + b * g j) = a * total f + b * total g := by
  induction n with
  | zero => simp only [total, Semiring.mul_zero, AddCommMonoid.add_zero]
  | succ n ih => simp only [total]; rw [ih]; grind only

private theorem linear_residual (K : Kernel F n) (f g : Fin n → F) (a b : F) (i : Fin n) :
    residual K (fun j => a * f j + b * g j) i =
      a * residual K f i + b * residual K g i := by
  unfold residual step
  have h (j : Fin n) : K i j * (a * f j + b * g j) =
      a * (K i j * f j) + b * (K i j * g j) := by grind only
  simp only [h, linear_sum]
  grind only

/-- A single nonzero exit reward at the corner. For a joint switch its weight is a². -/
theorem residence_green {K G : Kernel F n} (green : IsGreen K G) (c : Fin n)
    (weight : F) (u : Fin n → F) (eqn : ∀ i, residual K u i = weight * mark i c) :
    ∀ i, u i = weight * G i c := by
  have h := green.unique (f := u) (g := fun i => weight * G i c + 0 * G i c) (by
    intro i
    rw [linear_residual, green.column, eqn]
    grind only)
  intro i
  simpa only [Semiring.zero_mul, AddCommMonoid.add_zero] using congrFun h i

/-- Kill at the origin as well as on exit from DD. The first identity is the
taboo Green column. The second restarts it for one step at the origin, counting
an immediate return as the end of the excursion. It also holds when o = c. -/
theorem excursion_green {K G : Kernel F n} (green : IsGreen K G) (o c : Fin n)
    (nonzero : G o o ≠ 0) (weight : F) (u : Fin n → F) (atOrigin : u o = 0)
    (eqn : ∀ i, i ≠ o → residual K u i = weight * mark i c) :
    (∀ i, u i = weight * (G i c - G i o * G o c / G o o)) ∧
      weight * mark o c + step K u o = weight * G o c / G o o := by
  let k := residual K u o - weight * mark o c
  have h := green.unique (f := u) (g := fun i => weight * G i c + k * G i o) (by
    intro i
    rw [linear_residual, green.column, green.column]
    by_cases hi : i = o
    · subst i
      simp [mark, k, Semiring.mul_one]
      grind only
    · rw [eqn i hi]
      simp [mark, hi, Semiring.mul_zero, AddCommMonoid.add_zero])
  have atO := congrFun h o
  change u o = weight * G o c + k * G o o at atO
  have hk : k = -(weight * G o c / G o o) := by
    have inv := Field.mul_inv_cancel nonzero
    rw [Field.div_eq_mul_inv]
    grind only
  constructor
  · intro i
    have hi := congrFun h i
    change u i = weight * G i c + k * G i o at hi
    rw [hi, hk]
    simp only [Field.div_eq_mul_inv]
    grind only
  · change residual K u o - weight * mark o c = _ at hk
    unfold residual at hk
    grind only

/-- For distinct sites, killing at the origin subtracts the occupation following
the first visit there. Symmetry makes the correction a square. -/
theorem two_point_revisit {K G : Kernel F n} (green : IsGreen K G) (o c : Fin n)
    (_distinct : o ≠ c) (nonzero : G o o ≠ 0) (symm : G c o = G o c) (u : Fin n → F)
    (atOrigin : u o = 0) (eqn : ∀ i, i ≠ o → residual K u i = mark i c) :
    u c = G c c - G o c ^ 2 / G o o := by
  have h := (excursion_green green o c nonzero 1 u atOrigin (by
    simpa only [Semiring.one_mul] using eqn)).1 c
  simpa only [Semiring.one_mul, symm, Semiring.pow_succ, Semiring.pow_zero] using h

/-- The probability of hitting c in an origin excursion is obtained by restarting
the two-boundary harmonic function p at o. The distinct-site hypothesis rules
out a corner already hit at time zero. -/
theorem two_point_hit {K G : Kernel F n} (green : IsGreen K G) (o c : Fin n)
    (distinct : o ≠ c) (nonzero : G o o ≠ 0) (symm : G c o = G o c)
    (p : Fin n → F) (atOrigin : p o = 0) (atCorner : p c = 1)
    (harmonic : ∀ i, i ≠ o → i ≠ c → residual K p i = 0) :
    step K p o = G o c / (G o o * (G c c - G o c ^ 2 / G o o)) := by
  let flux := residual K p c
  have equations (i : Fin n) (hi : i ≠ o) : residual K p i = flux * mark i c := by
    by_cases hc : i = c
    · subst i; simp [mark, Semiring.mul_one, flux]
    · simp [mark, hc, Semiring.mul_zero, harmonic i hi hc]
  obtain ⟨values, firstStep⟩ := excursion_green green o c nonzero flux p atOrigin equations
  have corner := values c
  rw [atCorner, symm] at corner
  have hflux := Field.eq_inv_of_mul_eq_one corner.symm
  simp [mark, distinct, Semiring.mul_zero, AddCommMonoid.zero_add] at firstStep
  rw [firstStep, hflux]
  simp only [Field.div_eq_mul_inv, Field.inv_mul, Semiring.pow_succ, Semiring.pow_zero,
    Semiring.one_mul]
  grind only

/-- First positive return to the origin versus first exit. The probability of any
exit in an excursion is the complement of the one-step restarted hitting law. -/
theorem any_exit_per_excursion {K G : Kernel F n} (green : IsGreen K G) (o : Fin n)
    (p : Fin n → F) (atOrigin : p o = 1)
    (harmonic : ∀ i, i ≠ o → residual K p i = 0) :
    1 - step K p o = 1 / G o o := by
  have eqn (i : Fin n) : residual K p i = residual K p o * mark i o := by
    by_cases hi : i = o
    · subst i; simp [mark, Semiring.mul_one]
    · simp [mark, hi, Semiring.mul_zero, harmonic i hi]
  have h := residence_green green o (residual K p o) p eqn o
  rw [atOrigin] at h
  have hi := Field.eq_inv_of_mul_eq_one h.symm
  simpa only [residual, atOrigin, Field.div_eq_mul_inv, Semiring.one_mul] using hi

end Green

/-- The revisit count is killed at a positive return to the origin. At leading
order it is the diagonal limit D_w in the fair-corner asymptotics. -/
structure CornerData (F : Type) where
  origin : F
  transfer : F
  visits : F

section Ratios

variable {F : Type} [Field F]

def b (g : CornerData F) (a : F) := a^2 * g.transfer
def d (g : CornerData F) (a : F) := b g a / g.origin
def h (g : CornerData F) := g.transfer / (g.origin * g.visits)
def jImm (g : CornerData F) (a : F) := h g * a^2

private theorem product_ne {x y : F} (hx : x ≠ 0) (hy : y ≠ 0) : x*y ≠ 0 :=
  fun eqn => (Field.of_mul_eq_zero eqn).elim hx hy

private theorem quotient_ne {x y : F} (hx : x ≠ 0) (hy : y ≠ 0) : x/y ≠ 0 := by
  rw [Field.div_eq_mul_inv]
  exact product_ne hx (fun hi => hy (Field.inv_eq_zero_iff.mp hi))

private theorem ratio_of_scale {x y k : F} (hy : y ≠ 0) (scaled : x = k*y) :
    x / y = k := by
  rw [scaled, Field.div_eq_mul_inv, Semiring.mul_assoc, Field.mul_inv_cancel hy,
    Semiring.mul_one]

theorem revisit_factorization (g : CornerData F) (a : F) (hv : g.visits ≠ 0) :
    d g a = h g * a^2 * g.visits := by
  have inv := Field.mul_inv_cancel hv
  simp only [d, b, h, Field.div_eq_mul_inv, Field.inv_mul]
  grind only

theorem immediate_and_revisit_ratios (g : CornerData F) (a : F) (ho : g.origin ≠ 0)
    (ht : g.transfer ≠ 0) (hv : g.visits ≠ 0) (ha : a ≠ 0) :
    jImm g a / h g = a^2 ∧ d g a / jImm g a = g.visits := by
  have hh : h g ≠ 0 := quotient_ne ht (product_ne ho hv)
  have hj : jImm g a ≠ 0 := product_ne hh (fun e => ha (Field.of_pow_eq_zero a 2 e))
  constructor
  · apply ratio_of_scale hh
    unfold jImm
    grind only
  · apply ratio_of_scale hj
    rw [revisit_factorization g a hv]
    unfold jImm
    grind only

private theorem ratio_mul (x y u v : F) : (x*y)/(u*v) = (x/u)*(y/v) := by
  simp only [Field.div_eq_mul_inv, Field.inv_mul]
  grind only

private theorem ratio_div (x y u v : F) : (x/y)/(u/v) = (x/u)*(v/y) := by
  simp only [Field.div_eq_mul_inv, Field.inv_mul, Field.inv_inv]
  grind only

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

def Positive (g : CornerData F) : Prop := 0 < g.origin ∧ 0 < g.transfer ∧ 0 < g.visits

/-- Conditional comparison of the exact formulas. For the leading coefficients,
the factor four comes from (1 − 2w)⁻² and both origin coefficients are 4/π. -/
theorem three_way_cancellation (L B : CornerData F) (posL : Positive L) (_posB : Positive B)
    (transfer : B.transfer = 4 * L.transfer) :
    b B (1/4) / b L (1/2) = 1 ∧
    d B (1/4) / d L (1/2) = L.origin / B.origin ∧
    h B / h L = 4 * (L.origin / B.origin) * (L.visits / B.visits) ∧
    jImm B (1/4) / jImm L (1/2) = (1/4) * (h B / h L) ∧
    jImm B (1/4) / jImm L (1/2) = (L.origin / B.origin) * (L.visits / B.visits) := by
  have ht : L.transfer ≠ 0 := Preorder.ne_of_gt posL.2.1
  have tratio := ratio_of_scale ht transfer
  have coins : ((1/4 : F)^2)/((1/2 : F)^2) = 1/4 := by grind only
  have four : (1/4 : F) * 4 = 1 := Field.div_mul_cancel (by grind only)
  have rb : b B (1/4) / b L (1/2) = 1 := by
    unfold b
    rw [ratio_mul, coins, tratio, four]
  have rd : d B (1/4) / d L (1/2) = L.origin / B.origin := by
    unfold d
    rw [ratio_div, rb, Semiring.one_mul]
  have rh : h B / h L = 4 * (L.origin / B.origin) * (L.visits / B.visits) := by
    unfold h
    rw [ratio_div, tratio, ratio_mul, Semiring.mul_assoc]
  have rj : jImm B (1/4) / jImm L (1/2) = (1/4) * (h B / h L) := by
    unfold jImm
    rw [ratio_mul, coins, CommSemiring.mul_comm]
  refine ⟨rb, rd, rh, rj, ?_⟩
  rw [rj, rh]
  grind only

/-- Equal origin diagonals give the familiar three B/L coefficients. -/
theorem cancellation_equal_origins (L B : CornerData F) (posL : Positive L) (posB : Positive B)
    (transfer : B.transfer = 4 * L.transfer) (origin : B.origin = L.origin) :
    b B (1/4) / b L (1/2) = 1 ∧ d B (1/4) / d L (1/2) = 1 ∧
    h B / h L = 4 * (L.visits / B.visits) ∧
    jImm B (1/4) / jImm L (1/2) = L.visits / B.visits := by
  obtain ⟨rb, rd, rh, _, rj⟩ := three_way_cancellation L B posL posB transfer
  have same : L.origin / B.origin = 1 := by
    rw [origin, Field.div_eq_mul_inv, Field.mul_inv_cancel (Preorder.ne_of_gt posL.1)]
  rw [same] at rd rh rj
  exact ⟨rb, rd, by simpa only [Semiring.mul_one] using rh,
    by simpa only [Semiring.one_mul] using rj⟩

end Ratios

inductive Profile where
  | cc | cd | dc | dd
  deriving DecidableEq

open Profile

section DepthOne

variable {F : Type} [Field F]

/-- The two arguments are the players' next-round cooperation probabilities. -/
def independentRow (x y : F) : Profile → F
  | cc => x*y
  | cd => x*(1-y)
  | dc => (1-x)*y
  | dd => (1-x)*(1-y)

/-- Full depth-one game with independent signals, fair DD rewards, and
probability u of switching after a loss. Payoffs in the other profiles are R,T,S. -/
def depthOneKernel (u R T S : F) : Profile → Profile → F
  | cc => independentRow (1-u*(1-R)) (1-u*(1-R))
  | cd => independentRow (1-u*(1-S)) (u*(1-T))
  | dc => independentRow (u*(1-T)) (1-u*(1-S))
  | dd => independentRow (u/2) (u/2)

def mass (v : Profile → F) := v cc + v cd + v dc + v dd

theorem depth_one_rows_sum (u R T S : F) (i : Profile) : mass (depthOneKernel u R T S i) = 1 := by
  cases i <;> simp only [mass, depthOneKernel, independentRow] <;> grind only

/-- Solving a one-state DD Dirichlet system with per-round reward r. -/
def depthOneReward (K : Profile → Profile → F) (r : F) := r / (1 - K dd dd)

theorem depth_one_dirichlet (K : Profile → Profile → F) (r x : F) (exit : 1 - K dd dd ≠ 0) :
    (x = r + K dd dd * x) ↔ x = depthOneReward K r := by
  have inv := Field.mul_inv_cancel exit
  simp only [depthOneReward, Field.div_eq_mul_inv]
  constructor <;> intro e <;> grind only

structure DepthOneValues (F : Type) where
  goo : F
  goc : F
  gcc : F
  hit : F
  visits : F
  immediate : F
  excursion : F
  firstExit : F
  deriving DecidableEq

/-- At depth one the sole DD state is both o and c. A hit occurs at time zero,
and the first transition is either an exit or a positive return to o. -/
def depthOneValues (K : Profile → Profile → F) : DepthOneValues F :=
  let g := depthOneReward K 1
  let direct := K dd cc
  ⟨g, g, g, 1, 1, direct, direct, depthOneReward K direct⟩

def benchmark (u : Rat) := depthOneKernel u (4/5) (9/10) (1/5)

theorem depth_one_dd_rows :
    (benchmark 1 dd cc, benchmark 1 dd cd, benchmark 1 dd dc, benchmark 1 dd dd) =
      (1/4, 1/4, 1/4, 1/4) ∧
    (benchmark (1/2) dd cc, benchmark (1/2) dd cd, benchmark (1/2) dd dc, benchmark (1/2) dd dd) =
      (1/16, 3/16, 3/16, 9/16) := by decide +kernel

theorem depth_one_linear_values :
    depthOneValues (benchmark 1) = ⟨4/3, 4/3, 4/3, 1, 1, 1/4, 1/4, 1/3⟩ := by decide +kernel

theorem depth_one_boundary_values :
    depthOneValues (benchmark (1/2)) = ⟨16/7, 16/7, 16/7, 1, 1, 1/16, 1/16, 1/7⟩ := by decide +kernel

theorem depth_one_strict_comparison :
    (depthOneValues (benchmark (1/2))).excursion < (depthOneValues (benchmark 1)).excursion ∧
    (depthOneValues (benchmark (1/2))).firstExit < (depthOneValues (benchmark 1)).firstExit := by
  decide +kernel

def Stationary [LE F] (K : Profile → Profile → F) (v : Profile → F) : Prop :=
  mass v = 1 ∧ (∀ i, 0 ≤ v i) ∧ ∀ j, mass (fun i => v i * K i j) = v j

def linearStationary : Profile → Rat
  | cc => 3/11 | cd | dc => 2/11 | dd => 4/11

def boundaryStationary : Profile → Rat
  | cc => 59/307 | cd | dc => 66/307 | dd => 116/307

/-- The invariant law of the entire interacting game includes rounds after DD exit. -/
theorem depth_one_linear_stationary (v : Profile → Rat) :
    Stationary (benchmark 1) v ↔ v = linearStationary := by
  constructor
  · rintro ⟨norm, _, eqn⟩
    have e₁ := eqn cc
    have e₂ := eqn cd
    have e₃ := eqn dc
    change v cc + v cd + v dc + v dd = 1 at norm
    simp only [mass, benchmark, depthOneKernel, independentRow] at e₁ e₂ e₃
    funext j
    cases j <;> simp only [linearStationary] <;> grind only
  · rintro rfl
    exact ⟨by decide +kernel, by intro j; cases j <;> decide +kernel,
      by intro j; cases j <;> decide +kernel⟩

theorem depth_one_boundary_stationary (v : Profile → Rat) :
    Stationary (benchmark (1/2)) v ↔ v = boundaryStationary := by
  constructor
  · rintro ⟨norm, _, eqn⟩
    have e₁ := eqn cc
    have e₂ := eqn cd
    have e₃ := eqn dc
    change v cc + v cd + v dc + v dd = 1 at norm
    simp only [mass, benchmark, depthOneKernel, independentRow] at e₁ e₂ e₃
    funext j
    cases j <;> simp only [boundaryStationary] <;> grind only
  · rintro rfl
    exact ⟨by decide +kernel, by intro j; cases j <;> decide +kernel,
      by intro j; cases j <;> decide +kernel⟩

end DepthOne

end FairGameCancellation
