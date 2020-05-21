import sys
import os
import ctypes
from crypt import coding, decoding


# Фу-я для ввода пути
def input_way():
    out = True
    while out:
        way = input('write way for coding file: ')
        if os.path.isfile(way):  # проверка, существует ли путь
            out = False
        else:
            print('this way did not find')
    return way


# проверка пути где будет хранится шифрованный файл
def chek_way(path):
    if os.path.isdir(path):
        way = path + 'message'
        if not os.path.isdir(way):  # если такой путь есть, не нужно его создавать
            os.makedirs(way)
    else:
        way = input_way()

    return way


# Фу-я читает данные с файла, шифрует и записывает в файл
def cod_file():
    # Проверка платформы
    OS = sys.platform
    if OS == 'win32':
        path = 'D:\\'
        separator = '\\'
    elif OS == 'linux':
        path = '/home/'
        separator = '/'
    else:
        print('Syste is unknown')
        sys.exit

    # Чтение, шифрование, записи
    way_write = chek_way(path)
    way_read = input_way()

    filer = open(way_read, 'r', encoding='utf-8')
    data = filer.read()

    rebus = coding.coding(data, 1)

    way_write = way_write + separator + 'rebus.txt'

    filew = open(way_write, 'w', encoding='utf-8')
    filew.write(rebus)

    filer.close()
    filew.close()

    # Добавляем для файла атрибут скрытый
    if separator =='\\':
        kernel32 = ctypes.windll.kernel32
        attr = kernel32.GetFileAttributesW(way_write)
        kernel32.SetFileAttributesW(way_write, attr | 2)


# Фу-я читает шифр, декодирует его и записывает в файл
def decod_file():
    # Проверка платформы
    OS = sys.platform
    if OS == 'win32':
        path = r'D:\message\rebus.txt'
        separator = '\\'

        # Убираем атрибут скрытый
        kernel32 = ctypes.windll.kernel32
        attr = kernel32.GetFileAttributesW(path)
        kernel32.SetFileAttributesW(path, attr ^ 2)
    elif OS == 'linux':
        path = r'/home/rebus.txt'
        separator = '/'
    else:
        print('Syste is unknown')
        sys.exit

    # Чтение, декодирование, запись
    filer = open(path, 'r', encoding='utf-8')
    data = filer.read()

    way = os.path.split(path)
    path = way[0] + separator + 'text.txt'

    text = decoding.decoding(data)

    filew = open(path, 'w', encoding='utf-8')
    filew.write(text)
    print(text)

    filer.close()
    filew.close()
