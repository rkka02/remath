import Init

namespace PolygonParity
open Lean.Grind

/-- A vector on the cycle, represented by its periodic extension to natural indices. -/
structure Cycle (F : Type) (p : Nat) where
  val : Nat → F
  wrap : ∀ j, val (j+p) = val j

@[ext] theorem Cycle.ext {a b : Cycle F p} (h : ∀ j, a.val j = b.val j) : a = b := by
  cases a; cases b; congr; exact funext h

theorem Cycle.mod_index (a : Cycle F p) (j : Nat) : a.val (j % p) = a.val j := by
  induction j using Nat.strongRecOn with
  | ind j ih =>
    by_cases hp : p = 0
    · simp [hp]
    by_cases hj : j < p
    · simp [Nat.mod_eq_of_lt hj]
    rw [Nat.mod_eq_sub_mod (by omega : p ≤ j), ih (j-p) (by omega),
        ← a.wrap (j-p), Nat.sub_add_cancel (by omega)]

variable {F : Type} [Field F]

def incidence (a : Cycle F p) : Cycle F p where
  val j := a.val j + a.val (j+1)
  wrap j := by simp only [show j+p+1 = j+1+p by omega, a.wrap]

/-- The alternating sum of 2k+1 consecutive entries, starting with a plus sign. -/
def alternating (b : Nat → F) : Nat → Nat → F
  | 0, j => b j
  | k+1, j => b j - b (j+1) + alternating b k (j+2)

private theorem alt_period (b : Cycle F p) (k j : Nat) :
    alternating b.val k (j+p) = alternating b.val k j := by
  induction k generalizing j with
  | zero => exact b.wrap j
  | succ k ih =>
    simp only [alternating, show j+p+1 = j+1+p by omega, show j+p+2 = j+2+p by omega,
      b.wrap, ih]

private theorem alt_edges (a : Cycle F p) (k j : Nat) :
    alternating (incidence a).val k j = a.val j + a.val (j+(2*k+1)) := by
  induction k generalizing j with
  | zero => rfl
  | succ k ih =>
    rw [alternating, ih (j+2), show j+2+(2*k+1) = j+(2*(k+1)+1) by omega]
    simp only [incidence]
    grind only

private theorem adjacent_windows (b : Nat → F) (k j : Nat) :
    alternating b k j + alternating b k (j+1) = b j + b (j+(2*k+1)) := by
  induction k generalizing j with
  | zero => rfl
  | succ k ih =>
    have h := ih (j+2)
    simp only [alternating, show j+2+(2*k+1) = j+(2*(k+1)+1) by omega] at *
    grind only

def oddInverse (b : Cycle F (2*k+1)) : Cycle F (2*k+1) where
  val j := alternating b.val k j / 2
  wrap j := by rw [alt_period]

theorem odd_left_inverse (two : (2:F) ≠ 0) (a : Cycle F (2*k+1)) :
    oddInverse (incidence a) = a := by
  apply Cycle.ext; intro j
  change alternating (incidence a).val k j / 2 = _
  rw [alt_edges, a.wrap, Field.div_eq_mul_inv]
  have h := Field.mul_inv_cancel two
  grind only

theorem odd_right_inverse (two : (2:F) ≠ 0) (b : Cycle F (2*k+1)) :
    incidence (oddInverse b) = b := by
  apply Cycle.ext; intro j
  change alternating b.val k j / 2 + alternating b.val k (j+1) / 2 = _
  have h := adjacent_windows b.val k j
  rw [b.wrap] at h
  simp only [Field.div_eq_mul_inv]
  have h₂ := Field.mul_inv_cancel two
  grind only

/-- The conventional finite sum with the exponent equal to the offset from j. -/
def signedSum (f : Nat → F) (j : Nat) : Nat → F
  | 0 => 0
  | n+1 => signedSum f j n + (-1:F)^n * f (j+n)

private theorem signed_head (f : Nat → F) (j n : Nat) :
    signedSum f j (n+1) = f j - signedSum f (j+1) n := by
  induction n with
  | zero => simp only [signedSum, Semiring.pow_zero, Nat.add_zero]; grind only
  | succ n ih =>
    change signedSum f j (n+1) + (-1:F)^(n+1)*f (j+(n+1)) =
      f j - (signedSum f (j+1) n + (-1:F)^n * f ((j+1)+n))
    rw [ih, Semiring.pow_succ]
    rw [show j+(n+1)=j+1+n by omega]; grind only

private theorem alternating_sum (f : Nat → F) (k j : Nat) :
    alternating f k j = signedSum f j (2*k+1) := by
  induction k generalizing j with
  | zero => simp only [alternating, signedSum]; grind only
  | succ k ih =>
    rw [show 2*(k+1)+1 = (2*k+1)+1+1 by omega, signed_head, signed_head,
      alternating, ih]; grind only

theorem odd_formula (two : (2:F) ≠ 0) (a : Cycle F (2*k+1)) (j : Nat) :
    a.val j = signedSum (fun t => (incidence a).val (t % (2*k+1))) j (2*k+1) / 2 := by
  simp only [Cycle.mod_index]
  rw [← alternating_sum]
  exact (congrArg (fun b : Cycle F (2*k+1) => b.val j) (odd_left_inverse two a)).symm

theorem odd_bijective (two : (2:F) ≠ 0) (k : Nat) :
    (∀ a b : Cycle F (2*k+1), incidence a = incidence b → a = b) ∧
    (∀ b : Cycle F (2*k+1), ∃ a, incidence a = b) := by
  constructor
  · intro a b h
    rw [← odd_left_inverse two a, h, odd_left_inverse two b]
  · intro b; exact ⟨_, odd_right_inverse two b⟩

private theorem even_sign (k : Nat) : (-1:F)^(2*k) = 1 := by
  induction k with
  | zero => simp [Semiring.pow_zero]
  | succ k ih =>
    rw [show 2*(k+1) = 2*k+1+1 by omega, Semiring.pow_succ, Semiring.pow_succ, ih]
    grind only

def alternatingCycle (k : Nat) (c : F) : Cycle F (2*k) where
  val j := (-1:F)^j * c
  wrap j := by rw [Semiring.pow_add, even_sign, Semiring.mul_one]

theorem even_kernel (k : Nat) (a : Cycle F (2*k)) :
    (∀ j, (incidence a).val j = 0) ↔ a = alternatingCycle k (a.val 0) := by
  constructor
  · intro h
    apply Cycle.ext; intro j
    change a.val j = (-1:F)^j * a.val 0
    induction j with
    | zero => simp [Semiring.pow_zero, Semiring.one_mul]
    | succ j ih =>
      have hj := h j
      change a.val j + a.val (j+1) = 0 at hj
      rw [Semiring.pow_succ]; grind only
  · intro h j
    conv => lhs; rw [h]
    change (-1:F)^j * _ + (-1:F)^(j+1) * _ = 0
    rw [Semiring.pow_succ]; grind only

theorem even_kernel_parametrization (k : Nat) (c : F) :
    (alternatingCycle k c).val 0 = c ∧ ∀ j, (incidence (alternatingCycle k c)).val j = 0 := by
  have h : (alternatingCycle k c).val 0 = c := by
    simp [alternatingCycle, Semiring.pow_zero, Semiring.one_mul]
  exact ⟨h, (even_kernel k _).2 (by rw [h])⟩

def shift (z : F) (a : Cycle F p) := a.val 0 + z * a.val 1

theorem shift_recovery {z : F} (hz : z ≠ 1) (a : Cycle F p) :
    a.val 0 = (shift z a - z*(incidence a).val 0)/(1-z) := by
  have h : 1-z ≠ 0 := by grind only
  have hi := Field.mul_inv_cancel h
  simp only [shift, incidence, Field.div_eq_mul_inv]
  grind only

theorem propagate (a : Cycle F p) (j : Nat) :
    a.val (j+1) = (incidence a).val j - a.val j := by unfold incidence; grind only

theorem augmented_injective {z : F} (hz : z ≠ 1) (a b : Cycle F p)
    (he : incidence a = incidence b) (hs : shift z a = shift z b) : a = b := by
  apply Cycle.ext; intro j
  induction j with
  | zero => rw [shift_recovery hz a, he, hs, ← shift_recovery hz b]
  | succ j ih => rw [propagate a, propagate b, he, ih]

theorem half_step (two : (2:F) ≠ 0) (a : Cycle F p) :
    a.val 0 = (shift (-1) a + (incidence a).val 0)/2 ∧
    a.val 1 = ((incidence a).val 0 - shift (-1) a)/2 := by
  have h := Field.mul_inv_cancel two
  simp only [shift, incidence, Field.div_eq_mul_inv]
  constructor <;> grind only

end PolygonParity
