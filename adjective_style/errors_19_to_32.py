from adjgen import *
L, R = '‘', '’'
q = lambda t: f'{L}{t}{R}'
def kt(*f): return KeepTogether(list(f))
LX, RX = -113, 113
story = []

def checks(v, bad_s, red_t, red_c, grn_t, grn_c, res):
    v.bad(bad_s); v.text('Check', 9, DARK)
    v.text(red_t, 9.3, RED); v.cap(red_c); v.gap(4)
    v.text(grn_t, 9.3, GREEN); v.cap(grn_c); v.result(res)

# =============================================================== ERROR 19
v = VB()
v.head(f'1. After a Superlative the Joiner Is {q("That")}')
v.row([dict(t='who / whom', w=110, x=LX, c=RED, cap=['describes the PERSON', 'adds extra news about her']),
       dict(t='that', w=110, x=RX, c=GREEN, cap=['pins down the SUPERLATIVE', 'which one of all?'])])
v.arrow(xs=(CX + RX,), color=GREEN, w=1)
v.row([dict(t='the best dancer', w=130, c=NAVY, cap='superlative: ONE of all'), dict(t='that', w=60, c=GREEN, cap='pins it down'), dict(t='I have ever met', w=130, c=GREEN, cap='the group she is picked from')])
v.pill('a superlative picks out ONE, so the clause after it pins it down', size=9.5)
a19 = v.build()
v = VB()
v.head('2. The Clause Is Always in the Perfect Tense')
v.cap(f'{q("ever")} looks back over all the time up to now, and looking back is the job of the perfect')
v.row([dict(t='is / are', w=90, x=-150, cap='present'), dict(t='→', k='txt', x=-75), dict(t='I have ever seen', w=160, x=40, c=GREEN, cap='present perfect')])
v.row([dict(t='was / were', w=90, x=-150, cap='past'), dict(t='→', k='txt', x=-75), dict(t='I had ever seen', w=160, x=40, c=GREEN, cap='past perfect')])
v.row([dict(t='will be', w=90, x=-150, cap='future'), dict(t='→', k='txt', x=-75), dict(t='I will have ever seen', w=160, x=40, c=GREEN, cap='future perfect')])
v.sep()
v.bad('You are the most excited person that I ever saw.')
v.text(f'{q("saw")} (simple past) ignores the look back', 9.5, RED)
v.arrow(color=GREEN, w=1)
v.result('You are the most excited person that I have ever seen.')
b19 = v.build()
story += error(19, f'After a Superlative: {q("That")} and the Perfect Tense',
    [('Radhika is the best dancer whom I met.', 'Radhika is the best dancer that I have ever met.'), ('You are the most excited person who I ever saw.', 'You are the most excited person that I have ever seen.')],
    f'You see a person after the noun and reach for {q("who")} or {q("whom")}, and you put the verb in the simple past because the meeting is over. That is the normal pattern, but it\'s usually handed to you as one fixed pattern for every noun, with no explanation of why a sentence with a superlative behaves differently.',
    f'A superlative already picks out ONE from the whole group (Error 15), so the clause after it is not adding extra news about the person: it is pinning the superlative down, {q("the best dancer OF ALL I have met")}. {q("That")} is the word that pins down; {q("who")} and {q("whom")} only describe. And {q("ever")} means {q("at any time up to now")}, so the clause must look back over everything so far, and looking back over time is exactly the job of the PERFECT tense. The perfect follows the time of the main verb: present has ever seen, past had ever seen, future will have ever seen.',
    [a19]) + [Spacer(0, 8), kt(b19), PageBreak()]

# =============================================================== ERROR 20
v = VB()
v.head('1. What the Hyphen Does')
v.text('Without the hyphen, the reader can split the two words', 9.5, RED)
v.row([dict(t='a', w=40, c=GREY), dict(t='good', w=70, c=RED, cap='an adjective?'), dict(t='looking', w=80, c=RED, cap='another adjective?'), dict(t='friend', w=80)])
v.arrow(color=RED, w=1)
v.text('two separate adjectives, both describing the friend', 9.5, RED)
v.sep()
v.row([dict(t='a', w=40, c=GREY), dict(t='good-looking', w=120, c=GREEN, cap='ONE adjective, glued by the hyphen'), dict(t='friend', w=80)])
v.result('He is a good-looking friend.')
a20 = v.build()
v = VB()
v.head('2. After the Verb, There Is Nothing to Glue')
v.row([dict(t='good-looking friend', w=170, x=LX - 6, c=NAVY, cap=['before a noun: the hyphen', 'makes one adjective for the noun']),
       dict(t='He is good looking', w=150, x=RX + 22, c=GREEN, cap=['after the verb: no noun follows', 'so there is nothing to glue'])])
v.pill('the hyphen only appears in front of a noun', size=10)
v.result('He is good looking.')
b20 = v.build()
story += error(20, 'Compound Adjectives: Hyphen Before the Noun, None After the Verb',
    [('He is a good looking friend.', 'He is a good-looking friend.'), ('He is good-looking.', 'He is good looking.')],
    f'You learn that a compound adjective is two words joined by a hyphen (good-looking, well-known), so the hyphen goes in every time, or you leave it out every time. Both habits are common, but it\'s usually handed to you as a spelling rule to memorize, with no explanation of when the hyphen is actually needed.',
    f'A hyphen has one job: to glue two words into ONE adjective. That only matters in front of a noun, because there the adjective must describe the noun as a single unit: {q("a good-looking friend")}, not a good friend who happens to be looking. After the verb the compound stands alone as the complement. There is no noun to describe and nothing to glue, so no hyphen: {q("He is good looking")}.',
    [a20]) + [Spacer(0, 8), kt(b20), PageBreak()]

# =============================================================== ERROR 21
v = VB()
v.head('1. Specified, So the Highest Degree')
v.row([dict(t='its', w=60, c=GREEN, cap=['possessive: it SPECIFIES', '(Error 15)']), dict(t='highest', w=90, c=GREEN, cap='the adjective'), dict(t='(point)', w=80, c=GREY, cap=['understood, left out', '(Error 1)'])])
v.arrow(color=PURPLE, w=1.2)
v.text('the price reached ONE point: the top one', 9.5, PURPLE)
v.sep()
v.head(f'2. {q("High")} and {q("Higher")} Don{R}t Point to One Point')
v.row([dict(t='high', w=80, c=RED, cap=['names no point', 'at all']), dict(t='higher', w=90, c=RED, cap=['beats only', 'one other level']), dict(t='highest', w=100, c=GREEN, cap=['beats every level:', 'THE one'])])
v.bad('The price has reached its high.')
v.arrow(color=GREEN, w=1)
v.result('The price has reached its highest.')
a21 = v.build()
story += error(21, 'A Specified Adjective at the End: Use the Highest Degree',
    [('The price has reached its high.', 'The price has reached its highest.'), ('The price has reached its higher.', 'The price has reached its highest.')],
    f'You see {q("its")} followed by an adjective and treat it like any other adjective, so {q("high")} or {q("higher")} feels fine. That works when a noun follows, but it quietly breaks when the sentence ends on the adjective itself, and nobody explains why.',
    f'{q("Its")} is a possessive adjective, and a possessive SPECIFIES: it points to ONE particular thing (Error 15). When the sentence ends on the adjective, no noun follows to carry that meaning, so the adjective stands for {q("its ___ point")}, with the noun understood and left out (as in {q("The Rich")}, Error 1). The price reached ONE point, the top one, and picking one out of all the levels is the superlative\'s job: {q("its highest")}. {q("High")} names no point at all, and {q("higher")} only beats one other level.',
    [a21]) + [PageBreak()]

# =============================================================== ERROR 22
v = VB()
v.head('1. Which Degree Does Each Word Measure?')
v.row([dict(t='Positive', w=104, x=-152, cap='intelligent'), dict(t='Comparative', w=104, x=0, cap='wiser'), dict(t='Superlative', w=104, x=152, cap='wisest')])
v.arrow(xs=(CX - 152, CX, CX + 152), color=GREY)
v.row([dict(t='very', w=104, x=-152, c=GREEN, cap=['very intelligent', 'measures the QUALITY']), dict(t='much', w=104, x=0, c=GREEN, cap=['much wiser, much better than I', 'measures the GAP']),
       dict(t='by far / easily', w=110, x=152, c=GREEN, cap=['by far the wisest', 'measures the GAP'])])
v.pill(f'{q("much better")} only looks wrong: {q("much")} usually sounds like a quantity', size=9.5)
a22 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'She is very better than I.', 'very + better', f'{q("better")} is a comparison: very measures a quality, not the gap', 'much + better', 'much measures how big the gap is', 'She is much better than I.')
v.sep()
checks(v, 'This book is much more cheaper than the one I have bought.', 'more + cheaper', f'{q("cheaper")} is already comparative: the double-up of Error 8', 'much + cheaper', f'{q("much")} measures the gap, and {q("cheaper")} does the comparing', 'This book is much cheaper than the one I have bought.')
b22 = v.build()
story += error(22, 'Very vs. Much: Positive or Comparative?',
    [('She is very better than I.', 'She is much better than I.'), ('This book is much more cheaper than the one I have bought.', 'This book is much cheaper than the one I have bought.')],
    f'You learn that {q("very")} and {q("much")} both mean {q("a lot")}, so they get swapped freely. That is close enough in speech, but it\'s usually handed to you as a pair of synonyms, with no explanation of which degree each one belongs to.',
    f'{q("Very")} says how much of a QUALITY something has, so it sits on a plain adjective: very intelligent. {q("Much")} says how big a DIFFERENCE is, so it needs something being compared: much better than I, much wiser. A comparative is a comparison and a plain adjective is not, so {q("very")} goes with the positive degree and {q("much")} with the comparative. For the superlative, {q("by far")} (or {q("easily")}) measures the gap: by far the wisest.',
    [a22]) + [Spacer(0, 8), kt(b22), PageBreak()]

# =============================================================== ERROR 23
v = VB()
v.head('1. Two Kinds of Adjectives')
v.row([dict(t='Adjective', w=130, cap='a scale, or a fixed point?')])
v.split([CX + LX, CX + RX])
v.row([dict(t='Gradable', w=130, x=LX, c=NAVY, cap=['a SCALE: more or less', 'intelligent, high']), dict(t='Non-gradable', w=130, x=RX, c=GREEN, cap=['a FIXED POINT', 'unique, universal, parallel, perfect,', 'empty, ideal, red, black, circle'])])
v.arrow(xs=(CX + LX, CX + RX))
v.row([dict(t='very / much / more / most', w=170, x=LX - 8, c=GOLD, cap='they measure the scale'), dict(t='quite', w=80, x=RX + 24, c=GOLD, cap=['completely:', 'it measures nothing'])])
v.text('very = positive degree      much = comparative, superlative      quite = non-gradable', 8.8, PURPLE)
a23 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'The two paths are relatively parallel to each other.', 'relatively + parallel', f'{q("parallel")} is a fixed point: there is no more or less to measure', 'parallel', f'it is parallel or it is not: nothing to add', 'The two paths are parallel to each other.')
v.sep()
v.head(f'A Related Twist: {q("Ideal")} Already Means {q("Most Suitable")}')
v.row([dict(t='most', w=70, c=RED, cap=['a second', 'superlative']), dict(t='ideal', w=90, c=GREEN, cap=['= most suitable', 'already the top'])])
v.bad('It was the most ideal weather for a picnic.')
v.result('It was the ideal weather for a picnic.')
b23 = v.build()
story += error(23, 'Non-Gradable Adjectives: No Degrees',
    [('This book is very unique, so we should buy it.', 'This book is quite unique, so we should buy it.'), ('The two paths are relatively parallel to each other.', 'The two paths are parallel to each other.')],
    f'You learn that {q("very")} strengthens an adjective and {q("more")} and {q("most")} compare it, so any adjective can be made stronger or weaker. That is true for most adjectives, but it\'s usually handed to you as a rule for every adjective, with no explanation of why some adjectives refuse every degree word.',
    f'Adjectives come in two kinds. GRADABLE adjectives sit on a scale (intelligent, high): there is more or less of them, so very, much, more and most can measure them. NON-GRADABLE (absolute) adjectives name a fixed point, not a scale: unique, universal, parallel, perfect, empty, red, circle. Something is parallel or it is not, so there is no {q("relatively parallel")} and no {q("more unique")} to measure. The one word that still fits is {q("quite")}, because it measures nothing: it confirms {q("completely")}.',
    [a23]) + [Spacer(0, 8), kt(b23), PageBreak()]

# =============================================================== ERROR 24
v = VB()
v.head('1. Four Look-Alike Words')
v.row([dict(t='later', w=76, c=NAVY, cap=['TIME', 'see you later']), dict(t='latter', w=76, c=GREEN, cap=['POSITION', 'the second of two']), dict(t='letter', w=76, c=GREY, cap=['a written', 'message']), dict(t='latest', w=76, c=GOLD, cap=['the most recent,', 'the latest update'])])
v.sep()
v.head(f'2. {q("The Latter")} Is Out of Two')
v.row([dict(t='Ahmed', w=90, c=GREY, cap='the former'), dict(t='Bilal', w=90, c=GREEN, cap='the latter')])
v.text('Ahmed and Bilal are both strong.', 9.3, DARK)
v.bad('The later is the stronger.')
v.text('later = TIME', 9.3, RED); v.cap('there is no time here, only the order of two names')
v.gap(4)
v.text('latter = the second of two', 9.3, GREEN); v.cap(f'it is specified out of two, so it takes {q("the")} (Error 11)')
v.result('The latter is the stronger.')
a24 = v.build()
story += error(24, f'{q("Later")} vs. {q("Latter")}: Time or Position?',
    [('The later is the stronger.', 'The latter is the stronger.'), ('I will meet you latter.', 'I will meet you later.')],
    f'{q("Later")}, {q("latter")} and {q("letter")} differ by one letter and sound almost the same, so they get swapped without anyone noticing. They look like spelling slips, but it\'s usually handed to you as a spelling fact, with no explanation of how the meanings differ.',
    f'{q("Later")} is about TIME: after now (see you later). {q("Latter")} is about POSITION: the second of two things that have just been named (the former and the latter). So {q("the latter")} only works when exactly two things have been mentioned and the reader knows which one you mean. That makes it SPECIFIED, so it takes {q("the")}, the same reason as {q("the wiser of the two")} (Error 11). {q("Letter")} is a written message, and {q("latest")} means the most recent update.',
    [a24]) + [PageBreak()]

# =============================================================== ERROR 25
v = VB()
v.head('1. The Verb Follows the Noun Beside It')
v.row([dict(t='Many  +  students', w=150, x=LX, c=NAVY, cap=['a PLURAL noun', 'so a plural verb: are']), dict(t='Many a  +  student', w=150, x=RX, c=GREEN, cap=['a + ONE: a SINGULAR noun', 'so a singular verb: is'])])
v.row([dict(t='more  +  students', w=150, x=LX, c=NAVY, cap=['a PLURAL noun', 'so a plural verb: are']), dict(t='more than one  +  student', w=170, x=RX + 10, c=GREEN, cap=['one + a SINGULAR noun', 'so a singular verb: is'])])
v.pill('the verb agrees with the noun beside it, not with the meaning ‘many’', size=9.5)
a25 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'More than one student are absent.', 'more than one + student + are', f'it sounds plural, but the noun beside {q("one")} is singular', 'more than one + student + is', 'singular noun, singular verb', 'More than one student is absent.')
v.sep()
v.head(f'A Related Twist: {q("More Students Than One")}')
v.row([dict(t='more students', w=120, c=GREEN, cap='the SUBJECT: plural'), dict(t='than one', w=80, c=GREY, cap='extra'), dict(t='are', w=50, c=GREEN, cap='plural verb')])
v.text('the plural noun comes first, so the verb is plural', 9.5, GREEN)
b25 = v.build()
story += error(25, f'{q("Many A")} and {q("More Than One")}: Singular Verb',
    [('Many a student have failed the test.', 'Many a student has failed the test.'), ('More than one student are absent.', 'More than one student is absent.')],
    f'You learn that {q("many")} means more than one, so it takes a plural verb: many students are, more students are. That is true for {q("many")}, but it\'s usually handed to you as a rule about the meaning {q("more than one")}, with no explanation of why two expressions that sound plural take a singular verb.',
    f'The verb agrees with the grammar of the noun, not with the meaning {q("many")}. {q("Many students")} is built on a PLURAL noun, so the verb is plural. {q("Many a student")} is built on {q("a")}, which only takes a SINGULAR noun, so the verb is singular. The same goes for {q("more than one student")}: the noun beside {q("one")} is singular, so the verb is singular. And {q("more students than one")} puts the plural noun first: {q("more students")} is the subject, so the verb is plural.',
    [a25]) + [Spacer(0, 8), kt(b25), PageBreak()]

# =============================================================== ERROR 26
v = VB()
v.head('1. Where, Then How Many')
v.row([dict(t='first, second, third', w=140, x=LX - 6, c=NAVY, cap=['ORDINALS: where it stands', 'in the line']), dict(t='one, two, three', w=120, x=RX + 14, c=GREEN, cap=['CARDINALS: how many'])])
v.arrow(color=GREY)
v.row([dict(t='The', w=50, c=GREY, cap='article'), dict(t='first', w=60, c=NAVY, cap='WHERE'), dict(t='five', w=60, c=GREEN, cap='HOW MANY'), dict(t='students', w=90, cap='noun')])
v.sep()
v.bad('The five first students received medals.')
v.text('it counts the students before it says where they stand', 9.5, RED)
v.arrow(color=GREEN, w=1)
v.result('The first five students received medals.')
a26 = v.build()
story += error(26, 'Ordinals Before Cardinals: ‘The First Five Students’',
    [('The five first students received medals.', 'The first five students received medals.'), ('The two last members resigned.', 'The last two members resigned.')],
    f'You learn that ordinals (first, second, third) show order and cardinals (one, two, three) show number, and then you place them in whichever order sounds right. That works in a short phrase, but it\'s usually handed to you as two lists of words, with no explanation of how they combine.',
    f'An ordinal tells WHERE a thing stands in the line (first, last). A cardinal tells HOW MANY (five, two). The position comes first, because it says where the group STARTS or ENDS: {q("the first")}, and only then the count from that point: {q("five")}. So the order is always: the + ordinal + cardinal + noun. Turning it round ({q("the five first students")}) counts the students before it says where they stand.',
    [a26]) + [PageBreak()]

# =============================================================== ERROR 27
v = VB()
v.head(f'1. The Same Degree on Both Sides of {q("And")}')
v.gap(4)
v.text('Positive + Positive', 9.3, GREEN)
v.row([dict(t='bright', w=80, c=GREEN), dict(t='airy', w=80, c=GREEN), dict(t='spacious', w=90, c=GREEN)])
v.gap(8)
v.text('Comparative + Comparative', 9.3, GREEN)
v.row([dict(t='brighter', w=90, c=GREEN), dict(t='airier', w=80, c=GREEN), dict(t='more spacious', w=120, c=GREEN)])
v.gap(8)
v.text('Mixed', 9.3, RED)
v.row([dict(t='bright', w=80, c=RED, cap='positive'), dict(t='airy', w=80, c=RED, cap='positive'), dict(t='more spacious', w=120, c=RED, cap='comparative: ONE half is measuring')])
v.text('one half only describes, the other half is measuring against something', 9.3, RED)
a27 = v.build()
v = VB()
v.head('2. Check the Rest')
v.text('richest and wisest man', 9.5, GREEN); v.cap('superlative + superlative: the same degree')
v.gap(4)
v.text('long and more difficult', 9.5, RED); v.cap('positive + comparative: longer and more difficult')
v.gap(4)
v.text('more talented but modest', 9.5, RED); v.cap('comparative + positive: more talented but more modest')
b27 = v.build()
story += error(27, 'Consistency: Join Adjectives of the Same Degree',
    [('The room is bright, airy and more spacious.', 'The room is bright, airy and spacious.'), ('The book is long and more difficult.', 'The book is longer and more difficult.')],
    f'You learn that {q("and")} and {q("but")} join adjectives, and you add {q("more")} wherever a comparison feels right. But that checks each adjective on its own, not what it is joined to, and nobody explains the rule that connects them.',
    f'Words joined by {q("and")} or {q("but")} must be EQUAL: the same kind of word doing the same job. For adjectives, the kind is the DEGREE. A positive adjective only describes. A comparative measures against something. Put them side by side and one half is measuring while the other half isn\'t, so they can\'t share the sentence. Positive with positive, comparative with comparative, superlative with superlative: never mixed.',
    [a27]) + [Spacer(0, 8), kt(b27), PageBreak()]

# =============================================================== ERROR 28
v = VB()
v.head('1. Amount or Number?')
v.row([dict(t='less', w=90, x=LX, c=NAVY, cap=['an AMOUNT: you measure it', 'less money, less water']), dict(t='fewer', w=90, x=RX, c=GREEN, cap=['a NUMBER: you count it', 'fewer bags, fewer students'])])
v.text('the degrees of an amount:', 9, DARK)
v.row([dict(t='little', w=70, c=GREY), dict(t='→', k='txt', w=24), dict(t='less', w=70, c=NAVY), dict(t='→', k='txt', w=24), dict(t='least', w=70, c=GREY)])
v.cap('they never reach things you can count one by one')
a28 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'He bought no less than twenty school bags.', 'less + twenty school bags', 'bags are COUNTED one by one: it is a number, not an amount', 'fewer + twenty school bags', 'a smaller number', 'He bought no fewer than twenty school bags.')
b28 = v.build()
story += error(28, f'{q("Less")} or {q("Fewer")}: Amount or Number?',
    [('He bought no less than twenty school bags.', 'He bought no fewer than twenty school bags.')],
    f'You learn that {q("less")} is the opposite of {q("more")}, so it goes wherever {q("more")} goes. That works for {q("more water, less water")}, but it quietly breaks with things you can count, and nobody explains why.',
    f'{q("Less")} measures an AMOUNT: something you weigh or pour and cannot count one by one (less money, less water). School bags can be counted one by one, so what is being compared is a NUMBER, and the word for a smaller number is {q("fewer")}. Little, less, least is the degree chain of an amount, and it never reaches things you count.',
    [a28]) + [Spacer(0, 8), kt(b28), PageBreak()]

# =============================================================== ERROR 29
v = VB()
v.head('1. Surprise or Minimum?')
v.row([dict(t='no less than', w=130, x=LX, c=GREEN, cap=['= as many as, as much as', 'EMPHASIS: surprisingly large']), dict(t='not less than', w=130, x=RX, c=NAVY, cap=['= at least', 'REQUIREMENT: the minimum'])])
v.arrow(xs=(CX + LX, CX + RX), color=GREY)
v.texts([('He owns no less than 10 houses.', CX + LX, 9, DARK, HB), ('He must own not less than 10 houses.', CX + RX, 9, DARK, HB)])
v.texts([('wow! as many as 10', CX + LX, 8.3, GREY, HO), ('the minimum is 10', CX + RX, 8.3, GREY, HO)], h=14)
v.gap(6)
v.texts([('He donated no less than one million rupees.', CX + LX, 8.6, DARK, HB), ('The hall can accommodate not less than 500 people.', CX + RX, 8.6, DARK, HB)])
a29 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'Candidates must be no less than 18 years of age.', 'no less than 18', 'it cheers 18 as a surprisingly large number, but a rule needs a minimum', 'not less than 18', 'at least 18: the minimum requirement', 'Candidates must be not less than 18 years of age.')
b29 = v.build()
story += error(29, f'{q("No Less Than")} vs. {q("Not Less Than")}: Surprise or Minimum?',
    [('Candidates must be no less than 18 years of age.', 'Candidates must be not less than 18 years of age.')],
    f'{q("No")} and {q("not")} differ by one letter, so {q("no less than")} and {q("not less than")} feel like the same phrase. They get swapped without anyone noticing, but it\'s usually handed to you as a pair of look-alikes, with no explanation of what each one tells the reader.',
    f'{q("No less than")} means {q("as many as")} or {q("as much as")}: it makes the amount sound surprisingly LARGE (He owns no less than 10 houses: wow!). {q("Not less than")} means {q("at least")}: it states the MINIMUM that a rule or a limit needs (He must own not less than 10 houses: the minimum is 10). A rule about age or capacity is a requirement, not a surprise, so it needs {q("not less than")}.',
    [a29]) + [Spacer(0, 8), kt(b29), PageBreak()]

# =============================================================== ERROR 30
v = VB()
v.head('1. Amount or Adjective?')
v.row([dict(t='less', w=90, x=LX, c=NAVY, cap=['compares an AMOUNT', f'it takes {q("than")}']), dict(t='lesser', w=90, x=RX, c=GREEN, cap=['an ADJECTIVE: smaller, less important,', 'inferior; it stands before a noun'])])
v.arrow(xs=(CX + LX, CX + RX), color=GREY)
v.row([dict(t='less money than his brother', w=180, x=LX - 14, c=NAVY), dict(t='of lesser rent', w=130, x=RX + 40, c=GREEN)])
a30 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'He has lesser money than his brother.', 'lesser + money + than', f'{q("lesser")} describes quality (smaller, inferior): it doesn\'t compare amounts', 'less + money + than', f'an amount compared with another amount takes {q("than")}', 'He has less money than his brother.')
b30 = v.build()
story += error(30, f'{q("Less")} vs. {q("Lesser")}: Amount or Meaning?',
    [('He has lesser money than his brother.', 'He has less money than his brother.')],
    f'{q("Lesser")} sounds like a stronger, more formal version of {q("less")} (like {q("greater")}), so it feels right for a smaller amount. But it\'s usually handed to you as a pair of look-alikes, with no explanation of what each one does.',
    f'{q("Less")} compares an AMOUNT, so it needs something to be compared with: less money than his brother. {q("Lesser")} is an ADJECTIVE with its own meaning: smaller, less important, inferior. It stands in front of a noun and describes it (a lesser rent, a lesser evil). It doesn\'t compare, so it never takes {q("than")}.',
    [a30]) + [Spacer(0, 8), kt(b30), PageBreak()]

# =============================================================== ERROR 31
v = VB()
v.head('1. How Many Are Being Compared?')
v.sub('Exactly TWO: one beats the other, so a COMPARATIVE')
v.gap(2)
v.row([dict(t='son', w=70, c=GREEN), dict(t='son', w=70, c=GREEN)], frame=(0, 1, 'my two sons'))
v.text('younger  +  more intelligent', 9.3, GREEN)
v.gap(8)
v.sub('THREE or more (the whole family): one beats all the rest, so a SUPERLATIVE')
v.gap(2)
v.row([dict(t='child', w=70, c=NAVY), dict(t='child', w=70, c=NAVY), dict(t='child', w=70, c=NAVY)], frame=(0, 2, 'all the children in the family'))
v.text('the youngest  +  the most intelligent', 9.3, NAVY)
a31 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'This is the youngest and more intelligent of my two sons.', 'youngest  +  more intelligent', 'two sons need the comparative, and both halves must match (Error 27)', 'younger  +  more intelligent', 'comparative + comparative', 'This is the younger and more intelligent of my two sons.')
v.sep()
v.bad('Of Karachi and Hyderabad, which city is the oldest?')
v.text('only two cities: one beats the other', 9.5, RED)
v.arrow(color=GREEN, w=1)
v.result('Of Karachi and Hyderabad, which city is the older?')
b31 = v.build()
story += error(31, 'Two or Many: Comparative for Two, Superlative for More',
    [('This is the youngest and more intelligent of my two sons.', 'This is the younger and more intelligent of my two sons.'), ('Of Karachi and Hyderabad, which city is the oldest?', 'Of Karachi and Hyderabad, which city is the older?')],
    f'You learn that {q("est")} and {q("most")} show the top and {q("er")} and {q("more")} show a comparison, and you pick whichever sounds strongest. That works until you count the group, but it\'s usually handed to you without the question that decides it: how many are being compared?',
    f'The degree depends on the SIZE OF THE GROUP. Exactly TWO things: one beats the other, so it is a comparison (older, younger). THREE or more, like all the children in a family: one beats all the rest, so it is a superlative (the youngest). And in a series the degree must stay the same (Error 27): younger and more intelligent are both comparatives, and the youngest and the most intelligent are both superlatives, with {q("the")} before each.',
    [a31]) + [Spacer(0, 8), kt(b31), PageBreak()]

# =============================================================== ERROR 32
v = VB()
v.head('1. A Multiple of an Equal, Not a Comparison')
v.row([dict(t='twice', w=70, c=NAVY), dict(t='three times', w=100, c=NAVY), dict(t='half', w=70, c=NAVY)])
v.arrow(color=GREY)
v.pill('multiplier  +  as  +  adjective  +  as', size=10.5)
v.cap(f'the positive degree: the equality structure of Error 2')
v.sep()
v.row([dict(t='twice', w=70, c=NAVY), dict(t='as old as', w=90, c=GREEN), dict(t='the central library', w=140)])
v.cap('the building is twice as old as the central library')
a32 = v.build()
v = VB()
v.head('2. The Catch')
checks(v, 'The building is twice older than the central library.', 'twice + older + than', f'{q("older than")} says {q("more than")}: it can\'t also say a fixed multiple', 'twice + as old as', 'a multiple of an EQUAL', 'The building is twice as old as the central library.')
v.sep()
v.bad('The new phone was reported to be twice more efficient than the iPhone.')
v.arrow(color=GREEN, w=1)
v.result('The new phone was reported to be twice as efficient as the iPhone.')
b32 = v.build()
story += error(32, 'Multipliers: Half, Twice, Three Times Take the Positive Degree',
    [('The building is twice older than the central library.', 'The building is twice as old as the central library.'), ('The new phone was reported to be twice more efficient than the iPhone.', 'The new phone was reported to be twice as efficient as the iPhone.')],
    f'You see a number of times (twice, three times) and a comparison, so {q("er ... than")} feels natural: {q("twice older than")}. That works for ordinary comparatives, but it\'s usually handed to you as one pattern for every comparison, with no explanation of what a multiplier changes.',
    f'A multiplier (half, twice, thrice, three times) doesn\'t say one thing is MORE than another. It says one thing is a fixed FRACTION or MULTIPLE of the other, which is equality at a different size. Equality uses the positive degree: as + adjective + as (Error 2). So the pattern is multiplier + as + adjective + as, and the comparative\'s {q("than")} has no place in it.',
    [a32]) + [Spacer(0, 8), kt(b32)]
