"""Exact checkerboard conjugacy and moving-gap checks for a fixed tilted square."""

from fractions import Fraction
from numbers import Integral

import mpmath as mp


def _normalize_exact(x):
    """Return a Python-int-backed Fraction if x is an exact integer/Fraction (incl. NumPy integer)."""
    if isinstance(x, Fraction):
        return Fraction(int(x.numerator), int(x.denominator))
    if isinstance(x, Integral) and not isinstance(x, bool):
        return Fraction(int(x))
    if type(x).__module__ == "numpy" and getattr(x, "ndim", 1) == 0 and getattr(getattr(x, "dtype", None), "kind", "") in ("i", "u"):
        return Fraction(int(x))
    return None


def floor_value(x):
    q = _normalize_exact(x)
    if q is not None:
        return q.numerator // q.denominator
    return int(mp.floor(x, prec=0))


def column_height(y, a, b):
    """Shoot across one column, accumulating the distance to each horizontal edge."""
    qs = tuple(_normalize_exact(x) for x in (y, a, b))
    if all(q is not None for q in qs):
        y, a, b = qs
        distance = Fraction(1)
    else:
        y, a, b = map(mp.mpmathify, (y, a, b))
        distance = mp.mpf(1)
    while distance > 0:
        row = floor_value(y)
        slope = a if row % 2 == 0 else b
        until_edge = (row + 1 - y) / slope
        if distance <= until_edge:
            return y + distance * slope
        y = row + 1
        distance -= until_edge
    raise AssertionError("A positive column must have an exit.")


def section_coordinate(y, a, b):
    qs = tuple(_normalize_exact(x) for x in (y, a, b))
    if all(q is not None for q in qs):
        y, a, b = qs
    else:
        y, a, b = map(mp.mpmathify, (y, a, b))
    turns = floor_value(y) // 2
    height = y - 2 * turns
    return turns + (a * min(height, 1) + b * max(height - 1, 0)) / (a + b)


def normal_return(z, a, b):
    qs = tuple(_normalize_exact(x) for x in (z, a, b))
    if all(q is not None for q in qs):
        z, a, b = qs
        turns = z.numerator // z.denominator
        fraction = z - turns
    else:
        z, a, b = map(mp.mpmathify, (z, a, b))
        turns = floor_value(z)
        fraction = z - turns
    if fraction <= a / (a + b):
        image = b * fraction / a
    else:
        image = 1 + a * (fraction - 1) / b
    return turns + image + b * (a - 1) / (a + b)


def check_exact_conjugacy():
    Q = Fraction
    samples = [(Q(1, 3), Q(3)), (Q(2, 7), Q(5, 9)),
               (Q(9, 8), Q(11, 7)), (Q(7, 3), Q(23, 3))]
    count = 0
    for a, b in samples:
        for numerator in range(-55, 81):
            y = Q(numerator, 17)
            endpoint = column_height(y, a, b) - 1
            assert section_coordinate(endpoint, a, b) == normal_return(
                section_coordinate(y, a, b), a, b
            )
            count += 1
    return count


def marked_endpoint(v, word, sign):
    """Return a cylinder endpoint and its derivative with respect to v."""
    length = 2 * mp.cosh(v)
    length_derivative = 2 * mp.sinh(v)
    x = sign * mp.exp(-v)
    derivative = -x
    for digit in reversed(word):
        denominator = digit * length + x
        derivative = (digit * length_derivative + derivative) / denominator**2
        x = -1 / denominator
        assert abs(derivative) <= abs(x) * (1 + 20 * mp.eps)
    return x, derivative


def physical_dilation(u, tilt, aspect):
    return mp.asinh(mp.tan(2 * tilt) * mp.cosh(u + mp.log(aspect)))


def crossing(word, sign, tilt, aspect):
    """Cross a positive marked endpoint with a fixed physical rectangle."""
    def displacement(u):
        dilation = physical_dilation(u, tilt, aspect)
        t, _ = marked_endpoint(dilation, word, sign)
        return u - mp.log(t)

    left, right = mp.mpf(-4), mp.mpf(1)
    assert displacement(left) < 0 < displacement(right)
    for _ in range(mp.mp.prec + 5):
        middle = (left + right) / 2
        if displacement(middle) < 0:
            left = middle
        else:
            right = middle
    return (left + right) / 2


def check_moving_gaps():
    tilt, aspect = mp.pi / 36, mp.mpf(1)
    print("5-degree square, alternating continued-fraction digits")
    print("depth | cylinder width in log(sqrt(ab)) | gap fraction")
    for depth in (1, 2, 4, 8, 12):
        word = tuple(-1 if i % 2 == 0 else 1 for i in range(depth))
        left = crossing(word, -1, tilt, aspect)
        right = crossing(word, 1, tilt, aspect)
        gap_left = crossing(word + (1,), 1, tilt, aspect)
        gap_right = crossing(word + (2,), -1, tilt, aspect)
        assert left < gap_left < gap_right < right
        middle = (gap_left + gap_right) / 2
        v = physical_dilation(middle, tilt, aspect)
        frozen = [mp.log(marked_endpoint(v, digits, sign)[0])
                  for digits, sign in ((word, -1), (word, 1),
                                       (word + (1,), 1), (word + (2,), -1))]
        # On the interval, |dv/du| is largest at the endpoint furthest from zero.
        farthest = max(abs(left), abs(right))
        kappa = (mp.tan(2 * tilt) * mp.sinh(farthest)
                 / mp.sqrt(1 + (mp.tan(2 * tilt) * mp.cosh(farthest))**2))
        full_width, gap_width = right - left, gap_right - gap_left
        for frozen_width, width in ((frozen[1] - frozen[0], full_width),
                                    (frozen[3] - frozen[2], gap_width)):
            assert (1 - kappa) * width <= frozen_width <= (1 + kappa) * width
        print(depth, mp.nstr(full_width, 20), mp.nstr(gap_width / full_width, 20),
              sep=" | ")


if __name__ == "__main__":
    mp.mp.dps = 80
    print(f"Exact conjugacy at {check_exact_conjugacy()} rational slope and initial-height combinations.")
    check_moving_gaps()
