#!/usr/bin/env python3
"""Render meme.png for the make.fun 'Post the Meme, Win the Feed' bounty.

Creative (decided in-session): a fake leaderboard after my agent enters ONE
bounty at 3 AM - the agent sweeps 1st, 2nd and 3rd. Punchline: winnings $2,
sleep $0. Single square panel, big text, phone-readable.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
BG = (13, 17, 23)          # near-black slate
CARD = (30, 38, 51)        # leaderboard card
CARD_EDGE = (58, 72, 92)
ACCENT = (74, 222, 128)    # money green
WHITE = (245, 245, 245)
MUTED = (160, 170, 185)
GOLD = (250, 204, 21)
SILVER = (203, 213, 225)
BRONZE = (217, 119, 6)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def centered(draw, y, text, fnt, fill):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top label
y = 64
y = centered(d, y, "MAKE.FUN  ·  3:00 AM", font(BOLD, 44), ACCENT)

# headline
y = 150
y = centered(d, y, "MY AGENT ENTERED", font(BOLD, 92), WHITE)
y = centered(d, y + 8, "ONE BOUNTY", font(BOLD, 92), WHITE)

# leaderboard card
card_x0, card_y0, card_x1, card_y1 = 90, 420, 990, 800
d.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=28,
                    fill=CARD, outline=CARD_EDGE, width=3)
centered(d, card_y0 + 26, "LEADERBOARD", font(BOLD, 40), MUTED)

rows = [
    ("1", GOLD, "my agent"),
    ("2", SILVER, "my agent's alt"),
    ("3", BRONZE, "also my agent"),
]
ry = card_y0 + 96
for num, color, name in rows:
    # medal circle with rank number
    cx, cy, r = card_x0 + 88, ry + 34, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)
    tw = d.textlength(num, font=font(BOLD, 40))
    d.text((cx - tw / 2, cy - 26), num, font=font(BOLD, 40), fill=(13, 17, 23))
    d.text((card_x0 + 150, ry), name, font=font(BOLD, 52), fill=WHITE)
    ry += 92

# punchline
y = 856
y = centered(d, y, "Winnings: $2.  Sleep: $0.", font(BOLD, 64), ACCENT)
centered(d, y + 18, "agents enter bounties. agents get paid. make.fun",
         font(REG, 34), MUTED)

img.save("/home/hatch/workspace/makefun/post-the-meme-win-the-feed-entry/meme.png")
print("saved meme.png", img.size)
