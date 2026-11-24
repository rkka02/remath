"""Reproduce the constant-hare Stag Hunt reversal and the original StagHunt-2.

The small-depth formulas and independent integer-grid certificate use only
rational arithmetic. The larger curves use the subtraction-free decimal solver.
Run with --extended for the far tail or --certificates-only for the exact checks.
"""

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import combinations_with_replacement
from math import lcm, prod

from phase1_chain import dissection, game_rows, solve_game


CASES = {
    "simple": (".9375", ".8", ".8", ".5"),
    "high": (".94", ".8", ".8", ".5"),
    "biased": (".94", ".8", ".8", ".45"),
    "original": (".95", ".8", ".85", ".45"),
}


def outcomes(p, r, k=0):
    """WW, WL, LW, LL. Only equal marginals can have nonzero correlation here."""
    if k and p != r:
        raise ValueError("Mixed-profile outcomes are independent.")
    covariance = k * p * (1 - p)
    return (p*r + covariance, p*(1-r) - covariance,
            (1-p)*r - covariance, (1-p)*(1-r) + covariance)


def n1_masses(game, k_r=0, k_p=0):
    """Three tree polynomials for (CC, either mixed action, DD)."""
    r, p, t, s = map(Fraction, game)
    _, b, _, c = outcomes(r, r, Fraction(k_r))
    _, e, _, d = outcomes(p, p, Fraction(k_p))
    _, x, y, _ = outcomes(s, t)
    weights = (x*d + 2*x*e + y*d,
               4*b*e + 2*b*d + 2*c*e,
               c*y + c*x + 2*b*y)
    return tuple(w / sum(weights) for w in weights)


def integer_determinant(rows):
    """Fraction-free Bareiss determinant, with row pivoting."""
    a = [row[:] for row in rows]
    size = len(a)
    sign, previous = 1, 1
    for k in range(size - 1):
        if not a[k][k]:
            pivot_row = next((i for i in range(k + 1, size) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        pivot_tail = a[k][k + 1:]
        for i in range(k + 1, size):
            row, lead = a[i], a[i][k]
            if lead:
                row[k + 1:] = [(x * pivot - lead * y) // previous
                               for x, y in zip(row[k + 1:], pivot_tail)]
            elif pivot != previous:
                row[k + 1:] = [x * pivot // previous for x in row[k + 1:]]
            row[k] = 0
        previous = pivot
    return sign * a[-1][-1]


def rational_determinant(rows):
    denominators = [lcm(*(x.denominator for x in row)) for row in rows]
    integers = [[int(x * d) for x in row] for row, d in zip(rows, denominators)]
    return Fraction(integer_determinant(integers), prod(denominators))


def n2_masses(game, k_r=0, k_p=0):
    """Seven-state trace formula after eliminating three double-deep states."""
    r, p, t, s = map(Fraction, game)
    a, b, _, c = outcomes(r, r, Fraction(k_r))
    d, e, _, f = outcomes(p, p, Fraction(k_p))
    u, v, w, z = outcomes(s, t)
    # Order: CC00, CC01, CD00, CD10, CD01, DD00, DD01. Depth 0 is shallow.
    raw = [[0, 0, 0, 2*b, 0, c, 0],
           [0, b, c, b, 0, 0, 0],
           [0, v, z, 0, 0, 0, w],
           [z, v, 0, 0, w, 0, 0],
           [0, 0, 0, v, 0, z, w],
           [f, 0, 0, 0, 2*e, 0, 0],
           [0, 0, f, 0, e, 0, e]]
    deep_c = (c, 2*b, 0, 0, 0, 0, 0)
    deep_m = (0, 0, z, v, w, 0, 0)
    deep_d = (0, 0, 0, 0, 0, f, 2*e)
    erased = (a, a, u, u, u, d, d)
    deep_exits = (deep_c, deep_c, deep_m, deep_m, deep_m, deep_d, deep_d)
    trace = [[raw[i][j] + h * exits[j] / (1-h) for j in range(7)]
             for i, (h, exits) in enumerate(zip(erased, deep_exits))]
    assert all(sum(row) == 1 for row in trace)
    weights = []
    for i, h in enumerate(erased):
        keep = [k for k in range(7) if k != i]
        minor = [[int(j == k) - trace[j][k] for k in keep] for j in keep]
        weights.append(rational_determinant(minor) / (1-h))
    grouped = [sum(weights[:2]), sum(weights[2:5]), sum(weights[5:])]
    return tuple(w / sum(grouped) for w in grouped)


def exact_grid(n, game, k_r=0, k_p=0):
    """Independent integer determinant ratio on unordered pairs of full levels."""
    r, p, t, s = map(Fraction, game)
    table = (outcomes(r,r,Fraction(k_r)), outcomes(s,t), outcomes(p,p,Fraction(k_p)))
    denominator = lcm(*(z.denominator for row in table for z in row))
    weights = [[int(z * denominator) for z in row] for row in table]
    states = list(combinations_with_replacement(range(2*n), 2))
    indices = {point: k for k, point in enumerate(states)}
    matrix = [[0] * len(states) for _ in states]

    def step(x, win):
        direction = (1 if x >= n else -1) * (1 if win else -1)
        return min(2*n - 1, max(0, x + direction))

    for k, (x, y) in enumerate(states):
        profile = int(x >= n) + int(y >= n)
        for prob, (first, second) in zip(weights[profile],
                                          ((1,1), (1,0), (0,1), (0,0))):
            other = indices[tuple(sorted((step(x, first), step(y, second))))]
            if k != other:
                matrix[k][k] += prob
                matrix[other][k] -= prob
    matrix[-1] = [1] * len(states)
    den = integer_determinant(matrix)
    matrix[-1] = [int(y < n) for _, y in states]
    return Fraction(integer_determinant(matrix), den)


def decimal_value(fraction):
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)


def labeled_kernel(n, game):
    """Integer kernel and common denominator for two independently updated players."""
    r, p, t, s = map(Fraction, game)
    table = (outcomes(r,r), outcomes(s,t), outcomes(t,s), outcomes(p,p))
    scale = lcm(*(z.denominator for row in table for z in row))
    m = 2*n
    size = m*m
    kernel = [[0]*size for _ in range(size)]
    for i in range(size):
        x, y = divmod(i, m)
        left, right = (1 if x >= n else -1), (1 if y >= n else -1)
        for prob, (sx, sy) in zip(table[2*int(x >= n) + int(y >= n)],
                                   ((1,1), (1,-1), (-1,1), (-1,-1))):
            a = max(0, min(m-1, x + left*sx))
            b = max(0, min(m-1, y + right*sy))
            kernel[i][a*m + b] += int(prob * scale)
    return kernel, scale


def exact_small_mixing(n, game):
    """Worst-state TV mixing time at 1/4 from unrounded integer powers."""
    if n not in (1, 2):
        raise ValueError("The unrounded powers are intended for depth 1 or 2.")
    kernel, scale = labeled_kernel(n, game)
    size = len(kernel)
    tree_weights = []
    for k in range(size):
        keep = [i for i in range(size) if i != k]
        tree_weights.append(integer_determinant(
            [[scale*int(i == j) - kernel[i][j] for j in keep] for i in keep]))
    total = sum(tree_weights)
    transitions = [[(j,w) for j,w in enumerate(row) if w] for row in kernel]
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    denominator, elapsed = 1, 0
    while any(2*sum(abs(x*total - denominator*w) for x,w in zip(row, tree_weights))
              > denominator*total for row in power):
        following = [[0]*size for _ in range(size)]
        for i, row in enumerate(power):
            for k, x in enumerate(row):
                if x:
                    for j, weight in transitions[k]:
                        following[i][j] += x*weight
        power = following
        denominator *= scale
        elapsed += 1
    return elapsed


def enclosed_mixing(n, game, digits=70):
    """Certify the exact mixing time by rounding matrix products downward."""
    import numpy as np

    kernel, denominator = labeled_kernel(n, game)
    unit = 10**digits
    powers = [np.array(kernel, dtype=object) * unit // denominator]
    while True:
        stationary_lower = powers[-1].min(axis=0)
        stationary_gap = unit - sum(stationary_lower)
        if stationary_gap <= 10**(digits//2):
            break
        powers.append(powers[-1] @ powers[-1] // unit)
        if unit - min(powers[-1].sum(axis=1)) > 10**(digits//2):
            raise ArithmeticError("Increase precision to enclose the stationary law.")

    def above_threshold(matrix):
        distance = abs(matrix - stationary_lower).sum(axis=1)
        error = stationary_gap + unit - matrix.sum(axis=1)
        if 2*max(distance - error) > unit:
            return True
        if 2*max(distance + error) <= unit:
            return False
        raise ArithmeticError("Increase precision to separate the mixing threshold.")

    elapsed = 0
    accumulated = np.eye(len(kernel),dtype=object)*unit
    for k in reversed(range(len(powers))):
        candidate = accumulated @ powers[k] // unit if elapsed else powers[k]
        if above_threshold(candidate):
            elapsed += 2**k
            accumulated = candidate
    assert not above_threshold(accumulated @ powers[0] // unit)
    return elapsed + 1


def corner_passages(n, game, digits=76):
    """Mean deep DD→deep CC and deep CC→deep DD times by positive elimination."""
    with localcontext() as ctx:
        ctx.prec = digits
        states, rows = game_rows(n, n, game, 0, 0, "L", True)
        w, z = states.index((0,0)), states.index((2*n-1,2*n-1))
        order = dissection(states, set(range(len(states))).difference((w,z)))
        incoming = [set() for _ in rows]
        for i, row in enumerate(rows):
            for j in row:
                incoming[j].add(i)
        holding = [Decimal(1)] * len(states)
        for k in order:
            rate = sum(rows[k].values())
            exit_law = [(j, x/rate) for j,x in rows[k].items()]
            for j,_ in exit_law:
                incoming[j].remove(k)
            for i in incoming[k]:
                edges = rows[i]
                incoming_weight = edges.pop(k)
                holding[i] += incoming_weight * holding[k] / rate
                for j, conditional in exit_law:
                    if i != j:
                        if j not in edges:
                            incoming[j].add(i)
                        edges[j] = edges.get(j,0) + incoming_weight * conditional
            rows[k].clear()
            incoming[k].clear()
        return holding[z]/rows[z][w], holding[w]/rows[w][z]


def passage_constants(n, game):
    """Exact finite reference fluxes used in the two leading equivalents."""
    r,p,_,s = map(Decimal, game)
    rp, rr = (1-p)/p, (1-r)/r
    geometric = sum((s/(1-s))**j for j in range(n))
    normalizer = sum(rp**j for j in range(n)) + p*rp**n*geometric/(1-s)
    f = p*rp**n/normalizer
    entrance = f*f*(2*geometric/(1-s)-1)
    mark = (2*r-1)*rr**n/(1-rr**n)
    marked_flux = mark*(2-mark)
    theta = (1-rr)*(1-rp)/(1-rr*rp)
    return theta*entrance, theta*marked_flux


def check_certificates():
    for name, game in CASES.items():
        for n, small in ((1, n1_masses), (2, n2_masses)):
            for kr, kp in ((0,0), (".2","-.1")):
                masses = small(game, kr, kp)
                assert all(m >= 0 for m in masses) and sum(masses) == 1
                assert masses[0] == exact_grid(n, game, kr, kp)
                full = solve_game(n, n, game, kr, kp, digits=78)
                grouped = (full[0], full[1] + full[2], full[3])
                assert max(abs(decimal_value(x) - y) for x,y in zip(masses, grouped)) < Decimal("1e-74")
                if kr == kp == 0:
                    print(f"{name} n={n} exact CC = {masses[0]}")
    for name, n, threshold in (("simple",10,Fraction(4,5)),
                                ("high",6,Fraction(4,5)),
                                ("biased",6,Fraction(7,10))):
        cc = exact_grid(n, CASES[name])
        assert cc > threshold
        assert abs(decimal_value(cc) - solve_game(n,n,CASES[name],digits=78)[0]) < Decimal("1e-74")
        print(f"{name} n={n} exact determinant certifies CC > {threshold}")
    for n in (1,2):
        elapsed = exact_small_mixing(n, CASES["simple"])
        print(f"simple n={n} exact worst-start TV mixing time at 1/4 = {elapsed}")
    r,p,t,s = map(Decimal, CASES["simple"])
    a, b, c, d, e, f = 2*r*(1-r), (1-r)**2, s*(1-t), (1-s)*t, (1-p)**2, 2*p*(1-p)
    # Solve the 3-action first-passage equations separately at n=1.
    dd_to_cc = (c+d+f)/(e*(c+d)+f*c)
    cc_to_dd = (c+d+a)/(b*(c+d)+a*d)
    obtained = corner_passages(1, CASES["simple"])
    assert max(abs(x/y - 1) for x,y in zip(obtained,(dd_to_cc,cc_to_dd))) < Decimal("1e-73")


def collect(extended):
    depths = {"simple": [1,2,4,6,10,15,16,17,40,64],
              "high": [1,6,12,20,40,64],
              "biased": [1,6,12,30,60],
              "original": [1,2,6,12,16,22,40]}
    if extended:
        depths["simple"].extend((100,128,160))
        depths["high"].extend((100,140))
    for name, ns in depths.items():
        print(f"\n{name}, (R,P,T,S)={CASES[name]}", flush=True)
        for n in ns:
            cc, cd, dc, dd = solve_game(n, n, CASES[name], digits=76)
            print(f"  n={n:3d}  {cc}", flush=True)
            if name == "simple" and n in (1,16):
                r,p,t,s = map(Decimal, CASES[name])
                welfare = r*cc + (s+t)*(cd+dc)/2 + p*dd
                print(f"         mean individual success {welfare}", flush=True)

    print("\nStationary odds divided by G_n lambda^n", flush=True)
    for game in ((".9",".75",".75",".45"), (".9",".75",".75",".5"),
                 (".85",".75",".75",".6")):
        r,p,_,s = map(Decimal, game)
        base = ((1-p)/p)**2*r/(1-r)
        for n in ((10,20,40,64) if extended else (10,20,40)):
            cc = solve_game(n, n, game, digits=76)[0]
            geometric = sum((s/(1-s))**k for k in range(n))
            scaled = cc / ((1-cc)*geometric*base**n)
            print(f"  game={game} n={n:2d}  {scaled}", flush=True)
    print("\nCorner passage times times their predicted rates; both limits equal one.", flush=True)
    for game in (CASES["simple"], (".85",".75",".75",".6")):
        for n in ((10,20,40,64) if extended else (10,20,40)):
            times = corner_passages(n, game)
            rates = passage_constants(n, game)
            print(f"  game={game} n={n:2d}  {times[0]*rates[0]}  {times[1]*rates[1]}", flush=True)
    print("\nCertified worst-start mixing times at 1/4 (integer lower bounds on matrix powers).")
    for n in range(1, 7 if extended else 5):
        rounds = enclosed_mixing(n, CASES["simple"])
        if n in (1,2):
            assert rounds == exact_small_mixing(n, CASES["simple"])
        print(f"  simple n={n}  {rounds} rounds", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificates-only", action="store_true")
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()
    with localcontext() as ctx:
        ctx.prec = 84
        check_certificates()
        if not args.certificates_only:
            collect(args.extended)
