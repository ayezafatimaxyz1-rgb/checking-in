"""Names 1-3 and the Rahman/Raheem chapter, re-created from the supplied PDF (text kept as written)."""
from lib import *


def name1():
    o = [chapter_open("NAME 1 OF 99", "الرَّحْمٰنُ", "Ar-Rahman", "The Vastly & Abundantly Merciful",
                      "نہایت وسیع اور بے پایاں رحمت والا")]
    o.append(h2("1. Root Word & Meaning"))
    o.append(root_row("ر ح م", "الرِّقَّةُ وَالْعَطْفُ وَالرَّأْفَةُ",
                      "— tenderness, compassion, affection, mercy."))
    o.append(pattern_head("الرَّحْمٰنُ", "فَعْلَان"))
    o.append(bullets([
        "This pattern conveys شِدَّةٌ وَكَثْرَةٌ — intensity and abundance.",
        "So رَحْمٰن → immensely abundant and extensive mercy.",
        "It is not merely \"mercy\" — the form itself conveys the greatness and abundance of that mercy.",
        "Other words on this same pattern: غَضْبَان — intensely angry · عَطْشَان — intensely thirsty · جَوْعَان — intensely hungry. Each carries that same heightened, overflowing sense the bare root doesn't."]))
    o.append(box("الرَّحْمٰنُ → The One whose mercy is immensely abundant, vast and encompassing."))
    o.append(p("This mercy is **general and worldly** — it reaches every creature in this life, believer or disbeliever alike. Rain, provision, breath and health fall on both without distinction. That is the vastness of Ar-Rahman: mercy that does not first ask who deserves it."))
    o.append(related("رَحْمَة — mercy · رَحِيم — merciful · رَحِم — the womb · أَرْحَام — wombs, kinship · تَرَاحُم — mutual mercy"))
    o.append(h2("2. Qur'anic Connection"))
    o.append(ayah_box(ayah(55, 1, 2, tr="\"The Most Merciful, He taught the Qur'an.\"")))
    o.append(p("Remember what Ar-Rahman means — mercy at its most abundant, its most intense, its most overflowing. This is not a modest mercy. It is mercy carried by a Name built for vastness itself. And it is this very Ar-Rahman who says **عَلَّمَ الْقُرْآنَ** — He taught the Qur'an. He loved us with a love as immense as His own Name, and that love is what gave us the Qur'an."))
    o.append(p("His greatest blessing is that He taught us the Qur'an — before mentioning any other favour. His mercy did not merely give us life and provision; it gave us guidance and the path back to Him."))
    o.append(p("We so easily complain about what we lack in this world — a delay, a loss, a plan that didn't work out — while rarely pausing to weep with gratitude over the one gift that outweighs all of them: that Allah did not leave us to wander blindly, but gave us deen and the Qur'an to guide us. Seen through this lens, it is a strange thing indeed to grieve endlessly over what is temporary while remaining almost unmoved by the greatest mercy we have already been given."))
    o.append(hadith_box("الرَّاحِمُونَ يَرْحَمُهُمُ الرَّحْمٰنُ، ارْحَمُوا مَنْ فِي الْأَرْضِ",
                        "\"Those who show mercy will be shown mercy by Ar-Rahman. Show mercy to those on earth.\"",
                        "Jami' at-Tirmidhi 1924 — hasan sahih"))
    o.append(p("Know Ar-Rahman, receive His mercy, become merciful to others."))
    o.append(chapter_close())
    return "\n".join(o)


def name2():
    o = [chapter_open("NAME 2 OF 99", "الرَّحِيمُ", "Ar-Raheem", "The Especially & Continually Merciful",
                      "نہایت رحم فرمانے والا، اپنے بندوں پر خصوصی رحمت فرمانے والا")]
    o.append(h2("1. Root Word & Meaning"))
    o.append(root_row("ر ح م", "", "Same root as Ar-Rahman — الرِّقَّةُ، الْعَطْفُ، الرَّأْفَةُ — tenderness, compassion, affection, mercy."))
    o.append(pattern_head("الرَّحِيمُ", "فَعِيل"))
    o.append(bullets([
        "This pattern conveys a firm, established and continuing quality.",
        "So رَحِيم conveys: one characterised by mercy — continually and especially merciful.",
        "Ar-Rahman emphasises the **vastness** of mercy; Ar-Raheem highlights its **established, continual manifestation** toward those who receive it.",
        "Other words on this same pattern: كَرِيم — established generosity · عَلِيم — established knowledge · حَكِيم — established wisdom. Each names a quality so settled in its owner that it has become part of who they are."]))
    o.append(box("الرَّحِيمُ → The One who continually and especially bestows His mercy upon His servants."))
    o.append(p("Unlike Ar-Rahman's general mercy over all creation, this mercy is **particular and personal** — reserved especially for the believers, reaching them individually rather than falling on everyone alike."))
    o.append(related("رَحْمَة — mercy · رَحِم — the womb · الرَّحْمٰن — abundantly merciful"))
    o.append(h2("2. Qur'anic Connection"))
    o.append(ayah_box(ayah(33, 43, words=(10, 13), tr="\"And He is ever Merciful to the believers.\"")))
    o.append(p("Ar-Raheem's mercy does not merely surround us — it deals with us personally. When you repent, He receives your return; when you ask forgiveness, He forgives."))
    o.append(ayah_box(ayah(39, 53, words=(11, 100), tr="\"Indeed, Allah forgives all sins. Indeed, He is the All-Forgiving, the Especially Merciful.\"")))
    o.append(p("Your sin does not have to be the end of your relationship with Allah — you can return."))
    o.append(hadith_box("", "The Prophet ﷺ said, after seeing a woman desperately searching for her child and then embracing him: \"Allah is more merciful to His servants than this woman is to her child.\"",
                        "Sahih al-Bukhari 5999; Sahih Muslim 2754"))
    o.append(p("The image brings us back to the root: رَحِم → mother and child → intense care → mercy — but Allah's mercy toward His servants is far greater still."))
    o.append(chapter_close())
    return "\n".join(o)


def together12():
    o = [chapter_open("NAMES 1 & 2 — TOGETHER", "الرَّحْمٰنِ الرَّحِيمِ", "Ar-Rahman & Ar-Raheem",
                      "Differences, Equalities & What the Scholars Say", None)]
    o.append(h2("1. The Beautiful Connection: رَحِم — The Womb"))
    o.append(p("One of the most meaningful words from ر ح م is **رَحِم** — the womb, shared by both Names since both come from the same root. The womb is where a completely helpless and dependent child is surrounded by care before it can do anything for itself."))
    o.append(bullets(["The child cannot provide its own food.", "It cannot protect itself.", "It cannot ask for what it needs.",
                      "It cannot earn anything, or give anything in return.", "Yet it is continually nourished, protected, carried and sustained."]))
    o.append(p("This gives us the fundamental meaning behind ر ح م: **mercy is caring for, protecting, nourishing and providing for one who is dependent upon you.** We too are completely dependent upon Allah — unable to sustain our own existence, control our future, or guarantee the next moment. Yet He surrounds us with provision, protection, care and countless blessings."))
    o.append(p("But the picture deepens differently for each Name. Ar-Rahman's mercy is not merely an abstract quality; with Ar-Raheem, it is mercy that **reaches** the one being shown mercy. As Ibn al-Qayyim explains: *\"Ar-Rahman indicates the attribute established in Him, while Ar-Raheem indicates its connection to the one who receives mercy.\"*"))
    o.append(box("Ar-Rahman → His vast attribute of mercy.  |  Ar-Raheem → His mercy reaching His servant."))
    o.append(h2("2. What They Share"))
    o.append(p("Both Names come from the same root, ر ح م, and both carry the same seed meaning: tenderness, compassion, affection and mercy. Neither Name is mercy as a passing feeling — both describe mercy as Allah's enduring, active nature toward His creation."))
    o.append(h2("3. Where They Differ"))
    o.append(table(["", "Ar-Rahman", "Ar-Raheem"], [
        ["Pattern", "فَعْلَان — intensity & abundance", "فَعِيل — firm, established, continuing"],
        ["Scope", "Vast, general — reaches all creation, believer or not", "Particular, personal — especially the believers"],
        ["Nature", "The attribute of mercy itself", "That mercy reaching the one who receives it"],
        ["Best seen in", "Worldly provision — life, sustenance, guidance", "Personal return — forgiveness, repentance"]]))
    o.append(box("\"Ar-Rahman [is merciful] to all creation, while Ar-Raheem [is merciful] to the believers.\" These words of Al-'Arzami are the clearest statement of the general and particular distinction."))
    o.append(h2("4. What the Scholars Explain"))
    o.append(scholar("Ibn Faris", None, "Identifies the fundamental meaning of ر ح م as tenderness, compassion and mercy (الرِّقَّةُ وَالْعَطْفُ وَالرَّأْفَةُ) — the shared root beneath both Names."))
    o.append(scholar("Al-'Arzami", "الرحمن بجميع الخلق، الرحيم بالمؤمنين",
                     "\"Ar-Rahman [is merciful] to all creation, while Ar-Raheem [is merciful] to the believers.\" This is the clearest statement of the general and particular distinction."))
    o.append(scholar("Al-Qurtubi", "ذو الرحمة الذي لا نظير له فيها",
                     "\"The possessor of mercy for which there is no equal.\" He explains Ar-Raheem as the One who possesses mercy and bestows it upon those who receive it."))
    o.append(scholar("Al-Tabari", None, "Stresses that the two Names are not simply repetitions — each conveys a meaning the other does not fully convey."))
    o.append(scholar("Ibn al-Qayyim", "الرَّحْمٰنُ دَالٌّ عَلَى الصِّفَةِ الْقَائِمَةِ بِهِ سُبْحَانَهُ، وَالرَّحِيمُ دَالٌّ عَلَى تَعَلُّقِهَا بِالْمَرْحُومِ",
                     "\"Ar-Rahman indicates the attribute established in Him, while Ar-Raheem indicates its connection to the one who receives mercy.\" In short: Ar-Rahman is the attribute itself; Ar-Raheem is that mercy reaching the recipient."))
    o.append(h2("5. Why Both Names Appear Together"))
    o.append(p("This is why we say both Names in every rak'ah of salah, in Surah al-Fatiha — الرَّحْمٰنِ الرَّحِيمِ. Together they form a complete picture that neither gives alone: the vastness of His mercy, and its personal arrival to the one who seeks it."))
    o.append(h2("6. A Tadabbur of Surah al-Fatiha"))
    o.append(ayah_box(ayah(1, 2, 4, tr="\"Lord of the Worlds, the Most Merciful, the Especially Merciful, Master of the Day of Judgement.\"")))
    o.append(p("Look at these four descriptions together. They are not four separate, unrelated attributes listed one after another — notice how they naturally split into two pairs, each pair speaking to the same reality from two angles."))
    o.append(f'<div class="pair"><div class="m"><div class="pa" dir="rtl">رَبِّ الْعَالَمِينَ</div><div class="pl">{raw("LORD OF THE WORLDS")}</div></div><div class="g"><div class="pa" dir="rtl">الرَّحْمٰنِ</div><div class="pl">{raw("AR-RAHMAN")}</div></div></div>')
    o.append('<div class="card">' + p("**Rabb al-'Alameen** means Allah sustains every world, every realm, every creature that exists — nothing is outside His care.") +
             p("This is the pairing to notice closely: **'Alameen** (the worlds) carries the same worldly, all-encompassing reach as **Ar-Rahman**. Both terms describe the same scope from two directions. 'Alameen names *everyone who exists in this dunya* — believer and non-believer alike, every realm, every creature. Ar-Rahman names *the mercy that reaches all of them* — rain, food, breath, health, opportunity, given without first asking who deserves it. One tells you who receives; the other tells you what they receive. Neither excludes anyone in this worldly life, and each explains why the other is worded the way it is.") +
             p("So the pairing is: the One who is Lord over *all the worlds* is the same One whose mercy is *abundant and encompassing* — reaching every one of those worlds, in this life, right now.") + "</div>")
    o.append(f'<div class="pair" style="margin-top:12pt"><div class="g"><div class="pa" dir="rtl">الرَّحِيمِ</div><div class="pl">{raw("AR-RAHEEM")}</div></div><div class="m"><div class="pa" dir="rtl">مَالِكِ يَوْمِ الدِّينِ</div><div class="pl">{raw("MASTER OF THE DAY OF JUDGEMENT")}</div></div></div>')
    o.append('<div class="card">' + p("**Malik Yawm ad-Din** moves the scene from this world to the akhirah — the Day when everyone stands before Him.") +
             p("This matches Ar-Raheem, because Ar-Raheem's mercy is not the general mercy shown to all creation — it is the **continuing, particular** mercy shown to believers. And on the Day of Judgement, this distinction becomes final: it is **only the believers** who will be recipients of His mercy on that Day. The general mercy of the dunya (Ar-Rahman) does not carry over to everyone in the akhirah — but the special mercy of Ar-Raheem does, for those who believed.") +
             p("So the pairing is: the One who is Master of the Day *when mercy is no longer shown to all* is the same One whose Name, Ar-Raheem, was already telling you — in every rak'ah — that His continuing mercy was always reserved for those who turn to Him.") + "</div>")
    o.append(p("This is why the very next verse follows so naturally: *\"You alone we worship, and You alone we ask for help.\"*"))
    o.append(p("Think about what is actually at stake on that Day. Every worldly mercy you have ever known, the air, the food, your health, your ease, will mean nothing once you stand before Malik Yawm ad-Din. On that Day, the general mercy that once reached everyone stops reaching everyone. What remains is only the particular mercy of Ar-Raheem, and it belongs only to those who believed. There is no wealth to buy your way into it, no status to secure it, no one else who can carry it for you. The only thing that will matter is whether you were among those this mercy was reserved for."))
    o.append(p("And this is exactly why the believer says **only You** we worship, not \"You, among others.\" If He alone can grant what you need on the one Day that actually matters, then directing even a part of your worship, hope or reliance toward anything else is not a small compromise; it is hoping in something that was never going to be able to save you. Exclusive worship is not a demand Allah makes for His own sake; it is the only response that matches the reality of who actually holds your safety."))
    o.append(ayah_box(ayah(1, 5, tr="\"You alone we worship, and You alone we ask for help.\"")))
    o.append(p("Pull together everything above and one picture emerges from the Qur'an itself. Al-Fatiha places الرَّحْمٰنِ الرَّحِيمِ side by side in a single breath, and that pairing is not decoration; it is the whole architecture of the surah's opening. Rabb al-'Alameen introduces a Lord over every world, and Ar-Rahman immediately confirms the scale of that lordship: mercy poured over all of it, believer and disbeliever alike, in this life, right now. Then the scene turns. Malik Yawm ad-Din brings the Day itself into view, and Ar-Raheem is what is waiting there: not the general mercy anyone could receive, but the particular mercy reserved only for those who turned to Him."))
    o.append(p("One ayah outside the Fatiha confirms this with striking directness, the very first ayah Ar-Raheem's own chapter opened with:"))
    o.append(ayah_box(ayah(33, 43, words=(10, 13), tr="\"And He is ever Merciful to the believers.\"")))
    o.append(p("Look at exactly how the ayah is worded. It does not simply say Allah is Ar-Raheem and leave it there. It says **بِالْمُؤْمِنِينَ**, \"to the believers,\" naming who this mercy belongs to. Nothing forced that phrase into the verse; the ayah could easily have stopped at \"He is ever Merciful.\" Instead it specifies the recipient, and that specification is the same distinction this whole chapter has been building toward: Ar-Rahman needed no such qualifier because His mercy reaches everyone without exception, while Ar-Raheem is paired with al-mu'mineen because His continuing mercy does not. The wording of the ayah is not incidental. It is the Qur'an itself drawing the line between general and particular."))
    o.append(p("Living between these two Names is not complicated, though it asks something real of the heart. From Ar-Rahman, take the constant reminder that you are already surrounded by more than you earned: every breath, every meal, every ordinary day that continued without your permission. That is not owed to you. It is given."))
    o.append(p("From Ar-Raheem, take the reminder that this surrounding mercy is not the end of the relationship. It is an invitation into something closer: repentance that is actually received, weakness that is actually met with help, a return that is never once too late."))
    o.append(h3("When you feel unnoticed in a crowd of billions"))
    o.append(p("Ar-Rahman already sustains all of them, and Ar-Raheem still turns toward you individually.", "note"))
    o.append(h3("When you are grateful for something ordinary"))
    o.append(p("You are recognising Ar-Rahman.", "note"))
    o.append(h3("When you return to Allah after falling short"))
    o.append(p("You are experiencing Ar-Raheem.", "note"))
    o.append(p("The servant who knows both Names stops treating Allah's care as background noise and stops treating his own mistakes as disqualifying. He lives, instead, between abundance and return, certain that the same Lord who gives to everyone is the same Lord who is still, personally, waiting for him."))
    o.append(h2("7. Essence Together"))
    o.append(essence("Ar-Rahman is the vastness of mercy poured over all creation. Ar-Raheem is that same mercy, arriving personally to the one who turns to Him. One shows you how much He gives; the other shows you that He will not forget you."))
    o.append(h2("8. For You, the Servant"))
    o.append(p("**The Womb.** You came from a رَحِم. You lay there unable to feed yourself, protect yourself, or earn a single thing you were given, and still you were nourished, carried, kept alive. Nothing has changed since. You still cannot sustain your own existence. You are still held by the same kind of mercy, only now on a scale you were too small to notice the first time."))
    o.append(p("**Dunya and Akhira.** Right now, in your dunya, you are living inside Ar-Rahman: your breath, your food, the years you did not pay for. That much you have already been given, whether you asked for it or not. But your akhira is not automatic the same way. It waits on Ar-Raheem, and Ar-Raheem is only for those who turn back. So ask yourself plainly: are you only receiving from Ar-Rahman, or are you also returning to Ar-Raheem?"))
    o.append(chapter_close())
    return "\n".join(o)


def name3():
    d = dict(
        n=3, ar="الْمَلِكُ", tr="Al-Malik", en="The Absolute King & Sovereign", ur="مطلق بادشاہ اور حاکم",
        root="م ل ك", root_head="Base meaning:", root_ar="الْمُلْكُ، الْمِلْكُ، السُّلْطَانُ، الْقُدْرَةُ",
        root_en="— dominion, ownership, authority and power.",
        intro=["A human king may possess a kingdom, but his kingship is never absolute. Every dimension of it is limited:"],
        table=(["Dimension", "Human King", "Allah, Al-Malik"], [
            ["Ownership", "Owns the palace, not every person in it", "Owns everything, nothing excluded"],
            ["Authority", "Commands an army, not a single heart", "Nothing escapes His authority"],
            ["Power", "Limited by others, circumstance, death", "Nothing can overpower Him"],
            ["Duration", "His reign eventually ends", "His dominion does not end"]]),
        defbox="الْمَلِكُ, the One who possesses everything and has absolute authority and power over everything.",
        scholars=[("Al-Tabari", "الملك الذي له الملك", "\"The King to whom belongs dominion.\" Allah's command and sovereignty prevail over the whole of His creation."),
                  ("Ibn al-Qayyim", None, "Ties Allah's kingship to His absolute ownership, command and disposal of creation. Everything that exists belongs to Him and moves only by His command.")],
        related="مَلِك, king · مُلْك, kingdom, dominion · مَالِك, owner · مَلِيك, mighty king · عَبْد, servant",
    )
    o = [chapter_open("NAME 3 OF 99", d["ar"], d["tr"], d["en"], d["ur"])]
    o.append(h2("1. Root Word & Meaning"))
    o.append(root_row(d["root"], d["root_ar"], d["root_en"], d["root_head"]))
    o.append(p(d["intro"][0]))
    o.append(table(*d["table"]))
    o.append(box(d["defbox"]))
    for s in d["scholars"]:
        o.append(scholar(*s))
    o.append(related(d["related"]))
    o.append(h2("2. Qur'anic Connection"))
    o.append(ayah_box(ayah(3, 26, words=(0, 12), tr="\"Say: O Allah, Owner of Sovereignty, You give sovereignty to whom You will, and You take sovereignty away from whom You will.\"")))
    o.append(p("Look at exactly what this ayah proves. It does not simply call Allah the King. It says He gives kingship, تُؤْتِي الْمُلْكَ, and He takes it away, وَتَنزِعُ الْمُلْكَ, to whomever He wills. Every throne a human king has ever sat on was handed to him and can be removed from him, and neither the handing nor the removing was ever his own decision. This is the same \"Duration\" row from the table above, now stated directly in the Qur'an's own words: a human king's reign ends because it was never really his to keep."))
    o.append(p("This is why, immediately after describing Allah in al-Fatiha as مَالِكِ يَوْمِ الدِّينِ, Master of the Day of Judgement, the servant's very next words are:"))
    o.append(ayah_box(ayah(1, 5, tr="\"You alone we worship, and You alone we ask for help.\"")))
    o.append(h2("3. Essence of the Name"))
    o.append(essence("Al-Malik is the One who absolutely owns, possesses and rules everything, the King whose authority and power are unlimited, and before whom every human remains a servant.",
                     ["الْمَلِك وہ ذات ہے جو ہر چیز کی حقیقی مالک", "اور مطلق حاکم ہے؛ جس کی قدرت اور اقتدار", "کی کوئی حد نہیں، اور جس کے سامنے ہر انسان", "بندہ اور محتاج ہے۔"]))
    o.append(h2("4. For You, the Servant"))
    o.append(p("If Allah is Al-Malik, then you are not an independent owner. You are His عَبْد, His servant, and a servant lives under the authority of his master. Your body, your wealth, your abilities, the time you spend, all of it was only ever entrusted to you. You did not earn the right to keep any of it forever."))
    o.append(p("That should not make you feel small. If you have wealth, remember Al-Malik gave it. If you lose something, remember it belonged to Al-Malik before it ever touched your hands. If you are afraid of someone powerful, remember their power is also under His power. And when your own life feels out of your control, remember it was never in your control to begin with. It has always been His."))
    o.append(question("Are you still trying to own what was only ever lent to you, or have you settled into being a servant of the One who owns it all?"))
    o.append(chapter_close())
    return "\n".join(o)
