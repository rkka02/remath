"""Stationary selection in the unequal-memory dilemma (R,P,T,S)=(.8,.6,.9,.2).

The analytic boundary uses the proved frozen and action-switching kernels. The
finite-chain experiment independently varies only DD feedback correlation.
"""
import argparse
import json
import math
from decimal import Decimal
from pathlib import Path

import mpmath as mp

from fractions import Fraction
from phase1_chain import solve_game
from phase1_interface import bisect_zero, high_correlation
from phase1_negative_krylov import parameters as neg_parameters, phase_certificate
from phase1_quadrant import rate

STUDY = Path(__file__).resolve().parents[1]
DATA = STUDY / 'experiments' / 'data' / 'phase1_aspect.json'
GAME = ('.8', '.6', '.9', '.2')


def _to_exact_fraction(raw) -> Fraction:
    """Convert finite int/float/Decimal/str/Fraction/mpf to exact Fraction without str(mpf) truncation."""
    if isinstance(raw, Fraction):
        return raw
    if isinstance(raw, int):
        return Fraction(raw)
    if isinstance(raw, float):
        if not math.isfinite(raw):
            raise ValueError(f"Non-finite correlation value: {raw!r}")
        return Fraction(raw)
    if isinstance(raw, Decimal):
        if not raw.is_finite():
            raise ValueError(f"Non-finite correlation value: {raw!r}")
        return Fraction(raw)
    if isinstance(raw, mp.mpf):
        if not mp.isfinite(raw):
            raise ValueError(f"Non-finite correlation value: {raw!r}")
        sign, man, exp, _ = raw._mpf_
        if man == 0:
            return Fraction(0)
        val = Fraction(man) * (Fraction(2) ** exp)
        return -val if sign else val
    return Fraction(str(raw))


def critical_ratio(raw, kind):
    """Upper endpoint of strict cooperative ratios gamma >= 1 in this fixed game, or None if empty."""
    p, r, t, s = map(mp.mpf, (GAME[1], GAME[0], GAME[2], GAME[3]))
    hp = mp.log(p/(1-p))
    hr = mp.log(r/(1-r))
    top = hr/hp
    k_f = _to_exact_fraction(raw)
    if not Fraction(-2, 3) <= k_f <= Fraction(1):
        raise ValueError(f"Infeasible DD correlation {k_f} for P=0.6 (must lie in [-2/3, 1]).")
    k = mp.mpf(k_f.numerator) / k_f.denominator
    if k_f < 0:
        # Decide emptiness exactly in rational arithmetic before computing any floating-point root.
        probs_f, law_f = neg_parameters(kind, GAME, k_f)
        _, sign_at_1 = phase_certificate(probs_f, law_f, ratio=1)
        if sign_at_1 <= 0:
            return None
        # Exact certificate proves gamma_c > 1; boost working precision if near onset so root - 1 stays exact.
        old_dps = mp.mp.dps
        need_dps = max(old_dps, 40)
        if sign_at_1 != 0:
            est = max(0, -int(mp.floor(mp.log10(abs(mp.mpf(sign_at_1.numerator) / sign_at_1.denominator)))))
            need_dps = max(need_dps, est + 35)
        try:
            mp.mp.dps = need_dps
            p_hi, r_hi = mp.mpf(GAME[1]), mp.mpf(GAME[0])
            hp_hi, hr_hi = mp.log(p_hi / (1 - p_hi)), mp.log(r_hi / (1 - r_hi))
            offset = rate('.6', str(k_f), 1)[1] - hp_hi
            root = (hr_hi - offset) / hp_hi
        finally:
            mp.mp.dps = old_dps
        return root
    if k > mp.mpf('.5') and top*(2*k-1)>1:
        switch = mp.mpf(1) if kind == 'L' else mp.mpf('.5')
        spec = high_correlation(p,t,s,k,top,switch)
        onset = spec.get('onset of recrossing (memory ratio)')
        if onset is not None:
            root = (hr-spec['short tilt'])/spec['long tilt']
            if root >= onset:
                return root if root >= 1 else None
    # If the transition precedes a strictly active switching edge, the hard
    # exponent agrees with the full exponent at the root.
    def diff(gamma):
        return rate('.6', str(k_f), gamma)[1]-hr
    if diff(mp.mpf(1)) >= 0:
        return None
    if abs(diff(top)) < mp.eps*100:
        return top
    return bisect_zero(diff, mp.mpf(1), top)


def memory_boundaries():
    mp.mp.dps = 80
    result = {}
    for raw in ('-.20', '0', '.20', '.50', '.85', '.99', '1'):
        for kind in ('L','B'):
            result[raw,kind] = critical_ratio(raw,kind)
        print(f'critical memory ratio at k={raw}: L={mp.nstr(result[raw,"L"],66)}, '
              f'B={mp.nstr(result[raw,"B"],66)}')
    assert abs(result['-.20','L']-2) < mp.mpf('1e-72')
    assert abs(result['0','B']-(mp.log(4)/mp.log(mp.mpf('1.5'))-1)) < mp.mpf('1e-72')


def collect():
    mp.mp.dps = 80
    p = mp.mpf(GAME[1])
    hp, hr = mp.log(p/(1-p)), mp.log(4)
    gamma = mp.mpf(3)
    k_opt = (1+1/gamma)/2
    delta = 2*p-1
    curvature = 2*gamma*delta/((1-1/gamma)*(1+delta**2/gamma))
    for eps in map(mp.mpf, ('1e-8','1e-16','1e-24')):
        costs = [rate('.6',mp.nstr(k_opt+sign*eps,80),gamma)[1] for sign in (-1,1)]
        normalized = (sum(costs)/2-gamma*hp)/eps**2
        assert abs(normalized-curvature) < max(50*eps,mp.mpf('1e-28'))
    grid = [str(Decimal(i)/100) for i in range(-30,101,2)]
    gamma_max = hr/hp
    k_peak = (1+1/gamma_max)/2
    points = [dict(k=k,L=mp.nstr(critical_ratio(k,'L'),70),
                   B=mp.nstr(critical_ratio(k,'B'),70)) for k in grid]
    points.append(dict(k=mp.nstr(k_peak,70),L=mp.nstr(gamma_max,70),B=mp.nstr(gamma_max,70)))
    points.sort(key=lambda x: mp.mpf(x['k']))
    full = []
    for n in (16,40):
        for k in ('0','2/3','1'):
            for kind in ('L','B'):
                mass = solve_game(3*n,n,GAME,'0',k,kind,digits=72)
                full.append(dict(n=n,kind=kind,kP=k,CC=str(mass[0]),DD=str(mass[3])))
                print(f'{kind} ({3*n},{n}) DD correlation {k}: CC={mass[0]:.14g}',flush=True)
    out = dict(game=GAME,critical_ratios=points,gamma3_checks=full)
    DATA.write_text(json.dumps(out,indent=2)+'\n')
    return out


def figure(data):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    rows = data['critical_ratios']
    x = [float(row['k']) for row in rows]
    l = [float(row['L']) for row in rows]
    b = [float(row['B']) for row in rows]
    peak = max(range(len(l)),key=l.__getitem__)
    fig,ax=plt.subplots(figsize=(7.5,4.35),dpi=170)
    fig.subplots_adjust(left=.11,right=.965,top=.84,bottom=.17)
    ax.spines[['top','right']].set_visible(False)
    ax.fill_between(x,1,l,color='#d3ebe6')
    ax.fill_between(x,l,b,color='#efdfc4')
    ax.axhline(3,color='#77858b',linestyle=':',linewidth=1)
    ax.plot(x,b,label='Randomized boundary B',color='#aa6820',linewidth=2.4)
    ax.plot(x,l,label='Linear L',color='#126c68',linewidth=2,linestyle='--')
    ax.scatter([x[peak]],[l[peak]],s=23,color='#173f40',zorder=4)
    ax.annotate('Maximum ratio 3.419', (x[peak],l[peak]), xytext=(.23,3.56),
                arrowprops=dict(arrowstyle='-',color='#50696a'),color='#294347')
    ax.text(.04,1.58,'Both tactics select cooperation',color='#1b5756',fontsize=10)
    ax.set(xlim=(min(x),1.01),ylim=(1,3.68),xlabel='DD outcome correlation, κ',
           ylabel='Memory ratio, $n_1/n_2$')
    ax.set_title('How unequal can the two memories be?',loc='left',fontweight='bold',pad=13)
    ax.legend(loc='upper left',fontsize=8.5,frameon=False)
    out=STUDY/'figures'/'phase1_aspect.png'
    fig.savefig(out,facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse',action='store_true',help='redraw the saved analytic grid')
    args=parser.parse_args()
    figure(json.loads(DATA.read_text()) if args.reuse else collect())
