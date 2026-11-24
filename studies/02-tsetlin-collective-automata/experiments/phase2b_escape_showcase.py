"""Reproduce certified unequal-memory stationary masses and escape-geometry data.

    python3 experiments/phase2b_escape_showcase.py --jobs 2
    python3 experiments/phase2b_escape_showcase.py --geometry

The first command regenerates the stationary JSON. The second regenerates the
companion full-game bridge grids. --case R N_SHORT K_R K_P TACTIC prints one
stationary calculation. A C++17 compiler and GMP are required for the former.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from math import lcm
from pathlib import Path

from phase1_chain import game_rows_exact
from phase1_reversal import integer_determinant
from phase2b_stationary import fraction_decimal, solve_game_certified

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "data" / "phase2b_escape_showcase.json"
PROFILES = ("CC", "CD", "DC", "DD")
DIGITS = 76


def exact_check():
    """Small-chain determinants, a rounding midpoint and the perfect-shock bound."""
    game = (".82", ".60", ".90", ".20")
    for kind, kr, kp in (("L", "1", "1"), ("B", "2/3", "2/3")):
        n1, n2 = 3, 2
        states, rows = game_rows_exact(n1, n2, game, kr, kp, kind, False)
        scale = lcm(*(w.denominator for row in rows for w in row.values()))
        matrix = [[0] * len(rows) for _ in rows]
        for i, row in enumerate(rows):
            for j, w in row.items():
                weight = int(w * scale)
                matrix[i][i] += weight
                matrix[j][i] -= weight
        matrix[-1] = [1] * len(rows)
        determinant = integer_determinant(matrix)
        result = solve_game_certified(n1, n2, game, kr, kp, kind, digits=DIGITS)
        for profile, (low, high) in enumerate(result.intervals):
            matrix[-1] = [int(2 * (i >= n1) + (j >= n2) == profile) for i, j in states]
            numerator = integer_determinant(matrix)
            assert low <= Fraction(numerator, determinant) <= high
    # State-independent opponents give two independent two-state chains, each
    # with cooperation fraction .500000005. Its square sits on a decimal tie.
    midway = (".700000003", ".699999997", ".699999997", ".700000003")
    with localcontext() as ctx:
        ctx.rounding = ROUND_FLOOR
        result = solve_game_certified(1, 1, midway, digits=17, working_digits=45)
    cc = Fraction(".500000005")**2
    assert result.intervals[0] == (cc, cc)
    assert result.mass[0] == Decimal(".25000000500000002")

    # At kappa_P=1 test e^s=2. A negative quadratic at 2/3 puts the
    # mixed lower root below 2/3, so both interface constraints are slack.
    p, t, s = map(Fraction, game[1:])
    odds = p / (1 - p)
    m = t / 2 + (1 - t) * 2
    z = Fraction(2, 3)
    assert m*s*z*z - z + m*(1-s) == Fraction(-4, 45)
    assert z < 1/(2-z) == odds/2
    assert odds * 2**2 > odds**4


def benchmark_case(args):
    r, short, kr, kp, kind = args
    short = int(short)
    game = (r, ".60", ".90", ".20")
    work = 195 if short >= 75 else 170
    result = solve_game_certified(3 * short, short, game, kr, kp, kind,
                                  digits=DIGITS, working_digits=work)
    bounds = {}
    for name, (low, high) in zip(PROFILES, result.intervals):
        bounds[name] = [str(fraction_decimal(low, 83, ROUND_FLOOR)),
                        str(fraction_decimal(high, 83, ROUND_CEILING))]
    kr_f, kp_f = Fraction(kr), Fraction(kp)
    return dict(R=r, n1=3*short, n2=short, tactic=kind, kappa_R=kr, kappa_P=kp,
                protocols=(["fixed_CC_independent"] if kr_f == 0 else []) +
                          (["matched"] if kr_f == kp_f else []),
                closed_states=result.closed_states, working_digits=result.working_digits,
                stationary=dict(zip(PROFILES, map(str, result.mass))), enclosures=bounds)


def benchmark_grid():
    for r, n in (("0.80", 80), ("0.82", 40), ("0.82", 50)):
        for kr, kp in (("0", "0"), ("0", "2/3"), ("0", "1"), ("2/3", "2/3"), ("1", "1")):
            for kind in ("L", "B"):
                yield r, n, kr, kp, kind


def collect(jobs):
    exact_check()
    tasks = list(benchmark_grid())
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        rows = []
        for row in pool.map(benchmark_case, tasks):
            rows.append(row)
            print(f"R={row['R']} ({row['n1']},{row['n2']}) {row['tactic']} "
                  f"kR={row['kappa_R']} kP={row['kappa_P']} "
                  f"CC={Decimal(row['stationary']['CC']):.15g}", flush=True)
    return {
        "game": {"P": "0.60", "T": "0.90", "S": "0.20",
                 "mixed_profile_feedback": "independent", "memory_ratio": "3"},
        "observable": "Stationary mass of each ordered action pair. The first player has the long memory.",
        "protocols": {"fixed_CC_independent": "kappa_R = 0", "matched": "kappa_R = kappa_P"},
        "certification": {
            "significant_digits": DIGITS,
            "method": "Subtraction-free GTH on the unique recurrent class, followed by four exact integer Poisson-residual enclosures.",
            "enclosures": "Exact rational extrema are rounded outward to 83 significant digits. Each stationary decimal is the common 76-digit rounding of both exact endpoints.",
            "kernel": "Rational transitions include independent private boundary coins for B. Holding entries are implicit in off-diagonal balance.",
            "small_grid_check": "Integer Bareiss determinants independently verify every profile of asymmetric 3-by-2 memory examples for both tactics."
        },
        "cases": rows,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--jobs", type=int, default=1, help="parallel stationary calculations")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--geometry", action="store_true", help="regenerate companion bridge grids")
    group.add_argument("--case", nargs=5, metavar=("R", "N_SHORT", "K_R", "K_P", "TACTIC"))
    args = parser.parse_args()
    if args.geometry:
        subprocess.run([sys.executable, str(HERE / "phase2b_escape_geometry.py"),
                        "--jobs", str(args.jobs)], check=True)
    elif args.case:
        print(json.dumps(benchmark_case(args.case), indent=2))
    else:
        result = collect(args.jobs)
        OUTPUT.parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=OUTPUT.parent) as temp:
            staged = Path(temp) / OUTPUT.name
            staged.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            staged.replace(OUTPUT)


if __name__ == "__main__":
    main()
