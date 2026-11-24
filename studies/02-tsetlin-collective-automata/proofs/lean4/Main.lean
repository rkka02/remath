import ArchitectureHierarchy
import EscapeGeometry
import FairGameCancellation
import StagHuntMirage
import CommonFundCutoff
import Lean.Elab.Command
import Lean.Util.CollectAxioms

/-! Axiom audit for the public theorems of the five study modules. -/

-- ArchitectureHierarchy
#print axioms ArchitectureHierarchy.krinsky_minus_linear
#print axioms ArchitectureHierarchy.krylov_minus_krinsky
#print axioms ArchitectureHierarchy.linear_lt_krinsky
#print axioms ArchitectureHierarchy.krinsky_lt_krylov
#print axioms ArchitectureHierarchy.synchronized_thresholds
#print axioms ArchitectureHierarchy.private_coin_joint_law
#print axioms ArchitectureHierarchy.krylov_private_coin_reduction
#print axioms ArchitectureHierarchy.krylov_threshold_iff
#print axioms ArchitectureHierarchy.benchmark_thresholds
#print axioms ArchitectureHierarchy.volkonskii_threshold_split
#print axioms ArchitectureHierarchy.volkonskii_linear_odds_ratio
#print axioms ArchitectureHierarchy.weak_reward_reversal_witness

-- EscapeGeometry
#print axioms EscapeGeometry.natural_tilt_weights
#print axioms EscapeGeometry.tilted_mass_and_drifts
#print axioms EscapeGeometry.tilted_transverse_variance
#print axioms EscapeGeometry.phi_one
#print axioms EscapeGeometry.optimal_correlation_interior
#print axioms EscapeGeometry.tilted_weights_positive
#print axioms EscapeGeometry.drift_alignment_iff
#print axioms EscapeGeometry.curvature_pos
#print axioms EscapeGeometry.phi_squeeze
#print axioms EscapeGeometry.phi_strict_antitone
#print axioms EscapeGeometry.phi_half
#print axioms EscapeGeometry.hesitant_feasibility
#print axioms EscapeGeometry.odds_lt_iff
#print axioms EscapeGeometry.flip_threshold_odds
#print axioms EscapeGeometry.flip_interval_iff
#print axioms EscapeGeometry.flip_benchmark
#print axioms EscapeGeometry.perfect_correlation_barrier_data
#print axioms EscapeGeometry.perfect_correlation_return
#print axioms EscapeGeometry.public_good_advantage
#print axioms EscapeGeometry.public_good_balance
#print axioms EscapeGeometry.public_good_three_player
#print axioms EscapeGeometry.adjacent_memory_stationarity
#print axioms EscapeGeometry.adjacent_memory_witness
#print axioms EscapeGeometry.adjacent_memory_payoffs
#print axioms EscapeGeometry.forty_loss_path

-- FairGameCancellation
#print axioms FairGameCancellation.residence_green
#print axioms FairGameCancellation.excursion_green
#print axioms FairGameCancellation.two_point_revisit
#print axioms FairGameCancellation.two_point_hit
#print axioms FairGameCancellation.any_exit_per_excursion
#print axioms FairGameCancellation.revisit_factorization
#print axioms FairGameCancellation.immediate_and_revisit_ratios
#print axioms FairGameCancellation.three_way_cancellation
#print axioms FairGameCancellation.cancellation_equal_origins
#print axioms FairGameCancellation.depth_one_rows_sum
#print axioms FairGameCancellation.depth_one_dirichlet
#print axioms FairGameCancellation.depth_one_dd_rows
#print axioms FairGameCancellation.depth_one_linear_values
#print axioms FairGameCancellation.depth_one_boundary_values
#print axioms FairGameCancellation.depth_one_strict_comparison
#print axioms FairGameCancellation.depth_one_linear_stationary
#print axioms FairGameCancellation.depth_one_boundary_stationary

-- StagHuntMirage
#print axioms StagHuntMirage.G_closed
#print axioms StagHuntMirage.reference_entry_flux
#print axioms StagHuntMirage.G_half
#print axioms StagHuntMirage.reference_entry_flux_half
#print axioms StagHuntMirage.G_strict_mono
#print axioms StagHuntMirage.below_critical_iff
#print axioms StagHuntMirage.critical_antitone
#print axioms StagHuntMirage.ladder_equations_iff
#print axioms StagHuntMirage.transmission_cancellation
#print axioms StagHuntMirage.leading_constant
#print axioms StagHuntMirage.transition_row_sum
#print axioms StagHuntMirage.pi1_stationary
#print axioms StagHuntMirage.transition_positive
#print axioms StagHuntMirage.pi1_positive
#print axioms StagHuntMirage.pi1_normalized
#print axioms StagHuntMirage.pi1_unique
#print axioms StagHuntMirage.pi1_cc_mono
#print axioms StagHuntMirage.open_region_upper
#print axioms StagHuntMirage.corner_one
#print axioms StagHuntMirage.corner_two
#print axioms StagHuntMirage.corner_three
#print axioms StagHuntMirage.three_open_regions
#print axioms StagHuntMirage.benchmark_47_50

-- CommonFundCutoff
#print axioms CommonFundCutoff.duration_add_level
#print axioms CommonFundCutoff.ladder_detailed_balance
#print axioms CommonFundCutoff.duration_strict
#print axioms CommonFundCutoff.duration_ratio_depth_step
#print axioms CommonFundCutoff.quota_gap_formula
#print axioms CommonFundCutoff.quotaRatio_depth_strict
#print axioms CommonFundCutoff.quotaRatio_full_pool
#print axioms CommonFundCutoff.quotaRatio_share_strict
#print axioms CommonFundCutoff.duration_one
#print axioms CommonFundCutoff.duration_two
#print axioms CommonFundCutoff.depth_one_quota_iff
#print axioms CommonFundCutoff.depth_one_share_feasible_iff
#print axioms CommonFundCutoff.depth_one_quota_balance
#print axioms CommonFundCutoff.quota_welfare_and_extremes
#print axioms CommonFundCutoff.full_pool_fraction
#print axioms CommonFundCutoff.depth_one_below_nash_iff
#print axioms CommonFundCutoff.private_quota_example
#print axioms CommonFundCutoff.private_fixed_point_below_quota
#print axioms CommonFundCutoff.quota_welfare_maximum
#print axioms CommonFundCutoff.response_from_ratio
#print axioms CommonFundCutoff.quota_ratio_iff_quota_mass
#print axioms CommonFundCutoff.benchmark_shares
#print axioms CommonFundCutoff.benchmark_endpoint_welfares
#print axioms CommonFundCutoff.benchmark_nash_ratios
#print axioms CommonFundCutoff.critical_depth_two
#print axioms CommonFundCutoff.no_productive_fixed_point
#print axioms CommonFundCutoff.depth_one_algebraic_quota
#print axioms CommonFundCutoff.quota_response_deficit
#print axioms CommonFundCutoff.depthTwo_quota_iff_polynomial
#print axioms CommonFundCutoff.depthTwoShare_polynomial
#print axioms CommonFundCutoff.depthTwoShare_bracket
#print axioms CommonFundCutoff.depthTwoShare_quota_and_unique
#print axioms CommonFundCutoff.depthTwo_quota_polynomial_residual
#print axioms CommonFundCutoff.benchmark_depth_two_odds
#print axioms CommonFundCutoff.depth_two_quota_share
#print axioms CommonFundCutoff.depth_two_rational_bracket
#print axioms CommonFundCutoff.depth_two_means_of_stationary
#print axioms CommonFundCutoff.depth_two_stationary_welfare_certificate
#print axioms CommonFundCutoff.depth_two_welfare_bound_at_nash
#print axioms CommonFundCutoff.depth_two_stationary_welfare_gap

-- Also check private lemmas and compiler-generated proofs. The same axiom
-- collector backs #print axioms. An unexpected dependency fails the build.
open Lean Elab Command in
run_cmd
  let env ← getEnv
  let modules := [`ArchitectureHierarchy, `EscapeGeometry, `FairGameCancellation,
    `StagHuntMirage, `CommonFundCutoff]
  let allowed := [`propext, `Classical.choice, `Quot.sound]
  let mut count : Nat := 0
  for (decl, info) in env.constants.toList do
    if let some idx := env.getModuleIdxFor? decl then
      if modules.contains env.header.moduleNames[idx.toNat]! then
        match info with
        | .axiomInfo _ => throwError "Custom axiom {decl}"
        | .thmInfo _ =>
          for dep in ← collectAxioms decl do
            unless allowed.contains dep do throwError "Unexpected axiom {dep} in {decl}"
          count := count + 1
        | _ => pure ()
  logInfo m!"Verified the axiom whitelist for {count} theorem constants in the five study modules."
