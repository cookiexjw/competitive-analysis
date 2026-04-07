from pathlib import Path
import re

import markdown
from bs4 import BeautifulSoup


def build_html(markdown_text: str, title: str = "竞争分析") -> str:
    body_html = markdown.markdown(
        markdown_text,
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
    )
    soup = BeautifulSoup(f'<div id="root">{body_html}</div>', "html.parser")
    root = soup.find("div", id="root")

    for p in list(root.find_all("p")):
        if len(p.contents) != 1:
            continue
        img = p.find("img", recursive=False)
        if not img:
            continue

        alt = img.get("alt", "图片")
        src = img.get("src", "")
        figure = soup.new_tag("figure", attrs={"class": "image-card"})
        button = soup.new_tag(
            "button",
            attrs={
                "class": "image-button",
                "type": "button",
                "data-fullsrc": src,
                "data-caption": alt,
                "aria-label": f"点击放大查看 {alt}",
            },
        )
        new_img = soup.new_tag("img", attrs={"alt": alt, "src": src, "loading": "lazy"})
        caption = soup.new_tag("figcaption")
        caption.string = alt
        button.append(new_img)
        figure.append(button)
        figure.append(caption)
        p.replace_with(figure)

    for p in list(root.find_all("p")):
        text = p.get_text(" ", strip=True)
        if not re.fullmatch(r"[^<]{1,80}[：:]", text):
            continue
        next_tag = p.find_next_sibling()
        if not next_tag or next_tag.name != "figure":
            continue
        classes = next_tag.get("class", [])
        if "image-card" not in classes:
            continue
        if "with-label" not in classes:
            next_tag["class"] = classes + ["with-label"]
        label = soup.new_tag("div", attrs={"class": "image-label"})
        label.string = text
        next_tag.insert(0, label)
        p.extract()

    body = "".join(str(child) for child in root.contents)
    body = re.sub(
        r'<figure class="image-card with-label"><div class="image-label">(.*?)</div><figure class="image-card">(.*?)</figure>',
        r'<figure class="image-card with-label"><div class="image-label">\1</div>\2</figure>',
        body,
        flags=re.S,
    )
    body = re.sub(
        r'((?:<figure class="image-card(?: with-label)?">.*?</figure>\s*){2,})',
        r'<div class="image-grid">\1</div>',
        body,
        flags=re.S,
    )

    css = """
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; background: #f5f7fb; color: #1f2937; }
main { max-width: 960px; margin: 0 auto; background: #fff; padding: 36px 44px 72px; box-shadow: 0 10px 30px rgba(15, 23, 42, .08); }
h1, h2, h3, h4 { color: #111827; line-height: 1.3; }
p, li { font-size: 16px; line-height: 1.75; }
table { border-collapse: collapse; width: 100%; margin: 18px 0 28px; font-size: 15px; }
th, td { border: 1px solid #e5e7eb; padding: 10px 12px; text-align: left; vertical-align: top; }
th { background: #f9fafb; }
.image-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 18px; margin: 10px 0 24px; }
.image-card { width: min(100%, 560px); margin: 14px auto 18px; }
.image-grid .image-card { width: 100%; margin: 0; }
.image-label { margin-bottom: 10px; font-size: 15px; font-weight: 600; color: #374151; }
.image-button { display: block; width: 100%; padding: 0; border: 0; background: transparent; cursor: zoom-in; }
.image-card img { display: block; width: 100%; max-height: 340px; object-fit: contain; background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 14px; box-shadow: 0 6px 18px rgba(15, 23, 42, .08); }
.image-grid .image-card img { max-height: 250px; }
.image-card figcaption { margin-top: 8px; font-size: 14px; color: #6b7280; text-align: center; }
.preview-overlay { position: fixed; inset: 0; display: none; align-items: center; justify-content: center; padding: 28px; background: rgba(15, 23, 42, .82); z-index: 9999; }
.preview-overlay.is-open { display: flex; }
.preview-dialog { position: relative; max-width: min(92vw, 1400px); max-height: 90vh; }
.preview-dialog img { display: block; max-width: 100%; max-height: 82vh; border-radius: 16px; box-shadow: 0 18px 48px rgba(0, 0, 0, .35); background: white; }
.preview-caption { margin-top: 10px; text-align: center; color: #e5e7eb; font-size: 14px; }
.preview-close { position: absolute; right: -10px; top: -10px; width: 40px; height: 40px; border: 0; border-radius: 999px; background: rgba(17, 24, 39, .9); color: white; font-size: 24px; cursor: pointer; }
"""

    js = """
(() => {
  const overlay = document.querySelector('.preview-overlay');
  const overlayImg = overlay.querySelector('img');
  const caption = overlay.querySelector('.preview-caption');
  const closeBtn = overlay.querySelector('.preview-close');

  function closePreview() {
    overlay.classList.remove('is-open');
    overlayImg.removeAttribute('src');
    overlayImg.removeAttribute('alt');
    caption.textContent = '';
  }

  document.querySelectorAll('.image-button').forEach(btn => {
    btn.addEventListener('click', () => {
      overlayImg.src = btn.dataset.fullsrc;
      overlayImg.alt = btn.dataset.caption || '预览图片';
      caption.textContent = btn.dataset.caption || '';
      overlay.classList.add('is-open');
    });
  });

  closeBtn.addEventListener('click', closePreview);
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) closePreview();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closePreview();
  });
})();
"""

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<main>
{body}
</main>
<div class="preview-overlay" aria-hidden="true">
  <div class="preview-dialog">
    <button class="preview-close" type="button" aria-label="关闭图片预览">×</button>
    <img alt="" src="" />
    <div class="preview-caption"></div>
  </div>
</div>
<script>{js}</script>
</body>
</html>"""


if __name__ == "__main__":
    print("Usage: import build_html(markdown_text, title) from this script.")
