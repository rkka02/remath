#!/usr/bin/env python3
"""Exact tongue boundaries in the vertical section of a tilted rectangle.

Here m,n are the coprime horizontal and vertical winding counts. The CCW
boundary map applies the positive-slope chord first, so rho=m/(m+n).
Running this file checks the separate polygon/chord implementation against
the closed boundary formula and prints primary-family frequency measures.
"""

from fractions import Fraction as Q
from math import gcd
from numbers import Integral

import mpmath as mp

from phase1_probe import chord, enclosed_parameters


def _normalize_exact(x):
    """Rebuild Fraction or exact integer (including NumPy 0d integers) with native Python ints."""
    if isinstance(x, Q):
        return Q(int(x.numerator), int(x.denominator))
    if isinstance(x, Integral) and not isinstance(x, bool):
        return Q(int(x))
    if type(x).__module__ == "numpy" and getattr(x, "ndim", 1) == 0 and getattr(getattr(x, "dtype", None), "kind", "") in ("i", "u"):
        return Q(int(x))
    return x


def section_endpoint(winding, stretch):
    """Translation for which the decreasing derivative jump is periodic."""
    winding = _normalize_exact(winding)
    stretch = _normalize_exact(stretch)
    num, den = int(winding.numerator), int(winding.denominator)
    long_arc = stretch / (1 + stretch)
    numerator = 0
    denominator = 0
    weight = 1
    for j in reversed(range(den)):
        rank = j*num % den
        carry = ((j+1)*num)//den - (j*num)//den
        if 2*rank < den:
            slope = 1/stretch
            intercept = long_arc
        else:
            slope = stretch
            intercept = 1-stretch*long_arc
        numerator += weight*(carry-intercept)
        denominator += weight
        weight *= slope
    return numerator/denominator


def _require_exact_int(x, name):
    """Accept Python Integral (not bool) or NumPy 0d integer scalar; reject Fraction/float."""
    if isinstance(x, Integral) and not isinstance(x, bool):
        return int(x)
    if type(x).__module__ == "numpy" and getattr(x, "ndim", 1) == 0 and getattr(getattr(x, "dtype", None), "kind", "") in ("i", "u"):
        return int(x)
    raise TypeError(f"{name} must be an exact integer, got {type(x).__name__}")


def section_tongue(m, n, stretch):
    """Closed interval of section translations; a point when m+n is odd."""
    m = _require_exact_int(m, "m")
    n = _require_exact_int(n, "n")
    stretch = _normalize_exact(stretch)
    if min(m,n) < 1 or gcd(m,n) != 1 or stretch <= 1:
        raise ValueError('positive coprime winding counts and stretch > 1 required')
    winding = Q(m+n, 2*m)
    return tuple(sorted((section_endpoint(winding, stretch),
                         section_endpoint(winding, 1/stretch))))


def boundary_map(stretch, translation, *, input_radius=None):
    """Independent chord construction on the unit square, in edge coordinates."""
    stretch, translation = enclosed_parameters((stretch, translation), input_radius)
    a = translation*(1+stretch)/stretch
    b = translation*(1+stretch)
    along_positive = chord([0, -a, 1-a, 1])
    along_negative = chord([0, b, 1+b, 1])
    return along_negative.after(along_positive).one_lap_lift()


def check_tongues():
    checks = 0
    for stretch in (Q(2), Q(7,3)):
        for m in range(1,8):
            for n in range(1,8):
                if gcd(m,n) != 1:
                    continue
                lo, hi = section_tongue(m,n,stretch)
                q = m+n
                for translation in {lo, (lo+hi)/2, hi}:
                    return_map = boundary_map(stretch, translation).power(q)
                    disp = return_map.displacement(m)
                    if q % 2:
                        assert lo == hi and all(d == 0 for d in disp)
                    elif translation == lo or translation == hi:
                        assert lo < hi
                        assert min(disp) == 0 < max(disp) or min(disp) < 0 == max(disp)
                    else:
                        assert min(disp) < 0 < max(disp)
                        slopes = set()
                        for j,(left,right) in enumerate(zip(disp, disp[1:])):
                            if left*right <= 0:
                                x,y = return_map.x,return_map.y
                                slopes.add((y[j+1]-y[j])/(x[j+1]-x[j]))
                        assert slopes == {stretch**2, stretch**-2}
                    checks += 1
    print(f'{checks} exact polygon checks at neutral parameters, tongue edges and interiors.')


def primary_low_intervals(tilt, aspect):
    """Angles for (m,1), odd m≥3. At most one tongue meets the critical edge."""
    aspect = mp.mpmathify(aspect)
    cutoff = aspect/mp.tan(2*tilt)
    for k in range(1, int(mp.ceil(cutoff))):
        m = mp.mpf(2*k+1)
        scale = mp.sqrt(m*m+aspect*aspect)
        center = mp.atan(aspect/m)
        shift = aspect*mp.cos(2*tilt)
        spread = mp.sin(2*tilt)
        low = max(tilt, (center+mp.asin((shift-spread)/scale))/2)
        high = min(mp.pi/2-tilt, (center+mp.asin((shift+spread)/scale))/2)
        if low < high:
            yield low, high


def primary_measures(tilt, aspect):
    """Angular and frequency measures of both primary odd/odd families."""
    aspect = mp.mpmathify(aspect)
    center = mp.atan(aspect)
    intervals = [(max(tilt,center-tilt), min(mp.pi/2-tilt,center+tilt))]
    intervals.extend(primary_low_intervals(tilt, aspect))
    intervals.extend((mp.pi/2-hi,mp.pi/2-lo)
                     for lo,hi in primary_low_intervals(tilt,1/aspect))
    intervals.sort()
    assert all(a<b for a,b in intervals)
    assert all(b <= c for (_,b),(c,_) in zip(intervals,intervals[1:]))
    angles = mp.fsum(b-a for a,b in intervals)
    frequencies = mp.fsum(mp.cos(a)-mp.cos(b) for a,b in intervals)
    return len(intervals), angles, frequencies


def check_square():
    tilt = mp.pi/12
    a_mid = mp.tan(mp.pi/4-tilt)
    b_mid = mp.tan(mp.pi/4+tilt)
    assert mp.almosteq(b_mid/a_mid, 3)
    print('15-degree square at 45 degrees: full multiplier 1/9; per step',
          mp.nstr(-mp.log(b_mid/a_mid),65))
    print('tan(phi)=1/2 square: normalized slopes and multiplier at theta=pi/4,',
          Q(1,3), Q(3), Q(1,81))
    test_map = boundary_map(Q(9), Q(3,10)).power(2)
    assert {s for _,s in test_map.fixed_cells(1)[1]} == {Q(1,81), Q(81)}
    print('Square primary union: phi radians, number of tongues, angular measure, frequency measure')
    for tilt in map(mp.mpf, ('0.1','0.01','0.001','0.0001')):
        count, angles, frequencies = primary_measures(tilt,mp.mpf(1))
        print(mp.nstr(tilt,4), count, mp.nstr(angles,31), mp.nstr(frequencies,31))


def check_small_tilt():
    tilt = mp.mpf('1e-12')
    for m,n in ((1,1),(3,1),(1,5),(3,5),(5,7),(7,3)):
        aspect = mp.mpf('1.7')
        center = mp.atan(aspect*n/m)
        winding = Q(m+n,2*m)
        boundaries = []
        for branch in (-1,1):
            def residual(theta):
                a = mp.tan(theta-tilt)/aspect
                b = mp.tan(theta+tilt)/aspect
                endpoint = section_endpoint(winding, (b/a)**branch)
                return a*b/(a+b) - endpoint
            boundaries.append(mp.findroot(residual, center))
        shifts = sorted((theta-center)/tilt for theta in boundaries)
        assert abs(shifts[0]+mp.mpf(1)/(m*n)) < mp.mpf('1e-9')
        assert abs(shifts[1]-mp.mpf(1)/(m*n)) < mp.mpf('1e-9')
    print('Six individual tongue widths agree with 2 phi/(mn) at phi=1e-12 radians.')


if __name__ == '__main__':
    mp.mp.dps = 80
    check_tongues()
    check_square()
    check_small_tilt()
