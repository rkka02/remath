"""Stationary profiles and memory depths across the weak-reward transition.

Run directly from any directory. The chain is assembled with Decimal
probabilities and solved by subtraction-free GTH elimination.
"""
import argparse
from decimal import Decimal, localcontext

from phase1_architectures import reset_occupation
from phase1_chain import closed_classes, dissection, game_rows, solve_game, stationary


def observables(n, game, feedback, kind, digits):
    with localcontext() as context:
        context.prec = digits
        states, rows = game_rows(n, n, game, *feedback, kind, True)
        classes = closed_classes(rows)
        if len(classes) != 1:
            raise ValueError("The example must have a unique stationary law.")
        order = dissection(states, classes[0])
        probability = stationary(rows, order)
        profiles = [Decimal(0) for _ in range(3)]
        mean_gap = Decimal(0)
        mean_gap_square = Decimal(0)
        quarter = Decimal(0)

        def signed_depth(index):
            half = Decimal("0.5")
            y = Decimal(index-n) + half
            if kind == "B":
                y += half if index >= n else -half
            return y

        for (i, j), mass in zip(states, probability):
            number_defecting = int(i >= n) + int(j >= n)
            profiles[number_defecting] += mass
            gap = (signed_depth(j) - signed_depth(i)) / n
            mean_gap += gap * mass
            mean_gap_square += gap**2 * mass
            if gap <= Decimal("0.25"):
                quarter += mass
        return (*profiles, mean_gap, mean_gap_square, quarter)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depths", nargs="+", type=int, default=[8, 16, 32, 48])
    parser.add_argument("--digits", type=int, default=70)
    args = parser.parse_args()
    if min(args.depths) < 1 or args.digits < 20:
        parser.error("Use positive depths and at least 20 decimal digits.")

    with localcontext() as context:
        context.prec = args.digits
        games = [
            ("negative drift", ".60", "L", ("0", "0")),
            ("zero drift", ".75", "L", ("0", "0")),
            ("zero drift, correlated", ".75", "B", (".25", "-.20")),
            ("positive drift", ".95", "L", ("0", "0")),
        ]
        for label, t, kind, feedback in games:
            game = (".40", ".30", t, ".25")
            print(f"\n{label} ({kind}), (R,P,T,S)={game}, kappa={feedback}")
            print("   n           CC       CD + DC           DD       E|Z|/n     E(Z/n)^2     P(|Z|/n<=1/4)")
            for n in args.depths:
                values = observables(n, game, feedback, kind, args.digits)
                print(f"{n:4d} " + " ".join(f"{v:12.9f}" for v in values))

        print("\nCritical window for L with R=.40, P=.30, S=.25 and independent signals")
        print(" a    n     E|Z|/n    limit mean   P(|Z|/n<=1/4)   limit CDF")
        for a in [-1, 1]:
            k = Decimal(10*a) / 9
            limit_mean = 1 / (1-(-k).exp()) - 1 / k
            limit_quarter = ((k/4).exp()-1) / (k.exp()-1)
            for n in args.depths:
                t = Decimal(".75") + Decimal(a) / n
                if not Decimal(".4") < t < 1:
                    continue
                game = (".40", ".30", t, ".25")
                moments = observables(n, game, ("0", "0"), "L", args.digits)
                mean, quarter = moments[3], moments[5]
                print(f"{a:2d} {n:4d} {mean:11.8f} {limit_mean:13.8f}"
                      f" {quarter:16.8f} {limit_quarter:11.8f}")

        print("\nIndependent architecture reversal at (R,P,T,S)=(.45,.20,.95,.10)")
        print("   n          L(CC)          B(CC)          D(CC)          K(CC)")
        reversal = (".45", ".20", ".95", ".10")
        for n in args.depths:
            masses = [solve_game(n, n, reversal, kind=kind, digits=args.digits)[0]
                      if kind != "D" else reset_occupation(n, reversal, "0", "0")[0]
                      for kind in ("L", "B", "D", "K")]
            print(f"{n:4d} " + " ".join(f"{v:14.10f}" for v in masses))

        print("\nFair cooperative reward for L with P=.30, S=.25 and kappa_P=0")
        print("    T    kappa_R    n         CC")
        for t in (".60", ".75"):
            for kappa_r in ("-.65", "0", ".65"):
                for n in args.depths:
                    game = (".50", ".30", t, ".25")
                    cc = solve_game(n, n, game, kappa_r=kappa_r, digits=args.digits)[0]
                    print(f"{t:>5} {kappa_r:>10} {n:4d} {cc:12.9f}")

        strong = [
            ("weak punishment", (".60", ".30", ".70", ".20"), "L"),
            ("fair punishment", (".65", ".50", ".90", ".20"), "B"),
        ]
        for label, game, kind in strong:
            r = Decimal(game[0])
            expected = (r / (1-r)).ln()
            print(f"\n{label} ({kind}), (R,P,T,S)={game}, independent")
            print(f"   n           non-CC     -log(non-CC)/n     limit {expected:.9f}")
            for n in args.depths:
                _, cd, dc, dd = solve_game(n, n, game, kind=kind, digits=args.digits)
                outside = cd + dc + dd
                print(f"{n:4d} {outside:16.9E} {(-outside.ln()/n):18.9f}")


if __name__ == "__main__":
    main()
