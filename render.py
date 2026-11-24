#!/usr/bin/env python3
"""Render the 24 November 2026 front page for news-image-20261124.

Draws a 1024x1024 broadsheet, "THE WORLD TODAY", with Pillow and DejaVu
fonts only. No network, no external assets, fully deterministic.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 242, 228)
INK = (22, 22, 20)
NAVY = (28, 47, 87)
RED = (158, 27, 27)
GREEN = (23, 114, 69)
GRAY = (90, 90, 82)
PANEL = (233, 226, 203)
RULE = (22, 22, 20)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, leading, fill=INK):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, x1, y, width=2, fill=RULE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_chart(draw, box):
    """Lead illustration: NVDA share-price chart rocketing up."""
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=PANEL, outline=NAVY, width=2)
    # panel title
    draw.text((x0 + 14, y0 + 10), "NVIDIA  (NVDA)", font=SANS_B(17), fill=NAVY)
    draw.text((x0 + 14, y0 + 34), "BEST DAY SINCE 2003", font=SANS_B(14), fill=GRAY)
    # big gain figure
    draw.text((x0 + 14, y0 + 58), "+31%", font=SANS_B(64), fill=GREEN)
    draw.text((x0 + 16, y0 + 126), "IN ONE DAY", font=SANS_B(16), fill=INK)
    # chart area
    cx0, cy0, cx1, cy1 = x0 + 16, y0 + 158, x1 - 16, y1 - 52
    for gy in range(3):
        yy = cy0 + gy * (cy1 - cy0) // 2
        draw.line([(cx0, yy), (cx1, yy)], fill=(210, 202, 178), width=1)
    draw.line([(cx0, cy1), (cx1, cy1)], fill=INK, width=2)
    draw.line([(cx0, cy0), (cx0, cy1)], fill=INK, width=2)
    pts = [
        (cx0, cy1 - 8),
        (cx0 + 40, cy1 - 16),
        (cx0 + 80, cy1 - 10),
        (cx0 + 120, cy1 - 26),
        (cx0 + 160, cy1 - 20),
        (cx0 + 200, cy1 - 46),
        (cx0 + 240, cy1 - 40),
        (cx0 + 268, cy1 - 92),
        (cx1 - 6, cy1 - 118),
    ]
    draw.line(pts, fill=GREEN, width=5, joint="curve")
    # arrowhead at the end
    ex, ey = pts[-1]
    draw.polygon([(ex + 2, ey - 16), (ex + 16, ey + 2), (ex - 12, ey + 6)], fill=GREEN)
    draw.text((x0 + 14, y1 - 40), "ABOUT $1 TRILLION ADDED IN VALUE",
              font=SANS_B(15), fill=INK)


def star4(draw, cx, cy, r, fill):
    pts = []
    for i in range(8):
        ang = -90 + i * 45
        rr = r if i % 2 == 0 else r * 0.28
        import math
        pts.append((cx + rr * math.cos(math.radians(ang)),
                    cy + rr * math.sin(math.radians(ang))))
    draw.polygon(pts, fill=fill)


def icon_nato(draw, x, y, s):
    draw.ellipse([x, y, x + s, y + s], outline=NAVY, width=2)
    star4(draw, x + s // 2, y + s // 2, s // 2 - 4, NAVY)


def icon_kyiv(draw, x, y, s):
    # apartment block with a broken, smoking top
    bx, by = x + 4, y + 20
    bw, bh = s - 8, s - 24
    draw.polygon([(bx, by + bh), (bx, by + 10), (bx + 10, by + 16),
                  (bx + 20, by + 4), (bx + 30, by + 12), (bx + bw, by + 6),
                  (bx + bw, by + bh)], fill=NAVY)
    for wy in (by + 20, by + 30):
        for wx in (bx + 5, bx + 17, bx + 29):
            draw.rectangle([wx, wy, wx + 6, wy + 6], fill=(250, 220, 120))
    # smoke curling from the broken roof
    draw.line([(bx + 26, by + 2), (bx + 32, by - 6), (bx + 26, by - 12)],
              fill=GRAY, width=2)


def icon_cop(draw, x, y, s):
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=2)
    draw.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=NAVY, width=1)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=NAVY, width=1)
    draw.line([(cx - r, cy - 8), (cx - r // 3, cy + 10), (cx + r // 4, cy - 12),
               (cx + r, cy + 4)], fill=RED, width=3)


def icon_fifa(draw, x, y, s):
    import math
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
                 outline=INK, width=2)
    pr = r * 0.38
    pent = [(cx + pr * math.cos(math.radians(-90 + i * 72)),
             cy + pr * math.sin(math.radians(-90 + i * 72))) for i in range(5)]
    draw.polygon(pent, fill=INK)
    for i in range(5):
        vx, vy = pent[i]
        draw.line([(vx, vy), (cx + r * 0.95 * math.cos(math.radians(-90 + i * 72)),
                              cy + r * 0.95 * math.sin(math.radians(-90 + i * 72)))],
                  fill=INK, width=2)


def story(draw, x, y, w, kicker, headline, body, icon=None):
    """One grid story cell; returns y below the cell."""
    ix = None
    if icon is not None:
        icon(draw, x + w - 56, y + 2, 56)
        w -= 66
    draw.text((x, y), kicker, font=SANS_B(14), fill=RED)
    y += 22
    y = para(draw, (x, y), headline, SERIF_B(26), w, 32)
    y += 4
    y = para(draw, (x, y), body, SANS(17), w + (66 if icon else 0), 23)
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 34
    R = W - M  # right edge 990

    # ---- masthead ----
    title = "THE WORLD TODAY"
    tf = SERIF_B(62)
    d.text(((W - d.textlength(title, font=tf)) / 2, 22), title, font=tf, fill=INK)
    rule(d, M, R, 96, 3)
    rule(d, M, R, 101, 1)
    dl = "TUESDAY, 24 NOVEMBER 2026"
    df = SANS_B(23)
    d.text(((W - d.textlength(dl, font=df)) / 2, 110), dl, font=df, fill=NAVY)
    left = "VOL. I — No. 24"
    right = "ONE DAY · ONE PAGE"
    d.text((M, 116), left, font=SANS(14), fill=GRAY)
    d.text((R - d.textlength(right, font=SANS(14)), 116), right,
           font=SANS(14), fill=GRAY)
    rule(d, M, R, 146, 3)

    # ---- lead story ----
    lx, lw = M, 596
    d.text((lx, 160), "★  LEAD STORY — MARKETS", font=SANS_B(16), fill=RED)
    y = 186
    y = para(d, (lx, y), "HUANG'S $1 TRILLION COMEBACK",
             SERIF_B(46), lw, 54)
    y += 10
    y = para(d, (lx, y),
             "Nvidia's board reinstates Jensen Huang as chief executive, "
             "eleven days after he resigned. Shares soar 31% — the best "
             "day since 2003 — adding about $1 trillion in value, and the "
             "Nasdaq jumps 6.5% in a broad tech rally.",
             SANS(19), lw, 26)
    draw_chart(d, (656, 160, R, 470))

    rule(d, M, R, 490, 2)

    # ---- 2x2 grid ----
    col_w = 466
    x2 = M + col_w + 24
    story(d, M, 506, col_w,
          "WAR IN EUROPE",
          "NATO MEETS AS WAR SPILLS OVER",
          "Russian missiles land in Poland. Allies hold an emergency "
          "session in Brussels and send AWACS surveillance planes east.",
          icon_nato)
    story(d, x2, 506, col_w,
          "UKRAINE",
          "KYIV MOURNS 12 DEAD",
          "Russian strikes hit a block of flats in Dymer and a "
          "supermarket in Vyshneve. Rescuers search the rubble for the "
          "missing.",
          icon_kyiv)
    rule(d, M, R, 668, 1, fill=(180, 172, 150))
    story(d, M, 684, col_w,
          "CLIMATE",
          "COP31: 'WORST EVER'",
          "UN climate talks in Antalya end with no deal. The blame game "
          "erupts, and Pacific nations vow to go it alone.",
          icon_cop)
    story(d, x2, 684, col_w,
          "SPORT",
          "WORLD CUP HOSTS NAMED",
          "USA, Mexico, Costa Rica and Jamaica will host the 2031 "
          "Women's World Cup; England, Scotland, Wales and Northern "
          "Ireland take 2035.",
          icon_fifa)

    rule(d, M, R, 856, 2)

    # ---- also today strip ----
    d.text((M, 872), "ALSO TODAY", font=SANS_B(16), fill=RED)
    strip = [
        ("CYPRUS — ", "Expels two Russian diplomats over suspected spying."),
        ("KIRIBATI — ", "Remote Kanton Island evacuated at a day's notice."),
        ("CHICAGO — ", "O'Hare ground stop in the Thanksgiving travel rush."),
        ("BERLIN — ", "Some 450 schools hit by emailed bomb threats."),
    ]
    sw = (R - M - 3 * 16) // 4
    for i, (lead, rest) in enumerate(strip):
        sx = M + i * (sw + 16)
        yy = 900
        yy = para(d, (sx, yy), lead, SANS_B(15), sw, 20)
        yy = para(d, (sx, yy), rest, SANS(15), sw, 20)
        if i < 3:
            d.line([(sx + sw + 8, 900), (sx + sw + 8, 962)],
                   fill=(180, 172, 150), width=1)

    rule(d, M, R, 978, 1)
    foot = "THE WORLD TODAY  •  The news of Tuesday, 24 November 2026"
    ff = SANS(13)
    d.text(((W - d.textlength(foot, font=ff)) / 2, 986), foot, font=ff, fill=GRAY)

    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
