# The 2 minute version: one sentence and one word to repeat per step.
# Render with: LESSON=lesson_short python3 build.py
from lesson import CROPS, COVERS, NARRATOR, step

OUT_NAME = 'farm_vocab_2min'
REP = 2.0   # seconds to say a word back


def s(n, title, img, word, hint, model, *lines):
    beats = [dict(t=l) if isinstance(l, str) else l for l in lines]
    beats.append(dict(rep=word))
    return step(n, title, img, [(word, hint)], model, beats)


SCENES = [
    dict(kind='title', img='title', sub='Listen  ·  Repeat  ·  Speak', beats=[
        dict(t='The journey of **wheat**, from field to market.'),
        dict(t='Listen, and repeat each farm word.', pause=0.2),
    ]),
    s(1, 'Preparing the Land', 'plough', 'plough', 'rhymes with "cow"',
      'First, we plough the field.',
      'First, we prepare the land. A **plough** turns over the soil.',
      dict(img='leveller', t='Then a **land leveller** makes the field flat.')),
    s(2, 'Sowing the Seeds', 'sow', 'seed drill', 'SEED dril',
      'We sow the seeds with a seed drill.',
      'Next, we **sow** the seeds with a **seed drill**.'),
    s(3, 'Adding Fertilizer', 'fert', 'fertilizer', 'FER-ti-lie-zer',
      'We add fertilizer to feed the crop.',
      dict(t='We add **fertilizer**, like urea and DAP, to feed the crop.',
           tts='We add fertilizer, like urea and D. A. P., to feed the crop.')),
    s(4, 'Irrigation', 'irr', 'irrigation', 'ir-ri-GAY-shun',
      'We irrigate the field.',
      'We **irrigate** the field with water from a canal or a tube well.'),
    s(5, 'Crop Growth', 'grow', 'germinate', 'JER-mi-nate',
      'The seeds germinate and grow.',
      'The seeds **germinate**, and the crop grows taller.'),
    s(6, 'Ripening', 'ripe', 'ripe', 'rhymes with "pipe"',
      'The wheat is golden and ripe.',
      'After a few months, the wheat turns golden. It is **ripe**.'),
    s(7, 'Harvesting', 'harv', 'harvest', 'HAR-vest',
      'We harvest the wheat.',
      'We **harvest** the wheat with a **combine harvester**.'),
    s(8, 'Drying', 'dry', 'spread', 'SPRED',
      'We spread the wheat in the sun.',
      'We **spread** the wheat in the sun to dry.'),
    s(9, 'Threshing', 'thresh', 'thresher', 'THRESH-er',
      'The thresher separates the grain.',
      'A **thresher** separates the grain from the straw.'),
    s(10, 'Filling and Transporting', 'fill', 'sack', 'rhymes with "back"',
      'We load the sacks onto a trolley.',
      'We fill the **sacks** and load them onto a trolley.'),
    s(11, 'Selling at the Grain Market', 'market', 'grain market', 'GRAIN MAR-ket',
      'The wheat is weighed and sold.',
      'At the **grain market**, the wheat is weighed and sold.'),
    dict(kind='center', img='ripe', box=('SPEAK', 'Tell the journey of wheat.', 'First ... Then ... Next ... Finally ...'), beats=[
        dict(t="Now it's your turn! Tell the journey of wheat. Use **first**, **then**, **next** and **finally**.",
             pause=3.0, chime=True),
    ]),
    dict(kind='title', img='title', outro=True, sub='From field to market: you did it!', beats=[
        dict(t='Great work! Keep practising your farm English.', pause=0.6),
    ]),
]
