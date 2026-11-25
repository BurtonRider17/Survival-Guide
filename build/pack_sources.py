#!/usr/bin/env python3
"""Pack a Survival Info Sources subfolder into zip(s) under 23 MB each."""

from __future__ import annotations

import sys
import zipfile
import zlib
from pathlib import Path

ROOT = Path("/workspace/survival-info")
OUT_ROOT = ROOT / "Survival Info Sources"
LIMIT = 23 * 1024 * 1024  # 23 MB
ARC_PREFIX = "Survival Info Sources"


def est_zip_entry_size(path: Path, arcname: str) -> int:
    data = path.read_bytes()
    raw = len(data)
    # ZIP uses raw DEFLATE (wbits=-15)
    co = zlib.compressobj(9, zlib.DEFLATED, -15)
    comp = co.compress(data) + co.flush()
    used = min(len(comp), raw)
    name_len = len(arcname.encode("utf-8"))
    # local header 30 + name + data; central 46 + name; EOCD shared later
    return used + 30 + 46 + 2 * name_len


def pack_folder(folder_name: str) -> list[Path]:
    folder = OUT_ROOT / folder_name
    if not folder.is_dir():
        raise SystemExit(f"missing folder: {folder}")
    files = [p for p in folder.rglob("*") if p.is_file() and not p.name.endswith(".part") and not p.name.endswith(".part.pdf")]
    # PDFs largest-first, then the failure list last into part 1 or the last bin with room
    pdfs = [p for p in files if p.suffix.lower() == ".pdf"]
    extras = [p for p in files if p not in pdfs]
    pdfs.sort(key=lambda p: p.stat().st_size, reverse=True)

    def arcname(p: Path) -> str:
        return f"{ARC_PREFIX}/{folder_name}/{p.relative_to(folder).as_posix()}"

    # First-fit decreasing using estimated compressed size
    bins: list[list[Path]] = []
    bin_sizes: list[int] = []
    eocd = 22
    for p in pdfs:
        need = est_zip_entry_size(p, arcname(p))
        placed = False
        for i, sz in enumerate(bin_sizes):
            if sz + need + eocd <= LIMIT:
                bins[i].append(p)
                bin_sizes[i] += need
                placed = True
                break
        if not placed:
            # A single file over the limit still gets its own zip
            bins.append([p])
            bin_sizes.append(need)
    # Put extras (failure list) in the last bin if it fits, else last bin anyway (tiny)
    if extras:
        if not bins:
            bins.append([])
            bin_sizes.append(0)
        for p in extras:
            need = est_zip_entry_size(p, arcname(p))
            if bin_sizes[-1] + need + eocd <= LIMIT:
                bins[-1].append(p)
                bin_sizes[-1] += need
            else:
                bins[0].append(p)
                bin_sizes[0] += need

    stem = f"Sources_{folder_name}"
    # Remove previous zips for this guide so we don't leave stale parts
    for old in list(ROOT.glob(f"{stem}.zip")) + list(ROOT.glob(f"{stem}_part*.zip")):
        old.unlink()

    written: list[Path] = []
    multi = len(bins) > 1
    for i, group in enumerate(bins, 1):
        name = f"{stem}_part{i}.zip" if multi else f"{stem}.zip"
        dest = ROOT / name
        with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for p in group:
                zf.write(p, arcname=arcname(p))
        written.append(dest)
        print(f"  wrote {dest.name}  {dest.stat().st_size} bytes  ({len(group)} files)", flush=True)
        if dest.stat().st_size > LIMIT:
            print(f"  WARNING: {dest.name} exceeds 23 MB ({dest.stat().st_size} bytes)", flush=True)
    return written


def main() -> int:
    names = sys.argv[1:] or ["Concrete", "Tools", "House"]
    all_written: list[Path] = []
    for name in names:
        print(f"\n=== Packing {name} ===", flush=True)
        all_written.extend(pack_folder(name))
    print("\n=== ZIP SUMMARY ===", flush=True)
    for p in all_written:
        print(f"{p}  {p.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
