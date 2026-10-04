# Nagasaki at blue hour

A 20 second, 1920×1080, 30 fps view of Nagasaki harbour from Mt. Inasa, drawn entirely with Canvas2D. No footage, no photos, no AI models.

- **Real:** terrain heights from the open Terrarium elevation tiles (AWS Terrain Tiles, `data/terrain.png`, zoom 13), the harbour shape found in that data, the camera position on Mt. Inasa's summit, and the location of the Megami Bridge.
- **Generated:** every city light, road, ship and the bridge lighting. They are placed by a fixed hash using height, slope and distance from the city centre, so they look plausible but do not match real buildings.

```sh
node render.mjs --stills   # stills/t_03.png, t_10.png, t_17.png
node render.mjs            # out/nagasaki.mp4, frames piped straight into ffmpeg
```

Uses puppeteer from the parent folder's `node_modules`. Set `CHROME_PATH` to use an existing Chromium.
