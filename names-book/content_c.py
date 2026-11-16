"""Names 24-33 (Al-Mu'izz ... Al-'Azim)."""
from lib import *

N = []

# ------------------------------------------------------------------ 24 Al-Mu'izz
N.append(dict(
    n=24, ar="الْمُعِزُّ", name_ar="الْمُعِزُّ", tr="Al-Mu'izz", en="The Bestower of Honour",
    ur="جسے چاہے عزت دینے والا",
    root="ع ز ز", root_ar="الْعِزَّةُ وَالْقُوَّةُ وَالْمَنَعَةُ",
    root_en="— might and honour; the same root as Al-'Aziz (Name 8).",
    intro=["This is the same root as Al-'Aziz, in a form that means *to cause someone to have honour*. Al-'Aziz possesses all 'izzah; Al-Mu'izz is the One who grants it. That is why this Name is read together with Al-Mudhill, in the pair that follows."],
    pattern=dict(ar="مُفْعِل", bullets=[
        "This is the form of a verb that causes something to happen to another: أَعَزَّ means to make someone honoured.",
        "So Al-Mu'izz is the One who gives honour to whomever He wills, and who alone has the power to do so.",
        "No one can honour someone whom Allah has not honoured, and no one can take away honour that He has given."]),
    defbox="الْمُعِزُّ → The One who bestows honour and strength upon whomever He wills, and no one can lessen what He has honoured.",
    related="عِزَّة — honour, might · عَزِيز — mighty · أَعَزَّ — to honour · تَعْزِيز — strengthening",
    quran=[
        dict(ayah=ayah(3, 26, words=(12, 15), tr="\"...and You honour whom You will...\""), note=[
            "This is the same ayah we met in Al-Malik. There the Name was Sovereignty; here it is honour. The one who owns the kingdom owns the honour, and gives it to whoever He chooses."]),
        dict(ayah=ayah(4, 139, words=(7, 14), tr="\"Do they seek with them honour? But indeed, honour belongs to Allah entirely.\""), note=[
            "The people the ayah describes went looking for honour in the wrong place: in alliance with those who would give them status. The answer is blunt and kind at once. Honour is not found there. Go to the One who owns it."])],
    hadith=[dict(ar="وَمَا زَادَ اللَّهُ عَبْدًا بِعَفْوٍ إِلَّا عِزًّا",
                 en="The Prophet ﷺ said: \"Allah does not increase a servant who forgives except in honour.\" You would think forgiving costs you your standing. The Prophet ﷺ says the opposite.",
                 ref="Sahih Muslim 2588")],
    essence="Al-Mu'izz is the One who bestows honour and strength on whomever He wills. True honour is only what He gives, and it cannot be taken by anyone else.",
    essence_ur=["الْمُعِزّ وہ ذات ہے جو جسے چاہے عزت اور قوت", "عطا کرتی ہے؛ حقیقی عزت وہی ہے جو اس کی", "طرف سے ملے، اور اسے کوئی چھین نہیں سکتا۔"],
    servant=[
        "Honour that is given by people can be taken by people. A title, a following, an appearance of success can all vanish by next year. The honour that Al-Mu'izz gives stays, because it is not built on anything that can be removed.",
        "The strange secret of this honour is how it is earned. Not by pushing yourself above others, but by forgiving, by being truthful when it costs you, by standing for what is right when it is not popular, by staying humble before Allah. You do not have to defend your dignity when you know who gave it to you."],
    question="Where have you been looking for honour that only Allah can give?"))

# ------------------------------------------------------------------ 25 Al-Mudhill
N.append(dict(
    n=25, ar="الْمُذِلُّ", name_ar="الْمُذِلُّ", tr="Al-Mudhill", en="The Humbler of the Arrogant",
    ur="جسے چاہے ذلیل کرنے والا، انصاف کے ساتھ",
    root="ذ ل ل", root_ar="الْهَوَانُ وَالِانْقِيَادُ وَاللِّينُ",
    root_en="— lowness, being brought low; also yielding and softness.",
    intro=["This root is a good example of how one word can carry two opposite shades. **ذُلّ** can mean humiliation, the lowness of someone brought down. It can also mean a willing humility, the lowering of oneself before someone you love and honour. The Qur'an praises believers who are **أَذِلَّةٌ عَلَى الْمُؤْمِنِينَ**, gentle and humble toward other believers (5:54).",
           "As with Al-Khafid, this Name must be understood together with its pair, Al-Mu'izz. He humbles in justice, and for a reason."],
    pattern=dict(ar="مُفْعِل", bullets=[
        "The causative form again: Al-Mudhill is the One who brings someone to lowness.",
        "He humbles whoever raises himself against Him, whoever rejects the truth out of pride, and whoever oppresses His servants.",
        "His humbling is never unjust. It is a response, and it is always the result of what a person chose."]),
    defbox="الْمُذِلُّ → The One who humbles whoever He wills, in perfect justice, including those who proudly rejected the truth.",
    related="ذُلّ — lowness, humiliation · ذَلِيل — humbled · إِذْلَال — humbling · أَذِلَّة — humble ones",
    quran=[
        dict(ayah=ayah(3, 26, words=(15, 18), tr="\"...and You humble whom You will. In Your hand is [all] good.\""), note=[
            "Look at the words that come straight after: **بِيَدِكَ الْخَيْرُ**, \"in Your hand is all good.\" Even the humbling comes from a hand that is only good. There is no randomness or cruelty in it."]),
        dict(ayah=ayah(7, 13), note=[
            "This is Iblis. He was not lowered for being created from fire. He was lowered for **تَتَكَبَّرَ**, for arrogance. The first act of humbling in history was a response to pride, which is why the believer treats pride as the most dangerous disease of the heart."]),
        dict(ayah=ayah(22, 18, words=(25, 37), tr="\"And he whom Allah humiliates, for him there is no bestower of honour. Indeed, Allah does what He wills.\""), note=[
            "No one can lift up the one that Allah has lowered, and no one has any complaint against His justice."])],
    essence="Al-Mudhill is the One who humbles whomever He wills in perfect justice, so that no arrogance goes unanswered and no one stands above the truth.",
    essence_ur=["الْمُذِل وہ ذات ہے جو کامل انصاف کے ساتھ جسے", "چاہے ذلیل کرتی ہے، تاکہ کوئی تکبر بغیر جواب کے", "نہ رہے اور کوئی حق سے بلند نہ ہو۔"],
    servant=[
        "Two kinds of lowness are in front of you. There is the lowness you choose, before Allah, in sujud, in tears, in saying *I was wrong*. And there is the lowness that He brings on someone who refused to choose it. The first leads to honour; the second to ruin.",
        "So take the humility yourself, while it is still a gift. Humble yourself to your Lord. Be gentle with the believers. Be the one who says sorry first. The one who is humble by choice never meets the humbling that is by force."],
    question="Is there a place in your life where you must lower yourself before Allah, before someone else lowers you?"))

# ------------------------------------------------------------------ 26 As-Sami'
N.append(dict(
    n=26, ar="السَّمِيعُ", name_ar="السَّمِيعُ", tr="As-Sami'", en="The All-Hearing",
    ur="ہر آواز کو سننے اور دعا قبول کرنے والا",
    root="س م ع", root_ar="الْإِدْرَاكُ بِالْأُذُنِ وَالْإِجَابَةُ",
    root_en="— to hear, and also to listen and respond.",
    pattern=dict(ar="فَعِيل", bullets=[
        "The pattern of an established quality: His hearing is part of who He is. It is not something He does only sometimes.",
        "The scholars explain two meanings of this Name. First, He hears everything: every sound, every whisper, every silent thought that the heart says. Second, He hears in order to respond. This is the sense in the words we say in prayer, **سَمِعَ اللَّهُ لِمَنْ حَمِدَهُ**: Allah has heard, and answered, the one who praised Him.",
        "And His hearing is not like ours. The Qur'an gives the rule: *\"There is nothing like Him, and He is the All-Hearing, the All-Seeing\"* (42:11). We affirm what He has described, and we do not compare it to anything."]),
    defbox="السَّمِيعُ → The One who hears every sound and every whisper, near or far, loud or hidden, and who hears the call of His servants and answers.",
    related="سَمْع — hearing · مَسْمُوع — what is heard · اسْتِمَاع — listening · اسْتَجَابَ — to answer",
    quran=[
        dict(ayah=ayah(58, 1), note=[
            "This ayah was revealed about a woman who came to the Prophet ﷺ in distress, speaking about her husband. Aisha said: *\"Blessed is He whose hearing encompasses all sounds. I was in the corner of the room and could not hear some of what she said, and Allah revealed: Allah has heard the speech of the one who argues with you...\"* (Sunan Ibn Majah 188). A woman's private complaint, spoken quietly, was heard from above the seven heavens and a revelation came down because of it."]),
        dict(ayah=ayah(20, 46), note=[
            "Musa and Harun are being sent to Pharaoh, the most powerful man alive. They are afraid. And the answer is two words of presence: **أَسْمَعُ وَأَرَى**, \"I hear and I see.\" That was enough for them to go."]),
        dict(ayah=ayah(2, 127, words=(7, 14), tr="\"Our Lord, accept [this] from us. Indeed You are the Hearing, the Knowing.\""), note=[
            "Look at who is saying this. Ibrahim and Ismail, raising the walls of the Ka'bah, a work of the greatest honour, and the last thing they do is ask: please accept it. And they call Him by exactly this Name."])],
    hadith=[dict(ar="", en="When the companions were raising their voices in dhikr on a journey, the Prophet ﷺ said: \"O people, be gentle with yourselves. You are not calling upon one who is deaf or absent. You are calling upon One who is All-Hearing and near.\"",
                 ref="Sahih al-Bukhari 2992; Sahih Muslim 2704")],
    essence="As-Sami' is the One whose hearing encompasses every sound, who hears the whisper of the heart as clearly as the loudest voice, and who answers the call of those who turn to Him.",
    essence_ur=["السَّمِیع وہ ذات ہے جس کی سماعت ہر آواز کو", "گھیرے ہوئے ہے، جو دل کی سرگوشی کو بھی سنتی ہے،", "اور اپنی طرف پکارنے والوں کی دعا قبول فرماتی ہے۔"],
    servant=[
        "There are things you could never say to anyone: a fear, a shame, a hope that you are afraid will be laughed at. As-Sami' has heard it already. You do not need to find the right words, or the right place. The Prophet ﷺ said you are not calling someone deaf or far away.",
        "And it is also a Name that guards your tongue. If your words reach Him, then the unkind joke, the backbiting, the lie, is all heard. Hold your words with the same care that you want your du'a to be held."],
    question="What have you been carrying in silence that you could say, right now, to the One who hears?"))

# ------------------------------------------------------------------ 27 Al-Basir
N.append(dict(
    n=27, ar="الْبَصِيرُ", name_ar="الْبَصِيرُ", tr="Al-Basir", en="The All-Seeing",
    ur="ہر چیز کو دیکھنے والا",
    root="ب ص ر", root_ar="الرُّؤْيَةُ وَالْعِلْمُ بِالشَّيْءِ",
    root_en="— sight, and the clear perception of a thing.",
    intro=["From this root we also get **بَصِيرَة**, inner sight: the ability to see what something really is, beyond the surface. When the Qur'an says Allah is Al-Basir, it speaks both of seeing and of the complete understanding of what is seen."],
    pattern=dict(ar="فَعِيل", bullets=[
        "Established quality, again: His seeing is perfect and constant.",
        "He sees everything that is visible and everything that is hidden: the ant on a black rock in a dark night, and the intention in a heart.",
        "As with As-Sami', the Qur'an places the two together: **السَّمِيعُ الْبَصِيرُ**. Hearing and seeing complete each other, and nothing escapes either."]),
    defbox="الْبَصِيرُ → The One who sees everything, the visible and the hidden, with perfect clarity, and who knows the reality of what He sees.",
    related="بَصَر — sight · بَصِيرَة — insight · مُبْصِر — one who sees · أَبْصَار — eyes, sights",
    quran=[
        dict(ayah=ayah(26, 218, 219), note=[
            "Look at how personal this is. He sees you when you stand to pray at night, and He sees your movements among the worshippers. The ayah is spoken to the Prophet ﷺ, but every servant who stands in prayer is in it. No sujud is unseen."]),
        dict(ayah=ayah(96, 14), note=[
            "A short and sharp question to the one who thinks nothing is witnessed: *does he not know that Allah sees?*"]),
        dict(ayah=ayah(67, 19, words=(0, 15), tr="\"Do they not see the birds above them with wings outspread and [sometimes] folded in? None holds them [aloft] except the Most Merciful. Indeed He is, of all things, Seeing.\""), note=[
            "Notice that this ayah brings back Name number 1. Al-Basir sees every bird in the sky; Ar-Rahman is the One who holds each one up. Seeing and mercy together."])],
    hadith=[dict(ar="أَنْ تَعْبُدَ اللَّهَ كَأَنَّكَ تَرَاهُ، فَإِنْ لَمْ تَكُنْ تَرَاهُ فَإِنَّهُ يَرَاكَ",
                 en="In the hadith of Jibril, the Prophet ﷺ defined ihsan: \"That you worship Allah as if you see Him, and if you do not see Him, then indeed He sees you.\"",
                 ref="Sahih al-Bukhari 50; Sahih Muslim 8")],
    essence="Al-Basir is the One who sees everything with perfect clarity, the open and the hidden, the great and the small, and who knows the reality behind what He sees.",
    essence_ur=["الْبَصِیر وہ ذات ہے جو ہر چیز کو کامل وضاحت سے دیکھتی", "ہے، ظاہر ہو یا پوشیدہ، بڑی ہو یا چھوٹی، اور جو", "دیکھی ہوئی چیز کی حقیقت کو بھی جانتی ہے۔"],
    servant=[
        "The highest level of worship, ihsan, is built on this Name. Not fear alone, but the awareness of being seen with love and care. A person who prays as if he sees Allah does not need anyone to watch him. And a person who knows he is seen does not feel invisible when no one else notices his sacrifice.",
        "Take both comforts from it. The unseen good you do, the patient day, the secret charity, the kindness no one thanked, is seen. And the hidden fault is seen too, which is exactly why the doors to repentance stay open: you are not hiding anything from the One you are returning to."],
    question="If you knew that your next hour would be watched by the One who sees, what would you change?"))

# ------------------------------------------------------------------ 28 Al-Hakam
N.append(dict(
    n=28, ar="الْحَكَمُ", name_ar="الْحَكَمُ", tr="Al-Hakam", en="The Final Judge & Arbiter",
    ur="حتمی فیصلہ کرنے والا",
    root="ح ك م", root_ar="الْمَنْعُ لِإِصْلَاحٍ",
    root_en="— to prevent, in order to set right; hence to judge and to be wise.",
    intro=["Ibn Faris says that this root is built on one idea: prevention, stopping something from going wrong. A judge **حَاكِم** stops injustice between two people. The bridle on an animal is **حَكَمَة**, because it holds the animal back. And wisdom, **حِكْمَة**, stops a person from doing the foolish thing. They all share one root."],
    pattern=dict(ar="فَعَل", bullets=[
        "Al-Hakam is the one whose judgement ends the matter. No appeal, no overturning, no second court.",
        "Do not confuse it with **الْحَكِيم**, the All-Wise, a Name that comes later in the list. Al-Hakam is the judge; Al-Hakim is the One whose every action is wise. One tells you He decides; the other tells you He decides well.",
        "His rulings are in His laws, in the events of the world, and on the Day when all will stand before Him."]),
    defbox="الْحَكَمُ → The One whose judgement is final, who decides between His servants with perfect justice, and whose ruling no one can change.",
    related="حُكْم — a ruling · حَاكِم — judge · حِكْمَة — wisdom · حَكِيم — wise · تَحْكِيم — appointing a judge",
    quran=[
        dict(ayah=ayah(6, 114, words=(0, 5), tr="\"Then is it other than Allah I should seek as judge, while it is He who has revealed to you the Book, fully explained?\""), note=[
            "The Prophet ﷺ is being asked to find any other judge. The question is a rhetorical one, because everything that a fair judge needs is in the One who revealed the Book: knowledge, justice, and power."]),
        dict(ayah=ayah(10, 109, words=(3, 11), tr="\"And be patient until Allah judges. And He is the best of judges.\""), note=[
            "Patience until He judges. That is a command with a comfort inside it: the case is not closed, and the Judge is not absent."]),
        dict(ayah=ayah(40, 48, words=(6, 12), tr="\"Indeed, Allah has judged between the servants.\""), note=[
            "On the Day when the arrogant and the weak who followed them are talking to each other in the Fire, this is the end of the conversation. The ruling has been given."])],
    hadith=[dict(ar="إِنَّ اللَّهَ هُوَ الْحَكَمُ وَإِلَيْهِ الْحُكْمُ",
                 en="A man named Hani was called Abu al-Hakam, because his people would come to him to settle their disputes. The Prophet ﷺ said to him: \"Indeed Allah is Al-Hakam, and to Him belongs the judgement.\" He asked why he had that name, and when he explained, the Prophet ﷺ said it was good, and changed his name to Abu Shurayh.",
                 ref="Sunan Abi Dawud 4955; Sunan an-Nasa'i 5387")],
    essence="Al-Hakam is the One whose judgement is final and perfect, who decides between all His servants, and whose ruling can never be overturned.",
    essence_ur=["الْحَكَم وہ ذات ہے جس کا فیصلہ حتمی اور کامل ہے،", "جو اپنے تمام بندوں کے درمیان فیصلہ کرتی ہے اور", "جس کے حکم کو کوئی بدل نہیں سکتا۔"],
    servant=[
        "Look at what the Prophet ﷺ did in that hadith. Hani was doing something good: settling disputes. And still the Prophet ﷺ gently changed the name, because only Allah is Al-Hakam in the complete sense. The believer learns from this to hold his own judgement lightly. You can give an opinion, and you can settle a dispute, but the last word does not belong to you.",
        "There is also a heavy comfort. The wrong that was done to you and never put right, the person who was never held to account, the injustice no court ever saw: none of it is outside the Judge. And none of what you did, no matter how well hidden, will be outside it either. So live in such a way that you are ready for the ruling."],
    question="If the Final Judge gave His ruling on your life today, would you be at ease with it?"))

# ------------------------------------------------------------------ 29 Al-'Adl
N.append(dict(
    n=29, ar="الْعَدْلُ", name_ar="الْعَدْلُ", tr="Al-'Adl", en="The Utterly Just",
    ur="کامل انصاف کرنے والا",
    root="ع د ل", root_ar="الِاسْتِقَامَةُ وَالتَّسْوِيَةُ",
    root_en="— straightness, balance and setting things level and equal.",
    intro=["The root is about balance: to make two things equal, to set something straight, to give each thing its true weight. It is the opposite of **جَوْر**, crookedness and injustice. The word **عَدْل** can also mean a counterpart: something exactly equal to another."],
    pattern=dict(ar="فَعْل", bullets=[
        "Like As-Salam, this is a verbal noun (masdar) used as a Name. It does not say that Allah is someone who is just. It says that justice is what He is.",
        "That is why the scholars say that no one can be more just than Him, and that all justice in the world is a faint reflection of His.",
        "He is just in what He commands, in what He decrees, and in how He will reckon: never adding to a person's sin and never withholding the reward of a good deed."]),
    defbox="الْعَدْلُ → The One whose justice is perfect and complete, who never wrongs anyone in the slightest, and who gives each its true due.",
    related="عَدْل — justice · عَادِل — one who is just · عَدَالَة — fairness · اعْتِدَال — balance, moderation · جَوْر — injustice",
    quran=[
        dict(ayah=ayah(4, 40, words=(0, 15), tr="\"Indeed, Allah does not do injustice, even as much as an atom's weight; while if there is a good deed, He multiplies it and gives from Himself a great reward.\""), note=[
            "Look at the two halves. The first is about justice: not even an atom. The second goes beyond justice: the good deed is multiplied. His justice is the floor, and His grace is above it. Bad deeds are counted as they are; good deeds are given far more than they are worth."]),
        dict(ayah=ayah(21, 47), note=[
            "The scales on the Day of Judgement. A grain of mustard seed is brought forward and weighed. Nothing is too small to be seen and nothing will be lost."]),
        dict(ayah=ayah(16, 90, words=(0, 5), tr="\"Indeed, Allah orders justice and good conduct...\""), note=[
            "And this is how He expects His servants to treat each other. The Name is not only to be believed; it is to be lived."])],
    hadith=[dict(ar="يَا عِبَادِي إِنِّي حَرَّمْتُ الظُّلْمَ عَلَى نَفْسِي وَجَعَلْتُهُ بَيْنَكُمْ مُحَرَّمًا فَلَا تَظَالَمُوا",
                 en="In a hadith qudsi, Allah says: \"O My servants, I have forbidden injustice for Myself, and I have made it forbidden among you, so do not wrong one another.\"",
                 ref="Sahih Muslim 2577",
                 note=["He is the One who has every right to do as He wills, and still forbade injustice upon Himself. That is the measure of what it means to be Al-'Adl."])],
    essence="Al-'Adl is the One whose justice is perfect and whose reckoning never wrongs anyone, who gives every right its due and rewards beyond what is deserved.",
    essence_ur=["الْعَدْل وہ ذات ہے جس کا انصاف کامل ہے اور جس کے", "حساب میں کسی پر ذرا سا بھی ظلم نہیں ہوتا؛ جو ہر حق", "دار کو اس کا حق دیتی ہے اور بڑھ کر اجر بھی عطا کرتی ہے۔"],
    servant=[
        "If the Lord is Al-'Adl, then the believer cannot be unjust. Not in a business deal, not in a family argument, not in how he judges a person who disagrees with him. The Prophet ﷺ also told Mu'adh to beware of the du'a of the oppressed, because there is no veil between it and Allah (Sahih al-Bukhari 1496; Sahih Muslim 19).",
        "And it works the other way as well. When you were wronged, you do not have to fight for every last right with bitterness. The matter is in the hands of the One who forbade injustice upon Himself. Hold to justice in your own actions, and leave the complete reckoning to Him."],
    question="Is there someone you have been unfair to, whose right you still owe?"))

# ------------------------------------------------------------------ 30 Al-Latif
N.append(dict(
    n=30, ar="اللَّطِيفُ", name_ar="اللَّطِيفُ", tr="Al-Latif", en="The Subtle, The Gently Kind",
    ur="نہایت باریک بین اور مہربان",
    root="ل ط ف", root_ar="الدِّقَّةُ وَالرِّفْقُ",
    root_en="— fineness and subtlety, and gentle kindness.",
    intro=["This one root carries two meanings that fit together beautifully. The first is **fineness**: something so subtle that it cannot be grasped. The second is **gentleness**: to deal with someone kindly, in a soft and caring way. When both are in the same Name, the meaning is that He knows the finest hidden details of what is good for you, and He brings it to you gently."],
    pattern=dict(ar="فَعِيل", bullets=[
        "The pattern of an established quality: this subtlety and gentleness are always in Him.",
        "Al-Ghazali explains Al-Latif as the One who knows the fine details of what benefits His servants and delivers it to them by the gentlest means.",
        "So you may not even know that you are being treated with lutf. The care often arrives in ways that look, at first, like something else."]),
    defbox="اللَّطِيفُ → The One who knows the subtlest details of every matter and brings good to His servants in ways that are gentle and unseen.",
    related="لُطْف — gentleness, kindness · لَطَافَة — subtlety · لَطِيف — subtle · أَلْطَافٌ — kindnesses",
    quran=[
        dict(ayah=ayah(12, 100, words=(37, 46), tr="\"Indeed, my Lord is Subtle in what He wills. Indeed, it is He who is the Knowing, the Wise.\""), note=[
            "This is Yusuf, after the whole story. A well, slavery, a false accusation and a prison, and every step led to a throne and to his family coming back together. When he looks back, he does not say \"I worked it out.\" He says: my Lord is Latif. All of it was a subtle plan that none of us could see from inside."]),
        dict(ayah=ayah(42, 19, words=(0, 6), tr="\"Allah is Subtle toward His servants; He gives provision to whom He wills.\""), note=[
            "**لَطِيفٌ بِعِبَادِهِ**: gentle to His servants. Notice that it is a general statement. It is not about the prophets alone."]),
        dict(ayah=ayah(6, 103, words=(4, 9), tr="\"...and He perceives all vision, and He is the Subtle, the All-Aware.\""), note=[
            "And the two Names that always accompany this one: Al-Latif for the subtle gentleness, Al-Khabir for the full awareness. The One who is gentle with you knows exactly what you need."])],
    hadith=[dict(ar="عَجَبًا لِأَمْرِ الْمُؤْمِنِ إِنَّ أَمْرَهُ كُلَّهُ خَيْرٌ، وَلَيْسَ ذَاكَ لِأَحَدٍ إِلَّا لِلْمُؤْمِنِ",
                 en="The Prophet ﷺ said: \"How wonderful is the affair of the believer; all of his affair is good, and that is for no one except the believer. If something good befalls him, he is grateful, and that is good for him. If something harmful befalls him, he is patient, and that is good for him.\"",
                 ref="Sahih Muslim 2999")],
    essence="Al-Latif is the One who knows the finest details of every matter and brings good to His servants by gentle and hidden means, often in ways they do not notice.",
    essence_ur=["اللَّطِیف وہ ذات ہے جو ہر معاملے کی باریک ترین", "تفصیل جانتی ہے اور اپنے بندوں تک بھلائی نرم اور", "پوشیدہ طریقوں سے پہنچاتی ہے، اکثر ایسے کہ انہیں پتا بھی نہ چلے۔"],
    servant=[
        "Look back at your own life, and you will find a few moments where something you hated turned out to be what saved you. A closed door that kept you out of something worse. A delay that put you in the right place. A person who left, and the person who came in their place. You did not see Al-Latif working, and yet He was.",
        "So when the thing in front of you does not make sense, do what Yusuf did in the pit: be patient, because the story is not finished. Trust that the same gentle subtlety is still working. And do the same for others. Be latif with the people who are fragile, speak softly, help without making them feel the weight of it."],
    question="Looking back, where has Allah been gentle with you in a way you only noticed later?"))

# ------------------------------------------------------------------ 31 Al-Khabir
N.append(dict(
    n=31, ar="الْخَبِيرُ", name_ar="الْخَبِيرُ", tr="Al-Khabir", en="The All-Aware",
    ur="ہر ظاہر و پوشیدہ بات سے مکمل باخبر",
    root="خ ب ر", root_ar="الْعِلْمُ بِبَوَاطِنِ الْأُمُورِ",
    root_en="— knowledge of the inner reality of things, gained by close acquaintance.",
    intro=["**خِبْرَة** in Arabic is not general knowledge. It is the deep, inner knowledge of an expert who knows the thing from the inside. A person who has **خِبْرَة** knows what is behind the surface. That is the shade of meaning in this Name, and it is why it is paired so often with Al-'Alim and Al-Latif."],
    pattern=dict(ar="فَعِيل", bullets=[
        "An established quality: His awareness of the inner reality is always complete.",
        "Al-'Alim speaks of the breadth of His knowledge: that He knows everything. Al-Khabir speaks of its depth: that He knows what is inside, the reality and the secret.",
        "He knows the intention behind the deed, the reason behind the words, and the hidden state of the heart."]),
    defbox="الْخَبِيرُ → The One who is fully aware of the inner reality of everything: what is hidden, what is intended, and what is concealed in hearts.",
    related="خَبَر — news, information · خِبْرَة — expertise · مُخْتَبَر — a place of testing · اخْتِبَار — a test",
    quran=[
        dict(ayah=ayah(49, 13, words=(11, 20), tr="\"Indeed, the most noble of you in the sight of Allah is the most righteous of you. Indeed, Allah is Knowing and Aware.\""), note=[
            "The ayah ends with this Name for a reason. Only Al-Khabir can say who is truly the most righteous, because only He knows the heart. People look at the outside. He looks at what is inside, and that is the only measure."]),
        dict(ayah=ayah(25, 58, words=(8, 13), tr="\"And sufficient is He to be, with the sins of His servants, Aware.\""), note=[
            "A comfort to the one who was wronged, and a warning to the one who wronged. He needs no one to report what was done."]),
        dict(ayah=ayah(67, 14), note=[
            "Here the Name appears beside Al-Latif, in an unanswerable question: how could the One who created you not know you?"])],
    hadith=[dict(ar="إِنَّ اللَّهَ لَا يَنْظُرُ إِلَى صُوَرِكُمْ وَأَمْوَالِكُمْ وَلَكِنْ يَنْظُرُ إِلَى قُلُوبِكُمْ وَأَعْمَالِكُمْ",
                 en="The Prophet ﷺ said: \"Indeed Allah does not look at your appearances or your wealth, but He looks at your hearts and your deeds.\"",
                 ref="Sahih Muslim 2564")],
    essence="Al-Khabir is the One who is fully aware of the hidden reality of all things: the intentions, the secrets, the unseen conditions of every heart.",
    essence_ur=["الْخَبِیر وہ ذات ہے جو ہر چیز کی پوشیدہ حقیقت سے", "مکمل باخبر ہے: نیتیں، راز اور ہر دل کی چھپی ہوئی", "کیفیت سب اس کے علم میں ہے۔"],
    servant=[
        "This Name can be both frightening and freeing. Frightening, because there is no performance you can put on in front of Al-Khabir; He knows when your prayer is for Him and when it is for those watching. Freeing, because no one can misjudge you before Him. You can be misunderstood by everyone, and still be fully known by the One who matters.",
        "It also takes a weight off your judgement of others. You see someone's behaviour; you do not see their heart. Al-Khabir does. When you are tempted to decide who is better or worse, remember that the decision belongs to the One who is Aware."],
    question="If the One who knows your heart read your intentions today, would He find them clean?"))

# ------------------------------------------------------------------ 32 Al-Halim
N.append(dict(
    n=32, ar="الْحَلِيمُ", name_ar="الْحَلِيمُ", tr="Al-Halim", en="The Forbearing, Slow to Punish",
    ur="بردبار، سزا دینے میں جلدی نہ کرنے والا",
    root="ح ل م", root_ar="الْأَنَاةُ وَرَجَاحَةُ الْعَقْلِ",
    root_en="— composure, patience and a steady, mature mind that does not rush.",
    intro=["**حِلْم** is a rich word. It means to stay calm and unhurried when you have every reason to react, and to have the strength to hold back when you could strike. It is not weakness. It is power that chooses to wait. The same root gives **حُلُم**, which can mean a dream, and the age of maturity, because it is about a mind that has become steady."],
    pattern=dict(ar="فَعِيل", bullets=[
        "An established quality: forbearance is always in Him.",
        "Al-Ghazali explains Al-Halim as the One who sees the disobedience of the disobedient and is not provoked into a hasty punishment. He gives time, because He is not afraid that they will escape.",
        "Do not confuse it with weakness or with neglect. His delay is mercy with a time limit. At a time He knows, it ends."]),
    defbox="الْحَلِيمُ → The One who sees every sin and does not hasten to punish, who gives time to return, and whose patience is from power, not weakness.",
    related="حِلْم — forbearance · حَلِيم — forbearing · أَنَاة — deliberateness · حُلُم — maturity of mind; a dream",
    quran=[
        dict(ayah=ayah(35, 45), note=[
            "This ayah is stunning if you read it slowly. If Allah were to take people to account for what they earned, there would not be a single creature left on the earth's surface. We are alive, right now, because of this Name. Every day that a person gets to wake up after a sin is a day of Al-Halim."]),
        dict(ayah=ayah(2, 225, words=(11, 14), tr="\"And Allah is Forgiving and Forbearing.\""), note=[
            "Here the Name comes beside Al-Ghafur. Forbearance means that He gives time; forgiveness means that He pardons when we use it."]),
        dict(ayah=ayah(17, 44, words=(17, 21), tr="\"Indeed, He is ever Forbearing and Forgiving.\""), note=[
            "The ayah comes right after one that tells us that every creature in the heavens and earth glorifies Him, but we do not understand their glorification. And still, He is forbearing with us."])],
    hadith=[dict(ar="إِنَّ فِيكَ خَصْلَتَيْنِ يُحِبُّهُمَا اللَّهُ: الْحِلْمُ وَالْأَنَاةُ",
                 en="The Prophet ﷺ said to Ashajj of 'Abd al-Qays: \"You have two qualities that Allah loves: forbearance and deliberateness.\"",
                 ref="Sahih Muslim 17",
                 note=["And in another hadith, he said that no one is more patient than Allah upon hearing something harmful: they claim that He has a child, and still He gives them health and provision (Sahih al-Bukhari 6099; Sahih Muslim 2804)."])],
    essence="Al-Halim is the One who sees every disobedience and does not hasten to punish, whose patience comes from perfect power, and who gives His servants time to return.",
    essence_ur=["الْحَلِیم وہ ذات ہے جو ہر نافرمانی کو دیکھ کر بھی", "سزا میں جلدی نہیں کرتی؛ اس کا صبر کامل قدرت", "سے ہے، اور وہ بندوں کو لوٹنے کی مہلت دیتی ہے۔"],
    servant=[
        "Two reflections. First, about yourself. The time that you have been given after your sins is not a sign that they did not matter. It is an invitation. Do not use His forbearance as an excuse to delay. Treat each day as a chance that was held out to you by a patient Lord.",
        "Second, about others. He is Al-Halim with people who insult Him. Can you not be a little patient with a family member, a colleague, a child? The Prophet ﷺ taught that the strong one is the one who controls himself in anger. When you hold back a harsh word, you are living a small portion of this Name."],
    question="With whom are you being quick to anger, when Allah has been patient with you?"))

# ------------------------------------------------------------------ 33 Al-'Azim
N.append(dict(
    n=33, ar="الْعَظِيمُ", name_ar="الْعَظِيمُ", tr="Al-'Azim", en="The Magnificent, The Supremely Great",
    ur="نہایت عظمت والا",
    root="ع ظ م", root_ar="الْكِبَرُ وَالْقَدْرُ وَالْجَلَالُ",
    root_en="— greatness in size, in rank and in majesty; also the bone (عَظْم), the strong frame of the body.",
    pattern=dict(ar="فَعِيل", bullets=[
        "The pattern of an established quality: His greatness is always His, in every sense, and cannot be increased or lessened.",
        "The scholars explain that Al-'Azim means that Allah is greater than anything the mind can encompass. The Qur'an says that people *\"do not encompass Him in knowledge\"* (20:110).",
        "This is not just a description. It is the feeling the heart should have: that anything we say of Him is small next to what He is."]),
    defbox="الْعَظِيمُ → The One whose greatness is complete and beyond all comprehension, before whom everything else is small.",
    related="عَظَمَة — greatness · عَظِيم — great · تَعْظِيم — honouring, glorifying · عَظْم — bone",
    quran=[
        dict(ayah=ayah(2, 255, words=(40, 50), tr="\"His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.\""), note=[
            "This is the end of Ayat al-Kursi, the greatest ayah in the Qur'an. After describing His life, His power, His knowledge and His throne, the ayah ends with two Names: Al-'Aliyy, the Most High, and Al-'Azim, the Most Great. The Kursi alone, which is only His footstool, extends over the heavens and the earth. And keeping all of it does not tire Him."]),
        dict(ayah=ayah(56, 74), note=[
            "The command to respond to greatness with tasbih. When you know who He is, the natural reaction is to glorify."]),
        dict(ayah=ayah(39, 67, words=(0, 13), tr="\"And they did not appreciate Allah as He should be appreciated, while the earth entirely will be [within] His grip on the Day of Resurrection, and the heavens will be folded in His right hand. Exalted is He.\""), note=[
            "The earth, with all its mountains and oceans, will be in His grip. This is the one that we have been treating as the entire world."])],
    hadith=[dict(ar="كَلِمَتَانِ خَفِيفَتَانِ عَلَى اللِّسَانِ، ثَقِيلَتَانِ فِي الْمِيزَانِ، حَبِيبَتَانِ إِلَى الرَّحْمَٰنِ: سُبْحَانَ اللَّهِ وَبِحَمْدِهِ، سُبْحَانَ اللَّهِ الْعَظِيمِ",
                 en="The Prophet ﷺ said: \"There are two words that are light on the tongue, heavy on the scale, and beloved to Ar-Rahman: Subhan Allahi wa bihamdihi, Subhan Allahil-'Azim.\"",
                 ref="Sahih al-Bukhari 6406; Sahih Muslim 2694",
                 note=["Notice the last Name in this hadith: **الرَّحْمَٰن**. The book began with Ar-Rahman, and here is Al-'Azim beside it. The One of unbounded greatness is the One of unbounded mercy. The greatest is also the most merciful."]),
            dict(ar="لَا إِلَٰهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ، لَا إِلَٰهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ، لَا إِلَٰهَ إِلَّا اللَّهُ رَبُّ السَّمَاوَاتِ وَرَبُّ الْأَرْضِ وَرَبُّ الْعَرْشِ الْكَرِيمِ",
                 en="The du'a that the Prophet ﷺ used to say in times of distress: \"There is no god but Allah, the Magnificent, the Forbearing. There is no god but Allah, Lord of the Mighty Throne. There is no god but Allah, Lord of the heavens, Lord of the earth, and Lord of the Noble Throne.\"",
                 ref="Sahih al-Bukhari 6345; Sahih Muslim 2730")],
    essence="Al-'Azim is the One whose greatness is complete and beyond the grasp of any mind, so that everything else, in comparison, is small.",
    essence_ur=["الْعَظِیم وہ ذات ہے جس کی عظمت کامل اور ہر عقل", "کی گرفت سے بالاتر ہے، یہاں تک کہ اس کے مقابلے", "میں ہر دوسری چیز چھوٹی ہے۔"],
    servant=[
        "Every time you bend in ruku', you say **سُبْحَانَ رَبِّيَ الْعَظِيمِ**. Not as a formula, but as a recalibration. Your worries, your plans, even the great fears of your life, all of them are small in front of the One you are bowing to. A person who knows Al-'Azim does not collapse in front of problems, because he has seen what real greatness is.",
        "It also quietly reorders your life. When something is truly great in your eyes, you give it your best. If Allah is the greatest, then He should get the best of your time, your attention and your heart, not the leftover. The more the heart holds His greatness, the lighter everything else becomes."],
    question="What is great in your eyes today, and how does it compare to the One who is Al-'Azim?"))


ALL = N
