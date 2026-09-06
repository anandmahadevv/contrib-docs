from PIL import Image, ImageDraw, ImageFont
import os

width = 1200
height = 630

# Create high-res RGB canvas
img = Image.new('RGB', (width, height), color='#020617') # Slate-950 background
draw = ImageDraw.Draw(img)

# Try loading system font or fallback
def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeui.ttf" if not bold else "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\arial.ttf" if not bold else "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\consola.ttf"
    ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_hero = get_font(52, bold=True)
font_title = get_font(38, bold=True)
font_sub = get_font(22, bold=False)
font_badge = get_font(18, bold=True)
font_code = get_font(20, bold=True)
font_metric_val = get_font(36, bold=True)
font_metric_lbl = get_font(15, bold=False)

# Draw subtle top border accent
draw.rectangle([0, 0, width, 6], fill='#3b82f6') # Blue-500 accent bar

# Draw background glowing circles / gradient accents (subtle geometric shapes)
for r in range(300, 0, -20):
    alpha = int(25 * (r / 300))
    color = (30, 58, 138, alpha) # Dark blue glow top right
    # Draw soft circle
    draw.ellipse([850 - r, 100 - r, 850 + r, 100 + r], outline=None, fill='#0f172a')

# 1. Top Brand Pill
draw.rounded_rectangle([80, 60, 290, 100], radius=10, fill='#1e293b', outline='#334155', width=1)
draw.text((100, 70), "gsoc-contrib", fill='#38bdf8', font=font_badge)
draw.text((225, 70), "v0.4.0", fill='#94a3b8', font=font_badge)

# 2. Main Hero Title
draw.text((80, 125), "Sub-Second Workspace Manager", fill='#ffffff', font=font_hero)
draw.text((80, 190), "for Open-Source Contributors", fill='#38bdf8', font=font_hero)

# 3. Subtitle Description
draw.text((80, 265), "Instant, blobless git checkouts with 94%+ bandwidth savings & zero telemetry.", fill='#94a3b8', font=font_sub)

# 4. Code Snippet Terminal Box
draw.rounded_rectangle([80, 315, 1120, 425], radius=16, fill='#090d16', outline='#1e293b', width=2)
# Window dots
draw.ellipse([105, 335, 117, 347], fill='#ef4444')
draw.ellipse([125, 335, 137, 347], fill='#f59e0b')
draw.ellipse([145, 335, 157, 347], fill='#10b981')

# Code Command
draw.text((105, 370), "$ npx gsoc-contrib start https://github.com/owner/repo/issues/42 --worktree", fill='#34d399', font=font_code)

# 5. Metric Cards across the bottom
metrics = [
    {"val": "94.2%", "lbl": "Bandwidth & Disk Saved", "color": "#10b981", "bg": "#064e3b22", "border": "#059669"},
    {"val": "1.2s", "lbl": "Sub-Second Worktrees", "color": "#3b82f6", "bg": "#1e3a8a22", "border": "#2563eb"},
    {"val": "Zero", "lbl": "Telemetry & Tracking", "color": "#a855f7", "bg": "#581c8722", "border": "#9333ea"}
]

card_w = 325
card_h = 110
gap = 35

for i, m in enumerate(metrics):
    x1 = 80 + i * (card_w + gap)
    y1 = 460
    x2 = x1 + card_w
    y2 = y1 + card_h
    draw.rounded_rectangle([x1, y1, x2, y2], radius=14, fill='#0f172a', outline=m["border"], width=1)
    draw.text((x1 + 24, y1 + 18), m["val"], fill=m["color"], font=font_metric_val)
    draw.text((x1 + 24, y1 + 68), m["lbl"], fill='#94a3b8', font=font_metric_lbl)

# Footer domain attribution
draw.text((80, 585), "anandmahadevv.github.io/contrib-docs", fill='#64748b', font=font_metric_lbl)
draw.text((950, 585), "MIT Open Source", fill='#64748b', font=font_metric_lbl)

output_path = os.path.join(r"C:\Users\anand\contrib-docs", "og-image.png")
img.save(output_path, "PNG")
print(f"Generated OG Image successfully at {output_path}")
