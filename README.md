# quickdictate.github.io

Source for the **QuickDictate** landing page, served at <https://quickdictate.github.io/>.

QuickDictate is a small Windows tray app for speech-to-text dictation — bring your own
STT API key, press a hotkey, and your words type straight into whatever window has focus.
No subscription, no account, no telemetry.

- **App, source code & releases:** <https://github.com/LunarWerxs/QuickDictate>
- **Maker:** LunarWerx Studios — <https://lunarwerx.com>

## Editing

This is a single static `index.html` plus an `assets/` folder — no build step, no
dependencies, no external network requests. Edit `index.html` and push to `main`;
GitHub Pages redeploys automatically within a minute or so.

`.nojekyll` is present so Pages serves the files verbatim (no Jekyll processing).
