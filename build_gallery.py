import os
from pathlib import Path
from html import escape

PROJECT_ROOT = Path(__file__).parent
IMG_DIR = PROJECT_ROOT / "images" / "gallery"
OUTPUT = PROJECT_ROOT / "gallery.html"

ALLOWED = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

def get_images():
    if not IMG_DIR.exists():
        print(f"Creating image directory: {IMG_DIR}")
        IMG_DIR.mkdir(parents=True, exist_ok=True)
    files = [f for f in sorted(IMG_DIR.iterdir()) if f.suffix.lower() in ALLOWED]
    return files

def build_html(images):
    cards = []
    for img in images:
        rel_path = f"images/gallery/{img.name}"
        alt = escape(img.stem.replace('-', ' ').replace('_', ' ').title())
        cards.append(f"""
          <div class="gallery-item">
            <a href="{rel_path}" target="_blank">
              <img src="{rel_path}" alt="{alt}">
            </a>
            <a class="download-btn" href="{rel_path}" download>Download</a>
          </div>
        """.strip())

    gallery_items = "\n".join(cards) if cards else "<p>No photos yet. Check back soon!</p>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Jasmine's Birthday Gallery</title>
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <section class="gallery-background">
    <div class="gallery-heading-box">
      <h1>Magical Memories Gallery</h1>
      <p>Click any photo to view or use the button to download.</p>
    </div>

    <div class="gallery-grid">
      {gallery_items}
    </div>

    <p style="margin-top:24px;">
      <a class="gallery-button" href="index.html">← Back to Home</a>
    </p>
  </section>
</body>
</html>"""

def main():
    images = get_images()
    html = build_html(images)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated: {OUTPUT} ({len(images)} images)")

if __name__ == "__main__":
    main()