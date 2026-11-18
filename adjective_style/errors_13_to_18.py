import sys
from adjgen import *
L, R = '‘', '’'
q = lambda t: f'{L}{t}{R}'
def kt(*f): return KeepTogether(list(f))
LX, RX = -113, 113           # left and right column centres
story = []

# =============================================================== ERROR 13
v = VB()
v.head('1. Two Kinds of Comparison Words')
v.row([dict(t='Comparison', w=150, cap=f'two ways to say {q("more than")}')])
v.split([CX + LX, CX + RX])
v.row([dict(t='Comparative DEGREE', w=170, x=LX, c=NAVY, cap=['built by us: adjective + er', 'old + er = older']),
       dict(t='Comparative WORD', w=170, x=RX, c=GREEN, cap=['already built into the word:', 'junior, senior, superior, inferior,', 'prefer, preferable, elder'])])
v.arrow(xs=(CX + LX, CX + RX))
v.row([dict(t='than  /  of', w=110, x=LX, c=GOLD, cap=f'the comparison is still OPEN: more old than WHAT?'),
       dict(t='to', w=110, x=RX, c=GOLD, cap='the comparison is already COMPLETE')])
v.pill(f'A comparative word already carries the comparison: it takes {q("to")}, not {q("than")}', size=9.5)
a13 = v.build()

v = VB()
v.head(f'2. The Catch: {q("Than")} Looks Like the Normal Ending')
v.bad('He prefers coffee than tea.')
v.text('Check', 9, DARK)
v.text('prefers (comparative WORD)  +  than', 9.3, RED)
v.cap(f'{q("prefers")} already means {q("likes MORE than")}, so the comparison is complete and {q("than")} has no job')
v.gap(6)
v.text('prefers (comparative WORD)  +  to', 9.3, GREEN)
v.cap(f'the word borrows {q("to")} instead')
v.result('He prefers coffee to tea.')
v.sep()
v.sub(f'Compare: a comparative DEGREE still needs {q("than")}')
v.row([dict(t='This house', w=96), dict(t='is', w=34, c=GREY), dict(t='older', w=72, cap=['adjective + er,', 'still open']),
       dict(t='than', w=64, c=GREEN, cap=f'closes it'), dict(t='that one', w=90)])
v.result('This house is older than that one.')
b13 = v.build()

v = VB()
v.head(f'3. {q("To")} Takes the Object Case')
v.cap(f'{q("to")} is a PREPOSITION, so the pronoun after it is always in the OBJECT case', size=8.5)
v.bad('She is junior than I.')
v.text('Check', 9, DARK)
v.text('junior (comparative WORD)  +  than', 9.3, RED)
v.cap(f'a comparative word needs {q("to")}, not {q("than")}')
v.gap(4)
v.cmp('I (subject case)', 'object case', False, RED)
v.cap(f'UNEQUAL case: {q("to")} is a preposition, so an object is needed')
v.gap(4)
v.cmp('me (object case)', 'object case', True, GREEN)
v.cap('matching case: preposition + object')
v.result('She is junior to me.')
v.sep()
v.sub(f'The case rule is different after {q("than")} and after {q("to")}')
v.texts([(f'than: the case MATCHES the other side', CX + LX, 9, NAVY, HB), (f'to: always the OBJECT case', CX + RX, 9, GREEN, HB)])
v.texts([('She is older than I (am).', CX + LX, 9.3, DARK, HB), ('She is junior to me.', CX + RX, 9.3, DARK, HB)])
v.texts([('She (subject) = I (subject)', CX + LX, 8.3, GREY, HO), ('to + me (object)', CX + RX, 8.3, GREY, HO)], h=14)
c13 = v.build()

v = VB()
v.head(f'A Related Twist: {q("Prefer")} ... {q("Over")}')
v.row([dict(t='He prefers coffee', w=130), dict(t='over', w=60, c=GREY, cap='heard in speech: informal'), dict(t='tea', w=60)])
v.text(f'In formal writing and in exams, use {q("to")}', 9.5, GREEN)
v.result('He prefers coffee to tea.')
d13 = v.build()

story += error(13, f'Comparative Words: Take {q("To")}, Not {q("Than")}',
    [('He prefers coffee than tea.', 'He prefers coffee to tea.'), ('She is junior than I.', 'She is junior to me.')],
    f'You learn that every comparison finishes with {q("than")} (older than, taller than, wiser than) and you carry that one rule to every comparison word you meet. That works for ordinary comparatives, but it\'s usually handed to you as a single rule for everything, with no explanation of why some words flatly refuse {q("than")}.',
    f'There are two different kinds of comparison words. A comparative DEGREE is built by us: adjective + {q("er")} (old becomes older). {q("Older")} only says {q("more old")}, so the comparison is still OPEN (more old than WHAT?) and {q("than")} (or {q("of")} for a pair) must close it. A comparative WORD (the -ior words junior, senior, superior, inferior, and prefer, preferable, elder) already carries the comparison inside itself. There is nothing left to close, so it can\'t take {q("than")} and borrows {q("to")} instead. And since {q("to")} is a preposition, a pronoun after it takes the OBJECT case: {q("to me")}, never {q("to I")}.',
    [a13]) + [Spacer(0, 2), kt(b13), Spacer(0, 8), kt(c13), Spacer(0, 8), kt(d13), PageBreak()]

# =============================================================== ERROR 14
v = VB()
v.text('This book is more preferable than yours.', 9.8, DARK)
v.text(f'THE CATCH: a long word, so {q("more")} looks right', 9.5, RED)
v.row([dict(t='more', w=80, c=RED, cap='builds a comparison'), dict(t='preferable', w=120, c=GREEN, cap='ALREADY a comparison')])
v.arrow(color=RED, w=1)
v.text('the same comparison, built TWICE', 9.5, RED)
v.cap(f'the same double-up as {q("more taller")} in Error 8')
v.sep()
v.text('THE REAL CATCH', 10, GREEN)
v.text(f'{q("preferable")} is a comparative WORD, not a plain adjective', 9.5, DARK)
v.row([dict(t='preferable', w=130, c=GREEN, cap=f'already means {q("more wanted than")}')])
v.arrow(color=GREEN, w=1)
v.text(f'one word, one comparison: {q("more")} is not needed', 9.5, PURPLE)
v.row([dict(t='preferable', w=110, c=GREEN), dict(t='to', w=50, c=GOLD, cap=f'the word borrows {q("to")} (Error 13)'), dict(t='yours', w=80)])
v.result('This book is preferable to yours.')
a14 = v.build()
story += error(14, f'Comparative Words: Never Add {q("More")}',
    [('This book is more preferable than yours.', 'This book is preferable to yours.')],
    f'You learn that long words take {q("more")} (beautiful becomes more beautiful, Error 8), and {q("preferable")} is a long word, so {q("more")} goes in front of it automatically. That rule is real, but it\'s usually handed to you without the question that has to come first: does this word still need a comparison built for it?',
    f'{q("More")} is a tool for BUILDING a comparison out of a plain adjective. {q("Preferable")} is not a plain adjective. It is a comparative WORD (Error 13), so the comparison is already built into it: {q("preferable to")} already means {q("more wanted than")}. Adding {q("more")} builds the same comparison a second time, the same double-up as {q("more taller")} in Error 8, and {q("than")} then tries to close it again. One word, one comparison: {q("preferable")} does the whole job, and {q("to")} completes it.',
    [a14]) + [PageBreak()]

# =============================================================== ERROR 15
v = VB()
v.head('1. Building the Superlative, Then Specifying It')
v.row([dict(t='adjective + est', w=140, cap='wise + est = wisest'), dict(t='most / least + adjective', w=170, cap='most intelligent, least intelligent')])
v.arrow(xs=(CX - 100, CX + 100), color=GREY)
v.pill('picks out ONE from the group: it must be SPECIFIED', size=10)
v.arrow(color=PURPLE, w=1.2)
v.row([dict(t='article + noun', w=130, cap='the best student'), dict(t='or', k='txt', w=24), dict(t='possessive adjective + noun', w=190, cap='my best student')])
v.text('ONE specifier, never both: they share the same slot', 9.5, PURPLE)
a15 = v.build()
v = VB()
v.head(f'2. Two Specifiers Can{R}t Share One Slot')
v.bad('You are the my best student.')
v.row([dict(t='the', w=56, c=RED, cap='specifier 1'), dict(t='my', w=56, c=RED, cap='specifier 2'), dict(t='best student', w=110)])
v.text('two specifiers for one noun: the slot is already full', 9.5, RED)
v.cap(f'students add {q("the")} out of habit, but {q("my")} already points out the one')
v.arrow(color=GREEN, w=1)
v.row([dict(t='my', w=56, c=GREEN, cap='specifies'), dict(t='best student', w=110)])
v.result('You are my best student.')
b15 = v.build()
v = VB()
v.head(f'3. {q("A")} Can{R}t Specify')
v.bad('She is a most intelligent girl.')
v.row([dict(t='a', w=56, c=RED, cap='a = ANY one'), dict(t='most intelligent girl', w=170)])
v.text('a superlative points to THE one, never to any one', 9.5, RED)
v.arrow(color=GREEN, w=1)
v.row([dict(t='the', w=56, c=GREEN, cap='the = THE one'), dict(t='most intelligent girl', w=170)])
v.result('She is the most intelligent girl.')
c15 = v.build()
story += error(15, f'The Superlative Degree: Specify It With {q("The")} or a Possessive',
    [('You are the my best student.', 'You are my best student.'), ('She is a most intelligent girl.', 'She is the most intelligent girl.')],
    f'You learn that a superlative is built with {q("est")} or {q("most")} and always takes {q("the")}, so {q("the")} gets added to every superlative without a second thought. That\'s true most of the time, but it\'s usually handed to you as a fact to memorize, with no explanation of what {q("the")} is actually doing there.',
    f'A superlative picks out ONE from the whole group (the best, the most intelligent), so the reader must know exactly WHICH one. That is what it means to SPECIFY. English specifies with one of two words: the article {q("the")}, or a possessive adjective (my, your, his, her). Both stand in the same slot in front of the noun, so you need ONE, never both: {q("my best student")} is already pointed out by {q("my")}. And {q("a")} can never do the job: {q("a")} means ANY one, the very opposite of THE one.',
    [a15]) + [Spacer(0, 6), kt(b15), Spacer(0, 14), kt(c15), PageBreak()]

# =============================================================== ERROR 16
v = VB()
v.head('1. Ranking or Counting?')
v.row([dict(t='the most excited candidate', w=190, x=LX - 6, c=NAVY, cap=['RANKS: one winner is picked out', f'so it is specified with {q("the")}']),
       dict(t='Most of the people', w=150, x=RX + 24, c=GREEN, cap=['COUNTS: the majority of a group', f'nobody is ranked, so no {q("the")}'])])
v.sep()
v.bad('The most of the people are coming.')
v.text(f'{q("the most")} promises a winner, but no winner is picked', 9.5, RED)
v.arrow(color=GREEN, w=1)
v.text(f'{q("most of")} = the majority of the people', 9.5, GREEN)
v.result('Most of the people are coming.')
a16 = v.build()
story += error(16, f'{q("Most")} vs {q("The Most")}: Majority or Superlative?',
    [('The most of the people are coming.', 'Most of the people are coming.')],
    f'You learn that {q("most")} is the superlative of {q("many")} and that a superlative takes {q("the")}, so {q("the most")} gets used every time {q("most")} appears. But that treats every {q("most")} as a superlative, and nobody explains that some aren\'t.',
    f'{q("The most")} is a true superlative: it ranks and picks out ONE winner (the most excited candidate). But in {q("most of the people")} nobody is being ranked. {q("Most")} simply means the MAJORITY, a quantity of the group. With no winner to pick out, there is nothing to specify, so there is no {q("the")}.',
    [a16]) + [PageBreak()]

# =============================================================== ERROR 17
v = VB()
v.head('1. In the Group or Out of the Group?')
v.sub(f'Error 4: Radha stays OUT of the group ({q("No OTHER student")})')
v.gap(2)
v.row([dict(t='student', w=70, c=GREEN), dict(t='student', w=70, c=GREEN), dict(t='student', w=70, c=GREEN), dict(t='Radha', w=70, c=PURPLE, cap='OUT: compared to the group', capc=PURPLE, capf=HB, caps=8.5)],
      frame=(0, 2, 'No OTHER student'))
v.sub('Superlative: she stays IN the group and is picked out of it')
v.row([dict(t='candidate', w=80, c=GREEN), dict(t='candidate', w=80, c=GREEN), dict(t='She', w=80, c=PURPLE, cap=f'IN: picked {q("out of")} all', capc=PURPLE, capf=HB, caps=8.5)],
      frame=(0, 2, 'of all'))
a17a = v.build()
v = VB()
v.head(f'2. The Catch: {q("Other")} Removes Her From the Group')
v.bad('She is the most excited candidate among all other ones.')
v.row([dict(t='among all other ones', w=170, c=RED, cap=f'{q("other")} throws her out of her own group')])
v.arrow(color=RED, w=1)
v.text('nobody is left to be picked out as the winner', 9.5, RED)
v.sep()
v.row([dict(t='of all', w=100, c=GREEN, cap=f'{q("of")} = {q("out of")}: she is one of them')])
v.pill(f'Can{R}t use {q("other")} in the superlative', size=10.5)
v.result('She is the most excited candidate of all.')
b17 = v.build()
story += error(17, f'No {q("Other")} in the Superlative: {q("Of")} Means {q("Out Of")}',
    [('She is the most excited candidate among all other ones.', 'She is the most excited candidate of all.')],
    f'You\'ve just learned that comparing a person to her own group needs {q("other")} (Error 4), so it\'s tempting to add {q("other")} to every sentence that sets one person against a group, superlatives included. But that overcorrection creates a brand-new error of its own.',
    f'{q("Other")} takes the person OUT of the group, which is exactly what Error 4 needs. A superlative works the opposite way: the winner is chosen OUT OF the group, so she has to stay INSIDE it. {q("Of all")} means {q("out of all")}: she is one of them, and she comes first. Adding {q("other")} throws her out of the very group she is supposed to be picked from, so nobody is left to be the winner.',
    [a17a]) + [Spacer(0, 10), kt(b17), PageBreak()]

# =============================================================== ERROR 18
v = VB()
v.head('1. Choosing or Place?')
v.row([dict(t='of', w=70, x=LX, c=GREEN, cap='CHOOSING: a comparison'), dict(t='in', w=70, x=RX, c=NAVY, cap='PLACE: not a comparison')])
v.arrow(xs=(CX + LX, CX + RX), color=GREY)
v.row([dict(t='the best of the people', w=170, x=LX - 4, c=GREEN, cap=['the winner is chosen', 'from among its members']),
       dict(t='the best person in the class', w=190, x=RX + 12, c=NAVY, cap=['the class is only where', 'the group stands'])])
v.sep()
v.bad('You are my best student in all students.')
v.text(f'{q("all students")} are the members you CHOOSE from', 9.5, RED)
v.cap(f'choosing from members is a comparison, and a comparison takes {q("of")}')
v.arrow(color=GREEN, w=1)
v.pill(f'Comparison: {q("of")}        Not comparison: {q("in")}', size=10)
v.result('You are my best student of all students.')
a18 = v.build()
story += error(18, f'{q("Of")} or {q("In")} After a Superlative: Choosing or Place?',
    [('You are my best student in all students.', 'You are my best student of all students.'), ('She is the best in all girls.', 'She is the best of all girls.')],
    f'You see {q("in")} and {q("of")} after a superlative and pick whichever sounds right (in the class, of the people), as if it were just a matter of habit. That works by ear, but it\'s usually handed to you as a fact to memorize, with no explanation of when each one belongs.',
    f'After a superlative the group has to be named, and the small word in front of it says what that group is doing. If the winner is being CHOSEN from among its members (the best of the people, of all students), that is a comparison, and the winner is picked {q("out of")} them: use {q("of")}. If the group is only a PLACE or a container where the winner stands (in the class, in the school, in the world), nothing is chosen from among its members: use {q("in")}.',
    [a18])

if __name__ == '__main__':
    build(sys.argv[1], story)
