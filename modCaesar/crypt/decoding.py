# Фун-я для раскодирования шифра Цезаря
def revers_caesar(text):
    step = ord(text[0]) - 96  # Получаем сдвиг.
    text = text[1:]
    result = ""

    # Процесс раскодирования
    for char in text:

        if 64 < ord(char) < 91:
            cod = ord(char) - step
            if cod < 65:
                cod += 26
        elif 96 < ord(char) < 123:
            cod = ord(char) - step
            if cod < 97:
                cod += 26
        else:
            cod = ord(char)

        char = chr(cod)
        result += char
    return result


# Фун-я заменяет текст на символы
def processing_test(text):
    number = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
              '9': 'nine', '0': 'zero'}

    sign = {'.': 'point', ',': 'comma', '?': 'question', '!': 'exclamation', '-': 'minus', '+': 'plus', '=': 'equally',
            '*': 'star', '/': 'slash', '\\': 'reversl', ' ': 'space', ':': 'colon', '%': 'percent'}

    for key, val in number.items():
        if -1 != text.find(val):
            text = text.replace(val, key)

    for key, val in sign.items():
        if -1 != text.find(val):
            text = text.replace(val, key)

    return text


# Фун-я востановления порядка следования
def order(text):
    step = int(ord(text[0]) - 97)   # шаг смешивания
    start = int(ord(text[1]) - 97)  # стартовая позиция смешивания
    long = int(ord(text[2]) - 97)   # длинна фрагмента

    mark = 0
    text = text[3:]
    fragments = []

    # Разборка текста на фрагменты
    for i in range(0, len(text), long):
        frm = text[mark:i + long]
        fragments.append(frm)
        mark += long

    end = fragments.pop()  # Содержит информацию о кодировании

    # Востановление порядка следования фрагментов
    if step <= 0 or len(fragments) <= 2:
        pass
    else:
        try:
            for i in range(start, len(fragments), step + 1):
                buffer = fragments[i + step]
                fragments[i + step] = fragments[i]
                fragments[i] = buffer
        except IndexError:
            pass
    ballast = ord(end[0]) - 97  # проверка на лишние символы при кодировании
    if ballast == 0:
        return fragments
    else:
        fragments[-1] = fragments[-1][:-ballast]
        return fragments


# Фун-я для преобразования списка фрагментов в строку
def stick(fragments):
    text = ""
    for frg in fragments:
        text += frg
    return text


# Фнкция для раскодирования
def decoding(text):
    frag = order(text)
    text = stick(frag)
    text = revers_caesar(text)
    text = processing_test(text)
    return text
