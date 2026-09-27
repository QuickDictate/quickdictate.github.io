# Screenshotting the page

`scripts/copy-budget.mjs` measures a change; a screenshot shows it. The one catch is motion: a
plain capture can land mid-transition and show sections half faded in.

The page already has a switch for that. Under `prefers-reduced-motion: reduce`, the stylesheet at
the top of `index.html` cuts every animation and transition to near zero, so everything is drawn
in its finished state. Headless Chrome can force that preference. Run from the repo root:

    chrome --headless --force-prefers-reduced-motion --hide-scrollbars \
      --window-size=1280,4000 --screenshot=page.png index.html

Raise the window height until the footer is in frame, and narrow the width (say 390) to check
the phone layout. Do not commit `page.png`.

The Discord badge in the corner waits for the visitor to scroll before it appears, so a
still capture of the top of the page will not show it. That is expected.

The owner's machine also has a helper that does the same thing with a real scroll pass,
`shotpage.mjs`, kept in the shared claude-memory repo under `home/tools/shot/`. It is a
convenience, not a requirement; the command above is enough.
