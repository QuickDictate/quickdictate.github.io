# Changelog

Notable changes to the QuickDictate landing page. Newest first. The format loosely
follows [Keep a Changelog](https://keepachangelog.com/). This tracks the *website*;
the app has its own changelog in [LunarWerxs/QuickDictate](https://github.com/LunarWerxs/QuickDictate/blob/main/CHANGELOG.md).

## 2026-09-18

### Changed

- **Commercial use has a price.** The pricing page, the FAQ (visible and structured data),
  the feature list, `llms.txt` and `llms-full.txt` now say US$19.99 once or US$1.99 a month per
  installation, with the Connections checkout links, instead of "by separate license". Free
  for personal and other noncommercial use, unchanged.
- **Version 0.10.0** in the JSON-LD, the hero eyebrow and the closing line, synced from the
  published release.

## 2026-09-17

### Changed

- **Removed every em-dash from the visible copy.** A standing style rule that had never been
  applied to the pages already published. Each one became the punctuation that fits its
  sentence, and the rewrite was gated on the page's word-stream being identical afterwards,
  so only punctuation moved.
- **Shortened the long paragraphs.** Every visible paragraph is now under 40 words. No fact
  left the page; the second and third sentences did. The long-form still lives in `llms.txt`,
  `llms-full.txt` and the FAQ structured data.

### Added

- **A copy gate, `scripts/copy-budget.mjs`,** run by CI on every push to the page. Em-dashes
  are a hard zero; page length is a ratchet against a recorded baseline rather than a fixed
  bar, so the page can shrink but cannot creep back.

### Reverted

- **Collapsible page sections, shipped and pulled the same day.** Hiding a section's body
  behind a disclosure left the heading and a small button alone in a tall empty band, because
  the sections keep their own padding. It had been checked by measuring element boxes rather
  than by looking at it. The pages are byte-identical to before that change.

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
