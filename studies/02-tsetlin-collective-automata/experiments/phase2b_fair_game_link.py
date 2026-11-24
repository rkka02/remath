"""Direct CC breakouts at a fair DD profile, checked against exact game rows.

Depths count states per action. All exact checks use Fraction. Finite spectra
and limiting constants use 105 decimal working digits and export 82 digits.
"""
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from phase1_chain import game_rows_exact
from phase1_fair_corner import long_resolvent, short_spectrum


DATA = Path(__file__).resolve().parent / "data" / "phase2b_fair_game_link.json"
GAME = ("4/5", "1/2", "9/10", "1/5")  # R, P, T, S
OTHER_GAME = ("9/10", "1/2", "3/4", "3/10")
ZERO, ONE = Fraction(0), Fraction(1)
HOLDS = {"L": ZERO, "B": Fraction(1, 4)}
EXPORTED_DIGITS = 82


def numeric(q):
    return mp.mpf(q.numerator) / q.denominator


def display(x):
    return mp.nstr(x, EXPORTED_DIGITS)


def dd_rows(M, N, kind, game):
    """Restrict the labeled interacting game to DD and classify its exit rows."""
    states, off_diagonal = game_rows_exact(M, N, game, 0, 0, kind, lump=False)
    idx = {state: i for i, state in enumerate(states)}
    dd = [idx[2*M-1-x, 2*N-1-y] for x in range(M) for y in range(N)]
    local = {i: j for j, i in enumerate(dd)}
    rows, exits = [], []
    for i in dd:
        row = {local[i]: ONE - sum(off_diagonal[i].values())}
        both = first_only = second_only = ZERO
        for j, p in off_diagonal[i].items():
            u, v = states[j]
            if j in local:
                row[local[j]] = p
            elif u < M and v < N:
                both += p
            elif u < M:
                first_only += p
            else:
                second_only += p
        assert sum(row.values()) + both + first_only + second_only == ONE
        rows.append(row)
        exits.append((both, first_only, second_only))
    return rows, exits


def solve_rewards(rows, rewards, stop):
    """Exact cumulative rewards in a substochastic chain with extra taboo states."""
    active = [i for i in range(len(rows)) if i not in stop]
    count, width = len(active), len(rewards[0])
    system = [[Fraction(i == j) - rows[i].get(j, ZERO) for j in active]
              + list(rewards[i]) for i in active]
    for k, pivot_row in enumerate(system):
        assert pivot_row[k] > 0
        for row in system[k+1:]:
            if row[k]:
                weight = row[k] / pivot_row[k]
                for j in range(k+1, count+width):
                    if pivot_row[j]:
                        row[j] -= weight*pivot_row[j]
    values = [[ZERO]*width for _ in rows]
    for k in reversed(range(count)):
        row = system[k]
        values[active[k]] = [
            (row[count+t] - sum(row[j]*values[active[j]][t]
                                for j in range(k+1, count) if row[j])) / row[k]
            for t in range(width)]
    return values


def first_round(row, reward, continuations):
    return [b + sum(p*continuations[j][k] for j, p in row.items())
            for k, b in enumerate(reward)]


def exact_game(M, N, kind):
    rows, exits = dd_rows(M, N, kind, GAME)
    assert (rows, exits) == dd_rows(M, N, kind, OTHER_GAME)
    c = len(rows)-1
    a = Fraction(1, 2) - HOLDS[kind]
    assert [e[0] for e in exits] == [ZERO]*c + [a*a]
    rewards = [(*exit_row, ONE, Fraction(i == 0), Fraction(i == c))
               for i, exit_row in enumerate(exits)]
    entire = solve_rewards(rows, rewards, set())
    taboo = solve_rewards(rows, rewards, {0})
    first = first_round(rows[0], rewards[0], taboo)
    tie, first_only, second_only, rounds, goo, goc = entire[0]
    gcc = entire[c][-1]
    per, per_first, per_second, per_rounds = first[:4]
    if c:
        hit_reward = [(row.get(c, ZERO),) for row in rows]
        below_corner = solve_rewards(rows, hit_reward, {0, c})
        h = first_round(rows[0], hit_reward[0], below_corner)[0]
        visits = taboo[c][-1]
        assert h == goc/(goo*gcc - goc*goc)
        assert visits == gcc - goc*goc/goo
    else:
        h, visits = ONE, ONE  # first corner hit at time zero
    assert per == h*a*a*visits == a*a*goc/goo
    assert tie == a*a*goc and per+per_first+per_second == 1/goo
    assert tie+first_only+second_only == ONE and per_rounds == rounds/goo
    return {
        "G_oo": goo, "G_oc": goc, "G_cc": gcc,
        "corner_hit_per_excursion": h,
        "corner_visits_after_hit_before_origin_or_exit": visits,
        "immediate_flip_on_first_corner_hit_per_excursion": h*a*a,
        "direct_CC_per_excursion": per,
        "long_only_per_excursion": per_first, "short_only_per_excursion": per_second,
        "any_exit_per_excursion": per+per_first+per_second,
        "first_DD_exit_CC": tie, "first_DD_exit_long_only": first_only,
        "first_DD_exit_short_only": second_only,
        "mean_rounds_to_first_DD_exit": rounds, "mean_rounds_per_excursion": per_rounds,
    }


def endpoint_resolvent(M, z, w):
    """00, 0c and cc entries of the length-M resolvent, in constant work.

    The unperturbed tridiagonal determinants have roots u and u*t**2.
    Factoring out u**M and the common endpoint factor 1-t gives this form.
    """
    u = (1 + mp.sqrt(1 - z*z))/2
    t = z/(2*u)
    transfer = t**(M-1)
    carry = transfer**2 * (t*t - 2*w*t)
    denominator = u*(1 - 2*w*t + t*carry)
    r00 = (1 - 2*w*t - carry)/((1-t)*denominator)
    r0c = transfer*(1+t)/denominator
    rcc = (1 + transfer**2*t)/denominator
    return r00, r0c, rcc


def spectral(M, N, kind):
    """Tensor Green function and first-exit channels, using one short-axis sum."""
    w = numeric(HOLDS[kind])
    a = mp.mpf("0.5") - w
    goo = goc = gcc = long_inclusive = short_inclusive = rounds = mp.mpf(0)
    for z, s00, s0c, scc in short_spectrum(N-1, w):
        r00, r0c, rcc = endpoint_resolvent(M, z, w)
        if 2 <= M <= 12:  # independent tridiagonal determinant recursion
            for v, other in zip((r00, r0c, rcc), long_resolvent(M-1, z, w)):
                assert abs(v-other) < mp.mpf("1e-95")
        mass = a*s0c/(1-z)  # short spectral coefficient of survival
        row_sum = (1-a*z*r0c)/(1-z)  # long survival generating function
        goo += s00*r00
        goc += s0c*r0c
        gcc += scc*rcc
        long_inclusive += a*mass*r0c
        short_inclusive += a*s0c*row_sum
        rounds += mass*row_sum
    tie = a*a*goc
    first_only, second_only = long_inclusive-tie, short_inclusive-tie
    assert abs(tie+first_only+second_only-1) < mp.mpf("1e-89")
    if M*N == 1:
        h = visits = mp.mpf(1)
    else:
        visits = gcc-goc*goc/goo
        h = goc/(goo*visits)
    return {
        "G_oo": goo, "G_oc": goc, "G_cc": gcc,
        "corner_hit_per_excursion": h,
        "corner_visits_after_hit_before_origin_or_exit": visits,
        "immediate_flip_on_first_corner_hit_per_excursion": h*a*a,
        "direct_CC_per_excursion": tie/goo,
        "long_only_per_excursion": first_only/goo, "short_only_per_excursion": second_only/goo,
        "any_exit_per_excursion": 1/goo,
        "first_DD_exit_CC": tie, "first_DD_exit_long_only": first_only,
        "first_DD_exit_short_only": second_only,
        "mean_rounds_to_first_DD_exit": rounds, "mean_rounds_per_excursion": rounds/goo,
    }


def constants(gamma):
    def alternating(power):
        return mp.nsum(lambda k: (-1)**k*(2*k+1)**power
                       / mp.cosh((2*k+1)*gamma*mp.pi/2), [0, mp.inf])

    overlap = 2*mp.pi*alternating(1)
    if gamma == 1:
        assert abs(overlap - mp.gamma(mp.mpf("0.25"))**4/(8*mp.pi**2)) < mp.mpf("1e-98")
    out = {
        "I_gamma": overlap, "direct_CC_per_excursion_times_N2_log_N": mp.pi*overlap/16,
        "first_DD_exit_CC_times_N2": overlap/4,
        "mean_first_DD_exit_rounds_over_N2": 1 - 32*alternating(-3)/mp.pi**3,
        "long_only_probability_at_first_DD_exit": 4*alternating(-1)/mp.pi,
        "any_exit_per_excursion_times_log_N": mp.pi/4,
    }
    for kind, hold in HOLDS.items():
        w = numeric(hold)
        d = 16/mp.pi-4 if kind == "L" else 16*(4*mp.log(3)/mp.pi-1)/5
        hit = mp.pi*overlap/(4*(1-2*w)**2*d)
        out[f"{kind}_limiting_corner_visits_after_hit"] = d
        out[f"{kind}_corner_hit_per_excursion_times_N2_log_N"] = hit
        out[f"{kind}_immediate_flip_per_excursion_times_N2_log_N"] = hit*(mp.mpf("0.5")-w)**2
    return out


def main():
    mp.mp.dps = 105
    exact_cases, spectra, ratios, repeat_checks = [], [], [], []
    for M, N in ((1, 1), (3, 1), (2, 2), (4, 3), (7, 5), (12, 9)):
        for kind in HOLDS:
            exact = exact_game(M, N, kind)
            actual = spectral(M, N, kind)
            error = max(abs(actual[k]/numeric(v)-1) for k, v in exact.items() if v)
            assert error < mp.mpf("1e-90")
            exact_cases.append({"M": M, "N": N, "architecture": kind,
                                "exact": {k: str(v) for k, v in exact.items()},
                                "max_relative_difference_from_spectrum": mp.nstr(error, 6)})
    limits = {}
    for gamma in (1, 3):
        limits[str(gamma)] = {k: display(v) for k, v in constants(gamma).items()}
        for N in (16, 64, 256, 1024, 4096):
            M = gamma*N
            pair = {}
            for kind in HOLDS:
                v = spectral(M, N, kind)
                pair[kind] = v
                if N == 4096:
                    with mp.workdps(135):
                        repeat = spectral(M, N, kind)
                        error = max(abs(v[k]/repeat[k]-1) for k in v)
                        assert error < mp.mpf("1e-90")
                    repeat_checks.append({"M": M, "N": N, "architecture": kind,
                                          "max_relative_difference": mp.nstr(error, 6)})
                scaled = {
                    "direct_CC_per_excursion_times_N2_log_N": v["direct_CC_per_excursion"]*N*N*mp.log(N),
                    "first_DD_exit_CC_times_N2": v["first_DD_exit_CC"]*N*N,
                    "mean_first_DD_exit_rounds_over_N2": v["mean_rounds_to_first_DD_exit"]/N**2,
                    "any_exit_per_excursion_times_log_N": v["any_exit_per_excursion"]*mp.log(N),
                }
                spectra.append({"M": M, "N": N, "architecture": kind,
                                **{k: display(val) for k, val in v.items()},
                                **{k: display(val) for k, val in scaled.items()}})
            keys = ("corner_hit_per_excursion", "immediate_flip_on_first_corner_hit_per_excursion",
                    "direct_CC_per_excursion", "first_DD_exit_CC", "mean_rounds_to_first_DD_exit")
            ratios.append({"M": M, "N": N,
                           **{k: display(pair["B"][k]/pair["L"][k]) for k in keys}})
    output = {
        "working_decimal_digits": mp.mp.dps, "exported_significant_digits": EXPORTED_DIGITS,
        "depths": "M,N count memory states per action. The last DD deficit is (M-1,N-1).",
        "origin_excursion": "Ends on the first positive return to deepest DD or the first action switch.",
        "first_DD_exit": "Allows any number of returns to deepest DD before the first action switch.",
        "exact_checks_full_game_R_P_T_S": [list(GAME), list(OTHER_GAME)],
        "exact_full_game_checks": exact_cases, "limits_by_aspect": limits,
        "spectral_results": spectra, "finite_B_over_L": ratios,
        "repeat_at_135_working_decimal_digits": repeat_checks,
    }
    DATA.parent.mkdir(exist_ok=True)
    DATA.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Wrote {len(exact_cases)} exact checks and {len(spectra)} spectra to {DATA.name}.")
    for item in ratios:
        if item["N"] == 4096:
            print(f'({item["M"]},{item["N"]}) direct per-excursion B/L '
                  f'{item["direct_CC_per_excursion"][:22]}, entire residence '
                  f'{item["first_DD_exit_CC"][:22]}')


if __name__ == "__main__":
    main()
