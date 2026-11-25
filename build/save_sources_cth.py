#!/usr/bin/env python3
"""Save Concrete, Tools, and House cited sources as PDFs, reusing save_sources.py."""

from __future__ import annotations

import shutil
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import save_sources as ss

ROOT = ss.ROOT
OUT_ROOT = ss.OUT_ROOT

# USGS HTML pages previously timed out; keep Chrome short, curl still has full time.
for host in ("usgs.gov", "pubs.usgs.gov"):
    if host not in ss.SHORT_TIMEOUT_HOSTS:
        ss.SHORT_TIMEOUT_HOSTS = tuple(ss.SHORT_TIMEOUT_HOSTS) + (host,)


def looks_like_webpage(url: str) -> bool:
    p = urlparse(url)
    path = (p.path or "").lower()
    query = (p.query or "").lower()
    if path.endswith(".pdf") or "download" in query or "download" in path:
        return False
    if "viewcontent.cgi" in path or "download_attachment" in query:
        return False
    if path.endswith((".html", ".htm", ".php", ".asp", ".aspx", ".cfm", ".shtml", ".jsp")):
        return True
    last = path.rsplit("/", 1)[-1]
    if not last or "." not in last:
        return True
    return False


_orig_save_one = ss.save_one


def save_one(url: str, dest: Path) -> tuple[bool, str]:
    """Same as ss.save_one, but try curl first when a URL may be a direct PDF without a .pdf suffix."""
    if not ss.is_pdf_url(url) and not looks_like_webpage(url):
        ok, reason = ss.curl_download(url, dest)
        if ok:
            problem = ss.looks_like_block_page(ss.pdf_text(dest), dest)
            if problem:
                dest.unlink(missing_ok=True)
            else:
                return True, reason + " (direct download, URL has no .pdf suffix)"
        # fall through to the standard HTML/PDF path
    return _orig_save_one(url, dest)


# Patch the shared process_list to use the enhanced saver.
ss.save_one = save_one


def seed_cache(cache: dict[str, Path]) -> None:
    """Reuse already-saved PDFs from Water, Food, and Electricity when the URL matches."""
    for list_name, folder_name in (
        ("sources-water.txt", "Water"),
        ("sources-food.txt", "Food"),
        ("sources-electricity.txt", "Electricity"),
    ):
        list_path = ROOT / list_name
        folder = OUT_ROOT / folder_name
        if not list_path.exists() or not folder.exists():
            continue
        for url, title in ss.parse_sources(list_path):
            dest = folder / ss.slug_from_title(title)
            if url not in cache and ss.already_ok(dest):
                cache[url] = dest
    print(f"Seeded cache with {len(cache)} already-saved URLs", flush=True)


def main() -> int:
    if not ss.CHS.exists():
        print("chrome-headless-shell not found at", ss.CHS, file=sys.stderr)
        return 1
    ss.PROFILE.mkdir(parents=True, exist_ok=True)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    cache: dict[str, Path] = {}
    seed_cache(cache)

    total_saved = total_failed = 0
    all_fails: list[str] = []
    jobs = [
        (ROOT / "sources-concrete.txt", "Concrete"),
        (ROOT / "sources-tools.txt", "Tools"),
        (ROOT / "sources-house.txt", "House"),
    ]
    for path, name in jobs:
        if not path.exists():
            print(f"MISSING source list: {path}", flush=True)
            continue
        s, f, notes = ss.process_list(path, name, cache)
        total_saved += s
        total_failed += f
        all_fails.extend(notes)

    print("\n=== SUMMARY ===", flush=True)
    print(f"saved={total_saved} failed={total_failed}", flush=True)
    for n in all_fails:
        print("FAIL:", n, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
