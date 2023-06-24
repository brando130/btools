##################################################################
# B-TOOLS-TRANSLATE v0.24
#
# Translate:
# translate(text, from_language, to_language, style)
#
# style = enum. Valid values: "ANTIQUATED, MODERN_LITERAL, MODERN_READABLE, MODERN_PARAPHRASE"
##################################################################

import btools_gpt
from enum import Enum
from typing import Union

class Style(Enum):
    ANTIQUATED = 0
    MODERN_LITERAL = 1
    MODERN_READABLE = 2
    MODERN_PARAPHRASE = 3

def translate(text, from_language, to_language="Modern English", style: Style=Style.MODERN_READABLE):
    
    translation_style = "ANTIQUATED"
    if style == Style.MODERN_LITERAL:
        translation_style = "MODERN_LITERAL"
    elif style == Style.MODERN_READABLE:
        translation_style = "MODERN_READABLE"
    elif style == Style.MODERN_PARAPHRASE:
        translation_style = "MODERN_PARAPHRASE"

    prompt = "Let's work to create a fresh, casually-readable, updated translation of a text. I will show you the original language text of a passage, and your task is to create a " + translation_style + " translation. Here is an example of what a " + translation_style + """ translation should look like:

---
Τὸ δὲ πνεῦμα ῥητῶς λέγει ὅτι ἐν ὑστέροις καιροῖς ἀποστήσονταί τινες τῆς πίστεως προσέχοντες πνεύμασιν πλάνοις καὶ διδασκαλίαις δαιμονίων ἐν ὑποκρίσει ψευδολόγων, κεκαυστηριασμένων τὴν ἰδίαν συνείδησιν, κωλυόντων γαμεῖν, ἀπέχεσθαι βρωμάτων ἃ ὁ θεὸς ἔκτισεν εἰς μετάλημψιν μετὰ εὐχαριστίας τοῖς πιστοῖς καὶ ἐπεγνωκόσι τὴν ἀλήθειαν. ὅτι πᾶν κτίσμα θεοῦ καλὸν καὶ οὐδὲν ἀπόβλητον μετὰ εὐχαριστίας λαμβανόμενον· ἁγιάζεται γὰρ διὰ λόγου θεοῦ καὶ ἐντεύξεως.

ANTIQUATED:

Now the Spirit speaketh expressly, that in the latter times some shall depart from the faith, giving heed to seducing spirits, and doctrines of devils; Speaking lies in hypocrisy; having their conscience seared with a hot iron; Forbidding to marry, and commanding to abstain from meats, which God hath created to be received with thanksgiving of them which believe and know the truth. For every creature of God is good, and nothing to be refused, if it be received with thanksgiving: For it is sanctified by the word of God and prayer.

MODERN_LITERAL:

But the Spirit explicitly says that in later times some will fall away from the faith, paying attention to deceitful spirits and teachings of demons, by means of the hypocrisy of liars seared in their own conscience as with a branding iron, who forbid marriage and advocate abstaining from foods which God has created to be gratefully shared in by those who believe and know the truth. For everything created by God is good, and nothing is to be rejected if it is received with gratitude; for it is sanctified by means of the word of God and prayer.

MODERN_READABLE:

The Spirit clearly says that in later times some will abandon the faith and follow deceiving spirits and things taught by demons. Such teachings come through hypocritical liars, whose consciences have been seared as with a hot iron. They forbid people to marry and order them to abstain from certain foods, which God created to be received with thanksgiving by those who believe and who know the truth. For everything God created is good, and nothing is to be rejected if it is received with thanksgiving, because it is consecrated by the word of God and prayer.

MODERN_PARAPHRASE:

The Spirit of God says very plainly that in later times some people will stop believing. They will listen to other spirits that fool them, and to the teaching of bad spirits. Men will tell lies and make people believe they are something when they are not. These men will have made their hearts so hard that they will not know they are doing wrong. They will teach people that they should not marry. They will teach them not to eat some kinds of food. God made the food and he wanted people to take it and thank him for it. Those who believe and know what is true do this. Everything that God has made for food is good. It is all right to eat it if people thank God for it. God’s word and asking him to bless the food makes it good for people to eat.

TRANSLATE THE FOLLOWING PASSAGE FROM """ + from_language + " TO " + translation_style + " " + to_language + ":\n\n" + text

    return btools_gpt.gpt(prompt, model="gpt-3.5-turbo-0613", system="You are a master translator focused on translating from " + from_language + " to " + to_language + " in the style of " + translation_style)
