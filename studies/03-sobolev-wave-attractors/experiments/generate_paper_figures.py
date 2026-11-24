#!/usr/bin/env python3
"""Generate all 10 dedicated, non-overlapping publication figures for Study #03.

Outputs:
  papers/paper1_uncloakable_coexistence/figs/p1_fig{1,2,3}_*.png
  papers/paper2_tilt_rigidity_circle_limit/figs/p2_fig{1,2,3}_*.png
  papers/expository_kr/figs/kr_fig{1,2,3,4}_*.png
"""

from fractions import Fraction
from math import gcd, pi, sqrt, cos, sin, tan, atan, log
from pathlib import Path
import sys

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))

P1_FIGS = ROOT / "papers" / "paper1_uncloakable_coexistence" / "figs"
P2_FIGS = ROOT / "papers" / "paper2_tilt_rigidity_circle_limit" / "figs"
KR_FIGS = ROOT / "papers" / "expository_kr" / "figs"
for d in (P1_FIGS, P2_FIGS, KR_FIGS):
    d.mkdir(parents=True, exist_ok=True)

from phase1_probe import square_tongue_labels, SQUARE_SINGULAR
from phase1_coexistence import prescribed_wall
from phase1_measure import neutral_root

plt.rcParams.update({
    "font.family": "Arial Unicode MS",
    "mathtext.fontset": "dejavusans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.9,
    "figure.dpi": 240,
})


def certified_shaving_measure(eps):
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
                dlam_lo = 1.0 / sqrt(1.0 + s_lo**2) - 1.0 / sqrt(1.0 + s_hi**2)
                dlam_hi = s_hi / sqrt(1.0 + s_hi**2) - s_lo / sqrt(1.0 + s_lo**2)
                total_lam += dlam_lo + dlam_hi
    return count, total_lam


def sharp_profile(y):
    """Piecewise-linear profile attaining 0, 1, 0, -1, 0 at 3/4, 13/16, 7/8, 15/16, 1."""
    y = np.asarray(y, dtype=float)
    out = np.zeros_like(y)
    m1 = (y > 0.75) & (y <= 0.8125)
    m2 = (y > 0.8125) & (y <= 0.875)
    m3 = (y > 0.875) & (y <= 0.9375)
    m4 = (y > 0.9375) & (y <= 1.0)
    out[m1] = 16.0 * (y[m1] - 0.75)
    out[m2] = 16.0 * (0.875 - y[m2])
    out[m3] = -16.0 * (y[m3] - 0.875)
    out[m4] = -16.0 * (1.0 - y[m4])
    return out


def pentagon_verified_branches(s_p=0.9, deg_max=5.5, npts=111):
    p_deg_grid = np.linspace(0.0, deg_max, npts)
    res = []
    for seq in ((2, 3, 0, 1), (2, 3, 4, 1)):
        vd, vl = [], []
        for deg in p_deg_grid:
            ph = np.deg2rad(deg)
            verts = []
            for j in range(5):
                ang = pi / 2.0 + ph + 2.0 * pi * j / 5.0
                x, z = cos(ang), sin(ang)
                verts.append((z + s_p * x, z - s_p * x))
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
                vd.append(deg)
                vl.append(0.5 * log(M))
        res.append((np.array(vd), np.array(vl)))
    return res


# ==============================================================================
# PAPER 1 FIGURES (3 dedicated, non-overlapping plates)
# ==============================================================================

def make_p1_fig1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 4.9))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.87)

    # Physical hexagon translated to unit square [0,1]^2:
    # (xi,eta) -> x=(xi-eta)/2 + 1/2, z=(xi+eta)/2 + 1/2
    # Wait: in phase1_coexistence.md, physical vertices are (0,0),(1,0),(1,1/2),(29/36,8/9),(1/4,1),(0,1)
    # where s=x+z-1, t=z-x (shifted by (1/2,1/2) from s=x+z, t=z-x).
    # Let's use shifted unit square coordinates (x,z) in [0,1]^2 with xi = (x+z)-1, eta = z-x.
    # Wait: check (1, 1/2): xi = 1/2, eta = -1/2 -> (1/2, -1/2).
    # (29/36, 8/9): xi = 29/36 + 32/36 - 1 = 25/36, eta = 32/36 - 29/36 = 3/36 = 1/12. Exact!
    # (1/4, 1): xi = 1/4, eta = 3/4. Exact!
    # (0, 1): xi = 0, eta = 1. Exact!
    # (0, 0): xi = -1, eta = 0. Exact!
    # (1, 0): xi = 0, eta = -1. Exact!
    hex_pts = np.array([
        [0.0, 0.0], [1.0, 0.0], [1.0, 0.5],
        [29.0 / 36.0, 8.0 / 9.0], [0.25, 1.0], [0.0, 1.0]
    ])

    # Evaluate u_h on a fine grid inside the hexagon for subtle streamfunction contours
    gx = np.linspace(0.0, 1.0, 400)
    gz = np.linspace(0.0, 1.0, 400)
    X, Z = np.meshgrid(gx, gz)
    XI = X + Z - 1.0
    ETA = Z - X
    R_eta = np.minimum(np.minimum(1.0 - np.abs(ETA), 2.0 / 3.0 + ETA / 3.0), 0.75 - 2.0 * ETA / 3.0)
    inside = (np.abs(ETA) <= 1.0 + 1e-12) & (XI >= np.abs(ETA) - 1.0 - 1e-12) & (XI <= R_eta + 1e-12)
    U = np.where(inside, sharp_profile(1.0 - np.abs(XI)) - sharp_profile(np.abs(ETA)), np.nan)

    # Neutral ribbon background + subtle contours of u_h
    im = ax1.contourf(X, Z, U, levels=np.linspace(-2.0, 2.0, 17), cmap="RdBu_r", alpha=0.52)
    ax1.contour(X, Z, U, levels=[-1.5, -1.0, -0.5, 0.5, 1.0, 1.5], colors="#334E68", linewidths=0.45, alpha=0.55)
    ax1.add_patch(Polygon(hex_pts, facecolor="none", edgecolor="#102A43", lw=2.0, zorder=5))

    # Attracting 4-bounce circuit: corners of [-3/4, 7/12] x [-1/4, 1/4] in (xi, eta)
    # x = (xi - eta + 1)/2, z = (xi + eta + 1)/2
    circ_xe = [(-0.75, -0.25), (7.0 / 12.0, -0.25), (7.0 / 12.0, 0.25), (-0.75, 0.25), (-0.75, -0.25)]
    cx = [0.5 * (xi - eta + 1.0) for xi, eta in circ_xe]
    cz = [0.5 * (xi + eta + 1.0) for xi, eta in circ_xe]
    ax1.plot(cx, cz, color="#B23A2A", lw=2.5, zorder=7, label=r"Attracting circuit ($M=1/2$)")
    ax1.scatter(cx[:-1], cz[:-1], color="#B23A2A", s=34, zorder=8)

    # Explicit global peak |u| = 2 markers of Lean 4's sharpProfile (Uncloakability.lean):
    # (xi, eta) = (1/16, 13/16) -> (x,z) = (1/8, 15/16) and (1/16, -13/16) -> (15/16, 1/8), both u_h = -2
    for xi_p, eta_p, lbl, dx, dy in [
        (1.0 / 16.0, 13.0 / 16.0, r"Global peak $|u_h|=2$", 0.24, 0.09),
        (1.0 / 16.0, -13.0 / 16.0, r"$|u_h|=2$", -0.25, 0.08),
    ]:
        px, pz = 0.5 * (xi_p - eta_p + 1.0), 0.5 * (xi_p + eta_p + 1.0)
        ax1.scatter([px], [pz], marker="*", s=115, color="#1D4ED8", edgecolor="white", lw=0.6, zorder=9)
        ax1.annotate(lbl, xy=(px, pz), xytext=(px + dx, pz + dy),
                     fontsize=8.0, fontweight="bold", color="#1D4ED8",
                     bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.86),
                     arrowprops=dict(arrowstyle="->", color="#1D4ED8", lw=0.9))

    ax1.set_xlim(-0.06, 1.08)
    ax1.set_ylim(-0.15, 1.13)
    ax1.set_aspect("equal")
    ax1.set_xlabel("$x$", fontsize=10)
    ax1.set_ylabel("$z$", fontsize=10)
    ax1.set_title(r"A. Minimal 6-gon ($\lambda=1/\sqrt{2}$): contours & attractor", fontsize=10.6, fontweight="bold", pad=9)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower center", fontsize=7.8)

    # Panel B: Streamfunction trace along leg eta = 1/4 showing exact sharp 1/2 ratio + basin inset
    exact_knots = np.array([-0.75, -0.25, -3.0/16.0, -1.0/8.0, -1.0/16.0, 0.0, 1.0/16.0, 1.0/8.0, 3.0/16.0, 0.25, 7.0/12.0])
    xi_leg = np.unique(np.concatenate([np.linspace(-0.75, 7.0 / 12.0, 600), exact_knots]))
    u_leg = sharp_profile(1.0 - np.abs(xi_leg))
    ax2.plot(xi_leg, u_leg, color="#B23A2A", lw=2.2, label=r"$u_h$ along attractor leg $\eta = 1/4$")
    ax2.axhline(1.0, color="#1B5E7A", ls="--", lw=1.2, label=r"Circuit bound $\|u_h\|_{L^\infty(\Gamma)} = 1$")
    ax2.axhline(-1.0, color="#1B5E7A", ls="--", lw=1.2)
    ax2.axhline(2.0, color="#666666", ls=":", lw=1.2, label=r"Global peak $\|u_h\|_{L^\infty(\Omega)} = 2$ (ratio $1/2$)")
    ax2.axhline(-2.0, color="#666666", ls=":", lw=1.2)
    ax2.axhline(0.0, color="#999999", lw=0.7)
    ax2.set_xlim(-0.78, 0.62)
    ax2.set_ylim(-2.28, 2.38)
    ax2.set_xlabel(r"Characteristic coordinate $\xi = x + z - 1$ along leg $\eta = 1/4$", fontsize=9.6)
    ax2.set_ylabel(r"Streamfunction $u_h$", fontsize=9.8)
    ax2.set_title(r"B. Sharp half-amplitude trace ($\|u\|_{L^\infty(\Gamma)} = \frac{1}{2}\|u\|_{L^\infty(\Omega)}$)", fontsize=10.4, fontweight="bold", pad=9)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper left", fontsize=7.8)
    ax2.grid(alpha=0.22, ls=":")

    # Inset in completely empty bottom-left quadrant (where u_h = 0 on [-0.75, -0.25])
    ins = ax2.inset_axes([0.08, 0.08, 0.32, 0.27])
    cats = ["Neutral\nribbon", "Interior\nattractor", "Neutral\nrim"]
    vals = [0.25, 0.50, 0.25]
    cols = ["#4A90A4", "#B23A2A", "#D97742"]
    ins.bar(range(3), vals, color=cols, width=0.58, edgecolor="#102A43", lw=0.7)
    for i, (v, t) in enumerate(zip(vals, ["1/4", "1/2", "1/4"])):
        ins.text(i, v + 0.03, t, ha="center", va="bottom", fontsize=7.4, fontweight="bold")
    ins.set_xticks(range(3))
    ins.set_xticklabels(cats, fontsize=6.4)
    ins.set_ylim(0, 0.68)
    ins.set_yticks([0, 0.25, 0.5])
    ins.tick_params(axis="y", labelsize=6.4)
    ins.set_title("Horizontal-launch basins", fontsize=7.2, pad=2)
    ins.patch.set_facecolor("white")
    ins.patch.set_alpha(0.96)

    out = P1_FIGS / "p1_fig1_hexagon_uncloakability.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_p1_fig2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 4.9))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.87)

    # Panel A: 8-sided (m=3) prescribed-rate polygon in characteristic (xi, eta)
    r_list = [Fraction(1, 100), Fraction(7, 12), Fraction(2, 3)]
    k_list = [Fraction(16, 17), Fraction(1, 83), Fraction(7, 11)]
    a_cut = Fraction(3, 4)
    # Build exact wall from phase1_coexistence.prescribed_wall
    # Inspect structure of prescribed_wall dynamically
    wdata = prescribed_wall(r_list, k_list, a_cut)
    # Extract vertices from wdata (check return structure cleanly below)
    # To stay self-contained and exact, evaluate R(eta) piecewise directly from the construction:
    G = [Fraction(1)]
    for kp in k_list:
        G.append(G[-1] / kp)
    M_val = G[-1] + 2
    r_ext = [Fraction(0)] + list(r_list) + [a_cut]
    d_slopes = [Fraction(2)]
    for i in range(1, len(r_list) + 1):
        d_slopes.append(((-1)**i) * (G[i] - G[i - 1]))
    d_slopes.append(((-1)**(len(r_list) + 1)) * (M_val - G[-1]))
    d_slopes.append(Fraction(0))
    p_cross = []
    for i in range(1, len(r_list) + 2):
        p_i = (d_slopes[i] * r_ext[i] - d_slopes[i - 1] * r_ext[i - 1]) / (d_slopes[i] - d_slopes[i - 1])
        p_cross.append(p_i)
    p_cross.append(a_cut)
    corners = []
    for i in range(1, len(d_slopes)):
        delta = d_slopes[i] - d_slopes[i - 1]
        pi_v = p_cross[i - 1]
        t_pos = pi_v if delta < 0 else -pi_v
        corners.append((t_pos, abs(delta) / M_val))
    corners.sort(key=lambda pair: pair[0])

    def eval_R(t_arr):
        t_arr = np.asarray(t_arr, dtype=float)
        val = 1.0 + t_arr  # start from R(-1)=0, slope +1
        for tc, drop in corners:
            val = val - float(drop) * np.maximum(t_arr - float(tc), 0.0)
        return val

    ts = np.linspace(-1.0, 1.0, 800)
    Rs = eval_R(ts)
    Ls = np.abs(ts) - 1.0
    ax1.fill_betweenx(ts, Ls, Rs, color="#F0F4F8", zorder=1)
    ax1.plot(Ls, ts, color="#102A43", lw=1.9, zorder=4)
    ax1.plot(Rs, ts, color="#102A43", lw=1.9, zorder=4)
    # Neutral horizontal-launch caps |eta| in [3/4, 1]
    t_top = np.linspace(0.75, 1.0, 100)
    ax1.fill_betweenx(t_top, t_top - 1.0, 1.0 - t_top, color="#4A90A4", alpha=0.35, zorder=2,
                      label=r"Neutral launch caps $|t|\in[3/4,1]$")
    ax1.fill_betweenx(-t_top, t_top - 1.0, 1.0 - t_top, color="#4A90A4", alpha=0.35, zorder=2)

    rect_cols = ["#D97742", "#B23A2A", "#7A4988"]
    rect_lbls = [
        r"$r_1=\frac{1}{100},\ \kappa_1=\frac{16}{17}$",
        r"$r_2=\frac{7}{12},\ \kappa_2=\frac{1}{83}$",
        r"$r_3=\frac{2}{3},\ \kappa_3=\frac{7}{11}$",
    ]
    for r_i, col, lbl in zip(r_list, rect_cols, rect_lbls):
        rf = float(r_i)
        xr = float(eval_R(rf))
        xl = rf - 1.0
        ax1.add_patch(Rectangle((xl, -rf), xr - xl, 2.0 * rf, facecolor="none", edgecolor=col, lw=2.0, zorder=6, label=lbl))
    ax1.set_xlim(-1.14, 0.72)
    ax1.set_ylim(-1.12, 1.06)
    ax1.set_xlabel(r"Characteristic coordinate $s = x + z - 1$", fontsize=9.8)
    ax1.set_ylabel(r"Characteristic coordinate $t = z - x$", fontsize=9.8)
    ax1.set_title(r"A. Prescribed 8-gon ($m=3$): 3 custom attractors + modes", fontsize=10.4, fontweight="bold", pad=9)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.95, edgecolor="#D9E2EC",
               loc="lower left", fontsize=6.9, labelspacing=0.22, handlelength=1.35, borderpad=0.32)
    ax1.grid(alpha=0.2, ls=":")

    # Panel B: Sharp (k, m) feasibility map
    ks = np.arange(3, 15)
    m_all = np.maximum(0, ks - 3)
    m_mix = np.maximum(0, ks - 5)
    m_anyq = np.maximum(0, ks - 4)
    ks_even = np.arange(4, 15, 2)
    m_cent = np.maximum(0, ks_even // 2 - 3)

    ax2.step(ks, m_all, where="mid", color="#102A43", lw=2.2, marker="o", ms=5.5,
             label=r"General max (all periods): $m \leq k - 3$ (sharp)")
    ax2.step(ks, m_anyq, where="mid", color="#7A4988", lw=1.6, ls=":", marker="^", ms=4.5,
             label=r"Mixed upper bound (any $q$): $m \leq k - 4$ ($k=4 \Rightarrow 0$)")
    ax2.step(ks, m_mix, where="mid", color="#B23A2A", lw=2.2, marker="s", ms=5.5,
             label=r"Mixed period-2 max: $m \leq k - 5$ (sharp, min $k=6$)")
    ax2.plot(ks_even, m_cent, "D--", color="#2A9D8F", lw=1.9, ms=5.8,
             label=r"Central $2h$-gon period-2 mixed: $m \leq h - 3$ (min $2h=8$)")
    ax2.axvspan(2.7, 4.4, color="#FDE8E8", alpha=0.55, zorder=0)
    ax2.text(3.55, 7.6, "No mixed\ndynamics\n($k \\leq 4$)", ha="center", fontsize=8.0, color="#9B1C1C", fontweight="bold")
    ax2.annotate("Minimal period-2\nhexagon ($k=6$)", xy=(6.08, 1.04), xytext=(9.2, 2.75),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.1),
                 fontsize=7.9, color="#B23A2A", fontweight="bold")
    ax2.annotate("Minimal central\noctagon ($2h=8$)", xy=(8.08, 0.96), xytext=(10.0, 0.25),
                 arrowprops=dict(arrowstyle="->", color="#2A9D8F", lw=1.1),
                 fontsize=7.9, color="#2A9D8F", fontweight="bold")
    ax2.set_xlim(2.7, 14.4)
    ax2.set_ylim(-0.4, 11.8)
    ax2.set_xticks(ks)
    ax2.set_xlabel("Number of polygon sides $k$", fontsize=9.8)
    ax2.set_ylabel("Upper bound on regular attracting cycles $m$", fontsize=9.6)
    ax2.set_title("B. Side-count bounds for multi-attractor coexistence", fontsize=10.4, fontweight="bold", pad=9)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper left", fontsize=7.6)
    ax2.grid(alpha=0.22, ls=":")

    out = P1_FIGS / "p1_fig2_prescribed_multi_attractors.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_p1_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 4.8))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.87)

    # Panel A: Regular pentagon s=0.9 verified continuous split + odd-N k-3 saturation inset
    (d1, l1), (d2, l2) = pentagon_verified_branches(0.9, 5.5, 111)
    ax1.plot(d1, l1, color="#B23A2A", lw=2.3, label=r"Cycle $(2,3,0,1)$: $-1.119 \rightarrow -2.316$ at $5^\circ$")
    ax1.plot(d2, l2, color="#1B5E7A", lw=2.3, label=r"Cycle $(2,3,4,1)$: $-1.119 \rightarrow -0.517$ at $5^\circ$")
    ax1.scatter([0.0], [-1.119140], color="#102A43", s=55, zorder=6)
    ax1.scatter([5.0, 5.0], [-2.315916, -0.517345], color=["#B23A2A", "#1B5E7A"], s=45, zorder=6)
    ax1.axvline(5.9872, color="#666666", ls=":", lw=1.3, label=r"Char. edge alignment ($5.987^\circ$)")
    ax1.annotate(r"Symmetry pairing ($d\Lambda/d\phi = \pm 8.161$)",
                 xy=(0.06, -1.119), xytext=(1.35, -1.28),
                 arrowprops=dict(arrowstyle="->", color="#102A43", lw=1.0),
                 fontsize=8.1, color="#102A43",
                 bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax1.set_xlim(-0.2, 6.25)
    ax1.set_ylim(-2.95, -0.25)
    ax1.set_xlabel(r"Pentagon tilt $\phi$ from vertex-up (degrees)", fontsize=9.8)
    ax1.set_ylabel(r"Per-step Lyapunov exponent $\Lambda$", fontsize=9.8)
    ax1.set_title(r"A. Regular pentagon ($s=9/10$): $k-3=2$ rate split", fontsize=10.5, fontweight="bold", pad=9)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower left", fontsize=7.8)
    ax1.grid(alpha=0.22, ls=":")

    # Panel B: Common-extremum staircase contraction in a triangle + L-triomino trace obstruction
    # Draw characteristic-coordinate triangle K = {(xi, eta): 0<=xi<=1, 0.25*xi <= eta <= 0.85*xi} (shared corner (0,0))
    tri = np.array([[0.0, 0.0], [1.0, 0.25], [0.85, 0.90]])
    ax2.add_patch(Polygon(tri, facecolor="#EEF5F8", edgecolor="#102A43", lw=2.0, zorder=3))
    # Bounding box
    ax2.plot([0, 1, 1, 0, 0], [0, 0, 0.9, 0.9, 0], color="#829AB1", ls="--", lw=1.1, label="Characteristic bounding box")
    # Staircase iteration T(t) = m(l(t)) -> 0
    # Lower edge: eta = 0.25*xi; Left edge: eta = (0.90/0.85)*xi -> xi = (0.85/0.90)*eta
    t_cur = 0.92
    pts_x, pts_y = [t_cur], [0.25 * t_cur]
    for _ in range(7):
        y_cur = 0.25 * t_cur
        t_next = (0.85 / 0.90) * y_cur
        pts_x.extend([t_next, t_next])
        pts_y.extend([y_cur, 0.25 * t_next])
        t_cur = t_next
    ax2.plot(pts_x, pts_y, color="#B23A2A", lw=1.9, zorder=5, label=r"Zero-trace staircase $A(t)=A(T(t))\to A(0)$")
    ax2.scatter([0.0], [0.0], color="#B23A2A", s=55, zorder=7)
    ax2.annotate("Shared extremum\n$(0,0)$ kills kernel", xy=(0.02, 0.02), xytext=(0.14, 0.65),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.1),
                 fontsize=8.4, fontweight="bold", color="#B23A2A")
    ax2.set_xlim(-0.08, 1.30)
    ax2.set_ylim(-0.08, 1.02)
    ax2.set_xlabel(r"Characteristic $\xi$", fontsize=9.8)
    ax2.set_ylabel(r"Characteristic $\eta$", fontsize=9.8)
    ax2.set_title("B. Common-extremum contraction ($\\sigma_p(T)=\\varnothing$) & L-triomino", fontsize=10.2, fontweight="bold", pad=9)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper left", fontsize=7.5)
    ax2.grid(alpha=0.2, ls=":")

    # Inset completely clear of triangle on right side
    ins = ax2.inset_axes([0.67, 0.08, 0.31, 0.36])
    L_poly = np.array([[0, 0], [2, 0], [2, 1], [1, 1], [1, 2], [0, 2]])
    ins.add_patch(Polygon(L_poly, facecolor="#F7FAFC", edgecolor="#102A43", lw=1.4))
    ins.plot([1, 1], [0, 1], color="#D97742", lw=2.3, ls="--")
    ins.plot([0, 1], [1, 1], color="#D97742", lw=2.3, ls="--")
    ins.text(1.06, 1.48, "L-triomino:\nsine products\nvanish on cuts", fontsize=6.2, color="#9C4221", va="center")
    ins.set_xlim(-0.15, 2.38)
    ins.set_ylim(-0.15, 2.22)
    ins.set_aspect("equal")
    ins.set_xticks([])
    ins.set_yticks([])
    ins.patch.set_facecolor("white")
    ins.patch.set_alpha(0.96)

    out = P1_FIGS / "p1_fig3_pentagon_and_obstructions.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


# ==============================================================================
# PAPER 2 FIGURES (3 dedicated, non-overlapping plates)
# ==============================================================================

def make_p2_fig1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.95))
    fig.subplots_adjust(wspace=0.28, left=0.06, right=0.97, bottom=0.13, top=0.87)

    # Panel A: Exact tilted square Arnold tongues (reusing certified square_tongue_labels!)
    tilt_tenths = np.arange(1, 900, 2)    # 0.05 to 44.95 deg (450 steps)
    angle_tenths = np.arange(1, 1800, 2)  # 0.05 to 89.95 deg (900 steps)
    labels = square_tongue_labels(tilt_tenths, angle_tenths)
    phi_grid = tilt_tenths / 20.0
    theta_grid = angle_tenths / 20.0

    # Map actual square_tongue_labels return codes cleanly to RGB:
    # 0 = other or unclassified, 1 = corner capture,
    # 2..7 = even periods 2, 4, 6, 8, 10, 12, SQUARE_SINGULAR (8) = critical/primary edges
    rgb = np.ones((len(angle_tenths), len(tilt_tenths), 3), dtype=float)
    cmap_dict = {
        0: (1.00, 1.00, 1.00),    # other or unclassified
        1: (0.89, 0.91, 0.94),    # corner capture
        2: (0.16, 0.41, 0.51),    # period 2
        3: (0.85, 0.47, 0.26),    # period 4
        4: (0.45, 0.67, 0.77),    # period 6
        5: (0.58, 0.46, 0.67),    # period 8
        6: (0.36, 0.65, 0.54),    # period 10
        7: (0.89, 0.75, 0.40),    # period 12
        SQUARE_SINGULAR: (0.28, 0.22, 0.34),
    }
    for k, col in cmap_dict.items():
        rgb[labels == k] = col

    ax1.imshow(rgb, origin="lower", aspect="auto", extent=[0, 45, 0, 90], interpolation="nearest")
    # Overlay exact period-3 neutral curves: tan(theta-phi) + tan(theta+phi) = 1 and its complement
    p_c = np.linspace(0.2, 22.4, 300)
    t3_lo, t3_hi = [], []
    for pd in p_c:
        pr = np.deg2rad(pd)
        lo, hi = pr + 1e-6, pi / 4.0
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            if tan(mid - pr) + tan(mid + pr) < 1.0:
                lo = mid
            else:
                hi = mid
        th_deg = np.rad2deg(0.5 * (lo + hi))
        t3_lo.append(th_deg)
        t3_hi.append(90.0 - th_deg)
    ax1.plot(p_c, t3_lo, "--", color="#102A43", lw=1.4)
    ax1.plot(p_c, t3_hi, "--", color="#102A43", lw=1.4)
    ax1.text(28.0, 45.0, "Period 2\n($M=\\mu^{-2}$)", color="white", fontsize=8.8, ha="center", va="center", fontweight="bold")
    ax1.text(35.0, 79.0, "Corner capture", color="#334E68", fontsize=8.2, ha="center", fontweight="bold")
    ax1.text(35.0, 11.0, "Corner capture", color="#334E68", fontsize=8.2, ha="center", fontweight="bold")
    ax1.text(7.0, 27.2, "Period 3 ($b^3=\\mathrm{Id}$)", color="#102A43", fontsize=7.6, fontweight="bold")
    ax1.text(8.5, 17.5, "Per. 4", color="white", fontsize=7.5, fontweight="bold")
    ax1.text(0.8, 86.2, r"Colors: even $q \leq 12$; dark: singular; white: other/unclassified", fontsize=6.4, color="#334E68",
             bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#D9E2EC", alpha=0.92))
    ax1.set_xticks([0, 7.5, 15, 22.5, 30, 37.5, 45])
    ax1.set_yticks([0, 15, 30, 45, 60, 75, 90])
    ax1.set_xlabel(r"Square tilt $\phi$ (degrees)", fontsize=9.8)
    ax1.set_ylabel(r"Ray inclination $\theta$ (degrees)", fontsize=9.8)
    ax1.set_title(r"A. Tilted square ($R=1$): even tongues ($q\leq 12$) & $22.5^\circ$ saturation", fontsize=10.0, fontweight="bold", pad=9)

    # Panel B: Extinction horn carried all the way to the 45 deg viewport limit (clipped at viewport)
    phi_ext = np.concatenate([np.linspace(22.5, 44.99, 600), [45.0]])
    rad_ext = np.deg2rad(phi_ext[:-1])
    r_low = np.concatenate([1.0 / np.tan(2.0 * rad_ext), [0.0]])
    r_high = np.concatenate([np.tan(2.0 * rad_ext), [1e6]])
    ax2.fill_between(phi_ext, r_low, r_high, color="#2D6A7E", alpha=0.28, clip_on=True)
    ax2.plot(phi_ext, r_low, color="#1B5E7A", lw=2.0, clip_on=True)
    ax2.plot(phi_ext, r_high, color="#1B5E7A", lw=2.0, clip_on=True)
    ax2.axhline(1.0, color="#666666", ls=":", lw=1.1)
    ax2.plot([22.5], [1.0], "o", color="#B23A2A", ms=7.2, zorder=8)
    ax2.annotate(r"Square cliff: $\phi = 22.5^\circ$" + "\n(last eigenvalue dies)",
                 xy=(22.5, 1.10), xytext=(22.0, 2.52),
                 arrowprops=dict(arrowstyle="->", color="#9B1C1C", lw=1.9),
                 fontsize=8.3, color="#9B1C1C", fontweight="bold", zorder=12,
                 bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="none", alpha=0.88))
    ax2.text(1.6, 3.42, r"Countably $\infty$ standing frequencies" + "\n(each $\\infty$-dim; odd $q$, $b^q=\\mathrm{Id}$)\nRegular attractors: $\\cos\\phi-\\sin\\phi$\n(total with corner capture $=1$)",
             fontsize=7.6, color="#102A43",
             bbox=dict(boxstyle="round,pad=0.35", fc="#F7FAFC", ec="#BCCCDC", lw=0.8))
    ax2.text(26.5, 1.05, r"$\cot(2\phi)\leq R\leq\tan(2\phi)$" + "\n$\\sigma_p(T)=\\varnothing$",
             fontsize=8.6, color="#102A43", fontweight="bold")
    ax2.set_xlim(0, 45)
    ax2.set_ylim(0.15, 4.55)
    ax2.set_xlabel(r"Reduced rectangle tilt $\phi$ (degrees)", fontsize=9.8)
    ax2.set_ylabel(r"Aspect ratio $R = H/W$", fontsize=9.8)
    ax2.set_title(r"B. Extinction horn & $15^\circ$ five-tank parity reversal", fontsize=10.3, fontweight="bold", pad=9)
    ax2.grid(alpha=0.22, ls=":")

    ins2 = ax2.inset_axes([0.05, 0.08, 0.44, 0.32], zorder=5)
    names = ["Upright\n(0°)", "Right\ntrap", "Isosceles\n(/ \\)", "Shear\n(/ /)", "Tilted\nsquare"]
    mults = [1.0, 1.0 / sqrt(3.0), 1.0, 1.0 / 3.0, 1.0 / 9.0]
    cols = ["#4A90A4", "#D97742", "#2A9D8F", "#C84B31", "#7D1D3F"]
    bars = ins2.bar(range(5), mults, color=cols, width=0.60, edgecolor="#102A43", lw=0.7)
    for idx, (val, lbl) in enumerate(zip(mults, ["1", r"$1/\sqrt{3}$", "1!", "1/3", "1/9"])):
        ins2.text(idx, val + 0.04, lbl, ha="center", va="bottom", fontsize=7.3, fontweight="bold")
    ins2.set_xticks(range(5))
    ins2.set_xticklabels(names, fontsize=6.2)
    ins2.set_yticks([0.0, 0.5, 1.0])
    ins2.tick_params(axis="y", labelsize=6.6)
    ins2.set_ylim(0, 1.32)
    ins2.set_title(r"Same $15^\circ$ slant, $\lambda=1/\sqrt{2}$ (cycle factor)", fontsize=7.2, pad=2)
    ins2.patch.set_facecolor("white")
    ins2.patch.set_alpha(0.96)

    out = P2_FIGS / "p2_fig1_tilted_square_and_extinction.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_p2_fig2():
    # Clean 3-panel layout: A (broken x-axis corner shaving), B (chamfered octagon rigidity), C (re-entry convergence)
    fig = plt.figure(figsize=(13.6, 4.7))
    gs = fig.add_gridspec(1, 4, width_ratios=[3.6, 0.72, 3.2, 2.7], wspace=0.05, left=0.055, right=0.98, bottom=0.14, top=0.86)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1b = fig.add_subplot(gs[0, 1], sharey=ax1)
    ax2 = fig.add_subplot(gs[0, 2])
    ax3 = fig.add_subplot(gs[0, 3])
    # Clean visual gaps between A, B, and C
    p2 = ax2.get_position()
    ax2.set_position([p2.x0 + 0.048, p2.y0, p2.width - 0.048, p2.height])
    p3 = ax3.get_position()
    ax3.set_position([p3.x0 + 0.052, p3.y0, p3.width - 0.052, p3.height])

    denoms = [8, 16, 32, 64, 128, 256, 512]
    eps_vals = [Fraction(1, d) for d in denoms]
    areas = [0.5 * float(e)**2 for e in eps_vals]
    measures = [100.0 * certified_shaving_measure(e)[1] for e in eps_vals]
    lim_floor = 100.0 * (6.0 / (pi**2)) * (1.0 - 1.0 / sqrt(2.0))

    ax1.semilogx(areas, measures, "o-", color="#1B5E7A", lw=2.2, ms=6.0,
                 label="Certified plateau pairs (Thm. 3.4)")
    ax1.axhline(lim_floor, color="#B23A2A", ls="--", lw=1.6,
                label=r"Limit $\frac{6}{\pi^2}(1-1/\sqrt{2}) \approx 17.806\%$")
    ax1b.axhline(lim_floor, color="#B23A2A", ls="--", lw=1.6)
    ax1b.scatter([0.0], [0.0], color="#102A43", s=55, zorder=6)
    ax1b.annotate("Uncut\nsquare\n(0%)", xy=(0.0, 0.45), xytext=(0.0, 4.8),
                  ha="center", fontsize=7.8, color="#102A43", fontweight="bold",
                  arrowprops=dict(arrowstyle="->", color="#102A43", lw=1.1))

    ax1.annotate("39,797 pairs (79,594 plateaus)\n($\\varepsilon=1/512$, 17.728%)", xy=(areas[-1], measures[-1]),
                 xytext=(1.6e-3, 13.0), arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.1),
                 fontsize=7.3, color="#1B5E7A")
    ax1.invert_xaxis()
    ax1.set_xlim(2e-2, 7e-7)
    ax1.set_ylim(-1.2, 21.0)
    ax1b.set_xlim(-0.5, 0.5)
    ax1b.set_xticks([0.0])
    ax1b.set_xticklabels(["0"])
    ax1.spines["right"].set_visible(False)
    ax1b.spines["left"].set_visible(False)
    ax1b.tick_params(labelleft=False, left=False)

    d_mark = 0.020
    kw = dict(transform=ax1.transAxes, color="#102A43", clip_on=False, lw=1.2)
    ax1.plot((1 - d_mark, 1 + d_mark), (-d_mark, +d_mark), **kw)
    kw2 = dict(transform=ax1b.transAxes, color="#102A43", clip_on=False, lw=1.2)
    ax1b.plot((-5 * d_mark, +5 * d_mark), (-d_mark, +d_mark), **kw2)

    ax1.set_xlabel(r"Removed corner area $\varepsilon^2/2$ ($\rightarrow 0$)", fontsize=9.2)
    ax1.set_ylabel("Certified attracting frequency share (%)", fontsize=9.4)
    ax1.set_title(r"A. Corner shaving: sums $\to 17.806\%$ (uncut $= 0\%$)", fontsize=9.9, fontweight="bold", pad=10)
    ax1.legend(frameon=False, loc="lower left", fontsize=7.6)
    ax1.grid(alpha=0.22, ls=":")
    ax1b.grid(alpha=0.22, ls=":")

    ins = ax1.inset_axes([0.52, 0.24, 0.43, 0.40])
    eps_vis = 0.22
    poly = np.array([[0, 0], [1, 0], [1, 1 - eps_vis], [1 - eps_vis, 1], [0, 1]])
    ins.add_patch(Polygon(poly, facecolor="#EEF5F8", edgecolor="#102A43", lw=1.3))
    ins.fill([1 - eps_vis, 1, 1], [1, 1 - eps_vis, 1], color="#F5D0C5", alpha=0.85)
    p = eps_vis / 2.0
    ts = np.linspace(0, 1, 800)
    X = (1.0 - p) + ts * (-4.0 + 2.0 * p)
    Z = (1.0 - p) + ts * (-2.0)
    xf = 1.0 - np.abs((X % 2.0) - 1.0)
    zf = 1.0 - np.abs((Z % 2.0) - 1.0)
    ins.plot(xf, zf, color="#B23A2A", lw=1.4)
    ins.plot([1 - p], [1 - p], "o", color="#B23A2A", ms=4.0)
    ins.set_xlim(-0.06, 1.08)
    ins.set_ylim(-0.06, 1.08)
    ins.set_aspect("equal")
    ins.set_xticks([])
    ins.set_yticks([])
    for sp in ("top", "right", "bottom", "left"):
        ins.spines[sp].set_visible(False)
    ins.set_title(r"Bevel-midpoint factor $\to 1/3$", fontsize=7.1, color="#B23A2A", pad=2)

    # Panel B: Chamfered octagon rigidity (completely unobstructed!)
    oct_v = np.array([[0.5, -1], [1, -0.5], [1, 0.5], [0.5, 1], [-0.5, 1], [-1, 0.5], [-1, -0.5], [-0.5, -1]])
    ax2.add_patch(Polygon(oct_v, facecolor="#F7FAFC", edgecolor="#102A43", lw=1.9, zorder=2))
    orb = np.array([
        [-1.0, -1.0 / 6.0],
        [2.0 / 3.0, 5.0 / 6.0],
        [7.0 / 18.0, 1.0],
        [-1.0, 1.0 / 6.0],
        [2.0 / 3.0, -5.0 / 6.0],
        [7.0 / 18.0, -1.0],
        [-1.0, -1.0 / 6.0],
    ])
    ax2.plot(orb[:, 0], orb[:, 1], color="#B23A2A", lw=2.1, zorder=5,
             label=r"Period-3 ($s=3/5,\, M=1/16$)")
    ax2.scatter(orb[:-1, 0], orb[:-1, 1], color="#B23A2A", s=32, zorder=6)
    ax2.text(0.0, 1.24, r"All 4 axial walls present, yet $\beta_{1/2}=\frac{\log 2}{1+2\log 2}\notin\mathbb{Q}$",
             ha="center", va="center", fontsize=7.4, color="#102A43",
             bbox=dict(boxstyle="round,pad=0.28", fc="white", ec="#BCCCDC", lw=0.8))
    ax2.set_xlim(-1.14, 1.14)
    ax2.set_ylim(-1.38, 1.44)
    ax2.set_aspect("equal")
    ax2.set_xlabel("$x$", fontsize=9.4)
    ax2.set_ylabel("$z$", fontsize=9.4)
    ax2.set_title("B. Chamfered octagon rigidity", fontsize=10.1, fontweight="bold", pad=10)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.95, edgecolor="#D9E2EC", loc="lower center", fontsize=7.5)
    ax2.grid(alpha=0.2, ls=":")

    # Panel C: Live 95-digit computation of geometric re-entry ratio convergence (5 deg square, N=1..64)
    Ns = [1, 2, 4, 8, 16, 32, 64]
    with mp.workdps(95):
        phi5 = mp.radians(5)
        R1 = mp.mpf(1)
        th0 = mp.atan(R1) - phi5
        t0 = mp.tan(2 * phi5)
        C_asymp = t0 / (1 + R1 * t0)
        b_base = (R1 - t0) / (R1 * (1 + R1 * t0))
        ratios_mp = []
        for N_val in Ns:
            thN = neutral_root(phi5, R1, N_val)
            ratios_mp.append((th0 - thN) / (C_asymp * (b_base ** N_val)))
        ratios = [float(r) for r in ratios_mp]
        ratio64_str = mp.nstr(ratios_mp[-1], 12)
    ax3.semilogx(Ns, ratios, "o-", color="#1B5E7A", lw=2.1, ms=5.8,
                 label=r"Actual $(\theta_0-\theta_N)/(C\,b^N)$")
    ax3.axhline(1.0, color="#B23A2A", ls="--", lw=1.4, label="Exact asymptotic limit $1$")
    ax3.annotate(f"$N=64$: ${ratio64_str}$", xy=(64, ratios[-1]), xytext=(4.5, 1.55),
                 arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.1),
                 fontsize=7.8, color="#1B5E7A", fontweight="bold")
    ax3.set_xlim(0.8, 95)
    ax3.set_ylim(0.88, max(2.45, max(ratios) + 0.18))
    ax3.set_xlabel("Re-entry index $N$", fontsize=9.4)
    ax3.set_ylabel("Ratio to geometric law", fontsize=9.4)
    ax3.set_title(r"C. $5^\circ$ square re-entry law", fontsize=10.1, fontweight="bold", pad=10)
    ax3.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper right", fontsize=7.2)
    ax3.grid(alpha=0.22, ls=":")

    out = P2_FIGS / "p2_fig2_shaving_and_rigidity.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_p2_fig3():
    # Clean 3-panel layout: A (1002-gon 500 attractors + ghost inset), B (octagon cliff), C (mod-4 corner fractions)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13.6, 4.7), gridspec_kw={"width_ratios": [1.22, 1.08, 0.88]})
    fig.subplots_adjust(wspace=0.29, left=0.055, right=0.98, bottom=0.14, top=0.86)

    # Panel A: 1002-gon arcsine universal curve + strongest 1/3 vs O(N^{-3/2}) quasimode inset
    u_grid = np.linspace(0.015, 0.985, 500)
    ax1.plot(u_grid, 2.0 * pi / np.sin(pi * u_grid), color="#102A43", lw=2.1, ls="--",
             label=r"Universal law $2\pi / \sin(\pi U)$")
    for N, col, ms, alpha in [(22, "#D97742", 5.2, 0.95), (102, "#2A9D8F", 3.4, 0.85), (1002, "#1B5E7A", 1.8, 0.78)]:
        h = pi / N
        L = N // 2 - 1
        js = np.arange(1, L + 1)
        mj = (np.sin(2.0 * js * h) - sin(h)) / (np.sin(2.0 * js * h) + sin(h))
        ax1.plot(2.0 * js / N, -N * np.log(mj), "o", color=col, ms=ms, alpha=alpha, label=f"$N={N}$ ({L} cycles)")
    ax1.set_ylim(0, 62)
    ax1.set_xlim(0, 1)
    ax1.set_xlabel(r"Normalized index $u_j = 2j/N \in (0, 1)$", fontsize=9.3)
    ax1.set_ylabel(r"Rescaled Lyapunov rate $-N\log m_j$", fontsize=9.4)
    ax1.set_title(r"A. $N=4m+2$ ($\lambda=1/\sqrt{2}$): 500 attractors", fontsize=9.9, fontweight="bold", pad=9)
    ax1.legend(frameon=False, loc="upper center", fontsize=7.4)
    ax1.grid(alpha=0.22, ls=":")

    ins = ax1.inset_axes([0.23, 0.33, 0.54, 0.39])
    Ns = np.array([6, 10, 14, 22, 42, 102, 1002], dtype=float)
    hs = pi / Ns
    m_min = (2.0 * np.cos(hs) - 1.0) / (2.0 * np.cos(hs) + 1.0)
    a_c = np.cos(hs)
    D = np.sqrt((Ns**2 * np.sin(hs)**4 + (2.0 + (Ns - 2.0) * np.sin(hs)**2)**2 * np.tan(hs)**2) / (2.0 * Ns))
    resid = D / (2.0 * (a_c**2 - D))
    ins.loglog(Ns, m_min, "s-", color="#B23A2A", lw=1.5, ms=4.0, label=r"$m_{\min} \to 1/3$")
    ins.loglog(Ns, resid, "o-", color="#1B5E7A", lw=1.5, ms=4.0, label=r"Quasimode bound $O(N^{-3/2})$")
    ins.axhline(1.0 / 3.0, color="#B23A2A", ls=":", lw=1.0)
    ins.set_xlabel("$N$ (sides)", fontsize=7.0)
    ins.set_ylabel("Value", fontsize=7.0)
    ins.set_ylim(5e-5, 1.2)
    ins.tick_params(labelsize=6.5)
    ins.legend(frameon=False, fontsize=6.4, loc="lower left")
    ins.patch.set_facecolor("white")
    ins.patch.set_alpha(0.96)

    # Panel B: Octagon discontinuous cliff (completely unobstructed!)
    phis_deg = np.linspace(0.05, 22.0, 400)
    phis = np.deg2rad(phis_deg)
    lam_oct = []
    for j in (1, 2, 3):
        tj = j * pi / 8.0
        ej = phis if j % 2 == 1 else (phis - pi / 8.0)
        lam_oct.append(-np.abs(np.log(np.tan(tj + ej) / np.tan(tj - ej))))
    ax2.plot(phis_deg, lam_oct[1], color="#B23A2A", lw=2.4,
             label=r"$j=2$ (25% polar): limit $-2\log(1+\sqrt{2})$")
    ax2.plot(phis_deg, lam_oct[0], color="#1B5E7A", lw=1.9, ls="-.",
             label=r"$j=1,3$ (37.5% polar each): continuous")
    ax2.scatter([0.0], [0.0], color="#102A43", s=55, zorder=6, label=r"Aligned ($\phi=0$): $b^2=\mathrm{Id}$, $\Lambda=0$")
    ax2.scatter([0.0], [-2.0 * log(1.0 + sqrt(2.0))], facecolors="white", edgecolors="#B23A2A", s=58, lw=1.8, zorder=6)
    ax2.annotate(r"Discontinuous cliff: $-1.7627$" + "\n(factor $3-2\\sqrt{2}=0.1716$)",
                 xy=(0.35, -1.7627), xytext=(2.8, -2.02),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.3),
                 fontsize=7.7, color="#B23A2A", fontweight="bold")
    ax2.set_xlim(-0.8, 22.5)
    ax2.set_ylim(-3.55, 0.25)
    ax2.set_xlabel(r"Octagon tilt $\phi$ (degrees)", fontsize=9.3)
    ax2.set_ylabel(r"Per-step Lyapunov exponent $\Lambda$", fontsize=9.4)
    ax2.set_title("B. Regular octagon zero-tilt cliff", fontsize=9.9, fontweight="bold", pad=9)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.95, edgecolor="#D9E2EC", loc="lower left", fontsize=6.9)
    ax2.grid(alpha=0.22, ls=":")

    # Panel C: Exact mod-4 corner angular fractions at phi=5 deg
    ns_c = [3, 4, 5, 6, 7, 8, 10, 12, 20]
    fracs_c = [1.0, 8/9, 3/5, 1/3, 3/7, 7/18, 1/5, 2/9, 4/45]
    cols_c = ["#B23A2A" if n % 2 else ("#2A9D8F" if n % 4 == 2 else "#1B5E7A") for n in ns_c]
    ax3.bar(range(len(ns_c)), fracs_c, color=cols_c, width=0.66, edgecolor="#102A43", lw=0.7)
    # Legend proxies
    from matplotlib.patches import Patch
    handles = [
        Patch(facecolor="#B23A2A", edgecolor="#102A43", label=r"Odd: $3/N$ (or $1$)"),
        Patch(facecolor="#2A9D8F", edgecolor="#102A43", label=r"$4m+2$: $2/N$"),
        Patch(facecolor="#1B5E7A", edgecolor="#102A43", label=r"$4m$: $\frac{4}{N}(1-d(0)/h)$"),
    ]
    ax3.set_xticks(range(len(ns_c)))
    ax3.set_xticklabels([str(n) for n in ns_c], fontsize=8.0)
    ax3.set_ylim(0, 1.15)
    ax3.set_xlabel(r"Regular $N$-gon ($\phi = 5^\circ$)", fontsize=9.3)
    ax3.set_ylabel("Corner-capture angular fraction", fontsize=9.4)
    ax3.set_title("C. Exact mod-4 corner capture", fontsize=9.9, fontweight="bold", pad=9)
    ax3.legend(handles=handles, frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper right", fontsize=7.0)
    ax3.grid(axis="y", alpha=0.22, ls=":")

    out = P2_FIGS / "p2_fig3_circle_paradox_and_octagon.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


# ==============================================================================
# KOREAN EXPOSITORY FIGURES (4 dedicated Korean-labeled storytelling plates)
# ==============================================================================

def make_kr_fig1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 4.7))
    fig.subplots_adjust(wspace=0.26, left=0.06, right=0.97, bottom=0.14, top=0.86)

    # Panel A: Ordinary billiard reflection vs Sobolev compass-law beam focusing on a slanted wall
    # Slanted wall from (0.65, 0) to (0.35, 1) (15-20 deg slant)
    wall_x = np.array([0.82, 0.55])
    wall_z = np.array([0.0, 1.0])
    ax1.fill_betweenx(wall_z, wall_x, 1.05, color="#D9E2EC", alpha=0.8)
    ax1.plot(wall_x, wall_z, color="#102A43", lw=2.5)
    # Incoming beam going up-right at 45 deg (slope +1): z - x = c1, c2
    # Wall eq: x = 0.82 - 0.27*z
    # Ray z = x + c -> x = (0.82 - 0.27*c)/1.27, z = (0.82 + c)/1.27
    cs = [-0.42, -0.10]
    hits = []
    for c in cs:
        xh = (0.82 - 0.27 * c) / 1.27
        zh = xh + c
        hits.append((xh, zh))
        ax1.plot([0.05, xh], [0.05 + c, zh], color="#1B5E7A", lw=2.0)
        # Reflected ray at fixed slope -1 (compass law!): z = zh - (x - xh) -> hits z=0 or x=0.05
        x_end = 0.05
        z_end = zh + (xh - x_end)
        if z_end > 0.98:
            z_end = 0.98
            x_end = xh - (z_end - zh)
        ax1.plot([xh, x_end], [zh, z_end], color="#B23A2A", lw=2.2)
    # Shade incoming and outgoing beams
    ax1.fill([0.05, hits[0][0], hits[1][0], 0.05],
             [0.05 + cs[0], hits[0][1], hits[1][1], 0.05 + cs[1]],
             color="#1B5E7A", alpha=0.18, label="입사 파동 다발 (넓은 폭)")
    # Reflected beam polygon
    r0_z = min(0.98, hits[0][1] + (hits[0][0] - 0.05))
    r0_x = hits[0][0] - (r0_z - hits[0][1])
    r1_z = min(0.98, hits[1][1] + (hits[1][0] - 0.05))
    r1_x = hits[1][0] - (r1_z - hits[1][1])
    ax1.fill([hits[0][0], r0_x, r1_x, hits[1][0]],
             [hits[0][1], r0_z, r1_z, hits[1][1]],
             color="#B23A2A", alpha=0.22, label="반사 파동 다발 (좁게 압축!)")
    ax1.annotate("기울기 고정\n($\\pm 45^\\circ$ 나침반 법칙)", xy=(0.30, 0.72), xytext=(0.04, 0.56),
                 fontsize=8.6, color="#B23A2A", fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.2))
    ax1.text(0.86, 0.50, "경사벽", fontsize=9.2, fontweight="bold", color="#102A43", rotation=-75, va="center")
    ax1.set_xlim(0.02, 1.02)
    ax1.set_ylim(0.0, 1.02)
    ax1.set_aspect("equal")
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title("A. 내부파의 '나침반 반사': 경사벽이 파동을 압축한다", fontsize=10.5, fontweight="bold", pad=10)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.92, edgecolor="#D9E2EC", loc="lower left", fontsize=8.2)

    # Panel B: 5 equal-15-deg-slant tanks reversal bar chart in Korean
    names = ["똑바른\n정사각형\n(0°)", "직각\n사다리꼴\n(벽 1개 15°)", "대칭 등변\n사다리꼴\n(/ \\ 15°)", "평행\n사변형\n(/ / 15°)", "통째로 기울인\n정사각형\n(15°)"]
    mults = [1.0, 1.0 / sqrt(3.0), 1.0, 1.0 / 3.0, 1.0 / 9.0]
    cols = ["#4A90A4", "#D97742", "#2A9D8F", "#C84B31", "#7D1D3F"]
    bars = ax2.bar(range(5), mults, color=cols, width=0.58, edgecolor="#102A43", lw=0.9)
    lbls = ["1\n(정상파)", "0.577\n($1/\\sqrt{3}$)", "1!\n(정상파 부활!)", "0.333\n($1/3$)", "0.111\n($1/9$)"]
    for idx, (val, lbl) in enumerate(zip(mults, lbls)):
        ax2.text(idx, val + 0.03, lbl, ha="center", va="bottom", fontsize=8.2, fontweight="bold",
                 color="#1B5E7A" if idx == 2 else "#102A43")
    ax2.axhline(1.0, color="#829AB1", ls="--", lw=0.9)
    ax2.set_xticks(range(5))
    ax2.set_xticklabels(names, fontsize=8.0)
    ax2.set_ylim(0, 1.32)
    ax2.set_ylabel("한 바퀴 순환당 파동 폭 배율 (1 미만 = 블랙홀)", fontsize=9.2)
    ax2.set_title("B. 같은 15° 경사벽의 배신 ($\\lambda = 1/\\sqrt{2}$)", fontsize=10.5, fontweight="bold", pad=10)
    ax2.grid(axis="y", alpha=0.22, ls=":")

    out = KR_FIGS / "kr_fig1_compass_and_two_walls.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_kr_fig2():
    fig = plt.figure(figsize=(12.2, 4.8))
    gs = fig.add_gridspec(1, 3, width_ratios=[4.8, 3.9, 0.8], wspace=0.06, left=0.065, right=0.97, bottom=0.14, top=0.86)
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax2b = fig.add_subplot(gs[0, 2], sharey=ax2)
    p2 = ax2.get_position()
    p2b = ax2b.get_position()
    ax2.set_position([p2.x0 + 0.055, p2.y0, p2.width - 0.045, p2.height])
    ax2b.set_position([p2b.x0 + 0.012, p2b.y0, p2b.width, p2b.height])

    # Panel A: Frequency share of periodic attractors + corner capture vs tilt phi (0.001 to 44.95 deg)
    phi_d = np.linspace(0.001, 44.95, 500)
    phi_r = np.deg2rad(phi_d)
    per_share = 100.0 * (np.cos(phi_r) - np.sin(phi_r))

    ax1.fill_between(phi_d, 0, per_share, color="#1B5E7A", alpha=0.35, label="주기 파동 어트랙터 비율 ($\\cos\\phi - \\sin\\phi$)")
    ax1.fill_between(phi_d, per_share, 100.0, color="#D97742", alpha=0.30, label="꼭짓점 포획 비율 ($1 - \\cos\\phi + \\sin\\phi$)")
    ax1.plot(phi_d, per_share, color="#1B5E7A", lw=2.2)
    ax1.axvline(22.5, color="#B23A2A", ls="--", lw=1.7)
    ax1.scatter([0.0], [0.0], color="#102A43", s=65, zorder=7)
    ax1.scatter([0.0], [100.0], facecolors="white", edgecolors="#1B5E7A", s=65, lw=2.0, zorder=7)
    ax1.annotate("기울기 $0^\\circ$: 블랙홀 0%\n(완전 정상파 기저)", xy=(0.0, 0.0), xytext=(5.5, 14.0),
                 arrowprops=dict(arrowstyle="->", color="#102A43", lw=1.2), fontsize=8.2, fontweight="bold")
    ax1.annotate("$0.001^\\circ$ 기울이면\n즉시 99.998% 도약!", xy=(0.001, 99.9982546555), xytext=(7.2, 86.5),
                 arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.2), fontsize=8.3, color="#1B5E7A", fontweight="bold")
    ax1.text(23.7, 52.0, "$22.5^\\circ$ 절벽\n이후 정사각형\n정상파 0개\n완전 소멸!", fontsize=8.3, color="#B23A2A", fontweight="bold")
    ax1.set_xlim(-1.4, 45.5)
    ax1.set_ylim(-3.0, 107.0)
    ax1.set_xlabel("정사각형 물탱크 기울기 $\\phi$ (도)", fontsize=9.5)
    ax1.set_ylabel("전체 진동수 중 어트랙터 비율 (%)", fontsize=9.5)
    ax1.set_title("A. 종이 한 장 기울기($0.001^\\circ$)의 0% $\\rightarrow$ 99.998% 어트랙터 도약", fontsize=9.9, fontweight="bold", pad=10)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="upper right", fontsize=7.4)
    ax1.grid(alpha=0.2, ls=":")

    # Panel B: Sand-grain bevel shaving with explicit '//' break to uncut square (0%)
    denoms = [8, 16, 32, 64, 128, 256, 512]
    eps_vals = [Fraction(1, d) for d in denoms]
    areas = [0.5 * float(e)**2 for e in eps_vals]
    measures = [100.0 * certified_shaving_measure(e)[1] for e in eps_vals]
    lim_floor = 100.0 * (6.0 / (pi**2)) * (1.0 - 1.0 / sqrt(2.0))

    ax2.semilogx(areas, measures, "o-", color="#1B5E7A", lw=2.3, ms=6.2, label="엄밀 증명된 블랙홀 구간 합계")
    ax2.axhline(lim_floor, color="#B23A2A", ls="--", lw=1.7,
                label=r"증명 구간 합 극한 $\frac{6}{\pi^2}(1-1/\sqrt{2}) \approx 17.806\%$")
    ax2b.axhline(lim_floor, color="#B23A2A", ls="--", lw=1.7)
    ax2b.scatter([0.0], [0.0], color="#102A43", s=60, zorder=6)
    ax2b.annotate("안 깎음\n(0%)", xy=(0.0, 0.5), xytext=(0.0, 4.6),
                  ha="center", fontsize=7.9, color="#102A43", fontweight="bold",
                  arrowprops=dict(arrowstyle="->", color="#102A43", lw=1.1))
    ax2.annotate("39,797쌍 (79,594개 구간)\n17.728% (넓이 $0.00019\\%$)",
                 xy=(areas[-1], measures[-1]), xytext=(1.4e-3, 12.6),
                 arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.2), fontsize=7.6, color="#1B5E7A")
    ax2.text(3.5e-4, 4.6, "깎은 넓이가 0으로 가도\n극한 하한은 17.805% 이상 유지,\n중점 압축 배율은 $1/3$로 수렴!",
             fontsize=7.7, color="#9B1C1C", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.35", fc="#FFF5F5", ec="#FEB2B2", lw=0.9))
    ax2.invert_xaxis()
    ax2.set_xlim(2e-2, 7e-7)
    ax2.set_ylim(-1.0, 21.0)
    ax2b.set_xlim(-0.5, 0.5)
    ax2b.set_xticks([0.0])
    ax2b.set_xticklabels(["0"])
    ax2.spines["right"].set_visible(False)
    ax2b.spines["left"].set_visible(False)
    ax2b.tick_params(labelleft=False, left=False)
    d_mark = 0.020
    kw = dict(transform=ax2.transAxes, color="#102A43", clip_on=False, lw=1.2)
    ax2.plot((1 - d_mark, 1 + d_mark), (-d_mark, +d_mark), **kw)
    kw2 = dict(transform=ax2b.transAxes, color="#102A43", clip_on=False, lw=1.2)
    ax2b.plot((-5 * d_mark, +5 * d_mark), (-d_mark, +d_mark), **kw2)

    ax2.set_xlabel("한쪽 모서리에서 깎아낸 넓이 $\\varepsilon^2/2$ ($\\rightarrow 0$)", fontsize=9.2)
    ax2.set_ylabel("블랙홀 진동수 비율 (%)", fontsize=9.5)
    ax2.set_title("B. 모서리를 모래알만큼 깎아도 극한 17.8% 영구 붕괴", fontsize=9.9, fontweight="bold", pad=10)
    ax2.legend(frameon=False, loc="lower left", fontsize=7.6)
    ax2.grid(alpha=0.22, ls=":")
    ax2b.grid(alpha=0.22, ls=":")

    out = KR_FIGS / "kr_fig2_tilt_and_sand_chip.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_kr_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 4.8))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.86)

    # Panel A: 6-sided tank coexistence in Korean
    hex_pts = np.array([
        [0.0, 0.0], [1.0, 0.0], [1.0, 0.5],
        [29.0 / 36.0, 8.0 / 9.0], [0.25, 1.0], [0.0, 1.0]
    ])
    gx = np.linspace(0.0, 1.0, 360)
    gz = np.linspace(0.0, 1.0, 360)
    X, Z = np.meshgrid(gx, gz)
    XI = X + Z - 1.0
    ETA = Z - X
    R_eta = np.minimum(np.minimum(1.0 - np.abs(ETA), 2.0 / 3.0 + ETA / 3.0), 0.75 - 2.0 * ETA / 3.0)
    inside = (np.abs(ETA) <= 1.0 + 1e-12) & (XI >= np.abs(ETA) - 1.0 - 1e-12) & (XI <= R_eta + 1e-12)
    U = np.where(inside, sharp_profile(1.0 - np.abs(XI)) - sharp_profile(np.abs(ETA)), np.nan)
    ax1.contourf(X, Z, U, levels=np.linspace(-2.0, 2.0, 17), cmap="RdBu_r", alpha=0.52)
    ax1.add_patch(Polygon(hex_pts, facecolor="none", edgecolor="#102A43", lw=2.1, zorder=5))

    circ_xe = [(-0.75, -0.25), (7.0 / 12.0, -0.25), (7.0 / 12.0, 0.25), (-0.75, 0.25), (-0.75, -0.25)]
    cx = [0.5 * (xi - eta + 1.0) for xi, eta in circ_xe]
    cz = [0.5 * (xi + eta + 1.0) for xi, eta in circ_xe]
    ax1.plot(cx, cz, color="#B23A2A", lw=2.5, zorder=7, label="4회 반사 블랙홀 고리 (폭 1/2 압축)")
    ax1.scatter(cx[:-1], cz[:-1], color="#B23A2A", s=34, zorder=8)
    ax1.text(0.45, 0.45, "평화로운 정상파\n대각 통로\n(25% 유역)", ha="center", va="center",
             fontsize=8.2, fontweight="bold", color="#102A43",
             bbox=dict(boxstyle="round,pad=0.25", fc="white", alpha=0.82, ec="none"))
    ax1.annotate("두 번 깎은 모서리\n(최소 6각형!)", xy=(0.81, 0.89), xytext=(0.45, 1.03),
                 arrowprops=dict(arrowstyle="->", color="#102A43", lw=1.1), fontsize=8.0, fontweight="bold")
    ax1.set_xlim(-0.06, 1.07)
    ax1.set_ylim(-0.06, 1.16)
    ax1.set_aspect("equal")
    ax1.set_xlabel("$x$", fontsize=9.6)
    ax1.set_ylabel("$z$", fontsize=9.6)
    ax1.set_title("A. 한 육각형 탱크에 공존하는 정상파와 블랙홀", fontsize=10.5, fontweight="bold", pad=10)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower right", fontsize=8.0)

    # Panel B: 50% uncloakability detector signal (with exact piecewise-linear breakpoints included!)
    exact_knots = np.array([-0.75, -0.25, -3.0/16.0, -1.0/8.0, -1.0/16.0, 0.0, 1.0/16.0, 1.0/8.0, 3.0/16.0, 0.25, 7.0/12.0])
    xi_leg = np.unique(np.concatenate([np.linspace(-0.75, 7.0 / 12.0, 600), exact_knots]))
    u_leg = sharp_profile(1.0 - np.abs(xi_leg))
    ax2.plot(xi_leg, u_leg, color="#B23A2A", lw=2.3, label="블랙홀 고리 위 센서가 감지한 정상파")
    ax2.axhline(1.0, color="#1B5E7A", ls="--", lw=1.3, label="센서 최댓값 = 1 (정확히 50%!)")
    ax2.axhline(-1.0, color="#1B5E7A", ls="--", lw=1.3)
    ax2.axhline(2.0, color="#666666", ls=":", lw=1.3, label="물탱크 전체 최대 진폭 = 2")
    ax2.axhline(-2.0, color="#666666", ls=":", lw=1.3)
    ax2.fill_between(xi_leg, -1.0, 1.0, color="#1B5E7A", alpha=0.08)
    ax2.text(-0.72, 1.48, "어떤 볼록 다각형에서도\n정상파는 숨을 수 없다!\n(반드시 50% 이상 감지)",
             fontsize=8.3, color="#102A43", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.35", fc="#F0F4F8", ec="#BCCCDC", lw=0.8))
    ax2.set_xlim(-0.78, 0.62)
    ax2.set_ylim(-2.28, 2.38)
    ax2.set_xlabel("블랙홀 고리 위 위치 좌표 $\\xi$", fontsize=9.6)
    ax2.set_ylabel("감지된 파동 진폭 $u_h$", fontsize=9.6)
    ax2.set_title("B. 완벽 은폐 불가능 정리: 최소 50% 탐지 법칙", fontsize=10.5, fontweight="bold", pad=10)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower left", fontsize=7.8)
    ax2.grid(alpha=0.22, ls=":")

    out = KR_FIGS / "kr_fig3_impossible_cloak_hexagon.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


def make_kr_fig4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.8))
    fig.subplots_adjust(wspace=0.28, left=0.07, right=0.97, bottom=0.14, top=0.86)

    # Panel A: 1002-gon 500 attractors + 1/3 pinned vs 0.013% ghost wave
    Ns = np.array([6, 10, 14, 22, 42, 102, 1002], dtype=float)
    hs = pi / Ns
    m_min = (2.0 * np.cos(hs) - 1.0) / (2.0 * np.cos(hs) + 1.0)
    a_c = np.cos(hs)
    D = np.sqrt((Ns**2 * np.sin(hs)**4 + (2.0 + (Ns - 2.0) * np.sin(hs)**2)**2 * np.tan(hs)**2) / (2.0 * Ns))
    resid = D / (2.0 * (a_c**2 - D))

    ax1.loglog(Ns, m_min, "s-", color="#B23A2A", lw=2.3, ms=6.5, label="가장 강한 어트랙터 압축률 ($m_{\\min} \\rightarrow 1/3$)")
    ax1.loglog(Ns, resid, "o-", color="#1B5E7A", lw=2.3, ms=6.5, label="원판 정상파 유령 오차 상한 ($O(N^{-3/2})$)")
    ax1.axhline(1.0 / 3.0, color="#B23A2A", ls=":", lw=1.2)
    ax1.annotate("1002각형: 블랙홀 500개!\n최강 압축률 0.333331\n(100만 2각형도 3배 압축!)",
                 xy=(1002, m_min[-1]), xytext=(40, 0.55),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.2),
                 fontsize=8.2, color="#B23A2A", fontweight="bold")
    ax1.annotate("유령 파동 오차 상한\n$\\leq$ 0.0131% (0.000131)",
                 xy=(1002, resid[-1]), xytext=(36, 0.00034),
                 arrowprops=dict(arrowstyle="->", color="#1B5E7A", lw=1.2),
                 fontsize=8.2, color="#1B5E7A", fontweight="bold")
    ax1.set_xlim(4.5, 1600)
    ax1.set_ylim(5e-5, 1.8)
    ax1.set_xlabel("정$N$각형의 변 개수 $N$ ($N = 4m+2$)", fontsize=9.6)
    ax1.set_ylabel("압축 배율 / 스펙트럼 잔차 오차 상한", fontsize=9.4)
    ax1.set_title("A. 1000각형 vs 1002각형: 원의 착시와 500개 블랙홀", fontsize=10.3, fontweight="bold", pad=10)
    ax1.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower left", fontsize=7.6)
    ax1.grid(alpha=0.22, ls=":")

    # Panel B: Octagon discontinuous cliff
    phis_deg = np.linspace(0.00001, 22.0, 500)
    phis = np.deg2rad(phis_deg)
    t1, t2 = pi / 8.0, 2.0 * pi / 8.0
    l1 = -np.abs(np.log(np.tan(t1 + phis) / np.tan(t1 - phis)))
    l2 = -np.abs(np.log(np.tan(t2 + (phis - pi / 8.0)) / np.tan(t2 - (phis - pi / 8.0))))
    ax2.plot(phis_deg, l2, color="#B23A2A", lw=2.5, label="팔각형 중앙 고리 (편각 25%): 불연속 절벽!")
    ax2.plot(phis_deg, l1, color="#1B5E7A", lw=2.0, ls="-.", label="팔각형 나머지 고리 (편각 75%): 0에서 연속 시작")
    ax2.scatter([0.0], [0.0], color="#102A43", s=62, zorder=7, label="정렬된 팔각형 ($0^\\circ$): 모든 광선 중립 ($b^2=\\mathrm{Id},\\ \\Lambda=0$)")
    ax2.scatter([0.0], [-2.0 * log(1.0 + sqrt(2.0))], facecolors="white", edgecolors="#B23A2A", s=62, lw=2.0, zorder=7)
    ax2.annotate("0.00001°만 돌려도\n약 $-1.7627$ 절벽!\n(한 걸음에 약 5.83배 압축)",
                 xy=(0.00001, float(l2[0])), xytext=(5.5, -1.88),
                 arrowprops=dict(arrowstyle="->", color="#B23A2A", lw=1.3),
                 fontsize=8.3, color="#B23A2A", fontweight="bold")
    ax2.set_xlim(-0.8, 22.5)
    ax2.set_ylim(-3.1, 0.25)
    ax2.set_xlabel("정팔각형 회전 각도 $\\phi$ (도)", fontsize=9.6)
    ax2.set_ylabel("리아푸노프 수축 지수 $\\Lambda$", fontsize=9.6)
    ax2.set_title("B. 정팔각형의 0.00001° 불연속 절벽 ($\\lambda = 1/\\sqrt{2}$)", fontsize=10.3, fontweight="bold", pad=10)
    ax2.legend(frameon=True, facecolor="white", framealpha=0.94, edgecolor="#D9E2EC", loc="lower left", fontsize=7.7)
    ax2.grid(alpha=0.22, ls=":")

    out = KR_FIGS / "kr_fig4_1000_vs_1002_and_octagon.png"
    fig.savefig(out, dpi=240)
    plt.close(fig)
    print(f"Wrote {out}")


if __name__ == "__main__":
    make_p1_fig1()
    make_p1_fig2()
    make_p1_fig3()
    make_p2_fig1()
    make_p2_fig2()
    make_p2_fig3()
    make_kr_fig1()
    make_kr_fig2()
    make_kr_fig3()
    make_kr_fig4()
    print("All 10 dedicated publication figures generated successfully.")
