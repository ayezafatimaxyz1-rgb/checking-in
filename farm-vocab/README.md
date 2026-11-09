# Farm English: The Journey of Wheat

An 11 minute English lesson video (1920×1080, 30 fps, voiced) built from the "Journey of Wheat" infographic in `source.png`. It teaches farm vocabulary and gets the learner speaking.

What is in it:

1. Intro and how to use the video
2. Eleven steps, from preparing the land to selling at the grain market. Each step has narration with extra detail, key words with pronunciation help, "Repeat after me" pauses with a chime and countdown, and a model sentence to say.
3. Role play at the grain market (dealer and farmer voices), then "Your turn" where the learner plays the farmer
4. Speaking tip: sequence words (first, then, next, after a few months, once, finally)
5. Picture quiz: name the machine before the answer appears
6. Speaking questions with model answers
7. Final challenge: tell the whole story, with a model answer
8. Key vocabulary review and outro with homework

Files:

- `lesson.py`: every caption, spoken line, key word, pronunciation hint and crop box. Edit this to change the lesson.
- `build.py`: draws each frame with Pillow, voices the lines with Kokoro, renders scenes in parallel with ffmpeg.
- `fonts/SpaceGrotesk-700.ttf`: Space Grotesk Bold (SIL Open Font License), converted from `../fonts`.

```sh
pip install kokoro-onnx soundfile pillow numpy
mkdir kokoro && cd kokoro
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
cd ..
python3 build.py --stills   # one still per scene in stills/
python3 build.py            # out/farm_vocab.mp4
```

Voices: `af_heart` (teacher), `bm_george` (dealer), `am_michael` (farmer). Voice clips are cached in `.cache/`, so changing one line only re-voices that line.
