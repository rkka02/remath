"""Frozen B committors by positive elimination, with exact rational residual checks.

Each player independently declines a shallow flip with probability one half.
The optional hard calculation makes every shallow flip compulsory.  The finite
system and its certificates use the standard library.  The rate display uses
mpmath and the companion hard-wall calculation.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, MAX_EMAX, MIN_EMIN, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction

import mpmath as mp

from phase1_chain import dissection
from phase1_quadrant import rate as hard_rate


def mp_fraction(value):
    return mp.mpf(value.numerator) / value.denominator


def soft_rate(p, kappa, gamma):
    """Return route, rate per short barrier, and power at fixed aspect ratio."""
    q = 1 - p
    if kappa == -q / p:
        return 'unreachable', mp.inf, None
    if kappa == 1:
        exponent = mp_fraction(gamma) * mp.log(mp_fraction(p / q)) + mp_fraction(gamma-1) * mp.log(2)
        return 'synchronous', exponent, 0
    b = p * q * (1 - kappa)
    if b < q / 5 and (4 * p - 5 * b) * (q - 5 * b) > 16 * (p * q - b)**2:
        a, d = q - b, p - b
        A, D = a / 2 + 2 * b, b / 2 + 2 * d
        disc = 1 - 4 * A * D
        # At x=(1+sqrt(disc))/(2A), the sign of gamma*v_y-v_x is the
        # sign of u+v*sqrt(disc). Compare in Q, including critical equality.
        v = gamma * (a / 2 - 2 * b) - A
        u = v * (1 - 2 * A * D) + 2 * A**2 * (gamma * (b / 2 - 2 * d) + D)
        at_wall = (v >= 0 or u*u >= v*v*disc) if u >= 0 else (v > 0 and v*v*disc >= u*u)
        if at_wall:
            x = (1 + mp.sqrt(mp_fraction(disc))) / (2 * mp_fraction(A))
            return 'soft upper wall', mp_fraction(gamma) * mp.log(x) - mp.log(2), 0
    return hard_rate(str(p), str(kappa), gamma)


def rectangle(m, n, p, kappa, hard=False, first_flip=False):
    """Dirichlet rows for the corner excursion or the simultaneous first flip."""
    q = 1 - p
    b = p * q * (1 - kappa)
    steps = [(1, 1, q - b), (1, -1, b), (-1, 1, b), (-1, -1, p - b)]
    retention = Fraction(0) if hard else Fraction(1, 2)
    states = [(x, y) for x in range(m + 1) for y in range(n + 1)
              if first_flip or (x, y) != (m, n)]
    index = {state: i for i, state in enumerate(states)}
    success, failure = len(states), len(states) + 1
    rows = []
    for x, y in states:
        row = {}
        for dx, dy, mass in steps:
            if not mass:
                continue
            xx, yy = max(0, x + dx), max(0, y + dy)
            opportunities = int(xx > m) + int(yy > n)
            kept = mass * retention**opportunities
            dest = (min(m, xx), min(n, yy))
            if not first_flip and dest == (0, 0):
                j = failure
            elif not first_flip and dest == (m, n):
                j = success
            else:
                j = index[dest]
            if kept:
                row[j] = row.get(j, 0) + kept
            simultaneous = mass * (1 - retention)**2 if first_flip and opportunities == 2 else 0
            if simultaneous:
                row[success] = row.get(success, 0) + simultaneous
            failed = mass - kept - simultaneous
            if failed:
                row[failure] = row.get(failure, 0) + failed
        rows.append(row)
    return states, rows


def committors(states, original, exact=False):
    """Censor transient states using nonnegative operations, then back-substitute."""
    count = len(states)
    masses = {mass for row in original for mass in row.values()}
    weights = {mass: mass if exact else Decimal(mass.numerator) / Decimal(mass.denominator)
               for mass in masses}
    rows = [{j: weights[weight] for j, weight in row.items() if i != j}
            for i, row in enumerate(original)]
    incoming = [set() for _ in states]
    for i, row in enumerate(rows):
        for j in row:
            if j < count:
                incoming[j].add(i)
    order = dissection(states, set(range(1, count))) + [0]
    for k in order:
        total = sum(rows[k].values())
        normalized = {j: value / total for j, value in rows[k].items()}
        for j in normalized:
            if j < count:
                incoming[j].remove(k)
        for i in incoming[k]:
            row = rows[i]
            weight = row.pop(k)
            for j, probability in normalized.items():
                if i == j:
                    continue
                if j not in row:
                    row[j] = weight * probability
                    if j < count:
                        incoming[j].add(i)
                else:
                    row[j] += weight * probability
        incoming[k].clear()
        rows[k] = normalized
    value = [0] * count + [1, 0]
    for i in reversed(order):
        value[i] = sum(w * value[j] for j, w in rows[i].items())
    return value


def residual_radius(rows, values, m, d):
    """Exact absolute error bound from m consecutive joint rewards."""
    v = list(map(Fraction, values))
    residual = max(abs(sum(w * v[j] for j, w in row.items()) - v[i])
                   for i, row in enumerate(rows))
    return m * residual / d**m


def independent_constant(p, terms):
    """Enclose the leading constant with exact integer counts and a rational tail."""
    q = 1 - p
    base = 2 * p.denominator
    outward = 2 * p.numerator
    inward = base - outward
    hold = inward // 2
    counts = [1]
    total, denominator = 1, 1
    for _ in range(1, terms):
        following = [0] * (len(counts) + 1)
        following[0] = hold * counts[0]
        for x, mass in enumerate(counts):
            following[x + 1] += outward * mass
            if x:
                following[x - 1] += inward * mass
        counts = following
        total = total * base**2 + counts[0]**2
        denominator *= base**2
    partial = Fraction(total, denominator)
    R = 2 / (1 + 4 * p * q)
    generating = (1 + 4 * p * q) / p
    tail = generating**2 * R**(-2 * terms) / (1 - R**(-2))
    survival = (p - q) / (p - q / 2)
    return survival**2 / (partial + tail), survival**2 / partial


def display_enclosure(lower, upper, digits):
    """Round both rational endpoints outwards for display."""
    with localcontext() as ctx:
        ctx.prec = digits + 3
        ctx.rounding = ROUND_FLOOR
        lo = Decimal(lower.numerator) / Decimal(lower.denominator)
        ctx.rounding = ROUND_CEILING
        hi = Decimal(upper.numerator) / Decimal(upper.denominator)
        ctx.prec = 4
        relative = (upper - lower) / lower
        width = Decimal(relative.numerator) / Decimal(relative.denominator)
    print(f'    rational relative width <= {width}\n'
          f'    outward-displayed enclosure [{lo}, {hi}]', flush=True)


def check_small():
    """Exact one-barrier values, a synchronous overshoot, and both lower endpoints."""
    p = Fraction(7, 10)
    q = 1 - p
    b = p * q
    for m, n, kappa, hard, answer in [
        (1, 1, Fraction(0), False, q*q * (1 - b/2) / (1 - 3*b/2)),
        (1, 1, Fraction(0), True, q*q),
        (1, 1, Fraction(1), False, q),
        (2, 1, Fraction(1), False, q*q / 2),
        (2, 1, Fraction(1), True, 0),
        (3, 2, -q/p, False, 0),
        (3, 2, -q/p, True, 0),
    ]:
        states, rows = rectangle(m, n, p, kappa, hard)
        v = committors(states, rows, exact=True)
        assert v[0] == answer and residual_radius(rows, v, m, p-b*(1-kappa)) == 0
    for bound in (1, 3):
        states, rows = rectangle(bound, bound, p, Fraction(1), first_flip=True)
        assert committors(states, rows, exact=True)[0] == Fraction(1, 3)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--p', default='7/10')
    parser.add_argument('--kappa', default='181/189', help='rational value or min')
    parser.add_argument('--gamma', default='3', help='long/short barrier ratio, >= 1')
    parser.add_argument('--sizes', nargs='+', type=int, default=[10, 20, 40])
    parser.add_argument('--digits', type=int, default=70)
    parser.add_argument('--certify', type=int, default=0, metavar='N',
                        help='certify the stated digits at this short barrier')
    parser.add_argument('--compare-hard', action='store_true')
    parser.add_argument('--first-flip', action='store_true',
                        help='also solve for a simultaneous first flip over repeated excursions')
    parser.add_argument('--independent-terms', type=int, default=0, metavar='N',
                        help='also enclose the independent-feedback B constant with N terms')
    args = parser.parse_args()
    p, ratio = Fraction(args.p), Fraction(args.gamma)
    q = 1 - p
    if not Fraction(1, 2) < p < 1:
        parser.error('Require 1/2 < p < 1.')
    kappa = -q / p if args.kappa == 'min' else Fraction(args.kappa)
    if not -q / p <= kappa <= 1 or ratio < 1 or args.digits < 2:
        parser.error('Require feasible correlation, gamma >= 1, and at least two digits.')
    sizes = sorted(set(args.sizes + ([args.certify] if args.certify else [])))
    if min(sizes) < 1:
        parser.error('Both preflip barriers must be positive.')
    if args.independent_terms < 0:
        parser.error('The series length must be nonnegative.')
    mp.mp.dps = max(80, args.digits + 15)
    check_small()
    if args.independent_terms:
        lower, upper = independent_constant(p, args.independent_terms)
        print(f'B independent leading constant at p={p}, {args.independent_terms} terms')
        display_enclosure(lower, upper, args.digits)
    d = p - p * q * (1 - kappa)
    for hard in ([False, True] if args.compare_hard else [False]):
        def rate(gamma):
            if hard:
                return hard_rate(str(p), 'min' if kappa == -q/p else str(kappa), gamma)
            return soft_rate(p, kappa, gamma)

        route, exponent, power = rate(ratio)
        print(f"{'L' if hard else 'B'}  p={p}  kappa={kappa}  gamma={ratio}  "
              f'{route}  E={mp.nstr(exponent, 18)}  beta={power}', flush=True)
        for n in sizes:
            m = ratio.numerator * n // ratio.denominator
            _, local_exponent, _ = rate(Fraction(m, n))
            if mp.isinf(local_exponent):
                print(f'  ({m},{n})  h=0', flush=True)
                continue
            certify = n == args.certify
            extra = 0
            if certify:
                extra = max(0, int(mp.ceil((n * local_exponent - m * mp.log(mp_fraction(d)))
                                           / mp.log(10))))
            with localcontext() as ctx:
                ctx.prec = args.digits + extra + 15
                ctx.Emax, ctx.Emin = MAX_EMAX, MIN_EMIN
                states, rows = rectangle(m, n, p, kappa, hard)
                v = committors(states, rows)
                h = mp.mpf(str(v[0]))
                scaled = h * mp.exp(n * local_exponent) / mp.power(n, power or 0)
                print(f'  ({m},{n})  h={mp.nstr(h, 15)}  scaled={mp.nstr(scaled, 13)}',
                      flush=True)
                if certify:
                    radius = residual_radius(rows, v, m, d)
                    lower, upper = Fraction(v[0]) - radius, Fraction(v[0]) + radius
                    if lower <= 0 or 2 * radius / lower > Fraction(1, 10**args.digits):
                        raise ArithmeticError('Requested relative enclosure width was exceeded.')
                    display_enclosure(lower, upper, args.digits)
                if args.first_flip:
                    states, rows = rectangle(m, n, p, kappa, hard, first_flip=True)
                    simultaneous = mp.mpf(str(committors(states, rows)[0]))
                    print(f'    simultaneous first flip={mp.nstr(simultaneous, 15)}', flush=True)
                    if not hard and kappa == 1:
                        x = (q / (2 * p))**(m - n)
                        equivalent = (2*p - q)*x / (4*p - q + 2*(p - q)*x)
                        print(f'    finite / synchronous equivalent='
                              f'{mp.nstr(simultaneous / mp_fraction(equivalent), 13)}', flush=True)


if __name__ == '__main__':
    main()
