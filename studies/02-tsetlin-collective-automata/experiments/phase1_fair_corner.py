"""Neutral independent frozen corner, using 1D spectra and a 2-point trace."""
import argparse
from fractions import Fraction

import mpmath as mp

from phase1_random_boundary import committors, rectangle


def short_spectrum(n, hold):
    """Endpoint entries of each spectral projector of the short killed walk."""
    def boundary(theta):
        return mp.cos((n + mp.mpf("1.5")) * theta) - 2 * hold * mp.cos((n + mp.mpf(".5")) * theta)

    previous = mp.mpf(0)
    for k in range(n + 1):
        upper = (2*k + 1) * mp.pi / (2*n + 3)
        theta = mp.findroot(boundary, (previous, upper), solver="anderson") if hold else upper
        if hold:
            assert previous < theta < upper
        previous = upper
        norm = (n + 1)/mp.mpf(2) + mp.sin(2*(n + 1)*theta)/(4*mp.sin(theta))
        origin = mp.cos(theta/2)
        end = mp.cos((n + mp.mpf(".5"))*theta)
        yield mp.cos(theta), origin**2/norm, origin*end/norm, end**2/norm


def long_resolvent(m, z, hold):
    """Entries 00, 0m and mm of (I-zA)^{-1} by tridiagonal determinants."""
    off = z / 2
    sq = off * off
    first, last = 1 - off, 1 - z*hold
    left_prev, left = mp.mpf(1), first
    right_prev, right = mp.mpf(1), last
    for _ in range(1, m):
        left_prev, left = left, left - sq*left_prev
        right_prev, right = right, right - sq*right_prev
    det = last*left - sq*left_prev
    return right/det, off**m/det, left/det


def excursion(m, n, hold):
    g00 = g0c = gcc = mp.mpf(0)
    for z, s00, s0c, scc in short_spectrum(n, hold):
        r00, r0c, rcc = long_resolvent(m, z, hold)
        g00 += s00*r00
        g0c += s0c*r0c
        gcc += scc*rcc
    return g0c/(g00*gcc - g0c**2), (g00, g0c, gcc)


def asymptotic_constants(gamma, hold):
    def integrand(theta):
        z = mp.exp(mp.j*theta)
        base = 2 / (1 + mp.sqrt(1 - z*z))
        return abs(base / (1 - hold*z*base))**2

    gcc = mp.quad(integrand, [0, mp.pi/2, mp.pi])/mp.pi
    closed_gcc = 16/mp.pi - 4 if not hold else 16*(4*mp.log(3)/mp.pi - 1)/5
    tolerance = mp.eps**mp.mpf(".8")
    assert abs(gcc - closed_gcc) < tolerance
    overlap = 2*mp.pi*mp.nsum(
        lambda k: (-1)**k*(2*k+1)/mp.cosh(gamma*(2*k+1)*mp.pi/2), [0, mp.inf])
    parameter = mp.mfrom(q=mp.exp(-mp.pi*gamma))
    elliptic = 4*mp.sqrt(parameter*(1-parameter))*mp.ellipk(parameter)**2/mp.pi
    assert abs(overlap/elliptic - 1) < tolerance
    if gamma == 1:
        assert abs(overlap - mp.gamma(mp.mpf(".25"))**4/(8*mp.pi**2)) < tolerance
    g0c = overlap/(1-2*hold)**2
    return mp.pi*g0c/(4*gcc), g0c, gcc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gamma", default="1", help="fixed long/short ratio, e.g. 3/2")
    parser.add_argument("--sizes", nargs="+", type=int, default=[8, 24, 64, 160])
    parser.add_argument("--digits", type=int, default=75)
    args = parser.parse_args()
    ratio = Fraction(args.gamma)
    if ratio < 1 or min(args.sizes) < 2 or args.digits < 30:
        parser.error("Require gamma >= 1, sizes >= 2 and at least 30 digits.")
    mp.mp.dps = max(args.digits + 10, 40)
    gamma = mp.mpf(ratio.numerator)/ratio.denominator
    disp_amp = min(55, args.digits - 2)
    disp_g = min(30, args.digits - 2)
    for name, hold in (("L", mp.mpf(0)), ("B", mp.mpf(".25"))):
        for m, n in [(2, 2), (5, 3)]:
            states, rows = rectangle(m, n, Fraction(1, 2), Fraction(0), hard=name == "L")
            truth = committors(states, rows, exact=True)[0]
            observed, _ = excursion(m, n, hold)
            assert abs(observed - mp.mpf(truth.numerator)/truth.denominator) < 250*mp.eps
        amplitude, endpoint, gcc = asymptotic_constants(gamma, hold)
        print(f"{name}, gamma={ratio}: limiting n^2 log(n) h = {mp.nstr(amplitude, disp_amp)}", flush=True)
        print("  limiting n^2 G(0,c) and G(c,c):", mp.nstr(endpoint, disp_g), mp.nstr(gcc, disp_g))
        for n in args.sizes:
            m = n*ratio.numerator // ratio.denominator
            h, (_, g0c, _) = excursion(m, n, hold)
            print(f"  ({m},{n}) h={mp.nstr(h, 23)}  "
                  f"n^2 log(n) h={mp.nstr(n*n*mp.log(n)*h, 12)}  "
                  f"n^2 G(0,c)={mp.nstr(n*n*g0c, 12)}", flush=True)


if __name__ == "__main__":
    main()
