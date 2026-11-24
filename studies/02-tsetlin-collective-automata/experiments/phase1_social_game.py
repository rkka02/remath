"""Stationary weights for two independent, equal-memory linear or B automata.

The time step updates both coordinates. Nonnegative Grassmann–Taksar–Heyman
elimination avoids subtracting escape probabilities from one. The solver uses
only Python's standard library and also supports exact rational arithmetic.
"""

from argparse import ArgumentParser
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction


EXAMPLES = {
    # Entries are mutual cooperation, mutual defection, sucker, temptation.
    "pd-short": (".80", ".70", ".20", ".90"),
    "pd-cascade": (".76", ".70", ".69", ".77"),
    "pd-critical-neutral": (".90", ".75", ".50", ".94"),
    "pd-critical-positive": (".90", ".75", ".70", ".94"),
    "stag-cascade": (".78", ".70", ".67", ".72"),
    "chicken-cooperation": (".72", ".55", ".66", ".82"),
    "chicken-mixed": (".74", ".60", ".70", ".82"),
}


def positions(n, x, win, kind):
    """The single-coordinate state runs from deepest C to deepest D."""
    cooperate = x < n
    end = 2 * n - 1
    one = type(win)(1)
    loss = one - win
    reward_state = max(0, x - 1) if cooperate else min(end, x + 1)
    loss_state = x + 1 if cooperate else x - 1
    if kind == "B" and x in (n - 1, n):
        return ((reward_state, win), (x, loss / 2), (loss_state, loss / 2))
    return ((reward_state, win), (loss_state, loss))


def index(x, y):
    if x < y:
        x, y = y, x
    return x * (x + 1) // 2 + y


def transition_matrix(n, payoffs, kind):
    r, p, s, t = payoffs
    zero = type(r)(0)
    matrix = []
    classes = []
    for x in range(2 * n):
        for y in range(x + 1):
            if x < n:
                wx, wy, profile = r, r, "R"
            elif y >= n:
                wx, wy, profile = p, p, "P"
            else:
                wx, wy, profile = t, s, "M"
            row = defaultdict(lambda: zero)
            for i, pi in positions(n, x, wx, kind):
                for j, pj in positions(n, y, wy, kind):
                    row[index(i, j)] += pi * pj
            matrix.append(dict(row))
            classes.append(profile)
    return matrix, classes


def gth_stationary(matrix, one):
    """Eliminate the highest state successively. Diagonal entries are unused."""
    size = len(matrix)
    outgoing = [{j: w for j, w in row.items() if j != i}
                for i, row in enumerate(matrix)]
    incoming = [set() for _ in matrix]
    for i, row in enumerate(outgoing):
        for j in row:
            incoming[j].add(i)
    factors = [[] for _ in matrix]
    zero = one - one
    for k in range(size - 1, 0, -1):
        exit_weight = sum(outgoing[k].values(), zero)
        if not exit_weight:
            raise ValueError("the chain is reducible")
        for i in incoming[k]:
            weight = outgoing[i].pop(k) / exit_weight
            factors[k].append((i, weight))
            row = outgoing[i]
            for j, continuation in outgoing[k].items():
                if i == j:
                    continue
                if j not in row:
                    incoming[j].add(i)
                row[j] = row.get(j, zero) + weight * continuation
        for j in outgoing[k]:
            incoming[j].discard(k)
        outgoing[k].clear()
    weights = [one]
    for predecessors in factors[1:]:
        weights.append(sum((weights[i] * w for i, w in predecessors), zero))
    total = sum(weights, zero)
    return [w / total for w in weights]


def solve(n, payoffs, kind):
    matrix, classes = transition_matrix(n, payoffs, kind)
    scalar = type(payoffs[0])
    zero, one = scalar(0), scalar(1)
    weights = gth_stationary(matrix, one)
    masses = dict.fromkeys(("R", "M", "P"), zero)
    checked = [zero for _ in weights]
    for i, row in enumerate(matrix):
        masses[classes[i]] += weights[i]
        for j, prob in row.items():
            checked[j] += weights[i] * prob
    residual = max(abs(checked[i] / w - one) for i, w in enumerate(weights))
    return masses, residual


def core_passages(n, payoffs, kind):
    """Mean dates to the opposite homogeneous core, in the indicated order."""
    matrix, _ = transition_matrix(n, payoffs, kind)
    one = type(payoffs[0])(1)
    cc, dd = 0, len(matrix) - 1
    times = []
    for source, target in ((dd, cc), (cc, dd)):
        restarted = list(matrix)
        restarted[target] = {source: one}
        weights = gth_stationary(restarted, one)
        # A return cycle has one restart date plus a passage in the true chain.
        times.append(sum(w for i, w in enumerate(weights) if i != target)
                     / weights[target])
    return times


def predicted_odds(payoffs):
    r, p, s, t = payoffs
    one = Decimal(1)

    def log_odds(x):
        return (x / (one - x)).ln()

    if min(payoffs) > one / 2:
        r, p, s, t = map(log_odds, payoffs)
        return r + min(s, r + t) - p - min(t, p + s)
    if r > one / 2 and t >= p > one / 2 >= s:
        return log_odds(r) - 2 * log_odds(p)
    raise ValueError("no proved formula is implemented for these parameters")


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=tuple(EXAMPLES),
                        default=list(EXAMPLES))
    parser.add_argument("--n", nargs="+", type=int, default=[3, 6, 10, 16])
    parser.add_argument("--tactics", nargs="+", choices=("L", "B"),
                        default=["L", "B"])
    parser.add_argument("--digits", type=int, default=65)
    parser.add_argument("--exact-check", action="store_true",
                        help="also verify n=2 with rational numbers for each case")
    parser.add_argument("--passage", action="store_true",
                        help="also compute the two directional mean core-passage times")
    args = parser.parse_args()
    if min(args.n) < 1 or args.digits < 30:
        parser.error("depth must be positive and precision must be at least 30")
    with localcontext() as ctx:
        ctx.prec = args.digits
        tolerance = Decimal(10) ** (6 - args.digits)
        for case in args.cases:
            payoffs = tuple(map(Decimal, EXAMPLES[case]))
            theory = predicted_odds(payoffs)
            for kind in args.tactics:
                print(f"{case:20} {kind}   asymptotic log-odds slope {theory:+.10f}")
                if args.exact_check:
                    exact, exact_residual = solve(2, tuple(map(Fraction, EXAMPLES[case])), kind)
                    approx, _ = solve(2, payoffs, kind)
                    assert exact_residual == 0
                    for label, value in exact.items():
                        expected = Decimal(value.numerator) / Decimal(value.denominator)
                        assert abs(approx[label] / expected - 1) < tolerance
                    if args.passage:
                        rational = tuple(map(Fraction, EXAMPLES[case]))
                        matrix, _ = transition_matrix(1, rational, kind)
                        times = core_passages(1, rational, kind)
                        for (i, j), mean in zip(((2, 0), (0, 2)), times):
                            a, b = matrix[i][1], matrix[i][j]
                            c, d = matrix[1][i], matrix[1][j]
                            assert mean == (a + c + d) / (b * (c + d) + a * d)
                previous = None
                previous_passage = None
                for n in sorted(set(args.n)):
                    masses, residual = solve(n, payoffs, kind)
                    assert residual < tolerance, (case, n, residual)
                    odds = (masses["R"] / masses["P"]).ln()
                    slope = ((odds - previous[1]) / (n - previous[0])
                             if previous else None)
                    suffix = f"  slope={slope:+.9f}" if previous else ""
                    print(f"  n={n:3d}  CC={masses['R']:.10f}  "
                          f"mixed={masses['M']:.10f}  DD={masses['P']:.10f}"
                          f"  rel.res={residual:.1E}{suffix}")
                    if args.passage:
                        means = core_passages(n, payoffs, kind)
                        log_times = [mean.ln() for mean in means]
                        suffix = ""
                        if previous_passage is not None:
                            slopes = [(log_time - old) / (n - previous[0])
                                      for log_time, old in zip(log_times, previous_passage)]
                            suffix = f"  slopes=({slopes[0]:+.9f}, {slopes[1]:+.9f})"
                        print(f"         E[DD->CC]={means[0]:.9E}  "
                              f"E[CC->DD]={means[1]:.9E}{suffix}")
                        previous_passage = log_times
                    previous = n, odds


if __name__ == "__main__":
    main()
