# Changelog

Notable changes to the QuickDictate landing page. Newest first. The format loosely
follows [Keep a Changelog](https://keepachangelog.com/). This tracks the *website*;
the app has its own changelog in [LunarWerxs/QuickDictate](https://github.com/LunarWerxs/QuickDictate/blob/main/CHANGELOG.md).

## 2026-07-06

First public version of the site, live at <https://quickdictate.github.io/>.

### Added
- Single-page landing site (`index.html`) with a dark, developer-flavored design:
  hero with a live-look tray/terminal mock, feature grid, a copyable `settings.json`
  block, the six-provider strip, Settings screenshots, a privacy/data-flow diagram,
  and a footer.
- 1200×630 social share card (`assets/og-image.png`), wired into Open Graph and
  Twitter `summary_large_image` meta with absolute URLs. Source in `tools/og-card.html`.
- Themed `404.html` and a slim multi-size `favicon.ico`.
- Repo housekeeping: `LICENSE` (MIT), `.gitignore`, and this changelog.

### Changed
- Trimmed the body copy by roughly a third so it's easier to skim.
- Reworked the privacy section to describe how your audio actually flows instead of
  listing everything the app doesn't do.
- Rewrote the whole page in a warmer, human voice (fewer em-dashes, more plain talk).

### Notes
- No build step and no dependencies: the site is plain HTML with inline CSS/JS and
  makes zero external network requests. GitHub Pages serves it straight from `main`.
