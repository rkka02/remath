"""Equal-memory negative-shock selection for Krylov, linear and B automata.

Rational arithmetic certifies the strict selection sign. Decimal arithmetic
evaluates the wall rate and solves the complete finite stationary chain.
Mixed-profile rewards are independent. Games are ordered (R, P, T, S).
"""
from argparse import ArgumentParser
from decimal import Decimal, localcontext
from fractions import Fraction

from phase1_chain import solve_game


CASES = {
    "private": ("K", (".71", ".40", ".83", ".22"), "0", "0"),
    "weak": ("K", (".71", ".40", ".83", ".22"), "-.30", "-.30"),
    "pinned": ("K", (".976", ".55", ".992", ".12"), "0", "-.765"),
    "forbidden": ("K", (".93", ".625", ".95", ".25"), "0", "-.6"),
    "neutral": ("B", (".84", ".65", ".86", ".5"), "0", "-.52"),
    "unstable": ("L", (".84", ".65", ".86", ".25"), "0", "-.52"),
    "aspect": ("L", (".80", ".60", ".90", ".20"), "-.20", "-.20"),
    "boundary-L": ("L", (".64", ".60", ".68", ".04"), "0", "-.65"),
    "boundary-B": ("B", (".64", ".60", ".68", ".04"), "0", "-.65"),
}


def odds(probability):
    return probability / (1 - probability)


def parameters(kind, game, shock):
    r, p, t, s = map(Fraction, game)
    k = Fraction(shock)
    if not (0 < s < p < r < t < 1 and k <= 0):
        raise ValueError("Use strict PD probabilities and nonpositive DD shock.")
    cov = k * p * (1 - p)
    if min(p*p + cov, (1 - p)**2 + cov) < 0:
        raise ValueError("Infeasible DD correlation.")
    if kind == "K":
        r, p, t, s = ((1 + v) / 2 for v in (r, p, t, s))
        cov /= 4
    if not p > Fraction(1, 2):
        raise ValueError("Effective P must exceed 1/2.")
    q = 1 - p
    return (r, p, t, s), (q*q + cov, p*q - cov, p*p + cov)


def phase_certificate(probabilities, law, ratio=1):
    """Positive sign selects CC, negative selects DD, zero is the critical surface."""
    r, p, _, _ = probabilities
    a, b, d = law
    x = odds(p)
    y = odds(r) / x**ratio
    if y <= 1:
        # h >= log x > 0, even when this trial second tilt is nonpositive.
        return "nonpositive second tilt", y/x - 1
    a_y = a*y + b/y
    b_y = b*y + d/y
    if b_y <= a_y*x*x:
        branch, residual = "wall", a_y*x + b_y/x - 1
    else:
        branch, residual = "interior minimum", 4*a_y*b_y - 1
    return branch, residual


def dec(fraction):
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)


def rate(probabilities, law, ratio=1, kind="L"):
    r, p, t, s = (dec(odds(v)).ln() for v in probabilities)
    a, b, d = law
    x = odds(probabilities[1])
    wall = (b*x + d/x) / (a*x + b/x)
    derivative = x*(a*wall + b/wall) - (b*wall + d/wall)/x
    if a == 0:
        branch, beta = "zero double loss", Decimal("Infinity")
    elif derivative >= 0:
        branch = "oblique wall" if derivative else "tangent"
        beta = dec(wall).ln()
    else:
        branch = "pinned"
        da, db, dd = map(dec, law)
        h = Decimal(".25") - da*dd - db*db
        z = (h + (h*h - 4*da*db*db*dd).sqrt()) / (2*da*db)
        beta = z.ln() / 2
    escape = ratio*p + beta
    if s >= 0:
        if s > 0 and ratio != 1:
            raise ValueError("Stable mixed profiles require equal memories here.")
        slope = r - min(escape, ratio*p+t-s)
        bounds = (slope, slope)
    else:
        sucker = dec(probabilities[3])
        temptation = dec(probabilities[2])

        def mixed_tilt(survival):
            inverse = 1 / survival
            discriminant = inverse**2 - 4*temptation*(1-temptation)
            return ((inverse + discriminant.sqrt()) / (2*(1-temptation))).ln()

        fair = mixed_tilt(2 * (sucker * (1 - sucker)).sqrt())
        b_seam = 1 / odds(probabilities[3]) <= (2 - 1/x)**2
        if kind == "L" or b_seam:
            slope = r - ratio*p - min(beta, fair)
            bounds = (slope, slope)
        else:
            hold = mixed_tilt((1 - sucker) / 2)
            bounds = (r-ratio*p-min(beta, fair, hold),
                      r-ratio*p-min(beta, t))
    diagonal = dec(d/a).ln() if a else Decimal("Infinity")
    return branch, escape, diagonal, bounds


def verify():
    """Compare the small listed games with the independent dense stationary solve."""
    import mpmath as mp
    from phase1_mpmath_check import exact_2player_mp

    with localcontext() as ctx:
        ctx.prec = 82
        for name, (kind, game, kr, kp) in CASES.items():
            probabilities, _ = parameters(kind, game, kp)
            r, p, t, s = map(dec, probabilities)
            cr, cp = Decimal(kr), Decimal(kp)
            if kind == "K":
                raw_r, raw_p = map(Decimal, game[:2])
                cr *= raw_r / (1 + raw_r)
                cp *= raw_p / (1 + raw_p)
            oracle = exact_2player_mp(3, 2, [[(r,r), (s,t)], [(t,s), (p,p)]],
                                      [[cr, 0], [0, cp]], "L" if kind == "K" else kind, 80)
            weights = solve_game(3, 2, game, kr, kp, kind, 72)
            error = max(abs(mp.mpf(str(w))/z - 1)
                        for w, z in zip(weights, oracle[0] + oracle[1]))
            assert error < mp.mpf("1.2e-71"), (name, error)
            print(f"{name}: maximum relative profile error {mp.nstr(error, 4)}")

    raw_game = CASES["weak"][1]
    probabilities, law = parameters("K", raw_game, Fraction(-413, 2864))
    assert phase_certificate(probabilities, law)[1] == 0
    probabilities, law = parameters("L", CASES["aspect"][1], "-.20")
    assert phase_certificate(probabilities, law, 2)[1] == 0
    probabilities, (a,b,d) = parameters("L", CASES["boundary-L"][1], "-.65")
    _, _, t, s = probabilities
    x, y = Fraction(5), Fraction(7)
    mt = t/y + (1-t)*y
    assert a*x*y+b*(x/y+y/x)+d/(x*y) == Fraction(4301, 4375) < 1
    assert 4*s*(1-s)*mt*mt == Fraction(16058976, 19140625) < 1
    assert (1-s)*mt/2 == Fraction(4908, 4375) > 1
    print("Three rational phase and boundary checks passed.")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=CASES, default=list(CASES))
    parser.add_argument("--n", nargs="*", type=int, default=[8, 16, 32])
    parser.add_argument("--ratio", type=int, default=1,
                        help="integer long/short depth ratio for S <= 1/2")
    parser.add_argument("--digits", type=int, default=72)
    parser.add_argument("--verify", action="store_true",
                        help="cross-check all cases with dense mpmath and exact signs")
    args = parser.parse_args()
    if any(n < 1 for n in args.n) or args.ratio < 1 or args.digits < 30:
        parser.error("Use positive depths, ratio >= 1, and at least 30 digits.")
    if args.verify:
        verify()
    with localcontext() as ctx:
        ctx.prec = args.digits
        for case in args.cases:
            kind, game, kr, kp = CASES[case]
            probabilities, law = parameters(kind, game, kp)
            if probabilities[3] > Fraction(1, 2) and args.ratio != 1:
                parser.error(f"Case {case} requires equal memories for the stated theorem.")
            branch, residual = phase_certificate(probabilities, law, args.ratio)
            sign = (residual > 0) - (residual < 0)
            wall, escape, diagonal, (lo, hi) = rate(probabilities, law, args.ratio, kind)
            print(f"{case} ({kind})  exact sign {sign:+d}  {branch}  "
                  f"residual {residual}", flush=True)
            diag = f"  diagonal={diagonal:.12f}" if args.ratio == 1 else ""
            print(f"  {wall}  E={escape:.12f}{diag}  "
                  f"log-odds slope [{lo:.12f}, {hi:.12f}]", flush=True)
            previous = None
            for n in sorted(set(args.n)):
                cc, _, _, dd = solve_game(args.ratio*n, n, game, kr, kp, kind, args.digits)
                log_odds = (cc/dd).ln()
                line = (f"  n=({args.ratio*n},{n})  CC={cc:.12g}  "
                        f"log(CC/DD)={log_odds:.12f}")
                if previous:
                    slope = (log_odds - previous[1]) / (n - previous[0])
                    line += f"  secant={slope:.12f}"
                print(line, flush=True)
                previous = n, log_odds


if __name__ == "__main__":
    main()
