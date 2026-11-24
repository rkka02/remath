"""Exact certificates for local stability on both physical quorum branches.

The productive proof covers the cooperation interval [1/4, 1/2] at depths 2–15.
The low-branch proof covers all eligible shares at depths 2–28. Both use the
cumulative-tail Jacobian in phase2b_quorum_memory.md. The note proves local
stability analytically at the remaining depths.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt


COST = Q(3, 5)
HIGH = Q(97, 100)
LOW = Q(4, 5)
QUOTA = Q(1, 4)


@dataclass(frozen=True)
class Interval:
    """Closed intervals with exact rational endpoints."""

    low: Q
    high: Q

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.low + other.low, self.high + other.high)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __mul__(self, other):
        other = as_interval(other)
        products = (self.low * other.low, self.low * other.high,
                    self.high * other.low, self.high * other.high)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert other.low > 0
        return self * Interval(1 / other.high, 1 / other.low)

    def __pow__(self, exponent):
        assert self.low >= 0 and exponent >= 0
        return Interval(self.low ** exponent, self.high ** exponent)

    def square(self):
        maximum = max(self.low ** 2, self.high ** 2)
        minimum = max(0, self.low, -self.high) ** 2
        return Interval(minimum, maximum)


def as_interval(number):
    if isinstance(number, Interval):
        return number
    value = Q(number)
    return Interval(value, value)


def sqrt_upper(value):
    """An upward-rounded square root of a nonnegative rational."""
    scale = 1 << 256
    return Q(isqrt((scale ** 2 * value.numerator) // value.denominator) + 1, scale)


def duration(n, payoff):
    loss = 1 - payoff
    if payoff == loss:
        return Q(2 * n)
    return ((payoff / loss) ** n - 1) / (payoff - loss)


@lru_cache(maxsize=None)
def payoff_gap(n, cooperation):
    """Enclose d = c(1-alpha) at this physical root by exact rational bisection."""
    if cooperation == Q(1, 2):
        return as_interval(0)
    low, high = Q(0), COST
    mean = HIGH - COST * cooperation
    for _ in range(52):
        trial = (low + high) / 2
        product_c = (1 - cooperation) * duration(n, mean - (1 - cooperation) * trial)
        product_d = cooperation * duration(n, mean + cooperation * trial)
        if product_c < product_d:
            high = trial
        else:
            low = trial
    return Interval(low, high)


@dataclass(frozen=True)
class Side:
    loss: Interval
    payoff: Interval
    mass: Interval
    weakest: Interval


def frozen_sides(n, left, right):
    x = Interval(left, right)
    # The implicit derivative d'(x) is negative on the productive curve.
    gap = Interval(payoff_gap(n, right).low, payoff_gap(n, left).high)
    shared_cost = COST - gap
    defector_loss = 1 - HIGH + shared_cost * x
    sides = []
    for loss, mass in ((defector_loss, 1 - x), (defector_loss + gap, x)):
        payoff = 1 - loss
        ratio = loss / payoff
        normalization = sum(ratio ** j for j in range(n))
        weakest = mass * ratio ** (n - 1) / normalization
        sides.append(Side(loss, payoff, mass, weakest))
    return shared_cost, sides


@lru_cache(maxsize=None)
def clipped_low_root(n, shared_cost):
    """Enclose the low root, capped at the quota when its branch has ended."""
    gap = COST - shared_cost

    def balance(x):
        defect = LOW - shared_cost * x
        return (1 - x) * duration(n, defect - gap) - x * duration(n, defect)

    if balance(QUOTA) >= 0:
        return as_interval(QUOTA)
    if shared_cost == 0:
        coop = duration(n, LOW - COST)
        return as_interval(coop / (coop + duration(n, LOW)))
    left, right = Q(0), QUOTA
    for _ in range(58):
        middle = (left + right) / 2
        if balance(middle) > 0:
            left = middle
        else:
            right = middle
    return Interval(left, right)


def frozen_low_sides(n, left, right):
    low = clipped_low_root(n, left).low
    if low == QUOTA:
        return None  # The physical low branch requires strict x < QUOTA.
    x = Interval(low, clipped_low_root(n, right).high)
    shared_cost = Interval(left, right)
    loss_d = 1 - LOW + shared_cost * x
    loss_c = 1 - LOW + COST - shared_cost * (1 - x)
    ratio = loss_d / (1 - loss_d)
    weak_d = (1 - x) * ratio ** (n - 1) / sum(ratio ** j for j in range(n))
    # Interface stationarity holds even when the cooperative depth drift is outward.
    weak_c = weak_d * loss_d / loss_c
    return shared_cost, [Side(loss_d, 1 - loss_d, 1 - x, weak_d),
                         Side(loss_c, 1 - loss_c, x, weak_c)]


def cosine_upper(denominator):
    # 3.14 < pi; the fourth-order cosine Taylor polynomial bounds cos from above.
    argument = Q(314, 100 * denominator)
    return 1 - argument ** 2 / 2 + argument ** 4 / 24


def reward_variance_upper(payoff):
    if payoff.low <= Q(1, 2) <= payoff.high:
        return Q(1, 4)
    return max(payoff.low * (1 - payoff.low), payoff.high * (1 - payoff.high))


def separated_spectrum(n, switch, shared_cost, sides, low_branch):
    """Separate the single slow eigenvalue from both ends of the fast spectrum."""
    defect, coop = sides
    center = switch * shared_cost * (defect.weakest - coop.weakest)
    norm_squared = center.square()
    leakage = as_interval(0)
    weight = as_interval(1)
    for side in sides:
        ratio = side.loss / side.payoff
        norm_squared += (switch * shared_cost ** 2 * side.weakest
                         * (side.mass - side.weakest) / side.payoff ** 2)
        leakage += switch * side.loss * ratio ** (n - 1)
        weight += switch * sum(ratio ** j for j in range(1, n))
    perturbation = sqrt_upper(norm_squared.high)
    top_lower = (1 - leakage / weight).low
    if low_branch:
        variance = max(reward_variance_upper(side.payoff) for side in sides)
    else:
        variance = (coop.payoff * coop.loss).high
    coupling = 2 * sqrt_upper(variance)
    second_upper = coupling * cosine_upper(n)
    negative_radius = coupling * cosine_upper(2 * n)
    isolated = second_upper + 2 * perturbation < top_lower
    # If the top frozen eigenvalue is at most 1-delta, only +1 could touch.
    # Otherwise 3*delta < 1-lambda_2 guarantees isolation of its real outlier.
    small_perturbation = low_branch and second_upper + 3 * perturbation < 1
    return negative_radius + perturbation < 1 and (isolated or small_perturbation)


def signed_eigenvalue_brackets(n, switch, shared_cost, sides):
    """Count 2n-1 sign changes of the characteristic polynomial inside [-1,1]."""
    defect, coop = sides
    center = 1 - switch * (defect.loss + coop.loss)
    center += switch * shared_cost * (defect.weakest - coop.weakest)
    flanks = []
    for direction, side in zip((1, -1), sides):
        response = direction * shared_cost * side.weakest / side.loss
        column = [response * side.payoff ** j for j in range(n - 1)]
        column[0] += side.payoff
        flanks.append((side.payoff * side.loss, switch * side.loss, column))

    changes = 0
    previous = 0
    for grid_point in range(-48, 48):
        z = Q(grid_point, 48)
        determinants, terms = [], []
        for walk_product, entry, column in flanks:
            # Leading principal determinants of zI minus a Dirichlet flank.
            minor = [as_interval(1), as_interval(z)]
            for _ in range(2, n):
                minor.append(z * minor[-1] - walk_product * minor[-2])
            determinants.append(minor[n - 1])
            terms.append(entry * sum(v * m for v, m in zip(column, minor[n - 2::-1])))
        d_defect, d_coop = determinants
        at_z = (z - center) * d_defect * d_coop - terms[0] * d_coop - terms[1] * d_defect
        sign = int(at_z.low > 0) - int(at_z.high < 0)
        if sign:
            changes += int(previous == -sign)
            previous = sign
    # P(1) = det(I-A)*(1-F') is strictly positive throughout by the scalar proof.
    changes += int(previous == -1)
    return changes == 2 * n - 1


def verify_curve(parameter_range, max_depth, max_sign_depth, low_branch):
    result = {}
    for n in range(2, max_depth + 1):
        pending = [(*parameter_range, 0)]
        disk_count = sign_count = deepest = 0
        while pending:
            left, right, depth = pending.pop()
            box = frozen_low_sides(n, left, right) if low_branch else frozen_sides(n, left, right)
            if box is None:
                continue
            shared_cost, sides = box
            methods = []
            for switch in (Q(1), Q(1, 2)):
                if separated_spectrum(n, switch, shared_cost, sides, low_branch):
                    methods.append('disk')
                elif n <= max_sign_depth and signed_eigenvalue_brackets(n, switch, shared_cost, sides):
                    methods.append('sign')
            if len(methods) == 2:
                disk_count += methods.count('disk')
                sign_count += methods.count('sign')
                deepest = max(deepest, depth)
                continue
            if depth >= 14:
                raise ArithmeticError(f'Unverified interval at depth {n}: {left} to {right}')
            middle = (left + right) / 2
            pending.extend([(left, middle, depth + 1), (middle, right, depth + 1)])
        result[n] = {'spectral_disks': disk_count, 'polynomial_signs': sign_count,
                     'dyadic_subdivision_depth': deepest}
    return result


def verify_productive_stability():
    """Certify every physical high root, including its smooth continuation at equality."""
    return verify_curve((QUOTA, Q(1, 2)), 15, 5, low_branch=False)


def verify_low_stability():
    """Certify every physical low root at fixed shared cost c*alpha."""
    return verify_curve((Q(0), COST), 28, 8, low_branch=True)


if __name__ == '__main__':
    import json
    print(json.dumps({'productive': verify_productive_stability(),
                      'low': verify_low_stability()}, indent=2))
