"""Generate publication-grade visual figures for Project ReMath (A. F. Leont'ev)."""

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path as MplPath
import mpmath as mp
import numpy as np
from scipy import special

ROOT = Path(__file__).resolve().parent.parent
EXP = ROOT / "experiments"
FIGS = ROOT / "figures"
FIGS.mkdir(exist_ok=True)
sys.path.insert(0, str(EXP))

from phase3_anatomy_and_rhombus import skeleton_coefficients

# Clean scientific styling
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 11.5,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "axes.edgecolor": "#334155",
    "axes.linewidth": 0.9,
    "grid.color": "#cbd5e1",
    "grid.linestyle": "--",
    "grid.alpha": 0.6,
    "legend.framealpha": 0.92,
    "legend.edgecolor": "#cbd5e1",
    "figure.facecolor": "white",
    "axes.facecolor": "#fafbfc",
})

NAVY = "#0f172a"
BLUE = "#2563eb"
TEAL = "#0d9488"
CORAL = "#e11d48"
AMBER = "#d97706"
PURPLE = "#7c3aed"
SLATE = "#64748b"


def square_ghost_single(z, n_terms=18):
    """Evaluate G(w) = sum_{m>=1} (-1)^m (2*pi*m)^2 / (2*sinh(pi*m)) * exp(2*pi*m*w) on complex grid."""
    out = np.zeros_like(z, dtype=np.complex128)
    for m in range(1, n_terms + 1):
        coeff = ((-1) ** m) * (2 * np.pi * m) ** 2 / (2.0 * np.sinh(np.pi * m))
        out += coeff * np.exp(2 * np.pi * m * z)
    return out


def continued_ghost_grid(w_arr, n_terms=20):
    """Meromorphic Lambert continuation of G(w) valid outside the square too."""
    out = np.zeros_like(w_arr, dtype=np.complex128)
    for k in range(n_terms):
        q = -np.exp(2 * np.pi * (w_arr - k - 0.5))
        # Avoid exact pole division
        denom = (1.0 - q) ** 3
        out += (2 * np.pi) ** 2 * q * (1.0 + q) / denom
    return out


def make_fig1():
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.2), dpi=220)
    fig.suptitle(
        "Figure 1. Leont'ev's Polygon Frequencies, Square Ghost Waves, and Super-Resilient Erasure",
        fontsize=13.5, fontweight="bold", color=NAVY, y=0.99,
    )

    # --- Panel A: Equilateral triangle & square with Leont'ev frequency rays ---
    ax = axes[0]
    tri = np.array([0, 1, 0.5 + 1j * np.sqrt(3) / 2]) - (0.5 + 1j * np.sqrt(3) / 6)
    tri_scaled = tri * 0.9 - 1.55
    sq = np.array([-0.5 - 0.5j, 0.5 - 0.5j, 0.5 + 0.5j, -0.5 + 0.5j]) * 0.85 + 1.55

    for poly, center, col, label in [
        (tri_scaled, -1.55 + 0j, TEAL, "Equilateral Triangle\n(3 rays, 120° apart)"),
        (sq, 1.55 + 0j, BLUE, "Unit Square\n(4 rays, 90° apart)"),
    ]:
        patch = patches.Polygon(np.c_[poly.real, poly.imag], closed=True,
                                facecolor=col, alpha=0.16, edgecolor=col, lw=2.2)
        ax.add_patch(patch)
        ax.scatter(poly.real, poly.imag, color=NAVY, s=28, zorder=5)
        n = len(poly)
        for j in range(n):
            d = poly[(j + 1) % n] - poly[j]
            mid = 0.5 * (poly[j] + poly[(j + 1) % n])
            # Outward ray direction i / d (unit scaled for visual)
            ray_dir = 1j / d
            ray_dir /= abs(ray_dir)
            # Note: for visual clarity, draw outward perpendicular rays from polygon center
            # Actually -i*d/|d| is outward normal of edge; i/d = conj(i*d)/|d|^2 -> show actual Leont'ev ray direction!
            # Wait: for horizontal bottom edge d=1, i/d = +i (pointing UP, inward normal! Wait: in z-plane
            # Re((i/d)(z - gamma_j)) < 0 inside D? Let's check: z = 0.5 + 0.2i -> (i/1)*(0.5+0.2i) = -0.2 + 0.5i -> Re < 0!
            # So the ray in the SPECTRAL s-plane points along i/d (which is perpendicular to edge d in C, rotated by conj).
            # Let's plot the rays emanating from origin-shifted spectral anchors clearly labeled!
            for m in range(1, 5):
                pt = center + ray_dir * (0.42 + 0.24 * m)
                ax.scatter(pt.real, pt.imag, color=col, s=18 + 3 * (5 - m), alpha=0.85, zorder=4)
            end = center + ray_dir * 1.55
            ax.annotate("", xy=(end.real, end.imag), xytext=(center.real, center.imag),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.3, alpha=0.55, ls="--"))
        ax.text(center.real, -1.78, label, ha="center", va="top", fontsize=9.2, color=NAVY, fontweight="bold")

    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-2.25, 1.9)
    ax.set_aspect("equal")
    ax.set_title("A. Polygon Geometry → Leont'ev Frequency Rays")
    ax.set_xlabel(r"Real axis (physical $D$ & spectral rays $\nu_{jm} = 2\pi i m / d_j$)")
    ax.set_ylabel("Imaginary axis")
    ax.grid(True)

    # --- Panel B: Ghost Wave inside square + exterior cancellation slice ---
    ax = axes[1]
    xs = np.linspace(-0.46, 0.46, 120)
    ys = np.linspace(-0.46, 0.46, 120)
    X, Y = np.meshgrid(xs, ys)
    Z = X + 1j * Y
    G0 = square_ghost_single(Z, n_terms=12)
    im = ax.imshow(
        np.real(G0), extent=[-0.46, 0.46, -0.46, 0.46],
        origin="lower", cmap="RdBu_r", vmin=-3.5, vmax=3.5, aspect="equal",
    )
    sq_box = patches.Rectangle((-0.5, -0.5), 1.0, 1.0, fill=False, edgecolor=NAVY, lw=2.2)
    ax.add_patch(sq_box)
    # Mark test point inside and exterior continued point
    ax.scatter([0.17], [0.13], color="#fbbf24", edgecolor=NAVY, s=65, zorder=6, label=r"$z_{\rm in}=0.17+0.13i$")
    ax.annotate(
        "Single edge wave Re G(z)\noscillates strongly (±3.5),\nyet sum of 4 rotated waves\n= 5.5 × 10⁻⁴⁷ inside!",
        xy=(0.17, 0.13), xytext=(-0.47, -0.44),
        fontsize=8.3, color=NAVY, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.35", facecolor="white", edgecolor=NAVY, alpha=0.92),
        arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2),
    )
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    cbar.set_label(r"$\mathrm{Re}\,G(z)$ (one of 4 waves)", fontsize=8.8)
    ax.set_xlim(-0.56, 0.56)
    ax.set_ylim(-0.56, 0.56)
    ax.set_title(r"B. Square Ghost Wave: $\sum_{\ell=0}^3 i^\ell G(i^\ell z) \equiv 0$")
    ax.set_xlabel(r"$\mathrm{Re}(z)$")
    ax.set_ylabel(r"$\mathrm{Im}(z)$")

    # --- Panel C: Convergence & Square-Index Erasure Miracle (from verified 65-digit Phase 1 data) ---
    ax = axes[2]
    N_sq = np.array([4, 8, 16, 32, 56])
    err_ghost = np.array([2.673e-2, 2.478e-5, 5.062e-12, 7.545e-26, 5.515e-47])
    err_wave = np.array([6.538e-4, 3.894e-7, 4.890e-14, 3.661e-28, 1.545e-49])
    err_erased = np.array([2.527e-3, 1.726e-6, 2.451e-13, 8.755e-28, 4.454e-50])
    N_tri = np.array([8, 16, 32, 64, 80])
    err_tri = np.array([1.744e-3, 1.899e-6, 1.659e-12, 9.146e-25, 6.400e-31])

    ax.semilogy(N_sq, err_ghost, "o-", color=CORAL, lw=2.0, ms=6, label="Square ghost sum residual")
    ax.semilogy(N_sq, err_wave, "s-", color=BLUE, lw=2.0, ms=5.5, label=r"Square $e^{az}$ reconstruction")
    ax.semilogy(N_sq, err_erased, "^--", color=AMBER, lw=2.2, ms=6.5, label=r"Square after erasing ALL $m=k^2$ modes!")
    ax.semilogy(N_tri, err_tri, "D-", color=TEAL, lw=2.0, ms=5.5, label=r"Equilateral triangle $e^{az}$")

    ax.annotate(
        "Outside square (z=0.71+0.17i):\n1 term = 5.27×10²⁷, yet\ncontinued 4-wave sum = 4.89×10⁻⁶⁵",
        xy=(56, 5.5e-47), xytext=(5, 2e-43),
        fontsize=7.9, color=NAVY,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2),
    )
    ax.set_title("C. Exponential Convergence & Erasure Resilience")
    ax.set_xlabel("Modes per ray ($N$)")
    ax.set_ylabel("Absolute error (65-digit mpmath)")
    ax.set_ylim(1e-53, 1e0)
    ax.legend(loc="upper right", fontsize=8.0)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    out = FIGS / "fig1_ghost_waves_and_frequencies.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print("Saved", out)


def make_fig2():
    data = json.loads((EXP / "phase3_data.json").read_text())
    tri_npz = np.load(EXP / "data" / "phase3_triangle.npz")
    x_tri = tri_npz["x"]
    g_L2 = tri_npz["g_L2"]
    g_s0 = tri_npz["g_s"][0]
    g_is0 = tri_npz["g_is"][0]
    proj_768 = tri_npz["projection"][-1]

    fig, axes = plt.subplots(2, 2, figsize=(14.5, 11.0), dpi=220)
    fig.suptitle(
        "Figure 2. Invisible Physical Loads: Uniform Charge (Square) vs. Y-Shaped Zeta Skeleton (Triangle)",
        fontsize=13.5, fontweight="bold", color=NAVY, y=0.985,
    )

    # --- Panel A: Square Uniform Charge (Saint-Venant Torsion) ---
    ax = axes[0, 0]
    gx = np.linspace(0, 1, 140)
    gy = np.linspace(0, 1, 140)
    XX, YY = np.meshgrid(gx, gy)
    # Torsion solution -Delta u = 1 on [0,1]^2 via odd sine series
    u_sq = np.zeros_like(XX)
    for n in range(1, 30, 2):
        k = n * np.pi
        u_sq += (4.0 / k**3) * np.sin(k * XX) * (1.0 - np.cosh(k * (YY - 0.5)) / np.cosh(k / 2.0))
    # Compute boundary normal flux -du/dn along bottom edge y=0
    t_edge = np.linspace(0, 1, 300)
    sq_torsion_edge = np.zeros_like(t_edge)
    for n in range(1, 120, 2):
        k = n * np.pi
        sq_torsion_edge += (4.0 / k**2) * np.sin(k * t_edge) * np.tanh(k / 2.0)

    im = ax.contourf(XX, YY, u_sq, levels=22, cmap="YlOrRd")
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.2))
    # Draw outward boundary flux profile as glowing ribbon around the 4 sides
    scale = 0.42
    ax.plot(t_edge, -scale * sq_torsion_edge, color=BLUE, lw=2.2, label=r"Invisible torsion flux $-\partial_n u$")
    ax.fill_between(t_edge, 0, -scale * sq_torsion_edge, color=BLUE, alpha=0.22)
    ax.plot(t_edge, 1 + scale * sq_torsion_edge, color=BLUE, lw=2.2)
    ax.fill_between(t_edge, 1, 1 + scale * sq_torsion_edge, color=BLUE, alpha=0.22)
    ax.plot(-scale * sq_torsion_edge, t_edge, color=BLUE, lw=2.2)
    ax.fill_betweenx(t_edge, 0, -scale * sq_torsion_edge, color=BLUE, alpha=0.22)
    ax.plot(1 + scale * sq_torsion_edge, t_edge, color=BLUE, lw=2.2)
    ax.fill_betweenx(t_edge, 1, 1 + scale * sq_torsion_edge, color=BLUE, alpha=0.22)

    # Mark alternating corner charges (+1, -1, +1, -1)
    for (vx, vy), sgn, col in [((0, 0), "+1", CORAL), ((1, 0), "−1", PURPLE),
                                ((1, 1), "+1", CORAL), ((0, 1), "−1", PURPLE)]:
        ax.scatter([vx], [vy], color=col, edgecolor="white", s=100, zorder=6)
        dx = -0.10 if vx == 0 else 0.10
        dy = -0.10 if vy == 0 else 0.10
        ax.text(vx + dx, vy + dy, sgn, ha="center", va="center", fontsize=9.5,
                fontweight="bold", color=col)

    ax.text(0.5, 0.5, "Uniform 2D\nInterior Charge\n($-\\Delta u = 1$)\nBalayage = Torsion\n(100% Invisible!)",
            ha="center", va="center", fontsize=8.8, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white", alpha=0.88, edgecolor=NAVY))
    ax.set_xlim(-0.32, 1.32)
    ax.set_ylim(-0.32, 1.32)
    ax.set_aspect("equal")
    ax.set_title("A. Unit Square: 3 Smooth Invisible Loads ($n_x, n_y$, Torsion) + 1 Corner Ghost")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    # --- Panel B: Equilateral Triangle Y-Shaped Zeta Skeleton ---
    ax = axes[0, 1]
    H0 = np.sqrt(3) / 2
    v_tri = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, H0]])
    ctr = v_tri.mean(axis=0)
    ax.add_patch(patches.Polygon(v_tri, closed=True, facecolor="#ecfeff", edgecolor=NAVY, lw=2.2))

    # Plot the 3-spoked Y-shaped median skeleton colored by radial density h(r)
    mp.mp.dps = 30
    coeff = skeleton_coefficients(90)
    R = 1.0 / np.sqrt(3)
    rs = np.linspace(1e-4, R, 120)
    hs = np.array([float(mp.sqrt(r) * mp.polyval(coeff[::-1], mp.mpf(r) ** 3)) for r in rs])
    cmap = plt.get_cmap("plasma")
    norm = plt.Normalize(0, hs.max())
    for k in range(3):
        u_vec = (ctr - v_tri[k]) / R
        pts = v_tri[k][None, :] + rs[:, None] * u_vec[None, :]
        for i in range(len(rs) - 1):
            ax.plot(pts[i:i+2, 0], pts[i:i+2, 1], color=cmap(norm(hs[i])), lw=5.5, solid_capstyle="round", zorder=4)
    ax.scatter([ctr[0]], [ctr[1]], color="#facc15", edgecolor=NAVY, s=90, zorder=6)

    # Draw outward boundary shadow g_triangle on all 3 edges
    scale_t = 0.42
    for j in range(3):
        p0, p1 = v_tri[j], v_tri[(j + 1) % 3]
        e = p1 - p0
        n_out = np.array([e[1], -e[0]]) / np.linalg.norm(e)
        base_pts = p0[None, :] + x_tri[:, None] * e[None, :]
        outer_pts = base_pts + (scale_t * g_L2)[:, None] * n_out[None, :]
        ax.plot(outer_pts[:, 0], outer_pts[:, 1], color=TEAL, lw=2.2)
        poly_fill = np.vstack([base_pts, outer_pts[::-1]])
        ax.add_patch(patches.Polygon(poly_fill, closed=True, facecolor=TEAL, alpha=0.22, edgecolor="none"))

    ax.annotate(
        "Y-Shaped Median Skeleton\n"
        r"$h(r)=\sqrt{r}\sum a_j r^{3j}$" + "\n"
        r"(Binet kernel: $\zeta(4),\zeta(10),\zeta(16),\dots$)" + "\n"
        "Poisson shadow = unique $L^2$ ghost!",
        xy=(ctr[0] + 0.04, ctr[1] + 0.03), xytext=(0.50, 1.07), ha="center",
        fontsize=8.2, fontweight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.30", facecolor="white", edgecolor=PURPLE, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.4, connectionstyle="arc3,rad=-0.22"),
    )
    ax.scatter(v_tri[:, 0], v_tri[:, 1], color=NAVY, s=55, zorder=6)
    ax.set_xlim(-0.32, 1.32)
    ax.set_ylim(-0.30, 1.38)
    ax.set_aspect("equal")
    ax.set_title(r"B. Equilateral Triangle: Unique Invisible $L^2$ Flux $g_\triangle$ from Y-Skeleton")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    # --- Panel C: Direct Edge Profile Comparison (Square torsion vs Triangle torsion vs g_triangle vs L1\L2 siblings) ---
    ax = axes[1, 0]
    # Equilateral triangle Saint-Venant torsion flux: u = l1*l2*l3 / H0, on base y=0:
    # l1 = y, l2 = (sqrt(3)/2)*(1-x) - y/2, l3 = (sqrt(3)/2)*x - y/2 -> -du/dn = du/dy|_{y=0} = l2*l3/H0 = (sqrt(3)/2)*x*(1-x)
    # Normalize to total mass 1 over 3 sides: integral over 1 side is (sqrt(3)/2)*(1/6) = sqrt(3)/12; 3 sides = sqrt(3)/4 -> multiply by 4/sqrt(3) -> 2*x*(1-x)
    tri_torsion_norm = 2.0 * x_tri * (1.0 - x_tri)  # total mass over 3 sides = 3 * (2/6) = 1
    # Square torsion already has total mass = area = 1 over 4 sides (0.25 per side) -> scale by 4/3 to compare per-edge mass 1/3? No, plot exact mass-1 densities!
    ax.plot(x_tri, g_L2, color=TEAL, lw=2.8, label=r"Triangle unique invisible $L^2$ flux $g_\triangle$ ($\sim\sqrt{2/\pi}\,x^{1/2}$)")
    ax.plot(x_tri[::18], proj_768[::18], "o", color=NAVY, ms=4.0, alpha=0.85, label="Independent 768-harmonic projection check")
    ax.plot(x_tri, tri_torsion_norm, "--", color=AMBER, lw=2.1, label=r"Triangle torsion $2x(1-x)$ (NOT invisible: fails at $m=1$!)")
    ax.plot(t_edge, sq_torsion_edge, ":", color=BLUE, lw=2.3, label=r"Square torsion $-\partial_n u$ (invisible on square)")
    # Clip L1\L2 sibling for display
    sib_clip = np.clip(g_s0, -1.5, 1.5)
    ax.plot(x_tri, sib_clip, "-.", color=CORAL, lw=1.6, alpha=0.85, label=r"Triangle $L^1\setminus L^2$ sibling ($\sim \pm x^{-1/2}$ blowup at corners!)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_title("C. Boundary Flux Profiles Along One Unit Edge ($x \\in [0,1]$)")
    ax.set_xlabel("Arclength $x$ along edge")
    ax.set_ylabel("Boundary flux density (mass-1 normalized)")
    ax.legend(loc="lower center", fontsize=7.9, ncol=1)
    ax.grid(True)

    # --- Panel D: Two-Sided Symmetry-Breaking Collapse ---
    ax = axes[1, 1]
    eps = np.array(data["tilt"]["epsilon"])
    sig = np.array(data["tilt"]["singular_values"])
    mask = eps > 0
    colors_sv = [NAVY, BLUE, TEAL, CORAL]
    labels_sv = [
        r"$\sigma_1$ (slope $= 169.53$)",
        r"$\sigma_2$ (slope $= 6.93$)",
        r"$\sigma_3$ (slope $= 6.93$)",
        r"$\sigma_4$ (smallest; slope $= 0.549$)",
    ]
    for k in range(4):
        ls = "--" if k == 2 else "-"
        lw = 2.4 if k in (0, 3) else 2.0
        ax.loglog(eps[mask], sig[mask, k], ls, color=colors_sv[k], lw=lw, label=labels_sv[k])

    # Reference O(eps) line
    e_ref = np.array([1e-7, 1e-2])
    ax.loglog(e_ref, 0.25 * e_ref, ":", color=SLATE, lw=1.4, label=r"Linear scaling $O(\varepsilon)$")
    ax.annotate(
        r"At $\varepsilon=0$ (exact square): all 4 $\sigma_k = 0$" + "\n"
        r"Tilt ONE corner by $\varepsilon>0$ →" + "\n"
        "ALL 4 two-sided ghosts collapse to 0-dim!",
        xy=(1e-6, sig[mask, 3][3]), xytext=(3e-6, 1.5e-1),
        fontsize=8.3, fontweight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.3),
    )
    ax.set_title(r"D. Two-Sided Lattice $\Lambda_\pm$: Symmetry-Breaking Collapse")
    ax.set_xlabel(r"Vertex tilt angle $\varepsilon$ (radians)")
    ax.set_ylabel("Singular values of the 4 square invisible modes")
    ax.legend(loc="lower right", fontsize=8.1)
    ax.grid(True, which="both", alpha=0.45)

    plt.tight_layout(rect=[0, 0, 1, 0.955])
    out = FIGS / "fig2_invisible_loads_square_vs_triangle.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print("Saved", out)


def make_fig3():
    data = json.loads((EXP / "phase3_data.json").read_text())
    fig, axes = plt.subplots(1, 3, figsize=(16.8, 5.4), dpi=220)
    fig.suptitle(
        "Figure 3. Two-Slope 60°/120° Rhombus, The Half-Step Paradox, and Odd-Polygon Minimax Optimality",
        fontsize=13.5, fontweight="bold", color=NAVY, y=0.99,
    )

    # --- Panel A: Two-Slope 60/120 Rhombus vs Odd Triangle ---
    ax = axes[0]
    N_rh = np.array(data["rhombus"]["N"], dtype=float)
    risks_rh = np.array([[float(x) for x in row] for row in data["rhombus"]["risks"]])
    # Scalene triangle exact minimax risk at vertex 0 from Phase 2
    N_tri = np.array([4, 12, 32, 64], dtype=float)
    risk_tri = np.array([0.680890276, 0.673370022, 0.665515923, 0.660464909]) / np.sqrt(N_tri)

    ax.loglog(N_tri, risk_tri, "s-", color=SLATE, lw=2.1, ms=5.5,
              label=r"Odd scalene triangle (unbeatable $N^{-1/2}$)")
    ax.loglog(N_rh, risks_rh[:, 1], "o-", color=CORAL, lw=2.3, ms=6,
              label=r"Rhombus blunt $120^\circ$ corner ($N^{-2/3}$, fit $0.653$)")
    ax.loglog(N_rh, risks_rh[:, 3], "o--", color="#fb7185", lw=1.8, ms=5,
              label=r"Rhombus blunt $120^\circ$ opp. ($N^{-2/3}$, fit $0.671$)")
    ax.loglog(N_rh, risks_rh[:, 0], "^-", color=TEAL, lw=2.4, ms=6.5,
              label=r"Rhombus sharp $60^\circ$ corner ($N^{-5/6}$, fit $0.843$)")
    ax.loglog(N_rh, risks_rh[:, 2], "^--", color="#2dd4bf", lw=1.8, ms=5.5,
              label=r"Rhombus sharp $60^\circ$ opp. ($N^{-5/6}$, fit $0.849$)")

    # Reference slope lines
    nr = np.array([3.0, 22.0])
    ax.loglog(nr, 0.72 * nr ** (-0.5), ":", color=SLATE, lw=1.3)
    ax.loglog(nr, 0.56 * nr ** (-2 / 3), ":", color=CORAL, lw=1.3)
    ax.loglog(nr, 0.52 * nr ** (-5 / 6), ":", color=TEAL, lw=1.3)

    # Inset diamond diagram
    inset = ax.inset_axes([0.05, 0.06, 0.35, 0.30])
    u = np.array([0.5, np.sqrt(3) / 2])
    rv = np.array([[0.0, 0.0], [1.0, 0.0], np.array([1.0, 0.0]) + u, u])
    inset.add_patch(patches.Polygon(rv, closed=True, facecolor="#f0fdfa", edgecolor=NAVY, lw=1.6))
    inset.plot([0, 1], [0, 0], color=AMBER, lw=3.0)
    inset.scatter([0, 1.0 + u[0]], [0, u[1]], color=TEAL, s=36, zorder=5)
    inset.scatter([1, u[0]], [0, u[1]], color=CORAL, s=36, zorder=5)
    inset.text(0.14, 0.14, "60°", fontsize=7.5, color=TEAL, fontweight="bold")
    inset.text(0.73, 0.14, "120°", fontsize=7.5, color=CORAL, fontweight="bold")
    inset.text(0.5, -0.22, "shifted edge", ha="center", fontsize=7.0, color=AMBER, fontweight="bold")
    inset.set_xlim(-0.18, 1.68)
    inset.set_ylim(-0.34, 1.04)
    inset.set_aspect("equal")
    inset.axis("off")

    ax.set_title(r"A. Angle-Dependent Exponent $N^{-(1-\omega_k/2\pi)}$")
    ax.set_xlabel("Band cutoff $N$ (frequencies per side)")
    ax.set_ylabel("Exact minimax corner risk $E_k / M$")
    ax.legend(loc="upper right", fontsize=7.4)
    ax.grid(True, which="both", alpha=0.45)

    # --- Panel B: Square Shift-Optimality Paradox (Interval-Certified) ---
    ax = axes[1]
    theta = np.array(data["square"]["theta"])
    sq_colors = {1: CORAL, 2: BLUE, 4: TEAL}
    for idx, N_val in enumerate(data["square"]["N"]):
        risks_mat = np.array([[float(x) for x in row] for row in data["square"]["risks"][idx]])
        emax = risks_mat.max(axis=1)
        col = sq_colors[N_val]
        ax.plot(theta, emax, "-", color=col, lw=2.3, label=f"$N = {N_val}$")
        # Mark half-step
        half_val = max(float(x) for x in data["square"]["optima"][idx]["half_step_risks"])
        ax.scatter([0.5], [half_val], color=col, marker="x", s=70, lw=2.0, zorder=6)
        # Mark global optimum
        opt = data["square"]["optima"][idx]
        opt_t = float(opt["shift_bracket"][0])
        opt_r = float(opt["risk_bracket"][0])
        ax.scatter([opt_t], [opt_r], color="#fbbf24", edgecolor=NAVY, marker="*", s=130, zorder=7)

    ax.axvline(0.5, color=SLATE, ls="--", lw=1.2, alpha=0.8)
    ax.text(0.515, 1.12, r"Intuitive half-step $\theta=\frac{1}{2}$" + "\n(NEVER optimal!)",
            fontsize=8.2, color=NAVY, fontweight="bold")
    ax.annotate(r"$N=1$: inf as $\theta \uparrow 1$ (0.6099 vs 0.6613)",
                xy=(0.99, 0.610), xytext=(0.43, 0.80), fontsize=7.8, color=CORAL, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.annotate(r"$N=2$: inf as $\theta \downarrow 0$ (0.3735 vs 0.4046)",
                xy=(0.01, 0.374), xytext=(0.14, 0.49), fontsize=7.8, color=BLUE, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.annotate(r"$N=4$: unique $\theta^*\!\approx\!0.1133$ (0.2422)",
                xy=(0.1133, 0.2422), xytext=(0.24, 0.16), fontsize=7.8, color=TEAL, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2))

    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(0.12, 1.28)
    ax.set_title(r"B. The Half-Step Myth on the Square (Certified over $0<\theta<1$)")
    ax.set_xlabel(r"Fractional frequency shift $\theta$ on one edge")
    ax.set_ylabel(r"Exact minimax vector risk $E_\infty(N, \theta) / M$")
    ax.legend(loc="upper right", fontsize=8.5)
    ax.grid(True)

    # --- Panel C: Odd-Polygon Sharp Constant & Continuum Dyadic Convergence ---
    ax = axes[2]
    N_sc = np.array([4, 12, 32, 64])
    opt_sc = np.array([0.680890, 0.673370, 0.665516, 0.660465])
    ces_sc = np.array([0.762911, 0.791685, 0.806492, 0.812491])
    dyadic_bins = np.array([1, 2, 4, 8, 16, 32, 64])
    dyadic_ub = np.array([0.702161, 0.676476, 0.664559, 0.657443, 0.652608, 0.649038, 0.646252])

    ax.plot(N_sc, ces_sc, "s-", color=CORAL, lw=2.2, ms=6, label=r"Calibrated Cesàro $\sqrt{N} E_{\rm Ces}/M$")
    ax.axhline(0.821058, color=CORAL, ls=":", lw=1.5, label=r"Cesàro continuum limit $\|T^*c\| = 0.8211$")
    ax.plot(N_sc, opt_sc, "o-", color=BLUE, lw=2.3, ms=6, label=r"Exact finite minimax $\sqrt{N} E_0/M$")
    ax.plot(dyadic_bins, dyadic_ub, "^--", color=TEAL, lw=2.0, ms=5.5,
            label=r"Continuum dyadic upper bound $\downarrow \|\Pi T^*c\|$")

    ax.annotate("Cesàro is strictly\n>27% suboptimal!",
                xy=(50, 0.73), xytext=(14, 0.725), fontsize=8.4, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.95))
    ax.annotate("", xy=(58, 0.818), xytext=(58, 0.648),
                arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.6))

    ax.set_title("C. Scalene Triangle: Sharp Minimax Constant $C_0$")
    ax.set_xlabel("Band cutoff $N$ (or continuum dyadic bins)")
    ax.set_ylabel(r"Scaled risk $\sqrt{N} E_0 / M$")
    ax.set_ylim(0.55, 0.855)
    ax.legend(loc="lower center", fontsize=7.6)
    ax.grid(True)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    out = FIGS / "fig3_rhombus_two_slopes_and_shift_paradox.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print("Saved", out)


def make_fig4():
    fig, axes = plt.subplots(1, 3, figsize=(16.8, 5.3), dpi=220)
    fig.suptitle(
        "Figure 4. 24-Order Corner Super-Resolution, Fokas PDE Blind-Spot Removal, and Discontinuous Metal Plates",
        fontsize=13.2, fontweight="bold", color=NAVY, y=0.99,
    )

    # --- Panel A: Smooth-Background Super-Resolution (verified 80-digit Phase 2 outputs) ---
    ax = axes[0]
    N_sr = np.array([32, 64, 128])
    ces_tri = np.array([5.759e-2, 3.373e-2, 1.935e-2])
    ces_sq = np.array([7.409e-2, 4.319e-2, 2.469e-2])
    r3_tri = np.array([4.501e-9, 2.784e-10, 1.734e-11])
    r3_sq = np.array([1.076e-8, 6.807e-10, 4.281e-11])
    ext_tri = np.array([1.453e-11, 3.961e-23, 6.049e-26])
    ext_sq = np.array([2.454e-11, 5.597e-23, 8.304e-26])

    ax.loglog(N_sr, ces_sq, "o-", color=CORAL, lw=2.1, ms=6, label="Calibrated Cesàro (square)")
    ax.loglog(N_sr, ces_tri, "o--", color="#fb7185", lw=1.8, ms=5.5, label="Calibrated Cesàro (triangle)")
    ax.loglog(N_sr, r3_sq, "s-", color=BLUE, lw=2.1, ms=6, label=r"$r=3$ inverse-power window (square, $O(N^{-4})$)")
    ax.loglog(N_sr, r3_tri, "s--", color="#60a5fa", lw=1.8, ms=5.5, label=r"$r=3$ window (triangle)")
    ax.loglog(N_sr, ext_sq, "^-", color=TEAL, lw=2.4, ms=6.5, label="Extrapolation window (square, exp. decay)")
    ax.loglog(N_sr, ext_tri, "^--", color="#2dd4bf", lw=1.9, ms=5.5, label="Extrapolation window (triangle)")

    ax.annotate(
        "24 orders of magnitude gain!\n"
        r"($2.5\times10^{-2} \to 6.0\times10^{-26}$)" + "\n"
        r"Trade-off: $\|w\|_1 \geq |T_r(\frac{a+b}{b-a})|$",
        xy=(128, 6.05e-26), xytext=(56, 3e-18),
        fontsize=8.0, fontweight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#ecfdf5", edgecolor=TEAL, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.3),
    )
    ax.set_xticks(N_sr)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax.set_title("A. Smooth-Background Corner Super-Resolution")
    ax.set_xlabel("Band cutoff $N$")
    ax.set_ylabel("Max vertex recovery error (80-digit mpmath)")
    ax.set_ylim(1e-29, 1e0)
    ax.legend(loc="lower left", fontsize=7.2)
    ax.grid(True, which="both", alpha=0.45)

    # --- Panel B: Fokas PDE Solver Blind-Spot Removal (compute exact SVD live for accuracy!) ---
    ax = axes[1]
    from phase2_theorems import edges as poly_edges, GammaSymbol, unit_moment
    import scipy.linalg as la

    def fokas_svd_pair(verts):
        """Reproduce the enriched affine+invisible Fokas matrix SVD before & after moment completion."""
        p = len(verts)
        dirs = poly_edges(verts)
        k = p // 2
        n_freq = 5
        # Build 2 affine basis functions per edge (1 and t on [0,1]) + 1 invisible mass-1 column (exact transform L(s))
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
                row_c.extend([m0, m1])
            row_c.append(sym(s) * mp.exp(-s * anchor))
            rows_raw.append([float(z.real) for z in row_c])
            rows_raw.append([float(z.imag) for z in row_c])
        M_before = np.array(rows_raw, dtype=float)
        # Moment completion rows: mass (deg 0) + complex moments deg 1..k-1
        rows_mom = []
        # deg 0 (mass)
        r0 = []
        for j, d in enumerate(dirs):
            r0.extend([float(abs(d)), float(abs(d)) / 2.0])
        r0.append(1.0)  # L(0) = 1
        rows_mom.append(r0)
        for deg in range(1, k):
            rc = []
            for j, d in enumerate(dirs):
                # int_0^1 (v0 + d t)^deg * |d| dt and * t dt
                v0 = complex(verts[j])
                dc = complex(d)
                q, wt = special.roots_legendre(12)
                tt = (q + 1) / 2
                ww = wt / 2
                vals = (v0 + dc * tt) ** deg
                rc.append(abs(dc) * np.sum(ww * vals))
                rc.append(abs(dc) * np.sum(ww * tt * vals))
            # deg-th derivative of L at 0
            L_deg = complex(mp.diff(sym, 0, deg))
            rc.append(L_deg)
            rows_mom.append([z.real for z in rc])
            rows_mom.append([z.imag for z in rc])
        M_after = np.vstack([M_before, np.array(rows_mom, dtype=float)])
        sv_b = la.svdvals(M_before)
        sv_a = la.svdvals(M_after)
        return np.maximum(sv_b, 1e-17), sv_a

    with mp.workdps(40):
        sq_v = (mp.mpc(0), mp.mpc(1), mp.mpc(1, 1), mp.mpc(0, 1))
        tr_v = (mp.mpc(0), mp.mpc(1), mp.mpc("0.5", mp.sqrt(3) / 2))
        sv_sq_b, sv_sq_a = fokas_svd_pair(sq_v)
        sv_tr_b, sv_tr_a = fokas_svd_pair(tr_v)

    idx_sq = np.arange(1, len(sv_sq_b) + 1)
    idx_tr = np.arange(1, len(sv_tr_b) + 1)
    ax.semilogy(idx_sq, sv_sq_b, "o--", color=CORAL, lw=2.0, ms=6.5, label="Square BEFORE completion (3 zero modes!)")
    ax.semilogy(idx_sq, sv_sq_a, "o-", color=BLUE, lw=2.3, ms=6.5, label=r"Square AFTER $2k\!-\!1=3$ moments ($\kappa=16.5$)")
    ax.semilogy(idx_tr, sv_tr_b, "s--", color=AMBER, lw=2.0, ms=6, label="Triangle BEFORE completion (1 zero mode!)")
    ax.semilogy(idx_tr, sv_tr_a, "s-", color=TEAL, lw=2.3, ms=6, label=r"Triangle AFTER $2k\!-\!1=1$ moment ($\kappa=12.2$)")

    ax.annotate("Exact blind spot:\n3 singular values = 0\n($n_x, n_y$, torsion)",
                xy=(8.0, 1e-16), xytext=(3.6, 1e-12), fontsize=8.0, fontweight="bold", color=CORAL,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff1f2", edgecolor=CORAL, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2))
    ax.annotate("Field error:\nSquare: 3.9×10⁻¹⁶\nTriangle: 2.4×10⁻¹⁵",
                xy=(9, sv_sq_a[-1]), xytext=(4.6, 5e-5), fontsize=8.0, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#eff6ff", edgecolor=BLUE, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    ax.set_title("B. Fokas Global Relation: Exact Blind Spot Removed")
    ax.set_xlabel("Singular value index (sorted descending)")
    ax.set_ylabel("Singular value magnitude")
    ax.set_xticks(range(1, 10))
    ax.set_ylim(1e-18, 1e2)
    ax.legend(loc="lower left", fontsize=7.2)
    ax.grid(True, which="both", alpha=0.45)

    # --- Panel C: Heated Polygonal Metal Plates with Discontinuous Wall Temperatures ---
    ax = axes[2]
    # Solve harmonic field on unit square with wall temps T=(1, 4, -2, 5) via exact conformal/Fourier series!
    # For unit square [0,1]^2: bottom=1, right=4, top=-2, left=5
    gx = np.linspace(0.005, 0.995, 110)
    gy = np.linspace(0.005, 0.995, 110)
    XX, YY = np.meshgrid(gx, gy)

    def side_harmonic(X, Y, T_val, n_max=55):
        """Harmonic on [0,1]^2 equal to T_val on bottom edge y=0 and 0 on other 3 edges."""
        u = np.zeros_like(X)
        for n in range(1, n_max, 2):
            k = n * np.pi
            u += (4.0 * T_val / k) * np.sin(k * X) * np.sinh(k * (1.0 - Y)) / np.sinh(k)
        return u

    Q_sq = (
        side_harmonic(XX, YY, 1.0)
        + side_harmonic(YY, 1.0 - XX, 4.0)
        + side_harmonic(XX, 1.0 - YY, -2.0)
        + side_harmonic(YY, XX, 5.0)
    )
    im = ax.contourf(XX, YY, Q_sq, levels=24, cmap="coolwarm", vmin=-2.2, vmax=5.2)
    ax.contour(XX, YY, Q_sq, levels=12, colors="white", linewidths=0.5, alpha=0.5)
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False, edgecolor=NAVY, lw=2.2))

    # Label wall temperatures and corner jumps a_j = T_j - T_{j-1}
    ax.text(0.5, -0.09, r"$T_1 = 1$", ha="center", va="top", fontsize=9.2, fontweight="bold", color=NAVY)
    ax.text(1.07, 0.5, r"$T_2 = 4$", ha="left", va="center", fontsize=9.2, fontweight="bold", color=CORAL)
    ax.text(0.5, 1.07, r"$T_3 = -2$", ha="center", va="bottom", fontsize=9.2, fontweight="bold", color=BLUE)
    ax.text(-0.07, 0.5, r"$T_4 = 5$", ha="right", va="center", fontsize=9.2, fontweight="bold", color=CORAL)

    jumps = [((0, 0), r"$a_1=-4$", -0.14, -0.11),
             ((1, 0), r"$a_2=+3$", 1.15, -0.11),
             ((1, 1), r"$a_3=-6$", 1.15, 1.10),
             ((0, 1), r"$a_4=+7$", -0.14, 1.10)]
    for (vx, vy), txt, tx, ty in jumps:
        ax.scatter([vx], [vy], color="#fbbf24", edgecolor=NAVY, s=65, zorder=6)
        ax.text(tx, ty, txt, ha="center", va="center", fontsize=8.0, fontweight="bold", color=NAVY,
                bbox=dict(boxstyle="round,pad=0.18", facecolor="#fef3c7", edgecolor=AMBER, alpha=0.92))

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    cbar.set_label("Temperature $q(x,y)$", fontsize=8.8)
    ax.set_xlim(-0.34, 1.36)
    ax.set_ylim(-0.24, 1.24)
    ax.set_aspect("equal")
    ax.set_title(r"C. Heated Plate: $B_{\mathrm{fp}\,q_n}(s)=i\sum a_j e^{s\gamma_j}$ ($7.1\times10^{-14}$)")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.grid(False)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    out = FIGS / "fig4_super_resolution_and_fokas_pde.png"
    fig.savefig(out, dpi=220)
    plt.close(fig)
    print("Saved", out)


if __name__ == "__main__":
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    print("All 4 multi-panel figures generated successfully!")
