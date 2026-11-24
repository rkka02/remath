"""Stationary Stag Hunt curves, exact open-region witnesses and peak scaling.

Run from any directory with Python 3.9+, GNU MP and a C++17 compiler.
Each plotted stationary probability has an exact rational Poisson-residual
enclosure from the finite game. The three rectangle witnesses are also solved
by rational GTH. Reference functions are evaluated separately.
"""

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from phase1_chain import dissection, game_rows_exact, stationary
from phase1_reversal import exact_grid, n1_masses
from phase2b_stationary import fraction_decimal, solve_game_certified


P = Fraction(4, 5)
HALF = Fraction(1, 2)
DIGITS = 76
OUTPUT = Path(__file__).resolve().parent / "data" / "phase2b_staghunt_grid.json"
DEPTHS = (1, 2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 48, 64)
R_BY_S = {
    "0.35": ("0.9375", "0.94"),
    "0.40": ("0.9375", "0.94"),
    "0.45": ("0.9375", "0.94"),
    "0.47": ("0.9375", "0.94"),
    "0.48": ("0.9375", "0.94"),
    "0.49": ("0.9385",),
    "0.50": ("0.935", "0.9375", "0.939", "0.94", "0.9405"),
    "0.52": ("0.9325", "0.935", "0.93625"),
    "0.55": ("0.925", "0.928", "0.929"),
}
EXTRA_DEPTHS = {
    ("0.45", "0.94"): (11, 13, 96),
    ("0.47", "0.94"): (14, 15, 17),
    ("0.48", "0.9375"): (96, 128),
    ("0.48", "0.94"): (18, 22, 96, 128),
    ("0.49", "0.9385"): (96, 128, 160),
    ("0.50", "0.9375"): (80, 120, 160),
    ("0.52", "0.935"): (96,),
    ("0.55", "0.925"): (96, 128),
    ("0.55", "0.928"): (96, 128),
    ("0.55", "0.929"): (17, 18, 26, 28, 30),
}
# The lower corners and one finite depth on which the uniform 4/5 bound rests.
ANCHORS = (("0.47", "0.94", 16), ("0.52", "0.935", 10),
           ("0.5499", "0.929", 18))


def show(value):
    """Human-readable decimal, rounded to at most DIGITS significant figures."""
    return format(value, f".{DIGITS}g")


def dec(value):
    return Decimal(value.numerator) / Decimal(value.denominator)


def critical(s):
    a = max(Fraction(1), s / (1 - s))
    return P**2 / (P**2 + (1 - P)**2 * a)


def maximum_s(r):
    ratio = P**2 * (1 - r) / ((1 - P)**2 * r)
    return ratio / (1 + ratio)


def lmbda(r):
    return ((1 - P) / P)**2 * r / (1 - r)


def K(r, s):
    return (2 * P - 1)**2 / ((1 - s) * (2 * r - 1))


def profile(s, r):
    return (r, P, P, s)


def solve(task):
    s, r, n = task
    certified = solve_game_certified(
        n, n, profile(s, r), digits=DIGITS + 12, working_digits=114 + 2 * n)
    if n == 1:
        assert fraction_decimal(certified.intervals[0][0], DIGITS) == fraction_decimal(n1_masses(profile(s, r))[0], DIGITS)
    with localcontext() as ctx:
        ctx.prec = 94
        cc_full = certified.mass[0]
        outside_full = sum(certified.mass[1:])
    return task, (cc_full, outside_full, certified.working_digits, certified.intervals[0])


def scaled(r, n, masses, b):
    cc, outside, _, _ = masses
    with localcontext() as ctx:
        ctx.prec = 94
        delta = -dec(lmbda(r)).ln()
        x = n * delta
        reference = x * (-x).exp() if not b else (
            (-(1 - b) * x).exp() - (-x).exp()) / b
        obs_odds = delta * cc / (outside * dec(K(critical(HALF), HALF)))
    return {
        "n": n, "x": show(x), "CC": show(cc),
        "scaled_observed_odds": show(obs_odds),
        "limit_function_at_x": show(reference),
    }


def depths_near(r, targets, maximum):
    delta = -dec(lmbda(r)).ln()
    ns = {max(1, round(Decimal(target) / delta)) for target in targets}
    return tuple(sorted(n for n in ns if n <= maximum))


def schedule():
    curves = {}
    for ss, r_texts in R_BY_S.items():
        for rr in r_texts:
            curves[Fraction(ss), Fraction(rr)] = set(DEPTHS) | set(EXTRA_DEPTHS.get((ss, rr), ()))
    collapse = {}
    for rr in R_BY_S["0.50"]:
        r = Fraction(rr)
        collapse[r] = depths_near(r, ("0.25", "0.5", "0.75", "1", "1.5", "2", "3", "4"), 145)
        curves[HALF, r].update(collapse[r])
    wedge = {}
    for v in (Fraction(49, 50), Fraction(99, 100)):
        r = 16 * v**2 / (1 + 16 * v**2)
        for b, a in ((-HALF, v), (HALF, 1 / v)):
            s = a / (1 + a)
            wedge[b, v] = (s, r, depths_near(r, ("0.5", "1", "1.5"), 95))
    tasks = {(s, r, n) for (s, r), ns in curves.items() for n in ns}
    tasks.update((s, r, n) for s, r, ns in wedge.values() for n in ns)
    tasks.update((Fraction(s), Fraction(r), n) for s, r, n in ANCHORS)
    for s in (Fraction("0.45"), HALF, Fraction("0.52"), Fraction("0.55")):
        tasks.update((s, critical(s), n) for n in (12, 32, 64))
    return curves, collapse, wedge, sorted(tasks)


def exact_witness(s, r, n):
    states, rows = game_rows_exact(n, n, profile(s, r), 0, 0, "L", True)
    order = dissection(states, set(range(len(states))))
    mass = stationary(rows, order, zero=Fraction(0), one=Fraction(1))
    return sum(w for (_, y), w in zip(states, mass) if y < n)


def rectangles(values):
    result = []
    with localcontext() as ctx:
        ctx.prec = 94
        for ss, rr, n in ANCHORS:
            s, r = Fraction(ss), Fraction(rr)
            lower = exact_witness(s, r, n)
            assert lower > Fraction(4, 5)
            lo, hi = values[s, r, n][3]
            assert lo <= lower <= hi
            assert show(dec(lower)) == show(values[s, r, n][0])
            upper_s = HALF if s < HALF else maximum_s(r)
            upper_r = critical(s)
            upper = n1_masses(profile(upper_s, upper_r))[0]
            assert upper < Fraction(3, 8)
            result.append({
                "S_lower": str(s), "R_lower": str(r), "S_upper": str(upper_s),
                "R_upper": "critical(S)", "upper_corner_for_depth_one": {
                    "S": str(upper_s), "R": str(upper_r)},
                "witness_depth": n, "CC_at_lower_corner_exact": str(lower),
                "CC_at_lower_corner": show(dec(lower)), "depth_one_uniform_upper_exact": str(upper),
            })
        # An algebraically independent integer determinant of the whole quotient.
        s, r = Fraction("0.48"), Fraction("0.94")
        det = exact_grid(6, profile(s, r))
        lo, hi = values[s, r, 6][3]
        assert lo <= det <= hi
        assert show(dec(det)) == show(values[s, r, 6][0])
    return result, {"S": str(s), "R": str(r), "n": 6, "CC_exact": str(det)}


def make_data(workers):
    curves, collapse, wedge, tasks = schedule()
    if workers == 1:
        values = dict(map(solve, tasks))
    else:
        with ProcessPoolExecutor(max_workers=workers) as pool:
            values = dict(pool.map(solve, tasks, chunksize=1))
    witnesses, determinant = rectangles(values)
    series = []
    for (s, r), ns in curves.items():
        assert r < critical(s)
        row = {
            "S": show(dec(s)), "R": show(dec(r)), "critical_R_exact": str(critical(s)),
            "effective_exponential_base_exact": str(lmbda(r) * max(1, s / (1 - s))),
            "CC_limit": 0,
            "points": [{"n": n, "CC": show(values[s, r, n][0])} for n in sorted(ns)],
        }
        series.append(row)
    fair_curves = []
    for r, ns in collapse.items():
        fair_curves.append({
            "R": show(dec(r)), "delta": show(-dec(lmbda(r)).ln()),
            "points": [scaled(r, n, values[HALF, r, n], Decimal(0)) for n in ns],
        })
    critical_series = []
    for s in (Fraction("0.45"), HALF, Fraction("0.52"), Fraction("0.55")):
        r = critical(s)
        cc_limit = None
        if s == HALF:
            cc_limit = "1"
        if s > HALF:
            cc_limit = str(K(r, s) / (K(r, s) + s / (1 - s) - 1))
        critical_series.append({
            "S": show(dec(s)), "R_exact": str(r), "CC_limit_exact": cc_limit,
            "limit_status": "bounded odds; exact limit unresolved" if cc_limit is None else "proved",
            "points": [{"n": n, "CC": show(values[s, r, n][0])} for n in (12, 32, 64)],
        })
    cross_curves = []
    for (b, v), (s, r, ns) in wedge.items():
        cross_curves.append({
            "b_exact": str(b), "v_exact": str(v), "S_exact": str(s), "R_exact": str(r),
            "delta": show(-dec(lmbda(r)).ln()),
            "points": [scaled(r, n, values[s, r, n], dec(b)) for n in ns],
        })
    reference = []
    for i in range(101):
        x = Decimal(i) / 20
        reference.append({"x": str(x), "limit_function": show(x * (-x).exp())})
    return {
        "game": {"P": "4/5", "T": "4/5", "architecture": "L", "feedback": "independent"},
        "numerics": {
            "method": "Subtraction-free GTH on the exchange quotient, exact rational Poisson-residual tests",
            "certified_significant_digits_per_CC": DIGITS,
            "distinct_stationary_solves": len(values),
            "largest_working_decimal_precision": max(v[2] for v in values.values()),
            "scaled_columns": "Derived from certified masses using 94-digit Decimal arithmetic.",
        },
        "open_regions": witnesses, "independent_determinant": determinant,
        "robustness_curves": series, "critical_curves": critical_series,
        "fair_master_collapse": {
            "scaling": "x=delta*n, ordinate=delta*stationary_odds/K_c, K_c=102/125",
            "stationary_curves": fair_curves, "analytic_reference_only": reference,
        },
        "two_parameter_crossover": {
            "scaling": "b=log(S/(1-S))/delta, lambda=v^2, K_c=102/125",
            "stationary_curves": cross_curves,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=1, help="independent finite-chain solves in parallel")
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    with localcontext() as ctx:
        ctx.prec = 94
        data = make_data(args.workers)
    OUTPUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Wrote {data['numerics']['distinct_stationary_solves']} certified solves to {OUTPUT}")
