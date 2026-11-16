"""Names 4-13 (Al-Quddus ... Al-Musawwir) + the Khaliq/Bari'/Musawwir chapter."""
from lib import *

N = []

# ------------------------------------------------------------------ 4 Al-Quddus
N.append(dict(
    n=4, ar="الْقُدُّوسُ", name_ar="الْقُدُّوسُ", tr="Al-Quddus", en="The Most Pure & Holy",
    ur="نہایت پاک اور ہر عیب سے بالکل منزہ",
    root="ق د س", root_ar="الطُّهْرُ وَالنَّزَاهَةُ",
    root_en="— purity, and being far removed from every fault and impurity.",
    pattern=dict(ar="فُعُّول", bullets=[
        "This pattern is an intensive one: it conveys purity that is not merely present, but complete and overflowing.",
        "So قُدُّوس does not simply mean \"pure\" — it means purity at its absolute height, with no trace of defect anywhere in it.",
        "Another word on this same pattern is سُبُّوح — utterly free of every fault. The Prophet ﷺ joined the two together in his ruku' and sujud (see below)."]),
    defbox="الْقُدُّوسُ → The One who is absolutely pure, free of every defect, flaw and imperfection, and far above anything unworthy of Him.",
    after_def=["The mufassirun, such as al-Tabari and Ibn Kathir, explain Al-Quddus as the One who is perfectly pure and far above every deficiency. Nothing about Allah, His Names, His attributes or His actions carries any fault."],
    related="قُدْس — holiness, purity · مُقَدَّس — sanctified · تَقْدِيس — declaring holy · سُبُّوح — utterly free of fault · تَسْبِيح — glorifying",
    quran=[
        dict(ayah=ayah(59, 23), note=[
            "Notice where Al-Quddus sits in this ayah: straight after Al-Malik, the King. A king can be powerful and still flawed. Here the Qur'an places the Name Al-Quddus beside the Name Al-Malik, so that you know His sovereignty is not like any worldly rule. His authority is perfectly pure: no injustice in it, no weakness, no selfishness, no mistake.",
            "And the ayah ends where it must: *\"Exalted is Allah above whatever they associate with Him.\"* Everything that insults His purity is cleared away in one line."]),
        dict(ayah=ayah(2, 30, words=(17, 22), tr="\"...while we glorify You with praise and declare Your holiness.\""), note=[
            "This is the angels speaking, and the very word they use comes from this root: **وَنُقَدِّسُ لَكَ**. To declare Allah holy is to keep your thoughts about Him clean."])],
    hadith=[dict(ar="سُبُّوحٌ قُدُّوسٌ رَبُّ الْمَلَائِكَةِ وَالرُّوحِ",
                 en="\"Most Glorified, Most Holy, Lord of the angels and the Spirit.\" This is what the Prophet ﷺ used to say in his ruku' and sujud.",
                 ref="Sahih Muslim 487")],
    essence="Al-Quddus is the One who is perfectly pure and holy, free from every defect, whose Names, attributes and actions are all beyond any fault.",
    essence_ur=["الْقُدُّوس وہ ذات ہے جو ہر عیب، نقص اور کمزوری", "سے مکمل طور پر پاک اور بلند ہے؛ اس کے نام، صفات", "اور افعال سب ہر خامی سے منزہ ہیں۔"],
    servant=[
        "If Allah is Al-Quddus, then every complaint that sounds like an accusation against Him is a thought that must be put down. When a test comes, the heart sometimes whispers that this is unfair, that it makes no sense. Al-Quddus is the answer: whatever you cannot understand, the fault is never in Him. It is in your limited view, never in His perfect wisdom.",
        "And He loves those who clean themselves for Him: *\"Indeed, Allah loves those who are constantly repentant and loves those who purify themselves\"* (Qur'an 2:222). Purity is not only wudu. It is a clean tongue, a clean heart, clean earnings, clean intentions. Every time you say **سُبْحَانَ اللَّهِ**, you are doing what the angels do: keeping Allah far from any fault in your mind."],
    question="What are you carrying in your heart that you would be ashamed to place before the Most Pure?"))

# ------------------------------------------------------------------ 5 As-Salam
N.append(dict(
    n=5, ar="السَّلَامُ", name_ar="السَّلَامُ", tr="As-Salam", en="The Source of Peace & Perfection",
    ur="سلامتی کا سرچشمہ، ہر عیب اور نقص سے پاک",
    root="س ل م", root_ar="السَّلَامَةُ مِنَ الْعُيُوبِ وَالْآفَاتِ",
    root_en="— safety, soundness, being whole and free from every defect and harm.",
    intro=["This one root gives us a whole family of words that every Muslim knows: **سَلَام** (peace), **سَلَامَة** (safety), **إِسْلَام** (peaceful submission to Allah) and **مُسْلِم** (one who submits). To be Muslim is to be in the family of this Name."],
    pattern=dict(ar="سَلَام", bullets=[
        "سَلَام is a verbal noun (masdar) used as a Name. It does not describe someone who has peace; it names peace itself.",
        "Scholars explain two meanings: He is free from every defect and imperfection, and from Him alone comes all safety and peace for His creation.",
        "The first meaning is about Him; the second is about us. Both come from one source."]),
    defbox="السَّلَامُ → The One who is perfectly free of every defect, and from whom all peace and safety come.",
    related="سَلَامَة — safety · إِسْلَام — submission · مُسْلِم — one who submits · تَسْلِيم — greeting; surrendering · دَارُ السَّلَامِ — the Home of Peace",
    quran=[
        dict(ayah=ayah(59, 23, words=(0, 10), tr="\"He is Allah, other than whom there is no deity, the Sovereign, the Pure, the Perfection...\""), note=[
            "In this ayah the Name sits between Al-Quddus and Al-Mu'min. Al-Quddus declares that He is free of all fault; As-Salam adds that this freedom is complete and that peace begins with Him."]),
        dict(ayah=ayah(10, 25, tr="\"And Allah invites to the Home of Peace and guides whom He wills to a straight path.\""), note=[
            "Even Paradise is named after this Name: **دَارُ السَّلَامِ**. The final home of the believer is a home named after Allah Himself. And the first thing its people will hear is peace:"]),
        dict(ayah=ayah(36, 58, tr="\"Peace,\" a word from a Merciful Lord.\""), note=[
            "Imagine the moment: after every hardship, a greeting of peace spoken to you directly, from the Lord who is both As-Salam and Ar-Raheem."])],
    hadith=[dict(ar="اللَّهُمَّ أَنْتَ السَّلَامُ وَمِنْكَ السَّلَامُ، تَبَارَكْتَ يَا ذَا الْجَلَالِ وَالْإِكْرَامِ",
                 en="\"O Allah, You are As-Salam, and from You is all peace. Blessed are You, O Possessor of Majesty and Honour.\" The Prophet ﷺ said this after finishing the prayer, after asking forgiveness three times.",
                 ref="Sahih Muslim 591")],
    essence="As-Salam is the One who is perfect and free of all fault, and the source from whom all peace, safety and wellbeing come to His creation.",
    essence_ur=["السَّلَام وہ ذات ہے جو ہر عیب سے پاک اور کامل ہے،", "اور جس کی طرف سے اس کی مخلوق کو ہر قسم کی", "سلامتی اور امن عطا ہوتا ہے۔"],
    servant=[
        "Look at where the believer ends the prayer: with the Name As-Salam on the tongue and the word سلام on both shoulders. We begin our meeting with every Muslim in the Name of Allah, and we end our prayer the same way. Peace is not a mood you chase. It is something that is given by the One who owns it.",
        "So when your heart is restless, do not look for peace in the thing you lost or the thing you are missing. Ask the One whose Name it is. And pass it on. The Prophet ﷺ said that you will not enter Paradise until you believe, and you will not believe until you love one another, and he then taught the way: *\"Spread salam among yourselves\"* (Sahih Muslim 54). Every greeting you give is a small trace of this Name carried across the earth."],
    question="Where do you go looking for peace, and have you first asked the One whose Name it is?"))

# ------------------------------------------------------------------ 6 Al-Mu'min
N.append(dict(
    n=6, ar="الْمُؤْمِنُ", name_ar="الْمُؤْمِنُ", tr="Al-Mu'min", en="The Granter of Security & Affirmer of Truth",
    ur="امن عطا کرنے والا اور سچ کی تصدیق کرنے والا",
    root="أ م ن", root_ar="الْأَمْنُ وَالْأَمَانَةُ وَالتَّصْدِيقُ",
    root_en="— security, trust and affirmation.",
    intro=["From this same root come three words you already know: **أَمْن** (security), **أَمَانَة** (a trust) and **إِيمَان** (faith). In Arabic, faith is not only a belief. It is the feeling of safety that comes from trusting someone, and the act of confirming that what they say is true."],
    pattern=dict(ar="مُفْعِل", bullets=[
        "مُؤْمِن is the active form of the verb آمَنَ, which can mean \"to grant security\" as well as \"to believe.\"",
        "When this word is used for the servant, it means the one who believes. When it is used for Allah, the scholars explain that it carries two meanings that fit His majesty: He is the One who grants security, and He is the One who confirms the truth.",
        "It never means that Allah believes in something above Him. Nothing is above Him."]),
    defbox="الْمُؤْمِنُ → The One who gives security to His creation and confirms the truth of His promises and His messengers.",
    after_def=["Ibn Kathir, in his tafsir of Surah al-Hashr, relates from Ibn 'Abbas that Al-Mu'min means the One who gave His creation security from being wronged by Him. The second meaning is that He affirms His own word: what He has promised is true, and the messengers He sent were truthful."],
    related="أَمْن — security · أَمَان — safety · أَمَانَة — a trust · إِيمَان — faith · مُؤْمِن — believer",
    quran=[
        dict(ayah=ayah(106, 4, tr="\"Who has fed them, [saving them] from hunger, and made them safe, [saving them] from fear.\""), note=[
            "Here the verb **آمَنَهُم** appears: He made them safe. This is the action of Al-Mu'min. Hunger and fear are the two things that most unsettle a person, and He removed both. Every night that you slept without fear, every road you travelled safely, was this Name acting upon your life."]),
        dict(ayah=ayah(6, 82, tr="\"They who believe and do not mix their belief with injustice, those will have security, and they are [rightly] guided.\""), note=[
            "And the link between faith and safety is made explicit here: **لَهُمُ الْأَمْنُ**. Those who hold their faith clean have security. It is Al-Mu'min who gives it."]),
        dict(ayah=ayah(13, 28, tr="\"Those who have believed and whose hearts are assured by the remembrance of Allah. Unquestionably, by the remembrance of Allah hearts are assured.\""), note=[
            "The security Al-Mu'min gives is not only outward. It goes into the heart itself."])],
    hadith=[dict(ar="الْمُؤْمِنُ مَنْ أَمِنَهُ النَّاسُ عَلَى دِمَائِهِمْ وَأَمْوَالِهِمْ",
                 en="\"The believer is the one from whom people are safe regarding their blood and their wealth.\"",
                 ref="Jami' at-Tirmidhi 2627; Sunan an-Nasa'i 4995")],
    essence="Al-Mu'min is the One who grants safety and security to His creation and confirms the truth of His word, His promises and His messengers.",
    essence_ur=["الْمُؤْمِن وہ ذات ہے جو اپنی مخلوق کو امن اور", "حفاظت عطا کرتی ہے، اور اپنے وعدوں، اپنے کلام", "اور اپنے رسولوں کی سچائی کی تصدیق فرماتی ہے۔"],
    servant=[
        "If Allah is Al-Mu'min, then your safety was never in your own hands. The locked door, the savings account, the careful plan: all of these are only means. The One who actually keeps you safe is the One who gives amn. That should not make you careless; it should make you calm.",
        "And there is a second lesson in the hadith above. Your imaan is measured partly by how safe others are around you: from your hand, your tongue, your temper, your dishonesty. To hold the title **مُؤْمِن** is to become, in a small human way, a source of security for the people around you, in the shadow of the One who is truly Al-Mu'min."],
    question="Do the people around you feel safe in your company: with their secrets, their reputation and their trust?"))

# ------------------------------------------------------------------ 7 Al-Muhaymin
N.append(dict(
    n=7, ar="الْمُهَيْمِنُ", name_ar="الْمُهَيْمِنُ", tr="Al-Muhaymin", en="The Guardian, Watchful Over All",
    ur="ہر چیز کا نگہبان اور نگران",
    root="ه ي م ن", root_ar="الرَّقِيبُ وَالشَّاهِدُ وَالْحَافِظُ",
    root_en="— to watch over, to be a witness, to guard and oversee.",
    intro=["This is one of the few Names built on a four-letter root. Its sense is of one who stands over something completely: watching it, protecting it and bearing witness to it, so that nothing escapes his oversight."],
    pattern=dict(ar="مُفَيْعِل", bullets=[
        "The pattern gives the sense of active, constant oversight, not a one-time act.",
        "Among the early scholars, Ibn 'Abbas explained the word as \"trustworthy guardian\" (أَمِين), and Mujahid as \"witness\" (شَاهِد). Both are about the same reality: complete knowledge together with complete care.",
        "The Qur'an uses the same word of itself: it is **مُهَيْمِنًا عَلَيْهِ**, a guardian and standard over the earlier scriptures (Qur'an 5:48)."]),
    defbox="الْمُهَيْمِنُ → The One who watches over everything, bears witness to everything, and preserves everything.",
    related="رَقِيب — watchful observer · شَهِيد — witness · حَفِيظ — preserver · وَكِيل — disposer of affairs",
    quran=[
        dict(ayah=ayah(4, 1, words=(23, 28), tr="\"Indeed, Allah is ever, over you, an Observer.\""), note=[
            "**رَقِيبًا** — the same meaning as Al-Muhaymin. Notice that this reminder comes in the very ayah where the Qur'an speaks of family ties and the womb. The One who watches over you is the One who also watches how you treat your relatives."]),
        dict(ayah=ayah(50, 16), note=[
            "Closer than the jugular vein. Al-Muhaymin is not watching from a great distance; His knowledge is nearer to you than your own pulse. Scholars explain this nearness as His knowledge and encompassing oversight, in a way that befits Him."])],
    hadith=[dict(ar="احْفَظِ اللَّهَ يَحْفَظْكَ، احْفَظِ اللَّهَ تَجِدْهُ تُجَاهَكَ",
                 en="The Prophet ﷺ advised Ibn 'Abbas: \"Be mindful of Allah and He will protect you. Be mindful of Allah and you will find Him before you.\"",
                 ref="Jami' at-Tirmidhi 2516 — hasan sahih")],
    essence="Al-Muhaymin is the One who watches over all, witnesses all, and guards all, so that nothing in the heavens or the earth is outside His knowledge and care.",
    essence_ur=["الْمُهَیْمِن وہ ذات ہے جو ہر چیز پر نگہبان، ہر بات کی", "گواہ اور ہر شے کی حفاظت کرنے والی ہے؛ آسمانوں اور", "زمین میں کوئی چیز اس کے علم اور نگرانی سے باہر نہیں۔"],
    servant=[
        "Two things come together in this Name, and they are meant to be held together. First, you are watched: nothing you do is missed. Second, you are guarded: nothing that happens to you is outside His oversight. One calls you to sincerity; the other calls you to peace.",
        "The hadith of Ibn 'Abbas teaches the exchange. Guard what Allah has asked you to guard, His commands and limits, and Al-Muhaymin guards you: your faith, your family, your body, your end. The servant who stays in this exchange is never really alone, even in an empty room."],
    question="When no one is watching, who do you become, and does that match the person you are in front of others?"))

# ------------------------------------------------------------------ 8 Al-'Aziz
N.append(dict(
    n=8, ar="الْعَزِيزُ", name_ar="الْعَزِيزُ", tr="Al-'Aziz", en="The Almighty, The Ever-Honoured",
    ur="سب پر غالب، کبھی مغلوب نہ ہونے والا، عزت والا",
    root="ع ز ز", root_ar="الْقُوَّةُ وَالشِّدَّةُ وَالْغَلَبَةُ وَالنُّدْرَةُ",
    root_en="— strength, firmness, overpowering, and being rare and out of reach.",
    intro=["Ibn Faris explains that this root points to firmness and strength. The hard, unyielding ground is called أَرْضٌ عَزَازٌ. Something rare and hard to reach is also called عَزِيز. That is why this word carries the sense of both power and honour."],
    table=(["Kind of 'Izzah", "Meaning", "In Allah's case"], [
        ["عِزَّةُ الْقُوَّةِ", "Strength", "He has all power; none can match it"],
        ["عِزَّةُ الِامْتِنَاعِ", "Being out of reach", "Nothing can touch Him with harm or lessen Him"],
        ["عِزَّةُ الْقَهْرِ", "Overpowering", "He overcomes everything and is overcome by nothing"]]),
    pattern=dict(ar="فَعِيل", bullets=[
        "As with Ar-Raheem, this pattern describes a quality that is firmly established in its owner.",
        "Ibn al-Qayyim explains that 'izzah has these three meanings. Allah is Al-'Aziz in all three together, perfectly and forever."]),
    defbox="الْعَزِيزُ → The One who is perfect in strength, out of reach of every harm, and who overcomes all and is overcome by none.",
    related="عِزَّة — might, honour · عِزّ — glory · أَعَزّ — mightier · مُعِزّ — the One who bestows honour",
    quran=[
        dict(ayah=ayah(35, 10, words=(0, 7), tr="\"Whoever desires honour, then to Allah belongs all honour.\""), note=[
            "This is the great secret of the Name. If you want honour, there is no other door but His. Many people look for it in rank, wealth, followers, or in pleasing others. The ayah closes all of those doors and leaves open the only one."]),
        dict(ayah=ayah(63, 8, words=(9, 13), tr="\"And to Allah belongs [all] honour, and to His Messenger, and to the believers.\""), note=[
            "And see how generously He shares what is His: the honour that belongs to Him He gives to His Messenger and to the believers. Honour is borrowed from Al-'Aziz by those who stay with Him."])],
    hadith=[dict(ar="أَعُوذُ بِعِزَّتِكَ الَّذِي لَا إِلَٰهَ إِلَّا أَنْتَ الَّذِي لَا يَمُوتُ وَالْجِنُّ وَالْإِنْسُ يَمُوتُونَ",
                 en="\"I seek refuge in Your 'Izzah — there is no god but You — who does not die, while the jinn and mankind die.\" From the du'a of the Prophet ﷺ.",
                 ref="Sahih al-Bukhari 7383; Sahih Muslim 2717")],
    essence="Al-'Aziz is the One of complete might, beyond reach, who overcomes all things and is overcome by nothing, and who gives honour to whomever He wills.",
    essence_ur=["الْعَزِیز وہ ذات ہے جو کامل قوت اور غلبے والی ہے،", "جس تک کوئی نہیں پہنچ سکتا، جو سب پر غالب ہے", "اور جسے چاہے عزت عطا کرتی ہے۔"],
    servant=[
        "Even Iblis knew this Name. When he was cast out he swore **فَبِعِزَّتِكَ**, \"by Your 'Izzah\" (Qur'an 38:82). He recognised exactly who Allah is, and still refused to humble himself. Knowing the Name is not enough; the Name must be answered with submission.",
        "Real honour is not the opposite of humility. It comes through it. The believer who bows only to Allah finds that he does not have to bow to anyone else. And the person who chases honour through disobedience ends up with neither. The way to be honoured is to belong to the One who is Al-'Aziz."],
    question="Whose approval are you chasing for honour, and is it the One who owns all of it?"))

# ------------------------------------------------------------------ 9 Al-Jabbar
N.append(dict(
    n=9, ar="الْجَبَّارُ", name_ar="الْجَبَّارُ", tr="Al-Jabbar", en="The Compeller & Mender of the Broken",
    ur="ٹوٹے ہوئے دلوں کو جوڑنے والا، سب پر زبردست اختیار والا",
    root="ج ب ر", root_ar="إِصْلَاحُ الْكَسْرِ وَالْقَهْرُ وَالْعُلُوُّ",
    root_en="— mending what is broken, overpowering by force, and being lofty and high.",
    intro=["The scholars, from the linguists to the mufassirun, mention three meanings for this one Name. **First**, to mend and restore what is broken: a bone that is set is said to be جُبِرَ. **Second**, to compel and overpower, so that His will is carried out. **Third**, loftiness: a tall palm tree is called نَخْلَةٌ جَبَّارَةٌ. All three are true of Allah."],
    pattern=dict(ar="فَعَّال", bullets=[
        "This pattern conveys intensity and repetition: someone who does the action again and again, completely.",
        "So Al-Jabbar does not mend once; He mends continually. He does not compel weakly; He compels completely.",
        "You will meet this pattern again soon, in Al-Ghaffar, Al-Qahhar, Al-Wahhab, Ar-Razzaq and Al-Fattah."]),
    defbox="الْجَبَّارُ → The One who mends the broken, whose will is carried out over all, and who is exalted above all.",
    after_def=["When this word is used for a human being, it is a blame. The Qur'an says: **وَخَابَ كُلُّ جَبَّارٍ عَنِيدٍ**, \"and disappointed was every obstinate tyrant\" (14:15). A person has no right to force others by his own power, because he is not the owner of the power. When Allah is Al-Jabbar, it is praise, because every one of the three meanings is true of Him without any injustice."],
    related="جَبْر — mending; compelling · جَبِيرَة — a splint · إِجْبَار — compulsion · جَبَرُوت — might, majesty",
    quran=[
        dict(ayah=ayah(59, 23, words=(12, 15), tr="\"...the Exalted in Might, the Compeller, the Superior.\""), note=[
            "Look at the neighbours of this Name: Al-'Aziz before it, Al-Mutakabbir after it. This is the side of Allah that stops tyrants. Nothing He decides can be resisted."]),
        dict(ayah=ayah(94, 5, 6), note=[
            "And this is the other face of the same Name. The One who has overwhelming power is the One who sets right a heart that has been broken by difficulty. Ease does not come after hardship by accident; it comes with it, by His mending."])],
    hadith=[dict(ar="اللَّهُمَّ رَبَّ النَّاسِ أَذْهِبِ الْبَأْسَ، اشْفِ أَنْتَ الشَّافِي، لَا شِفَاءَ إِلَّا شِفَاؤُكَ، شِفَاءً لَا يُغَادِرُ سَقَمًا",
                 en="\"O Allah, Lord of mankind, remove the hardship. Heal, for You are the Healer; there is no healing except Your healing — a healing that leaves no illness behind.\" The Prophet ﷺ would say this over the sick.",
                 ref="Sahih al-Bukhari 5675; Sahih Muslim 2191")],
    essence="Al-Jabbar is the One who mends the broken and restores the wounded, whose will cannot be resisted, and who is high above every creature.",
    essence_ur=["الْجَبَّار وہ ذات ہے جو ٹوٹی ہوئی چیز کو جوڑنے اور", "سنوارنے والی ہے، جس کی مرضی کو کوئی روک نہیں سکتا", "اور جو ہر مخلوق سے بلند ہے۔"],
    servant=[
        "Every person has something in them that is broken: a loss that did not heal, a failure that stays in the memory, a relationship that fell apart, a sin that feels too heavy. The world can only cover these. Al-Jabbar can set them right. The same hand that no one can resist is the hand that is gentle with the broken.",
        "So bring Him the exact place where you are cracked. Do not tidy it up first. Ask Him to mend it, and trust that He who commands the heavens has not forgotten how to restore a human heart."],
    question="What is the broken place you have been carrying alone, which you have not yet handed to the One who mends?"))

# ------------------------------------------------------------------ 10 Al-Mutakabbir
N.append(dict(
    n=10, ar="الْمُتَكَبِّرُ", name_ar="الْمُتَكَبِّرُ", tr="Al-Mutakabbir", en="The Supreme in Greatness",
    ur="بڑائی اور عظمت کا حقیقی مالک",
    root="ك ب ر", root_ar="الْكِبَرُ وَالْعِظَمُ وَالْعُلُوُّ",
    root_en="— greatness in size, rank and standing; being exalted above others.",
    pattern=dict(ar="مُتَفَعِّل", bullets=[
        "This is the form that describes someone who takes on a quality and shows it. For a human being, تَكَبَّرَ means to show a greatness that he does not truly have. That is why it is blameworthy for people.",
        "For Allah the same word is praise, because His greatness is not a display. It is simply true. He is the only one who is actually great.",
        "So the one is claiming something he does not own; the other is declaring what is fully His."]),
    defbox="الْمُتَكَبِّرُ → The One who is truly supreme in greatness, above every flaw and every creature.",
    after_def=["Scholars also explain that Al-Mutakabbir is the One who is far above the evil and the faults that creatures fall into; He is too great to need anything or to be unjust to anyone."],
    related="كِبْرِيَاء — grandeur · كَبِير — great · أَكْبَر — greater · تَكْبِير — declaring Allah's greatness",
    quran=[
        dict(ayah=ayah(45, 37, tr="\"And to Him belongs all grandeur within the heavens and the earth, and He is the Exalted in Might, the Wise.\""), note=[
            "**وَلَهُ الْكِبْرِيَاءُ** — grandeur belongs to Him. Not to the king, not to the rich, not to the clever. The ayah puts all of it in one place."]),
        dict(ayah=ayah(7, 146, words=(0, 9), tr="\"I will turn away from My signs those who are arrogant upon the earth without right.\""), note=[
            "And this is what happens to the person who takes for himself what only belongs to Allah. The sign that pride brings is not only punishment later; it is blindness now. The arrogant person cannot see the truth even when it is shown to him."])],
    hadith=[dict(ar="الْكِبْرُ بَطَرُ الْحَقِّ وَغَمْطُ النَّاسِ",
                 en="The Prophet ﷺ said: \"No one who has an atom's weight of pride in his heart will enter Paradise.\" And he defined it: \"Pride is rejecting the truth and looking down on people.\"",
                 ref="Sahih Muslim 91",
                 note=["In a hadith qudsi, Allah says that might is His lower garment and pride is His cloak, and whoever contends with Him over them, He will punish (Sahih Muslim 2620). Greatness is the one thing He has not shared with anyone."])],
    essence="Al-Mutakabbir is the One whose greatness is absolute and real, above every creature and every fault. No one else has any share in it.",
    essence_ur=["الْمُتَکَبِّر وہ ذات ہے جس کی بڑائی اور عظمت", "حقیقی اور مطلق ہے، جو ہر مخلوق اور ہر عیب سے بلند", "ہے؛ اس میں کسی اور کا کوئی حصہ نہیں۔"],
    servant=[
        "This Name is mostly a warning for us, and a quiet relief. The warning: the Prophet ﷺ defined pride in two clear parts. Refusing the truth because it came from someone you did not like, or because it would cost you your standing, is pride. And looking down on people, because of lineage, degree, income, looks or even your own religious practice, is pride. It can hide inside a very pious-looking person.",
        "The relief: you do not have to carry greatness. You are not the one who has to be impressive. The only one who is truly great is Allah, and the closer you come to Him the smaller your need to prove anything. Bow in sujud, and know that the place where you are lowest is the place where you are nearest."],
    question="Is there a truth you have been avoiding, or a person you have been looking down on, because of pride?"))

# ------------------------------------------------------------------ 11 Al-Khaliq
N.append(dict(
    n=11, ar="الْخَالِقُ", name_ar="الْخَالِقُ", tr="Al-Khaliq", en="The Creator & Planner of All Things",
    ur="ہر چیز کو اندازے اور حکمت کے ساتھ پیدا کرنے والا",
    root="خ ل ق", root_ar="التَّقْدِيرُ وَالْإِيجَادُ",
    root_en="— measuring and proportioning something, and bringing it into being.",
    intro=["Al-Raghib al-Isfahani explains in his dictionary of the Qur'an that the base of this root is to measure something exactly, to give it a precise proportion. Creation, in this sense, is not a random act. It is the bringing into existence of something that was first measured and planned.",
           "And from the same root comes **خُلُق**, character: the inner shape of a person. Allah did not only shape your outer form; He also created the nature inside you."],
    pattern=dict(ar="فَاعِل", bullets=[
        "This is the active participle: the one who is doing the action.",
        "So Al-Khaliq is the One who is, constantly and in every moment, the Creator. Creation is not something that He did once and then stopped; He is still the Creator of everything that comes to exist."]),
    defbox="الْخَالِقُ → The One who plans, measures and brings everything into existence, from nothing and without an example to follow.",
    after_def=["This Name will be explained together with Al-Bari' and Al-Musawwir in the chapter that follows Name 13, because the Qur'an places all three side by side in a single ayah."],
    related="خَلْق — creation · مَخْلُوق — created being · خُلُق — character · خَلَّاق — Creator, again and again",
    quran=[
        dict(ayah=ayah(59, 24), note=[
            "This is the ayah of the three Names that this chapter belongs to. Immediately after them, the Qur'an says **لَهُ الْأَسْمَاءُ الْحُسْنَى**, \"to Him belong the best names,\" and that everything in the heavens and the earth glorifies Him."]),
        dict(ayah=ayah(13, 16, words=(37, 45), tr="\"Say, 'Allah is the Creator of all things, and He is the One, the Prevailing.'\""), note=[
            "**خَالِقُ كُلِّ شَيْءٍ** — Creator of all things. And a thing is not only a mountain or a star. Your thoughts, your abilities, your very free choices are all created. The ayah leaves nothing out."]),
        dict(ayah=ayah(35, 3, words=(6, 21), tr="\"Is there any creator other than Allah who provides for you from the heaven and earth? There is no deity except Him, so how are you deluded?\""), note=[
            "The Qur'an asks a question that has no answer except one: is there anyone else who created you?"])],
    hadith=[dict(ar="", en="The Prophet ﷺ said: \"Allah wrote down the measures of all creation fifty thousand years before He created the heavens and the earth.\"",
                 ref="Sahih Muslim 2653",
                 note=["That is the root meaning of this Name in a single sentence: measured first, created after. Nothing in your life was left to accident."])],
    essence="Al-Khaliq is the One who plans, measures and brings everything into being. Every created thing is His work, and nothing exists except by Him.",
    essence_ur=["الْخَالِق وہ ذات ہے جو ہر چیز کو اندازے اور", "حکمت کے ساتھ پیدا کرتی ہے؛ کائنات کی ہر شے", "اسی کی تخلیق ہے اور اس کے بغیر کچھ موجود نہیں۔"],
    servant=[
        "You are not an accident. You were measured before you were made: your height, your face, your voice, the time you were born into and the people you were given. A person who knows this stops comparing himself with others as if one of them got the better plan.",
        "It also means that you do not have to create your own worth. It was given to you with your existence. The One who created you in the best form (95:4) does not make worthless things."],
    question="If the One who created you planned you with care, what exactly are you still trying to prove?"))

# ------------------------------------------------------------------ 12 Al-Bari'
N.append(dict(
    n=12, ar="الْبَارِئُ", name_ar="الْبَارِئُ", tr="Al-Bari'", en="The Originator, Maker of Each Distinct",
    ur="عدم سے وجود میں لانے والا، ہر مخلوق کو الگ اور کامل بنانے والا",
    root="ب ر أ", root_ar="خُلُوصُ الشَّيْءِ مِنَ الشَّيْءِ",
    root_en="— a thing being brought forth, set apart and free from what it was not.",
    intro=["This root carries a lovely cluster of meanings. **بَرَأَ** is to create and bring forth. **بَرَأَ** is also to recover from an illness, to become free of it. And **بَرَاءَة** is innocence, being cleared of a charge. In all of them, something is separated cleanly from what it was before or from what attached to it."],
    pattern=dict(ar="فَاعِل", bullets=[
        "Like Al-Khaliq, this is the active participle: He is the continual doer of this act.",
        "Al-Bari' is the One who brings each creature into existence as its own distinct being, complete and sound, set apart from everything else.",
        "Even the word for creation in the Qur'an, **بَرِيَّة**, comes from this root (98:6)."]),
    defbox="الْبَارِئُ → The One who brings each creature into existence, distinct and complete, free of any flaw in His work.",
    related="بَرِيَّة — creation · بَرَاءَة — innocence; freedom from · بُرْء — recovery · مَبْرُوء — that which is brought forth",
    quran=[
        dict(ayah=ayah(2, 54, words=(10, 13), tr="\"So repent to your Bari' [Creator]...\""), note=[
            "This is Musa speaking to his people after they worshipped the calf. He did not say \"turn to your Lord\" in general. He said **بَارِئِكُمْ**: turn back to the One who brought you into being. The very Name is the argument. The one who made you knows exactly how to forgive you."]),
        dict(ayah=ayah(57, 22), note=[
            "Here the verb **نَبْرَأَهَا** appears: \"before We bring it into being.\" Every hardship that reaches the earth or you was written before it existed. This is Al-Bari': nothing is brought into existence without His knowledge. That does not remove your effort, but it removes your panic."])],
    essence="Al-Bari' is the One who brings every creature into being, distinct and complete, from nothing and by His will alone.",
    essence_ur=["الْبَارِئ وہ ذات ہے جو ہر مخلوق کو عدم سے وجود", "میں لاتی ہے، اسے الگ شناخت اور کامل صورت میں", "پیدا کرتی ہے، اور یہ سب صرف اس کی مرضی سے ہے۔"],
    servant=[
        "Your being is not a copy. Among billions of people, no two faces, voices or fingerprints are the same, and no one else has ever stood in exactly your place. That is the work of Al-Bari': each one brought forth distinct.",
        "And the word for recovery and the word for being cleared of a charge come from the same root. When you turn back to the One who brought you out of nothing, you are turning to the One who can also bring you out of guilt, out of sickness and out of despair."],
    question="Do you honour the one-of-a-kind creature that Allah brought forth when He made you?"))

# ------------------------------------------------------------------ 13 Al-Musawwir
N.append(dict(
    n=13, ar="الْمُصَوِّرُ", name_ar="الْمُصَوِّرُ", tr="Al-Musawwir", en="The Fashioner of Every Form",
    ur="ہر مخلوق کو صورت اور شکل دینے والا",
    root="ص و ر", root_ar="الشَّكْلُ وَالْهَيْئَةُ",
    root_en="— shape, form and appearance; giving something its particular image.",
    pattern=dict(ar="مُفَعِّل", bullets=[
        "The doubled middle letter gives intensity and detail: not simply giving a shape, but shaping with care.",
        "Al-Musawwir is the One who gives each creature its specific form, its features, its proportions and its look, exactly as He wills.",
        "Where Al-Bari' brings the creature out as a distinct being, Al-Musawwir gives that being its particular face."]),
    defbox="الْمُصَوِّرُ → The One who fashions every creature in its own specific form, exactly as He wills.",
    related="صُورَة — form, image · تَصْوِير — shaping · صُوَر — forms (plural) · مُصَوَّر — that which is shaped",
    quran=[
        dict(ayah=ayah(3, 6), note=[
            "**يُصَوِّرُكُمْ فِي الْأَرْحَامِ** — He shapes you in the wombs. The same word رَحِم that we met in Ar-Rahman and Ar-Raheem. In the darkest place, where no human hand can reach and no eye can see, Al-Musawwir is shaping a face. And the ayah says **كَيْفَ يَشَاءُ**: however He wills. No one chose their own face."]),
        dict(ayah=ayah(82, 6, 8), note=[
            "Look at the question the Qur'an asks: what has deceived you about your Generous Lord? Then it reminds us: He created you, proportioned you and balanced you, in whatever form He willed. Every human face is an argument for gratitude."]),
        dict(ayah=ayah(40, 64, words=(8, 11), tr="\"And He shaped you and perfected your forms.\""), note=[
            "**فَأَحْسَنَ صُوَرَكُمْ** — and He made your forms beautiful. Not average, not accidental: beautiful."])],
    hadith=[dict(ar="", en="The Prophet ﷺ said that each of us is gathered in his mother's womb for forty days as a drop, then a clot for forty days, then a lump of flesh for forty days; then an angel is sent, commanded to write his provision, his lifespan, his deeds, and whether he will be wretched or happy, and the soul is breathed into him.",
                 ref="Sahih al-Bukhari 3208; Sahih Muslim 2643")],
    essence="Al-Musawwir is the One who gives every creature its own form and features, shaping each exactly as He wills, in the wombs and in all creation.",
    essence_ur=["الْمُصَوِّر وہ ذات ہے جو ہر مخلوق کو اس کی مخصوص", "صورت اور شکل عطا کرتی ہے؛ رحموں میں اور پوری", "کائنات میں وہی جیسے چاہے صورت بناتا ہے۔"],
    servant=[
        "Your face is not your choice, but it is a gift with an author. When you look in the mirror and find something you wish were different, remember who drew it. And when you look at someone else and feel something that is not gratitude, remember that they were also fashioned by the same hands.",
        "The Prophet ﷺ taught us what matters beyond the form: *\"Allah does not look at your appearances or your wealth, but He looks at your hearts and your deeds\"* (Sahih Muslim 2564). The form is a gift from Al-Musawwir. The heart is what you offer back."],
    question="When you look at your own face, do you see an accident to be fixed, or a work of the One who fashioned it?"))


def trio_1113():
    o = [chapter_open("NAMES 11, 12 &amp; 13 — TOGETHER", "الْخَالِقُ الْبَارِئُ الْمُصَوِّرُ", "Al-Khaliq, Al-Bari' & Al-Musawwir",
                      "Three Names, One Ayah, One Complete Picture of Creation", None)]
    o.append(h2("1. Why They Come Together"))
    o.append(p("The Qur'an places these three Names side by side in one breath: *\"He is Allah, the Creator, the Inventor, the Fashioner; to Him belong the best names.\"* (Qur'an 59:24). They are not three repetitions. Each shows one side of the act of creating, and when you read them in order, you can follow a creature from its first measure to its final form."))
    o.append(box("الْخَالِقُ → He plans and brings into being.  |  الْبَارِئُ → He originates each one distinct.  |  الْمُصَوِّرُ → He gives each its form."))
    o.append(h2("2. What the Scholars Explain"))
    o.append(scholar("Ibn Kathir (tafsir of Surah al-Hashr)", None,
                     "Explains the three Names as stages of one act: Al-Khaliq is the One who plans and decrees what He wishes to bring into being; Al-Bari' is the One who brings it into existence according to that plan; Al-Musawwir is the One who gives it the form and shape He wills."))
    o.append(scholar("Al-Raghib al-Isfahani", None,
                     "Explains that the root of khalq is exact measuring and proportioning, which is why Al-Khaliq carries the sense of planning before bringing into being."))
    o.append(h2("3. Where They Differ"))
    o.append(table(["", "Al-Khaliq", "Al-Bari'", "Al-Musawwir"], [
        ["Pattern", "فَاعِل — active", "فَاعِل — active", "مُفَعِّل — intensive"],
        ["Root idea", "Measuring and proportioning", "Bringing forth, distinct and free", "Shape and form"],
        ["Stage", "The plan and the decree", "The coming into being", "The final form and features"],
        ["Seen in", "Everything created, with purpose", "Each creature as its own individual", "Every face and every body"]]))
    o.append(h2("4. One Picture, Three Moments"))
    o.append(p("Human examples are limited, and Allah's is the highest example (Qur'an 16:60), but a picture can still help the heart. Think of a craftsman. First he studies the measure and designs the work; that is the idea behind **Al-Khaliq**. Then the work comes into being as a separate thing; that is **Al-Bari'**. Then comes the detail: the lines of the face, the colour, the finish; that is **Al-Musawwir**. And Allah is beyond any comparison. He needs no tools, no material and no time."))
    o.append(p("The Qur'an itself walks through these stages in the womb: *\"Then We made the sperm-drop into a clinging clot, and We made the clot into a lump, and We made from the lump bones, and We covered the bones with flesh; then We developed him into another creation. So blessed is Allah, the best of creators.\"* (Qur'an 23:14). And then: *\"It is He who forms you in the wombs however He wills\"* (3:6). The womb again, the same رَحِم that carries the Names Ar-Rahman and Ar-Raheem. The place where mercy and creation meet."))
    o.append(h2("5. Essence Together"))
    o.append(essence("Al-Khaliq plans it, Al-Bari' brings it forth, Al-Musawwir shapes it. Nothing exists, and no face is the face it is, except by Him."))
    o.append(h2("6. For You, the Servant"))
    o.append(p("**Before you were anything.** There was a plan for you before you were a thought in anyone's mind. **While you were nothing.** You were brought out of nothing, distinct and complete. **When you took form.** You were shaped in a place no one could see, in a face that no one chose. Three Names, and you stand at the end of all of them. So the question is not whether you have a reason to be grateful; it is how long you will wait before you start."))
    o.append(chapter_close())
    return "\n".join(o)


ALL = N
