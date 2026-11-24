"""Cross-check the subtraction-free solver and reproduce the correlation data.

Run with a Python containing mpmath, scipy and numpy (only the independent
small-system audit imports the older mpmath oracle and its dependencies).
Full-precision numbers are written to experiments/data/phase1_shocks.json.
"""
import argparse
import json
from decimal import Decimal, localcontext
from pathlib import Path

from phase1_chain import solve_game

GAME = ('.8', '.7', '.9', '.2')  # R, P, T, S
OUT = Path(__file__).resolve().parent / 'data' / 'phase1_shocks.json'
D = Decimal


def validate():
    import mpmath as mp
    from phase1_mpmath_check import exact_2player_mp

    mp.mp.dps = 80
    r,p,t,s = map(D, GAME)
    for architecture in ('L', 'B', 'K', 'D'):
        for n1, n2, kr, kp in [(1,1,'0','.2'), (2,2,'.3','-.10'), (3,2,'-.2','.6')]:
            params = [[(r,r),(s,t)],[(t,s),(p,p)]]
            corr = [[D(kr), D(0)],[D(0),D(kp)]]
            if architecture == 'K':
                # Exact thinning identities independently feed the dense L solver.
                params = [[tuple((1+a)/2 for a in pair) for pair in row] for row in params]
                corr[0][0] *= r/(1+r)
                corr[1][1] *= p/(1+p)
            oracle = exact_2player_mp(n1,n2,params,corr,
                                      'L' if architecture=='K' else architecture,80)
            expected = [x for row in oracle for x in row]
            actual = solve_game(n1,n2,GAME,kr,kp,architecture,72)
            assert max(abs(mp.mpf(str(a))/e-1) for a,e in zip(actual,expected)) < mp.mpf('1e-68')
            if n1 == n2:
                labeled = solve_game(n1,n2,GAME,kr,kp,architecture,65,lump=False)
                assert max(abs(a/b-1) for a,b in zip(actual,labeled)) < D('1e-60')
    # A synchronized closed class supplies an independent exact all-depth test.
    for n in (4,40):
        c = ((r/(1-r))**n-1)/(2*r-1)
        d = ((p/(1-p))**n-1)/(2*p-1)
        mass = solve_game(n,n,GAME,1,1)
        assert abs(mass[0]/mass[3] * d/c-1) < D('1e-63')
        assert mass[1] == mass[2] == 0
    # Cancellation, conditioning, and lumpability checks on a rare-state problem.
    small = solve_game(40,40,GAME,'.5','.5','L',56)
    large = solve_game(40,40,GAME,'.5','.5','L',80)
    assert max(abs(a/b-1) for a,b in zip(small,large)) < D('1e-51')
    # Algebra and finite-chain sign checks for the constant-mean pooling example.
    z = (D(19)-D(340).sqrt())/10
    alpha = 1-z/D('.15')
    odds = lambda x: x/(1-x)
    p, r = D('.7'), D('.8')
    assert abs(odds(p+z)/odds(p-z) - odds(r)/odds(p)) < D('1e-78')
    for fund, sign in [(D('.40'),-1),(D('.80'),1)]:
        deviation = D('.15')*(1-fund)
        mass = solve_game(40,40,(r,p,p+deviation,p-deviation))
        assert (mass[0]-mass[3])*sign > 0
    original_fund = 1 - (D(38) - D(1353).sqrt())/6
    delta = D('.3')*(1-original_fund)
    assert abs(odds(D('.65')+delta)/odds(D('.65')-delta) - odds(r)/odds(p)) < D('1e-78')
    print(f'Constant-mean threshold {alpha:.64f}; original fund threshold {original_fund:.64f}', flush=True)
    print('Passed dense mpmath, labeled/lumped, synchronized and precision checks.',flush=True)


def collect():
    records = []
    def one(n1, n2, kr, kp, kind, family):
        mass = solve_game(n1,n2,GAME,kr,kp,kind,72)
        ratio = (mass[0]/mass[3]).ln()
        row = dict(family=family, n1=n1, n2=n2, kR=kr, kP=kp, kind=kind,
                   CC=str(mass[0]), CD=str(mass[1]), DC=str(mass[2]),
                   DD=str(mass[3]), log_odds=str(ratio))
        if kind == 'L' and D(kp) >= 0 and n1 == n2:
            p, r = D(GAME[1]), D(GAME[0])
            q = 1-p
            cov = D(kp)*p*q
            slope = (r/(1-r)).ln()-((p*p+cov)/(q*q+cov)).ln()
            beta = -D('.5') if 0 < D(kp) < 1 else D(0)
            row['rescaled_odds'] = str((ratio-n1*slope-beta*D(n1).ln()).exp())
        records.append(row)
        print(f'{kind} ({n1},{n2}) k=({kr},{kp}) CC={mass[0]:.10g}',flush=True)

    for k in ('0','.20','.25','.50'):
        for n in (12,24,40,60,80):
            one(n,n,k,k,'L','square')
    for k in ('-.20','-.35','.85'):
        for n in (24,48):
            one(n,n,'0',k,'L','dd_only')
    for kind in ('B','D','K'):
        for k in ('0','.25','.6','1'):
            one(40,40,k,k,kind,'architecture')
    for nr,nc in ((36,24),(48,24),(60,24)):
        for k in ('-.20','0','.4','.85'):
            one(nr,nc,'0',k,'L','rectangle')
    payload = dict(model='Mixed-profile shocks independent; equal-architecture pairs.',
                   digits=72, game=GAME, records=records)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(payload,indent=2)+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only',action='store_true')
    parser.add_argument('--memory-boundaries', action='store_true',
                        help='also print the unequal-memory phase cuts')
    args = parser.parse_args()
    with localcontext() as ctx:
        ctx.prec = 82
        validate()
        if args.memory_boundaries:
            from phase1_aspect import memory_boundaries
            memory_boundaries()
        if not args.verify_only:
            collect()
