# Title cards

A silent 15.5 s title card video (1920×1080, 30 fps). Every frame is drawn with Canvas2D in `index.html` and captured in headless Chrome. There is no footage and no audio.

- `tokens.js`: size, fps, colours, font, margin, lines and timing. To change the copy, edit `LINES` and wrap the one accent word in `*asterisks*`.
- `index.html`: exposes `window.renderFrame(t)`, `window.DURATION`, `window.FPS` and `window.READY`.
- `render.mjs`: serves this folder on a free port and saves each frame as a PNG.
- `fonts/SpaceGrotesk-700.woff2`: Space Grotesk Bold (SIL Open Font License).

```sh
npm install
node render.mjs --stills   # writes stills/card_N.png, one per card at mid hold
node render.mjs            # writes frames/f%05d.png
ffmpeg -y -framerate 30 -i frames/f%05d.png -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart out/title_cards.mp4
```

To use a Chromium you already have instead of the one puppeteer downloads, set `CHROME_PATH=/path/to/chrome`.
