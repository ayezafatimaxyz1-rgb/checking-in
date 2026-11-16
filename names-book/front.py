"""Title page, introduction, contents, 33-at-a-glance summary and sources page."""
from lib import *
import lib, html


def title_page():
    r = lambda s: html.escape(raw(s))
    if lib.LANG == "ur":
        return ('<section class="chapter title-page"><div class="eyebrow" style="margin-top:0">اسماءُ اللہ الحسنیٰ</div>'
                '<div class="ar-title" dir="rtl" style="font-size:44pt;margin-top:22pt">أَسْمَاءُ اللَّهِ الْحُسْنَىٰ</div>'
                '<div class="tr">Asma\' Allah al-Husna</div>'
                '<div class="en urmain">اللہ تعالیٰ کے ننانوے ناموں کی تفہیم</div>'
                '<div class="subm">حصہ اول: نام 1 تا 33</div>'
                '<div class="rule"></div>'
                '<p style="text-align:center;color:var(--maroon);margin:0 0 4pt 0">مادہ اور معنی &nbsp;·&nbsp; قرآنی تعلق</p>'
                '<p style="text-align:center;color:var(--maroon);margin:0">خلاصہ &nbsp;·&nbsp; بندے کے لیے پیغام</p>'
                '</section>')
    return ('<section class="chapter title-page"><div class="eyebrow" style="margin-top:0">THE 99 NAMES OF ALLAH</div>'
            '<div class="ar-title" dir="rtl" style="font-size:40pt;margin-top:22pt">أَسْمَاءُ اللَّهِ الْحُسْنَىٰ</div>'
            '<div class="tr">Asma\' Allah al-Husna</div>'
            '<div class="en">Part One: Names 1 to 33</div>'
            '<div class="ur" dir="rtl">اللہ تعالیٰ کے خوبصورت ناموں کی تفہیم</div>'
            '<div class="rule"></div>'
            '<p style="text-align:center;font-style:italic;color:var(--maroon);margin:0 0 4pt 0">Root &amp; Meaning &nbsp;·&nbsp; Qur\'anic Connection</p>'
            '<p style="text-align:center;font-style:italic;color:var(--maroon);margin:0">Essence &nbsp;·&nbsp; For You, the Servant</p>'
            '</section>')


def intro_page():
    o = [f'<section class="chapter"><div class="eyebrow" style="margin-top:6pt">{raw("BEFORE YOU BEGIN")}</div>']
    o.append(h2("The Beautiful Names"))
    o.append(ayah_box(ayah(7, 180, words=(0, 5), tr="\"And to Allah belong the best names, so invoke Him by them.\"")))
    o.append(hadith_box("إِنَّ لِلَّهِ تِسْعَةً وَتِسْعِينَ اسْمًا، مِائَةً إِلَّا وَاحِدًا، مَنْ أَحْصَاهَا دَخَلَ الْجَنَّةَ",
                        "The Prophet ﷺ said: \"Allah has ninety-nine names, one hundred less one. Whoever preserves them will enter Paradise.\"",
                        "Sahih al-Bukhari 2736; Sahih Muslim 2677"))
    o.append(p("Scholars explain that to \"preserve\" the Names (**إِحْصَاء**) is more than counting them. It has levels: to memorise them, to understand their meanings, and to call upon Allah by them, and to let them change how we live. This book is written for the second and the third."))
    o.append(h2("How Each Name Is Studied"))
    o.append(bullets([
        "**Root Word & Meaning.** The Arabic root, the pattern the Name is built on, and what that tells us. Many Names share a pattern, so you will begin to recognise them.",
        "**Qur'anic Connection.** Where the Name appears in the Qur'an, with the ayah itself, and where it is authentic, the words of the Prophet ﷺ.",
        "**Essence of the Name.** The meaning gathered into a few lines, in English and in Urdu.",
        "**For You, the Servant.** What the Name asks of the person who knows it."]))
    o.append(p("Some Names are explained together in a chapter of their own, because the Qur'an itself places them side by side: Ar-Rahman and Ar-Raheem; Al-Khaliq, Al-Bari' and Al-Musawwir; and the pairs Al-Qabid and Al-Basit, Al-Khafid and Ar-Rafi', Al-Mu'izz and Al-Mudhill."))
    o.append("</section>")
    return "\n".join(o)


def contents_page(items):
    """items: list of (num_label, title, arabic, page) ; page may be '' on first pass."""
    o = [f'<section class="chapter"><div class="eyebrow" style="margin-top:6pt">{raw("CONTENTS")}</div>']
    o.append('<ul class="toc" style="margin-top:14pt">')
    for num, title, ar, page in items:
        o.append(f'<li><span class="tn">{num}</span><span class="tt">{md(title)}</span><span class="dots"></span>'
                 f'<span class="ta" dir="rtl">{ar}</span><span class="tp">{page}</span></li>')
    o.append("</ul></section>")
    return "\n".join(o)


def glance_page(rows):
    o = [f'<section class="chapter"><div class="eyebrow" style="margin-top:6pt">{raw("REVIEW")}</div>']
    o.append(h2("The First 33 at a Glance"))
    o.append(p("A quick page to revise. Say each Name, recall its meaning, and recall the one ayah that holds it.", "note"))
    o.append(f'<table class="tbl glance"><thead><tr><th>#</th><th>{raw('Name')}</th><th>{raw('Meaning')}</th></tr></thead><tbody>')
    for n, ar, tr, en in rows:
        o.append(f'<tr><td class="k" style="width:9%">{n}</td><td style="width:40%"><i>{md(tr)}</i> &nbsp; <span class="a" dir="rtl">{ar}</span></td><td>{md(en)}</td></tr>')
    o.append("</tbody></table></section>")
    return "\n".join(o)


def sources_page():
    o = [f'<section class="chapter"><div class="eyebrow" style="margin-top:6pt">{raw("NOTES")}</div>']
    o.append(h2("Sources & Notes"))
    o.append(h3("The Qur'an"))
    o.append(p("Arabic text: the Uthmani script from The Noble Qur'an Encyclopedia (quranenc.com), as distributed in the open-source quran-json dataset (CC BY-SA 4.0). English: the Saheeh International translation, as distributed by Tanzil.net, with light edits for flow where an ayah is quoted in part. Every verse in this book is set from that source, not typed from memory.", "note"))
    o.append(h3("The Hadith"))
    o.append(p("References give the collection and the hadith number in the common numbering (for Sahih Muslim, the numbering of Muhammad Fu'ad 'Abd al-Baqi). Grades are given where the collection or a recognised scholar states one. Before sharing the book widely, have each reference checked against the primary collection by a qualified teacher.", "note"))
    o.append(h3("The list of 99"))
    o.append(p("The sahih hadith says that Allah has ninety-nine names (Bukhari 2736, Muslim 2677). The specific list that this book follows comes from the narration of Jami' at-Tirmidhi (3507). Many scholars note that the enumeration in that narration is a narrator's addition, not the words of the Prophet ﷺ, and that the Names of Allah are not limited to ninety-nine, as in the du'a recorded in the Musnad of Imam Ahmad: *\"I ask You by every name that is Yours, by which You named Yourself, or taught to any of Your creation, or revealed in Your Book, or kept to Yourself in the knowledge of the unseen with You.\"* Scholars have also differed over a small number of the Names in this list; that is why Al-Qabid, Al-Basit, Al-Khafid, Ar-Rafi', Al-Mu'izz and Al-Mudhill are always read together as pairs.", "note"))
    o.append(h3("The explanations"))
    o.append(p("The meanings of the roots and patterns draw on the classical works of language and tafsir, in particular Ibn Faris (Maqayis al-Lugha), al-Raghib al-Isfahani (al-Mufradat), al-Tabari, Ibn Kathir, al-Ghazali (al-Maqsad al-Asna) and Ibn al-Qayyim. They are summaries in simple English, not direct quotations, unless they are placed in quotation marks. The reflections under \"For You, the Servant\" are the author's own and are offered as reminders, not as rulings.", "note"))
    o.append(h3("A note on language"))
    o.append(p("Whenever the Names speak of Allah's hearing, seeing, hand, or anything similar, they are affirmed as Allah has described Himself, in a way that befits His majesty and without comparing Him to His creation: *\"There is nothing like Him, and He is the All-Hearing, the All-Seeing\"* (Qur'an 42:11). The pictures used in this book (a craftsman, a judge, a helmet) are only to help the heart understand, and Allah's is the highest example (16:60).", "note"))
    o.append("</section>")
    return "\n".join(o)
