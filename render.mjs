// Frame capture: node render.mjs          -> frames/f00000.png ...
//                node render.mjs --stills -> stills/card_1.png ... (mid hold of each card)
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const STILLS = process.argv.includes('--stills');
const OUT_DIR = path.join(ROOT, STILLS ? 'stills' : 'frames');

const TYPES = {
  '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.woff2': 'font/woff2', '.css': 'text/css', '.png': 'image/png',
};

const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  const file = path.join(ROOT, rel === '/' ? 'index.html' : rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    res.writeHead(404).end();
    return;
  }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r)); // port 0 = any free port
const { port } = server.address();

// Use puppeteer's own Chrome, or point CHROME_PATH at any Chromium.
const browser = await puppeteer.launch({
  headless: true,
  executablePath: process.env.CHROME_PATH || undefined,
  args: ['--no-sandbox', '--font-render-hinting=none', '--force-color-profile=srgb'],
});

try {
  const page = await browser.newPage();
  page.on('pageerror', (e) => console.error('page error:', e.message));
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${port}/index.html`, { waitUntil: 'load' });
  await page.waitForFunction('window.READY === true', { timeout: 30000 });

  const { duration, fps, stills } = await page.evaluate(() => ({
    duration: window.DURATION, fps: window.FPS, stills: window.CARD_STILLS,
  }));

  fs.rmSync(OUT_DIR, { recursive: true, force: true });
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const grab = (t) => page.evaluate((t) => {
    window.renderFrame(t);
    return document.getElementById('c').toDataURL('image/png');
  }, t);
  const save = (name, dataUrl) =>
    fs.writeFileSync(path.join(OUT_DIR, name), Buffer.from(dataUrl.split(',')[1], 'base64'));

  if (STILLS) {
    for (const [i, t] of stills.entries()) {
      save(`card_${i + 1}.png`, await grab(t));
      console.log(`card ${i + 1} at t=${t.toFixed(3)}s`);
    }
  } else {
    const total = Math.round(duration * fps);
    console.log(`${duration.toFixed(3)}s at ${fps} fps = ${total} frames`);
    for (let i = 0; i < total; i++) {
      save(`f${String(i).padStart(5, '0')}.png`, await grab(i / fps));
      if (i % 60 === 0) process.stdout.write(`\r${i}/${total}`);
    }
    process.stdout.write(`\r${total}/${total}\n`);
  }
} finally {
  await browser.close();
  server.close();
}
