"""Check the Krinsky reset and Krylov private-coin phase formulas.

The Krinsky computation observes the chain just after a round in which at
least one player received a reward. Between observations both players lose
and the path is deterministic. The exchange quotient has only 4n-1 observed
states. This independent reduction also measures occupation during each
unobserved run. All transition arithmetic uses decimal probabilities.
"""

from argparse import ArgumentParser
from collections import defaultdict
from decimal import Decimal, localcontext

from phase1_chain import closed_classes, solve_game, stationary
from phase1_negative_krylov import parameters as negative_parameters, rate as negative_rate


ZERO, ONE, TWO = map(Decimal, (0, 1, 2))
CASES = {
    # (R, P, T, S), correlation at CC, correlation at DD.
    "private": ((".80", ".70", ".90", ".20"), "0", "0"),
    "correlated": ((".80", ".70", ".90", ".20"), "0", ".70"),
    "synchronized": ((".80", ".70", ".90", ".20"), "0", "1"),
    "negative": ((".95", ".70", ".98", ".20"), "0", "-.20"),
    # q_R = .195 = q_P^2 + kappa_P p_P q_P exactly.
    "critical": ((".805", ".70", ".93", ".20"), "0", ".5"),
    # 2P/(1+P) = .75 at complete external synchronization.
    "krylov-critical": ((".75", ".60", ".90", ".20"), "0", "1"),
    # (1+R)/(1-R) = [(1+P)/(1-P)]^2 = 9.
    "krylov-private-critical": ((".80", ".50", ".90", ".20"), "0", "0"),
    "cascade": ((".76", ".70", ".77", ".69"), "0", "0"),
}


def probabilities(p1, p2, covariance):
    q1, q2 = ONE - p1, ONE - p2
    law = (p1 * p2 + covariance, p1 * q2 - covariance,
           q1 * p2 - covariance, q1 * q2 + covariance)
    if min(law) < 0:
        raise ValueError("infeasible joint outcome probabilities")
    return law


def reset_occupation(n, game, kappa_r, kappa_p):
    r, p, t, s = map(Decimal, game)
    tables = (probabilities(r, r, Decimal(kappa_r) * r * (ONE - r)),
              probabilities(s, t, ZERO),
              probabilities(p, p, Decimal(kappa_p) * p * (ONE - p)))
    end = 2 * n - 1
    anchors = [(i, j) for i in range(end + 1) for j in range(i, end + 1)
               if i == 0 or j == end]
    index = {state: i for i, state in enumerate(anchors)}
    rows, visits = [], []
    for anchor in anchors:
        state = anchor
        first, trail = {}, []
        while state not in first:
            first[state] = len(trail)
            i, j = state
            count_d = int(i >= n) + int(j >= n)
            law = tables[count_d]
            iw, jw = (0 if i < n else end), (0 if j < n else end)
            il, jl = i + (1 if i < n else -1), j + (1 if j < n else -1)
            next_anchors = (tuple(sorted((iw, jw))), tuple(sorted((iw, jl))),
                            tuple(sorted((il, jw))))
            trail.append((count_d, law, next_anchors))
            state = tuple(sorted((il, jl)))
        cycle_start = first[state]
        survival = ONE
        for _, law, _ in trail[cycle_start:]:
            survival *= law[3]
        cycle_sum = ONE / (ONE - survival)
        weight, row, occupation = ONE, defaultdict(Decimal), [ZERO] * 3
        for step, (count_d, law, targets) in enumerate(trail):
            total = weight if step < cycle_start else weight * cycle_sum
            occupation[count_d] += total
            for target, chance in zip(targets, law[:3]):
                if chance and target != anchor:
                    row[index[target]] += total * chance
            weight *= law[3]
        rows.append(dict(row))
        visits.append(occupation)

    classes = closed_classes(rows)
    if len(classes) != 1:
        raise ValueError(f"stationary law depends on initial state ({len(classes)} closed classes)")
    weights = stationary(rows, sorted(classes[0]))
    mass = [sum((w * v[i] for w, v in zip(weights, visits)), ZERO) for i in range(3)]
    norm = sum(mass)
    return tuple(m / norm for m in mass)


def phase_slope(kind, game, kappa):
    r, p, t, s = map(Decimal, game)

    def barrier(x):
        if kind == "D":
            return -(ONE - x).ln()
        return ((ONE + x) / (ONE - x)).ln()

    cov = Decimal(kappa) * p * (ONE - p)
    b = (ONE - p) ** 2 + cov
    if kind == "D":
        diagonal = -b.ln() if b else Decimal("Infinity")
    else:
        if Decimal(kappa) < 0:
            _, _, _, bounds = negative_rate(*negative_parameters(kind, game, kappa))
            return bounds[0]
        diagonal = (((ONE + p) ** 2 + cov) / b).ln()
    cascade = barrier(p) + barrier(t) - barrier(s)
    return barrier(r) - min(cascade, diagonal)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=CASES, default=list(CASES))
    parser.add_argument("--kinds", nargs="+", choices=("D", "K"), default=["D", "K"])
    parser.add_argument("--n", nargs="+", type=int, default=[8, 16, 24])
    parser.add_argument("--digits", type=int, default=70)
    args = parser.parse_args()
    if min(args.n) < 1 or args.digits < 30:
        parser.error("positive n and at least 30 decimal digits are required")
    with localcontext() as ctx:
        ctx.prec = args.digits
        for name in args.cases:
            game, kr, kp = CASES[name]
            # Compare the two different D chains even in runs devoted to K.
            check = reset_occupation(3, game, kr, kp)
            full = solve_game(3, 3, game, kr, kp, "D", args.digits)
            for left, right in zip(check, (full[0], full[1] + full[2], full[3])):
                assert abs(left - right) < Decimal(10) ** (8 - args.digits)
            for kind in args.kinds:
                predicted = phase_slope(kind, game, kp)
                print(f"{name}  {kind}   predicted log-odds slope {predicted:+.10f}")
                previous = None
                for n in sorted(set(args.n)):
                    if kind == "D":
                        cc, mixed, dd = reset_occupation(n, game, kr, kp)
                    else:
                        cc, cd, dc, dd = solve_game(n, n, game, kr, kp, kind, args.digits)
                        mixed = cd + dc
                    odds = (cc / dd).ln()
                    slope = "" if previous is None else (
                        f"  slope={(odds - previous[1]) / (n - previous[0]):+.8f}")
                    print(f"  n={n:3d}  CC={cc:.8f}  mixed={mixed:.4E}  "
                          f"DD={dd:.8f}  log(CC/DD)={odds:+.8f}{slope}")
                    previous = n, odds


if __name__ == "__main__":
    main()
