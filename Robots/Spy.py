import hashlib
import random
import datetime

import OOP.Robots.Robot as Robot


class Spy(Robot.Robot):
    __open_key = []
    __close_key = []

    def __init__(self, name, type, mass, year, element, specialization):
        super().__init__(name, type, mass, year, element)
        self.__specialization = specialization

    @property
    def get_specialiazation(self):
        return self.__specialization

    @property
    def get_open_key(self):
        return self.__open_key

    # функция для отбражения характеристик объекта
    def pasport(self):

        check = True
        flag_time = False
        count = 0
        then = datetime.datetime.now()

        # на ввод пароля 3 попытки
        while (check and count < 3):

            password = input('write access code: ')
            hash_pas = hashlib.sha256(password.encode()).hexdigest()  # получаем хэш

            if '9b8769a4a742959a2d0298c36fb70623f2dfacda8436237df08d8dfd5b37374c' == hash_pas:

                now = datetime.datetime.now()
                delata = now - then
                if delata.seconds > 30:  # ввод должен занимать не более 30 секунт
                    check = False
                    flag_time = True
                    print('time is over')
                else:
                    super().pasport()
                    print('Specialization: ', self.__specialization)
                    check = False
            else:
                print('password is incorrect')
                count += 1

        # если попыток было или время больше 30с данные заносятся в файл
        if count >= 3 or flag_time:
            path = 'D:\python\log\log.txt'
            while True:
                try:
                    with open(path, 'a', encoding='utf-8') as file:
                        if flag_time:
                            file.write('\ntime is over {0}'.format(now))
                        else:
                            file.write('\nattempt is error {0}'.format(datetime.datetime.today()))
                        break
                except FileNotFoundError:
                    print('not found way')
                    path = input('Write way:')

    # ф-я для получения списка простых чисел
    def __generator_prime(self):
        count = 0
        number = 2
        prime = []

        while (count < 800):
            check = True
            for i in range(2, int(number / 2) + 2):
                if number % i == 0:
                    check = False
                    break

            if check:
                prime.append(number)
                count += 1

            number += 1
        prime = prime[10:]  # отбрасываем первые 10 значения (при малых значениях наблюдаются проблемы с кодировкой)
        print(prime)
        return prime

    # ф-я для получения открытой экспоненты ( требуется передать список простых чисел и фи )
    # должно быть простое, е< фи  и взаимно простое с фи
    def __open_exponent(self, lst, f):

        half = lambda ls: int(len(ls) / 2)

        if lst[half(lst)] < f:
            while (True):
                e = random.choice(lst[:half(lst)])
                if f % e == 0:
                    continue
                else:
                    return e
        else:
            half_lst = lst[: half(lst)]
            e = self.__open_exponent(half_lst, f)

        return e

    # ф-я для получения открытого и закрытого ключа
    def __create_keys(self):
        prime = self.__generator_prime()
        part_prime = prime[:int(len(prime) / 10)]  # обрезаем список что бы в последствии найти d
        key = True

        while (key):

            # выбираем числа p и q
            p = random.choice(part_prime)
            index = part_prime.index(p)
            if index + 2 < len(part_prime):
                q = part_prime[index + 2]
            else:
                q = part_prime[index - 2]

            mod = p * q  # вычисляем модуль

            fi = (p - 1) * (q - 1)  # вычисляем фун-ю Эйлера

            e = self.__open_exponent(part_prime, fi)

            # получаем d
            for i in prime:
                ch = (i * e) % fi
                if ch == 1 and i != e:
                    d = i
                    key = False
                    break
                else:
                    d = None

        self.__close_key = [d, mod]
        self.__open_key = [e, mod]

    # фу-я для кодирования
    def encryption(self, text):

        ls = list(text)  # разбиваем строку на символы

        self.__create_keys()

        e = self.__open_key[0]
        n = self.__open_key[1]

        # для кодирование возводим число в степень и берем остаток по модулю
        # избигаем работу с большими числами, берем остаток после каждого умножения
        for i in range(len(ls)):
            ls[i] = ord(ls[i])
            balance = 1
            for j in range(e):
                balance = balance * ls[i]
                if balance > n:
                    balance = balance % n
                    if balance == 0:
                        balance = 1

            ls[i] = chr(balance)

        path = 'D:\\shifr.txt'
        while True:
            try:
                with open(path, 'w', encoding='utf-8')  as file:
                    for i in ls:
                        file.write(i)
                    break
            except FileNotFoundError:
                print('not found way')
                path = input('Write way:')


        return ls

    # фу-я для декодирования
    def decryption(self):

        path = 'D:\\shifr.txt'
        while True:
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    string = file.read()
                    break
            except FileNotFoundError:
                print('not found way')
                path = input('Write way:')


        text = list(string)  # разбиваем строку на символы

        d = self.__close_key[0]
        n = self.__close_key[1]
        message = ""

        for i in range(len(text)):
            balance = 1
            text[i] = ord(text[i])
            for j in range(d):
                balance = balance * text[i]
                if balance > n:
                    balance = balance % n
                    if balance == 0:
                        balance = 1

            text[i] = chr(balance)
            message += text[i]

        return message
