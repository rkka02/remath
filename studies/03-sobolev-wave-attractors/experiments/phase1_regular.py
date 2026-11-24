#!/usr/bin/env python3
"""Regular polygons, with slope dz/dx=tan(theta) and frequency lambda=cos(theta).

Run with Python 3 and mpmath. --tongues enumerates the quadratic half-period
events. --resonance N K VERTEX_DEG checks one rational grid on the actual walls.
"""
from __future__ import annotations

import argparse
import bisect
from fractions import Fraction
from math import gcd

import mpmath as mp
from mpmath.ctx_iv import MPIntervalContext

from phase1_probe import (UNRESOLVED, InsufficientResolution, chess, distinct,
                          input_ball, input_interval, mp_value, rational, regular_polygon)


def degree_interval(degrees):
    """Outward radians for a phase specified in exact rational degrees."""
    iv = MPIntervalContext()
    iv.dps = mp.mp.dps + 8
    return iv.pi*int(degrees.numerator)/(180*int(degrees.denominator))


def phase_interval(phi, input_radius=None):
    iv = MPIntervalContext()
    iv.dps = mp.mp.dps + 8
    return input_interval(phi, iv, input_radius)


def wrapped(x, step):
    """Signed offset in [-step/2,step/2)."""
    return (x + step / 2) % step - step / 2


def _dist_to_int_bounds(q_lo, q_hi):
    """Exact rational [min, max] of dist(u, Z) on the closed rational interval [q_lo, q_hi]."""
    def _d(q):
        f = q - (q.numerator // q.denominator)
        return f if f <= Fraction(1, 2) else 1 - f

    c_lo = -((-q_lo.numerator) // q_lo.denominator)
    f_hi = q_hi.numerator // q_hi.denominator
    h_lo = q_lo - Fraction(1, 2)
    h_hi = q_hi - Fraction(1, 2)
    ch_lo = -((-h_lo.numerator) // h_lo.denominator)
    fh_hi = h_hi.numerator // h_hi.denominator
    e0, e1 = _d(q_lo), _d(q_hi)
    lo_d = Fraction(0) if f_hi >= c_lo else min(e0, e1)
    hi_d = Fraction(1, 2) if fh_hi >= ch_lo else max(e0, e1)
    return lo_d, hi_d


def corner_widths(n, phi):
    """Vertical and horizontal corner-capture angular half-widths, reduced with outward precision."""
    from numbers import Integral
    from mpmath.libmp import from_rational, round_ceiling, round_floor, round_nearest, to_rational

    if isinstance(n, Integral) and not isinstance(n, bool):
        n = int(n)
    elif type(n).__module__ == "numpy" and getattr(n, "ndim", 1) == 0 and getattr(getattr(n, "dtype", None), "kind", "") in ("i", "u"):
        n = int(n)
    else:
        raise TypeError(f"corner_widths requires an exact integer n >= 3, got {type(n).__name__}")
    if n < 3:
        raise ValueError("corner_widths requires integer n >= 3")

    lo_q, hi_q, _, _, lazy_const = _exact_phase_endpoints(phi)
    target_prec = mp.mp.prec
    if lazy_const is not None:
        raw_est = lazy_const.func(64, round_ceiling)
        mag_bits = max(0, int(raw_est[2]) + int(raw_est[3]))
    else:
        mag_bits = max(0, max(abs(lo_q.numerator).bit_length() - lo_q.denominator.bit_length(),
                              abs(hi_q.numerator).bit_length() - hi_q.denominator.bit_length()))
    extra_bits = max(160, target_prec, mag_bits + 128)
    for _ in range(14):
        iv_red = MPIntervalContext()
        iv_red.prec = target_prec + extra_bits
        h_iv = iv_red.pi / n
        if lazy_const is not None:
            phi_iv = iv_red.make_mpf((
                lazy_const.func(iv_red.prec, round_floor),
                lazy_const.func(iv_red.prec, round_ceiling),
            ))
        else:
            phi_iv = iv_red.make_mpf((
                from_rational(lo_q.numerator, lo_q.denominator, iv_red.prec, round_floor),
                from_rational(hi_q.numerator, hi_q.denominator, iv_red.prec, round_ceiling),
            ))
        period_iv = 2 * h_iv if n % 2 == 0 else h_iv
        u_h = phi_iv / period_iv
        u_v = (phi_iv - iv_red.pi / 2) / period_iv
        scale = 2 if n % 2 == 0 else 1
        out = []
        for u_iv in (u_v, u_h):
            dl, dh = _dist_to_int_bounds(Fraction(*to_rational(u_iv._mpi_[0])),
                                         Fraction(*to_rational(u_iv._mpi_[1])))
            fac_lo = 1 - scale * dh
            fac_hi = 1 - scale * dl
            fac_iv = iv_red.make_mpf((
                from_rational(fac_lo.numerator, fac_lo.denominator, iv_red.prec, round_floor),
                from_rational(fac_hi.numerator, fac_hi.denominator, iv_red.prec, round_ceiling),
            ))
            w_iv = h_iv * fac_iv
            a_q = Fraction(*to_rational(w_iv._mpi_[0]))
            b_q = Fraction(*to_rational(w_iv._mpi_[1]))
            ra = from_rational(a_q.numerator, a_q.denominator, target_prec, round_nearest)
            rb = from_rational(b_q.numerator, b_q.denominator, target_prec, round_nearest)
            out.append(mp.mp.make_mpf(ra) if ra == rb else None)
        if out[0] is not None and out[1] is not None:
            return out[0], out[1]
        if lazy_const is None and lo_q < hi_q:
            raise InsufficientResolution("phase enclosure is too wide to certify rounded corner_widths")
        extra_bits *= 2
    raise InsufficientResolution("corner_widths could not certify rounded outputs at working precision")


def grid_law(n, k, phi):
    """Per-cycle multipliers of nongrazing grid cycles indexed modulo 2g."""
    h = mp.pi / n
    eta = mp.pi/2 + k*h/2
    g = gcd(k, n)
    q = n // g
    if abs(wrapped(eta - phi, h)) <= 16*mp.eps*max(1, abs(phi), abs(eta)):
        raise InsufficientResolution("unresolved grid alignment at this precision")
    offsets = [wrapped(phi+h-eta-j*h, 2*h) for j in range(2*g)]
    multipliers = {}
    for j, delta in enumerate(offsets):
        if j % g == 0:
            continue
        if q % 2:
            multipliers[j] = mp.mpf(1)
        else:
            r = q // 2
            multipliers[j] = (mp.tan(r*(j*h+delta)) /
                              mp.tan(r*(j*h-delta)))**2
    return q, offsets, multipliers


def radial_hit(n, phi, angle):
    """Counterclockwise edge coordinate of the point on the indicated ray."""
    h = mp.pi/n
    j = int(mp.floor((angle-phi)/(2*h))) % n
    a = wrapped(angle - phi - (2*j+1)*h, 2*mp.pi)
    t = (1 + mp.tan(a)/mp.tan(h))/2
    return j+t


def grid_check(n, k, phi, verify_count=False, *, input_radius=None):
    """Check the grid on the full ray map at an exact or enclosed radian phase."""
    phase = phase_interval(phi, input_radius)
    iv = phase.ctx
    grid_angle = k*iv.pi/(2*n)
    if 0 in iv.sin(n*(iv.pi/2+grid_angle-phase)):
        raise InsufficientResolution("unresolved grid alignment in the phase enclosure")
    phi = mp_value(input_ball(phase, 0)[0])
    h = mp.pi/n
    eta = mp.pi/2+k*h/2
    q, offsets, expected = grid_law(n, k, phi)
    g = n//q
    tolerance = mp.power(10, -mp.mp.dps+15)
    s = iv.tan(grid_angle)
    family = chess(regular_polygon(n, phase, iv), s).power(q)
    # Multipliers and radial hits below are predictions at the midpoint
    # phase. The midpoint of an interval cosine need not be its cosine there.
    power = chess(regular_polygon(n, iv.mpf(phi), iv), s).power(q)
    exponent = q-k//g  # counterclockwise lift
    cells = family.fixed_cells(exponent)
    alignment = abs(wrapped(eta-phi, h))
    check_tol = max(100*tolerance, 64*n*q*mp.eps/alignment)
    for j, multiplier in expected.items():
        x = rational(radial_hit(n, phi, eta+j*h))
        target = x + exponent*n
        # Evaluate a repelling branch backwards. The forward multiplier can
        # amplify the last bit of the radial hit by arbitrarily many orders.
        if multiplier > 1:
            source = power.inverse(target)
            residual = source-x
        else:
            source = x
            residual = power(x)-target
        assert abs(mp_value(residual)) < check_tol
        cell = bisect.bisect_right(power.x, source % n)-1
        slope = mp_value((power.y[cell+1]-power.y[cell])/(power.x[cell+1]-power.x[cell]))
        assert abs(slope/multiplier-1) < check_tol
    if q % 2 == 0:
        attracting = [v for v in expected.values() if v < 1]
        assert len(attracting) == g-1
        r = q//2
        telescoped = (mp.tan(r*abs(offsets[0])) *
                      mp.tan(r*abs(offsets[g])))**2
        assert abs(mp.fprod(attracting)-telescoped) < check_tol
    if cells == UNRESOLVED:
        return q, expected, UNRESOLVED
    neutral, isolated, endpoints = cells
    if verify_count and q == 2:
        assert not neutral and not endpoints and len(isolated) == 2*n-4
        if n % 4 == 2 and phi == 0:
            _, isolated, _ = power.fixed_cells(exponent)
            repellers = sorted(x for x, m in isolated if m > 1)
            mean = mp.mpf(0)
            for x, m in isolated:
                if m >= 1:
                    continue
                previous = min((x-y) % n for y in repellers)
                following = min((y-x) % n for y in repellers)
                mean += (previous+following)*mp.log(m)/(2*n)
            strongest = (2*mp.cos(h)-1)/(2*mp.cos(h)+1)
            predicted = (2*mp.log(mp.tan(h/2))+mp.log(strongest))/(n//2)
            assert abs(mean-predicted) < 100*tolerance
    return q, expected, (len(neutral), len(isolated), len(endpoints))


def resonance_window(n, k, phi):
    """Numerical endpoints inside the wall-angle cell, at the supplied radian phase.

    A scalar specifies the numerical sampling point. A phase interval carries
    the uncertainty of an intended angle through every bisection decision.
    """
    if isinstance(phi, (float, mp.mpf)):
        phi = rational(phi)  # the scalar sampling point of this numerical estimator
    phase = phase_interval(phi)
    iv = phase.ctx
    phase_center, phase_radius = input_ball(phase, 0)
    phi = mp_value(phase_center)
    g = gcd(k, n)
    q, p = n//g, k//g
    h = mp.pi/n
    center = k*h/2
    # Both the polygon's wall bearings and its quarter-turn tongue endpoints
    # move with phase. Their input uncertainty must fit the endpoint resolution.
    alignment = abs(wrapped(mp.pi/2+center-phi, h))
    accuracy = mp.sqrt(mp.eps*max(alignment, mp.eps))
    if mp_value(phase_radius) > accuracy or alignment <= 16*mp.eps*max(1, abs(phi)):
        raise InsufficientResolution("unresolved resonance phase at this precision")
    critical = [mp.mpf(0), mp.pi/2]
    for j in range(n):
        bearing = (phi+(2*j+1)*h+mp.pi/2) % mp.pi
        critical.append(min(bearing, mp.pi-bearing))
    lower = max(angle for angle in critical if angle < center)
    upper = min(angle for angle in critical if angle > center)
    # For quarter-turn symmetry a closest side-axis mirror makes the two
    # characteristic walls themselves the endpoints (regular chapter, half-period law).
    if q == 2 and n % 4 == 0 and abs(wrapped(center-phi-h, 2*h)) <= abs(wrapped(center-phi, 2*h)):
        return lower, upper
    polygon = regular_polygon(n, phase, iv)

    def status(angle):
        try:
            # The bisection chooses this precise dyadic angle as its test point.
            return chess(polygon, iv.tan(iv.mpf(angle))).power(q).rotation_status(q-p)
        except InsufficientResolution:
            return UNRESOLVED

    if g == 1 and status(k*iv.pi/(2*n)) is not True:
        raise InsufficientResolution("no certified periodic seed for this candidate")
    ends = []
    for boundary in (lower, upper):
        inside, outside = center, boundary
        while abs(outside-inside) > accuracy:
            trial = (inside+outside)/2
            decision = status(trial)
            if decision == UNRESOLVED:
                # A midpoint can be the endpoint itself. Retain only certified
                # decisions on either side, never count an unresolved trial as outside.
                near, far = (inside+trial)/2, (trial+outside)/2
                advance, retreat = status(near) is True, status(far) is False
                if not (advance or retreat):
                    raise InsufficientResolution("unresolved tongue boundary at this precision")
                if advance:
                    inside = near
                if retreat:
                    outside = far
            elif decision:
                inside = trial
            else:
                outside = trial
        ends.append((inside+outside)/2)
    return tuple(sorted(ends))


def quadratic_roots(a, b, c, tolerance):
    if tolerance < 0:
        raise ValueError("quadratic_roots requires nonnegative tolerance")
    if abs(a) < tolerance:
        return [] if abs(b) < tolerance else [-c/b]
    discriminant = b*b-4*a*c
    if discriminant < -tolerance:
        return []
    if abs(discriminant) <= tolerance:
        return [-b/(2*a)]
    root = mp.sqrt(discriminant)
    return [(-b-root)/(2*a), (-b+root)/(2*a)]


def _cluster_events(values, tolerance, noise_floor):
    """Merge sorted events within tolerance and always preserve true outward (lo, hi) bounds."""
    ordered = sorted(values)
    reps = []
    bounds = []
    clusters = []
    i = 0
    while i < len(ordered):
        j = i + 1
        while j < len(ordered) and ordered[j] - ordered[j - 1] <= tolerance:
            j += 1
        lo, hi = ordered[i], ordered[j - 1]
        rep = (lo + hi) / 2
        reps.append(rep)
        is_cl = j - i > 1 and hi - lo > noise_floor
        bounds.append((lo, hi, is_cl))
        if is_cl:
            clusters.append((lo, hi))
        i = j
    return reps, bounds, clusters


def _is_math_constant(val):
    """Detect precision-independent lazy mpmath mathematical constants (excluding context eps)."""
    from mpmath.ctx_mp_python import _constant

    return isinstance(val, _constant) and getattr(val, "name", None) != "epsilon of working precision"


def _exact_phase_endpoints(phi):
    """Extract exact rational radian endpoints (lo, hi), source context eps/dps, or lazy constant."""
    from numbers import Integral, Rational
    from mpmath.libmp import finf, fnan, fninf, to_rational

    if isinstance(phi, bool):
        raise TypeError("phase must be a real number, not bool")
    if _is_math_constant(phi):
        if getattr(phi, "func", None) is None:
            raise TypeError(f"unsupported mpmath constant {phi!r}")
        return None, None, None, None, phi
    if hasattr(phi, "_mpi_"):
        a_raw, b_raw = phi._mpi_
        if a_raw in (finf, fninf, fnan) or b_raw in (finf, fninf, fnan):
            raise ValueError("phase must be finite")
        lo = Fraction(*to_rational(a_raw))
        hi = Fraction(*to_rational(b_raw))
        ctx_dps = getattr(getattr(phi, "ctx", None), "dps", mp.mp.dps)
        eps_obj = getattr(getattr(phi, "ctx", None), "eps", mp.eps)
        eps_raw = eps_obj._mpi_[1] if hasattr(eps_obj, "_mpi_") else eps_obj._mpf_
        ctx_eps = Fraction(*to_rational(eps_raw))
        return lo, hi, ctx_dps, ctx_eps, None
    if hasattr(phi, "_mpf_"):
        raw = phi._mpf_
        if raw in (finf, fninf, fnan):
            raise ValueError("phase must be finite")
        q = Fraction(*to_rational(raw))
        ctx_obj = getattr(phi, "context", None) or getattr(phi, "ctx", None)
        ctx_dps = getattr(ctx_obj, "dps", mp.mp.dps)
        eps_raw = getattr(ctx_obj, "eps", mp.eps)._mpf_
        return q, q, ctx_dps, Fraction(*to_rational(eps_raw)), None
    if hasattr(phi, "_mpq_"):
        p_num, p_den = phi._mpq_
        q = Fraction(int(p_num), int(p_den))
        return q, q, None, None, None
    if isinstance(phi, Rational):
        q = Fraction(int(phi.numerator), int(phi.denominator))
        return q, q, None, None, None
    if isinstance(phi, Integral) and not isinstance(phi, bool):
        q = Fraction(int(phi))
        return q, q, None, None, None
    if type(phi).__module__ == "numpy" and getattr(phi, "ndim", 1) == 0 and getattr(getattr(phi, "dtype", None), "kind", "") in ("i", "u"):
        q = Fraction(int(phi))
        return q, q, None, None, None
    q = rational(phi)
    return q, q, None, None, None


def _round_mpf_dir(val_mpf, prec, rounding):
    """Round an mpf value into the active mp context with an explicit rounding mode."""
    from mpmath.libmp import from_rational, to_rational

    num, den = to_rational(val_mpf._mpf_)
    return mp.mp.make_mpf(from_rational(num, den, prec, rounding))


def half_events(n, phi, *, return_clusters=False, phi_hi=None):
    """All potential changes of the half-rotation condition for an even N.

    The constants in the quadratic equations are elementary trigonometric
    values. Evaluating the quadratics at double working precision eliminates
    square-root discriminant noise on tangent double roots while resolving
    events down to working precision.
    """
    if n < 4 or n % 2:
        raise ValueError("even n >= 4 required")
    from mpmath.libmp import round_ceiling, round_floor

    base_dps = mp.mp.dps
    base_prec = mp.mp.prec
    phi_list = [phi] if (phi_hi is None or phi_hi == phi) else [phi, phi_hi]
    with mp.workdps(2 * base_dps + 24):
        phi_vals = [mp.mpf(p.numerator) / mp.mpf(p.denominator) if isinstance(p, Fraction) else mp.mpf(p)
                    for p in phi_list]
        phi_span = max(phi_vals) - min(phi_vals)
        h = mp.pi/n
        disc_tol = mp.power(10, -(2 * base_dps + 8))
        tolerance = mp.power(10, -max(12, base_dps - 6))
        noise_floor = max(mp.power(10, -(2 * base_dps + 2)), 32 * phi_span)
        apothem, half_side = mp.cos(h), mp.sin(h)
        events = [mp.mpf(0), mp.pi/2]
        for pval in phi_vals:
            vertices = regular_polygon(n, pval)
            normals = regular_polygon(n, pval+h)
            for a, b in normals:
                if abs(b) > tolerance:
                    events.append(mp.atan(abs(a/b)))  # absolute tangent slope
                for x, z in vertices:
                    for s in quadratic_roots(b*x, -apothem, a*z, disc_tol):
                        if s <= tolerance:
                            continue
                        xx, zz = z/s, s*x
                        if abs(-b*xx+a*zz) <= half_side+tolerance:
                            events.append(mp.atan(s))
        merged, bounds, clusters = _cluster_events(events, tolerance, noise_floor)
        eval_pad = mp.power(10, -max(24, 2 * base_dps - 10))
        iv_out = MPIntervalContext()
        iv_out.dps = base_dps + 8
        cluster_ivs = [iv_out.mpf([lo, hi]) for lo, hi in clusters]
        bound_ivs = []
        for lo, hi, is_cl in bounds:
            # Pad by eval_pad (>> trig noise and phi_span^2, << base_prec ULP) before outward rounding
            # at active base_prec so inside cells trim strictly inward and boundary slivers are exact.
            lo_pad = max(mp.mpf(0), lo - eval_pad) if lo > 0 else mp.mpf(0)
            hi_pad = min(mp.pi / 2, hi + eval_pad)
            lo_r = _round_mpf_dir(lo_pad, base_prec, round_floor)
            hi_r = _round_mpf_dir(hi_pad, base_prec, round_ceiling)
            bound_ivs.append((lo_r, hi_r, is_cl))
    reps_out = [mp.mpf(e) for e in merged]
    if return_clusters:
        return reps_out, bound_ivs, cluster_ivs
    return reps_out


def line_product(a, b, c, d):
    """Coefficients in ascending order of (a+b*s)(c+d*s)."""
    return a*c, a*d+b*c, b*d


def vertex_half_events(n, phi, *, return_clusters=False, phi_hi=None):
    """Four-wall parallelogram closure at a vertex, evaluated at double working precision."""
    from mpmath.libmp import round_ceiling, round_floor

    base_dps = mp.mp.dps
    base_prec = mp.mp.prec
    phi_list = [phi] if (phi_hi is None or phi_hi == phi) else [phi, phi_hi]
    with mp.workdps(2 * base_dps + 24):
        phi_vals = [mp.mpf(p.numerator) / mp.mpf(p.denominator) if isinstance(p, Fraction) else mp.mpf(p)
                    for p in phi_list]
        phi_span = max(phi_vals) - min(phi_vals)
        h = mp.pi/n
        disc_tol = mp.power(10, -(2 * base_dps + 8))
        tolerance = mp.power(10, -max(12, base_dps - 6))
        noise_floor = max(mp.power(10, -(2 * base_dps + 2)), 32 * phi_span)
        apothem, half_side = mp.cos(h), mp.sin(h)
        lower, upper = max(mp.mpf(0), mp.pi/4-h), min(mp.pi/2, mp.pi/4+h)
        events = [mp.mpf(0), mp.pi/2, lower, upper]
        for pval in phi_vals:
            vertices, normals = regular_polygon(n, pval), regular_polygon(n, pval+h)
            for a, b in normals:
                if abs(b) > tolerance:
                    events.append(mp.atan(abs(a/b)))
            for vx, vz in vertices:
                for wx, wz in vertices:
                    if abs(wx-vx) > tolerance:
                        events.append(mp.atan(abs((wz-vz)/(wx-vx))))
                for a, b in normals:
                    u0 = apothem-a*vx-b*vz
                    if u0 < tolerance:
                        continue
                    for c, d in normals:
                        w0 = apothem-c*vx-d*vz
                        if w0 < tolerance:
                            continue
                        uw = line_product(a, b, c, -d)
                        for e, f in normals:
                            projected = e*vx+f*vz-apothem
                            forward = line_product(e, f, c, -d)
                            backward = line_product(e, -f, a, b)
                            cc, bb, aa = [projected*u+u0*v+w0*w
                                          for u, v, w in zip(uw, forward, backward)]
                            for slope in quadratic_roots(aa, bb, cc, disc_tol):
                                if slope <= tolerance:
                                    continue
                                angle = mp.atan(slope)
                                if not lower-tolerance <= angle <= upper+tolerance:
                                    continue
                                if min(abs(a+b*slope), abs(c-d*slope)) <= tolerance:
                                    continue
                                u, w = u0/(a+b*slope), w0/(c-d*slope)
                                u_hit = -b*(vx+u)+a*(vz+slope*u)
                                w_hit = -d*(vx+w)+c*(vz-slope*w)
                                far_hit = -f*(vx+u+w)+e*(vz+slope*(u-w))
                                if max(abs(u_hit), abs(w_hit), abs(far_hit)) <= half_side+tolerance:
                                    events.append(angle)
        merged, bounds, clusters = _cluster_events(events, tolerance, noise_floor)
        eval_pad = mp.power(10, -max(24, 2 * base_dps - 10))
        iv_out = MPIntervalContext()
        iv_out.dps = base_dps + 8
        cluster_ivs = [iv_out.mpf([lo, hi]) for lo, hi in clusters]
        bound_ivs = []
        for lo, hi, is_cl in bounds:
            lo_pad = max(mp.mpf(0), lo - eval_pad) if lo > 0 else mp.mpf(0)
            hi_pad = min(mp.pi / 2, hi + eval_pad)
            lo_r = _round_mpf_dir(lo_pad, base_prec, round_floor)
            hi_r = _round_mpf_dir(hi_pad, base_prec, round_ceiling)
            bound_ivs.append((lo_r, hi_r, is_cl))
    reps_out = [mp.mpf(e) for e in merged]
    if return_clusters:
        return reps_out, bound_ivs, cluster_ivs
    return reps_out


def has_centered_rectangle(n, phi, theta, *, input_radius=None):
    """Test a centered half-period rectangle at exact or enclosed radian angles."""
    if n < 4 or n % 2:
        raise ValueError("a centered half-period test requires an even polygon")
    phase = phase_interval(phi, input_radius)
    iv = phase.ctx
    angle = input_interval(theta, iv, input_radius)
    if not (angle > 0 and angle < iv.pi/2):
        return UNRESOLVED
    h, s = iv.pi/n, iv.tan(angle)
    apothem, half_side = iv.cos(h), iv.sin(h)
    normals = regular_polygon(n, phase+h, iv)
    for a, b in normals:
        for c, d in normals:
            det = a*c/s-b*d*s
            if 0 in det:
                continue
            x, z = apothem*(c/s-b)/det, apothem*(a-d*s)/det
            xx, zz = z/s, s*x
            if (abs(x-xx)+abs(z-zz) > 0 and abs(x+xx)+abs(z+zz) > 0 and
                    abs(-b*x+a*z) < half_side and abs(-d*xx+c*zz) < half_side):
                return True
    try:
        return chess(regular_polygon(n, phase, iv), s).power(2).rotation_status(1)
    except InsufficientResolution:
        return UNRESOLVED


def half_period_cells(n, phi, *, input_radius=None):
    """Numerical open cells and event diagnostics at an exact/ULP-tight phase."""
    from mpmath.libmp import from_rational, round_ceiling, round_floor, to_rational

    if input_radius is not None:
        rad_q = rational(input_radius)
        if rad_q < 0:
            raise ValueError("input_radius must be nonnegative")
        if rad_q > 0:
            raise InsufficientResolution("sharp cell endpoints require an exact phase (zero input_radius)")
    lo_q, hi_q, ctx_dps, ctx_eps, lazy_const = _exact_phase_endpoints(phi)
    base_dps = mp.mp.dps
    mp_eps_q = Fraction(*to_rational(mp.eps._mpf_))
    if lazy_const is not None:
        raw_est = lazy_const.func(64, round_ceiling)
        mag_bits = max(0, int(raw_est[2]) + int(raw_est[3]))
    else:
        delta_q = hi_q - lo_q
        if delta_q > 0:
            if ctx_dps is not None and ctx_dps < base_dps:
                raise InsufficientResolution("phase enclosure comes from a coarser interval context than working precision")
            min_eps_q = min(mp_eps_q, ctx_eps) if ctx_eps is not None else mp_eps_q
            mid_abs = abs((lo_q + hi_q) / 2)
            scale_q = min(mid_abs, Fraction(7))  # absolute radian cap (never let huge |phi| inflate tolerance)
            ulp_factor = 4 if (ctx_dps is not None and ctx_dps > base_dps) else 2
            if delta_q > ulp_factor * min_eps_q * scale_q:
                raise InsufficientResolution("phase enclosure is too wide to certify sharp cell endpoints")
        mag_bits = max(0, max(abs(lo_q.numerator).bit_length() - lo_q.denominator.bit_length(),
                              abs(hi_q.numerator).bit_length() - hi_q.denominator.bit_length()))
    # Reduce phase modulo 2*pi/n with outward interval arithmetic at full precision
    # (preserving every bit of huge exact angles like 2**253+1 and lazy constants like mp.e).
    red_dps = 2 * base_dps + 48 + int(mag_bits * 0.35)
    with mp.workdps(red_dps):
        iv_red = MPIntervalContext()
        iv_red.dps = red_dps
        step_iv = 2 * iv_red.pi / n
        if lazy_const is not None:
            phi_iv_red = iv_red.make_mpf((
                lazy_const.func(iv_red.prec, round_floor),
                lazy_const.func(iv_red.prec, round_ceiling),
            ))
        else:
            phi_iv_red = iv_red.make_mpf((
                from_rational(lo_q.numerator, lo_q.denominator, iv_red.prec, round_floor),
                from_rational(hi_q.numerator, hi_q.denominator, iv_red.prec, round_ceiling),
            ))
        if (phi_iv_red.b - phi_iv_red.a) >= step_iv.a:
            raise InsufficientResolution("phase enclosure spans a full polygon symmetry sector")
        k_red = int(mp.floor(mp.mp.make_mpf(phi_iv_red._mpi_[0]) / mp.mp.make_mpf(step_iv._mpi_[0]), prec=0))
        red_iv = phi_iv_red - k_red * step_iv
        lo_red_q = Fraction(*to_rational(red_iv._mpi_[0]))
        hi_red_q = Fraction(*to_rational(red_iv._mpi_[1]))
        iv = MPIntervalContext()
        iv.dps = base_dps + 8
        phase = iv.make_mpf((
            from_rational(lo_red_q.numerator, lo_red_q.denominator, iv.prec, round_floor),
            from_rational(hi_red_q.numerator, hi_red_q.denominator, iv.prec, round_ceiling),
        ))
    tol = mp.power(10, -max(12, base_dps - 6))
    if n % 2 == 0:
        events, event_bounds, merged_clusters = half_events(
            n, lo_red_q, return_clusters=True, phi_hi=hi_red_q
        )
    else:
        events, event_bounds, merged_clusters = vertex_half_events(
            n, lo_red_q, return_clusters=True, phi_hi=hi_red_q
        )
    h = mp.pi/n
    vertices = regular_polygon(n, phase, iv)
    samples = [(rational(a)+rational(b))/2 for a, b in zip(events, events[1:])]
    wall_angles = [iv.atan2(abs(a), abs(b)) for a, b in regular_polygon(n, phase+iv.pi/n, iv)]

    def rotation_half(angle):
        curve = chess(vertices, iv.tan(angle))
        if curve.support_vertices:
            return False
        return curve.power(2).rotation_status(1)

    def event_status(left, right):
        if any(not (wall < left or wall > right) for wall in wall_angles):
            return UNRESOLVED
        # In a wall-angle component the supporting vertices are constant and
        # the lifts are pointwise ordered in theta (regular chapter, corner
        # and half-period laws). Strict exclusion on the same side at both
        # samples therefore excludes every angle between them.
        signs = []
        for angle in (left, right):
            curve = chess(vertices, iv.tan(angle))
            power = curve.power(2)
            displacement = power.displacement(1)
            margin = max(power.error, power.tol)
            signs.append((min(displacement) > margin, max(displacement) < -margin))
        if signs[0] == signs[1] and any(signs[0]):
            return False
        return rotation_half(iv.mpf([left, right]))

    inside = []
    unresolved = []
    emitted_event_idx = set()

    def _emit_bound(event_idx):
        if event_idx in emitted_event_idx:
            return
        emitted_event_idx.add(event_idx)
        lo_e, hi_e, _ = event_bounds[event_idx]
        if lo_e < hi_e:
            unresolved.append(iv.mpf([lo_e, hi_e]))

    for idx, (a, b, sample) in enumerate(zip(events, events[1:], samples)):
        if abs(mp_value(sample)-mp.pi/4) > h+tol:
            continue
        angle = input_interval(sample, iv)
        active = (has_centered_rectangle(n, phase, angle) if n % 2 == 0 else rotation_half(angle))
        if active == UNRESOLVED:
            raise InsufficientResolution("unresolved open half-period cell")
        if active:
            # Trim endpoints strictly inward using outward-rounded bounds, and always record every
            # trimmed boundary sliver in unresolved so no angle can fall between inside and unresolved.
            left_end = event_bounds[idx][1]
            right_end = event_bounds[idx + 1][0]
            if left_end < right_end:
                inside.append((left_end, right_end))
                _emit_bound(idx)
                _emit_bound(idx + 1)
            else:
                unresolved.append(iv.mpf([event_bounds[idx][0], event_bounds[idx + 1][1]]))
                emitted_event_idx.add(idx)
                emitted_event_idx.add(idx + 1)
    isolated = []
    for i, v in enumerate(events[1:-1]):
        ev_idx = i + 1
        if abs(v-mp.pi/4) > h+tol:
            continue
        if ev_idx in emitted_event_idx:
            continue
        if event_bounds[ev_idx][2]:
            _emit_bound(ev_idx)
            continue
        if any(a-tol <= v <= b+tol for a, b in inside):
            _emit_bound(ev_idx)
            continue
        try:
            # The event angle is only an estimate. Test the whole region
            # between its two chosen samples, including the estimated event.
            active = event_status(input_interval(samples[i], iv), input_interval(samples[i+1], iv))
        except InsufficientResolution:
            active = UNRESOLVED
        if active == UNRESOLVED:
            lo_e, hi_e, _ = event_bounds[ev_idx]
            unresolved.append(iv.mpf([lo_e - tol, hi_e + tol]))
            emitted_event_idx.add(ev_idx)
        elif active:
            isolated.append(v)
    return inside, isolated, unresolved


def short(x):
    return mp.nstr(x, 14)


def wall_correction(n):
    """Exact polar energy integral and the analytic quasimode residual bound."""
    from numbers import Integral

    if isinstance(n, Integral) and not isinstance(n, bool):
        n = int(n)
    elif type(n).__module__ == "numpy" and getattr(n, "ndim", 1) == 0 and getattr(getattr(n, "dtype", None), "kind", "") in ("i", "u"):
        n = int(n)
    else:
        raise TypeError(f"wall_correction requires an exact integer n >= 3, got {type(n).__name__}")
    if n < 3:
        raise ValueError("wall_correction requires integer n >= 3")
    h = mp.pi/n
    a = mp.cos(h)

    def integrand_scaled(u):
        # Change of variable t = h * u with O(1) rescaling by n^2 = (pi / h)^2
        # so mp.quad converges to full working precision even for huge N (e.g. 10^50 + 2).
        t = h * u
        ct = mp.cos(t)
        g_scaled = (mp.sin(h - t) / h) * (mp.sin(h + t) / h) / (ct * ct)
        tan_scaled = mp.tan(t) / h
        g = h * h * g_scaled
        return (mp.pi * mp.pi * g_scaled)**2 + (2 + (n - 2) * g)**2 * (mp.pi * tan_scaled)**2

    # One symmetric half-face with dt = h du gives the angular mean on the whole polygon.
    relative_energy = mp.quad(integrand_scaled, [0, 1]) / (2 * mp.mpf(n)**3)
    amplitude = mp.sin(h)**2
    bound = mp.sqrt((n*n*amplitude**2 +
                     (2+(n-2)*amplitude)**2*mp.tan(h)**2)/(2*n))
    assert 0 < relative_energy < bound**2
    return relative_energy, bound/(2*(a*a-bound)) if a*a > bound else mp.inf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--digits', type=int, default=75)
    parser.add_argument('--resonance', nargs=3, metavar=('N', 'K', 'VERTEX_DEG'))
    parser.add_argument('--tongues', action='store_true')
    args = parser.parse_args()
    if args.digits < 50:
        parser.error("use at least 50 digits for the reported checks")
    mp.mp.dps = args.digits
    if args.resonance:
        n, k, degrees = args.resonance
        n, k, degrees = int(n), int(k), Fraction(degrees)
        if not 0 < k < n or n < 3:
            parser.error("require n >= 3 and 0 < k < n")
        # Test (eta-phi)/h in rational degree units before evaluating any trig.
        residue = (Fraction(n+k, 2)-n*degrees/180) % 1
        if residue == 0:
            parser.error("grid meets polygon vertices or reflection axes")
        distance = min(residue, 1-residue)
        mp.mp.dps += max(0, int(mp.ceil(-mp.log10(mp_value(distance)))))
        while True:
            phi = degree_interval(degrees % 360)
            q, multipliers, census = grid_check(n, k, phi, True)
            if q != 2 or census != UNRESOLVED:
                break
            # At a transverse half-period grid all roots are regular, so
            # refining the original rational degree input separates every break.
            mp.mp.dps *= 2
        confirmed = bool(multipliers) or (census != UNRESOLVED and any(census))
        print('period' if confirmed else 'candidate period', q,
              'affine census (neutral pieces, interior fixed points, boundary roots)', census)
        for j, m in multipliers.items():
            print('grid cycle', j, 'multiplier', mp.nstr(m, 55))
        if args.tongues and confirmed:
            left, right = resonance_window(n, k, phi)
            digits = 14
            if right > left:
                digits = max(digits, 5 + int(mp.ceil(mp.log10(right/(right-left)))))
            print('tongue within the noncritical component, degrees (numerical)',
                  mp.nstr(mp.degrees(left), digits), mp.nstr(mp.degrees(right), digits))
            print('tongue width in degrees (numerical)', short(mp.degrees(right-left)))
        return
    print('Corner widths, vertex phase 5 degrees (N, angular fraction, frequency length)')
    for n in (3, 4, 5, 6, 7, 8, 10, 12, 20):
        a, b = corner_widths(n, mp.radians(5))
        print(n, short(2*(a+b)/mp.pi), short(1-mp.cos(a)+mp.sin(b)))
    print('N=4m+2, theta=45 degrees, vertex on x-axis')
    print('N, number attracting, strongest per-step factor, weakest, mean log per step (equal weight per cycle)')
    for n in (6, 10, 14, 22, 42, 102, 1002):
        h, number = mp.pi/n, n//2-1
        strongest = (2*mp.cos(h)-1)/(2*mp.cos(h)+1)
        weakest = (mp.cos(h)-mp.sin(h))/(mp.cos(h)+mp.sin(h))
        mean = 2*mp.log(mp.tan(h/2))/number
        if n <= 42:
            _, values, _ = grid_check(n, n//2, 0, True)
            factors = [mp.sqrt(m) for m in values.values() if m < 1]
            assert abs(min(factors)-strongest) < mp.sqrt(mp.eps)
            assert abs(max(factors)-weakest) < mp.sqrt(mp.eps)
            assert abs(mp.fsum(map(mp.log, factors))/number-mean) < mp.sqrt(mp.eps)
        print(n, number, short(strongest), short(weakest), short(mean))
    print('General rational grid, vertex phase 5 degrees unless shown')
    for n, k, degrees in ((9, 3, 5), (12, 4, 5), (15, 6, 5), (16, 4, 5),
                          (15, 5, 5), (18, 3, 3), (24, 4, 3), (8, 4, 1)):
        q, values, census = grid_check(n, k, degree_interval(degrees), True)
        print(n, k, q, 'grid cycles', len(values), 'affine census', census)
    print('PDE quasimode, N, correction energy divided by 2pi, relative residual upper bound')
    for n in (10, 22, 42, 102, 1002):
        energy, residual = wall_correction(n)
        print(n, short(energy), short(residual))
    if args.tongues:
        print('Half-period open-cell hull in degrees, noncritical angles, vertex phase 5 degrees')
        for n in (3, 4, 5, 6, 7, 8, 10, 12, 20):
            cells, isolated, unresolved = half_period_cells(n, degree_interval(5))
            hull = (short(mp.degrees(cells[0][0])), short(mp.degrees(cells[-1][1]))) if cells else ()
            total = mp.fsum(b-a for a,b in cells)
            def _fmt_ev(v):
                if hasattr(v, "_mpi_"):
                    from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
                    from mpmath.libmp import to_rational

                    iv_deg = MPIntervalContext()
                    iv_deg.dps = mp.mp.dps + 12
                    deg_iv = iv_deg.mpf(v) * 180 / iv_deg.pi
                    a_q = Fraction(*to_rational(deg_iv._mpi_[0]))
                    b_q = Fraction(*to_rational(deg_iv._mpi_[1]))
                    with localcontext() as ctx:
                        ctx.prec = 14
                        ctx.rounding = ROUND_FLOOR
                        lo_s = str(Decimal(a_q.numerator) / Decimal(a_q.denominator))
                        ctx.rounding = ROUND_CEILING
                        hi_s = str(Decimal(b_q.numerator) / Decimal(b_q.denominator))
                    return f"[{lo_s}, {hi_s}]"
                return short(mp.degrees(v))
            print(n, 'hull', hull, 'total degrees', short(mp.degrees(total)),
                  'isolated event degrees', [_fmt_ev(v) for v in isolated],
                  'unresolved event degrees', [_fmt_ev(v) for v in unresolved])


if __name__ == '__main__':
    main()
