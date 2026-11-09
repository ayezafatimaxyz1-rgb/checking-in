# The lesson: every word that is shown or spoken in the video lives here.
#
# Crop boxes are (left, top, right, bottom) in source.png (1672 x 941).
# A beat is one spoken line. Keys:
#   t      caption text. Wrap a key word in **stars** to colour it gold.
#   tts    what the voice says, when it differs from the caption.
#   v      voice name (default NARRATOR).
#   img    switch the picture to another crop key.
#   rep    a word to repeat: shows it big, then a chime and a pause to speak.
#   hint   pronunciation help shown under a repeated or revealed word.
#   box    (label, big text, small text) for the panel under the picture.
#   item   reveal list item N (list scenes).
#   pause  silence after the line, in seconds.

NARRATOR = 'af_heart'
DEALER = 'bm_george'
FARMER = 'am_michael'

CROPS = {
    'title': (0, 0, 410, 242),
    'plough': (415, 0, 787, 190),
    'cultivator': (790, 0, 1105, 190),
    'rotavator': (1108, 0, 1384, 190),
    'leveller': (1387, 0, 1672, 190),
    'sow': (0, 247, 441, 416),
    'fert': (446, 247, 846, 416),
    'irr': (851, 247, 1257, 416),
    'grow': (1262, 247, 1672, 416),
    'ripe': (0, 486, 415, 637),
    'harv': (419, 486, 839, 637),
    'dry': (843, 486, 1267, 637),
    'thresh': (1272, 486, 1672, 637),
    'fill': (3, 700, 489, 832),
    'market': (494, 700, 1021, 842),
    'vocab': (1031, 702, 1670, 886),
}

# Labels and headings that would give a quiz answer away, hidden behind a "?" tag.
COVERS = {
    'plough': [(645, 150, 743, 184)],
    'cultivator': [(967, 150, 1094, 184)],
    'rotavator': [(1244, 150, 1361, 184)],
    'leveller': [(1514, 150, 1658, 184)],
    'sow': [(315, 374, 428, 407), (2, 250, 268, 290)],
    'harv': [(726, 588, 826, 634), (423, 489, 612, 530)],
    'thresh': [(1273, 489, 1468, 530)],
}

REP = 2.4    # seconds of silence to say a word back
ASK = 4.5    # seconds to answer a question


def step(n, title, img, words, model, beats):
    return dict(kind='step', n=n, title=title, img=img, words=words,
                box=('SAY IT', model, ''), beats=beats)


SCENES = [
    dict(kind='title', img='title', beats=[
        dict(t='Welcome to **Farm English**!'),
        dict(t='Today we follow the journey of **wheat**, from the field to the market.'),
        dict(t='You will learn farm vocabulary, and practise speaking about every step.'),
        dict(t='When you see **Repeat after me**, say the word out loud.'),
        dict(t='When you see a **question**, pause and answer in a full sentence.'),
        dict(t="Let's go to the farm!", pause=0.6),
    ]),

    step(1, 'Preparing the Land', 'plough',
         [('cultivation', 'cul-ti-VAY-shun'), ('plough', 'rhymes with "cow"'),
          ('cultivator', 'CUL-ti-vay-tor'), ('rotavator', 'RO-ta-vay-tor'),
          ('land leveller', 'land LEV-el-er')],
         'First, we plough the field. Then we level it.', [
        dict(t='Step one. **Preparing the land.**'),
        dict(t='First, we prepare the land for **cultivation**. Cultivation means growing crops.'),
        dict(rep='cultivation'),
        dict(t='We use a tractor with a **plough**. A plough turns over the soil and brings fresh soil to the top.'),
        dict(rep='plough'),
        dict(img='cultivator', t='Next, the **cultivator** loosens the soil and pulls out old roots and weeds.'),
        dict(rep='cultivator'),
        dict(img='rotavator', t='Then, the **rotavator** breaks the soil into finer pieces. Its blades spin very fast.'),
        dict(rep='rotavator'),
        dict(img='leveller', t='Finally, we level the field with a **land leveller**. On a flat field, water spreads evenly.'),
        dict(rep='land leveller'),
        dict(t='Say it: First, we plough the field. Then we level it.', pause=REP),
    ]),

    step(2, 'Sowing the Seeds', 'sow',
         [('sow', 'rhymes with "go"'), ('seed drill', 'SEED dril'), ('row', 'rhymes with "go"')],
         'We sow the seeds with a seed drill.', [
        dict(t='Step two. **Sowing the seeds.**'),
        dict(t='Once the land is ready, we **sow** the wheat seeds using a **seed drill**.'),
        dict(rep='sow'),
        dict(t='A seed drill places the seeds at the right depth and distance, in neat **rows**.'),
        dict(rep='seed drill'),
        dict(rep='row'),
        dict(t='In Pakistan and India, farmers usually sow wheat in **October or November**, when the weather turns cool.'),
        dict(t='Say it: We sow the seeds with a seed drill.', pause=REP),
    ]),

    step(3, 'Adding Fertilizer', 'fert',
         [('fertilizer', 'FER-ti-lie-zer'), ('urea', 'yoo-REE-a'), ('nutrients', 'NEW-tree-ents'),
          ('apply', 'a-PLY')],
         'We apply urea to give the crop nutrients.', [
        dict(t='Step three. **Adding fertilizer.**'),
        dict(t='Plants need food to grow strong. Plant food is called **fertilizer**.'),
        dict(rep='fertilizer'),
        dict(t='We **apply** fertilizers such as DAP and **urea**. They give **nutrients** to the crop.',
             tts='We apply fertilizers such as D. A. P. and urea. They give nutrients to the crop.'),
        dict(rep='urea'),
        dict(rep='nutrients'),
        dict(t='Here, the farmer spreads the fertilizer by hand across the field.'),
        dict(rep='apply'),
        dict(t='Say it: We apply urea to give the crop nutrients.', pause=REP),
    ]),

    step(4, 'Irrigation', 'irr',
         [('irrigation', 'ir-ri-GAY-shun'), ('irrigate', 'IR-ri-gate'), ('canal', 'ka-NAL'),
          ('tube well', 'TYOOB wel')],
         'We irrigate the field with canal water.', [
        dict(t='Step four. **Irrigation.**'),
        dict(t='**Irrigation** means supplying water to the field.'),
        dict(rep='irrigation'),
        dict(t='We **irrigate** the field when necessary. The water comes from a **canal** or a **tube well**.'),
        dict(rep='irrigate'),
        dict(rep='canal'),
        dict(t='A tube well pumps water up from under the ground, like in this picture.'),
        dict(rep='tube well'),
        dict(t='Say it: We irrigate the field with canal water.', pause=REP),
    ]),

    step(5, 'Crop Growth', 'grow',
         [('germinate', 'JER-mi-nate'), ('gradually', 'GRAD-joo-a-lee'), ('weeds', 'WEEDZ'),
          ('insects', 'IN-sekts')],
         'The seeds germinate and the crop grows taller.', [
        dict(t='Step five. **Crop growth.**'),
        dict(t='The seeds **germinate**, and small green plants appear.'),
        dict(rep='germinate'),
        dict(t='**Gradually**, the crop grows taller.'),
        dict(rep='gradually'),
        dict(t='We also control **weeds** and protect the crop from **insects**.'),
        dict(rep='weeds'),
        dict(rep='insects'),
        dict(t='Say it: The seeds germinate and the crop grows taller.', pause=REP),
    ]),

    step(6, 'Ripening', 'ripe',
         [('ripe', 'rhymes with "pipe"'), ('golden', 'GOHL-den'), ('mature', 'ma-CHOOR')],
         'The wheat turns golden when it is ripe.', [
        dict(t='Step six. **Ripening.**'),
        dict(t='After a few months, the wheat turns **golden** and becomes fully **mature**.'),
        dict(rep='golden'),
        dict(rep='mature'),
        dict(t='Now it is **ripe** and ready for harvesting. In Pakistan this is usually in **April**.'),
        dict(rep='ripe'),
        dict(t='Say it: The wheat turns golden when it is ripe.', pause=REP),
    ]),

    step(7, 'Harvesting', 'harv',
         [('harvest', 'HAR-vest'), ('reaper', 'REE-per'), ('combine harvester', 'KOM-bine HAR-ves-ter')],
         'We harvest the wheat with a combine harvester.', [
        dict(t='Step seven. **Harvesting.**'),
        dict(t='To **harvest** means to cut the crop.'),
        dict(rep='harvest'),
        dict(t='We harvest the wheat using a **reaper** or a **combine harvester**.'),
        dict(rep='reaper'),
        dict(t='A combine harvester cuts the crop and separates the grains, all in one machine.'),
        dict(rep='combine harvester'),
        dict(t='Say it: We harvest the wheat with a combine harvester.', pause=REP),
    ]),

    step(8, 'Drying', 'dry',
         [('spread', 'SPRED'), ('courtyard', 'KORT-yard'), ('rake', 'rhymes with "cake"'),
          ('rot', 'rhymes with "hot"')],
         'We spread the wheat in the sun to dry.', [
        dict(t='Step eight. **Drying.**'),
        dict(t='We **spread** the harvested wheat in the **courtyard** and leave it in the sun to dry.'),
        dict(rep='spread'),
        dict(rep='courtyard'),
        dict(t='The farmer uses a **rake** to turn the grain, so it dries evenly.'),
        dict(rep='rake'),
        dict(t='Dry grain does not **rot**, so it is safe to store.'),
        dict(rep='rot'),
        dict(t='Say it: We spread the wheat in the sun to dry.', pause=REP),
    ]),

    step(9, 'Threshing', 'thresh',
         [('thresher', 'THRESH-er'), ('grain', 'rhymes with "rain"'), ('straw', 'rhymes with "saw"')],
         'The thresher separates the grain from the straw.', [
        dict(t='Step nine. **Threshing.**'),
        dict(t='Once the wheat is dry, we use a **thresher**.'),
        dict(rep='thresher'),
        dict(t='A thresher separates the **grains** from the **straw**.'),
        dict(rep='grain'),
        dict(rep='straw'),
        dict(t='The straw is not wasted. Farmers use it as food for their animals.'),
        dict(t='Say it: The thresher separates the grain from the straw.', pause=REP),
    ]),

    step(10, 'Filling and Transporting', 'fill',
         [('sack', 'rhymes with "back"'), ('load', 'rhymes with "road"'), ('trolley', 'TROL-ee'),
          ('transport', 'trans-PORT')],
         'We load the sacks onto a trolley.', [
        dict(t='Step ten. **Filling and transporting.**'),
        dict(t='We fill the **sacks** with wheat.'),
        dict(rep='sack'),
        dict(t='Then we **load** them onto a tractor **trolley** or a truck.'),
        dict(rep='load'),
        dict(rep='trolley'),
        dict(t='Finally, we **transport** them to the grain market.'),
        dict(rep='transport'),
        dict(t='Say it: We load the sacks onto a trolley.', pause=REP),
    ]),

    step(11, 'Selling at the Grain Market', 'market',
         [('grain market', 'GRAIN MAR-ket'), ('weigh', 'rhymes with "day"'), ('dealer', 'DEE-ler'),
          ('price', 'rhymes with "rice"')],
         'The wheat is weighed and sold to a dealer.', [
        dict(t='Step eleven. **Selling at the grain market.**'),
        dict(t='At the **grain market**, the wheat is **weighed** and sold to grain **dealers**.'),
        dict(rep='grain market'),
        dict(rep='weigh'),
        dict(rep='dealer'),
        dict(t='The farmer and the dealer agree on a **price**.'),
        dict(rep='price'),
        dict(t='Say it: The wheat is weighed and sold to a dealer.', pause=REP),
    ]),

    dict(kind='list', img='market', heading='Role play: At the Grain Market', beats=[
        dict(t='Now listen to a farmer and a grain dealer at the market.', pause=0.5),
        dict(item=0, v=DEALER, t='Good morning! How many sacks have you brought today?'),
        dict(item=1, v=FARMER, t='Good morning! I have brought forty sacks of wheat.'),
        dict(item=2, v=DEALER, t="Let's weigh them first. The wheat looks clean and dry."),
        dict(item=3, v=FARMER, t='Yes, we dried it in the sun for two days. What is the price today?'),
        dict(item=4, v=DEALER, t='The price is good today. I can buy all of it.'),
        dict(item=5, v=FARMER, t="Great! Let's make a deal.", pause=0.8),
    ], items=[('Dealer', 'Good morning! How many sacks have you brought today?'),
              ('Farmer', 'Good morning! I have brought forty sacks of wheat.'),
              ('Dealer', "Let's weigh them first. The wheat looks clean and dry."),
              ('Farmer', 'Yes, we dried it in the sun for two days. What is the price today?'),
              ('Dealer', 'The price is good today. I can buy all of it.'),
              ('Farmer', "Great! Let's make a deal.")]),

    dict(kind='center', img='market', box=('YOUR TURN', 'You are the farmer.', 'Listen to the dealer, then answer.'), beats=[
        dict(t='Your turn! **You are the farmer.** Listen to the dealer, then answer.'),
        dict(v=DEALER, t='Good morning! How many sacks have you brought today?',
             box=('DEALER', 'How many sacks have you brought today?', 'Try: I have brought ... sacks of wheat.'), pause=ASK, chime=True),
        dict(v=FARMER, t='I have brought forty sacks of wheat.',
             box=('MODEL ANSWER', 'I have brought forty sacks of wheat.', '')),
        dict(v=DEALER, t='Is the wheat dry?',
             box=('DEALER', 'Is the wheat dry?', 'Try: Yes, we dried it in the sun for ...'), pause=ASK, chime=True),
        dict(v=FARMER, t='Yes, we dried it in the sun for two days.',
             box=('MODEL ANSWER', 'Yes, we dried it in the sun for two days.', '')),
        dict(v=DEALER, t='Do you want to sell all of it?',
             box=('DEALER', 'Do you want to sell all of it?', 'Try: Yes, ... What is the price today?'), pause=ASK, chime=True),
        dict(v=FARMER, t='Yes, I do. What is the price today?',
             box=('MODEL ANSWER', 'Yes, I do. What is the price today?', ''), pause=0.8),
    ]),

    dict(kind='list', img='title', heading='Speaking tip: Sequence words', beats=[
        dict(t='Speaking tip! When you describe a process, use **sequence words**.'),
        dict(t='They show the order of the steps.'),
        dict(item=0, t='**First**, we prepare the land.', pause=0.4),
        dict(item=1, t='**Then**, we sow the seeds.', pause=0.4),
        dict(item=2, t='**Next**, we add fertilizer and irrigate the field.', pause=0.4),
        dict(item=3, t='**After a few months**, the wheat ripens.', pause=0.4),
        dict(item=4, t='**Once it is dry**, we thresh it.', pause=0.4),
        dict(item=5, t='**Finally**, we sell it at the grain market.', pause=0.4),
        dict(t='Now say them with me: First. Then. Next. After a few months. Once it is dry. Finally.',
             tts='Now say them with me. First... Then... Next... After a few months... Once it is dry... Finally.',
             pause=REP),
    ], items=[('First,', 'we prepare the land.'), ('Then,', 'we sow the seeds.'),
              ('Next,', 'we add fertilizer and irrigate the field.'),
              ('After a few months,', 'the wheat ripens.'), ('Once it is dry,', 'we thresh it.'),
              ('Finally,', 'we sell it at the grain market.')]),

    dict(kind='center', img='plough', quiz=True, box=('QUIZ', 'What is this machine?', 'Say the answer before it appears.'), beats=[
        dict(t='Quiz time! Look at the picture. **What is this machine?** Say the answer before it appears.'),
        dict(img='q:plough', t='What is this?', box=('QUIZ', 'What is this?', ''), pause=3.2, chime=True),
        dict(img='plough', t="It's a **plough**. It turns over the soil.",
             box=('ANSWER', 'plough', 'It turns over the soil.'), pause=0.6),
        dict(img='q:sow', t='And this one?', box=('QUIZ', 'What is this?', ''), pause=3.2, chime=True),
        dict(img='sow', t="It's a **seed drill**. It sows seeds in rows.",
             box=('ANSWER', 'seed drill', 'It sows seeds in rows.'), pause=0.6),
        dict(img='q:rotavator', t='What is this?', box=('QUIZ', 'What is this?', ''), pause=3.2, chime=True),
        dict(img='rotavator', t="It's a **rotavator**. It breaks the soil into finer pieces.",
             box=('ANSWER', 'rotavator', 'It breaks the soil into finer pieces.'), pause=0.6),
        dict(img='q:harv', t='And this big yellow machine?', box=('QUIZ', 'What is this?', ''), pause=3.2, chime=True),
        dict(img='harv', t="It's a **combine harvester**. It cuts the crop and separates the grain.",
             box=('ANSWER', 'combine harvester', 'It cuts the crop and separates the grain.'), pause=0.6),
        dict(img='q:thresh', t='Last one. What is this?', box=('QUIZ', 'What is this?', ''), pause=3.2, chime=True),
        dict(img='thresh', t="It's a **thresher**. It separates the grains from the straw.",
             box=('ANSWER', 'thresher', 'It separates the grains from the straw.'), pause=0.6),
    ]),

    dict(kind='center', img='sow', box=('SPEAKING PRACTICE', 'Answer in a full sentence.', ''), beats=[
        dict(t='Speaking practice. Listen to the question, pause, and answer in a **full sentence**.'),
        dict(img='sow', t='What does a seed drill do?', box=('QUESTION', 'What does a seed drill do?', ''), pause=ASK, chime=True),
        dict(t='A seed drill sows the seeds in rows, at the right depth.',
             box=('MODEL ANSWER', 'A seed drill sows the seeds in rows, at the right depth.', '')),
        dict(img='irr', t='Where does the water for irrigation come from?',
             box=('QUESTION', 'Where does the water for irrigation come from?', ''), pause=ASK, chime=True),
        dict(t='It comes from a canal or a tube well.',
             box=('MODEL ANSWER', 'It comes from a canal or a tube well.', '')),
        dict(img='dry', t='Why do farmers dry the wheat in the sun?',
             box=('QUESTION', 'Why do farmers dry the wheat in the sun?', ''), pause=ASK, chime=True),
        dict(t='They dry it so that it does not rot.',
             box=('MODEL ANSWER', 'They dry it so that it does not rot.', '')),
        dict(img='market', t='What happens at the grain market?',
             box=('QUESTION', 'What happens at the grain market?', ''), pause=ASK, chime=True),
        dict(t='The wheat is weighed and sold to grain dealers.',
             box=('MODEL ANSWER', 'The wheat is weighed and sold to grain dealers.', ''), pause=0.6),
    ]),

    dict(kind='list', img='ripe', heading='Challenge: Tell the whole story', beats=[
        dict(t='Final challenge! Describe the whole journey of wheat in your own words.'),
        dict(t='Use **first**, **then**, **next** and **finally**. Pause the video and try now.', pause=3.0, chime=True),
        dict(t="Here is a model answer. Listen, then read it aloud.", pause=0.3),
        dict(item=0, t='First, we plough the land and level the field.'),
        dict(item=1, t='Then, we sow the seeds with a seed drill and add fertilizer.'),
        dict(item=2, t='Next, we irrigate the field, and the crop grows taller.'),
        dict(item=3, t='After a few months, the wheat turns golden, and we harvest it.'),
        dict(item=4, t='We dry it in the sun, and a thresher separates the grain from the straw.'),
        dict(item=5, t='Finally, we load the sacks and sell the wheat at the grain market.', pause=1.0),
    ], items=[('1', 'First, we plough the land and level the field.'),
              ('2', 'Then, we sow the seeds with a seed drill and add fertilizer.'),
              ('3', 'Next, we irrigate the field, and the crop grows taller.'),
              ('4', 'After a few months, the wheat turns golden, and we harvest it.'),
              ('5', 'We dry it in the sun, and a thresher separates the grain from the straw.'),
              ('6', 'Finally, we load the sacks and sell the wheat at the grain market.')]),

    dict(kind='review', img='vocab', heading='Key Vocabulary', beats=[
        dict(t="Let's review the **key vocabulary**."),
        dict(item=0, t='**Cultivation**: growing crops.'),
        dict(item=1, t='**Plough**: turns over the soil.'),
        dict(item=2, t='**Cultivator**: loosens the soil.'),
        dict(item=3, t='**Rotavator**: breaks soil into finer pieces.'),
        dict(item=4, t='**Land leveller**: levels the field.'),
        dict(item=5, t='**Seed drill**: sows seeds in rows.'),
        dict(item=6, t='**Fertilizer**: plant food, like urea and DAP.',
             tts='Fertilizer: plant food, like urea and D. A. P.'),
        dict(item=7, t='**Irrigation**: supplying water.'),
        dict(item=8, t='**Harvest**: cutting the crop.'),
        dict(item=9, t='**Combine harvester**: cuts the crop and separates the grain.'),
        dict(item=10, t='**Thresher**: separates grains from straw.'),
        dict(item=11, t='**Grain market**: the place to sell the crop.', pause=0.8),
    ], items=[('Cultivation', 'growing crops'), ('Plough', 'turns over the soil'),
              ('Cultivator', 'loosens the soil'), ('Rotavator', 'breaks soil into finer pieces'),
              ('Land leveller', 'levels the field'), ('Seed drill', 'sows seeds in rows'),
              ('Fertilizer', 'plant food (urea, DAP)'), ('Irrigation', 'supplying water'),
              ('Harvest', 'cutting the crop'), ('Combine harvester', 'cuts and separates grain'),
              ('Thresher', 'separates grains from straw'), ('Grain market', 'place to sell the crop')]),

    dict(kind='title', img='title', outro=True, beats=[
        dict(t='Great work! You followed wheat all the way **from field to market**.'),
        dict(t='Here is your homework: tell a friend or a family member about the journey of wheat.'),
        dict(t='Use the sequence words, and the new vocabulary.'),
        dict(t='Keep practising, and see you next time!', pause=1.2),
    ]),
]
