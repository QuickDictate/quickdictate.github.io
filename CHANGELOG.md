# Changelog

Notable changes to the QuickDictate landing page. Newest first. The format loosely
follows [Keep a Changelog](https://keepachangelog.com/). This tracks the *website*;
the app has its own changelog in [LunarWerxs/QuickDictate](https://github.com/LunarWerxs/QuickDictate/blob/main/CHANGELOG.md).

## 2026-09-10

### Changed

- **Corrected the privacy claims.** The page said "zero telemetry" in eight places (both
  social meta descriptions, a hero badge, the visible FAQ answer, the FAQPage JSON-LD,
  `llms.txt`, and `llms-full.txt` twice). That stopped being true when the app added an
  opt-in anonymized usage rollup in v0.9.0, and had always overstated the daily update
  check, which carries an anonymous install id. The badge now reads "Private by default"
  and the FAQ names exactly what leaves the machine: nothing dictated, one daily update
  check with a random install id that can be switched off, and a usage rollup that is off
  until the user turns it on. This now matches the app's own security policy, which
  documented both all along.
- Advertised version bumped to v0.9.1 (JSON-LD `softwareVersion`, hero eyebrow, closing CTA).

## 2026-09-10 (earlier)

### Changed

- Relicensing pass for the app's move to PolyForm Noncommercial 1.0.0 at v0.9.0: the last
  MIT badge became "Free for personal use", the pricing page and `llms-full.txt` now state
  the license and that releases through v0.8.0 stay MIT, and the social card was refreshed.
- Advertised version bumped to v0.9.0, with a new Settings screenshot.

## 2026-07-24

### Changed

- Refreshed the landing page for QuickDictate v0.5.0 and its fully offline Local
  provider.
- Added the Cohere Transcribe and Whisper Large v3 Turbo model choices, their
  download sizes and tradeoffs, and one-click install/select/cancel/delete details.
- Documented parallel verified model downloads, background prewarming, final-result
  feedback, queued local dictation, and the long-session memory/IO improvements.
- Updated setup, provider, privacy, and data-flow copy for the choice between six
  cloud providers and on-device transcription.
- Updated page metadata and the social share card so link previews mention cloud
  and offline speech recognition.

## 2026-07-06

First public version of the site, live at <https://quickdictate.lunarwerx.com/>.

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
