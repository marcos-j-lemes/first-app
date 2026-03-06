#!/usr/bin/env python3
"""
Gera ícones placeholder para o PWA.
Rode: python3 generate_icons.py
Requer: pip install Pillow
"""
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Instale Pillow: pip install Pillow")
    raise

def make_icon(size, filename):
    img = Image.new('RGB', (size, size), color='#0a0a0a')
    draw = ImageDraw.Draw(img)

    # Borda verde
    draw.rectangle([4, 4, size-5, size-5], outline='#00ff88', width=3)

    # Texto "HW"
    font_size = size // 4
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "HW"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) // 2, (size - th) // 2), text, fill='#00ff88', font=font)

    img.save(filename)
    print(f"✓ {filename} criado ({size}x{size})")

make_icon(192, 'icon-192.png')
make_icon(512, 'icon-512.png')
print("\nÍcones prontos! Coloque-os na mesma pasta do index.html.")