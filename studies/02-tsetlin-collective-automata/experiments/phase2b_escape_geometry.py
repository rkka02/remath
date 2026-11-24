"""Certified bridge occupation and hitting probabilities in the interacting game.

At time zero both players are deepest DD. A strict return there ends the attempt.
Success is the first CC visit, allowing any intervening visits to CD and DC.
All elimination, selected inversion and postprocessing use directed Decimal
intervals. The only inputs to these intervals are exact rational game rows.
"""

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

from phase1_chain import dissection, game_rows_exact


DATA = Path(__file__).resolve().parent / "data" / "phase2b_escape_geometry.json"
GAME = ("4/5", "3/5", "9/10", "1/5")
CORRELATIONS = ("0", "2/3", "99/100")
ZERO = (Decimal(0), Decimal(0))
ONE = (Decimal(1), Decimal(1))


class Bounds:
    """Outward-rounded intervals for nonnegative quantities."""

    def __init__(self, digits):
        lower = Context(prec=digits, rounding=ROUND_FLOOR)
        upper = Context(prec=digits, rounding=ROUND_CEILING)
        self.add_lo, self.add_hi = lower.add, upper.add
        self.mul_lo, self.mul_hi = lower.multiply, upper.multiply
        self.div_lo, self.div_hi = lower.divide, upper.divide
        self.fma_lo, self.fma_hi = lower.fma, upper.fma
        self.cache = {}

    def rational(self, value):
        if value not in self.cache:
            value = Fraction(value)
            assert value >= 0
            a, b = Decimal(value.numerator), Decimal(value.denominator)
            self.cache[value] = self.div_lo(a, b), self.div_hi(a, b)
        return self.cache[value]

    def add(self, a, b):
        return self.add_lo(a[0], b[0]), self.add_hi(a[1], b[1])

    def product(self, a, b):
        return self.mul_lo(a[0], b[0]), self.mul_hi(a[1], b[1])

    def quotient(self, a, b):
        assert b[0] > 0
        return self.div_lo(a[0], b[1]), self.div_hi(a[1], b[0])

    def fma(self, a, b, c):
        return self.fma_lo(a[0], b[0], c[0]), self.fma_hi(a[1], b[1], c[1])

    def total(self, values, initial=ZERO):
        result = initial
        for value in values:
            result = self.add(result, value)
        return result


class Printed:
    """Release a decimal only when the two rigorous endpoints round equally."""

    def __init__(self, digits):
        self.round = Context(prec=digits, rounding=ROUND_HALF_EVEN).plus

    def __call__(self, interval):
        lo, hi = map(self.round, interval)
        if lo != hi:
            raise ArithmeticError(f"Add guard digits to separate {lo} and {hi}")
        if lo == 0:
            return "0"
        if lo == 1:
            return "1"
        return str(lo)


def progress_chain(m, n, kappa, kind):
    """Progress from deepest D increases through shallow D and into C."""
    original, rows = game_rows_exact(m, n, GAME, "0", kappa, kind, False)
    progress = [(2*m - 1 - i, 2*n - 1 - j) for i, j in original]
    for i, row in enumerate(rows):
        hold = 1 - sum(row.values())
        assert hold >= 0
        if hold:
            row[i] = hold
    return progress, rows, progress.index((0, 0))


def factor_chain(progress, transitions, origin, active, arith):
    """Censor transient vertices, retaining the positive factors for both solves.

    All exits except a jump to the origin count as success in this restricted
    system. The full system kills at CC. The DD-only system kills at the first
    exit from DD and is used solely for the location of that first exit.
    """
    order = dissection(progress, active)
    local = {site: k for k, site in enumerate(order)}
    rows = []
    success, failure, source = [], [], []
    for site in order:
        edges = transitions[site]
        rows.append({local[j]: arith.rational(p) for j, p in edges.items()
                     if j != site and j in active})
        failure.append(arith.rational(edges.get(origin, 0)))
        success.append(arith.rational(sum(p for j, p in edges.items()
                                          if j != origin and j not in active)))
        source.append(arith.rational(transitions[origin].get(site, 0)))
    if any(i not in rows[j] for i, row in enumerate(rows) for j in row):
        raise ValueError("Selected inversion requires symmetric off-diagonal support")

    history = []
    for k, row in enumerate(rows):
        pivot = arith.total(row.values(), arith.add(success[k], failure[k]))
        inverse_pivot = arith.quotient(ONE, pivot)
        upward = [(j, arith.quotient(w, pivot)) for j, w in row.items()]
        reward = arith.quotient(success[k], pivot)
        loss = arith.quotient(failure[k], pivot)
        injection = arith.quotient(source[k], pivot)
        neighbors = []
        for i, u in upward:
            other = rows[i]
            incoming = other.pop(k)
            neighbors.append((i, u, arith.quotient(incoming, pivot)))
            success[i] = arith.fma(incoming, reward, success[i])
            failure[i] = arith.fma(incoming, loss, failure[i])
            source[i] = arith.fma(source[k], u, source[i])
            for j, v in upward:
                if i != j:
                    other[j] = arith.fma(incoming, v, other.get(j, ZERO))
        history.append((inverse_pivot, reward, injection, neighbors))
        row.clear()
    return order, history


def green_solves(history, arith):
    """Return (I-Q)^(-1) b and (I-Q)^(-T) alpha in elimination order."""
    committor = [ZERO] * len(history)
    occupation = [ZERO] * len(history)
    for k in reversed(range(len(history))):
        _, h, g, neighbors = history[k]
        for j, upward, downward in neighbors:
            h = arith.fma(upward, committor[j], h)
            g = arith.fma(downward, occupation[j], g)
        committor[k], occupation[k] = h, g
    return committor, occupation


def green_diagonal(history, arith):
    """Takahashi-style selected inversion from the two distinct directed factors.

    On reversing one pivot [d,-u;-l,B], the off-diagonal inverse blocks are
    (u/d)S^-1 and S^-1(l/d) for S=B-lu/d. The new diagonal is
    1/d+[(u/d)S^-1](l/d). Later neighbors form a filled clique, so every entry
    required here has already been computed. Each operation preserves positivity.
    """
    selected = [{} for _ in history]
    diagonal = [ZERO] * len(history)
    for k in reversed(range(len(history))):
        pivot_inverse, _, _, neighbors = history[k]
        row_values = [ZERO] * len(neighbors)
        for i, u, _ in neighbors:
            row_i = selected[i]
            column_value = ZERO
            for a, (j, _, v) in enumerate(neighbors):
                gij = row_i[j]
                row_values[a] = arith.fma(u, gij, row_values[a])
                column_value = arith.fma(gij, v, column_value)
            row_i[k] = column_value
        diag = pivot_inverse
        for (j, _, v), gij in zip(neighbors, row_values):
            selected[k][j] = gij
            diag = arith.fma(gij, v, diag)
        selected[k][k] = diagonal[k] = diag
    return diagonal


def enclose_solution(progress, transitions, origin, active, arith, with_diagonal):
    order, history = factor_chain(progress, transitions, origin, active, arith)
    h, g = green_solves(history, arith)
    diag = green_diagonal(history, arith) if with_diagonal else []
    return dict(zip(order, h)), dict(zip(order, g)), dict(zip(order, diag))


def first_step(transitions, origin, active, committor, arith):
    value = ZERO
    for j, p in transitions[origin].items():
        if j != origin:
            q = committor[j] if j in active else ONE
            value = arith.fma(arith.rational(p), q, value)
    return value


def exact_small_checks():
    """Compare every h, g and Gxx to a dense exact rational inverse."""
    arith = Bounds(90)
    for m, n, kappa, kind in ((3, 2, "99/100", "B"), (2, 2, "2/3", "L"),
                              (1, 1, "0", "L")):
        progress, transitions, origin = progress_chain(m, n, kappa, kind)
        sites = [k for k, (x, y) in enumerate(progress)
                 if k != origin and (x < m or y < n)]
        active = set(sites)
        h, g, diag = enclose_solution(progress, transitions, origin, active, arith, True)
        size = len(sites)
        aug = [[Fraction(i == j) - transitions[v].get(w, 0)
                for j, w in enumerate(sites)]
               + [Fraction(i == j) for j in range(size)]
               for i, v in enumerate(sites)]
        for k in range(size):
            pivot = aug[k][k]
            aug[k] = [v / pivot for v in aug[k]]
            for i in range(size):
                if i != k:
                    w = aug[i][k]
                    aug[i] = [a - w*b for a, b in zip(aug[i], aug[k])]
        inverse = [row[size:] for row in aug]
        rhs = [sum(p for j, p in transitions[v].items() if j != origin and j not in active)
               for v in sites]
        alpha = [transitions[origin].get(v, 0) for v in sites]
        for i, site in enumerate(sites):
            truth = (sum(a*b for a, b in zip(inverse[i], rhs)),
                     sum(alpha[j]*inverse[j][i] for j in range(size)), inverse[i][i])
            for interval, target in zip((h[site], g[site], diag[site]), truth):
                assert Fraction(interval[0]) <= target <= Fraction(interval[1])


def bridge_case(m, n, kappa, kind, working_digits, output_digits):
    arith, show = Bounds(working_digits), Printed(output_digits)
    progress, transitions, origin = progress_chain(m, n, kappa, kind)
    profile = [("D" if x < m else "C") + ("D" if y < n else "C") for x, y in progress]
    active = {i for i, label in enumerate(profile) if label != "CC" and i != origin}
    h, g, diag = enclose_solution(progress, transitions, origin, active, arith, True)
    success = first_step(transitions, origin, active, h, arith)
    # The initial origin is counted once. A later occurrence is the failure state.
    g[origin] = ONE
    visits = {i: arith.quotient(arith.product(g[i], h[i]), success) for i in active}
    hit = {i: arith.quotient(v, diag[i]) for i, v in visits.items()}
    visits[origin] = hit[origin] = ONE
    q = {**h, **{i: ONE for i, label in enumerate(profile) if label == "CC"}}

    last = dict.fromkeys(("DD", "DC", "CD"), ZERO)
    crossings = dict.fromkeys(("short_D_to_C", "short_C_to_D", "long_D_to_C", "long_C_to_D"),
                              ZERO)
    holds = dict.fromkeys(("short_weak_D", "short_weak_C", "long_weak_D", "long_weak_C"), ZERO)
    cc_entry = {}
    for i, v in g.items():
        x, y = progress[i]
        for j, p in transitions[i].items():
            if j == origin:
                continue
            xx, yy = progress[j]
            flow = arith.product(arith.product(v, arith.rational(p)), q[j])
            if profile[j] == "CC":
                cc_entry[j] = arith.add(cc_entry.get(j, ZERO), flow)
                last[profile[i]] = arith.add(last[profile[i]], flow)
            for pos, nxt, threshold, who in ((x, xx, m, "long"), (y, yy, n, "short")):
                if (pos < threshold) != (nxt < threshold):
                    transition = who + ("_D_to_C" if pos < threshold else "_C_to_D")
                    crossings[transition] = arith.add(crossings[transition], flow)
                if pos == nxt and threshold >= 2 and pos in (threshold-1, threshold):
                    weak = who + ("_weak_D" if pos < threshold else "_weak_C")
                    holds[weak] = arith.add(holds[weak], flow)
    cc_total = arith.total(cc_entry.values())
    assert cc_total[0] <= success[1] and success[0] <= cc_total[1]
    for i, weight in cc_entry.items():
        visits[i] = hit[i] = arith.quotient(weight, success)
    if kind == "L" and min(m, n) >= 2:
        assert all(v == ZERO for v in holds.values())
    for who in ("short", "long"):
        forward = crossings[who + "_D_to_C"]
        back_plus_one = arith.add(crossings[who + "_C_to_D"], success)
        assert forward[0] <= back_plus_one[1] and back_plus_one[0] <= forward[1]

    # Before the first departure from DD, future success depends only on the
    # first state outside DD. This weighting removes paths that ultimately fail.
    dd_active = {i for i in active if profile[i] == "DD"}
    _, dd_green, _ = enclose_solution(progress, transitions, origin, dd_active, arith, False)
    dd_green[origin] = ONE
    first = dict.fromkeys(("short_first", "long_first", "simultaneous"), ZERO)
    short_first_x = [ZERO] * m
    long_first_y = [ZERO] * n
    for i, weight in dd_green.items():
        for j, p in transitions[i].items():
            if profile[j] == "DD":
                continue
            x, y = progress[j]
            flow = arith.product(arith.product(weight, arith.rational(p)), q[j])
            mode = {"DC": "short_first", "CD": "long_first", "CC": "simultaneous"}[profile[j]]
            first[mode] = arith.add(first[mode], flow)
            if mode == "short_first":
                short_first_x[x] = arith.add(short_first_x[x], flow)
            if mode == "long_first":
                long_first_y[y] = arith.add(long_first_y[y], flow)
    first_total = arith.total(first.values())
    assert first_total[0] <= success[1] and success[0] <= first_total[1]
    assert all(0 <= v[0] and v[0] <= 1 for v in hit.values())

    site_at = {xy: i for i, xy in enumerate(progress)}
    def grid(table):
        return [[show(table.get(site_at[x, y], ZERO)) for y in range(2*n)]
                for x in range(2*m)]

    def conditional(mapping):
        return {key: show(arith.quotient(v, success)) for key, v in mapping.items()}

    def weighted_mean(weights):
        denominator = arith.total(weights)
        if denominator[1] == 0:
            return None
        numerator = arith.total(arith.product(arith.rational(i), v)
                                for i, v in enumerate(weights))
        return show(arith.quotient(numerator, denominator))

    conditional_length = arith.total(visits[i] for i in g)
    profile_time = {label: show(arith.total(visits[i] for i in g if profile[i] == label))
                    for label in ("DD", "DC", "CD")}
    weak_short_time = arith.total(visits[i] for i in g if progress[i][1] in (n-1, n))
    slice_means = {}
    for x in sorted({m//4, m//2, 3*m//4}):
        weights = [visits.get(site_at[x, y], ZERO) for y in range(n)]
        slice_means[str(x)] = weighted_mean(weights)

    return dict(
        kind=kind, kappa_P=kappa, success_before_strict_return=show(success),
        conditional_mean_steps_to_CC=show(conditional_length),
        conditional_expected_preterminal_visits_by_profile=profile_time,
        conditional_expected_time_at_short_weak_sites=show(weak_short_time),
        conditional_short_weak_fraction_of_preterminal_time=show(
            arith.quotient(weak_short_time, conditional_length)),
        conditional_expected_wall_crossings=conditional(crossings),
        conditional_expected_declined_switches=(conditional(holds) if min(m, n) >= 2 else None),
        conditional_last_profile_before_CC=conditional(last),
        conditional_first_action_change=conditional(first),
        conditional_first_short_only_probability_by_long_coordinate=[
            show(arith.quotient(v, success)) for v in short_first_x],
        conditional_first_long_only_probability_by_short_coordinate=[
            show(arith.quotient(v, success)) for v in long_first_y],
        mean_long_coordinate_given_success_and_short_first=weighted_mean(short_first_x),
        mean_short_DD_coordinate_by_long_coordinate_weighted_by_visits=slice_means,
        expected_visits_given_success=grid(visits), ever_hit_given_success=grid(hit))


def run_case(arguments):
    m, n, kappa, kind, working_digits, output_digits = arguments
    result = bridge_case(m, n, kappa, kind, working_digits, output_digits)
    print(f"{kind}  kP={kappa:<6}  p={result['success_before_strict_return']}", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depths", type=int, nargs=2, default=(60, 20), metavar=("LONG", "SHORT"))
    parser.add_argument("--working-digits", type=int, default=150)
    parser.add_argument("--output-digits", type=int, default=75)
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--output", type=Path, default=DATA)
    args = parser.parse_args()
    m, n = args.depths
    if m < n or n < 1 or args.jobs < 1 or args.working_digits <= args.output_digits:
        parser.error("Require long >= short >= 1, jobs >= 1 and working precision > output precision.")
    exact_small_checks()
    tasks = [(m, n, k, kind, args.working_digits, args.output_digits)
             for k in CORRELATIONS for kind in ("L", "B")]
    if args.jobs == 1:
        cases = list(map(run_case, tasks))
    else:
        with ProcessPoolExecutor(args.jobs) as executor:
            cases = list(executor.map(run_case, tasks))
    data = dict(
        depths=[m, n], game_R_P_T_S=list(GAME), kappa_R="0", mixed_feedback="independent",
        excursion="Start at deepest DD. First CC succeeds, first strictly positive return to "
                  "the origin fails. A self-loop on the first step is a strict return.",
        grid="A[x][y] with x the long player's progress from deepest D, y the short player's. "
             "For depth d, positions 0,...,d-1 are D, d,...,2d-1 are C. At d-1 and d the "
             "action is weakest. The time-zero origin and the first CC site are included. "
             "A CC site carries its first-entry probability. Unreachable sites have value zero.",
        conditioning="All path statistics except success_before_strict_return are conditional "
                     "on first CC before a strict origin return. An expected-visits cell counts "
                     "every visit. An ever-hit cell counts a path at most once.",
        first_action_change="short_first means DC is first, long_first means CD is first, "
                            "simultaneous means first CC precedes every mixed state. The two "
                            "position arrays sum to their respective first-change probabilities.",
        declined_switches="Expected count of private coins rejecting a weak loss in B, including "
                          "the last step. With depth >=2, a hold at a weak site identifies this event.",
        precision=dict(working_decimal_digits=args.working_digits,
                       certified_significant_digits=args.output_digits,
                       method="Outward-rounded positive elimination, forward and backward Green "
                              "solves, and sparse selected inverse from exact rational transitions. "
                              "Every displayed number has equally rounded interval endpoints.",
                       validation="Dense rational Gauss-Jordan inverse checks at (3,2) B with "
                                  "kP=99/100, (2,2) L with kP=2/3, and (1,1) L with kP=0."),
        cases=cases)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
