"""Plot full-chain stationary cooperation, preserving a 72-digit data table."""
import argparse
import json
from decimal import Decimal
from pathlib import Path

from phase1_chain import solve_game

STUDY = Path(__file__).resolve().parents[1]
DATA = STUDY / 'experiments' / 'data'
GAME = ('.9375','.8','.8','.5')


def reversal_curve(path, reuse):
    if reuse and path.exists():
        return json.loads(path.read_text())['points']
    points = []
    for n in (1,2,4,6,8,10,12,14,16,18,20,24,32,40,55,70,90,110,135,160):
        cc, _, _, _ = solve_game(n,n,GAME,digits=72)
        points.append({'n':n, 'CC':str(cc)})
    path.write_text(json.dumps({'game':GAME,'digits':72,'points':points},indent=2)+'\n')
    return points


def main(reuse):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import PercentFormatter

    plt.rcParams.update({'font.family':'DejaVu Sans', 'font.size':10,
                         'axes.spines.top':False, 'axes.spines.right':False})
    shocks = json.loads((DATA / 'phase1_shocks.json').read_text())['records']
    reversal = reversal_curve(DATA / 'phase1_reversal_curve.json',reuse)
    fig, axs = plt.subplots(1, 2, figsize=(10.6,4.15),dpi=180)
    fig.subplots_adjust(left=.075,right=.985,bottom=.16,top=.85,wspace=.23)

    for ax in axs:
        ax.set_ylim(-.025,1.04)
        ax.set_xlabel('Memory depth per action, $n$')
        ax.set_yticks([0,.25,.5,.75,1])
        ax.yaxis.set_major_formatter(PercentFormatter(1, decimals=0))
        ax.set_axisbelow(True)
        ax.grid(axis='y',color='#d8dce1',linewidth=.7)
        ax.tick_params(length=3,color='#485663')
    axs[0].set_ylabel('Stationary probability of mutual cooperation')
    axs[0].set_title('Prisoner’s Dilemma',loc='left',pad=17,fontweight='bold')
    for k,color,marker in [('0','#606d7b','o'),('.20','#9d6727','s'),
                           ('.25','#2f6d9a','^'),('.50','#096458','D')]:
        pts = sorted((x for x in shocks if x['family']=='square' and x['kP']==k),
                     key=lambda x:x['n1'])
        axs[0].plot([p['n1'] for p in pts],[float(p['CC']) for p in pts],
                    color=color,marker=marker,ms=4,lw=1.6,label=f'κ = {float(k):.2f}')
    axs[0].set_xticks([12,24,40,60,80])
    axs[0].legend(loc='center',bbox_to_anchor=(.58,.62),frameon=False,fontsize=9)

    ax = axs[1]
    ax.set_title('Constant-hare Stag Hunt',loc='left',pad=17,fontweight='bold')
    ax.plot([p['n'] for p in reversal],[float(p['CC']) for p in reversal],
            color='#774369',marker='o',ms=3,lw=1.7)
    for i,offset in [(16,(12,.93)),(160,(106,.15))]:
        value=next(Decimal(p['CC']) for p in reversal if p['n']==i)
        ax.annotate(f'{value*100:.2f}% at n = {i}',xy=(i,float(value)),
                    xytext=offset,arrowprops=dict(arrowstyle='-',color='#605c65'),
                    fontsize=9,color='#432943')
    ax.set_xticks([1,40,80,120,160])
    out = STUDY / 'figures' / 'phase1_cooperation.png'
    out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(out,facecolor='white')
    plt.close(fig)
    print(out)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse',action='store_true',help='use the saved Stag Hunt data')
    main(parser.parse_args().reuse)
