"""High-precision checks for reflected tails and synchronized linear automata.

Run with a Python containing mpmath, e.g. `python experiments/phase1_mixing.py`.
Use --tv to also diagonalize the synchronized birth-and-death path.
"""

import argparse
from fractions import Fraction
from math import lcm

import mpmath as mp


def mp_fraction(value):
    return mp.mpf(value.numerator) / value.denominator


def ladder_scale(p, kappa, n):
    """Return sqrt(n)*exp(2tn)*P(X hits first level n, Y hits n afterward).

    The named ordered event permits an earlier visit of Y to n. Fourier
    inversion is applied after a change of measure, so the quadrature
    never subtracts nearly equal crossing probabilities.
    """
    q = 1 - p
    delta = p - q
    a = q * q + kappa * p * q
    b = p * q * (1 - kappa)
    c = p * p + kappa * p * q
    t = mp.log(c / a) / 2
    lam = mp.log(p / q)
    positive_weight = mp.exp(-2 * t)
    negative_weight = mp.exp(-2 * (lam - t))
    sigma = mp.sqrt(8 * b / delta)
    limit = 2 / (sigma * mp.sqrt(2 * mp.pi)) * (
        1 / (1 - positive_weight) + negative_weight / (1 - negative_weight)
    )

    def integrand(u):
        phase = mp.expj(u)
        plus = c * phase + b / phase
        minus = b * phase + a / phase
        ladder = 2 * plus / (1 + mp.sqrt(1 - 4 * plus * minus))
        centered = ladder / phase
        pos = positive_weight / phase**2
        neg = negative_weight * phase**2
        return mp.re(centered**n * (1 / (1 - pos) + neg / (1 - neg)))

    cuts = [mp.mpf(0), 1 / mp.sqrt(n), 4 / mp.sqrt(n), mp.pi / 2]
    cuts = sorted({x for x in cuts if x <= mp.pi / 2})
    integral = 2 * mp.quad(integrand, cuts) / mp.pi
    return mp.sqrt(n) * integral, limit


def path_parameters(n, p_d, p_c):
    """Left/right holding rates and unnormalized reversible masses, D to C."""
    q_d, q_c = 1 - p_d, 1 - p_c
    r_d, r_c = p_d / q_d, p_c / q_c
    left = [0] + [p_d] * (n - 1) + [q_c] * n
    right = [q_d] * n + [p_c] * (n - 1) + [0]
    mass = [r_d**d / q_d for d in reversed(range(n))]
    mass.extend(r_c**d / q_c for d in range(n))
    return left, right, mass


def crossing_statistics(left, right, mass, target, s=None):
    """Two independent mean formulas, plus the exact transform by recursion."""
    prefix_mass = 0
    resistance_mean = 0
    step_mean = 0
    recurrence_mean = 0
    step_transform = 0
    transform = 1
    if s is not None:
        exp_s = mp.exp(s)
    for i in range(target):
        prefix_mass += mass[i]
        resistance_mean += prefix_mass / (mass[i] * right[i])
        step_mean = (1 + left[i] * step_mean) / right[i]
        recurrence_mean += step_mean
        if s is not None:
            stay = 1 - left[i] - right[i]
            step_transform = right[i] / (exp_s - stay - left[i] * step_transform)
            transform *= step_transform
    return resistance_mean, recurrence_mean, transform


def check_mixing():
    p_d, p_c = mp.mpf("0.7"), mp.mpf("0.8")
    r_d, r_c = p_d / (1 - p_d), p_c / (1 - p_c)
    resistance = 1 + 1 / (r_d - 1) + 1 / (r_c - 1)
    print("Synchronized D-deep to C-deep passage")
    print("n   mean/scale           Laplace(1/scale)       reverse/forward mean")
    for n in (4, 8, 16, 32, 64, 96):
        parameters = path_parameters(n, p_d, p_c)
        scale = resistance * (r_d**n - 1) / (2 * p_d - 1)
        mean, recurrence, lap = crossing_statistics(
            *parameters, 2 * n - 1, s=1 / scale
        )
        assert mp.almosteq(mean, recurrence, rel_eps=mp.mpf("1e-78")), (
            "Independent crossing means disagree"
        )
        means_reverse = crossing_statistics(
            *path_parameters(n, p_c, p_d), 2 * n - 1
        )
        print(f"{n:2}  {mp.nstr(mean / scale, 15):20} "
              f"{mp.nstr(lap, 15):21} {mp.nstr(means_reverse[0] / mean, 12)}")
    # Exact rationals exercise both edge orientations and the reflecting ends.
    for n in (1, 2, 5, 16):
        left, right, mass = path_parameters(n, Fraction(7, 10), Fraction(4, 5))
        assert all(mass[i] * right[i] == mass[i + 1] * left[i + 1]
                   for i in range(2 * n - 1))
        mean, other_mean, _ = crossing_statistics(left, right, mass, 2 * n - 1)
        assert mean == other_mean


def check_tv():
    """Direct maximum TV over rows of the closed class, in 85-digit arithmetic."""
    p_d, p_c = mp.mpf("0.7"), mp.mpf("0.8")
    print("n   max TV at the predicted scale    reference exp(-1)         gap*R*M_eff")
    for n in (4, 8, 16, 24):
        left, right, mass = path_parameters(n, p_d, p_c)
        dimension = 2 * n
        matrix = mp.matrix(dimension)
        for i in range(dimension):
            matrix[i, i] = 1 - left[i] - right[i]
            if i + 1 < dimension:
                edge = mp.sqrt(right[i] * left[i + 1])
                matrix[i, i + 1] = matrix[i + 1, i] = edge
        values, vectors = mp.eigsy(matrix)
        assert mp.almosteq(values[dimension - 1], 1, rel_eps=mp.mpf("1e-78"))
        scale = (mp.mpf(25) / 12) * sum(mass[:n])
        time = int(mp.floor(scale))
        # Remove the stationary eigenvector analytically.
        factors = mp.diag([values[k]**time for k in range(dimension - 1)] + [0])
        difference = vectors * factors * vectors.T
        tv = max(sum(abs(difference[i, j]) * mp.sqrt(mass[j] / mass[i])
                     for j in range(dimension)) / 2 for i in range(dimension))
        m_d, m_c = sum(mass[:n]), sum(mass[n:])
        gap_scale = (mp.mpf(25)/12)/(1/m_d+1/m_c)
        actual_gap = 1-max(abs(values[k]) for k in range(dimension-1))
        print(f"{n:2}  {mp.nstr(tv, 22):30} {mp.nstr(mp.exp(-1), 22):25} "
              f"{mp.nstr(actual_gap*gap_scale, 14)}")


def first_flip_spectrum(n, p):
    """Spectral weights for the first exit time of one frozen branch."""
    q = 1-p
    killed = mp.matrix(n)
    killed[0, 0] = p
    for i in range(n-1):
        killed[i, i+1] = killed[i+1, i] = mp.sqrt(p*q)
    values, vectors = mp.eigsy(killed)
    factor = q*(q/p)**(mp.mpf(n-1)/2)
    return [(values[j], factor*vectors[0,j]*vectors[n-1,j]) for j in range(n)]


def check_independent_flips():
    print("Independent first action changes, p=0.7")
    print("n   P(tie)/(rho/2)         E(time)*2*rho")
    p = mp.mpf("0.7")
    for n in (4, 8, 16, 32):
        terms = first_flip_spectrum(n, p)
        tie = mp.mpf(0)
        mean = mp.mpf(0)
        for x, a in terms:
            for y, b in terms:
                contribution = a*b/(1-x*y)
                tie += contribution
                mean += contribution/((1-x)*(1-y))
        rho = (2*p-1)**2/p*((1-p)/p)**n
        print(f"{n:2}  {mp.nstr(2*tie/rho, 16):22} {mp.nstr(mean*2*rho, 16)}")


def certified_tail(n, p, kappa, digits, ordered_tilt=False):
    """Enclose the scaled H_n using only rational transitions and integers.

    The scale is exp(2tn) in the diagonal tilt or exp((h+lambda)n) in the
    ordered tilt. Both tilted coordinates must have positive drift for this
    finite lower cutoff certificate. Discarded paths, the iteration horizon,
    and every downward rounding contribute to the explicit upper endpoint.
    """
    import numpy as np

    q = 1 - p
    a = q*q + kappa*p*q
    b = p*q*(1-kappa)
    c = p*p + kappa*p*q
    if not (Fraction(1, 2) < p < 1 and -q/p <= kappa <= 1):
        raise ValueError("The parameters do not define the stated walk.")
    if ordered_tilt:
        odds = p/q
        second_root = (p-kappa*(p-q))/(q+kappa*(p-q))
        pp, pm, mp_step, mm = a*second_root*odds, b*second_root/odds, b*odds/second_root, c/second_root/odds
        weight = 1
    else:
        if kappa < 0:
            raise ValueError("Use the ordered tilt at negative correlation.")
        pp, pm, mp_step, mm = c, b, b, a
        weight = (q/p)**2 * c/a
    up_x, up_y = pp+pm, pp+mp_step
    lower_odds = max((1-up_x)/up_x, (1-up_y)/up_y)
    if lower_odds >= 1:
        raise ValueError("A tilted coordinate has nonpositive drift at this parameter.")
    goal = Fraction(1, 10**(digits+2))
    scale = 10**(digits+14)
    lower_distance = 1
    while 2*lower_odds**lower_distance > goal:
        lower_distance += 1
    z = (1+(1-up_x)/up_x)/2
    moment = up_x*z + (1-up_x)/z
    time = 0
    time_bound = z**(-n)
    while time_bound > goal:
        time_bound *= moment
        time += 1
    lower = 1 - lower_distance
    grids = []
    for parity in (0, 1):
        first = lower + (parity-lower) % 2
        grids.append(range(first, n, 2))
    denominator = lcm(*(x.denominator for x in (pp, pm, mp_step, mm)))
    steps = [(1, 1, int(denominator*pp)), (1, -1, int(denominator*pm)),
             (-1, 1, int(denominator*mp_step)), (-1, -1, int(denominator*mm))]
    moves = []
    for parity in (0, 1):
        old, new = grids[parity], grids[1-parity]
        trims = {}
        for sign in (-1, 1):
            shift = (old.start + sign - new.start)//2
            start, end = max(0, -shift), min(len(old), len(new)-shift)
            trims[sign] = slice(start, end), slice(start+shift, end+shift)
        transfers = []
        for dx, dy, factor in steps:
            old_x, new_x = trims[dx]
            old_y, new_y = trims[dy]
            transfers.append(((old_x, old_y), (new_x, new_y), factor))
        moves.append(transfers)
    alive = np.zeros((len(grids[0]),)*2, dtype=object)
    origin = grids[0].index(0)
    alive[origin, origin] = scale
    edge_grid = grids[(n-1) % 2]
    edge_visits = np.zeros(len(edge_grid), dtype=object)
    for tick in range(time):
        parity = tick % 2
        if parity == (n-1) % 2:
            edge_visits += alive[-1, :]
        after = np.zeros((len(grids[1-parity]),)*2, dtype=object)
        for origin_slice, dest_slice, factor in moves[parity]:
            after[dest_slice] += factor * alive[origin_slice]
        alive = after // denominator
    total = Fraction(0)
    for y, visits in zip(edge_grid, edge_visits):
        j = (n-1-y)//2
        # One common step from (n-1,n-1) produces a tie counted once.
        common = pp if j == 0 else 2*pp
        total += Fraction(visits, scale) * weight**j * (common + 2*pm*weight)
    error = 2*lower_odds**lower_distance + time_bound + Fraction(
        time * max(map(len, grids))**2, scale
    )
    # Each retained exit has weight at most two in the ordered identity.
    if ordered_tilt:
        error *= 2
    return total, total + error


def certified_taboo_sum(p, kappa, digits):
    """Bound the bracket in (2) by finite Dirichlet iteration with fixed-point integers."""
    import numpy as np

    q = 1-p
    r = q/p
    a = q*q + kappa*p*q
    b = (1-kappa)*p*q
    c = p*p + kappa*p*q
    weight = r*r*c/a
    scale = 10**(digits+14)
    goal = Fraction(1, 10**(digits+2))
    barrier = 3
    while r**barrier > goal:
        barrier += 1
    z = (1+r)/2
    moment = p*z + q/z
    time_bound = z**(-barrier)
    ticks = 0
    while time_bound > goal:
        time_bound *= moment
        ticks += 1
    denominator = lcm(a.denominator, b.denominator, c.denominator)
    ca, cb, cc = (int(denominator*x) for x in (a, b, c))
    # Once a coordinate reaches the upper edge, release its lower constraint.
    # The future ruin probability of that released coordinate is r**barrier.
    survival = np.full((barrier+1, barrier+1), scale, dtype=object)
    survival[0, :] = 0
    survival[:, 0] = 0
    for j in range(1, barrier+1):
        one_survivor = int(scale * (1-r**j))
        survival[barrier, j] = survival[j, barrier] = one_survivor
    for _ in range(ticks):
        survival[1:-1, 1:-1] = (
            cc * survival[2:, 2:] + cb * survival[2:, :-2]
            + cb * survival[:-2, 2:] + ca * survival[:-2, :-2]
        ) // denominator
    def from_one(y):
        if y >= barrier:
            return 1-r
        return Fraction(survival[1, y], scale) if y > 0 else Fraction(0)
    last = barrier//2
    weighted = Fraction(0)
    for j in range(last+1):
        d = 2*j
        survival_estimate = c*from_one(d+1) + b*from_one(d-1)
        multiplicity = 1 if j == 0 else 2
        weighted += multiplicity * weight**j * survival_estimate
    # For the tail in d, 0 <= delta-u_d <= r**d by one-dimensional ruin.
    weighted += 2*(p-q)*weight**(last+1)/(1-weight)
    tail_error = 2*(weight*r*r)**(last+1)/(1-weight*r*r)
    # A path can use the first upper exit only once. Before that exit,
    # survival to 'ticks' implies the first coordinate is still below barrier.
    point_error = r**barrier + time_bound + Fraction(ticks+1, scale)
    error = (1+2*weight/(1-weight))*point_error + tail_error
    return weighted-error, weighted+error


def print_certificates():
    p, kappa = Fraction(4, 5), Fraction(1, 2)
    digits = 52
    lo, hi = certified_taboo_sum(p, kappa, digits)
    sigma = mp.sqrt(mp_fraction(8*p*(1-p)*(1-kappa)/(2*p-1)))
    multiplier = 2/(mp_fraction(2*p-1)*sigma*mp.sqrt(2*mp.pi))
    print("Exact-rational enclosures at p=4/5, kappa=1/2")
    print("C from (2)", mp.nstr(mp_fraction(lo)*multiplier, 51),
          "bracket width before the transcendental multiplier", mp.nstr(mp_fraction(hi-lo), 4))
    for n in (8, 32, 64):
        lo, hi = certified_tail(n, p, kappa, digits)
        print("n", n, "sqrt(n)*exp(2tn)*H_n", mp.nstr(mp.sqrt(n)*mp_fraction(lo), 51),
              "width before sqrt(n)", mp.nstr(mp_fraction(hi-lo), 4))
    for endpoint in (Fraction(0), Fraction(1)):
        lo, hi = certified_tail(6, p, endpoint, digits=15)
        assert lo <= 1 <= hi, "Exact endpoint fell outside the computed enclosure"


def check_windows():
    p = Fraction(4, 5)
    q = 1-p
    delta = p-q
    print("Gaussian window, ordered-tilt normalization")
    for z in (Fraction(-1, 2), Fraction(1, 2)):
        normal_argument = -mp_fraction(z) * mp.sqrt(2*mp_fraction(delta/(p*q)))
        target = 2*mp.ncdf(normal_argument)
        print("z", z, "target", mp.nstr(target, 12))
        for root_n in (4, 8, 12):
            lo, hi = certified_tail(root_n**2, p, z/root_n, digits=18, ordered_tilt=True)
            assert hi-lo < Fraction(1, 10**18)
            print(root_n**2, mp.nstr(mp_fraction(lo), 15))
    print("Poisson window, diagonal-tilt normalization, w=1")
    rate = mp_fraction(p*q/delta)
    odds = mp_fraction(q/p)
    target = mp.exp(-2*rate)*(mp.besseli(0, 2*rate) + 2*mp.nsum(
        lambda j: odds**j * mp.besseli(j, 2*rate), [1, mp.inf]
    ))
    print("target", mp.nstr(target, 14))
    for n in (16, 64, 144):
        lo, hi = certified_tail(n, p, 1-Fraction(1, n), digits=18)
        assert hi-lo < Fraction(1, 10**18)
        print(n, mp.nstr(mp_fraction(lo), 15))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tv", action="store_true", help="also run finite-path spectral TV checks")
    parser.add_argument("--certificates", action="store_true",
                        help="also enclose the joint tail and its coefficient with rational arithmetic")
    parser.add_argument("--windows", action="store_true",
                        help="also check the two near-endpoint limits with finite rational bounds")
    args = parser.parse_args()
    mp.mp.dps = 85
    check_mixing()
    print("Ordered free crossing after diagonal tilting, p=0.7, kappa=0.3")
    print("n      sqrt(n)*exp(2tn)*P(A12)          local-limit coefficient")
    for n in (16, 64, 256, 1024):
        value, limit = ladder_scale(mp.mpf("0.7"), mp.mpf("0.3"), n)
        print(f"{n:4}   {mp.nstr(value, 23):32} {mp.nstr(limit, 23)}")
    if args.tv:
        check_tv()
        check_independent_flips()
    if args.certificates:
        print_certificates()
    if args.windows:
        check_windows()


if __name__ == "__main__":
    main()
