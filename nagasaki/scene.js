// Nagasaki at blue hour, seen from Mt. Inasa.
// Terrain heights are real (Terrarium elevation tiles). City lights, bridge and
// ships are generated from those heights with a fixed hash, never Math.random.
import { W, H, FPS, DURATION, TERRAIN, CAMERA, BRIDGE, FONT } from './tokens.js';

const RES = TERRAIN.metersPerPixel;
const TAU = Math.PI * 2;
const clamp = (x, a, b) => (x < a ? a : x > b ? b : x);
const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
const mix = (a, b, t) => a + (b - a) * t;

// ---------- deterministic hashing ----------
function hashU(n) {
  n = Math.imul(n ^ (n >>> 16), 0x7feb352d);
  n = Math.imul(n ^ (n >>> 15), 0x846ca68b);
  return (n ^ (n >>> 16)) >>> 0;
}
const hash = (a, b = 0) => hashU(Math.imul(a, 0x9e3779b1) ^ hashU(b + 0x5bd1e995)) / 4294967296;

function valueNoise(x, y, seed) {
  const xi = Math.floor(x), yi = Math.floor(y);
  const fx = x - xi, fy = y - yi;
  const sx = fx * fx * (3 - 2 * fx), sy = fy * fy * (3 - 2 * fy);
  const h = (i, j) => hash(((xi + i) * 73856093) ^ ((yi + j) * 19349663), seed);
  return mix(mix(h(0, 0), h(1, 0), sx), mix(h(0, 1), h(1, 1), sx), sy);
}

// ---------- geo ----------
const WORLD = 256 * 2 ** TERRAIN.zoom;
const lonToPx = (lon) => (lon + 180) / 360 * WORLD - TERRAIN.tileX0 * 256;
const latToPy = (lat) => {
  const r = lat * Math.PI / 180;
  return (1 - Math.log(Math.tan(r) + 1 / Math.cos(r)) / Math.PI) / 2 * WORLD - TERRAIN.tileY0 * 256;
};

// ---------- terrain ----------
let GW, GH, height, water, waterF, cellR, cellG, cellB, glow;

async function loadTerrain() {
  const blob = await (await fetch(TERRAIN.src)).blob();
  const bmp = await createImageBitmap(blob, { colorSpaceConversion: 'none', premultiplyAlpha: 'none' });
  GW = bmp.width; GH = bmp.height;
  const c = new OffscreenCanvas(GW, GH);
  const g = c.getContext('2d');
  g.drawImage(bmp, 0, 0);
  const px = g.getImageData(0, 0, GW, GH).data;
  const raw = new Float32Array(GW * GH);
  for (let i = 0; i < GW * GH; i++) raw[i] = px[i * 4] * 256 + px[i * 4 + 1] + px[i * 4 + 2] / 256 - 32768;

  // Sea and reclaimed land both sit near 0 m, so call a cell water when most
  // of its 7 x 7 neighbourhood is below 0.5 m.
  const low = new Float32Array((GW + 1) * (GH + 1));
  for (let y = 0; y < GH; y++) {
    let row = 0;
    for (let x = 0; x < GW; x++) {
      row += raw[y * GW + x] < 0.5 ? 1 : 0;
      low[(y + 1) * (GW + 1) + x + 1] = low[y * (GW + 1) + x + 1] + row;
    }
  }
  const R = 3;
  water = new Uint8Array(GW * GH);
  waterF = new Float32Array(GW * GH);
  height = new Float32Array(GW * GH);
  for (let y = 0; y < GH; y++) for (let x = 0; x < GW; x++) {
    const x0 = Math.max(0, x - R), x1 = Math.min(GW, x + R + 1);
    const y0 = Math.max(0, y - R), y1 = Math.min(GH, y + R + 1);
    const s = low[y1 * (GW + 1) + x1] - low[y0 * (GW + 1) + x1] - low[y1 * (GW + 1) + x0] + low[y0 * (GW + 1) + x0];
    const i = y * GW + x;
    waterF[i] = s / ((x1 - x0) * (y1 - y0));
    water[i] = waterF[i] > 0.55 ? 1 : 0;
    height[i] = water[i] ? 0 : Math.max(raw[i], 1.5);
  }
}

const hAt = (x, y) => {
  const xi = clamp(x | 0, 0, GW - 1), yi = clamp(y | 0, 0, GH - 1);
  return height[yi * GW + xi];
};

// ---------- lights ----------
// Struct of arrays: world px, py, absolute height, rgb, phase, switch-on time.
let L = null;
const camPx = lonToPx(CAMERA.lon), camPy = latToPy(CAMERA.lat);

function nearWater(x, y, r) {
  for (let dy = -r; dy <= r; dy += r) for (let dx = -r; dx <= r; dx += r) {
    const xx = x + dx, yy = y + dy;
    if (xx >= 0 && yy >= 0 && xx < GW && yy < GH && water[yy * GW + xx]) return true;
  }
  return false;
}

const PALETTE = [
  // weight, r, g, b
  [0.30, 1.00, 0.62, 0.30], // sodium street light
  [0.26, 1.00, 0.80, 0.55], // warm window
  [0.24, 0.92, 0.95, 1.00], // white LED
  [0.12, 0.75, 0.85, 1.00], // cool LED
  [0.05, 1.00, 0.93, 0.80], // neutral
  [0.015, 1.00, 0.25, 0.22], // red beacon or sign
  [0.015, 0.45, 1.00, 0.65], // green sign
  [0.01, 1.00, 0.35, 0.75], // pink neon
];
const pickColor = (u) => {
  let acc = 0;
  for (const p of PALETTE) { acc += p[0]; if (u < acc) return p; }
  return PALETTE[0];
};

function buildLights() {
  const list = [];
  const push = (x, y, z, r, g, b, on) => list.push(x, y, z, r, g, b, hash(list.length, 9), on);
  const cityPx = lonToPx(129.878), cityPy = latToPy(32.748);

  for (let y = 2; y < GH - 2; y++) for (let x = 2; x < GW - 2; x++) {
    const i = y * GW + x;
    if (water[i]) continue;
    const dx = (x - camPx) * RES, dy = (camPy - y) * RES;
    const dist = Math.hypot(dx, dy);
    if (dist < 350 || dist > 17000) continue;
    const bearing = (Math.atan2(dx, dy) * 180 / Math.PI + 360) % 360;
    if (bearing < 45 || bearing > 205) continue;

    const h = height[i];
    const slope = Math.hypot(height[i + 1] - height[i - 1], height[i + GW] - height[i - GW]) / (2 * RES);
    let d = smooth(250, 60, h);
    d *= 1 - smooth(0.45, 0.9, slope);
    // neighbourhoods, parks and cemeteries at ~500 m scale
    const n = valueNoise(x / 28, y / 28, 1) * 0.65 + valueNoise(x / 9, y / 9, 2) * 0.35;
    d *= smooth(0.28, 0.62, n);
    // denser near the harbour basin and the Urakami valley, sparser on far islands
    const core = Math.hypot((x - cityPx) * RES, (y - cityPy) * RES * 0.6);
    d *= 0.18 + 0.82 * Math.exp(-core / 4200);
    // road-like lines from ridged noise: strings of sodium lamps
    const road = Math.abs(valueNoise(x / 22, y / 22, 3) - 0.5) < 0.022 && h < 200;
    const shore = h < 12 && nearWater(x, y, 3);

    const tries = 3;
    for (let k = 0; k < tries; k++) {
      const u = hash(i, k * 7 + 1);
      let p = d * 0.6;
      if (road) p = Math.max(p, 0.55 * (0.3 + 0.7 * Math.exp(-core / 6000)));
      if (shore) p = Math.max(p, 0.35);
      if (u >= p) continue;
      const jx = x + hash(i, k * 7 + 2), jy = y + hash(i, k * 7 + 3);
      const tall = h < 25 && core < 1800 ? 6 + 55 * hash(i, k * 7 + 4) ** 3 : 3 + 12 * hash(i, k * 7 + 4);
      let c = road ? PALETTE[0] : pickColor(hash(i, k * 7 + 5));
      if (shore && hash(i, k * 7 + 8) < 0.5) c = PALETTE[2];
      let s = 0.3 + 1.2 * hash(i, k * 7 + 6) ** 2 + (hash(i, k * 7 + 10) < 0.04 ? 3 : 0);
      if (shore) s *= 1.6;
      if (road) s *= 1.2;
      const on = hash(i, k * 7 + 7) < 0.72 ? -1 : 7 * hash(i, k * 7 + 9);
      push(jx, jy, h + tall, c[1] * s, c[2] * s, c[3] * s, on);
    }
  }

  // Megami Bridge: towers, deck and stay cables as rows of lamps.
  const bx = lonToPx(BRIDGE.lon), by = latToPy(BRIDGE.lat);
  const br = BRIDGE.bearing * Math.PI / 180;
  const ux = Math.sin(br), uy = -Math.cos(br); // along the deck, in px space
  const along = (m) => [bx + ux * m / RES, by + uy * m / RES];
  const half = BRIDGE.mainSpan / 2, total = 650;
  const deckH = (m) => BRIDGE.deck - 14 * (Math.abs(m) / total) ** 2;
  const bridgeCol = [0.85, 0.92, 1.0];
  for (let m = -total; m <= total; m += 9) {
    const [x, y] = along(m);
    push(x, y, deckH(m), bridgeCol[0] * 1.1, bridgeCol[1] * 1.1, bridgeCol[2] * 1.1, -1);
  }
  for (const side of [-1, 1]) {
    const tm = side * half;
    const [tx, ty] = along(tm);
    for (let z = 0; z <= BRIDGE.tower; z += 2.5) push(tx, ty, z, 1.4, 1.45, 1.5, -1);
    push(tx, ty, BRIDGE.tower + 3, 1.6, 0.25, 0.2, -1); // aviation light
    for (let c = 1; c <= 11; c++) {
      for (const dir of [-1, 1]) {
        const end = tm + dir * c * 21;
        const [ex, ey] = along(end);
        const top = BRIDGE.tower - 8 - c * 2.5;
        for (let s = 0.05; s < 1; s += 0.06) {
          push(mix(tx, ex, s), mix(ty, ey, s), mix(top, deckH(end), s), 0.35, 0.5, 0.75, -1);
        }
      }
    }
  }

  const n = list.length / 8;
  L = { n, data: new Float32Array(list) };
}

// Ground and water pick up a warm cast from nearby lamps.
function buildGlow() {
  const acc = new Float32Array(GW * GH);
  const d = L.data;
  for (let k = 0; k < L.n; k++) {
    const x = d[k * 8] | 0, y = d[k * 8 + 1] | 0;
    if (x >= 0 && y >= 0 && x < GW && y < GH) acc[y * GW + x] += d[k * 8 + 3] + d[k * 8 + 4];
  }
  const tmp = new Float32Array(GW * GH);
  const R = 6;
  for (let pass = 0; pass < 3; pass++) {
    for (let y = 0; y < GH; y++) {
      let s = 0;
      for (let x = -R; x < GW; x++) {
        if (x + R < GW) s += acc[y * GW + x + R];
        if (x - R - 1 >= 0) s -= acc[y * GW + x - R - 1];
        if (x >= 0) tmp[y * GW + x] = s / (2 * R + 1);
      }
    }
    for (let x = 0; x < GW; x++) {
      let s = 0;
      for (let y = -R; y < GH; y++) {
        if (y + R < GH) s += tmp[(y + R) * GW + x];
        if (y - R - 1 >= 0) s -= tmp[(y - R - 1) * GW + x];
        if (y >= 0) acc[y * GW + x] = s / (2 * R + 1);
      }
    }
  }
  glow = new Float32Array(GW * GH);
  for (let i = 0; i < GW * GH; i++) glow[i] = 1 - Math.exp(-acc[i] * 0.9);

  cellR = new Float32Array(GW * GH); cellG = new Float32Array(GW * GH); cellB = new Float32Array(GW * GH);
  for (let y = 1; y < GH - 1; y++) for (let x = 1; x < GW - 1; x++) {
    const i = y * GW + x;
    const gx = (height[i + 1] - height[i - 1]) / (2 * RES), gy = (height[i + GW] - height[i - GW]) / (2 * RES);
    const inv = 1 / Math.hypot(gx, gy, 1);
    const nx = -gx * inv, ny = -gy * inv, nz = inv;
    // sky dome plus a low western afterglow behind the viewer
    const lit = 0.55 + 0.45 * nz + 0.35 * clamp(-nx * 0.8 + ny * 0.1, 0, 1);
    const tex = 0.8 + 0.4 * valueNoise(x / 3, y / 3, 4);
    const gl = glow[i];
    if (water[i]) {
      cellR[i] = 34 * gl; cellG[i] = 22 * gl; cellB[i] = 14 * gl;
    } else {
      cellR[i] = 7 * lit * tex + 30 * gl;
      cellG[i] = 10 * lit * tex + 19 * gl;
      cellB[i] = 15 * lit * tex + 12 * gl;
    }
  }
}

// ---------- frame buffers ----------
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
const img = ctx.createImageData(W, H);
const pix = new Uint32Array(img.data.buffer);
const depth = new Float32Array(W * H);
const isWater = new Uint8Array(W * H);
const acc = new Float32Array(W * H * 3);
const lightCanvas = new OffscreenCanvas(W, H);
const lctx = lightCanvas.getContext('2d');
const limg = lctx.createImageData(W, H);
const ybuf = new Float32Array(W);
const rgba = (r, g, b) => (255 << 24) | (clamp(b, 0, 255) << 16) | (clamp(g, 0, 255) << 8) | clamp(r, 0, 255);

const skyR = new Float32Array(H * 2), skyG = new Float32Array(H * 2), skyB = new Float32Array(H * 2);
function skyRows(t, hy) {
  const dusk = smooth(0, DURATION, t); // the sky keeps darkening through the shot
  for (let y = -H; y < H; y++) {
    const up = clamp((hy - y) / hy, -1, 1.6);
    const a = clamp(up, 0, 1);
    let r = mix(64, 9, Math.pow(a, 0.55)), g = mix(76, 16, Math.pow(a, 0.55)), b = mix(110, 38, Math.pow(a, 0.6));
    const band = Math.exp(-Math.max(0, hy - y) / 70);
    r += 46 * band; g += 30 * band; b += 22 * band; // city light pollution on the haze
    const k = 1 - 0.28 * dusk;
    skyR[y + H] = r * k; skyG[y + H] = g * k; skyB[y + H] = b * (1 - 0.18 * dusk);
  }
}

function camera(t) {
  const u = t / DURATION;
  const e = 0.5 - 0.5 * Math.cos(Math.PI * u);
  const yaw = mix(CAMERA.yawStart, CAMERA.yawEnd, e) * Math.PI / 180;
  const zoom = mix(1, 1.04, u);
  const focal = (W / 2) / Math.tan(CAMERA.hfov * Math.PI / 360) * zoom;
  const camZ = height[(camPy | 0) * GW + (camPx | 0)] + CAMERA.eyeAboveGround;
  return { fx: Math.sin(yaw), fy: Math.cos(yaw), rx: Math.cos(yaw), ry: -Math.sin(yaw), focal, camZ, hy: CAMERA.horizonY };
}

function drawTerrain(t, cam) {
  const { fx, fy, rx, ry, focal, camZ, hy } = cam;
  skyRows(t, hy);
  // sky and stars
  for (let y = 0; y < H; y++) {
    const c = rgba(skyR[y + H], skyG[y + H], skyB[y + H]);
    pix.fill(c, y * W, (y + 1) * W);
  }
  const starsOn = 0.35 + 0.65 * smooth(2, DURATION, t);
  for (let s = 0; s < 700; s++) {
    const sx = (hash(s, 11) * W) | 0, sy = (hash(s, 12) * hy * 0.9) | 0;
    const lum = hash(s, 13) ** 3 * starsOn * (0.85 + 0.15 * Math.sin(t * (3 + 4 * hash(s, 14)) + TAU * hash(s, 15)));
    const i = sy * W + sx;
    const k = clamp((hy - sy) / hy, 0, 1) * 150 * lum;
    pix[i] = rgba(skyR[sy + H] + k, skyG[sy + H] + k, skyB[sy + H] + k * 1.1);
  }
  depth.fill(1e9);
  isWater.fill(0);
  ybuf.fill(H);

  const half = W / 2;
  const fog = (z) => 1 - Math.exp(-z / 10500);
  const fogR = 40, fogG = 50, fogB = 78;
  let z = CAMERA.near;
  while (z < CAMERA.far) {
    const dz = Math.max(1.2, z * 0.0042);
    const f = fog(z);
    const inv = focal / z;
    for (let x = 0; x < W; x++) {
      const u = (x - half) / focal;
      const east = (fx + rx * u) * z, north = (fy + ry * u) * z;
      const gx = camPx + east / RES, gy = camPy - north / RES;
      if (gx < 0 || gy < 0 || gx >= GW - 1 || gy >= GH - 1) continue;
      const xi = gx | 0, yi = gy | 0, tx = gx - xi, ty = gy - yi;
      const i = yi * GW + xi;
      const h = mix(mix(height[i], height[i + 1], tx), mix(height[i + GW], height[i + GW + 1], tx), ty);
      let sy = hy + (camZ - h) * inv;
      if (sy < 0) sy = 0;
      const top = sy | 0;
      const bot = ybuf[x] | 0;
      if (top >= bot) continue;
      let r, g, b;
      const wf = mix(mix(waterF[i], waterF[i + 1], tx), mix(waterF[i + GW], waterF[i + GW + 1], tx), ty);
      const wet = wf > 0.55;
      if (wet) {
        // the sky row this point would mirror, plus Fresnel toward the horizon
        const fres = 0.1 + 0.55 * z / (z + 3500);
        const ripple = 1 + 0.06 * Math.sin(gx * 2.1 + gy * 0.7 + t * 1.6);
        const ry2 = clamp((2 * hy - top) | 0, -H, H - 1) + H;
        r = (6 + skyR[ry2] * fres + cellR[i]) * ripple;
        g = (10 + skyG[ry2] * fres + cellG[i]) * ripple;
        b = (18 + skyB[ry2] * fres + cellB[i]) * ripple;
      } else {
        r = cellR[i]; g = cellG[i]; b = cellB[i];
      }
      r = mix(r, fogR, f); g = mix(g, fogG, f); b = mix(b, fogB, f);
      const c = rgba(r, g, b);
      for (let y = top; y < bot; y++) {
        const p = y * W + x;
        pix[p] = c;
        depth[p] = z;
        isWater[p] = wet ? 1 : 0;
      }
      ybuf[x] = top;
    }
    z += dz;
  }
}

function splat(x, y, r, g, b) {
  if (x < 0 || y < 0 || x >= W - 1 || y >= H - 1) return;
  const xi = x | 0, yi = y | 0, tx = x - xi, ty = y - yi;
  const w00 = (1 - tx) * (1 - ty), w10 = tx * (1 - ty), w01 = (1 - tx) * ty, w11 = tx * ty;
  let p = (yi * W + xi) * 3;
  acc[p] += r * w00; acc[p + 1] += g * w00; acc[p + 2] += b * w00;
  acc[p + 3] += r * w10; acc[p + 4] += g * w10; acc[p + 5] += b * w10;
  p += W * 3;
  acc[p] += r * w01; acc[p + 1] += g * w01; acc[p + 2] += b * w01;
  acc[p + 3] += r * w11; acc[p + 4] += g * w11; acc[p + 5] += b * w11;
}

function drawLight(t, cam, x, y, z, r, g, b, ph, on, reflect) {
  const { fx, fy, rx, ry, focal, camZ, hy } = cam;
  const dx = (x - camPx) * RES, dy = (camPy - y) * RES;
  const zf = dx * fx + dy * fy;
  if (zf < 80) return;
  const inv = focal / zf;
  const sx = W / 2 + (dx * rx + dy * ry) * inv;
  if (sx < -2 || sx > W + 2) return;
  const sy = hy + (camZ - z) * inv;
  let k = 1 / (1 + Math.pow(zf / 1900, 1.45)) * Math.exp(-zf / 30000);
  if (on >= 0) k *= smooth(on, on + 0.8, t);
  if (k <= 0) return;
  k *= 1 + 0.22 * clamp(zf / 7000, 0, 1) * Math.sin(t * (2.5 + 6 * ph) + TAU * ph);
  const px = sx | 0, py = sy | 0;
  if (py >= 0 && py < H && px >= 0 && px < W) {
    const dd = depth[py * W + px];
    if (dd < zf * 0.985 - 25) return; // hidden behind nearer terrain
  }
  splat(sx, sy, r * k, g * k, b * k);

  if (!reflect || zf > 9000) return;
  const yr = hy + (camZ + z) * inv;
  const yi = yr | 0;
  if (yi < 0 || yi >= H || px < 0 || px >= W) return;
  const q = yi * W + px;
  if (!isWater[q] || depth[q] > zf) return;
  const len = clamp((yr - sy) * 0.4, 3, 46);
  const kr = k * 0.38 / Math.sqrt(len);
  for (let s = 0; s < len; s += 1) {
    const yy = yr - len * 0.35 + s;
    const wob = Math.sin(yy * 0.55 + t * 2.3 + TAU * ph) * (0.6 + 1.6 * s / len);
    const xx = sx + wob;
    const qi = (yy | 0) * W + (xx | 0);
    if (yy < 0 || yy >= H - 1 || !isWater[qi]) continue;
    const fall = 1 - Math.abs(s / len - 0.35) * 1.3;
    if (fall <= 0) continue;
    const flick = 0.55 + 0.45 * Math.sin(yy * 1.7 - t * 3.1 + TAU * ph * 3);
    splat(xx, yy, r * kr * fall * flick, g * kr * fall * flick, b * kr * fall * flick);
  }
}

// Three ships moving down the harbour; positions depend only on t.
const SHIPS = [
  { a: [32.7480, 129.8650], b: [32.7330, 129.8590], speed: 0.020, phase: 0.15, size: 1.0 },
  { a: [32.7400, 129.8620], b: [32.7520, 129.8670], speed: 0.016, phase: 0.40, size: 0.6 },
  { a: [32.7320, 129.8575], b: [32.7210, 129.8510], speed: 0.024, phase: 0.55, size: 0.8 },
];
function drawShips(t, cam) {
  SHIPS.forEach((s, si) => {
    const u = s.phase + s.speed * t;
    const ax = lonToPx(s.a[1]), ay = latToPy(s.a[0]), bx = lonToPx(s.b[1]), by = latToPy(s.b[0]);
    const x = mix(ax, bx, u), y = mix(ay, by, u);
    if (!water[(y | 0) * GW + (x | 0)]) return;
    const len = Math.hypot(bx - ax, by - ay);
    const ux = (bx - ax) / len, uy = (by - ay) / len;
    const n = Math.round(14 * s.size);
    for (let k = 0; k < n; k++) {
      const along = (k / (n - 1) - 0.5) * 9 * s.size; // px, about 150 m at full size
      const hgt = 6 + 14 * s.size * hash(si * 100 + k, 21);
      const warm = hash(si * 100 + k, 22) < 0.5;
      drawLight(t, cam, x + ux * along, y + uy * along, hgt, warm ? 1.2 : 1.1, warm ? 0.95 : 1.15, warm ? 0.7 : 1.25, hash(k, si), -1, true);
    }
    drawLight(t, cam, x + ux * 4.6 * s.size, y + uy * 4.6 * s.size, 9, 0.2, 1.4, 0.4, 0.3, -1, true);
    drawLight(t, cam, x + ux * 4.6 * s.size, y + uy * 4.6 * s.size, 32 * s.size, 1.4, 1.4, 1.4, 0.7, -1, true);
  });
}

function drawLights(t, cam) {
  acc.fill(0);
  const d = L.data;
  for (let k = 0; k < L.n; k++) {
    const o = k * 8;
    drawLight(t, cam, d[o], d[o + 1], d[o + 2], d[o + 3], d[o + 4], d[o + 5], d[o + 6], d[o + 7], true);
  }
  drawShips(t, cam);
  const out = limg.data;
  for (let i = 0, p = 0; i < W * H; i++, p += 3) {
    out[i * 4] = 255 * (1 - Math.exp(-acc[p] * 3.2));
    out[i * 4 + 1] = 255 * (1 - Math.exp(-acc[p + 1] * 3.2));
    out[i * 4 + 2] = 255 * (1 - Math.exp(-acc[p + 2] * 3.2));
    out[i * 4 + 3] = 255;
  }
  lctx.putImageData(limg, 0, 0);
}

// ---------- film finish ----------
const grain = [];
function buildGrain() {
  for (let v = 0; v < 6; v++) {
    const c = new OffscreenCanvas(W / 2, H / 2);
    const g = c.getContext('2d');
    const d = g.createImageData(W / 2, H / 2);
    for (let i = 0; i < d.data.length; i += 4) {
      const n = 128 + (hash(i, v + 31) - 0.5) * 90;
      d.data[i] = d.data[i + 1] = d.data[i + 2] = n; d.data[i + 3] = 255;
    }
    g.putImageData(d, 0, 0);
    grain.push(c);
  }
}

function caption(t) {
  const a = smooth(0.8, 2.2, t) * (1 - smooth(6.0, 7.2, t));
  const b = smooth(14.5, 15.8, t) * (1 - smooth(19.3, 19.95, t));
  ctx.save();
  ctx.textBaseline = 'alphabetic';
  ctx.letterSpacing = '6px';
  if (a > 0) {
    ctx.globalAlpha = a;
    ctx.fillStyle = '#f4f2ec';
    ctx.font = `${FONT.weight} 64px "${FONT.family}"`;
    ctx.fillText('NAGASAKI', 144, H - 190 + 12 * (1 - a));
    ctx.font = `${FONT.weight} 26px "${FONT.family}"`;
    ctx.letterSpacing = '3px';
    ctx.globalAlpha = a * 0.75;
    ctx.fillText('FROM MT. INASA · 333 M · BLUE HOUR', 148, H - 144 + 12 * (1 - a));
  }
  if (b > 0) {
    ctx.globalAlpha = b * 0.8;
    ctx.fillStyle = '#f4f2ec';
    ctx.font = `${FONT.weight} 26px "${FONT.family}"`;
    ctx.letterSpacing = '3px';
    ctx.fillText('REAL TERRAIN · GENERATED LIGHTS · NO FOOTAGE', 148, H - 144);
  }
  ctx.restore();
}

function renderFrame(t) {
  const cam = camera(t);
  drawTerrain(t, cam);
  drawLights(t, cam);

  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.globalAlpha = 1;
  ctx.filter = 'none';
  ctx.globalCompositeOperation = 'source-over';
  ctx.putImageData(img, 0, 0);

  ctx.globalCompositeOperation = 'lighter';
  ctx.drawImage(lightCanvas, 0, 0);
  ctx.filter = 'blur(2px)'; ctx.globalAlpha = 0.7; ctx.drawImage(lightCanvas, 0, 0);
  ctx.filter = 'blur(10px)'; ctx.globalAlpha = 0.55; ctx.drawImage(lightCanvas, 0, 0);
  ctx.filter = 'blur(36px)'; ctx.globalAlpha = 0.45; ctx.drawImage(lightCanvas, 0, 0);
  ctx.filter = 'none';

  // vignette
  ctx.globalCompositeOperation = 'source-over';
  ctx.globalAlpha = 1;
  const v = ctx.createRadialGradient(W / 2, H * 0.48, H * 0.35, W / 2, H * 0.48, H * 1.05);
  v.addColorStop(0, 'rgba(0,0,0,0)');
  v.addColorStop(1, 'rgba(0,0,0,0.55)');
  ctx.fillStyle = v;
  ctx.fillRect(0, 0, W, H);

  // grain, picked by frame number so it is the same on every render
  ctx.globalCompositeOperation = 'overlay';
  ctx.globalAlpha = 0.07;
  ctx.drawImage(grain[Math.round(t * FPS) % grain.length], 0, 0, W, H);
  ctx.globalCompositeOperation = 'source-over';
  ctx.globalAlpha = 1;

  caption(t);

  // fade from and to black
  const fade = smooth(0, 0.8, t) * (1 - smooth(DURATION - 0.6, DURATION, t));
  if (fade < 1) {
    ctx.fillStyle = `rgba(0,0,0,${1 - fade})`;
    ctx.fillRect(0, 0, W, H);
  }
}

window.renderFrame = renderFrame;
window.DURATION = DURATION;
window.FPS = FPS;

await document.fonts.load(`${FONT.weight} 64px "${FONT.family}"`);
await document.fonts.ready;
await loadTerrain();
buildLights();
buildGlow();
buildGrain();
window.LIGHT_COUNT = L.n;
renderFrame(0);
window.READY = true;
