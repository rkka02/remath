import Init

namespace FiniteMinimax

open Lean.Grind

abbrev Vec (F : Type) (n : Nat) := Fin n → F
abbrev Matrix (F : Type) (m n : Nat) := Fin m → Fin n → F

variable {F : Type} [Field F]
local notation "V" => Vec F
local notation "Mat" => Matrix F

def total : {n : Nat} → V n → F
  | 0, _ => 0
  | n+1, f => total (fun i : Fin n => f i.castSucc) + f (Fin.last n)

private theorem linear_total {n : Nat} (u v : V n) (s t : F) :
    total (fun i => s*u i+t*v i) = s*total u + t*total v := by
  induction n with
  | zero => simp [total, Semiring.mul_zero, AddCommMonoid.add_zero]
  | succ n ih =>
    simp only [total]; rw [ih]; grind only

private theorem total_zero (n : Nat) : total (fun _ : Fin n => (0:F)) = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [total, ih, AddCommMonoid.add_zero]

private theorem total_add (u v : V n) :
    total (fun i => u i+v i) = total u+total v := by
  simpa [Semiring.one_mul] using linear_total u v 1 1

private theorem total_scale (t : F) (v : V n) :
    total (fun i => t*v i) = t*total v := by
  simpa [Semiring.zero_mul, AddCommMonoid.add_zero] using linear_total v v t 0

private theorem total_swap {m n : Nat} (f : Mat m n) :
    total (fun i => total (f i)) = total (fun j => total (fun i => f i j)) := by
  induction m with
  | zero => simp [total, total_zero]
  | succ m ih =>
    simp only [total]; rw [total_add, ← ih]

def dot (u v : V n) := total (fun i => u i*v i)
def energy (v : V n) := dot v v
def mv (A : Mat m n) (v : V n) : V m := fun i => dot (A i) v
def tr (A : Mat m n) : Mat n m := fun j i => A i j
def data (A : Mat m p) (R : Mat m n) (a : V p) (g : V n) : V m :=
  fun i => mv A a i + mv R g i

theorem adjoint_identity (A : Mat m n) (w : V m) (v : V n) :
    dot w (mv A v) = dot (mv (tr A) w) v := by
  unfold mv dot tr
  simp only [← total_scale]
  rw [total_swap]
  apply congrArg total; funext j
  rw [CommSemiring.mul_comm, ← total_scale]
  apply congrArg total; funext i; grind only

private theorem quadratic (u v : V n) (t : F) :
    energy (fun i => u i-t*v i) = energy u-2*t*dot u v+t*t*energy v := by
  induction n with
  | zero => simp only [energy, dot, total]; grind only
  | succ n ih =>
    simp only [energy, dot, total] at ih ⊢
    rw [ih]; grind only

private theorem mv_neg (A : Mat m n) (v : V n) (i : Fin m) :
    mv A (fun j => -v j) i = -mv A v i := by
  unfold mv dot
  have h := total_scale (-1) (fun j => A i j*v j)
  calc
    _ = total (fun j => -1*(A i j*v j)) := by apply congrArg total; funext j; grind only
    _ = _ := by rw [h]; grind only

private theorem energy_neg (v : V n) : energy (fun i => -v i) = energy v := by
  apply congrArg total; funext i; grind only

theorem opposite_data (A : Mat m p) (R : Mat m n) (a : V p) (g : V n)
    (null : data A R a g = fun _ => 0) :
    data A R (fun i => -a i) (fun i => -g i) = fun _ => 0 := by
  funext i
  have h := congrFun null i
  simp only [data, mv_neg] at *; grind only

def Calibrated (A : Mat m p) (w : V m) (k : Fin p) :=
  ∀ a, dot (mv (tr A) w) a = a k

def coordinate (k : Fin p) : V p := fun i => if i=k then 1 else 0

private theorem dot_coordinate (k : Fin p) (a : V p) : dot (coordinate k) a = a k := by
  induction p with
  | zero => exact Fin.elim0 k
  | succ p ih =>
    by_cases last : k=Fin.last p
    · subst k
      have h (i : Fin p) : i.castSucc ≠ Fin.last p := Fin.ne_of_lt i.castSucc_lt_last
      simp [dot, total, coordinate, h, total_zero, Semiring.one_mul, Semiring.zero_mul,
        AddCommMonoid.zero_add]
    · obtain ⟨j,rfl⟩ := Fin.exists_castSucc_eq.mpr last
      simpa [dot, total, coordinate, Fin.castSucc_inj, Ne.symm last, Semiring.zero_mul,
        AddCommMonoid.add_zero] using ih j (fun i => a i.castSucc)

theorem transpose_calibration (A : Mat m p) (w : V m) (k : Fin p) :
    mv (tr A) w = coordinate k ↔ Calibrated A w k := by
  constructor
  · intro h a; rw [h, dot_coordinate]
  · intro h; funext j
    have e := h (coordinate j)
    have comm (u v : V p) : dot u v = dot v u := by
      apply congrArg total; funext i; grind only
    rw [comm, dot_coordinate] at e
    by_cases eqn : k=j <;> simp [coordinate, eqn, Ne.symm] at e ⊢ <;> assumption

private theorem mv_scale (A : Mat m n) (z : F) (v : V n) (i : Fin m) :
    mv A (fun j => z*v j) i = z*mv A v i := by
  unfold mv dot; rw [← total_scale]
  apply congrArg total; funext j; grind only

private theorem energy_scale (z : F) (v : V n) :
    energy (fun i => z*v i) = (z*z)*energy v := by
  unfold energy dot; rw [← total_scale]
  apply congrArg total; funext i; grind only

theorem calibrated_error (A : Mat m p) (R : Mat m n) (w : V m)
    (k : Fin p) (cal : Calibrated A w k) (a : V p) (g : V n) :
    dot w (data A R a g) - a k = dot (mv (tr R) w) g := by
  have h : dot w (data A R a g) = dot w (mv A a) + dot w (mv R g) := by
    unfold dot data
    simp only [Semiring.left_distrib, total_add]
  rw [h, adjoint_identity, adjoint_identity, cal]; grind only

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

private theorem square_nonneg (x : F) : 0 ≤ x*x := by
  have h : 0 ≤ x^2 := Lean.Grind.OrderedRing.sq_nonneg
  simpa only [Semiring.pow_succ, Semiring.pow_zero, Semiring.one_mul] using h

private theorem energy_nonneg (v : V n) : 0 ≤ energy v := by
  induction n with
  | zero => exact Std.le_refl _
  | succ n ih =>
    change 0 ≤ energy (fun i : Fin n => v i.castSucc) + v (Fin.last n)*v (Fin.last n)
    have h := ih (fun i : Fin n => v i.castSucc)
    have h' := square_nonneg (v (Fin.last n))
    grind only

private theorem dot_zero_energy (u v : V n) (hz : energy v = 0) : dot u v = 0 := by
  induction n with
  | zero => rfl
  | succ n ih =>
    let last := Fin.last n
    let v' : V n := fun i => v i.castSucc
    change energy v' + v last * v last = 0 at hz
    have hp := energy_nonneg v'
    have hq := square_nonneg (v last)
    have e : energy v' = 0 := by grind only
    have l : v last = 0 := by grind only
    change dot (fun i : Fin n => u i.castSucc) v' + u last*v last = 0
    rw [ih _ _ e, l]; grind only

theorem cauchy_schwarz (u v : V n) : dot u v * dot u v ≤ energy u * energy v := by
  by_cases h : energy v = 0
  · rw [dot_zero_energy u v h, h]; grind only
  have hp : 0 < energy v := by have := energy_nonneg v; grind only
  let t := dot u v / energy v
  have cancel : t*energy v = dot u v := Field.div_mul_cancel h
  have hq := energy_nonneg (fun i => u i-t*v i)
  rw [quadratic] at hq
  have prod := OrderedRing.mul_nonneg hq (energy_nonneg v)
  have he : (energy u-2*t*dot u v+t*t*energy v)*energy v =
      energy u*energy v - dot u v*dot u v := by grind only
  rw [he] at prod; grind only

/-- Squared radii avoid adjoining irrational square roots to the rationals. -/
theorem upper_bound (A : Mat m p) (R : Mat m n) (w : V m)
    (k : Fin p) (cal : Calibrated A w k) (M : F) (a : V p) (g : V n)
    (budget : energy g ≤ M*M) :
    (dot w (data A R a g)-a k)^2 ≤ (M*M)*energy (mv (tr R) w) := by
  rw [calibrated_error A R w k cal, Semiring.pow_succ, Semiring.pow_one]
  have h := cauchy_schwarz (mv (tr R) w) g
  have b := OrderedRing.mul_le_mul_of_nonneg_left budget (energy_nonneg (mv (tr R) w))
  grind only

def absolute [DecidableLE F] (x : F) := if 0 ≤ x then x else -x

theorem upper_bound_norm [DecidableLE F] (A : Mat m p) (R : Mat m n) (w : V m)
    (k : Fin p) (cal : mv (tr A) w = coordinate k) (M q : F) (hM : 0 ≤ M) (hq : 0 ≤ q)
    (dualNorm : energy (mv (tr R) w) = q*q)
    (a : V p) (g : V n) (budget : energy g ≤ M*M) :
    absolute (dot w (data A R a g)-a k) ≤ M*q := by
  let x := dot w (data A R a g)-a k
  have h := upper_bound A R w k ((transpose_calibration A w k).mp cal) M a g budget
  change x^2 ≤ _ at h
  rw [dualNorm, Semiring.pow_succ, Semiring.pow_one] at h
  have pos := OrderedRing.mul_nonneg hM hq
  change absolute x ≤ M*q
  apply Classical.byContradiction; intro bad
  have fx : 0 < absolute x-M*q := by grind only
  have gx : 0 < absolute x+M*q := by grind only
  have product := OrderedRing.mul_pos fx gx
  unfold absolute at product
  split at product <;> grind only

theorem opposite_witnesses [DecidableLE F] (A : Mat m p) (R : Mat m n) (k : Fin p)
    (a : V p) (g : V n) (null : data A R a g = fun _ => 0) (est : V m → F) :
    absolute (a k) ≤ absolute (est (data A R a g)-a k) ∨
    absolute (a k) ≤ absolute (est (data A R (fun i => -a i) (fun i => -g i))-(-a k)) := by
  rw [null, opposite_data A R a g null]
  unfold absolute
  split <;> split <;> split <;> grind only

theorem opposite_errors (value target : Rat) :
    target.abs ≤ max (value-target).abs (value- -target).abs := by
  grind [Rat.abs_of_nonneg, Rat.abs_of_nonpos]

def UniformBound (A : Mat m p) (R : Mat m n) (k : Fin p)
    (M : F) (est : V m → F) (radiusSq : F) :=
  ∀ a g, energy g ≤ M*M → (est (data A R a g)-a k)^2 ≤ radiusSq

theorem nonlinear_lower (A : Mat m p) (R : Mat m n) (k : Fin p)
    (M : F) (a : V p) (g : V n) (null : data A R a g = fun _ => 0)
    (budget : energy g ≤ M*M) (est : V m → F) (B : F)
    (bound : UniformBound A R k M est B) : (a k)^2 ≤ B := by
  have h := bound a g budget
  have h' := bound (fun i => -a i) (fun i => -g i) (by rwa [energy_neg])
  rw [null] at h
  rw [opposite_data A R a g null] at h'
  have hv := square_nonneg (est (fun _ => 0))
  simp only [Semiring.pow_succ] at h h' ⊢
  grind only

theorem saddle_value (A : Mat m p) (R : Mat m n) (w : V m) (k : Fin p)
    (cal : Calibrated A w k) (a : V p) (g : V n) (M c : F)
    (null : data A R a g = fun _ => 0) (saturated : energy g = M*M)
    (parallel : mv (tr R) w = fun i => -c*g i) :
    (a k)^2 = (M*M)*energy (mv (tr R) w) := by
  have e := calibrated_error A R w k cal a g
  have z : dot w (fun _ => 0) = 0 := by simp [dot, total_zero, Semiring.mul_zero]
  rw [null, z, parallel] at e
  have dg : dot (fun i => -c*g i) g = -c*energy g := by
    unfold dot energy dot
    simp only [Semiring.mul_assoc, total_scale]
  have eg : energy (fun i => -c*g i) = (c*c)*energy g := by
    unfold energy dot
    rw [← total_scale]
    apply congrArg total; funext i; grind only
  rw [dg] at e
  rw [parallel, eg, ← saturated, Semiring.pow_succ, Semiring.pow_one]
  grind only

theorem exact_minimax (A : Mat m p) (R : Mat m n) (w : V m) (k : Fin p)
    (cal : Calibrated A w k) (a : V p) (g : V n) (M c : F)
    (null : data A R a g = fun _ => 0) (saturated : energy g = M*M)
    (parallel : mv (tr R) w = fun i => -c*g i) :
    UniformBound A R k M (dot w) ((M*M)*energy (mv (tr R) w)) ∧
    ∀ est B, UniformBound A R k M est B → (M*M)*energy (mv (tr R) w) ≤ B := by
  refine ⟨upper_bound A R w k cal M, ?_⟩
  intro est B h
  rw [← saddle_value A R w k cal a g M c null saturated parallel]
  exact nonlinear_lower A R k M a g null (by rw [saturated]; exact Std.le_refl _) est B h

/-- The positive square root of K_kk is represented by q. The normal equation
    constructs the adversarial pair, including the case M=0. -/
theorem normal_equation_minimax (A : Mat m p) (R : Mat m n) (w : V m) (k : Fin p)
    (col : V p) (cal : mv (tr A) w = coordinate k)
    (normal : mv R (mv (tr R) w) = mv A col) (M q : F) (pos : 0 < q)
    (root : q*q = col k) :
    UniformBound A R k M (dot w) ((M*q)^2) ∧
    ∀ est B, UniformBound A R k M est B → (M*q)^2 ≤ B := by
  have cal' := (transpose_calibration A w k).mp cal
  let v := mv (tr R) w
  have ev : energy v = col k := by
    change dot (mv (tr R) w) v = col k
    rw [← adjoint_identity, show mv R v = mv A col from normal, adjoint_identity, cal']
  have value : (M*q)^2 = (M*M)*energy v := by
    rw [ev, ← root, Semiring.pow_succ, Semiring.pow_one]; grind only
  refine ⟨?_, ?_⟩
  · rw [value]; exact upper_bound A R w k cal' M
  intro est B bound
  let s := M/q
  have scale : s*q = M := Field.div_mul_cancel (by grind only)
  let a : V p := fun j => s*col j
  let g : V n := fun j => (-s)*v j
  have null : data A R a g = fun _ => 0 := by
    funext i; change mv A (fun j => s*col j) i + mv R (fun j => -s*v j) i = 0
    rw [mv_scale, mv_scale, show mv R v = mv A col from normal]
    grind only
  have sat : energy g = M*M := by
    change energy (fun j => -s*v j) = _
    rw [energy_scale, ev, ← root]; grind only
  have lower := nonlinear_lower A R k M a g null (by rw [sat]; exact Std.le_refl _) est B bound
  have witness : a k = M*q := by change s*col k = _; rw [← root]; grind only
  rwa [witness] at lower

end FiniteMinimax
