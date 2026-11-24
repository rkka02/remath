"""Exact period-two coexistence checks in characteristic coordinates (s, t).

Run with Python 3.9 or newer. Only the standard library is required.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction as Q


Point = tuple[Q, Q]
Wall = tuple[Point, ...]


def left(t: Q) -> Point:
    return abs(t) - 1, t


def cap_wall(a: Q, r: Q, n: Q, kappa: Q) -> Wall:
    """Right-hand vertices, from the lower tip to the upper tip."""
    assert 0 < r < a < 1 and 0 < n < 1 and 0 < kappa <= 1
    m = kappa * n
    d = 1 - (1 - n) * a
    c = d - (n - m) * r
    lower_join = (1 - c) / (1 - m)
    peak = (d - c) / (m + n)
    heights = (-Q(1), -lower_join, peak, a, Q(1))
    return tuple((min(1 - abs(t), c + m * t, d - n * t), t)
                 for t in heights)


def prescribed_wall(radii: list[Q], contractions: list[Q], a: Q) -> Wall:
    """Produce the minimum-side polygon having the given heights and rates."""
    roots = [Q(0), *radii, a]
    assert len(radii) == len(contractions) > 0 and a < 1
    assert all(lo < hi for lo, hi in zip(roots, roots[1:]))
    assert all(0 < rate < 1 for rate in contractions)
    magnitude = Q(1)
    slopes = [Q(2)]
    for i, rate in enumerate(contractions, 1):
        next_magnitude = magnitude / rate
        slopes.append((-1) ** i * (next_magnitude - magnitude))
        magnitude = next_magnitude
    outer_slope = magnitude + 2
    slopes.append((-1) ** (len(radii) + 1) * (outer_slope - magnitude))
    heights = [(d1 * r1 - d0 * r0) / (d1 - d0)
               for r0, r1, d0, d1 in zip(roots, roots[1:], slopes, slopes[1:])]
    heights.append(a)
    slopes.append(Q(0))
    jumps = [d1 - d0 for d0, d1 in zip(slopes, slopes[1:])]
    assert Q(1) + sum(jump for jump in jumps if jump > 0) == outer_slope
    corners = sorted(
        (-t if jump > 0 else t, abs(jump) / outer_slope)
        for t, jump in zip(heights, jumps)
    )
    wall = [(Q(0), -Q(1))]
    slope = Q(1)
    for t, slope_drop in corners:
        s0, t0 = wall[-1]
        wall.append((s0 + slope * (t - t0), t))
        slope -= slope_drop
        assert slope != 0
    s0, t0 = wall[-1]
    assert slope == -1 and s0 + slope * (1 - t0) == 0
    return tuple(wall + [(Q(0), Q(1))])


def right(wall: Wall, t: Q) -> Point:
    for (s0, t0), (s1, t1) in zip(wall, wall[1:]):
        if t0 <= t <= t1:
            return s0 + (s1 - s0) * (t - t0) / (t1 - t0), t
    raise ValueError("Height lies outside the tank")


def right_slope(wall: Wall, t: Q) -> Q:
    for (s0, t0), (s1, t1) in zip(wall, wall[1:]):
        if t0 < t < t1:
            return (s1 - s0) / (t1 - t0)
    raise ValueError("A wall slope requires an interior edge point")


def remove_neutral_edges(wall: Wall, last_radius: Q) -> Wall:
    """Continue the two faces after the last isolated root to the left V."""
    s = right(wall, last_radius)[0]
    below = right_slope(wall, -last_radius)
    above = right_slope(wall, last_radius)
    t_min = (-1 - s - below * last_radius) / (1 + below)
    t_max = (1 + s - above * last_radius) / (1 - above)
    inner_corners = tuple(point for point in wall if abs(point[1]) < last_radius)
    assert t_min < -last_radius < last_radius < t_max and -t_min != t_max
    return (left(t_min),) + inner_corners + (left(t_max),)


def slice_values(wall: Wall, coordinate: int, level: Q) -> list[Q]:
    """Independent intersections of a straight line with every polygon edge."""
    polygon = (left(Q(0)),) + wall
    transverse = 1 - coordinate
    hits = set()
    for p, q in zip(polygon, polygon[1:] + polygon[:1]):
        lo, hi = sorted((p[coordinate], q[coordinate]))
        assert lo != hi
        if lo <= level <= hi:
            alpha = (level - p[coordinate]) / (q[coordinate] - p[coordinate])
            hits.add(p[transverse] + alpha * (q[transverse] - p[transverse]))
    return sorted(hits)


def flip(wall: Wall, point: Point, coordinate: int) -> Point:
    hits = slice_values(wall, coordinate, point[coordinate])
    assert len(hits) in (1, 2) and point[1 - coordinate] in hits
    other = hits[-1] if point[1 - coordinate] == hits[0] else hits[0]
    return (point[0], other) if coordinate == 0 else (other, point[1])


def billiard(wall: Wall, point: Point) -> Point:
    return flip(wall, flip(wall, point, 1), 0)


def period_two_sets(wall: Wall) -> tuple[list[Q], list[tuple[Q, Q]]]:
    """Solve R(y) = R(-y) on the common interval of admissible half-heights."""
    last = min(-wall[0][1], wall[-1][1])
    knots = sorted({Q(0), last} | {abs(t) for _, t in wall if abs(t) < last})
    roots = set()
    intervals = []
    for lo, hi in zip(knots, knots[1:]):
        d0 = right(wall, lo)[0] - right(wall, -lo)[0]
        d1 = right(wall, hi)[0] - right(wall, -hi)[0]
        if d0 == d1 == 0:
            if intervals and intervals[-1][1] == lo:
                intervals[-1] = intervals[-1][0], hi
            else:
                intervals.append((lo, hi))
        elif d0 * d1 <= 0:
            roots.add(lo - d0 * (hi - lo) / (d1 - d0))
    isolated = sorted(y for y in roots if y > 0 and
                      all(y < lo or y > hi for lo, hi in intervals))
    return isolated, intervals


def check_loop(wall: Wall, r: Q) -> Q:
    """Check both orientations and the two affine full-return derivatives."""
    lower_left, upper_left = left(-r), left(r)
    lower_right, upper_right = right(wall, -r), right(wall, r)
    assert billiard(wall, lower_left) == upper_right
    assert billiard(wall, upper_right) == lower_left
    assert billiard(wall, upper_left) == lower_right
    assert billiard(wall, lower_right) == upper_left
    ratio = right_slope(wall, -r) / (-right_slope(wall, r))
    clearance = min(abs(r - knot) for knot in {Q(0)} | {abs(t) for _, t in wall})
    step = clearance / (8 * max(ratio, 1 / ratio))
    for sign, derivative in ((-1, ratio), (1, 1 / ratio)):
        start = left(sign * (r + step))
        end = billiard(wall, billiard(wall, start))
        assert end == left(sign * (r + derivative * step))
    return min(ratio, 1 / ratio)


def check_modes(wall: Wall, a: Q) -> None:
    """Integrate a polynomial mode's energy from the actual polygon slices."""
    def h(y: Q) -> Q:
        return max(Q(0), y - a) ** 2

    polygon = (left(Q(0)),) + wall
    for p, q in zip(polygon, polygon[1:] + polygon[:1]):
        for i in range(11):
            s, t = (p[j] + Q(i, 10) * (q[j] - p[j]) for j in (0, 1))
            assert h(1 - abs(s)) == h(abs(t))

    def energy_density(y: Q) -> Q:
        lengths = []
        for coordinate, level in ((0, y - 1), (0, 1 - y), (1, y), (1, -y)):
            hits = slice_values(wall, coordinate, level)
            lengths.append(hits[-1] - hits[0])
        assert lengths == [2 * y, 2 * y, 2 * (1 - y), 2 * (1 - y)]
        return 4 * (y - a) ** 2 * sum(lengths)

    # Simpson's rule is exact for each of the cubic slice terms.
    numerical = (1 - a) * (energy_density(a) + 4 * energy_density((1 + a) / 2)
                           + energy_density(Q(1))) / 6
    assert numerical == 16 * (1 - a) ** 3 / 3


def check_basins(wall: Wall, a: Q, r: Q, n: Q) -> None:
    """Check signs on all fixed-free gaps and both sides of each neutral end."""
    gaps = [
        (lambda t: right(wall, t), -a, -r, -1),
        (lambda t: right(wall, t), -r, r, 1),
        (lambda t: right(wall, t), r, a, -1),
        (left, -a, -r, 1),
        (left, -r, r, -1),
        (left, r, a, 1),
    ]
    for point, lo, hi, direction in gaps:
        t = (lo + hi) / 2
        end = billiard(wall, billiard(wall, point(t)))
        assert end == point(end[1]) and lo < end[1] < hi
        assert (end[1] - t) * direction > 0
    clearance = min(abs(a - abs(t)) for _, t in wall if abs(t) != a)
    e = clearance * n / 32
    for point, y, derivative in (
        (lambda y: right(wall, -y), a - e, n),
        (left, a - e, n),
        (lambda y: right(wall, y), a - e, 1 / n),
        (lambda y: left(-y), a - e, 1 / n),
    ):
        assert billiard(wall, billiard(wall, point(y))) == point(a + derivative * (y - a))
        assert billiard(wall, billiard(wall, point(a + e))) == point(a + e)


def run() -> dict:
    a, r, n = Q(3, 4), Q(1, 4), Q(2, 3)
    for kappa in (Q(1, 97), Q(1, 2), Q(96, 97)):
        wall = cap_wall(a, r, n, kappa)
        assert period_two_sets(wall) == ([r], [(a, Q(1))])
        assert right(wall, r)[0] == Q(7, 12)
        assert check_loop(wall, r) == kappa
        check_basins(wall, a, r, n)
        check_modes(wall, a)

    symmetric = cap_wall(a, r, n, Q(1))
    assert period_two_sets(symmetric) == ([], [(Q(0), Q(1))])
    d = 1 - (1 - n) * a

    def inner(y: Q) -> Q:
        return max(Q(0), y) * max(Q(0), a - y)

    for j in range(65):
        t = Q(j, 32) - 1
        for point in (left(t), right(symmetric, t)):
            assert billiard(symmetric, billiard(symmetric, point)) == point
            s = point[0]
            assert inner(1 + s) + inner((d - s) / n) == inner(abs(t))
    check_modes(symmetric, a)

    counts = (1, 2, 3, 5, 8, 13)
    for count in counts:
        heights = [(i + Q(1, 2)) * a / (count + 2) for i in range(1, count + 1)]
        rates = [Q(4 * i - 3, 4 * i + 1) for i in range(1, count + 1)]
        wall = prescribed_wall(heights, rates, a)
        assert len(wall) + 1 == count + 5
        roots, neutral = period_two_sets(wall)
        assert roots == heights and neutral == [(a, Q(1))]
        assert [check_loop(wall, y) for y in roots] == rates
        check_modes(wall, a)
        unrestricted = remove_neutral_edges(wall, heights[-1])
        assert len(unrestricted) + 1 == count + 3
        assert period_two_sets(unrestricted) == (heights, [])
        assert [check_loop(unrestricted, y) for y in heights] == rates

    heights = [Q(1, 100), Q(7, 12), Q(2, 3)]
    rates = [Q(16, 17), Q(1, 83), Q(7, 11)]
    independent = prescribed_wall(heights, rates, a)
    assert period_two_sets(independent) == (heights, [(a, Q(1))])
    assert [check_loop(independent, y) for y in heights] == rates
    check_modes(independent, a)

    with localcontext() as context:
        context.prec = 75
        exponent = -Decimal(2).ln() / 2
    return {
        "hexagon_vertices_st": [tuple(map(str, p)) for p in
                                (left(Q(0)),) + cap_wall(a, r, n, Q(1, 2))],
        "isolated_half_height": str(r),
        "neutral_half_heights": [str(a), "1"],
        "phase_fractions_neutral_interior_endpoint": [
            str(1 - a), str((a + r) / 2), str((a - r) / 2)
        ],
        "per_billiard_step_exponent": str(exponent),
        "sharp_examples_checked_k": [count + 5 for count in counts],
        "sharp_examples_without_cylinder_k": [count + 3 for count in counts],
        "independent_prescribed_radii_and_rates": [
            [str(y), str(rate)] for y, rate in zip(heights, rates)
        ],
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2))
