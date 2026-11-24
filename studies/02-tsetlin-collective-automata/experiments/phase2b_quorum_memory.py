"""Productive quorum balance, local stability and finite-population stationarity.

Run this file from any directory. Root enclosures and finite-chain transition
weights are rational. The stationary solver uses Decimal GTH and certifies the
output from an exact residual. The local Jacobian bounds use interval arithmetic.
"""

from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product, zip_longest
import json
from math import comb, lcm
from pathlib import Path

from mpmath import iv, mp

from phase1_chain import moves, stationary
from phase2b_quorum_stability import verify_low_stability, verify_productive_stability

THETA, COST, LOW, HIGH = Q(1, 4), Q(3, 5), Q(4, 5), Q(97, 100)
NASH = 1 - (HIGH - LOW) / COST
DATA = Path(__file__).resolve().parent / "data" / "phase2b_quorum_memory.json"
ROOT_PLACES = 84


def real(a):
    return mp.mpf(a.numerator) / a.denominator if isinstance(a, Q) else mp.mpf(a)


def interval(a):
    return iv.mpf(a.numerator) / a.denominator if isinstance(a, Q) else iv.mpf(a)


def number(a, digits=82):
    return mp.nstr(real(a), digits)


def payoffs(t, x, share, cost):
    defect = t - cost * share * x
    return defect - cost * (1 - share), defect


def duration(n, p):
    """Stationary normalization on one action, with switch probability one."""
    if p == mp.mpf("0.5"):
        return 2 * n
    return mp.expm1(n * mp.log1p((2 * p - 1) / (1 - p))) / (2 * p - 1)


def duration_ratio_integers(n, p):
    """Unreduced exact numerator and denominator, efficient even at n=1024."""
    u, v = p.numerator, p.denominator
    w = v - u
    if w == u:
        return 2 * n, 1
    sign = 1 if u > w else -1
    w_power = w**n
    return sign * v * (u**n - w_power), sign * (u - w) * w_power


def exact_balance_sign(n, x, t, share, cost=COST):
    """Sign of F_n(p_C,p_D) - x, with no rounded intermediate values."""
    pc, pd = payoffs(t, x, share, cost)
    hc_num, hc_den = duration_ratio_integers(n, pc)
    hd_num, hd_den = duration_ratio_integers(n, pd)
    diff = (x.denominator - x.numerator) * hc_num * hd_den - x.numerator * hd_num * hc_den
    return (diff > 0) - (diff < 0)


def certified_share(n, t):
    theta, base, cost = map(real, (THETA, t, COST))
    low, high = mp.mpf(0), mp.mpf(1)
    assert exact_balance_sign(n, THETA, t, Q(0)) < 0
    assert exact_balance_sign(n, THETA, t, Q(1)) > 0
    for _ in range(310):
        share = (low + high) / 2
        pc, pd = payoffs(base, theta, share, cost)
        if (1 - theta) * duration(n, pc) < theta * duration(n, pd):
            low = share
        else:
            high = share
    value = (low + high) / 2
    scale = 10**ROOT_PLACES
    floor = int(mp.floor(value * scale))
    endpoints = (Q(floor - 1, scale), Q(floor + 2, scale))
    assert exact_balance_sign(n, THETA, t, endpoints[0]) < 0
    assert exact_balance_sign(n, THETA, t, endpoints[1]) > 0
    return value, endpoints


def decimal_endpoint(q):
    with localcontext() as ctx:
        ctx.prec = ROOT_PLACES + 5
        return format(Decimal(q.numerator) / Decimal(q.denominator), "f")


def branch_grid():
    result, high_intervals = [], {}
    for n in (*range(1, 13), 16, 32, 64, 128, 256, 512, 1024):
        vals = {}
        for label, base in (("low", LOW), ("high", HIGH)):
            value, endpoints = certified_share(n, base)
            vals[label] = {
                "share": number(value),
                "rational_bracket": [decimal_endpoint(e) for e in endpoints],
                "n_times_one_minus_share": number(n * (1 - value)),
            }
            if base == HIGH and n <= 3:
                high_intervals[n] = endpoints
        result.append(dict(depth=n, **vals))
    return result, high_intervals


def frozen_rows(n, pc, pd, kind):
    one, zero = pc * 0 + 1, pc * 0
    rows = [[zero for _ in range(2 * n)] for _ in range(2 * n)]
    for i in range(2 * n):
        p = pc if i < n else pd
        for outcome, weight in ((True, p), (False, one - p)):
            for j, fraction in moves(i, n, outcome, kind, exact=True):
                rows[i][j] += weight * fraction.numerator / fraction.denominator
    return rows


def depth_weights(n, pc, pd):
    weights = []
    for i in range(2 * n):
        p = pc if i < n else pd
        exponent = n - 1 - i if i < n else i - n
        weights.append((p / (1 - p)) ** exponent / (1 - p))
    total = sum(weights)
    return [w / total for w in weights]


def tangent_certificate(n, endpoints, kind):
    """Bound the high-branch Jacobian power at the quota in simplex coordinates."""
    share = iv.mpf([interval(endpoints[0]).a, interval(endpoints[1]).b])
    theta, cost = interval(THETA), interval(COST)
    pc, pd = payoffs(interval(HIGH), theta, share, cost)
    k = frozen_rows(n, pc, pd, kind)
    win = frozen_rows(n, interval(1), interval(1), kind)
    lose = frozen_rows(n, interval(0), interval(0), kind)
    weights = depth_weights(n, pc, pd)
    dim = 2 * n - 1
    jac = iv.matrix(dim, dim)
    for i in range(dim):
        response = (
            -cost * share * sum(weights[s] * (win[s][i] - lose[s][i]) for s in range(dim + 1))
        )
        for j in range(dim):
            jac[i, j] = k[j][i] - k[-1][i] + (response if j < n else 0)
    power, length = jac, 1
    while length <= 2048:
        bound = max(mp.mpf(sum(abs(power[i, j]) for j in range(dim)).b) for i in range(dim))
        if bound < mp.mpf("0.99"):
            upper = Q(int(mp.ceil(bound * 10**10)), 10**10)
            assert real(upper) < 1 and bound <= real(upper)
            return {
                "depth": n,
                "architecture": kind,
                "power": length,
                "infinity_norm_upper": decimal_endpoint(upper),
            }
        power = power * power
        length *= 2
    raise ArithmeticError("No local contraction certificate at the selected powers.")


def integer_count_rows(n, population, share, kind):
    """Strong exchange quotient; each row has the same exact denominator."""
    states = list(combinations_with_replacement(range(2 * n), population))
    index = {state: i for i, state in enumerate(states)}
    tables = []
    denominator = 1
    for contributors in range(population + 1):
        x = Q(contributors, population)
        pc, pd = payoffs(HIGH if x >= THETA else LOW, x, share, COST)
        k = frozen_rows(n, pc, pd, kind)
        for row in k:
            denominator = lcm(denominator, *(w.denominator for w in row))
        tables.append(k)
    moves_by_count = [
        [[(j, int(denominator * w)) for j, w in enumerate(row) if w] for row in k] for k in tables
    ]
    row_den = denominator**population
    rows, fractions = [], []
    for state in states:
        count = sum(i < n for i in state)
        fractions.append(Q(count, population))
        transitions = {(): 1}
        for i in state:
            next_counts = defaultdict(int)
            for dest, mass in transitions.items():
                for j, weight in moves_by_count[count][i]:
                    next_counts[tuple(sorted((*dest, j)))] += mass * weight
            transitions = next_counts
        assert sum(transitions.values()) == row_den
        rows.append({index[key]: mass for key, mass in transitions.items()})
    return fractions, rows, row_den


def exact_residual(rows, denominator, pi):
    """Integer L1 residual of a normalized positive rational approximation."""
    common = lcm(*(Q(x).denominator for x in pi))
    weights = [int(Q(x) * common) for x in pi]
    assert min(weights) > 0
    total = sum(weights)
    residual = [-u * denominator for u in weights]
    for u, row in zip(weights, rows):
        for j, a in row.items():
            residual[j] += u * a
    return Q(sum(abs(v) for v in residual), total * denominator), weights, total


def finite_chain(n, population, share, kind):
    xs, rows, denominator = integer_count_rows(n, population, share, kind)
    with localcontext() as ctx:
        ctx.prec = 175
        off_diag = [
            {j: Decimal(w) / denominator for j, w in row.items() if i != j}
            for i, row in enumerate(rows)
        ]
        pi = stationary(off_diag, list(range(len(rows))))
    residual, weights, total = exact_residual(rows, denominator, pi)
    # In at most 2n−1 rounds all agents can move left to deepest C, then hold.
    # Every prescribed step/hold has probability >= 3/200 per agent per round.
    length = 2 * n - 1
    minorization = Q(3, 200) ** (population * length)
    error = length * residual / minorization
    assert error < Q(1, 10**84)
    high_prob = Q(sum(w for w, x in zip(weights, xs) if x >= THETA), total)
    fraction = sum(w * x for w, x in zip(weights, xs)) / total
    welfare = LOW + (HIGH - LOW) * high_prob - COST * fraction
    return {
        "depth": n,
        "population": population,
        "architecture": kind,
        "share": str(share),
        "exchange_states": len(xs),
        "cooperation": number(fraction),
        "productive_probability": number(high_prob),
        "welfare": number(welfare),
        "L1_balance_residual": number(residual, 8),
        "L1_error_upper_scientific": upward_decimal(error),
    }


def upward_decimal(q):
    with localcontext() as ctx:
        ctx.prec, ctx.rounding = 8, ROUND_CEILING
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def bistability_witness():
    """Rational two-lag Jacobian and the fixed-point checks, for both rules."""
    n, share, cost, theta = 2, Q(333, 400), Q(1, 2), Q(1, 200)
    values = []
    for base, x, branch in (
        (Q(303733, 304760), Q(1, 401), "low"),
        (Q(1999, 2000), Q(1, 5), "high"),
    ):
        assert (x < theta) == (branch == "low")
        assert exact_balance_sign(n, x, base, share, cost) == 0
        pc, pd = payoffs(base, x, share, cost)
        q, r, a = 1 - pd, 1 - pc, cost * share
        for kind, nu in (("L", Q(1)), ("B", Q(1, 2))):
            A = 1 + nu * (a * (q * (1 - x) - r * x) - q - r)
            B = nu * (q * (1 - q + a * (1 - x)) + r * (1 - r - a * x))
            assert min(A, B, 1 - A - B) > 0
            values.append(
                {
                    "branch": branch,
                    "base": str(base),
                    "cooperation": str(x),
                    "architecture": kind,
                    "A": str(A),
                    "B": str(B),
                    "one_minus_A_minus_B": str(1 - A - B),
                }
            )
    return {
        "depth": n,
        "share": str(share),
        "cost": str(cost),
        "quota": str(theta),
        "checks": values,
    }


@dataclass(frozen=True)
class Interval:
    lo: Q
    hi: Q

    def __add__(self, other):
        other = box(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-box(other))

    def __rsub__(self, other):
        return box(other) + (-self)

    def __mul__(self, other):
        other = box(other)
        values = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(values), max(values))

    __rmul__ = __mul__

    @property
    def magnitude(self):
        return max(-self.lo, self.hi)


def box(number):
    return number if isinstance(number, Interval) else Interval(Q(number), Q(number))


def rational_interval(lo, hi):
    return Interval(Q(lo), Q(hi))


def next_x(y, x, previous_base, current_base, k, nu, with_jac=False):
    d = COST - k
    pd = previous_base - k * y
    pc = pd - d
    q = 1 - current_base + k * x
    bd = 1 - x - pd * (1 - y)
    bc = x - pc * y
    output = x + nu * (q * bd - (q + d) * bc)
    if not with_jac:
        return output
    dj = nu * (q * (previous_base + k - 2 * k * y) + (q + d) * (previous_base - d - 2 * k * y))
    di = 1 + nu * (k * (bd - bc) - 2 * q - d)
    return output, [[box(0), box(1)], [dj, di]]


def cell_number(x, segments):
    return min(segments - 1, max(0, x * segments // 1))


def certify_global_trap():
    k, noise = rational_interval("0.486", "0.492"), rational_interval("-0.0001", "0.0001")
    segments = 100
    cells = [rational_interval(Q(i, segments), Q(i + 1, segments)) for i in range(segments)]
    outcomes = []
    for nu in (Q(1), Q(1, 2)):
        transitions = {}
        for i, j in product(range(segments), repeat=2):
            s = LOW if i < 25 else HIGH
            t = LOW if j < 25 else HIGH
            image = next_x(cells[i], cells[j], s, t, k, nu) + noise
            transitions[i, j] = [
                (j, v)
                for v in range(
                    cell_number(image.lo, segments), cell_number(image.hi, segments) + 1
                )
            ]
        active = set(transitions)
        for steps in range(100):
            if all(24 <= min(i, j) and max(i, j) <= 46 for i, j in active):
                break
            active = {v for node in active for v in transitions[node]}
        else:
            raise AssertionError("The entire reachable region must enter the trapping square.")
        # Reachable sets from all cells are nested, so this inclusion persists at every later step.
        outcomes.append(
            {
                "nu": str(nu),
                "iterations": steps,
                "surviving_boxes": len(active),
                "range": [min(min(v) for v in active), 1 + max(max(v) for v in active)],
            }
        )
    return outcomes


def matmul(left, right):
    return [[sum(left[i][h] * right[h][j] for h in range(2)) for j in range(2)] for i in range(2)]


def certify_cycle():
    k, radius = Q(21, 50), Q(1, 10**80)
    centers = {
        Q(1): (
            "0.247563225574609643886266961323431265004871966477071023342636293455301781786525228217",
            "0.248013679853141051525104854777578150302898835288107596359528347248877610117256983018",
        ),
        Q(1, 2): (
            "0.246764272834113654865932577625142262491007075292944274628994308553330724737784900735",
            "0.244812525564393032956452327047785368053521961570228296903310697862045887171178475574",
        ),
    }
    results = []
    for nu, center in centers.items():
        cy, cx = map(Q, center)
        center_y, center_x = box(cy), box(cx)
        y, x = rational_interval(cy - radius, cy + radius), rational_interval(
            cx - radius, cx + radius
        )
        derivative = [[box(1), box(0)], [box(0), box(1)]]
        thirds = None
        for st in ((LOW, LOW), (LOW, HIGH), (HIGH, LOW)):
            for base, window in zip(st, (y, x)):
                assert window.hi < THETA if base == LOW else window.lo > THETA
            pd = st[0] - k * y
            assert (x - (pd - (COST - k)) * y).lo > 0 and (1 - x - pd * (1 - y)).lo > 0
            xnew, local = next_x(y, x, *st, k, nu, with_jac=True)
            if thirds is None:
                thirds = xnew
            y, x = x, xnew
            center_y, center_x = center_x, next_x(center_y, center_x, *st, k, nu)
            derivative = matmul(local, derivative)
        norm = max(sum(entry.magnitude for entry in row) for row in derivative)
        residual = max((center_y - cy).magnitude, (center_x - cx).magnitude)
        norm_cap = Q(72 if nu == 1 else 85, 100)
        assert norm < norm_cap and residual < radius * (1 - norm_cap)

        def rounded(fraction, places):
            scale = 10**places
            return "0." + str((fraction * scale + Q(1, 2)) // 1).zfill(places)

        third_display = rounded((thirds.lo + thirds.hi) / 2, 72)
        assert max(abs(thirds.lo - Q(third_display)), abs(thirds.hi - Q(third_display))) < Q(
            1, 2 * 10**72
        )
        results.append(
            {
                "nu": str(nu),
                "cycle_72_digits": [rounded(cy, 72), rounded(cx, 72), third_display],
                "return_box_center": list(center),
                "radius": "1e-80",
                "center_residual_lt_1e-83": residual < Q(1, 10**83),
                "infinity_norm_strict_upper": str(norm_cap),
            }
        )
    return results


def certify_local_order_bounds():
    k = rational_interval("0.486", "0.492")
    d = COST - k
    y = rational_interval("0.24", "0.47")
    bounds = []
    for s, t in product((LOW, HIGH), repeat=2):
        # The low current continuation is only used at x <= theta.
        x = rational_interval("0.24", THETA if t == LOW else "0.47")
        q = 1 - t + k * x
        gy = q * (s + k - 2 * k * y) + (q + d) * (s - d - 2 * k * y)
        gx = 1 - 2 * (1 - t) - d + k * (1 - 4 * x - (s - k * y) * (1 - 2 * y) - d * y)
        # These are d/dx for nu=1 and (d/dy)/nu. For nu=1/2 the x
        # derivative equals (1+gx)/2.
        assert gx.lo > Q(1, 10) and gy.lo > 0
        bounds.append((gx.lo, gy.lo))
    z = rational_interval("0.24", "0.26")
    positive_quadratic_derivative = (1 - 2 * z) * (1 - HIGH + k * z) - d * z
    assert positive_quadratic_derivative.lo > Q(3, 100)
    r_min = (1 - HIGH + k.lo * Q("0.24")) / d.hi
    v_min = 2 * r_min * (1 + r_min)
    assert v_min > 1
    F_lipschitz = k.hi / d.lo * v_min / (1 + v_min) ** 2
    assert F_lipschitz < Q(3, 5)
    q_cap = 1 - HIGH + k.hi * Q("0.47")
    ratio_cap = q_cap / d.lo
    endpoint_F = ratio_cap**2 / (ratio_cap**2 + (1 + ratio_cap) ** 2)
    assert endpoint_F < Q(34, 100)
    return {
        "positive_partial_y": True,
        "partial_x_strict_lower": "1/10",
        "diagonal_payoff_derivative_strict_lower": "3/100",
        "F_lipschitz_strict_upper": "3/5",
        "F_at_047_strict_upper": "17/50",
    }


def add(left, right):
    return [x + y for x, y in zip_longest(left, right, fillvalue=0)]


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, coefficient in enumerate(right):
            result[i + j] += value * coefficient
    return result


def scale(factor, coefficients):
    return [factor * value for value in coefficients]


def derivative(coefficients):
    return [i * value for i, value in enumerate(coefficients) if i] or [0]


def shifted(coefficients, offset):
    return [
        sum(
            value * comb(i, j) * offset ** (i - j)
            for i, value in enumerate(coefficients)
            if i >= j
        )
        for j in range(len(coefficients))
    ]


def verify_log_derivative(max_depth, offset, factor):
    """Expand the rational certificate for q(log h)''/(log h)' <= 1 + 1/factor."""
    minima = []
    for n in range(1, max_depth + 1):
        geom = [1] * n
        a = add(geom, multiply([1, 1], derivative(geom)))
        cross = add(multiply(a, derivative(geom)), scale(-1, multiply(derivative(a), geom)))
        poly = add(multiply(a, geom), scale(factor, multiply([1, 1], cross)))
        while len(poly) > 1 and poly[-1] == 0:
            poly.pop()
        minimum = min(shifted(poly, offset))
        assert minimum == n
        minima.append(int(minimum))
    return minima


def duration_and_log_slope(n, p):
    q = 1 - p
    weights = [(p / q) ** j for j in range(n)]
    total = sum(weights)
    mean = sum(j * weight for j, weight in enumerate(weights)) / total
    return total / q, (mean + p) / (p * q)


def verify_low_grid():
    """Bound F'_L at roots on p_C <= 4/7 in 400 exact payoff rectangles."""
    c = Q(3, 5)

    def grid(low, high):
        return [low + i * (high - low) / 5 for i in range(6)]

    p_c = grid(Q(1, 5), Q(4, 7))
    p_d = grid(Q(13, 20), Q(4, 5))
    maxima = []
    for n in range(1, 17):
        coop = [duration_and_log_slope(n, p) for p in p_c]
        defect = [duration_and_log_slope(n, p) for p in p_d]
        upper = []
        for i in range(5):
            for j in range(5):
                odds = coop[i + 1][0] / defect[j][0]
                assert odds < 1
                shared = c - p_d[j] + p_c[i + 1]
                slope = defect[j + 1][1] - coop[i][1]
                upper.append(shared * odds * slope / (1 + odds) ** 2)
        maxima.append(max(upper))
    assert max(maxima) < Q(22, 25)
    scaled_upper = [-((-(10**6) * v.numerator) // v.denominator) for v in maxima]
    return {
        "boxes_per_depth": 25,
        "upper_millionths_by_depth": scaled_upper,
        "strict_common_cap": "22/25",
    }


def depth_three_below_nash():
    """Bound every admissible product of depth-three kernels on 600 successive steps."""
    denominator, scale = 800, 10**9
    block_length, blocks = 12, 50
    results = {}
    for kind, nu_den in (("L", 1), ("B", 2)):
        rows = []
        for pd in (554, 776):
            pc = pd - 136
            qd, qc = denominator - pd, denominator - pc
            assert qd % nu_den == qc % nu_den == 0
            rows.append((pd, pc, qd, qc, qd // nu_den, qc // nu_den))
        upper = (scale,) * 6 + (0,)
        for _ in range(blocks):
            reachable = [upper]
            for _ in range(block_length):
                images = []
                for pd, pc, qd, qc, switch_d, switch_c in rows:
                    hold = denominator - switch_d - switch_c
                    assert hold >= 0
                    for v in reachable:
                        numerators = (
                            qd * v[0] + pd * v[2],
                            qd * v[1] + pd * v[3],
                            switch_d * v[2] + hold * v[3] + switch_c * v[4],
                            pc * v[3] + qc * v[5],
                            pc * v[4] + qc * v[6],
                        )
                        middle = tuple((a + denominator - 1) // denominator for a in numerators)
                        images.append((scale, *middle, 0))
                reachable = images
            upper = tuple(map(max, zip(*reachable)))
        assert 4 * upper[3] < scale
        results[kind] = {"tail_numerators": upper, "cooperation_upper": str(Q(upper[3], scale))}
    return {
        "denominator": scale,
        "block_length": block_length,
        "blocks": blocks,
        "results": results,
    }


def old_share_depth_three():
    """Select the depth-three low equilibrium at the depth-one efficient share."""
    k, pc0, pd0 = Q(9, 25), Q(14, 25), Q(4, 5)

    def response(pc, pd):
        hc = (1 - pc + pc**2) / (1 - pc) ** 3
        hd = (1 - pd + pd**2) / (1 - pd) ** 3
        return hc / (hc + hd)

    def comparison(lower, upper):
        return response(pc0 - k * upper, pd0 - k * lower), response(
            pc0 - k * lower, pd0 - k * upper
        )

    lower, upper = Q(0), THETA
    scale = 10**12
    for _ in range(6):
        low, high = comparison(lower, upper)
        lower, upper = Q(low * scale // 1, scale), Q(-((-high * scale) // 1), scale)
    left, right = Q(9, 100), Q(14, 125)
    assert left < lower < upper < right
    fmin, fmax = comparison(left, right)
    assert left <= fmin < fmax <= right

    def log_slope_bound(p):
        return 3 / (1 - p) + max(0, 2 * p - 1) * Q(4, 3)

    bound = k * fmax * (log_slope_bound(pc0 - k * left) + log_slope_bound(pd0 - k * left))
    assert bound < Q(4, 5)
    lo, hi = left, right
    for _ in range(310):
        mid = (lo + hi) / 2
        if exact_balance_sign(3, mid, LOW, Q(3, 5)) > 0:
            lo = mid
        else:
            hi = mid
    assert number(lo) == number(hi) and number(LOW - COST * lo) == number(LOW - COST * hi)
    return {
        "share": "3/5",
        "six_comparison_rounds": [str(lower), str(upper)],
        "lipschitz_upper": "4/5",
        "limiting_cooperation": number(lo),
        "limiting_welfare": number(LOW - COST * lo),
    }


def depth_three_impulse_signs():
    """Certify the signed response to a change of the common payoff at depth three."""
    import numpy as np

    denominator, scale = 20000, 10**11

    def tail_matrix(pd, gap, switch):
        pc, qd, qc = pd - gap, 1 - pd, 1 - pd + gap
        rows = [[Q(0)] * 7 for _ in range(7)]
        rows[0][0] = rows[6][6] = Q(1)
        for j in (1, 2):
            rows[j][j - 1], rows[j][j + 1] = qd, pd
        for j in (4, 5):
            rows[j][j - 1], rows[j][j + 1] = pc, qc
        rows[3][2:5] = (switch * qd, 1 - switch * (qd + qc), switch * qc)
        assert all(sum(row) == 1 and min(row) >= 0 for row in rows)
        assert all((w * denominator).denominator == 1 for row in rows for w in row)
        return np.array([[int(w * denominator) for w in row] for row in rows], dtype=np.int64).T

    def initial_lower(dlo, dhi, switch):
        lower = []
        for i in range(7030, 8380):
            pl, ph = Q(i, 10000), Q(i + 1, 10000)
            ql, qh = 1 - ph, 1 - pl
            qcl, qch = ql + dlo, qh + dhi
            vector = (
                0,
                pl * qcl**3,
                ql * qcl**3,
                switch * dlo * ql**2 * qcl**2,
                -qch * qh**3,
                -(ph - dlo) * qh**3,
                0,
            )
            lower.append([value * scale // 1 for value in vector])
        return np.array(lower, dtype=np.int64)

    # Row sums are denominator and all propagated magnitudes stay <= scale.
    # The largest absolute integer dot product fits exactly in int64.
    assert denominator * scale < 2**63
    result = {}
    for kind, switch in (("L", Q(1)), ("B", Q(1, 2))):
        center = interior = scale
        for j in range(678, 684):
            dl, dh = Q(j, 10000), Q(j + 1, 10000)
            vectors = initial_lower(dl, dh, switch)
            assert int(np.max(np.abs(vectors))) < scale
            operators = [
                (tail_matrix(p, dl, switch), tail_matrix(p, dh, switch))
                for p in (Q(666, 1000), Q(838, 1000))
            ]
            center = min(center, int(vectors[:, 3].min()))
            for _ in range(7):
                vectors = np.vstack(
                    [
                        np.minimum(vectors @ low, vectors @ high) // denominator
                        for low, high in operators
                    ]
                )
                center = min(center, int(vectors[:, 3].min()))
            interior = min(interior, int(vectors[:, 1:6].min()))
        assert min(center, interior) > 0
        result[kind] = {
            "central_minimum_numerator": center,
            "all_interior_minimum_at_length_7_numerator": interior,
        }
    return {
        "scale": scale,
        "matrix_denominator": denominator,
        "gap_box_count": 6,
        "reference_payoff_box_count": 1350,
        "length": 7,
        "results": result,
    }


def depth_three_trajectories():
    """Finite-time high-precision trajectories from each of the six pure starting states."""
    n, share, rounds = 3, Q(89, 100), 50000
    lo, hi = THETA, Q(1, 2)
    for _ in range(310):
        mid = (lo + hi) / 2
        if exact_balance_sign(n, mid, HIGH, share) > 0:
            lo = mid
        else:
            hi = mid
    assert exact_balance_sign(n, lo, HIGH, share) > 0
    assert exact_balance_sign(n, hi, HIGH, share) < 0
    cases = []
    with localcontext() as ctx:
        ctx.prec = 110
        target = Decimal(mid.numerator) / mid.denominator
        cutoff = Decimal("0.25")
        k, gap = Decimal("0.534"), Decimal("0.066")
        for kind, nu in (("L", Decimal(1)), ("B", Decimal("0.5"))):
            for start in range(2 * n):
                y = [Decimal(0)] * (2 * n)
                y[start] = Decimal(1)
                last_low = None
                for t in range(rounds):
                    x = sum(y[:n])
                    if x < cutoff:
                        base = Decimal("0.80")
                        last_low = t
                    else:
                        base = Decimal("0.97")
                    pd = base - k * x
                    pc = pd - gap
                    qc, qd = 1 - pc, 1 - pd
                    # States run deepest C to deepest D.
                    y = [
                        pc * (y[0] + y[1]),
                        qc * y[0] + pc * y[2],
                        qc * y[1] + (1 - nu) * qc * y[2] + nu * qd * y[3],
                        nu * qc * y[2] + (1 - nu) * qd * y[3] + qd * y[4],
                        pd * y[3] + qd * y[5],
                        pd * (y[4] + y[5]),
                    ]
                assert abs(sum(y) - 1) < Decimal("1e-102")
                deviation = abs(sum(y[:n]) - target)
                assert deviation < Decimal("1e-78")
                cases.append(
                    {
                        "architecture": kind,
                        "initial_state": start,
                        "last_unproductive_time_in_run": last_low,
                        "terminal_quota_fraction": format(sum(y[:n]), ".82f"),
                        "terminal_error_from_root_midpoint": str(deviation),
                    }
                )
    return {
        "share": str(share),
        "rounds": rounds,
        "arithmetic_decimal_digits": 110,
        "initial_order": "deepest C to deepest D, indexed 0 to 5",
        "productive_equilibrium": number(mid),
        "cases": cases,
    }


def main():
    mp.dps = 110
    iv.dps = 100
    grid, brackets = branch_grid()
    coefficient = real(HIGH - COST * THETA) * real(1 - HIGH + COST * THETA)
    coefficient *= mp.log(real((1 - THETA) / THETA)) / real(COST)
    assert exact_balance_sign(1, THETA, HIGH, NASH) > 0
    assert exact_balance_sign(2, THETA, HIGH, NASH) < 0
    assert exact_balance_sign(1, THETA, HIGH, Q(3, 5)) == 0
    local = [tangent_certificate(n, e, kind) for n, e in brackets.items() for kind in ("L", "B")]
    finite = []
    for n, populations in ((1, (5, 8)), (2, (5, 8)), (3, (4, 5))):
        for population in populations:
            for share in (Q(3, 4), Q(9, 10)):
                for kind in ("L", "B"):
                    row = finite_chain(n, population, share, kind)
                    finite.append(row)
                    print(n, population, share, kind, row["welfare"][:17], flush=True)
    data = {
        "parameters": {
            "theta": str(THETA),
            "L": str(LOW),
            "H": str(HIGH),
            "cost": str(COST),
            "limiting_Nash_share": str(NASH),
        },
        "first_depth_above_Nash": 2,
        "limiting_n_times_one_minus_high_share": number(coefficient),
        "quota_crossings": grid,
        "high_branch_tangent_certificates": local,
        "general_parameter_bistability": bistability_witness(),
        "finite_chains": finite,
        "benchmark_depth_two_global_trap": certify_global_trap(),
        "benchmark_depth_two_order_bounds": certify_local_order_bounds(),
        "benchmark_depth_two_period_three": certify_cycle(),
        "response_polynomial_minimum_coefficients": {
            "productive": verify_log_derivative(10, Q(16, 9), 5),
            "unproductive": verify_log_derivative(31, Q(4, 3), 1),
        },
        "productive_jacobian_interval_cover": verify_productive_stability(),
        "low_jacobian_interval_cover": verify_low_stability(),
        "low_root_slope_grid": verify_low_grid(),
        "depth_three_trajectories": depth_three_trajectories(),
        "depth_three_below_Nash": depth_three_below_nash(),
        "old_efficient_share_at_depth_three": old_share_depth_three(),
        "depth_three_signed_response": depth_three_impulse_signs(),
        "precision": {
            "root_decimal_enclosure_width": "3e-84",
            "stationary_GTH_decimal_digits": 175,
            "stationary_certified_L1_error_less_than": "1e-84",
        },
    }
    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
