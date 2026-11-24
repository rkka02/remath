"""
Phase 1 Deep Exact Markov Scouting Probe for Study #02.
Updated after Phase 2 read-only audit (C1, C3, M3, Minor 1, Minor 4 resolved):
  - Uses subtraction-free 72-digit GTH elimination (`phase1_chain.solve_game`) throughout.
  - Correctly reproduces Volkonskii's 1965 example (R=0.85, P=0.65, T=0.90, S=0.60),
    showing the historical architecture split where L selects CC and survey-D selects DD.
  - Includes n1=11 in the fixed-n2=10 memory scan and labels 10*gamma_c as a scaling prediction.
"""

from __future__ import annotations
import math
from fractions import Fraction
from phase1_chain import solve_game


def probe1_exact_correlation_exponent():
    print("=" * 78)
    print("PROBE 1: 72-DIGIT EXACT 2D-WALK CORRELATION EXPONENT (L_{2n,2})")
    print("=" * 78)
    game = ("0.8", "0.7", "0.9", "0.2")
    pR, pP = Fraction(4, 5), Fraction(7, 10)
    qR, qP = 1 - pR, 1 - pP
    for kap in ("0", "0.15", "0.20", "0.25", "0.30", "0.50", "0.80"):
        kf = Fraction(kap)
        logs = {}
        for n in (16, 20, 24, 28):
            cc, _, _, dd = solve_game(n, n, game, kappa_r=kap, kappa_p=kap, kind="L", digits=72)
            logs[n] = math.log(float(cc / dd))
        s16_20 = (logs[20] - logs[16]) / 4.0
        s20_24 = (logs[24] - logs[20]) / 4.0
        s24_28 = (logs[28] - logs[24]) / 4.0
        z_pred = float((pP**2 + kf * pP * qP) / (qP**2 + kf * pP * qP))
        th_A = math.log((1.0 / z_pred) / float(qR / pR))
        print(f"kap={float(kf):4.2f} | s16-20={s16_20:+.5f} s20-24={s20_24:+.5f} s24-28={s24_28:+.5f} | limit={th_A:+.5f}")


def probe2_volkonskii_1965_and_stag_hunt():
    print("\n" + "=" * 78)
    print("PROBE 2: VOLKONSKII (1965) ARCHITECTURE SPLIT & STAG HUNT FINITE REVERSAL")
    print("=" * 78)
    # Volkonskii (1965) pp. 46-47: q00=0.35, q10=0.40, q01=0.10, q11=0.15 => (R,P,T,S)=(0.85, 0.65, 0.90, 0.60)
    v_game = ("0.85", "0.65", "0.90", "0.60")
    print("Volkonskii (1965) pp. 46-47 exact tuple (R=0.85, P=0.65, T=0.90, S=0.60), kappa=0:")
    for kind in ("L", "D"):
        vals = [f"n={n}:{float(solve_game(n, n, v_game, '0', '0', kind=kind, digits=72)[0]):.6f}" for n in (4, 12, 24, 40)]
        print(f"  {kind} P(CC): " + " | ".join(vals))

    # Constant-hare Stag Hunt (15/16, 4/5, 4/5, 1/2): climbs to 82.30% at n=16 then collapses to 0%!
    sh_game = ("15/16", "4/5", "4/5", "1/2")
    print("\nConstant-hare Stag Hunt (R=15/16, P=T=4/5, S=1/2), kappa=0, L_{2n,2}:")
    vals = [f"n={n}:{float(solve_game(n, n, sh_game, '0', '0', kind='L', digits=72)[0]):.4f}" for n in (1, 2, 4, 8, 16, 32)]
    print("  P(CC): " + " | ".join(vals))


def probe3_asymmetric_memory_pd():
    print("\n" + "=" * 78)
    print("PROBE 3: ASYMMETRIC MEMORY SCAN (n2=10 fixed, 10 sampled depths in 4..34 including n1=11)")
    print("=" * 78)
    game = ("0.8", "0.6", "0.9", "0.2")
    gamma_c = math.log(4.0) / math.log(1.5) - 1.0
    print(f"PD (0.8, 0.6, 0.9, 0.2): large-memory ratio boundary gamma_c = {gamma_c:.6f} (scaling prediction n1 ~ {10*gamma_c:.2f} at n2=10)")
    for n1 in (4, 8, 10, 11, 12, 16, 20, 24, 28, 34):
        cc, cd, dc, dd = solve_game(n1, 10, game, "0", "0", kind="L", digits=72)
        W1 = 0.80 * float(cc) + 0.20 * float(cd) + 0.90 * float(dc) + 0.60 * float(dd)
        W2 = 0.80 * float(cc) + 0.90 * float(cd) + 0.20 * float(dc) + 0.60 * float(dd)
        print(f"  n1={n1:2d} (n1/n2={n1/10:4.2f}) | P(CC)={float(cc):.5f} P(DD)={float(dd):.5f} | W1={W1:.6f} W2={W2:.6f}")


if __name__ == "__main__":
    probe1_exact_correlation_exponent()
    probe2_volkonskii_1965_and_stag_hunt()
    probe3_asymmetric_memory_pd()
