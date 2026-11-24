#!/usr/bin/env python3
"""Generate Phase 2 prototype visual anatomy figures in figures/."""

from fractions import Fraction
from math import gcd, pi, sqrt, cos, sin, tan, atan, log
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "Arial Unicode MS",
    "mathtext.fontset": "dejavusans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.9,
    "figure.dpi": 220,
})


def certified_shaving_measure(eps):
    """Exact certified frequency measure from Theorem 4b plateaus for equal cut legs u=v=eps."""
    eps_q = Fraction(eps)
    max_n = int(1 / eps_q) + 2
    total_lam = 0.0
    count = 0
    for n in range(2, max_n + 1):
        for m in range(1, n):
            if gcd(m, n) != 1:
                continue
            s_lo_q = Fraction(m, n)
            s_hi_q = Fraction(m, n - eps_q)
            if s_hi_q >= 1:
                continue
            if eps_q * (1 + s_hi_q) < Fraction(1, n):
                count += 1
                s_lo = float(s_lo_q)
                s_hi = float(s_hi_q)
                # Below s=1: [s_lo, s_hi] -> lambda = 1/sqrt(1+s^2)
                dlam_lo = 1.0 / sqrt(1.0 + s_lo**2) - 1.0 / sqrt(1.0 + s_hi**2)
                # Reflected above s=1: [1/s_hi, 1/s_lo] -> lambda = s/sqrt(1+s^2)
                dlam_hi = s_hi / sqrt(1.0 + s_hi**2) - s_lo / sqrt(1.0 + s_lo**2)
                total_lam += dlam_lo + dlam_hi
    return count, total_lam


def make_shaving_and_canonical():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.9))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.86)

    # Panel A: Microscopic corner-shaving jump
    denoms = [8, 16, 32, 64, 128, 256, 512]
    eps_vals = [Fraction(1, d) for d in denoms]
    areas = [0.5 * float(e) ** 2 for e in eps_vals]
    measures = []
    counts = []
    for e in eps_vals:
        c, m = certified_shaving_measure(e)
        counts.append(c)
        measures.append(100.0 * m)
    lim_floor = 100.0 * (6.0 / (pi**2)) * (1.0 - 1.0 / sqrt(2.0))

    ax1.semilogx(areas, measures, "o-", color="#1B5E7A", lw=2.2, ms=6.5,
                 label="Certified attracting plateaus (Thm 4b)")
    ax1.axhline(lim_floor, color="#B23A2A", ls="--", lw=1.6,
                label=r"Exact limit $\frac{6}{\pi^2}(1 - 1/\sqrt{2}) \approx 17.806\%$")
    ax1.scatter([1e-7], [0.0], color="#111111", s=45, zorder=5)
    ax1.annotate("Uncut square\n(area 0 $\\rightarrow$ 0%)",
                 xy=(1e-7, 0.3), xytext=(2.8e-7, 4.2),
                 arrowprops=dict(arrowstyle="->", color="#222222", lw=1.1),
                 fontsize=8.3, color="#222222", ha="center")
    ax1.annotate("39,797 plateaus\n($\\varepsilon = 1/512$, area $1.9\\times 10^{-6}$)",
                 xy=(areas[-1], measures[-1]), xytext=(8e-5, 13.8),
                 arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.1),
                 fontsize=8.4, color="#1B5E7A")
    ax1.invert_xaxis()
    ax1.set_xlim(2e-2, 5e-8)
    ax1.set_ylim(-1.2, 21.0)
    ax1.set_xlabel(r"Removed corner area $\varepsilon^2 / 2$ (shrinking rightwards $\rightarrow 0$)", fontsize=9.8)
    ax1.set_ylabel("Certified attracting frequency share (%)", fontsize=9.8)
    ax1.set_title("A. Microscopic corner shaving: 0% $\\rightarrow \\geq 17.805\\%$ jump", fontsize=10.8, pad=10, fontweight="bold")
    ax1.legend(frameon=False, loc="lower left", fontsize=8.2)
    ax1.grid(alpha=0.22, ls=":")

    # Inset: shaved square + period-3 attractor with contraction -> 1/3
    ins = ax1.inset_axes([0.36, 0.25, 0.32, 0.38])
    eps_vis = 0.22
    poly = np.array([[0, 0], [1, 0], [1, 1 - eps_vis], [1 - eps_vis, 1], [0, 1]])
    ins.add_patch(Polygon(poly, facecolor="#EEF5F8", edgecolor="#1F2933", lw=1.3))
    ins.fill([1 - eps_vis, 1, 1], [1, 1 - eps_vis, 1], color="#F5D0C5", alpha=0.8)
    # Period-3 attracting ray at s = 1/(2 - eps/2), h = p = eps/2
    p = eps_vis / 2.0
    s = 1.0 / (2.0 - p)
    # Six impacts around unit square (from Theorem 4a unfolding)
    pts = [
        (1.0 - p, 1.0 - p),
        (1.0 - (1.0 - p) / s if False else 0.0, 1.0 - p - s * (1.0 - p)),
    ]
    # Trace exact 6-bounce ray starting from bevel (1-p, 1-p) going slope +s backwards / -s
    x0, z0 = 1.0 - p, 1.0 - p
    # slope +s down-left hits left wall x=0 at z1 = z0 - s*x0
    z1 = z0 - s * x0
    # slope -s down-right from (0, z1) hits bottom z=0 at x2 = z1/s
    x2 = z1 / s
    # slope +s up-right from (x2, 0) hits right wall x=1 at z3 = s*(1 - x2)
    z3 = s * (1.0 - x2)
    # slope -s up-left from (1, z3) hits top z=1 at x4 = 1 - (1 - z3)/s
    x4 = 1.0 - (1.0 - z3) / s
    # slope +s down-left from (x4, 1) hits left wall x=0 at z5 = 1 - s*x4
    z5 = 1.0 - s * x4
    # Wait: check return from (0, z5) slope -s down-right -> wait; instead trace unfolded line
    # A=(1-p,1-p) to A'=(-3+p,-1-p) slope s:
    ts = np.linspace(0, 1, 800)
    X = (1.0 - p) + ts * (-4.0 + 2.0 * p)
    Z = (1.0 - p) + ts * (-2.0)
    # Fold via triangle wave mod 2 into [0,1]
    xf = 1.0 - np.abs(((X) % 2.0) - 1.0)
    zf = 1.0 - np.abs(((Z) % 2.0) - 1.0)
    ins.plot(xf, zf, color="#B23A2A", lw=1.4)
    ins.plot([1 - p], [1 - p], "o", color="#B23A2A", ms=4.5)
    ins.set_xlim(-0.06, 1.08)
    ins.set_ylim(-0.06, 1.08)
    ins.set_aspect("equal")
    ins.set_xticks([])
    ins.set_yticks([])
    ins.set_title(r"Bevel factor $\to 1/3$ as $\varepsilon\downarrow 0$", fontsize=7.8, color="#B23A2A", pad=3)

    # Panel B: Tilted rectangle (phi, R) extinction diagram + 5-tank bar inset
    phi_deg = np.linspace(0.5, 44.5, 400)
    phi_rad = np.deg2rad(phi_deg)
    mask_ext = phi_deg >= 22.5
    phi_ext = phi_deg[mask_ext]
    rad_ext = np.deg2rad(phi_ext)
    r_low = 1.0 / np.tan(2.0 * rad_ext)
    r_high = np.tan(2.0 * rad_ext)

    ax2.fill_between(phi_ext, r_low, np.minimum(r_high, 4.5), color="#2D6A7E", alpha=0.28,
                     label=r"$\sigma_p(T) = \varnothing$ (0 standing waves)")
    ax2.plot(phi_ext, r_low, color="#2D6A7E", lw=2.0)
    ax2.plot(phi_ext, np.minimum(r_high, 4.5), color="#2D6A7E", lw=2.0)
    ax2.axhline(1.0, color="#666666", ls=":", lw=1.1)
    ax2.plot([22.5], [1.0], "o", color="#B23A2A", ms=7, zorder=6)
    ax2.annotate(r"Square cliff: $\phi = 22.5^\circ$" + "\n(last standing wave dies)",
                 xy=(22.5, 1.04), xytext=(12.0, 2.38),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.2),
                 fontsize=8.5, color="#B23A2A", fontweight="bold")
    ax2.text(2.2, 3.38, r"Countably $\infty$ standing frequencies" + "\n(each $\\infty$-dim; odd $q$, $b^q = \\mathrm{Id}$)\nRegular attractors: $\\cos\\phi-\\sin\\phi$\n(total with corner capture $= 1$)",
             fontsize=7.8, color="#1F2933",
             bbox=dict(boxstyle="round,pad=0.35", fc="#F7F9FA", ec="#C9D3DC", lw=0.8))
    ax2.text(27.5, 1.05, r"$\cot(2\phi) \leq R \leq \tan(2\phi)$" + "\nZero eigenvalues!",
             fontsize=8.5, color="#1B4D5C", fontweight="bold")
    ax2.set_xlim(0, 45)
    ax2.set_ylim(0.15, 4.45)
    ax2.set_xlabel(r"Reduced rectangle tilt $\phi$ (degrees)", fontsize=9.8)
    ax2.set_ylabel(r"Aspect ratio $R = H/W$", fontsize=9.8)
    ax2.set_title(r"B. Tilted-rectangle extinction cliff & $15^\circ$ parity reversal", fontsize=10.8, pad=10, fontweight="bold")
    ax2.grid(alpha=0.22, ls=":")

    # Inset: 5 equal-slope (15 deg) canonical tanks at lambda = 1/sqrt(2)
    ins2 = ax2.inset_axes([0.08, 0.10, 0.45, 0.32])
    names = ["Upright\n(0°)", "Right\ntrap", "Isosceles\n(/ \\)", "Shear\n(/ /)", "Tilted\nsquare"]
    mults = [1.0, 1.0 / sqrt(3.0), 1.0, 1.0 / 3.0, 1.0 / 9.0]
    colors = ["#4A90A4", "#D97742", "#2A9D8F", "#C84B31", "#7D1D3F"]
    bars = ins2.bar(range(5), mults, color=colors, width=0.60, edgecolor="#1F2933", lw=0.7)
    for idx, (b, val, lbl) in enumerate(zip(bars, mults, ["1", r"$1/\sqrt{3}$", "1!", "1/3", "1/9"])):
        ins2.text(idx, val + 0.04, lbl, ha="center", va="bottom", fontsize=7.4, fontweight="bold")
    ins2.set_xticks(range(5))
    ins2.set_xticklabels(names, fontsize=6.4)
    ins2.set_yticks([0.0, 0.5, 1.0])
    ins2.tick_params(axis="y", labelsize=6.8)
    ins2.set_ylim(0, 1.28)
    ins2.set_title(r"Same $15^\circ$ slant, $\lambda = 1/\sqrt{2}$ (cycle factor)", fontsize=7.5, pad=3)
    ins2.patch.set_alpha(0.95)

    out = FIGS / "phase2_shaving_and_canonical.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print(f"Wrote {out}")


def make_circle_paradox():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.9))
    fig.subplots_adjust(wspace=0.27, left=0.07, right=0.97, bottom=0.14, top=0.86)

    # Panel A: 1002-gon vs Circle universal arcsine law + pinned 1/3 strongest factor
    u_grid = np.linspace(0.015, 0.985, 500)
    ax1.plot(u_grid, 2.0 * pi / np.sin(pi * u_grid), color="#111111", lw=2.1, ls="--",
             label=r"Universal limit $2\pi / \sin(\pi U)$")
    for N, col, ms, alpha in [(22, "#D97742", 5.5, 0.95), (102, "#2A9D8F", 3.5, 0.85), (1002, "#1B5E7A", 1.8, 0.75)]:
        h = pi / N
        L = N // 2 - 1
        js = np.arange(1, L + 1)
        mj = (np.sin(2.0 * js * h) - sin(h)) / (np.sin(2.0 * js * h) + sin(h))
        scaled = -N * np.log(mj)
        uj = 2.0 * js / N
        ax1.plot(uj, scaled, "o", color=col, ms=ms, alpha=alpha, label=f"$N={N}$ ({L} attractors)")
    ax1.set_ylim(0, 62)
    ax1.set_xlim(0, 1)
    ax1.set_xlabel(r"Normalized attractor index $u_j = 2j/N \in (0, 1)$", fontsize=9.8)
    ax1.set_ylabel(r"Rescaled Lyapunov rate $-N\log m_j$", fontsize=9.8)
    ax1.set_title(r"A. $1002$-gon at $\lambda=1/\sqrt{2}$: 500 attractors & $O(N^{-3/2})$ ghost", fontsize=10.8, pad=10, fontweight="bold")
    ax1.legend(frameon=False, loc="upper center", fontsize=8.0)
    ax1.grid(alpha=0.22, ls=":")

    # Inset: Strongest contraction pinned at 1/3 vs quasimode residual O(N^{-3/2})
    ins = ax1.inset_axes([0.23, 0.34, 0.54, 0.41])
    Ns = np.array([6, 10, 14, 22, 42, 102, 1002], dtype=float)
    hs = pi / Ns
    m_min = (2.0 * np.cos(hs) - 1.0) / (2.0 * np.cos(hs) + 1.0)
    # Quasimode analytic upper bound from phase1_regular.md
    a_c = np.cos(hs)
    D2 = (Ns**2 * np.sin(hs)**4 + (2.0 + (Ns - 2.0) * np.sin(hs)**2)**2 * np.tan(hs)**2) / (2.0 * Ns)
    D = np.sqrt(D2)
    resid = D / (2.0 * (a_c**2 - D))
    ins.loglog(Ns, m_min, "s-", color="#B23A2A", lw=1.6, ms=4.5, label=r"Strongest $m_{\min}\to 1/3$")
    ins.loglog(Ns, resid, "o-", color="#1B5E7A", lw=1.6, ms=4.5, label=r"Quasimode err $O(N^{-3/2})$")
    ins.axhline(1.0 / 3.0, color="#B23A2A", ls=":", lw=1.0)
    ins.set_xlabel("$N$ (sides)", fontsize=7.5)
    ins.set_ylabel("Value", fontsize=7.5)
    ins.set_ylim(5e-5, 1.2)
    ins.tick_params(labelsize=7)
    ins.legend(frameon=False, fontsize=6.8, loc="lower left")
    ins.patch.set_alpha(0.94)

    # Panel B: Octagon discontinuous cliff vs Pentagon linear symmetry-breaking split
    phis_deg = np.linspace(0.05, 22.0, 400)
    phis = np.deg2rad(phis_deg)
    # Regular octagon (N=8, h=4, s=1): Theorem 3 of phase1_multiple.md
    # beta = phi in (0, pi/8); t_j = j*pi/8 for j=1,2,3; eps_j = beta (j odd), beta - pi/8 (j even)
    lam_oct = []
    for j in (1, 2, 3):
        tj = j * pi / 8.0
        ej = phis if j % 2 == 1 else (phis - pi / 8.0)
        vals = -np.abs(np.log(np.tan(tj + ej) / np.tan(tj - ej)))
        lam_oct.append(vals)

    ax2.plot(phis_deg, lam_oct[1], color="#B23A2A", lw=2.4,
             label=r"Octagon $j=2$ (25% basin): jumps $0 \rightarrow -2\log(1+\sqrt{2})$")
    ax2.plot(phis_deg, lam_oct[0], color="#2D6A7E", lw=1.8, ls="-.",
             label=r"Octagon $j=1,3$ (37.5% each): continuous from $0$")
    ax2.scatter([0.0], [0.0], color="#111111", s=55, zorder=6, label=r"Untilted octagon ($\phi=0$): $b^2=\mathrm{Id}$, all $\Lambda=0$")
    ax2.scatter([0.0], [-2.0 * log(1.0 + sqrt(2.0))], facecolors="white", edgecolors="#B23A2A", s=55, lw=1.8, zorder=6)

    # Plot the two pentagon branches at s=0.9 ONLY where strict edge-contact inequalities hold
    # (characteristic alignment occurs at 5.9872 deg; verify each point's 4 contact fractions in (0, 1))
    p_deg_grid = np.linspace(0.0, 5.5, 111)
    s_p = 0.9
    def pent_exp_verified(seq, deg_arr):
        valid_deg, valid_lam = [], []
        for deg in deg_arr:
            ph = np.deg2rad(deg)
            # Vertices in physical (x,z) then characteristic (u=z+sx, v=z-sx)
            verts = []
            for j in range(5):
                ang = pi / 2.0 + ph + 2.0 * pi * j / 5.0
                x, z = cos(ang), sin(ang)
                verts.append((z + s_p * x, z - s_p * x))
            # Solve rectangle on edges seq=(i0, i1, i2, i3)
            edges = []
            for k in range(5):
                u0, v0 = verts[k]
                u1, v1 = verts[(k + 1) % 5]
                slope = (u1 - u0) / (v1 - v0)
                edges.append((u0 - slope * v0, slope, v0, v1))
            e0, e1, e2, e3 = [edges[i] for i in seq]
            a0, b0 = e0[0], e0[1]
            a1, b1 = e1[0], e1[1]
            a2, b2 = e2[0], e2[1]
            a3, b3 = e3[0], e3[1]
            M_sw = (b1 * b3) / (b2 * b0)
            if abs(M_sw - 1.0) < 1e-12:
                continue
            off = (a1 - a2) / b2
            lo = ((a3 - a0) + b3 * off) / (b0 * (1.0 - M_sw))
            hi = off + (b1 / b2) * lo
            lt, rt = a0 + b0 * lo, a1 + b1 * lo
            if not (lo < hi and lt < rt):
                continue
            fracs = [(lv - st) / (en - st) for lv, (_, _, st, en) in zip((lo, lo, hi, hi), (e0, e1, e2, e3))]
            if all(1e-6 < f < 1.0 - 1e-6 for f in fracs):
                M = min(abs(M_sw), 1.0 / abs(M_sw))
                valid_deg.append(deg)
                valid_lam.append(0.5 * log(M))
        return np.array(valid_deg), np.array(valid_lam)

    d1, l1 = pent_exp_verified((2, 3, 0, 1), p_deg_grid)
    d2, l2 = pent_exp_verified((2, 3, 4, 1), p_deg_grid)
    ax2.plot(d1, l1, color="#7A4988", lw=2.0, ls="--",
             label=r"Pentagon ($s=0.9$) pair split: $-1.119 \to -2.316,\, -0.517$ at $5^\circ$")
    ax2.plot(d2, l2, color="#7A4988", lw=2.0, ls="--")
    ax2.scatter([5.0, 5.0], [-2.315916, -0.517345], color="#7A4988", s=38, zorder=6)

    ax2.annotate(r"Discontinuous cliff: $-1.7627$" + "\n(factor $3-2\\sqrt{2} = 0.1716$)",
                 xy=(0.25, -1.7627), xytext=(5.5, -1.68),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.2),
                 fontsize=8.2, color="#B23A2A", fontweight="bold")
    ax2.set_xlim(-0.8, 22.5)
    ax2.set_ylim(-3.55, 0.25)
    ax2.set_xlabel(r"Tank tilt $\phi$ (degrees)", fontsize=9.8)
    ax2.set_ylabel(r"Per-step Lyapunov exponent $\Lambda$", fontsize=9.8)
    ax2.set_title("B. Octagon zero-tilt cliff vs. pentagon symmetry split", fontsize=10.8, pad=10, fontweight="bold")
    ax2.legend(frameon=True, facecolor="white", framealpha=0.92, edgecolor="#D9E2EC", loc="lower left", fontsize=7.5)
    ax2.grid(alpha=0.22, ls=":")

    out = FIGS / "phase2_circle_paradox.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_shaving_and_canonical()
    make_circle_paradox()
