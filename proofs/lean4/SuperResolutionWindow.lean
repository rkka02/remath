import Init

namespace SuperResolutionWindow
open Lean.Grind

def factorial : Nat → Nat
  | 0 => 1
  | n+1 => (n+1)*factorial n

private theorem fac_ne (n : Nat) : (factorial n : Rat) ≠ 0 := by
  rw [ne_eq, Rat.natCast_eq_zero_iff]
  induction n with
  | zero => decide
  | succ n ih => exact Nat.mul_ne_zero (by omega) ih

/-- Sum f(i,j) over all i+j=r, in increasing order of i. -/
def diag (r : Nat) (f : Nat → Nat → Rat) : Rat :=
  match r with
  | 0 => f 0 0
  | r+1 => f 0 (r+1) + diag r (fun i j => f (i+1) j)

private theorem diag_congr (r : Nat) (f g : Nat → Nat → Rat)
    (h : ∀ i j, i+j=r → f i j = g i j) : diag r f = diag r g := by
  induction r generalizing f g with
  | zero => exact h 0 0 rfl
  | succ r ih =>
    rw [diag, diag, h 0 (r+1) (by omega), ih _ _ (by intros; apply h; omega)]

private theorem diag_linear (r : Nat) (f g : Nat → Nat → Rat) (a b : Rat) :
    diag r (fun i j => a*f i j + b*g i j) = a*diag r f + b*diag r g := by
  induction r generalizing f g with
  | zero => rfl
  | succ r ih => simp only [diag]; rw [ih]; grind only

private theorem diag_scale (r : Nat) (f : Nat → Nat → Rat) (a : Rat) :
    diag r (fun i j => a*f i j) = a*diag r f := by
  simpa [Rat.add_zero] using diag_linear r f f a 0

private theorem diag_last (r : Nat) (f : Nat → Nat → Rat) :
    diag (r+1) f = diag r (fun i j => f i (j+1)) + f (r+1) 0 := by
  induction r generalizing f with
  | zero => rfl
  | succ r ih =>
    change f 0 (r+2) + diag (r+1) _ = (f 0 (r+2) + _) + _
    rw [ih (fun i j => f (i+1) j)]
    exact (Rat.add_assoc _ _ _).symm

def coeff (i j : Nat) : Rat := (-1:Rat)^j / ((factorial i:Rat)*(factorial j:Rat))

private theorem coeff_i (i j : Nat) : ((i+1:Nat):Rat)*coeff (i+1) j = coeff i j := by
  have h := fac_ne i; have h' := fac_ne j
  have h₁ : ((i:Rat)+1) ≠ 0 := by have := Rat.natCast_nonneg (a:=i); grind only
  simp only [coeff, factorial, Rat.natCast_mul, Rat.natCast_add, Rat.natCast_ofNat,
    Field.div_eq_mul_inv, Field.inv_mul]
  have hi := Field.mul_inv_cancel h₁
  grind only

private theorem coeff_j (i j : Nat) : ((j+1:Nat):Rat)*coeff i (j+1) = -coeff i j := by
  have h₁ : ((j:Rat)+1) ≠ 0 := by have := Rat.natCast_nonneg (a:=j); grind only
  simp only [coeff, factorial, Rat.natCast_mul, Rat.natCast_add, Rat.natCast_ofNat,
    Field.div_eq_mul_inv, Field.inv_mul, Rat.pow_succ]
  have hi := Field.mul_inv_cancel h₁
  grind only

def functional (r : Nat) (f : Nat → Rat) := diag r (fun i j => coeff i j*f i)

private theorem index_i (r : Nat) (f : Nat → Rat) :
    diag (r+1) (fun i j => (i:Rat)*coeff i j*f i) = functional r (fun i => f (i+1)) := by
  rw [diag]
  simp only [Rat.natCast_ofNat, Rat.zero_mul, Rat.zero_add, coeff_i, functional]

private theorem index_j (r : Nat) (f : Nat → Rat) :
    diag (r+1) (fun i j => (j:Rat)*coeff i j*f i) = -functional r f := by
  rw [diag_last]
  simp only [Rat.natCast_ofNat, Rat.zero_mul, Rat.add_zero, coeff_j, functional]
  calc
    _ = diag r (fun i j => -1*(coeff i j*f i)) := by
      apply diag_congr; intros; grind only
    _ = _ := by rw [diag_scale]; grind only

private theorem constant_killed (r : Nat) : functional (r+1) (fun _ => 1) = 0 := by
  let f : Nat → Rat := fun _ => 1
  have eqn : ((r+1:Nat):Rat)*functional (r+1) f =
      diag (r+1) (fun i j => (i:Rat)*coeff i j*f i) +
      diag (r+1) (fun i j => (j:Rat)*coeff i j*f i) := by
    unfold functional
    rw [← diag_scale]
    have add := diag_linear (r+1) (fun i j => (i:Rat)*coeff i j*f i)
      (fun i j => (j:Rat)*coeff i j*f i) 1 1
    simp only [Rat.one_mul] at add
    rw [← add]
    apply diag_congr; intro i j h
    have he := congrArg (fun n : Nat => (n:Rat)) h
    simp only [Rat.natCast_add] at he
    grind only
  rw [index_i, index_j] at eqn
  have nz : ((r+1:Nat):Rat) ≠ 0 := fun h => Nat.succ_ne_zero r (Rat.natCast_eq_zero_iff.mp h)
  change functional (r+1) f = 0
  change _ = functional r f + -functional r f at eqn
  grind only

def powerMoment (r m : Nat) (x d : Rat) :=
  functional r (fun i => (x+(i:Rat)*d)^m)

private theorem power_step (r m : Nat) (x d : Rat) :
    powerMoment (r+1) (m+1) x d = x*powerMoment (r+1) m x d + d*powerMoment r m (x+d) d := by
  let f (i : Nat) := (x+(i:Rat)*d)^m
  have h : powerMoment (r+1) (m+1) x d =
      x*functional (r+1) f + d*diag (r+1) (fun i j => (i:Rat)*coeff i j*f i) := by
    unfold powerMoment functional
    rw [← diag_linear]
    apply diag_congr; intro i j _
    dsimp [f]; rw [Rat.pow_succ]; grind only
  rw [h, index_i]
  congr 2
  unfold powerMoment
  apply congrArg (functional r); funext i
  dsimp [f]; rw [Rat.natCast_add, Rat.natCast_ofNat]
  congr 1; grind only

theorem polynomial_moment (m r : Nat) (h : m ≤ r) (x d : Rat) :
    powerMoment r m x d = if m=r then d^r else 0 := by
  induction m generalizing r x with
  | zero =>
    cases r with
    | zero => simp [powerMoment, functional, diag, coeff, factorial, Field.div_eq_mul_inv, Field.inv_one]
    | succ r => simpa [powerMoment] using constant_killed r
  | succ m ih =>
    obtain ⟨r, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (show r ≠ 0 by omega)
    rw [power_step, ih (r+1) (by omega), ih r (by omega)]
    by_cases eqn : m=r
    · subst r; simp [Rat.pow_succ, Rat.mul_comm, Rat.zero_add]
    · simp [eqn, show m ≠ r+1 by omega, Rat.add_zero]

def weight (r i : Nat) (x d : Rat) : Rat :=
  (-1:Rat)^(r-i)*(x+(i:Rat)*d)^r /
    (d^r*(factorial i:Rat)*(factorial (r-i):Rat))

private theorem sum_weights (r : Nat) (x d : Rat) (f : Nat → Rat) :
    diag r (fun i _ => weight r i x d * f i) =
      (d^r)⁻¹ * functional r (fun i => (x+(i:Rat)*d)^r*f i) := by
  unfold functional; rw [← diag_scale]; apply diag_congr
  intro i j h
  simp only [weight, coeff, show r-i=j by omega, Field.div_eq_mul_inv, Field.inv_mul]
  grind only

private theorem power_ne (a : Rat) (h : a ≠ 0) (n : Nat) : a^n ≠ 0 := by
  induction n with
  | zero => simp
  | succ n ih => rw [Rat.pow_succ]; grind only [Rat.mul_eq_zero]

theorem normalization (r : Nat) (x d : Rat) (hd : d ≠ 0) :
    diag r (fun i _ => weight r i x d) = 1 := by
  have h := sum_weights r x d (fun _ => 1)
  simp only [Rat.mul_one] at h
  change _ = _ * powerMoment r r x d at h
  rw [h, polynomial_moment r r (by omega), ite_eq_left rfl]
  exact Field.inv_mul_cancel (power_ne d hd r)

theorem annihilation (r l : Nat) (hl : 1 ≤ l) (hr : l ≤ r) (x d : Rat)
    (nodes : ∀ i ≤ r, x+(i:Rat)*d ≠ 0) :
    diag r (fun i _ => weight r i x d * ((x+(i:Rat)*d)^l)⁻¹) = 0 := by
  rw [sum_weights]
  have h : functional r (fun i => (x+(i:Rat)*d)^r * ((x+(i:Rat)*d)^l)⁻¹) =
      powerMoment r (r-l) x d := by
    apply diag_congr; intro i j he
    have hn := power_ne _ (nodes i (by omega)) l
    have split := Semiring.pow_add (x+(i:Rat)*d) (r-l) l
    rw [Nat.sub_add_cancel hr] at split
    have inv := Field.mul_inv_cancel hn
    grind only
  rw [h, polynomial_moment _ _ (by omega), ite_eq_right (by omega : r-l ≠ r), Rat.mul_zero]

end SuperResolutionWindow
