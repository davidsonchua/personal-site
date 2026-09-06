#!/usr/bin/env python3
"""Regenerate site/assets/og-image.png (1200x630).
Run from /home/claude:  python3 _tools/make_og.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1200, 630
DARK = (26, 32, 44)
GRAY = (100, 110, 125)
BORDER = (225, 228, 232)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# card border
d.rectangle([28, 28, W - 29, H - 29], outline=BORDER, width=2)

# circular headshot
SIZE = 196
photo = Image.open("site/assets/profile-800.webp").convert("RGB")
photo = ImageOps.fit(photo, (SIZE, SIZE), Image.LANCZOS)
mask = Image.new("L", (SIZE * 4, SIZE * 4), 0)
ImageDraw.Draw(mask).ellipse([0, 0, SIZE * 4 - 1, SIZE * 4 - 1], fill=255)
mask = mask.resize((SIZE, SIZE), Image.LANCZOS)
img.paste(photo, (89, 119), mask)

f_name = ImageFont.truetype(BOLD, 54)
f_sub = ImageFont.truetype(REG, 32)
f_tag = ImageFont.truetype(REG, 28)
f_url = ImageFont.truetype(BOLD, 28)

X = 330
d.text((X, 132), "DAVIDSON CHUA", font=f_name, fill=DARK)
d.text((X, 208), "Co-founder & CEO, Influencees", font=f_sub, fill=(55, 65, 80))
d.text((X, 252), "Founder, Autosave", font=f_sub, fill=(55, 65, 80))
d.line([X, 316, X + 300, 316], fill=BORDER, width=2)
d.text((X, 338), "Creator credibility & community", font=f_tag, fill=GRAY)
d.text((X, 374), "building in Singapore", font=f_tag, fill=GRAY)
d.text((88, 540), "davidsonchua.cc", font=f_url, fill=DARK)

img.save("site/assets/og-image.png", optimize=True)
print("wrote site/assets/og-image.png", img.size)
