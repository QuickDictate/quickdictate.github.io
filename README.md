# quickdictate.github.io

The website for **QuickDictate**, a tiny Windows tray app that turns your voice into text
anywhere you can type using your choice of cloud or fully offline speech recognition.
This repo is just the site; the app lives in its own repo.

- **Live:** https://quickdictate.lunarwerx.com/
- **The app:** https://github.com/LunarWerxs/QuickDictate
- **By:** [LunarWerx Studios](https://lunarwerx.com)

[![Discord](https://img.shields.io/badge/Discord-join_the_community-5865F2?logo=discord&logoColor=white)](https://discord.gg/PsWpeNUzhk)

![QuickDictate](assets/og-image.png)

One hand-written `index.html` plus some images. No build step, no dependencies. Edit it
and push to `main`; GitHub Pages redeploys in about a minute.

The link-preview card (`assets/og-image.png`) comes from `tools/og-card.html`; the
regen command is in that file's comment.

This site's own code is MIT licensed (see [LICENSE](LICENSE) and [CHANGELOG.md](CHANGELOG.md)).
The app it describes is PolyForm Noncommercial 1.0.0 as of v0.9.0; see the
[app's LICENSE](https://github.com/LunarWerxs/QuickDictate/blob/main/LICENSE).

## Checks

`scripts/copy-budget.mjs` runs in CI on every push that touches the page, and locally with
`node scripts/copy-budget.mjs`. It enforces two things the owner cares about:

- **No em-dashes in visitor-facing copy.** A hard zero. Use a comma, colon, semicolon or a
  full stop. Dashes inside `<style>` or `<script>` comments are ignored.
- **The page does not quietly grow back.** Length is a ratchet against the baseline in
  `scripts/copy-budget.json`, not a fixed bar, so the page may shrink freely and drift up a
  little. Cut copy on purpose? Re-record it with `node scripts/copy-budget.mjs --update` and
  commit the new baseline.

It measures what a visitor actually reads, so collapsed `<details>`, elements with a `hidden`
attribute and `<noscript>` do not count. A naive word count reads about three times high.

To see a change rather than measure it, use `~/.claude/tools/shot/shotpage.mjs`, which
screenshots the page with the scroll-reveal animations forced to their finished state.
