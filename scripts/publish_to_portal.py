#!/usr/bin/env python3
"""
Sync a study's compiled PDFs and dedicated publication figures from
  remath/studies/<slug>/papers/
into the sibling GitHub Pages portal repository:
  ../rkka02.github.io/content/studies/<slug>/assets/{pdfs,figs}/

Usage:
  python3 scripts/publish_to_portal.py 01-leontiev-invisible-loads
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT.parent / "rkka02.github.io"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/publish_to_portal.py <study_slug>")
        sys.exit(1)

    slug = sys.argv[1].strip().strip("/")
    study_dir = ROOT / "studies" / slug
    if not study_dir.exists():
        print(f"Error: study not found: {study_dir}")
        sys.exit(1)
    if not PORTAL.exists():
        print(f"Error: sibling portal repo not found at {PORTAL}")
        sys.exit(1)

    portal_study = PORTAL / "content" / "studies" / slug
    if not (portal_study / "study.json").exists():
        print(f"Scaffolding portal metadata via {PORTAL / 'scripts' / 'new_study.py'} ...")
        subprocess.run(
            [sys.executable, str(PORTAL / "scripts" / "new_study.py"), slug],
            check=True,
        )

    dst_pdfs = portal_study / "assets" / "pdfs"
    dst_figs = portal_study / "assets" / "figs"
    dst_pdfs.mkdir(parents=True, exist_ok=True)
    dst_figs.mkdir(parents=True, exist_ok=True)

    papers_dir = study_dir / "papers"
    pdf_count = 0
    fig_count = 0
    if papers_dir.exists():
        for pdf in sorted(papers_dir.glob("*/*.pdf")):
            shutil.copy2(pdf, dst_pdfs / pdf.name)
            pdf_count += 1
        for fig in sorted(papers_dir.glob("*/figs/*.png")):
            shutil.copy2(fig, dst_figs / fig.name)
            fig_count += 1

    print(f"Synced {pdf_count} PDF(s) and {fig_count} figure(s) -> {portal_study / 'assets'}")
    subprocess.run([sys.executable, str(PORTAL / "scripts" / "build_site.py")], check=True)
    print(f"Rebuilt portal preview in {PORTAL / 'dist'}")
    print("Review content/studies/<slug>/study.json in ../rkka02.github.io, then commit & push to deploy.")


if __name__ == "__main__":
    main()
