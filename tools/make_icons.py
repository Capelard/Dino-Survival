#!/usr/bin/env python3
"""Stamp the version number onto the Dino Survival PWA icons.

Usage: python3 tools/make_icons.py v3.5

Reads the CLEAN art from icon-192-base.png and icon-512-base.png and writes
icon-192.png and icon-512.png with a version badge. Always badge from the
base files so badges never stack across releases.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BARK = (74, 46, 31, 255)     # --bark
CREAM = (255, 243, 214, 255)  # --cream


def badge(src, dst, version, size):
    im = Image.open(src).convert("RGBA")
    d = ImageDraw.Draw(im)
    fs = int(size * 0.155)
    font = ImageFont.truetype(FONT, fs)
    tb = d.textbbox((0, 0), version, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    pad_x, pad_y = int(fs * 0.55), int(fs * 0.34)
    pw, ph = tw + pad_x * 2, th + pad_y * 2
    # bottom-center, inside the iOS rounded-corner mask safe zone
    x0 = (size - pw) // 2
    y1 = size - int(size * 0.055)
    y0 = y1 - ph
    r = ph // 2
    d.rounded_rectangle([x0 - 3, y0 - 3, x0 + pw + 3, y1 + 3], radius=r + 3,
                        fill=(255, 243, 214, 235))  # cream rim
    d.rounded_rectangle([x0, y0, x0 + pw, y1], radius=r, fill=BARK)
    d.text((x0 + pad_x - tb[0], y0 + pad_y - tb[1]), version, font=font, fill=CREAM)
    im.save(dst, "PNG")
    print(f"wrote {dst} ({size}px, badge '{version}')")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].startswith("v"):
        sys.exit("usage: make_icons.py vN.n")
    v = sys.argv[1]
    badge("icon-192-base.png", "icon-192.png", v, 192)
    badge("icon-512-base.png", "icon-512.png", v, 512)
