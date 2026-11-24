"""Check the tilted-rectangle section and its accumulating neutral frequencies."""

import mpmath as mp


def _numpy_float_to_fraction(val):
    """Exact portable Fraction for any finite 0-d NumPy float (including 80/128-bit longdouble)."""
    from fractions import Fraction
    import numpy as np

    if not bool(np.isfinite(val)):
        return None
    if val == 0:
        return Fraction(0)
    sign = -1 if val < 0 else 1
    rem = -val if sign < 0 else val
    nbits = int(np.finfo(val.dtype).nmant) + 1
    chunk_bits = min(52, nbits)
    total = Fraction(0)
    while rem != 0:
        m_f, e_f = np.frexp(rem)
        int_part = int(np.floor(np.ldexp(m_f, chunk_bits)))
        if int_part == 0:
            break
        shift = int(e_f) - chunk_bits
        if shift >= 0:
            total += Fraction(int_part << shift, 1)
        else:
            total += Fraction(int_part, 1 << (-shift))
        rem = rem - np.ldexp(val.dtype.type(int_part), shift)
    return sign * total


def _is_math_constant(val):
    """Detect precision-independent lazy mpmath mathematical constants (excluding context eps)."""
    from mpmath.ctx_mp_python import _constant

    return isinstance(val, _constant) and getattr(val, "name", None) != "epsilon of working precision"


def _is_mp_constant(val):
    """Detect lazy precision-independent mpmath mathematical constants."""
    return _is_math_constant(val)


def _exact_rational(val):
    """Convert exact stored numeric inputs (never lazy mathematical constants) to Fraction."""
    from decimal import Decimal
    from fractions import Fraction
    from math import isfinite
    from numbers import Integral, Rational
    from mpmath.libmp import finf, fnan, fninf, to_rational

    if _is_math_constant(val):
        return None
    if isinstance(val, bool):
        return None
    if hasattr(val, "_mpq_"):
        p_num, p_den = val._mpq_
        return Fraction(int(p_num), int(p_den))
    if isinstance(val, Rational):
        return Fraction(int(val.numerator), int(val.denominator))
    if isinstance(val, Integral):
        return Fraction(int(val))
    if isinstance(val, float):
        return Fraction(val) if isfinite(val) else None
    if isinstance(val, Decimal):
        return Fraction(val) if val.is_finite() else None
    if type(val).__module__ == "numpy" and getattr(val, "ndim", 1) == 0:
        kind = getattr(getattr(val, "dtype", None), "kind", "")
        if kind in ("i", "u"):
            return Fraction(int(val))
        if kind == "f":
            return _numpy_float_to_fraction(val)
        return None
    if hasattr(val, "_mpi_"):
        a_mpf, b_mpf = val._mpi_
        if a_mpf == b_mpf and a_mpf not in (finf, fninf, fnan):
            return Fraction(*to_rational(a_mpf))
        return None
    if hasattr(val, "_mpf_"):
        raw = val._mpf_
        if raw not in (finf, fninf, fnan):
            return Fraction(*to_rational(raw))
        return None
    if isinstance(val, str):
        try:
            return Fraction(val.strip())
        except (ValueError, ZeroDivisionError):
            return None
    return None


def _exact_slope_ratio(a, b):
    """Return exact positive Fraction a/b whenever the ratio is provably rational."""
    from fractions import Fraction

    if _is_math_constant(a) and _is_math_constant(b):
        if getattr(a, "func", None) is getattr(b, "func", None):
            return Fraction(1, 1)
        na, nb = getattr(a, "name", None), getattr(b, "name", None)
        if na == "1 deg = pi / 180" and nb == "pi":
            return Fraction(1, 180)
        if na == "pi" and nb == "1 deg = pi / 180":
            return Fraction(180, 1)
        return None
    qa = _exact_rational(a)
    qb = _exact_rational(b)
    if qa is not None and qb is not None and qa > 0 and qb > 0:
        return qa / qb
    return None


def _same_slope(a, b):
    """Return True when a and b are provably the exact same mathematical real number."""
    from fractions import Fraction

    return _exact_slope_ratio(a, b) == Fraction(1, 1)


def _input_bit_budget(*vals):
    """Estimate rational bit precision already present in exact inputs so adaptive loops converge immediately."""
    bits = 0
    for val in vals:
        q = _exact_rational(val)
        if q is not None:
            bits = max(bits, abs(q.numerator).bit_length(), q.denominator.bit_length())
        elif hasattr(val, "_mpi_"):
            from mpmath.libmp import finf, fnan, fninf, to_rational
            for raw in val._mpi_:
                if raw not in (finf, fninf, fnan):
                    num, den = to_rational(raw)
                    bits = max(bits, abs(num).bit_length(), den.bit_length())
    return bits


def _exact_bounds(val, prec):
    """Return exact Fraction outward bounds (lo_q, hi_q) enclosing val at bit precision prec."""
    from decimal import Decimal
    from fractions import Fraction
    from mpmath.libmp import finf, fnan, fninf, round_ceiling, round_floor, to_rational

    q = _exact_rational(val)
    if q is not None:
        return q, q
    if _is_math_constant(val):
        func = getattr(val, "func", None)
        if func is None:
            raise TypeError(f"unsupported mpmath constant {val!r}")
        lo_raw = func(prec, round_floor)
        hi_raw = func(prec, round_ceiling)
        return Fraction(*to_rational(lo_raw)), Fraction(*to_rational(hi_raw))
    if hasattr(val, "_mpi_"):
        a_raw, b_raw = val._mpi_
        if a_raw in (finf, fninf, fnan) or b_raw in (finf, fninf, fnan):
            raise ValueError("interval inputs must be finite")
        return Fraction(*to_rational(a_raw)), Fraction(*to_rational(b_raw))
    if isinstance(val, (float, str, Decimal)) or hasattr(val, "_mpf_"):
        raise ValueError(f"input must be a finite real number: {val!r}")
    if type(val).__module__ == "numpy" and getattr(val, "ndim", 1) == 0:
        if getattr(getattr(val, "dtype", None), "kind", "") in ("i", "u", "f"):
            raise ValueError(f"input must be a finite real number: {val!r}")
    raise TypeError(f"unsupported input type for strip helper: {type(val).__name__}")


def _round_iv_exact(iv_val, target_prec):
    """Return correctly rounded mp.mpf if both finite endpoints of iv_val round identically."""
    from fractions import Fraction
    from mpmath.libmp import finf, fnan, fninf, to_rational

    a_raw, b_raw = iv_val._mpi_
    if a_raw in (finf, fninf, fnan) or b_raw in (finf, fninf, fnan):
        return None
    ra = _round_exact(Fraction(*to_rational(a_raw)), target_prec)
    rb = _round_exact(Fraction(*to_rational(b_raw)), target_prec)
    return mp.mp.make_mpf(ra) if ra == rb else None


def parameters(theta, phi, aspect):
    """Physical strip slopes (a, b), ratio r = sqrt(a/b), and scale x = sqrt(a*b)."""
    from mpmath.ctx_iv import MPIntervalContext
    from mpmath.libmp import from_rational, round_ceiling, round_floor

    target_prec = mp.mp.prec
    extra_bits = max(160, target_prec, _input_bit_budget(theta, phi, aspect) + 128)
    for _ in range(14):
        prec = target_prec + extra_bits
        th_lo, th_hi = _exact_bounds(theta, prec)
        ph_lo, ph_hi = _exact_bounds(phi, prec)
        r_lo, r_hi = _exact_bounds(aspect, prec)
        if r_hi <= 0:
            raise ValueError("parameters requires positive aspect ratio")
        if r_lo <= 0:
            extra_bits *= 2
            continue
        iv = MPIntervalContext()
        iv.prec = prec + 64
        th_iv = iv.make_mpf((from_rational(th_lo.numerator, th_lo.denominator, iv.prec, round_floor),
                             from_rational(th_hi.numerator, th_hi.denominator, iv.prec, round_ceiling)))
        ph_iv = iv.make_mpf((from_rational(ph_lo.numerator, ph_lo.denominator, iv.prec, round_floor),
                             from_rational(ph_hi.numerator, ph_hi.denominator, iv.prec, round_ceiling)))
        R_iv = iv.make_mpf((from_rational(r_lo.numerator, r_lo.denominator, iv.prec, round_floor),
                            from_rational(r_hi.numerator, r_hi.denominator, iv.prec, round_ceiling)))
        minus_iv = th_iv - ph_iv
        plus_iv = th_iv + ph_iv
        if 0 in iv.cos(minus_iv) or 0 in iv.cos(plus_iv):
            extra_bits *= 2
            continue
        a_iv = iv.tan(minus_iv) / R_iv
        b_iv = iv.tan(plus_iv) / R_iv
        if a_iv > 0 and b_iv > 0:
            ratio_iv = iv.sqrt(a_iv / b_iv)
            scale_iv = iv.sqrt(a_iv * b_iv)
            vals = (_round_iv_exact(a_iv, target_prec),
                    _round_iv_exact(b_iv, target_prec),
                    _round_iv_exact(ratio_iv, target_prec),
                    _round_iv_exact(scale_iv, target_prec))
            if all(v is not None for v in vals):
                return vals
        elif a_iv < 0 or b_iv < 0:
            raise ValueError("parameters requires positive strip slopes tan(theta - phi) and tan(theta + phi)")
        extra_bits *= 2
    raise ValueError("parameters could not certify rounded outputs at working precision")


def _to_iv_at_dps(val, iv):
    """Convert a stored exact number, lazy mpmath constant, or interval into outward iv at iv.dps."""
    from mpmath.libmp import from_rational, round_ceiling, round_floor

    lo_q, hi_q = _exact_bounds(val, iv.prec)
    a_raw = from_rational(lo_q.numerator, lo_q.denominator, iv.prec, round_floor)
    b_raw = from_rational(hi_q.numerator, hi_q.denominator, iv.prec, round_ceiling)
    return iv.make_mpf((a_raw, b_raw))


def _round_exact(q, target_prec):
    """Round an exact Fraction once to target_prec with ties-to-even."""
    from mpmath.libmp import from_rational, round_nearest

    return from_rational(q.numerator, q.denominator, target_prec, round_nearest)


def _strip_position_exact(qy, qa, qb):
    """Exact rational unfolded strip position for qy in Q and positive slopes qa, qb in Q."""
    from fractions import Fraction

    if qa <= 0 or qb <= 0:
        raise ValueError("strip_position requires positive slopes a, b")
    if qa == qb:
        return qy + qa
    row = qy.numerator // qy.denominator
    frac = qy - row  # in [0, 1)
    remaining = Fraction(1)
    slope = qa if row % 2 == 0 else qb
    to_next = (1 - frac) / slope
    if remaining <= to_next:
        return row + frac + remaining * slope
    remaining -= to_next
    row += 1
    if row % 2 == 1:
        to_next = Fraction(1) / qb
        if remaining <= to_next:
            return row + remaining * qb
        remaining -= to_next
        row += 1
    pair_cost = Fraction(1) / qa + Fraction(1) / qb
    pairs = int(remaining // pair_cost)
    row += 2 * pairs
    remaining -= pairs * pair_cost
    while remaining > 0:
        slope = qa if row % 2 == 0 else qb
        to_next = Fraction(1) / slope
        if remaining <= to_next:
            return row + remaining * slope
        remaining -= to_next
        row += 1
    return Fraction(row)


def _strip_coordinate_exact(qy, qa, qb):
    """Exact rational strip coordinate for qy in Q and positive slopes qa, qb in Q."""
    from fractions import Fraction

    if qa <= 0 or qb <= 0:
        raise ValueError("strip_coordinate requires positive slopes a, b")
    if qa == qb:
        return qy / 2
    k_half = (qy + 1) // 2  # nearest even integer is 2 * k_half, so u = qy - 2*k_half in [-1, 1)
    u = qy - 2 * k_half
    if u == 0:
        return Fraction(k_half)
    inv_sum = Fraction(1) / qa + Fraction(1) / qb
    if u > 0:
        return k_half + (u / qa) / inv_sum
    return k_half + (u / qb) / inv_sum


def strip_position(y, a, b):
    """Follow the unfolded ray to the next vertical line, keeping integer row separate from offset."""
    target_prec = mp.mp.prec
    qy = _exact_rational(y)
    qa = _exact_rational(a)
    qb = _exact_rational(b)
    if qy is not None and qa is not None and qb is not None:
        exact = _strip_position_exact(qy, qa, qb)
        return mp.mp.make_mpf(_round_exact(exact, target_prec))

    # P(y; a, b) is continuous and increasing in y, a, and b on {a > 0, b > 0}.
    # Thus exact rational bounds satisfy P(y_lo; a_lo, b_lo) <= P(y; a, b) <= P(y_hi; a_hi, b_hi).
    has_lazy = any(_is_mp_constant(v) for v in (y, a, b))
    same_ab = _same_slope(a, b)
    extra_bits = max(160, target_prec, _input_bit_budget(y, a, b) + 128)
    max_iters = 14 if has_lazy else 1
    for _ in range(max_iters):
        prec = target_prec + extra_bits
        y_lo, y_hi = _exact_bounds(y, prec)
        a_lo, a_hi = _exact_bounds(a, prec)
        b_lo, b_hi = (a_lo, a_hi) if same_ab else _exact_bounds(b, prec)
        if a_hi <= 0 or b_hi <= 0:
            raise ValueError("strip_position requires positive slopes a, b")
        if a_lo <= 0 or b_lo <= 0:
            if not has_lazy:
                raise ValueError("strip_position requires positive slopes a, b")
            extra_bits *= 2
            continue
        if same_ab:
            lo_q = y_lo + a_lo
            hi_q = y_hi + a_hi
        else:
            lo_q = _strip_position_exact(y_lo, a_lo, b_lo)
            hi_q = _strip_position_exact(y_hi, a_hi, b_hi)
        ra = _round_exact(lo_q, target_prec)
        rb = _round_exact(hi_q, target_prec)
        if ra == rb:
            return mp.mp.make_mpf(ra)
        # Early exit only for fixed (non-refinable) non-singleton interval inputs that provably span multiple floats.
        if y_lo < y_hi and not _is_math_constant(y):
            inner_min_hi = (y_lo + a_hi) if same_ab else _strip_position_exact(y_lo, a_hi, b_hi)
            inner_max_lo = (y_hi + a_lo) if same_ab else _strip_position_exact(y_hi, a_lo, b_lo)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_position at working precision")
        if a_lo < a_hi and not _is_math_constant(a):
            inner_min_hi = (y_hi + a_lo) if same_ab else _strip_position_exact(y_hi, a_lo, b_hi)
            inner_max_lo = (y_lo + a_hi) if same_ab else _strip_position_exact(y_lo, a_hi, b_lo)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_position at working precision")
        if not same_ab and b_lo < b_hi and not _is_math_constant(b):
            inner_min_hi = _strip_position_exact(y_hi, a_hi, b_lo)
            inner_max_lo = _strip_position_exact(y_lo, a_lo, b_hi)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_position at working precision")
        extra_bits *= 2
    raise ValueError("inputs do not uniquely determine strip_position at working precision")


def strip_coordinate(y, a, b):
    target_prec = mp.mp.prec
    qy = _exact_rational(y)
    qa = _exact_rational(a)
    qb = _exact_rational(b)
    if qy is not None and qa is not None and qb is not None:
        exact = _strip_coordinate_exact(qy, qa, qb)
        return mp.mp.make_mpf(_round_exact(exact, target_prec))

    # T(y; a, b) is continuous, strictly increasing in y, non-increasing in a, and non-decreasing in b.
    # It depends only on the slope ratio a/b; when a/b = r in Q_{>0} (e.g. a == b or mp.degree / mp.pi = 1/180),
    # T(y; a, b) = T(y; r, 1) holds identically without independent constant-bound drift.
    from fractions import Fraction

    slope_ratio = _exact_slope_ratio(a, b)
    same_ab = (slope_ratio == Fraction(1, 1))
    has_lazy = any(_is_mp_constant(v) for v in (y, a, b))
    extra_bits = max(160, target_prec, _input_bit_budget(y, a, b) + 128)
    max_iters = 14 if has_lazy else 1
    for _ in range(max_iters):
        prec = target_prec + extra_bits
        a_lo, a_hi = _exact_bounds(a, prec)
        b_lo, b_hi = (a_lo, a_hi) if same_ab else _exact_bounds(b, prec)
        if a_hi <= 0 or b_hi <= 0:
            raise ValueError("strip_coordinate requires positive slopes a, b")
        if a_lo <= 0 or b_lo <= 0:
            if not has_lazy:
                raise ValueError("strip_coordinate requires positive slopes a, b")
            extra_bits *= 2
            continue
        if slope_ratio is not None and qy is not None:
            exact = _strip_coordinate_exact(qy, slope_ratio, Fraction(1, 1))
            return mp.mp.make_mpf(_round_exact(exact, target_prec))
        y_lo, y_hi = _exact_bounds(y, prec)
        if slope_ratio is not None:
            lo_q = _strip_coordinate_exact(y_lo, slope_ratio, Fraction(1, 1))
            hi_q = _strip_coordinate_exact(y_hi, slope_ratio, Fraction(1, 1))
        else:
            lo_q = _strip_coordinate_exact(y_lo, a_hi, b_lo)
            hi_q = _strip_coordinate_exact(y_hi, a_lo, b_hi)
        ra = _round_exact(lo_q, target_prec)
        rb = _round_exact(hi_q, target_prec)
        if ra == rb:
            return mp.mp.make_mpf(ra)
        if y_lo < y_hi and not _is_math_constant(y):
            if slope_ratio is not None:
                inner_min_hi = _strip_coordinate_exact(y_lo, slope_ratio, Fraction(1, 1))
                inner_max_lo = _strip_coordinate_exact(y_hi, slope_ratio, Fraction(1, 1))
            else:
                inner_min_hi = _strip_coordinate_exact(y_lo, a_lo, b_hi)
                inner_max_lo = _strip_coordinate_exact(y_hi, a_hi, b_lo)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_coordinate at working precision")
        if slope_ratio is None and a_lo < a_hi and not _is_math_constant(a):
            inner_min_hi = _strip_coordinate_exact(y_hi, a_hi, b_hi)
            inner_max_lo = _strip_coordinate_exact(y_lo, a_lo, b_lo)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_coordinate at working precision")
        if slope_ratio is None and b_lo < b_hi and not _is_math_constant(b):
            inner_min_hi = _strip_coordinate_exact(y_hi, a_lo, b_lo)
            inner_max_lo = _strip_coordinate_exact(y_lo, a_hi, b_hi)
            if inner_min_hi < inner_max_lo:
                if _round_exact(inner_min_hi, target_prec) != _round_exact(inner_max_lo, target_prec):
                    raise ValueError("non-singleton inputs do not uniquely determine strip_coordinate at working precision")
        extra_bits *= 2
    raise ValueError("inputs do not uniquely determine strip_coordinate at working precision")


def _involution_exact(qt, qr):
    from fractions import Fraction

    if qr == 0:
        raise ValueError("involution requires nonzero r")
    r2 = qr * qr
    whole = qt.numerator // qt.denominator
    reduced = qt - whole
    m = Fraction(1) / (1 + r2)
    if reduced <= m:
        return whole + m + r2 * reduced
    return whole + 1 + (reduced - m) / r2


def involution(t, r):
    from mpmath.ctx_iv import MPIntervalContext
    from mpmath.libmp import from_rational, round_ceiling, round_floor

    target_prec = mp.mp.prec
    qt = _exact_rational(t)
    qr = _exact_rational(r)
    if qt is not None and qr is not None:
        return mp.mp.make_mpf(_round_exact(_involution_exact(qt, qr), target_prec))

    has_lazy = any(_is_mp_constant(v) for v in (t, r))
    extra_bits = max(160, target_prec, _input_bit_budget(t, r) + 128)
    max_iters = 14 if has_lazy else 1
    for _ in range(max_iters):
        prec = target_prec + extra_bits
        t_lo, t_hi = _exact_bounds(t, prec)
        r_lo, r_hi = _exact_bounds(r, prec)
        if r_lo <= 0 <= r_hi:
            if r_lo == 0 and r_hi == 0 or not has_lazy:
                raise ValueError("involution requires nonzero r")
            extra_bits *= 2
            continue
        iv = MPIntervalContext()
        iv.prec = prec + 64
        r_iv = iv.make_mpf((from_rational(r_lo.numerator, r_lo.denominator, iv.prec, round_floor),
                            from_rational(r_hi.numerator, r_hi.denominator, iv.prec, round_ceiling)))
        r2 = r_iv * r_iv
        m_iv = iv.mpf(1) / (iv.mpf(1) + r2)
        # Involution is continuous and strictly increasing in t for every fixed nonzero r.
        ends = []
        for q_end in (t_lo, t_hi):
            whole = q_end.numerator // q_end.denominator
            red_q = q_end - whole
            red_iv = iv.make_mpf((from_rational(red_q.numerator, red_q.denominator, iv.prec, round_floor),
                                  from_rational(red_q.numerator, red_q.denominator, iv.prec, round_ceiling)))
            if red_iv <= m_iv:
                ends.append(iv.mpf(whole) + m_iv + r2 * red_iv)
            elif red_iv >= m_iv:
                ends.append(iv.mpf(whole + 1) + (red_iv - m_iv) / r2)
            else:
                # Straddles breakpoint m_iv: union of both branches encloses the continuous transition.
                b1 = iv.mpf(whole) + m_iv + r2 * red_iv
                b2 = iv.mpf(whole + 1) + (red_iv - m_iv) / r2
                ends.append(iv.make_mpf((b1._mpi_[0] if b1.a <= b2.a else b2._mpi_[0],
                                         b1._mpi_[1] if b1.b >= b2.b else b2._mpi_[1])))
        out_iv = iv.make_mpf((ends[0]._mpi_[0], ends[1]._mpi_[1]))
        rounded = _round_iv_exact(out_iv, target_prec)
        if rounded is not None:
            return rounded
        extra_bits *= 2
    raise ValueError("inputs do not uniquely determine involution at working precision")


def _circle_dist_q(d):
    from fractions import Fraction

    frac = d - (d.numerator // d.denominator)  # in [0, 1)
    return frac if frac <= Fraction(1, 2) else 1 - frac


def circle_distance(left, right):
    from fractions import Fraction

    target_prec = mp.mp.prec
    ql = _exact_rational(left)
    qr = _exact_rational(right)
    if ql is not None and qr is not None:
        return mp.mp.make_mpf(_round_exact(_circle_dist_q(ql - qr), target_prec))

    has_lazy = any(_is_mp_constant(v) for v in (left, right))
    extra_bits = max(160, target_prec, _input_bit_budget(left, right) + 128)
    max_iters = 14 if has_lazy else 1
    for _ in range(max_iters):
        prec = target_prec + extra_bits
        l_lo, l_hi = _exact_bounds(left, prec)
        r_lo, r_hi = _exact_bounds(right, prec)
        d_lo = l_lo - r_hi
        d_hi = l_hi - r_lo
        # Exact extrema of dist_Z on [d_lo, d_hi]: endpoints, integers (dist=0), half-integers (dist=1/2).
        c_lo = -((-d_lo.numerator) // d_lo.denominator)  # ceil(d_lo)
        f_hi = d_hi.numerator // d_hi.denominator        # floor(d_hi)
        h_lo = d_lo - Fraction(1, 2)
        h_hi = d_hi - Fraction(1, 2)
        ch_lo = -((-h_lo.numerator) // h_lo.denominator)
        fh_hi = h_hi.numerator // h_hi.denominator
        e0, e1 = _circle_dist_q(d_lo), _circle_dist_q(d_hi)
        lo_d = Fraction(0) if f_hi >= c_lo else min(e0, e1)
        hi_d = Fraction(1, 2) if fh_hi >= ch_lo else max(e0, e1)
        ra = _round_exact(lo_d, target_prec)
        rb = _round_exact(hi_d, target_prec)
        if ra == rb:
            return mp.mp.make_mpf(ra)
        extra_bits *= 2
    raise ValueError("inputs do not uniquely determine circle_distance at working precision")


def check_section():
    worst = mp.mpf(0)
    for tilt, direction, aspect in [(4, 12, "3.1"), (15, 45, "1"), (17, 61, ".28")]:
        a, b, r, x = parameters(mp.radians(direction), mp.radians(tilt), mp.mpf(aspect))
        s = x / (r + 1 / r)
        for start in ("-1.327", ".057", ".81", "1.27", "2.91"):
            y = mp.mpf(start)
            direct = strip_coordinate(strip_position(y, a, b) - 1, a, b)
            closed = involution(strip_coordinate(y, a, b) + s, r)
            worst = max(worst, circle_distance(direct, closed))
    assert worst < mp.mpf("1e-85")
    print("Maximum section discrepancy against direct cell crossings", mp.nstr(worst, 4))


def neutral_root(phi, aspect, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("re-entry requires an integer N >= 1")
    if not 0 < phi < mp.pi/4 or aspect <= mp.tan(2*phi):
        raise ValueError("re-entry requires 0 < phi < pi/4 and R > tan(2*phi)")
    edge = mp.atan(aspect) - phi
    guard = 8*mp.eps*max(1, abs(edge))
    lower, upper = phi+guard, edge-guard

    def residual(theta):
        # b-1 via a sine difference, avoiding subtraction of nearly equal slopes.
        b_minus_one = mp.sin(theta-edge)/(aspect*mp.cos(theta+phi)*mp.cos(edge+phi))
        # This expression for 1-r² also works when the tilt is too small
        # for the two tangents in r² to round to distinct numbers.
        gap = mp.sin(2*phi)/(mp.cos(theta-phi)*mp.sin(theta+phi))
        log_r2 = (mp.log1p(-gap) if gap < mp.mpf('.5') else
                  mp.log(mp.tan(theta-phi)/mp.tan(theta+phi)))
        return b_minus_one + mp.exp(n*log_r2)*gap/(-mp.expm1((n+1)*log_r2))

    if not lower < upper or not residual(lower) < 0 < residual(upper):
        raise ValueError("insufficient resolution for an interior re-entry bracket; "
                         "increase precision and check R > tan(2*phi)")
    for _ in range(mp.mp.prec+1):
        midpoint = (lower + upper) / 2
        if midpoint == lower or midpoint == upper:
            break
        if residual(midpoint) < 0:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def check_neutral_curve():
    phi, aspect = mp.radians(5), mp.mpf(1)
    theta_edge = mp.atan(aspect) - phi
    tangent = mp.tan(2 * phi)
    ratio = (aspect - tangent) / (aspect * (1 + aspect * tangent))
    prefactor = tangent / (1 + aspect * tangent)
    print("Square tilted 5 degrees, lower primary edge 40 degrees")
    print(" N       edge distance (radians)          distance / predicted asymptotic")
    previous = phi
    for n in (1, 2, 4, 8, 16, 32, 64):
        theta = neutral_root(phi, aspect, n)
        assert previous < theta < theta_edge
        previous = theta
        a, b, r, x = parameters(theta, phi, aspect)
        u = r + 1 / r
        code = mp.mpf(0)
        for _ in range(n):
            code = 1 / (u - code)
        assert abs(code - x) < mp.mpf("1e-85")

        # These codes have two-strip winding (2N+2, 2N). Check the map on
        # several starts with the lifted return, retaining its integer drift.
        q = 2 * n + 2
        expected_drift = 2 * n + 1
        for initial in ("0", ".173127", ".618179", ".9137"):
            initial = mp.mpf(initial)
            point = initial
            for _ in range(q):
                point = involution(point, r) + x / u
            assert abs(point - initial - expected_drift) < mp.mpf("1e-70")

        distance = theta_edge - theta
        relative = distance / (prefactor * ratio**n)
        print(f"{n:2d}  {mp.nstr(distance, 24):>30}  {mp.nstr(relative, 20):>25}")


def check_measures():
    print("Tilt     periodic frequency measure              corner frequency measure")
    for degrees in (1, 5, 15, 30):
        phi = mp.radians(degrees)
        periodic = mp.cos(phi) - mp.sin(phi)
        corner = 1 - mp.cos(phi) + mp.sin(phi)
        assert abs(periodic + corner - 1) < mp.mpf("1e-85")
        print(f"{degrees:2d}°      {mp.nstr(periodic, 28):>30}  {mp.nstr(corner, 28):>30}")


def main():
    mp.mp.dps = 95
    check_section()
    check_neutral_curve()
    check_measures()


if __name__ == "__main__":
    main()
