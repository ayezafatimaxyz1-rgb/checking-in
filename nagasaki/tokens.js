// Scene constants. Everything renderFrame(t) uses comes from here or from the
// terrain file, so the same t always gives the same pixels.

export const W = 1920;
export const H = 1080;
export const FPS = 30;
export const DURATION = 20;

// data/terrain.png is 4 x 6 Terrarium tiles at zoom 13, x 7049..7052, y 3304..3309.
export const TERRAIN = {
  src: 'data/terrain.png',
  zoom: 13,
  tileX0: 7049,
  tileY0: 3304,
  metersPerPixel: 16.07, // at latitude 32.74
};

// Mt. Inasa summit (332 m), found as the highest cell near 32.754 N, 129.849 E.
export const CAMERA = {
  lat: 32.75343,
  lon: 129.84904,
  eyeAboveGround: 18,     // observation deck
  yawStart: 98,           // compass bearing in degrees
  yawEnd: 153,
  hfov: 58,
  horizonY: 0.34 * H,
  near: 200,
  far: 22000,
};

// Megami Bridge, centre of the main span.
export const BRIDGE = { lat: 32.7247, lon: 129.8531, bearing: 100, mainSpan: 480, deck: 64, tower: 170 };

export const FONT = { family: 'Space Grotesk', weight: 700 };
