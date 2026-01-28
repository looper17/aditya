#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Define work samples with company colors and emojis
work_samples = [
    {"name": "headtonet-brand-refresh", "title": "HeadToNet\nBrand Refresh", "emoji": "🎨", "color": (66, 99, 235)},  # Blue
    {"name": "headtonet-sales-deck", "title": "HeadToNet\nSales Deck", "emoji": "📊", "color": (66, 99, 235)},  # Blue
    {"name": "headtonet-gtm-funnel", "title": "HeadToNet\nGTM Funnel", "emoji": "🔄", "color": (66, 99, 235)},  # Blue
    {"name": "crewasis-haleon", "title": "Crewasis\nHaleon Case Study", "emoji": "💊", "color": (16, 185, 129)},  # Green
    {"name": "crewasis-kellanova", "title": "Crewasis\nKellanova Case Study", "emoji": "🥐", "color": (16, 185, 129)},  # Green
    {"name": "tessa-international", "title": "Tessa International\nMarketing Strategy", "emoji": "🌍", "color": (245, 158, 11)},  # Orange
    {"name": "real-madrid", "title": "Real Madrid\nFan Engagement", "emoji": "⚽", "color": (251, 191, 36)},  # Gold
    {"name": "cyringe-media", "title": "Cyringe Media\nContent Strategy", "emoji": "💉", "color": (239, 68, 68)},  # Red
    {"name": "sportz-interactive", "title": "Sportz Interactive\nContent Writing", "emoji": "🏏", "color": (34, 197, 94)},  # Green
]

# Create preview images
for sample in work_samples:
    # Create image
    img = Image.new('RGB', (800, 500), sample["color"])
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fallback to default
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
        emoji_font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", 100)
    except:
        title_font = ImageFont.load_default()
        emoji_font = ImageFont.load_default()

    # Draw emoji at top
    emoji_bbox = draw.textbbox((0, 0), sample["emoji"], font=emoji_font)
    emoji_width = emoji_bbox[2] - emoji_bbox[0]
    emoji_x = (800 - emoji_width) // 2
    draw.text((emoji_x, 80), sample["emoji"], fill=(255, 255, 255, 230), font=emoji_font)

    # Draw title
    title_bbox = draw.textbbox((0, 0), sample["title"], font=title_font, align="center")
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    title_x = (800 - title_width) // 2
    title_y = 250
    draw.text((title_x, title_y), sample["title"], fill=(255, 255, 255), font=title_font, align="center")

    # Save image
    output_path = f"static/images/{sample['name']}.jpg"
    img.save(output_path, 'JPEG', quality=90)
    print(f"Created: {output_path}")

print("All preview images created!")
