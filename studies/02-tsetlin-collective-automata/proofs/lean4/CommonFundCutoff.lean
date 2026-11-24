import Init

/-! The productive branch of the quorum Common Fund. At a fixed population
fraction the two roles have geometric stationary depth weights. Their ratio
determines the quorum equation and its change with depth and fund share. -/
namespace CommonFundCutoff
open Lean.Grind

section Quota
variable {F : Type} [Field F]

/-- A free rider and a volunteer both receive the pooled part of the cost. -/
def freePay (H c x α : F) := H - c * α * x
def volunteerPay (H c x α : F) := freePay H c x α - c * (1 - α)

/-- Finite geometric sum of the stationary depth weights within one role. -/
def weights (r : F) : Nat → F
  | 0 => 0
  | n+1 => weights r n + r^n

/-- The common boundary switch probability cancels in ratios of episode lengths. -/
def duration (n : Nat) (p : F) := weights (p / (1-p)) n / (1-p)

def depthWeight (p : F) (j : Nat) := (p/(1-p))^j / (1-p)

/-- Adding one depth level adds precisely its stationary weight to the role mass. -/
theorem duration_add_level (p : F) (n : Nat) :
    duration (n+1) p = duration n p + depthWeight p n := by
  simp only [duration, weights, depthWeight, Field.div_eq_mul_inv]; grind only

/-- Detailed balance on each adjacent depth edge, and across the role switch.
Holding at the reflecting ends contributes no flux across either edge. -/
theorem ladder_detailed_balance {pc pd : F} (hc : pc ≠ 1) (hd : pd ≠ 1) (ν : F) (n : Nat) :
    depthWeight pc n * pc = depthWeight pc (n+1) * (1-pc) ∧
    depthWeight pd n * pd = depthWeight pd (n+1) * (1-pd) ∧
    depthWeight pc 0 * (1-pc) * ν = depthWeight pd 0 * (1-pd) * ν := by
  have edge (p : F) (hp : p ≠ 1) :
      depthWeight p n * p = depthWeight p (n+1) * (1-p) := by
    have hq : 1-p ≠ 0 := by grind only
    unfold depthWeight
    rw [Field.div_mul_cancel hq, Semiring.pow_succ]
    simp only [Field.div_eq_mul_inv]; grind only
  refine ⟨edge pc hc, edge pd hd, ?_⟩
  simp only [depthWeight, Semiring.pow_zero, Field.div_mul_cancel (by grind only : 1-pc ≠ 0),
    Field.div_mul_cancel (by grind only : 1-pd ≠ 0)]

def response (n : Nat) (pc pd : F) := duration n pc / (duration n pc + duration n pd)

/-- At x = θ this is the quota-balance ratio of equation (1) of the memory notes. -/
def quotaRatio (n : Nat) (H c θ α : F) :=
  duration n (freePay H c θ α) / duration n (volunteerPay H c θ α)

def A₁ (H c θ : F) := (c*θ - (1-H)*(1-2*θ)) / (2*c*θ*(1-θ))
def nashShare (L H c : F) := 1 - (H-L)/c

/-- Welfare per player at a given fraction, with the high base at equality. -/
def welfare [LE F] [DecidableLE F] (L H c θ x : F) :=
  (if θ ≤ x then H else L) - c*x

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

private theorem frac_lt {a b c d : F} (hb : 0 < b) (hd : 0 < d) :
    a/b < c/d ↔ a*d < c*b := by
  simp only [Field.div_eq_mul_inv]
  rw [Field.IsOrdered.lt_mul_inv_iff_mul_lt _ _ hd,
    show a * b⁻¹ * d = (a*d) * b⁻¹ by grind only, Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ hb]

private theorem frac_eq {a b c d : F} (hb : 0 < b) (hd : 0 < d) :
    a/b = c/d ↔ a*d = c*b := by
  have := Field.div_mul_cancel (x := a) (Preorder.ne_of_gt hb)
  have := Field.div_mul_cancel (x := c) (Preorder.ne_of_gt hd)
  constructor <;> intro h <;> grind

private theorem quotient_pos {a b : F} (ha : 0 < a) (hb : 0 < b) : 0 < a/b := by
  rw [Field.div_eq_mul_inv]
  exact OrderedRing.mul_pos ha (Field.IsOrdered.inv_pos_iff.mpr hb)

omit [Std.LawfulOrderLT F] in
private theorem pow_positive {r : F} (hr : 0 < r) (n : Nat) : 0 < r^n := by
  induction n with
  | zero => rw [Semiring.pow_zero]; exact OrderedRing.zero_lt_one
  | succ n ih => rw [Semiring.pow_succ]; exact OrderedRing.mul_pos ih hr

private theorem powers_mono {r s : F} (hr : 0 < r) (hrs : r ≤ s) (n : Nat) : r^n ≤ s^n := by
  induction n with
  | zero => simp [Semiring.pow_zero]
  | succ n ih =>
    rw [Semiring.pow_succ, Semiring.pow_succ]
    calc
      _ ≤ s^n * r := OrderedRing.mul_le_mul_of_nonneg_right ih (by grind)
      _ ≤ _ := OrderedRing.mul_le_mul_of_nonneg_left hrs (Preorder.le_of_lt (pow_positive (by grind : 0 < s) n))

private theorem weights_nonneg {r : F} (hr : 0 < r) (n : Nat) : 0 ≤ weights r n := by
  induction n with
  | zero => simp [weights]
  | succ n ih => have := pow_positive hr n; rw [weights]; grind only

private theorem weights_pos {r : F} (hr : 0 < r) {n : Nat} (hn : 1 ≤ n) : 0 < weights r n := by
  cases n with
  | zero => omega
  | succ n => have := weights_nonneg hr n; have := pow_positive hr n; rw [weights]; grind only

private theorem weights_mono {r s : F} (hr : 0 < r) (hrs : r ≤ s) (n : Nat) :
    weights r n ≤ weights s n := by
  induction n with
  | zero => simp [weights]
  | succ n ih => have := powers_mono hr hrs n; simp only [weights]; grind only

private theorem odds_pos {p : F} (hp : 0 < p) (hp' : p < 1) : 0 < p/(1-p) :=
  quotient_pos hp (by grind only)

private theorem odds_strict {p q : F} (hpq : p < q) (hq : q < 1) :
    p/(1-p) < q/(1-q) := by
  apply (frac_lt (by grind only) (by grind only)).2
  grind only

private theorem duration_pos {p : F} (hp : 0 < p) (hp' : p < 1) {n : Nat} (hn : 1 ≤ n) :
    0 < duration n p :=
  quotient_pos (weights_pos (odds_pos hp hp') hn) (by grind only)

/-- Each additional increment in the win probability lengthens a positive-depth episode. -/
theorem duration_strict {p q : F} (hp : 0 < p) (hpq : p < q) (hq : q < 1)
    {n : Nat} (hn : 1 ≤ n) : duration n p < duration n q := by
  let u := weights (p/(1-p)) n
  let v := weights (q/(1-q)) n
  have hor := odds_pos hp (by grind only : p < 1)
  have huv : u ≤ v := weights_mono hor (Preorder.le_of_lt (odds_strict hpq hq)) n
  have hu : 0 < u := weights_pos hor hn
  apply (frac_lt (by grind only) (by grind only)).2
  change u*(1-q) < v*(1-p)
  have := OrderedRing.mul_lt_mul_of_pos_left (by grind only : 1-q < 1-p) hu
  have := OrderedRing.mul_le_mul_of_nonneg_right huv (by grind only : 0 ≤ 1-p)
  grind only

/-- The newest term in the higher-odds sum has a larger share of its mass.
This cross product also covers odds equal to one. -/
private theorem last_term_strict {r s : F} (hr : 0 < r) (hrs : r < s) (n : Nat) :
    weights s (n+1) * r^(n+1) < weights r (n+1) * s^(n+1) := by
  have hs : 0 < s := by grind only
  have step (k : Nat) (h : weights s k * r^k ≤ weights r k * s^k) :
      weights s (k+1) * r^(k+1) < weights r (k+1) * s^(k+1) := by
    have h' : weights s (k+1)*r^k ≤ weights r (k+1)*s^k := by
      simp only [weights]; grind only
    have pos := OrderedRing.mul_pos (weights_pos hr (by omega : 1 ≤ k+1)) (pow_positive hs k)
    have left := OrderedRing.mul_le_mul_of_nonneg_right h' (Preorder.le_of_lt hr)
    have right := OrderedRing.mul_lt_mul_of_pos_left hrs pos
    simp only [Semiring.pow_succ]; grind only
  induction n with
  | zero => exact step 0 (by simp [weights, Semiring.zero_mul])
  | succ n ih => exact step (n+1) (Preorder.le_of_lt ih)

/-- The source's geometric-duration comparison is strict as soon as the role
payoffs differ, including when either payoff is fair. -/
theorem duration_ratio_depth_step {pc pd : F} (hpc : 0 < pc) (hgap : pc < pd)
    (hpd : pd < 1) {n : Nat} (hn : 1 ≤ n) :
    duration n pd / duration n pc < duration (n+1) pd / duration (n+1) pc := by
  have hc : pc < 1 := by grind only
  have hr := odds_pos hpc hc
  have hrs := odds_strict hgap hpd
  have key := last_term_strict hr hrs (n-1)
  rw [show n-1+1 = n by omega] at key
  let r := pc/(1-pc)
  let s := pd/(1-pd)
  have hg : weights s n * weights r (n+1) < weights s (n+1) * weights r n := by
    change weights s n * r^n < weights r n * s^n at key
    simp only [weights]; grind only
  have hscale := OrderedRing.mul_pos
    (Field.IsOrdered.inv_pos_iff.mpr (by grind only : 0 < 1-pc))
    (Field.IsOrdered.inv_pos_iff.mpr (by grind only : 0 < 1-pd))
  have h := OrderedRing.mul_lt_mul_of_pos_right hg hscale
  apply (frac_lt (duration_pos hpc hc hn) (duration_pos hpc hc (by omega))).2
  change (weights s n / (1-pd)) * (weights r (n+1) / (1-pc)) <
    (weights s (n+1) / (1-pd)) * (weights r n / (1-pc))
  simp only [Field.div_eq_mul_inv]; grind only

private theorem pay_domain {H c x α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 ≤ x) (hx' : x ≤ 1) (ha : 0 ≤ α) (ha' : α ≤ 1) :
    0 < volunteerPay H c x α ∧ volunteerPay H c x α ≤ freePay H c x α ∧
      freePay H c x α < 1 := by
  have cα := OrderedRing.mul_nonneg (Preorder.le_of_lt hc) ha
  have := OrderedRing.mul_nonneg cα hx
  have := OrderedRing.mul_nonneg cα (by grind only : 0 ≤ 1-x)
  have := OrderedRing.mul_nonneg (Preorder.le_of_lt hc) (by grind only : 0 ≤ 1-α)
  simp only [volunteerPay, freePay]; grind only

omit [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F] in
/-- The reparametrization by the private payoff gap d = c(1−α). -/
theorem quota_gap_formula (n : Nat) (H c θ α : F) :
    quotaRatio n H c θ α =
      duration n ((H-c*θ) + θ*(c*(1-α))) /
      duration n ((H-c*θ) - (1-θ)*(c*(1-α))) := by
  unfold quotaRatio volunteerPay freePay
  congr 2 <;> grind only

theorem quotaRatio_depth_strict {H c θ α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hθ : 0 ≤ θ) (hθ' : θ ≤ 1) (ha : 0 ≤ α) (ha' : α < 1)
    {n : Nat} (hn : 1 ≤ n) : quotaRatio n H c θ α < quotaRatio (n+1) H c θ α := by
  obtain ⟨hp, _, hq⟩ := pay_domain hc hcH hH hθ hθ' ha (Preorder.le_of_lt ha')
  have hd := OrderedRing.mul_pos hc (by grind only : 0 < 1-α)
  exact duration_ratio_depth_step hp (by unfold volunteerPay; grind only) hq hn

theorem quotaRatio_full_pool {H c θ : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hθ : 0 ≤ θ) (hθ' : θ ≤ 1) {n : Nat} (hn : 1 ≤ n) :
    quotaRatio n H c θ 1 = 1 := by
  have h := pay_domain hc hcH hH hθ hθ' (by grind : (0:F) ≤ 1) (by grind : (1:F) ≤ 1)
  have eq : volunteerPay H c θ 1 = freePay H c θ 1 := by unfold volunteerPay; grind only
  rw [eq] at h
  have nz := Preorder.ne_of_gt (duration_pos h.1 h.2.2 hn)
  rw [quotaRatio, eq, Field.div_eq_mul_inv, Field.mul_inv_cancel nz]

private theorem duration_mono {p q : F} (hp : 0 < p) (hpq : p ≤ q) (hq : q < 1)
    {n : Nat} (hn : 1 ≤ n) : duration n p ≤ duration n q := by
  by_cases he : p = q
  · simp [he]
  · exact Preorder.le_of_lt (duration_strict hp (by grind only) hq hn)

/-- At any positive fraction, the free-rider duration decreases with pooling.
The volunteer duration increases weakly, including at x = 1. -/
theorem quotaRatio_share_strict {H c x α β : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 < x) (hx' : x ≤ 1) (ha : 0 ≤ α) (hab : α < β) (hb : β ≤ 1)
    {n : Nat} (hn : 1 ≤ n) : quotaRatio n H c x β < quotaRatio n H c x α := by
  obtain ⟨hca, hda, hea⟩ := pay_domain hc hcH hH (Preorder.le_of_lt hx) hx' ha (by grind only : α ≤ 1)
  obtain ⟨hcb, hdb, heb⟩ := pay_domain hc hcH hH (Preorder.le_of_lt hx) hx' (by grind only : 0 ≤ β) hb
  have gap := OrderedRing.mul_pos hc (by grind only : 0 < β-α)
  have := OrderedRing.mul_pos gap hx
  have := OrderedRing.mul_nonneg (Preorder.le_of_lt gap) (by grind only : 0 ≤ 1-x)
  have hd : freePay H c x β < freePay H c x α := by unfold freePay; grind only
  have hcp : volunteerPay H c x α ≤ volunteerPay H c x β := by unfold volunteerPay freePay; grind only
  have hD := duration_strict (by grind only : 0 < freePay H c x β) hd hea hn
  have hC := duration_mono hca hcp (by grind only) hn
  have hCa := duration_pos hca (by grind only) hn
  have hCb := duration_pos hcb (by grind only) hn
  have hDa := duration_pos (by grind only : 0 < freePay H c x α) hea hn
  have := OrderedRing.mul_lt_mul_of_pos_right hD hCa
  have := OrderedRing.mul_le_mul_of_nonneg_left hC (Preorder.le_of_lt hDa)
  exact (frac_lt hCb hCa).2 (by grind only)

private theorem eq_frac {a b c : F} (hc : 0 < c) : a = b/c ↔ a*c = b := by
  have := Field.div_mul_cancel (x := b) (Preorder.ne_of_gt hc)
  constructor <;> intro h <;> grind

omit [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F] in
theorem duration_one (p : F) : duration 1 p = 1/(1-p) := by
  simp only [duration, weights, Semiring.pow_zero, AddCommMonoid.zero_add]

theorem duration_two {p : F} (hp : p < 1) : duration 2 p = 1/(1-p)^2 := by
  have hq : 1-p ≠ 0 := by grind only
  have h := Field.div_mul_cancel (x := p) hq
  have hq2 := OrderedRing.sq_pos hq
  apply (frac_eq (by grind only) hq2).2
  simp only [weights, Semiring.pow_zero, Semiring.pow_one, AddCommMonoid.zero_add]
  grind only

private theorem response_one_formula {pc pd : F} (hc : pc < 1) (hd : pd < 1) :
    response 1 pc pd = (1-pd)/((1-pc)+(1-pd)) := by
  have hu := quotient_pos (by grind : (0:F) < 1) (by grind only : 0 < 1-pc)
  have hv := quotient_pos (by grind : (0:F) < 1) (by grind only : 0 < 1-pd)
  have h₁ := Field.div_mul_cancel (x := (1:F)) (by grind only : 1-pc ≠ 0)
  have h₂ := Field.div_mul_cancel (x := (1:F)) (by grind only : 1-pd ≠ 0)
  rw [response, duration_one, duration_one]
  apply (frac_eq (by grind only) (by grind only)).2
  grind only

private theorem quota_denom_pos {c θ : F} (hc : 0 < c) (hθ : 0 < θ) (hθ' : θ < 1/2) :
    0 < 2*c*θ*(1-θ) :=
  OrderedRing.mul_pos (OrderedRing.mul_pos (OrderedRing.mul_pos (by grind) hc) hθ) (by grind)

/-- The quota is stationary for the depth-one, two-role transition matrix
exactly when the two directional flows at the quota agree. -/
theorem depth_one_quota_iff {H c θ α : F} (hc : 0 < c) (hθ : 0 < θ) (hθ' : θ < 1/2)
    (hpc : volunteerPay H c θ α < 1) (hpd : freePay H c θ α < 1) :
    response 1 (volunteerPay H c θ α) (freePay H c θ α) = θ ↔ α = A₁ H c θ := by
  rw [response_one_formula hpc hpd, A₁, eq_frac (quota_denom_pos hc hθ hθ')]
  have eq := eq_frac (a := θ) (b := 1-freePay H c θ α)
    (by grind only : 0 < (1-volunteerPay H c θ α)+(1-freePay H c θ α))
  simp only [volunteerPay, freePay] at eq ⊢
  constructor
  · intro h
    have := eq.mp h.symm
    grind only
  · intro h
    apply Eq.symm
    apply eq.mpr
    grind only

/-- A₁ is below full pooling. Its lower feasibility boundary can be active. -/
theorem depth_one_share_feasible_iff {H c θ : F} (hH : H < 1)
    (hc : 0 < c) (hθ : 0 < θ) (hθ' : θ < 1/2) :
    (0 ≤ A₁ H c θ ∧ A₁ H c θ < 1) ↔ (1-H)*(1-2*θ) ≤ c*θ := by
  have hd := quota_denom_pos hc hθ hθ'
  have gap := OrderedRing.mul_pos
    (by have := OrderedRing.mul_pos hc hθ; grind only : 0 < 1-H+c*θ)
    (by grind : 0 < 1-2*θ)
  have lower := Field.IsOrdered.le_mul_inv_iff_mul_le (0:F) (c*θ-(1-H)*(1-2*θ)) hd
  have upper := Field.IsOrdered.mul_inv_lt_iff_lt_mul (c*θ-(1-H)*(1-2*θ)) (1:F) hd
  simp only [A₁, Field.div_eq_mul_inv]
  rw [lower, upper]
  grind only

/-- The productive mean-field law at A₁ has exactly quota mass. Both
architectures have the same two opposing fluxes up to their switch factor ν. -/
theorem depth_one_quota_balance {H c θ : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hθ : 0 < θ) (hθ' : θ < 1/2) (feasible : (1-H)*(1-2*θ) ≤ c*θ) (ν : F) :
    let α := A₁ H c θ
    response 1 (volunteerPay H c θ α) (freePay H c θ α) = θ ∧
      θ*(1-ν*(1-volunteerPay H c θ α)) + (1-θ)*ν*(1-freePay H c θ α) = θ := by
  dsimp only
  obtain ⟨ha, ha'⟩ := (depth_one_share_feasible_iff hH hc hθ hθ').2 feasible
  obtain ⟨_, hcp, hpd⟩ := pay_domain hc hcH hH (Preorder.le_of_lt hθ) (by grind)
    ha (Preorder.le_of_lt ha')
  have hα := Field.div_mul_cancel (x := c*θ-(1-H)*(1-2*θ)) (Preorder.ne_of_gt (quota_denom_pos hc hθ hθ'))
  refine ⟨(depth_one_quota_iff hc hθ hθ' (by grind only) hpd).2 rfl, ?_⟩
  unfold volunteerPay freePay A₁
  grind only

theorem quota_welfare_and_extremes [DecidableLE F] {L H c θ : F} (hc : 0 < c)
    (hθ' : θ < 1/2) (gain : L < H-c*θ) :
    welfare L H c θ θ = H-c*θ ∧ L < welfare L H c θ θ ∧
      welfare L H c θ (1/2) = H-c/2 ∧ welfare L H c θ (1/2) < welfare L H c θ θ ∧
      ∀ x : F, 0 ≤ x → x < θ → welfare L H c θ x ≤ L := by
  have := OrderedRing.mul_lt_mul_of_pos_left hθ' hc
  simp only [welfare, ite_eq_left (Std.IsPreorder.le_refl θ), ite_eq_left (Preorder.le_of_lt hθ')]
  refine ⟨True.intro, gain, by grind, by grind, ?_⟩
  intro x hx hx'
  rw [ite_eq_right (by grind only : ¬ θ ≤ x)]
  have := OrderedRing.mul_nonneg (Preorder.le_of_lt hc) hx
  grind only

theorem full_pool_fraction {H c x : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 ≤ x) (hx' : x ≤ 1) {n : Nat} (hn : 1 ≤ n) :
    response n (volunteerPay H c x 1) (freePay H c x 1) = 1/2 := by
  have h := pay_domain hc hcH hH hx hx' (by grind : (0:F) ≤ 1) (by grind : (1:F) ≤ 1)
  have he : volunteerPay H c x 1 = freePay H c x 1 := by unfold volunteerPay; grind only
  rw [he] at h
  have := duration_pos h.1 h.2.2 hn
  rw [he, response]
  exact (frac_eq (by grind only) (by grind)).2 (by grind only)

/-- Clearing the two positive denominators gives the precise below-Nash criterion. -/
theorem depth_one_below_nash_iff {L H c θ : F} (hc : 0 < c) (hθ : 0 < θ) (hθ' : θ < 1/2) :
    A₁ H c θ < nashShare L H c ↔
      2*θ*(1-θ)*(H-L) < (1-2*θ)*(1-H+c*θ) := by
  have re : nashShare L H c = (c-(H-L))/c := by
    unfold nashShare
    have := Field.div_mul_cancel (x := H-L) (Preorder.ne_of_gt hc)
    exact (eq_frac hc).2 (by grind only)
  rw [re, A₁, frac_lt (quota_denom_pos hc hθ hθ') hc]
  have cancel := Field.IsOrdered.mul_lt_mul_iff_of_pos_right
    (a := 2*θ*(1-θ)*(H-L)) (b := (1-2*θ)*(1-H+c*θ)) hc
  grind only

theorem private_quota_example :
    A₁ (9/10 : Rat) (1/5) (1/4) = 0 ∧
    response 1 (volunteerPay (9/10 : Rat) (1/5) (1/4) 0) (freePay (9/10) (1/5) (1/4) 0) = 1/4 ∧
    welfare (4/5 : Rat) (9/10) (1/5) (1/4) (1/4) = 17/20 := by decide +kernel

/-- When A₁ is strictly positive, even the extension of the productive private
branch fixes a fraction below quota. Every physical private fixed point then
has low-base welfare. The case A₁ = 0 is illustrated above. -/
theorem private_fixed_point_below_quota [DecidableLE F] {L H c θ x : F}
    (hc : 0 < c) (hH : H < 1) (hθ : 0 < θ) (hθ' : θ < 1/2)
    (gain : L < H-c*θ) (hA : 0 < A₁ H c θ) (hx : 0 ≤ x)
    (fixed : let t := if θ ≤ x then H else L
      response 1 (volunteerPay t c x 0) (freePay t c x 0) = x) :
    x < θ ∧ welfare L H c θ x ≤ L ∧ welfare L H c θ x < H-c*θ := by
  have den := quota_denom_pos hc hθ hθ'
  have num := OrderedRing.mul_pos hA den
  have share : A₁ H c θ * (2*c*θ*(1-θ)) = c*θ-(1-H)*(1-2*θ) :=
    Field.div_mul_cancel (Preorder.ne_of_gt den)
  rw [share] at num
  have low : x < θ := by
    apply Classical.byContradiction
    intro neg
    have high : θ ≤ x := by grind only
    simp only [ite_eq_left high] at fixed
    have hp : volunteerPay H c x 0 = H-c := by unfold volunteerPay freePay; grind only
    have hq : freePay H c x 0 = H := by unfold freePay; grind only
    rw [hp, hq, response_one_formula (by grind only) hH] at fixed
    have bal := (eq_frac (by grind only : 0 < (1-(H-c))+(1-H))).mp fixed.symm
    have := OrderedRing.mul_nonneg (by grind only : 0 ≤ x-θ) (by grind only : 0 ≤ 2*(1-H)+c)
    grind only
  have w := (quota_welfare_and_extremes hc hθ' gain).2.2.2.2 x hx low
  exact ⟨low, w, by grind only⟩

theorem quota_welfare_maximum [DecidableLE F] {L H c θ x : F} (hc : 0 < c)
    (gain : L < H-c*θ) (hx : 0 ≤ x) :
    welfare L H c θ x ≤ H-c*θ ∧ (welfare L H c θ x = H-c*θ ↔ x = θ) := by
  unfold welfare
  split
  · have := OrderedRing.mul_le_mul_of_nonneg_left (by assumption : θ ≤ x) (Preorder.le_of_lt hc)
    by_cases eq : x = θ
    · simp [eq]
    · have := OrderedRing.mul_lt_mul_of_pos_left (by grind only : θ < x) hc
      grind only
  · have := OrderedRing.mul_nonneg (Preorder.le_of_lt hc) hx
    grind only

/-- A positive-depth response is the logistic transform of the duration ratio. -/
theorem response_from_ratio {H c x α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 ≤ x) (hx' : x ≤ 1) (ha : 0 ≤ α) (ha' : α ≤ 1) {n : Nat} (hn : 1 ≤ n) :
    response n (volunteerPay H c x α) (freePay H c x α) = 1/(1+quotaRatio n H c x α) := by
  obtain ⟨hpc, hgap, hpd⟩ := pay_domain hc hcH hH hx hx' ha ha'
  have posC := duration_pos hpc (by grind only) hn
  have posD := duration_pos (by grind only : 0 < freePay H c x α) hpd hn
  let C := duration n (volunteerPay H c x α)
  let D := duration n (freePay H c x α)
  change 0 < C at posC
  change 0 < D at posD
  have := quotient_pos posD posC
  have := Field.div_mul_cancel (x := D) (Preorder.ne_of_gt posC)
  change C/(C+D) = 1/(1+D/C)
  exact (frac_eq (by grind only) (by grind only)).2 (by grind only)

/-- Quota balance in duration odds is equivalent to stationarity of the
prescribed volunteer fraction on the productive branch. -/
theorem quota_ratio_iff_quota_mass {H c θ α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hθ : 0 < θ) (hθ' : θ ≤ 1) (ha : 0 ≤ α) (ha' : α ≤ 1) {n : Nat} (hn : 1 ≤ n) :
    quotaRatio n H c θ α = (1-θ)/θ ↔
      response n (volunteerPay H c θ α) (freePay H c θ α) = θ := by
  obtain ⟨hpc, hgap, hpd⟩ := pay_domain hc hcH hH (Preorder.le_of_lt hθ) hθ' ha ha'
  have posC := duration_pos hpc (by grind only) hn
  have posD := duration_pos (by grind only : 0 < freePay H c θ α) hpd hn
  have pos : 0 < quotaRatio n H c θ α := quotient_pos posD posC
  rw [response_from_ratio hc hcH hH (Preorder.le_of_lt hθ) hθ' ha ha' hn, eq_frac hθ]
  have h := eq_frac (a := θ) (b := 1) (by grind only : 0 < 1+quotaRatio n H c θ α)
  grind only

private theorem share_le {H c x α β : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 < x) (hx' : x ≤ 1) (ha : 0 ≤ α) (hab : α ≤ β) (hb : β ≤ 1)
    {n : Nat} (hn : 1 ≤ n) : quotaRatio n H c x β ≤ quotaRatio n H c x α := by
  by_cases e : α = β
  · simp [e]
  · exact Preorder.le_of_lt (quotaRatio_share_strict hc hcH hH hx hx' ha (by grind only) hb hn)

private theorem depth_le {H c x α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 ≤ x) (hx' : x ≤ 1) (ha : 0 ≤ α) (ha' : α < 1)
    {m n : Nat} (hm : 1 ≤ m) (hmn : m ≤ n) : quotaRatio m H c x α ≤ quotaRatio n H c x α := by
  induction n with
  | zero => omega
  | succ n ih =>
    by_cases e : m = n+1
    · simp [e]
    · have prev := ih (by omega)
      have := quotaRatio_depth_strict hc hcH hH hx hx' ha ha' (by omega : 1 ≤ n)
      grind only

private theorem ratio_two {H c x α : F} (hc : 0 < c) (hcH : c < H) (hH : H < 1)
    (hx : 0 ≤ x) (hx' : x ≤ 1) (ha : 0 ≤ α) (ha' : α ≤ 1) :
    quotaRatio 2 H c x α = ((1-volunteerPay H c x α)/(1-freePay H c x α))^2 := by
  obtain ⟨_, hgap, hpd⟩ := pay_domain hc hcH hH hx hx' ha ha'
  let qC := 1-volunteerPay H c x α
  let qD := 1-freePay H c x α
  have hC : 0 < qC := by dsimp [qC]; grind only
  have hD : 0 < qD := by dsimp [qD]; grind only
  rw [quotaRatio, duration_two hpd, duration_two (by grind only)]
  change (1/qD^2)/(1/qC^2) = (qC/qD)^2
  simp only [Field.div_eq_mul_inv, Semiring.one_mul, Field.inv_inv, Field.inv_pow, CommSemiring.mul_pow]
  grind only

/-- Exact benchmark shares, in the payoff order L, H, c, θ. -/
theorem benchmark_shares :
    nashShare (4/5 : Rat) (97/100) (3/5) = 43/60 ∧
    A₁ (97/100 : Rat) (3/5) (1/4) = 3/5 ∧ (3/5 : Rat) < 43/60 := by decide +kernel

/-- The three physical depth-one fixed fractions, with their exact profile welfares. -/
theorem benchmark_endpoint_welfares :
    response 1 (volunteerPay (4/5 : Rat) (3/5) (1/5) 0) (freePay (4/5) (3/5) (1/5) 0) = 1/5 ∧
    welfare (4/5 : Rat) (97/100) (3/5) (1/4) (1/5) = 17/25 ∧
    response 1 (volunteerPay (97/100 : Rat) (3/5) (1/4) (3/5))
      (freePay (97/100) (3/5) (1/4) (3/5)) = 1/4 ∧
    welfare (4/5 : Rat) (97/100) (3/5) (1/4) (1/4) = 41/50 ∧
    response 1 (volunteerPay (97/100 : Rat) (3/5) (1/2) 1) (freePay (97/100) (3/5) (1/2) 1) = 1/2 ∧
    welfare (4/5 : Rat) (97/100) (3/5) (1/4) (1/2) = 67/100 := by decide +kernel

theorem benchmark_nash_ratios :
    quotaRatio 1 (97/100 : Rat) (3/5) (1/4) (43/60) = 123/55 ∧
    quotaRatio 2 (97/100 : Rat) (3/5) (1/4) (43/60) = (123/55)^2 ∧
    123/55 < (3 : Rat) ∧ (3 : Rat) < (123/55)^2 := by decide +kernel

private theorem benchmark_two_at_nash {x : F} (hx : 0 ≤ x) (hx' : x ≤ 1) :
    quotaRatio 2 (97/100) (3/5) x (43/60) = ((20+43*x)/(3+43*x))^2 := by
  rw [ratio_two (by grind) (by grind) (by grind) hx hx' (by grind) (by grind)]
  congr 1
  simp only [volunteerPay, freePay]
  apply (frac_eq (by grind) (by grind)).2
  grind only

private theorem nash_two_le_ratio {x α : F} (hx : 0 < x) (hx' : x ≤ 1)
    (ha : 0 ≤ α) (ha' : α ≤ 43/60) {n : Nat} (hn : 2 ≤ n) :
    quotaRatio 2 (97/100) (3/5) x (43/60) ≤ quotaRatio n (97/100) (3/5) x α := by
  have h := depth_le (H := (97/100 : F)) (c := 3/5) (α := 43/60) (by grind) (by grind) (by grind)
    (Preorder.le_of_lt hx) hx' (by grind) (by grind) (by decide : 1 ≤ 2) hn
  have h' := share_le (H := (97/100 : F)) (c := 3/5) (by grind) (by grind) (by grind)
    hx hx' ha ha' (by grind) (by omega : 1 ≤ n)
  grind only

/-- Depth one is below the quota ratio at Nash. From depth two on, every
feasible share at or below Nash exceeds it in every ordered field. -/
theorem critical_depth_two :
    quotaRatio 1 (97/100 : F) (3/5) (1/4) (43/60) < 3 ∧
      ∀ (n : Nat) (α : F), 2 ≤ n → 0 ≤ α → α ≤ 43/60 →
        3 < quotaRatio n (97/100) (3/5) (1/4) α := by
  constructor
  · simp only [quotaRatio, duration_one, volunteerPay, freePay]
    grind only
  · intro n α hn ha ha'
    have h := nash_two_le_ratio (x := (1/4 : F)) (by grind) (by grind) ha ha' hn
    rw [benchmark_two_at_nash (by grind) (by grind)] at h
    grind only

/-- The cutoff excludes fixed points everywhere on the productive branch.
For x ≥ 1/4, the cleared depth-two deficit at Nash has numerator
3698 x³ + 129 x² + 151 x − 9, strictly positive throughout the branch. -/
theorem no_productive_fixed_point {n : Nat} (hn : 2 ≤ n) {α x : F}
    (ha : 0 ≤ α) (ha' : α ≤ 43/60) (hx : 1/4 ≤ x) (hx' : x ≤ 1) :
    response n (volunteerPay (97/100) (3/5) x α) (freePay (97/100) (3/5) x α) < x := by
  have hx0 : 0 < x := by grind
  have bound := nash_two_le_ratio hx0 hx' ha ha' hn
  rw [benchmark_two_at_nash (Preorder.le_of_lt hx0) hx'] at bound
  let v := (20+43*x)/(3+43*x)
  have hv : v*(3+43*x) = 20+43*x := Field.div_mul_cancel (by grind)
  change v^2 ≤ _ at bound
  have hq : 0 < 3+43*x := by grind only
  have hq2 := OrderedRing.sq_pos (Preorder.ne_of_gt hq)
  have hsq := OrderedRing.sq_nonneg (a := x)
  have hcube := OrderedRing.mul_nonneg hsq (Preorder.le_of_lt hx0)
  have clear : (3+43*x)^2 < x*((3+43*x)^2 + (20+43*x)^2) := by grind only
  have multiplied : 1*(3+43*x)^2 < (x*(1+v^2))*(3+43*x)^2 := by
    have hs : v^2*(3+43*x)^2 = (20+43*x)^2 := by rw [← hv]; grind only
    grind only
  have base := (Field.IsOrdered.mul_lt_mul_iff_of_pos_right hq2).mp multiplied
  have := OrderedRing.mul_le_mul_of_nonneg_left bound (Preorder.le_of_lt hx0)
  have := OrderedRing.sq_nonneg (a := v)
  rw [response_from_ratio (by grind) (by grind) (by grind) (Preorder.le_of_lt hx0) hx'
    ha (by grind) (by omega), Field.div_eq_mul_inv]
  apply (Field.IsOrdered.mul_inv_lt_iff_lt_mul _ _ (by grind only)).2
  grind only

/-- Before imposing feasibility of the fund share, the rational depth-one
formula still balances the two flows algebraically. -/
theorem depth_one_algebraic_quota {H c θ : F} (hH : H < 1) (hc : 0 < c)
    (hθ : 0 < θ) (hθ' : θ < 1/2) :
    response 1 (volunteerPay H c θ (A₁ H c θ)) (freePay H c θ (A₁ H c θ)) = θ := by
  let α := A₁ H c θ
  have share : α * (2*c*θ*(1-θ)) = c*θ - (1-H)*(1-2*θ) :=
    Field.div_mul_cancel (Preorder.ne_of_gt (quota_denom_pos hc hθ hθ'))
  have pos : 0 < 1-H+c*θ := by have := OrderedRing.mul_pos hc hθ; grind only
  have free : (1-freePay H c θ α) * (2*(1-θ)) = 1-H+c*θ := by unfold freePay; grind only
  have vol : (1-volunteerPay H c θ α) * (2*θ) = 1-H+c*θ := by unfold volunteerPay freePay; grind only
  have hf := (Field.IsOrdered.mul_lt_mul_iff_of_pos_right
    (a := 0) (b := 1-freePay H c θ α) (by grind : 0 < 2*(1-θ))).mp (by grind only)
  have hv := (Field.IsOrdered.mul_lt_mul_iff_of_pos_right
    (a := 0) (b := 1-volunteerPay H c θ α) (by grind only : 0 < 2*θ)).mp (by grind only)
  exact (depth_one_quota_iff (α := α) hc hθ hθ' (by grind only) (by grind only)).2 rfl

/-- The exact response deficit at the worst endpoint supplies the numerator of
the stationary welfare estimate in equation (3) of the memory notes. -/
theorem quota_response_deficit :
    (1/4 : F) - response 2 (volunteerPay (97/100) (3/5) (1/4) (43/60))
      (freePay (97/100) (3/5) (1/4) (43/60)) = 3027/36308 ∧
    ∀ (n : Nat) (α : F), 2 ≤ n → 0 ≤ α → α ≤ 43/60 →
      3027/36308 ≤ 1/4 - response n (volunteerPay (97/100) (3/5) (1/4) α)
        (freePay (97/100) (3/5) (1/4) α) := by
  constructor
  · rw [response_from_ratio (by grind) (by grind) (by grind) (by grind) (by grind)
      (by grind) (by grind) (by decide), benchmark_two_at_nash (by grind) (by grind)]
    grind only
  · intro n α hn ha ha'
    have h := nash_two_le_ratio (x := (1/4 : F)) (by grind) (by grind) ha ha' hn
    rw [benchmark_two_at_nash (by grind) (by grind)] at h
    let D := 1+quotaRatio n (97/100) (3/5) (1/4) α
    have hd : 0 < D := by dsimp [D]; grind only
    have bound : 1/D ≤ 3025/18154 := by
      apply (Field.IsOrdered.mul_le_mul_iff_of_pos_right hd).mp
      rw [Field.div_mul_cancel (Preorder.ne_of_gt hd)]
      dsimp [D]; grind only
    rw [response_from_ratio (by grind) (by grind) (by grind) (by grind) (by grind)
      ha (by grind) (by omega)]
    change 3027/36308 ≤ 1/4-1/D
    grind only

end Quota

section DepthTwo

variable {F : Type} [Field F]

/-- At the productive quota, the benchmark losses are
    `100 q_C = 63 - 45 α` and `100 q_D = 3 + 15 α`. -/
def depthTwoOdds (α : F) : F := ((63 - 45 * α) / (3 + 15 * α)) ^ 2

/-- The benchmark depth-two share as a function of the positive square root of three. -/
def depthTwoShare (s : F) : F := (11 - 4 * s) / 5

variable [LE F] [LT F] [Std.LawfulOrderLT F] [Std.IsLinearOrder F] [OrderedRing F]

theorem depthTwo_quota_iff_polynomial {α : F} (ha : 0 ≤ α) :
    depthTwoOdds α = 3 ↔ 25 * α ^ 2 - 110 * α + 73 = 0 := by
  let r := (63 - 45 * α) / (3 + 15 * α)
  have hd : 3 + 15 * α ≠ 0 := by grind only
  have hc : r * (3 + 15 * α) = 63 - 45 * α := Field.div_mul_cancel hd
  have he : (3 + 15 * α) ^ 2 * (r ^ 2 - 3) = 54 * (25 * α ^ 2 - 110 * α + 73) := by
    calc
      _ = (r * (3 + 15 * α)) ^ 2 - 3 * (3 + 15 * α) ^ 2 := by grind only
      _ = _ := by rw [hc]; grind only
  change r ^ 2 = 3 ↔ _
  constructor
  · intro h
    rw [h] at he
    grind only
  · intro h
    rw [h, Semiring.mul_zero] at he
    rcases Field.of_mul_eq_zero he with hbad | hgood
    · exact False.elim (hd (Field.of_pow_eq_zero _ _ hbad))
    · grind only

theorem depthTwoShare_polynomial {s : F} (hs : s ^ 2 = 3) :
    25 * depthTwoShare s ^ 2 - 110 * depthTwoShare s + 73 = 0 := by
  unfold depthTwoShare
  grind only

theorem depthTwoShare_bracket {s : F} (hs : 0 < s) (hsq : s ^ 2 = 3) :
    814 / 1000 < depthTwoShare s ∧ depthTwoShare s < 815 / 1000 ∧
      43 / 60 < depthTwoShare s := by
  have lo : 277 < 160 * s := by
    apply Classical.byContradiction
    intro h
    have := OrderedRing.mul_nonneg (a := 277 - 160 * s) (b := 277 + 160 * s)
      (by grind only) (by grind only)
    grind only
  have hi : 400 * s < 693 := by
    apply Classical.byContradiction
    intro h
    have := OrderedRing.mul_nonneg (a := 400 * s - 693) (b := 400 * s + 693)
      (by grind only) (by grind only)
    grind only
  unfold depthTwoShare
  grind only

/-- The explicit radical is feasible, attains the quota, and is its unique feasible share. -/
theorem depthTwoShare_quota_and_unique {s : F} (hs : 0 < s) (hsq : s ^ 2 = 3) :
    (0 ≤ depthTwoShare s ∧ depthTwoShare s ≤ 1 ∧ depthTwoOdds (depthTwoShare s) = 3) ∧
    ∀ α : F, 0 ≤ α → α ≤ 1 → depthTwoOdds α = 3 → α = depthTwoShare s := by
  let a := depthTwoShare s
  obtain ⟨lo, hi, _⟩ := depthTwoShare_bracket hs hsq
  have ha : 0 ≤ a ∧ a ≤ 1 := by dsimp [a]; grind only
  have hp : 25 * a ^ 2 - 110 * a + 73 = 0 := depthTwoShare_polynomial hsq
  refine ⟨⟨ha.1, ha.2, (depthTwo_quota_iff_polynomial ha.1).2 hp⟩, ?_⟩
  intro α hα0 hα1 hquota
  have hαp := (depthTwo_quota_iff_polynomial hα0).1 hquota
  have factor : (α - a) * (25 * (α + a) - 110) = 0 := by grind only
  rcases Field.of_mul_eq_zero factor with h | h
  · change α = a
    grind only
  · grind only

/-- The polynomial with constant term 19 takes the positive value 22/5 at the quota. -/
theorem depthTwo_quota_polynomial_residual {α : F} (ha : 0 ≤ α) (h : depthTwoOdds α = 3) :
    5 * α ^ 2 - 22 * α + 19 = 22 / 5 ∧ 5 * α ^ 2 - 22 * α + 19 ≠ 0 := by
  have hp := (depthTwo_quota_iff_polynomial ha).1 h
  grind only

/-- Evaluation of the general duration ratio at depth two on the benchmark. -/
theorem benchmark_depth_two_odds {α : F} (ha : 0 ≤ α) (ha' : α ≤ 1) :
    quotaRatio 2 (97/100) (3/5) (1/4) α = depthTwoOdds α := by
  rw [ratio_two (by grind) (by grind) (by grind) (by grind) (by grind) ha ha', depthTwoOdds]
  congr 1
  simp only [volunteerPay, freePay]
  exact (frac_eq (by grind) (by grind)).2 (by grind only)

theorem depth_two_quota_share {s : F} (hs : 0 < s) (hsq : s^2 = 3) :
    let A := depthTwoShare s
    quotaRatio 2 (97/100) (3/5) (1/4) A = 3 ∧
      ∀ α : F, 0 ≤ α → α ≤ 1 → (quotaRatio 2 (97/100) (3/5) (1/4) α = 3 ↔ α = A) := by
  obtain ⟨⟨lo, hi, eq⟩, unique⟩ := depthTwoShare_quota_and_unique hs hsq
  have root := (benchmark_depth_two_odds lo hi).trans eq
  refine ⟨root, fun α ha ha' => ⟨?_, ?_⟩⟩
  · rw [benchmark_depth_two_odds ha ha']; exact unique α ha ha'
  · intro h; exact h ▸ root

/-- Opposite rational residuals give an isolating interval independently of any
choice of a field containing a square root of three. -/
theorem depth_two_rational_bracket :
    depthTwoOdds (814/1000 : Rat) - 3 = 166/28561 ∧
    depthTwoOdds (815/1000 : Rat) - 3 = -(426/41209) ∧
    depthTwoOdds (815/1000 : Rat) < 3 ∧ 3 < depthTwoOdds (814/1000 : Rat) := by decide +kernel

end DepthTwo

section DepthTwoWelfare
open Lean.Grind

/-- The four empirical masses, parametrized by total C, shallow C and shallow D.
    The deep masses are `volunteers - shallowC` and `1 - volunteers - shallowD`. -/
structure DepthTwoProfile (E : Type) where
  volunteers : E
  shallowC : E
  shallowD : E

variable {E : Type} [Field E] [LE E] [LT E] [Std.LawfulOrderLT E]
    [Std.IsLinearOrder E] [OrderedRing E] [DecidableLT E]

def DepthTwoProfile.Valid (p : DepthTwoProfile E) : Prop :=
  0 ≤ p.shallowC ∧ p.shallowC ≤ p.volunteers ∧
  0 ≤ p.shallowD ∧ p.shallowD ≤ 1 - p.volunteers

def DepthTwoProfile.observe (w p : DepthTwoProfile E) : E :=
  w.volunteers * p.volunteers + w.shallowC * p.shallowC + w.shallowD * p.shallowD

def depthTwoBase (x : E) : E := if x < 1/4 then 4/5 else 97/100

def depthTwoWelfare (p : DepthTwoProfile E) : E :=
  depthTwoBase p.volunteers - (3/5) * p.volunteers

private def welfareLossStep (qC qD ν : E) (p : DepthTwoProfile E) : DepthTwoProfile E :=
  let net := ν * (qD * p.shallowD - qC * p.shallowC)
  ⟨p.volunteers + net, qC * p.volunteers + net, qD * (1 - p.volunteers) - net⟩

/-- Conditional mean after one synchronous update. A shallow loss switches roles
    with probability ν. A win sends either depth of its role to the deep state. -/
def depthTwoUpdate (α ν : E) (p : DepthTwoProfile E) : DepthTwoProfile E :=
  let qD := 1 - depthTwoBase p.volunteers + (3/5) * α * p.volunteers
  welfareLossStep (qD + (3/5) * (1-α)) qD ν p

/-- One support point of a finite distribution of empirical profiles. -/
structure DepthTwoAtom (E : Type) [Field E] [LE E] where
  profile : DepthTwoProfile E
  valid : profile.Valid
  weight : E
  nonnegative : 0 ≤ weight

def depthTwoMean (law : List (DepthTwoAtom E)) (f : DepthTwoProfile E → E) : E :=
  match law with
  | [] => 0
  | a :: tail => a.weight * f a.profile + depthTwoMean tail f

omit [LT E] [Std.LawfulOrderLT E] [Std.IsLinearOrder E] [OrderedRing E] [DecidableLT E] in
private theorem welfare_mean_congr (law : List (DepthTwoAtom E)) (f g : DepthTwoProfile E → E)
    (h : ∀ atom ∈ law, f atom.profile = g atom.profile) : depthTwoMean law f = depthTwoMean law g := by
  induction law with
  | nil => rfl
  | cons a tail ih =>
    simp only [depthTwoMean, h a List.mem_cons_self,
      ih (fun b hb => h b (List.mem_cons_of_mem a hb))]

/-- Stationarity of empirical means. Every stationary finite-population law obeys
    this identity by taking conditional expectations of the three coordinates. -/
def DepthTwoStationaryMeans (law : List (DepthTwoAtom E)) (α ν : E) : Prop :=
  depthTwoMean law (fun _ => 1) = 1 ∧ ∀ w : DepthTwoProfile E,
    depthTwoMean law w.observe = depthTwoMean law (fun p => w.observe (depthTwoUpdate α ν p))

omit [Std.LawfulOrderLT E] [Std.IsLinearOrder E] [OrderedRing E] in
/-- A stationary transition law with the game's conditional means satisfies the
    balance above. The transition rows may describe a population of any size. -/
theorem depth_two_means_of_stationary (law : List (DepthTwoAtom E)) (α ν : E)
    (rows : DepthTwoProfile E → List (DepthTwoAtom E))
    (normalized : depthTwoMean law (fun _ => 1) = 1)
    (stationary : ∀ f, depthTwoMean law f = depthTwoMean law (fun p => depthTwoMean (rows p) f))
    (conditional : ∀ a ∈ law, ∀ w : DepthTwoProfile E,
      depthTwoMean (rows a.profile) w.observe = w.observe (depthTwoUpdate α ν a.profile)) :
    DepthTwoStationaryMeans law α ν := by
  refine ⟨normalized, fun w => ?_⟩
  rw [stationary w.observe]
  exact welfare_mean_congr law _ _ (fun a ha => conditional a ha w)

-- At the productive quota and α = 43/60 the C and D loss probabilities are
-- a = 123/400 and b = 55/400. From deepest D to deepest C the successive
-- potential increments are b, 1/ν, a. Their common normalization is omitted.
private def welfarePotential (ν : E) : DepthTwoProfile E :=
  ⟨123/400 + 55/400 + 1/ν, -(123/400), 55/400⟩

omit [DecidableLT E] in
private theorem welfare_potential_drift (qC qD ν : E) (hν : ν ≠ 0) (p : DepthTwoProfile E) :
    (welfarePotential ν).observe p - (welfarePotential ν).observe (welfareLossStep qC qD ν p) =
    (9077/80000) * p.volunteers - (55/400)^2 +
      (qC - 123/400) * ((123/400) * p.volunteers + p.shallowC) -
      (qD - 55/400) * ((55/400) * (1 - p.volunteers) + p.shallowD) := by
  have cancel : (1/ν) * ν = 1 := Field.div_mul_cancel hν
  dsimp [welfarePotential, DepthTwoProfile.observe, welfareLossStep]
  grind only

private theorem welfare_profile_bound (p : DepthTwoProfile E) (hp : p.Valid) (α ν : E)
    (ha : α ≤ 43/60) (hν : ν ≠ 0) :
    3027/320000 ≤ (welfarePotential ν).observe p -
      (welfarePotential ν).observe (depthTwoUpdate α ν p) + 5 * (41/50 - depthTwoWelfare p) := by
  obtain ⟨sc0, scx, sd0, sdx⟩ := hp
  let x := p.volunteers
  let qD := 1 - depthTwoBase x + (3/5) * α * x
  let qC := qD + (3/5) * (1-α)
  -- `e` is the change in D loss probability at the maximum allowed share.
  let e := 1 - depthTwoBase x + (43/100) * x - 55/400
  have hx : 0 ≤ x := by dsimp [x]; grind only
  have hx' : 0 ≤ 1-x := by dsimp [x]; grind only
  have slack : 0 ≤ 43/100 - (3/5)*α := by grind only
  have ec : e ≤ qC - 123/400 := by
    have := OrderedRing.mul_nonneg slack hx'
    dsimp [e, qC, qD]; grind only
  have ed : qD - 55/400 ≤ e := by
    have := OrderedRing.mul_nonneg slack hx
    dsimp [e, qD]; grind only
  have e0 : 0 ≤ e := by
    dsimp [e, depthTwoBase]; split <;> grind only
  have c0 : 0 ≤ (123/400) * x + p.shallowC := by grind only
  have d0 : 0 ≤ (55/400) * (1-x) + p.shallowD := by grind only
  have d1 : (55/400) * (1-x) + p.shallowD ≤ 455/400 := by dsimp [x] at *; grind only
  have cTerm := OrderedRing.mul_nonneg (Std.le_trans e0 ec) c0
  have dTerm : (qD - 55/400) * ((55/400) * (1-x) + p.shallowD) ≤ e * (455/400) :=
    Std.le_trans (OrderedRing.mul_le_mul_of_nonneg_right ed d0)
      (OrderedRing.mul_le_mul_of_nonneg_left d1 e0)
  have profileGap : 3027/320000 ≤ (9077/80000) * x - (55/400)^2 - e * (455/400) +
      5 * (41/50 - depthTwoWelfare p) := by
    change 3027/320000 ≤ (9077/80000) * x - (55/400)^2 - e * (455/400) +
      5 * (41/50 - (depthTwoBase x - (3/5)*x))
    dsimp [e, depthTwoBase]; split <;> grind only
  change 3027/320000 ≤ (welfarePotential ν).observe p -
    (welfarePotential ν).observe (welfareLossStep qC qD ν p) + 5 * (41/50 - depthTwoWelfare p)
  rw [welfare_potential_drift _ _ _ hν]
  change 3027/320000 ≤ (9077/80000) * x - (55/400)^2 +
    (qC - 123/400) * ((123/400) * x + p.shallowC) -
    (qD - 55/400) * ((55/400) * (1-x) + p.shallowD) + 5 * (41/50 - depthTwoWelfare p)
  grind only

omit [DecidableLT E] in
private theorem welfare_average_bound (law : List (DepthTwoAtom E))
    (f fNext w : DepthTwoProfile E → E) (a b k : E)
    (bound : ∀ p, p.Valid → a ≤ f p - fNext p + k * (b - w p)) :
    a * depthTwoMean law (fun _ => 1) ≤ depthTwoMean law f - depthTwoMean law fNext +
      k * (b * depthTwoMean law (fun _ => 1) - depthTwoMean law w) := by
  induction law with
  | nil => simp only [depthTwoMean]; grind only
  | cons atom tail ih =>
    have := OrderedRing.mul_le_mul_of_nonneg_left (bound atom.profile atom.valid) atom.nonnegative
    simp only [depthTwoMean]; grind only

/-- A direct four-state potential gives a uniform stationary welfare loss at all
    population sizes. It applies, in particular, to ν = 1 and ν = 1/2. -/
theorem depth_two_stationary_welfare_certificate (law : List (DepthTwoAtom E)) (α ν : E)
    (ha : α ≤ 43/60) (hν : 0 < ν) (hπ : DepthTwoStationaryMeans law α ν) :
    3027/1600000 ≤ 41/50 - depthTwoMean law depthTwoWelfare := by
  let u := welfarePotential ν
  have avg := welfare_average_bound law u.observe (fun p => u.observe (depthTwoUpdate α ν p))
    depthTwoWelfare (3027/320000) (41/50) 5
    (fun p hp => welfare_profile_bound p hp α ν ha (by grind only))
  rw [hπ.1, ← hπ.2 u] at avg
  grind only

/-- Denominator in equation (3) with n = 2, m = 3, g = 1/50 and Δ = 17/100. -/
def depthTwoWelfareDenominator (α : E) : E :=
  let B : E := 3 * (200/3)^3
  (1 + (3/5)*α*B) * (1/(3/5) + (1/4)/(1/50)) + (17/100)*B/(1/50)

def depthTwoWelfareBound (α : E) : E := (3027/36308) / depthTwoWelfareDenominator α

omit [DecidableLT E] in
/-- The lower bound in (3) at the largest allowed share. -/
theorem depth_two_welfare_bound_at_nash :
    depthTwoWelfareBound (43/60 : E) = 81729/12715075487810 := by
  unfold depthTwoWelfareBound depthTwoWelfareDenominator
  grind only

/-- Equation (3), including its positive worst-share value, for any stationary
    finite population satisfying the game's conditional update identities. -/
theorem depth_two_stationary_welfare_gap (law : List (DepthTwoAtom E)) (α ν : E)
    (ha0 : 0 ≤ α) (ha : α ≤ 43/60) (hν : 0 < ν) (hπ : DepthTwoStationaryMeans law α ν) :
    0 < (81729/12715075487810 : E) ∧ 81729/12715075487810 ≤ depthTwoWelfareBound α ∧
    depthTwoWelfareBound α ≤ 41/50 - depthTwoMean law depthTwoWelfare := by
  let d := depthTwoWelfareDenominator α
  have hd : 0 < d := by dsimp [d, depthTwoWelfareDenominator]; grind only
  have cancel : depthTwoWelfareBound α * d = 3027/36308 := Field.div_mul_cancel (by grind only : d ≠ 0)
  refine ⟨by grind only, ?_, Std.le_trans ?_ (depth_two_stationary_welfare_certificate law α ν ha hν hπ)⟩
  · apply (Field.IsOrdered.mul_le_mul_iff_of_pos_right hd).mp
    rw [cancel]; dsimp [d, depthTwoWelfareDenominator]; grind only
  · apply (Field.IsOrdered.mul_le_mul_iff_of_pos_right hd).mp
    rw [cancel]; dsimp [d, depthTwoWelfareDenominator]; grind only

end DepthTwoWelfare

end CommonFundCutoff
