"""Partial common funds for independent depth-one automata and GKT placement.

The default run proves the finite comparisons by exact rational arithmetic and
cross-checks the results at 80 decimal digits.  --scaling prints further
population sizes.  --quorum-shift uses the study's subtraction-free GTH solver
to compare two nearby fund shares in larger populations.  --placement-mc runs independent replicas of the archived
12-player placement experiment and requires NumPy and Numba.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from math import comb

import mpmath as mp


def binomial_weights(n, p):
    return [comb(n, j) * p**j * (1 - p) ** (n - j) for j in range(n + 1)]


def count_row(n, k, stay, enter):
    residents = binomial_weights(k, stay)
    newcomers = binomial_weights(n - k, enter)
    row = [0] * (n + 1)
    for i, kept in enumerate(residents):
        for j, added in enumerate(newcomers):
            row[i + j] += kept * added
    return row


def volunteer_chain(n, a, t, cost, alpha, nu):
    """Volunteer success t-cost and free-rider success t when the good exists."""
    rows = [binomial_weights(n, nu * (1 - a))]
    welfare = [a]
    for k in range(1, n + 1):
        private = t - cost
        mean = t - cost * k / n
        stay = 1 - nu * (1 - ((1 - alpha) * private + alpha * mean))
        enter = nu * (1 - ((1 - alpha) * t + alpha * mean))
        rows.append(count_row(n, k, stay, enter))
        welfare.append(mean)
    return rows, welfare


def quorum_chain(n, alpha, nu, low=Q(4, 5), high=Q(97, 100), cost=Q(3, 5)):
    """Nonrefundable contributions produce the high group benefit at a one-quarter quorum."""
    one = 1 + 0 * nu
    low, high, cost = [one * value.numerator / value.denominator for value in (low, high, cost)]
    rows, welfare = [], []
    for k in range(n + 1):
        base = high if 4 * k >= n else low
        mean = base - cost * k / n
        stay = 1 - nu * (1 - (1 - alpha) * (base - cost) - alpha * mean)
        enter = nu * (1 - (1 - alpha) * base - alpha * mean)
        rows.append(count_row(n, k, stay, enter))
        welfare.append(mean)
    return rows, welfare


def placement_chain(alpha, nu):
    """GKT raw welfare, two agents, rich capacity 1 and weak capacity 9/10."""
    rich, weak = Q(1), Q(9, 10)
    rows, welfare = [], []
    for k in range(3):
        u_r = rich / k if k else Q(0)
        u_w = weak / (2 - k) if k < 2 else Q(0)
        mean = (k * u_r + (2 - k) * u_w) / 2
        r_eff = (1 - alpha) * u_r + alpha * mean
        w_eff = (1 - alpha) * u_w + alpha * mean
        rows.append(count_row(2, k, 1 - nu * (1 - r_eff) / 2, nu * (1 - w_eff) / 2))
        welfare.append(mean)
    return rows, welfare


def exact_stationary(rows):
    """Solve the normalized stationary equations and verify every equation."""
    size = len(rows)
    assert all(sum(row) == 1 for row in rows)
    system = [
        [rows[j][i] - (i == j) for j in range(size)] + [Q(0)]
        for i in range(size - 1)
    ]
    system.append([Q(1)] * (size + 1))
    for i in range(size):
        pivot = next(j for j in range(i, size) if system[j][i])
        system[i], system[pivot] = system[pivot], system[i]
        scaled = [v / system[i][i] for v in system[i]]
        system[i] = scaled
        for j in range(size):
            if j != i and system[j][i]:
                factor = system[j][i]
                system[j] = [v - factor * b for v, b in zip(system[j], scaled)]
    pi = [row[-1] for row in system]
    assert all(v >= 0 for v in pi) and sum(pi) == 1
    assert all(sum(pi[j] * rows[j][i] for j in range(size)) == v for i, v in enumerate(pi))
    return pi


def to_mp(q):
    return mp.mpf(q.numerator) / q.denominator if isinstance(q, Q) else mp.mpf(q)


def mp_stationary(rows):
    size = len(rows)
    matrix = mp.matrix([[to_mp(w) for w in row] for row in rows])
    system = matrix.T - mp.eye(size)
    for j in range(size):
        system[size - 1, j] = 1
    rhs = mp.zeros(size, 1)
    rhs[size - 1] = 1
    pi = mp.lu_solve(system, rhs)
    assert mp.norm(matrix.T * pi - pi, 1) < mp.mpf("1e-65")
    assert abs(mp.fsum(pi) - 1) < mp.mpf("1e-65") and min(pi) >= 0
    return pi


def exact_mean(rows, welfare):
    pi = exact_stationary(rows)
    expected = sum(v * w for v, w in zip(pi, welfare))
    check = mp_stationary(rows)
    assert max(abs(to_mp(u) - v) for u, v in zip(pi, check)) < mp.mpf("1e-65")
    return expected


def pd_balance(t, r, p, s, alpha, nu):
    """Returns half the CC minus DD tree numerator in the two-player PD."""
    d = nu * (1 - p)
    keep = 1 - nu * (1 - r)
    v = nu * (1 - (s + t) / 2)
    z = nu * (t - s) * (1 - alpha) / 2
    return nu * (r - p) * (v * (1 - v) + z**2) - (d * (1 - d) + keep * (1 - keep)) * z


def finite_certificates():
    print("N=12 volunteer dilemma, exact rational solution checked at 80 digits")
    a, t, cost = Q(1, 20), Q(99, 100), Q(21, 25)
    for nu, interior in [(Q(1, 2), Q(1, 2)), (Q(1), Q(3, 4))]:
        values = []
        for alpha in [Q(0), interior, Q(1)]:
            result = exact_mean(*volunteer_chain(12, a, t, cost, alpha, nu))
            print(f"  nu={nu}, alpha={alpha}, W={mp.nstr(to_mp(result), 55)}")
            values.append(result)
        gain = values[1] - max(values[0], values[2])
        assert gain > (Q(79, 1000) if nu == Q(1, 2) else Q(1, 10))

    print("N=12 one-quarter quorum, all Bernoulli probabilities strictly interior")
    for nu in (Q(1), Q(1, 2)):
        for alpha in (Q(0), Q(3, 5), Q(2, 3), Q(1)):
            W = exact_mean(*quorum_chain(12, alpha, nu))
            print(f"  nu={nu}, alpha={alpha}, W={mp.nstr(to_mp(W), 28)}")

    print("One-quarter quorum, limiting efficient and Nash shares")
    theta = Q(1, 4)
    for low, high, cost, target, nash in [
        (Q(4, 5), Q(9, 10), Q(1, 5), Q(0), Q(1, 2)),
        (Q(67, 100), Q(97, 100), Q(3, 5), Q(3, 5), Q(1, 2)),
        (Q(4, 5), Q(97, 100), Q(3, 5), Q(3, 5), Q(43, 60)),
    ]:
        assert (cost * theta - (1 - high) * (1 - 2 * theta)) / (2 * cost * theta * (1 - theta)) == target
        assert 1 - (high - low) / cost == nash
        assert high - cost * theta > low
        print(f"  low={low} high={high} cost={cost}  efficient={target} Nash={nash} welfare={high-cost*theta}")

    print("Two-player GKT placement, capacities 1 and 9/10")
    for nu in (Q(1), Q(1, 2)):
        for alpha in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)):
            value = exact_mean(*placement_chain(alpha, nu))
            if nu == 1:
                formula = (20 * alpha**2 - 89 * alpha + 13180) / (2 * (21 * alpha**2 - 61 * alpha + 7349))
            else:
                formula = (20 * alpha**2 - 169 * alpha + 30780) / (2 * (21 * alpha**2 - 101 * alpha + 17029))
            assert value == formula
            print(f"  nu={nu}, alpha={alpha}, W={value}")
        offset = 231 if nu == 1 else 151
        optimum = offset / (200 + mp.sqrt(40000 - offset))
        print(f"  unique maximizing alpha={mp.nstr(optimum, 55)}")

    print("Two-player PD depth-one balance")
    for nu in (Q(1), Q(1, 2)):
        first = [Q(i, 20) for i in (19, 18, 12, 11)]
        second = [Q(i, 20) for i in (17, 16, 12, 8)]
        for alpha in (Q(0), Q(2, 9), Q(4, 9), Q(8, 9), Q(1)):
            t, r, p, s = second
            lhs = pd_balance(t, r, p, s, alpha, nu)
            if nu == 1:
                rhs = 3 * (3 * alpha + 22) * (9 * alpha - 4) / 8000
            else:
                rhs = 3 * (3 * alpha + 62) * (9 * alpha - 4) / 64000
            assert lhs == rhs
            mix = (t - s) * alpha / 2
            rows = [
                binomial_weights(2, nu * (1 - p)),
                count_row(2, 1, 1 - nu * (1 - s - mix), nu * (1 - t + mix)),
                binomial_weights(2, 1 - nu * (1 - r)),
            ]
            pi = exact_stationary(rows)
            assert (lhs > 0) == (pi[2] > pi[0]) and (lhs == 0) == (pi[2] == pi[0])
        if nu == 1:
            assert pd_balance(*first, Q(0), nu) == Q(9, 4000)
        print(f"  nu={nu}, second example alpha_bal=4/9, alpha_CC-Nash=2/9, alpha_dominance=8/9")

    print("N=12 GKT Nash occupancy transitions")
    caps_weak = Q(3, 20)
    thresholds = []
    for m in range(6, 1, -1):
        gap = Q(1, m) - caps_weak
        thresholds.append(gap / (gap + caps_weak / 12))
    assert thresholds == [Q(4, 7), Q(4, 5), Q(8, 9), Q(44, 47), Q(28, 29)]
    print("  " + ", ".join(str(a) for a in thresholds))


def scaling_checks():
    a, t, cost, nu = mp.mpf(".1"), mp.mpf(1), mp.mpf(".75"), mp.mpf(".5")
    print("N, alpha, raw welfare W, zero-volunteer probability, regeneration length")
    for n in (8, 16, 32, 64):
        for alpha in (mp.mpf(0), mp.mpf(".5"), mp.mpf(1)):
            rows, welfare = volunteer_chain(n, a, t, cost, alpha, nu)
            pi = mp_stationary(rows)
            W = mp.fdot(pi, welfare)
            x = mp.fsum(pi[k] * k / n for k in range(n + 1))
            x2 = mp.fsum(pi[k] * (mp.mpf(k) / n) ** 2 for k in range(n + 1))
            assert abs((1 - a) * pi[0] - cost * ((1 - 2 * alpha) * x + 2 * alpha * x2)) < mp.mpf("1e-65")
            if not alpha:
                b = nu * (1 - a)
                survival = 1 - nu * cost
                length = 1 + mp.fsum(
                    (-1) ** (j + 1) * comb(n, j) * b**j / (1 - survival**j)
                    for j in range(1, n + 1)
                )
                assert abs(1 / pi[0] - length) < mp.mpf("1e-65")
                assert abs((1 - W) * length - 2 * (1 - a)) < mp.mpf("1e-65")
            print(f"  {n:2} {float(alpha):.1f}  " + "  ".join(mp.nstr(u, 18) for u in (W, pi[0], 1 / pi[0])))

    print("Fixed free-rider failure 1/20: finite welfare, limiting welfare")
    failure = mp.mpf(".05")
    for alpha in (mp.mpf(0), mp.mpf(".5"), mp.mpf(1)):
        linear = cost * (2 * alpha - 1) - 2 * failure
        root = 2 * failure / (mp.sqrt(linear**2 + 8 * alpha * cost * failure) - linear)
        residual = failure * (1 - 2 * root) + cost * root * (2 * alpha - 1 - 2 * alpha * root)
        assert abs(residual) < mp.mpf("1e-65")
        for n in (16, 32, 64):
            rows, welfare = volunteer_chain(n, a, 1 - failure, cost, alpha, nu)
            W = mp.fdot(mp_stationary(rows), welfare)
            limit = 1 - failure - cost * root
            print(f"  N={n:2} alpha={float(alpha):.1f}  W={mp.nstr(W, 18)}  limit={mp.nstr(limit, 18)}")

    print("One-quarter quorum, nu=1/2: finite welfare and limiting welfare")
    for n in (16, 32, 64):
        for alpha, limit in [(Q(0), ".68"), (Q(3, 5), ".82"), (Q(2, 3), ".79"), (Q(1), ".67")]:
            rows, welfare = quorum_chain(n, to_mp(alpha), nu)
            pi = mp_stationary(rows)
            W = mp.fdot(pi, welfare)
            print(f"  N={n:2} alpha={alpha}  W={mp.nstr(W, 18)}  limit={limit}")


def placement_mc(replicates, burn, steps, depths=(3, 6, 12)):
    import numpy as np
    from numba import njit

    @njit
    def run(n, alpha, seed):
        np.random.seed(seed)
        actions = np.random.randint(0, 12, 12)
        depths = np.full(12, n - 1)
        occupied = np.zeros(12, dtype=np.int64)
        raw = 0.0
        for time in range(burn + steps):
            occupied[:] = 0
            for site in actions:
                occupied[site] += 1
            total = 1.0 if occupied[0] else 0.0
            for site in range(1, 12):
                if occupied[site]:
                    total += .15
            mean = total / 12
            if time >= burn:
                raw += mean
            for i, site in enumerate(actions):
                private = (1.0 if site == 0 else .15) / occupied[site]
                probability = (1 + (1 - alpha) * private + alpha * mean) / 2
                if np.random.random() < probability:
                    depths[i] = min(n - 1, depths[i] + 1)
                elif depths[i]:
                    depths[i] -= 1
                else:
                    actions[i] = np.random.randint(12)
        return raw / steps

    print(f"N=12 GKT raw welfare, {replicates} independent runs per cell, {burn} burn + {steps} sampled steps")
    for n in depths:
        for j, alpha in enumerate((0., .15, .30, .50, .70, .85, 1.)):
            sample = np.array([run(n, alpha, 310021 + 100000 * n + 1000 * j + i) for i in range(replicates)])
            mean = sample.mean()
            se = sample.std(ddof=1) / replicates**.5
            print(f"  n={n:2} alpha={alpha:.2f}  W={mean:.8f}  between-run SE={se:.8f}", flush=True)


def quorum_shift_checks():
    from decimal import Decimal, localcontext
    from phase1_chain import stationary

    print("One-quarter quorum, 80-digit GTH: critical share and a slightly higher fixed candidate")
    with localcontext() as ctx:
        ctx.prec = 80
        tol = Decimal("1e-72")
        for n in (64, 128, 256, 512):
            candidate = Q(5, 8) if n == 64 else Q(19, 30)
            values = []
            for fraction in (Q(3, 5), candidate):
                alpha = Decimal(fraction.numerator) / fraction.denominator
                rows, welfare = quorum_chain(n, alpha, Decimal(".5"))
                assert max(abs(sum(row) - 1) for row in rows) < tol
                off_diagonal = [{j: p for j, p in enumerate(row) if j != i} for i, row in enumerate(rows)]
                pi = stationary(off_diagonal, list(range(n + 1)))
                residual = max(abs(sum(pi[j] * rows[j][i] for j in range(n + 1)) - x) for i, x in enumerate(pi))
                assert min(pi) > 0 and residual < tol
                values.append(sum(x * w for x, w in zip(pi, welfare)))
            assert values[1] > values[0]
            print(f"  N={n:3} W(3/5)={values[0]:.30f} W({candidate})={values[1]:.30f}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scaling", action="store_true")
    parser.add_argument("--quorum-shift", action="store_true")
    parser.add_argument("--placement-mc", action="store_true")
    parser.add_argument("--replicates", type=int, default=16)
    parser.add_argument("--burn", type=int, default=30000)
    parser.add_argument("--steps", type=int, default=120000)
    parser.add_argument("--depths", type=int, nargs="+", default=[3, 6, 12])
    args = parser.parse_args()
    if args.replicates < 2 or args.steps <= 0 or args.burn < 0 or min(args.depths) <= 0:
        parser.error("Use at least two replicas, positive depths and sample count, and a nonnegative burn-in.")
    mp.mp.dps = 80
    finite_certificates()
    if args.scaling:
        scaling_checks()
    if args.quorum_shift:
        quorum_shift_checks()
    if args.placement_mc:
        placement_mc(args.replicates, args.burn, args.steps, args.depths)
