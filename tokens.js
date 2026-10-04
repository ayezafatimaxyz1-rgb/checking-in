// Every constant the renderer needs. Nothing here depends on time or randomness.

export const W = 1920;
export const H = 1080;
export const FPS = 30;

export const COLORS = {
  bg: '#0b0b0f',
  ink: '#f4f2ec',
  accent: '#c8ff3d',
};

export const FONT = {
  family: 'Space Grotesk',
  weight: 700,
  size: 168,          // starting size; a line shrinks only if it would break the margin
  letterSpacing: -3,  // px, tightens the display face a touch
};

export const MARGIN = 144;  // text must stay inside this on every side

// The accent word is wrapped in *asterisks*. Exactly one per line.
export const LINES = [
  'Every frame is *code*',
  'Nothing is *filmed*',
  'Same *input*',
  'Same *pixels*',
  'Render it *free*',
];

export const MOTION = {
  fadeIn: 0.5,   // seconds, while rising
  rise: 40,      // px
  fadeOut: 0.25, // seconds
  lead: 0.6,     // empty frame before the first card
  gap: 0.9,      // empty frame between cards
  tail: 1.0,     // empty frame after the last card
};

export const holdFor = (words) => Math.max(1.2, 0.35 + words / 3.2);
