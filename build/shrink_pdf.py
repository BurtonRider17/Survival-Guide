#!/usr/bin/env python3
"""Downsample PDF images to ~150 dpi JPEG so a file fits under ~22 MiB."""

from __future__ import annotations

import io
import sys
from pathlib import Path

import pymupdf
from PIL import Image

TARGET_DPI = 150
QUALITY = 80
AIM = 22 * 1024 * 1024


def _collect(doc: pymupdf.Document) -> dict[int, dict]:
    info: dict[int, dict] = {}
    for pi in range(doc.page_count):
        page = doc[pi]
        try:
            images = page.get_images(full=True)
        except Exception:
            continue
        for img in images:
            xref, smask, w, h, bpc = img[0], img[1], img[2], img[3], img[4]
            try:
                rects = page.get_image_rects(xref)
            except Exception:
                rects = []
            max_w = max((r.width for r in rects if r.width > 0), default=0.0)
            max_h = max((r.height for r in rects if r.height > 0), default=0.0)
            if xref not in info:
                info[xref] = dict(page=pi, w=w, h=h, bpc=bpc, smask=smask, max_w=max_w, max_h=max_h)
            else:
                rec = info[xref]
                rec["max_w"] = max(rec["max_w"], max_w)
                rec["max_h"] = max(rec["max_h"], max_h)
    return info


def _to_pil(pix: pymupdf.Pixmap) -> Image.Image:
    if pix.colorspace is not None and pix.n - pix.alpha == 4:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    im = pix.pil_image()
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    if im.mode == "P":
        if "transparency" in im.info:
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            return bg
        return im.convert("RGB")
    if im.mode not in ("RGB", "L"):
        return im.convert("RGB")
    return im


def shrink_pdf(src: Path, dest: Path | None = None, aim: int = AIM, quality: int = QUALITY, dpi: int = TARGET_DPI) -> Path:
    """Rewrite images in src; write to dest (default: overwrite src via a temp file). Returns dest."""
    src = Path(src)
    if dest is None:
        dest = src
    dest = Path(dest)
    tmp = dest.with_suffix(dest.suffix + ".shrinking.pdf")
    if tmp.exists():
        tmp.unlink()

    doc = pymupdf.open(src)
    before_pages = doc.page_count
    before_text = [" ".join(doc[i].get_text("text").split()) for i in range(before_pages)]
    info = _collect(doc)
    replaced = skipped = 0
    for xref, rec in info.items():
        try:
            if rec["bpc"] == 1 or rec["max_w"] <= 0 or rec["max_h"] <= 0:
                skipped += 1
                continue
            target_w = max(1, int(round(rec["max_w"] / 72.0 * dpi)))
            target_h = max(1, int(round(rec["max_h"] / 72.0 * dpi)))
            scale = min(min(rec["w"], target_w) / rec["w"], min(rec["h"], target_h) / rec["h"])
            new_w = max(1, int(round(rec["w"] * scale)))
            new_h = max(1, int(round(rec["h"] * scale)))
            pix = pymupdf.Pixmap(doc, xref)
            im = _to_pil(pix)
            if (new_w, new_h) != im.size:
                im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            save_im = im if im.mode in ("RGB", "L") else im.convert("RGB")
            save_im.save(buf, format="JPEG", quality=quality, optimize=True, subsampling=0 if quality >= 80 else 2)
            doc[rec["page"]].replace_image(xref, stream=buf.getvalue())
            replaced += 1
        except Exception as e:
            print(f"  skip xref {xref}: {type(e).__name__}: {e}", flush=True)
            skipped += 1
    doc.save(tmp, garbage=4, deflate=True, deflate_images=True, deflate_fonts=True, use_objstms=1, clean=True)
    doc.close()

    out = pymupdf.open(tmp)
    after_text = [" ".join(out[i].get_text("text").split()) for i in range(out.page_count)]
    ok = out.page_count == before_pages and after_text == before_text
    out.close()
    size = tmp.stat().st_size
    print(f"  shrink {src.name}: {src.stat().st_size:,} -> {size:,} bytes "
          f"({size/1024/1024:.2f} MiB); replaced={replaced} skipped={skipped} text_ok={ok}", flush=True)
    if not ok:
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"shrink changed pages or text: {src}")
    if dest.exists() and dest.resolve() != tmp.resolve():
        dest.unlink()
    tmp.replace(dest)
    if dest.stat().st_size > aim:
        print(f"  WARNING: still over 22 MiB ({dest.stat().st_size} bytes)", flush=True)
    return dest


def shrink_folder(folder: Path, aim: int = AIM) -> list[Path]:
    done = []
    for p in sorted(folder.glob("*.pdf")):
        if p.stat().st_size > aim:
            print(f"shrinking {p.name} ({p.stat().st_size:,} bytes)", flush=True)
            shrink_pdf(p, aim=aim)
            done.append(p)
    return done


if __name__ == "__main__":
    paths = [Path(a) for a in sys.argv[1:]]
    if not paths:
        raise SystemExit("usage: shrink_pdf.py FILE_OR_FOLDER ...")
    for p in paths:
        if p.is_dir():
            shrink_folder(p)
        else:
            shrink_pdf(p)
