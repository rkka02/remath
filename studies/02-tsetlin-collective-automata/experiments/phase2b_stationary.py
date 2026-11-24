"""Subtraction-free GMP stationary solves and exact Poisson-residual enclosures.

The source kernel, closed-class identification and nested-dissection order are
shared with phase1_chain. Requires a C++17 compiler and GNU MP development
headers and libraries (on macOS, `brew install gmp`). Set GMP_PREFIX for a
nonstandard installation. All compiled files live in a temporary directory.
"""
from __future__ import annotations

import io
import math
import os
import subprocess
import tempfile
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

from phase1_chain import closed_classes, dissection, game_rows_exact


@lru_cache(maxsize=1)
def _build():
    temp = tempfile.TemporaryDirectory(prefix="remath-gth-")
    binary = Path(temp.name) / "gth"
    source = Path(__file__).resolve().with_name("phase2b_gth.cpp")
    candidates = [os.environ.get("GMP_PREFIX"), "/opt/homebrew", "/usr/local"]
    flags = []
    for prefix in filter(None, candidates):
        inc = Path(prefix) / "include"
        if (inc / "gmpxx.h").is_file():
            flags = ["-isystem", str(inc), "-L" + str(Path(prefix) / "lib")]
            break
    subprocess.run([os.environ.get("CXX", "c++"), "-std=c++17", "-O3", *flags,
                    str(source), "-lgmpxx", "-lgmp", "-o", str(binary)], check=True)
    return temp, binary


def fraction_decimal(value, digits, rounding=ROUND_HALF_EVEN):
    """Convert an exact Fraction with the specified decimal rounding mode."""
    with localcontext() as ctx:
        ctx.prec = digits
        ctx.rounding = rounding
        return Decimal(value.numerator) / Decimal(value.denominator)


def _kernel(n1, n2, game, kappa_r, kappa_p, kind, lump):
    if kind not in ("L", "B"):
        raise ValueError("The accelerated grid ordering supports L and B.")
    lump = lump and n1 == n2
    states, rows = game_rows_exact(n1, n2, game, kappa_r, kappa_p, kind, lump)
    classes = closed_classes(rows)
    if len(classes) != 1:
        raise ValueError(f"{len(classes)} closed classes; an initial law is needed.")
    order = dissection(states, classes[0])
    rank = {index: pos for pos, index in enumerate(order)}
    weights = dict.fromkeys(w for i in order for w in rows[i].values())
    denominator = math.lcm(*(w.denominator for w in weights))
    indices = {w: j for j, w in enumerate(weights)}
    body = io.StringIO()
    print(" ".join(str(w.numerator * (denominator // w.denominator)) for w in weights),
          file=body)
    for i in order:
        x, y = states[i]
        outgoing = rows[i]
        pairs = (f"{rank[j]} {indices[w]}" for j, w in outgoing.items())
        print(2 * (x >= n1) + (y >= n2), len(outgoing), *pairs, file=body)
    return (len(order), len(weights), denominator, body.getvalue(), lump)


def _run(kernel, working_digits, certify):
    n, weight_count, denominator, body, lump = kernel
    header = f"{n} {weight_count} {working_digits} {int(certify)} {denominator}\n"
    build = _build()  # Keep the temporary directory alive during concurrent first calls.
    result = subprocess.run([build[1]], input=header + body, text=True,
                            stdout=subprocess.PIPE, check=True)
    records = [line.split() for line in result.stdout.splitlines()]
    if len(records) != 4:
        raise ArithmeticError("Expected four native stationary masses.")
    mass = [Decimal(record[0]) for record in records]
    intervals = []
    if certify:
        for _, low, high, denom in records:
            intervals.append((Fraction(int(low), int(denom)), Fraction(int(high), int(denom))))
    if lump:
        with localcontext() as ctx:
            ctx.prec = working_digits
            mass[1] = mass[2] = (mass[1] + mass[2]) / 2
        if intervals:
            intervals[1] = intervals[2] = tuple(
                (a + b) / 2 for a, b in zip(intervals[1], intervals[2]))
    return tuple(mass), tuple(intervals)


def solve_game_fast(n1, n2, game, kappa_r="0", kappa_p="0", kind="L", digits=90,
                    lump=True):
    """Return Decimal (CC, CD, DC, DD) via GTH at the requested precision."""
    if digits < 16:
        raise ValueError("Use at least 16 decimal digits.")
    kernel = _kernel(n1, n2, game, kappa_r, kappa_p, kind, lump)
    return _run(kernel, digits, False)[0]


@dataclass(frozen=True)
class CertifiedMasses:
    mass: tuple
    intervals: tuple
    working_digits: int
    closed_states: int


def _round_enclosure(low, high, digits, kernel):
    if low > high:
        raise ArithmeticError("Reversed stationary enclosure.")
    lo, hi = (fraction_decimal(x, digits) for x in (low, high))
    if lo == hi:
        return lo, (low, high)
    with localcontext() as ctx:
        ctx.prec = digits
        ctx.rounding = ROUND_HALF_EVEN
        if lo.next_plus() != hi:
            return None
    midpoint = (Fraction(lo) + Fraction(hi)) / 2
    if not low <= midpoint <= high:
        return None

    # A rational mass can be *exactly* on a ties-to-even rounding boundary.
    # The tree theorem bounds its denominator by Q = n D^(n-1) (twice this
    # for exchange-split masses): each integer-weight rooted tree is one of
    # the choices of an edge out of every non-root, whose total weight is at
    # most D^(n-1). Two distinct rationals then differ by >= 1/(Q den(mid)).
    n, _, denominator, _, lump = kernel
    radius = max(midpoint - low, high - midpoint)
    if radius:
        limit = (radius.denominator - 1) // (radius.numerator * midpoint.denominator)
        # Avoid constructing the large power when even its binary lower bound
        # already exceeds the required limit.
        if (n - 1) * (denominator.bit_length() - 1) >= limit.bit_length():
            return None
        if n * (2 if lump else 1) * denominator**(n-1) > limit:
            return None
    return fraction_decimal(midpoint, digits), (midpoint, midpoint)


def solve_game_certified(n1, n2, game, kappa_r="0", kappa_p="0", kind="L", digits=72,
                         working_digits=170, lump=True):
    """Certify all four masses by exact integer residuals at every recurrent state.

    Each returned decimal is the common rounding of **both** rational endpoints.
    The numerical Poisson systems may lose digits through cancellation. Increase
    working precision automatically until independently evaluated rational bounds
    prove every requested decimal. An exact midpoint is recognized from the
    matrix-tree denominator bound. All final rounding is round-to-nearest-even.
    """
    if digits < 16:
        raise ValueError("Use at least 16 decimal digits.")
    kernel = _kernel(n1, n2, game, kappa_r, kappa_p, kind, lump)
    precision = max(working_digits, digits + 16)
    while True:
        _, bounds = _run(kernel, precision, True)
        rounded = [_round_enclosure(low, high, digits, kernel) for low, high in bounds]
        if all(entry is not None for entry in rounded):
            mass, final_bounds = zip(*rounded)
            return CertifiedMasses(mass, final_bounds, precision, kernel[0])
        precision += max(48, precision // 3)
