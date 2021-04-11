hebrew_letters = ". אבגדהוזחטיכלמנסעפצקרשתםןץףך"
syriac_letters = ". ܐܒܓܕܗܘܙܚܛܝܟܠܡܢܣܥܦܨܩܪܫܬܡܢܨܦܟ"


def convert_text_from_hebrew(hebrew_string):
    syriac_string = ""
    for char in hebrew_string:
        alt_char = syriac_letters[hebrew_letters.index(char)] if char in hebrew_letters else char
        syriac_string += alt_char
    return syriac_string


def convert_text_from_syriac(syriac_string):
    hebrew_string = ""
    for char in syriac_string:
        alt_char = hebrew_letters[syriac_letters.index(char)] if char in syriac_letters else char
        hebrew_string += alt_char
    return hebrew_string


def replace_mid_form_to_final_form(sentence: str) -> str:
    mid_form = "מנצפכ"
    final_form = "םןץףך"
    words_list = sentence.split()
    fixed_words_list = list()
    for w in words_list:
        if w[-1] in mid_form:
            w = w[:-1] + w[-1].replace(w[-1], final_form[mid_form.index(w[-1])])
        fixed_words_list.append(w)
    return ' '.join(fixed_words_list)


def transliterate(message: str) -> str:
    if message[0] in hebrew_letters:
        return convert_text_from_hebrew(message)
    elif message[0] in syriac_letters:
        return replace_mid_form_to_final_form(convert_text_from_syriac(message))
    else:
        return "משהו כנראה השתבש, יש לכתוב טקסט בעברית או בסורית"
