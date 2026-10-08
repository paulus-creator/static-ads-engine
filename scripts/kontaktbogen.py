#!/usr/bin/env python3
"""Kontaktbogen: alle Kandidaten eines Runs auf Feed-Grösse nebeneinander.

Zweck: Das Wirkungs- und Vielfalts-Urteil bekommt ein Artefakt. Erste Handlung der JURY:
Kontaktbogen bauen und ANSEHEN, vor jedem Einzelverdikt. Referenz-Ads laufen als
markierte Kacheln mit.

Aufruf:
    python3 scripts/kontaktbogen.py --out <bogen.png> --dir workspace/DATUM/03-visuals --referenz r1.png --referenz r2.png
    python3 scripts/kontaktbogen.py --out <bogen.png> bild1.png bild2.png ... --referenz r1.png

--referenz je Referenz einmal angeben (wiederholbar).

Die Thumbnails sind ~270 px breit, ungefähr die Grösse, in der ein Static im mobilen
Feed erscheint. Was hier nicht wirkt, wirkt im Feed nicht.
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow fehlt: pip3 install Pillow")

THUMB_W = 270          # ≈ Feed-Breite mobil
PAD = 16               # Raster-Abstand
LABEL_H = 34           # Platz für Dateinamen
COLS = 5
BG = (245, 245, 243)
REF_BORDER = (200, 160, 30)
LABEL_COL = (60, 60, 60)
EXTS = {".png", ".jpg", ".jpeg", ".webp"}
FONT_CANDIDATES = [
    "/System/Library/Fonts/Helvetica.ttc",                       # macOS
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",           # Linux
    "C:/Windows/Fonts/arial.ttf",                                # Windows
]


def load_thumb(path: Path) -> Image.Image:
    img = Image.open(path).convert("RGB")
    h = max(1, round(img.height * THUMB_W / img.width))
    return img.resize((THUMB_W, h), Image.LANCZOS)


def load_font():
    for cand in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(cand, 13)
        except Exception:
            continue
    return ImageFont.load_default()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="Ziel-PNG des Kontaktbogens")
    ap.add_argument("--referenz", action="append", default=[], metavar="BILD",
                    help="Referenz-Ad (markierter Rahmen); je Referenz einmal angeben")
    ap.add_argument("--dir", help="Ordner rekursiv nach Bildern durchsuchen (statt Einzeldateien)")
    ap.add_argument("bilder", nargs="*", help="Kandidaten-Bilddateien")
    args = ap.parse_args()

    files: list[Path] = [Path(b) for b in args.bilder]
    if args.dir:
        files += sorted(p for p in Path(args.dir).rglob("*") if p.suffix.lower() in EXTS)
    files = [f for f in files if f.exists()]
    refs = [Path(r) for r in args.referenz if Path(r).exists()]
    if not files:
        sys.exit("Keine Bilddateien gefunden. Ein Kontaktbogen ohne Bilder ist kein Beleg.")

    entries = [(p, True) for p in refs] + [(p, False) for p in files]
    thumbs = []
    for path, is_ref in entries:
        try:
            thumbs.append((load_thumb(path), path.name, is_ref))
        except Exception as e:  # unlesbare Datei ist ein Befund, kein Abbruch
            print(f"Warnung: {path} nicht lesbar ({e}). Im Bogen als Lücke vermerken.", file=sys.stderr)

    cols = min(COLS, len(thumbs))
    rows = -(-len(thumbs) // cols)
    row_heights = []
    for r in range(rows):
        row = thumbs[r * cols:(r + 1) * cols]
        row_heights.append(max(t[0].height for t in row) + LABEL_H)

    W = cols * THUMB_W + (cols + 1) * PAD
    H = sum(row_heights) + (rows + 1) * PAD
    sheet = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(sheet)
    font = load_font()

    y = PAD
    for r in range(rows):
        row = thumbs[r * cols:(r + 1) * cols]
        for c, (thumb, name, is_ref) in enumerate(row):
            x = PAD + c * (THUMB_W + PAD)
            sheet.paste(thumb, (x, y))
            if is_ref:
                draw.rectangle([x - 3, y - 3, x + THUMB_W + 2, y + thumb.height + 2],
                               outline=REF_BORDER, width=3)
                name = "REF · " + name
            label = name if len(name) <= 38 else name[:35] + "…"
            draw.text((x, y + thumb.height + 6), label, fill=LABEL_COL, font=font)
        y += row_heights[r] + PAD

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    print(f"Kontaktbogen: {out} — {len(thumbs)} Kacheln ({len(refs)} Referenzen). "
          f"Der Bogen ist Arbeitsmaterial: ANSEHEN, nicht nur erzeugen.")


if __name__ == "__main__":
    main()
