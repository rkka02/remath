"""Stationary Krinsky games at singular feedback laws and a negative phase boundary.

The reward-epoch solver and the full finite Markov chain are compared at a
small depth. All the input Fréchet endpoints below are terminating decimals,
so a prohibited simultaneous outcome has exactly zero weight.
"""

from argparse import ArgumentParser
from decimal import Decimal, localcontext
from fractions import Fraction

from phase1_architectures import reset_occupation
from phase1_chain import solve_game


# (R, P, T, S), Pearson correlation at CC and at DD, respectively.
CASES = {
    "no-double-loss": ((".90", ".80", ".95", ".20"), "0", "-.25"),
    "complementary-DD": ((".75", ".50", ".875", ".25"), "0", "-1"),
    "complementary-synchronized-CC": ((".75", ".50", ".875", ".25"), "1", "-1"),
    "no-double-win": ((".50", ".20", ".75", ".10"), "-1", "-.25"),
    "endpoint-critical": ((".40", ".20", ".75", ".10"), "0", "-.25"),
    "negative-defection": ((".375", ".20", ".75", ".10"), "-.6", "-.25"),
    "negative-critical": ((".375", ".20", ".75", ".10"), "-.6", "-.09375"),
    "negative-cooperation": ((".375", ".20", ".75", ".10"), "-.6", "-.01"),
}


def rational_weights(game, kr, kp):
    r, p, t, s = map(Fraction, game)
    assert 0 < s < p < r < t < 1
    cr = (1 - r) ** 2 + Fraction(kr) * r * (1 - r)
    cp = (1 - p) ** 2 + Fraction(kp) * p * (1 - p)
    for marginal, double_loss in ((r, cr), (p, cp)):
        assert max(0, 1 - 2 * marginal) <= double_loss <= 1 - marginal
    cascade = (1 - p) * (1 - t) / (1 - s)
    return 2 * r - 1 + cr, 2 * p - 1 + cp, cp, max(cp, cascade) / (1 - r)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=CASES, default=list(CASES))
    parser.add_argument("--n", nargs="+", type=int, default=[16, 32, 64])
    parser.add_argument("--digits", type=int, default=75)
    args = parser.parse_args()
    if min(args.n) < 1 or args.digits < 35:
        parser.error("positive memory depths and at least 35 decimal digits are required")
    with localcontext() as ctx:
        ctx.prec = args.digits
        tol = Decimal(10) ** (8 - args.digits)
        for name in args.cases:
            game, kr, kp = CASES[name]
            rr, pp, cc, ratio = rational_weights(game, kr, kp)
            base = Decimal(ratio.numerator) / Decimal(ratio.denominator)
            nd = 4
            small = solve_game(nd, nd, game, kr, kp, kind="D", digits=args.digits)
            reduced = reset_occupation(nd, game, kr, kp)
            for x, y in zip(reduced, (small[0], small[1] + small[2], small[3])):
                assert abs(x / y - 1) < tol
            print(f"{name}  ++(CC)={rr}  ++(DD)={pp}  --(DD)={cc}  "
                  f"odds base={ratio}  log(base)={base.ln():+.10f}")
            if not cc:
                r, p, t, s = map(Fraction, game)
                coefficient = 2 * t / (1 - (1-r)*(1-t)) if kr == "1" else 1
                print(f"  exact limiting odds coefficient={coefficient}, "
                      f"mixed/DD is asymptotic to 2*({(1-p)/(1-s)})^n")
            previous = None
            for n in sorted(set(args.n)):
                coop, mixed, defect = reset_occupation(n, game, kr, kp)
                assert abs(coop + mixed + defect - 1) < tol
                odds = coop / defect
                log_odds = odds.ln()
                suffix = ""
                if previous:
                    slope = (log_odds - previous[1]) / (n - previous[0])
                    suffix = f"  slope={slope:+.8f}"
                print(f"  n={n:3d}  CC={coop:.8E}  M={mixed:.5E}  DD={defect:.8E}  "
                      f"odds/base^n={odds / base**n:.9f}{suffix}")
                previous = n, log_odds


if __name__ == "__main__":
    main()
