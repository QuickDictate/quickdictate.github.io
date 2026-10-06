"""Bytes a visitor downloads: the committed size at HEAD of the files the site serves (GitHub Pages, no build).
Counts the pages, the images they load, the favicon, the crawler files (robots/sitemap/llms) and the pricing.md
page that sitemap.xml lists. Skips repo tooling/docs folders, dot-folders, and the full-size PNG masters in
assets/ that scripts/optimize_images.py turns into the .webp/.png copies the pages actually load.
Prints shipped_bytes=<n>."""
import subprocess

SERVED = (".html", ".css", ".js", ".mjs", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico",
          ".woff", ".woff2", ".json", ".webmanifest", ".xml", ".txt")
# Markdown the site serves as a page (listed in sitemap.xml). README.md / CHANGELOG.md are repo docs, not counted.
SERVED_PAGES = {"pricing.md"}
# Inputs to scripts/optimize_images.py (the first item of each JOBS entry). No served page references them.
# og-image.png (social card) and icon-64.png (favicon) are NOT masters: they are fetched, so they stay counted.
MASTERS = {
    "assets/icon-256.png",
    "assets/settings.png",
    "assets/text-replacements.png",
    "assets/lw_logo_white.png",
    "assets/github_mark.png",
}
SKIP_DIRS = {"docs", "tools", "scripts", "tmp"}
listing = subprocess.run(["git", "ls-tree", "-r", "-l", "-z", "HEAD"], capture_output=True, check=True).stdout
total = 0
for entry in listing.split(b"\0"):
    if not entry:
        continue
    meta, path = entry.decode("utf-8", "replace").split("\t", 1)
    size = meta.split()[3]
    if size == "-":
        continue
    parts = path.split("/")
    if not (path.lower().endswith(SERVED) or path in SERVED_PAGES):
        continue
    if any(p.startswith(".") for p in parts) or (len(parts) > 1 and parts[0] in SKIP_DIRS):
        continue
    if path in MASTERS:
        continue
    total += int(size)
print(f"shipped_bytes={total}")
