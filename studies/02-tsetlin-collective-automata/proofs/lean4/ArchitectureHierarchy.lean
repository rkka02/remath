import Init

namespace ArchitectureHierarchy
open Lean.Grind

variable {F : Type} [Field F]

/-- Probability that both players are rewarded at a symmetric profile. -/
def jointReward (p κ : F) : F := p^2 + κ*p*(1-p)
/-- Probability that both players are penalized at a symmetric profile. -/
def jointPenalty (p κ : F) : F := (1-p)^2 + κ*p*(1-p)

/-- Payoff threshold for the linear and randomized-boundary architectures. -/
def F_L (p κ : F) : F := jointReward p κ / (jointReward p κ + jointPenalty p κ)
/-- Payoff threshold for the survey's Krinsky D architecture. -/
def F_D (p κ : F) : F := p + (1-κ)*p*(1-p)
/-- Payoff threshold for Krylov's private-coin architecture. -/
def F_K (p κ : F) : F := 2*p / (1 + p^2 + κ*p*(1-p))

/-- Effective reward and correlation after each player independently thins penalties. -/
def privateCoin (p κ : F) : F × F := ((1+p)/2, κ*p/(1+p))

/-- Cooperation probability against a persistent defector in the weak-reward regime. -/
def weakRewardFraction (p s : F) : F := (1-2*p) / (2*(1-p-s))

private theorem eq_div_of_mul_eq {x y d : F} (hd : d ≠ 0) (h : x*d = y) :
    x = y/d := by
  calc
    x = x * (d * d⁻¹) := by rw [Field.mul_inv_cancel hd, Semiring.mul_one]
    _ = y/d := by rw [← Semiring.mul_assoc, h, Field.div_eq_mul_inv]

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

private theorem denominator_positivity {p κ : F} (hp : 0 < p) (hp₁ : p < 1) (hκ : 0 ≤ κ) :
    0 < 1-2*(1-κ)*p*(1-p) ∧ 0 < 1+p-(1-κ)*p*(1-p) := by
  have hq : 0 < 1-p := by grind only
  have hp₂ : 0 < p^2 := OrderedRing.sq_pos (Preorder.ne_of_gt hp)
  have hq₂ : 0 < (1-p)^2 := OrderedRing.sq_pos (Preorder.ne_of_gt hq)
  have hcov : 0 ≤ κ*p*(1-p) :=
    OrderedRing.mul_nonneg (OrderedRing.mul_nonneg hκ (Preorder.le_of_lt hp)) (Preorder.le_of_lt hq)
  have l : 1-2*(1-κ)*p*(1-p) = p^2 + (1-p)^2 + 2*(κ*p*(1-p)) := by grind only
  have k : 1+p-(1-κ)*p*(1-p) = 1 + p^2 + κ*p*(1-p) := by grind only
  rw [l, k]
  constructor <;> grind only

theorem krinsky_minus_linear {p κ : F} (hp : 0 < p) (hp₁ : p < 1) (hκ : 0 ≤ κ) :
    F_D p κ - F_L p κ =
      2*(1-κ)*p*(1-p)^2*(1-(1-κ)*p) / (1-2*(1-κ)*p*(1-p)) := by
  have hd := Preorder.ne_of_gt (denominator_positivity hp hp₁ hκ).1
  have den : jointReward p κ + jointPenalty p κ = 1-2*(1-κ)*p*(1-p) := by
    unfold jointReward jointPenalty
    grind only
  unfold F_D F_L
  rw [den]
  apply eq_div_of_mul_eq hd
  have cancel := Field.div_mul_cancel (x := jointReward p κ) hd
  unfold jointReward at *
  grind only

theorem krylov_minus_krinsky {p κ : F} (hp : 0 < p) (hp₁ : p < 1) (hκ : 0 ≤ κ) :
    F_K p κ - F_D p κ =
      p*(1-p)*(1-(1-κ)*p)*(1-(1-κ)*(1-p)) / (1+p-(1-κ)*p*(1-p)) := by
  have hd := Preorder.ne_of_gt (denominator_positivity hp hp₁ hκ).2
  have den : 1 + p^2 + κ*p*(1-p) = 1+p-(1-κ)*p*(1-p) := by grind only
  unfold F_K F_D
  rw [den]
  apply eq_div_of_mul_eq hd
  have cancel := Field.div_mul_cancel (x := 2*p) hd
  grind only

private theorem remaining_factors_positive {p κ : F} (hp : 0 < p) (hp₁ : p < 1)
    (hκ : 0 ≤ κ) : 0 < 1-(1-κ)*p ∧ 0 < 1-(1-κ)*(1-p) := by
  have hq : 0 < 1-p := by grind only
  have hκp := OrderedRing.mul_nonneg hκ (Preorder.le_of_lt hp)
  have hκq := OrderedRing.mul_nonneg hκ (Preorder.le_of_lt hq)
  have left : 1-(1-κ)*p = (1-p) + κ*p := by grind only
  have right : 1-(1-κ)*(1-p) = p + κ*(1-p) := by grind only
  rw [left, right]
  constructor <;> grind only

private theorem quotient_positive {x d : F} (hx : 0 < x) (hd : 0 < d) : 0 < x/d := by
  rw [Field.div_eq_mul_inv]
  exact OrderedRing.mul_pos hx (Field.IsOrdered.inv_pos_iff.mpr hd)

theorem linear_lt_krinsky {p κ : F} (hp : 0 < p) (hp₁ : p < 1) (hκ : 0 ≤ κ) (hκ₁ : κ < 1) :
    F_L p κ < F_D p κ := by
  apply OrderedAdd.sub_pos_iff.mp
  rw [krinsky_minus_linear hp hp₁ hκ]
  apply quotient_positive _ (denominator_positivity hp hp₁ hκ).1
  have hq : 0 < 1-p := by grind only
  have hq₂ := OrderedRing.sq_pos (Preorder.ne_of_gt hq)
  have hh : 0 < 2*(1-κ) := by grind only
  exact OrderedRing.mul_pos (OrderedRing.mul_pos (OrderedRing.mul_pos hh hp) hq₂)
    (remaining_factors_positive hp hp₁ hκ).1

theorem krinsky_lt_krylov {p κ : F} (hp : 0 < p) (hp₁ : p < 1) (hκ : 0 ≤ κ) :
    F_D p κ < F_K p κ := by
  apply OrderedAdd.sub_pos_iff.mp
  rw [krylov_minus_krinsky hp hp₁ hκ]
  apply quotient_positive _ (denominator_positivity hp hp₁ hκ).2
  obtain ⟨ha,hb⟩ := remaining_factors_positive hp hp₁ hκ
  have hq : 0 < 1-p := by grind only
  exact OrderedRing.mul_pos (OrderedRing.mul_pos (OrderedRing.mul_pos hp hq) ha) hb

theorem synchronized_thresholds {p : F} (hp : 0 < p) (hp₁ : p < 1) :
    F_L p 1 = p ∧ F_D p 1 = p ∧ p < F_K p 1 ∧ F_K p 1 = 2*p/(1+p) := by
  have hd : F_D p 1 = p := by unfold F_D; grind only
  have hden : jointReward p 1 + jointPenalty p 1 = 1 := by
    unfold jointReward jointPenalty
    grind only
  have hl : F_L p 1 = p := by
    rw [F_L, hden, Field.div_eq_mul_inv, Field.inv_one, Semiring.mul_one]
    unfold jointReward
    grind only
  have hlt := krinsky_lt_krylov hp hp₁ (κ := 1) (by grind only)
  rw [hd] at hlt
  refine ⟨hl, hd, hlt, ?_⟩
  unfold F_K
  rw [show 1 + p^2 + 1*p*(1-p) = 1+p by grind only]

/-- Effective two-reward and two-penalty probabilities, scaled by the four coin outcomes. -/
theorem private_coin_joint_law {p : F} (κ : F) (hp : 0 < p) :
    let (p', κ') := privateCoin p κ
    4*jointReward p' κ' = (1+p)^2 + κ*p*(1-p) ∧
    4*jointPenalty p' κ' = (1-p)^2 + κ*p*(1-p) := by
  let x := (privateCoin p κ).1
  let k := (privateCoin p κ).2
  change 4*jointReward x k = _ ∧ 4*jointPenalty x k = _
  have hx : x*2 = 1+p := Field.div_mul_cancel (by grind only : (2:F) ≠ 0)
  have hk : k*(1+p) = κ*p := Field.div_mul_cancel (by grind only : 1+p ≠ 0)
  have hy : (1-x)*2 = 1-p := by grind only
  have cov : 4*(k*x*(1-x)) = κ*p*(1-p) := calc
    _ = (k*(x*2))*((1-x)*2) := by grind only
    _ = _ := by rw [hx, hy, hk]
  have xx : 4*x^2 = (1+p)^2 := calc
    _ = (x*2)^2 := by grind only
    _ = _ := by rw [hx]
  have yy : 4*(1-x)^2 = (1-p)^2 := calc
    _ = ((1-x)*2)^2 := by grind only
    _ = _ := by rw [hy]
  unfold jointReward jointPenalty
  constructor <;> grind only

/-- Undo the effective reward transformation on the linear threshold.
    Nonnegativity of the raw joint reward probability allows either sign of correlation. -/
theorem krylov_private_coin_reduction {p κ : F} (hp : 0 < p) (hA : 0 ≤ jointReward p κ) :
    F_K p κ = 2*F_L (privateCoin p κ).1 (privateCoin p κ).2 - 1 := by
  let a := jointReward (privateCoin p κ).1 (privateCoin p κ).2
  let b := jointPenalty (privateCoin p κ).1 (privateCoin p κ).2
  let d := 1 + p^2 + κ*p*(1-p)
  obtain ⟨ha,hb⟩ := private_coin_joint_law κ hp
  change 4*a = _ at ha
  change 4*b = _ at hb
  have hden : d = 2*(a+b) := by dsimp only [d]; grind only
  have hdiff : a-b = p := by grind only
  have hd : 0 < d := by unfold jointReward at hA; dsimp only [d]; grind only
  have hab : a+b ≠ 0 := by grind only
  have cancel := Field.div_mul_cancel (x := a) hab
  change 2*p/d = 2*(a/(a+b))-1
  symm
  apply eq_div_of_mul_eq (Preorder.ne_of_gt hd)
  rw [hden]
  calc
    _ = 4*((a/(a+b))*(a+b))-2*(a+b) := by grind only
    _ = 2*p := by rw [cancel]; grind only

theorem krylov_threshold_iff {p κ : F} (r : F) (hp : 0 < p) (hA : 0 ≤ jointReward p κ) :
    F_K p κ < r ↔ F_L (privateCoin p κ).1 (privateCoin p κ).2 < (1+r)/2 := by
  rw [krylov_private_coin_reduction hp hA]
  have h := Field.div_mul_cancel (x := 1+r) (by grind only : (2:F) ≠ 0)
  grind only

theorem benchmark_thresholds :
    F_L (7/10 : Rat) (13/63) = 4/5 ∧ F_D (7/10 : Rat) (11/21) = 4/5 ∧
    F_K (7/10 : Rat) 1 = 14/17 ∧ 4/5 < F_K (7/10 : Rat) 1 := by decide +kernel

theorem volkonskii_threshold_split :
    F_L (13/20 : Rat) 0 = 169/218 ∧ F_L (13/20 : Rat) 0 < 17/20 ∧
    17/20 < F_D (13/20 : Rat) 0 ∧ F_D (13/20 : Rat) 0 = 351/400 := by decide +kernel

theorem volkonskii_linear_odds_ratio :
    ((17/20 : Rat)/(3/20)) / ((169/218)/(49/218)) = 833/507 ∧ 1 < (833/507 : Rat) := by
  decide +kernel

theorem weak_reward_reversal_witness :
    (19/20 : Rat) + 1/10 = 21/20 ∧ 1 < (21/20 : Rat) ∧
    weakRewardFraction (1/5 : Rat) (1/10) = 3/7 ∧
    F_D (1/5 : Rat) 0 = 9/25 ∧ F_K (1/5 : Rat) 0 = 5/13 ∧
    F_D (1/5 : Rat) 0 < F_K (1/5 : Rat) 0 ∧ F_K (1/5 : Rat) 0 < 9/20 := by decide +kernel

end ArchitectureHierarchy
