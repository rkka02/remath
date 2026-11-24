"""Transfer-kernel checks for the linear two-automaton game.

Run with a Python installation containing mpmath and SciPy.  The phase-sign certificate
uses only integer/rational arithmetic.  No stationary fit enters the result.
"""

from fractions import Fraction as F
from itertools import product

import mpmath as mp


def bisect_zero(function, left, right):
    """Bisect a continuous sign change at the current working precision."""
    fleft, fright = function(left), function(right)
    if fleft == 0:
        return left
    if fright == 0:
        return right
    assert fleft * fright < 0
    for _ in range(mp.mp.prec + 4):
        mid = (left + right) / 2
        fmid = function(mid)
        if fmid == 0 or mid in (left, right):
            return mid
        if fmid * fleft > 0:
            left, fleft = mid, fmid
        else:
            right = mid
    return (left + right) / 2


def coefficients(p, kappa):
    q = 1 - p
    return p * p + kappa * p * q, (1 - kappa) * p * q, q * q + kappa * p * q


def dd_moments(ww, off, ll, u, z):
    """DD transform and its two logarithmic derivatives."""
    both_up, both_down = ll * u * z, ww / (u * z)
    long_up, short_up = off * u / z, off * z / u
    return (both_up + both_down + long_up + short_up,
            both_up - both_down + long_up - short_up,
            both_up - both_down - long_up + short_up)


def mixed_moments(temptation, sucker, u, z):
    """Short cooperator, long defector. Increments point towards cooperation."""
    xu, xd = (1 - temptation) * u, temptation / u
    yu, yd = sucker * z, (1 - sucker) / z
    return (xu + xd) * (yu + yd), (xu - xd) * (yu + yd), (xu + xd) * (yu - yd)


def weak_edge_transform(z, switch):
    return 1 - switch + switch**2 * z / (1 - (1 - switch) * z)


def high_correlation(p, temptation, sucker, kappa, gamma, switch=1):
    """Evaluate the L or randomized-boundary interface, including perfect synchrony."""
    ww, off, ll = coefficients(p, kappa)
    odds = p / (1 - p)
    assert kappa > mp.mpf(".5") and gamma * (2 * kappa - 1) > 1
    temptation_odds = temptation / (1 - temptation)

    def mixed_root(x, clock=1):
        m = clock * ((1 - temptation) * x + temptation / x)
        discriminant = 1 - 4 * m**2 * sucker * (1 - sucker)
        return 2 * m * (1 - sucker) / (1 + mp.sqrt(max(mp.mpf(0), discriminant)))

    if kappa == 1:
        def upper_z(x):
            return odds / x

        ub = None
        search_end = temptation_odds
    else:
        # The rightmost point of {M_D <= 1} has 4 A_D B_D = 1.
        delta = mp.mpf(".25") - ww * ll - off * off
        umax = mp.sqrt((delta + mp.sqrt(delta**2 - 4 * ww * ll * off**2))
                       / (2 * off * ll))

        def upper_z(x):
            a, b = ll * x + off / x, off * x + ww / x
            return (1 + mp.sqrt(max(mp.mpf(0), 1 - 4 * a * b))) / (2 * a)

        def bulk_normal(x):
            _, vx, vy = dd_moments(ww, off, ll, x, upper_z(x))
            return gamma * vy - vx

        ub = bisect_zero(bulk_normal, odds, umax)
        zb = upper_z(ub)
        search_end = min(ub, temptation_odds)

    def gap(x):
        return upper_z(x) - weak_edge_transform(mixed_root(x), switch)

    active = ub is None or ub > temptation_odds or gap(search_end) < 0
    u = bisect_zero(gap, odds, search_end) if active else ub
    z = upper_z(u)

    answer = {
        "long tilt": mp.log(u),
        "short tilt": mp.log(z),
        "full DD exponent": gamma * mp.log(u) + mp.log(z),
        "stationary DD exceedance exponent": gamma * mp.log(odds),
    }
    if ub is not None:
        answer["frozen DD endpoint exponent"] = gamma * mp.log(ub) + mp.log(zb)
    if active:
        _, dx, dy = dd_moments(ww, off, ll, u, z)
        _, cx, cy = mixed_moments(temptation, sucker, u, mixed_root(u))
        assert dy > 0 > cy
        answer["onset of recrossing (memory ratio)"] = dx / dy
        answer["long drift while in mixed profile (tilted)"] = cx
        def first_return(s, clock):
            x = mp.exp(s)
            dd_up, dd_down = clock * (ll * x + off / x), clock * (off * x + ww / x)
            from_dd = 2 * dd_up / (1 + mp.sqrt(1 - 4 * dd_up * dd_down))
            from_c = weak_edge_transform(mixed_root(x, clock), switch)
            return dd_down * from_dd + dd_up * from_c

        slong = mp.log(u)
        advance = mp.diff(lambda s: first_return(s, 1), slong)
        duration = mp.diff(lambda clock: first_return(slong, clock), 1)
        answer["long drift along interface (tilted)"] = advance / duration
        answer["interface first-return transform"] = first_return(slong, 1)
        if switch == 1:
            assert mp.almosteq(advance / duration, (dy * cx - cy * dx) / (dy - cy))
        assert mp.almosteq(answer["interface first-return transform"], 1)
        assert answer["long drift along interface (tilted)"] > 0
    return answer


def exact_phase_certificate():
    """Isolate the interface root and compare all phase odds over Q."""
    p, temptation, sucker, kappa = map(F, (".51", ".55", ".2", ".997"))
    ww, off, ll = coefficients(p, kappa)

    def dd(u, z):
        return dd_moments(ww, off, ll, u, z)

    def mix(u, z):
        return mixed_moments(temptation, sucker, u, z)[0]

    ulo, uhi = F("1.04691"), F("1.04692")
    brackets = ((ulo, F(".99413914"), F(".99413916")),
                (uhi, F(".99412957"), F(".99412959")))
    for u, zlo, zhi in brackets:
        assert dd(u, zlo)[0] < 1 < dd(u, zhi)[0]
        assert dd(u, zlo)[2] > 0
    assert mix(ulo, brackets[0][1]) < 1
    assert mix(uhi, brackets[1][2]) > 1

    zlo, zhi = brackets[1][1], brackets[0][2]
    # On this small rectangle both normal components are positive, and
    # 2 M_y - M_x > 0.  Lower bound each positive term and upper bound
    # each negative term in ll*u*z - ww/(u*z) -3 off*u/z +3 off*z/u.
    base = ll * ulo * zlo - ww / (ulo * zlo)
    assert base - off * uhi / zlo - off * zhi / ulo > 0
    assert base - 3 * off * uhi / zlo + 3 * off * zlo / uhi > 0
    exponent_lo, exponent_hi = ulo**2 * zlo, uhi**2 * zhi
    low_reward_odds = F(5206, 4794)
    high_reward_odds = F(53, 47)
    assert (p / (1 - p))**2 < low_reward_odds < exponent_lo < exponent_hi < high_reward_odds
    # A rational feasible point of the frozen bulk kernel alone.
    uf, zf = F("1.30"), F(".787")
    assert dd(uf, zf)[0] < 1 and uf**2 * zf > high_reward_odds
    print("Exact phase-odds ordering verified with fractions.")
    print("exp(V) lies strictly between", exponent_lo, "and", exponent_hi)


def exact_tactic_certificate():
    """At identical positive joint probabilities B cooperates and L defects."""
    p, temptation, sucker, kappa = map(F, (".6", ".9", ".2", ".99"))
    ww, off, ll = coefficients(p, kappa)
    reward_odds = F(39, 11)

    def dd(u, z):
        return dd_moments(ww, off, ll, u, z)

    def mixed(u, z):
        return mixed_moments(temptation, sucker, u, z)[0]

    # A feasible L tilt with cost higher than logit R.
    ul, zl = F("2.5"), F(".58")
    assert dd(ul, zl)[0] < 1 and mixed(ul, zl) < 1 and ul**2 * zl > reward_odds
    # The B cutoff lies between the following longitudinal tilts.
    lo, hi = F("2.14"), F("2.15")
    for u, zlo, zhi in ((lo, F(".6898"), F(".6900")), (hi, F(".6864"), F(".6865"))):
        assert dd(u, zlo)[0] < 1 < dd(u, zhi)[0] and dd(u, zlo)[2] > 0
    assert mixed(lo, F(".5455")) < 1 and mixed(hi, F(".5444")) > 1
    assert F(".6898") > weak_edge_transform(F(".5455"), F(".5"))
    assert F(".6865") < weak_edge_transform(F(".5444"), F(".5"))
    # The DD boundary objective is still increasing at the upper endpoint.
    zlo, zhi = F(".6864"), F(".6865")
    assert ll * hi * zlo - ww / (hi * zlo) - 3 * off * hi / zlo + 3 * off * zlo / hi > 0
    assert hi**2 * F(".6900") < reward_odds
    print("Exact phase-odds ordering for L and B verified with fractions.")


def finite_system(n, gamma, p, temptation, sucker, kappa, switch):
    """Dirichlet matrix, forcing, and initial jump for first CC versus deep DD."""
    nlong = gamma * n
    origin = (0, 0)
    states = [(x, y) for x in range(2 * nlong) for y in range(2 * n)
              if (x, y) != origin and (x < nlong or y < n)]
    indices = {state: i for i, state in enumerate(states)}
    size = len(states)
    ww, off, ll = coefficients(p, kappa)
    dd = {(1, 1): ll, (-1, -1): ww, (1, -1): off, (-1, 1): off}
    weights = {}
    for dx, dy in product((-1, 1), repeat=2):
        weights[False, False, dx, dy] = dd[dx, dy]
        weights[True, False, dx, dy] = ((sucker if dx == 1 else 1 - sucker)
                                       * (1 - temptation if dy == 1 else temptation))
        weights[False, True, dx, dy] = ((1 - temptation if dx == 1 else temptation)
                                       * (sucker if dy == 1 else 1 - sucker))

    def updates(depth):
        result = {}
        for x in range(2 * depth):
            for dx in (-1, 1):
                nx = min(max(x + dx, 0), 2 * depth - 1)
                crosses = (x < depth) != (nx < depth)
                if crosses and switch != 1:
                    result[x, dx] = ((x, 1 - switch), (nx, switch))
                else:
                    result[x, dx] = ((nx, 1),)
        return result

    long_moves, short_moves = updates(nlong), updates(n)
    rows = list(range(size))
    cols = list(range(size))
    values = [1] * size
    rhs = [0] * size
    for i, (x, y) in enumerate(states):
        for dx, dy in dd:
            prob = weights[x >= nlong, y >= n, dx, dy]
            for nx, wx in long_moves[x, dx]:
                for ny, wy in short_moves[y, dy]:
                    mass = prob * wx * wy
                    if nx >= nlong and ny >= n:
                        rhs[i] += mass
                    elif (nx, ny) != origin:
                        rows.append(i)
                        cols.append(indices[nx, ny])
                        values.append(-mass)
    # Include the first step explicitly, including direct absorption at depth 1.
    direct, initial = 0, []
    for (dx, dy), prob in dd.items():
        for x, wx in long_moves[0, dx]:
            for y, wy in short_moves[0, dy]:
                if x >= nlong and y >= n:
                    direct += prob * wx * wy
                elif (x, y) != origin:
                    initial.append((indices[x, y], prob * wx * wy))
    return rows, cols, values, rhs, direct, initial


def finite_attempt(n, gamma, p, temptation, sucker, kappa, high_precision=False, switch=1):
    rows, cols, values, rhs, direct, initial = finite_system(n, gamma, p, temptation, sucker, kappa, switch)
    size = len(rhs)
    if high_precision:
        matrix = mp.matrix(size)
        for i, j, value in zip(rows, cols, values):
            matrix[i, j] += value
        committor = mp.lu_solve(matrix, mp.matrix(rhs))
    else:
        from scipy.sparse import coo_matrix
        from scipy.sparse.linalg import spsolve

        matrix = coo_matrix((values, (rows, cols)), shape=(size, size)).tocsc()
        committor = spsolve(matrix, rhs)
    return direct + sum(weight * committor[j] for j, weight in initial)


def certified_finite_attempt(n, gamma, p, temptation, sucker, kappa, switch):
    """Enclose the committor using integer residuals and a positive supersolution."""
    import math

    import numpy as np
    from scipy.sparse import coo_matrix
    from scipy.sparse.linalg import splu

    rows, cols, values, rhs, direct, initial = finite_system(n, gamma, p, temptation, sucker, kappa, switch)
    size = len(rhs)
    den = math.lcm(*(F(v).denominator for v in set(values + rhs + [direct] + [w for _, w in initial])))
    entries = [int(v * den) for v in values]
    forcing = [int(v * den) for v in rhs]
    matrix = coo_matrix((entries, (rows, cols)), shape=(size, size)).tocsc()
    lu = splu(matrix.astype(float))
    terms = [[] for _ in rhs]
    for i, j, v in zip(rows, cols, entries):
        terms[i].append((j, v))

    def multiply(integers):
        return [sum(v * integers[j] for j, v in row) for row in terms]

    # For A = I-Q, (den A) Y >= 1024 den certifies A^{-1}1 <= Y/1024.
    time_guess = lu.solve(np.full(size, float(den)))
    time_bound = [math.ceil(2048 * t) for t in time_guess]
    assert min(time_bound) >= 0 and min(multiply(time_bound)) >= 1024 * den
    scale = 10**115
    solution = [round(scale * v) for v in lu.solve(np.array(forcing, dtype=float))]
    for _ in range(12):
        residual = [f * scale - v for f, v in zip(forcing, multiply(solution))]
        max_residual = max(map(abs, residual))
        if max_residual < 5 * den:
            break
        correction = lu.solve(np.array(residual, dtype=float))
        solution = [old + round(c) for old, c in zip(solution, correction)]
    else:
        raise ArithmeticError("The integer residual did not reach its target")
    central = direct + sum(weight * F(solution[j], scale) for j, weight in initial)
    error = F(max_residual * max(time_bound), 1024 * den * scale)
    assert error < central * F(1, 10**80)
    return central - error, central + error


def check_finite_attempts(params, gamma, switch):
    from math import log

    mp_params = list(map(mp.mpf, params))
    float_params = list(map(float, params))
    target = high_correlation(*mp_params, gamma, switch=switch)["full DD exponent"]
    reference = finite_attempt(3, gamma, *mp_params, high_precision=True, switch=switch)
    smallest = finite_attempt(3, gamma, *float_params, switch=float(switch))
    assert abs(reference - smallest) < reference * mp.mpf("5e-13")
    print("\nIndependent finite-state first-CC committor, (P,T,S,kappa) =", params, "switch =", switch)
    print("  n = 3 at 80-digit working precision:", mp.nstr(reference, 65))
    print("  exact limiting slope:", mp.nstr(target, 65))
    prev_n, prev_cost = 3, -log(smallest)
    for n in (10, 16, 24, 36, 48, 64, 80):
        cost = -log(finite_attempt(n, gamma, *float_params, switch=float(switch)))
        slope = (cost - prev_cost) / (n - prev_n)
        print(f"  n = {prev_n:2d} to {n:2d}    slope {slope:.14f}")
        prev_n, prev_cost = n, cost
    assert abs(slope - float(target)) < 1e-9


def main():
    mp.mp.dps = 80
    exact_phase_certificate()
    exact_tactic_certificate()
    examples = (
        (".51", ".55", ".2", ".997", "2"),
        (".7", ".9", ".2", ".9", "4"),
        (".51", ".55", ".2", "1", "2"),
    )
    for params in examples:
        print("\n(P, T, S, kappa_D, gamma) =", params)
        for name, value in high_correlation(*map(mp.mpf, params)).items():
            print(f"  {name:46} {mp.nstr(value, 62)}")
    for kappa in (".99", "1"):
        for switch in (1, mp.mpf(".5")):
            params = list(map(mp.mpf, (".6", ".9", ".2", kappa, "2")))
            value = high_correlation(*params, switch=switch)["full DD exponent"]
            print(f"  (P,T,S)=(.6,.9,.2), gamma=2, kappa={kappa}, switch={switch}: {mp.nstr(value, 65)}")
    check_finite_attempts((".7", ".75", ".2", ".9"), 4, 1)
    check_finite_attempts((".6", ".9", ".2", ".99"), 2, mp.mpf(".5"))
    for switch in (F(1), F(1, 2)):
        lo, hi = certified_finite_attempt(40, 2, *map(F, (".6", ".9", ".2", ".99")), switch)
        with mp.workdps(110):
            lower, upper = (mp.mpf(v.numerator) / v.denominator for v in (lo, hi))
            assert mp.nstr(lower, 75) == mp.nstr(upper, 75)
            print(f"  certified n=40, gamma=2, switch={switch}: {mp.nstr(lower, 75)}")
            print("    interval width:", mp.nstr(upper - lower, 5))


if __name__ == "__main__":
    main()
