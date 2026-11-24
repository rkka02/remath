"""Sharp cycle count, certified regular polygons and the octagon tilt limit.

The coordinates (u,v)=(z+s*x,z-s*x) preserve orientation. In these coordinates
the first reflection follows a horizontal chord and the second a vertical chord.
Only mpmath and the Python standard library are required.
"""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction as F
from itertools import combinations

from mpmath import iv, mp
from mpmath.libmp import to_rational


@dataclass
class Rectangle:
    edges: tuple
    left: object
    right: object
    lower: object
    upper: object
    edge_fractions: tuple
    multiplier_sw: object

    @property
    def attracting_multiplier(self):
        m = self.multiplier_sw
        if m < 1:
            return m
        assert m > 1
        return 1 / m


def _is_int_like(val):
    from numbers import Integral
    if isinstance(val, Integral) and not isinstance(val, bool):
        return True
    return type(val).__module__ == "numpy" and getattr(val, "ndim", 1) == 0 and getattr(val, "dtype", None).kind in ("i", "u")


def _normalize_coord(val):
    if isinstance(val, F):
        return F(int(val.numerator), int(val.denominator))
    if _is_int_like(val):
        return F(int(val))
    return val


def affine_edges(vertices):
    """Write each noncharacteristic edge in the form u=a+b*v."""
    edges = []
    converted = [(_normalize_coord(u), _normalize_coord(v)) for u, v in vertices]
    for (u, v), (next_u, next_v) in zip(converted, converted[1:] + converted[:1]):
        slope = (next_u - u) / (next_v - v)
        assert slope > 0 or slope < 0
        edges.append((u - slope * v, slope, v, next_v))
    return edges


def rectangle_on_edges(lines, indices):
    """Solve on the four given lines in SW, SE, NE, NW order."""
    e0, e1, e2, e3 = [lines[i] for i in indices]
    a0, b0 = e0[:2]
    a1, b1 = e1[:2]
    a2, b2 = e2[:2]
    a3, b3 = e3[:2]
    multiplier = (b1 * b3) / (b2 * b0)
    if multiplier == 1:
        return None  # Parallel affine equations give no isolated regular rectangle.
    upper_offset = (a1 - a2) / b2
    lower = ((a3 - a0) + b3 * upper_offset) / (b0 * (1 - multiplier))
    upper = upper_offset + (b1 / b2) * lower
    left, right = a0 + b0 * lower, a1 + b1 * lower
    if not (lower < upper and left < right):
        return None
    levels = (lower, lower, upper, upper)
    fractions = tuple((level - start) / (end - start)
                      for level, (_, _, start, end) in zip(levels, (e0, e1, e2, e3)))
    if not all(0 < fraction < 1 for fraction in fractions):
        return None
    assert multiplier > 0
    return Rectangle(indices, left, right, lower, upper, fractions, multiplier)


def rational_rectangles(vertices):
    """Enumerate regular hyperbolic rectangles in a transverse convex polygon."""
    exact = []
    for u, v in vertices:
        if not (isinstance(u, F) or _is_int_like(u)) or not (isinstance(v, F) or _is_int_like(v)):
            raise TypeError("rational_rectangles requires exact integer or Fraction vertices")
        exact.append((F(int(u.numerator), int(u.denominator)) if isinstance(u, F) else F(int(u)),
                      F(int(v.numerator), int(v.denominator)) if isinstance(v, F) else F(int(v))))
    vertices = exact
    double_area = sum(u*w-v*x for (u, v), (x, w) in
                      zip(vertices, vertices[1:]+vertices[:1]))
    if not double_area:
        raise ValueError("a polygon of positive area is required")
    for (u, v), (x, y) in zip(vertices, vertices[1:]+vertices[:1]):
        if any(((x-u)*(b-v) - (y-v)*(a-u))*double_area < 0 for a, b in vertices):
            raise ValueError("the edge itinerary test requires a convex polygon")
    lines = affine_edges(vertices)
    rectangles = []
    for subset in combinations(range(len(vertices)), 4):
        if double_area < 0:
            subset = subset[::-1]
        for shift in range(4):
            indices = subset[shift:] + subset[:shift]
            candidate = rectangle_on_edges(lines, indices)
            if candidate is not None:
                rectangles.append(candidate)
    return rectangles


def sharp_polygon(m):
    """Polygon with rational vertices, m+3 sides and m regular period-two attractors."""
    if m < 1:
        raise ValueError("The construction takes at least one attractor.")
    bends = [F((-1)**(j - 1) * (2*j - 1)) for j in range(1, m + 1)]
    height = F(10 * (m + 1)**2)

    def right(v):
        penalties = sum(max(F(0), v - a) if a > 0 else max(F(0), a - v)
                        for a in bends)
        return height + v/2 - 2 * penalties

    far = F(2 * m)
    slope_at_bottom = F(1, 2) + 2 * sum(a < 0 for a in bends)
    slope_at_top = F(1, 2) - 2 * sum(a > 0 for a in bends)
    bottom = -(right(-far) + far * slope_at_bottom) / (1 + slope_at_bottom)
    top = (right(far) - far * slope_at_top) / (1 - slope_at_top)
    assert bottom < -far < far < top
    assert right(bottom) == -bottom and right(top) == top
    return ([(-bottom, bottom)] + [(right(a), a) for a in sorted(bends)]
            + [(top, top), (F(0), F(0))])


def verify_sharp_family():
    for m in range(1, 9):
        vertices = sharp_polygon(m)
        assert len(vertices) == m + 3
        rectangles = sorted(rational_rectangles(vertices), key=lambda r: r.upper)
        assert len(rectangles) == m
        for j, r in enumerate(rectangles, start=1):
            assert (r.lower, r.upper, r.left) == (-2*j, 2*j, 2*j)
            assert r.attracting_multiplier == F(2*j - 1, 2*j + 1)
    print("Sharp rational family, k=4,...,11: all rectangles exhaustively verified.")


def regular_vertices(n, tilt_degrees, slope, ctx):
    tilt = ctx.mpf(tilt_degrees) * ctx.pi / 180
    s = ctx.mpf(slope)
    vertices = []
    for j in range(n):
        angle = ctx.pi/2 + tilt + 2 * ctx.pi * j/n
        x, z = ctx.cos(angle), ctx.sin(angle)
        vertices.append((z + s*x, z - s*x))
    return vertices


def show_interval(interval, digits=54):
    # Divide the exact binary endpoints directly at the display precision.
    # An intermediate decimal string could lose which side of a tie they lie on.
    with localcontext() as ctx:
        ctx.prec = digits
        ctx.rounding = ROUND_HALF_EVEN
        lower, upper = (ctx.divide(Decimal(n), Decimal(d))
                        for n, d in map(to_rational, interval._mpi_))
    if lower != upper:
        raise ValueError(f"interval endpoints round differently at {digits} digits")
    return str(lower)


def tilt_derivative(n, tilt, slope, rectangle):
    """Derivative with respect to physical tilt in radians at fixed slope."""
    tilt = iv.mpf(tilt) * iv.pi/180
    s = iv.mpf(slope)
    log_derivatives = []
    for j in rectangle.edges:
        alpha = iv.pi + tilt + (2*j + 1)*iv.pi/n
        si, co = iv.sin(alpha), iv.cos(alpha)
        log_derivatives.append((co - s*si)/(si + s*co) - (co + s*si)/(si - s*co))
    d0, d1, d2, d3 = log_derivatives
    derivative = (d1 + d3 - d0 - d2)/2
    return derivative if rectangle.multiplier_sw < 1 else -derivative


def certify_regular_examples():
    pentagon = [(2, 3, 0, 1), (2, 3, 4, 1)]
    hexagon = [(3, 4, 0, 1), (2, 4, 5, 1)]
    cases = [
        (5, "0", ".9", pentagon),
        (5, "5", ".9", pentagon),
        (6, "0", ".9", hexagon),
        (6, "5", ".9", hexagon),
        (8, "5", ".95", [(4, 5, 0, 1), (3, 5, 7, 1), (3, 6, 7, 2)]),
        (9, "0", ".98", [(5, 6, 0, 1), (4, 6, 0, 1), (4, 6, 0, 2),
                          (4, 6, 8, 2), (4, 7, 8, 2), (3, 7, 8, 2)]),
        (10, "0", ".95", [(5, 6, 0, 1), (5, 7, 0, 2),
                          (4, 7, 9, 2), (4, 8, 9, 3)]),
    ]
    for n, tilt, s, words in cases:
        lines = affine_edges(regular_vertices(n, tilt, s, iv))
        print(f"Regular {n}-gon, tilt={tilt} degrees from vertex-up, s={s}")
        for word in words:
            r = rectangle_on_edges(lines, word)
            assert r is not None
            m = r.attracting_multiplier
            exponent = iv.log(m)/2
            print(f"  {word}: {show_interval(exponent)}")
            if n == 5:
                print(f"    M = {show_interval(m)}")
                print(f"    dLambda/dphi = {show_interval(tilt_derivative(n, tilt, s, r))}")
                if tilt == "5":
                    print("    edge fractions =",
                          ", ".join(show_interval(value, 14) for value in r.edge_fractions))
    print("All listed edge fractions lie strictly inside (0,1).")


def verify_even_slice():
    """Compare the even-N radial formula against four independent chord equations."""
    for n in (4, 6, 8, 10, 12, 16, 32):
        for beta_weight in (F(1, 4), F(1, 2), F(3, 4)):
            weight = iv.mpf(beta_weight.numerator) / beta_weight.denominator
            beta = weight * iv.pi/n
            # A vertex angle of 45 degrees + beta in physical coordinates.
            physical_tilt = -45 + weight * 180/n
            lines = affine_edges(regular_vertices(n, physical_tilt, 1, iv))
            for j in range(1, n//2):
                positions = (n + j, -j, j, n - j)
                edge_word = tuple(((p - beta_weight)//2) % n for p in positions)
                r = rectangle_on_edges(lines, edge_word)
                assert r is not None
                t = j * iv.pi/n
                epsilon = beta if j % 2 else beta - iv.pi/n
                predicted = (iv.tan(t - epsilon)/iv.tan(t + epsilon))**2
                residual = r.multiplier_sw - predicted
                assert 0 in residual and residual.delta < iv.mpf("1e-65")
    cliff = -2*iv.log(1 + iv.sqrt(2))
    print("Even regular polygons, N=4,6,8,10,12,16,32: radial multipliers verified.")
    print("Octagon one-sided limiting per-step exponent =", show_interval(cliff))


def folded_normal_order(n, beta_weight):
    """Exact quadrant labels and edge indices, in increasing folded normal angle."""
    order = []
    half = F(n, 2)
    for edge in range(n):
        angle = (beta_weight + 2*edge + 1) % (2*n)
        if angle < half:
            folded, quadrant = angle, 2                  # NE
        elif angle < n:
            folded, quadrant = n - angle, 3              # NW
        elif angle < 3*half:
            folded, quadrant = angle - n, 0              # SW
        else:
            folded, quadrant = 2*n - angle, 1            # SE
        order.append((folded, quadrant, edge))
    return sorted(order)


def verify_odd_slice():
    for n in (5, 7, 9, 11, 15, 25, 51):
        for beta_weight in (F(1, 100), F(1, 10), F(1, 4), F(49, 100)):
            weight = iv.mpf(beta_weight.numerator) / beta_weight.denominator
            delta = iv.pi/n
            beta = weight * delta
            physical_tilt = -45 + weight * 180/n
            lines = affine_edges(regular_vertices(n, physical_tilt, 1, iv))
            normals = folded_normal_order(n, beta_weight)
            for start in range(n - 3):
                window = normals[start:start+4]
                edge_word = tuple(edge for _, _, edge
                                  in sorted(window, key=lambda entry: entry[1]))
                r = rectangle_on_edges(lines, edge_word)
                assert r is not None
                t = (2 + start)*delta/2
                if start % 2:
                    a, b = delta/2 + beta, delta/2 - beta
                else:
                    a, b = delta - beta, beta
                predicted = iv.tan(t-a)*iv.tan(t+b) / (iv.tan(t-b)*iv.tan(t+a))
                residual = r.attracting_multiplier - predicted
                assert 0 in residual and residual.delta < iv.mpf("1e-65")
    print("Odd regular polygons, N=5,7,9,11,15,25,51: all N-3 cycles verified.")


def main():
    mp.dps = 95
    iv.dps = 85
    verify_sharp_family()
    certify_regular_examples()
    verify_even_slice()
    verify_odd_slice()


if __name__ == "__main__":
    main()
