from random import randint

# Фун-я осуществляет сдвиг на заданную позиция, используется кодировка utf-8. Алгоритм шифр Цезаря.
def caesar(text, step):
    if step <= 0:
        return text
    # Если сдвиг превышает длинну алфавита.
    if step > 26:
        step = step % 26

    result = chr(96 + step)  # Кодируем шаг в сообщение

    for char in text:

        if 64 < ord(char) < 91:
            cod = ord(char) + step
            if cod > 90:  # Движение по кругу
                cod -= 26
        elif 96 < ord(char) < 123:
            cod = ord(char) + step
            if cod > 122:  # Движение по кругу
                cod -= 26
        else:
            cod = ord(char)

        char = chr(cod)
        result += char

    return result


# Фун-я для обработки текста. Заменяет символы на текст и приводит все к нижнему регистру.
def processing_text(text):
    result = ""
    number = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
              0: 'zero'}

    sign = {'.': 'point', ',': 'comma', '?': 'question', '!': 'exclamation', '-': 'minus', '+': 'plus', '=': 'equally',
            '*': 'star', '/': 'slash', '\\': 'reversl', ' ': 'space', ':': 'colon', '%': 'percent'}

    text = text.lower()

    for char in text:
        if char in '1234567890':
            key = int(char)
            char = number[key]
        elif char in '.,?!-+=*/\\: %':
            char = sign[char]
        result += char
    return result


# Фун-я разбивает текст на фрагменты указанной длинны ( по умолчанию 2).
def defragmentation_text(text, frg=2):
    balans = len(text) % frg  # Проверка на длинну фрагментов
    mark = 0
    fragments = []

    if balans == 0:
        # Процесс разбиения на фрагменты
        for i in range(0, len(text), frg):
            fragments.append(text[mark:i + frg])
            mark += frg
        balans = frg
    else:
        # Добивание текста случайными символами до необходимой длинны фрагмента
        for i in range(frg - balans):
            char = chr(randint(97, 122))
            text += char

        # Процесс разбиения на фрагменты
        for i in range(0, len(text), frg):
            fragments.append(text[mark:i + frg])
            mark += frg

    # Формируем пакет где  указывает кол-во добавленных символов и добавляем случайный элемент
    paket = chr(97 + (frg - balans))
    paket += chr(randint(97, 122))
    fragments.append(paket)

    return fragments


# Фун-я для смешивания пакетов принимает шаг смешивания step и начальную позицию start
def mixer(fragments, step=1, start=0):
    step = int(step)

    if step <= 0 or step >= int(len(fragments) / 2) or len(fragments) <= 2:
        paket = chr(97 + step)                # Кодируем шаг
        paket += chr(97 + start)              # Кодируем шаг
        paket += chr(97 + len(fragments[0]))  # Кодируем длинну фрагмента
        fragments.insert(0, paket)
        return fragments
    else:
        try:
            end = fragments.pop()  # Последний фрагмент в смешивании не участвует ( фрагмент от  defragmentation_text).

            # Процесс смешивания
            for i in range(start, len(fragments), step + 1):
                buffer = fragments[i]
                fragments[i] = fragments[i + step]
                fragments[i + step] = buffer
        except IndexError:
            pass
        finally:
            fragments.append(end)
            paket = chr(97 + step)                # Кодируем шаг
            paket += chr(97 + start)              # Кодируем шаг
            paket += chr(97 + len(fragments[0]))  # Кодируем длинну фрагмента
            fragments.insert(0, paket)

        return fragments


# Фун-я для преобразования списка фрагментов в строку
def stick(fragments):
    text = ""
    for frg in fragments:
        text += frg
    return text


# Фун-я полноценного кодирования
def coding(text, step_caesar, longfrg=2, stepmix=1, startmix=0):
    text = processing_text(text)
    text = caesar(text, step_caesar)
    frag = defragmentation_text(text, longfrg)
    frag = mixer(frag, stepmix, startmix)
    text = stick(frag)
    return text
