# TODO  Напишите функцию count_letters
def count_letters(string):
    low_string = string.lower()
    list_ = []
    dict_symbols = {}
    for i in low_string:
        if i.isalpha():
            if i not in list_:
                list_.append(i)

    for j in list_:
        count = low_string.count(j)
        dict_symbols[j] = count
    return dict_symbols


def calculate_frequency(dict_symbols):
    dict_symbols_new = {}
    for sym, count_ in dict_symbols.items():
        frequency = count_ / sum(dict_symbols.values())
        dict_symbols_new[sym] = frequency
    return dict_symbols_new


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
slovar = count_letters(main_str)
# calculate_frequency(slovar)
new_slovar = calculate_frequency(slovar)
for symbol_, frequency_ in new_slovar.items():
    print(f"{symbol_}: {frequency_:.2f}")




