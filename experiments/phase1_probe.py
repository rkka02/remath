"""Project ReMath, phase 1. Run with Python 3, mpmath, and NumPy."""

from itertools import product

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss


mp.mp.dps = 65
I = mp.j
TWO_PI = 2 * mp.pi
HALF = mp.mpf("0.5")
SQUARE = [(-1-I)/2, (1-I)/2, (1+I)/2, (-1+I)/2]
DIRECTIONS = (1, I, -1, -I)
TEST_POINT = mp.mpc("0.17", "0.13")
TEST_RATE = mp.mpc("0.7", "-0.35")
OFF_GRID = mp.mpc("1.0", "0.4")


def fmt(x):
    return mp.nstr(x, 9)


def sinhc(x):
    return mp.sinh(x) / x if x else mp.mpf(1)


def square_symbol(s):
    return sinhc(s/2) * sinhc(I*s/2)


def square_inverse_derivative(m):
    return (-1)**m * (TWO_PI*m)**2 / (2*mp.sinh(mp.pi*m))


def square_sums(z, n):
    ghosts = [mp.mpc(0) for _ in DIRECTIONS]
    plane_wave = mp.mpc(0)
    erased_constant = mp.mpc(0)
    largest_erased = mp.mpf(0)
    factor = square_symbol(TEST_RATE)
    for m in range(1, n+1):
        weight = square_inverse_derivative(m)
        for j, direction in enumerate(DIRECTIONS):
            node = direction * TWO_PI * m
            residue = direction * weight
            wave = mp.exp(node*z)
            ghosts[j] += residue * wave
            plane_wave += factor * residue * wave / (TEST_RATE-node)
            # Entire in s, including at zero. Its only zeros are 2*pi*k**2.
            mask = mp.sinc(mp.pi * mp.sqrt(node / TWO_PI))
            coefficient = -mask * residue / node
            erased_constant += coefficient * wave
            if j == 0 and int(mp.sqrt(m))**2 == m:
                largest_erased = max(largest_erased, abs(coefficient))
    return ghosts, plane_wave, erased_constant, largest_erased


def continued_ghost(w, n=35):
    terms = []
    for k in range(n):
        q = -mp.exp(TWO_PI*(w-k-HALF))
        terms.append(q*(1+q)/(1-q)**3)
    return TWO_PI**2 * mp.fsum(terms)


def test_square_series():
    print("Square: N, |ghost sum|, |plane wave error|, |square-index erasure error|")
    for n in (4, 8, 16, 32, 56):
        ghosts, wave, erased, largest = square_sums(TEST_POINT, n)
        errors = [abs(sum(ghosts)), abs(wave-mp.exp(TEST_RATE*TEST_POINT)), abs(erased-1)]
        print(n, *(fmt(e) for e in errors))
    print("edge waves:", *(fmt(z) for z in ghosts))
    print("largest absolute erased coefficient:", fmt(largest))
    assert max(errors) < mp.mpf("1e-44") and largest < mp.mpf("1e-60")

    inside = continued_ghost(TEST_POINT)
    outside = mp.mpc("0.71", "0.17")
    exterior_sum = sum(d*continued_ghost(d*outside) for d in DIRECTIONS)
    print("Lambert check inside, continued sum outside:",
          fmt(abs(inside-ghosts[0])), fmt(abs(exterior_sum)))
    print("outside |m=40 term on divergent ray|:",
          fmt(abs(square_inverse_derivative(40)*mp.exp(TWO_PI*40*outside))))
    assert abs(inside-ghosts[0]) < mp.mpf("1e-44") and abs(exterior_sum) < mp.mpf("1e-57")

    shift = mp.mpc("0.2", "-0.1")
    print("Translated square: support estimates in directions 1,i,-1,-i")
    for m in (32, 256, 2048):
        r = TWO_PI*m
        base = mp.log(abs(square_inverse_derivative(m)))
        print(m, *(fmt(mp.re(d*shift)-base/r) for d in DIRECTIONS))


def test_continuous_bridge():
    """Composite Gauss quadrature on four outward rays, in ordinary double precision."""
    points, weights = leggauss(24)
    target_node = 2*np.pi
    inverse_derivative = float(square_inverse_derivative(1))
    a = complex(TEST_RATE)
    exact = complex(square_symbol(TEST_RATE))*inverse_derivative/(a-target_node)
    vertices = np.array(SQUARE, dtype=complex)
    print("Continuous-to-discrete coefficient: exact", fmt(exact))
    for panels in (4, 8, 16, 32, 64):
        # An interior Gauss rule avoids evaluation of removable quotients at nodes.
        radii = (np.pi*(2*np.arange(panels)[:, None]+1+points)).ravel()
        coeff = 0j
        for left, right in zip(vertices, np.roll(vertices, -1)):
            edge = right-left
            direction = 1j/edge  # These four edges have length one.
            s = direction*radii
            symbol = 4*np.sinh(s/2)*np.sin(s/2)/s**2
            trace = np.exp((a-s)*left)*np.expm1((a-s)*edge)/(a-s)
            integrand = (symbol*trace/(s-target_node)).reshape(panels, -1)
            coeff += direction*np.pi*np.sum(integrand@weights)
        coeff *= inverse_derivative/(2j*np.pi)
        print(panels, f"{abs(coeff-exact):.9g}")
    assert abs(coeff-exact) < 1e-7


def test_triangle():
    omega = mp.exp(2*mp.pi*I/3)
    b = 1/(TWO_PI*I)
    rotations = (1, omega, omega**2)
    symbol = mp.fprod(mp.rgamma(1-b*d*TEST_RATE) for d in rotations)
    z = mp.mpc("0.10", "0.12")
    ghost = mp.mpc(0)
    wave = mp.mpc(0)
    print("Equilateral triangle, full integer rays: N, |ghost sum|, |plane wave error|")
    for m in range(1, 81):
        first = m/b
        deriv = (-1)**m*b*mp.factorial(m-1)
        deriv *= mp.rgamma(1-omega*m)*mp.rgamma(1-omega**2*m)
        for d in rotations:
            node = d*first
            term = d*mp.exp(node*z)/deriv
            ghost += term
            wave += term*symbol/(TEST_RATE-node)
        if m in (8, 16, 32, 64, 80):
            print(m, fmt(abs(ghost)), fmt(abs(wave-mp.exp(TEST_RATE*z))))
    assert abs(ghost) < mp.mpf("1e-26") and abs(wave-mp.exp(TEST_RATE*z)) < mp.mpf("1e-29")


def square_boundary_transform(s, density):
    """Integrate the spatial density directly; ds here is positive arclength."""
    result = mp.mpc(0)
    for left, right in zip(SQUARE, SQUARE[1:]+SQUARE[:1]):
        edge = right-left
        normal = -I*edge/abs(edge)
        result += abs(edge)*mp.quad(
            lambda t: mp.exp(s*(left+edge*t))*density(left+edge*t, normal), [0, 1])
    return result


def torsion_transform(s, cutoff):
    """Truncate the independent sine-series solution of -Laplacian u = 1."""
    total = mp.mpc(0)
    for left, right in zip(SQUARE, SQUARE[1:]+SQUARE[:1]):
        b = s*(right-left)
        # Integral from 0 to 1 of exp(b*t)*sin(n*pi*t), for odd n.
        terms = []
        for n in range(1, cutoff+1, 2):
            k = n*mp.pi
            sine_integral = k*(1+mp.exp(b))/(b*b+k*k)
            terms.append(4*mp.tanh(k/2)*sine_integral/(k*k))
        total += mp.exp(s*left)*mp.fsum(terms)
    return total


def test_square_flux():
    nx = lambda w, normal: normal.real
    nodes = [d*TWO_PI*m for d in DIRECTIONS for m in range(1, 7)]
    h = lambda s: (abs(s.real)+abs(s.imag))/2
    defect = max(abs(square_boundary_transform(s, nx))*mp.exp(-h(s)) for s in nodes)
    off = square_boundary_transform(OFF_GRID, nx)
    print("Square n_x: scaled sampled maximum, off-grid transform, |off-grid error|:",
          fmt(defect), fmt(off), fmt(abs(off-OFF_GRID*square_symbol(OFF_GRID))))
    # The first boundary moment is integral(w*n_x dl), independent of spectral formula.
    moment = square_boundary_transform(0, lambda w, normal: w*normal.real)
    print("n_x first moment, total flux:", fmt(moment), fmt(square_boundary_transform(0, nx)))
    assert defect < mp.mpf("1e-60") and abs(moment-1) < mp.eps*100
    assert abs(off-OFF_GRID*square_symbol(OFF_GRID)) < mp.mpf("1e-60")

    print("Torsion flux: largest odd sine mode, mass error, scaled node error, off-grid error")
    for n in (15, 63, 255, 511):
        print(n, fmt(abs(torsion_transform(0, n)-1)),
              fmt(abs(torsion_transform(TWO_PI, n))*mp.exp(-mp.pi)),
              fmt(abs(torsion_transform(OFF_GRID, n)-square_symbol(OFF_GRID))))
    assert abs(torsion_transform(OFF_GRID, n)-square_symbol(OFF_GRID)) < mp.mpf("4e-6")

    signs = (1, -1, 1, -1)
    atom = lambda s: mp.fsum(c*mp.exp(s*w) for c, w in zip(signs, SQUARE))
    assert abs(atom(OFF_GRID)-I*OFF_GRID**2*square_symbol(OFF_GRID)) < mp.mpf("1e-60")
    print("Square alternating corners, moments 0,1,2:",
          *(fmt(sum(c*w**k for c, w in zip(signs, SQUARE))) for k in range(3)))
    print("Square alternating corners, phase-corrected half-step samples at m=0,1,5:")
    for m in (0, 1, 5):
        u = TWO_PI*(m+HALF)
        shifted = mp.exp(-I*u*SQUARE[0])*atom(I*u)
        print(m, fmt(shifted.real))
        assert abs(shifted-2*(1-mp.exp(-u))) < mp.mpf("1e-60")


def test_hexagon():
    directions = (mp.mpf(1), mp.mpc("0.4", "0.8"), mp.mpc("-0.3", "0.9"))
    knots = [(sum(sign*d/2 for sign, d in zip(signs, directions)), mp.fprod(signs))
             for signs in product((-1, 1), repeat=3)]
    transform = lambda s: mp.fsum(weight*mp.exp(s*w) for w, weight in knots)
    nodes = [TWO_PI*I*m/d for d in directions for m in range(-6, 7) if m]
    error = max(abs(transform(s))*mp.exp(-sum(abs(mp.re(s*d))/2 for d in directions))
                for s in nodes)
    s = OFF_GRID
    expected = mp.fprod(directions)*s**3*mp.fprod(sinhc(s*d/2) for d in directions)
    moments = [mp.fsum(weight*w**j for w, weight in knots) for j in range(4)]
    print("Skew hexagon: scaled node error, off-grid magnitude, product error:",
          fmt(error), fmt(abs(transform(s))), fmt(abs(transform(s)-expected)))
    print("Hexagon signed-knot moments 0..3:", *(fmt(m) for m in moments))
    assert error < mp.mpf("1e-60") and abs(transform(s)-expected) < mp.mpf("1e-60")
    assert max(abs(m) for m in moments[:3]) < mp.mpf("1e-60")
    assert abs(moments[3]-6*mp.fprod(directions)) < mp.mpf("1e-60")


def test_corner_layers():
    # Replace each signed corner atom by unit mass on a short outgoing side segment.
    signs = (1, -1, 1, -1)
    m = 12
    s = TWO_PI*I*m
    print("Corner layers: kappa, |boundary sample| after scaling, |limiting profile|, difference")
    for kappa in map(mp.mpf, ("0.01", "0.1", "1", "3", "10", "40")):
        width = kappa/(TWO_PI*m)
        sample = mp.mpc(0)
        for j, (w, sign) in enumerate(zip(SQUARE, signs)):
            tangent = SQUARE[(j+1) % 4]-w
            sample += sign*mp.quad(lambda t: mp.exp(s*(w+t*width*tangent)), [0, 1])
        sample *= (-1)**m*mp.exp(-mp.pi*m)
        profile = mp.expm1(I*kappa)/(I*kappa) - mp.expm1(-kappa)/(-kappa)
        top = mp.expm1(-I*kappa)/(-I*kappa) - mp.expm1(kappa)/kappa
        assert abs(sample-profile-mp.exp(-TWO_PI*m)*top) < mp.mpf("1e-60")
        print(fmt(kappa), fmt(abs(sample)), fmt(abs(profile)), fmt(abs(sample-profile)))


def test_corner_recovery():
    """Endpoint-pair averages for a scalene triangle with unit arclength background."""
    vertices = np.array([0, 1.5+0.1j, 0.2+1.1j])
    edges = np.roll(vertices, -1)-vertices
    charges = np.array([2., -1., 3.])
    print("Triangle corner recovery: cutoff, estimates (real parts), max complex error")
    for n in (16, 64, 256, 1024):
        means = []
        for start, edge in zip(vertices, edges):
            nodes = 2j*np.pi*np.arange(1, n+1)/edge
            phase = np.exp(nodes[:, None]*(vertices-start))
            atoms = phase@charges
            # Integrate the diffuse density 1 exactly along each straight side.
            integrals = (np.roll(phase, -1, axis=1)-phase)/(nodes[:, None]*edges)
            means.append(np.mean(atoms+integrals@np.abs(edges)))
        means = np.array(means)
        recovered = (means-np.roll(means, -1)+np.roll(means, -2))/2
        error = np.max(np.abs(recovered-charges))
        print(n, *(f"{z.real:.8f}" for z in recovered), f"{error:.8g}")
    assert error < 0.002

    print("Worst-case rate example: cutoff, sqrt(N) times the unit L2 layer response")
    for n in (16, 64, 256, 1024):
        width = 1/(8*n)
        phase = 2j*np.pi*width*np.arange(1, n+1)
        mean = np.sqrt(width)*np.mean(np.expm1(phase)/phase)
        print(n, f"{np.sqrt(n)*abs(mean):.9g}")
    assert 0.33 < np.sqrt(n)*abs(mean) < 0.36


if __name__ == "__main__":
    print(f"mpmath {mp.__version__}, {mp.mp.dps} decimal digits; NumPy {np.__version__}")
    test_continuous_bridge()
    test_square_series()
    test_triangle()
    test_square_flux()
    test_hexagon()
    test_corner_layers()
    test_corner_recovery()
