"""Generate dedicated, non-overlapping publication figures for:
  1. Paper 1 (Complex Analysis / Balayage / Fokas Bridge): papers/paper1_invisible_loads/figs/
  2. Paper 2 (Minimax Corner Recovery / Super-Resolution): papers/paper2_corner_recovery/figs/
  3. Korean Expository Magazine (Korean labels via Apple SD Gothic Neo): papers/expository_kr/figs/
"""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.ticker as mticker
import mpmath as mp
import numpy as np
import scipy.linalg as la
from scipy import special

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "experiments"
P1_FIGS = ROOT / "papers" / "paper1_invisible_loads" / "figs"
P2_FIGS = ROOT / "papers" / "paper2_corner_recovery" / "figs"
KR_FIGS = ROOT / "papers" / "expository_kr" / "figs"
for d in (P1_FIGS, P2_FIGS, KR_FIGS):
    d.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(EXP))
from phase2_theorems import GammaSymbol, edges as poly_edges, unit_moment
from phase3_anatomy_and_rhombus import skeleton_coefficients

NAVY = "#0f172a"
BLUE = "#2563eb"
TEAL = "#0d9488"
CORAL = "#e11d48"
AMBER = "#d97706"
PURPLE = "#7c3aed"
SLATE = "#64748b"


def set_en_style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "axes.unicode_minus": True,
        "font.size": 9.5,
        "axes.titlesize": 10.8,
        "axes.titleweight": "bold",
        "axes.labelsize": 9.5,
        "axes.edgecolor": "#334155",
        "axes.linewidth": 0.85,
        "grid.color": "#cbd5e1",
        "grid.linestyle": "--",
        "grid.alpha": 0.55,
        "legend.framealpha": 0.93,
        "legend.edgecolor": "#cbd5e1",
        "figure.facecolor": "white",
        "axes.facecolor": "#fafbfc",
    })


def set_kr_style():
    set_en_style()
    plt.rcParams.update({
        "font.family": "Arial Unicode MS",
        "mathtext.fontset": "dejavusans",
        "axes.unicode_minus": True,
    })


def square_ghost_single(z, n_terms=14):
    out = np.zeros_like(z, dtype=np.complex128)
    for m in range(1, n_terms + 1):
        coeff = ((-1) ** m) * (2 * np.pi * m) ** 2 / (2.0 * np.sinh(np.pi * m))
        out += coeff * np.exp(2 * np.pi * m * z)
    return out


def continued_ghost_line(w_arr, n_terms=24):
    out = np.zeros_like(w_arr, dtype=np.complex128)
    for k in range(n_terms):
        q = -np.exp(2 * np.pi * (w_arr - k - 0.5))
        out += (2 * np.pi) ** 2 * q * (1.0 + q) / ((1.0 - q) ** 3)
    return out


def compute_fokas_svd_and_field():
    """Return SVD pairs (square & triangle) + 2D pointwise log10 error on unit square."""
    def svd_pair(verts):
        p = len(verts)
        dirs = poly_edges(verts)
        k = p // 2
        n_freq = 5
        sym = GammaSymbol(verts)
        nodes = [2 * mp.pi * mp.j * m / dirs[j] for j in range(p) for m in range(1, n_freq + 1)]
        rows_raw = []
        for s in nodes:
            anchor = max(verts, key=lambda w: mp.re(s * w))
            row_c = []
            for j, d in enumerate(dirs):
                v0 = verts[j]
                p0 = mp.exp(s * (v0 - anchor))
                p1 = mp.exp(s * (verts[(j + 1) % p] - anchor))
                m0 = abs(d) * unit_moment(0, s * d, p0, p1)
                m1 = abs(d) * unit_moment(1, s * d, p0, p1)
                row_c.extend([m0, 2 * m1 - m0])
            row_c.append(sym(s) * mp.exp(-s * anchor))
            rows_raw.append([float(z.real) for z in row_c])
            rows_raw.append([float(z.imag) for z in row_c])
        M_before = np.array(rows_raw, dtype=float)
        rows_mom = []
        r0 = []
        for j, d in enumerate(dirs):
            r0.extend([float(abs(d)), 0.0])
        r0.append(1.0)
        rows_mom.append(r0)
        for deg in range(1, k):
            rc = []
            for j, d in enumerate(dirs):
                v0 = complex(verts[j])
                dc = complex(d)
                q, wt = special.roots_legendre(12)
                tt, ww = (q + 1) / 2, wt / 2
                vals = (v0 + dc * tt) ** deg
                rc.append(abs(dc) * np.sum(ww * vals))
                rc.append(abs(dc) * np.sum(ww * (2 * tt - 1) * vals))
            rc.append(complex(mp.diff(sym, 0, deg)))
            rows_mom.append([z.real for z in rc])
            rows_mom.append([z.imag for z in rc])
        M_after = np.vstack([M_before, np.array(rows_mom, dtype=float)])
        return np.maximum(la.svdvals(M_before), 1e-17), la.svdvals(M_after), M_after

    with mp.workdps(40):
        sq_v = (mp.mpc(0), mp.mpc(1), mp.mpc(1, 1), mp.mpc(0, 1))
        tr_v = (mp.mpc(0), mp.mpc(1), mp.mpc("0.5", mp.sqrt(3) / 2))
        sv_sq_b, sv_sq_a, M_sq = svd_pair(sq_v)
        sv_tr_b, sv_tr_a, _ = svd_pair(tr_v)
    return sv_sq_b, sv_sq_a, sv_tr_b, sv_tr_a


# ==============================================================================
# PAPER 1 FIGURES (Complex Analysis / Balayage / Fokas Bridge)
# ==============================================================================
def build_paper1_figures():
    set_en_style()
    data = json.loads((EXP / "phase3_data.json").read_text())
    tri_npz = np.load(EXP / "data" / "phase3_triangle.npz")
    x_tri = tri_npz["x"]
    g_L2 = tri_npz["g_L2"]
    g_s0 = tri_npz["g_s"][0]
    proj_768 = tri_npz["projection"][-1]

    # --- P1 Fig 1: Fokas-Leont'ev Bridge, Ghost Wave, and Sharp Erasure ---
    fig, axes = plt.subplots(1, 3, figsize=(15.6, 4.7), dpi=300)

    # 1A: Ray quadrature convergence + Polygon rays
    ax = axes[0]
    panels = np.array([4, 8, 16, 32, 64])
    quad_err = np.array([1.035e-6, 1.135e-7, 1.441e-8, 1.800e-9, 2.242e-10])
    ax.loglog(panels, quad_err, "o-", color=BLUE, lw=2.2, ms=6,
              label=r"4-ray Gauss quadrature $|c_\nu^{\rm quad}-c_\nu^{\rm exact}|$")
    ax.loglog(panels, 7e-5 * panels ** (-3.0), ":", color=SLATE, lw=1.4, label=r"$O(P^{-3})$ reference")
    # Inset showing convex polygon + outward spectral rays
    ins = ax.inset_axes([0.08, 0.10, 0.42, 0.42])
    tri = np.array([0, 1, 0.5 + 1j * np.sqrt(3) / 2]) - (0.5 + 1j * np.sqrt(3) / 6)
    ins.add_patch(patches.Polygon(np.c_[tri.real, tri.imag], closed=True,
                                  facecolor=TEAL, alpha=0.18, edgecolor=TEAL, lw=1.8))
    for j in range(3):
        d = tri[(j + 1) % 3] - tri[j]
        u = (1j / d) / abs(1j / d)
        for m in range(1, 4):
            pt = u * (0.28 + 0.20 * m)
            ins.scatter([pt.real], [pt.imag], color=CORAL, s=14, zorder=5)
        ins.annotate("", xy=(u.real * 1.05, u.imag * 1.05), xytext=(0, 0),
                     arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.1, ls="--"))
    ins.set_xlim(-1.15, 1.15)
    ins.set_ylim(-1.15, 1.15)
    ins.set_aspect("equal")
    ins.axis("off")
    ins.set_title(r"Rays $\mathcal{R}_j$ & $\Lambda_+$", fontsize=7.8)

    ax.set_xticks(panels)
    ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())
    ax.set_title("A. Continuous-to-Discrete Ray Transfer")
    ax.set_xlabel("Composite Gauss panels per ray ($P$)")
    ax.set_ylabel(r"Coefficient transfer error $|c_\nu^{\rm quad} - c_\nu|$")
    ax.legend(loc="upper right", fontsize=7.8)
    ax.grid(True, which="both", alpha=0.45)

    # 1B: Square Ghost Wave + Exterior Lambert Continuation Slice
    ax = axes[1]
    xs_line = np.linspace(-0.48, 0.92, 300)
    z_line = xs_line + 0.17j
    w0 = continued_ghost_line(z_line)
    w1 = 1j * continued_ghost_line(1j * z_line)
    w2 = -continued_ghost_line(-z_line)
    w3 = -1j * continued_ghost_line(-1j * z_line)
    w_sum = w0 + w1 + w2 + w3

    ax.plot(xs_line, np.real(w0), "-", color=CORAL, lw=2.0, label=r"$\mathrm{Re}\,G(z)$ (east wave, continued)")
    ax.plot(xs_line, np.real(w1), "--", color=BLUE, lw=1.7, label=r"$\mathrm{Re}\,[iG(iz)]$")
    ax.plot(xs_line, np.real(w2 + w3), "-.", color=TEAL, lw=1.7, label=r"$\mathrm{Re}\,[-G(-z)-iG(-iz)]$")
    ax.plot(xs_line, np.abs(w_sum), "-", color=NAVY, lw=2.5, label=r"$|\sum_{\ell=0}^3 i^\ell G(i^\ell z)|$ ($\approx 0$ everywhere!)")
    ax.axvline(0.5, color=AMBER, ls=":", lw=1.8)
    ax.axvspan(-0.5, 0.5, color="#eff6ff", alpha=0.55, label=r"Square interior $|x|\leq 0.5$")
    ax.annotate("Square boundary $x=0.5$\n(raw series diverges for $x>0.5$,\nyet Lambert continuation cancels\nto $4.9\\times 10^{-65}$ at $x=0.71$!)",
                xy=(0.5, 1.8), xytext=(-0.45, 2.5), fontsize=7.6, color=NAVY,
                bbox=dict(boxstyle="round,pad=0.28", facecolor="white", edgecolor=AMBER, alpha=0.94),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2))
    ax.set_xlim(-0.48, 0.92)
    ax.set_ylim(-5.5, 5.2)
    ax.set_title(r"B. Ghost Wave Cancellation Along $z = x + 0.17i$")
    ax.set_xlabel(r"$x = \mathrm{Re}(z)$ (crosses right edge at $x = 0.5$)")
    ax.set_ylabel("Wave amplitude")
    ax.legend(loc="lower left", fontsize=7.2, ncol=1)
    ax.grid(True)

    # 1C: Exponential Reconstruction & Sharp Zero-Density Erasure
    ax = axes[2]
    N_sq = np.array([4, 8, 16, 32, 56])
    err_ghost = np.array([2.673e-2, 2.478e-5, 5.062e-12, 7.545e-26, 5.515e-47])
    err_wave = np.array([6.538e-4, 3.894e-7, 4.890e-14, 3.661e-28, 1.545e-49])
    err_erased = np.array([2.527e-3, 1.726e-6, 2.451e-13, 8.755e-28, 4.454e-50])
    N_tri = np.array([8, 16, 32, 64, 80])
    err_tri = np.array([1.744e-3, 1.899e-6, 1.659e-12, 9.146e-25, 6.400e-31])

    ax.semilogy(N_sq, err_ghost, "o-", color=CORAL, lw=2.0, ms=5.5, label="Square ghost residual")
    ax.semilogy(N_sq, err_wave, "s-", color=BLUE, lw=2.0, ms=5.5, label=r"Square $e^{az}$ synthesis")
    ax.semilogy(N_sq, err_erased, "^--", color=AMBER, lw=2.2, ms=6, label=r"Square ($m=k^2$ erased: $o(R)$)")
    ax.semilogy(N_tri, err_tri, "D-", color=TEAL, lw=2.0, ms=5, label=r"Triangle $e^{az}$ synthesis")
    ax.set_ylim(1e-53, 1e0)
    ax.set_title("C. Synthesis Convergence & $o(R)$ Erasure")
    ax.set_xlabel("Modes per ray ($N$)")
    ax.set_ylabel("65-digit reconstruction error")
    ax.legend(loc="upper right", fontsize=7.6)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout()
    fig.savefig(P1_FIGS / "p1_fig1_bridge_and_ghosts.png", dpi=300)
    plt.close(fig)

    # --- P1 Fig 2: Square Torsion vs. Triangle Y-Skeleton Balayage & Edge Profiles ---
    fig, axes = plt.subplots(1, 3, figsize=(15.8, 4.9), dpi=300)

    # 2A: Square Uniform Charge Torsion
    ax = axes[0]
    gx = np.linspace(0, 1, 120)
    XX, YY = np.meshgrid(gx, gx)
    u_sq = np.zeros_like(XX)
    for n in range(1, 30, 2):
        k = n * np.pi
        u_sq += (4.0 / k**3) * np.sin(k * XX) * (1.0 - np.cosh(k * (YY - 0.5)) / np.cosh(k / 2.0))
    t_edge = np.linspace(0, 1, 250)
    sq_tor = np.zeros_like(t_edge)
    for n in range(1, 120, 2):
        k = n * np.pi
        sq_tor += (4.0 / k**2) * np.sin(k * t_edge) * np.tanh(k / 2.0)

    ax.contourf(XX, YY, u_sq, levels=20, cmap="YlOrRd")
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.0))
    sc = 0.40
    for (x_p, y_p, x_b, y_b, horiz) in [
        (t_edge, -sc * sq_tor, t_edge, 0, True),
        (t_edge, 1 + sc * sq_tor, t_edge, 1, True),
        (-sc * sq_tor, t_edge, 0, t_edge, False),
        (1 + sc * sq_tor, t_edge, 1, t_edge, False),
    ]:
        ax.plot(x_p, y_p, color=BLUE, lw=2.0)
        if horiz:
            ax.fill_between(x_p, y_b, y_p, color=BLUE, alpha=0.20)
        else:
            ax.fill_betweenx(y_p, x_b, x_p, color=BLUE, alpha=0.20)
    for (vx, vy), sgn, col in [((0, 0), "+1", CORAL), ((1, 0), "−1", PURPLE),
                                ((1, 1), "+1", CORAL), ((0, 1), "−1", PURPLE)]:
        ax.scatter([vx], [vy], color=col, edgecolor="white", s=85, zorder=6)
        ax.text(vx + (-0.11 if vx == 0 else 0.11), vy + (-0.11 if vy == 0 else 0.11),
                sgn, ha="center", va="center", fontsize=8.8, fontweight="bold", color=col)
    ax.text(0.5, 0.5, "Uniform 2D Source\n$(-\\Delta u = 1)$\nBalayage $= -\\partial_n u$\n$\\in \\mathcal{K}_{L^2}(\\Lambda_+)$",
            ha="center", va="center", fontsize=8.2, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.88, edgecolor=NAVY))
    ax.set_xlim(-0.30, 1.30)
    ax.set_ylim(-0.30, 1.30)
    ax.set_aspect("equal")
    ax.set_title("A. Zonotope Square: Torsion Balayage")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    # 2B: Equilateral Triangle Y-Shaped Zeta Skeleton
    ax = axes[1]
    H0 = np.sqrt(3) / 2
    v_tri = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, H0]])
    ctr = v_tri.mean(axis=0)
    ax.add_patch(patches.Polygon(v_tri, closed=True, facecolor="#ecfeff", edgecolor=NAVY, lw=2.0))
    mp.mp.dps = 30
    coeff = skeleton_coefficients(90)
    R = 1.0 / np.sqrt(3)
    rs = np.linspace(1e-4, R, 110)
    hs = np.array([float(mp.sqrt(r) * mp.polyval(coeff[::-1], mp.mpf(r) ** 3)) for r in rs])
    cmap = plt.get_cmap("plasma")
    norm = plt.Normalize(0, hs.max())
    for k in range(3):
        u_vec = (ctr - v_tri[k]) / R
        pts = v_tri[k][None, :] + rs[:, None] * u_vec[None, :]
        for i in range(len(rs) - 1):
            ax.plot(pts[i:i+2, 0], pts[i:i+2, 1], color=cmap(norm(hs[i])), lw=5.0, solid_capstyle="round", zorder=4)
    ax.scatter([ctr[0]], [ctr[1]], color="#facc15", edgecolor=NAVY, s=80, zorder=6)
    for j in range(3):
        p0, p1 = v_tri[j], v_tri[(j + 1) % 3]
        e = p1 - p0
        n_out = np.array([e[1], -e[0]]) / np.linalg.norm(e)
        base_pts = p0[None, :] + x_tri[:, None] * e[None, :]
        outer_pts = base_pts + (0.40 * g_L2)[:, None] * n_out[None, :]
        ax.plot(outer_pts[:, 0], outer_pts[:, 1], color=TEAL, lw=2.0)
        ax.add_patch(patches.Polygon(np.vstack([base_pts, outer_pts[::-1]]),
                                     closed=True, facecolor=TEAL, alpha=0.20, edgecolor="none"))
    ax.annotate("1D Median Skeleton\n" + r"$h(r)=\sqrt{r}\sum a_j r^{3j}>0$" + "\n" + r"($\zeta(6m+4)$ Binet kernel)",
                xy=(ctr[0] + 0.03, ctr[1] + 0.03), xytext=(0.50, 1.06), ha="center",
                fontsize=7.9, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.26", facecolor="white", edgecolor=PURPLE, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.3, connectionstyle="arc3,rad=-0.2"))
    ax.scatter(v_tri[:, 0], v_tri[:, 1], color=NAVY, s=45, zorder=6)
    ax.set_xlim(-0.30, 1.30)
    ax.set_ylim(-0.28, 1.36)
    ax.set_aspect("equal")
    ax.set_title(r"B. Triangle: Y-Skeleton Balayage $g_\triangle$")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    # 2C: Edge-profile comparison + L1\L2 blowup
    ax = axes[2]
    tri_tor = 2.0 * x_tri * (1.0 - x_tri)
    ax.plot(x_tri, g_L2, color=TEAL, lw=2.6, label=r"Triangle $g_\triangle(x) \sim \sqrt{2/\pi}\,x^{1/2}$")
    ax.plot(x_tri[::20], proj_768[::20], "o", color=NAVY, ms=3.8, label="768-mode least-norm check")
    ax.plot(x_tri, tri_tor, "--", color=AMBER, lw=2.0, label=r"Normalized triangle torsion $2x(1-x)$")
    ax.plot(t_edge, sq_tor, ":", color=BLUE, lw=2.1, label=r"Square torsion $-\partial_n u$ ($\in \mathcal{K}_{L^2}$)")
    ax.plot(x_tri, np.clip(g_s0, -1.2, 1.2), "-.", color=CORAL, lw=1.5,
            label=r"$L^1\setminus L^2$ sibling ($\sim \pm x^{-1/2}$)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.08, 1.08)
    ax.set_title(r"C. Edge Profiles & $L^1 \setminus L^2$ Corner Gap")
    ax.set_xlabel(r"Arclength $x \in [0, 1]$")
    ax.set_ylabel("Mass-normalized boundary density")
    ax.legend(loc="lower center", fontsize=7.3)
    ax.grid(True)

    plt.tight_layout()
    fig.savefig(P1_FIGS / "p1_fig2_balayage_anatomy.png", dpi=300)
    plt.close(fig)

    # --- P1 Fig 3: Two-Sided Symmetry Collapse & Fokas Global Relation Completion ---
    sv_sq_b, sv_sq_a, sv_tr_b, sv_tr_a = compute_fokas_svd_and_field()
    fig, axes = plt.subplots(1, 2, figsize=(12.2, 4.7), dpi=300)

    # 3A: Symmetry-Breaking Collapse
    ax = axes[0]
    eps = np.array(data["tilt"]["epsilon"])
    sig = np.array(data["tilt"]["singular_values"])
    m = eps > 0
    for k, (col, ls, lbl) in enumerate([
        (NAVY, "-", r"$\sigma_1$ (slope $169.53$)"),
        (BLUE, "-", r"$\sigma_2$ (slope $6.93$)"),
        (TEAL, "--", r"$\sigma_3$ (slope $6.93$)"),
        (CORAL, "-", r"$\sigma_4$ (slope $0.549$)"),
    ]):
        ax.loglog(eps[m], sig[m, k], ls, color=col, lw=2.1, label=lbl)
    ax.loglog([1e-7, 1e-2], [2.5e-8, 2.5e-3], ":", color=SLATE, lw=1.3, label=r"$O(\varepsilon)$ linear lift")
    ax.annotate("At $\\varepsilon=0$: $\\dim \\mathcal{K}_{\\mathcal{M}}(\\Lambda_\\pm)=4$\n"
                "Any tilt $\\varepsilon>0$: $\\dim \\mathcal{K}_{\\mathcal{M}}(\\Lambda_\\pm)=0$!",
                xy=(1e-6, sig[m, 3][3]), xytext=(3e-6, 1.5e-1), fontsize=8.0, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.set_title(r"A. Two-Sided Lattice $\Lambda_\pm$ Symmetry Collapse")
    ax.set_xlabel(r"Vertex tilt perturbation $\varepsilon$ (radians)")
    ax.set_ylabel("Singular values on 4-mode invisible basis")
    ax.legend(loc="lower right", fontsize=7.8)
    ax.grid(True, which="both", alpha=0.45)

    # 3B: Fokas SVD Before vs After Minimal 2k-1 Moment Completion
    ax = axes[1]
    ax.semilogy(np.arange(1, len(sv_sq_b) + 1), sv_sq_b, "o--", color=CORAL, lw=2.0, ms=6,
                label="Square BEFORE completion (nullity 3)")
    ax.semilogy(np.arange(1, len(sv_sq_a) + 1), sv_sq_a, "o-", color=BLUE, lw=2.2, ms=6,
                label=r"Square AFTER $2k\!-\!1=3$ moments ($\kappa=16.45$)")
    ax.semilogy(np.arange(1, len(sv_tr_b) + 1), sv_tr_b, "s--", color=AMBER, lw=2.0, ms=5.5,
                label="Triangle BEFORE completion (nullity 1)")
    ax.semilogy(np.arange(1, len(sv_tr_a) + 1), sv_tr_a, "s-", color=TEAL, lw=2.2, ms=5.5,
                label=r"Triangle AFTER $2k\!-\!1=1$ moment ($\kappa=12.21$)")
    ax.annotate("Interior Laplace error after completion:\nSquare: $3.9\\times 10^{-16}$\nTriangle: $2.4\\times 10^{-15}$",
                xy=(9, sv_sq_a[-1]), xytext=(4.2, 1e-6), fontsize=8.0, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=BLUE, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.set_xticks(range(1, 10))
    ax.set_ylim(1e-18, 1e2)
    ax.set_title("B. Fokas Global Relation Nullspace Completion")
    ax.set_xlabel("Singular value index")
    ax.set_ylabel("Singular value magnitude")
    ax.legend(loc="lower left", fontsize=7.5)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout()
    fig.savefig(P1_FIGS / "p1_fig3_symmetry_and_fokas_completion.png", dpi=300)
    plt.close(fig)
    print("Built all Paper 1 dedicated figures!")


# ==============================================================================
# PAPER 2 FIGURES (Minimax Corner Recovery / Super-Resolution)
# ==============================================================================
def build_paper2_figures():
    set_en_style()
    data = json.loads((EXP / "phase3_data.json").read_text())

    # --- P2 Fig 1: Parity Unmasking, Odd-Polygon Sharp Constant, and Single-Shift Regimes ---
    fig, axes = plt.subplots(1, 3, figsize=(15.8, 4.8), dpi=300)

    # 1A: Scalene triangle vertex recovery vs Square alternating half-step unmasking
    ax = axes[0]
    N_rec = np.array([16, 64, 256, 1024])
    err_tri_ces = np.array([0.04966662, 0.01743722, 0.00563037, 0.00172637])
    worst_l2 = np.array([0.348017, 0.348224, 0.348277, 0.348290]) / np.sqrt(N_rec)
    ax.loglog(N_rec, worst_l2, "o-", color=CORAL, lw=2.2, ms=6,
              label=r"Worst-case unit-$L^2$ layer ($0.3483\,N^{-1/2}$)")
    ax.loglog(N_rec, err_tri_ces, "s-", color=TEAL, lw=2.1, ms=5.5,
              label="Scalene triangle $(2,-1,3)$ + unit flux")
    # Single shifted sample middle-band projected norm from Phase 2
    N_mid = np.array([16, 64, 256])
    mid_norm = np.array([0.21307, 0.110855, 0.0560524])
    last_floor = np.array([0.212207, 0.212207, 0.212207])
    ax.loglog(N_mid, mid_norm, "^--", color=BLUE, lw=2.0, ms=6,
              label=r"Square mid-shift proj. norm ($O(N^{-1/2})$)")
    ax.loglog(N_mid, last_floor, "v:", color=AMBER, lw=2.0, ms=6,
              label=r"Square end-shift witness ($\Theta(1)$ floor!)")
    ax.set_title("A. Corner Recovery & Single-Shift Regimes")
    ax.set_xlabel("Band cutoff $N$")
    ax.set_ylabel("Error / risk scale")
    ax.legend(loc="lower left", fontsize=7.3)
    ax.grid(True, which="both", alpha=0.45)

    # 1B: Odd-polygon sharp minimax constant vs calibrated Cesaro
    ax = axes[1]
    N_sc = np.array([4, 12, 32, 64])
    opt_sc = np.array([0.680890, 0.673370, 0.665516, 0.660465])
    ces_sc = np.array([0.762911, 0.791685, 0.806492, 0.812491])
    dyadic_bins = np.array([1, 2, 4, 8, 16, 32, 64])
    dyadic_ub = np.array([0.702161, 0.676476, 0.664559, 0.657443, 0.652608, 0.649038, 0.646252])
    ax.plot(N_sc, ces_sc, "s-", color=CORAL, lw=2.2, ms=6, label=r"Calibrated Cesàro $\sqrt{N} E_{\rm Ces}/M$")
    ax.axhline(0.821058, color=CORAL, ls=":", lw=1.5, label=r"Continuum limit $\|T^*c\| = 0.8211$")
    ax.plot(N_sc, opt_sc, "o-", color=BLUE, lw=2.3, ms=6, label=r"Exact finite minimax $\sqrt{N} E_0/M$")
    ax.plot(dyadic_bins, dyadic_ub, "^--", color=TEAL, lw=2.0, ms=5.5,
            label=r"Dyadic upper bound $\downarrow C_0 = \|\Pi T^*c\|$")
    ax.annotate("Strict asymptotic\ninefficiency $> 1.27\\times$",
                xy=(58, 0.73), xytext=(15, 0.725), fontsize=8.1, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.28", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.95))
    ax.annotate("", xy=(58, 0.818), xytext=(58, 0.648),
                arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.5))
    ax.set_ylim(0.55, 0.855)
    ax.set_title(r"B. Scalene Triangle Sharp Constant $C_0$")
    ax.set_xlabel("Band cutoff $N$ (or continuum dyadic bins)")
    ax.set_ylabel(r"Normalized risk $\sqrt{N} E_0 / M$")
    ax.legend(loc="lower center", fontsize=7.3)
    ax.grid(True)

    # 1C: Even-polygon alternating mode: integer blindness vs shifted readout
    ax = axes[2]
    m_idx = np.arange(0, 7)
    int_read = np.zeros_like(m_idx, dtype=float)
    half_read = np.array([2.0 * (1.0 - np.exp(-2 * np.pi * (m + 0.5))) for m in m_idx])
    ax.plot(m_idx + 1, int_read, "o--", color=SLATE, lw=2.0, ms=6,
            label=r"Integer nodes $\nu_{1,m}$ (reads exact $0$!)")
    ax.plot(m_idx + 0.5, half_read, "s-", color=CORAL, lw=2.3, ms=6.5,
            label=r"Half-shifted $\nu_{1,m+1/2}$ ($1.9136 \to 2.0000$)")
    ax.axhline(2.0, color=TEAL, ls=":", lw=1.5, label=r"True $a_1 - a_2 = 2$")
    ax.annotate("First shifted sample\nreads $1.91357216$!",
                xy=(0.5, 1.9136), xytext=(1.8, 1.15), fontsize=8.2, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.3))
    ax.set_ylim(-0.18, 2.28)
    ax.set_title("C. Unmasking Alternating Square Charges")
    ax.set_xlabel("Harmonic index along edge 1")
    ax.set_ylabel("Phase-calibrated spectral reading")
    ax.legend(loc="center right", fontsize=7.5)
    ax.grid(True)

    plt.tight_layout()
    fig.savefig(P2_FIGS / "p2_fig1_parity_and_minimax_odd.png", dpi=300)
    plt.close(fig)

    # --- P2 Fig 2: 60/120 Rhombus Two-Slope Law + Normalized Scaling + Square Shift Certificate ---
    fig, axes = plt.subplots(1, 3, figsize=(16.0, 4.9), dpi=300)
    N_rh = np.array(data["rhombus"]["N"], dtype=float)
    risks_rh = np.array([[float(x) for x in row] for row in data["rhombus"]["risks"]])
    scaled_rh = np.array(data["rhombus"]["scaled"])

    # 2A: Raw log-log slopes on the 60/120 rhombus
    ax = axes[0]
    ax.loglog(N_rh, risks_rh[:, 1], "o-", color=CORAL, lw=2.2, ms=6, label=r"Blunt $120^\circ$ ($v_1$, fit $0.653$ vs $2/3$)")
    ax.loglog(N_rh, risks_rh[:, 3], "o--", color="#fb7185", lw=1.8, ms=5, label=r"Blunt $120^\circ$ ($v_3$, fit $0.671$ vs $2/3$)")
    ax.loglog(N_rh, risks_rh[:, 0], "^-", color=TEAL, lw=2.3, ms=6.5, label=r"Sharp $60^\circ$ ($v_0$, fit $0.843$ vs $5/6$)")
    ax.loglog(N_rh, risks_rh[:, 2], "^--", color="#2dd4bf", lw=1.8, ms=5.5, label=r"Sharp $60^\circ$ ($v_2$, fit $0.849$ vs $5/6$)")
    nr = np.array([2.0, 20.0])
    ax.loglog(nr, 0.56 * nr ** (-2 / 3), ":", color=CORAL, lw=1.3)
    ax.loglog(nr, 0.52 * nr ** (-5 / 6), ":", color=TEAL, lw=1.3)

    inset = ax.inset_axes([0.06, 0.06, 0.36, 0.31])
    u = np.array([0.5, np.sqrt(3) / 2])
    rv = np.array([[0.0, 0.0], [1.0, 0.0], np.array([1.0, 0.0]) + u, u])
    inset.add_patch(patches.Polygon(rv, closed=True, facecolor="#f0fdfa", edgecolor=NAVY, lw=1.6))
    inset.plot([0, 1], [0, 0], color=AMBER, lw=3.0)
    inset.scatter([0, 1.0 + u[0]], [0, u[1]], color=TEAL, s=34, zorder=5)
    inset.scatter([1, u[0]], [0, u[1]], color=CORAL, s=34, zorder=5)
    inset.text(0.14, 0.14, "60°", fontsize=7.4, color=TEAL, fontweight="bold")
    inset.text(0.72, 0.14, "120°", fontsize=7.4, color=CORAL, fontweight="bold")
    inset.set_xlim(-0.18, 1.68)
    inset.set_ylim(-0.28, 1.04)
    inset.set_aspect("equal")
    inset.axis("off")

    ax.set_title(r"A. $60^\circ/120^\circ$ Rhombus: $N^{-5/6}$ vs $N^{-2/3}$")
    ax.set_xlabel("Band cutoff $N$")
    ax.set_ylabel("Exact minimax vertex risk $E_k / M$")
    ax.legend(loc="upper right", fontsize=7.3)
    ax.grid(True, which="both", alpha=0.45)

    # 2B: Rescaled N^(1 - omega_k / 2pi) * E_k stability check (including unit square N^3/4)
    ax = axes[1]
    N_sq_sh = np.array([2, 4, 8, 12], dtype=float)
    sq_sc_v0 = np.array([0.523620, 0.544775, 0.528941, 0.530178])
    sq_sc_max = np.array([0.680376, 0.693348, 0.719365, 0.676709])
    ax.plot(N_rh, scaled_rh[:, 0], "^-", color=TEAL, lw=2.1, ms=6, label=r"Rhombus $60^\circ$: $N^{5/6} E_0/M$")
    ax.plot(N_rh, scaled_rh[:, 1], "o-", color=CORAL, lw=2.1, ms=5.5, label=r"Rhombus $120^\circ$: $N^{2/3} E_1/M$")
    ax.plot(N_sq_sh, sq_sc_v0, "s--", color=BLUE, lw=2.0, ms=5.5, label=r"Square $90^\circ$ ($v_0$): $N^{3/4} E_0/M$")
    ax.plot(N_sq_sh, sq_sc_max, "D:", color=PURPLE, lw=1.9, ms=5, label=r"Square $90^\circ$ (max): $N^{3/4} E_\infty/M$")
    ax.set_ylim(0.42, 0.86)
    ax.set_title(r"B. Rescaled Stability $N^{1-\omega_k/(2\pi)} E_k / M$")
    ax.set_xlabel("Band cutoff $N$")
    ax.set_ylabel(r"Normalized risk $N^{\beta_k/2} E_k / M$")
    ax.legend(loc="upper right", fontsize=7.5)
    ax.grid(True)

    # 2C: Interval-Certified Suboptimality of Half-Step on Unit Square
    ax = axes[2]
    theta = np.array(data["square"]["theta"])
    for idx, (N_val, col) in enumerate([(1, CORAL), (2, BLUE), (4, TEAL)]):
        rmat = np.array([[float(x) for x in row] for row in data["square"]["risks"][idx]])
        emax = rmat.max(axis=1)
        ax.plot(theta, emax, "-", color=col, lw=2.2, label=f"$N = {N_val}$")
        hval = max(float(x) for x in data["square"]["optima"][idx]["half_step_risks"])
        ax.scatter([0.5], [hval], color=col, marker="x", s=65, lw=2.0, zorder=6)
        opt = data["square"]["optima"][idx]
        ax.scatter([float(opt["shift_bracket"][0])], [float(opt["risk_bracket"][0])],
                   color="#fbbf24", edgecolor=NAVY, marker="*", s=125, zorder=7)
    ax.axvline(0.5, color=SLATE, ls="--", lw=1.2)
    ax.annotate(r"$N=1$: $\theta\uparrow 1$ ($0.6099$)", xy=(0.99, 0.610), xytext=(0.48, 0.82),
                fontsize=7.7, color=CORAL, fontweight="bold", arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.1))
    ax.annotate(r"$N=2$: $\theta\downarrow 0$ ($0.3735$)", xy=(0.01, 0.374), xytext=(0.14, 0.49),
                fontsize=7.7, color=BLUE, fontweight="bold", arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1))
    ax.annotate(r"$N=4$: $\theta^*\!\approx\!0.1133$ ($0.2422$)", xy=(0.1133, 0.2422), xytext=(0.24, 0.15),
                fontsize=7.7, color=TEAL, fontweight="bold", arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.1))
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(0.11, 1.25)
    ax.set_title(r"C. Global Shift Risk $E_\infty(N,\theta)/M$ on Square")
    ax.set_xlabel(r"Fractional shift $\theta \in (0, 1)$")
    ax.set_ylabel(r"$E_\infty(N, \theta) / M$")
    ax.legend(loc="upper right", fontsize=8.2)
    ax.grid(True)

    plt.tight_layout()
    fig.savefig(P2_FIGS / "p2_fig2_rhombus_and_shift_certificate.png", dpi=300)
    plt.close(fig)

    # --- P2 Fig 3: Super-Resolution, Chebyshev Trade-off, and Discontinuous Heated Plate ---
    fig, axes = plt.subplots(1, 3, figsize=(16.0, 4.8), dpi=300)

    # 3A: Super-resolution convergence
    ax = axes[0]
    N_sr = np.array([32, 64, 128])
    ax.loglog(N_sr, [7.409e-2, 4.319e-2, 2.469e-2], "o-", color=CORAL, lw=2.1, ms=5.5, label="Calibrated Cesàro (square)")
    ax.loglog(N_sr, [5.759e-2, 3.373e-2, 1.935e-2], "o--", color="#fb7185", lw=1.8, ms=5, label="Calibrated Cesàro (triangle)")
    ax.loglog(N_sr, [1.076e-8, 6.807e-10, 4.281e-11], "s-", color=BLUE, lw=2.1, ms=5.5, label=r"$r=3$ window (square, $O(N^{-4})$)")
    ax.loglog(N_sr, [4.501e-9, 2.784e-10, 1.734e-11], "s--", color="#60a5fa", lw=1.8, ms=5, label=r"$r=3$ window (triangle)")
    ax.loglog(N_sr, [2.454e-11, 5.597e-23, 8.304e-26], "^-", color=TEAL, lw=2.3, ms=6, label="Extrapolation window (square)")
    ax.loglog(N_sr, [1.453e-11, 3.961e-23, 6.049e-26], "^--", color="#2dd4bf", lw=1.9, ms=5.5, label="Extrapolation window (triangle)")
    ax.set_xticks(N_sr)
    ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())
    ax.set_ylim(1e-29, 1e0)
    ax.set_title("A. Smooth & Analytic Super-Resolution")
    ax.set_xlabel("Band cutoff $N$")
    ax.set_ylabel("Max vertex error (80-digit mpmath)")
    ax.legend(loc="lower left", fontsize=7.1)
    ax.grid(True, which="both", alpha=0.45)

    # 3B: Chebyshev Weight-Norm Lower Bound vs Actual Extrapolation Window Norm
    ax = axes[1]
    orders = np.arange(1, 11)
    # Band [a, b] = [0.5, 1.0] -> (a+b)/(b-a) = 3.0
    a_b, b_b = 0.5, 1.0
    cheb_arg = (a_b + b_b) / (b_b - a_b)
    cheb_lb = np.cosh(orders * np.arccosh(cheb_arg))
    actual_l1 = []
    for r_ord in orders:
        xs_i = np.linspace(a_b, b_b, r_ord + 1)
        d_step = (b_b - a_b) / r_ord
        ws = [((-1) ** (r_ord - i)) * (xs_i[i] ** r_ord) /
              ((d_step ** r_ord) * special.factorial(i) * special.factorial(r_ord - i))
              for i in range(r_ord + 1)]
        actual_l1.append(np.sum(np.abs(ws)))
    ax.semilogy(orders, actual_l1, "o-", color=BLUE, lw=2.2, ms=6,
                label=r"Equispaced extrapolation $\|w\|_1$ on $[\frac{1}{2}N, N]$")
    ax.semilogy(orders, cheb_lb, "s--", color=CORAL, lw=2.1, ms=5.5,
                label=r"Universal Chebyshev lower bound $|T_r(3)|$")
    ax.annotate("Unavoidable noise-amplification\ncost of cancelling $r$ poles\non any high band $[aN, bN]$",
                xy=(7, cheb_lb[6]), xytext=(2.2, 3e6), fontsize=7.9, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.28", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.set_xticks(orders)
    ax.set_title("B. Chebyshev Amplification Barrier")
    ax.set_xlabel("Inverse-power cancellation order $r$")
    ax.set_ylabel(r"Window $\ell^1$ norm $\|w\|_1$")
    ax.legend(loc="lower right", fontsize=7.5)
    ax.grid(True, which="both", alpha=0.45)

    # 3C: Discontinuous Wall Temperature Heated Plate
    ax = axes[2]
    gx = np.linspace(0.005, 0.995, 105)
    XX, YY = np.meshgrid(gx, gx)

    def side_h(X, Y, Tv):
        u = np.zeros_like(X)
        for n in range(1, 55, 2):
            k = n * np.pi
            u += (4.0 * Tv / k) * np.sin(k * X) * np.sinh(k * (1.0 - Y)) / np.sinh(k)
        return u

    Q_sq = side_h(XX, YY, 1.0) + side_h(YY, 1.0 - XX, 4.0) + side_h(XX, 1.0 - YY, -2.0) + side_h(YY, XX, 5.0)
    im = ax.contourf(XX, YY, Q_sq, levels=22, cmap="coolwarm", vmin=-2.2, vmax=5.2)
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.0))
    ax.text(0.5, -0.09, "$T_1=1$", ha="center", va="top", fontsize=8.8, fontweight="bold", color=NAVY)
    ax.text(1.07, 0.5, "$T_2=4$", ha="left", va="center", fontsize=8.8, fontweight="bold", color=CORAL)
    ax.text(0.5, 1.07, "$T_3=-2$", ha="center", va="bottom", fontsize=8.8, fontweight="bold", color=BLUE)
    ax.text(-0.07, 0.5, "$T_4=5$", ha="right", va="center", fontsize=8.8, fontweight="bold", color=CORAL)
    for (vx, vy), txt, tx, ty in [
        ((0, 0), "$a_1=-4$", -0.15, -0.11), ((1, 0), "$a_2=+3$", 1.15, -0.11),
        ((1, 1), "$a_3=-6$", 1.15, 1.10), ((0, 1), "$a_4=+7$", -0.15, 1.10),
    ]:
        ax.scatter([vx], [vy], color="#fbbf24", edgecolor=NAVY, s=55, zorder=6)
        ax.text(tx, ty, txt, ha="center", va="center", fontsize=7.6, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.16", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.92))
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    ax.set_xlim(-0.35, 1.36)
    ax.set_ylim(-0.24, 1.24)
    ax.set_aspect("equal")
    ax.set_title(r"C. Hadamard Finite-Part Jump Readout")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    plt.tight_layout()
    fig.savefig(P2_FIGS / "p2_fig3_superresolution_and_heat_plate.png", dpi=300)
    plt.close(fig)
    print("Built all Paper 2 dedicated figures!")


# ==============================================================================
# KOREAN EXPOSITORY MAGAZINE FIGURES (Natural Korean Labels!)
# ==============================================================================
def build_korean_magazine_figures():
    set_kr_style()
    data = json.loads((EXP / "phase3_data.json").read_text())
    tri_npz = np.load(EXP / "data" / "phase3_triangle.npz")
    x_tri = tri_npz["x"]
    g_L2 = tri_npz["g_L2"]
    g_s0 = tri_npz["g_s"][0]
    proj_768 = tri_npz["projection"][-1]

    # --- KR Fig 1: 다각형 주파수와 유령 파동 ---
    fig, axes = plt.subplots(1, 3, figsize=(15.8, 4.9), dpi=260)

    ax = axes[0]
    tri = np.array([0, 1, 0.5 + 1j * np.sqrt(3) / 2]) - (0.5 + 1j * np.sqrt(3) / 6)
    tri_s = tri * 0.9 - 1.55
    sq_s = np.array([-0.5 - 0.5j, 0.5 - 0.5j, 0.5 + 0.5j, -0.5 + 0.5j]) * 0.85 + 1.55
    for poly, center, col, label in [
        (tri_s, -1.55 + 0j, TEAL, "정삼각형\n(3방향 반직선 주파수)"),
        (sq_s, 1.55 + 0j, BLUE, "정사각형\n(4방향 반직선 주파수)"),
    ]:
        ax.add_patch(patches.Polygon(np.c_[poly.real, poly.imag], closed=True,
                                     facecolor=col, alpha=0.16, edgecolor=col, lw=2.1))
        ax.scatter(poly.real, poly.imag, color=NAVY, s=26, zorder=5)
        for j in range(len(poly)):
            d = poly[(j + 1) % len(poly)] - poly[j]
            u = (1j / d) / abs(1j / d)
            for m in range(1, 5):
                pt = center + u * (0.42 + 0.24 * m)
                ax.scatter(pt.real, pt.imag, color=col, s=18 + 3 * (5 - m), alpha=0.85, zorder=4)
            end = center + u * 1.55
            ax.annotate("", xy=(end.real, end.imag), xytext=(center.real, center.imag),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.2, alpha=0.55, ls="--"))
        ax.text(center.real, -1.78, label, ha="center", va="top", fontsize=9.2, color=NAVY, fontweight="bold")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.3, 1.9)
    ax.set_aspect("equal")
    ax.set_title("A. 도형의 모양이 결정하는 레온티예프 주파수")
    ax.set_xlabel("실수축")
    ax.set_ylabel("허수축")
    ax.grid(True)

    ax = axes[1]
    xs = np.linspace(-0.46, 0.46, 115)
    X, Y = np.meshgrid(xs, xs)
    G0 = square_ghost_single(X + 1j * Y, n_terms=12)
    im = ax.imshow(np.real(G0), extent=[-0.46, 0.46, -0.46, 0.46],
                   origin="lower", cmap="RdBu_r", vmin=-3.5, vmax=3.5, aspect="equal")
    ax.add_patch(patches.Rectangle((-0.5, -0.5), 1.0, 1.0, fill=False, edgecolor=NAVY, lw=2.1))
    ax.scatter([0.17], [0.13], color="#fbbf24", edgecolor=NAVY, s=60, zorder=6)
    ax.annotate("한 방향 파동은 ±3.5로 출렁이지만\n90° 회전한 4개 파동을 합치면\n내부 전체에서 5.5×10⁻⁴⁷ (완벽한 0)!",
                xy=(0.17, 0.13), xytext=(-0.46, -0.43), fontsize=8.2, color=NAVY, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.32", facecolor="white", edgecolor=NAVY, alpha=0.92),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2))
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    ax.set_xlim(-0.56, 0.56)
    ax.set_ylim(-0.56, 0.56)
    ax.set_title("B. 정사각형의 '유령 파동' (0의 비자명한 전개)")
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")

    ax = axes[2]
    N_sq = np.array([4, 8, 16, 32, 56])
    ax.semilogy(N_sq, [2.673e-2, 2.478e-5, 5.062e-12, 7.545e-26, 5.515e-47], "o-", color=CORAL, lw=2.0, label="정사각형 유령 파동 합 (→ 0)")
    ax.semilogy(N_sq, [6.538e-4, 3.894e-7, 4.890e-14, 3.661e-28, 1.545e-49], "s-", color=BLUE, lw=2.0, label="정사각형 함수 복원 오차")
    ax.semilogy(N_sq, [2.527e-3, 1.726e-6, 2.451e-13, 8.755e-28, 4.454e-50], "^--", color=AMBER, lw=2.2, label="제곱수 번호(1,4,9,…) 주파수 삭제 후!")
    ax.semilogy([8, 16, 32, 64, 80], [1.744e-3, 1.899e-6, 1.659e-12, 9.146e-25, 6.400e-31], "D-", color=TEAL, lw=2.0, label="정삼각형 함수 복원 오차")
    ax.annotate("사각형 바깥(z=0.71+0.17i):\n개별 항은 5.27×10²⁷ 폭주,\n연장된 4파동 합은 4.89×10⁻⁶⁵!",
                xy=(56, 5.5e-47), xytext=(5, 2e-43), fontsize=8.0, color=NAVY, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2))
    ax.set_ylim(1e-53, 1e0)
    ax.set_title("C. 초고속 지수 수렴과 주파수 삭제 내구성")
    ax.set_xlabel("반직선당 주파수 개수 (N)")
    ax.set_ylabel("절대 오차 (65자리 정밀도)")
    ax.legend(loc="upper right", fontsize=7.8)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout()
    fig.savefig(KR_FIGS / "kr_fig1_concept_and_ghost.png", dpi=260)
    plt.close(fig)

    # --- KR Fig 2: 정사각형 균일 전하 vs 정삼각형 Y자 제타 해골 & 대칭 붕괴 ---
    fig, axes = plt.subplots(2, 2, figsize=(13.8, 10.6), dpi=260)

    ax = axes[0, 0]
    gx = np.linspace(0, 1, 120)
    XX, YY = np.meshgrid(gx, gx)
    u_sq = np.zeros_like(XX)
    for n in range(1, 30, 2):
        k = n * np.pi
        u_sq += (4.0 / k**3) * np.sin(k * XX) * (1.0 - np.cosh(k * (YY - 0.5)) / np.cosh(k / 2.0))
    t_edge = np.linspace(0, 1, 250)
    sq_tor = np.zeros_like(t_edge)
    for n in range(1, 120, 2):
        k = n * np.pi
        sq_tor += (4.0 / k**2) * np.sin(k * t_edge) * np.tanh(k / 2.0)

    ax.contourf(XX, YY, u_sq, levels=20, cmap="YlOrRd")
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.1))
    sc = 0.42
    ax.plot(t_edge, -sc * sq_tor, color=BLUE, lw=2.1); ax.fill_between(t_edge, 0, -sc * sq_tor, color=BLUE, alpha=0.22)
    ax.plot(t_edge, 1 + sc * sq_tor, color=BLUE, lw=2.1); ax.fill_between(t_edge, 1, 1 + sc * sq_tor, color=BLUE, alpha=0.22)
    ax.plot(-sc * sq_tor, t_edge, color=BLUE, lw=2.1); ax.fill_betweenx(t_edge, 0, -sc * sq_tor, color=BLUE, alpha=0.22)
    ax.plot(1 + sc * sq_tor, t_edge, color=BLUE, lw=2.1); ax.fill_betweenx(t_edge, 1, 1 + sc * sq_tor, color=BLUE, alpha=0.22)
    for (vx, vy), sgn, col in [((0, 0), "+1", CORAL), ((1, 0), "-1", PURPLE),
                                ((1, 1), "+1", CORAL), ((0, 1), "-1", PURPLE)]:
        ax.scatter([vx], [vy], color=col, edgecolor="white", s=90, zorder=6)
        ax.text(vx + (-0.10 if vx == 0 else 0.10), vy + (-0.10 if vy == 0 else 0.10),
                sgn, ha="center", va="center", fontsize=9.2, fontweight="bold", color=col)
    ax.text(0.5, 0.5, "2차원 균일 내부 전하\n(생브낭 탄성 비틀림)\n→ 정사각형 주파수에\n100% 투명!",
            ha="center", va="center", fontsize=8.8, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.32", facecolor="white", alpha=0.90, edgecolor=NAVY))
    ax.set_xlim(-0.32, 1.32); ax.set_ylim(-0.32, 1.32); ax.set_aspect("equal")
    ax.set_title("A. 정사각형: 균일 전하 비틀림 응력(3종) + 교대 꼭짓점 유령(1종)")
    ax.grid(False)

    ax = axes[0, 1]
    H0 = np.sqrt(3) / 2
    v_tri = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, H0]])
    ctr = v_tri.mean(axis=0)
    ax.add_patch(patches.Polygon(v_tri, closed=True, facecolor="#ecfeff", edgecolor=NAVY, lw=2.1))
    mp.mp.dps = 30
    coeff = skeleton_coefficients(90)
    R = 1.0 / np.sqrt(3)
    rs = np.linspace(1e-4, R, 110)
    hs = np.array([float(mp.sqrt(r) * mp.polyval(coeff[::-1], mp.mpf(r) ** 3)) for r in rs])
    cmap = plt.get_cmap("plasma")
    norm = plt.Normalize(0, hs.max())
    for k in range(3):
        u_vec = (ctr - v_tri[k]) / R
        pts = v_tri[k][None, :] + rs[:, None] * u_vec[None, :]
        for i in range(len(rs) - 1):
            ax.plot(pts[i:i+2, 0], pts[i:i+2, 1], color=cmap(norm(hs[i])), lw=5.2, solid_capstyle="round", zorder=4)
    ax.scatter([ctr[0]], [ctr[1]], color="#facc15", edgecolor=NAVY, s=85, zorder=6)
    for j in range(3):
        p0, p1 = v_tri[j], v_tri[(j + 1) % 3]
        e = p1 - p0
        n_out = np.array([e[1], -e[0]]) / np.linalg.norm(e)
        base_pts = p0[None, :] + x_tri[:, None] * e[None, :]
        outer_pts = base_pts + (0.42 * g_L2)[:, None] * n_out[None, :]
        ax.plot(outer_pts[:, 0], outer_pts[:, 1], color=TEAL, lw=2.1)
        ax.add_patch(patches.Polygon(np.vstack([base_pts, outer_pts[::-1]]),
                                     closed=True, facecolor=TEAL, alpha=0.22, edgecolor="none"))
    ax.annotate("Y자 중선 해골 확률밀도 h(r)\n(리만 제타값 ζ(4), ζ(10), ζ(16), …)\n이 그림자만이 유일한 L² 투명 물리장!",
                xy=(ctr[0] + 0.04, ctr[1] + 0.03), xytext=(0.50, 1.07), ha="center",
                fontsize=8.3, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.30", facecolor="white", edgecolor=PURPLE, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.3, connectionstyle="arc3,rad=-0.22"))
    ax.scatter(v_tri[:, 0], v_tri[:, 1], color=NAVY, s=50, zorder=6)
    ax.set_xlim(-0.32, 1.32); ax.set_ylim(-0.30, 1.38); ax.set_aspect("equal")
    ax.set_title("B. 정삼각형: 유일한 투명 물리장을 만드는 'Y자 제타 해골'")
    ax.grid(False)

    ax = axes[1, 0]
    ax.plot(x_tri, g_L2, color=TEAL, lw=2.7, label=r"정삼각형 유일 투명 $L^2$ 플럭스 $g_\triangle$ ($\sim\sqrt{2/\pi}\,x^{1/2}$)")
    ax.plot(x_tri[::20], proj_768[::20], "o", color=NAVY, ms=3.8, label="독립 768-고조파 최소노름 검증")
    ax.plot(x_tri, 2.0 * x_tri * (1.0 - x_tri), "--", color=AMBER, lw=2.1, label="정삼각형 생브낭 비틀림 (투명 실패: m=1에서 들통!)")
    ax.plot(t_edge, sq_tor, ":", color=BLUE, lw=2.2, label="정사각형 생브낭 비틀림 (정사각형에선 투명)")
    ax.plot(x_tri, np.clip(g_s0, -1.2, 1.2), "-.", color=CORAL, lw=1.6, label=r"삼각형 $L^1\setminus L^2$ 특이 형제 모드 ($\sim\pm x^{-1/2}$ 발산)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlim(0, 1); ax.set_ylim(-1.1, 1.1)
    ax.set_title("C. 한 변 위에서의 물리장 단면 비교")
    ax.set_xlabel("변 위의 위치 x")
    ax.set_ylabel("경계 플럭스 밀도 (총질량 1 정규화)")
    ax.legend(loc="lower center", fontsize=7.8)
    ax.grid(True)

    ax = axes[1, 1]
    eps = np.array(data["tilt"]["epsilon"])
    sig = np.array(data["tilt"]["singular_values"])
    m = eps > 0
    for k, (col, ls, lbl) in enumerate([
        (NAVY, "-", "특이값 1 (기울기 169.53)"),
        (BLUE, "-", "특이값 2 (기울기 6.93)"),
        (TEAL, "--", "특이값 3 (기울기 6.93)"),
        (CORAL, "-", "특이값 4 (최소 모드; 기울기 0.549)"),
    ]):
        ax.loglog(eps[m], sig[m, k], ls, color=col, lw=2.1, label=lbl)
    ax.annotate("완벽한 정사각형(ε=0)에선 4개 모두 0!\n꼭짓점 하나를 ε>0만큼 비트는 순간\n양방향 투명 모드 4개가 전부 소멸!",
                xy=(1e-6, sig[m, 3][3]), xytext=(3e-6, 1.4e-1), fontsize=8.3, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.32", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.set_title("D. 양방향 주파수의 대칭 붕괴 현상")
    ax.set_xlabel("꼭짓점 비틀림 각도 ε (라디안)")
    ax.set_ylabel("투명 모드 행렬의 특이값")
    ax.legend(loc="lower right", fontsize=8.0)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout()
    fig.savefig(KR_FIGS / "kr_fig2_square_vs_triangle.png", dpi=260)
    plt.close(fig)

    # --- KR Fig 3: 60/120 마름모 이중 기울기 & 반스텝 신화 붕괴 ---
    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.1), dpi=260)

    ax = axes[0]
    N_rh = np.array(data["rhombus"]["N"], dtype=float)
    risks_rh = np.array([[float(x) for x in row] for row in data["rhombus"]["risks"]])
    N_tri = np.array([4, 12, 32, 64], dtype=float)
    risk_tri = np.array([0.680890, 0.673370, 0.665516, 0.660465]) / np.sqrt(N_tri)
    ax.loglog(N_tri, risk_tri, "s-", color=SLATE, lw=2.1, ms=5.5, label=r"홀수 삼각형 (절대 한계 $N^{-1/2}$)")
    ax.loglog(N_rh, risks_rh[:, 1], "o-", color=CORAL, lw=2.3, ms=6, label=r"마름모 뭉툭한 120° 꼭짓점 ($N^{-2/3}$, 실측 0.653)")
    ax.loglog(N_rh, risks_rh[:, 0], "^-", color=TEAL, lw=2.4, ms=6.5, label=r"마름모 뾰족한 60° 꼭짓점 ($N^{-5/6}$, 실측 0.843)")
    nr = np.array([3.0, 22.0])
    ax.loglog(nr, 0.72 * nr ** (-0.5), ":", color=SLATE, lw=1.3)
    ax.loglog(nr, 0.56 * nr ** (-2 / 3), ":", color=CORAL, lw=1.3)
    ax.loglog(nr, 0.52 * nr ** (-5 / 6), ":", color=TEAL, lw=1.3)

    inset = ax.inset_axes([0.06, 0.06, 0.35, 0.30])
    u = np.array([0.5, np.sqrt(3) / 2])
    rv = np.array([[0.0, 0.0], [1.0, 0.0], np.array([1.0, 0.0]) + u, u])
    inset.add_patch(patches.Polygon(rv, closed=True, facecolor="#f0fdfa", edgecolor=NAVY, lw=1.6))
    inset.plot([0, 1], [0, 0], color=AMBER, lw=3.0)
    inset.scatter([0, 1.0 + u[0]], [0, u[1]], color=TEAL, s=36, zorder=5)
    inset.scatter([1, u[0]], [0, u[1]], color=CORAL, s=36, zorder=5)
    inset.text(0.14, 0.14, "60°", fontsize=7.6, color=TEAL, fontweight="bold")
    inset.text(0.72, 0.14, "120°", fontsize=7.6, color=CORAL, fontweight="bold")
    inset.set_xlim(-0.18, 1.68); inset.set_ylim(-0.28, 1.04); inset.set_aspect("equal"); inset.axis("off")

    ax.set_title(r"A. 60°/120° 마름모의 두 기울기: 내각이 수렴 지수를 바꾼다!")
    ax.set_xlabel("변당 주파수 개수 (N)")
    ax.set_ylabel("꼭짓점 복원 미니맥스 오차 한계")
    ax.legend(loc="upper right", fontsize=8.0)
    ax.grid(True, which="both", alpha=0.45)

    ax = axes[1]
    theta = np.array(data["square"]["theta"])
    for idx, (N_val, col) in enumerate([(1, CORAL), (2, BLUE), (4, TEAL)]):
        rmat = np.array([[float(x) for x in row] for row in data["square"]["risks"][idx]])
        emax = rmat.max(axis=1)
        ax.plot(theta, emax, "-", color=col, lw=2.3, label=f"N = {N_val}")
        hval = max(float(x) for x in data["square"]["optima"][idx]["half_step_risks"])
        ax.scatter([0.5], [hval], color=col, marker="x", s=65, lw=2.0, zorder=6)
        opt = data["square"]["optima"][idx]
        ax.scatter([float(opt["shift_bracket"][0])], [float(opt["risk_bracket"][0])],
                   color="#fbbf24", edgecolor=NAVY, marker="*", s=130, zorder=7)
    ax.axvline(0.5, color=SLATE, ls="--", lw=1.2)
    ax.text(0.515, 1.11, "직관적인 반스텝 (θ = 0.5)\n→ 한 번도 최적인 적이 없다!", fontsize=8.4, color=NAVY, fontweight="bold")
    ax.annotate("N=1 최적: θ→1 (0.6099)", xy=(0.99, 0.610), xytext=(0.52, 0.81),
                fontsize=8.0, color=CORAL, fontweight="bold", arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.annotate("N=2 최적: θ→0 (0.3735)", xy=(0.01, 0.374), xytext=(0.14, 0.49),
                fontsize=8.0, color=BLUE, fontweight="bold", arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate("N=4 유일 최적: θ*≈0.1133", xy=(0.1133, 0.2422), xytext=(0.24, 0.15),
                fontsize=8.0, color=TEAL, fontweight="bold", arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2))
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(0.11, 1.26)
    ax.set_title("B. 정사각형에서 무너진 '반스텝(θ=1/2) 신화' (구간연산 전역 인증)")
    ax.set_xlabel("한 변에 가한 주파수 이동량 θ")
    ax.set_ylabel("최악 오차 한계 (낮을수록 정확)")
    ax.legend(loc="upper right", fontsize=8.5)
    ax.grid(True)

    plt.tight_layout()
    fig.savefig(KR_FIGS / "kr_fig3_parity_and_rhombus.png", dpi=260)
    plt.close(fig)

    # --- KR Fig 4: 24자릿수 초해상도, 포카스 PDE 사각지대 제거, 가열 금속판 ---
    sv_sq_b, sv_sq_a, sv_tr_b, sv_tr_a = compute_fokas_svd_and_field()
    fig, axes = plt.subplots(1, 3, figsize=(16.2, 5.0), dpi=260)

    ax = axes[0]
    N_sr = np.array([32, 64, 128])
    ax.loglog(N_sr, [7.409e-2, 4.319e-2, 2.469e-2], "o-", color=CORAL, lw=2.1, ms=6, label="단순 보정 평균 (정사각형)")
    ax.loglog(N_sr, [1.076e-8, 6.807e-10, 4.281e-11], "s-", color=BLUE, lw=2.1, ms=6, label="3차 역거듭제곱 소거 윈도우")
    ax.loglog(N_sr, [2.454e-11, 5.597e-23, 8.304e-26], "^-", color=TEAL, lw=2.4, ms=6.5, label="외삽 초해상도 윈도우 (정사각형)")
    ax.loglog(N_sr, [1.453e-11, 3.961e-23, 6.049e-26], "^--", color="#2dd4bf", lw=1.9, ms=5.5, label="외삽 초해상도 윈도우 (삼각형)")
    ax.annotate("무려 23.5자릿수 정밀도 향상!\n(삼각형: 1.9×10⁻² → 6.0×10⁻²⁶)",
                xy=(128, 6.05e-26), xytext=(48, 5e-18), fontsize=8.2, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#ecfdf5", edgecolor=TEAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.3))
    ax.set_xticks(N_sr); ax.get_xaxis().set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())
    ax.set_ylim(1e-29, 1e0)
    ax.set_title("A. 매끄러운 배경에서의 24자릿수 초해상도")
    ax.set_xlabel("변당 주파수 개수 (N)")
    ax.set_ylabel("최대 꼭짓점 복원 오차")
    ax.legend(loc="lower left", fontsize=7.6)
    ax.grid(True, which="both", alpha=0.45)

    ax = axes[1]
    ax.semilogy(np.arange(1, len(sv_sq_b) + 1), sv_sq_b, "o--", color=CORAL, lw=2.0, label="정사각형 보완 전 (영공간 3개!)")
    ax.semilogy(np.arange(1, len(sv_sq_a) + 1), sv_sq_a, "o-", color=BLUE, lw=2.3, label="정사각형 3개 모멘트 보완 후")
    ax.semilogy(np.arange(1, len(sv_tr_b) + 1), sv_tr_b, "s--", color=AMBER, lw=2.0, label="정삼각형 보완 전 (영공간 1개!)")
    ax.semilogy(np.arange(1, len(sv_tr_a) + 1), sv_tr_a, "s-", color=TEAL, lw=2.3, label="정삼각형 1개 모멘트 보완 후")
    ax.annotate("보완 후 내부 PDE 오차:\n정사각형 3.9×10⁻¹⁶\n정삼각형 2.4×10⁻¹⁵",
                xy=(9, sv_sq_a[-1]), xytext=(4.3, 1e-6), fontsize=8.2, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=BLUE, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.set_xticks(range(1, 10)); ax.set_ylim(1e-18, 1e2)
    ax.set_title("B. 현대 포카스 PDE 해법의 사각지대 제거")
    ax.set_xlabel("특이값 번호")
    ax.set_ylabel("특이값 크기")
    ax.legend(loc="lower left", fontsize=7.6)
    ax.grid(True, which="both", alpha=0.45)

    ax = axes[2]
    gx = np.linspace(0.005, 0.995, 105)
    XX, YY = np.meshgrid(gx, gx)

    def side_h(X, Y, Tv):
        u = np.zeros_like(X)
        for n in range(1, 55, 2):
            k = n * np.pi
            u += (4.0 * Tv / k) * np.sin(k * X) * np.sinh(k * (1.0 - Y)) / np.sinh(k)
        return u

    Q_sq = side_h(XX, YY, 1.0) + side_h(YY, 1.0 - XX, 4.0) + side_h(XX, 1.0 - YY, -2.0) + side_h(YY, XX, 5.0)
    im = ax.contourf(XX, YY, Q_sq, levels=22, cmap="coolwarm", vmin=-2.2, vmax=5.2)
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.1))
    ax.text(0.5, -0.09, "아래 벽 1°C", ha="center", va="top", fontsize=8.6, fontweight="bold", color=NAVY)
    ax.text(1.07, 0.5, "오른벽\n4°C", ha="left", va="center", fontsize=8.6, fontweight="bold", color=CORAL)
    ax.text(0.5, 1.07, "위 벽 -2°C", ha="center", va="bottom", fontsize=8.6, fontweight="bold", color=BLUE)
    ax.text(-0.07, 0.5, "왼벽\n5°C", ha="right", va="center", fontsize=8.6, fontweight="bold", color=CORAL)
    for (vx, vy), txt, tx, ty in [
        ((0, 0), "점프 -4", -0.15, -0.11), ((1, 0), "점프 +3", 1.15, -0.11),
        ((1, 1), "점프 -6", 1.15, 1.10), ((0, 1), "점프 +7", -0.15, 1.10),
    ]:
        ax.scatter([vx], [vy], color="#fbbf24", edgecolor=NAVY, s=55, zorder=6)
        ax.text(tx, ty, txt, ha="center", va="center", fontsize=7.8, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.16", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.92))
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    ax.set_xlim(-0.35, 1.36); ax.set_ylim(-0.24, 1.24); ax.set_aspect("equal")
    ax.set_title("C. 벽 온도가 끊기는 금속판의 꼭짓점 열유속 해독")
    ax.grid(False)

    plt.tight_layout()
    fig.savefig(KR_FIGS / "kr_fig4_superres_and_plate.png", dpi=260)
    plt.close(fig)
    print("Built all Korean Magazine dedicated figures!")


if __name__ == "__main__":
    build_paper1_figures()
    build_paper2_figures()
    build_korean_magazine_figures()
    print("ALL 10 DEDICATED FIGURES GENERATED!")
