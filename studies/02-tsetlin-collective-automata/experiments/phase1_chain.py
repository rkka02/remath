"""Subtraction-free finite-state Markov solver for paired blind automata.

Standard library only. Probabilities may be exact decimal or fraction strings.
The GTH state reduction works on off-diagonal flows, so tiny transitions never
come from subtracting two nearly equal numbers. Nested dissection limits fill.
"""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction

ZERO, ONE, TWO = map(Decimal, (0, 1, 2))
HALF = ONE / TWO


def closed_classes(rows):
    """Kosaraju's algorithm, including singleton holding classes."""
    def postorder(graph):
        seen = set()
        finish = []
        for start in range(len(graph)):
            if start in seen:
                continue
            seen.add(start)
            stack = [(start, iter(graph[start]))]
            while stack:
                vertex, edges = stack[-1]
                dest = next(edges, None)
                if dest is None:
                    finish.append(vertex)
                    stack.pop()
                elif dest not in seen:
                    seen.add(dest)
                    stack.append((dest, iter(graph[dest])))
        return finish

    incoming = [[] for _ in rows]
    for i, row in enumerate(rows):
        for j in row:
            incoming[j].append(i)
    assigned = set()
    closed = []
    for start in reversed(postorder(rows)):
        if start in assigned:
            continue
        comp = {start}
        assigned.add(start)
        stack = [start]
        while stack:
            i = stack.pop()
            for j in incoming[i]:
                if j not in assigned:
                    assigned.add(j)
                    comp.add(j)
                    stack.append(j)
        if all(j in comp for i in comp for j in rows[i]):
            closed.append(comp)
    return closed


def dissection(states, vertices):
    """Eliminate smaller rectangles before their separating grid lines."""
    if len(vertices) <= 16:
        return sorted(vertices)
    lo = [min(states[i][k] for i in vertices) for k in (0, 1)]
    hi = [max(states[i][k] for i in vertices) for k in (0, 1)]
    axis = int(hi[1] - lo[1] > hi[0] - lo[0])
    mid = (lo[axis] + hi[axis]) // 2
    left, right, seam = [], [], []
    for i in vertices:
        v = states[i][axis]
        dest = left if v < mid else right if v > mid else seam
        dest.append(i)
    return dissection(states, left) + dissection(states, right) + sorted(seam)


def stationary(rows, order, *, zero=ZERO, one=ONE):
    """Censor successive states, solve global balance in reverse order.

    rows contains off-diagonal nonnegative one-step weights. Destructively
    updates rows. order must consist of the single closed communicating class.
    Pass Fraction identities for exact rational rows.
    """
    incoming = [set() for _ in rows]
    for i in order:
        for j in rows[i]:
            incoming[j].add(i)
    history = []
    for k in order[:-1]:
        row = rows[k]
        rate = sum(row.values(), zero)
        probs = [(j, w / rate) for j, w in row.items()]
        for j, _ in probs:
            incoming[j].remove(k)
        terms = []
        for i in incoming[k]:
            source = rows[i]
            w = source.pop(k)
            terms.append((i, w))
            for j, prob in probs:
                if i == j:
                    continue
                if j not in source:
                    source[j] = w * prob
                    incoming[j].add(i)
                else:
                    source[j] += w * prob
        history.append((k, rate, terms))
        row.clear()
        incoming[k].clear()
    weights = [zero] * len(rows)
    weights[order[-1]] = one
    for k, rate, terms in reversed(history):
        weights[k] = sum((weights[i] * w for i, w in terms), zero) / rate
    total = sum(weights, zero)
    return [x / total for x in weights]


def moves(x, n, win, kind, exact=False):
    """x=0 is deepest C, x=n-1 shallow C, x=n shallow D, x=2n-1 deepest D."""
    one = Fraction(1) if exact else ONE
    half = Fraction(1, 2) if exact else HALF
    deepen = -1 if x < n else 1
    if win:
        if kind == 'D':
            return [(0 if x < n else 2 * n - 1, one)]
        return [(min(2 * n - 1, max(0, x + deepen)), one)]
    if kind == 'B' and x in (n - 1, n):
        return [(x, half), (x - deepen, half)]
    return [(x - deepen, one)]


def _validate_and_tables(n1, n2, game, kappa_r, kappa_p, kind, lump):
    if min(n1, n2) < 1 or kind not in ('L', 'B', 'D', 'K'):
        raise ValueError('Use positive memory depths and architecture L, B, D or K.')
    if lump and n1 != n2:
        raise ValueError('Exchange lumping requires equal memory depths (n1 == n2).')
    r, p, t, s = (Fraction(str(x)) for x in game)
    if any(not 0 < x < 1 for x in (r, p, t, s)):
        raise ValueError('Each game entry must be strictly between 0 and 1.')
    kap_r, kap_p = (Fraction(str(x)) for x in (kappa_r, kappa_p))
    profiles = [(r, r, kap_r), (s, t, Fraction(0)), (t, s, Fraction(0)), (p, p, kap_p)]
    exact_tables = []
    for p1, p2, kappa in profiles:
        cov = kappa * p1 * (1 - p1)  # nonzero only at a symmetric profile
        q1, q2 = 1 - p1, 1 - p2
        if min(p1*p2+cov, q1*q2+cov, p1*q2-cov, q1*p2-cov) < 0:
            raise ValueError('Infeasible feedback correlation.')
        if kind == 'K':
            q1, q2, cov = q1/2, q2/2, cov/4
            p1, p2 = 1-q1, 1-q2
        outcomes = [(True, True, p1*p2+cov), (True, False, p1*q2-cov),
                    (False, True, q1*p2-cov), (False, False, q1*q2+cov)]
        exact_tables.append([(w1, w2, w) for w1, w2, w in outcomes if w])
    return exact_tables


def game_rows_exact(n1, n2, game, kappa_r, kappa_p, kind, lump):
    """Build exact Fraction transition rows directly from rational inputs (no Decimal rounding)."""
    exact_tables = _validate_and_tables(n1, n2, game, kappa_r, kappa_p, kind, lump)
    states = [(i, j) for i in range(2*n1) for j in range(i if lump else 0, 2*n2)]
    index = {state: i for i, state in enumerate(states)}
    rows = []
    for idx, (i, j) in enumerate(states):
        row = defaultdict(Fraction)
        for w1, w2, prob in exact_tables[2*int(i >= n1) + int(j >= n2)]:
            for ii, h in moves(i, n1, w1, kind, exact=True):
                for jj, k in moves(j, n2, w2, kind, exact=True):
                    dest = index[(jj, ii) if lump and ii > jj else (ii, jj)]
                    if dest != idx:
                        row[dest] += prob * h * k
        rows.append(dict(row))
    return states, rows


def game_rows(n1, n2, game, kappa_r, kappa_p, kind, lump):
    """Build a labeled or exchange-lumped chain; K integrates its private coins."""
    exact_tables = _validate_and_tables(n1, n2, game, kappa_r, kappa_p, kind, lump)
    tables = [[(w1, w2, Decimal(w.numerator)/Decimal(w.denominator))
               for w1, w2, w in tab] for tab in exact_tables]
    states = [(i,j) for i in range(2*n1) for j in range(i if lump else 0, 2*n2)]
    index = {state: i for i, state in enumerate(states)}
    rows = []
    for idx, (i,j) in enumerate(states):
        row = defaultdict(Decimal)
        for w1, w2, prob in tables[2*int(i>=n1)+int(j>=n2)]:
            for ii,h in moves(i,n1,w1,kind):
                for jj,k in moves(j,n2,w2,kind):
                    dest = index[(jj,ii) if lump and ii>jj else (ii,jj)]
                    if dest != idx:
                        row[dest] += prob*h*k
        rows.append(dict(row))
    return states, rows


def solve_game(n1, n2, game, kappa_r='0', kappa_p='0', kind='L', digits=70,
               lump=True):
    """Return stationary (CC, CD, DC, DD), mixed-profile feedback independent.

    Supports reducibility with a single closed class. Refuses ambiguous stationary
    laws. The exchange quotient is automatic for equal memory, unless disabled.
    """
    with localcontext() as ctx:
        ctx.prec = digits
        lump = lump and n1 == n2
        states, rows = game_rows(n1, n2, game, kappa_r, kappa_p, kind, lump)
        classes = closed_classes(rows)
        if len(classes) != 1:
            raise ValueError(f'{len(classes)} closed classes; initial law is needed.')
        active = classes[0]
        if kind == 'D':
            # Sending all deep-reset rows/columns to the final separator prevents
            # their long-range edges from filling the entire grid prematurely.
            reset = [i for i in active if states[i][0] in (0,2*n1-1)
                     or states[i][1] in (0,2*n2-1)]
            order = dissection(states, active.difference(reset)) + sorted(reset)
        else:
            order = dissection(states, active)
        pi = stationary(rows, order)
        mass = [ZERO] * 4
        for (i,j), w in zip(states,pi):
            mass[2*int(i>=n1)+int(j>=n2)] += w
        if lump:
            mass[1] = mass[2] = (mass[1] + mass[2])/TWO
        return tuple(mass)
