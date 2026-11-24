"""Exact checks for the boundary and polyomino results in docs/phase1_pde.md."""

from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import atan, gcd, hypot, pi
from numbers import Integral


def reflect(levels, t):
    """Other point at this level of a linear projection on a convex polygon boundary.

    Each edge takes one unit of parameter. On a characteristic edge the
    midpoint extension interchanges its endpoints (no collinear subdivisions).
    Exact integer or Fraction inputs are required so boundary coincidences
    cannot suffer binary floating-point rounding.
    """
    exact_levels = []
    for v in levels:
        if isinstance(v, Q):
            exact_levels.append(Q(int(v.numerator), int(v.denominator)))
        elif isinstance(v, Integral) and not isinstance(v, bool):
            exact_levels.append(Q(int(v)))
        elif type(v).__module__ == "numpy" and getattr(v, "ndim", 1) == 0 and getattr(v, "dtype", None).kind in ("i", "u"):
            exact_levels.append(Q(int(v)))
        else:
            raise TypeError(f"reflect requires exact integer or Fraction levels, got {type(v).__name__}")
    levels = exact_levels
    if isinstance(t, Q):
        t = Q(int(t.numerator), int(t.denominator))
    elif isinstance(t, Integral) and not isinstance(t, bool):
        t = Q(int(t))
    elif type(t).__module__ == "numpy" and getattr(t, "ndim", 1) == 0 and getattr(t, "dtype", None).kind in ("i", "u"):
        t = Q(int(t))
    else:
        raise TypeError(f"reflect requires an exact integer or Fraction parameter, got {type(t).__name__}")
    n = len(levels)
    t %= n
    edge = int(t)
    height = levels[edge] + (t - edge) * (levels[(edge + 1) % n] - levels[edge])
    hits = set()
    for j, start in enumerate(levels):
        end = levels[(j + 1) % n]
        if start == end == height:
            return (2 * j + 1 - t) % n
        if start != end and min(start, end) <= height <= max(start, end):
            hits.add((j + (height - start) / (end - start)) % n)
    hits.remove(t)
    if hits:
        other, = hits
        return other
    return t


def walk(word, t):
    for levels in word:
        t = reflect(levels, t)
    return t


def periodic_set(word):
    """Partition the full boundary, then solve every affine fixed-point equation."""
    n = len(word[0])
    cuts = set()
    for k in range(len(word) + 1):
        for vertex in range(n):
            cuts.add(walk(reversed(word[:k]), Q(vertex)))
    ordered = sorted(cuts | {Q(n)})
    isolated = {cut for cut in cuts if walk(word, cut) == cut}
    intervals = []
    multipliers = {}
    for lo, hi in zip(ordered, ordered[1:]):
        x1, x2 = (2 * lo + hi) / 3, (lo + 2 * hi) / 3
        y1, y2 = walk(word, x1), walk(word, x2)
        slope = (y2 - y1) / (x2 - x1)
        if slope == 1:
            if x1 == y1:
                intervals.append((lo, hi))
        else:
            root = x1 + (y1 - x1) / (1 - slope)
            if lo < root < hi:
                assert walk(word, root) == root
                isolated.add(root)
                multipliers[root] = slope
    # A neutral cell contains every subdivision mark in its closure.
    # The last cell ends at n, the same boundary point as zero.
    isolated.difference_update(x % n for interval in intervals for x in interval)
    return ordered, sorted(isolated), intervals, multipliers


def check_tilted_square():
    # For tan(phi)=1/3 and physical angle pi/4, the two line slopes
    # in tank coordinates are 1/2 and -2. Vertices run counterclockwise
    # from (0,0) along the bottom, right, top, and left sides.
    up = tuple(map(Q, (0, -1, 1, 2)))     # 2z - x
    down = tuple(map(Q, (0, 2, 3, 1)))    # z + 2x
    word = [up, down] * 2
    cuts, fixed, intervals, multipliers = periodic_set(word)
    assert len(fixed) == 4 and not intervals
    assert all(walk(word[:2], t) != t for t in fixed)
    assert sorted(multipliers.values()) == [Q(1, 16), Q(1, 16), Q(16), Q(16)]
    print("Tilted square, tan(phi)=1/3, physical slopes ±1.")
    print("Exact affine cells of b²:", len(cuts) - 1)
    for t in fixed:
        print(f"  t={t}, b(t)={walk(word[:2], t)}, derivative of b²={multipliers[t]}")
    print("Fixed intervals:", intervals)


def check_characteristic_diamond():
    # In characteristic coordinates the diamond at its critical angle is
    # the unit square. Both involutions use their midpoint edge extensions.
    xi = tuple(map(Q, (0, 1, 1, 0)))
    eta = tuple(map(Q, (0, 0, 1, 1)))
    cuts, isolated, intervals, multipliers = periodic_set([xi, eta] * 2)
    assert sum(hi - lo for lo, hi in intervals) == 4
    assert len(cuts) == 5 and not isolated and not multipliers
    print("Critical diamond: midpoint extension gives b²=id on all four edges.")
    print("Each whole edge is characteristic, so its common trace is constant.")


def check_corner_cut():
    # A unit square with a half-unit chamfer at its northeast corner.
    polygon = ((0, 0), (1, 0), (1, Q(1, 2)), (Q(1, 2), 1), (0, 1))
    slope = Q(5, 8)
    xi = [z + slope * x for x, z in polygon]
    eta = [z - slope * x for x, z in polygon]
    _, fixed, intervals, multipliers = periodic_set([eta, xi] * 3)
    assert len(fixed) == 6 and not intervals
    expected = [Q(3, 13)] * 3 + [Q(13, 3)] * 3
    assert sorted(multipliers.values()) == expected
    assert all(walk([eta, xi], t) != t for t in fixed)
    print("Single corner cut at s=5/8: b³ has two cycles, multipliers 3/13 and 13/3.")


def check_sparse_tongue():
    leg = Q(1, 16)
    polygon = ((0, 0), (1, 0), (1, 1 - leg), (1 - leg, 1), (0, 1))

    def seventh_return(slope):
        xi = [z + slope * x for x, z in polygon]
        eta = [z - slope * x for x, z in polygon]
        return periodic_set([eta, xi] * 7)

    _, _, intervals, _ = seventh_return(Q(2, 5))
    assert intervals
    _, fixed, intervals, multipliers = seventh_return(Q(64, 159))
    assert len(fixed) == 14 and not intervals
    assert sorted(multipliers.values()) == [Q(95, 223)] * 7 + [Q(223, 95)] * 7
    _, fixed, intervals, _ = seventh_return(Q(32, 79))
    assert len(fixed) == 7 and not intervals
    _, fixed, intervals, _ = seventh_return(Q(13, 32))
    assert not fixed and not intervals
    print("1/16 corner cut: 2/5 plateau [2/5,32/79], interior multiplier 95/223.")


def check_chamfer_measures():
    # Finite-parameter sums use double precision. Limits use 75-digit arithmetic.
    for mesh in (32, 128, 512):
        count = 0
        frequency_measure = angle_fraction = 0.0
        for n in range(2, mesh):
            for m in range(1, min(n, mesh - n)):
                if gcd(m, n) != 1:
                    continue
                low = m / n
                high = m / (n - 1 / mesh)
                count += 1
                # The reciprocal slope contributes the other frequency branch.
                frequency_measure += (1 - low) / hypot(1, low) - (1 - high) / hypot(1, high)
                angle_fraction += 4 * (atan(high) - atan(low)) / pi
        print(f"  ε=1/{mesh}: {count} plateaus below s=1, "
              f"λ-measure={frequency_measure:.8f}, angular fraction={angle_fraction:.8f}")
    with localcontext() as ctx:
        ctx.prec = 75
        # Arithmetic-geometric mean iteration for pi.
        one = Decimal(1)
        a, b, correction, weight = one, one / Decimal(2).sqrt(), one / 4, one
        for _ in range(8):
            mean = (a + b) / 2
            correction -= weight * (a - mean) ** 2
            b = (a * b).sqrt()
            a = mean
            weight *= 2
        high_precision_pi = (a + b) ** 2 / (4 * correction)
        frequency_limit = 6 * (one - one / Decimal(2).sqrt()) / high_precision_pi**2
        angle_limit = (12 / high_precision_pi**3) * (high_precision_pi / 4 - Decimal(2).ln() / 2)
        print(f"  limiting λ-measure of certified plateaus: {frequency_limit:.65f}")
        print(f"  limiting angular fraction of certified plateaus: {angle_limit:.65f}")


def check_l_shape():
    # Three unit squares. All boundary edges lie on the integer grid.
    polygon = ((0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2))
    m, n = 3, 2
    for (x, z), (xx, zz) in zip(polygon, polygon[1:] + polygon[:1]):
        assert (x == xx and Q(m * x).denominator == 1) or (
            z == zz and Q(n * z).denominator == 1
        )
    value = Q(n**2, m**2 + n**2)
    assert (1 - value) * n**2 == value * m**2
    print(f"L triomino: sin({m}πx) sin({n}πz) has eigenvalue {value}.")


if __name__ == "__main__":
    check_tilted_square()
    check_characteristic_diamond()
    check_corner_cut()
    check_sparse_tongue()
    check_chamfer_measures()
    check_l_shape()
