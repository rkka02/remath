"""
High-precision 50-digit mpmath verification of Probe 1 correlation exponent and large-N GKT placement check.
Updated after Phase 2 read-only audit (M3, M10, Minor 4 resolved):
  - Validates architecture kind (supports L, B, D, K explicitly) and exact rational Frechet bounds.
  - Exact working precision matches printed labels (50-digit check).
  - Exact N=12 GKT placement Nash benchmark 19/120 = 0.1583 vs Moore opt 53/240 = 0.2208 (+39.47%).
"""

from __future__ import annotations
from decimal import Decimal
from fractions import Fraction
import math
import mpmath as mp
import numpy as np


def _to_exact_fraction(x) -> Fraction:
    """Convert finite int/float/Decimal/str/Fraction/mpf to exact Fraction without truncating mpf."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, float):
        if not math.isfinite(x):
            raise ValueError(f"Non-finite probability/correlation value: {x!r}")
        return Fraction(x)
    if isinstance(x, Decimal):
        if not x.is_finite():
            raise ValueError(f"Non-finite probability/correlation value: {x!r}")
        return Fraction(x)
    if isinstance(x, mp.mpf):
        if not mp.isfinite(x):
            raise ValueError(f"Non-finite probability/correlation value: {x!r}")
        sign, man, exp, _ = x._mpf_
        if man == 0:
            return Fraction(0)
        val = Fraction(man) * (Fraction(2) ** exp)
        return -val if sign else val
    return Fraction(str(x))


def _exact_frechet_check(p1_f: Fraction, p2_f: Fraction, kap_f: Fraction) -> tuple[bool, str]:
    """Validate exact Frechet bounds in rational arithmetic; return (at_endpoint, which_zero)."""
    q1_f, q2_f = 1 - p1_f, 1 - p2_f
    if not (0 < p1_f < 1 and 0 < p2_f < 1):
        raise ValueError(f"Marginal win probabilities must lie in (0,1); got ({p1_f}, {p2_f}).")
    if p1_f == p2_f:
        cov_f = kap_f * p1_f * q1_f
        if min(p1_f * p2_f + cov_f, q1_f * q2_f + cov_f, p1_f * q2_f - cov_f, q1_f * p2_f - cov_f) < 0:
            raise ValueError(f"Infeasible correlation kappa={kap_f} for marginals ({p1_f}, {p2_f}).")
        return False, ""
    prod_var = p1_f * q1_f * p2_f * q2_f
    if kap_f >= 0:
        cmax = min(p1_f, p2_f) - p1_f * p2_f
        lhs = kap_f * kap_f * prod_var
        rhs = cmax * cmax
        if lhs > rhs:
            raise ValueError(f"Infeasible positive correlation kappa={kap_f} for ({p1_f}, {p2_f}).")
        if lhs == rhs:
            return True, "01" if p1_f <= p2_f else "10"
        return False, ""
    cmin_abs = min(p1_f * p2_f, q1_f * q2_f)
    lhs = kap_f * kap_f * prod_var
    rhs = cmin_abs * cmin_abs
    if lhs > rhs:
        raise ValueError(f"Infeasible negative correlation kappa={kap_f} for ({p1_f}, {p2_f}).")
    if lhs == rhs:
        return True, "00" if p1_f * p2_f <= q1_f * q2_f else "11"
    return False, ""


def exact_2player_mp(n1: int, n2: int, p_mat, kappa_mat=None, kind: str = "L", dps: int = 50):
    """Exact mpmath stationary distribution of 2-player automaton game (4*n1*n2 states)."""
    if kind not in ("L", "B", "D", "K"):
        raise ValueError(f"Unsupported architecture kind={kind!r}; expected 'L', 'B', 'D', or 'K'.")
    mp.mp.dps = dps
    N1, N2 = 2 * n1, 2 * n2
    N = N1 * N2

    def idx(a1, d1, a2, d2):
        return (a1 * n1 + d1) * N2 + (a2 * n2 + d2)

    def trans(n, a, d, s):
        if s == 0:
            return [(a, n - 1, mp.mpf(1))] if kind == "D" else [(a, min(d + 1, n - 1), mp.mpf(1))]
        if d > 0:
            return [(a, d - 1, mp.mpf(1))]
        if kind == "B":
            return [(a, 0, mp.mpf("0.5")), (1 - a, 0, mp.mpf("0.5"))]
        return [(1 - a, 0, mp.mpf(1))]

    A = mp.matrix(N, N)
    for i in range(N):
        A[i, i] = -mp.mpf(1)

    for a1 in (0, 1):
        for a2 in (0, 1):
            p1_f = _to_exact_fraction(p_mat[a1][a2][0])
            p2_f = _to_exact_fraction(p_mat[a1][a2][1])
            kap_f = Fraction(0) if kappa_mat is None else _to_exact_fraction(kappa_mat[a1][a2])
            at_end, zero_cell = _exact_frechet_check(p1_f, p2_f, kap_f)
            q1_f, q2_f = 1 - p1_f, 1 - p2_f
            if p1_f == p2_f or at_end:
                if p1_f == p2_f:
                    cov_f = kap_f * p1_f * q1_f
                elif zero_cell == "01":
                    cov_f = p1_f * q2_f
                elif zero_cell == "10":
                    cov_f = q1_f * p2_f
                elif zero_cell == "00":
                    cov_f = -p1_f * p2_f
                else:
                    cov_f = -q1_f * q2_f
                if kind == "K":
                    q1_f, q2_f, cov_f = q1_f / 2, q2_f / 2, cov_f / 4
                    p1_f, p2_f = 1 - q1_f, 1 - q2_f
                exact_p = {
                    (0, 0): p1_f * p2_f + cov_f,
                    (0, 1): p1_f * q2_f - cov_f,
                    (1, 0): q1_f * p2_f - cov_f,
                    (1, 1): q1_f * q2_f + cov_f,
                }
                probs = {k: (mp.mpf(0) if v == 0 else mp.mpf(v.numerator) / v.denominator) for k, v in exact_p.items()}
            else:
                p1, p2 = mp.mpf(p1_f.numerator) / p1_f.denominator, mp.mpf(p2_f.numerator) / p2_f.denominator
                q1, q2 = 1 - p1, 1 - p2
                kap = mp.mpf(kap_f.numerator) / kap_f.denominator
                cov = kap * mp.sqrt(p1 * q1 * p2 * q2)
                if kind == "K":
                    q1, q2, cov = q1 / 2, q2 / 2, cov / 4
                    p1, p2 = 1 - q1, 1 - q2
                probs = {
                    (0, 0): p1 * p2 + cov,
                    (0, 1): p1 * q2 - cov,
                    (1, 0): q1 * p2 - cov,
                    (1, 1): q1 * q2 + cov,
                }
            for d1 in range(n1):
                for d2 in range(n2):
                    r = idx(a1, d1, a2, d2)
                    for (s1, s2), pr in probs.items():
                        if pr == 0:
                            continue
                        for na1, nd1, w1 in trans(n1, a1, d1, s1):
                            for na2, nd2, w2 in trans(n2, a2, d2, s2):
                                A[idx(na1, nd1, na2, nd2), r] += pr * w1 * w2

    for j in range(N):
        A[N - 1, j] = mp.mpf(1)
    b = mp.matrix(N, 1)
    b[N - 1, 0] = mp.mpf(1)
    pi = mp.lu_solve(A, b)

    ap = [[mp.mpf(0), mp.mpf(0)], [mp.mpf(0), mp.mpf(0)]]
    for a1 in (0, 1):
        for a2 in (0, 1):
            ap[a1][a2] = sum(pi[idx(a1, d1, a2, d2)] for d1 in range(n1) for d2 in range(n2))
    return ap


def check_exact_exponent_mp():
    dps = 50
    print("=" * 78)
    print(f"{dps}-DIGIT MPMATH CHECK: EXACT 2D CORRELATED WALK EXPONENT IN PRISONER'S DILEMMA")
    print("=" * 78)
    mp.mp.dps = dps
    pR, pP = mp.mpf("0.8"), mp.mpf("0.7")
    qR, qP = 1 - pR, 1 - pP
    p_mat = [[("0.8", "0.8"), ("0.2", "0.9")], [("0.9", "0.2"), ("0.7", "0.7")]]
    for kap_str in ("0.0", "0.2", "0.3", "0.5"):
        kap = mp.mpf(kap_str)
        kmat = [[kap_str, "0.0"], ["0.0", kap_str]]
        logs = {}
        for n in (6, 8, 10):
            ap = exact_2player_mp(n, n, p_mat, kmat, kind="L", dps=dps)
            logs[n] = mp.log(ap[0][0] / ap[1][1])
        s8_10 = (logs[10] - logs[8]) / 2
        z_pred = (pP**2 + kap * pP * qP) / (qP**2 + kap * pP * qP)
        th_A = mp.log((1 / z_pred) / (qR / pR))
        print(f"kap={kap_str} | s8-10={float(s8_10):+.6f} | limit={float(th_A):+.6f}")


def check_largeN_partial_common_fund_mc():
    print("\n" + "=" * 78)
    print("LARGE-N (N=12, K=12) GKT PLACEMENT GAME: PARTIAL POOLING alpha IN [0,1]")
    print("=" * 78)
    # Exact Nash occupancy: 1/6 > 3/20 > 1/7 => 6 on site 0, 6 on distinct small sites:
    # Nash mean raw welfare = (1 + 6*3/20)/12 = 19/120 = 0.158333...
    # Moore optimum: 1 on site 0, 11 on small sites => (1 + 11*3/20)/12 = 53/240 = 0.220833... (+39.47%).
    nash_u = Fraction(19, 120)
    opt_u = Fraction(53, 240)
    rel_gain = 100.0 * float((opt_u - nash_u) / nash_u)
    print(f"Exact benchmarks: Nash avg u = 19/120 ({float(nash_u):.4f}), Moore opt avg u = 53/240 ({float(opt_u):.4f}, +{rel_gain:.2f}%)")
    rng = np.random.default_rng(42)
    N, K = 12, 12
    caps = np.array([1.0] + [0.15] * (K - 1))
    T, burn = 20000, 5000
    for n in (3, 6):
        row = []
        for alpha in (0.0, 0.30, 0.70, 1.0):
            act = rng.integers(0, K, size=N)
            dep = np.full(N, n - 1, dtype=int)
            tot_u = 0.0
            for t in range(T):
                counts = np.bincount(act, minlength=K)
                u_indiv = caps[act] / counts[act]
                u_avg = u_indiv.mean()
                if t >= burn:
                    tot_u += u_avg
                p_win = 0.5 * (1.0 + (1.0 - alpha) * u_indiv + alpha * u_avg)
                win = rng.random(N) < p_win
                dep = np.where(win, np.minimum(dep + 1, n - 1), dep - 1)
                switch = dep < 0
                if np.any(switch):
                    dep[switch] = 0
                    act[switch] = rng.integers(0, K, size=switch.sum())
            row.append(f"a={alpha:.2f}:{tot_u/(T-burn):.4f}")
        print(f"  n={n:2d}: " + " | ".join(row))


if __name__ == "__main__":
    check_exact_exponent_mp()
    check_largeN_partial_common_fund_mc()
