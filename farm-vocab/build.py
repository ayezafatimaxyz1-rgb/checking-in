"""Render the farm vocabulary lesson to out/farm_vocab.mp4.

python3 build.py            full render
python3 build.py --stills   one still per scene into stills/ (fast check)

Voice: Kokoro (free, runs offline). Point KOKORO_DIR at a folder holding
kokoro-v1.0.onnx and voices-v1.0.bin.
"""
import hashlib
import math
import os
import re
import subprocess
import sys
from multiprocessing import Pool

import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from lesson import CROPS, COVERS, NARRATOR, REP, SCENES

ROOT = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, SR = 1920, 1080, 30, 24000
KOKORO_DIR = os.environ.get('KOKORO_DIR', os.path.join(ROOT, 'kokoro'))
CACHE = os.path.join(ROOT, '.cache')

NAVY = (14, 42, 82)
NAVY2 = (9, 28, 58)
GOLD = (247, 196, 37)
CREAM = (252, 248, 236)
INK = (22, 30, 44)
MUTED = (120, 130, 145)
GREEN = (52, 168, 83)

GROTESK = os.path.join(ROOT, 'fonts', 'SpaceGrotesk-700.ttf')
SANS = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
SANS_B = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
_fonts = {}


def font(path, size):
    key = (path, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(path, size)
    return _fonts[key]


# ---------------------------------------------------------------- timeline

def strip(t):
    return t.replace('**', '')


def expand(scene):
    """Fill in caption / tts / box for repeat beats."""
    first = True
    hints = dict(scene.get('words', []))
    for b in scene['beats']:
        if 'rep' in b:
            w = b['rep']
            b.setdefault('hint', hints.get(w, ''))
            b.setdefault('t', f'Repeat after me: **{w}**' if first else f'Say it: **{w}**')
            b.setdefault('tts', f'Repeat after me. {w}.' if first else f'{w}.')
            b.setdefault('pause', REP)
            b['chime'] = True
            b['box'] = ('REPEAT AFTER ME', w, b['hint'])
            b['speed'] = 0.82
            first = False
        b.setdefault('pause', 0.35)
        b.setdefault('tts', strip(b['t']))


_kokoro = None


def tts(text, voice, speed):
    os.makedirs(CACHE, exist_ok=True)
    key = hashlib.sha1(f'{voice}|{speed}|{text}'.encode()).hexdigest()[:16]
    path = os.path.join(CACHE, key + '.wav')
    if not os.path.exists(path):
        global _kokoro
        if _kokoro is None:
            from kokoro_onnx import Kokoro
            _kokoro = Kokoro(os.path.join(KOKORO_DIR, 'kokoro-v1.0.onnx'),
                             os.path.join(KOKORO_DIR, 'voices-v1.0.bin'))
        lang = 'en-gb' if voice.startswith('b') else 'en-us'
        samples, sr = _kokoro.create(text, voice=voice, speed=speed, lang=lang)
        assert sr == SR
        # trim leading/trailing near silence so timing is tight
        idx = np.where(np.abs(samples) > 0.01)[0]
        if len(idx):
            samples = samples[max(0, idx[0] - 600): idx[-1] + 2400]
        sf.write(path, samples, SR)
    data, _ = sf.read(path, dtype='float32')
    return data


def build_timeline():
    t = 0.0
    for s in SCENES:
        expand(s)
        cur = 0.45
        for b in s['beats']:
            b['audio'] = tts(b['tts'], b.get('v', NARRATOR), b.get('speed', 0.9))
            b['start'] = cur
            b['speak_end'] = cur + len(b['audio']) / SR
            b['end'] = b['speak_end'] + b['pause']
            cur = b['end']
        dur = cur + 0.5
        s['frames'] = int(math.ceil(dur * FPS))
        s['dur'] = s['frames'] / FPS
        s['t0'] = t
        t += s['dur']
    return t


def chime():
    n = int(0.45 * SR)
    x = np.arange(n) / SR
    env = np.exp(-x * 9)
    tone = 0.5 * np.sin(2 * np.pi * 880 * x) + 0.3 * np.sin(2 * np.pi * 1320 * x)
    return (tone * env * 0.22).astype(np.float32)


def build_audio(total, path):
    out = np.zeros(int(total * SR) + SR, dtype=np.float32)
    ding = chime()
    for s in SCENES:
        for b in s['beats']:
            a = b['audio']
            i = int((s['t0'] + b['start']) * SR)
            out[i:i + len(a)] += a
            if b.get('chime'):
                j = int((s['t0'] + b['speak_end'] + 0.08) * SR)
                out[j:j + len(ding)] += ding
    out = out[:int(total * SR)]
    peak = np.max(np.abs(out)) or 1
    out = out / peak * 0.89
    sf.write(path, out, SR)


# ---------------------------------------------------------------- images

_src = None
_img_cache = {}


def src():
    global _src
    if _src is None:
        _src = Image.open(os.path.join(ROOT, 'source.png')).convert('RGB')
    return _src


def crop(key):
    """'plough' or 'q:plough' (labels covered with a ? tag)."""
    if key in _img_cache:
        return _img_cache[key]
    quiz = key.startswith('q:')
    name = key[2:] if quiz else key
    im = src().copy()
    if quiz:
        d = ImageDraw.Draw(im)
        for (l, t, r, b) in COVERS.get(name, []):
            d.rounded_rectangle((l, t, r, b), radius=8, fill=NAVY, outline=CREAM, width=2)
            f = font(GROTESK, int((b - t) * 0.75))
            d.text(((l + r) / 2, (t + b) / 2), '?', font=f, fill=GOLD, anchor='mm')
    im = im.crop(CROPS[name])
    _img_cache[key] = im
    return im


_bg_cache = {}


def background(key):
    if key not in _bg_cache:
        im = crop(key.replace('q:', '')).resize((W // 4, H // 4), Image.BILINEAR)
        im = im.filter(ImageFilter.GaussianBlur(6)).resize((W, H), Image.BILINEAR)
        dark = Image.new('RGB', (W, H), NAVY2)
        _bg_cache[key] = Image.blend(im, dark, 0.62)
    return _bg_cache[key]


_card_cache = {}


def card_source(key, bw, bh):
    """Panel scaled to contain-fit (bw, bh), at 1.12x for zoom headroom."""
    ck = (key, bw, bh)
    if ck not in _card_cache:
        im = crop(key)
        sc = min(bw / im.width, bh / im.height)
        cw, ch = int(im.width * sc), int(im.height * sc)
        big = im.resize((int(cw * 1.12), int(ch * 1.12)), Image.LANCZOS)
        big = big.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
        mask = Image.new('L', (cw, ch), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, cw - 1, ch - 1), radius=22, fill=255)
        _card_cache[ck] = (big, cw, ch, mask)
    return _card_cache[ck]


def card(key, bw, bh, zoom):
    big, cw, ch, mask = card_source(key, bw, bh)
    # zoom 0 shows the whole panel, 1 shows it at 1.12x around the centre
    k = 1 + 0.07 * zoom
    ww, wh = big.width / k, big.height / k
    x0, y0 = (big.width - ww) / 2, (big.height - wh) / 2
    return big.resize((cw, ch), Image.BILINEAR, box=(x0, y0, x0 + ww, y0 + wh)), mask


# ---------------------------------------------------------------- drawing helpers

def ease(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def wrap(text, f, width):
    words, lines, line = text.split(), [], ''
    for w in words:
        trial = (line + ' ' + w).strip()
        if f.getlength(strip(trial)) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def rich_line(d, x, y, line, f, fill, accent, anchor_center=None):
    """Draw a line with **gold** segments. Bold markers may span lines, so state is tracked by caller."""
    parts = re.split(r'(\*\*)', line)
    segs, on = [], False
    for p in parts:
        if p == '**':
            on = not on
        elif p:
            segs.append((p, on))
    total = sum(f.getlength(p) for p, _ in segs)
    if anchor_center is not None:
        x = anchor_center - total / 2
    for p, on in segs:
        d.text((x, y), p, font=f, fill=accent if on else fill)
        x += f.getlength(p)


def split_rich(text, f, width):
    lines = wrap(text, f, width)
    out, open_ = [], False
    for ln in lines:
        s = ('**' if open_ else '') + ln
        n = ln.count('**')
        if open_ ^ (n % 2 == 1):
            s += '**'
            open_ = True
        else:
            open_ = False
        out.append(s)
    return out


def shadow_box(base, xy, radius, fill, alpha=235, shadow=True):
    x0, y0, x1, y1 = [int(v) for v in xy]
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    if shadow:
        d.rounded_rectangle((x0 + 6, y0 + 10, x1 + 6, y1 + 10), radius, fill=(0, 0, 0, 90))
        layer = layer.filter(ImageFilter.GaussianBlur(10))
        d = ImageDraw.Draw(layer)
    d.rounded_rectangle((x0, y0, x1, y1), radius, fill=fill + (alpha,))
    base.alpha_composite(layer)


def active_beat(scene, t):
    cur = None
    for b in scene['beats']:
        if b['start'] <= t:
            cur = b
    return cur


def current_value(scene, t, key, default=None):
    v = default
    for b in scene['beats']:
        if b['start'] <= t and key in b:
            v = b[key]
    return v


# ---------------------------------------------------------------- static layers (per scene)

def top_bar(layer, step_n):
    d = ImageDraw.Draw(layer)
    d.rectangle((0, 0, W, 78), fill=NAVY2 + (230,))
    d.rectangle((0, 76, W, 80), fill=GOLD + (255,))
    f = font(GROTESK, 34)
    d.text((60, 39), 'FARM ENGLISH', font=f, fill=GOLD, anchor='lm')
    x = 60 + f.getlength('FARM ENGLISH') + 22
    d.text((x, 41), 'The Journey of Wheat: From Field to Market', font=font(SANS, 28), fill=CREAM, anchor='lm')
    # progress dots
    for i in range(11):
        cx = W - 60 - (10 - i) * 52
        n = i + 1
        if step_n and n == step_n:
            d.ellipse((cx - 22, 17, cx + 22, 61), fill=GOLD)
            d.text((cx, 40), str(n), font=font(GROTESK, 24), fill=NAVY2, anchor='mm')
        elif step_n and n < step_n:
            d.ellipse((cx - 17, 22, cx + 17, 56), fill=CREAM)
            d.text((cx, 40), str(n), font=font(GROTESK, 19), fill=NAVY, anchor='mm')
        else:
            d.ellipse((cx - 17, 22, cx + 17, 56), outline=CREAM, width=2)
            d.text((cx, 40), str(n), font=font(GROTESK, 19), fill=CREAM, anchor='mm')


def caption_band(frame, text, alpha):
    if not text:
        return
    f = font(SANS_B, 42)
    lines = split_rich(text, f, 1640)
    lh = 54
    h = len(lines) * lh + 40
    y0 = H - 36 - h
    layer = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((90, y0, W - 90, H - 36), 20, fill=(6, 14, 30, int(215 * alpha)))
    a = int(255 * alpha)
    for i, ln in enumerate(lines):
        rich_line(d, 0, y0 + 20 + i * lh, ln, f, (255, 255, 255, a), GOLD + (a,), anchor_center=W / 2)
    frame.alpha_composite(layer)


def info_box(frame, xy, label, big, small, countdown, align_center=False):
    x0, y0, x1, y1 = xy
    shadow_box(frame, xy, 26, CREAM, 245)
    d = ImageDraw.Draw(frame)
    lf = font(GROTESK, 28)
    lw = lf.getlength(label) + 40
    lx = (x0 + x1) / 2 - lw / 2 if align_center else x0 + 30
    color = GREEN if label in ('ANSWER', 'MODEL ANSWER') else (GOLD if label != 'DEALER' else (226, 120, 60))
    d.rounded_rectangle((lx, y0 - 22, lx + lw, y0 + 22), 22, fill=color)
    d.text((lx + lw / 2, y0 + 1), label, font=lf, fill=NAVY2, anchor='mm')

    inner = x1 - x0 - 70
    size = 76 if len(big) <= 18 else (58 if len(big) <= 34 else 46)
    bf = font(GROTESK, size)
    lines = wrap(big, bf, inner)
    while len(lines) > 2 and size > 34:
        size -= 4
        bf = font(GROTESK, size)
        lines = wrap(big, bf, inner)
    lh = int(size * 1.12)
    sf_ = font(SANS, 34)
    block = len(lines) * lh + (50 if small else 0)
    y = (y0 + y1) / 2 - block / 2 + 4
    for ln in lines:
        if align_center:
            d.text(((x0 + x1) / 2, y), ln, font=bf, fill=NAVY, anchor='ma')
        else:
            d.text((x0 + 36, y), ln, font=bf, fill=NAVY)
        y += lh
    if small:
        if align_center:
            d.text(((x0 + x1) / 2, y + 8), small, font=sf_, fill=MUTED, anchor='ma')
        else:
            d.text((x0 + 36, y + 8), small, font=sf_, fill=MUTED)
    if countdown is not None:
        bx0, bx1, by = x0 + 36, x1 - 36, y1 - 26
        d.rounded_rectangle((bx0, by, bx1, by + 10), 5, fill=(225, 220, 205))
        d.rounded_rectangle((bx0, by, bx0 + max(10, (bx1 - bx0) * (1 - countdown)), by + 10), 5, fill=GOLD)
        pf = font(GROTESK, 24)
        pw = pf.getlength('YOUR TURN') + 36
        pulse = 0.5 + 0.5 * math.sin(countdown * math.pi * 6)
        col = tuple(int(GOLD[k] * (0.75 + 0.25 * pulse) + NAVY[k] * 0) for k in range(3))
        d.rounded_rectangle((x1 - 24 - pw, y0 + 20, x1 - 24, y0 + 62), 21, fill=col)
        d.text((x1 - 24 - pw / 2, y0 + 41), 'YOUR TURN', font=pf, fill=NAVY2, anchor='mm')


def countdown_for(beat, t):
    if beat and beat.get('chime') and t >= beat['speak_end']:
        span = beat['end'] - beat['speak_end']
        return min(1.0, (t - beat['speak_end']) / span)
    return None


# ---------------------------------------------------------------- scene renderers

def paste_card(frame, key, box, zoom, prev=None, mix=1.0):
    bx, by, bw, bh = box
    im, mask = card(key, bw, bh, zoom)
    if prev and mix < 1:
        pim, pmask = card(prev, bw, bh, zoom)
        if pim.size == im.size:
            im = Image.blend(pim, im, mix)
    x = bx + (bw - im.width) // 2
    y = by + (bh - im.height) // 2
    sh = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x + 6, y + 12, x + im.width + 6, y + im.height + 12), 24, fill=(0, 0, 0, 120))
    frame.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    frame.paste(im, (x, y), mask)
    ImageDraw.Draw(frame).rounded_rectangle((x, y, x + im.width - 1, y + im.height - 1), 22, outline=CREAM + (255,), width=4)
    return x, y, im.width, im.height


def image_state(scene, t):
    """(current key, previous key, crossfade 0..1)."""
    cur, prev, at = scene['img'], None, -10
    for b in scene['beats']:
        if 'img' in b and b['start'] <= t:
            prev, cur, at = cur, b['img'], b['start']
    mix = ease((t - at) / 0.4)
    return cur, (prev if mix < 1 else None), mix


def render_step(scene, t, static):
    key, prev, mix = image_state(scene, t)
    frame = background(key.replace('q:', '')).convert('RGBA')
    frame.alpha_composite(static)
    paste_card(frame, key, (60, 112, 1160, 540), t / scene['dur'], prev, mix)

    beat = active_beat(scene, t)
    d = ImageDraw.Draw(frame)
    # word list on the right
    done = set()
    active = None
    for b in scene['beats']:
        if 'rep' in b and b['start'] <= t:
            if t < b['end']:
                active = b['rep']
            else:
                done.add(b['rep'])
    y = 345
    for w, hint in scene['words']:
        on = w == active
        fill = GOLD if on else (CREAM if w in done else (255, 255, 255))
        alpha = 255 if (on or w in done) else 150
        x0, x1 = 1270, 1860
        d.rounded_rectangle((x0, y, x1, y + 70), 18, fill=fill + (alpha,))
        d.text((x0 + 26, y + 35), w, font=font(GROTESK, 34), fill=NAVY2, anchor='lm')
        if w in done and not on:
            d.ellipse((x1 - 52, y + 17, x1 - 16, y + 53), fill=GREEN)
            d.line((x1 - 43, y + 36, x1 - 36, y + 43, x1 - 25, y + 28), fill=(255, 255, 255), width=4)
        elif on:
            d.text((x1 - 22, y + 35), hint, font=font(SANS, 22), fill=NAVY, anchor='rm')
        y += 84

    if beat and 'rep' in beat and t < beat['end']:
        label, big, small = beat['box']
        cd = countdown_for(beat, t)
    else:
        label, big, small = scene['box']
        cd = countdown_for(beat, t)
    info_box(frame, (60, 690, 1220, 880), label, big, small, cd)
    caption_band(frame, beat['t'] if beat else '', 1.0)
    return frame


def render_center(scene, t, static):
    key, prev, mix = image_state(scene, t)
    frame = background(key.replace('q:', '')).convert('RGBA')
    frame.alpha_composite(static)
    paste_card(frame, key, (260, 112, 1400, 520), t / scene['dur'], prev, mix)
    beat = active_beat(scene, t)
    box = current_value(scene, t, 'box', scene['box'])
    info_box(frame, (260, 680, 1660, 880), box[0], box[1], box[2], countdown_for(beat, t), align_center=True)
    caption_band(frame, beat['t'] if beat else '', 1.0)
    return frame


def render_list(scene, t, static):
    frame = background(scene['img']).convert('RGBA')
    frame.alpha_composite(static)
    d = ImageDraw.Draw(frame)
    shown = -1
    cur = None
    for b in scene['beats']:
        if 'item' in b and b['start'] <= t:
            shown = max(shown, b['item'])
            cur = b['item'] if t < b['end'] + 0.2 else cur
    review = scene['kind'] == 'review'
    items = scene['items']
    if review:
        cols, rows = 2, 6
        for i, (head, sub) in enumerate(items):
            if i > shown:
                continue
            c, r = i // rows, i % rows
            x0 = 120 + c * 850
            y0 = 260 + r * 92
            a = ease((t - next(b['start'] for b in scene['beats'] if b.get('item') == i)) / 0.3)
            on = i == cur
            d.rounded_rectangle((x0, y0, x0 + 820, y0 + 78), 18, fill=(GOLD if on else CREAM) + (int(255 * a),))
            d.ellipse((x0 + 18, y0 + 22, x0 + 52, y0 + 56), fill=GREEN + (int(255 * a),))
            d.line((x0 + 27, y0 + 40, x0 + 34, y0 + 47, x0 + 45, y0 + 31), fill=(255, 255, 255, int(255 * a)), width=4)
            hf = font(GROTESK, 34)
            d.text((x0 + 70, y0 + 39), head, font=hf, fill=NAVY2 + (int(255 * a),), anchor='lm')
            d.text((x0 + 80 + hf.getlength(head), y0 + 41), '  ' + sub, font=font(SANS, 29),
                   fill=INK + (int(255 * a),), anchor='lm')
    else:
        dialogue = items[0][0] in ('Dealer', 'Farmer')
        y = 255
        for i, (head, sub) in enumerate(items):
            if i > shown:
                continue
            start = next(b['start'] for b in scene['beats'] if b.get('item') == i)
            a = ease((t - start) / 0.3)
            on = i == cur
            hf = font(GROTESK, 34)
            sf_ = font(SANS, 36)
            if dialogue:
                left = head == 'Dealer'
                lines = wrap(sub, sf_, 1100)
                h = 30 + len(lines) * 44 + 20
                x0 = 150 if left else W - 150 - 1240
                col = (226, 120, 60) if left else GREEN
                d.rounded_rectangle((x0, y, x0 + 1240, y + h), 22,
                                    fill=(255, 255, 255) + (int(255 * a),) if not on else CREAM + (int(255 * a),),
                                    outline=col + (int(255 * a),) if on else None, width=4)
                d.text((x0 + 24, y + h / 2), head.upper(), font=font(GROTESK, 24), fill=col + (int(255 * a),), anchor='lm')
                for j, ln in enumerate(lines):
                    d.text((x0 + 150, y + 22 + j * 44), ln, font=sf_, fill=INK + (int(255 * a),))
                y += h + 14
            else:
                tag = head if len(head) > 2 else head
                tw = hf.getlength(tag) + 40 if len(head) > 2 else 64
                lines = wrap(sub, sf_, 1560 - tw)
                h = 24 + len(lines) * 44 + 16
                x0 = 150
                d.rounded_rectangle((x0, y, W - 150, y + h), 20,
                                    fill=(GOLD if on else CREAM) + (int(255 * a),))
                d.text((x0 + 24, y + 22), tag, font=hf, fill=NAVY2 + (int(255 * a),))
                for j, ln in enumerate(lines):
                    d.text((x0 + tw + 20, y + 24 + j * 44), ln, font=sf_, fill=INK + (int(255 * a),))
                y += h + 16
    beat = active_beat(scene, t)
    caption_band(frame, beat['t'] if beat else '', 1.0)
    return frame


def render_title(scene, t, static):
    frame = background('title').convert('RGBA')
    frame.alpha_composite(static)
    paste_card(frame, 'title', (510, 140, 900, 540), t / scene['dur'])
    d = ImageDraw.Draw(frame)
    if scene.get('outro'):
        d.text((W / 2, 720), 'Well done!', font=font(GROTESK, 80), fill=GOLD, anchor='mm')
        d.text((W / 2, 800), 'Homework: tell someone the journey of wheat.', font=font(SANS, 40), fill=CREAM, anchor='mm')
    else:
        d.text((W / 2, 720), 'Farm Vocabulary & Speaking', font=font(GROTESK, 76), fill=GOLD, anchor='mm')
        d.text((W / 2, 800), '11 steps  ·  50+ words  ·  role play  ·  quiz', font=font(SANS, 40), fill=CREAM, anchor='mm')
    beat = active_beat(scene, t)
    caption_band(frame, beat['t'] if beat else '', 1.0)
    return frame


def make_static(scene):
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    top_bar(layer, scene.get('n'))
    d = ImageDraw.Draw(layer)
    if scene['kind'] == 'step':
        d.ellipse((1270, 120, 1370, 220), fill=GOLD)
        d.text((1320, 171), str(scene['n']), font=font(GROTESK, 58), fill=NAVY2, anchor='mm')
        d.text((1390, 128), f'STEP {scene["n"]} OF 11', font=font(SANS_B, 26), fill=GOLD)
        f = font(GROTESK, 50)
        lines = wrap(scene['title'], f, 470)
        for i, ln in enumerate(lines):
            d.text((1390, 160 + i * 56), ln, font=f, fill=(255, 255, 255))
        d.text((1270, 300), 'KEY WORDS', font=font(SANS_B, 26), fill=GOLD)
    elif scene['kind'] in ('list', 'review'):
        d.text((W / 2, 170), scene['heading'], font=font(GROTESK, 64), fill=(255, 255, 255), anchor='mm')
        d.rectangle((W / 2 - 60, 212, W / 2 + 60, 218), fill=GOLD)
    return layer


RENDER = {'step': render_step, 'center': render_center, 'list': render_list,
          'review': render_list, 'title': render_title}


def render_frame(scene, static, t):
    frame = RENDER[scene['kind']](scene, t, static)
    # fade in from / out to navy at scene edges
    edge = min(t / 0.35, (scene['dur'] - t) / 0.35, 1.0)
    if edge < 1:
        frame = Image.blend(Image.new('RGBA', (W, H), NAVY2 + (255,)), frame, max(0.0, edge))
    return frame.convert('RGB')


def render_scene(i):
    scene = SCENES[i]
    static = make_static(scene)
    path = os.path.join(CACHE, f'scene_{i:02d}.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                          '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'medium',
                          '-crf', '20', '-pix_fmt', 'yuv420p', path], stdin=subprocess.PIPE)
    for f in range(scene['frames']):
        p.stdin.write(render_frame(scene, static, f / FPS).tobytes())
    p.stdin.close()
    p.wait()
    return path


def init_worker(scenes):
    SCENES[:] = scenes


def main():
    total = build_timeline()
    print(f'{len(SCENES)} scenes, {total:.1f}s ({total / 60:.1f} min)')
    if '--stills' in sys.argv:
        os.makedirs(os.path.join(ROOT, 'stills'), exist_ok=True)
        for i, s in enumerate(SCENES):
            static = make_static(s)
            pick = next((b for b in s['beats'] if 'rep' in b or 'item' in b or b.get('chime')), s['beats'][-1])
            t = pick['speak_end'] + (0.6 if 'rep' in pick or pick.get('chime') else 0.3)
            if s['kind'] in ('list', 'review'):
                t = s['beats'][-1]['start'] + 0.5
            render_frame(s, static, t).save(os.path.join(ROOT, 'stills', f'scene_{i:02d}.png'))
        return
    out = os.path.join(ROOT, 'out')
    os.makedirs(out, exist_ok=True)
    wav = os.path.join(CACHE, 'voice.wav')
    build_audio(total, wav)
    with Pool(os.cpu_count(), initializer=init_worker, initargs=(SCENES,)) as pool:
        paths = pool.map(render_scene, range(len(SCENES)), chunksize=1)
    lst = os.path.join(CACHE, 'list.txt')
    with open(lst, 'w') as fh:
        fh.writelines(f"file '{p}'\n" for p in paths)
    final = os.path.join(out, 'farm_vocab.mp4')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-i', wav,
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', final],
                   check=True)
    print('wrote', final)


if __name__ == '__main__':
    main()
