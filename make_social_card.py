"""Generate the Open Graph preview asset with Pillow when the brand copy changes."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
image = Image.new("RGB", (1200, 630), "#11110f")
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 18, 630), fill="#ffc400")
draw.ellipse((904, -120, 1310, 286), outline="#ffc400", width=3)
draw.ellipse((968, -56, 1246, 222), outline="#6c601b", width=2)
draw.line((80, 472, 1120, 472), fill="#4d4c43", width=2)

fonts = Path("C:/Windows/Fonts")
display = ImageFont.truetype(str(fonts / "arialbd.ttf"), 78)
body = ImageFont.truetype(str(fonts / "arial.ttf"), 40)
label = ImageFont.truetype(str(fonts / "arialbd.ttf"), 29)
draw.text((80, 75), "RAIKO", font=label, fill="#ffc400")
draw.text((80, 204), "Yapay zekâ çalışanları.", font=display, fill="#f5f3e9")
draw.text((80, 315), "İletişim. CRM. Satış.", font=body, fill="#d2d0c5")
draw.text((80, 520), "raiko.tech", font=label, fill="#ffc400")
image.save(ROOT / "src" / "social-card.png", optimize=True)
