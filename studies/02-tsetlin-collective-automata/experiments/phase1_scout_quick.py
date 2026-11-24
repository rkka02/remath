"""
Phase 1 Quick Exact Markov Scouting Probe for Study #02 (Tsetlin Collective Automata).
Updated after Phase 2 read-only audit (C1, M3, M11, M13, Minor 4 resolved):
  - Uses subtraction-free 70-digit GTH state elimination (`phase1_chain.solve_game`) instead of
    ill-conditioned binary64 linear solves.
  - Validates architecture kinds and exact Frechet correlation bounds.
  - Distinguishes zero-sum-in-expectation (independent outcomes, mixed value 24/35) from
    Tsetlin (1963 §6) complementary-outcome B-automaton zero-sum games.
  - Correctly labels the static threshold where CC first becomes a Nash equilibrium.
"""

from __future__ import annotations
import math
from fractions import Fraction
from phase1_chain import solve_game


def probe_vein1_pd_correlation():
    print("=" * 78)
    print("VEIN 1: BLIND PRISONER'S DILEMMA + CORRELATION FLIP (EXACT SAME PAYOFFS!)")
    print("=" * 78)
    game = ("0.8", "0.7", "0.9", "0.2")
    pR, pP, pT, pS = map(Fraction, game)
    qR, qP = 1 - pR, 1 - pP
    rho_R = qR / pR
    rho_P = qP / pP
    kappa_c_L = (qR * pP**2 - pR * qP**2) / ((pR - qR) * pP * qP)
    kappa_c_D = (qR - qP**2) / (pP * qP)
    print(f"PD params: pT={float(pT)}, pR={float(pR)}, pP={float(pP)}, pS={float(pS)}")
    print(f"  Exact critical correlation: L/B = {kappa_c_L} ({float(kappa_c_L):.6f}), survey-D = {kappa_c_D} ({float(kappa_c_D):.6f})")

    for kind in ("L", "D"):
        print(f"\n--- Automaton kind = {kind}_{{2n,2}} (70-digit subtraction-free GTH) ---")
        print(f"{'kappa':>7s} | " + " | ".join(f"n={n:2d}" for n in (4, 8, 12, 16, 20)))
        for kap in ("0", "0.10", "0.15", "0.20", "0.25", "0.30", "0.40", "0.60", "0.90"):
            vals = []
            for n in (4, 8, 12, 16, 20):
                cc, cd, dc, dd = solve_game(n, n, game, kappa_r=kap, kappa_p=kap, kind=kind, digits=70)
                vals.append(f"{float(cc):6.4f}")
            print(f"{float(kap):7.2f} | " + " | ".join(vals))

    print("\n--- Exact Exponential Rate Check for L_{2n,2} (secant from n=16 to n=20) ---")
    for kap in ("0", "0.10", "0.20", "0.25", "0.30", "0.50", "0.80"):
        k_f = Fraction(kap)
        ratios = {}
        for n in (16, 20):
            cc, _, _, dd = solve_game(n, n, game, kappa_r=kap, kappa_p=kap, kind="L", digits=70)
            ratios[n] = math.log(float(cc / dd))
        emp_slope = (ratios[20] - ratios[16]) / 4.0
        z_pred = float((pP**2 + k_f * pP * qP) / (qP**2 + k_f * pP * qP))
        th_slope = math.log((1.0 / z_pred) / float(rho_R))
        print(f"kap={float(kap):4.2f} | emp_slope(16->20)={emp_slope:+.6f} | limit_slope={th_slope:+.6f}")


def probe_vein2_finite_memory_and_asymmetry():
    print("\n" + "=" * 78)
    print("VEIN 2: FINITE-MEMORY & ASYMMETRIC MEMORY (70-digit GTH)")
    print("=" * 78)
    game = ("0.8", "0.7", "0.9", "0.2")
    print("2A. Symmetric PD in Defection phase (pR=0.80, pP=0.70, pT=0.90, pS=0.20, kappa=0):")
    for n in (1, 2, 4, 8, 10, 14, 20):
        cc, cd, dc, dd = solve_game(n, n, game, "0", "0", kind="L", digits=70)
        W = 0.80 * float(cc) + 0.55 * float(cd + dc) + 0.70 * float(dd)
        print(f"  n={n:2d}: P(CC)={float(cc):.5f}, P(CD+DC)={float(cd+dc):.5f}, P(DD)={float(dd):.5f}, E[p]={W:.5f}")

    print("\n2B. Asymmetric Memory (n1 vs n2) in Prisoner's Dilemma (pR=0.80, pP=0.60, pT=0.90, pS=0.20):")
    game_pd2 = ("0.8", "0.6", "0.9", "0.2")
    for n1, n2 in [(4, 4), (8, 4), (10, 10), (11, 10), (12, 10), (12, 12)]:
        cc, cd, dc, dd = solve_game(n1, n2, game_pd2, "0", "0", kind="L", digits=70)
        W1 = 0.80 * float(cc) + 0.20 * float(cd) + 0.90 * float(dc) + 0.60 * float(dd)
        W2 = 0.80 * float(cc) + 0.90 * float(cd) + 0.20 * float(dc) + 0.60 * float(dd)
        print(f"  (n1={n1:2d}, n2={n2:2d}): P(CC)={float(cc):.5f} P(DD)={float(dd):.5f} | W1={W1:.5f} W2={W2:.5f}")

    print("\n2C. Zero-sum-in-expectation 2x2 game (independent outcomes, mixed value 24/35 = 0.68571):")
    # Note: distinct from Tsetlin (1963 §6), which uses B automata and complementary realized outcomes.
    # Matrix [[0.8, 0.6], [0.4, 0.9]] -> classical mixed-strategy row value = (0.8*0.9 - 0.6*0.4)/(0.8 + 0.9 - 0.6 - 0.4) = 24/35.
    print("  Classical mixed-strategy row value = 24/35 =", f"{24/35:.6f}")


def probe_vein3_partial_common_fund():
    print("\n" + "=" * 78)
    print("VEIN 3: PARTIAL COMMON FUND (alpha in [0,1]) IN 2-PLAYER PD")
    print("=" * 78)
    pR, pP, pT, pS = Fraction(4, 5), Fraction(7, 10), Fraction(19, 20), Fraction(7, 20)
    alpha_cc_nash = (pT - pR) / ((pT - pS) / 2)
    print(f"3A. 2-player PD with Partial Pooling: pR=0.80, pP=0.70, pT=0.95, pS=0.35")
    print(f"    CC first becomes a Nash equilibrium at alpha = {alpha_cc_nash} (DD remains strict Nash through alpha=1).")
    for alpha_str in ("0", "0.2", "0.5", "0.6", "0.8", "1"):
        a = Fraction(alpha_str)
        pS_a = (1 - a) * pS + a * (pT + pS) / 2
        pT_a = (1 - a) * pT + a * (pT + pS) / 2
        g = (str(pR), str(pP), str(pT_a), str(pS_a))
        res = [f"{float(solve_game(n, n, g, '0', '0', kind='L', digits=70)[0]):.4f}" for n in (4, 8, 12, 18)]
        print(f"  alpha={float(a):4.2f} (pS={float(pS_a):.3f}, pT={float(pT_a):.3f}) | P(CC) @ n=4,8,12,18: " + "  ".join(res))


if __name__ == "__main__":
    probe_vein1_pd_correlation()
    probe_vein2_finite_memory_and_asymmetry()
    probe_vein3_partial_common_fund()
