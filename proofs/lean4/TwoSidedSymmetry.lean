import PolygonParity

namespace TwoSidedSymmetry
open Lean.Grind

def Integral (x : Rat) := ∃ z : Int, x = z

private theorem consecutive_ratio {a b : Rat} (m : Int) (ha : a ≠ 0)
    (h : Integral (m*b/a)) (h' : Integral ((m+1:Int)*b/a)) :
    ∃ z : Int, (z : Rat)*a = b := by
  obtain ⟨i, hi⟩ := h
  obtain ⟨j, hj⟩ := h'
  have h₀ := Rat.div_mul_cancel (a := (m:Rat)*b) ha
  have h₁ := Rat.div_mul_cancel (a := ((m+1:Int):Rat)*b) ha
  rw [hi] at h₀; rw [hj] at h₁
  refine ⟨j-i, ?_⟩
  simp only [Rat.intCast_sub, Rat.intCast_add, Rat.intCast_one] at *
  grind only

private theorem multiple_ge {a b : Rat} (ha : 0 < a) (hb : 0 < b)
    (z : Int) (h : (z:Rat)*a = b) : a ≤ b := by
  have hz : 0 < (z:Rat) := (Rat.mul_pos_iff_of_pos_right ha).mp (by rwa [h])
  have hz' := Rat.intCast_pos.mp hz
  have hz₁ : (1:Rat) ≤ (z:Rat) := Rat.intCast_le_intCast.mpr (show (1:Int) ≤ z by omega)
  have := Rat.mul_le_mul_of_nonneg_right hz₁ (Rat.le_of_lt ha)
  grind only

theorem consecutive_collapse {a b : Rat} (ha : 0 < a) (hb : 0 < b) (m : Int)
    (h₀ : Integral (m*b/a)) (h₁ : Integral ((m+1:Int)*b/a))
    (h₂ : Integral (m*a/b)) (h₃ : Integral ((m+1:Int)*a/b)) : a = b := by
  obtain ⟨i, hi⟩ := consecutive_ratio m (by grind only : a ≠ 0) h₀ h₁
  obtain ⟨j, hj⟩ := consecutive_ratio m (by grind only : b ≠ 0) h₂ h₃
  exact Rat.le_antisymm (multiple_ge ha hb i hi) (multiple_ge hb ha j hj)

variable {F : Type} [Field F]

/-- Coordinatewise in any dimension. Convexity is unnecessary for this implication. -/
theorem opposite_edges_center {ι : Type} (k : Nat) (v : PolygonParity.Cycle (ι → F) (2*k))
    (opposite : ∀ j i, v.val (j+k+1) i - v.val (j+k) i = -(v.val (j+1) i-v.val j i))
    (j : Nat) : (fun i => v.val j i + v.val (j+k) i) = fun i => v.val 0 i + v.val k i := by
  funext i
  induction j with
  | zero => simp only [Nat.zero_add]
  | succ j ih =>
    have h := opposite j i
    rw [show j+1+k = j+k+1 by omega]
    grind only

def moment (w : F → F) (n : Nat) : List F → F
  | [] => 0
  | x::xs => w x*x^n + moment w n xs

private theorem moment_zeros (xs : List F) (w : F → F) (h : ∀ x ∈ xs, w x = 0) (n : Nat) :
    moment w n xs = 0 := by
  induction xs with
  | nil => rfl
  | cons x xs ih =>
    rw [moment, h x (by simp), ih (by grind)]
    grind only

private theorem eliminate (xs : List F) (w : F → F) (a : F) (n : Nat) :
    moment (fun x => (x-a)*w x) n xs = moment w (n+1) xs - a*moment w n xs := by
  induction xs with
  | nil => simp only [moment]; grind only
  | cons x xs ih => simp only [moment, ih, Semiring.pow_succ]; grind only

/-- The first as many positive powers as there are distinct, nonzero nodes suffice. -/
theorem vandermonde (xs : List F) (distinct : xs.Nodup) (nz : ∀ x ∈ xs, x ≠ 0)
    (w : F → F) :
    (∀ n < xs.length, moment w (n+1) xs = 0) ↔ ∀ x ∈ xs, w x = 0 := by
  refine ⟨?_, fun h n _ => moment_zeros xs w h (n+1)⟩
  induction xs generalizing w with
  | nil => simp
  | cons a xs ih =>
    intro h
    obtain ⟨fresh, tail⟩ := List.nodup_cons.mp distinct
    have reduced : ∀ n < xs.length, moment (fun x => (x-a)*w x) (n+1) xs = 0 := by
      intro n hn
      have h₀ := h n (by simp; omega)
      have h₁ := h (n+1) (by simp; omega)
      rw [eliminate]; simp only [moment] at h₀ h₁
      rw [Semiring.pow_succ a (n+1)] at h₁
      grind only
    have vanish := ih tail (by grind) _ reduced
    have tailZero : ∀ x ∈ xs, w x = 0 := by
      intro x hx
      have h₁ := vanish x hx
      have diff : x-a ≠ 0 := by grind only
      have inv := Field.mul_inv_cancel diff
      grind only
    have first := h 0 (by simp)
    rw [moment, moment_zeros xs w tailZero, Semiring.pow_succ, Semiring.pow_zero] at first
    have inv := Field.mul_inv_cancel (nz a (by simp))
    intro x hx
    rcases List.mem_cons.mp hx with rfl | hx
    · grind only
    · exact tailZero x hx

section Groups
variable [DecidableEq F]

def charge (x : F) : List (F × F) → F
  | [] => 0
  | (z,c)::rest => (if x=z then c else 0) + charge x rest

def atomMoment (n : Nat) : List (F × F) → F
  | [] => 0
  | (z,c)::rest => c*z^n + atomMoment n rest

omit [DecidableEq F] in
private theorem moment_add (xs : List F) (u v : F → F) (n : Nat) :
    moment (fun x => u x+v x) n xs = moment u n xs + moment v n xs := by
  induction xs with
  | nil => simp [moment, Semiring.add_zero]
  | cons x xs ih => simp only [moment, ih]; grind only

private theorem spike (xs : List F) (hd : xs.Nodup) (z c : F) (n : Nat) :
    moment (fun x => if x=z then c else 0) n xs = if z ∈ xs then c*z^n else 0 := by
  induction xs with
  | nil => simp [moment]
  | cons x xs ih =>
    obtain ⟨hx, ht⟩ := List.nodup_cons.mp hd
    rw [moment, ih ht]
    by_cases h : x=z
    · subst x; simp [hx, Semiring.add_zero]
    · simp [h, Ne.symm h, Semiring.zero_mul, AddCommMonoid.zero_add] <;> grind only

private theorem collect (atoms : List (F × F)) (xs : List F) (hd : xs.Nodup)
    (covers : ∀ b ∈ atoms, b.1 ∈ xs) (n : Nat) :
    moment (fun x => charge x atoms) n xs = atomMoment n atoms := by
  induction atoms with
  | nil => exact moment_zeros xs _ (by simp [charge]) n
  | cons b bs ih =>
    obtain ⟨z,c⟩ := b
    have hz := covers (z,c) (by simp)
    simp only [charge, atomMoment, moment_add, spike xs hd, ite_eq_left hz, ih (by grind)]

theorem pure_atom_grouping (atoms : List (F × F)) (xs : List F) (hd : xs.Nodup)
    (nz : ∀ x ∈ xs, x ≠ 0) (covers : ∀ b ∈ atoms, b.1 ∈ xs) :
    (∀ n < xs.length, atomMoment (n+1) atoms = 0) ↔ ∀ x ∈ xs, charge x atoms = 0 := by
  simp only [← collect atoms xs hd covers]
  exact vandermonde xs hd nz _

end Groups
end TwoSidedSymmetry
