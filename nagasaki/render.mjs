// node render.mjs --stills    -> stills/t_XX.png at a few moments
// node render.mjs             -> out/nagasaki.mp4 (PNG frames piped straight into ffmpeg)
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const STILLS = process.argv.includes('--stills');

const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.woff2': 'font/woff2', '.png': 'image/png' };
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  const file = path.join(ROOT, rel === '/' ? 'index.html' : rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) return res.writeHead(404).end();
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));

const browser = await puppeteer.launch({
  headless: true,
  executablePath: process.env.CHROME_PATH || undefined,
  args: ['--no-sandbox', '--force-color-profile=srgb', '--font-render-hinting=none'],
  protocolTimeout: 600000,
});

try {
  const page = await browser.newPage();
  page.on('pageerror', (e) => console.error('page error:', e.message));
  page.on('console', (m) => console.log('page:', m.text()));
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:${server.address().port}/index.html`);
  await page.waitForFunction('window.READY === true', { timeout: 300000 });
  const { duration, fps, lights } = await page.evaluate(() => ({ duration: window.DURATION, fps: window.FPS, lights: window.LIGHT_COUNT }));
  console.log(`${lights} lights, ${duration}s at ${fps} fps`);

  const grab = (t) => page.evaluate((t) => {
    window.renderFrame(t);
    return document.getElementById('c').toDataURL('image/png');
  }, t).then((u) => Buffer.from(u.split(',')[1], 'base64'));

  if (STILLS) {
    const dir = path.join(ROOT, 'stills');
    fs.mkdirSync(dir, { recursive: true });
    for (const t of [3, 10, 17]) {
      const t0 = Date.now();
      fs.writeFileSync(path.join(dir, `t_${String(t).padStart(2, '0')}.png`), await grab(t));
      console.log(`t=${t}s in ${Date.now() - t0} ms`);
    }
  } else {
    fs.mkdirSync(path.join(ROOT, 'out'), { recursive: true });
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-',
      '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path.join(ROOT, 'out/nagasaki.mp4')],
      { stdio: ['pipe', 'inherit', 'inherit'] });
    const done = new Promise((r, j) => ff.on('close', (c) => (c === 0 ? r() : j(new Error(`ffmpeg exited ${c}`)))));
    const total = Math.round(duration * fps);
    const t0 = Date.now();
    for (let i = 0; i < total; i++) {
      const buf = await grab(i / fps);
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
      if (i % 30 === 0) console.log(`${i}/${total}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
    ff.stdin.end();
    await done;
    console.log(`done ${total} frames in ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
} finally {
  await browser.close();
  server.close();
}
