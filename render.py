#!/usr/bin/env python3
"""Render the news-image entry for Sunday 22 November 2026.

Draws a 1024x1024 newspaper front page with PIL: every letter is rendered
from a system font, so no text is ever garbled. All illustrations are
original vector-style drawings made from PIL primitives -- no photographs,
no copied artwork, no image generator.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (25, 25, 25)
RED = (163, 22, 33)
NAVY = (16, 39, 61)
NAVY2 = (24, 58, 88)
AMBER = (242, 183, 5)
GREY = (90, 84, 72)
CARD = (255, 253, 247)
BORDER = (216, 208, 189)
LIGHT = (223, 232, 240)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lead_art(d, x0, y0, x1, y1):
    """Night sky over the Gulf: skyline, radar dome, missile arcs, sea."""
    d.rectangle([x0, y0, x1, y1], fill=NAVY)
    # stars
    import random
    rng = random.Random(7)
    for _ in range(46):
        sx = rng.randint(x0 + 4, x1 - 4)
        sy = rng.randint(y0 + 4, y0 + 110)
        r = rng.choice([1, 1, 2])
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(200, 215, 230))
    # moon
    d.ellipse([x1 - 62, y0 + 18, x1 - 22, y0 + 58], fill=(240, 230, 190))
    d.ellipse([x1 - 54, y0 + 24, x1 - 22, y0 + 58], fill=NAVY)
    # missile arcs with glowing heads
    for (ax, ay, bx, by, col) in [
        (x0 + 30, y1 - 60, x0 + 210, y0 + 70, (255, 150, 60)),
        (x0 + 90, y1 - 40, x0 + 260, y0 + 95, (255, 200, 90)),
    ]:
        d.arc([ax - 120, ay - 190, bx + 60, by + 130], start=200, end=330,
              fill=col, width=4)
        d.ellipse([bx - 6, by - 6, bx + 6, by + 6], fill=col)
        d.ellipse([bx - 3, by - 3, bx + 3, by + 3], fill=(255, 255, 220))
    # skyline silhouettes
    base = y1 - 78
    heights = [46, 78, 58, 92, 40, 70, 52, 84, 36, 64]
    bw = (x1 - x0) // len(heights)
    for i, hh in enumerate(heights):
        bx0 = x0 + i * bw + 2
        bx1 = x0 + (i + 1) * bw - 2
        d.rectangle([bx0, base - hh, bx1, base], fill=(8, 22, 36))
        for wy in range(base - hh + 8, base - 6, 14):
            for wx in range(bx0 + 5, bx1 - 4, 11):
                if (wx + wy) % 3 == 0:
                    d.rectangle([wx, wy, wx + 3, wy + 5], fill=(255, 205, 90))
    # radar dome + dish on a low block
    cx = x0 + 250
    d.rectangle([cx - 30, base - 26, cx + 30, base], fill=(8, 22, 36))
    d.pieslice([cx - 24, base - 72, cx + 24, base - 24], start=180, end=360,
               fill=(235, 238, 240))
    d.line([cx, base - 48, cx + 22, base - 68], fill=(235, 238, 240), width=4)
    d.ellipse([cx + 16, base - 74, cx + 30, base - 60], fill=(235, 238, 240))
    # sea
    d.rectangle([x0, base, x1, y1], fill=(13, 48, 74))
    for wy in range(base + 10, y1 - 6, 14):
        d.line([x0 + 12, wy, x0 + 60, wy], fill=(70, 120, 160), width=2)
        d.line([x0 + 180, wy + 6, x0 + 250, wy + 6], fill=(70, 120, 160), width=2)
        d.line([x1 - 90, wy, x1 - 30, wy], fill=(70, 120, 160), width=2)


def draw_ship(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(31, 74, 110))
    d.rectangle([x0, y1 - 46, x1, y1], fill=(13, 48, 74))
    for wy in range(y1 - 40, y1 - 4, 12):
        d.line([x0 + 10, wy, x0 + 46, wy], fill=(90, 140, 180), width=2)
        d.line([x0 + 90, wy + 5, x0 + 130, wy + 5], fill=(90, 140, 180), width=2)
    # hull
    d.polygon([(x0 + 14, y1 - 78), (x1 - 14, y1 - 78), (x1 - 34, y1 - 52),
               (x0 + 34, y1 - 52)], fill=(60, 60, 64))
    d.polygon([(x0 + 14, y1 - 78), (x1 - 14, y1 - 78), (x1 - 20, y1 - 70),
               (x0 + 20, y1 - 70)], fill=(163, 22, 33))
    # containers
    d.rectangle([x0 + 30, y1 - 104, x0 + 62, y1 - 78], fill=(242, 183, 5))
    d.rectangle([x0 + 66, y1 - 104, x0 + 98, y1 - 78], fill=(220, 220, 215))
    d.rectangle([x0 + 48, y1 - 128, x0 + 80, y1 - 104], fill=(200, 90, 60))
    # smoke + flame
    d.ellipse([x0 + 96, y0 + 16, x0 + 118, y0 + 38], fill=(120, 120, 118))
    d.ellipse([x0 + 108, y0 + 6, x0 + 126, y0 + 24], fill=(150, 150, 148))
    d.polygon([(x0 + 100, y1 - 104), (x0 + 112, y1 - 124), (x0 + 122, y1 - 104)],
              fill=(255, 150, 60))


def draw_city(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(74, 52, 44))
    # damaged towers
    d.polygon([(x0 + 16, y1 - 20), (x0 + 16, y0 + 52), (x0 + 44, y0 + 38),
               (x0 + 52, y0 + 66), (x0 + 52, y1 - 20)], fill=(38, 32, 30))
    d.rectangle([x0 + 62, y0 + 66, x0 + 104, y1 - 20], fill=(52, 44, 40))
    d.polygon([(x0 + 62, y0 + 66), (x0 + 83, y0 + 46), (x0 + 104, y0 + 66)],
              fill=(52, 44, 40))
    d.rectangle([x0 + 112, y0 + 88, x0 + 136, y1 - 20], fill=(38, 32, 30))
    for wx in range(x0 + 70, x0 + 100, 12):
        for wy in range(y0 + 78, y1 - 30, 16):
            if (wx + wy) % 5 == 0:
                d.rectangle([wx, wy, wx + 4, wy + 6], fill=(255, 205, 90))
    # smoke
    d.ellipse([x0 + 30, y0 + 14, x0 + 56, y0 + 36], fill=(150, 145, 138))
    d.ellipse([x0 + 48, y0 + 4, x0 + 70, y0 + 24], fill=(170, 165, 158))
    # ground line
    d.rectangle([x0, y1 - 20, x1, y1 - 14], fill=(30, 26, 24))


def draw_ballot(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(26, 84, 66))
    # ballot paper dropping in
    d.polygon([(x0 + 58, y0 + 22), (x0 + 96, y0 + 22), (x0 + 96, y0 + 62),
               (x0 + 58, y0 + 62)], fill=(255, 253, 247))
    d.line([x0 + 66, y0 + 34, x0 + 88, y0 + 34], fill=(26, 84, 66), width=3)
    d.line([x0 + 66, y0 + 44, x0 + 88, y0 + 44], fill=(26, 84, 66), width=3)
    d.line([x0 + 66, y0 + 54, x0 + 80, y0 + 54], fill=(26, 84, 66), width=3)
    # box
    d.rectangle([x0 + 34, y0 + 66, x0 + 120, y1 - 24], fill=(242, 183, 5))
    d.rectangle([x0 + 34, y0 + 66, x0 + 120, y0 + 82], fill=(214, 158, 0))
    d.rectangle([x0 + 68, y0 + 60, x0 + 86, y0 + 70], fill=(26, 84, 66))
    # check mark
    d.line([x0 + 52, y0 + 108, x0 + 68, y0 + 124], fill=(163, 22, 33), width=6)
    d.line([x0 + 68, y0 + 124, x0 + 102, y0 + 90], fill=(163, 22, 33), width=6)


def draw_globe(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(18, 64, 96))
    cx, cy, r = (x0 + x1) // 2, (y0 + y1) // 2, 56
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 190, 220))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 253, 247), width=3)
    # meridians
    d.ellipse([cx - 26, cy - r, cx + 26, cy + r], outline=(255, 253, 247), width=2)
    d.line([cx - r, cy, cx + r, cy], fill=(255, 253, 247), width=2)
    d.arc([cx - r, cy - 26, cx + r, cy + 26], start=0, end=360,
          fill=(255, 253, 247), width=2)
    # land blobs
    d.ellipse([cx - 44, cy - 34, cx - 8, cy - 6], fill=(46, 139, 87))
    d.ellipse([cx + 2, cy + 8, cx + 42, cy + 38], fill=(46, 139, 87))
    d.ellipse([cx + 8, cy - 40, cx + 34, cy - 16], fill=(46, 139, 87))
    # sun / heat rays
    for i in range(5):
        yy = y0 + 14 + i * 8
        d.line([x1 - 34, yy, x1 - 18, yy], fill=(242, 183, 5), width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 30

    # ---- masthead ----
    title_f = font(SERIF_B, 64)
    d.text((W // 2, 66), "THE WORLD TODAY", font=title_f, fill=INK, anchor="mm")
    date_f = font(SERIF_B, 38)
    d.text((W // 2, 122), "SUNDAY, 22 NOVEMBER 2026", font=date_f, fill=RED,
           anchor="mm")
    d.line([M, 152, W - M, 152], fill=INK, width=3)
    d.line([M, 158, W - M, 158], fill=INK, width=1)
    sub_f = font(SERIF, 19)
    d.text((W // 2, 176), "Six stories from one day — the Gulf, Europe, Asia, the climate talks and sport",
           font=sub_f, fill=GREY, anchor="mm")

    # ---- lead story ----
    lx0, ly0, lx1, ly1 = M, 196, W - M, 480
    d.rectangle([lx0, ly0, lx1, ly1], fill=NAVY)
    draw_lead_art(d, lx1 - 340, ly0 + 14, lx1 - 16, ly1 - 14)
    tx = lx0 + 24
    d.text((tx, ly0 + 22), "THE GULF  ·  LEAD STORY", font=font(SANS_B, 18),
           fill=AMBER)
    head_f = font(SERIF_B, 45)
    lines = wrap(d, "IRAN STRIKES U.S. BASES IN BAHRAIN", head_f, 560)
    y = ly0 + 56
    for ln in lines:
        d.text((tx, y), ln, font=head_f, fill=(255, 255, 255))
        y += 52
    body_f = font(SANS, 21)
    summary = ("Tehran claims its missiles and drones destroyed two U.S. "
               "Patriot radars. Bahrain says its air defences intercepted "
               "attacks; the U.S. has not confirmed radar damage. Bahrain "
               "says a factory caught fire.")
    y += 8
    for ln in wrap(d, summary, body_f, 560):
        d.text((tx, y), ln, font=body_f, fill=LIGHT)
        y += 28

    # ---- 2x2 grid ----
    stories = [
        ("BALTIC SEA", "Ship ablaze after drone strike",
         "The sanctioned Russian ship Sparta II burns and drifts into Finnish "
         "waters. All 16 crew escape unhurt.", draw_ship),
        ("UKRAINE", "Missiles kill two in Kryvyi Rih",
         "A Russian strike on the president's home city kills a boy of 7 and a "
         "paramedic, and wounds 60.", draw_city),
        ("HONG KONG", "Hong Kong picks its Election Committee",
         "Polls open for 723 seats on the 1,500-member body that picks the "
         "city's leader. 856 candidates run.", draw_ballot),
        ("CLIMATE", "COP31 deadlocked in overtime",
         "Talks in Antalya run past their deadline, split over fossil fuels "
         "and finance.", draw_globe),
    ]
    gy0, cell_h, gap = 496, 186, 14
    cw = (W - 2 * M - gap) // 2
    for i, (kick, head, body, art) in enumerate(stories):
        cx0 = M + (i % 2) * (cw + gap)
        cy0 = gy0 + (i // 2) * (cell_h + gap)
        cx1, cy1 = cx0 + cw, cy0 + cell_h
        d.rectangle([cx0, cy0, cx1, cy1], fill=CARD, outline=BORDER, width=1)
        art(d, cx0 + 10, cy0 + 10, cx0 + 140, cy1 - 10)
        tx2 = cx0 + 154
        d.text((tx2, cy0 + 16), kick, font=font(SANS_B, 15), fill=RED)
        hf = font(SERIF_B, 24)
        hy = cy0 + 40
        for ln in wrap(d, head, hf, cw - 170):
            d.text((tx2, hy), ln, font=hf, fill=INK)
            hy += 29
        bf = font(SANS, 17)
        by = hy + 6
        for ln in wrap(d, body, bf, cw - 170):
            d.text((tx2, by), ln, font=bf, fill=(60, 56, 48))
            by += 22

    # ---- bottom strip ----
    fy = gy0 + 2 * cell_h + gap + 14
    d.line([M, fy, W - M, fy], fill=INK, width=2)
    sf = font(SANS_B, 19)
    d.text((M, fy + 16), "SPORT", font=sf, fill=RED)
    d.text((M + 78, fy + 16),
           "Smith, Starc ruled out of South Africa tour — Labuschagne "
           "recalled to the ODI squad.", font=font(SANS, 19), fill=INK)
    ff = font(SANS, 15)
    d.text((M, fy + 52),
           "Sources: Reuters, AP, Xinhua, Al Jazeera, CNN, China Daily — 22 "
           "November 2026. Original illustration; no photographs.",
           font=ff, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
