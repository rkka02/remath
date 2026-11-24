"""Unequal-memory stationary checks. Run directly with standard Python 3.

The frozen-opponent calculations use exact fractions. The finite paired
chains use Decimal GTH elimination. --certify also provides rigorous rational
payoff bounds by checking a Poisson inequality at every recurrent state.
"""

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction

from phase1_chain import closed_classes, dissection, game_rows, game_rows_exact, solve_game


ORIGINAL = (".8", ".6", ".9", ".2")
STRONG_TEMPTATION = (".55", ".40", ".99", ".39")
CHICKEN = (".70", ".20", ".71", ".23")
LOCAL_PD = (".52", ".45", ".999", ".44")


def half_mass(win, depth):
    """Unnormalized mass of an action in the ordinary two-action L chain."""
    odds = win / (1 - win)
    series = depth if odds == 1 else (odds**depth - 1) / (odds - 1)
    return series / (1 - win)


def frozen_cooperation(win_c, win_d, depth):
    c = half_mass(win_c, depth)
    return c / (c + half_mass(win_d, depth))


def frozen_means(game, depth):
    r, p, t, s = map(Fraction, game)
    facing_c = frozen_cooperation(r, t, depth)
    facing_d = frozen_cooperation(s, p, depth)
    return s + (r - s) * facing_c, p + (t - p) * facing_d


def payoff(mass, game):
    r, p, t, s = map(Decimal, game)
    return sum(w * a for w, a in zip(mass, (r, s, t, p)))


def local_nash_margin(n=40, horizon=15):
    """Exact lower bound on (W1+W2-2R)/Pr(mixed) for depths n+1, n."""
    r, p, t, s = map(Fraction, LOCAL_PD)
    if n < horizon:
        raise ValueError("The short cap must accommodate the truncated walk.")
    alive = [Fraction(1)]
    mean_mixed = Fraction(0)
    for step in range(horizon):
        mean_mixed += sum(alive) - step * (1 - t)
        following = [Fraction(0)] * (len(alive) + 1)
        for depth, mass in enumerate(alive):
            following[depth + 1] += s * mass
            if depth:
                following[depth - 1] += (1 - s) * mass
        alive = following
    c = 1 - (1 - r) / r
    a = ((1 - r) / r)**n
    b = (p / (1 - p))**(n - 1)
    good = max(1 + b / c, a / c)
    dd_over_mixed = (good / mean_mixed + (1 - s)*(1 - t) / c) / (1 - 2*p)
    return mean_mixed, t + s - 2*r - 2*(r - p)*dd_over_mixed


def check_spectral_example():
    """Exact brackets for the two Perron roots when the opponent has depth one."""
    r, p, t, s = map(Fraction, (".70", ".60", ".80", ".55"))
    cases = ((r, s, r, t, "1.5340660", "1.5340661"),
             (t, p, s, p, "2.2361037", "2.2361038"))
    for tagged_c, tagged_d, peer_c, peer_d, low, high in cases:
        for z, expected_sign in ((Fraction(low), 1), (Fraction(high), -1)):
            x = tagged_c/z + (1 - tagged_c)*z
            y = tagged_d/z + (1 - tagged_d)*z
            # The smaller eigenvalue is below each diagonal entry.
            assert min(x*peer_c, y*peer_d) < 1
            determinant = 1 - x*peer_c - y*peer_d + x*y*(peer_c + peer_d - 1)
            assert expected_sign * determinant > 0
    assert frozen_means((r, p, t, s), 1)[1] == Fraction(59, 85)


def rational_payoff_bounds(m, n, game, corr, digits, measure="W1"):
    """Check the Collatz-type Poisson bounds exactly, using a numerical bias.

    For any vector g, stationarity puts the mean reward between the minimum
    and maximum of r_i + sum_j P_ij (g_j-g_i). GTH elimination below constructs
    g, but the separate final rational evaluation alone proves the result.
    """
    with localcontext() as context:
        context.prec = digits
        states, rows = game_rows(m, n, game, corr, corr, "L", False)
        _, raw_exact_rows = game_rows_exact(m, n, game, corr, corr, "L", False)
        classes = closed_classes(rows)
        if len(classes) != 1:
            raise ValueError("A single recurrent class is needed.")
        active = classes[0]
        order = dissection(states, active)
        exact_rows = {i: raw_exact_rows[i] for i in order}
        r_f, p_f, t_f, s_f = (Fraction(str(x)) for x in game)
        exact_marks = (Fraction(1), Fraction(0), Fraction(0), Fraction(0)) if measure == "CC" else (r_f, s_f, t_f, p_f)
        exact_reward = [exact_marks[2 * (i >= m) + (j >= n)] for i, j in states]
        r, p, t, s = (Decimal(x.numerator) / Decimal(x.denominator) for x in (r_f, p_f, t_f, s_f))
        marks = (Decimal(1), Decimal(0), Decimal(0), Decimal(0)) if measure == "CC" else (r, s, t, p)
        reward = [marks[2 * (i >= m) + (j >= n)] for i, j in states]
        mass = solve_game(m, n, game, corr, corr, digits=digits)
        estimate = sum(w * mark for w, mark in zip(mass, marks))
        rhs = [w - estimate for w in reward]
        incoming = [set() for _ in states]
        for i in order:
            for j in rows[i]:
                incoming[j].add(i)
        records = []
        for k in order[:-1]:
            row = rows[k]
            total = sum(row.values())
            outgoing = [(j, w / total) for j, w in row.items()]
            offset = rhs[k] / total
            for j, _ in outgoing:
                incoming[j].remove(k)
            for i in incoming[k]:
                scaled = rows[i].pop(k)
                rhs[i] += scaled * offset
                for j, prob in outgoing:
                    if i != j:
                        rows[i][j] = rows[i].get(j, 0) + scaled * prob
                        incoming[j].add(i)
            records.append((k, offset, outgoing))
        bias = [Decimal(0)] * len(states)
        for k, offset, outgoing in reversed(records):
            bias[k] = offset + sum(w * bias[j] for j, w in outgoing)
        g = list(map(Fraction, bias))
        adjusted = [exact_reward[i] + sum(
            w * (g[j] - g[i]) for j, w in exact_rows[i].items()
        ) for i in order]
        return min(adjusted), max(adjusted)


def show_cases(digits):
    print("Independent-feedback baseline, fixed n2=10")
    print(" n1        CC                 DD                 W1")
    grid = []
    for m in range(4, 35):
        mass = solve_game(m, 10, ORIGINAL, digits=digits)
        w = payoff(mass, ORIGINAL)
        grid.append((m, mass[0], w))
        print(f"{m:3d}  {mass[0]:.15f}  {mass[3]:.15f}  {w:.15f}")
    assert max(grid, key=lambda row: row[1])[0] == 11
    assert max(grid, key=lambda row: row[2])[0] == 11
    print("Frozen means at n2=10", *frozen_means(ORIGINAL, 10))
    print("Common shocks at homogeneous profiles, independent shocks while mixed")
    print("Game             n     W1(n,n)         W1(n+1,n)       CC(n+1,n)")
    for name, game in (("Strict PD", STRONG_TEMPTATION), ("Chicken", CHICKEN)):
        for n in (6, 10, 20, 40):
            a = solve_game(n, n, game, "1", "1", digits=digits)
            b = solve_game(n + 1, n, game, "1", "1", digits=digits)
            print(f"{name:13} {n:3d}   {payoff(a, game):.13f}   "
                  f"{payoff(b, game):.13f}   {b[0]:.13f}")
    print("Linear public good, N=3, b=.45, h=.25, frozen follower frequencies")
    b, h = Fraction(".45"), Fraction(".25")
    for d in map(Fraction, (".07", ".125", ".16")):
        for n in (10, 50, 150):
            c = frozen_cooperation(b + h, b + d + h/2, n)
            d_response = frozen_cooperation(b + h/2, b + d, n)
            print(f"  d={str(d):6} n={n:3d}  {float(c):.12g}  {float(d_response):.12g}")
    length, margin = local_nash_margin()
    assert length > Fraction("4.092") and margin > Fraction(".0449")
    print("Certified at all n >= 40: mean mixed block > 4.092, "
          "(W1+W2-2R)/Pr(mixed) > .0449")
    check_spectral_example()
    print("Certified frozen Perron intervals (1.5340660,1.5340661), "
          "(2.2361037,2.2361038), limiting tagged payoff 59/85")


def certify_cases(digits):
    targets = (("W1", 10, 10, ORIGINAL, "0", ".743962571531403", ".743962571531405"),
               ("W1", 11, 10, ORIGINAL, "0", ".746391275680355", ".746391275680358"),
               ("CC", 10, 10, ORIGINAL, "0", ".720608517331597", ".720608517331599"),
               ("CC", 11, 10, ORIGINAL, "0", ".731673697006677", ".731673697006679"),
               ("W1", 40, 40, STRONG_TEMPTATION, "1", ".5499755023", ".5499755025"),
               ("W1", 41, 40, STRONG_TEMPTATION, "1", ".6704057221", ".6704057224"),
               ("W1", 10, 10, CHICKEN, "1", ".6999303146", ".6999303149"),
               ("W1", 11, 10, CHICKEN, "1", ".6979957708", ".6979957711"))
    for measure, m, n, game, corr, low, high in targets:
        lo, hi = rational_payoff_bounds(m, n, game, corr, digits, measure)
        if not Fraction(low) < lo <= hi < Fraction(high):
            raise ArithmeticError(f"Expected certificate failed at ({m},{n})")
        print(f"Certified {measure}({m},{n}) in ({low}, {high}) for {game}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--digits", type=int, default=75)
    parser.add_argument("--certify", action="store_true")
    args = parser.parse_args()
    with localcontext() as ctx:
        ctx.prec = args.digits
        show_cases(args.digits)
        if args.certify:
            certify_cases(args.digits)
