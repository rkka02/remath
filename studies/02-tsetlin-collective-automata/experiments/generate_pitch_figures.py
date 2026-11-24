"""
Generate three publication-grade prototype figures for the Round-R2 Wow-Factor Panel Pitch
using verified high-precision data (70-82 digits) in experiments/data/, 80-digit
subtraction-free GTH solves for Panel B1/B2, and exact analytical formulas.

Outputs:
  - figures/pitch_fig1_architecture_phase.png
  - figures/pitch_fig2_unequal_escape_geometry.png
  - figures/pitch_fig3_mirage_and_fund.png
"""

from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.colors import LogNorm

STUDY = Path(__file__).resolve().parents[1]
DATA = STUDY / "experiments" / "data"
FIGS = STUDY / "figures"
FIGS.mkdir(exist_ok=True)

# AGENTS.md macOS zero-warning matplotlib style
plt.rcParams.update({
    "font.family": "Arial Unicode MS",
    "mathtext.fontset": "dejavusans",
    "font.size": 10,
    "axes.titlesize": 11.5,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8.8,
    "figure.dpi": 220,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# Palette
C_TEAL = "#0F766E"
C_AMBER = "#B45309"
C_INDIGO = "#3730A3"
C_CRIMSON = "#BE123C"
C_SLATE = "#475569"
C_GOLD = "#D97706"
C_PURPLE = "#6D28D9"


def make_fig1_architecture_phase():
    from phase1_chain import solve_game

    fig = plt.figure(figsize=(12.2, 5.2), constrained_layout=True)
    gs = GridSpec(2, 2, width_ratios=[1.35, 1.0], height_ratios=[1.0, 1.0], figure=fig)
    axA = fig.add_subplot(gs[:, 0])
    axB1 = fig.add_subplot(gs[0, 1])
    axB2 = fig.add_subplot(gs[1, 1])

    # Panel A: (kappa_P, R) phase diagram at P = 0.70
    p = 0.70
    q = 1.0 - p
    kap = np.linspace(0.0, 1.0, 400)
    F_L = (p**2 + kap * p * q) / (p**2 + q**2 + 2 * kap * p * q)
    F_D = p + (1.0 - kap) * p * q
    F_K = 2 * p / (1.0 + p**2 + kap * p * q)

    axA.fill_between(kap, 0.70, F_L, color="#E2E8F0", alpha=0.85)
    axA.fill_between(kap, F_L, F_D, color="#99F6E4", alpha=0.65)
    axA.fill_between(kap, F_D, F_K, color="#FDE68A", alpha=0.65)
    axA.fill_between(kap, F_K, 1.0, color="#C7D2FE", alpha=0.65)

    axA.plot(kap, F_L, color=C_TEAL, lw=2.3, label=r"$F_L = F_B = \frac{p^2+\kappa pq}{p^2+q^2+2\kappa pq}$")
    axA.plot(kap, F_D, color=C_AMBER, lw=2.3, ls="--", label=r"$F_D = p+(1-\kappa)pq$")
    axA.plot(kap, F_K, color=C_INDIGO, lw=2.3, ls="-.", label=r"$F_K = \frac{2p}{1+p^2+\kappa pq}$")

    # Direct clean in-band region labels (zero legend clutter!)
    axA.text(0.18, 0.725, "All 4 defect\n(DD phase)", fontsize=8.8, color="#334155", fontweight="bold", ha="center")
    axA.text(0.19, 0.845, "Only $L, B$\ncooperate", fontsize=8.5, color="#0F766E", fontweight="bold", ha="center")
    axA.text(0.84, 0.785, "$L, B, D$ cooperate;\nKrylov $K$ defects", fontsize=8.3, color="#92400E", fontweight="bold", ha="center")
    axA.text(0.28, 0.962, "All 4 architectures cooperate (CC phase)", fontsize=8.8, color="#312E81", fontweight="bold", ha="center")

    # Motivating slice R = 0.80
    axA.axhline(0.80, color="#1E293B", lw=1.2, ls=":")
    kc_L = 13.0 / 63.0
    kc_D = 11.0 / 21.0
    axA.scatter([kc_L, kc_D], [0.80, 0.80], color=[C_TEAL, C_AMBER], s=60, zorder=6, edgecolor="white", lw=1.2)
    axA.annotate(r"$\kappa_c^{L,B} = \frac{13}{63} \approx 0.206$",
                 xy=(kc_L, 0.80), xytext=(0.35, 0.768),
                 arrowprops=dict(arrowstyle="->", color=C_TEAL, lw=1.2),
                 fontsize=8.6, fontweight="bold", color=C_TEAL,
                 bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=C_TEAL, alpha=0.92))
    axA.annotate(r"$\kappa_c^{D} = \frac{11}{21} \approx 0.524$",
                 xy=(kc_D, 0.80), xytext=(0.60, 0.730),
                 arrowprops=dict(arrowstyle="->", color=C_AMBER, lw=1.2),
                 fontsize=8.6, fontweight="bold", color=C_AMBER,
                 bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=C_AMBER, alpha=0.92))
    axA.text(0.02, 0.804, r"$R=0.80$", fontsize=8.2, color="#1E293B", fontweight="bold")

    axA.set_xlim(0.0, 1.0)
    axA.set_ylim(0.70, 1.0)
    axA.set_xlabel(r"Mutual-defection outcome correlation $\kappa_P$ (payoffs frozen)")
    axA.set_ylabel(r"Mutual-cooperation win probability $R$ (at $P = 0.70$)")
    axA.set_title(r"A. Strict Architecture Hierarchy ($F_L = F_B < F_D < F_K$ for $\kappa_P < 1$)")
    axA.legend(loc="upper right", frameon=True, facecolor="white", framealpha=0.94, fontsize=8.2)
    axA.grid(True, alpha=0.25)

    # Panel B1: Volkonskii (1965, p. 47) original example (R=0.85, P=0.65, T=0.90, S=0.60), kappa=0
    ns_v = [2, 4, 8, 12, 16, 24, 32, 40]
    v_game = ("0.85", "0.65", "0.90", "0.60")
    v_L = [float(solve_game(n, n, v_game, "0", "0", kind="L", digits=80)[0]) for n in ns_v]
    v_D = [float(solve_game(n, n, v_game, "0", "0", kind="D", digits=80)[0]) for n in ns_v]
    v_K = [float(solve_game(n, n, v_game, "0", "0", kind="K", digits=80)[0]) for n in ns_v]

    axB1.plot(ns_v, [100 * x for x in v_L], "-o", color=C_TEAL, lw=2.0, ms=4.5, label=r"Tsetlin $L \to 100\%$ CC")
    axB1.plot(ns_v, [100 * x for x in v_D], "--s", color=C_AMBER, lw=2.0, ms=4.5, label=r"Survey-$D \to 0\%$ (Volkonskii)")
    axB1.plot(ns_v, [100 * x for x in v_K], ":^", color=C_INDIGO, lw=1.8, ms=4.2, label=r"Krylov $K \to 0\%$")
    axB1.set_title("B1. Volkonskii (1965, p. 47) Erratum Exposed\n(0.85, 0.65, 0.90, 0.60), independent")
    axB1.set_ylabel("Mutual cooperation (%)")
    axB1.set_ylim(-5, 108)
    axB1.legend(loc="center right", frameon=True, facecolor="white", framealpha=0.9, fontsize=8.0)
    axB1.grid(True, alpha=0.25)

    # Panel B2: Weak-Reward Reversal (R=0.45, P=0.20, T=0.95, S=0.10), kappa=0
    ns_w = [2, 4, 8, 16, 24, 32, 40, 48]
    w_game = ("0.45", "0.20", "0.95", "0.10")
    w_L = [float(solve_game(n, n, w_game, "0", "0", kind="L", digits=80)[0]) for n in ns_w]
    w_B = [float(solve_game(n, n, w_game, "0", "0", kind="B", digits=80)[0]) for n in ns_w]
    w_D = [float(solve_game(n, n, w_game, "0", "0", kind="D", digits=80)[0]) for n in ns_w]
    w_K = [float(solve_game(n, n, w_game, "0", "0", kind="K", digits=80)[0]) for n in ns_w]

    axB2.plot(ns_w, [100 * x for x in w_D], "--s", color=C_AMBER, lw=2.0, ms=4.5, label=r"Survey-$D \to 100\%$ CC")
    axB2.plot(ns_w, [100 * x for x in w_K], "-.^", color=C_INDIGO, lw=2.0, ms=4.5, label=r"Krylov $K \to 100\%$ CC")
    axB2.plot(ns_w, [100 * x for x in w_L], "-o", color=C_TEAL, lw=2.0, ms=4.0, label=r"Tsetlin $L, B \to 0\%$ CC")
    axB2.plot(ns_w, [100 * x for x in w_B], ":", color="#14B8A6", lw=1.6)
    axB2.set_title("B2. Complete Weak-Reward Inversion ($R < 1/2$)\n(0.45, 0.20, 0.95, 0.10), independent")
    axB2.set_xlabel("Memory depth per action, $n$")
    axB2.set_ylabel("Mutual cooperation (%)")
    axB2.set_ylim(-5, 108)
    axB2.legend(loc="center left", frameon=True, facecolor="white", framealpha=0.9, fontsize=8.0)
    axB2.grid(True, alpha=0.25)

    out = FIGS / "pitch_fig1_architecture_phase.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print(f"Saved {out}")


def make_fig2_unequal_escape_geometry():
    aspect = json.loads((DATA / "phase1_aspect.json").read_text())
    geom = json.loads((DATA / "phase2b_escape_geometry.json").read_text())

    fig = plt.figure(figsize=(13.0, 7.6), constrained_layout=True)
    gs = GridSpec(2, 2, width_ratios=[1.15, 1.0], height_ratios=[1.0, 1.0], figure=fig)
    axDome = fig.add_subplot(gs[0, 0])
    axK0 = fig.add_subplot(gs[0, 1])
    axKopt = fig.add_subplot(gs[1, 0])
    axK99 = fig.add_subplot(gs[1, 1])

    # Panel A: Phase Dome (kappa_P, gamma)
    pts = aspect["critical_ratios"]
    ks = np.array([float(p["k"]) for p in pts])
    gL = np.array([float(p["L"]) for p in pts])
    gB = np.array([float(p["B"]) for p in pts])

    axDome.fill_between(ks, 1.0, gL, color="#99F6E4", alpha=0.48, label=r"Both $L$ & $B$ cooperate ($100\%$ CC)")
    axDome.fill_between(ks, gL, gB, color="#FDE68A", alpha=0.85, label="Interface wedge: ONLY $B$ cooperates")
    axDome.plot(ks, gB, color=C_AMBER, lw=2.4, label=r"Randomized boundary $B$")
    axDome.plot(ks, gL, color=C_TEAL, lw=2.2, ls="--", label=r"Deterministic linear $L$")

    # Peak at gamma_max = log(4)/log(1.5)
    gmax = np.log(4.0) / np.log(1.5)
    kpeak = 0.5 * (1.0 + 1.0 / gmax)
    axDome.scatter([kpeak], [gmax], color="#0F172A", s=50, zorder=6)
    axDome.annotate(rf"Tip $\gamma_{{\max}} = h_R/h_P = {gmax:.3f}$" + "\n" + rf"at $\kappa_* = {kpeak:.3f}$",
                    xy=(kpeak, gmax), xytext=(0.15, 3.43),
                    arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.1),
                    fontsize=8.5, fontweight="bold")

    # gamma = 3 horizontal cut showing 0 -> 2/3 -> 1
    axDome.axhline(3.0, color=C_CRIMSON, lw=1.2, ls=":")
    axDome.scatter([0.0, 2.0 / 3.0, 1.0], [3.0, 3.0, 3.0],
                   color=[C_CRIMSON, C_TEAL, C_CRIMSON], s=55, zorder=7, edgecolor="white", lw=1.1)
    axDome.text(0.02, 3.09, r"$L:\ 9.1\times 10^{-11}$", fontsize=8.0, color=C_CRIMSON, fontweight="bold")
    axDome.text(0.66, 2.72, r"$\kappa_*=\frac{2}{3}:\ L=99.85\%$", fontsize=8.2, color=C_TEAL, fontweight="bold", ha="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=C_TEAL, alpha=0.92))
    axDome.text(0.99, 3.16, r"$L:\ 2.2\times 10^{-42}$", fontsize=8.0, color=C_CRIMSON, fontweight="bold", ha="right")

    axDome.set_xlim(-0.30, 1.02)
    axDome.set_ylim(1.0, 3.72)
    axDome.set_xlabel(r"DD outcome correlation $\kappa_P$")
    axDome.set_ylabel(r"Memory depth ratio $\gamma = n_1 / n_2$")
    axDome.set_title("A. Imperfect-Sync Cooperation Dome & $B$-vs-$L$ Wedge\n" + r"PD $(0.8,0.6,0.9,0.2)$; annotated $L$ masses at $(240,80),\ \kappa_R=0$")
    axDome.legend(loc="lower left", frameon=True, facecolor="white", framealpha=0.92, fontsize=7.8)
    axDome.grid(True, alpha=0.25)

    # Helper to plot 2D ever-hit density on the DD + near-interface region (d1 in 0..65, d2 in 0..25)
    case_map = {(c["kind"], c["kappa_P"]): c for c in geom["cases"]}

    def plot_heatmap(ax, kind, kap_str, title, subtitle, note_xy=None, note_xytext=None, note_txt=None):
        c = case_map[(kind, kap_str)]
        arr = np.array([[float(val) for val in row[:26]] for row in c["ever_hit_given_success"][:66]])
        grid = np.clip(arr.T, 1e-4, 1.0)
        im = ax.imshow(
            grid, origin="lower", aspect="auto",
            norm=LogNorm(vmin=1e-3, vmax=1.0), cmap="magma",
            extent=[-0.5, 65.5, -0.5, 25.5]
        )
        ax.axvline(59.5, color="#38BDF8", lw=1.5, ls="--")
        ax.axhline(19.5, color="#38BDF8", lw=1.5, ls="--")
        ax.scatter([0, 60], [0, 20], color=["#22C55E", "#FACC15"], s=55, zorder=8, edgecolor="black", lw=0.9)
        ax.text(2.2, 2.2, "Deep DD", color="#86EFAC", fontsize=7.6, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.18", fc="#0F172A", ec="#22C55E", alpha=0.82))
        ax.text(58.2, 22.4, "Corner CC\n(60,20)", color="#FEF08A", fontsize=7.6, fontweight="bold", ha="right")
        if note_xy is not None and note_txt is not None:
            ax.annotate(note_txt, xy=note_xy, xytext=note_xytext,
                        arrowprops=dict(arrowstyle="->", color="white", lw=1.2),
                        color="white", fontsize=8.0, fontweight="bold",
                        bbox=dict(boxstyle="round,pad=0.25", fc="#0F172A", ec="white", alpha=0.88))
        ax.set_xlabel(r"Long-memory progress $d_1$ (switch at $60$)")
        ax.set_ylabel(r"Short-memory progress $d_2$ (switch at $20$)")
        ax.set_title(f"{title}\n{subtitle}", fontsize=10.5)
        cb = fig.colorbar(im, ax=ax, fraction=0.042, pad=0.02)
        cb.set_label("Ever-hit prob. given escape", fontsize=8.2)

    plot_heatmap(
        axK0, "L", "0",
        r"B. Independent Shocks ($\kappa_P = 0$, Tsetlin $L$)",
        r"Axis-hugging 2-leg route · escape prob. $= 6.94\times 10^{-16}$",
        note_xy=(28, 2.0), note_xytext=(5, 13.5),
        note_txt="Long player crawls\nalong $d_2 \\approx 0$ first"
    )
    plot_heatmap(
        axKopt, "L", "2/3",
        r"C. Optimal Imperfect Sync ($\kappa_P = 2/3$, Tsetlin $L$)",
        r"Diagonal instanton beam · escape prob. $= 1.39\times 10^{-13}$ (200× higher)",
        note_xy=(30, 10.0), note_xytext=(27, 2.5),
        note_txt="Direct 3:1 diagonal\n(92.0% enter CC at (60,20))"
    )
    plot_heatmap(
        axK99, "B", "99/100",
        r"D. High Sync ($\kappa_P = 0.99$, Randomized $B$)",
        r"Interface recrossing · $B$ escape prob. $= 8{,}994\times L$",
        note_xy=(40, 19.0), note_xytext=(19, 9.0),
        note_txt="87.5% of $B$ escapes visit\nsite (40,19) (vs 0.63% for $L$)"
    )

    out = FIGS / "pitch_fig2_unequal_escape_geometry.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print(f"Saved {out}")


def make_fig3_mirage_and_fund():
    sg = json.loads((DATA / "phase2b_staghunt_grid.json").read_text())
    qm = json.loads((DATA / "phase2b_quorum_memory.json").read_text())

    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(14.0, 4.4), constrained_layout=True)

    # Panel A: Stag-Hunt mirage robustness across BOTH sides of S = 1/2
    selected = [
        ("0.45", "0.94", r"$S=0.45,\ R=0.94$ (sampled max $73.8\%$)", C_SLATE, "--"),
        ("0.48", "0.94", r"$S=0.48,\ R=0.94$ (sampled max $84.1\%$)", C_TEAL, "-"),
        ("0.5", "0.9405", r"$S=0.50,\ R=0.9405$ (sampled max $96.1\%$)", C_CRIMSON, "-"),
        ("0.55", "0.929", r"$S=0.55,\ R=0.929$ (sampled max $80.5\%$)", C_PURPLE, "-."),
    ]
    curve_map = {(c["S"], c["R"]): c for c in sg["robustness_curves"]}
    for s_str, r_str, lbl, col, ls in selected:
        c = curve_map[(s_str, r_str)]
        ns = [p["n"] for p in c["points"]]
        ccs = [100.0 * float(p["CC"]) for p in c["points"]]
        axA.plot(ns, ccs, ls=ls, color=col, lw=2.1, marker="o", ms=3.2, label=lbl)

    axA.set_xscale("log")
    axA.set_xlim(1, 220)
    axA.set_ylim(-3, 105)
    axA.set_xlabel("Memory depth per action, $n$ (log scale)")
    axA.set_ylabel("Mutual stag hunting (%)")
    axA.set_title("A. Stag-Hunt Mirage on Both Sides of $S=1/2$\n(All curves vanish: $\\lim_{n\\to\\infty}\\pi_n(CC)=0$)")
    axA.legend(loc="lower left", frameon=True, facecolor="white", framealpha=0.92, fontsize=7.8)
    axA.grid(True, alpha=0.25)

    # Panel B: Universal x*exp(-x) master collapse at S = 1/2
    xs_ref = np.linspace(0.0, 4.2, 300)
    axB.plot(xs_ref, xs_ref * np.exp(-xs_ref), color="#0F172A", lw=2.4, label=r"Universal limit $x e^{-x}$")
    cols_m = ["#94A3B8", "#3B82F6", "#0D9488", "#D97706", "#BE123C"]
    markers_m = ["o", "s", "^", "D", "*"]
    for idx, c in enumerate(sg["fair_master_collapse"]["stationary_curves"]):
        xs = [float(p["x"]) for p in c["points"]]
        ys = [float(p["scaled_observed_odds"]) for p in c["points"]]
        axB.scatter(xs, ys, color=cols_m[idx % len(cols_m)], marker=markers_m[idx % len(markers_m)],
                    s=36 if idx < 4 else 65, zorder=5 + idx, label=f"$R={c['R']}$")
    axB.axvline(1.0, color=C_CRIMSON, lw=1.1, ls=":")
    axB.annotate(r"Peak at $x = \delta n_* \to 1$" + "\n" + r"height $= 1/e \approx 0.3679$",
                 xy=(1.0, np.exp(-1)), xytext=(1.08, 0.11),
                 arrowprops=dict(arrowstyle="->", color=C_CRIMSON, lw=1.2),
                 fontsize=8.3, color=C_CRIMSON, fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=C_CRIMSON, alpha=0.92))
    axB.set_xlim(0.0, 4.0)
    axB.set_ylim(0.0, 0.42)
    axB.set_xlabel(r"Rescaled memory depth $x = \delta n$")
    axB.set_ylabel(r"Rescaled stationary odds $\delta U_n / K_*$")
    axB.set_title(r"B. Fair-Solo Master Collapse ($S=1/2,\ R \uparrow R_c=16/17$)")
    axB.legend(loc="upper right", frameon=True, facecolor="white", framealpha=0.92, fontsize=7.8)
    axB.grid(True, alpha=0.25)

    # Panel C: Quorum Partial Common Fund (n_c = 2 exact cutoff)
    crossings = [row for row in qm["quota_crossings"] if row["depth"] <= 12]
    ds = np.array([row["depth"] for row in crossings])
    An = np.array([float(row["high"]["share"]) for row in crossings])
    Bn = np.array([float(row["low"]["share"]) for row in crossings])
    nash = 43.0 / 60.0

    # Shaded regions
    axC.axhspan(0.0, nash, color="#DCFCE7", alpha=0.45, label=r"Below-Nash zone ($\alpha < 43/60$, D dominant)")
    axC.axhline(nash, color=C_CRIMSON, lw=2.0, ls="--", label=r"Pivotal Nash threshold $\alpha_{\mathrm{Nash}} = 43/60$")
    axC.plot(ds, An, "-o", color=C_TEAL, lw=2.2, ms=5.5, label=r"Quota-balance share $A_n$ (opt. proved $n\leq 3$)")
    axC.plot(ds, Bn, ":s", color=C_SLATE, lw=1.6, ms=4.0, label=r"Low-branch crossing $B_n$")
    # Asymptotic envelope 1 - (123/500)*log(3)/n
    d_fine = np.linspace(1.5, 12.2, 200)
    asymp = 1.0 - (123.0 / 500.0) * np.log(3.0) / d_fine
    axC.plot(d_fine, asymp, color=C_AMBER, lw=1.5, ls="-.", label=r"$1 - \frac{123\log 3}{500\,n}$ asymptotic")

    # Highlight n=1 Goldilocks point and n=2 cutoff + period-3 point
    axC.scatter([1], [0.60], color=C_TEAL, s=85, zorder=7, edgecolor="black", lw=1.0)
    axC.annotate("ONLY below-Nash efficient\noptimum: $n=1,\\ A_1 = 3/5$\n(W=0.82 vs 0.68 / 0.67)",
                 xy=(1.0, 0.60), xytext=(2.5, 0.44),
                 arrowprops=dict(arrowstyle="->", color=C_TEAL, lw=1.2),
                 fontsize=7.6, fontweight="bold", color=C_TEAL,
                 bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=C_TEAL, alpha=0.94))
    axC.scatter([2], [0.70], color=C_PURPLE, marker="D", s=55, zorder=7, edgecolor="white")
    axC.annotate("Period-3 cycle\n($n=2,\\ \\alpha=0.70$)",
                 xy=(2.0, 0.70), xytext=(6.2, 0.60),
                 arrowprops=dict(arrowstyle="->", color=C_PURPLE, lw=1.1),
                 fontsize=7.7, fontweight="bold", color=C_PURPLE)
    axC.annotate(r"$n_c=2$: $A_2 = \frac{11-4\sqrt{3}}{5} \approx 0.814$",
                 xy=(2.0, An[1]), xytext=(4.8, 0.77),
                 arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.0),
                 fontsize=7.8, fontweight="bold")

    axC.set_xlim(0.6, 12.4)
    axC.set_ylim(0.18, 1.03)
    axC.set_xticks(range(1, 13))
    axC.set_xlabel("Individual memory depth per action, $n$")
    axC.set_ylabel(r"Common-fund sharing fraction $\alpha$")
    axC.set_title(r"C. Quorum Fund Cutoff at $n_c = 2$" + "\n(1/4-quorum public good, $N \\to \\infty$)")
    axC.legend(loc="lower right", frameon=True, facecolor="white", framealpha=0.94, fontsize=6.9)
    axC.grid(True, alpha=0.25)

    out = FIGS / "pitch_fig3_mirage_and_fund.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print(f"Saved {out}")


if __name__ == "__main__":
    make_fig1_architecture_phase()
    make_fig2_unequal_escape_geometry()
    make_fig3_mirage_and_fund()
