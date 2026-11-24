"""Exact checks of the canonical quadrilaterals using the original chord map."""

from fractions import Fraction as Q
from functools import lru_cache
from numbers import Integral


def _exact_rational(value):
    if isinstance(value, Q):
        return Q(int(value.numerator), int(value.denominator))
    if isinstance(value, Integral) and not isinstance(value, bool):
        return Q(int(value))
    if type(value).__module__ == "numpy" and getattr(value, "ndim", 1) == 0 and getattr(value, "dtype", None).kind in ("i", "u"):
        return Q(int(value))
    raise TypeError(f"ChessMap requires exact integer or Fraction inputs, got {type(value).__name__}")


def polygon(left_bottom, left_top, right_bottom, right_top, height=1):
    return tuple((_exact_rational(x), _exact_rational(z)) for x, z in [
        (left_bottom, 0), (left_top, height),
        (right_top, height), (right_bottom, 0),
    ])


class ChessMap:
    """Clockwise boundary length four, one unit of parameter per side."""

    def __init__(self, vertices, rising, falling=None):
        self.vertices = tuple((_exact_rational(x), _exact_rational(z)) for x, z in vertices)
        rising = _exact_rational(rising)
        falling = rising if falling is None else _exact_rational(falling)
        self.first = tuple(z - rising * x for x, z in self.vertices)
        self.second = tuple(z + falling * x for x, z in self.vertices)
        for heights in (self.first, self.second):
            assert all(heights[i] != heights[(i + 1) % 4] for i in range(4))

    @staticmethod
    def chord(t, heights):
        t = _exact_rational(t) % 4
        i = int(t)
        w = heights[i] + (t - i) * (heights[(i + 1) % 4] - heights[i])
        for j, low in enumerate(heights):
            high = heights[(j + 1) % 4]
            if min(low, high) <= w <= max(low, high):
                other = (j + (w - low) / (high - low)) % 4
                if other != t:
                    return other
        return t

    def forward(self, t):
        return self.chord(self.chord(t, self.first), self.second)

    def backward(self, t):
        return self.chord(self.chord(t, self.second), self.first)

    def displacement(self, t, period, turns):
        position = t
        for _ in range(period):
            next_point = self.forward(position)
            difference = (next_point - position) % 4
            assert difference, "The test domain must have transverse sides and no fixed vertex"
            position += difference
        return position - t - 4 * turns

    def branches(self, period):
        vertices = {Q(i) for i in range(4)}
        seeds = vertices | {self.chord(t, self.first) for t in vertices}
        seeds |= {self.backward(t) for t in vertices}
        knots = set()
        for _ in range(period):
            knots.update(seeds)
            seeds = {self.backward(t) for t in seeds}
        return sorted(knots | {Q(4)})

    def periodic_data(self, turns, period):
        knots = self.branches(period)
        differences = [self.displacement(t, period, turns) for t in knots]
        if all(value == 0 for value in differences):
            return True, {}
        roots = {}
        for x, y, dx, dy in zip(knots, knots[1:], differences, differences[1:]):
            if dx == dy:
                assert dx != 0, "A proper neutral interval occurs"
                continue
            t = x - dx * (y - x) / (dy - dx)
            if x <= t <= y:
                roots.setdefault(t % 4, set()).add(1 + (dy - dx) / (y - x))
        return False, roots


def check(chess, turns, period, multiplier):
    identity, roots = chess.periodic_data(turns, period)
    if multiplier == 1:
        assert identity
        return "global identity"
    assert not identity
    assert len(roots) == 2 * period, roots
    for slopes in roots.values():
        assert len(slopes) == 1
    assert {next(iter(slopes)) for slopes in roots.values()} == {multiplier, 1 / multiplier}
    return f"regular attracting multiplier {multiplier}"


def half_lift(a, displacement, t):
    integer = t // 1
    u = t - integer
    ratio = (1 - a) / a
    if u <= a:
        return integer + displacement + a + ratio * u
    return integer + displacement + 1 + (u - a) / ratio


def half_periodic(a, displacement, period, turns):
    breaks = {Q(0), a}
    tests = set()
    for _ in range(period):
        tests.update(breaks)
        # K_a is an involution modulo one, so (T_displacement K_a)^-1=K_a T_-displacement.
        breaks = {half_lift(a, 0, t - displacement) % 1 for t in breaks}
    tests = sorted(tests | {Q(1)})
    values = []
    for t in tests:
        v = t
        for _ in range(period):
            v = half_lift(a, displacement, v)
        values.append(v - t - turns)
    return min(values), max(values)


def dimension_certificate():
    """Upper-bound the length-three Hausdorff sum at t=9/10 for tilt >=15 degrees."""
    scale = 10**12
    cutoff = 24

    @lru_cache(None)
    def upper_weight(numerator, denominator):
        # Return ceil(scale * (numerator / denominator**2)**(9/10)) using integers.
        target = scale**10 * numerator**9
        factor = denominator**18
        lower, upper = 0, scale
        while upper - lower > 1:
            midpoint = (lower + upper) // 2
            if midpoint**10 * factor >= target:
                upper = midpoint
            else:
                lower = midpoint
        return upper

    positive = range(1, cutoff + 1)
    digits = tuple(positive) + tuple(-n for n in positive)
    triple_sum = 0
    for i in positive:
        for j in digits:
            for k in digits:
                denominator = abs(64 * i * j * k - 12 * i - 12 * k) - abs(16 * i * j - 3)
                # Simultaneous negation of all three digits preserves this denominator.
                triple_sum += 2 * upper_weight(27, denominator)
    finite = Q(2 * sum(upper_weight(3, 4 * n - 1) for n in positive), scale)
    end = 4 * cutoff - 1
    tail = Q(5 * end * upper_weight(3, end), 8 * scale)
    bound = Q(triple_sum, scale) + 3 * finite**2 * tail + 3 * finite * tail**2 + tail**3
    assert bound < Q(991, 1000)
    print(f"15-degree dimension certificate: t=9/10 bound {float(bound):.9f} (rounded), exactly < 991/1000")


def main():
    a = Q(1, 4)
    tables = {
        "upright": (polygon(0, 0, 1, 1), Q(1)),
        "right": (polygon(0, 0, 1 + a / 2, 1 - a / 2), Q(3, 5)),
        "isosceles": (polygon(-a / 2, a / 2, 1 + a / 2, 1 - a / 2), Q(1)),
        "shear": (polygon(-a / 2, a / 2, 1 - a / 2, 1 + a / 2), Q(9, 25)),
    }
    for name, (shape, multiplier) in tables.items():
        print(f"{name:10}  rho=1/2  {check(ChessMap(shape, Q(1)), 1, 2, multiplier)}")

    # 0<a<1/2 here is the normalized break position in the half map.
    # At a=1/4, the reciprocal branch slopes are 3 and 1/3.
    a = Q(1, 4)
    # h has lift rotation 2/3, 1, 3/2, 5/3, hence b has the indicated rotation.
    # The translations below are strictly inside their tongues or on finite-order curves.
    for displacement, p, q in [(Q(1, 8), 1, 4), (Q(1, 2), 1, 2),
                               (Q(1), 2, 3), (Q(9, 8), 7, 10)]:
        u, v = displacement / (1 - a), displacement / a
        chess = ChessMap(polygon(0, 0, 1, 1), u, v)
        multiplier = Q(1, 9) if q % 2 == 0 else Q(1)
        result = check(chess, p, q, multiplier)
        r = Q(q, 2 * (q - p))
        low, high = half_periodic(a, displacement, r.denominator, r.numerator)
        if q % 2:
            assert low == high == 0
        else:
            assert low < 0 < high
        print(f"u={u}, v={v}  rho={p}/{q}  {result}")

    # Checking the exact endpoints of the primary tongue on the same half map.
    for displacement in (a, 1 - a):
        low, high = half_periodic(a, displacement, 1, 1)
        assert (low == 0 < high) or (low < 0 == high)
        print(f"primary endpoint delta={displacement}  displacement range [{low}, {high}]")

    for a in (Q(1, 4), Q(3, 8)):
        b = 1 - a
        for k in range(1, 5):
            lower = a * b / (k - 1 + b)
            upper = a * b / (k - 1 + a)
            middle = (lower + upper) / 2
            for endpoint in (lower, upper):
                low, high = half_periodic(a, endpoint, 2 * k - 1, k)
                assert (low == 0 < high) or (low < 0 == high)
            chess = ChessMap(polygon(0, 0, 1, 1), middle / b, middle / a)
            check(chess, 1, 2 * k, (a / b) ** 2)
            neutral = a * b / k
            chess = ChessMap(polygon(0, 0, 1, 1), neutral / b, neutral / a)
            check(chess, 1, 2 * k + 1, Q(1))
        neutral = a * b / (1 - a * b)
        chess = ChessMap(polygon(0, 0, 1, 1), neutral / b, neutral / a)
        check(chess, 2, 5, Q(1))
        print(f"a={a}  checked both 1/(2k) endpoints and all 1/(2k+1) identities, k=1,...,4, and 2/5")
    dimension_certificate()


if __name__ == "__main__":
    main()
