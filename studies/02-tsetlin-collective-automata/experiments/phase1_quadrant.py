"""Killed frozen-quadrant committor and its asymptotic rate.

The positive Decimal solve starts at the origin and stops on its first return, either
upper overflow, or the upper corner.  --verify-size independently encloses
a finite committor using interval residuals and a positive inverse bound.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, MAX_EMAX, MIN_EMIN, ROUND_CEILING, localcontext
from fractions import Fraction
from math import ceil

import mpmath as mp
from phase1_chain import dissection


class DecimalMath:
    mpf = Decimal
    sqrt = Decimal.sqrt


def parameters(ctx, p_text, k_text):
    def number(value):
        return ctx.mpf(value.numerator) / value.denominator

    pf = Fraction(p_text)
    if not 0 < pf < 1:
        raise ValueError("Require 0 < p < 1.")
    qf = 1-pf
    p, q = number(pf), number(qf)
    if k_text == "tangent":
        if pf <= qf:
            raise ValueError("The negative tangency parameter requires p > 1/2.")
        h = p*q
        den = 1+ctx.sqrt(1+4*h*h)
        k = -h-2*h*h/den
        a = q**3*(1+p-2*p**3/den)
        d = p**3*(1+q-2*q**3/den)
        b = h*(1-k)
        return p, q, k, (a, b, b, d)
    minimum = -min(pf, qf)/max(pf, qf)
    kf = minimum if k_text == "min" else Fraction(k_text)
    if not minimum <= kf <= 1:
        raise ValueError(f"Require {minimum} <= kappa <= 1.")
    # Form all rational probabilities exactly, including tiny joint losses
    # near the lower correlation endpoint, before rounding to a working precision.
    a, b, d = qf*qf+kf*pf*qf, pf*qf*(1-kf), pf*pf+kf*pf*qf
    return p, q, number(kf), (number(a), number(b), number(b), number(d))


def support(x, y, a, b, d, delta, diff_xy=None):
    """Support of {M <= 1} for a nonnegative direction, cancellation-free near x=y and delta=0."""
    abs_diff = abs(x - y) if diff_xy is None else abs(diff_xy)
    eta = abs_diff / (x + y)
    e = eta*eta
    c = 4*b*b + e*(4*b*(1-b)+delta**2)
    z = c / (e + mp.sqrt(e*e+(1-e)*c))
    # D = a exp(u) - d exp(-u); avoids cancellation at small drift or near x=y.
    D = abs(delta)*mp.sqrt((z+2*b)/(z+2*b+e*(2-z-2*b)))
    if delta > 0:
        u = mp.log1p(delta/a)/2 + mp.asinh(D/(2*mp.sqrt(a*d)))
    elif delta < 0:
        # Since d - a = delta < 0, a > d and a - d = -delta > 0.
        # u = log((D + sqrt(D^2 + 4ad))/(2a)) = asinh(D/(2*sqrt(ad))) - (1/2)*log(a/d)
        # Note 1/2 log(a/d) = 1/2 log1p((-delta)/d) and asinh(D/(2*sqrt(ad))) <= 1/2 log1p((-delta)/d) since D <= |delta|.
        # Use exact cancellation-free form via D^2 - delta^2 = -(1-z-2b)... wait:
        # Directly: ((D + sqrt(D^2 + 4ad)) / (2a)) - 1 = (D + sqrt(D^2 + 4ad) - 2a)/(2a)
        # Better: D^2 + 4ad = (2a + delta)^2 + (D^2 - delta^2) = (a+d)^2 + (D^2 - delta^2).
        # Compute D^2 - delta^2 = -delta^2 * e*(2-z-2b) / (z+2b + e*(2-z-2b)) <= 0!
        # Let R_sq = D^2 + 4ad. Then u = log1p((D - (-delta) + (sqrt(D^2+4ad) - (a+d))) / (2a))
        # where sqrt(D^2+4ad) - (a+d) = (D^2 - delta^2) / (sqrt(D^2+4ad) + a + d)
        # and D - |delta| = (D^2 - delta^2) / (D + |delta|) — BOTH exact without catastrophic cancellation!
        abs_d = -delta
        denom_D2 = z + 2*b + e*(2 - z - 2*b)
        diff_D2 = -(delta*delta) * e * (2 - z - 2*b) / denom_D2  # D^2 - delta^2 <= 0
        s_term = mp.sqrt(D*D + 4*a*d)
        num = diff_D2 / (D + abs_d) + diff_D2 / (s_term + a + d)
        u = mp.log1p(num / (2*a))
    else:
        u = mp.mpf(0)
    v = mp.asinh(eta*D/(2*b))
    # For delta < 0, (x+y)*u < 0 while |x-y|*v > 0; evaluate with extra precision if near-cancellative
    if delta < 0 and abs_diff > 0:
        # Express ((x+y)*u + abs_diff*v)/2 directly via high-precision working dps
        return ((x+y)*u + abs_diff*v)/2
    return ((x+y)*u+abs_diff*v)/2


def _to_exact_fraction(x):
    if isinstance(x, Fraction):
        return x
    if isinstance(x, mp.mpf):
        sign, man, exp, _ = x._mpf_
        if man == 0:
            return Fraction(0)
        val = Fraction(man) * (Fraction(2) ** exp)
        return -val if sign else val
    return Fraction(str(x))


def rate(p_text, k_text, gamma):
    pf = Fraction(p_text)
    ratio = _to_exact_fraction(gamma)
    delta_f = 2*pf - 1
    # Adaptive precision if |delta| or |gamma - 1| is tiny (M8 fix)
    extra_dps = 0
    if delta_f != 0:
        est = max(0, -int(mp.floor(mp.log10(abs(mp.mpf(delta_f.numerator)/delta_f.denominator)))))
        extra_dps = max(extra_dps, 2 * est + 30)
    if ratio != 1:
        diff_f = ratio - 1
        est_g = max(0, -int(mp.floor(mp.log10(abs(mp.mpf(diff_f.numerator)/diff_f.denominator)))))
        extra_dps = max(extra_dps, 2 * est_g + 30)
    old_dps = mp.mp.dps
    if extra_dps > old_dps:
        mp.mp.dps = extra_dps
    try:
        p, q, k, (a, b, _, d) = parameters(mp, p_text, k_text)
        gamma_mp = mp.mpf(ratio.numerator)/ratio.denominator
        diff_ratio = ratio - 1
        diff_mp = mp.mpf(diff_ratio.numerator)/diff_ratio.denominator
        delta = mp.mpf(delta_f.numerator)/delta_f.denominator
        if not a:
            return "unreachable", mp.inf, None
        if not b:
            if ratio != 1:
                return "unreachable", mp.inf, None
            return "synchronous", mp.log1p(delta/q) if delta > 0 else mp.mpf(0), (
                -1 if not delta else 0)
        if delta < 0:
            exponent = mp.mpf(0) if ratio == 1 else support(gamma_mp, mp.mpf(1), a, b, d, delta, diff_xy=diff_mp)
            return "positive deficit drift", +exponent, -.5
        if not delta:
            return "zero deficit drift", mp.mpf(0), None
        r = mp.log1p(delta/q)
        if k_text != "tangent" and Fraction(k_text) >= Fraction(1, 2):
            return "direct", +support(gamma_mp, mp.mpf(1), a, b, d, delta, diff_xy=diff_mp), -.5
        t = mp.log1p(delta*(1-2*k)/(a*p/q+b*q/p))
        if k_text == "tangent":
            return "tangent", +(gamma_mp*r+t), -.5
        lam = 1-2*Fraction(k_text)
        g = (1+(1-delta_f**2)*lam-lam**2)/(lam*(1-delta_f**2*lam**2))
        if not g:
            return "tangent", +(gamma_mp*r+t), -.5
        if g < 0:
            return "pinned", +(gamma_mp*r+support(mp.mpf(0), mp.mpf(1), a, b, d, delta)), -1.5
        if g <= ratio:
            return "oblique wall", +(gamma_mp*r+t), 0
        return "direct", +support(gamma_mp, mp.mpf(1), a, b, d, delta, diff_xy=diff_mp), -.5
    finally:
        mp.mp.dps = old_dps


def catalan_constant(p_text, terms, digits):
    """Use an interval sum and a geometric bound on its remaining tail."""
    old_precision = mp.iv.dps
    mp.iv.dps = digits+10
    try:
        p, q, _, _ = parameters(mp.iv, p_text, "0")
        delta_f = 2*Fraction(p_text)-1
        delta = mp.iv.mpf(delta_f.numerator)/delta_f.denominator
        term = mp.iv.mpf(1)
        total = mp.iv.mpf(0)
        for j in range(terms):
            total += term**2
            term *= (4*j+2)*p*q/(j+2)
        tail = term**2/(delta**2*(1+4*p*q))
        return str((delta/p)**2/(total+mp.iv.mpf([0, 1])*tail))
    finally:
        mp.iv.dps = old_precision


class Corner:
    """A Dirichlet system with launch at 0 and failure/success as absorbing data."""

    def __init__(self, m, n):
        self.m = m
        symmetric = m == n
        states = [(x, y) for x in range(m+1)
                  for y in range(x if symmetric else 0, n+1)
                  if (x, y) not in ((0, 0), (m, n))]
        states.append((0, 0))
        index = {state: i for i, state in enumerate(states)}
        self.size = len(states)
        self.launch = self.size-1
        self.order = dissection(states, range(self.launch)) + [self.launch]
        self.rows = []
        for x, y in states:
            row = []
            for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                xx, yy = max(0, x+dx), max(0, y+dy)
                if xx > m or yy > n or (xx, yy) == (0, 0):
                    row.append(self.size)
                elif (xx, yy) == (m, n):
                    row.append(self.size+1)
                else:
                    z = (yy, xx) if symmetric and xx > yy else (xx, yy)
                    row.append(index[z])
            self.rows.append(row)

    def solve(self, p_text, k_text, digits, full=False):
        """Positive state elimination. Decimal exponents cover arbitrarily small odds."""
        with localcontext() as ctx:
            ctx.prec = digits
            ctx.Emax, ctx.Emin = MAX_EMAX, MIN_EMIN
            zero, one = Decimal(0), Decimal(1)
            prob = parameters(DecimalMath, p_text, k_text)[-1]
            edges = []
            incoming = [set() for _ in range(self.size)]
            for i, dests in enumerate(self.rows):
                row = {}
                for j, w in zip(dests, prob):
                    if j != i and w:
                        row[j] = row.get(j, zero)+w
                        if j < self.size:
                            incoming[j].add(i)
                edges.append(row)
            history = []
            for k in self.order:
                row = edges[k]
                total = sum(row.values(), zero)
                out = [(j, w/total) for j, w in row.items()]
                if k == self.launch and not full:
                    return next((w for j, w in out if j == self.size+1), zero)
                if full:
                    history.append((k, out))
                for j, _ in out:
                    if j < self.size:
                        incoming[j].remove(k)
                for i in incoming[k]:
                    source = edges[i]
                    w = source.pop(k)
                    for j, cond in out:
                        if i != j:
                            if j in source:
                                source[j] += w*cond
                            else:
                                source[j] = w*cond
                                if j < self.size:
                                    incoming[j].add(i)
                row.clear()
                incoming[k].clear()
            value = [zero]*self.size + [zero, one]
            for k, out in reversed(history):
                value[k] = sum((w*value[j] for j, w in out), zero)
            return value

    def certify(self, p_text, k_text, digits, estimate):
        """Enclose the launch committor using an interval Dirichlet residual."""
        if estimate <= 0:
            raise ArithmeticError("An interior case must have positive corner probability.")
        d = parameters(mp, p_text, k_text)[-1][3]
        a = parameters(mp, p_text, k_text)[-1][0]
        block = self.m+1
        best = max(a, d)
        work = digits - estimate.adjusted() + ceil(-block*mp.log10(best)) + 20
        with mp.workdps(work):
            trial = self.solve(p_text, k_text, work, full=True)
            previous = mp.iv.dps
            mp.iv.dps = work
            try:
                iv = mp.iv
                prob = parameters(iv, p_text, k_text)[-1]
                v = [iv.mpf(str(x)) for x in trial]
                defect = max(abs(sum((w*v[j] for w, j in zip(prob, row)), start=0)-v[i]).b
                             for i, row in enumerate(self.rows))
                # A block of m+1 equal double outcomes reaches an absorbing
                # state from anywhere, including the lower feasibility endpoint.
                bound_prob = prob[0] if a >= d else prob[3]
                error = defect*block / bound_prob**block
                interval = v[self.launch] + iv.mpf([-1, 1])*error
                lo = mp.make_mpf(interval._mpi_[0])
                hi = mp.make_mpf(interval._mpi_[1])
                if lo <= 0 or (hi-lo)/lo > mp.power(10, -digits):
                    raise ArithmeticError("Insufficient interval accuracy.")
                power = int(mp.floor(mp.log10(lo))) - digits - 2
                scaled = interval / iv.mpf("1e" + str(power))
                lower = int(mp.floor(mp.make_mpf(scaled._mpi_[0])))
                upper = int(mp.ceil(mp.make_mpf(scaled._mpi_[1])))
                with localcontext() as ctx:
                    ctx.prec = digits+5
                    ctx.Emax, ctx.Emin = MAX_EMAX, MIN_EMIN
                    left = Decimal(lower).scaleb(power)
                    right = Decimal(upper).scaleb(power)
                    ctx.prec, ctx.rounding = 4, ROUND_CEILING
                    relative = Decimal(upper-lower)/Decimal(lower)
                return f"[{left}, {right}]", str(relative)
            finally:
                mp.iv.dps = previous


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--p", default="0.7")
    parser.add_argument("--kappa", help="decimal, fraction, tangent, or min")
    parser.add_argument("--gamma", default="1")
    parser.add_argument("--sizes", nargs="+", type=int, default=[20, 40, 80])
    parser.add_argument("--verify-size", type=int, default=0)
    parser.add_argument("--digits", type=int, default=60)
    parser.add_argument("--catalan-terms", type=int, default=0,
                        help="Enclose the independence constant with this many terms.")
    args = parser.parse_args()
    if args.digits < 2 or args.catalan_terms < 0:
        parser.error("Use at least two decimal digits and a nonnegative term count.")
    mp.mp.dps = max(80, args.digits+10)
    if args.kappa is not None:
        cases = [(args.kappa, Fraction(args.gamma))]
    else:
        pf = Fraction(args.p)
        if pf > Fraction(1, 2):
            cases = [(k, Fraction(g)) for k, g in
                     [(".5", 1), ("0", 1), ("-.12", 1), ("tangent", 1),
                      ("-.38", 1), (".2", 3), (".8", 3)]
                     if k == "tangent" or Fraction(k) >= -(1-pf)/pf]
        else:
            cases = [(k, Fraction(g)) for k, g in
                     [(".5", 1), (".5", 2), ("min", 2), ("0", 1)]]
    for k, ratio in cases:
        if ratio < 1:
            parser.error("Use gamma >= 1, interchanging the two coordinates if needed.")
        label, exponent, beta = rate(args.p, k, ratio)
        p, q, _, probs = parameters(mp, args.p, k)
        print(f"p={args.p} kappa={k} gamma={ratio}  {label}  "
              f"E={mp.nstr(exponent, 14)} beta={beta}", flush=True)
        if (args.catalan_terms and Fraction(args.p) > Fraction(1, 2)
                and k not in ("min", "tangent") and not Fraction(k)):
            print("  Catalan constant enclosure",
                  catalan_constant(args.p, args.catalan_terms, args.digits), flush=True)
        for n in sorted(set(args.sizes + ([args.verify_size] if args.verify_size else []))):
            m = ratio.numerator*n//ratio.denominator
            if n < 1:
                parser.error("Barriers must be positive.")
            if not probs[1] and m == n:
                df = 2*Fraction(args.p)-1
                drift = mp.mpf(df.numerator)/df.denominator
                r = mp.log1p(drift/q) if drift >= 0 else -mp.log1p(-drift/p)
                value = q*mp.expm1(r)/mp.expm1(n*r) if r else q/n
                if label == "unreachable":
                    print(f"  ({m},{n})  synchronous finite committor={mp.nstr(value, 16)}")
                    continue
            elif label == "unreachable":
                print(f"  ({m},{n})  committor=0")
                continue
            else:
                corner = Corner(m, n)
                decimal_value = corner.solve(args.p, k, args.digits)
                value = mp.mpf(str(decimal_value))
            # Account for the bounded rounding of the longer barrier.
            local_rate = rate(args.p, k, Fraction(m, n))[1]
            if beta is None:
                summary = f"-log(h)/n={mp.nstr(-mp.log(value)/n, 10)}"
            else:
                scaled = value*mp.exp(n*local_rate)/mp.power(n, beta)
                summary = f"h exp(n E) / n^beta={mp.nstr(scaled, 10)}"
            print(f"  ({m:3},{n:3})  h={mp.nstr(value, 11):>17}  {summary}", flush=True)
            if args.verify_size == n and label != "synchronous":
                interval, relative = corner.certify(args.p, k, args.digits, decimal_value)
                print(f"  enclosure {interval}  relative width <= {relative}",
                      flush=True)


if __name__ == "__main__":
    main()
