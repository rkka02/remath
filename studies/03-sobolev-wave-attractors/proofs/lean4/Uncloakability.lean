import Std

/-!
The finite minimax argument, boundary symmetries, and the hexagon in characteristic
coordinates. All wall positions, ray intersections, profile values, and launch
weights are exact rationals. In the symmetry statements the type of boundary
points and the types of both characteristic projections are arbitrary.
-/

namespace Uncloakability

/-- Half the oscillation is the smallest possible maximum distance to the two
extreme values. The midpoint is the unique minimizing detector level. -/
theorem sharpHalfAmplitude (m M c : Rat) (h : m ≤ M) :
    let radius := max (M - c).abs (m - c).abs
    (M - m) / 2 ≤ radius ∧ (radius = (M - m) / 2 ↔ c = (m + M) / 2) := by
  dsimp only
  grind only [Rat.abs, Rat.max_def]

/-- The maximum deviation of a nonempty list attains half its range exactly
at its midrange, for every rational detector level. -/
theorem finiteSharpHalfAmplitude (vals : List Rat) (hne : vals ≠ []) (c : Rat) :
    let m := vals.min hne
    let M := vals.max hne
    let radius := (vals.map (fun w => (w - c).abs)).max (by simpa using hne)
    (M - m) / 2 ≤ radius ∧ (radius = (M - m) / 2 ↔ c = (m + M) / 2) := by
  let f := fun w : Rat => (w - c).abs
  have hn : vals.map f ≠ [] := by simpa using hne
  have hM := List.max_mem hne
  have hm := List.min_mem hne
  have dM := List.le_max_of_mem (List.mem_map_of_mem (f := f) hM)
  have dm := List.le_max_of_mem (List.mem_map_of_mem (f := f) hm)
  obtain ⟨w, hw, hmax⟩ := List.mem_map.mp (List.max_mem hn)
  have low := List.min_le_of_mem hw
  have high := List.le_max_of_mem hw
  have he : (vals.map f).max hn = max (f (vals.max hne)) (f (vals.min hne)) := by
    simp only [f] at dM dm hmax ⊢
    grind only [Rat.abs, Rat.max_def]
  dsimp only
  rw [he]
  exact sharpHalfAmplitude _ _ _ (List.min_le_of_mem hM)

/-- Reversing the order of the two chord involutions gives a two-sided inverse.
Conjugation by either chord involution realizes this inverse. -/
theorem dihedralTimeReversal {α : Type} (gPlus gMinus : α → α)
    (hp : ∀ p, gPlus (gPlus p) = p) (hm : ∀ p, gMinus (gMinus p) = p) :
    let b := gPlus ∘ gMinus
    let back := gMinus ∘ gPlus
    Function.LeftInverse back b ∧ Function.RightInverse back b ∧
      gMinus ∘ b ∘ gMinus = back ∧ gPlus ∘ b ∘ gPlus = back := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro x
    simp [hp, hm]
  · intro x
    simp [hp, hm]
  · funext x
    simp [Function.comp_def, hm]
  · funext x
    simp [Function.comp_def, hp]

private theorem repeat_intertwines {α : Type} {a back g : α → α}
    (h : ∀ p, g (a p) = back (g p)) (q : Nat) :
    g ∘ Nat.repeat a q = Nat.repeat back q ∘ g := by
  induction q with
  | zero => rfl
  | succ n ih =>
    funext x
    simpa only [Function.comp_apply, Nat.repeat, h] using congrArg back (congrFun ih x)

private theorem repeat_leftInverse {α : Type} {f g : α → α}
    (h : Function.LeftInverse g f) (q : Nat) :
    Function.LeftInverse (Nat.repeat g q) (Nat.repeat f q) := by
  have commute := repeat_intertwines (a := g) (back := g) (g := g) (fun _ => rfl)
  induction q with
  | zero =>
    intro x
    rfl
  | succ n ih =>
    intro x
    change g (Nat.repeat g n (f (Nat.repeat f n x))) = x
    rw [show g (Nat.repeat g n (f (Nat.repeat f n x))) =
      Nat.repeat g n (g (f (Nat.repeat f n x))) from congrFun (commute n) _, h, ih]

/-- Both reflections conjugate every nonnegative iterate to the same iterate
of the inverse map. -/
theorem dihedralIterates {α : Type} (gPlus gMinus : α → α)
    (hp : ∀ p, gPlus (gPlus p) = p) (hm : ∀ p, gMinus (gMinus p) = p) (q : Nat) :
    let b := gPlus ∘ gMinus
    let back := gMinus ∘ gPlus
    Function.LeftInverse (Nat.repeat back q) (Nat.repeat b q) ∧
      Function.RightInverse (Nat.repeat back q) (Nat.repeat b q) ∧
      gMinus ∘ Nat.repeat b q = Nat.repeat back q ∘ gMinus ∧
      gPlus ∘ Nat.repeat b q = Nat.repeat back q ∘ gPlus := by
  have inv := dihedralTimeReversal gPlus gMinus hp hm
  refine ⟨repeat_leftInverse inv.1 q, repeat_leftInverse inv.2.1 q, ?_, ?_⟩
  · apply repeat_intertwines
    intro p
    rfl
  · apply repeat_intertwines
    intro p
    simp [hp]

/-- The two chords preserve their respective characteristic coordinates. Zero
Dirichlet trace identifies the two pullbacks, giving invariance of their common
boundary profile under either chord and under the return map. -/
theorem zeroTraceInvariance {P X Y V : Type} (gPlus gMinus : P → P)
    (ξ : P → X) (η : P → Y) (A : X → V) (B : Y → V)
    (hp : ∀ p, ξ (gPlus p) = ξ p) (hm : ∀ p, η (gMinus p) = η p)
    (trace : ∀ p, A (ξ p) = B (η p)) :
    let H := A ∘ ξ
    H ∘ gPlus = H ∧ H ∘ gMinus = H ∧ H ∘ (gPlus ∘ gMinus) = H := by
  have plus (p : P) : A (ξ (gPlus p)) = A (ξ p) := congrArg A (hp p)
  have minus (p : P) : A (ξ (gMinus p)) = A (ξ p) := by
    rw [trace, hm, ← trace]
  exact ⟨funext plus, funext minus, funext (fun p => (plus (gMinus p)).trans (minus p))⟩

/-- The two graphs meet at both tips, at heights −1 and 1. -/
def leftWall (t : Rat) : Rat := t.abs - 1

def rightWall (t : Rat) : Rat :=
  min (1 - t.abs) (min (2/3 + t/3) (3/4 - 2*t/3))

def OnBoundary (s t : Rat) : Prop :=
  t.abs ≤ 1 ∧ (s = leftWall t ∨ s = rightWall t)

def InOpenHexagon (s t : Rat) : Prop :=
  t.abs < 1 ∧ leftWall t < s ∧ s < rightWall t

/-- The outer two right faces agree with the diamond. Inside the cutoff the
right graph lies between 1/4 and the diamond wall. -/
theorem hexagonWallBounds (t : Rat) :
    (3/4 ≤ t.abs → rightWall t = 1 - t.abs) ∧
    (t.abs ≤ 3/4 → 1/4 ≤ rightWall t) ∧ rightWall t ≤ 1 - t.abs := by
  grind only [rightWall, Rat.abs, Rat.min_def]

def mode (h : Rat → Rat) (s t : Rat) : Rat := h (1 - s.abs) - h t.abs

/-- The separated mode vanishes on all six walls for any profile vanishing
between zero and the cutoff. -/
theorem hexagonZeroTrace (h : Rat → Rat)
    (hzero : ∀ y, 0 ≤ y → y ≤ 3/4 → h y = 0) {s t : Rat} (hb : OnBoundary s t) :
    mode h s t = 0 := by
  obtain ⟨ht, hs | hs⟩ := hb
  · have hs' : 1 - s.abs = t.abs := by grind only [leftWall, Rat.abs]
    simp only [mode, hs', Rat.sub_self]
  · by_cases outer : 3/4 ≤ t.abs
    · have hr := (hexagonWallBounds t).1 outer
      have hs' : 1 - s.abs = t.abs := by grind only [Rat.abs]
      simp only [mode, hs', Rat.sub_self]
    · obtain ⟨hr, upper⟩ := (hexagonWallBounds t).2
      have lower := hr (by grind only)
      have hs' : s.abs = s := Rat.abs_of_nonneg (by grind only)
      have ht0 : 0 ≤ t.abs := Rat.abs_nonneg
      unfold mode
      rw [hs', hzero (1 - s) (by grind only) (by grind only), hzero t.abs ht0 (by grind only)]
      exact Rat.sub_self

/-- Four successive nondegenerate chords, horizontal then vertical twice.
The two free coordinates locate the intermediate intersections. The starting
and returning points lie on the left graph at heights −y and −z. -/
def FourChordReturn (y z : Rat) : Prop :=
  ∃ s t, OnBoundary (leftWall (-y)) (-y) ∧ OnBoundary s (-y) ∧
    OnBoundary s t ∧ OnBoundary (leftWall (-z)) t ∧ OnBoundary (leftWall (-z)) (-z) ∧
    leftWall (-y) ≠ s ∧ -y ≠ t ∧ s ≠ leftWall (-z) ∧ t ≠ -z

private theorem lower_right_face {y : Rat} (hy : 0 < y) (hhalf : y < 1/2) :
    rightWall (-y) = 2/3 - y/3 := by
  grind only [rightWall, Rat.abs, Rat.min_def]

private theorem local_right_fiber {y : Rat} (hy : 0 < y) (hhalf : y < 1/2) (t : Rat) :
    rightWall t = rightWall (-y) ↔ t = -y ∨ t = 1/8 + y/2 := by
  rw [lower_right_face hy hhalf]
  grind only [rightWall, Rat.abs, Rat.min_def]

/-- The local return map is derived from the four chord intersections. -/
theorem hexagonLocalReturn {y z : Rat} (hy : 0 < y) (hhalf : y < 1/2) :
    FourChordReturn y z ↔ z = 1/8 + y/2 := by
  have hr : 0 < rightWall (-y) := by
    rw [lower_right_face hy hhalf]
    grind only
  constructor
  · rintro ⟨s, t, _, hs, ht, hl, _, h₁, h₂, h₃, h₄⟩
    have hs' : s = rightWall (-y) := hs.2.resolve_left (Ne.symm h₁)
    have ht' : s = rightWall t := ht.2.resolve_left (by
      have bound := ht.1
      grind only [leftWall])
    have leg := (local_right_fiber hy hhalf t).mp (ht'.symm.trans hs')
    have htpos : t = 1/8 + y/2 := leg.resolve_left (Ne.symm h₂)
    have hl' : leftWall (-z) = leftWall t := hl.2.resolve_right (by grind only)
    grind only [leftWall, Rat.abs]
  · rintro rfl
    let z := 1/8 + y/2
    have equal := (local_right_fiber hy hhalf z).mpr (Or.inr rfl)
    refine ⟨rightWall (-y), z, ?_⟩
    dsimp only [z] at *
    grind only [OnBoundary, leftWall, Rat.abs]

/-- This neighborhood contains a unique closed circuit. The signed displacement
from the fixed point contracts by exactly one half at each return. -/
theorem hexagonFixedPointAndContraction {y : Rat} (hy : 0 < y) (hhalf : y < 1/2) :
    (FourChordReturn y y ↔ y = 1/4) ∧
    ∀ z, FourChordReturn y z → z - 1/4 = (1/2) * (y - 1/4) := by
  constructor
  · rw [hexagonLocalReturn hy hhalf]
    grind only
  · intro z h
    rw [(hexagonLocalReturn hy hhalf).mp h]
    grind only

/-- All noncollapsed rectangles with heights ±y have matching right corners
exactly at the isolated attracting height and on the neutral interval. -/
theorem hexagonPeriodicHeights {y : Rat} (hy : 0 < y) :
    (y < 1 ∧ rightWall y = rightWall (-y)) ↔ y = 1/4 ∨ (3/4 ≤ y ∧ y < 1) := by
  grind only [rightWall, Rat.abs, Rat.min_def]

/-- The continuous piecewise-linear witness. The middle affine piece crosses
zero at 7/8 on its way from 1 to −1. -/
def sharpProfile (y : Rat) : Rat :=
  if y ≤ 3/4 then 0
  else if y ≤ 13/16 then 16*y - 12
  else if y ≤ 15/16 then 14 - 16*y
  else if y ≤ 1 then 16*y - 16
  else 0

/-- The five specified profile values, the full range bound, and zero trace. -/
theorem sharpProfileData :
    [3/4, 13/16, 7/8, 15/16, 1].map sharpProfile = [0, 1, 0, -1, 0] ∧
    (∀ y, -1 ≤ sharpProfile y ∧ sharpProfile y ≤ 1) ∧
    (∀ s t, OnBoundary s t → mode sharpProfile s t = 0) := by
  refine ⟨?_, ?_, ?_⟩
  · simp only [List.map_cons, List.map_nil]
    grind only [sharpProfile]
  · intro y
    grind only [sharpProfile]
  · intro s t hb
    exact hexagonZeroTrace sharpProfile (fun y _ hy => by simp [sharpProfile, hy]) hb

/-- Perimeter of the attracting rectangle with lower and upper heights ±1/4. -/
def OnCircuit (s t : Rat) : Prop :=
  leftWall (1/4) ≤ s ∧ s ≤ rightWall (1/4) ∧ t.abs ≤ 1/4 ∧
    (s = leftWall (1/4) ∨ s = rightWall (1/4) ∨ t.abs = 1/4)

/-- Global sharpness is attained at an interior point of the tank. The
global upper bound in fact holds for every pair of rational coordinates. -/
theorem sharpGlobalAmplitude :
    (∀ s t, (mode sharpProfile s t).abs ≤ 2) ∧
    InOpenHexagon (1/16) (13/16) ∧ (mode sharpProfile (1/16) (13/16)).abs = 2 := by
  refine ⟨?_, ?_, ?_⟩
  · intro s t
    have hs := sharpProfileData.2.1 (1 - s.abs)
    have ht := sharpProfileData.2.1 t.abs
    grind only [mode, Rat.abs]
  · grind only [InOpenHexagon, leftWall, rightWall, Rat.abs, Rat.min_def]
  · decide +kernel

/-- The full circuit sees at most one unit. The top horizontal leg attains it
at s = 1/16. Together with the interior witness this gives the factor 1/2. -/
theorem sharpCircuitAmplitude :
    (∀ s t, OnCircuit s t → (mode sharpProfile s t).abs ≤ 1) ∧
    OnCircuit (1/16) (1/4) ∧ (mode sharpProfile (1/16) (1/4)).abs = 1 := by
  refine ⟨?_, ?_, ?_⟩
  · intro s t hc
    have ht := hc.2.2.1
    have hz : sharpProfile t.abs = 0 := ite_eq_left (by grind only)
    have hs := sharpProfileData.2.1 (1 - s.abs)
    unfold mode
    rw [hz]
    grind only [Rat.abs]
  · grind only [OnCircuit, leftWall, rightWall, Rat.min_def, Rat.abs]
  · decide +kernel

/-- Left-wall height after four reflections. On the right graph the vertical
chord exchanges t with −leftReturn(t). On the left graph it exchanges t with −t. -/
def leftReturn (t : Rat) : Rat :=
  if t ≤ -3/4 then t
  else if t ≤ -1/2 then 3/8 + 3*t/2
  else if t ≤ 1/12 then -1/8 + t/2
  else if t ≤ 3/8 then 2*t - 1/4
  else if t ≤ 3/4 then 1/4 + 2*t/3
  else t

/-- Right-wall height after the same four reflections, starting on the right. -/
def rightReturn (t : Rat) : Rat := -leftReturn (-t)

private theorem right_faces (t : Rat) :
    rightWall t = (if t ≤ -1/2 then 1 + t else if t ≤ 1/12 then 2/3 + t/3
      else if t ≤ 3/4 then 3/4 - 2*t/3 else 1 - t) := by
  grind only [rightWall, Rat.min_def, Rat.abs]

/-- Complete vertical fibers of both wall graphs, including the singleton
fiber at a tangency. The horizontal fibers are the two defining wall graphs. -/
theorem hexagonVerticalFibers (t v : Rat) (ht : t.abs ≤ 1) :
    (OnBoundary (rightWall t) v ↔ v = t ∨ v = -leftReturn t) ∧
    (OnBoundary (leftWall t) v ↔ v = t ∨ v = -t) := by
  simp only [OnBoundary, right_faces, leftWall]
  constructor <;> constructor <;> intro h <;> grind (splits := 18) only [leftReturn, Rat.abs]

/-- Exact directions of drift in all three nonperiodic gaps. Reflection in
height zero reverses the signed displacement when the launch wall is exchanged. -/
theorem hexagonBasinSigns (t : Rat) :
    (t < leftReturn t ↔ (-3/4 < t ∧ t < -1/4) ∨ (1/4 < t ∧ t < 3/4)) ∧
    (leftReturn t < t ↔ -1/4 < t ∧ t < 1/4) ∧
    rightReturn (-t) - (-t) = -(leftReturn t - t) := by
  refine ⟨?_, ?_, ?_⟩
  · grind only [leftReturn]
  · grind only [leftReturn]
  · simp only [rightReturn, Rat.neg_neg]
    grind only

private theorem exists_nat_mul_gt (v d : Rat) (hd : 0 < d) :
    ∃ n : Nat, v < (n : Rat) * d := by
  let c := (v/d).ceil
  have hc : v/d ≤ (c : Rat) := Rat.le_ceil
  have hc' : (c : Rat) ≤ (c.toNat : Rat) := by
    simpa only [Rat.intCast_natCast] using Rat.intCast_le_intCast.mpr (Int.self_le_toNat c)
  refine ⟨c.toNat + 1, (Rat.div_lt_iff hd).mp ?_⟩
  rw [Rat.natCast_add, Rat.natCast_ofNat]
  grind only

/-- Every rational tolerance eventually contains every subsequent return. -/
def ConvergesTo (step : Rat → Rat) (start limit : Rat) : Prop :=
  ∀ ε : Rat, 0 < ε → ∃ n₀ : Nat, ∀ n : Nat, n₀ ≤ n →
    (Nat.repeat step n start - limit).abs < ε

/-- In a forward-invariant segment, the distance decreases by at least δ
outside any ε-neighborhood and can never increase inside it. -/
private theorem converges_of_decrement {step : Rat → Rat} {start limit : Rat}
    (P : Rat → Prop) (hstart : P start) (hinv : ∀ t, P t → P (step t))
    (hinward : ∀ t, P t → (step t - limit).abs ≤ (t - limit).abs)
    (hdrop : ∀ ε : Rat, 0 < ε → ∃ δ : Rat, 0 < δ ∧ ∀ t, P t → ε ≤ (t - limit).abs →
      (step t - limit).abs + δ ≤ (t - limit).abs) : ConvergesTo step start limit := by
  let x (n : Nat) := Nat.repeat step n start
  have hP (n : Nat) : P (x n) := by
    induction n with
    | zero => exact hstart
    | succ k ih => exact hinv _ ih
  intro ε hε
  obtain ⟨δ, hδ, drop⟩ := hdrop ε hε
  -- Before the first entrance into the ε-neighborhood, at least nδ is lost.
  have estimate (n : Nat) :
      (x n - limit).abs < ε ∨ (x n - limit).abs + (n : Rat)*δ ≤ (start - limit).abs := by
    induction n with
    | zero =>
      right
      change (start - limit).abs + (0 : Rat)*δ ≤ (start - limit).abs
      simp [Rat.zero_mul, Rat.add_zero]
    | succ k ih =>
      change (step (x k) - limit).abs < ε ∨
        (step (x k) - limit).abs + ((k + 1 : Nat) : Rat)*δ ≤ (start - limit).abs
      have hm := hinward _ (hP k)
      by_cases small : (x k - limit).abs < ε
      · left
        exact Std.lt_of_le_of_lt hm small
      · right
        have hk := ih.resolve_left small
        have diff := drop _ (hP k) (by grind only)
        rw [Rat.natCast_add, Rat.natCast_ofNat]
        grind only
  obtain ⟨N, hN⟩ := exists_nat_mul_gt (start - limit).abs δ hδ
  refine ⟨N, ?_⟩
  intro n hn
  have order := Rat.mul_le_mul_of_nonneg_right (Rat.natCast_le_natCast.mpr hn) (Rat.le_of_lt hδ)
  have nonneg := Rat.abs_nonneg (x := x n - limit)
  exact (estimate n).resolve_right (by grind only)

private theorem interior_basin {x : Rat} (hlo : -3/4 < x) (hhi : x < 1/4) :
    ConvergesTo leftReturn x (-1/4) := by
  apply converges_of_decrement (fun t => min x (-1/4) ≤ t ∧ t ≤ max x (-1/4))
  · grind only [Rat.min_def, Rat.max_def]
  · intro t ht
    grind (splits := 14) only [leftReturn, Rat.min_def, Rat.max_def]
  · intro t ht
    grind (splits := 14) only [leftReturn, Rat.min_def, Rat.max_def, Rat.abs]
  · intro ε hε
    -- The three increments come from the middle branch and the two repelling ends.
    refine ⟨min (ε/2) (min ((x + 3/4)/2) (1/4 - x)), ?_, ?_⟩
    · grind only [Rat.min_def]
    · intro t ht he
      grind (splits := 18) only [leftReturn, Rat.min_def, Rat.max_def, Rat.abs]

private theorem endpoint_basin {x : Rat} (hlo : 1/4 < x) (hhi : x < 3/4) :
    ConvergesTo leftReturn x (3/4) := by
  apply converges_of_decrement (fun t => x ≤ t ∧ t ≤ 3/4)
  · grind only
  · intro t ht
    grind only [leftReturn]
  · intro t ht
    grind only [leftReturn, Rat.abs]
  · intro ε hε
    refine ⟨min (ε/3) (x - 1/4), ?_, ?_⟩
    · grind only [Rat.min_def]
    · intro t ht he
      grind only [leftReturn, Rat.min_def, Rat.abs]

private theorem reverse_basin {x c : Rat} (h : ConvergesTo leftReturn x c) :
    ConvergesTo rightReturn (-x) (-c) := by
  have mirror := repeat_intertwines (a := leftReturn) (back := rightReturn) (g := fun y => -y)
    (fun y => by simp [rightReturn, Rat.neg_neg])
  intro ε hε
  obtain ⟨N, tail⟩ := h ε hε
  refine ⟨N, ?_⟩
  intro n hn
  have hm : -Nat.repeat leftReturn n x = Nat.repeat rightReturn n (-x) := congrFun (mirror n) x
  have hh := tail n hn
  rw [← hm]
  grind only [Rat.abs]

/-- Forward limits for the open basins on both launch walls. Mirroring the
initial height exchanges the walls. The neutral arcs and isolated repeller are
fixed by four reflections. Convergence is quantified at every rational tolerance. -/
theorem hexagonBasinDynamics (x : Rat) :
    (-3/4 < x → x < 1/4 →
      ConvergesTo leftReturn x (-1/4) ∧ ConvergesTo rightReturn (-x) (1/4)) ∧
    (1/4 < x → x < 3/4 →
      ConvergesTo leftReturn x (3/4) ∧ ConvergesTo rightReturn (-x) (-(3/4))) ∧
    (((3/4 ≤ x.abs ∧ x.abs ≤ 1) ∨ x = 1/4) → leftReturn x = x ∧ rightReturn (-x) = -x) := by
  refine ⟨?_, ?_, ?_⟩
  · intro lo hi
    have left := interior_basin lo hi
    have right := reverse_basin left
    rw [show -((-1 : Rat)/4) = 1/4 by decide +kernel] at right
    exact ⟨left, right⟩
  · intro lo hi
    have left := endpoint_basin lo hi
    exact ⟨left, reverse_basin left⟩
  · intro fixed
    have hl : leftReturn x = x := by
      rcases fixed with outer | rfl
      · grind only [leftReturn, Rat.abs]
      · decide +kernel
    exact ⟨hl, by simp only [rightReturn, Rat.neg_neg, hl]⟩

/-- A uniformly distributed horizontal offset uses length two on each of two
equally probable launch walls. -/
private def arcMass (lo hi : Rat) : Rat := (hi - lo) / 4

/-- Four neutral arcs, two interior-attractor arcs, and two neutral-endpoint
arcs. The repelling cycle and the individual interval endpoints have zero length. -/
def offsetBasinWeights (a r : Rat) : Rat × Rat × Rat :=
  (2 * (arcMass (-1) (-a) + arcMass a 1),
   arcMass (-a) r + arcMass (-r) a,
   arcMass r a + arcMass (-a) (-r))

/-- Normalized masses of the neutral cylinder, isolated basin, and neutral
endpoint basin for the rational hexagon. -/
theorem hexagonBasinWeights :
    let (neutral, isolated, endpoint) := offsetBasinWeights (3/4) (1/4)
    neutral = 1/4 ∧ isolated = 1/2 ∧ endpoint = 1/4 ∧ neutral + isolated + endpoint = 1 := by
  dsimp only [offsetBasinWeights, arcMass]
  grind only

end Uncloakability
